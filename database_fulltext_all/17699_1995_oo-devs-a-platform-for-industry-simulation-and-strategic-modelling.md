---
otero_id: 17699
otero_key: "MQDAXS6J"
title: "OO/DEVS: A platform for industry simulation and strategic modelling"
authors: "P. Ninios; K. Vlahos; D.W. Bunn"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00013-v"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# OO/DEVS: A platform for industry simulation and strategic modelling

P. Ninios, K. Vlahos \*, D.W. Bunn

London Business School, Regent's Park, London NW1 4SA, UK

## Abstract

OO/DEVS is a software platform designed for industry modelling and simulation. By that we refer to the modelling of enterprises, their policies and their interaction in the marketplace with the aim to explore different industrial scenarios or alternative strategies. The framework exploits concepts from Object Oriented design and analysis, as well as the Discrete Event System Specification (DEVS) formalism, to support the development of natural, modular and reusable models. This paper provides an overview of OO/DEVS and discusses its implementation in Smalltalk. It also presents its graphical user interface that allows graphical model design and management:

Keywords: Simulation; Object orientation; Strategic modelling; Modelling environments

## 1. Introduction

The use of simulation for the development of business strategy models and the facilitation of executive debate, focusing on the exploration of different scenarios and the formulation of future policy is now well established (for example see [2], [9], [10]). Industry simulation is a term describing this type of simulation, to distinguish it from applications of simulation to manufacturing and distribution logistics.

The participants of an industry simulation exercise are invited to think about the structure of the industry and the behaviour of its main players. A model of the industry is developed, which represents the shared understanding of the functioning of the industry. This is usually followed by the elaboration of credible industry scenarios which are simulated in order to explore the impact of interrelationships and the main uncertainties. Interest focuses on the dynamic behaviour resulting from the industry structure and its relation to different postulated strategies. The whole process aims at enhancing the group's understanding of the main issues in the industry and will, its advocates argue, lead to the development of robust strategies. Finally, the models developed document the shared understanding of the industry and facilitate communication with other people in the organisation. Fig. 1 summarises the main objectives of industry simulation.

System Dynamics has been the most popular technique to support this style of industry simulation. Despite its growing success, however, some criticism has surfaced within its own community related to its core technology (differential equations that are expressed as stocks and flows) [11]. Overall, we have suggested that the associated practical limitations can be classified as related to structure (modelling generalisation, aggregation and association relationships within a model), focus (modelling sufficient level of detail), reusability (creating reusable model components), and time-representation. We have attempted to address these issues, and to present an alternative platform called Object Oriented/DEVS (OO/DEVS), based on the object oriented paradigm and the Discrete Event System Specification (DEVS) formalism. The former provides the framework with the conceptual tools for model building while the latter supports a concise way to represent time as discrete events.

![](/api/attachments/MQDAXS6J/fulltext/images/2213df4b77854637774039a128fbd9ad32528606b64ed214b530e69de72064fe.jpg)  
Fig. 1. The aims of industry simulation

This paper provides an overview of OO/DEVS and discusses in some detail its implementation in Smalltalk/V for Windows. We start by presenting the main features of the OO/DEVS. Then the object oriented implementation of the DEVS formalism is described and compared to earlier implementations. This is then followed by the description of the OO/DEVS GUI. The GUI removes the need for programming by providing the means for graphical model building with little or no knowledge of programming syntax. The use of model bases and live communication to other applications, in particular spreadsheets, through DDE is also discussed. Finally, the “Beer Game” (for a description of the game see $[16]$ ) is used as an example, demonstrating the functionality of OO/DEVS in a context well known to the system dynamics community, thereby facilitating direct comparison.

## 2. OO / DEVS: An overview

As we have mentioned earlier OO/DEVS has been conceived and developed, as a fundamental extension to System Dynamics for industry modelling and simulation (see $[11]$ for a comparison of OO/DEVS to System Dynamics). In that respect it provides expressive power to model not only association relationships (as in SD) but also aggregation and generalization ones. Overall, the OO/DEVS platform provides for:

1. Entity based modelling: encapsulation and message passing allow the modeller to think and model the industry in terms of the main players, their strategies and the way they interact. Each player can be viewed as an object with specific attributes and methods that represent decision rules. The OO/DEVS paradigm allows this natural type of thinking to be directly mapped into a representation that can then be simulated.

2. Specialisation / generalisation: inheritance is one of the most powerful concepts supported by the object oriented paradigm. Objects that share common attributes and behaviour can be modelled in generic classes and organised in a tree-like structure.

