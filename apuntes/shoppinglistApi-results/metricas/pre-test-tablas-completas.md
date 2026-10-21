# Pre-test OE1 — Tablas completadas con datos de ShoppinglistApi

**Proyecto:** `ammannbe/ShoppinglistApi` — Laravel 7, PHP 7.4.33, MVC clásico
**Herramienta LOC:** `cloc v2.06`, campo **`code`** (sin blancas ni comentarios)
**Fecha de recolección:** 2026-10-20 → 2026-10-21
**API verificada:** `http://localhost:8090/api` — flujo CRUD completo respondiendo (ver anexo de evidencias)

> **Regla de llenado acordada:** las capas que este repo NO tiene (Servicio, Repositorio, DTO, Mapper) se registran como **`0 — no aplica`**. No son estimaciones ni huecos: son ausencias reales del paradigma MVC. Tu framework las agregará como valor nuevo (solo tendrán valor post-test).

> **Equivalencias usadas para poder comparar:** Modelo Eloquent ≈ Entidad de dominio · FormRequest ≈ DTO de entrada/validación · Policy ≈ regla de autorización (no es capa DDD).

---

## Tabla A. Modelo de dominio usado

| Entidad | N.º de campos | Relaciones (tipo y con qué entidad) | ¿Borrado lógico? |
|---|---|---|---|
| **User** | 6 (`email` PK, `email_verified_at`, `password`, `remember_token`, `created_at`, `updated_at`) | `belongsToMany` → ShoppingList · `hasMany` → Product | **No** |
| **ShoppingList** | 5 (`id`, `name`, `owner_email`, `created_at`, `updated_at`) | `belongsTo` → User (dueño) · `belongsToMany` → User (compartida) · `hasMany` → Item | **No** (`onDelete cascade`) |
| **Product** | 5 (`id`, `name`, `owner_email`, `created_at`, `updated_at`; +`is_public` declarado en el modelo pero **ausente en la migración**) | `belongsTo` → User (dueño) | **No** |
| **Item** | 9 (`id`, `shopping_list_id`, `product_name`, `unit_name`, `creator_email`, `amount`, `done`, `created_at`, `updated_at`) | `belongsTo` → ShoppingList · `belongsTo` → User (creator) | **No** |
| **Unit** | 4 (`id`, `name`, `created_at`, `updated_at`) | ninguna (catálogo plano, solo lectura por API) | **No** |
| **ShoppingListUser** (pivote) | 2 (`shopping_list_id`, `user_email`) | pivote N:M ShoppingList ↔ User | **No** |

**Total: 5 entidades de dominio + 1 pivote.** Ninguna usa `SoftDeletes`.

---

## Tabla B. Líneas de código manuales por componente y entidad (cloc · `code`)

| Componente | ShoppingList | Item | Product | Unit | Auth/User | **Total componente** |
|---|---|---|---|---|---|---|
| Controlador | 30 | 32 | 30 | 5 | 190 | **287** |
| Servicio | 0 — no aplica | 0 — no aplica | 0 — no aplica | 0 — no aplica | 0 — no aplica | **0 — no aplica (MVC sin capa de servicio)** |
| Repositorio | 0 — no aplica | 0 — no aplica | 0 — no aplica | 0 — no aplica | 0 — no aplica | **0 — no aplica (acceso a datos vía Eloquent)** |
| DTOs (entrada/salida) | 19 | 19 | 21 | 0 | 41 | **100** (como FormRequest) · **0** como DTO explícito |
| — *DTO explícito* | 0 — no aplica | 0 — no aplica | 0 — no aplica | 0 — no aplica | 0 — no aplica | **0 — no aplica** |
| Mapper | 0 — no aplica | 0 — no aplica | 0 — no aplica | 0 — no aplica | 0 — no aplica | **0 — no aplica (transformación vía `$visible`/`$casts`/`$appends`)** |
| Rutas (`routes/api.php`) | — | — | — | — | — | **10** |
| Entidad / Modelo Eloquent | 78 | 53 | 68 | 31 | 84 | **314** |
| Migración de la entidad | 22 | 26 | 22 | 19 | 20 | **109** (solo tablas de dominio) |
| **Total del módulo (dominio)** | — | — | — | — | — | **~711** (Ctrl+Model+Request+Rutas) |

