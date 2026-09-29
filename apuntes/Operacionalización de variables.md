---
tags: [apunte, tesis, metodologia, operacionalizacion, defensa]
tipo: apunte de concepto
---

# Operacionalización de variables

> La nota más útil para la sustentación. Traduce el problema a algo medible, y
> ahí es donde una tesis se gana o se pierde: una variable que no se puede
> medir no se puede demostrar.

## Las dos variables

**Variable independiente:** framework basado en DDD-liviano con autogeneración
de endpoints.

**Variable dependiente:** reducción del código boilerplate en APIs REST.

Fíjese en la dirección: la independiente es **una herramienta**, la dependiente
es **un cantidad de código eliminado**. La tesis no promete "más productividad"
—que sería inmensurable—, promete una reducción concreta y acotada.

## Por qué el acotamiento es la defensa

Boilerplate, como concepto, se prestaría a discusión. La operacionalización
obliga a definirlo: si la definición operativa cubre **controladores, DTOs,
mapeadores, repositorios y configuración de rutas**, entonces cualquier cantidad
medida es defendible porque el criterio se declaró antes de medir. Eso es lo que
hace que la medición sea válida en vez de arbitraria.

## La cadena de evidencia

Cada eslabón tiene su fuente, y esa cadena es lo que hay que sostener en la
defensa:

| Eje | Qué establece | Fuente |
| --- | --- | --- |
| Que el boilerplate es real y estructural | 82 % de las APIs públicas; 24 471 APIs; 62 % con 11-100 operaciones | [[Peldszus 2026 - Developer Perspectives on REST API Usability/Peldszus et al. - 2026 - Developer Perspectives on REST API Usability A Study of REST API Guidelines|Peldszus et al. (2026)]] |
| Que cuesta tiempo de valor | 70 % del tiempo en *inner loop* | [[Gnanasambandam 2023 - Yes, you can measure developer productivity/Gnanasambandam et al. - 2023 - Yes, you can measure software developer productivity|McKinsey & Company (2023)]] |
| Que la IA no lo resuelve sola | +7,2 % menos estabilidad por cada +25 % de adopción de IA | [[DORA 2024 - Accelerate State of DevOps Report/DORA y Google Cloud - 2024 - Accelerate State of DevOps Report 2024 Fostering Culture with Artificial Intelligence|DORA & Google Cloud (2024)]] |
| Que se debe poder confiar en lo generado | 66 % frustrated por salidas "casi correctas" | [[Stack Overflow 2025 - Developer Survey/Stack Overflow Developer Survey 2025|Stack Overflow 2025]] |
| Que el estado del arte es mixto | +55 % de velocidad en tareas repetitivas | [[Peng 2023 - The Impact of AI on Developer Productivity/Peng et al. - 2023 - The Impact of AI on Developer Productivity Evidence from GitHub Copilot|Peng et al. (2023)]] |

## El riesgo metodológico que queda abierto

Los indicadores de productividad de GitClear y McKinsey están construidos sobre
grandes muestras de la industria global. Aplicados al caso peruano —que es el
contexto de la tesis— son **referencia**, no evidencia directa. El marco local
peruano que sí es evidencia: Chavez & Wong, Bobadilla Chara, Vasquez Pari,
Pizarro Romero, Trebejo Loayza, Cosme Escalera, Villanueva Campos y
Campos Salcedo. Son los que sostienen la delimitación geográfica.

## Ver también

- [[DDD-liviano]] — la variable independiente, en detalle
- [[Código boilerplate y scaffolding]] — lo que se mide
- [[Deuda técnica]] — el acumulador que la variable dependiente busca reducir