3. Time representation: a concise way (through DEVS) to represent time as events within the system and furthermore to bound decision rules (that are object methods) to time.

4. Aggregation / disaggregation: the ability to construct coupled models from a set of atomic models allows the modeller to develop detailed decision support systems by modelling the required level of detail in atomic models. At the same time a strategic “view from above” can be maintained by monitoring behaviour at different aggregation levels.

5. Separation of models and simulation engine: this is achieved through the ability to have generic simulator and coordinator modules attached to models. This is particularly attractive because it provides the basis for treating models as knowledge and creating model-bases.

6. Modularity, reusability, extensibility: due to the separation of models and simulation engine, objects can be stored in a model base. In addition, inheritance and encapsulation provide the means of extending, modifying and reusing old model components.

In the following sections we present the foundations of the DEVS formalism and present our object-oriented implementation.

## 2.1. The DEVS formalism

The Discrete Event System Specification formalism (DEVS, [20], [21]), is one of the basic formalisms for discrete event modelling. It provides a formal representation of discrete event systems capable of mathematical manipulation just as differential equations serve this role for continuous systems. The formalism has been used to support the design of computer architectures, communication networks and multi-robotic and manufacturing systems [15],[17].

In the DEVS formalism, it is necessary to specify: (a) the basic models (atomic models) from which larger one could be build, and (b) how these models are connected together in a hierarchical fashion to form coupled models. Atomic models are defined as mathematical structures:

$$
\mathbf {M} = <   \mathrm{X}, \mathrm{S}, \mathrm{Y}, \delta_ {\text { int }}, \delta_ {\text { ext }}, \lambda , t a >,
$$

where X is the set of external input values, Y the set of output events, S the sequential state set, $\delta_{int}$ the internal transition function, dictating state changes due to internal events, $\delta_{ext}$ the external transition function, dictating state changes due to external events, $\lambda$ the output function, generating external events at the output, and ta the time advance function.

Under the constraints:

(i) ta is a mapping from S to the non-negative reals with infinity:

$$
\mathrm{ta}: \mathrm{S} \rightarrow \mathrm{R} _ {0, \infty} ^ {+}
$$

(ii) the total state set of the system specified by M is:

$$
\mathrm{Q} = (\mathrm{s}, \mathrm{e}) | \mathrm{s} \in \mathrm{S}, 0 \leq \mathrm{e} \leq \mathrm{ta} (\mathrm{s}),
$$

where s the sequential state, and e the elapsed time spend in this state.

$$
\text {(iii)} \delta_ {\mathrm{int}}: \mathrm{S} \rightarrow \mathrm{S}
$$

$$
\mathrm{(iv)} \delta_ {\mathrm{ext}} \colon \mathbf {Q} \times \mathbf {X} \rightarrow \mathbf {S}
$$

Atomic models can be coupled to form a multi-component DEVS which is defined as a structure:

$$
\mathrm{DS} = <   \mathrm{D}, \{\mathrm{M} _ {\mathrm{i}} \}, \{\mathrm{I} _ {\mathrm{i}} \}, \{\mathrm{Z} _ {\mathrm{ij}} \}, \text { SELECT } >,
$$

where D is a set, the component names, $M_{i}$ is a component DEVS model for each i in D, $I_{i}$ is a set of influencees of i, $Z_{ij}$ is the transition function from i to j, for each influencee j in $I_{i}$ , and SELECT is the tie breaking selector (i.e. selects which of the next events will be executed first when more than one have the same scheduled time).

## 2.2. DEVS implementation views

Zeigler [22] (see also [15]) has used the DEVS formalism as the foundation for a general purpose simulation environment, based on the principles of the abstract simulation developed by Concepcion and Zeigler [1], as part of the DEVS theory. This DEVS-Scheme simulation environment, developed in a Lisp dialect, separates models (entities of the system modelled) from the mechanics of carrying out the simulation. It introduces two generic classes of objects, models and processors. Atomic and coupled models are specialisations of models, whilst simulators and coordinators are specialisations of processors. Simulations are carried out as follows: Simulators and coordinators are assigned to handle atomic models and coupled models respectively, in a one-to-one fashion. A root-coordinator, a special type of processor, manages the overall simulation and is linked to the coordinator of the outermost coupled model. Thomasma and Ulgen [17] take a similar view in their Smalltalk-80 implementation, while in the Linvy [8] implementation no distinction is made between atomic and coupled models.

