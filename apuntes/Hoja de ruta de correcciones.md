---
tags: [apunte, tesis, correccion, auditoria, bibliografia, hoja-de-ruta]
tipo: hoja de ruta
estado: en curso
fecha: 2026-09-27
---

# Hoja de ruta de correcciones

> Resultado de la auditoría del 27 de septiembre de 2026 sobre 25 entradas
> bibliográficas y 76 atribuciones a autores. Informe completo en
> `INFORME-auditoria-bibliografia-y-definiciones.md`.

**Estado de avance — 28 de septiembre de 2026**

| Bloque | Qué cubre | Estado |
| --- | --- | --- |
| A | El vault contiene el documento equivocado | ✅ Cerrado — 7 items |
| D | Formato de la bibliografía | ✅ Cerrado — 4 items (F1–F4) |
| C | Metadatos de la bibliografía | ✅ Cerrado — 7 items |
| E | Atribuciones y metadatos | ✅ Cerrado — 29 correcciones |
| B | Atribuciones a fuentes **distintas de XBoot** (B1–B9) | ✅ **Cerrado (2026-09-28)** — B1, B2, B3, B5, B6, B7, B8, B9 ✅ + T1/T2 Trebejo ✅ + B4 ✅ |
| D4 | El **lote XBoot**: 24 atribuciones del cuerpo | ✅ Cerrado — 18 sitios corregidos (2026-09-28) |
| Pasada final | Segunda revisión manual completa: atribuciones restantes | ✅ **Cerrada (2026-09-28)** — 26 ediciones aplicadas (A1–A9 atribuciones falsas + B1–B13 matices) |

Cada título de bloque lleva ✅ cuando está cerrado y ⬜ cuando queda trabajo.

> ### ⚠️ Tres cosas que se confunden entre sí
>
> **1. Hay dos series «D», y una además repite los números.**
> El **bloque D** es el formato de la bibliografía; sus items se renumeraron como
> **F1–F4** para eliminar la colisión. Las **decisiones D1–D4** son preguntas de
> contenido, no de formato. Antes de leer un «D3», hay que saber en qué sección
> se está.
>
> **2. El lote XBoot NO es el bloque B.** Los dos son «afirmaciones atribuidas a un
> autor», y por eso se confunden, pero son trabajo distinto y con fuentes distintas.
> El **bloque B** son 9 atribuciones a 8 fuentes que **no** son XBoot: Evans,
> Trebejo, Fowler, Vasquez, Özkan, GitClear, Stack Overflow y Bobadilla.
> El **lote XBoot** son 24 atribuciones al artículo de Alkazemi y Nour, y en esta
> hoja se llama **D4** porque nació como una decisión, no como un bloque.
>
> **3. El bloque B está partido en dos.** **B4–B9** (6 items) se corrigen sin
> decidir nada: se borra la atribución falsa y se dice lo que la fuente sí dice.
> **B1, B2, B3 y B5** (4 items) están **bloqueados** hasta que se tomen las
> decisiones D1 y D2, porque tocan el fundamento de la tesis.

## La idea en una línea

No son errores sueltos: hay tres capas, y la de arriba condiciona a la de abajo.
Primero se arregla **qué documento es cada fuente**; después **qué dice cada
autor**; al final **cómo está escrita cada cita**.

---

## ✅ A. El vault contiene el documento equivocado — CERRADO

Nada de lo de abajo se arregla por coherencia interna: se arregla porque la
fuente citada no respalda la cita. **Es la capa que bloquea a las demás.**

| # | Qué estaba mal | Qué es la realidad | Estado |
| --- | --- | --- | --- |
| A1 | `Alqahtani 2025 - XBoot`: 4 autores, *Applied Sciences* 15(**8**), 4123, DOI `app15084123` | **Alkazemi, B. Y., & Nour, M. K. (2025)**, 15(**19**), **10621**, DOI `app151910621`. Autores, número, artículo y DOI: los cuatro mal | ✅ |
| A2 | El PDF archivado como XBoot | Es *In Silico Methods for Assessing Cancer Immunogenicity* (Sotirov y Dimitrov): **inmunología oncológica** | ✅ |
| A3 | `Larsson, E., Runeson, P., & Engström, E.` | **Karlsson, S., Jongeling, R., Čaušević, A., & Sundmark, D.** Ninguno de los tres declarados existe en el trabajo | ✅ |
| A4 | `Gurgul, V., Kłos, J., Madeyski, L., & Mroczek, T.` | **Gurgul, V., Gubela, R., & Lessmann, S.** Tres de cuatro inventados | ✅ |
| A5 | Cosme Escalera, año **2022**, un solo autor | **2024**, y falta el coautor **Quispe Cansaya**. El 2022 viene del título («Juliaca 2022») | ✅ |
| A6 | `Peldszus` con sede `FSE, Industry Track` y `arXiv:2601.16705` | La fuente es una versión de autor sin cabecera. Ni sede, ni ID, ni año aparecen en ninguna línea | ✅ |
| A7 | «investigadores en Suecia en la **Universidad de Lund**» (L105) | La afiliación real es **ABB AB** y **Mälardalen University**, ambas en **Västerås**. `Lund` no aparece ni una vez en el artículo | ✅ |

### Qué se aplicó

- **6 entradas bibliográficas** reescritas con los datos verificados contra la fuente.
- **32 destinos de wikilink** actualizados en el cuerpo (25 de XBoot, 5 de Karlsson, 3 de Gurgul, 2 de Cosme Escalera) más las 3 líneas de enlace de la bibliografía.
- **2 citas en texto plano** sin wikilink corregidas (una a XBoot, otra a Karlsson con número de página).
- **3 carpetas y 4 archivos** del vault renombrados; el artículo de inmunología se conservó con su identidad real en mayúsculas en vez de borrarse.
- **1 defecto de enlace oculto**: los wikilinks de Cosme Escalera apuntaban a un nombre **truncado** (`…de la empre`, sin «ma») que venía del documento original. 2 enlaces reparados.
- **`referencias/Alkazemi 2025 - XBoot/`** con el PDF real y su `.md` extraído (21.053 palabras). Esto **desbloquea D4**.

### Cómo se verificó

