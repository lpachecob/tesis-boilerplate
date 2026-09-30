# Corrección de estilo y APA 7 — tesis_boilerplate.md

## Objetivo
Corregir el cuerpo de la tesis para cumplir APA 7 en citas y referencias, y
eliminar las inconsistencias de estilo del escrito. Trabajo manual: cada
reemplazo decidido por lectura directa, sin scripts de corrección masiva.

## Alcance autorizado
- `tesis_boilerplate.md` — cuerpo (cap. I a V) y lista de referencias
- Añadir entrada de Fielding (2000) a la lista V
- Ordenar la lista V alfabéticamente
- Eliminar primera persona y unificar comillas y convención numérica

Fuera de alcance: portada, índice, maquetación de Word, contenido de la
bibliografía `referencias/` del vault.

## Tareas — estado

### APA (T1–T9)
- [x] T1 `et al.` en obras de 2 autores → `Alkazemi y Nour` / `Alkazemi & Nour` (21 sitios)
- [x] T2 `&` → `y` en citas narrativas (13 sitios; se conservó la parentética de L241)
- [x] T3 Coma eliminada antes de `(año)` en cita narrativa — `Chavez y Wong (2022)`
- [x] T4 Autorías incompletas — `Cosme Escalera y Quispe Cansaya (2024)`, `Chavez Chavez y Wong Portillo (2022)`, `Reyes Huamán`
- [x] T5 Fielding (2000) añadido a la lista V (estaba citado sin entrada)
- [x] T6 Lista V reordenada alfabéticamente (Gnanasambandam, Stack Overflow ×2 movidos)
- [x] T7 Títulos a sentence case en lista V y en las 11 citas de antecedentes
- [x] T8 Rangos de página con raya (53–64, 25–35, 1–12, 1287–1324)
- [x] T9 Números de página en las citas textuales — resuelto:
      `Trebejo Loayza (p. 57)`, `Alkazemi y Nour (p. 1)`, `Peldszus et al. (p. 1)`;
      cita de Evans reformulada como subtítulo (no era textual);
      Gnanasambandam y Stack Overflow 2024/2025: preprints/encuestas web sin paginación
      o traducción con original al lado — sin página inventada

### Estilo del escrito (T10–T19)
- [x] T10 Convención numérica: `24.471`, `1.350` (era `1350`)
- [x] T11 `IC95%` → `IC 95 %` (7 sitios) y espacio antes de `%` (5 sitios)
- [x] T12 Comillas unificadas en angulares «» (30 casos, 3 convenciones distintas)
- [x] T13 Primera persona eliminada del marco teórico (10 sitios)
- [x] T14 Concordancia con sujeto plural (Alkazemi, Cosme Escalera, Özkan)
- [x] T15 ~~Leísmos~~ — **descartado**, eran pronombre objeto directo legítimo
- [x] T16 Negritas: partidas y fragmentadas unidas, densidad de 1.1 reducida
- [x] T17 Párrafos partidos a mitad de frase unidos (11 casos)
- [x] T18 `developed` → `desarrollados`; tildes `búsqueda`/`realizó`/`región`/`dirección`
- [x] T19 Redundancia `en Suecia en Mälardalen`

### Defectos estructurales encontrados durante la ejecución
- [x] **Lista V partida**: cada entrada cortada con línea en blanco entre fragmentos;
      al renderizar, 104 fragmentos se convertían en párrafos distintos
- [x] Cursivas partidas por salto de línea (títulos de revista y de obra)
- [x] Negritas partidas (`**Microsoft** **Research**`) y frase partidas en negrita
- [x] `DDD- liviano` con espacio fantasma en matrices de anexos (6 sitios)
- [x] `Indicadores :` espacio antes de dos puntos
- [x] Citas parentéticas de Stack Overflow sin coma: `(Stack Overflow 2025)`
- [x] Nombre de revista unificado en `Revista Peruana de Computación y Sistemas`

## Verificación

Comprobado sobre el archivo final:
- comillas rectas 0 · comillas curvas 0 · angulares 20
- `%` pegado al número 0 · `IC 95 %` en 7 sitios
- `et al.` con 2 autores 0 · `developed` 0 · primera persona 0
- `&` en cita narrativa 0 · coma antes de `(año)` 0
- `DDD- liviano` 0 · `Master's Thesis` 0
- Referencias: 26 entradas, una línea cada una, orden alfabético correcto
- Índice: 0 anclas rotas
- Citas huérfanas: 0 (cruce cuerpo ↔ lista V: 25 fuentes citadas, 26 entradas, las 2 de Stack Overflow son ediciones distintas)

## Pendiente para el autor
1. **Números de página en las citas textuales** — RESUELTO con las fuentes del vault (Trebejo p. 57, Alkazemi p. 1, Peldszus p. 1; Evans reformulada como subtítulo). Quedan sin página, con justificación APA 7: Gnanasambandam (traducción con original al lado, informe sin paginación fija) y Stack Overflow 2024/2025 (encuestas web sin paginación).
2. **Quitar los `→ [[...]]`** de la lista V antes de exportar a PDF/Word. Se
   conservaron porque son andamiaje de navegación del vault Obsidian.
3. **Verificar el dato de Stack Overflow 2024** — RESUELTO: el informe dice
   textualmente "Technical debt is the top frustration at work for professional developers
   according to 63% of respondents" (Stack Overflow Developer Survey 2024,
   sección Most common frustrations). («the DevRel scaffolding» confirmado en la
   misma fuente, sección de salarios y experiencia del desarrollador.)
4. **Longitud de párrafos**: se unieron los fragmentos, pero hay párrafos largos
   (L87 tiene ~3.900 caracteres). No los dividí porque es una decisión de
   argumentación, no de corrección.
