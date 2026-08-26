---
otero_id: 21489
otero_key: "7CVC6G96"
title: "A comprehensive method for the evaluation of complete intelligent tutoring systems"
authors: "Julika Siemer; Marios C Angelides"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00033-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A comprehensive method for the evaluation of complete intelligent tutoring systems

Julika Siemer <sup>)</sup>, Marios C. Angelides

Information Systems Department, London School of Economics, Houghton Street, London WC2A 2AE, UK

## Abstract

Although it is generally believed that intelligent tutoring systems promise a great potential for education, little work has been done on the development of an appropriate evaluation method to assess these systems. This paper proposes an evaluation approach that serves to deliver comprehensive suggestions for the overall improvement of both the architecture and the behaviour of a complete intelligent tutoring system. q 1998 Elsevier Science B.V.

Keywords: Intelligent tutoring systems; Evaluation; Education

## 1. Introduction

Many intelligent tutoring systems have been developed to date. However, little work has been done on the development of evaluation methods for intelligent tutoring systems. Most papers on intelligent tutoring systems that have been developed merely give a detailed description of the system’s architecture in order to provide sufficient information for the reader to reconstruct or at least understand the system 1,12,14 . In fact, this phenomenon can be found<sup>w</sup> <sup>x</sup> in the area of artificial intelligence as a whole where the ‘develop–test–review–throwaway’ sequence, which does not include an evaluation step, has been a common approach 18 . <sup>w</sup> <sup>x</sup>

Appropriate evaluation can serve as a tool to propel research developments by providing suggestions for the overall improvement of the architecture and the behaviour of intelligent tutoring systems. In a future where intelligent tutoring systems might be widely available in educational institutions, evaluations will have to answer questions about the usefulness of intelligent tutoring systems, i.e. their ability to foster learning. Evaluations may influence what and how students learn 29 . They may provide <sup>w</sup> <sup>x</sup> information about the system’s architecture and the impact of its behaviour on the user which may serve as feedback into the system and, thereby, assist system improvement. In this way, evaluations help to determine the extent to which a particular system meets certain requirements and to reveal its research value, such as its strengths and shortcomings. Consequently, evaluations may eventually influence the choice as to whether or not one should use a particular intelligent tutoring system.

Furthermore, evaluating intelligent tutoring systems makes interested readers more aware of the system’s research value in the context of their own work and helps to describe the direction in which the system is moving. The evaluation of intelligent tutoring systems may influence interest in, and support for, future research and development 29 .<sup>w</sup> <sup>x</sup>

It is the objective of this paper to propose an evaluation approach that serves to deliver comprehensive feedback about a complete intelligent tutoring system for the purpose of system improvement. For this purpose, the paper first defines ‘complete intelligent tutoring systems’. It then introduces two fundamental evaluation questions that stem from the relevant literature, one that addresses the architecture of an intelligent tutoring system, and one that addresses the behaviour of the system during system– user interaction. This leads to proposing a comprehensive evaluation method that examines both the system architecture and the behaviour the system.

## 2. Defining complete intelligent tutoring systems

The early teaching theory views educational processes as the communication of knowledge to the student. Wenger 26 initially defines this form of<sup>w</sup> <sup>x</sup> knowledge communication as ‘‘the ability to cause and<sup>r</sup>or support the acquisition of one’s knowledge by someone else, via a restricted set of communication operations’’. Systems, such as computer aided instruction, which simply present the teaching material to the student in a sequential order, have been developed based on this theory.

However, in more recent empirical studies of the behaviour of human teachers, diagnosis and remediation have been found to form a substantial part of the overall tutoring interaction 1,27 . Within a tutorial<sup>w</sup> <sup>x</sup> interaction, a human teacher tries to identify and interpret a student problem diagnosis and then—Ž . using a suitable strategy—continues to communicate with the student to overcome or correct the problem Ž . remediation .

These observations and views have recently evolved in the wide acceptance of a general structure for the overall teaching process in intelligent tutoring systems 28 . This structure divides the teaching<sup>w</sup> <sup>x</sup> process of an intelligent tutoring system into four separate functions: the planning of a series of teaching actions; the monitoring of the execution of these actions with the student, i.e. comparing the student behaviour against the expected outcome in order to determine any errors; the diagnosis of any discrepancies found between the student behaviour and the expected outcome in order to determine the cause of an error; and then remediate the error.

Comparing this structure with the earlier view of the teaching process, i.e. that of the communication of the domain knowledge, results in the observation that the more recent view of the teaching process in intelligent tutoring systems features diagnosis and remediation as central aspects.

The majority of intelligent tutoring systems which have been developed more recently are based on this new structure of the teaching process which emphasises the significance of diagnosis and remediation in a tutoring process 15,30 . With the emergence of<sup>w</sup> <sup>x</sup> this new learning theory frameworks for the architecture of a complete intelligent tutoring system which provides student-centred instruction evolved. No standard for an intelligent tutoring system architecture exists, but the general agreement has emerged that an intelligent tutoring system should comprise the following three models 7 : the<sup>w</sup> <sup>x</sup> domain model, which contains the knowledge about the domain to be taught; the student model; which represents the emerging knowledge and skills of the student; and the tutoring model; which designs and regulates instructional interactions with the student, i.e., it pursues certain teaching goals through the use of teaching strategies. Each of these models may incorporate certain processes that manipulate the information necessary for the tutoring interaction. The domain model incorporates the domain knowledge process, referred to as the expertise; the student model incorporates the student knowledge process, referred to as diagnostics; and the tutoring model incorporates the tutoring knowledge process known as the didactics. Further processes are required to maintain overall system control, i.e. to co-ordinate the interaction between the system’s three knowledge and process models. Frequently, the user interface is mentioned as a fourth component of an intelligent tutoring system architecture 30 . The general intelligent<sup>w</sup> <sup>x</sup> tutoring system architecture is illustrated in Fig. 1.

The three components of an intelligent tutoring system are addressed in more detail below followed by a description of how complete intelligent tutoring may be provided by such a system.

## 2.1. The domain model

The domain model of an intelligent tutoring system contains the knowledge about the subject area to be taught. The intelligent tutoring system uses its domain knowledge to reason about and solve a problem or question which has been set for, or by, a student. For this purpose, the knowledge has to be represented in such a way that it supports reasoning that resembles the human problem-solving process within the teaching domain. Furthermore, different knowledge representations of the same domain knowledge may be required to support the application of alternative teaching strategies.

![](/api/attachments/7CVC6G96/fulltext/images/bbd2f81d8f14a6e6c8d8090d0398e5f4232202dfdfba0fc6c9e85e80eeb78ffd.jpg)  
Fig. 1. The components of an intelligent tutoring system.

Additional domain knowledge may be required to deal with student errors. The domain model may have to provide knowledge in order to correct any common misconceptions or missing concepts the student might display during a tutoring interaction.

The expertise includes all the processes required to provide for the content, i.e. for the appropriate domain knowledge, of a teaching interaction. Such processes may include the retrieval of the teaching material following system requests for materials on the next topic to be taught or a student error to be corrected. Similarly, the system may demand a different presentation, or viewpoint, of the same teaching material requiring the domain knowledge process to manipulate or retrieve the domain knowledge accordingly.

## 2.2. The tutoring model

