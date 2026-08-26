---
otero_id: 17659
otero_key: "TEMU925B"
title: "An active intelligent decision support system — Architecture and simulation"
authors: "H.Raghav Rao; Ramalingam Sridhar; Sudeep Narain"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90075-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An active intelligent decision support system – Architecture and simulation

H. Raghav Rao, Ramalingam Sridhar and Sudeep Narain

State University of New York at Buffalo, Buffalo, NY 14260, USA

Development and implementation of decision support systems to support intelligent decision making is an area of research that has gained in importance in recent years. Due to the increased complexity of decision making, active involvement of the user and the computer in an intelligent way is necessary in the decision process. This paper presents issues in the design of an active intelligent decision support system (IDSS), develops an architectural model based on cooperative distributed problem solving, and performs a simulation of the system using object oriented programming for an example application in airfleet control.

Keywords: Intelligent decision support; Architecture; Simulation; Cooperative distributed problem solving.

## 1. Introduction

Historically, researchers have developed systems that support decision making in managerial and organizational situations [1]. Such systems, called decision-support systems (DSS), typically consist of software for database, model base, and user interface management. The design of a DSS has predominantly consisted of software development on a general purpose computer system [1,2]. However, as Elam and Mead [3] have pointed out, very few researchers have considered detailed architectural implementation and design issues.

Many of the decision-support systems offer passive forms of decision support, as mere computerized assistants, where the decision making process depends on the user's initiative. An alternate viewpoint, advocated by Manheim and Mili [4,5,6,7,8], suggests active involvement of a DSS in the decision making process. Such active involvement is especially needed in complex decision making environments.

The advent of improved techniques in computer system development and artificial intelligence (AI) makes it feasible to implement active intelligent decision support systems (IDSS). Distributed artificial intelligence techniques, principles of cooperative distributed problem solving (CDPS) $[12,13,14,15,16,17,18,19]$ , and cognitive modeling $[20]$ can play a major role in the implementation of intelligent systems. Distributed problem solving networks are distributed networks of semiautonomous problem solvers that cooperatively interact with each other on a very limited basis in reaching a solution to the problem $[12]$ . CDPS is the process by which loosely coupled problem solvers cooperate to solve subproblems from a given domain of problem solving, and integrate the subsolutions into an effective overall solution $[21]$ . Cognitive modeling has inspired viable approaches for facilitating human-machine interaction, such as the menu-driven user interface $[20]$ .

This research presents an intelligent decision support system that incorporates the concepts of an active DSS. An architectural framework is modeled on the CDPS architecture. The IDSS has a set of knowledge-based processors, with a centralized controller that coordinates the activities of the individual processors in arriving at a consolidated solution. The architecture uses a message board, which is implemented as a shared memory system. The IDSS system is simulated on a Sun platform using X-window interface and object oriented programming(C $^{++}$ ). Menu-driven interfaces are used for facilitating interaction between the user and the IDSS. The IDSS simulation is performed for an example application of command decision making in air-fleet control.

The role of the IDSS developed here is not to replace the human decision maker but to function as a tool for decision making by complementing the user's abilities of problem solving in the application domain. In the process of problem solving, at various intermediate stages, the IDSS presents a user $^{1}$ with different alternatives to choose from, thus determining the problem solving path. By providing a user with the ability to determine the problem solving path, the IDSS has the flexibility of adapting to a user's style of problem solving, an important and essential aspect in the design of decision-support systems [22].

## 2. Background

Early decision support systems were computer systems that utilized decision rules and models coupled with databases to help decision makers solve semistructured and unstructured problems $[1,23,24]$ . Keen defines DSS to be an interactive computer-based aid designed to assist managers in complex tasks requiring human judgment $[25]$ . Moore and Chang $[26]$ suggest that DSS is an extensible system that is oriented toward future planning and has an intrinsic capability to support ad hoc data analysis and reduction, as well as decision modeling activities. These early systems can be classified as passive forms of decision support, where the systems do what the users explicitly direct them to do. For example, they answer what-if kinds of questions, and support a narrow range of decision-making tasks.

A new definition for decision-support systems that provides active support to the decision maker has been proposed by Manheim [4]. An active system operates almost independent of explicit direction from the users to provide support that the user finds helpful. A computer maintains an updated model of the user problem-working process and complements the user's work in a number of forms, such as suggesting alternate actions and indicating issues that the user might 'have overlooked. The system has two independent processes, one user directed and the other computer directed. The user initiates the problem solving process and subsequently the computer may activate some processes, which would operate without explicit direction from the user. The result of the computer directed process can be used by the user in arriving at a solution.

In the recent past, researchers $[27,28,10,29]$ have focused on tandem architectures that synthesize expert systems and decision support systems. An expert system is a decision-making/problem-solving integrated package that contains a knowledge base for a particular problem domain, and a reasoning mechanism for inference $[30,31]$ . A DSS on the other hand helps decision-makers utilize data and models from its database and model-base to solve unstructured or semi-structured problems by allowing the user to approach a problem analysis in a flexible, personal way $[22]$ . While a typical DSS supports quantitative, mathematical, and analytical reasoning, a typical expert system can support qualitative analysis based on methodologies such as symbolic reasoning and pattern recognition. Integrating the two into an intelligent decision support system $[27,28,10,29]$ can thus support various types of problem solving processes and provide active modes of support to the decision maker.

