---
otero_id: 17759
otero_key: "JG7TWVVD"
title: "Identification of ontologies to reuse knowledge for substation fault recovery support system"
authors: "Yoshiyuki Takaoka; Riichiro Mizoguchi"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(96)00014-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Identification of ontologies to reuse knowledge for substation fault recovery support system

Yoshiyuki Takaoka $^{a,*}$ , Riichiro Mizoguchi $^{b}$

$^{a}$ Control Devices Department, Toko Seiki Company Ltd., 3-14-40 Senrioka, Settsu-shi, Osaka 566, Japan $^{b}$ I.S.I.R., Osaka University, 8-1 Mihogaoka, Ibaraki-shi, Osaka 567, Japan

## Abstract

A methodology to identify task/domain ontologies is proposed in this paper. According to the methodology, task/domain ontologies that are indispensable for building a reusable knowledge base are identified. The expertise model of the methodology has two kinds of ontologies at different abstraction levels. The first one is based on a vocabulary applicable in common to the entire target field. This vocabulary is used as a communication basis between domain experts and knowledge engineers. The first layer of an expertise model is described in this vocabulary and is built in collaboration with them. The second one is based on a generic vocabulary. By defining the common vocabulary in terms of the generic vocabulary, a reusable task model that is an expertise model at the second layer can be built. We evaluate the effectiveness of this methodology by applying it into substation restoration problems.

Keywords: Expert systems; Knowledge reuse; Ontology; Restoration

## 1. Introduction

To deal with restoration problems at primary substations (hereafter referred to as substations), the authors built several prototypes as described in [12,13]. Based on the experience obtained from these prototypes, we built an operation support system and verified in the field that it was effective [17,18]. The system has been in practical operation since February 1993.

However, like many other expert systems (hereafter referred to as ESs) or knowledge-based systems, it is difficult to apply most of the knowledge in this system to other substations. This is the problem of knowledge reuse. The technology for knowledge reuse has a potentiality to get over the difficulties that the current knowledge engineering is faced with.

There are many ways to establish the technology for knowledge reuse. We decided to adopt the bottom-up approach which is expected to make the best use of our experiences. The bottom-up approach deals with practical problems, and here discussed are substation restoration problems. With the approach, the generalized methodology for knowledge reuse will be built up in the process that abstracts and generalizes the practical problems.

The methods to identify the ontology have been developed and verified in the substation restoration problems [19,15,24]. In the methods, the expertise was decomposed into task knowledge and domain knowledge. Then ontology which is a system of vocabulary used as a fundamental concept for describing the task/domain knowledge is identified. A reusable task/domain model can be represented in that ontology. There are two different levels of abstraction for describing sets of concepts. The first set is a vocabulary applicable in common to the entire target field, and the first layer of the expertise model is described in terms of the vocabulary. They are used in discussions as a common concept between domain experts (hereafter referred to as DEs) and knowledge engineers (hereafter referred to as KEs). The second set is a generic vocabulary which defines task knowledge independently of domain concepts, and the second layer of the expertise model is represented in the generic vocabulary. The generic vocabulary is a result of MULTIS project, a task analysis interview system [22], and it has some features in common with our research:

\- A reusable task model can be built, because the problem solving structure can be described in terms of task ontology which is independent of domain concepts.

\- If the knowledge model is built successfully, a computer program code is generated semi-automatically because MULTIS has symbol level parts which corresponds to knowledge level models.

In the next section, we discuss a general issue of building a reusable knowledge base. Before entering the main issue, we summarize the restoration problem in Section 3. A methodology for identifying the ontology is summarized in Section 4. We illustrate and discuss our methodology with some examples referring to substation restoration problems in Section 5.

## 2. Building and reuse of knowledge bases

## 2.1. Current technology and obstacles for knowledge reuse

With our experiences, we recognize two kinds of difficulties in developing and operating ESs that are practically used.

The first is the difficulty of building knowledge bases. In other words, it is a difficulty of knowledge acquisition. The difficulty is caused by:

\- the gap between expert's conceptual level and implementation level,

\- the lack of communication basis between DEs and KEs.

The process of developing ESs consists of four phases: problem specification, conceptualization, formalization and implementation. We tended to represent knowledge in phases from conceptualization to implementation using production rules. But knowledge representation in rules was not satisfactory for some reasons. Because grain size of description in conceptualization was too rough, KEs were not able to define the expertise correctly. It was difficult for DEs to verify rules in formalization, because such rules contained not only their expertise but also the control knowledge for computer processing. The lessons we learned and our experiences are:

\- To bridge the gap, an incremental development is preferable. Development should be done in several phases and different description levels.

\- To secure the communication basis, a system of vocabulary or ontology should be established and common concepts described using the ontology.

The second difficulty is that of reusing knowledge base. Rule base is one of the most popular knowledge base technologies in which expertise is implemented. It is true that rule base technology is suitable for representing expertise and contributes to building ESs. But the most of the current knowledge bases cannot be reused even if it is the same task and the same field with a different target, because the rules are already compiled and tailored for specific problems. Fig. 1 shows a rule in the field test system. It is one of the rules of the fault section identification task and it is represented in OPS5. It involves some terms specified to a certain substation that is, 1TrB87S, CB210, etc. This means the rule and structure of these rules depend on a topology of a certain substation, so we cannot reuse these rules to other substations. To make the matter worse, they were generalized in the fault section identification task, in other words, the problem solving knowledge which is common in diagnostic problems was not explicit in these rules. We cannot reuse these rules in other similar diagnostic problems such as diagnosis of transformer of substation. The factor which prevents knowledge reuse is a content-related problem. To eliminate the preventive factors, it is important to solve the following problems that are not represented in knowledge base explicitly:

\- to find implicit assumptions, to find implicit viewpoints, and

\- to unify the difference in the purpose of using the knowledge base.

From the viewpoint of how to develop ESs, bottom-up methods have been taken in the industries. Such methods gather pieces of expertise and determine the structure of knowledge, then task structure is determined and an expertise model is built. But it is difficult to grasp the whole structure of the problem in that way, and we recognized the importance of determining the task structure at the beginning of developing [2,6]. On the contrary, the recent methodologies of building ESs adopt top-down methods in which a problem solving process, or task structure, of DEs is modeled first. And then, knowledge structure associated with the task knowledge is extracted. As changing of the methodology, the essential points that are considered in building ESs are being switched over from run-time efficiency to developmental efficiency or reusability of knowledge.

