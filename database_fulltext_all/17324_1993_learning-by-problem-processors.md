---
otero_id: 17324
otero_key: "TDV9GT62"
title: "Learning by problem processors"
authors: "Clyde W. Holsapple; Ramakrishnan Pakath; Varghese S. Jacob; Jigish S. Zaveri"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90032-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Learning by problem processors Adaptive decision support systems

Clyde W. Holsapple,
Ramakrishnan Pakath

University of Kentucky, Lexington, KY, USA

Varghese S. Jacob

The Ohio State University, Columbus, OH, USA

Jigish S. Zaveri

Morgan State University, Baltimore, MD, USA

Clyde W. Holsapple is Professor of Decision Science and Information Systems and holds the Endowed Chair in Management Information Systems at the University of Kentucky. In addition to his books in the decision support system, data base management and expert system areas, he has many research articles published in such journals as Decision Support Systems, Operations Research, The Computer Journal, Organization Science, Decision Sciences, IEEE Expert, Fi

In this paper, we describe the potential advantages of developing Adaptive Decision Support Systems (Adaptive DSSs) for the efficient and/or effective solution of problems in complex domains. The problem processing components of DSSs that subscribe to existing DSS paradigms typically utilize supervised learning strategies to acquire problem processing knowledge (PPK). On the other hand, the problem processor of an Adaptive DSS utilizes unsupervised inductive learning, perhaps in addition to other forms of learning, to acquire some of the necessary PPK. Thus, Adaptive DSSs are, to some extent, self-teaching systems with comparatively less reliance on external agents for PPK acquisition. To illustrate these notions, we examine an application in the domain concerned with the scheduling of jobs in flexible manufacturing systems (FMSs). We provide an architectural description for an Adaptive DSS for supporting static scheduling decisions in FMSs. We illustrate key problem processing features of the system using an example. A prototype system, based on this architecture, is currently under implementation.

![](/api/attachments/TDV9GT62/fulltext/images/01316be07f87a658765337d81b2c136d29bef1d383d3baa596b05619d7663c90.jpg)

Keywords: Decision support systems; Machine learning; Adaptive DSSs; Flexible manufacturing systems.

nancial Management, Policy Sciences and Recherche Operationnelle. Dr. Holsapple is the DSS Area Editor for ORSA Journal on Computing and Associate Editor for Organizational Computing and Management Science.

![](/api/attachments/TDV9GT62/fulltext/images/de76e6b2a5cae06632d68794de11bf2f89a65e92ad2b2e0eb286f4b10ef21ff3.jpg)

Varghese S. Jacob obtained his Ph.D. degree in Management, majoring in Management Information Systems, from Purdue University in 1986. He is an Assistant Professor in the Department of Accounting and Management Information Systems at The Ohio State University. His teaching and research interests are in Decision Support Systems, Expert Systems, Distributed Systems, Genetic Algorithms and Neural Networks. Dr. Jacob has published articles in various journals including Interfaces, Computer Science in Economics and Management, Decision Support Systems, IEEE Transactions on Systems, Man and Cybernetics, Journal of Economic Dynamics and Control, and International Journal of Man-Machine Studies. He is a member of the Institute of Management Science, IEEE and Association of Computing Machinery.

![](/api/attachments/TDV9GT62/fulltext/images/9e5d8c545f4906f9019b47bf8e88b697afbf3842f84e75827309b5db126fb89d.jpg)

Ramakrishnan Pakath is an Assistant Professor of Decision Science and Information Systems at the University of Kentucky. He received the Ph.D. degree in Management (MIS) from the Krannert Graduate School of Management, Purdue University, in 1988. Ram's research interests and experience are in applying artificial intelligence-based techniques to centralized and distributed decision support- and expert-system design, studying inventory control issues in serial and non-serial manufacturing systems and assessing information value in decision modeling. His articles have appeared or are forthcoming in such forums as Behaviour and Information Technology, Computer Science in Economics and Management, Decision Support Systems, European Journal of Operational Research, Handbook of Industrial Engineering, IEEE Transactions on Systems, Man, and Cybernetics, and Information & Management.

## 1. Introduction

In recent years, the decision support system (DSS) field has come to encompass such paradigms as expert systems (ESs), intelligent DSSs (IDSSs), active DSSs (ADSSs), and systems that seek to take advantage of the benefits of integrating DSSs with ESs (Integrated DS-ESs). Such paradigms have application potential in both individual and multiparticipant support contexts. The degree and extent to which today's DSSs can learn has yet to be investigated in depth. This paper is a step in that direction. It explores the idea of Adaptive DSSs and describes one approach for constructing an Adaptive DSS for the support of static scheduling decisions in flexible manufacturing systems (FMSs).

An examination of the foregoing paradigms from the perspective of machine learning strategies suggests that each performs its problem processing activities utilizing problem processing knowledge (PPK) acquired through one or more supervised learning strategies. Strategies employed currently include rote learning, instructional learning, deductive learning, and learning from examples. Consequently, specific systems that subscribe to these existing DSS paradigms are dependent on external agents for problem processing support. The extent of this dependence is determined by the specific supervised strategies pursued by the paradigm under consideration.

Outside the DSS realm, research on machine learning has also identified several unsupervised learning techniques. In general, unsupervised learning techniques entail less dependence on

![](/api/attachments/TDV9GT62/fulltext/images/55b598883efd8b84724f8b254a3eeba131e35802da480f2517f769dad1e64262.jpg)

Jigish S. Zaveri is an Assistant Professor of Information Systems at Morgan State University. He received the Ph.D. degree in Business Administration (DSIS) from the University of Kentucky in 1992. His thesis research focus was on using genetics-based machine learning techniques to assist with scheduling in flexible manufacturing contexts. His teaching and research interests encompass decision support systems, expert systems, machine learning and manufacturing. He received the B.Tech. degree from the Indian Institute of Technology, Kharagpur, India and the M.S. degree from the University of Kentucky, both in chemical engineering. He has articles that have appeared or are forthcoming in Decision Support Systems, IEEE Transactions on Systems, Man, and Cybernetics, and the Proceedings of the 1990 International Society for Decision Support Systems Conference. He is a member of the Decision Sciences Institute and the Production and Operations Management Society.

external agents in contrast with supervised learning methods. This suggests that there is potential for developing DSSs that generate some or all of the needed problem processing knowledge without the benefit of external agents. This is desirable to the extent that such DSSs would be more self-reliant and agent-independent than systems that subscribe wholly to supervised PPK acquisition methods.

Based on these considerations, Jacob et al. [34] propose the class of Adaptive DSSs, which is distinguished by a form of unsupervised learning called learning through observation and discovery or unsupervised inductive learning. In this paper, we refine and extend that earlier work. The purpose of the refinement is to clearly contrast the proposed paradigm with existing paradigms, in terms of a number of problem processor characteristics. The extension shows how the Adaptive DSS paradigm can be applied in developing a DSS architecture that supports static scheduling decisions in flexible manufacturing contexts. An implementation of this system is currently in progress. Implementation details and performance test results will be reported in subsequent papers. This and other applications are important for studying, testing, and improving Adaptive DSS concepts and techniques.

The rest of this paper is organized as follows. In section 2 we present a brief overview of machine learning literature that is relevant to our work. Section 3 examines each of the aforementioned DSS paradigms (and representative implementations) and assesses the types of learning strategies currently employed by their problem processors. Section 4 describes Adaptive DSSs and contrasts such systems with existing paradigms in terms of key problem processor features. In section 5 we briefly examine the FMS scheduling problem and describe the architecture for an Adaptive DSS that is currently under implementation. We then present an example that illustrates key features of the proposed system. Section 6 contains concluding observations.

## 2. An overview of machine learning

Human learning may be viewed as an amalgam of knowledge acquisition and skill acquisition. Research in the field of machine learning endeavors to develop computational models of learning and thus, impart to computers the abilities to learn. A computer that is endowed with such abilities is called a machine learning system or, more simply, a learning system. Our focus in this paper is primarily on learning for knowledge acquisition and it is in this sense that we use the terms “learning” and “learning systems” in the remainder of the paper. The sophistication of a learning system depends to some extent on the type(s) of learning strategy it pursues. These strategies, largely borrowed from research on human learning, differ from one another in terms of the amounts of inferential responsibility they place on the learner. The greater a system’s inferential abilities, the lesser is its dependence on the external environment for successful learning.

Numerous machine learning strategies have been identified in the machine learning literature [e.g., 8,46,47,55]. For purposes of this discussion, it suffices to note the following spectrum of strategies: Learning by rote, learning from instruction, learning by deduction, learning by analogy, and learning by induction. Learning by induction may itself be viewed as encompassing two broad approaches: Learning from examples (i.e., supervised induction) and learning through observation and discovery (i.e., unsupervised induction). We note that there perhaps exist learning strategies for machines that are significantly different from or superior to strategies humans are known to pursue. However, there has been little research aimed at exploring this possibility.

Michalski and Kodratoff [47] present a classification scheme that categorizes learning approaches as being analytic and/or synthetic. They note that analytic learning strategies seek to analyze and transform existing knowledge into more effective patterns (based on some measure of effectiveness). In addition to input information, these strategies rely on vast amounts of a priori (or background) knowledge and use deduction as the primary inferencing mechanism. Synthetic learning, on the other hand, is primarily concerned with creating fundamentally new knowledge from existing input information with or without the benefit of background knowledge. These approaches use induction as the primary inferencing mechanism. From the perspective of this classification scheme, learning by deduction is an analytical approach, whereas learning by induction is a synthetic approach. Learning that involves both deduction and induction (e.g., based on analogical reasoning) is both synthetic and analytic.

Although individual humans differ from each other in learning abilities, to be viable, a machine learning system must be at least as efficient and/or effective as an ‘average’ human in learning a concept or a task (perhaps within a specific domain or set of domains). Regardless of strategy pursued, it is generally accepted that human learning (while effective) can be a very slow and inefficient process. Consequently, a key concern in machine learning research is to develop systems that are significantly faster than humans in performing some learning activity $[62]$ . To a substantial extent, machine learning efficiency depends on: (i) the type(s) of learning strategy pursued; and (ii) the implementation of this strategy within the system. The latter is highly sensitive to the development language, developer skill, target hardware, and other contextual variables. However, for a given learning task, efficiencies inherent to the various learning strategies are essentially independent of such contextual issues.

To illustrate two extremes, a system that learns by rote performs no inferencing whatsoever. The emphasis is on learning through memorization and the development of indexing schemes to quickly retrieve memorized knowledge when needed. There is no attempt at transforming initial information into new knowledge via either analytic or synthetic learning. An example of a rote learning system would be a conventional word-processing program that accepts and stores typed input as is, and permits this information to be subsequently retrieved intact.

At the other extreme, learning through observation and discovery is a form of inductive learning called unsupervised inductive learning (i.e., learning without the benefit of a teacher or supervisor). A system employing this strategy learns by scrutinizing a relevant environment that contains a concept, or even multiple concepts, of interest without explicit external guidance. The learning task could be further complicated by a noisy and dynamic operating environment. The system must be capable of coping with the possibility of resultant confusion, overload, and distortion to the learning process. Observation itself may be carried out passively (i.e., without disturbing the environment in any way) or actively.

Contained within the spectrum defined by these extremes are: Instructional learning, deductive learning, analogical learning, and learning from examples. We briefly review these learning strategies. A system that learns from instruction depends on external sources (i.e., 'teachers') to incrementally present it with knowledge in an appropriately organized form. From these inputs, the system selects new knowledge that must be acquired (based on what is already known) and performs syntactic reformulation of this knowledge to integrate it with existing knowledge. A deductive learning system performs one or more forms of truth-preserving transformations on existing knowledge to generate new and potentially useful knowledge. Such transformations include the use of macro operators, cacheing, chunking, and so on. Analogical learning involves retrieving, transforming, and augmenting relevant existing knowledge into new knowledge that is appropriate for effectively dealing with a new problem that is similar to some previously encountered problem(s). In learning from examples, a system develops a general description of a new concept based only on examples and, perhaps, counter-examples of the concept that are provided to it by an external entity.

