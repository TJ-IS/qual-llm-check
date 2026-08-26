---
otero_id: 11260
otero_key: "YFCDTEVN"
title: "Designing IT systems according to environmental settings: A strategic analysis framework"
authors: "He Zhang; Lin Liu; Tong Li"
year: "2011"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/j.jsis.2011.01.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Designing IT systems according to environmental settings: A strategic analysis framework

He Zhang, Lin Liu ⇑, Tong Li

School of Software, Tsinghua University, Beijing 100084, China

## a r t i c l e i n f o

Article history: Available online 24 February 2011

Keywords: Requirements Modeling Goals Environment Impact

## a b s t r a c t

In the past, IT system design is mainly driven by two essential factors: technical merits and costs. Environmental consideration only emerges in most recent discussions under the label of green IT. As the evaluation of environmental and climate impact involves too many parameters, some of which are indirect and hidden, it is very hard to make rationale analysis without the support of a holistic strategic analysis framework. In this paper, we propose to extend the goal-oriented requirements modeling language, GRL, to model the rationality behind IT system design, in particular, how the environment related considerations come into play in such design decision making. It can be adopted as a strategic analysis framework to facilitate concrete decision makings under different environmental settings. Example real world scenarios are used to illustrate how the proposed approach can help improve the state of the practice.

\- 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Nowadays, more and more enterprises begin to realize that they have to pay dearly for the negative environmental impact they have done. For example, information and communication systems account for 2–2.5% of the global carbon emissions, but if indirect energy use were included, the total carbon emissions would be responsible for as high as 14% of the global total carbon emissions. (ITU-T, 2007). The e-waste problem caused by the massive use of IT equipments also results in tremendous environmental crisis. About 500 million PCs reached the end of their service lives between 1994 and 2003. Five hundred million PCs contain approximately 2872,000 t of plastics, 718,000 t of lead, 1363 t of cadmium and 287 t of mercury (Puckett and Smith, 2002). The IT related environmental problems are undoubtedly one of the major rising concerns for both the IT society and the general public.

So far, most of the environmental regulations and controlling measures only focus on the IT equipment manufactures. But just as in (Princen et al., 2002), environmental problems nowadays is more closely related to the unsustainable trends in consumption rather than the human population, technology and supply. Specifically, for the IT system, the system owner’s design decision is of great importance to the system’s overall environmental impact. As Kohler and Erdmann summarized (Köhler and Erdmann, 2004), there are three levels of environmental impact involved, namely, the environmental impact resulting from the hardware’s full lifecycle, the changing of other related non-IT processes, and the changing to people’s daily life, economic structures and lifestyles. A good system design could not only minimize the overall environmental impact and lower the owner’s future environmental risks, but also result in improved corporate social responsibility and increased competitive advantage.

This paper aims at providing a framework to support the IT system design decision support based on the system’s environmental impact. In practice, there are several kinds of existing tools and methods to assist the designer and system owner investigating the IT system’s environmental impact in the designing stage, for instance, environmental life cycle assessments (Robin and Davidson, 2001) and EPEAT green electronics product list (EPEAT, 2006). These tools and methods are powerful, but mostly focusing on the product level and hard to provide a holistic view of the system’s overall environmental impact. In our approach, we take the negative environmental impact as a kind of system non-functional requirements, and illustrate the environmentally concerned IT system design decision-making process based on the extended goal-oriented requirements modeling language (GRL) (Liu and Yu, 2004). Designing for environmental protection amounts to the answering of questions such as: ‘‘who is likely to care about the greening of the system? Who is influenced by the greening of the system? Who will pay for the expense of environmental cost? What are the short-term expenses of greening the system, and what are the long term benefits? What is the risk of not greening? What are the side effects of adding particular countermeasures?’ Yet, there is no systematic analysis technique through which one can go from answers to these questions to particular greening solutions. Our proposal is intended to provide mechanisms that explicitly relate social, economical, environmental concerns with the technologies and policies addressing these concerns.

The framework offers a set of environmental requirements analysis facilities to help the stakeholders better understand the various environmental expense they face, the countermeasures they can take, and how these can be combined to achieve the desired optimization results within the broader picture of system design and the business environment. The proposed environment requirements analysis is illustrated with the example of a management information system design for an organization.

The paper will be organized as follows: Section 2 introduces the basic requirement analysis process supported by GRL. Section 3 discusses the extended modeling process and a set of environment-related analysis techniques. Section 4 describes a running example explaining the proposed quantitative model evaluation technique. Sections 5 and 6 discuss related work and summarize the results of the paper.

## 2. The goal-oriented requirements language (GRL) modeling notation

The goal-oriented requirements language (GRL) is a language for supporting goal and agent oriented modeling and reasoning about requirements, with an emphasis on dealing with non-functional requirements (NFRs) (Chung et al., 2000). It provides constructs for expressing various types of concepts that are useful for supporting the requirements and high level design process. There are three main categories of concepts: intentional elements, intentional links, and actors. GRL elements and links are strategic and intentional in that they are used in models that answer questions about intents, motivations and rationales, such as:

\- Why are particular behaviors, information and structures chosen to be included in the system requirements?

\- What are the alternatives to be considered?

\- What criteria are to be used to deliberate among alternative options?

\- What are the reasons for choosing one alternative over others?

A GRL model can be composed of either a global goal model, or a series of goal models distributed amongst several actors. If a goal model includes more than one actor, then the intentional dependency relationships between actors can also be represented and reasoned about.

The intentional elements in GRL are goal, task, softgoal, resource and belief. A goal is a condition or state of affairs in the world that the stakeholders would like to achieve. For instance, the element ‘‘Document Be managed’’ is a goal to be achieved by an actor ‘‘Document Owner’’. A goal can be either a business goal or a system goal. Business goals are about the business or state of the affairs the individual or organization wishes to achieve in the world. System goals are about what the target system should achieve, which, generally, describe the functional requirements of the target information system. In GRL graphical representation, goals are represented as a rounded rectangle with the goal name inside.

