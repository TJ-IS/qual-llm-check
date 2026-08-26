---
otero_id: 17203
otero_key: "AZZJV3NG"
title: "A paradigm for active decision support"
authors: "Sridhar A. Raghavan"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90065-j"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
JANUS

# A paradigm for active decision support

Sridhar A. Raghavan

CIS Department, Bentley College, Waltham, MA 02254, USA

Active decision support is concerned with developing advanced forms of decision support where the support tools are capable of actively participating in the decision making process, and decisions are made by fruitful collaboration between the human and the machine. It is currently an active and leading area of research within the field of decision support systems. The objective of this paper is to share the details of our research in this area. We present our overall research strategy for exploring advanced forms of decision support and discuss in detail our research prototype called JANUS that implements our ideas. We establish the contributions of our work and discuss our experiences and plans for future.

Keywords: Decision support, Active support, Intelligent support, Intelligent agents, Idea stimulation, Critiquing.

## 1. Purpose and organization

This paper has three major objectives: provide a brief review of the key ideas in the active decision support systems area; present our overall strategy for exploring advanced forms of decision support; and discuss in detail JANUS, the research prototype that implements our ideas.

The paper is organized into five sections. Section 2 provides an introduction to the concept of active decision support and reviews the key works from literature. Section 3 describes our research framework for exploring active decision support ideas. Section 4 is devoted to the detail description of the JANUS system. The system is described in terms of its goals, functional features, architectural design, and annotated sample session. In section 5, we establish the contributions of the JANUS work and establish its relationships to relevant prior works. We also reflect on the outcomes of the JANUS project, provide a list of the key research problems that have emerged, and discuss our plans for future work. The final section summarizes the key aspects of the paper.

## 2. Active decision support

## 2.1. Introduction

The concept of active decision support is an advanced variation and refinement of the traditional DSS philosophy [4]. Whereas the traditional DSS philosophy merely calls for computer-based support tools that can enhance human decision making, the active decision support concept advocates developing advanced forms of support where the underlying tools are capable of actively participating in the decision making process.

The notion of active participation in decision making can represent a broad range of ideas such as: monitoring the decision making processes of the user and detecting inconsistencies and problems; understanding and inferring users context, goals, and intentions and automatically scheduling and carrying out the required activities; alerting the decision maker to the aspects of the problem and problem-solving processes that are not getting enough attention; criticizing decision maker's actions and decisions from various perspectives; stimulating creative ideas; serving as a sounding board for ideas; and carrying on insightful conversations with the decision maker that can lead to creative formulation and solution of decision problems.

Active decision support ideas stand in striking contrast to the approaches underlying the conventional DSSs. The latter are largely passive partners in decision making. They are passive in the sense that they merely place a set of useful facilities at the disposal of a decision maker and expect that the decision maker will somehow exploit these facilities effectively for decision making. They are not capable of taking initiatives - they can only respond to users requests. In essence, they provide a weak form of support that does not exploit the full power and potential of computer-based support.

## 2.2. The key premises

The key premises underlying the active decision support research can be summarized as follows:

\- Decision support systems are essentially man-machine systems for enhanced decision making [16]. Since man and machine have distinguishing characteristics and skills, a potentially promising synergy exists between them. This synergy can be realized by properly distributing the roles, skills, and responsibilities between the man and the machine within the man-machine setup [27].

\- It is possible for the machine component to play active roles during decision making without violating the fundamental support philosophy of decision support systems.

\- It is necessary to incorporate active roles in the machine component for fully exploiting the potential power of a computer.

\- AI/Expert systems technology can provide the implementation techniques necessary for implementing active support ideas.

## 2.3. Review of key ideas

Research in active DSSs is carried out under a variety of labels such as intelligent decision support systems $[5]$ , symbiotic DSS $[8]$ , and joint man-machine cognition $[27,16]$ . Currently there are four broad threads of ideas in this area: idea stimulation, autonomous processes, expert systems, and active elicitation and structuring.

## 2.3.1. Idea stimulation

Idea stimulation is widely recognized as an important form of active decision support $[28,8,6,12,16]$ . There are at least two systems that illustrate this approach $[6,12]$ . Later we will also discuss how this approach is pursued in our JANUS system.

Krcmar et al. [6] have developed a DSS that can help users identify new ways to exploit information technology as a competitive weapon. They use questions as triggers for stimulating new ideas. They generate the trigger questions by using a theoretical model that is widely used for studying information technology and its impacts.

The underlying model provides primitive variables for characterizing information technology, impacts, and their inter-relationships. Each relationship in this model represents a potentially new idea for exploiting information technology as a competitive weapon. This provides a basis for stimulating new ideas – facilitating the user to think about the potential relationships between the variables in the model. The system accomplishes this by systematically instantiating the model variables, and posing questions about the possible relationships. Since the number of questions at any point in time can be combinatorially explosive, the system uses contextual information for pruning down the irrelevant ones. The authors do not provide any system performance measures.

Whereas Krcmar uses a problem-specific model for idea stimulation, Nierenberg [12] employs a set of domain independent modules for stimulating ideas. Their system, named Idea Generator, is essentially a decision structuring tool. The underlying structuring technique uses primitives such as problem, goal, actions, and strengths of relationships for structuring a decision problem. The system uses several idea generation modules for helping the user identify novel actions.

Each idea generation module in the system is based on a specific scheme for provoking novel thoughts. Some of the schemes used by the modules are:

\- Think of similar situations.

\- Think of metaphors for the situation.

\- Think from other perspectives - that is think of how other people may solve the problem.

\- Focus on goals one at a time and then collectively.

\- Reverse your goals and actions.

\- Focus on the people who will be affected by your actions.

The user can collect the ideas they generate into a temporary workspace. The system provides facilities for grouping, pruning, and synthesizing these ideas. Authors claim that the system has been used in several simple business problems and has proved to be quite effective.

## 2.3.2. Autonomous processes