## 3. Architectural model

## 3.1. The underlying process

In this subsection, we describe the basis for modeling problem solving situations within the IDSS. An independent agent can look at a problem from different, often incommensurate frames of reference [33]. This can be equivalently described by a model where different agents solve a problem from their own perspective, and then collaborate together to try and reach a common goal. Thus the decision process is analogous to that of a group of decision makers, who cooperate with each other in generating a composite solution. The IDSS developed in this research reflects such an organization in which decision making is distributed among a set of agents. Each agent has a knowledge base pertaining to a specific area within the problem solving domain and the expertise to solve problems from that area. Coordination and cooperation among the agents is effected by a controller that exercises control over these agents.

![](/api/attachments/TEMU925B/fulltext/images/2fc5c349c646f69dbf92d48a9fc3eccf52165c652c701ba28f9fe89d11643e20.jpg)  
Fig. 1. Block level representation of an IDSS

Further, the IDSS is designed to support decision making actively, an approach that essentially stems from the fundamental suggestions of Mili and Manheim $[4,5,6,7]$ . Symbiosis between the user and the computer in decision making is emphasized by the active IDSS. In this paper, the symbiosis is achieved by the IDSS with the help of an intelligent menu-driven interface between the user and the computer that helps in the initiation of the various processes. The purpose of the menu interface for user interaction is to create a “constrained cognitive architecture” [34,20]. The conceptual model of a system’s functionality is represented in menu selections by the order of menus presented to the user in a top down fashion [20]. This menu selection model of user interaction represents the engagement of a set of cognitive processes. The menus define and limit the flow of control and information through the interface. The approach taken in this paper closely follows the tree model specified by Norman [20]. In the tree model, menu traversal occurs from a central node to leaves according to increasing levels of specificity. Once one such a path is completed for a particular subproblem domain, another similar tree model is used to specify the details of another subproblem domain.

![](/api/attachments/TEMU925B/fulltext/images/be65700a17a7c1571268807450d164fb5e75a2417ffcd81eecfe29c08e52ddb2.jpg)  
Fig. 2. The architecture for the IDSS

The computer-directed processes in the IDSS can either independently operate in helping the user in the solution process, or interact with the user. The system embodies limited forms of knowledge as a set of production rules and draws on the user's knowledge of the problem solving domain. The user can influence the solution path by selecting different alternatives at the user interface and by selecting a desired solution from the alternatives provided by the IDSS. In this process the IDSS helps the user in analyzing the different alternatives (using the past history and the problem solving steps).

The knowledge and problem solving abilities of the IDSS are complemented by the user's expertise in generating an effective solution, and thus the user helps in guiding the problem solving process. Thus, the system is modeled using a distributed problem solving approach.

## 3.1.1. Architectural specifications

Problem solving between the IDSS and the user is an interactive process in which the user applies his judgment and experience to the knowledge and abilities of the IDSS. The organization of a typical DSS $[22,1]$ is used as the basis for the development of the IDSS architecture and is shown in Figure 1. A detailed architecture illustrating the various components of the IDSS is presented in Figure 2.

## Controller

The controller is the heart of the IDSS and has indirect or direct control over all the constituents of the system. In developing a solution to a given problem, the controller uses

(a) The Facilitating Element (FE) to communicate with the user

(b) The model subsystem to select a suitable model for solving the problem

<table><tr><td>IDSS Menu System</td><td>Menu1</td></tr><tr><td colspan="2">Click in window to make selection</td></tr><tr><td colspan="2">Indicate region of operation:</td></tr><tr><td colspan="2">Region1</td></tr><tr><td colspan="2">Region2</td></tr><tr><td colspan="2">Region3</td></tr></table>

<table><tr><td>IDSS Menu System</td><td>Menu2</td></tr><tr><td colspan="2">Click in window to make selection</td></tr><tr><td colspan="2">Friendly forces involvement</td></tr><tr><td colspan="2">YES</td></tr><tr><td colspan="2">NO</td></tr></table>

<table><tr><td colspan="3">Menu7</td></tr><tr><td colspan="3">Click in window to make selection</td></tr><tr><td colspan="3">Indicate available aircraft</td></tr><tr><td>F16</td><td>F15</td><td>B2</td></tr><tr><td>F1</td><td>F9</td><td>S9</td></tr><tr><td colspan="2">Cancel</td><td>Enter</td></tr></table>

Fig. 3. Sample menus

(c) The data subsystem to perform all data related tasks and

(d) A knowledge subsystem to generate a single or a set of alternate solutions.