A softgoal is typically a quality (or non-functional) attribute on one of the other intentional elements. A softgoal is similar to a (hard) goal except that the criteria for whether a softgoal is achieved are not clear-cut and a priori. It is up to the developer to judge whether a particular state of affairs in fact sufficiently achieves the stated softgoal. Non-functional requirements (NFRs), such as performance, security, accuracy, reusability, interoperability, time-to-market and cost are often crucial for the success of an information system. In GRL, non-functional requirements are represented as softgoals and addressed as early as possible in the software lifecycle. They should be properly modeled and addressed in design reasoning before a commitment is made to a specific design choice. In the GRL graphical representation, a softgoal, which is ‘‘soft’’ in nature, is shown as an irregular curvilinear shape with the softgoal name inside. As we can see from the model in Fig. 1. “Low GHG Emissions’’ and ‘‘Low Electricity Consumption’’ are both modeled as softgoals.

A goal can be achieved in different ways, prompting alternatives to be considered. A task specifies a particular way of doing something. There are two different means for accomplishing the document owner’s business goal ‘‘Document be managed’’, are represented as task ‘‘Use Paper-Based Document System’’, and task ‘‘Use Electronic Document System’’. Tasks are connected to the goal with means-ends links. It may be decomposed into a combination of subgoals, sub-tasks, resources and softgoals. The task ‘‘Use Paper-based Document System’’ is decomposed into two sub-components (connected with task decomposition links): the sub-task of ‘‘Manufacturing and Disposal of Paper’’ and ‘‘Print Document’’. The decomposition relationship concerns more on the strategic and intentional sub-components of a task than the sub-procedure or concrete data components. These sub-components specify a particular course of action while still allowing some freedom. Tasks are used to incrementally specify and refine solutions in the target system. They are used to achieve goals or to ‘‘operationalize’’ softgoals. These solutions provide operations, processes, data representations, structuring, constraints and agents in the target system to meet the needs stated in the goals and softgoals. In GRL graphical representation, tasks are represented as a hexagon with the task name inside.

![](/api/attachments/YFCDTEVN/fulltext/images/a9136edb2d98b63c053a606ad19b305a1a153de33494a79e741721eaa65d262e.jpg)  
Fig. 1. Example GRL strategic rationale (SR) analysis model.

A resource is a (physical or informational) entity, which may serve some purpose. From the viewpoint of intentional analysis, the main concern with a resource is whether it is available. Resources are shown as rectangles in GRL graphical representation. When the tasks are further decomposed, entities such as ‘‘documents’’, ‘‘paper’’, ‘‘devices’’ can be modeled as resources, being sub-component of the tasks mentioned previously.

The Belief construct is used to represent design assumptions and relevant environmental conditions. It allows domain characteristics to be considered and properly reflected in the decision-making process, hence facilitating later review, justification and change of the system, as well as enhancing traceability. Beliefs are shown as ellipses in GRL graphical representation.

The intentional links in GRL include means-ends, decomposition, contribution, correlation and dependency links. Meansends links ( ) are used to describe how goals can be achieved. Each task connected to a goal by a means-ends link is one possible way of achieving the goal. Decomposition links ( ) define the sub-components of a task. A contribution link (?) describes the impact that one element has on another. A contribution can be negative or positive and can be of different extents. The extent is judged to be partial or sufficient based on Simon’s concept of satisficing [16]. Accordingly, contribution link types include: help (positive and partial), make (positive and sufficient), hurt (negative and partial), break (negative and sufficient), some + (positive of unknown extent), some – (negative of unknown extent). Correlation links (dashed contribution links) describe the side effects of the existence of one element to others. Dependency links ( ) describe the inter-agent dependent relationships.

An actor is an active entity that carries out actions to achieve its goals by exercising know-how. It is an encapsulation of intentionally, rationality and autonomy (Yu, 1997). Graphically, an actor is represented as a circle, and may optionally have a dotted boundary, with intentional elements inside. To model complex relationships among social actors, we further define the concepts of agents (circle with a line at top), roles (circle with a line at bottom), and positions (four-leaf flower), each of which is an actor in a more specialized sense.

The strategic rationale (SR) analysis of GRL provides a detailed level of modeling by looking ‘‘inside’’ actors to model internal intentional relationships. Intentional elements (goals, tasks, resources, and softgoals) appear in SR models as internal elements arranged into a hierarchy of means-ends, task decompositions and contribution relationships.

The positive contribution types for softgoals are help (positive but not by itself sufficient to meet the higher goal), make (positive & sufficient) and some + (positive in unknown degree). The corresponding negative types are Hurt, Break and Some-. ‘‘And’’ means if all subgoals are met, then the higher goal will be sufficiently met. ‘‘Or’’ means the higher goal will be sufficiently met if any of its subgoals are met. During system analysis and design, softgoals such as low GHG emissions are systematically refined until they can be operationalized, implemented or quantified. Unlike functional goals, nonfunctional qualities represented as softgoals frequently interact or interfere with each other, so the graph of contributions is usually not a strict tree structure.

With SR models like Fig. 1, we can reason about each alternative’s contributions to high-level non-functional quality requirements including low environmental impact, which helps to make a more favorable choice among existing options.

## 3. An environment-driven strategic analysis approach based on GRL

In this section, we will introduce an environment-driven strategic analysis approach based on GRL. This quantitative strategic analysis is capable of exploring the hidden environmental impact of the IT systems, and could help the stakeholders to make rational decisions in green IT system design.

As explained in the previous section, GRL is often used for the reasoning of requirements, and especially with nonfunctional requirements (NFRs). We find the IT systems’ environment-friendliness requirements can be seen as a kind of NFR. By adopting the GRL modeling technique, the IT system stakeholders could make the hidden environmental impact explicit, and gain a holistic view of the system’s overall environmental impact during the system design stage. The stakeholders could then get a quantified understanding of the estimate environmental impacts of their system design alternatives and make strategic decisions based on the GRL models and with the help of the quantitative calculation models.

In the following parts of this section, we will begin with introduce the general framework under which the system’s environmental-friendliness NFR can be studied. After that, a quantitative GRL modeling and design decision making approach will be explained with a simple case study.

## 3.1. Environmental-friendliness as one of the competing NFRs

Environment-friendliness can be seen as a kind of IT system NFR. Like safety, cost and user-friendliness, the IT system owners and designers have great concerns about their systems’ negative environmental impact. These concerns have made the environment-friendliness becoming a popular kind of IT system design requirements nowadays. How to analyze the IT system design alternatives against their environment-friendliness NFRs is a problem that the system designer faces.

In this part, we built a topology to support the quantitative analysis for the IT system’s first order (direct) environmental impact. But as the previous studies in green ICT have pointed out, the IT system’s environmental impact may become hard to predict as the system gets complicated and intervenes with the second (indirect) and third order environmental impacts (Köhler and Erdmann, 2004). We have identified two particular challenges that may have caused the design decisions hard to make for the complicated IT system.

