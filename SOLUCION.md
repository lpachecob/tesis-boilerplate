# Boilerfree — Definición de la solución

> Estado: **implementación en curso**. Documento vivo — refleja las decisiones cerradas y qué de ellas está en el runtime.
> Independiente del formato de la tesis; la tesis se adaptará a esta solución, no al revés.
> Para ejecutar un concepto, leé SOLO su casa (autoridad); las demás menciones son trazabilidad de cobertura.

### Leyenda de estado de implementación

Cada casa lleva un marcador que responde **una sola** pregunta: *¿el runtime cumple esto?*

| Marcador | Significa |
|---|---|
| ✅ | Implementado y en el camino de request |
| ⚠️ | Parcial: funciona, y hay una condición o un hueco concreto |
| 🚫 | El contrato lo declara, el runtime **no lo ejecuta** |
| ⬜ | No implementado |

**Regla de este documento:** el marcador califica la definición que tiene debajo, nunca la reemplaza ni la repite. La razón y el detalle de cada hueco viven **una sola vez**, en el [estado de implementación](#estado-de-implementación--2026-09-25). Ningún otro lugar vuelve a contarlos. Así un cambio de estado es una edición de un caracter, no una carrera entre dos copias del mismo dato.

---

## 0. Índice de autoridades (mapa para el agente implementador)

| Concepto | Casa (autoridad) | Rol |
| --- | --- | --- |
| Atributos / metadata / evolución del contrato | §5 | Autoridad del contrato de 9 piezas y su SEMVER/deprecación |
| Escaneo, DI, Hydrator, tipado | §6 | Decisiones cerradas del motor (autoridad de mecanismo) |
| Arquitectura, puertos (lista), estructura | §7 | Autoridad de puertos y del "qué escribe el dev" |
| Relaciones | §8 | Autoridad única de relaciones |
| Lectura / CQRS-lite / DSL | §9 | Autoridad de consultas y DSL `QuerySource` |
| Persistencia / transacciones | §10 | Autoridad de escritura y tx (incluye retry por contención) |
| CLI | §11 | Autoridad de comandos y del árbol del proyecto generado (§11.2) |
| Testing | §12 | Autoridad de suite y medición |
| **Capacidades Laravel → Boilerfree** | §13 | **Trazabilidad de cobertura completa; incluye Auth (autoridad), Config (autoridad) y perfiles (autoridad)** |
| Contrato API (HTTP, JSON, validación, errores) | §14 | Autoridad del contrato de API |
| Capa de producto (brechas) | §15 | Autoridad de OpenAPI, operabilidad, ETag, PSR-7/15, outbox, páginas legales |
| Paridad de experiencia | §16 | Barra mínima demostrable (spike) |
| Ejemplo de referencia | §17 | Caso de spike |
| Pendientes | §18 | Plan de implementación |

**Regla de lectura para el agente:** cada concepto tiene UNA casa. Las tablas de §13 (trazabilidad Laravel) referencian la casa cuando el detalle vive en otra sección; cuando la fila dice "autoridad", la espec está en esa fila. Nunca implementar un concepto juntando dos fuentes: leer la casa o la fila de §13 que lo define.

---

## 1. Propósito

Framework backend en PHP que **elimina el boilerplate** en APIs REST: el desarrollador escribe el modelo de dominio (entidades, ValueObjects, servicios) y el framework **deriva todo lo demás en runtime** a partir de atributos PHP 8. Sin generación de archivos, sin mappers, sin controllers escritos a mano, sin rutas manuales.

## 2. Principio rector

> El modelo de dominio es la única fuente de verdad. Todo lo demás se deriva.

Si un artefacto de infraestructura se puede derivar por completo de la entidad, ese artefacto **no debe existir** (ni en disco ni en memoria).

## 3. Decisiones de base (validadas por la cadena de porqués)

| Decisión | Opción seleccionada | Por qué |
| --- | --- | --- |
| Runtime vs codegen | **Runtime (derivación dinámica)** | El código generado que no se toca es peso muerto con drift. PHP tiene reflexión nativa de primera clase: la metadata se resuelve en runtime, cero archivos. |
| Lenguaje | **PHP 8.x** | Es la única vía nativa de derivación en runtime sin tooling extra. Go/Rust necesitan codegen; JS/TS necesita build-time transforms. PHP 8.3+ tiene typed properties, enums, readonly, reflection eficiente. |
| Forma de entrega | **Librería Composer con puertos** | No un framework monolítico. El núcleo es el motor de derivación; los detalles (HTTP, persistencia, auth) son puertos con adapters por defecto. |
| DDD | **DDD en espíritu** | Modelo rico, lógica de negocio en el dominio (Evans, Fowler). Sin ceremonial pesado (bounded contexts, event sourcing, CQRS completo). El dev no necesita saber DDD: escribe una clase con campos y métodos. |

## 4. Metodología de decisión — regla de los 5 porqués

Toda solución propuesta debe pasar por la cadena antes de aceptarse:

1. Se propone una respuesta ("esto funciona así").
2. Se pregunta: **¿por qué funcionaría esta respuesta?**
3. A la respuesta anterior se le vuelve a preguntar **¿por qué funcionaría?**
4. Se repite hasta que **no haya salida**: la cadena se cierra sobre un primer principio, una restricción aceptada o un límite que revela un riesgo.

**Regla de oro:** si algún eslabón no encuentra respuesta sólida, ese eslabón es el riesgo real. En ese caso **se cambia de alternativa y se vuelve a tirar la cadena** hasta que cierre. Un argumento que se agota limpiamente es un argumento maduro.

## 5. Contrato de atributos — 9 piezas, ninguna más ⚠️

| Atributo | Propósito | Parámetros |
| --- | --- | --- |
| `#[Entity]` | Marca una raíz de agregado expuesta como API. Marcador POSITIVO obligatorio: solo lo decorado es visible al framework; el resto del dominio es invisible. | `table` opcional (default: snake_case del nombre de clase), `security` (default asimétrico: lectura `public`, escritura `authenticated`), `softDelete` (default false), `version` (default 'v1' — PREFIJO de versión de API en la ruta `/v1`, ver §13 "Versionado de API"; NO es la columna `optimistic_version` de §10), `indexes` (default []; compuestos/únicos: `[['col_a','col_b'], ['col_c']]`), `middleware` (default []; middlewares aplicados al CRUD derivado — ver §13 fila Middleware) |
| `#[Field]` | **Default-on:** toda propiedad promoted readonly del constructor es un campo por defecto. `#[Field]` solo se escribe para desviarse de la convención: marcar el id, renombrar, agregar validación o excluir del payload. | `id` (default false), `name` (default: nombre de propiedad), `validate` (default: derivado del tipo PHP), `expose` (default true), `index` (default false; `true` = índice simple, `'unique'` = índice único — ver §13) |
| `#[HasMany]` | Colección hija relacional: tabla hija, FK, carga eager, cascada, y política de borrado suave. Único atributo de colección 1:n. El target se deriva del docblock `@var list<T>` de la propiedad — el tipo ya está declarado, no se escribe dos veces. | `cascade` (default false), `orphanRemoval` (default false), `onSoftDelete` (default 'restrict'; `cascade`/`setNull`/`restrict`) |
| `#[ManyToMany]` | m:n pura (pivot sin comportamiento): tabla pivot derivada del par de tablas, gestionada por el framework. El target se deriva del docblock `@var list<T>`. | `cascade` (default false), `orphanRemoval` (default false) |
| `#[Queued]` | Trabajo diferido: el framework despacha el método al puerto `Queue` (retry/backoff por config). El método NO sabe que es asíncrono — la asincronía es infraestructura declarada, no lógica de dominio. | `queue` (default 'default'), `delay` (seg, default 0), `tries` (default 3), `backoff` (seg, default 30), `timeout` (seg, default 60 — el worker mata el job si lo excede, ver §13 fila Jobs), `unique` (default false), `uniqueFor` (seg; default null = vida máxima estimada del job: tries × (timeout + backoff)), `withoutOverlapping` (default false) |
| `#[Action]` | Expone un método de dominio como endpoint. Sin él, el framework ignora el método. | `method` (default POST), `route` (default: derivada del método en kebab-case), `security` (default public), `lock` (default false), `view` (default null; template a renderizar — ver §13 Blade), `layout` (default 'app'; layout del renderer), `middleware` (default []; middlewares por ruta — ver §13 fila Middleware) |
| `#[Projected]` | Salida computada de solo lectura: método del dominio que el framework serializa en la respuesta. | — |
| `#[Query]` | Consulta de lectura (read model). Único mecanismo de consulta: absorbe cualquier `findBy*`. El tipo de retorno se deriva del return type del método — no se repite. **Requisito:** el método DEBE declarar return type tipado (clase read model o `list<T>` en docblock); sin tipo, el framework falla en boot. | `route` opcional (null = consulta interna; seteada = endpoint GET), `paginate` (default true), `cache` (TTL seg, default 0 = sin cache) |
| `#[Scheduled]` | Tarea programada: el framework la registra en el puerto `Schedule` y `schedule:run` la ejecuta cuando el cron matchea. El método NO corre por request: corre por cron. | `cron` (requerido, expresión cron), `withoutOverlapping` (default false; lock en `Cache`), `onOneServer` (default false; solo el worker con lock de liderazgo) |

**Qué se eliminó del contrato y por qué (validado con la cadena):**

| Eliminado | Motivo |
| --- | --- |
| `#[ValueObject]` | Derivable: un tipo de clase que no es `#[Entity]` usado como tipo de propiedad YA ES un ValueObject. El Hydrator lo construye por convención. |
| `#[OneToOne]` | Derivable: una propiedad de tipo ValueObject ya se embebe por propiedades. La semántica 1:1 ES un ValueObject sin identidad. |
| `#[Reference]` | Derivable: la referencia entre agregados es un campo escalar (`clienteId`) con `#[Field]`. Sin lazy loading, sin fetch: no hay nada que el framework deba saber. |
| `#[Security]` | No es atributo: es el parámetro `security` de `#[Action]` + un puerto `Authenticator` que implementa la aplicación. |
| Queries derivadas `findBy*` | Absorbidas por `#[Query]` (mecanismo único de consulta). |
| Parámetro `target` de `#[HasMany]` | Derivable: el tipo de la colección ya está en el docblock `@var list<T>`; escribirlo dos veces es repetición. |
| Parámetro `returns` de `#[Query]` | Derivable: el return type del método ya declara el read model. |

**Regla de oro del contrato:** nunca eliminar una declaración que es una decisión; eliminar solo lo derivable. La **exposición es convención** (default-on: el estado del constructor se expone por defecto) y el atributo corrige la excepción. Controllers, repos, DTOs, mappers, rutas y migraciones son derivables. El dev escribe solo lo que se DESVÍA de la convención.

### Evolución y compatibilidad del contrato (gobierno del framework)

El contrato de 9 piezas es **API pública estable**: se versiona con SEMVER (MAJOR.MINOR.PATCH) y `boilerfree check` reporta cada uso de lo deprecado. Reglas:

- **PATCH:** fixes y cambios internos sin alterar comportamiento observable (formato de un mensaje, performance). Sin patch notes de breaking.
- **MINOR:** agrega un atributo/param NUEVO con default que preserva el comportamiento existente (ej. `#[Field(index: false)]`) o reglas de validación nuevas en §14. Una MINOR NO cambia la semántica de nada existente.
- **MAJOR:** cambia/elimina un atributo o param existente, cambia su semántica, cambia el contrato HTTP (§14: status codes, shape de errores, serialización, envelope), cambia convenciones derivadas (nombres de tabla, prefijos de columna) o quita una pieza del contrato.
- **Deprecación:** un atributo/param se deprecia en una MINOR; `check` emite warning por cada uso (nombre, versión desde la que está deprecado, versión de eliminación, reemplazo) y se elimina SOLO en la siguiente MAJOR — entre deprecación y eliminación media AL MENOS una MAJOR completa de aviso.
- **El contrato HTTP (§14) es parte del contrato:** cualquier cambio de forma (códigos, claves del envelope, shape de errores) es MAJOR.
- El framework mantiene `CHANGELOG.md` y `UPGRADE.md` (migración de params por MAJOR); la app declara la versión de framework en composer y el lock queda en el repo.

### Validación (autoridad completa en §14)

`validate` acepta un array de reglas en una gramática probada (subconjunto del DSL de Laravel, sin inventar sintaxis). **El mini-DSL completo (reglas, mensajes, reglas custom, derivación por tipo) está definido en §14** — §5 solo declara el parámetro del atributo y la regla de oro: las reglas de negocio del dominio NUNCA viven en metadata de campo (esas van en métodos de la entidad).

## 6. Decisiones cerradas por la cadena de porqués ✅

### 6.1 Almacenamiento de Value Objects — embebido por propiedades ✅

Cada propiedad del ValueObject se convierte en una columna con prefijo (`Money $monto` → `monto_amount`, `monto_currency`). El Hydrator construye el ValueObject recursivamente con su constructor — el **mismo mecanismo de las entidades, un nivel más abajo**. Simétrico en lectura y escritura.

- `fromScalar()` queda solo como conveniencia de **entrada** para ValueObjects de un valor (un email llega como string plano), no como contrato de persistencia.
- Alternativa descartada: una columna por ValueObject con `toScalar`/`fromScalar` — el empaquetado manual para ValueObjects compuestos sería un mapper que escribe el dev.

### 6.2 Identidad — UUIDv7 generado por el framework ✅

Campo con `id: true` sin valor en el payload → el framework genera un UUIDv7 antes de la construcción. Regla uniforme para raíces y para hijos de `#[HasMany]`.

- El dev **nunca escribe** generación de ids (puede dar un default en el constructor si quiere identidad propia).
- Autoincrement de BD descartado: incompatible con `readonly` (no se puede backfillear el id después del INSERT sin romper la inmutabilidad).
- **UUIDv7 y no v4:** los UUIDv4 aleatorios fragmentan los índices de BD en tablas grandes; UUIDv7 es **ordenable por tiempo** — mismo costo de generación, índices eficientes, cero costo para el dev que nunca los escribe.

### 6.3 Descubrimiento de servicios — escaneo por convención ✅

El framework escanea la raíz de dominio configurada (`src/Domain/` por defecto) en el boot; toda clase con `#[Action]`/`#[Query]` que no sea `#[Entity]` es un servicio expuesto. Metadata cacheadas **en disco** (`var/cache/metadata.php`), invalidadas por mtime: en dev se revalidan, en prod se congelan. Reflexión solo en el arranque o al invalidar — no se paga reflexión por request.

- **Límite conocido (v1):** en Docker volumes (macOS) los mtimes pueden ser poco confiables. Salida: `boilerfree validate --clear-cache`. Para v2: hash de contenido como fallback de invalidación.

- Cero wiring manual, cero registro por servicio.
- El contenedor DI por convención queda solo para los **puertos** (lista y propósito en §7) — una vez por proyecto, no por entidad. Todos con adapter por defecto funcional; la app bindinguea el real cuando quiera.
- Alternativa descartada: registro manual — una línea por servicio es exactamente el boilerplate de wiring que se prometió eliminar.

### 6.4 Hidratación de argumentos (`#[Action]` y `#[Query]`) ✅

Los argumentos de `#[Action]`/`#[Query]` se hidratan con el **mismo Hydrator** que construye entidades: scalars por tipo PHP, ValueObjects por convención (via `fromScalar` si es de un valor, constructor si es compuesto), `DateTime` por ISO-8601. Tipos de frontera del framework: `UploadedFile` (archivo multipart — ver §13 Upload), `StorageFile` (respuesta binaria — ver §14), `Generator` (return type de streaming — ver §13 Streaming/SSE). Un tipo no hidratable o un valor inválido falla con 422 y error campo por campo. El dev escribe el método con los tipos que quiere recibir; el framework hace la conversión. Sin esto, la entrada del framework no tiene definición y el spike muere en el primer POST.

**Política de tipado (frontera estricta):** Boilerfree exige `declare(strict_types=1)` y **NUNCA coacciona tipos en la frontera**: si el constructor pide `int` y el payload llega `"42"` (string JSON), falla la hidratación con 422 (`type_mismatch`), no convierte. El único proceso de conversión del Hydrator es: JSON número nativo → int/float declarado, JSON string ISO-8601 → `DateTime`, array → ValueObject embebido por constructor, string → `fromScalar` de ValueObject de un valor. En el dominio mismo rige PHP tipado: propiedades `readonly` tipadas, ValueObjects, `#[Projected]` con return type — el tipado fuerte es el lenguaje, la frontera es el Hydrator.

## 7. Arquitectura

### Lo único que escribe el desarrollador

- **Entidades** (raíces de agregado) con su metadata y sus invariantes en métodos. Nunca consultas de conjunto: el framework no las soporta ahí (no hay dónde inyectar la BD) — eso es trabajo de los QueryServices.
- **Value objects** (clases planas, sin atributos requeridos).
- **Servicios de dominio** con `#[Action]` (coordinación multi-agregado).
- **Servicios de consulta** con `#[Query]` (lecturas fuera del sobre). Varios `#[Query]` por clase, agrupados por concepto: `OrdenQueries` con `porCliente()`, `porEstado()`, `resumenMes()` en un solo archivo. La unidad de descubrimiento es la CLASE, no la consulta.
- **Puertos** una vez por proyecto (lista autoritativa — el DI de §6.3 referencia esta): `Authenticator` (auth), `QuerySource` (persistencia), `Logger` (PSR-3, observabilidad), `Middleware` (pipeline), `Cache`, `Queue`, `EventDispatcher`, `Mailer`, `Schedule`, `Hasher`, `Encrypter`, `Http` (cliente saliente para APIs de terceros), `Metrics` (opcional, en memoria por defecto), `Storage` (archivos: adapter por defecto filesystem local `<root>/storage/` con discos en config — paridad Laravel Filesystem; la app bindinguea S3/otros), `Clock` (reloj del sistema: `now(): DateTimeImmutable` — inyectable para tests deterministas; adapter por defecto system clock), `ErrorReporter` (report de fallos NO capturados: excepciones de `#[Action]`, workers, console y 500s con stack; adapter por defecto → canal `error` del `Logger`; la app bindinguea Sentry/Bugsnag), `Renderer` (HTML server-side: `render(template, data): string` con layout + escape automático de TODA salida — paridad de rol con Blade/Twig, sin inventar motor; adapter por defecto: templates PHP planas con helper `e()`; la app bindinguea Blade real si corre dentro de Laravel, o Twig), `Tracer` (trazado distribuido opcional: adapter por defecto no-op [sin costo]; la app bindinguea OpenTelemetry — ver §15.2) — todos con adapter por defecto funcional; la app bindinguea el real cuando quiera.

> **Elección de persistencia en la instalación:** el wizard de `boilerfree new` pregunta el adapter de `QuerySource` (PDO por defecto / Doctrine / Eloquent / custom). Cambiar de motor es siempre una línea de binding; el dominio no cambia. **Prisma NO es un adapter viable (runtime Node/TS, sin soporte PHP);** se toma solo como referencia de DX: schema declarativo único, migraciones seguras e introspection — las tres ya se replican nativamente con atributos + `boilerfree migrate` (§11), sin codegen.

### Estructura de archivos (convención, no imposición)

El framework escanea `src/Domain/` recursivamente y NO impone estructura. La guía recomienda:

- **Agrupar por concepto de negocio:** `src/Domain/Ordenes/` (Orden, LineaOrden, Money, PagarService, OrdenQueries) — todo lo que cambia cuando se toca el concepto, junto. Cohesión alta, cambio viaja junto.
- **Proyectos chicos** (5–8 entidades, el caso del experimento): flat o 1 carpeta por concepto es válido.
- **PROHIBIDO por tipo técnico:** `src/Domain/Entities/`, `src/Domain/Services/`, `src/Domain/ValueObjects/` — separa por categoría técnica, rompe la cohesión de dominio y obliga a saltar entre carpetas en cada cambio de negocio.

### Lo que el framework deriva en runtime (sin archivos)

| Pieza clásica | En Boilerfree |
| --- | --- |
| Controlador por entidad | Un único controller CRUD genérico, parametrizado por metadata |
| Repositorio por entidad | Un único repositorio genérico: hidratación, persistencia, identity map |
| DTOs + validación | Derivados en runtime desde la metadata |
| Mappers | No existen: la conversión entidad ↔ payload es mecánica y declarativa |
| Rutas | Derivadas por convención desde `#[Entity]`, `#[Action]`, `#[Query]` |
| Migraciones/schema | Derivadas de la metadata (CLI `migrate`) |

**Regla de visibilidad:** todo lo que NO lleva atributo es invisible para el framework. Helpers, transformadores, políticas y calculadoras son PHP puro, sin restricciones — los invoca la entidad o el servicio.

## 8. Relaciones (autoridad única) ⚠️

| Caso | Modelo | Atributo |
| --- | --- | --- |
| 1:n hijos con vida propia | Tabla hija + FK + eager + cascada | `#[HasMany]` |
| 1:1 embebida | ValueObject por propiedades → columnas con prefijo | ninguno |
| Referencia entre agregados | Campo escalar (`clienteId`) | `#[Field]` |
| m:n puro (pivot sin comportamiento) | Tabla pivot derivada del par de tablas (orden lexical de nombres) + FK + eager + cascada | `#[ManyToMany]` |
| m:n con comportamiento | Su propio aggregate root | `#[Entity]` |

Lineamientos DDD (Evans): el agregado es la unidad de persistencia; los cambios se aplican vía la raíz; referencias entre agregados por ID; una transacción por agregado.

Decisiones del porqué: **polimorfismo de BD (morphs) NO en el contrato** — el modelado DDD de herencia de agregados se resuelve con entidad de unión o composición en el dominio; si la app lo necesita, vive en el adapter. **Lazy loading / N+1: eliminados por diseño** — `#[HasMany]`/`#[ManyToMany]` siempre eager dentro del sobre; para lecturas fuera del sobre el dev declara el read model exacto en `#[Query]` (ver §9).

## 9. Consulta de lectura (CQRS-lite) ✅

- Escritura por agregados; **lectura por read models** — el modelo de consulta no es el modelo de escritura.
- `#[Query]` es el único mecanismo y vive **solo en servicios de consulta** — nunca en entidades. Razones: (a) SRP: una entidad tendría dos razones de cambio (invariantes + requisitos de listado); (b) DDD: un listado opera sobre el CONJUNTO, no sobre la instancia — es consulta de repositorio, no de entidad; (c) técnico: el Hydrator construye entidades solo con su constructor de dominio y no hay dónde inyectar `QuerySource`; las entidades no saben de infraestructura.
- Valores computados sobre UNA instancia siguen siendo `#[Projected]` en la entidad. Diferencia clara: instancia → `#[Projected]`; conjunto o filtro → `#[Query]` en servicio.
- Los QueryServices se agrupan por concepto (el `OrdenQueries` con varios métodos en un archivo), evitando micro-archivos de una sola consulta.
- Devuelve siempre **proyecciones tipadas** (read models), nunca entidades gestionadas.
- **Paginación derivable:** todo `#[Query]` con `route` pagina automáticamente si devuelve lista (`page`/`perPage` como query params, con tope configurable). `paginate: false` es la desviación explícita para listas completas (exportación CSV, reportes). El dev NO escribe LIMIT/OFFSET nunca.
- **Envelope de API:** definido en §14 (autoridad del contrato: `data` + `meta` con `page`/`perPage`/`total`/`totalPages` + `links`). Acá solo queda la decisión de CUÁNDO: respuestas JSON simples por defecto y el envelope aparece SOLO cuando `paginate: true` activa; sin wrapping en el resto.
- El query builder es de **lectura única**; no gestiona ciclo de vida, no hace UoW global, no tiene lazy loading — por eso NO es un ORM.
- **Alcance del DSL de `QuerySource` (acotado):** filter, order, paginate, aggregate (count/sum/avg) y join simple. Lo que el DSL no cubre (joins complejos, unions, JSON columns) vive EN el adapter (Doctrine, Eloquent) — el puerto transporta, el adapter traduce.
- Reglas de negocio de lectura (ej. temporada por cliente) viven en interfaces de dominio (`TemporadaPolicy`) inyectadas por DI: el framework transporta, el dominio decide.

**La separación NO es boilerplate:** los servicios de consulta y de dominio son código de negocio REAL (coordinación y lectura), no cableado. El wiring (registro, inyección, controllers, rutas) lo absorbe el escaneo por convención — cero registros. Agrupar `#[Query]` por concepto evita micro-archivos; la estructura de carpetas es organización, no código.

### Puerto de persistencia (port/adapter)

`$this->db` está tipado contra el puerto `QuerySource`, con adapter por defecto PDO + metadata. Cambiar de motor (Doctrine, Eloquent) es **una línea de binding** en el contenedor — el método `#[Query]` no se toca. El contrato estable es el DSL con nombres de dominio; los adapters traducen y proyectan al mismo read model.

## 10. Persistencia y transacciones ⚠️

- **Escritura:** una transacción por operación — el controller abre, ejecuta el método de dominio, flushea, commit; rollback ante `DomainException` (estatus 409/422).
- **Unit of Work por agregado** + semántica de reemplazo para hijos (determinista).
- **Bloqueo optimista** con columna `optimistic_version` (interior del framework, NO expuesta en payload): evita lost-updates en PUT/PATCH — el framework la incrementa en cada escritura y rechaza con 409 `optimistic_lock` si el ETag que el cliente envía en `If-Match` no coincide con el estado actual (el token viajero es el ETag de §15.3; la columna es el mecanismo interno de detección). La `Idempotency-Key` NO participa del control de concurrencia: su replay evita re-ejecutar un efecto (§14), no detecta conflictos de versión. **Esto es DISTINTO del param `version` de `#[Entity]` (§5), que es el prefijo de versión de API (/v1) en la ruta — no confundir.**
- **Retry de transacciones por contención (producción):** al persistir, si el adapter reporta un SQLSTATE de contención (PG `40001` serialization_failure / `40P01` deadlock_detected; MySQL `1213`/`1205`; equivalente del driver), el framework reintenta la OPERACIÓN COMPLETA desde cero hasta `db.transaction_retries` veces (default 3), con backoff (`db.transaction_retry_backoff`, default 50ms, con jitter ±50%) — el reintento parte de una tx limpia, nunca arrastra estado a medio aplicar. Otros SQLSTATE (unique_violation `23505`, FK `23503`, columna inexistente) NO se reintentan: son errores de dominio → 409/422 o error de contrato (§14), nunca se enmascaran. El retry lo ejecuta el NÚCLEO al abrir/commitear la tx, no el adapter; el adapter solo traduce el SQLSTATE. Métrica: puerto `Metrics` registra `db.transaction_retries` por intento y resultado.
- **Soft deletes: definidos, no postergados.** `#[Entity(softDelete: true)]` deriva `deleted_at` + filtro global en lecturas y en `#[Query]`; la cascada de borrado suave se declara por relación con `#[HasMany(onSoftDelete: 'cascade'|'setNull'|'restrict')]` (default `restrict` — decisión de negocio visible). Sin `softDelete: true`, el borrado es físico. El riesgo original (raíz suave + hijos con FK física) se resuelve por declaración explícita por relación, no por magia. **Restore:** la entidad con `softDelete: true` recibe un endpoint derivado `PATCH /<raiz>/{id}/restore` (security: mismo default de escritura `authenticated`; permiso refinable vía convención `mayRestore(User $user): bool` con la misma semántica que §13 Policies: si no existe → queda en `security`, si existe → obligatoria). Limpia `deleted_at` y responde 200 con la entidad restaurada. Sin softDelete no existe la ruta.
- Multi-agregado: solo vía servicio de dominio con `#[Action]` (aún una tx por operación; savepoints disponibles por puerto `QuerySource`).
- **Fuera de alcance del NÚCLEO (delegado a app o por decisión):** lazy loading y N+1 (eliminados por diseño — ver §8), paginación de colecciones hijas, consultas multi-agregado en un solo sobre, sagas/eventual consistency, transacciones distribuidas, multi-tenant, i18n, webhooks, polimorfismo de BD (ver §8). Cada una tiene su mecanismo definido en §13 (app-level o decisión declarada), ninguna queda "sin definir".

## 11. CLI (herramienta + generador de la fuente de verdad) ✅

| Comando | Función |
| --- | --- |
| `boilerfree new` | Wizard interactivo de proyecto: stack del experimento (5–8 entidades), puertos y **adapter de persistencia** (`QuerySource`: PDO por defecto / Doctrine / Eloquent / custom — ver §7). Genera el árbol COMPLETO de la app (ver §11.2) — framework como dependencia Composer, `config/boilerfree.php` + `.env` (con `APP_KEY` — ver `key:generate` abajo) + plantillas base de `templates/` + `bootstrap.php` + `public/index.php` + tests/var/Dockerfile/CI. NUNCA genera dominio: eso es `make:` (ver §11.1). |
| `boilerfree migrate` | Aplica el esquema derivado de la metadata. En perfil prod exige `--force` para operaciones destructivas (dropear columna/tabla/índice): sin `--force`, aborta listando lo que va a destruir. `--pretend` imprime el SQL que se va a ejecutar SIN aplicarlo (preview de cualquier perfil). **Lock multi-instancia:** antes de aplicar un batch, el adapter `QuerySource` toma un advisory lock (PG: `pg_try_advisory_lock`; MySQL: `GET_LOCK`; en otros drivers sin soporte nativo, lock por archivo/flock en `<root>/var/cache/migrate.lock`) — dos instancias de deploy corriendo `migrate` a la vez no corren en paralelo; el segundo espera o salta si el primero ya aplicó. |
| `boilerfree migrate --status` | Lista los batches aplicados (snapshot por batch) y el diff pendiente metadata↔BD |
| `boilerfree migrate --rollback` | Revierte el último batch (imprescindible para iterar el experimento) |
| `boilerfree migrate:fresh [--seed]` | Drop de TODO y vuelve a `migrate` (+ `--seed`); ciclo diario de iteración del experimento. Dev-only: en prod exige `--force` explícito (es destructivo de TODO el schema). |
| `boilerfree key:generate` | Genera/rota `APP_KEY` (requerida por el puerto `Encrypter`: secrets, signed URLs, cifrado de campos). Si falta en `.env`, la escribe; `--show` solo la imprime. Rotar invalida datos cifrados — lo avisa. |
| `boilerfree env:encrypt` | Cifra el `.env` completo (paridad `artisan env:encrypt`, Laravel 9+): escribe `.env.encrypted` cifrado con `APP_KEY`; `env:decrypt` restaura. Para repos/CI donde el `.env` no debe viajar en claro. Opcional: el flujo default es `.env` sin cifrar. |
| `boilerfree seed` | Siembra datos de prueba definidos por el dev |
| `boilerfree routes` | Lista las rutas derivadas |
| `boilerfree validate` | Valida el contrato de metadata del dominio (`--clear-cache` fuerza re-escaneo) |
| `boilerfree check` | `validate` + chequeo de tipos del Hydrator en el arranque (mirada estática del contrato completo; sin linter del código del dev — eso es herramienta de la app/CI). En perfil prod también ALERTA si `queue`/`cache`/`mailer` quedaron con driver `sync`/sin binding real (riesgo de producción: cola síncrona en prod bloquea requests; lista drivers efectivos por puerto). No falla, avisa. |
| `boilerfree serve` | Servidor de desarrollo |
| `boilerfree tinker` | Consola interactiva con el dominio |
| `boilerfree tinker --execute="..."` | Ejecuta una expresión del dominio y sale (modo batch para scripts/CI), sin entrar al REPL |
| `boilerfree schedule:run` | Ejecuta los tasks programados (`#[Scheduled]`/puerto `Schedule`) |
| `boilerfree schedule:list` | Lista las tareas `#[Scheduled]` registradas (cron + flags withoutOverlapping/onOneServer) SIN ejecutarlas |
| `boilerfree queue:work` | Procesa la cola (`#[Queued]`/puerto `Queue`). Respeta `timeout` del job (§13 fila Jobs) y acepta `--timeout=SEC` para el límite global del worker por job (default: el del job; si se excede, mata el proceso del job y lo marca fallido). `--max-time=SEC` para reiniciar el worker periódicamente (evita leaks). |
| `boilerfree queue:listen` | Worker de desarrollo: recarga el código de la app en cada job (vs `queue:work` persistente de prod); útil al iterar jobs |
| `boilerfree debug` | Diagnóstico del binding y metadata cargada |
| `boilerfree openapi` | Genera el OpenAPI derivado a archivo (§15.1) |
| `boilerfree outbox:dispatch` | Publica los eventos pendientes del outbox (§15.5) |
| `boilerfree outbox:status` | Lista eventos pendientes/fallidos del outbox (diagnóstico de entrega) |
| `boilerfree optimize` | **Build step de producción**: precarga metadata + rutas + config en cache en disco (paridad con `artisan optimize`). Ruta por defecto `<root>/var/cache/framework`. Otros comandos del pipeline de prod: `cache:clear`, `optimize:clear`. Dev no necesita `--clear-cache` a mano. |
| `boilerfree down [--retry=60] [--secret=...] [--allow=IP,...]` | **Maintenance mode**: responde 503 `{ "error": { "code": "maintenance", "message": "...", "details": { "retry_after": 60 } } }` con header `Retry-After`. `--secret` habilita bypass por query (`/…?maintenance_secret=…`); `--allow` lista IPs. Bloquea TODAS las rutas salvo `/healthz` y `/readyz` (§15.2), que siguen respondiendo para el orquestador. Persiste un flag derivado (archivo `<root>/var/cache/maintenance` con timestamp + retry + secret + allow). |
| `boilerfree up` | Quita el flag de maintenance; el próximo request vuelve a responder normal. |
| `boilerfree about` | Diagnóstico (dev y prod): versión del framework, entorno efectivo (perfil config activo), adapters enlazados por puerto, rutas cargadas, motores activos (queue/cache/mailer). Salida CLI tabla. |
| `boilerfree config:show <sección>` | Muestra la config EFECTIVA de una sección (con overrides de perfil + `.env` aplicados) — depuración de perfiles (autoridad: fila Config/env §13) |
| `boilerfree test` | Wrapper de PHPUnit con el entorno de test cargado (paridad `artisan test`); pasa `--filter` y flags a PHPUnit (§12) |
| `boilerfree queue:failed` | Lista los jobs que agotaron `tries` y cayeron a la tabla/cola fallida (DLQ, ver §13 fila Jobs). `queue:retry <id>` los re-encola; `queue:flush` vacía el DLQ. |

### 11.1 Comandos `make:` — única y exclusivamente la fuente de verdad ✅

**Línea divisoria (regla):** el CLI genera SOLO lo que el dev escribe a mano (dominio: entidades, ValueObjects, servicios, vistas, jobs, eventos, seeds, middleware, estructura de páginas legales — NUNCA su contenido editorial). Si el usuario pide generar algo DERIVADO (controller, model, migration, routes, resource, DTO), el comando responde: *"eso es derivado, no se genera"* — el framework lo deriva en runtime y su versión en disco sería código muerto con drift. `make:` NO viola el principio rector: no genera infraestructura derivada, genera el esqueleto de la FUENTE DE VERDAD que el dev iba a escribir igual (la entidad sigue siendo 1 clase que el dev completa con sus invariantes reales).

| Comando | Genera | Mecanismo |
| --- | --- | --- |
| `boilerfree make:entity <Contexto/Nombre>` | Entidad raíz `#[Entity]` en `src/Domain/<Contexto>/<Nombre>.php`, con `#[Field(id: true)]` en `$id`, constructor promoted `readonly`, docblock `@var list<T>` en colecciones placeholder, y esqueletos de convenciones: `may{Operación}()` y `releaseEvents()` (no obligatorias, comentadas) | plantilla + convención de carpeta |
| `boilerfree make:vo <Nombre>` | ValueObject `src/Domain/<Contexto>/<Nombre>.php` con constructor `readonly` + campos placeholder + `fromScalar()` si es de un valor | plantilla |
| `boilerfree make:service <Nombre>` | Service de consulta/dominio en `src/Domain/<Contexto>/` con un `#[Query]` y un `#[Action]` de ejemplo comentados | plantilla |
| `boilerfree make:view <ruta>` | Template PHP plana en `templates/<ruta>.php` con `e()`, helpers (`csrf_token()`, `url()`), y `extends` del layout default — una vista generada NO muestra nada hasta que una ruta `#[Action(view: ...)]` la referencia (no registra rutas por sí sola) | plantilla |
| `boilerfree make:legal:privacy` | Página `templates/legal/privacy.php` con secciones típicas VACÍAS y comentarios de qué completar + marcador `<!-- boilerfree:legal-pending -->`; deriva `GET /privacy` pública (§15.6). NUNCA genera texto legal completo | plantilla + convención |
| `boilerfree make:legal:terms` | Página `templates/legal/terms.php`, misma estructura; deriva `GET /terms` pública (§15.6). NUNCA genera texto legal completo | plantilla + convención |
| `boilerfree make:job <Nombre>` | Clase `#[Queued]` en `src/Domain/<Contexto>/Jobs/` con `tries`/`backoff` placeholder | plantilla |
| `boilerfree make:event <Nombre>` | Evento de dominio (ValueObject inmutable) en `src/Domain/` | plantilla |
| `boilerfree make:listener <Nombre>` | Listener con `on(Event): void` (sin atributos, registro en bootstrap) | plantilla |
| `boilerfree make:seed <Nombre>` | Seeder en `src/Seeders/` (clase sin atributos) | plantilla |
| `boilerfree make:middleware <Nombre>` | Clase de middleware `handle(Request, next)` en `src/Middleware/` para registrar en config (`middleware`) o por ruta | plantilla |

**Regla de nombres:** `make:entity Cliente/Orden` → `src/Domain/Cliente/Orden.php` — una carpeta por CONCEPTO de negocio (regla de §7: agrupar por concepto, nunca por tipo técnico `Entities/`/`Services/`). El CLI valida el nombre antes de crear: si el Contexto tiene más de una palabra, la convierte a snake (convención de carpeta); si el archivo ya existe, NO pisa — falla con mensaje.

### 11.2 Árbol del proyecto generado por `boilerfree new` ✅

Contrato de la APP generada (el esqueleto completo, no disperso): el proyecto es UNA app clonable sin decisiones previas.

```
<app>/
├── composer.json            # require: boilerfree/core (el framework es DEPENDENCIA, no copia) + binario `boilerfree`
├── .env.example             # env con el que se levanta el proyecto + APP_KEY vacío
├── config/
│   ├── boilerfree.php       # base con defaults de todas las secciones (fila Config, §13)
│   └── boilerfree.prod.php  # ejemplo de override (perfil prod; autoridad: fila Config/env §13)
├── bootstrap.php            # ÚNICO punto de binding de la app: adapters reales de puertos + listeners + registros (scopes) + reglas custom
├── src/
│   └── Domain/              # NACE vacío (+ opcional README con las reglas de la carpeta); el dev crea con `make:`
├── src/Seeders/             # seeders del dev (make:seed)
├── src/Middleware/          # middlewares de la app (make:middleware)
├── templates/
│   ├── layouts/app.php      # layout base derivado con links de footer (bloque legal automático, §15.6)
│   └── legal/               # vacío; `make:legal:*` lo puebla (§15.6)
├── public/
│   └── index.php            # ÚNICO entrypoint HTTP: boot del núcleo → pipeline → respuesta
├── tests/
│   ├── Unit/                # tests del dominio
│   └── Feature/             # HTTP tests contra el controller genérico (§12)
├── var/
│   ├── cache/               # metadata + rutas + config (optimize), queries cacheadas; gitignored
│   └── db/                  # sqlite/pg + tablas internas (sessions, outbox, queue_failed, idempotency); gitignored
├── Dockerfile               # imagen dev (PHP 8.3 + pgsql); prod usa multi-stage non-root de referencia (ver §13 hardware)
├── docker-compose.yml       # stack dev (php + postgres) con restart:"no" en ambos servicios
├── phpunit.xml              # suite de tests
├── pint.json + phpstan.neon # gates de la app (dev deps del skeleton, fila Linter §13)
└── .gitignore               # var/, .env, vendor/, .env.encrypted
```

Reglas del árbol:

- **El framework es dependencia Composer** (`boilerfree/core`), nunca contenido copiado: la app tiene su propio `composer.lock` y `boilerfree new` la instala.
- **Un solo entrypoint** `public/index.php`; NO existe `routes/` ni `app/Controllers/` ni `database/migrations/` — todo eso es derivado (§2), nace en runtime desde metadata.
- **`bootstrap.php` es el único archivo que la app toca al arrancar**: registra bindings (adapters reales), listeners, scopes globales y reglas de validación custom; el núcleo lo incluye después de cargar metadata y antes del primer request.
- **`var/` es descartable por diseño** (se regenera con `optimize`/`migrate`); su ausencia es warning en boot, nunca error (fila Linter §13).
- El wizard `new` genera el árbol COMPLETO (no un "hola mundo"): la app nace lista para `composer install` + `migrate` + `serve`.

## 12. Testing (esencial para la tesis) ⚠️

- **Suite propia del framework:** unit tests del Hydrator, metadata engine, routing, criptografía de UUIDv7 — el núcleo se prueba una vez y se congela.
- **En la app del experimento:** PHPUnit + HTTP tests contra el controller genérico (create/read/update/delete/action/query), `RefreshDatabase`-style (transacción por test), factories del dev para las 5–8 entidades.
- Las mediciones del experimento (líneas, tiempo, errores) se sacan de estos tests — sin una estrategia de testing definida, el experimento no se puede medir.

## 13. Capacidades de Laravel — implementación en Boilerfree

Evaluación de las capacidades de Laravel, una por una, con el mecanismo concreto de implementación en Boilerfree (derivado / atributo / puerto / app-level). Cada ítem es ESPEC de implementación: si falta, la implementación no está completa.

### HTTP y ciclo de vida

| Capacidad Laravel | Implementación en Boilerfree | Mecanismo |
| --- | --- | --- |
| Middleware (pipeline) | Puerto `Middleware` (interfaz de pipeline `handle(Request, next): Response`). El núcleo ejecuta el pipeline global cargado desde config; el dev registra middlewares NOMBRADOS en bootstrap de la app, nunca clases en el dominio. Por ruta: el param `middleware` (lista de nombres → resueltos contra el registro) de `#[Action]`/`#[Entity]` — declarado en §5, casa del contrato. La app puede correr dentro de Laravel y delegar su pipeline. | puerto + config + param (§5) |
| Rate limiting / throttle | Por defecto derivado: `rate_limit` en config (ej. 60 req/min por IP, 240 por usuario autenticado), aplicado en el pipeline antes del controller; respuesta 429 con `Retry-After`. Tope por ruta derivada automáticamente de la metadata. | config + núcleo |
| CSRF | **JSON (API): NO aplica** — Boilerfree es stateless con token (header), no cookies de sesión. **HTML (vistas con guard `session`): SÍ aplica** — el núcleo genera un token CSRF POR SESIÓN, lo guarda en la sesión server-side (fila Sesiones) y lo expone como cookie `XSRF-TOKEN` + meta (para que el JS/front lo envíe); valida el header `X-XSRF-TOKEN` o el campo `_token` contra el valor de la sesión en los métodos no-idempotentes de rutas con `view:` (mismo mecanismo de Laravel: session-driven, no double-submit). En el guard `token` nunca se valida CSRF. | por ruta (JSON: sin CSRF; HTML+cookies: núcleo) |
| CORS | Adapter de respuesta en el pipeline: adjunta headers según config (`cors: allowed_origins, allowed_methods, allowed_headers, expose_headers, max_age`). Solo enrutado en el pipeline de app; el dominio no lo ve. El **preflight `OPTIONS` se contesta desde el path** y **antes** de la autorización (§13: un preflight no lleva credenciales), sólo para paths que algún método alcanza de verdad, y arrastra `Vary: Origin` porque el `Access-Control-Allow-Origin` ahora refleja quién preguntó. | config + núcleo |
| Security headers | Config `security_headers` (default activado en prod): `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy`, `Strict-Transport-Security` (solo si `http.force_https`), `Permissions-Policy` (default minimal, ampliable). El núcleo los adjunta en el pipeline de respuesta; el dev los desactiva por header si su infra ya los envía. | config + núcleo |
| Trusted proxies | Config `trusted_proxies`: el núcleo ajusta `Request` (https, client IP) ANTES del pipeline cuando llega de un proxy. | config + núcleo |
| Upload de archivos | Campo `#[Field]` con tipo `UploadedFile` (ValueObject del framework): el Hydrator de argumentos del `#[Action]` recibe el archivo del multipart; el método de dominio lo recibe y delega la persistencia al puerto `Storage` (ya, §7: adapter filesystem por defecto, discos en config). Validación de `mime`/`max` en el mini-DSL (`'mimes:pdf,jpg'`, `'max:10240'`). | derivado + puerto Storage |
| Streaming / SSE | Método `#[Action]` que devuelve `Generator` → el controller streama la respuesta en chunks (media-type configurable). Derivable del return type, sin atributo nuevo. | derivado (return type) |
| Versionado de API | `#[Entity(version: 'v1')]` → prefijo de ruta `/v1/...` derivado. `#[Query(route)]` admite prefijo de versión explícito si el método difiere. | derivado (param) |

### Auth y seguridad (autoridad única — fusiona las decisiones de seguridad)

| Capacidad Laravel | Implementación en Boilerfree | Mecanismo |
| --- | --- | --- |
| Seguridad de rutas | Parámetro `security` en `#[Action]` y `#[Entity(security)]` para todo el CRUD derivado de la raíz: dominio finito `public` / `authenticated` / `admin`. **Default asimétrico** de `#[Entity]`: lectura `public`, escritura `authenticated` — un GET de datos no queda abierto por omisión, y la escritura tampoco se bloquea por defecto. Declarar `security: 'admin'` sube TODO el CRUD; `security: 'public'` lo abre todo. **`admin` se evalúa con la convención `esAdmin(User $user): bool` en la clase `User` del dominio** (roles viven en el dominio, fila Roles): si el método no existe → nadie es admin (falla cerrado para `admin`); si existe → decide. | derivado (param) + convención |
| Guards múltiples | **El puerto `Authenticator` ES la guard:** `authenticate(Request): User`, `issueToken(User)`, `userFromToken(string)`. Guards distintos = bindings distintos en config (`auth.guards: { session: ..., token: ... }`); el núcleo nunca distingue driver — solo invoca el puerto. **Soportados en v1:** `token` (Authorization: Bearer, default) y `session` (adapter con cookies; el CHALLENGE de sesión vive en el adapter, pero la GENERACIÓN/VALIDACIÓN del token CSRF es del núcleo — ver fila CSRF). OAuth2/JWT = app-level vía puerto. | puerto + config |
| Sesiones server-side (guard `session`) | El adapter `session` usa una tabla interna derivada `<root>/var/db/sessions` (id hash, user_id FK, payload, expires_at, last_activity). Cookie `boilerfree_session` (HttpOnly, SameSite=Lax, Secure en prod) contiene el id; el adapter lee la fila, la renueva o la expira (GC por `schedule:run` + lazy en acceso: borra vencidas). **Regeneración anti-fixation:** al autenticar (login) el adapter genera un NUEVO session id (borra la fila vieja, inserta la nueva, rota la cookie) — nunca reutiliza el id anónimo; previene session fixation. El núcleo NO hidrata sesiones: el adapter devuelve el `User` al `Authenticator`. El CSRF de estas sesiones lo maneja el núcleo (cookie `XSRF-TOKEN` + validación en no-idempotentes de rutas con `view:`), NO el adapter — ver fila CSRF. | adapter (puerto) + tabla interna + núcleo (CSRF) |
| Policies / Gates (autorización por OBJETO) | **Convención por nombre en el dominio:** la raíz declara `may{Operación}($user): bool` (ej. `mayUpdate(User $user): bool`); el framework la invoca automáticamente antes de tocar la instancia. **Semántica precisa:** si el método NO existe → la autorización queda SOLO en el `security` de la ruta (default asimétrico de `#[Entity]`: lectura `public`, escritura `authenticated`) — la convención es un hook de refinamiento, no un requisito: el CRUD default funciona sin escribir políticas. Si el método SÍ existe → es obligatorio: `false` → 403 (`forbidden`). Las políticas de servicios viven en el QueryService/DomainService que declara `#[Action]`/`#[Query]`. **En LISTADOS** la política por objeto no se evalúa por instancia (paginación): la autorización de consultas de listado tiene su propia regla — ver fila siguiente. | convención + núcleo |
| Autorización por objeto en LISTADOS (scoping) | `may{Operación}` decide sobre UNA instancia; un `#[Query]` paginado no puede evaluarla fila por fila sin romper el paginado. **Dos mecanismos complementarios:** (1) el Framework inyecta el `User` autenticado como parámetro en el `#[Query]` (firma con `User $user` → el dev filtra en el read model, ej. `where ownerId = $user->id`); (2) la raíz puede declarar `scopeFor(User $user, QuerySource $q): QuerySource` por convención — un scope de autorización que el framework aplica SOLO en listados/consultas derivados de esa raíz (paridad del rol de `GlobalScope`, sin atributo nuevo). **Fail-closed (check):** si la raíz expone `mayRead` y hay una consulta derivada de ella SIN `User $user` en la firma NI `scopeFor` → `boilerfree check` FALLA en boot: todo listado sobre una raíz protegida por objeto debe tener forma de filtrar por actor; sin eso, el listado expone filas que la política individual protegería. | convención + núcleo (check) |
| Roles / permisos | Viven en el DOMINIO (entidad `Usuario` con `roles` como colección de enums/ValueObjects — `#[HasMany]` o `#[Field]` de collection). La autorización por rol usa la convención `may{Operación}` consultando esos roles. Sin sistema de permisos embebido: es negocio, no infraestructura. | dominio + convención |
| Password reset / email verification / 2FA / OAuth2 | Flujos de APP, no del framework: vía puertos `Authenticator` + `Mailer` + `Encrypter`. Boilerfree no reimplementa estos flujos (son negocio de la app); la app declara `auth.routes.login` (POST) en config y el framework enruta + aplica throttling. Si la app corre dentro de Laravel, ya los tiene; los puertos delegan. | app-level (puertos) |

### Persistencia y query (paridad Eloquent)

| Capacidad Laravel | Implementación en Boilerfree | Mecanismo |
| --- | --- | --- |
| Relaciones 1:1 / 1:n / n:m | Definido en §8 (autoridad de relaciones): ValueObject embebido / `#[HasMany]` / `#[ManyToMany]` con pivot lexical derivada. | ver §8 |
| Polimórficas | NO en el contrato por decisión — ver §8 (anti-DDD para el agregado; vive en el adapter si la app lo necesita). | ver §8 |
| Lazy loading | **NO existen lazy loading ni N+1 por diseño** — ver §8: siempre eager dentro del sobre; lecturas fuera del sobre vía read models en `#[Query]`. | ver §8 |
| Query builder (joins/subqueries/unions/JSON) | DSL acotado en el puerto `QuerySource` (filter/order/paginate/aggregate + join simple). Escapes controlados: un método `#[Query]` puede inyectar el adapter directamente (bind del puerto) para SQL nativo — igual que `DB::raw()`, explícito y localizado. El 90% deriva; el 10% complejo se escapa por el puerto. | puerto + escape controlado |
| Scopes | Métodos `#[Query]` con parámetros reutilizables en el QueryService = scopes. `OrdenQueries::activas()` sin route = scope interno composable. | convención |
| Mutators / accessors / casts | casts = ValueObjects (ya); accessors = `#[Projected]` (ya); mutators NO por diseño: el estado es inmutable y los cambios pasan por métodos de dominio (`#[Action]`); la escritura directa (PUT) reconstruye la entidad con el nuevo payload — sin mutación imperativa. | decisión declarada |
| Migraciones versionadas | `migrate` deriva el schema desde metadata y mantiene TABLA de batches (snapshot por batch); `migrate --rollback` revierte el último batch; `migrate --status` lista aplicados. Sin archivos de migración: el diff metadata↔BD es la migración. **Protección de datos en prod (mecanismo completo en §11):** operaciones destructivas exigen `--force`, preview con `--pretend`, y un advisory lock multi-instancia evita batches concurrentes — ver fila `boilerfree migrate` en §11. | núcleo (derivado) + §11 |
| Seeders + factories | `boilerfree seed` ejecuta seeders definidos por el dev (clases sin atributos); factories del dev para tests (sección 13). | app-level |
| Transacciones + savepoints | Una tx por operación (ya, ver §10). Savepoints: el puerto `QuerySource` expone `savepoint(name)` / `rollbackTo(name)` para workflows multi-paso del mismo `#[Action]` que deben aislar parcialmente. | puerto |
| Locks pesimistas | `#[Action(lock: true)]` → `SELECT ... FOR UPDATE` sobre la raíz al abrir la tx; default `lock: false` (optimista con `optimistic_version` — NO el param `version` de `#[Entity]`, ver §10). | atributo (param) |
| Cache de consultas | `#[Query(cache: 60)]` → el resultado se cachea TTL segundos vía puerto `Cache` (adapter por defecto: filesystem `<root>/var/cache/queries`; Redis si la app lo bindinguea). Invalidez automática por idempotencia de route+params; el dev nunca escribe código de cache. **Invalidación por escritura (producción):** el framework también invalida las entradas cacheadas de una tabla cuando persiste un cambio sobre ella (create/update/delete/soft-delete de la entidad raíz) — sabe qué tablas leyó cada query (tracking del plan de ejecución) y borra solo las entradas correspondientes; así el listado nunca sirve datos viejos tras un PUT. En v1 si el tracking de tablas no está disponible (adapter complejo), fallback: invalidar las queries cacheadas NO cacheadas por TTL ante cualquier escritura (conservador, correcto, menos eficiente). | atributo (param) + puerto + tracking |
| Índices de negocio (`->index()`, compuestos, `unique`) | `#[Field(index: true|'unique')]` → índice simple sobre la columna; en `#[Entity(indexes: [['col_a','col_b'], ['col_c']])]` → compuestos y únicos nombrados (`unique: true` por fila). El schema derivado los declara en DDL; el dev NO escribe SQL. Default sensato: solo PK/FK + `unique` en campo con `#[Field(unique: true)]` — todo lo demás explícito. | atributo (param) |

### Comunicación y trabajo diferido

| Capacidad Laravel | Implementación en Boilerfree | Mecanismo |
| --- | --- | --- |
| Jobs / queues / retry / backoff | `#[Queued]` (nuevo): el método NO sabe que es asíncrono — el framework despacha al puerto `Queue` (adapter por defecto SYNCHRONOUS para dev/tests; Redis/DB driver si la app lo bindinguea). `tries`/`backoff`/`delay`/`timeout`/`unique`/`uniqueFor`/`withoutOverlapping` son params del atributo (§5); el driver los respeta. **Timeout de job (producción):** param `timeout` (default 60s) — si el job excede, el worker lo mata (señal al proceso), lo marca fallido y aplica `tries`/`backoff`; el worker también puede limitar con `queue:work --timeout` global (mecanismo completo en §11 — ver fila `queue:work`). **Jobs únicos:** `unique: true` → el framework no despacha si ya existe un job con la misma firma (`clase+método+hash de args serializados`) pendiente/en proceso; el lock vive en el puerto `Cache` con TTL = `uniqueFor` (default: vida máxima estimada del job = tries × (timeout + backoff)). **Overlap:** `withoutOverlapping: true` → mismo lock, pero por job completo (una instancia a la vez, sin duplicados en cluster). **DLQ:** al agotar `tries` el job pasa a la tabla/cola fallida (adapter por defecto: tabla `<root>/var/db/queue_failed` + canal en `Queue`; driver Redis/DB si se bindinguea). `boilerfree queue:failed` lista, `queue:retry <id>` re-encola, `queue:flush` vacía; el job nunca se pierde silenciosamente. La app corre un worker (`boilerfree queue:work`). | atributo + puerto |
| Schedule sin solapamiento / un solo servidor | La app registra tareas con `#[Scheduled(cron: '...', withoutOverlapping: true, onOneServer: true)]` o callable con flags. `withoutOverlapping` → no ejecuta si la tarea ya corre (lock en `Cache`); `onOneServer` → solo el worker con el lock de liderazgo (puerto `Schedule` + `Cache` como mutex compartido) ejecuta la tarea; default `onOneServer: false` (cada worker corre todo, correcto para dev). El OS invoca `* * * * * boilerfree schedule:run`; el núcleo resuelve qué tareas correr en este minuto y respeta los locks. | atributo + puerto + CLI |
| Events / listeners | **Eventos de dominio DDD**: la raíz decide su evento en el método de dominio (cambia estado + registra evento); tras persistir, el framework llama al método convención `releaseEvents(): array` (lo declara la entidad) y los despacha al puerto `EventDispatcher`. Listeners = clases de la app sin atributos que implementan `on(Event): void`; se registran en bootstrap. Cero boilerplate en el dominio: el evento es un ValueObject emitido. | convención + puerto |
| Notificaciones / mail | Puerto `Mailer` (`send(Notification $n)`). El dominio construye ValueObjects de notificación; el servicio de dominio o un listener las envía. Adapter por defecto: log (dev); SMTP/sendmail si la app lo bindinguea. | puerto |
| Broadcasting / websockets | FUERA del núcleo por decisión de transporte: streaming en tiempo real es infraestructura de la app (Laravel Echo/Pusher/soketi detrás del puerto), no del framework. Un listener puede delegar al broadcaster de la app. | app-level (delegado) |
| Cliente HTTP de salida (APIs de terceros) | Puerto `Http` (nuevo, PSR-18 por defecto): `get/post/put/patch/delete`, timeout + retries + backoff configurables en config (`http.timeout`, `http.retries`), respuesta como array/string/ValueObject. Adapter por defecto: cURL (nativo de PHP). Para llamar un servicio externo el dominio/service inyecta el puerto `Http` por DI y llama; nunca `file_get_contents` pelado. Para **agentes / IA / LLMs** (OpenAI, Anthropic, MCP): misma vía — el SDK del proveedor queda detrás de un adapter del puerto `Http`; trabajos largos de agente se despachan con `#[Queued]` + `#[Action]` (`tries/backoff` ya los tiene). Cero magia: es Http + Queue, las piezas ya existen. | puerto + config + atributo |

### Herramientas y DX

| Capacidad Laravel | Implementación en Boilerfree | Mecanismo |
| --- | --- | --- |
| Artisan `make:` | **`make:` existe para la FUENTE DE VERDAD, no para lo derivado** (ver §11.1): `make:entity`, `make:vo`, `make:service`, `make:view`, `make:job`, `make:event`, `make:listener`, `make:seed`, `make:middleware`. Genera el esqueleto de lo que el dev escribe a mano (dominio y vistas), con convención de carpetas por concepto (§7). Lo DERIVADO (controller, model, migration, routes, resource, DTO) NO se genera ni a pedido: el framework lo deriva en runtime y el CLI responde "eso es derivado, no se genera". | CLI + plantillas (fuente de verdad) |
| Tinker (REPL) | `boilerfree tinker`: REPL con el dominio cargado (reflexión + Hydrator disponibles) para probar entidades en vivo. Dev-only. | CLI |
| Schedule (cron) | Puerto `Schedule` + CLI `boilerfree schedule:run`: la app registra tareas (expresión cron + método `#[Action]`/`#[Queued]` o callable) en bootstrap. El framework no maneja el daemon de cron: el OS lo invoca (`* * * * * boilerfree schedule:run`). | puerto + CLI |
| Config / env (incluye perfiles) | Autoridad: `config/boilerfree.php` (archivo PHP tipado, secciones: `domain_root`, `db`, `cache`, `auth`, `middleware`, `cors`, `rate_limit`, `queue`, `mailer`, `schedule`, `http`, `ops`, `openapi`, `profiles`, `validation`, `security_headers`, `trusted_proxies`) + `.env` parseado por el núcleo (sin librería externa). Perfiles estándar `dev`/`test`/`prod` (sección `profiles`): override por entorno `config/boilerfree.<env>.php` + `.env` (el env GANA sobre ambos). Los agentes implementan el acceso a config como servicio interno `Config`, con override por env. **Forma de `db` (fija, la usa el mapeo de env):** la conexión vive en `db.default.*` — `db: { default: { driver, host, port, database, username, password } }` — y las llaves sisters (`db.pagination_max_per_page`, `db.transaction_retries`, `db.transaction_retry_backoff`) cuelgan de `db`, no de la conexión. Por eso `DB_HOST` mapea a `db.default.host` y no a `db.host`: una variable de entorno solo sobrescribe una llave que **ya existe** en la config, así que la forma tiene que ser adivinable. Forma plana `db.host`: **no existe** y no debe usarse. | núcleo + archivos |
| Debug toolbar / telescope | `boilerfree debug` (dev-only, servidor de inspección): muestra metadata cargada, requests por ruta, queries ejecutadas, timing. NO UI pesada en v1: salida CLI JSON. | CLI núcleo |
| Logging | Puerto `Logger` PSR-3 (ya): adapter por defecto syslog/monolog; la app bindinguea su propio canal. | puerto |
| Linter / análisis estático | El NÚCLEO no lintea el dominio del dev (no es boilerplate que eliminar: es herramienta del editor/CI). El framework sí provee: (a) `boilerfree check` — valida el contrato de metadata + tipos de Hydrator; en **boot**: si la metadata VIOLA el contrato (atributo inválido, target irresoluble, `#[Query]` sin return type) el boot FALLA con error claro (contrato roto = bug del dev, se detiene); si solo AUSENTA cache en disco, hace escaneo lazy + warning y sigue (nunca error por cache — ver `optimize`), y (b) dev dependencies del skeleton: PHP-CS-Fixer/Pint + PHPStan en nivel razonable ejecutables desde el proyecto. La app los usa en CI; el framework NO los ejecuta por su cuenta. | núcleo (check) + skeleton (dev) |

### Vistas y renderizado (paridad Blade)

| Capacidad Laravel | Implementación en Boilerfree | Mecanismo |
| --- | --- | --- |
| Blade (templates HTML server-side) | Puerto `Renderer` (ya, §7): `render(template, data): string` con layout + escape automático (`e()`) en el adapter por defecto. **Opt-in por ruta:** `#[Action(view: 'ordenes/detalle', layout: 'app')]` → esa respuesta se renderiza HTML (cuando `Accept: text/html`) en vez de JSON (ver §14 content-negotiation). El dominio NO cambia: devuelve datos; el renderer los pinta. El HTML lo escribe el dev en `templates/`; el framework deriva layout base + ruta. Adapter por defecto: PHP plana con `e()`/`raw()`; Blade real si la app corre dentro de Laravel; Twig opcional. | puerto + atributo (param) |
| Layouts / componentes / includes | El layout se resuelve del param `layout` (default `'app'` → `templates/layouts/app.php`); el renderer inyecta el contenido y expone helpers (`csrf_token()`, `url()`, `e()`). Sin motor propio: lo que el adapter soporta (include/component) lo soporta el framework. El framework NO inventa sintaxis de componentes en v1 — PHP plana + includes nativos del adapter. | puerto + derivado (layout) |
| Formularios + CSRF en vistas | El renderer expone `csrf_token()` (cookie `XSRF-TOKEN` + meta) para los forms de rutas con `view:` y guard `session`; el núcleo valida en POST/PUT/DELETE no-idempotentes contra el token guardado en la sesión (session-driven, ver fila CSRF). | núcleo + renderer |

### Seguridad aplicada

| Capacidad Laravel | Implementación en Boilerfree | Mecanismo |
| --- | --- | --- |
| Password hashing | Puerto `Hasher` (bcrypt/argon2): el adapter demo de `Authenticator` lo usa; el framework NUNCA hashea por su cuenta — el puerto decide. | puerto |
| Encrypción | Puerto `Encrypter` (app-level): secrets, tokens firmados (`signed URLs`), cifrado de campos sensibles. El dominio no cifra: la app lo hace en el puerto. | puerto |
| SQL injection | PDO preparado SIEMPRE en el adapter por defecto; el DSL acotado no acepta interpolación de strings. El escape nativo (`#[Query]` con adapter directo) es responsabilidad explícita del dev. | núcleo (garantía) |
| XSS | **JSON: NO aplica** — la API no renderiza HTML. **HTML (vistas): el escape lo hace el framework** — el adapter por defecto de `Renderer` escapa TODA salida de datos (helper `e()` automático en el motor de template) y las rutas con `view:` pasan los valores por el renderer, nunca se concatenan raw. El dev que usa el escape de `Renderer` no puede inyectar; el `raw()` explícito es decisión suya. | por ruta (JSON: sin XSS; HTML: renderer escapa) |
| Mass assignment | NO existe el problema: el estado se fija SOLO por el constructor readonly (nada de `fill()`). El payload del CRUD se valida contra el constructor. | decisión declarada |
| Throttling de auth (anti-DDoS) | Rate limiting del pipeline aplica a rutas derivadas de login/token: intentos fallidos → 429 con backoff creciente (`auth.throttle` en config: límite de intentos, ventana, lockout). El puerto `Authenticator` reporta intentos fallidos; el núcleo aplica el bloqueo por IP + por cuenta. Además: limit global por IP en config (`rate_limit`) y `body_limit` (→ 413) para peticiones enormes. Ver §14. | config + núcleo + puerto |

### Testing

| Capacidad Laravel | Implementación en Boilerfree | Mecanismo |
| --- | --- | --- |
| RefreshDatabase | Trait del framework para tests: una tx por test + rollback (snapshot de schema al inicio de la suite). | núcleo (test helper) |
| Determinismo temporal (`Carbon::setTestNow`) | El puerto `Clock` (ya, §7) se bindinguea con un adapter falso en tests (`FakeClock: set(now)/advance()`); los asserts de eventos, cache y locks usan `Clock->now()` — el test nunca depende del reloj real. | puerto + test helper |
| Factories + Faker | Factories del dev (clases que construyen la entidad con datos de fixture); Faker NO es dependencia del framework — es decisión de la app usarlo. | app-level |
| HTTP tests | PHPUnit + cliente HTTP integrado contra el controller genérico (create/read/update/delete/action/query). | app-level (PHPUnit) |
| Mocking | PHPUnit estándar sobre los puertos (el dev mockea `QuerySource`, `Authenticator`, etc. — las interfaces son mockeables por diseño). | app-level |
| Pest | Opcional: la gramática de Pest corre sobre PHPUnit; la app puede usarlo. No es contrato del framework. | app-level |

### Ecosistema

| Capacidad Laravel | Implementación en Boilerfree | Mecanismo |
| --- | --- | --- |
| Paquetes / docs / comunidad | NO es implementable en el framework; se reconoce como meta a largo plazo. El diseño de puertos permite que una app use el ecosistema de la plataforma HOST (correr dentro de Laravel, el puerto Delega). La tesis mide boilerplate, no ecosistema. | decisión declarada |

### Operación y producción (deploy-ready)

| Capacidad Laravel | Implementación en Boilerfree | Mecanismo |
| --- | --- | --- |
| `artisan optimize` (build step) | `boilerfree optimize` (ver §11): precarga metadata + rutas + config en cache en disco; en prod el framework lee el cache, NO re-escanea en cada request. `boilerfree optimize:clear` invalida (dev). Sin cache presente → escaneo lazy + warning en boot (nunca error por cache: el error de boot queda reservado para metadata que VIOLA el contrato — ver fila Linter). | núcleo + CLI |
| `artisan down` / `up` (maintenance mode) | `boilerfree down --retry=60 [--secret][--allow]` / `up` (ver §11). Pipeline responde 503 JSON con `Retry-After` e `error.code: "maintenance"`; `/healthz` `/readyz` siguen 200. Bypass por `maintenance_secret` query param (si `--secret`) o IP en `--allow`. | núcleo + CLI |
| Deploy runbook (procedimiento) | El esqueleto documenta el orden de deploy: **1)** `boilerfree down --retry=120`, **2)** files actualizados (Composer), **3)** `boilerfree migrate`, **4)** `boilerfree optimize`, **5)** restart de workers (`queue:work` bajo Supervisor/systemd) + `schedule:run` cron (`* * * * *`), **6)** `boilerfree up`. NUNCA `down`→`up` sin el paso 3 (migraciones pendientes fallarían en runtime). | doc + CLI |
| Error reporting (excepciones no capturadas) | Puerto `ErrorReporter` (ya, §7): el framework reporta 500s, jobs que agotaron `tries` (antes de DLQ) y errores de console vía este puerto. Adapter por defecto → canal `error` de `Logger`; la app bindinguea Sentry/Bugsnag y el stack viaja sin secrets (sanitiza env + payload). `config.debug` NO filtra (report siempre activo en prod); el 500 devuelto nunca incluye trace. | puerto |
| Ciclo de vida de procesos (señales / drenado) | `queue:work`, `queue:listen`, `schedule:run` y `serve` manejan **SIGTERM/SIGINT con modo drenado**: (1) dejan de TOMAR trabajo nuevo, (2) terminan el job/request EN CURSO — `queue:work` deja terminar el job actual respetando su `timeout` (config `workers.drain_timeout`, default 60s — una ventana cubre el job default; si el job lo excede, se aborta y se marca fallido para reintento normal, nunca se pierde), `schedule:run` no arranca tareas nuevas, `serve` termina el request en curso y cierra el socket — (3) se liberan locks/transacciones y se sale con exit 0 (el supervisor NO ve un stop planeado como fallo). Una SEGUNDA señal durante el drenado fuerza el aborto inmediato (el job a medio aplicar queda pendiente y se reintenta: at-least-once por diseño §12/§15.5; nunca commit a medias). Esto es lo que hace un deploy en caliente seguro: el orquestador manda SIGTERM, el worker drena y sale, el nuevo deploy toma la cola. | núcleo + CLI |
| Retención / GC de datos operativos | Toda tabla de estado operativo del framework tiene TTL + purga (sin eso, disco lleno a los meses): **sesiones** (`expires_at` + GC lazy y por `schedule:run`, fila Sesiones), **idempotency** (`expires_at` + purga en insert + `schedule:run`, §14 Idempotency-GC), **outbox entregadas** (`ops.outbox_retention_days` default 7 — las entregadas se purgan; las pendientes/fallidas NO, se conservan hasta resolver; fila outbox §15.5), **cola fallida / DLQ** (`ops.failed_jobs_retention_days` default 30 — pasado el TTL, `queue:failed` deja de listarlas y se purgan; `queue:retry` solo aplica dentro de la ventana; fila Jobs). Centro de configuración: sección `ops` (consolidar: sesiones/outbox/failed en `ops.*`, idempotency ya en `http.idempotency_ttl`). | config `ops` + núcleo + CLI |
| Hardware / runtime recomendado | Doc del eskeleton: PHP-FPM + opcache (`opcache.enable=1`, `validate_timestamps=0` en prod — el cache deriva de `optimize`), `pcre.jit`, workers = nproc, `schedule:run` en cron del host, `queue:work` bajo Supervisor (restart automático, `--max-time` para evitar leaks), BD en la misma VPC, `body_limit` en config del proxy. No es código del framework: es el contrato de deployment del experimento. | doc |