## 2.2. Approach of our method

As mentioned above, a rule base cannot be reused across systems, because each knowledge base has already been compiled for a specific problem. To overcome this difficulty, it is a reasonable way to decompose expertise into some portions and to attempt to reuse every portion. We think task/domain decomposition is an adequate way. Here, by tasks we mean major types of problem solving structures such as diagnosis, design, planning, etc. The domain consists of a field and a target object. By a field we mean an area, where problem solving takes place, i.e. medicine, machinery, steel industry, electric power industry, etc. By a target we mean a concrete object in the field, i.e. a human's body, an automobile, a power plant, etc. [10]. According to the decomposition of expertise into three kinds of knowledge, task knowledge is built for every type of task and is reused in the same type of task across different domains. Field knowledge is built for every kind of domain and is reused in the same domain. Classification of knowledge reuse will be discussed in Section 4.1.

To build a reusable knowledge base, the target task is first decomposed into several general tasks. Then, expertise associated with each general task is decomposed into task knowledge and domain knowledge, and identification of ontology to represent task/domain knowledge is done [8]. Ontology is a system of vocabulary used as fundamental concepts in building an artificial system, and plays an important role in eliminating the preventive factors except implicit assumptions. Task knowledge is mainly composed of control structures specific to respective tasks. By task ontology, we mean a set of primitives for representation of task structures common to ESs in various domains. To facilitate knowledge reusability, we have to devise an appropriate vocabulary for describing the control structure of all ESs. Domain knowledge takes a dominant portion of expertise. Domain ontology is a system of vocabulary for describing the domain.

```txt
(p 1TrB B87: If CB210 = IN, all areas above Bus1 is protective zone
{ <phase> ( phase
^phase_name { <phase_name> | KD3:2:Solving for current protective zone 1 | <> NIL }
}) {
{ <operated_relay> ( operated_relay
^relay_name
{ <relay_name> << |1TrBB87S|
|1TrBB87G| >> }
^target_fault
<target_fault>
^delay_time
<delay_time> ) }
{ <CB210> ( Status of CB before fault
^CB_name
|CB210|
^CB_status
|IN| ) }
-->
(make CB_to_be_tripped
^CB_name
|CB210|
^relay_name    <relay_name>
...
```  
Fig. 1. Example of rule in the field test system.

In identifying task ontology, MULTIS [22] has achieved good results. We want to clear the features of our research to point out similarities and differences between MULTIS and ours.

(1) Bottom-up approach

MULTIS adopts a top-down approach in which the fundamental methodologies for task analysis are investigated using ontology identified in advance. Our research adopts a bottom-up approach focussing our attention on the reusability of a specific knowledge base on an ES.

## (2) To identify task ontology

Task ontology in MULTIS is obtained by analyzing task structures of real world problems. Design of task ontology is done in order to overcome the shortcomings of generic tasks [1] and half weak methods [7] while preserving their basic philosophies. The ultimate goal of task ontology research is to provide all the vocabulary necessary for building a model of human problem solving processes. Our research aim is to develop a methodology to identify task ontology.

(3) The range of our interests include domain ontology

MULTIS has a domain-dependent vocabulary, but it is not a main issue of its research goal. In our research, it is one of the main issues how to define domain ontology that can be treated by task ontology in practical problems.

(4) Preparing two different abstraction level ontologies

MULTIS presents a generic vocabulary independent of domain concepts to DEs directly, because scheduling task treated in MULTIS is a high abstraction level problem itself. But it is not always easy for DEs to describe their ways of problem solving in terms of generic vocabulary. We have two steps of model construction as follows:

\- At first, we find a vocabulary applicable in common to the entire target field. A layer of an expertise model that includes common concepts between DEs and KEs is described in terms of the common vocabulary.

\- Then, the common vocabulary is defined in terms of generic vocabulary. Another layer of an expertise model is represented in generic vocabulary.

Generic vocabulary is for DEs in MULTIS, but it is for KEs in our research. As the purpose of utilization of generic vocabulary is slightly different, we added control vocabulary that was rejected on purpose in MULTIS. We could justify MULTIS research by demonstrating that practical problems are successfully represented in terms of generic vocabulary.

(5) Methodology for supporting to develop ESs

While MULTIS tries to perform automatic or KE-less knowledge acquisition by machines, we aim to support KEs in knowledge acquisition, and to support the whole process of building ESs. Our research shares a lot with KADS [23].

## 3. Restoration problems

Power system functions include the generation, transmission, distribution, and consumption of electricity. Power stations, transmission, substation and distribution facilities, and a variety of loads, are organically connected. Power systems consist of main power transfer components (power stations or power supplies, transmission and distribution lines) and the facilities and equipments used to assure stable operation (protective and communication facilities, monitoring and control equipments, and others).

![](/api/attachments/JG7TWVVD/fulltext/images/2e724d49e3cbd1ff414652e8bc6251c3a69a66cfa543b0aa3862f1c2a5aad9b7.jpg)  
Fig. 2. Three states of power system operation.

Possible power system operating states are broadly classified into normal, emergency, and restored states [11]. Fig. 2 shows the three states of power system operation. The normal state refers to the time when load supply, system configuration, frequency, voltage, and load-flow are appropriately maintained. The emergency state refers to the time when a fault or unexpected load change in the power system threatens to cause disconnection either of the power supply or the load from the power system, transmission line tripping, or even a system blackout. The restored state refers to the time when power system operation has stabilized as a whole although some areas remain unstable due to hindered power supply and generation and interrupted power transmission. Restoration control is performed to return the power system from the restored state to the normal state. Because judgment of the overall situation is necessary, human intervention plays an important role in this control at present.

Restoration originally refers to repairing the facility that experienced a fault, and returning the power system to the state it was in before the fault occurred. Therefore, the power system operation section regards the completion of isolating the power supply outage as the beginning of the temporary restored state. This state is occasionally referred to as system restoration [25]. In most theoretical cases, operations performed until the power supply outage is isolated are regarded as restoration operations. In this study, system switching that is carried out from the time a fault occurs until the power supply outage is isolated is also considered theoretically. The flow chart in Fig. 3 shows the basic sequence of restoration operations. This paper focuses on the operations from the fault section identification to the recovery procedure included in Fig. 3.

![](/api/attachments/JG7TWVVD/fulltext/images/bcec3785b6ea7d2260e92921da3268d5c1afc44deb6319aa7fb29f51123ea339.jpg)  
Fig. 3. Flow of restoration operations.