When it comes to reducing the negative environmental impact of the information systems, green IT is usually mentioned as a major solution to the problem. Regarding only the direct environmental impact of IT system, Green IT is described as ‘‘the study and practice of designing, manufacturing, using, and disposing of computers, servers, and associated subsystems—such as monitors, printers, storage devices, and networking and communications systems—efficiently and effectively with minimal or no impact on the environment.’’ (Murugesan, 2008) Based on this understanding, we have built a goal decomposition structure to summarize the common kinds of IT system environment impacts as shown in Fig. 2. In this struc ture, the top level softgoal ‘‘Low Negative Environment Impact’’ can be decomposed into several levels of detailed softgoals And eventually, the relevant resources and tasks.

Based on this structure, the direct environmental impact of an IT system could be estimated. A straightforward way of analyzing the system against its environmental NFRs would be using the quantitative calculation models to replace the contribution links and calculate the system’s various environmental impacts. But when the system gets complicated, the analysis usually hard to carry out or to provide accurate results for design decision making

One challenge for analyzing complicated IT systems is the complexity in stakeholder relations. Complicated IT system is not only large in scale, but also complicated in the inter-relations among the various stakeholders. For example an application on a cloud computing platform meshing up several web services is hard very hard to analyze its environmental impact. Under such circumstances, the system boundary is hard to identify and the decision makers hard to obtain a holistic view of the system. As a result, the analysis is usually limited by the decision makers’ own understanding of the system.

Another challenge for analyzing complicated IT systems and for making design decision is to deal with the relationships with other competing NFRs. There are many kinds of trade-off and mutually enhancing relationships between the system’s environmental requirements and other kinds of NFRs. How to balance the different kinds of NFRs and make clear design is a major problem for the system designers and stakeholders.

Fig. 3 shows some possible relationships between the environment-friendliness softgoal and other NFR softgoals. As the figure indicates, these relationships are not always clear. For Example, the ‘‘Low Negative Environmental Impact’’ softgoal may cost the enterprise more money to implement an environment-friendly IT system. But on the other hand, if we put some parts of the long term hidden environmental cost (e.g. future environmental taxes and related compensations) into consideration, the overall own and operation cost of the IT system may be lower than the systems without the environmentalfriendly design. Therefore, in order to make sound design decisions, a comprehensive yet flexible quantitative analysis framework need to be provided.

As introduced in the previous section, GRL is often used for analyzing IT system against their NFRs in Requirements Engineering. GRL modeling could help the decision makers to generate a holistic picture of the system by exploring the dependency relations between the various stakeholders. Besides, GRL can also provide the stakeholders with a flexible design decision making support balancing the various IT system design requirements and goals.

![](/api/attachments/YFCDTEVN/fulltext/images/db9ff15f6004cf50fe0f631ae90a8e1786bb837ac1f51e89382def526246dbdf.jpg)  
Fig. 2. Environmental softgoal decomposition structure for IT systems.

![](/api/attachments/YFCDTEVN/fulltext/images/0fca7130a5bc1dfd6140d54e7ebee881e0d1d7baa36370f46a7f4636418e66b5.jpg)  
Fig. 3. Environment-friendliness as a competing non-functional requirement.

We find the GRL modeling technique could also be used to support design decision making related to the IT system environment-friendliness requirements. In the following parts of this section, we will use a simple case study to illustrate the major modeling techniques of the GRL-based system strategic analysis and to proof the effectiveness of this approach.

## 3.2. Quantitative analysis for green IT design based on GRL

Quantitative analysis for IT system against their environment-friendliness NFRs can help the system designers to estimate the environmental impact of their system design alternatives. In this part, we will introduce how the GRL SR model can be extended to carry out the quantitative analysis for green IT system design decision making.

In our proposed case study, a small work group in China is making decisions on how to manage their documents. The work group now has two choices: one is to keep on using their paper-based document system: the other is to upgrade to an electronic document management system. The group members all hope the new document management system could be both cost-effective and environment-friendly. If they choose to use the electronic document system, the document storage service will be provided by the organization’s IT supporting team. Fortunately, the IT supporting team also has paid close attention to greening their IT facilities. They have acquired the basic knowledge of installing and managing virtual server in order to reduce their IT systems’ environmental footprint.

The GRL model in Fig. 1 shows the design alternatives for the document management systems. Within the document owner’s boundary, the goal ‘‘Documents be Managed’’ has been decomposed into two alternative tasks ‘‘Use Paper-Based Document System’’ and ‘‘Implement Electronic Document System’’. And each task has also been decomposed into even smaller tasks explaining how the parent task is being operationalized. The bottom-level task for the document owner ‘‘Store and Manage e-Document’’ has a dependency link links to the document storage service provider, illustrating the work group depends on the IT supporting team to store and manage the electronic documents. Inside the documents storage service provider’s boundary, the service could be delivered using either virtual server or stand-alone server.

To carry out the quantitative analysis, it is important to first learn the stakeholders’ most critical environmental concerns. Environmental issues are quite complicated and covering a large variety of different aspects. It is hard for a single organization or party to tackle all the environmental problems at one time. As a result, most of the environmental-concern companies tend to select the most important environmental issues and make strategies according to their unique circumstances.

After the environmental concerns being identified, a set of user-specific environmental NFRs can be selected from the softgoal structure of Fig. 2. In the document management case study, the stakeholders both interested in reducing the climate change effect of their IT system. Therefore, the ‘‘Low GHG Emissions’’ and its decedent softgoals are selected to build the customized environmental requirements tree. As the requirements being built, the relationships between these bottomlevel tasks and the softgoal structure could be identified, and their inter-relationships could then be marked with the GRL contribution links (shown in Fig. 4).

With the help of GRL models, we could generate a holistic view of the system with the IT system design objectives, design alternatives and the user-specific environmental NFRs. But it is still not enough for measuring and comparing the various system design alternatives. To support design decision making, a detailed quantitative analysis is necessary to estimate the system design’s overall environmental impact.

