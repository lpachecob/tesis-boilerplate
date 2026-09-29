|            | Universidad   |         |        |             | Católica     |                | de         | Santa   | María      |        |
| ---------- | ------------- | ------- | ------ | ----------- | ------------ | -------------- | ---------- | ------- | ---------- | ------ |
|            | Facultad      |         |        | de Ciencias |              | e Ingenierías  |            | Físicas | y Formales |        |
|            |               | Escuela |        | Profesional |              | de             | Ingeniería | de      | Sistemas   |        |
| DESARROLLO |               |         |        | DE          | UN FRAMEWORK |                |            | CON     | UNA        | ARQUI- |
| TECTURA    |               |         | BASADA |             | EN           | MICROSERVICIOS |            |         | PARA       | EL UP- |
| GRADE      |               | DEL     |        | SISTEMA     | DE           | PLANIFICACIÓN  |            |         | DE         | RECUR- |
| SOS        | EMPRESARIALES |         |        |             | DE           | LA             | UCSM       |         |            |        |
Tesispresentadaporelbachiller:
BobadillaCharaSebastianGonzalo
ParaoptarelTítuloProfesionalde:
IngenierodeSistemas
Asesora:
Dra.CastroGutierrezEvelingGloria
Arequipa-Perú
2022

UCSM-ERP
UNIVERSIDAD CATÓLICA DE SANTA MARÍA
INGENIERIA DE SISTEMAS
TITULACIÓN CON TESIS
DICTAMEN APROBACIÓN DE BORRADOR
Arequipa, 08 de Junio del 2022
Dictamen: 006317-C-EPIS-2022
Visto el borrador del expediente 006317, presentado por:
2017204541 - BOBADILLA CHARA SEBASTIAN GONZALO
Titulado:
DESARROLLO DE UN FRAMEWORK CON UNA ARQUITECTURA BASADA EN MICROSERVICIOS
PARA EL UPGRADE DEL SISTEMA DE PLANIFICACIÓN DE RECURSOS EMPRESARIALES DE LA
UCSM
Nuestro dictamen es:
APROBADO
1221 - PAREDES MARCHENA FERNANDO GERMAN
DICTAMINADOR
1425 - MARTINEZ MUÑOZ JORGE LUIS
DICTAMINADOR
1564 - CORRALES DELGADO CARLO JOSE LUIS
DICTAMINADOR

Agradecimientos
Deboagradecerenprimerlugaramispadres,CaterineyJuanManuel.Quienesademásdedarmela
vida,meformaroncomopersonaymeenseñaronacaminarpormimismo.
Agradezcotambiénalosdocentesdequienesaprendíalolargodemicarreraprofesional,que
ademásdeimpartirconocimientosmedemostraronloqueesserunbuenprofesional.
Finalmenteagradeceramisamigos,enespecialaDiegoyMarcelo,quienesmeacompañarondesde
elprimerañodeuniversidad,yquemeapoyaronentodomomento.
iii

Dedicatoria
Dedicoestetrabajoenprimerlugaramispadres,sinquienesnohabríapodidocompletarlo.Dedico
tambiénestelogroamisamigos,queenningúnmomentodudarondemíysiempremebrindan
ánimoparaseguiradelante.
iv

Resumen
Latecnologíaseencuentraenconstanteevolución,yconstantementepodemosverquesurgennue-
vasmanerasdehacersoftwarequebuscanestarmejorpreparadasparaelentornodealtocrecimiento
queestamosviviendo.Sinembargo,muchasorganizacioneshandecididomantenersistemascontec-
nologíasantiguasypresentanunaaltaresistenciaalcambio.Estoenconsecuenciageneraunamayor
cantidadderiesgos,ademásdegenerarunmayorcostodemantenimiento.Esporestosmotivosque
enelpresentetrabajosebuscaproponerunframeworkpararealizarlarefactorizaciónymejoradel
backenddeunsistema,tomandocomocasodeestudioelERPdelaUniversidadCatólicadeSanta
María.
Framework, refactorización de software, escalabilidad de software, mantenibilidad
Palabras clave:
desoftware,microservicios
v

Abstract
Technology is constantly evolving, and so new ways to make software emerge in order to be bet-
terpreparedforthehigh-growthenvironmentwearelivingin.However,manyorganizationshave
decidedtomaintainsystemswitholdtechnologiesandarehighlyresistanttochange.This,inconse-
quence,generatesagreaternumberofrisks,inadditiontogeneratingahighermaintenancecost.It
isforthesereasonsthatinthisworkIproposeaframeworktoperformtherefactoringandimprove-
mentofthebackendofasystem,takingasacasestudytheERPoftheCatholicUniversityofSanta
María.
Framework,softwarerefactoring,softwareescalability,softwaremaintainability,micro-
Keywords:
services
vi

Introducción
Al igual que la tecnología, el software evoluciona constantemente y da lugar a nuevas maneras de
construirlo, ya sea a través de nuevos lenguajes de programación o nuevas metodologías, e incluso
arquitecturas.Sinembargo,enmuchoscasoslasorganizacionesnoactualizansusoftwareyloman-
tienencomoseconstruyóinicialmentebasadosenquenorequieredeunamejorayaquecumplecon
losobjetivosdelnegocio.Aestosepuedesumarelhechodequelasorganizacionesnoquierenreali-
zarunainversiónenrealizarlamodernizacióndesussistemas,oqueconsideranqueloúnicoquees
necesarioparaquesiganoperandoesaplicarlesmantenimientodemanerafrecuente.Esteproblema
semanifiestadediferentesmanerasyadiferentesniveles,quepuedeabarcardesdeseguirutilizando
procedimientosenCobolparacálculosfinancierosausarmotoresdeplantillasparaeldesarrollode
unsistema.
TaleselcasodelsistemaERPdelaUniversidadCatólicadeSantaMaría,queactualmenteutilizapa-
rasusistemaPHPyelmotordeplantillasSmarty.PHP,sinembargo,esunatecnologíawebqueya
tienemásde25años,ydesdesuorigenhansurgidodiferentesframeworks,tantoenPHPcomoen
tecnologíasmásmodernasqueofrecenunamayorgamadefuncionalidadesyunamejorexperiencia
paralosdesarrolladores.Actualmente,debidoalusodePHPySmartyparaelDesarrollodelsistema
ERP,esteyasehaconvertidoeninmantenible,debidoalamagnituddelsoftware.Estosumadoalas
limitacionesdelaarquitecturaactualhanhechoqueelcódigoFuentedelaaplicaciónrequieramás
tiempoenmantenimientoqueeneldesarrollodenuevasfuncionalidadesoinclusooptimizaciónde
losprocesosyaimplementados.Yconelpasodeltiempo,elmantenimientoesmáscomplicado,yel
desempeñodelsistemacontinúadegradándose.
vii

Porloanteriormentemencionado,seproponelaelaboracióndeunframeworkparallevaracabola
modernización del sistema ERP de la Universidad Católica de Santa María, considerando puntos
centralescomolaescalabilidaddelsoftware,lafacilidaddemantenimiento,yeldesempeñodelsiste-
ma.Estapropuestaserealizaráconelobjetivodedescubrirlamejormaneradediseñarlaarquitectura
delbackend,demaneraquepuedaponerseapruebayasígenerarunaplantillaquepuedaserusada
paraelDesarrollodelsistema.EsasíqueelinterésdelProyectoesmeramenteacadémico.
Paralarealizacióndelproyectoprimerosellevaráacabounarevisiónbibliográficadelasarquitectu-
rasmásusadasactualmenteydeesamaneraelegirlaquecuenteconmáscasosdeéxitoyasítomarla
dereferencia.LuegoseseleccionaráunodelosmódulosdelactualsistemaERPdelaUCSMpara
refactorizarloyaplicarenlaarquitecturaytecnologíaselegidastraslarevisiónbibliográfica.Parala
evaluacióndelaarquitecturapropuestaserealizaráunavalidaciónenprimerlugaratravésdemétri-
casdedesempeñodelsistema.Porlascaracterísticasmencionadasanteriormente,estaesunainvesti-
gaciónaplicadatecnológica.
El objetivo del trabajo es desarrollar un framework con una arquitectura basada en microservicios
paralamejoradelsistemaERPdelaUCSM,paralocualsepropone3objetivosespecíficos:(i)De-
terminarlamejormaneradeconstruirlaAPIenbasealastendenciasactualesdelmercado,asícomo
tambiéndefinirconquétecnologíarealizarlo.(ii)RefactorizarunmódulodelERPutilizandolaar-
quitecturaytecnologíapropuesta.(iii)Realizarlavalidacióndelmoduloparaevaluarsuusabilidad
ydesempeño.
En el presente documento y en los capítulos correspondientes se expone el proyecto a desarrollar.
Enelprimercapítulosepresentaelplandelainvestigación,conelobjetivogeneral,específicos,las
preguntasdeinvestigación,ylahipótesisyvariables.Enelcapítulo2sepresentalosfundamentos
teóricos,enelcapítulo3elmarcometodológico,enelcapítulo4eldesarrollodelapropuesta,enel
capítulo5elanálisisyvalidaciónderesultados,enelcapítulo6ladiscusión,yfinalmentelasconclu-
siones.
viii

Índice
Resumen v
Abstract vi
Introducción vii
1 Plandelainvestigación 1
1.1 Planteamientodelproblema . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Objetivosdelainvestigación . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2.1 Objetivogeneral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2.2 Objetivosespecíficos . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 Preguntasdeinvestigación,hipótesis,yvariables . . . . . . . . . . . . . . . . . . 2
1.3.1 Preguntasdeinvestigación . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3.2 Hipótesisyvariables . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 LíneaySublíneadeInvestigación . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.5 Palabrasclave . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.6 SoluciónPropuesta . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.6.1 JustificacióneImportancia . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.6.2 DescripcióndelaSolución . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.6.3 Aporte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.6.4 MatrizdeConsistencia . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
ix

2 Fundamentosteóricos 7
2.1 EstadodelArte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2 BasesTeóricasdelaInvestigación . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.2.1 EnterpriseResourcePlanning . . . . . . . . . . . . . . . . . . . . . . . 16
2.2.2 Frontend . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.2.3 Backend . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.2.4 API . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.2.5 REST . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.2.6 Bundler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.2.7 Mantenimiento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.2.8 JSON . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.2.9 JWT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.2.10 ReactJS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.2.11 Go . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3 MarcoMetodológico 21
3.1 AlcancesyLimitaciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.1.1 Alcance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.1.2 Limitaciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.2 TipoyNiveldeInvestigación . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.2.1 TipodeInvestigación . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.2.2 NiveldeInvestigación . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.3 PoblaciónyMuestra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.3.1 Población . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.3.2 Muestra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.3.3 Métodos,TécnicaseInstrumentosdeRecoleccióndeDatos . . . . . . . . 24
3.3.4 TécnicasdeRecoleccióndeDatos . . . . . . . . . . . . . . . . . . . . . 24
x

3.3.5 InstrumentosdeRecoleccióndeDatos . . . . . . . . . . . . . . . . . . . 24
3.3.6 TécnicasdeProcesamientodeDatos . . . . . . . . . . . . . . . . . . . . 25
3.3.7 HerramientasparaelProcesamientodeDatos . . . . . . . . . . . . . . . 26
3.4 Estudioeconómico . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.5 Plandelproyecto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4 Desarrollodelapropuesta 30
4.1 AnálisisdelCódigoActual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.2 ElaboracióndelaNuevaArquitectura . . . . . . . . . . . . . . . . . . . . . . . 34
4.3 TransformacióndelCódigoyGeneracióndelaPlantilla . . . . . . . . . . . . . . 34
4.4 Testing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
4.4.1 PruebasUnitarias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
4.4.2 PruebasIntegrales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
4.4.3 PruebasFuncionales . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
4.5 EstrategiadeDespliegue . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5 AnálisisyValidacióndeResultados 44
5.1 ValidaciónCualitativa . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
5.2 Validacióncuantitativa . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
5.2.1 PruebasenEntornodeDesarrollo . . . . . . . . . . . . . . . . . . . . . 46
5.2.2 PruebasenEntornodeProducción . . . . . . . . . . . . . . . . . . . . . 51
6 Discusión 58
Conclusiones 59
Recomendaciones 61
Estándares 62
xi

Glosario 63
Referencias 64
Anexos 68
A Cuestionariopropuesto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
B Costosdemantenimiento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
C Cálculodelarevalorizacióndelsistema . . . . . . . . . . . . . . . . . . . . . . . 69
D Cartadevalidacióndeljefedelárea . . . . . . . . . . . . . . . . . . . . . . . . . 70
E Capturasdelaspruebasrealizadas . . . . . . . . . . . . . . . . . . . . . . . . . . 71
E.1 CapturadelresultadodelapruebadecargarealizadaconlaCLIdeK6al
localhostconelsistemadesarrolladoenPHP. . . . . . . . . . . . . . . . . 71
E.2 CapturadelresultadodelapruebadecargarealizadaconlaCLIdeK6al
localhostconelmicroserviciodesarrolladoenGo. . . . . . . . . . . . . . 72
E.3 CapturadeejemplodelapruebadecargaaPHP. . . . . . . . . . . . . . . 72
E.4 CapturadeejemplodelapruebadecargaaGo. . . . . . . . . . . . . . . . 73
E.5 CapturadeejemplodeunapruebadeestrésrealizadaalservidorenPHP. . 74
E.6 CapturadeejemplodeunapruebadeestrésrealizadaalservidorenGo. . . 75
xii

Índice de figuras
1.1 Matrizdeconsistencia . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3.1 PlanificacióndelproyectopresentadaenundiagramadeGantt . . . . . . . . . . . 29
4.1 Esquemadelametodologíadedesarrollo,adaptadode(Wolfartycol.,2021) . . . . 30
4.2 Capturadellistadodearchivosydirectoriosenlaraízdelrepositorio . . . . . . . . 32
4.3 DiagramadeinterfazdeserviciosdelmóduloparalaBoticaAliviari . . . . . . . . . 34
4.4 DiagramadelaarquitecturaquetendríanlosserviciosdelERP . . . . . . . . . . . 35
4.5 Capturadelaestructuradearchivosdelserviciodeautenticación . . . . . . . . . . 36
4.6 Capturadelaestructuradearchivosdelainterfazdeautenticación . . . . . . . . . 37
4.7 Capturadelárboldearchivosdelmicroserviciodeiniciarsesión . . . . . . . . . . 39
4.8 Ejecucióndepruebasunitariasycobertura . . . . . . . . . . . . . . . . . . . . . 41
4.9 ResultadosdelaejecucióndelaspruebasdefinidasconJest . . . . . . . . . . . . . 42
5.1 Promediodeladuracióndelasolicituddelsistemaactualyelframeworkpropuesto
segúnelnúmerodeusuarios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
5.2 Promediodeladuracióndelasolicitudenunapruebadeestréscon200usuariosal
sistemaactualyalframeworkpropuesto . . . . . . . . . . . . . . . . . . . . . . 51
5.3 Diagramadecajasybigotesdeladuracióndesolicitudpromedio(ms)depruebas
deestrésalsistemaactualyalframeworkpropuesto . . . . . . . . . . . . . . . . . 53
5.4 Diagramadecajasybigotesdeladuracióndesolicitud(ms)depruebadeusuarios
alsistemaactualyalframeworkpropuesto . . . . . . . . . . . . . . . . . . . . . 56
xiii

Índice de tablas
1.1 Indicadoreseíndicesparalavariable“Productividaddelosdesarrolladores” . . . . 3
1.2 Indicadores e índices para la variable “Framework utilizado para el desarrollo del
sistema” . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
3.1 Detalledelamétricadeadecuidad . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.2 Detalledelamétricadeeficiencia . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.3 Detalledelamétricademantenibilidad . . . . . . . . . . . . . . . . . . . . . . . 27
3.4 Detalledeloscostosmensualesparaeldesarrollodelproyecto . . . . . . . . . . . . 28
3.5 Análisisdelcosto/beneficioderealizarelproyecto . . . . . . . . . . . . . . . . . . 28
4.1 Casosdepruebadefinidosparalaspruebasunitarias . . . . . . . . . . . . . . . . 40
4.2 Casosdepruebadefinidosparalaspruebasintegrales . . . . . . . . . . . . . . . . 41
4.3 Casosdepruebadefinidosparalaspruebasfuncionales . . . . . . . . . . . . . . . 42
5.1 Resultadosdelaspreguntascerradasdelaencuestaaplicada,donde5es“totalmente
deacuerdo”y0es“totalmenteendesacuerdo" . . . . . . . . . . . . . . . . . . . 45
5.2 Comparacióndelapruebadecargarealizada . . . . . . . . . . . . . . . . . . . . 47
5.3 Análisisestadísticodelapruebadecargadurante10segundosalsistemaactualyal
sistemadesarrolladoconelframeworkpropuestosegúnelnúmerodeusuarios . . . 47
5.4 Análisis estadístico de la prueba de estrés con 200 usuarios al sistema actual y al
frameworkpropuesto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
5.5 Distribucióndefrecuenciasdeladuracióndesolicitudpromedio(ms)depruebas
deestrésalsistemaactual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
xiv

