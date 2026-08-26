---
otero_id: 13054
otero_key: "6FH52RGP"
title: "Building ontology based knowledge maps to assist business process re-engineering"
authors: "Lila Rao; Gunjan Mansingh; Kweku-Muata Osei-Bryson"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.10.014"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Building ontology based knowledge maps to assist business process re-engineering

Lila Rao <sup>a</sup>, Gunjan Mansingh <sup>b,</sup>⁎, Kweku-Muata Osei-Bryson

<sup>a</sup> Mona School of Business, The University of West Indies, Mona Campus, Kingston, Jamaica

<sup>b</sup> Department of Computing, The University of West Indies, Mona Campus, Kingston, Jamaica

<sup>c</sup> School of Business, Virginia Commonwealth University, Richmond, VA, USA

## a r t i c l e i n f o

Article history: Received1 December 2010 Received in revised form 19 September 2011 Accepted 11 October 2011 Available online 18 October 2011

Keywords: Business process reengineering Ontology Knowledge maps Knowledge management

## a b s t r a c t

Business Process Re-engineering (BPR) is being used to improve the ef<sup>fi</sup>ciency of the organizational processes, however, a number of obstacles have prevented its full potential from being realised. One of these obstacles is caused by an emphasis on the business process itself at the exclusion of considering other important knowledge of the organization. Another is due to the lack of tools for identifying the cause of the inef<sup>fi</sup>ciencies and inconsistencies in BPR. In this paper we propose a methodology for BPR that overcomes these two obstacles through the use of a formal organizational ontology and knowledge structure and source maps. These knowledge maps are represented formally to facilitate an inferencing mechanism which helps to automatically identify the causes of the inef<sup>fi</sup>ciencies and inconsistencies. We demonstrate the applicability of this methodology through the use of a case study of a university domain.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Business process re-engineering (BPR) has been de<sup>fi</sup>ned as the fundamental rethinking and radical design of business processes to achieve dramatic improvements in critical, contemporary measures of performance such as cost, quality, service, and speed [18]. Although there were high expectations for the improvements in performance that BPR would bring about for organizations, in many cases these bene<sup>fi</sup>ts were not realised and high failure rates (e.g. 70%) have been reported [2, 5, 27].

The reasons for these high failure rates have been debated and a number of factors have been posited as to why these expected bene-<sup>fi</sup>ts have not been realised. One factor is the focus on the steps in the business process (e.g. business process diagrams) at the exclusion of the environment within which the process is carried out [42]. In considering the environment organizations will be faced with the challenge of making certain types of knowledge visible to relevant stakeholders. Another factor is that although there are a number of tools for modelling the business processes, many of these tools only support diagrammatic and mathematical modelling [39]. While these models are useful for understanding the business processes, they do not support the automated analysis for identifying the cause of inef<sup>fi</sup>ciencies in the business process, which is considered to be one of the most time consuming stages of BPR [1, 39].

This research addresses the issues of the lack of understanding of the environment within which the business process exists and of automating the identi<sup>fi</sup>cation of the inef<sup>fi</sup>ciencies and inconsistencies in the business process. The lack of understanding of the environment suggests the need for the integration of knowledge management models and techniques [3]. One such knowledge management technique that could be relevant is knowledge mapping, as knowledge maps can be used for several purposes, including <sup>fi</sup>nding sources of knowledge or opportunities for knowledge creation, identifying expertise and increasing knowledge-sharing, and helping to determine the knowledge competencies that exist within an organization [9, 37] and how they interact. The lack of automated methods can be addressed by representing the business processes and the environment using a formal notation. Alleviating these problems will improve the BPR efforts and ultimately help organizations realise the bene<sup>fi</sup>ts that have been anticipated.

In this paper we use a design science approach [19] to develop a methodology that incorporates a number of existing techniques, namely ontologies and knowledge maps, to ensure that both the process and its environment are modelled when re-engineering is being undertaken by an organization. The methodology also proposes an automated mechanism for analysing these domain models by using a formally represented ontology which facilitates automated inferencing. The applicability of the methodology will be demonstrated by applying it to a university domain.

The following section describes the BPR, ontology and knowledge literature. The methodology is then described and evaluated using a case study. The applicability of the methodology for this domain is then discussed and <sup>fi</sup>nally the conclusion and suggestions for future directions for this research are presented.

## 2. Background Research

## 2.1. Business process re-engineering

There are a number of de<sup>fi</sup>nitions of Business Process Re-engineering (BPR) that differ somewhat in their focus [27]. It has been de<sup>fi</sup>ned as a process that involves analysing and designing work<sup>fl</sup>ows and processes within and between organizations [7]. It is also de<sup>fi</sup>ned as fundamental rethinking and radical design of business processes to achieve dramatic improvements in critical, contemporary measures of performance such as cost, quality, service, and speed [18]. The critical components of BPR are fundamental rethinking and redesign of operating processes and organizational structure, with an objective to achieve dramatic improvements in organizational performance [22].

The steps that have been associated with BPR include, de<sup>fi</sup>ning a vision and mission to prepare for BPR, mapping and analysing the current processes (i.e. the AS-IS process), identifying improvement opportunity and designing new processes (i.e. the TO-BE processes) and implementing reengineering processes [24, 25]. Mapping and analysing AS-IS processes and designing TO-BE processes requires a careful analysis of the process under consideration. Several techniques have been used for modelling these business processes to improve their understanding [1, 40, 41].

A number of techniques exist for modelling the business processes [1, 39, 40]. These techniques include Business Process Modelling language (BPML), Petri-nets, Uni<sup>fi</sup>ed Modelling Language (UML), <sup>fl</sup>owcharts. Vergidis et al. [39] classify these techniques according to their analysis and optimization capabilities (i.e. diagrammatical, mathematical and business process languages). They emphasise that although there is an abundance of techniques for modelling there is a lack of those that are suitable for analysis and optimization.

The risks associated with BPR are high and failure rates as high as 70% have been reported [15, 20]. This lack of success has been attributed to the lack of tools and methods for managing change while others have attributed it to a lack of connection between BPR efforts and the corporate goals [4]. According to Attaran [4] many organizations who reengineer focus on the process design and ignore the importance of the people and how their tasks would be affected by these changes. Yu & Mylopoulos [42] emphasise that business processes exist in a social organizational setting, where organizations are made up of actors who perform certain roles to achieve their goals through a network of relationships. Hence it is important to know not only the ‘what’ in the organization (i.e. what entities exist, what activities occur and what relationships hold) but also the ‘why’. This can be achieved if the organizational knowledge is taken into consideration.