Fig. 4 shows the quantitative analysis result of the tasks in the GRL model. Based on the GRL model structure, the contribution links between the bottom-level tasks and the environmental NFRs and the decomposition links between the environmental NFRs are replaced by existing quantitative calculation models. In this way, a quantitative analyze model can be built for the system under study. Take the example of the relationship between the task ‘‘Manufacturing and Disposal of Paper’’ and the softgoal ‘‘Low GHG Emissions’’, the contribution link is replaces by a model calculating carbon footprint for paper production and disposal. After setting the paper type (80 g/m<sup>2</sup>, 100% Recycle Paper) and annual paper consumption (10,000 pages), the model could calculate the estimate annual GHG emission of the paper producing and disposal is 893.64 kgCO -e. In this way, the quantitative models collect their input data and calculate the estimate annual GHG emissions of each bottom-level task.

In brief, the design decision makers could use GRL modeling to discover the IT system’s boundary, and generate design alternatives according to the business objectives. After that, the GRL model could be used as a framework to combine use the existing environmental quantitative calculation models to estimate the quantified environmental impact of each individual task in the design alternatives. This quantified environmental impact can then be used to help IT system designers and stakeholders to make design decisions.

![](/api/attachments/YFCDTEVN/fulltext/images/dd176dab1327714e5553e57652c92a23c4563e231cb7d19b1cb85fcd068acfdf.jpg)  
Fig, 4. Environmental quantitative analysis for each task in the GRL model (data source: HP, 2010: Dell, 2010: Clean Tech Group LLC, 2009: IEA, 2010: EDO. 2007).

## 3.3. Strategic design decision making for green IT design

Based on the quantified results, stakeholders and system designers can work together to analyze and improve the IT system design alternatives, and to make strategic design decision to better comply with the system’s environment-friendliness requirements.

According to the AND, OR relations between tasks in the GRL model, the composition of each design solution can be recognized. Using the quantitative analysis result introduced in the last part of this section, we could estimate the overall envi ronmental impact of each design solution.

As Fig. 5 depicts, three design alternatives can be identified form the GRL model with their estimate total ${ \mathsf { C O } } _ { 2 }$ emissions. If the document owner is the one makes the decision and it only pays attention to the IT system fragment inside its boundary, design alternatives 2 and 3 may be more attractive in terms of ${ \mathsf { C O } } _ { 2 }$ emissions. While if the stakeholders making their design decisions according to the Green IT technology usage, design alternative 2 may surpass the other two to be the best choice. In this case, the document owner believes it has saved 122 $\mathrm { k g C O } _ { 2 ^ { - } }$ e annually by implement ‘‘paperless office’’ and the document storage service provider could also clam that they have saved 1162 kg $\mathsf { \Delta } _ { - } \mathsf { O } _ { 2 } { - } \mathsf { e }$ annually with the virtual server technique However, with the help of GRL model. it is obvious to identify that the design alternative 3 is the most environmentalfriendly design in terms of ${ \mathrm { C O } } _ { 2 }$ emissions.

From the case study, we could learn that using Green IT checklist or performing quantitative analysis for individual stakeholders may not be able to generate the best decisions. However, by GRL modeling, the stakeholders could make some of the environmental impact explicit, and generate a holistic view of the system for design decision making.

To balance the environmental requirements with other NFRs, the decision makers could use a similar approach to estimate the IT system’s satisfactory to other system NFRs. After that, each design solution’s NFRs quantitative analysis results could then be combined into vectors or a weighted sum for further comparison or improvement analysis:

<Management Cost (USD), Environmental Impact $( \mathsf { k g C O _ { 2 } - e } ) >$

(1) Paper-Based Document System: <250USD, 944.90 kg $\mathsf { T } 0 _ { 2 } \mathsf { - e } \mathsf { > }$

(2) Electronic Document System with Virtual Server: <137USD<sup></sup>, 1984.92 $\mathrm { k g C O } _ { 2 } – \mathrm { e } >$

(3) Electronic Document System with Stand-alone Server: <196USD<sup></sup>, 3146.94 kg $\mathsf { T O } _ { 2 } \mathsf { - e } >$

Note: <sup></sup>Not including upgrading reading devices.

In the document management case study, the stakeholder would like to balance the system environmental requirements with the system install and maintenance cost. The vectors above show the quantitative analysis result of the three design alternatives. In this kind of situations, the design decision makers could vote to make the selection. However, when the dimension of the vector is too high, a weighted sum formula could also be generated to represent the IT system’s overall satisfactory to this bunch of system NFRs.

In conclusion, reducing negative environmental impact can be treated as non-functional requirements (NFRs) for IT systems during the design stage. On one hand, GRL modeling explores the dependency relations between various stakeholders and make the hidden environmental impact explicit. It could help the decision makers to gain a holistic view of the system’s overall environmental impact. On the other hand, GRL modeling could also be used to balance between the IT system’s environmental requirements and other kinds of system NFRs.

![](/api/attachments/YFCDTEVN/fulltext/images/e527686341c3fd35763c48ec71bdd8717985c8de9ef3d61a129cb4f894396a57.jpg)  
Fig. 5. Design decision making for the document management system case study.

## 4. Environment-driven IT system design strategic analysis process

In the past section, we have introduced the basic idea and the capability of the environment-driven strategic analysis approach based on GRL, and used a simple case study to depict the effectiveness of such approach.

In this section, we will introduce the detailed process to carry out this strategic analysis. As shown in Fig. 6, the process consist of five steps starting from the identification of the IT system major design objectives to the design alternative improving and design decision making. We will explain in detail of how to build the user-specific analysis model for the IT system, how to evaluating environmental impact of each design alternatives, and how to refine and operationalize the design alter natives according to their NFRs. An example of enterprise information system is also provided to illustrate the implementation of the analysis process.

The example is the designing of an enterprise information system for a Chinese manufacturing company, adapted from (Li Dong, 2002). This company, NHX Co., is producing intermediate products for its parent company in Finland, collecting raw materials and spare parts from China, Japan and Finland, and exporting the finished product back to its parent company. The IT system under designing is the company’s management information system. This system is design to help the company to implement order management, production planning, inventory control and packaging and shipment management. The company is considering using mobile, bar code and RFID tagging techniques to improve their performance. Mean time, they are also considering using an online order approval process to replace their original process based on hand-signed papers. The parent company also has very strong environmental awareness, and requires the production of NHX Co. to be as environment-friendly as possible. This requirement from the parent company made the environmental impact to be a new concern for the implementation of the company’s new IT system.

In the following parts of this section, we will go through the five-step analysis process, and use the case study to explain how to compare the environmental impact of various IT system design alternatives with different workflow, scanning and input technologies.

