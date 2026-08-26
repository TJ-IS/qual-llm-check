---
otero_id: 6192
otero_key: "GXQVR9V2"
title: "A user-centered approach for the design and implementation of KDD-based DSS: A case study in the healthcare domain"
authors: "Mounir Ben Ayed; Hela Ltifi; Christophe Kolski; Adel M. Alimi"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.07.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A user-centered approach for the design and implementation of KDD-based DSS: A case study in the healthcare domain

Mounir Ben Ayed <sup>a,b,</sup>⁎, Hela Ltifi <sup>a,c</sup>, Christophe Kolski <sup>c</sup>, Adel M. Alimi <sup>a</sup>

<sup>a</sup> REGIM: REsearch Group on Intelligent Machines, National School of Engineers (ENIS) of Sfax, BP 1173, Sfax, 3038, Tunisia

<sup>b</sup> Faculty of Sciences of Sfax, Computer Science and Communications Department, Route Sokra Km 3.5, BP 1171, 3000, Sfax, Tunisia

<sup>c</sup> LAMIH, UMR CNRS 8530, Université of Valenciennes and Hainaut-Cambrésis, Le Mont Houy, F-59313 Valenciennes cedex 9, France

## a r t i c l e i n f o

Article history: Received 19 June 2009 Received in revised form 5 July 2010 Accepted 14 July 2010 Available online 18 July 2010

Keywords: Decision support system Knowledge Discovery from Database Data mining Human–Computer Interaction Software Engineering Uni<sup>fi</sup>ed Process U model

## a b s t r a c t

In this article we propose an approach for a decision support system (DSS) based on Knowledge Discovery from Databases (KDD). In such system, user must be involved throughout the decision-making process. In consequence we propose the integration of a Human–Computer Interaction (HCI) model into the development of DSS process based on KDD. The approach we propose is based on two systems development methods—the Uni<sup>fi</sup>ed Process (UP) from Software Engineering and the U model from HCI. In this article, w describe our combined approach (UP/U) and the way we used it to develop a DSS in a medical <sup>fi</sup>eld.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

This article stems from our research on the user-centered design of interactive decision support systems (DSS) based on a process of Knowledge Discovery from Data (KDD). The evolution of data-processing and the increasing complexity of the problems involved have generated needs to more and more technological solutions for decision process strategies. DSS deal with problems based on the available knowledge. Some of this knowledge can be extracted using a decisional support tool called data mining [13, 17, 31], which is in fact part of the KDD process (see Section 2). Many techniques can be used to mine data and extract new information. This new information needs to be interpreted and evaluated in order to propose it as a valid element of decision support. Data mining tools are usually dif<sup>fi</sup>cult to exploit because most of the endusers are expert neither in computer science nor in statistics. It is also dif<sup>fi</sup>cult to develop a KDD system that responds exactly to the expert (or end user) needs. Those dif<sup>fi</sup>culties can be overcome by the implication of the user all along the DSS development. No approach is proposed in the literature for the KDD-based DSS development. So, in this work, we wanted to explore the following questions: (1) “which approach should be followed to build a KDD-based DSS?” (2) “Is it possible to take advantage of the existing approaches or methodologies?”

Human–Computer cooperation is essential to the decision support process. From this perspective, Human–Computer Interaction (HCI) is a fundamental aspect for interactive DSS, because the design of such systems heavily relies on a user-centered approach. Given this context, in order to accurately design a DSS, we believe that it is necessary to combine and integrate methods from Software Engineering (SE) and HCI. There already are a number of software development models available in SE for improving software reliability, evolvability, reusability, and portability. However, these models are limited when the system is highly interactive because they do not take the user into account explicitly and systematically [26].

In this paper we propose an approach to develop a KDD-based DSS. This approach is based on two systems development methods—the Uni<sup>fi</sup>ed Process (UP) from SE and the U model from HCI.

We developed and validated our approach with the help of physicians from the Intensive Care Unit (ICU) of Habib Bourguiba Teaching Hospital of Sfax, Tunisia. Indeed, medicine, and more precisely the ICU, is one of the <sup>fi</sup>elds where there is a great mass of data daily collected and where experts have to take important decisions. These physicians need a DSS based on KDD to help them predicting and preventing nosocomial infections, also called hospital infections. These infections are caught by some patients, a few days after their entrance to the hospital. Some of these patients may die because of nosocomial infections.

This article continues with a short review of the literature about the two fundamental concepts: DSS and KDD (Section 2). Then, it presents a short survey of the most widespread development processes in the <sup>fi</sup>elds of SE and HCI in order to identify the key elements needed to implement a more complete process that supports DSS design and development based on a KDD process (Section 3). It then summarizes this more complete approach (Section 4) and provides a case study of its implementation in a medical environment (Section 5). In Section 6 we give a discussion about our approach, and the research and practice implications of this work. This article ends with our conclusions and the perspectives for future research (Section 7).

## 2. DSS and HCI: key concepts for KDD

## 2.1. Decision-making process, DSS and HCI

Simon [53] distinguishes three phases in the decision-making process [24, 39, 43, 57]: (1) the search for information, which includes the identi<sup>fi</sup>cation and the statement of the problem to deal with; (2) the design process, which includes generating, developing and analyzing the different possible series of actions (solutions); and (3) the choice of a solution, which involves researching, evaluating and selecting the most appropriate solution identi<sup>fi</sup>ed during the previous phase.

Beynon et al. [6] have shown that there are fundamental problems for the DSS process described above: (1) initially the expert doesn't know how to identify or formulate a problem; (2) the expert doesn't always have an abstract or systematic method for <sup>fi</sup>nding solutions, only recognizing solutions that have been seen or explored; (3) the expert may have no explicit heuristic for evaluating and selecting solutions. Beynon et al. [6] highlighted the DSS's need for synergy between human processing and “automatic” processing.

In the early eighties, several User Interface Management Systems (UIMS) [44] and many toolkits [40] were developed, as extensions of the graphics libraries. The fundamental principles of UIMSs are the reuse of interface code and the separation of the functional part of an application from its interface [40].

Fisher [14] has stated that the success or failure of a DSS depends more on its communication capabilities and its interface for human– computer interaction than on its processing speed and problem solving capabilities. We tend to agree with this assessment. We consider that interactive DSS are systems that allow one user (decision-maker) or a group of users to identify, explore and solve problems through human–computer dialogue, with the communication between the various human actors (e.g., decision-makers, consultants, experts) involved in a DSS [57].

The concept of interactivity in a DSS highlights the essential role of humans. This role is not passive and is facilitated by the integrative quality of the various system components and by the HCI, which takes on the supporting role of decision-maker's assistant [43]. We believe that system developers must design cooperative DSS systems that permit the distribution of competencies between the user and the computer.

## 2.2. KDD: an interactive and iterative process

The concept of decisional computer science [58] refers to decisionmaking support, or in other words, to the exploitation of data to facilitate decision-making. There exist several decisional tools, such as: On-Line Analytical Processing (OLAP) [12, 56] for multidimensional analysis and data mining (DM) for exploring new knowledge in large quantities of data [13, 17]. DM aims to identify the possible correlations between data elements in a signi<sup>fi</sup>cant volume of data in order to highlight “hidden” trends. With DM the system often takes the initiative, discovering the associations among data by itself. To a certain extent, this makes it possible “to predict the future, according to the past.”

Originally, DM referred to the most important stage of a multistage interactive and iterative process known as KDD (Knowledge Discovery from Databases) [31]; results can be re<sup>fi</sup>ned by repeating the various stages several times under the control of an analyst (Fig. 1). The various stages of the KDD process are: (1) problem formulation (identifying the objectives, de<sup>fi</sup>ning the targets and checking the needs); (2) data retrieval (identifying the information and the sources, checking their quality and accessibility); (3) data selection (choosing the data related to the requested analysis); (4) data cleansing (detecting and correcting the inaccuracies and/or errors in the data); (5) data transformation (formatting the data in preparation for the “mining” operation); (6) data mining (applying one or more techniques—such as neuronal networks, Bayesian networks or decision trees—to extract interesting patterns); (7) result evaluation (estimating the quality of the patterns extracted, interpreting the patterns' meaning); and (8) knowledge integration (putting the pattern or its results into the company's information system).

According on the above stages, a KDD-based DSS could require up to six modules for its implementation: (1) one to select data, (2) one to cleanse data, (3) one to transform them, (4) one to mine them, (5) one to evaluate and interpret the patterns extracted, and <sup>fi</sup>nally (6) one to manage the extracted knowledge. Some modules may contain a number of different applications. For example, the data mining (DM) module could contain several applications, each one using a different technique to achieve different objectives. Other modules may be combined together. Some researchers have proposed combining the data selection, cleansing and transformation modules into a single module called “data preparation” [17, 41]. This is the direction that we have taken in our work (see Section 5).

