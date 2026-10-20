# **Domain-Driven Design Representation of Monolith Candidate Decompositions Based on Entity Accesses** 

Miguel Levezinho 

miguel.levezinho@tecnico.ulisboa.pt 

University of Lisbon Instituto Superior Técnico Lisbon, Portugal 

## Olaf Zimmermann 

olaf.zimmermann@ost.ch 

OST Eastern Switzerland University of Applied Sciences Rapperswil, Switzerland 

### **ABSTRACT** 

Microservice architectures have gained popularity as one of the preferred architectural approaches to develop large-scale systems, replacing the monolith architecture approach. Similarly, strategic Domain-Driven Design (DDD) gained traction as the preferred architectural design approach for the development of microservices. However, DDD and its strategic patterns are open-ended by design, leading to a gap between the concepts of DDD and the design of microservices. This gap is especially evident in migration tools that identify microservices from monoliths, where candidate decompositions into microservices provide little in terms of DDD refactoring and visualization. This paper proposes a solution to this problem by extending the operational pipeline of a multi-strategy microservice identification tool, called Mono2Micro, with a DDD modeling tool that provides a language, called Context Mapper DSL (CML), for formalizing the most relevant DDD concepts. The extension maps the content of the candidate decompositions, which include clusters, entities, and functionalities, to CML constructs that represent DDD concepts such as _Bounded Context_ , _Aggregate_ , _Entity_ , and _Service_ , among others. The results are validated with a case study by comparing the candidate decompositions resulting from a real-world monolith application with and without CML translation. 

### **KEYWORDS** 

Domain-Driven Design, Microservices, Migration. 

#### **ACM Reference Format:** 

Miguel Levezinho, Stefan Kapferer, Olaf Zimmermann, and António Rito Silva. 2024. Domain-Driven Design Representation of Monolith Candidate Decompositions Based on Entity Accesses. In _Proceedings of (arXiv)._ ACM, New York, NY, USA, 11 pages. https://doi.org/10.1145/nnnnnnn.nnnnnnn 

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. _arXiv, June, 2024_ 

© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 978-x-xxxx-xxxx-x/YY/MM 

Stefan Kapferer 

stefan.kapferer@ost.ch 

OST Eastern Switzerland University of Applied Sciences Rapperswil, Switzerland 

António Rito Silva 

rito.silva@tecnico.ulisboa.pt 

University of Lisbon Instituto Superior Técnico 

Lisbon, Portugal 

### **1 INTRODUCTION** 

Microservice architectures have become one of the architectures of choice for emerging large enterprise applications [6, 23]. This adoption results from the advantages of partitioning a large system into several independent services, which provide qualities such as strong boundaries between services; independent development, testing, deployment, and scaling of each service; and service-tailored infrastructures [10, 19, 27]. On the other hand, topics such as how to distribute the system and the consistency model might stagger the design early on. The use of a monolith architecture, where the business logic of the system is interconnected, has the advantage that it does not require early modularization. The neat identification of modules occurs through refactorings, after initial development, which allows one to explore the application domain first [11]. 

Therefore, it is common practice to start with a monolith and, as the system grows in size and complexity, migrate to a more modular architectural approach, such as a modular monolith [12] or a microservice architecture. Since this architectural migration is not trivial [25], recent research has proposed approaches and tools to help the migration process [1, 2]. 

This has led to the development of Mono2Micro, a modular and extensible tool for the identification of microservices in a monolith system [20]. Mono2Micro focuses on identifying transactional contexts to inform its generated candidate decompositions [22]. To this end, it integrates several approaches, such as static code analysis of monolith accesses to domain entities [29], dynamic analysis of monolith execution logs [4], lexical analysis of abstract syntactic trees of monolith methods [8], and analysis of the history of monolith development [21]. Furthermore, Mono2Micro supports a set of measures and graph views to evaluate the quality of the generated candidate decompositions [28]. 

However, as with most research on the identification of microservices in monolith systems, Mono2Micro does not allow software architects to further model generated candidate decompositions using Domain-Driven Design (DDD) [7], which has shown good results on microservice design [33] and growing interest in the industry [34]. Instead, Mono2Micro representations of candidate decompositions are based on sequences of read and write accesses to the monolith domain entities, which are difficult to work with when trying to redesign the original monolith system and its functionalities for a modular architecture. 

https://doi.org/10.1145/nnnnnnn.nnnnnnn 

Levezinho et al. 

arXiv, June, 2024 

This paper addresses this problem by providing a representation of the Mono2Micro candidate decompositions in terms of automatically generated tactical and strategic DDD patterns. In this way, software architects can work on candidate decompositions from the perspective of DDD. 

This is achieved by extending the operational pipeline of Mono2Micro with a connection to Context Mapper, a DDD-focused modeling tool that provides a Domain-Specific Language, named Context Mapper DSL (CML). CML supports the declarative description of DDD domain models, using DDD concepts as building blocks of the language [16]. With this goal in mind, the following research questions are raised: 

- **RQ1** : How can current approaches to the identification of microservices in monolith systems be extended to include DDD? 

- **RQ2** : Can the results of a candidate decomposition based on entity accesses be represented in terms of DDD? 

- **RQ3** : Can an architect benefit from the use of a tool that integrates DDD when analyzing and working on a candidate decomposition? 

To answer these research questions, a real monolith system was used as a case study. The resulting candidate decompositions of this system were generated with and without the new DDD modeling capabilities and then compared. 

The remainder of this paper is structured as follows. Section 2 goes over the current literature on DDD application and microservice identification tools. Section 3 gives some background on the Mono2Micro and Context Mapper tools. Section 4 presents the solution to the aforementioned research questions. Section 5 provides the validation of the solution with a case study application, and in Section 6 the results and answers to the research questions are discussed. Finally, Section 7 concludes the paper. 

### **2 RELATED WORK** 

The application of DDD in microservice development, although widely practiced, is still poorly formulated [30]. Research on DDD modeling techniques is still sparse, especially in terms of modeling tools that leverage tactic and strategic DDD patterns [34]. 

Most research takes advantage of already developed models and diagram standards in the industry to convey DDD concepts. The use of annotated constructs is one of the most common approaches, such as in [26], where a mapping from DDD to UML is presented with the use of annotations inside UML class constructs, or in [18], where an annotation-based DSL was developed to scope objects and attributes within the concepts of DDD. However, they do not support all DDD patterns, especially strategic ones such as _Bounded Context_ relationships, which are useful when modeling microservices from candidate decompositions. 

Context Mapper is an exception to this, providing a DSL to model tactic and strategic DDD patterns [16], rapid model prototyping by deriving _Domains_ and _Bounded Contexts_ from use case definitions [17], and integration with other technologies such as Microservice Domain-Specific Language (MDSL) [15]. 

