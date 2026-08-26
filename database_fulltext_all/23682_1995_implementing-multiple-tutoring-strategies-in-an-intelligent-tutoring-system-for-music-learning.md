---
otero_id: 23682
otero_key: "JEPYHWKY"
title: "Implementing multiple tutoring strategies in an intelligent tutoring system for music learning"
authors: "Marios C Angelides; Amelia K Y Tong"
year: "1995"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1995.7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Implementing multiple tutoring strategies in an intelligent tutoring system for music learning

MARIOS C. ANGELIDES and AMELIA K.Y. TONG

Information Systems Department, London School of Economics and Political Science, London WC2A 2AE, UK

Variation in tutoring strategies plays an important part in intelligent tutoring systems. The potential for providing an adaptive intelligent tutoring system depends on having a range of tutoring strategies to select from. In order to react effectively to the student's needs, an intelligent tutoring system has to be able to choose intelligently among the strategies and determine which strategy is best for an individual student at a particular moment. This paper describes, through the discussion pertaining to the implementation of SONATA, a music theory tutoring system, how an intelligent tutoring system can be developed to support multiple tutoring strategies during the course of interaction. SONATA has been implemented using a hypertext tool, HyperCard II.1.

## Introduction

Intelligent tutoring systems (ITSs) facilitate the provision of a one to one tuition between student and teacher. For an intelligent tutoring system to offer a valuable educational experience on this individualized basis, it must be able to adjust its tutoring style to the student's changing needs. Variation in tutoring strategies is fundamental in this respect, as tutoring strategies are the means through which the tutor imparts tutorial material to the student. The purpose of this paper is through the discussion pertaining to the development of SONATA, to illustrate how an intelligent tutoring system can switch from one strategy to another by incorporating the agents responsible for helping the system to make the 'switch' decision. SONATA was developed using the hypertext approach (Angelides and Gibson, 1993). This involves decomposing and storing logically the different types of knowledge required in SONATA as a collection of 'cards' and setting up links to integrate the stored information together in a desired manner.

SONATA is an intelligent tutoring system aimed at primary level music students. The assumption underlying the use of the system is that the user does not possess any prior knowledge of music theory. The system treats every new student as an absolute beginner. It aims to assist students with their learning of music theory, by providing guidance as well as assessment to the student within the knowledge domain. The long-term goal of SONATA is to contribute towards a teaching environment an intelligent tutoring system which offers multiple tutoring resources, enabling tutorial material to be presented from alternative teaching viewpoints.

The paper first gives an overview of intelligent tutoring systems, including discussions about current practices with tutoring strategies and intelligent tutoring systems for music learning. It then presents the development approach used to implement SONATA, followed by a full description of SONATA's architecture, functionality and the mechanisms it deploys in making its strategy-selection decisions.

## Intelligent tutoring systems (ITSs)

For a tutoring system to be classified as intelligent, it must pass three tests of intelligence (Angelides and Doukidis, 1990). First, the system must know the subject matter well enough to be able to draw inferences or solve problems in the domain of application. Second, it must be able to deduce a user-learner's approximation of the domain knowledge. Third, the tutorial strategy must allow the system to implement strategies that reduce the difference between the expert and the student performance. Therefore, at the foundation of an ITS one expects to find three special kinds of knowledge: domain, student and tutoring knowledge.

The first key place for intelligence in an ITS is in the knowledge that the system has of its subject domain (Anderson, 1988). There are three approaches to encoding knowledge into the domain model which gives rise to the three different types of domain models. The first approach, which gives rise to a black box model of the domain knowledge, involves finding a method of reasoning about the domain that does not actually require codification of the knowledge. A black box model generates the correct input–output behaviour over a range of tasks and so can be used as a judge of correctness. However, the internal computations by which it provides this behaviour are either not available or are of no use in delivering instruction. Such a domain model can be used in a reactive tutor that tells the students whether they are right or wrong and possibly what the right move would be. This is known as surface-level tutoring. The second approach, which gives rise to a glass box model of the domain knowledge, involves reasoning about the domain by applying codified knowledge. A glass box model is the standard knowledge-based systems approach to reasoning with knowledge. Because of its nature, the emerging system should be more amenable to tutoring than a black box model because a major component of this expert system is an articulate representation of the domain knowledge. The third approach, which gives rise to a cognitive model of the domain knowledge, involves making the domain model a computer simulation of human problem solving in the domain of application.

The second key place for intelligence in an ITS is in the knowledge that the system infers of its student (VanLehn, 1988). An ITS diagnoses a student's current knowledge of the subject matter and uses this to individualize instruction according to the student's needs. The ITS component that holds the student's current knowledge is the student model. The input for diagnosis is garnered through the interaction with the student. The output of diagnosis depends on the use of the student model. Nevertheless, it should reflect the student's current knowledge state. Common uses for the student model include advancing the user to the next curriculum topic, offering unsolicited advice when the student needs it, generating new problems and adapting explanations by using concepts that the student understands. A student model usually consists of three kinds of information: bandwidth (i.e. quality and amount of student input), the type of domain knowledge (i.e. declarative, procedural or causal) and differences between the student and domain models in terms of missing conceptions (i.e. as an overlay model) and misconceptions (i.e. as a list of bugs).