## 4.1. Step 1: modeling IT system design objectives

In the first step of the analysis process, the IT system’s major stakeholders and its high level design objectives will be identified. The major stakeholders of the IT system can be easily identified, as they are the ones that the system serves. As the IT system is built to satisfy the major stakeholders’ requirements, these major stakeholders’ requirements could reflect the IT system’s design objectives. After the main players are identified, the system’s high level design objectives will be elicited, i.e., what the system is used for and what are the major goals for building the system.

In GRL grammar, the major stakeholders are modeled as actors. And the design objectives and requirements will be mod eled as primitive goals or softgoals of the actors, placed within the related major stakeholders’ boundary.

In our case study, the IT system servers NHX Co. to manage its enterprise production. The major usage of the system is to manage the order, inventory, production, packaging and delivery of the company. As shown in Fig. 7, NHX Co. is represented by the ‘‘IT System Owner’’ role in the GRL model, and inside its system boundary. The IT system design objective is modeled as the ‘‘Production be Managed’’ softgoal, and it can be decomposed to the four lower-level design objectives, namely the ‘‘Orders be Managed’’, ‘‘Inventory be Managed’’, ‘‘Production be Planned and Controlled’’ and ‘‘Packaging and Delivery be Managed’’ softgoals.

## 4.2. Step 2: generating IT system design alternatives

In the second step of the analysis process, the IT system designers will generate system design alternatives according to the identified design objectives. As the design alternatives being modeled using GRL, the hidden dependency relationship and actors that appears only in certain design alternatives can be revealed.

Step 1: Modelling IT System Design Objectives

Step 2: Generating IT System Design Alternatives

![](/api/attachments/YFCDTEVN/fulltext/images/039649514bcb7c1bb6016413c4c94c0ab0d6a0c19f6aa7017784cf7e3565e308.jpg)

Step 3: Building Environemental Analysis Model for the System Desigr

Step 4: Evaluating Environmental Impact of the Design Alternatives

Step 5: Improving the Design Alternatives and Making Design Decisions

Fig. 6. Environment-driven IT system design strategic analysis process

![](/api/attachments/YFCDTEVN/fulltext/images/355d13dd1846893fd3e750489d211dc863d323e3167c02fa4d8d2a499c9145bf.jpg)  
Fig. 7. Modeling the design objectives and the major actor.

Starting from the initial goals and softgoals in the GRL model, we could proceed to explore the alternative processes, methods or IT technologies used to accomplish the design objectives. In other words, generating IT system design alternatives is to search for the various combinations of these operational processes, methods or technologies that together could satisfy the system design objective goals and softgoals.

In GRL modeling, the operational processes, methods or technologies that satisfy the design objective goals can be represented as tasks. Their connections to the corresponding goal are represented with means-ends links. And if the tasks are linked to the softgoals, contribution links will be used to represent their relations. The whole design alternative generation process is usually done layer by layer from the top down. When operationalizing a high-level goal/softgoal or to break a task into even smaller tasks, we may use decomposition, specialization, substitution, or other refinement techniques to decompose the modeling element, until operational design solutions are concrete enough to provide solid data and input for future quantitative analysis. After the design alternative being modeled, the task in the model may require external help to complete. In that case, the dependency links can be identified, and the stakeholders from which the external help came from can also be added to the GRL model as actors.

Fig. 8 shows the GRL model for the design alternative in our case study. The top-level design objectives are operationalized by a set of tasks. For example, the goal ‘‘Orders be Managed’’ could be satisfied using either hand-signed or online order confirmation and management system. For some specific tasks, the major actor ‘‘IT System Owner’’ may depend on other parties to finish the work. In this case, new dependency links and actors can be identified. Like the task ‘‘Use Bar Code Packaging and Delivery System’’ of the major actor, if the company choose to use the bar code system, they have to rely on the express delivery company to help them track the package. Therefore, the actor ‘‘Delivery Service Provider’’ needs to use the appropriate scanner devices and tracking system accordingly. After this step, the possible design alternatives that the company interested in can be covered by the GRL model. Meanwhile, two actors ‘‘Customer’’ and ‘‘Delivery Service Provider’’ are introduced for further analyzing the overall environmental impact of the system design alternatives

![](/api/attachments/YFCDTEVN/fulltext/images/7a8edd0fd20c9f76194a657323c2061ede6ec9f28fbb6eddac2eb0e43e861106.jpg)  
Fig. 8. Generate design alternatives based on the IT system design objectives.

## 4.3. Step 3: building environmental analysis model for the IT system design

In the third step of the analysis process, the system-specific environmental analysis model will be generated from the GRL model built in the previous part. Based on their unique circumstances, the design decision makers could work together to identify the most important aspects of the IT system’s environmental impact. After that, these decision makers could identify the relationship between the operational tasks and the environmental requirements, or to reuse the links in the existing analysis models to build the analysis model for the system under study.

The decision makers could select from the IT system environmental softgoal structure introduced in Section 3 to identify the important aspects of environmental impact. These important aspects can add to the GRL model as softgoals. Then the bottom-level tasks’ contribution to these environmental softgoals could be represented with the contribution links in the GRL model. In this step, the decision makers could also choose a part of IT system that they are most interested in for future analysis. In that case, the decision makers could define the boundary of the IT system design that need to be analyzed.

In our case study, the system design decision makers agreed on the environmental softgoal ‘‘High Resources Efficiency’ and ‘‘Low Energy Consumption’’ should be the most important environmental aspect that should be put into consideration. As a result, the two softgoals along with their descendent softgoals are added to the GRL model (shown in Fig. 9). As the design alternatives in Fig. 8 is still on the abstract level, we decompose these design alternatives into even smaller tasks. With the help of these smaller tasks, the contribution relationships between the design alternatives and the environmental softgoals can be modeled. Fig. 9 shows the task decomposition for two out of the four second-level system design goals. The GRL model could reflect the basic relationships between the bottom-level tasks and the environmental softgoals. Therefore, this GRl model could serve as the primary conceptual framework for analyzing the IT system design alternatives’ environmental impact.

## 4.4. Step 4: evaluating environmental impact of the design alternatives

In the fourth step of analysis process, the bottom-level tasks that forms the design alternatives will be quantitative evaluated against the selected kinds of environmental impacts. Evaluating to what extent the design alternatives could satisfy the chosen environmental requirements, the quantitative contributions of the design options to the softgoal will be explicitly modeled. Based on the input data that the design alternatives provide, we could build up the entire computational model for the top level softgoals by adding the quantitative calculation models to the contribution and decomposition links in the GRL model. Using this computational model, we could predict how much contributions or destruction each task in the design alternatives may do to satisfy the top level environmental softgoals.