Other research also explores the extensibility of DDD to better fit other stages of software development. In [13] they define _Domain Views_ , which enable different stakeholders to perceive the domain 

model with their respective knowledge base. The Context Mapper tool also provides _Domain Views_ through the definition of types of _Bounded Context_ and _Context Maps_ [16]. 

On the other hand, there has been extensive and recent research on the identification of microservices in monolith systems [1]. These approaches provide a rich set of decomposition criteria and metrics to assess the generated decompositions. In particular, Mono2Micro [20] is a modular and extensible tool for those criteria and methods. However, these tools do not provide output that enables DDD-based editing and modeling, they mostly provide decompositions that are service-oriented and not domain-oriented. 

To our knowledge, the only tool that supports the reverse engineering of DDD concepts is the Discovery Library tool [16], which provides a way to reverse engineer domain models from Spring Boot<sup>1</sup> service APIs using discovery strategies. From the analysis of the code, it finds specific Spring Boot annotations and maps them to the corresponding DDD concepts. It generates _Bounded Contexts_ from @SpringBootApplication annotated classes and _Aggregates_ from @RequestMapping annotated classes. 

### **3 BACKGROUND** 

To better inform the integration of Context Mapper into the Mono2Micro pipeline, this section gives an overview of the architecture of both tools and compares them. 

### **3.1 Mono2Micro** 

Mono2Micro is a migration tool that provides candidate monolith decompositions composed of clusters of domain classes. This work initially focused on the identification of microservices driven by the identification of transactional contexts [22], but other strategies have been added [4, 8, 21]. 

Mono2Micro is designed as a pipeline, which is represented in Figure 1. The five stages of the pipeline are: 

- (1) _Collection_ : Implements several static and dynamic code collection strategies to represent monoliths, including representations based on accesses to source code domain entities, functionality logs, and commit history and authors. 

- (2) _Decomposition Generation_ : Partitions the monolith domain entities into clusters using a set of similarity criteria, with a focus on producing good quality decompositions. 

- (3) _Quality Assessment_ : Compares the decompositions and calculates the measures that are used to evaluate the generated decompositions. The measures include coupling, cohesion, size, and complexity. 

- (4) _Visualization_ : Depicts decompositions in the form of graphs with multiple levels of detail. Nodes and edges can represent different elements, depending on the chosen collection strategy. 

- (5) _Editing and Modeling_ : Provides an interface with operations to modify the automatically generated decompositions so that the architect can refine them. Quality measures are also automatically recalculated, if applicable. 

Each stage is composed of one or more modules that output artifacts for the next stage in the pipeline. The underlying model of 

1https://spring.io/projects/spring-boot 

Domain-Driven Design Representation of Monolith Candidate Decompositions Based on Entity Accesses 

arXiv, June, 2024 



**Figure 1: The five stages of the Mono2Micro operational pipeline [20]. Each stage can use the output of former stages as input.** 

the tool that makes up these modules and artifacts is also built with several extension points, making it possible to support multiple decomposition strategies. 

However, this pipeline does not include any way for an architect to model candidate decompositions using DDD after the _Decomposition Generation_ stage. More concretely, in the _Visualization_ stage, graph representations of the decomposition include cluster-based views of the decomposition domain entities, and functionality-based views that represent its sequence of accesses to domain entities ("Graphs" in Figure 1). There are no DDD-based views that show the model of each candidate microservice. Likewise, the _Editing and Modeling_ stage does not contain any operations related to the application of DDD. This is where Context Mapper comes in. 

### **3.2 Context Mapper** 

Context Mapper is a modeling framework that provides a DSL to design systems using DDD concepts. This DSL, henceforth called Context Mapper DSL (CML), was developed to unify the many patterns of DDD and their invariants in a concise language [16]. Figure 2 shows an example of the CML syntax, with the declaration of a _Context Map_ containing two _Bounded Contexts_ . 

Within _Bounded Contexts_ , one can define _Aggregates_ , which consist of a group of closely related domain objects that form a unit for the purpose of data consistency. This consistency is enforced inside the _Aggregate_ by its root _Entity_ , which represents the only entry point. For example, in Figure 2 the Customers aggregate has the Customer entity as its root. 

Although DDD focuses on the _Domain Layer_ of systems, where the business logic is residing, a CML Bounded Context can also represent the _Application Layer_ , which manages services that call different parts of the system, including processes in other layers. Using the Application keyword, _Application Services_ can be defined, among other constructs, and contain operations like createCustomer and getCustomer as represented in Figure 2. 

In addition to the CML language, Context Mapper also contains other utilities to facilitate modeling activities. These include the following: 

- (1) _Discovery Library_ : Implements several strategies to reverse engineer source code artifacts and represent them in CML [14]. 

- (2) _Architectural Refactoring_ : Includes operations to refactor and transform CML code for easier modeling. 



**Figure 2: Example syntax of CML, containing the syntax for defining a** **_Context Map_ (1-6);** **_Bounded Contexts_ (8-29, 31-32);** **_Aggregates_ (9-21);** **_Entities_ (10-15,17-20); and** **_Services_ (24-27).** 

- (3) _Diagram Generators_ : Provide translators to visualize CML artifacts in diagram form, such as UML representations of _Bounded Contexts_ and BPMN maps of _Aggregate_ states. 

Each of these features has similarities with the features in Mono2Micro. First, the Discovery Library performs a similar job as the Collectors of Mono2Micro, but more importantly, it provides a way to generate CML from its input. Second, the Architectural Refactoring (AR) module supports the architect on the edition and modeling of CML models, as the Editing and Modeling stage of Mono2Micro. However, AR operations are built on DDD concepts. Finally, the Diagram Generators module can provide ways to view a candidate decomposition from the perspective of DDD, also something missing in Mono2Micro, which presents decompositions as a graph of clustered domain entities. 

### **4 SOLUTION ARCHITECTURE** 

The proposed extension to the Mono2Micro microservice identification pipeline provides a representation of candidate decompositions in CML, so that DDD can be used for modeling and refactoring 

Levezinho et al. 

arXiv, June, 2024 

activities. Figure 3 shows this extension in terms of modules and their input and output artifacts. The top process bar represents the relevant stages of the Mono2Micro pipeline, and the different colors separate existing modules from new ones. The following sections, each corresponding to one of the research questions, explain each module and artifact in more detail. 

### **4.1 Tool Integration** 