## 4. The methodology

4.1. Classification of situation for knowledge reuse and ontology

There are a lot of situations where reuse of knowledge is required as shown in Table 1. We discuss each case according to the table.

Task/field knowledge is reused in the same task and the same field in Case A, so the main issue there is to separate the task/field knowledge from the target-related knowledge. A task model may include field-dependent concepts, since it is reused within the same field. It is the chief aim for a field model to be described target-independently. That is, it is an appropriate way to describe task/field knowledge in a vocabulary applicable in common to the entire target field (hereafter referred to as common vocabulary). We should pay attention to the following case: When one wants to reuse a field model in another class of targets in the same field, the grain size of the model will be occasionally changed according to changing the class of target. Then field knowledge sometimes changes according to the change. For example, consider a case of reusing the transformer model in the fault section identification task for the equipment diagnosis problem. There are problems in the same field and in the same type of task. But the equipment diagnosis problem requires not only a theory of electrical circuit but also chemistry of gas analysis. This case does not belong to Case A but to Case C, since the different field knowledge is needed.

Field knowledge is reused across different tasks in the same field in Case B. Task ontology may also include field-dependent concepts in this case, as it also is reused in the same field. We only have to pay attention to the following case: When one wants to reuse a field model in the different task, DEs view the domain from different viewpoints. Functions and attributes of the field model of interest change in such cases, so we must define some extra attributes and additional knowledge. Let us take an example of reusing the transformer model in a fault section identification task and one in a task of target network configuration in fault recovery. The two models are in the same field, that is, a power system. The former task is a diagnostic task and the latter one is a design task. A transformer is only one of the elements belonging to the main circuits in the former task, but it is an important device that has some extra attributes (i.e. maximum load value, allowance for over load condition, etc.) in the latter task.

<table><tr><td rowspan="2">Case no.</td><td rowspan="2">Type of task</td><td>Domain</td><td>Example of job</td><td colspan="2">Example of reuse</td><td colspan="2">Points</td><td rowspan="2">How to identify ontology</td></tr><tr><td>Field</td><td>Target</td><td colspan="2"></td><td>Task ontology</td><td>Domain ontology</td></tr><tr><td>—</td><td>Same</td><td>Same</td><td>Same</td><td colspan="2">(Need not consider reusing knowledge.)</td><td>—</td><td>—</td><td>—</td></tr><tr><td>A</td><td>Same</td><td>Same</td><td>Diff</td><td>Fault section identification.</td><td>(Instance) From As/s to Bs/s. (Class) From s/s to c/c.</td><td>As in the same domain, task ontology can be domain-dependent.</td><td>Domain model should be target-independent.</td><td>Task knowledge and domain knowledge are described in vocabulary commonly applicable to the respective field.</td></tr><tr><td>B</td><td>Diff</td><td>Same</td><td>Same</td><td>Fault section identification and target network configuration.</td><td>Reuse a Tr-model.</td><td></td><td></td><td></td></tr><tr><td rowspan="2">C</td><td rowspan="2">Same</td><td rowspan="2">Diff</td><td>Diff</td><td colspan="2">(Same as in the case that is in the same task and same domain.)</td><td></td><td></td><td></td></tr><tr><td>Same</td><td colspan="2">(As in different fields, there are no same targets.)</td><td colspan="2">Task ontology must be domain-independent.</td><td>MULTIS</td></tr><tr><td rowspan="2">—</td><td rowspan="2">Diff</td><td rowspan="2">Diff</td><td>Diff</td><td>Diagnosis</td><td>Automobile and human</td><td></td><td></td><td></td></tr><tr><td>Diff</td><td colspan="2">(Cannot reuse knowledge.)</td><td>—</td><td>—</td><td>—</td></tr></table>

The same way that describes task/field knowledge in terms of common vocabulary can be applied to both Cases A and B [19]. But we need domain-independent task ontology in Case C, since we have to reuse the task knowledge across various domains. It is effective to use the generic vocabulary developed in MULTIS project to identify the task ontology. Domain-dependent concepts can be detached by redefining the common vocabulary using a set of generic vocabulary. Domain ontology is also redefined as a model, in order to be operated by the task ontology.

## 4.2. Process of building a knowledge base

The point is how to make field knowledge reusable in Case A and B. So, it is a possible way to analyze the knowledge by concentrating on a target or an object (or a noun) and to organize it according to the object-oriented approach. In building ESs, however, the problem solving methods are categorized in generic tasks. We can select an appropriate set of generic tasks equivalent to the respective problems and can analyze the problem concentrating on task structure according to the framework of the respective generic task. It is a good idea to analyze the problem solving process from the perspective of activities (or verbs). In this way, DEs are asked what they do next or what they do before it. It seems easy for humans to reflect on their behavior in this way [20]. According to this manner, KEs acquire expertise related only to the respective task. Furthermore, KEs do not have to go into the details of the field and the matters related to computer software are concealed from DEs. It is important to note that we cannot cope with the problems in Case C without this way of analysis.

Basically, our methodology is following the typical process described in [4], as follows:

Problem Specification, Conceptualization, Formalization and Implementation. The process of building a knowledge base is summarized in this section (the details are not explained in this paper). The process is rarely carried out in a single pass and is done in continual iteration. Terms that appear in the following explanation are summarized in Table 2.

Phase 1. Problem Specification: The environment of the problem (i.e. resource conditions and organizational restrictions) is clarified, and the initial description of the problem that has to be solved within the environment is obtained. The description states what is to be done and does not state how it is to be done.

The person concerned: administrators, a project manager and end users.

## Result: Requirements.

Phase 2. Expertise Design: The problem solving method which DEs do is analyzed and modeled by KEs. In this phase, how to be done is clarified. This phase is described in detail in this paper. This phase is composed of four sub-phases as follows: Phase 2.1. Data Collection and Knowledge Elicitation: A collection of raw data is carried out by DEs. Then the problem solving knowledge is described in natural language.

The person concerned: a project manager, DEs and KEs.

Result: Description of Expertise.

Phase 2.2. Conceptualization of Actual Expertise 1: The purpose of this phase is to logically describe the problem solving knowledge of DEs using their vocabulary. In other words, it is the purpose of the phase to get the structured information. Expertise is decomposed into problem solving knowledge and domain knowledge and is modeled. The model is refined repeatedly with concrete examples gathered in the former subphase. The model is described in concepts of DEs or common vocabulary. DEs and KEs build their common concepts using the model. Task knowledge (in a broad sense) consists of specific processes and a specific process network. Domain knowledge consists of a target model and theories of the corresponding field. Domain knowledge is acquired under the control of elicited task knowledge.

