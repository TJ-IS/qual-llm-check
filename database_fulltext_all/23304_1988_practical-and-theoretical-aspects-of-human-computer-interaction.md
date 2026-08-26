---
otero_id: 23304
otero_key: "R6JAZ89A"
title: "Practical and Theoretical Aspects of Human Computer Interaction"
authors: "Peter Johnson; Hilary Johnson"
year: "1988"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1988.30"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Practical and Theoretical Aspects of Human Computer Interaction

Peter Johnson and Hilary Johnson, Department of Computer Science, Queen Mary College, University of London

## Introduction

What is the scope of human computer interaction? Human computer interaction (HCI) is concerned with the design, development and evaluation of computer systems, taking full account of the consequences for, and requirements of, the subsequent users. HCI is a special case of the more general topic area of the interaction between people and machines. It is special because HCI requires conceptual effort on the part of the computer user, while generally more physical or motor efforts are required on behalf of the machine user. Moreover, the interaction between people and computers differs from the interaction between people and other machines, in terms of the level of involvement in the task. A person's interaction with a typewriter is at a lower level of inclusion in the task of document preparation than it would be with a word processor. Another way to characterize this difference is in terms of the powerfulness of the computer as a tool, where one could argue that the word processor is a more powerful editing tool than the typewriter since it enables the user to carry out more editing operations.

There are three issues which seem to capture the essence of HCI, and which affect the power of the computer:

1. the tasks to which the computer should be applicable;

2. the characteristics of the software and hardware;

3. the characteristics of the people using the computer.

The first defines the range of applications for which the system is designed to be used. The second defines the system itself, and the third defines the known characteristics of the user population which will affect the usefulness of the system in a defined task. Together, all three define the limits to which a system will be useful for a particular type of task, performed by a person with a given set of characteristics.

As a consequence of the importance of the above three issues, it follows that one aim of HCI research is to design computer systems that function as powerful tools for people to use in carrying out their required and chosen tasks. HCI therefore is concerned with theories, models and methods for describing tasks, defining software and hardware, and characterizing people. In addition, if design is to be based on these three components, there must be a way of relating them together and applying them to the design, development and evaluation of computer systems.

It would be useful if there were a recognized design cycle into which HCI research could be easily accommodated. Unfortunately, there is no instantly recognized or universally agreed design cycle. However, it is possible to identify some activities that occur during the development of a computer system, although the ordering and number of iterations may vary. Four identified activities are:

\- analysing user requirements and user groups

\- specification of a design

\- development of a prototype

\- evaluation.

The aim and scope of HCI research can usefully be characterized by relating the previous issues of tasks, software/hardware, and people to the above development activities. Thus HCI research seeks to develop appropriate forms of:

-user models

\- task analysis

\- specification (both formal and informal) of interactions

\- prototyping user interfaces

\- evaluating designs for usability.

However, HCI research is concerned also with combining these various activities to produce usable systems. Consequently, there is an emphasis on fitting these components within the context of system development and transferring relevant research findings to both users and designers of computer systems.

The aim of this article is to review the major areas of research in HCI and to give instances of the current state of that research. The first section considers the concept of user models, followed by a discussion of task models and task analysis which comprises the second section. The third section is concerned with the role of formal methods in design specification. The fourth and fifth sections are concerned with the topics of prototyping and evaluation respectively. The direction of future research and the issue of technology transfer constitutes the final section of the paper.

## 1. User models

The term ‘user model’ has been misunderstood and abused perhaps more than any other term in HCI. Moran (1978) is partly responsible for this confusion; the command language grammar (CLG) is referred to at one and the same time as a user conceptual model (UCM) for the system designer, and also as a model of the user’s conceptual understanding of the system. It is highly unlikely that the system designer will have the same conceptual model of the system as the user, unless he or she is one and the same person. Young (1981) discusses thoroughly the concept of the UCM; he makes a distinction between four versions of the concept. First, the UCM of a user corresponds to the expectations and predictions that the user entertains about the device’s behaviour as a consequence of that person’s actions upon the device and second, the UCM of the psychologist or the researcher’s view of the user’s view of the system; third, the researcher’s version of the UCM is further differentiated from the designer’s view of the system and fourth, the previous three versions of the UCM, while differentiated from one another, can also be quite distinct from the system’s view of the user’s view of the system, such as might be the case in intelligent systems. To clarify the issue, in this paper the term ‘user’s model’ is reserved for the representation the user has of the system. The designer’s view of the system is termed the ‘design model’ which may be refined and simplified for presenting to a user; however, this is still a version of the design model and not a user’s model. One other use of ‘user model’ which needs clarification is the psychologist’s model of a user. This might be a simplified version of a complex psychological theory which the psychologist provides for the designer; it should be referred to as the ‘researcher’s model’, or the model of the user. The system’s model of the user is then best referred to in full, i.e. the ‘system’s model of the user’.

Current research on user modelling can be discussed relative to the four different uses of the term. However, these are not meant to be discrete categories, since some forms of model are classified under more than one category.

User models. This is the representation the person has of the system and, by definition, is not open to direct investigation. However, in evaluating a system it may be necessary to ask users what view or understanding they have of the system. Controversial issues about introspection need to be raised here, and the data from such reports have to be treated with caution. The previous use of introspection, was not scientific. It is hoped that now a researcher will have clear and precise hypotheses about what the user knows about the system which can be investigated by introspection methods. This method would not be used in isolation but might provide corroborating evidence to some other empirical evidence gleaned from a different source. The resultant model from those investigations becomes a version of the researcher's model of a user. A recent investigation attempted to manipulate the assumed user model by giving differing instructions and training material to users of a simulated system, (Kieras and Bovair, 1984). The results showed that a form of entity/function mapping was remembered better, learned faster and produced higher levels of performance than either rote instructions of operations or a 'fantasy model'. This line of research is a common approach in experimental psychology and it rests on the assumption that the user's mental representation is related to the instruction material.

Design models. This is perhaps the least active area of research in user modelling. The now classic approach has been the use of the metaphor as a design heuristic. The most well-known example of this is the 'desk-top' metaphor, currently employed on systems such as the Apple Macintosh. The role of metaphors in design is well documented by Smith et al., (1982) in a report of the design of the Star User Interface. Insomuch as the metaphor provides a simplified model of the design of the system for the user, it seems best to think of this as functioning as a heuristic to aid learning about the system. Research on metaphors has focused on identifying how a metaphor might function as a learning aid (Gentner (1983), Carrol and Mack (1985)). Of course, metaphors are not the only possible form of design model. Command language grammar (Moran, 1981) is described as a design model since it provides an abstract specification of the design at six different levels of abstraction. The use of models in the design process is centred on abstract specifications of a design. This topic is covered in detail in section 3.