Communication between the user and the IDSS is accomplished through a facilitating element, implemented as a menu-driven interface. The model subsystem contains a library of models needed for the problem solving and the routines that manage these models. The controller applies the data stored in the data subsystem for a given problem to the models stored in the model subsystem. In the implementation, the controller has two subcomponents, a task allocator and a conflict resolver (CR). The task allocator is used to allocate subproblems to the processors in the knowledge subsystem. The conflict resolver is used in the resolution of conflicts of variables within the knowledge subsystem.

## Facilitating element

The facilitating element (FE) incorporates the communication interface between the user and the IDSS. This interface is implemented as a menu-driven interface in which the IDSS presents its queries to the user in the form of a menu with alternate selections. The FE processes the user's response and may either generate another menu to present further queries to the user or display a result. If a response points out that none of the listed options is acceptable, the user is presented with an edit window. The user can give a new value by simply typing in the response. The FE has the ability to interpret such a response by parsing through the text. This form of a menu-driven user interface [20] has been chosen over a natural-language interface because of its practicality. A history recorder records the various steps taken in the decision process. The facilitating element, with the help of the controller, uses the history recorder in answering various queries of the user.

The menus are not fully preset and the user has freedom in directing the sequence of menu options presented by the system. In time critical situations, a user may prefer to use simple preset menus that have the best performance. However, the user still has the option of creating menus based on his/her experience.

## Data subsystem

The data subsystem stores factual information about the problem solving domain in general and the current problem in particular. It provides data to the computing elements and the user during the problem solving process. This is implemented as part of the controller subsystem.

## Model subsystem

The model subsystem stores typical problem solving techniques for the problem solving domain. It provides analytical and mathematical models to the computing elements. It also stores the necessary information that is used to decompose a given problem into its subproblems, in the form of a set of rules. This is implemented as part of the controller subsystem.

## Knowledge subsystem

The knowledge subsystem of the IDSS contains the knowledge of the problem solving domain. This knowledge is distributed among a loosely coupled network of domain intensive processors that can individually solve an aspect of the problem and collectively cooperate to solve a given problem within the domain of the IDSS. Each of these processors, called a knowledge processor (KP), contains knowledge in a specific domain and functions under the direction of a centralized controller. These knowledge processors implement the knowledge source of the system. The controller is a special kind of knowledge processor containing global knowledge, and is used to formulate subproblems, identify the KPs that can be used to solve these subproblems, distribute the tasks accordingly, coordinate the efforts of the KPs, and construct a composite solution. Following the literature in distributed artificial intelligence, this research focuses on the class of problems, where the main problem can be divided into relatively independent, marginally overlapping subproblems. The marginal dependency of the subproblems is such that it can be handled by a simple conflict resolution scheme.

This system has a distributed set of processors with a limited centralized control. A problem is first divided into subproblems and distributed to appropriate KPs. This is better handled by one central controller, since only one processor needs to keep track of the information about the subdivision. The subproblems are relatively independent, and hence, individual KPs do not often have to interact with each other. However, they may share common resources. Each of the KPs has its own memory space. Part of the memory space of the processor acting as the controller is designated as a message board and all the processors are given access to read this memory.

## Message board

The message board (MB) is used as the means for communication among the KPs. The use of such an approach has been influenced by the blackboard architectures often used in distributed AI systems $[13,35]$ . Both the message board and the blackboard architectures are memory subsystems that can store data structures to be used by various parts of the knowledge subsystem. The blackboard paradigm provides design guidelines for intelligent systems in a serial computing framework $[35]$ . The blackboard data structure stores global data and the control data are stored in a control data structure. Knowledge sources that are linked to the blackboard have a set of rules used in the problem solving process and are allowed to change the blackboard or control data during this process. The knowledge sources act sequentially on these data.

The message board architecture presented is a specialization of the blackboard architecture. The message board is a shared memory resource among the different knowledge processors (including the controller) and it stores various data that are common to different knowledge processors. However, the different knowledge processes can be invoked in parallel and can access the data at the same time. Each processor has a certain memory block private to itself, that can be modified only by that processor $[36]$ . All other KPs are only allowed to read from this memory region. By keeping separate write regions on the MB, it is ensured that the data written by one KP is not corrupted by another KP. Such a mechanism is enforced by the controller.

By properly mapping portions of the message board's memory to the individual KPs, the KPs are given read and write permission to this select area in MB. During the problem solving process, individual KPs can write to this area (allocated to them), though all the KPs can read the data in the MB (since it is a shared memory). KPs also use their local memory for storing any local data. When a solution has been reached, the KPs output their results and the justification of the decision to the MB. Individual solutions can be transmitted to the controller either through the message board or through semaphores. Also, using a tagged data structure, the KPs can be blocked from reading data when it is being changed, thus preventing the use of old data.

Also for integrating the individual solutions, the controller has the capabilities to form an overall solution. The controller can help negotiate a mutually acceptable value for different KPs, since the controller has a more global picture of the individual KPs capabilities and an overall picture of the problem. In a distributed control it is difficult to enforce these various aspects.

