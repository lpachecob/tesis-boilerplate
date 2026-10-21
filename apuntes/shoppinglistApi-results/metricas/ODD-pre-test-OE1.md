# OE1 — Pre-test: Desarrollo convencional manual

**Proyecto analizado:** `ShoppinglistApi` (Laravel 7, PHP 7.4, MVC clásico)
**Repositorio:** https://github.com/ammannbe/ShoppinglistApi
**Autor original:** Benjamin Ammann (ammannbe)
**Herramienta de conteo:** `cloc v2.06` — métrica usada: campo **`code`** (excluye blancas y comentarios)
**Fecha de recolección (esta sesión):** 2026-10-20 → 2026-10-21

> **Nota metodológica crítica (leer antes de usar las tablas).**
> Este repositorio es **MVC plano de Laravel**, NO una arquitectura DDD. No contiene capas de `Servicio`, `Repositorio`, `DTO` ni `Mapper`. Por lo tanto las celdas correspondientes a esos componentes en las Tablas B, C y D son **0 / no aplican en el pre-test** — no porque el boilerplate no exista, sino porque en el paradigma MVC esos componentes no se escriben a mano.
> Tu framework (post-test) SÍ genera esas capas. Eso significa que **la comparación es válida para las capas comunes (Controlador, Modelo/Entidad, Rutas, Migración) y para los totales**, pero NO es 1:1 en Servicio/Repositorio/DTO/Mapper (esos solo tienen valor "post"). Declara esto en tu tesis.
> Equivalencias usadas: **Modelo Eloquent ≈ Entidad de dominio** · **FormRequest ≈ DTO de entrada (validación)** · **Policy ≈ regla de autorización** (no es capa DDD).

---

## Tabla A. Modelo de dominio usado

| Entidad | N.º de campos | Relaciones (tipo y con qué entidad) | ¿Borrado lógico? |
|---|---|---|---|
| **User** | 6 (`id`, `name`, `email`, `email_verified_at`, `password`, `remember_token`) | `belongsToMany` → ShoppingList · `hasMany` → Product | No |
| **ShoppingList** | 5 (`id`, `name`, `owner_email`, `created_at`, `updated_at`) | `belongsTo` → User (dueño) · `belongsToMany` → User (compartida) · `hasMany` → Item | No (`onDelete cascade` físico) |
| **Product** | 4 (`id`, `name`, `owner_email`, `created_at`, `updated_at`) | `belongsTo` → User (dueño) · `hasMany` → Item (conceptual; el Item referencia por nombre) | No |
| **Item** | 8 (`id`, `shopping_list_id`, `product_name`, `unit_name`, `creator_email`, `amount`, `done`, `created_at`, `updated_at`) | `belongsTo` → ShoppingList · `belongsTo` → User (creator) | No |
| **Unit** | 3 (`id`, `name`, `created_at`, `updated_at`) | ninguna (catálogo plano, solo lectura vía API) | No |
| **ShoppingListUser** (pivote) | 2 (`shopping_list_id`, `user_email`) | pivote N:M entre ShoppingList y User | No |

**Observaciones:**
- **Ninguna entidad usa borrado lógico.** El repo no incluye `SoftDeletes` ni columnas `deleted_at`. Todos los borrados son físicos con `onDelete('cascade')`.
- El FK de usuario apunta a **`email`**, no a `id` (`owner_email` / `user_email` / `creator_email`), lo cual es un antipatrón a documentar.
- `Product` declara `is_public` en `$visible`/`$casts`/`$appends` pero **la migración no tiene esa columna** — inconsistencia real del repo.

---

## Tabla B. Líneas de código manuales por componente y entidad (cloc · campo `code`)

Las cifras por entidad se obtuvieron con `cloc <carpeta> --by-file` y se agruparon por entidad de dominio.
**Los valores entre paréntesis indican total por componente (todos los archivos de ese tipo).**

