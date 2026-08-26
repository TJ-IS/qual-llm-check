---
otero_id: 4390
otero_key: "NW9FUPZ7"
title: "Understanding Human Computer Interaction for Information Systems Design"
authors: "James Gerlach; Feng-Yang Kuo"
year: "1977"
journal: "MIS Quarterly"
doi: "10.2307/249456"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Understanding Human-Computer Interaction for Information Systems Design

By: James H. Gerlach
Graduate School of Business Administration
University of Colorado at Denver
Campus Box 165
P.O. Box 173364
Denver, Colorado 80217-3364

Feng-Yang Kuo
Graduate School of Business Administration
University of Colorado at Denver
Campus Box 165
P.O. Box 173364
Denver, Colorado 80217-3364

## Abstract

Over the past 35 years, information technology has permeated every business activity. This growing use of information technology promised an unprecedented increase in end-user productivity. Yet this promise is unfulfilled, due primarily to a lack of understanding of end-user behavior. End-user productivity is tied directly to functionality and ease of learning and use. Furthermore, system designers lack the necessary guidance and tools to apply effectively what is known about human-computer interaction (HCI) during systems design. Software developers need to expand their focus beyond functional requirements to include the behavioral needs of users. Only when system functions fit actual work and the system is easy to learn and use will the system be adopted by office workers and business professionals.

The large, interdisciplinary body of research literature suggest HCI's importance as well as its complexity. This article is the product of an extensive effort to integrate the diverse body of HCI literature into a comprehensible framework that provides guidance to system designers. HCI design is divided into three major divisions: system model, action language, and presentation language. The system model is a conceptual depiction of system objects and functions. The basic premise is that the selection of a good system model provides direction for designing action and presentation languages that determine the system's look and feel. Major design recommendations in each division are identified along with current research trends and future research issues.

Keywords: User-computer interface, user mental model, human factors, system model, presentation language, action language

ACM Categories: D.2.2, H.1.2, K.6.1

## Introduction

The user is often placed in the position of an absolute master over an awesomely powerful slave, who speaks a strange and painfully awkward tongue, whose obedience is immediate and complete but woefully thoughtless, without regard to the potential destruction of its master's things, rigid to the point of being psychotic, lacking sense, memory, compassion, and—worst of all—obvious consistency (Miller and Thomas 1977, p. 512).

The problems of human-computer interaction (HCI), such as cryptic error messages and inconsistent command syntax, are well-documented (Carroll, 1982; Lewis and Anderson, 1985; Nickerson, 1981) and trace back to the beginning of the computer revolution (Grudin, 1990). The impact of problematic HCI designs is magnified greatly by the advent of desk top computers, employed mainly by professionals for enhancing their work productivity. A faulty HCI design traps the user in unintended and mystifying circumstances. Consequently, the user may not adopt the system in his or her work because learning and using the system are too difficult and time-consuming; the business loses its investment in the system.

As concern about HCI problems grew, research was conducted by both practitioners and scholars to find solutions. Initially, researchers focused on enhancing programming environments in order to improve programmers' productivity. With the proliferation of desk-top computers, it was discovered that non-technical users were not satisfied with the same type of environment that programmers used. Research has since expanded beyond technical considerations to investigating behavioral issues involving human motor skills, perception, and cognition for developing functional, usable, and learnable software. HCI is now an important scientific discipline built upon computer science, ergonomics, linguistics, psychology, and social science.

Today's system designers are expected to apply these interdisciplinary principles to improve user satisfaction and productivity. This is a formidable task because HCI development is not an aspect of software design that can be illuminated by a single design approach. More importantly, there is a lack of guidance in applying HCI research findings to design practice. Consider a typical interface design based upon many decisions: which functions and objects to include; how they are to be labeled and displayed; whether the interface should use command language, menus, or icons; and how online help can be provided. As will be discussed later, each of these decisions involves consideration of complicated, and sometimes conflicting, human factors. When all decisions are considered at once, interface design becomes overwhelming. Therefore, our first objective in writing this article is to separate HCI design into major divisions and identify the most relevant design goals and human factors. In each division, design subtasks are analyzed within the context of current HCI research. The intent of this classification is to assist designers in relating the research findings to the HCI design process.

Early research emphasized the development of design guidelines. But, after attempts to both write and use guidelines, it was recognized that when a design is highly dependent upon task context and user behavior, the usefulness of guidelines diminishes (Gould and Lewis, 1985; Moran, 1981). The answer to this problem for a particular design is to model the behavior of users doing specific tasks. The model provides a basis for analyzing why a design works or fails. This leads to the emphasis of understanding cognitive processes employed in HCI; Model Human Processor (Card, et al., 1983), SOAR (Laird, et al., 1987), and Task Action Grammars (Payne and

Green, 1986) are examples of HCI theoretic models for studying user behavior (to be discussed later). These models provide a basis for explaining why some design guidelines work. Our second objective is to elaborate existing guidelines with their task constraints and theoretic bases so a designer can relate them to new, untested situations.

Our third and last objective is to identify opportunities for HCI research. An exhaustive review of guidelines and theories in user interface design reveals gaps in our knowledge regarding the impact of design choices on human behavior. By noting these opportunities, we hope to interest both practitioners and research scholars in furthering our knowledge of user interface design.

We begin with a framework for organizing HCI design and several theoretic approaches to investigating HCI issues. This is followed by design recommendations and research opportunities for each issue in the framework, and our conclusions.

## Overview of User Interface Framework and Theories

Card, et al. (1983) propose the user's recognition-action cycle as the basic behavior for understanding the psychology of HCI. This cycle includes three stages: the user perceives the computer presentation and encodes it, searches long and short-term memory to determine a response, and then carries out the response by sending his or her motor processors in motion. A more elaborate seven-stage HCI model is proposed by Norman (1986) (see Figure 1). Norman's model expands the memory stage to include mental activities, such as interpretation and evaluation of system response, formulation of personal goals and intentions, and specification of action sequences. Four cognitive processors are employed in the elaborated recognition-action cycle: motor movements, perception, cognition, and memory (Olson and Olson, 1990). Except for long-term memory, these processors have limited capacity and constrain users' behavior and, thus, HCI design. Most obvious is the need to satisfy users' motor and perceptual needs: signals must be perceivable, and responses should be within the range of a user's motor skills. But more importantly, the interface must empower the memory and cognitive capacity of its users to learn and reason easily about the system's behavior. Otherwise, the user interface will hinder the user's ability to learn all aspects of the system; a bad interface means the user will not use the system to solve new, difficult problems.

![](/api/attachments/NW9FUPZ7/fulltext/images/4a53e970fbeda1d952a52ef8e0fb5bb15f205d6800730dba33f2900d6c8bae37.jpg)  
Figure 1. Physical and Mental Processes in Operating a Computer  
(Adapted from Norman, 1986, and reprinted from Olson and Olson, 1990, p. 229, by permission of Lawrence Erlbaum Associates)

## Overview of the framework

While HCI objectives are clear, it is less obvious how the designer should go about developing interfaces that meet these objectives. Recent research suggests that a system model be employed as the basis of HCI design (Norman, 1986). The system model is a conceptual depiction of the set of objects, permissible operations over the objects, and relationships between objects and operations underlying the interface (Jagodzinski, 1983).

Norman (1986) points out that the selection of a good system model enables the development of clear and consistent interfaces. This is the premise of the interface design framework described in Figure 2. The conceptual aspect of the framework concerns design of the system model such that the underlying process the computer is performing is directly pertinent to the user in a manner compatible with the user's own understanding of that process (Fitter, 1979). The physical aspect of the framework involves the design of action and presentation languages, which consist of patterns of signs and symbols enabling the user to communicate to and from the system (Bennett, 1983).

![](/api/attachments/NW9FUPZ7/fulltext/images/19dba937282bb0cb3c11630aa157aa1274c9bd6ad4e0ebe148083575b087f928.jpg)  
Figure 2. The HCI Design Framework

Designing action and presentation languages based on a coherent system model enables the user to easily develop a mental model of the system through repetitive use. The mental model is the user's own conceptualization of the system components, their interrelations, and the process that changes these components (Carroll and Olson, 1988). The mental model provides predictive and explanatory power for understanding the interaction, enabling the user to reason about how to accomplish goals (Halasz and Moran, 1983; Norman, 1986). Hence, the closer the system model is matched to user expectations, the more easily and quickly user learning takes place. Developing the system model, therefore, requires a study of what the user expectations are.

A system model provides direction for designing action and presentation languages that determine the system's look and feel. When there is close correspondence between the system model and these two languages, the user can manipulate all parts of the system with relative ease. This creates an interface of “naive realism” (diSessa,1985): one that the user operates unaware of the computational technicalities embedded in the system software. But this naive realism cannot be easily achieved because technological restrictions limit the choice of dialog style and impose rigid syntax rules and recovery procedures. Hence, in specifying an action language, design tradeoffs must be made between satisfying the user's cognitive requirements and satisfying technological constraints. The presentation language complements the action language by displaying the results of system execution such that the user can easily evaluate and interpret the results. It also involves design tradeoffs in choosing proper object representations, data formats, spatial layout, confirmative mechanisms, and user assistance facilities.

