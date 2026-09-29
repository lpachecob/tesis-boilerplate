#!/usr/bin/env python3
"""Verifica que la identidad de cada referencia sea coherente en los tres sitios
donde hoy está escrita a mano:

  1. el texto de la entrada bibliográfica,
  2. el nombre de la carpeta en referencias/,
  3. la etiqueta visible de cada cita en el cuerpo.

La bibliografía manda: es la fuente de verdad. Las carpetas y las etiquetas se
verifican contra ella. No modifica nada; solo informa y, cuando algo diverge,
imprime el comando exacto para arreglarlo.

Uso:
    python3 verificar_referencias.py           # informe completo
    python3 verificar_referencias.py --fix     # aplica los renombres propuestos

Códigos de salida: 0 sin problemas, 1 con divergencias, 2 error de uso.
"""

import argparse
import pathlib
import re
import sys
import unicodedata

RAIZ = pathlib.Path(__file__).resolve().parent
TESIS = RAIZ / "tesis_boilerplate.md"
REFERENCIAS = RAIZ / "referencias"
ENCABEZADO_BIB = "# REFERENCIAS BIBLIOGRÁFICAS"

# Entradas fuera de alcance acordadas: el usuario las excluyó de la auditoría.
FUERA_DE_ALCANCE = {
    "Deljouyi 2022 - MDD4REST",
    "Gravitee.io 2024 - AI-Driven Boilerplate Code Automation",
    "Wohlin 2012 - Experimentation in Software Engineering",
}

# Documentos que el vault conserva sin que la tesis los cite. No es un error:
# se guardaron para no perder material, pero no son referencias de la tesis.
CONSERVADAS_SIN_CITAR = {
    # El artículo de inmunología oncológica que estaba archivado con el nombre de
    # XBoot. Al identificar la fuente correcta quedo huerfano, y se conservo
    # renombrado con su identidad real en vez de borrarlo.
    "Sotirov y Dimitrov 2025 - In Silico Cancer Immunogenicity",
}

APELLIDOS_CON_PARTICULA = {"Da", "De", "Del", "Di", "La", "Las", "Le", "Los", "Van", "Von"}


def sin_acentos(texto):
    """Minúsculas sin diacríticos, para comparar nombres de forma tolerante."""
    plano = unicodedata.normalize("NFD", texto)
    return "".join(c for c in plano if not unicodedata.combining(c)).lower()


def separar_entradas(lineas, i_ref):
    """Devuelve la bibliografía como lista de (lineas, año, autor_crudo)."""
    entradas, actual = [], []
    for linea in lineas[i_ref + 1:]:
        if not linea.strip():
            continue
        actual.append(linea)
        if linea.startswith("→ [["):
            entradas.append(actual)
            actual = []
    return entradas


def anio_de(entrada):
    """Año de publicación, tolerando el ajuste de línea (puede caer en la línea 2)."""
    texto = " ".join(entrada)
    coincidencia = re.search(r"\((\d{4})\)", texto)
    if not coincidencia:
        return None
    return coincidencia.group(1)


def apellido_de(entrada):
    """Primer apellido nominal, ignorando el punto final y las partículas."""
    texto = " ".join(entrada)
    coincidencia = re.match(r"^(.*?)\s*\(\d{4}\)", texto)
    if not coincidencia:
        return None
    autor = coincidencia.group(1).strip().rstrip(",").rstrip(".")
    partes = re.split(r",|\s+y\s+|\s+&\s+|\s+et al\.|\s+& Company|\.", autor)
    for parte in partes:
        limpia = parte.strip()
        if limpia and limpia not in APELLIDOS_CON_PARTICULA:
            return limpia
    return None


