---
otero_id: 20096
otero_key: "NXYTF8NR"
title: "Structured modeling group support systems: a product design theory"
authors: "Kenneth R. Walsh; Michael H. Dickey"
year: "2004"
journal: "Information & Management"
doi: "10.1016/j.im.2003.07.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Structured modeling group support systems: a product design theory

Kenneth R. Walsh<sup>a,\*</sup>, Michael H. Dickey<sup>b,1</sup>

<sup>a</sup>Department of Management, University of New Orleans, New Orleans, LA 70148, USA

<sup>b</sup>Management Information Systems Department, College of Business, Florida State University, Tallahassee, FL 32306, USA

Accepted 31 July 2003

## Abstract

Structured modeling is critical to the design, development, and implementation of many systems including computer software, business processes, and data networks. Since the creation of structured models relies on the knowledge of many organizational stakeholders, groups often accomplish this task. Group support systems (GSS) focus on the support of group processes and would appear to be useful for structured modeling; however, GSS usually only provide textual or decision related output rather than the structured models needed for many design processes. This paper proposes a class of systems, structured modeling GSS (smGSS), which adds support for the development of structured models to standard GSS. Since past research has shown that research results may be difficult to compare across studies when the system under investigation is not well defined, this paper develops a product design theory that defines the required characteristics of and testable design propositions for an smGSS as derived from existing theory and empirical investigations.

Keywords: D.1.1 applicative (functional) programming; D.2.2 design tools and techniques; D.2.10 design; H.4.1 office automation; Groupware; H.5.3 group and organization interfaces; I.6.5 model development; Group support systems (GSS)

## 1. Introduction

Structured modeling is a vital process in systems analysis and work redesign [15]. Structured models can address many of the human cognitive limitations that occur when developing correct systems requirements [7]. They also play an important communication role when a design must be developed that meets the approval of many stakeholders. Improving communication can be pivotal to creating better models that in turn result in better finished products.

Some researchers have argued that collaborative systems development, focused on user needs, can improve software development more than either CASE or group support systems (GSS) has [25]. Joint application design (JAD) and rapid application development (RAD) have been shown to be effective in some contexts; however, larger systems involving many users can also benefit from computer supported collaborative requirements analysis [8].

GSS is specifically designed to support group processes, but it does not support graphics-based structured modeling. Previous GSS research has studied systems where the output has been decisions and/or textual supporting documents. We propose structured modeling GSS (smGSS) as an extension of standard GSS that supports the interactive model development process. The primary research question addressed in this paper is:

How should systems be designed for use in supporting a group structured modeling process?

One way of discussing design issues is the IS design theory (ISDT) approach, which is used to link basic research and systems design [31]. Walls et al. [48] in their exposition of ISDT explain that a design theory is a prescriptive theory based on theoretical foundations that illustrates how a design process can be completed both effectively and feasibly. A complete design theory, according to them, has two components. One deals with the product of design, or the plan of how something can be accomplished or produced; the other deals with the process of design, or the actions of planning and proportioning structure in a way that satisfies all requirements. This paper proposes only a product design theory of an smGSS.

This theory can be used to develop new, internally consistent, prototypes or systems; evaluate existing collaborative modeling systems; and inspire scientific debate. Then modifications to the design theory can be considered in a fashion similar to traditional theory.

Differences in findings in previous studies on collaborative environments may be attributable to differences in the systems used [9,23,40]. The ISDTapproach makes explicit links between theory and systems that can mitigate such weaknesses. Here, we use the ISDT approach to address the question of how computer systems should be designed for supporting a group structured modeling process.

## 2. Structured modeling and collaboration

Structured modeling and collaboration are often useful in design of systems; each is intended to improve communication and work results. Together they provide powerful, synergistic process improvements.

Structured modeling is the development of models with well-defined components and rules for interconnecting them. The components can be stored as data definitions rather than as image files, thereby allowing for semantic rather than purely graphical manipulation [38]. Data flow diagrams, entity-relationship (ER) diagrams, and flow charts are examples. Structured models are used because concise and unambiguous system representation cannot be made using merely natural language [46].

Collaboration is a goal oriented group process that permeates many organizational environments. GSS are software systems designed to support such collaboration [16]. GSS typically include several tools designed to support tasks common to business meetings and decision making including brainstorming, writing, organizing ideas, and voting or prioritizing. A trained facilitator usually orchestrates the tools [36].

Integration of GSS and structured modeling tools would be of great benefit to structure modeling processes. However, in a study of business process change, a list of 102 software tools was compiled and none supported both group support and structured modeling [29]. Although many tools span the BPR life cycle, few tools exist to support non-technical design teams in the critical activity of designing business processes.

Special purpose collaborative activity modeling tools have been shown to improve the efficiency of the development process [17]. Model quality has been found to be equal to that of models developed without a collaborative tool while allowing for substantially wider user participation [15]. A group data modeling tool has also been used to support larger groups developing enterprise data models, improving both participation and comprehension of participants [30]. However, exploratory research with collaborative activity and data modeling tools has not developed a general theory of structured modeling tool design. Further, the tools are not integrated with GSS, relying on basic import and export features.

## 3. An IS design theory approach

Creating systems that test the feasibility of new types of IT-enabled automation is critical, but for developed systems to be effective, they must be consistent with the theories or concepts being evaluated. Typical systems development methodologies help improve consistency with requirements but do not address the need for consistency with theory. An ISDT methodology can be used to create requirements that follow the theory.