An intelligent tutoring system should exhibit various tutoring characteristics. These are encapsulated in the tutoring model. Every teaching episode pursues a specific teaching goal. The tutoring model has to provide appropriate knowledge for theses goals to be pursued. It must have control over the selection and the sequencing of material to be presented to the student, it has to have capabilities to respond to a student’s question about the subject matter and it has to apply strategies to determine when students need help in the course of practicing a skill, and what sort of help is needed. For this purpose, the tutoring model has to incorporate different teaching strategies <sup>w</sup> <sup>x</sup> 16 .

Teaching strategies are used to present material and depend on the subject matter and the instructional objectives of the intelligent tutoring system. A teaching strategy determines the style of material delivery that is employed in order to lead the student through the tutorial and to intervene if the student needs special assistance with a problem he encounters. Accordingly, different teaching strategies may be required in different teaching situations. A wide selection of different teaching strategies offers better flexibility and may therefore provide better adaptation of the teaching process to the student.

The tutoring knowledge process, i.e. the didactics, is responsible for selecting the next teaching goal to be satisfied from the teaching goals to be pursued and for determining an appropriate teaching strategy for attaining this goal for a particular student based on information from the student model. The strategy may be chosen according to the peculiarities of a tutorial situation, such as the student’s needs and preferences, his experience and the domain of discourse 2 .<sup>w</sup> <sup>x</sup>

## 2.3. The student model

To carry out intelligent tutoring, a tutor has to have a good understanding of the student being taught. For this reason, an intelligent tutoring system uses a student model to represent the student’s emerging knowledge and skills of the subject matter. An intelligent tutoring system uses its student model to analyse the input of the student during a tutoring interaction. The student’s input may be answers to questions posed by the intelligent tutoring system, moves taken in a game, or commands delivered within an editor. Accordingly, a more sophisticated student model may contain more detailed information about the student. This information does not only have to refer to the knowledge the student has acquired within the learning process. Information about the student, such as his leaning preferences, his past learning experience and his advancement stage may be relevant for the adaptation of the teaching process.

Furthermore, the student model may have to record any errors a student might have made. Whilst missing concepts may easily be recorded as missing domain knowledge the student model has to arrange for the recording of any misconceptions, i.e. a different conception of some part of domain knowledge, the student might have been found to possess.

The student knowledge depicts the relative strengths e.g. with topics and with teaching ap- Ž proaches and weaknesses of the student e.g. mis- . Ž conceptions and missing concepts . To provide this . information, i.e. to maintain the student model, the student knowledge process analyses the behaviour of the student.

## 2.4. Towards student-centred tutoring

The overall system control coordinates the knowledge of the three knowledge models to provide student-centred tutoring, i.e., to adapt the tutoring process to the student’s needs and preferences. There are a number of adaptation tasks and features which require overall system control coordination.

An intelligent tutoring system, for example, has to apply suitable teaching strategies and presentations for each subject matter unit as needed, choosing the form that is most beneficial to the student for a particular instructional situation.

At the same time, the system has to account for student errors that might occur during the tutoring interaction. As described in the discussion about learning theories above, individualised and efficient remediation forms an essential part of the overall teaching process. Every detected error requires a remedial process that is adapted to the individual needs of the student.

The selection of an appropriate teaching strategy and its presentation for both general and remedial tutoring may require knowledge about the student’s needs and preferences stored in the student model.

A further issue of student-centred tutoring is the issue of proactive instruction and reactive instruction <sup>w</sup> <sup>x</sup> 1,24 . An intelligent tutoring system may provide adaptability to the student by providing both help that may be invoked by the student or by the system. An advanced student, for example, may recognise his need for help and may decide to activate system help. However, when the student is a novice, or when the domain knowledge is broader, system-invoked help seems more appropriate. The student may require intervention when the student makes a mistake without realising it, or when the student does not know what to do next.

This section has introduced the components and characteristics of a complete intelligent tutoring system that offers individualised student guidance and support within the learning environment. Section 3 reviews existing evaluation methods and examines how well they address complete intelligent tutoring systems as defined in this section.

## 3. The need for evaluation

Recent literature gives evidence of an increased interest in the development of evaluation methods for intelligent tutoring systems 9,13 . However, the<sup>w</sup> <sup>x</sup> few evaluation proposals that have been made generally represent methods which have been developed in an ad hoc manner for the purpose of examining a specific feature or component of the intelligent tutoring system.

O’Shea et al. 17 , for example, propose their 13 <sup>w</sup> <sup>x</sup> ‘pillars’ of intelligent tutoring system design as a framework for intelligent tutoring system evaluation. These pillars represent the author’s desired features of any computer-based tutor. They include robustness, helpfulness, simplicity, perspicuity, power, navigability, consistency, transparency, flexibility, redundancy, sensitivity, omniscience and docility. Although these ‘pillars’ provide a basis for a wide and flexible evaluation of an intelligent tutoring system, they constitute very general design principles which address the displayed behaviour of an intelligent tutoring system. They do not attempt to investigate the underlying architecture, i.e. the components, of the intelligent tutoring system which is responsible for the behaviour of the system. The pillars address overall system features without addressing the underlying ‘intelligence’ of the system, such as tutoring and student modelling abilities.

Self 19 suggests a further evaluation method. He<sup>w</sup> <sup>x</sup> proposes a set of subject-independent questions to determine how well an intelligent tutoring system lives up to its prefix ‘intelligent’. Self derives his evaluation questions from the following four princi ples that should apply in any teaching situation:

<sup>Ø</sup> the teacher should know something about the subject,

<sup>Ø</sup> the teacher should know something about the student,

<sup>Ø</sup> the student should be ‘actively engaged’ and not simply be told, and

<sup>Ø</sup> learning is likely to be handicapped if the teacher and student have difficulty communicating with one another.

Accordingly, the evaluation questions fall under the following four categories:

<sup>Ø</sup> domain knowledge,

<sup>Ø</sup> student knowledge,

<sup>Ø</sup> student control, and

<sup>Ø</sup> mode of communication.

Self 19 keeps the questions very general, like, for<sup>w</sup> <sup>x</sup> example, ‘‘Does the system intervene if the user appears to be having difficulties?’’. The idea behind this generality is to give the evaluator a chance to state exactly to what extent the system intervenes and to what extent it does not, possibly by giving examples of situations in which the system intervenes and in which it does not.

However, Self’s evaluation method has its drawbacks. The four categories do not address all aspects of a complete intelligent tutoring system. Although Self attempts to address the ‘intelligence’ of the intelligent tutoring system his investigation fails to address important issues, such as the system’s ability to diagnose student errors and to provide remedial tutoring which, according to recent theories of teaching, constitutes an essential part of the overall tutoring process 15 . Also, apart from the student control <sup>w</sup> <sup>x</sup> issues addressed, the evaluation method does not investigate other tutoring abilities, such as tutoring approaches used within a tutoring interaction. Furthermore, Self’s questions merely investigate the ‘intelligent behaviour’ of the intelligent tutoring system as it may be perceived by a system user. The underlying architecture that provides this behaviour is not addressed.

Nwana 14 proposes a further evaluation method.<sup>w</sup> <sup>x</sup> He evaluates his fractions intelligent tutoring system against:

<sup>Ø</sup> the principles upon which it was built to determine how well it achieved its goals,

<sup>Ø</sup> Self’s 19 set of evaluation questions, <sup>w</sup> <sup>x</sup>

<sup>Ø</sup> real students to reveal any limitations of the system’s usability, and

