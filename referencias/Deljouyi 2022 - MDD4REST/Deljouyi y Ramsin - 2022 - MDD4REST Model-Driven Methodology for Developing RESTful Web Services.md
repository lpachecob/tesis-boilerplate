MDD4REST: Model-Driven Methodology for Developing RESTful
Web Services
Amirhossein Deljouyi and Raman Ramsin a
Department of Computer Engineering, Sharif University of Technology, Tehran, Iran
Keywords: Model-Driven Development, Domain-Driven Design, Web Engineering, REST Architectural Style, Model
Transformation, Automatic Code Generation.
Abstract: Web services based on the REpresentational State Transfer (REST) architectural style have become
increasingly popular in recent years. REST provides several desirable features, such as simplicity and
scalability; however, developing RESTful web services involves repetitive and trivial tasks that can be
avoided through automatic code generation. Model-Driven Development (MDD) can be used to this aim, as
it facilitates the construction of complex applications and can provide automatic code generation through
transformations of models. This paper presents MDD4REST as a model-driven methodology, consisting of a
framework and a process, for developing RESTful web services. MDD4REST takes advantage of Domain-
Driven Design (DDD) to produce a rich domain model for web services. It provides an effective method for
designing RESTful web services using modeling languages, and supports automatic code generation through
transformation of models. In addition, MDD4REST has the capability to support modern web architectures
and patterns, such as Microservice, Event-Driven, and CQRS.
1 INTRODUCTION Truyen, 2006); its potential has therefore been
recognized in designing RESTful web services by
using modeling languages (Zolotas et al., 2017).
Offering software in the form of web services has
On the other hand, Domain-Driven Design
gained immense popularity due to the evolution of
(DDD) is an effective method for producing a rich
cloud architectures. REpresentational State Transfer
domain model for web services by focusing on the
(REST) comprises a set of rules and practices that
problem domain. DDD can take advantage of MDD
provide simple and comprehensible APIs, clear
best practices in order to develop a system based on
representational structures, and scalable services for
models (Evans and Evans, 2004).
use in web services engineering. Due to its simplicity
Web services can address functional or non-
and scalability, the REST architecture has become
functional requirements. Functional requirements can
increasingly popular among web-service developers.
be expressed through visual models or text, based on
Among the architectures used in web service design
which the domain model is formed. Non-functional
(REST, WSDL, SOAP), REST is the most common;
requirements can be addressed by designing
it has significantly changed how systems are
appropriate architectures. Architectural styles and
developed based on web services (Fielding and
patterns, including Microservice, Event-Driven, and
Taylor, 2000; Mulloy, 2013; Ong et al., 2015;
CQRS, help enhance the scalability and performance
Richardson and Ruby, 2008; Rodriguez, 2008).
of web services (Fowler, 2002, 2017; Greg Young,
Model-Driven Development (MDD) is a software
2010; Newman, 2015; Rademacher et al., 2017).
engineering approach in which models are construed
Despite their merits, existing MDD methods for
as primary artifacts of the software development
web services engineering do not adequately cover the
process, from requirements engineering to analysis,
web services development process and fail to produce
design, and implementation. MDD facilitates the
all of its artifacts. Also, they fail to support high-level
construction of complex applications and supports
modeling at an adequately abstract level, and fail to
automatic code generation through transformation of
provide adequate complexity management features.
models (Hailpern and Tarr, 2006; Siegel, 2014;
a https://orcid.org/0000-0003-1996-9906
93
Deljouyi,A.andRamsin,R.
MDD4REST:Model-DrivenMethodologyforDevelopingRESTfulWebServices.
DOI:10.5220/0011006300003119
InProceedingsofthe10thInternationalConferenceonModel-DrivenEngineeringandSoftwareDevelopment(MODELSWARD2022),pages93-104
ISBN:978-989-758-550-0;ISSN:2184-4348
Copyright c 2022bySCITEPRESS–ScienceandTechnologyPublications,Lda.Allrightsreserved
(cid:13)

MODELSWARD2022-10thInternationalConferenceonModel-DrivenEngineeringandSoftwareDevelopment
We propose a model-driven methodology, which Zolotas et al. have proposed a methodology for
we have chosen to call MDD4REST, for developing generating RESTful web services based on software
RESTful web services. Modeling levels and model requirements (Zolotas et al., 2017); in this approach,
transformation rules are precisely defined in informal specifications or use-cases are used for
MDD4REST, and DDD is applied for producing the modeling functional requirements, and behavioral
domain model. MDD4REST has been evaluated by requirements are modeled in activity diagrams or
applying four different categories of criteria in order storyboards. Gonçalves and Azevedo have introduced
to evaluate its different aspects. Furthermore, it has a model-driven approach in which a DSL is proposed
been empirically validated through application to a for developing OpenAPI specifications; this enables
web development project in a software development developers to utilize the first-design approach,
company; this case study has demonstrated the degree focusing on the definition of resources and
of applicability of the proposed methodology, and has relationships (Gonçalves and Azevedo, 2018). Koren
helped identify its strengths and weaknesses. and Klamma have developed a method for creating
The rest of this paper is structured as follows: front-end pages from OpenAPI specifications (Koren
Section 2 provides an outline of the related works; and Klamma, 2018). Hernandez-Mendez et al. have
Section 3 presents an overview of MDD4REST; proposed an MDD method for consumption of
modeling levels and transformation rules are RESTful APIs in single-page applications, which
explained in Section 4; Section 5 presents a process aggregates RESTful APIs through a query service
for applying the MDD4REST framework; Section 6 meta-model (Hernandez-Mendez et al., 2018).
provides the evaluation results; and Section 7 presents Jegadeesan has proposed an approach for
the conclusion and a discussion of the future work. generating web services of various granularities in
which requirements are obtained through DDD
(Jegadeesan, 2009). Kapferer has introduced a DDD-
2 RELATED WORKS driven approach for strategic design of systems and
decomposition of web services (Kapferer, 2020).
Terzić et al. have addressed the challenges of
In order to elicit the target methodology, the different
RESTful web services in a microservice architecture
facets of an MDD methodology for developing
(such as routing, and microservice auto-discovery and
RESTful web services have been studied. In this
registering) (Terzić et al., 2018).
section, existing approaches are briefly reviewed,
along with three high-level frameworks for MDD and
2.2 High-level Process Frameworks for
web engineering.
MDD and Web Engineering
2.1 Existing MDD/DDD Approaches
We have used three high-level process frameworks as
for Developing RESTful Web
bases for developing our proposed methodology;
Services
these frameworks are briefly introduced in this
section.
Valverde and Pastor have produced a methodology by
Babanezhad et al. have proposed a high-level
extending the OO-Method methodology with a basic
process framework consisting of process patterns for
meta-model for generating RESTful web services
developing web-based systems (Babanezhad et al.,
(Valverde and Pastor, 2009). Schreier has introduced
2010). By applying abstraction to existing MDD
meta-models for modeling structural and behavioral
methodologies, Asadi et al. have devised a generic
aspects of RESTful applications (Schreier, 2011).
framework of process patterns for MDD (Asadi et al.,
Haupt et al. have presented a meta-model for REST
2010). Blake has provided a lightweight framework
constraints (Haupt et al., 2014). Ed-Douibi et al. have
for development of web services (Blake, 2006).
proposed a method for developing RESTful web
services by taking advantage of MDD and combining
REST principles with the Eclipse Modeling
3 OVERVIEW OF PROPOSED
Framework (EMF) (Ed-Douibi et al., 2015); EMF
allows the construction of meta-models using the MDD4REST METHODOLOGY
Ecore language (Steinberg et al., 2008). Ed-Douibi et
al. have also addressed various challenges of RESTful As mentioned before, MDD4REST consists of two
web services development, including testing and parts, a modeling framework (shown in Figure 1) and
integration of APIs, through MDD (Ed-Douibi, 2019). a process.
94

MDD4REST:Model-DrivenMethodologyforDevelopingRESTfulWebServices
Computation Independent Model Ontologies
|     |     | CIM DSL      |     |     |     | Static  |              |
| --- | --- | ------------ | --- | --- | --- | ------- | ------------ |
|     |     | MIC :1 leveL |     |     |     |         | Requirements |
Ontology A
S
Linked
|     |     |     |     | Ontology | S   |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- |
Activity
Dynamic
Storming
Ontology A
Model
S
MIP :2 leveL
|     |     |     |  niamoD | Dynamic- |     |     |     |
| --- | --- | --- | ------- | -------- | --- | --- | --- |
ledoM
|     |     |     |     | Security  | Static Model |     |     |
| --- | --- | --- | --- | --------- | ------------ | --- | --- |
Model
S
MSP :3 leveL
 dnekcaB
|     |     | sledoM | Configuration  |       | Service  | Deployment  |     |
| --- | --- | ------ | -------------- | ----- | -------- | ----------- | --- |
|     |     |        |                | Model | Model    | Model       |     |
|     |     |        |                | M     |          |             | M   |
|     |     | S      |                |       | S        |             | A   |
A
Sculptor
|     |     | OAI model    |     |     |                |     | JDL model |
| --- | --- | ------------ | --- | --- | -------------- | --- | --------- |
|     |     | MSP :4 leveL |     |     | Model          |     |           |
|     |     | A            |     |     | A              |     | A         |
|     |     | YAML Files   |     |     | Btdesign Files |     | JDL Files |
stcafitrA :5 leveL
API
|     |     |               |     | Server &    | Test   |          | Front-End |
| --- | --- | ------------- | --- | ----------- | ------ | -------- | --------- |
|     |     | Specification |     | Client APIs |        | Back-End |           |
|     |     | Automatic     |     |             | Legend |          |           |
A
Transformation
|     |     | Semi-Automatic  |     | Transformation | Artifact | Model | Document |
| --- | --- | --------------- | --- | -------------- | -------- | ----- | -------- |
S
Transformation
|     |     | Manual         |     | API | Test Document | Front-End | Primary |
| --- | --- | -------------- | --- | --- | ------------- | --------- | ------- |
|     |     | Transformation | M   |     |               |           |         |

Figure 1: MDD4REST modeling framework.
The modeling framework supports modeling the  Software  Architectures.  The  MDD4REST
target  web  system.  It  consists  of  four  levels  of  framework supports various architectural styles and
abstraction and was defined based on the results of  patterns for complex web applications. The system
the literature review. A fifth level houses the artifacts  generated  through  applying  the  MDD4REST
of the end product (components of the generated  framework will be based on an onion architecture.
system). The framework provides a set of model  Code generators support architectural styles such as
transformations  that  supports  semi-automatic  Microservice and Event-Driven. Also, command and
construction of target models from source models,  query concepts are split from the first level to support
producing  the  detailed  design  of  RESTful  web  more advanced patterns, including CQRS.
| services.  All  | modeling  | levels  | are  | thoroughly  |     |     |     |
| --------------- | --------- | ------- | ---- | ----------- | --- | --- | --- |
described in Section 4. A process was also proposed  Tool Support. Several tools have been developed to
for applying the MDD4REST framework that will be
facilitate using the MDD4REST framework; these
explained in Section 5.  tools are depicted in Figure 2:  1) mdd4rest-annotater,
which is mainly based on BRAT  (Stenetorp et al.,
95

MODELSWARD2022-10thInternationalConferenceonModel-DrivenEngineeringandSoftwareDevelopment
2012), annotates software requirements and generates  structural modeling of a system. mdd4rest-annotator
the static ontology; 2) mdd4rest-activity-storming,  can  annotate  textual  requirements  and  parse
which is based on Eugenia (Kolovos , 2017), provides  annotations into a static ontology (Figure 3).
| a  modeling  | tool  and  meta-model  |     | for  exploring,  |     |     |     |     |     |
| ------------ | ---------------------- | --- | ---------------- | --- | --- | --- | --- | --- |
visualizing, designing, and formalizing the business
| domain;                                             | 3)  mdd4rest-generator,  |             | which  is   | mainly  |     |     |     |     |
| --------------------------------------------------- | ------------------------ | ----------- | ----------- | ------- | --- | --- | --- | --- |
| based  on                                           | the  Eclipse             | Epsilon     | family  of  | model   |     |     |     |     |
| transformation                                      | and                      | management  | languages   |         |     |     |     |     |
| (including ETL, EOL, EML, and EGL), provides a set  |                          |             |             |         |     |     |     |     |
of transformation rules for generating models; 4)  Figure 3: An example of textual requirements specifications
| mdd4rest-cli  | is  a  command-line  |     | interface  | for  | and annotations.  |     |     |     |
| ------------- | -------------------- | --- | ---------- | ---- | ----------------- | --- | --- | --- |
facilitating the use of the mdd4rest-generator; 5)
mdd4rest-metamodels contains a set of EMF meta- 4.1.2  Activity Storming Diagrams
models for the framework's modeling levels. All the
projects  for  MDD4REST,  and  the  case  study’s  For behavioral modeling, we have developed a new
artifacts, are available online (Deljouyi, 2021).  diagram named “Activity Storming” via combining
UML Activity Diagram elements with concepts taken
from Event Storming (Brandolini, 2013). Activity
diagrams provide formalization, and Event Storming
|     |     |     |     |     | covers  DDD  | concepts.  Activity  | Storming  | thus  |
| --- | --- | --- | --- | --- | ------------ | -------------------- | --------- | ----- |
provides both formalization and support of DDD
concepts. In addition, our mdd4rest-activity-storming
tool comes as an Eclipse plugin to explore, visualize,
and design Activity Storming models. The elements
of Activity Storming are shown in Figure 4.

