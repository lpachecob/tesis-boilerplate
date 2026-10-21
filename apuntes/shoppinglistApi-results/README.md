# Para tesis — Sustento de medición (pre-test OE1)

Esta carpeta reúne **todo el material de sustento** de la medición pre-test
sobre `ammannbe/ShoppinglistApi` (Laravel 7, PHP 7.4, MVC clásico). Es una
**copia autocontenida**: podés llevarla a otro lado y todo queda documentado,
aunque los scripts necesitan el repo original para analizar el código.

Contexto: esta medición cuantifica el **boilerplate manual** que el engine del
framework de tesis debe erradicar. El objetivo declarado es que el desarrollador
**solo declare entidades** y el engine genere controladores, servicios,
repositorios, DTOs y mappers **por hidratación**.

---

## Contenido

```
para-tesis/
├── README.md                     ← este índice
├── metricas/
│   ├── pre-test-tablas-completas.md   ← Tablas A–F + Instrumentos 1–5 (documento principal)
│   └── ODD-pre-test-OE1.md            ← métricas cloc iniciales (Tablas A, B, D, F)
├── scripts/
│   ├── sim-estructural.py        ← similitud estructural global (controladores, FormRequests)
│   ├── sim-por-entidad.py        ← similitud estructural por entidad (Item/Product/ShoppingList)
│   ├── smoke-api.sh              ← evidencia del flujo end-to-end de la API
│   └── smoke-api-full.sh         ← flujo completo automatizado (register→login→CRUD)
├── configuracion/
│   ├── docker-compose.local.yml  ← entorno local (app + MariaDB) — puerto 8090
│   ├── docker-compose.sonar.yml  ← SonarQube + Postgres
│   ├── Dockerfile                ← con los 2 fixes para toolchain EOL
│   ├── .dockerignore             ← crítico: excluye .env del build
│   ├── .env.example              ← plantilla de variables
│   └── sonar-project.properties  ← config del análisis Sonar
├── api/
│   ├── ShoppinglistApi.postman_collection.json
│   ├── ShoppinglistApi.postman_environment.json
│   └── ShoppinglistApi.insomnia.json
└── evidencias/
    ├── 01-similitud-global.txt        ← salida cruda de sim-estructural.py
    ├── 02-similitud-por-entidad.txt   ← salida cruda de sim-por-entidad.py
    └── 03-sonarqube-metricas.txt      ← métricas SonarQube vía API (crudas)
```

---

## El número que sostiene la tesis

| Capa / artefacto | Reproducibilidad (`code`) | Veredicto para el engine |
|---|---|---|
| **Controlador** | **82 %** idéntico entre entidades | **Generar por hidratación** |
| **Migración** | **83,7 %** | **Generar desde el esquema** |
| **FormRequest Store/Update** | 68–73 % | **Generar; solo inyectar validación** |
| **Modelo** | **31 %** (el más heterogéneo) | **Hidratar parte declarativa; preservar lógica de dominio** |
| Servicio / Repositorio / Mapper | no existen (MVC) | El engine los **introduce** como valor nuevo |

Del módulo de dominio (~711 líneas `code`), **~95 % son capas replicadas**. El
engine debe llevar esa repetición estructural a ~0, dejando al dev declarar solo
la entidad.

---

## Cómo reproducir todo

```bash
# 1) Levantar el entorno
cd <repo>/ShoppinglistApi
docker compose -f docker/docker-compose.local.yml up -d
docker compose -f docker/docker-compose.local.yml exec -T app php artisan migrate --force

# 2) Evidencia de la API
bash para-tesis/scripts/smoke-api-full.sh

# 3) Similitud estructural (desde cualquier ubicación)
python3 para-tesis/scripts/sim-estructural.py    > para-tesis/evidencias/01-similitud-global.txt
python3 para-tesis/scripts/sim-por-entidad.py    > para-tesis/evidencias/02-similitud-por-entidad.txt

# 4) SonarQube (duplicación literal, contraste)
docker compose -f docker/docker-compose.sonar.yml up -d
docker run --rm --network docker_default \
  -e SONAR_HOST_URL=http://sonarqube:9000 -e SONAR_TOKEN=<token> \
  -v "$PWD:/usr/src" sonarsource/sonar-scanner-cli:latest
curl -s "http://localhost:9000/api/measures/component?component=shoppinglistapi&metricKeys=duplicated_lines_density,duplicated_lines,duplicated_blocks,ncloc"
```

---

## Metodología (para el capítulo de la tesis)

- **LOC**: `cloc v2.06`, campo **`code`** (excluye líneas en blanco y comentarios).
- **Duplicación literal**: SonarQube Community 26.10.0, métrica `duplicated_lines_density`
  (umbral ≥ 100 tokens idénticos). Mide copy-paste **literal**.
- **Similitud estructural** (métrica primaria del objetivo): normalización de tokens
  (se eliminan docblocks/imports; se neutralizan nombres de entidad y variables) +
  `difflib.SequenceMatcher`. Mide repetición de **esqueleto**, que es lo que el
  engine colapsa.
- **Jerarquía de métricas**: la **estructural** es la que importa para el objetivo
  (erradicar capas replicadas). Sonar se incluye como **contraste**: da 0 % en
  controladores/requests porque su esqueleto se repite pero los cuerpos difieren, lo
  que sería un **falso negativo** para este objetivo. Ambos hechos se documentan por
  separado en la Tabla C.

- **Delimitación temporal**: 2026-10-20 → 2026-10-21.
- **Stack medido**: PHP 7.4.33 · Laravel 7 · Sanctum 2.6 · MariaDB 10.11.

---

## Notas de honestidad metodológica

- Este repo es **MVC clásico, no DDD**. Las capas Servicio/Repositorio/DTO/Mapper se
  registran como **`0 — no aplica`**: son ausencias reales del paradigma, no huecos.
  (El usuario declaró que hará su versión DDD posteriormente; esta medición establece
  la **línea base MVC**.)
- La **Tabla D** (tiempos) es una **estimación de ingeniero**, no una bitácora
  cronometrada. La bitácora real (Instrumento N° 3) se llena en el desarrollo propio.
- Las **Tablas A–C, E, F e Instrumentos 1, 2 y 5** se llenan con datos **medidos**
  (cloc, SonarQube, evidencia HTTP, análisis estructural reproducible).
- Los scripts son **portables**: detectan la raíz del repo por su cuenta y pueden
  ejecutarse desde `para-tesis/scripts/` o desde la raíz indistintamente.