Mono2Micro and Context Mapper are built with an emphasis on modularity and extensibility. This makes it viable for Context Mapper to integrate into the Mono2Micro pipeline. However, it is still important to respect the models of each tool to avoid compromising their internal cohesion. In practice, this meant pursuing a low-coupling solution when connecting the tools. This solution was achieved by leveraging on the Discovery Library (DL). 

As described in Section 3, the DL is a standalone tool capable of generating CML code. This is done using discovery strategies that translate input into CML. Since the DL was designed to be highly extensible, it also provides an API for the creation of these discovery strategies. Using this API, the Mono2Micro pipeline was extended with a module that defines new discovery strategies capable of translating candidate decompositions into CML. This module is represented by the _CML Translator_ in Figure 3. 

The _CML Translator_ has two stages. In the first, the internal representations of a decomposition in the Mono2Micro model are used to create a JSON contract that contains all the information needed to map a candidate decomposition to CML. This contract serves as input for the new discovery strategies and adds a layer of decoupling between the Mono2Micro model and the DL model, ensuring that changes made to the former do not inadvertently propagate to the latter. In the second stage, the new discovery strategies translate the contract to an internal representation of CML in the DL model. This model is, in turn, automatically converted to actual CML code. 

Figure 4 shows how DL is used in this process from the perspective of DDD. On the right, the DL acts as an _Anti-Corruption Layer_ , protecting its internal model from the Mono2Micro model present in the inbound contract. On the left, the DL model aligns closely with the CML model to facilitate the generation of CML, represented by the use of the _Conformist_ pattern. 

### **4.2 DDD Mapping** 

For the new discovery strategies to perform the translation to CML, the concepts that form a candidate decomposition must be mapped to the DDD concepts first. Since DDD and its concepts are structural in nature [7], a candidate decomposition was also structurally defined, based on its internal representation in Mono2Micro. 

A candidate decomposition is composed of three key concepts: **entities** , which represent domain classes in the monolith; **clusters** , which represent a set of entities grouped by similarity criteria through a clustering algorithm; and **functionalities** , which represent sequences of read/write accesses to entities in one or more clusters. 

Mapping a candidate decomposition to DDD corresponds to mapping these three concepts and understanding what information is needed from Mono2Micro once a DDD concept is chosen. Figure 5 

shows a summary of the achieved mappings, which are discussed in the next paragraphs. 

_4.2.1 Entity Mapping._ The entities of a candidate decomposition, by definition, are already based on the concept of _Entity_ from DDD, which facilitates this mapping. The main difference is that Mono2Micro does not require the internal structure of entities to generate candidate decompositions, while in DDD and CML the internal state and relationships with other entities are relevant information to model an _Entity_ . 

To guarantee a more complete translation of candidate decomposition entities into CML, a new source code collector module was added to the Mono2Micro Collection stage, aptly named _Structure Collector_ as shown in Figure 3. This module uses the Spoon Framework library [24] to analyze and collect structural information from entities in the monolith domain, including entity names, entity attributes, and relationships between entities, i.e. composition or inheritance. 

_4.2.2 Cluster Mapping._ The main criteria that dictate how entities are clustered in the Mono2Micro Decomposition stage are based on transactional similarity. This means entities commonly accessed together (i.e. read/write) during the same transactions are more likely to belong in the same cluster. Similarly, a DDD _Aggregate_ is defined as a group of tightly coupled domain objects that can be seen as a unit for the purpose of data changes during transactions, which makes it a good fit to represent a cluster. 

However, the concept of cluster also fits the concept of a DDD _Bounded Context_ . This is because clusters define physical boundaries between microservices in a candidate decomposition and can be evaluated based on coupling with other clusters in the same decomposition. This dual mapping of the cluster concept could be achieved with different variations in the number of generated _Bounded Contexts_ and _Aggregates_ , but in the end the chosen mapping was to take each cluster and generate a corresponding _Bounded Context_ and single _Aggregate_ inside it, which in turn contains all the entities in the cluster. 

Compared to other mapping combinations, this solution has several advantages. To start with, it satisfies all the given definitions of a cluster in Mono2Micro. In contrast, solutions such as mapping each cluster to an _Aggregate_ and adding all _Aggregates_ to a single _Bounded Context_ would remove the distributed nature on which the decomposition is based, and mapping each cluster to a single _Bounded Context_ while defining one _Aggregate_ per _Entity_ would completely ignore the transactional similarity that exists between entities on a cluster. This does not mean that the end product is to have one _Aggregate_ per _Bounded Context_ . It is important to remember that the generated CML code is by no means final and that further refactoring is expected by the architect doing the modeling. Starting from this initial mapping that satisfies the definition of a cluster, architects have the ability to further refine the model by partitioning the generated _Aggregate_ of each _Bounded Context_ using not only entity access information, but also the new structural context of entities that is not available in Mono2Micro. 

On the subject of this structural context, there is also a caveat to take into account. Entities that share structural relationships in the monolith are likely to end up in different clusters after decomposition. This makes it necessary to ensure that the generated CML 

Domain-Driven Design Representation of Monolith Candidate Decompositions Based on Entity Accesses 

arXiv, June, 2024 



**Figure 3: Mono2Micro pipeline extension to support CML representation of candidate decompositions. In blue, the relevant pipeline steps (top) and modules. In orange, the extension to the pipeline, composed of the addition of new modules.** 



**Figure 4: Generated Context Map diagram of the integration between Mono2Micro and Context Mapper. PL stands for** **_Published Language_ , ACL stands for** **_Anti-Corruption Layer_ , and CF stands for the** **_Conformist_ pattern.** 



**Figure 5: Mapping strategy of candidate decomposition concepts from Mono2Micro (M2M) to DDD and CML.** 

code does not contain _Entities_ directly referencing other _Entities_ in outer _Bounded Contexts_ . 

This problem is solved in two ways. First, when an _Entity_ references an outer _Entity_ , i.e. from an outer _Bounded Context_ , the _Context Map_ is updated with a relationship between _Bounded Contexts_ in the direction of the referenced _Entity_ . Second, this reference is replaced with a reference to a newly created local _Entity_ , which represents the outer _Entity_ locally. This is done so that the architect 

can better visualize which references in _Entities_ need to be refactored, facilitating the modeling work. Figure 6 shows an example of an outer reference being resolved. A comment is also automatically generated to make these references stand out. 



**Figure 6: Generated CML example, representing an** **_Aggregate_ that contains 2** **_Entities_ . Since Topic referenced an** **_Entity_ in its fields not present in the** **_Aggregate_ , Question_Reference was generated locally to replace this reference.** 