Essentially, learn-by-rote systems pursue the most primitive form of learning, whereas learn-through-observation-and-discovery systems constitute the most sophisticated of learning systems. Learning speed is, to a certain extent, a function of the complexity of the task being learned. Thus, a particular learning strategy may be notably fast in one context but exceedingly slow in another. In general, however, it is fair to state that the learn-by-rote method tends to be fastest from a machine learning perspective. On the other hand, it requires supervision which can be slow, expensive, and/or faulty. While learning through observation and discovery is likely to require more machine time, it avoids such disadvantages of supervision. It, therefore, is an interesting candidate for incorporation into DSSs.

In conclusion, Michalski [46] observes that the intent of a learning activity may differ from one learner to another. The intent may be to: (a) merely acquire new knowledge (although the learner may never again utilize this knowledge); (b) acquire new knowledge to improve current performance; or (c) acquire new knowledge with the intent of generalizing this knowledge for enhancing subsequent performance. Performance is measured in terms of a stated purpose(s) or goal(s) of the learner. A learner may have more than one intent in mind: Our own interest lies in constructing DSSs whose learning intents are as described in (b) and (c) above.

## 3. Decision support paradigms and machine learning

Any DSS may be regarded as subscribing to one or more of the machine learning strategies described in the preceding section. In this section, we formally present the notion of problem processing knowledge (PPK), which is the subject of learning that we focus on in this paper. We then examine the various DSS paradigms mentioned earlier with respect to their PPK acquisition approaches. For each, we assess the associated types of learning strategies.

The learning strategies discussed earlier may be used by a learner for a variety of purposes. From the perspective of DSSs, a system may utilize learning strategies to improve its language system (LS), presentation system (PS), knowledge system (KS), or problem processing system (PPS). (See [4,16] for definitions of these terms.) Here, we are concerned with learning abilities that improve the problem processing behavior of a DSS. This improvement may be in the guise of greater efficiency and/or effectiveness of problem recognition and/or solution.

A common approach to effecting such improvement is through alteration of the KS contents. The KS could contain several types of knowledge. For the purposes of this discussion we focus on the following basic types: Environmental knowledge (i.e., knowledge about the state of some world), procedural knowledge (i.e., knowledge about how to do something), and reasoning knowledge (i.e., knowledge about what conclusions to draw when certain situations exist).

Some of the contents of the KS constitute what we term as the problem processing knowledge (PPK) of the DSS. PPK itself is usually made up of two of the three basic knowledge types: reasoning knowledge and procedural knowledge. For instance, in a rule-based expert system, the PPK is made up of the rules (i.e., reasoning knowledge) and, optionally, the algorithms/heuristics (i.e., procedural knowledge) utilized by these rules. In addition, the KS contains procedural knowledge about how to utilize available PPK, (optionally) reasoning knowledge about when and why a certain piece of PPK may be used, and environmental knowledge about: (a) the objectives of a particular problem processing exercise; and (b) general facts and constraints about the problem domain. Collectively, these are referred to as background knowledge. (See [35] for further discussions on background knowledge and its uses in various learning contexts.) In our rule-based expert system example, such background knowledge includes knowledge on how to control direction of reasoning (i.e., forward, backward, or both), knowledge that provides the system's justification abilities, the goals of the consultation, and so forth.

Essentially, the PPS utilizes PPK, within the framework set by the background knowledge, to operate on input information (also part of environmental knowledge) to generate new knowledge called derived knowledge. Derived knowledge itself may be one or more of the basic knowledge types, i.e., it may be environmental, procedural, or reasoning knowledge.

During the course of a single problem processing episode, available PPK may be repeatedly invoked to generate more and more derived knowledge. Of these, any potentially useful piece of knowledge is stored in the KS while the remainder is discarded (at acquisition time or thereafter). Subsequent processing iterations could utilize useful derived knowledge generated in preceding iterations of the same problem processing task. Also, useful derived knowledge generated in one problem processing episode may be utilized fruitfully in subsequent episodes. Observe that, since derived knowledge itself is made up of environmental, procedural, and/or reasoning knowledge, it could contribute to the pool of available PPK. This is the case when the system derives new procedural and/or reasoning knowledge, and these are used in subsequent processing steps. Thus, it is possible for a DSS to generate some of the necessary PPK through knowledge derivation without having all PPK predefined by an external agent.

In the case of a typical system, all derived knowledge is environmental in nature while all PPK is predefined. This is true, for instance, in traditional expert systems that do not generate new rules but can populate the KS with new facts. Our focus here, however, is on DSSs with the abilities to generate additional, useful PPK (i.e., procedural and reasoning knowledge) without the aid of an external agent to facilitate more effective and/or efficient problem processing. This generation could occur during a single problem processing episode. Newly acquired PPK may be utilized along with existing PPK or in isolation to complete the task in a facile way. Further, PPK acquired during one problem processing effort may be applied in subsequent problem processing situations as well. Finally, the acquisition of new PPK could result in the elimination of some of the existing PPK in the interests of problem processing efficiency and effectiveness.

The remainder of this section examines the PPK acquisition approaches utilized by each of the current DSS paradigms from a machine-learning viewpoint. These discussions serve to provide a platform for our subsequent discussions on Adaptive DSSs and an application.

From the perspective of the above discussions on knowledge types and PPK, a typical traditional DSS is analogous to our earlier example of word-processing software. Once a debugged version of the software constituting the DSS (for a specific application) is resident in storage, it may be repeatedly invoked to correctly perform prespecified problem processing tasks. All of its problem processor capabilities are ordinarily built-in at design time. The PPS does not become more effective or efficient in its abilities to satisfy a user's knowledge needs. The problem processor is invariant, executing stored instructions at a user's behest, but incapable of accommodating changes in its own behavior. This dependence on user direction has lead some researchers to view conventional DSSs as being passive or reactive systems. In essence, conventional DSSs employ PPK acquired through rote learning (from system developers) to conduct all problem processing activities.

Some researchers $[1,3]$ have argued that an ES can play the role of supporting decision making. That is, it functions as a consultant from which the decision maker can get expert advice in the course of his or her deliberations. Such ES usage is typical, for instance, in complex business decision making contexts where a decision maker may seek an expert opinion on some facet of the decision problem but is free to disregard the same in the interests of making a ‘better’ overall decision. A good example of an ES being used as a DSS (for real-time support in a trouble-shooting environment) is the YES/MVS system [21].

An ES employs deductive reasoning mechanisms to transform existing knowledge and inputs into new, more useful representations. The system relies on deductive reasoning laws derived from human experts in performing its functions. This reasoning knowledge constitutes part of the PPK for the ES. The reasoning knowledge is stored in the system's KS, often in the form of if-then rules. The system's PPS (often called an inference engine) uses this knowledge to perform truth-preserving transformations of user inputs based on available background knowledge. The typical ES does not possess the ability to generate new rules of inference for its own use. From the perspective of this limitation, an ES may also be viewed as a system that acquires PPK through rote learning. However, if the ES were equipped with a PPK-acquisition tool such as an intelligent editor, then it would have the ability to learn from instruction and, depending on the capabilities of the editor, by deduction as well. We conclude that, in general, current ESs are typically endowed with rote learning and, perhaps, instructional learning and/or deductive learning capabilities in acquiring PPK.

Another paradigm suggests integrating model-oriented DSSs and ESs to create intelligent support systems that have been called Integrated DS-ESs $[29,30,67]$ . While such integration can take on a variety of forms, the highest potential benefit may be offered by allowing a set of ES components to provide expert-level support to the DSS model-based component of the integrated system. The exact nature of integration is subject to considerable variation $[30,33]$ . A representative example of an Integrated DS-ES is the police patrol scheduling system $[66]$ , where the problem processor is enhanced with ES capabilities.

The learning strategies pursued by an Integrated DS-ES for problem processing depend on whether one or more ES components benefit the problem processing abilities of the integrated system. Given our conclusions concerning PPK acquisition strategies pursued by conventional DSSs and stand-alone ESs above, we observe that an Integrated DS-ES utilizes rote learning only or, perhaps, instructional learning and/or deductive learning as well in acquiring PPK.

Hwang [32] views intelligence in a DSS from a purely model-oriented perspective with the emphasis on two broad categories of models. First, in the absence of any traditional analytical modeling approaches for a decision problem, a decision maker may rely on an expert's reasoning knowledge about the problem domain to construct an AI-based judgmental model. However, if a decision problem is susceptible to analytical modeling, then a decision maker can rely on someone versed in management science/operations research (MS/OR) to construct a procedural model. In this event, the MS/OR consultant is the domain expert. Both types of modeling knowledge may be captured and stored within a support system's KS for subsequent use.

Based on these considerations, Hwang proposes the development of an Intelligent DSS (IDSS) as one that: (i) analyzes a problem and identifies a solution approach; (ii) constructs or searches for an appropriate decision model (i.e., a judgmental model or an analytical model); (iii) executes this model; and (iv) interprets the solution and “learns from the experience”. In essence, the system is largely an expert mathematical modeling consultant (and this is how we view an IDSS in all subsequent discussions). The first three of the features listed are explicit in earlier IDSS notions [4]. The fourth, is our focus in this study.

Other researchers have worked at implementing intelligent mathematical modeling systems (not using the IDSS label but rather under research on model management in DSSs), particularly for the automated construction of linear programming problem statements. The predominant learning approaches utilized by these systems include rote learning [e.g., 2,36,37,38,52], instructional learning [e.g., 43], and a form of deductive learning [e.g., 51]. More recently, Liang and Konsynski [41] describe a framework for developing problem processors equipped with analogical reasoning capabilities for mathematical modeling. To the best of our knowledge, no implementation that utilizes analogical learning exists. Thus, apart from rote learning, current IDSS implementations utilize instructional learning and/or deductive learning for acquiring PPK.

In discussing generic capabilities and roles of knowledge workers and the underlying computerized infrastructure in knowledge-based organizations of the future, Holsapple and Whinston [31] note “(…) these computer coworkers (…) will also actively recognize needs, stimulate insights and offer advice.” The idea is that DSSs could function as intelligent preprocessors and postprocessors with respect to a networked knowledge worker’s activities. More recently, Manheim [44] describes an active DSS (ADSS) as one that “operates in part almost completely independent of explicit direction from the user”. The author contends that ADSSs offer “active” support in contrast to traditional systems that are “passive” (i.e., ‘largely’ user-directed) support systems. Further, Manheim proposes a symbiotic DSS (SDSS) as a special case of an ADSS where independent processing by the system is enhanced through a model of the user’s ‘image’ of the problem that is generated during a particular problem processing session and stored by the system. The model could presumably change during the course of the problem processing episode as the user’s grasp of the problem changes. More generally, the notion of storing diverse kinds of user knowledge in the KS has been discussed in [16].

