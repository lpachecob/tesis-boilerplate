---
tags: [apunte, tesis, marco-teorico, problema]
tipo: apunte de concepto
---

# Deuda técnica

> Problema estructural que la tesis usa como justificante del *boilerplate*. No
> es un invento del marco teórico: es la frustración laboral más reportada por
> los desarrolladores en 2024, y la razón por la que generar ese código
> automáticamente no es un lujo sino una necesidad.

## Qué es

Deuda técnica es el costo futuro de tomar atajos hoy para entregar más rápido:
estructuras que funcionan pero que nadie diseñó, que nadie documentó y que
nadie va a mantener. En el contexto de esta tesis aparece específicamente como
**el volumen de código estructural escrito a mano** —controladores, DTOs,
mapeadores, repositorios, configuración de rutas— que se replica por cada
entidad del dominio sin aportar lógica de negocio.

## Los datos (verificados)

De [[Stack Overflow 2024 - Developer Survey/Stack Overflow Developer Survey 2024|Stack Overflow Developer Survey 2024]]:

| Indicador | Valor |
| --- | --- |
| Principal frustración laboral de los desarrolladores profesionales | **63 %** |
| Concentración de la deuda técnica en el monto de las respuestas | **62,4 %** |

Estos dos números son distintos y la tesis los usa como distintos: el 63 %
mide *cuántos* desarrolladores la reportan; el 62,4 % mide *cuánto peso* tiene
dentro de lo que reportan. Confundirlos sería el error fácil.

En [[Stack Overflow 2025 - Developer Survey/Stack Overflow Developer Survey 2025|Stack Overflow 2025]] el término "technical debt" ya **no aparece** entre las frustraciones principales: fue desplazado por un problema nuevo, el de la verificación de la IA. Ver [[Verificación de salidas de IA]].

## Por qué importa para la tesis

La deuda técnica es el **denominador** del problema. La tesis no propone
reducir el esfuerzo de escribir código en general, sino eliminar la categoría de
código que la genera y que no requiere criterio. Si el *boilerplate* desaparece,
una parte de la deuda técnica desaparece con él.

## Cuidado con las fuentes

Este tema es donde antes hubo cifras inventadas en el borrador. La fuente
original de casi todos los números anteriores era `TechExactly 2025`, **que no
es una entidad real**. Los datos válidos vienen de Stack Overflow, verificables
en la nota enlazada arriba.

## Ver también

- [[Código boilerplate y scaffolding]] — el código que genera la deuda
- [[Entropía de código y code churn]] — la IA agrava el problema
- [[Inner loop y outer loop]] — dónde se va el tiempo del desarrollador