def destino_de(entrada):
    """Destino del wikilink de la entrada, sin la etiqueta visible."""
    enlace = entrada[-1]
    coincidencia = re.search(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", enlace)
    if not coincidencia:
        return ""
    return coincidencia.group(1).strip()


def prefijo_de_carpeta(nombre):
    """Parte del nombre de carpeta anterior al primer separador ' - '."""
    return nombre.split(" - ")[0].strip()


# --- reescritura confinada de destinos de wikilink --------------------------

WIKILINK = re.compile(r"\[\[([^\]|]*)(?:\|([^\]]*))?\]\]")
MARCA = "\x00DESTINO\x00"


def normalizar(linea, conservar_etiqueta):
    """Neutraliza el destino de cada wikilink para poder comparar el resto.

    Si el texto visible de la linea es identico antes y despues del cambio,
    el unico cambio posible esta dentro del destino del enlace, que no se
    renderiza. Ahi es donde se permite tocar: el texto que el lector ve
    solo cambia si --etiquetas esta activo.
    """
    if conservar_etiqueta:
        return WIKILINK.sub(f"[[{MARCA}]]", linea)
    return WIKILINK.sub(
        lambda m: f"[[{MARCA}|{m.group(2) or ''}]]", linea
    )


class SubstitutionError(Exception):
    """El texto a escribir no es solo un cambio de destinos. No se escribe."""


def escribir(ruta, contenido):
    """Escribe de forma atomica: temporal y renombrado, nunca a medias."""
    temporal = ruta.with_name(ruta.name + ".tmp")
    temporal.write_text(contenido, encoding="utf-8")
    temporal.replace(ruta)


def conferir_cambio(lineas_antes, lineas_despues, conservar_etiqueta):
    """Verifica que la reescritura solo haya tocado destinos de wikilink.

    Es la red que evita repetir el incidente en el que un script reescribio una
    region entera y borro un encabezado de los anexos. Ante cualquier duda
    lanza SubstitutionError y quien llama no escribe nada.
    """
    if len(lineas_antes) != len(lineas_despues):
        raise SubstitutionError(
            f"el numero de lineas cambio: {len(lineas_antes)} -> {len(lineas_despues)}"
        )
    enlaces_antes = sum(len(WIKILINK.findall(l)) for l in lineas_antes)
    enlaces_despues = sum(len(WIKILINK.findall(l)) for l in lineas_despues)
    if enlaces_antes != enlaces_despues:
        raise SubstitutionError(
            f"el numero de wikilinks cambio: {enlaces_antes} -> {enlaces_despues}"
        )
    for numero, (antes, despues) in enumerate(zip(lineas_antes, lineas_despues), 1):
        if antes == despues:
            continue
        if normalizar(antes, conservar_etiqueta) != normalizar(despues, conservar_etiqueta):
            raise SubstitutionError(
                f"el cambio de la linea {numero} sale del destino de un wikilink.\n"
                f"      antes: {antes!r}\n"
                f"      ahora: {despues!r}"
            )


def resolver_destino(destino, cambios):
    """Reescribe un destino aplicando el prefijo mas largo que coincida.

    No basta con buscar la ruta exacta: un enlace a una nota trae el nombre del
    archivo detras de la carpeta, asi que el destino es un prefijo mas largo que
    la carpeta. Con el caso exacto, renombrar la carpeta dejaba los enlaces
    apuntando a un archivo que ya no existia.
    """
    if not cambios:
        return destino
    for clave in sorted(cambios, key=len, reverse=True):
        if destino == clave or destino.startswith(clave + "/"):
            sufijo = destino[len(clave):]
            return cambios[clave] + sufijo
    return destino


def reescribir_destinos(lineas, cambios, conservar_etiqueta, apellidos=None):
    """Aplica el mapa de rutas a los destinos de los wikilinks de las lineas.

    Si --etiquetas esta activo, la etiqueta visible solo cambia cuando su
    primer token es exactamente el apellido que se esta corrigiendo. Nunca se
    reescribe texto que venga de otra fuente.
    """
    apellidos = apellidos or {}
    resultado = []
    for linea in lineas:
        def sustituir(match):
            destino, etiqueta = match.group(1), match.group(2)
            nuevo = resolver_destino(destino, cambios)
            if etiqueta is None:
                return f"[[{nuevo}]]"
            if conservar_etiqueta:
                palabras = etiqueta.split(" ")
                if palabras and palabras[0] in apellidos:
                    palabras[0] = apellidos[palabras[0]]
                    etiqueta = " ".join(palabras)
            return f"[[{nuevo}|{etiqueta}]]"

        resultado.append(WIKILINK.sub(sustituir, linea))
    return resultado


def main(solo_informe=False):
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument(
        "--fix",
        action="store_true",
        help="renombra carpetas y notas, y actualiza los destinos de los wikilinks",
    )
    parser.add_argument(
        "--etiquetas",
        action="store_true",
        help="ademas de los destinos, cambia el texto visible de las citas. "
        "Esto SI altera lo que se lee, asi que va aparte y por defecto apagado",
    )
    args = parser.parse_args()
    if solo_informe:
        args.fix = False

    if not TESIS.exists():
        print(f"No encuentro {TESIS}", file=sys.stderr)
        return 2

    texto = TESIS.read_text(encoding="utf-8")
    lineas = texto.split("\n")

    indice = next(
        (i for i, l in enumerate(lineas) if l.strip() == ENCABEZADO_BIB), None
    )
    if indice is None:
        print(f"No encuentro el encabezado {ENCABEZADO_BIB}", file=sys.stderr)
        return 2

    entradas = separar_entradas(lineas, indice)
    carpetas = {
        p.name: p for p in REFERENCIAS.iterdir() if p.is_dir() and not p.name.startswith("_")
    }

    problemas = []

    # --- 1. entradas: coherencia interna y contra su carpeta -------------------
    print(f"Entradas bibliográficas: {len(entradas)}")
    print(f"Carpetas en referencias/: {len(carpetas)}\n")

    print(f"{'#':<4}{'AUTOR':<22}{'AÑO':<7}{'CARPETA':<46}ESTADO")
    print("-" * 100)

    for numero, entrada in enumerate(entradas, 1):
        anio = anio_de(entrada)
        apellido = apellido_de(entrada)
        destino = destino_de(entrada)
        carpeta = destino.split("/")[0]
        archivo = destino.split("/")[1] if "/" in destino else None

        if anio is None or apellido is None:
            problemas.append(f"entrada {numero}: no se pudo leer autor/año -> {entrada[0][:60]}")
            print(f"{numero:<4}{'???':<22}{'???':<7}{carpeta[:44]:<46}ILEGIBLE")
            continue

        ruta_carpeta = REFERENCIAS / carpeta
        existe_carpeta = ruta_carpeta.exists()

        # ¿la carpeta refleja el autor y el año que dice la bibliografía?
        prefijo = prefijo_de_carpeta(carpeta)
        coincide_autor = sin_acentos(apellido) in sin_acentos(prefijo)
        coincide_anio = anio in carpeta
        divergente = existe_carpeta and not (coincide_autor and coincide_anio)

        if not existe_carpeta:
            problemas.append(f"entrada {numero}: la carpeta {carpeta!r} no existe")
            estado = "CARPETA AUSENTE"
        elif divergente:
            # El nombre correcto reutiliza el descriptor que ya está en la carpeta
            # y solo reemplaza la parte de autor y año por lo que dice la entrada.
            descriptor = carpeta.split(" - ", 1)[1] if " - " in carpeta else ""
            esperado = f"{apellido} {anio} - {descriptor}" if descriptor else f"{apellido} {anio}"
            problemas.append(
                f"entrada {numero}: la carpeta {carpeta!r} no coincide con {apellido} ({anio}). "
                f"Renombrar a: {esperado!r}"
            )
            estado = "DIVERGE"
        else:
            estado = "OK"

        if archivo is not None:
            if not (ruta_carpeta / f"{archivo}.md").exists():
                problemas.append(
                    f"entrada {numero}: no existe {carpeta}/{archivo}.md"
                )
                estado = "NOTA AUSENTE"

        print(f"{numero:<4}{apellido[:20]:<22}{anio:<7}{carpeta[:44]:<46}{estado}")

    # --- 2. enlaces del cuerpo: resolubles y coherentes con la entrada ---------
    print("\nEnlaces del cuerpo")
    destinos_cuerpo = 0
    sueltos = 0
    for indice_linea, linea in enumerate(lineas[:indice], 1):
        for destino, etiqueta in re.findall(r"\[\[([^\]|]+)\|([^\]]+)\]\]", linea):
            limpio = destino.split("#")[0].strip()
            if not limpio or limpio.startswith("#"):
                continue
            destinos_cuerpo += 1
            base = pathlib.Path(limpio).name
            if not (
                (RAIZ / f"{limpio}.md").exists()
                or list(RAIZ.rglob(f"{base}.md"))
                or list(RAIZ.rglob(base))
            ):
                problemas.append(
                    f"cuerpo L{indice_linea}: enlace roto -> [[{limpio}]]"
                )
            etiqueta_limpia = etiqueta.strip().rstrip(".")
            if not etiqueta_limpia:
                problemas.append(
                    f"cuerpo L{indice_linea}: etiqueta visible vacía en [[{limpio}]]"
                )
                sueltos += 1
    print(f"  destinos con etiqueta visible: {destinos_cuerpo}")
    print(f"  etiquetas vacías: {sueltos}")

    # --- 3. carpetas huérfanas --------------------------------------------------
    citadas = {destino_de(e).split("/")[0] for e in entradas}
    huerfanas = sorted(set(carpetas) - citadas)
    print("\nCarpetas sin entrada bibliográfica")
    if not huerfanas:
        print("  ninguna")
    for nombre in huerfanas:
        if nombre in FUERA_DE_ALCANCE:
            etiqueta = "FUERA DE ALCANCE (acordado)"
        elif nombre in CONSERVADAS_SIN_CITAR:
            etiqueta = "CONSERVADA, no es referencia de la tesis"
        else:
            etiqueta = "REVISAR"
        print(f"  {nombre}  [{etiqueta}]")
        if nombre not in FUERA_DE_ALCANCE and nombre not in CONSERVADAS_SIN_CITAR:
            problemas.append(
                f"carpeta sin citar y sin motivo registrado: {nombre!r}. "
                f"Si es material a conservar, agregala a CONSERVADAS_SIN_CITAR en este script."
            )

    # --- 4. el .md y el .pdf de una referencia deben decir lo mismo -------------
    print("\nNotas de referencia: .md frente a .pdf")
    desalineados = 0
    for carpeta in sorted(carpetas.values(), key=lambda p: p.name):
        mds = sorted(carpeta.rglob("*.md"))
        pdfs = sorted(carpeta.rglob("*.pdf"))
        if not mds or not pdfs:
            continue
        # Se comparan entre si, no solo cuando el nombre coincide: comparar
        # unicamente los de nombre identico seria no mirar nunca los INTERESTANTES.
        pares = (
            list(zip(mds, pdfs))
            if len(mds) == len(pdfs) == 1
            else [(m, p) for m in mds for p in pdfs if m.stem == p.stem]
        )
        for nota, pdf in pares:
            autor_md = nota.stem.split(" - ")[0].split(" ")[0]
            autor_pdf = pdf.stem.split(" - ")[0].split(" ")[0]
            anio_md = next((t for t in nota.stem.split(" - ") if re.fullmatch(r"\d{4}", t)), None)
            anio_pdf = next((t for t in pdf.stem.split(" - ") if re.fullmatch(r"\d{4}", t)), None)
            if sin_acentos(autor_md) != sin_acentos(autor_pdf) or anio_md != anio_pdf:
                desalineados += 1
                problemas.append(
                    f"{carpeta.name}: el .md dice {autor_md} ({anio_md}) y el .pdf dice "
                    f"{autor_pdf} ({anio_pdf}). El PDF conserva una identidad vieja."
                )
                print(f"  {carpeta.name}")
                print(f"    .md  {nota.name}")
                print(f"    .pdf {pdf.name}")
    if desalineados == 0:
        print("  todas coinciden en autor y año")

    # --- 5. aplicar renombres si se pidió --------------------------------------
    if args.fix:
        # 4a. construir el mapa, sin tocar el disco.
        #     Los destinos de wikilink del vault son relativos a referencias/ y
        #     no llevan ese prefijo, asi que se registran las dos formas.
        cambios = {}
        movimientos = []
        apellidos = {}
        for problema in problemas:
            destino = re.search(r"Renombrar a: '(.+)'", problema)
            origen = re.search(r"la carpeta '(.+?)' no coincide", problema)
            if not destino or not origen:
                continue
            viejo, nuevo = origen.group(1), destino.group(1)
            base_vieja = REFERENCIAS / viejo
            if not base_vieja.is_dir():
                continue

            cambios[viejo] = nuevo
            cambios[f"referencias/{viejo}"] = f"referencias/{nuevo}"
            movimientos.append((base_vieja, REFERENCIAS / nuevo))
            apellidos[prefijo_de_carpeta(viejo).split(" ")[0]] = prefijo_de_carpeta(nuevo).split(" ")[0]

            # la nota interna puede llevar el apellido equivocado en su nombre
            apellido_viejo = prefijo_de_carpeta(viejo).split(" ")[0]
            apellido_nuevo = prefijo_de_carpeta(nuevo).split(" ")[0]
            for nota in sorted(base_vieja.rglob("*.md")):
                if not nota.stem.startswith(apellido_viejo):
                    continue
                nombre_nuevo = apellido_nuevo + nota.stem[len(apellido_viejo):]
                relativo = nota.relative_to(base_vieja)
                cambios[f"{viejo}/{relativo}"] = f"{nuevo}/{nombre_nuevo}"
                cambios[f"referencias/{viejo}/{relativo}"] = (
                    f"referencias/{nuevo}/{nombre_nuevo}"
                )
                movimientos.append((nota, nota.with_name(nombre_nuevo)))

        if not movimientos:
            print("\nNo hay renombres que aplicar.")
        else:
            print(f"\nRutas a renombrar en disco ({len(movimientos)}):")
            for origen, destino in movimientos:
                print(f"  {origen.relative_to(RAIZ)}\n    -> {destino.relative_to(RAIZ)}")

            # 4b. reescribir los .md del vault y verificar ANTES de escribir nada
            reescritos, rechazos = [], []
            for archivo in sorted(RAIZ.rglob("*.md")):
                if archivo.name in {"tesis.bak", "verificar_referencias.py"}:
                    continue
                try:
                    lineas_antes = archivo.read_text(encoding="utf-8").split("\n")
                except (OSError, UnicodeDecodeError):
                    continue
                lineas_despues = reescribir_destinos(
                    lineas_antes, cambios, args.etiquetas, apellidos
                )
                if lineas_antes == lineas_despues:
                    continue
                try:
                    conferir_cambio(lineas_antes, lineas_despues, args.etiquetas)
                except SubstitutionError as error:
                    rechazos.append((archivo, str(error)))
                    continue
                escribir(archivo, "\n".join(lineas_despues))
                reescritos.append(archivo)

            if rechazos:
                print(f"\nABORTADO: {len(rechazos)} archivo(s) no pasaron la verificacion.")
                for archivo, motivo in rechazos:
                    print(f"  {archivo.relative_to(RAIZ)}: {motivo}")
                print("  No se renombro nada en el disco. Corrige y vuelve a intentar.")
                return 1

            # 4c. renombrar en disco, ya con todos los .md verificados
            for origen, destino in movimientos:
                if not origen.exists():
                    continue
                destino.parent.mkdir(parents=True, exist_ok=True)
                origen.rename(destino)

            print(f"\nRenombres en disco: {len(movimientos)}")
            print(f"Archivos de texto actualizados: {len(reescritos)}")
            for archivo in reescritos:
                print(f"  {archivo.relative_to(RAIZ)}")

            # El informe de arriba se calculo antes de aplicar. Se vuelve a
            # verificar para que el codigo de salida refleje el estado final.
            print("\n" + "-" * 100)
            print("Verificacion del estado ya corregido:")
            return main(solo_informe=True)

    # --- resultado --------------------------------------------------------------
    print("\n" + "=" * 100)
    if problemas:
        print(f"{len(problemas)} problema(s) pendiente(s):")
        for problema in problemas:
            print(f"  - {problema}")
        return 1
    print("Sin divergencias: bibliografía, carpetas y enlaces coinciden.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
