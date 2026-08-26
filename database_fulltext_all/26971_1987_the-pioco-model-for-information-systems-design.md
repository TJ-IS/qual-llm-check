---
otero_id: 26971
otero_key: "YA4ARQN7"
title: "The PIOCO Model for Information Systems Design"
authors: "Juhani Iivari; Erkki Koskela"
year: "1987"
journal: "MIS Quarterly"
doi: "10.2307/248688"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
The PIOCO Model for Information Systems Design
Author(s): Juhani Iivari and Erkki Koskela
Source: MIS Quarterly, Vol. 11, No. 3 (Sep., 1987), pp. 401-419
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248688
Accessed: 28/08/2013 02:59

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# The PIOCO Model for Information Systems Design

By: Juhani livari
Erkki Koskela
University of Oulu
Institute of Data Processing Science
Linnanmaa, SF-90570 OULU 57
Finland

## Abstract

The PIOCO model is a comprehensive methodology for information systems (IS) design consisting of a metamodel for an information system, the corresponding description languages, a process model for information systems design, and a model for choice and quality criteria. The metamodel for an information system consists of three levels of abstraction and forms a profound and articulated conceptual basis for the PIOCO model for the IS design process.

The article gives an overview of the PIOCO approach from a management perspective, emphasizing the role of IS design as an inquiry process supporting the decision-making concerning the information system, the quality criteria related to the IS design, and the use of the PIOCO model as a macro-framework which integrates more detailed micro-level methodologies, methods, techniques and tools.

Keywords: Information systems, systems analysis and design, application development, quality criteria.

ACM Categories: D.2, H.1, H.2, K.6

This work was supported by the Academy of Finland.

## Introduction

There is general agreement in the area of information systems (IS) design, that the state of this art is, in practice, quite unsatisfactory. This state is often described by the phrase 'software crisis' referring to the poor quality of systems, excessive costs, schedule and budget overruns, implementation problems, etc. Vick [53] suggests that the problems lie not in the lack of methods, techniques and tools, but in their fragmentation. We largely agree with this viewpoint, but at the same time we wish to point out that the fundamental problem is our limited understanding of IS design and, in particular, its basic principles.

The purpose of this article is to give an overview of the PIOCO model for IS design, paying special attention to its basic principles and most distinctive features. The term 'PIOCO' is an acronym derived from the three main viewpoints of systems analysis $[29, 30]$ : pragmatic (P), input/output (I/O) and constructive/operative (C/O). The pragmatic considers a system as an element of its environment, paying attention to its purpose and impact; I/O considers its external behavior; and C/O its structure and internal behavior.

The development of the PIOCO model began in 1978. In addition to the earlier PSC model $[29, 30]$ , it has been especially influenced by the Scandinavian tradition $[9, 32, 37, 49]$ . Compared with alternative IS design methodologies, the development of the PIOCO model has been governed by the following five ideas:

\- Decision-making orientation. Most IS and software design methodologies and frameworks view the design process as a sequence of transformations of successive representations of the product (e.g. [17, 35, 37]). This is a significant aspect, but it is also important to recognize that at the same time the IS design process is, or should be, an inquiry process supporting decisions to be made concerning the information system to be developed.

\- Contingency approach. The proliferation of IS design methodologies, methods, techniques and tools implies a problem of selecting appropriate methodologies, etc., for each situation. The contingency idea, that there is no detailed IS design methodology which is best in all situations, is widely accepted now and has been highly influential in the development of the PIOCO model. But for reasons to be examined later, we have included the contingency approach within the PIOCO model as its flexibility requirement. Briefly, the PIOCO model integrates existing IS design methodologies, methods and techniques into a common framework to promote the flexible, situation-dependent application of these detailed methodologies.

\- A balanced organizational, conceptual and technical view. IS design methodologies evolved during the 70's from technically oriented methodologies toward conceptual ones, emphasizing the specification of the information system in a way which is, as far as possible, independent of the technical implementation of the system. Even though the importance of this principle is generally recognized by researchers, it is often neglected in practice. In more recent times researchers have become aware of the need for one further level, in which IS development is viewed as a form and constituent of organizational change. The P, I/O and C/O viewpoints in the PIOCO model correspond to the organizational, conceptual and technical perspectives: the P viewpoint reflecting the perspective of all interest groups affected by the organizational change, management in particular; the I/O viewpoint being that of users of the system; and the C/O viewpoint reflecting EDP experts.

\- The dynamics of IS design process. The dynamics of the IS design process are usually framed in terms of the systems development life cycle developed to support project management by means of well-defined phases outlining the milestones and baselines of the IS design process. More recent prototyping and evolutionary approaches have been suggested as alternatives to the traditional life cycle approach, but have led to project management problems in practice [2]. Even though the inherently iterative process of the prototype approach inevitably requires more flexible project management practice, the difficulties encountered in prototyping can be attributed to its use in inappropriate situations and without sufficient discipline. The PIOCO model suggests that it is by no means necessary to interpret these two approaches as strict alternatives, but instead that they can be considered complementary to each other.

In fact, the PIOCO model is an integrative framework, including:

– life cycle dynamics of information systems based on an hierarchical concept of IS evolution taking place at the three levels of abstraction,

\- main phase dynamics of IS design to define the main phases required for the generation of each new life cycle,

\- learning dynamics of IS design, suggesting a flexible process-mode of project planning as an alternative to the more traditional blueprint mode, and

\- the non-linear structure of main phases.

\- IS assessment. IS design always includes explicit and implicit consideration and selection of alternative information systems based on various criteria. In spite of this importance, issues related to IS assessment and selection are largely neglected in IS design methodologies. Due to its decision making orientation the PIOCO model suggests three complementary sets of criteria for the IS assessment: effectiveness, user satisfaction and efficiency criteria.

The whole PIOCO model consists of four major parts:

1. The metamodel for an information system

2. The model for the IS design process

3. The model for choice and quality criteria

4. The description languages for an information system

We shall concentrate on the first three components of the PIOCO approach, excluding the description languages due to the limited space available for this article. The general research problems concerning these three components are summarized in Table 1, the major purpose of which is to indicate that the three models form an integrated whole. The PIOCO metamodel for an information system explicitly defines the product of information systems design, since such an understanding is regarded as a necessary prerequisite for a clear and explicit discussion of the design process. It is divided into the P, I/O and C/O metamodels, describing the information system in the context of its host organization, the user-oriented specifications for the system, and its technical solution.

The PIOCO model for the IS design process defines the design process itself, which is divided into three main design phases supporting the selection of the information system at the three levels defined by the P, I/O and C/O metamodels. The three design phases are followed by the implementation phase in which the information system is realized and institutionalized in the host system.