Note that in Figure 2 the system model serves as the basis for developing action and presentation languages. The importance of this principle is illustrated by the user interfaces of two spreadsheet packages: IFPS (Execucom, 1979) and 1-2-3 (Lotus, 1989). IFPS's system model resembles linear algebra with a Fortran-like programming language; 1-2-3's resembles a paper spreadsheet and an electronic calculator. The system model choice results in clear differentiation in the action and presentation languages of these two packages. IFPS's action language requires the user to follow strict syntax rules to enter a spreadsheet model. Its presentation is that of an accounting report that can only be viewed in a top-down manner. Also, user actions and system presentations are clearly disjointed in IFPS; that is, the user first enters the algebraic formulae, waits for the system to process them, and receives the output when the system is finished.

In contrast, 1-2-3's action and presentation languages are intertwined. 1-2-3 allows the user to enter the spreadsheet by moving to any cell, row, or column in any order to enter data or specify formulae. Its presentation utilizes the same row-column format used for input; the user obtains an instant result for each action. The properties of 1-2-3's action and presentation languages are more generally accepted than those of IFPS, even though both provide similar capability. Hutchins, et al. (1986) attributes the success of spreadsheet packages like 1-2-3 to their use of a conceptual model that matches the user's understanding of spreadsheet tasks.

## Cognitive modeling

As previously mentioned, developing the system model requires a study of user expectations. One approach is to create prototypes, which provide an environment for testing and refining the system model. This, however, is expensive and time-consuming. Alternatively, several cognitive models can be used to analyze and clearly describe user behavior. This type of theoretical analysis can help designers select the best design from several alternatives, resulting in less time needed for HCI design (Lewis, et al., 1990).

## GOMS Model

A family of cognitive models based on the GOMS model is proposed by Card, et al. (1983) for predicting user performance. A GOMS model consists of four cognitive components: (1) goals and subgoals for the task; (2) operators, including both overt operators (like key presses)

and internal operators (like memory retrieval); (3) methods composed of a series of operators for achieving the goals; and (4) selection rules for choosing among competing methods to achieve the same goal. The majority of GOMS research has centered on the study of experts performing well-learned, repetitive tasks. This has led to the discovery of parameters, such as times for keystroke entry and the scanning of system outputs, useful for predicting skilled-user performance (Card, et al., 1983). But other important aspects of user behavior cannot be easily modeled in GOMS, such as the production of and recovery from errors (Olson and Olson, 1990) and the use of sub-optimal goals or methods in performing routine editing tasks, even when more efficient goals or methods are known (Young, et al., 1989).

## SOAR

SOAR (Laird, et al., 1987) is a general cognitive architecture of human intelligence. Although it has not been applied extensively in HCI research, SOAR has the potential for answering questions not addressed by GOMS. SOAR is an application of artificial intelligence that models users doing both routine and new tasks. In addition to a knowledge base and an engine that performs tasks it knows, SOAR has a learning mechanism. It provides an account of how a user evaluates system responses and formulates a new goal or intention. With SOAR, one can estimate how long it takes a user to recognize an impasse in his or her skill and set up a new goal and action sequence to overcome that impasse.

## Formal Grammars

Formal grammars expressed in Backus-Naur form (BNF) can be used to describe the rules of an action language. From these, an analyst can predict the cognitive effort needed to learn the language by examining the volume and consistency of the rules (Reisner, 1981). Task Action Grammars (TAG) are similar languages, which make explicit the knowledge needed for a user to comprehend the semantics and syntax of a user interface (Payne, et al., 1986). In addition to identifying the consistency of grammar rules, TAG can be applied to study how well the task features of the language match user goals.

## Discussion

GOMS, SOAR, and formal grammars collectively provide guidance in the design of system models and action and presentation languages. For example, GOMS suggests that system model design should be guided by analysis of user goals in order to identify methods for achieving these goals; SOAR demonstrates the importance of modeling user knowledge of the system model for solving new, difficult problems; TAG indicates how an action language's organization affects user learning.

It should be noted that each of these theories can explain some, but not all, aspects of human behavior in HCI. For example, the GOMS model can explain the task of selecting an option from a list of choices, but it fails to predict errors a person makes when using a line editor; TAG provides a reason why errors might occur but cannot predict moment-by-moment performance. In addition, psychological attributes, such as preference and attitude, and cognitive functions, such as mental imagery and cognitive style, are not considered in these theories (Olson and Olson, 1990). The specificity of each of these theories results in areas of uncertainty in HCI design, restricting our ability to apply them to practice. A great need for integrating theory and practice remains in HCI research.

## System Model Design

Central to the entire HCI design question is the design of the system model, a conceptual description of how the system works. This requires an analysis of user tasks so the system model can be organized to match the user's understanding of these tasks (Carroll and Thomas, 1982; Halasz and Moran, 1982; Moran, 1981). It also requires an analysis of metaphors and abstract models that can adequately portray system functionality (Carroll, et al., 1988). The result of the latter analysis may also help in selecting representations for system objects/functions and in user training.

## Analysis of task

The work by Card, et al. (1983) and Norman (1986) indicates that during computer interaction, the user's mental activities center around goal determination and action planning. To ensure that the system model supports these activities, task analysis should emphasize identifying user goals and the methods and objects employed to achieve these goals (Grudin, 1989; Phillips, et al., 1988).

## Work Activities and Scenarios

Goals, methods, and objects can be discovered by analyzing users acting out work-related scenarios (Young, et al., 1989). A scenario is a record of a user interacting with some device in response to an event, which is carefully constructed so that the user performs a definite action (like reordering paragraphs of a document or computing the return on a financial investment). A carefully constructed set of events assures that a comprehensive range of situations is studied and the results are applicable to brief, real-life work situations (Young and Barnard, 1987). Scenario analysis produces records of user actions from which specific user goals, methods, and objects needed to achieve these goals are identified. In addition, records of several users completing the same scenario enable the designer to compare different approaches to the same work situation and generate a set of methods and objects for a wide range of users.

## Routine Tasks and Complex Work

Task analysis proceeds by studying cognitive processes involved in handling the events. Researchers have observed that users' mental processes occur at two levels (Bobrow, 1975). Low-level processing involves well-learned, rehearsed procedures for handling routine operations such as data entry or word deletion. High-level processing, which relies upon knowledge of the system model, is used to generate plans of action to handle non-routine tasks.

To support low-level processing, objects need to be organized into logical chunks, and operations need to match the actions users normally make with these objects in the real world (Phillips, et al., 1988). In so doing, learning to associate operations with objects is easy; with practice, operations can be applied almost automatically, and even in parallel, because examination of data content and the meaning of each user action is unnecessary (Shiffrin and Schneider, 1977). For example, the spreadsheet system model supports low-level processing by organizing spreadsheets into cells, rows, and columns; operations like “delete” can be applied to any of these data levels with simple cursor movement and the same menu action choices.

High-level processing is top-down and is guided by user goals and motives; planning is slow, serial, and conscious (Newell and Simon, 1972; Rasmussen, 1980). A plan of action is a goal structure that describes how the user decomposes the problem into a sequence of methods which, when executed, properly handles the work situation. When facing a complex task, a user may divide the entire task into many subtasks and perform these subtasks separately at different times (diSessa, 1986). Thus, to support higher-level processing, one must ensure that nearly all user goals can be easily achieved through combinations of operations described in the system model in either a sequential or distributed manner. This flexibility can be seen in Xerox's Star Workstation, where operations for one goal (like creating a document) can be easily suspended to perform operations for another goal (like creating a spreadsheet) (Bewley, et al., 1983). Star also allows the user to cut a portion of one object (like a spreadsheet) and paste it to another object (a document) to achieve a higher-level goal of creating a report.

Task analysis results can be documented using GOMS, BNF, TAG, or SOAR. To complete the interface design, details of the methods and the operations to be performed on the objects need to be specified later during physical design.

## Analysis of metaphors and abstract models

In designing the system model, it is beneficial to search for metaphors analogical to the system model. Presenting metaphors to users helps them relate the concepts in the system model to those already known by a wide set of users. This enables the user to make inferences regarding what system actions are possible and how the system model will respond to a given action.

## Metaphors and Composite Metaphors

Metaphors can be drawn from tools and systems that are used in the task domain and the common-sense real world (Carroll, et. al., 1988). For example, many use a typewriter as a metaphor for a word processor. Unfortunately, the analogy between a word processor and a typewriter breaks down for depicting block insertion and deletion in word processing. For these actions, the word processor works more like a magnetic tape splicer. Hence, complex systems can be more completely described by a composite of several metaphors, each examined closely for its correspondence to the system's actual goal-action sequence. Since users generally develop disjointed, fragmented models to explain different kinds of system behavior (Waren, 1987), it is easy for them to accommodate composite metaphors in learning the system (Carroll and Thomas, 1982).

Even with composite metaphors, mismatches may still occur. Typical computer systems are more powerful than manual tools and may contain features not embodied in the metaphors, and vice versa. These mismatches may lead the user to form misconceptions about how the system works (Halasz and Moran, 1982). For example, in word processing, document changes need to be saved or the entire work session is lost; there is no such concept applicable to typewriters. Explicitly pointing out the mismatches to the user should prevent such misconceptions (Carroll, et al., 1988.)

## Abstract Models

Abstract models explicitly represent a system model as a simple, abstract mechanism, which the user can mentally “run” to generate expected system responses (Young, 1981). For example, a hierarchical chart depicting the organization of messages, folders, and files serves as the abstract model of storage for an electronic mail system, while a file cabinet serves as the metaphor (Sein and Bostrom, 1989). Like a metaphor, the abstract model is not intended to fully document every detail of a system model; rather, both provide a semantic interpretation and a framework to which the user can attach each new system concept (Carroll, et. al., 1988; Mayer, 1981). But unlike a metaphor, there is a one-to-one mapping from the attributes of an abstract model to those of the system model, although not vice versa. Abstract models are particularly useful for depicting system models that have no real-world counterparts; for instance, a pictorial depiction of interactions among memory, instructions, input, and output can provide a useful high-level description of a BASIC program's execution.