Here the active support is implemented as a set of daemons or agents that watch over the decision making process of the user and trigger appropriate responses autonomously. In [14] we proposed several initial ideas in this direction: observing decision maker's activities and scheduling the necessary related tasks; keeping track of the pending tasks and ensuring that they are completed; eliciting and enforcing constraints; forcing a divergent process if the user is judged to be prematurely converging; and forcing a convergent process if user appears to be disorganized with too many tasks and thoughts.

Manaheim [8] has proposed a general architecture for active DSSs based on autonomous processes. The key aspect of his architecture is the existence of two kinds of processes in the system: user directed, and system directed. User directed processes correspond to tasks in conventional passive DSS. For example, retrieving data, requesting analysis etc. The system directed processes, on the other hand, are processes that are autonomously initiated by the system while playing its role as an independent and active agent in the decision making process. For example, the system initiating processes for consistency checking and critiquing at periodic intervals.

The ability of the system to play active roles in this architecture rests on the following critical factors: understanding the decision making processes of the user; having criteria for judging the quality of the decision making process; and having strategies for improving the process. Once these requirements are met, the system can closely monitor the decision making process of the user, and intervene as and when necessary to criticize and offer suggestions. The system can raise pointed questions and extract rationale and justifications for users actions, and force him to think of additional alternatives and contingencies. It can also anticipate users needs, schedule processes and perform useful analyses in advance.

Since Manaheim's architecture rests on having an explicit model of decision process (he uses the term problem-working process), much of his work [7,8,9] focuses on developing the necessary theoretical bases. At present there are no prototype systems to demonstrate his ideas.

## 2.3.3. Expert systems as active DSSs

One could argue that expert systems are active DSSs because they can be used merely for advice rather than for decisions. But, they make very poor DSSs when used in this fashion as their design makes them suitable only for playing a decision making/recommendation role. However, it is possible to develop expert systems to function effectively as active DSSs. The key is to develop them as critiquing agents $[10,11,24]$ rather than as expert decision making agents.

Miller [10] provides a comprehensive description of the ATTENDING system, a critiquing expert system from the medical domain. The system becomes operative only after the user has a tentative decision. The system interacts with the user and gathers the details of the problem, users decision, rationale and justifications. This dialog process itself can be very insightful to the decision maker as he is forced to communicate and justify his decision to the system. After the details are collected, the system reconstructs a plausible decision making process using its knowledge base and internal models, and identifies potential problems and possible improvements.

A closely related approach is to endow the expert system with reasoning processes of different problem-solving perspectives and use them for critiquing. For example, a decision maker can greatly benefit by getting his business decision analyzed from the marketing perspective, finance perspective, legal perspective and so on. AI systems such as PARRY [3] and POLITICS [2] have demonstrated the feasibilities of these approaches. It may be possible to extend this approach for playing other kinds of generic roles such as devil's advocate, adversarial, optimistic, pessimistic, conservative, aggressive personalities and so on.

Another popular approach for active support is to use embedded intelligent agents in the decision support system for purposes such as: automatic selection and construction of models, explaining the results of model runs, recognizing patterns in data, and making complex retrievals and inferences. Though these are valid active support ideas, they are less interesting from our perspective and therefore are not discussed further.

## 2.3.4. Active problem elicitation and structuring

Here the system is based on a problem/decision structuring technique that is suitable for problems of interest. Some examples of such structuring techniques are goal-oriented structuring, analytical hierarchy structuring, constraint satisfaction paradigm etc. Since structuring techniques are normative models of decision making, they immediately provide: a basis for active problem elicitation, a basis for making recommendations, criteria for judging the decision making process, and a framework for incorporating idea stimulation and other machine-based personalities. Thus this approach makes it easier to implement many of Manaheim's ideas by avoiding the problem of understanding the unconstrained decision making process of the user, a critical requirement of his architecture.

The key objective a system that is based on this approach is helping the users to effectively organize and structure their own knowledge and expertise for solving problems. The GODESS system $[13]$ is an excellent example of such a system. The acronym GODESS stands for goal-oriented decision structuring system. Goal-oriented structuring is an adaptation of the means-ends analysis technique that is widely used in AI planning systems $[25]$ . Here a problem is structured in terms of goals, actions, preconditions, states, factors, and strengths of relationship between these components.

GODESS can play both support and decision-making roles. In the support role, the system carries on an active dialog with the user and formulates the decision problem in terms of the primitives of the goal-oriented structuring technique. The system is domain-independent and its only knowledge is that of the structuring technique. Therefore, it relies on the decision maker to be knowledgeable about the problem, and supply the problem-specific knowledge.

GODESS uses an And-Or tree [1] to structure the details of the problem as they unfold during the elicitation process. The tree is used throughout the dialog process for meaningfully communicating with the user, making decisions about how the focus should shift between various parts of the problem, and determining what aspects of the problem need further elaboration. At the end of problem information gathering, the system processes the information accumulated in the And-Or tree to make recommendations.

The GODESS work adds several key ideas for developing active decision support: active problem elicitation and decision structuring; domain independent decision support; exploiting users' knowledge of the decision problem; and adapting AI problem-solving techniques for decision structuring. Though the system does not use any specialized domain knowledge, its architectural framework does not preclude the incorporation of problem-specific knowledge bases.

## 2.4. Summary

We discussed four broad themes of ideas for developing active decision support: idea stimulation, autonomous processes, expert critiquing systems, and active elicitation and structuring techniques. Though we described them as disjoint ideas, they are closely related to each other and can be easily combined together.

## 3. Our research framework

## 3.1. Overall context and goals

The overall context of our research is developing advanced decision support environments where man and machine can engage in an effective partnership during decision making. We visualize these environments as an integrated set of tools and facilities that operationalize the various alternative strategies for decision support. We recognize three major strategies for developing decision support: resource support, process support, and intellectual support.

In the resource support approach, the focus is on providing the information and the analytical resources that are necessary for decision making. This has been the focus of much of the traditional DSSs. Examples of the resources needed for decision making are:

\- Data bases

\- Models