The PIOCO model for choice and quality criteria expresses and explicates the values underlying the PIOCO model for the IS design process. The choice of the P model is assumed to be based on the cost/effectiveness criterion, the choice of the I/O model on the cost/user satisfaction criterion, and the choice of the C/O model on the total efficiency criterion.

The scheme of problems outlined in Table 1 illustrates that it is beyond the scope of this article to describe the PIOCO model and its research problems in detail. Our aim is to provide an overview emphasizing the management perspective. In order to emphasize this perspective we will first analyze the interaction between the IS design and the steering committee which makes the principal decisions concerning the system and controls the IS design process. Following sections detail the three components of the PIOCO model, and finally we summarize the whole paper.

## IS Design and Decision-Making Interaction

The PIOCO model is based on the sociocybernetic metamodel which explains IS design in terms of information economics $[39]$ as an interaction between the steering committee and the IS design group $[22, 23]$ . The idea is to regard the IS design process as an inquiry process supporting the steering committee. The sociocybernetic metamodel emphasizes the following points:

Table 1. The Major Research Problems Addressed by the PIOCO Approach  
![](/api/attachments/YA4ARQN7/fulltext/images/0a5bfc801cb690115ecbd6e7967d93c906c0bd5be50aa8eb8bd012321c4358ab.jpg)

1. IS design always includes explicit and implicit consideration and selection of the alternative information systems.

2. It is the responsibility of the steering committee to make the major decisions concerning the information system.

3. The IS design group should promote the free and informed choice of an information system by providing the steering committee with information.

4. The effectiveness of the IS design process should be evaluated in terms of the quality of the information produced for the steering committee [25].

As Figure 1 suggests, the role of the IS design group is to provide information to assist the steering committee in deciding on the IS design alternatives and controlling the IS design process. This information will include:

![](/api/attachments/YA4ARQN7/fulltext/images/3db3afb1282dd3c22657b61b248398fb23cf5d5e0084fa1ca141211594af5bc6.jpg)  
Figure 1. IS Design and Decision-Making Interaction

\- the interest groups and their values

\- the exogenous factors and causalities coproducing the effects of the information system,

\- IS alternatives

\- the internal (or formal) quality of the IS alternatives (e.g., consistency and completeness),

\- the feasibility of the IS alternatives with respect to the constraints imposed,

\- the external quality of the information system (e.g., effectiveness, user satisfaction and efficiency), [25].

Chris Argyris proposes free and informed choice as the basic requirement for intervention [3], and we suggest that this can also be regarded as an ideal for interaction between the IS design group and the decision-making unit. It is an ideal in the sense that it can never be satisfied completely, but approximations can be made. Free and informed choice implies that the decision-making unit is prepared to retain its autonomy vis-a-vis the design group, and to take responsibility for IS development. This requires that the participants of the decision-making unit have a reasonable understanding of IS development, because it is possible that the decision-makers may “prefer to give up their responsibility and their autonomy, especially if they are feeling a sense of failure” [3, p. 19].

Due to its information economy background, the sociocybernetic metamodel considers IS design to be, in a way, complementary to a priori knowledge. This idea, in combination with the situation dependency of IS design, suggests that it should represent reflective rather than unreflective obedience to some detailed IS design methodology.

The contingency idea that there is no detailed IS design methodology which is best in all situations has been one of the governing ideas in the development of the PIOCO model. The contingency approach is widely recognized, but the fact that it makes IS design more complicated for the participants involved has remained quite unnoticed. The situation-dependent application of IS design methodologies means that the participants should be able to diagnose IS design situations relevant to the assessment of alternative IS design methodologies, methods, techniques and tools, and they should master all these constituents of methodologies. It is quite obvious that mastery of this kind soon exceeds the cognitive capabilities of even the most competent IS designers.

How can one deal with this problem? It is our firm conviction that we should have a higher order IS design methodology in which the contingency idea is encompassed. This macro-level model would include alternative micro-level models for different problem areas in IS design, and instructions for the selection of the appropriate micromodel depending on the situation. It is important, however, that the micro parts are integrated in the macromodel in order to ensure consistency and conformity in IS design within organizations and in order to reduce the cognitive burden imposed upon IS designers and the other participants involved. The PIOCO model has been developed to serve as a macromodel of this kind.

## The PIOCO Metamodel for an Information System

Information systems are often quite complex. There are two major sources of this complexity: the scope of the application domain (e.g. the number of transaction types processed) and the inherent multidimensionality of information systems. They are not only technical systems, but also, and more primarily, organizational and social communication systems.

The complexity of information systems is usually handled by means of two modeling principles, which are unfortunately often confused one with the other: the principle of hierarchical decomposition (levels of detail) and the principle of levels of abstraction. Hierarchical decomposition is primarily a means of coping with domain complexity, whereas levels of abstraction deal with social complexity [42]. It is interesting to observe the considerable difference in the application of these principles between two central subfields of IS design. Database research is very heavily based on the latter principle, since the relationships between the levels of abstraction are mapping relationships similar to mappings between conceptual and internal schemas in database architectures. The software engineering literature, on the other hand, typically reflects more the former principle of hierarchical decomposition or refinement and of ten confuses the two principles. For instance, Ramamoorthy, et al., describe the distinction between specification and design as follows: "The design phase specifies how the system is to be implemented. It includes decomposition of the requirement specification into certain basic elements . . ." [47, p. 196].

There are fundamental differences between these principles. In the case of hierarchical decomposition, the number of levels (total system, subsystem, sub-subsystem, etc.) is not fixed in advance, but is determined during the application in question, whereas in the case of levels of abstraction, the number of levels is determined by the underlying “theory.” In the case of information systems there is growing agreement about the usefulness of distinguishing three levels of abstraction in information systems.

Level A: Defines the organizational context of the information system

Level B: Defines the conceptual/infological specification of the information system

Level C: Defines the technical/datalogical structure of the information system.

These levels correspond quite closely to the systeological, infological and datalogical perspectives as defined by Welke [56]. In the PI-OCO model these levels correspond to the pragmatic (P), input output (I/O) and constructive operative (C/O) metamodels for an information system. We call these metamodels because they are, in a way, conceptual grammars for defining the actual P, I/O and C/O models specific to each information system.

In the PIOCO metamodel for an information system each of the three metamodels is defined as an hierarchical structure of concepts. We will introduce here only the upper concepts in this hierarchy as a kind of macro-model for an information system and its major background ideas. The concepts are depicted in Figure 2 using an application of JSP notation (\* for iteration).

## Pragmatic model