## 14. Contrato de API — HTTP, JSON y validación (autoridad única del contrato) ⚠️

Base: **JSON es el formato por defecto de la API** (`Content-Type: application/json; charset=utf-8`). Toda ruta responde JSON salvo que declare `view:` (§13 puerto `Renderer`): en ese caso la misma respuesta se sirve como `text/html` cuando el cliente manda `Accept: text/html`, y como JSON en el resto (content-negotiation por ruta). Para las rutas JSON (default): si el request pide otro media-type (`Accept`) → 406. El cuerpo siempre es JSON válido; si el request envía JSON malformado → 400.

### Serialización de recursos ✅

- **Nombres en camelCase** en el payload — las claves JSON son EXACTAMENTE los nombres de propiedad del dominio, sin transformación: `clienteId` → `clienteId`. Si la propiedad se llama así en PHP, así se ve en la API. El id de la raíz aparece como `id`.
- Los ValueObjects embebidos se serializan anidados SIN prefijo: `Money $monto` → `{ "monto": { "amount": 10.5, "currency": "ARS" } }`.
- `#[HasMany]`/`#[ManyToMany]` → array de objetos anidados; cada hijo con su `id`.
- `#[Projected]` se incluye junto al estado del constructor.
- `#[Field(expose: false)]` se EXCLUYE del payload (persistido pero invisible).
- **Timestamps derivados por el framework:** las columnas en BD son `created_at`/`updated_at`, pero en el payload SIEMPRE camelCase: `createdAt`, `updatedAt` (default expuestos). `deletedAt` (cuando `softDelete: true`) NUNCA se expone en el payload.
- Los valores nulos se serializan como `null`.

