# Capítulo 4 — Respuesta técnica a los Objetivos 1 y 2

## 4.0 Formulación de objetivos (reproducidos de §1.4 del manuscrito)

- **Objetivo General:** diseñar e implementar un framework basado en DDD-liviano con autogeneración de endpoints que reduzca el boilerplate en el desenvolvimiento de APIs REST.
- **OE1:** Analizar y cuantificar el código boilerplate presente en el desenvolvimiento convencional de APIs REST bajo DDD, identificando componentes con mayor replicación estructural.
- **OE2:** Diseñar la arquitectura del framework, definiendo mecanismos de autogeneración de controladores, servicios, repositorios, DTOs y mappers a partir del modelo de dominio.

---

## 4.1 Respuesta al Objetivo Específico 1: arquitectura metadata-first y pipeline

### 4.1.1 Tesis arquitectónica

Boilerfree adopta una arquitectura metadata-first: el dominio proclama la verdad a través de decoradores (`#[Entity]`, `#[Field]`, `#[Action]`, `#[Query]`, `#[HasMany]`, `#[ManyToMany]`, `#[Projected]`, `#[Queued]`, `#[Scheduled]`) y la infraestructura **deriva mecánicamente** el HTTP, la persistencia, la validación y la observabilidad a partir del snapshot `ClassMetadata`. esta desición elimina la transcripción manual del CRUD, los mappers y los DTOs desaparecidos en la capa de presentación.

Código seminal en `src/Core/Metadata/DomainScanner.php` (`scan()`, `referencedClasses()`): el scanner **no escanea por argumentos CLI ni YAML**; reflexiona el dominio por archivos PHP y descubrimos transitivamente las referencias por `@var` (fields/relations/parameters). La frontera se mantiene en los decoradores; sin ellos la clase es invisible.

### 4.1.2 Mecanismos de orquestación

