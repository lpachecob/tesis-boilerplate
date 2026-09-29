---
tags: [apunte, tesis, marco-teorico, problema, objeto-de-estudio]
tipo: apunte de concepto
---

# Código boilerplate y scaffolding

> El objeto de estudio de la tesis. Todo lo demás —el marco, el método, las
> métricas— se organiza alrededor de eliminar este código.

## Definición

**Boilerplate** es el código necesario para que el sistema funcione pero que
**no expresa lógica de dominio**. Se replica, casi literalmente, por cada
entidad o módulo nuevo. No es código malo: es código *repetible*, y por eso es
perfecto candidato para generarse.

**Scaffolding** es su sinónimo en el ecosistema de frameworks: la estructura que
se levanta automáticamente al iniciar un proyecto o módulo. En este documento
se usan como equivalentes.

En una API REST el boilerplate típico es:

- controladores con los mismos métodos CRUD
- capas de servicio
- objetos de transferencia de datos (DTOs)
- *mappers* entre entidad y DTO
- configuración de rutas

La suma obliga a escribir cientos de líneas cuya lógica no cambia de un recurso
a otro.

## Por qué es un problema y no una molestia menor

Porque el costo no es el tiempo de teclear: es la **fragmentación del
razonamiento**. El desarrollador alterna entre construir reglas de negocio —donde
está el valor— y transcribir estructura —donde no lo hay—, y ese cambio de
tarea interrumpe el flujo de resolución de problemas complejos. Es el punto que
desarrolla [[Ma 2024 - Breaking the Flow: A Study of Interruptions/Ma et al. - 2024 - Breaking the Flow A Study of Interruptions During Software Engineering Activities|Ma et al. (2024)]], de Duke University y Vanderbilt University.

## La evidencia empírica

De [[Peldszus 2026 - Developer Perspectives on REST API Usability/Peldszus et al. - 2026 - Developer Perspectives on REST API Usability A Study of REST API Guidelines|Peldszus et al. (2026)]], Ruhr University Bochum e IT University of Copenhagen:

| Indicador | Valor |
| --- | --- |
| APIs REST públicas concentradas por esta arquitectura (2017) | **82 %** |
| APIs registradas (2022) | **24 471** |
| APIs REST que exponen entre 11 y 100 operaciones | **62 %** |

La tercera cifra es la que más importa: casi dos tercios de las APIs repiten en
un rango de operaciones **muy similar al de la tesis**, y cada operación
replica las mismas estructuras. A escala de 24 471 APIs, eso es lo que convierte
el problema en estructural y no en una molestia de proyecto.

## La paradoja de la IA

La herramienta que debía resolver el problema lo agravó. Ver
[[Entropía de código y code churn]].

## Ver también

- [[Deuda técnica]] — el costo acumulado de ese código
- [[DDD-liviano]] — la respuesta arquitectónica de la tesis
- [[Operacionalización de variables]] — cómo se mide la reducción