## 2.3. Integrating HCI in a KDD process

One of the challenges of KDD-based DSS is detecting the strategies for solving a decision problem through a process that has a DM stage. This process includes various important stages, such as analyzing the decision-makers' need, determining the various preparatory activities, handling the relevant data and visualizing the results. The endusers' acceptance or rejection of the decision support tool depends on these stages [31]. For this reason, appropriate HCI activities should be able to guide users throughout the stages of the KDD process; it is also important to adapt these HCI activities as much as possible to each decision-maker [28]. The next section describes some representative systems development models in the <sup>fi</sup>elds of the SE and the HCI.

## 3. Development approaches

Given the stakes involved in most DSS problems and the quantity of raw data used in KDD, it is essential to have the most complete model possible of the methodology. In order to select an appropriate global approach for our context, a critical study of some traditional development cycles was necessary [34]. This section provides a representative rather than exhaustive examination of the available systems development models in the <sup>fi</sup>elds of the SE and the HCI.

## 3.1. The principal SE development models

SE development processes or models describe the logical and temporal order of the software production stages. Several models have been proposed. The main ones are discussed brie<sup>fl</sup>y below. The Uni<sup>fi</sup>ed Process, which is based on a speci<sup>fi</sup>c methodological process, is also examined.

The waterfall model [48] identi<sup>fi</sup>es the main steps in the sequential production and maintenance of an application. It allows returns to the immediately preceding stage but it does not take HCI into account, even when the system is highly interactive [25]. The V model [37] structures the process steps in two sub-processes: (1) a descending sub-process for speci<sup>fi</sup>cation and design and (2) an ascending subprocess for validation and testing. But, it does not introduce HCI considerations; it is mainly intended to evaluate the technical aspects of the system concerned. The spiral model [7] is based on a succession of 4-phase cycles, each of which is based on a systematic analysis of the risks related to the alternatives in the decision-making process during the project steps. It introduces the concepts of prototyping and re<sup>fi</sup>ning. Nevertheless, like the other models, it does not take the HCI into considerations.

![](/api/attachments/GXQVR9V2/fulltext/images/d2b44e5251637a77acc78908f47905aa2a5d6b6af8448840c272d2d7c6f1c99b.jpg)  
Fig. 1. KDD tools.

The agile models [30] for software development appeared in the early 1990s. These models do not have such systematic processes as the traditional models. Their objective is quick software design based on heavy customer involvement and signi<sup>fi</sup>cant reactivity to his requests. These models target customer satisfaction rather than satisfying the terms of the contract. They include, for example, Adaptive Software Development (ASD), Dynamic Systems Development Method (DSDM), Extreme Programming (XP) [23] and Rapid Application Development (RAD). Such development models recommend regular meetings with the customer, delivering an initial product as rapidly as possible and adapting to changing customer needs. But these models do not cover all the steps of a process. In addition the agile methodologies deployment often encounters resistance from systems developers [11].

Jacobson and his colleagues, the fathers of the Unified Process (UP), do not cite any of the methods mentioned above in their reference book [21], nor do they use the term “agile.” They thus apparently do not consider UP being an “agile” model. Nevertheless, we feel that its potential is very interesting.

Indeed, UP consists of a set of generic principles that can be adapted to speci<sup>fi</sup>c projects [21, 29]. It is thus a process pattern that can be adapted to a large category of software systems, various <sup>fi</sup>elds of applications, different types of companies, different quali<sup>fi</sup>cation levels and various project sizes. UP is (1) controlled by the use cases, representing the functional needs of the system, (2) centered on system architecture, which provides the structure used as framework for the work carried out during the iterations, and (3) iterative and incremental, with the aim of reducing complexity by controlling it, by breaking up a data-processing project into sub-projects that each represent one iteration. These iterations indicate the steps in the sequence of activities, while the increments correspond to the stages of product development. The aspects of the model being analyzed and designed are based on UML [21, 30, 50].

UP has 4 phases: (1) initialization, during which the extent of the project is de<sup>fi</sup>ned through use cases and feasibility studies; (2) development, during which the needs are de<sup>fi</sup>ned and the architecture speci<sup>fi</sup>ed; (3) construction, during which the software is built by means of several iterations and various system versions; and (4) transition, during which the system is delivered to the end-users and put into service and these end-users are trained and provided with tech support [21, 29] (Fig. 2).

The advantage of UP is that it: (i) allows the costs to be limited to the strict expenses (workload) related to an iteration, (ii) makes it possible to limit the risks of delaying the installation of the application to be developed, and (iii) permits potential problems to be identi<sup>fi</sup>ed in the <sup>fi</sup>rst stages of development. This short-term planning is due to the fact that user needs and the corresponding requirements cannot be de<sup>fi</sup>ned completely in advance. The system architecture provides the structure that is used as a framework.

Lemieux and Desmarais [32] showed that the Rational Uni<sup>fi</sup>ed Process (RUP), a commercial version of the UP, is not user-centered according to the standard ISO 13407 [20]. This standard speci<sup>fi</sup>es the rules to be followed to adapt a software development process for usercentered design. They also note that the introduction of the use cases is not suf<sup>fi</sup>cient to make a design process user-centered.

SE is designed to produce quality systems. However, most traditional models are too often directed towards the technical aspects of the system (e.g., the code) and not enough towards user needs. The only real exception to this observation is UP. Nonetheless, though the user is involved throughout the project life cycle, no formal explanation shows this involvement. The UP diagram (Fig. 2) does not mention the user anywhere.

![](/api/attachments/GXQVR9V2/fulltext/images/9661abcf7285161d11a4cb06931fc48924f4ceb46f6f726c0ea992e3e69f8cdc.jpg)  
Fig. 2. Uni<sup>fi</sup>ed process. [21]

The general tendency in software development is towards iterative processes (e.g., spiral, UP) but also towards integrating the re-use concept. Even when users are relatively involved in the analysis and validation stages for a prototype, the models and processes are generally not accompanied by explanations of their involvement. HCI design and evaluation principles are not part of these generic processes [27, 32]. From the perspective of interactive system development, user characteristics must be clearly expressed. The SE development models have been judged to take the user insuf<sup>fi</sup>ciently into account, about <sup>fi</sup>fteen years ago, the traditional models began being enriched with HCI principles. This enrichment is discussed in the following section.

## 3.2. The principal HCI-enriched development models

HCI-enriched development models are user-centered; their principal concern is to highlight the fundamental methodological aspects of the system, such as the modeling of human tasks, the iterative development based on prototypes and the evaluation of the interactive system. The best-known models are mentioned below (For a more complete review, see the article by Kolski et al. [27]).

The star model [19] places the evaluation at the center of the complete process, which permits interactions and iterations between each stage. This model is very <sup>fl</sup>exible; it does not impose any order for the stages of the process. The star model offers a participative design process that targets the detection of usability problems [34]. This model's weakness is that the tasks are validated by only one prototype [10].

In the HCI-enriched V model proposed by Balbo [5], the steps of development process are divided into two zones: the HCI zone and the software zone. The <sup>fi</sup>rst is characterized by the priority given to the ergonomic aspects; the second by the importance given to the software implementation techniques.

The U model [1, 3, 33, 38] considers the steps which do not exist in traditional SE models. The U model has two phases (Fig. 3): (1) a descending phase for speci<sup>fi</sup>cation and human–machine systems design, which leads to its implementation; and (2) an ascending phase for the evaluation of the global system. Validation consists of comparing the model of the theoretical tasks speci<sup>fi</sup>ed in the descending phase with the model of the real tasks highlighted in ascending phase, according to the original principles suggested by Abed et al. [2,3]. The result of this comparison either validates the human–machine system or highlights its de<sup>fi</sup>ciencies. In case of de<sup>fi</sup>ciencies, the result of the comparison has to be gradually <sup>fi</sup>netuned, particularly on the level of HCI and the support tools. The <sup>fi</sup>nal model resulting from the assessment allows the users' speci<sup>fi</sup>c behaviors to be generalized under particular work conditions, and can be reused in situations dealing with similar systems [34].

The U model can be adapted according to the characteristics of the application. For example, Lepreux et al. [33] adapted this model for particular types of DSS. This model is centered on HCI, but it does not clearly present the iterative and incremental development of the interactive system to be created.

## 3.3. Conclusion on the SE models and those enriched under the HCI angle

The inadequacies of the SE models with respect to interactive systems (e.g., task analysis, consideration of human factors) led to the development of user-centered HCI-enriched models. This development highlights the evolution brought about by applying HCI principles to SE. It is centered on the essential ideas for the interactive system development, (i.e. setting the activities of the various actors; clarifying the evaluation within the process; modeling the system, the tasks and the HCI), especially the evaluation, in order to compare the theoretical tasks speci<sup>fi</sup>ed by the designer at the beginning of the process to the real tasks carried out by the users. Still, none of these enriched models is perfect.