5.6 Distribucióndefrecuenciasdeladuracióndesolicitudpromedio(ms)depruebas
deestrésalframeworkpropuesto . . . . . . . . . . . . . . . . . . . . . . . . . . 54
5.7 Distribucióndefrecuenciasdeladuracióndesolicitud(ms)depruebaconusuarios
alsistemaactual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
5.8 Distribucióndefrecuenciasdeladuracióndesolicitud(ms)depruebaconusuarios
alframeworkpropuesto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
5.9 Análisisestadísticodelaspruebasdeestrésydeusuariosrealizadasalsistemaactual
yalframeworkpropuesto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
xv

1
Plan de la investigación
1.1. Planteamiento del problema
A lo largo de los años las tecnologías y frameworks para el desarrollo de aplicaciones web han
evolucionado.Sinembargo,muchasinstitucioneshancontinuadoutilizandotecnologíasantiguasa
pesardelasevidentetendenciahacianosólonuevasherramientas,sinotambiénanuevasmaneras
derealizarlaarquitecturadesusserviciosenelbackend.
El lugar elegido para realizar el estudio es la oficina del ERP de la Universidad Católica de Santa
María.Dondesepresentanproblemasrelacionadosalsoftwarequesibiennopresentafallasaún,el
repositoriodelcódigofuentedelsistemayaesinmantenibledebidoalamaneraenlaqueestáestruc-
turado,ademásdeestardesactualizado.
Lascausasqueoriginanesteproblemasonvariadas,ycomoindican(Hussainycol.,2017)laprin-
cipal causa es que las organizaciones consideran que dichos sistemas funcionan adecuadamente y
cumplenconlosobjetivosdelnegocio,ademásdequeconsideranquelainversiónenactualizarlosy
mejorarlosnoesnecesaria,yquenoofreceríaunretornosignificativo.
Las consecuencias de esto es que los sistemas desactualizados continúan creciendo con los proble-
mas y fallas propios de su implementación, y por lo tanto hacen que el trabajo con ellos sea más
complicado.Sucódigoesmáscomplicadodeentender,sumantenimientosevuelvemáscostoso,y
sudesempeñosevadegradando.Estoporejemplooriginaqueenlugardeoptimizarlasoperaciones
actuales,oimplementarnuevasfuncionalidades,losdesarrolladorespasenlamayorpartedesutiem-
poresolviendoproblemasydandomantenimientoalsistema.
Porello,lapresenteinvestigaciónpretendeelaborarunframeworkpararealizarlarefactorizacióny
1

upgradedelbackenddelsistemaERPdelaUniversidadCatólicadeSantaMaría,demaneraquese
usentecnologíasmodernasyunaarquitecturaqueconsiderelaescalabilidaddelsistema.
1.2. Objetivos de la investigación
1.2.1. Objetivogeneral
Desarrollarunframeworkutilizandotecnologíasyarquitecturasmodernaspararealizarelupgrade
delsistemaERPdelaUniversidadCatólicadeSantaMaríaenel2021.
1.2.2. Objetivosespecíficos
Analizarlas tendenciasactuales enelmercado yel estadodelarte parala construccióndela
arquitecturadelaAPIdelsistema.
Definirlaarquitecturaautilizarparaeldesarrollodelsistema.
Refactorizarunmóduloconelframeworkpropuesto.
Validareldesempeñodelmódulodesarrollado,asícomotambiénlausabilidaddelframework
propuesto.
1.3. Preguntas de investigación, hipótesis, y variables
1.3.1. Preguntasdeinvestigación
¿CuáleslamejormaneraderealizarelupgradedelsistemaERPdelaUniversidadCatólicade
SantaMaríamedianteunframeworkqueutilicetecnologíasyarquitecturasmodernas?
¿Quéimpactotraeutilizartecnologíasyarquitecturasdebackendmodernas?
¿Cuálessonlascaracterísticasquedebecumplirunframeworkorientadoalaescalabilidadde
unsoftware?
2

1.3.2. Hipótesisyvariables
a) Hipótesis
En este caso se planteó la siguiente hipótesis: “Utilizar un framework con una arquitectura
basadaenmicroserviciosycontecnologíasmodernasmejoralaproductividaddelosdesarro-
lladores”.
b) Variabledependiente
En base a la hipótesis podemos definir como variable dependiente “la productividad de los
desarrolladores”,paralacualsusindicadoressemuestranenlaTabla1.1.
c) Variableindependiente
Enbasealahipótesispodemosdefinircomovariableindependiente“elframeworkutilizado
paraeldesarrollodelsistema”,paralacualsusindicadoressemuestranenlaTabla1.2.
Tabla1.1
Indicadoreseíndicesparalavariable“Productividaddelosdesarrolladores”
Indicadores Índices
Esfuerzorequeridopararealizarelmantenimientoaunmódulo Tiempopromediode13horas
Velocidaddeimplementacióndeunanuevafuncionalidad Tiempopromediode8horas
Tabla1.2
Indicadoreseíndicesparalavariable“Frameworkutilizadoparaeldesarrollodelsistema”
Indicadores Índices
Tiempopromedioenencontrarunarchivo<
Complejidaddelárboldearchivosdel
10s
códigofuente
Númerodelíneasdelarchivodecódigo
Númerodefuncionescontenidasenun
Complejidaddelarchivodecódigofuente
archivodecódigo
3

1.4. Línea y Sublínea de Investigación
Lalíneaalaqueperteneceelpresenteproyectoes“IngenieríadelSoftware”,ylasublíneaes“Ar-
quitecturadelSoftware”.
1.5. Palabras clave
Framework,refactorizacióndesoftware,escalabilidad,mantenibilidad,microservicios.
1.6. Solución Propuesta
1.6.1. JustificacióneImportancia
Actualmente,paraelERPdelaUniversidadCatólicadeSantaMaríaseutilizaPHPparaeldesa-
rrollodelsistema,unatecnologíadehacemásde25años.Estohahechoqueelsistemamantenga
ciertasdeficienciasenloquerespectaalaarquitecturadelsoftware,yhoyendía,dadoelcrecimiento
delsistemaERP,esinmantenible.
Debido a las deficiencias técnicas, este presenta una alta entropía. En consecuencia, el tiempo de
mantenimientoesmáselevado,yexisteunamayorposibilidaddequesepresentenerroresensufun-
cionamiento.AsícomosucedeestoenlaUCSM,sedaelcasoendiversasorganizacionesalolargo
denosóloelPerú,sinotambiénelmundo.Estasorganizacionesnorealizanlamejoradesussistemas
pordiversosmotivos,sinembargo,elmantenersistemascontecnologíasdesactualizadassólogenera
queloscostosdemantenimientoseelevenconstantemente,yqueeldesempeñodelsistemasevea
degradadoconformelasnecesidadesdelosusuariosaumentan.
1.6.2. DescripcióndelaSolución
Lasoluciónqueseproponeeslaelaboracióndeunframeworkquepermitarealizarlarefactoriza-
cióndelbackenddelsistemaERP,demaneraqueseusetecnologíasyarquitecturasdeAPImodernas.
Esteframeworkademás,debeconsiderarotrosaspectosparaeldesarrollodelsistemaengeneral,de
4

maneraquesetengatambiénunenfoqueenlaescalabilidaddelsistema.
Paraestasoluciónserealizaráunarevisiónyevaluacióndelastecnologíasyarquitecturasqueactual-
mentetienenunamayorpresenciaenelmercado,demaneraqueselaspuedacompararyasíobtener
unframeworkquerecopilelosmejoresaspectosencontrados.
1.6.3. Aporte
EnunaprimerainstanciaelaportequeseobtieneeselframeworkquelepermitiríaalaUnidad
deImplementacióndelERPdelaUniversidadCatólicadeSantaMaríallevaracaboelupgradedel
sistema,demaneraqueestepaseaestarconstruidocontecnologíasyarquitecturasmodernasymejor
preparadasparalasnecesidadesactualesdelosusuarios;además,frutodeltrabajosetendrátambién
identificadoslosbeneficiosderealizarestetipoderefactorizaciónenunsistemadegestiónempresa-
rial.
Sinembargo,sepretendellegaraelaborarunframeworkquepuedaseraplicadoencualquierinstitu-
ción,sinimportarsurubrootamaño.Estoasuvezayudaráaquelosgerentespresentenunamenor
resistenciaalcambio,alpoderfundamentaradecuadamentelanecesidad,beneficios,ypasosaseguir
delaactualizacióndesussistemas.
1.6.4. MatrizdeConsistencia
Amaneraderesumirlodesarrolladoenelpresentecapítuloseelaboróunamatrizdeconsisten-
cia,demaneraquesepuedatenertodosloselementosclaveparalainvestigaciónenunasolatabla
que pueda ser consultada con mayor facilidad. La matriz de consistencia se puede ver en la Figura
1.1,ycontieneelproblemadeinvestigación,losobjetivos,lahipótesis,lasvariableseindicadores,la
metodología,ylatécnicaseinstrumentosparalarecoleccióndedatos.
5

aicnetsisnocedzirtaM
.1.1arugiF
6

2
Fundamentos teóricos
2.1. Estado del Arte
Larefactorizacióndecódigosiemprehasidounatareaimportante.Esasíque(Jindal&Khurana,
2013),conelobjetivodehacerqueestatareaseamásfácilparalosdesarrolladores,propusieronuna
herramientaqueayudaaidentificaraquellospuntosquepuedenserrefactorizados,aligualquela
magnituddeloscambiosquepodríanrealizarse.Enestapropuestasemencionaqueunamanerade
mejorareltiempodeprocesamientodelalgoritmoesatravésdelaseleccióndeatributossignificati-
vosparaelanálisis.
Setieneporotroladolapropuestade(Pérez-Castilloycol.,2013),quienespropusieronunproceso
de reingeniería para recuperar y adaptar los web services asociados con las bases de datos antiguas
oactualmenteenuso.Deestamanera,dichasbasesdedatospodíancontinuarenfuncionamiento
acelerandoelprocesoderefactorizaciónyobteniendomejoresresultados.
Ambaspropuestasmencionadasanteriormentebuscanhacerquelarefactorizaciónseaunproceso
másefectivoymenosdisruptivo.Tanto(Pérez-Castilloycol.,2013)como(Jindal&Khurana,2013)
mencionanquelamaneradehacerqueunprocesoderefactorizaciónseamásefectivoesatravésde
identificarloselementoscríticosparaelsistema.Esdecir,aquelloselementoscomoserviciosimpor-
tantesofuncionalidadesinvocadasconstantemente,demaneraquesetengauntrabajomásefectivo
sobredichospuntosyrealizarlarefactorizaciónadecuadamente.
Llevaracabolarefactorizacióndeunsoftwareconmotivodemodernizarloesunatareaqueseeje-
cutaconelobjetivodemantenerelsistemaoperandoadecuadamente,yesunatareaquepuedetener
diferentescausaspararealizarse.Sobreestetemaseencontródospropuestasquecoincidenenque
7

realizarunarefactorizaciónesunatareacomplicada.Primero,comoloindicaensuestudio(Gerasi-
mouycol.,2018),puedeserqueconelobjetivodemejorarlamantenibilidaddeunsistemaseusen
libreríasdeterceros,yqueesaslibreríashayanquedadoobsoletasohayancambiadodetalmanera
queesnecesarioactualizarelsistemadesarrolladoconellas.Sinembargo,tambiénidentificaronque
muchasvecesunmotivoparanollevaracabolamejoraesevitarlosriesgosasociadosaesta,como
puedensererroresdelosprogramadores,incompatibilidadesconotroselementosdelsistema,entre
otros.Estollevaaquelasorganizacionespormantenerelsoftwareensuestadoactualquedenexpues-
tasaotrosriesgosdemayorgravedad,comoerroresquequedaronsinresolver,oinclusovulnerabi-
lidadfrenteataquescibernéticos.Esporelloqueproponenunametodologíaparalamodernización
delsoftware,enlacualprincipalmentesebasanenmétricas(comolacantidaddeinvocacionesque
sehaceaunaAPI)paradeterminarelniveldedependenciaquesetienefrenteaunalibrería.Luego,
seprocesaelcódigofuenteparaobtenerpatronesyasígenerarposiblesplantillasparaqueestasluego
seancompletadasporlosdesarrolladoresyasítenerunatransiciónconmenoscomplicacionesala
nuevalibrería.
Luego,demanerasimilaraltrabajoanteriorseelaboróunmétodoparaevaluarunsistemamonolítico
demaneraqueseobtengalascaracterísticasestáticasydinámicasdelsistema.Estetrabajofuereali-
zadopor(Renycol.,2018),quienesproponenqueenbaseadichoanálisisseobtengaunaprimera
listadefuncionalidadescandidatasarefactorización,debidoaquepresentanunalevedependencia
deotrasfuncionespresentesenelmonolitoodelibreríasdeterceros.Sinembargo,atravésdeeste
métodosepuedegeneraruntrabajoiterativoquepermitarefactorizarlatotalidaddelmonolitode
maneragradual.Losautorescomentanquesealcanzóunniveldedesempeñoóptimoparaelmétodo
propuesto,yqueestepuedeserautomatizadofácilmentedemaneraqueseagilicesuejecución.
Alosdostrabajosmencionadosanteriormentesepuedeagregarlaperspectivaqueofrecen(Al-Debagy
& Martinek, 2020). En su propuesta desarrollaron una metodología no sólo para identificar fun-
cionescandidatasasermigradasamicroservicios,sinoquetambiéndefinieronunapropuestapara
determinarsiunmicroservicionecesitamayorgranularidad.Ensutrabajoresaltanlautilizaciónde
8

dosmétricas,lacohesiónylacomplejidad.Elobjetivodetrásdeestoesconseguirmicroservicioscon-
sistentesyasítenerunaaplicaciónestablequeminimicelaocurrenciadeerrores.Además,alevaluar
losmicroserviciosdeestamanerapodemostenerunamejorguíaalahoradeagruparlosdeacuerdo
aquétanrelacionadasestánlasaccionesquedesarrollanentresí,comoporejemplositrabajancon
lamismaentidad,osiesquetodostienenunobjetivosimilarendiferentesetapasdeunproceso.
Demanerasimilaralosanteriorestrabajos,setienelapropuestade(Hussainycol.,2017),quienes
describentambiénotrosmotivosporloquealgunasempresaspresentanunaciertaresistenciaalcam-
bioomodernizacióndesusistema.Elprincipalmotivoqueencontraronparaestaresistenciaesque
elsistemaconelquecuentanactualmente,pormásdesactualizadoquepuedaestar,aúncumplecon
losobjetivosdelnegocioynopresentaunanecesidaddeseractualizado.Sinembargo,esohaceque
mantenerdichosistemaseacadavezmáscostoso,ylapreservacióndelmismoseconvierteenunata-
reaconstantementemáscomplicadadebidoalosproblemasinherentesalatecnologíaoherramienta
utilizadaeneseentonces.Frenteaesteproblemalosautoresproponen4posiblescaminosaseguir,
queson:descartarelsistemacompletamenteyevaluarnuevamentelosrequerimientosdelnegocio,
seguirrealizandoelmantenimiento,reescribiralgunaspartesdelsistemaqueseannecesarias,reescri-
birelsistemagradualmentehastareemplazarloporcompleto.Losautoresllegaronalaconclusiónde
quesinoselopuedepermitirlaempresa,porlomenosdebenrealizarlareingenieríadelosmódulos
máscríticos,paraquesepuedadarpaseluegoaunarenovacióntotal.
Envistadelacrecientenecesidadderealizarunamodernizacióndelsoftware(Somogyi&Kovesdan,
2021)hanpropuestouna herramientaparaasistirenestatarea. Ellosmencionanqueesinnegable
que realizar la modernización del software es una tarea altamente susceptible a errores, y que ade-
másconsumebastantetiempo.Sinembargo,parahacerqueestatareaseamássencillarealizaronuna
herramientaqueatravésdetécnicasdemachinelearningasistaalosdesarrolladoresalmomentode
realizar esta actividad. Esto se basa en la identificación de punteros en código en C para que sean
convertidosavariablesdeJava.Demanerasimilaraltrabajopropuestopor(Gerasimouycol.,2018)
podemos ver que uno de los puntos centrales de llevar a cabo un proceso de modernización es el
9

