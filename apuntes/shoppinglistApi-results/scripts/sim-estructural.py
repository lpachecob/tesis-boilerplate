#!/usr/bin/env python3
"""
Similitud estructural entre capas MVC replicadas — pre-test de tesis.

Mide lo que SonarQube NO ve: la repeticion del ESQUELETO entre recursos.
Dos controladores que implementan el mismo CRUD con otra entidad son
estructuralmente el mismo archivo; Sonar los puntua en 0% porque no hay
>=100 tokens identicos. Este script normaliza (borra docblocks/imports,
sustituye nombres de entidad y variables) y compara token a token.

Uso:
    python3 sim-estructural.py            # desde la raiz del repo
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

# Nombres de entidad que se neutralizan a ENTITY
ENTITIES = [
    "ShoppingListUser", "ShoppingList", "Product", "Item", "User", "Unit",
]

RESOURCE_CONTROLLERS = [
    "ItemController.php",
    "ProductController.php",
    "ShoppingListController.php",
    "ShoppingListUserController.php",
    "UnitController.php",
]


def normalize(path):
    """Devuelve la secuencia de tokens normalizada."""
    src = open(path, encoding="utf-8").read()
    src = re.sub(r"/\*\*.*?\*/", "", src, flags=re.S)          # docblocks
    src = re.sub(r"//[^\n]*", "", src)                          # line comments
    src = re.sub(r"^\s*(namespace|use)\b.*$", "", src, flags=re.M)  # imports
    src = re.sub(r"class\s+\w+", "class ENTITY", src)
    for name in ENTITIES:
        src = re.sub(r"\b" + name + r"\b", "ENTITY", src)
    src = re.sub(r"\$\w+", "$V", src)                           # variables
    src = re.sub(r"'[^']*'", "'S'", src)                        # string literals
    return re.findall(r"[A-Za-z_]\w*|\S", src)


def similarity(a, b):
    return round(
        difflib.SequenceMatcher(None, normalize(a), normalize(b)).ratio() * 100, 1
    )


def report_controllers():
    print("=== CONTROLADORES de recurso (similitud estructural) ===")
    paths = [
        os.path.join(REPO, "app/Http/Controllers", c)
        for c in RESOURCE_CONTROLLERS
    ]
    paths = [p for p in paths if os.path.exists(p)]
    vals = []
    for a, b in itertools.combinations(paths, 2):
        s = similarity(a, b)
        vals.append(s)
        print(f"  {os.path.basename(a):30} vs {os.path.basename(b):30} -> {s}%")
    if vals:
        print(f"\n  PROMEDIO: {round(sum(vals) / len(vals), 1)}%")


def report_requests(min_sim=80):
    print(f"\n=== FormRequests: pares con similitud >= {min_sim}% ===")
    reqs = []
    for root, _, files in os.walk(os.path.join(REPO, "app/Http/Requests")):
        for f in sorted(files):
            if f.endswith(".php"):
                reqs.append(os.path.join(root, f))
    reqs.sort()
    total = 0
    hi = 0
    for a, b in itertools.combinations(reqs, 2):
        total += 1
        s = similarity(a, b)
        if s >= min_sim:
            hi += 1
            na = os.path.relpath(a, os.path.join(REPO, "app/Http/Requests"))
            nb = os.path.relpath(b, os.path.join(REPO, "app/Http/Requests"))
            print(f"  {na:28} vs {nb:28} -> {s}%")
    print(f"\n  {hi} de {total} pares posibles con similitud >= {min_sim}%")


if __name__ == "__main__":
    report_controllers()
    report_requests()