The method of information sharing using the centralized message board has been chosen, since the information that needs to be shared among the KPs is minimal. By allowing this information exchange through the message board, the central controller can selectively restrict the information flow if desired. Though the individual KPs solve the subproblems independently (as in a distributed system), a centralized control is needed for an effective implementation of some of the tasks, such as conflict resolution and task allocation. An alternate approach to information sharing is point-to-point communication, where KPs interact with each other directly. This may be necessary if KPs need intense interaction and if subproblems are heavily interdependent. However, this method is also more expensive in terms of resources required, such as the additional communication linkages needed $^{2}$ , which are in the order of $n^{*}(n+1)/2$ vs n. In addition, overhead on the KPs increases since each KP needs to keep the knowledge about the other KPs, without which the information exchange among KPs would not converge into a coherent solution [15].

## 3.2. Problem solving phases

Problem solving in the IDSS can be divided into four phases. Phase I is preprocessing, where the IDSS gathers information about the problem description. In this phase, the facilitating element communicates with the user through a set of menus. Menus to obtain the knowledge processors in the system by using the models stored in the model-base. Models in the context of an IDSS can be of two kinds. The first kind are those that the controller can use to verify if a KP can be used to solve a subproblem. The other kind are those that can be used by the controller to split up a problem into subproblems. These models are installed during the system design stage. In their simplest form, models are sets of if-then rules. Models in the model-base describe the functions that are based on the features of the objects. These models are organized according to the knowledge areas of the KPs. This facilitates an easier mapping of the subproblems from the given problem to the existing knowledge base. The user is informed of the subproblem distribution and allocation to the KPs that have been selected to solve the problem. Users can choose to determine the subproblem distribution without the controller's help, since they have access to the models and can use their problem-solving expertise to identify and distribute the problem into subproblems.

Phase III is the stage in which the KPs work on the subproblems allocated earlier. The controller coordinates the actions of the KPs in constructing the overall solution. The problem-solving is a distributed process and hence the individual solutions of the KPs have to be integrated into a composite solution. Coherence among the individual subsolutions of the KPs is achieved through conflict resolution $[37,38]$ . A list of decision variables (called primary variables) that are common to more than one KP are identified by the task allocator. Each KP involved proposes a value for such variables based on its subgoals. In addition, the KPs estimate the range of possible values for these variables (maximum and minimum values).

A common value for a primary variable acceptable to the KPs involved is generated through conflict resolution between the KPs and the controller. Conflict resolution is an iterative process, accomplished by the conflict resolver (CR), and it involves communication between the KPs and the controller. The CR has to make sure that this process converges in a finite amount of time. For this, it uses the range of values reported by the individual KPs and the data on the availability of resources. If no common solution exists after some finite number of iterations, it forces a least conflict value based on an acceptable value for a majority of the KPs involved, and other parameters are adjusted accordingly. Such a resolution mechanism is known as least commitment conflict resolution [39]. It supports applications where the problem is decomposable, sequence is important, each additional step in the problem solving generates more paths, conflicting perspectives must be considered, and any path that leads to a solution is theoretically acceptable $^{3}$ .

Phase IV of the problem-solving process deals with the controller integrating the individual solutions into a composite solution. The controller has the information about the division of the problem before the subproblems were distributed to the individual KPs, and it uses this information along with the subsolutions presented by the KPs in reaching a solution. KPs can generate multiple solutions to their individual problems which allows the controller to present more than one alternate solution to the user and the user, has the prerogative in selecting one solution over another. The controller uses the history recorder to record the progress of the various solutions in the IDSS and uses this information in composing the final solution and in providing justifications on the usefulness of one approach over another. Users can query the controller about the steps used in reaching each of the decisions. Answers to the user's queries are essentially derived from the collection of results in the history recorder. The interface with the user is handled by the facilitating element. Though there is no restriction conceptually on the size of this recorder, physical memory limitations may require transferring the information least used, periodically to slower disk memory and retrieving when needed.

## 4. An IDSS for air fleet control

In this section, the model discussed earlier is applied to the design of an IDSS for command and control decision making in air fleet control. The model for the IDSS can be applied to diverse fields ranging from inventory control $[33]$ to VLSI design $[40]$ .

The use of automated decision making aids in military environments has been widely researched [41,42,43,44]. The following considerations have often favored the use of such automation:

(a) Under stressful conditions (which are common during warfare), human decision making can be expected to falter resulting in grave losses of life and property. An automated decision aid can prevent such losses [42].

(b) With extensive use of electronic sensory equipment, decision making has become exceedingly complex involving a large amount of analysis and data processing. There is a limit on human information handling capacity, referred to as Simon's bounded rationality principle [45,46]. A computer system is therefore more suitable in these situations as compared to a team of personnel performing the task [42,41,43].

In the Air Force, an air fleet commander (AFC) is primarily responsible for planning and carrying out an air attack on enemy targets.

In drawing up a plan of attack, an AFC needs to

(a) Identify the target(s) to be attacked,

(b) Evaluate available resources (such as aircraft and personnel),

(c) Design the model for attack, and

(d) Allocate resources.

Decisions in the AFC's domain of operation can be classified into command and control decisions [42,44]. Command decisions are the preoperation decisions and control decisions refer to those made during the operation. The IDSS discussed here is intended for command decision making. It can be extended to include control decisions.

