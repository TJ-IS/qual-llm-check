---
otero_id: 26000
otero_key: "6AH82NXW"
title: "Causal modelling as a tool for problem framing within a group decision support system: an object‐oriented approach"
authors: "T. J. Heintz; W. Acar"
year: "1994"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1994.tb00057.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Causal modelling as a tool for problem framing within a group decision support system: an object-oriented approach

T. J. Heintz & W. Acar\*

College of Business Administration, Marquette University, Milwaukee, WI 53233, USA, and Graduate School of Management, Kent State University, Kent, OH 44242, USA

Abstract. This paper contributes toward the design of intelligent group decision support systems (GDSS). It suggests a GDSS architecture that would enable a group of managers to discuss, learn from each other and possibly develop consensus about decisions or their causes. It shows how an object-oriented approach can be used in producing interactive software to support managerial debate about problem solving. The method uses comprehensive situation mapping causal mapping to represent each manager's perceptions of the relationships between key variables of a firm's strategic situation. The paper presents a prototype implementation and, based on experiences from it, discusses issues concerning future development and use.

Keywords: causal mapping, group decision support systems, object-oriented design, problem framing, strategic situation analysis.

## 1 INTRODUCTION

Managers typically identify and resolve problems within work or peer groups or within political communities. The evolving concept of a group decision support system (GDSS) addresses the former by suggesting that technology can facilitate these managerial problem-framing and problem-solving processes within work groups (Eden & Radford, 1990). This prospect raises some intriguing questions on the use of computer technology in supporting the complex, ill-structured decision-making processes associated with high-level managerial deliberations.

These deliberations usually involve examining the perspectives of multiple individuals who are active participants in the process or who are, as stakeholders in the decisions made, affected by the results of it. Issues raised within this process are often vague, consisting of many qualitative and interrelated factors. The perspective of individual decision makers may vary considerably in this type of environment.

This paper will advocate that groups develop an understanding of a problem situation and decide on how to attack a problem by recognition of causes as opposed to discussion of their end effects. It will suggest that we can use a combination of a causal mapping method and a computing approach called object-oriented programming (OOP) to analyse and better understand complex decision-making situations. Our basic premise is that by examining individual members' perceptions of underlying causes and effects, groups can form an understanding through agreement on the assumptions associated with a problem situation.

Lind and Zmud (1991) empirically show that information frequency speeds up convergence of ideas or interests because convergence affects innovativeness positively. This study also cited communications channel richness as a predictor of convergence. This paper will propose a computer-based support system that is designed to provide for a richer communications mode among GDSS participants. It uses a causal mapping technique to provide a graphical basis for communicating and arguing logically on perspectives on problem situations.

Eventually, a GDSS will provide a modicum of intelligent facilitation of the group decision process and step toward the incorporation of increasingly more ‘intelligent’ capabilities (Heintz & Acar, 1992). Causal factors and their interactions as they pertain to a specific situation are one way to represent the complex knowledge people bring to a business meeting or problem-solving group. Also, concepts inherent in OOP are widely used within the field of artificial intelligence (AI) to represent knowledge and infer conclusions from it. Our premise is that through combining the representation power of OOP ‘objects’ with the explanatory power of causal maps we may eventually produce more ‘intelligent’ GDSS implementations.

In this paper, we first review the work within the GDSS and related fields and examine the literature pertaining to the causal mapping method. A brief description of the OOP approach follows. We provide a specific causal mapping illustration and briefly report on experiences with developing a prototype that implements a simplified version of the mapping method. We then develop an object-oriented architecture for a more comprehensive tool for forming group consensus through the examination of differences in the underlying assumption among group participants.

## 2 GROUP DECISION SUPPORT SYSTEMS

The term group decisions support systems (GDSS) represents a specialized area within the evolving field of computerized 'groupware' systems. Groupware includes efforts to: (1) manage electronic mail exchanges (Lai et al., 1988), (2) use hypermedia concepts for supporting and arguing against positions taken by group members (Conklin & Begeman, 1988; Carlson & Ram, 1990) and (3) structure electronic conversations in a manner helpful for organizing group work (Winograd, 1987–88).

GDSS research (Huber, 1984; DeSanctis & Gallupe, 1987; Dennis et al., 1988; Kraemer & King, 1988; Pinsonneault & Kraemer) has evolved from early work focusing on ways the computer can mediate group processes (Joyner & Tunstall, 1970). Since then a number of group decision support software systems have been developed (Bui & Jarke, 1986; Gray, 1987; Nunamaker et al., Stefik et al., 1987; Watson et al., 1988).

Used primarily as research tools, most of these systems facilitate the collection of ideas and forming of consensus among individuals within face-to-face meeting situations. These systems provide support for agenda formulation, brainstorming on problems and solutions and consensus formulation via a voting mechanism.

DeSanctis and Gallupe (1987) develop a three-level categorization for group decision support systems. Their level 1 systems are those which enable the entry, sharing and group evaluation of ideas. Their level 2 systems provide specific tools to support decision making; and, further, their level 3 system facilitates the decision-making process by acting as an 'intelligent' mediator.

Empirical research focuses primarily on level 1 systems and has reported limited and sometimes conflicting results. Joyner and Tunstall (1970) reports that the computer itself has no significant effect on the quality of the group decision, although subjects already trained on the decision process suggested by the software being used perform better than those without instruction. Other laboratory experiments (Watson et al., 1988) supported this premise by demonstrating that groups assisted by the computer do no better than those given manual guidance on the decision-making process.

However, other studies provide evidence indicating improvement in the quality of decisions by groups that have computer support. This is especially so in cases involving more complex tasks (Gallupe et al., 1988) or larger groups composed of business professionals (Nunamaker et al., 1988). The same results hold for pre-existing groups in a field setting (Jarvenpaa et al., 1988) or when subjects use the technology over time (Zigurs, 1989; Lind & Zmud, 1991).

