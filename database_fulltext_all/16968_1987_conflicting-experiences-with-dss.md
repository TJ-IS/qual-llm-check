---
otero_id: 16968
otero_key: "Z2DB4JWQ"
title: "Conflicting experiences with DSS"
authors: "Henk G. Sol"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90175-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Conflicting Experiences with DSS

Henk G. SOL

Delft University of Technology, 2628 BL Delft, The Netherlands

The concept of DSS is clearly attracting a lot of interest. Although this should be welcomed, it does not signify that the concept is well-defined and well-established. Above, we may observe that empirical evidence on the effectiveness of DSS is not overwhelmingly positive, and is often conflicting. Many DSS focus on problem-solving, not on problem-identification. Many DSS are constructed around aggregated data, separated from primary, transaction processing data. However, it is shown in several studies that use of this type of data may be dangerous for decision-making. With regard to the model component of many DSS: Most models encountered in DSS are of the 'equation' type. These models are only applicable under the assumption that the equations can be filled in and that they give a valid description of reality. This assumption seems to hold only in a very few cases. A way out can be found in the application of models of the discrete event or 'process' type. A frequently encountered approach for the development of DSS is an evolutionary, step-wise one. However, such an approach is not necessarily converging. Especially personalized DSS demand a strong project management to avoid a chaos of hardware, software, personal files and models. Decentralization of decision-making and computing does not guarantee a better co-ordination of the workstations of individual information workers. We propose to use the concept DSS in a more narrow sense of an environment to support decision making, encompassing a language system, a knowledge system and a problem processing system. The language system is based on an object-oriented representation form. The problem processing system and the knowledge system bear heavily on the process type system specification.

![](/api/attachments/Z2DB4JWQ/fulltext/images/015a415e3f3aec8a33c0428504b88b616475d4ea14e5a4a33ba56c611e544548.jpg)

Henk G. Sol is professor of information systems at Delft University of Technology, The Netherlands, Information Systems Group. From a background in operations research, he moved to the discipline of information systems design and management.

His Ph.D. Dissertation 'Simulation in Informations Systems Design' tries to bridge the gap between information technology and organizational sciences. His current teaching activities, research project and consulting address information system planning, design methodologies, MIS, DSS, prototyping and simulation. Sol is author or editor of well over a hundred publications in this field.

## 1. Introduction

Numerous researchers and practitioners have no hesitations in putting the label Decision Support Systems (DSS) to their work. It is remarkable that the term DSS is much without a very strict definition of its content. Many writers seem to approach DSS as a philosophy to seek a useful complementarity between technological tools and human judgement and discretion. Klein and Hirschheim (1985) point out that ‘there appears to be an implicit assumption on the part of DSS writers that DSS are beneficial to organizations and the DSS intervention process is not inherently polemic’.

Ginzberg and Stohr (1982) remark that ‘the basis for defining DSS has been migrating from an explicit statement of what a DSS does to some ideas about how the DSS objective can be accomplished (i.e., what components are required?, what usage pattern is appropriate?, what development process is necessary?)’.

This migration during the years can be shown in the following descriptions of DSS:

(1) In the early 1970's DSS was described as 'a computer-based system to aid in decision-making'. The starting point was found in the application of interactive technology to managerial tasks in order to use computers for better decision-making. There was a strong cognitive focus in this DSS-concept, viz. that of a single decision-maker.

(2) In the mid to late 1970's the DSS-movement emphasized ‘interactive computer-based systems which help decision-makers utilize data bases and models to solve ill-structured problems’. The emphasis lies not so much on the decision process, but rather on the support for personal computing with tools for fast applications development and packages for financial planning.

(3) In the later 1970's to early 1980's the DSS bandwagon provides systems 'using suitable and available technology to improve effectiveness of managerial and professional activities'. User-friendly software is produced almost unexceptionally under the label DSS. Disciplines like operations research and psychology are jumping on the bandwagon. Concepts like information center and prototyping are put forward in the same utterance as DSS.