<sup>Ø</sup> O’Shea et al’s. 17 thirteen ‘pillars’ of intelligent<sup>w</sup> <sup>x</sup> tutoring system design.

Nwana offers a broad and flexible evaluation of his system. However, although the evaluation method aims to be more comprehensive through the collection of student feedback and the incorporation of the ideas proposed by both O’Shea 17 and Self 19 ,<sup>w x</sup> <sup>w x</sup> the evaluation method still remains at a very general level and does not address architectural details. Nwana’s evaluation has been developed around the principles upon which a system is built. As a consequence, the proposed evaluation approach is closely tailored to the specific needs of a system, and in this case Nwana’s system. Although many evaluation methods have been developed for the evaluation of one specific system, these methods could not be used in the evaluation of another system 20 .<sup>w</sup> <sup>x</sup>

This section has revealed that existing evaluation methods have been tailored to address specific systems, particular components, or the behaviour of a system 11,13 . There are currently no generally <sup>w</sup> <sup>x</sup> agreed principles for the assessment of complete intelligent tutoring systems 21 . The successful eval-<sup>w</sup> <sup>x</sup> uation of an intelligent tutoring system requires a comprehensive examination of both the underlying architecture of an intelligent tutoring system and the impact of the system’s behaviour on the student. This calls for both internal and external evaluation of a complete intelligent tutoring system 9,10 . Accord-<sup>w</sup> <sup>x</sup> ingly, a comprehensive evaluation of a complete intelligent tutoring system seeks to answer the following two questions: 1 ‘What is the relationship Ž . between the architecture of an intelligent tutoring system and its behaviour?’; 2 ‘What is the educa-Ž . tional impact of an intelligent tutoring system on students?’ Internal evaluation addresses question 1, and external evaluation addresses question 2. This is summarised in Fig. 2.

![](/api/attachments/7CVC6G96/fulltext/images/ee9ee33d2decc5141df191cd32dbce1dd3dee43d0215f3a15f4a8148f0728659.jpg)  
Fig. 2. The internal and external evaluation of an intelligen tutoring system.

Section 4 proposes a comprehensive method for internal and external evaluation and demonstrates how such an evaluation method can overcome the weaknesses of current evaluation approaches.

## 4. Developing a comprehensive method for the internal and external evaluation of a complete intelligent tutoring system

The following sections discuss how internal and external evaluation can eliminate the weaknesses and incorporate the strengths of the evaluation methods proposed to date. They attempt to provide comprehensive examination of all features of an intelligent tutoring system in order to account for O’Shea’s concern for wide and overall evaluation. At the same time, the proposed method eliminates the vagueness and generality that is represented in O’Shea’s 13 pillars by making the evaluation more specific to the intelligent tutoring system in question allowing for detailed evaluation of specific features or components as requested by Self. Furthermore, the method eliminates the weakness of system-tailored methods as proposed by Nwana 14 and Shute and Glaser <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 20 , i.e., it remains system-independent in that it provides a tool for the evaluation of any intelligent tutoring system.

## 4.1. Internal eÕaluation

The purpose of internal evaluation is to provide a clear picture of the architecture of the intelligent tutoring system and to determine how this architecture yields the system’s behaviour. To clarify the relationship between the three main components of the architecture and the behaviour of an intelligent tutoring system, an intelligent tutoring system can be characterised in terms of answers to the following three key questions:

<sup>Ø</sup> What does the intelligent tutoring system know?

This question is addressed by an analysis of the system’s domain, student and tutoring knowledge in respect to what the intelligent tutoring system can possibly do based on the knowledge its three knowledge and process models are able to provide.

<sup>Ø</sup> How does the intelligent tutoring system do what it does?

Answering this question assesses whether the system performs in the way the designer intended it. This question is answered by analysing the intelligent tutoring system to determine how its processes generate the system’s observed behaviour. The processes to be examined include the system’s expertise, diagnostics and didactics, as well as the overall system control which directs the cooperation of the three knowledge and process models.

What should the intelligent tutoring system do? This question is addressed by examining the overall capabilities of the system’s teaching processes.

According to Littman and Soloway 10 , these<sup>w</sup> <sup>x</sup> three questions are addressed by performing Knowledge LeÕel Analysis, Program Process Analysis and Tutorial Domain Analysis.

Knowledge LeÕel Analysis attempts to characterise the knowledge provided by the intelligent tutoring system and hence answers the first question: What does the intelligent tutoring system know? It provides useful information about whether the intelligent tutoring system has sufficient and appropriate knowledge about the domain, the student and tutoring in order to meet the requirements that were set for it. It is not concerned with how and when the system uses or manipulates this knowledge in order to provide for student guidance. Accordingly, knowledge level analysis has to address issues, such as the scope of the system’s domain, student and tutoring knowledge and whether the knowledge representation is appropriate.

Program Process Analysis answers the second question: How does the intelligent tutoring system do what it does? Program process analysis examines whether the intelligent tutoring system does what it does in the right way. In contrast to knowledge level analysis, which asks whether the intelligent tutoring system is able to perform certain input–output tasks, program process analysis looks just at how a system uses and manipulates its intelligent knowledge for the purpose of game play. Program process analysis may consequently investigate the expertise, i.e., the way domain knowledge is used and manipulated, the diagnostics, i.e., procedures used by the system to analyse the input of the student to maintain the student model, and the didactics, i.e., the way teaching goals are determined and teaching strategies are used to guide the game. Eventually, program process analysis may assess the overall system control which coordinates the interaction between the system’s three knowledge models.

Tutorial Domain Analysis answers the third question of What the intelligent tutoring system should do? by emphasising any lack of tutorial abilities in any of the three standard knowledge components of the intelligent tutoring system. These tutorial capabilities are generally specified at the outset of the system implementation stage. However, tutorial domain analysis during the implementation process may sometimes change the limits of the tutorial domain, i.e., the system requirements, with the result that part or all of the three knowledge models may require alteration or extension.

The result of these three analyses provide a picture of whether and how all the knowledge and process models, i.e., the domain model, the student model, the tutoring model, and the overall system control of an intelligent tutoring system architecture, account for the system’s desirable behaviour. Consequently, these analyses involve a thorough investigation of the behaviour of the intelligent tutoring system under evaluation. In order to carry out such an investigation, it is necessary to define exactly what constitutes the behaviour that the architecture of an intelligent tutoring system should provide. A popular way of presenting the desirable overall behavioural properties of an intelligent tutoring system is to establish a set of evaluation questions. The use of evaluation questions is generally referred to as criterion-based eÕaluation <sup>w</sup> <sup>x</sup> 11 . Each evaluation question addresses a criterion that needs to be considered in connection with a particular behaviour expected by the system. These questions can be derived from the behaviour, and a complete intelligent tutoring system is expected to display as outlined in Section 2. Accordingly, the evaluation questions should relate to the three knowledge and process models of an intelligent tutoring system architecture, addressing the behaviour a system may display using the knowledge and the processes provided by its architecture. The actual internal evaluation, i.e., Knowledge LeÕel Analysis, Program Process Analysis and Tutorial Domain Analysis, is carried out by determining whether the system can behave in the way suggested by the evaluation questions within those three categories.

![](/api/attachments/7CVC6G96/fulltext/images/b9aaac44f7d9d5d2f4ce7f1472664504f86167b8b4e9b1bf7f8f097cf4a0fb3d.jpg)  
Fig. 3. The internal evaluation of intelligent tutoring systems.