## Applying Metaphors and Abstract Models

Metaphors and abstract models are powerful means for conveying the system model to novices. Mayer (1981) reports that novices who lack requisite knowledge are aided by learning abstract models, which enable them to understand system concepts during interactions with the system. Sein and Bostrom (1989) find that abstract models work best for novices who are able to create and manipulate mental images. For other novices, the metaphor is better. Hence, the choice between metaphor and abstract model is dependent upon the user's task knowledge and the ability to conceptually visualize the system model.

In conceptual design, candidate metaphors and abstract models can be identified to provide the designer with building blocks for constructing a consistent, logical system model based upon the user's task model (Waren, 1987). But basing the system model entirely on metaphors may be too limiting for harnessing the full power of the computer. The designer's objective should be to properly balance the users' descriptive model of the task, the normative model of how the task ought to be done, and the new opportunities provided by computer technology.

## Iterative system model development methodologies and tools

Task and metaphor analysis must be user-centered and iterative. Initial attempts produce a crude system model; iterative design and testing rework this crude model into a successful system model. For example, questionnaires help determine the basic attributes of the user group like age, computer training, and education. Interviews can be used to identify the basic system capabilities (Olson and Rueter, 1987). Other useful approaches include psychological scaling methodologies and simulation and protocol analysis.

## Psychological Scaling Methodologies

To identify the grouping of objects/methods, the designer can solicit user similarity judgments on all pairs of objects/operations based upon user judgment of frequency of occurrence, temporal distance, or spatial distance (McDonald and Schvaneveldt, 1988). From this similarity measurement, clusters of objects/methods can be identified by applying psychological scaling methodologies, such as hierarchical clustering, multidimensional scaling, and network structuring techniques (e.g., Pathfinder) (McDonald et al., 1988; Olson and Rueter, 1987). These methodologies can be applied to organize system documentation or menu hierarchy. For example, Kellogg and Breen (1987) developed users' views of how various elements of documents (footnotes, captions, etc.) are interrelated; McDonald and Schvaneveldt (1988) organized UNIX documentation according to perceived functionality.

## Simulation and Protocol Analysis

Requiring users to describe their work requirements in their own language can identify useful metaphors and abstract models (Mayer, 1981). Pencil-and-paper simulations of a proposed interface enable the user to act out typical work scenarios (Gould and Lewis, 1985). This technique, coupled with think-aloud protocol analysis, makes it possible to determine how work is actually done. It is useful for deriving an initial estimate of the users' set of basic functions and data objects.

Another approach is called the Wizard of Oz (Carroll and Aaronson, 1988). This approach employs two linked machines, one for the user and the other for the designer. Both the user's display and the designer's display show a simulated view of the system. To attempt a task, the user enters a command, which is routed to the designer's screen. The designer simulates the computer by evaluating the user input and sending a response to the user's display. This approach has the advantage of putting the user in a work-like situation well before the final system is fully programmed. Finally, user interface management systems like GUIDE, Domain/Dialog, and Prototyper (Hartson and Hix, 1989) or hypermedia tools like Hypercard (Halasz, 1988) can be used for rapid prototyping to evaluate user needs. They are, however, more expensive than the Wizard of Oz in terms of manpower and time needed for creating the prototype.

## Discussion

Much research is still needed if we are to thoroughly understand system model design. Our knowledge of cognitive processes in HCI is still limited, although recent emphases in this area indicate an increasing awareness of its significance among researchers and practitioners (Olson and Olson, 1990). One important strategy is to apply theories like GOMS, TAG, and SOAR to study a broad range of computer tasks for understanding mental activities involved in solving routine and novel problems. An attempt at this research has been underway; an AI program in-cooporating means-ends analysis and multiple problem spaces has been used to analyze user task knowledge (Young and Whittington, 1990). This analysis can alert the designer to potential problems of a proposed interface.

Another important strategy is to improve psychological methods for studying users' prior knowledge and cognitive processes. The methods may be applied to investigate how a user forms a mental model of a system and to evaluate the discrepancies between the user's mental model and the system model. This provides feedback regarding the quality of system model design to designers, who can then improve their design strategies.

In addition, guidance is needed for applying metaphors to system model design. Whether or not system models are based upon metaphors, users are likely to generate metaphoric comparisons on their own (Mack, et al., 1983). What happens if this comparison creates user confusion because of the discrepancy between the designer's metaphor choice and the user's own comparative idea? Strategies are needed for portraying metaphors so that the metaphoric comparison is obvious but not distracting. There is also a need for methodologies for evaluating alternative metaphors. Carroll, et al. (1988) hypothesize that the user transforms metaphors into a precise understanding of the system model via a three-stage process: (1) establishing a metaphoric comparison; (2) elaborating aspects of the metaphoric comparison map meaningfully to the system model; and (3) consolidating to produce a system model from what was learned from each comparison. However, it is unclear how this theory can be applied to analyze metaphor learnability.

Finally, user confusion may arise when system concepts have no analogical descriptions, such as the difference between a line wraparound and a hard carriage control. How can abstract models be useful in these situations? Research is needed to provide principles to guide the development of abstract models and strategies for using these models effectively in user training.

## Action Language Design

The next component of the HCI framework to be addressed is the action language design. It involves the creation of a means for the user to easily translate his or her intentions to actions accepted by the system. Because natural language is not yet a viable option, designers must rely upon dialog styles unnatural to novices, relying primarily on keyboards and pointing devices. Designers must also choose a syntax and vocabulary for action specifications, and mechanisms for protecting the user from unintentionally destroying completed work.

## Dialog style

Many conversation-based dialog styles have been employed in HCI. In Table 1, these styles are classified according to who initiates the dialogs and choices available for action specifications (Miller and Thomas, 1977). Recently, direct manipulation styles using pointing and graphics devices have become popular; they differ from conversational styles in many aspects (see Table 2) (Hutchins, et al., 1986; Shneiderman, 1987).

The system model, when designed in accord with user perception of how tasks are conducted, may suggest the dialog style. For example, the “form” style is the natural choice for a system involving database inquiries because forms are widely used for storing data manually and, as a consequence, become the metaphor for that system.

But choosing a dialog style often requires considering human factors other than the system model. The tasks may be complex, suggesting that no single style is sufficient. For example, accounting application interfaces are often a mix of forms, menus, and command languages, each tailored to specific task requirements. User difference also plays an important role. Performance on relatively low-skill, computer-based tasks can vary as much as 9:1 (Egan, 1988). This variance in user performance can be partially attributable to individual differences such as skill level, technical aptitude, age, and cognitive style.

The level of user experience and technical skill is a dominant factor in selecting an appropriate dialog style (Mozeico, 1982). For novices, computer-guided, constrained-choice interfaces are better because the time spent on mental activities, shown in Figure 1, is reduced. Conversely, with experience comes a clear understanding of how tasks can be achieved, decreasing the need for a computer-guided interface and creating a preference for a user-initiated language.

Direct manipulation styles, like Star's iconic desktop interface, are easy to learn because they closely reflect the system model, which in turn closely matches the user's task knowledge. They are easy to use for both novices and experts because of simple push-button actions and a continuous display of the "system states" that guide user actions (Shneiderman, 1987). Still, direct manipulation styles may be slower than conversational styles for experts to use (Hutchins, et al., 1986).

Novices can become expert through experience. This transition is easier if the user possesses technical aptitude, which involves high spatial memory and visualization and/or deductive reasoning ability. These abilities help the user remember, visualize, and locate objects and generate syntactically correct instructions (Egan 1988).

Cognitive style and age also affect the dialog style decision. A study by Fowler, et al. (1985) shows that field-independent users, autonomous and self-reliant, prefer a user-initiated command structure, while field-dependent users tend to prefer constrained interfaces. Age is a significant factor in predicting user performance, particularly for interfaces requiring the user to possess a technical aptitude (Egan, 1988). The loss in performance due to aging can be countered with a simplified interface that reduces the necessity of visualizing important displays.

Multi-style interfaces can be employed to satisfy users varying in skill level, cognitive style, and age. For example, styles ranging from question-answer to menu and command language can all be included within the interface; the user can then choose any style to achieve better performance and satisfaction (Mozeico, 1982). Recently, an implementation integrating natural language with direct manipulation (Cohen, et al., 1989) and another combining command language and direct manipulation (Gerlach and Kuo, 1991) show the practicality of this approach.

Table 1. Taxonomy of Dialog Styles Based on Initiation and Choice

<table><tr><td>Choice Initiation</td><td>Free-Response</td><td>Forced-Choice</td></tr><tr><td>User-guided</td><td>Database languageCommand languageData mnemonicsText (word) processing</td><td>Expert system questionsInput-in-the-context-of-output</td></tr><tr><td>System-guided</td><td>Question/free answerForm filling</td><td>Question/forced answerCommand menu selectionData menu selectionEmbedded menuAccelerated menu</td></tr></table>

Table 2. Comparison of Conversational and Direct Manipulation Styles