As a result, no model associates both the advantages of the SE models and those of the HCI models. Moreover, there is no model that deals with the subject that interest us: DSS based on the KDD process. This critical study of the various development models in both <sup>fi</sup>elds has made it possible to suggest what, for us, is a more appropriate approach to this subject.

## 4. Proposed approach: UP/U

SE development models include a set of traditional steps. However, they do not integrate the user's point of view and do not allow the development of interactive applications in which the human– machine interaction must meet speci<sup>fi</sup>c user-centered quality criteria. Even the HCI-enriched versions of these traditional models are still insuf<sup>fi</sup>cient for designing and evaluating the DSS that interests us because the designer does not have to cover all the steps of the traditional development process. For this reason, we propose a new design approach that combines an SE process with an HCI model. Since our approach reconsiders the UP in the light of the U model, we call it UP/U. We think this new approach is more appropriate to our DSS context.

![](/api/attachments/GXQVR9V2/fulltext/images/9a5cc0b91bc08c7e85f21e3f941cbbc9dfe540c145efd1379d5f86b6a7417907.jpg)  
Fig. 3. The U model. [2]

4.1. Justification of the adopted methodology

The critical study of the development processes in the <sup>fi</sup>elds of SE and HCI, presented in Section 3, allowed us to highlight the advantages and

## Table 1

The complementarity of the Uni<sup>fi</sup>ed Process and the U model.

<table><tr><td>The Unified Process</td><td>The U model</td></tr><tr><td>Methodology from SE</td><td>Methodology from HCI</td></tr><tr><td>Defining characteristic:Generic: this process can be adapted to a large class of software systems, various fields of application, various ability (or qualification) levels and various project sizes.</td><td>Defining characteristic:Specific to interactive applications: this model has its roots in the various traditional HCI-enriched models</td></tr><tr><td>Basic principles:Iterative and incremental; based on use cases, and thus incidentally on user needs; centered on the system architecture rather than the system user</td><td>Basic principles:User-centered, meaning that human factors are taken into account by the development team; comparison of the theoretical and real tasks in order to validate and fine-tune the system</td></tr><tr><td>Relevance:More than the advantages offered by this methodology (e.g., adaptability, control of projects complexity), the strong point is the interactivity of its process.Advantages:- Minimizes the costs, in terms of risk, to the cost of only one iteration.- Thanks to the iterative nature of the development, user needs appear more clearly with each successive iteration, making it easier to adapt to the user&#x27;s evolving needs.</td><td>Relevance:The methodology&#x27;s interactivity is fundamental from the perspective of DSS design.In addition, the analysis of the system users and their tasks is recommended.Advantages:- A set of tasks is associated to each user objective. This allows certain interactive system functions to be defined.- The designer becomes more aware of the importance of the human factor in HCI design and evaluation.</td></tr><tr><td>Life cycle:- UP iterates a series of cycles that constitute the construction of a system generation. All cycles end with the delivery of a product version to the customers.- Each UP cycle has 4 phases: initialization, development, construction and transition.Each of these phases is in turn divided into iterations. Each iteration includes five activities: needs assessment, analysis, design, implementation and testing.</td><td>Life cycle:The U model has 2 phases:- A descending phase that includes the specification and design of human-machine systems.- An ascending phase that includes the evaluation of the global system.In turn, the first phase can be divided into 4 stages: needs assessment, analysis, design and implementation; the second phase can be divided into the activities of evaluation and comparison.</td></tr></table>

disadvantages of the various models. Interactive systems design as practiced in HCI and the development processes as performed in SE are generally executed separately and thus lack coherency. In order for the two <sup>fi</sup>elds to work together, it is essential to discover the commonalities of SE and HCI practice. To accomplish this, we compare the UP from SE and the U model from HCI. In our opinion, these two standards are complementary. Table 1 presents the elements that, in our opinion, justify this choice. As the table shows, both methodologies have elements that are relevant for the development of a DSS based on a KDD process. The development approach that we propose must make it possible to take the user into account (the contribution of the U model) by emphasizing the use of prototypes, the explicit positioning of the activities of the development process actors and the analysis of the activity (the contribution of UP).

To model the DSS that interests us, we used the Uni<sup>fi</sup>ed Modeling Language (UML) [29, 49]. Indeed, UP (Fig. 2) offers a generic methodological framework based on UML [21]. Given that UML does not impose a speci<sup>fi</sup>c working method, it can be used transparently with any other software development process, making it possible to use this language with the U model (Fig. 3), which does not de<sup>fi</sup>ne an obligatory modeling language.

Our objective is to design a DSS that makes it possible for decisionmakers to interact with the system to get information to support their decision-making process. In the problem identi<sup>fi</sup>cation stage of the KDD process, the different main objectives of the future system are determined and de<sup>fi</sup>ned. In the pre-treatment stages, speci<sup>fi</sup>c databases are built, the data is cleansed, any missing data is processed, data attributes or elements are selected and then transformed that it can be used by a DM algorithm. These stages are crucial for the retrieval of information relevant to the decision-making process [57]. DM can then be performed to provide knowledge in the form of models that must be validated. Post-processing is also necessary to make these models understandable to humans and/or computers [57]. Information visualization can help the user (decider) to get and understand information ef<sup>fi</sup>ciently and implicate him/her in the data mining process thanks to his/her perception possibilities [35]. For this reason, several possible solutions to the studied problem need to be developed based on the knowledge discovered through KDD. Fig. 4 shows how a DSS can be based on a KDD process.

As pointed out above the U model must be adapted in such way that it can be used in our approach.

## 4.2. Adaptation of the U model

In this paragraph we will explain the reasons for the adaptation of the U model.

Indeed, several elements of this model could be better adapted to the DSS context. Thus, when the existing system is studied, it is important for the decision-maker (the potential user) to describe his/her functional needs and to evaluate and validate the preliminary interface models to show how he/she wants to see HCI executed in the upcoming application. All this information can be used “to model” the decision-maker (e.g., characteristics, preferences, strategies) [46]. In addition, since task de<sup>fi</sup>nition and task allocation in a KDD-based DSS are very important, these activities must be singled out for attention. Furthermore, the original U model does not clearly present the order of the activities (needs assessments, analysis, design, implementation and testing); so, we proposed an order for these activities needs to be established as the U model is to be used with UP. Moreover, since the steps of U model are more concerned with the speci<sup>fi</sup>cation and evaluation of HCI than with the applications of the interactive system studied, this aspect also needs to be reinforced for the KDD-based DSS. Finally, we think that the “general knowledge capitalization model” step could be simpli<sup>fi</sup>ed by getting feedback from the “user model” step. Based on this list of elements, we propose an adapted U model for DSS design and development (Fig. 5). Its description is indicated in the following paragraph.

Descending phase: the beginning of the descending phase starts with two essential steps that take place simultaneously: (1) the analysis of the application domain, including de<sup>fi</sup>ning the system objectives, which allows the <sup>fi</sup>rst functional and structural description of the system to be developed; and (2) the development of the <sup>fi</sup>rst interface prototypes (models) for the DSS in question, which, by giving future users an idea of the possible solutions, allows them to be implicated as early as possible in the project life cycle. These two steps provide a structural framework for future activities and technical solutions. Once these steps accomplished, it is possible to draw up a list of the tasks (manual, automatic or interactive) needed for the future operations of the DSS. These tasks must be de<sup>fi</sup>ned and formalized. These steps can take place cyclically, as suggested by the arrows in the <sup>fi</sup>gure of the adapted U model (Fig. 5). Then, the speci<sup>fi</sup>ed tasks must be modeled [2]. Three principal task categories are customary in SE and HCI: (1) tasks involving the user only, called manual tasks, (2) tasks involving the application only, called automatic or system tasks, and (3) tasks involving different levels of collaboration between the user and the system, called interactive tasks. The probable behaviors of the various user types serve as the basis of these representations, taking the form of a general user model. The limitations and physical and cognitive resources of the various types of users are incorporated into the model [46, 59].

![](/api/attachments/GXQVR9V2/fulltext/images/ed405ef82fb8faabff858d4a531be635c449d5aae71dff3b376dfa20fe0b8519.jpg)  
Fig. 4. DSS based on KDD.

![](/api/attachments/GXQVR9V2/fulltext/images/2aa84bf8397e326a2cc4f3150c6a8cb26aa0f6f451ec284653431ad86da666db.jpg)  
Fig. 5. Adapted U model.