\- Statistical models

\- OR/MS, optimization models

\- Other Quantitative models

\- Qualitative and Symbolic models

\- Causal models

\- Knowledge bases

\- Domain specific

\- General heuristics

\- Expert system modules

In the process support approach the emphasis is on addressing the generic needs of decision making processes. Some of the operational levels goals of this approach are:

\- Supporting the planning, organizing, and the execution of complex and inter-related tasks that constitute decision-making

\- Supporting flexible process sequences during decision making

\- Supporting interruption and resumption

\- Simulating decisions and studying their potential consequences

\- Supporting multiple worlds/contexts for exploring potential scenarios

\- Providing various schemes for choice reduction

\- Maintaining details about intermediate decisions and their inter-relationships

In the intellectual support, the focus is on higher level cognitive activities of decision making including innovation and creativity. In operational terms, it translates into the following kinds of support:

\- Active elicitation and structuring of problems

\- Surfacing the assumptions, justifications and contingencies

\- Stimulating creative ideas, learning, and discovery

\- Suggesting alternatives and improvements

\- Critiquing decision makers' processes, judgements, and decisions

\- Overcoming decision makers tunnel vision, fixations, and biases

\- Promoting convergent and divergent thinking

\- Employing machine-based personalities for analyzing problems from diverse perspectives

\- The machine playing various kinds of sounding board roles. For example: playing a devil's advocate role

In our research we concentrate on process support and intellectual support approaches. Our goal is to resolve the conceptual and implementation problems underlying these approaches. We do not address active support as an explicit goal, as it is a constant theme throughout our research.

## 3.2. Methodology

The key intellectual problem in our research is bridging the gap between the conceptual ideas and the implementation techniques. There are uncertainties associated with both the ends. We cannot be certain that our ideas represent valid abstractions; are at the right level; and carry enough content and direction for developing implementations. Again, we cannot be certain that our ideas can be implemented using the available implementation techniques. The situation is very similar to artificial intelligence (AI) research, where research often begins with a limited and high level understanding of the problem, and a lot of uncertainty about the solution approaches – both at the conceptual and implementation level. The ideal research methodology for such situations is the exploratory systems development process, a method that has a long and established tradition in AI research.

In the exploratory systems development paradigm, the research proceeds as follows. The researcher begins by developing an initial prototype system to articulate his initial understanding of the problem and solution approach. He then uses this prototype as the experimental vehicle/environment for refining and overcoming the problems associated with his ideas and implementation techniques. He evolves the prototype continuously as he recognizes and resolves the problems. When the research is completed, the prototype represents a clear expression of both the problems and solutions to the problems. The prototype plays a critical role in the research process as well as becomes a significant output of the research.

The power of the exploratory systems development as a research paradigm can be traced to the following: implementing ideas on a machine makes exacting demands on conceptual clarity, rigor, and resolution of details; therefore getting a working implementation is a very valuable research process and a robust test of the ideas.

Within the overall paradigm of exploratory systems development, we use the following step-by-step approach:

\- Pick a good structuring technique. Use it as the basis for the steps that follows.

\- Develop a machine representation for organizing the problem details

\- Enhance the representation for primitives such as assumptions, justifications, and contingencies.

\- Develop elicitation strategies

\- Implement process support mechanisms - Identify criteria and strategies for improving the decision making process

\- Incorporate machine personalities that can stimulate thinking and enhance the problem solving process

\- Develop knowledge-bases needed for the machine personalities. Develop modules for what-if, sensitivity, and contingency analyses.

## 3.3. Conceptual architecture

The conceptual architecture we use for our exploration is shown in figure 1. We recognize four major functional components: Representation, Elicitation, Analysis, and User interface.

Representation provides the schemes for representing information internally, and mechanisms for retrieval and inferencing. It also provides the base for organizing and utilizing domain specific and generalized knowledge bases. Analysis block provides for internal consistency checks, constraint satisfaction, triggers and daemons, sensitivity analysis, scenario analysis, and decision simulation.

Elicitation carries dialog generation strategies, and active agents for critiquing, stimulating ideas, and playing partnerships roles. User interface provides high bandwidth communication, process support mechanisms for: mixed-mode initiative i.e the ability to shift control between the system and the user freely, flexible process sequences, interruption and resumptions.

![](/api/attachments/AZZJV3NG/fulltext/images/bbc91d51b659a80f37653b4f01fb82ad964a013c884ebb0401cb8ac88917b4b0.jpg)  
Fig. 1. Conceptual architecture.

The structuring methodology underlying the system is the conceptual glue that unifies the architectural components of the system. It provides the primitives and vocabulary for thinking about and articulating domain problems, graphical primitives for man-machine communication, rules for internal consistency, methods for analysis, and basis for making recommendations.

## 4. The description of the JANUS system

JANUS is an experimental research prototype we have developed for exploring our research ideas.

The system is implemented in C-Prolog (8000 lines) under VAX/Ultrix. The system uses Saaty's analytical hierarchical process [26] as the underlying decision structuring methodology.

## 4.1. Structuring primitives

The basic primitives of the analytical hierarchical process are Goals, Factors, Subfactors, and Judgments. In the JANUS system we have added three additional primitives – Notes, Justifications and Contingencies. Note is an arbitrary piece of text or annotation that can be attached to any element of the representation. It can be used by the decision maker for leaving reminders for himself or recording down arbitrary thoughts about various aspects of the problem. The justification primitive is used for capturing the assumptions and premises underlying the elements of a decision problem. The contingency primitive is used for capturing the relationships between the elements of the problem and the exogenous variables.

![](/api/attachments/AZZJV3NG/fulltext/images/1c8e41a66cbf544b56fb97434e4ea02c72ec3426cc0f873885f51c6caa3c890a.jpg)  
Fig. 2. The JANUS structuring primitives.

Figure 2 illustrates the relationships between these primitives in the context of a simple decision problem.

## 4.2. System features

The following is the summary of the major functional features/capabilities implemented by the system:

## Elicitation