| Comprobación | Resultado |
| --- | --- |
| Rastros de los errores corregidos (`Alqahtani`, `Larsson`, `app15084123`, `Lund`, …) | **0 apariciones** en los 11 tokens |
| Wikilinks con destino | **212 destinos, 0 rotos** |
| Región de ANEXOS (L661–824) | Byte a byte idéntica salvo 4 líneas de la matriz de operacionalización que citan al autor corregido |
| Texto visible de la tesis | 32 líneas modificadas, **todas** explicables por los renombres y las 6 entradas; ninguna otra prosa alterada |
| `tesis.bak` | `862a0580bbdeacc492aff57cbe34edfb`, sin cambios |

### Lo que queda abierto de este bloque

- **`Master’s Thesis` en la entrada de Cosme Escalera** sigue ahí, aunque la fuente
  es un título profesional. Es el ítem **C1**, no de este bloque: se deja para
  cuando se ataque C, para que la verificación de cada bloque sea concluyente.
- **Los enlaces rotos del documento original** eran 39, no 35: 4 autorrealimentados
  por los renombres previos de carpetas más 2 truncados. Ya no queda ninguno.

**El patrón detrás de A3, A4 y A5:** los autores se rellenaron desde el **nombre de
la carpeta del vault**, que a su vez se generó desde la bibliografía. El error se
realimenta. Por eso corregir la bibliografía sin corregir las carpetas reproduce el
error en la siguiente pasada. **Ya está cortado** — ver «Cómo se cortó el bucle»
más abajo.

**Consecuencia directa:** las 16 atribuciones a «Alqahtani et al. (2025)» se
verificaron contra el artículo equivocado. **Sus veredictos son nulos** y hay que
rehacerlos contra el PDF real, ya extraído a `.md` (ver D4).

---

## ✅ Cómo se cortó el bucle de autorrealimentación

La causa de fondo no era un error concreto: era que **la identidad de cada referencia
está escrita a mano en tres sitios**, y nada los comparaba.

| # | Copia del dato | Cómo se mantenía |
| --- | --- | --- |
| 1 | Texto de la entrada bibliográfica | a mano, 25 entradas |
| 2 | Nombre de la carpeta en `referencias/` | a mano, 29 carpetas |
| 3 | Etiqueta visible de cada cita en el cuerpo | a mano, 87 pares distintos |

Con tres copias y ningún mecanismo de contraste, corregir una y olvidar otra
reproduce el error. De ahí que A3, A4 y A5 se contaminaran dos veces.

**Solución: la bibliografía manda, y un verificador la hace cumplir.** Se añadió
`verificar_referencias.py` en la raíz del vault. Extrae autor y año de cada entrada
y los contrasta contra la carpeta, contra la nota interna y contra los 187 enlaces
con etiqueta visible del cuerpo.

```bash
cd "boilerfree vault"
python3 verificar_referencias.py          # informe; salida 0 = coherente, 1 = divergencias
python3 verificar_referencias.py --fix    # aplica los renombres propuestos
```

**Qué detecta**

- Carpeta cuyo autor o año contradice a la entrada bibliográfica → imprime el
  nombre correcto exacto.
- Carpeta citada que no existe, o nota interna ausente.
- Enlace del cuerpo que no resuelve a ningún archivo.
- Etiqueta visible vacía, que en el texto renderizado deja una cita sin nombre.
- Carpeta sin citar y sin motivo registrado.

**Cómo se probó que funciona.** Un verificador sin prueba no vale nada, así que se
reprodujeron los errores sobre una copia desechable:

| Escenario reproducido | Resultado |
| --- | --- |
| Vault tal como está | **salida 0**, 25/25 entradas OK, 187 enlaces resueltos |
| Carpeta renombrada a mano, enlaces desactualizados | **salida 1**, detecta carpeta ausente |
| Carpeta y enlaces coherentes entre sí pero con el apellido equivocado (el caso exacto de A3) | **salida 1**, propone `Renombrar a: 'Karlsson 2024 - Exploring behaviours of RESTful APIs'` |
| El mismo caso, con `--fix` | Renombra la carpeta correctamente |

**Lo que el verificador NO hace**, y hay que saber: renombra la carpeta pero **no
actualiza los wikilinks**, porque eso exige tocar el texto de la tesis. Lo dice
explícitamente al terminar. El orden correcto de una corrección de autor es
siempre: **bibliografía → verificador → `mv` → actualizar enlaces → volver a pasar
el verificador.**

**Regla de herramientas (decidida por el autor, 2026-09-28):** **prohibido usar
scripts para aplicar texto.** Todo texto que se escribe o reemplaza en la tesis
lo compone y aplica el asistente con sus herramientas de edición, y **todo texto
debe pasar por el autor** antes de aplicarse. El verificador se usa solo para
leer estado (sin `--fix`), nunca para modificar la tesis.

**Carpetas que no son referencias de la tesis.** Declaradas en el propio script para
que no se confundan con un error: Deljouyi, Gravitee.io y Wohlin (fuera de alcance
acordado) y el artículo de Sotirov y Dimitrov, que se conserva a propósito con su
identidad real.

---

## ⬜ B. Lo que la tesis afirma y la fuente no dice — 9 atribuciones a 8 fuentes

> **Este bloque NO incluye el lote XBoot.** Las 24 atribuciones al artículo de
> Alkazemi y Nour son la decisión **D4**, más abajo. Aquí las fuentes son
> Evans, Trebejo, Fowler, Vasquez, Özkan, GitClear, Stack Overflow y Bobadilla.