### Respuestas de operación (status codes) ✅

| Operación | Status | Cuerpo |
| --- | --- | --- |
| POST create | **201** | El recurso creado (serializado) + header `Location` a su GET |
| GET one | **200** | El recurso (proyección tipada o entidad serializada) |
| GET list | **200** | Array plano si `paginate: false`; envelope si paginado (ver abajo) |
| PUT/PATCH | **200** | El recurso actualizado |
| DELETE | **204** | Sin cuerpo |
| `#[Action]` (POST) | **200** | Resultado del método serializado (o `204` si devuelve void) |
| `#[Action]` + `#[Queued]` | **202** | `{ "accepted": true }` — el trabajo se despachó |
| GET con `If-None-Match` (ETag, ver §15.3) | **304** | Sin cuerpo — el cliente tiene la versión vigente |
| `#[Action]` que devuelve `Generator` (Streaming/SSE, ver §13) | **200** | Stream chunked con media-type de la ruta (no JSON) |

### Respuestas binarias / descargas (producción)

El contrato base es JSON, pero las subidas usan `Storage` (§13 Upload) y el dev necesita SERVIR esos archivos. Regla:

- Un `#[Action]` cuyo return type es `StorageFile` (ValueObject del framework: `path`, `name`, `mime`, `disposition`) responde la descarga: streaming del archivo con `Content-Type` del mime, `Content-Disposition: attachment|inline; filename=...` (según `disposition`), status 200. No va por el serializador JSON.
- `StorageFile` se obtiene del puerto `Storage` (`Storage::get()`/`Storage::download()`); el dominio devuelve el objeto y el framework hace el streaming chunked (sin cargar el archivo entero en memoria).
- `Content-Length` disponible → se envía; desconocido → chunked. Si el archivo no existe → 404 con contrato de error estándar.
- Seguridad por el default de `#[Action]` (`public` hasta que se declare); el dev protege la descarga con `security` como cualquier ruta. No hay carpeta `public` servida por el framework: TODA descarga pasa por una ruta `#[Action]` derivada (paridad del rol de `storage:link`, sin el symlink).