Researcher's model. This is perhaps the most active area of current research in the area of 'user models'. The aim is to develop models of user behaviour that can predict or explain performance on a system. Card, Moran and Newell (1983) provided an early form of researcher's model, called the human information processing (HIP) model. This was an approximation over psychological theories of human information processing. The HIP model was used in conjunction with a form of task analysis (GOMS – see section 2) which allowed the analyst to predict performance times for various tasks by relating the output of the analysis to the HIP model. A more refined and less approximated model has recently been proposed by Barnard (1987) based on a view of cognitive psychology which assumes a number of interacting cognitive subsystems (ICS). As with HIP, ICS is intended to be used in conjunction with a task analysis to identify how tasks are performed and where difficulties may arise.

Systems model of a user. This is predominantly the area of 'intelligent systems', and more specifically 'intelligent user interfaces'. The most obvious application area for this type of model is in the design of intelligent tutoring systems, where the machine has some representation of the student's current understanding of the topic (Sleeman and Brown, 1979). In another context, designers have attempted to model some aspect of users such as their preferred style of interaction. It is useful to distinguish between models which attempt to capture the person's knowledge of the domain, such as in tutoring systems, and those which attempt to model some aspect of the user's knowledge of the system (as in intelligent interfaces to Unix, for example). In the latter case, Alty (1984) developed a form of path algebra for analysing the transitions through a network, where the system is assumed to be represented by some network diagram, the aim being to identify preferred and optimum routes through a system for particular classes of user.

## 2. Task models

Task models may be related to user models if the task model enables one to produce predictions of user behaviour. Here, three different types of task model will be considered:

1. Extant task models (ETM)

2. System task models (STM)

3. Interaction task models (ITM).

Extant task models (ETM) describe a person's behaviour using existing technology to achieve a desired goal. For example, if the goal was to draw money out of a bank account, the activities involved might include:

\- going to the bank with a cheque book;

\- asking the bank clerk how much money was currently in the account;

– deciding how much money to withdraw;

\- writing out a cheque;

-- handing the cheque to the bank clerk;

\- receiving and counting the money.

A model could be constructed to describe this task, in the form perhaps of a hierarchical task model showing the dependences, independences and interrelations of various subgoals and procedures involved in achieving the main goal (Annett et al., 1971). Alternatively, the knowledge used in performing the task might be characterized using task analysis for knowledge descriptions (TAKD) (Johnson, Diaper and Long, 1984a).

In TAKD the above scenario might be described in terms of the following Knowledge Representation Grammar (KRG) sentences:-

ENTER/ a BANK/ with a WITHDRAWAL TOKEN

REQUEST/ a STATEMENT/ from a BANKING
ASSISTANT/ from an ACCOUNT

RECEIVE/ a STATEMENT/ from a BANKING ASSISTANT/ for an ACCOUNT

CHOOSE/ an AMOUNT OF MONEY/ from an ACCOUNT

ENTER/ an AMOUNT OF MONEY/ on a WITHDRAWAL TOKEN

GIVE/ a WITHDRAWAL TOKEN/ to a BANKING ASSISTANT

RECEIVE/ an AMOUNT OF MONEY/ from a BANKING ASSISTANT

CHECK/ an AMOUNT OF MONEY/ against an AMOUNT OF MONEY/ on a WITHDRAWAL TOKEN.

Where the form of each sentence is:-
GENERIC ACTION/GENERIC OBJECT PHRASE:
GENERIC OBJECT PHRASE/GENERIC OBJECT
+ GENERIC OBJECT......

A sentence in a grammar comprises a generic action followed by a generic object phrase which comprises one or more generic objects detailing the object (direct), and an optional indirect object and agent. (The subject is assumed to be the person carrying out the action.) The generic action and objects are shown in upper case. These generic actions and objects are derived from specific instances found in the task domain (in this case, personal banking).

System task models (STM) describe a set of tasks a system can or might perform to assist a person in achieving a particular goal. This type of model is different from the ETM in that design decisions have been made about the extent of the computer application. The overlap between the ETM and the STM may be complete or only partial. In this case the model might describe the activities the system performs, such as:

\- accepting an identity code from a keyboard;

\- checking the code entered against a code on a card;

\- identifying the customer's bank account;

\- asking a customer what service is required;

\- accepting an input from a special function key;

\- asking a customer to key in an acceptable amount plus an enter command, etc.

The higher-level components of command language grammar (Moran, 1981) provide one example of the system task model.

Interaction task models (ITM) describe the activities or behaviour of the person using a particular interactive system to achieve some specified goal. The ITM can refer to an implemented system (or prototype system) or it may be derived from a design specification and an assumed set of activities. An example of an ITM of a cash dispensing system is given below:

\- inserting a card

\- reading a prompt

\- keying in a four digit identity number

\- reading a menu, etc.

There are many examples of this type of task model. Task action language (Reisner, 1981) uses a form of BNF notation to model the actions the user performs at a given interface. More recently, Payne and Green (1987) have developed task action grammar as a method of modelling the knowledge required by a person in carrying out a particular interaction. Perhaps the most well-known approach is the goals, operations and selection rules (GOMS) approach of Card, Moran and Newell (1983).

The relationship between an ETM, STM and ITM. The STM is not solely derived from the ETM; the designer may have views of what can be built into a computer system, leading either to an extension or a reduction in the task functionality of the system. With respect to the ITM, the STM provides the semantics for the command language through which the interaction tasks are performed. The command language must support the STM but again there may not be a direct mapping between the STM and the ITM. The ITM and the ETM relate the behaviour of the person in the extant technology to achieve a given goal, to the behaviour required of the person to use the computer system to achieve that same goal. The mapping between the ITM and the ETM may also be indirect. External/internal task mappings (ETIT) developed by Moran (1983) model the mapping relations between the extant task and the interaction tasks. A similar approach is provided by the task/action mappings of Young (1983).

Task analysis (TA), and the relationship between task analysis and task models. The method of analysing a task is in part determined by the particular type of task model that is to be developed. TA refers to the structure or organization that is imposed on a set of data to produce a task model, and the type of data that is collected. TA can be likened to parsing a sentence in terms of a predefined set of structures such as subject, object and verb. The analysis invariably includes some form of description, notation or language, such as BNF as used by Reisner (1981), to express or capture the analysis of the task.