Depending on the speci<sup>fi</sup>cities of the domain, the various decision support tools must be analyzed in order to determine those that are the most appropriate for the system to be designed. The last step of the descending phase leads to the implementation of the DSS module or one of its versions.

Ascending phase: the evaluation of a human–machine system consists of testing whether or not users can accomplish their tasks using the provided interface. Two properties are usually explored for such evaluations: usefulness and usability [42, 51]. A number of methods can be used to evaluate interactive systems [42, 60]: interviews, questionnaires, observations, electronic informers, trace analysis. The ascending phase generally concerns the tasks shown on the right-hand side concentrating on: (1) user behavior when interacting with the system (e.g., the time required to accomplish a task, the accuracy of the results, the number and types of errors, user opinions, etc.), and (2) the differences between the system objectives and the <sup>fi</sup>nal results.

The ascending phase starts with the de<sup>fi</sup>nition of the experimental protocols (i.e., subjects, progress, situations and tasks concerned, data to be collected, etc.) [3]. Once collected, the data is processed according to the operational principles established in the descending phase in order to correlate the data with the observed human activity for the whole decision-making process shown in Fig. 4. The operating sequences are highlighted, which allows the real activities (tasks) to be gradually reconstituted. The tasks really accomplished can be different from the tasks initially speci<sup>fi</sup>ed by the designer in the descending phase. One of the fundamental principles of the U model concerns the direct comparison between the real and the speci<sup>fi</sup>ed tasks. The results of this comparison lead either to validate the entire system or to identify the areas that need to be improved. Depending on the extent of the improvements needed, implementing these improvements may require returning to the various steps of the descending phase, which is perfectly coherent with the iterative nature of the UP.

## 4.3. The proposed user-centered approach (UP/U)

Since it is intended to allow KDD-based DSS to be designed, our approach puts HCI in a central position, rede<sup>fi</sup>ning the user's role allowing him/her to intervene at any time in the KDD process (Fig. 6). This approach is based on the UP principle of iterative and incremental development, which allows each task accomplished to be evaluated as soon as the <sup>fi</sup>rst iterations of the development process have been completed.

Our approach executes several complete UP iterations, from the initialization phase to the transition phase [36]. However, since the <sup>fi</sup>ve activities of the original UP process (needs assessment, analysis, design, implementation and testing) do not model the system users or system– user interaction, our adapted U model is applied at each iteration level. Our approach thus incorporates the continual presence and constant participation of the user throughout the project. Each activity of the adapted U model is divided into sub-activities that model the HCI of the DSS in question. Each of these activities is presented in detail below.

![](/api/attachments/GXQVR9V2/fulltext/images/6fea556464a6dea31f531b94d6a1898608bf5b09b9b50962d196d885a090aa5b.jpg)  
Fig. 6. The UP/U approach.

## 4.3.1. Needs assessment

This activity allows the user's functional needs and the nonfunctional technical needs to be de<sup>fi</sup>ned. At each UP phase (initialization, development, construction and transition) user-centered activities are carried out. Therefore, to the original UP activity level, we have added the actions “model user” (e.g., the decisionmaker) [46], “de<sup>fi</sup>ne and allocate the decisional functions” and “model the automatic, manual and interactive tasks.”

## 4.3.2. Analysis

This activity allows the customer needs and requirements to be understood. This understanding leads to de<sup>fi</sup>ning the speci<sup>fi</sup>cations in order to choose the design solution. An analysis model provides a complete needs speci<sup>fi</sup>cation based on the use cases and structures these needs in a form (e.g., in a scenario form [47]) that facilitates the comprehension, the preparation, the modi<sup>fi</sup>cation and the maintenance of the future system.

## 4.3.3. Design

This activity provides a more accurate understanding of the constraints related to the programming language, the use of components and the operating system. It also determines the architecture of the automatic and interactive modules.

## 4.3.4. Implementation

This activity is the result of the design. Its main objectives are planning the integration of the components and producing the classes and providing the source code. This activity includes also the interfaces implementation according to the de<sup>fi</sup>ned speci<sup>fi</sup>cations.

## 4.3.5. Testing

This UP activity allows the results to be veri<sup>fi</sup>ed. It must be carried out at the same time as the activities suggested for the U model, notably tests with the users and the comparison of the tasks initially speci<sup>fi</sup>ed by the designer and the tasks really accomplished by the users.

## 5. Healthcare case study

In the previous section, we presented our proposal for a usercentered approach. This approach was applied to a concrete case in the <sup>fi</sup>eld of healthcare. The DSS discussed below is based on a KDD process in which the data mining stage uses Case-based Reasoning [45]. This DSS is being used and evaluated in the intensive care unit (ICU) of the Habib Bourguiba Teaching Hospital (HBTH) in Sfax, Tunisia. The DSS was designed to help the physicians, who are the current users of the system, to understand, predict and prevent nosocomial infections (NI). In this section, we <sup>fi</sup>rst describe the context. Then we explain how the proposed user-centered approach was implemented in this context.

## 5.1. Context

Our project is part of a much wider project aimed at <sup>fi</sup>ghting NI. They are infections contracted by patients during their hospital stay. It is a major public health problem. An infection is typically regarded as nosocomial if it appears 48 h or more after hospital admission [16]. NI can be located in any organ; the most commonly affected organs are lungs, kidneys and the heart. In ICU, the problem of NI is far more alarming because the patients who are hospitalized in that unit are more fragile. It is such an important problem that some European countries have created groups to <sup>fi</sup>ght NI [54]. A few studies have proposed information-processing systems based on data mining techniques to monitor NI [8, 9]. Some of these studies have shown the effectiveness of these systems and their capacity to produce useful rules. But, as described in the articles, these systems appear to be dif<sup>fi</sup>cult for physicians to use.

A study on the prevalence of NI in the HBTH [22] showed that 17.9 % of the 280 patients hospitalized in the entire hospital were victims of one NI between April 17th 2002 (midnight) and April 18th 2002 (midnight). The ICU of the HBTH has 22 beds in 11 compartments. The patients admitted to ICU are known as “critical” because they require much care and constant monitoring. These patients are often connected to machines (e.g., arti<sup>fi</sup>cial respirator, electrocardiogram, electrical syringe) and/or have catheters (e.g., venous catheters, urinary probes, thoracic drains). Extremely fragile, these patients are sensitive to every new germ that enters their bodies, which makes them more likely to develop NI. When an infection (nosocomial or not) appears, a sample is sent to the laboratory to get an anti-biogram. Depending on the result of the anti-biogram, anti-biotherapy is prescribed. The problem with anti-biotherapy is that a germ can be sensitive to an antibiotic one week and resistant a few weeks or a month later. In addition, this sensitivity can be different from one patient to another.

Several doctoral dissertations and studies have been published on this subject by the team of ICU physicians at HBTH [15, 18]. Previously, to conduct these studies, doctors collected their data manually on paper forms and then entered and stored the data in an Excel® <sup>fi</sup>le, which was analyzed by statistics software such as SPSS®. However, such tools are only capable of producing the “classic” statistics (e.g., percentages, averages, variance analyses). The physicians wanted go further in their analysis in order to extract information and knowledge that would allow them to better understand, predict and prevent the appearance of NI. We got involved because data mining can provide them with that knowledge.

## 5.2. KDD process modules

Fig. 1 shows the six modules that it would, in theory, be necessary to develop to create a DSS based on a complete KDD process. In reality, depending on the speci<sup>fi</sup>c details of the context, the number of modules can vary. To develop our DSS, since we did not have initial data sources, we had to create one especially for the project. Consequently, the modules “data selection,” “data pre-treatment” and “data transformation” could be combined to form one module “data storage and acquisition.” As a result of this fusion, only four modules were necessary: “data acquisition and storage,” “data mining,” “evaluation” and “knowledge management.”

Initialization phase for the “storage and data acquisition” module.

