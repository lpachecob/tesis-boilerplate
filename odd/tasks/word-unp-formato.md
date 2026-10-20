# Word UNP — conversión con formato del manual

## Objetivo
Generar `tesis_boilerplate.docx` a partir de `tesis_boilerplate.md` aplicando las
especificaciones del REGLAMENTO OCIN-VRI-UNP-2017 (ANEXO 1 proyecto / ANEXO 4 tesis).

## Alcance
- Formato: Times New Roman 11 pt, interlineado sencillo, márgenes L 3 cm / R 2.5 cm / T y B 2.5 cm.
- Títulos: nivel 1 → 14 pt negrita; niveles 2–4 → 12 pt negrita (numeración ya en el texto).
- Numeración de páginas en parte inferior derecha (todas las páginas).
- Portada según Formato N°1: Universidad 18 pt, Facultad/Escuela 16 pt, resto 14 pt, centrado.
- Índice con páginas reales mediante campo TOC de Word (actualizable con F9).
- Tablas: fuente 10 pt (más pequeña que el cuerpo, según ANEXO 4), bordes conservados.
- Sintaxis Obsidian resuelta: wikilinks → texto visible; líneas `→ [[...]]` eliminadas de la lista V.

## Restricciones
- El contenido textual NO cambia: solo conversión de formato y resolución de sintaxis de vault.
- Herramientas: LibreOffice (headless) + scripts de conversión/post-proceso (no hay pandoc ni python-docx).

## Tareas
- [x] W1 Limpiar markdown: wikilinks, flechas de lista V, índice → marca TOC
- [x] W2 Convertir md → docx con LibreOffice (infilter Markdown)
- [x] W3 Post-procesar XML: estilos TNR, márgenes A4, pie con número de página, portada, campo TOC
- [x] W4 Verificar: abrir docx, revisar estilos/márgenes/pie/tablas y el texto contra el md

## Verificación (evidencia W3–W4, 2026-09-29)
- **Estructura zip**: `word/footer1.xml` presente; rels con `Id="rIdF1"` → `Target="footer1.xml"`;
  `[Content_Types].xml` registra el footer; imagen en `word/media/image1.png` (1 sola).
- **sectPr**: `pgMar` left=1701 / right=1417 / top=1417 / bottom=1417, header=709, footer=709;
  `footerReference w:type="default" r:id="rIdF1"`; A4 11906×16838 twips.
- **Portada** (párrafos 0–11, todos `jc=center`):
  - 0 UNIVERSIDAD NACIONAL DE PIURA — sz 36 bold (18 pt)
  - 1 Facultad de Ingeniería Industrial — sz 32 (16 pt)
  - 2 Escuela Profesional de Ingeniería Informática — sz 32 (16 pt)
  - Resto sz 28 (14 pt); PROYECTO DE TESIS y título en bold (como en el md).
- **Saltos de página**: 2 (`<w:br w:type="page"/>`): tras PIURA-PERÚ y tras el campo TOC.
- **Campo TOC**: `TOC \o "1-3" \h \z \u` con fldChar begin/separate/end; `@@TOC@@` eliminado;
  `updateFields=true` en settings (insertado antes de `<w:compat>`, orden del schema).
- **Imagen**: `<w:drawing>` quedó DESPUÉS de `</w:tbl>` (fuera de la tabla de Fases), párrafo
  centrado BodyText; pie "Ilustración 1- Fases del procedimiento" en párrafo centrado, cursiva.
- **Fuentes/estilos**: docDefaults/Normal/Ttulo → TNR 11 (sz 22); Heading1 sz 28, H2–H4 sz 24
  (H4 sin itálica); sin `numPr` en headings (outlineLvl conservado para TOC);
  Contenidodelatabla/Ttulodelatabla → TNR 10 (sz 20); `w:line=276` → 240 (interlineado sencillo,
  0 restantes en document.xml). Único "Liberation" restante: Liberation Mono en
  Textopreformateado (estilo de código, intencional).
- **Footer**: `jc=right`, campo `PAGE`, TNR sz 22 (11 pt); numeración visible 1..N en todas
  las páginas del PDF (portada incluida).
- **PDF de control** (LibreOffice): A4, **38 páginas**; portada centrada, ÍNDICE con placeholder
  F9, imagen en página 22 (pdfimages: 540×303 RGB), orden tabla → imagen → pie → contenido.
- **Integridad textual**: normalizando sintaxis md (encabezados, negrita/cursiva, código, bullets,
  pipes de tabla, imagen base64, enlaces, etiquetas HTML, placeholder TOC y BOM) →
  `equal: True` entre `tesis_limpio.md` y el texto del docx (116 307 caracteres).
  Cero wikilinks `[[ ]]`, cero `→`, cero `@@TOC@@`, cero `##` md, cero `**` md, cero `[](url)`.

## Notas para el usuario
- Actualizar el índice en Word: seleccionar el campo y presionar F9.
- El md NO tiene logo UNP ni "Coasesor:" — no se inventaron; el usuario debe insertarlos en la
  portada si su facultad lo exige.
- Alineación del cuerpo: izquierda (start), como importa LO; el manual no exige justificado —
  queda a criterio de la facultad del usuario.
- Sin corchetes ni comas en el asesor: la portada dice solo "Asesor" (el md no trae nombre).

## Ruta de implementación
- Directa inline (scripts de una sola pieza + verificación), sin SDD.