There are also systems that try to incorporate level 2 and level 3 concepts. Some systems designed specifically to support the negotiation process (Jarke, 1986) use models, and there exists an electronic mail system (Malone et al., 1987) that uses an 'intelligent' filtering mechanism. Also, both the SAMM and GroupSystems environments (Easton et al., 1989) provide a stakeholder analysis tool (Emery & Trist, 1973; Eden, 1978; Ackoff, 1981; Acar, 1987). This latter effort reflects an attempt to use the computer to perform a type of situation modelling as is advocated by this paper.

In general, the results of the efforts undertaken in the area of GDSS are relatively modest and often produce confusing results. Lacking is an understanding of specifically how the computer can augment group processes. It is not surprising that groups using a system which simply displays ideas and tabulates votes perceive the computer as providing limit benefit. We must continue to undertake efforts to build the level 2 and level 3 systems. To accomplish this, we must design systems around modelling techniques that facilitate understanding of the underlying assumptions that people bring to complex decision-making situations. Our approach also provides a graphical user interface (GUI). Conceptually, we view the use of graphics as not an end in itself but as a means of facilitating the visualization and communication of ideas and relationships. Recent research supports this conclusion (Eden & Radford, 1990; Keyer, 1991; Heintz & Acar, 1992).

## 3 APPROACHES TO MANAGERIAL PROBLEM SOLVING

This paper discusses computerizing a problem-solving approach that traces its philosophical roots primarily to the work of Churchman (1971, 1979) on the systemic perspective in the design of enquiring systems, its theoretical roots to Ackoff and Emery's (1972) work on adaptive and interactive social systems, its processual (process implementation) roots to Mason (1969) and Mason and Mitroff (1981) and its methodological roots to Axelrod (1978) and Jones & Eden's (1981) formulation of influence diagramming(ID)-based methods for problem framing and problem solving.

We argue that participants bring to a meeting or problem-solving situation differing mental models of the problem situation (Kelly, 1955; Bannister & Fransella, 1971). These cognitive models represent personal constructs (which we symbolically represent as variables or factors) and linkages between them.

Influence diagramming (ID) (Maruyama, 1963; Eden, 1978, 1989; Weick, 1979; Diffenbach, 1982) is a diagrammatic form of cognitive modelling. ID uses a representation in which variables or 'nodes' are connected by a single type of linkage: a unidirectional link represented by an arrow connecting two nodes. This diagramming procedure attempts to have the user examine how critical decision variables influence each other. It is a straightforward approach whose strength lies in its simplicity. The intensities of the influence relationships are ignored in ID — only their signs (+ or −) and directions are represented. There has been no explicit attempt within ID to analyse methodologically the differing perspectives of multiple decision makers.

ID produces good means of visualizing a problem situation, but it provides limited power in helping individuals understand the underlying assumptions that people bring to a situation. This is because it is based on loose associations between factors. There is no way to evaluate carefully the impact that a change in a specific variable would have on the goals of a decision maker.

Acar's (1983) comprehensive situation mapping (CSM) extends the ID concept in the representation of both the network's links and its nodes. Causal links are assigned an intensity as well as a direction. There are also different types of causal link that model the traditional distinction between ‘necessary’ and ‘sufficient’ causality (Mill, 1862; Ackoff, 1962).

As in ID, factors or variables are represented by nodes, but CSM explicitly identifies those actors or forces that act upon or influence a system; it thus distinguishes between controllable factors (levers) and uncontrollable factors (triggers). CSM nodes are either instrumental or goal variables. Instrumental variables may be controlled by the environment (the triggers of change) or by an actor (these nodes are the levers), or they may be any intermediate or 'mid-nodes' of the causal graph (endogenous variables).

Figure 1 provides a simplified illustration of CSM applied to a decision on how much acreage a farmer should cultivate. Here the lever 'acreage to be farmed' initiates a propagation of change process influenced by trigger 'weather permitting', which affects potential harvest, actual harvest, purchases of supplies/equipment and, in turn, other downstream variables such as net revenue and cash on hand. The double arrows represent links that are sufficient (called full channels) to propagate a change through the link. The single arrows represent conditions necessary (half-channels) but not sufficient for the propagation of change. For example, in Figure 1 both acreage to be farmed and purchases are prerequisite to determining an effect on potential harvest. A third type of link, called a restriction, is represented by a dotted arrow. A restriction within a causal network precludes the propagation of change to its downstream variable.

![](/api/attachments/6AH82NXW/fulltext/images/f2ee540416ab51159fde12c67e1799a96e477a03e09b16d1fa5b119ee79c0904.jpg)  
Figure 1. Illustrative causal map for a farmer deciding on acreage to farm.

CSM has the decision maker specify intensities and time lags for the causal links he or she perceives. This quantitative information gives CSM additional power beyond ID, and it enables the forward analysis of the causal map. Forward analysis is accomplished by using a simulation-like computational capability to determine the effect of changing selected levers and triggers within the causal network. For the case illustrated within the figure, this helps a user formulate a statement of the form: 'If number of calls increases by x per cent, then we would expect earnings to increase by y per cent.' CSM thus aids the decision maker in computing alternative decision scenarios.

The argumentation literature (Toulmin, 1958; Mitroff et al., 1982) deals with the way decision makers attempt to convince each other of the cause and effect structure underlying their belief in the reality or inevitability of something. For individuals with varying points of view to reach a common understanding, they must understand each other's mental model through the recognition of differences in either the variables or the linkages. Examination of these differences enables decision makers to understand the underlying assumptions associated with a co-participant's position. The use of the causal map in this regard moves the participants away from a mode of averaging out feelings and preconceptions and into a mode of representing the existence or influences of causal links. It provides a richer problem representation structure based upon their understanding of causality.