\- Active elicitation and structuring of the details of a decision problem i.e goals, factors, alternatives, and judgements.

\- In addition to the essential details, the system is also capable of eliciting and capturing the assumptions, justifications and contingencies behind users statements.

\- A keyword facility automatically extracts key words from the input text, and organizes the text for flexible retrieval.

\- The system provides a notepad facility for creating and retrieving notes. The notes are arbitrary pieces of text that can be attached to any element of the problem. They can be used in a variety of ways. For example, leaving reminders to oneself; jotting down important ideas for later use etc.

\- A constraint/contingency entry and checking facility for imposing constraints and contingencies on judgments made by the decision maker.

## Process Support

\- The system supports dual initiative. That is, the overall decision making process can be controlled either by the user or by the system. The control can be freely switched between them at any point in time.

\- The system supports flexible process sequences. That is, the decision structuring process is not constrained to follow any predetermined order. Though the underlying structuring strategy has a top-down orientation, the system permits a high degree of flexibility regarding the order in which the details are collected. For example, the user can describe factors before alternatives and vice versa. He can also defer answering questions if he feels a need to do so. The system will keep track of the loose ends.

\- The system supports interruptions and resumptions by providing mechanisms for saving and restoring problem contexts. This mechanism is also used by the system for accumulating its data base of solved problems.

\- Users can customize the various aspects of the structuring process through the user programmability feature.

## Decision Recommendation & Analysis

\- The system can make decision recommendations by performing the calculations defined by the analytical hierarchy process.

\- While describing/explaining its recommendations, the system can integrate the relevant notes, assumptions, justifications and contingencies.

\- The user can perform what-if analyses by changing the values of the judgments and contingency variables.

## Mind Expansion

\- The system provides intellectual support through a “mind expansion module”. The module supports four different personalities/roles: Spock, Bozo, Mom, and Aesop.

\- Spock emulates logical thinking.

\- Bozo emulates lateral thinking.

\- Mom emulates a personality that is obsessed with justifications and counter arguments.

\- Aesop is a story teller.

## Knowledge Base

\- The system provides facilities for developing a database of solved problems for use by the mind-expansion module for suggesting new ideas to the user. The problems are organized and indexed using the primitives of the structuring model and key words.

\- The knowledge base of the mind-expansion personalities are represented in a declarative form using templates. This facilitates the ease of evolving and enhancing the knowledge bases.

## Customization

\- A keyword facility for defining keywords and complex relationships among keywords such as syntactical synonyms, semantic synonyms, antonyms, and hierarchies.

\- The system provides appropriate entry and exit points for the user to define daemons and insert code segments for customizing the various aspects of the structuring process.

## 4.3. Design overview

## 4.3.1. Architecture

The architecture of the system is shown in figure. 3. At the overall level the modules in the system are: user-interface, scheduler, action-cluster, and representations manager. The user interface module is responsible for low-level system-user interactions. It gathers user inputs and displays messages.

The scheduler module controls the overall operation of the system. It consists of an agenda structure, a scheduling logic, and a work data base. The agenda structure is used for keeping track of the pending tasks. Modules in the system invoke each other by placing task requests in the agenda. Any task that can occur in the system has a priority level and a generic task description. The priority levels are assigned (at the design time) to reflect the natural order in which the problem elicitation should proceed. The scheduling logic determines how the tasks are selected for execution. The default selection criteria uses only priority levels. However, the scheduler is capable of using any other criteria specified through the customizing code.

The scheduler also carries daemons (there are none at present) which watch over the representation, the agenda, and the work data base. When a daemon fires, it becomes a task in the agenda, and gets selected as per the normal scheme of things.

The work data base within the scheduler is used for various purposes: storing secondary details of tasks (only primary details are stored on the agenda), maintaining the overall system context information, and as a message exchange area by the modules of the system.

![](/api/attachments/AZZJV3NG/fulltext/images/9e53d442f336346ff47968c5600b3d18ad87617d90447a4f140b8023fb4c8248.jpg)  
Fig. 3. The architecture of the JANUS System.

The action-cluster carries all the worker-modules of the system. As a general rule, there is one worker module for each major activity in the system. A partial list of the worker modules are: goal-entry, factor-entry, alternative-entry, judgement-entry, mind-expander, problem-analysis, constraints-entry, and notepad-entry. The scheduling module invokes the appropriate worker module when a task need to be completed. Usually worker modules schedule tasks for other modules when they complete. For example, the last step in the goal entry processing is scheduling tasks for factor-entry, and alternatives entry.

The representation manager is responsible for providing a higher level interface that shields the low level implementation details of the representation from other modules. It maintains the decision problem information, keywords data base, and mind expansion knowledge bases. The keywords data base maintains the keyword taxonomies, syntactical synonyms and semantical synonyms, and links to the textural information contained in the problem structure and knowledge bases. The mind expansion knowledge base maintains a library of reference problems, text templates, stories for the aesop module, and specialized rules for matching and retrieval.

## 4.3.2. System operation

The basic execution cycle of the system is as follows. The scheduler picks up a task from the agenda and invokes the appropriate worker module. The worker modules gets the details of the task from agenda and the work data base. Typically it accesses the representation to retrieve the relevant details of the problem. It may then schedule a task for the user interface to collect some input from the user. As a last step in its processing, it may reschedule itself for processing the user input.

The user interface module is then invoked. It interacts with the user and places the users input in the work data base and relinquishes control back to the scheduler. Now the earlier worker module gets reinvoked for processing of the user input. This time the module may schedule appropriate tasks for other modules before completing.

This basic cycle repeats. During this cycle, the user may force his initiative any time the user interface is waiting for his input. By issuing a command he can request any task of his choice to be executed. The command translates into a high priority task on the agenda and gets scheduled next. When the task all its related tasks are completed, the control returns back to the system automatically.

