---
tags: [apunte, tesis, marco-teorico, ia, paradoxo]
tipo: apunte de concepto
---

# Entropía de código y code churn

> El giro que convierte el problema de la tesis en algo urgente: la IA generativa
> no eliminó el boilerplate, lo industrializó.

## Qué es *code churn*

El porcentaje de líneas que se **revierten o actualizan** menos de dos semanas
después de haber sido escritas. Es una medida de desaparición: código que se
escribe y se deshace. El churn bajo indica que el código se sostiene; el churn
alto indica que se está escribiendo código que no se sabe si está bien.

## El hallazgo

De [[Harding 2024 - Coding on Copilot/Harding y Kloster - 2024 - Coding on Copilot 2023 Data Shows Downward Pressure on Code Quality|GitClear (2024)]]:

- El uso de asistentes de codificación empresarial (OpenAI, Google, Anthropic)
 produjo un **incremento en bloques de código duplicado** (*copy/pasted code*),
  medido como proporción de las líneas actualizadas, eliminadas o movidas.
- Proyección de **duplicación del code churn** para 2024 frente a la línea base
  previa a la IA (2021). GitClear lo denomina **«entropía de código»**.

Y el efecto se nota en el resultado, no solo en el volumen:

- De [[DORA 2024 - Accelerate State of DevOps Report/DORA y Google Cloud - 2024 - Accelerate State of DevOps Report 2024 Fostering Culture with Artificial Intelligence|DORA & Google Cloud (2024)]]: reducir la estabilidad de la entrega en un **7,2 %** por cada **+25 % de adopción de IA**.

## La paradoja

La IA generativa se ha comercializado como la herramienta que elimina el
código repetitivo. Los datos apuntan a lo contrario: multiplica exactamente
esa categoría. El scaffolding mal generado —por una IA o por una plantilla
rígida— produce el mismo resultado: estructura predecible,duplicada y difícil
de mantener.

Ahí está la justificación de la tesis: si la generación automática va a
producir ese código de todos modos, conviene que sea **controlada y
consistente**, derivative del modelo de dominio. Ver [[DDD-liviano]].

## La otra cara

Al mismo tiempo, la asistencia sí acelera el trabajo mecánico. De
[[Peng 2023 - The Impact of AI on Developer Productivity/Peng et al. - 2023 - The Impact of AI on Developer Productivity Evidence from GitHub Copilot|Peng et al. (2023)]],
Microsoft Research, la asistencia en tareas repetitivas incrementa la velocidad
de desarrollo en torno al **55 %**. Las dos cosas son ciertas a la vez, y esa
tensión es el estado del arte del campo.

## Ver también

- [[Verificación de salidas de IA]] — el costo de confiar en lo generado
- [[Inner loop y outer loop]] — dónde se gana y dónde se pierde ese tiempo
- [[Deuda técnica]] — el acumulador