The pragmatic (P) model for an information system is defined as a restricted, planned change in the host system/organization. The change may concern both systemized (formal) and unsystemized (informal) information systems, as well as other structural factors such as personnel, organizational arrangements, working procedures, technological arrangements, etc. From the viewpoint of the individual information system, the P model identifies the input and output users, includes a rough definition of the input and output information types and their relationships to the users' activities (I/O model), and may also outline the technical structure of the system in rough terms (C/O model). The I/O and C/O characteristics are specified to the extent that the interest groups and actors are able to evaluate the organizational change implied by the information system.

The rationale underlying this definition is discussed most thoroughly in a previous paper [22]. We concentrate here on some of the major ideas and points which clarify these. Our main assumption here, reflecting modern socio-technical thinking, can be expressed in the words of Bostrom and Heinen “An integration between the MIS technology and other technologies is needed to produce a more effective intervention. . . . These techniques coupled with a MIS intervention would allow us to pursue the goal of joint optimization” [8, p. 27]. The P model defines this total ‘intervention’ and the development of information systems as a potential ingredient of this change.

The idea of a planned change leads us to one of the major aspects of the P model, the organizational implementation or institutionalization of a planned change. It is very important to take this implementation aspect into account as a precondition for successful institutionalization, to establish a set of complementary changes (e.g., compensating for the potential negative impacts upon some interest groups or actors) and, more generally, to develop a congruence relation between the planned information system and its societal, organizational and user environments. These three means closely correspond to the people-oriented, system-oriented and interaction theories of resistance to change identified by Markus [40]. The implementation aspect in the P model means that implementation, or more strictly the problems associated with institutionalization, will be taken into consideration in the very first phase of IS development.

![](/api/attachments/YA4ARQN7/fulltext/images/9d987d789ce2898a71b51ff8c569710d39cb418c8aa5d95a08330f82e22c482a.jpg)  
Figure 2. An Overview of the PIOCO Metamodel for an Information System

The phrase ‘restricted, planned change,’ used in our characterization of the P model, points out that the change is assumed to form an investment entity which cannot be decomposed into separate investments due to joint benefits and costs. This means that the PIOCO model is oriented towards the small-scale development of individual, or clustered application-oriented information systems (e.g., DSSs) rather than to the large-scale development of total MISs, which we regard as evolutionary supersystems made up of individual application-oriented information systems.

## The input-output (I/O) model

The input-output (I/O) model determines the primary information (data) and its processing rules at the infological level (omitting technical solutions) and the external behavior of the system (i.e., the user-system interaction). The I/O model presents the information system from the viewpoint of the user. This includes local views relevant to each individual user and an integrated view defining the whole information system as a formal organizational communication system. At the I/O level the information system is regarded as an abstract system of interacting information process types and related information types. Primary information means that we do not pay attention to the secondary information needed in various control, quality monitoring and supporting activities (C/O model). In fact, one of the major ideas of the I/O model, in addition to its technology independency, is to assume an ideal, error-free world. This makes it possible for users to concentrate on the complexity and fuzziness of the primary information requirements at this level.

The I/O metamodel is defined more formally as a quadruple object system model, information model, information process model, interaction model (see [20,22] for a more formal definition). This structure is based on a clear conceptual distinction between information modeling, (specification of the information to be communicated by the information system), and reality modeling, (specification of the conceptual model for a slice of reality, or the object system or universe of discourse) about which the system should provide information.

In the realm of information modeling the information system is specified by means of three submodels:

\- the information model specifies the semantic content and syntactic form of information types included in the information system,

\- the information process model defines the derivation rules for the non-initial information types and the related control of information process types,

\- the interaction model specifies the interaction process types in terms of dialogue techniques [38] and the transaction information types between the information system and its input and output users.

These three models define the information system proper in user-oriented terms and de-limit the parts of the object system which are of interest to users. The object system underlying the information system is expressed by the object system model defining the entity, association and event types. The latter are dynamic in the sense that the occurrence of any event causes changes in the state of the object system.

## The constructive-operative (C/O) model

The constructive-operative (C/O) model determines the internal structure and action of an information system (i.e., the primary data and its processing rules at the datalogical level), the control and supporting activities, and the technical implementation of the information system. In accordance with this characterization, the C/O metamodel is defined as a triplet primary action model, control and supporting action model, implementation model (see [22] for more formal definitions).

The primary action model is decomposed into the data model and the data process model, similarly to the distinction between information and information process models in the I/O metamodel. The level of abstraction is different, however, including the technical structure of databases and algorithmic structure of programs at the C/O level.

The distinction between the primary action and the control and supporting action models implies a distinction between primary and secondary data. The primary data corresponds to the information/data identified in the I/O model, while control and supporting activities may have their own, often considerable, information requirements, including consistency or integrity rules to be used in data validation, access control information, help information, etc. It is beyond the scope of this paper to discuss these features in any more detail. Our only comment is that the systematic consideration and design of these activities is assuming increasing importance in modern, interactive, real-time systems.

One of the major ideas of the C/O model is to make a clear distinction between technology-dependent and equipment-dependent solutions for a data system. The technology-dependent solution is defined by the first two components of the C/O model, while the equipment-dependent solution is designed in the last one which outlines the human, hardware and software resources to be used in the technical implementation, and the adaptation of the system defined by the previous models to the selected resource environment.

## Summary

The three models introduced above define explicitly the product of IS design at three levels of abstraction. These levels have quite a natural relationship to the major interest groups or stakeholders affected by and involved in IS development. The P model reflects the view of all interest groups affected by the organizational change, forming an overall view which is particularly relevant to management. The I/O model reflects the viewpoint of users, including input and output users as well as primary and secondary users $[13]$ . The borderline in the case of secondary users is not totally fixed, since some secondary users may be included in the manual subsystems of the whole information system (operators). We regard it as a general rule in this case that secondary users who use the information system as an integral part of their larger job, which cannot be regarded as information system support work, should be taken into account at the I/O level. Finally, the C/O model reflects the viewpoint of EDP professionals and operating staff.

We shall now proceed to IS design as a process. This discussion is very heavily based on the PIOCO model for an information system introduced above, since the baselines, milestones and main phases are defined in terms of the three metamodels for an information system. This relationship between the IS design process and the levels of abstraction is not, nevertheless, assumed to be so straightforward as in existing linear life cycle models.

## The PIOCO Model for the IS Design Process

It is becoming customary to distinguish two alternative approaches to IS development: the traditional life cycle approach and the more recent prototyping approach $[13, 43]$ . This may be quite a valid classification of the current approaches used in practice, but from the viewpoint of the development of IS design methodologies it is not necessarily very fruitful. Instead we suggest an integrative approach which includes features of both:

\- Life cycle dynamics. First of all, the PIOCO model leads us to conclude that the life cycle metaphor, suggesting that information systems have some definite life cycle consisting of initial development and operation and maintenance, should be replaced by a metaphor of IS evolution consisting of successive life cycles of the operational system at the three levels of abstraction (P, I/O and C/O). This concept of evolution discards the old dichotomy between initial development and maintenance [35] and gives a more realistic image of IS evolution in practice.

\- Main phase dynamics. Secondly, each new life cycle is generated by an IS design process consisting of well-defined main phases (P, I/O and C/O). Each main phase includes the selection and freezing of the information at the corresponding level of abstraction. In accordance with traditional life cycle models, the main phase determines the milestones and baselines of the IS design process [7]. The baselines correspond to the three metamodels for the information system (P, I/O and C/O) which define formal criteria for the evaluation of the completion of each main phase. The criteria facilitate effective project management and control.

\- Learning dynamics. Each main phase consists of successive subphases (iterations) which may be repeated depending on the learning process during the IS design process. The purpose of learning dynamics is to make some of the inevitable iterations explicit in order to support realistic project scheduling and cost estimation. The concept of learning dynamics also suggests a flexible process-mode of project planning as an alternative to the more traditional blueprint mode of planning $[16]$ . The flexible structure of main phases is totally compatible with the iterative structure adopted in prototyping. Although prototyping differs in many respects from traditional life cycle approaches, the PIOCO model proposes that it is not essentially the use of prototypes which makes the difference. It is also significant that prototyping in the PIOCO model is applied in the context of well-defined main phases, implying a more disciplined practice of prototyping.

Table 2. The PLOCO Model as a Macro-Framework of IS Design

<table><tr><td>Model for IS</td><td>Viewpoint</td><td>Reference Discipline</td><td>Methodological Background</td><td>Specific Methodologies etc:</td></tr><tr><td>P model</td><td>All interest groups generally and management in particularTotal effectiveness criterion</td><td>Organization theoryEconomicsSociologyCyberneticsDecision sciencesWork sciences</td><td>Methods of organizational change, design and development, Socio-technical designImplementation approaches</td><td>ETHICS [41]ISAC (change analysis) [37]</td></tr><tr><td>I/O model-object system model</td><td></td><td rowspan="4">Communication theoryLinguisticsSemioticsCognitive psychologyErgonomicsFormal logic</td><td>Conceptual modelling of UoD</td><td>CIM [9]EAR [10]NIAM [52]</td></tr><tr><td>-information model</td><td>Input/output users</td><td>Information modeling</td><td>RM [11]RM/T [12,14]</td></tr><tr><td>-information process model</td><td rowspan="2">Total user satisfaction</td><td>Information requirements analysis/specification</td><td>ISAC (information analysis [37]SA [15]SADT [46]SREM [6]RM (query languages)</td></tr><tr><td>- interaction model</td><td>Human-computer interaction</td><td>USE [55]</td></tr><tr><td>C/O model-data model</td><td></td><td rowspan="4">Computer scienceElectronicsMathematicsErgonomics</td><td>Data base systems file structures</td><td>DBTGIMS RM</td></tr><tr><td>-data process model</td><td>ADP professionalsOperations personnel</td><td>Algorithm/program design, Data structures</td><td>JSP [27]WaOr [44,54]</td></tr><tr><td>-control and supporting action model</td><td>Total efficiency</td><td>Security</td><td></td></tr><tr><td>- implementation model</td><td></td><td>Specific HW and SW technology for the technical IS implementation</td><td></td></tr></table>

\- Non-linear structure. Most traditional life cycle models have a linear structure. The non-linear structure of the PIOCO model emphasizes the need for the steering committee to possess information on the cost of alternatives for the system at each level of abstraction. It also makes some of the inevitable iterations explicit and therefore supports more realistic project scheduling and cost estimation.

Referring to the discussion above, it is quite obvious that the PIOCO model for the IS design process is a radically different approach which does not directly fit into the existing classifications. This fact may make it somewhat difficult to understand. In order to reduce this difficulty we shall concentrate entirely on the PIOCO model for IS design at its macro-level.

## Main phase dynamics

The main phase dynamics of the PIOCO model are based on the decomposition of decision making concerning the information system into three parts according to the structure of the PIOCO metamodel for an information system:

1) The P model is chosen in the first, pragmatic (P) main phase using the cost/effectiveness criterion.

2) The I/O model is chosen in the second, input-output (I/O) main phase using the cost/user satisfaction criterion.

3) The C/O model is selected in the third, constructive-operative (C/O) main phase using the total efficiency criterion.

4) The information/data system is implemented in the fourth main phase.

We shall return to the effectiveness, user satisfaction and total efficiency criteria later. At the moment it is important to be aware of the assumption that the decision-making unit (steering committee) has sufficient belief in the realizability of a candidate model to choose, and sufficient knowledge of the expected costs of the model $[22]$ . Both of these requirements imply that the decision-making unit has some knowledge of C/O models. This leads us to the non-linear structure originally proposed by Kerola $[30]$ in simplified form, omitting the learning dynamics.

$$
\begin{array}{c} 1. \text {Pragmatic main phase} \\ (\text {choice of P model}) \\ P _ {D} ^ {1} (I / O _ {D} ^ {1} (C / O _ {D} ^ {1} C / O _ {T} ^ {1}) I / O _ {T} ^ {1}) P _ {T} ^ {1} \end{array}\tag{\( n^{1} \}
$$

$$
\begin{array}{c} 2. \text {Input - output main phase} \\ (\text {choice of I / O model}) \\ I / O _ {D} ^ {2} (C / O _ {D} ^ {2} C / O _ {T} ^ {2}) I / O _ {T} ^ {2}) P _ {T} ^ {2} \end{array}\tag{\( n^{2} \}
$$

$$
\begin{array}{c} 3. \text {Constructive - operative main phase} \\ (\text {choice of C / O model}) \\ C / O _ {D} ^ {3} C / O _ {T} ^ {3}) I / O _ {T} ^ {3}) P _ {T} ^ {3} \end{array}\tag{\( n^{3} \}
$$

$$
\begin{array}{c} 4. \quad \text { Implementation } \\ (\text { producing   the   real   data   system }) \\ B C / O _ {T} ^ {4}) I / O _ {T} ^ {4}) P _ {T} ^ {4} \end{array}
$$

In this notational formulation $P_{D}$ denotes the P design, $I/O_{D}$ the I/O design, $C/O_{D}$ the C/O design, B the realization, $C/O_{T}$ the C/O testing, $I/O_{T}$ the I/O testing and $P_{T}$ the P testing of the information/data system in the respective main phases. The notation $n_{i}$ (i = 1,2,3) is related to learning dynamics and means that the respective subphases are repeated $n_{i}$ times, where the number of repetitions is in the general case determined by the learning process and cannot be known in advance.