The third key place for intelligence in an ITS is in the principles by which it tutors students and in the methods by which it applies these principles (Halff, 1988). Tutor models may incorporate many different instructional techniques. A tutor model must exhibit three characteristics.

(1) It must exercise some control over curriculum, that is, the selection and sequencing of material to be presented to the student and some control over instruction, that is the process of the actual presentation of that material to the student.

(2) It must be able to respond to student's questions about the subject matter.

(3) It must be able to determine when students need help in the course of practising a skill and what sort of help is needed.

Some tutors are primarily concerned with teaching factual knowledge and inferential skills. These are the expository tutors. Some tutors are primarily concerned with teaching skills and procedures that manipulate factual knowledge. These are the procedural tutors. The curriculum can be broken down into formulating a representation of the material in the domain model and selecting and sequencing concepts from that representation. A tutor model must also incorporate some form of propaedeutics, that is, knowledge which is needed for enabling learning but not for achieving proficient performance. The underlying assumption is that skilled performance will be achieved only with practice. As a result, propaedeutics serve, firstly, to relate theory to practice, secondly, to justify, explain and test possible problem solutions, thirdly, as a stepping-stone to more efficient problem-solving strategies and, fourthly, as strategies for management of the working memory during intermediate stages of learning. Curricula serve several functions.

(1) They divide the material to be learned into manageable units which should address at most a small number of instructional goals and should present material that will allow students to master them.

(2) They sequence the material in a way that conveys its structure to students.

(3) They ensure that the instructional goals presented in each unit are achievable.

(4) They enable the tutor model to evaluate the student reaction to instruction on a moment-to-moment basis and reformulation of the curriculum.

## Tutoring strategies currently in use

Some of the common tutoring strategies currently in use include apprenticeship, successive refinement, learning through exploration, practice and Socratic diagnosis.

Apprenticeship is an approach most often used by experts to teach skills in a craft. The expert demonstrates a skill with associated verbal explanation. The apprentice watches the tutor in action and asks questions. As time passes by, the apprentice is allowed to perform small parts of the whole tasks and eventually the whole task in question. This technique may operate beyond the level of manual skill acquisition, as the same principle applies on processes such as problem solving and reasoning. A tutor using this approach must be able to reason meaningfully with the student. In terms of ITS, this strategy requires the system to have a glass box domain model. SOPHIE (Brown et al., 1975) is an ITS which employs the apprentice strategy. It tutors trouble-shooting of electric circuits. SOPHIE mimics the human expert and apprentice relationship by providing a simulated laboratory in which the student is given a demonstration of how a task should be done by a trouble-shooting expert. The student's first activity is to watch the expert locate a fault. Once the expert succeeds in locating a faulty function block, the student is given a chance to locate the particular faulty component within that block.

Successive refinement is often used in cases where the tutorial material contains a substantial amount of detail. A tutor using this approach addresses the domain primarily at a global level, by telling a consistent story but omitting the details. Increasing levels of details are presented as the student progresses. A tutor using this technique may have to constantly make justification for the untrue simplicity about the domain which the student has previously established and to actively support the reconstruction of the mental model of the domain within the student. STEAMER (Hollan et al., 1981) is an ITS which employs this approach. It is used to train engineers to operate complex steam propulsion plants in large ships. STEAMER uses the successive refinement approach by initially presenting a top-level view of the steam plant. As the student progresses, more sophisticated materials are tutored. This is achieved through a hierarchical decomposition of the domain which allows the student to explore subsystems in increasing levels of detail.

Learning through exploration involves putting a pupil in a situation where he or she is allowed to act freely and to explore and discover new material for him/herself. The tutor employing this approach has to be responsible for selecting an area which is new to the student for him/her to explore, setting up an appropriate environment in which the learning can take place and monitoring the student's activities, so as to be able to provide guidance to the student when requested or when the student is in difficulty. WUSOR (Goldstein and Carr, 1977) is an ITS which uses this strategy. It is responsible for instructing the student on how to play the computer game WUMPUS (Goldstein, 1982). WUSOR uses instructional games to tutor the student, focusing on the role the student creates for him/herself by playing the game, thus enhancing the student's own learning environment. There is often no direct knowledge being conveyed to the student. The learning material is disguised as elements of the game, making learning both challenging and more entertaining.

Practice is another strategy that is commonly used. A tutor employing this approach generates practice problems, monitors the student's practice activities and gives feedback. The value of practice activities lies in the stimulation they offer to the student in acquiring new knowledge and, more importantly, in the application of the knowledge the student has acquired. The Lisp Tutor (Anderson and Reiser, 1985) is an ITS which employs the practice approach. It is a tutoring system for Lisp programming. The system is strongly directed towards recurrent skills and it provides a lot of practice in the basic skills. It has a structured editor and gives on-line help.

The system offers a variation in the practice exercises, allows the student to make errors and gives explanation about errors on request.

Socratic diagnosis is seen as a strategy employed in many ITSs. In its broadest terms, Socratic diagnosis is an approach which incorporates some form of 'Socratic dialogue'. This involves a question and answer sequence directed towards uncovering the underlying misconceptions of the student. In a stricter sense, this technique requires the tutor to firstly detect the misconception of the student about the domain and then make the pupil realize that there is an error in their knowledge about the domain through a series of educational interactions. The strategy employed in WHY (Stevens et al., 1982) is commonly described as Socratic – when the student makes a mistake at a level involving some concept the tutor will switch to a sequence of questions regarding subconcepts of the erroneous concept. If the student makes an error with one of them, it is further broken into its constituent concepts in turn. The major difference of this strategy from true Socratic tutoring is that instead of diagnosing each of the misconceptions first, the strategy used in WHY is using the remedial action as diagnostic action for the next misconception.