<table><tr><td>Terms</td><td>Explanation</td></tr><tr><td>Problem specification</td><td>The first development phase whose result is a requirement described in natural language.</td></tr><tr><td>Expertise design</td><td>The 2nd development phase in which concepts are elicited from a DE.Firstly, concepts are elicited and arranged in terms of DE&#x27;s vocabulary.Secondary, elicited concepts are redescribed in terms of an ontology. To build a reusable KB, knowledge representation and problem solving methods are determined.The result is an expertise model which consists of two layers.</td></tr><tr><td>Conceptual design</td><td>The 3rd development phase.To implement the expertise model, conceptual design is carried out.The result is a knowledge model.</td></tr><tr><td>Implementation</td><td>The phase in which results of conceptual design are transformed to symbol-level description.</td></tr><tr><td>Administrator</td><td>Their duty is to represent the needs and requirements of the organization for ES application.Whether these needs and requirements are met ultimately determine the overall benefit of the application.</td></tr><tr><td>End user</td><td>These people will actually use the application.</td></tr><tr><td>Project manager</td><td>He champions the cause of the project and facilitates the resolution of problems that may occur in the running of the project.</td></tr><tr><td>Domain expert</td><td>They provide the expertise that serves as the fundamental source of knowledge for the system.</td></tr><tr><td>Knowledge engineer</td><td>They study the problem domain, acquire the knowledge, and structure it to solve the class of problems associated with the domain.</td></tr><tr><td>System engineer</td><td>The person who implement expertise.</td></tr><tr><td>General task</td><td>Major types of problem solving structures such as diagnosis, design, planning, etc.</td></tr><tr><td>Subtask</td><td>Units that a DE handles as one chunk of operations in a general task.</td></tr><tr><td>Requirement</td><td>A definition of a problem written in natural language.</td></tr><tr><td>Expertise model</td><td>A model described in terms of common vocabulary.Common concepts between a DE and a KE are realized in this model.</td></tr><tr><td>Knowledge model</td><td>The respective problem is represented in terms of generic ontology in this model.</td></tr><tr><td>Building block</td><td>Reusable parts of problem solving engines in a symbol level. This consists of executable codes.</td></tr><tr><td>Common vocabulary</td><td>A vocabulary applicable in common to the entire target field which describes expertise in DE&#x27;s terminology. It consists of common verbs, common nouns, etc.</td></tr><tr><td>Specific process</td><td>A unit of task structure described at DE&#x27;s abstraction level. It is defined as a pair of a common verb and a common noun.</td></tr><tr><td>Framework of specific process</td><td>A framework that defines a specific process and consists of an operator and a knowledge source.An operator is a mechanism of executing the common verb.A knowledge source is a domain knowledge which is needed for execution of the operator.</td></tr><tr><td>Specific process network</td><td>A network of problem solving behavior of a DE represented by specific processes.</td></tr><tr><td>Generic vocabulary</td><td>A basic vocabulary to describe generic ontology for each task.It consists of generic nouns, generic verbs, generic adjectives, etc.</td></tr><tr><td>Generic process</td><td>A reusable unit of task structure. It consists of a pair of generic verb and a generic noun.</td></tr><tr><td>Generic process network</td><td>A reusable control structure of a task represented in terms of generic processes.</td></tr></table>

Table 3  
Relation between reuse of knowledge and reusable results

<table><tr><td rowspan="2">Results</td><td colspan="2">Case A</td><td colspan="2">Case B</td><td colspan="2">Case C</td></tr><tr><td>Task knwlg</td><td>Domain knwlg</td><td>Task knwlg</td><td>Domain knwlg</td><td>Task knwlg</td><td>Domain knwlg</td></tr><tr><td>Requirements</td><td> $\Delta$ </td><td></td><td> $\times$ </td><td></td><td> $\times$ </td><td></td></tr><tr><td>Expertise model</td><td> $\bigcirc$ </td><td> $\bigcirc$ </td><td> $\times$ </td><td> $\Delta$ </td><td> $\Delta$ </td><td> $\times$ </td></tr><tr><td>Conceptual model</td><td> $\bigcirc$ </td><td> $\bigcirc$ </td><td> $\Delta$ </td><td> $\bigcirc$ </td><td> $\bigcirc$ </td><td> $\Delta$ </td></tr><tr><td>Building blocks</td><td> $\bigcirc$ </td><td> $\bigcirc$ </td><td> $\bigcirc$ </td><td> $\bigcirc$ </td><td> $\bigcirc$ </td><td> $\bigcirc$ </td></tr></table>

○: reusable; △: reusable (need to modify); x: not reusable.

The person concerned: a project manager, DEs and KEs.

Result: Expertise Model (common vocabulary layer).

Phase 2.3. Conceptualization of Actual Expertise 2: Expertise described in common vocabulary is redescribed in generic vocabulary. Generic vocabulary is a vocabulary with high reusability that is prepared in every general task. It enables to describe expertise in a domain-independent form. The person concerned: a project manager, DEs and KEs.

Result: Expertise Model (generic vocabulary layer).

Phase 2.4. Refinement of Expertise: An actual expertise model which is built in the former subphase is validated and modified into a desirable model for the organization.

The person concerned: administrators, a project manager, end users, DEs and KEs.

Result: Desired Expertise Model.

Phase 3. Conceptual Design: The purposes of the former phases are how to elicit expertise and how to build reusable models. In this phase and after, it is the main purpose how to implement the expertise model. Conceptual design is carried out in this phase.

The person concerned: a project manager and system engineers.

Result: Conceptual Model.

Phase 4. Implementation: This phase consists of some phases responsible for implementation which is not a main issue of this paper. The task model is represented by combining building blocks which are predefined executable codes.

The person concerned: a project manager and system engineers.

Result: Knowledge Base.

Table 3 shows a relation between reuse of knowledge and reusable results.

## 5. Illustration and discussion

We have applied the proposed methodology to several problems. This section presents how to carry out the methodology by using these practical applications as examples. We adopted a real substation as shown in Fig. 4.

5.1. Knowledge reuse across the different target objects (Case A in Table 1)

The goal here is reusing task/field knowledge across the different target objects in the same field.

