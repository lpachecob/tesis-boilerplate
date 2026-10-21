#!/usr/bin/env python3
"""
Analisis estructural POR ENTIDAD — pre-test de tesis.

Para cada entidad de dominio (Item, Product, ShoppingList) mide:
  1. Tamano real de cada artefacto (LOC code, sin blancas ni comentarios).
  2. Similitud estructural de cada artefacto contra el MISMO artefacto de
     las otras entidades (controlador vs controlador, modelo vs modelo, etc).
  3. Cuanto del artefacto es esqueleto replicable vs logica propia.

Objetivo: cuantificar el boilerplate que el engine del framework debe
generar por hidratacion desde la entidad declarada.

Uso:
    python3 sim-por-entidad.py
"""

import difflib
import itertools
import os
import re

def _repo_root():
    """Detecta la raiz del repo subiendo hasta encontrar app/ y composer.json.
    Permite ejecutar el script tanto desde la raiz como desde para-tesis/scripts/."""
    here = os.path.dirname(os.path.abspath(__file__))
    cur = here
    for _ in range(6):
        if os.path.isdir(os.path.join(cur, "app")) and os.path.isfile(
            os.path.join(cur, "composer.json")
        ):
            return cur
        cur = os.path.dirname(cur)
    return here


REPO = _repo_root()

ENTITIES = [
    "ShoppingListUser", "ShoppingList", "Product", "Item", "User", "Unit",
]

# Artefactos por entidad: (etiqueta, ruta relativa)
ARTIFACTS = {
    "Controlador": {
        "Item": "app/Http/Controllers/ItemController.php",
        "Product": "app/Http/Controllers/ProductController.php",
        "ShoppingList": "app/Http/Controllers/ShoppingListController.php",
    },
    "Modelo": {
        "Item": "app/Models/Item.php",
        "Product": "app/Models/Product.php",
        "ShoppingList": "app/Models/ShoppingList.php",
    },
    "RequestStore": {
        "Item": "app/Http/Requests/Item/Store.php",
        "Product": "app/Http/Requests/Product/Store.php",
        "ShoppingList": "app/Http/Requests/ShoppingList/Store.php",
    },
    "RequestUpdate": {
        "Item": "app/Http/Requests/Item/Update.php",
        "Product": "app/Http/Requests/Product/Update.php",
        "ShoppingList": "app/Http/Requests/ShoppingList/Update.php",
    },
    "Migracion": {
        "Item": None,  # se resuelve por glob
        "Product": None,
        "ShoppingList": None,
    },
}


def find_migration(table):
    d = os.path.join(REPO, "database/migrations")
    for f in sorted(os.listdir(d)):
        if f.endswith("_create_%s_table.php" % table):
            return "database/migrations/" + f
    return None


def loc_code(path):
    """LOC campo 'code' aproximado: lineas no vacias, sin comentarios de linea
    ni docblocks. Coincide con cloc --by-file para este repo."""
    if not path or not os.path.exists(os.path.join(REPO, path)):
        return 0
    src = open(os.path.join(REPO, path), encoding="utf-8").read()
    src = re.sub(r"/\*\*.*?\*/", "", src, flags=re.S)
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    src = re.sub(r"//[^\n]*", "", src)
    return sum(1 for ln in src.splitlines() if ln.strip())


def normalize(path):
    full = os.path.join(REPO, path)
    src = open(full, encoding="utf-8").read()
    src = re.sub(r"/\*\*.*?\*/", "", src, flags=re.S)
    src = re.sub(r"//[^\n]*", "", src)
    src = re.sub(r"^\s*(namespace|use)\b.*$", "", src, flags=re.M)
    src = re.sub(r"class\s+\w+", "class ENTITY", src)
    for name in ENTITIES:
        src = re.sub(r"\b" + name + r"\b", "ENTITY", src)
    src = re.sub(r"\$\w+", "$V", src)
    src = re.sub(r"'[^']*'", "'S'", src)
    return re.findall(r"[A-Za-z_]\w*|\S", src)


def sim(a, b):
    return round(
        difflib.SequenceMatcher(None, normalize(a), normalize(b)).ratio() * 100, 1
    )


def resolve(artifact, entity):
    if artifact == "Migracion":
        return find_migration(
            {"Item": "items", "Product": "products", "ShoppingList": "shopping_lists"}[entity]
        )
    return ARTIFACTS[artifact][entity]


def main():
    ents = ["Item", "Product", "ShoppingList"]

    print("=" * 78)
    print("LOC 'code' REAL POR ARTEFACTO Y ENTIDAD")
    print("=" * 78)
    header = f"{'Artefacto':16}" + "".join(f"{e:>14}" for e in ents) + f"{'Total':>9}"
    print(header)
    print("-" * len(header))
    for art in ["Modelo", "Controlador", "RequestStore", "RequestUpdate", "Migracion"]:
        row = f"{art:16}"
        vals = []
        for e in ents:
            n = loc_code(resolve(art, e))
            vals.append(n)
            row += f"{n:>14}"
        print(row + f"{sum(vals):>9}")
    print("-" * len(header))
    row = f"{'TOTAL/entidad':16}"
    grand = 0
    for e in ents:
        n = sum(loc_code(resolve(art, e)) for art in
                ["Modelo", "Controlador", "RequestStore", "RequestUpdate", "Migracion"])
        grand += n
        row += f"{n:>14}"
    print(row + f"{grand:>9}")

    print()
    print("=" * 78)
    print("SIMILITUD ESTRUCTURAL ENTRE ENTIDADES (mismo artefacto, distinta entidad)")
    print("=" * 78)
    for art in ["Controlador", "Modelo", "RequestStore", "RequestUpdate", "Migracion"]:
        print(f"\n--- {art} ---")
        vals = []
        for a, b in itertools.combinations(ents, 2):
            pa, pb = resolve(art, a), resolve(art, b)
            if pa and pb:
                s = sim(pa, pb)
                vals.append(s)
                print(f"  {a:14} vs {b:14} -> {s}%")
        if vals:
            print(f"  PROMEDIO {art}: {round(sum(vals) / len(vals), 1)}%")

    # Similitud Item vs Product vs ShoppingList a nivel MODULO (4 artefactos juntos)
    print()
    print("=" * 78)
    print("SIMILITUD A NIVEL MODULO (controlador+modelo+2 requests+migracion juntos)")
    print("=" * 78)

    def module_tokens(e):
        toks = []
        for art in ["Modelo", "Controlador", "RequestStore", "RequestUpdate", "Migracion"]:
            p = resolve(art, e)
            if p:
                toks += normalize(p) + ["<<FILE>>"]
        return toks

    for a, b in itertools.combinations(ents, 2):
        s = round(
            difflib.SequenceMatcher(None, module_tokens(a), module_tokens(b)).ratio() * 100, 1
        )
        print(f"  modulo {a:14} vs {b:14} -> {s}%")


if __name__ == "__main__":
    main()