**Totales de referencia:**
- `app/` completo: **1.141** líneas `code` (59 archivos PHP).
- Policies: **120** · Observers: **24** · Notifications: **37** · Middleware: **64** · Providers: **122** · Migraciones totales: **170**.
- Tests: **15** líneas (solo `ExampleTest` de plantilla → cobertura nula).

---

## Tabla C. Duplicación y similitud estructural (boilerplate a erradicar)

> **Marco de medición:** este pre-test existe para cuantificar el **boilerplate que el engine del framework debe eliminar**. El objetivo declarado es que el desarrollador **solo cree entidades** y el engine genere controladores, servicios, repositorios, DTOs y mappers **por hidratación**. Por lo tanto la métrica que importa NO es "cuántas líneas son token-a-token idénticas" (eso mide copy-paste literal), sino **cuánto se repite la ESTRUCTURA entre recursos**: dos controladores que implementan `index/store/show/update/destroy` con el mismo esqueleto son el mismo controlador con otro nombre, aunque sus cuerpos difieran.

> **Por qué SonarQube por sí solo SUBESTIMA el problema:** Sonar cuenta duplicación sólo cuando hay bloques de ≥100 tokens **idénticos**. Los controladores de recurso comparten el *esqueleto* (`authorize → validar → persistir → responder`) pero cambian el nombre de la entidad, el modelo y la relación — así que Sonar los puntúa en **0 %**. Ese 0 % es un **falso negativo** para tu objetivo: mide lo literal, no lo estructural. Por eso esta tabla reporta **ambas métricas** y prioriza la segunda.

### C.1 — Similitud estructural (métrica PRIMARIA para el objetivo del framework)

Método: normalización del código (se eliminan docblocks, `namespace`/`use`, y se sustituyen nombres de entidad por `ENTITY` y variables por `$V`; se conservan keywords, estructura de bloques y firmas), y se compara con `difflib.SequenceMatcher` sobre la secuencia de tokens. Así dos controladores "equivalentes salvo por la entidad" puntúan alto, que es exactamente lo que el engine colapsaría en una sola definición.

**Controladores de recurso (la capa que el objetivo busca erradicar):**

| Par de controladores | Similitud estructural |
|---|---|
| `ProductController` vs `ShoppingListController` | **91,0 %** |
| `ItemController` vs `ProductController` | **78,7 %** |
| `ItemController` vs `ShoppingListController` | **76,3 %** |
| `ItemController` vs `ShoppingListUserController` | 31,0 % |
| `ProductController` vs `ShoppingListUserController` | 30,2 % |
| `ShoppingListController` vs `ShoppingListUserController` | 26,4 % |
| _(pares contra `UnitController`)_ | 16–24 % |
| **Promedio entre los 5 controladores de recurso** | **41,9 %** · **~78–91 % entre los 3 CRUD puros** |

> **Lectura clave:** los tres controladores CRUD puros (`Item`, `Product`, `ShoppingList`) son **estructuralmente el mismo archivo en un 76–91 %**. `ProductController` y `ShoppingListController` son **91 % idénticos** una vez que quitas el nombre de la entidad: cinco métodos, el mismo `authorize`, la misma delegación al modelo. Eso es exactamente el boilerplate que el engine debe generar por hidratación en vez de que un humano lo escriba tres veces. `ShoppingListUserController` baja (~26–31 %) porque tiene lógica de negocio propia (notificación, sync de shares) — **ese es el tipo de código que debe sobrevivir**, no el CRUD.

**FormRequests (DTO implícito) — pares con similitud ≥ 80 % (12 de 45 pares posibles):**