Figure 2: MDD4REST Framework Tools.
4  MDD4REST FRAMEWORK
This section introduces the four modeling levels of
the MDD4REST framework. Examples of the models

produced are presented in Section 6.1 (Case Study).
Figure 4: Elements of Activity Storming.
4.1  Level 1: Computation-Independent
| Model (CIM)  |     |     |     |     | 4.1.3  Ontologies  |     |     |     |
| ------------ | --- | --- | --- | --- | ------------------ | --- | --- | --- |
MDD4REST incorporates three ontologies regarding
At level 1, system requirements are identified and
different views of the system: 1) Static Ontology,
modeled, and the system’s domain model is thus
representing a structural view; 2) Dynamic Ontology,
formed. Two approaches are used at the first level for
representing a dynamic view; 3) Linked Ontology,
domain modeling: textual requirements specifications
combining structural and dynamic views. mdd4rest-
and activity storming models.
generator transforms activity storming models into a
dynamic ontology, and then aggregates the static and
4.1.1  Textual Requirements Specifications
dynamic ontologies to produce a linked ontology.
|     |     |     |     |     | Ultimately,  | mdd4rest-generator  | transforms  | the  |
| --- | --- | --- | --- | --- | ------------ | ------------------- | ----------- | ---- |
Due to the fact that textual specifications of the
|               |                   |           |               |     | linked  ontology  | into  a  YAML-based  |     | Domain- |
| ------------- | ----------------- | --------- | ------------- | --- | ----------------- | -------------------- | --- | ------- |
| requirements  | are  prevalently  | utilized  | in  software  |     |                   |                      |     |         |
Specific Language (DSL).
| development  | projects,  they  | are  | good  sources  | for  |     |     |     |     |
| ------------ | ---------------- | ---- | -------------- | ---- | --- | --- | --- | --- |
96

