Article

XBoot: A RAPID and Instructional Low-Code Generator for
Spring Boot Applications
Basem Y. Alkazemi * and Mohamed K. Nour

 Department of Software Engineering, College of Computing, Umm Al-Qura University,
 Makkah 21955, Saudi Arabia; mknour@uqu.edu.sa
 * Correspondence: bykazemi@uqu.edu.sa

 Abstract
 Developing secure and well-structured web applications using Spring Boot presents a sig-
 nificant challenge, as it requires developers to manage multiple layers, employ framework-
 specific annotations, and ensure authentication, authorization, and compliance with
 architectural standards. These complexities often lead to errors among students and
 novice developers. Although current low-code platforms reduce coding effort, they fre-
 quently compromise clarity, modularity, and maintainability. This paper introduces XBoot,
 a lightweight framework that utilizes a straightforward XML-based domain-specific lan-
 guage (DSL) to automatically generate modular and secure Spring Boot applications. By
 providing concise specifications for entities, services, routes, and user roles, XBoot gener-
 ates database entities, service classes, controllers, user interface templates, and integrated
 security rules. Validation rules are directly enforced from the DSL, and built-in Swag-
 ger documentation facilitates interactive API testing. The evaluation was conducted in
 two phases. Initially, XBoot was validated by generating applications for student–course
 and flight-booking domains, where less than 50 lines of DSL resulted in 950–1350 lines
 of Java and HTML code, complete with security and documentation. Subsequently,
 10 undergraduate students utilized XBoot in practice. All participants successfully gener-
 ated and deployed applications within 2–20 min (average ≈ 7), compared to 45–120 min
 for manual implementation. On a 5-point Likert scale, students rated the reinforcement
 of layered architecture at an average of 4.0. These findings suggest that XBoot effectively
Academic Editor: Luis Javier
 eliminates common structural and security errors, reduces boilerplate complexity through
García Villalba
 concise DSL specifications, and maintains modularity and transparency-limitations often
Received: 13 August 2025
 observed in traditional coding and other low-code platforms.
Revised: 25 September 2025
Accepted: 28 September 2025
Published: 30 September 2025
 Keywords: spring boot; domain-specific language (DSL); code generation; web application
 scaffolding; RBAC; layered architecture; model-driven development; educational tool;
Citation: Alkazemi, B.Y.; Nour, M.K.
XBoot: A RAPID and Instructional
 component-connector architecture
Low-Code Generator for Spring Boot
Applications. Appl. Sci. 2025, 15, 10621.
app151910621 1. Introduction
Copyright: © 2025 by the authors. The development of modern web applications increasingly demands systems that
Licensee MDPI, Basel, Switzerland. are modular, secure, and rapidly deployable. In both enterprise and cloud-native settings,
This article is an open access article
 developers must adhere to layered architectures, enforce fine-grained access control, and
distributed under the terms and
 maintain adaptable codebases as requirements evolve. Meeting these challenges requires
conditions of the Creative Commons
Attribution (CC BY) license
 frameworks that accelerate backend construction without compromising software engineer-
(https://creativecommons.org/ ing principles. Among these, Spring Boot [1] is widely adopted, offering strong support for
licenses/by/4.0/). RESTful APIs, persistence management, modular design, and integrated security.

Appl. Sci. 2025, 15, 10621 https://doi.org/10.3390/app151910621
Appl. Sci. 2025, 15, 10621 2 of 35

 A defining strength of Spring Boot is its annotation-driven configuration. Annotations
 such as @RestController, @Service, @Repository, and @PreAuthorize eliminate boilerplate
 and enable declarative, maintainable design. While experienced developers benefit from
 this abstraction, students and novices often struggle to understand how layers interact,
 how dependency injection operates, and how security is enforced. Misuse of annotations,
 inconsistent routing, and blurred separation of concerns are common pitfalls.
 Instructional experience confirms that even moderately complex applications, such
 as those with two entities, JPA repositories, and multiple controllers with Thymeleaf tem-
 plates, pose challenges for undergraduates. Errors typically arise from misconfigurations,
 controller–view mismatches, or weak architectural separation, highlighting that these are
 framework-specific difficulties rather than general programming issues.
 Effective strategies in this context emphasize learning through complete, working
 examples. Studying full applications helps students see how components integrate, while
 formalizing designs with a domain-specific language (DSL) [2] further strengthens architec-
 tural reasoning. By expressing systems declaratively, learners think in terms of structure
 and behavior rather than low-level details. This promotes clarity, reinforces component
 boundaries, and supports the transition from coding to deliberate, model-driven design.
 The need for accessible backend scaffolding also extends to professional settings,
 particularly for rapid prototyping and early-stage system design. Existing low-code and
 scaffolding tools promise speed but often lack transparency, security modeling, and adher-
 ence to architectural principles, limiting their educational and professional value [3–5].
 To address these gaps, this paper introduces XBoot, a lightweight DSL-based frame-
 work for generating modular and secure Spring Boot applications. Using compact XML
 specifications, developers can define entities, validation rules, roles, routes, and component
 relationships. XBoot generates the full backend stack: JPA entities, services, REST and view
 controllers, Thymeleaf templates, role-based security, and Swagger API documentation. XML
 is chosen for its readability, structure, and wide tool support [6,7]. The role of DSLs in promot-
 ing maintainability and modularity is well established in software engineering literature [8,9].
 This paper makes the following contributions:
 1. Introduces XBoot, a DSL-based framework that generates secure, modular Spring
 Boot applications from high-level XML specifications.
 2. Demonstrates how XBoot improves educational outcomes by enabling learners to
 practice software architecture and Spring Boot development using traceable, fully
 functional prototypes.
 3. Illustrates how XBoot supports rapid prototyping while preserving architectural
 traceability and component clarity.
 4. Defines and implements a declarative security model using DSL constructs to consis-
 tently enforce access control across application routes and services.
 Unlike existing tools, XBoot uniquely combines architectural discipline, integrated
 security, and educational clarity. Every DSL element maps directly to generated code,
 ensuring traceability and aligning with the component-connector architectural style [10],
 which emphasizes modular composition and secure coordination.
 The paper is organized as follows: Section 2 reviews related work. Section 3 describes the XML
 DSL engineering process, and Section 4 outlines XBoot’s architecture. Section 5 presents syntax and
 workflow, Section 6 explains the security model, and Section 7 reports case studies and evaluation.
 Section 8 discusses educational benefits, Section 9 contrasts XBoot with AI tools, Section 10 compares
 it with manual development, Section 11 concludes, and Section 12 summarizes limitations.