Simulation is carried out by message passing among the processors which carry information concerning internal and external events. Time is represented through the event scheduling world view. The DEVS state set is represented by component states that consist of sets $(s_{i}, \sigma_{i})$ where $s_{i}$ a state and $\sigma_{i}$ the non-negative time-left component representing a scheduled event of component i. If $\sigma_{i} = \infty$ then the component i is passive.

Each time an internal event occurs $\delta_{\mathrm{int}}(\mathrm{s}_{\mathrm{i}})$ , the corresponding model component is processed. Actions may cause changes to the influences of the active component. Each time an external event $x \in X$ occurs, the event is said to be ignored if the model remains scheduled to undergo a transition from the same state as it was before, or is said to cause an interrupt and causes a state change and/or a rescheduling of the model's next internal transition.

In Zeigler's implementation [22], every DEVS-model communicates with its world through a set of input and output ports. The addition of the concept of a port represents an extension of the original Discrete Event System Specification as formally defined by Zeigler [20], and was introduced by Linvy [8], who has also produced a DEVS implementation using this concept. The advantage of the port structure is that it enables the modeller to represent the coupling specification within two DEVS as a mapping from the output port of one DEVS to the input port of the other. Such a mapping preserves the autonomy and structural independence of the two systems and thus leads to modular and extensible models.

In Zeigler's implementation, messages are triples of the form: Message = <source, time, <port, value >> . The fields of these triples correspond respectively to the source of the message (a DEVS model), the time that it was send, the port that it was send from and a value that the message is carrying. Four types of messages facilitate the message passing between Processors: \*, x, y and done message. When a Coordinator of a Coupled Model receives a message, the coupling scheme is consulted and the message is translated and dispatched accordingly. When a Simulator of an Atomic Model receives a message two things can happen. If the message is a \*-message that means that the model is scheduled to undergo its next internal transition. This results into the triggering of the output function that produces output into the output ports, and the triggering of the internal transition function that changes the state of the model. If the message is an x-message then the model is about to receive input in one of its input ports. Then the external transition function is triggered and in accordance to the port that the input is placed some specific operation is performed. Overall, the external transition, internal transition and output functions provide a mapping between the ports of the model and the operations that the model can carry out. The basic characteristics of the DEVS-Scheme have been transferred in a C++ implementation by Kim and Park [7].

## 2.3. Modelling object oriented message passing within DEVS

Given the acceptance of the compatibility between OO and discrete event world view formalisms $[12]$ , the Object Oriented language Smalltalk $[3]$ has been used as the implementation platform for OO/DEVS. A fundamental implementation objective was to exploit fully the naturalness and modularity provided by object orientation. Taking a critical view in the design of a DEVS simulation environment we can identify that the fore-mentioned design poses a certain incompatibility with the classic OO view, due to the fact that the interface of a DEVS object to the rest of the object world is through the internal transition, external transition and output functions. The addition of the port concept alleviates partially this problem, as the ports constitute a kind of interface. Nevertheless, a pure object oriented design would identify the main actions (responsibilities) of each object and model them through methods and message passing (see $[4]$ , $[19]$ ). Moreover, the main attraction of such an approach is that a DEVS-model would be more transparent, as its main functions would be identifiable by looking at the interface and not the specifications of the three fore-mentioned functions. Selective specialisation of behaviour through inheritance is also facilitated.

It is this objective that has mainly driven our Smalltalk implementation, in which we exploit fully the message passing concept of object orientation. As we mentioned above, objects communicate in object oriented environments by message passing. Each object has a set of methods that are made up of selectors and arguments. A message expression describes a receiver, a selector and possibly some arguments. Every object can request from another object to execute one of its methods through a message expression [6]. However, message passing within the DEVS-Scheme specification is not that straight-forward. While we would like objects to communicate with each other, the communication should be performed through the coupling mechanism as part of the simulation process. This restriction means effectively, that some objects should be able to invoke only some methods of some other objects in a model. The modelling question here was whether or not we could exploit directly the object oriented view and remove the DEVS functions without loosing the DEVS functionality. In addition, this posed the additional design issue of how to model object oriented like message passing at the coupled-model level (aggregation level).

## 2.4. Towards an object oriented DEVS implementation

In our OO/DEVS implementation we first tried to address the issue of using OO type message passing, skipping the three types of functions implicit in DEVS, as well as bypassing completely the concept of the port. This objective resulted into a design that literally transfers the responsibilities of the internal transition, external transition and output functions to the simulator of an atomic-model. It should be pointed out, that a fundamental design consideration, in order to achieve this, is related to the way we represent messages within the OO/DEVS environment. Our design decision was to model messages as instances of the class SimulationMessage which is a subclass of class Message of Smalltalk. As a result, a SimulationMessage can be represented by a structure: <receiver, selector, arguments, source, method, time>. Variables “selector”, “receiver” and “arguments” are inherited from class Message. The variable “source” contains a reference to the DEVS-model that is the sender of the message. The variable “method” contains the name of the method that sends the message. And finally, “time” is a variable that contains the simulated time that a message was send.