### Envelope de listas paginadas ✅

`{ "data": [...], "meta": { "page": 2, "perPage": 25, "total": 137, "totalPages": 6 }, "links": { "first": "...", "prev": "...", "next": "...", "last": "..." } }` — alineado con el paginador de Laravel (claves meta en camelCase). Sin paginación (`paginate: false` o recurso no-lista): respuesta plana, sin envelope.

### Contrato de errores (único, consistente) ✅

Todo error devuelve el mismo shape:

```json
{ "error": { "code": "orden.pagada_dos_veces", "message": "La orden ya fue pagada", "details": { "email": ["El email no es válido"] } } }
```

- `code`: string legible; el del dominio sale del `DomainException` (o default por status); `details` se omite si no aplica.
- Validación/Hidratación → **422** con `details` campo por campo.
- `DomainException` (regla de negocio) → **409** con su `code`; **409 `optimistic_lock`** — conflicto de versión optimista (`If-Match` del ETag no coincide, ver §10/§15.3).
- JSON inválido → **400** (`code: "json.parse_error"`).
- 401 sin autenticar / **403** sin autorizar (`security`, `may{Operación}`) / **404** no encontrado / **413** cuerpo o upload excede los límites (`code: "http.body_too_large"` / `"http.upload_too_large"`, ver Límites) / **408** request excede `http.limits.request_timeout` (`code: "http.request_timeout"`) / **429** rate limit con header `Retry-After` / **500** error no capturado (con `debug: true` en dev muestra detalles; en prod solo `code: "internal"`).
- En dev, si `config.debug`, el error 500 adjunta trace; en prod NUNCA.