| # | La tesis afirma | Qué dice la fuente | Estado |
| --- | --- | --- | --- |
| B1 | Evans advierte que el DDD completo «puede resultar pesada para proyectos pequeños» | Evans L1711: con un proyecto simple, «it will have been canceled». Su consejo (L1715) es **no usarlo**, no usarlo a medias | ✅ **Aplicado — L279, L333 (2026-09-28):** voz del autor; la advertencia citada ahora es la real de Evans (L1711: «difficult learning curve»), no la frase inventada |
| B2 | Evans prescribe un framework que encapsule los patrones tácticos del DDD | L8435: «**Back off restrictive frameworks in your CORE DOMAIN**». Y L219: su «framework» es **el libro** | ✅ **Aplicado — L279, L333, L433 (2026-09-28):** reformulado como **voz del autor**; la estructura del libro de Evans (táctica vs. estratégica) se menciona como hecho, no como prescripción de framework |
| B3 | Trebejo Loayza sostiene «DDD-liviano» y un framework en PHP | Tabla 4.1.1: **«C# con Net Core / Java \u2013 SpringBoot», Entorno Web: ASP.NET Core 6.0**, MVC, JQuery, MySQL/MariaDB, StarUML. El generador implementado es **`generator-springboot` (Yeoman \u2192 Spring Boot)**. `PHP`=3 (solo URLs), `reflex`=0, `inyecc`=0, `middleware`=0, `namespace`=0, `router`=0, `composer`=0, `CLI`=0. L1402-1404: «estratégico y táctico, **ambos deben combinarse**». Asume modelado UML (12) y validación con 10 profesionales | ✅ **Cerrado (2026-09-28)** — T1 aplicado (13 líneas); **L333** ya no dice que Trebejo «adopta la variante»; **L285, L435** definiciones como voz del autor, Trebejo como evidencia de viabilidad real (UML + Yeoman `generator-springboot` / Spring Boot, sin reflexión ni PHP) |
| B4 | Fowler define el boilerplate como «lo necesario para que funcione pero no expresa el dominio» | `boilerplate` sale **1 vez en 13.907 líneas**, de pasada, sobre el patrón *Two Step View*. Su término real es **plumbing** | ✅ Aplicado — L247, L445 |
| B5 | Vasquez Pari: el boilerplate es el 20 %–35 % del tiempo, correlación 0,72 | **Ninguna de las dos cifras existe.** `boilerplate` aparece **0 veces** en 1.897 líneas; tampoco existen el «40 %» (se le atribuyó en L115/L123) ni el «30 %» (atribuido a Chavez en L113/L123), ni los «35 % / 20 %» o «78 %» atribuidos a Pizarro (inventos) | ✅ **Cerrado (2026-09-28, pasada B5 completa)**: L113, L115, L123, L227 y L273 reformulados con lo que las fuentes sí dicen — Vasquez: 73,23 % reducción del esfuerzo por IA (30 proyectos; β=−82,73 min; IC95% −73,92/−72,53; p<0,001); Chavez: «un gran porcentaje del desarrollo es repetitivo… genera pérdidas de tiempo y dinero» (sin cifra); Pizarro: 9 h manual vs. 4 h con Copilot (55,6 % menos), +12,27 % líneas libres de errores (74,04→86,31 %), +78,38 % pruebas unitarias (50→100 %) |
| B6 | Özkan define boilerplate como controladores, DTOs y repositorios | `boiler`=0, `boilerplate`=0, `DTO`=0, `ontroller`=0, `CRUD`=0 | ✅ **Cerrado (2026-09-28, pasada completa de Özkan — 20 cambios)**: B6 parcial (L249, L445, L688) + 18 sitios con la misma atribución falsa en dimensiones, bases, glosario y metodología; ver lote abajo |
| B7 | GitClear advierte el duplicado «en scaffolding» | `scaffold`=0. Su hallazgo fuerte es el *code churn* (Pearson 0,98), no el copy/paste | ✅ Aplicado — L401 |
| B8 | Stack Overflow define `Scaffolding` como andamio de código | Aparece 2 veces y ambas son «the **DevRel** scaffolding»: estructura de *roles*, no código | ✅ Aplicado — L401 |
| B9 | Bobadilla Chara trabaja con Spring y Composer | `Spring`=0, `Composer`=0. Usa **Go + ReactJS** | ✅ Aplicado — L325 |

B4, B6, B7, B8 y B9 se corrigen borrando la atribución falsa y diciendo lo que la
fuente sí dice. **B1, B2, B3 y B5 no se pueden corregir sin decidir antes** — ver
el último bloque.

**Aplicado el 2026-09-28 — 8 sitios en 6 líneas.** B4 (L247, L445): Fowler no
define «código boilerplate» (su única aparición es de pasada, en Two Step
View); su término es *plumbing*. B6 (L249, L445, L688): Özkan no menciona
boilerplate/DTO/controller/CRUD; su SLR se centra en desafíos de implementación
y efectividad. B7 (L401): GitClear no dice «en scaffolding» — su hallazgo es el
duplicado + *code churn*. B8 (L401): SO no define el término; única mención
«the DevRel scaffolding» (roles), y se conserva el 63 % de deuda técnica
(verificado en E). B9 (L325): Bobadilla no usa Composer ni Spring; su framework
es **Go + ReactJS** (los 21 «PHP» de su PDF son el ERP legado de la UCSM, no el
framework). **Queda congelada** en L325 la cláusula «Trebejo Loayza (2023) lo
describe…» sobre Composer en ecosistema PHP: pertenece a **B3**.

**Lote completo de Özkan aplicado el 2026-09-28 — 20 cambios en 18 líneas.**
La fuente real de Özkan: `boilerplate`=0, `controller`=0, `DTO`=0, `CRUD`=0,
`repository`=1 (solo «repository mining», no el patrón). Lo que sí dice: 36
estudios, DDD prominente en microservicios, faltan evaluaciones empíricas
(abstract; L1504), DDD «mejora la calidad del código, potencia la construcción y
proporciona soluciones más completas para el modelado del dominio y la
generación de software» (L614-616, base de L153 y L195, intactas), agregados
«encapsulan entidades, objetos de valor y lógica de dominio; puntos principales
de acceso y modificación de datos» (L134-139), Ubiquitous Language «captura
términos técnicos y específicos del dominio» (L137-138), oportunidad O3
«Increasing tool support (e.g., DSLs, context-mapping tools)» (L1083). Sitios
reformulados: **L255** (cabecera sin Özkan + Vasquez corregido: compara grupos
con/sin IA, no «mide porcentaje de tiempo»), **L265, L287** (cabecera +
cuerpo), **L293, L301** (agregado: ahora describe lo real de Özkan),
**L315, L323** (CRUD: cita fabricada eliminada → voz de la tesis), **L327**
(DDD: cita fabricada «se necesitan más herramientas…» → conclusión real +
O3), **L333** (DTO → voz de la tesis), **L363** (Lenguaje Ubicado: «paso
previo indispensable» → descripción real), **L387** (Repositorio → voz de la
tesis), **L397** (Servicio de Dominio: «genera boilerplate» → «lo listan entre
los conceptos tácticos»), **L409** (Value Object: «autogeneración de DTOs» →
«atributos conceptuales sin identidad»), **L447** (criterio de caracterización
propio + Vasquez como apoyo), **L457** (L465 original: «tal como lo metodizan»
→ «diseño experimental de medición pre-test definido en la presente
investigación»), **L465** (validación: «que Özkan y Alkazemi consideran
relevante» → necesidad real de Özkan + esquema de validación con XBoot y 10
estudiantes), **L489** (población: «caracterizan como prioritario» → voz de la
tesis, Vasquez documenta el problema), **L535** (Fase 1: criterio propio).
Intactas por verificadas: L153, L195, L247, L437, L559. **25 menciones → 13**
(las demás borradas con las atribuciones falsas).