In his work toward a pragmatic and dialectical view of the philosophy of research, Churchman (1971) has laid the foundations of a grand ‘dialectical enquiry’ or dialogue between various disciplinary approaches to knowledge. The problem-framing literature also uses this term to simply denote a scaled-down version aimed at capturing or reconciling cognitive differences in group decision making. This results in a dialectic process for cognitive exploration and negotiation among the multiple participants. Both influence diagramming (ID) and CSM support this process through the use of alternative ID or CSM maps as a tool for resolving individual differences. As described in the applied dialectical inquiry literature (Mason, 1969; Mitroff & Emshoff, 1979; Ackoff, 1981; Acar, 1983), decision makers should approach consensus through explanation and negotiation rather than voting and power play. Such a process prods hidden assumptions to surface and thus allows meaningful discussion to begin.

Mitroff and Emshoff (1979) call this crucial phase of decision making assumptional analysis, and Acar (1983) calls it the backward analysis. Interestingly, both ID and CSM lend themselves to the backward analysis of a complex business situation because it is primarily qualitative. However, as mentioned earlier, only CSM leads itself to the simulation-like forward analysis because of its computational features.

Although Acar's approach is more comprehensive and potentially more powerful than other suggested approaches, implementation problems still exist. Eliciting causal maps can be difficult because of the large number of factors and relationships that may exist, and the difficulty that some individuals may have in articulating their feelings on the underlying cause-and-effect relationships. This process is complicated further when we look at comparing, modifying or combining causal maps.

A computerized system could potentially facilitate this process by storing and graphically presenting these maps and by providing an interface that makes it easy for decision makers to identify assumptions on key variables and their interrelationships. The two basic premises here are that: (i) interconnections exist and are becoming increasingly important within today's increasingly complex business environment (Emery & Trist, 1973) and (ii) information technology can assist decision makers to understand the linkages (Charalambides & Heintz, 1988).

A computerized system could also become the repository for commonly agreed-upon knowledge concerning key factors and relationships between them. It then provides the context in which participants present arguments and support or validate them. This amounts to initiating a type of ‘systemic intelligence’ entailing the emergence of a knowledge base composed of causal links. These causal links become a means to infer conclusions and to assist in proving or disproving premises.

The compilations of problem-framing and -solving techniques by Rosenhead (1989) and Eden and Radford (1990) offers a survey of approaches to GDSS based on problem framing. One of the most extensive systems today has evolved from the work of Eden and his colleagues (Eden 1978, 1989; Eden et al., 1992; Jones & Eden, 1981). This system has many variations and comes under a variety of acronyms (e.g. SODA, COPE, etc.). In general, while some effort focuses on scenario generation, most of its published output (such as 'cognitive maps', 'concept maps', 'implication maps', etc.) relies primarily on the basic notion of cognitive psychology and the simpler forms of causal mapping. Both the output generated in specific instances of decision making and the publications describing them appear voluminous. This paper concentrates instead on developing a more unified, yet richer system, and one that is easier for decision makers to understand.

## 4 OBJECT-ORIENTED PROGRAMMING

Implementation of CSM within a GDSS necessitates a systems development approach that facilitates the generation of highly complex software. The use of interactive graphics and a need to coordinate the activities or maps of many individuals requires the use of software protocols that provide for easy communications between modules, access to graphical code libraries and a rich information representation scheme. Others, including the intelligent E-mail efforts (Lai, et al., 1988) and hypertext-based systems (Conklin, 1987), rely heavily on object-oriented programming (OOP) concepts within their implementation. This section thus briefly reviews some OOP basics to show that it provides such capabilities.

OOP (Cox, 1987) views programming as a process in which the programmer creates special data structures called objects. These 'objects' form a conceptual representation of the physical process that the programmer tries to encode on the computer. Each object consists of attributes that have values indicating the state of the object.

Objects also contain procedures called methods. These methods act as operators that can transform the state of the object or related objects through a message-sending protocol. Programmers generate OOP code by defining methods for an object. The code within these methods usually involves sending messages to other objects. An OOP environment will often include a number of predefined objects for handling such tasks as data representation, the user interface and input-output operations.

Defining attributes and methods involves creating a special object called a class. Program code generation is a process of assigning methods to object class definitions. In the process of program execution, the OOP environment generates instances of these class objects. These instances contain all the attributes and methods of their class, but vary in the specific values assigned to attributes. OOP also allows the definition of class/subclass hierarchies. A subclass can inherit both methods and attributes from its superclass, but can extend them with its own behaviour; in effect, subclasses are specializations of their superclasses.

For example, in the causal mapping system described in the next section of this paper, we create a class definition for a 'participant' object. One of its attributes contains an array of 'maps'. Each map identifies a labelled problem domain containing a set of variables (called factors) and causal links between them. Separate instantiations of the class 'participant' will exist for each decision maker and, within each instance, the 'maps' array may differ.

All these separate 'participant' objects, however, will respond to methods defined as part of the participant class specification. For instance, one method, let us call it 'selectMapFor: aLabel', returns the instance of a map object containing information on the factors and links that compose the map. This map object in turn has a method called 'draw' that produces a graphical display of itself. If, within the OOP language, we assign a variable named John, an instance of 'participant' class, the message 'John selectMapFor: "Profit" draw' will retrieve and display the causal map for the participant John. If Mary represents another participant, then the similar message, 'Mary selectMapFor: "Profit" draw', displays Mary's unique view on the factors defined in her map named Profit. This produces a very powerful way of creating and accessing code to handle complex situations.