## ITSs for music learning

Our research results in the field of music education show that while some basic computer-based approaches may have been used to assist music learning, tutoring systems classified as ‘intelligent’ which are designed for music learning are immensely scarce. Most of the existing computer-based systems for music learning encourage students to explore and to be creative in music learning, but seldom record or monitor the student’s progress and diagnose individual’s misconceptions.

MC (Holland and Elsom-cook, 1990), which stands for music composition, is a knowledge-based tutoring system which is still under development. This system aims to help novices explore musical ideas through experiments in music composition. It is intended to aid amateur musicians, in an informal setting, to acquire musical knowledge and skills with direct application. The framework suggested in MC involves linking the knowledge-based tutor to one or more ‘musical microworlds’. The microworlds together form the ‘environment’ within which the student is attempting to learn. These microworlds can be used together as free learning or as a tool for composition. The knowledge-based tutor provides a source of guidance and a means of establishing interrelationships between the microworlds.

## The hypertext approach

SONATA has been developed using a hypertext tool.

Hypertext is the organization of information into information nodes and links (Nielsen, 1990a). Information nodes are linked via information links either sequentially, hierarchically or mixed (Nielsen, 1990b). The main component of any hypertext system is the stack. A stack is a collection of related cards of information which are seen to logically belong together (Shneiderman and Kearsley, 1989). These cards depict the information nodes. The link is the core of all hypertext systems (Smeaton, 1991). With a hypertext framework for specifying an ITS, the domain, tutoring and student knowledge must first be organized into one or more stacks. Secondly, links will be installed to integrate the stored knowledge, not only within but also between individual knowledge models.

All the knowledge of SONATA is incorporated in one stack only. The purpose of this design is to shorten the on-line response time of the system, as it takes longer to cross-reference across different stacks. A card may be linked to other cards with which it has a class-instance relationship. This establishes a semantic network of cards which are organized hierarchically so that properties can be inherited from generic cards to cards lower in the hierarchy (Marchionini and Shneiderman, 1988). Links will be set up as 'organizational' hypertext information links to connect a parent card with its children and thus establish a hierarchical tree in this hypertext network. Cards can be linked to other cards with which they are not hierarchically related via 'referential' hypertext information links, thus establishing a non-hierarchical structure in this network (Begeman and Conklin, 1988). Any information related to a card which cannot be included in the card structure will be 'annotated' to the card as a 'typed' hypertext information node, if it is text, or as a 'graphical' hypertext information node, if it is an image via an 'annotation' link. This will establish a part to whole relationship with a given card. Within this annotation, there may be further referential, keyword or annotation links to cards which the annotation may relate to. A card may also be linked to another card by a 'keyword' link, if two cards have the same value for a given attribute slot. The slot exists in a card in the form of a labelled field. The link names will carry a name which will depict semantic information.

There are two main reasons for following a hypertext paradigm for developing an ITS. The first one stems from the two fundamental limitations with the expert systems paradigm (Angelides, 1992). Firstly, knowledge decomposition, representation and inferencing with expert systems is exclusively hierarchical. Secondly, expert systems lack explicit information linking since all relationships are established through reasoning. The second limitation raises a serious problem with respect to any possible attempts to interconnect the knowledge models. For instance, how does one represent non-hierarchical and thus non-inferentiable relationships established in the student's knowledge?

Explicit hierarchical and non-hierarchical information linking is regarded as one of the foremost advantages of hypertext. The application of different hypertext information links settles the first limitation of the expert systems paradigm to developing ITSs. Organizational links set up inheritance hierarchies and all other links set up non-hierarchical relationships. The use of hypertext information links which are exclusively explicit because they carry semantic information settles the second limitation of the expert systems paradigm to developing ITSs and also eradicates the need to perform logical reasoning in order to infer, at least, any direct relationships between related parts in a knowledge model or related knowledge models.

Nevertheless, hypertext on its own does not constitute a framework for developing an ITS because it lacks the logical inferencing mechanisms provided by artificial intelligence. Recent research and development on artificial intelligence has focused on hybrid models that are made up of artificial intelligence and hypertext. These models utilize hypertext's hierarchical and non-hierarchical information linking abilities with artificial intelligence's logical inferencing techniques.

The second main reason for using hypertext to develop an ITS is a pragmatic one. ITS development is usually a laborious process which assumes that a lot of human and other resources will be made available during the course of development. The expert systems paradigm for developing an ITS can be time intensive and at the same time inflexible when compared to the hypertext approach. While the expert system version of an ITS took 7 months to develop (Angelides and Garcia, 1993), the same ITS developed using HyperCard II (Angelides and Gibson, 1993) only took 3 weeks, leaving also a lot of room for improvement and re-engineering.

## A sample interaction with SONATA

The system is invoked from the 'home card' of HyperCard II.1. When the user clicks the 'START' button on the start-up screen, SONATA asks for their name to check whether they are already a registered user (see Figure 1) and, if not, to construct a student record card for them.