A task is performed by processing data and knowledge based on different criteria. Problem domain and information about specific problems determine these criteria. In identifying the targets for attack, criteria such as physical location of the target, risk involvement and importance of the attack on a particular target with respect to the goal of the mission can be considered.

Table 1 is a scenario for a set of KPs required for the IDSS to operate in the problem solving domain of the air fleet controller. The knowledge of the KPs will determine the limitations of the IDSS. This set of KPs has been chosen to assist the AFC in the task of planning an air attack by conducting an analysis and evaluation of the options involved. Additional KPs could be used to augment the capabilities of the IDSS. For instance, a knowledge processor could be added to help the AFC make decisions regarding the diagnosis and maintenance of the aircraft.

Table 1  
An example Knowledge Processor scenario

<table><tr><td>KP</td><td>Area of proficiency</td></tr><tr><td>KP1</td><td>Models of attack for the air fleet</td></tr><tr><td>KP2</td><td>Army support</td></tr><tr><td>KP3</td><td>Navy support</td></tr><tr><td>KP4</td><td>Allied forces support</td></tr><tr><td>KP5</td><td>Weaponry and aircraft data</td></tr><tr><td>KP6</td><td>Overall plan analysis</td></tr><tr><td>KP7</td><td>Geographical data analysis</td></tr><tr><td>KP8</td><td>Weather data analysis</td></tr><tr><td>KP9</td><td>Personnel data</td></tr><tr><td>KP10</td><td>Reconnaissance data analysis</td></tr></table>

## 4.1. IDSS simulation program

This section presents the simulation details for the AFC problem. The simulation employs object oriented programming, production rules and dynamic programming techniques for the selection of the appropriate weapon system. The user formulates the problem description for the IDSS through a menu-driven interface. A database of information on a set of targets is made available and the IDSS has to select the effective weapon system to destroy a particular target.

Goal: To simulate the air fleet control example. The objective is to demonstrate the application of cooperative distributed problem solving principles to IDSS design. To illustrate this, independent processes are created by forking. Solutions to sub-problems are created concurrently.

Scenario: To destroy a set of military targets, such as an enemy airfield. Items of military importance on the airfield such as aircraft, army post, tank and ammunition store house are its elements. These targets are characterized by their location region.

A target may be destroyed by selecting an air-based weapon system (air target) or a ground-based weapon system (ground target). This involves selection of an aircraft for an air target and ground force for a ground target. Also, missile selection is performed for all types of targets. The user inputs the constraints and the resources (types and number of aircraft/ground forces) under which this military operation is to be carried out. The IDSS uses its knowledge base to select the weapon system to destroy each target. The information about the military targets is available in the IDSS database.

Interface: The IDSS uses a menu based interface to communicate with the user. The user is given a set of options in a pop-up menu system in X-windows. The input from the user is used by the IDSS to define the problem. The user identifies region of operation, available aircraft, weapon systems etc. As soon as the information about the region is presented, data about the targets from the database is read while concurrently continuing to interact with the user to obtain more information about the available resources. For the given region in which the operation is to be carried out, all the targets in the database listed under that region are selected. The user's response to a query will trigger the subsequent menus generated. The problem is decomposed into two subproblems, one dealing with the weapon system selection for all targets to be. The data structures describing a target-element and destroyed by air and the other for ground targets. This is possible since the knowledge needed to analyze a target to be destroyed by air is often different from that for destroying a target by employing ground-based weapons.

Database: Targets in the database are organized according to their location (such as region 1 and 2). Each target contains a set of target elements (e.g., airfield is a target and its elements are an aircraft, tank, building, etc.). Each target element has a set of attributes such as its location, its category (which indicates the order of its military importance), and its attacking capabilities. Such information is provided in a file that contains the information about the number of targets, the description of the targets, and the information about their target-elements.

Each target in the database is characterized by the following:

(a) region in which the target following exists (example 1);

(b) description of the target (example: Airfield);

(c) number of target-elements in the target (example: 9);

```c
struct TargetLocation {
    int in_region; // Region 1 or 2
    int region_pos; // Absolute region location
    char location_des; // underground(u) or level(l) or raised(r)
    int size[3]; // length, breadth and height
    int next_target_dist; // distance to the next closest target
    int shadow_ht; // if the nearest target shadows it,
    // the height of that target
    int proximity_count; // number of targets surrounding (MAX=4)
    int hidden; // target hidden ?
    int visibility; // the farthest visible from (air)
    char surrounding_des[20]; // describe the surrounding area - 
    // rocky | ground | water | forest
};

struct Targetsupport {
    char prim_sup_type; // a-aircraft,g-ground,b-both,n-none
    int attack_cap; // 0 - none, 1 - can destroy air targets
    int resp_time; // 0 - immediate, 1 - < min avg escape time
    // 2 > min avg escape time, 3 - none
    int multi_attacks; // multiple attacks ?
    int safe_range; // what is the range for safe approach
};
```

