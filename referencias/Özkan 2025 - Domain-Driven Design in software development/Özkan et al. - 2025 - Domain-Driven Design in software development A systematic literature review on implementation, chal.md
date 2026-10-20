The Journal of Systems and Software 230 (2025) 112537
Contents lists available at ScienceDirect
TheJournalofSystems&Software
journal homepage: www.elsevier.com/locate/jss
Domain-DrivenDesigninsoftwaredevelopment:Asystematicliterature
(cid:73)
reviewonimplementation,challenges,andeffectiveness
Ozan Özkana ,∗, Önder Babura,b , Mark van den Branda
aMathematics and Computer Science, Eindhoven University of Technology,Eindhoven,The Netherlands
bInformation Technology Group, Wageningen University and Research,Wageningen,The Netherlands
A R T I C L E I N F O A B S T R A C T
Keywords: Context:Domain-Driven Design (DDD) has gained significant attention in software development for its poten-
Domain-Driven Design tial to address complex software challenges, particularly in the areas of system refactoring, reimplementation,
DDD and adoption. Using domain knowledge, DDD aims to solve complex business problems effectively.
Software architecture Objective:This SLR aims to provide an analysis of existing research on DDD in software development, paint
S
S
o
ys
ft
t
w
em
ar
a
e
t i
d
c
e
l
v
it
e
e
l
r
o
a
p
t
m
ur
e
e
n
r
t
eview
a picture of DDD in solving software problems, identify the challenges encountered during its application and
explore the results of these studies.
Method:We systematically selected 36 peer reviewed studies and conducted quantitative and qualitative
analyzes to synthesize the findings.
Results:DDD has effectively improved software systems, with its key concepts. The application of DDD in
microservices has gained prominence for its ability to facilitate system decomposition. Some studies lacked
empirical evaluations, highlighting challenges in onboarding and the need for expertise.
Conclusion:Adopting DDD benefits software development, involving stakeholders such as engineers, archi-
tects, managers, and domain experts. More empirical evaluations and open discussions on challenges are
needed. Collaboration between academia and industry advances the adoption and transfer of knowledge of
DDD in projects.
1. Introduction tify and address software architecture challenges effectively (Evans,
2004; Vernon, 2013). This approach provides guidance on how to
In the field of software development, the pursuit of effective design improve system quality, maintainability, and scalability by ensuring
methodologies and architectural approaches has been a crucial en- that software design closely mirrors the business domain Evans (2004).
deavor for both researchers and practitioners. Among these approaches, Although DDD presents solutions with its conceptual elegance and
DDD has gained significant attention and adoption, particularly in the potential benefits in managing software architecture challenges (Evans,
context of solving software architecture problems and addressing chal- 2004; Vernon, 2013), it is crucial to evaluate its practical application
lenges related to refactoring, reimplementation and adoption (Avram and assess its impact on software development projects. This Systematic
and Marinescu, 2006). DDD, as advocated by Eric Evans in his influ- Literature Review (SLR) aims to provide a comprehensive analysis of
ential book, ‘‘Domain-Driven Design: Tackling Complexity in the Heart existing research studies that have used DDD for various purposes in
of Software’’ (Evans, 2004), offers a framework for understanding, software development, such as improving system design, enhancing
modeling, and solving complex business problems by placing domain maintainability, and facilitating communication between stakeholders.
knowledge at the core of the design process.
By analyzing and synthesizing empirical studies, we aim to gain insight
DDD emphasizes the alignment of software systems with the un-
into the effectiveness of DDD in solving software architecture problems
derlying business domain, enabling developers to better understand
and identify the challenges encountered during the application of DDD
and model complex business requirements. By capturing the language,
from these studies.
concepts, and relationships within the domain, DDD helps to iden-
(cid:73)
Editor: Patricia Lago.
∗ Corresponding author.
E-mail address: o.ozkan@tue.nl (O. Özkan).
https://doi.org/10.1016/j.jss.2025.112537
Received 24 December 2024; Received in revised form 1 May 2025; Accepted 13 June 2025
Available online 27 June 2025
0164-1212/© 2025 The Authors. Published by Elsevier Inc. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-
nc-nd/4.0/) .

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
To achieve this objective, a rigorous research methodology was 1.1.2. Bounded context
employed that adheres to established guidelines proposed by Kitchen- The Bounded Context concept effectively sets the boundaries of
ham and Charters (2007) and Wohlin (2014). A group of 36 peer- distinct zones where the semantics of a domain model are consistently
reviewed studies was systematically selected and quantitative and qual- applied. In applications of substantial scale that incorporate a variety
itative analyzes were performed based on the data extracted from these of domain models, there is an inherent risk of ambiguity and mis-
studies. alignment. Bounded Contexts serve as strategic divisions, separating
The conclusion drawn from this SLR emphasizes the potential bene- different domain models to maintain their integrity. This approach
fits of adopting DDD in software development. The study highlights the confines each domain to specific contexts, thus preventing semantic
importance of involving key stakeholders, including software engineers, conflicts and ensuring a unified representation of the business domain
architects, project managers, and domain experts, to ensure a successful within each delimitated area (Evans, 2004). It can serve as an ab-
implementation. In addition, the study identifies the importance of straction of a (sub-)system or team, aligning boundaries with software
open discussions on challenges and limitations and emphasizes the components, organizational structures, and responsibilities.
collaboration between academia and industry to advance the adoption
of DDD and the transfer of knowledge in real-world projects. 1.2. Context mapping
This study contributes to the growing body of knowledge on DDD
and provides valuable insights for practitioners and researchers seeking In DDD, Context Mapping is a strategic practice used to understand
to apply the principles of DDD effectively in software development. and manage the relationships between different bounded contexts in
By identifying the strengths and weaknesses of existing research and complex software systems (Evans, 2004). A Bounded Context defines
proposing areas for improvement, this SLR aims to foster the further the boundary within which a particular domain model is defined and
advancement and adoption of DDD principles in contemporary software applicable. However, in real-world systems, multiple teams often work
development projects. on different subdomains or systems, each with its own Bounded Con-
text. These contexts must interact and integrate, which introduces the
1.1. Domain-Driven Design essentials risk of model contamination or ambiguity across teams.
Context Mapping provides a visual and conceptual technique to
DDD is a conceptual framework and approach to software de- explicitly define how bounded contexts relate to each other and how
velopment in software engineering that seeks harmony between the integration should be handled. It helps development teams determine
structure of software code and the complexities of the business domain appropriate integration patterns (e.g., Shared Kernel, Customer/Sup-
it serves. The goal of DDD is to bridge the gap between technical plier, Conformist, or Anti-Corruption Layer) depending on the nature
implementation and business requirements, resulting in more effective of team collaboration, legacy constraints, or organizational structure.
communication between developers and domain experts (Evans, 2004; These relationships are represented using a Context Map, which be-
Vernon, 2013). This concept was pioneered by Eric Evans, whose comes an essential communication artifact in large systems involving
significant book Domain-Driven Design: Tackling Complexity in the Heart multiple teams and domains.
of Software (Evans, 2004) has shaped this paradigm. Evans emphasizes Evans emphasizes that strategic design decisions are essential when
the alignment of software design with the intricate nuances of the busi- teams develop models in parallel, and that context mapping serves as
ness domain. He argues that effective software development requires a bridge to align models and avoid conflicts (Evans, 2004). In prac-
a deep understanding of the complexities of the domain, allowing tice, context maps also guide technical implementation, by informing
developers to create software that genuinely resonates with real-world decisions about API design, data ownership, and service integration. As
needs (Evans, 2004). such, context mapping is a vital part of ensuring semantic consistency
In DDD, the domain refers to the specific area of expertise or the and architectural integrity across distributed systems.
subject matter of the software application. This could be anything
from e-Commerce, finance, healthcare, or logistics. The central concept 1.2.1. Aggregates
in DDD is the development of a rich, well-defined domain model The concept of Aggregates encapsulates Entities, Value Objects, and
that accurately represents the business rules, processes, and entities Domain Logic through methods in entities and the use of domain ser-
within the domain. This model is built through collaboration between vices. Aggregates are the main points for accessing and changing data,
developers and domain experts, often using a shared language called ensuring data integrity within business transactions (Evans, 2004).
Ubiquitous Language that captures both technical and domain-specific By containing data within defined boundaries, Aggregates optimize
terms. data management and system scalability while also enforcing logical
Through its concepts, which are explained in the following sections, boundaries that prevent uncontrolled data manipulation.
DDD introduces principles that help software architects effectively rep-
resent the complex aspects of the real world. By embracing these core 1.2.2. Entities and value objects
tenets, software engineers navigate the complex landscape of software Entities and Value Objects differentiate within the DDD framework.
development with a compass calibrated to the nuances of the domain, Entities embody tangible elements within the domain, each possess-
thus achieving a symbiotic fusion of technical precision and domain ing a unique identity. These entities change over time, capturing the
understanding. mutable aspects of the business reality (Evans, 2004). In contrast,
Value Objects represent conceptual attributes that lack identity and
1.1.1. Ubiquitous language remain immutable. By distinguishing between these two constructs,
At the core of DDD lies the concept of Ubiquitous Language, a DDD provides a complete representation of the domain, accurately
practice that aims to bridge the gap between technical jargon and modeling tangible entities and abstract attributes (Evans, 2004).
domain-specific vocabulary (Evans, 2004). Ubiquitous Language fosters
a shared vocabulary that harmonizes conversations among develop- 1.2.3. Domain services
ers, domain experts, and business stakeholders. By encapsulating the Domain Services encapsulate domain logic that transcends individ-
complexities of the business domain in a common understanding, Ubiq- ual entities and value objects (Evans, 2004). These services orchestrate
uitous Language eliminates ambiguity and streamlines communication. complex operations and interactions within the domain. By segregating
This shared linguistic framework empowers stakeholders to articulate multifaceted logic, domain services promote modular, reusable, and
domain intricacies effortlessly and translates directly into the software’s concise code. This approach mirrors the coherent coordination of real-
code, facilitating a direct and unambiguous translation of domain world processes, enhancing the software’s alignment with the domain’s
understanding into the software’s design and implementation. intricacies.
2

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
1.2.4. Domain events 1.2.9. Event storming
Domain Events is a concept used to model and communicate chang- In addition to modeling patterns, DDD also includes collaborative
es or significant occurrences within a domain Vernon (2013). They play modeling techniques that help bridge the gap between business and
a role in capturing and representing the behavior and state changes technical stakeholders. One widely adopted practice is Event Storming,
within an application’s core domain. A Domain Event is a lightweight a workshop-based approach introduced by Alberto Brandolini (Bran-
object that represents something important that has happened in the dolini, 2013), where domain experts and developers collaboratively ex-
domain. These events are usually named in the past tense to indicate plore business processes by identifying and organizing domain events,
that they have already occurred. They help decouple different parts of a commands, aggregates, and actors. This method is particularly effective
system by allowing different components or aggregates to communicate for discovering Bounded Contexts and aligning the domain model with
without needing to know the specifics of each other. This promotes a real-world business operations.
more modular and maintainable architecture.
1.2.10. Other DDD patterns and concepts
1.2.5. Anti-Corruption Layer (ACL) The DDD patterns and concepts introduced in this section reflect
The concept of an ACL protects the domain model from external those discussed most frequently in the 36 primary studies reviewed.
influences. This layer mediates interactions between different models or Although there are additional patterns in the DDD literature, such as
systems, preserving the domain’s integrity. By translating data between Customer/Supplier, Open Host Service, Conformist, and Published Lan-
disparate representations, the ACL ensures a consistent domain model, guage, these were not consistently represented in the reviewed studies
safeguarding it from external distortions (Evans, 2004). and, therefore, were not included in detail. Our goal in this section is
to provide a focused overview of the key patterns that emerged from
1.2.6. Core domain the literature rather than an exhaustive catalog of all DDD concepts.
Core Domain is a central concept of strategic design in DDD, which
refers to the part of the software system that delivers the most value 2. Related work
and differentiates the business. The goal is to focus development effort
on the Core Domain to gain competitive advantage, often assigning the To the best of our knowledge, despite the growing interest in
most skilled developers to it (Evans, 2004). DDD as a software development approach, there is a scarcity of SLRs
specifically focused on DDD. While the literature landscape on DDD
1.2.7. Shared kernel is not completely unexplored, previous studies have primarily touched
Shared Kernel refers to a pattern in which two Bounded Contexts upon certain aspects remotely related to DDD.
share a common subset of the domain model. This shared part must be For instance, Le et al. (2016) propose a set of concrete design
carefully managed to avoid conflicts and preserve the integrity of the patterns for Domain Modeling within the context of Object-Oriented
model, often requiring close collaboration and coordination between DDD, providing valuable insights into the practical application of DDD
teams (Evans, 2004). in specific modeling scenarios. Singjai et al. (2021a), on the other
The ACL shares similarities with several well-known design pat- hand, examine the interrelation between microservice APIs and DDD,
terns. For instance, the Remote Proxy pattern (Gamma et al., 2009) shedding light on how DDD principles can be applied in the con-
provides a local representative for an object that resides in a different text of microservices architecture. However, it is worth noting that
address space, mediating interactions between local and remote sys- some related systematic literature reviews have been conducted in
tems. The Wrapper pattern (Buschmann, 1996) encapsulates an object adjacent domains. De Goey et al. (2019), for instance, undertakes a
to provide a different interface, much like the ACL encapsulates ex- Systematic Literature Review on Design-Driven Innovation, exploring
ternal systems to present a consistent interface to the domain model. design-driven approaches and methodologies in innovation processes,
The Adapter pattern (Gamma et al., 2009) converts the interface of a which, although related to design-driven practices, do not directly
class into another interface that a client expects, similar to how the address the specific principles and patterns of DDD. Similarly, Bertoni
ACL adapts external data representations to match the internal domain (2020) conducts an SLR on Data-Driven Design in Concept Develop-
model. ment, focusing on the role of data-driven approaches in the early stages
The fundamental contribution of DDD lies in creating software of concept development but not explicitly addressing the nuances of
systems that closely mirror the business’s cognitive schema. By converg- DDD.
ing domain experts, business stakeholders, and software developers, Despite valuable contributions from these studies, none of them pro-
DDD facilitates synergistic collaboration to deliver software solutions vide a comprehensive review of DDD as a whole, addressing its princi-
that optimally cater to business needs. This collaborative effort fosters ples, methodologies, and practical applications. While these prior stud-
the combination of domain insights, augments the comprehension of ies offer valuable perspectives related to design-driven or microservice-
problems and solutions across the entirety of the development team, oriented software development, they do not conduct a structured or
and supports the fostering of inter-team relationships. comprehensive SLR focused on the conceptual and practical aspects
of DDD itself. In contrast, our study takes a DDD-centric perspective,
1.2.8. Strategic and tactical DDD systematically analyzing how DDD principles, patterns, and stakehold-
Over time, the DDD community has categorized DDD patterns into ers are discussed and applied in peer-reviewed literature. This focus
two broad groups: Strategic and Tactical. Evans also has a similar enables us to capture insights specifically tied to DDD adoption, effec-
categorization in his book (Evans, 2004) as he calls it Strategic Design, tiveness, and evaluation, filling a gap not directly addressed by adjacent
but the community calls it as Tactical Design as of today. It has become literature.
a widely adopted framing, especially in practitioner literature such as
Vernon’s work (Vernon, 2013). Strategic DDD focuses on aligning the 3. Research objectives and method
software model with the broader business strategy and organization,
with key concepts including Bounded Context, Core Domain, Context This study employed a Systematic Literature Review methodology
Maps, and Anti-Corruption Layer. In contrast, Tactical DDD includes to create generalizable empirical results (as opposed to specific and in-
concrete modeling techniques used within a Bounded Context, such depth yes less generalizable research methods such as case studies (Stol
as Entities, Value Objects, Aggregates, Domain Services, and Domain and Fitzgerald, 2018)) to (1) consolidate the existing knowledge on the
Events. Throughout this study, we use this distinction as a lens to utilization of DDD in the domain of software development, (2) identify
interpret the usage patterns of DDD concepts in the literature. gaps in the current research, guiding future studies and helping to
3

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
focus on underexplored areas, and (3) for practitioners, a comprehen- Table 1
sive review can offer insights into best practices, common challenges, List of exclusion and inclusion criteria.
and effective strategies for implementing DDD in real-world projects. Exclusion criteria
The research approach adhered to established guidelines as proposed EC1 Duplicate papers from multiple sources.
by Lübke et al. (2019) and Wohlin (2014). EC2 Papers without full text available.
EC3 Papers not written in English.
Additionally, this study delves into further detail regarding the Goal
EC4 Books, book chapters, editorials, issue introductions.
and Research Questions (Section 3.1), Search Strategy and Data Sources EC5 Papers are not primary studies.
(Section 3.2), Exclusion Criteria (Section 3.3), Primary Study Identifi- EC6 Papers do not explicitly introduce a method, technique,
cation and Selection (Section 3.4), and Data Extraction (Section 3.5) tool and/or evaluation of adaptation or extension.
in subsequent sections. By examining these aspects in a meticulous Inclusion Criterion
manner, this study aims to provide a comprehensive and rigorous Papers do not meet any exclusion criteria.
analysis of the research topic at hand.
3.1. Goal and research questions
3.3. Exclusion criteria
The primary objective of this research is to investigate and synthe-
The establishment of selection criteria was undertaken with the
size the current state of research on the application of DDD in software
aim of mitigating bias and minimizing subjectivity within the study.
development, to understand its benefits, challenges, used patterns,
The inclusion and exclusion criteria were formulated in accordance
and effectiveness. To achieve this objective, the following research
with the research questions (RQs) as delineated by Kuhrmann et al.
questions (RQ)s have been formulated:
(2017), thereby ensuring that the criteria align closely with the in-
RQ1: What is the state of the art concerning DDD in the existing tended objectives of the investigation. Following our criteria, (1) we
literature, in terms of study types, research venues, software meticulously identified and removed duplicate studies that appeared
systems, and the distribution between academic and industrial in more than one of the selected databases to prevent the inclusion
settings? of redundant information. To maintain the comprehensiveness of our
RQ2: What categories of software systems have demonstrated analysis, (2) we excluded studies that lacked full-text availability, as
benefits from the implementation of DDD? the absence of complete content may hinder a thorough evaluation of
RQ3: Which specific software development concerns have been the study’s findings and methodology. Given the language limitations
addressed through the application of DDD in previous studies? of our review team, (3) we restricted our analysis to studies written in
RQ4: What are the most common DDD patterns utilized in previ- English to ensure accurate and consistent interpretation and analysis.
ous research, such as ACLs, Bounded Contexts, and other related In the interest of focusing on primary research articles, (4) we excluded
approaches? books, book chapters, editorials, and issue introductions from our
RQ5: What are the challenges encountered during the implemen-
analysis, as they may not present original empirical studies or detailed
tation of DDD in software development projects?
investigations. (5) We excluded studies that were not primary research
RQ6: How has the effectiveness of DDD been assessed and mea-
studies (e.g., review articles, meta-analyses, opinion pieces) to maintain
sured in prior studies?
a clear focus on empirical research directly relevant to our research
RQ7: Who are the key stakeholders involved and benefited in the
questions. To ensure the inclusion of studies closely related to DDD and
implementation of DDD?
its practical applications, (6) we excluded studies that did not explicitly
present or discuss the introduction of a method, technique, tool, or
3.2. Search strategy and data sources
evaluation pertaining to DDD or its adaptation and extension. The list
of the exclusion criteria can be seen in Table 1.
In line with established protocols and our previous studies (Gi-
ray et al., 2023; Ochoa et al., 2025), we meticulously designed our 3.4. Primary study identification and selection
search strategy to identify pertinent studies from reputable academic
databases renowned for their extensive coverage of computer science 3.4.1. Conducting manual database search
and software engineering literature . The databases utilized in this In the first stage, we performed a meticulous and systematic manual
study were ACM, SpringerLink, IEEE, and Wiley, all of which are widely search of the databases mentioned in Section 2.2. The search was
recognized for their authoritative and diverse repositories of articles. carried out in March 2023 and yielded a total of 707 studies, which
The search query employed in this investigation was thoughtfully were 153 studies from ACM, 19 studies from IEEE Xplore, 510 studies
crafted to encompass a broad spectrum of articles relevant to our from SpringerLink, and 25 studies from Wiley, as also shown in Table
research objectives. The query utilized a combination of keywords and 4. To ensure the exclusion of duplicate results, we conducted conflict
logical operators to target studies explicitly discussing DDD in conjunc- resolution, resulting in the identification of one duplicate paper. After
tion with software development activities. We used ‘‘Domain-Driven eliminating duplicates, we advanced 706 unique studies to the next
Design’’ because we explicitly wanted to capture studies that employed stage of the selection process .
DDD. When using only ‘‘Domain-Driven Design’’, we encountered a
significant number of false positives, such as studies from medicine. 3.4.2. Applying exclusion criteria
Therefore, to ensure the relevance of the captured studies, we included In the second stage, we applied our predefined exclusion criteria to
implementation keywords to specifically address studies that employed the 706 studies. The screening process involved the assessment of each
DDD in practice. The search query was formulated as follows: paper based on its title, abstract, and keywords. In situations where
a thorough evaluation was not possible based on these elements, we
"Domain Driven Design" AND (refactor* OR improv* OR optimiz* briefly reviewed the introduction and conclusion of the paper, follow-
OR restructur* OR migrat* OR evolution OR cleanup OR ing the guidelines suggested by Wohlin (2014). To ensure a rigorous
reengineering) assessment, we adopted a multi-assessor strategy, where 2 authors
independently evaluated the studies without knowing each other’s
We strategically used asterisks (*) as wildcards to capture variations assessments. Due to the high number of studies, we performed the
of the specified keywords and to ensure inclusivity in the search results. assessment in iterations until we achieved at least 0.80 Cohen’s Kappa
4

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
Fig. 1. Study selection progressed from a database search to the quality assessment. The final set of primary studies advanced to the data extraction stage. The count of studies
in the evaluation steps is displayed in parentheses.
Table 2 centralized indexing of our target databases mentioned in Section 3.2
Number of studies excluded per criterion during the screening process. and to eliminate results from grey literature. The screening process for
Count of studies excluded per criterion Evans’ book forward snowballing followed the same strategy as that
EC1 11 studies excluded as duplicates across databases. used for forward snowballing in the primary studies. In the process of
EC2 15 studies excluded due to lack of full-text access. analysis, a comparison was made among the database search results,
EC3 0 studies excluded for being in non-English languages.
EC4 461 studies excluded as books, editorials, or chapters.
forward snowballing results, and the previously identified studies to
EC5 53 studies excluded as they were not primary studies. identify any potential duplicates. As a result, a total of 10 duplicate
EC6 147 studies excluded for not introducing or evaluating studies were identified, and these duplicates were subsequently re-
DDD methods, tools, or adaptations. solved in favor of the database search results and forward snowballing
Total 687 studies excluded across all criteria. outcomes. Consequently, an additional 15 studies that did not meet
any of the exclusion criteria were identified and subsequently included
in our study. The comprehensive forward snowballing process, en-
compassing both the forward snowballing of included studies and the
coefficient (Cohen, 1960), which indicates almost perfect agreement
examination of studies cited in Evans’ book, resulted in a total of 23
between the assessors (Cohen, 1960). Once the desired Cohen’s Kappa
studies being incorporated into our analysis.
was reached, the first author continued to assess the remaining studies
to determine their inclusion or exclusion, following the approach done
We also performed forward snowballing following Wohlin et al.
in previous studies (Torres et al., 2021; Wang et al., 2023). In each
guidelines (Wohlin, 2014), we used Google Scholar to identify studies
iteration, we randomly selected 30 studies for assessment. After each
that cited our included primary studies. We assessed these additional
iteration, we conducted conflict resolution sessions to discuss the ra-
studies based on their title, abstract, and keywords, using the exclusion
tionale of our assessments. We eventually achieved 1.0 Cohen’s Kappa
criteria established earlier. In cases where a definitive resolution was
coefficient in the second iteration. The remaining studies were evalu-
not achievable based on the provided information, we conducted a
ated by the first author, resulting in 31 studies marked for inclusion
rapid analysis of the entire paper, as suggested by Wohlin (2014).
and progression to the next stage. The distribution of these included
Through this process, we identified 8 studies that did not meet any of
studies across the search databases is presented in Table 4.
the exclusion criteria and were therefore included in our study.
Table 2 provides a detailed breakdown of the number of studies
excluded under each exclusion criterion. This complements the overall 3.4.4. Quality assessment
metrics shown in Table 4, providing transparency on how rigorously During stage 4 of our primary study identification and selection
the exclusion process was applied. process, we proceeded with the task of conducting a comprehensive
quality assessment of the selected studies. Adhering to the established
3.4.3. Conducting forward snowballing guidelines put forth by Kitchenham and Charters (2007), each study
In the third stage, we conducted forward snowballing to make was meticulously evaluated, with ratings assigned on a scale ranging
our study population wider and ensure relevancy. We conducted the from 0 to 1. On this scale, a rating of 1 denoted a positive affirmation,
forward snowballing in two approaches. We conducted a forward snow- 0.5 indicated a partial fulfillment of the quality criteria, and 0 repre-
balling process for studies that cited Evans’ book (Evans, 2004) since sented a negative response. The specific quality assessment questions
Evans holds significant prominence in the field of DDD due to his influ- utilized in this evaluation can be found in Table 3. Studies that achieved
ential contributions. His book, which serves as a reference, has gained a total score of 4 or higher were deemed to have successfully met the
substantial recognition and is widely regarded as a crucial resource quality assessment criteria and were subsequently included in the data
among practitioners in the software development community (Avram extraction stage. In order to maintain the rigor and objectivity of the
and Marinescu, 2006; Vernon, 2013, 2016; Nilsson, 2006). To conduct process, we adopted a multi-assessor strategy during the quality assess-
this snowballing, we utilized Scopus as a database because of its ment stage. Each study was independently evaluated by two assessors.
5