Historically, TA developed from psychology, engineering, operational research and work study. There are a number of different approaches to TA and each approach carries with it assumptions about what aspect of behaviour is of interest, a method of collecting data about the given aspect of behaviour, a method of describing the analysed task and a method of analysing the task. From a psychological perspective, a person's behaviour associated with a particular task might be analysed in a variety of ways: for example, the time taken to perform some unit of the task, the psychological processes involved, or the knowledge that is required or recruited to perform the task.

Task analysis techniques either explicitly or implicitly include:

1. a method of collecting data;

2. a method of analysing the data;

3. a structure for interpreting the task data;

4. a form of expression for describing the task.

Similarly a task model includes:

(a) a definition of data;

(b) a set of principles for modelling the task;

(c) an output from a TA;

(d) a set of predictions about behaviour associated with the task.

Different approaches to modelling and analysing tasks. In this section some of the different approaches to task modelling and analysing are discussed in more detail.

The first approach to be considered is task analysis for knowledge descriptions (TAKD). Briefly, TAKD was developed originally as part of a method for designing a syllabus to identify training requirements in areas of information technology (Johnson, Diaper and Long, 1984a). More recently, the application of TAKD to other design areas, including interface design, has been considered (Johnson, Diaper and Long, 1984b; Johnson, 1985). The TAKD method of analysing and describing tasks involves (a) identifying the generic components of a task in terms of generic actions and objects, and (b) providing a form of notation for describing tasks. TAKD focuses on the identification of a set of generic actions and objects from a collection of informal task descriptions. These generic actions and objects are then used to redescribe the tasks expressed in terms of a KRG. The procedure involves:

\- identifying a representative set of tasks;

\- carrying out task analyses of the identified tasks;
- identifying the complete set of actions and objects used in all the tasks;

\- defining the set of generic actions and objects from the individual actions and objects;

\- re-expressing the tasks in terms of generic actions and objects using the syntax of KRG.

The advantages of this method are that first, it is a more explicit approach to task descriptions than was previously available, second, the analysis provides detailed descriptions of actions and objects and their relations; and finally, it permits the analyst to describe a task independent of any specific task environment. This last feature is important, since it allows the task to be described independently of particular actions and objects which might be artefacts of the technology. This independence is achieved by producing generic actions and objects from the specific actions and objects of the task and technology. The task is then redescribed using a grammar (KRG).

The process of TAKD consists of producing English language descriptions of task steps and abstracting from these the generic actions and objects to be used in the KRG sentences. For example, the task of writing a memo to a secretary could be described in terms of the following KRG sentence:

## CREATE/ a MESSAGE/ on a TEXT MEDIA/ with a HEADER (of TEXT) with a BODY (of TEXT) to a RECEIVER/ at an ADDRESS/ with a TEXT INPUT DEVICE.

The generic actions have a meaning that can be related to both entities and operations of (for instance) a newly designed electronic mail system, and to the particular actions and objects of extant tasks, such as pens, paper and written communications. There are a number of implications of this approach to HCI for the design of interfaces. One implication is that users' tasks are explicitly represented in the design of the interfaces. The designer can make use of the user's existing knowledge of the action and objects to define the relationship between the system entities and operations. Moreover, the designer has an explicit link between the user's existing environment and the new task environment. As a consequence the mismatch between the knowledge recruited by the user and the idealized system knowledge can be minimized. Finally, TAKD can be used to design training manuals and courses in accordance with its original usage.

Cognitive task analysis (CTA). Barnard (1987) proposes an approach to HCI known as cognitive task analysis (CTA), which attempts to represent tasks within the human-information-processing framework of cognitive psychology. Barnard therefore is concentrating on the underlying representation system of the person carrying out the task, rather than on details of the task itself. The human information processing system is assumed to be divided into a set of functionally independent subsystems each of which operates in a specific domain of processing. Associated with each subsystem is an 'image record' which preserves episodic memory traces appropriate to each domain. Sensory subsystems process incoming data in their domain, for example visual data, and then transform it into specific mental codes that are handled by other subsystems which specialize in the processing of higher-level representations. Effector subsystems process the output from representational subsystems and compute appropriate instructions to control motor output.

The framework of CTA is broad in that it includes many different cognitive processors, but it is also necessarily shallow in terms of the detail of how each processor functions, since the technique is to approximate over the details of psychological theory. The approach adopted by Barnard involves the developing of a task analysis with bottom-up constraints provided by empirical evidence, from individual pieces of research, and top-down constraints provided by the theoretical framework, such as processing constraints, knowledge representation, etc. The analysis involves describing a task within the cognitive subsystems mentioned earlier, then using empirically established mappings to furnish attributes relevant for user behaviour on the task, and then specifying a core set of intermediate principles to link data characteristics to the framework and domain of application. This is not a trivial task since a good understanding of psychological theory or empirical findings is required. There is, therefore, little chance of a designer using the technique in its raw form. One solution has been to develop a small expert system. The objective is to get the knowledge base to a point where it can build a model for the cognitive task analysis from some novel specification and which infers key aspects of user behaviour. The initial target would be to establish enough intermediate principles to handle a restricted set of cases. In principle, therefore, CTA establishes approximate relations between components of the model based on empirical evidence. These relationships used in conjunction with generalizable principles would enable the analyst to build a predictive model for a particular task.

Task action grammar (TAG). Payne and Green (1987) offer a formalism which is intended to model the mental representation a person would have of the interface language and therefore to allow a formal specification of the language as perceived by the user.

The notation they provide is a grammar describing a mapping from the user's task on to sequences of actions. A task is defined as a transformation from a given state to a goal state. In any particular example the TAG definition models the mental representation of a user who, for example, has learnt a number of commands. A 'simple task dictionary' represents all the tasks the user can routinely perform and defines each as a set of components. Rule schemas generate action specifications from simple tasks. Generalization is achieved in that the grammar allows the basic form of all task action mapping rules to be represented in a single higher-level schema. The following is an example of a task action rule schema for moving a cursor one letter or word, forward or backward:

\+ letter (Unit)

$$
\text { letter } (\text { Unit } = \text { char }) - > ^ {\prime \prime} \mathrm{C} ^ {\prime \prime}
$$

TAG's main empirical prediction is that, of two similar task languages the one which will be easier to learn and remember is the one with the fewer simple task rules. Therefore TAG could be useful for comparison purposes at the evaluation stage of design. TAG also makes predictions about the optimal strategies for abbreviating command names.

The main assumption underlying TAG that ‘simple tasks’ are in fact cognitive units (i.e. psychologically valid) is questionable. Moreover, one may also question whether simple tasks in combination make more complex tasks, and how more high-level goals are accommodated. There are also no suggestions in the approach as to how the analyst should determine what is a simple task, and therefore this may change not only from user to analyst but also from analyst to analyst.