```cpp
struct TargetDescription {
    char target_class[20]; // Runway, tanks, aircraft, storage,
    // camp, building
    int status; // operational or non-operational
    int nature; // destructive or non-destructive
    int class_cat; // target classification category
    // - indicates importance
};
```

Knowledge base: The IDSS uses its knowledge base to select the weapon system for each target element. This knowledge base is distributed and organized as knowledge concerning targets that can be attacked by aircraft and knowledge about targets that can be attacked by ground forces. The IDSS uses its knowledge

(a) to prioritize the target elements based on their importance;

(b) to determine the effectiveness of a weapon system with respect to a target element and compare one with the other.

Model: The IDSS uses a dynamic programming model [47] in selecting one weapon system over another. Given the available choices, the IDSS makes the final selection between the two best rated weapon systems by evaluating their effectiveness for a target element. This is achieved by applying a Bayesian adaptive learning model for decision making, which bases its decision on a dynamic minimum expected cost function.

Table 2  
Mapping IDSS functions to simulation

<table><tr><td>IDSS function</td><td>Simulation program</td></tr><tr><td>Facilitating Element</td><td>X Window based menu driven user interface</td></tr><tr><td>Data Base</td><td>Text file that contains target/region information</td></tr><tr><td>Model Base</td><td>Process computing the Bayesian probabilities and expected values based on decision theory (using Mathematica)</td></tr><tr><td>Controller</td><td>Main process which creates the different child processes by forking</td></tr><tr><td>Knowledge Processors</td><td>Forked child processes</td></tr><tr><td>Processor communications</td><td>Shared memory regions and pipes</td></tr><tr><td>Parallel Processing</td><td>Forking of processes</td></tr><tr><td>Knowledge Base</td><td>If-then rules</td></tr><tr><td>Knowledge Processing</td><td>Rule based inference</td></tr></table>

Output: The aircraft and the missile for an air target; ground force and missile for a ground target; priority of the target elements; and the target description are output to the user.

Table 2 presents a description of the mapping of the different functional blocks of the IDSS architecture to the elements in the simulation program. The main steps are

\- Obtain the problem description (constraints and resources) from the user

\- Select the targets from the database (according to the region of operation)

\- Separate the target elements into two lists of air and ground targets, which can then be processed by two concurrent processes

\- Group elements in the list, for use in the application of a dynamic programming model for selecting weapon systems from available alternatives

\- Prioritize the target elements in each list depending on the characteristics of the target, such as location, description, accessibility, and position with respect to other targets for each target element of every target

\- Create two processes to do the following for each list:

-rate each weapon system (aircraft/ground-forces) with respect to each target element; -if more than one weapon system is found suitable, run a dynamic programming model and make the final selection

\- Output the target description, the priority allocated, and the weapon system selected for each target-element.

```txt
B. Air Weapon Selections
Selection data follows
Group :Members : 4
Target :tank
Priority :2
Selected Aircraft: F16
Aircraft Rating :2
Selected Weapon :S (short range missile)
Target :camp
Priority :4
Selected Aircraft: F16
Aircraft Rating :2
Selected Weapon :L (long range missile)
Target :ammunition
Priority :3
Selected Aircraft: F15
Aircraft Rating :4
Selected Weapon :S (short range missile)
Target :unit
Priority :0
Selected Aircraft: F15
Aircraft Rating :4
Selected Weapon :L (long range missile)
```

## 4.2. Results

The simulation program had two main objectives. The first objective was to depict the working of the functional blocks in the IDSS and the second to prove that significant time savings can result by executing the functional blocks in parallel.

The simulation program was executed for different sets of targets in the database and an execution profile of the program was obtained for these various sets of data. The program was executed by using the forking mechanism to simulate the working of the two knowledge processors concurrently and without forking which depicts a monolithic sequential implementation of the knowledge base. The execution time for the different data sets under the two different operating conditions is summarized in Table 3.

Table 3  
Execution profile of the simulation program

<table><tr><td>Groups (no. of elements)</td><td>Concurrent (seconds)</td><td>Monolithic (seconds)</td><td>Time savings (seconds)</td></tr><tr><td>3</td><td>5.38</td><td>6.35</td><td>0.97</td></tr><tr><td>6</td><td>5.71</td><td>9.28</td><td>3.57</td></tr><tr><td>9</td><td>9.07</td><td>11.73</td><td>2.66</td></tr><tr><td>12</td><td>10.91</td><td>20.96</td><td>10.05</td></tr><tr><td>15</td><td>13.17</td><td>22.40</td><td>9.23</td></tr><tr><td>18</td><td>14.63</td><td>23.34</td><td>8.71</td></tr><tr><td>21</td><td>16.18</td><td>27.90</td><td>11.72</td></tr></table>

The program execution time shown in this table is an average run time. From the above data, it can be observed that significant time is saved by executing the concurrent execution of the processes as compared to the sequential implementation. Also it is evident from these results that the time saved is not linearly proportional to the number of elements in the group.

The simulation implements the distributed processing environment and exhibits the main principles in the design of the architectural framework to implement an IDSS. It can serve as the basis for testing the effectiveness of this design and further explore the IDSS design issues.