Appl. Sci. 2025, 15, 10621 3 of 35

 2. Related Work
 The growing emphasis on modularity, scalability, and secure-by-design principles has
 shaped the evolution of back-end and full-stack application development. Microservice-based
 architecture, promoted by Fowler and Lewis [11] then expanded by Newman [12] and critically
 analyzed by Dragoni et al. [13], enables systems to be composed of independently deployable
 services that align with organizational agility. Likewise, the secure-by-design approach [14]
 emphasizes the embedding of security principles throughout the system lifecycle, from
 modeling to implementation. These shifts have catalyzed the development of a wave of tools
 designed to support backend automation and reduce architectural complexity.
 Numerous tools and frameworks have emerged to accelerate backend and full-stack
 web application development by automating the generation of boilerplate code, data access
 layers, and user interfaces. These tools offer varying levels of abstraction, automation, and
 adherence to architectural principles. To evaluate the suitability of existing tools for secure
 and maintainable backend development, we adopted the following six practical criteria.
 • DSL-Based Modeling: Whether the tool provides a domain-specific language to define
 the application structure declaratively. DSLs offer several benefits, including design-to-
 code traceability, architectural consistency, and modular thinking, which are essential
 in both professional and educational contexts [2,6]
 • View Generation: The extent to which the tool supports the generation of user inter-
 faces (none, partial, or full). This capability facilitates rapid prototyping and prepares
 applications for automated testing using tools such as JMeter [15] and Selenium [16].
 • REST API Support: Whether the tool scaffolds REST endpoints for CRUD operations
 and custom business logic. Robust API generation is essential for building functional
 and integrable web applications [4,17].
 • Security Model Integration: Support for defining and enforcing access control policies,
 such as role-based authorization. Given the prevalence of security concerns in web
 systems, integrated security modeling is a critical aspect of evaluation.
 • Scope: The range of functionality covered, whether the tool supports backend-only
 generation, full-stack development, or basic scaffolding.
 • Complexity: The learning curve, ease of customization, and usability of the tool,
 particularly in instructional environments. Simplicity and clarity are especially valu-
 able for novice learners, whereas excessive complexity may hinder its adoption in
 academic contexts.
 This paper presents a curated selection of tools, evaluated through a combination
 of practical experimentation and literature review. The selection process was guided
 by several criteria, including their popularity in both academic and industrial contexts,
 accessibility for evaluation, and relevance to back-end and full-stack code generation.
 Priority was given to solutions that are widely adopted, frequently cited in related research,
 and representative of well-established low-code development practices. Furthermore, the
 aim was to encompass a range of modeling paradigms, from DSLs to visual scaffolding
 environments. Tools that were not publicly accessible, lacked sufficient documentation,
 or had a narrow functional scope were excluded. Freely available tools were assessed by
 generating an application similar to that presented in the case study. Commercial tools
 without free trials were evaluated based on official documents and published academic or
 industry reviews. The subsequent discussion surveys candidate tools and frameworks that
 exemplify these trends.
 Commercial low-code platforms, such as Mendix [18] offer visual modeling for
 database design, business logic, and user interfaces, and have even been utilized in edu-
 cational settings [19]. However, these platforms obscure backend details, lack DSL-based
 modeling, and are proprietary, which limits their extensibility and transparency. Boo-
 [20] also and
 modeling, facilitates project
 proprietary,
 modeling,
 are andsetup [20] limits
 proprietary,
 which
 modeling,
 are through
 also facilitates
 and [20]
 which
 modeling,
 are
 their also
 project
 wizard-driven limits
 extensibility
 proprietary, and interface,
 setup
 facilitates
 theirare
 which
 and project
 through but
 limits
 extensibility
 proprietary, a
 transparency. itswizard-driven
 etup free
 their which
 and through
 version
 Bootify
 extensibility
 transparency.
 limits interface,
 wizard-driven
 theirand but
 extensibility
 Bootify
 transparency. its free
 interface,
 and version
 Bootifybut
 transparen its fr
 and Commercial
 directory low-code
 structure. Spring base
 platforms,
 Roo design,
 [22]such
 Commercial business
 as
 previously base
 Mendix
 and design,
 [18]
 Commercial
 low-code logic,
 reduced
 directory and
 business
 oﬀer
 platforms, user
 visual
 low-code
 boilerplate
 structure. logic,
 interfaces,
 such
 modeling
 through
 Spring as and
 platforms,
 Mendix
 Roouser
 and
 for[22] have
 interfaces,
 [18]
 data-
 annota- such even
 oﬀer
 as
 previously and
 been
 visual
 Mendix have
 utilized
 modeling
 [18]
 reduced even
 oﬀer infor
 been
 educa-
 visual
 boilerplate data- utilized
 modelin
 throu
 excludes REST rity.
 API Spring that
 generation, exemplify
 Initializrdynamic
 excludes [21] these
 is confined
 views
 REST trends.
 rity.
 such
 excludes
 API Spring
 to asproject
 generation, Thymeleaf,
 REST bootstrapping,
 Initializr
 API
 dynamic [21]
 generation,
 and is
 viewsconfined
 integratedproducing
 such
 dynamic to
 secu-
 as only
 project
 views
 Thymeleaf, build
 bootstrapping,
 a such andasfileThymeleaf,
 integrated producing secu-
 and only
 integr
 [20] also facilitates [20] also
 project facilitates
 setup [20]
 tional also
 through
 project
 settings asetup
 wizard-driven
 facilitates [20]
 [19]. through
 tional project
 also
 However,
 settings wizard-driven
 interface,
 asetup
 facilitates [19].
 these project
 through but
 However,
 platforms aits
 setup
 interface,
 wizard-driven
 free through
 version but a
 itsinterface,
 free version
 wizard-driven but its free
 interface, version but itslackfr
 base design, business
 tion-driven
 rity. Spring scaﬀolding,
 and
 Initializr
 logic,
 directory
 [21] but
 is itandbase
 is user
 now
 Commercial
 structure.
 confined
 rity.
 design,
 outdated,
 Spring
 to
 interfaces,
 Spring
 project
 base
 business
 low-code Roo
 and
 rity.
 Initializr
 and
 reliant
 tion-driven logic,
 esign,
 platforms,
 [22] have
 directory
 bootstrapping,
 Spring
 [21] onis
 business
 and
 even
 AspectJ,
 scaﬀolding,
 previously
 Initializr
 confined
 user
 such
 structure. been
 producing and
 toasinterfaces,
 logic,
 educed
 [21]
 utilized
 more
 but
 Mendix
 Spring
 is
 project itand
 only
 confined
 obscure
 isthese
 in
 and
 usereduca-
 challenging
 now
 [18]
 boilerplate
 aRoobuild
 bootstrapping,oﬀer
 [22]
 to
 havebackend
 platforms
 interfaces,
 outdated,
 project
 file
 evenobscure
 visual
 through
 previously
 details,
 and
 been
 reliant
 modeling
 annota-
 producing
 bootstrapping,
 utilized
 have
 on
 reduced
 lack
 backend
 AspectJ,
 only
 even
 for
 DSL-based
 indetails,
 adata-
 been
 boilerplate
 producing
 build
 educa-
 andfile utilized
 more
 throu
 only c
 excludes REST excludes
 API generation,
 REST excludes
 API
 dynamic
 modeling, views
 REST
 generation, and are API
 excludes
 dynamic
 such generation,
 modeling, as
 proprietary, views
 Thymeleaf,
 REST
 and API
 are such
 dynamic
 which as
 and
 proprietary,
 limitsThymeleaf,
 generation, integrated
 views their dynamic
 such
 which secu-
 as
 and limits
 extensibility views
 integrated
 Thymeleaf, their such
 and as
 secu-
 and
 extensibilityThymeleaf,
 integrated
 transparency. and and
 secu-
 Bootify
 transparenintegr
 tional
 to trace, settings [19].
 diminishing However,
 tion-driven its educational
 base these
 design,
 scaﬀolding, platforms
 settings
 value.
 business
 but tional
 [19].
 OpenXava
 it tonow
 tion-driven
 isand trace,
 logic, and backend
 settings
 However,
 bscure diminishing
 [23]
 outdated, generates
 user [19].
 these
 scaﬀolding,reliant platforms
 However,
 details,
 its
 interfaces, lack
 educational
 enterprise
 on
 but and
 AspectJ,
 it these
 obscure
 DSL-based
 now
 isaRoo platforms
 applica-
 have andvalue.
 evenbackend
 outdated,
 more OpenXava
 been details,
 obscure
 utilized
 challenging
 reliant [23]
 on lack
 backend
 in DSL-based
 generates
 educa-
 AspectJ, details,
 and lack
 enterpri
 more c
 and
 Appl.
 rity. directory
 Sci.Spring
 2025, structure.
 15,Initializr
 10621
 rity. [21]
 Spring Spring and directory
 Roo [22]
 rity.
 confined
 is Initializr to
 [21]
 Spring previously
 project
 is structure.
 Initializr
 confinedrity. directory
 reduced
 to
 bootstrapping,
 Spring
 [21] Spring
 is
 project bootstrapping,
 Initializr
 confined Roo
 boilerplate
 structure.
 roducing[22]
 to
 [21] previously
 Spring
 through
 is
 project annota-
 reduced
 [22] previously
 boilerplate reduced through boilerplate
 annota- throu
 modeling,
 tions from and are
 annotated proprietary,
 domain [20]
 modeling,
 which
 classes, also butfacilitates
 limitsandits [20]
 their
 are
 modeling,
 tions
 dependence also
 project facilitates
 extensibility
 proprietary,
 from setup
 and
 on
 annotated through
 which
 areand
 proprietary project
 proprietary,
 transparency.
 limits
 domain
 confined
 aonly
 setup
 their
 bootstrapping,
 producing
 build
 wizard-driven
 through
 which
 classes,
 annotations
 to
 Bootify
 file
 limits
 extensibility
 butre-
 only
 project
 a
 its
 producing
 wizard-driven
 interface,
 their
 a
 bootstrapping,
 and
 build
 dependence
 file
 but
 transparency.
 extensibility
 only
 its
 on
 producing
 a
 interface,
 free build
 and
 version
 Bootify
 proprietary
 file
 transparen
 onlyfr
 but annoits
 tion-driven to trace,
 scaﬀolding, tional
 diminishing
 but it and settings
 tion-driven
 now its [19].
 educational
 outdated, However,
 to trace,
 reliant
 tion-driven
 scaﬀolding, value.diminishing
 onthese
 but OpenXava
 it is
 scaﬀolding,
 AspectJ, platforms
 now andits
 outdated, generates
 educational
 [23]
 but obscure
 more it isRoo
 challenging
 reliant
 now backend enterprise
 value.
 outdated,
 on details,
 OpenXava
 AspectJ, applica-
 reliant lack
 and on DSL-based
 [23]
 more generates
 AspectJ,
 challenging and enterpri
 more
 and directory and structure.
 directory Spring structure.
 Roo
 excludes [22]
 directory Spring
 previously
 REST structure.
 and
 Roo
 excludes
 API directory
 [22]
 reduced
 generation,previously
 Spring
 REST Roo
 boilerplate
 structure.
 API
 dynamic reduced
 [22]
 generation, through
 previously
 Spring
 views boilerplate
 such
 dynamic [22]
 reduced
 annota-
 as through reduced
 annota-
 boilerplate
 previously
 Thymeleaf,
 views such andas through
 Thymeleaf,
 integratedboilerplate
 annota-
 secu-
 and throuc
 [20]
 sults facilitates
 alsolock-in
 in and
 tions project
 conceals
 from etup [20] through
 architectural
 modeling,
 annotated also
 and facilitates
 domain area
 layers [20]
 ults also
 project
 wizard-driven
 crucial
 proprietary,
 classes,
 tions in
 from
 but setup
 facilitates
 for
 ock-in
 which
 its terface,
 learning.
 and through
 limits
 dependence
 annotated projectbut
 conceals
 their
 domain its
 aon free
 architectural version
 through
 wizard-driven
 etup
 extensibility
 proprietary
 classes, but a
 and
 itsinterface,
 layerswizard-driven
 crucial
 transparency.
 dependence
 annotations but for
 re- its
 on interface,
 free
 learning.
 Bootify version
 proprietary butintegr
 its fr
 anno
 to trace, diminishing
 tion-driven scaﬀolding, tion-driven its educational to trace,
 now
 tion-driven
 scaﬀolding,
 but it is value.
 diminishing
 outdated,
 but OpenXava
 to
 scaﬀolding,
 it now
 tion-driven
 reliant its
 trace, on
 but
 outdated, generates
 diminishing
 educational
 [23] AspectJ,
 scaﬀolding,
 it is now
 reliant andits
 value. more
 but
 on
 utdated, OpenXava
 educational
 enterprise
 AspectJ,
 it is now applica-
 challenging
 reliant andvalue.[23]
 utdated,
 on more generates
 OpenXava
 AspectJ, challenging
 reliant
 and enterprise
 [23]
 on
 more generates
 AspectJ, applica-
 challenging enterpri
 andfile more c
 excludesIn REST
 addition API
 to generation,
 these commercial rity.
 dynamic
 excludes Spring
 and views
 REST Initializr
 rity.
 wizard-driven such
 excludes
 API Spring
 [21]
 generation,
 In as is
 REST confined
 Initializr
 Thymeleaf,
 platforms,
 addition dynamic
 API
 to generation,
 aa[21]
 to
 theseand is
 project
 views
 commercial
 parallel bootstrapping,
 confined
 integrated
 linedynamic
 such to
 as
 secu-
 of and
 DSL- project
 views
 Thymeleaf, producing
 wizard-drivenbootstrapping,
 such andas only
 integrated
 Thymeleaf,
 platforms, a build
 producing and
 secu-
 a parallel only
 integr li
 tions from sults
 annotated in domain[20]
 lock-in tify also
 [20] also
 and
 tions
 classes,facilitates
 conceals
 frombut project
 facilitates
 annotated
 its ults
 architectural
 dependence
 tions project
 insetup
 lock-in
 domain
 from through
 setup
 layers
 on and through
 crucial
 classes,
 proprietary
 annotated wizard-driven
 conceals
 domain
 but for wizard-driven
 its architectural
 learning.
 classes,
 dependence
 annotations interface,
 butre- interface,
 layers
 its
 on but
 crucial
 dependence
 proprietary its its
 but freefree
 for version
 version
 learning.
 annotations
 on proprietary re- anno
 to trace, diminishing
 to trace, its diminishing
 educational to
 and trace, value.
 its
 directory educational
 OpenXava
 diminishing to
 structure.
 and trace,
 its
 value.
 [23]
 directory
 Spring generates
 OpenXava
 diminishing
 educational Roo
 structure. its
 value.
 [22] [23]
 enterprise
 educational
 previously
 Spring OpenXava
 generates applica- enterprise
 value.[23] OpenXava
 generates applica- [23]
 enterprise generates applica- enterpri
 rity. Spring
 oriented toolsInitializr
 has [21]
 sought istoconfined
 excludes rity.
 provide
 excludes Spring
 REST to
 REST Initializr
 project
 higherAPI API rity.
 bootstrapping,
 levels
 oriented
 generation, [21]
 Spring
 of
 generation, is Initializr
 confined
 automation
 tools
 dynamic has
 dynamic producing [21]
 to
 sought
 and
 views
 views is
 projecttoconfined
 only
 model-driven
 such
 such aRoo
 provide
 as build
 as
 reduced
 [22]
 bootstrapping,
 ato higher
 Thymeleaf,file
 Thymeleaf,project
 ex- boilerplate
 previously reduced
 bootstrapping,
 producing
 levels
 and of automation
 integrated
 through
 only boilerplate
 asecu- annota-
 producing
 build
 security. and file throu
 onlyli
 model-
 tions in
 sults lock-in
 from tionsIn
 and
 annotated addition
 conceals
 from
 domain sults
 architectural
 annotated to
 classes,
 tions these
 tion-driven
 in
 fromlock-in
 domain
 but commercial
 layers
 annotated
 its and ults
 crucial
 dependence
 classes,
 tions
 scaﬀolding,
 In
 conceals
 in
 tion-driven
 and
 fromaddition
 domain
 butbut
 wizard-driven
 for
 ock-in on
 its andto
 architectural
 learning.
 it proprietary
 annotated
 dependence
 classes,
 scaﬀolding,
 is now
 these
 onceals
 domain
 but commercial
 platforms,
 outdated,
 but
 layers
 its
 on architectural
 annotations
 it dependence
 proprietary
 classes,
 is
 crucial
 reliant
 now
 parallel
 andbut
 on
 for
 re-
 outdated,
 layers
 on
 its
 AspectJ,
 line
 wizard-driven
 learning. of
 crucial
 dependence
 proprietary
 annotations reliant
 and
 DSL- re-
 on
 platforms,
 for
 more onlearning.
 proprietary
 annotations
 AspectJ,
 challenging
 a parallel
 and re-
 more anno c
 and directory
 pressiveness. structure.
 DSL-oriented
 oriented Spring
 rity.
 tools andRoo
 tools
 Spring
 Spring
 has [22]
 directory
 oﬀer
 Initializr
 Initializr
 sought previously
 to [21] and
 structure.
 pressiveness.
 greater
 [21]
 provideis
 oriented directory
 is Spring
 reduced
 automation
 confined
 confined
 highertools structure.
 boilerplate
 tohas Roo
 DSL-oriented
 to
 levels [22]
 but
 project
 project sought
 of previously
 Spring
 through
 remain
 bootstrapping,
 bootstrapping,
 to
 automation Roo
 tools
 provide annota-
 reduced
 [22]
 limited.
 and oﬀer
 producing
 higherpreviously
 producingboilerplate
 greater
 model-drivenlevels only reduced
 of automation
 only ax- through
 a
 build build
 utomation annota-
 boilerplate
 filefile but
 and
 and throu
 remain
 model-
 sults In additionand
 in lock-in to these
 sults inconceals commercial
 lock-in sults
 and
 architectural
 tonow
 In
 trace,in wizard-driven
 addition
 andlock-in
 conceals architectural
 layers
 diminishing andto these
 in
 conceals
 crucial
 ults In
 its on
 trace,
 toreliant
 commercial
 addition
 platforms,
 for
 educational
 diminishing andto aand
 these parallel
 conceals
 crucial
 architectural
 learning.
 layers
 ock-in its
 value.
 commercial
 for line
 wizard-driven
 learning.
 layersarchitectural
 OpenXava
 educational
 of
 crucial and
 DSL-
 value.
 platforms,
 for wizard-driven
 learning.
 layers
 OpenXava
 generates
 [23]AspectJ,
 a
 crucial parallelplatforms,
 for
 enterprise
 [23]
 line
 learning.
 generates
 of aDSL-
 applica-
 parallel
 enterpri
 li
 tion-driven
 CRUDyLeaf scaﬀolding,
 [24] is a but
 lightweight
 and it istion-driven
 DSL-based
 directory outdated, tion-driven
 scaﬀolding,
 structure. generator
 CRUDyLeaf
 Spring but
 thatRoo itgreater
 is
 scaﬀolding,
 AspectJ,
 creates
 [24] now
 [22] is but
 outdated,
 and
 lightweight
 aand
 CRUD
 previouslymore it
 APIs is
 challenging
 reliant
 now
 DSL-based
 for
 reduced on
 outdated,
 entity boilerplate reliant
 generator and
 through on
 more
 that AspectJ,
 challenging
 creates
 annota- and
 CRUD more APIc
 oriented tools
 In addition pressiveness.
 to sought
 has these
 In additionto irectory
 commercial DSL-oriented
 provide
 oriented
 to these
 In
 structure.
 and tools
 higher
 addition
 commercial
 Spring
 tools
 pressiveness.
 levels
 hasoriented
 wizard-drivento sought
 of
 In
 these oﬀer
 and
 Roo
 automation
 ools
 to
 commercial
 addition
 [22] DSL-oriented
 provide
 platforms, has
 wizard-driven to
 previously
 ought
 these
 a automation
 higher
 andparallel to
 commercial
 reduced
 model-driven
 platforms, tools
 levels
 provide
 line
 wizard-driven but
 ofof
 aand
 boilerplate
 oﬀer
 DSL- ex- line
 wizard-driven
 platforms,
 parallelremain
 automation
 higher greater
 levels through
 limited.
 ofand
 aof automation
 DSL-
 annotation-
 automation
 model-driven
 parallelplatforms, line of but
 and
 aDSL- ex- remain
 model-
 parallel li
 to trace,
 management, yetdiminishing it its educational
 does not[24] tions
 to
 generatetrace, fromviews OpenXava
 diminishing
 value. annotated
 or tions
 to its
 trace,
 security
 management, domain
 from [23] classes,
 annotated
 educational
 generates
 diminishing
 features, yet ita domain
 but
 its
 value.
 leaving
 does its
 enterprise dependence
 educational
 not classes,
 OpenXava
 generate
 applications but
 value.
 applica- [23]
 in-
 views its
 on proprietary
 dependence
 OpenXava
 generates
 or security [23] annotations
 enterpriseon generates
 features, proprietary
 applica-
 leaving re- anno
 enterpri
 appli
 pressiveness. CRUDyLeaf
 DSL-oriented tion-driven
 driven is
 pressiveness.
 tools scaﬀolding,
 scaffolding,
 lightweight
 oﬀer but
 greater but
 it is
 DSL-based
 CRUDyLeaf
 pressiveness.
 DSL-oriented itnowis now
 automation outdated,
 [24] outdated,
 generator
 tools is lightweight
 but
 DSL-oriented oﬀereliant
 that reliant
 remain on
 creates
 greater
 tools on
 AspectJ, AspectJ,
 CRUD
 DSL-based
 automation
 limited.
 oﬀer and APIs and
 more
 generator
 greater for more
 challenging
 entity
 but challenging
 that
 automation
 remain to trace,
 creates CRUD
 limited.
 but API
 remain
 oriented tools hasoriented
 sought tools
 to hasprovide
 oriented
 sults sought
 in tools
 higher
 lock-in to provide
 levels
 hasoriented
 sults
 and sought
 of higher
 conceals
 in to
 ools
 automation
 lock-in provide
 has
 levels
 and
 architectural and
 of
 conceals to
 automation
 higher
 sought layers provide
 model-driven
 levels crucial
 architectural and
 of higher
 model-driven
 ex-
 automation
 forlayers levels
 learning. and
 of
 crucial for model-driven
 automation
 ex- learning. and model-
 ex-
 tions
 complete fromand annotated
 limiting
 management, domain
 itsto trace, classes,
 tions
 educational
 diminishing
 yet it from
 diminishing
 does but its its
 annotated
 utility.
 not dependence
 tions
 JHipster
 complete
 its
 educational
 generate
 management, domain
 from
 educationalvalue.
 views[25]
 andannotated
 on orclasses,
 proprietary
 integrates
 limiting
 yet value.
 OpenXava
 security domain
 doesbutits
 Spring
 OpenXava annotations
 its
 not dependence
 classes,
 educational
 [23]
 features, Boot
 [23]
 generates
 generate leaving but
 withre-
 generates
 views its
 on
 utility. proprietary
 enterprise
 ordependence
 JHipster
 applications enterprise
 security in-[25]
 applications on
 annotations
 proprietary
 integrates
 applica-
 features, from
 leaving re- anno
 Spring
 appli
 CRUDyLeaf
 pressiveness. [24] is a lightweight
 pressiveness.
 DSL-oriented CRUDyLeaf
 tools DSL-based
 pressiveness.
 DSL-oriented oﬀer [24]
 greater is
 enerator
 CRUDyLeaf
 DSL-oriented
 tools that
 lightweight
 pressiveness.automation
 oﬀer creates
 [24]
 greater
 tools
 DSL-oriented lightweight
 CRUD
 DSL-based
 is a but
 oﬀer
 automation APIs
 remain generator
 tools
 greater DSL-based
 forlimited.
 but oﬀerthat
 ntity remain
 automation creates
 generator
 greater CRUD
 but
 limited. that
 automation APIs
 remain creates for entity
 CRUD
 limited.
 but API
 remain
 sults
 modern in lock-in
 frontends and conceals
 and supports architectural
 sults In
 in
 advanced addition
 lock-in layers andto
 security in
 conceals
 crucial
 ults
 modern In
 theseand commercial
 addition
 for
 ock-in and
 learning.
 microservices.
 frontends to
 architectural these
 andand
 conceals wizard-driven
 commercial
 layers
 While
 supports architectural
 crucial
 potent,
 advancedand platforms,
 for
 itswizard-driven
 learning.
 layers
 security a
 crucial parallel
 and platforms,
 for line
 learning.
 microservices. of a parallel
 DSL- While li
 management,[24] complete
 yetisita does not tions
 and from
 annotated
 limiting
 generate
 management, annotated
 domain
 its
 views classes,
 educational
 or domain
 completedoes
 security
 management,
 yetisit but classes,
 and
 utility.
 notits
 features, dependence
 limiting
 JHipster
 generate
 yet but its
 leaving
 does dependence
 views[25]
 its on
 not proprietary
 integrates
 educational ecurity
 generate
 applications
 or on proprietary
 annotations
 Spring
 utility.
 features,
 in-
 views or Boot
 JHipster
 leaving
 security annotations
 results
 with [25]
 features, in re-
 lock-in
 tegrates
 applications leaving Spring
 in- appli
 CRUDyLeaf CRUDyLeaf lightweight [24] CRUDyLeaf
 isDSL-based
 oriented lightweight generator
 [24]
 tools has CRUDyLeaf
 DSL-based
 a lightweight
 sought
 oriented that
 ools
 to generator
 creates
 [24]
 provide
 has is a lightweight
 CRUD
 DSL-based
 ought that
 higher to generator
 creates
 APIslevels
 provide CRUD
 DSL-based
 for ofDSL- that
 ntity
 automation
 higher APIs
 creates
 generator
 for
 levelsand CRUD
 entity that APIs
 creates for CRUD
 entity API
 In addition
 complexity often to these
 overwhelms
 modern commercial
 sultsand
 frontends novices,
 in In
 lock-in
 conceals
 and andwizard-driven
 addition
 and and
 architectural
 supports to
 conceals
 modern
 advanced platforms,
 addition
 commercial
 In layers
 these
 complexity
 empirical studies often
 architectural
 frontends crucial
 ecurity to
 have a
 these
 overwhelms
 layers
 andandparallel
 highlighted
 for
 and supportscrucial
 learning. line
 wizard-driven
 commercial novices,
 microservices. forand
 theof
 advanced intri-andwizard-driven
 platforms,
 learning.
 While empirical
 security potent,aof
 and
 automation
 model-driven
 parallelplatforms,
 studies
 its line
 have
 microservices. ofand parallel
 aDSL- model-
 ex-
 highlighte
 While li
 complete
 management, and limiting doesits
 management,
 yet noteducational
 complete
 management,
 yet
 generateit does and
 utility.
 viewsnot complete
 limiting
 yet
 or JHipster
 management,
 security
 generate does its
 views[25]
 and
 not
 features,or limiting
 educational
 integrates
 yet
 generate security
 leaving
 does utility.
 views noteducational
 Spring
 its or
 applications
 features, JHipster
 Boot
 generate leaving
 security withutility.
 [25]
 in-
 views
 features, or JHipster
 integrates
 applicationssecurity
 leaving [25]
 Spring
 in-features, Boot
 integrates
 applications with
 leaving Spring
 in- appli
 oriented
 cacy of its tools has
 build and soughtdeploymentto pressiveness.
 oriented
 provide processes tools
 higher DSL-oriented
 has
 [26],pressiveness.
 oriented
 levels
 cacy sought
 of
 raising its to
 ools
 automation
 build
 concerns DSL-oriented
 tools
 provide
 has and oﬀer
 andhigher
 sought
 deployment
 about to greater
 model-driven tools
 levels
 provide
 maintainability. of automation
 oﬀer
 processes automation
 ex-
 higher greater
 levels
 [26],a but
 of
 and
 raising remain
 automation
 model-driven
 automation
 concerns but
 limited.
 and
 about remain
 model-
 ex- main
 modern frontends complexity
 and supports In
 ften addition
 In
 overwhelms
 modern addition
 advanced tosecurity
 frontends these
 to these
 complexity
 novices,
 modern commercial
 andandcommercial
 and and
 empirical
 often
 microservices.
 supports
 frontends and wizard-driven
 overwhelms
 and
 advanced wizard-driven
 studies
 supports
 While have
 novices,
 security platforms,
 potent, platforms,
 highlighted
 and
 advanced and security
 microservices.
 its a parallel
 empirical theparallel
 intri-
 and line
 studies
 While of
 line DSL-
 of
 have
 microservices. DSL-
 potent, highlighte
 itsWhile
 complete and limiting
 complete itsandeducational
 limiting
 complete
 CRUDyLeaf itsand
 utility.
 educational
 [24]limiting
 complete
 JHipster
 is
 CRUDyLeaf
 a its
 utility.
 [25]
 and
 lightweight [24]limiting
 educational
 integrates
 JHipster
 issteep
 DSL-based
 a utility.
 its
 [25]
 Spring
 lightweight JHipster
 educational
 generatorBoot
 integrates
 DSL-based with Spring
 [25]
 utility.
 that integrates
 creates Boot
 JHipster
 generator CRUDwith [25]
 Spring
 that APIs Boot
 integrates
 creates for but with
 CRUD
 entity SpringAPI
 pressiveness.
 Educationally, DSL-oriented
 its
 cacy steep
 of learning
 its oriented tools
 pressiveness.
 oriented
 buildmodern curve
 and tools oﬀer
 tools and
 has
 deploymenthas greater
 pressiveness.
 DSL-oriented
 Educationally,
 production-grade
 ought
 sought
 cacy o automation
 processes
 ofto provide
 provide
 its build tools
 [26], its
 tooling
 higher
 higher
 and but
 DSL-oriented oﬀer
 raising renderremain
 learning
 levels
 deployment greater
 concerns it
 of ools
 curve
 more aboutoﬀer
 limited.
 automationautomation
 automationsuit-
 processes and greater
 production-grade
 and
 and
 maintainability.
 [26], but automation
 model-driven
 model-driven
 raising remain
 concerns tooling limited.
 ex-
 expres- remain
 render it
 complexity
 modern frontends often overwhelms
 modern and frontends
 supports complexity
 novices,
 and
 advanced and overwhelms
 complexity
 empirical
 often
 frontends
 supports modern
 security and
 advanced
 and studies
 frontends
 upports often novices,
 securityhave
 microservices. advancedand and
 highlighted
 overwhelms
 and upports
 While
 microservices.
 security the
 novices,
 empiricalpotent,
 advanced
 and and
 studies
 intri- While
 its have
 empirical
 microservices.
 security potent, highlighted
 and studies
 its
 While have
 microservices. theabout
 potent, intri-
 highlighte main
 itsWhile
 CRUDyLeaf
 able for advanced[24] is ora lightweight
 DevOps-oriented management,
 DSL-based
 CRUDyLeaf courses yet is
 than
 able a
 CRUDyLeaf
 generator
 [24] management,
 it does
 lightweight
 for not
 that
 advanced
 introductory generate
 yet
 [24]
 creates it adoes
 CRUD
 lightweight
 DSL-based
 is or web views not generate
 generator
 APIs
 DevOps-oriented
 engineering. ecurity
 for
 DSL-based that
 Fur-features,
 views
 ntitycourses or
 generator
 creates leaving
 security
 han CRUD features,
 that applications
 introductory creates
 APIs for leaving
 entity
 CRUD
 web in- appli
 engineAPI
 cacy of its build Educationally,
 and deployment siveness.
 pressiveness.
 its
 cacy steep
 of DSL-oriented
 processesits DSL-oriented
 learning
 build [26], curve
 and
 cacy tools
 Educationally,
 raising
 of and
 itsoffer
 tools
 deployment concerns
 build greater
 oﬀer
 its
 production-grade
 and teep automation
 deployment
 about
 processesgreater
 learning [26], but
 automation
 curve
 tooling
 maintainability.raising remain
 processesrender
 and concerns limited.
 but
 it
 [26], more
 production-grade CRUDyLeaf
 main
 raising
 aboutsuit- limited.
 tooling
 maintainability.
 concerns [24] render it
 complexity oftencomplexity
 overwhelms often complexity
 ovices,
 overwhelms
 complete and
 and often complexity
 overwhelms
 ovices,
 empirical
 complete
 limiting studies
 and
 its and often
 empirical
 novices,
 have
 limiting
 educational overwhelms and
 highlighted
 studies
 utility.
 its empirical
 have
 novices,
 the
 JHipster
 educational intri-and
 studies
 highlighted
 utility.
 [25] have
 empirical the
 integrates
 JHipster studies
 intri-
 highlighted
 Spring
 [25] havetheabout
 integrates
 Boot intri-
 highlighte
 with
 main
 Spring
 management,
 thermore, yet
 although
 able it does
 JDL
 for not is generate
 facilitates
 CRUDyLeaf
 advanced a management,
 ordomain
 lightweight views
 [24] is yet
 or thermore,
 modeling,
 DSL-based
 DevOps-oriented a management,
 security
 it does
 lightweight
 able for features,
 not
 JHipster
 advanced generate
 although
 generator
 courses yet
 DSL-based provides
 than or does
 leaving
 it
 that JDL views
 creates notapplications
 limited
 generator or
 facilitates
 introductory
 DevOps-oriented generate
 CRUD security
 domain
 backend
 that APIs
 web in-
 views
 features,
 createsfor
 courses or
 modeling,
 entity
 engineering. CRUD leaving
 security
 than JHipster
 management,
 APIs applications
 features,
 introductory
 Fur- for entity leaving
 provides
 yetweb it in- appli
 limite
 engine
 cacy of its buildits
 Educationally, and
 cacy steep learning
 buildcacy
 deployment
 of its Educationally,
 curve
 and processes
 of and
 deployment
 its Educationally,
 its steep
 production-grade
 build [26],cacy
 and raising
 processes
 of learning
 eployment
 its concerns
 build[26], its
 tooling
 curve
 andsteep
 about
 processes
 raising learning
 and
 render [26],
 maintainability.
 concerns
 eployment it more
 production-grade
 curve
 raising suit-
 processes
 about and production-grade
 concerns tooling
 maintainability.
 [26], raising
 aboutrender it more
 tooling
 maintainability.
 concerns about render
 suit- main it
 complete
 view-layer and limiting
 generation and lacks modern
 complete
 its educational explicit frontends
 and
 utility.
 modeling modern
 limiting and
 JHipster
 completeof
 view-layer frontends
 supports
 its
 secure and
 [25]
 educational advanced
 integrates
 limiting
 connectors,
 generation and supports
 Spring
 its
 utility.
 and security
 educational
 reducing
 lacks advanced
 Boot
 JHipster its
 explicitand with
 ped- [25]
 utility. security
 microservices.
 modeling JHipster
 integrates of and
 secure microservices.
 While
 [25]
 Spring potent,
 Boot
 integrates
 connectors, withitsWhile
 Spring
 reduci
 able for advanced thermore, does
 management,
 although not JDLgenerate
 yet it
 facilitates views
 does
 thermore, or
 not
 domain security
 generate
 although
 modeling, features,
 views JDL or leaving
 facilitates
 JHipstersecurity applications
 features,
 provides
 domain limited incomplete
 leaving
 modeling, applications
 backend JHipsterand limiting
 in-
 provides limite
 Educationally, its or DevOps-oriented
 Educationally,
 steep learning able
 its curvefor
 Educationally,
 steep
 complexity
 courses
 advanced
 learning
 and often
 able
 thanor for
 DevOps-oriented
 introductory
 Educationally,
 production-grade
 its curve
 teep
 complexity
 overwhelms
 advanced
 and
 learning production-grade
 often tooling
 its steep
 curve
 novices,
 or web courses
 DevOps-oriented
 overwhelms and
 engineering.
 render
 and
 learning than
 tooling
 it curve
 more
 production-grade
 empirical
 novices,
 introductory
 Fur-
 suit-courses
 render
 and
 and
 studies production-grade
 ittooling
 more
 empirical
 than
 have
 web introductory
 render
 suit-engineering.
 highlighted
 studies it more
 tooling
 havethe
 web Fur-
 render
 suit-engine
 highlighte
 intri- it
 modern
 agogical frontends
 value for andteaching
 view-layer supportsits
 complete modernadvanced
 architectural
 educational
 generation and andfrontends
 layering
 utility.
 limiting
 lacks modern
 security and
 agogical
 JHipster
 its
 explicit
 view-layer and
 and supports
 frontends
 value
 educationalmicroservices.
 security
 [25]
 generation
 modeling foradvanced
 and
 design.
 teaching
 integrates
 utility.
 of supports
 and
 secure Whilesecurity
 To
 Spring
 JHipster
 lacks potent,
 consolidate
 architectural
 Boot
 connectors, [25]
 explicitand
 advanced with its
 microservices.
 layering
 modern
 integratessecurity
 reducing
 modeling frontends
 Spring
 its
 of and
 and
 secure
 ped- microservices.
 While
 security
 Boot andpotent,
 with
 connectors, design.
 sup- While
 itsreduci
 To c
 thermore,
 able for advanced although JDL facilitates
 DevOps-oriented
 ableorfor advanced thermore,
 able domain advanced
 DevOps-oriented
 for itscourses
 orof although
 modeling,than
 able JDL
 thermore,
 or of JHipster
 DevOps-oriented
 for its facilitates
 although
 advanced
 courses
 introductory provides
 han JDL
 domain
 orweb courses
 introductorymodeling,
 facilitates
 limited
 DevOps-oriented
 engineering. thanbackend
 domain
 web JHipster
 introductory
 Fur-coursesmodeling,
 engineering. provides
 than web limited
 JHipster
 introductory
 Fur- engineering. backend
 provides
 web Fur- limite
 engine
 complexity
 these often
 observations overwhelms
 andand enable cacy
 novices,
 complexity
 a structured and build
 often and
 cacy
 empirical
 complexity
 comparison,
 these deployment
 overwhelms studiesbuild
 observations
 theoften and
 have
 novices,
 surveyed processes
 overwhelms
 and eployment
 and
 highlighted
 enable
 tools [26], raising
 novices,
 empirical
 area processes
 the
 summa-
 structured and
 studies
 intri- concerns[26],
 empirical
 have
 comparison, about
 raising
 highlighted
 studiesmaintainability.
 concerns
 the havethe
 surveyed about
 intri-
 highlighte main
 tools
 view-layer
 thermore, agogical
 generation
 thermore,
 although JDL value
 ports
 modern
 lacks
 facilitates
 although for advanced
 frontends
 thermore,teaching
 view-layer
 explicit
 JDL
 domain
 security
 modeling and
 architectural
 generationagogical
 view-layer
 modeling,
 facilitates
 although
 supports
 of
 thermore,
 and
 domain
 JDL secure
 and microservices.
 value connectors,
 generation
 lacks
 modeling,
 although
 facilitates
 JHipster
 advanced
 layering for teaching
 explicit
 provides and
 domain
 JDL
 While
 security
 and security
 modeling
 reducing
 JHipster lacks potent,
 architectural
 modeling,
 facilitates
 limited
 and design.
 its
 of
 explicit its
 secure
 domain
 backend
 provides ped- complexity
 microservices.
 JHipster To
 layering
 modelingconnectors,
 imited
 modeling,
 often
 While
 consolidate
 of
 provides and
 backend secure overwhelms
 potent,
 security
 reducing
 JHipster
 limited connectors,its
 design.
 its
 provides
 backend ped- To ac
 reduci
 limite
 cacy
 rized ofin its build
 Table 1 and
 across deployment
 six key Educationally,
 cacy
 novices, processes
 of
 evaluation
 and its build
 empirical its
 [26],
 criteria:
 rized teep
 Educationally,
 cacy
 and learning
 its
 deployment
 of
 raising
 DSLin
 studies concerns
 Tablebuild
 support,
 have 1 andsteep
 itscurve
 processes
 about
 view
 across
 highlighted and
 learning
 deployment
 six production-grade
 [26],
 maintainability.
 generation,
 key
 the curve
 evaluation
 intricacyprocesses
 raising REST and
 of production-grade
 concerns
 its tooling
 [26],
 criteria:
 build about
 raising
 and DSLrender concerns
 maintainability.
 support,
 deployment tooling
 it more about
 view
 pro-suit-
 render main
 genera it
 agogical value for complexity
 observations
 theseteaching architectural
 agogical often
 andand enable
 value overwhelms
 a
 these
 for
 layeringagogical novices,
 observations
 structured
 teaching
 and value comparison,
 architectural
 security for andand
 teaching
 design.empirical
 the
 enable surveyed
 layering
 To a studies
 structured
 architectural
 consolidateand have
 tools
 security are
 layering highlighted
 summa-
 comparison,design.
 and the
 security
 Tothe intri-
 surveyed
 consolidate
 design. tools To ac
 view-layer generation
 view-layer and lacks
 generation
 view-layer
 ableexplicit
 for generation
 modeling
 lacks
 advanced explicit
 able orof
 view-layer
 for secure
 and modeling
 lacks
 generation
 DevOps-oriented
 advanced of
 explicit
 connectors, or secure
 andmodeling
 courses
 DevOps-orientedconnectors,
 lacks
 reducing than its
 of
 explicit ped-
 secure modeling
 reducing
 introductory
 courses connectors,
 than of
 its
 web secure
 ped- reducing
 engineering.
 introductory connectors,its
 web ped-
 Fur- reduci
 engine
 APIs, security, its
 Educationally, steep
 scope,
 rized inandlearning
 complexity.
 cacy
 Table cessesof curve
 Educationally,
 [26],
 its build and
 raising andproduction-grade
 its
 Educationally,
 steep
 APIs,
 concerns
 deployment learning
 security,
 about tooling
 its
 processescurve
 scope, steep
 maintainability. render
 andand
 learning
 [26], it more
 complexity. curve
 production-grade
 Educationally,
 raising and its
 suit-
 concerns production-grade
 tooling
 steep DSL
 about render
 learning
 maintainability. tooling
 it more
 curve and render
 suit- it
 these observations
 agogical value for
 agogicaland
 teaching across
 value 1thermore,
 enable a
 these
 architectural six
 observations
 structured
 agogical
 for teaching value keycomparison,
 layering
 for
 architectural
 although
 evaluation
 rized
 these and
 agogical
 thermore,
 JDL
 in
 teaching
 and Table
 enablethe
 observations
 although
 afor
 architectural
 layering
 security
 valuecriteria:
 facilitates
 1 across
 surveyed DSL
 and
 structured
 design.
 teaching
 and
 domain
 JDL
 six key
 support,
 enable
 tools To
 layering
 security
 modeling,
 facilitates
 are view
 evaluation
 a
 comparison, structured
 summa-
 consolidate
 design.
 architectural and
 domain
 generation,
 the criteria:
 security
 JHipster To comparison,
 surveyed
 layering
 modeling,
 REST
 design.
 consolidate
 provides and support,
 tools
 security
 JHipster
 the
 To
 limited
 are
 surveyed view
 summa-
 design.
 consolidate
 provides
 backend
 genera
 tools To ac
 limite
 able for advanced or security,
 DevOps-oriented able
 production-gradefor advanced
 courses able
 than
 tooling orforDevOps-oriented
 introductory
 advanced
 render it orweb engineering.
 courses
 DevOps-oriented than introductory
 Fur-or
 courses than web introductory
 engineering. web Fur- engine
 rized
 these in Table 1APIs,
 observations across
 these and six
 Educationally,
 enable
 observations key scope,
 rized
 evaluation
 these
 a inand its
 Table
 observations
 tructured
 and
 steep
 complexity.
 enable 1 APIs,
 rized
 criteria:
 aacross
 these
 comparison,
 arning
 DSL
 and in
 tructuredecurity,
 Table
 six curve
 support,
 enable key
 the
 observations 1more
 a
 and
 scope,
 across
 view
 evaluation
 and
 structured
 surveyed
 comparison,
 suitable
 production-grade
 and six the key
 criteria:
 generation,
 tools
 enable
 for
 complexity.
 comparison,
 surveyed
 area
 advanced
 DSL
 evaluation
 summa- REST
 structured
 tooling
 the
 tools
 DevOps-oriented
 criteria:
 support, render
 surveyed
 comparison,
 are viewDSLtools
 summa-
 it more
 generation,
 support,
 the are
 courses
 suit-
 surveyed REST
 view
 summa- genera
 tools a
 thermore,
 Table although
 1. Summary of JDL
 Related facilitates
 Work.
 than view-layer
 thermore,domain
 introductory generationTable
 web JDL
 thermore,
 modeling,
 although view-layer and
 1. lacks
 JHipstergeneration
 facilitates
 engineering. although
 Summary explicit
 provides
 of domain
 JDL and
 Related
 Furthermore, lacks
 modeling
 modeling,
 facilitates
 limited
 Work. explicit
 backend
 althoughof secure
 domain modeling
 JHipster connectors,
 modeling,
 JDL web of
 provides
 facilitates securereducing
 limited
 JHipster
 domain Fur- connectors,
 model- reduci
 its
 backend
 provides ped- limite
 APIs, in security, scope, and able for
 complexity.
 APIs, advanced
 security, DevOps-oriented
 orscope,
 APIs, andecurity,
 complexity. scope, coursesand than
 complexity. introductory engineering.
 rized Table 1rizedacross in six
 Table key1 rized
 evaluation
 across
 agogical in Table
 six
 value 1 rized
 evaluation
 across
 criteria:
 key DSLin
 teaching
 agogical
 for six
 Table
 valuecriteria:
 key
 support, 1
 architectural
 for view
 across
 evaluationDSL
 teachingsix key
 criteria:
 support,
 generation,
 layering evaluation
 DSL
 view
 architectural andREST criteria:
 support,
 generation,
 layering
 security view REST
 DSL
 and
 design. generation,
 support,
 security
 To view
 consolidate REST
 design. generaTo c
 view-layer generation and lacks
 ing,
 thermore, view-layer
 explicit
 JHipster
 although generation
 modeling
 provides JDLview-layer
 of secure
 and
 limited
 facilitates lacks connectors,
 generation
 backend
 domain explicit and
 view-layer lacks
 reducing
 modeling
 modeling, its
 of
 explicit
 generation
 JHipster ped-
 secure modeling
 and connectors,
 provides lacks of secure
 explicit
 limited reducing connectors,
 modeling
 backend its ped-reduci
 DSL-Based View Table
 APIs, security, REST1.API
 scope,
 APIs,
 Summary
 security,
 and Tool Security
 complexity.
 of
 APIs,
 Related
 scope, and Model
 DSL-Based
 security,
 Work.
 complexity.
 Table
 scope,
 APIs,
 1.
 View
 and
 Summary
 security,Scope
 complexity. REST of
 scope,
 Related
 API
 and
 Work.
 Security
 Complexity
 complexity. Model Scope Co
 agogical value for teachingof these
 agogical
 architectural
 secure observations
 value
 connectors, these and
 agogical
 for
 layering teaching
 educing enable
 observations
 and value
 security
 its a structured
 for
 architectural
 pedagogical and
 design.
 teaching enable
 value a
 comparison, structured
 consolidate
 architectural
 layering
 To for and
 teaching the
 security surveyed
 comparison,
 layering design.
 architectural and To toolsthe
 security summa-
 surveyed
 are
 layering design.
 consolidate
 and tools To ac
 ✗ view-layer generation and lacks explicit modeling of secure connectors, reducing its ped-
 Tool Table 1. ✔
 DSL-Based ✔ View
 Summary of RelatedMendix Work.
 Tool rized REST✗in
 Table 1. Summary
 API
 DSL-Based
 Table ✗ of
 Table
 Security
 across
 1rized
 Related
 1. Summary
 View
 Model
 insix✔
 Full-stack
 Table
 Work.
 key REST
 1a
 of ✔ API
 evaluation
 across
 Related
 six
 Work.
 Scope Security
 criteria:
 key
 High ✗ Model
 evaluation
 DSL support,Complexity
 criteria: view
 Full-stack
 DSLtools Scope
 generation,
 support, view
 REST genera Co
 these observations and enable agogical these
 securitya observations
 structured
 design.
 value for To these
 comparison,
 teaching and
 consolidate enablethe
 observationsthese
 architectural surveyed
 structured
 and
 observations enable
 tools
 layering are
 and
 anda
 comparison, structured
 summa-
 enable
 security the
 a comparison,
 surveyed
 structured
 design. To the
 comparison, are
 consolidate summa-
 surveyed the tools a
 ✔
 Mendix
 DSL-BasedTable 1. ✗
 ViewTool ✗ 1REST
 Summary of
 Table ✔ 1.
 Related ✔
 CRUDyLeaf
 Summary
 Mendix
 DSL-Based
 API ToolWork.
 Securityof
 Table
 APIs, ✗
 ✔in
 Related
 1. Summary
 DSL-Based
 View
 Model
 security, ✔
 ✗
 Work. Table
 RESTof
 scope, ✗and
 Backend
 APIs, 1.
 Related
 API ✗
 ✔
 Summary
 View
 security,
 (CRUD
 Work.
 Scope REST
 Security
 complexity. of
 scope, ✔
 ✔ and
 only)
 Related Work.
 Full-stack
 Model
 API Complexity
 Security
 complexity.
 Low ✗
 ✗RESTModel Scope Backend
 High (CRUD
 Full-stack
 ScopeComplexity only) Co
 rized in Table across six key rized
 surveyed evaluation Table criteria:
 1 across
 rized DSLin Table
 six key
 support, 1 evaluation
 view
 across six criteria:
 key
 generation, evaluation
 DSL support,
 criteria: viewDSL generation,
 support, view
 REST genera
 ✗
 ✗