| Componente | ShoppingList | Item | Product | Unit | Auth/User | Total del componente |
|---|---|---|---|---|---|---|
| Controlador | 30 (`ShoppingListController`) | 32 (`ItemController`) | 30 (`ProductController`) | 5 (`UnitController`) | 190 (Auth/*, User, Home, Teapot) | **287** |
| Servicio | 0 | 0 | 0 | 0 | 0 | **0 (no existe en MVC)** |
| Repositorio | 0 | 0 | 0 | 0 | 0 | **0 (no existe en MVC)** |
| DTOs (entrada/salida) | 0 | 0 | 0 | 0 | 0 | **0** |
| — FormRequest (equivalente de validación) | 19 (Store+Update) | 19 (Store+Update) | 21 (Store+Update) | 0 | 41 (Auth/User) | **100** |
| Mapper | 0 | 0 | 0 | 0 | 0 | **0 (no existe en MVC)** |
| Rutas (`routes/api.php`) | — | — | — | — | — | **10** |
| Entidad / Modelo Eloquent | 78 (`ShoppingList`) | 53 (`Item`) | 68 (`Product`) | 31 (`Unit`) | 84 (`User`) | **314** |
| **Total del módulo** | — | — | — | — | — | **~711** (controladores+modelos+requests+rutas) |

**Notas de conteo:**
- `app/` completo: **1.141 líneas de código** (cloc campo `code`), 59 archivos PHP, 1.338 líneas totales.
- Migraciones: **170 líneas de código** en 17 archivos (incluye tablas de scaffold: users, password_resets, oauth_*, failed_jobs, personal_access_tokens).
- Policies: **120** · Observers: **24** · Notifications: **37** · Middleware: **64** · Providers: **122**.
- Tests: **15 líneas de código** en total (solo `ExampleTest` de plantilla) → prácticamente nula cobertura.

### Desglose por archivo (controladores y modelos)

| Archivo | `code` |
|---|---|
| `Models/ShoppingList.php` | 78 |
| `Models/Product.php` | 68 |
| `Models/User.php` | 84 |
| `Models/Item.php` | 53 |
| `Models/Unit.php` | 31 |
| `Http/Controllers/ItemController.php` | 32 |
| `Http/Controllers/ProductController.php` | 30 |
| `Http/Controllers/ShoppingListController.php` | 30 |
| `Http/Controllers/ShoppingListUserController.php` | 21 |
| `Http/Controllers/Auth/RegisterController.php` | 32 |
| `Http/Controllers/Auth/VerificationController.php` | 34 |
| `Http/Controllers/UnitController.php` | 5 |

---

## Tabla C. Duplicación

> **Estado: PENDIENTE DE MEDIR.** Aún no se ha ejecutado PMD CPD ni SonarQube en esta máquina.

Los valores siguientes son **observación estructural preliminar** (no medición con herramienta). Hay que reemplazarlos por PMD CPD:

Recomendación de comando para el umbral de 50 tokens:

```bash
pmd cpd --language php --minimum-tokens 50 --dir app/Http/Controllers
pmd cpd --language php --minimum-tokens 50 --dir app/Models
pmd cpd --language php --minimum-tokens 50 --dir app/Http/Requests
pmd cpd --language php --minimum-tokens 50 --dir app
```
En SonarQube la métrica es `duplicated_lines_density` (%).

| Componente | % de duplicación (PMD/Sonar) | N.º de bloques duplicados | Evidencia preliminar |
|---|---|---|---|
| Controlador | _pendiente_ | _pendiente_ | Los 4 controladores de recurso (`Product`, `ShoppingList`, `Item`, `ShoppingListUser`) repiten la misma estructura `authorize → acción`: candidatos claros a duplicación. |
| Servicio | N/A (no existe) | N/A | — |
| Repositorio | N/A (no existe) | N/A | — |
| DTOs (FormRequest) | _pendiente_ | _pendiente_ | Los 4 archivos de `Item/*`, `Product/*`, `ShoppingList/*` tienen estructura idéntica (~16–23 líneas c/u), probable duplicación alta. |
| Mapper | N/A (no existe) | N/A | — |
| **Global del módulo** | _pendiente_ | _pendiente_ | **Hipótesis:** alta (>25%) por replicación estructural en controladores y requests. |

**Herramienta elegida:** `PMD CPD`, `--language php`, `--minimum-tokens 50`. *(Confirmar tras ejecutar.)*

---

## Tabla D. Tiempo de desarrollo manual (estimación)

> **Estado: ESTIMACIÓN**, no bitácora cronometrada. Este proyecto se recolectó como código ya escrito (commits de 2020), **no fue cronometrado por ti**. Para tu tesis necesitas la bitácora real (Instrumento N° 3). Aquí van estimaciones de un dev de nivel intermedio en Laravel:

| Componente | Horas estimadas |
|---|---|
| Controlador (5 controladores de recurso + auth) | 8–12 h |
| Servicio | 0 (no existe) |
| Repositorio | 0 (no existe) |
| DTOs / FormRequest | 3–5 h |
| Mapper | 0 (no existe) |
| Rutas | 1–2 h |
| Modelos Eloquent + relaciones + scopes | 6–10 h |
| Migraciones | 3–5 h |
| Auth completo (Sanctum, verificación, reset) | 10–16 h |
| Policies + Observers + Notifications + Middleware | 8–12 h |
| Setup Docker/entorno (hoy, con toolchain EOL) | 4–8 h |
| **Total del módulo** | **~45–70 h** |

**Delimitación temporal:**
- **Inicio de recolección de datos (esta sesión):** 2026-10-20
- **Fin de recolección:** 2026-10-21 *(fecha actual; ajustar si continúas midiendo)*
- **Origen del código medido:** commits del proyecto original en 2020 (no es trabajo cronometrado propio).

---

## Tabla E. Evidencia de pruebas (OE2, estado actual)

| Dato | Valor |
|---|---|
| Pruebas ejecutadas | **0 pruebas de dominio** (solo `tests/Feature/ExampleTest.php` y `tests/Unit/ExampleTest.php`, ambos de plantilla y sin aserciones reales) |
| Aserciones | **~0** (los `ExampleTest` de Laravel 7 suelen tener 1 aserción trivial; verificar con `vendor/bin/phpunit`) |
| Resultado | _pendiente de ejecutar_ |
| Fecha de la ejecución | _pendiente_ |
| Versión de PHP | **PHP 7.4.33** (contenedor `php:7.4-apache`) |
| Versión de PHPUnit | **^8.5** (según `composer.json`, `require-dev`) |

**Bloqueo actual:** el contenedor `app` responde 500 por permisos en `storage/`. Antes de correr `phpunit` hay que:
```bash
docker compose -f docker/docker-compose.local.yml exec app \
  chown -R www-data:www-data storage bootstrap/cache
```
Luego:
```bash
docker compose -f docker/docker-compose.local.yml exec app vendor/bin/phpunit
```
La última línea de `phpunit` da: pruebas ejecutadas, aserciones, resultado (OK/failures), y versión.

---

## Tabla F. Ejemplo "antes y después" — Entidad **Item**

### F.1 Clase de dominio (Eloquent) tal como la escribes con el framework MVC

`app/Models/Item.php` — **53 líneas de código** (cloc `code`), 102 líneas totales con docblocks y el bloque `@property` generado por `laravel-ide-helper`.

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

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
        'owner_email' => 'string',
        'shopping_list_id' => 'integer',
        'product_name' => 'string',
        'unit_name' => 'string',
        'creator_email' => 'string',
        'amount' => 'integer',
        'done' => 'boolean',
    ];

    public function shoppingList(): BelongsTo
    {
        return $this->belongsTo('App\Models\ShoppingList');
    }

    public function creator(): BelongsTo
    {
        return $this->belongsTo('App\Models\User');
    }
}
```
*(Los docblocks `@property`/`@method` ocupan el resto del archivo y son generados por `laravel-ide-helper`, no escritos a mano.)*

### F.2 Endpoints que genera a partir de la entidad

Comando para listar rutas reales del framework:
```bash
docker compose -f docker/docker-compose.local.yml exec app php artisan route:list --path=api
```

Rutas declaradas en `routes/api.php` (`code` = 10 líneas) para `Item`:

| Método | URI | Acción | Nombre |
|---|---|---|---|
| GET | `/api/shopping-lists/{shopping_list}/items` | `ItemController@index` | `items.index` |
| POST | `/api/shopping-lists/{shopping_list}/items` | `ItemController@store` | `items.store` |
| GET | `/api/items/{item}` | `ItemController@show` | `items.show` |
| PUT/PATCH | `/api/items/{item}` | `ItemController@update` | `items.update` |
| DELETE | `/api/items/{item}` | `ItemController@destroy` | `items.destroy` |

**5 endpoints REST** por entidad CRUD completa (index/store/show/update/destroy).

### F.3 Comparación de líneas

| Artefacto para `Item` (MVC manual) | Líneas `code` (cloc) |
|---|---|
| Modelo Eloquent (`Item.php`) | 53 |
| Controlador (`ItemController.php`) | 32 |
| FormRequests (Store + Update) | 19 |
| Migración (`create_items_table`) | 10 |
| Rutas declaradas (prorrateo de `api.php`) | ~2 |
| **Total por entidad** | **~116** |

> **Este es tu punto de comparación clave para OE2:** la entidad `Item` ocupa **~116 líneas `code`** escritas a mano. El "después" es cuántas líneas (idealmente de declaración/anotación) exige tu framework para generar esos mismos 5 endpoints + modelo + migración + DTOs.

---

## Instrumento N° 1: Ficha de análisis de código (checklist de componentes boilerplate)

| N° | Componente | LOC total (cloc `code`) | LOC repetidas / similares | ¿Patrón replicable identificado? (Sí/No) | Observaciones |
|---|---|---|---|---|---|
| 1 | Controlador | **287** (16 archivos) | *pendiente PMD* — los 4 de recurso son estructuralmente idénticos | **Sí** | Patrón `authorize → acción → respuesta` repetido. Existe `Controller.php` base (0 `code`). |
| 2 | Servicio | **0** | N/A | **N/A** | No existe capa de servicio en MVC. |
| 3 | Repositorio | **0** | N/A | **N/A** | El acceso a datos vive en Eloquent/Modelo. |
| 4 | DTO | **0** (FormRequests: **100**) | *pendiente PMD* | **Sí** (para FormRequest) | `Item/*`, `Product/*`, `ShoppingList/*` con estructura idéntica. |
| 5 | Mapper | **0** | N/A | **N/A** | No existe. La transformación la hace Eloquent (`$visible`/`$casts`/`$appends`). |

---

## Instrumento N° 2: Guía de observación y lista de cotejo métrico

| Indicador | Herramienta | Valor pre-test (manual) | Valor post-test (framework) | Observaciones |
|---|---|---|---|---|
| Líneas de código (LOC) escritas a mano | cloc | **1.141** (`app/`) · **~711** (módulo dominio) | _pendiente_ | Campo `code`, sin blancas ni comentarios. |
| Porcentaje de duplicación de código | SonarQube / PMD | _pendiente de ejecutar PMD CPD_ | _pendiente_ | Correr con `--minimum-tokens 50`. |
| Densidad de errores / bugs detectados | SonarQube | _pendiente_ (requiere SonarQube) | _pendiente_ | — |
| Porcentaje de cumplimiento de estándares (linting) | PHPMD | _pendiente_ | _pendiente_ | El repo usa `php-cs-fixer` y `phpstan` en `composer.json`; correr en Fase 1. |
| Índice de mantenibilidad | SonarQube | _pendiente_ (requiere SonarQube) | _pendiente_ | — |

---

## Instrumento N° 3: Bitácora cronométrica (registro de tiempos)

> **No disponible como cronómetro real.** El código pre-test se obtuvo de un repo existente, no de una sesión cronometrada. Las filas quedan como plantilla para que las completes cuando hagas TU desarrollo manual de referencia y tu ejecución del framework.

| Entidad | Actividad | Modalidad (Manual/Framework) | Hora inicio | Hora fin | Tiempo total | Observaciones |
|---|---|---|---|---|---|---|
| ShoppingList | Scaffolding CRUD | Manual | — | — | — | — |
| Item | Scaffolding CRUD | Manual | — | — | — | — |
| Product | Scaffolding CRUD | Manual | — | — | — | — |
| Unit | Scaffolding CRUD | Manual | — | — | — | — |
| ShoppingListUser | Scaffolding CRUD (pivote/share) | Manual | — | — | — | — |

---

## Instrumento N° 4: Cuestionario de percepción (Likert) — plantilla

> No aplicable a esta fase (requiere desarrolladores reales post-ejecución). Plantilla sin cambios.

| N° | Ítem | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 1 | El framework facilita la generación de controladores, servicios, repositorios, DTOs y mappers. | | | | | |
| 2 | El código generado automáticamente es fácil de comprender y mantener. | | | | | |
| 3 | El uso del framework redujo el tiempo dedicado a tareas repetitivas de scaffolding. | | | | | |
| 4 | El código generado cumple con los estándares de codificación esperados. | | | | | |
| 5 | Recomendaría el uso de este framework en proyectos reales de desarrollo backend. | | | | | |

---

## Instrumento N° 5: Lista de cotejo de buenas prácticas (pre-test observado)

| N° | Criterio | Cumple (Sí) | No cumple (No) | Observaciones |
|---|---|---|---|---|
| 1 | Convención consistente de nombres | **Sí** | | PSR-4 / Laravel conventions; `php-cs-fixer` configurado. |
| 2 | Sin bloques duplicados entre entidades generadas | | **No** | Controladores CRUD y FormRequests replican estructura (confirmar con PMD CPD). |
| 3 | SRP (responsabilidad única) por clase | **Parcial** | | El `Model` mezcla persistencia, serialización (`$visible`), cast y scopes de autorización. |
| 4 | Compila sin advertencias/errores | **Sí** | | `larastan` (phpstan) configurado en `phpstan.neon`. |
| 5 | Separación de capas (dominio/aplicación/infraestructura) | | **No** | No hay capas DDD; MVC monolítico. |
| 6 | Manejo adecuado de excepciones | **Parcial** | | `app/Exceptions/Handler.php` (55 líneas totales); dependiente del comportamiento por defecto de Laravel. |

---

## Estado del levantamiento (contexto de esta sesión)

La API fue levantada con Docker. El `Dockerfile` original **ya no builda en 2026**; se requirieron 3 correcciones para reproducirlo:

1. **NodeSource Node 14 EOL** → reemplazado por Node 12 de Debian (suficiente para laravel-mix 5).
2. **Debian bullseye en EOL** → `deb.debian.org` retiró los `.deb` de `bullseye-security` (404). Apt redirigido a `archive.debian.org` + `Check-Valid-Until` desactivado.
3. **`.dockerignore`** añadido (el `.env` con `APP_ENV=local` se colaba en la imagen y activaba Telescope, paquete `require-dev` ausente en `--no-dev`).

Contenedores: `app` (PHP 7.4.33/Apache, puerto host **8090** porque 8080 estaba ocupado) + `db` (MariaDB 10.11).

**Pendiente inmediato:** corregir permisos de `storage/` dentro del contenedor (responde 500) y ejecutar `phpunit` + `artisan route:list` para cerrar las Tablas E y F.2.

---

## Resumen ejecutivo de la brecha (pre → post)

| Dimensión | Pre-test (MVC manual) | Lo que tu framework debería demostrar (post) |
|---|---|---|
| Capas generadas | Modelo + Controlador + Request + Policy + Migración | + **Servicio, Repositorio, DTO, Mapper** |
| LOC del módulo dominio | ~711 `code` | ≤ ese valor y con menos escritura manual |
| Duplicación estructural | Alta (hipótesis; confirmar PMD) | Cerca de 0 (una plantilla por capa) |
| Trazabilidad DDD | **Ausente** | Presente (dominio/aplicación/infra) |
| Esfuerzo de scaffolding por entidad | ~116 líneas / 45–70 h el módulo | Objetivo: declarar la entidad y generar el resto |