![](/api/attachments/NXYTF8NR/fulltext/images/4df413850d9e888fd1f1ec44f49ccf086ba632b099b750405eb400b44355a319.jpg)  
Fig. 1. An IS research approach (adapted from [35]).

An IS research approach recommended by Nunamaker [35] is shown in Fig. 1. However, since theories cannot be proven, confidence in them can only develop from repeated study in which they are tested and modified. The arrows can be considered knowledge links between activities in a research program. If these are not validly maintained, studies, systems and theory will be inconsistent, leading to uninterpretable results. The ISDT approach allows for the explicit definition of system design requirements, maintaining a valid link between systems design, theory, and research design. The components of an ISDT, as espoused by Walls et al., are listed in Table 1.

## 4. A product design theory for an smGSS

A product design theory begins with relevant kernel theories and develops meta-requirements, and a meta-design resulting in testable design hypotheses. Each of these elements is developed in the following sections.

## 4.1. Design product kernel theories

Design product kernel theories derive from natural or social sciences that govern design requirements. They describe the domain in which a tool will function and provide a basis for developing design propositions that will lead to desired outcomes. This may be organized around the major categories of constructs relevant to a product design theory of an smGSS. The constructs are shown in Table 2, including related research. The following sections are organized by the classes of constructs, group, task, context, technology, process, and outcome, commonly used in group research (e.g. [32]).

## 4.1.1. Group

A group consists of two or more individual members. There is no strict limit on the size, but large groups tend to become less mutually aware, and thus become less effective.

Four group-related constructs, member proximity, group size, formal hierarchy, and group history, have been identified in other research. DeSanctis and Gallupe found that member proximity can affect productivity, satisfaction, and quality of deliverables. Distributed groups may also require software support for both larger group sizes and increased facilitation support, as opposed to face-to-face groups [45]. Group size can affect group work and how members interact [47]. In groups where members are identified, formal hierarchy, or the existence of a leader, may improve

<table><tr><td colspan="2">Components of an information system design theory (ISDT) [48]</td></tr><tr><td>Design Product</td><td></td></tr><tr><td>Meta-requirements</td><td>Describes the class of goals to which the theory applies</td></tr><tr><td>Meta-design</td><td>Describes a class of artifacts hypothesized to meet the meta-requirements</td></tr><tr><td>Kernel theories</td><td>Theories from natural or social sciences governing design requirements</td></tr><tr><td>Testable design product hypotheses</td><td>Used to test whether the meta-design satisfies the meta-requirements</td></tr><tr><td>Design Process</td><td></td></tr><tr><td>Design method</td><td>A description of procedure(s) for artifact construction</td></tr><tr><td>Kernel theories</td><td>Theories from natural or social sciences governing the design process itself</td></tr><tr><td>Testable design process hypotheses</td><td>Used to verify whether the design method results in an artifact which is consistent with the meta-design</td></tr></table>

Table 2 Construct summary

<table><tr><td>Construct</td><td>Description</td><td>Related research</td></tr><tr><td>Group</td><td>Set of interacting people</td><td>[33]</td></tr><tr><td>Member</td><td>A person participating in a group</td><td>[33]</td></tr><tr><td>Member proximity</td><td>Physical closeness of group members</td><td>[18,45]</td></tr><tr><td>Group size</td><td>Number of members in group</td><td>[18,47]</td></tr><tr><td>Formal hierarchy</td><td>Existence of a leader in the group</td><td>[4]</td></tr><tr><td>Group history</td><td>Shared experience of an established group</td><td>[32]</td></tr><tr><td>Task</td><td>What the group is trying to accomplish</td><td>[32]</td></tr><tr><td>Task complexity</td><td>The degree of effort required to complete a task</td><td>[4]</td></tr><tr><td>Solution multiplicity</td><td>The degree to which there is more than one possible course of action to accomplish a given objective</td><td>[4,49]</td></tr><tr><td>Context</td><td>Setting in which a task is being performed</td><td>[16]</td></tr><tr><td>Socially sensitive</td><td>A context where members may withhold information because of possible personal ramifications</td><td>[24]</td></tr><tr><td>Reliance on individual expertise</td><td>The degree to which individual expertise changes task complexity or solution multiplicity</td><td>[49]</td></tr><tr><td>Technology</td><td>Tools use by the group to complete a task</td><td>[16]</td></tr><tr><td>Facilitation</td><td>Preparation of the technology for group use and creation of user comfort with it</td><td>[1,6,10,34]</td></tr><tr><td>Access control</td><td>A designated member&#x27;s ability to control access of others</td><td></td></tr><tr><td>Usability</td><td>The ability of a user to easily and effectively complete desired tasks in target environment</td><td>[19]</td></tr><tr><td>Model definition</td><td>Structures for model elements and their relationships</td><td>[12]</td></tr><tr><td>Hierarchical modeling structures</td><td>Decomposition of a model from parents to children</td><td>[42]</td></tr><tr><td>Model editing</td><td>Inserting, deleting, modifying and combining model elements</td><td>[12]</td></tr><tr><td>Tool support for syntax checking</td><td>Computer support for identifying syntax errors</td><td>[14]</td></tr><tr><td>Tool support for semantic checking</td><td>Computer support for identifying semantic errors</td><td>[14]</td></tr><tr><td>Form based UI</td><td>Use of a computer form with specific labeled fields for each data item</td><td>[14]</td></tr><tr><td>Graphical model view</td><td>A computer generated graphical version of model</td><td>[12]</td></tr><tr><td>Process</td><td></td><td></td></tr><tr><td>Anonymity</td><td>The extent to which the author of an input is unknown</td><td>[36]</td></tr><tr><td>Identified input</td><td>Input to a system is identified by the author</td><td>[39]</td></tr><tr><td>Parallel input</td><td>All members can edit model simultaneously</td><td>[36]</td></tr><tr><td>Editing awareness</td><td>Indicators for when an element is in use or an editing event has occurred</td><td></td></tr><tr><td>Outcome</td><td>The result of group members interacting in a process</td><td></td></tr><tr><td>Syntactic quality</td><td>Conformance to modeling rules</td><td>[14]</td></tr><tr><td>Semantic quality</td><td>Conformance of the model to the real situation being modeled</td><td>[14]</td></tr><tr><td>Modeling productivity</td><td>The rate at which the model is created relative to resource required</td><td>[14]</td></tr><tr><td>Participant understanding</td><td>The degree to which the participants understand the modeling language and what has been modeled</td><td>[19]</td></tr></table>