_4.2.3 Functionality Mapping._ Functionalities are more challenging to represent in DDD since each functionality is composed of a sequence of read and write accesses to entities, which is a concept very particular to Mono2Micro and without apparent DDD equivalent concept. Additionally, the sequence of accesses that represents a functionality can be quite extensive. The reason for this is the finegrained nature of the accesses collected from monolith code, due to their object-oriented design. This contrasts with the coarse-grained communication that is expected between microservices to avoid distribution communication costs. Without resolving this granularity issue, it becomes very impractical to represent functionalities compactly. 

Fortunately, Mono2Micro provides a Functionality Refactoring tool that rewrites the functionalities of a candidate decomposition as Sagas [3, 5]. The tool converts several fine-grained microservice invocations into some coarse-grained ones, incorporating the Remote Façade pattern in the decomposition. Refactoring the functionalities using this tool has an extreme positive effect on the granularity of the access sequences, so the Functionality Refactoring module is represented in Figure 3 as a crucial step in the extended pipeline. 

Refactoring functionalities as Sagas also makes a possible map to DDD more adequate. Although the Saga pattern is not a DDD 

Levezinho et al. 

arXiv, June, 2024 

pattern, in practice it can be used in conjunction with DDD to model distributed transactions [9]. Similarly, Context Mapper also supports constructs in addition to the original DDD patterns that enrich the modeling capabilities of the tool. For the case of functionality representation, the definitions of _Use Case_ and _Event Flows_ are the two most obvious constructs to use. However, they have some drawbacks. _Use Case_ definitions would imply reverse engineering of the functionalities as they are to a previous stage of the development cycle, losing in the process the information of the entity accesses and their Saga format. _Event Flows_ seem more plausible to model Sagas, but they would lock the architect into using Event-Driven Design for all functionalities, which should be left for the architect to decide later case by case instead of enforcing it through the automatic translation to CML. 

To supply a construct for the representation of Sagas meeting the current requirements, an expansion to the CML syntax was proposed and implemented in Context Mapper, which allows for the definition of distributed workflows without specifying the communication model of the process. For the current functionality mapping use case, this new concept can be used to simply state the steps of the saga, without any implementing technology commitments. 

This construct is called _Coordination_ , and is based on the coordination property of Sagas that specifies whether the steps of a Saga are orchestrated or choreographed [9], and nothing more. 

In CML, _Coordinations_ can be used to coordinate defined _Service_ operations, the same way a Saga coordinates steps. Figure 7 shows an example of the syntax in CML. _Coordinations_ are defined within the _Application_ layer of a _Bounded Context_ . To reference a _Service_ operation, a coordination step is divided into three segments, separated by the :: symbol: The name of the Bounded Context where the operation is defined; the name of the application _Service_ where the operation is defined; and the name of the operation. 

### **4.3 CML Representation and Interaction** 

When using Mono2Micro, architects now have the option to convert candidate decompositions to CML using the translation strategy mentioned so far. 

Like all CML discovery strategies, the initial representation of the candidate decomposition in CML is not final. Further refactoring is expected. However, an effort was made to automatically create a good starting point. The names of entities, clusters, and functionalities from the initial decomposition are maintained and used for naming _Entities_ , _Aggregates_ , _Bounded Contexts_ , and _Coordinations_ in CML. The conversion of the format of functionalities to Sagas also creates additional constructs, in the form of _Service_ operation calls, which correspond to _Coordination_ steps in CML. These operations make up the interface of each _Bounded Context_ in CML, but there is no straightforward name that can be used to name each operation. As such, several access-based naming heuristics were implemented in the translation strategy. Names are formatted with the names of entities, which are prefixed by the type of access and separated by a dash. For example, assuming that the sequence of accesses of the _Coordination_ in Figure 7 is: Tournament read for step 0; Quiz read/write and Question read/write for step 1; and Tournament write for step 2. Each service call name would be generated as rTournament, rwQuiz_rwQuestion and wTournament, respectively. The architect can further customize the level of detail they want the name to have regarding access information: 

- Full Access Trace: Transcribe the entire ordered entity access sequence that happens within an operation into the name of that operation; 

- Ignore Access Types: Omit the type of access to entities in operation names, i.e. read/write, replacing it with a "ac" prefix; 

- Ignore Access Order: Omit the type and order of access to entities in the operation names. 



**Figure 7:** **_Coordination_ construct in CML. The steps of the** **_Coordination_ (4-6) represent ordered calls to** **_Service_ operations (10,20,11).** 

Functionalities that do not access other _Bounded Contexts_ are simply mapped to a _Service_ , also defined in the _Application_ layer of the _Bounded Context_ where they are defined. 

Each heuristic used reduces the number of generated operations, at the cost of entity access details. In its most reduced form, each operation name shows which entities are accessed in that step. Access information is also added to each translated entity in the form of a comment, showing metrics related to the percentage of external and local accesses to the entity in comparison with the total external and local accesses to the _Bounded Context_ . In contrast to these heuristics, there is also the option to generate generic names for operations that are not access-based. These names are composed of the name of the functionality and the step number in the corresponding _Coordination_ , meaning each step of each _Coordination_ will call a unique operation. 

In terms of interaction, by opening this CML artifact in Context Mapper, architects have at their disposal a DDD-based view of the candidate decomposition, and several features to further refine, refactor, and visualize it. Table 1 shows some of these new features compared to what was previously available in Mono2Micro. Architects can refactor decompositions at a more structural level in CML. They can also use the additional DDD patterns present in CML to add to the initial translation, especially strategic ones, to define, for example, what type of relationships exist between the translated _Bounded Contexts_ . 

Domain-Driven Design Representation of Monolith Candidate Decompositions Based on Entity Accesses 

arXiv, June, 2024 

**Table 1: Operations in Mono2Micro and Context Mapper.** 

|**Mono2Micro**|**Context Mapper**|
|---|---|
|Expand / Collapse cluster views<br>Merge / Split clusters|Merge / Split Bounded Contexts<br>Merge / Split Aggregates|
|Transfer entities between clusters|Design Bounded Context Relationships|
|Rename clusters|Redesign Coordinations|
|Redesign functionalities|Redesign Entities|
|Analyse access-based measures|Generate UML / BPMN representations|



**Table 2: Candidate decomposition measures for the QT case study.** 

|**Cluster**|**Entities**|**Functionalities**|**Cohesion**|**Coupling**|**Complexity**|
|---|---|---|---|---|---|
|Cluster0|6|7|0.81|0.185|787.571|
|Cluster1|27|107|0.212|0.657|106.832|
|Cluster2|4|11|0.727|0.179|431.091|
|Cluster3|9|35|0.654|0.753|322.486|



### **5 CASE STUDY** 