![](/api/attachments/YFCDTEVN/fulltext/images/b94832f8742d16ff8b2a88b9716bca3f1fe64467e8d032c43092977c0a70e2b7.jpg)  
Fig. 9. Building environmental analysis model for the IT system design alternatives.

According to our previous work, environmental simulation models as well as other environmental quantitative calculation applications could be packed into web services using a specially designed XML based web service description format And by using a goal decomposition structure to avoid duplicate calculation, these calculation services can be selected according to the environmental variables and combined to form a holistic quantitative model. (Giorgini et al., 2002) To build the quantitative analysis models for the design alternatives, we could implement a similar method.

As shown in the right side of Fig. 10, the related environmental quantitative calculation models can be represented with a tetrad:<Inputs, Outputs, Restrictions, Error>. The inputs and outputs attribute shows the input and output variables of the model, while the restrictions attribute explains under what circumstances the model could be used. The last attribute error denotes the models calculation error, which could be used to predict the accuracy of such quantitative evaluation. To form a quantitative evaluation for the IT system design alternatives, the contribution links and the decomposition links added in the third step of the process could be replaced by quantitative calculation models. With the bottom-level tasks and environmental softgoals providing inputs and expected outputs, the quantitative models could be selected according to the satisfactory to their restrictions attribute. Likewise, the quantitative model selection for the decomposition links between the environmental softgoals could also be done by matching these attributes of the quantitative calculation models. After the models being selected, the quantitative calculation models could form one or several calculation trees with the top level environmental softgoals on the top. Using the inputs from the bottom-level task, the estimate environmental impact of the task could be estimated with the calculation trees calculating from the bottom up The result collected at the top of the calculation tree reflects the task’s environmental impact in that specific aspect represented by the top softgoal. And if there are more than one top level softgoals or there are other kinds of NFRs need to satisfy, the quantitative results could be combined together to form a vector or use a weighted sum formula to represent its estimated quantitative environmental impact. These quantitative results could later be used for further design decision making or design improvement.

Shown in Fig. 10, the basic unit of each environmental softgoal should first be defined. Then, the properties of the bottomlevel tasks as well as the system design assumptions and settings are collected under unified coding system. After that, the quantitative calculation models could be selected from the environmental quantitative model pool to support the quantitative analysis of the design alternatives. The selection can be made by matching the inputs, outputs and restrictions attribute of the quantitative models: the data collected from the bottom-level task should contain the required inputs noted by the inputs attributes; on the other hand, the basic unit of the higher-level softgoal that the contribution or decomposition links to should also match with the quantitative calculation model’s outputs attribute; finally, the restrictions attribute of the quantitative calculation model should also be satisfied by the input data and the system design assumptions. Take Model 6 in the GRL model as an example. The data RFID writer/scanner model and the estimated frequency of use can be collected at the task ‘‘Use RFID Writing and Scanning Device’’. Meanwhile, the outputs attribute of Model 6 is annual electricity consumption in kWh/a, this match perfectly with the softgoal ‘‘Low Electricity (kWh/a)’’. As the scanner is a member of the Motorola MC family, the model capable of calculate the estimate annual electricity consumption of using the IT system owner using RFID writing and scanning devices, with a maximum error of 20%. In this way, a set of quantitative models can be selected for the decomposition links and the contribution links in the model. With these quantitative calculation models, two separate calculation tree structures can be generated to estimate the bottom-level tasks’ energy consumption and natural resources consumption.

![](/api/attachments/YFCDTEVN/fulltext/images/568e35c07f779afdb600d7576f25b9f4c18703dea21099342e35df4bc20aac30.jpg)  
Fig. 10. Use quantitative models to estimate design alternatives’ environmental impact.

## 4.5. Step 5: improving the design alternatives and making design decisions

In the last step of the analysis process, the design decision makers could obtain a holistic view of the system design alternative’s environmental impact by summing up the involved tasks’ quantitative results. Thus, we could already be able to pick the better design alternative according against the selected environmental softgoals. But even for the better design alternative, there is always room for improvement. The refining of a certain design alternative could be done by replacing the tasks that make the most destruction to the softgoal with similar task which have less negative impact against the top level environmental softgoal. At this last step of the analysis process, quantitative analysis results of other related NFRs could also be put into consideration. These quantitative analysis results could add as additional dimensions to the environmental impact result vectors, or as additional weighted factors adding to the final weighted sum evaluation formula.

Back to the case study, Fig. 11 shows the design alternatives selected by the IT system design decision makers. By comparing the overall environmental impact of the hand-signed and online order confirmation and management system, the de sign decision makers find the latter solution more environment-friendly. Thus, the ‘‘Use Online Order Confirmation and Management System’’ solution is picked as a part of the new system. In the same way, the design decisions for production management system and the packaging and delivery system can be made. As the inventory management system account for a large proportion of the overall energy use, the decision makers also find the inventory management system may be able to provide extra energy savings applying smart stand-by mode to the client desktop computers.

The case study shows how to make environment-friendly IT system design decisions using the design strategic analysis process based on GRL. A computational model for the stakeholders’ most important expectations towards the system is built based on the softgoal and task decomposition structure provided by the GRL model.

## 5. Related work and discussions

In this section, we consider current state of the art and research trends. The currently dominant approach is either a micro-level case study approach or a macro-level statistical approach. We expect that a strategic modeling framework can be complementary and beneficial to various existing approaches. It is more predictive when applied to certain sector of society, be it international, national, regional, enterprise scale, or individual behavior. Thus, it is more beneficial to integrating environmental analysis and system engineering in the long term. We begin with work from the green IT community, followed by requirements engineering approaches that have paid special attention to environmental impact analysis and climate change related issues.

![](/api/attachments/YFCDTEVN/fulltext/images/2d786a318732dffbdd5d9dba73d047750ab36247e1f1938423a017d97effd113.jpg)  
Fig. 11. Improving IT system design alternatives and making design decisions

## 5.1. Environment models

