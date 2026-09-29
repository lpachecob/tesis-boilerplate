---
tags: [apunte, tesis, marco-teorico, ia, verificacion]
tipo: apunte de concepto
---

# Verificación de salidas de IA

> El problema que en 2025 desplazó a la deuda técnica como principal
> frustración de los desarrolladores. Importa para la tesis porque define el
> límite de la generación automática: no basta con generar, hay que poder
> **confiar** en lo generado.

## El dato

De [[Stack Overflow 2025 - Developer Survey/Stack Overflow Developer Survey 2025|Stack Overflow Developer Survey 2025]]: la principal frustración declarada por el **66 %** de los desarrolladores son las **«soluciones de IA que están casi bien, pero no del todo»** (*AI solutions that are almost right, but not quite*).

## Por qué "casi bien" es peor que "mal"

Una salida completamente incorrecta se detecta y se descarta: el costo es
tiempo perdido y nada más. Una salida **casi correcta** pasa la revisión
superficial, se integra, y el defecto aparece en producción. El costo no es la
corrección: es el haber confiado. De ahí el esfuerzo de verificación, que es
justamente trabajo mecánico.

Esta es la cara oculta del dato de [[Entropía de código y code churn]]: la IA
acelera la generación **y** multiplica la carga de comprobación. La ganancia
neta depende de cuál de las dos domine, y hoy nadie tiene esa respuesta cerrada.

## Qué implica para una generación automática defendible

La tesis no puede simplemente afirmar "genero más rápido". Tiene que sostener que su
generación es **predecible**: si el endpoint generado responde a la definición
del aggregate y a nada más, entonces es determinista y verificable por
inspección. Ese es el argumento a favor de DDD-liviano frente a un generador
genérico basado en plantillas o prompts. Ver [[DDD-liviano]].

## Dato de contraste, 2024 vs. 2025

| Año | Principal frustración reportada |
| --- | --- |
| 2024 | Deuda técnica — **63 %** |
| 2025 | Soluciones de IA "casi bien" — **66 %** |

El término "technical debt" prácticamente desaparece de la lista en 2025. No
significa que la deuda técnica se resolvió: significa que dejó de ser lo que más
molesta. Leer el 2024 sin el 2025 da una imagen desactualizada del campo.

## Ver también

- [[Entropía de código y code churn]] — la otra mitad de la ecuación
- [[Deuda técnica]] — lo que se desplazó