The causal mapping application also utilizes the specialization/generalization capability provided by OOP's class/subclass definition capability. For instance, information associated with the object 'node' differs depending on whether it represents a controllable factor (lever), an uncontrollable factor (trigger) or a goal variable. For instance, a goal node may have both actual and realized values associated with it and a trigger typically has an identifiable external influence (an actor) associated with it. These goal, lever and trigger objects represent subclasses of node. They respond to the same methods as node but, in addition, we define specialized procedures, such as one for assigning an actor to a Trigger, for the subclasses.

OOP systems are typically implemented within sophisticated graphically oriented computing environments. Within such environments object classes are usually available that manage a very rich, interactive windowing system with mouse-driving terminal input and output.

Figure 2 illustrates the interface generated with the Smalltalk OOP language for a prototype causal mapping system. This interface enables the specification and graphical presentation of certain types of variables and causal links. Here a participant window provides menus for selecting analysis options and displays instructions and information for the user. A second window exists for producing the causal map. This interactive environment enables us to represent and modify relationships in a highly visual fashion and thus facilitate digging deeper into understanding the underlying assumptions. This should enable decision-making groups to better perceive the positions of others and easily adapt their views to reflect new information.

![](/api/attachments/6AH82NXW/fulltext/images/b0d1e0d0800015c0aa27fc48620b91714bc342ad60b5bcab47002fcc6c7318e1.jpg)  
Figure 2. Illustrative user interface for a prototype causal mapping system.

The graphical interface suggested by Figure 2 demonstrates how an OOP environment provides a natural means of presenting causal maps. Application-defined objects representing such entities as participants, nodes or links coexist with system-provided objects such as windows, menus and various graphical entities. To carry the prototype demonstrated within this figure further, we simply implement refinements for appending more detailed information to the variables (or nodes), defining CSM types (subclasses) or links, and creating varying window displays. The OOP environment will handle many of the implementation details once we determine the overall approach to implementing the object-based system.

The key to implementing an object-oriented mapping system is understanding that causal maps can represent situation-related variables and their interactions. The initially complex task of defining the problem and properly framing it within its domain can be a stumbling block (Mason, 1969; Eden, 1978; Edge & Radford, 1990). In the next section, we use the object-based approach for implementing CSM as a technique to recognize and resolve differing perspectives among individuals.

## 5 AN OBJECT-BASED CAUSAL MAPPING SYSTEM

## The prototype causal mapping system is composed of five major segments as follows:

1 Factor identifier. This segment assists in scoping out the problem domain by identifying the critical variables, or what we call 'factors', associated with a situation or discussion issue. Factor definitions will usually evolve from a process of brainstorming and evaluation that is found in current GDSS implementations and is thus not discussed in detail here.

2 Situation mapper. This segment assists each individual decision maker in examining a problem situation by specifying the cause-and-effect relationships among critical factors. This includes capabilities of classifying these variables as goals (final and intermediate) or as controllable or uncontrollable system inputs. The end result of this effort is a completed causal map.

3 Assumption surfacer. This segment examines differences between causal maps with the purpose of enabling individuals to discuss and understand their differences. This form of 'backward analysis' represents an operational rendering of the assumptional analysis of Mason (1969) and Mason and Mitroff (1981).

4 Scenario Simulator. This segment takes a causal map, associates values with various inputs and projects the values for the goals and subgoals at some future times. Its projection capability enables each participant to test the implications of assumptions implicit in his or her causal map. This process facilitates the 'forward analysis' phase of the CSM method.

5 Consensus formulator. This segment enables the formulation of new maps that represent a consensus of given number individuals or groups. Consensus is formed by having individuals submit linkages to a 'public' or shared map and then allowing them to edit this shared map. Although not always necessary, we envisage group consensus as potentially emerging from a process of generating a series of shared maps.

Figure 3 illustrates how the various segments interact. Individuals initially form their own causal maps through separate analyses of the problem situation. As part of the process of generating a map, new variable or factors may surface. Thus we allow for the possibility go back to factor identification. Similarly, the scenario simulation and the assumption surfacing modules may motivate individuals to go back and modify their maps before consensus formulation ever takes place. Thus, unlike current group decision support systems, consensus is not formed through uninformed voting. Rather, a dialectic process evolves in which participants discuss each other's maps, running scenarios to test their implications and amending them until differences are either negotiated or accepted (Acar, 1983).

Factor identification consists of declaring a short 'tag' name and a descriptive narrative for key concepts or variable. As new factors surface through this decision-making process, the decision maker can define his or her private factors, or alternatively request that they be registered as 'public' terms. This defining of agreed-upon factors is the first step in addressing the complex task of developing the boundaries of the problem domain. In this phase and as well as subsequent ones, it is the negotiation dialectic that assists in performing this unstructured task. This provides a more viable approach to interactive, group-based modelling than fully structured techniques such as the analytical hierarchy process (Saaty, 1980).

The remaining subsections discuss the other four segments more carefully.

Figure 3. Major conceptual components or segments of a causal mapping system.  
![](/api/attachments/6AH82NXW/fulltext/images/cde0e1c08ef5fa2c81739c48a54bff6c470ccc8c80fad77375b26f5fcdceb0f0.jpg)

## 5.1 Situation mapping

The situation mapping supports the formulation of the causal maps through the application of an interactive graphical user interface (GUI). Our prototype development primarily deals with this segment.

The map-drawing process begins by having a participant use a pointing device, such as a mouse, to place a marker at the location where he or she wishes to draw a node. A pulldown menu allows the selection of a factor that the node represents. The user than creates links to and from a selected node through the use of the pointing device and other menu options.

Figure 4 illustrates the object classes used in generating causal maps. This and the subsequent diagrams use a notation commonly used in the database literature in which linkages indicate that one class of object contains or refers to one or many other types of objects.

