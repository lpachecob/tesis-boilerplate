---
tags: [apunte, tesis, marco-teorico, productividad, metricas]
tipo: apunte de concepto
---

# Inner loop y outer loop

> El marco que usa la tesis para explicar **dónde se va el tiempo** de un
> desarrollador, y por qué quitar código mecánico no es una mejora de productividad
> marginal sino el movimiento más grande disponible.

## La división

De [[Gnanasambandam 2023 - Yes, you can measure developer productivity/Gnanasambandam et al. - 2023 - Yes, you can measure software developer productivity|McKinsey & Company (2023)]]:

- **Inner loop** — codificar, construir y probar. Es trabajo de creación
  directa. Objetivo declarado de las empresas tecnológicas líderes: que sus
  desarrolladores dediquen **hasta el 70 %** de su tiempo aquí.
- **Outer loop** — integración, pruebas de integración, *release*, despliegue,
  seguridad, cumplimiento y reuniones. El esfuerzo restante. McKinsey lo califica
  de **«tareas tediosas y poco satisfactorias»**.

## Por qué importa más que una cifra de velocidad

La lectura ingenua sería: "el desarrollador es 70 % productivo". La lectura útil es
**composicional**: si el *outer loop* es tedioso y el *inner loop* es el valor,
entonces cualquier hora recuperada en tareas mecánicas se traduce
directamente en Inner loop. No es una ganancia lineal del 30 %, es una
**transferencia de categoría**.

## La conexión con la tesis

La generación automática de endpoints no acelera el tecleo: elimina trabajo del
*outer loop* (andamiaje, mapeo, configuración) y lo convierte en trabajo de
*inner loop* (definir el aggregate, escribir la regla de negocio). Ese es el
mecanismo causal que la tesis propone medir, y por eso [[Operacionalización de variables]]
define el indicador en términos de reducción de estructura, no en líneas de
código.

## Advertencia sobre la fuente

Este dato viene de *Technology, Media & Telecommunications Practice* de
McKinsey & Company, **no** del McKinsey Global Institute. Un borrador anterior
atribuyó la cifra al Global Institute; era una fuente distinta. Corregido.

## Ver también

- [[Código boilerplate y scaffolding]] — el trabajo mecánico a eliminar
- [[Entropía de código y code churn]] — por qué la IA no lo resuelve