Mili [50] suggests that ADSSs themselves could differ in; (i) the nature of active support provided (i.e., the system may behave as an associate, an advisor, a critic, a stimulator, etc.); and (ii) the manner in which independent processes are initiated by the system (i.e., the system may work in parallel with the user on a problem, in tandem to check the consistency of the user's solution, etc.).

Raghavan and Chand [53] argue that it may be difficult to build effective SDSSs due to the inherent complexities in comprehending a user's decision making process. Rather than attempting to capture such knowledge, they suggest that the appropriate direction would be to use a suitable generic structuring technique that may be applied to the problem under consideration. Based on insights gathered via structuring, one may construct an ADSS for enhanced decision support. The authors describe a prototype ADSS called JANUS that uses the analytical hierarchy process [54] for problem structuring.

However, subsequent to this, Manheim et al. [45] discuss the development of an SDSS called intelligent scheduler's assistant (ISA) for production planning and scheduling in steel mills. As ISA is being used for a particular scheduling exercise, the system monitors and analyzes the user's usage pattern in parallel and acts as an advisor by suggesting alternative schedules. Alternately, the system has the capacity to work independent of (and in parallel with) the user on developing a schedule and schedule variations (rather than monitoring the user's schedule building process). A key component of the system is the history inference processor (HIP). The primary objective of the HIP is to use historical information captured during the session by a History Recorder component to construct a conceptual model (a set of schemas) of the users 'image' of the problem. This conceptual model is used by the system in conducting its own independent analysis of the problem and in activating appropriate processes. If necessary, the user may also directly access the model to facilitate his/her own analysis. Other descriptions of SDSS implementations are contained in [15,44].

Our review of available literature on current implementations suggests that SDSSs/ADSSs acquire PPK using deductive learning and special cases of learning from examples in addition to knowledge learned by rote. ISA, for instance, uses the technique of part-to-whole generalization in learning from examples. Similarly, Shaw et al. [60] describe an approach (although not using the ADSS label) for model selection and refinement in model management, that uses a special case of learning from examples called instance-to-class generalization.

![](/api/attachments/TDV9GT62/fulltext/images/a0e25f719c32fa151449454a4377f410b56cd0afa8e5ec5b051810833a269021.jpg)  
Fig. 1. Relationships among DSS paradigms.

Fig. 1 summarizes relationships among the foregoing DSS paradigms based on two problem processor-related factors. On the one hand, we have two broad subclasses of DSSs: Active DSSs (i.e., whose problem processors are largely self-driven), and passive or reactive DSSs (i.e., whose problem processors are largely user-driven). On the other, DSSs may be categorized as being non-adaptive DSSs (i.e., whose problem processors acquire and eliminate PPK via supervised learning strategies) and adaptive DSSs (i.e., whose problem processors acquire and eliminate PPK through unsupervised learning). Thus the space of possible DSSs may be (loosely) subdivided into four quadrants corresponding to: (a) non-adaptive, reactive systems; (b) non-adaptive, active systems; (c) adaptive, reactive systems; and (d) adaptive, active systems.

From the perspective of this framework, virtually all traditional DSSs may be viewed as non-adaptive, reactive systems. A large proportion of Integrated DS-ESs are also non-adaptive, reactive systems. In the remainder, the integral ES components that benefit the problem processor are highly user-independent (i.e., self-driven). The systems are, hence, non-adaptive, active systems. A stand-alone ES may be regarded as a special case of an Integrated DS-ES, where the system (is wholly an ES and hence) contains no other DSS components. As with the more general Integrated DS-ES, an appreciable fraction of ESs may be viewed as being non-adaptive, reactive systems while a relatively smaller proportion are non-adaptive and active.

Observe that an Integrated DS-ES where the system acts as an expert analytical/judgmental modeling consultant to users is tantamount to an IDSS. However, IDSSs may also be constructed without explicit integration of separate DSS and ES components. Based on Hwang's [32] description of IDSSs, it would appear that a large proportion of IDSSs would be non-adaptive, active systems. Nonetheless, it is conceivable that some IDSSs may be regarded as being non-adaptive and reactive. Finally, ADSSs/SDSSs are largely non-adaptive and active with a smaller proportion of such systems being adaptive and active. However, such ADSSs/SDSSs are adaptive only in a very limited sense, as evidenced by our discussions in section 4.

Observe from fig. 1 that the quadrants pertaining to adaptive, reactive systems and adaptive, active systems are essentially empty. Our own interest lies in developing systems that lie largely in the adaptive, active quadrant. We do not believe that the adaptive, reactive sector represents interesting DSS research possibilities and will receive much research attention.

## 4. Adaptive decision support systems

The preceding section analyzed existing DSS paradigms from the perspective of learning strategies utilized in acquiring PPK. Here, we develop what we call the Adaptive DSS paradigm and contrast it with other DSS paradigms in terms of several key problem processor characteristics. Unlike implementations of existing paradigms, by our definition, Adaptive DSSs would subscribe to some form(s) of unsupervised inductive learning in acquiring PPK, in addition to conventional rote learning and, perhaps, other forms of learning.

There exist several manifestations of the unsupervised inductive learning (i.e., learning through observation and discovery) approach. Michalski et al. [48,49], and Kodratoff and Michalski [35] discuss various types of unsupervised learning methods at length. While all of these are candidates for use in Adaptive DSSs, we focus on one such method: Genetic algorithms (GAs). We expect that, in general, the choice of an appropriate method may be task dependent. For the application problem we are using to explore Adaptive DSS possibilities (i.e., static scheduling in FMSs), GAs seem particularly valuable. A brief overview of this problem area and our motivation for using GAs as the unsupervised inductive learning mechanism for this context are contained in section 5. A concise discussion on GAs and some of their applications is contained in Appendix A.

In contrast with usual realizations of other DSS paradigms, Adaptive DSSs exhibit the following characteristics with regard to the nature of the problem processor. These are summarized in table 1.

\- Unlike traditional reactive DSSs, Adaptive DSSs (like ADSSs/SDSSs and some ESs, Integrated DS-ESs, and IDSSs) offer active problem processing support. That is, the nature and extent of problem processing support offered are not wholly dependent on explicit directions provided by users. Adaptive DSSs are usually highly active systems.

Table 1  
Comparison of problem processor characteristics for various DSS paradigms

<table><tr><td>Characteristic</td><td>DSSa</td><td>ES</td><td>Integrated DS-ES</td><td>IDSS</td><td>ADSS/SDSS</td><td>AdDSSb</td></tr><tr><td>1. Self organizing?</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Partly</td><td>Yes</td></tr><tr><td>2. Symbiotic focus?</td><td>Little</td><td>Little</td><td>Little</td><td>Little</td><td>High with SDSS</td><td>Little</td></tr><tr><td>3. Justification ability?</td><td>Usually no</td><td>Usually yes</td><td>Perhaps</td><td>Perhaps</td><td>Perhaps</td><td>Usually no</td></tr><tr><td>4. Treatment of reasoning knowledge?</td><td>Usually equal</td><td>Depends but static</td><td>Depends but static</td><td>Depends but static</td><td>Depends but static</td><td>Unequal and dynamic</td></tr><tr><td>5. Learning strategies currently pursued?</td><td>Rote</td><td>Rote, instruction, deduction</td><td>Rote, instruction, deduction</td><td>Rote, instruction, deduction</td><td>Rote, deduction, supervised induction</td><td>Rote, unsupervised induction</td></tr></table>

$^{a}$ Traditional DSS.  
$^{b}$ Adaptive DSS.

\- Unlike DSSs, ESs, Integrated DS-ESs, and IDSSs that are externally-organized systems, Adaptive DSSs are self-organizing in that they acclimatize themselves to currently available information and current environmental conditions. By “acclimation” we mean that self-organizing systems are capable of independently acquiring and eliminating PPK that drives the problem processor. In this sense, Adaptive DSSs perform algorithm management, although the user may not be always aware of the specifics of this management activity. (This is not to imply that the system may not be equipped with other, explicit algorithm management techniques.)

While it may be argued that ADSSs/SDSSs also possess the ability to add to existing knowledge (in particular, PPK), an Adaptive DSS can identify and purge itself of knowledge that is deemed relatively useless. The space thus freed can be used to store newly-acquired processing (and other) information. The History Recorder component of an ADSS/SDSS, however, attempts to maintain all of the knowledge acquired during a problem solving episode with no attempt at knowledge elimination. Apart from the drawbacks of significant storage overheads, processing based on highly historical information may cause overload problems and may be irrelevant in dynamic environments.

Further, unlike ESs, and perhaps Integrated DS-ESs, Adaptive DSSs do not depend entirely on domain experts, knowledge engineers, or intelligent editors for problem processing knowledge acquisition (and elimination).

\- Unlike SDSSs, there is little focus on symbiosis, where the human and machine components thrive on mutualism. To borrow SDSS terminology, Adaptive DSSs are highly “computer directed process” oriented. At the same time, the system is not completely dependent on predefined PPK like traditional DSSs, ESs, and Integrated DSEs. Their self-organizing capability allows Adaptive DSSs to selectively acquire and eliminate PPK.

\- Unlike ESs, and perhaps Integrated DS-ESs, IDSSs, and ADSSs/SDSSs, Adaptive DSSs may lack the ability to explain or Justify reasoning processes. Although this may appear as an apparent weakness, note that an ES's explanation capabilities must also be predefined and stored in the KS. In many complex contexts, even human experts may be unable to explain their thinking. This is true especially in novel problem-solving situations where experts rely more on general problem solving abilities rather than problem-specific skills. In such contexts, problem solving is intermixed with learning and discovery. Adaptive DSSs behave much in the same manner.

\- In Adaptive DSSs, unlike virtually all other DSS paradigms, all problem processing knowledge is not treated equal. The approach utilizes goodness measures that attribute “fitness values” to the processing knowledge elements in the system. This is much like prioritizing the rules in an ES. However, unlike ESs where rule priorities are generally fixed, in Adaptive DSSs the fitness values are dynamic and determined through controlled experimentation.

Having presented these contrasting characteristics, we note that the term adaptive applies to this class of support systems in the following sense. The paramount feature of an Adaptive DSS is its ability to start with an initial set of very generic PPK and, if necessary, to progressively refine this knowledge (through implicit algorithm management techniques acquired at run-time via unsupervised learning strategies) to generate problem processing capabilities commensurate with existing conditions. The system, thus adapts itself to a knowledge state where it (generates and) possesses the desired problem processing capabilities, rather than having such abilities predefined. While such abilities are certainly useful in static contexts, they are especially desirable in dynamic environments where predefinition of processing abilities could be impossible or undesirable.

It is also worthwhile noting that adaptability does not necessarily imply generalizability. Adaptation occurs during the course of a particular problem processing episode. Depending on context, it may be possible to generalize the knowledge acquired through such adaptation for the benefit of resolving other, similar problem instances through further adaptation. Thus, while generalizable systems are indeed adaptive systems, all adaptive systems need not be generalizable.

## 5. An illustration: Adaptive DSSs for scheduling in FMS contexts

In this section we introduce one of possibly many application areas that could benefit from an Adaptive DSS. We provide a brief overview of the issues involved in making static scheduling decisions in flexible manufacturing systems (FMSs) and the design of an Adaptive DSS for effective support of such decisions. This application serves to illustrate and explore the general Adaptive DSS ideas in a concrete setting. Having presented an architecture, we provide an example that demonstrates the key problem processor features of the proposed system. Currently, we are implementing a prototype version of this Adaptive DSS. Implementation details and the results of performance tests for the implementation will be reported in other forums.

## 5.1. The static scheduling problem in FMSs and existing approaches

In the most general case, an FMS uses either a central supervisory computer or a set of cell-host computers that are interconnected via a local area network to monitor and control a set of flexible manufacturing cells and automated material handling procedures. Each cell in the system consists of one or more workstations. Typically, each station is capable of performing a variety of manufacturing operations. Also, a given operation could be performed by more than one station in the system and these stations may be located in different cells. Such redundancy is built into the system to protect against system failures. A job, consisting of a single part or several units of a particular type of part that are demanded as a batch, may be entirely processed using the capabilities of a single manufacturing cell or may require processing at workstations located in multiple cells. Typically, all part units in a job require several operations to be performed in a particular sequence (called the operational precedence requirement for that part/job). Usually, each cell is equipped to perform a set of operations needed by a “family” of parts, i.e., parts belonging to different batches that share common operational requirements.

At the operational control level, FMS scheduling decisions must be made on a routine basis to account for several complex issues. Paramount among these are the issues of: (a) prioritizing jobs for release into the system; (b) examining and picking a 'good' or the 'best' route for each job, from amongst alternative ways of routing the job within the system; and (c) accounting for unexpected shocks (i.e., system failures) and turbulence (i.e., sudden job influxes and cancellations).

One way of handling the FMS scheduling problem is to divide the scheduling exercise into two stages comprised of the static scheduling stage and the dynamic rescheduling stage. Essentially, static scheduling ignores the dynamic nature of the operating environment characterized by factors mentioned in item (c) above. Static scheduling is normally done ahead of run-time, based on hard and soft constraints only (i.e., system specifications, objectives of the scheduling exercise, etc.). If there are no shocks and/or turbulence at run-time, the static schedule may be implemented as is. However, this is not always the case. It is usually necessary to repeatedly adjust the static schedule at run time to account for prevailing conditions. Such adjustments are collectively referred to as dynamic rescheduling. Regardless, there always is some probability that dynamic rescheduling may be unnecessary during a particular production run. It is therefore customary to attempt to construct 'good quality' static schedules. Further, a good static schedule serves as a benchmark against which alternate dynamic schedules may be compared prior to implementation.

For ease of exposition, we limit our discussion of Adaptive DSS design in this paper to the case of static schedule generation only. To lend some motivation for developing Adaptive DSSs in this context, it is worthwhile briefly examining the existing AI-based approaches to the FMS scheduling problem. Several researchers have approached the problem using traditional ES-oriented concepts/implementations [e.g., 6,7,40,64]. Other researchers [e.g., 13,56,57,58] view the problem as a special case of the planning paradigm in AI and use the state-operator approach to generate schedules. Yet others [e.g., 14,61] utilize frame-based approaches in conjunction with scheduling algorithms and heuristics like beam search.

Virtually all of these studies make use of rote learning, with a few making use of deduction [e.g., 58] and supervised induction (i.e., learning from examples) [e.g., 59] for acquiring PPK. In particular, to our knowledge there exist no implementations that utilize some form of unsupervised induction for gathering PPK. Also, the existing methods either: (i) consider each job in isolation first in generating an initial static schedule and then attempt to improve schedule quality by using some heuristic methods to account for conflicts in resource requirements [e.g., 13,56,57, 58]; (ii) consider scheduling jobs in some random sequence, such as first-come-first-served basis [e.g., 6]; or (iii) attempt to consider all jobs simultaneously, with solution-space pruning if this strategy becomes unwieldy [e.g., 14].

Our Adaptive DSS for the problem pursues a different strategy that: (a) uses unsupervised inductive learning for acquiring some of the necessary PPK; (b) seeks to improve schedule quality by avoiding the extremes of considering jobs in isolation, simultaneously, or in some random sequence; and (c) seeks to improve schedule generation speed by implicitly examining several alternative schedules concurrently and pruning out bad ones a priori (see discussion on “implicit parallelism” of GAs contained in $[5]$ ).

We also note that the applicability and performance of the proposed learning mechanism – genetic algorithms – has been examined in the context of scheduling by many researchers, although none of these efforts were directed at scheduling in FMSs. Noteworthy amongst these are the numerous studies on GAs in the context of single-machine job shop scheduling [e.g., 22,23,24,26], multistage flow shop scheduling [e.g., 9,68], multi-objective workforce scheduling [25], and limited-resource scheduling in a time-constrained environment [65].

## 5.2 The Adaptive DSS approach to the problem

The general strategy being explored in this Adaptive DSS application is as follows:

Initialization. Start with a set of 'seed' job sequences. Determine (using an appropriate heuristic or algorithm) a 'good' or 'best' sequence-dependent schedule corresponding to each seed sequence in the set.

Iterative step.

(a) Measure the quality of each sequence-dependent schedule currently available (in terms of predefined measures). (Re)assess the fitness value for each sequence currently available. IF

Prespecified stopping criteria have been met, STOP. OUTPUT THE BEST SCHEDULE GENERATED THUS FAR.

ELSE

(b) Utilize knowledge about existing sequence fitnesses to generate a 'better' set of job sequences using a genetic algorithm.

(c) Determine a ‘good’ or ‘best’ sequence-dependent schedule corresponding to each sequence in the revised set.

(d) Go to (a).

By a sequence-dependent schedule we mean a schedule that is somehow dependent on the sequencing of jobs in a job list. Such schedules are also part of the total space of legal schedules (i.e., schedules that do not violate the operational precedence requirements for each job) for the set of jobs in the list. We are not attempting to obtain the optimal solution for the problem but only good solutions. To contain our search efforts, we must prune the space of possible solutions (i.e., legal schedules). One way of pruning is to isolate regions in the solution space corresponding to different sequence-dependent schedules. Having done this, the GA seeks to make the search process more efficient by: (1) implicitly searching multiple regions in parallel; and (2) not necessarily searching all such regions. We next discuss a few approaches to developing sequence-dependent schedules.

For instance, the scheduling method may consider the first job in the list first, and schedules all of its operations. It then picks the second job in the list, and schedules all of its operations next, while accounting for resource usage by the first job. The process continues until the last job and all of its operations are scheduled.

![](/api/attachments/TDV9GT62/fulltext/images/7b8cd7dbe9d87aa7f109d8e785dc54eebea815f4f1ab217b7d570012b27331a4.jpg)  
Fig. 2. System architecture.

We may devise many such methods for generating sequence-dependent schedules. For example, we may group together and schedule all of the operations of the first k jobs in a sequence of n jobs (k < n) first, and repeat the procedure for the next set of k jobs, and so on. Note that, in this variant, it is not necessary that all operations of the $(j - 1)$ th job be scheduled prior to scheduling the operations of the jth job in the sequence. Rather, the method schedules all operations of the $(j - 1)$ th batch of jobs (of size k) before considering jobs in the jth batch. A second variant operates such that in one pass of the method, the first i operations of all jobs (considered in the appropriate sequence) are scheduled. The next i operations are scheduled in the second pass, and so on. By appropriately varying the parameters k and i in the two methods, a variety of sequence-dependent schedules may be generated for a given sequence.

In the following section, we present an overview of the architecture for an Adaptive DSS we are currently exploring that incorporates such sequence-dependent scheduling methods and GA-based search capabilities.

## 5.3 An overview of the Adaptive DSS architecture

Fig. 2 presents the surface architecture for an Adaptive DSS that supports static schedule generation in FMS contexts. The system has 4 major components, the language system (LS), the presentation system (PS), the knowledge system (KS) and the problem processing system (PPS). Our primary focus is on the design and implementation of the PPS. We briefly discuss the other subsystems collectively and then consider the PPS in more depth.

## 5.3.1. The knowledge system, language system, and presentation system

In general, the KS could contain a variety of knowledge types. In the FMS scheduling context, we focus on two basic types: Environmental knowledge, and procedural knowledge. The available procedural knowledge includes: (a) optimal and/or heuristic sequence-dependent scheduling methods; (b) schedule quality evaluation procedures; (c) a GA; and (d) a 'current' set of job sequences with associated sequence-dependent schedules. Environmental knowledge includes: (a) FMS-specific hard constraints pertaining to the topology and design of the FMS; (b) all information input by the user at run-time that must be stored for subsequent processing; and (c) a set of 'fitness' measures corresponding to each member of the current set of job sequences. Note that we treat the set of job sequences as procedural knowledge. Apart from the obvious interpretation that a particular sequence explicitly 'tells' us one way of sequencing the jobs, the sequence itself is a manifestation of some underlying sequencing rule.

User inputs (via the LS) pertain largely to information concerning the scheduling exercise under consideration (e.g., number of jobs, operational precedences, objective(s), and so forth). In addition, the user may choose to supply an initial set of 'seed' job sequences to the system or have the system generate this set. This initial set is stored as the 'current' set of sequences (i.e., as part of the procedural knowledge) by the system at the beginning of the session. The set of sequences could change with time, based on fitness measures assigned to the members by the PPS.

Some of the contents of the KS are subject to periodic (i.e., scheduled) and random updates. Only scheduled updates are of importance for the purposes of this study. Random updates (e.g., due to unexpected station failures, job cancellations, and so on) must be considered when dealing with the dynamic rescheduling activity. Scheduled updates for the hard constraints typically become known before a scheduling exercise. They include information on preventive maintenance shutdowns for stations, design changes to the system, and so on. Scheduled updates of the job sequence information contained in the KS is carried out by the problem processor during solution.

The PS is the component that handles the outputs of the system. The single major output is the final static schedule and related information generated by the system. The PS is also used for displaying error messages and for prompting the user for further information/clarifications. As such, all three components of the PPS (discussed next) provide inputs to the PS.

## 5.3.2. The problem processing system

An example that illustrates the basic functions and the inductive learning ability of the PPS is contained in section 5.4. Here, we discuss this subsystem in more abstract terms. The PPS contains three subcomponents: The sequence discovery system (SDS), the schedule generation system (SGS), and the schedule evaluation system (SES). As mentioned earlier, the PPS uses unsupervised inductive learning for acquiring some of the needed PPK. The PPS first accesses each sequence in the 'current' set of job sequences, and utilizes the schedule generation system (SGS) to build a sequence-dependent schedule utilizing one of the possibly many heuristic/algorithmic methods contained in the KS. In doing so, the SGS also accounts for user input information and the FMS-specific hard constraints.

Each of these schedules is passed on to an evaluation component, the schedule evaluation system (SES), that associates a measure of goodness called a total fitness value with the schedule, and hence with the sequence that forms the basis for that schedule. The SES itself utilizes predefined evaluation methods contained in the KS. One component of the total fitness for a sequence is the extent to which the objective of the scheduling task is being met (i.e., the quality of the generated schedule). For instance, if the objective is due-date satisfaction, then this component would reflect the extent of due-date violation by a schedule. Further, the total fitness of a sequence is also influenced by its past and anticipated performance in generating 'good' offspring sequences as discussed below.

The sequence discovery system (SDS) utilizes a GA stored in the KS to access a set of 'parent' sequences from the existing sequences in the KS and to generate new 'offspring' sequences by applying genetic operators to these parents. (Appendix A contains a brief review of GAs and their applications.) The selection of parent sequences is based on the associated total fitness values of the current sequences in the KS. Essentially, a set of highly fit sequences are chosen as parents. Unions among the parent sequences are based on hypotheses concerning the quality of the resultant offspring. For each such union, the method applies genetic operators to the parent sequences involved and generates (i.e., hypothesizes) an offspring sequence(s) that could possibly yield a schedule of the hypothesized quality. The generated sequence is passed on to the SGS for schedule generation. The schedule is then passed on to the SES for evaluation and fitness assignment. The deviation of an offspring's actual quality from its hypothesized quality is then used to influence (positively or negatively) the total fitness values of all ancestors of the offspring. Having discovered new sequences, better (i.e., more fit) sequences (along with their associated fitness values) replace poorer sequences in the sequence set contained in the KS.

The cyclical process consisting of schedule-generation, schedule-evaluation, and sequence-discovery terminates when predefined stopping criteria have been satisfied. At this stage, the best schedule generated thus far is output. A variety of terminating conditions may be specified. For instance, the system may be asked to terminate as soon as a schedule whose makespan is within prespecified bounds is discovered.

We now draw attention to those features of the DSS just described that qualify it as an Adaptive DSS in terms of the characteristics of an Adaptive DSS discussed in section 4. As we discuss with an example in section 5.4, implicitly, the system repetitively hypothesizes and validates reasoning rules of the conventional IF-THEN form found in traditional ESs

$$
S _ {\mathrm{a}} \rightarrow Q _ {\mathrm{a}} (f _ {\mathrm{a}}),
$$

that states: “If sequence $S_{a}$ is involved in a union with some member of the current genetic pool, then the resultant offspring would have a quality level of at least $Q_{a}$ (with an associated rule fitness value of $f_{a}$ ).”

If a union does take place between $S_{a}$ and some member $S_{b}$ of the current genetic pool, the result is the addition of a new (offspring) sequence $S_{c}$ and a corresponding rule, $S_{c} \rightarrow Q_{c}(f_{c})$ to the knowledge system. Depending on predefined limits on allowable population size, it is also possible that the addition of $S_{c}$ could result in an existing sequence, and hence its corresponding rule, being dropped from the knowledge system. During this process, the rule set is revised and the fitness values of the revised rules are computed. Thus, in contrast with conventional ESs, in our Adaptive DSS both the rule set as well as rule fitness values are dynamic.

The process of sequence-discovery is an unsupervised learning strategy because there is no external agent who is providing the system with carefully constructed example schedules from which to draw inferences concerning desirable and undesirable sequences. Also note that the system, through the process of discovering new sequences, is essentially discovering new sequencing heuristics (e.g., the SAPT (i.e., shortest-average-processing-time first) rule, or the EDD (earliest-due-date first) rule, etc.). However, the discovery of such sequencing rules may be opaque to humans. Thus, the system performs implicit algorithm management in deciding which sequencing heuristics to maintain and which to eliminate over time. In doing so, the SDS does not act in a totally random fashion. Its actions are guided by what it observes in the environment: i.e., the fitness measures generated by the SES.

The process of learning is inductive for a variety of reasons:

(a) there is a mechanism for generating plausibly useful new reasoning rules (i.e., via the sequence-discovery process);

(b) there is a mechanism for assessing the plausibility of generated rules (i.e., the rule fitness values) and revising belief based on the assessment;

(c) there is a mechanism for discovering sequencing heuristics without being told what such a heuristic is and without being provided with examples of such heuristics.

Finally, note that learning occurs during a problem processing episode to facilitate the current problem processing task. All of the needed PPK is not predefined as some of it (i.e., various job sequencing rules and hence various reasoning rules) is acquired incrementally at run time. At the end of one problem processing episode, we will have identified a “best-so-far” sequence for the current problem and numerous ‘good’ sequences as well. To clearly visualize the learning that has occurred during the solution of the problem, consider the following: Suppose the system were asked to solve the same problem instance once again, with all other parameters being held the same and the only difference being that the current solution process begins with the population remaining at the end of the last attempt. The system will now converge to the solution it last discovered much faster as it now begins with the revised (better) initial population as opposed to the original starting population. It is indeed possible that it may proceed to discover a better solution than it last did. In any event, the solution will never be poorer than any previously discovered solutions. Thus, even with repeated attempts at, solving the same problem instance, the system seeks to progressively adapt itself to more useful knowledge states. This behavior is quite different from traditional optimization and heuristic procedures where the solution process is usually repeated in its entirety and the solution path followed is exactly the same in each repetition. The underlying random behavior of the genetic operators ensures that in subsequent trials, the system is likely to explore solution paths that are different from the ones previously examined. Yet, the nature of the genetic operators also ensures that the resultant search is not chaotic.

It is clearly possible to generalize the knowledge acquired during one problem solving session to other, similar problem contexts. The sequences left in the population at the end of one session, could be used to provide an initial (seed) population for subsequent episodes where the problem inputs have ‘similar’ characteristics. Whether or not two problem instances are similar may be determined, for instance, through the use of predefined similarity measures. Alternately, the system may possess analogical reasoning capabilities to make such decisions on its own. We are currently exploring various such approaches with a view to incorporating similarity recognition abilities within the system.

The following section presents a concrete example illustrating key features of the proposed Adaptive DSS. The example demonstrates how inductive learning occurs, how new procedural and reasoning knowledge are acquired, and how existing knowledge is purged, if need be. Some of the computational mechanisms we use in the example are still under investigation. Nevertheless, the example adequately conveys the general thrust of our approach.

## 5.4 An example

Tables 2–4 characterize an FMS and a scheduling problem of interest. Table 2 displays the setup and processing times $S(\mathrm{Oj})$ and $P(\mathrm{Oj})$ , respectively, for 5 operations labeled O1, O2, ..., O5 in an FMS consisting of 5 workstations denoted as M1, M2, ..., M5. For example, row 1 of the table indicates that operation O1 requires set up and processing times of 2 and 40 time units, respectively, at station M1, 5 and 45 time units, respectively, at station M3, and 5 and

Table 2  
Station set up and processing times

<table><tr><td>Operations</td><td>M1</td><td>M2</td><td>M3</td><td>M4</td><td>M5</td></tr><tr><td>S(O1)</td><td>02</td><td>-</td><td>05</td><td>-</td><td>05</td></tr><tr><td>P(O1)</td><td>40</td><td>-</td><td>45</td><td>-</td><td>85</td></tr><tr><td>S(O2)</td><td>-</td><td>10</td><td>-</td><td>03</td><td>-</td></tr><tr><td>P(O2)</td><td>-</td><td>99</td><td>-</td><td>45</td><td>-</td></tr><tr><td>S(O3)</td><td>03</td><td>-</td><td>05</td><td>-</td><td>-</td></tr><tr><td>P(O3)</td><td>35</td><td>-</td><td>75</td><td>-</td><td>-</td></tr><tr><td>S(O4)</td><td>-</td><td>10</td><td>-</td><td>-</td><td>03</td></tr><tr><td>P(O4)</td><td>-</td><td>90</td><td>-</td><td>-</td><td>40</td></tr><tr><td>S(O5)</td><td>05</td><td>-</td><td>-</td><td>02</td><td>-</td></tr><tr><td>P(O5)</td><td>90</td><td>-</td><td>-</td><td>45</td><td>-</td></tr></table>

Table 3  
Interstation transfer times

<table><tr><td>Machine</td><td>M1</td><td>M2</td><td>M3</td><td>M4</td><td>M5</td></tr><tr><td>M1</td><td>00</td><td>10</td><td>10</td><td>15</td><td>10</td></tr><tr><td>M2</td><td>15</td><td>00</td><td>10</td><td>10</td><td>-</td></tr><tr><td>M3</td><td>15</td><td>15</td><td>00</td><td>-</td><td>-</td></tr><tr><td>M4</td><td>15</td><td>10</td><td>-</td><td>00</td><td>-</td></tr><tr><td>M5</td><td>-</td><td>-</td><td>15</td><td>-</td><td>00</td></tr></table>

Table 4

Operations and precedence requirements for jobs

<table><tr><td>Job</td><td>operations-required</td></tr><tr><td>1</td><td>O1, O2, O5</td></tr><tr><td>2</td><td>O1, O3</td></tr><tr><td>3</td><td>O1, O4</td></tr><tr><td>4</td><td>O1, O2, O4</td></tr></table>

Table 5  
Population at the start of the search

<table><tr><td rowspan="2">Sequence</td><td colspan="2">Actual</td><td colspan="3">Relative</td></tr><tr><td>Makespan</td><td>Anticipation</td><td>Makespan</td><td>Anticipation</td><td>Total</td></tr><tr><td>S01: 1234</td><td>318</td><td>300.50</td><td>0.3745</td><td>0.3539</td><td>0.7285</td></tr><tr><td>S10: 2341</td><td>274</td><td>278.50</td><td>0.3227</td><td>0.3280</td><td>0.6507</td></tr><tr><td>S17: 3412</td><td>257</td><td>270.00</td><td>0.3027</td><td>0.3180</td><td>0.6207</td></tr><tr><td>Sum</td><td>849</td><td>849.00</td><td>1.0000</td><td>1.0000</td><td>2.0000</td></tr></table>

Table 6  
Population after iteration 1

<table><tr><td rowspan="2">Sequence</td><td colspan="2">Actual</td><td colspan="3">Relative</td></tr><tr><td>Makespan</td><td>Anticipation</td><td>Makespan</td><td>Anticipation</td><td>Total</td></tr><tr><td>S01: 1234</td><td>318</td><td>305.63</td><td>0.2710</td><td>0.2481</td><td>0.5192</td></tr><tr><td>S10: 2341</td><td>274</td><td>312.88</td><td>0.2335</td><td>0.2540</td><td>0.4876</td></tr><tr><td>S17: 3412</td><td>257</td><td>304.38</td><td>0.2190</td><td>0.2471</td><td>0.4662</td></tr><tr><td>S15: 3214</td><td>324</td><td>308.63</td><td>0.2762</td><td>0.2506</td><td>0.5268</td></tr><tr><td>Sum</td><td>1173</td><td>1231.50</td><td>1.0000</td><td>1.0000</td><td>2.0000</td></tr></table>

Table 7  
Population after iteration 2

<table><tr><td rowspan="2">Sequence</td><td colspan="2">Actual</td><td colspan="3">Relative</td></tr><tr><td>Makespan</td><td>Anticipation</td><td>Makespan</td><td>Anticipation</td><td>Total</td></tr><tr><td>S01: 1234</td><td>318</td><td>301.80</td><td>0.2226</td><td>0.2044</td><td>0.4271</td></tr><tr><td>S10: 2341</td><td>274</td><td>303.80</td><td>0.1918</td><td>0.2058</td><td>0.3977</td></tr><tr><td>S17: 3412</td><td>257</td><td>295.30</td><td>0.1799</td><td>0.2000</td><td>0.3800</td></tr><tr><td>S15: 3214</td><td>324</td><td>304.80</td><td>0.2268</td><td>0.2065</td><td>0.4333</td></tr><tr><td>S24: 4321</td><td>255</td><td>270.30</td><td>0.1785</td><td>0.1831</td><td>0.3617</td></tr><tr><td>Sum</td><td>1428</td><td>1476.00</td><td>1.0000</td><td>1.0000</td><td>2.0000</td></tr></table>

Table 8  
Population after iteration 3

<table><tr><td rowspan="2">Sequence</td><td colspan="2">Actual</td><td colspan="3">Relative</td></tr><tr><td>Makespan</td><td>Anticipation</td><td>Makespan</td><td>Anticipation</td><td>Total</td></tr><tr><td>S01: 1234</td><td>318</td><td>295.92</td><td>0.1935</td><td>0.1793</td><td>0.3728</td></tr><tr><td>S10: 2341</td><td>274</td><td>292.79</td><td>0.1667</td><td>0.1774</td><td>0.3442</td></tr><tr><td>S17: 3412</td><td>257</td><td>263.79</td><td>0.1564</td><td>0.1598</td><td>0.3162</td></tr><tr><td>S15: 3214</td><td>324</td><td>298.92</td><td>0.1972</td><td>0.1811</td><td>0.3783</td></tr><tr><td>S24: 4321</td><td>255</td><td>254.17</td><td>0.1552</td><td>0.1540</td><td>0.3092</td></tr><tr><td>S23: 4312</td><td>215</td><td>244.42</td><td>0.1308</td><td>0.1481</td><td>0.2789</td></tr><tr><td>Sum</td><td>1643</td><td>1650.00</td><td>1.0000</td><td>1.0000</td><td>2.0000</td></tr></table>

Table 9  
Population during iteration 4

<table><tr><td rowspan="2">Sequence</td><td colspan="2">Actual</td><td colspan="3">Relative</td></tr><tr><td>Makespan</td><td>Anticipation</td><td>Makespan</td><td>Anticipation</td><td>Total</td></tr><tr><td>S01: 1234</td><td>318</td><td>294.71</td><td>0.1673</td><td>0.1512</td><td>0.3185</td></tr><tr><td>S10: 2341</td><td>274</td><td>294.21</td><td>0.1442</td><td>0.1509</td><td>0.2951</td></tr><tr><td>S17: 3412</td><td>257</td><td>275.71</td><td>0.1352</td><td>0.1414</td><td>0.2767</td></tr><tr><td>S15: 3214</td><td>324</td><td>297.71</td><td>0.1705</td><td>0.1527</td><td>0.3232</td></tr><tr><td>S24: 4321</td><td>255</td><td>258.21</td><td>0.1342</td><td>0.1324</td><td>0.2666</td></tr><tr><td>S23: 4312</td><td>215</td><td>264.21</td><td>0.1131</td><td>0.1355</td><td>0.2487</td></tr><tr><td>S17: 3412</td><td>257</td><td>264.21</td><td>0.1352</td><td>0.1355</td><td>0.2708</td></tr><tr><td>Sum</td><td>1900</td><td>1949.00</td><td>1.0000</td><td>1.0000</td><td>2.0000</td></tr></table>

Table 10  
Population after iteration 4

<table><tr><td rowspan="2">Sequence</td><td colspan="2">Actual</td><td colspan="3">Relative</td></tr><tr><td>Makespan</td><td>Anticipation</td><td>Makespan</td><td>Anticipation</td><td>Total</td></tr><tr><td>S01: 1234</td><td>318</td><td>290.33</td><td>0.2017</td><td>0.1786</td><td>0.3804</td></tr><tr><td>S10: 2341</td><td>274</td><td>289.83</td><td>0.1738</td><td>0.1783</td><td>0.3522</td></tr><tr><td>S17: 3412</td><td>257</td><td>271.33</td><td>0.1630</td><td>0.1669</td><td>0.3300</td></tr><tr><td>S24: 4321</td><td>255</td><td>253.83</td><td>0.1618</td><td>0.1562</td><td>0.3180</td></tr><tr><td>S23: 4312</td><td>215</td><td>259.83</td><td>0.1364</td><td>0.1598</td><td>0.2963</td></tr><tr><td>S17: 3412</td><td>257</td><td>259.83</td><td>0.1630</td><td>0.1598</td><td>0.3229</td></tr><tr><td>Sum</td><td>1576</td><td>1625.00</td><td>1.0000</td><td>1.0000</td><td>2.0000</td></tr></table>

Table 11  
Population during iteration 5

<table><tr><td rowspan="2">Sequence</td><td colspan="2">Actual</td><td colspan="3">Relative</td></tr><tr><td>Makespan</td><td>anticipation</td><td>Makespan</td><td>Anticipation</td><td>Total</td></tr><tr><td>S01: 1234</td><td>318</td><td>294.71</td><td>0.1673</td><td>0.1446</td><td>0.3119</td></tr><tr><td>S10: 2341</td><td>274</td><td>308.12</td><td>0.1442</td><td>0.1511</td><td>0.2953</td></tr><tr><td>S17: 3412</td><td>257</td><td>300.75</td><td>0.1352</td><td>0.1475</td><td>0.2828</td></tr><tr><td>S24: 4321</td><td>255</td><td>286.03</td><td>0.1342</td><td>0.1403</td><td>0.2745</td></tr><tr><td>S23: 4312</td><td>215</td><td>286.46</td><td>0.1131</td><td>0.1405</td><td>0.2537</td></tr><tr><td>S17: 3412</td><td>257</td><td>264.21</td><td>0.1352</td><td>0.1296</td><td>0.2649</td></tr><tr><td>S13: 3124</td><td>324</td><td>297.71</td><td>0.1705</td><td>0.1460</td><td>0.3166</td></tr><tr><td>Sum</td><td>1900</td><td>2038.00</td><td>1.0000</td><td>1.0000</td><td>2.0000</td></tr></table>

85 time units, respectively, at station M5. Stations M2 and M4 cannot perform operation O1.

Table 3 displays transportation times between pairs of workstations in the system. For instance, row 4 of table 3 states that the transportation time from station M4 to M1 is 15 time units and from M4 to M2 is 10 time units. There are no transportation facilities from M4 to stations M3 and M5. Table 4 shows the specific operational and operational precedence requirements for 4 jobs labeled 1, 2, 3, and 4. Row 1 of this table indicates that job 1 requires operations O1, O2, and O5 performed in that order. We assume that each job consists of 1 unit of a particular part type. We wish to develop a sequence-dependent schedule for the 4 jobs that meets certain desired criteria as discussed subsequently.

With 4 jobs, there is a total of $4!=24$ possible job sequences, each of which has an associated sequence-dependent schedule. If at all possible, we would like to pick a good sequence-dependent schedule from the 24 possibilities without necessarily seeking the best of these schedules or exhaustively searching the space of 24 schedules. Tables 5–12 depict the search process conducted by the Adaptive DSS. We explain this process in the following paragraphs.

The example is based on the following assumptions. The limit on allowable population size is set at 6 (i.e., the population can contain at most 6 job sequences). The search procedure must last for at least 3 iterations. A best-so-far solution must have persisted for at least 3 consecutive iterations before the process is terminated and it is selected as the solution to the problem.

The initial population contains 3 seed sequences that are randomly picked. These are shown in column 1 of table 5. Each sequence is assigned a unique label. The 3 seed sequences are labeled S01, S10, and S17. S01 refers to the sequence $\langle1,2,3,4\rangle$ , S10 to the sequence $\langle2,3,4,1\rangle$ , and S17 to the sequence $\langle3,4,1,2\rangle$ . The 5 remaining columns in the table have been broadly categorized under two headings: Actual and Relative.

Columns 2 and 4 contain the Actual Makespan and the Relative Makespan values for the sequence-dependent schedules corresponding to each of the three sequences. We used the first of the three methods described in section 5.2 for developing sequence-dependent schedules. That is, all operations of the jth job in a sequence were fully scheduled before the operations of the $(j+1)$ th job were considered. We embedded this rule within a version of the A\* algorithm for optimal schedule generation. Thus, all schedules are the “optimal” sequence-dependent schedules for the kind of sequence dependence described.

By definition, makespan is the largest of the completion times for the various jobs in a job list. The smaller the makespan, the sooner all of the jobs under consideration are completely processed. Minimizing makespan is, therefore, a common objective in many scheduling contexts. Thus, from the perspective of minimizing makespan, sequence S17 is more preferable than S10 which, in turn, is more preferable than S01. The last row in the table contains the sum of the values in each of the columns 2–6. The entry of 849 in this row for column 2 is the sum of the makespan values in that column. Column 4 translates each of the 'raw' makespan values in column 2 to relative proportions with respect to the total makespan of all members currently in the population. Sequence S01, for example, has an actual makespan of 318 and a relative makespan of $318/849 = 0.3745$ .

Columns 3 and 5 in table 5 contain what we refer to as the Actual Anticipation and the Relative Anticipation associated with each sequence. The “anticipation” of a sequence refers to an overall numerical assessment of: (a) the anticipated minimum quality of its next child based on the current members in the population, tempered by: (b) past performance of that sequence based on the actual qualities of all past offspring (i.e., a child or any descendant) of that sequence.

Table 12  
Population after iteration 5

<table><tr><td rowspan="2">Sequence</td><td colspan="2">Actual</td><td colspan="3">Relative</td></tr><tr><td>Makespan</td><td>Anticipation</td><td>Makespan</td><td>Anticipation</td><td>Total</td></tr><tr><td>S01: 1234</td><td>318</td><td>290.33</td><td>0.2017</td><td>0.1693</td><td>0.3711</td></tr><tr><td>S10: 2341</td><td>274</td><td>303.74</td><td>0.1738</td><td>0.1772</td><td>0.3510</td></tr><tr><td>S17: 3412</td><td>257</td><td>296.36</td><td>0.1630</td><td>0.1729</td><td>0.3359</td></tr><tr><td>S24: 4321</td><td>255</td><td>281.65</td><td>0.1618</td><td>0.1643</td><td>0.3261</td></tr><tr><td>S23: 4312</td><td>215</td><td>282.08</td><td>0.1364</td><td>0.1645</td><td>0.3009</td></tr><tr><td>S17: 3412</td><td>257</td><td>259.83</td><td>0.1630</td><td>0.1515</td><td>0.3146</td></tr><tr><td>Sum</td><td>1576</td><td>1714.00</td><td>1.0000</td><td>1.0000</td><td>2.0000</td></tr></table>

Initially, we have no past data available as no offspring have been created as yet. Thus, in table 5 the actual anticipation values are based only on anticipated quality of the next child. Assuming that a member in the population is equally likely to mate with any other member, the actual anticipation value is defined as the average makespan of an offspring based on all possible such unions. Possible unions also include mutation wherein only a single parent is involved. Thus, for sequence S01, the actual anticipation value (shown in column 3) is $\{(318 + 318)/2 + (318 + 274)/2 + (318 + 257)/2\}/3 = 300.5$ . The first member of the summation on the left-hand-side of this equality denotes the anticipated minimum quality of an the offspring if reproduction is via mutation, the second member denotes the anticipation if S01 and S10 unite, and the third member denotes the anticipated result if the union is between S01 and S17.

Column 5 represents the actual anticipations in column 3 as proportions relative to the sum (also 849 in this case) of all anticipation values for sequences in the population. Thus, the relative anticipation for S01 is $300.5/849 = 0.3539$ . Finally, entries in column 6 (entitled Total) are the sums of corresponding entries in the two preceding columns 4 and 5. These values represent the total fitness for each of the sequences in the population. For instance, sequence S01 has a total fitness of $(0.3745 + 0.3539) = 0.7285$ . All other entries in the different columns in table 5 are similarly obtained.

Note that the total fitness value of a sequence is based on 3 measures: The actual makespan corresponding to the sequence, a measure of its past performance in generating good offspring, and an anticipated measure of its performance in generating the next offspring. Since all three measures are related to makespan, the smaller the total fitness the better. From table 5 we see that, based on total fitness, S17 is preferable to S10, which is preferable to S01. The best solution thus far corresponds to sequence S17 with the smallest makespan of 257. We store this result for subsequent reference.

We next consider table 6. Table 6 depicts the scenario following the first iteration of our GA-based scheduler. During each iteration, the following events take place. First, we randomly decide whether the (next) genetic operation involves one parent (i.e., mutation) or two (i.e., some type of crossover). This decision is biased such that mutation is used far less frequently than crossover. Secondly, we generate a separate genetic pool via the reproduction operation. The members of the genetic pool will act as parents in generating offspring sequences. We assume that, at each iteration, we wish to generate just a single new offspring sequence. This pool will have one member if mutation is chosen as the genetic operator and two members, if crossover is chosen. The choice of members is guided by the total (relative) strength values of sequences currently in the population. That is, sequences with a lower total strength (recall, our example is a minimization problem) have a higher likelihood of participating in the genetic pool than sequences with higher total strengths. In our example, the crossover operator is selected at iteration 1. Further, following the above procedure, sequences S10 and S17 are chosen as members of a genetic pool of size 2.

Observe that we assume that only one union takes place in each iteration. Certainly, this need not be the case and an actual implementation would allow multiple unions to occur concurrently. Whenever two parents are involved, we use a type of crossover operation called “subtour chunking”. (We are not presenting details about this operator here. See [9] for a description.) The union of S17 and S10 (via subtour chunking) yields the sequence S15: $\langle3,2,1,4\rangle$ . Table 6 shows that there are now 4 members S01, S10, S17, and S15 in the population. This concludes step two of the iteration.

Thirdly, we assess the goodness of the current population as follows. Using our scheduling algorithm we determine that the sequence-dependent schedule corresponding to S15 has a makespan of 324 (see column 2 of the table). Going back to table 5, recall that one component of the anticipation value for a sequence is the minimum anticipated quality of its next offspring. This anticipation is essentially the average makespan based on all possible unions for that sequence. Thus, for sequence S10, this anticipation is $((274 + 274)/2 + (274 + 318)/2 + (274 + 257)/2)/3 = 278.5$ . However, the actual union that took place (based on total fitness) was between S10 and S17. This particular union has an anticipation of $(274 + 257)/2 = 265.5$ . Thus, the offspring, S15, with a makespan of 324 fell short of this anticipation by $(324 - 265.5) = 58.5$ time units. This ‘poor’ performance of the parents results in the parents as well as all ancestors of these parents being penalized. At this stage of the example the only ancestors of S15 are its parents, S10 and S17. The total penalty of 58.5 is divided equally between both parents. The current actual anticipation values (in table 6) reflect this reward/punishment mechanism. For instance, the actual anticipation value for S10 in table 6 is computed as

$$
\begin{array}{l} \left\{(2 7 4 + 2 7 4) / 2 + (2 7 4 + 3 1 8) / 2 \right. \\ \left. + (2 7 4 + 2 5 7) / 2 + (2 7 4 + 3 2 4) / 2 \right\} / 4 \\ \left. + 5 8. 5 / 2 \right. \\ = 2 8 3. 6 2 5 + 2 9. 2 5 = 3 1 2. 8 7 5. \end{array}
$$

Sequence S17's actual anticipation value also has a penalty of 29.25 attached. S01 and S15, however, have no such reward or penalty as yet. The remaining columns in table 6 are computed as they were in table 5. After iteration 1, the best solution still remains the same (i.e., a makespan of 257 corresponding to S17). The procedure continues iteratively in the manner just described. We highlight a few noteworthy aspects of the solution below:

(1) At iteration 3, the best solution corresponds to sequence S23 with a makespan of 215. The same solution persists over the next two iterations. Thus, based on our assumed stopping criteria, the process terminates after 5 iterations and returns S23 (with an associated schedule having a makespan of 215) as the best solution.

(2) In all iterations except at iteration 4, offspring were created using subtour-chunking crossover on the two selected individuals. At iteration 4, mutation was performed on the selected sequence to generate an offspring.

(3) As we progress through the various iterations, reward/punishment is propagated amongst several levels of ancestors. For example, at iteration 3 (see tables 7 and 8) S17 and S24 produce S23. The anticipated quality of the union is $(257 +$

255)/2 = 256. The actual makespan of S23 is 215. The penalty is thus 215 - 256 = -41 (i.e., actually a reward). This penalty is propagated amongst S23's ancestors in the following fashion. S23 has two parents and hence, the penalty is first divided in half. Parent S17 has no ancestors and gets to keep all of its share (i.e., -41/2 = -20.5). Parent S24 has S10 and S17 as its parents. S24 keeps only half of its penalty (i.e., -41/4 = -10.25). The remainder is to be shared between its parents and any other ancestors. S10 and S17 have no ancestors and hence the remaining penalty is shared equally between them (i.e., each obtains -41/8 = -5.125). At the end of the propagation process, S10, accumulates a total penalty of -5.125, S17 accumulates a penalty of -(20.5 + 5.125) = -25.625, and S24 a penalty of -10.25. The actual anticipation values for S10, S17, and S24 reflect these rewards as well.

(4) Iterations 4 and 5 are both depicted using two tables each. Tables 9 and 10 pertain to iteration 4, and tables 11 and 12 pertain to iteration 5. Recall that we had set the population limit at 6. At the end of iteration 3 (table 8), the population has 6 members. During iteration 4, another instance of sequence S17 was created through mutation of S23. As the population size is at its limit, we need to determine which of the 7 individuals (i.e., the 6 existing sequences plus the new offspring) belong in the population and which individual must be purged. Temporarily, the new offspring S17 is placed in the population (as shown in table 9). The total fitness values for all 7 members are computed. The weakest member, S15, is eliminated. The population now contains S01, S10, S17(old), S24, S23, and S17(new). All measures must be reassessed for the new population of 6 members. These reassessments are shown in table 10. Similar observations apply to iteration 5.

(5) In this particular example the impact of repeated reward/penalty propagations begin to be felt at iteration 5. In table 12, if we were to pick parents based on actual makespan values alone, sequences S23 and S24 with makespans of 215 and 255, respectively, would be the most probable members of the genetic pool. But based on total fitness values, S23 and S17(new) are more likely to be chosen for procreation at the next iteration, if any.

(6) It is worthwhile examining the dynamic nature of the underlying (implicit) set of reasoning rules and the fitness values associated with these rules. For example, after iteration 2 (see table 7) the population contains 5 sequences, namely, S01, S10, S17, S15, and S24. The system implicitly constructs meta-level reasoning rules of the form “ $S_{a} \rightarrow Q_{a}$ ( $f_{a}$ )” as described in the preceding section), one for each member of the current population.

There are 5 such meta rules after iteration 2: S01 → 301.8 (0.4271), S10 → 279.8 (0.3977), S17 → 271.3 (0.3800), S15 → 304.8 (0.4333), and S24 → 270.3 (0.3617). The consequent of a rule corresponding to a sequence is the average makespan of an offspring based on all possible unions for the corresponding sequence. For instance, in S24 → 270.3 (0.3617), the right-hand side value is $\{(255 + 318)/2 + (255 + 274)/2 + (255 + 257)/2 + (255 + 324)/2 + (255 + 255)/2\}/5 = 1351.5/5 = 270.3$ . (These quantities may also be obtained from the Actual Anticipation values shown in column 3 of table 7 by subtracting out any rewards/penalties accrued by the sequences. Based on prior iterations, sequences S01, S15, and S24 have accumulated no rewards or penalties. Both S10 and S17 have accumulated a net penalty of 24 each.) The rule fitness values are directly obtained from column 6 (i.e., Relative Total) of the table.

Each meta rule $S_{\mathrm{a}} \rightarrow Q_{\mathrm{a}}(f_{\mathrm{a}})$ , is essentially an aggregation of a set of more detailed reasoning rules $\{S_{\mathrm{a}} + S_{\mathrm{b}} \rightarrow Q_{\mathrm{ab}}(f_{\mathrm{ab}})\}$ , corresponding to the different unions that $S_{a}$ could participate in. Thus, the meta rule $S24 \rightarrow 270.3(0.3617)$ is an aggregation of the following set of 5 rules:

$$
S 2 4 + S 0 1 \rightarrow 2 8 6. 5 \quad (0. 0 7 6 7 + 0. 0 8 1 1 = 0. 1 5 7 8);
$$

$$
S 2 4 + S 1 0 \rightarrow 2 6 4. 5 \quad (0. 0 7 0 8 + 0. 0 7 5 2 = 0. 1 4 6);
$$

$$
S 2 4 + S 1 7 \rightarrow 2 5 6 \quad (0. 0 6 8 5 + 0. 0 7 1 7 = 0. 1 4 0 2);
$$

$$
S 2 4 + S 1 5 \rightarrow 2 8 9. 5 \quad (0. 0 7 7 5 + 0. 0 8 2 3 = 0. 1 5 9 8);
$$

$$
S 2 4 + S 2 4 \rightarrow 2 5 5 \quad (0. 0 6 8 2 + 0. 0 6 8 2 = 0. 1 3 6 4).
$$

The first 4 rules in this set correspond to the crossover operator and the last rule embodies mutation. The consequent for a detailed rule is the average makespan of the two parents involved in the union. Thus the consequent of 286.5 for $S24 + S01 \rightarrow 286.5$ (0.1578) is nothing but $(255 + 318)/2$ . Each detailed rule can be associated with two meta rules, one corresponding to each parent involved in the detailed rule. The fitness value for each detailed rule is obtained from the fitness of the associated parents in the following manner. Consider $S24 + S01 \rightarrow 286.5$ ( $0.0767 + 0.0811 = 0.1578$ ). Here, $0.0767 = (286.5 / 1351.5) \times 0.3617$ and $0.0811 = (286.5 / 1509) \times 0.4271$ . Thus, the total fitness of $S24 + S01 \rightarrow 286.5$ is 0.1578. Essentially, the fitness value of a meta rule is divided amongst its associated detailed rules by taking into account the contribution of the consequent of each detailed rule to the consequent of the meta rule.

During iteration 3, because the system chose crossover over mutation, the two selected rules, $S24 \rightarrow 270.3$ (0.3617) and $S17 \rightarrow 271.3$ (0.3800), are “fired” resulting in the addition of S23 (see table 8). It is easily verified that the rule $S24 + S17 \rightarrow 256$ (0.1402) is the fittest of all detailed rules pertaining to crossover in the entire detailed rule set. With the addition of S23, our meta-rule set now contains 6 rules and the detailed rule set contains 21 rules (i.e., 6 new rules are added to reflect the possible unions between existing members and the newcomer to the population). As before the fitnesses for the meta rules and detailed rules may be obtained from the data contained in table 8. The process continues in this fashion until termination.

In closing, we make the following general observations. The best-thus-far makespan of 215 also happens to be the best solution that we would have obtained had we exhaustively evaluated all 24 sequences. The average makespan of the seed population consisting of the sequences S01, S10, and S17 is $(318 + 274 + 257)/3 = 283$ . Our solution represents a 24% reduction in makespan on comparison with this average and a 16% improvement in comparison with the best of the seeds, namely S17. The true optimal solution to the problem (i.e., had we not restricted our search to sequence-dependent schedules only) could be better than 215. However, determining this optimum is no trivial task even for this relatively small problem. In general, performance evaluation would not be based on a single instance due to the random factors involved (i.e., selection of seeds, limit on population size, selection of operators, and the behavior of operators themselves). More robust evaluations of the proposed approach using our prototype implementation is underway. These results will be reported subsequently.

## 6. Concluding remarks

In this paper, we examine existing DSS paradigms from the perspective of learning by problem processors. DSS implementations that subscribe to these paradigms have employed supervised learning techniques for acquiring all of their problem processing knowledge (PPK). Techniques employed to date include rote learning, instructional learning, deductive learning, and various supervised induction methods. All of these approaches imply reliance upon the external environment by the system to varying degrees depending on the specific strategies used. We propose a new paradigm called Adaptive DSSs whose problem processors are endowed with some form of unsupervised inductive learning abilities in addition to other forms of learning to assist with acquiring PPK. Adaptive DSSs are, to some extent, self teaching systems. Therefore, overall, an Adaptive DSS entails less dependence on external agents than systems based on current paradigms. Relative to DSSs of the past, Adaptive DSSs may well be more efficient and effective in solving problems in complex and/or dynamic domains, where predefinition of PPK is impossible and/or undesirable.

We examine one such domain, the domain of problems involving the (static) scheduling of jobs in FMSs, and present an overview of the architecture for an Adaptive DSS in this context. We demonstrate the learning process of the system using an example problem instance. A prototype version of the Adaptive DSS described here is being implemented using the C programming language on a 24-processor Sequent Symmetry computer (running a version of the Unix operating system). This implementation will enable us to explore in detail the performance of our system via structured experimentation. These and investigations in other application domains should help further develop the Adaptive DSS concept.

## Acknowledgement

Dr. R. Pakath's participation in this research was made possible in part by a Summer Research Grant from the College of Business and Economics of the University of Kentucky. The grant was made possible by a donation of funds to the College by Ashland Oil, Inc.

Appendix A: An overview of genetic algorithms and their applications

Holland [27] devised the genetic algorithm (GA) as a means to realizing learning through observation and discovery. The algorithm rests on the observation that a combination of sexual reproduction and natural selection allows nature to develop living species that are highly adapted to their environment. The method operates on a population of fixed size (N) and iteratively performs three steps, namely: (1) evaluate the fitness of the individuals in the population; (2) select individuals according to their fitness to populate a genetic pool of size N; and (3) use various kinds of genetic operators on the genetic pool to construct a new population of size N. This process of learning and discovery continues until some prespecified stopping criteria is met. At this point, the population consists of a set of 'highly fit' individuals. There are three basic kinds of genetic operators for use in step 3, namely, reproduction, crossover, and mutation. Reproduction and crossover are the most frequently used with mutation being resorted to only relatively rarely. Numerous forms of the crossover operator have been identified including partially-mapped, position-based, order-based, and edge-recombination crossovers. The choice of operators for a given problem and the frequency with which each operator is used is usually problem-dependent

GAs have been incorporated as part of two kinds of systems, Learning System 1 (LS1) [63] and Classifier Systems [5,18,28]. Both systems are called rule discovery systems. They use the GA to facilitate the discovery of new rules to populate a rule set. The systems differ in their rule representation schemes and in their approaches to fitness evaluation. Liepins and Hilliard [42] discuss several illustrative GA applications in different domains: Image registration [20], surveillance [39], network configuration [10,11,12], gas and oil pipeline operations [17,19]. Fairly comprehensive bibliographies on GA research may be found in [18,35].

## References

[1] S.L. Alter, Decision Support Systems: Current Practices and Continuing Challenges (Addison-Wesley, MA, 1980).

[2] M. Binbasioglu and M. Jarke, Domain Specific Tools for

Knowledge-Based Model Building, Decision Support Systems 2 (1986) 213–223.

[3] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Future Directions for Developing Decision Support Systems, Decision Sciences (1980) 616–631.

[4] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems (Academic Press, New York, 1981).

[5] L.B. Booker, D.E. Goldberg and J.H. Holland, Classifier Systems and Genetic Algorithms, Artificial Intelligence 40 (1989) 235–282.

[6] G. Bruno, A. Elia and P. Laface, A Rule-Based System to Schedule Production, IEEE Computer (July 1986) 32–39.

[7] W.I. Bullers, S.Y. Nof and A.B. Whinston, Artificial Intelligence in Manufacturing Planning and Control, AIIE Transactions (Dec. 1980) 351–363.

[8] J.G. Carbonell, R.S. Michalski and T.M. Mitchell, An Overview of Machine Learning, in: R.S. Michalski, J.G. Carbonell, T.M. Mitchell, Eds., Machine Learning: An Artificial Intelligence Approach, Vol. 1 (Morgan Kaufmann, San Mateo, CA, 1983).

[9] G.A. Cleveland and S.F. Smith, Using Genetic Algorithms to Schedule Flow Shop Releases, Proceedings of the Third International Conference on Genetic Algorithms (1989) 160–169.

[10] S. Coombs and L. Davis, Genetic Algorithms and Communication Link Speed Design: Constraints and Operators, Genetic Algorithms and Their Applications, Proceedings of the Second International Conference on Genetic Algorithms (1987) 257–260.

[11] L. Davis and S. Coombs, Genetic Algorithms and Communication Link Speed Design: Theoretical Considerations, Genetic Algorithms and Their Applications, Proceedings of the Second International Conference on Genetic Algorithms (1987) 252–256.

[12] L. Davis and S. Coombs, Optimizing Network Link Sizes with Genetic Algorithms, in: M.S. Elzas, T.I. Oren and B.P. Zeigler, Eds., Modelling and Simulation Methodology: Knowledge Systems Paradigms (North-Holland, Amsterdam, 1989).

[13] S. De, A Knowledge-Based Approach to Scheduling in an FMS, Annals of Operations Research 12 (1988) 109-134.

[14] S. De and A. Lee, FMS Scheduling Using Beam Search, Journal of Intelligent Manufacturing 1 (1990) 165–183.

[15] D.R. Dolk and D.J. Kridel, Toward a Symbiotic Expert System for Econometric Modeling, Proceedings of the 22nd Hawaii International Conference on Systems Sciences 3 (1989) 3–13.

[16] B.L. Dos Santos and C.W. Holsapple, A Framework for Designing Adaptive DSS Interfaces, Decision Support Systems 5 (1989) 1–11.

[17] D.E. Goldberg, Computer-Aided Gas Pipeline Operation Using Genetic Algorithms and Rule Learning, Ph.D. Thesis, (College of Engineering, University of Alabama, 1983).

[19] D.E. Goldberg, Genetic Algorithms in Search, Optimization and Machine Learning (Addison-Wesley, MA, 1989).

[18] D.E. Goldberg and C.H. Kuo, Genetic Algorithms in

Pipeline Optimization, Journal of Computing in Civil Engineering 1 (1987) 128–141.

[20] J.J. Grefenstette and J.M. Fitzpatrick, Genetic Search with Approximate Function Evaluations, Proceedings of an International Conference on Genetic Algorithms and Their Applications (1985) 112–120.

[21] J.H. Griesmer, S.J. Hong, M. Karnaugh, J.K. Kastner, M.I. Schor, R.L. Enis, D.A. Klein, K.R. Milliken and H.M. Van Woerkom, YES/MVS: A Continuous Real Time Expert System, Proceedings of the American Association of Artificial Intelligence (1984).

[22] M.R. Hilliard, G.E. Liepins and M. Palmer, Machine Learning Applications to Job Shop Scheduling, Proceedings of the First International Conference on Industrial and Engineering Applications of Artificial Intelligence and Expert Systems (1988) 723–733.

[23] M.R. Hilliard, G.E. Liepins and M. Palmer, Discovering and Refining Algorithms Through Machine Learning, in: D. Brown and C. White, Eds., OR/AI: The Integration of Problem Solving Strategies.

[24] M.R. Hilliard, G.E. Liepins, M. Palmer, M. Morrow and J. Richardson, A Classifier-Based System for Discovering Scheduling Heuristics, Proceedings of the Second International Conference on Genetic Algorithms and Their Applications (1987) 231–235.

[25] M.R. Hilliard, G.E. Liepins, M. Palmer and G. Rangarajan, The Computer as a Partner in Algorithmic Design: Automated Discovery of Parameters for a Multi-Objective Scheduling Heuristic, in: R. Sharda, B. Golden, E. Wasil, O. Balci and W. Stewart, Eds., Impacts of Recent Computer Advances on Operations Research (North-Holland, New York, 1989).

[26] M.R. Hilliard, G. Liepins, G. Rangarajan and M. Palmer, Learning Decision Rules for Scheduling Problems: A Classifier Hybrid Approach, Proceedings of the Sixth International Conference on Machine Learning (1989) 188–200.

[27] J.H. Holland, Adaptation in Natural and Artificial Systems (The University of Michigan Press, Ann Arbor, MI, 1975).

[28] J.H. Holland and J.S. Reitman, Cognitive Systems Based on Adaptive Algorithms, in: D.A. Waterman and F. Hayes-Roth, Eds., Pattern Directed Inference Systems (Academic Press, New York, 1978).

[29] C.W. Holsapple and A.B. Whinston, Management Support Through Artificial Intelligence, Human Systems Management 5 (1985) 163–171.

[30] C.W. Holsapple and A.B. Whinston, Manager's Guide to Expert Systems (Dow Jones–Irwin, Homewood, IL, 1986).

[31] C.W. Holsapple and A.B. Whinston, Knowledge-Based Organizations, The Information Society 5 (1987) 77–90.

[32] S. Hwang, Automatic Model Building Systems: A Survey, Proceedings of the 1985 DSS Conference (1985) 22–32.

[33] V.S. Jacob and H. Pirkul, A Framework for Networked Knowledge-Based Systems, IEEE Transactions on Systems, Man and Cybernetics 20 (1990) 119–127.

[34] V.S. Jacob, R. Pakath and J.S. Zaveri, Adaptive Decision Support Systems: Incorporating Learning Into Decision Support Systems, Proceedings of the 1990 ISDSS Conference (1990) 313–330.

[35] Y. Kodratoff and R.S. Michalski, Machine Learning: An Artificial Intelligence Approach, Vol. 3 (Morgan Kaufmann, San Mateo, CA, 1990).

[36] R. Krishnan, PDM: A Knowledge-Based Tool for Model Construction Proceedings of the 21st Hawaii International Conference on Systems Sciences 3 (1988).

[37] R. Krishnan, Automated Model Construction: A Logic-Based Approach, Annals of Operations Research, Special Issue on Linkages with Artificial Intelligence (1988).

[38] R. Krishnan, A Logic Modeling Language for Automated Model Construction, Decision Support Systems 6 (1990) 123–152.

[39] M.J. Kuchinski, Battle Management Systems Control Rule Optimization Using Artificial Intelligence, Technical Report No. NSWC MP 84-329 (Naval Surface Weapons Center, Dahlgren, VA, 1985).

[40] A. Kusiak, Designing Expert Systems for Scheduling of Automated Manufacturing, Industrial Engineering 19 (1987) 42–46.

[41] T. Liang and B.R. Konsynski, Modeling by Analogy: Use of Analogical Reasoning in Model Management Systems, Proceedings of the 1990 ISDSS Conference (1990) 405–421.

[42] G.E. Liepins and M.R. Hilliard, Genetic Algorithms: Foundations and Applications, Annals of Operations Research 21 (1989) 31–58.

[43] P. Ma, F.H. Murphy and E.A. Stohr, A Graphics Interface for Linear Programming, Communications of the ACM 32 (1989) 996–1012.

[44] M.L. Manheim, Issues in Design of a Symbiotic DSS, Proceedings of the 22nd Hawaii International Conference on Systems Sciences 3 (1989) 14–23.

[45] M.L. Manheim, S. Srivastava, N. Vlahos, J. Hsu and P. Jones, A Symbiotic DSS for Production Planning and Scheduling: Issues and Approaches, Proceedings of the 22nd Hawaii International Conference on Systems Sciences 3 (1990) 383–390.

[46] R.S. Michalski, Understanding the Nature of Learning: Issues and Research Directions, in: R.S. Michalski, J.G. Carbonell and T.M. Mitchell, Eds., Machine Learning: An Artificial Intelligence Approach, Vol. 2 (Morgan Kaufmann, San Mateo, CA, 1986).

[47] R.S. Michalski and Y. Kodratoff, Research in Machine Learning: Recent Progress, Classification of Methods and Future Directions, in: Y. Kodratoff and R.S. Michalski, Eds., Machine Learning: An Artificial Intelligence Approach, Vol. 3 (Morgan Kaufmann, San Mateo, CA, 1990).

[48] R.S. Michalski, J.G. Carbonell and T.M. Mitchell, Machine Learning. An Artificial Intelligence Approach, Vol. 1 (Morgan Kaufmann, San Mateo, CA, 1983).

[49] R.S. Michalski, J.G. Carbonell and T.M. Mitchell, Machine Learning: An Artificial Intelligence Approach, Vol. 2 (Morgan Kaufmann, San Mateo, CA, 1986).

[50] F. Mili, Dynamic View of Decision Domains for the Design of Active DSS, Proceedings of the 22nd Hawaii International Conference on Systems Sciences 3 (1989) 24–32.

[51] W.A. Muhanna and R.A. Pick, Composite Models in SYMMS, Proceedings of the 21st Hawaii International Conference on Systems Sciences 3 (1988) 418–427.

[52] F.H. Murphy and E.A. Stohr, An Intelligent System for Formulating Linear Programs, Decision Support Systems 2 (1986) 39–47.

[53] S.A. Raghavan and D.R. Chand, Exploring Active Decision Support: The JANUS Project, Proceedings of the 22nd Hawaii International Conference on Systems Sciences 3 (1989) 33–45.

[54] T.L. Saaty, The Analytical Hierarchy Process (McGraw Hill, New York, 1980).

[55] J.W. Shavlik and T.G. Dietterich, Readings in Machine Learning (Morgan Kaufmann, San Mateo, CA, 1990).

[56] M.J. Shaw, Knowledge-Based Scheduling in Flexible Manufacturing Systems: An Integration of Pattern-Directed Inference and Heuristic Search, International Journal of Production Research 26 (1988) 821–844.

[57] M.J. Shaw, A Pattern-Directed Approach to FMS Scheduling, Annals of Operations Research 15 (1988) 353–376.

[58] M.J. Shaw and A.B. Whinston, An Artificial Intelligence Approach to the Scheduling of Flexible Manufacturing Systems, IIE Transactions 21 (1989) 170–183.

[59] M.J. Shaw, S.C. Park and N. Raman, Intelligent Scheduling with Machine Learning Capabilities: The Induction of Scheduling Knowledge, IIE Transactions 24 (1992) 156–168.

[60] M.J. Shaw, P. Tu and P. De, Applying Machine Learning to Model Management in Decision Support Systems, Decision Support Systems 4 (1988) 285–305.

[61] S. Shen and Y. Chang, Schedule Generation in a Flexible Manufacturing System: A Knowledge-Based Approach, Decision Support Systems 4 (1988) 157–166.

[62] H.A. Simon, Why Should Machines Learn?, in: R.S. Michalski, J.G. Carbonell and T.M. Mitchell, Eds., Machine Learning: An Artificial Intelligence Approach, Vol. 1 (Morgan Kaufmann, San Mateo, CA, 1983).

[63] S.F. Smith, A Learning System Based on Genetic Adaptive Algorithms, Ph.D. Thesis (Department of Computer Science, University of Pittsburgh, Pittsburgh, PA, 1980).

[64] S. Subramanyam and R.G. Askin, An Expert Systems Approach to Scheduling in Flexible Manufacturing Systems, in: A. Kusiak, Ed., Flexible Manufacturing Systems: Methods and Studies (North-Holland, Amsterdam, 1986).

[65] G. Syswerda, Schedule Optimization Using Genetic Algorithms, in: L. Davis, Ed., The Genetic Algorithms Handbook (1991) (Von Nostrand Reinhold, New York).

[66] P.E. Taylor and S.J. Huxley, A Break from Tradition for the San Francisco Police: Patrol Officer Scheduling Using an Optimization-Based Decision Support System, Interfaces 19 (1989) 4–24.

[67] E. Turban and P.R. Watkins, Integrating Expert Systems and Decision Support Systems, MIS Quarterly 10 (1986) 121–136.

[68] D. Whitley, T. Starkweather and D. Fuquay, Scheduling Problems and Traveling Salesmen: The Genetic Edge Recombination Operator, Proceedings of the Third International Conference on Genetic Algorithms and Their Applications (1989) 133–140.
