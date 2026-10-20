# Session Work Journal (Boilerfree — whole conversation)

> Exportado manualmente por el asistente desde la memoria activa de la conversación, sin leer otros archivos.  
> Repositorio: `feat/framework-runtime-gaps` → merged a `main`. Remoto: `origin/main`.  
> Fecha de referencia de esta síntesis: sesión activa (seguir en el repo para corroborar hashes).

## 1. Cronología por wave

### Wave 1 (cerrada previamente)
- S2, S3, S3b, S1. Suite base alrededor de 745/2945.

### Wave 2 — puertos §7 y salida HTTP (commits digest)
- S4 (11 puertos: Logger, ErrorReporter, Tracer, Clock, Hasher, Encrypter, EventDispatcher, Mailer, Schedule, Storage, Http) con locators container-first y adapters por defecto (mismo patrón `CacheLocator`/`RendererLocator`).  
  Commits clave: `f94a924`, `9772199`, `0573c3f`, `1752713`, `db4f093`, `374cfa0`, `b308dfe`, `9366fce`, `42694d0`, `d071848`.
- suite base 785/3100.
- S9 operabilidad: request id, log estructurado `http_request`, metrics port, PrometheusExposition, `/metrics` gated por `ops.metrics`, `/healthz` y `/readyz` gated por `ops.enabled`, readyz pingea `query_source`. Commits `e1a9e5c`, `a12ada0`.
- S8 PSR-7 hand-rolled + PSR-15 hand-rolled sin dependencia externa: `Uri`, `Stream`, `UploadedFile`, Request, response, factories, `HandlerInterface`, `Psr15Middleware`, `Pipe`. Commits `e579a93`, `1701958`. Baseline 800/3196.
- Roadmap S9/S8 movidos a `R-W2` con recepción de evidencia.
- `.obsidian/` y `src/Domain/route_creation_check.php` quedaron sin tocar (invariant del user).

### Wave 3 — S5 / S6 / S7
- S5 upload boundary:
  - `StoragePort` + `LocalStorage` + `StorageManager`.
  - `StorageFile` (disk/path/size/mimeType/name).
  - `Request::fromGlobals()` ahora llena `uploadedFiles` con `$_FILES`.
  - `Validator` aprendió `mimes`/`dimensions` sobre `UploadedFile`.
  - `Response::download(...)`.
  - Test: `UploadStorageContractTest.php` (6 tests, 19 assertions).
  - Commit `d2e4ee7`.
- S6 streaming/SSE:
  - Response::stream(Traversable), `isStreaming()`, send chunked.
  - Kernel::runAction detecta `\Generator` retornado por `#[Action]` y devuelve stream.
  - Test: `StreamingContractTest.php`.
  - Commits `3c31156`, `a057a57` (fix `\Generator` parse).
- S7 trusted proxies:
  - `Request::getClientIp(array $trustedProxies)`, `isSecure(...)`, `isTrustedProxy(...)`.
  - Test `TrustedProxyContractTest.php`.
  - Commit `0942f90`.
- Post-wave3 suite: 810 tests / 3227 assertions, verde.
- Roadmap S5/S6/S7 movidos a `R-W3`.
- Commit docs: `eead931`.

### Ola posterior — backlog (A/B/C/D)
- S10:
  - `OutboxPersister::class` bindDefault en Kernel (PDO lazy).
  - commit `e4393f0`.
- S11:
  - `SessionStore::regenerate()` (signed session rotation, fail-closed).
  - `DatabaseSessionStore::regenerate()` con transaction.
  - CSRF tests adaptados.
  - commit `577d175`.
- S12 (parcial):
  - `outbox:dispatch` alias → `outbox:process` (`DispatchCommand`).
  - `cache:clear` alias → `optimize:clear` (`CacheClearCommand`).
  - `make:vo` command (`ValueObjectCommand`).
  - Commits `306984b`, `df1e45b`, `13d539c` + `c8e4a5b` fix visibility.
- D2:
  - adapter de security headers en `handle()` (todas las respuestas incl. early failures).
  - commit `12191df`.
- Tracker vivo en `odd/tasks/backlog-closure.md`.
- suite verde (810/3227).
- Merge y push a `main`:
  - ask permission -> user chose branch → later user asked “todo en main”; se hizo fast-forward y push.
  - push 1: `origin/main 6cef070..e4393f0`.
  - push docs: `49dc9cb`.

## 2. Decisiones técnicas relevantes (why)

- No reinventar lenguaje/framework: Boilerfree es PHP 8.3 real.
- Metadata-first: DomainScanner → DomainScanner scan (transitive references), ClassMetadata serializable.
- Fail-closed: RouteAuthorizer/CSRF/session store; security headers always.
- ports container-first: bindDefault, app override gana.
- Immutable HTTP: PSR-lite immutable (Response/Request).
- Trusted proxies solo si REMOTE_ADDR listado.
- Streaming: Response::isStreaming + chunking sin header Content-Length.
- S5: UploadedFile + StorageFile + Validator entienden frontera.
- D2 security headers en `handle()` (no sólo applyResponsePolicy).
- S10 seam: persister disponible para las transacciones (convención releaseEvents es de app).
- S11 session regeneration: issue rotation sin re-mint cookie, eliminar old.
- Comandos de consola(auto-descubrimiento por namespace).
- Deuda honesta en backlog (sin sobre-afirmar).
- Documentación source-derived (`docs/boilerfree-technical-deep-dive.md`).

## 3. Backlog pendiente (ids)

- S10 convención complete (persister), restan wrappers.
- S12 remaining make commands (view, job, event, listener, seed; migration derivada).
- D1 rate_limit adapter / 429 / retry-after.
- D3 `upload_max` granular + `raw_body_limit`.
- D4 OpenApi serve endpoint (intentional).
- D5 queued 202 e2e.
- O1 auth throttling.
- O2 PHPStan/Pint CI.
- O3 job timeout + tries/backoff verified.
- O4 unique/overlap locks + DLQ/GC.
- O5 SIGTERM/SIGINT schedule/run y serve.
- O6 retention purge.
- O7 boilerfree new completo.
- O8 metadata cache hash fallback (Docker volumes).
- O9 end-to-end spike.
- O10 experiment.
- O11 docs tesis.
- O12 mini DSL text/array.
- E1 SDD alignment.
- E2 cache poisoned test identification.
- E3 static analysis tooling.
- E4 check §7 y §15 capability rows.
- Tracker: `odd/tasks/backlog-closure.md`.

## 4. Documentación generada

- `docs/cap4-objetivos-1-2.md` restored separately (ver fichero).
- `docs/boilerfree-technical-deep-dive.md` (arquitectura + secuencia + infra + deuda).
- `odd/tasks/backlog-closure.md`.

## 5. Vault / tesis

- `/run/media/ernesto/D/Tesis boilerplate/boilerfree vault`: autorizada read/edit, sin tocarla hasta solicitud.

## 6. Pushes y estado

- commit docs: `49dc9cb docs: technical deep-dive...`.
- commit S10: `e4393f0`.
- suite al cierre: 810 tests / 3227 assertions, verde .
- Branch final quedó Main (merge ffi).
- remote origin main actualizado.

## 7. Recomendaciones para nueva sesión

- Aprovechar `mem_search/mem_context` con términos `sdd-...` si Use SDD, pero ODD sigue default.
- Revisar git status for only .obsidian and route_creation_check.php untracked.
- No alterar leftovers no-project.
- Run new slices as RED→GREEN→commit.
MD
echo journal_done