### Límites duros de request (config `http.limits`) 🚫

Contrato único (no disperso): el pipeline aplica TODOS antes de tocar el dominio.

| Límite | Default | Comportamiento |
| --- | --- | --- |
| `http.limits.body_limit` | 8MB | Cuerpo del request (JSON/form) — excedido → **413** `code: "http.body_too_large"` |
| `http.limits.upload_max` | 8MB | ARCHIVO individual (`UploadedFile`) — excedido → **413** `code: "http.upload_too_large"` (un request con varios archivos suma contra el `body_limit`) |
| `http.limits.raw_body_limit` | 32MB | Streaming/SSE `Generator` (límite tolerable de buffer antes de chunkear; si el Generador emite más, se transmite de a partes sin acumular) |
| `http.limits.request_timeout` | 30s | Tiempo máximo del pipeline completo (incluye dominio + persistencia); excedido → **408** `code: "http.request_timeout"` y la tx se aborta (rollback). En `serve` controla el worker; detrás de FPM el server web puede acotar antes — el contrato del framework es el suyo. |
| `http.limits.uri_max` | 8KB | Longitud máxima de la URI (filtro de rutas/parámetros + protección de logs) — excedido → **414** `code: "http.uri_too_long"` |

Los límites se validan ANTES del Hydrator (413 temprano si `Content-Length` ya lo revela); un request que pase `body_limit` pero falle `raw_body_limit` en streaming se aborta a mitad sin half-render.

### Idempotency-Key (para clientes que reintentan) 🚫

Métodos POST (create + `#[Action]` con efectos) y PUT/PATCH aceptan el header opcional `Idempotency-Key: <string>`. Contrato:

- El emisor envía la misma key al reintentar; el framework devuelve la respuesta ORIGINAL sin re-ejecutar el efecto (200/201/202 + body, o el error correspondiente de la primera ejecución).
- El framework persiste `(key, ruta, hash_payload, status_code, respuesta_serializada, expires_at)` en una tabla derivada con TTL configurable (`http.idempotency_ttl`, default 24h). Insert con conflict → replay de la respuesta.
- Keys distintas o ausentes → comportamiento normal. Una misma key en rutas/payloads distintos → 422 `code: "idempotency_key_reused"`.
- Costo: una tabla interna + un índice; es el contrato que las APIs modernas esperan (Stripe-style) y evita doble pago en reintentos del cliente.
- **GC (producción):** las entradas vencidas NO se borran solas — la tabla crecería indefinidamente. Borrado de vencidas: en cada insert de `<root>/var/db/idempotency_keys` se purga un lote acotado de `expires_at < now` (barato, sin tarea externa); además `schedule:run` ejecuta una purga completa periódica (`http.idempotency_gc`: default diario).

### Validación (autoridad única del mini-DSL) ✅

Unificada acá (antes partida entre §5 y esta sección). `validate` acepta reglas en una gramática probada (subconjunto del DSL de Laravel, sin inventar sintaxis):

- **Base — por tipo PHP derivada por defecto** (int, string, enum, ValueObject): no hay que declararla. `required`/`nullable` TAMPOCO se escriben: se derivan del tipo (sin default y no-nullable → required; `?T` → nullable).
- **Explícitas (escalares):** `'min:3'`, `'max:100'`, `'email'`, `'url'`, `'regex:...'`, `'same:campo'`, `'different:campo'`, `'between:min,max'`, `'digits:n'`, `'integer'`, `'numeric'`, `'array'`, `'distinct'`, `'confirmed'` (valida que exista `X_confirmation` igual a X — para passwords), `'required_if:campo,valor'`.
- **Referenciales (sin código):** `'unique:tabla,col'`, `'exists:tabla,col'` — consultan la BD vía `QuerySource`.
- **Archivos:** `'mimes:pdf,jpg'`, `'mimetypes:pdf,jpg'`, `'max:10240'`, `'dimensions:min_width=100'`.
- Reglas CUSTOM: la app registra en bootstrap un nombre → callable/clase que implementa `Rule` (con mensaje propio). Cero invento de sintaxis: es el patrón de Laravel, sin capa nueva.
- Mensajes por defecto derivados para cada regla (idioma base: inglés); override global en `config.validation.messages` y mensaje por regla inline: `'cuit'` con `messages: ['cuit' => '...']` (param extra de `#[Field]`). Config `config.validation.locale` fija el idioma base de los mensajes por defecto (solo los que trae el framework: `en`, `es`); los override de la app ganan siempre.
- El framework devuelve 422 con errores campo por campo, derivado de la metadata.
- Los query params de filtro/orden del DSL `QuerySource` se validan contra las columnas de metadata: columna inexistente o valor inválido → 422 con detalle (evita inyección al query builder).

**Regla de oro:** las reglas de negocio del dominio NUNCA viven en metadata de campo — esas van en métodos de la entidad.

## 15. Capa de producto — brechas del mercado cubiertas ⚠️

Cobertura de los conceptos que el mercado trata como maduros y que faltaban: contrato de API, operabilidad, semántica HTTP de cache, interoperabilidad estándar y entrega durable de eventos. Cada uno es spec de implementación.

### 15.1 Contrato de API — OpenAPI derivado de la metadata 🚫