The windows illustrated within Figure 2 show the user interface for the situation mapping phase. Each participant has a main window that handles message passing with other participants and the selection of major software options. For illustrative purposes, multiple menus are shown, although typically only one would appear at any point in time. To perform the mapping we select the situation analysis (CSM) option from the menu that causes the creation an instance of the SituationMapper. The SituationMapper in turn opens a window allowing the user to draw alternative maps. Each user labels one or more maps, which could be map subsets or completely separate maps. If so desired, the user can open and reposition additional map windows. The system thus does not require all users to examine the same maps. This allows users to argue alternative perspectives while having the level of detail and the logical information deemed most appropriate available on the display screen.

As illustrated in Figure 3, each instance of a 'map' contains a series of 'link' objects that make up the map. Each link has two attributes, indicating the variables that are the 'cause' and 'effect' associated within the link. The power of using OOP is easily illustrated by this representation. Where two or more links have a common cause or effect, they share the same (rather than a copy) node object, thus maintaining the referential integrity of these nodes and their associated factors. The modularity provided by OOP approaches makes it straightforward to add, delete and change these nodes and links. Furthermore, we associate the procedures or methods that draw a note or link on the map with the individual 'node' or 'link' objects. The 'map' object has its own procedure for drawing the entire map, which sends messages that invoke the node and link draw methods when needed. This greatly facilitates the development of the interactive user interface.

![](/api/attachments/6AH82NXW/fulltext/images/2dad2cf22af2ba4392d50eae3b4f017fca37a57a0089467d6365e82cfa19da6f.jpg)  
Figure 4. Object classes with attributes that establish links between objects that are used by the situation mapping segment.

## 5.2 Assumption surfacing

The AssumptionAnalyser object allows pairwise comparison of several causal maps, resulting in a specification of the differences between them. As shown in Figure 5, the AssumptionAnalyser contains two attributes providing links between the views of two separate participants and/or group maps (see section 5.4 for discussion of groups). These two attributes establish 'point' and 'counterpoint' positions as represented by each participant's or group's causal map for the purpose of dialectical queries and comparisons.

This approach to presenting alternative views allows us to depart from the conventional view of obtaining consensus at all costs. Problem-framing approaches do not strictly require it (Churchman, 1971; Cosier & Swenck, 1981; Mason & Mitroff, 1981). By having decision makers focus on differences between their maps, this assumptional or 'backward analysis' attempts to resolve issues through understanding of alternative perspectives. From these differences we build a list of the assumptions that the interacting system users bring into a problem situation. It is through negotiation or resolution of these assumptions that new perspectives develop or consensus may emerge. Alternatively, through a shared understanding of varying assumptions, we may obtain tolerance for differing positions (Mason & Mitroff, 1981; Acar, 1983).

![](/api/attachments/6AH82NXW/fulltext/images/f7d34577361477294e52e67a5e449bf73f8baf11e7209eeb917901c82bbeabf2.jpg)  
Figure 5. Object classes with attributes that establish links between objects that are used by the assumption surfacing segment.

Table 1 presents a list of the type of assumptions that the AssumptionSurfacer currently examines. CSM classifies them from major, those involving the existence and type of factor or linkages, to minor, those associated with magnitude of quantitative values assigned to variables and links. The AssumptionSurfacer contains a list of generic assumption objects and systematically checks for existence of each type of assumption by comparing the point and counterpoint maps.

Assumption surfacing uses a ‘mixed initiative’ approach. The prioritization scheme suggested above provides a means for the CSM implementation itself to suggest a focus for comparison by starting initially with the major assumptions. On the other hand, the users could select specific types of assumptions or specify an individual map node or set of map nodes, and limit

## Table 1. Assumptions detected during assumption surfacing

```txt
I Inclusion of relevant factors.
Factor x is relevant to the issue
Factor x is not relevant to the issue

II Type of causal linkages
Factors x affects item y
Factor x does not affect item y
Factor x is sufficient in itself to have an effect on y
Factor(s) x are needed in conjunction with the factor(s) to cause an effect on z
Factor(s) x are not needed in conjunction with the factor(s) y to cause an effect on z
Factor x restricts effects on y
Factor x does not restrict effects on y

III Control of levers and triggers
Factor x is controlled by actor y
Factor x is not controlled by actor y
Factor x is determined by an environmental agent
Factor x is not determined by environmental agent

IV Direction and strength of causal linkages
The direction of influence between x any y is just the opposite
Factor x has a positive influence on factor y
Factor x has a negative influence on factor y
Factor x has a stronger influence on factor y
Factor x has a weaker influence on factor y
```

discussion to those items selected. In this latter case, the dialogue among participants thus provides a ‘human-based intelligence’ of the competitive or problem situation.

Our system has even greater potential in producing a greater variety of ‘machine-based intelligence’. We plan to consider additional prioritization schemes and build into the system over time inferencing schemes that will compare a user’s map with a set of stored ‘knowledge maps’. For instance, in refining prioritization schemes, we may wish to incorporate a rule that places a higher priority on nodes that differ the most in the number of causal links feeding them. The stored ‘knowledge maps’ provide a means for this assumption-surfacing approach to incorporating domain-specific expertise into the CSM process. A library of stored reference maps would represent a collection of commonly agreed-upon assumptions impacting issues of concern for the decision-making group. By referring to these stored maps for comparison with an individual’s map, differences between an individual’s view and what is considered ‘commonly accepted knowledge’ can surface. In effect, the system would make specific suggestions concerning what may be inaccurate with an individual’s view of a problem.

The object-oriented implementation of the CSM will facilitate the incorporation of this type of intelligence in that we would use the same type of link and node object for the stored knowledge maps. We would add methods to the object class that would help a 'stored' node or link determine if it is relevant to a similar one in a decision maker's individual map.