![](/api/attachments/JG7TWVVD/fulltext/images/ecec73bfa10cf51fa671b3dafac03f26672137659ed5a6fbb5e0407ff47fefe2.jpg)  
Fig. 4. Substation facility configuration in the field test system.

Development of the Field Test System (Substation A)  
![](/api/attachments/JG7TWVVD/fulltext/images/af3d399a912abc4b0d7d0550181d9a85d8a44d5f3460902dbe0417dc1eb99d20.jpg)  
Fig. 5. Evaluation of the method.

Although this objective seems easier to achieve than ones in Cases B and C, it is quite worth while to investigate in the status quo. For example, primary substations that are targets of the restoration problem have various types of configurations (i.e. seven kinds of variations in primary buses, two kinds of variations in neutral resistors and six kinds of variations in secondary buses, etc.), so it is not easy at all to identify the domain ontology independent of topology of substations. In fact, all the ESs for substation operation have been built for each specific substation from scratch.

We have demonstrated that we can build reusable knowledge bases by decomposing expertise into task/domain knowledge and decomposing domain knowledge into field/target knowledge in the diagnostic type problem (i.e. fault section identification) [19], the design type problem (i.e. target network configuration) [15], and the planning type problem (i.e. recovery procedure) [24]. Prototypes of diagnosis and design are implemented in the Rule-extended Algorithmic Language (RAL). The prototype of planning is coded in OPS83.

![](/api/attachments/JG7TWVVD/fulltext/images/55131dae651b608f294d41cbf66b042f2eed5164d16777997991c906856004d7.jpg)  
Fig. 6. Substation facility configuration in the prototype.

![](/api/attachments/JG7TWVVD/fulltext/images/cb70e8524c4bae8c2cdb07783b0164b2aaa8267b396231c27564acd46f447982.jpg)  
Fig. 7. Examples of common verbs and generic verbs (diagnostic task).

In the case study of diagnosis, we have shown that we can establish a communication basis and reuse knowledge base according to the method proposed.

## 5.1.1. Establishing communication basis

As mentioned above, we developed a field test system three years ago. And this time, the expertise of the substation to which our field test system had been applied was reanalyzed. The steps performed are problem specification, conceptualization, formalization and implementation as shown in Fig. 5. Then it was verified in comparison to the field test system that the prototype was equally efficient in identifying fault sections by applying 303 cases. Also, the manpower required for steps from problem formulation to formalization has been substantially reduced from about 24 man-months for the field test system to only 3 man-months for the prototype. The man-power reduction rate is about one eighth. So we can verify the following points:

\- Common vocabulary can become a communication basis between DEs and KEs, and

\- Common vocabulary makes it easy to build an expertise model which is a common concept between DEs and KEs.

## 5.1.2. Reusing knowledge base and ontology

Next, the prototype was applied to another substation as shown in Fig. 5. In this case, the substation shown in Fig. 6 had a different configuration from that of the field test substation in Fig. 4. It was verified that the prototype was built very efficiently because it was able to reuse the problem-solving knowledge for identifying fault sections, and also because a knowledge base was built simply by entering the substation facility configuration data. The prototype was verified using 138 cases.

![](/api/attachments/JG7TWVVD/fulltext/images/696f6ebe2ce43551c51651942f038c34d7e22f7613b9d590cf8d7d55b5961941.jpg)  
Fig. 8. Examples of common nouns and generic nouns (diagnostic task).

The above result demonstrates that it is possible to reuse the task and field knowledge to multiple substations if the expertise is decomposed into task knowledge and domain knowledge and also if the structure of such knowledge is clarified.

The ontology identified in the diagnostic type problem is summarized in Figs. 7 and 8. Only a few verbs have been identified in the fault section identification task. To put them extremely, they can be grouped into three categories as follows:

\- select or list-up: select a part of a target, select essential information, select an assumption based on symptom, etc.,

\- remove: remove unnecessary assumptions,

\- calculate or compute.

The reasons why there were only a few verbs in the task are:

\- The diagnostic type problem does not have so many verbs originally, and

\- The problem solving structure of the fault section identification task is so simple.

## 5.2. Knowledge reuse across the different tasks (Case B in Table 1)

The main objective in Case B is reusing field knowledge across the different tasks. The field knowledge base which was built in the diagnostic problem (fault section identification) has been modified in order to be used in the design problem (target network configuration) design. We illustrate that we can identify reusable domain ontology according to the methodology proposed.

Identification process of the ontology in the design type problem is illustrated according to the methodology explained in Section 4. And I will limit our scope only on the sub-phases from phase 2.1 to phase 2.3.

## Phase 2.1. Data Collection and Knowledge Elicitation

## (Step 2.1.1) Define the Problem Definition Statements

To obtain an initial description of the problem, requirements of the problem are summarized in one or a few statements. The problem definition statements for the substation restoration problem are summarized as follows:

\- Identify the fault sections and specify damaged devices.

\- Generate the feasible target network configuration which consists of only sound devices.

\- Generate a sequence of operations that switches over from the current network configuration to the target network configuration.

(Step 2.1.2) Collect raw data from manuals KEs try to collect raw data, and they consult manuals concerned with the respective problem, collect essential information from them and arrange them. In the restoration problem, operation manuals for the substation were found out.

## (Step 2.1.3) Decompose the problem into several general tasks

The problem is decomposed into several general tasks (i.e. diagnosis, design, planning, etc.) based on the problem definition statements. Each task's requirements are summarized in one or a few statements. We were able to decompose the restoration problem into the task of a fault section identification, the task of a target network configuration and the task of a recovery planning. For example, the problem definition statement for the task of target network configuration was defined as follows:

\- Generate candidates of a network configuration which can get rid of or minimize the abnormal status.

## (Step 2.1.4) Decompose the general tasks into sub-tasks

Analyzing the definition statements of each general task, KEs find units that DEs handle as one chunk of operations, and consider them as subtasks. The rest of the procedure is done for each sub-task so that the problem can be solved easily. The target network configuration task was decomposed into four sub-tasks as follows: secure control power supply, secure neutral resistor, isolate fault sections, restore outage circuit block.

## (Step 2.1.5) Define detailed requirement of each sub-task