## 5. Conclusion

In contrast to the passive form of decision support of traditional DSS, an alternate approach has emerged that stresses active involvement of computer systems in decision making. Such active support can be generated by imparting intelligence to the system by designing it as a knowledge-based system. This paper has developed a detailed architectural framework for implementing an active IDSS. This was in part based on the previous research by the authors and others $[4,7,28,33,48,18,19,21,40]$ . The system incorporates distributed artificial intelligence and principles of cooperative distributed problem solving in the decision making process. As the next step, to demonstrate the viability of the system, a detailed simulation of the system was performed using an object-oriented programming language $(C++)$ and X-window system on a Sun workstation. The communication between the user and the IDSS was effected by means of a menu-driven interface based on cognitive modeling principles.

The scenario was tested for two processors (simulated by forking) in the current simulation. Future research will simulate the multiple processor scenario. Also, various bottlenecks in implementing individual functional blocks on dedicated processors will be investigated. A fully functional system will be developed that considers parallel processing and pipelining techniques. In this process, issues in the selection of processors for the KPs, controller and the conflict resolver and special purpose hardware, such as a register file for implementing message boards, will be explored.

## Acknowledgements

The authors would like to thank the anonymous referees for their detailed comments that have considerably improved the paper. The authors also thank Professor A.B. Whinston for his encouragement.

## References

[1] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems. Academic Press, 1981.

[2] E. Turban, Decision Support and Expert Systems. Macmillan Publishers, 2 ed., 1990.

[3] J. Elam and M. Mead, Can Software Influence Creativity, Information Systems Research, vol. 1, no. 1, March 1990.

[4] M.L. Manheim, An Architecture for Active DSS, 21st Hawaii International Conference on System Sciences, pp. 356–365, 1988.

[5] M.L. Manheim, Issues in Design of A Symbiotic DSS, 22nd Hawaii International Conference on System Sciences, pp. 14–24, 1989.

[6] F. Mili, Dynamic View of Decision Domains for the Design of Active DSS, 22nd Hawaii International Conference on System Sciences, pp. 24–32, 1989.

[7] F. Mili and M.L. Manheim, Introduction to the DSS Minitrack on Active DSS and Symbiotic Systems, 22nd Hawaii International Conference on System Sciences, pp. 24–32, 1989.

[8] M.L. Manheim, M.L. Srivastava, S. Vlahos, N. Hsu and J. Jones, A Symbiotic DSS for Production Planning and Scheduling: Issues and Approaches, 23nd Hawaii International Conference on System Sciences, pp. 383–390, 1990.

[9] T. Kosaka and T. Hirouchi, An Effective Architecture for Decision Support Systems, Information and Management, vol. 5, pp. 7–17, 1982.

[10] J.T.C. Teng, R. Mirani and A. Sinha, A Unified Architecture for Intelligent DSS, 21st Hawaii International Conference on System Sciences, pp. 286–294, 1988.

[11] L. Uhr, Multi-computer Architectures for Artificial Intelligence. John Wiley and Sons Publishers, 1987.

[12] V.R. Lesser and D.D. Corkill, The Distributed Vehicle Monitoring Testbed: A Tool for Investigating Distributed Problem Solving Networks, in Blackboard Systems (R. Engelmore and T. Morgan, eds.), pp. 353–386, New York: Addison-Wesley Publishing Company, 1988.

[13] H.A. Bond and L. Gasser, An Analysis of Problems and Research in DAI, in Readings in Distributed Artificial Intelligence, Morgan Kaufmann Publishers, 1988.

[14] D. McArthur, R. Steeb and S. Cammarata, A Framework for Distributed Problem Solving, Proceedings of the 1982 Conference of the AAAI, pp. 181–184, 1982.

[15] H.E. Durfee, Coordination of Distributed Problem Solvers. Boston: Kluwer Academic Publishers, 1988.

[16] K.S. Decker, E.H. Durfee and V.R. Lesser, Evaluating Research in Cooperative Distributed Problem Solving, in Distributed Artificial Intelligence (L. Gasser and M.N. Huhns, eds.), vol. 2, pp. 487–519, Morgan Kaufmann Publishers, 1989.

[17] V.R. Lesser and D.D. Corkill, The distributed vehicle monitoring testbed, AI Magazine, Fall 1983.

[18] V.R. Lesser and D.D. Corkill, Functionally Accurate, Cooperative Distributed Systems, IEEE Transactions on Systems, Man and Cybernetics, vol. 11, pp. 81–86, January 1981.

[19] V.R. Lesser and L.D. Erman, Distributed Interpretation: A Model and Experiment, IEEE Transactions on Computers, vol. 29, pp. 1144–1163, December 1980.

[20] L.K. Norman, Models of the Mind and Machine: Information Flow and Control between Humans and Computers, in Advances in Computers–Vol 32 (C.M. Yovitis, ed.), Academic Press, 1991.