O. Özkan et al.
The Journal of Systems & Software 230 (2025) 112537
| Table 3 |     |     |     | Table 5 |     |     |     |
| ------- | --- | --- | --- | ------- | --- | --- | --- |
List of quality criteria adopted from Kitchenham et al. guidelines (Kitchenham and  Data extraction form.
Charters, 2007). Each criterion is rated on a scale of 0 to 1. Studies that achieved a   Category Input type
|     |     |     |     |     | Field |     | RQ  |
| --- | --- | --- | --- | --- | ----- | --- | --- |
score of >=4.0 advanced to the data extraction stage.
|      |                                         |     |     |                      | ID     | Auto Alphanumeric | –     |
| ---- | --------------------------------------- | --- | --- | -------------------- | ------ | ----------------- | ----- |
|  #   | Quality criteria                        |     |     | atadateM noitacilbuP |        |                   |       |
|      |                                         |     |     |                      | Title  | Free Text         | RQ1   |
|  QC1 | The aim of the study is clearly stated. |     |     |                      |        | Free Text         |       |
|      |                                         |     |     |                      | Author |                   | RQ1   |
 QC2 The scope and context of the study are clearly defined.     Item Type Selection RQ1
 QC3 The study is variable, valid and reliable.     Database Selection RQ1
 QC4 The research process of the study is documented properly.    Publication Year
|     |     |     |     |     |     | Number | RQ1 |
| --- | --- | --- | --- | --- | --- | ------ | --- |
 QC5 The research questions in the study are answered.     Free Text
|     |     |     |     |     | Publisher |     | RQ1 |
| --- | --- | --- | --- | --- | --------- | --- | --- |
 QC6 Negative findings in the study are presented.     Source Selection RQ1
|  QC7 | The main findings are clearly stated. |     |     |     |     |     |     |
| ---- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
 QC8 Conclusions relate to the aim and purpose of the study.     Study Design Selection RQ1
|         |     |     |     |                       | Data Collection Methods | Free Text |       |
| ------- | --- | --- | --- | --------------------- | ----------------------- | --------- | ----- |
|         |     |     |     | scitsiretcarahC ydutS |                         |           | RQ1   |
|         |     |     |     |                       | Academic/Industry       | Binary    | RQ1   |
| Table 4 |     |     |     |                       | Participants            | Free Text | RQ7   |
|         |     |     |     |                       | Empirically Evaluated   |           |       |
Primary study identification metrics showing accessed databases, search dates, number  Binary RQ1
|     |     |     |     |     | Human Metrics |     |     |
| --- | --- | --- | --- | --- | ------------- | --- | --- |
of resulting studies, conflicted studies, included studies, and the count of studies that  Binary RQ1
| passed quality checks. |     |     |     |     | Evaluation Methods | Free Text | RQ6   |
| ---------------------- | --- | --- | --- | --- | ------------------ | --------- | ----- |
|                        |     |     |     |     | Evaluation Metrics | Free Text | RQ6   |
 Database Search date Results Conflict Included Quality C.    Evaluation Results Free Text