Expertise is acquired through an interview using concrete examples. Essential matters such as the reason of doing the respective operations and necessary conditions for the operations have to be included in the requirements. The requirements are described in natural language. And they are described in terms of target-independent vocabulary or applicable in common to the entire target field. The candidates of common vocabulary (i.e. common verbs and common nouns) have to be found in this phase. These candidates are repeatedly refined. Let us take the sub-task “secure neutral resistor” as an example. In this task, a typical statement made by a DE is: “If 5TrB is isolated because of a fault, neutral resistors attached to 5TrB and 6TrB should be out of use, then I use the neutral resistors attached to 7TrB.” In the interview we found hidden information to make underlying conditions explicit (i.e. connection, charge and damage of devices, etc.). The requirements were defined in target-independent terms, as follows:

\- Neutral resistors have several kinds of resistance values.

\- If we want to use neutral resistors, we have to select a resistor or a set of resistors that has appropriate resistance values.

Target-independent terms are candidates of common vocabulary. We pay attention to verbs, and decompose them into common verbs by asking DEs how they carry it out. For example, a candidate “find a combination” is decomposed into “list-up”, “generate sets”, etc.

## Phase 2.2. Conceptualization of Actual Expertise 1

(Step 2.2.1) Define a specific process network

A specific process is defined as a pair of a common verb and a common noun. A specific process network that is a control structure of operation is constructed by configuring several specific processes in a network. We think that a frame work of problem solving behavior of DEs is represented by a specific process network. Fig. 9 shows an example of a specific process network drawn in PAD [3]. We were able to confirm that it is not difficult for DEs to find specific processes and to define specific process networks in the expertise design phase, if the candidates of common vocabulary were appropriately selected in the problem specification phase. In the specific process identification, one for a secure neutral resistor shown in Fig. 9 was obtained in which the shaded portion is a key process to elicit from DEs. KEs added some processes not shaded in Fig. 9. The difficulties in identifying ontology are decomposing of task/domain concepts and determination of grain size and abstraction level. They are not only dependent concepts but also relate deeply to each other. Determination of grain size and abstraction level are especially difficult, but we can show a guideline. That is, ontology must be detailed enough to describe the respective task structure and be general enough to reuse knowledge described by themselves [9]. Concerning specific processes, verbs can be used as the key to separate task knowledge from domain-dependent concepts. Their grain sizes are justified when they have been decomposed into minimum operation units that DEs recognize, or when we reach an algorithm. Their abstraction level becomes suitable when they are general enough in the respective domain. Let us pay attention to the most popular common verb “select”, and consider separation of concepts, grain size and abstraction level. In the specific process “select a top priority combination (of neutral resistors)" in Fig. 9, it has been separated and abstracted from the target concepts (i.e. 5TrB, etc.). The way of selection is determined by a certain algorithm, so there is no need to decompose it further.

![](/api/attachments/JG7TWVVD/fulltext/images/47e9175e7a470255665157992267cffb6cc93790acc9a4cd7e07e0a40addf4b5.jpg)  
Fig. 9. An example of a specific process network.

![](/api/attachments/JG7TWVVD/fulltext/images/fdc89b8c12609c7153ccc75a3ffa2aafbd7ea70c99408838e4f733c438bcec57.jpg)  
Fig. 10. Framework of specific process.

## (Step 2.2.2) Define specific processes

Specific processes are defined according to the framework of the specific process shown in Fig. 10. It consists of an operator and a knowledge source. Operator is a mechanism of executing the operation of the common verb, and knowledge source is a domain knowledge which is needed for execution of the operator. Framework is a concept corresponding to a building block in MULTIS. In our methodology, we use this concept in an earlier stage than MULTIS does, because it makes easier for KEs to specify the expertise model. Let us take a specific process “select a top priority combination (of neutral resistors)” again as an example. It’s operator is to select one element in the specified sets according to the condition, which is separated from domain concepts completely. In the knowledge source, the target is a combination (of neutral resistors). The attribute to note is the order of priority (of combinations). The evaluation function is one that determines the order of priority.

## (Step 2.2.3) Finalize the definition of common vocabulary

Common vocabulary is finally defined when specific processes have been defined completely.

## (Step 2.2.4) Build a domain model

A domain model is constructed as an object model of the object-oriented method. Common nouns are extracted as candidates of object classes. The followings are the reasons why a domain model is constructed as an object model:

\- Object-oriented analysis is an eligible way to modeling a complicated objects incrementally.

\- An object model can be easily modified after development.

The domain model is represented in the style of OMT [14]. It becomes easier for KEs to build a domain model. KEs can pick up candidates of objects and their attribute as common nouns in knowledge source. Expertise model is easily understood by DEs, and it contributes a lot to making discussion between DEs and KEs effective. A substation device model and a class hierarchy of main circuits are shown in Figs. 11 and 12 respectively. They were built in the fault section identification task. We were able to modify these domain models to obtain one for the task of target network configuration generation. We can say the domain model is reusable, though there are two major modification points. First one is an addition of a new class. According to a change of viewpoints, the recognition unit in the task was changed from each circuit element to a block of elements that consist of chief devices (i.e. buses, transformers, etc.). So, a new class, which is a main circuit block, was added to the main circuit hierarchy as shown Fig. 13. This new class was found as a new concept or new common vocabulary in the problem specification phase. The second one is modifications of functions and attributes according to change the viewpoint. A transformer is just an element included in the main circuit in the former task, but it is an important device that has some extra attributes (i.e. maximum load value and allowance for over load condition, etc.). So, we added new attributes. This changes were found as new concepts in the problem specification phase and were identified as new attributes in defining a framework of specific process in the expertise design phase. The number of classes of the target model which was built in the fault section identification problem is 45. We added five new classes and modified three classes in it in this problem.

![](/api/attachments/JG7TWVVD/fulltext/images/fa4d9116957f2d1fc99c2112956aac008704f81e8a3899ece0850212655e95e9.jpg)  
Fig. 11. Model of substation equipments.

![](/api/attachments/JG7TWVVD/fulltext/images/d7d680fa354389c86826bed9614573a016a28adc3d3931a211ddc0769eb23423.jpg)  
Fig. 12. Class hierarchy of main circuit device.

## (Step 2.2.5) Justify an expertise model

An expertise model which is built in this sub-phase is applied to concrete examples and is justified by the examples. As mentioned before, we verified the expertise model by applying about 303 cases when we built the field test system. We were able to reduce the number of the cases to 99 to verify its performance.

## Phase 2.3. Conceptualization of Actual Expertise 2

(Step 2.3.1) Describe each common verb in terms of generic verbs