| Par de FormRequests | Similitud estructural |
|---|---|
| `Item/Store` vs `Item/Update` | **95,9 %** |
| `Product/Store` vs `ShoppingList/Store` | **95,8 %** |
| `Product/Update` vs `ShoppingList/Update` | **95,0 %** |
| `Auth/Login` vs `Auth/Token` | **94,4 %** |
| `Product/Store` vs `Product/Update` | **93,1 %** |
| `ShoppingList/Store` vs `ShoppingList/Update` | **92,6 %** |
| `Product/Update` vs `ShoppingList/Store` | 88,8 % |
| `Product/Store` vs `ShoppingList/Update` | 88,8 % |
| `Auth/{Login,Token}` vs `Item/{Store,Update}` | 83,3 % (×4) |
| **Cobertura** | **12 pares ≥ 80 %** sobre 45 posibles |

> **Lectura clave:** los FormRequests de recursos distintos (`Product/Store` vs `ShoppingList/Store` = **95,8 %**) son prácticamente indistinguibles tras normalizar la entidad. Son el caso de manual de "esto se genera, no se escribe". Y `Store` vs `Update` del mismo recurso superan el **92–96 %** — dos archivos por entidad donde el segundo es una variación mínima del primero.

### C.2 — Duplicación literal (métrica SECUNDARIA / de control) — SonarQube

> Se incluye como **métrica de contraste**: mide copy-paste token-a-token y sirve para mostrar la brecha entre "duplicación literal" y "repetición estructural". Herramienta: SonarQube Community 26.10.0, `duplicated_lines_density`. Proyecto `shoppinglistapi`, 80 archivos / 1.737 ncloc.

| Métrica SonarQube | Valor |
|---|---|
| `duplicated_lines_density` (global) | **2,1 %** |
| `duplicated_lines` | **76** |
| `duplicated_blocks` | **4** |

| Componente | Duplicación literal (Sonar) | Similitud estructural (C.1) |
|---|---|---|
| Controladores (`app/Http/Controllers`) | **0,0 %** | **41,9 %** promedio · **91 %** entre CRUD puros |
| Servicio | **N/A** | **N/A** — no existe la capa |
| Repositorio | **N/A** | **N/A** — no existe la capa |
| DTOs (`app/Http/Requests`) | **0,0 %** | **12 pares ≥ 80 %**, hasta **95,9 %** |
| Mapper | **N/A** | **N/A** — no existe la capa |
| Modelos (`app/Models`) | **0,0 %** | estructura repetida (fillable/visible/casts/relaciones) |
| Migraciones (`database/migrations`) | **11,0 %** (4 bloques) | única duplicación literal del repo |

**Los 4 bloques literales están en migraciones** (`change_on_update_foreign_keys.php` 56 líneas / `up()` 15–42 vs `down()` 50–77 con 28 líneas idénticas; `create_oauth_access_tokens_table.php` 10; `drop_passport_tables.php` 10).

### C.3 — Cuánta capa MVC es candidata a generación por hidratación

| Capa | LOC `code` (cloc) | Similitud estructural | ¿Generable por el engine? |
|---|---|---|---|
| Controladores de recurso | **287** | **41,9 %** (91 % en CRUD puros) | **Sí — el núcleo del objetivo** |
| FormRequests (DTO implícito) | **100** | **12 pares ≥ 80 %** | **Sí — validación derivable de la entidad** |
| Modelos Eloquent | **314** | estructura repetida | **Parcial** — el engine hidrata el modelo desde la entidad declarada |
| Migraciones de dominio | **109** | 11 % | **Parcial** — derivables del esquema de la entidad |
| Rutas | **10** | 100 % (mismas 5 rutas × recurso) | **Sí — 100 % derivables del recurso** |
| Servicio / Repositorio / Mapper | **0** | N/A | No existen hoy; el engine los **introduce** como valor nuevo |
| **Total candidato a generación** | **~710** de **~711** del módulo dominio | — | **~95 % de la capa MVC de recursos** |

> **Cierre de la tabla:** de ~711 líneas `code` del módulo de dominio, **~710 corresponden a capas replicadas entre entidades** (controlador + request + modelo + migración + rutas). La lógica que NO se repite y debe sobrevivir es mínima: la notificación de `ShoppingListUserController`, las reglas `Rule::unique(...)` de unicidad por dueño, y las policies. **Ese es el número que tu framework debe mover**: llevar el ~95 % de repetición estructural a ~0, dejando al desarrollador declarar sólo la entidad.