(4) By now we face a new technical base for DSS: the convergence on intelligent workstations. Telecommunication technology puts forward the issues of organizational versus personal computing and distributed DSS. We see new technologies emerging as expert systems and document-based systems. This is expressed by Elam et al. (1985) in the need for a new vision on DSS. They propose to confine the notion DSS to ‘the exploitation of intellectual and computer-related technologies to improve creativity in decisions that really matter’.

We do not want to enter a new debate on definitions of DSS. Rather, we like to explore what new insights we gained from applying the DSS concept to improve organizational efficiency and effectiveness.

In general, for a comparison of research contributions dealing with organizational decision making, one might wonder

\- what problems are addressed,

\- what paradigm or ‘Weltanschauung’ governs the process of problem conceptualization and problem specification,

\- what construct-paradigm or model cycle is followed, expressing in broad terms the order of activities,

\- what methodology, as an actual sequence of activities in view of a problem situation, is used, telling what to do in which activity,

\- what project control is performed, during the activities,

-- what theory is followed, contributing to the actualization of the model cycle and the methodology in terms of how the activity is to be performed, and especially, how alternative solutions are to be generated.

## 2. Paradoxical Observations on DSS

A useful framework for research on DSS is introduced in Sprague (1980). He discusses the perspective of the end-user, the builder and the toolsmith from which a DSS can be viewed. In accordance with this distinction the concept of a DSS can be viewed. In accordance with this distinction the concept of a DSS-generator is put forward to bridge the gap between general tools and specific DSS. Sprague distinguishes as the main components of a DSS a data base, a model base, and an intermediate software system which interfaces the DSS with the user.

Within the data base for decision support one can distinguish between external data from public data sources, administrative data produced by the transaction processing system, and internal data created by personal computing. The models in the model base as envisaged by Sprague are mostly of the 'equation' type: great number of so called corporate models or financial models consists of definition equations and behavioural equations. Econometric models also consist of equation models. Another category is formed by optimization models based on linear, dynamic or stochastic programming.

A first generation of so-called DSS-generators focusses on equation models with data base and interactive facilities like data-, model- and text manipulation, cf. Klein and Manteau (1983) and Bergquist and McLean (1983). By now, the integrated facilities are not only offered on mainframes, but also on micro-computers together with facilities for 'down-loading from and uploading to central computer systems through data-communication'.

A more conceptual framework is put forward by Bonczek et al. (1981). They replace the components mentioned by the concepts of a language system, a knowledge system and a problem processing system. The language system is the sum of all linguistic facilities made available to the decision-maker by a DSS. A knowledge system is a DSS's body of knowledge about a problem domain. The problem processing system is the mediating mechanism between expressions of knowledge in the knowledge system and expressions of problems in the language system.

The framework put forward by Bonczek et al. makes it easy to relate the work in the field of artificial intelligence to DSS. We define an expert system as ‘a computer system containing organised knowledge, both factual and heuristic, that contains some specific area of human expertise, and that is able to produce inferences for the user’, see

Chang, Melamud and Seabrook (1983).

When one looks upon an inference system as a special kind of problem processing system and upon the knowledge base as a special kind of knowledge system, then these expert systems fit neatly into the framework. Along this line, a school of researchers focusses on the representation of knowledge for decision support, cf. Fox (1984), Bonczek et al. (1983). The relevance of epistemology to improve decision-making processes is addressed by, e.g., Lee (1983). Stamper (1984).

The process of designing DSS is as yet not much addressed. Sprague and Carlson (1982) advocate an approach ‘to systems analysis which is intended to identify requirements in each of the three major capability areas of DSS. The approach is based on a set of four user-oriented entities: Representations, Operations, Memory Aids and Control Mechanisms’. Humphreys et al. (1983) report empirical research on rounds and stages in the development paths and the roles played by various participants, as analyzed in several projects. Empirical research as presented, e.g., in Fick and Sprague (1980), Ginzberg et al. (1982), Bennett (1983), Sol (1983), shows the variety of approaches undertaken by various researchers and practitioners to create systems for effective decision support.