performance. Groups can also be categorized by the history members share as well as their expectations for continuing as a group [41].

## 4.1.2. Task

Benbasat and Lim [4] identify two task-related constructs, task complexity and solution multiplicity, as the most stable. The greater the effort required to complete a task, the more complex it is [22]. The greater the number of acceptable solutions, the greater the degree of solution multiplicity.

## 4.1.3. Context

Context covers a wide array of factors. One is the individual expertise of group members; this may affect task complexity [49]. Another factor is the existence of a socially sensitive context or one in which members may withhold information because of personal ramifications [24].

## 4.1.4. Technology

Benbasat and Lim identified facilitation as an important technology factor for GSS. We also include usability as an important technology factor. In addition, Nunamaker et al. [37] identified task structure and task support as categories that are specific to the task being supported.

Facilitation has been theorized to be critical to GSS success [6,13]. Process facilitation has been shown to have a positive effect on meeting processes [34]. A facilitator prepares technology for group use and creates comfort. Effective facilitation also requires the facilitator to have a clear understanding of the technology and its capabilities. Closely related is tool support for access control, which gives a designated member the ability to change member access rights. For example, a facilitator can use it to focus group attention on a subset of the model.

Another technology factor is usability [19]. It is difficult to develop usable systems, particularly novel systems, such as an smGSS without prototyping. However, analysis of tasks can provide a logical starting point. Understanding task structure aids in designing systems that provide appropriate task support.

Task structure and task support are specific to the problem task. Task structure provides a method for the problem solving process. Task support aids in analysis of the task structure with search engines that help look for more information, etc. [21]. Although task support provided by GSS is useful for meetings, it is inadequate for structured modeling. For example, conflicts may be lost in the volume of electronic text produced in GSS/JAD sessions. Further, the textual nature of general purpose GSS make systematic assessment of completeness and consistency nearly impossible [13]. Therefore, structures for model definitions, including definitions of elements and their relationships, must be included in an smGSS. Additionally, complex models require support for hierarchical modeling structures.

To develop a structured model, group members will need to edit the model, inserting, deleting, and modifying elements. There is also a need for a ‘‘combine’ editing function, because the same activities may have been entered with different names. Proliferation of synonyms occurs in group modeling efforts, although facilitation may reduce its occurrence. Furthermore, computer-based syntax and semantic checking are needed to minimize ambiguity in defining structured models.

Usability is also affected by the user interface. Although the use of a modern graphical user interface (GUI) is obvious, unstructured collaborative graphical tools can lead to problems of model element convergence and drawing space management resulting in increased times for diagramming tasks [2]. Dean et al. used a more successful form-based user interface, where model elements are edited with a screen form that lists and labels all model element fields and only requires entry of minimal information: model elements can be inserted, deleted, or selected for editing from a hierarchical text view allowing simpler access and entry of elements. However, to help SMEs understand the complete model, graphical views are also needed. Given the unstructured nature of an individual’s choice to review or edit the model, switching between views should be as intuitive as possible.

## 4.1.5. Process

Theory on how to collaborate electronically and develop structured models are foundational for an smGSS product design theory. Some aspects of computer-mediated collaboration result in process gains while others result in losses compared to both individual efforts and unsupported group collaboration [26]. Nunamaker et al. suggested that four theoretical mechanisms, process support, process structure, task structure, and task support, affect process gains and losses.

Four system features have been identified that provide process support: anonymity, identified input, parallel input, and editing awareness. Anonymity is the extent to which group members can associate input with its author [28]. It is sometimes confused with identified input, which is input that has its author explicitly shown. Parallel input is a feature which enables all group members to edit models simultaneously. Editing awareness is provided by giving feedback to users about current or past editing activity. These features keep users informed of the activity of others [27]. The feedback facilitates shared understanding of information flow [5].

## 4.1.6. Outcomes

Benbasat and Lim identified three categories of outcomes: performance, satisfaction, and structural products. For decision-making processes, the performance category included decision quality, number of alternatives, and time to reach a decision. The satisfaction category included the constructs satisfaction with process, satisfaction with outcome, and confidence with the outcome. The structural products category included consensus and equality of influence.

In the structured modeling environment, a primary outcome is the model itself. Thus, model quality is an important outcome; it has three facets: syntactic quality, semantic quality, and robustness.

Another performance construct is modeling productivity, defined as the rate at which the model is created relative to the resources required. An example is the number of model elements created per personhour.