**Lote T1 de Trebejo aplicado el 2026-09-28 — 13 líneas (12 sitios).** El núcleo
del hallazgo: la hoja había resumido mal la evidencia de B3. El PDF real de
Trebejo declara **«C# con Net Core / Java \u2013 SpringBoot»** (tabla 4.1.1) y el
generador que implementó es **`generator-springboot` (Yeoman \u2192 Spring Boot)**;
**no** es «solo C#/.NET» como decía esta fila, y tampoco se sostiene ninguna
atribución de reflexión, DI, middleware, namespace, router, Composer, PHP o
migraciones de BD (todas 0 apariciones; `migración` en su PDF significa «migración
de sistemas legados»). Sitios corregidos (método D4: borrar la atribución falsa,
decir lo que la fuente sí dice): **L117** (no existe la «replicación manual de
patrones»; su conclusión real es reducir el esfuerzo de diseño: 26,5 min por
participante vs. horas, y facilitar la migración de legados), **L219** (no hay
«DSL basado en UML» ni «70 %» ni «contexto peruano»; su modelado es UML/StarUML y
el generador es Yeoman/Spring Boot), **L313** (no usa «backend»), **L323** (su
herramienta es una aplicación web, no CLI), **L325** (no menciona Composer: su
pila es C#/.NET o Java/Spring Boot), **L355** (no menciona DI), **L375** (no
menciona middleware), **L377** (sus «migraciones» = sistemas legados, no BD),
**L381** (no usa namespace), **L385** (no escoge PHP como ecosistema; la línea
huérfana «masiva adopción regional…» se absorbió), **L391** (no usa reflexión; su
mecanismo es modelado UML + Yeoman) y **L397** (no usa router).

**T2 de Trebejo ✅ CERRADA (2026-09-28):** **L285 ✅**: la
definición de framework de autogeneración es voz del autor y Trebejo se cita
como evidencia de viabilidad real (herramienta web, modelado UML + Yeoman
`generator-springboot` / Spring Boot; sin «técnicas de reflexión» ni
«ecosistema PHP»). **L435 (antes L439) ✅**: la definición del framework
"DDD-liviano con autogeneración de endpoints" pasó a ser voz del autor y la
atribución entre paréntesis a Trebejo se reemplazó por respaldo de viabilidad
con su mecanismo real. **L333 ✅**: ya no dice que Trebejo «adopta la variante»
ni que Evans prescribió el framework; la cita real de Trebejo (L1402-1404:
«estratégico y táctico, ambos deben combinarse») se usa como evidencia de la
distinción, y el resto es voz del autor anclada en fuentes (Evans L1711,
Alkazemi «lightweight framework»). **L279 y L433 ✅**: segunda y tercera
aparición del defecto B1/B2 (Evans «define un framework de dominio» y
«una implementación completa puede resultar pesada») — halladas en la pasada de
L285; reformuladas como voz del autor. La decisión **D1** confirma que
«DDD-liviano» es **propuesta del autor** con el uso del dominio de Evans como
punto de partida: todos los sitios reformulados como voz del autor, sin
atribuir el concepto a Trebejo ni a Evans.

---

## ✅ E. Atribuciones y metadatos — CERRADO

Agrupó la verificación de las 25 entradas contra el papel y la corrección de todo
lo que no coincidía. **29 correcciones** (15 en la bibliografía visible, 14 en el
cuerpo). Regla aplicada: **el papel manda** sobre el nombre del archivo.

### Nombres y autores

| Entrada | Corrección | Evidencia |
|---|---|---|
| Cosme Escalera | `Quispe Cansaya, V.` → `D. D.` | portada: `Bach. DIEGO DEYVIS QUISPE CANSAYA` |
| Chavez y Wong | `Chavez, A., & Wong, L.` → `Chavez Chavez, A., & Wong Portillo, L.` | `Alvaro Chavez Chavez, Lenis Wong Portillo`. **Carpeta → `Chavez Chavez 2022 - EasyRest` (2026-09-28)** |
| Campos Salcedo | `Reyes-Huamán, M.` → `Reyes Huamán, M.` | `Marlene Reyes Huamán`, sin guion |
| GitClear | autor corporativo → `Harding, W., & Kloster, M.`; título `Suggests` → `Shows` | `William Harding` (Alloy.dev), `Matthew Kloster` (GitClear). **Carpeta → `Harding 2024 - Coding on Copilot` (2026-09-28)** |
| McKinsey | autor corporativo → `Gnanasambandam, C., Harrysson, M., Hussin, A., Keovichit, J., & Srivastava, S.` | `This article is a collaborative effort by…`. **Carpeta → `Gnanasambandam 2023 - …` (2026-09-28)** |
| Peldszus | affiliation inventada → 4 reales | `Paderborn` = 0 apariciones |

### Metadatos

- **Chavez**: páginas `28-34` → **`25-35`**. El PDF tiene 11 páginas desde la 25 y su
  propia autocita dice `4(1):25-35`. El `4(1):25-36` del encabezado es un typo de la
  revista. *(El rango estaba garbleado en el `.md` como `25-3365`; el PDF lo resolvió.)*
- **Jones**: añadido `(RFC 7519)` e `Internet Engineering Task Force`.
- **Sadik**: añadido `arXiv:2310.04304`; era `Honda… (Preprint)` vía ResearchGate.
- **Özkan**: `En … (Vol. 230, p. 112537). Elsevier.` → `*Journal of Systems and
  Software*, *230*, Article 112537.` — 112537 es **número de artículo**, no páginas;
  además `En` es la preposición española dentro de una referencia en inglés.
- **Editorial repetido como autor** (APA 6.1): eliminado en Stack Overflow ×2. En
  GitClear y McKinsey **se resolvió solo** al pasar a los autores nominales.

### Tipo de trabajo — 4 de 6 tesis mal etiquetadas

`Master's Thesis` → descriptor real: Bobadilla Chara y Pizarro Romero y Cosme
Escalera a **`[Tesis de grado, …]`**; Villanueva Campos a
**`[Trabajo de investigación, …]`** (es bachillerato en Administración).
Trebejo y Vasquez **se quedan** como `Master's Thesis` — su portada sí dice
`Grado Académico de Magíster` y `GRADO DE MAESTRO`.