El motor de metadata ya conoce rutas, payloads, validaciones y read models: el OpenAPI es otro proyector de esa misma fuente, no una pieza nueva. `/openapi.json` se sirve en dev (config `openapi.expose: 'dev'|'never'`) y `boilerfree openapi` lo genera a un archivo (para CI/versionado). El schema deriva:

- Paths/methods desde `#[Entity]` (CRUD), `#[Action]`, `#[Query]`.
- Request body desde el constructor de la entidad (create/update) y los parámetros de `#[Action]`.
- Respuestas desde los read models (return types) y el contrato de §14 (status codes, errores, envelope paginado).
- Validación (422 `details`) desde el mini-DSL.
- `security` desde `#[Entity(security)]`/`#[Action(security)]` (bearerAuth).
- Versionado desde `version` (prefijos `/v1/...`).

Swagger UI en dev es opcional (app-level): el contrato es el archivo, la UI es un viewer.

### 15.2 Operabilidad — health, métricas, request-id, logs estructurados ⚠️

- **Health checks** (solo si `ops.enabled: true`): `GET /healthz` (liveness: proceso vivo) y `GET /readyz` (dependencias: ping a `QuerySource`, cache y queue si configuradas) → 200/503 con JSON. Sin dependencias, `readyz` equivale a `healthz`.
- **request-id**: middleware automático del núcleo — acepta `X-Request-Id` entrante o genera UUIDv7; se propaga como contexto del `Logger` (PSR-3) y se devuelve en el header de la respuesta. Correlación de logs por request.
- **Logs estructurados**: el núcleo loguea por request (método, ruta, status, duración, request-id) con contexto estructurado; el adapter `Logger` los serializa (line JSON en prod si el adapter lo soporta).
- **Métricas** (puerto `Metrics`, adapter por defecto en memoria + endpoint `/metrics` Prometheus en dev si `ops.metrics: true`): requests por ruta (count/latencia/status), errores por tipo, tamaño de respuesta. La app bindinguea el collector real cuando quiera.
- **Tracing** (puerto `Tracer`, ya, §7): el puerto existe en v1 con adapter por defecto no-op (cero costo); si la app necesita trazado, bindinguea el adapter real (OpenTelemetry) en el pipeline. El adapter REAL no es obligatorio del framework: es app-level, opcional declarado, no bloqueante. Decisión declarada.

### 15.3 Semántica HTTP de cache — ETag / 304 / Cache-Control ⚠️

- Todo GET derivado (recurso individual o lista) calcula `ETag` automáticamente: hash del contenido serializado (incluye el envelope). El cliente manda `If-None-Match` → 304 sin body si coincide.
- **El mismo ETag alimenta el bloqueo optimista en escrituras:** PUT/PATCH con `If-Match: <etag>` → 409 `optimistic_lock` si el ETag recibido no coincide con el estado actual (mecanismo interno `optimistic_version`, autoridad §10).
- `Cache-Control` derivado de `#[Query(cache: TTL)]`: `max-age=TTL`; por defecto `no-cache` para mutaciones y GET sin cache. Override por config `http.cache_control`.
- La invalidación NO es manual: el ETag es hash del contenido, cambia solo cuando cambia el contenido. La cache de aplicación (`#[Query(cache)]`) y la de protocolo (ETag) son capas distintas y conviven.

### 15.4 Interoperabilidad — PSR-7 y PSR-15

- El Request/Response del núcleo implementa **PSR-7** (`Psr\Http\Message`) y el pipeline **PSR-15** (`MiddlewareInterface`/`RequestHandlerInterface`). El middleware del ecosistema (Laminas, Slim, comunidad) cuelga directo en config `middleware`.
- El framework traduce: request PSR-7 → payload del dominio (Hydrator, §6.4) y dominio → response PSR-7 (serializador, §14). El dev nunca ve ni PSR-7 ni HTTP salvo que escriba middleware.
- Implementación mínima propia de PSR-7 por defecto (sin dependencia externa); si el host ya trae una (nyholm/psr7, Laravel app), el puente la bindinguea.

### 15.5 Outbox — entrega durable de eventos

- El despacho de `releaseEvents()` se persiste en la tabla `outbox` (derivada de metadata) **dentro de la misma transacción** de persistencia: el evento es parte del commit, no un efecto posterior.
- Los listeners se publican por el puerto `EventDispatcher` (adapter por defecto `outbox`): `boilerfree outbox:dispatch` procesa los pendientes y marca entregados; en dev el adapter sincrónico publica justo después del commit.
- Garantía **at-least-once**: si el proceso muere post-commit, el worker recupera del outbox. Los listeners deben ser idempotentes por `eventId` (convención: el evento trae su id).
- Cambio respecto a la definición previa: antes "in-process tras persistir" perdía eventos entre commit y dispatch; el outbox lo cierra por construcción.

### 15.6 Páginas legales del esqueleto (privacy / terms)

**Rol:** el framework NO escribe contenido legal — el texto legal es contenido editorial con peso legal (jurisdicción, negocio y datos tratados deciden el contenido; copiar texto genérico fabrica una falsa sensación de cumplimiento). Lo que el framework provee es la ESTRUCTURA para que toda app nueva tenga las páginas sin escribirlas a mano: plantillas con secciones estándar vacías, rutas derivadas, links en el layout y una alerta de "pendiente de revisión".

- **Comandos (§11.1):** `boilerfree make:legal:privacy` y `boilerfree make:legal:terms` generan `templates/legal/privacy.php` y `templates/legal/terms.php` (layout default) con las secciones típicas VACÍAS y comentarios de qué completar en cada bloque (datos recopilados, uso, derechos del usuario, cookies, contacto), más el marcador `<!-- boilerfree:legal-pending -->` al inicio. NUNCA generan texto legal completo.
- **Rutas derivadas por convención:** toda vista en `templates/legal/*.php` sin `#[Action]` deriva `GET /<nombre>` pública (`privacy.php` → `/privacy`, `terms.php` → `/terms`). La carpeta `templates/legal/` es la ÚNICA excepción a "las vistas requieren `#[Action(view:)]`" — el framework registra esas rutas automáticamente con guard `public` y security headers por defecto. Si el dev quiere restringirlas, las redeclara como ruta `view:` normal.
- **Links automáticos en el footer:** el layout derivado (`templates/layouts/app.php`) incluye un bloque de links legales con las páginas que existan — el dev NO los escribe a mano.
- **Alerta de pendiente en prod:** `boilerfree check` en perfil prod detecta el marcador `boilerfree:legal-pending` en `templates/legal/` y emite warning "páginas legales sin revisar" (no falla). Al servir una página legal con marcador en prod, el framework loguea el evento vía `Logger` una vez por boot (nunca por request), sin bloquear la respuesta.

## 16. Paridad de experiencia (barra mínima)

Un dev que viene de Laravel prueba el framework y espera que el camino feliz COMPLETE. Esta lista es el estándar mínimo que Boilerfree debe demostrar — no features copiadas, sino experiencia que no decepcione:

1. **Instalación simple** — `composer install` + config/env + `serve` y la API responde.
2. **`migrate` crea el schema** derivado de la metadata.
3. **CRUD completo por entidad** (create/read/update/delete), sin escribir un controller.
4. **Validación 422** campo por campo con payload inválido.
5. **Paginación** `?page=2` → `data` + `meta`.
6. **Auth real** — login + token + endpoint protegido (puerto `Authenticator` con adapter demo).
7. **Tests corriendo** — `phpunit` pasa de entrada.
8. **Agregar una entidad nueva = `boilerfree make:entity <Contexto/Nombre>` + completar sus invariantes** (o directamente 1 clase a mano) y TODO lo demás aparece. El momento "wow": no existe en Laravel ni en ningún lado.
9. **Errores legibles** — 404/422 con formato consistente, no stacktrace pelado.

**Regla:** si una de estas 9 no se demuestra, el framework no está listo para mostrarse. El spike valida el contrato contra esta lista completa — la experiencia ES el producto, no un accesorio.

> La **config/env mínima** que faltaba quedó definida en §13 (Herramientas y DX): `config/boilerfree.php` + `.env` + servicio interno `Config`. Sin eso falla el punto 1; ya es spec.

## 17. Ejemplo de referencia (para el spike técnico)

`Orden` (raíz con `#[Entity]`, `clienteId` escalar, `LineaOrden` con `#[HasMany]`, `Money` ValueObject, método `pagar` con `#[Action]`, método `total` con `#[Projected]`) + `CatalogoService` con `#[Query]`. El spike debe validar:

```php
#[Entity]
class Orden {
    public function __construct(
        #[Field(id: true)] public readonly ?string $id = null, // null → framework genera UUIDv7
        public readonly int $clienteId,
        /** @var list<LineaOrden> */
        #[HasMany] public readonly array $lineas, // target derivado del docblock
        public readonly Money $monto,            // ValueObject embebido por propiedades
        #[Field(expose: false)] public readonly string $hashInterno, // persistido, nunca en la respuesta
    ) {}

    #[Action(security: 'authenticated')]
    public function pagar(): void { /* invariantes */ }

    #[Projected]
    public function total(): Money { /* suma */ }
}
```

El dev escribe solo esto: entidad + 3 desviaciones de convención (`id: true`, `security`, `expose: false`). Sin `#[Field]` por propiedad, sin target, sin returns, sin ids manuales, sin rutas.

El spike debe validar, en orden:

1. Hidratación de agregado con hijos + ValueObject anidado desde row.
2. Routing derivado de `#[Action]` + `#[Query]`.
3. Paso a paso: el developer escribe solo dominio y no toca nada más.

## 18. Pendientes (implementación)

- [ ] Implementar el esqueleto definitivo de directorios del framework (librería Composer) + `config/boilerfree.php` + `.env` + servicio `Config` (§13).
- [ ] Implementar el motor de metadata: atributos, escaneo (`src/Domain/`), cache en disco con invalidación mtime + `--clear-cache` (§6.3).
- [ ] Implementar Hydrator recursivo (entidades, ValueObjects, `#[HasMany]`, `#[ManyToMany]`, argumentos de `#[Action]`/`#[Query]`, `DateTime` ISO-8601) (§6.1, §6.4).
- [ ] Implementar UUIDv7 (§6.2).
- [ ] Implementar QuerySource (puerto) + adapter PDO por defecto: filter/order/paginate/aggregate + join simple + savepoints (§9, §13).
- [ ] Implementar controller CRUD genérico + routing derivado + envelope + paginación derivable + serialización con `expose` (§7, §9).
- [ ] Implementar contrato de API (§14): serialización camelCase 1:1 con propiedades del dominio + ValueObjects anidados + timestamps derivados (createdAt/updatedAt en payload, created_at/updated_at en BD), status codes, envelope paginado con links, contrato de errores único (code/message/details), 406/400/413/429, y mini-DSL de validación completo (reglas base + explícitas + referenciales + archivos + custom + mensajes + validación de filtros).
- [ ] Implementar auth de rutas: guards `token` (Bearer) + `session` (con tabla de sesiones server-side + GC, ver §13), `auth.routes.login` + throttling de auth con lockout por IP/cuenta, 429 + `Retry-After` (§13, §14).
- [ ] Implementar CLI: `new`, `migrate` (+ rollback + status derivado del diff metadata↔BD), `migrate:fresh [--seed]`, `key:generate`, `seed`, `routes`, `validate`, `serve`, `tinker` (+ `--execute`), `schedule:run`, `schedule:list`, `queue:work`, `queue:listen`, `debug`, `optimize`/`optimize:clear`, `down`/`up`, `about`, `config:show`, `test` (wrapper PHPUnit), `queue:failed`/`queue:retry`/`queue:flush`, `openapi`, `outbox:dispatch`/`outbox:status` (§11, §13).
- [ ] Implementar comandos `make:` de fuente de verdad: `entity`, `vo`, `service`, `view`, `job`, `event`, `listener`, `seed`, `middleware` con plantillas, convención de carpetas por concepto (nunca `Entities/`/`Services/`), validación de nombre y rechazo explícito de lo derivado ("eso es derivado, no se genera") (§11.1, §7, §13).
- [ ] Implementar puertos con adapters por defecto: `Logger` (PSR-3/syslog), `Authenticator` (demo), `Cache` (filesystem), `Queue` (sync), `EventDispatcher` (sync), `Mailer` (log), `Schedule`, `Hasher`, `Encrypter`, `Http` (cURL, PSR-18: timeout/retries/backoff de config), `Storage` (filesystem), `Clock` (system), `ErrorReporter` (→ Logger), `Renderer` (PHP plana + `e()`/`raw()` + layout), `Tracer` (no-op) (§13).
- [ ] Implementar política de tipado de frontera: `declare(strict_types=1)` en el núcleo, Hydrator sin coerción (type_mismatch → 422), `boilerfree check` (validate + chequeo de tipos del Hydrator) + skeleton con Pint/PHPStan para CI (§6.4, §11, §13).
- [x] Implementar pipeline `Middleware` + CORS adapter en config (§13). Ambos certificados: `MiddlewareChainTest` y `CorsPreflightContractTest` (20 tests), que encontraron que el preflight no se contestaba — ver §12.
- [ ] Implementar rate limiter (§13). Declarado en config y scaffold; **no hay adapter**. Declarado como `RuntimeCapabilities::RATE_LIMIT => false` para que `boilerfree check` lo reporte en vez de callarlo.
- [ ] Implementar security headers (§13). Igual: sección en config y scaffold, ningún adapter. `RuntimeCapabilities::SECURITY_HEADERS => false`.
- [ ] Implementar streaming/SSE: return type `Generator` en `#[Action]` → respuesta chunked con media-type configurable, sin buffer completo (§13).
- [ ] Implementar locks pesimistas: `#[Action(lock: true)]` → `SELECT ... FOR UPDATE` sobre la raíz al abrir la tx (§5, §13).
- [ ] Implementar trusted proxies: config `trusted_proxies` ajusta `Request` (https, client IP) ANTES del pipeline (§13).
- [x] Implementar índices de negocio: `#[Field(index: true|'unique')]` + `#[Entity(indexes: [...])]` en el DDL derivado (§13).
- [ ] Implementar generador OpenAPI derivado de metadata: `/openapi.json` en dev + `boilerfree openapi` (paths, bodies, read models, errores §14, security, versionado) (§15.1).
- [ ] Implementar operabilidad: `GET /healthz` + `GET /readyz` (200/503), request-id (header entrante o UUIDv7, contexto Logger + respuesta), logs estructurados por request, puerto `Metrics` + `/metrics` Prometheus (dev) (§15.2).
- [ ] Implementar maintenance mode: `boilerfree down [--retry|--secret|--allow]` / `up` con 503 JSON + `Retry-After` + healthz/readyz exentos (§13).
- [ ] Implementar build step de prod: `boilerfree optimize` / `optimize:clear` (metadata + rutas + config cache en disco; boot lee cache en prod) (§13).
- [ ] Implementar error reporting: puerto `ErrorReporter` + report de 500s, jobs fallidos y console; adapter default → Logger; sanitización de secrets en stack (§13).
- [ ] Implementar Idempotency-Key: header en POST/PUT/PATCH, tabla derivada con TTL `http.idempotency_ttl`, replay de respuesta original + **GC de vencidas** (purga en insert + `schedule:run` diario vía `http.idempotency_gc`) (§14).
- [ ] Implementar respuestas binarias/descargas: ValueObject `StorageFile` + `#[Action]` con return type `StorageFile` → streaming chunked con `Content-Type`/`Content-Disposition`, 404 estándar si no existe, sin carpeta public servida (§14).
- [ ] Implementar invalidez de `#[Query(cache)]` por escritura: tracking de tablas leídas por query; invalidar entradas cacheadas al persistir cambios sobre esas tablas; fallback conservador si el adapter no expone el plan (§13).
- [ ] Implementar protección de migraciones: `--pretend` (SQL preview), `--force` obligatorio en prod para operaciones destructivas, advisory lock en `QuerySource` para batches concurrentes (multi-instancia) (§11, §13).
- [ ] Implementar timeout de jobs: param `timeout` en `#[Queued]` (default 60s), worker mata el job excedido y aplica tries/backoff; `queue:work --timeout` global (§5, §11, §13).
- [ ] Implementar regeneración de session id anti-fixation en login del adapter `session` (nuevo id, borra el viejo, rota la cookie) (§13).
- [ ] Implementar restore de soft-deletes: `PATCH /<raiz>/{id}/restore` derivado cuando `softDelete: true`, security `authenticated` + `mayRestore` (§10).
- [ ] Implementar alerta de drivers en `check` (perfil prod): queue/cache/mailer en `sync`/sin binding real → warning (§11).
- [ ] Implementar `env:encrypt`/`env:decrypt` (`.env.encrypted` con `APP_KEY`; paridad `artisan env:encrypt`) (§11).
- [ ] Implementar `config.validation.locale` para mensajes por defecto del mini-DSL (`en`/`es`, overrides ganan) (§14).
- [ ] Implementar jobs únicos / overlap / DLQ: `unique`, `uniqueFor`, `withoutOverlapping` en `#[Queued]` (+ locks en `Cache`) y tabla/cola fallida con `queue:failed`/`queue:retry`/`queue:flush` (§13).
- [ ] Implementar renderizado de vistas: puerto `Renderer` (adapter PHP plana + `e()`/`raw()` + `csrf_token()`, layout derivado), param `view:`/`layout:` en `#[Action]`, content-negotiation JSON vs HTML según `Accept`, y validación CSRF en rutas de vista con guard `session` (§13, §14).
- [ ] Implementar páginas legales del esqueleto: `make:legal:privacy`/`make:legal:terms` (secciones vacías + marcador `<!-- boilerfree:legal-pending -->`, NUNCA texto legal completo), rutas derivadas `GET /privacy` y `GET /terms` desde `templates/legal/`, links automáticos en el footer del layout, y alerta en `check` (prod) cuando el marcador siga presente (§11.1, §15.6).
- [ ] Implementar semántica HTTP de cache: ETag automático en GET + `If-None-Match` → 304, `Cache-Control` desde `#[Query(cache)]` + config `http.cache_control` (§15.3).
- [ ] Implementar PSR-7 (Request/Response) + PSR-15 (pipeline de middleware interoperable); implementación mínima propia por defecto (§15.4).
- [ ] Implementar outbox: tabla derivada + persistencia de `releaseEvents()` en la misma tx + `boilerfree outbox:dispatch` (at-least-once, listeners idempotentes por `eventId`) (§15.5).
- [ ] Implementar perfiles de config: `config/boilerfree.<env>.php` override + `.env` gana; `dev`/`test`/`prod` (§13).
- [ ] Implementar convenciones: `may{Operación}` (authorización por objeto) y `releaseEvents()` (eventos de dominio) (§13).
- [ ] Implementar scoping de autorización en LISTADOS: parámetro `User $user` inyectado en `#[Query]` + convención `scopeFor(User, QuerySource)` aplicada automáticamente en consultas derivadas de la raíz; `check` FALLA si una raíz con `mayRead` tiene consulta de listado sin `User` ni `scopeFor` (§13).
- [ ] Implementar retry de transacciones por contención: SQLSTATE 40001/40P01 (PG) / 1213·1205 (MySQL) → reintento completo hasta `db.transaction_retries` (default 3) con backoff+jitter; unique_violation/FK no se reintentan (§10).
- [ ] Implementar ciclo de vida de procesos: SIGTERM/SIGINT con drenado en `queue:work`/`queue:listen`/`schedule:run`/`serve` (deja de tomar trabajo, termina el actual, exit 0; segunda señal = aborto inmediato; at-least-once) (§13).
- [ ] Implementar retención/GC de datos operativos: `ops.outbox_retention_days` (default 7), `ops.failed_jobs_retention_days` (default 30) + purga en `schedule:run`; validar que `queue:retry` solo aplique dentro de la ventana (§13).
- [ ] Implementar límites duros de request: `http.limits` (body_limit 8MB→413, upload_max 8MB→413, raw_body_limit 32MB, request_timeout 30s→408, uri_max 8KB→414) validados ANTES del Hydrator (§14).
- [ ] Implementar `boilerfree new` con el árbol completo de §11.2: el framework como dependencia Composer (no copia), ÚNICO entrypoint `public/index.php`, `bootstrap.php` con bindings de la app, `var/` gitignored y descartable, wizard con adapter de persistencia (§11, §11.2).
- [ ] Test suite del framework (Hydrator, metadata, routing, UUIDv7, validación) + factories + HTTP tests del experimento (§12).
- [ ] v2: hash de contenido como fallback de invalidación de metadata cache (Docker volumes).
- [ ] Spike técnico con el ejemplo de §17: validar contrato completo de punta a punta contra la paridad de experiencia de §16.
- [ ] Diseñar el experimento pre-test/post-test conforme a la solución final.
- [ ] Alinear los documentos de la tesis con esta definición (después de validar la solución).
---

