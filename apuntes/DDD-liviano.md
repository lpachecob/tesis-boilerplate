---
tags: [apunte, tesis, marco-teorico, arquitectura, contribucion-propia]
tipo: apunte de concepto
---

# DDD-liviano

> La posición teórica propia de la tesis. No es Domain-Driven Design completo:
> es DDD con la capa estratégica removida, y por eso se le dice *liviano*.

## El problema que resuelve

La tesis no propone reescribir el dominio. Propone **generar** el código que se
repite. Pero si la generación es ciega, produce estructura sin intención. La
herramienta que controla la generación tiene que conocer el modelo de dominio:
ahí entra DDD. Ver [[Código boilerplate y scaffolding]].

## DDD completo vs. DDD-liviano

[[Evans 2003 - Domain-Driven Design/Evans03|Evans (2003)]] organiza el libro en
cuatro partes. La distinción de "liviano" cae exactamente en esa frontera:

| Parte | Contenido | ¿En el framework? |
| --- | --- | --- |
| Part I — *The Kernels of the Model* | Crunching Knowledge, Lenguaje Ubiquitous, Modelo e implementación | Parcial: solo el lenguaje del dominio |
| **Part II — *The Building Blocks of Model-driven Design*** | Entidades, Value Objects, **Aggregates**, **Repositories**, **Domain Services**, capa de aplicación | **Sí — el núcleo del framework** |
| Part III — Reconstruction, Refactoring, Delivery | Integración con el proceso de entrega | No: es territorio de la metodología |
| Part IV — *Strategic Design* | Bounded Context, Distillation, Large-Scale Structure | **No — es lo que se descarta** |

**"Liviano" significa exactamente esto: se conservan los patrones tácticos de
Part II y se descarta la capa estratégica de Part IV.** No es DDD "simplificado"
por pereza, es DDD acotado a un proyecto donde el *bounded context* ya está
dado por el alcance de la tesis y no hace falta derivarlo
re-derivarlo.

## Los patrones que el framework encapsula

Según el propio glosario del documento, un framework de dominio es «una
estructura de soporte que encapsula patrones tácticos del DDD (Aggregates,
Repositories, Domain Services), permitiendo al desarrollador enfocarse en la
lógica diferenciadora del negocio». Son los tres que la generación necesita
para saber *qué* producir:

- **Aggregate** — la frontera de consistencia. Define qué entidades se cargan y
  se guardan juntas; de ahí sale el alcance de un endpoint.
- **Repository** — la abstracción de persistencia que permite al framework
  emitir un mapper uniforme sin conocer la tabla ni el ORM.
- **Domain Service** — la lógica que no pertenece a ninguna entidad. Es la que
  el desarrollador **no** quiere autogenerar, y por eso el framework debe
  dejarla explícita.

## Por qué esto reduce boilerplate

Porque el generador no adivina la estructura: la **deriva del modelo**. Un
endpoint por aggregate, un mapper por repository, y la lógica de negocio
declarada aparte. La repetibilidad deja de ser un defecto del desarrollador y pasa a
ser la propiedad de la que se benefician la generación y el mantenimiento.

## Cuidado

DDD-liviano no es una categoría establecida en la literatura. Es la
contribución de esta tesis y hay que defenderla como tal en la sustentación:
el criterio de qué se descarta y por qué es el argumento, no la etiqueta.

## Ver también

- [[Código boilerplate y scaffolding]] — el problema
- [[Deuda técnica]] — el costo
- [[Operacionalización de variables]] — cómo se mide el resultado