Fig. 3 outlines the concept of the internal evaluation of intelligent tutoring systems. It illustrates what kind of evaluation questions may support internal evaluation. The questions have been grouped under the knowledge and process models they address. The evaluation questions suggested in Fig. 3 are based on Self’s proposed set of evaluation questions and their relevance to complete intelligent tutoring systems as defined above. The questions inquire about the intelligent tutoring system’s properties in a fairly general way allowing the evaluator to specify all negative and positive features that are addressed by the question under consideration. The resulting answers can then be used to relate the system’s behaviour to its architecture by stating how the system does certain things or why it might be unable to do them. Consequently, the answer to the same question may investigate knowledge and processes as part of knowledge level analysis and program process analysis, whilst the same answer may also reveal overall shortcomings of the system thereby addressing tutorial domain analysis.

The boundaries between knowledge and process of a knowledge and process model vary between different systems and are not always clearly defined. For this reason, the same evaluation question may support both knowledge level analysis and program process analysis depending on the system under evaluation. The question ‘Can the system give alternative explanations of the same concept?’, for example, requires an intelligent tutoring system to provide for different representations of the same domain knowledge. Whilst one system may directly refer to ready stored representations of the domain knowledge, the other system may have to apply a particular process to restructure its knowledge for the representation on request. Consequently, the provision of the particular representation within the second system involves the investigation of both domain knowledge and the process of expertise.

## 4.2. External eÕaluation

External evaluation assesses the impact an intelligent tutoring system may have on the student. It examines how an intelligent tutoring system affects the student and how it changes his knowledge and skills. Since the goal of an intelligent tutoring system is to teach, a major issue is to evaluate how effectively students learn. At the same time, user-centred evaluation may assess the more general issue of user satisfaction with the system 5,6 . External evalua-<sup>w</sup> <sup>x</sup> tion, therefore, aims at an overall conclusion or estimate about the system, such as the more fundamental needs concerning the system’s usefulness to the student, like its ability to a foster learning,Ž . which is generally referred to as learning achieÕement; and b motivate and satisfy the student, de-Ž . scribed as the learning affect.

## 4.2.1. Learning achieÕement

The evaluation of learning achievement as an overall impact of an intelligent tutoring system involves the determination of how well the system teaches underlying knowledge and skills. Learning achievement includes aspects such as the acquisition and the understanding of, and the performance with, the student’s knowledge. The dominant approach to assess learning achievement of students with earlier tutoring systems, such as computer aided instruction, has been through determining whether students correctly responded to test questions. However, such an evaluation which focuses on correct and incorrect answers does not adequately reflect the mental processes underlying the answers. With the emergence of intelligent tutoring systems came the request to assess the reasons why students give correct and incorrect answers by determining how well the system teaches students the knowledge and skills that support the mental processes required to solve problems in the system’s teaching domain.

Intelligent tutoring systems reason about the student’s problem-solving behaviour, i.e., they apply diagnostic processes, in order to build up a student model that provides information on the understanding of the student’s knowledge and skills. In return, this information is used to interpret the student’s behaviour and to guide the system’s teaching processes.

The student model can be used to assess how well the intelligent tutoring system teaches problem solving knowledge in the domain. Littman and Soloway <sup>w</sup> <sup>x</sup> 10 first proposed the use of student modelling techniques to support a new approach to external evaluation. They suggest that with the help of their student modelling abilities, intelligent tutoring systems could construct a range of problems that the student should be able to solve. These problems can then be used to test the student. The success rate of the student is a measure for the student’s learning achievement. A correct student problem solution indicates that the underlying processes or knowledge and skills have been taught successfully by the system. Furthermore, the result of such a test may not only indicate whether the student is able to solve certain problems, but it may also give the reasons why the student has been able or unable to solve the problem. Student modelling techniques based on process models can be used to predict the actual process the student has to go through to solve problems whilst student modelling techniques that are not based on process models can be used to determine some of the knowledge and skills the student has to use to solve problems.

Therefore, the evaluation of early tutoring systems which focused on correct and incorrect answers is different from the evaluation of intelligent tutoring systems which assess the reasons why students give correct and incorrect answers. In the external evaluation of the intelligent tutoring system, the criterion is not how many of the students’ answers are correct but how well the system teaches underlying finegrained skills that support the student’s problem solving processes in the domain.

## 4.2.2. Learning affect

The affect of the teaching process is concerned with aspects such as attitudes and emotions caused by the intelligent tutoring system. Motivation in the context of learning can be viewed as an indication of the student’s willingness to be active and involved in the learning process and is therefore recognised as an important factor of learning 3 . Various ways of<sup>w</sup> <sup>x</sup> assessing the motivating impact of systems have been suggested 10 . Motivation is often assessed by <sup>w</sup> <sup>x</sup> asking the student to simply rate his agreement with specific issues, such as attitudes and activities. Comparisons of time spent on task-related and task-unrelated material during an interaction are another indicator for the motivation of the student. Also the drop-out rate, i.e., the overall time spent on a teaching session, indicates the level of interest of the student.

Measuring motivation provides an indication for how students feel about a particular system. The extent of motivation in return may provide information about the learning achievement since such motivation contributes towards the actual learning achievement discussed in Section 4.2.1. At the same time, the motivation of students working with a particular system suggests whether the system will be accepted and used.

The external evaluation of an intelligent tutoring system involves a planned experiment 24 . Experi-<sup>w</sup> <sup>x</sup> mental research enables researchers to examine whether the implementation of a system or part of a system has been successful in the sense that it is accepted by the student and that the student perceives the system’s behaviour in the intended way. It also gives information about the relationships between teaching interactions between student and system and the teaching outcome. Setting up an experiment generally involves the following aspects 24 .<sup>w</sup> <sup>x</sup>

The determination of the experimental group or person to carry out the investigation, such as students, the supervisor and the system designer. The experimental group may be selected based on factors, such as different ability and age. Some form of introduction or training may be required to prepare the group in order to use the intelligent tutoring system and carry out the experiment.

The determination of the environment of the experiment. An experiment may take place in a classroom under normal teaching conditions or in a more controlled environment with a selected experimental group.

The selection and design of reaction assessment tools. Experimental evaluation may involve interviewing the experimental group or asking them to fill in a questionnaire. It is left to the system developer and his knowledge about the system’s goals to prepare an appropriate reaction assessment tool, such as the questionnaire or interview, in such a way that it addresses the research question under examination. The concept of complete intelligent tutoring may support the design of such a questionnaire since it portrays tutoring in the way it should be perceived by the student. Additionally, the affect of intelligent tutoring systems can be assessed with individuals by means of individual interviews.

The assessment of learning achievement may further require the special design of a problem for the student to solve.

The determination of the setting. A setting refers to what the evaluator intends to expose the experimental group or person to, such as the part of the system processes they will have to encounter. Since this section is concerned with the overall evaluation of an intelligent tutoring system, the experimental setting should include all system processes. The determination of the setting may therefore involve ensuring that all relevant aspects are addressed within the experiment, possibly requiring the evaluator to allocate time to the relevant aspects or tasks to be addressed by the experimental group.