CRUDyLeaf Partial
 ✔
 Mendix ✔ scope, ✗
 ✔ API ✗
 CRUDyLeaf
 these
 Bootify.io
 Mendix ✗ ✗tools
 observations
 ✔✗ ✔
 are
 ✗
 ✗
 summarized
 and enable
 ✔Security ✔✗API ✗
 Partial
 Backend
 ✔
 a instructured
 Full-stack
 Table✗1 across
 starter ✔
 ✔
 ✗
 Backend
 comparison,
 (CRUD
 six
 Medium key✗
 High
 the
 ✗
 ✗
 only)
 surveyedcriteria:
 evaluation
 Full-stack Low
 toolsBackend
 Backend
 areDSL
 (CRUD
 Full-stack
 support,
 summa-
 starter
 High only) M
 Tool
 DSL-Based View
 DSL-Based
 APIs, security,Tool REST View
 DSL-Based
 and Tool
 rized Security
 view REST
 complexity.
 APIs,
 in Table DSL-Based
 Model
 View
 API
 security,
 generation, 1 across REST
 scope,
 REST APIs,six Model
 View
 and
 APIs,security,
 key ScopeSecurity
 complexity.
 security,
 evaluation REST
 scope,scope, API
 Model
 and andScope
 criteria: Complexity
 Security
 complexity.
 complexity.
 DSL Model
 support, Scope Complexity
 view generation, ScopeComplexity
 REST Co
 ✗✔
 Bootify.io ✗
 ✗ ✗ ✗
 Spring
 ✔Partial ✔ Table✗
 Initializr
 Bootify.io ✗
 ✗1. ✗ ✗
 ✗
 ✔ of ✔✗
 Skeleton ✗
 ✗
 Partial project ✗
 ✗
 only
 ✗
 ✔ Backend Low
 starter ✗
 ✗
 ✗ Medium Skeleton
 Backend project
 starter only M
 ✗
 Mendix ✔
 CRUDyLeaf
 Mendix ✗ ✔ ✔
 CRUDyLeaf
 Mendix ✗
 APIs, ✔✗
 security, ✔scope,
 Summary ✗ and✔✗
 Table Related
 Backend 1. ✔
 complexity.
 Work.
 Summary(CRUD
 Full-stack of ✗ ✔
 Related
 only) Work.
 Full-stack ✗
 Backend
 Low
 High (CRUD
 Full-stack Backend
 Highonly) (CRUD
 Full-stack Low
 High only)
 Partial
 ✗ ✔ ✗ ✔ ✗
 JHipster ✗✔ ✗
 Partial ✗ ✔
 ✗
 Full-stack ✔
 ✗ High ✔
 ✗ Full-stack
pring Initializr
 ✔ Table 1.
CRUDyLeaf ✗
 Partial
 Bootify.io
 CRUDyLeaf
 Tool ✔
 Summary of ✗Spring
 ✗Tool
 ✔CRUDyLeaf
 Related
 DSL-Based✗
 Initializr
 ✔
 Bootify.io
 Work.
 Table Table1. ✔ ✗
 ✗1. ✗ ✗
 Partial
 Summary
 Summary ✔ of
 Table ✗
 ✔✗API
 Backend
 Partial
 1.
 Related
 Backend
 Related
 ofREST ✗
 Work. Work.
 Summary(CRUD starterof ✗
 Skeleton
 ✗
 ✔ API
 Related
 Backend
 only) project
 Work.
 (CRUD Medium
 Low ✗
 only
 ✗
 BackendBackend
 only) (CRUD Low
 starter
 LowSkeleton
 Backend
 only)Backend project
 (CRUD Medium
 starter
 Low only
 only) M
 Partial Spring Partial ✗ ✔
 Spring Roo ✔✗View DSL-Based
 Partial ✔ ✔
 Partial
 MonolithicView SpringREST
 Security ✗
 ✔
 Model
 apps Security
 Medium ✗
 ✔
 Model Scope Monolithic ScopeComplexity
 Spring apps Co M
 ✗
 JHipster
 ✗
 Bootify.io ✗ Partial
 Bootify.io
 Partial
 Mendix ✗ REST
 Initializr ✗
 Spring JHipster
 ✗Partial ✗
 ✗
 Initializr
 ✗
 Bootify.io
 Table
 Mendix 1. ✗ ✗
 ✗
 Summary ✗
 ✔
 Partial ✗
 Partial
 ✗
 ✗
 of Related ✗
 ✗
 Skeleton
 ✔✗Work. ✗
 ✔
 Partial
 Backend project
 starter ✗
 ✗
 only
 ✗
 ✔
 Full-stack
 Backend Low
 starter
 Medium ✗
 ✗
 Skeleton
 ✗Backend project
 Full-stack
 High
 Medium
 starter only
 Skeleton Full-stack
 Backend project
 Full-stack
 Low
 starter
 Medium
 High
 only M
 ✗Roo
 DSL-Based Tool✔Partial
 ViewTool ✗ API
 DSL-Based
 Tool Roo ✗✗
 Security Model
 DSL-Based
 View ✗ REST API
 View✔ Scope REST
 Security ✗ Model
 API Complexity
 Security ✗ Model Scope ScopeComplexity Co
 ✗✗ ✗ ✗
 OpenXava Full-stack Low Full-stack
 Spring