It may be dangerous to draw conclusions from the available expertise on DSS. However, following the framework for evaluation outlined above it is possible to present some conclusions in the form of several paradoxes.

## (1) Problems addressed

DSS are directed at ill-structured problem situations. It is striking, however, how little attention is paid to the process of problem solving. There are various frames to describe these processes. If one takes, for instance, the phases of intelligence – design – choice – implementation, then one might observe that a great number of DSS address the phases of choice and implementation. Recently there is argumentation to focus on intelligence and choice, see, e.g., Landry et al. (1985), Sol (1982).

Before one can start looking for a problem solution or designing a DSS or, more generally, an information system, one has to understand the problem situation or the actual object system. Of course, design of an application or choice of a solution has to be done within constraints of time and resources. But, ‘thinking before doing’ is also applicable to DSS-design. Therefore, more emphasis should be placed on the activities of problem identification and specification.

## (2) Weltanschauung

We may conclude that a great many of the contributions start from the premise that decision support can be achieved through aggregation of data. Keen (1980) presents a summary of major case studies, all using data on an aggregated level. The same applies to the case studies presented in Alter (1980), Sol (1983), McLean and Sol (1986).

A great many approaches are starting from the premise that more and better information will also lead to better decisions. Dickson (1983) identifies as required facilities for management support: writing, communicating, individual processing, managing data, problem finding, making decisions and conveying decisions. As Sprague and Carlson (1982) put it: 'Databases and DBMS are an important prerequisite to a DSS because building a DSS without existing data bases and associated DBMS will be extremely difficult'.

In several organizations using DSS one may observe a logical or even physical distinction between

\- a data base with detailed figures on primary processes,

\- a decision support data base with individual data, external data and aggregated administrative and transactional data.

One can give several, mainly technical, arguments for this distinction:

\- The efficiency of existing data base management systems and especially of relational ones, still is a technical problem, if one tries to develop one physical data base.

\- Personal computing demands a hardware- and software environment different from the one for transaction processing.

\- Data in the decision support data base may be not as accurate as the transactional data.

The decision support data base mostly contains data aggregated from the basic figures, e.g., on time or on product characteristics. However, it is shown in several studies that use of this type of data may be dangerous for decision making: One may question the validity of management information produced through aggregation, see Reuijl (1982), Sol (1982), Sol (1985). It is difficult to give the appropriate degree of aggregation for various decisions. Aggregated data do not always support equations that give a valid description of reality. Many decision support system-generators are based on the use of aggregated data, which is in contradiction with the empirical findings.

## (3) Model cycle

The model cycle behind a great many contributions in the DSS-field may be characterized as one, trying to integrate scientific, ethical and esthetic modes of thought in a synthetic, interdisciplinary way. The availability of data and appropriateness of decision-making in organizations is not much questioned.

Or, to put it in another way, the modelling paradigm is mostly the one of thinking in terms of relationships between variables.

Most models encountered in DSS are of the 'equation' type: a set of definition and behavioural equations, possibly together with a goal function. Once the behavioural equations are estimated and empirically validated, one starts playing with the model, e.g., in an optimization mode, or in a 'what-if' or 'goal-seeking' mode.

However, these models are only applicable under the assumption that the equations can be filled in and that they give a valid description of reality. This assumption that one can describe reality based on an input-output specification of a black-box, seems to hold only in a very few decision-making situations. A way-out can be found in the application of models of the 'process' type, as presented in the next paragraph.

## (4) Methodology

As to a methodology for developing DSS, it is difficult to identify a generic framework.