<table><tr><td>Conversational Style</td><td>Direct Manipulation Style</td></tr><tr><td>Sequential dialog, which requires the user to enter parts of an instruction in a predetermined order</td><td>Asynchronous dialog, which enables the user to enter parts of an instruction in virtually any order</td></tr><tr><td>Language of strict syntax to describe the user intention</td><td>Direct manipulation of objects</td></tr><tr><td>Complete specification of user intention is required</td><td>Incremental specification of user intention is allowed</td></tr><tr><td>Discrete display of states of system executions; this includes errors if the command fails to execute</td><td>Continuous update of objects to reflect system execution results; few error messages are needed</td></tr><tr><td>Single-threaded dialogs, which force the user to perform tasks serially</td><td>Multi-threaded dialogs, which permit the user to switch back and forth between tasks</td></tr><tr><td>Command first, object next is typical</td><td>Object first, command next is typical</td></tr><tr><td>Modes are often used to increase keystroke efficiency</td><td>Modeless user operations, which are less confusing to the user</td></tr></table>

## User interface syntax

In interacting with a computer, the user is required to translate his or her goals and intentions into actions understood by the system. Hence, in syntax design, designers must select words that not only represent system objects and functions but also match user expectations. Likewise, the action sequence of entering these words needs to be specified so it can be easily recognized and remembered by users.

## Vocabulary

One way to select vocabulary is for designers to select keywords based upon the system model. This approach to vocabulary design, although intuitively appealing, is shown to be impractical because designers' word choices vary significantly among themselves and may differ from users' choices (Carroll, 1985). Barnard (1988) suggests user testing for obtaining specific words.

Novices prefer general, frequently used words that are not representative of system concepts (Black and Sebrechts, 1981; Bloom, 1987). Different novices often assign different words to the same concept (Good, et al., 1984; Landauer, et al., 1983). As a result, words used by some novices may not help others learn the action language.

A better alternative is to have expert users select terms that are highly representative of system concepts; these terms can then be evaluated by novices for learnability (Bloom, 1987). To accommodate both novices' and experts' preferences, synonyms should be included as a part of the action language (Good, et al., 1984). The alternative word choices, even if synonyms are not implemented, can be presented to novice users for learning the concept of the chosen word (Bloom, 1987).

## Action Consistency

Consistent keystrokes within and across different systems lend themselves to easy memorization, resulting in faster, easier learning. This helps users in transferring knowledge of a well-learned system to a new system (Polson, 1988; Polson, et al., 1986). It also reduces user errors and the time and assistance needed to enter commands (Barnard, et al., 1981).

Action inconsistency typically occurs in systems employing modes. For example, line editors typically have two modes: one for input and the other for editing. Modes are confusing to novices because identical keystroke sequences generate different results in different modes (Norman, 1983). However, they are efficient for applications in which the number of commands exceeds the number of keys available. With practice, modes allow experts to use fewer keystrokes for command entry; elimination of modes may penalize the experienced user. Norman recommends that modes be employed judiciously. We suggest that techniques for focusing user attention (discussed later) should be used to make modes obvious to the user to reduce confusion.

An action language's consistency is affected by its orthogonality. In an orthogonal language, each basic keystroke component is assigned a unique meaning representing a single action parameter, which can be an operation, an object, or any other qualifier (Bowden, et al., 1989). A single set of rules determines how these unique keystroke components can be combined to form commands. For example, in a word processing system, commands must obey the rule: first, operation (e.g., DELETE); next, object (e.g., LETTER); and last, direction qualifier (e.g., RIGHT). In an orthogonal language, keystrokes per command increases in proportion to the size of the command set; more time is therefore needed to enter commands. But less effort is needed to memorize and recall each keystroke's meaning. This reduction in mental effort and time may make the memorability-efficiency tradeoff beneficial if ease of learning is critical to the user.

## Action Efficiency

Many system implementations concentrate on minimizing keystrokes to reduce motor activities through the use of function keys, command abbreviations, and recognition of an option's first letter. But as noted earlier, keystroke efficiency is also a function of memorizing and recalling the keystrokes. For example, when a function key is given multiple meanings whose interpretation depends upon the context in which it is applied, a user can be easily confused because of the increased mental load in recall (Morland, 1983). Offering both whole and abbreviated commands is one way to increase motor efficiency while reducing the mental load. With these options, the user can initially enter the whole command and then quickly make use of abbreviated commands (Landauer, et al., 1983). The importance of reducing the mental load is further illustrated by Lerch, et al.'s (1989) study of spreadsheet users performing financial planning tasks. They found that users perform better using relative referencing of spreadsheet variables (e.g., PREVIOUS REVENUES) than when using absolute row and column coordiantes. Absolute row and column coordinates require less keystroke time to enter but additional mental overhead. Overall, relative referencing schemes reduce user errors and allow the user to devote mental capacity to planning the task solution.

Another way of increasing efficiency is for a system to offer multiple methods for doing the same type of task; the efficiency of each method varies in accordance with the task situation. But the user may fail to choose the method that requires the least number of keystrokes for a given task because of the additional mental cost expended in choosing between two methods (Olson and Nilsen, 1987). Further investigation may focus on trade-off decisions between using a well-rehearsed single general method and learning and employing several context-specific methods.

## Protection mechanisms

The majority of beginners act recklessly; they make little effort to read user manuals to acquire system knowledge. A survey shows that trial-and-error learning is most widely used (Hiltz and Kerr, 1986). A major concern, therefore, is to ensure that the action language protects the user from being penalized for trying the system.

One common technique for this is to provide the user with an “undo” function that reverses a series of actions. Another is to prompt the user to reconsider planned actions that can lead to damaging, irreversible results, such as deleting a file.

A third, more interesting approach is “training wheels,” which encourage novices to explore system features during the initial learning stage while protecting them from disaster (Carroll and Carrithers, 1984). They block invocation of non-elementary system features and respond with a message stating that the feature is unavailable. The “training wheels” approach effectively supports exploratory learning by reducing the amount of time users spend recovering from their errors. But they do not help the learner acquire system concepts needed for performing tasks not attempted previously (Catrambone and Carroll, 1987). Research is needed to study what users learn or do not learn from their mistakes. Another interesting question is the effect of combining the abstract model and the “training wheels” approach for providing the user with an interface for learning the system model. We hypothesize this combination will result in deeper user understanding of system concepts.

## Discussion

An important issue of action-language design concerns trade-offs between efficiency and consistency. Keystroke consistency may increase learnability for novices but decrease efficiency for experts. This issue requires further research in understanding the user's cognitive processes for memorization and recall when interacting with a computer.

Another research issue concerns how to design an interface or suite of interfaces to satisfy all users. For example, multi-style interfaces can be created so all styles are equally functional. The user can then express the same intention in his or her preferred style. To do so, research must address questions related to how interfaces can assist users in transferring knowledge from one dialog style to another. How can one build multi-style interfaces so that mastery of one style is instrumental and perhaps sufficient to facilitate progress to another? Can users move from a style that is system-initiated to one that is user-initiated? Future research should focus on understanding cognitive processes for knowledge transfer, building on the work by Kieras, et al. (e.g., Kieras and Bovair, 1984; Kieras and Polson, 1985).

Finally, there is a need for developing principles to guide the use of speech and gesture devices. Preliminary studies have shown that users prefer these devices (Hauptmann, 1989; Weimer and Ganapathy, 1989). Effective incorporation of such devices in the action language requires further studies to assess their impact on the motor, sensory, perceptual, and cognitive processes of the user.

## Presentation Language Design

The last section of the HCI framework concerns presentation language design. An important design objective is for interface displays to guide user actions (Bennett, 1983). This objective requires selecting representations that fit the user's task knowledge; the format of data produced by the system must satisfy task needs and preferences. A display's layout is to be organized so that the collective presentation of various outputs eases user perception and interpretation. Presentations also convey feedback to attract the user's attention and confirm user actions. Finally, online assistance must be designed to help users learn system operations and correct their errors.

## Object representation

If the presentation is to adequately reflect the metaphors on which the system model is based, the designer must choose a display appearance that assists users in establishing the analogy between that display and the metaphors. A familiar appearance enables the user to recognize and interpret the representation easily. Examples of this principle are found in the spreadsheet-like interfaces of 1-2-3 and the electronic desk top of Star.

Icons can represent much information and be easily differentiated (Blattner, et al., 1989). An icon can be a concrete picture replicate of a familiar object, such as the trash can icon in Star. System concepts having no pictoral replicates can be depicted by abstract icons composed of geometric shapes and figures. Concrete and abstract icons may also be combined to create hybrid icons, e.g., ⚠ for deleting a character. Unlike concrete icons, abstract and hybrid icons must be taught to the user. Once learned, however, they are effective on conveying important system concepts.

## Presentation formats: table vs. graph

Presenting results in graph or table formats to satisfy both user decision style and task requirements is of great interest to designers of decision support systems. When the task requires a large volume of data, graphs are more effective than tables for allowing the user to summarize the data (Jarvenpaa and Dickson, 1988). Graphs are also good for tasks (such as interpolation, trend analysis, and forecasting) that require identification of patterns from large volumes of data. Conversely, if the task requires pinpointing data with precision, tables are better. Tables also outperform graphs for simple production scheduling decisions. But for complex decisions, graphs are superior (Remus, 1984; 1987). Finally, combining graph and table formats can result in better decisions, albeit with slower performance, compared to using either display alone (Powers, et al., 1984).