pring ✗
 Partial
 Initializr Spring ✔
 ✗
 JHipster✗
 Initializr ✔
 DSL-Based
 ✗
 Partial
 Spring
 Spring ✗
 JHipster✗
 Partial
 ✔
 Initializr ✔ ✗
 View
 ✗✗
 ✗ ✔Partial
 ✗
 Partial REST
 ✗
 ✔ ✔
 ✔✗ ✗
 Skeleton ✔
 API
 Partial
 ✗
 Full-stack
 project ✗
 Security
 ✔
 Monolithic
 ✗
 ✔
 only
 Skeleton
 ModelSpring
 project High
 Skeleton
 Low ✔
 apps
 ✗
 ✗
 only
 Scope Medium
 Full-stack
 project Monolithic
 LowSkeleton
 only
 Complexity
 Full-stack Spring
 project High
 Low apps
 only M
 ✗ ✔ ✔
 CRUDyLeaf
 Mendix ✗Roo ✗ ✔ CRUDyLeaf
 Mendix
 ✔ ✗ ✔ ✗ ✔ ✔ ✔
 Full-stack ✗
 ✔ High ✗
 Backend (CRUD
 Full-stack only)
 Backend (CRUD
 Full-stack Low
 High only)
 OpenXava Note:Tool
 Partial Mendix =
 ✔
 Full
 Partial
 Spring DSL-Based
 support,
 ✔
 ✗ =
 OpenXava
 ✔
 Spring No
 Partial Roo ✗ View
 support,
 ✔✗
 Partial
 ✔
 ✔Partial
 ✔Partial
 Partial REST ✗
 Partial ✗
 = API
 Note:
 Limited
 ✔✗
 ✔
 ✔or ✔
 Security
 = support,
 component-specific
 ✔
 Partial
 Monolithic Full Spring✗ Model ✗
 ✔
 ✗
 apps = Nosupport.
 Full-stack support, ✗
 Scope
 ✗
 Monolithic
 Medium ✔
 Partial
 Full-stack = Limited
 Spring Low or
 Monolithic
 apps Complexity
 component-specific
 Full-stackHigh
 Spring
 Medium apps suppo M
 JHipster
 Partial
 ✔
 JHipster
 ✗
 Partial
 Bootify.io JHipster
 ✔CRUDyLeaf ✗
 Partial
 ✔
 Bootify.io ✗ ✗ ✗
 ✔✔ ✗
 ✔
 Full-stack
 ✗
 Partial ✗
 ✗
 ✔
 Full-stack High ✗
 ✗BackendFull-stack High
 starter Full-stack
 Backend High
 Medium
 starter M
 CRUDyLeaf
 Mendix ✗
 ✔✔= ✔ Backend
 ✔
 (CRUD ✗ only) Low
 Backend
 Full-stack (CRUD Backend
 only) (CRUD
 High Low only)
 Spring✗Roo CRUDyLeaf
 Partial ✔
 OpenXava Roo
 Partial
 Partial
 Spring Note:✗ ✗ Full
 OpenXava
 Partial
 Spring ✗
 ✗
 Partial support,
 Roo ✗✗
 ✗ ✗ ✔= No✗support,
 ✗Partial
 Partial Note:
 ✗ Monolithic
 ✗
 ✗✗
 ✗ ✔= ✔Full=
 Partial
 Full-stack
 ✗the
 Partial Limited
 support,
 Spring ✗
 ✗
 ✗
 ✗
 apps= NoSpring
 or
 Monolithic component-specific
 support,Low
 Medium ✗
 ✗
 Backend
 ✗
 Monolithic
 appsPartial support.
 Full-stack
 (CRUD = Limited
 Spring only)
 Medium or
 Monolithic
 apps component-specific
 Full-stack Low
 Spring Low
 Medium apps suppo M
 ✗ CRUDyLeaf
 Spring
 Bootify.io
 Partial
 DSL Initializr
 research ✗
 Spring
 eﬀorts✔ ✗
 Initializr
 Bootify.io
 provide ✗ ✗ Partial
 another ✗ ✔
 perspective ✗ Backend
 DSLPartial
 on research ✗starter
 role of✗
 eﬀorts
 DSLs in provide Medium
 low-code
 Backend ✗
 Skeleton
 Backend
 another
 (CRUDand project starter
 perspective
 only)
 Skeleton
 only Backend
 on the
 Low
 project
 role Low
 Medium
 starterofonly
 DSLs in low M
 ✗ Note: ✔ ✔ ✗support, ✗ ✔
 ✗JHipster ✗ Note:✗ ✗✔ =✔ ✗ ✗✗✗ ✔or=✔ ✗ ✗ ✗
 ✗ ✔ ✔ ✔ ✔ ✔
 OpenXava =
 Bootify.io Full
 OpenXava =Partial
 OpenXavaNo support, Partial
 Partial Full Note:
 Limited
 =support, component-specific
 Full
 No support,
 Full-stack support, Partial= No=
 Full-stack Limited
 support,
 support. Low Partial
 or
 Backend Full-stack= Limited
 component-specific
 starter Low support.
 component-specific
 or Full-stack
 Medium Low suppo
 ✗ no-code Spring
 Bootify.io ✗
 JHipster
 Initializr
 (LC/NC) ✗DSL✗ research
 Spring
 development. ✗
 Initializr Slifka
 Partial
 eﬀorts ✗
 and ✗
 Partial
 Pergl
 provide ✗ [27] Skeleton
 no-code✗ DSL✗
 another (LC/NC)
 applied research ✗
 project
 Normalized
 perspective ✗
 only
 development.
 eﬀorts on the provide roleLow
 Systems Skeleton
 Slifka
 Backend
 of ✗
 Theory
 another
 DSLs
 Full-stack
 and project
 Pergl
 starter low-code
 perspective
 in only
 Skeleton
 [27] applied
 on
 Full-stack
 Medium
 andthe project High
 Low ofonly
 Normalized
 role DSLs in Syste
 low
 PartialNote:
 Spring ✔ =✔
 Spring Full
 Initializr
 JHipster RooNote:
 support, ✔ ✔ ✗ = =
 Spring No
 Full
 Partial
 JHipster
 Partial support,
 support,
 Roo Note: ✔✔ ✗ =✔= No
 Full
 Partial
 Partial =
 Partial
 Partialsupport,
 support,
 Limited
 Note: ✗
 ✔ ✗✔or = ✔
 PartialNo
 Full =
 Full-stack Limited
 support,
 support,
 component-specific
 Partial ✗
 ✔ ✗
 Partial
 or = Nosupport.
 =
 component-specific
 support,
 LimitedMonolithic
 Skeleton
 High ✗
 ✔ or
 Partial
 component-specific
 support.
 Full-stack= Limited
 Spring
 project Monolithic
 only appsor component-specific
 support.
 Full-stack LowMedium
 Spring High apps suppo M
 to functional
 Spring Initializr DSLs,
 no-code
 DSL research eﬀorts ✗ provide ✗
 emphasizing
 (LC/NC) modularity
 development.
 another
 DSL research ✗
 and to functional
 sustainability
 no-code
 perspectiveSlifka DSL
 eﬀorts and (LC/NC)
 on the Pergl
 provide DSLs,
 research ✗
 role ofrather than
 emphasizing
 development.
 [27]
 anotherapplied
 eﬀorts
 DSLs in full-stack
 Skeleton
 provide
 perspective
 low-code modularity
 Slifka
 Normalized another gen-
 project
 and
 onand Pergl
 Systems
 the role and
 only
 perspective sustainability
 [27]
 of DSLsapplied
 Theory on in Low
 the role rather
 Normalized
 low-code of DSLs than full
 Syste
 and in low
 OpenXava
 JHipster ✗ OpenXava
 Partial ✗ ✗✔ ✔ ✗ ✗
 ✗ ✔ ✔ a Spring ✗
 ✗✔ ✗
 ✗ Full-stack
 Full-stack Full-stackHigh Low
 Partialeration.
 JHipster
 no-code
 Spring
 Partial
 DSL(LC/NC)
 Roo
 Martínez-Lasaca
 research Partial
 to eﬀorts Spring
 functional
 development.
 DSL
 Partial
 et Roo
 al.
 DSLs,
 provide
 research
 [28] ✔ introduced
 Slifka
 no-code emphasizing
 another
 eﬀorts
 Partial
 DSL and
 Partial
 (LC/NC)Pergl
 provide
 research ✔eration.
 perspective
 Monolithic
 Dandelion,
 no-code DSL
 eﬀorts
 another
 Partial
 functional
 to[27]
 modularity
 development.
 on
 Martínez-Lasaca
 (LC/NC)
 applied perspective
 the
 research
 provide ✔
 graphical
 DSLs,
 and
 Normalized
 role sustainability
 Slifka
 development.
 of
 apps DSL
 emphasizing
 eﬀortsand
 on
 DSLs
 another the
 in
 Medium
 workbench
 etPergl
 al. [28]
 Systems
 provide
 perspective
 low-code
 role
 Monolithic
 Full-stack
 rather
 modularity
 [27]
 Slifka
 of
 introduced
 Theory
 DSLs
 another
 for
 than
 and
 pplied
 onand the
 Spring
 Pergl
 in and
 full-stack
 Normalized
 perspective
 low-code
 role
 apps
 Monolithic
 Dandelion,
 sustainability
 [27]
 of applied
 DSLsgen-
 and
 on
 a
 High Medium
 Spring
 Systems
 the
 in
 graphical
 rather
 Normalized
 low-code
 role of
 apps
 Theory
 DSLs
 DSL
 than
 and
 wor
 full
 Syste
 in low
 M
 ✗ Spring ✔ ✗ ✗ Note: ✗✔ =✔et ✗
 Full al.✗ Note:
 support, ✗ ✗✔ = ✔ Full
 No support,
 support, ✗ ✗
 Partial= No = support,
 Limited ✗ or
 Partial
 component-specific
 = Limited or component-specific
 support. suppo
 industrial
 to
 Spring
 no-code
 OpenXava
 Roo
 Roo
 functional LC/NC
 (LC/NC)
 development,
 eration.
 DSLs,
 no-code
 OpenXava
 Partial
 Partial Martínez-Lasaca
 emphasizing
 development.(LC/NC) to but
 Partial Partial
 modularity
 functional
 no-code
 Slifka
 its
 development.
 and(LC/NC) and
 DSLs,
 Pergl
 industrial
 infrastructure
 [28]
 eration.
 to
 no-code
 Slifka
 [27]introduced
 emphasizing
 functional
 sustainability
 and
 development.
 Full-stack
 Martínez-Lasaca
 applied
 requirements
 LC/NC
 Pergl
 (LC/NC) ✗
 DSLs,
 Normalized
 Slifka
 [27]
 development,
 Dandelion,
 development.
 applied
 andthan
 emphasizing
 modularity
 rather makeet aal.
 Systems
 it
 Monolithic
 graphical
 Pergl [28]
 full-stack
 and
 Lowbut
 less
 Monolithic
 modularity
 Normalized
 Slifka
 [27]
 ight-
 its
 introduced
 Theory
 Full-stack
 Spring
 DSL
 gen-
 sustainability
 and
 pplied
 infrastructure
 Spring apps
 workbench
 Systems
 Pergl and
 apps
 Dandelion,
 rather
 Normalized
 [27]Theory
 Full-stack
 than
 ustainability
 applied
 requirements
 Medium
 Medium
 a
 forSystems Low DSL
 graphical
 rather
 full-stack
 Normalized Theory
 make
 than
 gen- worit
 full
 Syste
 weight.
 Note:
 OpenXava
 OpenXava
 eration. ✔ Chavarriaga
 =Martínez-Lasaca
 Full support,
 industrial ✗
 et al.
 ✗ = et [29]
 No
 LC/NC
 al. proposed
 Note:
 support,
 [28]
 eration. ✔✔=
 ✔introduced Full
 Partial
 development, a = ✗
 JSON-basedweight.
 Limited
 support,
 Martínez-Lasaca Note:
 industrial
 but
 Dandelion,
 eration. ✗✔or
 itsChavarriaga
 DSL
 = etFull
 No LC/NCfor✗
 support,
 support,
 component-specific
 infrastructure
 [28]
 graphical
 aal.and
 Martínez-Lasaca web et
 ✗ al.
 applications,
 Partial
 DSL
 introduced =
 development, et[29] Limited
 support,
 support.
 No=
 requirements
 al. proposed
 workbench
 [28] oﬀering
 butor
 Dandelion, Partial
 Full-stackits
 introduced a
 make JSON-based
 component-specific
 fora = and
 Full-stack Limited
 it
 infrastructureless or
 Dandelion,
 graphical light-
 DSLDSL for
 component-specific
 support.
 ow
 requirements
 Low
 afull-stack
 workbench web
 graphical application
 make
 DSL
 for suppo
 worit
 to functional DSLs, emphasizing
 to functional DSLs,to modularity
 functional
 emphasizing
 DSLand researchDSLs,
 and to emphasizing
 functional
 sustainability
 modularity
 DSL
 eﬀorts DSLs,
 research
 provide rather
 modularity
 sustainability
 emphasizing
 another
 eﬀorts than full-stack
 perspective
 provideand another than
 gen-
 sustainability
 modularity
 rather on full-stack
 role
 theschema
 perspective sustainability
 rather than
 gen-
 of enforcement
 DSLs on in the role
 low-coderather
 of DSLs than
 gen-
 and full
 intolow
 concise
 industrial notation
 LC/NC but
 weight. weaker Note: validation
 Chavarriaga
 development, ✔✔ == Full
 but
 industrial et al.
 its [29]
 support, concise
 proposed
 weight.
 infrastructure
 LC/NCschema ✗ = enforcement
 No notation
 Chavarriaga
 support,
 development,
 industrial a JSON-based but
 compared
 Partial weaker
 et= DSL
 al. [29]
 Limited to
 validation
 for XML.
 web
 proposed
 or Pinho anda
 applications,
 component-specific JSON-based oﬀering DSL
 support. for compared
 web application itX
 eration. Martínez-Lasaca eration. et Note:
 Martínez-Lasaca
 al. [28]
 eration.
 no-code Full support,
 Martínez-Lasaca
 introduced et
 (LC/NC) al. [28] =
 Dandelion,
 eration.
 no-code No
 introduced etLC/NC
 support,
 development.
 requirements
 aal. Partial
 Martínez-Lasaca
 (LC/NC)
 but
 Slifka
 its make
 development,
 =
 introduced
 Dandelion,
 [28]
 graphical Limited
 DSL
 development.
 and
 infrastructure
 etaal.or it
 Pergl component-specific
 [28]
 Dandelion,
 graphical
 workbench less
 Slifka
 [27]
 but its
 light-
 introduced
 DSL infrastructure
 requirements
 for
 pplied
 and aPergl Dandelion,
 graphical
 workbenchsupport.
 [27]
 Normalized
 make
 DSLfor
 applied
 requirements
 a it less light-
 graphical
 workbench
 Systems Normalized Theory
 make
 DSL
 for wor
 Syste
 et al. DSL
 [30] research
 reviewed eﬀorts
 concise usability provide in another
 LC/NC DSL research
 perspective
 platforms, et al. DSL
 eﬀorts on
 [30]
 stressing provide
 research
 the
 reviewed role
 the eﬀorts
 another
 of DSLs
 usability
 importance in
 provide
 perspective
 low-code
 of
 in another
 developer
 LC/NC onand the
 perspective
 platforms,role of DSLs on
 stressing the
 in low-code
 role
 the of DSLs
 importanceand in low
 of
 weight.
 industrial Chavarriaga
 LC/NC development,
 industrial et notation
 . [29]
 LC/NC but
 weight.
 proposed Chavarriaga
 its a
 development,
 industrial
 but weaker infrastructure
 LC/NCvalidation
 JSON-basedconcise
 weight.
 industrial
 development,
 but etitsnotation
 and
 al. schema
 Chavarriaga
 DSL [29]
 LC/NCforproposed
 infrastructure
 requirements but
 web
 but enforcement
 weaker
 etitsal.
 development,a
 make validation
 JSON-based
 [29]
 applications,
 requirements compared
 proposed
 it
 infrastructure oﬀering
 but
 less and
 maketo
 DSL
 its
 light- a schema
 forit
 JSON-based
 requirements XML.
 web
 infrastructure enforcement
 less Pinho DSL
 applications,
 light-
 make for
 it
 requirements compared
 web
 lessoﬀering
 application
 light-
 make to itX
 no-code (LC/NC) development. to functional
 Slifka
 no-code and(LC/NC) DSLs,
 Pergl to[27]
 functional (LC/NC)
 applied
 development.
 no-codeemphasizing DSLs, Slifka
 Normalized emphasizing
 modularityand
 development. Systems
 Pergland sustainability
 modularity
 [27]
 Slifka Theory and
 pplied Pergl and rather
 Normalizedsustainability
 [27] than
 applied full-stack
 Systems rather
 Normalized Theory than
 gen- full
 Syste
 concise notation et al. [30]
 but weaker reviewed DSL
 concise
 validation research
 usability
 DSLet al. and
 notation
 research eﬀorts
 in
 schema et
 LC/NC
 concise
 but
 effortsal.provide
 [30]
 weaker platforms,
 enforcement
 notation another
 reviewed
 validation perspective
 usability
 and
 weaker
 compared
 but stressing to in
 theXML. on
 LC/NC
 validation
 schema the
 importance
 Pinho role
 and
 enforcement of
 platforms, of
 schemaDSLs in
 stressing
 developer
 compared low-code
 enforcement to the
 XML. and
 importance
 compared
 Pinho toofX
 weight. Chavarriagaweight. et al. [29]
 Chavarriaga weight.
 proposed
 eration. JSON-based
 a[29]
 Chavarriaga
 Martínez-Lasaca weight.
 proposed
 eration. etprovide
 Chavarriaga
 DSL
 al. aet
 [29]al.foranother
 JSON-based
 proposed
 Martínez-Lasaca
 [28] web et perspective
 al.
 introducedDSL
 a et[29]
 applications, for
 JSON-based
 al. proposed
 web on
 oﬀering
 Dandelion,
 [28] the
 applications,
 DSL
 introduced arole
 a for of
 JSON-based web
 graphical DSLs
 oﬀering
 Dandelion, in
 DSLDSL low-code
 applications, for
 workbench web
 graphical andapplication
 oﬀering DSL
 for wor
 to functional DSLs, emphasizing no-code to functional
 modularity
 (LC/NC) DSLs,
 and to functional
 development. sustainability
 emphasizing DSLs,
 Slifka modularity
 rather
 and Perglthan
 emphasizing and
 full-stack
 [27] modularity
 sustainability
 applied gen-
 Normalized and than
 sustainability
 rather Systems rathergen-
 full-stack
 Theory than full
 et al. [30] reviewed usability inet
 no-code al.
 LC/NC [30]
 (LC/NC)platforms,
 reviewed et al.
 development.[30]
 stressing
 usability reviewedin
 the LC/NC
 Slifka importance
 usability
 platforms, of
 in LC/NC stressing
 developer the
 platforms, importance
 stressing of
 the developer
 importance toof
 concise notation concise
 eration. Martínez-Lasaca to
 but weakernotation
 et al.
 but
 concise
 validation
 industrial
 [28]
 eration.
 weaker and
 notation schema
 validation
 Martínez-Lasaca
 introduced LC/NC concise
 but
 eration.
 weaker
 industrial
 Dandelion,
 and
 notation
 enforcement
 development, et al.
 schema
 validation
 LC/NC
 Martínez-Lasaca
 graphical
 [28] butand and
 weaker
 enforcement
 compared
 but its
 development,
 DSL
 introduced
 Pergl
 schema
 infrastructure
 workbench
 et al.
 to [27]
 validation
 XML.
 Dandelion,
 [28]
 applied
 enforcement
 Pinho
 compared
 but its
 introduced
 and to
 schema
 requirements
 forrather
 a
 Normalized
 XML.
 infrastructure compared
 enforcement
 Dandelion,
 graphical
 Pinhomake
 DSL
 Systems
 to
 a it
 XML.
 requirements
 workbench lessThe-
 graphical
 Pinho
 compared make
 light- itX
 functional
 ory to DSLs,
 functional emphasizing
 DSLs, emphasizing modularity modularityand sustainability
 and sustainability than
 rather full-stack
 than gen- for
 full-stack
 DSL wor
 et al. [30] reviewed et al. [30]
 usability reviewed inet al.
 LC/NC
 weight. usability
 [30] platforms,
 reviewed
 Chavarriaga in et al.
 LC/NC
 weight. usability
 stressing
 [30]
 et reviewed
 platforms,
 [29]
 Chavarriaga
 al. in
 the LC/NC
 proposedimportance
 stressing
 usability
 platforms, the
 in
 of importance
 LC/NC stressing
 developer of
 the
 platforms, stressing
 importance
 developer of
 thewebdeveloper
 importance of
 industrial LC/NC development, eration. but
 industrial its
 Martínez-Lasaca LC/NC development,
 industrial
 infrastructure et al. [28] LC/NC
 requirements
 introducedbut etits al.
 development, [29]
 JSON-based
 Dandelion,
 proposed
 it
 infrastructure
 make buta its
 less DSL
 light- ainfrastructure
 JSON-based
 for
 requirements
 graphical
 web
 DSL
 applications,
 DSL
 make requirements
 workbench
 for
 it lessoﬀering
 application
 forlight- make it
 generation. Martínez-Lasaca et al. [28] introduced Dandelion, a graphical DSL work-
 weight. Chavarriaga et al.industrial [29] concise
 weight.
 proposed notation
 a JSON-based
 Chavarriaga but
 concise
 weight. weaker
 et notation
 al.
 Chavarriaga
 DSL [29] validation
 for but
 proposed
 web et and
 weakeral.a [29]
 JSON-based
 applications, validation
 schema proposed oﬀering and
 enforcement
 DSL a schema
 JSON-based
 for compared
 web enforcement
 make DSL
 applications, toforXML.web Pinho
 compared
 oﬀering
 application to X
 bench et forLC/NC
 al. industrial
 [30]
 development,
 reviewed etLC/NC
 al. [30]
 usability
 but
 development,
 reviewedin
 its
 LC/NC
 infrastructure
 but
 usability
 platforms, LC/NC
 requirements
 itsininfrastructure
 stressing platforms,requirements
 the importance
 stressing
 it lessmakeof
 the
 light-
 it less
 developer
 importance
 concise notation but weaker validation
 weight. concise
 Chavarriaganotation
 and schemaetbut
 concise
 al. weaker
 enforcement
 [29]etnotation validation
 proposed but and to
 a weaker
 compared
 JSON-based schema XML.
 validation DSL Pinho and
 enforcement
 for webschema compared
 enforcement
 applications, tooﬀering
 XML. Pinho toof
 compared X
 lightweight. Chavarriaga al. [29] proposed a JSON-based DSL for web applications,
 et al. [30] reviewed usability concise inet LC/NC
 al. [30]
 notation platforms,
 reviewed et al. [30]
 usability
 stressing reviewedin
 the importance
 LC/NC platforms,
 usability in
 of developer
 LC/NC stressing platforms,
 the importance
 stressing of
 the developer
 importance of
 offering concisebut weakerbut
 notation validation
 weaker validation and schema and enforcement
 schema enforcement comparedcompared to XML. Pinho to XML.
 et Pinho
 al. [30]etreviewed usability in LC/NC platforms,
 al. [30] reviewed usability in LC/NC platforms, stressing the importance of devel- stressing the importance of developer
 oper experience and accessibility. Dalibor et al. [31] investigated DSL-driven customization
 of LC/NC platforms for digital twins, demonstrating adaptability but reinforcing the
 domain-specific nature of many DSL efforts.
 Collectively, these studies elucidate both the potential and the constraints of contem-
 porary DSL and low-code/no-code methodologies, thereby establishing the foundation for