MDD4REST:Model-DrivenMethodologyforDevelopingRESTfulWebServices
4.2 Level 2: Platform-Independent by applying EGL rules on these models. Code
Model (PIM) generators use these level-4 products to generate the
final artifacts of the target system (residing at level 5).
The focus of level 2 is on the REST architecture and
contains resource-oriented concepts. Two models are
produced at this level: Static and Dynamic-Security
models. At this level, mdd4rest-generator semi-
automatically transforms the YAML-based DSL
produced at level 1 into the models of level 2. Figure
5 shows the architecture of this level. As Static and
Dynamic models have common elements, EOL rules
are developed for synchronizing them.
Figure 6: CQRS Intra-Application view.
Figure 7: Inter-Application architecture view.
Figure 5: PIM’s architecture.
4.3 Level 3: Platform-Specific Model 5 MDD4REST PROCESS
(PSM) of the Architecture
In order to define an MDD methodology, a process
Levels 3 and 4 are both platform-specific. At level 3,
must be defined for applying the modeling
the architecture of the system will be determined;
framework. The process that we propose (shown in
PIM models are merged into a service model, and the
Figure 8) consists of four phases: Start-up,
user can create deployment and configuration models
Construction, Transition, and Maintenance. The
manually. There are two types of architectural views
process is primarily based on the Web Engineering
at the third level: intra-application and inter-
Process Framework of (Babanezhad et al., 2010). The
application. Intra-application represents the
phases are performed serially, but they are broken
architecture of each application, which may be simple
down into stages that are executed iteratively.
or CQRS. Inter-application describes the architecture
The goal of the Start-up phase is to acquire
between the applications, as several microservice
knowledge about the target system and perform the
applications can comprise the system. Figure 6 and
essential activities for initiating the project.
Figure 7 demonstrate intra-application and inter-
The Construction phase is aimed at developing
application views, respectively.
the target system in several iterations, and consists of
three coarse-grained stages: Analysis, Model-Driven
4.4 Level 4: Platform-Specific Model
Development, and Implementation. Construction is
(PSM) for Code Generators where modeling is performed based on the different
levels of the MDD4REST framework. In the Analysis
Level 4 contains models and DSLs for code stage (level 1), the functional and non-functional
generators, namely Jhipster, Sculptor, and OpenAPI. requirements of the system are elicited, estimation
mdd4rest-generator transforms level-3 models into and prioritization are performed, and higher-priority
code generator models, and DSLs are then generated requirements are selected for the iterations.
97