Goals, operators, methods and selection rules. The GOMS approach is put forward by Card, Moran and Newell (1983). GOMS models are essentially intended to be practical engineering models which are tools for designers of computer systems. They are specifically concerned with predicting time requirements in error-free performance, and as such have only limited applicability. The models have their roots in human information processing accounts of cognitive psychology. The purpose of the models is to predict the time taken by an expert to complete a task. The authors assume that underlying users' behaviour is a small number of information processing operators. Moreover, users' behaviour can be described as a sequence of these operators. The model is additive in that the time the user requires to act is the sum of the individual operators.

The person's cognitive structure is assumed to consist of four components: a set of goals, a set of operators, a set of methods for achieving goals, and a set of selection rules for choosing among the competing methods for goals.

A goal is a symbolic structure that defines a state of affairs and determines a set of possible methods by which it may be accomplished. Operators are elementary perceptual, motor, or cognitive acts whose execution is necessary to change some aspect of the user's mental state or to affect the task environment. Behaviour is assumed to consist of the serial execution of operators. A method describes a procedure for accomplishing a goal. It is one of the ways in which a person stores knowledge of the task.

GOMS produces a family of models at a number of different levels of detail ranging from the goals and subgoals, to the finger and head movements at the keystroke level of analysis.

One notion central to the approach of Card, Moran and Newell is that of the 'unit task'. 'Unit tasks' are user-defined subtasks: in other words how the user decomposes the task into more manageable subcomponents. One problem here is that the designer may not in fact decompose the task into 'unit tasks' in the same way as the user. This is a problem similar to that of TAG and 'simple tasks', although the two are not identical constructs. While the GOMS approach has an explicit psychological model, its simplicity and assumptions about 'expert' performance make the approach of little practical value in many design settings. However, GOMS provide a framework for HCI which has influenced other work (including CTA, mentioned earlier).

Command language grammar (CLG) (Moran 1978, 1981) is called a grammar because it is argued that it can be used to generate a wide variety of command language descriptions. For Moran (1978) a CLG representation of a system is a description of the system as the user sees and understands it.

Therefore, the levels of description (see below) correspond to levels of representations held by users. He argues that the psychological hypothesis behind CLG is that it describes the user's mental model of the system. This mental model is also considered to be exactly what the designer of the user interface should be working with; consequently CLG is also structured to be useful during the system design process. There seems to be some confusion here between the actual user's mental model and the designer's model of the user's mental model; as mentioned previously it cannot be assumed that they are the same thing.

The dominant structural feature of CLG is its stratification into levels. The levels are ordered so that the description at each level makes only a few global assumptions about the system features described in subsequent levels. Each CLG system describes a class of systems that may be realized in many different ways at the subsequent levels, which describe narrower and narrower classes. CLG consists of sets of characteristic elements that define each of its levels, and a mapping that relates the elements at the different levels. Each level is a complete description of the system at its level of abstraction. CLG attempts to provide mappings between the descriptions which form part of a user's representational system and the components of the computer system.

The grammar consists of three components which are then further subdivided to give six levels of description:

CONCEPTUAL COMPONENT

Task level

Semantic level

COMMUNICATION COMPONENT

Syntactic level

Interaction level

PHYSICAL COMPONENT

Spatial layout level

Device level

The conceptual component contains the abstract concepts around which the system is organized. The communication component contains the command language and the conversational dialogue, and the physical component contains the physical devices that the user sees and comes into contact with. A CLG representation is made up of a sequence of description levels, each level being a refinement of previous levels. The task level describes the task domain addressed by the system, and the semantic level describes the concepts represented by the system. The syntactic level describes the command-argument structure, and the interaction level describes the dialogue structure. The spatial layout level is concerned with the arrangement of the input/output devices and the display graphics, with the remaining features described at the device level.

The definition of a task in CLG is informal. The task structure consists of a hierarchy of tasks and subtasks. Tasks are the specific goals that users set themselves. Task entities are the conceptual objects that are involved in the task environment and upon which actions are carried out.

One problem with CLG, admitted by Moran, is that there is no theory or method, such as a generative taxonomy for deriving the set of all possible tasks for a given system. Consequently, CLG provides a levels description of a design, but does not (a) identify how the design relates to the existing task requirements, or (b) predict how a user might perform a task using the designed system.

Task action language (TAL). This approach, expounded by Reisner (1981), is a system-oriented, interaction task model (ITM). It is appropriate for the ITM since it can provide a description of the activities or behaviour of the person using a particular interactive system to achieve some specified goal. Reisner's intention with TAL is to show that an action language can be formally described and that the formal description can be used to compare alternative designs for simplicity (ease of use), and consistency. Therefore, TAL may be useful in evaluating different designs in addition to providing input to the design process. Reisner is specifically concerned with 'action languages for interactive systems', i.e. the sequences of button presses, typing actions, etc. performed by a user interacting with a terminal. A user's actions at a terminal are consequently viewed as a 'language'.

According to Reisner there are three characteristics of a language which influence its ease of use:

1. the number of terminal symbols;

2. the length of the terminal strings;

3. the number and form of the (production) rules.

Rules in this context are described as sets of sequences of actions, and learning a language requires learning the rules. In her paper, Reisner (1981) provides a detailed comparison of two versions of an interactive colour graphics system for producing slides, ROBART 1 and 2. The terminal symbols for a grammar represent actions the user has to learn and remember, for example, to study the physical device in use for a particular action; 'physical terminal symbols' would be defined, e.g. the screen. To describe where the user was looking, a 'visual terminal symbol' would be defined. Finally, 'pure physical' action would be defined as 'action terminals', e.g. MOVE JOYSTICK. The physical and visual terminals could then be used to examine the assignment of function to hardware.

TAL assumes that the terminal symbols are cognitive components, and that the grammar is a cognitive grammar. There is no explicit cognitive theory to support this assumption.

Reisner argues that one possible metric, to evaluate designs for ease of use, would be to count the number of alternations required for the terminal strings under study — i.e. the more changes in hand and eye position required, the more difficult the design. Furthermore, Reisner contends that the more predictable a design, in terms of knowing some rule(s), the easier it should be to learn.

There are a number of reservations about Reisner's work. Reisner (1977) has argued that the natural complexity of a statement might be the number of rewrite rules which may be used to describe the statement. Unfortunately, this assumes that complexity can be captured by the number, or even the nature, of rewrite rules. In other words, there is no psychological theory which underlies Reisner's assumptions. The problems are these: first, she is assuming that increasing complexity dictates that a language is harder to learn; second, she is assuming that complexity can be captured by the number of rewrite rules (when it could be that four difficult rewrite rules are more complex than six easy rewrite rules) for which there is no theoretical basis; and finally, she is assuming that the scale of complexity in terms of the number of rewrite rules means that four rewrite rules are twice as difficult as eight rewrite rules. A similar problem surfaces in the TAG grammar where again it is assumed that complexity is captured by the number of rewrite rules.