Our understanding of the cognitive processes involved in handling tables and graphs is still limited. Johnson and Payne (1985) and Johnson, et al. (1988) demonstrate that if information is presented in a format difficult for the user to comprehend, the user may employ an easier but less effective decision strategy than one that requires more sophisticated reasoning but leads to a better result. Lohse (1991) shows that graphs and tables differ in their cognitive effort. Lohse's research is interesting because it is based on a cognitive model that includes perceptual stores, short-term memory, algorithms for discrimination and encoding, and timing parameters. The model can predict the time needed for a user to understand a graph. It can be an advisory tool for choosing formats to match task needs and has the potential to answer questions regarding how and when graphs and tables can be applied to facilitate problem solving.

## Spatial layout

User productivity is enhanced when all needed information is readily available. To display as much information as possible in a limited area, the designer should consider information chunking, placement consistency, and the use of windows and 3-D displays.

## Chunking

The display, partitioned into well-organized chunks that match the user's expectations and natural perception abilities, provides a basis for the user to select and evaluate actions (Mehlenbacher, et al., 1989). Chunks can be identified using the psychological techniques discussed in the system model section. The layout can be organized following Gestalt principles: the principles of proximity and closure suggest enclosing each chunk of objects in a separated area; the principle of similarity suggests using the same font or color for objects of the same chunk. Also, spatial consistency of chunks is important because memorization of location is effortless (Mandler, et al., 1977); labels can be used with chunking to improve recognition and recall (Burns, et al., 1986; Jones and Dumais, 1986).

## Placement Consistency

One way proposed to reduce the time in searching menu items is arranging menus according to frequency of use (Witten, et al., 1984). But this approach may have only a short-term advantage over a menu with fixed configuration; it may even cause slower performance because the mental effort for searching the menu increases with change and the user becomes disoriented (Somberg, 1987; Trevellyan and Browne, 1987). In the long term, a fixed configuration facilitates searching better than, or as well as, a dynamic menu. The fixed configuration lends itself to memorization, and, therefore, menu selection is effortless once it is learned by the user.

## Windows and 3-D Displays

A window is a clearly defined portion of the screen that provides a working area for a particular task. Windowing has several benefits. Using multiple windows enables the user to simultaneously perform multiple tasks that may be unrelated. The content of the unfinished task in a window is preserved so the user can easily continue that task later. Windows also serve as visible memory caches for integrating information from multiple sources or monitoring changes in separate windows. These benefits collectively enable windowing to support separate but concurrent task execution.

A drawback of windowing is that operating multiple windows demands higher cognitive processes, i.e., memory, perception, and motor skills. Overuse of windows can cause information overload and loss of user control such that the user may employ an inefficient search strategy in scanning multiple windows (Hendrickson, 1989). Window manipulation is also shown to be difficult for the user, probably caused by the complexity in arranging windows (Carroll and Mazur, 1986). Users perform tasks more slowly, although more accurately, with windows (Hendrickson, 1989). Thus, operations for managing windows should be simplified. The window design should employ consistent placement and avoid overcrowded window to ease user perception and memory load.

Also, 3-D displays can be used to accommodate and condense a large volume of data (Card, et al., 1991). A 3-D display is divided into many 3-D rooms, each used for a distinct application. The user can manipulate objects in the 3-D space to differentiate images, investigate for hidden information, and zoom in for details.

## Attention and confirmation

Video and audio effects are useful in drawing a user's attention to important system responses and confirming user actions. Both are important for helping the user judge the status of his or her actions.

People typically have an orienting reflex to things that change in their visual periphery. Hence, video effects such as color, blinking, flashing, and brightness contrast can stimulate user curiosity for critical information (Benbasat, et al., 1986; Morland, 1983). Audio effects can be used to complement video effects or reveal information difficult to represent with video (Gaver, 1986; 1989). In addition, audio feedback can reduce space needs and synchronize user input with system response (Nakatani, et al., 1986).

Often there is delay between user actions and system presentations. In this situation, confirmatory feedback, such as immediate cursor response and changing shapes and shades of icons, is useful (Bewley, et al., 1983; Gould, et al., 1985). Similarly useful are progress indicators to display the percentage of work completed. Graphic-based progress indicators, like a percent-done thermometer or a clock, are considered fun to use (Myers, 1985). Progress indicators also aid in conducting multiple tasks. For example, a user informed that a long time is required for printing a document may decide to spend that time editing another file or retrieving a cup of coffee.

Both visual and auditory cues are shown to motivate users to explore unknown system features (Malone, 1984). Incorporating both video and audio feedback may have significant impact on user learning and satisfaction. Auditory icons, or “earcons,” provide intuitive ways to use sound for presenting information to users (Blattner, et al., 1989; Gaver, 1986; 1989). Like visual icons, auditory icons can be constructed by digitizing natural sounds with which the user is familiar; abstract auditory icons can also be created by composing a series of sound pitches (Blattner, et al., 1989). For example, in SonicFinder (Gaver, 1989), a wooden sound is used for opening a file and a metal sound for opening an application, while a scraping could indicate the dragging of an object. The research in this area could focus on creating game-like interfaces that are fun to learn (Carroll and Mazur, 1986) and on assisting visually impaired users.

## User assistance

Three types of information have been shown to be valuable for providing user assistance (Carroll and Aaronson 1988; Kieras and Bovair, 1984). One is “how-to-do-it” information that defines specific action steps for operating the system. Another is “what-it-is-for” information that elaborates on the purpose of each step; this helps users associate steps with individual goals. Third is “how-it-works” information that explains the system model; this is useful for advanced troubleshooting and creative use of the system. All three types of information can be used in writing online error messages and user instructions.

## Error Correction

When novices make errors and are uncertain about what to do next, they often look for instructions from the system message (Good, et al., 1984). Thus, error messages should pinpoint corrective, “how-to-do-it” information and state “what-it-is-for” (Carroll and Aaronson, 1988). In addition, immediate feedback on user errors facilitates learning better than delayed feedback because a user can easily associate the correct action with the exact point of error (Catrambone and Carroll, 1987). The style of error messages is also important: they should reflect users’ words, avoid negative tones, and clearly identify the portion of the action in error (Shneiderman, 1987).

## Online Manuals

When users know the task they wish to perform, brief “guided exploration cards” (Catrambone and Carroll, 1987) help users perform better than long manuals. Specific “how-to-do-it” information can be included for novices to do complete tasks quickly in the beginning (Carroll and Aaronson, 1988; Catrambone, 1990). In addition, instructions describing general rules of the system model encourage novices to infer unstated details of the interface, resulting in better user learning of the system (Black, et al., 1989).

The GOMS model described earlier can be used to create online manuals (Gong and Elkerton,

1990). To do so, the designer conducts a GOMS analysis of user tasks. The result is then applied to organize the manual based on possible user goals; for each goal, specific “how-to-do-it” information on methods and operators is then provided. Error avoidance and recovery information can be included to improve user performance.

## Query-in-Depth

Query-in-depth is a technique designed to provide multi-level assistance to help users at various levels of expertise learn the system (Gaines, 1981; Houghton, 1984). Its low-level help includes brief “how-to-do-it” and “what-it-is-for” information that instructs users’ immediate actions. If not satisfied, the user can request more advanced “how-it-works” information for troubleshooting.

## Discussion

In the past 10 years, engineers have created sophisticated video and audio technologies for computer input and output. New technologies, like Virtual Reality and Speech I/O, will likely be integrated into normal presentations. To effectively apply them, we need to better understand how they affect the user in performing work. Studies have shown that while auditory memory has less storage capacity than visual memory, it retains signals more than twice as long as visual memory (Cowan, 1984). These differences in attention and memory phenomena must be examined within the context of human-computer interaction. What is the impact on user cognitive process given that only limited capacity is available for motion and perception? How should the various devices be integrated? What are the costs and benefits in terms of hardware, software, user training, and actual user performance? Providing guidance in designing video and audio interfaces is challenging but critical in HCI research in the near future.

Windowing offers many advantages in action and presentation language design that have yet been explored. For example, one way to implement multi-style interfaces is to allow each style to be operated in a separate window. Or, to adapt to a user's pattern of menu usage, a window for the most recently used menu options, another for the most frequently used options, and a third for the regular menu options can be used in combination. Windows are ideal for user assistance: error messages, online manual, or confirmatory feedback can be located in windows separated from work dialogs. Complex tasks can also be supported by allowing subtasks in separate windows or 3-D rooms. Again, research is needed to study how windows and 3-D rooms can be effectively applied for these various purposes. The central issue is to understand how they can impact the user's cognitive processes, as discussed in the work by Card, et al. (1991).

Finally, there is a need for research in online advising. Research so far has shown that online advising, even that provided by an expert using the Wizard-of-Oz technique, is of limited use for the novice user (Carroll and Aaronson, 1988). The difficult issues to be addressed are what information should be given and when, what ideas should be left to user inference, and how to use motivational feedback to make learning enjoyable. Studies could also explore the use of video and audio feedback in assisting the user.

## Conclusion

Interfaces are complex, cybernetic-like systems that can be built quickly but are difficult to build well. Their complexities necessitate the decomposition of the entire user-interface design problem into small, manageable subproblems, along with a reexamination of their interrelationships into a whole. The framework presented in this article serves this purpose; it organizes research findings into three major divisions: system model, action language, and presentation language. This article reviews current HCI research findings and illuminates their practical implications. The aim of this work is to enable HCI design practice to become more systematic and less intuitive than it is today.