After the experiment has been set up and carried out, the evaluation results have to be analysed in order to determine any benefits and shortcomings of the system. It is argued that the use of an experimental approach to intelligent tutoring system evaluation does not require a particular method for examining or analysing the data 29 . The data itself, in conjunc-<sup>w</sup> <sup>x</sup> tion with the questions it addresses, guides the decisions about how the data should be analysed to provide constructive feedback for system improvements.

Section 5 demonstrates how to apply the proposed method in the evaluation of an existing intelligent tutoring system which according to the definition in Section 2 is complete. Although so far, internal and external evaluation have been addressed separately for the purpose of their discussion, this is not the case when the actual evaluation of a system is performed. There is much cross-fertilisation between the two. After all, the behaviour of a system which is addressed by external evaluation arises from the architecture of a system as shown in Fig. 2. There is much to be learned, for example, about teaching strategies from interrogating both the tutoring model and the user of the system.

## 5. Applying the proposed evaluation method to intelligent tutoring systems for gaming-simulation: The case of intuition

Existing intelligent tutoring systems are grouped into generic categories by the approach which they follow in tutoring a certain topic. These approaches include tutorial dialogues, drills, simulations, instructional games and gaming-simulations. INTUITION, which falls under the generic category of gamingsimulations 22,23 , will be used as the testbed for<sup>w</sup> <sup>x</sup> applying the proposed evaluation method. Gamingsimulations have become particularly popular for the purpose of management education 8 . INTUITION is such a business gaming-simulation which teaches principles and skills in areas such as marketing, production, stock control and labour relations.

Gaming-simulation is a hybrid form, involving the performance of game activities in simulated contexts. A gaming-simulation may be viewed as a device which provides for both the simulated real world and the recreational character of games. A gaming-simulation works wholly or partly on the basis of players’ decisions in which the activities of participants have the characteristics of games: players have goals, sets of activities to perform, constraints on what can be done, and payoffs good and Ž bad as consequences of the actions. The elements in. a gaming-simulation are patterned from real life: roles, goals, activities, constraints, and consequences, and the linkages among them simulate those elements of the real-world system. A gaming-simulation generally incorporates the following concept <sup>w</sup> <sup>x</sup> 25 : the participant adopts a role which is the representation of a role in the real world. He is left to make decisions within the setting in which he finds himself and experiences simulated consequences as a response to his decisions. He may observe the consequences of his decisions and reflect on the relationships between his decisions and their consequences.

The internal evaluation of INTUITION involves an examination of how its architecture supports tutoring. It examines the domain, student and tutoring model with respect to what behaviour INTUITION can possibly exhibit based on the knowledge it entails. Internal evaluation also examines INTUITION’s processes to determine how the observed behaviour is provided. Tutorial domain analysis, which draws conclusions about INTUITION’s overall tutoring approach, is integrated into the external evaluation of the learning achievement.

The external evaluation examines the educational impact of tutoring on students and the learning achievement. It examines whether a student feels that INTUITION provides satisfactory tutoring. The external evaluation was carried out with a group of 16 postgraduate students under the supervision of the system developer. The students were provided with both a detailed description and the rules of the business simulation–game in advance of the experiment. During the experiment, students interact with INTUITION in groups of two or three players per game. The students have the option to upgrade their advancement stage after they have completed their first game and thereby gain some understanding about business management strategies and techniques. After the completion of a minimum of two games, the students were asked to give feedback on INTUITION’s tutorial features and abilities by filling in a questionnaire. A copy of the questionnaire can be found in Appendix A of this paper. Learning achievement was assessed when the players were requested to repeat some tasks in consecutive business quarters.

The main part of the remaining section addresses the issues discussed in the section on complete tutoring systems above. The answers to the evaluation questions of knowledge level analysis and program process analysis of Fig. 3 are integrated with the answers to the evaluation questions on INTUITION’s learning affect. This fusion of the internal evaluation of INTUITION’s architecture with the external evaluation of INTUITION’s learning affect provides an overall evaluation of complete tutoring.

The section then discusses INTUITION’s learning achievement based on the feedback provided by the students who examined INTUITION. It also addresses tutorial domain analysis, i.e., it presents the overall capabilities and limitations of the system’s tutorial operations which have arisen form knowledge and process analysis during the internal evaluation.

The final part of this section draws together all evaluation outcomes and discusses the suitability of the proposed evaluation approach for the purpose of examining complete intelligent tutoring systems.

## 5.1. INTUITION’s domain model

INTUITION’s domain model includes knowledge about management approaches and strategies in form of rules, management techniques and examples of tasks that have to be carried out within the game. In this way, students may be presented with alternative explanations of the same concept or referred to relevant rules or examples in the domain model. INTUITION does not account for knowledge that lies outside the domain of business management. However, none of the students who interacted with INTUITION expressed a need for information on or help with issues outside this domain. Although the scope of INTUITION’s domain model does currently not go beyond the domain of business management, it may easily be expanded should the need for an extension of the subject domain arise.

The domain model also contains knowledge about common missing concepts and misconceptions which have been encountered as the cause of errors by tutors who used the paper-based version of the Metal Box Business Game 4 with students and trainee <sup>w</sup> <sup>x</sup> managers. INTUITION stores this knowledge in the library of misconceptions and missing concepts of its domain model. Each detected error is diagnosed and related to a misconception or missing concept which is then remediated.

Students acquired a good understanding of the concepts to be learned through the explanations, exercises and examples the system was able to offer. It was mentioned that some explanations of concepts could have been more ‘detailed’ and that examples did not always relate directly to problems to be solved. However, students generally agreed that the system provided ‘useful suggestions and examples’.

## 5.2. INTUITION’s tutoring model

INTUITION’s tutoring model provides a variety of teaching strategies which use the different presentations of the knowledge in the domain model. IN-TUITION makes use of the following teaching strategies within its tutorial intervention.

Cognitive apprenticeship. This strategy is based on the idea that cognitive skills can be learned in the same way as an apprentice in the crafts learns, i.e., by watching an expert in action and asking questions. The apprentice starts with the performance of small separate tasks which are gradually increased in size or linked to other tasks until the apprentice is able to perform the entire task by his or herself.

Reteaching. The player is presented again with those rules of the game that represent the prerequisite knowledge for the task he has been found to have a problem with.

Successive refinement. This strategy is based on the principle that the material to be taught should be explained to the student in steps with gradually increasing levels of detail. This way the student is provided with an initial framework into which subsequent teaching of the domain can be fitted.

Practice. The student is presented with a problem on the screen and is asked to carry out a task.

Demonstration. Presenting the student with an example–demonstration forces the student to go through the correct reasoning process 1 . <sup>w</sup> <sup>x</sup>

Socratic hinting. Socratic hinting attempts to place the user in a specific frame of mind 24 . For this<sup>w</sup> <sup>x</sup> purpose, the system provides the student with short reminders or questions which force him to reason about what he or she does and does not know.

All these strategies are provided by INTUITION’s tutoring model. The tutoring model provides knowledge about the choice of strategies that can be applied with a particular concept to be learned or a misconception or missing concept to be eliminated. Overall system control directs the selection process of the most suitable remedial strategy from this range. Apart from the format in which a concept is presented within the regular tutoring interaction, IN-TUITION’s domain model stores additional domain knowledge in formats which provide for the presentation of remedial information of alternative textual explanations, gamed examples and related exercises.