## 5.3 Scenario simulation

Figure 6 diagrams the objects driving the scenario simulation. An instance of the ScenarioSimulator, like the SituationMapper, opens a map window, while menu options allow specification of change values (positive or negative) for each lever or trigger node. The ScenarioSimulator then propagates these change values through the network of causal links to generate change values for the goal nodes. This process creates a scenario object, containing all the input and generated values. We can display the results of a scenario either by overlaying computed values on the map or by displaying a textual summary. The user can save alternative scenarios for later review. The nodes contain separate 'value' objects that contain attributes specifying both magnitude and time. These value objects are maintained independently of the nodes to allow maintenance of values for differing scenarios at different times.

Maintaining the spirit and power of the object-oriented representation, the computer code to generate results is associated with the object representing the information. The 'map' object uses a 'draw with scenario' method using the same procedures to draw the map as before, but adds to the representation value labels. Individual scenario objects contain methods to accept input values and display all its values in textual form. The 'link' and 'node' objects handle value propagation by receiving and transmitting 'transmit value' messages. We thus implement a constraint propagation concept commonly found within the AI literature (Stefic, 1981).

## 5.4 Consensus formulation

The ConsensusFormulator simply enables building new maps from two or more existing maps.

![](/api/attachments/6AH82NXW/fulltext/images/2e745e24c238669f68767d6d4730e1dd73d21927659ba556ac8687fca41e743d.jpg)  
Figure 6. Object classes with attributes that establish links between objects that are used by the scenario simulation segment.

The owner of the new map is a new participant type of object called a 'group'. The group object is a subclass of participant, inheriting all the behaviour of participant, but adding a membership attribute that associates two or more individual participants or subgroups to the group entity.

The ConsensusFormulator provides methods that enable the building of new maps by selecting and modifying links from existing maps. In effect, we implement a user-directed, 'cut and paste' operation on graphical objects. Once defined, such new groups behave as any other participant. We could then use the ScenarioSimulator and the AssumptionSurfacer to perform the forward and backward analyses on the consensual of partial consensus perspective. Thus, agreed-upon maps emerge through a dialectic process of group members discussing each other's maps, reviewing scenarios to test their implications and amending them accordingly until differences are either negotiated away or accepted. See Acar (1983) for a discussion of this process and an application of using CSM as a basis for group discussion.

Our prototype SituationAnalyser demonstrates the feasibility of using an object-oriented environment for generating causal maps. It also provides the structure for a knowledge base that uses causal maps as its foundation. The prototype is easy to learn and intuitive in its use. It is a system that is very flexible and highly interactive. The user can effortlessly move from one segment to another. Individual users, rather than the computer system, will usually control the sequence in which they perform the desired stages of causal analysis. The computer system simply provides support and structure in the development of a common understanding based upon the causal effects present in a problem situation.

## 6 IMPLEMENTATION CONSIDERATIONS

This approach greatly eases system design through generating a highly modular implementation and minimizing direct programming through code reusability. It facilitates development of systems of this complexity and allows for easy addition of new capabilities. For instance, a possible refinement to the prototype entails adding methods enabling the ScenarioSimulator to compare desired levels of goal variables with simulated ones and to suggest ways of resolving goal differences for changing inputs. With the current object structure, we can incorporate these additional features fairly easily by simply adding new methods.

The language used in developing our prototype is Smalltalk (Goldberg and Robson, 1983). We used a version of this language developed by Digitalk (see Smalltalk/Windows, 1990, for documentation on the latest version), which runs fairly well on the Intel 80386 microprocessor-based computers. We created a large proportion of this prototype using standard Smalltalk objects. This helped reduce considerably the programming effort needed. Within the Smalltalk environment, the developer is easily able to experiment with different user interfaces and incrementally expand the functionality of the system. The prototype provided a generally good demonstration of the technical feasibility of developing the type of system described in this paper.

The Smalltalk/Windows uses the Microsoft Windows GUI. Using a standardized GUI allows easier integration of new applications and expansion of existing ones. Indeed, since Windows is based upon objected-oriented concepts, it provides many of the advantages of using OOP. Implementation within such advanced operating environments presents the opportunity to utilize programs and tools developed in differing languages all within the same common user interface.

However, we have found problems in moving code from one operating environment to another. Various versions of our prototyping efforts are implemented in Smalltalk's own windowing system, in Windows 3.0 and OS/2 Presentation Manager. In converting from one environment to another, we have encountered major compatibility problems and conversion difficulties. Thus, we may wish to investigate alternative implementation environments. Current object-oriented extensions of the C and Pascal programming languages are increasing in popularity.

The implementation of the software within a multiuser environment is paramount among the technical concerns. There are available, within Smalltalk itself, language extensions providing support for multiprocessing and communications. Also, if we use a version of Smalltalk-implemented OS/2's Presentation Manager or Windows 3.0, we should be able to access networking tools available for those environments. In a recent paper, Heintz (1993) suggests the use of an object-oriented software environment for just managing GDSS applications and communicating among GDSS participants. Effective implementation of the mapping system suggested herein requires integrating it into a more comprehensive GDSS environment. Efforts along these lines are already under way.

There is a need for improved graphics. Large maps could necessitate higher resolution than is currently provided within the IBM PC environment. The capability for scrolling a large map within a window, resizing a window or zooming a window to occupy a full screen provided by the Smalltalk system helps in this regard; however, as maps become large, added capabilities for scaling and zooming on map segments may be necessary. Some alternative workstation environments do provide high-resolution graphics capability, but at a higher cost.

## 7 CONCLUSIONS