Throughout the literature two major philosophies of interface design and research can be identified. One is that interface design is often driven by technological advancement; research is conducted to address problems that occur after a design is implemented. This generated the mouse, voice, windows, and graphics. The other is that we still know little about the psychological make-up of the user. The work on the psychology of HCI by Card, et al. (1983) and Norman (1986) provide a solid theoretic beginning; much research is needed to expand these theories so they can be useful in addressing a wide range of interface design issues based upon user and task considerations.

Great challenges remain ahead in interface research. We should not limit ourselves to the study of problems concerning only existing technologies. We should explore new, creative uses of advanced technologies to know what, when, and how to apply them effectively. We can save substantial research effort by ceasing to emphasize problems inherent in poorly developed technologies unless they illuminate cognitive processes that will be important to interfaces of the future (Wixon, et al., 1990).

We need to broaden research concerning how people organize, store, and retrieve concepts (Carroll and Campbell, 1986; Newell and Card, 1985; 1986). Theories of exemplar memory, prototype memory, episodic memory, and semantic memory are probably applicable to HCI research. We also need to investigate psychological attributes (such as attitude and preference), work-related factors (such as fatigue and organizational culture), and certain physical limitations (such as hearing and vision impairment). We must study how user interfaces should cope with the limitations imposed by varying user characteristics. More importantly, we must focus on what aspects of user characteristics are important, how they are related to each stage of HCI design, and when during the design stage they must be considered. This focus ensures the applicability to research findings to design.

Finally, we must interrelate the research findings if we are to develop comprehensive theories for the design, implementation, and testing of functional, usable, and learnable interfaces. In this pursuit, the role of the designer in documenting his or her design rationales is especially important. A design rationale is a record of design alternatives and explanation of why some specific choice is made. To further our understanding of HCI, design rationales should be a co-product of the design process (Maclean, et al., 1989). Comparing and contrasting design rationales of various systems enables us to capture the range of constraints affecting the HCI design and gain insights into why a choice works or does not work.

Some excellent exploratory work has been done in this area. For example, Wixon, et al. (1990) propose collection of usability data in the context of user tasks to identify both general principles and detailed guidelines for HCI design. Carroll and Kellogg (1989) and Carroll (1990) emphasize the identification of psychological claims embodied in an interface and the application of artifacts as bases for assessing appropriateness of these claims. In conclusion, data regarding user tasks, user achievement and problems, and changes in the overall environment should be collected on a continuous basis. Assumptions about the psychology of the user performing the task and limitations of technology must be explicitly stated. The collection of design rationales can then be used to develop practical guidelines and principles, which should be repeatedly evaluated to develop theories governing HCI design.

## Acknowledgements

We are indebted to the anonymous reviewers for their considerable effort in reviewing this article. We are particularly thankful to the associate editor, Judith Olson, for her insights into the field of HCI. Their many recommendations contributed significantly to this article's development.

## References

Barnard, P.J. "Command Names," in Handbook of Human-Computer Interaction, M. Helender, (ed.), Elsevier Science Publishers, Amsterdam, 1988, pp. 181-199.

Barnard, P.J., Hammond, N. V., Morton, J., Long, J.B., and Clark, I.A. "Consistency and Compatibility in Human/Computer Dialogue," International Journal of Man-Machine Studies (15), 1981, pp. 87-134.

Benbasat, I., Dexter, A.S., and Todd, P. "An Experimental Program Investigating Color-Enhanced and Graphical Information Presentation: An Integration of the Findings," Communications of the ACM (29:11), December 1986, pp. 1094-1105.

Bennett, J. "Analysis and Design of the User Interface for Decision Support Systems," in Building Decision Support Systems, J. Bennett (ed.), Addison-Wesley, Reading, MA, 1983, pp. 41-64.

Bewley, W.L., Roberts, T.L., Schroit, D., and Verplank, W.L. "Human Factors Testing in the

Design of Xerox's 8010 STAR Workstation," Proceedings of CHI'83 Human Factors in Computing Systems, Boston, MA, 1983, pp. 72-77.

Black, J.B., Bechtold, J.S., Mitrain, M, and Carroll, J.M. "On-line Tutorials: What Kind of Inference Leads to the Most Effective Learning?" Proceedings of CHI'89 Human Factors in Computing Systems, Austin, TX, 1989, pp. 81-83.

Black, J.B. and Sebrechts, M.M. "Facilitating Human-Computer Communication," Applied Psycholinguistics (2), 1981, pp. 149-177.

Blattner, M.M., Sumikawa, D.A., and Greenberg, R.M. "Earcons and Icons: Their Structure and Common Design Principles," Human-Computer Interaction (4:1), 1989, pp. 11-44.

Bloom, C.P. "Procedures for Obtaining and Testing User-Selected Terminologies," Human-Computer Interaction (3:2), 1987-1988, pp. 155-177.

Bobrow, D.G. "Dimensions of Representations," in Representation and Understanding, D.G. Bobrow and A. Collins (eds.), Academic Press, New York, NY, 1975, pp. 1-34.

Bowden, E.M., Douglas, S.A., and Stanford, C.A. "Testing the Principle of Orthogonality in Language Design," Human Computer Interaction (4:2), 1989, pp. 95-120.

Burns, M.J., Warren, D.L., and Rudisill, M. "Formatting Space-Related Displays to Optimize Expert and Nonexpert User Performance," Proceedings of CHI'86 Human Factors in Computing Systems, Boston, MA, 1986, pp. 274-280.

Card, S.K., Moran, T.P., and Newell, A. The Psychology of Human-Computer Interaction, Lawrence Erlbaum Associates, Hillsdale, NJ, 1983.

Card, S.K., Robertson, G.G., and Mackinlay, J.D. "The Information Visualizer: An Information Workspace," Proceedings of CHI'91 Human Factors in Computing Systems, New Orleans, LA, 1991, pp. 181-188.

Carroll, J.M. "The Adventure of Getting to Know a Computer," IEEE Computer (15:11), Nov. 1982, pp. 49-58.

Carroll, J.M. What's in a Name, Freeman, New York, NY, 1985.

Carroll, J.M. "Infinite Detail and Emulation in an Ontologically Minimized HCI," Proceedings of CHI'90 Human Factors in Computing Systems, Seattle, WA, 1990, pp. 321-327.

Carroll, J.M and Aaronson, A.P. "Learning by Doing with Simulated Intelligent Help," Communications of the ACM (31:9), September 1988, pp. 1064-1079.

Carroll, J.M. and Carrithers, C. "Training Wheels in a User Interface," Communications of the ACM (27:8), August 1984, pp. 800-806.

Carroll, J.M. and Campbell, R.L. "Softening Up Hard Science: Reply to Newell and Card" Human Computer Interaction (2:3), 1986, pp. 227-249.

Carroll, J.M. and Kellogg, W.A. "Artifact as Theory-Nexus: Hermeneutics Meets Theory-Based Design," Proceedings of CHI'89, Human Factors in Computing Systems, Austin, TX, 1989, pp. 7-14.

Carroll, J.M., Mack R.L., and Kellogg, W.A. "Interface Metaphors and User Interface Design," in Handbook of Human-Computer Interaction, M. Helander, (ed.), Elsevier Science Publishers, Amsterdam, 1988, pp. 67-86.

Carroll, J.M. and Mazur, S.A. "Lisa Learning," IEEE Computer (19:11), November 1986, pp. 35-49.

Carroll, J.M. and Olson, J.R. "Mental Models in Human-Computer Interaction," in Handbook of Human-Computer Interaction, M. Helander (ed.), Elsevier Science Publishers, Amsterdam, 1988, pp. 45-65.

Carroll, J.M. and Thomas, J.C. "Metaphor and the Cognitive Representation of Computing Systems," IEEE Transactions on Systems, Man, and Cybernetics (12:2), 1982, pp. 107-116.

Catrambone, R. "Specific Versus General Procedures in Instructions," Human Computer Interaction (5:1), 1990, pp. 49-93.

Catrambone, R. and Carroll, J.M. "Learning a Word Processing System with Training Wheels and Guided Exploration," Proceedings of CHI + GI 1987 Human Factors in Computing Systems, Toronto, Ontario, 1987, pp. 169-174.

Cohen, P.R., Dalrymple, M., Moran, D.B., Pereira, F.C.N., Sullivan, J.W., Gargan, R.A., Jr., Schlossberg, J.L., and Tyler, S.W. "Synergistic Use of Direct Manipulation and Natural Language," Proceedings of CHI'89 Human Factors in Computing Systems, Austin, TX, 1989, pp. 227-234.

Cowan, N. "On Short and Long Auditory Stores," Psychological Bulletin (96), 1984, pp. 341-470.

diSessa, A.A. "A Principled Design for an In-

tegrated Computational Environment," Human-Computer Interaction (1:2), 1985, pp. 1-47.

diSessa, A.A. "Models of Computation," in User Centered System Design, D.A. Norman and S.W. Draper (eds.), Lawrence Erlbaum Associates, Hillside, NJ, 1986, pp. 201-218.

Egan, D.E. "Individual Differences in Human-Computer Interaction," in Cognitive Science and its Application for Human-Computer Interaction, H. Helendar (ed.), Elsevier Science Publishers B.V., Hillsdale, NJ, 1988, pp. 543-568.

Execucom Systems Corporation. Cases and Models Using IFPS, Execucom, Austin, TX, 1979.

Fitter, M. "Towards More Natural Interactive Systems," International Journal on Man-Machine Studies (11:3), 1979, pp. 339-350.