Students noticed the use of different teaching strategies when interacting with INTUITION. Hints, suggestions, demonstrations, practice sessions, the presentation of rules, and explanations were the methods the system used according to the students. However, the teaching strategy selected by the system was not always considered most favourable by the student. This suggests the need for further research on the strategy selection algorithms.

## 5.3. INTUITION’s student model

INTUITION’s student models provide knowledge about the needs and preferences of the student. Apart from a history of interaction and an overlay model, INTUITION keeps a detailed chronological record about detected errors and all remedial interventions carried out for every player.

For a newcomer to the game, the advancement stage is automatically set to novice. At the beginning of any subsequent game, the student is asked to select the level of advancement he believes is appropriate for his knowledge and experience with the game.

A tutoring strategy is selected according to the advancement stage of the player. If a role is played at the advanced level INTUITION avoids unnecessary detailed explanations. This approach is based on the view that more advanced students generally do not require detailed explanations, but are able to apply the necessary interpretations themselves <sup>w</sup> <sup>x</sup> 26,27 . Socratic hinting is a strategy which typically helps to focus the student’s attention onto the relevant aspect of a concept or problem leaving the student to then apply his own interpretation to determine the solution or the cause of the problem 24 .<sup>w</sup> <sup>x</sup>

At the novice level, INTUITION provides the student with more detailed explanations about a concept or problem. If the concept to be taught or the student error to be repaired for a novice player allows the application of more than one strategy, the strategy is selected according to the student’s needs and preferences. The mechanism used to choose a strategy follows the concept of learner control with guidance. INTUITION provides the student with a choice of teaching methods which imply the use of a specific strategy. If the student’s chosen method does not lead to the acquisition of the knowledge to be learned, INTUITION itself decides on the strategy to be used next. With this approach INTUITION takes into account the needs and preferences of the student by selecting the strategy which has proven to be most successful with the student in previous tutorial interventions.

Students generally agreed that the system took account of differences in their advancement stages and both advanced and novice players considered the tutoring and the remediation provided helpful. The students felt that the explanation of basics and the use of simple examples provided adaptive tutoring at the novice level. Furthermore, novice students in particular welcomed the opportunity to test and consolidate their knowledge in extra practice sessions.

Students recognised a change in the teaching method used when the same mistake was repeated. Although students did not seem to notice a particular pattern in the sequence of teaching strategies applied, the approaches used were mainly considered helpful, but not always most appropriate. It was noticed that INTUITION switched the advancement stage back to the novice level when a mistake was repeated at the advanced stage.

Most students encountered and welcomed situations in which they had the opportunity to determine their method of tutoring. It was pointed out that the options provided allowed the system to maintain control over the tutoring session, but that within this control the system determined what was ‘best for the player’ before allowing the student to express his preference. One student denied having been offered any choice by the system, but argued that the system nevertheless provided ‘good guidance’.

## 5.4. INTUITION’s oÕerall system control

INTUITION’s overall system control coordinates the three knowledge and process models in order to provide satisfactory tutoring to the student.

Any remedial intervention is carried out when the system recognises the student’s need for it. A business quarter within INTUITION is divided into seven steps of play which are linked in order of the sequence of the decisions to be made. Due to the business management character of the simulationgame, the decisions within a specific step of play may be interrelated and influence each other. INTU-ITION, therefore, waits for the student to complete his step of play, i.e., it waits for the student to complete all decisions to be made within a step of play and to finalise his decisions before it intervenes, i.e., before it detects and diagnoses any possible errors.

The majority of students who used INTUITION regarded the time of remediation as appropriate. None of the students questioned ever felt that they w ere interrupted unnecessarily and that INTUITION’s remediation was not required. However, it was suggested to provide a facility for optional help before a decision is finalised. Also, it was pointed out that more immediate remediation would have been helpful in situations in which the committed error did not relate to other decisions within the same step of play e.g., a novice financial director Ž would have preferred the remediation of any independent errors on the revenue and expenditure statement before moving on to the calculations on other operating statements . INTUITION does not provide. immediate remediation for errors which occur independently of other decisions or actions taking place within the same step of play.

A further interesting outcome from the external evaluation of INTUITION was the suggestion to reduce the chance of committing an error through criticism or advice given by the system before the student had to finalise his decision.

It can be concluded that in the case of INTU-ITION the delayed approach to treating errors is largely justified, because delayed remediation has the advantage that the error may be detected and pointed out to the student. At the same time, delayed remediation forces the student to rethink the overall step of action instead of creating local sub-optimal solutions <sup>w</sup> <sup>x</sup> 24 . However, INTUITION could improve its timing of remedial interventions by considering the needs of the novice student who might be in demand of more immediate help, especially at an early stage when he is still unable to understand the interrelatedness of decisions within an entire step of play. Offering remediation to the student before an error has been committed is an issue of error avoidance rather than error correction. However, the use of preventive methods might be an issue for further research.

Also, INTUITION does not provide remediation on student requests. Although students were unable to trigger a remedial intervention themselves, the majority of students recognised that help could be acquired by making use of the facility to view the rules of the game at any stage within the game, thus allowing players to refer to regulations and operating examples before they made a decision. However, it was pointed out that a more context-sensitive help facility would have been beneficial. INTUITION lacks the ability to refer the student directly to the rule that is relevant to the student’s problem in hand before the student has finalised a decision. This leaves a student to browse through the rules without further guidance. However, most of the time students were not aware of a problem before they committed a mistake and consequently had to rely on the system to point out their mistakes to them.

Pro-active instruction is the obvious approach for a gaming-simulation like INTUITION where the players are expected to learn from the reaction of the system and decisions have to be viewed within the context in which they are made 8 . After a remedial intervention, INTUITION takes the student back into the game where he is given the chance to correct his decision. Student-invoked remediation, therefore, is neither required nor appropriate in order to avoid undesirable results due to insensible decisions. The student may reconfirm or supplement his knowledge from the rules to which permanent access is provided.

## 5.5. Learning achieÕement through tutoring with IN-TUITION

The evaluation of the learning achievement examines whether, after the tutorial intervention, the player understands the skills and knowledge he was supposed to acquire. Here, the external evaluation of learning achievement is coupled with tutorial domain analysis. Tutorial domain analysis addresses the internal evaluation question of what INTUITION should do.

In order to assess whether INTUITION has led the student to understand the aspects of the game he should have learned, a game situation has to be designed that requires the student to use those aspects in a different context. INTUITION provides this game situation through its inherent quarterly structure, i.e., its recurring playing cycles. Every new quarter within a game provides the student with a game scenario in which the player has the opportunity to apply his acquired knowledge. The players student models record whether the player is able to apply his knowledge successfully. If the student can solve the problem, i.e., if he can apply the knowledge and skills in the scenario presented to him, the system can be considered as having contributed towards the learning achievement of the student.

The results from the observation of the student’s performance during the experiment and the investigation of the student models afterwards correspond with the feedback from the players. Players were asked whether INTUITION provided useful tutoring, to which the majority of players claimed that INTU-ITION provided useful tutoring ‘most of the time’ Ž . 56% . Thirty-eight percent of the answers were ‘sometimes’. The remaining players claimed that tutoring was ‘always’ helpful. More significantly, the answer to the question of whether players were able to apply their newly-acquired knowledge successfully in a subsequent quarter were restricted to ‘always’ 50% , ‘most of the time’ 31% and ‘some- Ž . Ž . times’ 19% . Consequently, overall tutoring with Ž . INTUITION can largely be considered as successful.