identificarobjetoscríticosparaelsoftware,comosonlasinvocacionesaunaAPIexterna,olasvaria-
blesesencialesqueseusanparalosdiferentesprocesos.Altenerencuentaesoselementospodemos
asegurarnosdequeelprocesodemodernizacióncumpliráconsusobjetivos.
Sepuedeconsiderarcomoejemploeltrabajorealizadopor(Wolfartycol.,2021),quienesrealizaron
unapropuestadeunahojaderutaqueseguiralmomentoderealizarlamodernizacióndesistemas
utilizando microservicios. Al inicio de su trabajo, indican que realizar este tipo de trabajos de mo-
dernizaciónesunadelasmejoresestrategiasparapromoverunamejorevolucióndelossistemasim-
plementadosalaprovecharnuevastecnologíasymetodologías.Ensutrabajoproponenorganizarel
proyectoen4fases,yenuntotalde8actividades.Llegaronalaconclusióndequeestaorganización
deltrabajopresentaligerasvariacionesentrabajosrelacionados,sinembargo,indicanqueenfuturos
trabajosesperanllegaratenerunavalidacióncompletadeestametodologíademaneraquepuedaser
consideradaunestándarosertomadacomoreferenciaporlosdesarrolladoresyasíteneruntrabajo
mejororganizado.
Aloanteriormencionadosepuedesumareltrabajorealizadopor(Yin&Du,2021),quienesmencio-
nanquelaresilienciaesunadelascaracterísticasclavedelasarquitecturasbasadasenmicroservicios.
Es por ello, que en su propuesta ofrecen una definición de la resiliencia, y un modelo con el cual
evaluarla.Ladefiniciónquenosofrecenlosautoreses“lacapacidaddelaarquitecturabasadaenmi-
croserviciosdesuperarlaocurrenciadefallosyrecuperarlosserviciosafectadosparaqueregresena
suestadonormal”.Asímismo,elmodeloqueproponenestábasadoen6elementos:elobjetivodel
sistema,larelaciónentrelossubobjetivosyelobjetivogeneral,losobstáculosalosqueseenfrentael
sistema,elagenteactivodelsistema(quienrealizaelprocesamiento),elrequerimientodelsistema,y
eldominioenelqueseencuentraelsistema,esdecir,suentorno.Losautoresllegaronalaconclusión
dequeelmodelopropuestoesefectivoalproveerunvalornuméricodelaresilienciadeunsistema,
demaneraquepuedasercontrastadoconlosvaloresesperadosparaeste.
Tambiénsepuedetomarencuentaeltrabajode(DiFrancescoycol.,2018),quienesrealizaronun
estudiosobreempresasqueestabanrealizandoelprocesodemigracióndesusserviciosaunaarqui-
10

tecturabasadaenmicroservicios.Estaencuestaserealizóconelobjetivodeconocermejorlasactivi-
dadesquellevanacabolosdesarrolladoresylosretosqueencontraronenelcamino.Dentrodelas
diferentesrespuestasqueobtuvieron,llamalaatenciónlapreguntareferenteasiseimplementaron
nuevasfuncionalidadesduranteelprocesodemigración,enlaquesólounodelosdesarrolladores
encuestadosrespondióqueno.Encuantoalosresultadosqueobtuvieron,setieneunaconfirmación
enlovistoenotrostrabajos,comoelde(Gerasimouycol.,2018),yesqueelprocesodemigración
aunaarquitecturabasadaenmicroserviciosdebeserrealizadademaneraprogresiva,ydebeseror-
ganizadacomounproyectodecarácteriterativoeincremental.Además,encontraronquelarazón
porlaquelamayoríadeencuestadosimplementónuevasfuncionalidadesesdebidoaqueelsistema
anteriornolopermitía.
Untrabajodesimilarmetodologíaalanteriormencionadoeselrealizadopor(Carvalhoycol.,2019).
En su propuesta los autores realizaron una encuesta a 15 especialistas en llevar a cabo un proceso
demigracióndeunaarquitecturamonolíticaaunabasadaenmicroserviciossobreloscriteriosque
consideranmásútilesalahoradeextraermicroserviciosycómoagruparlos.Comoresultadodela
encuesta,encontraronquelacohesióndelosmicroservicioseselcriteriomásútil,yaquemediante
dichocriteriosepuededeterminarloslímitesdeunmicroserviciodeunamaneramásrápidaysen-
cilla.Aestosesumanlosotrosdoscriteriosidentificadoscomomásútiles,quesonlareusabilidad,y
elposibleacoplamientoquepuedentenerenfuturasimplementacionesconnuevosmicroservicios.
Porotroladosetieneeltrabajorealizadopor(Knoche&Hasselbring,2018),quienesproponenel
usodeunaarquitecturademicroserviciosparalamodernizacióndesoftwareantiguo.Ellosindican
queesteestiloarquitecturalhaganadopopularidadporsufacilidaddeescalamientoenentornosde
cloudcomputing.Sinembargo,enelmercadoseestáadoptandoestaarquitecturanoporeseaspecto,
sinoporqueesaltamentemantenible.Estosedebeaquemantienenbasesdecódigomáspequeñas
porsuaislamientoencomponentes.Asímismo,dentrodesutrabajoproponenunametodologíapa-
rarealizarunatransicióndelossistemasantiguosaunomodernobasadoenmicroserviciossinque
elprocesoseamuydisruptivoparalasoperacionesdelaorganización.
11

Sepuedeverqueenlaliteraturaelusodemicroserviciosestasiendoadoptadocomolamejorarqui-
tecturadesoftwaredebidoalosdiversosbeneficiosqueaporta,comolomencionan(Balalaieycol.,
2018).Además,enambostrabajoslosautoresproponenpatronesparallevaracabounamigración
de un sistema antiguo o monolítico a uno basado en microservicios. Estos patrones forman parte
deunametodologíaqueesconsideradacomounplandemigración,debidoaquesepuedenelegir
variosparaacomodarlosalasnecesidadesdelaorganización.Apesardequesontrabajosdiferentes,
ambos llegaron a obtener modelos similares, que tras la validación correspondiente llegaron a ob-
tenerundesempeñoadecuado,enfocadosenmejorarlaescalabilidad,ymantenibilidaddelsistema
quesedesarrolleosemigreaunaarquitecturabasadaenmicroservicios.
Sinembargo,algoqueesnecesariomencionaresloqueindican(Costaycol.,2020),quienesensu
trabajodicenquesibienesciertoquelosmicroserviciosestánsiendoampliamenteaceptadosenla
industriaanivelmundial,aúnnosetieneunaguíageneralparaeltrabajoconestaarquitectura.Es
asíquesutrabajotienecomoobjetivoinvestigarelestadoactualdeestaáreaenaspectoscentralesco-
molosestándaresmásadoptados,yquétécnicasyherramientasseusanactualmenteenlaliteratura.
Losresultadosqueobtuvieronesquelamayoríadelasinvestigacionessecentranenresolverretos
relacionados con la comunicación entre microservicios en sistemasdistribuidos a nivel mundial, y
queenbaseaestomuchossistemasmáspequeñossehanvistoaltamentebeneficiados.Además,en
los entornos cloud, encontraron que las prácticas de CI/CD utilizan en su mayoría contenedores
aisladoscomoDockerpararealizarlagestióndelosmicroserviciosdesarrollados.
Aestosepuedesumareltrabajorealizadopor(Carrascoycol.,2018),quienesidentificaroncarac-
terísticasquesonpropensasagenerarfallasalahoradelaimplementacióndemicroserviciosenun
sistema,yaseadecerooalahoradellevaracabounprocesoderefactorización.Detodoslospuntos
que identificaron es importante mencionar primero que muchas veces se incurre en fallas al tener
unasolapersonahaciéndosecargodetodoelflujodedesarrollo,yquelosequiposquetrabajanen
unmicroserviciodebenconstardepersonascondiferenteshabilidadesdemaneraquesealcanceun
desarrollointegral.Unsegundopuntoimportantequeyafuemencionadoporotrosautorescomo
12

(Gerasimouycol.,2018;Knoche&Hasselbring,2018),esquenosedeberealizarunarefactorización
súbita.Esdecir,quetodoprocesodemigraciónaunaarquitecturabasadaenmicroserviciosdebeser
realizadademaneraprogresiva,manteniendodeguíalalógicadelnegocioylosmodelosexistentes.
Considerando la implementación de microservicios, se puede considerar también la propuesta de
(DeIasio&Zimeo,2021),quienesademásderesaltarlosbeneficiosdeusarunaarquitecturabasada
enmicroservicios,indicanqueensistemasdemayortamañoycomplejidad,esosserviciosrequieren
decomunicaciónysincronizaciónentresí,porquepuedeserqueseconsumandosomásdeellosal
momentoderealizarunprocesodelaorganización.Esasíqueellosproponenunframeworkpara
mejorareltrabajoysincronizacióndelosmicroserviciosdeunsistema,demaneraquepuedanopti-
mizarsealesperaraqueculminenantesdepoderserinvocadosporelsiguienteservicioenlacadena
deejecución.Trasrealizarlavalidacióndeltrabajosevióquetenerencuentaestasincronizaciónefec-
tivamentemejoraeldesempeñodelsistema,demaneraquesedebetenerencuentasuaplicaciónpara
cuandoseestétrabajandoconsistemasgrandesqueconsumanunagrancantidaddemicroservicios.
Es importante también considerar que al trabajar con microservicios vamos a tener que gestionar
unagrancantidaddecomponentes,ycuyacomplejidadseencuentraenfuncióndelanaturalezadel
sistemaenlacualseaplican,comoloindican(Engelycol.,2018).Ensutrabajolosautoresproponen
unsistemadeevaluaciónparamodelosarquitectónicosbasadosenmicroservicios,todobasadoen
un estudio realizado que muestra los principales retos en dichas arquitecturas actualmente. Algu-
nos de estos puntos de evaluación son el tamaño del microservicio, la cohesión de la arquitectura,
lacomplejidaddeladependenciaentremicroservicios,entreotros.Losresultadosobtenidosporlos
autores son bastante positivos, y al aplicar la propuesta en un sistema desarrollado con una arqui-
tecturabasadaenmicroservicioslograronidentificardiferentespuntosdemejora,ademásdeservir
comobaseparalaconstruccióndemódulosadicionales.
Además,eneltrabajorealizadopor(Pietrantuonoycol.,2020)podemosverotroaspectoimportan-
tealmomentodetrabajarconmicroservicios:eltesting.Comomencionanlosautores,asegurarla
confiabilidaddelsistemadesarrolladoescrucialparalosgerentesdelaorganización.Esporelloque
13

propusieronunmétododenominadoEMARTparallevaracabolaevaluacióndelaconfiabilidad
delsistemaenunentornooperacional.Dichaherramientaaprovechaloscasosdetestdefinidospor
losdesarrolladores,perotambiénescapazdegeneraralgunoscasosrepresentativos,demaneraquesu
monitoreodurantelafasedeevaluaciónseaefectiva.Losresultadosqueobtuvieronlosautoresfue-
ronpositivos,ydeterminaronquesupropuestapuedeserusadaconéxitopararealizarlaevaluación
delaconfiabilidaddeunsistemaconunaarquitecturabasadaenmicroservicios,dandounresultado
bastanteacertado,yseñalandolosaspectosquesedebenmejorarenelsistemaanalizado.
Así mismo, se propuso un flujo de trabajo que automatice el testing del software en el trabajo de
(Kargar & Hanifizade, 2018). Este flujo propuesto aprovecha diferentes herramientas usadas para
construirentornosdeCI/CD,comoGitLab,Jenkins,yDocker.Suobjetivoesmejorarlacalidady
estabilidaddelsoftwarealtenerunaejecucióndetestingderegresióncadavezquesetieneuncandi-
datoaproducción.Deestamanera,sepuedetenerunmecanismodeseguridadadicionalquepuede
detectarbugsantesdequeestossemanifiestencuandolosclientesutilicenelsistema.Además,enel
flujoqueproponenlosautoressetieneunnodofinalqueenbasealosresultadosdeltestingidentifica
enquéserviciosseprodujeronlasfallas,demaneraquelosdesarrolladorespuedanconocerinmedia-
tamenteelorigendelproblema.
Porotrolado,esimportanteconsiderarcómoesquealrededordelmundocadavezmásempresasy
proyectosdecidierondejardeconstruirmonolitosparapasaratenerunaarquitecturamásgranular.
Sobreestepunto(Miguelycol.,2022)mencionanquelaempresadestreamingNetflixjugóunrol
importanteenesteaspecto,aldecidirserunadelasprimerasenadoptarelnuevoparadigmaarqui-
tectónicoque eranlosmicroservicios. Elrápidocrecimiento delaempresafue demostracióndeel
impactoquepuedellegaratenerenunaempresaseguiresteparadigma,enelquepequeñosgrupos
dedesarrolladoresseencargandeunservicioyseencargandeélalolargodelciclodevidadedesa-
rrollodesoftware.
Aloanteriormencionadosepuedesumarelhechodequetenerunaarquitecturabasaenmicroservi-
ciospermitequeestosseanautónomoseindependientes,comoloindican(Gan&Delimitrou,2018;
14

Heinrichycol.,2017).Ensusrespectivostrabajoscadaunoresaltalasventajasdequecadaservicio
seaunaunidadaisladaytecnológicamenteagnósticaquesepuedecomunicarconotrosserviciosy
responderalassolicitudesdelosclientesatravésdeinterfacescomoRESTAPIsyformatosuniver-
salescomoJSON.Adicionalmente,lapropuestade(Khazaeiycol.,2020)concuerdayexpandeel
trabajo realizado por (Heinrich y col., 2017). Ambos hacen énfasis en que el principal objetivo de
seguirestaarquitecturaesmejoraryagilizarelprocesodedesarrolloeimplementacióndelsoftware;
ytambiénqueunavezquesetieneimplementadaestaarquitecturaalgoquenosedebedejardelado
eselmonitoreodeldesempeñodelosserviciosimplementados,demaneraqueenfuturasimplemen-
tacionessetengaunmejormodelodemicroservicios.
Adicionalmenteseencontróuntrabajoenelquelosautoresmencionanquedebidoalanaturaleza
delosmicroserviciosesdifícildeterminarquétamañodebentener,yaqueendiferentescasosdeuso
puedellegaratenerdiferentessignificados.Enlapropuestade(Jamshidiycol.,2018)sedetallalos
diferentes argumentos para cada posible definición, pero debido a la flexibilidad inherente que se
quieretenerconlosmicroserviciosestosedejaadiscrecióndelosdesarrolladoresymodelodene-
gociodelaempresaenlaqueseimplementan.Además,mencionanquetenerunbackendconuna
arquitecturademicroserviciosnoessuficienteparaaprovecharlosbeneficiosqueofrece,sinoque
tambiénlainterfazdebesermodular,yagruparlosmicroserviciosqueesténrelacionadosentresíde
maneraquesealcanceunverdaderoentornodemicroserviciosalolargodetodoelstackdedesarro-
llo.
Unejemplodelomencionadoeneltrabajoanteriorsepuedeverreflejadoenlapropuestade(Naik
ycol.,2021),quienesdesarrollaronunaplataformaeducativaquecomprendenadamás3microser-
vicios,unoparalagestióndelosusuarios,otroparaloscursos,yfinalmenteunoparalagestiónde
pagos. En su propuesta los autores además aprovechan otras herramientas usadas en los entornos
cloudcomoDockeryKubernetes,demaneraquesellegueatenerunmayorcontrolsobrelamanera
enlaqueserealizalaimplementacióndelosmicroserviciosquedesarrollaron.Alfinalizarlaetapade
15

validación,supropuestaalcanzólosobjetivosplanteados,resaltandolasventajasdelautilizaciónde
microserviciosenconjuntoconcontenedoresenunentornocloud.
2.2. Bases Teóricas de la Investigación
2.2.1. EnterpriseResourcePlanning
Enprimerlugar,debemosentenderloqueesunsistemadeplanificaciónderecursosempresariales
(ERPporsussiglaseninglés).Según(Oracle,2021),unsistemaERPesaquelsoftwarequeseusaen
lasorganizacionesparagestionarlasactividadesdeldíaadíaqueformanpartedelnegocio,comolas
referentesacontabilidad,compras,logística,entreotras.Esdebidoaestoqueexisteunagranvariedad
desistemasERPenelmercado,algunosquecuentanconunagranreputacióncomoSAP,quesegún
su página web (SAP, s.f.), son el líder del mercado de software de aplicaciones empresariales. Sin
embargo,existelaopcióndequelasempresasdesarrollensupropiosistemaERP,demaneraqueeste
seaconstruidoenbasealasnecesidadesdelaempresaynosetengaquepagarporlacompraysoporte
delossistemasdegrandesproveedores.
Endichoescenario,sepuedetenerelsoftwarequelaempresanecesitaconprecisión.Sinembargo,
estoimplicaunagrancantidaddedecisionesquesedebentomarparaeldesarrollodeeste.Sedebe
considerarlaarquitecturageneraldelsistema,elmotordebasededatos,entreotrosaspectospropios
deunproyectodedesarrollodesoftware.Dejandodeladoelmotordebasededatosdebidoaque
noesunfactorqueafectesignificativamentelaelaboracióndelaarquitectura,setienedoselementos
fundamentalesdetodosistema,queresaltanmáscuandosetratadeaplicacionesweb:elfrontend,y
elbackend.
2.2.2. Frontend
En lo referente al frontend, es el lado que interactúa con el cliente. Esto quiere decir que com-
prendetodoloreferentealainterfaz,eldiseñoyexperienciadelusuarioenlaaplicación,asícomola
interacciónconelusuario,deacuerdocon(Singhalycol.,2021).Enelcasodeaplicacioneswebse
16