If the user requests mind expansion functions, the underlying personalities are invoked in sequence. The personalities engage in an appropriate conversation to stimulate the user. They use the overall context information from the scheduler, the problem details that has been gathered till that point in time, and their own internal context to guide their conversation. For example, if the user is working on factors for a personal computer purchasing problem, the mind expander may show him the factors that were associated with an equipment selection decision that was made in the past.

Whenever the user inputs text say for a goal, first the representation is updated. The keywords in the text are automatically extracted and retrieval links are established for promoting flexible retrieval. The system provides several alternative ways to extract a piece of text: using the conceptual primitives like goal, factor etc.; by traversing the problem graph, for example, getting to the factors from the goal; by using the keyword mechanism – either by direct match or by matching through synonyms, antonyms, closeness measures etc. These flexible retrieval mechanisms provides the base for the operation of the mind expansion personalities.

## 4.3.3. Knowledge representation

The basic structures in the knowledge base are: trees for storing problem information and key word taxonomies; lists for pointers from keywords to the various conceptual entities; templates and rules for text generation; and production rules for specifying situation-action pairs. The standard prolog primitives of relations, lists and rules are used for implementing these structures.

Since the overall control structure of the system, i.e. the scheduling operations, are data driven, we have implemented a simple forward-chaining interpreter on top of the backward chaining scheme of the prolog engine.

## 4.3.4. Mind expansion module

The system supports four distinct mind-expansion personalities: Spock, Bozo, Mom, and Aesop. Each personality pursues a characteristic strategy for helping the decision maker.

Spock emulates logical thinking. It uses the keywords associated with the current problem context to retrieve similar problems from its data base to trigger ideas. Its slogan is “If problem A is similar to problem B then the knowledge of goals, factors, and alternatives of the problem A can be useful for solving problem B”.

For example, if the user is working on the problem “Buying a Boat”, Spock may suggest that Cost, Loan Rate, Resale value as relevant factors by extracting them from the problem of “Buying a Car”.

Bozo emulates lateral thinking. It forces the user to develop alternative problem formulations by tracing the goals-means hierarchy, by thinking about incorrect and infeasible formulations and how they may be made feasible. Its uses several slogans: “A goal is a means to a higher level goal”. Any problem A is contained in some other problem B; therefore solving problem B solves problem A”, “A good way to come up with novel alternatives is to think of nonalternatives and think clearly why they do not work and how they can be made to work”, and “Think of at least N alternatives before making a choice”, “Think of the alternatives person X would come up with”.

Thus Bozo will raise questions such as: Well are there alternatives which you would definitely not consider? Why? Under what conditions will they work? Under what conditions will this alternative not work? If Car is to Transportation, What is X (his problem) is to?

Mom emulates a personality that is obsessed with justifications and counter arguments. Its slogans are: “My son has not thought about all possible cases. I have to raise counter examples”, “He is making assumptions”, and “His justifications could be wrong”. So it poses potential alternatives and makes the user think about why they should be rejected or accepted. It also forces the user to justify his factors, alternatives and judgments.

Thus in the context of “Buying a Computer” problem, Mom may use the keywords taxonomy to find out that words such as calculator, Macintosh, VAX are related to computer, and raise questions such as “How about Macintosh?”, “Why do you think service is more important than price?” etc.

Aesop is a story teller. It presents the user with short parables that have general morals for problem-solving. The intent is to help the user overcome his fixations and tunnel visions. For example, it may present the story of “Newton making the egg stand on its ends by placing it on a ring” to warn the user that he may be unduly constraining himself.

The user can invoke these personalities any time during elicitation. The mind expansion module attempts to use the available contextual information to generate appropriate idea stimulating responses. The system remembers the phrases it has used before and avoids repeating them during a given problem.

## 4.4. Sample session

Legend: User inputs are in bold. System messages are in normal type. Annotations are in italics.

## Janus

[User invokes the system]

Welcome to JANUS system

[Initially the system is in the goal mode. The user can switch to a different mode by issuing a valid command.]

The list of valid commands are:

? Invoke the idea stimulation module

/a Invoke Alternative Mode.

/c Invoke Constraint Entry Mode.

/d Invoke Data Entry Mode.

/e Consult User Program.

/f Invoke Factor Mode.

/g Invoke Goal Mode.

/h Invoke help system/

documentation.

/j Invoke Judgement Mode.

/k Invoke Keyword Mode.

/n Invoke Notepad Mode.

/t Invoke Tree Display Mode.

/p Invoke Problem Analysis Mode.

/q Quit Janus System.

/s Save Janus context.

[The valid list at any point in time varies with the context. The permitted mode switches are continuously updated and displayed on the screen] What is your goal?

[The system begins in the goal elicitation mode]

## Buy a computer.

[The system initializes a new problem. It posts several tasks in its agenda such as ask for factors, ask for alternatives etc.]