Under our implementation, we have two classes of objects: Model and Simulator. The advantage of providing a unified view of Model (by combining the functionality of atomic and coupled model at the same level) is that the framework benefits by the property of being able to operate at any level using the same set of constructs. Class Model provides the constructs to specify new methods, influences between two models (by specifying method-to-method relationships), and message structures for model output. Each instance of Model also contains a messageList that accommodates a set of messages to be triggered by the simulator when a specific method of the Model has been triggered. The contents of the messageList are specified by the modeller upon model specification.

Every instance of Model (or of a subclass of Model) is an object with some specific functionality (for example a company that invests and retires production capacity), that has a (possibly empty) list of children. The modeller is given the ability to specify which methods of the subordinate models are methods of the aggregate model, and therefore provide selected functionality (methods) of the sub-models at the aggregate model level. This view of aggregation of DEVS models is compatible with the emerging view of aggregation in object orientation (see [5] for the layers concept in object oriented design). For example, in Fig. 2 objects A and B represent DEVS-models, where B has two methods that process input, and A has one method that process output. Model C is an aggregate version of A and B that can respond to messages which have the same receivers as the methods of A and B.

![](/api/attachments/MQDAXS6J/fulltext/images/c1dced6d5776beaef4956af28fec1bdb24b9f208e76759e2403065ee8849c74b.jpg)  
Fig. 2. The aggregate version of A and B.

It should be pointed out that such a view does not violate the DEVS definition of neither the atomic nor the coupled model. In the case of an atomic model (which will be an instance of a subclass of Model) two different disjoint sets of methods will be corresponding to the external and internal transition functions, while their selectors will accommodate the X and Y sets correspondingly. At the coupled model level, $M_{i}$ is an object corresponding to a component DEVS-model, $I_{i}$ is a set of models coupled with model i (that would belong to the influences of i), and finally $Z_{ij}$ will be the i-to-j output translation and is a method-to-method relationship in the form of a quadruple: < from\_Model, from\_Method, to\_Model, to\_method>.

The simulation capabilities of a DEVS-model have been transferred to its Simulator (an instance of class Simulator). As a result three methods have been created (see Fig. 3). Method perform is triggered when its DEVS-model is imminent. Perform triggers the imminent method and then traverses the messageList to output all the messages linked to the triggered method. Notice that the expressive power provided by such a view is equivalent to the atomic-model internal transition function, as discussed in the DEVS-Scheme. This can be shown by scheduling a message to self at time zero, which can produce the same effect as the sequence output function–internal transition function, i.e., change the state of the model after output. Method input is triggered to dispatch an incoming message to the associated DEVS-model, and finally, method output is triggered when its DEVS-Model sends an output message. An output message can be either a message to other objects in the overall model, or a message to self. In that way objects can schedule themselves to trigger one (or more) of their methods in the future.

All three methods handle and dispatch instances of class SimulationMessage. It should be pointed out that, while in the DEVS-Scheme implementation only coupled models have wait lists that store messages of their subordinate models, in our implementation every model has a wait list. As a result, an “atomic model” object can schedule itself to trigger more than one of its methods in the future, and can also remove messages from its waitList as it has direct access to it. In addition, $\sigma$ , and as a consequence the ta function (time-advance), are specified by the time of the imminent message.

## 3. Graphical support for model building

The goal of OO/DEVS GUI is to allow the modeller to form clear mental images of the model's structure and function. The need for model visualization, and the advantages that represents over textual modelling languages has been stressed by a number of researchers (for example see [13]). 'Visual' software has proved these advantages in a number of simulation areas, with iThink [14] as a distinct example within the SD modelling community. However, the success of a GUI is very much based on the model structuring tools that it provides. In this respect the intrinsic characteristics of OO/DEVS provide the basis for a semantically rich model visualization platform which can fulfil the above goal.

![](/api/attachments/MQDAXS6J/fulltext/images/0f66689a29c3262bdd5b7ee9110eae30339c78af69a61ed101c7fdf8d102bd10.jpg)  
Fig. 3. The interface of the Simulator.