El cuerpo repetía el error y se corrigió en los 3 sitios: `tesis de maestría` →
`tesis de grado` (Bobadilla, Pizarro, Cosme Escalera).

### Cifras del cuerpo

- **L107 y L401 — el 63 % y el 62,4 %** son de poblaciones distintas y ambos son
  correctos: `Technical debt is the top frustration at work for professional
  developers according to 63% of respondents` y `| Amount of technical debt | 62.4% |`
  (All Respondents). L401 mezclaba el número de una con la etiqueta de la otra → corregido.
- **L395 — el 82 %** es de **2017** sobre 18.400 APIs, no «al 2022» (24.471 APIs).
- **L351 — el «protocolo base»** entrecomillado a Karlsson es una cita fabricada:
  `protocol` aparece 0 veces en su artículo. Sustituida por lo que sí dice.
- **El «20 %–35 %» de Vasquez y el «>80 %» de Alkazemi no existían** — 6 sitios
  (L231, L251, L253, L267, L269, L295, L317, L445, L688). Reemplazados por lo que las
  fuentes sí sostienen: Vasquez es un **diseño longitudinal de 30 proyectos en una
  empresa de Trujillo**, 15 sin IA y 15 con IA, con una reducción del esfuerzo del
  **73,23 %** (β = −82,73 min; IC95% −73,92/−72,53; p<0,001), no una boilershare.
  Alkazemi: **menos de 50 líneas de DSL → 950–1.350 líneas** de Java y HTML, y
  despliegue en **2–20 min (≈7)** frente a **45–120 min** manual.
- **L231 «encuestas a 45 desarrolladores»** era inventado (el 45 del PDF era un folio
  de página). La metodología real es correlacional longitudinal con muestra
  intencional de 30 proyectos.

### C3 de la hoja de ruta — RECHAZADO, habría empeorado la entrada

La hoja proponía sustituir el autor corporativo de DORA por «DeBellis, Storer,
Lewis y Good». **El PDF lo desmiente**: esos cuatro aparecen bajo el encabezado
**«Equipo del informe DORA»**, una lista de más de 25 personas. La sección
«Autores» es otra cosa, con biografías. Sustituir un autor corporativo por 4 de
25 miembros del equipo habría sido un error nuevo. **La entrada actual se queda.**

### Límites de verificación que quedan declarados

- **Evans**: el archivo es el *Final Manuscript*, que no nombra a Addison-Wesley. La
  editorial es correcta en realidad pero **no es verificable contra el archivo**.
- **Levezinho**: el propio paper trae su bloque `ACM Reference Format` roto, con un
  DOI placeholder (`10.1145/nnnnnnn.nnnnnnn`) y `Proceedings of (arXiv)`. Ahí el
  `arXiv:2407.02512` de la tesis es **más preciso que la autocita del paper**. No se toca.
- **DORA**: no se halló declaración de copyright en el PDF, así que la afirmación
  «copyright de Google LLC» **no se puede confirmar** y no se cambió.

---

## ✅ C. Metadatos de la bibliografía — CERRADO

- **C1** Cuatro tesis marcadas `Master's Thesis` que **no son maestría**. ✅
  **Aplicado en el bloque E, 5 de 6:** Bobadilla Chara, Cosme Escalera y Pizarro
  Romero → `[Tesis de grado]`; Villanueva Campos → `[Trabajo de investigación]`.
  Trebejo y Vasquez **se quedan** como `Master's Thesis` (son maestría de verdad).

  ✅ **Y el lugar, en los dos sitios donde aparecía.** Decisión del usuario
  (2026-09-28): **localidad con región**, `Pimentel, Lambayeque`, tanto en el
  cuerpo (L121) como en la bibliografía (L1019). Solo con la localidad se perdía
  la región, que sí viene de la portada; solo con la región se perdía la localidad,
  que es la que el PDF declara.

  *Evidencia:* el PDF imprime «Pimentel – Perú» en la portada y «Pimentel, 10 de
  Julio del 2024» en la línea de firma. `Lambayeque` **no aparece ni una vez** como
  lugar. `Chiclayo` sí aparece 15 veces, pero es la ciudad donde opera la empresa
  estudiada, no la sede de la institución.

  *Lo que casi se escapa:* el error estaba en **dos** sitios, no en uno. El cuerpo
  decía «Villanueva Campos (2024) en la Universidad Señor de Sipán en Lambayeque»
  con la misma firma equivocada, tomándola de la portada de la fuente. Corregir
  solo la bibliografía habría dejado al juez leyendo «Pimentel» a tres líneas de
  distancia de «Lambayeque».
- **C2** Chavez y Wong: páginas `28-34` → **`25-35`**. ✅ RESUELTO en el bloque E.
- **C3** DORA: **propuesta rechazada** — los cuatro nombres son del «Equipo del
  informe DORA» (25+ personas), no autores. La entrada corporativa se queda. Ver
  el bloque E.
- **C4** GitClear y McKinsey: autor corporativo en lugar de los autores nominales
  (Harding y Kloster; Gnanasambandam, Harrysson, Hussin, Keovichit y Srivastava).
  ✅ RESUELTO en el bloque E.
- **C5** Jones: falta `RFC 7519` e `Internet Engineering Task Force`, que es
  justamente lo que identifica una RFC. ✅ RESUELTO en el bloque E.
- **C6** Özkan: construcción híbrida `En … (Vol. 230, p. 112537)`. 112537 es un
  **número de artículo**, no páginas, y falta el `The` del nombre oficial.
  ✅ RESUELTO en el bloque E, salvo el `The`: el PDF imprime `Journal of Systems
  and Software` **sin** «The», así que la hoja se equivocaba también en eso.
- **C7** Identificadores. ✅ **Resuelto en su parte verificable.** Leyendo el sello
  de la página 1 de cada PDF: `arXiv:2603.16975` (Gurgul), `arXiv:2407.02512`
  (Levezinho), `arXiv:2302.06590` (Peng) y `arXiv:2310.04304` (Sadik) — **los tres
  que la hoja marcaba estaban bien**. El defecto real era otro y no estaba en la
  lista: **Peldszus no tenía arXiv**, ahora `arXiv:2601.16705` añadido.
  ✅ **Los 5 handles `hdl.handle.net` se dejan tal cual — decisión del usuario
  (2026-09-28): los descended de los repositorios de cada universidad.** No 9:
  son 5 distintos, cada uno aparece dos veces (URL desnuda + destino del enlace).

  *Contexto para quien lo lea después:* un handle lo asigna el repositorio al
  subir la tesis y **no aparece en el PDF impreso** — el PDF muestra la URL del
  repositorio, que es otro sistema. Por eso no se podían verificar leyendo el
  vault. Crucce de todos modos el prefijo contra la evidencia del propio vault:
  `20.500.12802` = USS, lo que confirma el de Villanueva Campos; los otros cuatro
  prefijos no aparecen en ningún otro archivo, así que no había con qué cruzarlos.
  **No se hizo ninguna consulta de red.**