[21] E.H. Durfee, V.R. Lesser and D.D. Corkill, Trends in Cooperative Problem Solving, IEEE Transactions on Knowledge and Data Engineering, vol. 1, March 1989.

[22] F.N. Ford, Decision Support Systems and Expert Systems: A Comparison, Information and Management, pp. 21–26, 1985.

[23] R.H. Sprague Jr., A Framework for Development of Decision Support Systems, MIS Quarterly, pp. 1–26, December 1980.

[24] R.H. Sprague Jr., Guest Editor's Introduction, DataBase, vol. 12, no. 1 and 2, pp. 1–7, 1980.

[25] P.G.W. Keen, Adaptive Design for DSS, DataBase, vol. 12, no. 1 and 2, pp. 15–25, 1980.

[26] J.H. Moore and C.H. Chang, Design of Decision Support Systems, DataBase, vol. 12, no. 1 and 2, pp. 8–14, 1980.

[27] W.E. Remus and J.E. Kottemann, Toward Intelligent Decision Support Systems: An Artificially Intelligent Statistician, MIS Quarterly, pp. 403–418, 1986.

[28] H.R. Rao, Intelligent management systems: cooperative problem solvers, Proceedings of DSS-86, 1986.

[29] D.D. Woods, Paradigms for Intelligent Decision Support, in Intelligent Decision Support in Process Environments (E. Hollnagel, G. Mancini, and D.D. Woods, eds.), Springer Verlag Publishers, 1986.

[30] H.R. Rao and B.P. Lingaraj, Expert Systems in Produc-

tion/Operations Management: Classifications and Prospects, Interfaces, December 1988.

[31] E. Turban and D. King, Building Expert Systems for Decision Support, Proceedings of DSS-86, pp. 96–115, 1986.

[32] E. Turban and P.R. Watkins, Integrating Expert Systems and Decision Support Systems, MIS Quarterly, pp. 121–136, June 1986.

[33] H.R. Rao, R.P. Cerveny, G.L. Sanders, R. Sridhar and E.J. Garrity, Intelligent Control and Resolution of a Network of Learning and Problem Solving Processors, 23rd Hawaii International Conference on System Sciences, 1990.

[34] R.M. Young, T.R.G. Green and T. Simon, Programmable user models for predictive evaluation of interface designs, in Human Factors in Computing Systems CHI '89 Conference Proceedings, (New York), pp. 15–19, Association of Computing Machinery, 1989.

[35] R. Engelmore, A.J. Morgan and H.P. Nii, Introduction in Blackboard Systems (R. Engelmore and T. Morgan, eds.), New York: Addison-Wesley Publishing Company, 1988.

[36] S. Narain, Design and Simulation of an Architectural Framework for an Intelligent Decision Support System, Master's thesis, Department of Electrical and Computer Engineering, The State University of New York at Buffalo, 1991.

[37] M.H. Bazerman and M.A. Neale, Heuristics in Negotiation, in Negotiating in Organizations, Sage Publishers, 1983.

[38] R. Davis and R.G. Smith, Negotiation as a Metaphor for Distributed Problem Solving, Artificial Intelligence, vol. 20, no. 1, pp. 63–109, 1983.

[39] P.A. Evans, Using Characterization of Manufacturing Applications to suggest AI Techniques, in Integrated and

Intelligent Manufacturing (C.R. Liu and J.C. Chang, eds.), pp. 27–44, ASME, 1986.

[40] R. Sridhar, An Intelligent Decision Support System for VLSI Design, Proceedings of the Northcon 90, Feature Session on Combined Analog and Digital Integrated Circuits, 1990.

[41] K. Funk, A Knowledge-Based System for Tactical Situation Assessment, Tech. Rep. 41, Navy Personnel Research and Development Center, SanDiego, CA 92152, 1986.

[42] J.G. Wohl, Force Management Decision Requirements for Air Force Tactical Command and Control, IEEE Transactions on Systems, Man and Cybernetics, vol. 11, pp. 618–639, September 1981.

[43] M. Ben-Bassat and A. Freedy, Knowledge Requirements and Management in Expert Decision Support Systems for (Military) Situation Assessment, IEEE Transactions on Systems, Man and Cybernetics, vol. 12, pp. 479–490, July/August 1982.

[44] M.D. Callero, D.A. Waterman and J.R. Kipps, TATR: A Prototype Expert System for Tactical Air Targeting, in Expert Systems – Techniques, Tools and Applications (P. Klahr and D.A. Waterman, eds.), ch. 6, pp. 186–223, Addison-Wesley Publishers, 1986.

[45] H.A. Simon, Sciences of the Artificial. MIT Press, 1981.

[46] M.S. Fox, An Organizational View of Distributed Systems, IEEE Transactions on Systems, Man and Cybernetics, vol. 11, pp. 70–80, 1981.

[47] S.E. Dreyfus and A.M. Law, The Art and Theory of Dynamic Programming. Academic Press, 1977.

[48] R. Sridhar, H.R. Rao and S. Narain, An Architectural Framework for an Intelligent Decision Support System, International Journal of Mini and Microcomputers, vol. 12, no. 2, 1990.