<table><tr><td>ETM</td><td>TAKD</td></tr><tr><td>ITM</td><td>GOMS*, CTA*, TAL, TAG</td></tr><tr><td>STM</td><td>CLG</td></tr></table>

\* indicates that the approach contains an explicit psychological theory or framework from which behavioural predictions can be derived.  
Figure 1. Summary of the reviewed approaches to task analysis

Figure 1 summarizes the various methods of TA considered in this paper, in terms of their intention to model extant, interaction or system tasks. Clearly, the predominant effort has been concerned with modelling the interaction that a person must carry out in order to use a designed system. Of those reviewed only TAKD attempts to analyse a set of extant tasks as a basis for generating a design, but there is no principled way to transform the output from TAKD into a design at present. CLG is more accurately reflected as providing an STM, but it might be argued that the interaction level of CLG describes an ITM. While this would be possible, CLG has not been used to describe an interaction task and does not make any predictions at all about behaviour. GOMS, CTA, TAL and TAG each describe an ITM and make predictions about user behaviour; however, only GOMS and CTA have an explicit psychological theory to support these predictions.

The next section is concerned with the role of formal methods in design.

## 3. The role of formal methods in design specifications

What constitutes a formal description of a system? One view is expressed by Anderson (1985) who presented a framework for the formal specification of interactive systems. Three major components were identified: the input syntax specification (which utilized grammar notation); the semantics (which consisted of a state set specification which specified all possible system states, plus meaning functions which map from the input syntax to their interpretation); and display specifications which specified how particular states should be mapped on to the available output devices. Anderson also provides a 'formal' definition of an interactive system. Briefly, an interactive system Sys is a six tuple:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$S_{ys} = &lt;G,S,M,O,D,I&gt;.$  where
 $G = &lt;T,N,P,Start&gt; - is a context free grammar$ 
defining the input
S = the set of system states
M = the meaning functions
O = the set of outputs or the output devices
D = the display function
I = the set of initial states.
</div>

Anderson's example specification is a file browser. The specification methods used were (a) BNF for syntax (b) direct definition for the meaning functions, and (c) algebraic (equational) specifications for the basic operations on the types comprising the state.

What are the advantages of using a formal specification? Cook (1986), in a paper which formally describes components of user interfaces, has outlined a number of reasons for using 'more formal' techniques. The first reason is that precise and unambiguous formal specifications provide a standard against which implementations of user interfaces may be judged, and can be used for the expression of such standards. Second, formal descriptions are amenable to the carrying out of proofs of formal properties. Third, formal descriptions can be free from implementation bias and uncommitted to any particular model of execution or architecture. Fourth, and more speculatively, formal descriptions potentially could be used to model and compare the expectations of various classes of user. This last reason for using 'more formal' methods assumes that users' expectations can be modelled in some way by formal descriptions and that the expectations of users can be compared via the medium of formal techniques. Cook (1986) argues that existing examples of generic user interfaces with any degree of complexity have often been implemented within object oriented programming (OOP) environments. It is claimed that OOP languages provide a useful and clear way of expressing the separation between interface and application.

Jacob (1986) has also considered the use of formal techniques within the framework of human-computer interaction. It is argued that previous user interface specifications have suffered because they lacked an acceptable language for describing the semantics of the interface; that is the actions that the system performs in response to the user's commands. Jacob suggests that designers should make use of a high-level model that describes the operations that the system performs. As a consequence, the user specification (Jacob does not say exactly what this is) would describe the user interface in terms of the model, while the internal details of the model would be described in a separate specification.

What are the ideal properties of a specification technique? Jacob (1986) has pointed out that one should seek certain properties when selecting a technique for specifying a human-computer interface. First, the specification should be easier to understand and produce than the software that implements the user interface. It should also be precise and easy to check for consistency. Second, the specification technique should be powerful enough to express non-trivial system behaviour with a minimum of complexity. It should be capable of separating what the system does (the function) from how it does it (implementation). Third, the specification should allow the possibility of constructing a prototype of the system directly from the specification of the user interface. Finally, the structure of the specification should be closely related to the user's mental model of the system itself. In Jacob's words, the principal constructs of the system should represent concepts that will be meaningful to users — for example the user answering a message — rather than internal constructs required by the specification language. In order to achieve this, in our view, an analysis should be carried out of what the user expects of the system. The user has a conceptual model of the system which relates to previous experience with other systems and which also relates to how the user's task is carried out when not using a computer. The more correspondences between the user's existing knowledge and the knowledge required when using a computer system generally means the easier the system is to use. To achieve this a task analysis of the user's task 'in the real world' should be carried out. However, it is questionable if this analysis can or should be in terms of a formal specification.

Different approaches to formal specification. According to Guttag (1986) there are many possible approaches to the formal specification of abstract types. Most can be placed in one of two categories: operational or definitional. In an operational specification, instead of trying to describe the properties of the abstract type, one gives a recipe for constructing it. With an operational specification the properties of the abstract type are inferred from the properties of the operational model. The main problem with this approach seems to be that as the number of operations grows a problem arises, because the relations among the operations are not explicitly stated and inferring them becomes combinatorially harder. In a definitional specification, one explicitly lists properties required for the values and operations forming the abstract type. For Guttag, the primary advantage of this mode of specification is that it tends to define the type quite generally, in that only the essential characteristics need be specified. The specification is thus an abstraction encompassing a relatively large class of implementations. One approach to definitional specification is the mathematical notation known as 'Z'. Sufrin (1986) used this notation in an attempt to develop a specification and formalize the design of an implementation, with the intention eventually of establishing its correctness by a proof. Sufrin's example was an office system which provided a variety of methods of composing and storing documents, and transmitting them between individuals. The main objective of the study was to demonstrate the separability of the implementation from the user interface.