A structural product outcome is participant understanding. It is the degree to which the participants understand the real situation. Understanding the information structure will affect the user’s ability to use electronic texts. Many group members may not initially understand the modeling language, and may or may not understand the work previously performed on the model by others. Model understanding, therefore, can be viewed as an intermediate outcome needed to conduct model editing.

## 4.2. Meta-requirements for an smGSS

Meta-requirements are prescriptions for tool design derived from testable design theory propositions. Since an ISDT’s goal is to tell ‘‘how to’’ design a system, we restrict these propositions to the form ‘‘tool construct causes modeling goal construct.’’ More general propositions can be developed in conjunction with general theory and are considered outside the scope of this paper. Only non-continuous constructs were chosen.

Propositions are a form of integrating the kernel theories. When theory is developed by integrating other theories, its boundaries are restricted by the theory from which it was derived [20].

Constructs other than tool and modeling goal constructs have been identified as affecting modeling goals. If they affect the circumstances in which the design theory propositions would hold, they are described as boundaries.

## 4.2.1. Boundaries

Boundaries define the limits within which the design theory can be applied. They must be within the boundaries of the kernel theories. Here, we develop and explain five boundary conditions, as given in Table 3.

Structured models are useful in a wide range of domains and some evidence has shown that systems can be designed to help develop them. Unstructured models can be useful also, but early research into tools supporting unstructured models (such as that of Aytes) indicated that different issues are important for good design. Therefore, we focused on a product design theory for structured modeling. Within the domain where structured models are useful, its usefulness is dependent on choosing the right structured model for the task. The first boundary definition states precisely that the design theory applies to:

B1: domains where useful structured models can be identified.

In many design domains, groups of subject matter experts (SMEs) are the source of real world information. The needs of these domains differ from those where a single modeling expert is developing a system. We limit the scope of this ISDT to a second boundary condition:

B2: domains where input from a group of SMEs is beneficial.

Many GSS studies have confirmed that as group size increases the beneficial effects of GSS increase. However, most have been performed with fewer than

<table><tr><td colspan="2">Boundary conditions</td></tr><tr><td>B1</td><td>Domains where useful structured models can be identified</td></tr><tr><td>B2</td><td>Domains where input by a group of SMEs is beneficial</td></tr><tr><td>B3</td><td>Domains where group size is manageable and cost effective</td></tr><tr><td>B4</td><td>Domains where adequate facilitation and modeling expertise is provided</td></tr><tr><td>B5</td><td>Domains where usable interfaces can be designed</td></tr></table>

12 members [18], well below McGrath’s 25–35 range where groups are expected to lose their identity. The group modeling task has both divergent and convergent aspects. As group size becomes large, convergence becomes difficult. Some research has suggested that GSS may have a lower limit on group size. For example, Gallupe et al. found no effect when using GSS in a two-person group. Since not all group sizes produce effective results, we limit the scope of our design theory to:

B3: domains where group size is manageable and cost effective.

Facilitation can have a positive effect on group processes and group cohesion in meetings with or without GSS [1]. Dean and his colleagues have noted that groups also need modeling expertise. Therefore, smGSS usage should be limited to:

B4: domains where adequate facilitation and modeling expertise is provided.

User interfaces can be evaluated on the basis of five factors: time to learn, speed of performance, rate of errors by users, retention over time, and user satisfaction [43]. Further, user interface design may be dependent on trends in operating systems and other business software. smGSS are intended to be used by a general professional group and would benefit from being consistent with state of the art software. Some structured model types may be so complex that it is difficult to create a user interface appropriate for the general audience. However, an smGSS can only be effective within a fifth boundary condition:

B5: domains where usable interfaces can be designed.

## 4.2.2. Propositions

Although structured models are critical to many forms of systems design, the development of structured models is difficult. User and developers often speak differently about the same problems and have difficulty in communicating [42]. Further, in many business situations, no one SME has complete knowledge of a system, requiring the analyst to interview several experts and reconcile differences. JAD methods were introduced to allow several SMEs to meet with analyst(s) in order to increase modeling efficiency, participation, and error control. However, these meeting processes are also inefficient. But if SMEs can enter model information directly into a shared format, communication problems can be reduced. Therefore:

P1: Direct group member editing of a shared model can increase modeling productivity, model quality, and participant understanding.

Anonymity in computer-mediated groups can lead to higher quality idea generation [11], by allowing candid, task-focused communication. However, research on anonymity has had mixed results that have been attributed to the context of the studies [39]. In socially sensitive contexts, anonymity is useful, but in less sensitive, expertise-driven contexts, anonymity can be an inhibitor. Although the lack of identified input should not be confused with anonymity, it is one factor that can improve anonymity.

P2a: Identified input can decrease model quality in socially sensitive contexts.

P2b: Identified input can increase model quality when individual expertise is critical.

Parallel input has been shown as a factor in increasing modeling efficiency and individual participation. Parallel contribution dissipates problems of production blocking that could limit an individual’s ability to contribute and adversely affect the quality of outcomes.

P3: Parallel input can increase modeling productivity and model quality.

Hierarchical decomposition is a fundamental tool; expressing a functional architecture as systems made up of components is a valid paradigm [44]. In collaborative modeling, large groups developing large models can be difficult to manage. Hierarchical decomposition helps manage the complexity of the group process by creating submodels that subgroups can work on in parallel.

P4: Hierarchical modeling structures can increase modeling productivity and model quality.

Groups are likely to develop models that contain syntactic errors. Although a common modeling goal is to correct syntactic errors, the enforcement of syntax rules in the early stage of model building can impede progress. Tool support for syntax checking can aid users in identifying syntax errors, but can also distract users [12]. Therefore, a tool needs to support ondemand syntax checking.