However, feedback from some of the players indicated that INTUITION’s tutoring could possibly benefit from the incorporation of more motivational issues. Although ‘entertaining and informative’ was a term to describe the general view of INTUITION’s tutoring, some of the players displayed signs of decreasing interest and motivation at some stage in the game. Internal evaluation shows that INTU-ITION does not support the maintenance of motivation other than through student involvement. INTU-ITION does not take account of individual personal differences between players which may indicate how a particular player may be kept interested and motivated. A system could adapt to such individual differences through actions, such as avoiding a certain task or concept temporarily or congratulating a student on a small success 26 .<sup>w</sup> <sup>x</sup>

A further issue which arose from the overall external evaluation and which provides a suggestion for the possible refinement of the approach with which remediation is carried out is the aspect of remediation before an error occurs. INTUITION offers delayed remediation. However, students’ comments suggest the introduction of error prevention. Remediation may be carried out before the error can be committed in order to warn students about common errors. If students are made aware of errors in advance, they might not make the mistake.

## 6. How well does the evaluation method work?

The purpose of this paper is to develop a comprehensive evaluation method for the assessment of the complete usefulness of intelligent tutoring systems. The result of the evaluation shows that by and large, INTUITION offers satisfactory tutoring according to the tutorial qualities a complete intelligent tutoring system is expected to deliver. However, the evaluation also sheds light on various shortcomings of INTUITION: 1 lack of deep knowledge in theŽ . domain of business management; 2 lack of knowl-Ž . edge outside the domain of business management; Ž . 3 lack of links between the examples used, and the business problems addressed, by the system; 4Ž . students’ needs and preferences are not adequately considered in teaching strategy selection; 5 lack ofŽ . student-invoked help or remediation; 6 lack ofŽ . immediate remediation when the error does not effect other decisions; 7 lack of consideration of Ž . individual differences between players; 8 lack of Ž . motivational aspects. The internal evaluation of IN-TUITION covers all components of the intelligent tutoring system architecture, e.g., both the knowledge and processes of the system. The information obtained is detailed and comprehensive. It provides evidence that the evaluation method manages to reveal both shortcomings and accomplishments of the complete intelligent tutoring system architecture, including information on important issues, such as tutoring approaches, diagnosis and remedial tutoring, which are not addressed by evaluation methods such as those proposed by O’Shea 17 , Self 19 and<sup>w x</sup> <sup>w x</sup> Nwana 14 . A relevant example from the evaluation<sup>w</sup> <sup>x</sup> of INTUITION is the detection of the need for more detailed knowledge in the domain model. Furthermore, the evaluation investigates the tutoring approaches INTUITION offers based on its choice of teaching strategies, and it detects the need for refinement of the algorithm that selects a teaching strategy for a particular tutoring interaction.

The external evaluation of INTUITION reveals information about the behaviour of the system which other methods fail to detect. The external evaluation of INTUITION, for example, reveals issues such as the timing of remedial processes within the overall teaching interaction, the request by students for more context-sensitive help, and the suggestion to incorporate more motivational issues in order to improve the learning achievement.

The evaluation method proposed in this paper eliminates the weakness of system-tailored methods such as those proposed by Nwana 14 and Shute and <sup>w</sup> <sup>x</sup> Glaser 20 , by remaining system-independent in or-<sup>w</sup> <sup>x</sup> der to provide a tool for the evaluation of any intelligent tutoring system.

## 7. Conclusion

Intelligent tutoring systems have become increasingly widespread in teaching<sup>r</sup>learning environments. They promise to enrich the learning opportunities of students by providing individualised student guidance and support within a teaching<sup>r</sup>learning environment.

The evaluation of these educational systems is becoming increasingly important. Evaluation can serve as a tool to further research developments in the field of intelligent tutoring systems by providing suggestions for the overall improvement of the architecture and the behaviour of these systems. Although the significance of intelligent tutoring system evaluation has been recognised, only the recent literature gives evidence of an increased interest in the development of evaluation methods for intelligent tutoring systems 9,13 . However, the few evaluation propos- <sup>w</sup> <sup>x</sup> als that have been made generally represent methods which have been developed in an ad hoc manner. They fail to address the complete intelligent tutoring system architecture. Also, they tend to be tailored to a specific system and remain at a very general level.

This paper, therefore, proposes an evaluation approach that serves to deliver comprehensive feedback about a complete intelligent tutoring system, in order to account for O’Shea’s concern for wide and overall evaluation. The proposed method overcomes the vagueness of O’Shea’s 13 pillars by making the evaluation more specific to the intelligent tutoring system in question and at the same time allowing for detailed evaluation of specific features or components as suggested by Self. This method overcomes the weakness of the system-tailored methods of Nwana, and Shute and Glaser.

This evaluation method was used with the INTU-ITION system. The evaluation of INTUITION has shown that the evaluation method proposed in this paper overcomes the major weaknesses of other methods that have been developed.

## Appendix A. Questionnaire

## A.1. General

Ž . 1 What director roles were allocated to you? At what advancement level did you play: novice or advanced?

Game no. Director role played Advancement level 1 2 3 4 5

## A.2. System behaÕiour

Ž . 2 Did the system provide useful instruction?

I never

I seldom

I sometimes

I most of the time

I always

Ž . 3 Were you able to apply successfully the knowledge you obtained within a tutorial interaction in a subsequent quarter of the game?

I never

I seldom

I sometimes

I most of the time

I always

Ž . 4 Can the system answer arbitrary questions about the subject?

Ž . 5 Does the system teach prerequisite skills?

Ž . 6 Can the system give an explanation of a problem solution including one of a problem posed by the Ž user ?.

Ž . 7 Can the systems give alternative explanations, perhaps using analogy?

Ž . 8 Were you able to initiate some new area of investigation?

Ž . 9 Are the problems presented by the system adapted to the users’ needs?

Ž . 10 Does the system offer a flexible style of tutoring?

Ž . 11 Do the systems provide hints, pieces of advice, corrections, remedial demonstrations, traces of reasoning, interpretations, explanations, simulations, motivation?

Ž . 12 Was the system able to provide tutoring using alternative methods? Please list the methods.

Ž . 13 Did the system use different methods of remediation when you made a mistake? Please give example s . Ž .

Ž . 14 At any point, did the system allow you to determine the way you were tutored, or did you feel the system took over leaving you with no options? What were you allowed to do? Would you have liked to express any other preferences? Please give example s .Ž .

Ž . 15 Do the systems intervene if the user appears to be having difficulty?

Ž . 16 Did the system explain the cause of your mistakes or did it simply correct the mistakes? Please give example s .Ž .

Ž . 17 Are the system’s explanations tailored to the user?

Ž . 18 Is the system’s tutoring sensitive to the individual student needs and preferences?

Ž . 19 Does the system provide informative feedback? Ž . 20 Is tutoring tailored to your level of advancement? Please give example s .Ž .

Ž . 21 If you played at different advancement levels did you notice a difference in the tutoring methods used? Did you find the differences useful? Please give example s .Ž .

Ž . 22 Did the system intervene at a time at which you considered it useful or would you have preferred intervention at a different point in time? If the timing was inappropriate, when should intervention have taken place? Please give example s .Ž .

Ž . 23 Did you ever feel that the system interrupted you unnecessarily? When? Please give example s .Ž .