Fowler, C.J.H., Macaulay, L.A., and Fowler, J.F. "The Relationship Between Cognitive Style and Dialogue Style: An Explorative Study," in People and Computers: Designing the Interface, P. Johnson and S. Cook (eds.), Cambridge University Press, New York, NY, 1985, pp. 186-198.

Gaines, B. "The Technology of Interaction-Dialogue Programming Rules," International Journal of Man-Machine Studies (14:1), 1981, pp. 133-150.

Gaver, W. "Auditory Icons: Using Sound in Computer Interfaces," Human-Computer Interaction (2:2), 1986, pp. 167-177.

Gaver, W.W. "The SonicFinder: An Interface that Uses Auditory Icons," Human-Computer Interaction (4:1), 1989, pp. 67-94.

Gerlach, J.H. and Kuo, F.Y. "Formal Development of Hybrid User-Computer Interfaces with Advanced Forms of User Assistance," Journal of Systems and Software (16:3), November 1991, pp. 169-184.

Gong, R. and Elkerton, J. "Designing Minimal Documentation Using a GOMS Model: A Usability Evaluation of an Engineering Approach," Proceedings of CHI'90 Human Factors in Computing Systems, Seattle, WA, 1990, pp. 99-106.

Good, M.D., Whiteside, J.A., Wixon, D.R., and Jones, S.J. "Building a User-Derived Interface," Communications of the ACM (27:10), October 1984, pp. 1032-1043.

Gould, J.D., Lewis, C., and Barnes, V. "Cursor

Movement During Text Editing," ACM Transactions on Office Information Systems (3:1), January 1985, pp. 22-34.

Gould, J.D. and Lewis, C. "Designing for Usability: Key Principles and What Designers Think," Communications of the ACM (28:3), March 1985, pp. 300-311.

Grudin, J. "The Case Against User Interface Consistency," Communications of the ACM (32:10), October 1989, pp. 1164-1173.

Grudin, J. "The Computer Reaches Out: The Historical Continuity of Interface Design," Proceedings of CHI'90 Human Factors in Computing Systems, Seattle, WA, 1990, pp. 261-268.

Halasz, F.G. "Reflections on Notecards: Seven Issues for the Next Generation of Hypermedia Systems," Communications of the ACM (31:7), July 1988, pp. 836-852.

Halasz, F.G. and Moran, T.P. "Analogy Considered Harmful," Proceedings of the Conference on Human Factors in Computing Systems, Gaithersburg, MA, 1982, pp. 383-386.

Halasz, F.G. and Moran, T.P. "Mental Models and Problem Solving in Using a Calculator," Proceedings of CHI'83 Human Factors in Computing Systems, Austin, TX, 1983, pp. 212-216.

Hartson, H.R. and Hix, D. "Human-Computer Interface Development: Concepts and Systems for Its Management," Computing Surveys (21:1), March 1989, pp. 5-92.

Hauptmann, A.G. "Speech and Gestures for Graphic Image Manipulation," Proceedings of CHI'89 Human Factors in Computing Systems, Austin, TX, 1989, pp. 241-245.

Hendrickson, J.J. "Performance, Preference, and Visual Scan Patterns on a Menu-Based System: Implications for Interface Design," Proceedings of CHI'89 Human Factors in Computing Systems, Austin, TX, 1989, pp. 217-222.

Hiltz, S.R. and Kerr, E.B. "Learning Modes and Subsequent Use of Computer-Mediated Communication Systems," Proceedings of CHI'86 Human Factors in Computing Systems, Boston, MA, 1986, pp. 149-155.

Houghton, R.C. "Online Help Systems: A Conspectus," Communications of the ACM (27:2), February 1984, pp. 126-133.

Hutchins, E.L., Hollan, J.D. and Norman, D.A. "Direct Manipulation Interfaces," in User

Centered System Design, D.A. Norman and S.W. Draper (eds.), Lawrence Erlbaum Associates, Hillsdale, NJ, 1986, pp. 87-124.

Jagodzinski, A.P. "A Theoretical Basis for the Representation of On-Line Computer Systems to Naive Users," International Journal of Man-Machine Studies (18), 1983, pp. 215-252.

Jarvenpaa, S.L. and Dickson, G.W. "Graphics and Managerial Decision Making: Research-Based Guidelines," Communications of the ACM (31:6), June 1988, pp. 764-774.

Johnson, E.J. and Payne, J.W. "Effort and Accuracy in Choice," Management Science (31:4), April 1985, pp. 395-414.

Johnson, E.J., Payne, J.W., and Bettman, J.R. "Information Displays and Preference Reversals," Organizational Behavior and Human Decision Processes (42), 1988, pp. 1-21.

Jones, W.P. and Dumais, S.T. "The Spatial Metaphor for User Interfaces: Experimental Tests of Reference by Location versus Names," ACM Transactions on Office Information Systems (4:1), January 1986, pp. 42-63.

Kellogg, W.A. and Breen, T.J. "Evaluating User and System Models: Applying Scaling Techniques to Problems in Human-Computer Interaction," Proceedings of CHI + GI 1987 Human Factors in Computing Systems, Toronto, Ontario, 1987, pp. 303-308.

Kieras, D.E. and Bovair, S. "The Role of Mental Knowledge in Learning to Operate a Device," Cognitive Science (8), 1984, pp. 191-219.

Kieras, D.E. and Polson, P.G. "An Approach to the Formal Analysis of User Complexity," International Journal of Man-Machine Studies (22), 1985, pp. 365-394.

Laird, J.E., Newell, A., and Rosenbloom, P.S. "SOAR: An Architecture for General Intelligence," Artificial Intelligence (33), 1987, pp. 1-64.

Landauer, T.K., Galotti, K.M., and Hartwell, S. "Natural Command Names and Initial Learning: A Study of Text-Editing Terms," Communications of the ACM (26:7), July 1983, pp. 495-503.

Lerch, F.J., Mantei, M.M., and Olson, J.R. "Skilled Financial Planning: The Cost of Translating Ideas into Action," Proceedings of CHI'89 Human Factors in Computing Systems, Austin, TX, 1989, pp. 121-126.

Lewis, C., Polson, P., Wharton, C., and Rieman,

J. "Testing a Walkthrough Methodology for Theory-Based Design of Walk-Up and Use Interfaces," Proceedings of CHI'90 Human Factors in Computing Systems, Seattle, WA, 1990, pp. 235-242.

Lewis, M.W. and Anderson, J.R. "Discrimination of Operator in Problem Solving: Learning from Examples," Cognitive Psychology (17), 1985, pp. 26-65.

Lohse, J. "A Cognitive Model for the Perception and Understanding of Graphs," Proceedings of CHI'91 Human Factors in Computing Systems, New Orleans, LA, 1991, pp. 137-144.

Lotus Development Corporation. Lotus 1-2-3, Lotus Development Corporation, Cambridge, MA, 1989.

Mack, R.L., Lewis, C.H., and Carroll, J.M. "Learning to Use Word Processors: Problems and Prospects," ACM Transactions on Office Information Systems (1:3), July 1983, pp. 254-271.

Maclean, A., Young, R.M., and Moran, T.P. "Design Rationale: The Argument Behind the Artifact," Proceedings of CHI'89 Human Factors in Computing Systems, Austin, TX, 1989, pp. 247-252.

Malone, T.W. "Heuristics for Designing Enjoyable User Interfaces: Lessons from Computer Games," in Human Factors in Computing Systems, J.C. Thomas and M. Schneider (eds.), Ablex, Norwood, NJ, 1984, pp. 1-12.

Mandler, J.M., Seegmiller, D., and Day, J. "On the Encoding of Spatial Information," Memory Cognition (5), 1977, pp. 10-16.

Mayer, R.E. "The Psychology of How Novices Learn Computer Programming," Computing Surveys (13:1), March 1981, pp. 121-141.

McDonald, J.E. and Schvaneveldt, R.W. "The Application of User Knowledge to Interface Design," in Cognitive Science and Its Application for Human-Computer Interaction, R. Guinden (ed.), Lawrence Erlbaum Associates, Hillsdale, NJ, 1988, pp. 289-338.

Mehlenbacher, B., Duffy, T.M., and Palmer J. "Finding Information on a Menu: Linking Menu Organization to the User's Goals," Human-Computer Interaction (4:3), 1989, pp. 231-251.

Miller, L.A. and Thomas, J.C., Jr. "Behavior Issues in the Use of Interactive Systems," International Journal of Man Machine Studies

(9), 1977, pp. 509-536.

Moran, T. "An Applied Psychology of the User," Computing Surveys (13:1), March 1981, pp. 1-12.

Morland, D.V. "Human Factors Guidelines for Terminal Interface Design," Communications of the ACM (26:7), July 1983, pp. 100-104.

Mozeico H. "A Human/Computer Interfaces to Accommodate User Learning Stages," Communications of the ACM (25:2), February 1982, pp. 100-104.

Myers, B.A. "The Importance of Percent-Done Indicators for Computer-Human Interfaces," Proceedings of CHI'85 Human Factors in Computing Systems, San Francisco, CA, 1985, pp. 11-17.

Nakatani, L.H., Egan, D.E., Ruedisueli, L.W., Hawley, P.M., and Lewart, D.K. "TNT: A Talking Tutor 'N' Trainer for Teaching the Use of Interactive Computer Systems," Proceedings of CHI'86 Human Factors in Computing Systems, Boston, MA, 1986, pp. 29-34.

Newell, A. and Card, S. "The Prospects of Psychological Science in Human-Computer Interaction," Human Computer Interaction (1:3), 1985, pp. 209-242.