Appl. Sci. 2025, 15, 10621 5 of 35

 our comprehensive assessment of existing frameworks. The review of existing frameworks
 shows that while many tools simplify development, they often lack integrated security,
 view generation, and transparent design-to-code traceability. In parallel, recent DSL re-
 search underscores the central role of DSLs in advancing low-code and no-code platforms,
 but these efforts are either domain-specific or limited in scope, making them less applicable
 to lightweight educational contexts. Together, these observations highlight the need for
 a general-purpose DSL-driven framework that combines the strengths of low-code tools
 with the rigor and transparency of DSLs.
 To address the recurring gaps observed in existing tools and DSL research, the design
 of XBoot was guided by the following requirements:
 RQ1: Enable full-stack generation from a single XML DSL specification.
 RQ2: Provide built-in security with role-based access control.
 RQ3: Support generation of both REST APIs and server-rendered Thymeleaf views.
 RQ4: Ensure transparent, traceable Spring Boot code aligned with best practices.
 The development of the XML-based DSL, which forms the foundation of XBoot, was
 directly informed by these requirements, as will be discussed in the following section.

 3. Engineering Process of the XML-Based DSL
 The XML-based DSL at the core of XBoot was engineered following established practices
 in DSL and model-driven engineering [2]. The process comprised four stages: domain
 modeling, XML syntax design, schema formalization, and processor implementation. This
 provided a disciplined path from requirements analysis to the implementation of a working
 tool, ensuring that the language was both technically sound and pedagogically suitable. In
 the paper, this structured process provides the foundation for the subsequent Sections 4 and 5,
 which elaborate the architectural perspective of XBoot and detail the DSL design and code
 generation process.

 3.1. Domain Modeling
 The process began with domain modeling, where the essential concepts of Spring Boot
 applications were identified. These included entities and their fields, relationships between
 entities, repositories for persistence, services for business logic, controllers for interaction
 handling, views for user interface pages, and routes for navigation and interaction between
 components. Security requirements were also considered, with roles representing access
 control responsibilities.
 This stage also incorporated educational requirements, as XBoot is intended for both
 professional prototyping and instructional use. Readability, simplicity, and verifiability
 were prioritized, ensuring that learners can quickly understand how domain concepts map
 to generated artifacts, while instructors can validate student specifications against clear
 structural rules.
 The result of this stage was a domain model capturing the recurring concepts and
 relationships of a typical Spring Boot application, enriched with educational considerations.

 3.2. XML Syntax Design
 Once the domain model was established, the next step was to define the DSL’s concrete
 syntax in XML. Each domain concept was mapped to an XML element or attribute. For example:
 <Entity> elements capture domain objects.
 <Field> elements define entity attributes, with attributes such as name and type.
 <Relation> elements represent associations (e.g., one-to-many, many-to-many).
 <Role> elements specify access control roles.
 <Route> elements describe navigational paths and associated views.
Appl. Sci. 2025, 15, 10621 6 of 35

 This mapping establishes the link between abstract syntax (concepts) and concrete
 syntax (notations). XML was chosen because of its familiarity, machine-readability, and
 support in common development tools. It provides a structured format that can be easily
 parsed and validated, while remaining accessible to learners.

 3.3. XSD Formalization
 To ensure correctness and enforce constraints, an XML Schema Definition (XSD) was
 created. The schema defines:
 • Which elements are allowed (e.g., <Entity>, <Field>, <Relation>, <Role>, <Route>).
 • Cardinalities (e.g., an <Entity> must have one or more <Field> elements).
 • Attribute constraints (e.g., type in <Field> must match a predefined set of data types).
 • Nesting rules (e.g., <Relation> must reference valid <Entity> names).
 Schema-based validation [32] ensures that any DSL specification is structurally correct
 before processing. This reduces runtime errors in code generation and provides users with
 immediate feedback if their model is incomplete or inconsistent. The use of XSD also improves
 verifiability and supports tool-assisted editing in IDEs that understand XML schemas.

 3.4. Processor Implementation
 The final stage was the implementation of a processor that parses valid XML speci-
 fications and transforms them into Spring Boot code. A Java-based parser interprets the
 XML input, builds an internal representation of the model, and passes it to modular code
 generators. Each generator corresponds to one application layer, some of which are:
 • EntityGenerator: creates annotated Java entity classes.
 • RepositoryGenerator: produces Spring Data JPA repositories.
 • ServiceGenerator: generates service classes with CRUD and domain logic.
 • ControllerGenerator: builds REST and MVC controllers.
 • ViewGenerator: generates Thymeleaf templates for server-side rendering.
 • SecurityGenerator: configures role-based access control.
 These generators apply model-to-text transformation patterns [2], producing traceable,
 standard Spring Boot artifacts. The modular design supports separation of concerns [10],
 as each generator is independent and can evolve without affecting others. This also ensures
 extensibility, allowing future generators (e.g., for APIs, messaging, or external integrations)
 to be added incrementally.
 The processor thus serves as the bridge between DSL specification and executable
 Spring Boot code, completing the engineering lifecycle.

 4. Architectural Overview of XBoot
 XBoot is a lightweight modular framework designed to generate secure Spring Boot
 application prototypes using a model-driven approach. In contrast to black-box low-code
 tools, XBoot prioritizes architectural transparency, traceability, and alignment with the
 best practices in layered backend development. The framework transforms a compact
 XML-based specification into a fully runnable Spring Boot application through a structured
 toolchain comprising the following core components:
 1. XML-based DSL: Developers specify the application architecture using a structured
 DSL. This includes the definitions of entities, fields, controllers, routes, validation
 constraints, access roles, and view mappings.
 2. XSD Schema Validator: XML is validated against a dedicated XSD schema to enforce
 structural correctness, tag constraints, and data type compatibility. This ensures
 real-time error detection and improves the IDE integration.
Appl. Sci. 2025, 15, 10621 7 of 35

 3. Java-based DSL Parser: A custom parser maps DSL elements (e.g., <Entity>, <Field>,
 <Validation>, <Route>, <Connector>) to an internal object model. This model pre-
 serves entity relationships, validation rules, and security mappings to ensure accurate
 code generation.
 4. Spring Boot Code Generator: Based on the internal model, XBoot generates a complete
 executable backend project that includes the following:
 • JPA entity classes with validation annotations.
 • Repositories extending JpaRepository.
 • Service classes encapsulating business logic.
 • REST controllers with route and role-based access control.
 • View controllers for form rendering and data listing.
 • Thymeleaf templates with Bootstrap 5 styling and validation error rendering.
 • Spring Security configuration for enforcing role-based access.
 • Swagger configuration and annotations (@Api, @ApiOperation) for documenting
 and testing REST APIs.
 • Project metadata (e.g., pom.xml, application.properties, and MainApp entry point).
 Collectively, these generated artifacts constitute an integrated toolchain encompass-
 ing all backend layers, as depicted in Figure 1. This toolchain not only visualizes the
 flow of transformations but also illustrates how the design requirements (RQ1–RQ4) are
 operationalized across components.

 Figure 1. XBoot toolchain for generating Spring Boot applications from DSL specifications.

 The alignment between the research questions and the architectural components
 underscores the systematic design of XBoot. Specifically, the XML DSL, Validator, and
 Parser together address RQ1 by facilitating unified full-stack generation. The Parser
 and Code Generator address RQ2 by maintaining role definitions and producing secure
 controllers with Spring Security. Furthermore, the Code Generator’s outputs for REST
 controllers and Thymeleaf templates correspond to RQ3. Finally, the adoption of standard
 Spring Boot conventions in entities, services, and configuration files ensures RQ4. These
 mappings are detailed in Table 2.
Appl. Sci. 2025, 15, 10621 8 of 35

 Table 2. Mapping of research questions (RQ1–RQ4) to XBoot architectural components.

 Research Question Requirement Architectural Support in XBoot
 XML DSL block provides the model; XSD Schema Validator ensures correctness;
 RQ1 Full-stack generation from a single XML DSL XML Parser transforms into an internal model; Code Generator produces Java
 classes, Thymeleaf templates, configuration files
 XML Parser preserves role definitions; Code Generator outputs secure REST
 RQ2 Built-in security with role-based access control
 controllers, Spring Security configuration, and supporting metadata (e.g., pom.xml)
 Code Generator produces REST controllers with Swagger annotations and
 RQ3 Generation of both REST APIs and Thymeleaf views
 Thymeleaf templates for forms and listings
 Code Generator outputs JPA entities, repositories, services, and configuration files
 RQ4 Transparent, traceable Spring Boot code
 (application.properties, pom.xml) using standard Spring Boot conventions

 As delineated in Table 2, the architectural components of XBoot collectively address
 the identified research questions, thereby ensuring comprehensive full-stack generation,
 integrated security, view support, and traceable code. While this systematic mapping
 underscores the rigor of XBoot’s design, effective utilization of the DSL necessitates support
 for students and novice developers who may encounter difficulties with XML syntax and
 modeling conventions. To address this challenge and further enhance usability, XBoot is
 supplemented by a custom-trained GPT-based assistant, XBoot GPT [33]. This language
 model is fine-tuned to understand backend development concepts and can translate infor-
 mal system descriptions into valid XBoot DSL code. Students and developers can interact
 with XBoot GPT to rapidly bootstrap their models, reducing time spent on DSL syntax and
 structure. Importantly, the generated XML is still validated and transformed by the core
 XBoot generator, ensuring traceability, determinism, and architectural consistency.

 5. DSL Design and Code Generation Process
 The design of XBoot is guided by the principles of modularity, traceability, and security-
 by-design. These principles are implemented using a structured XML-based DSL and
 a layered code generation pipeline. Unlike traditional low-code environments, XBoot
 leverages textual DSL to promote structural clarity and customization. This approach
 aligns with emerging frameworks that propose DSL extensibility as a pathway to complete
 no-code solutions [34]. This section outlines the core elements of the DSL and how they
 drive the automated creation of Spring Boot applications.
 XBoot’s DSL supports both structural (e.g., entities, fields, relationships) and be-
 havioral modeling (e.g., controllers, routes, roles). Developers use a single XML file to
 describe the entire application architecture, which reduces repetitive code and improves
 architectural consistency across all layers.

 5.1. DSL Structure and Modeling Semantics
 At the heart of XBoot is a structured XML DSL that defines the static and dynamic
 aspects of the application. Tags such as <Entity>, <Field>, <Controller>, <Connector>,
 <Route>, and <Validation> are used to capture the domain models, access roles, API paths,
 and field-level constraints.
 Each XML specification was validated against an XSD schema to ensure well-
 formedness and design correctness. This schema-aware modeling approach supports
 both auto-completion and early error detection in modern integrated IDEs. Table 3 outlines
 the main DSL tags and attributes allowing for fine-grained input constraint modeling at
 the field level.
Appl. Sci. 2025, 15, 10621 9 of 35

 Table 3. XBoot DSL Tags and Attributes.

 Tag Attribute Allowed Values/Format Description
 Defines the application name and serves as the root element of
 <Application> name String (e.g., StudentCourses)
 the XML document.
 <Entity> name String It declares a persistent domain class.
 <Field> name String Name of entity field.
 type String, Integer, Date, etc. Data type of the field.
 required true, false Indicates whether the field is mandatory.
 relation OneToMany, ManyToOne, ManyToMany Defines the relationship with another entity.
 <Validation> type NotBlank, NotNull, Size, Pattern, Email Type of validation constraints.
 min, max Integer Used with Size to define the length bounds.
 regex Java-compatible regex (e.g., \\d{10}) The pattern is used to enforce the input format.
 <Service> name String (optional) Name of the service class (automatically generated if omitted).
 <Controller> name String Name of the controller.
 for Matches <Entity> name This indicates which entity the controller handles.
 <Repository> name String (optional) Name of the repository interface (auto-generated if omitted).
 <Connector> from, to Names of controller and entity Secured interaction between components.
 role ADMIN, USER, etc., (comma-separated) Roles authorized to use connectors.
 type REST, MVC, async, secured Communication style and access type
 <View> for Name of entity or controller Indicates the subject for which the view was generated.
 template e.g., form.html, list.html Thymeleaf HTML template to render.
 <Route> path e.g.,/students,/register Defines the URL path.
 view View name (must match template) View to render this route.
 method GET, POST, PUT, DELETE HTTP method to handle.
 role USER, ADMIN, etc. Role required to access the route.
 controller Name of controller The route to the backend controller is mapped.

 This DSL supports both functional unit modeling (entities, repositories, and services)
 and interaction modeling (routes and access roles). For example, the following snippet in
 Box 1 defines an enrollment entity with two relationships.

 Box 1. XML-DSL Definition of the Enrollment Bridge Table.

 <Entity name="Enrollment">
 <Field name="student" type="Student" relation="ManyToOne"/>
 <Validation type="NotBlank"/>
 <Validation type="Size" min="3" max="10" message="Student name must be be-
 tween 3 and 10 characters"/>
 <Field name="course" type="Course" relation="ManyToOne"/>
 <Field name="grade" type="String"/>
 </Entity>

 The simplicity of this definition belies the complexity of the backend components it
 generates: JPA annotations, repository interfaces, controller endpoints, view templates, and
 security layers.
 For standardization and future extensibility, we formally defined the core syntax
 of the XBoot DSL using the Extended Backus-Naur Form (EBNF) [32], as outlined in
 Appendix A.2. This grammar captures both functional unit modeling, including entities,
 repositories, and services, and interaction modeling, such as routes and role-based access
 definitions. This facilitates precise tooling, such as syntax validation and DSL-aware
 editors, enables schema evolution tracking through formal diffs, and supports integration
 with parser generators and language workbenches. Moreover, clearly defined grammar
 enhances the future portability of DSL and its adoption by third-party tools or educational
 environments, where consistent interpretation of models is critical.

 5.2. Security and Role-Based Connectors
 XBoot treats security as a first-class concern by embedding role-based access control
 (RBAC) directly into the system architecture. The <Connector> and <Route> elements
 support a role attribute that declaratively defines the user roles that can access a given path