Ž . 24 Do the systems enable the student to communicate his plans i.e., intentions prior to executing Ž . them?

Ž . 25 Did the system provide you with a facility to call for help on issues that you did not understand? How? Please give example s . Ž .

Ž . 26 Please feel free to make any additional comments:

## References

<sup>w</sup> <sup>x</sup> 1 S.R. Alpert, M.K. Singley, J.M. Carroll, Multiple multimodal mentors: delivering computer-based instruction via specialized anthropomorphic advisors, Behav. Information Technol. 2 14 1995 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 M.C. Angelides, A.K.Y. Tong, Implementing multiple tutoring strategies in an intelligent tutoring system for music learning, J. Information Technol. 10 1995 . Ž .

<sup>w</sup> <sup>x</sup> 3 G. Beekman, Computer Currents—Navigating Tomorrow’s Technology, The Benjamin<sup>r</sup>Cummings Publishing, Redwood City, CA, 1994.

<sup>w</sup> <sup>x</sup> 4 Careers Research and Advisory Centre CRAC , Stelrad Ž . Limited The Metal Box Business Game, Hobsons Press, Cambridge, 1978.

<sup>w</sup> <sup>x</sup>5 D.W. Conrath, R.S. Sharma, Evaluation measures for computer-based information systems, Comput. Ind. 3 21 1993 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 B. Ives, M.H. Olson, J.J. Baroudi, The measurement of user information satisfaction, Commun. ACM 26 10 1983 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 R. Kaplan, D. Rock, New directions for intelligent tutoring, AI Expert 2 10 1995 . Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 D.C. Lane, On the resurgence of management simulations and games, J. Operational Res. Soc. 5 46 1995 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 P.J. Legree, P.D. Gillis, M.A. Orey, The quantitative evaluation of intelligent tutoring system application: product and process criteria, J. Artif. Intell. Educ. 2<sup>r</sup>3 4 1993 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 D. Littman, E. Soloway, Evaluating ITSs: the cognitive science perspective, in: M.C. Polson, J.J. Richardson Eds. ,Ž . Foundations of Intelligent Tutoring Systems, Lawrence Erlbaum Associates, 1988.

<sup>w</sup> <sup>x</sup> 11 M.A. Mark, J.E. Greer, Evaluation methodologies for intelligent tutoring systems, J. Artif. Intell. Educ. 2<sup>r</sup>3 4 1993 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 T. Murray, Formative qualitative evaluation for ‘exploratory ITS research, J. Artif. Intell. Educ. 2–3 4 1993 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 F. Ng, G. Butler, J. Kay, An intelligent tutoring system for the Dijkstra–Gries methodology, IEEE Trans. Software Eng. 21 5 1995 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 H.S. Nwana, The evaluation of an intelligent tutoring system, Intell. Tutoring Media 3 1 1990 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 S. Ohlsson, Knowledge requirements for teaching: the case of fractions, in: P. Goodyear Ed. , Teaching Knowledge andŽ . Intelligent Tutoring, Ablex Publishing, NJ, 1991.

<sup>w</sup> <sup>x</sup> 16 H.F. O’Neil, D.A. Slawson, E.L. Baker, Design of a domain-independent problem-solving strategy for intelligent computer assisted instruction, in: H.L. Burns, J.W. Parlett, C.L. Redfield Eds. , Intelligent Tutoring Systems: Evolu-Ž . tions in Design, Lawrence Erlbaum Associates, Hillsdale, NJ, 1991.

<sup>w</sup> <sup>x</sup> 17 T. O’Shea, R. Bornat, B. Boulay, M. Eisenstad, I. Page, Tools for creating intelligent computer tutors, in: A. Elithor, R. Banerji Eds. , Human and Artificial Intelligence, NorthŽ . Holland, London, 1984.

<sup>w</sup> <sup>x</sup> 18 E. Rich, K. Knight, Artificial Intelligence, McGraw-Hill, 1991.

<sup>w</sup> <sup>x</sup> 19 J.A. Self, Intelligent Computer Assisted Instruction, paper presented at the ICAI Spring Seminar, Logica Cambridge, UK, 1985.

<sup>w</sup> <sup>x</sup>20 V.J. Shute, R. Glaser, A large-scale evaluation of an intelligent discovery world: Smithtown, Interactive Learn. Environ. 1 19 1990 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 21 V.J. Shute, J.W. Regian, Principles for evaluating intelligent tutoring systems, J. Artif. Intell. Educ. 2<sup>r</sup>3 4 1993 . Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 J. Siemer, INTUITION—applying intelligent tutoring to gaming-simulation, J. CIT 3 1 1995 . Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 J. Siemer, M.C. Angelides, Evaluating intelligent tutoring with gaming-simulations, in: C. Alexopoulos, K. Kang, W.R. Lilegdon, D. Goldsman Eds. , Proceedings of the 1995 Ž . Winter Simulation Conference, Arlington, VA, 1995.

<sup>w</sup> <sup>x</sup> 24 B.G. Silverman, Critiquing Human Error—A Knowledge Based Human–Computer Collaboration Approach, Academic Press, London, 1992.

<sup>w</sup> <sup>x</sup> 25 J.L. Taylor, R. Walford, Learning and the Simulation Game, The Open Univ. Press, Milton Keynes, England, 1978.

<sup>w</sup> <sup>x</sup> 26 E. Wenger, Artificial Intelligence and Tutoring Systems— Computational and Cognitive Approaches to the Communication of Knowledge, Morgan Kaufmann Publishers, Los Altos, CA, 1987.

<sup>w</sup> <sup>x</sup> 27 R. Winkels, Explorations in Intelligent Tutoring and Help, IOS Press, Amsterdam, 1992.

<sup>w</sup> <sup>x</sup>28 R. Winkels, J. Breuker, What’s in an ITS? A Functional decomposition, in: E. Costa Ed. , New Directions for Intelli-Ž . gent Tutoring Systems, Springer-Verlag, Berlin, 1992.

<sup>w</sup> <sup>x</sup> 29 P.H. Winne, A landscape of issues in evaluating adaptive learning systems, J. Artif. Intell. Educ. 4 4 1993 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 30 B.P. Woolf, W. Hall, Multimedia pedagogues—interactive systems for teaching and learning, IEEE Comput. 5 1995 .Ž .

![](/api/attachments/7CVC6G96/fulltext/images/3670c97de625679d274ec2c74be03cbf03e264ad68c4832a83c5301f84589efd.jpg)  
Julika Siemer is a lecturer in Information Systems at the London School of Economics. She studied Informatics at Hildesheim University, Germany, and holds an MSc and a PhD in Information Systems both from the London School of Economics. Her major area of research is the field of intelligent tutoring systems where she has published extensively. She is a member of the ACM, the IEEE Computer Society, and the British Computer Society.

![](/api/attachments/7CVC6G96/fulltext/images/def83a4620dc0b7efab4edcafdbfb44e10a23f20cdf4456940864f54f9b8c9cb.jpg)

Marios Angelides is a lecturer in Information Systems at the London School of Economics. He received both his BSc and PhD in Computing from the London School of Economics. His major areas of research are multimedia information systems, information superhighways, and intelligent tutoring systems. He has published extensively in these areas, and he is the author of Multimedia Information Systems Kluwer Academic Pub-Ž lishers, 1997 . He is a member of the.

ACM, the IEEE Computer Society, and the British Computer Society.