utilizaprincipalmenteHTML,CSS,yJavaScrip.Dichoslenguajesdeprogramaciónpermitencum-
plircontodoslosrequerimientosdelainterfaz.Además,parafacilitareldesarrollodelainterfaz,con
elpasardelosañossehancreadodiferenteslibreríasyframeworkscomoAngularJS,ReactJS,SASS,
entremuchosotros.Estaslibreríasenglobantodoeldesarrollodelfrontenddelaaplicación,ydeesta
manerasepodíacompletarlacodificaciónenunmenortiempo,ademásdecontarconfuncionalida-
desextendidasdebidoalasherramientasincluidas.
2.2.3. Backend
Porotrolado,tenemoselbackend,queeselladodelservidor.Eslapartedelaaplicaciónquepro-
cesalosdatoseinformaciónquesecapturanysepresentanporlainterfaz.Estapartedelaaplicación
nopuedeservistanimanipuladadirectamenteporlosusuarios.Dentrodelbackendsedebeconsi-
deraraspectoscomolaconexióneinteracciónlabasededatos,losserviciosofuncionalidadesquese
proveeránalainterfaz,yelprocesamientoengeneraldedatos,deacuerdocon(Singhalycol.,2021).
Para el trabajo y desarrollo del backend se utilizan lenguajes que se ejecutan del lado del servidor,
yporlogeneralnopresentanfacilidadesparalaconstruccióndeinterfaces,sinoqueseenfocanen
las operaciones y funcionalidades de la aplicación. Algunos lenguajes usados para el desarrollo del
backendsonPHP,C++,Java,Python,entreotros.
2.2.4. API
Sinembargo,senecesitaunamaneraparaqueambaspartesdelaaplicaciónsecomuniquenentre
sí,yahíentraatallarloqueeslaAPI,oenelcasodeaplicacionesmásantiguas,sepuedehablardeun
webservice.Según(RedHat,2017),unaAPI(ApplicationProgrammingInterface)permitequeun
productooserviciosecomuniqueconotrossinnecesidaddeconocesdetallesdelaimplementación.
Estohacequeeldesarrolloseamásrápidoyflexible.LamejoraquepresentanlasAPIsobrelosweb
servicetradicionalesesquepuedenprocesarsolicitudesenHTTPS,ytambiénconlaestructurade
datosJSON.Caberesaltar,queconestosconceptos,todosloswebservicessonAPI,peronotodas
lasAPIsonwebservice.
17

2.2.5. REST
EsunacrónimoparaREpresentationalStateTransfer,yesunestiloarquitectónicoparasistemas
distribuidos (Fielding, 2000). Se basa en el concepto de generalidad de las entidades, y el uso de
verbosparaladiferenciacióndelosrecursosqueseinvocanatravésdelassolicitudesWeb,comoGET,
POST,PUT,PATCH,DELETE,entreotros.Esteestiloarquitecturalesunodelosmásutilizados
actualmentedebidoalafacilidadqueofrecealosdesarrolladoresparalaconstruccióndeservicios,
sobretodo en una arquitectura cliente-servidor. Es así que el servidor no almacena los estados del
cliente, y simplemente responde a las solicitudes que recibe, dejando el control del estado a cada
cliente.
2.2.6. Bundler
Un bundler, o más específicamente un "module bundler", es una herramienta que toma archi-
vosdearchivosdeJavaScriptysusdependenciasylasempaquetaenunsoloarchivo,generalmente
utilizadoparasubirloaunentornodeproducción,deacuerdocon(Kelly,2018).
2.2.7. Mantenimiento
Finalmente,sedebedefinirloqueeselmantenimiento.Según(Ganneyycol.,2020),elmanteni-
mientodesoftwareesquelaactividadqueconsisteenmodificarunproductodesoftwaredespuésde
quefuepuestoenproducciónofueentregadoalclienteparacorregirfallas,mejorarsudesempeño,
o adaptarlo a un nuevo ambiente. Esta actividad se realiza durante todo el tiempo de vida útil del
sistema,ycomprendeunconjuntodeactividades.Estaactividadformapartedelciclodevidadede-
sarrollo,yporlotantoesregular.Sinembargo,unaseñaldequeseestándandoproblemasesqueesta
actividadempiezaapresentarirregularidades,comolanecesidadderealizarlamásfrecuentemente,
oquerequierademayortiempo.
18

2.2.8. JSON
JavaScriptObjectNotation(JSON)es,según(JSON,s.f.),unformatodeintercambiodedatos
que se basa en ser ligero, universal, y sencillo de escribir tanto para humanos como para compu-
tadoras.EsteformatonacedentrodelasdefinicionesdeJavaScript,sinembargohademostradoser
extremadamenteútilcomounformatodetransferenciadeinformaciónuniversal,yaquesuestruc-
turadellave-valoressoportadaenprácticamentetodosloslenguajesdeprogramaciónmodernos.Es
debidoasusimplicidadqueseadoptórápidamenteenreemplazodelformatoXML.
2.2.9. JWT
Según(Auth0&Peyrott,s.f.),JSONWebToken(JWT)esunamaneracompactaeindependiente
paratransmitirdemanerasegurainformaciónentredosentesmedianteunobjetoJSON.LosJWT
seencuentrandefinidosenelestándarRFC7519(Jonesycol.,2015).UnJWTconstadetrespartes:
Lacabecera:contieneinformaciónsobreeltoken,comoelalgoritmoqueseusóparalafirma.
Elpayload:contienedatossobreelusuarioqueseautenticó,comoporejemplosucódigo,o
nombredeusuario,ademásdeeltiempodevalidezdeltoken.
Lafirma:comprendeelhashgeneradoporelalgoritmoelegidoparalacreacióndeltokende
lacabecera,elpayload,ylaclaveprivadadefinidaalmomentodecreareltoken.
LosJWTsonsegurosyaquedemanipularsecualquieradesusseccioneslafirmayanoseráválida,
porloqueelservidordeautenticaciónpuededeterminarfácilmentesiuntokenesauténticoono.
Además,elhashgeneradonoesreversible,porloquetenemoslaseguridaddequelafirmaesgenuina.
2.2.10. ReactJS
React es una librería de JavaScript para el desarrollo de interfaces de usuario (Facebook Open
Source, s.f.). Fue desarrollada en Facebook que fue implementada por primera vez en el 2011, dos
años más tarde fue publicada como open-source y hoy en día es mantenida tanto por Meta como
19

porlacomunidad.Actualmente,segúnlaencuestaanualdeStackOverflow(StackOverflow,2021)
esel“webframework”másutilizadoanivelmundial.
2.2.11. Go
TambiénllamadoGolang,esunlenguajedeprogramacióncreadoenGoogleenel2007,quedesde
quesehizopublicofueadoptadopordiversasempresasdebidoasurapidezycapacidaddedesarrollo
de aplicaciones robustas, concurrentes, y escalables (Google, s.f.). Es sintácticamente similar a C,
debidoaqueunodesuscreadoresesKenThompson,quiencolaboróenlacreacióndedicholenguaje
juntoaDennisRitchie.
20

3
Marco Metodológico
3.1. Alcances y Limitaciones
3.1.1. Alcance
La necesidad de desarrollar la presente propuesta de investigación es evidente debido que se re-
quiere tener una mejor manera de desarrollar el sistema de ERP de la UCSM, debido a que en su
situaciónactualcuentacondeficienciasensuestructura.Estoocasionaqueeldesarrollodelsistema
seamáscomplicadodebidoaquelaarquitecturaactualnoesescalable,ytambiénhacequeelsiste-
marequieradeunmayortiempodedesarrollo.Porestosmotivos,elframeworkadesarrollardeberá
cubrirtodosestosaspectosparaquesepuedarealizarelupgradeprogresivodelsistemaERP.
Losobjetivosdelproyectosonobtenerenunperiodode6mesesunframeworkconunaarquitectura
basadaenmicroserviciosqueseaaplicableparallevaracabolamejoradelbackenddelsistemaERP
delaUCSM.Elgradodesuaplicabilidadsemediráatravésdemétricasdedesempeñodelsistema,
asícomotambiénlausabilidaddelframeworkparaeldesarrollodelsistema.
Enbasealoanteriormentemencionado,sedefinelassiguientesfasesparalaelaboracióndelproyecto,
dentrodelascualessedefineelalcancedecadauna:
a) Revisiónbibliográfica
Larevisiónbibliográficaselimitaráalosartículosrelacionadosaltemaquehayansidopublica-
dosenlosúltimos5añosenrevistasorepositoriosdealtoimpacto,comoIEEE,ACMdigital
library,Scopus,oWebofScience.
21

b) Análisisdelafuncionalidaddelmóduloarefactorizar
SeelegiráunmodulodelsistemaERP,yseanalizarálasfuncionalidadesconlasquecuentade
maneraquesepuedanabstraerparalaelaboracióndelframework.Esteanálisisestarálimitado
alasinteraccionesnecesariasdentrodelsistema,ynoconsiderarálalógicadelnegocioyaque
noesunfactordeterminante.
c) Elaboracióndelaarquitecturayframework
Se elaborará el planteamiento del diseño de arquitectura y framework, que comprenderá el
diseñodelbackenddelsistema,yseemitiráunarecomendaciónparaeldesarrollodelasinter-
faces.
d) Refactorizacióndelmóduloelegido
Serealizarálacodificacióndelmóduloconsiderandolaarquitecturayframeworkpropuesto.
Dichomódulooperarácondatosdepruebaobtenidosdelabasededatosreal,demaneraque
serespetelaimplementaciónylosrequerimientosdeeste.
e) Validacióndelapropuesta
Lavalidacióndelmóduloserviráparaevaluarlaarquitecturapropuesta,porloqueserealizará
enbaseamétricascomotiempoderespuesta,toleranciaalaconcurrencia,entreotros.
Por otro lado, el framework debe cumplir con los requerimientos de usabilidad, por lo que
seevaluaráestecriterioatravésdeunaencuestadeopiniónalostrabajadoresdelaunidadde
implementacióndelERPdelaUCSMparaqueemitansuopiniónsobrelapropuesta.
3.1.2. Limitaciones
Laslimitacionesqueafectanalproyectosonlasrestriccionespropiasdelservidordondeseencuen-
traalojadoelERPdelaUCSM,ademásdenocontarconlibertadtotalparaelmomentoderealizar
laspruebaseimplementacióndelmódulopropuestodebidoaqueendichoservidorseencuentran
otrossistemasquenopuedendejardefuncionar.
22

3.2. Tipo y Nivel de Investigación
3.2.1. TipodeInvestigación
Enprimerlugar,esimportantemencionarquelapresenteinvestigaciónesdecarácterexperimen-
tal, ya que como indican (Hernández Sampieri y col., 2010) se quiere determinar el impacto que
tienenunaomásvariablesindependientessobreunadependiente.Enestecasoseplanteólasiguien-
tehipótesis:“Utilizarunframeworkconunaarquitecturabasadaenmicroserviciosycontecnologías
modernasmejoralaproductividaddelosdesarrolladores”.
3.2.2. NiveldeInvestigación
Elniveldelainvestigaciónsegúnsuscaracterísticasesexploratorio,debidoaquesebuscaconocer
más acerca de los servicios desarrollados con las tecnologías elegidas y la manera en la que pueden
beneficiareltrabajoenunaorganización.Además,estransversaldebidoaquesebuscaevaluarlos
resultadosenunmomentodeterminado,másnosuevolucióneneltiempo.
3.3. Población y Muestra
3.3.1. Población
LapoblaciónquesedefineeselequipodedesarrollodelaUnidaddeImplementacióndelERP
delaUCSM,conunvalordeN=7.
3.3.2. Muestra
Lamuestraqueseconsideraráparaelestudio,sonaquellosprofesionalesdedicadosaldesarrollo
ymantenimientodemóduloscríticosdelERP,conunvalorden=3.
23

3.3.3. Métodos,TécnicaseInstrumentosdeRecoleccióndeDatos
Elpresentetrabajoserádiseñadotomandounenfoquemixto,yaquetieneaspectoscualitativosy
cuantitativos.Estodebidoaqueseutilizarámedicionesnuméricasparalavalidaciónymedicióndel
objetivo;ademásderecurriralasexperienciasdelosparticipantesenelestudioparacontribuirenla
construccióndelconocimiento,comomencionan(HernándezSampieriycol.,2010).
3.3.4. TécnicasdeRecoleccióndeDatos
Larecoleccióndedatosparalapresenteinvestigaciónserealizaráatravésdedostécnicas:
Encuestas
Seaplicaráestatécnicaparaconocerdemaneraanónimayrápidalasopinionesdelospartici-
pantesenelestudioquetienequeverconlaevaluacióndelausabilidaddelframeworkquese
propone.
Análisisestáticoydinámicodeunsistema
Se aplicará esta técnica para poder conocer la manera en la que se desempeña el módulo re-
factorizadoenunentornodeproducción,demaneraquesepuedanevaluarsusmétricasen
tiempoderespuesta,toleranciaaconcurrencia,entreotros.
Juiciodeexpertos
Debidoalaslimitacionesconelnúmerodeelementosdelapoblaciónymuestra,seutilizará
latécnicaDelphiparalarecolecciónyevaluacióndelosdatosobtenidosdelaencuesta.
3.3.5. InstrumentosdeRecoleccióndeDatos
Losinstrumentosderecoleccióndedatosqueseutilizaránparalapresenteinvestigaciónsonlos
siguientes:
24

Cuestionario
Seráatravésde4preguntascerradasbajolaescaladeLikertydospreguntasabiertas.Paraesto
seutilizaráGoogleForms,ylaspreguntasplanteadassepuedenverenelAnexoA.
Logsdelservidoryscriptscomplementarios
Serecuperaránlosregistrosdelassolicitudesquealmacenaelsistemademaneraautomática,
ademásdeincluirlosresultadosdescriptsyherramientasadicionalesqueregistreninforma-
ciónqueseaderelevanciaparalaevaluaciónadecuadadetodaslasmétricascorrespondientes.
3.3.6. TécnicasdeProcesamientodeDatos
Encuantoalosresultadosdelasencuestaslatécnicaqueseutilizaráeslaestadísticadescriptiva,
demaneraquesepuedapresentarlosresultadosobtenidosdeunamanerasencillayvisualatravés
degráficosdebarras.Deestamaneralacomunicacióndelosresultadosobtenidosserámásefectiva.
Asímismo,elframeworkseráevaluadoatravésdelasmétricasinternasdelacalidaddelproductode
softwareestablecidasenelestándarISO9126.Debidoalanaturalezadelsistemaalqueseaplicará
elframework,seseleccionólasmétricasdetalladasenlasTablas3.1,3.2,y3.3.Porotrolado,parael
análisisdelosdatosrecopiladosdelanálisisestáticoydinámicodeunsistemaseutilizarálaspruebas
deanálisisestadísticodeShapiroWilkydetdeStudent.PrimeroatravésdelapruebadeShapiroWilk
sedeterminarásiesquelosdatossiguenunadistribuciónnormal,siesasí,seaplicarálapruebadet
deStudentparadeterminarsilosresultadosobtenidosdelanálisisentreelsistemaactualyelsistema
nuevopresentandiferenciasignificativa.Encasoquelosdatosnopresentendistribuciónnormalse
aplicarálapruebadeUdeMann-Whitney.Además,seelaboraráunadistribucióndefrecuenciasy
diagramasdecajasybigotesparaanalizarladistribucióndelosdatosobtenidos.
25

3.3.7. HerramientasparaelProcesamientodeDatos
Para llevar a cabo la tabulación y análisis de los datos, al igual que la obtención de los gráficos
respectivos, se utilizará la aplicación de hojas de cálculo. En cuanto a la realización de las pruebas
estadísticascorrespondientesparalavalidacióndelaspruebasseutilizaráelsoftwareestadísticoSPSS.
Tabla3.1
Detalledelamétricadeadecuidad
Nombre Completituddelaimplementación
Evaluarquétancompletaestála
Propósito
implementacióndelmódulo
Contarlacantidadderequisitosfuncionales
Métododeaplicación
propiosdelmóduloquefaltanimplementar
X = 1− A
B
Fórmula A=númerodefuncionesfaltantes
B=númerodefuncionesespecificadas
0 ≤ X ≤ 1
Interpretación
Entremáscercano1,máscompleto
TipodeEscala Absoluta
A=contador
Tipodemedida
B=contador
Especificaciónderequisitos
Fuentedemedición
Códigofuente
3.4. Estudio económico
El presupuesto para el proyecto consta de los gastos del uso de las herramientas de trabajo. Los
gastosconsideradosparaelproyectosedetallanenlaTabla3.4.
Luego,serealizóelanálisisdecostobeneficiodelproyecto,quesepuedeverenlaTabla3.5.Comose
observaendichatabla,elproyectosiesviable;yaqueapesardequenoproduceingresosensíreduce
losgastosdelainstitución,generandoasíunahorroenlostiemposdetrabajo.Además,revalorizará
elsistemaenunmontoproporcionalaloquecostórealizarlo.
26