<table><tr><td colspan="2">Initialization</td></tr><tr><td>Activities</td><td>Iteration 1 (only one iteration in this phase)</td></tr><tr><td>UP: needs assessment</td><td>Need for data to be used by a data mining tool. A database needed to be implemented containing data useful for studying NI. Data should be recorded after the patient leaves the ICU. The persons in charge placed a computer with limited capacities at our disposal for certain period of time</td></tr><tr><td>U: analysis of the application domain</td><td>Study of nosocomial infections (definition, causes, risks...)</td></tr><tr><td>U: first interface prototypes. Description of the system&#x27;s functional and structural needs and task definition.</td><td>Structural and functional description was deduced after consultation with the future users and the general architecture of HCI prototypes was outlined. The doctors proposed windows with tabs.</td></tr><tr><td>U: user design</td><td>A preliminary user model (only one type for the moment) was created. This user was an expert in the NI field, as witnessed by his many publications and his supervision of doctoral dissertations about the fight against NI. He also had good computer skills, spending more than 3 h per day in front of his PC.</td></tr><tr><td>U: definition and allocation of tasks to be executed</td><td>The first description of manual tasks (Cards containing the data necessary to the study are filled out by the internal doctors at the patients&#x27; bedside), automatics tasks (calculation of the patient&#x27;s age and death risk parameter) and interactive tasks (choice of the titles of the data entry zones) was done using the MAD task model [52].</td></tr><tr><td>UP: analysis and design</td><td>A first analysis consisted of studying the way in which studies are now carried out (manually). To facilitate the design process, a description of the data useful for the study and an outline of a Entity/Association model were generated.</td></tr><tr><td>U: specification and design of automatic modules</td><td>A first specification of calculation modules (age, duration of stay, risk of death) and of the transactions with the DBMS was carried out.</td></tr><tr><td>U: specification and design of interactive modules</td><td>A first specification of interactive modules was done using UML sequence diagrams and the MAD task model.</td></tr><tr><td>UP: implementation of the application</td><td>The implementation concerned only the database. The DBMS Oracle® and its tools (SQLplus...) were used.</td></tr><tr><td>U: HCI implementation</td><td>N/A in this iteration (no application intended for the user has been developed yet)</td></tr><tr><td>UP: technical tests</td><td>N/A in this iteration</td></tr><tr><td>U: user-centered tests</td><td>N/A t in this iteration</td></tr></table>

This development project should last several more years. At the time that this article was written, our user-centered, iterative, incremental process had resulted in: (1) the creation of a database, (2) the development of a data acquisition application and (3) the development of two data mining applications. The evaluation module is now under development [4]. The knowledge management module is expected to be brought under development soon. The various phases of our approach are described in more detail in the following section.

## 5.3. Implementation

In this section, we <sup>fi</sup>rst describe the activities undertaken to create the <sup>fi</sup>rst interactive KDD module in order to show how our approach can be implemented. Next, we provide a general explanation for one of the 2 data mining modules, illustrated by a screen shot of the interface of this data mining tool.

5.3.1. Implementation process of “storage and data acquisition” module

In this section, the progress of our approach towards the creation of the “Data acquisition and storage” module is described in 4 tables, one for each phase (initialization, development, construction and transition). The activities related to UP are presented on the lines with a grey background, and those related to the U model appear on the lines with a white background.

Development phase for the “storage and data acquisition” module

<table><tr><td colspan="4">Development</td></tr><tr><td>Activities</td><td>Iteration 1</td><td>Iteration 2</td><td>Iteration 3</td></tr><tr><td>UP Needs assessment</td><td>At the beginning, we were asked to store only the patient diagnoses. It was necessary to refine this information to indicate the type of pathology associated to the diagnosis. This would make it possible to carry out analyses on a particular type of pathology and also to compare the appearance of NI according to various pathology types.</td><td>Following the first tests, the users wanted other functions (patient searches, data modification and/or suppression). Moreover, it was not always possible for us to work at the hospital, so we needed to transfer the data to the laboratory. With Oracle, data transfers were difficult and complex. For this reason, we migrated towards the DBMS SQL Server.</td><td>As the data are recorded after the patients leave ICU, it is useless to record the date each time. A button for “next Day” and for “previous Day” would facilitate the data entry. Furthermore, filling out the forms created an additional workload for the interns. To compensate for this increased workload, our interlocutor asked us to offer interns full patient reports to reduce their workload by allowing them to avoid writing exit reports</td></tr><tr><td>U: analysis of the application domain</td><td>Thorough study of NI, especially with regard to the infectious examinations and the antibiotic regulations.</td><td>Further study of international and national researches about NI.</td><td>N/A in this iteration.</td></tr><tr><td>U: first interface prototypes. Description of the system&#x27;s functional and structural needs and task definition.</td><td>No change on the level of the initial architecture of the proposed HCI.</td><td>Addition of the possibility of searching for a patient in the database and of updating some data</td><td>Modifications of the HCI: check boxes or radio buttons to facilitate the data entry, to avoid errors and to make the data coherent, especially the values on which certain statistical tests are based. Addition of a “Report” button for launching a procedure recapitulating the patient&#x27;s history of hospitalization</td></tr><tr><td>U: user design</td><td>The user understood UP principles very well. He found it advantageous to be able to express other needs and to propose modifications over the course of the project. He was, in fact, an active participant in the approach.</td><td>N/A in this iteration</td><td>N/A in this iteration</td></tr><tr><td>U: definition and allocation of tasks to be executed</td><td>The thorough analysis of the NI domain allowed us to refine the definition of the tasks to be executed by the user/decision-maker); the MAD task model was thus adapted to reflect this finetuning.</td><td>Addition of tasks: display of the patients concerned when the user types a name, an index (administrative code) or a birth date; double clicking on the line corresponding to a patient results in a display of his/her contact information.</td><td>Addition of a selection task for the “Next Day” or “Previous Day”, a simplification of a task that previously required 11 mouse clicks. The entry of the date with the keyboard is still possible.</td></tr><tr><td>UP: analysis and design</td><td>A first use case diagram was set up, followed by other UML diagrams.</td><td>Modification of the diagrams to reflect the additional tasks.</td><td>Modification of the diagrams according to that</td></tr><tr><td>U: specification and design of the automatic modules</td><td>Use of UML diagrams for specifying and designing the application</td><td>Addition of the necessary procedures to display the patient data corresponding to the selection criteria.</td><td>N/A in this iteration</td></tr><tr><td>U: specification and design of the interactive modules</td><td>The sequence diagrams, the models obtained with the MAD task model in the initialization phase, as well as the first paper drafts produced with the users, enabled us to specify and design the HCI.</td><td>Modification of the diagrams to reflect the additional tasks.</td><td>N/A in this iteration</td></tr><tr><td>UP: implementation of the application</td><td>Implementation of the first data entry application</td><td>Implementation of a new DB using SQL Server and a new data entry application using C#.net</td><td>Implementation of a new version for entering daily information</td></tr><tr><td>U: implementation of the HCI</td><td>Implementation of the data entry HCI.</td><td>Where it is possible, the data entry zones were replaced by radio buttons or check boxes.</td><td>Modification of the data entry HCI by adding the buttons: “Next Day” and “Previous Day.”</td></tr><tr><td>UP: technical tests</td><td>Tests of different types of transactions in the DBMS with SQL as well as in Oracle® with Java application</td><td>Tests of the transactions with the new DBMS SQL Server (in place of Oracle).</td><td>Tests of the new version.</td></tr><tr><td>U: user-centered tests</td><td>Execution of user tests. Results: description of the usability problems related to data entry, detection of other needs for the doctors.</td><td>Execution of user tests. Results: tasks accomplished as expected, though with some HCI overlap.</td><td>Execution of user tests related to the dates. Results: simplifications of the data entry procedures</td></tr></table>

Table 4  
Construction phase for the “storage and data acquisition” module.

<table><tr><td colspan="3">Construction</td></tr><tr><td>Activities</td><td>Iteration 1</td><td>Iteration 2</td></tr><tr><td>UP needs assessment</td><td>N/A in this iteration</td><td>N/A in this iteration</td></tr><tr><td>U: analysis of the appl. domain</td><td>N/A in this iteration</td><td>N/A in this iteration</td></tr><tr><td>U: first interface prototypes</td><td>N/A in this iteration</td><td>N/A in this iteration</td></tr><tr><td>U: user design</td><td>N/A in this iteration</td><td>N/A in this iteration</td></tr><tr><td>U: def. and alloc. of tasks to execute</td><td>N/A in this iteration</td><td>N/A in this iteration</td></tr><tr><td>UP: analysis and design</td><td>N/A in this iteration</td><td>N/A in this iteration</td></tr><tr><td>U: specification and design of the automatic modules</td><td>N/A in this iteration</td><td>N/A in this iteration</td></tr><tr><td>U: specification and design of the interactive modules</td><td>N/A in this iteration</td><td>N/A in this iteration</td></tr><tr><td>UP: implementation of the application</td><td>Complete implementation of the application.</td><td>The last bugs linked to the application were corrected.</td></tr><tr><td>U: implementation of the HCI</td><td>Implementation of the various HCI, taking all the user&#x27;s remarks into account, especially concerning the addition of explanatory icons associated to the various buttons (+, Magnifying glass, Stop...).</td><td>The last bugs connected to the latest user tests were corrected.</td></tr><tr><td>UP: technical tests</td><td>Tests of the application in laboratory with fictitious data.</td><td>Tests of the final version.</td></tr><tr><td>U: user-centered tests</td><td>Execution of user tests comparing the specified tasks and the tasks really carried out by the user. Result: overall success, some remaining usability problems were highlighted.</td><td>Execution of user tests verifying the interface proposed had the characteristics of a quality interface (Coherence, error prevention...) and a final validation.</td></tr></table>