MODELSWARD2022-10thInternationalConferenceonModel-DrivenEngineeringandSoftwareDevelopment
Semi-Automatic  Generation of
|     |     |     |     |     |     | S t a t i c   M o d e l | A r c h i t                                                  | e c t u r a l  | D e s i g n   a n d   C o n t in u o u s ƈ              |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | ------------------------------------------------------------ | -------------- | ------------------------------------------------------- | --- | --- |
|     |     |     |     |     |     |                         | D y n S a t m a t i i c c     M a n o d d   e l s  S t y l e | s  a n d       | I m p l e m o f e   U n I ta t io n  In t e g ra t io n |     |     |
P P l a r n o n c i e n s g s  &     S e m i - A u t o m a t i c   Sy n c h r o n iz a t i o n S P e a l t e t c e t r i n o s n   R e w o r k C o n t i n u o u s   T r a d it io n a l
S e l e c t i o n G e D n y e n r a a m t i o i c n -   o f   D e l i v e r y M a i n te n a n c e
|     | R e q u i | re m e n ts  | T e & x   t A   A u | n t o n m o t a a t t ic i o   n   G A e n u e t | o r a m t i a o t n ic  o   f  Se m i - A u | t o m a t i c  S e c u r i t y   M o d e l |     | G S e e n m e r i a   - t A io u n t o ƈ o m | f ƈC a t o ic d ƈ eƈ Co d G e e s n   b e r y a   C t e o   d e   R e v ie w |                                         |         |
| --- | --------- | ------------ | ------------------- | ------------------------------------------------ | ------------------------------------------- | ------------------------------------------ | --- | -------------------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------- | ------- |
|     | E n g i n | e er in g    | S t a G t e i c n   | e O r n a t t o io l o n g y   O L n i           | t n o k l e o d g y   G e Y n A e M r a     | L t   i D o S n L   o f                    |     | G e n e r a t o r s                          | ƈ D S L s G e n e r a t o r s                                                |                                         |         |
|     |           |              |                     |                                                  |                                             |                                            |     |                                              |                                                                              | Te s t  i n   t he  D e p l o y m e n t | W e b   |
C h a r t e r in g A u t o m a t ic   S e m i  - A u t o m a t i c ƈ l a r g e M a i n te n a nce
|     |     | It e r a ti o n   D | o m a i n   Ge n e   | r a t i o n   o f       |     | S G e m en i- e A r u a t t i o o m n   a o t f i   c  | S G e m e n i - e A r u at t i o o m n   a o t f i   c  G e n e r a | t i o n ƈ o f ƈ                                             | C B a o c m k p - e le n t d e     Tes s t m  in al  t l he  |     |     |
| --- | --- | ------------------- | -------------------- | ----------------------- | --- | ------------------------------------------------------ | ------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ | --- | --- |
|     |     | P l a n n i n g M o | d e li n g O D n y t | n o a l m o g i c y     |     | D e v m e l o o d p e m l e n t                        | S e r v i c e   M o d e l C o n M f i g o u d                       | r e a l t i o n ƈ G e A n u e to ra m t i a o t n i c ƈ o ƈ | fƈ Imp l e m e n t a t ion                                   |     |     |
|     |     |                     |                      |                         |     |                                                        |                                                                     | G e n e r a t o r s ƈ                                       |                                                              |     |     |
|     |     |                     |                      |                         |     |                                                        | A r c h i t e                                                       | c t u r a lƈ Models                                         |                                                              |     |     |
|     |     |                     |                      |                         |     | S C p o l i m t t i b n i g n   i a n n g d            | S P y S n M ch   M r o o n d iz e a ls t   i a n P d a ƈ t D t e e  | r s n i g s ƈ n ƈ                                           |                                                              |     |     |
|     |     |                     |                      |                         |     | A p p l i c a t i o n s                                | o n S e l e c                                                       | t i o n                                                     |                                                              |     |     |
|     |     |                     |                      |                         |     | O n t o l o g y   Man a g em e                         | n t                                                                 |                                                             |                                                              |     |     |
|     |     |                     |                      |                         |     | B a s e d                                              | O p t io n al                                                       | Stage                                                       |                                                              |     |     |
|     |     |                     |                      |                         |     | Mo d e l - D r iv e n T e ch ni c                      | a l S t a g e                                                       |                                                             |                                                              |     |     |
Figure 8: MDD4REST process.
In  the  Model-Driven  Development  stage,  software solutions for medium to large businesses.
activities  related  to  levels  2  to  4,  including  the  MDD4REST was used to develop a virtual gift card
transformations,  are  performed.  In  the  generator  system.  A  technical  manager  of  the
Implementation  stage,  code  is  generated  by  code  company was actively involved in the study, both as
generators,  and  is  then  completed  by  developers  product owner and user. The first author was involved
(level 5).   in the project and carried out the activities prescribed
The Transition phase is focused on deploying the  by MDD4REST in collaboration with the technical
developed system into the user environment. The  manager. The development took about 30 working
Maintenance  phase  focuses  on  maintenance  and  days,  and  all  the products  were  delivered  to  the
|          |              |     |           |             |     |            | technical  | manager  | to  acquire  | his  feedback  | and  |
| -------- | ------------ | --- | --------- | ----------- | --- | ---------- | ---------- | -------- | ------------ | -------------- | ---- |
| support  | activities.  |     | Umbrella  | activities  |     | are  also  |            |          |              |                |      |
considered in this process, shown on the arrow at the  confirmation. A questionnaire was designed to collect
bottom of Figure 8.    the final feedback from the technical manager.
Two types of roles are involved in this process:
6.1.1  Definition
mandatory and optional. The mandatory roles are:
| user,  | product  | owner,  | coach,  | domain  |     | expert,  and  |     |     |     |     |     |
| ------ | -------- | ------- | ------- | ------- | --- | ------------- | --- | --- | --- | --- | --- |
developer. The optional roles are: architecture owner,  The virtual gift card generator system provides the
following services: 1) browsing gift card designs and
| tester,  | modeler,  | user  | interface  |     | designer,  | and  |     |     |     |     |     |
| -------- | --------- | ----- | ---------- | --- | ---------- | ---- | --- | --- | --- | --- | --- |
categories; 2) buying gift cards; 3) receiving the list
infrastructure expert.
of orders of a customer; 4) setting a second password
for a gift card.
6  EVALUATION
6.1.2  Requirements Engineering
| To  | assess  | the  applicability  |     | and  | effectiveness  | of  |     |     |     |     |     |
| --- | ------- | ------------------- | --- | ---- | -------------- | --- | --- | --- | --- | --- | --- |
Requirements were elicited and expressed as textual
MDD4REST, a case study was conducted and criteria- specifications and event storming models. An excerpt
based evaluation was applied. The research questions  of the event storming model of the "buying a gift
were as follows: RQ1. How logical and accurate are
card" scenario is depicted in Figure 9.
| the  | modeling  | levels  | and  | model  | transformations?  |     |     |     |     |     |     |
| ---- | --------- | ------- | ---- | ------ | ----------------- | --- | --- | --- | --- | --- | --- |
RQ2. Does MDD4REST facilitate the design and
development of RESTful web services? RQ3. Are the
| concerns  | of  | RESTful  | web  | service  | well  | covered?  |     |     |     |     |     |
| --------- | --- | -------- | ---- | -------- | ----- | --------- | --- | --- | --- | --- | --- |
RQ4. How applicable are the tools in MDD4REST?
6.1  Case Study