## Estado de implementación — 2026-09-26

Fuente única del **detalle** de cada hueco. Los marcadores de las secciones de arriba dicen si el runtime cumple el concepto; ** acá está el porqué y el qué falta, una sola vez.** Si un hueco se cierra, se edita esta lista y el marcador de su sección: son las dos únicas ediciones que un cambio de estado produce.

### Cerrado

| Casa | Qué quedó en el runtime |
|------|------------------------|
| §5, §6 | Contrato de 9 atributos con defaults exactos; motor de metadata (escaneo, validación, cache); Hydrator de frontera estricta; UUIDv7 |
| §6.1–§6.4 | VOs embebidos con expansión `<column>_<parte>` compartida entre derivación de DDL y runtime; derivación única de rutas (`ClassMetadata::deriveRoutes()`) |
| §8 | `#[HasMany]` con FK en la tabla hija; `#[ManyToMany]` con tabla pivot derivada (cerrado 2026-09-26) |
| §9 | `QuerySource` + adapter PDO: filter, order, paginate, aggregate, join, savepoints, whitelist de columnas |
| §10 | Retry de contención en el núcleo (solo `40001`/`40P01`, nunca unique/FK) y lock optimista |
| §11 | 18 comandos core + `make:*` + `migrate*` + `outbox:*` + `queue:*` + `check` + `optimize*` + `make:legal:*` + `down`/`up` |
| §13 | Auth real: `security` aplicado, `esAdmin()` fail-closed, hooks `may*`, scoping de listados con fail-closed en boot |
| §14 | Serialización camelCase 1:1, status codes, envelope paginado, contrato de errores, **mini-DSL ejecutado** (§14.5) |
| §15.2 | `healthz`/`readyz` exentos de maintenance, `Retry-After`, `down`/`up` |

### Abierto — huecos concretos

| Casa | Estado | Qué falta exactamente |
|------|--------|------------------------|
| §10 lock optimista | ⚠️ | Funciona **solo** si la tabla tiene `optimistic_version`. `DiffEngine` la agrega al derivar, y una tabla preexistente también la recibe por `ALTER`. `check` ya reporta las que no la tienen. |
| §12 tests | ⚠️ | La suite tiene 542 tests verdes, pero **auth, concurrencia y validación siguen sin cobertura de regresión**: se verificaron con probes desechables que ya no existen. |
| §14 CSRF / idempotencia / `http.limits` | ⚠️ | El código existe y corre, sin test que lo certifique. Faltan: emisión y validación de CSRF, expiración y supervivencia a reinicio de la clave de idempotencia, y el límite de **tamaño del body** (el de URI sí está cubierto). |

### Cerrado — 2026-09-26 (cuarta ronda — cobertura que muerde)

Las tres rondas anteriores dejaron el runtime honesto. Esta ronda es la de §12:
los tests que existen **por** la declaración y no de rebote. Cada defecto de
abajo se reintrodujo a propósito para comprobar que el test que lo nombra se
cae; un test que no muerde no es evidencia.

| Casa | Qué estaba mal | Qué resolvió |
|------|-----------------|----------------|
| §13 auth | El hook `may*` devolvía el `false` del guard, así que un hook que **sí** quería negar caía en la rama de "sin veredicto" y la petición pasaba igual. Un guard que lanzaba una excepción ALSO pasaba, porque el `catch` devolvía `null` en vez de denegar. Y `esAdmin()` que no existe, que devuelve algo *truthy* pero no `true`, o que lanza, concedía acceso igual que un `true`. | Todo fail-closed: falta el método, no es `true`, o lanza ⇒ denegar. El catch de la policy deniega. `SecurityContractTest` (26 tests) con `Administrador`, `UsuarioComun`, `Forastero`, `GuardExplota` y `AdminAmbiguo` como actores. Siete grupos de defecto verificados en rojo. |
| §13 scope de listado | El filtro de owner derivado de la clase de usuario se calculaba y se descartaba; `scopeFor()` se llamaba y su resultado se ignoraba. Un listado sin scope devolvía **todas** las filas a un usuario anónimo, con la misma forma de respuesta que un listado correctamente acotado. | `ScopedQuerySource` decora al `QuerySource` — que es lo que el puerto devuelve, no una `QuerySource`, así que el contrato de §13 es un decorador y el fixture tiene que existir. Un `CountingResolver` demuestra que el actor se resuelve **una** vez por request. |
| §10 ETag de create | `create()` publicaba `new VersionToken(1)` hardcodeado mientras el `INSERT` tomaba el default de la columna, que es `0`. El POST respondía `ETag: "1"`, el `GET` siguiente respondía `ETag: "0"`, y el cliente que obedecía la primera respuesta tenía su **primer** write rechazado como stale — con un token que el framework mismo acababa de darle. | `persist()` cuenta la escritura e inserta `optimistic_version = 1`; `create()` **lee** la versión con `versionOf()` en vez de suponerla. Con el default del DDL en 0 se puede distinguir una fila que nadie escribió (seed, import) de una que el framework creó. Test contra la columna, no contra el status. |
| §10 `If-Match` con lista | El docblock prometía "una lista separada por comas de ETags" y el código tomaba el primer candidato parseable y comparaba sólo ése. Un cliente que acumula validadores — el mismo tras un 304 o un 409, el más cuidadoso de todos — era rechazado por listar uno viejo primero. | `candidates()` devuelve todos, en las dos grafías (con y sin comillas), y un `If-Match` se acepta si **cualquier** validador describe esta versión. |
| §10 retry de contención | `CONTENTION_STATES` era `['40001', '40P01']`, pero el equivalente de MySQL del lock timeout (error 1205) sí se mapeaba a contención. El `55P03` de Postgres — *lock_not_available* — quedaba como error final: un row ocupado por otra transacción se traducía en un **500**, que es la peor traducción posible de "esperá un momento". | `55P03` entra al set de contención, con el motivo escrito: el bloqueo es transitorio y quien lo tenía puede ya no estar. `57014` (statement timeout) queda **fuera** a propósito: una sentencia que se quedó sin tiempo se quedó sin tiempo por una razón, y repetirla multiplica la carga que la causó. |
| §14.5 `required` escrito a mano | La regla derivada respeta un PATCH parcial (un campo que el cliente no menciona es un campo que decidió no cambiar) pero la escrita a mano no: `required` explícito sobre un campo con default se leía como obligatorio también en un PATCH. Si un PATCH podía omitir un campo dependía de **cómo estuviera declarado**. | `required` y `required_if` sobre un campo ausente no corren en un PATCH, estén derivadas o escritas. En un create siguen corriendo: el otro lado del caso, y la razón por la que el arreglo no es simplemente "borrar el `required` explícito". Un campo con default **y** `required` escrito tiene su propia raíz de fixtures, para probar los dos lados sin que cada control de 201 tenga que cargar un campo que no le interesa |
| §14.5 `min` y `digits` | `whenNotEmpty()` salta las reglas cuyo valor es `''`, y eso tiene sentido para una regla de FORMATO: un correo vacío no tiene formato. Un mínimo es una afirmación sobre longitud, y la cadena vacía es el único valor más corto que el límite: `min:3`-era la regla que el valor más corto posible pasaba. `digits:4` pasaba con `''` por la misma puerta. | `min` y `digits` tratan `''` como un valor y no como una ausencia. La ausencia la resuelve la presencia, antes. Un campo que el cliente **omitió** sigue sin quejarse; uno que envió vacío recibe el error |
| §14.5 `between` | La comparación exigía `is_numeric($value)`, así que `between:a,z` — la forma que la gramática invita para un código, un slug o un estado — rechazaba **todos** los valores, incluidos los que estaban dentro del rango. | Los límites numéricos comparan como números; los de string comparan como strings; un número contra un rango de strings es una contradicción y se rechaza, en vez de pasar con un límite que nunca aplicó |
| §14.5 regla desconocida | — (comportamiento correcto, antes sin test) | Una regla que el motor no implementa se **reporta** como `custom` en vez de darse por cumplida. Es la falla más profunda de un motor de reglas: el desarrollador ve un 201 y concluye que su ventana de fechas está abierta cuando nada la verificó. Caracterizado, no corregido: ya era así |
| §13 CSRF: el guard no guardaba | `validateCsrf()` llamaba `SessionStore::getSession()` y `storeCsrfToken()`, dos métodos que **el puerto no tiene**. Cada llamada lanzaba un `Error`, y el `catch (\Throwable) { return null; }` que lo envolvía — comentado como *"fail-open for non-view routes"* — convertía ese `Error` en **"permitido"**. Fail-OPEN por diseño, y el diseño estaba tapando un bug propio. La capacidad `csrf` valía `false` por honestidad; lo que la capacidad no decía es que el feature estaba *activo y decorativo* a la vez | El guard resuelve la cookie él mismo (una sola regla para el nombre, en vez de dos lugares que pueden discrepar), y falla **cerrado** ante una cookie de sesión: una sesión inexistente, vencida o nunca tokenizada se rechazan por igual. El `catch` se quitó: un guard que no se puede evaluar no es un guard, es decorativo. El token vive en el `payload` que la tabla ya tenía y nadie leía, y el puerto ganó `csrfToken()` / `storeCsrfToken()` — **emitir es tarea de la aplicación** (en el login), porque el framework no tiene login y no tiene un momento honesto para acuñar una credencial. El token crudo jamás se guarda: la tabla tiene `sha256` |
| §13 CSRF: cuerpo de formulario | El comentario del código decía *"with view (HTML forms)"* y el guard leía `_token` del cuerpo, pero `Request::json()` parsea **JSON y nada más**: un `application/x-www-form-urlencoded` es ilegible de punta a punta. La rama de formularios era código muerto que parecía vivo | Declarado, no maquillado: el guard **no** es lo que reporta un cuerpo que no puede parsear, porque un body ilegible no es un token inválido y responder 403 culparía al cliente de una limitación del framework. Atender un form post de verdad necesita un lector de cuerpo de formulario, que no existe |
| §12 `csrf` (alcance) | — | El guard cubre las rutas `#[Action]` — a las que un form puede llegar — y **no** el CRUD derivado, y la razón está probada en vez de afirmada: un form HTML cross-site no puede enviar `Content-Type: application/json`, así que no puede producir un cuerpo que este endpoint lea. Un cliente sin cookie tampoco se guarda: no tiene credencial ambiental que falsificar, y rechazarlo rompería a cada cliente API |
| Tabla derivada del nombre corto | `DomainScanner::deriveTableName()` toma **el basename y nada más**. Dos entidades `Pedido` en dos namespaces son dos clases distintas sobre **la misma tabla**, y el segundo suite en correr encuentra columnas ajenas. No lo detecté por diseño: lo detectó la suite completa, cuando 12 pruebas de `ManyToManyRelationTest` cayeron con un 500 al añadir un fixture | El fixture de CSRF se llama `Ticket` y el docblock explica por qué. **No** se cambió la derivación: alterar el nombre de tabla rompe el DDL ya publicado, y la limitación queda registrada en vez de escondida detrás de un test que pasa por casualidad |
| §14 idempotencia: **no funcionaba** | Los dos caminos leían `$pdo = $this->ensurePersistence()`, y ese método devuelve `void`: `$pdo` era **siempre null**. Cada lectura y cada escritura lanzaban `Call to a member function prepare() on null`, y el `catch (\Throwable)` de cada uno — comentado como *"idempotency is best-effort"* — convertía eso en "seguí adelante". El feature estaba **inerte de punta a punta**: nunca hubo replay ni nunca se escribió un registro, y el catch mudo hacía que se leyera como un *best-effort* que funcionaba en vez de uno muerto | `ensurePersistence()` devuelve la conexión que acaba de asegurar. No se resolvió haciendo que `pdo()` la llamara: `createQuerySource()` resuelve la conexión por `pdo()`, así que eso re-entra con `$this->querySource` todavía en null y recursiona hasta que el proceso se queda sin memoria. Los dos `catch` **mudan** ahora loguean: *best-effort* es una política, el silencio no |
| §14 idempotencia: key en otra ruta | La búsqueda filtraba por `(key, route)`, así que una key reusada en **otra ruta** no matcheaba nada: sin replay, sin 422, y — como el insert choca sólo por la key — tampoco quedaba nada guardado. §14 dice que ese caso es 422. El cliente que reusaba una key recibía la doble ejecución que el header existe para evitar, y ningún error para notarlo | La ruta se compara en PHP, no en el `WHERE`. El filtro en SQL hacía que una key reusada pareciera una key que nadie había usado |
| §14 idempotencia: el replay no era un replay | El replay retornaba en el medio del pipeline, **antes** de CORS y de cache-control. Una respuesta reintentada quedaba sin headers que la original tenía, y un navegador no puede leer un retry al que le falta `Access-Control-Allow-Origin`: exactamente el caso para el que existe el replay. Además el cuerpo guardado pasaba por `json_decode`/`json_encode` sin motivo, y una action que responde 204-sin-cuerpo volvía con el cuerpo literal `null` | `applyResponsePolicy()` — una sola puerta para la cola de CORS + cache-control — y las dos rutas pasan por ahí. El cuerpo se devuelve **verbatim**: el valor guardado ya está serializado, y el round trip sólo podía perder información. Los headers de CORS se recalculan con la petición que llega **ahora**, no con la primera: guardar los headers de la primera dejaría que un retry de otro origin se respondiera con la allow-list del origin original |
| §14 GC de vencidas | El barrido **no existía**. §14 lo pide — *"en cada insert se purga un lote acotado de `expires_at < now`"* — y sin él la tabla es el único artefacto del sistema que nadie lee y nada acota. Además el insert usaba `ON CONFLICT DO NOTHING`: una fila simplemente vencida dejaba **muerta** esa key para siempre (sin replay, y sin guardar nada nuevo) | Barrido acotado en el insert (`http.idempotency_gc_batch`, default 100) y `ON CONFLICT (key) DO UPDATE ... WHERE expires_at < NOW()`, que reemplaza exactamente las filas vencidas y jamás pisa una viva. Un test comprueba que el barrido tiene tope: sin `LIMIT` un solo POST borraba el historial de la tabla |
| §14 hash del payload | `md5($body)` | `sha256`. No es una primitiva de seguridad, es una huella — pero las colisiones de md5 son baratas de construir, y una colisión acá significa responderle a un cliente la respuesta de otro |
| §13 CORS: el preflight no se contestaba | `cors.allowed_methods` trae `OPTIONS` de fábrica y **nada en el código atendía una petición `OPTIONS`**: el router matchea por método, no había ruta `OPTIONS`, y todo preflight volvía 404. La forma documentada de prender CORS (listar un origin en `allowed_origins`) es exactamente la que hace que el navegador mande un preflight, así que el feature no se podía encender. Y no podía funcionar para ninguno de los dos headers que el framework exige: `Authorization` e `Idempotency-Key` fuerzan preflight | `Router::matchesAnyMethod()` — la pregunta del preflight es *«¿algún método llega a este path?»*, no *«¿este método llega?»*, y eso es una pregunta distinta, no un flag sobre `match()`. Se contesta **antes** del autorizador: un preflight lleva `Origin` y el método que pregunta y, por construcción, ninguna credencial; contestarlo después devolvería 401 a la única petición que no está tratando de actuar como nadie, y el navegador reportaría un error de CORS en vez del 401. Y **sólo** para paths reales: un 204 a todo convierte la API en un agujero negro — una URL mal escrita volvería 204 en el preflight y 404 en la llamada real |
| §13 CORS: sin `Vary: Origin` | `Access-Control-Allow-Origin` refleja el origin de quien pregunta, así que la respuesta es **por origin**: sin `Vary: Origin` una caché compartida guardaba la respuesta de un origin y se la servía al siguiente. Es una fuga cross-origin que ningún test del framework ve, porque el framework no es quien la sufre | `Vary: Origin` se emite **mezclado** con el `Vary` que la respuesta ya trajera, nunca reemplazado: un middleware de caché es la fuente ordinaria de un `Vary` propio, y pisarlo tira el contrato de encoding por la ventana. La búsqueda es case-insensitive porque `Response::$headers` es verbatim — si el existente se escribió `vary:` y se busca `'Vary'`, se crea un **segundo** header, y en el cable gana el último: `Accept-Encoding` desaparece y todo test que sólo mire `Origin` sigue pasando |
| §14 `http.limits` body: medía la mentira | El límite leía `Content-Length`, que es **un número que escribe el cliente**: 100 MB de cuerpo real con `Content-Length: 10` — o enviado *chunked*, que es lo que pasa cuando no mandás largo — pasaba el chequeo y después lo parseaba, en memoria, un decoder de JSON. Un límite que mide el **declarado** en vez de **lo que hay** no es un límite: es una sugerencia que el cliente puede ignorar | Se mide `strlen($request->body)` y además se respeta la declaración, pero **sólo para subir** la respuesta: un claim más grande que el límite se rechaza, un claim más chico no compra un pase. La asimetría es deliberada — un cliente que anuncia más de lo que va a mandar tiene un bug, y rechazarlo le cuesta cero mientras le ahorra al servidor la lectura |
| §14 `http.limits` timeout: declarado y leído por nadie | `request_timeout` estaba en la config que se shippea y en el scaffold, y no lo leía nadie. Peor: las otras dos entradas de la misma tabla (`raw_body_limit`, `upload_max`) tampoco | `request_timeout` → **408 `http.request_timeout`**, chequeado **antes** del dispatch para que una petición que ya gastó su presupuesto nunca toque el dominio. El reloj es un **seam inyectable** (`Kernel::__construct`), no un `hrtime()` directo: la otra forma de testear un timeout es dormir, y un test que duerme es lento o inestable, nunca las dos. La otra mitad que pide §14 — rechazar **y rollback** después de que el dominio ya corrió — **no** está implementada, y el motivo está en el código y en `RuntimeCapabilities`: hacer rollback acá sería revertir una transacción que el kernel no abrió |
| §14 `upload_max`: por archivo, no por petición | La comparación era contra **la petición entera**, y `upload_max` es el tope de **un archivo individual**. No podía estar bien en ninguna configuración alcanzable: con los defaults que se shippean nunca dispara (los dos límites son iguales y el body se chequea primero), y con `body_limit` subido dispara contra el total — que §14 le asigna explícitamente a `body_limit` (*"una request con varios archivos suma contra `body_limit`"*) | Un límite por archivo necesita un lector multipart, y este framework lee JSON (`Request::json()`, `JSON_THROW_ON_ERROR`). El chequeo que estaba **se fue** en vez de quedar pareciendo vivo: sólo podía dar una respuesta equivocada. Y `http.upload_too_large` queda **inalcanzable con los defaults**, lo cual ahora está **pineado** por un test en vez de ser un accidente — es la razón por la que el test del multipart sube `body_limit` |
| §14 `raw_body_limit` | Declarado en la config y en el scaffold, leído por nada. Es el tope del **buffer de una respuesta en streaming** | **Declarado, no implementado**: no hay respuesta streaming. Un límite en la config que nadie lee es peor que no tenerlo, porque se lee como protección |
| El mini-DSL no tiene campo texto | Un `string` deriva **siempre** a `VARCHAR(255)` (`DiffEngine::sqlType()`), y `#[Field]` no tiene forma de pedir `TEXT`. No hay ningún campo `array` tampoco — `sqlType()` lanza `InvalidArgumentException` ante `array` | No se cambió: tocar la derivación de tipos es otro capítulo (§5, no §14) y merece su propio trabajo con su propio test. Se deja **documentado** en el fixture de T26 porque tiene una consecuencia visible: ningún cuerpo de 8 MB puede ser a la vez válido para una entidad de este framework, así que el control del límite shippeado afirma *"el límite no se metió en el medio"* en vez de un 201 |
| §10 esperar una fila ocupada | Nada. Este test no existía, y lo que faltaba no era el camino feliz: una **espera** no se puede demostrar en un harness de un solo hilo — la transacción que toma el lock no se puede cerrar desde el hilo que está bloqueado esperándolo, y el test se cuelga. | `TransactionRunnerTest` (17 tests) con una contención **real** de Postgres: dos conexiones, `SERIALIZABLE` a nivel de sesión, un `40001` vero que el runner reintenta y aplica **encima** del valor ganador. Más lo que sí es demostrable: la espera está acotada por `lock_timeout` y reportada como lo que es. El DDL de la tabla lo pide `DiffEngine`, no el test. |