RQ6
|  ACM         | March 2023 153 | 0 13 | 12   |                 |                 |           |       |
| ------------ | -------------- | ---- | ---- | --------------- | --------------- | --------- | ----- |
|              |                |      |      |   )txetnoC( DDD | Software System | Free Text | RQ2   |
|  IEEE Xplore | March 2023 19  | 0 8  | 3    |                 |                 |           |       |
 SpringerLink March 2023     Problems/Motivations Free Text RQ3
|               | 510            | 1 8   | 5   |     | Evaluation of Effectiveness | Free Text |        |
| ------------- | -------------- | ----- | --- | --- | --------------------------- | --------- | ------ |
|  Wiley        | March 2023 25  | 0 2   | 1   |     |                             |           | RQ6    |
|               |                |       |     |     | Challenges and Limitations  | Free Text |        |
|  Sum Database |                |       |     |     |                             |           | RQ5    |
|               | 707            | 1 31  | 21  |     | Lessons Learned             | Free Text | RQ4-5  |
|  Scopus       | April 2023 608 | 10 15 | 9   |     |                             |           |        |
|               |                |       |     |     | Ubiquitous Language         | Binary    | RQ4    |
 Google Scholar June 2023 93 0 8 6     )tnetnoC( DDD Bounded Context
|               |      |       |      |     |                            | Binary | RQ4   |
| ------------- | ---- | ----- | ---- | --- | -------------------------- | ------ | ----- |
|  Sum Snowball | 701  | 10 23 | 15   |     | ACL                        | Binary | RQ4   |
|  Total        |      |       |      |     | Aggregation                | Binary | RQ4   |
|               | 1408 | 11 54 | 36   |     | Domain Events              |        |       |
|               |      |       |      |     |                            | Binary | RQ4   |
|               |      |       |      |     | Domain Services            |        |       |
|               |      |       |      |     |                            | Binary | RQ4   |
|               |      |       |      |     | Entities and Value Objects | Binary | RQ4   |
In cases of disagreement or doubt, the assessors consulted with each
other to reach a consensus. This approach ensured that the quality
assessments were rigorous, minimized potential biases, and allowed  Study Characteristics category included data related to the study de-
discrepancies to be resolved systematically. After quality assessment,  sign, data collection methods, and evaluation metrics employed. Lastly,
we identified the 36 primary studies. The final list of primary studies  the Domain-Driven Design category focused on extracting information
can be found in Table  6. specifically pertaining to the application of DDD in each study.
Among the 36 selected studies, the majority demonstrated strong
Following the completion of the quality assessment stage, the final
adherence to methodological rigor: 78% received a full score (1.0) for
set of studies deemed relevant and has sufficient quality to be moved
clearly stating research aims (QA1), and 75% scored full on explaining
to the data extraction stage. The data extraction process was carried
their methodology (QA2). However, some common weaknesses were  out by the first author using a predefined data extraction form. This
observed. For instance, 39% of studies scored partially (0.5) or zero  form served as a structured tool to systematically collect and record
on reporting negative findings (QA5), indicating a tendency to report  pertinent information from the selected studies.
only positive outcomes. Additionally, 36% had incomplete descriptions
of their data collection or analysis procedures (QA3), which limits
reproducibility. These gaps reflect typical challenges in empirical DDD
| research, where reporting standards may vary, and certain studies lean  |     |     |     | 3.5.2. Synthesis |     |     |     |
| ----------------------------------------------------------------------- | --- | --- | --- | ---------------- | --- | --- | --- |
more toward industrial experience than academic evaluation. Despite  In this study, the data extraction process involved the collection of
this, all selected studies met a minimum quality threshold, ensuring a  both qualitative and quantitative data from the final set of primary
consistent baseline for analysis. studies to derive our results. Specifically, for research questions (RQs)
encompassing 1 to 4, we focused on extracting quantitative data. The
frequencies and percentages of each identified category were then
3.5. Data extraction and synthesis
computed and reported to address these specific research questions.
This approach allowed us to quantify and present the distribution and
3.5.1. Data extraction prevalence of different factors and concepts relevant to the research
In order to ensure consistency and alignment with our research  questions under consideration.
questions and goals, a data extraction form was developed (Table  5).
Conversely, for RQs pertaining to RQs 5 to 7, we concentrated
The initial list of data points was prepared by the first author, and
on extracting qualitative data from the primary studies. To synthesize
this list was then discussed among the authors to refine and finalize a  and interpret these qualitative findings, we applied a narrative synthe-
starting set of categories. A pilot data extraction was done on a subset of  sis method based on the guidance provided by Popay et al. (2006).
randomly selected primary studies. During the data extraction process,  This involved systematically extracting key information and important
we adopted an iterative and incremental approach, continuously refin- findings from each individual study. Subsequently, we conducted a
ing the categories as new insights emerged. This iterative refinement  comprehensive analysis and interpretation of the extracted qualitative
allowed us to adapt the data extraction form to better capture the  data to draw overarching and meaningful conclusions in response to
nuances and specific details relevant to our RQs and goals. the respective research questions. The narrative synthesis approach al-
The data points were categorized into 3 main categories. Firstly,  lowed us to integrate diverse qualitative evidence, explore patterns and
the Publication Metadata category involved extracting basic information  themes across the studies, and provide a cohesive and comprehensive
such as the title, authors, and publisher of each study. Secondly, the understanding of the research questions in question.
6

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
Table 6
List of primary studies and their quality assessment scores.
Title Author(s) Year Score
Singjai et al. (2021b) Patterns on Deriving APIs and their Endpoints from Domain Models Singjai et al. 2021 4
Maddodi et al. (2020) Aggregate Architecture Simulation in Event-Sourcing Applications Maddodi et al. 2020 7.5
using Layered Queuing Networks
Peng and Hu (2007) IAnticorruption: a domain-driven design approach to more robust Peng et al. 2007 4.5
integration
Josélyne et al. (2018) Partitioning microservices: a domain engineering approach Josélyne et al. 2018 5
Perillo et al. (2009) Daileon: a tool for enabling domain annotations Perillo et al. 2009 4.5
Le et al. (2019) jDomainApp: A Module-Based Domain-Driven Software Framework Le et al. 2019 6.5
Le et al. (2022) Generating Multi-platform Single Page Applications: A Hierarchical Le et al. 2022 5
Domain-Driven Design Approach
Uludağ et al. (2018) Supporting Large-Scale Agile Development with Domain-Driven Uludağ et al. 2018 7
Design
Wang et al. (2022) A Reference Architecture for Blockchain-based Traceability Systems Wang et al. 2022 6.5
Using Domain-Driven Design and Microservices
Landre et al. (2006) Architectural improvement by use of strategic level domain-driven Landre et al. 2006 6.5
design
Kapferer and Zimmermann (2020) Domain-Driven Service Design: Context Modeling, Model Kapferer et al. 2020 5.5
Refactoring and Contract Generation
Camilli et al. (2023) Actor-driven Decomposition of Microservices through Multi-level Camilli et al. 2023 7
Scalability Assessment
Braun et al. (2021b) Tackling Consistency-related Design Challenges of Distributed Braun et al. 2021 7
Data-Intensive Systems: An Action Research Study
Landre et al. (2007) Agile enterprise software development using domain-driven design Landre et al. 2007 6.5
and test first
Braun et al. (2021a) Advanced Domain-Driven Design for Consistency in Distributed Braun et al. 2021 6.5
Data-Intensive Systems
Zhao and Zhao (2021) Applying Microservice Refactoring to Object-Oriented Legacy System Zhao et al. 2021 4
Krause et al. (2020) Microservice Decomposition via Static and Dynamic Analysis of the Krause et al. 2020 5.5
Monolith
Snoeck and Wautelet (2022) Agile MERODE: a model-driven software engineering method for Snoeck et al. 2022 6
user-centric and value-based development
Danenas and Garsva (2012) Domain Driven Development and Feature Driven Development for Danenas et al 2012 4
Development of Decision Support Systems
Kapferer and Zimmermann (2021) Domain-Driven Architecture Modeling and Rapid Prototyping with Kapferer et al. 2021 6.5
Context Mapper
Hammarström and Herzog (2016) Experience from integrating Domain Driven Software System Design Hammarström et al. 2016 5.5
into a Systems Engineering Organization
Da Silva et al. (2022) BPM2DDD: A Systematic Process for Identifying Domains from Da Silva et al. 2022 6.5
Business Processes Models
Hippchen et al. (2017) Designing Microservice-Based Applications by Using a Hippchen et al. 2017 6
Domain-Driven Design Approach
Ding et al. (2020) Enterprise service application architecture based on Domain Driven Ding et al. 2020 5
Model Design
Özkan et al. (2023) Refactoring with domain-driven design in an industrial context: An Özkan et al. 2023 8
action research report
Pereira and Silva (2022) Towards Transactional Causal Consistent Microservices Business Pereira et al. 2022 6.5
Logic
Joselyne et al. (2021) A Systematic Framework of Application Modernization to Joselyne et al. 2021 4.5
Microservice based Architecture
Wanderley and Da Silveria (2012) A Framework to Diminish the Gap between the Business Specialist Wanderley et al. 2012 5
and the Software Designer
Koryl (2017) Active resources concept of computation for enterprise software Koryl et al. 2017 4
Mayer and Weinreich (2018) An Approach to Extract the Architecture of Microservice-Based Mayer et al. 2018 5
Software Systems
Vural and Koyuncu (2021) Does Domain-Driven Design Lead to Finding the Optimal Vural et al. 2021 8
Modularity of a Microservice?
Oukes et al. (2021) Domain-Driven Design applied to land administration system Oukes et al. 2021 4.5
development: Lessons from the Netherlands
Häser et al. (2016) Is business domain language support beneficial for creating test case Häser et al 2016 6.5
specifications: A controlled experiment
Le et al. (2018) On domain driven design using annotation-based domain specific Le et al. 2018 6
language
Abeck et al. (2019) A Context Map as the Basis for a Microservice Architecture for the Abeck et al. 2019 4
Connected Car Domain
Bünder and Kuchen (2019) A model-driven approach for behavior-driven GUI testing Bünder et al. 2019 5.5
4. Results sheds light on the key insights and trends related to the implementa-
tion, effectiveness, and assessment of DDD in diverse software systems.
This section presents a comprehensive analysis of the findings ob- By organizing the results around the research questions, this section
tained from our SLR conducted on DDD and aims to address the offers valuable insights into the involvement of key stakeholders, the
research questions by providing a detailed exploration of the current evaluation and measurement of DDD’s effectiveness, and the overar-
state of research pertaining to DDD in the literature. Through a metic- ching research landscape concerning this domain-centric architectural
ulous examination of various articles, studies, and sources, the section approach.
7

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
Fig. 2. Breakdown of study types (left) and study designs (right).
Fig. 3. Breakdown of the primary studies based on their field of focus (left) and field of focus by publication year (right).
4.1. (RQ1) What is the state of the art concerning DDD in the existing industrial case studies involving microservices and distributed systems,
literature, in terms of study types, research venues, software systems, and while studies focused on tools or frameworks tended to lack rigorous
the distribution between academic and industrial settings? empirical assessment. Furthermore, studies based on action research or
industry collaborations generally provided more detailed insight into
DDD’s impact on software quality, maintainability, and organizational
Based on our primary studies (36), the current state of research
communication.
concerning DDD in the existing literature showcases studies conducted
between 2006 and 2023. Among these studies, 23 (64%) are Conference Regarding the software systems studied, Microservices received the
Papers, 12 (33%) are Journal Articles, and 1 (3%) study is from the highest attention with 16 (44%) studies, followed by Enterprise Software
Preprint database, which also can be seen in Fig. 2. Systems with 6 (17%) studies, and DDD-related Tools and System Agnos-
In terms of venues, a diverse range of conferences and journals
tic studies with 4 (11%) studies each. Additionally, Standard Computer
have emerged as platforms for the dissemination of DDD research.
Applications and Web Applications were subjects of 2 (6%) studies each,
These venues span the spectrum of software engineering and tech-
while Service-Oriented Applications and Distributed Systems each had 1
nology domains. Among them, the Conference on Object-Oriented Pro-
(3%) study (see Fig. 3).
gramming Systems, Languages, and Applications takes a prominent role Out of the 16 Microservices studies, 10 (63%) were conducted in an
with 3 publications, showcasing its relevance in fostering discussions academic environment, while the remaining 6 (38%) were performed in
around object-oriented paradigms in software development. Addition- industrial settings. In contrast, Enterprise Software Systems were predom-
ally, the Symposium on Information and Communication Technology have inantly studied in industry settings. Interestingly, DDD-related Tools
contributed 2 publications. were exclusively implemented in academic settings.
The most common study type is Case Study, accounting for 10 (28%) The interest in DDD initially emerged in industry settings, as ev-
studies, followed by Theoretical Study with 9 (25%) studies. There idenced by the first 3 studies conducted between 2006 and 2007.
are also 4 (11%) Action Research studies, 3 (8%) Experience Reports, Subsequently, the focus shifted to academic settings, with all 3 studies
2 (6%) Empirical Studies, 2 (6%) that are not explicitly mentioning a from 2009 to 2012 being conducted in academia. The trend then
type but using empirical methodologies, Controlled Experiments, 2 (6%) became more balanced, with an equal distribution of studies between
Comparative Analyses, 1 (3%) Observational Study, 1 (3%) Methodological academic and industrial settings in 2016.
Study, and 1 (3%) Experimental Study. The remaining studies were The distribution of studies across academic and industry settings
primarily conceptual, methodological, or design proposals with limited reveals an interesting pattern. Out of the total 36 studies, 21 (58.3%)
or no empirical validation. were conducted in academia, indicating a dominant presence of aca-
In terms of measurement rigor, 17 studies did not report any demic research in this field. Conversely, 13 (36.1%) studies were
concrete evaluation metrics. Those studies are theoretical or design- conducted in industry settings, and 2 (5.6%) studies had a hybrid
oriented. Many propose methods, tools, or architectural patterns with- setting involving both academic and industry collaboration. This dis-
out validating them through empirical means. While some are labeled parity in the academic-industry ratio suggests that DDD has garnered
as case studies or experience reports, their evidence is often anecdotal significant attention from the academic community, where researchers
and lacks systematic measurement. This pattern suggests a gap in are actively exploring its concepts and applications. However, it also
empirically grounded research in certain areas of DDD, particularly tool highlights the relevance and practical implications of DDD in industry
development and architectural modeling. settings, as evidenced by the notable number of industry-based studies.
When cross-referencing these findings with the application domains, The existing literature demonstrates a diverse and evolving land-
we observed that empirical evaluations were more likely to be found in scape of research on DDD, with a particular emphasis on Microservices
8

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
Fig. 4. Breakdown of the primary studies based on applied software systems (left) and studies grouped by the study type and software systems (right).
and an increasing number of academic contributions. This suggests a 4.2.4. Tools and standard computer applications
growing recognition of the relevance and applicability of DDD in both Several studies have applied DDD in the context of tools (Perillo
academic and industrial contexts. et al., 2009; Kapferer and Zimmermann, 2020; Häser et al., 2016)
and standard computer applications (Le et al., 2019; Hammarström
4.2. (RQ2) What categories of software systems have demonstrated benefits and Herzog, 2016). DDD has been leveraged to improve code quality,
from the implementation of DDD? enhance the software construction process, and provide more compre-
hensive solutions for domain modeling and software generation. In the
With this RQ, we present the categories of software systems that case of tools, DDD has been employed to bridge the gap between busi-
have demonstrated benefits from the implementation of DDD, based ness domain concerns and infrastructure, ensuring the maintainability
on the findings. The studies were analyzed, and their contributions and readability of code.
to various software system categories were identified during the data
extraction phase. The breakdown of the following data can also be
4.2.5. Distributed systems
visually seen in Fig. 4 and Table 7.
In this study, we classified systems based on the architectural types
explicitly mentioned in the primary studies. However, some system
4.2.1. Microservices
types, such as Service-Oriented Architecture (SOA) (Section 4.2.6) and
Several studies have highlighted the advantages of applying DDD
Distributed Systems, may overlap in practice. For example, SOA is one
principles in the context of microservices architecture (Singjai et al.,
possible way of realizing a distributed system.
2021b; Josélyne et al., 2018; Wang et al., 2022; Camilli et al., 2023;
In cases where the primary study did not specify the exact ar-
Braun et al., 2021a; Zhao and Zhao, 2021; Krause et al., 2020; Hip-
chitectural type such as microservices or SOA, but specifies it is a
pchen et al., 2017; Ding et al., 2020; Özkan et al., 2023; Pereira
distributed system, we used the more generic term Distributed Systems
and Silva, 2022; Joselyne et al., 2021; Mayer and Weinreich, 2018;
to accurately reflect the nature of the system without over-specification.
Vural and Koyuncu, 2021; Oukes et al., 2021; Abeck et al., 2019).
This classification ensures that we do not make assumptions about
According to our learnings from those studies, by adopting DDD, orga-
the specific system architecture when such information is not available,
nizations have been able to improve the modularity, maintainability,
and it provides a comprehensive view of how DDD is applied in various
and scalability of microservices-based applications, enabling effective
types of distributed systems. We acknowledge that system types like
handling of complex and distributed systems. The use of DDD patterns
SOA and Distributed Systems are not always mutually exclusive, and we
and concepts in the design and development of microservices has been
carefully categorized the systems according to the information available
particularly beneficial in achieving clear boundaries between services,
in the primary studies.
enabling better communication between development teams, and en-
This approach was applied to Braun et al.’s study (Braun et al.,
suring a strong alignment with business domains. For instance, Krause
2021b), where it reported that DDD has demonstrated benefits in the
et al. (2020) applied DDD principles to modernize a real-world lot-
development of distributed systems. By controlling concurrent data
tery system into a microservices-based architecture, demonstrating the
access and achieving semantic compatibility in domain models, DDD
approach’s relevance in refactoring legacy systems in the public sector.
has been instrumental in tackling consistency-related design challenges
in distributed data-intensive systems. Similarly, Wang et al. (2022)
4.2.2. Enterprise software systems
utilized DDD to architect a blockchain-based traceability system in the
Several studies have reported the benefits of applying DDD in the
global supply chain domain, where managing bounded contexts across
context of enterprise software systems (Maddodi et al., 2020; Peng
distributed actors was critical.
and Hu, 2007; Uludağ et al., 2018; Landre et al., 2007; Danenas and
Garsva, 2012; Koryl, 2017). The adoption of DDD principles has proven
valuable in handling the increasing complexity of enterprise systems 4.2.6. Service-Oriented Applications (SOA)
and addressing challenges related to legacy system modernization. By Landre et al. (2006) use DDD patterns to improve the software
emphasizing bounded contexts and domain models, DDD enables more architecture of a large enterprise system, which is designed as a SOA.
maintainable and flexible enterprise software architectures, allowing The authors mention that establishing a DDD context map helped
organizations to better adapt to changing business requirements. in scoping the project and identifying architectural problems such as
complex dependencies and gateway roles.
4.2.3. Web applications In this study, we distinguish between SOA and Microservices as
Some studies have shown that DDD can be beneficial in the develop- separate architectural classifications, not to make a strict ontological
ment of web applications (Le et al., 2022; Bünder and Kuchen, 2019). separation, but to reflect the terminology used in the primary stud-
By applying DDD principles, web application developers have been able ies themselves. While both paradigms promote modular and service-
to improve the design and implementation of Single Page Applications based decomposition, they also differ in typical implementations: mi-
(SPAs), achieving better cross-framework compatibility and enhancing croservices emphasize lightweight, independently deployable compo-
productivity in SPA development. nents with decentralized governance, whereas SOA is often realized
9

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
with centralized orchestration and heavier protocols (e.g., ESB and These patterns align well with DDD’s tactical building blocks — such
SOAP) (Dragoni et al., 2017; Fritzsch et al., 2019). as aggregates and domain events — and have been leveraged in stud-
We acknowledge that this boundary is not universally agreed upon, ies to evaluate performance characteristics under different workload
and many researchers recognize significant overlap between SOA and patterns (Maddodi et al., 2020).
microservices. As noted by Lewis and Fowler (2014), the distinction In pursuit of achieving optimized performance and resource met-
lies more in implementation philosophy than fundamental principles. rics in component-based software, DDD has been used in research to
Our categorization aims to reflect how the systems were described investigate the effect of workload patterns. Specifically, the research
and studied in the reviewed literature, without implying that SOA and aimed to gain insight into how patterns like CQRS and ES are created,
microservices are categorically distinct. Future work could explore how thus providing valuable guidelines for architects to select appropriate
these architectural paradigms co-evolve in practice. architectures based on workload characteristics (Peng and Hu, 2007).
4.2.7. System agnostic
Certain studies have shown that DDD can provide valuable contri- 4.3.3. Reducing complexity in currency exchange systems
butions for the implementation of software which is suitable across A prevalent software development problem addressed by DDD per-
various system categories (Snoeck and Wautelet, 2022; Kapferer and tains to reducing complexity and high coupling in currency exchange
Zimmermann, 2021; Da Silva et al., 2022; Wanderley and Da Silve- systems. The case in question involves the integration layer between
ria, 2012). In these studies, DDD principles and patterns have been a new currency exchange system (SPOT) and a legacy back office
applied to implement practitioner frameworks and methods to address system (TBS), wherein the integration layer (TBSExport) had become
communication gaps between business specialists and software design- an unwieldy burden with unpredictable side effects following minor
ers, improve software system modularity, and support the creation of changes. To tackle this complexity and streamline the integration pro-
context maps. cess, researchers sought to devise effective solutions using DDD princi-
ples (Peng and Hu, 2007).
4.2.8. DDD tools
DDD has been applied to improve code quality, readability, and
maintainability through the development of supportive tooling. These 4.3.4. Microservice size, partitioning and defining API endpoints
tools fall into two main categories. Annotation-based DDD frameworks, Microservice architecture introduces the challenge of determining
such as Daileon by Perillo et al. (2009), aim to separate business the appropriate size of individual microservices, thereby necessitating
domain concerns from infrastructure code. In contrast, DDD modeling a conceptual methodology for partitioning microservices based on do-
tools, such as Context Mapper by Kapferer and Zimmermann (2020), main engineering techniques. Improperly sized microservices can lead
provide higher-level support for visualizing and evolving Context Maps to complexity management issues, where too large services become
and other domain artifacts. monolithic and too small services create an overly complex system. This
can also result in performance bottlenecks and scalability challenges,
4.3. (RQ3) Which specific software development concerns have been ad- as well as data consistency problems due to poorly coordinated related
dressed through the application of DDD in previous studies? data spread across services. Additionally, undefined or poorly defined
boundaries complicate maintenance and evolution, and misaligned mi-
The SLR conducted in this study sought to identify the specific croservice boundaries with team boundaries hinder team autonomy and
software development concerns that have been addressed through the require excessive coordination. DDD has been instrumental in address-
application of DDD in previous research. The results revealed several ing this challenge, aiming to achieve optimal microservice design and
challenges and motivations encountered in various software develop- composition within the context of a microservices architecture (Singjai
ment projects, encompassing diverse domains such as microservices et al., 2021b; Josélyne et al., 2018).
architecture, legacy system modernization, distributed systems, and
complex decision support systems. The subsequent information present
a comprehensive overview of the identified challenges and motivations 4.3.5. Improving code quality with domain annotations
for adopting DDD. In the pursuit of enhancing code quality, readability, and maintain-
ability while ensuring a clear separation between the business domain
4.3.1. Addressing API design problems in distributed systems and infrastructure concerns, DDD has been leveraged to address chal-
One of the prominent challenges addressed by DDD in software lenges associated with using annotations in DDD. The proposed concept
development projects is related to API design in distributed systems, of ‘‘domain annotations’’ by Perillo et al. (2009) serves to mitigate these
particularly in microservice-based systems. This challenge revolves challenges and fosters a robust software design approach.
around missing guidance on how to derive APIs and API endpoints
from domain model elements. The primary concern is that coupling
smells lead to poor API design in distributed systems. These issues 4.3.6. Enhancing software construction and development environment
result in shallow APIs that are difficult to understand, maintain, and The lack of generative, module-based software construction and
evolve. Singjai et al. (2021b) propose clear guidance on how to de- seamless development environment integration poses significant chal-
rive APIs and API endpoints from domain model elements using DDD lenges in software development. Without these capabilities, developers
patterns. face difficulties in automating the generation of software from domain
models, leading to increased manual effort and potential for errors (Le
4.3.2. Investigating performance in component-based software et al., 2019). This can result in inconsistencies between the domain
Command Query Responsibility Segregation (CQRS) and Event model and the implemented software, hindering maintainability and
Sourcing (ES) are two architectural patterns often used in conjunction scalability. Additionally, the absence of integrated development tools
with DDD to improve scalability and traceability. CQRS separates means that developers must switch between different environments
write operations (commands) from read operations (queries), enabling and tools, disrupting their workflow and reducing productivity. By
systems to optimize each independently. Event Sourcing, on the other addressing these issues, in the work of Le et al. (2019) the adoption
hand, persists all changes to the application state as a sequence of of the jDomainApp framework and an Eclipse IDE plugin has been
immutable events rather than storing the current state directly. In this proposed as a solution to these challenges, thereby optimizing software
approach, the current state is reconstructed by replaying these events. construction and development processes.
10

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
4.3.7. Multi-platform SPA development Table 7
The challenges faced by Single Page Application (SPA) developers Reported benefits of DDD across different software system categories, as identified in
the primary studies.
encompass two crucial aspects: designing SPAs that can effectively
work across different SPA frameworks (e.g., Angular, React, React
Software system Reported benefits of DDD
category
Native, and Vue.js) and translating this design into an intermediate
Microservices Improved modularity, maintainability, and
high-level language that can seamlessly transform into a target frame-
scalability; better service boundary definition;
work of choice. DDD offers a multi-platform, hierarchical approach enhanced team autonomy; reduced coupling
to tackle these challenges, significantly enhancing SPA development through bounded contexts and context mapping
productivity (Le et al., 2022). (Singjai et al., 2021b; Josélyne et al., 2018;
Wang et al., 2022; Camilli et al., 2023).
4.3.8. Scaling agility in large organizations
E
So
n
f
t
t
e
w
rp
a
r
r
i
e
s e
S ystems
S
cl
u
e
p
a
p
re
o
r
r t
a
f
r
o
c
r
h i
l
t
e
e
g
c
a
tu
cy
re
s
v
y
i
s
a
te
b
m
o u
m
n
o
d
d
e
e
d
r n
c
i
o
z
n
a
t
t
e
io
x
n
ts
;
;
Large organizations encounter a myriad of challenges when striving improved adaptability to evolving business
to scale agility, including effective coordination and communication requirements (Maddodi et al., 2020; Uludağ
between agile teams, inter-team dependencies, and the need for clearly et al., 2018; Landre et al., 2007).
defined requirements. By adopting DDD, enterprises have sought to Web Better SPA design across frameworks;
address these challenges and provide architectural guidance to support Applications productivity boost through DDD-driven
large-scale agile development. However, it is important to acknowledge
c
a
o
n
m
d
p
K
o
u
n
c
e
h
n
e
t
n
g
,
e
2
n
0
e
1
r
9
a
)
ti
.
on (Le et al., 2022; Bünder
that successful DDD implementation in large organizations necessitates
Tools Improved code quality and modularity through
experienced enterprise architects to provide effective guidance (Uludağ
domain annotations; enhanced maintainability
et al., 2018). by separating domain logic from infrastructure
concerns (Perillo et al., 2009; Kapferer and
4.3.9. Complexities in Blockchain-Based Traceability Systems (BTS) Zimmermann, 2020).
BTSs are software systems designed to ensure transparent, tamper- Distributed Addressed consistency challenges; improved
proof tracking of products or data throughout a supply chain or process.
Systems s
m
e
o
m
d
a
u
n
l
t
e
i
s
c
(
c
B
o
r
m
au
p
n
a t
e
ib
t
il
a
i
l
t
.
y
, 2
a
0
n
2
d
1
i
b
s
)
o
.
lation between
These systems leverage blockchain technology to record transactions
SOA/Service- Clear project scoping; identification of
and state changes in an immutable ledger, enhancing trust, provenance,
Oriented architectural problems (e.g., dependency
and accountability. Applications complexity) using context maps (Landre et al.,
In the context of DDD, BTSs benefit from patterns such as Bounded 2006).
Contexts and Aggregates to model complex interactions and respon- System-Agnostic Support for agile methods; communication
sibilities across different stakeholders and subsystems. As reported Approaches alignment between business and technical
in Wang et al. (2022), the application of DDD in BTS improves the stakeholders; improved modeling modularity
maintainability and extensibility of these systems by clearly delineat-
(Snoeck and Wautelet, 2022; Da Silva et al.,
2022).
ing domain boundaries and aligning technical implementations with
business processes.
The design and development of BTSs pose unique challenges and
complexities, including domain model intricacies, modeling bound- 4.4. (RQ4) What are the most common DDD patterns utilized in previous
aries, and managing the relationship between different bounded con- research, such as ACLs, Bounded Contexts, and other related approaches?
texts. Researchers have employed DDD and microservice architecture
to address these challenges, thereby improving the cohesiveness, main- In this SLR on DDD, we investigated the most commonly utilized
tainability, and extensibility of BTSs in handling complex data in the DDD patterns across various software systems. The analysis was based
global supply chain in Wang et al. (2022). on a dataset comprising studies identified through our study selection
process explained in Section 3.4. Each study was examined for the
4.3.10. Challenges in model decomposition presence or absence of specific DDD patterns, marked by ‘‘Y’’ for used
Decomposing software systems into cohesive and loosely coupled and ‘‘N’’ for not used patterns, during our data extraction process. Our
modules poses significant challenges for software engineers and ser- results are also visually shown in Fig. 5.
vice designers. DDD patterns have been instrumental in addressing The results reveal that certain DDD patterns are prevalent in the
this challenge, offering a clear and concise interpretation of these majority of the analyzed studies, indicating their significance and
patterns, despite debates and differing interpretations among practi- widespread adoption in the DDD context. The following DDD patterns
tioners (Kapferer and Zimmermann, 2021). were found to be most commonly utilized:
4.3.11. Legacy system modernization and refactoring 1. Ubiquitous Language. Ubiquitous language is a fundamental DDD
Legacy systems often suffer from outdated technologies, poor docu- pattern, and our findings indicate that it is frequently employed
mentation, and a lack of alignment between the system’s current state in various software systems, including Microservices, Enterprise
and the evolving business requirements. This misalignment creates a Software Systems and Web Applications (Maddodi et al., 2020;
communication gap between business specialists, who understand the Peng and Hu, 2007; Josélyne et al., 2018; Le et al., 2022; Uludağ
domain requirements, and software designers, who are tasked with et al., 2018; Krause et al., 2020; Danenas and Garsva, 2012;
implementing these requirements (Özkan et al., 2023). As a result, Kapferer and Zimmermann, 2021; Özkan et al., 2023; Pereira and
changes and enhancements become risky, time-consuming, and error- Silva, 2022; Joselyne et al., 2021; Oukes et al., 2021).
prone. DDD addresses these issues by providing a structured approach 2. Bounded Context. Bounded contexts were found to be widely
to align the domain model with business needs, facilitating better com- utilized in Microservices, Enterprise Software Systems and Web
munication and understanding. This alignment enables more effective Applications (Maddodi et al., 2020; Peng and Hu, 2007; Josélyne
refactoring and modernization efforts, ensuring that the updated system et al., 2018; Le et al., 2022; Uludağ et al., 2018; Camilli et al.,
meets current business requirements while maintaining or improving 2023; Braun et al., 2021b,a; Zhao and Zhao, 2021; Snoeck and
system integrity and performance (Özkan et al., 2023; Wanderley and Wautelet, 2022; Kapferer and Zimmermann, 2021; Özkan et al.,
Da Silveria, 2012). 2023; Pereira and Silva, 2022).
11

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
Fig. 5. Breakdown of the applied DDD patterns in the primary studies. Applied DDD patterns marked with ‘‘Y’’ and not applied pattern marked with ‘‘N’’.
3. Entities and Value Objects. Entities and value objects, representing discussion, we also summarize the main DDD implementation chal-
domain concepts, were extensively adopted in Microservices, lenges and mitigation strategies identified across the primary studies.
Enterprise Software Systems and Web Applications (Maddodi Table 8 and Table 9 presents a concise mapping that highlights both
et al., 2020; Peng and Hu, 2007; Josélyne et al., 2018; Le et al., the barriers encountered and the approaches taken to address them in
2022; Uludağ et al., 2018; Wang et al., 2022; Braun et al., practice.
2021b; Snoeck and Wautelet, 2022; Danenas and Garsva, 2012;
Kapferer and Zimmermann, 2021; Hammarström and Herzog,
4.5.1. Addressing design complexities
2016; Da Silva et al., 2022; Hippchen et al., 2017; Özkan et al.,
Several studies highlight the complexity associated with implement-
2023; Pereira and Silva, 2022; Joselyne et al., 2021; Wanderley
ing DDD patterns, particularly in the context of microservices and
and Da Silveria, 2012).
distributed systems. The integration layer between different Bounded
Contexts can become burdensome, leading to high coupling and unpre-
In contrast, the ACL was identified as the least used DDD pattern
dictability in the system. This challenge, for instance, is exemplified in
across different software systems. Several studies did not utilize the ACL
the case of the currency exchange system (SPOT) and the legacy back-
in their respective projects (Peng and Hu, 2007; Le et al., 2019; Landre
office system (TBS) in Peng and Hu (2007). Finding the right balance
et al., 2006; Kapferer and Zimmermann, 2020; Koryl, 2017; Häser et al.,
between high cohesion within services and loose coupling between
2016; Bünder and Kuchen, 2019).
them is crucial for scalability and maintainability (Peng and Hu, 2007;
The ACL serves as a means to protect the integrity of the main
Josélyne et al., 2018).
domain from external and legacy systems, and its limited adoption
suggests that certain software projects may have addressed integration
challenges through alternative approaches or may not have encoun- 4.5.2. Identifying optimal microservices boundaries
tered a specific need for this pattern. Decomposing monolithic systems into microservices presents its
While Ubiquitous Language, Bounded Context, and Entities/Value own set of challenges. Determining the appropriate size and boundaries
Objects were widely observed across studies, patterns such as Core of microservices is not straightforward and requires careful consid-
Domain and Shared Kernel were rarely reported. Only a limited number eration of the domain and workload characteristics (Josélyne et al.,
of studies (e.g., Landre et al. (2006), Özkan et al. (2023)) referred 2018). The granularity of microservices can be subjective, leading
to the Core Domain explicitly, often in the context of prioritizing to potential disagreements among development teams (Kapferer and
critical business logic. Shared Kernel was not discussed as a stan- Zimmermann, 2021). Ensuring that microservices align with business
dalone concept in any study, although collaboration between teams needs and subdomains can be challenging (Hippchen et al., 2017).
was sometimes implied in studies using Bounded Contexts. Similarly, Additionally, finding suitable examples that demonstrate DDD-driven
upstream–downstream relationships — central to context mapping in microservices architecture is often noted as a limitation (Vural and
Strategic Design — were briefly mentioned in a few cases but not Koyuncu, 2021).
analyzed in depth.
4.5.3. Managing domain model complexity
4.5. (RQ5) What are the challenges encountered during the implementation When adopting DDD, managing the complexity of the domain model
of DDD in software development projects? becomes a crucial challenge. Modeling boundaries between different
Bounded Contexts and ensuring the relationships between them are
The challenges encountered during the implementation of DDD in properly managed require deep knowledge about the organization’s
software development projects are diverse and demand careful consid- domain Da Silva et al. (2022). The complexity of the domain model
eration to ensure successful adoption. In this RQ, we present the key and the interactions between bounded contexts can hinder the process
challenges identified through primary studies. To support the narrative of abstraction and generalization of elements (Da Silva et al., 2022).
12

O. Özkan et al.
The Journal of Systems & Software 230 (2025) 112537
| Table 8 |     |     | Table 9 |     |     |     |     |
| ------- | --- | --- | ------- | --- | --- | --- | --- |
Challenges in implementing DDD and corresponding mitigation strategies and tech- SWOT analysis of DDD in software research.
| niques reported in the literature. |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Strengths
|  Challenge | Mitigation strategy and concrete  |     |     |                                                              |     |     |     |
| ---------- | --------------------------------- | --- | --- | ------------------------------------------------------------ | --- | --- | --- |
|            |                                   |     |  S1 | Aligns software systems with business domains conceptually.  |     |     |     |
techniques (from literature)
|     |     |     |  S2 | Widespread use of tactical/strategic patterns (e.g., Ubiquitous  |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- |
 Design complexity in  Use of context mapping and bounded      Language, Bounded Context, Entities, Aggregates).
distributed systems contexts to reduce coupling; ACLs to   S3 Demonstrated benefits in modularity and maintainability,
encapsulate legacy interactions (Peng    especially in microservices.
and Hu, 2007; Josélyne et al., 2018)
|     |     |     |     | Weaknesses |     |     |     |
| --- | --- | --- | --- | ---------- | --- | --- | --- |
 Defining microservices  Domain decomposition using     W1 Limited empirical evaluation in several studies.
business-aligned subdomains and context
boundaries  W2 Underreporting of strategic patterns (e.g., Shared Kernel,
maps; Use of design workshops to
|     |     |     |     | Core Domain, upstream/downstream relations). |     |     |     |
| --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- |
iteratively refine service granularity
|     |     |     |  W3 | High learning curve for newcomers to DDD. |     |     |     |
| --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- |
(Josélyne et al., 2018; Hippchen et al.,
|                    | 2017; Vural and Koyuncu, 2021)      |     |     | Opportunities                                         |     |     |     |
| ------------------ | ----------------------------------- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
|                    |                                     |     |  O1 | Growing interest in academia and industry since 2017. |     |     |     |
|  Managing complex  | Collaborative modeling with domain  |     |     |                                                       |     |     |     |
domain models experts; event storming sessions;   O2 Potential for stronger empirical and comparative research.
maintaining cohesion through tactical   O3 Increasing tool support (e.g., DSLs, context-mapping tools).
|     | DDD patterns (Da Silva et al., 2022;  |     |     |     |     |     |     |
| --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
Threats
K a p f e r e r   a n d Zimmermann, 2020; Wang
      T 1 R is k   o f  s u p e r f ic i a l   o r  in c o n s is t e n t  D D D   a d o p t io n .
|     | et a l ., 2 0 2 2 | )   |     | l                |                              |                                          |     |
| --- | ----------------- | --- | --- | ---------------- | ---------------------------- | ---------------------------------------- | --- |
|     |                   |     | T 2 | Co n c e p t u a | d i s a g r e e m e n ts a n | d a m b i gu i ty i n im p l ementation. |     |
 Integration with legacy  Use of ACLs to decouple legacy     T3 Dependence on domain experts may limit broader adoption.
dependencies and allow incremental
systems
migration (Peng and Hu, 2007)
|  Communication gaps  | Establishing Ubiquitous Language and  |     |     |     |     |     |     |
| -------------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
between domain  domain co-design practices; continuous  4.5.6. Model-code gap in domain-specific language (DSL)
experts and developers involvement of stakeholders (Wanderley  A domain-specific language (DSL) is a computer language special-
and Da Silveria, 2012; Kapferer and  ized to a particular application domain Evans (2004). Studies that
Zimmermann, 2020)
focus on DSL-based DDD implementations point out potential weak-
|  M o d e l -c o d e   | U s e   o f  t o o l | s  l i ke   C o n t e x t  M a p p e r  for  |     |     |     |     |     |
| --------------------- | -------------------- | -------------------------------------------- | --- | --- | --- | --- | --- |
t in      d    nesses, including the existence of a ‘‘model-code’’ gap (Kapferer and
| mi s a li g n m e n | sy n c h r o n i z | e d m o d e li n g a n c o d e |     |     |     |     |     |
| ------------------- | ------------------ | ------------------------------ | --- | --- | --- | --- | --- |
DSL-based tooling generation; contract-based validation  Zimmermann, 2020). The lack of a deeper knowledge about the domain
(Kapferer and Zimmermann, 2020) may hinder the process of abstraction and generalization, leading to
 Onboarding and lack of  Internal DDD training sessions;    artifacts that may not align with the organization’s domain Da Silva
| DDD expertise | mentoring by experienced architects;  |     | et al. (2022). |     |     |     |     |
| ------------- | ------------------------------------- | --- | -------------- | --- | --- | --- | --- |
gradual learning curve through pilot
projects (Özkan et al., 2023; Hippchen
et al., 2017) 4.5.7. Impact of developer’s experience and challenges in onboarding
 Pattern interpretation  Team workshops to align on DDD    The level of experience and familiarity with DDD concepts among
pattern usage; creation of design  the development team can influence the effectiveness of DDD imple-
disagreements
documentation to guide consistent  mentation (Hippchen et al., 2017). Developers with prior experience
practices (Kapferer and Zimmermann,  in DDD are more likely to understand and apply DDD patterns ef-
2021; Özkan et al., 2023)
fectively, resulting in better-designed and more maintainable software
 Limited availability of  Early involvement of domain specialists;   systems (Hippchen et al., 2017). On the other hand, inexperienced
| domain experts |   f  |       |     |     |     |     |     |
| -------------- | ---- | ----- | --- | --- | --- | --- | --- |
u se o d o m a in w a lk t h r o u g h s a n d developers may struggle with grasping the complexities of DDD and
|     | s   | s   t   t  |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | --- |
bu s in e s p ro c e s m o d e l s o e x t ra c may not fully utilize the benefits of the approach (Hippchen et al.,
knowledge (Vural and Koyuncu, 2021;
Da Silva et al., 2022) 2017). Also, introducing DDD to a development team that has lit-
tle or no prior exposure to DDD can be a challenge (Özkan et al.,
2023). Onboarding developers and providing the necessary training
and resources to understand DDD concepts and principles can require
This challenge is especially pronounced when dealing with large-scale
additional time and effort (Özkan et al., 2023). This challenge can be
and complex data-intensive systems (Wang et al., 2022).
particularly pronounced in organizations that are transitioning from
traditional software development approaches to DDD.
4.5.4. Integrating DDD with existing frameworks
4.5.8. Navigating controversial debates
Integrating DDD into existing software frameworks can present
Controversial debates and differing interpretations exist among
compatibility issues, as DDD introduces encapsulation and abstraction
practitioners regarding the application and combination of DDD pat-
levels that may not align seamlessly with existing structures (Özkan
terns (Kapferer and Zimmermann, 2021; Özkan et al., 2023). Develop-
et al., 2023). Refactoring in an actively developed codebase can also  ers may face challenges in deciding which patterns to adopt and how to
prove challenging, especially when engineers lack prior experience  effectively integrate them into the development process. This can result
with DDD (Özkan et al., 2023). in disagreements within the team and may require additional effort to
reach a consensus.
4.5.5. Communication gap between business specialists and software design- 4.5.9. Need for experienced domain experts
ers Incorporating DDD requires a deep understanding of the domain
Incorporating DDD requires effective communication between busi- and business requirements. Experienced domain experts are valuable in
ness specialists and software designers to ensure consistency in re- guiding the development team to create accurate and effective domain
quirements and conceptual models (Wanderley and Da Silveria, 2012).  models (Vural and Koyuncu, 2021). However, the availability of such
Misalignment in communication can lead to discrepancies in the final  domain experts may be limited, especially in specialized domains, and
design and implementation. this can hinder the DDD adoption process.
13

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
4.6. (RQ6) How has the effectiveness of DDD been assessed and measured 4.6.8. Time and resource consumption
in prior studies? In Häser et al. (2016) the effectiveness of including business domain
concepts in the DSL was measured by evaluating the perceived quality,
The effectiveness of DDD has been assessed and measured in prior creation time, and length of test case specifications.
studies through various evaluation methods and metrics. It is evident
from the data that prior studies have employed a combination of quan-
titative and qualitative evaluation methods to assess the effectiveness 4.6.9. Granularity and coupling analysis
of DDD. These methods are described in more detail in the following The study (Vural and Koyuncu, 2021) assessed the effectiveness
subsections. of DDD in microservices by comparing the coupling and cohesion
values of different examples. The study concluded that original exam-
4.6.1. Performance and resource metrics
ples achieved a good balance between low coupling and acceptable
In the case of Maddodi et al. (2020) the effectiveness of DDD
cohesion.
was measured by evaluating the performance and resource metrics
of the software system using Command Query Responsibility Segrega-
tion (CQRS) and Event Sourcing (ES) frameworks. The study reported
4.6.10. Prototype application
relative error values for throughput and response time for different
In Krause et al. (2020) the effectiveness of the approach for mod-
scenarios.
ernizing legacy lottery applications into microservices was evaluated
through its successful application to a real-world lottery application.
4.6.2. Feedback from stakeholders
In Uludağ et al. (2018) the effectiveness of DDD practices, such
as event storming workshops and domain modeling, was measured
4.6.11. Metamodel and design models
through the adoption and use of these practices by agile teams. The
study also considered feedback from stakeholders, including Program
Le et al. (2022) aimed to assess the efficacy of DDD in constructing
Managers, Product Owners, and Domain Architects, on the benefits and
Single Page Applications (SPAs) compatible with multiple platforms.
value of DDD in supporting large-scale agile software development.
For this purpose, they developed a novel metamodel and implemented a
hierarchical approach within the DDD framework. The outcomes of the
4.6.3. Context mapping and complexity reduction study revealed that employing the domain model as a central compo-
Landre et al. (2006) evaluated the effectiveness of DDD, particularly nent and adhering to the hierarchical DDD approach yielded favorable
the strategic part of it, by using context mapping and context relation- design models alongside prosperous generation of SPAs tailored for
ships to analyze the software architecture and identify complexities. various platforms.
The study demonstrated how DDD provides mechanisms to address the
identified problems and improve the quality of the Enterprise Archi-
tecture and derived software architectures by applying responsibility 4.7. (RQ7) Who are the key stakeholders involved and benefited in the
layers and improving scoping of projects. implementation of DDD?
4.6.4. Effectiveness of design guidelines
In the implementation of DDD, several key stakeholders are in-
Braun et al. (2021b) conducted an assessment to determine the
volved to ensure its successful application. These stakeholders encom-
efficacy of design guidelines pertaining to distributed data-intensive
pass a diverse set of roles, including software engineers, architects,
systems. The evaluation encompassed various metrics, including the
project managers, and domain experts. Through our SLR, we have
proportion of compatible domain operations and the extent of trivial
identified the following key stakeholders.
aggregates within the domain model.
4.6.5. Questionnaires and developer perception
4.7.1. Software engineers
The study by Özkan et al. (2023), the efficacy of DDD was evaluated
Software Engineers play a central role in implementing DDD princi-
using a combination of qualitative methods, including focus group
ples and practices in various software systems. They are responsible for
sessions, semi-structured interviews, and think-aloud protocols. Addi-
translating the domain model into code, implementing domain-specific
tionally, a quantitative analysis was conducted using the Technology
logic, and ensuring the alignment of the software architecture with the
Acceptance Model (mTAM) questionnaire. The findings revealed that
domain requirements (Singjai et al., 2021b; Maddodi et al., 2020; Peng
DDD positively impacted software maintainability, as developers per-
and Hu, 2007; Snoeck and Wautelet, 2022; Özkan et al., 2023).
ceived it. Similarly, Braun et al. (2021b) undertook an assessment of
design guidelines effectiveness by gauging developers’ perceptions in
their study.
4.7.2. Architects
4.6.6. Measuring effectiveness of ECD3 guidelines Architects are crucial in the implementation of DDD as they provide
In Braun et al. (2021a) the effectiveness of the DDD measured based strategic guidance and oversight on the overall software design. They
on Eventually Consistent Domain-Driven Design Guidelines (ECD3), collaborate with Software Engineers and other stakeholders to de-
assessed by conducting a comparative analysis between compatible fine the high-level architecture, bounded contexts, and domain models
and incompatible domain operations in the redesigned domain models. that capture the domain knowledge effectively (Maddodi et al., 2020;
The implementation of the recommended ECD3 guidelines exhibited a Kapferer and Zimmermann, 2021; Da Silva et al., 2022).
notable enhancement in the proportion of compatible operations within
the domain models.
4.7.3. Project managers
4.6.7. Software generation and complexity analysis Project managers play a vital role in coordinating DDD implemen-
The effectiveness of the DDD-based software generation method tation efforts. They ensure that DDD practices align with project goals,
proposed in Le et al. (2019) was evaluated by examining its linear allocate resources appropriately, and facilitate effective communication
time complexity and scalability on real-world software of considerable between different teams and stakeholders (Peng and Hu, 2007; Uludağ
magnitude, through the utilization of the jDomainApp framework. et al., 2018).
14

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
4.7.4. Domain experts 5.3. Bounded context and decomposition of microservices
Domain experts are individuals who possess in-depth knowledge of
the specific business domain for which the software system is being Bounded Context is another fundamental concept in DDD, and its
developed. Their active involvement is critical for refining the domain significance in microservices architecture is evident in several stud-
model, identifying key domain concepts, and validating the software’s ies (Maddodi et al., 2020; Peng and Hu, 2007; Josélyne et al., 2018;
alignment with real-world domain requirements (Singjai et al., 2021b; Uludağ et al., 2018; Braun et al., 2021b; Krause et al., 2020; Pereira
Uludağ et al., 2018; Da Silva et al., 2022). and Silva, 2022; Joselyne et al., 2021; Vural and Koyuncu, 2021;
In addition to the primary stakeholders mentioned above, the liter- Bünder and Kuchen, 2019). The concept of Bounded Context is used
ature also identifies other relevant participants involved in the imple- to define explicit boundaries where specific domain models apply,
mentation of DDD. These participants include Quality Assurance (QA) allowing the system to be decomposed into manageable, cohesive units.
Engineers, DevOps Engineers, UX Designers, Business Analysts, Systems Decomposing a system into microservices based on Bounded Contexts
Analysts, Data Modeling Specialists, and end-users (Peng and Hu, 2007; enables easier scaling, maintenance, and independent updating of each
Braun et al., 2021a; Özkan et al., 2023; Oukes et al., 2021; Häser et al., microservice.
2016; Bünder and Kuchen, 2019).
Taking our findings in consideration, we identified that the success- 5.4. Domain services, entities, and value objects as a tactical DDD
ful implementation of DDD requires close collaboration and communi-
cation among these diverse stakeholders to ensure that the developed Several studies discuss the use of Domain Services, Entities, and
software system effectively represents the domain’s complexity and Value Objects as part of DDD’s tactical patterns (Maddodi et al., 2020;
meets the business needs. The active engagement of software engineers, Le et al., 2022; Uludağ et al., 2018; Hippchen et al., 2017; Özkan et al.,
architects, project managers, and domain experts, along with the con- 2023; Pereira and Silva, 2022). Domain Services are employed to han-
tributions from other relevant participants, enables the application of dle application tasks and technical code that is not part of the core busi-
DDD principles to create robust and domain-centric software solutions. ness logic, while Entities and Value Objects represent different entities
and their relationships in the domain model. These concepts contribute
to modeling complex business domains and enabling object-oriented
5. Discussions
representations of domain concepts.
In this section, we aim to consolidate and evaluate the extensive 5.5. ACL for maintaining domain integrity
range of information obtained through our RQs in order to present a
comprehensive overview of the effectiveness, challenges, and potential When dealing with different bounded contexts, interacting with
consequences associated with the adoption of DDD in software devel- external systems or refactoring legacy systems, the risk of corrupting
opment. Throughout this section, we will do an examination of the a domain model with concepts and structures from another context is
findings by establishing connections across various studies and identify- high. The ACL acts as a safeguard, ensuring that each context’s domain
ing recurring themes and patterns. It is important to acknowledge that remains untainted and independent. The concept of the ACL is dis-
certain aspects of the discussion have already been addressed in Sec- cussed in some studies (Peng and Hu, 2007; Josélyne et al., 2018; Lan-
tion 4 when answering to the RQs. Nevertheless, within this dedicated dre et al., 2006; Le et al., 2018). It is utilized in the studies to manage
section, we will explore further nuances, ramifications, and potential dependencies between different domains, preventing the contamination
applications attributable to DDD based on the available evidence. of contexts, safeguard the domain model of a Bounded Context from
changes in other contexts, segregating application-specific elements
5.1. Adoption and implementation of DDD from domain-specific components in microservices and maintaining
consistency between aggregates. Studies also suggests that ACL shields
new contexts from potential contaminations or disruptions originating
Several studies report successful implementations of DDD, showcas-
in legacy contexts.
ing its ability to improve software design, maintainability, scalability,
and agility. DDD concepts, such as Ubiquitous Language, Bounded
5.6. All hands on deck: It is not only about software engineers
Contexts, Aggregates, Entities, Value Objects, and Domain Events, are
commonly utilized to model complex domains effectively. Many re-
Based on the data extracted from the literature, the implementation
searchers emphasize the significance of defining clear domain bound-
of DDD involves the active participation of various key stakeholders
aries and using a common language between domain experts and soft-
who play critical roles in ensuring its successful application. These
ware designers to ensure effective communication and understanding.
stakeholders encompass a diverse set of roles, including Software En-
Additionally, DDD is frequently integrated with other software develop-
gineers, Architects, Project Managers, and Domain Experts. Software
ment paradigms, such as microservices and event-driven architecture,
Engineers hold a central position in the DDD implementation process,
to achieve better modularity and maintainable systems.
responsible for translating the domain model into executable code,
implementing domain-specific logic, and aligning the software architec-
5.2. Ubiquitous language as a core principle of DDD ture with domain requirements (Singjai et al., 2021b; Maddodi et al.,
2020; Peng and Hu, 2007; Snoeck and Wautelet, 2022; Özkan et al.,
The data analyzed points out that the Ubiquitous Language stands 2023). Architects contribute strategic guidance and oversight to the
as a foundational principle of DDD. It ensures a shared and consistent overall software design, collaborating with Software Engineers and
understanding of the domain between stakeholders, including business other stakeholders to define high-level architecture, bounded contexts,
specialists, software designers, and developers (Evans, 2004). The stud- and domain models that effectively capture domain knowledge (Mad-
ies consistently emphasize the importance of Ubiquitous Language in dodi et al., 2020; Kapferer and Zimmermann, 2021; Da Silva et al.,
facilitating communication, clarifying domain concepts, and improving 2022).
collaboration among team members (Singjai et al., 2021b; Maddodi Project Managers play a vital role in coordinating DDD implementa-
et al., 2020; Josélyne et al., 2018; Perillo et al., 2009; Le et al., 2019, tion efforts, ensuring alignment with project goals, resource allocation,
2022; Uludağ et al., 2018; Danenas and Garsva, 2012; Hippchen et al., and effective communication between teams and stakeholders (Peng
2017; Ding et al., 2020; Özkan et al., 2023; Pereira and Silva, 2022; and Hu, 2007; Uludağ et al., 2018). Domain Experts, possessing in-
Wanderley and Da Silveria, 2012; Le et al., 2018). depth knowledge of the specific business domain, actively contribute
15

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
Fig. 6. DDD studies grouped by their software systems and publication years.
to refining the domain model, identifying key domain concepts, and Özkan et al., 2023; Mayer and Weinreich, 2018). However, several
validating the software’s alignment with real-world domain require- studies lack specific evaluation results or empirical evidence (Perillo
ments (Singjai et al., 2021b; Uludağ et al., 2018; Da Silva et al., et al., 2009; Krause et al., 2020; Ding et al., 2020; Wanderley and
2022). Da Silveria, 2012; Abeck et al., 2019; Bünder and Kuchen, 2019).
Moreover, the literature also identifies other relevant participants To establish a more comprehensive understanding of the benefits
involved in the DDD implementation, including QA Engineers, DevOps and potential challenges of implementing DDD in different software de-
Engineers, UX Designers, Business Analysts, Systems Analysts, Data velopment scenarios, further empirical research is needed. Researchers
Modeling Specialists, and end-users (Peng and Hu, 2007; Braun et al., and practitioners should focus on collecting concrete metrics, conduct-
2021a; Özkan et al., 2023; Oukes et al., 2021; Häser et al., 2016; ing real-world case studies, and measuring the perception of practition-
Bünder and Kuchen, 2019). The successful implementation of DDD ers. We believe that it is also essential to involve human metrics, such
requires close collaboration and communication among these diverse as user feedback and assessments from domain experts, architects, and
stakeholders to ensure that the developed software system effectively experienced developers. Considering the challenges in implementing
represents the domain’s complexity and meets the business needs. The DDD, human-centric evaluations can provide valuable insights into
active engagement of software engineers, architects, project managers, the effectiveness of DDD and its impact on the software development
and domain experts, along with the contributions from other relevant process.
participants, enables the application of DDD principles to create robust
and domain-centric software solutions. The involvement of these stake- 5.8. Rise of the microservices in DDD
holders enhances the alignment of software systems with real-world
domain requirements and fosters the development of high-quality and Our SLR reveals a significant shift in the popularity of microservices
effective software solutions. in DDD studies starting 2017 and at peak in 2021. As depicted in Fig. 6,
Our review adds a nuanced view of how this collaboration evolves
prior to 2017, credible DDD studies specifically focusing on microser-
in practice. Rather than treating the developer–domain expert relation-
vices were scarce, indicating a lack of attention in this area. However,
ship as static, the primary studies reflect varied degrees of maturity in
from 2017 onwards, we observed a notable increase in the number of
this interaction. For instance, some report structured practices such as
studies exploring the application of DDD principles in the context of mi-
Event Storming workshops (Uludağ et al., 2018), while others high-
croservices. This trend aligns with the findings of a Systematic Mapping
light onboarding challenges and communication gaps (Özkan et al.,
Study on Microservices conducted by Hamzehloui et al. (2018) in 2018,
2023; Wanderley and Da Silveria, 2012). This range of experiences
which also reports a rising number of evaluation papers, suggesting that
suggests that bridging the gap is not a one-time activity, but an ongoing
microservices have been gaining wider implementation in real-world
and often iterative process influenced by tooling, team experience,
software development scenarios.
and organizational context — a perspective less emphasized in prior
Furthermore, Viggiato et al. (2018) in 2018 highlights the increas-
ing popularity of microservices architectures, further emphasizing the
discussions.
growing relevance and adoption of microservices in the software in-
dustry. In a similar vein, Knoche and Hasselbring (2019) in 2019 notes
5.7. Evaluation of DDD effectiveness that many companies are actively considering whether microservices
are a viable option for their applications, indicating the considerable
The evaluation of DDD effectiveness varies across studies. Some interest and attention surrounding the adoption of microservices-based
studies present empirical evaluations based on metrics, user feedback, architectures.
or controlled experiments (Singjai et al., 2021b; Maddodi et al., 2020; The convergence of our findings with those of the previously men-
Uludağ et al., 2018; Braun et al., 2021b; Danenas and Garsva, 2012; tioned studies and experts further corroborates the growing significance
16

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
of microservices in the domain of software development, especially in Our findings indicate a healthy mix of academic and industry stud-
the context of DDD methodologies. The upward trend in microservices ies, reflecting the growing interest in DDD from both research and
adoption is evident from the year 2017 onwards, indicating a turning practical application perspectives. While academic studies contribute
point in the landscape of software development practices. Beyond iden- theoretical advancements and innovative approaches, industry-focused
tifying the rise in microservices, our study offers novel insights into how studies demonstrate the real-world applicability and effectiveness of
DDD contributes to shaping modularity in such architectures. In partic- DDD principles in solving complex software design and development
ular, we observe that practitioners increasingly rely on DDD patterns challenges. More interaction between academia and industry in DDD
like Bounded Contexts and Aggregates to define service boundaries research could potentially facilitate the transfer of knowledge and
and promote semantic clarity. While prior studies may suggest that best practices, contributing to the further advancement and adoption
microservices benefit from domain-aligned decomposition, our findings of DDD principles in real-world software development scenarios, as
ground this assumption in a broader empirical base across 36 peer- successfully demonstrated in Özkan et al. (2023).
reviewed studies. This synthesis provides stronger evidence for how
DDD actively influences microservice design practices in both academic 5.10.1. Contrasting academic and industry perspectives
and industrial settings. While our study includes a balanced set of academic (58.3%) and
industry (36.1%) studies — with a small number of hybrid cases (5.6%)
5.9. Challenges and considerations in implementing DDD effectively
— the practical perspectives from industry deserve further distinction.
Academic research on DDD tends to focus on conceptual modeling,
tool development (e.g., DSLs, context mapping tools), and theoretical
To ensure the successful implementation of DDD, it is essential
discussions on patterns such as Bounded Contexts or Entities. These
to employ DDD patterns accurately and efficiently. Proper utilization
studies often propose frameworks or methodologies but may lack con-
of DDD principles demands a skilled team consisting of experienced
crete empirical validation. In contrast, industry studies are generally
developers, domain experts, and seasoned architects (Özkan et al.,
more experience-driven, describing real-world applications of DDD
2023). The significance of experience in DDD cannot be overstated,
in large-scale systems such as microservices, enterprise refactoring,
as we have observed from various studies that onboarding to DDD
or system modernization. These studies prioritize architectural prag-
is not a straightforward process, and the expertise of developers sig-
matism, performance concerns, and integration challenges, and often
nificantly influences the success of the implementation (Kapferer and
highlight the social or organizational implications of DDD adoption
Zimmermann, 2021; Özkan et al., 2023).
(e.g., communication, onboarding, and team alignment).
Implementing DDD effectively requires a substantial amount of
For example, the academic studies often examine how to formal-
attention and effort, particularly when integrating it into existing soft-
ize context boundaries using modeling tools like Context Mapper or
ware systems. The transition from traditional software development
domain-specific languages, whereas the industry studies report prac-
approaches to DDD can be challenging, and the process demands
tical experience applying bounded contexts in cross-functional teams
careful planning, training, and a clear understanding of the DDD con-
or resolving communication issues between developers and domain ex-
cepts and principles. Seasoned developers with prior experience in
perts. Moreover, industry papers tend to use anecdotal or case-based ev-
DDD are more likely to grasp the complexities and intricacies of the
idence, while academic studies more frequently advocate for abstract,
approach, resulting in better-designed and more maintainable software
generalizable models. This contrast reveals complementary strengths:
systems (Hippchen et al., 2017). On the other hand, inexperienced
academia offers methodological structure and design guidance, while
developers may struggle to fully utilize the benefits of DDD, leading
industry grounds these concepts in complex, evolving development
to potential issues in the implementation process.
environments. Recognizing this distinction helps to contextualize the
Furthermore, the involvement of domain experts plays a crucial role
relevance and maturity of DDD research across settings.
in the success of DDD implementation. Their deep understanding of the
business domain is invaluable in guiding the development team to cre-
5.11. A critical analysis of research quality in the DDD literature
ate accurate and effective domain models (Vural and Koyuncu, 2021).
However, acquiring experienced domain experts can be challenging,
The analyzed studies demonstrate varying degrees of adherence to
especially in specialized domains. Their scarcity may pose hurdles in
DDD principles and the effective application of DDD concepts. While
the adoption of DDD, but their involvement is crucial for crafting
some studies effectively apply DDD principles, others exhibit shortcom-
domain models that truly reflect the intricacies and requirements of
ings in implementation and evaluation. To enhance research quality,
the real-world domain.
future studies should emphasize the consistent use of Ubiquitous Lan-
guage, explicit definition of Bounded Contexts, proper utilization of Do-
5.10. Academia-industry collaboration main Events and DDD patterns, and robust evaluation methodologies.
Additionally, studies should openly discuss the challenges and limita-
The academic studies in our SLR predominantly emphasize the tions of DDD, contributing to a more comprehensive understanding of
theoretical aspects of DDD. They explore the foundational principles its potential and practical implications in software development.
and patterns of DDD, such as Ubiquitous Language, Bounded Con- Several studies employed the notion of Ubiquitous Language, which
text, Entities, and Value Objects. These studies often propose novel facilitates effective communication between stakeholders and software
frameworks, tools and methodologies that extend the DDD concepts to designers by creating a shared vocabulary. However, a few studies
specific problem domains. While they provide valuable insights into the failed to implement this language consistently, potentially hindering
theoretical underpinnings of DDD, they might lack empirical validation communication and understanding among team members. Future re-
and practical implementation in real-world projects. search should emphasize the importance of adopting and consistently
On the other hand, we experienced that the industry-focused studies applying Ubiquitous Language throughout the development process to
put DDD principles into practice in various software systems. They ensure better alignment and clarity.
showcase how DDD is applied to real-world projects and explore its Bounded Context, another key concept in DDD, helps define explicit
impact on system design, architecture, and development. These studies boundaries where specific domain models apply (Evans, 2004; Vernon,
often involve case studies and experience reports from software en- 2016). While some studies effectively utilized Bounded Context to
gineers, architects, and domain experts. The emphasis is on practical organize and segregate domains, others did not explicitly mention or
implementation, challenges faced, and lessons learned while applying implement this principle. Ensuring clear identification and definition
DDD in complex software projects. of Bounded Contexts is crucial for managing interactions between
17

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
different models and contexts, and future studies should focus on this software components with evolving business needs. Practitioners aim-
aspect to enhance research quality. ing to modernize legacy systems should consider using context maps
The application of Domain Events to trigger behavior across multi- and ACLs (as highlighted in Section 4.5) to incrementally isolate and
ple aggregates within a Bounded Context was observed in some studies. refactor legacy code while preserving domain integrity.
However, not all studies effectively leveraged this concept. Imple- Additionally, DDD has demonstrated benefits in improving code
menting Domain Events can improve event-driven communication and quality and software construction in web applications and development
coordination between domain components, promoting a more cohesive tools (Le et al., 2022; Perillo et al., 2009; Kapferer and Zimmer-
and flexible architecture (Evans, 2004; Vernon, 2016). Future research mann, 2020). In Section 4.3, studies report that domain annotations
should explore the potential benefits of Domain Events in event-driven and modeling tools help practitioners maintain separation of concerns
systems and provide concrete examples of their implementation. and automate parts of the development process. These insights can
Several studies showcased the use of Aggregates, Entities, and Value guide practitioners in selecting DDD-aligned tools that improve code
Objects to model complex business domains. While these concepts maintainability (Le et al., 2022) and streamline software generation.
were well-implemented in some cases, others lacked specific details However, DDD is not without its challenges. As discussed in Sec-
or provided inadequate explanations about their usage. To bolster tion 4.5, one of the most significant obstacles is the steep learning
research quality, studies should strive for comprehensive and consistent curve, especially for developers new to DDD (Özkan et al., 2023; Hip-
implementation of these DDD patterns, ensuring a clear understanding pchen et al., 2017). Misunderstandings in the application of patterns,
of their roles and relationships within the domain model. unclear decomposition strategies, and the misalignment between teams
We observed that Strategic Design patterns such as Core Domain, and domains are common pitfalls. To mitigate this, practitioners should
Shared Kernel, and upstream–downstream relationships were underre- invest in onboarding initiatives, including dedicated DDD training ses-
ported in most studies. This suggests a possible gap in the literature, sions, domain modeling workshops (e.g., Event Storming (Uludağ et al.,
where tactical DDD patterns are emphasized, but strategic alignment 2018)), and mentorship from experienced architects (see Table 8).
is less frequently explored or documented. Future research should pay Implications for Researchers. Despite the progress made in un-
more attention to these higher-level design patterns to understand their derstanding the application and benefits of DDD, Section 4.6 shows
role in system architecture and team collaboration. that only a limited number of studies (approximately 39%) employ
One significant aspect that emerged from the data was the lack empirical evaluations. Future research should prioritize the design of
of specific evaluation methods in some studies. While some research empirical studies with concrete evaluation metrics — such as team pro-
incorporated empirical evaluations, others relied solely on proposing ductivity, domain alignment, and architectural complexity — to mea-
methodologies or demonstrating case studies without conducting rig- sure the actual impact of DDD adoption in industrial settings (Singjai
orous evaluations. Future studies should adopt more robust evaluation et al., 2021b; Maddodi et al., 2020; Uludağ et al., 2018).
methods, such as controlled experiments, surveys, or user feedback, to
Furthermore, Section 4.5 indicates that the complexity of managing
assess the effectiveness of DDD implementation and provide empirical
domain boundaries, integrating DDD with legacy systems, and support-
evidence to support their findings.
ing DSL-based tooling are persistent technical challenges. Researchers
Moreover, most studies did not discuss the challenges and limi- should explore novel techniques — e.g., automated decomposition,
tations associated with DDD adoption, leaving potential gaps in ad- model-code synchronization, and refactoring strategies — to support
dressing concerns or drawbacks of the approach. To improve research scalable DDD adoption in complex environments (Braun et al., 2021b;
quality, studies should acknowledge and discuss both the advantages Özkan et al., 2023).
and limitations of DDD, offering a balanced view to readers and prac-
Another important research direction involves studying stakeholder
titioners. This will help in understanding the practical implications of
dynamics. Section 4.7 emphasizes the critical role of collaboration
DDD and guide future research and implementation efforts.
between software engineers, architects, and domain experts in the
Future research can provide a more comprehensive and balanced
success of DDD. Yet, communication breakdowns and a lack of do-
analysis of DDD by addressing these areas to contribute to the advance-
main understanding remain major barriers (Wanderley and Da Silve-
ment of knowledge and practice in the field of software development.
ria, 2012; Da Silva et al., 2022). Researchers could investigate socio-
technical methods (e.g., participatory modeling (Voinov and Bousquet,
6. Implications 2010; Brandolini, 2019), collaborative tooling (Famelis et al., 2012))
to bridge this gap and formalize co-design practices.
In this section, we introduce the implications of our findings for In addition, Section 4.6 reveals that studies vary widely in how they
both practitioners and researchers. We draw on the results presented in evaluate DDD. Developing standardized frameworks and reproducible
our RQs to ground our implications in the evidence synthesized from evaluation methodologies will help unify the field and allow compari-
the primary studies. son across contexts (Özkan et al., 2023; Le et al., 2022). Incorporating
Implications for Practitioners. One of the primary implications both technical metrics (e.g., coupling, cohesion) and human-centered
for practitioners is the recognition of the diverse benefits that DDD metrics (e.g., developer perception, onboarding effort) can lead to a
can bring to various software systems. The application of DDD prin- more holistic understanding of DDD’s effectiveness.
ciples has been shown to improve the modularity, maintainability, and Based on our findings, future research should prioritize empirical
scalability of microservices-based applications (Section 4.3), thereby studies that not only report qualitative insights but also collect large-
enabling organizations to handle complex and distributed systems more scale (e.g. via repository mining for DDD similar to Babur et al. (2024)),
effectively (Singjai et al., 2021b; Josélyne et al., 2018; Wang et al., longitudinal and team-level data. While several studies use focus groups
2022). Practitioners can leverage these insights to enhance their soft- and interviews, we observed a lack of sustained evaluations on aspects
ware architecture and development practices by adopting DDD pat- such as maintainability, modularity drift over time, or onboarding ef-
terns such as Bounded Contexts and Aggregates to define clear service fectiveness. Studies like Braun et al. (2021b,a) and Özkan et al. (2023)
boundaries and promote decoupling. demonstrate the potential of combining qualitative feedback with struc-
Moreover, the adoption of DDD in enterprise software systems has tured metrics, yet these efforts remain isolated. To build on this,
proven valuable in addressing challenges related to legacy system researchers could design action research or longitudinal case studies
modernization and increasing architectural complexity (Maddodi et al., that track DDD adoption over multiple sprints or releases, focusing on
2020; Peng and Hu, 2007; Uludağ et al., 2018). Section 4.2 illustrates how domain alignment evolves, how design debt is managed, and how
how DDD facilitates flexible and maintainable architectures by aligning development teams adapt. Similarly, design-science-based evaluations
18

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
of modeling tools (e.g., Context Mapper) can shed light on how tooling search approach was aimed at encompassing a wide range of academic
impacts the domain-code connection in practical workflows. These sources and reducing potential biases in the selection of studies.
directions would help close both methodological and tooling-related Language Bias. The SLR focused primarily on studies published
gaps identified in current literature. in English, which might introduce a language bias. Relevant research
By addressing these research gaps, scholars can contribute not only conducted in other languages could have been omitted, potentially
to the theoretical advancement of DDD but also to practical guidelines, impacting the comprehensiveness of the review.
tool support, and empirical validation frameworks that help teams Agreement Level During Quality Assessment. Another potential
successfully adopt DDD in complex software projects. threat to validity is the lack of assessment of agreement levels between
assessors during the quality assessment stage. While Cohen’s Kappa was
7. Limitations and threats to validity
used to evaluate inter-rater reliability during the inclusion/exclusion
stage, no similar measure was applied during the quality assessment
Some limitations and validity considerations are applicable for SLR
of the included studies. This omission could introduce subjectivity and
studies (Petersen et al., 2015, 2008). The limitations and threats to the
potential bias in the quality assessment process, as individual assessors
validity of this study are discussed in this section.
may have differing interpretations of quality criteria. However, dur-
Timeframe and Currency. One limitation is the timeframe of the
ing the quality assessment stage, in cases of disagreement or doubt,
literature search and the currency of the included studies. The SLR is
the assessors consulted with each other to reach a consensus. This
based on data available up to June 2023, and relevant studies published
approach used to ensure that the quality assessments were rigorous,
after that date might have been missed. The field of DDD is rapidly
minimized potential biases, and allowed discrepancies to be resolved
evolving, and newer developments or trends may not be fully captured
systematically.
in this review.
Study-Specific Validity Considerations. In addition to general
Quality of Studies. The quality of individual studies can impact
methodological considerations, we acknowledge several threats specific
the overall reliability of the SLR findings. The included studies vary
to our study. First, our focus on implementation-related search terms
in terms of methodological rigor, sample size, and research design.
(e.g., refactor*, improv*, optimiz*) may have led to the exclusion of
Some studies might have limitations or biases that could influence
relevant DDD papers that are more theoretical or descriptive in nature.
their results and subsequent conclusions. Nonetheless, we endeavored
This trade-off was a deliberate decision to ensure practical relevance,
to rigorously exclude studies of low quality by systematically applying
but it may affect the completeness of our study population. Second,
inclusion and exclusion criteria as well as conducting thorough quality
while our inclusion of forward snowballing from Evans’ seminal book
assessments.
aimed to enrich the dataset with practically grounded work, it may also
Inclusion and Exclusion Criteria. The effectiveness of an SLR
have introduced a bias toward studies that cite this particular source,
largely depends on the clarity and appropriateness of the inclusion and
possibly underrepresenting alternative DDD schools of thought. Finally,
exclusion criteria. Despite our efforts to define comprehensive criteria,
our coding and classification of DDD patterns — especially in distin-
there is a possibility of unintentionally excluding relevant studies or
guishing strategic vs. tactical applications — required interpretation
including studies that do not precisely fit the research questions. To
and contextual judgment. Despite using a predefined form and multiple
mitigate this potential limitation, a rigorous approach was adopted.
authors reviewing the coding, subjectivity may still have influenced the
Two authors independently applied predefined inclusion and exclu-
final categorization.
sion criteria to a randomly selected pool of 60 studies. The level of
agreement between the two authors was assessed using Cohen’s Kappa
coefficient (Cohen, 1960), a widely accepted measure of inter-rater 8. Conclusion
reliability. Encouragingly, the analysis revealed a perfect agreement
between the authors in their decisions regarding study inclusion and
exclusion within the randomly sampled studies. This robust agreement
This SLR provides a comprehensive overview of the effectiveness,
underscores the reliability of the selection process and enhances the
challenges, and implications of adopting DDD in software development.
credibility of the findings.
Through the analysis of a diverse set of primary studies, we identified
Bias in Data Extraction. A limitation related to the validity of
key stakeholders involved in the implementation of DDD, including
data extraction in this study is the potential for human error or bias
Software Engineers, Architects, Project Managers, and Domain Ex-
during the data extraction process. Despite efforts to maintain con-
perts. These stakeholders play critical roles in ensuring the successful
sistency and accuracy, the interpretation of information from primary
application of DDD principles and practices in various software systems.
studies could be influenced by the subjectivity of the researchers. Dif- The findings highlight the significance of Ubiquitous Language as
ferent individuals extracting data may interpret the findings differently a core principle of DDD, emphasizing its role in facilitating effective
or unintentionally introduce errors, leading to inconsistencies in the communication and collaboration among team members. Bounded Con-
extracted data. To address this limitation, a careful and systematic texts and the decomposition of microservices stand out as fundamental
approach was employed, and multiple researchers were involved in the concepts in DDD, enabling the creation of scalable and maintainable
data extraction process. Inter-rater reliability checks and discussions software systems. Domain Services, Entities, and Value Objects serve as
among the researchers were conducted to ensure agreement and min- tactical DDD patterns, contributing to the modeling of complex business
imize discrepancies. However, it is essential to acknowledge that the domains.
possibility of human-related errors cannot be entirely eliminated, and The implementation of DDD demands considerable attention and ef-
they may have some impact on the final results and conclusions of the fort, particularly in transitioning from traditional software development
systematic literature review. approaches to DDD. Experienced developers and domain experts play
Publication Bias. One potential threat to validity is publication crucial roles in effectively implementing DDD concepts. The involve-
bias. The studies included in this SLR were obtained from various ment of domain experts is especially critical for crafting domain models
academic databases and sources, which might not represent the entire that accurately represent real-world domain requirements.
body of literature on DDD. Some studies might not have been pub- The SLR also highlights the rise of microservices in the context of
lished or accessible, leading to a skewed representation of the research DDD, indicating a significant shift in the popularity of microservices-
landscape. Nevertheless, to mitigate this bias, we performed a compre- based architectures since 2017. However, further empirical research is
hensive search across multiple academic databases, including Google needed to comprehensively understand the benefits and challenges of
Scholar and Scopus during the snowballing process. This extensive implementing DDD in different software development scenarios.
19

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
The collaboration between academia and industry in DDD research Buschmann, F. (Ed.), 1996. Pattern-Oriented Software Architecture: A System of
is evident, with academic studies contributing theoretical advance- Patterns. Wiley, Chichester ; New York.
ments and innovative approaches, while industry-focused studies show- Camilli, M., Colarusso, C., Russo, B., Zimeo, E., 2023. Actor-driven decomposition of
microservices through multi-level scalability assessment. ACM Trans. Softw. Eng.
case practical implementation and real-world applicability. This collab-
Methodol. 3583563. http://dx.doi.org/10.1145/3583563.
oration can facilitate knowledge transfer and best practices, contribut- Cohen, J., 1960. A coefficient of agreement for nominal scales. Educ. Psychol. Meas.
ing to the advancement and adoption of DDD principles in software 20 (1), 37–46. http://dx.doi.org/10.1177/001316446002000104.
development. Da Silva, C.E., Gomes, E.L., Basu, S.S., 2022. BPM2DDD: A systematic process for
identifying domains from business processes models. Software 1 (4), 417–449.
A critical analysis of research quality in the DDD literature reveals
http://dx.doi.org/10.3390/software1040018.
varying degrees of adherence to DDD principles and the effective Danenas, P., Garsva, G., 2012. Domain driven development and feature driven devel-
application of DDD concepts. Future studies should emphasize the opment for development of decision support systems. In: Skersys, T., Butleris, R.,
consistent use of Ubiquitous Language, clear definition of Bounded Butkiene, R. (Eds.), Information and Software Technologies. vol. 319, Springer
Contexts, proper utilization of Domain Events and DDD patterns, and
Berlin Heidelberg, Berlin, Heidelberg, pp. 187–198. http://dx.doi.org/10.1007/978-
3-642-33308-8_16.
robust evaluation methodologies. Moreover, studies should openly dis- De Goey, H., Hilletofth, P., Eriksson, L., 2019. Design-driven innovation: A systematic
cuss the challenges and limitations of DDD to provide a comprehensive literature review. Eur. Bus. Rev. 31 (1), 92–114. http://dx.doi.org/10.1108/EBR-
understanding of its potential and practical implications. 09-2017-0160.
DDD offers valuable insights and practices for software develop-
Ding, Y., Wang, L., Li, S., Wang, X., Zhang, J., 2020. Enterprise service application
architecture based on domain driven model design. In: 2020 2nd Interna-
ment, fostering communication, and collaboration among stakeholders
tional Conference on Information Technology and Computer Application. ITCA,
while modeling complex business domains. However, its successful im- IEEE, Guangzhou, China, pp. 778–784. http://dx.doi.org/10.1109/ITCA52113.
plementation depends on the expertise of stakeholders, proper utiliza- 2020.00167.
tion of DDD principles, and the adoption of robust evaluation methods. Dragoni, N., Giallorenzo, S., Lafuente, A.L., Mazzara, M., Montesi, F., Mustafin, R.,
Safina, L., 2017. Microservices: Yesterday, today, and tomorrow. http://dx.doi.org/
As software systems continue to grow in complexity, DDD remains a
10.48550/arXiv.1606.04036, arXiv:1606.04036.
relevant and promising approach for developing domain-centric and Evans, E., 2004. Domain-Driven Design: Tackling Complexity in the Heart of Software.
scalable software solutions. Addison-Wesley, Boston.
Famelis, M., Salay, R., Chechik, M., 2012. Partial models: Towards modeling and
CRediT authorship contribution statement reasoning with uncertainty. In: Proceedings of the 34th International Conference
on Software Engineering. ICSE, IEEE, pp. 573–583.
Fritzsch, J., Bogner, J., Wagner, S., Zimmermann, A., 2019. Microservices migration
Ozan Özkan: Writing – review & editing, Writing – original draft, in industry: intentions, strategies, and challenges. In: 2019 IEEE International
Project administration, Methodology, Investigation, Formal analysis, Conference on Software Maintenance and Evolution. ICSME, IEEE, Cleveland, OH,
Data curation, Conceptualization. Önder Babur: Validation, Supervi- USA, pp. 481–490. http://dx.doi.org/10.1109/ICSME.2019.00081.
Gamma, E., Helm, R., Johnson, R.E., Vlissides, J., 2009. Design Patterns: Elements
sion. Mark van den Brand: Supervision.
of Reusable Object-Oriented Software. Addison-Wesley, Reading, MA, OCLC:
624525693.
Declaration of competing interest Giray, G., Bennin, K.E., Köksal, Ö., Babur, Ö., Tekinerdogan, B., 2023. On the use
of deep learning in software defect prediction. J. Syst. Softw. 195, 111537.
The authors declare that they have no known competing finan- http://dx.doi.org/10.1016/j.jss.2022.111537, URL https://linkinghub.elsevier.com/
cial interests or personal relationships that could have appeared to
Ham
r
m
et
a
r
r
ie
st
v
r
e
ö
/
m
pi
,
i /
P
S
.
0
,
16
H
4
e
1
r
2
zo
1
g
2
,
2 2
E
0
.
0
,
2
2
1
0
3
1
8
6
.
. Experience from integrating domain driven
influence the work reported in this paper. software system design into a systems engineering organization. INCOSE Int. Symp.
26 (1), 1192–1203. http://dx.doi.org/10.1002/j.2334-5837.2016.00220.x.
Data availability Hamzehloui, M.S., Sahibuddin, S., Salah, K., 2018. A systematic mapping study on
microservices. In: Advances in Intelligent Systems and Computing. Springer Inter-
national Publishing, pp. 1079–1090. http://dx.doi.org/10.1007/978-3-319-99007-
Data will be made available on request.
1_100.
Häser, F., Felderer, M., Breu, R., 2016. Is business domain language support beneficial
for creating test case specifications: A controlled experiment. Inf. Softw. Technol.
References 79, 52–62. http://dx.doi.org/10.1016/j.infsof.2016.07.001.
Hippchen, B., Giessler, P., Steinegger, R.H., Schneider, M., Abeck, S., 2017. Designing
Abeck, S., Schneider, M., Quirmbach, J.-P., Klarl, H., Urbaczek, C., Zogaj, S., 2019. microservice-based applications by using a domain-driven design approach.
A context map as the basis for a microservice architecture for the connected car Joselyne, M.I., Bajpai, G., Nzanywayingoma, F., 2021. A systematic framework of ap-
domain. http://dx.doi.org/10.18420/INF2019_18. plication modernization to microservice based architecture. In: 2021 International
Avram, A., Marinescu, F., 2006. Domain-driven design quickly: a summary of eric evans’ Conference on Engineering and Emerging Technologies. ICEET, IEEE, Istanbul,
domain-driven design. In: Enterprise Software Development Series, C4Media. Turkey, pp. 1–6. http://dx.doi.org/10.1109/ICEET53442.2021.9659783.
Babur, Ö., Constantinou, E., Serebrenik, A., 2024. Language usage analysis for EMF Josélyne, M.I., Tuheirwe-Mukasa, D., Kanagwa, B., Balikuddembe, J., 2018. Partitioning
metamodels on GitHub. Empir. Softw. Eng. 29 (1), 23. microservices: A domain engineering approach. In: Proceedings of the 2018
Bertoni, A., 2020. Data-driven design in concept development: systematic review and International Conference on Software Engineering in Africa. ACM, Gothenburg
missed opportunities. Proc. Des. Soc.: Design Conf. 1, 101–110. http://dx.doi.org/ Sweden, pp. 43–49. http://dx.doi.org/10.1145/3195528.3195535.
10.1017/dsd.2020.4. Kapferer, S., Zimmermann, O., 2020. Domain-driven service design. In: Service-Oriented
Brandolini, A., 2013. Introducing EventStorming – an explosive modeling tech- Computing. In: Communications in Computer and Information Science, Springer
nique for lean discovery. https://ziobrando.blogspot.com/2013/11/introducing- International Publishing, Cham, pp. 189–208.
eventstorming.html. (Accessed April 2025). Kapferer, S., Zimmermann, O., 2021. Domain-driven architecture modeling and rapid
Brandolini, A., 2019. Introducing EventStorming: An Act of Deliberate Collective prototyping with context mapper. In: Hammoudi, S., Pires, L.F., Selić, B. (Eds.),
Learning. Leanpub. Model-Driven Engineering and Software Development. vol. 1361, Springer In-
Braun, S., Bieniusa, A., Elberzhager, F., 2021a. Advanced domain-driven design for ternational Publishing, Cham, pp. 250–272. http://dx.doi.org/10.1007/978-3-030-
consistency in distributed data-intensive systems. In: Proceedings of the 8th 67445-8_11.
Workshop on Principles and Practice of Consistency for Distributed Data. ACM, Kitchenham, B., Charters, S., 2007. Guidelines for performing systematic literature
Online United Kingdom, pp. 1–12. http://dx.doi.org/10.1145/3447865.3457969. reviews in software engineering 2.
Braun, S., Deßloch, S., Wolff, E., Elberzhager, F., Jedlitschka, A., 2021b. Tackling Knoche, H., Hasselbring, W., 2019. Drivers and barriers for microservice adoption – A
consistency-related design challenges of distributed data-intensive systems: An Survey among professionals in Germany. Enterp. Model. Inf. Syst. Archit. (EMISAJ)
action research study. In: Proceedings of the 15th ACM / IEEE International 1:1–35. http://dx.doi.org/10.18417/EMISA.14.1.
Symposium on Empirical Software Engineering and Measurement. ESEM, ACM, Bari Koryl, M., 2017. Active resources concept of computation for enterprise software. Arch.
Italy, pp. 1–11. http://dx.doi.org/10.1145/3475716.3475771. Contol. Sci. 27 (2), 279–291. http://dx.doi.org/10.1515/acsc-2017-0018.
Bünder, H., Kuchen, H., 2019. A model-driven approach for behavior-driven GUI Krause, A., Zirkelbach, C., Hasselbring, W., Lenga, S., Kroger, D., 2020. Microservice
testing. In: Proceedings of the 34th ACM/SIGAPP Symposium on Applied Comput- decomposition via static and dynamic analysis of the monolith. In: 2020 IEEE
ing. ACM, Limassol Cyprus, pp. 1742–1751. http://dx.doi.org/10.1145/3297280. International Conference on Software Architecture Companion. ICSA-C, IEEE,
3297450. Salvador, Brazil, pp. 9–16. http://dx.doi.org/10.1109/ICSA-C50368.2020.00011.
20

O. Özkan et al. The Journal of Systems & Software 230 (2025) 112537
Kuhrmann, M., Fernández, D.M., Daneva, M., 2017. On the pragmatic design of Perillo, J.R.C., Guerra, E.M., Fernandes, C.T., 2009. Daileon: A tool for enabling
literature studies in software engineering: An experience-based guideline. Empir. domain annotations. In: Proceedings of the Workshop on AOP and Meta-Data
Softw. Eng. 22 (6), 2852–2891. http://dx.doi.org/10.1007/s10664-016-9492-y. for Software Evolution. ACM, Genova Italy, pp. 1–4. http://dx.doi.org/10.1145/
Landre, E., Wesenberg, H., Olmheim, J., 2007. Agile enterprise software development 1562860.1562867.
using domain-driven design and test first. In: Companion to the 22nd ACM SIGPLAN Petersen, K., Feldt, R., Mujtaba, S., Mattsson, M., 2008. Systematic mapping studies in
Conference on Object-Oriented Programming Systems and Applications Companion. software engineering. In: 12th International Conference on Evaluation and Assess-
ACM, Montreal Quebec Canada, pp. 983–993. http://dx.doi.org/10.1145/1297846. ment in Software Engineering. EASE, http://dx.doi.org/10.14236/ewic/EASE2008.
1297967. 8.
Landre, E., Wesenberg, H., Rønneberg, H., 2006. Architectural improvement by Petersen, K., Vakkalanka, S., Kuzniarz, L., 2015. Guidelines for conducting systematic
use of strategic level domain-driven design. In: Companion To the 21st ACM mapping studies in software engineering: An update. Inf. Softw. Technol. 64, 1–18.
SIGPLAN Symposium on Object-Oriented Programming Systems, Languages, and http://dx.doi.org/10.1016/j.infsof.2015.03.007.
Applications. ACM, Portland Oregon USA, pp. 809–814. http://dx.doi.org/10.1145/ Popay, J., Roberts, H., Sowden, A., Petticrew, M., Arai, L., Rodgers, M., Britten, N.,
1176617.1176728. Roen, K., Duffy, S., 2006. Guidance on the Conduct of Narrative Synthesis in
Le, D.M., Dang, D.-H., Nguyen, V.-H., 2016. Domain-driven design patterns: A metadata- Systematic Reviews: A Product from the ESRC Methods Programme. Lancaster
based approach. In: 2016 IEEE RIVF International Conference on Computing & University, http://dx.doi.org/10.13140/2.1.1018.4643.
Communication Technologies, Research, Innovation, and Vision for the Future. Singjai, A., Zdun, U., Zimmermann, O., 2021a. Practitioner views on the interrelation
RIVF, IEEE, Hanoi, pp. 247–252. http://dx.doi.org/10.1109/RIVF.2016.7800302. of microservice APIs and domain-driven design: a grey literature study based
Le, D.M., Dang, D.-H., Nguyen, V.-H., 2018. On domain driven design using annotation- on grounded theory. In: 2021 IEEE 18th International Conference on Software
based domain specific language. Comput. Lang. Syst. Struct. 54, 199–235. http: Architecture. ICSA, IEEE, Stuttgart, Germany, pp. 25–35. http://dx.doi.org/10.
//dx.doi.org/10.1016/j.cl.2018.05.001. 1109/ICSA51549.2021.00011.
Le, D.M., Dang, D.-H., Vu, H.T., 2019. JDomainApp: A module-based domain-driven Singjai, A., Zdun, U., Zimmermann, O., Pautasso, C., 2021b. Patterns on deriving APIs
software framework. In: Proceedings of the Tenth International Symposium on and their endpoints from domain models. In: 26th European Conference on Pattern
Information and Communication Technology - SoICT 2019. ACM Press, Hanoi, Ha Languages of Programs. ACM, Graz Austria, pp. 1–15. http://dx.doi.org/10.1145/
Long Bay, Viet Nam, pp. 399–406. http://dx.doi.org/10.1145/3368926.3369657. 3489449.3489976.
Le, D.M., Nguyen, A.P., Tran, L.Q., Le, H.T., Tong, H.V.-A., 2022. Generating multi- Snoeck, M., Wautelet, Y., 2022. Agile MERODE: A model-driven software engineering
platform single page applications: A hierarchical domain-driven design approach. method for user-centric and value-based development. Softw. Syst. Model. 21 (4),
In: The 11th International Symposium on Information and Communication Tech- 1469–1494. http://dx.doi.org/10.1007/s10270-022-01015-y.
nology. ACM, Hanoi Vietnam, pp. 344–351. http://dx.doi.org/10.1145/3568562. Stol, K.-J., Fitzgerald, B., 2018. The ABC of software engineering research. ACM Trans.
3568566. Softw. Eng. Methodol. (TOSEM) 27 (3), 1–51.
Lewis, J., Fowler, M., 2014. Microservices: A definition of this new architectural term. Torres, W., Van Den Brand, M.G.J., Serebrenik, A., 2021. A systematic literature review
MartinFowler.com 25 (14–26), 12. of cross-domain model consistency checking by model management tools. Softw.
Lübke, D., Zimmermann, O., Pautasso, C., Zdun, U., Stocker, M., 2019. Interface Syst. Model. 20 (3), 897–916. http://dx.doi.org/10.1007/s10270-020-00834-1.
evolution patterns: Balancing compatibility and extensibility across service life Uludağ, Ö., Hauder, M., Kleehaus, M., Schimpfle, C., Matthes, F., 2018. Support-
cycles. In: Proceedings of the 24th European Conference on Pattern Languages of ing large-scale agile development with domain-driven design. In: Garbajosa, J.,
Programs. In: EuroPLop ’19, Association for Computing Machinery, New York, NY, Wang, X., Aguiar, A. (Eds.), Agile Processes in Software Engineering and Extreme
USA, http://dx.doi.org/10.1145/3361149.3361164. Programming. vol. 314, Springer International Publishing, Cham, pp. 232–247.
Maddodi, G., Jansen, S., Overeem, M., 2020. Aggregate architecture simulation in http://dx.doi.org/10.1007/978-3-319-91602-6_16.
event-sourcing applications using layered queuing networks. In: Proceedings of the Vernon, V., 2013. Implementing Domain-Driven Design. Addision-Wesley, Upper Saddle
ACM/SPEC International Conference on Performance Engineering. ACM, Edmonton River, NJ.
AB Canada, pp. 238–245. http://dx.doi.org/10.1145/3358960.3375797. Vernon, V., 2016. Domain-Driven Design Distilled. Addison-Wesley, Boston.
Mayer, B., Weinreich, R., 2018. An approach to extract the architecture of microservice- Viggiato, M., Terra, R., Rocha, H., Valente, M.T., Figueiredo, E., 2018. Microservices
based software systems. In: 2018 IEEE Symposium on Service-Oriented System in practice: A survey study. http://dx.doi.org/10.48550/ARXIV.1808.04836.
Engineering. SOSE, IEEE, Bamberg, pp. 21–30. http://dx.doi.org/10.1109/SOSE. Voinov, A., Bousquet, F., 2010. Modeling with stakeholders. Environ. Model. Softw. 25
2018.00012. (11), 1268–1281.
Nilsson, J., 2006. Applying Domain-Driven Design and Patterns: With Examples in C# Vural, H., Koyuncu, M., 2021. Does domain-driven design lead to finding the optimal
and NET. Addison-Wesley, Upper Saddle River, NJ. modularity of a microservice? IEEE Access 9, 32721–32733. http://dx.doi.org/10.
Ochoa, L., Hammad, M., Giray, G., Babur, Ö., Bennin, K., 2025. Characterising harmful 1109/ACCESS.2021.3060895.
API uses and repair techniques: Insights from a systematic review. Comput. Sci. Wanderley, F., Da Silveria, D.S., 2012. A framework to diminish the gap between
Rev. 57, 100732. the business specialist and the software designer. In: 2012 Eighth International
Oukes, P., Andel, M.V., Folmer, E., Bennett, R., Lemmen, C., 2021. Domain-driven Conference on the Quality of Information and Communications Technology. IEEE,
design applied to land administration system development: Lessons from the Lisbon, TBD, Portugal, pp. 199–204. http://dx.doi.org/10.1109/QUATIC.2012.9.
Netherlands. Land Use Policy 104, 105379. http://dx.doi.org/10.1016/j.landusepol. Wang, S., Huang, L., Gao, A., Ge, J., Zhang, T., Feng, H., Satyarth, I., Li, M.,
2021.105379. Zhang, H., Ng, V., 2023. Machine/deep learning for software engineering: A
Özkan, O., Babur, Ö., Van Den Brand, M., 2023. Refactoring with domain-driven design systematic literature review. IEEE Trans. Softw. Eng. 49 (3), 1188–1231. http:
in an industrial context: an action research report. Empir. Softw. Eng. 28 (4), 94. //dx.doi.org/10.1109/TSE.2022.3173346.
http://dx.doi.org/10.1007/s10664-023-10310-1. Wang, Y., Li, S., Liu, H., Zhang, H., Pan, B., 2022. A reference architecture for
Peng, S., Hu, Y., 2007. Ianticorruption: A domain-driven design approach to blockchain-based traceability systems using domain-driven design and microser-
more robust integration. In: Companion To the 22nd ACM SIGPLAN Confer- vices. In: 2022 29th Asia-Pacific Software Engineering Conference. APSEC, IEEE,
ence on Object-Oriented Programming Systems and Applications Companion. Japan, pp. 269–278. http://dx.doi.org/10.1109/APSEC57359.2022.00039.
ACM, Montreal Quebec Canada, pp. 976–982. http://dx.doi.org/10.1145/1297846. Wohlin, C., 2014. Guidelines for snowballing in systematic literature studies and
1297966. a replication in software engineering. In: Proceedings of the 18th International
Pereira, P., Silva, A.R., 2022. Towards transactional causal consistent microservices Conference on Evaluation and Assessment in Software Engineering. ACM, London
business logic. arXiv:2212.11658. England United Kingdom, pp. 1–10. http://dx.doi.org/10.1145/2601248.2601268.
Zhao, J., Zhao, K., 2021. Applying microservice refactoring to object-2riented legacy
system. In: 2021 8th International Conference on Dependable Systems and their
Applications. DSA, IEEE, Yinchuan, China, pp. 467–473. http://dx.doi.org/10.1109/
DSA52907.2021.00070.
21