Tabla3.2
Detalledelamétricadeeficiencia
Nombre Tiempodedesarrollo
Evaluartiemporequeridoparacompletaruna
Propósito
tarea
Realizarunamedicióndeltiemponecesario
Métododeaplicación paraactividadesdedesarrolloconel
frameworkpropuesto
Fórmula X=tiempo
Interpretación Entremáscorto,mejor
TipodeEscala Proporcional
Tipodemedida X=tiempo
Logsdelsistemaoperativo
Fuentedemedición
Logsdeherramientasdetrabajo
Tabla3.3
Detalledelamétricademantenibilidad
Nombre Tiempodemantenimiento
Evaluartiemporequeridoparacorregirerrores
Propósito
ocambiaraspectos
Realizarunamedicióndeltiemponecesario
Métododeaplicación paraactividadesdemantenimientoconel
frameworkpropuesto
Fórmula X=tiempo
Interpretación Entremáscorto,mejor
TipodeEscala Proporcional
Tipodemedida X=tiempo
Logsdelsistemaoperativo
Fuentedemedición
Logsdeherramientasdetrabajo
27

Tabla3.4
Detalledeloscostosmensualesparaeldesarrollodelproyecto
Elemento Costo
Serviciodeinternet 180
Electricidad 200
Total 380
Tabla3.5
Análisisdelcosto/beneficioderealizarelproyecto
| Categoría | Descripción        | Tipo                   | Monto(S/)  |
| --------- | ------------------ | ---------------------- | ---------- |
|           | Electricidad       | Costoindirectovariable | 200mensual |
| Costos    | Serviciodeinternet | Costoindirectofijo     | 180mensual |
|           | Costodetrabajo     | Costodirectofijo       | 450mensual |
|           | Totalcostos        |                        | 830mensual |
Reducciónen
tiempode
|     |     | Ahorrovariable | 26001 |
| --- | --- | -------------- | ----- |
mantenimientoal
sistema
Beneficios
Revalorizacióndel
|     |     | Ingresovariable | 300002 |
| --- | --- | --------------- | ------ |
sistema
Reducciónenel
tiempode
|     |     | Ahorrovariable | -   |
| --- | --- | -------------- | --- |
procesamientode
solicitudesalservidor
Reducciónenel
tiempodeespera
|     |     | Ahorrovariable | -   |
| --- | --- | -------------- | --- |
paralasoluciónde
errores
Reducciónenel
tiemporequerido
|     | paraelcumplimiento | Ahorrovariable | -   |
| --- | ------------------ | -------------- | --- |
detareas
administrativas
|     | Totalbeneficios |     | 32600 |
| --- | --------------- | --- | ----- |
1
DeacuerdoconelcálculomostradoenlatabladelanexoB,tomandoencuenta4desarrolladores
principales.
2 DeacuerdoconelcálculomostradoenlatabladelanexoC.
28

3.5. Plan del proyecto
ParaeldesarrollodelproyectoseeligiólametodologíaSCRUM,demaneraquesetengauntra-
bajoiterativoeincremental.Paraesto,sehadefinidoeltrabajoen5fases,cadaunadelascualesserá
un sprint. Las fases definidas y las actividades que se considera por cada una de ellas se puede ver
representadoenundiagramadeGanttenlaFigura3.1.
PlanificacióndelproyectopresentadaenundiagramadeGantt
Figura3.1.
FASE 1 FASE 2 FASE 3 FASE 4 FASE 5
DURACIÓN
N° ACTIVIDAD
(DÍAS)
S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11 S12 S13
1 Revisión bibliográfica
Búsqueda y lectura de artículos
1.1 8
científicos
1.2 Elaboración del estado del arte 10
1.3 Elaboración del marco teórico 10
Análisis de la funcionalidad del
2
módulo a refactorizar
2.1 Selección del módulo 3
Análisis de sus casos de uso y modelo de
2.2 7
datos
Análisis de la interacción que tiene con el
2.3 7
backend
3 Elaboración de la arquitectura y
3.1 Selección de tecnologías y librerías 7
3.2 7
Diseño de la arquitectura para el backend
3.3 Construcción del framework 7
4 Refactorización del módulo
4.1 Configuración del entorno de desarrollo 3
Codificación del módulo utilizando el
4.2 10
framework desarrollado
4.3 Fase de pruebas locales 3
5 Validación de la propuesta
5.1 Medición del desepeño del sistema 7
Evaluación de la usabilidad del
5.2 7
framework
29

4
Desarrollo de la propuesta
Dentro del presente capítulo se desarrolla los aspectos correspondientes al desarrollo de la pro-
puesta.Lasfasesqueseproponenseobtuvierontraslarevisióndelestadodelarte,endondeseob-
servóquetodaslaspropuestassiguenelmismoprocedimientoengeneralconligerasmodificaciones.
Sinembargo,lapropuestamásrepresentativaeslade(Wolfartycol.,2021),quienesestablecieronuna
hojaderutaparalamodernizacióndesistemas.Elesquemaresumendelametodologíasepuedever
enlaFigura4.1.
Esquemadelametodologíadedesarrollo,adaptadode(Wolfartycol.,2021)
Figura4.1.
A B
Análisis del código actual
C D
Elaboración de la nueva
Servicios y
arquitectura
aplicaciones de estilo
monolítico
Transformación del código y
generación de la plantilla
Validación y Verificación
Las interfaces consumen
microservicios
30

4.1. Análisis del Código Actual
Elprimerpasoesllevaracabolaetapadeanálisisdelcódigoactual,durantelacualsebuscallegar
aentendermejorelsistemaquesequiererefactorizar,demaneraquesepuedadescomponerenmi-
croservicios.
ActualmenteelsistemaERPdelaUCSMseencuentradesarrolladobajounestilomonolítico,por
loqueelrepositoriodecódigofuenteesbastanteextenso,ypresentaunaaltaentropía.Estoencon-
secuenciahacequeseacadavezmásdifícildemantener,ylasolucióndeproblemasrequieredeun
mayorperiododetiempo.Estoasuvez,afectalaproductividaddelosdesarrolladoresyaquetanto
paraeldesarrollodenuevasfuncionalidadescomoparalasactividadesdemantenimientotienenque
lidiarconunrepositoriocomplejoyenconsecuenciarequierendemástiempo.
Actualmente se usa la tecnología PHP como base del sistema, y utiliza para las interfaces el motor
deplantillasdeSmarty.EnlaFigura4.2semuestraelresultadodelcomando enlaraízdelrepo-
ls
sitorio. Como podemos ver, se tiene una gran variedad de carpetas y archivos, con 776 elementos
en el directorioraíz. Estohace que ubicar un archivosea bastante complicado, y por lamanera en
la que se nombraron los archivos no se puede saber que funcionalidad cubre cada uno. A esto, se
sumaelhechodequeporelusodeSmartyydePHP,cadafuncionalidadseencuentradivididaen
dosarchivos,unarchivoconelcódigoenPHPquecontrolalalógicadelavista,yotroarchivoen
HTMLquepresentalainterfazdelusuario.Algunasvecessepuedellegarinclusoanecesitar3ar-
chivoscuandosetienealgúncomportamientoonecesidadmáscompleja,comoporejemploenlas
tablasquepresentaninformacióndeunamaneramásdetalladaoconfrecuenteactualización.Alo
anterior mencionado, se suma el hecho de que se generan archivos de cache, lo que si bien puede
ayudareneltiempodecargadelasinterfaces,estopuedeocasionarproblemaseneldesarrolloalmo-
mentoderesolverunerror.
ComocasodeestudiodelpresentetrabajoserealizarálaimplementacióndeunmóduloparalaBo-
ticaAliviari.Endichocentrodecostosepresentaunproblemaconlasnotasdecréditoy/obonosde
descuentoqueemitenlosproveedores.Estosedebeaqueelregistrodedichosdocumentosserealiza
31

Capturadellistadodearchivosydirectoriosenlaraízdelrepositorio
Figura4.2.
32

demaneramanual,ysedebeemitiruninformeparaqueenladireccióndecontabilidadserealice
el pago de los comprobantes respectivos aplicando los descuentos correspondientes. Como punto
decomparaciónsetendráelmóduloimplementadobajoelesquemadedesarrolloactual,yporotro
ladosetendráunaimplementaciónconsiderandoelframeworkpropuesto.Elflujodetrabajoactual
consisteenquealtenerproductosqueestánporcaducarenlabotica,estossedevuelvenalprovee-
dor, quien puede reponerlos, o caso contrario emite una nota de crédito o un bono de descuento
parafuturascomprasalproveedor.Esasíquesellevaunregistromanual,ycadamesseelaboraun
informamanualmenteporlaencargadadelaboticaqueindicaquenotasdecréditoybonosfueron
entregadosporlosproveedores.
Este informe se envía a la dirección de logística, quienes dan el visto bueno y luego se envía dicho
informealadireccióndecontabilidadparaqueseregistreelpagoysedenlosbonosylasnotasde
créditoporcontabilizadas.Sinembargo,esteprocesospuedeautomatizarseypuedesimplificarsea
travésdelERP.
Sellevaráacabolaimplementacióndeunmóduloquecuentecon3opcionesprincipales.Lapri-
meraquepermitarecuperarlascomprasyventasrealizadasenlaboticadelsistemadefacturación
electrónica;lasegundaopciónconsistiráenunapantalladeregistrodenotasdecrédito,enlacualse
podráingresartodoslosdatosnecesariosparadichodocumento;yfinalmente,laterceraopciónper-
mitiráregistraralabasededatosloscomprobantesqueseveránafectadosporlasnotasdecrédito,de
maneraqueladireccióndecontabilidadtengaunaccesodirectoaesainformaciónylaelaboración
deuninformeyanoseanecesaria.
Porotrolado,sedebemencionarqueelsistemaERPactualmenteseencuentraconstruidobajoel
paradigmadelaprogramaciónorientadaaobjetos,porloquesetienearchivosenlosquesedefine
lasclasesqueseutilizanenelsistema.Estosarchivosporlogeneralsuelenexcederlas5000líneasde
código,porloqueeltrabajoconestetipodearchivosestedioso,ygeneracomplicacionesalahora
dedesarrollarnuevasfuncionalidadesoderealizarelmantenimientoaopcionesanteriores.
33

4.2. Elaboración de la Nueva Arquitectura
Enbasealasnecesidadesdelmódulosepuedeelaborarunainterfazdeservicios,agrupándolosde
acuerdoalasentidadesconlasquevanainteractuar.DichodiagramasepuedeverenlaFigura4.3.
Enbasealainterfazdeserviciospodemossepararlosserviciosrequeridosendoscategorías,aquellos
DiagramadeinterfazdeserviciosdelmóduloparalaBoticaAliviari
Figura4.3.
Elaboraciónpropia.
Nota:
queformanpartedelafuncionalidaddelmóduloensí,yelserviciodeautenticaciónquepuedeser
reutilizadoporlosdemásserviciosqueseimplementenenelfuturo.Esasíquelaarquitecturaquese
tendríaparalosserviciosdelERPsepuedeserenlaFigura4.4.Endichafigurapodemosobservarlos
diferentesmódulosqueformaríanpartedelaarquitectura,yquetodossecomunicanconelservicio
deautenticación.Deestamanerasemantieneelcódigoaisladoeindependientedeotrosmódulos.
4.3. Transformación del Código y Generación de la Plantilla
Unavezquesetienedefinidoslaarquitecturaylosservicios,elsiguientepasofueeldesarrollode
unmicroservicio,demaneraquepuedasertomadodeejemployconstruirlaplantilladecódigoen
baseaeste.
El primer microservicio que se eligió para ser desarrollado es el de autenticación. Este comprende
34

DiagramadelaarquitecturaquetendríanlosserviciosdelERP
Figura4.4.
Autenticación
REST
REST
API Botica Contabilidad
REST
Gateway Aliviari
REST
DB
REST
Logística
Etc…
REST
Elaboraciónpropia.
Nota:
quesevalidenlascredencialesdeunusuario.Altenerunaarquitecturabasadaenmicroserviciosque
seránaccedidosmedianteRESTsedebetenerunmecanismoquepermitagestionarlaautorización
de acceso a los servicios. Para esto se implementó en servidor los métodos adecuados para generar
yverificarJSONWebTokens(JWT).Manteniendoparaelaccesstokenuntiempode5minutosy
paraelrefreshtokenuntiempodevalidezde15minutos.
EsasíqueparaconstruirlaaplicaciónserealizólaconfiguracióndellenguajedeprogramaciónGo
en el entorno de desarrollo, y se creó los directorios correspondientes para el desarrollo. Tras crear
losarchivoscorrespondientessellegóatenerlaestructuraquesemuestraenlaFigura4.5,endonde
podemosverquesetieneelpuntodeentradaenlaraízdeldirectorio,ydentrodelacarpetahand-
lerssetienelosarchivosdelasdiferentesaccionesqueestánpresentesenelserviciodeautenticación.
Cabe resaltar la existencia del archivo , que contiene funciones y variables globales que son
utils.go
reutilizadas.
Porotrolado,paralainterfazseutilizaráReactJS,debidoaqueeslalibreríadedesarrollowebmás
usadaanivelmundialsegúnlaencuestarealizadapor(StackOverflow,2021),yaqueofreceunagran
gamadefuncionalidadesyherramientasalosdesarrolladoresparacrearinterfacesdinámicasdeuna
35

Capturadelaestructuradearchivosdelserviciodeautenticación
Figura4.5.
manerasencillayeficaz,además,alserlalibreríamásutilizadacuentaconunacomunidadbastante
activa,porloquesisetieneproblemasosisedeseaconocercómoconstruiralgosepuedeencontrar
lasoluciónenlosdiferentesforosdeinternetsinproblemas.ParalacreacióndelproyectodeReactJS
seutilizólaherramientaVite,querealizaelscaffoldingdetodoslosarchivosyconfiguracionesnece-
sariasparaeldesarrollo.Además,ViteusaESBuildcomobundlerparaelservidordedesarrollo,de
maneraquesetengauniniciorápido,ycuandoserealizalacompilacióndelbundledeproducción
utilizaunaconfiguraciónpersonalizadadeRollup.
EsasíquetenemoslaestructuradearchivosquesemuestraenlaFigura4.6unavezcompletadoel
desarrollodelasinterfaces.Deestaestructuraesimportantemencionarqueeldesarrolloserealizará
principalmenteenelsubdirectoriodepagesydecomponents,mientrasqueelrestodelosarchivos
contienefuncionalidadadicionalparagestionarlaautenticación.Además,unavezsecompleteelde-
sarrollo,setendráúnicamente3archivosparasubiralservidor,unodeHTML,unodeJavaScript,y
unodeCSS,ademásdelasimágenesquehayamosincluido.
Enestepuntoyasetienelaestructurabásicadelproyecto,quepuedetomarsedereferenciaparael
36

Capturadelaestructuradearchivosdelainterfazdeautenticación
Figura4.6.
37

desarrollodelosdemásmicroserviciosqueconformaránelsistema.
Comosepuedever,cadamicroservicioseenfocaenmantenerlacantidadmínimaeindispensablede
archivosydecódigofuente,aprovechandolasherramientasquenosofrecenlastecnologíaselegidas
lomásquesepuede.Además,porlamaneraenlaqueestátodoorganizado,sepuedeencontrarlos
archivossobrelosquesenecesitatrabajardeunamaneramuchomásrápidayefectiva.EnlaFigura
4.7podemosverelárboldearchivoscompletodelserviciodeautenticación,considerandotantola
interfazcomoelbackend.
Dentro del proyecto se incluyen así mismo archivos necesarios para un trabajo más eficiente. Por
ejemplosesugierelautilizacióndelaherramientaPrettierparaqueformateeelcódigodelfrontend
de manera automática, por lo que considera un archivo de configuración para dicha herramienta.
Además,setieneelarchivo.gitignoreparaquelosdirectoriosdondesedescarganlasdependencias
noseanconsiderarosenelcontroldeversionamiento.
4.4. Testing
Adicionalmente,seconsdieraproporcionardentrodelframeworklasherramientasnecesariaspara
llevarcabodiferentestiposdetesting,loscualessedetallanacontinuaciónconloscasosdefinidosy
susresultadoscorrespondientes.
4.4.1. PruebasUnitarias
Paralaspruebasunitariassedefinieronlossiguientescasosdeprueba,atravésdeloscualessebusca
asegurarqueelsistemaestápreparadopararesponderalassolicitudesqueserealicedesdeelcliente.
LoscasosdefinidosparalaspruebasunitariassepuedenverenlaTabla4.1.
AtravésdelapropialibreríadetestingdeGo,sepudodefinirdiferentescasosdetestunitariospara
elmicroserviciodesarrollado.Estosmásquenadaestánorientadosaprobarlavalidacióndeparáme-
tros,demaneraqueseasegurequeseestárealizandolasverificacionesadecuadas.Además,Gonos
38

Capturadelárboldearchivosdelmicroserviciodeiniciarsesión
Figura4.7.
39