The initialization phase activities are presented in Table 2. During this phase, which has only one iteration, we mainly studied the context and de<sup>fi</sup>ned the objectives through regular meetings with the doctor dealing with the problem of nosocomial infections (NI), who played the double role of decision-maker and user. Sometimes his associates attended the meetings. The tasks were de<sup>fi</sup>ned and allocated with his total cooperation. During this phase, we also studied the NI that constituted the context of the project. Only a <sup>fi</sup>rst draft of the database set was concerned by the implementation. During this phase, no applications or interfaces were proposed to the user.

The iterations of the development phase (Table 3) are often the most numerous and most charged. During this phase, the user expressed new needs. The <sup>fi</sup>rst tests of the preliminary versions were very useful for the remainder of the development process. The interest the user showed for our approach allowed him to clearly express the evolutions of his objectives. As a result of his evolving objectives, we developed several versions, one for each of the three iterations.

The construction phase (Table 4) is principally made up of “Implementation” and “Testing” activities. Two iterations were suf<sup>fi</sup>- cient to obtain an almost <sup>fi</sup>nal version. The tests of the technical and functional aspects were performed with the expert user (the doctor).

During the transition phase (Table 5), we corrected some residual defects. The application now being used, with the data recorded in the database being exploited by both of DM modules (see Section 5.3.2).

Fig. 7 provides an idea of the signi<sup>fi</sup>cant changes made to the HCI over the course of the project. Fig. 7(a) shows the HCI of the very <sup>fi</sup>rst version, and Fig. 7(b) shows the HCI of an advanced version of the data acquisition application.

## 5.3.2. The data mining module

Once the module of “data acquisition and storage” was realized, we started developing the “data mining” module. The initial objective of this module was to help the doctor predict the probability of NI appearance for a patient entering ICU. We developed two applications for data mining based on the needs expressed by the expert users: (1) an application for predicting the appearance of an NI, based on the KNN technique [45] and (2) an application for calculating, displaying and printing out the status of NI outbreaks in ICU (Fig. 8). As for the previous module, this one was designed and implemented according to the user-centered UP/U approach.<sup>1</sup>

While the prediction module was being implemented, the needs evolved signi<sup>fi</sup>cantly: the original objective was to predict a possible NI outbreak when the patient was admitted or the day after. This objective was extended to allow the prediction to be calculated every day throughout the hospital stay due to the fact that patients see their state worsening or improving from the perspective of the risk of catching a NI during their stay in the ICU. The second “data mining” application involves statistical calculations. The objective was to make statistical studies of NI for each organ. As for all the DSS modules, the doctors showed a great interest for this type of studies. Fig. 8(a) shows a handwritten description (paper draft) of the way the doctor wanted to obtain the results; Fig. 8(b) shows the HCI created by taking his needs into account.

## 6. Discussion

In this work we showed that KDD is a process that helps experts to get knowledge that supports them to choose the “right” decision. DSS

Transition phase for the “storage and data acquisition” module.

<table><tr><td colspan="2">Transition</td></tr><tr><td>Activities</td><td>Iteration 1 (only one iteration)</td></tr><tr><td>UP needs assessment</td><td>N/A in this iteration</td></tr><tr><td>U: analysis of the application domain</td><td>N/A in this iteration</td></tr><tr><td>U: first interface prototypes.</td><td>N/A in this phase</td></tr><tr><td>U: user design</td><td>N/A in this iteration</td></tr><tr><td>U: definition and allocation of tasks to be executed</td><td>N/A in this iteration</td></tr><tr><td>UP: analysis and design</td><td>N/A in this iteration</td></tr><tr><td>U: specification and design of the automatic modules</td><td>N/A in this iteration</td></tr><tr><td>U: specification and design of the interactive modules</td><td>N/A in this iteration</td></tr><tr><td>UP: implementation of the application</td><td>N/A in this iteration</td></tr><tr><td>U: implementation of the HCI</td><td>Some slight improvements to the HCI were made (texts displays).</td></tr><tr><td>UP: technical tests</td><td>Test of the last version carried out with ICU patient data transcribed on the provided forms: no error detected.</td></tr><tr><td>U: user-centered tests</td><td>The user expressed his satisfaction and acceptance of the final module “data acquisition and storage.”</td></tr></table>

![](/api/attachments/GXQVR9V2/fulltext/images/8aeefa323d9ab997aa01f241bb16a65ada9c6293f6d20a9cbdad59eb2f512ed6.jpg)  
Fig. 7. Screen shot of the patient data HCI: (a) from the development phase (iteration 1); (b) from the construction phase (iteration 2).

and KDD converge in the fact that DSS can be based on KDD process. We have shown in Section 4.1 and Fig. 4 that a DSS can be based on KDD. A DSS is naturally interactive [6]; and according to Fayyad et al. [13], a KDD process should be interactive too. But when we studied the way they have to be set up, according to the authors, we noticed that they propose stages in the process development (see Sections 2.1 and 2.2). The stages, indicated for both DSS process and KDD process, start by the de<sup>fi</sup>nition of the problem and the objectives; and end by the choice of the decision, for the DSS process, and the use of the extracted knowledge to help choosing decisions, in the KDD process. As far as we know, no one has proposed any approach to develop a KDD-based DSS.

The motivation of this work is to propose an approach where the user is the principal actor all along the development period. So our approach must be a model that guides the developer to build up the system by respecting the interactivity and the iterativity qualities. In the literature we can found many models either for SE development, (such as the waterfall model [48], the V model [37], the spiral model [7] and the UP) or enriched under the HCI angle (such as the star model [19], the HCI-enriched V model [5] and the U model [1, 3]). But none of these models is adapted to develop a KDDbased DSS.

By studying the SE model we found that UP is the most appropriate one for iterative and interactive process; but as it is not user-centered, it has to be associated with a HCI model. Among the HCI-enriched development models, the U model is the one that imposes to the development team to take the human actor into consideration and it permits to make assessments cyclically; the tasks are then validated for each system prototype. Thus, as U model is generic to develop user-centered applications, it has to be adapted to the DSS context.

(a)  
![](/api/attachments/GXQVR9V2/fulltext/images/24551365b290a24ae2d1692c89627bb1ebe34f2857af3385e6062c8e5f034333.jpg)  
Fig. 8. Extracts of the HCI of the second data mining tool: (a) from the initialization phase (iteration 1); (b) from the construction phase (iteration 1).

The adaptation is also made to allow the U model to be used in association with the UP model.

As a result, to build a KDD-based DSS, we proposed a new usercentered approach (based on the use of the U model) by underlining the use of prototypes, the explicit positioning of the activities of the development process actors (lying on the UP). Our approach is then

[13] U. Fayyad, S.G. Djorgovski, N. Weir, Advances in Knowledge Discovery and Data Mining, AAAI/MIT Press, 1996.

called UP/U. In the following paragraphs, we will highlight the main implications for research and practice of our work.

The most important research contribution of this work is the proposed approach (UP/U) to develop a KDD-based DSS. UP/U is a generic approach that helps data miners to develop systems by involving the end user all along the KDD-based DSS process. Usually, Data Miners think about the ef<sup>fi</sup>ciency of their algorithm, more than about the ease of use for the end user. Our approach incite the developer to build up a user-centered DSS and to evaluate, with him/ her, the tasks he/she achieves from the beginning to the end of the development process. A DSS which is dif<sup>fi</sup>cult to use is generally dropped out by the user [31].

On addition, in many cases, the user either couldn't think of all his/ her needs or discover some needs during the project development. Then developer has to be very often near by the end user (or users) to: (1) detect those new needs and integrate them into the system, (2) implicate him/her all along the development process (so at the end he/she <sup>fi</sup>nd himself/herself familiar with the application), and (3) guarantee that the system evaluation (of utility and usability) is made from the beginning of the project. To make this choice we had to accomplish a critical study survey about the development models in the <sup>fi</sup>elds of SE and HCI <sup>fi</sup>elds. This survey allows us to note that no model associates both advantages of those of SE and HCI models. The survey conclusion led us to choose the Uni<sup>fi</sup>ed Process and the U model to build up our UP/U approach. Another important implication is the adaptation of the U model to our context. Thereby, we made it possible for the potential user to describe his/her functional needs and to evaluate and validate the different interfaces.

As a practical implication, we can note the development of a KDDbased DSS using our UP/U approach in a real context which is the <sup>fi</sup>ght against nosocomial infections. During this project we were able to involve physicians throughout the development of the KDD-based DSS. Indeed, as we have detailed in Tables 2 to 5, physicians were involved from the beginning to the end of the development process. The palpable implication for practice of this study is the <sup>fi</sup>nal product set up in the ICU of HBTH of Sfax. Indeed, nowadays the KDD-based DSS is set in that ICU and it is used to explain and prevent nosocomial infections. Each patient entering the ICU, has his/her data collected and used to predict and prevent a possible nosocomial infection.