Design and testing at each level of abstraction have a general structure: design processes $(P_{D}^{i}, I/O_{D}^{i}, C/O_{D}^{i})$ include diagnosis (e.g., interest group, problem, situation, future, constraint and goal analysis) and generation and refinement of alternatives. Testing processes $(P_{T}^{i}, I/O_{T}^{i}, C/O_{T}^{i})$ on the other hand comprise testing of internal quality (the consistency and completeness of the models for the system), testing of feasibility (relative to models chosen for the system and to special constraints (cf., verification in [7]) and evaluation of the external quality of the system (cf. validation in [7]).

In order to clarify the main phase structure, let us analyze the I/O main phase in greater depth. Since the P model has been selected in the preceding P main phase, there is no P design in the I/O main phase. The main problem in this phase is to diagnose or analyze the information requirements of the users and to design an I/O model satisfying the given P model which, if not optimal, is at least reasonably good when evaluated by the cost/user satisfaction criterion. The process $I/O_{D}$ produces candidate I/O model alternatives and the process $C/O_{D}$ , corresponding C/O models for the estimation of the realizability and costs of the I/O models to be analyzed.

The testing process $C/O_{T}$ assesses the internal quality (consistency, completeness, etc.) of the C/O models designed, and their feasibility. It also produces the cost estimates required in I/O decision making. In addition to the assessment of internal quality and feasibility with regard to the given P model, the process $I/O_{T}$ also includes the evaluation of external quality (satisfaction with the alternative I/O models among the user community). The testing process $P_{T}$ is essentially a monitoring process which evaluates whether the experience obtained in the I/O main phase necessitates any change in the P model (corrections) or in the corresponding decision. It is beyond the scope of the present paper to analyze this structure more thoroughly. For a more complete explanation, we refer to [22].

The P, I/O and C/O models form the baselines for the main phases in the sense that they are fixed or frozen for the following main phases and can be changed only by using a formal procedure. The other information delivered by the main phases (e.g. due to the non-linear structure) does not have a similar prescriptive status, but can be used in later phases if this is considered reasonable. Since the I/O and C/O models have quite formal metamodels which can be used for testing the formal completeness of the corresponding models, the endpoints or milestones of the I/O and C/O main phases can be defined quite rigorously. Both main phases end when the desired information system is completely fixed at the corresponding level of abstraction. In the case of the P main phase the borderline with the I/O main phase is more fuzzy and must be decided on a more intuitive basis.

If we finally compare the non-linear structure with the linear structure of traditional life cycle models, it is important to observe that the actual IS design process according to some linear model often turns out to be a non-linear process due to various iterations. Some of these iterations are due to the decision-making criteria to be used in the selection of the information system. Since a non-linear structure is, in our view, a logical necessity if those assumptions are accepted (see also $[50, 51]$ ), our aim has been to make these inevitable iterations explicit constructs. It can be expected that compared with linear models, this non-linear structure will reduce the number of unplanned iterations to earlier main phases and will give a more realistic view of the IS design process in terms of project scheduling and cost estimation. This point is clearly recognized by Boehm $[7]$ in the case activities of his waterfall model, where he breaks the phases into activities which clearly imply a non-linear structure (p. 50) and which have their own resource requirements (pp. 99–101).

## Learning dynamics

We do not assume in the PIOCO model that IS design or its main phases are completely programmed and scheduled processes, but rather that they consist of sub-phases, the number of which is in the general case determined by learning dynamics and cannot be known in advance. After each sub-phase the increased experience and knowledge is used to evaluate whether it is reasonable to continue the main phase in question.

Traditional life cycle models treat learning in terms of unplanned iterations. Our aim here has also been to make learning dynamics explicit. We wish to point out, however, that the choice of learning strategy is a matter of discretion, since the learning strategy has far-reaching implications for project management. The frequent changes allowed by a flexible learning strategy make the traditional blueprint principle of project management impractical, since project plans cannot cover the IS design process or its main phase in a fixed or prescriptive sense, but instead must be based on a more process-oriented principle, taking place in smaller steps. It is possible, however, to mix these two principles in such a way that the choices differ from one main phase to another.

It is also important to observe that the explicit learning strategy of the PIOCO model is totally compatible with the iterative structure adopted in prototyping. This indicates that the flexible process mode is a practical alternative to the predominantly blueprint mode of traditional life cycle models, even though the difficulty of project management is mentioned as a drawback to prototyping $[2]$ . We have pointed out that the prototype approach includes not only explicit learning dynamics, but also a non-linear structure and applies the principle of alternative design. All three features are characteristic of the PIOCO model for the IS design process, and due to this structural similarity it is very easy to modify it to cover the prototype approach in the sense that we may have prototyping at each level of abstraction (see $[21, 22]$ ). In its simplest form, this includes incorporation of the process B (symbolizing the implementation of prototypes) between the C/O design and testing processes in every main phase corresponding to the level of prototyping. The structural similarity between the basic PIOCO model (without the prototyping option) and the prototype approaches also suggests that prototyping is not a strategic determinant of the IS design process as has been proposed $[4, 24, 43]$ .

## Life cycle dynamics

The life cycle of an information system is conventionally divided into the development phase and the operations and maintenance phase. Even though this life cycle metaphor recognizes the maintenance of the system, it suggests that information systems have some definite life cycle. In reality, many information systems are like institutions—virtually immortal. They change and evolve, but never die.

An increasing proportion of the total budget for information systems development (40–75%), [18] is being devoted to maintenance costs. In practice, a substantial percentage of maintenance (80% according to Ramamoorthy [47]) is of the enhancement type (perfective and adaptive). It is important to recognize that enhancement maintenance is inevitable, since it is caused by the fundamental fact that information systems are functioning in dynamic and changing societal, organizational, and technological environments. This ultimate need for enhancement distinguishes it clearly from repair $[13]$ or corrective $[36]$ maintenance. It is quite likely that in the future a larger and larger percentage of IS development will involve enhancement of existing systems. In the case of an existing information system it is hard to make any clear distinction between initial development and enhancement maintenance, since the existing system is used in the IS design process. Moreover, we do not see any real need for this distinction and, referring to our discussion above, we suggest that the whole distinction between initial development and maintenance (excluding repair maintenance) is harmful $[35]$ .

These considerations have led us to the metaphor of IS evolution $[21, 34, 35, 48]$ , an evolution consisting of successive life cycles. We do not, however, assume information systems to have any definite life cycle, but have extended the concept to distinguish life cycles at the three levels of modelling. At each level the life cycle is the time span between two consecutive “non-repairing” changes in the respective models for the information/data system. The evolution of a system can take place at a different tempo at each level, but is synchronized in the sense that a change at an upper level inevitably imposes changes at the lower levels.

The production of each life cycle requires an IS design and implementation process of its own, the scope of which is different depending on the level. Changes at the P level require all four main phases, those at the I/O level the three main phases from the I/O main phase onwards and those at the C/O level the remaining two main phases starting from the C/O main phase.

Applying this concept, we have incorporated in the PIOCO model the option of an evolutionary IS development. Compared with the experimental or prototype approach, the evolutionary approach is based on feedback from the real operation and use of the information system, while the prototype approach regards this operation and use as no more than experimental.

## Summary

At its macro level the PIOCO model for the IS design process includes the evolutionary nature of information systems (life cycle dynamics), learning in IS design (learning dynamics), the division of the design process into three major design phases (main phase dynamics) and the non-linear structure of the main phases. All these four characteristics of the IS design process reflect close interaction between the IS design group and the steering committee (1) in deciding on the general need for a new life cycle at a specified level of abstraction, (2) in assessing and deciding whether it is informed enough to make the choice concerning the information system at the level of abstraction in question, or whether it wants to have more information or to abort the whole design process, (3) in making the choices concerning the information system, and (4) in expressing specific information requirements (e.g., concerning the expected costs and realizability of the system). Each main phase is considered an inquiry process supporting the characteristic decision-making problems of the main phase in question.

The ideas summarized above suggest certain explanations and reformulations to the problems mentioned in the introductory part of this paper. Cost and schedule overruns may be explained by the inevitable iterations corresponding to the non-linear structure and learning dynamics of the PIOCO model. If these iterations are not made explicit in IS design methodologies, they will not be recognized in project planning or in cost and resource estimates. But more fundamentally there is the question of the operational criteria regarding cost and schedule overruns. The estimates used as operation yardsticks for controlling costs and schedules often reflect the blueprint principle of project management, whereas there are good reasons to insist that IS design, as a process, should be more adaptive [28], reflecting the idea of process-oriented project management. The latter principle does not make the control of costs and schedules impossible, but the estimates to be used as yardsticks should be reformulated to concern only the next “step” in the IS design process instead of whole phases or the whole IS design process. The idea of IS evolution also suggests that the high percentage of “maintenance costs”

should be interpreted with care, since IS evolution is a natural phenomenon which should often be rewarded rather than retarded.

## PIOCO Model for Choice and Quality Criteria

Information systems design always includes explicit or implicit consideration and selection of alternative information systems based on either implicit or explicit criteria. It is also clear that the explication of the principal alternatives is an important precondition for meaningful management involvement as well as for user participation in IS development $[31]$ . In spite of this importance, issues related to information system selection (e.g., the principle of alternative design, the evaluation of information systems, and the choice and quality criteria to be applied in the evaluation), are almost totally neglected in most IS design methodologies.

These issues are integral parts of the PIOCO methodology. The main phase dynamics of the model are defined by means of three choice problems with the following criteria.

1. P main phase: choice of the P model, based on the cost/effectiveness criterion

2. I/O main phase: choice of the I/O model, based on the cost/user satisfaction criterion, with user satisfaction defined over the whole user community

3. C/O main phase: choice of the C/O model, based on the total efficiency criterion.

The three sets of quality criteria identified above—effectiveness, user satisfaction and total efficiency—are briefly introduced.

## Effectiveness criteria

Effectiveness is defined as changes in the relevant environment in the host organization caused by the IS development. This includes both primary effects, which act as motives for the development act, and secondary effects. The relevant environment may include dimensions common to the entire host organizations, or may be specific to a department or office. This, of course, makes it difficult to provide effectiveness criteria (schemas) of wide applicability. Due to the diversity of potential effects, the principle of many points of view should be applied to their identification reflecting the various interests involved and taking into account not only the economic effects (productivity and service level), but also various social (quality of work life), technical, and managerial effects.

The evaluation of effectiveness is without doubt a very difficult task [26], including the typical problems of cost-benefit analysis. On the other hand, it is a highly pragmatic question and we can conclude that every information systems development project entails a cost/benefit evaluation in one form or another. Fortunately, management is used to making this kind of decision since it is “normal management judgement and not very special to IS evaluation” [33].

## User satisfaction criteria

The criteria for user satisfaction, describing how well the information system satisfies the ideal I/O requirements of the user, are depicted in the form of a relevance tree in Figure 3.

The hierarchical structure is entirely based on conceptual analysis aimed at ensuring the theoretical meaningfulness of the concepts. In general terms the resultant structure is highly consistent with the dimensions of the concept of information satisfaction found empirically in Zmud's investigation [57], even though his dimensions are restricted to our concept ‘informativeness’ (corresponding to ‘quality of information’ in Zmud) and to our criterion ‘interpretability’ (‘quality of format’ and ‘quality of meaning’ in Zmud).

In terms of the classification of approaches to the assessment of the value of information given by Ahituv, Munro and Wand [1], user satisfaction clearly represents a subjectivistic approach which has the benefit that it is relatively easy to conduct such assessments. We are not so optimistic, since our main interest is in ex ante evaluation, when the system is in the form of abstract descriptions or a prototype. It should be observed, however, that the essential purpose of the user satisfaction criteria is to express the general idea of goals and values relevant to IS design at the I/O level, rather than to form a quantitative goal function for decision-making purposes. In most cases the choices concerning the I/O models can be made without such quantification.

We have assumed that user satisfaction can be measured on a scale from 0 to 1 (or from 0 to 10) in which 1 indicates a perfect match between the I/O model and the ideal I/O requirements of the user. The measurement of these numerical values can, of course, take place in fuzzy terms, e.g. “perfect”(10), “very good” (9), “quite good” (7), “satisfactory” (5), “poor” (3), “very poor” (1) “useless” (0). It also seems evident that Pearson’s measurement tool based on a semantic differential technique [5, 45] can be applied to the evaluation of the corresponding user satisfaction criteria, even though it reflects a more attitudinal definition of satisfaction.

![](/api/attachments/YA4ARQN7/fulltext/images/c83de6a1ae18478b48c1d201aae1b7dc3db44d2a58c159259d824290a81bb711.jpg)  
Figure 3. User Satisfaction Criteria

## Efficiency criteria

Total efficiency refers to a state in which a given output or task is produced at minimum costs. The efficiency criteria are described in the form of a relevance tree in Figure 4 [19].

Efficiency criteria have many horizontal relations, which are not shown by the relevance tree (e.g. conflict between design, operation and maintenance costs, the conflict between the costs of normal and abnormal operations, etc.). Even if the ultimate criterion is quite clear-cut and tangible, determination of optimal efficiency is still very difficult. This is due to the fact that the effects of the criteria at the bottom of Figure 4 on the corresponding cost components will not be known exactly. Consequently, the choice problem tends to incorporate many efficiency criteria. The structure, however, suggests what efficiency criteria are needed and how efficiency criteria should be weighted in order to approximate total efficiency.

## Summary

Clearly, all IS design methodologies reflect certain value assumptions. The purpose of the model for choice criteria is to explicate the values underlying the PIOCO approach. Due to the order of selection of the information system, the model assumes the highest priority for effectiveness, the next highest priority for user satisfaction, and the lowest for total efficiency. It is significant, however, that the effectiveness criteria may include criteria related to user satisfaction and total efficiency.

The PIOCO model for quality criteria also emphasizes that different criteria are meaningful at different levels of abstraction. This suggests that the value assumptions mentioned above are rooted in the levels of abstraction rather than in the quality criteria, which are only explications of the assumptions. The model also considers the sets of criteria to be complementary rather than alternative or surrogate to each other [26]. The criterion variables form a potential cognitive frame of reference for different participants (stakeholders) in communication and negotiation concerning the values, goals and consequences of the information system during the design process and related decision-making.

![](/api/attachments/YA4ARQN7/fulltext/images/6ed714bb383e9a60a4bdbb9dca8273670b67fd34e21b0fc365b5bd92e5f4d255.jpg)  
Figure 4. Efficiency Criteria

The PIOCO model forms an integrated structure in which the models for the information system, the IS design process, and the choice and quality criteria are closely related. It is conceptually based on the three levels of abstraction for an information system which reflect in a quite natural way the major viewpoints needed in IS design. The form 'viewpoint' refers here to the different interests involved in design and the different expertise required and participants involved in IS design and related decision-making. The levels of abstraction and the specific macrostructures of the I/O and C/O meta-models also form a framework for analyzing and structuring the theoretical and methodological background (methodologies, methods, techniques and tools) of IS design. We have found this structuring extremely helpful in education, but we also feel that this simple framework may be useful for management as a kind of overview of the methodology of IS design.

## Acknowledgements

We are grateful to Professors Pentti Kerola and Pertti Järvinen, whose PSC model provided the impetus for the development of the PIOCO model, and also to the anonymous referees and Ms. Leslie Maggi for their patience and constructive comments.

## References

1. Ahituv, N., Munro, M.C. and Wand, Y. "The Value of Information in Information Analysis," Information & Management, Volume 4, Number 3, March 1981, pp. 143–150.

2. Alavi, M. "An Assessment of the Prototyping Approach to Information Systems Development," Communications of the ACM, Volume 27, Number 6, June 1984, pp. 556–563.

3. Argyris, C. Intervention Theory and Method, A Behavioral Science View, Addison-Wesley, Reading, Massachusetts, 1973.

4. Bally, L., Brittain, J. and Wagner, K.H. "A Prototype Approach to Information System Design and Development," Information & Management, Volume 1, Number 1, November 1977, pp. 21–26.

5. Bailey, J.L. and Pearson, S.W. "Development of a Tool for Measuring and Analyzing Computer User Satisfaction," Management Science, Volume 29, Number 5, May 1983, pp. 530–545.

6. Bell, T., Bixter, D. and Dyer, M. "An Extendable Approach to Computer-Aided Software Engineering," IEEE Transactions on Software Engineering, Volume 5E-3, Number 7, January 1977, pp. 6–15.

7. Boehm, B.W. Software Engineering Economics, Prentice-Hall, Englewood Cliffs, New Jersey, 1981.

8. Bostrom, R.P. and Heinen, J.S. "MIS Problems and Failures: A Socio-Technical Perspective, Part I: The Causes," MIS Quarterly, Volume 1, Number 3, September 1977, pp. 17–32.

9. Bubenko, J.Jr. "Information Modeling in the Context of System Development," in Information Processing 80, S. Lavington (ed.), North-Holland, Amsterdam, Holland, 1980.

10. Chen, P.P. "The Entity-Relationship Model—Toward a Unified View of Data," ACM Transactions on Database Systems, Volume 1, Number 1, 1976, pp. 9–36.

11. Codd, E.F. "A Relational Model of Data for Large Shared Data Banks," Communications of the ACM, Volume 13, Number 6, June 1970, pp. 377–387.

12. Codd, E.F. "Extending the Database Relational Model to Capture More Meaning," ACM Transactions on Database Systems, Volume 4, Number 4, December 1979, pp. 397–434.

13. Davis, G.B. and Olson, M.H. Management Information Systems, McGraw-Hill, Inc., New York, New York, 1984.

14. Date, C.J. An Introduction to Databases. Volume 2. Addison-Wesley, Reading, Massachusetts, 1983.

15. DeMarco T. Structured Analysis and Systems Specification, Prentice-Hall, Inc., Englewood Cliffs, New Jersey, 1979.

16. Faludi, A. Planning Theory. Pergamon Press, Oxford, England, 1973.

17. Freeman, P. and von Staa, A. "Towards a

Theory of Software Engineering," unpublished manuscript, University of California-Irvine, October 1984.

18. Guimaraes, T. "Managing Application Program Maintenance Expenditures," Communications of the ACM, Volume 16, Number 10, October 1983, pp. 739–746.

19. livari, J. and Koskela, E. "Choice and Quality Criteria for Data System Selection," In EuroIFIP 79, P.A. Samet (ed.), North-Holland, Amsterdam, Holland, 1979, pp. 143–150.

20. livari, J. and Koskela, E. "An Extended EAR Approach for Information System Specification," in Entity-relationship Approach to Software Engineering. C. G. Davis, S. Jajodia, P.A. Ng, R.T. Yeh (eds.), North-Holland, Amsterdam, Holland, 1983, pp. 605–636.

21. livari, J. "Taxonomy of the Experimental and Evolutionary Approaches to System-eering," in Evolutionary Information Systems. J. Hawgood (ed.), North-Holland, Amsterdam, Holland, 1982, pp. 101–119.

22. Iivari, J. "Contributions to the Theoretical Foundations of Systemeering Research and the PIOCO Model," Acta Universitatis Ouluensis, A150, Oulu, Finland, 1983.

23. Iivari, J. "A Sociocybernetic Metamodel for Systemeering as a Framework for the Contingency Research into Information Systems Development," in Beyond Productivity: Information Systems Development for Organizational Effectiveness, Th.M.A. Bemelmans (ed.), North-Holland, Amsterdam, Holland, 1983, pp. 49–78.

24. livari, J. "Prototyping in the Context of Information Systems Design." In Approaches to Prototyping: Proceedings of the Working Conference on Prototyping, R. Budde, K. Kuhlenkamp, L. Mathiassen, H. Züllighoven (eds.), Springer-Verlag, Berlin, Germany, 1984, pp. 261–277.

25. Iivari, J. "Dimensions of Information Systems Design: A Framework for a Long-Range Research Program," Information Systems, Volume 11, Number 2, June 1986, pp. 185–197.

26. Ives, B., Olson, M.H., Baroudi, I.J. "The Measurement of User Information Satisfaction." Communications of the ACM, Volume 26, Number 10, October 1983, pp. 785–793.

27. Jackson, M. Principles of Program Design, Academic Press, London, England 1975.

28. Keen, P.G.W. "Adaptive Design for Decision Support Systems," Data Base, Volume 12, Number 1/2, Fall & Winter 1980, pp. 15–25.

29. Kerola, P. and Järvinen, P. Systemointi II. Oy Gaudeamus Ab, Helsinki, Finland 1975.

30. Kerola, P. "On Hierarchical Information and Data Systems in Data System Life Cycle." In Systemeering 75, M. Lundeberg and J. Jr. Bubenko (eds.), Student-litteratur, Lund, Sweden, 1975.

31. King, W.R. "Alternative Designs in Information System Development," MIS Quarterly, Special Issue, December 1982, pp. 31–42.

32. Langefors, B. Theoretical Analysis of Information Systems. Studentlitteratur, Lund, Sweden 1966.

33. Langefors, B. "Information Systems," Information Processing 74, North-Holland, Amsterdam, Holland, 1974, pp. 937–945.

34. Lehman, M.M. "Programs, Programming and the Software Life Cycle," Report No 8016, Imperial College of Science and Technology, London, England, 1980.

35. Lehman, M.M. "Program Evolution," Information Processing Management, Volume 20, Numbers 1–2, January 1984, pp. 19–36.

36. Lientz, B.P., Swanson, E.B. and Tompkins, G.E. "Characteristics of Application Software Maintenance," Communications of the ACM, Volume 21, Number 6, June 1978, pp. 466–471.

37. Lundeberg, M., Goldkuhl, G. and Nilsson, A. Information Systems Development: A Systematic Approach. Prentice-Hall, Englewood Cliffs, New Jersey, 1981.

38. Martin, J. Security, Accuracy and Privacy in Computer Systems, Prentice-Hall, Englewood Cliffs, New Jersey, 1973.

39. Marschak, J. Economic Information, Decision and Prediction, Selected Essays, Volume II, Dordrecht, D. Reidel, Boston, Massachusetts, 1974.

40. Markus, M.L. "Power, Politics and MIS Implementation," Communications of the ACM, Volume 26, Number 6, June 1983, pp. 431–444.

41. Mumford, E. Designing Human Systems

For New Technology. The ETHICS Method, Manchester Business School, Manchester, England, 1983.

42. Mustonen, S. Tavoitteisen Järjestelmän Kyberneettinen Analyysi Päätäntäteorioiden ja Systemoinnin Metatutkimuksessa. Report A7, Institute of Data Processing Science, University of Oulu, Oulu, Finland, 1978.

43. Naumann, J.D. and Jenkins, A.M. "Prototyping: The New Paradigm for Systems Development," M/S Quarterly, Volume 6, Number 3, September 1982, pp. 29–44.

44. Orr, K. Structured Systems Development, Yourdon Press, New York, New York, 1977.

45. Pearson, S.W. Measurement of Computer User Satisfaction, Ph.D. Dissertation, Arizona State University, Tempe, Arizona, 1977.

46. Ross, D. "Structured Analysis (SA): A Language for Communicating Ideas," IEEE Transactions of Software Engineering, Volume SE-3, Number 1, January 1977, pp. 16–34.

47. Ramamoorthy, C.V., Prakash, A., Tsai, W., and Usuda, Y. "Software Engineering Problems and Perspectives," Computer, Volume 17, Number 10, October 1984, pp. 191–207.

48. Rzevski, G. "Some Philosophical Aspects of System Design," in Cybernetics and Systems Research, R. Trappl (ed.), North-Holland, Amsterdam, Holland, 1982.

49. Sundgren, B. An Infological Approach to Data Bases. Skrifts Number 7, Statistiska Centralbyra $^{e}$ n, Stockholm, 1973.

50. Swartout, W. and Balzer, R. "On the Inevitable Intertwining of Specification and Implementation," Communications of ACM, Volume 25, Number 7, July 1982, pp. 438–440.

51. Tausworthe, R.C. Standardized Development of Computer Software, Part 1: Methods. Prentice-Hall, Englewood Cliffs, New Jersey, 1977.

52. Verheijen, G.M.A. and Van Bekkum, J. "NIAM: An Information Analysis Method," in Information Systems Design Methodologies: A Comparative Review, T.W. Olle, H.G. Sol, and A.A. Verrijn-Sturat (eds.), North-Holland, Amsterdam, Holland, 1982, pp. 537–587.

53. Vick, C.R. "A Software Engineering Environment," in Handbook of Software En-

gineering. C.R. Vick and C.V. Ramamoorthy (eds.), Van Nostrand Reinhold, New York, New York, 1984, pp. xi-xxxii.

54. Warnier, J-D. Logical Construction of Programs. H.E. Stenfert Krose, Leiden, Holland, 1974.

55. Wasserman, A.I. "USE: A Methodology for the Design and Development of Interactive Information Systems," in Formal Models and Practical Tools for Information Systems Design, H-J Schneider (ed.), North-Holland, Amsterdam, Holland, 1979.

56. Welke, R.J. "Current Information System Analysis and Design Approaches: Framework, Overview, Comments and Conclusions for Large-Complex Information System Education," in Education and Large Information Systems, R.A. Buckingham (ed.), North-Holland, Amsterdam, Holland, 1977, pp. 149–166.

57. Zmud, R.W. "An Empirical Investigation of the Dimensionality of the Concept of Information," Decision Science, Volume 9, Number 2, April 1978, pp. 187–195.

## About the Authors

Juhani livari is an Associate Professor of Information Processing Science at the University of Oulu, where he received his M.S. and Ph.D. degrees. He has published several articles in the IS field. His research interests include the comparative analysis of IS design methodologies, the organizational aspects of IS design and implementation, the specification of information systems and IS assessment. He is a member of IFIP (the International Federation of Information Processing) TC8 (Technical Committee of Information Systems) Working Group WG8.2 on “The Interaction of the Information Systems and the Organization.”

Erkki Koskela is an Assistant Professor of Information Processing Science at the University of Oulu, where he received his M.S. and Phil.Lic. degrees. For the present he is acting as a Professor of Software Engineering. His research interests include the comparative analysis of IS and software design methodologies, the specification of management information systems and embedded systems, and the IS and software development tools and environments.