Quizzes-Tutor (QT)<sup>2</sup> is an online quizzes management application developed for educational institutions. It can be used to create, manage, and evaluate quizzes composed of varying types of question formats. Teachers can add questions related to topics of the courses they preside over, while students can answer these questions within quizzes. Other functionalities include the creation of quiz tournaments between students, question proposals from students, and ways to discuss question answers. This real-world monolith, composed of 46 domain entities and 107 functionalities, was used as a case study to validate the Mono2Micro pipeline extension, which provides DDD modeling capabilities. 

### **5.1 Decomposition Generation** 

To start the validation, a candidate decomposition for the QT application must be generated and chosen. To this end, around 2000 candidate decompositions were generated with different values of similarity criteria and number of clusters. Candidate decompositions were then filtered on the basis of the values of their measures. The heuristic used was to order decompositions based on their coupling value in ascending order, and then based on their cohesion value in descending order, to prioritize decompositions with low coupling and high cohesion. Of the top 100 results, the candidate decomposition with the lowest complexity value was chosen. Data for this candidate decomposition can be seen in Table 2. Figure 8 also shows the clusters view of the decomposition shown in Mono2Micro. 

Table 2 shows two noteworthy pieces of information. To start with, the complexity of each cluster is very high. The complexity measure represents the migration cost of the functionalities in a cluster. This migration cost is measured as the cost of re-designing from an ACID context to a distributed one. Of the initial 107 functionalities, 31 involve distributed calls composed of several hops between clusters that drive the complexity high. This is because functionalities are still represented by the fine-grained monolith interactions between entities that can now be in different clusters. 

2https://quizzes-tutor.tecnico.ulisboa.pt/ 



**Figure 8: Mono2Micro decomposition visualization with finegrained interaction between clusters. Edges represent functionalities shared between clusters.** 

**Table 3: Refactored functionalities for QT case study. CGI stands for Coarse-Grained Interaction, and FGI stands for Fine-Grained Interactions.** 

|**Name**|**#Clusters**|**CGI**|**FGI**|**Reduction%**|
|---|---|---|---|---|
|concludeQuiz|3|4|73|94.52|
|getQuizByCode|3|4|33|87.88|
|getQuizAnswers|4|8|84|90.48|
|exportCourseExecutionInfo|4|9|110|91.82|
|importAll|3|5|119|95.8|
|createQuestion|2|3|24|87.5|
|getQuizAnswers|4|8|92|91.30|



To reduce this complexity, the _Functionality Refactoring_ tool represented in Figure 3 is used to create coarse-grained interactions between clusters. Table 3 shows the reduction of invocations for some of the QT functionalities. Applying this complexity reduction also makes it viable for functionalities to be represented in a structural language such as CML. Otherwise, any translation strategy would culminate in thousands of operation definitions for just a subset of the functionalities, as the FGI (Fine-Grained Interaction) values show in Table 3. 

The other noteworthy piece of information is the high number of entities inside Cluster1 compared to the other clusters, which means that the entities inside this cluster are more entangled when it comes to the functionalities that use them, and are more difficult to separate without creating an overly complex decomposition. It is also the reason for the non-optimal levels of cohesion and coupling in this cluster. At this stage, when some manual refactoring of functionalities is needed, modeling using DDD can help. 

The candidate decomposition is translated into CML by the discovery strategies, which outputs a .cml file with a representation of the candidate decomposition. Figure 9 shows a modified snippet of the generated CML, related to the ConcludeQuiz functionality of a decomposition. Without any optimization, the translation generates a total of 121 operations, used by 31 Coordinations that represent the distributed functionalities. With naming heuristics, the number of service calls can be reduced to 87 using _Full Access Trace_ , to 84 using the _Ignore Access Types_ , and to 48 using the _Ignore Access Order_ . Table 4 shows the reduction of generated services according to which heuristics are used per cluster. 

Regarding entity generation, a total of 11 reference entities were generated to signal structural dependencies between entities, also shown in Table 4, and every entity is generated with information 

Levezinho et al. 

arXiv, June, 2024 

**Table 4: Generated CML constructs. The number of services is represented by four values: No heuristics used;** **_Full Access Trace_ used;** **_Ignore Access Types_ used; and** **_Ignore Access Order_ used. The number of entities is represented by two values: original entities and reference entities. The most accessed entity is based on external accesses to the** **_Bounded Context_ .** 

|**Cluster**|**#Services**|**#Entities**|**Most Accessed Entity**|
|---|---|---|---|
|Cluster0|15/7/6/4|6/4|QuizAnswerItem (35.14%)|
|Cluster1|59/53/52/34|27/3|Quiz (12.2%)|
|Cluster2|11/5/5/2|4/0|QuestionAnswerItem (30.0%)|
|Cluster3|36/22/21/8|9/4|QuestionDetails/Image (16.46%)|



on the number of accesses to it, from the total _Bounded Context_ accesses (external and local), as shown in Figure 9. This information can help to refactor the decomposition further. For example, in Cluster3, there are 2 dominant entities out of 9 in terms of external accesses: QuestionDetails and _Image_ . These make them good possible candidates to serve as _Aggregate Roots_ to the _Bounded Context_ . A look at their structural relationships reveals that QuestionDetails also contains 3 subclass entities in the same cluster: MultipleChoiceQuestion, CodeOrderQuestion and CodeFillInQuestion; which in turn are structurally related to: Option, CodeOrderSlot, CodeFillInSlot and CodeFillInOption. Image is not structurally related to these, but its presence in this _Bounded Context_ means its commonly accessed together with the other entities. A possible first refactoring of this cluster could then be the separation of the Cluster3 _Aggregate_ into 2 _Aggregates_ , which is an automatic architectural refactor supported by CML. The first _Aggregate_ would control question types, formats, and related invariants with QuestionDetails as its _Aggregate Root_ . The second _Aggregate_ would represent a repository of images and be controlled through its Image _Aggregate Root_ . 

### **6 DISCUSSION** 

This section discusses the findings of applying the DDD-based extension to the operational pipeline of Mono2Micro by analyzing how the implemented solution and the results of its application in the case study answer the research questions raised in the introduction of this paper. 

### **6.1 Results Validation** 

Starting with the first research question (RQ1), to understand whether the Mono2Micro operational pipeline can be extended to integrate DDD, through the use of CML, the first step taken was to compare the architectural characteristics of each tool. 

Mono2Micro follows a pipe-and-filter architecture with its stages, and provides extension points in the form of abstractions for each stage; while Context Mapper follows a hub-and-spoke architecture, and also provides extension points in its core, the CML language, and each of its spoke modules, including the Discovery Library (DL). As described in the solution, these characteristics show that the tools emphasize modularity and extensibility, which made the 