**No tocar, aunque parezcan errores:** Fowler muestra `2003` en el CIP de la
Library of Congress y en el copyright, pero se publicó en **2002**. Özkan muestra
recepción en 2024 y publicación en **2025**. Ambos están bien.

---

## ✅ D. Formato — CERRADO

*Los items de este bloque se numeran **F1–F4**, no D1–D4: la serie D está tomada por
las decisiones de la sección siguiente, y usar los mismos números para cosas
distintas fue la causa de una confusión en esta hoja.*

- **F1** L989 empieza con `##` y Obsidian lo lee como encabezado: se traga el
  **lugar** de la entrada de Pizarro Romero. ✅ RESUELTO.
- **F2** L1015 empieza con `##` y se traga la **institución y el lugar** de la
  entrada de Vasquez Pari. ✅ RESUELTO.
- **F3** URL partida a mitad de enlace en dos entradas: GitClear (L897-899) y
  McKinsey (L947-951). El enlace apunta a una dirección truncada y el resto queda
  como texto suelto, con un `_` que abre cursiva sin cerrar. ✅ RESUELTO — ambas
  URLs unidas en una sola línea, con corchetes balanceados.
- **F4** Las cinco entradas de autor corporativo repiten el mismo nombre como autor
  y como editorial. ✅ RESUELTO — Stack Overflow ×2 por eliminación del repetido;
  **GitClear y McKinsey se resolvieron solos** al pasar a los autores nominales
  (Harding y Kloster / Gnanasambandam et al.), porque el nombre corporativo pasó a
  ser editorial y no autor. **DORA se queda**: `DORA & Google Cloud` como autor y
  `DevOps Research and Assessment (DORA)` como editorial no son la misma cadena,
  y la hoja no recomienda cambiarla (ver el bloque E).

---

## Lo que ya se hizo (reversible)

Renombres en `boilerfree vault/referencias/`. **No se borró nada**: el artículo de
inmunología se conservó, renombrado para que no se pueda citar por error.

| Antes | Después |
| --- | --- |
| `Larsson 2024 - Exploring behaviours of RESTful APIs` | `Karlsson 2024 - Exploring behaviours of RESTful APIs` |
| `Cosme Escalera 2022 - Arquitectura de microservicios Group de mercado` | `Cosme Escalera 2024 - …` |
| `Gurgul et al. - 2026 - The State of Generative AI….md` | `Gurgul Gubela y Lessmann - 2026 - ….md` |
| `applsci-15-04123.md/.pdf` | `Sotirov y Dimitrov - 2025 - In Silico Methods….md` |
| *(carpeta nueva)* | `Alkazemi 2025 - XBoot/` con el PDF real de XBoot |

Los `.pdf` conservan el nombre viejo; solo se renombraron los `.md`. Para
revertir, deshaciendo el cambio con esta tabla.

**Pendiente de sincronizar:** los wikilinks de la bibliografía y del cuerpo que
apuntan a estas cuatro rutas quedaron apuntando a nombres que ya no existen. Hay
que actualizarlos en el mismo cambio.

---

## Las cuatro decisiones que bloquean el resto

> *Los `D1`–`D4` de esta sección son **decisiones de contenido**. No tienen nada que ver
> con los items `F1`–`F4` del bloque de formato, que se renumeraron para que no se
> confundan.*

Estas no son erratas. Son el fundamento de la tesis, y corregirlas cambia **lo que
la tesis afirma**. Afectan a [[DDD-liviano]] y a [[Código boilerplate y scaffolding]].

### D1 — ¿De dónde sale «DDD-liviano»? — RESUELTA POR EL AUTOR (2026-09-28)

El autor confirma: **«DDD-liviano es mi propuesta. De Evans vi el uso de dominio,
y solo estoy tomando eso como punto de partida.»** Es propuesta de la
investigación, no atribución externa. Evans no lo dice (B1, B2) y Trebejo dice
lo contrario (B3). El artículo de XBoot se describe a sí mismo como «a
*lightweight framework*» con DSL, pero el término de la tesis es **decisión
propia del autor**.

- ✅ **Decisión:** presentarlo como propuesta propia, con el dominio de Evans
  como punto de partida, sin atribuir el término «liviano» a Evans ni a Trebejo.
  Desbloquea **B1, B2, B3-T2 (L285, L333, L439)**.
- Reatribuirlo a Alkazemi y Nour (2025) — descartado: es del autor, no de XBoot.
- Mantener a Evans con una salvedad de que él advierte en contra — opcional,
  según redacción final.

### D2 — ¿Cómo se reformula la definición de boilerplate? — RESUELTA POR EL AUTOR (2026-09-28)

El autor confirma: **«Las definiciones de boilerplate salen de una combinación
de conceptos de varios autores.»** Es síntesis propia de la investigación, no
una definición literal de una sola fuente. Fowler no la define (B4); la
definición de la tesis combina conceptos de varias fuentes.

- ✅ **Decisión:** mantener la definición como **síntesis propia** de la
  combinación de conceptos de varios autores; no atribuir a Fowler literalmente.
  Desbloquea **B5** (sin cifras inventadas — D3).
- ✅ **Ejecutado (2026-09-28):** la pasada B5 reformuló L113, L115, L123, L227 y
  L273, eliminando además inventos no registrados en la hoja (40 % de Vasquez,
  30 % de Chavez, 35 %/20 % y 78 % de Pizarro).

### D3 — ¿De dónde sale el «20 %–35 %» de la dimensión D1? — RESUELTO SIN CIFRA

La dimensión D1 necesitaba una cifra del peso del boilerplate y ninguna fuente del
vault la tiene. **No se conserva ninguna cifra: se eliminó.** La cifra se sustituyó
por lo que las fuentes sí sostienen —Vasquez: 73,23 % de reducción del esfuerzo por
IA, que es otra magnitud; Alkazemi: 950–1.350 líneas desde 50 de DSL— y la
definición conceptual de D1 se apoya ahora en Özkan (replicación de
controladores, DTOs y repositorios), que sí es una fuente directa del fenómeno.