P5a: Tool support for syntax checking can increase syntactic correctness.

P5b: Tool support for syntax checking can decrease modeling productivity.

P5c: Tool support for on-demand syntax checking can reduce the decrease in group productivity caused by syntax checking.

Semantic correctness is another important aspect of model quality. Allowing semantic errors to grow unchecked can make them extremely difficult to correct later and can make them impossible for analysts to correct alone. However, correcting all semantic errors immediately can drastically impede model development productivity. On-demand semantic checking can achieve a balance between productivity and semantic correctness.

P6a: Tool support for semantic checking can increase semantic correctness.

P6b: Tool support for semantic checking can decrease modeling productivity.

P6c: Tool support for on-demand semantic checking can minimize losses in group productivity caused by semantic checking.

If SMEs are expected to follow a strict complex syntax, they are likely to reject a system. However, if they use free-form graphical tools, the collaboration process becomes unmanageable [3]. Dean and his colleagues demonstrated how to represent an activity model as a textual hierarchy with a formbased interface for entering activities and activity details. This approach labels each data item, reducing the need for users to remember syntax and hiding the complexity of model element relationships at points in the process where the information is not needed.

P7: A form-based textual editing user interface can increase modeling productivity.

SMEs prefer to use graphical views of models, as well as text views. Although data entry may be easier in text format, understanding of the models is often easier in graphical format. In cases where group composition changes over time or models already exist, SMEs may have substantial previous work to review. Dean and his colleagues used a system that produced delayed printed graphical model views and found the delays resulted in the printed views not always being consistent with the working model, which reduced productivity.

P8: A real-time graphical model view can increase participant understanding and productivity.

Much facilitation occurs without the use of a GSS, such as in face-to-face (FTF) meetings where the facilitator reviews the agenda or arbitrates a conflict. Facilitation can be enhanced with tools such as audio or video transmission and can be done by trained people or by the group. Facilitation support in the form of access control needs to be incorporated into the GSS. This allows the facilitator to choose the views and privileges of the SMEs, thereby increasing facilitation effectiveness.

P9: Access control can increase modeling productivity.

Editing awareness gives user information on current or previous changes, which reduces duplication of effort and helps users organize change review. Such awareness features can contribute to productivity and become increasingly important in distributed processes. Propositions are summarized in Table 4.

P10: Editing awareness can increase modeling productivity.

## 4.2.3. Meta-requirements

We next derive 10 meta-requirements which are summarized in Table 5. P1 leads to meta-requirement 1 (MR1): an smGSS should support a structured model representation, and MR2: an smGSS should support update of model representations by multiple users.

P2 implies different requirements for different contexts resulting in MR3a: an smGSS should support unidentified computer input in socially sensitive contexts, and MR3b: an smGSS should support identified computer input in expertise driven contexts.

P3 indicates the need for MR4: an smGSS should support parallel user input.

Table 4 smGSS design theory propositions

<table><tr><td>P1</td><td>Direct group member editing of a shared model can increase modeling productivity, model quality, and participant understanding</td></tr><tr><td>P2a</td><td>Identified input can decrease model quality in socially sensitive contexts</td></tr><tr><td>P2b</td><td>Identified input can increase model quality when individual expertise is critical</td></tr><tr><td>P3</td><td>Parallel input can increase modeling productivity and model quality</td></tr><tr><td>P4</td><td>Hierarchical modeling structures can increase modeling productivity and model quality</td></tr><tr><td>P5a</td><td>Tool support for syntax checking can increase syntactic correctness</td></tr><tr><td>P5b</td><td>Tool support for syntax checking can decrease modeling productivity</td></tr><tr><td>P5c</td><td>Tool support for on-demand syntax checking can reduce the decrease to productivity caused by syntax checking</td></tr><tr><td>P6a</td><td>Tool support for semantic checking can increase semantic correctness</td></tr><tr><td>P6b</td><td>Tool support for semantic checking can decrease modeling productivity</td></tr><tr><td>P6c</td><td>Tool support for on-demand semantic checking can minimize losses in productivity caused by semantic checking</td></tr><tr><td>P7</td><td>A form-based textual editing user interface can increase modeling productivity</td></tr><tr><td>P8</td><td>A graphical model view can increase participant understanding and modeling productivity</td></tr><tr><td>P9</td><td>Access control can increase modeling productivity</td></tr><tr><td>P10</td><td>Editing awareness can increase modeling productivity</td></tr></table>

P4 indicates the need for MR5: an smGSS should support hierarchical decomposition. When hierarchical decomposition is available, it should be supported in the system. When it is not, hierarchical decomposition should be added to the representation to achieve the goals of P4.

P5a, P5b, and P5c indicate the need for MR6: an smGSS should support on-demand syntax checking. Implied in this is support for entry of models with incorrect syntax.

P6a, P6b, and P6c indicate the need for MR7: an smGSS should support on-demand semantic checking.

Implied in this is support for entry with incorrect semantics.

P7 indicates the need for MR8: an smGSS should support a forms-based user interface for model editing. P8 indicates the need for MR9: an smGSS should support a graphical model view. P9 indicates the need for MR10: an smGSS should support access control.

P10 indicates the need for MR11: an smGSS should support indicators of when model elements are being edited, and MR12: an smGSS should sup port indicators of when model elements are being edited.

Table 5  
Meta-requirements for an smGSS