**Figure 9: Snippet of the generated CML related to the functionality ConcludeQuiz. Triple dots (...) represent omitted constructs for the purpose of the example. Service operation names were also truncated.** 

development of an integration strategy that follows the same requirements possible. By measuring the level of modularity and extensibility of the solution, RQ1 can be evaluated. 

First, modularity deals with how divided a system is into logical modules that encapsulate specific self-contained functionality, improving separation of concerns and internal cohesion. The solution is composed of two new modules in Mono2Micro, the _Structure Collector_ and _CML Translator_ . In terms of cohesion, both modules respect the pipeline architecture of Mono2Micro, and are placed accordingly inside it based on their responsibilities. Regarding coupling, Figure 3 also shows the dependencies of each model. The _Structure Collector_ is highly decoupled, depending only on the monolith source code. It does not know about the subsequent stages of the pipeline. The _CML Translator_ has a contract between it and 

Domain-Driven Design Representation of Monolith Candidate Decompositions Based on Entity Accesses 

arXiv, June, 2024 

the Mono2Micro model, ensuring that it is only coupled to one source. 

Second, extensibility deals with how open for extension the features of a system are without putting at risk their core structure, improving the addition of new functionality. The _Structure Collector_ was designed from scratch. It provides abstractions for the collection of data from new frameworks and the collection of other types of structural data. The CML Translator is an extension of the DL API, so it follows that the discovery strategies implemented follow the same design and are also open to extension by providing abstractions. Additionally, the contract generation is also built with abstractions if new information is needed for future discovery strategies. 

Moving on to the second research question (RQ2), the mappings of the cluster, entity, and functionality concepts to DDD demonstrate how a candidate decomposition based on entity accesses can be represented with DDD concepts. Mono2Micro entities are already based on the concept of DDD _Entities_ , so the mapping is consistent in this regard. Further more, to improve usability, structural information about entities is collected for a more complete representation in CML. In the case of clusters, consistency was maintained by mapping each of them to a _Bounded Context_ and an _Aggregate_ . The structural context of the CML was also considered. To avoid having the cluster entities break the bounds of outer _Bounded Contexts_ with direct references, reference entities were added. This improves usability by highlighting where refactoring needs to be applied to entity relationships. For the mapping of functionalities, the sequence of accesses to entities that composed them was first converted into a structured Saga. This significantly reduced the complexity of the sequence in terms of size and hops between clusters, and made it simpler to represent with DDD, since Saga is a well-known pattern in distributed systems. Sagas were mapped to _Coordinations_ in CML, which encode an ordered sequence of service calls, just as Sagas encode a sequence of steps. To improve the usability of this mapping, hints to which entities are accessed in each service call were generated in the names of each service call. 

Finally, in regard to the third research question (RQ3), analyzing and comparing the decomposition artifacts represented in each tool, as demonstrated in the case study, can show how an architect can benefit from the use of this extension. 

In the case of entity representation, structural information is now available in the CML representation. This information is novel in regard to the old pipeline, as Mono2Micro representations can at most show the names of entities within each cluster, not its internal state or structural connections, as illustrated in the QT decomposition in Figure 8. With the CML representation of entities, it is possible to observe the attributes of each entity and also the structural refactorings that must be made in existing entities based on reference entities to other Bounded Contexts, demonstrated in Figure 9. 

In the case of clusters, _Aggregates_ can now be defined and used to further partition a cluster and its entities based on access patterns, access percentages, and the structural information provided at generation time in the form of commented constructs. 

In the case of functionalities, the architect now has the option of editing their Saga representation in CML, by editing the generated 

_Coordinations_ . Mono2Micro only allowed for the visualization of fine-grained functionality traces in a graph representation, and the Functionality Refactoring module of the tool only produced the data for the Sagas, without any way to edit or visualize them in a graphical representation. Using CML, these functionalities can be modeled as _Coordinations_ and edited in the language with the added context of the internal structure of the _Bounded Contexts_ they interact with. Furthermore, _Coordinations_ can be visualized in BPMN using a prompt to generate the diagram in BPMN Sketch Miner<sup>3</sup> . Figures 10 and 11 show the comparison of the views of a functionality that interacts with three of the four clusters before and after integration with CML. 

Additionally, the service naming heuristics allow the architect to reduce the number of generated service calls that exist in each cluster. This does not reduce the number of functionality steps but increases the level of reuse of services. 



**Figure 10: Graph representation of the ConcludeQuiz functionality in Mono2Micro, and the clusters that participate in it. Edge numbers represent the number of accessed entities in the clusters they point to.** 



**Figure 11: BPMN representation of the ConcludeQuiz** **_Coordination_ in Context Mapper, generated using BPMN Sketch Miner. The tasks in the diagram represent the steps of the** **_Coordination_ , and each participant (lane) represents the** **_Bounded Context_ where the step is defined.** 

### **6.2 Practical Relevance and Adoption** 

The problem addressed with the presented approach is of high relevance to practitioners, mainly software engineers and architects, who need to modernize existing monolith applications. Such monolith applications without an inner modular structure, a.k.a. _Big Ball of Mud_ [32], turned out to be a huge challenge in practice 

3https://www.bpmn-sketch-miner.ai 

Levezinho et al. 

arXiv, June, 2024 

for several reasons, which can also be seen as use cases for our solution presented in this paper: 

- **Economic reasons** : Maintaining a _Big Ball of Mud_ is often becoming expensive for software companies. Changing such applications, adding new features, or fixing bugs, often takes too much time because of the intertwined code base and dependencies within the system. 

- **Scalability and "Cloud readiness"** : Many companies have to decompose their applications to migrate to the cloud. The monolithic architecture approach is not scalable and does not fit the requirements for cloud deployment. 

- **Autonomous teams and "DevOps"** : Many companies aim to implement agile development approaches in which teams develop and operate their part of an application autonomously [31]. A team should be able to make its own design and architectural decisions, ideally without many dependencies towards other teams. This requires loosely coupled (micro)services or at least a system with loosely coupled modules. The structure of the organization (teams) defines the architecture of the software. 

As already mentioned, the adoption of DDD for service decomposition is widespread in the software industry. Both our tools, Mono2Micro<sup>4</sup> as well as Context Mapper<sup>5</sup> are open-sourced and, at least individually, have already gained some adoption in industry and real-world projects. The proposed approach is therefore foreseen as an important contribution and support for practitioners who want to: use a tool that automatically suggests decompositions for an existing monolith system; and want to express their future architecture and service decomposition in terms of DDD patterns and follow the "domain-driven" approach. Once a CML model is available, practitioners can benefit from all Context Mapper features: iterative and agile modeling, architectural refactorings, model visualization (diagram generators), or even code generation. 