The modeller, and indeed the user, can build and view an OO/DEVS model through three types of diagram, which depict the specialization, aggregation and association relationships within the model. These diagrams are represented within corresponding windows in the GUI: (i) the Class Hierarchy Diagram (see Fig. 4), which is the equivalent to the class hierarchy diagram of an OO language, but for the model hierarchy within OO/DEVS. This diagram shows the model components (objects), which can be used to build an OO/DEVS model. These objects are subclasses of TModel which, as we have discussed earlier, is the object that carries the essential functionality for a model to be simulated. The subclasses of TModel contain methods that represent decision rules that will be utilised during a simulation run.

(ii) the Model Decomposition Diagram (Fig. 5) which provides a platform for model conceptualization, as it allows the user to view and (re)structure the model at different levels of detail. Model building takes place within the Model Decomposition Diagram window, as the user picks with the mouse model components from the Class Hierarchy Diagram and pastes them on existing model components within the Model Decomposition Diagram. The user has the ability not only to paste the newly selected models but to cut models previously added to the decomposition diagram, and consequently paste them to other models. This quality of the interface is a direct consequence of the underlying modelling paradigm, and can be used as a powerful tool for experimentation with different model structures.

(iii) the Level Diagram (Fig. 6) which provides a view of the decomposition diagram, from the top. It allows the user, to zoom in and out of model aggregates, as well as to create and view influences between different sub-models as he/she dissects the Model Decomposition Diagram.

![](/api/attachments/MQDAXS6J/fulltext/images/79ae3330c6862091898153abfa6db2e4fdb3477990af2b27001c2e213176f864.jpg)  
Fig. 4. The Class Hierarchy Diagram.

## 3.1. The GUI smalltalk implementation

The OO/DEVS GUI is based on three main classes. Class TreeDiagram provides the functionality for drawing hierarchical tree structures. This is a class that provides the generic functionality for two subclasses: DecompositionDiagram and HierarchyDiagram. These two classes cater respectively, for the aggregation and generalization relationship modelling of the model components. The third class, the Level Diagram, provides the graphical tools for association relationship modelling.

The HierarchyDiagram class provides the functionality specific to the Model Hierarchy Window. Here, the user may add or remove model components, add or change model decision rules (methods), create new instances of the model components and specify message protocols.

![](/api/attachments/MQDAXS6J/fulltext/images/b672bd12ae43dda1fe00410dc61b3d76f98cab7e1785b218cdcf8682c63bb84f.jpg)  
Fig. 5. The Model Decomposition Diagram.

The Decomposition Diagram class, allows the model components to be aggregated by cutting and pasting the tree nodes (which represent instances). This class also provides for model simulation. This mechanism is hidden from the user, and effectively couples the object models to Simulators so that a simulation run can be initiated. In addition to the above functionality, the class provides for model variable initialization, specification of public versus private methods for each of the models, and for each model aggregate entry into its relevant level diagram.

Class Level Diagram finally, permits links to be created and removed between the components of aggregate models. These links are displayed graphically as lines between the object entities on the screen, and represent relationships of the type <modelFrom, methodFrom, modelTo, methodTo> between the models within a level diagram. The presence of a link denotes the existence of a message protocol between two model objects.

Message protocol dialogues facilitate message specification, addition, deletion, editing and sequencing. The definition of the message passing protocol between OO/DEVS models, is facilitated at two levels: (i) The first level is within the Class Hierarchy Diagram. At this level, the modeller can define, the message protocol that will be common for all the instances of a specific model class. The receiver of a Message, at this stage, may be defined either as self, or as undefined. Undefined receivers will be automatically specified later when the user draws links between models, and evokes the messages specified at the class level. This approach enhances model reusability as models (and their subclasses, as the message protocol is inherited in an OO fashion) know how they may behave in a simulation run, but they do not know yet which are the other models within an overall model space.

![](/api/attachments/MQDAXS6J/fulltext/images/39d01411109fcaab5e9b59746da3422a5e496e2ab37e4f9a7a8616f6f7a5cc8a.jpg)  
Fig. 6. Level Diagram.

(ii) The second level for message protocol specification exists within the Level Diagram. At this stage the modeller is presented with the class message protocol, from which he/she can select messages for the specific instance, while maintaining the ability to specify new messages in the message protocol of the instance.

## 3.2. Decision rule modelling

In terms of decision rule modelling, our objective is to provide the modeller with a number of tools that can be used in accordance to the specific problem in hand. Currently, two ways of decision rule modelling are offered, the first one is to write Smalltalk code, while the second is to