<table><tr><td></td><td>An smGSS should support</td><td>Primary propositions supported</td></tr><tr><td>MR1</td><td>A structured model representation</td><td>P1</td></tr><tr><td>MR2</td><td>Update by multiple users</td><td>P1</td></tr><tr><td>MR3a</td><td>Unidentified computer input in socially sensitive contexts</td><td>P2a</td></tr><tr><td>MR3b</td><td>Identified computer input in expertise driven contexts</td><td>P2b</td></tr><tr><td>MR4</td><td>Parallel user input</td><td>P3</td></tr><tr><td>MR5</td><td>Hierarchical decomposition</td><td>P4</td></tr><tr><td>MR6</td><td>On-demand syntax checking</td><td>P5c</td></tr><tr><td>MR7</td><td>On-demand semantic checking</td><td>P6c</td></tr><tr><td>MR8</td><td>A forms-based user interface for model editing</td><td>P7</td></tr><tr><td>MR9</td><td>A graphical model view</td><td>P8</td></tr><tr><td>MR10</td><td>Access control</td><td>P9</td></tr><tr><td>MR11</td><td>Indicators of when model elements are being edited</td><td>P10</td></tr><tr><td>MR12</td><td>Indicators of when modeling events have occurred</td><td>P10</td></tr></table>

Table 6  
Meta-design elements for an smGSS

<table><tr><td></td><td>smGSS artifacts</td><td>Primary meta-requirements supported</td><td>Contingent?</td></tr><tr><td>MD1</td><td>A structured model data structure</td><td>MR1</td><td>No</td></tr><tr><td>MD2</td><td>A forms-based interface for model editing</td><td>MR2, MR8</td><td>No</td></tr><tr><td>MD3</td><td>Concurrency control with locking at the model component level of granularity</td><td>MR2, MR4</td><td>No</td></tr><tr><td>MD4</td><td>A user identity property within the structured model data structure</td><td>MR3b</td><td>Yes</td></tr><tr><td>MD5</td><td>A user identity data structure</td><td>MR3b</td><td>Yes</td></tr><tr><td>MD6</td><td>A hierarchical relationship data structure</td><td>MR5</td><td>No</td></tr><tr><td>MD7</td><td>Syntax logic rules</td><td>MR6</td><td>No</td></tr><tr><td>MD8</td><td>Control of application of syntax logic rules</td><td>MR6</td><td>No</td></tr><tr><td>MD9</td><td>Semantic logic rules</td><td>MR7</td><td>No</td></tr><tr><td>MD10</td><td>Control of application of semantic logic rules</td><td>MR7</td><td>No</td></tr><tr><td>MD11</td><td>A graphical model view</td><td>MR9</td><td>No</td></tr><tr><td>MD12</td><td>Graphical layout generation logic</td><td>MR9</td><td>No</td></tr><tr><td>MD13</td><td>An access control data structure</td><td>MR10</td><td>No</td></tr><tr><td>MD14</td><td>A user interface for setting access control</td><td>MR10</td><td>No</td></tr><tr><td>MD15</td><td>User interface indicators of locked model elements</td><td>MR11</td><td>No</td></tr><tr><td>MD16</td><td>User interface indicators of model elements that have been edited since last viewing</td><td>MR12</td><td>No</td></tr><tr><td>MD17</td><td>A data structure for storing each user&#x27;s access to model elements</td><td>MR12</td><td>No</td></tr></table>

## 4.3. Meta-design

Meta-design artifacts that support the meta-requirements are implementation technology independent. Some are always required, as indicated by the metarequirements, and some are contingent on other factors. The following section derives fourteen meta-design elements and their contingencies from the metarequirements given in Table 6.

MR1 indicates the need for MD1: a structured model data structure.

MR8 leads to MD2: a forms-based interface for model editing. MR2 and MR4 indicate the need for updates by multiple users simultaneously. Since users must be able to edit parts of the model in parallel with others, the granularity of concurrency control should be at the level of model element granularity. Since data items within an element are so closely tied, allowing simultaneous editing by multiple users could create inconsistently defined elements. Therefore, MD3 is needed: concurrency control with locking at the model component level of granularity.

MR3b directly indicates the need for MD4: a user identity property within the structured model data structure. This property would be updated by the system, rather than manually; therefore, the system must link the user to an editing session, indicating the need for MD5: a user identity data structure. MR3a indicates that MD4 and MD5 are not needed in socially sensitive contexts and are, therefore, contingent on context.

MR5 indicates the need for MD6: a hierarchical relationship data structure.

MR6 indicates the need for two meta-design elements, MD7: syntax logic rules, and MD8: control of application of syntax logic rules.

MR7 indicates the need for MD9: semantic logic rules, and MD10: control of application of syntax logic rules.

MR9 directly indicates the need for MD11: a graphical model view. However, since model information is entered in the forms-based user interface, the user does not specify specific graphical layouts. This leads to MD12: graphical layout generation logic.

MR10 indicates the need for MD13: an access control data structure. The facilitator sets access control, which leads to MD14: a user interface for setting access control.

MR11 indicates the need for MD15: user interface indicators of locked model elements.

MR12 indicates the need for MD16: user interface indicators of model elements that have been edited since last viewing. Since storage of information of what users have viewed must be maintained to display the indicators, MD16 implies a need for MD17: a data structure for storing each user’s access to model elements.

## 4.4. Testable design product hypotheses