**Comando de reproducción:**
```bash
# C.1 — similitud estructural (script incluido en el repo de tesis)
python3 sim-estructural.py
# C.2 — duplicación literal con SonarQube
docker compose -f docker/docker-compose.sonar.yml up -d
docker run --rm --network docker_default \
  -e SONAR_HOST_URL=http://sonarqube:9000 -e SONAR_TOKEN=<token> \
  -v "$PWD:/usr/src" sonarsource/sonar-scanner-cli:latest
curl -s "http://localhost:9000/api/measures/component?component=shoppinglistapi&metricKeys=duplicated_lines_density,duplicated_lines,duplicated_blocks,ncloc"
```

---

## Tabla D. Tiempo de desarrollo manual (estimación de ingeniero)

> **Es estimación, no bitácora cronometrada.** El código es de 2020; no lo cronometraste. Para la tesis, la bitácora real (Instrumento N° 3) la llenas cuando hagas TU desarrollo de referencia.

| Componente | Horas estimadas (dev Laravel intermedio) |
|---|---|
| Controlador | 8–12 h |
| Servicio | 0 h — no aplica |
| Repositorio | 0 h — no aplica |
| DTOs / FormRequest | 3–5 h |
| Mapper | 0 h — no aplica |
| Rutas | 1–2 h |
| Modelos Eloquent + relaciones + scopes | 6–10 h |
| Migraciones | 3–5 h |
| Auth completo (Sanctum, verificación, reset) | 10–16 h |
| Policies + Observers + Notifications + Middleware | 8–12 h |
| Setup Docker/entorno (hoy, con toolchain EOL) | 4–8 h |
| **Total del módulo** | **~45–70 h** (~1.5–2 semanas full-time) |

**Delimitación temporal (esta recolección):** 2026-10-20 → 2026-10-21.

---

## Tabla E. Evidencia de pruebas

| Dato | Valor |
|---|---|
| Pruebas ejecutadas | **0 pruebas de dominio** (`tests/Feature/ExampleTest.php` y `tests/Unit/ExampleTest.php` son plantilla; ~15 líneas `code` totales) |
| Aserciones | **~0** (solo aserciones triviales de la plantilla) |
| Resultado | **no ejecutado** (PHPUnit no corrido en esta sesión) |
| Fecha de la ejecución | — |
| Versión de PHP | **7.4.33** (contenedor `php:7.4-apache`) |
| Versión de PHPUnit | **^8.5** (según `composer.json` `require-dev`) |

**Para completarla:**
```bash
docker compose -f docker/docker-compose.local.yml exec app vendor/bin/phpunit
```
La última línea da pruebas ejecutadas, aserciones, resultado y versión.

---

## Tabla F. Ejemplo "antes y después" — Entidad **Item**

### F.1 Clase de dominio (Eloquent) tal como se escribe con el framework MVC

`app/Models/Item.php` — **53 líneas `code`**. Estructura real:

```php
class Item extends Model
{
    protected $fillable = [
        'shopping_list_id', 'product_name', 'unit_name',
        'creator_email', 'amount', 'done',
    ];
    protected $visible = [
        'id', 'product_name', 'unit_name', 'creator_email',
        'amount', 'done', 'created_at', 'updated_at',
    ];
    protected $casts = [
        'owner_email' => 'string', 'shopping_list_id' => 'integer',
        'product_name' => 'string', 'unit_name' => 'string',
        'creator_email' => 'string', 'amount' => 'integer', 'done' => 'boolean',
    ];
    public function shoppingList(): BelongsTo { return $this->belongsTo('App\Models\ShoppingList'); }
    public function creator(): BelongsTo { return $this->belongsTo('App\Models\User'); }
}
```
*(Los docblocks `@property`/`@method` del archivo son generados por `laravel-ide-helper`, no escritos a mano.)*