## 7. Conclusion

This article is the result of work on a user-centered approach for designing DSS based on KDD. For the last several decades, companies have stored a signi<sup>fi</sup>cant amount of information electronically. Company's information systems are designed to keep track of events reliably and with integrity. They automate more business processes, particularly to decision support. To accomplish this automation, the KDD process is used as decisional tool that makes it possible to explore databases to discover previously unknown knowledge that is potentially useful for the decision-making. Since KDD-based DSS are highly interactive, designers of such systems must rely on elements from two separate <sup>fi</sup>elds, Software Engineering (SE) and Human– Computer Interaction (HCI).

After studying the models from both the SE and HCI <sup>fi</sup>elds, we proposed a user-centered approach, called UP/U, based on the Uni<sup>fi</sup>ed Process from the <sup>fi</sup>eld of the SE and the U model from the <sup>fi</sup>eld of the HCI. Using these two complementary methods allowed us to take advantage of the positive elements in both <sup>fi</sup>elds to develop decision support systems (DSS). To validate our approach, we designed and constructed a KDD-based DSS for a hospital Intensive Care Unit (ICU). This system aims to facilitate the <sup>fi</sup>ght against nosocomial infections contracted in such units. Throughout the entire process (needs assessment, task de<sup>fi</sup>nition, identi<sup>fi</sup>cation of typical user characteristics, modeling and prototyping, evaluation and validation), we were in constant contact with the physicians, the system's end-users. The <sup>fi</sup>nal DSS will have four modules: the <sup>fi</sup>rst two modules have already been developed using the UP/U approach, the third is still under development [4] and the fourth one remains at the project stage. An ongoing study relating to the module “data mining,” using dynamic Bayesian networks is underway [55].

In the short term, we plan to continue developing the two remaining modules (evaluation and knowledge management). In the long term, we expect to validate our UP/U approach on other types of KDD-based DSS, using other data mining techniques, such as association rules and Bayesian networks. The information produced by these techniques has a very complex form, especially for a user who is not a specialist in the <sup>fi</sup>eld of the arti<sup>fi</sup>cial intelligence. We hope to be able to facilitate the user's comprehension of this complex information. We also hope to propose a speci<sup>fi</sup>c evaluation methodology for DM-based DSS, taking as our starting point the evaluation criteria, methods and techniques used in the <sup>fi</sup>elds of HCI and visual data mining [35].

## Acknowledgments

The <sup>fi</sup>rst, second and fourth authors would like to acknowledge the <sup>fi</sup>nancial support provided by grants from the General Department of Scienti<sup>fi</sup>c Research and Technological Renovation (DGRST), Tunisia, under the ARUB program 01/UR/11/02. Thanks also to Dr. H. Kallel and all the ICU staff of Habib Bourguiba Teaching Hospital for their interest to the project and all the time spent to help us design, use and evaluate our system. The third author would like to acknowledge the Nord-Pas de Calais region, the French national government and the FEDER program for their <sup>fi</sup>nancial support of the TAC MIAOU and EUCUE projects, in which were studied models and methods that proved to be very useful within the framework of this study.

## References

[1] M. Abed, Contribution à la modélisation de la tâche par outils de spéci<sup>fi</sup>cation exploitant les mouvements oculaires: application à la conception et à l'évaluation des interfaces homme-machine PhD Thesis University of Valenciennes France 1990.

[2] M. Abed, J.M. Bernard, J.C. Angué, Task Analysis and Modelization by Using SADT and Petri Networks Proceedings Tenth European Annual Conference on Human Decision Making and Manual Control, Liege, Belgium, 1991.

[3] M. Abed, J.C. Angué, A New Method for Conception, Realisation and Evaluation of Man–Machine, Proceedings of the IEEE International Conference on SMC, 1994.

[4] R. Bahloul, M. Ben Ayed, A.M. Alimi, Vers une méthode d'évaluation de Système Interactif d'Aide à la Décision basé sur le processus d'ECD, Atelier: Évaluation des méthodes d'Extraction de Connaissances dans les Données, 10ème Conférence Internationale Francophone sur l'Extraction et la Gestion des Connaissances, EGC 2010, Hammamet, Tunisia, 2010, 26–29 janvier.

[5] S. Balbo, Evaluation ergonomique des interfaces utilisateur: un pas vers l'automatisation. PhD Thesis, University of Grenoble, France, 1994.

[6] M. Beynon, S. Rasmequan, S. Russ, A new paradigm for computer-based decision support, Decision Support Systems 33 (2002) 127–142.

[7] B. Boehm, A spiral model of software development and enhancement, Computer 21 (May 1988) 61–72.

[8] S.E. Brossette, A.P. Sprague, J.M. Hardin, K.B. Waites, W.T. Jones, S.A. Moser, Association rules and data mining in hospital infection control and public health surveillance, Journal of the American Medical Informatics Association 5 (4) (1998) 373–381.

[9] S.E. Brossette, A.P. Sprague, W.T. Jones, S.A. Moser, A data mining system for infection control surveillance, Methods of Information in Medicine 39 (4–5) (2000) 303–310.

[10] G. Calvary, Proactivité et réactivité: de l'assignation à la complémentarité en conception et évaluation d'interfaces Homme-Machine, PhD Thesis, Grenoble I, 1998.

[11] F.K.Y. Chan, J.Y.L. Thong, Acceptance of agile methodologies: a critical review and conceptual framework, Decision Support Systems 46 (2009) 803–814.

[12] S. Chaudhuri, U. Dayal, An overview of data warehousing and OLAP technology, ACM SIGMOD Record 261 (1997) 65–74

[14] G. Fischer, Human–computer interaction software: lessons learned, challenges ahead, IEEE Software 6 (1) (1989) 44–52.

[15] S. Gafsi-Moalla, Les infections acquises en réanimation, étude prospective réalisée dans le service de réanimation de Sfax sur une période de 3 mois, PhD Thesis, Faculty of Medicine of Sfax, Tunisia, 2005.

[37] J. McDermid, K. Ripkin, Life Cycle Support in the ADA Environment, Cambridge University Press, Cambridge, 1984.

[16] J.S. Garner, W.R. Jarvis, T.G. Emori, T.C. Hogan, J.M. Hugues, CDC de<sup>fi</sup>nitions for nosocomial infections, American Journal of Infection Control 16 (3) (1988) 128–140.

[17] D. Hand, H. Mannila, P. Smyth, Principles of Data Mining, MIT Press, Cambridge 2001.

[18] L. Herga<sup>fi</sup>, Présentation et validation d'un nouveau système pour la surveillance de l'infection acquise en réanimation, PhD Thesis, Faculty of Medicine of Sfax, Tunisia, 2006.

[19] D. Hix, H.R. Hartson, Developing User Interface: Ensuring Usability through Product & Process, Wiley, New York, 1993.

[20] ISO 13407, Human-centred Design Processes for Interactive Systems, The International Organization For Standardization, 1999.

[21] I. Jacobson, G. Booch, J. Rumbaugh, The Uni<sup>fi</sup>ed Software Development Process, Addison Wesley Longman, 1999.

[22] H. Kallel, M. Bouaziz, H. Ksibi, H. Chelly, C. Ben Hmida, A. Chaari, N. Rekik, M. Bouaziz, Prevalence of hospital-acquired infection in a Tunisian Hospital, Journal of Hospital Infection 59 (2005) 343–347.

[23] B. Kent, Extreme Programming Explained: Embrace Change, Addison-Wesley, 2000.

[24] M. Klein, L.B. Methlie, Expert Systems: A Decision Support Approach with Applications in Management and Finance, Addison-Wesley, 1990.

[25] C. Kolski, Interfaces Homme-Machine, application aux systèmes industriels complexes, Hermes, Paris, 1997.

[26] C. Kolski, A call for answers around the proposition of an HCI-enriched model, ACM SIGSOFT Software Engineering Notes 3 (1998) 93–96.

[27] C. Kolski, H. Ezzedine, M. Abed, Développement du logiciel: des cycles classiques aux cycles enrichis sous l'angle des IHM, Analyse et conception de l'IHM, Interaction Homme-Machine pour les SI, Hermes, Paris, 2001, pp. 145–174.

[28] M. Lajnef, M. Ben Ayed, C. Kolski, Convergence possible des processus du data mining et de conception-évaluation d'IHM: adaptation du modèle en U, in: Proceedings of IHM 2005, International Conference Proceedings Series, ACM Press, Toulouse (2005), pp. 243–246.

