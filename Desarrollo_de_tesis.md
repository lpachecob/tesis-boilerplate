| **UNIVERSIDAD NACIONAL DE PIURA** |
| --- |
| **Facultad de Ingeniería Industrial** |
| **Escuela Profesional de Ingeniería Informática** |
|  |
|  |  |  |
|  |
| **PROYECTO DE TESIS** |
|  |
| **IMPLEMENTACIÓN DE UN FRAMEWORK BASADO EN DDD-LIVIANO CON AUTOGENERACIÓN DE ENDPOINTS PARA REDUCIR EL BOILERPLATE EN APIS REST EN 2026** |
|  |
| **Presentado por:** |
|  |
| **Luis Ernesto Pacheco Brophy** |
|  |
| **Asesor** |
|  |
| **-** |
|  |
| **Línea de investigación: Computación e Informática** |
|  |
| **Sub línea de investigación: Sistemas Automáticos de control** |
|  |
| **PIURA - PERÚ** |
|  |
| **2026** |

| **UNIVERSIDAD NACIONAL DE PIURA** |
| --- |
| **Facultad de Ingeniería Industrial** |
| **Escuela Profesional de Ingeniería Informática** |
|  |
|  |  |  |
|  |
|  |
| **IMPLEMENTACIÓN DE UN FRAMEWORK BASADO EN DDD-LIVIANO CON AUTOGENERACIÓN DE ENDPOINTS PARA REDUCIR EL BOILERPLATE EN APIS REST EN 2026** |
|  |
| **Línea de investigación: Computación e Informática** |
|  |
| **Sub línea de investigación: Sistemas Automáticos de control** |
|  |
| **Pacheco Brophy Luis Ernesto** |
|  |
| **Piura, ****Perú** |

- DECLARACIÓN JURADA DE ORIGINALIDAD DE LA TESIS

Yo: Luis Ernesto Pacheco Brophy, identificado con DNI N°. 72578726, Bachiller de Escuela Profesional de Ingeniería Informática, de la Facultad de Ingeniería Industrial domiciliado calle en: Miguel Grau 1591, Distrito. Sullana, Provincia. Sullana, Departamento. Piura, Email: lpachecoby@gmail.com y del Celular: 969677248.

**DECLARO BAJO JURAMENTO**: que la tesis que presento es original e inédita, no siendo copia parcial ni total de una tesis desarrollada, y/o realizada en el Perú o en el Extranjero, en caso contrario de resultar falsa la información que proporciono, me sujeto a los alcances de lo establecido en el Art. N° 411, del código Penal concordante con el Art. 32º de la Ley Nº 27444, y Ley del Procedimiento Administrativo General y las Normas Legales de Protección a los Derechos de Autor.

En fe de lo cual firmo la presente.

Piura, _______ de _____________________ del 2026.

……………………………………..

DNI NO………………………… 

**Artículo 411.- El que, en un procedimiento administrativo, hace una falsa declaración en relación con hechos o circunstancias que le corresponde probar, violando la presunción de veracidad establecida por ley, será reprimido con pena privativa de libertad no menor de uno ni mayor de cuatro años.**

**Art. 4. Inciso 4.12 del Reglamento del Registro Nacional de Trabajos de Investigación para optar grados académicos y ****titulos**** profesionales-RENATI Resolución de Consejo Directivo ****Nº**** 033-2016-SUNEDU/CD**

| **ELABORO** | **REVISÓ** | **APROBO** | **COPIA CONTROLADA** |
| --- | --- | --- | --- |
| VICERRECTORADO DE INVESTIGACIÓN | COMISIÓN ACADÉMICA | CONSEJO UNIVERSITARIO | NO |

Hoja de firmas del jurado, con el título de la tesis

Acta de sustentación original escaneada e impresa (después de la sustentación)

Dedicatoria

Agradecimientos

**ÍNDICE**** ****GENERAL**

	DECLARACIÓN JURADA DE ORIGINALIDAD DE LA TESIS	3

	RESUMEN	11

	ABSTRACТ	12

	INTRODUCCIÓN	13

		I.	Capitulo I: Aspectos de la problemática	14

		1.1.	Descripción de la realidad problemática	14

		1.2.	FORMULACIÓN DEL PROBLEMA DE INVESTIGACIÓN	17

		1.2.1.	Problema General	17

		1.2.2.	Problemas Específicos	17

		1.3.	JUSTIFICACIÓN E IMPORTANCIA DE LA INVESTIGACIÓN	17

		1.4.	OBJETIVOS	18

		1.4.1.	Objetivo General	18

		1.4.2.	Objetivos Específicos	18

		1.5.	DELIMITACIÓN DE LA INVESTIGACIÓN	18

		II.	MARCO TEÓRICO	19

		2.1.	ANTECEDENTES DE LA INVESTIGACIÓN	19

		2.2.	BASES TEÓRICAS	21

		2.2.1.	Reducción del código boilerplate en APIs REST	21

		2.2.2.	Implementación de un framework basado en DDD-liviano con autogeneración de endpoints	23

		2.3.	GLOSARIO DE TÉRMINOS BÁSICOS	24

		2.4.	HIPÓTESIS	29

		2.4.1.	Hipótesis General	29

		2.4.2.	Hipótesis Especificas	29

		2.5.	DEFINICIÓN Y OPERACIONALIZACIÓN DE VARIABLES	29

		2.5.1.	Variable independiente: Framework basado en DDD-liviano con autogeneración de endpoints	29

		2.5.2.	Variable dependiente: Reducción del código boilerplate en APIs REST	30

		III.	MARCO METODOLÓGICO	31

		3.1.	ENFOQUE	31

		3.2.	DISEÑO	31

		3.3.	NIVEL	32

		3.4.	TIPO	32

		3.5.	SUJETOS DE LA INVESTIGACIÓN	32

		3.5.1.	Universo	32

		3.5.2.	Población	33

		3.5.3.	Muestra	33

		3.6.	MÉTODOS Y PROCEDIMIENTOS	33

		3.6.1.	Métodos	33

		3.6.2.	Procedimientos	34

		3.7.	TÉCNICAS E INSTRUMENTOS	37

		3.7.1.	Técnicas	37

		3.7.2.	Instrumentos	37

		3.7.3.	Confiabilidad y validez de los instrumentos	37

		3.8.	ASPECTOS ÉTICOS	38

		IV.	ASPECTOS ADMINISTRATIVOS	39

		4.1.	CRONOGRAMA DE EJECUCIÓN	39

		4.2.	PRESUPUESTO	39

		4.3.	FINANCIAMIENTO	40

		V.	DESARROLLO DE LA SOLUCIÓN	40

		VI.	REFERENCIAS BIBLIOGRÁFICAS	48

	ANEXOS	50

	ANEXO 1 - FORMATO N°3: MATRIZ BÁSICA DE CONSISTENCIA	50

	ANEXO 2 - FORMATO N°4 MATRIZ DE OPERACIONALIZACIÓN DE LAS VARIABLES	51

	ANEXO 3 - FORMATO N°5: MATRIZ GENERAL DE CONSISTENCIA.	52

	ANEXO 4 - INSTRUMENTOS DE RECOLECCIÓN DE DATOS	53

	Instrumento N° 1: Ficha de análisis de código (checklist de componentes boilerplate)	53

	Instrumento N° 2: Guía de observación y lista de cotejo métrico	53

	Instrumento N° 3: Bitácora cronométrica (registro de tiempos)	53

	Instrumento N° 4: Cuestionario de percepción a desarrolladores (Escala Likert)	54

	Instrumento N° 5: Lista de cotejo de buenas prácticas de codificación	54

	ANEXO 5 - Informe de validez y confiabilidad de los instrumentos	55

	ANEXO 6 - REPORTE DE SIMILITUD TURNITIN	56

**Índice de tablas**

	**Tabla 1: Fases del procedimiento**	34

	**Tabla 2: Cronograma de Ejecución**	39

	**Tabla 3: Presupuesto de la investigación**	39

	**Tabla 4: Modelos de metadatos**	42

**Índice de Ilustraciones**

	**Ilustración 1** - Fases del procedimiento	35

	**Ilustración 2** - Arquitectura general de Boilerfree: del front controller a la base de datos.	41

	**Ilustración 3** - Flujo de datos: Del lenguaje de dominio (DSL) al entorno de ejecución (runtime).	42

	**Ilustración 4** - Ciclo de vida de una petición HTTP a través del kernel.	44

	**Ilustración 5** - Flujo de ejecución del comando de optimización de metadatos.	45

	**Ilustración 6** - Máquina de estados y ciclo de vida del caché de metadatos.	45

	**Ilustración 7** - Portada del reporte de similitud	56

	**Ilustración 8 **- Reporte de similitud porcentaje	56

**Índice de ****Anexos**

	ANEXO 1 - FORMATO N°3: MATRIZ BÁSICA DE CONSISTENCIA	50

	ANEXO 2 - FORMATO N°4 MATRIZ DE OPERACIONALIZACIÓN DE LAS VARIABLES	51

	ANEXO 3 - FORMATO N°5: MATRIZ GENERAL DE CONSISTENCIA.	52

	ANEXO 4 - INSTRUMENTOS DE RECOLECCIÓN DE DATOS	53

	ANEXO 5 - Informe de validez y confiabilidad de los instrumentos	55

	ANEXO 6 - REPORTE DE SIMILITUD TURNITIN	56

Capitulo I: Aspectos de la problemática

Descripción de la realidad problemática 

La presente investigación se alinea con el **noveno ODS (Industria, Innovación e Infraestructura)** al proponer una herramienta que fortalece la capacidad tecnológica y la innovación en el desarrollo de software. Asimismo, contribuye al **octavo ODS (Trabajo Decente y Crecimiento Económico)** al optimizar la productividad mediante la **automatización de tareas repetitivas**, lo que permite que el desarrollo de APIs REST sea más eficiente y que la experiencia de desarrollo se enfoque en soluciones de valor en lugar de en código estructural.

Tal como señalan Karlsson et al. (2024), investigadores de Mälardalen University y Asea Brown Boveri, ambas en Västeras, Suecia, la tecnología web es un medio común para que los sistemas expongan funcionalidad a los clientes, usualmente siguiendo el **estilo arquitectónico REST** (Fielding, 2000). Este predominio se ve respaldado por los hallazgos de Peldszus et al. (2026), investigadores de la Universidad de Bochum en Alemania y la IT University of Copenhagen en Dinamarca, quienes documentan que esta arquitectura ya concentraba el **82****% ****de todas las ****APIs**** públicas en 2017** y ascendió a **24.471 ****APIs**** registradas en 2022**. Este proceso arrastra un problema estructural ampliamente reconocido en la ingeniería de software: el denominado **código ****boilerplate**. Peldszus et al. (2026) documentan que el **62****% ****de las ****APIs**** REST** exponen entre 11 y 100 operaciones y que su usabilidad se ve afectada por la inconsistencia de nombres y usos entre sus partes. En la presente investigación, la **repetición de patrones estructurales predecibles**, con cada operación replicando las mismas estructuras, se identifica como uno de los principales factores que deterioran la usabilidad y la productividad del desarrollador.

A nivel mundial, la evidencia cuantitativa de este problema es contundente. En Estados Unidos, Gnanasambandam et al. (2023) sostienen que las empresas tecnológicas líderes aspiran a que sus desarrolladores dediquen hasta el **70****% ****de su tiempo** a actividades de *inner** **loop* (codificar, construir y probar). En cambio, califican como tareas necesarias, pero generalmente poco satisfactorias (*generally** **unsatisfying** chores*) las de *outer** **loop* (integración, pruebas de integración, release, despliegue, seguridad y cumplimiento, y reuniones), que comprenden el esfuerzo restante y se centran mayormente en actividades de **bajo valor añadido**.

Esta carga de trabajo redundante tiene un impacto directo en la **salud laboral y la capacidad creativa**. Según la investigación de Ma et al. (2024), investigadores de Duke University y Vanderbilt University en Estados Unidos, las interrupciones externas, como las notificaciones en pantalla o las interrupciones presenciales, afectan el flujo de resolución de problemas complejos. La presente investigación extiende esta conclusión a la **transcripción repetitiva de código estructural**, cuyo efecto es análogo: alternar entre la escritura creativa de reglas de negocio y el código mecánico produce un **agotamiento innecesario** en el desarrollador. Esta tendencia se ratifica en los informes de la plataforma Stack Overflow, con sede en Estados Unidos, cuyo *Developer** Survey 2024* (Stack Overflow, 2024) identificó la **deuda técnica** como la principal frustración laboral del **63****% **de los desarrolladores profesionales, con la cantidad de deuda técnica concentrando el **62,4****% **de las respuestas. Por su parte, el reciente *Stack **Overflow** **Developer** Survey 2025* (Stack Overflow, 2025) señala que la principal frustración declarada por el **66****% **de los desarrolladores son las soluciones de IA que están casi bien, pero no del todo (*AI **solutions** **that** are **almost** **right**, **but** **not** quite*), cuya carga de verificación y depuración intensifica precisamente el trabajo mecánico descrito.