Since a system needs to be built before its effect can be assessed, feasibility is a prerequisite for effectiveness, and positive results from feasibility testing are necessary before valid effectiveness test can be conducted. Feasibility hypotheses derive directly from each meta-design element. Feasibility hypotheses are tested by constructing and testing the relevant artifact, which should be tested for both feasibility and construct validity, relating the artifact to the meta-design element. Effectiveness hypotheses derive directly from the design theory propositions. Positive results provide evidence of the validity of the propositions and construct validity between the artifacts and the propositions. Meta-requirements are not tested directly. Negative results of effectiveness hypothesis testing could be the result of invalid propositions or an invalid derivation of the artifacts.

## 5. Conclusion

This paper developed a product design theory for smGSS which synthesizes and generalized previous research on GSS and modeling. The theory contributes by showing how collaborative structured modeling systems should be designed. Two important criteria in evaluation theories, in general, are falsifiability and utility. These should also be applied to design theories. By specifying falsifiable propositions, the design theory is falsifiable. Utility may be viewed as a link between explanation and prediction.

If smGSS studies use systems developed or compared to the product theory, then comparisons across experiments can be made. Further, in systems development studies that find systems changes must be done in mid-process to achieve results, this product theory can provide a point of reference for documenting how the system was changed. In referencing system changes to product design theory, researchers can interpret them as being implementation problems, identification of new constructs, or significant challenges to the theory.

To enhance internal and construct validity, specific links between design propositions, meta-requirements, meta-design, and design product hypotheses were demonstrated. This tight linkage can help ensure that systems derived from this design and their evaluation are valid. It should also be possible to discern the effect on tool design of new findings that might update the kernel theories.

## References

[1] R. Anson, R. Bostrom, B. Wynne, An experiment assessing group support systems and facilitator effects on meeting outcomes, Management Science 41 (2) (1995).

[2] K.J. Aytes, Comparing collaborative drawing tools and whiteboards: an analysis of the group process, Computer Supported Cooperative Work, 4 (1996).

[3] I. Benbasat, B. Konsynski, Introduction to special section of GDSS, MIS Quarterly 12 (4) (1988).

[4] I. Benbasat, L. Lim, The effects of group, task, context, and technology variables on the usefulness of group support systems, Small Group Research 24 (4) (1993).

[5] G.E. Bock, D.A. Marca, Designing Groupware: A Guidebook for Designers, Implementors, and Users, McGraw-Hill, New York, 1996.

[6] R.P. Bostrom, R. Anson, V.K. Clawson, Group facilitation and group support systems, in: L. Jessup, J. Valacich (Eds.), Group Support Systems: New Perspectives, Macmillan, New York, 1993.

[7] G.J. Brown, V. Ramesh, Improving information requirements determination: a cognitive perspective, Information and Management 39, 2002, pp. 625–645.

[8] E. Carmel, J.F. George, J.F. Nunamaker Jr., Examining the process of electronic JAD, Journal of End User Computing 7 (1) (1995).

[9] K.J. Chun, H.K. Park, Examining the conflicting results of GDSS research, Information and Management 33, 1998, pp. 313–325.

[10] V.K. Clawson, R.P. Bostrom, R. Anson, The role of the facilitator in computer-supported meetings, Small Group Research 24 (4) (November 1993).

[11] T. Connolly, L.M. Jessup, J.S. Valacich, Effects of anonymity and evaluative tone on idea generation in computer-mediated groups, Management Science 36 (6) (June 1990).

[12] D.L. Dean, J.D. Lee, R.E. Orwig, D.R. Vogel, Technological support for group process modeling, Journal of Management Information Systems 11 (3) (Winter 1994–1995).

[13] D.L. Dean, J.D. Lee, M.O. Pendergast, A.M. Hickey, J.F. Nunamaker Jr., Enabling the effective involvement of multiple users: methods and tools for collaborative software engineering, Journal of Management Information Systems 14 (3) (Winter 1997–1998).

[14] D.L. Dean, R.E. Orwig, D.R. Vogel, Facilitation methods for collaborative modeling tools, Group Decision and Negotiation 9 (2) (2000).

[15] D.L. Dean, M.O. Pendergast, K.J. Aytes, Computer-supported collaborative modeling: the enterprise analysis project, ACM Special Interest Group Bulletin (1997).

[16] A.R. Dennis, J.F. George, L.M. Jessup, J.F. Nunamaker Jr., D.R. Vogel, Information technology to support electronic meetings, MIS Quarterly 12 (4) (1988).

[17] A.R. Dennis, G.S. Hayes, R.M. Daniels, Business process modeling with group support systems, Journal of Management Information Systems 15 (4) (Spring 1999).

[18] A.R. Dennis, J.S. Valacich, J.F. Nunamaker Jr., An experimental investigation of the effects of group size in an electronic meeting environment, IEEE Transactions on Systems, Man, and Cybernetics 25 (5) (1990).

[19] A. Dillon, Designing Usable Electronic Text: Ergonomic Aspect of Human Information Usage, Taylor & Francis, Southport, England, 1994.

[20] R. Dubin, Theory Building, Free Press, New York, 1978.

[21] R.B. Gallupe, A.R. Dennis, W.H. Cooper, J.S. Valacich, L.M. Bastianutti, J.F. Nunamaker Jr., Electronic brainstorming and group size, Academy of Management Journal 35 (2) (1992).

[22] R.B. Gallupe, G. DeSanctis, G.W. Dickson, Computer-based support for group problem finding: an experimental investigation, MIS Quarterly 2 (2) (1988).

[23] J.F. George, An examination of four GDSS experiments, Journal of Information Science 18 (1992).