La dimensión conserva su indicador propio (LOC por componente, ficha de análisis,
SonarQube/PMD), así que **la operacionalización no se queda sin sustento**: lo que
se perdió es el número de contexto, no la medida.

### D4 — ¿Se rehace el lote XBoot? — YA ES POSIBLE

Las 16 atribuciones a «Alqahtani» se verificaron contra el artículo equivocado.
*(Eran 16 en el momento de detectarlo. Hoy el cuerpo tiene **24 sitios** enlazando a
XBoot, tras el renumerado de autores del bloque A.)*

El PDF real ya está en el vault y su `.md` fue extraído (21.053 palabras), así que
rehacerlas ya no depende de ninguna descarga.

**Hallazgo que cambia el panorama:** el artículo real menciona **boilerplate 26
veces** y se describe a sí mismo como «a *lightweight framework*». Es decir, la
fuente que hasta ahora llevaba el nombre equivocado sí sostiene el vocabulario
que la tesis le atribuía a otros autores. Eso afecta directamente a **D1 y D2**.

**APLICADO — 28 de septiembre de 2026.** Las 24 atribuciones se cotejaron contra el
artículo real. Veredicto: las cifras están bien citadas en todas partes; lo
inventado es la **mecánica** (DTOs, mappers, middleware, CLI, DI, análisis
estático, estadística) — artefactos de la propia investigación proyectados sobre
él. Se corrigieron **18 sitios**: 15 atribuciones falsas reemplazadas por lo que el
artículo sí dice (o cláusula eliminada) y 3 matices (L253 sin «DTOs»; L259 acotado a
los dos casos de estudio; L473 «indispensable» → «consideran relevante»). Los 6
sitios verificados (L205, L269, L335, L413, L445, L567) quedaron intactos.
Integridad: 1.032 líneas, **261 wikilinks (−6**: 5 retirados con las citas falsas
de Alkazemi + 1 de Pizarro en L561), 0 destinos rotos, `tesis.bak` intacto.

> ⚠️ ~~**Observación fuera de alcance (no tocada):** L465 «tal como lo metodizan
> [[Özkan…]] et al. (2025)» padece el mismo patrón, pero atribuido a **Özkan**, no a
> Alkazemi — quedó fuera del lote D4 y debe revisarse en una pasada sobre las
> atribuciones a Özkan.~~ **RESUELTA (2026-09-28): pasada completa de atribuciones
> a Özkan ejecutada — 20 cambios en 18 líneas**, ver lote en la sección B6.

---

## ✅ Pasada final (segunda revisión manual completa) — CERRADA (2026-09-28)

Última pasada manual sin scripts sobre atribuciones restantes: **22 hallazgos
aprobados por el autor y aplicados con `edit` (26 ediciones)** + 2 pendientes
opcionales sin aprobar.

### Bloque A — atribuciones falsas (9)

| # | Sitio | Qué se corrigió | Evidencia de la fuente |
| --- | --- | --- | --- |
| A1 | L353 IoC | Fowler y Pizarro **no emplean «inversión de control»** (`inversion`=0 en Fowler; IoC/inversión=0 en Pizarro); la frase «invierten el trabajo mecánico» era fabricada → definición técnica propia, DI de Spring Boot como implementación, sin atribución externa | greps 0/0 |
| A2 | L105 + L303 + L389 Karlsson | «la forma más común… directrices arquitectónicas REST» y la cita p. 1288 **no son textuales** → traducción fiel de L26-27: «la tecnología web es un medio común… usualmente siguiendo el estilo arquitectónico REST (Fielding, 2000)»; se quita la página de cita (1288 = primera página del artículo, journal 32:1287–1324) | Karlsson L26-27 |
| A3 | L389 REST | «la directriz arquitectónica dominante» **es de Peldszus** (L51: «REST is the dominant architectural style for delivering web services»), no de Karlsson → frase movida a Peldszus | Peldszus L51 |
| A4 | L279 + L343 + L429-431 Fowler | «conjunto de clases que colaboran…» y «que automatiza las tareas repetitivas…» **no existen en Fowler** → voz de la tesis anclada en el término real *plumbing* (L11883) | Fowler L11883 |
| A5 | L313 | Fowler «compara con la plomería de una casa» — **no existe**; Fowler solo usa *plumbing* 1 vez, sin metáfora → metáfora como voz de la tesis equivalente al término inglés (alineada con L437) | Fowler L11883 |
| A6 | L113 Campos Salcedo | «lógica sepultada bajo capas de código redundante» **0 matches** (paper = gestión del conocimiento con SECI) → se describe el contenido real (KM, capturar/organizar/compartir conocimiento) | Campos 0 matches código/redundante/trazabilidad/mantenibilidad |
| A7 | L117-119 + L221 Bobadilla | «estandarización de controladores, servicios y repositorios» y «deuda técnica» **no aparecen** (la única «deuda» del PDF es económica, BBVA L1998); el framework fue la **refactorización del ERP inmantenible** de la UCSM (L61) → reformulado con mantenibilidad real, Go + ReactJS | Bobadilla L61, L98, L252 |
| A8 | L121 + L233 Cosme | «tiempos de despliegue» / «juicio de expertos» / «estandarización disminuye la complejidad» / «generación automática de infraestructura» **no aparecen** → conclusiones reales L232-238: microservicios + Kubernetes mejoran un **100 %** rendimiento, disponibilidad y tiempo de respuesta vs. monolíticos; empresa Group de Mercado (Juliaca); metodología XP/BPMN/Vue.js/JWT/PHP | Cosme L225-238 |
| A9 | L407 Validación | Pizarro **no usa «boilerplate» (0 matches)** ni habla de «tareas estructurales» → atribución eliminada; quedó la parte Alkazemi reformulada (ver B13) | Pizarro 0 «boilerplate» |

### Bloque B — matices (13)