## 2.2. Organizational knowledge

A knowledge perspective represents the different types of knowledge within an organization, for example, Know-Why, Know-What, Know-How and Know-Who. Knowing is de<sup>fi</sup>ned as how knowledge works in a business system and is important in understanding how knowledge is used in the processes [3, 8, 30, 36]. The emphasis of this knowledge perspective is not just on processes but on system wide knowledge. Know-What is the knowledge about the facts in the domain and also the knowledge of what to do. This is embedded in the process instances (i.e. practices) of an organization. Know-How is the knowledge that is inherent in the chains of causality between processes. Know-Why is related to how goals interact with each other and thus focuses on knowing why certain things are done rather than how they are done. Know-Who is the knowledge about who knows what and is embedded in the interactions among actors and roles and social networks. Know-Where is related to the location of assets in the organization. Having access to all these types of knowledge will help strategic decision makers to examine not only the business process but also the environment within which it exists. Hence, it is important that this knowledge can be modelled so it can be easily accessed during BPR.

A knowledge map is a knowledge representation technique that reveals the underlying relationships of the knowledge sources using a map metaphor for visualization [28]. Eppler [8] categorized different types of knowledge maps; knowledge source maps, knowledge asset maps, knowledge structure maps, knowledge application maps and knowledge development maps. The knowledge maps provide views to different types of knowledge. For example, knowledge structure maps de<sup>fi</sup>ne the different roles which come together to perform a set of tasks so can be used to identify the know-what and know-how. Eppler [8] summarized the different types of knowledge maps and aspects of organizational knowledge they represent.

## 2.3. Organizational modelling

Several organizational modelling techniques exist, for example, AALADIN, Agent/Group/Role (AGR), MOISE+, Agile Integration Modeling Language (AIML), Enterprise Ontology, each of which focuses on a speci<sup>fi</sup>c aspect of an organization. AALADIN and AGR focus on modelling the structural aspect of the organization (e.g. groups, roles and agents) [10, 11]. MOISE+focuses on the functional aspect of the organization (e.g. goals, plans and mission) [17]. AIML focuses on goals, roles, agents, tasks and interactions [21, 43]. An enterprise ontology considers an enterprise model to be a computational representation of processes, information, resources, people, behaviour, goals and constraints [12] and therefore can be considered to be an encapsulation of the other modelling techniques.

Ontologies provide a framework for facilitating effective and ef<sup>fi</sup>- cient knowledge-sharing by formally modelling the domain of discourse [16]. An organizational ontology provides a set of terms and constraints that describe the structure and behaviour of the organization [13, 43]. They have been used for modelling the enterprises activities, processes, information, resources, behaviour, goals and constraints [12].

Noy and McGuinness [26] highlight several bene<sup>fi</sup>ts of developing an ontology to make domain assumptions explicit, these include: (1) facilitating the sharing of a common understanding of the structure of information among stakeholders in a domain (2) facilitating more effective communication and idea-sharing (3) assisting new entrants in a <sup>fi</sup>eld to quickly assimilate important domain concepts and knowledge and (4) generally supporting the analysis of domain knowledge.

Some of the bene<sup>fi</sup>ts of using ontologies for BPR have been recognised [6, 14]. Galatescu and Greceanu [14] speak to the importance of ontologies for a common vocabulary and understanding and the use of the formal notation for inferencing. Cottam et al. [6] describe how knowledge acquisition techniques and ontologies support the acquisition and organization of process knowledge during BPR.