| Componente | Función real | Archivo |
|---|---|---|
| MetadataEngine | Scan/validar/cache metadata; falla claro ante metadata inválida (RQ-META-003) | src/Core/Metadata/MetadataEngine |
| DomainScanner | Transitive discovery; colisión de rutas `D1` | src/Core/Metadata/DomainScanner.php |
| ClassMetadata | Modelo serializable de entidad/tabla/campos/acciones/queries/relaciones/version | src/Core/Metadata/ClassMetadata.php |
| Router | Construye rutas desde metadata + legal templates, detecta colisión METHOD-path | src/Core/Http/Router.php |
| Kernel | Boot único + dispatch único + `applyResponsePolicy` (CORS/cache/security headers), `X-Request-Id`, métricas, log estructurado | src/Core/Http/Kernel.php |
| CrudController | CRUD genérico parametrizado por metadata; hooks `may{Operacion}`, scoping, ETag desde versión real | src/Core/Http/CrudController.php |
| Hydrator/Validator | hydrate body → tipos; mini-DSL rules §14.5; errors 422 por campo | src/Core/Hydration/Hydrator.php, src/Core/Validation/Validator.php |
| PdoQuerySource | SQL por metadata, paginación, aggregates, joins, pivots, version token, lockRow, ping | src/Core/QuerySource/PdoQuerySource.php |
| VersionToken/TransactionRunner | Optimistic If-Match, pessimistic `FOR UPDATE`, retries, métrica `db.transaction_retries` | src/Core/Concurrency/* |
| Puertos | Infra container-first (Logger, Storage, Metrics, Cache, Queue, …) | src/Core/*/…Locator.php, …Port.php |
| Security | RouteAuthorizer, CSRF fail-closed, trusted proxies, ListingScopeResolver | src/Core/Security/*, Auth/* |

### 4.1.3 Pipeline exacto (`Kernel::dispatch()`)

Orden documentado en el propio código:

1. `normalizePath`
2. probes GET: `/healthz`, `/readyz`, `/metrics` — antes de limits
3. `enforceHttpLimits`
4. `MaintenanceMiddleware`
5. `boot()` lazy
6. query parse/attrs merge
7. OPTIONS preflight (solo si route existe)
8. router match (exacto → regex param)
9. route attrs merge
10. `RouteAuthorizer::authorizeRoute`
11. idempotency replay
12. CSRF (solo rutas `action`)
13. middleware registry + validación de nombres no registrados (500, no se omite)
14. ejecutor según `route->kind`
15. store idempotency
16. `applyResponsePolicy` (CORS + cache control)

Tras el dispatch: `withHeader('X-Request-Id')`, métricas `requests_total`/`request_duration_ms`, log `http_request`, y `security_headers` desde config en **toda** respuesta (incluidos early 404/408/413/503).

### 4.1.4 Decisiones de diseño (el "por qué")

- **Request id**: el valor entrante se retorna solo si match `/^[\x20-\x7E]+$/` y ≤128 bytes; en caso contrario se reemplaza por `random_bytes(16)`. Razón: un valor con newlines o control chars es header-splitting surface.
- **Fail-closed en CSRF**: si `SessionStore` no resuelve → 403 (no 404). El docstring mismo explica por qué no se minta token on-demand (man-in-the-middle + fuerza-de-legibilidad del token lado cliente).
- **Trusted proxies condicionales**: `getClientIp(array $trustedProxies)` usa solo el primer hop de `X-Forwarded-For` si `REMOTE_ADDR ∈ trustedProxies`, sino devuelve el peer directo. Protege contra IP forging cuando no estás detrás de proxy.
- **Idempotencia 422 semántica**: detecta `misma key + reruta ≠ 422` (422 `idempotency_key_reused` routes/payloads distinct) para prevenir doble ejecución.
- **Boot idempotencia race**: `booted` guard + `metadata` binding cache.
- **RuntimeCapabilities honest**: booleanos reportados false para capabilities parciales (rate_limit/security_headers/http_limits/openapi/queued). Evita promesas técnicas falsas.

---

## 4.2 Respuesta al Objetivo Específico 2 (arquitectura de mecanismos y validación)

### 4.2.1 Mechanismos de autogeneración desde modelo de dominio

- `deriveRoutes()` fuel:
  - CRUD (list/create/get/update/patch/delete) por entidad,
  - soft-delete → `PATCH /{id}/restore`,
  - Actions/Queries → GET/POST por route derivado,
  - many-to-many/relations, security floor por el propio entity, middleware inheritance.
- `CrudController::handle()` (single dispatcher) + create/list/get/update/patch/delete/restore con:
  - validation mini-DSL,
  - hydration,
  - authorization por operación (`may{Op}` + scope),
  - persisted entity validation-error per field, location header 201,
  - optimistic `If-Match` via `VersionToken`,
  - pessimistic `#[Action(lock: true)]` dentro de `TransactionRunner`.
- QuerySource: filter/full/paginated, aggregates, joins/related/relatedMany, `lockRow`, savepoint, persisted.
- Validator DSL: required, nullable, string, int, numeric, array, email, url, min/max, regex, in, unique, exists, mimes, dimensions + `withCustomRule`. Arrays multi-input, `UploadedFile` boundary.
- Concurrency: optimistic precondition 412; domain conflict 409; TransactionRunner retries deadlock/connection drops; métrica `db.transaction_retries`.
- Middleware chain outside-in: `MiddlewareRegistry::run`, PSR-15 `Pipe`, valida missing.

### 4.2.2 Pipeline de autogeneración no entrampado (D3/honest)

- `OpenApiGenerator` existe pero el comando `openapi` se rehúsa (por diseño, reglas incompletas).
- `#[Queued]` dispatch: sync provider si no hay queue externo y lifecycle asignado (tries/unique/withoutOverlapping).
- `#[Scheduled]` y `ScannerSchedule` (cron parsing, on one server, no overlapping).
- `Projected` fields, rendering template via content negotiation (HTML si Accept pide HTML + `#[Action(view)]`).

### 4.2.3 Seguridad por diseño documentada

- SessionStore server-side (`SHA256` del id, nunca cookie opaco).
- CSRF: action only, session cookie → expected token o 403 `csrf_token_mismatch`; token render por `csrfTokenClosure()`.
- Trusted Proxy: XFF primer hop solo si `REMOTE_ADDR in TrustedProxies`.
- Soft-delete/selection scope: listing forbbiden before boot.

### 4.2.4 Evidencia de validación

- phpunit 810 tests / 33227 assertions (verde).
- contracts por componente (diagnostic, events, schedule storage, upload, streaming, trusted proxy, psr).
- byte-check (`docker/bite-check.sh`) re-introduce bug y valida fallo; restore.
- docker image propio con `ext-curl`; scripts reproducibles.

### 4.3 Límites (no sobrefirmar, honestidad)

- ❓ D1 rate adapter.
- ❓ D3 `upload_max` y `raw_body_limit` end-to-end.
- ❓ D4 openapi server endpoint.
- ❓ O8 hash metadata (debate de volumen-mtime).
- ❓ O9/O10 + E2/E4 pendientes.

---

## Anexo A — puertos y adapter (S4)

| Puerto | Interface | Locator | Adapter default |
|---|---|---|---|
| Logger | LoggerPort | LoggerLocator | StructuredLogger |
| ErrorReporter | ErrorReporterPort | ErrorReporterLocator | LogErrorReporter |
| Tracer | TracerPort | TracerLocator | NullTracer |
| Clock | ClockPort | ClockLocator | SystemClock/FakeClock |
| Hasher | HasherPort | HasherLocator | BcryptHasher |
| Encrypter | EncrypterPort | EncrypterLocator | AesGcmEncrypter (AES-256-GCM) |
| EventDispatcher | EventDispatcherPort | EventDispatcherLocator | SyncEventDispatcher + Persister |
| Mailer | MailerPort | MailerLocator | LogMailer |
| Schedule | SchedulePort | ScheduleLocator | ScannerSchedule |
| Storage | StoragePort | StorageLocator | StorageManager→LocalStorage (path guard) |
| Http | HttpPort | HttpLocator | CurlHttpClient |
| Cache | CachePort | CacheLocator | ArrayCache/FileCache |
| Queue | QueuePort | QueueLocator/SyncQueue | SyncQueue |
| Metrics | MetricsPort | MetricsLocator | InMemoryMetrics |
| Renderer | RendererPort | RendererLocator | PhpTemplateRenderer |

## Anexo B — deuda

- `RuntimeCapabilities` textual honrado.
- `S10` outbox wiring; `S12` parcial.
- Outbox same-transaction convention sigue parcial (persister ya disponible).

---

## Lectura sugerida para agente redactor (THESIS)

- Cita `Kernel::handle` y `RouteAuthorizer` para sección **request pipeline**.
- Diagrama de `src/Core/Http/MiddlewareRegistry.php`, `Pipe.php`, `Psr15Middleware.php`.
- Secuencia HTTP exacta: deep-dive §4.1 (Mermaid sequence).
- Claim de boilerplate cuantificado con commits y tests; conclusiones honestas sobre deuda pendiente.
- For the final thesis doc, this assembly maps directly to the "Obtaining objectives 1 and 2" without perjury.