Enter factors for \`\`Buy a

computer'.

[The system automatically goes into the factor elicitation mode. It displays the goal for which factor needs to be entered.]

## Cost

[The user has entered the first factor]

Current factors for \`\`Buy a computer'' are:

1. Cost

Enter additional factors [The system displays the factors that have been entered so far]

## Availability of programs.

Current factors for \`\`Buy a computer'' are:

1. Cost

2. Availability of programs

Enter additional factors

## ?

[User is invoking idea stimulation. Spock, the logical thinker has been activated now. The system characterizes the context as factor entry and the relevant key words as: buy, computer.]

I have information about the following problems that should be of interest to you:

1. I want to buy a boat.

2. I want to buy a house.

Indicate your choice

## 2

[The user asks the system to show the details of the second problem]

For the problem 'I want to buy a house'

I have the following factors:

1: Cost

2: Location

3: Interest rate

4: Resale Value

Would you like to see more? (Yes/No)

[User notes that resale value may be a relevant factor to his current problem. He indicates to the system to terminate mind expansion and proceed with the factor elicitation]

[Assuming that the user has entered resale value as the factor]

Current factors for \`\`Buy a computer'' are:

1. Cost

2. Availability of programs

3. Resale Value

Enter additional factors

## Reliability of the machine

Current factors for \`\`Buy a computer'' are:

1. Cost

2. Availability of programs

3. Resale Value

4. Reliability of the machine
Enter additional factors

## done

[The user indicates that he has entered all the factors]

Would you be adding more factors to this goal later?

(Yes / No):

[The user cannot think of any more factors at this point in time. So he instructs the user to check back with him later]

## yes

[System posts a pending task in its agenda. It will come back to ask for more factors later]

[Since the factors have been entered, the system starts asking for alternatives]

Enter alternatives for \`\`Buy a computer''

## IBM PC

Current alternatives for \`\`Buy a computer'' are:

1. IBM PC

Enter additional alternatives?

[User is invoking idea stimulation. At this point the context is characterized by alternatives entry, and the keywords buy, computer, IBM. Spock is once again invoked which recognizes several relevant problems]

I have factors and alternatives for
.....

4. I want to compete with IBM

5. I want to get a job with IBM

6. I want to become an IBM OEM Indicate your choice

## 4

[The user requests for more information about the

problem of competing with IBM]

The factors for \`\`I want to compete with IBM' are:

.. Money

.. Market Share

.. Product

The alternatives are:

..Merger with Apple

..Increase R&D Budget

..Hire marketing consultant

Would you like to see more?

## No

[The user has however recognized apple as an alternative for his problem by serendipity!]

Current alternatives for \`\`Buy a computer'' are:

## 1. IBM PC

Enter additional alternatives

## Apple

Current alternatives for \`\`Buy a computer'' are:

1: IBM PC

2: Apple

Enter additional alternatives?

[User is invoking idea stimulation again. Since the context has not changed the system determines that Spock will not be useful. Therefore it brings up Bozo, the lateral thinker]

Are there any alternatives that you would definitely not consider?

[The principle is that alternatives can be generalized by making modifications to a non alternative]

Compaq

Why?

## Because....

I would say that \`\`Buy a computer'' is really not your goal.

Is there a higher goal that you are trying to achieve?

[It is a laddering technique to make the user focus on the real problem rather than on one of the solutions to the problem]

I want to be more productive.

Consider 'I want to be more productive'

Why have you not included this as a factor?

[The principle is that in many instances goals and factors are interchangeable]

[After these digressions the system gets back to the alternatives entry]

Current alternatives for \`\`Buy a computer'' are:

1: IBM PC

2: Apple

3: Leading Edge

Enter additional alternatives?

[User is invoking idea stimulation again. Since the context has not changed much from the previous instance, the system activates a new personality for idea stimulation. In this case it brings up 'Mom']. Why is \`\`IBM'' such a good alternative?

## Because IBM has good service.

[The principle is that by focussing on good and bad things about each alternative new factors can be identified. Hopefully the user will recognize service as an important factor]

Why \`\`MAC'' is not an alternative?
[Mom uses the principle of generating counter examples. MAC is a computer but the user has not stated it as an alternative]

## Never heard of it!!!

[!! The user is just giving a smack to those MAC addicts!!]

What's so great about 'Leading Edge'?

Shutup

I'm only trying to help. No need to be rude.

[The elicitation is continued in a similar fashion to capture the subfactors, weights of the factors, alternatives etc. User can invoke the analysis module anytime by issuing the /p command. The system will provide a recommendation, if possible, using the available details.]

## 5. Discussion

## 5.1. The project goals and outcome

The objectives for this project were: Exploring process support and intellectual support; developing a good understanding of the underlying conceptual and implementation problems; developing strategies for resolving these problems; and developing a research prototype that can be used for on-going research exploration. The project has succeeded well on all these counts.

We have been able to translate much of our process support and intellectual support ideas into working features of the JANUS system. Specifically, we have successfully implemented the following features: active elicitation, capturing contingencies and justifications, the system keeping track of pending tasks, flexible process sequences (ability of the user to switch modes at his will), mixed-mode initiative, and idea stimulation through machine-based personalities. Though the current implementations of these features are rudimentary in nature, they provide a good starting point for further exploration.

We have not a conducted a formal evaluation of the performance and effectiveness of the system. But, our preliminary and informal evaluations are very reassuring. We have verified that the system makes correct decision recommendations as per the analytical hierarchy model. We have received good feedbacks from friendly users who have used the system for simple decision problems. Their experiences indicate that the features of the system are well-founded and effective.

The system has several limitations that are customary of prototype systems. The user interface is basic and crude. The problem can be traced to two sources. First, the use of main-frame environment – notorious for their user interfaces. Second, since developing good user interfaces would have diverted our limited resources for other aspects we were exploring, we did not give it a high priority. We are currently remedying the interface problems by porting the system to run under Arity Prolog on IBM-AT compatibles and take full advantage of the extensive user interface capabilities available in that environment.

The knowledge base and keywords data base of the system are at present very small. This greatly limits the performance of the mind-expansion personalities. Our plan was to evolve/expand the underlying knowledge bases slowly over time. But we are recognizing the need to start with a sizeable initial knowledge and keywords data base in the system. Therefore we have started a mini-project for populating the knowledge base with: representative decision problems; adages and stories related to problem solving; a library of probing questions for stimulating lateral thinking and problem reformulations; and adding a keywords dictionary.

On the whole, the project has been a rich learning experience in terms of understanding the underlying conceptual and implementation problems. We will talk more about these in Section 5.3. Our experiences so far have been very encouraging. We seem to have made the right decisions regarding the architecture and the choice of Prolog as the implementation language. The system has taken shape as an easily-extensible system, and promises to be a good research vehicle for our further exploration.

## 5.2. Relating to prior work

The JANUS work integrates and extends several current approaches to active support. Krcmar [6] and Nierenberg [12] explore the use of questions as mechanisms for stimulating ideas. Krcmar generates questions using a model of the competitive analysis problem. The advantage of this approach is the specificity of the questions. However, the system may bias the user to think within the framework of the model. Further, the system becomes problem-dependent. On the other hand, Nierenberg uses generic questions that are independent of the problem domain. While this can promote divergent thinking, it lacks the specificity enjoyed by Krcmar's approach.

In JANUS we have tried to get the best of both these worlds. We use a generic structuring technique to guide problem-solving. Therefore the system can be effective for a wide range of problems that can benefit from the underlying structuring strategy. The questions we raise originate from this model. Therefore they can be focussed and efficient. At the same time, since the model is generic, the questions can apply to a variety of situations. Further, our mind expansion facilities try to use the problem context information to generate questions and locating analogous situations. Our architecture supports a knowledge base that can be loaded with information specific to the kinds of problems expected to be solved using the system.

Some of the features in JANUS are essentially operationalizations of the conceptual ideas outlined by Manaheim [8]. In JANUS, the user is not constrained to executed his tasks in any predeterminated chronological sequence. As the user performs tasks, the system sort of watches over his activities and schedules related tasks which have to be completed. The system periodically reminds the user of tasks that are pending and need to be completed. These are operationalizations of the system-directed processes ideas of Manaheim. The system also has daemons which can enforce constraints and consistencies. At a later date, we hope to use the daemons to change the system mode dynamically to force the user to think divergently or convergently [14] as appropriate.

A critical requirement of Manaheim's architecture is to have a good understanding of the users decision making processes. Given that decision making is an extremely complex process, we believe that it may be extremely difficult, if not impossible, to meet this requirement. We feel that the most productive approach is to use a good generic structuring technique, and implement it with appropriate process support mechanisms so that user is free to carry his processes in a flexible and more or less unconstrained manner. We have illustrated this approach through the JANUS system.

Though JANUS is similar to GODESS in the sense that both are essentially generic structuring systems, they are considerably different from each other in terms of the support they provide to a decision maker. JANUS goes far beyond GODESS because it not only provides structuring support like GODESS, but also provides process support mechanisms and mindexpansion personalities. The popular approach for enhancing the performance of a generic structuring system is to incorporate domain-specific knowledge. In JANUS we have shown additional approaches for enhancing the support capabilities of a generic structuring system.

At present, our mind expansion personalities are not critiquing agents, or expert personalities in the sense of our discussions in “employing expert systems as active DSS” (Section 2.3.3). But JANUS provides the overall architectural framework for productively exploring these ideas. We are planning several projects to implement mind-expansion personalities along the lines of PARRY [3] and POLITICS [2]. In the Birbal project [22], we are currently exploring a machine-based devil’s advocate personality.

In summary, the JANUS work shows how the various active support approaches can be integrated and extended. The work is significant from many perspectives: exploration of process support mechanisms and mind expansion facilities; exploration of active support in a generic fashion; and the methodological thrust - the use of explorative systems development as a research strategy for developing conceptual and implementation ideas in parallel. The last is especially important for the field of decision support systems to develop deep roots rather than stay at the ideas level.

## 5.3. Future work

During the course of the project, we have acquired valuable insights into the problems that underlie the development of man-machine joint cognition systems. We have developed a long-list of research problems that need to be investigated. These will be the focus of our on-going research. Due to the limitations of time and space, we highlight only some of the key problems here.

The mind-expansion personalities in the current system are based on simple and intuitive models. As a result, their capabilities are quite limited. They can only ‘speak’; they cannot ‘listen’. That is, they are not capable of understanding and utilizing the responses of the user in the on-going dialogs. Further, as their reasoning capabilities are rather superficial (key word matching) they are not capable of making use of all the available information in the problem context. We are already working on other projects [22] to develop personalities that are based on formal models of inquiry and role playing, and employ expert critiquing techniques.

As the decision problem becomes large, the number of pending tasks within the system tend to explode. We are becoming aware that our present mechanisms for task selection and scheduling are inadequate to deal with this problem. We need better approaches and criteria for deciding what part of the problem should receive attention at a given point in time, and when and how the focus should be switched.

At present, we have taken a very simple approach to interruption and resumption. The system is capable of restoring its context, and starting from where it left off. But the system provides no help to the user to regain his mental context when he resumes after interruption. In this regard, we need good mechanisms for summarizing, and explaining what has transcribed over time during a decision making process. We recognize that this is quite a difficult and challenging problem.

The philosophy and pragmatics of man-machine joint cognition dictate that knowledge and expertise will be distributed in the man-machine setup. As a consequence, the system has to acquire the necessary problem-specific and background knowledge from the user. The primary mechanism for the system to fulfil this goal is to pose questions to the user. We are discovering that this can trigger endless series of questions and can be a severe distraction from the central purpose of dialog between the user and the system. To address this problem we need systematic and effective approaches for: pruning down the questions; distributing/inserting the questions during the course of the dialog; motivating the user to cooperate with the system for satisfying the system's needs; and determining what knowledge the system should begin with, and how it should acquire additional knowledge over time.

We are also recognizing the need for the elicitation process to be “interesting”, and ‘natural’ to be effective. These are unique problems of intellectual support systems. Whereas in traditional systems the consistency and predictability of the interface is the key requirement, in intellectual support systems they can be ineffective and even dysfunctional. Imagine an intellectual support system that repeats the same phrases and uses the same examples during its sessions. It can quickly become dull and boring and incapable of stimulating thoughts in the user. For the system to retain its effectiveness, it should exhibit interesting variations, have elements of surprise and unpredictability. These require that the system carry a rich knowledge base of phrases and examples, and be capable of carrying on conversations in a manner that reduces monotony and avoids repetitions.

We are also recognizing that a user may not relate to the system's use of the structuring primitives such as ‘goals’, ‘factors’, ‘judgments’ etc. Therefore we need to make extensive use of analogies to establish common basis for communication. We have done some initial exploration of this idea in the DRONA system [17] and in the software maintenance context in [23]

Thus we have identified and increased our own awareness of a large set of detailed conceptual and implementation problems. These will be the focus of our on-going research. However, in the immediate future our focus will be mostly on exploring the concept of machine-based personalities in more depth.

## 6. Summary and conclusions

We had three major goals for this paper: provide a brief review of the key ideas in the active decision support systems area; present our overall strategy for exploring advanced forms of decision support; and discuss in detail the JANUS system, the research prototype that implements our ideas. We have successfully addressed all these objectives.

We started with an overview of the current approaches and themes for pursuing active support. We followed this with a detailed discussion of our research framework, methodology, and architecture for developing advanced forms of process support and intellectual support. We then presented the details of our JANUS system to show how we are implementing and evolving our ideas. We established the contributions of the JANUS work by relating it to the relevant prior works. We reflected on what we have learnt through our research, and presented a list of key problems that need to be addressed in the future.

We conclude this paper by summarizing the key ideas of our work:

\- Developing and implementing process support and intellectual support approaches.

\- Introducing and demonstrating the promise of the concept of machine-based personalities that are capable of playing variety of distinguished roles.

\- Developing a domain-independent approach to active support.

\- Integrating and extending the available approaches to active support, and

\- emphasizing the use of exploratory systems development (and AI research paradigms) for DSS research.

## References

[1] Barr, A., Feigenbaum, E., “The Handbook of Artificial Intelligence”, Vols I, II, and III, Morgan-Kaufmann Inc., Los Altos, CA., 1981.

[2] Carbonell, J.G. Jr., “POLITICS: An experiment in subjective understanding and integrated reasoning”, in Inside Computer Understanding: Five programs plus miniatures, R.C. Schank & Reisbeck (eds.), Erlbaum, Hillsdale, N.J., 1980.

[3] Colby K., Artificial Paranoia, Pergammon Press. New York, 1975.

[4] Gory, G.A., Scott Morton, M.S. "A Framework for Management Information Systems", Sloan Management Review, Vol. 13, No. 1, pp 55–70, Fall 1971.

[5] Hollangel et al. (eds.), “Intelligent Decision Support for Process Environments”, Springer-Verlag, Heidelberg, 1986.

[6] Krcmar, H., Asthana, A., “Identifying Competitive Information Systems: A symbiotic approach” in the Proceedings of the twentieth Annual Hawaii International Conference on Systems Sciences, 1987, pp 765–773.

[7] Manheim, M.L., Isenberg, D., “A Theoretical Model of Human Problem-Solving and Its Use for Designing Decision-Support Systems”, The Proceedings HICSS-87, IEEE Computer Society, 1987, pp 614–627.

[8] Manaheim, M.L., “An Architecture for Active DSS”, Proceedings of HICSS-21, IEEE Computer Society, 1988, pp 381–386.

[9] Manaheim, M.L., “Issues in Design of a Symbiotic DSS”, Proceedings of HICSS-22, IEEE Computer Society, 1988, pp 14–23.

[10] Miller, P., “ATTENDING: A Critiquing Approach to Expert Computer Advice”, Pitman Publishing Program, Boston, 1984.

[11] Mili, F., “A Framework for a Decision Critic and Advisor” 21st HICSS Conference, January 1988, Vol III, pp 381–386, IEEE Computer Society Press.

[12] Nierenberg, G.I., "The Idea Generator", (A Software Product), Experience in Software Inc., Berkley, CA, 1987.

[13] Pearl et al, “GODESS: A goal directed decision structuring system”, IEEE Transactions on Pattern Analysis and Machine Intelligence, 1982, PAMI-4, 250–262.

[14] Raghavan, S.A., “A Decision Support Systems based on Generic Support Concepts and their Application to Decision-Making Processes”, Unpublished Doctoral Dissertation, Information Systems Department, Georgia State University, June 1984.

[15] Raghavan, S.A., et al., "TOS: A Unix Thoughts Organiz-

ing System", Unpublished MSE Project Course Report, Wang Institute of Graduate Studies, Spring 1986.

[16] Raghavan, S.A., Chand, D.R., “Decision Support Systems and Expert Systems”, in the Proceedings of Fifth Generation Computing Systems Symposium, Madras, February 24–27. 1987.

[17] Raghavan, S.A., et al., “DRONA: A Decision Structuring System”, Unpublished MSE Project Course Report, Wang Institute of Graduate Studies, Spring 1987.

[18] Raghavan, S.A., et al., “JANUS: A Decision Structuring System”, Unpublished MSE Project Course Report, Wang Institute of Graduate Studies, Spring 1987.

[19] Raghavan, S.A., Chand, D.R., “Towards Decision Support Environment: The Thoughts Organizing Project”, in DSS-87 Transactions, June 1987, pp 83–86.

[20] Raghavan, S.A., Chand, D.R., “Intellectual Support in CASE Environments”, Second International Symposium on Computer-Aided Software Engineering. July 1988.

[21] Raghavan, S.A., Chand, D.R., “Exploring Active Decision Support: The JANUS Project”, in the Proceedings of Hawaii International Conference on Systems Sciences, January 1989, pp 33–45.

[22] Raghavan, S.A., “Birbal: A Computer-based Devil’s Advocate”, in the Proceedings of Hawaii International Conference on Systems Sciences, January 1990, pp 391–402.

[23] Raghavan, S.A., Murthy, V., “Developing Support Agents for Software Maintenance: A Practical Approach”, in the Proceedings of Hawaii International Conference on Systems Sciences, January 1990, pp 82–92.

[24] “Approaches to Knowledge-based Critiquing: A Review of Literature”, Technical Report, Bentley College, (under preparation), September 1989.

[25] Rich, E., “Artificial Intelligence”, McGraw-Hill, New York, 1983.

[26] Saaty, T.L., “The Analytic Hierarchy Process”, McGraw-Hill, New York, 1980.

[27] Woods, D.D., “Cognitive Technologies: The design of joint human-machine cognitive systems”, AI Magazine, Vol 6. No. 4, Winter 1986, pp 86–92.

[28] Young, L.F., “Computer Support for Creative Decision-Making: Right Brained DSS”, in “Processes and Tools for Decision Support”, edited by H.G. Sol, North-Holland, 1982, pp 47–64.