Task knowledge which is described in terms of common verbs includes domain-dependent concepts, since common verbs are domain-dependent. The domain-dependent concepts are separated from task knowledge by defining common verbs in terms of generic verbs defined in MULTIS. As a result, 11 common verbs were found as shown in Fig. 14, and were described in terms of 12 generic verbs found in MULTIS and in terms of new control verbs, if-do and loop. For example, the common verb “list-up” was defined by four generic verbs that are “generate”, “pick-up”, “check” and “insert”.

## (Step 2.3.2) Redefine the task model

The control structure which is defined in terms of a specific process and a specific process network is redefined in generic processes and a generic processes network is defined in MULTIS.

## (Step 2.3.3) Redefine the domain model

The common nouns were described in terms of generic nouns as shown in Fig. 15. The domain model is represented by the generic nouns.

## 5.3. Knowledge reuse across the different domains (Case C in Table 1)

We have not verified our methodology for Case C yet. However, we have an optimistic view to the applicability of our methodology to the Case C problems, because we were able to define common verbs in terms of generic verbs and common nouns in the form that generic verbs or generic processes can operate on.

![](/api/attachments/JG7TWVVD/fulltext/images/b512d0b5bc64e6a620fe80d63aae932af2b071b1777fd5bd9e33928c19cf8a51.jpg)  
Fig. 13. A class appended to main circuit model.

Specific Process (Common Verbs + Nouns)  
![](/api/attachments/JG7TWVVD/fulltext/images/d25a4321d5cbed2c7162c918b26940c12ec6923ed617d4102d11c1093462f6db.jpg)  
Fig. 14. Examples of common verbs and generic verbs (design task).

5.4. Mediation between the expertise design and implementation

We explain how to mediate between the expertise design and implementation briefly. The domain model was redefined using a list or sets in order to be operated by generic processes as shown in Fig. 14, as the task model has been redefined using generic processes. Let us explain the relation between a domain model and a generic model taking the generic verb “select” and a main circuit element as examples. Because the meaning of the verb “select” is to select objects satisfying some conditions from a set, which is one of the abstract data structures, a set was introduced as a metaclass of objects. Then, a main circuit element, which is one of the domain models, is redefined using sets. Fig. 16 shows a set of main circuit elements taking a network search algorithm into account. In this example, domain-dependent objects, which are shaded in Fig. 16, are defined as related with a metaclass that represents a set.

![](/api/attachments/JG7TWVVD/fulltext/images/6212fedc63f81e6e44de3618019117c670e9418d75fdc3f4e603f79d56fd3444.jpg)  
Fig. 15. Examples of common nouns and generic nouns (design task).

![](/api/attachments/JG7TWVVD/fulltext/images/98caea6e77ff7968de9dc93b99f54ca6157bf24b874f79489315301794b19231.jpg)  
Fig. 16. A set of main circuit elements.

## 5.5. Discussion

The goal of this research is to establish a methodology for building a reusable knowledge base, under which we have two subgoals. The first subgoal is to provide a guideline for developing a practical ES with a reusable knowledge base. The second one is to develop a tool which supports to build a prototype for validating an acquired knowledge base.

The former is not described in this paper except the outline of development phases. Following the guideline we designed, we have developed an operational ES. The outline of our development process is similar to one of KADS [23]. Both adopt the conventional development process, that is, problem specification, conceptualization, formalization and implementation. However, our method is reflected in the decisions making way in Japan in its problem specification phase. In the conceptualization phase and the implementation phase, the object-oriented approach [16,14] suggests the way to build a domain model and the way to analyze the problem in depth through iterative refinement.

Concerning the second subgoal, we have been studying a way for identifying the ontology that is indispensable for building reusable knowledge. And we aim to develop a smart tool for knowledge acquisition. The tool supports KEs in eliciting raw data and building a structured expertise model. It also supports to build a prototype to validate an expertise model. We do not consider the performance of a prototype. In the process, we adopt the two layered expertise model. We can analyze and structure the expertise model step by step.

Let us discuss related work. Terano [21] has discussed a methodology for developing an ES emphasizing a life cycle of an ES in practical use, and defines knowledge acquisition activities of each developmental phase. He also discusses validation methods of ESs. ES/SDEM [2] is a guideline for development of an ES. It introduces a framework called expertise model that combines a problem solving process and a data structure. The structure of the model is similar to our framework that consists of task/domain knowledge. CAKE [5] proposed a methodology for building a problem solving method regarding to a concrete task by combining primitives of problem solving methods.

The methodologies for developing software has been changing from a top-down approach in water fall style to a bottom-up approach such as object-oriented analysis. On the other hand, the methodologies for developing ESs is clanging in an opposite direction, which is an interesting trend.

## 6. Conclusion

We have discussed a methodology for building reusable knowledge bases based on identification of task/domain ontology. The methodology has four phases such as requirement specification, expertise model, conceptual model and building block. Requirement specifies the problem in natural language using domain expert's terms, so it is not completely logical. The first layer of the expertise model is logically described in terms of common vocabulary as ontology, and the model enables a collaborative work among domain experts and knowledge engineers. A target-independent and field-dependent model can be described in this model, so a reusable domain model can be built. Based on that expertise model, a knowledge engineer builds the second layer of the expertise model using generic vocabulary as ontology. In this model, a domain-independent task model can be defined. As we can prepare executable building blocks, a knowledge level model can be linked to a symbol level model.

We verified our methodology is efficient in Case A, that is, different target objects in the same task and field, and B, that is, different tasks in the same domain and target. Evaluation for the Case C problems, that is, different domains for the same task, has not been done. But it seems our method is applicable to the problems in that case, because task knowledge can be represented in terms of generic vocabulary that is independent of domain concepts.

Future work includes to refine each development phase in more detail and systematize the methodology. We think it is the most important to establish a methodology which can be used in practical ESs' developments. After establishing the whole methodology, we would like to try to develop a computer aided tool which is based on common vocabulary and generic vocabulary.

## Acknowledgements

We are grateful to our colleagues for discussions that have influenced this paper. In particular, we would like to thank Johan Vanwelkenhuysen for his helpful comments.

## References

[1] B. Chandrasekaran, Generic Tasks in Knowledge-Based Reasoning: High-Level Building Blocks for Expert System Design, IEEE Expert (Fall 1986) 23–30.

[2] K. Fujidoh, S. Matsumoto and T. Sato, Development Environment for Expert System Based on ES/SDEM, Journal of Japanese Society for Artificial Intelligence 5, No. 2 (1990) 213–219.