[29] C. Larman, Applying UML and Patterns, An Introduction to Object-Oriented Analysis and Design and the Uni<sup>fi</sup>ed Process, Third Ed., Prentice Hall, 2004.

[30] C. Larman, Agile and Iterative Development: A Manager's Guide, Addison-Wesley, Pearson Education, 2007.

[31] R. Lefébure, G. Venturini, Data Mining: Gestion de la relation client, Personnalisation des sites Web, Eyrolles, Paris, 2001.

[32] F. Lemieux, M.C. Desmarais, RUP et conception centrée sur l'utilisateur: une étude de cas in: Proceedings ERGO-IA'2006 Conference, 11-13 octobre 2006 Biarritz France, (2006) pp. 237–244.

[33] S. Lepreux, M. Abed, C. Kolski, A human-centred methodology applied to decision support system design and evaluation in a railway network context, Cognition Technology and Work 5 (2003) 248–271.

[34] S. Lepreux, Approche de Développement centré décideur et à l'aide de patrons de Systèmes Interactifs d'Aide à la Décision, PhD Thesis, University of Valenciennes, France, 2005.

[35] H. Lti<sup>fi</sup>, M. Ben Ayed, S. Lepreux, A.M. Alimi, Survey of Information Visualization Techniques for Exploitation in KDD, in: 7th ACS/IEEE International Conference on Computer Systems and Applications, AICCSA-2009, May 10–13, Rabat, Morocco, (2009) pp. 218–225.

[36] H. Lti<sup>fi</sup>, M. Ben Ayed, C. Kolski, A.M. Alimi, HCI-enriched approach for DSS development: the UP/U approach, in: 14th IEEE Symposium on Computers and Communications, ISCC 2009, July 5–8, Sousse, Tunisia, (2009) pp. 895–900.

[38] P. Millot, S. Debernard, Men Machines Cooperative Organizations: Methodological and Practical Attempts in Air Traf<sup>fi</sup>c Control, Proceedings IEEE SMC, Le Touquet, France, October 1993.

[39] H. Mintzberg, D. Raisinghani, A. Theoret, The Structure of “Unstructured” Decision Processes, Administrative Science Quarterly 21 (1976) 246–275.

[40] B.A. Myers, User Interface Tools: Introduction and Survey, IEEE Software 6 (1989) 15–23.

[41] D. Nakache, Data Warehouse et Data Mining, CNAM, Lille, 1998 accessible at: http: //home.nordnet.fr/\~dnakache/valeurc.

[42] J. Nielsen, Usability Engineering, Academic Press, Boston, 1993.

[43] D.J. Power, Decision Support Systems: Concepts and Resources for Managers, Quorum Books, Westport, 2002.

[44] S. Rathnam, M.V. Mannino, Tools for building the human–computer interface of a decision support system, Decision Support Systems 13 (1995) 35–59.

[45] C. Riesbeck, R. Shank, Inside Case-Based Reasoning, Lawrence Erlbaum, , 1989

[46] J.M. Robert, Que faut-il savoir sur l'utilisateur pour réaliser des interfaces de qualité? in: G. Boy (Ed.), Ingénierie cognitive, IHM et cognition, Hermes, Paris, 2003, pp. 249–283.

[47] M. Rosson, J.M. Carroll, Scenario-based design, in: J.A. Jacko, A. Sears (Eds.), The Human–Computer Interaction Handbook, Lawrence Erlbaum Associates, London, 2003, pp. 1032–1050.

[48] W. Royce, Managing the Development of Large Software Systems: Concepts and Techniques, WESCON, Technical Papers, 1970.

[49] J.R. Ruault, UML and interactive systems, another step forward, in: C. Kolski, J. Vanderdonckt (Eds.), Computer-aided Design of User Interface III, Kluwer Academic Publishers Dordrecht. 2002 pp. 243-256

[50] J. Rumbaugh, I. Jacobson, G. Booch, The Uni<sup>fi</sup>ed Modeling Language Reference Manual, Addison-Wesley Professional, 1999.

[51] D.L. Scapin, J.M.C. Bastien, Ergonomic criteria for evaluating the ergonomic quality of interactive systems, Behaviour and Information Technology 16 (1997) 220–231.

[52] D.L. Scapin, C. Pierret-Golbreich, Towards a method for task description, in: L. Berlinguet, D. Berthelette (Eds.), Proceedings of Conference on Working With Display Units, Elsevier, Amsterdam, The Netherlands, 1990, pp. 371–380.

[53] H.A. Simon, The New Science of Management Decision, Harper and Row, Prentice Hall, 1960.

[54] C. Suetens, A. Savey, J. Labeeuw, I. Morales, Le projet HELICS-ICU: vers une surveillance européenne des infections nosocomiales dans les unités de soins intensifs, Eurosurveillance 7 (9) (2002) 127–128.

[55] G. Trabelsi, M. Ben Ayed, M.A. Alimi, Système d'extraction des connaissances à partir des données temporelles basé sur les Réseaux Bayésiens Dynamiques, in: 10ème Conférence Internationale Francophone sur l'Extraction et la Gestion des Connaissances, EGC 2010, Hammamet, Tunisia, 26–29 janvier 2010, Revue des Nouvelles Technologies de l'Information RNTI-E-19, 2010, pp 241–246.

[56] M.C. Tremblay, R. Fuller, D. Berndt, J. Studnicki, Doing more with more information: changing healthcare planning with OLAP tools, Decision Support Systems 43 (2007) 1305–1320.

[57] E. Turban, Decision Support and Expert Systems, Macmillan, New York, 1993.

[58] E. Turban, J.E. Aronson, T. Liang, R. Sharda, Decision Support and Business Intelligence Systems, Pearson Education, 2008.

[59] G.C. Van der Veer, M.D.C. Puerta Melguizo, Mental models, in: J.A. Jacko, A. Sears (Eds.), The Human–Computer Interaction Handbook, Lawrence Erlbaum Associates, London, 2003, pp. 52–80

[60] J.R. Wilson, E.N. Corlett (Eds.), Evaluation of Human Works: A Practical Ergonomics Methodology, Second Ed., Taylor & Francis, 1996.

![](/api/attachments/GXQVR9V2/fulltext/images/2ffaef725db227ff0ccace022b35204552e129bffca46ba076eb08e19cad14f1.jpg)

Mounir Ben Ayed has a PhD in Biomedical Engineering. He is a member of the REGIM research unit, ENIS, University of Sfax, Tunisia. He is an assistant professor; he teaches DBMS, data warehouse and data mining. His research activities concern DSS based on a KDD process. Most of his research works are applied in health care domain. He is an author of many papers in international conferences Mounir Ben Ayed has been a member of organization committees of several conference, and particularly co-chair of the ACIDCA-ICMI'2005 organization comitee. He is currently the Director of Training at the Faculty of Sciences of Sfax.

![](/api/attachments/GXQVR9V2/fulltext/images/425e6e6ef88080065f52a6822eafc095f4ea1bdca0bc2a1323dd37e67d947592.jpg)

Hela Lti<sup>fi</sup> is currently a doctoral in computer science. She is a member of two laboratories: REGIM (ENIS, Tunisia) and LAMIH (Univ. Valenciennes, France). Her research activities concern DSS based on a KDD process and user-centred design; her application domain is hospital infections. She is a co-author of several papers in international conferences

![](/api/attachments/GXQVR9V2/fulltext/images/19b882c712bfd8597a932e672b46f7c68669907aca1e43697d73adc53fcbf4ce.jpg)

Christophe Kolski has obtained his Ph.D in 1989. He is a professor in Computer Science at the University of Valenciennes (France) and head of the “Human–Computer Interaction and Automated Reasoning” research group in the LAMIH. He is involved in several research networks, projects and associations and is a referee for many scienti<sup>fi</sup>c journals and conferences. He is specialized in human–computer interaction, software engineering for interactive systems and intelligent system design. He is an author or a co-author or several books, more than 40 articles in journals and more than 100 communications in conferences.

![](/api/attachments/GXQVR9V2/fulltext/images/fa8c515ab5374cf59b7c872876bea6d67c37353b37f7757af27bed14cf9e7da1.jpg)

Adel M. Alimi is a professor in industrial informatics. He is the head of the REGIM research unit, ENIS, University of Sfax, Tunisia, He was chair of the 2nd ACIDCA-ICMI'2005 International Conference on Machine Intelligence, co-chair of the SCS'2004 International Conference on Signals, Circuits & Systems, and chair of the ACIDCA'2000, International Conference on Arti<sup>fi</sup>cial & Computational Intelligence for Decision, Control and Automation. He has been member of program committees of several conferences Adel M. Alimi is an author, co-author, editor or co-editor of book chapters, special issues of journals, and of many articles in journals and international conferences