Newell, A. and Card, S. "Straightening Out Softening Up: Response to Carroll and Campbell," Human Computer Interaction (2:3), 1986, pp. 251-267.

Newell, A. and Simon, H.A. Human Problem Solving, Prentice-Hall, Englewood Cliffs, NJ, 1972.

Nickerson, R.S. "Why Interactive Computer Systems Are Sometimes Not Used by the People Who Might Benefit from Them," International Journal of Man-Machine Studies (4), 1981, pp. 469-483.

Norman, D.A. "Design Rules Based on Analysis of Human Error," Communications of the ACM (26:4), April 1983, pp. 254-258.

Norman, D.A. "Cognitive Engineering," in User Centered System Design, D.A. Norman and S.W. Draper (eds.), Lawrence Erlbaum Associates, Hillsdale, NJ, 1986, pp. 31-61.

Olson, J.R. and Nilsen, E. "Analysis of the Cognition Involved in Spreadsheet Software Interaction," Human-Computer Interaction (3:4), 1987, pp. 309-349.

Olson, J.R. and Olson, G.M. "The Growth of Cognitive Modeling in Human Computer Interaction Since GOMS," Human Computer Interaction (5:2-3), 1990, pp. 221-266.

Olson, J.R. and Rueter, H.H. "Extracting Expertise from Experts: Methods for Knowledge Acquisition," Journal of Expert Systems (4:3), 1987, pp. 152-168.

Payne, S.J. and Green, T.R.G. "Task-Action Grammars: A Model of the Mental Representation of Task Languages," Human-Computer Interaction (2:2), 1986, pp.93-134.

Phillips, M.D., Howard, B.S., Ammerman, H.L., and Fligg, C.M., Jr. "A Task Analytic Approach to Dialogue Design," in Handbook of Human-Computer Interaction, M. Helander (ed.), Elsevier Science Publishers, Amsterdam, 1988, pp. 835-857.

Polson, P., Muncher, E., and Englebeck, G. "A Test of a Common Elements Theory of Transfer," Proceedings of CHI'86 Human Factors in Computing Systems, Boston, MA, 1986, pp. 78-83.

Polson, P. "The Consequences of Consistent and Inconsistent Interfaces," in Cognitive Science and Its Application for Human-Computer Interaction, R. Guinden (ed.), Lawrence Erlbaum Associates, Hillsdale, NJ, 1988, pp. 59-107.

Powers, M., Lashley, C., Sanchez, D., and Shneiderman, B. "An Experimental Comparison of Tabular and Graphical Data Presentation," International Journal of Man-Machine Studies (20), 1984, pp. 545-566.

Rasmussen, J. "The Human as a System Component," in Human Interaction with Computers, H.T. Smith and T.R.G. Green (eds.), Academic Press, London, 1980, pp. 67-96.

Reisner, P. "Using a Formal Grammar in Human Factors Design of an Interactive Graphics System," IEEE Transactions on Software Engineering (7:2), March 1981, pp. 1409-1411.

Remus, W. "An Experimental Investigation of the Impact of Graphical and Tabular Data Presentations of Decision Making," Management Science (30:5), May 1984, pp. 533-542.

Remus, W. "A Study of Graphical and Tabular Displays and Their Integration with Environmental Complexity," Management Science (33:9), September 1987, pp. 1200-1204.

Sein, M.K. and Bostrom, R.P. "Individual Differences and Conceptual Models in Training Novice Users," Human-Computer Interaction (4:3), 1989, pp. 197-229.

Shiffrin, R.M. and Schneider, W. "Controlled and Automatic Information Processing: Perceptual

Learning, Automatic Attending, and a General Theory," Psychological Review (84:2), March 1977, pp. 127-190.

Shneiderman, B. Designing the User Interface, Addison-Wesley, Reading, MA, 1987.

Somberg, B.L. "A Comparison of Rule-Based and Potentially Constant Arrangements of Computer Menu Items," Proceedings of CHI + GI 1987 Human Factors in Computing Systems, Toronto, Ontario, 1987, pp. 255-260.

Trevellyan, R. and Browne, D.P. "A Self-Regulating Adaptive System," Proceedings of CHI + GI 1987 Human Factors in Computing Systems, Toronto, Ontario, 1987, pp. 103-107.

Waren, Y. "Mental Models in Learning Computerized Tasks," in Psychological Issues of Human Computer Interaction in the Work Place, M. Frese, E. Ulich, and W. Dzida (eds.), Elsevier Science Publishers, Amsterdam, 1987, pp. 275-294.

Weimer, D. and Ganapathy, S.K. "A Synthetic Visual Environment with Hand Gesturing and Voice Input," Proceedings of CHI'89 Human Factors in Computing Systems, Austin, TX, 1989, pp. 235-240.

Witten, I.H., Cleary, J., and Greenberg, S. "On Frequency-Based Menu-Splitting Algorithms," International Journal of Man-Machine Studies (21), 1984, pp. 135-148.

Wixon, D., Holtzblatt, K., and Knox, S. "Contextual Design: An Emergent View of System Design," Proceedings of CHI'90 Human Factors in Computing Systems, Seattle, WA, 1990, pp. 329-336.

Young, R.M. "The Machine Inside the Machine: Users' Models of Pocket Calculators," International Journal on Man-Machine Studies (15), 1981, pp. 51-85.

Young, R.M. and Barnard, P.J. "The Use of Scenarios in Human-Computer Interaction Research: Turbo-Charging the Tortoise of Cumulative Science," Proceedings of CHI + GI 1987 Human Factors in Computing Systems, Toronto, Ontario, 1987, pp. 291-296.

Young, R.M., Barnard, P., Simon, T., and Whittington, J. "How Would Your Favourite User Model Cope with These Scenarios?" SIGCHI Bulletin (20:4), April 1989, pp. 51-55.

Young, R.M. and Whittington, J. "Using a Knowledge Analysis to Predict Conceptual Errors in Text-Editor Usage," Proceedings of CHI '90 Human Factors in Computing Systems, Seattle, WA, 1990, pp. 91-97.

## About the Authors

James H. Gerlach is associate professor of information systems at the University of Colorado at Denver. In addition to human-computer interaction, his research interests include software engineering and EDP auditing. His work has appeared in ACM Transactions on Information Systems, IEEE Computer, Decision Support Systems, Journal of Systems and Software, The Accounting Review, and Auditing. Dr. Gerlach received an M.S. in computer science and a Ph.D. in management, both from Purdue University.

Feng-Yang Kuo is assistant professor of information systems in the Graduate School of Business, University of Colorado at Denver. He received his Ph.D. in management information systems from the University of Arizona. His research interests include human-computer interaction, database management, office automation, and decision support systems. Dr. Kuo's work has appeared in MIS Quarterly, Communications of the ACM, Information Management, and Decision Support Systems.

# Executive Overview

It is widely recognized that partnership arrangements are likely to play an increasingly common role in the development and application of new technology. For ambitious projects, the stakes may be too high for any one organization to foot the entire bill and take all of the risks. Partnership arrangements can be extremely effective in bringing together complementary resources and sharing the risks and rewards for high-payoff projects. This paper describes such an arrangement between the United Services Automobile Association (USAA) and IBM.

USAA is a very large financial services company serving a specialized market of active and retired military officers. Some 80 percent of its revenue comes from property and casualty insurance. The company manages the largest mail order business in the country, with a huge daily volume of incoming and outgoing mail (100,000 and 250,000 respectively). It also operates the largest automatic telephone call distribution system in the world.

A great variety of paper documents is generated by such a massive operation. The effort of managing the resulting paper files had drawn the attention of USAA senior executives since the early 1980s. The CEO of the company had an early vision of doing away with most of the paper through the use of imaging technology. Prototype imaging systems were developed in the mid-80s in an attempt to reduce the flood of paper. The lack of standards and the relatively primitive technology of the time precluded a really satisfactory solution to the problem.

Discussion about possible cooperative arrangements to develop imaging technology had been initiated between USAA and IBM executives as early as 1982. There were pockets of support for the idea within IBM, but it was not until 1987 that sufficient corporate interest was generated for the deal to be put together. Once this was done, however, both partners became thoroughly committed to the success of the venture.

In order for a partnership to work, a number of conditions must be created. There must be a clear set of compatible objectives, a strong top-level commitment, complementary resources and skills, a willingness to respond flexibly to the inevitable problems that arise, and mutual trust. Each party must bring something to the table. USAA brought a vision of the “paperless” processing system as a way out of its growing deluge of paper, a number of years of experience with earlier imaging systems, and a willing test bed for proving the hardware, software, and processing procedures in a very demanding environment. IBM brought its large-scale resources, broad technology base, and a desire to develop a product line that would satisfy what top management saw as potentially a very important market segment.

The partnership proved to be a great success. The imaging system went “live” in the latter half of 1988, and by the third quarter of 1989 all incoming mail was handled for the underwriting, sales, and service areas in the property and casualty line of business. By the first quarter of 1990, over 1,400 image workstations had been installed, serving over 2,000 users. Millions of dollars per year were saved in storage space and labor costs. Storage space shrank to a tiny fraction of the amount formerly required. It became possible to substantially re-engineer the management of work and the control of documents.

The case presents an interesting example of a successful strategic partnership. It illustrates the benefits that can accrue to both partners if things are done right. The article discusses the conditions that must be put into place and the supporting roles that must be provided, if a partnership stands a strong chance of succeeding.