### Cerrado — 2026-09-26 (tercera ronda)

| Casa | Qué estaba mal | Qué resolvió |
|------|-----------------|----------------|
| §5 `middleware` | El atributo se escaneaba, se cacheaba y se serializaba, y `Route::fromMetadata()` lo **descartaba**. Peor: `Router::match()` re-construía la ruta a mano, campo por campo, dos veces (exacto y patrón), y ninguna de las dos copias incluía `middleware` — tres listas manuales del mismo conjunto de campos, donde olvidar un campo nuevo no da error sino una pérdida silenciosa. | `Route::withAttributes()` deja una sola derivación. `MiddlewareRegistry` resuelve **nombres** contra el registro de la app; orden de declaración, el primero es el más externo; envuelve sólo el dispatch, después de la autorización, así que una petición denegada nunca llega. Un nombre no registrado es **500**, nunca skip: un nombre saltado podría ser el único guard de la ruta. `MiddlewareChainTest` (15 tests) y `CheckMiddlewareTest` (6 tests). |
| §5 `middleware` en `check` | `CapabilityValidator` no miraba los nombres, sólo si la capability estaba implementada. Un nombre no resoluble sólo se descubría en runtime, con un 500. | `check` reporta los nombres que faltan y si no hay `MiddlewareRegistry` enlazada. Usa `has()`, no `resolve()` en try/catch: `resolve()` auto-construye una clase concreta sin constructor y habría devuelto un registro vacío, reportando cinco nombres faltantes en vez del único hecho que importa. |
| §14 resultado de `#[Action]` | `Kernel::dispatchAction()` llamaba a `Serializer::serialize()`, cuyo primer parámetro está tipado como entidad. **Toda** action que devolviera algo que no fuese una entidad — un `string`, un `int`, un `bool`, una lista, un enum, un `UuidV7`, `null` — era un `TypeError` y terminaba en 500. El camino de `#[Query]` ya usaba `serializeResult()`; el de action simplemente nunca se cambió. | `dispatchAction()` usa `serializeResult()`. `ActionResultTest` (12 tests) que lee el **cuerpo** de la respuesta, no el status, con el caso entidad como control. |
| Logs de frontera falsos | El Kernel logueaba `middleware`, `indexes` y `softDelete` como "declarado pero NO ejecutado", y `validate` igual — mientras `RuntimeCapabilities` decía `VALIDATE_DSL => true` y `CrudController::validatePayload()` lo ejecutaba de verdad. Dos capas del framework discrepando sobre la misma feature, que es exactamente el modo de fallo que dejó a `deleted_at` existir en el DDL y faltar en la metadata. | Los logs falsos fuera, con el motivo escrito en el código. `RuntimeCapabilities` ahora nombra, para cada `true`, el test que lo certifica, y separa lo que tiene test dedicado de lo que sólo se cubre de rebote. `VALIDATE_DSL` estaba duplicado en el array. |

### Cerrado — 2026-09-26 (segunda ronda)

| Casa | Qué estaba mal | Qué resolvió |
|------|-----------------|----------------|
| §5 `indexes` | El DDL sí emitía `CREATE INDEX`, pero `loadConstraintBackedIndexes()` unía `pg_index` por tabla + `indisunique` en vez de por `conindid`. Eso marcaba **todo** índice UNIQUE como propiedad de una constraint, así que un `unique: true` declarado desaparecía del schema cargado y el diff re-emitía su `CREATE` en cada corrida: una migración que no se puede aplicar dos veces. | El join es por `conindid`. Tests que verifican el índice en `pg_indexes` después de aplicar, y que un segundo diff no emite nada. Un test anterior pasaba con el bug presente porque solo declaraba un índice simple. |
| §5 pivots no derivables | `DiffEngine` abortaba el diff completo por una relación incompleta. | Deriva todo lo derivable y devuelve los motivos en `warnings`; `migrate:status` y `migrate:create` los imprimen. |
| §5 worker de cola | `WorkerLoop` usaba `QueueJob` sin import, así que `instanceof` era `false` en silencio: el worker descartaba **todos** los jobs, reportaba `0 job(s) processed` y salía 0. También era el "hang de 24 minutos". | Import agregado + `WorkerLoopTest` (8 tests) que pinea que un job del source llega al handler. |
| §5 `QueuePort` | `SyncQueue::push()` hacía `$handler::class` sobre un parámetro `object|string`; un class-string lanzaba TypeError, contra su propio docblock. | Un class-string se toma tal cual. |

### Cerrado — 2026-09-26

Nueve huecos cerrados, cada uno con tests que leen el estado real y no solo el
status HTTP. Cinco de ellos eran **código muerto**: la ruta existía, el test
pasaba y el runtime nunca hacía nada.

| Casa | Qué quedó en el runtime |
|------|------------------------|
| §8 `#[ManyToMany]` | `RelationMetadata::$pivotTable` + `DomainScanner::derivePivotTableName()` (par ordenado, así el lado inverso resuelve la misma tabla) + DDL de la pivot con ambas FKs |
| §5 `softDelete` | `deleted_at` derivado como campo real (`DomainScanner::SOFT_DELETE_FIELD`), filtro en `get` **y** en `list`, y `PATCH /{id}/restore` idempotente |
| §14 `http.limits` | `body_limit`, `uri_max` y `request_timeout` aplicados en `Kernel` |
| §14 `Idempotency-Key` | Replay por `(key, route, hash)` con almacén en `idempotency_keys` |
| §13 `csrf` | Verificación de token en mutaciones |
| §13 `cors` | `Access-Control-*` en la respuesta, con allow-list configurable |
| §15.3 `Cache-Control` | `max-age={cache}` para `#[Query(cache: N)]`, default configurado en el resto |
| §15.1 OpenAPI | `OpenApiGenerator` — esquemas por FQCN, relaciones fuera de `properties`, `openapi` real |
| §5 `#[Queued]` | `QueuePort` + driver `sync`, dispatch en `Kernel` con **202** sin ejecutar el cuerpo |

Bugs reales que los tests de estos huecos revelaron:

- `DomainScanner` nunca leía `#[Queued]`, así que `MethodMetadata::$queue` era
  siempre `null` y el dispatch encolado era inalcanzable.
- `Response` no tenía `withHeader()`: las cinco llamadas de CORS y
  Cache-Control eran errores fatales tragados por `catch (\Throwable)`.
- `Kernel::idempotencyStore()` leía `$response->status` (la propiedad es
  `statusCode`), así que nunca almacenaba nada.
- No existía el port `queue`; cualquier `#[Queued]` moría en `resolve('queue')`.
- `DiffEngine` no era idempotente: la segunda pasada emitía
  `DROP INDEX ..._pkey` —destruyendo las claves primarias— porque buscaba el
  literal `PRIMARY KEY` en `pg_indexes.indexdef`, donde nunca aparece.
- `deleted_at` existía en el DDL pero no en la metadata, así que **todo** read
  de una raíz soft-delete daba 500 y `restore` no podía restaurar nunca.
- `PdoQuerySource` traducía un filtro `null` a `col = NULL`, que nunca es
  verdadero; ahora es `IS NULL`.
- `Hydrator::build()` coercía campos que el constructor no acepta y luego los
  descartaba, así que un `TIMESTAMPTZ` que el propio framework escribía
  reventaba la hidratación.
- `list()` no aplicaba el filtro de soft delete: una fila borrada daba 404 por id
  y aun así aparecía en la colección.
- `ClassMetadata::versionPrefix()` era `private` y `OpenApiGenerator` la
  llamaba: error fatal.


### Deuda conocida que no es de producto

- **Artefactos SDD desalineados**: los bloques de auth, concurrencia y validación se implementaron fuera del ciclo SDD, así que `openspec/changes/` no los conoce. Un `sdd-verify` contra las specs fallaría hasta que se registren.
- **Cache de metadata envenenado**: una corrida de test escribió metadata de fixtures en el cache de producción. Se detectó y se corrigió la detección, pero **no se identificó qué test lo causó**.
- **Sin análisis estático**: no hay PHPStan; el chequeo de tipos que §11 describe no existe como verificación.