Specifications - a formal or an informal approach? Gehani (1986) compared formal and informal specifications of the EVENT LOG subsystem of the change management automatic build system (CM ABS). Gehani argues that formal specifications cannot replace informal specifications; rather they should be treated as complementary. Ideally, system specifications should include both formal and informal specifications. The informal are easier to read and understand while the formal specifications tend to be clearer, more precise and unambiguous. Whenever there are doubts about the informal specifications, the formal specifications should be used to resolve them. However, formal specifications do not allow (according to Gehani) the specification of behavioural characteristics of systems such as storage requirements or input and output characteristics. We would add that formal specifications do not characterize the behavioural aspects of usability since there are none that are derived from any theory of users or usability. Work is currently in progress in this area, however, in the form of GUEPS (Harrison and Thimbleby, 1985), which takes 'intuitive' principles of usability and demonstrates by means of a formal proof how these can be shown to be present or absent in the design. The weakness in this approach is twofold — first, the principles are intuitive; second, the relation between the principle and the property to be proved is largely subjective and intuitive.

In a slightly different vein, Abbott (1983) has put forward an approach to programme development and specification which consists of three steps. The first step is to develop an informal strategy for a problem which should state the problem solution on the same conceptual level as the problem itself. It should be expressed in problem domain terms. The second step is to formalize the informal strategy. Unfortunately, the formalization may not in fact capture the exact nature of the informal strategy. However, Abbott contends that the solution can be formalized by formalizing the data types, objects, operators and control constructs. The final step consists of segregating the solution into two parts: a package and a sub-program, or collection of subprograms. The package would contain the formalization of the problem domain, i.e., the data types and their operators. The sub-program(s) will contain the specific steps for solving the particular problem.

In summary, research on specification in design is encouraging, in that it is now recognized that designs can be usefully specified in a formal and informal manner, and that both types of specification are of use. The main limitation of informal specifications is their inability to support mathematical proofs. However, not everything to be specified can be proofed or captured in a formal way, so some aspects of the design (namely the user interaction) are necessarily specified informally.

## 4. Prototyping and its relation to HCI

The topic of prototyping is not divorced from the notion and use of formal methods in design, since it is advantageous in rapid prototyping to separate the development and implementation of the user interface from computational aspects of the system. In the previous section we made the point that a good design specification using formal methods allowed one to separate the design from the implementation of the system.

Prototyping is becoming increasingly important in HCI research. From the design point of view a prototype is basically a first version or attempt at building a computer system; it provides designers with a view, or way of thinking, about solutions to problems. Generally, a prototype has to be quick to build and be 'throwawayable'. It enables designers to check out their designs for potential problems; for example, it might take 10 minutes for a page of text to format. Therefore, the prototype is useful for other logistic aspects of the design process as well as those which are directly related to usability.

From the HCI viewpoint, prototypes are important since they allow human factors people to assess the interface design for ease of use prior to the final version of the system. Here, we are overlapping the territory of evaluation. Prototyping is a prerequisite for most current forms of evaluation, and evaluation is primarily concerned with usability. A number of prototyping techniques are now considered.

Wasserman (1984) has investigated the role of prototypes in HCI. He argues that there are several reasons for building prototypes. First, it enables the user to evaluate the interface in practice and to suggest changes. Second, it allows the developer to evaluate user performance with the interface and to modify it to minimize user errors and improve user satisfaction. Third, it facilitates experimentation with a number of alternative interfaces and modification of those interfaces, and reduces the likelihood of project failure. Finally, it gives users a more immediate sense of the proposed system and thereby encourages them to think more carefully about the needs and desirable characteristics of the system.

Wasserman is concerned with an interactive information system which provides its users with conversational access to data. The user software engineering (USE) methodology, described by Wasserman, was developed to support the specification, design and implementation of interactive information systems. The goal of the USE methodology is to involve the users effectively in the early stages of the development process. The following are the steps that comprise the USE methodology:-

1. requirements analysis – activity and modelling leading to preliminary informal specification, identification of user characteristics;

2. external design - specification of user/program dialogue and interfaces;

3. creation of a prototype of the user/program dialogue with revisions as needed;

4. completion of the informal functional specification of the system operations using narrative text;

5. preliminary relational database design;

6. creation of a functional prototype system, providing at least some, and possibly all, of the system's functions;

7. formal specification of the system operations using behavioural abstraction;

8. system design at the architectural and module levels;

9. implementation of above (5,6 and 7);

10. test and/or verification.

Wasserman saw the need for a tool that would help in the evaluation of the user interface, from the perspective of both the user and the developer. This need led to the creation of RAPID/USE, which originally was envisaged as a tool for experimenting with user interfaces to systems. Wasserman chose transition diagrams, in preference to BNF, as the basis for specifying user interaction in systems, mainly due to readability considerations.

Basically, a transition diagram is a series of nodes and directed arcs. In an interactive systems application, a message may be displayed at any node. An arc is selected and traversed based upon user input. Actions are associated with traversal of the arc and the terminal is then in the state represented by the node at the end of the arc. Actions are specified informally with a narrative, or more formally using a formal specification language. Together with the specification of user input that 'caused' state transitions and the messages displayed at specific nodes, a complete system specification could be produced. RAPID/USE was developed to provide a way of building a prototype of the user interface, and also to provide a way to determine the quality of the user interface design: it allows only textual dialogues to be prototyped, since there is no graphics capability. RAPID/USE allows a straightforward encoding of USE transition diagrams and subsequent interpretation of the encoding to provide an executable version of the dialogue design. RAPID/USE consists of two parts: a transition diagram interpreter (TDI) and an action linker. The TDI checks the specification of a set of USE transition diagrams and executes the specification. Input to TDI is a set of transition diagram descriptions: this input file is known as a 'TDI script'. The TDI script is a translation of the transition diagrams themselves. A major reason why RAPID/USE was built was to allow evaluation of the human computer interface.

Bird and Schofield (1985) describe a software tool called inSET (Software Engineering Toolkit) which was designed to enable programmers to model the interaction between a user and the application program(s). They argue that skeleton code can be generated automatically to a known structure, simplifying prototyping. The main benefit which seems to be available through inSET is the ability to generate code quickly, enabling the rapid production of a prototype. The software development aids which comprise inSET divide into two classes: those which help generate code (development utilities) and those that can be used as part of the final packaging (building blocks). The intention was for building blocks to provide 40 per cent of the final code (although the actual figure was approximately 80 per cent), and consequently the developmental effort would also be reduced. The building blocks appear to be just packages of code which will slot into particular applications. Using inSET is much like using a statistical cookbook. Any function that could occur in several different projects is a suitable candidate for a building block. Designers however, have to be sure that the codes provide what is needed and that they are appropriate for particular applications — otherwise they have to write their own library of routines.