Tabla4.1
Casosdepruebadefinidosparalaspruebasunitarias
ID Nombre Resultadoesperado Estado
Elsistemaretornaunmensajeindicando
PU-01 TestWrongDNILenght Exitoso
erroresenelcampoDNI
Elsistemaretornaunmensajeindicando
PU-02 TestMissingDNI Exitoso
erroresenelcampoDNI
Elsistemaretornaunmensajeindicando
PU-03 TestMissingClave Exitoso
erroresenelcampoClave
Elsistemaretornaunmensajeindicando
PU-04 TestMissingBoth Exitoso
erroresenloscamposDNIyClave
Elsistemaprocedeconlaejecucióndela
PU-05 TestCorrectParams Exitoso
consulta
presentalafacilidaddequetodoslosarchivosqueterminenconelsufijo seránejecutadosbajo
_test
elcomandotest,porloquepodemoscorrertodaslaspruebasdefinidasautomáticamente.Además,
mediantelamismalibreríadetestingpodemosgenerarunreportedecoberturadeloscasosdetest
quedefinimos.
EnlaFigura4.8podemosverlaejecucióndeloscasosdepruebadefinidosyelporcentajedecober-
turaquesealcanzó.
4.4.2. PruebasIntegrales
Encuandoalaspruebasintegrales,seutilizólaherramientaJestdeReactJS,yaqueatravésdeella
desdelainterfazpodemosprobarsiesquelosdatosqueregresarondelbackendsonlosadecuados.
ParaestapruebasedefinieronloscasosdetestdefinidosenlaTabla4.2.
AlhaberdefinidoestapruebaatravésdeJestparaprobarlosresultadosdesdelainterfaz,losresulta-
dosdelapruebasemuestranmásadelanteenlaFigura4.9,juntoconlosresultadosdelaspruebas
funcionales.
40

Ejecucióndepruebasunitariasycobertura
Figura4.8.
Tabla4.2
Casosdepruebadefinidosparalaspruebasintegrales
| ID Nombre | Resultadoesperado | Estado |
| --------- | ----------------- | ------ |
Elmicroserviciodeautenticaciónse
| PI-01 TestIntegracion |     | Exitoso |
| --------------------- | --- | ------- |
comunicaadecuadamenteconeldemenú
41

4.4.3. PruebasFuncionales
Alhabersedesarrolladounmicroserviciodeautenticación,sepuederealizarpruebasfuncionales
alverificarquealenviardiferentesDNIsycontraseñaslaAPInosretornalainformaciónadecuada
paradichousuario.Parahaceresto,podemosutilizarnuevamentelaherramientaJest,atravésdela
cualverificamosquelosdatosquenospresentaelmenúdeopcionesdeusuarioregresalosvalores
adecuados.LoscasosdepruebadefinidossedetallanenlaTabla4.3.
LosresultadosdeestapruebasemuestranenlaFigura4.9,dondeatravésdelaterminalseejecutó
todoslostestdefinidosconJest.Endichafigurasepuedeverlosdostestsfuncionalesdefinidos,así
comotambiéneltestdeintegración,cadaunodentrodesupropiodirectorio.
Tabla4.3
Casosdepruebadefinidosparalaspruebasfuncionales
ID Nombre Resultadoesperado Estado
Elsistemavalidalascredenciales
PF-01 TestAutenticacion Exitoso
correctamente
Elsistemapresentalasopcionesalasque
PF-02 TestInitMenu Exitoso
tieneaccesoelusuario
ResultadosdelaejecucióndelaspruebasdefinidasconJest
Figura4.9.
42

4.5. Estrategia de Despliegue
Unaprimerapartedelaestrategiadedespliegueeslapublicacióndelframeworkenunrepositorio
públicodeGitLab,demaneraquepuedaseraccedidopúblicamente,yclonadoporlosdesarrollado-
resquelonecesiten.Deestamaneratambiénsepuedegestionarloscambiosyactualizacionesenla
versióndelframework.
EncuantoalaestrategiaderefactorizaciónqueseguiráparaelERPesunacombinacióndelrolling
deploymentycanarydeployment.Estodebidoaqueeldesplieguedelosmódulosofuncionalidades
refactorizadasserealizaráporfases,conformesevayacompletandoeldesarrollodelasfuncionalida-
des;yasuvez,estasfuncionalidadesnoestarándisponiblesalatotalidaddeusuarios,sinoquesedará
accesoaciertosusuariosaliniciodemaneraquesepuedaprobarquetodofuncionaadecuadamente
antesdepublicarelmóduloensutotalidad.Adicionalmente,amanerademantenerunrespaldode
seguridad,ambasversionessemantendránenunentornodeproducciónhastaquesetengalasegu-
ridad de que el módulo refactorizado cumple con todos las funcionalidades requeridas de manera
satisfactoria.
43

5
Análisis y Validación de Resultados
5.1. Validación Cualitativa
Tras haber desarrollado el primer microservicio, se procedió a tener reuniones con las personas
pertenecientesalgrupoelegidoparalamuestradelpresenteestudio.
Losparticipantes,quienesaceptaronparticipardelpresenteestudio,cuentanconelsiguienteperfil:
1. Desarrollador1
EgresadodelacarreradeIngenieríadeSistemasdelaUCSMhace3años
EstudiantedemaestríaenlaUCSM
4añosdeexperienciaeneldesarrolloconPHPyHTML
EnelERPrealizaeldesarrolloymantenimientodemóduloscríticos
2. Desarrollador2
EgresadodelacarreradeIngenieríadeSistemasdelaUCSMhace1añoymedio
2añosdeexperienciaeneldesarrolloconPHPyHTML
EnelERPrealizaeldesarrolloymantenimientodemóduloscríticos
Recopilarequerimientosparaeldesarrollodenuevasfuncionalidadesomódulos
3. Desarrollador3
EgresadodelacarreradeIngenieríadeSistemasdelaUCSMhace1añoymedio
2añosdeexperienciaeneldesarrolloconPHPyHTML
44

EnelERPrealizaeldesarrolloymantenimientodemóduloscríticos
Desarrolla,mantiene,ygestionaloswebserviceinternosyexternosdelaUCSM
Adichaspersonasselespresentóelframeworkdesarrolladoparaconocersusopiniones.Selesex-
plicólosaspectostécnicosyelflujodetrabajoquesesueletenerconestasherramientasdeacuerdoa
lorevisadoenelestadodelarteyenlasbuenasprácticas.Posteriormente,selesrealizólaspreguntas
planteadasenelcuestionario.
Comofrutodelosresultadosdelaencuesta,seobtuvocomoresultadosdelaspreguntascerradaslos
valoresmostradosenlaTabla5.1.
Encuantoalaspreguntasabiertas,seobtuvolavalidacióncorrespondiente.Todoslosparticipantes
Tabla5.1
Resultadosdelaspreguntascerradasdelaencuestaaplicada,donde5es“totalmentedeacuerdo”y0es“total-
menteendesacuerdo"
Ítem ValoraciónPromedio
Elframeworkpresentadopuedemejorarla
4.67
calidaddesoftwarequeusteddesarrolla
Elframeworkpresentadofacilitaríalastareas
4.67
demantenimientodesoftware
Elframeworkpresentadoleparecesencillode
4.67
aprenderyutilizar
Ustedseadaptaríafácilmenteaunflujode
4.67
trabajoutilizandoelframeworkpresentado
respondieronqueelframeworkpropuestomejoraríademanerasignificativaeltiempodedesarrollo.
Resaltandolasfacilidadesquesetieneparalavalidacióndedatos,asícomotambiénlafacilidadde
crearproyectosutilizandolabasepresentada,ytambiénlasimplicidaddelapuestaenproducción
yaquelosarchivoscompiladossonindependientes.
Asímismo,alpresentarlapropuestaalIng.FernandoParedesMarchena,jefedeláreaenlaquese
desarrollóelpresentetrabajó,manifestósuconformidad.Porloqueseutilizaráelframeworkpro-
puestoparaproyectosdelárea,comosepuedeverenlacartadelanexoD.
45

5.2. Validación cuantitativa
Debidoalanaturalezadelsistemaqueseestádesarrollando,serealizaronalgunostiposdetestpa-
raasegurarqueelframeworkdesarrolladomantendrálosestándaresrequeridosporlaorganización.
PararealizarlaspruebasseutilizólaherramientadeK6,quecomoseindicaen(Grafana,2021),es
unaherramientadetestingdecargamodernadiseñadaparadesarrolladoresytestersdelaeramoder-
na.Dichaherramientanospermiterealizardiferentespruebasyanalizardiferentesmétricasdeuna
maneramuysencilla,aligualquesimulardiferentesescenarios.
5.2.1. PruebasenEntornodeDesarrollo
Pruebadecarga
Enunaprimerainstanciaserealizóunapruebadecargaalmicroserviciodesarrollado,lamisma
queseaplicóalsistemaactual.Estapruebasimplementemideeltiempoderespuestadeunasolicitud
GETparaingresaralapáginadeiniciodesesión.Ambaspruebassellevaronacaboenunentornode
desarrollo,sinembargo,puedenreflejarelcomportamientoquesetendráenunentornodeproduc-
ción.LosresultadoscompletosdeestaprimerapruebasepuedenverenelanexoE.1paraelsistema
actual,enelanexoE.2paraelsistemadesarrolladoconelframeworkpropuesto,yenlaTabla5.2se
muestralacomparacióndelosresultadosentreelmicroserviciodesarrolladoconelframeworkpro-
puestoyelsistemaensuestadoactual.Enestaprimeraprueba,sepuedeverqueelusodelframework
propuestopresentaunamejorademásdel95%entodosloscasosencomparaciónconlosvalores
obtenidosdelsistemaactual.
Luego,sepasóarealizarunapruebadecargaenlaquesetengaunainteracciónconlabasededatos,
de manera que se pueda tener una simulación de cómo será la interacción el sistema. Para esto, se
realizólapruebadecargasimulando1únicousuario,10usuariossimultáneos,y200usuariossimul-
táneos,quienesrealizaránlaconsultade“Iniciarsesión”demanerarepetitivadurante10segundos.
LosresultadosdeejemplosepuedenverenelanexoE.3paraelsistemaactualyenelanexoE.4para
elframeworkpropuesto.
46

Tabla5.2
Comparacióndelapruebadecargarealizada
Tecnología
| Ítemevaluado |     |               |     |                    |        |     |     | Mejora(%) |       |
| ------------ | --- | ------------- | --- | ------------------ | ------ | --- | --- | --------- | ----- |
|              |     | SistemaActual |     | FrameworkPropuesto |        |     |     |           |       |
| Datarecibida |     | 57kB          |     |                    | 6.75kB |     |     |           | 88.16 |
Tiempopromediode
|     |     | 37.63ms |     |     | 23.06ms |     |     |     | 38.72 |
| --- | --- | ------- | --- | --- | ------- | --- | --- | --- | ----- |
respuestadelservidor
Promediodeladuracióndela
|     |     | 37.97ms |     |     | 23.38ms |     |     |     | 38.43 |
| --- | --- | ------- | --- | --- | ------- | --- | --- | --- | ----- |
solicitudhttp
Tabla5.3
Análisisestadísticodelapruebadecargadurante10segundosalsistemaactualyalsistemadesarrolladoconel
frameworkpropuestosegúnelnúmerodeusuarios
|                   |        | SistemaActual |                  |         |     | Frameworkpropuesto |       |             |        |
| ----------------- | ------ | ------------- | ---------------- | ------- | --- | ------------------ | ----- | ----------- | ------ |
| ESTADÍSTICOS      |        |               | NÚMERODEUSUARIOS |         |     |                    |       |             |        |
|                   |        | 1             | 10               | 200     |     | 1                  | 10    |             | 200    |
| n                 |        | 10            | 10               |         | 10  | 10                 | 10    |             | 10     |
| Promedio(ms)      |        | 26,84         | 162,84           | 1878,00 |     | 16,07              | 35,76 |             | 68,26  |
| DE(ms)            |        | 6,40          | 5,80             | 53,29   |     | 0,20               | 4,43  |             | 14,29  |
| Vmín(ms)          |        | 21,58         | 25,35            | 16,29   |     | 13,84              | 24,06 |             | 34,46  |
| Vmáx(ms)          |        | 36,50         | 198,78           | 2377,00 |     | 28,35              | 66,50 |             | 113,88 |
| Tiempodemejora(%) |        |               | -                |         |     | 37,39              | 77,99 |             | 96,36  |
|                   | NÚMERO |               | 1                |         |     | =5,32t             |       | =1,83p<0,05 |        |
t
| Pruebadehipótesis |          |     |     | investigacion |     |          | critico |             |             |
| ----------------- | -------- | --- | --- | ------------- | --- | -------- | ------- | ----------- | ----------- |
|                   |          | DE  | 10  | t             |     | =53,96t  |         | =1,83p<0,05 |             |
| tdeStudent        |          |     |     | investigacion |     |          | critico |             |             |
|                   | USUARIOS |     | 200 | t             |     | =103,73t |         |             | =1,83p<0,05 |
|                   |          |     |     | investigacion |     |          |         | critico     |             |
n:númeroderepeticiones
DE:desviaciónestándar
Vmín:valormínimo
Vmáx:valormáximo
Tiempodemejora(%): Duraciondesolicitudensistemaactual−Duraciondesolicitudenelframeworkpropuesto
×100
Duraciondesolicitudenelframeworkpropuesto
47

Los resultados obtenidos tras realizar 10 iteraciones se muestran en la Tabla 5.3. A estos datos
seaplicóinicialmentelapruebadeShapiroWilk,atravésdelacualseencontróquelosresultados
se ajustan a una distribución normal con un valor p > 0,05. Sabiendo eso, se aplicó la prueba de
contrastedetdeStudent,endondeseencontróquesiexistediferenciasignificativa(p<0,05)entre
laduracióndelasolicitud(ms)delsistemaactualydelframeworkpropuesto,encontrandoenesta
última tecnología menores promedios. Es importante mencionar que el porcentaje de tiempo de
mejoraesmayormientrassetengaunmayornúmerodeusuariosconcurrentes,siendoenelcasode
200usuariosconcurrentesunamejorade96,36%.Asímismo,losdatosobtenidossegraficaronpara
presentarlosresultadosdeunamaneravisualysencilla.DichográficosepuedeverenlaFigura5.1.
PruebadeEstrés
Encuantoalaspruebasdeestrésserealizóunapruebaenlaquesesimulaunescenarioquepo-
dríapresentarseenlarealidad.ElescenarioqueseprogramóconlaherramientadeK6esqueenlos
primeros30segundossetengaunaconexiónde200usuariosquienesrealizansolicitudesconstante-
mente,luegoenelminutoymediosiguientesestenúmerodeusuariosdisminuyeprogresivamente
a100,perosiguerealizandosolicitudesalservidor,yfinalmente,enlosúltimos20segundossetiene
unadesconexiónprogresivadetodoslosusuarios.
EnelanexoE.5sepuedeverunacapturadeejemplodelapruebadeestrésrealizadaalsistemaactual
yenelanexoE.6sepuedeverparaelframeworkpropuesto.Ylosresultadosqueseobtuvieronde
estapruebasepuedenverenlaTabla5.4.
DeigualmaneraqueconlosdatosdelapruebadeShapiroWilkparaverificarsilosdatospresentan
unadistribuciónnormal.AlserasípodemosaplicarlapruebadetdeStudent,conlacualseobtuvo
que existe una diferencia significativa (p < 0,05) entre la duración de la solicitud (ms) del sistema
actual y del framework propuesto, encontrando que en esta última tecnología se tiene un menor
tiempopromedio.
Asímismo,elframeworkpropuestopresentaunmayorporcentajederespuestasexitosas(99,86%),
48

Promediodeladuracióndelasolicituddelsistemaactualyelframeworkpropuestosegún
Figura5.1.
elnúmerodeusuarios
49

Tabla5.4
Análisisestadísticodelapruebadeestréscon200usuariosalsistemaactualyalframeworkpropuesto
200USUARIOS
ESTADÍSTICOS
|                     | SistemaActual | FrameworkPropuesto |
| ------------------- | ------------- | ------------------ |
| n                   | 10            | 10                 |
| Promedio(ms)        | 1807,00       | 261,58             |
| DE(ms)              | 65,16         | 34,61              |
| Vmín(ms)            | 15,59         | 13,80              |
| Vmáx(ms)            | 2909,00       | 4488,00            |
| Tiempodemejora(%)   | -             | 85,50              |
| Respuestaexitosa(%) | 98,53         | 99,86              |
| Respuestafallida(%) | 1,47          | 0,14               |
t =66,24
| Pruebadehipótesis | Pruebadeestrés | investigacion |
| ----------------- | -------------- | ------------- |
t =1,83
| tdeStudent |     | critico |
| ---------- | --- | ------- |
p<0,05
t =36,61
|     | Respuestaexitosa | investigacion |
| --- | ---------------- | ------------- |
t =1,83
critico
p<0,05
n:númeroderepeticiones
DE:desviaciónestándar
Vmín:valormínimo
Vmáx:valormáximo
Tiempodemejora(%): Duraciondesolicitudenelsistemaactual−Duraciondesolicitudenframeworkpropuesto ×100
Duraciondesolicitudenelsistemaactual
50