Keen (1980) applies the term DSS to situations where a final system can be developed only through an adaptive process of learning and evolution. Henderson and Ingraham (1982) remark that ‘prototyping or adaptive design has been suggested as an effective approach for developing and implementing DSS. Empirical research has shown this design strategy is effective in establishing meaningful user involvement and high user satisfaction. A comparison with the information requirements generated by a structured group process indicates that prototyping is a convergent design method that may overlook important user information needs'. It is clear that an evolutionary or iterative approach is prevailing in many cases of DSS development, see, e.g., Davis et al. (1980) and Sol (1982). However, such a prototyping or incremental approach is not necessarily converging and is no guarantee for an effective DSS. Our experiences with prototyping in a number of practical studies lead to the conclusion, see Sol (1984b), that

\- prototyping may overemphasize the activity of solution finding by jumping to a dynamic model of the target system. The activity of understanding a problem situation may get too little attention.

\- not every organization can bear the 'throw away' aspects of prototyping. In a bureaucratic organization and even in a traditional data processing department it may be difficult to set aside a prototype in which money and manpower is invested.

\- a prototype is easily taken away as a pilot system or as a final production system, before one has properly experimented with the prototype.

\- developing prototypes for various sub-systems in an information system may lead to isolated thinking or a 'tunnel vision', neglecting the overview of the total system. This danger can be reduced if one starts prototyping from a good information systems plan for an organization.

## (5) Project control

DSS is closely related to phrases as end-user computing and personal computing. A lot of development effort and tools are directed at the support of individual decision-making. An uncontrolled stimulation of this path may lead to a chaos of hardware and software, of personal files and of models. This asks for a strong management of personal computing resources and facilities.

## (6) Design theory

As to possible theories for developing DSS we observe that co-ordination of decision-making processes is still a neglected topic. Many DSS and DSS-environments tacitly take the assumption that loosely coupled systems, be it individual decision-makers, groups, departments or DSS-environments, are an appropriate answer to the coordination problem in organizations. However, this is not obvious at all, cf. Bosman (1983). This starting point is still much used.

## 3. Rethinking the Concept

The observations above make it clear that the bandwagon of DSS does not necessarily follow a right track.

Although the interest for DSS should be welcomed, a clearer delineation of the concept of DSS is needed in order to make it a potentially rich track.

Rich, in the sense that it can foster the effectiveness and efficiency of organizational decision-making. Keen has questioned the role of modelling and quantitative models in stimulating creative thinking. If the OR-discipline is taking up the DSS-line, it should pick up this challenge and focus on creative decision-making and learning on the merge of MIS and OR/Management Science.

![](/api/attachments/Z2DB4JWQ/fulltext/images/5095abf2f68194b995996c3c6f49ee72bdfd342f4de0b06019bfb3e3c3678976.jpg)  
Fig. 1.

Some researchers try to design DSS according to principles from cognitive psychology. Cats-Baril and Huber (1984) point out that the generalizability of these principles is still low. They also mention a critical factor in decision support, viz. the presence of problem-solving heuristics.

Another consideration deals with the relevance of AI-research to DSS. Stamper (1984) remarks: 'Our growing technical capacity to produce, store and distribute information is no guarantee of the information's organizational and social usefulness. The trend towards intelligent, knowledge based systems cannot solve the problem; instead it could well make the problem worse by disguising poor information under a cloak of logical self-consistency'.

Although DSS may provide a link on the path from traditional information processing towards knowledge engineering, we may recall that expert systems are always based on historical expertise. The search for expertise should not detract attention from grasping creativity-process in new, unexperienced problem situations.

However, I would prefer to take up the process of problem solving in a knowledge-based framework, which may give a solution to the paradoxes formulated.

Therefore, I extended in Sol (1983) the frameworks presented by Sprague and Bonczek into a new one, see fig. 1.

I propose to direct DSS-research to the concept of DSS-generators or, more generally, DSS-design environments. One of the main reasons for this choice is the lack of generalizability in dealing with specific decision support systems. Another reason is that one has to address all stages in the process of problem-solving, not only at the empirical, problem-dependent level, but also at the conceptual level.