There are a number of existing tools that support the development of formal ontologies, one such tool is Protégé-OWL, a suite of tools to construct domain models and knowledge-based applications with ontologies (http://protege.stanford.edu/). OWL is the most recent development in standard ontology languages, endorsed by the World Wide Web Consortium (W3C) to promote the Semantic Web vision. The OWL ontology may include descriptions of classes, properties and their instances. Given such an ontology, the OWL formal semantics speci<sup>fi</sup>es how to derive its logical consequences (i.e. facts not literally present in the ontology, but entailed by the semantics). Thus, the OWL language facilitates:

i. formalizing a domain by de<sup>fi</sup>ning classes and properties of the classes

ii. de<sup>fi</sup>ning individuals and asserting properties about them

iii. reasoning about the classes and individuals to the degree permitted by the formal semantics of the OWL language.

We will use the ontology driven method of building knowledge maps proposed by Mansingh et al., [23]. The various knowledge maps are created by extracting speci<sup>fi</sup>c types of knowledge items from the ontology and process diagrams (see Fig. 1).

## 3. Methodology for BPR using ontologies

There is a view that a holistic approach is required for successful BPR [4, 33, 38]. This approach requires not just drastically changing the business process but it also requires an extensive analysis of the environment around it. Therefore, access to organizational knowledge is imperative if the full potential of BPR is to be realised. The BPR methodology proposed in this paper incorporates a number of existing modelling techniques (e.g. organizational ontologies, knowledge maps, BPDs) and therefore can be used to improve the BPR process.

The methodology involves the following steps; the details for each of these steps are described in the sections below:

Step 1: Adopt/Develop a high quality formal organizational ontology

Step 2: Use the ontology to facilitate the identi<sup>fi</sup>cation and prioritization of the business processes that need to be re-engineered

Step 3: Create the knowledge source map and the knowledge structure map from the ontology

Step 4: Analyze the maps to assist in identifying the causes of the inef<sup>fi</sup>ciencies in the process

Step 5: Modify the business process(es) and/or the environment Step 6: Update the organizational ontology and process models to re<sup>fl</sup>ect these changes

The <sup>fi</sup>rst step of the methodology involves adopting/developing and instantiating an organizational ontology. The ontology represents the organizational knowledge which provides the means to understand the relationships between organizational goals, sub-goals, business processes, tasks, subtasks, resources and decision makers (e.g. groups, actors). It helps to identify the business processes and the tasks and subtasks required to carry out each of these processes. It can also be used to identify which roles and/or groups are carrying out particular subtasks and the resources that are being produced and consumed during the execution of these subtasks. One important resource that must be considered is knowledge, the ontology shows the knowledge each actor possesses and also the knowledge decision makers should possess. This helps to determine if there is a mis-match between the knowledge needed for a subtask and the knowledge allocated to the subtask (i.e. the actors assigned to a task) [4].

![](/api/attachments/6FH52RGP/fulltext/images/2429393355e5409d621d9bf7c201a31a3d28426d0a0a4ecb92786e3de3c81bc1.jpg)  
Fig. 1. Building knowledge maps.

This organizational ontology is then represented using a formal notation (e.g. Protégé-OWL). This will provide a common understanding of the structure of information involved in the re-engineering process which in turn facilitates more effective communication and ideasharing as all stakeholders will be using the same information as a common reference point. Additionally, Protégé-OWL will support the analysis of the domain knowledge. Protégé-OWL ontologies can be built for the semantic web and this facilitates the sharing of these organizational ontologies, an important consideration especially for smaller organizations that may not have the resources to undergo business process re-engineering on their own.

The second step involves identifying and prioritizing the business processes to be re-engineered. This is important as it is unlikely that the organization has the resources to address all processes at once and therefore prioritization and resource allocation becomes important. This prioritization process can be improved if the organizational goal the process is achieving is known. This information is available from an organizational ontology and therefore the prioritization of the business process will be derived based on the priority of the organizational goal to which it is linked. Prioritizing is a subjective decision and therefore Analytic Hierarchical Processing (AHP) is used [34]. AHP is a technique for subjective estimation that quanti<sup>fi</sup>es managerial judgments of the relative importance of each of several con<sup>fl</sup>icting criteria used in a decision making process.

The third step involves developing the knowledge maps (i.e. knowledge source and structure maps) from the ontology [23]. The knowledge source map represents the knowledge that the roles require as well as the knowledge that speci<sup>fi</sup>c actors possess. The knowledge structure map represents the sequencing of subtasks, the decision makers (i.e. roles/groups) involved, their interactions with each other and the resources consumed/produced in carrying out a subtask. These maps represent knowledge of the environment that should be considered in the re-engineering process.

The knowledge maps can then be automatically analyzed to identify the causes of the inef<sup>fi</sup>ciencies and inconsistencies as opposed to manually analysing static diagrammatic models (e.g. BPD) [39]. This can be done as the knowledge maps are a view of the formal ontology. Formal notations are supported by an inferencing mechanism which allows for automated reasoning.

Once the sources of the inef<sup>fi</sup>ciencies have been identi<sup>fi</sup>ed and addressed, the models (i.e. organizational ontology, BPD) must then be updated to re<sup>fl</sup>ect these changes. This will ensure that the models are always re<sup>fl</sup>ective of the organization as it exists.

## 3.1. Step 1: Adopting/developing a high quality organizational ontology

An existing organizational ontology can be adapted if it is appropriate, if not, one can be developed using an existing methodology [32]. The ontology represents the relationships between organizational goals, business processes, tasks, subtasks, resources and decision makers (i.e. groups, actors). The organizational ontology below was adapted from a previous study that describes an approach to the development, representation and evaluation of formal ontologies (see Fig. 2) [32]. This multi-step approach includes the development of a complete organizational ontology by synthesizing existing ones [12, 35] and the conversion of this ontology into a formal notation (e.g. Protégé-OWL).

![](/api/attachments/6FH52RGP/fulltext/images/5784ef4e62846e0a9ad7a7ffe9a96a3e538d65475a0c716de737ff98cba4284d.jpg)  
Fig. 2. Organizational ontology.

Fig. 3 represents a part of the formal organizational ontology in Protégé-OWL: entities of the domain, the hierarchical structure of these entities (e.g. groups and roles are decision makers; actors, data/information and knowledge are resources), the relationships between these entities (e.g. organizational goals are decomposed into sub-goals, sub-goals are achieved through the business processes and these business processes are made up of tasks which are performed by decision makers).

It should be noted that the organizational ontology proposed in Fig. 2 and implemented in Protégé is not domain speci<sup>fi</sup>c and so can be applied to many types of organizations. It could be considered to be a minimal initial ontological structure that could be extended by a particular organization if necessary. For many organizations it may be adequate, so the major task would be to populate (instantiate) the ontology with details from the given organization.

To instantiate the ontology all the instances will have to be identi-<sup>fi</sup>ed, for example, the particular resources, decision makers, organizational goals and business processes. This information is usually dispersed throughout the organization in various forms (e.g. existing organizational charts, database diagrams. business process & work<sup>fl</sup>ow documentation, people, etc.) and can be acquired by interviewing the stakeholders and reviewing existing documentation.

## 3.2. Step 2: identifying and prioritising the processes for re-engineering

An organization decides to engage in BPR because it is seeking to improve it's ef<sup>fi</sup>ciency. Therefore it must identify the processes that are deemed to be inef<sup>fi</sup>cient. This can be done by interviewing and surveying various stakeholders (e.g. employees, customers). These stakeholders can be identi<sup>fi</sup>ed by querying the ontology for the decision makers and then traversing the ontology to <sup>fi</sup>nd the particular actors playing these decision makers (i.e. see Fig. 2). Once the persons are identi<sup>fi</sup>ed, they can be interviewed about the subtasks, tasks or business process they are performing (depending on their role) and the problems they are having (if any) in performing them. For those tasks and subtasks that are identi<sup>fi</sup>ed as being problematic the business processes they are associated with are identi<sup>fi</sup>ed using the ontology. This will result in the set of business processes the organization should focus on during the re-engineering process.

These problematic business processes then need to be prioritized so that the limited BPR resources can be allocated appropriately. The prioritization process will be more informed if the decision maker is clear which subgoals and organizational goals each business process is ful<sup>fi</sup>lling. This information can be extracted by querying or traversing the organizational ontology. A set of mappings from business process to organizational subgoals to organizational goals will be generated.

![](/api/attachments/6FH52RGP/fulltext/images/4a823d55a97e497e3a263c2a825bd46ec05e7445c236a47c756fff9956f213d7.jpg)  
Fig. 3. Implementation of organizational ontology using Protege-OWL.

Table 1  
illustration of the prioritization of business processes.

<table><tr><td>Business Process</td><td>Subgoal</td><td>Organizational Goal</td><td>Weight of Subgoal</td><td>Weight of Organizational Goal</td><td>Business Process Weight</td></tr><tr><td>BP1</td><td>O1-S1</td><td>O1</td><td>0.4</td><td>0.6</td><td>0.6*0.4 = .24</td></tr><tr><td>BP2</td><td>O1-S2</td><td>O1</td><td>0.6</td><td></td><td>0.6*0.6 = .36</td></tr><tr><td>BP3</td><td>O2-S1</td><td>O2</td><td>0.7</td><td>0.4</td><td>0.4*0.7 = .21</td></tr><tr><td>BP4</td><td>O2_S2</td><td>O2</td><td>0.3</td><td></td><td>0.4*0.3 = .12</td></tr></table>

These mappings will then be used to assign some level of priority to the business processes using a subjective prioritization technique such as Analytic Hierarchy Process (AHP) [29]. AHP helps the decision maker to prioritize alternatives so that the best one can be selected (Table 1 will be used to illustrate this). The decision maker will <sup>fi</sup>rst implicitly assign a weight to each of the organizational goals in the set using the pairwise comparisons and weight vector generation facilities of the AHP (e.g. in Table 1 organizational goal O1 is assigned a weight of 0.6). Next the decision makers will similarly use the AHP implicitly assign a weight to each organizational subgoal (e.g. in Table 1 organizational subgoal O1-S1 of organizational goal O1 is assigned a weight of 0.4). These individual weights will be combined to derive an overall weight for each business process (e.g. in Table 1 business process 1 has an overall weight of 0.24).

Resources can then be allocated based on these weightings. From Table 1 it can be seen that the second business process is the most important followed by businesses process 1, 3 and 4. These weights also re<sup>fl</sup>ect the relative importance of these business processes and this information can be bene<sup>fi</sup>cial in the resource allocation as it may not be that only the top process is selected for re-engineering but rather the top few and then the resource allocation would depend on the weights assigned to each.

## 3.3. Step 3: creating knowledge maps

Knowledge maps provide different views of an instance of the ontology for the particular business processes being addressed. The development of knowledge maps may require information from the instantiated ontology and any existing diagrammatic representation of the business process (e.g. BPD).

The knowledge structure map represents the sequencing of tasks and subtasks, the decision makers (i.e. roles/groups) involved and the interactions between them, the resources consumed/produced in carrying out a task and their location (see Fig. 4).

The ontology will be used to identify the know-what and knowwhere required to build the knowledge structure map for the business process identi<sup>fi</sup>ed in Step 2 (see Section 3.2). The know-what includes the tasks, subtasks, roles, groups, interactions and resources. The know-where includes the resources and their locations. The knowhow can be identi<sup>fi</sup>ed through the sequencing of the tasks and subtasks. The know-how can be identi<sup>fi</sup>ed by accessing the relevant current graphical model of the business process (e.g. BPD) if one exists or by interviewing the actors who have been identi<sup>fi</sup>ed as playing a role in that particular business process.

The knowledge source map represents the ‘know- what’ and the ‘know-who’ (i.e. in doing a task what knowledge is to be applied to do the task and by whom). This includes the knowledge that the role requires, the knowledge that speci<sup>fi</sup>c actors possess and the roles actors are playing. The formal ontology will be queried to extract the instantiation of the Decision Maker, Actor, Requires, Possesses and Play.

These knowledge maps provide the details of the environment within which the business process exists and therefore can help to identify the causes of the inef<sup>fi</sup>ciencies and how changing the process can affect the environment (i.e. who and what will be affected by the change).

## 3.4. Step 4: analyze knowledge maps

The knowledge maps provide a useful tool for identifying some of the possible causes of inef<sup>fi</sup>ciencies in business processes. The knowledge structure map can be used to identify inconsistencies in the know-what, know-where and know-how. Know-how includes the sequencing of subtasks and tasks, the know-what includes the roles and resources that are needed for sub-tasks and the know-where includes the location of the various resources. The knowledge source map can be used to identify inconsistencies in the know-what and know-who. The know-who includes the actors and the roles they play and know-what includes the knowledge that the decision makers possess and the knowledge that they require.

Given that the knowledge maps are a subset of a formal ontology then the inferencing mechanism of the ontology can be invoked to identify certain inconsistencies in the knowledge maps. A number of types of inconsistencies will be detected:

Cardinality violations — the violation of the cardinality of relationships can cause inef<sup>fi</sup>ciencies in business processes.

Domain Rule Violations – a knowledge base consisting of a set of domain rules will be developed with the help of the business process expert. These rules specify the conditions that must hold between the relationships and entities a speci<sup>fi</sup>c knowledge map represents and the actions to be taken if the conditions are matched. For example, for the knowledge source map a rule should be speci<sup>fi</sup>ed to ensure that there is no mismatch between the knowledge that the decision makers possess and the knowledge that they require to perform the roles they are assigned and if this is violated the action would require retraining or reassigning these actors.

![](/api/attachments/6FH52RGP/fulltext/images/60a8f1856e67882cbaf0c4d7b0d6349186cef2cdd6c74f8bdab723d5fe20edba.jpg)  
Fig. 4. Knowledge structure map.

## 3.5. Step 5: update the business process(es)

The list of inconsistencies identi<sup>fi</sup>ed in Step 4 (see Section 3.4) will be evaluated by the BPR team to determine how the process or the environment should be changed to address these inef<sup>fi</sup>ciencies. The solutions may vary from restructuring the business processes to adopting information systems to retraining employees. In cases where the inconsistency is caused by a violation of a domain rule the antecedent (i.e. Action) of the matched domain rule will provide a recommendation for addressing the inconsistency. For example, in the case of a mismatch of knowledge between actors and the roles they are playing, the recommendation may be for them to get training to gain the knowledge they are lacking.

## 3.6. Step 6: update ontology to reflect changes

Once the process and/or environment has been re-engineered the changes must be re<sup>fl</sup>ected in the ontology. It is essential that the quality of the ontology remains high so that the ontology remains accurate, complete and consistent [31]. The reasons for these changes must be recorded so that the ontology is traceable [31].

Example instantiations for entities and relationships in University domain.

<table><tr><td>Concept</td><td>Type</td><td>Example Instantiations</td></tr><tr><td>Organizational Goal</td><td>Entity</td><td>Prepare a distinctive graduate for the 21st century; Make the university an internationally recognized centre of excellence for graduate education</td></tr><tr><td>Sub-Goal</td><td>Entity</td><td>Emphasize and carry our curriculum review as a reflective and dynamic process; Enhance learning effectiveness by providing students with a more diverse and flexible learning experience; Build a reputation of excellence in the university&#x27;s higher degree programmes; Enhance teaching quality; Improve the flexibility of postgraduate programme delivery and significantly expand the number of postgraduate programmes delivered by distance or blended education.</td></tr><tr><td>Business Process</td><td>Entity</td><td>Development and approval of new programme/course; Adopt and tailor a course management system (CMS)</td></tr><tr><td>Task</td><td>Entity</td><td>Design programme/course; Faculty board approval of programme/course; Academic board approval of programme/course; Board of Undergraduate Studies Approval; Upload programme/course content in the system</td></tr><tr><td>Subtask</td><td>Entity</td><td>Develop aims and objectives for the programme; Determine the structure of the programme; Develop course outlines in template format; Submit document to relevant persons before meeting; Faculty board meeting; Make changes recommended from faculty board; Submit document to relevant persons before meeting; Academic board meeting; Make changes recommended from academic board; Submit document to relevant persons before meeting; Board of graduate/postgraduate studies meeting; Make changes recommended from board of graduate/postgraduate studies; Notify students records of start of programme; Acquire programme/course details; Upload details to information system</td></tr><tr><td>Resource</td><td>Entity</td><td></td></tr><tr><td>Actor</td><td>Entity</td><td>John Brown; Chandra Mbeki</td></tr><tr><td>Data/Information</td><td>Entity</td><td>Approved programme/course details; Minutes; Template; Operational registration data; Course information</td></tr><tr><td>Knowledge</td><td>Entity</td><td>Business; Existing systems; Quality expectations within a faculty; Quality expectations within the university; Technical; University IT architecture; University registration process</td></tr><tr><td>Decision Maker</td><td>Entity</td><td></td></tr><tr><td>Group</td><td>Entity</td><td>Faculty Board; Academic Board; Board of Undergraduate Studies; Student Records Unit; Technical Services (TS)</td></tr><tr><td>Role</td><td>Entity</td><td>Lecturer; Head of Department; CIO; TS IT-Officer; SRU IT-Officer</td></tr><tr><td>Decomposed_Into</td><td>Relationship</td><td>Prepare a distinctive graduate for the 21st century: Emphasize and carry our curriculum review as a reflective and dynamic process; Enhance learning effectiveness by providing students with a more diverse and flexible learning experienceMake the university an internationally recognized centre of excellence for graduate education: Enhance teaching quality; Improve the flexibility of postgraduate programme delivery and significantly expand the number of postgraduate programmes delivered by distance or blended education.</td></tr><tr><td>Achieved_by</td><td>Relationship</td><td>Development and approval of new course and programme: Emphasize and carry our curriculum review as a reflective and dynamic processAdopt and tailor a course management system (CMS): Improve the flexibility of postgraduate programme delivery and significantly expand the number of postgraduate programmes delivered by distance or blended education.</td></tr><tr><td>Made_Up_Of</td><td>Relationship</td><td>Development and approval of new course or programme: Design programme/course; Faculty board approval of programme or course; Academic board approval of programme or course; Board of Undergraduate Studies Approval; Upload Program and Course Content in the System</td></tr><tr><td>Divided_Into</td><td>Relationship</td><td>Design programme/course: Develop aims and objectives for the programme, Determine the structure of the programme; Develop course outlines in template format; Faculty board approval of programme/course: Submit document to relevant persons before meeting; Meeting to discuss document; Academic board approval of programme/course: Make changes recommended from faculty board; Submit document to relevant persons; Academic board meeting; Board of graduate/undergraduate studies approval: Make changes recommended from academic board; Submit document to relevant persons before meeting, Meeting to discuss document; Upload programme/course content in the system: Make changes recommended from board of graduate/postgraduate studies; Notify students records of start of programme; Acquire programme/course details; Upload details to information system.</td></tr><tr><td>Performs</td><td>Relationship</td><td>Lecturer, Head of Department: Develop aims and objectives for the programme, Determine the structure of the programme; Develop course outlines in template format; Faculty Board, Head of Department: Attend meeting to defend document</td></tr><tr><td>Consumes</td><td>Relationship</td><td>Faculty board meeting: Quality expectations within a faculty</td></tr><tr><td>Produces</td><td>Relationship</td><td>Faculty board meeting: Minutes</td></tr><tr><td>Plays</td><td>Relationship</td><td>Chandra Mbeki: SRU IT-Officer; John Brown: TS IT-Officer</td></tr><tr><td>Requires</td><td>Relationship</td><td>SRU IT-Officer: University IT Architecture, University Registration processTS IT-Officer: Technical</td></tr><tr><td>Possesses</td><td>Relationship</td><td>Chandra Mbeki: University Registration process; John Brown: Technical</td></tr></table>

## 4. Illustration: case study

A university campus in Jamaica, which has recently been forced to examine how it currently carries out its functions as it is facing severe budget cuts and, at the same time, increased competition, is seeking to become more ef<sup>fi</sup>cient by improving the existing business processes. The proposed methodology was applied to this organization.

## 4.1. Step 1: developing/adopting a high quality organizational ontology

The organizational ontology proposed (Fig. 2) would be applicable to the university domain. It must then be instantiated which requires the identi<sup>fi</sup>cation of the organizational goals, subgoals, business processes, tasks, resources and decision makers as well as the relationships between these instances. Interviews were conducted and relevant documentation (e.g. the university's <sup>fi</sup>ve year strategic plan) was examined to identify this information. Table 2 represents all the concepts in the ontology, classi<sup>fi</sup>es them as either entities or relationships and provides some example instantiations of these (e.g. Chandra Mbeki is an instance of the entity Actor, SRU IT-Officer is an instance of the entity Role, Chandra Mbeki: SRU IT-Officer is an instance of the Plays relationship, Chandra Mbeki: University Registration Process is an instance of the Possesses relationship).

The ontology is then instantiated in Protégé-OWL. This formal representation provides a common reference that can be used by all stakeholders of the university. The ontology can be queried or traversed to <sup>fi</sup>nd all instantiations of the entities and relationships within the organization (see Fig. 5). This <sup>fi</sup>gure shows that the task “Faculty Board Approval of a Programme or Course” produces the data/information resources “minutes”, consumes the knowledge of “Quality Expectations within the Faculty” and the task should involve the decision makers “Faculty Board” and “Head of the Department”.

## 4.2. Step 2: identifying and prioritising the processes for re-engineering

The ontology was consulted to identify some of the key decision makers in the organization. These included an academic director, lecturers, a head of department, IT administrators and students. Particular actors playing these key roles were then identi<sup>fi</sup>ed by querying the ontology and were interviewed to determine problems they were experiencing in carrying out their assigned business processes, tasks or subtasks. Those tasks and subtasks that were deemed to be problematic were mapped to a business process by consulting the ontology. From these discussions it was clear that two of the business processes within the university (i.e. development and approval of a new programme/course and adopting and tailoring a Course Management System (CMS)) were deemed to be problematic. However, the university does not have the resources to address both problems so there was a need to prioritize.

![](/api/attachments/6FH52RGP/fulltext/images/69932bf72ba1d8c2ff7baf2195e4c9eaf5d3bd285ec08eb45e79c85c99ce817a.jpg)  
Fig. 5. Instantiation of University Ontology in Protege-OWL.

For the prioritization, each of the business processes was mapped to their corresponding subgoal and, in turn, organizational goal by querying the ontology. In the case of development and approval of a new programme/course it maps to the organizational goal of preparing the distinctive graduate while adopting and tailoring the CMS maps to the organizational goal of becoming an internationally recognized centre for graduate education (see Figs. 6 and 7).

The two possible organizational goals were then presented to the strategic decision makers to assist in the prioritization process. The weightings of each were combined in AHP to determine the overall importance of each organizational goal (see Table 3).

Based on this information it was decided to focus on the organizational goal of preparing the distinctive graduate and therefore to re-engineer the business process development and approval of new programme/course.

## 4.3. Step 3: creating knowledge maps

The knowledge structure map was developed by querying the ontology to identify the tasks and subtasks associated with the business process development and approval of new programme/course. The tasks included: (i) Design programme/course (ii) Faculty Board approval of programme or course (iii) Academic Board approval of programme or course (iv) Board of Undergraduate Studies approval (v) Upload program and course content in the system. The subtasks of designing the programme/course were: (a) Develop aims and objective for programme/course, (b) Develop structure of programme/course, (c) Develop course outlines. Additionally, the roles/groups, interactions resources and locations were also extracted (e.g. lecturer, head of the department is responsible for designing programmes/courses) from the ontology (see Figs. 8 and 9).

No business process diagram existed, therefore, interviews were conducted with an IT of<sup>fi</sup>cer, a head of department, two lecturers and an academic coordinator to determine the sequencing and details (e.g. decisions) of these tasks. From these interviews it was found that the department <sup>fi</sup>rst de<sup>fi</sup>nes the aims, objectives and structure of the new programme being created. The courses that will meet these objectives are then designed and corresponding course outlines are developed. Each programme/course is then approved at the faculty board level. Any changes recommended by the board are then sent to the department. After the approval by the faculty board the programme/course proposal then goes to a university wide subcommittee which monitors the quality of all programmes/courses offered at the university. Any changes required at this stage are sent back to the department. After this the programme/course proposal is sent to the undergraduate/postgraduate board for of<sup>fi</sup>cial approval. The information about the approved programme is then sent to the Student Records Unit which is responsible for the coordination of registration activities (e.g. putting the new programmes/courses online). The unit will not put the programme online until it receives a memo from the undergraduate/postgraduate board. If this unit requires any further information or clari<sup>fi</sup>cation it interacts with the department or consults the minutes of the university wide meeting. The information above represents the knowledge structure map for the business process development and approval of new programme/course (see Fig. 9).

The knowledge structure map was developed by querying the ontology to identify, for each task, the corresponding groups, roles, actors, knowledge required for a role and the knowledge the actor possesses. Fig. 10 represents the extracted source map for the task of uploading programme/course content.

BPR.owl (http://www.semanticweb.org/ontologies/2010/5/BPR.owl) - [C:Documents and Settings\10011914Wy Documents\Dr. GrahamDesktop\Research\Ontology for BPRI... File Edit Ontologles Reasone- Tools Refactor Tabs View Window Help BPR.ow (ht  
![](/api/attachments/6FH52RGP/fulltext/images/5103fbd24eab0cbad44ec22a03f7801ea6afb6cb6df4eb26a881001f399c3055.jpg)  
Fig. 6. Mapping of business process to organizational goal.

![](/api/attachments/6FH52RGP/fulltext/images/9ddbc34ea0da29203266b8b2a36130f45ada632f8fcb729e4aa355c69fb7ac97.jpg)  
Fig. 7. Mapping of alternate business process to organizational goal.

## 4.4. Step 4: analysis of knowledge maps

The knowledge maps were analyzed to identify inef<sup>fi</sup>ciencies in the process. The knowledge structure map (see Fig. 9) identi<sup>fi</sup>ed all the roles and groups that are involved in the tasks of the approval of new programmes/courses. It also identi<sup>fi</sup>ed all interactions that were occurring between these tasks, the resources being consumed and produced and their location. The knowledge source map (see Fig. 10) shows the knowledge being used to perform tasks and the knowledge required to do the task.

The knowledge structure map developed in Step 3 (see Section 4.3) was used to identify cardinality violations. It was found that 1-M mapping of the stored\_in relationship (i.e. each resource should only be found in one location) was violated. In this case the resource course/programme outline is stored in more than one location (i.e. department, faculty of<sup>fi</sup>ce). This can lead to inconsistencies if various versions of the document exist in a number of locations (e.g. a course code may have different course titles and different list of pre-requisites associated with it in different locations).

A knowledge base of domain rules was developed, one of which identi<sup>fi</sup>ed mismatches between the knowledge required by a role to do a task and the knowledge that actors assigned to the task possess. This condition-action rule would be speci<sup>fi</sup>ed as:

Table 3  
AHP weighting.

<table><tr><td>Organizational Goal</td><td>Overall Weight</td></tr><tr><td>Preparing the distinctive graduate</td><td>0.65</td></tr><tr><td>Internationally recognized centre for graduate education</td><td>0.35</td></tr></table>

## if a particular role requires knowledge

and a particular actor posses knowledge

and the actor plays a role

and the role knowledge is not a subset of the actor knowledge then train the actor to acquire the required knowledge or reallocate actor.

An inferencing mechanism was used with the knowledge maps and domain rules to identify domain violations. It was found that there was a mismatch in this knowledge. The SRU IT-Of<sup>fi</sup>cer should have knowledge of the university IT architecture as well as knowledge of the university registration process. However, Chandra Mbeki, an actor performing the role of SRU IT-Of<sup>fi</sup>cer only has the knowledge of the university registration process and not of the IT architecture and should be trained in this or reallocated. This mismatch of knowledge can lead to delays in uploading programs and course content.

## 4.5. Step 5: modify the business process(es) and/or environment

Given the inef<sup>fi</sup>ciencies identi<sup>fi</sup>ed in Step 4 (see Section 4.4) recommendations were made by the BPR team for improving the process:

i. The problem of multiple locations for a resource could be addressed by having a document management system where the new programme/ course details would be stored from their creation. This would avoid duplication in locations and reduction in inconsistency. It will require that the process includes security and access permissions to ensure that only authorised parties have access to these documents.

![](/api/attachments/6FH52RGP/fulltext/images/0a1a27f260f56d0274e5d6395c782e75c1eceeca3be2db49d5566d8835d5b301.jpg)  
Fig. 8. Tasks, subtasks, roles and groups.

ii. Where it is found that a particular actor (i.e. Chandra Mbeki) does not have the requisite knowledge to perform their role the recommendation to re-train the actor would be made.

## 4.6. Step 6: update the ontology

Once approved, the changes recommended would be re<sup>fl</sup>ected in the instantiation of the ontology. The addition of the document management system would change the instantiation of the Location and Resource entities and the Stored\_in relationship. The change in knowledge through training would change the instantiation of the Possesses relationship (e.g. Chandra Mbeki possess IT architecture knowledge).

## 5. Summary and future work

In this paper we proposed an ontology-driven methodology for business process re-engineering that includes the development and analysis of knowledge maps. It was found that is not enough to simply reengineer by examining only the process but rather organizations must consider the environment within which the process is carried out. The formal representation of the knowledge of the domain also facilitated an automated inferencing mechanism which improves the identi<sup>fi</sup>cation of the causes of inef<sup>fi</sup>ciencies. We demonstrated the applicability of the methodology using a case study of a university.

The success of this methodology depends on the quality of the ontology (e.g. accuracy and completeness) and therefore the instantiation becomes extremely important. Creating and maintaining this instantiation can be a tedious process. The choice of the formal notation will impact the level of automated reasoning that can be achieved and these limitations must be understood.

In this study we applied our methodology to the university domain, however, the steps are not speci<sup>fi</sup>c to a particular organization. Any organization adopting the proposed methodology will be required to instantiate the given ontology. Once instantiated the knowledge maps generated from the ontology will be representative of the knowledge in the new domain. Therefore, this methodology is generalizable, which will be demonstrated by applying it to a number of other domains (e.g. healthcare, crime).

![](/api/attachments/6FH52RGP/fulltext/images/e389045e3e7c471ab5adc8e1594db54a6316a4559b8c4eabb8a4809282a65020.jpg)  
Fig. 9. Knowledge structure map — creating new programs or courses.

![](/api/attachments/6FH52RGP/fulltext/images/a08d932002e6afa522f2cd1240e524549d6837a340f77d22f2c601bc1f96fc88.jpg)  
Fig. 10. Knowledge source map for task upload program/course content.

The methodology proposed is based on an instantiated ontology. The focus in this study was on the business process entity (as BPR was being considered), however, the focus could be on other entities in the ontology which would then bene<sup>fi</sup>t other decision making situations (e.g. disaster recovery planning (DRP) where the focus would be on the resource entity). This will be explored in future work.

## Acknowledgements

This research was supported in part by a grant from the 2011 Summer Research Program of the School of Business at Virginia Commonwealth University.

## References

[1] R.S. Aguilar-Saven, Business Process Modelling: Review and Framework, International Journal of Production Economics 90 (2) (2004) 129–149.

[2] M. Al-Mashari, Z. Irani, M. Zairi, Business Process Reengineering: A Survey of International Experience, Business Process Management 7 (5) (2001) 437–455.

[3] M. Alavi, D.E. Leidner, Review: Knowledge Management and Knowledge Management Systems: Conceptual Foundations and Research Issues, MIS Quarterly 25 (1) (2001) 107–135.

[4] M. Attaran, Exploring the Relationship Between Information Technology and Business Process Reengineering, Information Management 41 (2004) 585–596.

[5] M.-C. Boudreau, D. Robey, Coping with Contradictions in Business Process Re-engineering, Information Technology & People 9 (4) (1996) 40–57.

[6] H. Cottam, N. Shadbolt, N. Milton, Acquiring Knowledge for Business Process Re-engineering, AAAI-98 Workshop on Using AI for Knowledge Management and Business Process Engineering, 1998.

[7] S.H. Davenport, J.E. Short, The New Industrial Engineering: Information Technology and Business Process Redesign, Sloan Management Review (1990) 11–27.

[8] M.J. Eppler, Making knowledge visible through knowledge maps: concepts, elements cases in: CW. Holsapple (Ed.) Handbook on Knowledge Management Springer-Verlag, Berlin, Heidelberg, 2001, pp. 189–205.

[9] M.J. Eppler, A process-based classi<sup>fi</sup>cation of knowledge maps and application examples Knowledge and Process Management 15 (1) (2008) 59–71

[10] J. Ferber, O. Gutknecht, A meta-model for the analysis and design of organizations in multi-agent systems, International Conference on Multi Agent Systems 3 (7) (1998) 128–135.

[11] J. Ferber, O. Gutknecht, F. Michel, From agents to organizations: an organizational view of multi-agent systems, Agent-Oriented Software Engineering IV: 4th InternationalWorkshop, AOSE 2003, 2935, LNCS - Springer, 2003, pp. 214–230.

[12] M.S. Fox, M. Barbuceanu, M. Gruninger, J. Lin, An organisation ontology for enterprise modeling, in: M. Prietula, K. Carley, L. Gasser (Eds.), Simulating Organizations: Computational Models of Institutions and Groups, AAAI/MIT Press, Menlo Park CA, 1998, pp. 131–152.

[13] M.S. Fox, M. Gruninger, Enterprise Modeling, AI Magazine 19 (3) (1998) 109–121.

[14] A. Galatescu, T. Greceanu, Ontologies supporting business process re-engineering, in: M. Paittini, J. Filipe, J. Braz (Eds.), Enterprise Information Systems IV, Kluwer Academic, 2003, pp. 186–193.

[15] D. Grant, A wider view of business process re-engineering, Communications of the ACM 45 (2) (2002) 84–92.

[16] T.R. Gruber, Toward Principles for the Design of Ontologies Used for Knowledge Sharing, International Journal of Human Computer Studies 43 (5–6) (1995) 907–928.

[17] J.F. H¨ubner, J.S. ao Sichman, O. Boissier, MOISE+: Towards a structural, functional, and deontic model for MAS organization, Proceedings of the First International Joint Conference on Autonomous Agents and Multi-Agent Systems (AAMAS'2002), Bologna, Italy, 2002.

[18] M. Hammer, J. Champy, Reengineering the Corporation: A Manifesto for Business Revolution, Nicholas Brealey Publishing, London, U.K., 1993.

[19] A.R. Hevner, S.T. March, J. Park, S. Ram, Design Science in Information Systems Research, MIS Ouarterly 28 (1) (2004) 75–105.

[20] V. Hlupic, J. Choudrie, N. Patel, Business Process Re-engineering: The REBUS Approach, Cognition, Technology & Work 2 (2) (2000) 89–96.

[21] R. Kishore, R. Sharman, R. Ramesh, Computational Ontologies and Information Systems: I. Foundations, Communications of the Association for Information Systems, 14, 2004, pp. 158–183.

[22] J.N. Lowenthal, Reengineering the organization, a step-by-step approach to corporate revitalization: Part 2, Quality Progress 27 (2) (1994) 61–63

[23] G. Mansingh, K.-M. Osei-Bryson, H. Reichgelt, Building Ontology-Based Knowledge Maps to Assist Knowledge Process Outsourcing Decisions, Knowledge Management Research and Practice 7 (2009) 37–51.

[24] R.J. Mayer, P.C. Benjamin, B.E. Caraway, M.K. Painter, A framework and suite of methods for BPR, in: W.J.K.V. Grover (Ed.), Business Process Change - Reengineering, concepts, methods and technologies, IDEA Group Publishing, 1995, pp. 245–290.

[25] S. Muthu, L. Whitman, S.H. Cheraghi, Business Process Reengineering: A consolidated Methodology, The 4th Annual International Conference on Industrial engi neering, Theory, Applications and Practice, San Antonio, Texas, U.S.A, 1999.

[26] N. Noy, D.L. McGuiness, Ontology Development 101: A Guide to Creating your <sup>fi</sup>rst Ontology, Stanford Medical Informatics, Stanford University, Stanford, 2001.

[27] P. O'Neill, A.S. Sohal, Business Process Reengineering: A Review of Recent Literature, Technovation 19 (1999) 571–581.

[28] T.-H. Ong, H. Chen, W.-k. Sung, B. Zhu, Newsmap: A knowledge map for online news, Decision Support Systems 39 (2005) 583–597.

[29] K.-M. Osei-Bryson, O.K. Ngwenyama, Managing risks in information systems outsourcing: An approach to analyzing outsourcing risks and structuring incentive contracts, European Journal of Operational Research 174 (1) (2006) 245–264.

[30] L. Prusak, Where did Knowledge Management come from? IBM Systems Journal 40 (4) (2001) 1002–1007.

[31] L. Rao, K.-M. Osei-Bryson, Towards De<sup>fi</sup>ning Dimensions of Knowledge Systems Quality, Expert Systems with Applications 33 (2) (2007) 368–378.

[32] L. Rao, H. Reichgelt, K.-M. Osei-Bryson, An Approach for Ontology Development and Assessment Using a Quality Framework, Knowledge Management Research and Practice 7 (2009) 260–276.

[33] H.A. Reijers, S.L. Mansar, Best practices in business process redesign: an overview and qualitative evaluation of successful redesign heuristics, Omega.- International Journal of Management Science 33 (2005) 283–306.

[34] T. Saaty, The Analytic Hierarchy Process: Planning, Priority Setting, Resource Allocation, McGraw-Hill New York NY 1980

[35] S. Sharma, K.M. Osei-Bryson, Organization-Ontology Based Framework for Implementing the Business Understanding Phase of Data Mining Projects, 41st Hawaii International Conference on Systems Sciences, Hawaii, U.S.A, 2008.

[36] J. Swart, J.H. Powell, Men and measures: Capturing knowledge requirements in <sup>fi</sup>rms through qualitative system modelling, The Journal of the Operational Research Society 57 (2006) 10–21.

[37] E.F. Vail, Knowledge mapping: getting started with knowledge management, Information Systems Management 16 (1) (1999) 16–23.

[38] G. Valiris, M. Glykas, Critical Review of Existing BPR Methodologies: The Need fo a Holistic Approach, Business Process Management 5 (1) (1999) 65–86.

[39] K. Vergidis, A. Tiwari, B. Majeed, Business Process Analysis and Optimization: Beyond Reengineering, IEEE Transactions on Systems, Man, and Cybernetic Part C: Applications and Reviews 38 (1) (2008) 69–81.

[40] S.A. White, Introduction to BPMN, BPTrends, 2004.

[41] P. Wohed, W.M.P. van der Aalst, M. Dumas, A.H.M. ter Hofstede, N. Russell, On the Suitability of BPMN for Business Process Modelling, Lecture Notes in Computer Science 4102 (2006) 161–176.

[42] E. Yu, J. Mylopoulos, From E-R to A-R – Modelling Strategic Actor Relationships for Business Process Reengineering, International Journal of Intelligent and Coopera tive Information Systems 4 (2 & 3) (1995) 125–144.

[43] H. Zhang, R. Kishore, R. Sharman, R. Ramesh, Agile Integration Modeling Language (AIML): A Conceptual Modeling Grammar for Agile Integrative Business Informa tion Systems, Decision Support Systems 44 (1) (2007) 266–284.

Lila Rao is the Academic Director and a Lecturer at the Mona School of Business at The University of the West Indies. She holds a Ph.D. in Information Systems from The University of the West Indies. She currently does work in various areas including: Ontologies, Data Warehousing, Information and Knowledge Quality, Decision Support Systems and Technology Adoption. She has published in the Journal of Information Systems for Crisis Response and Management, Data and Knowledge Engineering, Expert Systems with Applications and Information Systems Frontiers journal. She also has papers published in the proceedings of FLAIRS Research Symposium, e-business workshop, IRMA, AMCIS and ICEIS.

Gunjan Mansingh is a Lecturer in the Department of Computing at the University of the West Indies (U.W.I.), Jamaica. She holds a Ph.D. in Information Systems from the University of the West Indies, Jamaica. Her research interests are Decision Support Systems, Expert Systems, Data Mining, Knowledge Management, E-Commerce and Technology Adoption. She has published in Information Sciences, Knowledge Management in Research and Practice, Expert Systems with Applications and British Journal of Sports Medicine journal. She also has papers published in the proceedings of IEEE Communications Conference Jamcon, e-business workshop, SIG GlobDev workshop, IRMA, AMCIS and IASTED.

Kweku-Muata Osei-Bryson is Professor of Information Systems at Virginia Commonwealth University, USA. Previously he was Professor of Information Systems & Decision Sciences at Howard University, USA. He holds a Ph.D. in Applied Mathematics (Management Science & Information Systems) from the University of Maryland at College Park. He currently does research in various areas including: Data Mining, Decision Support Systems, Knowledge Management, Project Management, IT & Productivity, IS Outsourcing, e-Commerce, IS Security, Multi-Criteria Decision Analysis. Currently he serves as an Associate Editor of the INFORMS Journal on Computing, and is a member of the Editorial Board of the Computers & Operations Research journal and the International Advisory Board of the Journal of the Operational Research Society.