The case was a web development project in a software
Figure 9: Scenario for buying a gift card.
development company that specializes in producing
98

MDD4REST:Model-DrivenMethodologyforDevelopingRESTfulWebServices
| 6.1.3  Level 1  |     |     |     |     |     | Semi-automatic Generation of YAML DSL. The  |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
mdd4-rest-generator transformed the linked ontology
Text Annotation and Automatic Generation of  into  a  YAML-based  DSL.  This  DSL  must  be
Static  Ontology.  The  textual  specifications  of  reviewed and evaluated and is considered as the
requirements  were  annotated  using  mdd4rest- system's high-level design.
| annotator;  | an  excerpt  | of  | the  | annotation  result  | is  |                 |     |     |     |     |     |
| ----------- | ------------ | --- | ---- | ------------------- | --- | --------------- | --- | --- | --- | --- | --- |
|             |              |     |      |                     |     | 6.1.4  Level 2  |     |     |     |     |     |
shown in Figure 10. The static ontology (Figure 11)
was later generated by mdd4rest-annotator.
The YAML DSL was given as input to the model-
driven engine of mdd4rest-generator, and the Static
and Dynamic-Security models were generated. The
|     |     |     |     |     |     | attributes  | and  | relationships  | of  | the  domain  | and  |
| --- | --- | --- | --- | --- | --- | ----------- | ---- | -------------- | --- | ------------ | ---- |
aggregation objects are modeled in the Static model,
whereas processes and operations are modeled in the
Dynamic-Security model. In this phase, the generated
resources are completed; the relationships between
resources, operations, and processes are defined. In
addition, policies for accessing the resources and the
  access level of roles are modeled in the Dynamic-
Security model. An excerpt of the generated Static
Figure 10: An excerpt of the annotation of the system.
and Dynamic-Security models is shown in Figure 12.
Domain Modeling and Automatic Generation of
Dynamic Ontology. Problem domain modeling was
performed by designing Activity Storming models.
Event Storming models can be used for producing
Activity Storming models; however, Event Storming
models are optional, and Activity Storming models
| can  be  designed  |     | directly.  | The  | dynamic  ontology  |     |     |     |     |     |     |     |
| ------------------ | --- | ---------- | ---- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
(Figure 11) was later generated.
| Automatic           | Generation  |         | of           | Linked  Ontology.  |         |     |     |     |     |     |     |
| ------------------- | ----------- | ------- | ------------ | ------------------ | ------- | --- | --- | --- | --- | --- | --- |
| After  creating     | the static  |         | and dynamic  | ontologies,        |         |     |     |     |     |     |     |
| mdd4rest-generator  |             | merged  | them         | into  the          | linked  |     |     |     |     |     |     |
ontology. Figure 11 shows the mapping of static and
dynamic ontologies onto the linked ontology. The
| "property"  | attribute  | is  | mapped  | from  the  | static  |     |     |     |     |     |     |
| ----------- | ---------- | --- | ------- | ---------- | ------- | --- | --- | --- | --- | --- | --- |
ontology to the linked ontology in parts 1 and 3, and
the "event" element is mapped from the dynamic
ontology to the linked ontology in parts 2 and 4.

Figure 12: Static and Dynamic-Security models.
|     |     |     |     |     |     | 6.1.5  Level 3  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
At this level, mdd4rest-generator merged the Static
and Dynamic-Security models and transformed them
|     |     |     |     |     |     | into  PSM  | models  | (Service,  | Configuration,  |     | and  |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ---------- | --------------- | --- | ---- |
Deployment). In order to generate a system with the
|     |     |     |     |     |     | CQRS      | architecture,  | three  | modules,    |            | namely  |
| --- | --- | --- | --- | --- | --- | --------- | -------------- | ------ | ----------- | ---------- | ------- |
|     |     |     |     |     |     | command,  | query,         | and    | web,  were  | generated  | as      |
constituents of the Service model (partially shown in

|     |     |     |     |     |     | Figure  | 13).  Consequently,  |     | the  | domain  | objects,  |
| --- | --- | --- | --- | --- | --- | ------- | -------------------- | --- | ---- | ------- | --------- |
Figure 11: Static, Dynamic, and Linked ontologies.
operations, internal/external services, and resources
were completed; the Configuration and Deployment
models were enhanced accordingly.
99

MODELSWARD2022-10thInternationalConferenceonModel-DrivenEngineeringandSoftwareDevelopment
generated back-end code was completed. In order to
access the front-end services, a single-page
application was generated by the Jhipster code
generator, which was then improved. Figure 15 shows
the appearance of the gift-card generator system.
Figure 15: Appearance of the single-page application for
Figure 13: Modules in the Service model. the gift-card generator system.
6.1.6 Level 4 6.1.8 Questionnaire-based Interviews
At this level, level-3 models were transformed into The participants involved in the case study were
models specific to each supported code generator, and interviewed using a specially designed questionnaire.
DSLs for each code generator were subsequently The questionnaire was designed to summarize the
generated. These DSLs are reviewed and modified as opinions of the participants, particularly regarding the
necessary. An excerpt of the Sculptor’s DSL is shown research questions; a partial view of the questionnaire
in Figure 14. is shown in Table 1. Furthermore, the advantages and
drawbacks of MDD4REST were discussed with the
participants for future improvement.
6.2 Evaluation Criteria
We developed a set of evaluation criteria to assess
MDD4REST in a systematic manner, particularly
regarding the research questions. There are four
groups of criteria: general criteria, model-driven
criteria, model-driven web engineering criteria, and
RESTful web services criteria. As some groups are
quite populous (containing more than 20 criteria),
showing the whole sets of results is not possible in
this paper. However, excerpts of the criteria and
evaluation results are shown in Tables 2 to 5.
6.3 Analysis of Results
The analysis results are presented in the order of the
research questions:
Answering RQ1- Adequacy of MDD4REST from
Figure 14: The DSL of the Sculptor Code generator.
an MDD perspective: the evaluation results shown in
Tables 3 and 5 indicate that modeling levels are
6.1.7 Implementation
defined accurately and distinguishably. However,
support for round-trip engineering is low.
At this stage, the code was generated by the three
Answering RQ2- Usability of MDD4REST: the
code generators, and the body of functions of the
case study demonstrated that MDD4REST improves
100