existiendotambiéndiferenciasignificativa(p<0,05)enrelaciónconlatecnologíaactualmenteim-
plementada,teniendounamejoradel85,50%.Asímismosegraficaronlosresultadosobtenidospara
sumejorvisualización,loquesepuedeverenlaFigura5.2.
Promediodeladuracióndelasolicitudenunapruebadeestréscon200usuariosalsis-
Figura5.2.
temaactualyalframeworkpropuesto
5.2.2. PruebasenEntornodeProducción
Pruebadeestrés
Paratenerunamejorrepresentaciónestadísticadelapruebadeestrésrealizadaalservidordepro-
ducción,serealizaron40iteracionesconK6configuradoa200VU(virtualusers).Deestamaneraal
realizarelanálisiscorrespondientepodemostenerunamayorcertezadelosdatos.Losresultadosde
estosepuedenverenlaTabla5.5.EnlaTabla5.5seobservaqueel12,50%deiteracionesseregistran
51

Tabla5.5
Distribucióndefrecuenciasdeladuracióndesolicitudpromedio(ms)depruebasdeestrésalsistemaactual
| DURACIÓNDE | NÚMERODE | NÚMERODE |     | PORCENTAJE |
| ---------- | -------- | -------- | --- | ---------- |
PORCENTAJE
| SOLICITUD |             | ITERACIONES |     |           |
| --------- | ----------- | ----------- | --- | --------- |
|           | ITERACIONES |             |     | ACUMULADO |
(%)
| PROMEDIO  |          | ACUMULADO |        |        |
| --------- | -------- | --------- | ------ | ------ |
|           | (/200VU) |           |        | (%)    |
| (ms)      |          | (/200VU)  |        |        |
| 6789-6875 | 6        | 6         | 15,00  | 15,00  |
| 6876-6962 | 9        | 15        | 22,50  | 37,50  |
| 6963-7049 | 11       | 26        | 27,50  | 65,00  |
| 7050-7136 | 2        | 28        | 5,00   | 70,00  |
| 7137-7223 | 7        | 35        | 17,50  | 87,50  |
| 7224-7310 | 5        | 40        | 12,50  | 100,00 |
| TOTAL     | 40       |           | 100,00 |        |
VU:virtualusergeneradoporK6
en el último intervalo que va de 7224 ms a 7310 ms. Es importante mencionar que en esta distri-
buciónlaamplituddeintervaloesde87ms.Asímismo,siseconsideraelporcentajeacumulado,el
65,00%registraronunaduraciónpromedioentre6789msy7049ms.EnlaTabla5.6seobservaque
el5,00%deiteracionesseregistranenelúltimointervaloquevade4219msa4250ms.Enestecaso
la distribución presenta una amplitud de intervalo de 32 ms. Además, considerando el porcentaje
acumulado,el62,50%registraronunaduraciónpromedioentre4059msy4154ms.
Laduracióndesolicitudpromediodelframeworkpropuesto(Tabla5.5)esmenoraladelsistema
actual(Tabla5.6).EnlaFigura5.3seobservaqueel50,00%deiteracionesqueseencuentranentre
elcuartil1ycuartil3presentanmásdispersiónenlosdatosregistradosconelsistemaactualquecon
elframeworkpropuesto,siendomenoreslosvaloresdeduracióndelasolicitudpromedio(ms)de
estaúltima.
52

Diagrama de cajas y bigotes de la duración de solicitud promedio (ms) de pruebas de
Figura5.3.
estrésalsistemaactualyalframeworkpropuesto
53

Tabla5.6
Distribucióndefrecuenciasdeladuracióndesolicitudpromedio(ms)depruebasdeestrésalframeworkpropuesto
| DURACIÓNDE | NÚMERODE | NÚMERODE |     | PORCENTAJE |
| ---------- | -------- | -------- | --- | ---------- |
PORCENTAJE
| SOLICITUD |             | ITERACIONES |     |           |
| --------- | ----------- | ----------- | --- | --------- |
|           | ITERACIONES |             |     | ACUMULADO |
(%)
| PROMEDIO  |          | ACUMULADO |        |        |
| --------- | -------- | --------- | ------ | ------ |
|           | (/200VU) |           |        | (%)    |
| (ms)      |          | (/200VU)  |        |        |
| 4059-4090 | 8        | 8         | 20,00  | 20,00  |
| 4091-4122 | 6        | 14        | 15,50  | 35,00  |
| 4123-4154 | 11       | 25        | 27,50  | 62,50  |
| 4155-4186 | 6        | 31        | 15,00  | 77,50  |
| 4187-4218 | 7        | 38        | 17,50  | 95,00  |
| 4219-4250 | 2        | 40        | 5,00   | 100,00 |
| TOTAL     | 40       |           | 100,00 |        |
VU:virtualusergeneradoporK6
PruebaconUsuarios
Paralaspruebasconusuarios,seconstruyóunainterfazsencillaquecumplaconlafuncionalidad
deinvocarlafuncióndelbackendusadaenlaspruebasanterioresyqueadicionalmenteregistreen
pantallaeltiempototaldeladuracióndelasolicitud,demaneraqueestaseaaccesiblealosusuarios
ypuedaserrecopiladademanerarápidaysencilla.
Estapruebasellevóacabocon77estudiantesdemedicina,quienesestandodesdesuscasasrealizaron
lasolicitudcorrespondienteyluegoregistraronlosvaloresdeduraciónquesemostrabanenpantalla.
EnlaTabla5.7seobservaqueel94,81%deusuariosregistraronunaduracióndesolicitudentre367
msy2474ms.Enestadistribuciónlaamplituddeintervaloesde1054ms.EnlaTabla5.8seobserva
que el 94,81% de usuarios registraron una duración de solicitud entre 213 ms y 1436 ms. En esta
distribuciónlaamplituddeintervaloesde306ms.Estosvaloressoninferioresalospresentadosen
laTabla5.7.
EnlaFigura5.4seobservaqueel50,00%deiteracionesqueseencuentranentreelcuartil1ycuartil
3presentanmásdispersiónenlosdatosregistradosconelsistemaactualqueconelframeworkpro-
puesto,siendomenoreslosvaloresdeduracióndelasolicitud(ms)deestaúltima.
54

Tabla5.7
Distribucióndefrecuenciasdeladuracióndesolicitud(ms)depruebaconusuariosalsistemaactual
DURACIÓN
|           | NÚMERODE      |     | NÚMERODE      |     | PORCENTAJE |     | PORCENTAJE |     |
| --------- | ------------- | --- | ------------- | --- | ---------- | --- | ---------- | --- |
| DE        |               |     | PARTICIPANTES |     |            |     | ACUMULADO  |     |
|           | PARTICIPANTES |     |               |     |            | (%) |            |     |
| SOLICITUD |               |     | ACUMULADO     |     |            |     |            | (%) |
(ms)
| 367-1420  |     | 64  |     | 64  |     | 83,12  |     | 83,12  |
| --------- | --- | --- | --- | --- | --- | ------ | --- | ------ |
| 1421-2474 |     | 9   |     | 73  |     | 11,69  |     | 94,81  |
| 2475-3528 |     | 1   |     | 74  |     | 1,30   |     | 96,11  |
| 3529-4582 |     | 2   |     | 76  |     | 2,60   |     | 98,70  |
| 4583-5636 |     | 0   |     | 76  |     | 0,00   |     | 98,70  |
| 5637-6690 |     | 0   |     | 76  |     | 0,00   |     | 98,70  |
| 6691-7744 |     | 1   |     | 77  |     | 1,30   |     | 100,00 |
| TOTAL     |     | 77  |     |     |     | 100,00 |     |        |
Tabla5.8
Distribucióndefrecuenciasdeladuracióndesolicitud(ms)depruebaconusuariosalframeworkpropuesto
DURACIÓN
|     |          |     | NÚMERODE |     |            |     | PORCENTAJE |     |
| --- | -------- | --- | -------- | --- | ---------- | --- | ---------- | --- |
|     | NÚMERODE |     |          |     | PORCENTAJE |     |            |     |
DE
|     | PARTICIPANTES |     | PARTICIPANTES |     |     | (%) | ACUMULADO |     |
| --- | ------------- | --- | ------------- | --- | --- | --- | --------- | --- |
SOLICITUD
|     |     |     | ACUMULADO |     |     |     |     | (%) |
| --- | --- | --- | --------- | --- | --- | --- | --- | --- |
(ms)
| 213-518   |     | 32  |     | 32  |     | 41,56  |     | 41,56  |
| --------- | --- | --- | --- | --- | --- | ------ | --- | ------ |
| 519-824   |     | 28  |     | 60  |     | 36,36  |     | 77,92  |
| 825-1130  |     | 5   |     | 65  |     | 6,49   |     | 84,42  |
| 1131-1436 |     | 8   |     | 73  |     | 10,39  |     | 94,81  |
| 1437-1742 |     | 2   |     | 75  |     | 2,60   |     | 97,40  |
| 1743-2048 |     | 0   |     | 75  |     | 0,00   |     | 97,40  |
| 2049-2354 |     | 2   |     | 77  |     | 2,60   |     | 100,00 |
| TOTAL     |     | 77  |     |     |     | 100,00 |     |        |
55

Cabedestacarqueconelsistemaactualsepresentanmayornúmeroderegistrosatípicos,observando
unoextremoquecorrespondea7744ms.Enelcasodelframeworkpropuestosolosepresentaron
03casos.
Diagrama de cajas y bigotes de la duración de solicitud (ms) de prueba de usuarios al
Figura5.4.
sistemaactualyalframeworkpropuesto
ComparacióndeResultadosdelasPruebas
EnlaTabla5.9seobservaquelosvaloresdelosdiferentesestadísticossonmayoresenelsistema
actualqueconelframeworkpropuesto,tantoenlaspruebasdeestréscomoenladeusuarios.Elco-
eficientedeasimetríaentodosloscasosesmayorquecero,locualindicaquelosregistrosrealizados
graficanunadistribuciónasimétricaconpresenciadevaloresextremoshacialaderecha.
56

ConlapruebadeKolmogorov-Smirnovseencontróquelosdatosnoseajustanaunadistribución
normal(p<0,05),exceptoenlapruebadeestrésalframeworkpropuesto(p>0,05).
LapruebadecontrastedehipótesisdeUMann-Whitneyestablecequeenambaspruebasexistedife-
renciasignificativa(p<0,05)deladuracióndelasolicitud(ms)entreelsistemaactualyelframework
propuesto,encontrandoenestaúltimatecnologíamenoresvalores.
Tabla5.9
Análisisestadísticodelaspruebasdeestrésydeusuariosrealizadasalsistemaactualyalframeworkpropuesto
|     |     | K6  |     |     | USUARIOS |     |
| --- | --- | --- | --- | --- | -------- | --- |
ESTADÍSTICOS
|         | Sistema   |     | Framework | Sistema  |     | Framework |
| ------- | --------- | --- | --------- | -------- | --- | --------- |
|         | actual    |     | Propuesto | Actual   |     | Propuesto |
| n       | 40        |     | 40        | 77       |     | 77        |
| Me(RIC) | 7000(225) |     | 4140(70)  | 633(483) |     | 577(349)  |
| Vmín    | 6790      |     | 4060      | 369      |     | 215       |
| Vmáx    | 7310      |     | 4250      | 7744     |     | 2354      |
| R       | 520       |     | 190       | 7375     |     | 2139      |
| As      | 0,39      |     | 0,11      | 4,49     |     | 2,01      |
Pruebade
|     | p=0,014 |     | p=0,200 | p=0,000 |     | p=0,000 |
| --- | ------- | --- | ------- | ------- | --- | ------- |
Kolmogorov-Smirnov
| p-crítico |     | 0,050 |     |     | 0,050 |     |
| --------- | --- | ----- | --- | --- | ----- | --- |
| p-valor   |     | 0,000 |     |     | 0,023 |     |
SignificanciaUde
|     |     | p<0,05 |     |     | p<0,05 |     |
| --- | --- | ------ | --- | --- | ------ | --- |
Mann-Whitney
n:númerodedatos
Me(RIC):Mediana(RangoIntercuartílico)
Vmín:valormínimo
Vmáx:valormáximo
R:Rango
As:coeficientedeasimetría
57

6
Discusión
Conelpresentetrabajodesarrolladosevalidólapropuestade(Gerasimouycol.,2018;Knoche
&Hasselbring,2018;Somogyi&Kovesdan,2021),quienesindicanquelatareaderefactorización
desoftwareesunprocesoquepuedeconsumirbastantetiempodependiendodelacomplejidaddel
caso.Peroalevaluaryobtenerlasfuncionescríticasdelsistemasepuedefacilitaresteproceso,loque
enelpresentetrabajosevioreflejadoalelaborarlainterfazdeserviciosdelsistema.
Porotrolado,lametodologíapropuestaparaeldesarrollodelarefactorizacióndelsoftwarefueefec-
tivaeneldesarrollodelproyectoyalestaralineadaconelestadodelarte,comoconlapropuestade
(Wolfartycol.,2021),sepuedeafirmarqueesunametodologíavalida.
Tambiénesimportantemencionarquelamantenibilidaddeunsistemaconstruidoconmicroservi-
ciosessuperior,ademásdepresentarventajasenlaflexibilidaddeestos,deacuerdoaloindicadopor
(Khazaeiycol.,2020;Knoche&Hasselbring,2018).Todoestofueindicadoporlostrabajadoresde
la Unidad de Implementación del ERP durante las entrevistas que se tuvieron; las que estuvieron
alineadasconeltrabajorealizadopor(DiFrancescoycol.,2018),yseencontróunflujodetrabajo
similaralquefuedesarrolladoenelcasodeestudiollevadoacabopor(Balalaieycol.,2018).
Finalmente,setieneelaspectodeltesting,quesegúnlomencionadopor(Pietrantuonoycol.,2020)
esunodelosaspectosquemuchasvecessepasaporalto.Enelpresentetrabajotambiénseviolaim-
portanciaderealizarpruebas,yseaplicaronalgunasdelasrecomendadaspor(Pietrantuonoycol.,
2020),obteniendolosresultadosesperados.
58

Conclusiones
PRIMERO.Selogródesarrollarunframeworkutilizandotecnologíasyarquitecturasmodernas
pararealizarelupgradedelsistemaERPdelaUniversidadCatólicadeSantaMaría,llegandoaobte-
nerunaarquitectura,asícomotambiénunaplantillaparaqueestaseareplicada.
SEGUNDO.Seanalizólastendenciasactualesenelmercado,dondesedeterminóqueReactJSes
la mejor librería para el desarrollo de las interfaces, debido a que es la más utilizada actualmente y
cuentaconunagrancomunidaddeusuariosquecontribuyenenlasolucióndeerroresycreaciónde
plantillasyotraslibrerías.
TERCERO.Sedefinióquelaarquitecturaautilizarparaeldesarrollodelsistemaesunaarquitectura
basadaenmicroserviciosdebidoalosbeneficiosqueofreceencuantoalamantenibilidadyescala-
bilidad del sistema. Además, se realizó la refactorización del módulo gestión de notas de crédito y
costopromediodelaboticaAliviari,yserealizólavalidacióncorrespondiente;obteniendoquesu
desempeñoeselesperadoyquesuusoessencillo.
CUARTO.Elusodeunframeworkconunaarquitecturabasadaenmicroserviciosutilizandotec-
nologíasmodernasmejoralaproductividaddelosdesarrolladores.Estoseveevidenciadoaltenerun
árboldearchivosconunamenorcomplejidad,ademásdepresentarunamejormaneradeorganizar
elcódigofuentedelsistema.
QUINTO. El uso de Go y ReactJS bajo el framework propuesto es una mejor alternativa para el
desarrollodelsistemaERP.Sedeterminóqueelusodelframeworkpropuestoreduceeltiempode
duraciónpromediodelasolicitudhttp.Enunentornodeproducciónseobtuvoqueel65%deite-
racionesdepruebaalsistemaenPHPseencuentraentre6789msy7049ms;mientrasquealsistema
desarrolladoenelcasodeestudiopresentaenel62.50%deiteracionesunpromedioentre4059ms
59

y4154ms.EstodebidoqueGoesunlenguajecompilado,mientasquePHPesunlenguajeinterpre-
tado.
SEXTO.Aloanteriormencionadosesumalosresultadosdelapruebaconusuarios,dondeapesar
detenerunavariablefueradenuestrocontrolcomoeslavelocidaddeinternetdecadausuario,el
frameworkpropuestopresentamejorestiempospromediodesolicitudes,estandoestosentre213ms
y2354ms,acomparacióndelsistemaactual,conelquesealcanzaronvaloresentre367y7744ms.
SÉPTIMO.Tomandoencuentalavalidacióncualitativa,seconcluyequeelframeworkpresentado
mejoralaproductividaddelosdesarrolladores,brindándolesfacilidadestantoenelmomentodede-
sarrollocomoalmomentodedarlemantenimientoalsistema.Estoatravésdeunaseparacióndelos
módulosdelERPdentrodesusrespectivosproyectos,yteniendounaestructuradelrepositoriode
códigofuentemásorganizadayfácildegestionar.
60