Finally, another approach more pertinent to HCI is that of EASIE (MacLean, Barnard and Wilson, 1986). MacLean, Barnard and Wilson attack techniques such as RAPID/USE because they believe them to be severely restricted since they are optimized to operate over a very limited domain (in the case of RAPID/USE, the domain is database retrieval). As human factors researchers, the authors argue that they are operating with a different set of constraints; first, they want to test multiple interfaces for a single application and second, they want to test an interface on real users. EASIE was developed to satisfy these criteria. It consists of three distinct layers. The bottom layer handles the basic functionality such as formatting text: it is written in C. The dialogue specification makes up the further two distinct layers — the dialogue script (DS) and the dialogue interface (DI). DS is a text file and provides a very simple description of the structure and content of the dialogue. DI looks after functions such as presentation style, form of interaction with the system and mapping on to basic functionality. The simplicity of the DS and the fact that a new DS can be edited and loaded into the main application while it is running means that it is possible to make rapid iterations around the dialogue design cycle. Another benefit is that because the DS is a separate file compiled into main application runtime, multiple interfaces can easily be provided to single applications. EASIE is in its infancy yet and is currently being used in running experiments comparing different dialogues and relating these to user goals.

## 5. The place of evaluation in design

It is important to realize at the outset that the role of evaluation may change depending upon when it occurs within the design process. Evaluation which occurs after a system has been built has two main functions — one important use of evaluation at this stage is in comparison with other already built systems. The comparison between ROBART 1 and 2 presented in Reisner's (1981) TAL paper is an instance of this type of evaluation. The other use of evaluation at this stage is in recommendations for the building of a new system which would build on the advantages, but cut down on the disadvantages, of the old system.

In preference when the system has been built, early iterative evaluation throughout the design process is to be recommended. This would result in the building of prototypes which could be evaluated in systematic ways. The cycle here might be construed as 'design-evaluate redesign'. This cycle involves monitoring the flow of the design process and checking on the validity and usefulness of the products of system development. The evaluation itself involves collecting together feedback from users which will be taken into account in fine tuning and further system development.

The key principles of evaluation, according to Gould and Lewis (1985) are early, interactive involvement of users, empirical measurement and iterative design. Hewett (1986), in a paper which considers the role of evaluation in design, recommends that designers when building a computer system should not only seek early involvement with users as part of the design team but that they should study a variety of possible system users as well. He terms evaluation of an already built system 'summative', and evaluation which occurs as part of the design process 'formative' evaluation. Hewett argues for the importance of iterative evaluation which he regards as the driving force underlying the process of successful design. The results of the system evaluation, during any stage of its design, shape the direction of the design and the changes taking place in redesign. The evaluation process, therefore, must be structured to create and maintain a clear focus on the goals of the project.

Evaluation should be considered early in the design process by identifying what is to be evaluated, at what stage of the design, and how this is to be carried out. Several questions arise when making these decisions — for example at a very early stage in the design the ultimate goal of the system must be agreed upon, and evaluated in some way. One question is whether or not the goal is a realistic one and is capable of some sort of measurement. Most measures involve either speed to complete some task, number and/or type of errors and, more subjectively, attitude questionnaires. The evaluation included in the RAPID/USE system, for example, involved the number of errors and help requests.

Evaluation may focus on a number of aspects of design: for example usability, learnability, acceptance and functionality. For each of these aspects an appropriate set of criteria against which to evaluate the relevant features and properties of the system need to be identified. Usability, for instance, might be evaluated against the criteria that a person of a given ability, with a particular skill level, could perform a given task on the system within some time parameter and with some level of error.

Very crudely, an ideal scenario for interface design might look something like the following:-

1. people's existing tasks are analysed, and any potential new tasks are considered;

2. a model and methodology that describe someone carrying out those tasks are developed;

3. the model has then to be passed on to the designer in some suitable form, agreed in advance between the task analyst and the designer;

4. the designer writes a design specification which is then passed on to someone who implements the specification;

5. a prototype is built and is evaluated;

6. iterative evaluation occurs until a state has been achieved which satisfies the designer's and task analyst's original and present goals;

7. the final system is built and then evaluated.

The purpose of evaluation in HCI is therefore to improve the usability of the system. One could argue that summative evaluation is the end of the design process and that to start again one goes back to comparing the final system with the expectations and predictions of the user. The system must take into account the knowledge people bring with them to the task, in terms of both the actions and the objects they are performed on, and also in terms of the sequence of carrying out the various sub-tasks that make up the task.

## 6. Future directions

The previous sections have focused on current research in a number of topic areas of HCI. The rationale for this choice of topic structuring was to relate HCI research to design activities. However, it is necessary to consider how each topic area interrelates with the other areas and whether or not they do provide an integrated approach to design. For example, research on task analysis and user modelling, in addition to investigating methods and types of analysis, or forms of models, should be directed toward the relation between task analysis and specifications, prototypes and evaluations. What are the consequences of a particular design method for other design activities? How can the output from an activity be used by another design activity? These are important questions to be asked of each of the research areas. For example, TA research must consider how the task analysis might influence other design activities, and what form the analysis must take if it is to be of use in the specification, prototyping and evaluation of the design. HCI research needs to be both theoretical and applied; it is of little use to the design team if the specification captures nothing of interest to any other design activity. In many cases research in HCI is beginning to recognize that good design is produced by a combination of differing skills and expertise. To enable these differing skills to complement each other, more effort is required to identify the necessary environments by which good design can flourish. Each activity is of equal importance in bringing about good design. However, each component activity needs to be communicated to others involved in the design. This means that an important aspect of design is communication between activities.

Within HCI research laboratories in industry and academia there is a new emphasis on ‘integrated design’. This has been achieved partly through the initiatives for collaborative research provided by government funding bodies such as ALVEY in the UK, and ESPRIT in Europe. Researchers from various backgrounds have grouped together with a common interest in good design. One example of this is a research project currently under way at Queen Mary College to develop a configurable structured message system (COSMOS). This is an ALVEY-funded research project bringing together computer scientists, psychologists and ergonomists from universities and industry. (The other partners in this research are Manchester University, Department of Psychology; Nottingham University, Department of Computer Science; British Telecom, Human Factors Division, and Computer Sciences Company Ltd.) In COSMOS teams of researchers are working together on the design, which includes a theory of structured communication, a taxonomy of communication tasks, a message kernel, a user interface and evaluations. In other areas similar interdisciplinary researchers are working together sharing in the development of HCI theory and methods.

The ultimate goal is to pass the research findings to industry. This can be achieved by getting industry involved in the research activities (as in ALVEY- and ESPRIT-funded research). In addition, smaller industrial companies who do not have the resources for such research projects need to be catered for. To fulfil this requirement a number of HCI centres are emerging to pass on the benefits of research to industrial clients. At present three such centres exist — the Scottish HCI centre, the London HCI centre and HCI Service (located in the Midlands). These, and hopefully other such centres, are aiming to provide an infrastructure by which HCI research can result in the design of better computer systems giving people more usable and powerful tools.