MDD4REST:Model-DrivenMethodologyforDevelopingRESTfulWebServices
quality  and  comprehensibility  in  design  and  In contrast, the MDD4REST modeling framework
modeling.  As  a  result  of  these  features  and  the  supports modeling at all levels, including CIM, PIM,
| automation provided, the web services development  |     |     | and PSM.  |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
process is significantly easier to use in comparison  Rich  domain  model-  Existing  methods  cover
with common approaches; this was confirmed by the  CRUD operations only, whereas MDD4REST is not
results of the questionnaire-based interviews.  limited to CRUD operations. A rich domain model is
Answering  RQ3-  Addressing  the  concerns  of  produced in MDD4REST based on DDD concepts.
RESTful  web  services  development:  the  results  Generating the artifacts necessary for RESTful
obtained from criteria-based evaluation (Table 4) and  web services- Existing methods do not create all the
questionnaire-based interviews indicate that there is  products needed for web services development based
an  adequate  level  of  coverage.  The  primary  on the REST architecture. In contrast, MDD4REST
deficiency  is  the  maintenance  of  the  generated  generates code, API specifications, and tests.
systems. This issue will be tackled by supporting  Supporting  common  architectures-  Existing
round-trip engineering in future work.  approaches do not address the architectures common
Answering RQ4- Applicability of MDD4REST  in modern web systems, such as microservices and
tools:  the  results  obtained  from  criteria-based  event-driven.  In  contrast,  MDD4REST  covers
evaluation (Tables 3 and 4) and questionnaire-based  prevalent architectural styles and patterns.
interviews indicate that the tool support is adequate,
and provides convenient employment of MDD4REST
at  all  levels.  In  fact,  tool  support  is  one  of  the  7  CONCLUSIONS
strengths of MDD4REST.
The MDD4REST methodology was developed as a
6.4  Comparative Analysis
|     |     |     | comprehensive  |     | model-driven  |      | methodology  |     | for     |
| --- | --- | --- | -------------- | --- | ------------- | ---- | ------------ | --- | ------- |
|     |     |     | developing     |     | RESTful       | web  | services.    |     | It  is  |
MDD4REST has overcome many of the shortcomings
|     |     |     | comprehensive  |     | in  that  | it  | provides  | a  multilevel  |     |
| --- | --- | --- | -------------- | --- | --------- | --- | --------- | -------------- | --- |
of previous methods. Here are a few issues that have  modeling  framework  along  with  a  process  for
been addressed:
|     |     |     | applying  |     | it.  Transformation  |     | rules  | have  | been  |
| --- | --- | --- | --------- | --- | -------------------- | --- | ------ | ----- | ----- |
Coverage of web services development lifecycle-
|           |                           |               | implemented  |     | to  generate  |     | the  models  | so  | that  the  |
| --------- | ------------------------- | ------------- | ------------ | --- | ------------- | --- | ------------ | --- | ---------- |
| Previous  | methods  for  generating  | RESTful  web  |              |     |               |     |              |     |            |
transitions between modeling levels are smooth and
services either do not provide full coverage of the web
trouble-free. Furthermore, we have developed several
services development lifecycle, or fail to define a
tools to support MDD4REST. For future work, we
development process at all. In contrast, MDD4REST
plan to support other diagrams for domain modeling,
incorporates a detailed process that covers the entire
improve the textual annotation process by using NLP
lifecycle, from analysis to maintenance.
|     |     |     | methods,  |     | cover  strategic  |     | concepts  | of  DDD,  | and  |
| --- | --- | --- | --------- | --- | ----------------- | --- | --------- | --------- | ---- |
Coverage of MDD abstraction levels- Existing
support reverse-engineering from DSLs to models.
| methods  lack  | sufficient  modeling  | and  abstraction  |     |     |     |     |     |     |     |
| -------------- | --------------------- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
levels, and only a few of them support the CIM Level.
Table 1: Part of the designed questionnaire.
|                                                      |                                     |     |     | Strongly  |        |          |           | Strongly  |     |
| ---------------------------------------------------- | ----------------------------------- | --- | --- | --------- | ------ | -------- | --------- | --------- | --- |
|                                                      | General evaluation of the approach  |     |     |           | Agree  | Neutral  | Disagree  |           |     |
|                                                      |                                     |     |     | Agree     |        |          |           | Disagree  |     |
| 1  The approach can be used easily in organizations. |                                     |     |     |           |        |          |           |           |     |
| 2  Others can extend the approach.                   |                                     |     |     |           |        |          |           |           |     |
The approach can improve the quality of code and decrease errors
| 3   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in web services.
| 4  Technical people are enthusiastic about this approach. |     |     |     |           |     |     |     |           |     |
| --------------------------------------------------------- | --- | --- | --- | --------- | --- | --- | --- | --------- | --- |
|                                                           |     |     |     | Strongly  |     |     |     | Strongly  |     |
Technical evaluation of the approach  Agree  Neutral  Disagree
|     |     |     |     | Agree |     |     |     | Disagree |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | -------- | --- |
1  The approach helps developers and designerssignificantly.
| 2  The approach designs web services adequately.  |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3  The approach deploys the systems efficiently and automatically.
| 4  The approach can maintain the systems efficiently.          |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| The developed tools are able to improve the automation of the  |     |     |     |     |     |     |     |     |     |
| 5                                                              |     |     |     |     |     |     |     |     |     |
transformation and generation of models.
6  Common architectures in web engineering are supported.
101