Environment models have been an important part of environment policy making. Such policies originate from laws, regulations, or organizational practices, and are typically written in natural language. Environment models using mathematica formalisms and equations can provide a precise formulation of the policies for implementation. More importantly, formally specified policy models can be mathematically verified to guarantee expected environmental constraints be satisfied. As mathematical and statistical abstractions, they provide unambiguous specifications that are independent of concrete system implementation mechanisms. Some example environmental models include the models using system dynamics (Deakin et al., 2002).

Since environmental models are idealized abstractions, their application in real life requires a series of translations and reductions, involving interpretation and decision making at each stage. Organizational structures must be analyzed so as to select the appropriate models, or a combination of models. Policies need to be interpreted and codified properly to achieve the desired results. Real world entities and relationships are mapped to the model abstractions. Finally, the environmental model is mapped to policy making parameters and system implementation mechanisms. The levels of abstractions used in environmental requirements, design, and implementation therefore mirror those in information system development and provide a basis for integration.

The strategic model outlined in this paper can facilitate and augment an integrated environmental friendly development process by enriching the reasoning support needed to arrive at decisions at each stage in the process. The modeling ontology in existing models are intended for the automated enforcement of specified environmental constraints, e.g., to decide what resource or procedure to adopt. They do not support reasoning about why particular models or policies are appropriate for the target environment, especially when there are conflicting objectives and interpretations. Furthermore, many of the simplifying assumptions that formal models rely on do not hold in real life. The social analysis of strategic actors provides a framework for reasoning about the use of such models from a pragmatic, broader perspective.

In the development of new environment models, there is a trend towards ontologies that are more closely aligned with the ontology of organizational work. These trends are consistent with the proposed social ontology approach, though most models are meant for policy making and regulation enforcement, not strategic organizational planning and decision making.

## 5.2. Environmental impact management frameworks

While mathematical models focus on policies built into the social-technical system, the overall environmental impact of information and software systems depend very much on organizational practices. Environmental protection practices have existed long before the computer age. Many of the principles continue to apply and have been adapted to IT systems. Standards have been defined to promote best practices, e.g., ISO 14040 series.

Environmental management frameworks are oriented towards decision making from a business perspective, leading to management, operational, and technical requirements and procedures. Although few frameworks have explicit information models, they do have implicit ontologies revolving around key concepts. The main focus of these frameworks is on prescriptive guidelines. Tables and charts are used to enumerate and cross-list wastes, emissions and consumptions. Potential countermeasures are suggested. Quantitative estimates of impacts are computed from potential losses arising from estimated consumptions and emissions.

While formal environmental models attempt to analysis the interactions between different entities or physical worlds (requiring simplifying assumptions that may depart from reality), environmental management frameworks suggest countermeasures to reduce negative impact. This pragmatic stance is very much in the spirit of the strategic modeling approach proposed in this paper. Environmental management frameworks can be augmented by the modeling of strategic actor relationships and reasoning about how their goals may be achieved or hindered.

Another drawback of checklists and guidelines is that they tend to be too generic. Experience and expert judgment are needed to properly apply them to specific systems and organizational settings. Such judgments are hard to trace or maintain over time as the systems evolve.

The explicit modeling of strategic relationships can provide a more specific analysis of sources of consumptions and emission, thus also allowing countermeasures to be targeted appropriately. Using the strategic dependencies and rationales, one can trace the impact of threats along the paths to determine which business goals are affected. The impact on goals other than environment protection can also be determined through the model since they appear in the same model. One can see how environmental protection goals might compete with or are synergistic with other goals. thus leading to decisions that take the overall set of goals into account. Using an agent-oriented ontology, one can determine which actors are most affected by which environmental threats, and are therefore likely to be most motivated to take measures. Tradeoffs are done from the viewpoint of each stakeholder. This approach provides a good basis for a topology of environment factors which can mediate between business reasoning from an organizational perspective and system design reasoning from a technical perspective.

## 5.3. Green IT systems analysis

There is a body of literature aims to map out the most important and obvious linkages between e-business/ICTs and the environment and to conduct a qualitative assessment of the positive and negative impacts. (Köhler and Erdmann, 2004) The three-order-effects of ICT are the most frequently quoted categorizations in this field, and also a promising route for future. The first order refers direct impacts and opportunities created by the physical existence of ICT, the infrastructure and the processes involved; the second order refers to the indirect impacts and opportunities created by the ongoing use and application of ICT; the third order refers to the impacts and opportunities created by the aggregated effects of large numbers of people using ICT over the medium and long term.

While most of the benefits of ICTs lie in the second order effects via increased efficiency, transparency, speed of transactions, rapid time-to-market, long-tail effects, most of the downsides are associated with the first order, direct environmental impacts from ICT infrastructure such as resource consumption and carbon emission during manufacturing and disposal of hardware. The third level effects, such as increased consumption due to lower price online and taking a leisure drive after teleworking, await to be further explored due to many uncertainties involved.

The goal-based modeling approach proposed in this paper allows the explicit modeling of the hidden dependencies and correlations between impact factors across different orders, so that a holistic and integrated analysis is made possible.

In his recent paper on IS innovation for environmental sustainability, Melville et al. have proposed a Belief–Action– Outcome framework for IS research on Sustainability. It is targeting at similar strategic analysis issues such as what role IS can play in enabling and transforming sustainable processes and practices in organizations. The goal-oriented model, we proposed in the paper also has the model construct of belief, which can be used to capture similar arguments to support the decision making process of organizations strategic planning. The goal decomposition and operationalization process can provide refiner grained analysis and more iterations than their approach, since we can assign the strategic concerns to the different stakeholders, and refine the high-level concerns into detailed operation strategies of the organization. Thus, the two approaches are complementary in nature.

## 5.4. Requirements engineering approaches

While environment impact analysis needs to be integrated into all stages of information systems engineering, there is general agreement that integration starting from the earliest stages is essential. It is well known that mistakes early in the software process can have far reaching consequences in subsequent stages that are difficult and costly to remedy. Brooks (1995) had noted that the requirements stage is the most difficult, and suggested that software engineering should focus more on ‘‘building the right system’’, and not just on ‘‘building the system right’’.

In requirements engineering research, a large part of the effort has been devoted to verifying that the requirements statements are precise, unambiguous, consistent, and complete. Recently, more attention has been given to the challenge of understanding the environment and context of the intended system so that the requirements will truly reflect what stakeholders want.