Once this has been concluded the tutorial lesson begins. In the case of a new user, SONATA presents the user knowledge in the first area of the domain, in the form of a scenario, as shown in Figure 2.

The user clicks around with the mouse to discover the knowledge embedded in the scenario, as shown in Figure 3.

![](/api/attachments/JEPYHWKY/fulltext/images/d8164809c515b271ec31c9e9e5066acaa4bdf1296acf2282e662f778b7eb56ca.jpg)  
Figure 1 Student's status checked

When the user clicks the 'OK' button, they are returned to the original scenario. Help is available on request when the user clicks the 'HELP' button. The user can leave the scenario by clicking the 'READY TO MOVE ON' button. SONATA will prompt them to do so when it 'thinks' that the user is ready.

On leaving the scenario, the user has to go through a series of problem-solving activities, one at a time, by applying the knowledge they have acquired from the scenario they were previously in. Each activity can be tutored using up to three different strategies. Which strategy is to be used depends on the student's performance and the criteria set by SONATA. The student places a proposed solution in the box provided and informs SONATA of their attempt by clicking the 'COMPLETE' button. If the answer is right the student is advanced by SONATA, based on performance levels, to the next appropriate problem. If the answer is wrong,

![](/api/attachments/JEPYHWKY/fulltext/images/311f5754abd9a4a9a74fa254ac0e44f2a0fe68ff238f32f597d31e44b3315afc.jpg)  
Figure 2 Scenario of area 1 of SONATA's domain

![](/api/attachments/JEPYHWKY/fulltext/images/352c7e40a0cd9f137339c4e550a2e3c2378379e843bc1aa5cbbec48fe01dbbb1.jpg)  
Figure 3 Association knowledge presented

SONATA diagnoses the next best strategy to be used and tutors the same activity again. Figure 4 shows an interaction of a student engaged in a problem-solving activity.

At the end of every attempt SONATA awards the student with a score. This score is kept in a unique student record card. This interaction continues until there are no more problem-solving activities available related to the specific area or the student wishes to leave the system. In the first case, the student will be presented a scenario about the second area of the domain where the cycle starts again. In the second case, the student can leave at any point of the lesson by clicking the 'QUIT' button. When the student has completed all the problem-solving activities in the various areas of the domain, SONATA will calculate a performance score based on the scores recorded in the student's record card. This overall score will be analysed and SONATA will advise the student on whether they should continue interacting with the system or that they will no longer gain any benefit from interaction as they are deemed to be as good as the expert, as shown in Figure 5.

![](/api/attachments/JEPYHWKY/fulltext/images/2ea3e42f05914905d94e66d006a62d5cd223feec9605a42299c3923082c4b6e9.jpg)  
Figure 4 Student attempts a problem,

![](/api/attachments/JEPYHWKY/fulltext/images/0cb706c3e6274a1a07c8f2bc7c4ee225f94f2bde2f9af21eb307dcae4d3d25dc.jpg)  
Figure 5 Student's performance score analysed

The prototype was tested with a small group of students who have no previous knowledge in music theory. They commented that the tutorial sessions have been beneficial and the system is ‘relatively’ easy to use. On the basis of the interaction of that group of students with SONATA it has been estimated that it takes an average student between 2 and 3 h of continuous interaction to complete all the tests.

## Development and implementation of SONATA

SONATA is a domain-independent ITS prototype for music theory learning. The tutorial material it presents is factual knowledge covering the syllabus of the grade 1 theory of music examination set by the Associated Board of the Royal Schools of Music. The domain is divided into four areas. These areas vary in difficulty and are introduced one after another, with the easiest introduced first. Tutoring in each area involves SONATA initially teaching the student about the area, followed by the student applying their acquired knowledge through 12 successive problem-solving activities, before moving into a new area. SONATA provides four actual teaching scenarios and 48 problem-solving activities altogether.

## Tutoring strategies used in SONATA

The strategies employed in SONATA are learning through exploration, practice with a hint, multiple choice and strict question and answering. Learning through exploration presents the student with a scenario full of domain icons, that is, icons containing knowledge about one of the four areas of the domain. The student may choose freely using the mouse. When a domain icon is selected, the associated knowledge is presented to the student. The student is then expected to read and learn the material and signals the return to the original scenario when they are ready for more exploration. Practice with a hint requires the student to practise by applying his/her knowledge associated with the material presented by SONATA. A hint is supplied alongside with each practice as guidance. The multiple choice approach presents on the screen an incomplete statement associated with the knowledge domain. The student then has to select an item from a list of alternative choices offered by SONATA in order to provide the missing information. The strict question and answering strategy requires the student to answer questions associated with the domain without the help of any hints or choices.

Each of the strategies used in SONATA is distinguished from one another. Although practice with a hint, multiple choice and strict question and answering may all involve some form of question and answering activity, they differ from one another as they may influence the student's problem-solving behaviour in different ways. While practice with a hint gives indirect guidance to the student, the multiple choice approach explicitly puts the correct answer, mingled with other apparently equally likely but incorrect answers in front of the student, without any clue as to which one is the right answer. Strict question and answering differs from the two, in that no guidance or possible answers are initially given to the student.

