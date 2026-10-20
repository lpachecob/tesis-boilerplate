Revista PeRuana de ComPutaCión y sistemas 2022 4(1):25-3365 ISSN Online: 2617-2003
https://doi.org/10.15381/rpcs.v4i1.24125 Facultad de IngenIería de SIStemaS e InFormátIca
unIverSIdad nacIonal mayor de San marcoS
Artículo de Contribución
EasyRest: Generador automático de API Rest basado en
Spring Framework y motor de plantillas Beetl
Automated Rest API generator based on Spring Framework and Beetl
template engine
Alvaro Chavez Chavez 1,a, Lenis Wong Portillo 1,b
1 Universidad Nacional Mayor de Marcos, Facultad de Ingeniería de Sistemas e Informática. Lima, Perú
a Autor de correspondencia: alvaro.chavez4@unmsm.edu.pe - ORCID: https://orcid.org/0000-0001-7638-8636
b E-mail: lwongp@unmsm.edu.pe - ORCID: https://orcid.org/0000-0002-5032-3233
Resumen
En la actualidad API REST es el enfoque de desarrollo de aplicaciones más usado a nivel mundial, sin embargo, un gran porcentaje
del desarrollo es repetitivo. La repetición en el desarrollo genera pérdidas de tiempo y dinero. En el presente estudio se propone
EasyRest, un proyecto de generación automática de API Rest basado en Spring Framework. Para el desarrollo de esta propuesta se
realizó la construcción de un arquetipo personalizado en Apache Maven. Además, se realizó la construcción de los templates basados
en Beetl. La propuesta genera un proyecto backend Rest, que contiene controladores, servicios y repositorios. Los resultados obteni-
dos con la propuesta pudieron reducir significativamente el tiempo necesario para la construcción del API Rest, en comparación a una
construcción manual. Como conclusión la propuesta EasyRest permite la creación automática de API’s Rest en un mínimo de tiempo
de desarrollo, automatizando el desarrollo de proyectos backend.
Palabras clave: Generador API Rest; Spring Framework Project; Generador Java Project Code; Generador de Proyecto MVC.
Abstract
API REST is currently the most widely used application development approach worldwide, however, a large percentage of develop-
ment is repetitive. Repetition in development generates waste of time and money. For this purpose, EasyRest is proposed, a project
for automatic generation of API Rest based on Spring Framework. For the development of this proposal, a custom archetype was built
in Apache Maven. In addition, the construction of templates based on Beetl is performed. The proposal generates a Rest backend
project, which contains controllers, services and repositories. The results obtained with the proposal were able to significantly reduce
the time required for the construction of API Rest, compared to a manual construction. As a conclusion, the EasyRest proposal allows
the automatic creation of API's Rest in a minimum of development time, automating the development of backend projects.
Keywords: API Rest Generator; Spring Framework Project; Java Project Code Generator; MVC Project Generator.
Correspondencia:
XXX
Recibido: 28/06/2022 - Aceptado: 04/10/2022 - Publicado: 28/11/2022
Citar como:
Chavez, A. & Wong, L. (2022) EasyRest: Generador automático de API Rest basado en Spring Framework y motor de plantillas Beetl. Revista Peruana de
Computación y Sistemas, 4(1):25-35. https://doi.org/10.15381/rpcs.v4i1.24125
© Los autores. Este artículo es publicado por la Revista Peruana de Computación y Sistemas de la Facultad de Ingeniería de Sistemas e Informáticade la Universidad
Nacional Mayor de San Marcos. Este es un artículo de acceso abierto, distribuido bajo los términos de la licencia Creative Commons Atribución 4.0 Internacional (CC BY
4.0) [https://creativecommons.org/licenses/by/4.0/deed.es] que permite el uso, distribución y reproducción en cualquier medio, siempre que la obra original sea debidamente
citada de su fuente original.
2255

Chavez & Wong
1. Introducción para la ejecución además se generará la documentación
automática mediante Swagger [10].
En la actualidad para desarrollar software se ne-
cesita un alto nivel técnico y una buena especificación En el capítulo 3 se describe un resumen del Estado
sin embargo muchas veces en el desarrollo de API Rest del Arte donde se realizaron 3 preguntas para la revisión
existen ciertos procesos que son repetitivos (operaciones
y una descripción por cada fase explicando los artículos
CRUD, generación de reportes, búsquedas típicas en
que más impactaron para el desarrollo de esta propuesta.
una BD, Test Unitarios, configuraciones) [1]. Realizar
En la Sección 4 se describe la propuesta, su estructura y
reiteradas veces dichas operaciones ocasiona pérdidas de
el flujo para la generación de API’s Rest. En la sección
tiempo y dinero [2], repetir código puede ocasionar pro-
5 se evalúa la propuesta desarrollada y finalmente en la
blemas de mantenimiento donde al modificar código se
Sección 6 se presenta la conclusión y trabajos futuros.
tendría que modificar en todos los valores repetidos ade-
más de tener un código difícil de mantener [3]. En el
2. Trabajos relacionados
desarrollo de software empresarial suceden situaciones
que pueden ocasionar demora, el nivel de complejidad La revisión sistemática de la literatura tomando en
aumenta y con ello el tiempo de desarrollo [4] . consideración el trabajo de [11] la cual cuenta las si-
guientes fases: Planificación de revisión, desarrollo de la
Por otra parte, desarrollar API’s Rest con Spring revisión y resultados y análisis de la revisión.
Framework [1] es muy sencillo, nos provee distintas
soluciones listas para usar y no tener que preocuparnos En la fase de planeamiento se consideraron tres
en escribir código de configuración, gestionar puertos preguntas, (P1) ¿Cuáles son las técnicas utilizadas para
o cargar un contenedor web [5]. A pesar de ello se tiene la generación de código?, (P2) ¿Qué tipo de propuestas
que construir distintas entidades (clase java que repre- están siendo implementadas?, (P3) ¿Qué formas de in-
senta una tabla), servicios (clases encargadas de la lógi- greso de requerimientos son utilizadas en los aportes?
ca de negocio), repositorios (clase relacionada con las
Para realizar la búsqueda de los potenciales artí-
operaciones de persistencia) y controladores (clase que
culos se utilizaron las siguientes palabras claves “Code
responde a acciones del usuario), archivos de configu-
generator Java”, “Code generator Api Rest”, “Automatic
ración, utilitarios, documentación de las API’s y ma-
generator Java”, “Automatic Generator Api Rest”, “Code
nejo de excepciones, realizar estas implementaciones
consumen tiempo además se vuelven repetitivas. Un generator Spring Boot”, la búsqueda de los artículos se
generador de código basado en Spring Framework es realizó en las bases de datos ScienceDirect, ResearchGa-
CRUDLeaf [6] que permite automatizar el proceso de te, IEEExplore, Springer Link.
creación mediante meta modelos, si bien esta propues-
Se establecieron los siguientes criterios de inclusión:
ta es muy interesante y reciente, agrega complejidad
Año de publicación entre 2018 y 2021, tipo de fuente
al usuario final obligando a entender la sintaxis de un
Journals o proceedings y artículos relacionados que res-
nuevo lenguaje además de no contar con las validacio-
pondan alguna de las tres preguntas de investigación.
nes correspondientes. Otro aporte muy interesante es
Automatic Code Generation of MVC Web Applica-
En la fase de desarrollo se realizó la búsqueda de
tions [7] que utiliza diagramas UML para la captación
los potenciales artículos teniendo en consideración los
de información previniendo errores al momento de
criterios de inclusión.
ingresar la información y metamodelos como plantilla
para generar código sin embargo los diagramas UML En la fase de resultados se obtuvieron 20 artículos
cada vez son menos utilizado depender de ello limita que se analizaron a través de una taxonomía obteniendo
su uso. Para la generación de código se puede utilizar las siguientes categorías: técnicas utilizadas, tipos de pro-
distintas técnicas una de ellas son los meta modelos, puestas, arquitecturas, cada categoría está relacionada a
Ariel Arsaute y su equipo [8] desarrollaron un genera- una pregunta de investigación planteada.
dor automático de API Rest basado en metamodelos
donde utilizan un formato XMI, el aporte solo brinda
Tabla 1. Clasificación de estudios
las clases generadas mas no un proyecto con las confi-
guraciones para su ejecución. Taxonomía Referencias Total
Técnicas Utilizadas [12], [6], [13], [14], [7], [15], 15
Con la finalidad de agilizar el desarrollo de cons-
(P1) [16], [17], [18], [19] [20], [8],
trucción de API’s Rest se propone EasyRest, un gene- [21], [22]
rador basado en Spring Framework [1] y el motor de Tipos de Propuestas [12], [6], [13], [14], [7], [15], 17
plantillas Beetl [9] donde se busca automatizar el proce- (P2) [16], [17], [18], [19] [20], [8],
[23], [25], [21], [22]
so de desarrollo de APÍ’s Rest permitiendo que a partir
de la lógica de negocio se genere entidades, repositorios Formas Ingreso de [12], [6], [13], [14], [7], [15], 14
Requerimientos [16], [18], [19], [8], [24], [25],
CRUD, servicios y controladores, así como archivos de
(P3) [21], [22]
configuración predefinidos, clases utilitarias y manejo de
excepciones. Las clases generadas serán agregadas al ar-
quetipo Maven que cuenta con una estructura definida En las técnicas utilizadas para generar la generación
y un archivo pom.xml con las dependencias necesarias de código se lograron clasificar 4, generación de código
26 Revista Peruana de Computación y Sistemas 2022; 4(1)

EasyRest: Generador automático de API Rest basado en Spring Framework y motor de plantillas Beetl
a partir de meta-modelos [6], [7], [15], [16], [18], [19], abierto para la creación de aplicaciones empresariales
[8], [21], [22], reflexión [20], algoritmos de Inteligencia Java [1]. También se utilizará Maven [29] para la ges-
artificial [17], [18], [12], [13], [14]. El tipo de técni- tión de dependencias además de Lombok [30] para la
ca a considerar es la generación de código a partir de reducción de código y Swagger [10] para la generación
meta-modelos ya que permite establecer plantillas que automática de la documentación.
serán utilizadas para la generación de código [26]. En
el artículo Automatic Code Generation of MVC Web En la Fig. 1 se ejemplifica el flujo de construcción
Applications [7], se propone un software para traducir de una API Rest mediante EasyRest. Como primer paso
diagramas del lenguaje de modelado unificado (UML) se realizará el ingreso de la información mediante una
en código orientado a objetos, la generación automática petición http, dicha petición que será interceptada por
de código a través de la propuesta ayuda a los diseñado- el Business Controller (2) que se encargará de procesar
res a entregar software en intervalos cortos de tiempo. la petición e invocar a los Generadores (3).
Para realizar la implementación utilizaron metamodelos
para los casos de uso y clases además de la herramien-
ta XGenerator [7] que transforma dichos modelos en
clases java todo ello basado en una arquitectura Mode-
lo-Vista-Controlador.
Dentro del tipo de propuestas como resultado de
la revisión se lograron identificar 4, generación de API
Rest [7], [15], [25], [24], [20], [8], generación de Casos
de prueba [13], [14], [17], [18] , generación de Aplica-
ciones WEB [7], [16], [21] generación de código [12],
[19], [22] dentro de los artículos destaca CRUDyLe- Fig. 1. Flujo de EasyRest
af [6] que desarrollaron un DSL basado en texto para
construir API REST de Spring Boot mediante opera-
El módulo de generadores se divide en 4, cada di-
ciones CRUD. A partir de una sintaxis del CRUDyLeaf
visión se encarga de generar una capa de la API Rest.
DSL se definen las propiedades necesarias para la cons-
El generador de controladores se encarga de generar
trucción del proyecto además utilizaron XTend [27], un
los controladores necesarios para el funcionamiento de
lenguaje para escribir el generador de código a partir del
la API Rest. El generador de Entidades se encarga del
DSL propuesto, para crear una API Rest que contenga
mapeo entre objetos Java y de agregar las anotaciones
diferentes operaciones CRUD se deberá seguir la gra-
necesarias para que la clase sea utilizada como una enti-
mática propuesta en el DSL, así como especificar el en-
dad que estará asignada a una tabla de base de datos. El
dpoint de salida de la API, el tipo de dato de los campos,
generador de Servicios se encargará de manejar la lógica
groupId, artifactId y demás propiedades.
de negocio, así como las invocaciones del controlador y
En las formas de ingreso de requerimientos del las peticiones al repositorio. El generador de repositorio
usuario como resultado de la revisión se lograron iden- se encargará de realizar las funciones básicas de CRUD a
tificar 4, ingreso de información mediante código [6], la base de datos mediante JpaRepository [31].
[8], [12], [13], [14] [15], diagramas UML [7], [19],
Para que los generadores creen las clases Java es ne-
[22], formularios [16], [25] y en formato JSON [18],
cesario definir templates (4), para ello se dispondrá de
[21], [24], [25], destacando el ingreso de información
una clase y una interfaz template por cada división del
en formato JSON al ser una forma de ingreso simple
generador que funcionan como plantillas donde se agre-
de utilizar sin tener que aprender algún lenguaje nuevo
ga los datos ingresados por el usuario según la lógica de
o depender de los diagramas, dentro de esta categoría
negocio. Las clases generadas deberán ser almacenadas
destaca Automatic Generation of Test Cases for REST
APIs : a Specification-Based Approach [25] que a partir en el Arquetipo de un Proyecto Spring (5), dicho arque-
de requerimientos de usuario utilizando metamodelos tipo contendrá algunas clases por defecto como utilita-
generan casos de prueba, un punto muy importante es rios, archivos de configuración, así como también con-
la adaptación del ingreso de información a la especifica- tendrá el archivo POM con las dependencias necesarias
ción OpenAPI [28]. para una compilación exitosa del API Rest generado.
Para una mejor comprensión del gráfico, se divi-
3. EasyRest: Generador API Rest
dirá el flujo del sistema en 6 pasos que se explicaran a
En el presenta trabajo proponemos EasyRest, un continuación.
software novedoso para generar API Rest en Spring Fra-
mework y documentación automática en Swager a par- 3.1. Ingreso de información
tir de datos ingresados en formato JSON mediante una
El ingreso de información solicitada por el genera-
petición Rest.
dor consta de 4 partes: propiedades del proyecto, pro-
La API Rest generada estará construida con el piedades para la documentación de las Apis Rest, pro-
Framework Spring, Spring es un framework de código piedades de seguridad e información del negocio.
Revista Peruana de Computación y Sistemas 2022; 4(1) 27

Chavez & Wong
3.1.1 Propiedades del Proyecto. Las propiedades del cionada se utilizará para generar las entidades, controla-
proyecto están vinculadas al nombre de la compañía, dores, servicios y repositorios que serán detallados en los
nombre del proyecto, versión del proyecto, puerto que siguientes capítulos.
será utilizado por el proyecto y ruta base de las Apis del
3.2. Controlador de peticiones
proyecto. Esta información será utilizada para definir la
estructura del proyecto e información general.
Se realizará una petición http de tipo POST con
3.1.2 Propiedades para la documentación. Es nece- la información solicitada al controlador del generador
sario información de contacto que será utilizada para de API Rest como se muestra en la figura 3. El contro-
documentar la Api Rest como descripción del proyecto, lador de peticiones capturará la petición y transformará
email, página web y tipo de licencia del proyecto. el JSON [32] enviado en un objeto Java e invoca al ge-
nerador central para el procesamiento de la información
3.1.3 Propiedades de seguridad. Para el consumo de y generación del proyecto Java, como respuesta de la
las API Rest es necesario autentificarse es por ello que petición se obtendrá un archivo con extensión zip que
será necesario proporcionar las credenciales de acceso contendrá el proyecto generado.
que se utilizará.
3.3. Definición del arquetipo del proyecto
3.1.4 Información del negocio. Contiene la informa-
ción del negocio, información como nombre del objeto, Un arquetipo es un artefacto muy simple, que con-
nombre de la tabla en la base de datos, descripción, ruta tiene el prototipo del proyecto que desea crear. Maven
que será utilizada por el api Rest y los distintos campos provee distintos arquetipos para ser utilizado en proyec-
como se visualiza en la Figura 2. La información propor- tos Java [33].
Fig. 2. Información del negocio
Fig. 3. Controlador peticiones
28 Revista Peruana de Computación y Sistemas 2022; 4(1)

EasyRest: Generador automático de API Rest basado en Spring Framework y motor de plantillas Beetl
A continuación, se detalla la estructura del arquetipo. paquete de utilitarios que contendrá clases de apoyo, así
como los paquetes de configuración, manejo de excep-
3.3.1 Estructura del proyecto generado. La estruc-
ciones y un archivFo con las credenciales a la base de
tura del proyecto generado por IziRest estará dividido
datos. En la Fig. 5 se muestra la estructura del proyecto
por paquetes donde cada paquete cumple una función
generado por EasyRest.
determinada y la comunicación entre paquetes será
mediante interfaces como se visualiza en la figura 4.
Fig. 4. Estructura del proyecto
generado por EasyRest
• Controller: Contendrá las clases encargadas
de responder a solicitudes Rest enviadas por el
cliente, las clases y los métodos de este paquete
utilizaran anotaciones definidas en Spring Fra-
mework para peticiones Http.
• Model: Contendrá las clases java que serán
utilizadas como una entidad, dichas clases
estarán relacionadas a una tabla en la base de
datos.
• Service: Contendrá las clases encargadas de la
lógica de negocio, desde esta capa se podrá in-
vocar al repositorio o a otros servicios.
• Repository: Basado en el patrón repositorio
contendrá las clases que serán utilizadas para la
persistencia de los datos, así como el almacena-
miento, obtención y búsqueda a una entidad.
3.3.2 Nomenclatura de clases e interfaces. Para nom-
brar clases e interfaces generadas se realizará el uso de
convenciones de nomenclatura [34]. Por ejemplo, para Fig. 5. Estructura de un proyecto generado con EasyRest
nombrar a una interfaz del controlador de producto
usaremos la letra “I” como prefijo seguido de la palabra
3.4. Definición y creación de templates
Producto y “Controller” como sufijo. En la Tabla 2 se
muestra los siguientes casos para la API Product.
Si bien a partir del manejo de templates es posi-
ble generar código, el objetivo de esta propuesta no es
Tabla 2. Nomenclatura utilizada para las clases generadas generar la mayor cantidad de código sino generar la mí-
Capa Clase Interfaz nima cantidad de código que a su vez sea legible y apli-
que buenas prácticas de programación como principios
Controller ProductController IProductController
SOLID [35] en el código generado. Para la creación y
Service ProductService IProductService
manejo de templates se utilizará Beetl [9], Beetl es un
Entity ProductEntity
motor de plantillas con funciones completas, de rendi-
Repository ProductRepository IProductRepository
miento ultra alto y que tiene una gramática muy simple
similar a Javascript además de una fácil integración con
3.3.3 Arquetipo del proyecto generado. Como se distintos marcos Web.
mencionó anteriormente se creará un arquetipo Maven
[33] personalizado basado en la estructura del proyecto Beetl [9] funciona como una plantilla que es capaz
detallada en el punto 3.3.1 dentro de cada paquete se de recibir información enviada mediante programación.
generarán las clases con las nomenclaturas mencionadas Para la creación de los templates se creó distintas planti-
en el punto 3.3.2 además en el arquetipo se agregará un llas que serán detalladas a continuación.
Revista Peruana de Computación y Sistemas 2022; 4(1) 29

Chavez & Wong
3.4.1 Plantilla Entity. Una “entidad” es una clase mediante la lógica de negocio además es necesario que
que representa a una tabla, en la plantilla se puede esta- la interfaz extienda de IGenericRepository para acceder a
blecer las características que tendrá la entidad para ello métodos de persistencia.
se presenta la Tabla 3.
3.4.3 Plantillas para los servicios. Se ha dividido la
generación de servicios en 2 plantillas, plantilla de la in-
Tabla 3. Características plantilla Entity
terfaz del servicio y plantilla de la implementación del
Característica Descripción Valores servicio.
Id de la tabla permite identificar de forma
única las filas de la tabla Auto incremental Debido a que todos los servicios generados imple-
Nombre de la mentaran los métodos de la Fig. 6 es necesario centra-
- -
columna lizar los métodos para ello se ha agregado al prototipo
Definición de la Indica el tipo formato en el
Fecha corta, larga la clase abstracta GenericServiceImpl que se encarga de
columna campo fecha
invocar al repositorio respectivo para ejecutar los méto-
Obligatorio Indica si un campo es obligatorio Verdadero, falso
dos CRUD.
Único Indica si el campo es único en
Verdadero, falso
la tabla
Tamaño Indica el tamaño del campo de
-
tipo texto
La elección de una o más características depende
de las necesidades del usuario. En la plantilla se pue-
de asignar el nombre de la tabla, valores a los atributos
de la clase y permite la reducción de código utilizando
anotaciones de Lombok además permite crear relaciones
entre entidades.
Fig. 6. Interfaz Genérica que provee métodos CRUD
3.4.2 Plantilla Repository. Spring Framework [5]
facilita gestionar las operaciones de persistencia contra La plantilla Interfaz Servicio deberá de extender
una tabla de la base de datos para ello nos provee dis- la clase IGenericService enviando la entidad correspon-
tintas interfaces. Para la realización de la plantilla se diente (Fig. 7).
creó una interfaz IGenericRepository donde se le envía
3.4.3.2 Plantilla Implementacion Servicio. La plan-
el tipo de objeto y el id, esta clase extiende de JpaRepo-
tilla ImplementacionServicio deberá de extender de la
sitory [31] que contiene todas las funciones relaciona-
clase abstracta GenericServiceServiceImpl enviando la en-
das a la persistencia.
tidad y el tipo de id además de sobrescribir el método
La plantilla repository tendrá la estructura de una getRepo() donde se enviará el repositorio respectivo. En
interfaz en Java el nombre de esta interfaz será manejada la Fig. 8 se visualiza la plantilla implementación servicio.
Fig. 7. Plantilla Interfaz Servicio
Fig. 8. Plantilla Implementación Servicio
30 Revista Peruana de Computación y Sistemas 2022; 4(1)

EasyRest: Generador automático de API Rest basado en Spring Framework y motor de plantillas Beetl
3.5. Documentación mediante Swagger muestra en la Fig. 10, si las credenciales no son correctas
no podrá hacer uso de ninguna API.
Documentar una API es una tarea muy importan-
te, pero a su vez laboriosa, por suerte existen muchas
4. Validación
herramientas que facilitan generar documentación. Para
generación automática de API Rest se utilizará la libre- Para la validación del aporte se desarrollará el
ría SpringFox que nos permite generar documentación backend Rest basado en Spring Framework de una
basada en Swagger según la lógica de negocio. Además, tienda online de productos Agrícolas, para ello se rea-
agrega información adicional que brindaran mayor in- lizará el desarrollo en dos casos de estudios, en el pri-
formación al usuario final, para ello se hace uso del tem- mer caso de estudio se realizará el desarrollo común
plate de documentación. En la Fig. 9 muestra la infor- del backend Rest y en el segundo caso se desarrollará
mación de contacto proporcionada por el usuario. con la propuesta.
3.6. Seguridad en las API REST En cada caso de estudio se tendrá las siguientes
operaciones por cada API Rest: consulta por id, consul-
Asegurar las API nos ayuda a protegernos de ata- tar todos, guardar, actualizar y eliminar. Las API Rest a
ques externos ya que exponemos una gran cantidad de desarrollar son Productos, Categorías, Usuarios y Órde-
datos e información personal. Para la seguridad en las nes tal como se muestra en la Tabla 4.
APIS se utilizará el módulo de seguridad de Spring Fra-
mework. Se implementará la seguridad de tipo Basic Como resultado de cada caso de estudio se obten-
Authentication y se agregará las credenciales proporcio- drá la misma arquitectura, estructura, nomenclatura del
nadas por el usuario. proyecto, nomenclatura de las clases en las distintas ca-
pas que fueron detalladas en el punto 3.3.2.
3.6.1. Autenticación de usuario. Para utilizar las
APIS es necesario autenticarse con las credenciales En la Tabla 5 mostrada a continuación se visualiza
proporcionadas por el usuario en el formulario que se las clases java que se obtendrán por la lógica de negocio
Fig. 9. Información de contacto documentación API Rest
Fig.10. Autenticación usuario.
Revista Peruana de Computación y Sistemas 2022; 4(1) 31

Chavez & Wong
Tabla 4. Funcionalidades por cada caso de estudio
Caso de Estudio Sujeto de estudio APIS Rest a validar Operaciones por cada API Rest Métricas
Tienda online de productos  Producto, categorías,  Consultar por id, consultar todos,  Tiempo de ciclo,
Con arquetipo
agrícolas usuarios, órdenes guardar, actualizar y eliminar Tasa de productividad por LOC
Con el generador  Tienda online de productos  Producto, categorías,  Consultar por id, consultar todos,  Tiempo de ciclo,
API Rest agrícolas usuarios, órdenes guardar, actualizar y eliminar Tasa de productividad por LOC
Tabla 5. Clases generadas en las distintas capas
| Entidad/ Capa | Controller |     | Service | Repository | Model |
| ------------- | ---------- | --- | ------- | ---------- | ----- |
Producto ProductController, IProductController ProductService, IProductService IProductRepository Product
Categoría CategoriaController, ICategoriaController CategoriaService, ICategoriaService ICategoryRepository Category
Usuario UserController, IUserController UserService, IUserService IUserRepository User
Orden OrderController, IOrderController OrderService, IOrderService IOrderRepository Order
para ambos casos de estudio, cabe mencionar que en la  El aporte género las siguientes cantidades de líneas
Tabla 5 no se tomó en consideración las clases de confi- por paquete como se visualiza en la Tabla 7.
guración, seguridad, utilitarios y excepciones.
Tabla 7. Cantidad de líneas generadas por tipo paquete.
Para el caso de estudio 1 se utilizará un arqueti-
po maven que contendrá las clases utilitarias, excep- Paquete LOC Generadas
ciones, configuraciones y dependencias necesarias para  CONFIG 98
el desarrollo del software, este arquetipo también se
|     |     |     | CONTROLLER |     | 415 |
| --- | --- | --- | ---------- | --- | --- |
encuentra incluido dentro del generador de API Rest.
|     |     |     | EXCEPTION |     | 147 |
| --- | --- | --- | --------- | --- | --- |
El objetivo de utilizar un arquetipo es centrarnos en
|     |     |     | REPOSITORY |     | 31  |
| --- | --- | --- | ---------- | --- | --- |
el desarrollo de la lógica de negocio y no en clases o
|     |     |     | SECURITY |     | 70  |
| --- | --- | --- | -------- | --- | --- |
archivos de configuración.
|     |     |     | SERVICE |     | 154 |
| --- | --- | --- | ------- | --- | --- |
Para el caso de estudio 2 se utilizará el software
|     |     |     | ÚTIL |     | 160 |
| --- | --- | --- | ---- | --- | --- |
generador de API Rest desarrollado en el aporte. El
|     |     |     | APP |     | 12  |
| --- | --- | --- | --- | --- | --- |
software generador de API Rest necesita de entrada un
JSON con la estructura detallada en el punto 3.1, la  RESOURCES 14
|     |     |     | POM |     | 140 |
| --- | --- | --- | --- | --- | --- |
información enviada será transformada a una clase Java
y será utilizada para generar el proyecto backend Rest  ENTITY 142
según la lógica de negocio.
|     |     |     | Total |     | 1383 |
| --- | --- | --- | ----- | --- | ---- |
Posteriormente se procederá a realizar la petición
Tiempo de ciclo. El tiempo de ciclo se calcula
http de tipo POST con la información solicitada en for-
mato de JSON. como la diferencia entre la fecha de terminación (FT)
y la fecha de inicio (FI). Con el sistema propuesto el
5.  Resultados y discusión tiempo de ciclo fue de 9 segundos aproximadamente
(ver ecuación 1).
A continuación, se detallan los resultados obteni-
dos del proceso de validación realizado al aporte pro-
  Tiempo Ciclo = FT - F I    (1)
puesto en el caso de estudio 1.
Entonces:
| 5.1.  | Con el generador de API REST |     |     |     |     |
| ----- | ---------------------------- | --- | --- | --- | --- |
  Tiempo Ciclo = 9 segundos
El tiempo que demoro en generar el proyecto bac-
kend rest con el aporte fue de 8827 milisegundos. En la  Tasa de automatización por LOC para cada Loc. La
Tabla 6 mostrada a continuación se visualiza la cantidad  tasa de automatización por cada linea de código ingre-
de líneas de código generadas según el tipo de archivo.
sada es de 6 lineas de código obtenidas, dicho valor se
obtuvo dividiendo la cantidad de líneas de código gene-
Tabla 6. Cantidad de líneas por tipo de archivo radas entre la cantidad de líneas de información ingresa-
das, tal como se observa en la ecuación 2.
| Tipos Archivos | Cantidad Líneas Código Fuente (LOC) |      |     |     |       |
| -------------- | ----------------------------------- | ---- | --- | --- | ----- |
| Java           |                                     | 1229 |     |     |   (2) |
| Properties     |                                     | 14   |     |     |       |
𝑥𝑥𝐴𝐴𝐴𝐴𝐴𝐴 𝑥𝑥𝐴𝐴𝐴𝐴𝐿𝐿𝐴𝐴𝐿𝐿 𝐺𝐺𝐿𝐿𝐴𝐴
𝑇𝑇.𝐴𝐴E𝐴𝐴𝐴𝐴n𝐴𝐴t𝐴𝐴on𝐴𝐴c𝐴𝐴𝐴𝐴e𝐴𝐴s𝐴𝐴: 𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴 𝑥𝑥𝑥𝑥𝑥𝑥𝑥𝑥=
| XML   |     | 140   |     | 𝑥𝑥𝐴𝐴𝐴𝐴𝐴𝐴 𝑥𝑥𝐴𝐴𝐴𝐴𝐿𝐿𝐴𝐴𝐿𝐿 𝐼𝐼𝐴𝐴𝐼𝐼𝐼𝐼𝐿𝐿𝐿𝐿𝐴𝐴𝐼𝐼𝐴𝐴𝐿𝐿 |     |
| ----- | --- | ----- | --- | ------------------------------------------ | --- |
| Total |     | 1383  |     |                                            |     |
  T.Automatizacion xLOC=6
32   Revista Peruana de Computación y Sistemas 2022; 4(1)

EasyRest: Generador automático de API Rest basado en Spring Framework y motor de plantillas Beetl
5.2.  Sin el generador de API REST
A continuación, en la Tabla 8 se visualiza las clases
java generadas y la cantidad de líneas generadas por cada
| clase. |     |     | Para realizar la implementación de la tienda sin el  |     |
| ------ | --- | --- | ---------------------------------------------------- | --- |
aporte se deberá crear servicios, controladores y reposi-
Tabla 8. Cantidad de líneas de código fuente por clase generada torios por cada entidad además es necesario comprender
las relaciones entre entidades y realizar el mapeo. Este
| #   | Clase | LOC |     |     |
| --- | ----- | --- | --- | --- |
proceso suele ser repetitivo y tedioso cuando se necesita
| 1 App.java                       |     | 12 crear una gran cantidad de API Rest |     |     |
| -------------------------------- | --- | -------------------------------------- | --- | --- |
| 2 CategoryProductController.java |     | 71                                     |     |     |
Tasa de automatización por LOC para cada Loc. La
| 3 CategoryProductEntity.java |     | 23  |     |     |
| ---------------------------- | --- | --- | --- | --- |
tasa de automatización por LOC para cada LOC utili-
| 4 CategoryProductService.java |     | 18  |     |     |
| ----------------------------- | --- | --- | --- | --- |
zando la ecuación 2 fue de 1 ya que la construcción del
| 5 ClientController.java |     | 71  |     |     |
| ----------------------- | --- | --- | --- | --- |
proyecto fue manual y no se utiliza alguna herramienta
6 ClientEntity.java 25 que permita automatizar algunos procesos.
| 7 ClientService.java |     | 18  |                           |     |
| -------------------- | --- | --- | ------------------------- | --- |
| 8 CORS.java          |     | 38  |   T.Automatizacion xLOC=1 |     |
| 9 ErrorResponse.java |     | 31  |                           |     |
Tasa de productividad por LOC. Para calcular el
10 FileStorageException.java 9 tiempo de ciclo fue necesario revisar algunos estudios
11 GenericResponse.java 52 para encontrar tasas de productividad por líneas de có-
digo fuente, estableciendo en promedio 20 LOC por
| 12 GenericServiceImpl.java |     | 30  |     |     |
| -------------------------- | --- | --- | --- | --- |
cada hora.
| 13 GlobalExceptionHandler.java     |     | 85  |     |     |
| ---------------------------------- | --- | --- | --- | --- |
| 14 ICategoryProductController.java |     | 12  |     |     |
  Tasa productividad por LOC =20 LOC x hora
| 15 ICategoryProductRepository.java |     | 5   |     |     |
| ---------------------------------- | --- | --- | --- | --- |
Tiempo de ciclo. Con el generador de API Rest se
| 16 ICategoryProductService.java |     | 5   |     |     |
| ------------------------------- | --- | --- | --- | --- |
obtuvo 1383 líneas de código fuente (LOC), para ge-
| 17 IClientController.java |     | 12  |     |     |
| ------------------------- | --- | --- | --- | --- |
nerar dichas cantidades de líneas requerirá 69.15 horas
| 18 IClientRepository.java |     | 5   |     |     |
| ------------------------- | --- | --- | --- | --- |
aproximadamente, que serían alrededor de 8 días con 3
| 19 IClientService.java     |     | 5 horas laborales.  |     |     |
| -------------------------- | --- | ------------------- | --- | --- |
| 20 IGenericRepository.java |     | 6                   |     |     |
  Tiempo Ciclo=69.15 horas
| 21 IGenericService.java  |     | 9   |     |     |
| ------------------------ | --- | --- | --- | --- |
| 22 IOrderController.java |     | 12  |     |     |
5.3.  Discusión
| 23 IOrderDetailController.java |     | 12  |     |     |
| ------------------------------ | --- | --- | --- | --- |
En la Tabla 9 mostrada a continuación se visualiza
| 24 IOrderDetailRepository.java |     | 5   |     |     |
| ------------------------------ | --- | --- | --- | --- |
los resultados obtenidos al construir el proyecto backend
| 25 IOrderDetailService.java |     | 5   |     |     |
| --------------------------- | --- | --- | --- | --- |
rest con y sin el aporte.
| 26 IOrderRepository.java |     | 5   |     |     |
| ------------------------ | --- | --- | --- | --- |
| 27 IOrderService.java    |     | 5   |     |     |
Tabla 9. Resultados obtenidos según el caso de estudio
| 28 IProductController.java |     | 12  |     |     |
| -------------------------- | --- | --- | --- | --- |
Tiempo de  TR LOC  TA x LOC para
| 29 IProductRepository.java |     | 5   | Caso de Estudio LOC X LOC |     |
| -------------------------- | --- | --- | ------------------------- | --- |
ciclo por 1h cada LOC
| 30 IProductService.java |     | 5   |     |     |
| ----------------------- | --- | --- | --- | --- |
553 200
|                         |     |     | Con el generador 1383 9 segundos | 6   |
| ----------------------- | --- | --- | -------------------------------- | --- |
| 31 MessageResponse.java |     | 57  |                                  | LOC |
32 MyFileNotFoundException.java 12 Sin el generador 1383 69.15 horas 20 LOC 1
| 33 NoSuchElementFoundException.java |     | 10  |     |     |
| ----------------------------------- | --- | --- | --- | --- |
34 ObjectMapperJSON.java 13 Como se puede observar, el aporte solo necesito
de 9 segundos aproximadamente para generar 1383
| 35 OrderController.java |     | 71  |     |     |
| ----------------------- | --- | --- | --- | --- |
líneas de código fuente a comparación de la construc-
| 36 OrderDetailController.java |     | 71  |     |     |
| ----------------------------- | --- | --- | --- | --- |
ción manual donde se necesitó 69.15 horas. Además,
| 37 OrderDetailEntity.java |     | 29  |     |     |
| ------------------------- | --- | --- | --- | --- |
el aporte reflejó una tasa de automatización 6 LOC por
| 38 OrderDetailService.java |     | 18  |     |     |
| -------------------------- | --- | --- | --- | --- |
cada LOC ingresado, si bien el valor no es tan alto, esto
| 39 OrderEntity.java |     | 35  |     |     |
| ------------------- | --- | --- | --- | --- |
se debe principalmente al método de ingreso de infor-
40 OrderService.java 18 mación ya que al usar un formato JSON es necesario
41 ProductController.java 71 escribir algunas líneas adicionales, cabe mencionar que
el principal aporte de este generador no es generar la
| 42 ProductEntity.java |     | 30  |     |     |
| --------------------- | --- | --- | --- | --- |
mayor cantidad de líneas sino generar según las nece-
| 43 ProductService.java |     | 18  |     |     |
| ---------------------- | --- | --- | --- | --- |
sidades del negocio una aplicación  REST basado en la
| 44 SecurityConfiguration.java |     | 42  |     |     |
| ----------------------------- | --- | --- | --- | --- |
arquitectura de capas y utilizando plantillas que sirve
| 45 SecurityProperties.java |     | 28  |     |     |
| -------------------------- | --- | --- | --- | --- |
como iniciación al momento de desarrollar aplicaciones
| 46 SwaggerConfig.java |     | 98  |     |     |
| --------------------- | --- | --- | --- | --- |
con Spring Framework.
Revista Peruana de Computación y Sistemas 2022; 4(1) 33

Chavez & Wong
6. Conclusiones [7] Paolone G., Marinelli M., Paesani R. & Di Felice P., «Automa-
tic Code Generation of MVC Web Applications,» Computers,
En el presente trabajo se desarrolló un generador
2020.
de API REST basado en plantillas que brinda distintos
[8] Arsaute A., Zorzan F., Daniele M., González A. & Frutos M.,
métodos para ser consumidos con el fin de automatizar
«Generación automática de API REST a partir de API Java,
el proceso de construcción de proyectos backend con
basada en,» XX Workshop de Investigadores en Ciencias de
tecnologías Java y Spring Framework. El proyecto gene-
la Computaci´on, 2018.
rado con el aporte está constituido en distintos paquetes
[9] L. J. (. D. Fu), «Beetl 3,» 2021. [En línea]. Available: http://
(servicios, controladores, repositorio, entidades) además
ibeetl.com/guide/#/beetl.
de la implementación de la seguridad y la documenta-
ción automática mediante Swagger. El aporte nos per- [10] S. Software, «Swagger IO,» 2021. [En línea]. Available: ht-
mite enfocarnos en la lógica de negocio dejando de lado tps://swagger.io/.
tareas repetitivas y archivos de configuración. [11] Wong L., Mauricio D. & Rodriguez G. «Una revisión sistemá-
tica de la literatura sobre la obtención de requisitos de sof-
El ingreso de la información en formato JSON fa- tware,» Revista de ciencia y tecnología de la ingeniería, vol.
cilitó la transformación a objetos java permitiendo un 12, nº 2, 2017.
fácil tratamiento de los datos.
[12] Wei B., Li G., Xia X., Fu Z. & Jin Z, «Code Generation as
a Dual Task of Code Summarization,» 33rd Conference on
Maven como herramienta para la gestión y cons-
Neural Information Processing Systems, 2019.
trucción del aporte fue fundamental, ya que permitió
la construcción de arquetipos customizados que fueron [13] Arcuri A, «RESTful API Automated Test Case Generation,»
utilizados en el estudio. Además de brindar un fácil ma- IEEE, Vols. %1 de %2International Conference on Software
Quality, Reliability and Security, 2017.
nejo de dependencias y facilitó la compilación y empa-
quetado del proyecto generado. [14] Atlidakis V., Godefroid P. & Polishchuk M. «RESTler: Stateful
REST API Fuzzing,» IEEE/ACEM 41st International Confe-
Beetl como motor de plantillas permitió la comu- rence on Software Engineering (ICSE), 2019.
nicación mediante código Java, además la velocidad de
[15] P. Rantanen, «REST API Example Generation Using Java-
captura de información a la plantilla fue rápida.
doc,» Computer Science and Information Systems, 2019.
[16] Tijana L., Zeljko. & Gordana M, «A Meta-Model and Code
7. Trabajos futuros
Generator for Evolving Software Product Lines,» 2021.
Como futuros trabajos se propone realizar la ge-
[17] Arcuri A., «Automated Blackbox and Whitebox Testing of
neración automática de las pruebas unitarias, que es una
RESTful APIs with EvoMaster,» IEEE Explore, 2020.
actividad fundamental en el desarrollo de software y la
inclusión de archivos Dockerfile para un fácil despliegue. [18] Ed-douibi H., Cánovas J. & Cabot J., «Automatic Generation
of Test Cases for REST, » IEEE 22nd International Enterprise
Además de agrupar este tipo de proyecto en dos catego-
Distributed Object Computing Conference, 2018.
rías: monolitos y microservicios
[19] Sunitha E. & Philip S, «Automatic Code Generation From
8. Referencias UML State Chart Diagrams, » IEEE Xplore, vol. 7, 2019.
[20] Nakamaru T. & Chiba S, «Generating a Generic Fluent API in
[1] Gupta A., Suri B. & Misra S. A Systematic Literature Re-
Java,» The Art, Science, and Engineering of Programming,
view: Code Bad Smells in Java Source Code. 665-682.
vol. 4, nº 3, p. 23 pages, 2020.
10.1007/978-3-319-62404-4_49, «A Systematic Literature
Review: Code Bad Smells in Java Source Code,» Springer, [21] Fajardo A., «Método para complementar la generación de
2017. códigos de aplicaciones web desde el diagrama de clases
UML,» Ciencia y Tecnologia, 2019.
[2] C. McGregor, «Craftsmanship for Software,» 25 Mayo
2015. [En línea]. Available: https://craftsmanshipforsoftware. [22] Radermacher A., Gérard S., Cam Pham V. & Li S. «Complete
com/2015/05/25/the-cost-of-duplicated-code/. Code Generation from UML State Machine,» Science and Te-
chnology Publications, Vols. %1 de %2In Proceedings of the
[3] Amjed T., Jens D., Steve C., Sherlock L & Aiko Y, «A large
5th International Conference on Model-Driven Engineering
scale study on how developers discuss code smells and an-
and Software Development, p. 208'2019, 2017.
ti-pattern in Stack Exchange,» Information and Software Te-
chnology, 2020. [23] Venkatraj S., Rajiv V., Vasughi V., Vengatesan K. & Rajesh M.
«Development of Test Automation Framework for REST API
[4] Huari Casas M., «Revisión sistemática sobre generadores de Testing, » Computational and Theoretical Nanoscience, vol.
código fuente y patrones de arquitectura,» Pontificia Univer- 16, pp. 453-457, 2019.
sidad Católica del Perú, 2020.
[24] Hanyang C., Jean-Rémy F. & Xavier B. «Automated Genera-
[5] Spring io, «Spring Framework,» 2021. [En línea]. Available: tion of REST API Specification from Plain HTML Documenta-
https://spring.io/why-spring. tion, » Springer International Publishing, p. 453=461, 2017.
[6] Gómez O., Rosero R. & Cortés K, «CRUDyLeaf: A DSL for [25] Sohan S., Craig A. & Frank M., «Automated Example Orien-
Generating Spring Boot REST APIs from Entity CRUD Ope- ted REST API Documentation at Cisco, » IEEE/ACM 39th
rations,» CYBERNETICS AND INFORMATION TECHNOLO- International Conference on Software Engineering: Software
GIES, vol. 20, nº 3, 2020. Engineering in Practice Track, 2017.
34 Revista Peruana de Computación y Sistemas 2022; 4(1)

EasyRest: Generador automático de API Rest basado en Spring Framework y motor de plantillas Beetl
[26] Fajardo Adolfo, «Método para complementar la generación [32] JSON Org, «Introducción a JSON,» [En línea]. Available: ht-
de códigos de aplicaciones web desde el diagrama de clases tps://www.json.org/json-es.html.
UML,» Ciencia y Tecnología, nº 19, pp. 35 - 63, 2019.
[33] The Apache Software Foundation, «Introduction to Arche-
[27] Eclipse Fundation, «LANGUAGE ENGINEERING FOR types,» 2021. [En línea]. Available: https://maven.apache.
EVERYONE!,» 2021. [En línea]. Available: https://www.eclip- org/guides/introduction/introduction-to-archetypes.html.
se.org/Xtext/.
[34] Rodriguez P., «Convenciones sobre nombres de clases, mé-
[28] The Linux Foundation, «OPENAPI,» 2021. [En línea]. Availa- todos, interfaces, variables y constantes en java.,» 18 Julio
ble: https://www.openapis.org/about. 2020. [En línea]. Available: https://sacavix.com/2020/07/18/
convenciones-sobre-nombres-de-clases-metodos-interfa-
[29] The Apache Software Foundation, «Welcome to Apache Ma-
ces-variables-y-constantes-en-java/.
ven,» 2021. [En línea]. Available: https://maven.apache.org/.
[35] Martin C., «Principios SOLID,» 03 Abril 2019. [En línea].
[30] R. S. Reinier Zwitserloot, «Project Lombok,» 2021. [En línea].
Available: https://enmilocalfunciona.io/principios-solid/.
Available: https://projectlombok.org/.
[31] T. D. C. S. M. P. J. B. Oliver Gierke, «Spring Data JPA - Re-
ference Documentation,» [En línea]. Available: https://docs.
spring.io/spring-data/jpa/docs/current/reference/html/#refe-
rence.
Revista Peruana de Computación y Sistemas 2022; 4(1) 35