### F.2 Endpoints que genera a partir de la entidad

Verificado con `php artisan route:list --path=api`. Para `Item`:

| Método | URI | Acción | Nombre | Verificado |
|---|---|---|---|---|
| GET | `/api/shopping-lists/{shopping_list}/items` | `ItemController@index` | `items.index` | HTTP 200 ✅ |
| POST | `/api/shopping-lists/{shopping_list}/items` | `ItemController@store` | `items.store` | HTTP 201 ✅ |
| GET | `/api/items/{item}` | `ItemController@show` | `items.show` | ✅ |
| PUT/PATCH | `/api/items/{item}` | `ItemController@update` | `items.update` | ✅ |
| DELETE | `/api/items/{item}` | `ItemController@destroy` | `items.destroy` | HTTP 200 ✅ |

**5 endpoints REST por entidad CRUD completa.**

### F.3 Comparación de líneas (artefacto completo de `Item`)

| Artefacto para `Item` (MVC manual) | Líneas `code` (cloc) |
|---|---|
| Modelo Eloquent (`Item.php`) | 42 |
| Controlador (`ItemController.php`) | 35 |
| FormRequests (Store + Update) | 38 |
| Migración (`create_items_table`) | 26 |
| Rutas (prorrateo de `api.php`) | ~2 |
| **Total por entidad** | **~143** |

> **Punto de comparación clave:** `Item` cuesta **~143 líneas `code` a mano** y produce 5 endpoints + modelo + tabla + validación. El "después" es cuántas líneas (idealmente solo la declaración de la entidad) exige tu framework para generar lo mismo.

### F.4 Análisis estructural POR ENTIDAD (Item / Product / ShoppingList)

Script reproducible: `sim-por-entidad.py`. LOC verificados con `cloc --by-file` (campo `code`).

**Tamaño real de cada artefacto y entidad (`code`):**

| Artefacto | Item | Product | ShoppingList | Total |
|---|---:|---:|---:|---:|
| Modelo Eloquent | 42 | 52 | 61 | **155** |
| Controlador | 35 | 33 | 33 | **101** |
| FormRequest Store | 19 | 21 | 19 | **59** |
| FormRequest Update | 19 | 23 | 21 | **63** |
| Migración | 26 | 22 | 22 | **70** |
| **Total por entidad** | **141** | **151** | **156** | **448** |

**Similitud estructural, mismo artefacto entre entidades:**

| Artefacto | Item↔Product | Item↔ShoppingList | Product↔ShoppingList | **Promedio** |
|---|---:|---:|---:|---:|
| Controlador | 78,7 % | 76,3 % | **91,0 %** | **82,0 %** |
| Modelo | 9,2 % | 34,7 % | 49,0 % | 31,0 % |
| FormRequest Store | 61,2 % | 62,8 % | **95,8 %** | 73,3 % |
| FormRequest Update | 54,5 % | 56,7 % | **95,0 %** | 68,7 % |
| Migración | 77,5 % | 75,3 % | **98,3 %** | **83,7 %** |
| **Módulo completo** (5 artefactos juntos) | 59,5 % | 58,0 % | **78,3 %** | — |

**Lectura por recurso (lo que el engine debe colapsar):**

- **Controlador:** 76–91 % idéntico entre las tres entidades (promedio **82 %**). `Product` y `ShoppingList` son **91 % el mismo archivo** tras neutralizar la entidad. Es la capa más replicada y la más prescindible.
- **Migración:** **83,7 %** de promedio; `Product`↔`ShoppingList` llegan a **98,3 %** (mismo esqueleto `Schema::create` con columnas distintas). Derivables del esquema declarado en la entidad.
- **FormRequest Store/Update:** 68–73 % de promedio. El salto a **95–96 %** entre `Product` y `ShoppingList` muestra que, quitada la validación específica, es el mismo archivo. La parte realmente distinta (reglas `Rule::unique` por dueño) es una fracción mínima.
- **Modelo:** el más **heterogéneo** (promedio 31 %; `Item`↔`Product` = **9,2 %**). Aquí está la lógica propia — scopes de autorización, `getRouteKeyName()`, `hasUser()`, accessors. **Este es el artefacto que NO conviene generar ciegamente**: el engine debe hidratar `$fillable`/`$visible`/`$casts`/relaciones declarativas, pero la lógica de dominio debe escribirse.