The educational and psychological validity of these strategies is not the main focus of this paper. Here we take the view of how appropriate a strategy is to a particular student to be subjective. When applied on a student who knows the domain thoroughly, each of the four strategies may be as appropriate as one another. As for students who are still familiarizing themselves with the domain, while multiple choice may be a more suitable strategy to use than strict question and answering for one individual, another student may find it confusing to have to think about and choose between the alternatives. In that case, strict question and answering may potentially be more appropriate. Hence, except for the application of learning through exploration, which is to be used as a first strategy when a new area is to be introduced, no other order of application is presumed for the rest of the three strategies employed in SONATA. Since SONATA has no prior knowledge of a first-time student and it assumes no prior knowledge on the domain on behalf of the student, it is not possible to select an ‘appropriate’ strategy for a new student before experimenting for a while. The control mechanism in switching between strategies does not follow any extremely rigid presumed pattern.

## Criteria for the strategy selection in SONATA

At the conceptual level, the factors affecting SONATA's strategy-selection decisions are whether an area is introduced for the first time, the student's prior success with the different strategies and the suitability of a strategy to a particular type of question involved in a problem-solving activity.

When introducing an area to the student for the first time, learning through exploration is always used. This is because the other three strategies are all ‘knowledge application’ strategies, that is, they tutor through the student’s application of their knowledge about the area. Therefore, they are not applicable when the student has not even acquired any knowledge on the area. The criteria for switching from learning through exploration to one of the three strategies is based on the number of times the tutorial material in that area has been referred to. This is to prevent the student from ‘dwelling’ in the exploration scenario for too long without having to apply the knowledge they acquired from their exploration experience.

The strategies to be used for the problem-solving activities are practice with a hint (strategy P), multiple choice (strategy MC) and strict question and answering (strategy QA). For each activity, SONATA's choice of strategy depends on the student's prior success with the strategies. A strategy is regarded as successful if the student provides the correct solution in a problem-solving activity which employs that strategy. This factor affects SONATA's strategy selection at two levels. At a local level, the decision depends on the performance of the student in the previous activity. For instance, given that strategy MC is unsuccessful as the first strategy used in problem-solving activity 3 of area 1 and that strategy QA is successful as the second strategy to tutor the same activity, then the first strategy to be used in problem-solving activity 4 in area 1 will be strategy QA. If it fails, SONATA will switch to strategy P and tutor the same activity again. Strategy QA is used first because it was successful in the previous activity. Strategy P is preferred to strategy MC as a second strategy because the former had not been attempted in the last activity whereas the latter failed.

At a higher level, SONATA's strategy selection is influenced by the overall success ratings of the strategies. When $25\%$ of the 48 problem-solving activities in total have been completed, data from the student model will be gathered to infer, for the first time, the overall success rate of each of the three knowledge application strategies. SONATA will then be informed of which strategy is comparatively the most successful, moderately successful and the least successful in general up to the $25\%$ mark. This information is updated after each step in the interaction from then on. The most current information available on the success ratings control SONATA's strategy selection in the next $25\%$ of the problem-solving activities.

The type of question involved factor reflects the influence of the ‘student’s prior success’ factor on SONATA’s strategy decisions at a global level. Here an additional agent is taken into account. Every question in the problem-solving activities belongs to one of four types. Each type of question is characterized by its physical appearance and its aim, which is partly content related. When 50% of the 48 problem-solving activities have been completed, data from the student model will be collected to infer, for the first time, the success rate of each of the three knowledge application strategies on each type of question. These ‘type’ success ratings are updated after every step in the interaction thereafter and control SONATA’s strategy decision for each question in the problem-solving activities according to its type until the end of area 4.

Specific rules are used to control the criteria for SONATA's strategy selection. At the implementation level, these rules are translated into HyperCard scripts, which are pieces of program code written in HyperTalk. There are also rules used to manipulate the different types of knowledge in SONATA. All the rules are embedded in different processors within the domain model, the tutor model and the student model of the system. The rule-based mechanisms behind these processors take the form of rule sets and are achieved by using IF-THEN-ELSE control structures, together with other 'hypertextual' commands to carry out the necessary deductive reasoning. Figure 6 shows SONATA's architecture in terms of SONATA's components.

![](/api/attachments/JEPYHWKY/fulltext/images/4458358cd406efc5c308cb55483d56dc58ab79babd626bd26493754d68fefead.jpg)  
Figure 6 SONATA's architecture

## Domain model

The domain model contains the domain knowledge and the domain knowledge processor. The domain knowledge includes knowledge on the four exploration scenarios and the solutions to the 48 problem-solving activities. The processor is responsible for providing an exploration scenario with the associated knowledge, a question for a problem-solving activity, an indication of whether a student's answer is correct and the correct answer to a question when necessary.

Within the SONATA stack, there is one card allocated to the exploration scenario in an area. Another ten cards are allocated to hold the tutorial material associated with that scenario. Each of the ten cards is hierarchically linked with the scenario card. Three cards are allocated to a question for each problem-solving activity. Each of the three cards represents either strategy QA, strategy MC or strategy P.

When the student is engaged in a problem-solving activity, the student's proposed answer is stored in a labelled field in the foreground of a question card, overlapping SONATA's model answer for that question, which is stored in a labelled field in the background in the same position of the same card. The model answer is normally made invisible by the overlapping foreground field. The domain model compares the values in the foreground and background fields to check and signal for the correctness of the student's answer. If an answer is to be given to the student, the foreground field will be temporarily hidden, revealing the background field with the model answer.