MODELSWARD2022-10thInternationalConferenceonModel-DrivenEngineeringandSoftwareDevelopment
Table 2: Partial view of the results of assessment based on General methodology evaluation criteria.
Criterion Result Description of possible values
Requirements Engineering A
Analysis A
Lifecycle Design A A: Supported with detailed instructions.
Coverage Implementation A B: Supported with general guidelines.
Test B C: Not Supported.
Deployment B
Maintenance B
Coverage of Project Management B A: Supported with detailed instructions.
Umbrella Risk Management B B: Supported with general guidelines.
Activities Quality Management A C: Not Supported.
Clarity of Development Process Work-products, actors, and activities are: A: entirely supported and precisely
A
Definition described. B: partially supported or just mentioned. C: weakly supported.
Seamlessness and Smoothness of A: Both provided; B: Only seamlessness provided. C: Only smoothness provided.
A
Transition between Phases D: None provided.
A: The methodology explicitly provides an atmosphere in which the user is actively
Encouragement of Active User
A involved. B: The methodology provides a number of guidelines for involving the
Involvement
user. C: The methodology does not provide any support.
A: The methodology explicitly provides coping mechanisms. B: Some guidelines
Manageability of complexity A
are defined in order to manage complexity. C: This feature is weakly supported.
Process-Centered: The lifecycle phases, stages, and activities are considered, and
Process- other aspects are described as secondary. Product-Centered: Products are taken
Process Definition Type
Centered into consideration, and other aspects are described as secondary. Role-Centered:
roles are taken into consideration, and other aspects are described as secondary.
Table 3: Partial view of the results of assessing support for Model-Driven Development.
Criterion Result Description of possible values
Transparency of modeling The boundary between levels: A: is accurately distinguishable. B: is relatively transparent. C:
A
levels cannot be distinguished.
Classification of the
A A: accurate classification. B: Relative classification. C: lack of classification.
modeling levels' data
Support for abstraction A: abstraction levels and transitions are fully supported. B: All abstraction levels are defined,
A
levels (CIM, PIM, PSM) but transitions between them are not supported. C: some abstraction levels are not supported.
Structural, Behavioral,
A A: All the system’s aspects are modeled. B: some aspects of the system are not modeled.
Functional modeling
Vertical: The source and target models are at different levels of abstraction.
Model Transformation type Both
Horizontal: The source and target models are at the same level of abstraction.
Automation level of
Medium High: Fully-automated. Medium: Semi-automated. Low: Manual.
transformations
A: All parts of the code are automatically generated. B: Most parts of the code are automatically
Automatic code generation B
generated. C: some parts of the code are automatically generated.
A: A complete toolset is provided, or precise guidelines are defined to select alternative tools. B:
Tool support B A complete toolset is not provided, but general guidelines are provided to select alternative
tools. C: No specific tools or guidelines are provided.
Round-trip engineering,
Synchronization of source A: Detailed procedures are specified for the task in the methodology. B: Only general guidelines
B
and target models, are provided for the task. C: The task is not covered by the methodology.
Verification/Validation
102

MDD4REST:Model-DrivenMethodologyforDevelopingRESTfulWebServices
Table 4: Partial view of the results of assessing support for RESTful Web Services.
|     | Criterion   | Result | Status of MDD4REST based on the criterion  |
| --- | ----------- | ------ | ------------------------------------------ |
General Modeling of  RESTful Web Services
|     |     | A   | All aspects of modeling RESTful web services are considered.  |
| --- | --- | --- | ------------------------------------------------------------- |
(Structural, Behavioral, Functional)
RESTful Practices modeling (Resource, REST API  All aspects relating to REST architecture are precisely defined. However,
A
Specification, Query, Third-Party API Integration)  only guidelines are defined for third-party API Integration.
Security  Access Levels to Resources   A  In Dynamic-security and Service models, access levels are defined for
Modeling
Access Levels to Resource Operations  C  resources and roles, but access controls to resource operations are not
|                      |     |     | supported.  |
| -------------------- | --- | --- | ----------- |
| Definition of Roles  |     | A   |             |
Domain-Driven  Tactical Design   A  The bounded context concept is not covered in MDD4REST. However,
Modeling  Strategic Design  B  similar concepts, including application and module, are supported.
|     | Event-Driven  | A   |     |
| --- | ------------- | --- | --- |
Web Engineering  In MDD4REST, the common Web architectures, including event-driven,
Microservice  A  microservices, and layered, are supported. The presentation layer must be
Architectures
|     | Layered  | B   | completed by developers.  |
| --- | -------- | --- | ------------------------- |
Process: CI/CD, First-API Design, Rich Domain
|     |     | A   | All of these activities are precisely defined in the process of MDD4REST.  |
| --- | --- | --- | -------------------------------------------------------------------------- |
Model
Services: Service Integration and Service  The external services layer integrates internal services with third-party
A
Granularity  APIs. The Services are also divided into two layers: internal and external.
Operations: CRUD and Non-CRUD Operations,
REST constraints, Error handling, Pagination,  A  MDD4REST provides guidelines for all of these activities.
Filters
Test: Unit-Test, Integration-Test, API-Test, Test  By default, the code generator will produce unit and API tests, but
B
Case Generation  developers should also produce other types of tests.
| Support for SQL and NoSQL Databases   |     | A   |     |
| ------------------------------------- | --- | --- | --- |
Tools  Support for Query Languages   C  MDD4REST uses popular code generators capable of supporting a wide
  Use of Standard Technologies  A  range of products and programming languages.
| Diversity of Programming Languages  |     | B   |     |
| ----------------------------------- | --- | --- | --- |
Legend- A: Fully Supported; B: Partially supported; C: Not Supported.
Table 5: Partial view of the results of assessing support for Model-Driven Web Engineering.
| Criterion   | Result  | Status of MDD4REST based on the criterion  |     |
| ----------- | ------- | ------------------------------------------ | --- |
Existence of the Models Necessary  Except for the presentation model, all the models necessary for designing web systems are
B
| for Web Development  |     | supported.  |     |
| -------------------- | --- | ----------- | --- |
Data Model   Domain objects representing system data are obtained from the beginning in the form of
A
| (CIM, PIM, PSM)  |     | ontologies and static models.   |     |
| ---------------- | --- | ------------------------------- | --- |
Business Model   Business logic is provided in the form of Activity Storming models at the CIM level. At the
A
(CIM, PIM, PSM)  following levels, this aspect can be seen in the Dynamic-Security and Service models.
Navigation Model   Service navigation has been considered in the modeling levels of MDD4REST. However,
B  presentation navigation has not been addressed, as the presentation aspect is outside the
| (CIM, PIM, PSM)  |     | scope of MDD4REST.  |     |
| ---------------- | --- | ------------------- | --- |
Presentation Model   In MDD4REST, the focus is on generating web services, and addressing the presentation
C
| (CIM, PIM, PSM)  |     | aspect is outside the scope of MDD4REST.  |     |
| ---------------- | --- | ----------------------------------------- | --- |
Legend- A: Fully Supported; B: Partially supported; C: Not Supported.