[24] J.R. Hackman, C.G. Morris, Group tasks, group interaction process, and group performance effectiveness: a review and proposed integration, in: L. Berkowitz (Ed.), Advances in Experimental Social Psychology, vol. 8, Academic Press, Orlando, FL, 1975.

[25] A.M. Hickey, D.L. Dean, J.F. Nunamaker Jr., Establishing a foundation for collaborative scenario elicitation, The DATABASE for Advances in Information Systems 30 (3–4) (1999).

[26] G.W. Hill, Group versus individual performance: are N þ 1 heads better than one? Psychological Bulletin 91 (3) (1982).

[27] J.A. Hoffer, J.F. George, J.S. Valacich, Modern Systems Analysis and Design, third ed., Prentice-Hall, Upper Saddle River, NJ, 2001.

[28] L.M. Jessup, T. Connolly, J. Galegher, The effects of anonymity on GDSS group process with an idea-generating task, MIS Quarterly 14 (3) 313–322.

[29] W.J. Kettinger, J.T.C. Teng, S. Guha, Business process change: a study of methodologies, techniques, and tools, MIS Quarterly 21 (1) (March 1997).

[30] J.D. Lee, D.L. Dean, D.R. Vogel, Tools and methods for group data modeling: a key enabler of enterprise modeling, SIGGROUP Bulletin 18 (2) (August 1997).

[31] M.L. Markus, A. Majchrzak, L. Gasser, A design theory for systems that support emergent knowledge processes, MIS Quarterly 26 (3) (2002).

[32] J.E. McGrath, Social Psychology: A Brief Introduction, Holt, New York, 1964.

[33] J.E. McGrath, Groups: Interaction and Performance, Prentice-Hall, Englewood, NJ, 1984.

[34] S.M. Miranda, R.P. Bostrom, Meeting facilitation: process vs. content intervention, Journal of Management Information Systems 15 (4) (1999).

[35] J.F. Nunamaker Jr., Build and learn, evaluate and learn, Informatica 1 (1) (December 1992).

[36] J.F. Nunamaker Jr., A.R. Dennis, J.S. Valacich, D.R. Vogel, J.F. George, Electronic meeting systems to support group work, Communications of the ACM 34 (7) (1991).

[37] J.F. Nunamaker Jr., A.R. Dennis, J.S. Valacich, D.R. Vogel, J.F. George, Group support systems research at Arizona: experience from the lab and field, in: L.M. Jessup, J.S. Valacich (Eds.), Group Support Systems: New Perspectives, Macmillan, New York, 1993.

[38] M.O. Pendergast, GroupGraphics: prototype to product, in: Proceedings of the Workshop on Multi-user Drawing Tools, Conference on Computer-Supported Work, Toronto, Canada, 1992.

[39] A. Pinsonneault, N. Heppel, Anonymity in group support systems research: a new conceptualization, measure, and contingency framework, Journal of Management Information Systems 14 (3) (1997–1998).

[40] A. Pinsonneault, K.L. Kraemer, The impact of technological support on groups: an assessment of the empirical research, Decision Support Systems 5 (2) (1989).

[41] L.L. Putnam, C. Stohl, Bona fide groups, in: R.Y. Kirokawa, M.S. Poole (Eds.), Communication and Group Decision Making, second ed., Sage, Thousand Oaks, CA, 1996.

[42] D.T. Ross, K.E. Schoman Jr., Structured analysis for requirements definition, IEEE Transactions on Software Engineering 3 (1) (1977).

[43] B. Shneiderman, Designing the User Interface, Addison-Wessley/Longman, Reading, MA, 1988.

[44] I.D. Steiner, Group Process and Productivity, Academic Press, New York, 1972.

[45] M. Turoff, S.R. Hiltz, A.N.F. Bahgat, A.R. Rana, Distributed group support systems, MIS Quarterly 17 (4) (December 1993).

[46] J.S. Valacich, J.F. George, J.A. Hoffer, Essentials of Systems Analysis and Design, second ed., Prentice-Hall, Upper Saddle River, NJ, 2004.

[47] J.S. Valacich, B.C. Wheeler, B.E. Mennecke, R. Wachter, The effects of numerical and logical group size on computermediated idea generation, Organizational Behavior and Human Decision Processes 62 (3) (June 1995).

[48] J.G. Walls, G.R. Widemeyer, O.A. El Sawy, Building an information system design theory for vigilant EIS, Information Systems Research 3 (1) (March 1992).

[49] I. Zigurs, B. Buckland, A theory of task/technology fit and group support systems effectiveness, MIS Quarterly 3 (September 1998).

![](/api/attachments/NXYTF8NR/fulltext/images/284cb786ad132bebe5ef6db6c3cff01278648419d82b18d0c8ab23c04985e074.jpg)  
Kenneth R. Walsh is an assistant professor of information systems in the Management Department of the College of Business at University of New Orleans. He received his PhD in management information systems from the University of Arizona. He has published in Communications of the ACM, Communications of the AIS, and Journal of Computer Information Systems, among others. His research interests include virtual reality, group support systems, and electronic commerce.

![](/api/attachments/NXYTF8NR/fulltext/images/cec1da96851fb30a7a380293fa36d1d3b0bb0e7116afb87c7d7a9b58f14b4774.jpg)  
Michael H. Dickey is an assistant professor in the Management Information Systems Department of the College of Business at Florida State University. She received her PhD in management information systems from Louisiana State University, Baton Rouge, LA. Her research interests include virtual work environments, the use of language in electronic communications, and the organizational impact of information systems, including in franchise organizations and global environmental movements.