![](/api/attachments/MQDAXS6J/fulltext/images/2d8c4277aa92acc6f731350a795dad12aaf2b81d6b66d02593ccd0b07554397e.jpg)  
Fig. 7. Spreadsheet Decision Rule Specification Dialog.

link an object method to a spreadsheet, through the Windows DDE interface. This requires the modeller to specify a number of input and output cells within the client spreadsheet, which provide the interface to the OO/DEVS object. After the definition of the interface, facilitated by a simple dialogue box (see Fig. 7), the modeller can use straightforward spreadsheet modelling in specifying the required decision rules. The advantage of this approach lies in the fact that it utilises the experience of most modellers in using spreadsheets, while at the same time provides a consistent interface to a broad base of models (for example financial analyses) that can exist independently outside the scope of the simulation model. It should be noted, that the same principle can be used to provide access to databases or other Windows applications that support DDE. In that respect an OO/DEVS model can be viewed as a platform that integrates information existing outside the simulation model but relevant to different parts of it.

## 3.3. Support for reusable model components

The DDE functionality enables the incorporation and reuse of existing corporate models within the OO/DEVS environment. In addition, reuse of model components is promoted in two different ways:

![](/api/attachments/MQDAXS6J/fulltext/images/2c15b3c958941aef5bf60eef0169f8398b516e04f547b9852442d838f97dbbb9.jpg)  
Fig. 8. Model Browser.

1. (a) at the level of the class hierarchy diagram The decomposition of the internal/external transition and output functions into a set of methods results in a finer granularity of the specification of behaviour. Therefore, by using inheritance to derive specialised versions of object classes, the user can easily reuse or overload parts of the object behaviour.

2. (b) at the level of the model decomposition diagram Model instances, both atomic and coupled (ie. aggregate models), can be saved into disk with all the information they contain, which includes the initialised state set and the coupling specification. The saved models can be retrieved independently to become components of larger models. Moreover, the user can open more than one model decomposition diagrams and use the cut and paste facility to move or copy model instances between the different diagrams.

## 4. Using the OO/DEVS GUI: the beer game example

The Beer Game is a classic System Dynamics model that explores the behaviour of a dynamic feedback system. It involves a distribution chain the constituents of which are customers, a retailer, a distributor and a brewery. The model explores the effects of time lags within the beer ordering and distribution system when a demand shock is transmitted through the system. The aim of the game, is to demonstrate how the initial shock is amplified regarding the inventories of the entities within the distribution chain, given different decision rules about ordering, formulating demand expectations and maintaining effective inventories.

The first window of the OO/DEVS GUI, that the modeller encounters, is the Class Hierarchy Diagram containing the OO/DEVS class hierarchy (see Fig. 4). Within this window the modeller can add, delete and edit model classes. At this point the behaviour of the Beer Model entities has to be coded in Smalltalk or within a spreadsheet environment (at the current implementation Lotus 1-2-3 and Quattro Pro have been used for that purpose). Since the behaviour of the Retailer, Wholesaler and Brewery is similar, inheritance is utilised and a superclass is created to cater for the commonalities in behaviour. Fig. 8 depicts the classic Smalltalk model browser of the GUI. The three top panes from left to right depict the instance variables of the model, its superclasses and its methods. The bottom pane depicts the behaviour under the method #dispatchGoods:.

![](/api/attachments/MQDAXS6J/fulltext/images/1c1267866fc42e4cfe354a25ad110da17d85692661c7faa4fa0a1e6449e223cc.jpg)  
Fig. 9. Message Protocol Dialogue.

Instances of each model component may be created by clicking the mouse over the desired object. Instances may be named and pasted into the Decomposition Window (see Fig. 5). This Window displays a similar tree structure to that of the Hierarchy Window and permits the cutting and pasting of nodes to form aggregate models. In our example the basic structure of the Beer Model can be obtained by selecting an instance of TModel to represent the model aggregate, and pasting on it instances of the classes BMCustomer, BMRetailer, BMWholesaler and BM-Brewery respectively.

The Level Diagram (see Fig. 6) may be obtained by clicking the mouse over a node in the Decomposition Window and selecting the relevant option from the pane menu. The Interface will open the Level Diagram with all the instances aggregated immediately below the selected node in the Decomposition Diagram being displayed. The user can move the iconised representations of these instances around the screen and create the message protocol between individual instances. As an example Fig. 9 depicts the

![](/api/attachments/MQDAXS6J/fulltext/images/b4c7c96bf7a299640e6194a60cc07e93c44b0a85a806dd5543c60ea5ca985b53.jpg)  
Fig. 10. Retailer Inventory.