## Acknowledgements

The authors are grateful to ICL for funding, and colleagues at QMC for discussions concerning some of the ideas presented here.

## References

Abbott, R.J. (1983) Program design by informal English descriptions. Communications of the ACM, 26, 882–894.

Alty, J. (1984) The application of path algebras to interactive dialogue design. Behaviour and Information Technology, 3, 119–132.

Anderson, S. (1985) Proving properties of interactive systems. In M.D. Harrison and A. Monk (eds.) People and Computers: Designing for Usability. Cambridge University Press, Cambridge.

Annett, J., Duncan, K.D., Stammers, R.B., and Gray, M.J. (1971) Task Analysis. Training information No. 6, HMSO, London.

Barnard, P.J. (1987) Cognitive resources and the learning of human-computer dialogues. In J.M. Carroll (ed.) Interactive Thought: Cognitive Aspects of Human-Computer Interaction. MIT Press, Cambridge, Mass. (in press).

Bird, M. and Schofield, N. (1985) A practical approach to software engineering by using an interaction handler and skeleton code generator. Computer-Aided Design. October, 374–378.

Card, S.K., Moran, T.P. and Newell, A. (1983) The Psychology of Human-Computer Interaction. Lawrence Erlbaum Associates, Hillsdale, N.J.

Carroll, J.M. and Mack, R.L. (1985) Metaphor, computing systems and active learning. International Journal of Man-Machine Studies. 22, 39–57.

Cook, S. (1986) Modelling generic user-interfaces with functional programs. In M.D. Harrison and A. Monk (eds.) People and Computers: Designing for Usability. Cambridge University Press, Cambridge.

Gehani, N. (1986) Specifications: formal and informal – a case study. In N. Gehani and A.D. McGettrick (eds.) Software Specification Techniques. Addison Wesley, Woking.

Gentner, D. (1983) Structure-mapping: A theoretical framework for analogy. Cognitive Science, 7, 155–170.

Gould, J.D. and Lewis, C. (1985) Designing for usability: key principles and what designers think. Communications of the ACM. 28, 300–311.

Guttag, J. (1986) Notes on type abstraction. In N. Gehani and A.D. McGettrick (eds.) Software Specification Techniques. Addison Wesley, Woking.

Harrison, M.D. and Thimbleby, H.W. (1985) Formalising guidelines for the design of interactive systems. In P. Johnson and S. Cook (eds.) People and Computers: Designing the Interface. Cambridge University Press.

Hewett, T.T. (1986) The role of iterative evaluation in designing systems for usability. In M.D. Harrison and A. Monk (eds) People and Computers: Designing for Usability. Cambridge University Press, Cambridge.

Jacob, R.J.K. (1986) Using formal specifications in the design of a human-computer interface. In N. Gehani and A.D. McGettrick (eds.) Software Specification Techniques. Addison Wesley, Woking.

Johnson, P. (1985) Towards a task model of messaging: an example of the application of TAKD to user interface design. In P. Johnson and S. Cook (eds.) People and Computers: Designing the Interface. Cambridge University Press.

Johnson, P., Diaper, D. and Long, J.B. (1984a) Syllabi for training in information technology. In E. Megaw (ed.) Contemporary Prgonomics. Taylor and Francis.

Johnson, P., Diaper, D. and Long, J.B. (1984b) Tasks, skill and knowledge: task analysis for

knowledge descriptions. In B. Shackel (ed.) Interact 84. Elsevier, Holland.

Kieras, D.E. and Bovair, S. (1984) The role of the mental model in learning to operate a device. Cognitive Science, 8, 255–273.

MacLean, A., Barnard, P. and Wilson, M. (1986) Rapid prototyping of dialogue for human factors research: the EASIE approach. In M.D. Harrison and A. Monk (eds.) People and Computers: Designing for Usability. Cambridge University Press, Cambridge.

Moran, T.P. (1978) Introduction to the command language grammar: a representation for the user interface of interactive computer systems. Report SSL.78.3 AIP Memo 111.

Moran, T.P. (1981) The command language grammar: a representation for the user interface of interactive computer systems. International Journal of Man-Machine Studies, 15, 3–50.

Moran, T.P. (1983) Getting into a system: external-internal task mapping analysis. Proceedings of CHI 1983 Conference on Human Factors in Computing. ACM, Washington, D.C.

Payne, S. and Green, T.R.G. (1987) Task-action grammars: a model of the mental representation of task languages. Human Computer Interaction (in press).

Reisner, P. (1977) Use of psychological experimentation as an aid to development of a query language. IEEE Transactions on Software Engineering. SE-3, 218–229.

Reisner, P. (1981) Formal grammar and design of an interactive system. IEEE Transactions on Software Engineering, 5, 229–240.

Sleeman, D.H. and Brown, J.S. (1979) Editorial: intelligent tutoring systems. International Journal of Man-Machine Studies, 11, 1–3.

Smith, D.C., Irby, C., Kimball, R., Verplank, B., and Harslem, E. (1982) Designing the star user interface. Byte 7 April.

Sufrin, B. (1986) Formal methods and the design of effective user interfaces. In M.D. Harrison and A. Monk (eds.) People and Computers: Designing for Usability. Cambridge University Press, Cambridge.

Wasserman, A.I. (1984) Developing interactive systems with the user software engineering methodology. In B. Shackel (ed.) Human-Computer Interaction. INTERACT'84, North Holland, 611–618.

Young, R.M. (1981) The machine inside the machine: user's models of pocket calculators. International Journal of Man-Machine Studies, 15, 51–85.

Young, R.M. (1983) Surrogates and mappings: two kinds of conceptual models for interactive devices. In D. Gentner and A.L. Stevens (eds.) Mental Models. 35–52. Lawrence Erlbaum, Hillsdale, N.J.

## Biographical notes

Peter Johnson is currently a reader in the Computer Science Department at Queen Mary College, University of London. He gained a BSc in Psychology and Statistics from Salford University, and a PhD in Cognitive Psychology from the University of Warwick. He is involved in a number of research projects in Human Computer Interaction.

Hilary Johnson gained a first degree in Psychology and Statistics from Salford University, and a PhD in Cognitive and Developmental Psychology from Birmingham University. After four years at the Medical Research Council's Cognitive Development Department she joined the Computer Science Department at Queen Mary College, University of London in October 1986 as a post-doctoral research assistant.

Address for correspondence: Department of Computer Science, Queen Mary College, University of London, Mile End Road, London E1 4NS.