Appl. Sci. 2025, 15, 10621 10 of 35

 or service. These access rules are automatically translated into Spring Security annotations
 (e.g., @PreAuthorize) or configuration entries to ensure consistency across the codebase.
 This architectural embedding of access control aligns with the concept of secure
 connectors [35], where interactions between components are governed by structure and
 verifiable security constraints. For instance, Box 2 elucidates the interface connecting the
 controller and service layers of the application:

 Box 2. Connector Definition between Controller and Service layers.

 <Connector from="EnrollmentController" to="EnrollmentService" role="AD-
 MIN,MANAGER"/>
 <Route path="/enrollments" view="list" role="USER" controller="Enroll-
 mentController"/>

 This model eliminates the need to manually define and synchronize access control
 policies in scattered controllers or configuration files. It also enables traceable changes;
 when a role is updated in the DSL, all related access points are regenerated consistently.

 5.3. Code Generation and Traceability
 XBoot enforces model-to-code traceability by treating DSL as a single source of truth.
 Every entity, field, route, and validation rule defined in the XML specification is faithfully
 reflected in the generated backend code, thereby ensuring consistency across all layers
 of the application. For instance, the DSL snippet presented in Box 3 specifies a title field
 within the course entity, accompanied by a validation constraint.:

 Box 3. DSL Definition of Validation on the Title Element.

 <Entity name="Course">
 <Field name="title" type="String" required="true">
 <Validation type="NotBlank"/>
 <Validation type="Size" min="3" max="100" message="Title must be be-
 tween 3 and 100 characters"/>
 </Field>
 <Field name="description" type="String"/>
 </Entity>

 From this DSL fragment, XBoot generates various classes across different layers. Some
 examples are:
 • JPA Entity (Course.java) with its validations is shown in Box 4.

 Box 4. Generated JPA Entity (Course.java) with Validations.

 @NotBlank
 @Size(min = 3, max = 100, message = "Title must be between 3 and 100 char-
 acters")
 private String title;
 private String description;

 • Thymeleaf form template (course-form.html) is shown in Box 5.:
Appl. Sci. 2025, 15, 10621 11 of 35

 Box 5. Generated Thymeleaf Template with Validation.

 <input type="text" th:field="*{title}" class="form-control"/>
 <div th:if="${#fields.hasErrors('title')}" th:errors="*{title}"

 • REST controller for course management (CourseController.java) is given in Box 6.

 Box 6. Generated REST Controller for Course Management.

 @Api(tags = "Course")
 @RestController
 @RequestMapping("/courses")
 public class CourseController {

 @ApiOperation("Create a new course")
 @PostMapping
 public ResponseEntity<Course> saveCourse(@Valid @RequestBody Course
 course) {
 return ResponseEntity.ok(courseService.saveCourse(course));
 }
 }

 This example demonstrates how a single field definition in the DSL propagates across
 multiple architectural layers:
 • To the data model: The DSL specification is translated into Java code within the entity
 class, where validation constraints (such as @NotBlank and @Size) are directly applied
 to fields. These annotations ensure that invalid data are rejected early at the persistence
 or controller layer, preserving data integrity and reducing the need for manual checks.
 • To the view layer: The corresponding Thymeleaf form is automatically generated
 with th:field bindings linked to the entity fields. Validation messages are displayed
 in context using th:errors, providing immediate and localized feedback to the user.
 This ensures that the client-side and server-side validations are aligned and easy
 to maintain.
 • To the REST API: The REST controller generated by XBoot includes the appropriate
 method for creating or updating the entity. Swagger annotations (@Api, @ApiOpera-
 tion) document the endpoint clearly, while @Valid ensures that any request payload
 adheres to the validation rules defined in the DSL. This leads to consistent runtime
 behavior and transparent API contracts for clients.
 Together, these mappings reflect the core benefit of XBoot’s design: complete traceabil-
 ity from the design to the implementation. When a developer updates the DSL, by adjusting
 a constraint, renaming a field, or adding a new entity, those changes are automatically
 reflected across all affected layers. This eliminates boilerplate, prevents configuration drift,
 and reinforces architectural understanding. In instructional settings, this transparency
 helps learners observe how a high-level model drives consistent changes across the back-
 end, reinforcing their understanding of the separation of concerns, validation propagation,
 and layered architecture, thereby making XBoot an effective teaching and prototyping tool.
 To further clarify how XBoot enforces traceability across layers, Figure 2 maps key
 elements of the XML-based DSL to the corresponding backend components generated
Appl. Sci. 2025, 15, 10621 12 of 35

 by the system. This visual representation demonstrates how a single source of truth
 translates into concrete application artifacts, such as JPA entities, service classes, REST
 controllers, Thymeleaf views, and role-based access control policies. By making these
 mappings explicit, the figure reinforces XBoot’s pedagogical value in showing students
 how high-level specifications propagate across architectural layers. This traceability not
 only ensures consistency and maintainability but also aids in teaching layered design,
 validation propagation, and secure software construction.

 Figure 2. Mapping DSL to Generated Artifacts.

 6. Security Modeling and Access Control
 Security in multi-user web applications must be designed from the ground up to
 ensure that users only access data and actions for which they are authorized. XBoot embeds
 RBAC directly into the architectural model using declarative tags within the DSL. This
 ensures that security concerns are not treated as an afterthought but are defined alongside
 the core application logic.
 XBoot supports access control through two primary DSL constructs:
 • <Route> which governs the view level and endpoint access.
 • <Connector> which controls the component-level communication and service access.
 Together, these tags allow developers to define fine-grained access policies for both
 front-end views and back-end services.

 6.1. Route-Based Access Control
 The <Route> element defines a navigational path within the application and specifies
 the user roles allowed to access it. Each route entry includes the following:
 • A URL path (path).
 • The HTTP method (method).
 • The view template (view) rendered.
 • The controller handling the route (controller).
 • The authorized role(s) (role).
 For example, the following DSL snippet in Box 7 defines which user roles have
 permission to access specific views or REST endpoints.
Appl. Sci. 2025, 15, 10621 13 of 35

 Box 7. XML-DSL RBAC Definition for Application Users (USER/ADMIN).

 <Route path="/students" view="student-list" method="GET" controller="Stu-
 dentController" role="USER"/>
 <Route path="/enrollments/new" view="enrollment-form" method="POST" con-
 troller="EnrollmentController" role="ADMIN"/>

 These DSL entries are translated as follows:
 • Controller methods are annotated with @PreAuthorize to enforce access at runtime.
 • Spring Security configuration that maps HTTP paths to the required roles.
 • Thymeleaf conditionals for selectively rendering view elements based on the user role.
 The code snippet included in the generated view controller code is presented in Box 8.

 Box 8. Generated Post Method for the Enrollments Controller.

 @PreAuthorize("hasRole('ADMIN')")
 @PostMapping("/enrollments/new")
 public String saveEnrollment(@ModelAttribute Enrollment enrollment) {
 enrollmentService.saveEnrollment(enrollment);
 return "redirect:/enrollments";
 }

 The corresponding Thymeleaf template (enrollment-list.html) shown in Box 9 will include
 a conditional “Add Enrollment” link generated only for users with the ADMIN role.

 Box 9. Generated Thymeleaf Snippet (enrollment-list.html) with Conditional Role-Based Link.

 <a th:if="${#authorization.expression('hasRole(''ADMIN'')')}"
 th:href="@{/enrollments/new}" class="btn btn-primary">
 Add Enrollment
 </a>

 This layered enforcement ensures that even if a user bypasses the UI, unauthorized
 POST requests are rejected at the controller level. The consistent translation of DSL-defined
 roles into both backend and frontend layers reinforces access integrity and reduces the
 likelihood of security oversights. The corresponding RBAC configuration class generated
 is listed in Appendix A.3. Backend access control is strictly enforced via Spring Security
 annotations (e.g., @PreAuthorize), ensuring that role-based restrictions are consistently
 applied across the application.

 6.2. Component-Level Access with Connectors
 While <Route> secures navigation and endpoints, the <Connector> tag secures the
 interactions between components, such as between controllers and domain models. This
 design is influenced by the secure connector paradigm proposed by Shin et al. [35], where
 security semantics are embedded into the system’s interaction logic. Each connector
 includes the following:
 • The source component (typically a controller).
 • The destination component (usually an entity or service).
Appl. Sci. 2025, 15, 10621 14 of 35

 • The permitted role(s).
 • The connector type (REST, MVC, async, etc.).
 An example DSL specification of a connector is shown in Box 10.

 Box 10. DSL Snippet Defining a Connector with Role and Type.

 <Connector from="EnrollmentController" to="Enrollment" role="USER"
 type="REST"/>

 This connector declares that the EnrollmentController is allowed to access the Enrollment
 entity using RESTful operations on behalf of users with the USER role. The generator
 translates this into method-level annotations and path restrictions to ensure that only
 authenticated users with the right role can trigger those interactions. If a controller is
 linked to an entity through a secure connector, all corresponding controller methods are
 consistently protected.

 6.3. Generated Security Configuration
 In the current implementation of XBoot, Spring Security is configured to load user cre-
 dentials and role assignments from the application.properties file. This approach intentionally
 avoids hardcoding sensitive data within Java classes and enables straightforward externaliza-
 tion of authentication details. As a result, developers and instructors can update usernames,
 passwords, and roles without touching the Java source code, which streamlines testing and
 credential rotation in both educational and lightweight production environments.
 The XBoot generator produces two key security artifacts:
 • A SecurityConfig.java class that maps HTTP paths to role-based access rules using
 standard Spring Security constructs.
 • An application.properties file that includes pre-encoded credentials and associated
 role assignments for predefined users.
 An excerpt of the generated SecurityConfig.java class is shown in Box 11.
 Box 11. Generated Security Configuration (SecurityConfig.java).

 http
 .authorizeHttpRequests(auth -> auth
 .requestMatchers("/students").hasRole("USER")
 .requestMatchers("/enrollments/new").hasRole("ADMIN")
 .anyRequest().authenticated()
 )
 .formLogin()
 .httpBasic();

 An excerpt of the generated application.properties file with predefined users is shown
 in Box 12.
 This configuration supports both form-based login for web interfaces and HTTP
 basic authentication for RESTful access, making it adaptable for classroom environments,
 API testing tools like Postman, and automated clients. By externalizing credentials in
 the application.properties file, XBoot promotes maintainability and adheres to secure
 development practices.
Appl. Sci. 2025, 15, 10621 15 of 35

 Crucially, this setup reflects the DSL-driven model: role attributes defined in <Route>
 or <Connector> are automatically translated into Spring Security configurations, ensuring
 consistent enforcement across controllers and views. This declarative, end-to-end approach
 simplifies application security while providing the transparency and structure necessary
 for instructional use and real-world development.

 Box 12. Generated Application Properties with Predefined Users (application.properties).

 # Security: In-memory users
 app.security.user.username=user
 app.security.user.password=password
 app.security.user.roles=USER

 app.security.admin.username=admin
 app.security.admin.password=password
 app.security.admin.roles=ADMIN,USER

 7. Case Study and Evaluation
 The evaluation of XBoot was conducted through two complementary modes. First,
 the authors validated the tool by manually specifying and generating two different ap-
 plications to ensure correctness and completeness. Second, a preliminary usability study
 was conducted with 10 undergraduate students who had previously completed formal
 coursework in Spring Boot and Java programming. The students participated under
 two conditions: four remotely and six in class under direct supervision. In both settings,
 XBoot GPT was employed to generate DSL specifications from natural language descrip-
 tions. The study was designed to evaluate XBoot’s practical usability, generation accuracy,
 and educational impact within realistic academic contexts.

 7.1. Author’s Evaluation of XBoot Fidelity
 The first case study models a university registration system comprising three entities:
 Student, Course, and Enrollment entity. These were defined in the DSL with attributes,
 validation rules, and relational constraints (e.g., foreign key references). For example,
 Enrollment includes a composite structure referencing both Student and Course. The
 application models three core entities: Student, with fields such as name, email, and mobile;
 Course, with a title and optional description; and Enrollment, which links students to
 courses and optionally stores a grade. This mirrors a normalized many-to-many schema,
 where many students can register for many courses via an intermediary entity that can
 also store additional contextual data like grades. The relationships are encoded using
 “ManyToOne” mappings from Enrollment to both Student and Course, which XBoot
 correctly decomposes into two one-to-many relationships. The DSL also specifies access
 roles, routes, and component interactions.
 A partial specification is shown below in Listing 1 (with the full listing included in
 Appendix A.4.).
 This DSL acts as a single source of truth for the system architecture, encapsulating
 both the structure (entities, fields, relationships) and behavior (routes, roles, access control).
 Each DSL element is mapped to specific backend components, as outlined in Section 4. The
 execution log is provided in Appendix A.1., which shows all the steps and artifacts generated.
Appl. Sci. 2025, 15, 10621 16 of 35

 Listing 1. XBoot DSL representation for the Student–Course case study.

 <Application name="StudentCourses">
 <!-- Entities -->
 <Entity name="Student">
 <Field name="name" type="String" required="true">
 <Validation type="NotBlank"/>
 …..
 <!-- Controllers -->
 <Controller name="StudentController" for="Student"/>
 <!-- Routes -->
 <Route path="/home" view="home" method="GET" role="USER"/>
 <Route path="/students" view="student-list" method="GET" controller="Stu-
 dentController" role="USER"/>
 …..
 <!-- Security Connectors -->
 <Connector from="StudentController" to="Student" role="USER"
 type="REST"/>
 <Connector from="CourseController" to="Course" role="USER" type="REST"/>
 " type="REST"/>
 …..
 </Application>

 Passing the DSL to the XBoot toolchain produced a fully functional Spring Boot project
 with the following outputs, as shown in Table 4:

 Table 4. Case Study Generated Artifacts.

 Layer Artifacts Generated
 Model Layer JPA entity classes with field-level validation annotations (@NotBlank, @Size)
 Repository Interfaces extending JpaRepository for each entity
 Service Layer Service classes exposing entity operations (e.g., saveStudent, findAllCourses)
 Controller Layer REST and view controllers, annotated with Swagger and Spring Security
 View Layer 7 Thymeleaf templates: 2 per entity (form, list) + 1 homepage (home.html)
 Security SecurityConfig.java, application.properties with roles, routes, login config
 Documentation Swagger UI enabled via @Api, @ApiOperation, and OpenAPI integration

 This shows that XBoot successfully transforms a compact DSL into a complete,
 runnable, secure, and structured web application without manual coding. A total of
 7 Thymeleaf templates were generated: six for data insertion and listing (two per en-
 tity), and one homepage view (home.html). The generated web application compiled and
 ran without errors and required no manual edits for handling student entry, listing, and
 enrollment in various courses’ functionality.
 Several screenshots of the generated pages are provided below for demonstration
 purposes. Figure 3 shows the student’s registration form at the following route: illustrating
 validation messages due to missing entries in the email and mobile number.

 Figure 3. Generated Student details Entry form.
Appl. Sci. 2025, 15, 10621 17 of 35

 Once the full details are entered correctly, the details are shown in the student-list.html
 page at route: as shown in Figure 4.

 Figure 4. Student listing page with edit and delete capability.

 Corresponding pages are also generated for the Course entity (entry form and list-
 ing), as shown in Appendix B.1. Since the Student–Course relationship is many-to-many,
 an Enrollment bridge table is used to capture this association. The Enrollment form
 (Appendix B.2.) allows users to register students in courses by selecting from drop-down
 lists of existing entries. The resulting enrollment records are displayed in the enrollment-
 list.html view (Appendix B.3.), which lists all students enrolled in courses.
 The simplicity of the user interface is intentional, as the primary goal of this study
 is to demonstrate XBoot’s ability to generate fully functional backend applications from
 a high-level specification. Visual styling and branding are outside the current scope but
 can be easily incorporated into the Thymeleaf generator in future enhancements.
 Figure 5 provides a visual overview of the generated application architecture, illustrating
 how the DSL model is propagated across backend layers including the entity, service, repos-
 itory, controller, and view tiers alongside security and API documentation configurations.

 Figure 5. Generated StudentCourse Spring Boot application.
Appl. Sci. 2025, 15, 10621 18 of 35

 To further test generality, we specified a flight reservation system DSL (given in
 Appendix A.5.) comprising four entities: Passenger, Airplane, Flight, and Reservation. Each
 entity includes diverse field types, validation constraints, and inter-entity relationships,
 e.g., Reservation defines ManyToOne links to Flight, Passenger, and Airplane. The valida-
 tion rules include patterns, ranges, and email formats.
 Despite the domain shift and slight increase in complexity, XBoot generated the
 complete backend stack from the DSL without requiring changes to the generator. The
 generated application includes the same set of classes and files as in the previous case study,
 with differences in counts and details. This confirms XBoot’s capacity to handle larger
 relational models across varied application domains with consistent generation quality.
 The evaluation of the StudentCourses and FlightBooking case studies demonstrated
 that XBoot reliably transforms compact, declarative specifications into complete, secure,
 and modular Spring Boot applications. These examples highlight the expressive power
 of the DSL and the generator’s ability to produce all backend layers (entities, services,
 repositories, controllers, views, and security configurations) automatically and without
 manual intervention. The consistency of results across distinct domains reinforces XBoot’s
 strengths in modular architecture, traceability, and security enforcement. As such, XBoot
 proves to be a valuable tool for instructional use, model-driven engineering, and rapid
 prototyping, where reducing boilerplate and preserving architectural consistency are key
 to success. Table 5 lists the different metrics resulting from the case studies.

 Table 5. Summary of Evaluation Metrics.

 Metric StudentCourses FlightBooking
 DSL Entities 3 4
 Total Fields 11 22
 Controllers (REST + View) 6 8
 Services and Repositories 6 8
 Thymeleaf Views 7 9
 Protected Routes 6 5
 Swagger-Documented Endpoints 6 5
 Java + HTML Lines of Code ~950 ~1350
 Time to Build Manually (on average) ~45 min ~60 min
 Time Using XBoot (on average) -from typing
 ~5 min ~5 min
 specification in XBoot GPT to running application

 Manual development times were obtained by both authors independently imple-
 menting the full applications by hand; the reported values represent the average of their
 efforts. In parallel, the same applications were generated using XBoot during the evaluation
 study, with average end-to-end times (from specification entry in XBoot GPT to a running
 application) of approximately five minutes.
 The prototype was evaluated against the core design goals of XBoot, including mod-
 ularity, transparency, security integration, educational effectiveness, and prototyping ef-
 ficiency. The evaluation involved applying XBoot to both case studies and assessing the
 generated artifacts against each objective. The results of this assessment are summarized in
 Table 6, which highlights how well XBoot meets its intended design principles.

 Table 6. Summary of XBoot Design Goals Evaluation.

 Criterion Evaluation
 Modularity Each concern (entity, service, controller, and view) was generated separately and mapped via DSL, as shown in Figure 2.
 Transparency Every code artifact is traceable to the DSL tag. No hidden logic or dependencies were observed.
 Security Integration Connectors and routes encode roles that are translated into Spring Security annotations.
 Educational Utility The generated code serves as a clean template for teaching standard Spring Boot architecture and security.
 Prototyping Fidelity The generated applications were examined by hand on Eclipse IDE and found to be complete, runnable, and structurally correct.
 Approximately 40 XML lines produce >900 lines of code spanning all backend layers including Java code, Thymeleafe HTML, and
 Complexity Reduction
 application properties.
Appl. Sci. 2025, 15, 10621 19 of 35

 As shown in Table 6, XBoot successfully meets the core design objectives. It promotes
 modular design by cleanly separating layers and linking them through a compact DSL.
 All generated code is transparent and traceable to DSL specifications, which supports
 both debugging and pedagogical exploration. Security is embedded declaratively via
 routes and connectors, automatically enforced in the generated application. Furthermore,
 the tool greatly accelerates prototyping while reducing cognitive overhead, especially for
 learners encountering Spring Boot’s layered architecture for the first time. These attributes
 make XBoot particularly well-suited for rapid instructional deployment and backend
 development prototyping. In fact, XBoot can also play a significant role in establishing
 a software product line (SPL) [36] for web application development and prototyping.
 All generated artifacts, including the StudentCourses and FlightBooking applications,
 can be reproduced using the instructions and DSL examples available in the public GitHub
 repository (XBoot v1.0, commit hash: 4e8a783; see Data Availability section).

 7.2. Preliminary Evaluation with Student Participants
 To complement the author-led evaluation, we conducted a preliminary proof-of-
 concept (POC) study with ten senior undergraduate software engineering students. The
 goal was not to produce statistically generalizable results, but to verify XBoot’s functionality
 and obtain provisional insights into its educational value.
 Participants, all of whom had prior Spring Boot experience and achieved A/A+ grades in
 relevant coursework, followed a standardized workflow: (1) describe application requirements
 in natural language, (2) use XBoot GPT to generate DSL specifications, (3) generate a Spring
 Boot application with XBoot, (4) run the JAR and verify CRUD operations, Thymeleaf views,
 and RBAC, and (5) provide feedback through a structured post-experiment survey. The survey
 (Appendix A.7.) included nine questions covering usability, correctness, and learning impact.
 This structured process ensured consistent engagement with XBoot across all participants and
 allowed us to capture both quantitative and qualitative insights into its usability and educational
 value. The responses, summarized below, provide an initial perspective on how effectively
 XBoot supports rapid application generation while reinforcing key Spring Boot concepts.

 7.2.1. Results
 Table 7 summarizes student feedback across both case studies. Most participants re-
 ported completing application generation and deployment within minutes, with the majority
 requiring less than ten. By comparison, manual development of similar case studies in prior
 Web Engineering lab assignments typically required 90–120 min, where students were tasked
 with implementing applications to consolidate their understanding of course concepts. This
 contrast underscores the substantial acceleration achieved with XBoot.

 Table 7. Student Feedback Summary on the Two Case Studies.

 Questions Summary of Feedback
 Most students completed generation and deployment within minutes. Times ranged from ~2 to ~20 min, with the majority under 10 min, compared to 45–60 min
 1
 for manual development.
 2 Reported difficulty was consistently low (1–3), with most students rating the process as “very easy.”
 3 All students confirmed that the generated applications followed the expected layered architecture (Controller-Service-Repository).
 4 All participants verified that home, list, and form pages were generated correctly.
 5 Functionality was generally confirmed. Minor mismatches occurred in isolated cases due to route inconsistencies.
 6 Students found the structure highly consistent with what was taught in class, which reinforced their understanding of architectural layering.
 The tool reinforced understanding of Spring Boot architecture, averaging 4/5 on the Likert scale (range 3–5). Students noted it “made it simpler to remember
 7
 what I learned,” “helped visualize how layers connect,” and clarified interactions between controllers, services, repositories, and views.
 8 Ratings varied from 1 to 5. Some felt highly confident in extending the code, while others noted the initial volume of generated code was overwhelming.
 Students reported learning about: (a) practical use of the terminal and Spring Boot JARs, (b) connecting controllers, services, and repositories, (c) working with
 9 validation, Swagger, and configuration files, and (d) appreciating the role of low-code tools in rapid prototyping. Overall, students recognized the tool’s value in
 reinforcing class concepts.

 Beyond speed, students emphasized usability. They consistently rated the difficulty of
 launching the generated JAR file as very low, most often describing the process as ‘very
Appl. Sci. 2025, 15, 10621 20 of 35

 easy.’ This indicates that the generated applications were not only structurally correct but
 also straightforward to deploy.
 All participants confirmed that the applications adhered to the expected layered
 architecture (Controller-Service-Repository) and included fully functional Thymeleaf pages
 (home, list, and form). Role-based access control was also generally successful, with only
 minor mismatches reported in isolated cases due to route inconsistencies.
 From an educational perspective, students found the generated codebase highly
 consistent with classroom instruction, which reinforced their understanding of architectural
 layering. Several participants noted that XBoot made it simpler to remember key concepts,
 helped them visualize how layers connect, and clarified the interactions between controllers,
 services, repositories, and views.
 Confidence in reusing or extending the generated applications was more mixed.
 Some students felt overwhelmed by the initial code volume, while others appreciated the
 modularity and maintainability of the generated structure, which they believed would
 facilitate future modifications.
 In their open-ended feedback, students highlighted a variety of learning outcomes.
 They gained practical experience with terminal commands, CRUD functionality, RBAC,
 validation handling, Swagger documentation, and configuration management. Several
 also recognized the broader significance of low-code tools in accelerating prototyping and
 reducing boilerplate work, which provided them with a deeper appreciation of how such
 tools can complement traditional software engineering practice.

 7.2.2. Discussion
 The findings confirm that XBoot reliably transforms natural language requirements
 into runnable Spring Boot applications with minimal effort and strong consistency. The
 drastic reduction in time-to-application compared to manual coding suggests clear produc-
 tivity benefits. Importantly, the automatically enforced architectural patterns and RBAC
 mechanisms reduced the likelihood of common structural and security flaws. For example,
 in prior coursework by the same cohort, approximately 60% of manually written Spring
 Boot projects exhibited issues such as missing role restrictions, incorrect layer mappings,
 or hardcoded credentials. By contrast, no XBoot-generated project displayed such flaws,
 underscoring its ability to encode best practices directly into the DSL.
 From an educational perspective, the tool effectively reinforced architectural principles.
 Students confirmed that the generated layered structure mirrored classroom instruction
 and provided a clearer visualization of the interaction between components. The positive
 average on Q7, alongside qualitative comments, indicates that XBoot not only accelerated
 development but also served as a pedagogical scaffold for understanding layered design
 and separation of concerns.
 At the same time, the mixed confidence levels in extending the generated code high-
 light an area for refinement. While the modular architecture facilitated reusability for some,
 others felt overwhelmed by the volume of boilerplate produced. This points to the need
 for additional scaffolding tools such as documentation, navigation aids, or partial code
 explanations to ease onboarding for less experienced learners.
 Overall, the POC suggests that XBoot achieves both functional correctness and ped-
 agogical value. It accelerates development, enforces best practices, and reinforces key
 educational outcomes. However, larger-scale and more controlled studies are needed to
 validate these preliminary insights. Future evaluations should also incorporate additional
 metrics, such as lines of code saved compared to manual development and the degree of
 editing required when DSL specifications are generated by LLMs.
Appl. Sci. 2025, 15, 10621 21 of 35

 7.3. XBoot Alingment with Common DSL Experiments Outcomes
 Previous empirical studies on DSLs have reported consistent benefits in terms of de-
 veloper effectiveness and efficiency compared to general-purpose languages (GPLs). For
 example, Voelter and Visser [2] showed that DSLs can improve comprehension by providing
 higher-level abstractions, while Chavarriaga et al. [6] and da Rocha et al. [7] demonstrated that
 XML-based DSLs can streamline development in specialized domains. More recent work has
 emphasized developer experience, where low-code and DSL-based solutions improve produc-
 tivity and reduce configuration overhead compared to traditional GPL development [5,30,34].
 Our proof-of-concept results with XBoot are consistent with these findings. Students
 were able to generate fully functional, structurally correct Spring Boot applications in
 minutes, whereas similar applications developed manually in prior coursework required
 45–60 min. Structural and security-related flaws, which were common in manually coded
 projects, were absent in the XBoot-generated systems. These outcomes mirror prior DSL
 experiments in demonstrating gains in correctness and efficiency, while also extending the
 discussion to educational impact. In particular, participants reported that XBoot reinforced
 their understanding of layered architecture, role-based access control, and validation.
 Unlike industrial DSL evaluations that mainly emphasize productivity in professional
 contexts, our results highlight how DSL-driven modeling can scaffold novice developers.
 This aligns with the broader DSL literature [2,30], while contributing a novel perspective
 on the pedagogical value of DSLs in backend software engineering education.

 7.4. Limitations and Observations
 It is important to contextualize the findings within the nature of this POC evalua-
 tion. The study involved a small and homogeneous cohort of 10 senior undergraduate
 students, which means the results should be interpreted as exploratory rather than statisti-
 cally generalizable. Some participants conducted the experiment remotely while engaged
 in cooperative training, and no formal instruction on XBoot’s DSL syntax was provided.
 Students relied solely on XBoot GPT to convert natural language descriptions into valid
 DSL specifications. While this reflects realistic usage of AI-assisted modeling in modern
 low-code environments, it introduced a degree of inconsistency, especially in datatype
 declarations and relationship formats, that could have been mitigated with targeted
 DSL instruction.
 While the majority of student participants successfully generated and executed their
 applications using XBoot without requiring manual intervention, several limitations
 emerged that were primarily rooted in the intermediate DSL specifications produced
 via the GPT assistant, rather than in the XBoot generator itself.
 However, a few participants reported issues with RBAC. Upon inspection, these were
 traced to mismatches between DSL-defined routes and controller paths. Two common
 issues were observed:
 • Route Mismatch: An example of a route mismatch in the DSL is shown in Box 13.:

 Box 13. DSL Snippet Illustrating a Route Mismatch.

 <Route path="/enrollments/create" view="enrollment-create" method="POST"
 controller="EnrollmentController" role="ADMIN"/>

 This mismatch resulted in the generated Spring Security rule shown in Box 14.
Appl. Sci. 2025, 15, 10621 22 of 35

 Box 14. Generated Spring Security Rule from Mismatched Route.

 .requestMatchers("/enrollments/create").hasRole("ADMIN")

 However, the corresponding form was accessed via “/enrollments/form “, resulting in
 the page being unprotected. The issue was resolved by adjusting the rule as shown in Box 15.

 Box 15. Corrected Spring Security Rule Protecting the Enrollment Form.

 .requestMatchers("/enrollments/form").hasRole("ADMIN")

 • Path Naming: Another case of mismatch arose from singular vs. plural path naming,
 where the controller was mapped as shown in Box 16.

 Box 16. REST Controller Mapping with Plural Path (/enrollments).

 @RequestMapping("/enrollments")

 As with the previous issue, this was resolved by updating the route definition to
 ensure consistency.
 These cases highlight the importance of maintaining strict alignment between DSL
 routes, controller mappings, and security configurations. To address this, XBoot GPT
 was enhanced with smarter path suggestions and stricter validation logic to reduce the
 likelihood of such mismatches in future use.
 In addition, some students reported other DSL-related issues via informal communi-
 cation channels such as WhatsApp. These included:
 • Incorrect Data Types: A common mistake involved specifying primitive types
 (e.g., Long) in relationship fields, when a class reference (e.g., Course, Student) was
 required. These led to invalid JPA mappings and compilation errors. Students resolved
 the issue by correcting the field types, and XBoot GPT was updated to enforce entity
 references more strictly in generated DSL code.
 • Improper Relationship Formatting: In multiple instances, relationships were defined
 using lowercase, hyphenated values such as “many-to-one” instead of the expected
 “ManyToOne” format. Due to the case-sensitive nature of the XBoot schema, these
 entries were either ignored or incorrectly parsed, leading to missing or incomplete
 relationship mappings. This prompted an update to XBoot GPT to generate only
 schema-compliant relationship types.
 • Advanced Customization Error—Date Field: One student experimented by changing
 a flight departure field’s type from String to Date. While the XML was valid, the
 generated Java class lacked the required import (import java.util.Date). This caused
 a compilation error. After manually adding the required library, the application
 compiled but failed at runtime due to Thymeleaf expecting a String rather than a Date
 type. The student resolved this by adjusting the controller, service, and Thymeleaf
 template to support a date picker input. Although this required additional effort, it
 demonstrated that XBoot-generated code is modular and extensible for more advanced
 development scenarios.
Appl. Sci. 2025, 15, 10621 23 of 35

 These issues also exposed a broader design limitation: XBoot currently defaults tem-
 poral fields to String to reduce dependency complexity and facilitate smoother onboarding.
 While suitable for most beginners, this limits type expressiveness. Future releases will
 support optional handling for Java temporal types (Date, LocalDate, LocalDateTime), with
 automatic imports and Thymeleaf-compatible view rendering.
 Despite these issues, students were generally able to debug and fix problems with
 minimal effort. When compilation errors occurred, XBoot-generated projects made it easy
 to locate the issue due to standard naming and file structure. Students used IDE error
 messages to trace and correct faulty XML specifications or Java code lines. This highlights
 the modularity and transparency of the generated artifacts.
 Overall, these observations are consistent with the POC nature of the study: they
 demonstrate that the tool works as intended and can provide provisional learning benefits,
 while also highlighting the need for larger, more diverse cohorts and controlled settings in
 future evaluations.

 7.5. Threats to Validity
 While the evaluation of XBoot demonstrates promising results in terms of generation
 fidelity, student productivity, and educational value, it is important to acknowledge poten-
 tial threats to the validity of these findings. This section discusses key internal, external,
 construct, and conclusion validity concerns.

 7.5.1. Internal Validity
 The internal validity of the experiment may be influenced by individual differences
 among participants. Although all students had prior exposure to Java and Spring Boot,
 variations in programming experience, problem-solving skills, and familiarity with XML
 may have affected their performance. Furthermore, students relied on XBoot GPT to
 generate the DSL specifications, and any inaccuracies in the GPT-generated output may
 have introduced confounding variables unrelated to XBoot itself. For example, some DSL
 errors were caused by incorrect relationship type formats or invalid data types, which
 required manual intervention by the participants.

 7.5.2. External Validity
 The study was conducted with a relatively small and homogeneous group of
 ten senior undergraduate students from a single institution. While the results suggest
 that XBoot can support backend development in educational settings, these findings may
 not generalize to novice programmers, non-technical users, or students from other aca-
 demic backgrounds. Additionally, all participants had been previously trained in Spring
 Boot, which may have influenced their ability to recognize and correct DSL issues. The
 remote nature of the experiment, conducted during students’ cooperative training, may
 also differ from in-class use scenarios where peer support and instructor guidance are more
 readily available. Overall, the small sample size and the homogeneity of the group mean
 that the findings should be interpreted only as an exploratory pilot, with larger-scale and
 more diverse studies required to draw general conclusions.

 7.5.3. Construct Validity
 The constructions used to evaluate productivity and learning, such as time-to-
 completion, self-reported understanding, and confidence, may not fully capture the depth
 of architectural comprehension or long-term learning outcomes. While these measures
 provide insight into usability and perceived clarity, they are inherently subjective. The
 evaluation did not include objective tests of students’ retained knowledge or ability to
 generalize beyond the generated codebase. Additionally, the use of DSL modeling as
Appl. Sci. 2025, 15, 10621 24 of 35

 a proxy for backend design skill assumes that learners understand the DSL semantics,
 which was not directly tested.

 7.5.4. Conclusion Validity
 Given the limited sample size (four participants) and exploratory nature of the eval-
 uation, it is not possible to make statistically significant claims about the effectiveness
 of XBoot and exploratory nature of the evaluation, it is not possible to make statistically
 significant claims about the effectiveness of XBoot. The findings suggest clear trends in
 reduced development time and high user satisfaction, but larger-scale studies are needed to
 validate these conclusions across broader populations. Furthermore, while students were
 able to generate and deploy applications quickly, the need for occasional DSL corrections (as
 discussed in Section 7.3) suggests that the overall automation pipeline still relies partially
 on student judgment and technical intuition.

 7.5.5. Mitigation and Future Work
 To address these threats, future evaluations of XBoot will involve larger cohorts, ran-
 domized controlled designs, and direct comparison with manual development workflows.
 Planned in-class studies will compare student performance under three conditions: manual
 coding, DSL-based modeling, and natural language-driven GPT modeling. Additionally,
 integrating in-tool validation and guided DSL editors may help reduce errors and improve
 reliability for novice users.

 8. XBoot in Education
 In addition to rapid prototyping, XBoot was designed to support backend software
 engineering education. Drawing on the authors’ experience teaching undergraduate web
 engineering, it addresses recurring challenges students face when learning Spring Boot.
 The observations are based on third-year software engineering students who, despite
 completing multiple Java-focused courses (OOP, data structures, design patterns), struggled
 with Spring Boot’s framework-specific requirements. Common issues included:
 • Project setup errors: Misplaced @SpringBootApplication classes or incorrect pack-
 age hierarchies broke component scanning. Students also confused REST and view
 controllers, often implementing one but not both.
 • Thymeleaf difficulties: Form bindings and constructs such as th:each were frequently
 mishandled. Missing dependencies in lab setups (e.g., omitting Spring Web) caused
 build failures and wasted debugging time.
 • Security gaps: Students implemented login but often failed to enforce RBAC in
 final projects.
 These challenges showed that novices struggled more with Spring Boot’s struc-
 ture and configuration than with application logic, slowing progress and limiting
 architectural focus.
 XBoot mitigates these difficulties by shifting effort from manual coding to high-level
 modeling. With a concise XML DSL, students specify entities, relationships, routes, and
 roles, and the generator produces:
 • A valid Maven project with correct package hierarchy and entry point.
 • REST and view controllers with consistent routing.
 • Thymeleaf templates for forms and listings with valid bindings.
 • Spring Security enforcing RBAC at both view and API layers.
 • All required dependencies included automatically.
 For example, in the StudentCourses case study, a 40-line DSL produced over 900 lines
 of Java and HTML, scaffolding the entire backend stack. The result is a complete, functional
Appl. Sci. 2025, 15, 10621 25 of 35

 application that reflects best practices in separation of concerns, layered architecture, and
 security, providing students with a template to study, run, and extend.

 8.1. Educational Impact and Instructional Advantages of XBoot
 The following discussion highlights the observed classroom benefits for students,
 practical advantages for instructors, and potential curriculum positioning of XBoot.
 Classroom Benefits and Observations
 Although XBoot has not yet been subjected to a formal educational study, its use in
 labs, quizzes, exams, and projects has revealed several benefits:
 • Students complete backend assignments more quickly and with greater confidence.
 • Structural and configuration errors, particularly in project setup, are reduced.
 • REST and view controller roles become clearer through consistent scaffolding.
 • Thymeleaf integration is less error-prone due to ready-made templates.
 • Role-based authorization is easier to apply using declarative modeling rather than
 manual annotations.
 By starting from high-level models and incrementally exploring the generated code,
 students face a lower entry barrier and are encouraged to reason architecturally from
 the outset.
 Instructor Utility
 XBoot also offers substantial advantages for instructors.
 • Enables the design of structured, multi-stage assignments.
 • Provides a clean codebase to demonstrate layered design, secure routing, and
 service abstraction.
 • Minimizes time spent on setup errors, allowing more time for teaching architecture
 and design thinking.
 • Facilitates model-to-code traceability, making it easier to explain how changes in
 design are reflected in implementation.
 Positioning in the Curriculum
 XBoot fits well within backend development courses in software engineering, infor-
 mation systems and computer science. It also supports broader themes, such as:
 • Web engineering.
 • Secure application development.
 • Model-driven engineering.
 • Low-code and DSLs.
 • Component-based system design.
 In summary, XBoot helps students and instructors move beyond boilerplate and
 misconfiguration by providing a structured, declarative, and secure approach to backend
 development. It bridges the gap between theory, modeling, and implementation, offering
 a strong foundation for full-stack learning in academic settings.

 8.2. Pedagogical Benefits: Structured Learning of Spring Boot and Layered Architecture
 A recurring challenge in backend software engineering education is ensuring that
 students not only build functional applications but also internalize sound architectural
 practices. In manual Spring Boot projects, novices often bypass the service layer or embed
 business logic in controllers, undermining modularity and maintainability.
 XBoot addresses this challenge by generating applications that consistently follow
 a layered model with entities, repositories, services, REST and view controllers, and
 Thymeleaf templates. This scaffolding provides tangible examples of best practices, guiding
 students toward modular design aligned with established conventions.
Appl. Sci. 2025, 15, 10621 26 of 35

 XBoot is not a replacement for learning Spring Boot fundamentals but a structured
 scaffold that lowers the entry barrier. By abstracting setup, dependency management,
 and annotation complexity, it enables students to focus on architectural concerns such as
 request handling, validation, routing, and access control. As familiarity grows, learners can
 reconstruct or extend these layers manually.
 A potential risk is over-reliance on generated artifacts, which may limit coding practice.
 To mitigate this, phased assignments are recommended: students can begin with DSL-based
 generation, then progressively modify service logic, extend validation, or add secured
 endpoints. This approach balances automation with hands-on experience, reinforcing both
 architectural understanding and coding competence.

 9. XBoot in the Context of AI-Driven Development Tools
 The rise in AI coding assistants such as GitHub Copilot, Amazon CodeWhisperer, and
 GPT-based generators has introduced new paradigms in software development. These
 tools translate natural language prompts into code, enabling rapid prototyping but often at
 the expense of traceability, consistency, maintainability, and educational suitability [37].
 XBoot addresses these shortcomings through a model-driven approach grounded in
 a formal XML-based DSL. Unlike probabilistic outputs from AI, XBoot delivers deter-
 ministic, traceable, and security-aware code generation. Its distinct advantages can be
 summarized across five areas:
 1. Deterministic generation: AI outputs vary with phrasing, while XBoot ensures repeat-
 able, auditable results from the same XML input.
 2. Design-to-code transparency: Each DSL tag maps directly to entities, controllers,
 views, or security rules, making implementation artifacts traceable to requirements.
 3. Enforced layering: Whereas AI may blur responsibilities, XBoot consistently applies
 MVC principles, producing separate entities, repositories, services, and controllers.
 4. Integrated security: Role attributes in <Route> and <Connector> tags are trans-
 lated into Spring Security rules and Thymeleaf restrictions, ensuring consistent
 RBAC enforcement.
 5. Structured refinement: XBoot supports incremental evolution of models through
 schema validation, avoiding the instability of re-prompting AI tools.
 Rather than replacing AI, XBoot complements it. GPT-based tools can draft DSL
 snippets from informal descriptions, after which XBoot validates, structures, and generates
 a complete application. In this way, AI provides flexibility for exploration, while XBoot
 guarantees transparency, architectural discipline, and security. Together, they support both
 rapid prototyping and structured learning, making XBoot well suited for academic and
 professional contexts.

 10. Trade-Offs of Learning with XBoot vs. Manual Development
 XBoot lowers the entry barrier to backend development by allowing students to model
 and generate complete Spring Boot applications from compact specifications. This enables
 learners to focus on architectural concepts such as layered design, modularity, and role-
 based access control without being hindered by configuration overhead. By scaffolding fully
 functional applications, it provides a clear entry point for understanding backend architecture.
 However, this abstraction introduces trade-offs. Students risk gaining only a super-
 ficial grasp of Spring Boot internals, such as how annotations (@Service, @PreAuthorize,
 @RequestMapping), dependency injection, or request routing shape application behavior.
 Overreliance on generated code can create “black box” learning, limiting skills in debug-
 ging, configuration, and manual setup competencies essential in professional contexts.
Appl. Sci. 2025, 15, 10621 27 of 35

 To mitigate this, XBoot should be used as a complement rather than a substitute
 for manual development. Educators can start with DSL-based modeling to emphasize
 architecture and security, then progressively shift to coding tasks where students adapt
 or rewrite generated artifacts. This staged approach helps learners first understand what
 needs to be built before mastering how to build it.
 XBoot GPT further supports this path by transforming natural language descrip-
 tions into valid DSL specifications, accelerating design and allowing instructors to focus
 on patterns and principles rather than syntax. Together, XBoot and its assistant foster
 a balanced strategy: rapid early comprehension and architectural reasoning paired with
 the rigor of traditional Spring Boot development, ensuring students gain both high-level
 design thinking and hands-on implementation skills.

 11. Conclusions and Future Work
 This study introduced XBoot, a lightweight model-driven tool for generating secure
 and modular Spring Boot applications from XML specifications. Designed with education in
 mind, XBoot enables students and instructors to focus on architecture, entity relationships,
 and access control rather than framework configuration and boilerplate coding.
 By adopting a component-connector model and embedding role-based access control
 at the specification layer, XBoot produces maintainable and traceable backend systems
 aligned with established engineering principles. The generated code spans all backend
 layers, with security consistently enforced across REST endpoints and user interfaces.
 The StudentCourses case study demonstrated that a compact DSL file can generate a com-
 plete system including entities, repositories, services, controllers, security settings, and Thymeleaf
 views with minimal effort. Author-driven validation and a structured student experiment con-
 firmed the correctness, usability, and educational value of the generated applications.
 The evaluation results highlight several advantages. XBoot reduced development time
 dramatically (from ~45–60 min manually to ~5 min using DSL specifications), eliminated com-
 mon errors in role restrictions and architectural layering, and produced applications directly
 aligned with classroom instruction. Student feedback further confirmed its usability and
 effectiveness as an educational tool. Together, these findings demonstrate XBoot’s potential to
 accelerate learning while reinforcing best practices in secure backend development.
 Future work will extend frontend security enforcement. While unauthorized requests are
 already blocked at the controller level through Spring Security annotations (e.g., @PreAutho-
 rize), current view templates do not dynamically reflect user permissions. Upcoming versions
 will incorporate Thymeleaf’s sec:authorize attributes into generated views, ensuring that
 navigation links and form elements are visible only to users with appropriate roles. This will
 bring frontend and backend security layers into full alignment and further enhance the user
 experience. In addition, benchmarking XBoot against alternative frameworks on equivalent
 case studies is planned to provide a broader comparative evaluation.

 12. Current Limitations of XBoot
 While XBoot shows strong educational value and practical usability, several limitations
 remain. First, its security model relies on statically defined roles in the DSL, limiting support
 for dynamic scenarios such as runtime role assignment, tenant-based authorization, or
 integration with external identity providers. This reduces suitability for enterprise-grade
 applications requiring fine-grained access control.
 Second, view generation is restricted to basic data entry and listing. Advanced UI
 logic, client-side validation, and responsive design must still be implemented manually,
 constraining its use for complex or production-ready interfaces.
Appl. Sci. 2025, 15, 10621 28 of 35

 Third, XBoot is tightly coupled with Spring Boot and a fixed project structure, which
 may limit adaptability to alternative frameworks or modular architectures. Although the
 DSL enforces architectural separation, it can also abstract details that advanced learners or
 professionals may wish to study more directly.
 Finally, while promising for instruction and prototyping, XBoot has not yet been
 evaluated in large-scale classroom trials, leaving its broader educational impact to be
 assessed in future empirical studies.

 Author Contributions: Conceptualization, B.Y.A. and M.K.N.; methodology, B.Y.A. and M.K.N.; soft-
 ware, B.Y.A.; validation, B.Y.A. and M.K.N.; formal analysis, B.Y.A.; investigation, M.K.N.; resources,
 M.K.N.; data curation, M.K.N.; writing—original draft preparation, B.Y.A.; writing—review and editing,
 M.K.N.; visualization, M.K.N.; supervision, B.Y.A.; project administration, B.Y.A.; funding acquisition,
 B.Y.A. and M.K.N. All authors have read and agreed to the published version of the manuscript.

 Funding: This research received no external funding.

 Data Availability Statement: All data are provided in the text of this paper. The XBoot framework
 binary and usage instructions are available publicly on GitHub [38].

 Acknowledgments: The authors acknowledge the use of an AI-based tool (PaperPal) to assist in
 proofreading and improving the clarity of the English language in this manuscript. The tool was not
 used for generating original content, analysis, or results. All substantive ideas, experiments, and
 conclusions are the authors’ own.

 Conflicts of Interest: The authors declare no conflicts of interest in the publication of this paper.

 Appendix A
 Appendix A.1 XBoot Execution Checklist Generated at Console
Appl. Sci. 2025, 15, 10621 29 of 35

 Appendix A.2 XBoot EBNF Representation
 The core grammar of the XBoot DSL is represented below using the Extended Backus-
 Naur Form (EBNF). This defines the structure of the valid XBoot XML specifications.

 Appendix A.3 Generated Security Configuration (Excerpt)
 Below is an excerpt of the generated Spring Security configuration file, automatically
 produced by XBoot for the StudentCourses system.

 @Configuration

 public class SecurityConfig {

 @Bean

 public SecurityFilterChain filterChain(HttpSecurity http) throws Excep-

 tion {

 http

 .authorizeHttpRequests(auth -> auth

 .requestMatchers("/home", "/css/**", "/js/**", "/im-

 ages/**").permitAll()

 .requestMatchers("/student/**").hasRole("USER")

 .requestMatchers("/course/**").hasRole("USER")

 .requestMatchers("/enrollment/**").hasRole("USER")

 .anyRequest().authenticated()

 )

 .formLogin(form -> form
Appl. Sci. 2025, 15, 10621 30 of 35

 Appendix A.4 Students–Courses Case Study DSL Description

 Appendix A.5 FlightsBooking XBoot XML-DSL Description
Appl. Sci. 2025, 15, 10621 31 of 35

 Appendix A.6 Student Experiment Manual
 This appendix reproduces the manual provided to student participants during the
 XBoot evaluation. It outlines the experiment procedure, tool usage instructions, and the
 formal case study descriptions used in the study.
 XBoot Student Experiment Manual
 This manual guides you through the controlled experiment using the XBoot tool for
 low-code generation of Spring Boot full-stack applications. You will complete two case
 studies and provide structured feedback.
 Folder Structure
 • You will receive a zip file containing a folder named xboot/with:
 • xboot.jar—the executable generator
 • input/– place your XML DSL file here (xboot.xml)
 • output/– generated project will appear here
 • schema/– contains XBootSchema.xsd used for validation
 What You Will Do
 You will complete two tasks:
 1. Generate the StudentCourses application
 2. Generate the FlightBooking application
 For each task:
 • Describe the application to the XBoot GPT assistant in natural language
 • Save the XML DSL to input/xboot.xml
 • Run the JAR file
 • Open the generated project in your IDE (e.g., Eclipse or IntelliJ)
 • Explore the structure and test the views
 • Complete the feedback form
 Instructions
 1. Access the GPT assistant: ChatGPT—XBoot DSL Generator
 2. Provide a natural language prompt (see example below): “Create an application for
 employees and departments. Employees have name, email, salary. A department can hold
 many employees. . .”
 3. Adapt this for StudentCourses or FlightBooking.
 4. Copy the XML to input/xboot.xml.
 5. Run the tool via:
 java -jar xboot.jar input/xboot.xml schema/XBootSchema.xsd, Or double-click the .jar file.
 6. Open the project in your IDE.
 7. Navigate and test generated views.
 8. Fill out the feedback form.
 9. Repeat the same for the second case study.
 Submission
 Submit the following:
 • Feedback form
 • Screenshots of the running applications
 • Two DSL XML files
 • Generated output projects (as zip)
 Testing URLs
 StudentCourses:
 • /home
Appl. Sci. 2025, 15, 10621 32 of 35

 • /students
 • /courses
 • /enrollments
 • /enrollments/new (Admin only)
 FlightBooking:
 • /flights
 • /passengers
 • /reservations
 • /reservations/new (Admin only)
 Check application.properties for username/password.
 Case Study Descriptions
 Case Study 1: StudentCourses
 • Entities:
 # Student: name, email, mobile
 # Course: title, description
 # Enrollment: student (ManyToOne → Student), course (ManyToOne → Course), grade
 • Relationships:
 # Student enrolls in many courses via Enrollment
 # Enrollment links Student and Course
 • Requirements:
 # Use @NotBlank, @Email, @Pattern for validation
 # User views for listing and creating enrollments
 # Protect enrollment creation with ADMIN role
 Case Study 2: FlightBooking
 • Entities:
 # Flight: flightNumber, origin, destination, departureTime
 # Passenger: name, passportNumber, email
 # Reservation: flight (ManyToOne → Flight), passenger (ManyToOne → Passen-
 ger), seatNumber, status
 • Relationships:
 # One passenger and one flight per reservation
 # A flight/passenger can have many reservations
 • Requirements:
 # Use validation annotations
 # List/form views for reservations
 # Protect reservation form with ADMIN role

 Appendix A.7 Student Feedback Form
 This form must be filled out after completing each case study using the XBoot tool
 and GPT assistant. Please answer all sections carefully. Your feedback supports research on
 low-code Spring Boot prototyping.
 Case Studies Metrics:
 A. Timing Metrics
 1. Time (in minutes) from natural language description to working application:
 2. How difficult was it to run the JAR and launch the app? (1 = Very Easy, 5 =
 Very Difficult).
Appl. Sci. 2025, 15, 10621 33 of 35

 B. Structural Correctness
 1. Was a layered architecture (Controller–Service–Repository) generated?
 (Yes/No/Partial):
 2. Were Thymeleaf view pages (home, list, form) generated? (Yes/No):
 3. Was role-based access control working as expected? (Yes/No):
 4. Was the structure similar to what you learned in class? If no, explain:
 C. Learning and Confidence
 1. Did this tool help reinforce your understanding of Spring Boot architecture?
 (1–5):
 2. Do you feel confident reusing or extending the generated app? (1–5):
 3. What did you learn from this experience?

 Appendix B
 Appendix B.1 Courses Listing Page

 Appendix B.2 Students’ Enrollment Form

 Appendix B.3 Students’ Enrollments in Courses Listing Page

References
1. Walls, C. Spring Boot in Action, 6th ed.; Manning Publications: Shelter Island, NY, USA, 2023.
2. Voelter, M.; Visser, E. DSL Engineering: Designing, Implementing and Using Domain-Specific Languages. In Software Language
 Engineering; Springer: Berlin/Heidelberg, Germany, 2011; pp. 24–44.
3. Bucaioni, A.; Cicchetti, A.; Ciccozzi, F. Modelling in low-code development: A multivocal systematic review. Softw. Syst. Model.
 2022, 21, 1959–1981. [CrossRef]
4. Soldani, J.; Tamburri, D.A.; Van Den Heuvel, W.-J. The pains and gains of microservices: A systematic grey literature review. J.
 Syst. Softw. 2018, 146, 215–232. [CrossRef]
5. Guthardt, L.; Kosiol, J.; Hohlfeld, O. Lowcode vs. the developer: An empirical study on the developer experience and efficiency
 of a nocode platform. In Proceedings of the ACM/IEEE 27th International Conference on Model Driven Engineering Languages
 and Systems, Linz, Austria, 22–27 September 2024. [CrossRef]
Appl. Sci. 2025, 15, 10621 34 of 35

6. Chavarriaga, E.; Jurado, F.; Díez, F. An approach to build XML-based domain specific languages solutions for client-side web
 applications. Comput. Lang Syst. Struct. 2017, 49, 133–151. [CrossRef]
7. da Rocha, M.M.; Favela, J.; Muchaluat-Saade, D.C. Design and Evaluation of an XML-Based Language for Programming Socially
 Assistive Robots. Int. J. Soc. Robot. 2025, 17, 1305–1333. [CrossRef]
8. Alonso, S.; Kalinowski, M.; Ferreira, B.; Barbosa, S.D.J.; Lopes, H. A systematic mapping study and practitioner insights on the
 use of software engineering practices to develop MVPs. Inf. Softw. Technol. 2023, 156, 107144. [CrossRef]
9. Rädler, S.; Berardinelli, L.; Winter, K.; Rahimi, A. Bridging MDE and AI: A systematic review of domain-specific modeling for AI
 software systems. Softw. Syst. Model. 2024, 24, 445–469. [CrossRef]
10. Taylor, R.N.; Medvidovic, N.; Dashofy, E.M. Component and connector views in practice: An experience report. In Proceedings
 of the ACM International Conference on Model-Driven Engineering Languages and Systems (MODELS), Ann Arbor, MI, USA,
 5–10 October 2017.
11. Fowler, M.; Lewis, J. Microservices: A Definition of This New Architectural Term. 2014. Available online: https://martinfowler.
 com/articles/microservices.html (accessed on 3 June 2025).
12. Newman, S.; Microservices, B.; Media, O. Building Microservices: Designing Fine-Grained Systems, 2nd ed.; O’Reilly Media:
 Sebastopol, CA, USA, 2021.
13. Dragoni, N.; Dustdar, S.; Larsen, S.; Mazzara, M. Microservices: Yesterday, Today, and Tomorrow. In Present and Ulterior Software
 Engineering; Mazzara, M., Meyer, B., Eds.; Springer: Cham, Switzerland, 2017; pp. 195–216. [CrossRef]
14. Johnsson, D.B.; Deogun, D.; Sawano, D.; Design, S.B. Software and Service Security; Manning Publications: Shelter Island, NY, USA, 2019.
15. Agnihotri, J.; Phalnikar, R. Development of performance testing suite using Apache JMeter. In Advances in Intelligent Systems and
 Computing; Springer: Singapore, 2018; pp. 317–326. [CrossRef]
16. Moreno-García, J.P.; García-Magariño, I.; Sánchez, C. A survey of the Selenium ecosystem. Electronics 2020, 9, 1067. [CrossRef]
17. Barakat, S.; Roque, E.B.; Sánchez, A.B.; Segura, S. Specification-Driven Code Generation for Interparameter Dependencies in Web
 APIs. In Service-Oriented Computing—ICSOC 2022 Workshops (LNCS, vol. 13821); Springer: Cham, Switzerland, 2023; pp. 261–273.
 [CrossRef]
18. Mendix, Low-Code Application Development Platform. Available online: https://www.mendix.com/platform/ (accessed on 25 May 2025).
19. Mew, L.; Field, D. A case study on using the Mendix low code platform to support a project management course. In Proceedings
 of the 2018 Information Systems & Computing Academic Professionals (ISCAP) Conference, Norfolk, VA, USA, 8–11 August 2018.
 Available online: https://iscap.us/proceedings/2018/pdf/4621.pdf (accessed on 17 April 2025), ISSN 2473–3857.
20. Bootify. Rapid Spring Boot Prototypes|Bootify.io. Available online: https://bootify.io/ (accessed on 25 March 2025).
21. Pivotal Software, Inc. Spring Initializr. Available online: https://start.spring.io/ (accessed on 11 November 2024).
22. Vuksan, B.; Jadhav, S.G.; McCarthy, J. Spring Roo in Action; Manning Publications: Shelter Island, NY, USA, 2012.
23. Project, O. OpenXava Reference Guide. Available online: https://openxava.org/OpenXavaDoc/ (accessed on 12 January 2025).
24. Gómez, O.S.; Miranda, R.H.R.; Verdín, K.C. CRUDyLeaf: A DSL for Generating Spring Boot REST APIs from Entity CRUD
 Operations. Cybern. Inf. Technol. 2020, 20, 3–14. [CrossRef]
25. Guégain, E.; Bonvoisin, A.; Acher, M.; Quinton, C.; Rouvoy, R. On the Interplay between Performance Indicators in Configurable
 Software: The Jhipster Case Study. 2023. Available online: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4640065
 (accessed on 14 June 2025).
26. Halin, A.; Nuttinck, A.; Acher, M.; Devroey, X.; Perrouin, G.; Baudry, B. Test Them All, Is It Worth It? Assessing Configuration
 Sampling on the JHipster Web Development Stack. Empir. Softw. Eng. 2019, 24, 674–717. [CrossRef]
27. Slifka, J.; Pergl, R. Application of Normalized Systems Theory to pure functional code to achieve sustainability of web front-end
 applications. J. Comput. Lang. 2025, 85, 101346. [CrossRef]
28. Martínez-Lasaca, F.; Díez, P.; Guerra, E.; de Lara, J. Dandelion: A scalable, cloud-based graphical language workbench for
 industrial low-code development. J. Comput. Lang 2023, 76, 101217. [CrossRef]
29. Chavarriaga, E.; Jurado, F.; Rodríguez, F.D. An approach to build JSON-based Domain Specific Languages solutions for web
 applications. J. Comput. Lang. 2023, 75, 101203. [CrossRef]
30. Pinho, D.; Aguiar, A.; Amaral, V. What about the usability in low-code platforms? A systematic literature review. J. Comput. Lang.
 2023, 74, 101185. [CrossRef]
31. Dalibor, M.; Heithoff, M.; Michael, J.; Netz, L.; Pfeiffer, J.; Rumpe, B.; Varga, S.; Wortmann, A. Generating customized low-code
 development platforms for digital twins. J. Comput. Lang. 2022, 70, 101117. [CrossRef]
32. ISO/IEC 14977; Information Technology—Syntactic Metalanguage—Extended BNF (EBNF). ISO: Geneva, Switzerland, 1996.
33. Alkazemi, B.; Nour, M. XBoot DSL Generator. Available online: https://tinyurl.com/2j3ejb78 (accessed on 18 July 2025).
34. Hagel, N.; Hili, N.; Bartel, A.; Koziolek, A. Turning Low-Code Development Platforms into True No-Code with Extensible
 DSLs. In Proceedings of the ACM/IEEE 27th International Conference on Model Driven Engineering Languages and Systems,
 Linz, Austria, 22–27 September 2024. [CrossRef]
Appl. Sci. 2025, 15, 10621 35 of 35

35. Shin, M.E.; Kang, T.; Gomaa, H. Secure Software Architectural Patterns Designed with Secure Connectors. In Proceedings of the
 17th International Conference on Software Technologies ICSOFT, Lisbon, Portugal, 11–13 July 2022; pp. 484–491. [CrossRef]
36. Shin, M.E.; Gomaa, H.; Pathirage, D. A Software Product Line Approach for Feature Modeling and Design of Secure Connectors.
 In Proceedings of the 13th International Conference on Software Technologies, Porto, Portugal, 26–28 July 2018; pp. 506–517.
 [CrossRef]
37. Zhang, H.; Zhang, K.; Li, Z.; Li, J.; Li, J.; Li, Y.; Zhao, Y.; Zhu, Y.; Liu, F.; Li, G.; et al. Deep learning for code generation: A survey.
 Sci. China Inf. Sci. 2024, 67, 191101. [CrossRef]
38. Alkazemi, B.; Nour, M. XBoot: A Low-Code Generator for Spring Boot. Available online: https://github.com/mkmnma/XBoot
 (accessed on 9 June 2025).

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