Message Protocol Dialogue for the model Customer. This specifies that the message displayed will be triggered as soon as the method #demand is evoked. This message will trigger the method #receiveOrder of the model Retailer at the current clock time, with arguments the current demand value (note that demand is one of the instance variables of the model Customer).

Along with the message protocols the modeller has to specify one or more initial messages. By default, all models are initialised to do nothing unless the modeller specifies that a method will be triggered at some point in time. As a consequence, it is vital that at least one of the models is initialised to perform one of its methods, in order to start a simulation run.

As soon as the initial messages and the message protocols have been set up the model is ready to be simulated. Variable monitoring facilities are provided within the GUI, and model variables can be inspected for each simulation run. Figs. 10 and 11 depict the inventories of the entities Retailer and Brewery respectively. The amplified effects of the initial demand change (4 cases of beer for period 1 to 8 thereafter) combined with the delays in the system can be easily seen in the inventories of the two entities.

More elaborate versions of the initial model, can be produced by increasing the level of detail in some model components, while reusing existing ones. For instance, the brewery can maintain the data series related to the previous orders and use a forecasting model to set up the desired inventory. This situation can be modelled in OO/DEVS by adding a subclass of the class Brewery, say “BreweryWithForecastedInventory”, in the class hierarchy diagram that has one extra variable with the data series of previous orders, and overloads the method “formulateDesiredLevels” to cater for the implementation of the forecasting model. The user can introduce this new level of detail in the model reusing the initial model by simply removing the instance of Brewery and substituting it with an instance of the class ‘BreweryWithForecastedInventory’. In addition, the model can be expanded by adding new entities in it using the cut and paste facilities of the model decomposition diagram (see Fig. 12 for a version with two breweries and their aggregate).

![](/api/attachments/MQDAXS6J/fulltext/images/5102f39284749ddeb97a5e2b9bdbad0ecf3999423a313f4f32640250a0256010.jpg)  
Fig. 11. Brewery: Inventory.

## 5. Conclusions

In this paper we have presented a platform for industry simulation based on object oriented design and the DEVS formalism. The Smalltalk implementation and the GUI were described in some detail. OO/DEVS, as a modelling environment offers a number of features that are particularly attractive for strategy analysis and executive decision support modelling, namely:

1. entity based modelling that minimises the gap between mental and computer models

2. support for aggregation/disaggregation, that helps modellers view a model at different levels of detail

3. an easy-to-use GUI that allows non-programmers to create useful models

4. graphical representation of model structure

5. live links to spreadsheets, for decision rule modelling, that expand the scope and power of the models and help tap into existing company models

The features of OO/DEVS were demonstrated with the beer game example. A real life application from the UK electricity industry is presented in [18]. OO/DEVS is currently used and tested by users from industry and their input will be instrumental in further developing and refining the software. Overall a key contribution is the extension of functionality of the currently popular System Dynamics approach to industry simulation. This suffers from problems of model reusability and extensibility (a virtue is made of SD models being small and discardable, but this is out of necessity). The OO platform described here facilitates modular design and, through DDE facilities, integration with other functionally-rich models.

![](/api/attachments/MQDAXS6J/fulltext/images/cc7855bb793a299ea82e2f39175b9315fefbb70fe0d6e40381d81bdec5df91fd.jpg)  
Fig. 12. Expanded model decomposition diagram.

## References

[1] A.I. Concepcion and B.P. Zeigler, DEVS Formalism: A Framework for Hierarchical Model Development, IEEE Transactions on Software Engineering, Vol. 14, No. 2, 1988.

[2] D.W. Bunn and E.R. Larsen, Sensitivity of Reserve Margin to Factors Influencing Investment Behaviour in the Electricity Market of England and Wales, Energy Policy, 1992.

[3] Digitalk Inc., Smalltalk/V for Window: Tutorial and Programming Handbook (Los Angeles, 1991).

[4] E. Gibson, Objects-Born and Bred, Byte, 1990.

[5] I. Graham, Migration using SOMA: A semantically rich method of object-oriented analysis, Journal of Object Oriented Programming, Vol. 5, No. 9, 1993.

[6] A. Goldberg and D. Robson, Smalltalk-80: The Language and its Implementation (Addison-Wesley, Reading, MA, 1983).

[7] T.G. Kim and S.B. Park, The DEVS Formalism: Hierarchical Modular Systems Specification in C++, Proceedings of the 1992 European Simulation Multiconference, 1992.

[8] M. Linvy, DELab: A Simulation Laboratory, Proceedings of the 1987 Winter Simulation Conference, 1987.