### **6.3 Threats to Validity** 

With respect to internal validity, there are two points worth considering. First, the functionalities used in the decomposition and CML mapping process are all linear in nature. This is due to the existent static entity access collection tool in Mono2Micro, which flattens code branches into a single access sequence in a depth-first fashion. However, previous research that used the same sequences to develop the Saga representation of functionalities has shown this has little impact on the final results [5], and support for multiple traces per functionality is being developed. By extension, the current implementation of _Coordinations_ in CML is also based on linear Sagas. However, _Coordinations_ can be opened in BPMN Sketch Miner, where they can be further edited with more complex workflow logic. Context Mapper also supports branching processes in its _Event Flows_ , so the concept could be expanded to _Coordinations_ as well in the future. 

Second, the provided solution for resolving service operation names with access traces can sometimes generate verbose names, but these are meant to be temporary and only inform on what a certain step is doing, which is more appropriate and informative 

than the alternative of generating incremental "step" names. Future work could expand on the level of collected information to create heuristics based on method names to reduced verbosity. 

In terms of external validity, the current implementation assumes the use of Java and the Spring Boot JPA Framework to collect entity access and structure information, but the process is general enough to be applicable to other programming languages and frameworks. The modules that assume these limitations are also built with abstractions for the implementation of other technologies. 

The implementation of the solution is also realized by using Mono2Micro and Context Mapper, but this does not mean that a more general solution cannot be derived for other tools. Mono2Micro itself is designed as a generalization of the state of the art in microservice identification [20]. As for Context Mapper, the tool is built on top of the concepts and patterns of tactical and strategic DDD. If other tools follow representations of the same patterns, they can be used by the same mapping strategies applied to Context Mapper. 

### **7 CONCLUSION** 

A significant amount of research has been done on the migration of monoliths into a microservice architecture, but almost no tools incorporate mappings to DDD concepts in their migration processes. Research showed a trend for developing DSLs to represent DDD concepts and adapting the concepts to work in other diagramming tools to develop microservices, but to our knowledge never directly in a migration tool. 

Practitioners and software architects who need to migrate their current monolith architectures due to economic reasons, scalability, or more autonomous development teams would benefit from a solution that not only proposes candidate decompositions, but also automatically generated design-level DDD artifacts from that decomposition, as a starting point to facilitate the refactoring process towards a microservice architecture. 

This paper proposes a solution pipeline for this problem composed of the integration of Context Mapper, a modeling framework that provides a DSL to represent DDD patterns, into the Mono2Micro decomposition pipeline, a robust microservice identification tool. 

The proposed solution achieves the integration of both tools by defining a mapping of concepts between tools, whilst respecting each of the tool models. To support this mapping, the solution includes several new modules and modifications to the tools, including a new static collector of entity structural information, a contract for effective communication between the tools, a translation strategy to generate CML from Mono2Micro decompositions, i.e. entities, clusters, and functionalities, an extension to the CML syntax to support concepts from decomposition in the form of _Coordinations_ , and new diagram generators from CML based on translated decompositions. 

The artifacts developed in the project are publicly<sup>6</sup> available together with the description of the procedures necessary to use them. 

> 4https://github.com/socialsoftware/mono2micro 

> 5https://github.com/ContextMapper 

> 6https://github.com/socialsoftware/mono2micro/tree/master/tools/cml-converter 

Domain-Driven Design Representation of Monolith Candidate Decompositions Based on Entity Accesses 

arXiv, June, 2024 

### **ACKNOWLEDGMENTS** 

This work was partially supported by Fundação para a Ciência e Tecnologia (FCT) through projects UIDB/50021/2020 (INESC-ID) and PTDC/CCI-COM/2156/2021 (DACOMICO) 

### **REFERENCES** 

- [1] Manel Abdellatif, Anas Shatnawi, Hafedh Mili, Naouel Moha, Ghizlane El Boussaidi, Geoffrey Hecht, Jean Privat, and Yann-Gaël Guéhéneuc. 2021. A taxonomy of service identification approaches for legacy software systems modernization. _Journal of Systems and Software_ 173 (2021), 110868. 

- [2] Yalemisew Abgaz, Andrew McCarren, Peter Elger, David Solan, Neil Lapuz, Marin Bivol, Glenn Jackson, Murat Yilmaz, Jim Buckley, and Paul Clarke. 2023. Decomposition of Monolith Applications Into Microservices Architectures: A Systematic Review. _IEEE Transactions on Software Engineering_ 49, 8 (2023), 4213– 4242. https://doi.org/10.1109/TSE.2023.3287297 

- [3] João Franscisco Almeida and António Rito Silva. 2020. Monolith Migration Complexity Tuning Through the Application of Microservices Patterns. In _Software Architecture_ . Springer International Publishing, Cham, 39–54. https: //doi.org/10.1007/978-3-030-58923-3_3 

- [4] Bernardo Andrade, Samuel Santos, and António Rito Silva. 2023. A Comparison of Static and Dynamic Analysis to Identify Microservices in Monolith Systems. In _Software Architecture_ , Bedir Tekinerdogan, Catia Trubiani, Chouki Tibermacine, Patrizia Scandurra, and Carlos E. Cuesta (Eds.). Springer Nature Switzerland, Cham, 354–361. 

- [5] José Correia and António Rito Silva. 2022. Identification of monolith functionality refactorings for microservices migration. _Software: Practice and Experience_ 52, 12 (2022), 2664–2683. https://doi.org/10.1002/spe.3141 

- [6] Paolo Di Francesco, Patricia Lago, and Ivano Malavolta. 2018. Migrating Towards Microservice Architectures: An Industrial Survey. In _2018 IEEE International Conference on Software Architecture (ICSA)_ . 29–2909. https://doi.org/10.1109/ ICSA.2018.00012 

- [7] Eric Evans. 2003. _Domain-Driven Design: Tackling Complexity in the Heart of Software_ . Addison Wesley. 

- [8] Vasco Faria and António Rito Silva. 2023. Code Vectorization and Sequence of Accesses Strategies for Monolith Microservices Identification. In _Web Engineering_ , Irene Garrigós, Juan Manuel Murillo Rodríguez, and Manuel Wimmer (Eds.). Springer Nature Switzerland, Cham, 19–33. 

- [9] Neal Ford, Mark Richards, Pramod Sadalage, and Zhamak Dehghani. 2021. _Software Architecture: The Hard Parts_ . O’Reilly Media, Inc. 

- [10] Martin Fowler. 2015. Microservice Trade-Offs. Retrieved March 22, 2024 from https://martinfowler.com/articles/microservice-trade-offs.html 