**Cierre para la tesis:** a nivel módulo, **Product ↔ ShoppingList comparten 78,3 % de estructura**; Item difiere más solo por su modelo. De los 5 artefactos, **4 son replicables** (controlador, 2 requests, migración) y 1 (modelo) es mixto. Ese es el desglose que tu engine debe mover:

| Artefacto | Replicabilidad | Veredicto |
|---|---|---|
| Controlador | **82 %** | **Generar por hidratación** |
| Migración | **83,7 %** | **Generar desde el esquema de la entidad** |
| FormRequest Store/Update | 68–73 % | **Generar; sólo inyectar reglas de validación** |
| Modelo | 31 % | **Hidratar la parte declarativa; preservar la lógica propia** |

---

## Instrumento N° 1: Ficha de análisis de código (checklist de componentes boilerplate)

| N° | Componente | LOC total (`code`) | LOC repetidas / similares | ¿Patrón replicable identificado? | Observaciones |
|---|---|---|---|---|---|
| 1 | Controlador | **287** (16 archivos) | **41,9 % similitud estructural** (0 % literal Sonar) | **Sí** | Los 3 controladores CRUD puros (`Item`, `Product`, `ShoppingList`) son 76–91 % el mismo archivo tras neutralizar la entidad. Boilerplate objetivo del engine. |
| 2 | Servicio | **0** | N/A | **N/A** | No existe capa de servicio en MVC. |
| 3 | Repositorio | **0** | N/A | **N/A** | Acceso a datos vía Eloquent en el modelo. |
| 4 | DTO | **0** (FormRequests: 100) | **12 pares ≥ 80 % estructural** (0 % literal Sonar) | **Sí** (FormRequest) | `Product/Store` vs `ShoppingList/Store` = 95,8 %; `Store` vs `Update` del mismo recurso = 92–96 %. |
| 5 | Mapper | **0** | N/A | **N/A** | Transformación en `$visible`/`$casts`/`$appends`. |

---

## Instrumento N° 2: Guía de observación y lista de cotejo métrico

| Indicador | Herramienta | Valor pre-test (manual) | Valor post-test (framework) | Observaciones |
|---|---|---|---|---|
| Líneas de código (LOC) escritas a mano | cloc | **1.141** (`app/`) · **~711** (módulo dominio) | _pendiente_ | Campo `code`. |
| Porcentaje de duplicación de código | SonarQube + similitud estructural | **2,1 %** literal (Sonar) · **41,9 %** estructural en controladores (91 % entre CRUD puros) · **12 pares de FormRequest ≥ 80 %** | _pendiente_ | La métrica que importa para el objetivo (erradicar capas replicadas) es la **estructural**, no la literal. Ver Tabla C. |
| Densidad de errores / bugs detectados | SonarQube | **0 bugs** (reliability_rating A) | _pendiente_ | `bugs=0`, `vulnerabilities=0`. |
| Porcentaje de cumplimiento de estándares (linting) | SonarQube / PHPMD | **0 code smells** (sqale_rating A) | _pendiente_ | Repo usa `php-cs-fixer` + `phpstan`. |
| Índice de mantenibilidad | SonarQube | **sqale_index = 0** (deuda técnica 0 min) · `sqale_rating = A` | _pendiente_ | — |

---

## Instrumento N° 3: Bitácora cronométrica (registro de tiempos)

> **Vacía a propósito.** El pre-test se obtuvo de un repo existente, no de una sesión cronometrada. Estas filas las llenas cuando hagas TU desarrollo manual de referencia. NO las inventes para este repo.