Recomendaciones
Primero:UtilizarlaarquitecturabasadaenmicroserviciosaplicandoDevOpsparaelciclodede-
sarrollo,implementandoflujosdeautomatizaciónatravésdepipelinesdeCI/CD;demaneraquese
tengaunaentregamásrápidayconfiabledelsoftwaredesarrollado.
Segundo:Realizareldesplieguedelsistemaatravésdecontenedores,dependiendodelcrecimiento
delmismousarorquestadoresdecontenedoresysiesposibleimplementarunservicemeshybalan-
ceadoresdecargaparalosservicios.
Tercero:Usarunentornocloud,iniciandoconlosserviciosyopcionesdelsistemaquerecibenun
mayorflujodeusuarios.Asícomotambién,unamigracióndelasbasesdedatosaestaarquitectura
cloud.
61

Estándares
ISO/IEC25000:
EstándarconocidocomoSQuaRE(SystemandSoftwareQualityRequirementsandEvalua-
tion), que tiene como objetivo definir un framework para la evaluación de la calidad de un
productosoftware.Sedivideen5subestándares,cadaunoorientadoacumplirconlacalidad
endiferentesmomentosdelciclodevidadeldesarrollodesoftware.
ISO/IEC9126:
Estándarquedefinemétricasinternasyexternasparadeterminarlacalidaddeunaaplicación.
Dichas métricas se determinan a partir de una serie de atributos como la funcionalidad, la
confiabilidad,lausabilidad,entreotros.
ISO/IEC9241-11:
Lasección11delestándarsecentraenmedirlaefectividad,eficiencia,ysatisfacciónenelcon-
textodequétantoelusuariopuedealcanzarlosobjetivosparacualessedesarrollólaaplicación,
asícomotambiénelcambioenelniveldeusabilidadalolargodeltiempo.
ISO/IEC12207:
Estableceunframeworkparalosprocesosdelciclodevidadeldesarrollodesoftware,estable-
ciendounaterminologíacomún,asícomofases,tareas,yrolesquesellevanacabo.
62

Glosario
CLI:Siglasde“Command-lineinterface”,esunprogramaqueaceptatextocomoentradadel
usuarioyloprocesaparaaccederoinvocarfuncionalidadesdelsistemaodeunaherramienta.
Go:Esunlenguajedeprogramaciónconcurrenteycompilado,conunsistemadetipadoes-
tático.EssintácticamentesimilarlafamiliadelenguajesC,perobuscasertandinámicocomo
Python.
PHP:Esunlenguajedeprogramacióndepropósitogeneralqueestáorientadoaldesarrollo
web.Fuecreadoen1994conelobjetivodedarmayorfuncionalidadalaspáginasweb.
ReactJS:EsunalibreríadeJavaScriptparalaconstruccióndeinterfacesdeusuario.Esactual-
metneelframeworkpreferidoporlosdesarolladoresalrededordelmundosegúnlaencuesta
deStackOverflow.
TdeStudent:Pruebaestadísitcaquesirveparadeterminarsiexisteunadiferenciasignificativa
entrelasmedidasdedosgruposquepresentandistribuciónnormal.
U de Mann-Whitney: Prueba estadísitca que sirve para determinar si existe una diferencia
significativaentrelasmedidasdedosgruposquepresentanunadistribuciónnoparamétrica.
ShapiroWilk:Esunapruebadenormalidad,enlaquesedeterminasilosdatosquesetiene
deunapoblaciónomuestrapresentandistribuciónnormal.
63

Referencias
Al-Debagy,O.&Martinek,P.(2020).ExtractingMicroservices’CandidatesfromMonolithicAp-
| plications: | Interface Analysis | and Evaluation | Metrics Approach. |           |             |
| ----------- | ------------------ | -------------- | ----------------- | --------- | ----------- |
|             |                    |                |                   | SOSE 2020 | - IEEE 15th |
InternationalConferenceofSystemofSystemsEngineering,Proceedings ,289-293.https://
doi.org/10.1109/SOSE50414.2020.9130466
Auth0&Peyrott,S.(s.f.).JSONWebTokenIntroduction-jwt.io.https://jwt.io/introduction
Balalaie,A.,Heydarnoori,A.,Jamshidi,P.,Tamburri,D.A.&Lynn,T.(2018).Microservicesmi-
| grationpatterns. |                                |     | , (11),2019-2042.https://doi.org/10. |     |     |
| ---------------- | ------------------------------ | --- | ------------------------------------ | --- | --- |
|                  | Software-PracticeandExperience |     | 48                                   |     |     |
1002/SPE.2608
Carrasco,A.,VanBladel,B.&Demeyer,S.(2018).Migratingtowardsmicroservices:Migrationand
architecturesmells.
IWoR2018-Proceedingsofthe2ndInternationalWorkshoponRefacto-
,1-6.https://doi.org/10.1145/3242163.3242164
ring,co-locatedwithASE2018
Carvalho, L., Garcia, A., Assuncao, W. K., De Mello, R. & Julia De Lima, M. (2019). Analysis of
theCriteriaAdoptedinIndustrytoExtractMicroservices. Proceedings-2019IEEE/ACM
Joint7thInternationalWorkshoponConductingEmpiricalStudiesinIndustryand6thInter-
nationalWorkshoponSoftwareEngineeringResearchandIndustrialPractice,CESSER-IP
,22-29.https://doi.org/10.1109/CESSER-IP.2019.00012
2019
Costa, D. I. C., Filho, E. P. S., Da Silva, R. F., Thiago, T. D. & Cortés, M. I. (2020). Microservi-
| ce architecture: | A tertiary | study.            |            |            | , 61-70. |
| ---------------- | ---------- | ----------------- | ---------- | ---------- | -------- |
|                  |            | ACM International | Conference | Proceeding | Series   |
https://doi.org/10.1145/3425269.3425277
DeIasio,A.&Zimeo,E.(2021).Aframeworkformicroservicessynchronization.
Software-Practice
| andExperience | , 51 (1),25-45.https://doi.org/10.1002/SPE.2877 |     |     |     |     |
| ------------- | ----------------------------------------------- | --- | --- | --- | --- |
64

Di Francesco, P., Lago, P. & Malavolta, I. (2018). Migrating Towards Microservice Architectures:
An Industrial Survey.
Proceedings - 2018 IEEE 15th International Conference on Software
,29-38.https://doi.org/10.1109/ICSA.2018.00012
Architecture,ICSA2018
Engel,T.,Langermeier,M.,Bauer,B.&Hofmann,A.(2018).Evaluationofmicroservicearchitec-
tures:Ametricandtool-basedapproach. ,
LectureNotesinBusinessInformationProcessing
,74-89.https://doi.org/10.1007/978-3-319-92901-9_8
317
Facebook Open Source. (s.f.). React – A JavaScript library for building user interfaces. https://
reactjs.org/
Gan,Y.&Delimitrou,C.(2018).Thearchitecturalimplicationsofcloudmicroservices.
IEEECom-
, (2),155-158.https://doi.org/10.1109/LCA.2018.2839189
puterArchitectureLetters 17
Ganney,P.S.,Pisharody,S.&Claridge,E.(2020).Softwareengineering. ,131-168.
ClinicalEngineering
https://doi.org/10.1016/B978-0-08-102694-6.00009-7
Gerasimou,S.,Kechagia,M.,Kolovos,D.,Paige,R.&Gousios,G.(2018).Onsoftwaremoderni-
sationduetolibraryobsolescence.
Proceedings-InternationalConferenceonSoftwareEngi-
,6-9.https://doi.org/10.1145/3194793.3194798
neering
Google.(s.f.).TheGoProgrammingLanguage.https://go.dev/
Grafana.(2021).Open-sourceloadtestingtoolfordevelopers|k6OSS.https://k6.io/open-source
Heinrich,R.,VanHoorn,A.,Knoche,H.,Li,F.,Lwakatare,L.E.,Pahl,C.,Schulte,S.&Wettin-
ger,J.(2017).Performanceengineeringformicroservices:Researchchallenges&directions.
ICPE2017-Companionofthe2017ACM/SPECInternationalConferenceonPerformance
,223-226.https://doi.org/10.1145/3053600.3053653
Engineering
HernándezSampieri,R.,FernándezCollado,C.&delPilarBaptistaLucio,M.(2010).
Metodología
(5taEd.).McGraw-Hill.
delainvestigación
Hussain,S.M.,Bhatti,S.N.&Rasool,M.F.U.(2017).Legacysystemandwaysofitsevolution.
, 56-59. https://
International Conference on Communication Technologies, ComTech 2017
doi.org/10.1109/COMTECH.2017.8065750
65

Jamshidi,P.,Pahl,C.,Mendonca,N.C.,Lewis,J.&Tilkov,S.(2018).Microservices:Thejourney
so far and challengesahead. , (3), 24-35. https://doi.org/10.1109/MS.
IEEE Software 35
2018.2141039
Jindal,S.&Khurana,G.(2013).Thestatisticalanalysisofsource-codetodeterminetherefactoring
opportunities factor (ROF) using a machine learning algorithm.
IET Conference Publica-
, (645CP),396-403.https://doi.org/10.1049/CP.2013.2244
tions 2013
Jones,M.,Bradley,J.&Sakimura,N.(2015).JSONWebToken(JWT).https://doi.org/10.17487/
RFC7519
JSON.(s.f.).JSON.https://www.json.org/json-en.html
Kargar,M.J.&Hanifizade,A.(2018).Automationofregressiontestinmicroservicearchitecture.
,133-137.https://doi.org/
20184thInternationalConferenceonWebResearch,ICWR2018
10.1109/ICWR.2018.8387249
Kelly,A.(2018).Let’slearnhowmodulebundlersworkandthenwriteoneourselves.https://www.
freecodecamp.org/news/lets-learn-how-module-bundlers-work-and-then-write-one-
ourselves-b2e3fe6c88ae/
Khazaei,H.,Mahmoudi,N.,Barna,C.&Litoiu,M.(2020).PerformanceModelingofMicroservice
Platforms. , 1-1. https://doi.org/10.1109/TCC.
IEEE Transactions on Cloud Computing
2020.3029092
Knoche, H. & Hasselbring, W. (2018). Using Microservices for Legacy Software Modernization.
, (3),44-49.https://doi.org/10.1109/MS.2018.2141035
IEEESoftware 35
Miguel,F.S.,Mareddy,N.,Moorthy,A.K.&Liu,X.(2022).Microservicesformultimedia,89-89.
https://doi.org/10.1145/3510450.3517298
Naik, A., Choudhari, J., Pawar, V. & Shitole, S. (2021). Building an EdTech Platform Using Mi-
croservicesandDocker. .
2021IEEEPuneSectionInternationalConference,PuneCon2021
https://doi.org/10.1109/PUNECON52575.2021.9686535
Oracle.(2021).WhatisERP?https://www.oracle.com/erp/what-is-erp/
66

Pérez-Castillo,R.,DeGuzmán,I.G.R.,Caballero,I.&Piattini,M.(2013).Softwaremodernization
byrecoveringWebservicesfromlegacydatabases. ,
Journalofsoftware:EvolutionandProcess
(5),507-533.https://doi.org/10.1002/SMR.1554
25
Pietrantuono, R., Russo, S. & Guerriero, A. (2020). Testing microservice architectures for opera-
tionalreliability. , (2).https://doi.org/10.
SoftwareTestingVerificationandReliability 30
1002/STVR.1725
RedHat.(2017).WhatisanAPI?https://www.redhat.com/en/topics/api/what-are-application-
programming-interfaces
Ren,Z.,Wang,W.,Wu,G.,Gao,C.,Chen,W.,Wei,J.&Huang,T.(2018).Migratingwebappli-
cationsfrommonolithicstructuretomicroservicesarchitecture.
ACMInternationalCon-
.https://doi.org/10.1145/3275219.3275230
ferenceProceedingSeries
SAP.(s.f.).Informacióndelaempresa|AcercadeSAPSE.https://www.sap.com/latinamerica/
about/company.html
Singhal, P., Kumar, A., Irshad, A. & Gumber, V. (2021). Frontend vs Backend. https://www.
geeksforgeeks.org/frontend-vs-backend/
Somogyi,N.&Kovesdan,G.(2021).SoftwareModernizationUsingMachineLearningTechniques.
SAMI2021-IEEE19thWorldSymposiumonAppliedMachineIntelligenceandInforma-
,361-365.https://doi.org/10.1109/SAMI50585.2021.9378659
tics,Proceedings
Stack Overflow. (2021). Stack Overflow Developer Survey 2021. https://insights.stackoverflow.
com/survey/2021#most-popular-technologies-database-prof
Wolfart,D.,Assunção,W.K.,DaSilva,I.F.,Domingos,D.C.,Schmeing,E.,Villaca,G.L.&Paza,
D.D.N.(2021).Modernizinglegacysystemswithmicroservices:Aroadmap.
ACMInter-
,149-159.https://doi.org/10.1145/3463274.3463334
nationalConferenceProceedingSeries
Yin,K.&Du,Q.(2021).OnRepresentingResilienceRequirementsofMicroserviceArchitecture
Systems. , (6),
InternationalJournalofSoftwareEngineeringandKnowledgeEngineering 31
863-888.https://doi.org/10.1142/S0218194021500261
67

Anexos
A. Cuestionario propuesto
ElcuestionarioseaplicóatravésdeGoogleForms.
Laspreguntascerradasdefinidasson:
1. Elframeworkpresentadopuedemejorarlacalidaddelsoftwarequeusteddesarrolla.
2. Elframeworkpresentadofacilitaríalastareasdemantenimientodesoftware.
3. Elframeworkpresentadoleparecesencillodeaprenderyutilizar.
4. Ustedseadaptaríafácilmenteaunflujodetrabajoutilizandoelframeworkpresentado.
Laspreguntasabiertasdefinidasson:
1. Indique,segúnsuopinión,¿Quéaspectosmejoraríadelframeworkpresentado?
2. Indiquesuopiniónsobreelframeworkpresentado,considerandoquéimpactopuedetener
sobresuproductividad.
Lasrespuestasquefueronregistradassepuedenverenelsiguienteenlace:VerRespuestas.
68

| B. Costos | de mantenimiento |     |     |     |
| --------- | ---------------- | --- | --- | --- |
Cálculodeloscostosdemantenimientomensualestomandoencuentaúnicamenteundesarro-
llador.
|            | Elemento             |                      | Monto(S/) |           |
| ---------- | -------------------- | -------------------- | --------- | --------- |
|            | Sueldopromedio       |                      | 1300      |           |
|            | Elemento             | Valorpromedio(horas) |           | Monto(S/) |
|            | Tiempoideal          |                      | 46        | 373.75    |
|            | Tiemporeal           |                      | 80        | 650       |
| C. Cálculo | de la revalorización | del                  | sistema   |           |
Cálculodelarevalorizacióndelsistemaenfuncióndeloscostosdedesarrollodelproyecto.
|     |                     | Elemento | Valor    |     |
| --- | ------------------- | -------- | -------- | --- |
|     | Costostotalespormes |          | S/830    |     |
|     | Duracióndelproyecto |          | 3años    |     |
|     |                     | Total    | S/29,880 |     |
69

D. Carta de validación del jefe del área
VALIDACIÓN DEL TRABAJO DE TESIS
Yo, Ing. Fernando Germán Paredes Marchena, jefe de la Unidad de Implementación del ERP de la
Universidad Católica de Santa María doy conformidad del trabajo llevado a cabo por el egresado
Sebastián Gonzalo Bobadilla Chara durante el desarrollo de su tesis titulada “DESARROLLO DE
UN FRAMEWORK CON UNA ARQUITECTURA BASADA EN MICROSERVICIOS PARA EL
UPGRADE DEL SISTEMA DE PLANIFICACIÓN DE RECURSOS EMPRESARIALES DE LA
UCSM”.
Además, su propuesta se está utilizando actualmente para la implementación de Web Service para la
consulta y pago de deudas de los estudiantes de la universidad con el banco BBVA y la Caja
Arequipa.
Ing. Fernando Germán Paredes Marchena
DNI 29244573
70

| E. Capturas | de las pruebas | realizadas |
| ----------- | -------------- | ---------- |
E.1. CapturadelresultadodelapruebadecargarealizadaconlaCLIdeK6allocalhost
conelsistemadesarrolladoenPHP.
71

E.2. CapturadelresultadodelapruebadecargarealizadaconlaCLIdeK6allocalhost
conelmicroserviciodesarrolladoenGo.
E.3. CapturadeejemplodelapruebadecargaaPHP.
72

E.4. CapturadeejemplodelapruebadecargaaGo.
73

E.5. CapturadeejemplodeunapruebadeestrésrealizadaalservidorenPHP.
74

E.6. CapturadeejemplodeunapruebadeestrésrealizadaalservidorenGo.
75