## Tutor model

The tutor model contains the tutoring knowledge and a strategy-selection processor. The tutoring knowledge includes knowledge on the four tutoring strategies and the criteria for the strategy selection. The processor refers to the student model, the domain knowledge and the criteria within the tutoring knowledge, in order to determine which strategy is to be used at a given point for a particular student and when to switch from one strategy to another. Some mechanisms controlling the major rules in SONATA's strategy selection are given in the following subsections.

## Using the general best strategy first

This mechanism corresponds to the ‘student’s prior success with the strategies’ factor considered at the conceptual level. This mechanism is relevant when the student is engaged in the problem-solving activities before the 25% mark. It is used when the information from the student model indicates which strategy is the most preferred at a given point. The tutor model always uses the best strategy first. If it fails, subsequent strategies will be used in the order of preference indicated by the student model. Its choice of strategy is then passed onto the domain model, such that the appropriate card will be called upon the screen.

## Choosing a strategy at random

This mechanism also corresponds to the ‘student’s prior success’ factor considered at the conceptual level. It is used when the information from the student model does not suggest a specific preferred strategy for the next interaction, for instance, when the success ratings of the strategies are the same at a given point. In such a situation, one of the three knowledge application strategies will be picked at random to be used for the next interaction.

## Unexpected strategy change

This mechanism is related to both the ‘introduction of a new area’ factor and the ‘student’s prior success’ factor at the conceptual level. One function of this mechanism is to inform the domain model to call up the exploration scenario on the screen when introducing a new area, rather than to continue with one of the knowledge-application strategies used at the end of the last area, hence resulting in a sudden change of strategy. The second function of this mechanism is to prevent the student from being trapped in the tutoring with a single strategy for too long. Examples of this situation can be when a student lingers in an exploration scenario or when, before the 25% mark, a single strategy has been successful in five consecutive problem-solving activities within the 12 in an area.

In the first case, the student model keeps a count of the number of times the student has clicked each domain icon in an exploration scenario and passes this information onto the tutor model. When the student has referred to each domain icon in an exploration scenario of an area at least once, the tutor model will advise the student to move on to the problem-solving activities. If the student indicates they are not ready, they may continue to explore for the second round. When the student has gone through all the icons at least once more again, the tutor model automatically stops using learning through exploration and starts tutoring through problem-solving activities by switching to one of the knowledge-application strategies.

In the second case where a strategy has been successful in five consecutive problem-solving activities, the tutor model will switch to one of the rest of the two knowledge application strategies for the next activity. The tutor checks for the consecutive success by referring to the student model. This is an attempt to make sure that all strategies will have a chance to be employed, such that the purpose of SONATA's multiple strategy tutoring is not undermined.

## Using the best strategy concerning the type of question

This mechanism corresponds to the ‘type of question’ factor at the conceptual level. It is similar to the ‘using the general best strategy first’ mechanism, except that this time, the type of question the current question belongs to is taken into account. Implementing this extension involves adding another global variable which keeps the information on the type of question. A number representing the ‘type’ is tagged along each question card so that the ‘type’ variable is updated each time a different card is called up.

## Student model

The student model consists of the student knowledge and a student knowledge processor. The student knowledge includes knowledge on the score of each problem-solving activity of the student and their prior success and failure with the different strategies. The student knowledge is stored in a collection of student record cards. They form a permanent entity which keeps a historical record of each individual student's interactions with the system. Each student record card belongs to an individual student who has previously interacted with SONATA. Checks for new students are made by seeing whether a record card for that student already exists. A new card is created for every new student.

A student record card can be divided into two main parts. The first part contains 144 fields. They store the overlay scores allocated by the inference rules used in the student knowledge processor. Together they make up the student overlay record. This part of the student record card shows the subset relationship between the knowledge of the student and the expert of the domain. The second part of the record card keeps a history of the success and the current success ratings of an individual student with the different strategies. The tutor model refers to both parts of the student record card when making its strategy decision. Figure 7 shows a sample student record card.

The student knowledge processor is responsible for keeping each student record and subsequently the entire student model up-to-date. The overlay record part of a record card is maintained by inferring the student's current level of understanding of the domain. To this end, the student knowledge processor employs a set of strategy specific overlay rules to allocate an overlay score for each strategy-specific question completed by the student engaged in a problem-solving activity. Since these overlay scores are strategy specific, three scores are allocated to each problem-solving activity, as three different knowledge-application strategies can be used for each activity.

The overlay rules governing the score on each question are kept in the script of the 'COMPLETE' button on each question card, which the student has to click to indicate they have completed their attempt at that question. The overlay rules are then triggered. The resulting overlay score will be added to the corresponding field in the overlay record on the student's record card. The overlay rule set covers all the possible concoctions which may be encountered. Each overlay score awarded is within the range of -2 to 2 and is entirely dependent on the combination acquired. An example of the combination rules is shown below:

![](/api/attachments/JEPYHWKY/fulltext/images/23cc7c9d12a0cddb080fd698218a3fa39dd9b69c6f2ab825baf61b7d0c917c98.jpg)  
Figure 7 A sample student record card

IF (studentAnswer = modelAnswer) and