Especially for the solution of ill-structured problems, the choice of a Weltanschauung and a construct-paradigm or model cycle, as point of departure for activities of problem conceptualization and problem specification, are closely related. The expression of a methodology and a theory, in view of a problem under consideration, follows these choices closely. I put forward the idea that it is possible to combine a Weltanschauung with a construct-paradigm by giving the concepts of a DSS-generator, a language system, a knowledge system and a problem processing system a concrete content in the notion of an INQUIRY SYSTEM. I define an inquiry system as a structured set of instruments which can be used as a context or modelling environment in the problem-solving activities. It expresses a methodology in view of a problem area.

The inquiry system serves in the first instance as a ‘context for conceptualization’. It presents in its language system and knowledge-base the building blocks for the creation of a system description. Subsequently, the inquiry system appears as a conceptual model for the problem specification, in an empirical model for the solution finding and in a target system for the implementation.

The notion of an inquiry system has several important contributions.

(1) By translation of a Weltanschauung and a construct-paradigm into a context for conceptualization one can discuss the premises behind theory formulation. Through its application in the construction of a conceptual model and a model system, a theory comes about.

(2) The products of the various activities in the process of problem-solving are building on each other as successive layers. This allows for an easy adjustment of individual theories and organisational theories and for an evolutionary development of a target system.

(3) The modelling environments in the inquiry system enable a flexible support of all phases in the process of problem solving. Problem finding can get at least as much attention as solution finding.

For the construction of conceptual models and empirical models one needs a language system which does not restrict the capabilities of inquirers and decision-makers in using knowledge to make models and to create evidence. I make a distinction between on the one hand a description form using equations and on the other hand process or rule-based models.

The EQUATION MODELS are frequently encountered in DSS for strategic and organizational problems, especially in corporate or financial models. In these models one has to define functional relationships in terms of definition equations or behavioural equations. Although these may be specified in a non-procedural way as in several DSS-generators, they still apply to the outside of a phenomenon, seen as a black-box.

In the PROCESS OR RULE-BASED MODELS one does not try to summarize a process in equation form. Instead, one tries to describe the sequence of events in a system. I introduce the notion of an ENTITY as an identifiable set of associated ATTRIBUTES. An entity may portray behaviour by applying one or more transformation rules to change the values of some of its attributes and by interactions with other entities. I define in a SCENARIO related to an entity the possible transformation rules and the possible interaction paths of an entity, as well as the conditions under which these can be actualized. This can be done in various modes. One mode is the 'declarative' mode, as, e.g., encountered in interpreted predicate logic, see Bubenko (1982), Sernadas (1982). Another mode is the 'procedural' mode, as we know this style from a great many procedural programming languages. It is sometimes suggested that these modes are their antagonists. I prefer to see them as complementary. Depending on the application domain and the users involved, one might prefer one of the modes.

In combining within an entity a data part and an action part, I come close to the concept of object-representation in object-oriented languages, see, e.g., Cox (1984).

The notions of an entity and a scenario enable us to ‘open the black-box’ of an individual decision maker and specify the concepts and rules applied. We are able to specify their own language system, knowledge system and problem processing system. As to the construction of a conceptual model of an individual decision-maker, we have to describe how scenario’s of entities with their attributes are actualized. We may specify various psychological types of a decision-maker in a multidisciplinary way by introducing entities with corresponding attributes and scenario’s for processing data and making decisions. In a scenario for an individual we may even describe the changes in the data input mode and decision-making during the process of problem solving. We observe that scenario’s for portraying behaviour may bring about transformation rules not previously thought of, as well as attributes and interaction paths involved. We may have to describe that a decision-maker has a local scope: As an entity he only deals with a specific set of attributes and specific access-paths to other entities. He only observes a ‘representative state’ of an entity, i.e., those attributes and that part of the scenario which gave meaning to him. However, this representativeness may change dynamically during the problem-solving process.

To summarize, through process-specifications of objects we can look into the dynamics of decision-making processes and the resulting behaviour. In this way we may create evidence on problem-solving processes in specific situations using strategic and actual knowledge in the process-specifications.