- [11] Martin Fowler. 2015. Monolith First. Retrieved March 22, 2024 from https: //martinfowler.com/bliki/MonolithFirst.html 

- [12] Dan Haywood. 2017. In Defence of the Monolith. (2017). Retrieved March 22, 2024 from https://www.infoq.com/minibooks/emag-microservices-monoliths/ 

_Conference on Web Services (ICWS)_ . 50–56. https://doi.org/10.1109/ICWS60048. 2023.00019 

   - [22] Luís Nunes, Nuno Santos, and António Rito Silva. 2019. From a Monolith to a Microservices Architecture: An Approach Based on Transactional Contexts. In _Software Architecture: 13th European Conference, ECSA 2019, Paris, France, September 9–13, 2019, Proceedings_ . Springer International Publishing, Cham, 37– 52. https://doi.org/10.1007/978-3-030-29983-5_3 

   - [23] Charlene O’Hanlon. 2006. A Conversation with Werner Vogels. _Queue_ 4, 4 (May 2006), 14–22. https://doi.org/10.1145/1142055.1142065 

   - [24] Renaud Pawlak, Martin Monperrus, Nicolas Petitprez, Carlos Noguera, and Lionel Seinturier. 2015. Spoon: A Library for Implementing Analyses and Transformations of Java Source Code. _Software: Practice and Experience_ 46 (2015), 1155–1179. https://doi.org/10.1002/spe.2346 

   - [25] Francisco Ponce, Gastón Márquez, and Hernán Astudillo. 2019. Migrating from monolithic architecture to microservices: A Rapid Review. In _2019 38th International Conference of the Chilean Computer Science Society (SCCC)_ . 1–7. https://doi.org/10.1109/SCCC49216.2019.8966423 

   - [26] Florian Rademacher, Sabine Sachweh, and Albert Zündorf. 2018. Towards a UML Profile for Domain-Driven Design of Microservice Architectures. In _Software Engineering and Formal Methods_ . Springer International Publishing, Cham, 230– 245. https://doi.org/10.1007/978-3-319-74781-1_17 

   - [27] Chris Richardson. 2017. Developing Transactional Microservices Using Aggregates, Event Sourcing and CQRS. _InfoQ_ (2017). Retrieved March 22, 2024 from https://www.infoq.com/minibooks/emag-microservices-monoliths/ 

   - [28] Nuno Santos and António Rito Silva. 2020. A Complexity Metric for Microservices Architecture Migration. In _2020 IEEE International Conference on Software Architecture (ICSA)_ . 169–178. https://doi.org/10.1109/ICSA47634.2020.00024 

   - [29] Samuel Santos and António Rito Silva. 2022. Microservices Identification in Monolith Systems: Functionality Redesign Complexity and Evaluation of Similarity Measures. _Journal of Web Engineering_ 21, 5 (2022), 1543–1582. https: //doi.org/10.13052/jwe1540-9589.2158 

   - [30] Apitchaka Singjai, Uwe Zdun, and Olaf Zimmermann. 2021. Practitioner Views on the Interrelation of Microservice APIs and Domain-Driven Design: A Grey Literature Study Based on Grounded Theory. In _2021 IEEE 18th International Conference on Software Architecture (ICSA)_ . 25–35. https://doi.org/10.1109/ICSA51549. 2021.00011 

   - [31] Nick Tune and Scott Millett. 2017. _Designing Autonomous Teams and Services_ . O’Reilly Media, Incorporated. 

   - [32] Vaughn Vernon. 2016. _Domain-driven Design Distilled_ . Addison-Wesley. 

   - [33] Hulya Vural and Murat Koyuncu. 2021. Does Domain-Driven Design Lead to Finding the Optimal Modularity of a Microservice? _IEEE Access_ 9 (2021), 32721– 32733. https://doi.org/10.1109/ACCESS.2021.3060895 

   - [34] Ozan Özkan, Önder Babur, and Mark van den Brand. 2023. Domain-Driven Design in Software Development: A Systematic Literature Review on Implementation, Challenges, and Effectiveness. https://doi.org/10.48550/arXiv.2310.01905 arXiv:2310.01905 [cs.SE] 

- [13] Benjamin Hippchen, Pascal Giessler, Roland Steinegger, Michael Schneider, and Sebastian Abeck. 2017. Designing Microservice-Based Applications by Using a Domain-Driven Design Approach. _International Journal on Advances in Software (1942-2628)_ 10 (12 2017), 432 – 445. 

- [14] Stefan Kapferer. 2020. _A Modeling Framework for Strategic Domain-driven Design and Service Decomposition_ . Master’s thesis. University of Applied Sciences of Eastern Switzerland. https://doi.org/10.13140/RG.2.2.22950.68167 

- [15] Stefan Kapferer and Olaf Zimmermann. 2020. Domain-Driven Service Design. In _Service-Oriented Computing_ , Schahram Dustdar (Ed.). Springer International Publishing, Cham, 189–208. https://doi.org/10.1007/978-3-030-64846-6_11 

- [16] Stefan Kapferer. and Olaf Zimmermann. 2020. Domain-specific Language and Tools for Strategic Domain-driven Design, Context Mapping and Bounded Context Modeling. In _Proceedings of the 8th International Conference on Model-Driven Engineering and Software Development - MODELSWARD,_ . INSTICC, SciTePress, 299–306. https://doi.org/10.5220/0008910502990306 

- [17] Stefan Kapferer and Olaf Zimmermann. 2021. Domain-Driven Architecture Modeling and Rapid Prototyping with Context Mapper. In _Model-Driven Engineering and Software Development_ . 250–272. https://doi.org/10.1007/978-3-030-674458_11 

- [18] Duc Minh Le, Duc-Hanh Dang, and Viet-Ha Nguyen. 2018. On domain driven design using annotation-based domain specific language. _Computer Languages, Systems and Structures_ 54 (2018), 199–235. https://doi.org/10.1016/j.cl.2018.05.001 

- [19] James Lewis and Martin Fowler. 2014. Microservices. Retrieved March 22, 2024 from http://martinfowler.com/articles/microservices.html 

- [20] Telmo Lopes and António Rito Silva. 2023. Monolith Microservices Identification: Towards An Extensible Multiple Strategy Tool. In _2023 IEEE 20th International Conference on Software Architecture Companion (ICSA-C)_ . 111–115. https://doi. org/10.1109/ICSA-C57050.2023.00034 

- [21] João Lourenço and António Rito Silva. 2023. Monolith Development History for Microservices Identification: a Comparative Analysis. In _2023 IEEE International_ 