THEN {depending on other conditions

put 1.5 into background field X of the

corresponding student record card ELSE IF...

Before 25% of the total number of problem-solving activities are completed, the tutor model bases its strategy selection on information provided by the student overlay record.

The second half of the student record card concerns the student's prior success with the different strategies. The student knowledge processor maintains this half of the record card by keeping a count of the number of problem-solving activities the student has completed, the number of questions the student has attempted with each strategy and the number of successes the student has with each strategy. The counts are kept in individual fields on the student record card (for example, fields A, B and C, respectively, as shown in Figure 7). When the count in field A shows that the $25\%$ mark has been reached, the student knowledge processor calculates the general success rate of each knowledge-application strategy by dividing the number of successes with strategy X by the number of questions attempted with strategy X. The three resulting success rates are compared. The most successful, the moderately successful and the least successful strategies are kept separately in another three fields on the record card (for example, fields D, E and F, respectively, in Figure 7). The tutor model bases part of its ‘unexpected strategy change’ and its ‘using the general best strategy first’ decision mechanisms on this set of ratings. Each time a question is attempted, all the counts are updated, yielding a different set of success ratings. Information in the corresponding fields continue to be updated accordingly until the number of problem-solving activities completed reaches 50%. The tutor will then base its strategy-selection decisions on another set of ratings, that of the success ratings concerning the type of question.

When the corresponding count indicates that the 50% mark is reached, the success rate of each strategy for each type of question concerned is calculated by dividing the number of successes with strategy X on type Y questions by the number of type Y questions attempted with strategy X. The associated counts and fields are updated after the attempt of every single question until the end of area 4. The tutor model bases its ‘using the best strategy concerning the type of question’ decision mechanism on this set of ratings.

There is a record kept by the student model which is not registered on the student record card. This is the record related to learning through exploration. When a student is engaged in learning through exploration, the student model keeps a temporary record on the number of times the student has referred to each domain icon. The tutor model bases part of its ‘unexpected change of strategy’ decision mechanism on this record. This record is only kept in the short-term as local variables because the information it provides will no longer be useful when the tutor model moves onto tutoring through problem-solving activities.

## Concluding discussion

This paper has shown the possibility with SONATA of the development and implementation of an ITS that offers multiple tutoring strategies and can switch between them in a sensible manner. SONATA is an experimental prototype and as such succumbs to many shortcomings which may, however, provide the necessary ground for any future research and development efforts to enhance it.

Short-term research and development to enhance the system performance may be undertaken in several areas. As far as SONATA's strategy selection is concerned, the system bases all its decision on its diagnosis of the student and the student's own preference is never consulted (Siemer and Angelides, 1993). Improvement of the system can be made by identifying situations where the student should be able to express their preference. For example, at a given point at which the student's prior success rates with the different strategies are equal, rather than selecting the strategy for the next problem-solving activity at random, SONATA should allow the student to choose a strategy him/herself. SONATA can even go further onto making a record of the student's initial preferences and take them into account in its future strategy-selection decisions.

SONATA assumes that each new user is an absolute beginner. With respect to pre-modelling, the system may be made more sensitive to the student's needs if the system can ask the user a series of standard questions, so as to deduce the level of knowledge of a new student about the domain. As for student modelling, at least one more element can be added to SONATA's student model to enhance the model's usefulness as an informative agent, that of a set of mal-rules. With the incorporation of mal-rules, SONATA will then be able to diagnose and represent a student's misconceptions as well as missing concepts, such that remedial activities can be offered accordingly. While misconception diagnosis may not be a requirement in certain ITSs, it would be appropriate if SONATA can take into account the type of misconceptions a student has about the domain when deciding which strategy is to be used.

More work can be done to enhance the communication channel between SONATA and its student. At the moment, the system is not able to answer arbitrary questions or hypothetical questions from the student about the subject matter, nor can it give an explanation of a problem solution. This is due to the lack of a natural language interface since SONATA does not incorporate the underlying grammar that reflects the semantics of the domain. Further work on SONATA in the long run will eventually have to be diverted to an extensive research on natural language processing if SONATA is to be able to respond intelligently to questions and situations posed by the pupil. In the short-term, future development can aim at improving the existing menu-based interface, perhaps by increasing the variety of legitimate inputs from the user and the corresponding pre-set output messages, so as to provide a wider channel of communication between SONATA and its users.

In terms of implementing multiple tutoring strategies in ITSs in general, future researchers should not merely rest upon developing a model which can merely accommodate a number of different strategies and being able to switch between them in a reasonable manner. In order to recognize such an ITS as a system that is educationally and psychologically valid, a more solid foundation on which its strategy selection is based is necessary. The core of implementing multiple strategies in ITSs requires more specific and detailed accounts of teaching. We have to understand why, when and how human tutors switch strategies and, more fundamentally, in what way do the strategies themselves and the changes in strategies affect a student's learning, which in turn bring us to the question of how does one learn. In order to understand the essence of the interaction between the tutor and the student, we must jump out of the limits set by the boundaries of existing ITS architecture to try to capture and model other aspects in the field of education, such as reasoning and learning processes (Elsom-cook, 1991).

## References

Anderson, J.R. (1988) The expert module, in Foundations of Intelligent Tutoring Systems, Polson, M.C. and Richardson, J.J. (eds) (Lawrence Erlbaum, NJ, USA), pp. 21–53.

Anderson, J.R. and Reiser, B.J. (1985) The Lisp Tutor. Byte, 10(6), 159–75.

Angelides, M.C. (1992) Developing the didactic operations for intelligent tutoring systems: a synthesis of artificial intelligence and hypertext, PhD thesis, University of London, UK.

Angelides, M.C. and Doukidis, G.I. (1990) Is there a place in OR for intelligent tutoring systems? Journal of the Operational Research Society, 41 (6), 491–503. (Reprinted in Artificial Intelligence in Operational Research, Doukidis, G.I. and Paul, R.J. (eds) (Macmillan, London), pp. 287–299.)

Angelides, M.C. and Garcia, I. (1993) Towards an intelligent knowledge based tutoring system for foreign language learning. Journal of Computing and Information Technology, 1 (1), 15–28.

Angelides, M.C. and Gibson, G. (1993) PEDRO – the Spanish tutor: a hypertext-based intelligent tutoring system for foreign language learning. Hypermedia, 5(3), 205–30.

Begeman, M.L. and Conklin, J. (1988) The right tool for the right job. Byte, 13 (10), 255–267.

Brown, J.J., Burton, R.R. and Bell, A.G. (1975) SOPHIE: a step towards learning environment. International Journal of Man–Machine Studies, 7, 675–96.

Elsom-cook, M.T. (1991) Dialogue and teaching styles, in Teaching Knowledge and Information Technology, Goodyear, P. (ed.) (Ablex Publishing Corporation, NJ), pp. 61–83.

Goldstein, I.P. and Carr, B. (1977) The computer as coach: an athletic paradigm for intellectual education, in Proceedings of the International ACM Conference, Seattle, Washington, DC, pp. 227–33.

Goldstein, I.P. (1982) WUMPUS, in Handbook of Artificial Intelligence, Barr, A. and Feigenbaum, F.A. (eds) (Addison-Wesley, MA, USA), pp. 261–6.

Halff, H.M. (1988) Curriculum and instruction in automated tutors, in Foundations of Intelligent Tutoring Systems, Polson, M.C. and Richardson, J.J. (eds) (Lawrence Erlbaum, NJ), pp. 79–108.

Hollan, J.D., Williams, M.D. and Stevens, A.L. (1981) An overview of STEAMER: an advanced computer-assisted instruction system for propulsion engineering. Behaviour Research Methods and Instrumentation, 13, 177–217.

Holland, S. and Elsom-cook, M.T. (1990) Architecture of a knowledge based music tutor, in Guided Discovery Tutoring, Elsom-cook, M.T. (ed.) (Paul Chapman Publishing, London), pp. 70–93.

Marchionini, G. and Shneiderman, B. (1988) Finding facts vs. browsing knowledge in Hypertext systems. IEEE Computer, 21(1), 70–80.

Nielsen, J. (1990a) Hypertext and Hypermedia (Academic Press, Boston, USA).

Nielsen, J. (1990b) The art of navigating through Hypertext. Communications of the Association of Computing Machinery, 33 (3), 297–321.

Shneiderman, B. and Kearsley, G. (1989) HYPERTEXT-HANDS-ON!: An Introduction to a New Way of Organising and Accessing Information (Addison-Wesley, MA, USA).

Siemer, J. and Angelides, M.C. (1993) Towards a model for remedial operations in intelligent tutoring systems, in Opportunity and Risks of Artificial Intelligence Systems, Proceedings of the Artificial Intelligence Stream, 35th Annual Operational Research Society Conference, Angelides, M.C. and Siemer, J. (eds) University of York, September, pp. 4–32.

Smeaton, A.F. (1991) Retrieving information from hypertext: issues and problems. European Journal of Information Systems, 1 (4), 239–247.

Stevens, A., Collins, A. and Goldin, S.E. (1982) Misconception in students understanding, in Intelligent Tutoring Systems, Sleeman, D. and Brown, J.S. (eds) (Academic Press, London), pp. 13–24.

VanLehn, K. (1988) Student modelling, in Foundations of Intelligent Tutoring Systems, Polson, M.C. and Richardson, J.J. (eds) (Lawrence Erlbaum, NJ, USA), pp. 55–78.

## Biographical notes

Marios Angelides is a Lecturer in the Information Systems Department at the London School of Economics. He holds a BSc degree in Computing and a PhD in Information Systems, both from the London School of Economics. He has 6 years of experience in researching in the area of intelligent tutoring systems in which he completed his PhD. He has authored and co-authored 12 journal papers in intelligent tutoring systems. In addition he has published another six articles in other areas of artificial intelligence, one of which is in the area of artificial intelligence and simulation. He is the co-author of the book Lisp: From Foundations to Applications published in 1988. He is Vice-Chairman of IFIP's (International Federation for Information Processing) Working Group 9.5: Social Implications of Artificial Intelligence Systems.

Amelia Tong is a full-time research student reading towards the degree of PhD (Econ) in Information Systems in the Information Systems Department at the London School of Economics. Her research area is that of intelligent tutoring systems. She holds the degrees of BSc in Computing and MSc in Analysis, Design and Management of Information Systems, both from the London School of Economics.

Address for correspondence: Marios Angelides, Information Systems Department, London School of Economics and Political Science, Houghton Street, London WC2A 2AE, UK.