This paper examines the issue of developing a support system for strategic decision makers that would enable problem framing and consensus formulation based on an understanding of the variables affecting a situation and the causes and effects existing between them. It proposes the use of an 'object-oriented' development and programming approach, and briefly discusses a prototype implementation that demonstrates the feasibility of implementing such a system.

Although there are other tool implementations that attempt to have users map cause-and-effect relationships or have them more carefully structure the arguments they present, none provides as comprehensive support of a dialectically based decision-making process. We offer the first computerized rendering of Mason and Mitroff's (1981) and Acar's (1987) assumptional analysis. These assumptional analysis techniques are simplified adaptations of Churchman's (1971) dialectical inquiry to managerial decision making. We thus move closer to suggesting specific means of providing intelligence facilitation of the group decision-making process.

The object-oriented programming (OOP) approach enables the development of a highly interactive user interface and facilitates the incremental development of the system. These two factors are key to successful implementation. Since within an OOP environment, tools already exist for developing a graphically-oriented, multitasking system, considerably less effort is involved in producing a sophisticated user interface. The OOP environment also forces the development of highly modularized code, which greatly aids in the incremental development. Interactive editing and debugging tools make it easy to expand or modify existing or add new object classes.

There has been, in recent years, a resurgence of interest in cognitive mapping approaches (Barr, et al., 1992; Simons, 1993). The CSM causal mapping method itself (Acar, 1983) is a well-developed technique. Its forward analysis or simulation-like capability would allow policy makers easily to examine the implications of a strategy. The method also provides a backward analysis capability. This feature allows group members to determine the underlying causes and assumptions associated with an issue, and to work dialectically toward a possible resolution. However, future implementation may still require a number of refinements. The Scenario-Simulator may need development on goal-directed propagation techniques and goal-based inferencing methods. The AssumptionSurfacer may need a finer classification scheme for the various types of assumptions, refined methods for comparing map elements and a more specific 'case-base' inferencing strategy. We may also wish to develop further computational refinements for building causal maps from map segments and creating new maps by combining individual maps.

As the system evolves, refinement of the intelligent facilitation process provides a natural extension of the prototyping efforts. This paper has already identified three possible areas for incorporating more intelligence: prioritization of assumption-based anomalies, generation of alternative scenarios and using a case-based reasoning approach incorporating causal maps. Each of these needs further investigation and development. We could also provide specific rules for facilitating the overall process of generating causal maps by incorporating alternative means of providing domain-specific knowledge. For instance, rather than relying on stored maps, we could include specific assertions an expert may provide with respect to the plausibility of certain causal connections.

## REFERENCES

Acar, W. (1983) Toward a Theory of Problem Formulation and the Planning of Change: Causal Mapping and Dialectical Debate in Situation Formulation. University Microfilms, Ann Arbor, MI.

Acar, W. (1987) Toward expending dialectical inquiry: design requirements of a comprehensive dialectical inquiry system. Proceedings of the Annual Meeting of The Decision Sciences Institute. Boston, 1987.

Ackoff, R.L. (1962) Scientific Method. Wiley, New York.

Ackoff, R.L. (1981) Creating The Corporate Future. Wiley, New York.

Ackoff, R.L. & Emery, F.E. (1972) On Purposeful Systems. Aldine-Atherton, Chicago.

Axelrod, R. (ed.) (1976) Structure of Decision. Princeton University Press, Princeton NJ.

Bannister, D. & Fransella, F. (1971) Inquiring Man: The Theory of Personal Constructs. Penguin, London.

Barr, P.S., Stimpert, J.L. & Huff, A.S. (1992) Cognitive change, strategic action and organizational renewal. Strategic Management Journal, 13, 15–36.

Bui, T. & Jarke, M. (1989) Communications design for co-op: a group decision support system. ACM Transaction of Office Information Systems, 4(2), 81–103.

Carlson, D.A. & Ram, S. (1990) HyperIntelligence: the next frontier. Communications of The ACM, 33(3), 311–321.

Charalambides, L. & Heintz, T. (1988) Frame-based knowledge representation as a tool for organizational group decision support. Unpublished Working Paper, Marquette University.

Conklin, J. (1987) A Hypertext: An Introduction and Survey. Computer, September, 17–41.

Conklin, J. & Begeman, M.L. (1988) gIBIS: A hypertext tool for exploratory policy discussion. ACM Transaction on Office Information Systems, 6(4), October, 303–331.

Cox, B. (1987) Objects-oriented programming: an evolutionary approach. Addison Wesley, Reading, MA.

Dennis, A.R., George, J.F., Jessup, L.M., Nunamaker Jr, J.F., Vogel, D.R. (1988) Information technology ti support electronic meetings. MIS Quarterly, 12(4), December, 591–624.

DeSanctis, G. & Gallupe, R.B. (1981) A foundation for group decision support systems design. Management Science, 33(5), May, 589–609.

Diffenbach, J. (1982) Influence diagrams for complex strategic issues. Strategic Management Journal, 3, 133–146.

Easton, A., Vogel, D.R. & Nunamaker, J.F. (1989) Stakeholder identification and assumption surfacing in small groups: an experimental study. Proceedings of the twenty-second Annual Hawaii International Conference on System Sciences.

Eden, C. (1978) Operational research and organization development. Human Relations, (31)8, 657–674.

Eden, C. (1989) Using cognitive mapping for strategic options development and analysis (SODA). In: Rosenhead, J. (ed.) Rational analysis for a problematic world: problem structuring methods for complexity, uncertainty, and conflict. John Wiley, Chichester, UK.

Eden, C. & Radford, J. (1990) Tackling of Strategic Problems, the Role of Group Decision Support. Sage, London.

Eden, C., Ackerman, F. & Cropper, S. (1992) The analysis of cause maps. Journal of Management Studies, 29(3), May, 310–323.