Paradójicamente, el auge de la **Inteligencia Artificial Generativa** ha intensificado esta problemática. Investigaciones de Harding & Kloster (2024) en GitClear, empresa de análisis de software en Estados Unidos, revelan que el uso de asistentes de codificación de empresas como OpenAI, Google y Anthropic ha provocado un incremento en los **bloques de código duplicados** (*copy**/**pasted** **code*) en proporción a las líneas actualizadas, eliminadas o movidas. Además, proyectan para 2024 una **duplicación del *****code****** ******churn*** (el porcentaje de líneas revertidas o actualizadas menos de dos semanas después de ser escritas) respecto de la línea base previa a la IA de 2021, fenómeno denominado **entropía de código**. Lejos de simplificar el desarrollo, estas herramientas tienden a masificar la creación de estructuras predecibles, inyectando una deuda técnica que, según el reciente reporte de DORA & Google Cloud (2024) en Estados Unidos, **reduce la estabilidad de la entrega en un 7,2 %**. En la misma línea, la investigación de Peng et al. (2023) en Microsoft Research, realizada en Estados Unidos, ratifica esta premisa al demostrar que la asistencia de GitHub Copilot **incrementó la velocidad de desarrollo en un 55,8****% **en una tarea de implementación (servidor HTTP en JavaScript), lo que subraya la magnitud del tiempo que se pierde en procesos mecánicos.

A nivel nacional, la generación manual de código repetitivo o *boilerplate* en el desarrollo de capas de persistencia y servicios web se ha consolidado como una **brecha crítica** que compromete la competitividad del sector tecnológico peruano. En Lima, Chavez Chavez & Wong Portillo (2022), en la Revista Peruana de Computación y Sistemas de la Universidad Nacional Mayor de San Marcos, identificaron que un gran porcentaje del desarrollo de API REST es repetitivo (operaciones CRUD, generación de reportes, búsquedas típicas en una base de datos, pruebas unitarias y configuraciones) y que esa repetición genera **pérdidas de tiempo y dinero**. Esto evidencia que una parte sustancial del esfuerzo técnico se destina a reproducir código estructural que no aporta lógica de negocio diferencial. La naturaleza mecánica de este proceso, donde el desarrollador replica patrones predecibles en cada nueva entidad o módulo, constituye la **definición operativa del problema de ****boilerplate**: esfuerzo técnico elevado, valor agregado nulo. Bajo esta misma línea, aunque orientada a la gestión del conocimiento, Campos Salcedo & Reyes Huamán, (2025), en la Revista Peruana de Computación y Sistemas de la Universidad Nacional Mayor de San Marcos en Lima, advierten que la ausencia de modelos tecnológicos estandarizados dificulta capturar, organizar y compartir el conocimiento técnico en las organizaciones (modelo SECI), lo que compromete la **calidad y la mantenibilidad** de los sistemas de información empresariales.

La magnitud del problema se hace aún más evidente al analizar el impacto directo del boilerplate sobre los equipos de desarrollo. En Trujillo, Vasquez Pari, (2025), en la Universidad Privada Antenor Orrego, cuantificó sobre una muestra de 30 proyectos de una empresa desarrolladora de software que el uso de herramientas de IA **reduce el esfuerzo de ejecución en un 73,23 %**, una magnitud que revela cuánto del esfuerzo técnico disponible queda atrapado en la reproducción mecánica de estructuras predecibles en lugar de destinarse a la lógica propia del negocio. Este escenario se agrava con Pizarro Romero & Paredes Orihuela (2025), en la Universidad Tecnológica del Perú con sede en Lima, quienes documentaron en una empresa limeña que el desarrollo manual de un proyecto requirió **9 horas frente a las 4 horas** con asistencia estructurada (**55,6****% ****menos de tiempo de desarrollo**), con un incremento del **12,27****% **en las líneas libres de errores y del **78,38****% **en la efectividad de las pruebas unitarias.

Desde la perspectiva arquitectónica, el boilerplate representa además un **riesgo de inconsistencia sistémica**. Trebejo Loayza (2023), en la Universidad Nacional Mayor de San Marcos en Lima, concluyó que la generación de código a partir del modelo del dominio reduce el tiempo de esfuerzo del diseño de la arquitectura a **26,5 minutos por participante**, frente a las varias horas del diseño manual, y facilita la migración de sistemas legados. En la misma dirección, Bobadilla Chara, (2022), en la Universidad Católica de Santa María en Arequipa, reportó que el sistema ERP universitario se había vuelto inmantenible y que su refactorización mediante un framework de microservicios mejoró la mantenibilidad y escalabilidad del sistema.

El problema del boilerplate no se restringe a las grandes urbes del país. Villanueva Campos, (2024), en la Universidad Señor de Sipán en Pimentel, Lambayeque, advirtió que la carencia de software de control estandarizado limita la capacidad de respuesta del sector empresarial regional ante entornos dinámicos y competitivos, mientras que Cosme Escalera & Quispe Cansaya (2024), en la Universidad Nacional del Altiplano en Puno, demostraron en la empresa local Group de Mercado (Juliaca) que una arquitectura de microservicios con Kubernetes mejora significativamente las métricas de rendimiento, disponibilidad y tiempo de respuesta de las aplicaciones web frente a los modelos monolíticos. El conjunto de estas evidencias traza un patrón inequívoco a escala nacional: la escritura manual de código boilerplate en proyectos de backend representa un **cuello de botella transversal a todas las regiones del país**, y su eliminación mediante herramientas de generación automática de código constituye una **necesidad técnica urgente** para el desarrollo tecnológico peruano.

En la Región Piura, **no se han identificado trabajos de investigación locales** que aborden directamente el problema del código boilerplate en APIs REST o que propongan frameworks de autogeneración de endpoints bajo el paradigma DDD. Esta búsqueda se realizó en los repositorios de las universidades de la región: el Repositorio Institucional Digital de la Universidad Nacional de Piura (repositorio.unp.edu.pe), el Repositorio PIRHUA de la Universidad de Piura (pirhua.udep.edu.pe), el Repositorio Institucional de la Universidad César Vallejo sede Piura (repositorio.ucv.edu.pe) y el Repositorio Institucional de la Universidad Tecnológica del Perú sede Piura (repositorio.utp.edu.pe), así como en el Repositorio Nacional Digital de Ciencia, Tecnología e Innovación de Acceso Abierto ALICIA del CONCYTEC (alicia.concytec.gob.pe). Esta ausencia de producción científica local contrasta con la realidad nacional, donde investigaciones recientes han cuantificado el impacto del código repetitivo: en Trujillo se ha registrado que el uso de tecnologías de IA reduce el esfuerzo de ejecución del desarrollo en **73,23****%**** **(Vasquez Pari, 2025), y en Lima se ha documentado que gran parte del desarrollo de APIs REST es repetitivo y que esa repetición genera pérdidas de tiempo y dinero (Chavez Chavez & Wong Portillo, 2022).

En el contexto específico de Piura, esta brecha tecnológica representa una **oportunidad de investigación**. Los equipos de desarrollo locales, tanto en empresas de software como en proyectos académicos de la Universidad Nacional de Piura y la Universidad de Piura, continúan escribiendo código estructural de forma manual, recurso por recurso, sin acceso a herramientas estandarizadas que automaticen esta capa repetitiva. La falta de un **framework DDD liviano** adaptado al contexto regional prolonga los ciclos de desarrollo, posterga la implementación de la lógica de negocio y acumula deuda técnica. Este vacío constituye la **problemática concreta** que aborda la presente investigación.

El problema se manifiesta en el desarrollo de APIs REST. Al iniciar un nuevo recurso del dominio, el desarrollador debe escribir manualmente los mismos artefactos una y otra vez: **controlador, servicio, repositorio, entidad, DTOs de entrada y salida, mapeadores y configuración de rutas**. Esta repetición sistemática de código estructural, y no de lógica de negocio, consume tiempo de desarrollo sin aportar valor diferencial al proyecto. Cada uno de estos artefactos sigue patrones predecibles: el controlador implementa los métodos CRUD estándar (GET, POST, PUT, DELETE); el servicio encapsula la lógica de negocio básica; el repositorio define las operaciones de acceso a datos; los DTOs estructuran los datos de entrada y salida con validaciones similares; los mapeadores copian campos entre capas; y las rutas conectan los endpoints a los controladores. Ninguno de estos elementos contiene lógica específica del dominio: son infraestructuras necesarias que se replican idénticas para cada nueva entidad.

Esta repetición sistemática genera una **carga operativa significativa**. Por cada recurso del dominio se requieren **entre cinco y ocho artefactos** con estructuras idénticas o muy similares. En un sistema con veinte entidades de dominio, esto representa **hasta ciento sesenta artefactos repetitivos** que deben escribirse manualmente antes de poder concentrar esfuerzos en las reglas de negocio que realmente distinguen al producto. La escritura de estos artefactos consume las primeras iteraciones del ciclo de desarrollo y posterga la implementación de la funcionalidad propia del negocio.

FORMULACIÓN DEL PROBLEMA DE INVESTIGACIÓN

Problema General

¿En qué medida la implementación de un framework basado en DDD-liviano con autogeneración de endpoints reduce el código boilerplate en el desarrollo de APIs REST?

Problemas Específicos

- ¿Cuál es el nivel actual de código boilerplate generado durante el desarrollo manual de APIs REST siguiendo el paradigma DDD?

- ¿Qué componentes del ciclo de desarrollo de una API REST (controladores, servicios, repositorios, DTOs y mappers) presentan mayor replicación estructural y pueden ser autogenerados a partir del modelo de dominio?

- ¿En qué porcentaje se reduce el tiempo de desarrollo y las líneas de código repetitivas, y cuál es el nivel de calidad del código generado por el framework en comparación con el desarrollo manual?

- ¿Es factible la implementación del framework en un escenario real de desarrollo de APIs REST?

JUSTIFICACIÓN E IMPORTANCIA DE LA INVESTIGACIÓN

**Justificación práctica.** El código boilerplate representa un costo real y cuantificable en los proyectos de software. La automatización de estas estructuras repetitivas reduce tiempos de entrega, disminuye la probabilidad de errores derivados de la transcripción manual y libera la capacidad cognitiva del desarrollador para concentrarse en la lógica de negocio. El framework propuesto aportará una solución concreta a equipos de desarrollo que inician proyectos backend basados en DDD y necesitan reducir el tiempo de scaffolding inicial, con impacto directo en la productividad y en la calidad del producto final.

**Justificación teórica.** La investigación contribuye al cuerpo de conocimiento existente sobre generación de código, arquitecturas dirigidas por modelos y aplicación del DDD en entornos ligeros. Özkan et al. (2025) evidencian que el DDD puede emplearse para mejorar la calidad del código, potenciar el proceso de construcción del software y proporcionar soluciones más completas para el modelado del dominio y la generación de software. Esta investigación extiende ese conocimiento al ámbito específico de los frameworks de autogeneración de endpoints REST en contextos de DDD-liviano.

**Justificación tecnológica.** El auge del desarrollo de microservicios y la proliferación de APIs REST hacen indispensable contar con herramientas que aceleren el ciclo de desarrollo sin sacrificar la calidad arquitectónica. La propuesta de un framework basado en DDD-liviano se alinea con las tendencias actuales de automatización en el desarrollo backend y representa un aporte tecnológico para la industria de software regional.

**Justificación social.** Al reducir el tiempo destinado a código repetitivo, los desarrolladores pueden orientar su esfuerzo hacia la resolución de problemas de mayor valor para la organización y la sociedad, contribuyendo a un ambiente de trabajo más satisfactorio y sostenible, lo cual incide positivamente en los indicadores de bienestar laboral del sector tecnológico.

OBJETIVOS

Objetivo General

Diseñar e implementar un framework basado en DDD-liviano con autogeneración de endpoints que reduzca el código boilerplate en el desarrollo de APIs REST.

Objetivos Específicos

- Analizar y cuantificar el código boilerplate presente en el desarrollo convencional de APIs REST bajo el paradigma DDD, identificando los componentes con mayor nivel de replicación estructural.

- Diseñar la arquitectura del framework, definiendo los mecanismos de autogeneración de controladores, servicios, repositorios, DTOs y mappers a partir del modelo de dominio.

- Implementar el framework con sus módulos de autogeneración de endpoints y validarlo en un escenario de desarrollo real.

- Evaluar la reducción del código boilerplate, el tiempo de desarrollo y la calidad del código generado mediante comparación controlada con el desarrollo manual.

DELIMITACIÓN DE LA INVESTIGACIÓN

**Delimitación temática.** La investigación se circunscribe a la implementación de un framework de backend orientado a la autogeneración de endpoints REST bajo el paradigma DDD en su forma liviana (*Lightweight** DDD*). No abarca el desarrollo de interfaces de usuario, la integración con sistemas externos de terceros ni la gestión de infraestructura de despliegue.

**Delimitación espacial.** La investigación se desarrollará en el ámbito de la Universidad Nacional de Piura. La validación del framework se realizará mediante casos de desarrollo representativos del contexto de los equipos de software de la región Piura.

**Delimitación temporal.** El estudio comprende el período académico 2025–2026.

**Delimitación tecnológica.** El framework será implementado para un ecosistema de backend específico bajo el lenguaje PHP, y su validación se realizará sobre APIs REST con base de datos relacional.

**Delimitación económica.** La investigación se ejecutará con un presupuesto estimado de S/ 3,603.00 y será autofinanciada por el tesista. Este monto comprende el valor de los equipos propios, los materiales y los servicios requeridos durante los cuatro meses de ejecución. El aporte de la Universidad Nacional de Piura mediante asesoría académica, ambientes, laboratorios y recursos bibliográficos se considerará no monetario y no generará un costo adicional para el investigador.

MARCO TEÓRICO

ANTECEDENTES DE LA INVESTIGACIÓN

**Özkan et al. ****(****2025)**, en su revisión sistemática titulada *Domain-**driven** **design** in software **development**: A **systematic** **literature** **review** **on** **implementation**, **challenges**, **effectiveness*, tuvieron como objetivo analizar la implementación, los desafíos y la efectividad del DDD en el desarrollo de software. La metodología consistió en una revisión sistemática de **36 estudios**. Los resultados confirman que el DDD se adopta cada vez más en microservicios, pero persisten dos problemas: la **falta de evaluaciones empíricas rigurosas** y la **escasez de herramientas de apoyo** para los desarrolladores. Concluyen que se necesitan más herramientas que automaticen la infraestructura DDD. Esta conclusión es clave para la presente investigación, ya que sustenta directamente los **objetivos 1, 2 y 4**: cuantificar el boilerplate, diseñar una arquitectura de autogeneración y evaluar su impacto.

**Gurgul et al. ****(****2026)**, en su estudio *The **state** **of** generative AI in software **development**: **Insights** **from** **literature** and a **developer** **survey*, tuvieron como objetivo evaluar el impacto de la IA generativa en la productividad del desarrollo de software. La metodología combinó una revisión sistemática con una encuesta a **65 desarrolladores**. Los resultados muestran que más del **70****% **de los profesionales reportan que la IA reduce al menos a la mitad el tiempo dedicado a código repetitivo, y que el **79****% **usa estas herramientas a diario. Sin embargo, identifican riesgos como la adopción acrítica de la IA, la erosión de habilidades y la acumulación de deuda técnica. Concluyen que se requiere un enfoque estructurado para automatizar tareas repetitivas sin generar código redundante. Estos hallazgos resultan útiles para el **objetivo 4**, al cuantificar el potencial de ahorro en tareas repetitivas y reforzar la necesidad de un framework estructurado.

**Alkazemi**** ****&**** Nour ****(****2025)**, en su artículo *XBoot**: A **rapid** and **instructional** **low-code** **generator** **for** Spring Boot **applications*, tuvieron como objetivo diseñar y evaluar un generador low-code que produzca aplicaciones Spring Boot completas. La metodología consistió en el desarrollo de XBoot, un generador que utiliza un DSL de menos de 50 líneas. Los resultados mostraron que genera entre **950 y 1.350 líneas de código** (entidades, controladores, servicios, seguridad) y reduce el tiempo de despliegue de **45–120 minutos** (manual) a solo **2–20 minutos**. Concluyen que los generadores automáticos de código son viables y altamente productivos. Esta arquitectura de generación automatizada es análoga a la que se plantea en el **objetivo específico 2**, y sus métricas sirven como referencia para el **objetivo específico 4**.

**Levezinho**** et al. ****(****2024)**, en su trabajo *Domain-**driven** **design** **representation** **of** **monolith** candidate **decompositions** **based** **on** **entity** **accesses*, tuvieron como objetivo extender la herramienta Mono2Micro para formalizar conceptos DDD a partir del análisis de un monolito. La metodología consistió en añadir la capacidad de representar Contextos Delimitados, Agregados y Entidades. Los resultados demuestran que es posible **traducir modelos de dominio en artefactos técnicos ejecutables**. Concluyen que la formalización de conceptos DDD facilita la evolución arquitectónica. Este enfoque se vincula con el **objetivo específico 2**, que busca definir mecanismos para transformar el modelo de dominio en controladores, servicios, repositorios, DTOs y mappers.

**Sadik et al. ****(****2023)**, en su estudio *Coding** **by** **design**: GPT-4 **empowers** agile **model** **driven** **development*, tuvieron como objetivo explorar la integración de GPT-4 con el Desarrollo Dirigido por Modelos (MDD). La metodología consistió en transformar diagramas UML en código Java y Python mediante GPT-4. Los resultados muestran que el código autogenerado se alinea perfectamente con los diagramas de secuencia. Concluyen que la combinación de IA generativa y MDD es viable para automatizar tareas repetitivas. A pesar de utilizar IA generativa en lugar de reflexión, su enfoque aporta pautas metodológicas de implementación y validación que resultan útiles para el **objetivo específico 3**.

**Trebejo Loayza ****(****2023)**, en su tesis de maestría *Herramienta para el modelado y generación de código de arquitecturas de software basadas en microservicios*, tuvo como objetivo desarrollar una herramienta web que genere código base para microservicios a partir de un modelo del dominio expresado con diagramas de clases UML. La metodología fue aplicada; el generador implementado (generator-springboot, basado en **Yeoman**) produce microservicios con Spring Boot. Los resultados mostraron un tiempo de esfuerzo de **26,5 minutos por participante** en la generación del código de la arquitectura, frente a las varias horas del diseño manual. Concluye que la herramienta facilita y agiliza el desarrollo de proyectos de software y la migración de sistemas legados. Este antecedente es fundamental para el **objetivo general** y para el **objetivo específico 2**, al confirmar la viabilidad de herramientas de autogeneración en el Perú.

**Bobadilla Chara ****(****2022)**, en su tesis de grado *Desarrollo de un framework con una arquitectura basada en microservicios para el UP-Grade del Sistema de Planificación de Recursos Empresariales de la UCSM*, tuvo como objetivo diseñar e implementar un framework de microservicios para modernizar un sistema ERP universitario. La metodología fue aplicada, con desarrollo incremental. El framework propuesto realizó la refactorización y mejora del ERP universitario, que se había vuelto inmantenible, mediante una arquitectura de microservicios (Go con interfaz en ReactJS). Los resultados mostraron una **mejora en la mantenibilidad y escalabilidad** del sistema. Concluye que un framework basado en microservicios facilita el mantenimiento y la modernización de sistemas heredados en entornos reales. Se alinea con los **objetivos específicos 2 y 3**, al demostrar cómo un framework puede estandarizar artefactos y facilitar el mantenimiento.

**Pizarro Romero ****&**** Paredes Orihuela ****(****2025)**, en su tesis de grado *Optimización del desarrollo de software con GitHub **Copilot**: Análisis comparativo de productividad y calidad en una empresa de Lima 2024*, tuvieron como objetivo comparar el desarrollo con y sin GitHub Copilot. La metodología fue un experimento controlado en una empresa limeña. Los resultados mostraron una **reducción del tiempo de desarrollo del 55,6****% **y un incremento del **12,27****% **en las líneas libres de errores, con una mejora del **78,38****% **en la efectividad de las pruebas unitarias. Concluyen que las herramientas de asistencia estructurada mejoran la productividad. Su diseño experimental controlado es análogo al que se plantea en el **objetivo específico 4** para evaluar la reducción de tiempo y la calidad del código generado.

**Vasquez Pari ****(****2025)**, en su tesis de maestría *Inteligencia artificial en la productividad de una empresa desarrolladora de software en la ciudad de Trujillo, 2025*, tuvo como objetivo determinar el impacto de la IA en la productividad del desarrollo de software en empresas trujillanas. La metodología fue cuantitativa correlacional, con un diseño longitudinal sobre una muestra intencional no probabilística de **30 proyectos** de una misma empresa: 15 desarrollados sin herramientas de IA (enero a julio de 2024) y 15 con ellas (agosto de 2024 a febrero de 2025). Los resultados indican que el uso de IA **reduce el esfuerzo de ejecución en 82,73 minutos, equivalente a una disminución del 73,23 %**, con efectos de −70,94% en Machine Learning, −90,72% en Automatización de Procesos y −63,55% en Sistemas Inteligentes. Concluye que la inteligencia artificial influye de manera directa y significativa en la productividad de la empresa desarrolladora de software. Este antecedente aporta directamente al **objetivo específico 1**, al proporcionar una línea base cuantificada del peso del boilerplate en el norte del Perú.

**Cosme Escalera ****&**** Quispe ****Cansaya**** (2024)**, en su tesis de grado *Arquitectura de software basada en microservicios para el desarrollo de aplicaciones web de la empresa Group de Mercado, Juliaca 2022*, tuvieron como objetivo mejorar los servicios web de la empresa Group de Mercado (áreas de ventas, marketing, inventario y almacén) mediante una arquitectura de microservicios. La metodología fue aplicada: la composición de microservicios se modeló con BPMN, el frontend se implementó con Vue.js, la seguridad con JWT y el despliegue se realizó sobre servidor PHP y Kubernetes. Los resultados mostraron que la arquitectura de microservicios **mejora significativamente las métricas de rendimiento, disponibilidad y tiempo de respuesta en un 100****% **frente a los modelos monolíticos. Concluyen que esta arquitectura mejora los servicios de la empresa y facilita su evolución. Este antecedente respalda el **objetivo general** y el **objetivo específico 2**, al subrayar la urgencia local de frameworks que automaticen el código repetitivo.

Se realizó una **búsqueda sistemática** en los repositorios institucionales de la Universidad Nacional de Piura (UNP), la Universidad de Piura (UDEP), la Universidad César Vallejo (sede Piura), la Universidad Tecnológica del Perú (sede Piura) y en el Repositorio Nacional ALICIA del CONCYTEC, abarcando el período **2021-2026**. No se encontraron tesis de pregrado ni artículos científicos que aborden directamente la autogeneración de endpoints REST, el diseño de frameworks basados en DDD liviano o la automatización de código boilerplate en el desarrollo backend. Este **vacío documental** confirma la originalidad de la presente investigación en el ámbito local de Piura y justifica la necesidad de generar nuevo conocimiento tecnológico aplicable a los equipos de desarrollo de la región.

BASES TEÓRICAS

Reducción del código boilerplate en APIs REST

**Fowler ****(****2002)** Menciona el término código boilerplate en el patrón *Two Step View*; su concepto equivalente es el ***plumbing*** o **plomería**: el código de infraestructura necesario para que el sistema funcione, pero que no expresa la lógica del dominio, y que resulta indispensable, repetitivo y fácil de estandarizar. En su obra *Patterns** **of** Enterprise **Application** **Architecture*, identifica que el **código de mapeo repetitivo es una señal de diseño deficiente** y que puede evitarse mediante generación de código o programación reflexiva (*Metadata** **Mapping*).

**Vasquez Pari (2025)** midió el efecto de la inteligencia artificial sobre el esfuerzo de ejecución en una empresa desarrolladora de software de la ciudad de Trujillo, con una muestra de **30 proyectos**. Con un modelo global apilado con bloqueo, encontró que el uso de IA **reduce el esfuerzo en 82,73 minutos, equivalente a una disminución del 73,23**, con efectos por dimensión de −70,94% (Machine Learning), −90,72% (Automatización de Procesos) y −63,55% (Sistemas Inteligentes).

**Alkazemi**** ****&**** Nour (2025)**, desde la perspectiva de los generadores low-code, definen el código boilerplate como las **secciones de código de infraestructura** (controladores, servicios, entidades y plantillas de interfaz, con la capa de acceso a datos resuelta mediante anotaciones como @Repository) que pueden generarse automáticamente a partir de un modelo abstracto. Demuestran que su reducción mediante herramientas como XBoot es viable: **menos de 50 líneas** de un lenguaje de dominio específico producen entre **950 y 1.350 líneas** de Java y HTML, con la seguridad y la documentación ya resueltas.

Dimensiones

**D1: Cuantificación del ****boilerplate**** **(Vasquez Pari, 2025). Esta dimensión hace referencia al peso relativo que el código repetitivo representa dentro del esfuerzo total de desarrollo. Vasquez Pari (2025) la cuantifica comparando la reducción del esfuerzo entre un grupo con IA y otro sin IA (30 proyectos), mientras que la identificación de los componentes con mayor nivel de replicación (controladores, DTOs, repositorios) corresponde al análisis estructural de la presente investigación. En conjunto, ambos enfoques permiten establecer una línea base sobre la magnitud del problema antes de aplicar cualquier solución de automatización.

**D2: Reducción de código** (cantidad) **Alkazemi**** ****&**** Nour ****(****2025)**. Esta dimensión se refiere a la disminución medible de líneas de código que el desarrollador debe escribir manualmente cuando se introduce un mecanismo de generación automática. Alkazemi & Nour (2025) la operacionalizan comparando la cantidad de líneas de especificación necesarias frente a las líneas de código de infraestructura producidas, demostrando en los dos casos de estudio que un generador low-code puede reducir drásticamente el esfuerzo manual sin comprometer la funcionalidad.

**D3: Reducción de tiempo de desarrollo** **(Pizarro Romero ****&**** Paredes Orihuela, 2025; Gurgul et al., 2026).** Esta dimensión aborda el ahorro temporal que experimenta un desarrollador al utilizar herramientas de asistencia o automatización frente al desarrollo manual. Pizarro Romero & Paredes Orihuela (2025) la midieron mediante un experimento controlado comparando tiempos de codificación con y sin GitHub Copilot, mientras que Gurgul et al., (2026) la respaldan a través de una encuesta donde la mayoría de desarrolladores percibe una reducción de al menos la mitad del tiempo dedicado a código repetitivo.

**D4: Calidad del código generado**** (Sadik et al., 2023; ****Alkazemi**** y Nour, 2025).** Esta dimensión evalúa si el código producido automáticamente mantiene estándares aceptables de mantenibilidad, complejidad y ausencia de duplicación. Sadik et al. (2023) la abordan desde el enfoque de desarrollo dirigido por modelos, demostrando que la generación guiada por modelos produce código mantenible y de baja complejidad, mientras que Alkazemi & Nour (2025) describen el código generado por su herramienta como modular y mantenible, libre de errores estructurales y de seguridad comunes.

Bases teóricas

**Base teórica de D1 (Cuantificación del ****boilerplate****).** La medición de líneas de código (LOC) por componente es una métrica clásica para estimar el peso estructural de un sistema. Fowler (2002) identifica que el código de mapeo repetitivo es una señal de diseño deficiente y que puede evitarse mediante generación de código o programación reflexiva (*Metadata** **Mapping*); esa replicación es la que la presente investigación identifica concentrada en controladores, DTOs y repositorios por cada entidad del dominio. Vasquez Pari (2025) aporta una cuantificación local en una empresa de Trujillo, con una muestra de 30 proyectos, donde el uso de IA se asoció a una reducción del esfuerzo de ejecución del 73,23%. Para operacionalizar esta dimensión se utilizará una ficha de análisis de código tipo checklist que registre el LOC por componente, complementada con una herramienta de análisis estático (SonarQube/PMD) que calcule el porcentaje de código duplicado.

**Base teórica de D2 (Reducción de código-cantidad).** La comparación de líneas de código entre el desarrollo manual y el autogenerado permite cuantificar directamente el ahorro estructural logrado. Alkazemi & Nour (2025) demostraron con XBoot que un generador low-code puede producir entre 950 y 1.350 líneas de código de infraestructura a partir de menos de 50 líneas de especificación, y que las aplicaciones así generadas se desplegaron en 2 a 20 minutos, frente a los 45 a 120 minutos de la implementación manual. Para esta dimensión se aplicará una ficha de comparación pre-test/post-test que registre el porcentaje de reducción de LOC y el número de archivos/clases generados automáticamente, replicando el diseño de medición utilizado por dicho estudio.

**Base teórica de D3 (Reducción del tiempo de desarrollo).** El tiempo de desarrollo es un indicador directo de productividad. Gurgul et al. (2026) reportan que más del 70% de los desarrolladores percibe que las herramientas de IA reducen al menos a la mitad el tiempo dedicado a código repetitivo, mientras que Pizarro Romero y Paredes Orihuela (2025) demostraron experimentalmente una reducción del 55,6% del tiempo de desarrollo al usar GitHub Copilot. Esta dimensión se medirá mediante cronómetro/bitácora de registro de tiempos, comparando el desarrollo manual frente al asistido por el framework, en un diseño cuasi-experimental similar al propuesto por dichos autores.

**Base teórica de D4 (Calidad del código generado).** La calidad del código se evalúa habitualmente mediante el índice de mantenibilidad, la complejidad ciclomática y el porcentaje de duplicación. Sadik et al. (2023) demuestran que la generación guiada por modelos (MDD) produce código con alta mantenibilidad y baja complejidad, y Alkazemi y Nour (2025) valoran la modularidad y mantenibilidad del código generado por XBoot. Para esta dimensión se utilizará una herramienta de análisis estático (SonarQube) que mida errores/bugs y el porcentaje de cumplimiento de linting, complementada con una lista de cotejo de buenas prácticas y un cuestionario de percepción a desarrolladores (escala Likert), instrumento empleado por Pizarro Romero y Paredes Orihuela (2025) y Vasquez Pari (2025).

Implementación de un framework basado en DDD-liviano con autogeneración de endpoints

El framework propuesto en esta tesis adopta el modelo de dominio como núcleo del diseño, siguiendo a Evans (2003), y conserva los patrones tácticos del Domain-Driven Design (Aggregates, Repositories, Domain Services) como estructura de soporte para implementar el modelo de negocio. Evans (2003) advierte que un equipo con un proyecto simple que adopta el diseño guiado por el modelo completo enfrenta una curva de aprendizaje difícil, premisa de la cual esta tesis deriva su variante liviano: seleccionar solo los patrones esenciales para el alcance de una API REST.

En esta tesis, un framework se concibe como un conjunto de clases que colaboran para realizar una responsabilidad común en un dominio específico, automatizando las tareas repetitivas el código de infraestructura que Fowler (2002) describe como *plumbing* para permitir al desarrollador concentrarse en la lógica diferenciadora.

Alkazemi y Nour (2025) definen un generador low-code como una herramienta que, a partir de un modelo abstracto (un DSL), produce automáticamente el código de infraestructura (controladores, servicios, entidades y plantillas de interfaz, con la capa de acceso a datos resuelta mediante anotaciones como @Repository), reduciendo drásticamente el tiempo de generación y despliegue. Este concepto se aplica directamente a la autogeneración de endpoints REST.

Un framework de autogeneración se define en esta tesis como aquel que, a partir de un modelo del dominio, genera automáticamente los artefactos de la capa de aplicación e infraestructura, eliminando la necesidad de escribir código estructural repetitivo. Trebejo Loayza (2023) demuestra la viabilidad de este enfoque con una herramienta web que modela arquitecturas de microservicios guiadas por el dominio y genera el código de infraestructura mediante el generador Yeoman generator-springboot sobre Spring Boot.

Dimensiones

**D1: Cuantificación del ****boilerplate** (Vasquez Pari, 2025). Aunque esta dimensión también aparece en la variable dependiente, en el contexto del framework hace referencia a la identificación previa de los componentes con mayor nivel de replicación que el framework deberá atacar. La presente investigación identifica que controladores, DTOs y repositorios son los artefactos más replicados en DDD, mientras que Vasquez Pari (2025) aporta la magnitud cuantitativa del problema en el contexto peruano, sirviendo como insumo de diseño para el framework.

**D2: Diseño arquitectónico del framework** (Evans, 2003; Levezinho et al., 2024). Esta dimensión se refiere a la definición formal de los mecanismos mediante los cuales el framework transforma el modelo de dominio en artefactos técnicos. Evans (2003) la sustenta al establecer que un framework de dominio debe encapsular los patrones tácticos esenciales del DDD, mientras que Levezinho et al. (2024) demuestran empíricamente que es posible formalizar estos conceptos y traducirlos en artefactos ejecutables a partir del análisis del modelo de dominio.

Bases teóricas

**Base teórica de D1 (Cuantificación del ****boilerplate****).** Esta dimensión, aplicada al diseño del framework, parte de la necesidad de identificar qué componentes presentan mayor nivel de replicación estructural antes de automatizarlos. La presente investigación identifica que en DDD la replicación se concentra en controladores, DTOs y repositorios por cada entidad del dominio, mientras que Vasquez Pari (2025) cuantifica, en una empresa de Trujillo con 30 proyectos evaluados, una reducción del esfuerzo de ejecución del 73,23% atribuida al uso de IA. Esta evidencia justifica que el framework priorice la autogeneración precisamente de estos componentes. Para esta dimensión se utilizará una ficha de análisis de código (checklist de componentes boilerplate) y una herramienta de análisis estático (SonarQube/PMD) para medir el porcentaje de duplicación.

**Base teórica de D2 (Diseño arquitectónico del framework).** El diseño de mecanismos de autogeneración requiere definir reglas formales de transformación entre el modelo de dominio y los artefactos técnicos. Evans (2003) establece que un framework de dominio debe encapsular los patrones tácticos esenciales (Aggregates, Repositories, Domain Services), mientras que Levezinho et al. (2024) demuestran que es posible formalizar estos conceptos a partir del análisis estructural de un sistema, traduciéndolos en artefactos ejecutables. Para medir esta dimensión se empleará una matriz de trazabilidad que vincule cada elemento del modelo de dominio con su artefacto generado, y una lista de verificación de cumplimiento de patrones DDD, instrumento análogo al utilizado por Trebejo Loayza (2023) para validar la cobertura de patrones en su herramienta de generación basada en DSL.

GLOSARIO DE TÉRMINOS BÁSICOS

**A**

**Agregado (****Aggregate****)**. Unidad táctica de consistencia del Domain-Driven Design que agrupa un conjunto de entidades y objetos de valor bajo una raíz (aggregate root), definiendo un límite transaccional explícito para las invariantes del dominio. Evans (2003) lo concibe como el patrón mediante el cual se encapsula la lógica invariante del modelo y se garantiza la integridad de las operaciones que afectan a objetos asociados. Özkan et al. (2025) describen el agregado como el concepto que encapsula entidades, objetos de valor y lógica de dominio, y como el punto principal de acceso y modificación de los datos dentro de límites definidos.

**API (****Application**** ****Programming**** ****Interface****)**. Conjunto de reglas, protocolos y definiciones que permiten la comunicación e interoperabilidad entre componentes de software heterogéneos. En la presente investigación, el término se circunscribe a las APIs web basadas en el estilo arquitectónico REST, que Karlsson et al. (2024) describen como un medio común para que los sistemas expongan funcionalidad a los clientes. Peldszus et al. (2026) documentan que esta arquitectura concentraba el 82% de las APIs públicas en 2017 y registró 24 471 APIs catalogadas en 2022, evidencia que sustenta su predominio como vehículo de integración.

**Análisis estático de código.** Técnica automatizada de evaluación de software que, sin ejecutar el programa, examina el código fuente para detectar defectos estilísticos, duplicaciones, vulnerabilidades y métricas de complejidad (líneas de código, complejidad ciclomática, índice de mantenibilidad). Pizarro Romero y Paredes Orihuela (2025) lo utilizan para comparar la calidad del código escrito manualmente frente al asistido por GitHub Copilot, lo que respalda su uso como instrumento de medición confiable en la presente investigación.

**B**

**Backend.** Capa de una aplicación de software encargada de la lógica de negocio, el acceso a datos y la exposición de servicios, en contraposición al frontend (capa de presentación). En el contexto del estudio, se refiere específicamente al backend de APIs REST construidas con PHP y gestionadas con Composer, donde se concentra el código estructural objeto de automatización. Trebejo Loayza (2023), en cambio, no emplea el término backend: su herramienta se estructura como una aplicación web con el patrón MVC y delega la generación del código al proyecto Yeoman generator-springboot.

**Bounded**** ****Context**** (Contexto Delimitado).** Límite explícito dentro del cual un modelo de dominio es válido y consistente; cada contexto delimita un lenguaje ubicado y un equipo responsable. Evans (2003) lo introduce como el patrón estratégico central del DDD para resolver la ambigüedad terminológica entre subdominios. Levezinho et al. (2024) demuestran que la formalización de bounded contexts a partir del análisis de accesos a entidades permite traducir el modelo de dominio en artefactos técnicos ejecutables.

**Boilerplate**** ****code****.** Código necesario para el funcionamiento del sistema pero que no expresa lógica de dominio, cuya escritura manual consume tiempo del desarrollador sin aportar valor diferencial. En la presente investigación se utiliza la metáfora de la plomería de una casa indispensable pero repetitiva y fácil de estandarizar como equivalente del término inglés *plumbing* que Fowler (2002) emplea para el código de infraestructura. En el contexto del DDD, la presente investigación lo identifica en la replicación de controladores, DTOs y repositorios por cada entidad. Vasquez Pari (2025) cuantifica, en una empresa desarrolladora de software de Trujillo con una muestra de 30 proyectos, una reducción del 73,23% en el esfuerzo de ejecución atribuida al uso de herramientas de inteligencia artificial).

**C**

**CLI (Command Line Interface).** Interfaz textual mediante la cual el desarrollador interactúa con un programa tecleando comandos en una terminal. En la investigación, el CLI del framework propuesto es el canal por el cual se invocan los comandos de autogeneración de artefactos. Alkazemi y Nour (2025) describen la invocación de XBoot desde la terminal mediante java -jar xboot.jar con el archivo XML del DSL como argumento, sin llegar a definirlo como una CLI.

DSL de menos de 50 líneas, mientras que Trebejo Loayza (2023) realiza la generación desde una aplicación web, no desde una interfaz de línea de comandos.

**CRUD (Create, Read, Update, Delete)**. Acrónimo de las cuatro operaciones básicas de persistencia que todo endpoint REST expone para una entidad del dominio: creación, lectura, actualización y eliminación. En la presente investigación, el CRUD se identifica como el patrón estructural cuya replicación sistemática por cada entidad genera el grueso del código repetitivo en proyectos DDD. Pizarro Romero y Paredes Orihuela (2025) comparan tres proyectos de desarrollo completos, cuya gestión incluye operaciones CRUD, en su experimento controlado sobre productividad del desarrollador.

**D**

**DDD (Domain-Driven Design).** Enfoque de diseño de software centrado en el modelo de dominio y el lenguaje ubicado, articulado por Evans (2003), cuyo subtítulo *Tackling** **Complexity** in **the** Heart **of** Software* condensa esa finalidad. Özkan et al. (2025), en una revisión sistemática de 36 estudios, confirman que el DDD se adopta crecientemente en arquitecturas de microservicios y concluyen que se requieren más evaluaciones empíricas y un mayor soporte de herramientas (p. ej., DSLs y herramientas de context mapping) para apoyar su implementación. Levezinho et al. (2024) lo aplican a la descomposición de monolitos, formalizando agregados y entidades como artefactos ejecutables.

**DDD-liviano (****Lightweight**** DDD).** Variante del Domain-Driven Design propuesta en esta tesis, que conserva únicamente los patrones tácticos esenciales (agregados, repositorios, servicios de dominio) y descarta la capa estratégica (bounded contexts, context maps, event sourcing, CQRS). La distinción entre ambas capas no es invención propia: Evans (2003) organiza su libro en torno a los bloques del diseño guiado por el modelo la capa táctica y al diseño estratégico, y Trebejo Loayza (2023) la recoge explícitamente al señalar que DDD se divide en diseño estratégico y diseño táctico, y ambos deben combinarse para alcanzar el éxito en la aportación de un sistema (Evans, 2015) (Trebejo Loayza, 2023, p. 57). La selección de solo la capa táctica es la propuesta de esta tesis y se apoya en dos premisas con respaldo en las fuentes: Evans (2003) advierte que un equipo con un proyecto simple que adopta el diseño guiado por el modelo completo enfrenta una curva de aprendizaje difícil, y la literatura de generación de código ya emplea el atributo de ligereza Alkazemi y Nour (2025) describen XBoot como a lightweight framework. En consecuencia, el término liviano se adopta como denominación propia para una variante acotada al contexto ya definido de una API REST, donde el contexto delimitado no requiere derivación.

**DSL (Domain-Specific ****Language****).** Lenguaje de propósito específico que expresa las entidades, atributos y reglas de un dominio concreto mediante una notación compacta y cercana al usuario. Alkazemi y Nour (2025) definen el DSL como el insumo mínimo (menos de 50 líneas en su caso) a partir del cual su generador XBoot produce entre 950 y 1.350 líneas de código de infraestructura. Trebejo Loayza (2023) utiliza un DSL basado en UML como entrada de su herramienta de modelado y generación de microservicios.

**E**

**Endpoint****.** Punto de conexión específico dentro de una API REST, identificado por una URL y un método HTTP (por ejemplo, GET /usuarios/{id}). Karlsson et al. (2024) describen los endpoints como las operaciones (*behaviours*) que una API expone lo que la API debe o no debe hacer mediante interacciones HTTP con sus clientes. Peldszus et al. (2026) reportan que el 62% de las APIs REST exponen entre 11 y 100 operaciones, cada una replicando las mismas estructuras, lo que justifica la autogeneración de endpoints propuesta en esta investigación.

**Entidad (****Entity****).** Objeto del dominio con identidad propia, distinguible a lo largo del tiempo y de los cambios de estado. Evans (2003) la distingue de los value objects por su identidad estable. Levezinho et al. (2024) formalizan las entidades como nodos de un grafo de accesos a partir del cual derivan agregados y contextos delimitados, demostrando que la noción es directamente traducible a artefactos técnicos.

**F**

**Framework.** Conjunto de clases, interfaces y convenciones que colaboran para resolver una responsabilidad común dentro de un dominio específico. En esta tesis, un framework se concibe como una estructura que automatiza las tareas repetitivas el código de infraestructura que Fowler (2002) describe como *plumbing* y permite al desarrollador concentrarse en la lógica diferenciadora. Evans (2003) añade la noción de framework de dominio al aplicarlo a los patrones tácticos del DDD. Bobadilla Chara (2022) y Trebejo Loayza (2023) lo aplican respectivamente al desarrollo de un framework de microservicios para un ERP universitario y a una herramienta de modelado y generación de código.

**H**

**HTTP (Hypertext Transfer Protocol)**. Protocolo de capa de aplicación base para la transferencia de información en la web, cuyos métodos estándar (GET, POST, PUT, DELETE) materializan las operaciones CRUD en una API REST. Karlsson et al. (2024) describen las operaciones CRUD de una API REST en términos de los métodos HTTP que las invocan, y Peldszus et al. (2026) lo utilizan como referencia para evaluar la usabilidad de las APIs REST desde la perspectiva del desarrollador.

**I**

**IoC**** (****Inversion**** ****of**** Control)**. Principio de diseño en el que el control del flujo de ejecución y de la resolución de dependencias se transfiere del código de aplicación al framework contenedor. En la presente investigación, la inyección de dependencias de Spring Boot constituye una implementación concreta de este principio; los autores revisados Fowler (2002) y Pizarro Romero y Paredes Orihuela (2025) no emplean el término en sus publicaciones.

**J**

**JSON (JavaScript Object Notation).** Formato ligero de intercambio de datos basado en texto, ampliamente utilizado en APIs REST para serializar la información entre cliente y servidor.

Jones et al. (2015), al especificar el estándar JWT, lo describen como un formato compacto de representación de claims (*compact **claims** **representation** **format*), empleado en esta investigación para la autenticación de las APIs REST generadas. Chavez Chavez y Wong Portillo (2022) lo adoptan como formato de salida predeterminado en su generador automático EasyRest.

**L**

**Lenguaje Ubicado (****Ubiquitous**** ****Language****).** Vocabulario compartido, riguroso y continuo entre desarrolladores y expertos del dominio, articulado por Evans (2003) como elemento fundacional del DDD. Özkan et al. (2025) describen el lenguaje ubicado como el lenguaje compartido que captura tanto los términos técnicos como los específicos del dominio.

**M**

**MDD (Model-****Driven**** ****Development****).** Paradigma de desarrollo de software donde el código se genera a partir de modelos abstractos del sistema (diagramas UML, DSLs u ontologías). Sadik et al. (2023) demuestran que la combinación de MDD con GPT-4 produce código autogenerado que se alinea perfectamente con los diagramas de secuencia, lo que respalda la viabilidad de la autogeneración guiada por el modelo de dominio en este trabajo.

**Middleware.** Capa de software que intercepta las peticiones HTTP antes de que lleguen al controlador, permitiendo ejecutar lógica transversal como autenticación, logging o validación global. Trebejo Loayza (2023), en cambio, no emplea el término middleware en su tesis. Alkazemi y Nour (2025) no incluyen middleware: XBoot genera entidades, servicios, controladores, plantillas de interfaz y configuración de seguridad.

**Migración (base de datos).** Archivo versionado que registra un cambio estructural en el esquema de la base de datos (creación, modificación o eliminación de tablas, columnas o índices). Trebejo Loayza (2023), en cambio, emplea migración para referirse a la migración de sistemas legados hacia microservicios, no a la generación de archivos de migración de base de datos.

**N**

**Namespace****.** Mecanismo de encapsulación de PHP (heredado de lenguajes como C# y Java) que agrupa clases, interfaces, funciones y constantes bajo un identificador jerárquico para prevenir conflictos de nombres. Trebejo Loayza (2023), en cambio, no emplea el término namespace en su tesis.

**P**

**PHP (PHP: Hypertext Preprocessor).** Lenguaje de programación de código abierto, interpretado y de propósito general, ampliamente empleado en el desarrollo backend web. Trebejo Loayza (2023), en cambio, no lo emplea: su pila declarada es C#/.NET o Java/Spring Boot, con generación de microservicios mediante generator-springboot (Yeoman).

**R**

**Reflexión / ****Metaprogramación**** (****Reflection****).** Capacidad de un programa para inspeccionar y modificar en tiempo de ejecución la estructura y el comportamiento de clases, métodos y atributos de otros programas. Trebejo Loayza (2023), en cambio, no la emplea: su generador trabaja sobre el modelo de dominio modelado con UML y produce el código mediante generator-springboot (Yeoman). Pizarro Romero y Paredes Orihuela (2025) muestran un uso análogo en asistentes de codificación como GitHub Copilot, basados en la introspección del contexto del código.

**Repositorio (****Repository****).** Patrón táctico del DDD que encapsula el acceso y la persistencia de un agregado, ofreciendo una interfaz de colección para el resto del dominio. Evans (2003) lo concibe como un mecanismo que encapsula el almacenamiento, la recuperación y la búsqueda de los agregados, aislando el modelo de dominio de los detalles de la capa de infraestructura. En la presente investigación, el repositorio se identifica como uno de los componentes más replicados manualmente en proyectos DDD, junto con controladores y DTOs.

**REST (****Representational**** State Transfer).** Estilo arquitectónico para sistemas distribuidos hipermedia propuesto por Fielding y sistematizado por la comunidad académica para el diseño de APIs web. Karlsson et al. (2024) señalan que la tecnología web es un medio común para que los sistemas expongan funcionalidad a los clientes, usualmente siguiendo este estilo arquitectónico, mientras que Peldszus et al. (2026) lo describen como el estilo arquitectónico dominante para la entrega de servicios web (p. 1) y ratifican su predominio a escala industrial: el 82% de las APIs registradas en 2017 sobre un total de 18.400, cifra que crece hasta 24.471 APIs en 2022.

**Router****.** Componente de un framework web responsable de analizar la URL de una petición HTTP entrante y direccionarla al método del controlador correspondiente. Trebejo Loayza (2023), en cambio, no emplea el término router en su tesis.

**S**

**Scaffolding****.** Conjunto de código estructural generado automáticamente al inicio de un proyecto o módulo, cuya única función es sustentar la aplicación sin contener lógica de negocio diferenciadora. Stack Overflow (2024) no define el término su única mención, the DevRel scaffolding, se refiere a la estructura de roles de relaciones con desarrolladores, no a código; lo que la encuesta sí reporta es que la **deuda técnica** es la principal frustración laboral de los desarrolladores profesionales, con un **63****% **de las respuestas. Harding y Kloster (2024) advierten que las herramientas de IA generativa han incrementado los bloques de código duplicado y el *code** **churn* en el código versionado, fenómeno que el framework de esta investigación busca revertir mediante una generación controlada y consistente.

**Servicio de Dominio (Domain Service).** Patrón táctico del DDD que encapsula lógica de negocio que no pertenece naturalmente a ninguna entidad ni value object específico. Evans (2003) lo introduce como mecanismo para mantener la cohesión del modelo. Özkan et al. (2025) lo listan entre los conceptos tácticos del DDD, junto con entidades, objetos de valor y agregados.

**U**

**URI (****Uniform**** ****Resource**** ****Identifier****).** Cadena compacta de caracteres que identifica un recurso dentro de una API REST, utilizada como ruta del endpoint. Peldszus et al. (2026) y Karlsson et al. (2024) identifican estos endpoints como las operaciones que las APIs exponen vía HTTP; sobre esa base, la presente investigación adopta la URI como unidad de direcciónamiento sobre la cual el framework genera rutas coherentes.

**V**

**Validación.** Proceso que verifica que los datos de entrada (payload JSON de una petición) cumplan con reglas definidas (campos obligatorios, tipos, formatos, rangos). En el contexto del framework, la validación se autogenera en los DTOs de entrada. Alkazemi y Nour (2025) la definen en el lenguaje de dominio específico (DSL) del generador XBoot, que la materializa en el código producido.

**Value**** ****Object**. Objeto inmutable del dominio sin identidad propia, definido únicamente por el valor de sus atributos. Evans (2003) lo distingue tajantemente de las entidades. Özkan et al. (2025) diferencian los objetos de valor de las entidades al señalar que representan atributos conceptuales que carecen de identidad.

HIPÓTESIS

Hipótesis General

La implementación de un framework basado en DDD-liviano con autogeneración de endpoints reduce significativamente el código boilerplate en el desarrollo de APIs REST.

Hipótesis Especificas

	- El código boilerplate presente en el desarrollo convencional de APIs REST bajo el paradigma DDD representa un porcentaje significativo del total de líneas de código, concentrándose principalmente en controladores, servicios, repositorios, DTOs y mappers.

	- El diseño de una arquitectura basada en mecanismos de autogeneración de controladores, servicios, repositorios, DTOs y mappers a partir del modelo de dominio permite cubrir los patrones esenciales del DDD-liviano.

	- La implementación del framework con sus módulos de autogeneración genera endpoints funcionales, compilables y libres de errores en un escenario de desarrollo real.

	- El uso del framework reduce significativamente el tiempo de desarrollo y mantiene o mejora la calidad del código generado, en comparación con el desarrollo manual.

	

DEFINICIÓN Y OPERACIONALIZACIÓN DE VARIABLES

Variable independiente: Framework basado en DDD-liviano con autogeneración de endpoints

**Definición conceptual**. Un framework de dominio se define en esta tesis como una estructura de soporte que encapsula los patrones tácticos del Domain-Driven Design (Aggregates, Repositories, Domain Services), proporcionando una base consistente para implementar el modelo de negocio; los patrones provienen del diseño guiado por el dominio de Evans (2003), pero la noción de framework que los encapsula es propia de esta investigación. Fowler (2002) complementa esta noción al describir el código de infraestructura de una aplicación como *plumbing*; sobre esa base, esta tesis concibe un framework como un conjunto de clases que colaboran para realizar una responsabilidad común en un dominio específico, automatizando las tareas repetitivas y permitiendo al desarrollador concentrarse en la lógica diferenciadora. En esta línea, Alkazemi y Nour (2025) definen un generador low-code como una herramienta que, a partir de un modelo abstracto (un DSL), produce automáticamente el código de infraestructura (controladores, servicios, entidades y plantillas de interfaz, con la capa de acceso a datos resuelta mediante anotaciones como @Repository). Un framework DDD-liviano con autogeneración de endpoints se define en esta tesis como aquel que selecciona los patrones esenciales del DDD y utiliza mecanismos de reflexión o anotaciones para inspeccionar el modelo de dominio y generar automáticamente los artefactos de la capa de aplicación e infraestructura. La viabilidad de la autogeneración de infraestructura a partir del modelo de dominio está respaldada por la herramienta web de Trebejo Loayza (2023), que modela arquitecturas de microservicios y genera el código de infraestructura mediante el generador Yeoman generator-springboot.

**Definición operacional**. El framework basado en DDD-liviano con autogeneración de endpoints se define operacionalmente como el conjunto de módulos y mecanismos diseñados e implementados a partir de un modelo de dominio que permiten generar automáticamente controladores, servicios, repositorios, DTOs y mappers para las entidades de una API REST. Se mide a través del análisis estructural del código boilerplate existente en proyectos convencionales (para establecer la línea base) y mediante la evaluación del diseño arquitectónico del framework, verificando el número de mecanismos de autogeneración definidos, las reglas de transformación modelo-código implementadas y la cobertura de patrones DDD soportados. Este enfoque evalúa la capacidad del framework para reducir el código estructural repetitivo en el desarrollo de APIs REST.

Variable dependiente: Reducción del código boilerplate en APIs REST

**Definición conceptual**. El código boilerplate se define como aquel necesario para que el sistema funcione pero que no expresa la lógica del dominio, comparable con la plomería de una casa: indispensable pero repetitivo y fácil de estandarizar (término equivalente al *plumbing* de Fowler, 2002). En el contexto de DDD, Özkan et al. (2025) no emplean el término: su revisión sistemática se centra en los desafíos de implementación del DDD y en su efectividad. Vasquez Pari (2025) midió, en una empresa desarrolladora de software de Trujillo y sobre una muestra de 30 proyectos, que el uso de herramientas de inteligencia artificial reduce el esfuerzo de ejecución en 82,73 minutos, equivalente a una disminución del 73,23%. Alkazemi y Nour (2025) reportan, desde la perspectiva de los generadores low-code, que menos de 50 líneas de un lenguaje de dominio específico producen entre 950 y 1.350 líneas de Java y HTML con la seguridad y la documentación ya resueltas, y que 10 participantes desplegaron sus aplicaciones en 2 a 20 minutos (promedio ≈ 7) frente a los 45 a 120 minutos de la implementación manual.

Definición operacional. La reducción del código boilerplate en APIs REST se define operacionalmente como la diferencia medible en cantidad de código, tiempo de desarrollo y calidad entre el desarrollo manual y el desarrollo asistido por el framework propuesto. Se mide comparando el porcentaje de reducción de líneas de código (LOC) y el número de archivos/clases generados automáticamente; el tiempo de desarrollo en horas/minutos requerido para implementar un conjunto de endpoints CRUD, manual versus con framework; y la calidad del código generado mediante el número de errores/bugs detectados, el porcentaje de cumplimiento de estándares de codificación (linting) y el índice de mantenibilidad. Este enfoque evalúa el impacto del framework en la productividad y calidad del desarrollo de APIs REST, mediante una comparación cuasiexperimental con medidas relacionadas.

MARCO METODOLÓGICO

ENFOQUE

La presente investigación se desarrolla bajo un **enfoque cuantitativo**. En el ámbito de la ingeniería de software, este enfoque se fundamenta en la **recolección, medición objetiva y análisis estadístico de métricas técnicas** para evaluar la viabilidad, productividad y calidad de las herramientas automatizadas.

Bajo este enfoque, las variables del estudio se operacionalizan y evalúan a través de **indicadores numéricos y datos empíricos verificables**. Por un lado, la cuantificación del problema estructural del código repetitivo se realiza mediante la medición de **líneas de código (LOC) por componente** y la determinación del **porcentaje de duplicación técnica entre módulos**, siguiendo el criterio de caracterización por LOC y porcentaje de duplicación definido en la presente investigación, cuya pertinencia se apoya en la evidencia de reducción de esfuerzo reportada por Vasquez Pari (2025). Por otro lado, el impacto y la reducción del código boilerplate en las APIs REST se determinan a través de un **contraste matemático directo** entre el desarrollo manual tradicional y el desarrollo asistido por el framework propuesto.

La naturaleza cuantitativa de esta investigación permite registrar con precisión datos exactos como el **número de archivos y clases generados automáticamente**, el **tiempo en horas y minutos** invertido por el desarrollador en el *scaffolding* inicial, y los **índices de mantenibilidad y densidad de errores** obtenidos mediante herramientas de análisis estático. De este modo, el enfoque cuantitativo asegura un entorno de evaluación controlado y objetivo, idóneo para contrastar las hipótesis planteadas y medir estadísticamente el **incremento en la eficiencia del ciclo de desarrollo ****backend**.

DISEÑO

La investigación adopta un **diseño cuasiexperimental de un solo grupo con mediciones pretest y ****postest**. Se manipulará deliberadamente la variable independiente el uso del framework propuesto para observar su efecto sobre la variable dependiente la reducción del código boilerplate, comparando el desarrollo manual y el desarrollo asistido sobre el mismo conjunto de entidades y endpoints CRUD. Se clasifica como cuasiexperimental porque las unidades de análisis serán seleccionadas intencionalmente y no se asignarán al azar a grupos independientes; cada unidad funcionará como su propio control al ser evaluada en ambas condiciones. Este esquema permite estimar el efecto del framework mediante medidas relacionadas y es coherente con la comparación controlada de productividad y calidad planteada en el estudio.

La configuración del diseño se divide en **dos fases comparativas secuenciales**:

Medición pre-test (desarrollo manual). Consiste en la construcción convencional y puramente manual de un conjunto de endpoints CRUD para un modelo de dominio específico. En esta fase se registrarán las métricas base de esfuerzo técnico, tales como las líneas de código escritas a mano (LOC) por cada controlador, servicio, repositorio, DTO y mapper, así como el tiempo exacto de desarrollo y la deuda técnica inicial. Esto permitirá establecer la línea base cuantitativa del peso del boilerplate en el ecosistema regional, dentro del diseño cuasiexperimental de medición pretest definido en la presente investigación.

**Medición post-test (desarrollo asistido).** Consiste en la implementación del mismo modelo de dominio y sus respectivos endpoints REST utilizando los **módulos de autogeneración por reflexión** del framework diseñado. En esta fase se volverán a compilar y medir de forma estática las mismas dimensiones cuantitativas: **LOC manual remanente**, **tiempo de ****scaffolding**** inicial**, **porcentaje de código duplicado** por herramientas de *linting* y **bugs detectados**.

NIVEL

La investigación se sitúa en un **nivel explicativo**. De acuerdo con la naturaleza de los proyectos de ingeniería de software que evalúan el impacto de herramientas automatizadas, un estudio de nivel explicativo tiene como propósito principal **determinar las causas y los mecanismos** por los cuales ocurre un fenómeno, yendo más allá de la mera descripción de variables.

En este proyecto, el nivel explicativo se fundamenta en que no solo se busca detallar las características del código estructurado tradicional, sino **demostrar y explicar la relación de causalidad** entre la introducción de la **variable independiente** (mecanismos de autogeneración de endpoints mediante reflexión bajo un enfoque DDD liviano) y la optimización de la **variable dependiente** (reducción medible de la plomería o código boilerplate y disminución del tiempo de desarrollo). Se pretende establecer con rigor científico en qué medida el framework es la causa directa del **incremento en la productividad del backend** y de la **estandarización de artefactos arquitectónicos**. Este enfoque de validación empírica y causal responde a la necesidad señalada por Özkan et al. (2025) de contar con más evaluaciones empíricas del DDD, y sigue el esquema de validación práctica empleado por Alkazemi y Nour (2025) con su generador XBoot y 10 estudiantes.

TIPO

La investigación es de **tipo aplicada y tecnológica**. Es **aplicada** porque está orientada a la resolución de un **problema técnico, práctico y cuantificable** que afecta la competitividad y los ciclos de entrega en el sector tecnológico: el esfuerzo redundante y la acumulación de deuda técnica derivados de la escritura manual de controladores, servicios y repositorios en APIs REST, un cuello de botella documentado a nivel nacional por Chavez Chavez y Wong Portillo (2022) y Vasquez Pari (2025).

Asimismo, se clasifica como una investigación **tecnológica** debido a que su resultado principal es el **diseño, construcción y validación de un artefacto de software inédito** (un framework backend para el ecosistema PHP). Siguiendo el marco de desarrollo tecnológico aplicado en las tesis de Trebejo Loayza (2023) y Bobadilla Chara (2022), el estudio utiliza los conocimientos teóricos existentes sobre los **patrones tácticos del Domain-****Driven**** ****Design** (Evans, 2003) y la **ingeniería dirigida por modelos** (Sadik et al., 2023) para transformarlos en una herramienta operativa, funcional y ejecutable en un escenario real de desarrollo de software regional.

SUJETOS DE LA INVESTIGACIÓN

Universo

El universo de la investigación está conformado por los **artefactos de software, componentes arquitectónicos y contratos de interfaz** que integran las APIs REST desarrolladas bajo entornos orientados al dominio (*Domain-**Driven** **Design*) en el ecosistema de desarrollo backend moderno. Este grupo de elementos tecnológicos se selecciona específicamente para estudiar cómo la automatización de la plomería o infraestructura de código (*boilerplate** **code*) influye en la **optimización de los tiempos de respuesta del programador** y en la **calidad estructural** de los proyectos. Al enfocarse en este universo, se busca comprender el comportamiento y las métricas técnicas de los componentes de software en su fase de construcción inicial (*scaffolding*), lo que permite obtener una perspectiva representativa del impacto de los frameworks dirigidos por modelos en el ciclo de vida del software backend.

Este enfoque es clave, ya que las APIs REST estructuradas con patrones tácticos tradicionales ya poseen un **acoplamiento inherente** y una **alta redundancia** en las capas de controladores y transferencia de datos (DTOs), y se encuentran en una fase crítica donde la mantenibilidad técnica puede mejorar significativamente con el uso adecuado de la **autogeneración por reflexión**. Además, al centrarse en este universo conceptual, se puede observar cómo el acoplamiento y el volumen de código se integran con las reglas de negocio puras, una disciplina de la ingeniería que demanda no solo solidez lógica, sino también la capacidad de mitigar la deuda técnica y acelerar el tiempo de comercialización (*time-**to**-**market*).

La selección de este universo también permite identificar los **cuellos de botella en la escritura manual de código repetitivo**, así como las estrategias que se pueden implementar para mejorar el rendimiento de la ingeniería de software regional, con miras a fortalecer la mantenibilidad de los futuros sistemas empresariales distribuidos.

Población

La población de estudio está constituida por la **totalidad de componentes técnicos e interfaces transaccionales CRUD** (*Create**, Read, **Update**, Delete*) requeridos para dar soporte a la capa de infraestructura e intercomunicación de una solución de software empresarial backend. En la presente investigación, la población se define como el conjunto completo de **unidades de análisis medibles y estandarizadas** que representan el fenómeno de la duplicación de código en su totalidad. A diferencia de la población de proyectos de una empresa limeña empleada por Pizarro Romero y Paredes Orihuela (2025), aquí se circunscribe a los componentes técnicos descritos a continuación.

Para efectos de esta investigación, la población teórica evaluada abarca un total estimado de componentes de plomería técnica distribuidos en las capas de **controladores, servicios de aplicación, repositorios de persistencia, DTOs y mappers** necesarios para mapear las operaciones de datos de un dominio de software. Estos elementos técnicos representan de forma fidedigna el ecosistema donde el esfuerzo redundante y la acumulación de líneas de código manuales (LOC) impactan de manera directa sobre la **productividad del desarrollador backend**. Este escenario se identifica en la presente investigación como prioritario para la introducción de métricas cuantitativas de automatización, y su problemática de esfuerzo redundante ha sido documentada por Vasquez Pari (2025).

Muestra

La muestra de estudio es de tipo **no probabilística, por conveniencia o intencional**. En el ámbito de la ingeniería empírica de software, la selección de la muestra se realiza bajo criterios técnicos estrictos para asegurar que el subconjunto específico de componentes refleje con precisión los desafíos de mantenibilidad del sistema completo, sin requerir la implementación redundante de toda la población, lo que hace que el experimento controlado sea eficiente y manejable.

La muestra seleccionada para la validación experimental del framework propuesto estará compuesta por los **artefactos arquitectónicos generados para un conjunto representativo de entidades de negocio** del dominio (por ejemplo, **entre 5 y 8 entidades clave** del modelo de datos). Esta muestra técnica, que incluye tanto sus controladores autogenerados como sus contratos de persistencia y objetos de transferencia, permitirá recolectar y contrastar de manera controlada los datos matemáticos reales del *pre-test* (construcción manual tradicional) frente al *post-test* (construcción asistida por el framework de *Lightweight** DDD*). El análisis estático de esta muestra proporcionará datos de alto valor científico respecto a la **reducción efectiva de líneas de código escritas a mano**, la **densidad de duplicación** y el **ahorro de tiempo en minutos** dedicados al *scaffolding* arquitectónico.

MÉTODOS Y PROCEDIMIENTOS

Métodos

En el desarrollo del presente trabajo de investigación se aplicarán los siguientes métodos, seleccionados cuidadosamente para garantizar la precisión y relevancia de los resultados en el ámbito de la ingeniería de software.

**Método inductivo.** Este método se basa en un razonamiento que va de lo particular a lo general, observando las características de fenómenos específicos para llegar a conclusiones más amplias. En este estudio, durante la etapa de diagnóstico preliminar, se utiliza el método inductivo a través de la **inspección de bloques de código específicos y patrones redundantes** en controladores y mappers particulares dentro de APIs REST tradicionales. Esto permitirá que la información técnica recogida sobre cada indicador de duplicación conduzca a deducciones más generales sobre el **peso real y el impacto operativo** que el código boilerplate ejerce sobre los proyectos backend a escala nacional, facilitando la identificación de patrones de redundancia estructural. Así, el método inductivo resulta ser una herramienta esencial para abstraer las **reglas de transformación modelo-código** que el framework automatizará.

**Método deductivo.** El método deductivo organiza hechos o realidades generales para derivar conclusiones a partir de enunciados previamente establecidos, partiendo de principios o teorías generales para aplicarlos a casos específicos, con el objetivo de obtener conclusiones precisas y verificables. En el contexto de esta investigación, este método permitirá aplicar las teorías globales del **Diseño Guiado por el Dominio (DDD)** y los **patrones tácticos** planteados por Evans (2003) a la arquitectura particular de software que se va a construir. A partir de estos axiomas arquitectónicos generales, se deducirán las **estructuras lógicas de reflexión** que gobernarán la autogeneración de endpoints funcionales en PHP, lo que ayudará a validar las hipótesis mediante la observación de datos técnicos precisos.

**Método analítico.** El método analítico implica descomponer un conjunto en varias partes para estudiar el comportamiento de cada una y luego sintetizar las características del todo. En este proyecto, se utiliza este enfoque para procesar y desglosar los **datos métricos obtenidos en los ****análisis estáticos de código**, lo que permitirá interpretar de manera detallada el volumen de líneas por componente (controladores, servicios, repositorios, DTOs y mappers). Al aplicar este método, se podrá examinar minuciosamente el **impacto individual de cada artefacto ****boilerplate** en la mantenibilidad y la deuda técnica, para luego integrar dicha información desglosada en una visión clara que demuestre científicamente el **porcentaje exacto de reducción del esfuerzo de desarrollo** logrado por el framework.

Procedimientos

Para el cumplimiento de los objetivos específicos de la investigación, el desarrollo del proyecto se ejecutará a través de un **procedimiento metodológico estructurado en cuatro fases secuenciales** basadas en la ingeniería de software empírica. Cada etapa detalla las actividades, los métodos y los materiales o equipos tecnológicos requeridos para su realización.

**Tabla ****1****: Fases del procedimiento**

| Fase | Métodos | Entregable |
| --- | --- | --- |
| **FASE 1**: DIAGNÓSTICO Y ANÁLISIS DE REQUISITOS | Análisis estático de código y observación estructurada | Línea base de métricas de boilerplate (Pre-test) |
| **FASE 2**: DISEÑO ARQUITECTÓNICO DEL FRAMEWORK | Modelado de software (UML) y patrones tácticos (DDD-liviano) | Blueprint estructural y algoritmos de reflexión |
| **FASE 3**: IMPLEMENTACIÓN Y CONSTRUCCIÓN TECNOLÓGICA | Desarrollo ágil y metaprogramación en PHP 8.x | Framework ejecutable y APIs de prueba |
| **FASE 4**: EVALUACIÓN Y CONTRASTE ESTADÍSTICO | Experimentación controlada y análisis inferencial (Post-test) | Validación empírica de reducción de deuda técnica |

**Ilustración ****1** - Fases del procedimiento

Fase 1: Diagnóstico y Análisis de Requisitos (Objetivo Específico 1)

*Procedimiento:* Esta fase inicial consiste en caracterizar y cuantificar la problemática del código repetitivo (*boilerplate*) en el desarrollo convencional de APIs REST. Se procederá a compilar la estructura de una API tradicional escrita de forma manual para identificar los patrones redundantes en controladores, mappers y capas de transferencia (DTOs). Se registrarán rigurosamente las métricas de líneas de código escritas a mano (LOC) y los tiempos de configuración arquitectónica inicial, estableciendo formalmente la medición *Pre-test* siguiendo el criterio de caracterización por LOC y duplicación definido en la presente investigación.

*Materiales y Equipos:* Estación de trabajo con procesador de arquitectura x86-64, 16 GB de memoria RAM y entorno operativo Windows 11 con Subsistema de Windows para Linux (WSL2). En software se emplearán analizadores estáticos (PHP_CodeSniffer, PHPMD), herramientas de conteo de líneas (cloc) y hojas de cálculo para registrar la línea base.

Fase 2: Diseño Arquitectónico del Framework (Objetivo Específico 2)

*Procedimiento:* Se definirá la arquitectura de software del framework propuesto integrando un enfoque de *Lightweight** Domain-**Driven** **Design* (DDD-liviano). El método se centrará en el modelado de los componentes de abstracción que permitirán aislar el modelo de dominio y gobernar la autogeneración dinámica de contratos mediante técnicas de reflexión en tiempo de ejecución. Se diseñarán las interfaces del núcleo, las estrategias de mapeo automático y la infraestructura de enrutamiento sin requerir acoplamiento de plomería manual, fundamentando el diseño en las pautas arquitectónicas de Evans (2003) y los principios de generación de código dirigidos por modelos descritos por Sadik et al. (2023).

*Materiales y Equipos:* Estación de trabajo principal, entornos de modelado visual para diagramación UML, editores de texto avanzados (Visual Studio Code) y documentación técnica de la API de reflexión nativa de PHP.

Fase 3: Implementación y Construcción Tecnológica (Objetivo Específico 3)

*Procedimiento:* Consiste en la codificación y ensamblaje del artefacto tecnológico (el framework backend). Utilizando programación orientada a objetos avanzada y metaprogramación, se construirán los módulos de lectura de metadatos, el motor de resolución de dependencias por inversión de control (IoC) y los componentes automatizados para la exposición de endpoints CRUD de manera transparente. Una vez operativo el framework, se procederá a implementar la muestra de entidades seleccionada a través de este entorno automatizado, consolidando el prototipo funcional ejecutable de acuerdo con los marcos de construcción de herramientas de software aplicados por Trebejo Loayza (2023).

*Materiales y Equipos:* Estación de trabajo con entorno virtualizado mediante VMware Workstation para simular el despliegue en un servidor de producción Linux (Ubuntu Server). Como software se utilizará el entorno de ejecución PHP 8.x, el gestor de dependencias Composer, herramientas de depuración (Xdebug) y el sistema de control de versiones Git/GitHub.

Fase 4: Evaluación y Contraste Estadístico (Objetivo Específico 4)

*Procedimiento:* En la fase final, se ejecutará el experimento controlado mediante la medición *Post-test*. Se someterán las APIs autogeneradas por el framework a las mismas pruebas de análisis estático aplicadas en la Fase 1. Se recolectarán los datos finales de líneas de código remanentes, la densidad de duplicación técnica detectada por herramientas de *linting*, y el tiempo exacto invertido bajo el enfoque asistido. Los resultados de ambas mediciones (*Pre-test* vs. *Post-test*) se tabularán para realizar un contraste estadístico directo, lo que permitirá evaluar formalmente las hipótesis de la investigación y determinar con exactitud el porcentaje de reducción de *boilerplate** **code* y optimización del esfuerzo técnico.

*Materiales y* Equipos*:* Estación de trabajo principal, herramientas informáticas de análisis estático y calidad de código (SonarQube local) y el software estadístico IBM SPSS Statistics (o scripts automatizados en R/Python) para la ejecución de pruebas paramétricas o no paramétricas (como la prueba de rangos con signo de Wilcoxon o T-Student).

Para operativizar estas fases transversales dentro de las tareas rutinarias de la investigación, se ejecutarán de forma complementaria las siguientes actividades normativas de recolección:

	- **Revisión de literatura:** La revisión de literatura permitirá explorar cómo la comunidad científica e informática internacional ha abordado la reducción del código estructurado y la generación *low-code*, identificando los métodos y herramientas tecnológicas arquitectónicas que han demostrado ser eficaces en contextos distribuidos contemporáneos, tales como los enfoques de Alkazemi y Nour (2025) y Özkan et al. (2025). Esta información servirá de referencia para optimizar el diseño del framework basado en DDD-liviano.

	- **Análisis documental:** Se realizará una revisión detallada de las estructuras de código, proyectos backend de referencia, documentación de APIs REST convencionales e investigaciones locales sobre productividad, como las desarrolladas por Chavez Chavez y Wong Portillo (2022) y Vasquez Pari (2025). Este análisis será fundamental para evaluar cómo las capas de persistencia y servicios actuales están absorbiendo horas de desarrollo innecesarias.

	- **Observación directa:** Consiste en inspeccionar y registrar en tiempo real, mediante bitácoras de seguimiento técnico, los comportamientos, la densidad de errores tipográficos y las prácticas convencionales que ejecutan los programadores durante el scaffolding manual de endpoints REST, aportando datos reales sobre la variabilidad estructural que introduce la transcripción repetitiva.

	- **Análisis cuantitativo:** Ayudará a medir de manera estadística las variables dependientes de la investigación, evaluando matemáticamente la diferencia entre el desarrollo manual tradicional y el desarrollo asistido por el framework mediante el procesamiento automatizado de datos numéricos.

	

TÉCNICAS E INSTRUMENTOS

Al combinar las técnicas e instrumentos seleccionados, se busca obtener métricas precisas y objetivas sobre el estado actual del código repetitivo y evaluar de forma rigurosa el impacto del framework DDD-liviano en el desarrollo de APIs REST. Este enfoque asegura la validez de los resultados y la eficacia de la solución arquitectónica propuesta.

Técnicas

	- **Técnicas de muestreo**: Se aplicará un muestreo no probabilístico intencional. Se seleccionará de forma deliberada un conjunto representativo de entidades del modelo de dominio para someterlas al desarrollo manual y automatizado, garantizando que incluyan las interacciones CRUD estándar necesarias para contrastar el esfuerzo técnico.

	- **Técnicas de recolección de datos**: a) ***Técnicas de gabinete*** (Análisis documental): Revisión exhaustiva de repositorios de código, documentación técnica y manuales de arquitectura. Permitirá extraer las bases para establecer las métricas de la plomería redundante en los proyectos backend. b) ***Técnicas de laboratorio*** (Observación directa métrica): Ejecución controlada del desarrollo de software en la estación de trabajo y servidores locales. Se recolectarán los datos empíricos de manera automatizada en el entorno de desarrollo, capturando sin sesgos el rendimiento del código pre-test y post-test.

- Técnicas de análisis: Se utilizarán pruebas estadísticas inferenciales. Debido al diseño cuasiexperimental con medidas relacionadas, se aplicará la prueba paramétrica T de Student para muestras relacionadas (o la prueba no paramétrica de Wilcoxon) mediante software estadístico. Esto determinará si la reducción de tiempos y líneas de código presenta una diferencia estadísticamente significativa.

Instrumentos

**Fichas de análisis documental y revisión bibliográfica:** Instrumento estructurado para clasificar y registrar los patrones de diseño y los componentes que generan mayor nivel de replicación estructural (boilerplate).

**Guías de observación y listas de cotejo métrico:** Formularios técnicos vinculados a las salidas de las herramientas de análisis estático (SonarQube, PHPMD, cloc). Registrarán objetivamente los indicadores dependientes: líneas de código escritas a mano (LOC), porcentaje de duplicación y densidad de errores.

**Bitácora cronométrica (Registro de tiempos):** Ficha de recolección diseñada para asentar estrictamente el tiempo en horas y minutos invertido en la configuración inicial y desarrollo del scaffolding, tanto en la fase manual como en la automatizada por el CLI del framework.

Confiabilidad y validez de los instrumentos

**Validez**: Los instrumentos de recolección documental y las bitácoras cronométricas serán sometidos a validación mediante la técnica de Juicio de Expertos. Tres especialistas con grado académico en Ingeniería Informática o áreas afines evaluarán la pertinencia, claridad y congruencia de los formatos. Los informes y certificados de validación estarán incluidos en los Anexos de la investigación.

**Confiabilidad**: Gran parte de la recolección de datos se apoyará en software de análisis estático estandarizado, lo que otorga una confiabilidad y precisión paramétrica incorruptible a variables como las LOC y la complejidad del código. Para los registros cronométricos manuales, se ejecutará una prueba piloto sobre un módulo de software de prueba para asegurar la consistencia y fiabilidad del proceso de medición de tiempos antes de la recolección oficial

ASPECTOS ÉTICOS

Los aspectos éticos son fundamentales en la investigación tecnológica, no solo porque aseguran la validez y confiabilidad del desarrollo del software, sino también porque son la base sobre la que se construye la integridad científica y el respeto a la propiedad intelectual. Sin una sólida ética profesional, los resultados y las métricas obtenidas pierden su legitimidad. Por ello, mantener estos principios en cada fase del ciclo de vida del desarrollo es vital para lograr una investigación honesta, transparente y respetuosa con la comunidad académica e informática.

**Originalidad y probidad académica**: La investigación se desarrollará bajo estrictos estándares de integridad científica, respetando la autoría de las bases teóricas y antecedentes consultados. En cumplimiento con la normativa de originalidad de la universidad, se suscribirá y adjuntará el Formato N° 6: Declaración jurada, documento proporcionado por la Oficina Central de Investigación (OCIN-VRI-UNP), certificando que el framework propuesto y los datos presentados son producto del trabajo original del tesista y no constituyen plagio.

**Propiedad intelectual y licenciamiento**: Se respetará rigurosamente la autonomía y los derechos de autor de todas las herramientas, repositorios de terceros, dependencias de Composer y analizadores estáticos empleados en el ecosistema PHP. Todo uso de librerías externas de código abierto (open-source) se realizará en estricto cumplimiento de sus respectivas licencias (MIT, GPL, Apache, entre otras), citando adecuadamente a los creadores originales de las tecnologías base.

**Confidencialidad y privacidad de datos**: En caso de que la medición de la línea base (pre-test) requiera analizar repositorios o APIs de proyectos reales existentes, se protegerá rigurosamente la privacidad de dicha información. Cualquier credencial de acceso, cadena de conexión a bases de datos, tokens de seguridad o lógica de negocio sensible será anonimizada u omitida de los reportes públicos, asegurando que los datos queden accesibles únicamente para los fines de tabulación métrica.

**Imparcialidad y objetividad métrica**: La recopilación y el análisis de los datos cuantitativos se realizarán con total neutralidad algorítmica. Los resultados de reducción de líneas de código (LOC) y tiempos de ejecución serán procesados y presentados de forma precisa y justa, sin alterar ni manipular las reglas de los analizadores estáticos (como SonarQube) para favorecer artificialmente el rendimiento del framework autogenerador.

**Transparencia tecnológica**: Se mantendrá una comunicación clara y auditable sobre los alcances de la herramienta. Los algoritmos de reflexión, el diseño arquitectónico basado en DDD-liviano y los métodos de enrutamiento del framework serán explicados abiertamente. Si el framework presenta limitaciones técnicas o incompatibilidades con ciertos patrones complejos, esto se informará de manera inmediata y transparente en las conclusiones de la tesis.

**Responsabilidad social y beneficio mutuo**: Los resultados de la investigación están orientados a enriquecer el conocimiento general de la ingeniería de software regional. Al reducir el código estructural redundante (boilerplate), la propuesta busca mejorar la salud laboral y el bienestar de los desarrolladores, mitigando el agotamiento mental (burnout) derivado de tareas mecánicas y permitiendo que los profesionales se enfoquen en la creación de soluciones innovadoras que aporten valor real a la sociedad.

**Finalización ética y código abierto**: Al concluir el proyecto, se tomarán medidas para asegurar la trazabilidad y reproducibilidad del estudio de manera transparente. Las bases de datos estadísticos del experimento pre-test y post-test se preservarán de forma íntegra para posibles auditorías, y el código fuente del framework generado podrá ser compartido bajo lineamientos éticos que promuevan la mejora continua del desarrollo backend en el país.

ASPECTOS ADMINISTRATIVOS

CRONOGRAMA DE EJECUCIÓN

El proyecto de investigación se ejecutará en un plazo total de cuatro (4) meses, equivalentes a dieciséis (16) semanas, contados a partir de la aprobación del presente proyecto de tesis. El diagrama de Gantt presenta la distribución mensual de todas las actividades previstas, incluida la presentación obligatoria del avance del informe al 50 % y la presentación del informe final.

**Tabla ****2****: Cronograma de Ejecución**

| ACTIVIDADES | Meses |
| --- | --- |
|  | Mes 1 | Mes 2 | Mes 3 | Mes 4 |
|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| Adecuación de la estructura del informe de tesis |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Recojo de datos |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Presentación del avance del informe de tesis (50%) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Análisis de datos |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Discusión |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Concluir y recomendar |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Elaborar artículo científico |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Postulación a revista para publicación del artículo |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sustentación del informe final de tesis |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

PRESUPUESTO

El presupuesto estimado para el desarrollo de la investigación considera la adquisición de equipos, materiales y la contratación de servicios de terceros necesarios para completar satisfactoriamente las cuatro fases del proyecto. Los montos se expresan en soles (S/) y corresponden a valores aproximados de mercado a la fecha de elaboración del presente proyecto.

**Tabla ****3****: Presupuesto de la investigación**

| Denominación | Unidad | Valor unitario (S/) | Cantidad | Costo total (S/) |
| --- | --- | --- | --- | --- |
| Equipos |  |  |  |  |
| Laptop (equipo propio) | unidad | 2000.00 | 1 | 2000.00 |
| Subtotal equipos |  |  |  | 2000.00 |
| Materiales |  |  |  |  |
| Papel bond A4 (paquete) | paquete | 18.00 | 1 | 18.00 |
| Útiles de oficina | global | 20.00 | 1 | 20.00 |
| Cartuchos de impresión | unidad | 90.00 | 2 | 180.00 |
| Subtotal materiales |  |  |  | 218.00 |
| Servicios |  |  |  |  |
| Licencia Microsoft 365 | anual | 165.00 | 1 | 165.00 |
| Antivirus | anual | 120.00 | 1 | 120.00 |
| Internet (hogar) | mensual | 200.00 | 4 | 800.00 |
| Telefonía móvil (datos) | mensual | 35.00 | 4 | 140.00 |
| Energía eléctrica | mensual | 40.00 | 4 | 160.00 |
| Subtotal servicios |  |  |  | 1385.00 |
| TOTAL GENERAL |  |  |  | 3603.00 |

FINANCIAMIENTO

El presente proyecto de investigación será **autofinanciado en su totalidad** por el propio investigador (tesista), quien asumirá los costos correspondientes a la adquisición de equipos, materiales y servicios detallados en el punto 4.2, ascendentes a un monto aproximado de **S/ 3,603.00**.

Asimismo, se contará con el **aporte no monetario de la Universidad Nacional de Piura (UNP)**, a través de la asesoría académica brindada por el docente asesor, el acceso a los ambientes y laboratorios de la Facultad de Ingeniería Industrial, y el uso de los recursos bibliográficos y bases de datos científicas disponibles en la biblioteca institucional, los cuales no representan un costo adicional para el tesista.

DESARROLLO DE LA SOLUCIÓN

Descripción general de la solución

Boilerfree es la solución tecnológica propuesta en la presente investigación. Consiste en un framework backend para PHP 8.x orientado a reducir el código estructural repetitivo que suele acompañar el desarrollo de APIs REST. Su diseño adopta un enfoque DDD-liviano: conserva los elementos tácticos necesarios para representar entidades, objetos de valor, agregados, repositorios y servicios de dominio, pero evita incorporar una carga arquitectónica que no resulte indispensable para el alcance del sistema.

La propuesta utiliza el modelo de dominio como fuente principal de información. A partir de clases tipadas y metadatos declarados mediante atributos de PHP, el framework inspecciona la estructura del dominio y deriva en tiempo de ejecución el comportamiento requerido para exponer endpoints, validar solicitudes, hidratar objetos, serializar respuestas y persistir agregados. En consecuencia, el término autogeneración se emplea en esta investigación para describir la derivación automática de comportamiento y componentes durante la ejecución, y no necesariamente la creación permanente de archivos fuente.

Esta precisión permite mantener la coherencia entre el título de la investigación y la implementación planteada. Los controladores, repositorios, objetos de transferencia, mapeadores, rutas y operaciones de persistencia no se reproducen como archivos independientes para cada entidad; sus responsabilidades son asumidas por componentes genéricos configurados con la metadata del dominio. Por ello, la reducción del boilerplate se medirá mediante el código manual evitado, el tiempo requerido para implementar los mismos casos funcionales y la calidad estructural resultante.

Propósito y principios de diseño

El propósito de Boilerfree es permitir que el desarrollador concentre su esfuerzo en las reglas de negocio y en las decisiones que no pueden inferirse automáticamente. El principio rector establece que toda información derivable del modelo debe ser resuelta por el framework, mientras que las decisiones propias del dominio deben permanecer explícitas. De este modo, la automatización no sustituye la lógica de negocio ni oculta sus invariantes, sino que elimina el cableado técnico repetitivo que las rodea.

La solución se apoya en cuatro decisiones fundamentales: derivación dinámica en tiempo de ejecución, implementación sobre PHP 8.x, distribución como librería gestionada mediante Composer y arquitectura basada en puertos y adaptadores. La derivación dinámica evita mantener archivos generados que podrían quedar desactualizados respecto del modelo. PHP aporta tipado, atributos y reflexión nativa; Composer facilita la integración en proyectos existentes; y los puertos desacoplan el núcleo de tecnologías específicas de persistencia, autenticación, almacenamiento, correo, colas y observabilidad.

Las decisiones arquitectónicas se evalúan mediante un análisis causal iterativo inspirado en la técnica de los cinco porqués. Cada alternativa se contrasta con el problema que pretende resolver, sus dependencias y sus riesgos. Cuando una decisión no puede justificarse mediante una restricción técnica, un principio de diseño o una necesidad del dominio, se revisa antes de incorporarla al contrato del framework.

Arquitectura de la solución

La arquitectura se organiza en un núcleo de derivación y un conjunto de adaptadores intercambiables. El núcleo descubre las clases del dominio, interpreta sus atributos, construye una representación de metadata y coordina el enrutamiento, la hidratación, la validación, la serialización y el ciclo transaccional. Los adaptadores implementan capacidades externas mediante contratos estables, lo que permite sustituir la base de datos, el mecanismo de autenticación o los servicios operativos sin modificar las entidades.

**Ilustración ****2** - Arquitectura general de Boilerfree: del front controller a la base de datos.

***Descripción****:* El diagrama ilustra los componentes principales de la arquitectura del framework. Muestra el flujo de inicialización desde el controlador frontal (public/index.php), el arranque con inyección de dependencias (Container), y la interacción entre el motor de metadatos (MetadataEngine) y el enrutador HTTP (Http\Router) para despachar la petición hacia los controladores CRUD y la capa de persistencia en PostgreSQL. Elaborado con la herramienta Archify ([https://github.com/tt-a1i/archify](https://github.com/tt-a1i/archify)), empleando inteligencia artificial para modelar la representación visual a partir del código fuente de la solución.

El desarrollador escribe únicamente entidades, objetos de valor, servicios de dominio y servicios de consulta. Las entidades concentran identidad, estado e invariantes; los objetos de valor representan conceptos inmutables; los servicios de dominio coordinan operaciones que no pertenecen naturalmente a una entidad; y los servicios de consulta producen modelos de lectura tipados. Esta separación evita introducir dependencias de infraestructura en el dominio.

Los componentes derivados incluyen un controlador CRUD genérico, un repositorio genérico, las rutas, la validación de entrada, la conversión entre representaciones y el esquema de persistencia. Estos componentes existen como comportamiento reutilizable del framework, no como copias por entidad. Los puertos de persistencia, autenticación, almacenamiento, caché, colas, correo, registro, reloj y eventos permiten integrar implementaciones específicas cuando el proyecto lo requiera.

Modelo de metadatos

El contrato declarativo se mantiene deliberadamente reducido. Los atributos principales identifican entidades, campos, relaciones, acciones, proyecciones, consultas y tareas diferidas o programadas. La convención predomina sobre la configuración: las propiedades tipadas del constructor se consideran campos por defecto y los atributos se emplean cuando existe una desviación que debe expresarse de forma explícita.

**Ilustración ****3** - Flujo de datos: Del lenguaje de dominio (DSL) al entorno de ejecución (runtime).

***Descripción****:* Representación del proceso de escaneo y derivación de metadatos. Las clases de dominio ubicadas en src/Domain son interpretadas por el MetadataEngine mediante sus atributos. Este proceso genera un caché asíncrono (metadata.php) que alimenta a los consumidores finales en tiempo de ejecución, como la tabla de rutas, las columnas de objetos de valor y las sentencias SQL. Elaborado con la herramienta Archify ([https://github.com/tt-a1i/archify](https://github.com/tt-a1i/archify)), empleando inteligencia artificial para modelar la representación visual a partir del código fuente de la solución.

**Tabla ****4****: Modelos de metadatos**

| Elemento | Responsabilidad |
| --- | --- |
| Entidad | Declara una raíz de agregado expuesta por la API y sus opciones generales. |
| Campo | Define identidad, nombre, exposición, validación o indexación cuando se aparta de la convención. |
| Relaciones | Representan colecciones uno a muchos o muchos a muchos y sus reglas de persistencia. |
| Acción | Expone una operación de dominio como endpoint controlado. |
| Proyección | Incorpora valores calculados de solo lectura en la respuesta. |
| Consulta | Declara modelos de lectura, filtros, paginación y caché. |

Los objetos de valor se reconocen por su tipo y se hidratan mediante su constructor. Cuando contienen varias propiedades, cada valor se almacena en una columna con prefijo y se reconstruye de forma recursiva. La identidad se resuelve mediante UUID versión 7 cuando el cliente no suministra un valor, decisión compatible con la inmutabilidad del dominio y con la eficiencia de los índices ordenados temporalmente.

Persistencia, relaciones y consultas

La escritura se realiza por agregado y cada operación se ejecuta dentro de una transacción. El repositorio genérico hidrata la raíz, aplica la operación de dominio, persiste el nuevo estado y confirma la transacción; ante una excepción, revierte los cambios. El control de concurrencia utiliza bloqueo optimista mediante una versión interna, mientras que las operaciones que requieran exclusión pueden solicitar bloqueo pesimista.

Las relaciones uno a muchos y muchos a muchos se declaran en el dominio y se cargan dentro del límite del agregado. Las referencias entre agregados se representan mediante identificadores escalares, lo que evita acoplamiento y carga diferida implícita. Los objetos de valor se almacenan embebidos. Con ello se elimina el problema de consultas inesperadas asociado al lazy loading y se mantiene explícito el límite transaccional.

Para las lecturas se adopta un enfoque CQRS-liviano. Los servicios de consulta operan sobre un puerto de acceso a datos y devuelven modelos de lectura tipados, sin reconstruir agregados cuando no resulta necesario. El mecanismo admite filtros, ordenamiento, paginación, agregaciones y uniones simples. Las consultas más complejas pueden delegarse a un adaptador especializado sin alterar el contrato del dominio.

Las entidades que habiliten eliminación lógica incorporan una marca temporal y un filtro global. La política sobre sus elementos relacionados debe declararse de manera explícita como restricción, propagación o asignación nula. Asimismo, el framework contempla reintentos controlados para errores transitorios de concurrencia, pero no oculta infracciones de unicidad, integridad referencial o contrato.

Exposición de endpoints y contrato HTTP

Las rutas CRUD se derivan del nombre y la versión declarada para cada entidad. Las acciones del dominio y las consultas expuestas producen rutas adicionales. El framework hidrata sus argumentos a partir del cuerpo JSON, parámetros de ruta o consulta, manteniendo una frontera de tipado estricto: los valores incompatibles no se convierten de forma silenciosa, sino que originan una respuesta de validación.

**Ilustración ****4** - Ciclo de vida de una petición HTTP a través del kernel.

***Descripción***: Diagrama de secuencia que detalla el procesamiento de una solicitud HTTP (por ejemplo, GET /v1/ordenes?page=2). Muestra la validación de estado de mantenimiento temprano, el enrutamiento lógico, y la delegación al CrudController genérico, el cual realiza la consulta paginada a través de PdoQuerySource y retorna una respuesta HTTP 200 en formato JSON con enlaces de navegación. Elaborado con la herramienta Archify ([https://github.com/tt-a1i/archify](https://github.com/tt-a1i/archify)), empleando inteligencia artificial para modelar la representación visual a partir del código fuente de la solución.

El formato predeterminado es JSON. La creación devuelve el recurso y el código 201; la consulta individual y la actualización devuelven 200; la eliminación satisfactoria devuelve 204; y una operación diferida aceptada devuelve 202. Las listas paginadas incluyen los datos, la metadata de página y los enlaces de navegación, mientras que las listas no paginadas se entregan como arreglos simples.

Todos los errores mantienen una estructura uniforme compuesta por código, mensaje y detalles opcionales. Los errores de hidratación o validación se informan con el código 422; un conflicto de negocio o concurrencia, con 409; un recurso inexistente, con 404; una solicitud sin autenticación, con 401; y una operación no autorizada, con 403. Los errores internos no exponen información sensible en producción.

La validación combina reglas derivadas del tipo con reglas declarativas para longitudes, formatos, rangos, unicidad, existencia y archivos. Las invariantes de negocio no se trasladan a esta metadata: permanecen en los métodos de las entidades o servicios. Esta distinción evita confundir validación de entrada con reglas propias del dominio.

**Herramientas de desarrollo y operación**

Boilerfree incorpora una interfaz de línea de comandos para crear la estructura inicial del proyecto, validar la metadata, inspeccionar rutas, aplicar o revertir cambios del esquema, ejecutar pruebas y levantar un servidor de desarrollo. Los comandos de creación solo generan esqueletos pertenecientes a la fuente de verdad, como entidades, objetos de valor, servicios, pruebas o datos iniciales; no crean controladores, repositorios, DTOs ni rutas, porque estas piezas se derivan en ejecución.

**Ilustración ****5** - Flujo de ejecución del comando de optimización de metadatos.

***Descripción***: Proceso de validación y reconstrucción ejecutado por el comando CLI optimize. El flujo verifica la existencia del directorio de dominio, borra el caché obsoleto, carga las nuevas reglas mediante el MetadataEngine y reconstruye la tabla de rutas y el caché de metadatos antes de emitir los artefactos finales mediante Composer. Elaborado con la herramienta Archify ([https://github.com/tt-a1i/archify](https://github.com/tt-a1i/archify)), empleando inteligencia artificial para modelar la representación visual a partir del código fuente de la solución.

El proyecto resultante se distribuye como una aplicación Composer con un único punto de entrada HTTP, archivos de configuración por entorno, un archivo central para enlazar adaptadores y carpetas para el dominio, pruebas y datos temporales. La organización recomendada agrupa el código por concepto de negocio y no por categoría técnica, con el propósito de conservar la cohesión y reducir desplazamientos innecesarios entre directorios. 

**Ilustración ****6** - Máquina de estados y ciclo de vida del caché de metadatos.

***Descripción***: El diagrama describe las transiciones de estado del archivo de caché subyacente. Muestra cómo un caché válido (fresh) pasa a estar obsoleto (stale) cuando se detectan cambios en el código fuente, desencadenando una reconstrucción (rebuilding). También ilustra los estados de error (invalid o no reconstruible) si la carga del DSL falla o los permisos de escritura son insuficientes. Elaborado con la herramienta Archify ([https://github.com/tt-a1i/archify](https://github.com/tt-a1i/archify)), empleando inteligencia artificial para modelar la representación visual a partir del código fuente de la solución.

La gestión del esquema compara la metadata con la base de datos y aplica las diferencias. En producción, las operaciones destructivas requieren confirmación explícita y pueden revisarse previamente. También se mantiene un registro de lotes para conocer el estado y revertir el último cambio. Estas medidas permiten que la automatización no comprometa la seguridad de los datos.

**Seguridad y operabilidad**

La seguridad se aborda mediante un puerto de autenticación y reglas de acceso declaradas por ruta. Las operaciones pueden ser públicas, requerir un usuario autenticado o restringirse a funciones administrativas. Las decisiones dependientes del objeto se implementan como políticas del dominio, mientras que las consultas de lista deben aplicar un alcance que evite exponer registros no autorizados.

El ciclo HTTP contempla limitación de solicitudes, configuración CORS, encabezados de seguridad, consultas preparadas y límites de tamaño y tiempo. En aplicaciones con sesiones y vistas, la protección contra solicitudes falsificadas se aplica a las operaciones no idempotentes. Para las APIs basadas en tokens, el diseño conserva un comportamiento sin estado.

La operabilidad incluye identificadores de solicitud, registros estructurados, comprobaciones de salud y disponibilidad, métricas básicas y reporte de errores. La documentación OpenAPI podrá derivarse de las mismas rutas, tipos y reglas de validación. Estas capacidades forman parte del diseño del producto, pero su disponibilidad deberá informarse según el avance real de la implementación.

**Estrategia de pruebas y validación experimental**

La estrategia de pruebas se divide en dos niveles. El núcleo requiere pruebas unitarias para el motor de metadata, el hidratador, el enrutamiento, la serialización y la persistencia. La aplicación experimental requiere pruebas funcionales de creación, lectura, actualización, eliminación, acciones y consultas sobre las entidades seleccionadas.

La evaluación utilizará el mismo conjunto de cinco a ocho entidades en las condiciones manual y asistida. Se registrarán las líneas de código escritas por el desarrollador, el tiempo de implementación, la duplicación, los defectos detectados, el cumplimiento de estándares y el índice de mantenibilidad. En la condición asistida, los componentes resueltos dinámicamente se contabilizarán como responsabilidades automatizadas y no como archivos físicos generados.

Los resultados de ambas condiciones se analizarán como medidas relacionadas. Cuando se cumplan los supuestos de normalidad se empleará la prueba T de Student para muestras relacionadas; en caso contrario, se utilizará la prueba de rangos con signo de Wilcoxon. El capítulo no anticipa resultados: describe el artefacto y el procedimiento que permitirá comprobar posteriormente su efecto.

**Estado y alcance de la implementación**

El desarrollo del framework se encuentra en curso. El diseño técnico define el motor de metadata, la hidratación tipada, el enrutamiento derivado, la persistencia genérica, el contrato HTTP y la interfaz de comandos. Sin embargo, la presencia de una capacidad en el diseño no debe interpretarse como evidencia de que ya ha sido implementada o validada.

Durante la construcción se registrará cada capacidad como implementada, parcialmente implementada, pendiente o fuera del alcance experimental. La validación principal se limitará al camino necesario para demostrar instalación, derivación del esquema, operaciones CRUD, validación, paginación, autenticación básica, manejo uniforme de errores y ejecución de pruebas. Las capacidades avanzadas de colas, programación, vistas, observabilidad ampliada, idempotencia, OpenAPI y entrega durable de eventos podrán incorporarse progresivamente sin condicionar la medición central del boilerplate.

Como caso de referencia se utilizará un agregado de órdenes compuesto por una raíz, líneas de detalle, un objeto de valor monetario, una acción de pago y una proyección del total. Este escenario permite verificar identidad, relaciones, persistencia embebida, exposición de acciones, serialización y consultas sin introducir una complejidad ajena al objetivo del estudio.

REFERENCIAS BIBLIOGRÁFICAS

Alkazemi, B. Y., & Nour, M. K. (2025). XBoot: A RAPID and instructional low-code generator for Spring Boot applications. *Applied Sciences*, *15*(19), 10621. [https://doi.org/10.3390/app151910621](https://doi.org/10.3390/app151910621)

Bobadilla Chara, S. G. (2022). *Desarrollo de un framework con una arquitectura basada en microservicios para el UP-Grade del Sistema de Planificación de Recursos Empresariales de la UCSM* [Tesis de grado, Universidad Católica de Santa María (Arequipa)]. [https://hdl.handle.net/20.500.12920/11796](https://hdl.handle.net/20.500.12920/11796)

Campos Salcedo, J., & Reyes Huamán, M. (2025). Herramientas y modelos tecnológicos para la gestión del conocimiento en el desarrollo de software: Una revisión sistemática y análisis de impactos y desafíos. *Revista Peruana de Computación y Sistemas*, *7*(1), 53–64. [https://doi.org/10.15381/rpcs.v7i1.30500](https://doi.org/10.15381/rpcs.v7i1.30500)

Chavez Chavez, A., & Wong Portillo, L. (2022). EasyRest: Generador automático de API Rest basado en Spring Framework y motor de plantillas Beetl. *Revista Peruana de Computación y Sistemas*, *4*(1), 25–35. [https://doi.org/10.15381/rpcs.v4i1.24125](https://doi.org/10.15381/rpcs.v4i1.24125)

Cosme Escalera, S. Y., & Quispe Cansaya, D. D. (2024). *Arquitectura de software basada en microservicios para el desarrollo de aplicaciones web de la empresa Group de Mercado, Juliaca 2022* [Tesis de grado, Universidad Nacional del Altiplano (Puno)]. [https://repositorio.unap.edu.pe/items/24c469c5-566d-4c4c-9866-b18130631565](https://repositorio.unap.edu.pe/items/24c469c5-566d-4c4c-9866-b18130631565)

DORA & Google Cloud. (2024). *Accelerate state of DevOps report 2024: Fostering culture with artificial intelligence* [Research report]. DevOps Research and Assessment. [https://dora.dev/research/2024/dora-report/](https://dora.dev/research/2024/dora-report/)

Evans, E. (2003). *Domain-driven design: Tackling complexity in the heart of software*. Addison-Wesley.

Fielding, R. T. (2000). *Architectural styles and the design of network-based software architectures* [Tesis doctoral, University of California, Irvine]. [https://ics.uci.edu/~fielding/pubs/dissertation/top_html.htm](https://ics.uci.edu/~fielding/pubs/dissertation/top_html.htm)

Fowler, M. (2002). *Patterns of enterprise application architecture*. Addison-Wesley Professional.

Gnanasambandam, C., Harrysson, M., Hussin, A., Keovichit, J., & Srivastava, S. (2023). *Yes, you can measure software developer productivity* [Research report]. McKinsey & Company. [https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/yes-you-can-measure-software-developer-productivity](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/yes-you-can-measure-software-developer-productivity)

Gurgul, V., Gubela, R., & Lessmann, S. (2026). The state of generative AI in software development: Insights from literature and a developer survey [Preprint]. arXiv. [https://arxiv.org/abs/2603.16975](https://arxiv.org/abs/2603.16975)

Harding, W., & Kloster, M. (2024). *Coding on Copilot: 2023 data **shows** downward pressure on code quality*. GitClear. [https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality)

Jones, M., Bradley, J., & Sakimura, N. (2015). *JSON Web Token (JWT)* (RFC 7519). Internet Engineering Task Force. [https://doi.org/10.17487/RFC7519](https://doi.org/10.17487/RFC7519)

Karlsson, S., Jongeling, R., Čaušević, A., & Sundmark, D. (2024). Exploring behaviours of RESTful APIs in an industrial setting. *Software Quality Journal*, *32*, 1287–1324. [https://doi.org/10.1007/s11219-024-09686-0](https://doi.org/10.1007/s11219-024-09686-0)

Levezinho, M., Kapferer, S., Zimmermann, O., & Silva, A. R. (2024). Domain-driven design representation of monolith candidate decompositions based on entity accesses [Preprint]. arXiv. [https://arxiv.org/abs/2407.02512](https://arxiv.org/abs/2407.02512)

Ma, Y., Huang, Y., & Leach, K. (2024). Breaking the flow: A study of interruptions during software engineering activities. In *Proceedings of the IEEE/ACM 46th International Conference on Software Engineering (ICSE ’24)* (pp. 1–12). [https://doi.org/10.1145/3597503.3639079](https://doi.org/10.1145/3597503.3639079)

Özkan, O., Babur, Ö., & van den Brand, M. (2025). Domain-driven design in software development: A systematic literature review on implementation, challenges, and effectiveness. *Journal of Systems and Software*, *230*, Article 112537. [https://doi.org/10.1016/j.jss.2025.112537](https://doi.org/10.1016/j.jss.2025.112537)

Peldszus, S., Rutenkolk, J., Heide, M., Sollmann, J., Klatt, B., Köhne, F., & Berger, T. (2026). Developer perspectives on REST API usability: A study of REST API guidelines [Manuscrito de autor]. IT University of Copenhagen; Ruhr University Bochum; viadee AG; Chalmers University of Technology. [Preprint]. arXiv. [https://arxiv.org/abs/2601.16705](https://arxiv.org/abs/2601.16705)

Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). The impact of AI on developer productivity: Evidence from GitHub Copilot [Preprint]. arXiv. [https://arxiv.org/abs/2302.06590](https://arxiv.org/abs/2302.06590)

Pizarro Romero, A. P., & Paredes Orihuela, J. L. (2025). *Optimización del desarrollo de software con GitHub **Copilot**: Análisis comparativo de productividad y calidad en una empresa de Lima 2024* [Tesis de grado, Universidad Tecnológica del Perú (Lima)]. [https://hdl.handle.net/20.500.12867/12741](https://hdl.handle.net/20.500.12867/12741)

Sadik, A., Brulin, S., & Olhofer, M. (2023). *Coding by design: GPT-4 empowers agile model driven development* [Preprint]. Honda Research Institute Europe. arXiv. [https://arxiv.org/abs/2310.04304](https://arxiv.org/abs/2310.04304)

Stack Overflow. (2024). *Stack Overflow developer survey 2024*. [https://survey.stackoverflow.co/2024/](https://survey.stackoverflow.co/2024/)

Stack Overflow. (2025). *Stack Overflow developer survey 2025*. [https://survey.stackoverflow.co/2025/](https://survey.stackoverflow.co/2025/)

Trebejo Loayza, W. J. (2023). *Herramienta para el modelado y generación de código de arquitecturas de software basadas en microservicios* [Tesis de maestría, Universidad Nacional Mayor de San Marcos (Lima)]. [https://hdl.handle.net/20.500.12672/19678](https://hdl.handle.net/20.500.12672/19678)

Vasquez Pari, M. L. (2025). *Inteligencia artificial en la productividad de una empresa desarrolladora de software en la ciudad de Trujillo, 2025* [Tesis de maestría, Universidad Privada Antenor Orrego (Trujillo)]. [https://hdl.handle.net/20.500.12759/92452](https://hdl.handle.net/20.500.12759/92452)

Villanueva Campos, C. E. (2024). *Software de control y su impacto en el sector empresarial 2024* [Trabajo de investigación, Universidad Señor de Sipán (Pimentel, Lambayeque)]. [https://hdl.handle.net/20.500.12802/12931](https://hdl.handle.net/20.500.12802/12931)

ANEXOS

- ANEXO 1 - FORMATO N°3: MATRIZ BÁSICA DE CONSISTENCIA

**Título del Proyecto:**

IMPLEMENTACIÓN DE UN FRAMEWORK BASADO EN DDD-LIVIANO CON AUTOGENERACIÓN DE ENDPOINTS PARA REDUCIR EL BOILERPLATE EN APIS REST EN 2026

**Nombre del Tesista:**

**Pacheco Brophy Luis Ernesto**

| Código | Preguntas | Hipótesis | Objetivos |
| --- | --- | --- | --- |
| G | ¿En qué medida la implementación de un framework basado en DDD-liviano con autogeneración de endpoints reduce el código boilerplate en el desarrollo de APIs REST? | La implementación de un framework basado en DDD-liviano con autogeneración de endpoints reduce significativamente el código boilerplate en el desarrollo de APIs REST. | Diseñar e implementar un framework basado en DDD-liviano con autogeneración de endpoints que reduzca el código boilerplate en el desarrollo de APIs REST. |
| E1 | ¿Cuál es el nivel actual de código boilerplate generado durante el desarrollo manual de APIs REST siguiendo el paradigma DDD? | El código boilerplate presente en el desarrollo convencional de APIs REST bajo el paradigma DDD representa un porcentaje significativo del total de líneas de código, concentrándose principalmente en controladores, servicios, repositorios, DTOs y mappers. | Analizar y cuantificar el código boilerplate presente en el desarrollo convencional de APIs REST bajo el paradigma DDD, identificando los componentes con mayor nivel de replicación estructural. |
| E2 | ¿Qué componentes del ciclo de desarrollo de una API REST (controladores, servicios, repositorios, DTOs y mappers) presentan mayor replicación estructural y pueden ser autogenerados a partir del modelo de dominio? | El diseño de una arquitectura basada en mecanismos de autogeneración de controladores, servicios, repositorios, DTOs y mappers a partir del modelo de dominio permite cubrir los patrones esenciales del DDD-liviano. | Diseñar la arquitectura del framework, definiendo los mecanismos de autogeneración de controladores, servicios, repositorios, DTOs y mappers a partir del modelo de dominio. |
| E3 | ¿Es factible la implementación del framework en un escenario real de desarrollo de APIs REST? | La implementación del framework con sus módulos de autogeneración genera endpoints funcionales, compilables y libres de errores en un escenario de desarrollo real. | Implementar el framework con sus módulos de autogeneración de endpoints y validarlo en un escenario de desarrollo real. |
| E4 | ¿En qué porcentaje se reduce el tiempo de desarrollo y las líneas de código repetitivas, y cuál es el nivel de calidad del código generado por el framework en comparación con el desarrollo manual? | El uso del framework reduce significativamente el tiempo de desarrollo y mantiene o mejora la calidad del código generado, en comparación con el desarrollo manual. | Evaluar la reducción del código boilerplate, el tiempo de desarrollo y la calidad del código generado mediante comparación controlada con el desarrollo manual. |

| ELABORÓ | REVISÓ | APROBÓ | COPIA CONTROLADA |
| --- | --- | --- | --- |
|  |  |  |  |

- ANEXO 2 - FORMATO N°4 MATRIZ DE OPERACIONALIZACIÓN DE LAS VARIABLES

| Definición Conceptual | Definición Operacional | Dimensiones | Indicadores | Ítems |
| --- | --- | --- | --- | --- |
| Un framework basado en DDD-liviano con autogeneración de endpoints es una estructura de soporte que selecciona los patrones tácticos esenciales del Domain-Driven Design agregados, repositorios y servicios de dominio y utiliza reflexión o metaprogramación para inspeccionar el modelo de dominio y generar automáticamente controladores, servicios, repositorios, DTOs y mappers. La selección de patrones se sustenta en Evans (2003) y la automatización del código de infraestructura o plumbing en Fowler (2002), Alkazemi y Nour (2025) y Trebejo Loayza (2023). | Se operacionaliza como el conjunto de módulos y mecanismos que transforman un modelo de dominio en artefactos de aplicación e infraestructura para una API REST en PHP. Se evaluará mediante la cuantificación previa del boilerplate y el diseño arquitectónico del framework, considerando los mecanismos de autogeneración, las reglas de transformación modelo-código y la cobertura de patrones DDD-liviano soportados. | Cuantificación del boilerplate | Líneas de código (LOC) por componente (controlador, servicio, repositorio, DTO, mapper) | Ficha de análisis de código (checklist de componentes boilerplate) Herramienta de análisis estático (SonarQube/PHPMD) y herramienta de conteo de líneas (cloc) |
|  |  |  | Porcentaje de código repetido/estructuralmente similar entre módulos |  |
|  |  |  | Número de componentes con patrón replicable identificado |  |
|  |  | Diseño arquitectónico del framework | Número de mecanismos de autogeneración implementados (controladores, servicios, repositorios, DTOs y mappers) | Matriz de trazabilidad entre el modelo de dominio y los artefactos generados Lista de verificación del cumplimiento de patrones DDD-liviano |
|  |  |  | Número de reglas de transformación modelo-código implementadas |  |
|  |  |  | Porcentaje de patrones DDD-liviano cubiertos |  |
| La reducción del código boilerplate en APIs REST es la disminución medible del código de infraestructura necesario para el funcionamiento del sistema que no expresa lógica de dominio. En esta investigación comprende la reducción de líneas escritas manualmente, del tiempo de desarrollo y de la duplicación, manteniendo o mejorando la calidad del código generado. El concepto se sustenta en el plumbing descrito por Fowler (2002) y en la evidencia sobre automatización y productividad de Alkazemi y Nour (2025), Pizarro Romero y Paredes Orihuela (2025) y Vasquez Pari (2025). | Se medirá mediante una comparación controlada pre-test/post-test del mismo conjunto de endpoints CRUD: desarrollo manual frente al desarrollo asistido por el framework. Se compararán las líneas de código manuales, los archivos o clases autogenerados, el tiempo de desarrollo, la duplicación, los errores o bugs, el cumplimiento de estándares de codificación y el índice de mantenibilidad. | Reducción de código (cantidad) | Porcentaje de reducción de LOC escritas manualmente (pre-test frente a post-test) | Ficha de comparación pre-test/post-test y resultados de cloc |
|  |  |  | Número de archivos o clases generados automáticamente |  |
|  |  | Reducción de tiempo de desarrollo | Tiempo de desarrollo en minutos para el mismo conjunto de endpoints CRUD | Bitácora cronométrica de registro de tiempos |
|  |  |  | Porcentaje de reducción del tiempo de desarrollo |  |
|  |  | Calidad del código generado | Número de errores o bugs detectados (manual frente a generado) | SonarQube y PHPMD Cuestionario de percepción a desarrolladores (escala Likert) Lista de cotejo de buenas prácticas de codificación |
|  |  |  | Porcentaje de cumplimiento de estándares de codificación |  |
|  |  |  | Índice de mantenibilidad del código |  |

- ANEXO 3 - FORMATO N°5: MATRIZ GENERAL DE CONSISTENCIA.

| **Título**: IMPLEMENTACIÓN DE UN FRAMEWORK BASADO EN DDD-LIVIANO CON AUTOGENERACIÓN DE ENDPOINTS PARA REDUCIR EL BOILERPLATE EN APIS REST EN 2026 **Nombre del Tesista**: Pacheco Brophy Luis Ernesto |
| --- |
| Problemas | Objetivos | Hipótesis | Variables / Indicadores | Metodología |
| General ¿En qué medida la implementación de un framework basado en DDD-liviano con autogeneración de endpoints reduce el código boilerplate en el desarrollo de APIs REST? Específicos ¿Cuál es el nivel actual de código boilerplate generado durante el desarrollo manual de APIs REST? ¿Qué componentes presentan mayor replicación estructural y pueden ser autogenerados? ¿En qué porcentaje se reduce el tiempo de desarrollo, las líneas de código, y cuál es la calidad del código generado? ¿Es factible la implementación del framework en un escenario real? | General Diseñar e implementar un framework basado en DDD-liviano con autogeneración de endpoints que reduzca el código boilerplate en el desarrollo de APIs REST. Específicos Analizar y cuantificar el código boilerplate presente en el desarrollo convencional. Diseñar la arquitectura del framework y los mecanismos de autogeneración. Implementar el framework y validarlo en un escenario de desarrollo real. Evaluar la reducción del código, el tiempo de desarrollo y la calidad mediante comparación controlada. | General La implementación de un framework basado en DDD-liviano con autogeneración de endpoints reduce significativamente el código boilerplate en el desarrollo de APIs REST. Específicos El boilerplate representa un porcentaje significativo de líneas de código en controladores, servicios, repositorios, DTOs y mappers. El diseño basado en el modelo de dominio cubre los patrones esenciales del DDD-liviano. La implementación genera endpoints funcionales y libres de errores. El framework reduce el tiempo de desarrollo y mantiene/mejora la calidad frente al método manual. | Unidad de análisis: Artefactos de software (controladores, servicios, repositorios, DTOs, mappers). Variable Independiente: Framework basado en DDD-liviano con autogeneración. ***Dimensiones****:* Cuantificación del boilerplate, Diseño arquitectónico. ***Indicadores****:* N° de mecanismos de autogeneración, Reglas de transformación, Cobertura de patrones DDD. Variable Dependiente: Reducción del código boilerplate en APIs REST. ***Dimensiones****:* Reducción de LOC, Reducción de tiempo, Calidad de código. ***Indicadores****:* Porcentaje de reducción de LOC, Tiempo de desarrollo (min/horas), Índice de mantenibilidad, N° de bugs. | **Enfoque:** Cuantitativo. Diseño: cuasiexperimental de un solo grupo (pretest/postest). **Nivel:** Explicativo. **Tipo:** Aplicada / Tecnológica. Métodos: Inductivo, Deductivo, Analítico. Técnicas e instrumentos: *De muestreo:* No probabilístico intencional. *De recolección:* Gabinete (Análisis documental), Laboratorio (Observación métrica). *Procesamiento:* Tabulación matricial. *Análisis:* Prueba T de Student o Wilcoxon. **Población:** Componentes CRUD de la arquitectura backend. **Muestra:** Artefactos generados para un conjunto de 5 a 8 entidades del dominio. Procedimientos: Fase 1: Diagnóstico (Pre-test). Fase 2: Diseño del Framework. Fase 3: Implementación. Fase 4: Contraste estadístico (Post-test). |

| **ELABORÓ** | **REVISÓ** | **APROBÓ** | **COPIA CONTROLADA** |
| --- | --- | --- | --- |
|  |  |  |  |

- ANEXO 4 - INSTRUMENTOS DE RECOLECCIÓN DE DATOS

A continuación, se presentan los instrumentos diseñados para la recolección de datos de la investigación, en concordancia con las técnicas descritas en el apartado 3.7 del proyecto de tesis.

- Instrumento N° 1: Ficha de análisis de código (checklist de componentes boilerplate)

Propósito: registrar y clasificar el nivel de replicación estructural por componente durante la fase de diagnóstico (pre-test).

| **N°** | **Componente** | **LOC total** | **LOC repetidas / similares** | **¿Patrón replicable identificado? (Sí/No)** | **Observaciones** |
| --- | --- | --- | --- | --- | --- |
| 1 | Controlador |  |  |  |  |
| 2 | Servicio |  |  |  |  |
| 3 | Repositorio |  |  |  |  |
| 4 | DTO |  |  |  |  |
| 5 | Mapper |  |  |  |  |

- Instrumento N° 2: Guía de observación y lista de cotejo métrico

Propósito: registrar objetivamente los indicadores dependientes vinculados a las salidas de las herramientas de análisis estático (SonarQube, PHPMD, cloc).

| **Indicador** | **Herramienta** | **Valor pre-test (manual)** | **Valor post-test (framework)** | **Observaciones** |
| --- | --- | --- | --- | --- |
| Líneas de código (LOC) escritas a mano | cloc |  |  |  |
| Porcentaje de duplicación de código | SonarQube / PMD |  |  |  |
| Densidad de errores / bugs detectados | SonarQube |  |  |  |
| Porcentaje de cumplimiento de estándares (linting) | PHPMD |  |  |  |
| Índice de mantenibilidad | SonarQube |  |  |  |

- Instrumento N° 3: Bitácora cronométrica (registro de tiempos)

Propósito: registrar el tiempo en horas y minutos invertido en la configuración inicial y el desarrollo del scaffolding, tanto en la fase manual como en la automatizada.

| **Entidad** | **Actividad** | **Modalidad (Manual/Framework)** | **Hora inicio** | **Hora fin** | **Tiempo total** | **Observaciones** |
| --- | --- | --- | --- | --- | --- | --- |
|  | Scaffolding CRUD |  |  |  |  |  |
|  | Scaffolding CRUD |  |  |  |  |  |
|  | Scaffolding CRUD |  |  |  |  |  |
|  | Scaffolding CRUD |  |  |  |  |  |
|  | Scaffolding CRUD |  |  |  |  |  |

- Instrumento N° 4: Cuestionario de percepción a desarrolladores (Escala Likert)

Propósito: recoger la percepción de los desarrolladores respecto a la usabilidad, calidad y utilidad del framework. Escala: 1 = Muy en desacuerdo, 5 = Muy de acuerdo.

| **N°** | **Ítem** | **1 (Muy en desacuerdo)** | **2** | **3** | **4** | **5 (Muy de acuerdo)** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | El framework facilita la generación de controladores, servicios, repositorios, DTOs y mappers. |  |  |  |  |  |
| 2 | El código generado automáticamente es fácil de comprender y mantener. |  |  |  |  |  |
| 3 | El uso del framework redujo el tiempo dedicado a tareas repetitivas de scaffolding. |  |  |  |  |  |
| 4 | El código generado cumple con los estándares de codificación esperados. |  |  |  |  |  |
| 5 | Recomendaría el uso de este framework en proyectos reales de desarrollo backend. |  |  |  |  |  |

- Instrumento N° 5: Lista de cotejo de buenas prácticas de codificación

Propósito: verificar el cumplimiento de buenas prácticas de codificación en el código generado por el framework.

| **N°** | **Criterio** | **Cumple (Sí)** | **No cumple (No)** | **Observaciones** |
| --- | --- | --- | --- | --- |
| 1 | Los nombres de clases, métodos y variables siguen una convención consistente. |  |  |  |
| 2 | No existen bloques de código duplicados entre las entidades generadas. |  |  |  |
| 3 | Cada clase cumple con el principio de responsabilidad única (SRP). |  |  |  |
| 4 | El código generado compila sin advertencias ni errores. |  |  |  |
| 5 | Las dependencias entre capas (dominio, aplicación, infraestructura) están correctamente separadas. |  |  |  |
| 6 | El código cuenta con manejo adecuado de excepciones. |  |  |  |

- ANEXO 5 - Informe de validez y confiabilidad de los instrumentos

**Validez: Ficha de validación por Juicio de Expertos**

Los instrumentos de recolección documental y las bitácoras cronométricas serán sometidos a validación mediante la técnica de Juicio de Expertos. Tres especialistas con grado académico en Ingeniería Informática o áreas afines evaluarán la pertinencia, claridad y congruencia de los formatos, conforme a la siguiente ficha:

Instrumento evaluado: __________________________________________________

Nombre del experto: ____________________________________________________

Grado académico: _______________________________________________________

Especialidad: ___________________________________________________________

| **N°** | **Criterio** | **Deficiente** | **Regular** | **Bueno** | **Muy bueno** | **Excelente** | **Observaciones** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Claridad |  |  |  |  |  |  |
| 2 | Objetividad |  |  |  |  |  |  |
| 3 | Actualidad |  |  |  |  |  |  |
| 4 | Organización |  |  |  |  |  |  |
| 5 | Suficiencia |  |  |  |  |  |  |
| 6 | Intencionalidad |  |  |  |  |  |  |
| 7 | Consistencia |  |  |  |  |  |  |
| 8 | Coherencia |  |  |  |  |  |  |
| 9 | Metodología |  |  |  |  |  |  |
| 10 | Pertinencia |  |  |  |  |  |  |

Opinión de aplicabilidad: ( ) Aplicable   ( ) Aplicable después de corregir   ( ) No aplicable

Firma del experto: _______________________     Fecha: _____ / _____ / 2026

**Confiabilidad**

Gran parte de la recolección de datos se apoya en software de análisis estático estandarizado (SonarQube, PHPMD, cloc), lo que otorga una confiabilidad y precisión paramétrica a variables como las líneas de código (LOC) y la complejidad del código. Para los registros cronométricos manuales (bitácora), se ejecutará una prueba piloto sobre un módulo de software de prueba, con el propósito de asegurar la consistencia y fiabilidad del proceso de medición de tiempos antes de la recolección oficial de datos.

- ANEXO 6 - REPORTE DE SIMILITUD TURNITIN

**Ilustración ****7** - Portada del reporte de similitud

**Ilustración ****8**** **- Reporte de similitud porcentaje

1