Traditional requirements languages for software specification focus on structure and behavior, with ontologies that center around entities, activities, states, constraints, and their variants. A goal-oriented ontology allows systems to be placed within the intentional setting of the usage environment. Typically, goal-oriented requirements engineering frameworks employ AND/OR tree structures (or variants) to analyze and explore alternate system definitions that will contribute to stakeholder goals in different ways. Environmental considerations can be readily integrated into such a framework since the intentional selection of different resources, and procedures are intertwined with the normal achievement of stakeholder goals. Environmental impact controls and evaluations can be derived from the ultimate environment protection and sustainability goals to avoid over consumption and emission.

Earlier explorative work by Easterbrook et al. (Easterbrook & Johns, 2009) in integrating requirements analysis and climate change reports on a detailed case study of the practices used by climate scientists. They found that software develop ment for climate models is particularly interesting for a number of reasons. Advances in climate science will play a central role in shaping our understanding of the likely impacts of climate change over the next few decades, and hence will be particularly important for government policy making. Computational models have always played a central role in this field, driving both a heavy demand for supercomputing power, and a need for expertise in computational techniques. If there are opportunities for improvements in software development practices, they are likely to have a big impact on the field. On the other hand, if current software engineering techniques do not offer any immediate benefit, this presents an interesting challenge for software engineering researchers as well.

## 5.5. Environment evaluation tools

In practice, there are several kinds of existing tools and methods to assist the designer and system owner investigating the IT system’s environmental impact in the designing stage. To focus on the IT system itself, there is environmental life cycle assessments (Robin and Davidson, 2001) to analyze the IT equipments’ full life cycle environmental impact, and tools for customers to select and compare IT equipments according to their environmental impact like EPEAT and Energy Star.

![](/api/attachments/YFCDTEVN/fulltext/images/ca2a005ff42be5eda846e5d13f4f2d260cb4dc082922a8b09bb6b5e1dca28b58.jpg)  
Fig. 12. Major steps in a life cycle analysis (Robin and Davidson, 2001)

Whereas to estimated indirect and social level environmental impact caused by the IT system, there is pervasive computing (Köhler and Erdmann, 2004).

Environmental life cycle assessments (LCA) tools provide a framework for incorporating environmental effects into the decision making process. (Robin and Davidson, 2001) As Fig. 12 shows, the LCA process involves three steps: inventory analysis, impact analysis and improvement analysis. In inventory analysis, the product or system life cycle is represented by a flow of processes. The assessment uses an inventory list to estimate the inputs and outputs of the processes at each stage the life cycle. After that, as the inputs and outputs identified in the inventory list all have some potential environmental impacts, the impact analysis is introduced to determine these impacts. Focusing on a list of important environmental impacts the impact analysis carries out a set of quantitative or qualitative impact analysis based on the result of the inventory analysis. Finally in the last step of LCA, improvement assessment compares the results of the impact analysis for different design alternatives. The comparison could help the designers to identify the solution that best meets their environmental-friendliness goals. These tools and methods mostly focus on the concrete product level and hard to provide a holistic view of the system’s overall environmental impact. In our approach, we take the negative environmental impact as a kind of system non-functional requirements, and illustrate the environmentally concerned IT system design decision making process.

## 6. Conclusion

This paper sets out from our belief that software engineering for climate change should take environment as a set of first: class non-functional requirements, in supplement to the classic business objectives and concrete application scenarios. In order to make better handle of these climate change non-functional requirements, we should conduct systematic analysis and design streamline of the environment protect and climate change related NFRs; we should also develop a set of models and techniques which could support rich simulation, prediction, planning, integration and management of the climate change NFRs: and eventually, establish a set of quantitative analysis procedures for representing how environment related resources and factors interact, interfere, and influence with each other.

The goal analysis approach suggested in this paper is mainly used in the early strategic planning stage of the information systems engineering life cycle. One of our ongoing efforts is to maintain the goal model continuously during system execution, conduct run-time monitoring to the environment, and support dynamic adaptation and planning (Jian et al., 2009). These two line of research are to be integrated in future.

## References

Brooks Jr., F.P., 1995. The Mythical Man-Month: Essays on Software Engineering, 20th Anniversary Edition. Addison-Wesley, Reading, MA, 322 pp.

Chung, L., Nixon, B.A., Yu, E., Mylopoulos, J., 2000. Non-Functional Requirements in Software Engineering. Kluwer Academic Publishers.

Deakin, Mark, Steve, Curwell, Patrizia, Lombardi, 2002. Sustainable urban development: the framework and directory of assessment methods. Journal of Environmental Assessment Policy and Management 4 (2), 171–197 (June).

Easterbrook, S.M., Johns, T.C., 2009. Engineering the software for understanding climate change. Computing in Science and Engineering 11, 65–74. EPEAT. 2006, Electronic Product Environmental Assessment Tool (EPEAT). EPEAT. <http://www,epeat.net/>.

Giorgini, P., Mylopoulos, J., Nicchiarelli, E., Sebastiani, R., 2002. Reasoning with goal models. In: 21th International Conference on Conceptual Modeling (ER 2002), LNCS:2503, Tampere, Finland. Springer Verlag, pp. 232–246 (October 167–181).

ITU-T, 2007. ICTs and Climate Change. ITU-T Technology Watch Briefing Report No. 3 (November).

Jian, Y., Li, T., Liu, L. Yu, E., 2009. Goal-oriented modelling for running systems. In: Proceeding of the First International Conference on Requirements@Runtime, Sydney, Australia (28 September 2010).

Köhler, A., Erdmann, L., 2004. Expected environmental impacts of pervasive computing. Human and Ecological Risk Assessment 10 (5), 831–852

Liu, L., Yu, E., 2004. Designing information systems in social context: a goal and scenario modeling approach. Information Systems 29, 187–203.

Murugesan, S., 2008. Harnessing Green IT: Principles and Practices. IEEE IT Professional, pp 24–33 (January–February 2008).

Princen, T., Maniates, M., et al, 2002. Confronting Consumption. MIT Press, Cambridge, Mass.

Puckett, J., Smith, T., 2002. Exporting Harm: The High-tech Trashing of Asia. The Basel Action Network Silicon Valley Toxics Coalition.

Robin, E., Davidson, C., 2001. Environmental Life Cycle Assessments. Introduction to Engineering & the Environment. McGraw-Hill Companies.

Yu, E., 1997. Towards modeling and reasoning support for early-phase requirements engineering. In: Proceedings of the 3rd IEEE International Symposium on Requirements Engineering (RE’97), Washington, DC, USA, pp. 226–235 (January 6–8).