Emery, F.E. & Trist, E.L. (1973) Towards Social Ecology. Plenum, New York.

Gallupe, R.B., DeSanctis, G.L. & Dickson, G.W. (1988) Computer-based support for group problem finding: an experimental investigation. MIS Quarterly, 12(2), June, 277–296.

Goldberg, A. & Robson, D. (1983) Smalltalk-80 The Language and Its Implementation. Addison Wesley, Reading, MA.

Gray, P. (1987) Group decision support systems. Decision Support Systems 3(3), September, 233–242.

Heintz, T. (1993) An object-oriented architecture for the design of group decision support systems. The Journal of Group Negotiation and Decision, 2(1), 5–25.

Heintz, T. & Acar, W. (1992) Toward computerizing a causal modeling approach to strategic problem framing. Decision Sciences, 23(5), 1220–1230.

Huber, G.P. (1984) Issues in the design of group decision support systems. MIS Quarterly 8(3), 195–204.

Jarke, M. (1986) Knowledge sharing and negotiation support in multiperson decision support systems. Decision Support Systems 2(2), 92–102.

Jarvenpaa, S.L., Rao, V.S. & Huber, G.P. (1988) Computer support for meetings of groups working on unstructured problems: a field experiment. MIS Quarterly, 12(4), 645–665.

Jones, S. & Eden, C. (1981) O.R. in the community. Journal of the Operational Research Society, 32, 335–345.

Joyner, R. and Tunstall, K. (1970) Computer augmented organizational problem solving. Management Science, 17(4), B212–B225.

Kelly, G.A. (1955) Psychology of Personal Constructs, Vols 1 and 2, Norton, New York.

Kraemer, K.L. & King, J.L. (1988) Computer-based systems for cooperative work and group decision making. ACM Computing Surveys, 20(2), 115–146.

Lai, K., Malone, T.W. & Yu, K. (1988) Object lens: a 'Spreadsheet' for cooperative work. ACM Transactions on Office Information Systems, 6(4), 338–353.

Lind, M.R. & Zmud, R.W. (1991) The influence of a convergence in understanding between technology providers and users on information technology innovativeness. Organizational Science, (2)2, 195–217.

Malone, T.W., Grant, K.R., Turbank, F.A., Brobst, S.A. & Cohen, M.D. (1987) Intelligent information sharing systems. Communications of the ACM, 30, 390–402.

Maruyama, M. (1963) The second cybernetics: deviation-amplifying mutual causal processes. American Scientist, 51, 164–179, 250–256.

Mason, R.O. (1969) A dialectical approach to strategic planning. Management Science, 15(8), B403–B414.

Mason, R.O. & Mitroff, I.I. (1981) Challenging Strategic Planning Assumptions. Wiley, New York.

Meyer, A.D. (1991) Visual data in organizational research. Organizational Science, 2, 217–236.

Mill, J.S. (1862) A System of Logic. Parker, Son, and Bowen, London.

Mitroff, I.I. & Emshoff, J.R. (1979) On strategic assumption-

making: a dialectical approach to policy and planning. Academy of Management Review, 4(1), 1–12.

Mitroff, I.I., Mason, R.O. & Barabba, V.P. (1987) Policy as arguments — a logic for ill-structured decision problems. Management Science, 28, 1391–1404.

Nunamaker, J.F., Applegate, L.M. & Konsynski, B.R. (1987) Facilitating group activity with GDSS. Journal of Management Information Systems, [b]3(4), 5–19.

Nunamaker, J.F., Applegate, L.M. & Konsynski, B.R. (1988) Computer-aided deliberation: model management and group decision support. Operations Research, 36, 826–848.

Pinsonneault, A. & Kraemer, K.L. (1990) The effects of electronic meetings on group processes. European Journal of Operational Research, 46, 143–161.

Rosenhead, J. (ed.) (1989) Rational Analysis for a Problematic World. John Wiley, Chichester, UK.

Smalltalk V/Windows, Tutorial and Programming Handbook (1991) Digitalk Inc., Los Angeles.

Simons, T. (1993) Speech patterns and the concept of utility in cognitive maps: the case of integrative bargaining. Academy of Management Journal, 36(1), 139–156.

Stefik, M. (1981) Planning with constraints (MOLGEN: Part 1). Artificial Intelligence, 16(2), 111–140.

Stefik, M., Foster, G., Bebrow, D.G. et al. (1987) Beyond the chalkboard: computer support for collaboration and problem solving in meetings. Communications of the ACM, 30(1), 32–47.

Toulmin, S. (1958) The Use of Argument. Cambridge University Press, Cambridge, MA.

Watson, R.T., DeSanctis, G. & Poole, M.S. (1988) Using a GDSS to facilitate group consensus: some intended and unintended consequences. MIS Quarterly, 12, 463–478.

Winograd, T. (1987–88) A language/action perspective on the design of cooperative work. Human-Computer Interaction, 3(1), 3–30.

Weick, K.E. (1979) The Social Psychology of Organizing, Addison-Wesley, Reading, MA.

Zigurs, I. (1989) Interaction analysis in GDSS research: description of an experience and some recommendations. Decision Support Systems, 5(2), 233–241.

## Biography

Timothy J. Heintz is an associate professor of business administration at Marquette University. He holds a DBA in quantitative business analysis from Indiana University with minors in management information systems and operations management. His current research interests are in the application of techniques from the field of artificial intelligence to business problems and development of large database systems. He has been focusing on applications that involve planning, coordination and communication among groups of individuals in organizations and data warehousing. He has published in Decision Sciences, The

Transportation Research Record, The Canadian Journal of Operational research and Information Systems, The Journal of Experiential Learning and Simulation, Information and Management and others. He is currently a member of The Institute of Management Sciences and the Decision Sciences Institute.