The inquiry system mentioned supports the process of problem-solving, firstly by creating an epistemological specification of processes in an empirical situation. This specification is based on a conceptual model formulated against the background of knowledge of an application domain. Subsequently, the inquiry system facilitates the generation of alternatives and the choice of a solution. By keeping track of the subsequent steps in the process of problem solving we may acquire knowledge, not only on the actual problem situations, but also perhaps for future situations. The inquiry system can be seen as a problem-solving environment. When it is supported on a computer, we are dealing with a DSS-environment.

How can we apply these environments to create supporting inquiry systems for individual decision-makers? The construction of the descriptive understanding model and the prescriptive target solutions can be facilitated by a design environment in which various expert systems and knowledge bases have their place. The process of producing the epistemological representation can be facilitated by an expert system with a knowledge base characteristic for the application domain.

Further expert systems with a different knowledge base, to support the process of problem-solving are dedicated at

\- verification and validation of the descriptive model,

\- screening and evaluating this model and setting up an experimental design,

\- creating suggestions for alternative target specifications.

The approach in applying these knowledge bases is then:

\- choose appropriate building blocks for a system description of the existing situation,

\- identify decision entities and describe rules in the existing situation,

\- develop a simulation model and analyze the problem,

\- develop prototype alternatives and experiment,

\- transform the target prototype to a concrete DSS/IS.

Pilot applications of this approach are reported in Sol (1984a, 1984b).

## References

Alter, S.L., Decision Support Systems: Current practices and continuing challenges (Addison-Wesley, Reading, 1980).

Bennet, J.L. (ed.), Building Decision Support Systems (Addison-Wesley, 1983).

Bergquist, J.W., E.R. McLean, Integrated Data Analysis and Management Systems: An APL-Based Decision Support System, in: H.G. Sol (ed.), Processes and Tools for Decision Support (North-Holland, Amsterdam, 1983).

Bonczek, R.H., C.W. Holsapple, A.B. Whinston, Foundations of Decision Support Systems (Academic Press, 1981).

Bonczek, R.H., C.W. Holsapple, A.B. Whinston, Specification of Modeling and Knowledge in Decision Support Systems, in: H.G. Sol (ed.), Processes and Tools for Decision Support (North-Holland, Amsterdam, 1983).

Bosman, A., Decision Support Systems: Problem Processing and Co-ordination, in: H.G. sol (ed.), Processes and Tools for Decision Support (North-Holland, Amsterdam, 1983).

Bubenko, J.A. et al., CIAM, in: T.W. Olle, H.G. Sol, A.A. Verrijn Stuart (eds.), Information Systems Design Methodologies: A Comparative Review (North-Holland, Amsterdam, 1982).

Burch, J.C. and F.R. Strater, Information Systems: Theory and Practice (Hamilton Publishing Company, Santa Barbara, 1974).

Cats-Baril, W.L., G.P. Huber, DSS for Ill-Structured Problems: A Cognitive Approach and an Empirical Study, Proceedings of the IFIP 8.3 Working Conference on Knowledge Representation for Decision Support Systems (Durham, 1984).

Chang, C., Y. Melamud and D. Seabrook, Expert Systems, The Butler Cox Foundation, Report Series 37 (1983).

Cox, C., Message/Object Programming: An Evolutionary Change in Programming Technology, IEEE Software, Jan. (1984).

Davis, G.B. et al., A Contingency Method for Selection of a Requirements Assurance Strategy, The Journal of Systems and Software 1 (1980).

Dickson, G., Requisite Functions for a Management Support Facility, in: H.G. Sol (ed.), Processes and Tools for Decision Support (North-Holland, Amsterdam, 1983).

Elam, J. et al., A. Vision for DSS, Proceedings DSS-85 (1985).

Fick, G., K.H. Sprague (eds.), Decision Support Systems: Issues and Challenges (Pergamon Press, Oxford, 1980).

Fox, M.S., Knowledge Representation for Decision Support, Proceedings of the IFIP 8.3 Working Conference on Knowledge Representation for Decision Support Systems (Durham, 1984).