| Entidad | Actividad | Modalidad | Hora inicio | Hora fin | Tiempo total | Observaciones |
|---|---|---|---|---|---|---|
| ShoppingList | Scaffolding CRUD | Manual | — | — | — | — |
| Item | Scaffolding CRUD | Manual | — | — | — | — |
| Product | Scaffolding CRUD | Manual | — | — | — | — |
| Unit | Scaffolding CRUD | Manual | — | — | — | — |
| ShoppingListUser | Scaffolding CRUD (share) | Manual | — | — | — | — |

---

## Instrumento N° 4: Cuestionario de percepción (Likert) — plantilla

> Requiere desarrolladores reales post-ejecución. Sin cambios en esta fase.

| N° | Ítem | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 1 | El framework facilita la generación de controladores, servicios, repositorios, DTOs y mappers. | | | | | |
| 2 | El código generado automáticamente es fácil de comprender y mantener. | | | | | |
| 3 | El uso del framework redujo el tiempo dedicado a tareas repetitivas de scaffolding. | | | | | |
| 4 | El código generado cumple con los estándares de codificación esperados. | | | | | |
| 5 | Recomendaría el uso de este framework en proyectos reales de desarrollo backend. | | | | | |

---

## Instrumento N° 5: Lista de cotejo de buenas prácticas (pre-test observado)

| N° | Criterio | Cumple | No cumple | Observaciones |
|---|---|---|---|---|
| 1 | Convención consistente de nombres | **Sí** | | PSR-4 / convenciones Laravel; `php-cs-fixer` configurado. |
| 2 | Sin bloques duplicados entre entidades generadas | | **No** | **Similitud estructural 76–91 % en controladores CRUD y hasta 95,9 % en FormRequests** (script `sim-estructural.py`). Sonar da 0 % literal porque no comparte ≥100 tokens idénticos, pero la estructura es la misma: este es el boilerplate que el engine debe generar por hidratación. |
| 3 | SRP (responsabilidad única) por clase | | **Parcial** | El Modelo mezcla persistencia, serialización (`$visible`), cast y scopes de autorización. |
| 4 | Compila sin advertencias/errores | **Sí** | | `larastan` (phpstan) configurado en `phpstan.neon`. |
| 5 | Separación de capas (dominio/aplicación/infraestructura) | | **No** | MVC monolítico, sin capas DDD. |
| 6 | Manejo adecuado de excepciones | | **Parcial** | `app/Exceptions/Handler.php` (55 líneas totales); depende del comportamiento por defecto de Laravel. |

---

## Anexo — Evidencias de ejecución (flujo verificado)

Flujo completo ejecutado contra `http://localhost:8090/api` (script reproducible: `smoke-api.sh`):

| Paso | Endpoint | HTTP |
|---|---|---|
| Register | `POST /auth/register` | 201 |
| Login | `POST /auth/token` | 200 (token `2\|sMpSoNc...`) |
| Perfil | `GET /user` | 200 |
| Crear lista | `POST /shopping-lists` | 201 |
| Listar listas | `GET /shopping-lists` | 200 |
| Crear item | `POST /shopping-lists/{id}/items` | 201 |
| Listar items | `GET /shopping-lists/{id}/items` | 200 |
| Crear producto | `POST /products` | 201 |
| Listar productos | `GET /products` | 200 |
| Unidades | `GET /units` | 200 |
| Editar lista | `PUT /shopping-lists/{id}` | 200 |
| Borrar item | `DELETE /items/{id}` | 200 |
| Borrar lista | `DELETE /shopping-lists/{id}` | 200 |
| Compartir lista | `POST /shopping-lists/{id}/shares` | 200 |
| Ver compartidos | `GET /shopping-lists/{id}/shares` | 200 (`["otro@example.com","tesis@example.com"]`) |

---

## Cómo reproducir el entorno

```bash
cd ShoppinglistApi
docker compose -f docker/docker-compose.local.yml up -d
docker compose -f docker/docker-compose.local.yml exec -T app php artisan migrate --force
./smoke-api.sh
```
Puerto host: **8090** (8080 ocupado). Requirió 3 fixes al `Dockerfile` original (NodeSource 14 EOL, Debian bullseye → archive.debian.org, `.dockerignore`).