REFERENCES  Babanezhad, R., Bibalan, Y.M., & Ramsin, R. (2010).
Process patterns for web engineering. In IEEE Annual
Computer Software and Applications Conference, 477–
Asadi, M., Esfahani, N., & Ramsin, R. (2010). Process
486.
| patterns  | for  MDA-based  software  | development.  | In  |
| --------- | ------------------------- | ------------- | --- |
Blake, M. B. (2006). A lightweight software design process
| ACIS  | International  Conference  | on  Software  |     |
| ----- | -------------------------- | ------------- | --- |
for web services workflows. In IEEE International
Engineering Research, Management and Applications,
Conference on Web Services, 411–418.
190–197.
103

MODELSWARD2022-10thInternationalConferenceonModel-DrivenEngineeringandSoftwareDevelopment
Brandolini, A. (2013). Introducing event storming. blog, Ong, S. P. et al. (2015). The Materials Application
Ziobrando’s Lair, 18. Programming Interface (API): A simple, flexible and
Deljouyi, A. (2021). MDD4REST Labs. Retrieved from efficient API for materials data based on
https://github.com/MDD4REST REpresentational State Transfer (REST) principles.
Ed-Douibi, H. (2019). Model-driven round-trip Computational Materials Science, 97, 209–215.
engineering of REST APIs (PhD Thesis, Network and Rademacher, F., Sachweh, S., & Zündorf, A. (2017).
Information Technologies Doctoral Programme, Differences between model-driven development of
Universitat Oberta de Catalunya). service-oriented and microservice architecture. In IEEE
Ed-Douibi, H., Izquierdo, J. L. C., Gómez, A., Tisi, M., & International Conference on Software Architecture
Cabot, J. (2015). EMF-REST: Generation of RESTful Workshops, 38–45.
APIs from Models. In Annual ACM Symposium on Richardson, L., & Ruby, S. (2008). RESTful web services.
Applied Computing, 1446–1453. O’Reilly Media, Inc.
Evans, E. J., & Evans, E. (2004). Domain-driven design: Rodriguez, A. (2008). RESTful web services: The basics,
Tackling complexity in the heart of software. Addison- 33, 18 (Technical Report, IBM DeveloperWorks).
Wesley Professional. Schreier, S. (2011). Modeling RESTful applications. In
Fielding, R. T., & Taylor, R. N. (2000). Architectural styles International Workshop on Restful Design, 15–21.
and the design of network-based software architectures Siegel, J. M. (2014). Model driven architecture (MDA)-
(Vol. 7). (PhD Thesis, University of California, Irvine). MDA Guide rev. 2.0. (Technical Report, Object
Fowler, M. (2002). Patterns of enterprise application Management Group).
architecture. Addison-Wesley Longman Publishing Steinberg, D., Budinsky, F., Merks, E., & Paternostro, M.
Co. (2008). EMF: Eclipse Modeling Framework. Pearson
Fowler, M. (2017). What do you mean by “Event-Driven”? Education.
Retrieved from https://martinfowler.com/articles/2017 Stenetorp, P., Pyysalo, S., Topić, G., Ohta, T., Ananiadou,
01-event-driven.html S., & Tsujii, J. (2012). BRAT: A web-based tool for
Gonçalves, R. C. da C., & Azevedo, I. (2018). RESTful Web NLP-assisted text annotation. In Demonstrations
Services Development With a Model-Driven Session at European Chapter of the Association for
Engineering Approach. (M.S. Thesis, Instituto Superior Computational Linguistics.
de Engenharia do Porto) Terzić, B., Dimitrieski, V., Kordić, S., Milosavljević, G., &
Greg Young. (2010). CQRS Documents by Greg Young. Luković, I. (2018). Development and evaluation of
Hailpern, B., & Tarr, P. (2006). Model-driven MicroBuilder: A Model-Driven tool for the
development: The good, the bad, and the ugly. IBM specification of REST Microservice Software
Systems Journal, 45(3), 451–461. Architectures. Enterprise Information Systems, 12(8–
Haupt, F., Karastoyanova, D., Leymann, F., & Schroth, B. 9), 1034–1057.
(2014). A model-driven approach for REST compliant Truyen, F. (2006). The fast guide to model driven
services. In International Conference on Web Services, architecture. Cephas Consulting Corp.
129–136. Valverde, F., & Pastor, O. (2009). Dealing with REST
Hernandez-Mendez, A., Scholz, N., & Matthes, F. (2018). services in model-driven web engineering methods. V
A Model-driven Approach for Generating RESTful Jornadas Cientifico-Técnicas en Servicios Web y SOA,
Web Services in Single-Page Applications. In 243–250.
International Conference on Model-Driven Zolotas, C., Diamantopoulos, T., Chatzidimitriou, K. C., &
Engineering and Software Development, 480–487. Symeonidis, A. L. (2017). From requirements to source
Jegadeesan, H. (2009). Towards a Model-Driven Approach code: A Model-Driven Engineering approach for
to Support SOA-Based Web-Business Platforms. (Ph.D. RESTful web services. Automated Software
Thesis, BITS Pilani). Engineering, 24(4), 791–838
Kapferer, S. (2020). A Modeling Framework for Strategic
Domain-driven Design and Service Decomposition.
(M.S. Thesis, University of Applied Sciences of
Eastern Switzerland).
Kolovos, D. S., Garcia-Dominguez, A., Rose, L. M., &
Paige, R. F. (2017). Eugenia: Towards disciplined and
automated development of GMF-based graphical
model editors. Software & Systems Modeling, 16(1),
229–255.
Koren, I., & Klamma, R. (2018). The Exploitation of
OpenAPI Documentation for the Generation of Web
Frontends. In Web Conference, 781–787.
Mulloy, B. (2013). Web API design. Academic Press.
Newman, S. (2015). Building microservices: Designing
fine-grained systems. O’Reilly Media, Inc.
104