Ginzberg, M.J. and E.A. Stohr, Decision Support Systems: Issues and Perspectives, in: M.J. Ginzberg, W. Reitman, E.A. Stohr (eds.), Decision Support Systems (North-Holland, Amsterdam, 1982).

Henderson, J.C., R.S. Ingraham, Prototyping for DSS: A Critical Appraisal, in: M.J. Ginzberg, W. Reitman, E.A. Stohr (eds.), Decision Support Systems (North-Holland, Amsterdam, 1982).

Humphreys, P., O.I. Lariche, A. Vari, J. Vecseny, Comparative Analysis of Use of Decision Support Systems in R & V Decisions, in: H.G. Sol (eds.), Processes and Tools for Decision Support (North-Holland, Amsterdam, 1983).

Keen, P.G.W., Adaptive Design for Decision Support Systems, Data Base 12, No. 1 and 2 (1980).

Klein, H.K., R. Hirschheim, Consequentialist Perspective of Decision Support systems, Decision Support Systems 1, no. 1 (1985).

Klein, M., A. Manteau, Optrans: A Tool for Implementation of Decision Support Centers: in: H.G. Sol, (ed.), Processes and Tools for Decision Support Centers: in: H.G. Sol, (ed.), Processes and Tools for Decision Support (North-Holland, Amsterdam, 1983).

Landry, M., D. Pascot, D. Briolat, Can DSS Evolve Without Changing Our View of the Concept of 'Problem'? , Decision Support Systems 1, nr. 1 (1985).

Lee, R.M., Epistemological Aspects of Knowledge-Based Decision Support Systems, in: H.G. Sol (ed.), Processes and Tools for Decision Support (North-Holland, Amsterdam, 1983).

McLean, E.R., H.G. Sol, DSS: A Decade in Perspective (North-Holland, Amsterdam, 1986).

Naylor, Th.H., Decisions Support Systems or What Happened to MIS?, Interfaces 12, nr. 4 (1982).

Olle, T.W., H.G. Sol, C.J. Tully (eds.), Information Systems Design Methodologies; A Feature Analysis (North-Holland, Amsterdam, 1983).

Olle, T.W., H.G. Sol, A.A. Verrijn Stuart (eds.), Information Systems Design Methodologies: A Comparative Review (North-Holland, Amsterdam, 1982).

Reuijl, J.C., On the Determination of Advertising Effectiveness, An Empirical Study of the German Cigarette Market (Stenfert Kroese, Leiden, 1982).

Sernadas, A., Software Behaviour Specification with Triggering Logic, Infolog Research Report RR02 (Lisbon, 1982).

Simon, H.A., the New Science of Management Decision (Harper and Brothers, New York, 1960).

Sol, H.G., Simulation in Information Systems Development, Ph.D. Thesis University of Groningen (1982).

Sol, H.G., Processes and Tools for Decision Support: Inferences for Future Developments (North-Holland, Amsterdam, 1983).

Sol, H.G., The Emerging Role of Simulation Based Inquiry Systems, in: Th.M.A. Bemelmans (ed.), Beyond Productivity, Information Systems Development for Organizational Effectiveness (North-Holland, Amsterdam, 1984a).

Sol, H.G., Prototyping: A Methodological Assessment, in: R. Budde et al. (eds.), Approaches to Prototyping (Springer, Berlin, 1984b).

Sol, H.G., Aggregating Data for Decision Support, Decision Support Systems 1 no. 2 (1985).

Sprague, R.H., A Framework for Research on Decision Sup-

port Systems, in: G. Fick, R.H. Sprague (eds.), Decision Support Systems: Issues and Challenges (Pergamon Press, Oxford, 1980).

Sprague, R.H., E.D. Carlson, Building Effective Decision Support Systems (Prentice Hall, Englewood Cliffs, 1982).

Stamper, R., Management Epistemology: Garbage In, Garbage Out, Proceedings of the IFIP 8.3 Working Conference on Knowledge Representation for Decision Support Systems (Durham, 1984).