| # | Sitio | Corrección |
| --- | --- | --- |
| B1 | L107 Peldszus | «repetición de patrones estructurales predecibles… principal factor» y «cada una replica las mismas estructuras» **no son textuales** (el PDF habla de *inconsistent naming or usage*, L53) → lo textual (62 %, 11-100 ops, usabilidad afectada por inconsistencia) a Peldszus; la interpretación de duplicación estructural pasa a voz de la tesis |
| B2 | L107 Gnanasambandam | «tareas tediosas y poco satisfactorias» → «tareas necesarias pero generalmente poco satisfactorias» (*generally unsatisfying chores*, L286-287); «comprise» → «comprende»; «no generador de valor» suavizado a «bajo valor añadido» |
| B3 | L111 Peng | 55 % → **55,8 %** (L15/L27), en la tarea de **implementar un servidor HTTP en JavaScript** |
| B4 | L113 Chavez | enumeración «—controladores, servicios y repositorios—» → la real del PDF (L50-56): «operaciones CRUD, generación de reportes, búsquedas típicas en una BD, Test Unitarios, configuraciones» |
| B5 | L199 Gurgul | «entropía de código» **no es de Gurgul** → «adopción acrítica, erosión de habilidades y acumulación de deuda técnica» (L21/L117) |
| B6 | L359 Jones | RFC 7519 dice «a **compact claims representation format**» (L220), no «canónico… en entornos REST» → corregido, uso en esta investigación como voz de la tesis |
| B7 | L245 + L265 Fowler | «getters/setters» **no aparece en PEAA** → la evidencia real L1625-1627: mapeo repetitivo evitable con *Metadata Mapping* (generación de código o programación reflexiva) — además sustenta el framework por reflexión |
| B8 | L323 CRUD | Pizarro compara **3 proyectos completos** (L457), no usa el CRUD como «unidad de comparación» (solo lo menciona en la API del Proyecto 1, L2410) |
| B9 | L401-403 URI | «unidad de direccionamiento canónica» atribuida sin respaldo (Peldszus: *HTTP endpoints*; Karlsson: *operations/behaviours*) → voz de la tesis, con la identificación de endpoints como operaciones HTTP de las fuentes |
| B10 | L251 + L281 + L431 Alkazemi | lista «(…, repositorios, …)» inconsistente con D4 (artefactos reales L20-22/L87-88: entidades, servicios, controladores, plantillas) → unificada + «capa de acceso a datos resuelta mediante anotaciones como @Repository» (L64) |
| B11 | L387 Evans | cita entre comillas «aislar el modelo…» **no es textual** (la cercana L1628 es sobre capas) → paráfrasis sin comillas con la definición canónica del patrón (encapsula almacenamiento, recuperación y búsqueda) |
| B12 | L487 Población | «Siguiendo la definición técnica aplicada… por Pizarro» — la definición formulada **no es de Pizarro** (su población real = proyectos de una empresa limeña, L1053-1059) → voz de la tesis + contraste con la población de Pizarro |
| B13 | L407 Alkazemi (con A9) | «dentro de las entidades generadas» → se **define en el DSL** (L22/L86) y XBoot la materializa en el código producido |

### Verificados ✅ en esta pasada (sin cambios)

Gurgul (65 devs, >70 %, 79 %), Levezinho (Mono2Micro), Sadik (UML→Java/Python),
Ma (interrupciones), Chavez (gran porcentaje + pérdidas + JSON de salida), Jones
(claims), Karlsson (CRUD/HTTP methods L197/L216-217), Pizarro (9h→4h,
(9−4)×9/100 = 55,6 %), Stack Overflow 2025 (66 % «almost right»), Peldszus (cifras
+ «dominant», ya asignada), Gnanasambandam (70 % + outer loop), Bobadilla
(Go/ReactJS), Cosme (conclusión real), Trebejo (26,5 min), Vasquez (73,23 %).

### Pendientes opcionales — APLICADOS (2026-09-28, aprobados por el autor)

1. **L337 Endpoint — «unidades de interacción»**: la frase no era textual en
   Karlsson; su concepto central es *behaviour* («what an API should or should not
   do», L103). ✅ Reformulado: «las operaciones (*behaviours*) que una API expone
   —lo que la API debe o no debe hacer— mediante interacciones HTTP».
2. **L107 Ma — paráfrasis**: Ma estudia interrupciones **externas** (on-screen /
   in-person); «las tareas mecánicas interrumpen el flujo» era interpretación de
   la tesis. ✅ Reformulado: las interrupciones externas afectan el flujo (texto
   real de Ma) y la extensión al código estructural queda como voz de la tesis.

### Verificación de la pasada

- Verificador read-only: **25/25 OK** (los 2 avisos son identidades viejas de PDF
  ya acordadas: Gnanasambandam/McKinsey, Harding/GitClear).
- `tesis.bak` intacto: `862a0580bbdeacc492aff57cbe34edfb`.
- 0 apariciones de los términos falsos corregidos (salvo «entropía de código» en
  L109, que es de Harding/GitClear — correcto).

---

## Orden sugerido de ataque

### Ya hecho

1. ~~**A**~~ — integridad de fuente. Sin esto, cualquier corrección posterior podía
   apoyarse en el documento equivocado.
2. ~~**D**~~ — formato. Barato, sin decisiones, y sanea el outline de Obsidian.
3. ~~**C**~~ — metadatos. Datos puros, con la fuente a la vista.
4. ~~**E**~~ — atribuciones y metadatos de las entradas.

### Lo que queda, en orden

5. **D4** — rehacer el lote XBoot contra el PDF real. *Es lo que más valor da: no es
   una errata, es el artículo que de verdad sostiene el vocabulario de la tesis, y de
   él dependen 24 atribuciones del cuerpo.*
6. ~~**B4, B6, B7, B8 y B9**~~ — atribuciones corregidas borrando lo falso
   (2026-09-28, 8 sitios). B5 sigue congelado con B1, B2 y B3.
6b. ~~**T1 Trebejo**~~ — 12 sitios de atribuciones falsas corregidos (2026-09-28,
   L117, L219, L313, L323, L325, L355, L375, L377, L381, L385, L391, L397);
   evidencia de B3 corregida en la hoja (no es «solo C#/.NET»: pila declarada
   C#/.NET **o** Java-SpringBoot, generador implementado Yeoman/Spring Boot).
7. ~~**D1 y D2**~~ — decisiones de contenido resueltas por el autor (2026-09-28);
   B1, B2, B5 y T2 Trebejo aplicados. (D3 resuelta: no se conserva ninguna cifra
   inventada.)
8. ~~**Pasada final**~~ — segunda revisión manual completa de atribuciones
   restantes, aprobada y aplicada (2026-09-28, 26 ediciones A1–A9 + B1–B13; ver
   sección «✅ Pasada final»). Pendientes L337 Endpoint y L107 Ma **aplicados**
   (2026-09-28). **Lote completo cerrado.**