[9] P. Merten, R. Loffler and K.P. Wiedmann, Portfolio Simulation: A Tool to Support Strategic Management, System Dynamics Review, Vol. 3, No. 2, 1987.

[10] J.W. Morecroft and K. van der Heijden, Modelling the Oil Producers: Capturing Oil Industry Knowledge in a Behavioural Simulation Model in Modelling for Learning, A Special Issue of The European Journal of Operational Research, 1992.

[11] P. Ninios, K. Vlahos and D.W. Bunn, Industry Simulation: Systems Thinking with an Object Oriented/DEVS

Technology, European Journal of Operational Research, 1994.

[12] R. O'Keefe, Simulation and Expert Systems: A Taxonomy and Some Examples, Simulation, Vol. 46, No. 1, 1986.

[13] W.E. Pracht, Model Visualization: Graphical Support for DSS Problem Structuring and Knowledge Organisation, Decision Support Systems, Vol. 6, No. 1, 1990.

[14] B. Richmond, S. Peterson and C. Charyk, ithink $^{TM}$ Documentation (High Performance Systems, Hanover, NH, 1990).

[15] J. Rosenblit, J. Hu, T.G. Kim and B. Zeigler, Knowledge Based Design and Simulation Environment (KBDSE): Foundation Concepts and Implementation, Journal of Operational Research Society, Vol. 41, No. 6, 1990.

[16] J.D. Sterman, Modelling Managerial Behaviour: Misperceptions of Feedback in a Dynamic Decision Making Experiment, Management Science, Vol. 35, No. 3, 1989.

[17] T. Thomasma and O.M. Ulgen, Hierarchical, Modular Simulation Modelling in Icon-based Simulation Program Generators for Manufacturing, Proceedings of the 1988 Winter Simulation Conference, 1988.

[18] K. Vlahos, P. Ninios and D.W. Bunn, Modelling the UK Electricity Contract Market under the Object Oriented/DEVS Framework, Proceedings of the 6th International Symposium on Applied Stochastic Models and Data Analysis, 1993.

[19] R. Wirfs-Brock, and B. Wilkerson, Object Oriented Design: A responsibility driven approach, OOPSLA '89 Proceedings, 1989.

[20] B.P. Zeigler, Multifaceted Modelling and Discrete Event Simulation (Academic Press, 1984).

[21] B.P. Zeigler, Hierarchical, Modular Discrete-Event Modelling in an Object-Oriented Environment, Simulation, Vol. 49, No. 5, 1987.

[22] B.P. Zeigler, Object Oriented Simulation with Hierarchical Modular Models (Academic Press, 1990).

![](/api/attachments/MQDAXS6J/fulltext/images/130eafe54af4bf3c3876429a48f251177c893c356eb53fb5759b29676c554316.jpg)

Panos Ninios completed his PhD at the London Business School in 1994. Since then he has been working as a Senior Financial Engineer in a financial software firm. His research work has evolved around the strategic modelling and simulation of industries, with particular focus on the UK electricity industry. His general interests include object oriented modelling methodologies, systems modelling and simulation. His publications include

articles in the Journal of the Operational Research Society and the European Journal of Operational Research, as well as a number of simulation conference proceedings.

![](/api/attachments/MQDAXS6J/fulltext/images/a8bb25a4478c6d3c832636c7f106ff3cbfb7a1d504991f59213980c4fd56946b.jpg)

Kiriakos Vlahos (PhD London) is an Assistant Professor of Decision Sciences at the London Business School where he teaches courses on business statistics and decision support. His research work has evolved around the study of the energy sector and its interactions with the economy and the environment. His early research was relying on the use of large scale optimisation models, but he is now investigating the use of more flexible mod-

elling frameworks that allow the integration of hard and soft approaches. He has been a frequent presenter in international conferences of Management Science and has published articles in Fiscal Studies, Energy Economics, the Journal of the Operational Research Society and the European Journal of Operational Research.

![](/api/attachments/MQDAXS6J/fulltext/images/f51d7b18786f25c674a40da5525a71d432556ec9958014ddbce7600a2619930f.jpg)

Derek W. Bunn (MA Cambridge, 1971, MSc London, 1972, PhD London, 1975) is currently Professor and Chairman of the Decision Sciences subject area at the London Business School. He has held previous appointments at the Universities of Oxford, Stanford, Southern California and IIASA. Author of over 100 papers and 6 books in the areas of forecasting, decision analysis and capacity planning. Recipient of research awards from several public and private funds. Editor of the Journal of Forecasting and Associate Editor of Management Science, European Journal of Operational Research and several other journals.