[3] Y. Futamura, The Problem Analysis Method PAD and its Application, Symposium of the Technique of Microcomputer Software, Information Processing Society of Japan (1982).

[4] F. Hayes-Roth et al., Building Expert Systems (Addison-Wesley, 1983).

[5] M. Hori, Y. Nakamura and T. Hama, Methodology for Configuring Scheduling Engines with Task-Specific Component, Proceedings of the Second Japanese Knowledge Acquisition for Knowledge-Based Systems Workshop (1992) 215-229.

[6] S. Matsumoto and A. Horsfall, The Automation of Knowledge Acquisition, Proceedings of Australian Workshop on Knowledge Acquisition for Knowledge-Based Systems (1991) 98–113.

[7] J. McDermott, Using Problem-Solving Methods to Impose on Knowledge, Proceedings of International Workshop on Artificial Intelligence for Industrial Applications (1988) 7–11.

[8] R. Mizoguchi, T. Yamaguchi and O. Kakusyo, A Methodology for Building Expert Systems, Japanese Society for Artificial Intelligence, SIG-KBS-8801-2 (1988) 11–22.

[9] Mizoguchi et al., Task Ontology and its Use in a Task Analysis Interview System - Two-Level Mediating Representation in MULTIS, Proceedings of the Second Japanese Knowledge Acquisition for Knowledge-Based Systems Workshop (1992) 185-198.

[10] H. Motoda, R. Mizoguchi and T. Nishida, Report of the Workshop of Knowledge Sharing and Reuse, Journal of Japanese Society for Artificial Intelligence 8, No. 5 (1993) 666–671.

[11] G. Noda, Power System Control (Denki Shoin, 1986).

[12] M. Oki, Y. Takaoka et al., Substation Operation Support System Which Allows Even-Driven Processing, Proceedings of International Workshop on Artificial Intelligence for Industrial Applications, IEEE (1988) 64–69.

[13] M. Oki, Y. Takaoka et al., Substation Operation Support System with Even Driven Processing, Future Generation Computer Systems, Vol. 5 (North-Holland, 1989) 41–49.

[14] J. Rumbaugh et al., Object-Oriented Modeling and Design (Prentice Hall, 1991).

[15] M. Sakamoto, Y. Takaoka, Q. Zhang and R. Mizoguchi, Fault Recovery Operation Support System of Primary Substations Based on the Reusable Knowledge Base, Japan Society for Artificial Intelligence, SIG-KBS-9304-3 (1994) 17–24.

[16] S. Shlaer and S.J. Mellor, Object Lifecycles (Prentice Hall, 1992).

[17] Y. Takaoka et al., 275kV Substation Operation Support System - System under Field Test and the Dedicated Shell, Proceedings of Expert System World Congress, Vol. 2 (1991) 1327-1334.

[18] Y. Takaoka et al., Primary Substation Operation Support System with Multiple Inference Engines, Journal of Japanese Society for Artificial Intelligence 9, No. 1 (1994) 148–156.

[19] Y. Takaoka, R. Mizoguchi et al., A Study of Methods of Knowledge Reuse Regarding Substation Fault Recovery Operation Support System, Proceedings of '94 Japan/Korea Joint Conference on Expert Systems (1994) 259–264.

[20] H. Taki and K. Tsubaki, Expert Model: A Knowledge Representation for Knowledge Acquisition, Journal of Japanese Society for Artificial Intelligence 5, No. 2 (1990) 203–212.

[21] T. Terano, The Methodology for Developing Knowledge-Based Systems (Asakura Shoten, 1993).

[22] Tijerino and Mizoguchi, MULTIS II: Enabling End-Users to Design Problem-Solving Engines via Two-Level Task Ontologies, Lecture Notes in Artificial Intelligence 723-Knowledge Acquisition for Knowledge-Based Systems (Springer-Verlag, 1993) 340–359.

[23] B.J. Wielinga, A.Th. Shcreiber and J.A. Breuker, KADS: A Modeling Approach to Knowledge Engineering, Knowledge Acquisition 4, No. 1 (1992) 5–53.

[24] Q. Zhang, Y. Takaoka, R. Mizoguchi et al., Effort for Building a Reusable Knowledge Base – Generating Operation Sequences for Accident Restoration of Primary Substations Based on the Reusable Knowledge Base, the Transactions of the Institute of Electronics, Information and Communication Engineers (1994) (to appear).

[25] Investigation Committee for Power System Restoration Operations, Power System Restoration Operations, Technical Report of Institute of Electrical Engineers of Japan, Vol. 2, No. 354 (1990).

![](/api/attachments/JG7TWVVD/fulltext/images/00afcd34d986e588bd757f51a736ba12b92c29ab48cee0e4522584a48574bb67.jpg)

Yoshiyuki Takaoka was born in Nara, Japan, on January 10, 1953. He received the B.S. and M.S. in Electrical Engineering from Kansai University, Osaka, Japan, in 1975 and 1977, respectively. Since his graduation, he has been working for Toko Seiki Company Ltd. He received the Ph.D. degrees from Osaka University, Osaka, Japan, in 1995. He is currently interested in the research of knowledge engineering. He is a member of the Japanese Society for Artificial

Intelligence, the Information Processing Society of Japan and the Institute of Electric Engineers of Japan.

![](/api/attachments/JG7TWVVD/fulltext/images/5d19c525877627e6994d53d210eefd86ee99cad9e75869661c0a5a4a8babd6fa.jpg)

Riichiro Mizoguchi was born in Tokyo, Japan, on October 13, 1948. He received the B.S., M.S., and Ph.D. degrees from Osaka University, Osaka, Japan, in 1972, 1974 and 1977, respectively. From 1978 to 1986 he was research associate in the Research Department of Electronics, the Institute of Scientific and Industrial Research, Osaka University. From 1986 to 1989 he was Associate Professor and he is currently Professor there. His research interests include nonparametric data

analyses, speech understanding, knowledge engineering and intelligent tutoring systems. Dr. Mizoguchi is a member of the Japanese Society for Artificial Intelligence, the Institute of Electronics, Information and Communication Engineers, the Information Processing Society of Japan, the Acoustic Society of Japan, the Japan Society for CAI, AAAI and IEEE. He received honorable mention for the Pattern Recognition Society Award and the Institute of Electronics, Information and Communication Engineers Award in 1985 and 1988, respectively.
