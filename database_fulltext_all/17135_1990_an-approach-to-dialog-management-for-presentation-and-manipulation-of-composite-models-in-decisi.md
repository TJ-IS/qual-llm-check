---
otero_id: 17135
otero_key: "PGYNJMW8"
title: "An approach to dialog management for presentation and manipulation of composite models in decision support systems"
authors: "James Gerlach; Feng-Yang Kuo"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90016-k"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Approach to Dialog Management for Presentation and Manipulation of Composite Models in Decision Support Systems

James GERLACH and Feng-Yang KUO
Information Systems, Graduate School of Business University of Colorado at Denver, Denver, CO 80204, USA

This paper discusses an object-oriented approach to user interface design that facilitates the exploration of components of a composite-model based DSS. A semantic network of objects is used as the framework to organize the user interface representation. The network is graphically represented and can be directly manipulated by the user. It serves as a framework to assist the user in understanding the conceptual model underlying the DSS. As a result, the network representation should support both fast user learning of the system and easy user control of actions when using the DSS.

Keywords: Decision Support Systems, Model Management, User Interface, Semantic Network

James H. Gerlach is an assistant professor of information systems at the University of Coloroda at Denver. Current teaching and research interests include user interface, object-oriented design, and computer auditing. He received his Ph.D. degree from Purdue University.

Feng-Yang Kuo is an Assistant Professor of Information Systems in the Graduate School of Business, University of Colorado at Denver. He received his Ph.D. degree in management information systems from University of Arizona. His research interests include the design of user-computer interfaces, database management, office automation, and decision support systems.

## Introduction

A decision support system (DSS) includes three functional components: dialog management, model management, and data management [29]. The dialog management component facilitates user-system interactions. The model management component contains models and model relationships to support model integration. The data management component provides access to data that are used as inputs to the DSS for computation or display purpose.

This article discusses a dialog management approach that facilitates the presentation and manipulation of a composite-model based DSS for nontechnical users. A composite model consists of two or more levels of models and/or data that are used to support a complex decision. A composite-model based DSS is normally created by a DSS expert who understands mathematics and computing technology which can be used to support decision making. The DSS expert is needed because the complexity involved in DSS design and implementation can be overwhelming for many users. For example, a study by Brown and Gould [9] shows that even experienced users of spreadsheet packages, commonly used for modeling accounting and financial problems, make programming errors in forty-four percent of cases. The DSS expert analyzes the problem, designs and implements the DSS, and assists the user in evaluating the DSS. This DSS design cycle, described in fig. 1, may be an iterative process.

The particular issue of concern here is the design of the DSS user interface that guides the decision maker and helps him/her explore the levels of models and data that form the composite model. The user typically performs sensitivity analyses on the decision process by experimenting with the different components of the composite model. By selecting among alternative model and data compositions, the user observes the impact of these compositions on the solution. Although the general construct of a composite-model based DSS can be predefined by a DSS expert, the DSS user interface must provide the means by which the user can manipulate individual components.

DSS users, however, are generally not trained in advanced computing technology. Consequently, one may argue that an important design goal should be to simplify the DSS user interface by tailoring it to the particular decision problem faced by the decision maker. The DSS might employ a system-guided dialog style like questions/answers or menu/forms. In these cases, all questions or forms are directed at requesting the input needed by the components of the composite model to solve the specific problem that the system was designed to handle. The DSS becomes extremely easy to use for this particular decision; but there are problems associated with this approach. Mainly, a powerful, intelligent system can cause the user to be a passive observer of system operations, no longer in control of either what operations take place, or how they are done [22].

Conversely, the DSS might employ a programming-language like interface that allows for all possible tasks, from coding model details to integrating models/data to formatting the results of model execution. In this case, the user is forced to learn the technological details involved in operation of that DSS. According to Hutchins et al. [22], systems that are not sufficiently powerful or intelligent can leave too large a gap in the mappings from intention to action execution and from system state to psychological interpretation. The result is that operation and interpretation are complex and difficult, and the user again feels out of control, distanced from the system.

Consequently, both over- and under-automation must be avoided in DSS interface design. At one extreme, an interface such as a general purpose programming language enables the user to program the computer to perform all computable tasks, but every task is extremely difficult for the user. This interface cannot be handled by most of today's business managers. At the other extreme, push-button systems can be developed to handle specific decisions, but too often they eliminate user involvement by trading it off for ease-of-use. These limitations may preclude DSS usefulness since DSS's are supposed to help users solve semi-structured problems. What is needed, therefore, is an interface that employs “representations to assist in conceptualization and to provide a frame of reference for using the DSS” [11, p. 21].

Central to the design of the DSS user interface is the issue of user control. The essence of control is a user frame of reference for conceptualizing the decision task. The user needs to be fully informed of the DSS activities so s/he can evaluate the interface presentations to see if his or her goal is accomplished. If the goal has not been achieved, the interface needs to assist in planning for future actions. In addition, the DSS must be reasonably easy to use. Only then does the DSS become a convivial tool of the decision maker: a tool that reveals its underlying conceptual model and allows for interactions that emphasize comfort, ease and pleasure [22].

![](/api/attachments/PGYNJMW8/fulltext/images/89330993f4aaa258c48442433880ade59228846f86d999d2fd64648a70276acc.jpg)  
Fig. 1. The DSS design cycle.

This means that the DSS user interface design must take into account the psychological and behavioral makeup of its user. Bewley et al. [2], Gaines [18], and Moran [25] suggest that the representation of an interface should closely resemble the user's mental model of the problem-solving task. Because of this resemblance, the decision maker can easily relate the interface representations, i.e., what s/he sees, to what s/he knows and then consider alternative actions to be taken. The three issues: what the user sees, has to know, and can do are emphasized by Bennett [1] in his study of DSS dialogue design.

## User Mental Model of Decision Making

Research has shown that novice users' mental models of a computer system are typically disorganized and they vary across users substantially. In contrast, experienced users' mental models are precise and consistent [12,15,20]. Users can develop a precise and consistent mental model of the system by interacting with the user interface; but user conceptualization based upon disorganized learning sessions often results in fragmented understanding of the underlying conceptual model. The user interface design goal is, therefore, to provide an abstract, coherent conceptual model of the system [19] so that users can learn the model easily and quickly. This design goal is emphasized by Young [30] in his study of mental models of calculators and by Hutchins et al. [22] in his investigation of spreadsheet packages.

The remaining question to be addressed concerns the appropriate way to organize the user interface so the computerized task structure can be learned easily. According to Rasmussen [28], the mental process of a person operating an on-line monitoring system occurs at two levels: bottom-up, data domain processing and top-down, functional domain processing. Data domain processes are typically well-learned rehearsed procedures for handling routine operations associated with well-known objects, such as entry of frequently used data. These operations can be performed almost automatically because examination of data content and contemplation of the functional meaning

```txt
GOAL: CAPITAL BUDGETING- determine which projects to undertake
Goal: determine RESOURCE CONSTRAINTS
Goal: determine CAPITAL CONSTRAINTS
Goal: determine PROJECTS' return and resources needed
Goal: determine NPV of the project
Goal: determine the CASH FLOW of the project
Goal: determine the COST OF CAPITAL (CAPM)
Goal: determine the Km
Choose between DCF-Km and BROKERAGE-Km
[Task: calculate DCF-Km
Task: Select BROKERAGE-Km
among VALUE-LINE-KM,
MERRIL-LYNCH-Km, &
SHEARSON-LEHMAN-Km]
Goal: determine BETA
Choose between HISTORICAL-BETA and
FUNDAMENTAL-BETA
[Task: Derive HISTORICAL-BETA
Select between OWN-BETA and BROKERAGE-BETA
[Task: Calculate OWN-BETA
Task: Select BROKERAGE-BETA
among VALUE-LINE-BETA
MERRIL-LYNCH-BETA,&
SHEARSON-LEHMAN-BETA]
Task: Calculate FUNDAMENTAL-BETA]
Goal: determine Rf
Choose between 15YR-TBOND and 30YR-TBOND
Goal: determine CAPITAL OUTLAY of the project
Goal: determine RESOURCE CONSUMPTION of the project
```

Fig. 2. CAPITAL BUDGETING requires many levels of goals; the lower level goals are achieved by applying some task. The indentation shows the levels of goals that can be formulated by the user. The brackets [] indicate that only one of the tasks specified within the brackets is to be selected.

of the user's actions is unnecessary. For non-routine tasks, functional domain processing relies upon knowledge of the underlying conceptual model to generate plans of action. These plans are based upon predictions of system responses to unfamiliar situations.

The concepts of functional domain and data domain processing are similar to the goal- and event-driven processing proposed by Bobrow and Norman [6]. Bobrow and Norman suggest that functional domain processing is naturally top down, concept driven, and guided by user goals and motives. In contrast, the lower-level data domain processing is event driven. It is totally self contained when performing well-learned tasks. Card, Moran, and Newell [10] in their study of the GOMS (goals, operators, methods, selections) model also propose using a structure based upon hierarchical decomposition for describing experienced user's mental model of a computerized task.

## An Example

Fig. 2 is a partial description of the levels of task to be performed if a person is to choose among many capital investment ventures such as producing widgets, buying out a company, and leasing computing facilities. These choices require four inputs: the set of business projects to be considered, physical plant and material resource constraints, capital constraints, and possible inter-project constraints. For each project, three items of information are needed: the net present value (NPV) of the project's return, capital outlay, and resources needed to carry out the project. With this information available, a linear programming (LP) model can be used to help determine which projects are to be undertaken.

The NPV of a project is determined by the cash flow over the life of the project and by the firm's cost of capital. The NPV model is well studied and widely used, so is the cash flow model [8]. The cost of capital can be calculated by using the capital asset pricing model (CAPM) which requires inputs such as the market return (Km), the risk indicator of the company (Beta), and the risk free rate (Rf). Market return can be derived by using the discount cash flow model (DCF) which requires the dividend (D1), the stock price (Pv), and the growth rate (G) unless market return is provided by a brokerage company like Merrill Lynch and Shearson Lehman.

If a DSS is to be created for the example above, the underlying conceptual model can be described as a set of hierarchically related objects, each of which represents a model (e.g., the DCF model) or a data entity (e.g., Merrill Lynch Km). Furthermore, the decision maker normally experiments with different assumptions underlying various components to better understand possible outcomes of alternative choices of model and/or data. For example, in calculating the cost of capital for each project, different risk free rates based on different economic assumptions can be used. This means that the conceptual model must be extended to include many interrelated test cases that result from sensitivity analyses. Hence, the DSS interface needs to assist the decision maker in not only representing the decision process but also in exploring decision alternatives.

![](/api/attachments/PGYNJMW8/fulltext/images/6f09ad4ffda84546439f2e9cb6806d6c56b845768c5d4daa64bfba91b2ff0872.jpg)  
Fig. 3. The higher-level semantic network for capital budgeting decisions.

## Semantic Network Representation

The present research investigates an object-oriented approach to presenting the conceptual model of a composite-model DSS to its users. In this approach, a semantic network of objects [13], each of which is either a model or a data entity, is used as the primary vehicle of presentation. Figs 3 and 4 depict the semantic networks for the capital budgeting and CAPM models.

A semantic network of objects allows relationships between objects to be classified in one of two ways: IS-A or IS-A-PART-OF. IS-A describes the relationship between a subclass and a superclass; it can also describe the relationship between an object instance and the class to which the instance belongs. IS-A-PART-OF describes the composition of different objects that unite to form an aggregate object.

In the graphic representation used here, a named circle represents either an object instance or a class of objects. A top-down connection between two objects represents a IS-A-PART-OF relationship; the IS-A-PART-OF relationship is used to show input-output interdependence between objects. Horizontal connections linking an object to several other objects are used to depict IS-A relationships. IS-A relationships associate a subclass of objects to a parent class or object instances to an object class. To the decision maker, IS-A relationships are used to group objects into meaningful classes which facilitate data management and specify alternative goals or alternative methods for achieving a goal. IS-A-PART-OF relationships show how a complex decision process is broken down into elementary methods and operations, which, in turn, can be aggregated upwards to attain the indicated goal.

Fig. 3 describes the higher-level network that invokes the CAPM network shown in fig. 4. In fig. 3, the IS-A-PART-OF connections between CAPITAL BUDGETING and RESOURCE CONSTRAINTS, CAPITAL CONSTRAINTS, PROJECTS, and PROJECT CONSTRAINTS specify that these four objects are needed as input to the CAPITAL BUDGETING process. This process, built upon a LP model, would analyze the PROJECTS in relationship to the availability of capital and manufacturing and administrative capacity. The CAPITAL BUDGETING object accepts the inputs from these four objects and transforms them into a LP model which it executes. A feasible set of PROJECTS would be selected that would maximize the net present value of the cash flows they would generate. The output is then properly formatted for user viewing by the CAPITAL BUDGETING object.

![](/api/attachments/PGYNJMW8/fulltext/images/1d6c0417bafeea40391e351756ef0de670bf250cadcb15ceb76a454afdc6a410.jpg)  
Fig. 4. The lower-level semantic network describing the CAPM object used in capital budgeting decisions.

Furthermore, every PROJECT consists of three objects: NPV, CAPITAL OUTLAY and RESOURCE CONSUMPTION. Similarly, NPV is comprised of a CASH FLOW analysis and a cost of capital, CAPM. Project selection may also be constrained by PROJECT CONSTRAINTS: some projects may be mutually exclusive; others may be interdependent, i.e., the selection of one is dependent upon the adoption of another.

Fig. 4 shows by IS-A-PART-OF linkages that three values are required to estimate the cost of a firm's retained earnings using the CAPM model: the Km (market risk premium), BETA (risk indicator), and Rf (risk free rate of return). Since two different computations, HISTORICAL-BETA and FUNDAMENTAL-BETA, can generate BETA, both HISTORICAL-BETA and FUNDAMENTAL-BETA are subclasses of BETA. By the same token, OWN-BETA, calculated by the company's own research, and BROKERAGE-BETA, obtained from brokerage houses, are subclasses of HISTORICAL-BETA. The connections linking these BETAs show IS-A relationships, i.e., alternative ways to generate BETAs.

## Semantic Network Operations

Several operators are needed to facilitate user interaction with the semantic network of models. In the following sections, the operators are discussed and illustrated using as the example DSS based on the capital budgeting model.

## Initial Presentation and Object Selection

The initial presentation at the beginning of user operations is a semantic network of objects (figs. 3 and 4). Each figure represents a separate window; with the window for fig. 3 overlapping the window for fig. 4. This presents fig. 3 in full view to the user. The windows present the entire network in two-layers to the user.

As mentioned previously, this network is a general construct designed by the DSS expert after s/he integrates models and data to form the composite model. It is a network of objects, with each object representing a class or an object instance. Class objects are used to group its members and to create members. Members can be subclasses or object instances. An object instance consists of the actual data elements and the procedures for deriving their values. For example, the class CASH FLOW possesses the ability to generate a CASH FLOW instance. The CASH FLOW instance contains the data and the procedures for performing the actual cash flow computation.

From the network presentation shown in fig. 3, the SELECT operation is used to identify the object the user wishes to manipulate. The SELECT operation is performed by pointing the cursor to the circle representing the desired object, which will be highlighted. Once an object is selected, a pop up menu can be used to list the operations permissible for that object. Operations exist for creating and deleting object and class instances, viewing and modifying the data structure of an object, and tracing the semantic network in order to display those portions of the semantic network the decision maker wishes to evaluate next.

Creating, Manipulating and Deleting Decision Objects

To create an object, the NEW operator is applied to the object class selected. The to-be-created object can be an object instance formed according to the class definition or it can be a subclass of the selected class. If the newly formed object is itself a class then the NEW operator produces a clone of the selected object; if the NEW operator is used to construct an object instance, the instance is created from the class underlying the selected object. The value of the newly-created object instance can be generated as soon as all instances of the constituting objects are generated. As the constituting objects are revised by the user and their values are changed, the higher-level object instances having a IS-A-PART-OF relationship with the modified objects are also changed.

Fig. 5 illustrates the creation of a brand new object. The object is attached to its parent class; it inherits its parent's semantic network. In this manner, the newly created object inherits the parent's underlying decision structure and its parent's processing capabilities. The figure also shows the internal data structure used to store the semantic network. The internal data representation will be discussed in more detail later in this article.

Figs. 6 and 7 show a semantic network that the user could generate from the original network (figs. 3 and 4). Together they show a partial solution to the capital budgeting problem for 1989. Fig. 6 shows three instances of CAPITAL BUDGETING: 1989, 1988, and 1987. The 1989 object is highlighted since it is marked as PRIMARY. The PRIMARY operator enables the user to communicate user selections from a set of choices to the DSS interface. In this case, the user indicates that CAPITAL BUDGETING for 1989 is selected.

The semantic network underlying the 1989 budget is drawn underneath the 1989 object. For 1989, three projects are shown: PRODUCE WIDGETS, BUYOUT COMPANY, LEASE COMPUTER. All three of these objects are marked as PRIMARY since CAPITAL BUDGETING requires not one single primary object but a set of PROJECTS. In this situation the user may select more than one project instance. The semantic network underlying PRODUCE WIDGETS is shown as well. The user operators for controlling which part of the semantic network is displayed are discussed later in this article.

In fig. 7, the decision maker has generated three different cost of capital values by experimenting with different choices for Km, BETA, and Rf. Each value is generated by first applying

![](/api/attachments/PGYNJMW8/fulltext/images/71fc233399186638469d36d1a1f6f0f25f859a4905f146f219ca507170103853.jpg)  
Fig. 5. The user view and underlying internal view of a semantic network.

![](/api/attachments/PGYNJMW8/fulltext/images/22554d76231f339532eebae79610400935e1c4629730dbe3a08b0f50c48b4d9e.jpg)  
Fig. 6. The presentation of the higher-level semantic network with instances after user operations. Dotted circles indicate the PRIMARY objects that are selected.

the NEW operator to CAPM in order to generate an unevaluated instance. Next, the user marks as PRIMARY each IS-A-PART-OF object that is to be used in the calculation. In the calculation shown in fig. 7, the user PRIMARY choices are highlighted. Once all the IS-A-PART-OF objects are selected, the computation is performed.

By repeating this procedure to select different objects as PRIMARY, additional CAPM instances can be generated. Note that even though the value 14.4 is marked as PRIMARY, the other values and their supporting semantic network structures are maintained in case the decision maker wishes to review the computations or to select one of the other two CAPM instances as PRIMARY. Figs. 6 and 7 are interrelated by the CAPM object which appears in both diagrams. Hence the cost of capital value of 14.4 will be used in the assessment of the 1989 project, PRODUCE WIDGETS.

![](/api/attachments/PGYNJMW8/fulltext/images/d7cf7758bc7627f6381149e9d7dfa02d0b06226fba0203bfd63256a18835762c.jpg)  
Fig. 7. The presentation of the lower-level semantic network with instances after user operations. Dotted circles indicate PRIMARY objects selected by the user.

Each object contains local data used to represent the object's natural view, e.g. spreadsheet, graph, or form. This view can be displayed by the user invoking the VIEW operation. In cases where an object can be presented simply as a standard data type such as an integer, real number, or character, the object representation can be shown on the semantic network. Such is the case shown in fig. 7 where the values for various objects are shown next to it.

When presentation of the object is more complex, then the VIEW operation will display a window containing the object in suitable form. Fig. 8 shows the user view of the object CASH FLOW. If the user is permitted to manipulate the object directly, then the VIEW window will provide the user with commands to directly manipulate the object. Hence the CASH FLOW window might provide the user with standard spreadsheet capabilities for modifying the spreadsheet. This capability is referred to as the MODIFY operation.

Object instances are deleted by applying the DELETE operation. When an instance of a higher level is deleted, all its constituting object instances are deleted as well without specific requests for the additional deletions.

## Sensitivity Analysis and User Selections

Many object instances may be generated in a decision-making session, particularly when the user employs a trial and error approach to decision making or when sensitivity analyses are required. Sensitivity analyses are performed by simply experimenting with various objects to generate alternative values. The combination of NEW, VIEW and MODIFY, and PRIMARY operations allows a user to try different ideas for solving a problem. This sequence of events is similar to asking “What If” questions in IFPS. Fig. 7 serves as an example of a sensitivity analysis.

## Navigating Through the Semantic Network

Since the semantic network representing the user decision process can be complex and can grow in size due to sensitivity analyses and trial-and-error generation of objects, operations are needed for exploration of the semantic network.

![](/api/attachments/PGYNJMW8/fulltext/images/bf1fabcbf129338c04371b3181b983a70d1fd1548754c86883151d9f60959d90.jpg)  
Fig. 8. The user view of a CASH FLOW object when this object is activated by the VIEW operation.

Initially, the DSS designer specifies a series of interrelated semantic networks that are used to present the entire network to the user a component at a time. In the capital budgeting example, two interrelated networks (Figs. 6 and 7) are specified. Note that these two networks do not provide a complete interface description. Additional networks are needed for RESOURCE CONSTRAINTS, CAPITAL CONSTRAINTS and PROJECT CONSTRAINTS to complete the interface.

The ZOOM-IN and ZOOM-OUT operations are used to page between these networks. When ZOOM-IN is applied, the DSS interface switches to the window in which the supporting semantic network is displayed. By ZOOMING in on CAPM of fig. 6, fig. 7 is presented to the user. The user can perform standard operations on the CAPM object within this window. The ZOOM-OUT operation is the opposite of the ZOOM-IN operation; it restores the screen to the state prior to activation of the ZOOM-IN operation.

Operations are needed for exploring IS-A linkages in order to control the semantic network presented on the screen. A user can apply the operations to trace or locate any object within the network in one of several ways: left, right, and down.

The $\leftarrow$ (left-arrow) operation and the $\rightarrow$ (right-arrow) operation are used to scroll through instances of a selected object. The $\rightarrow$ is for scrolling right, the $\leftarrow$ for scrolling left. For example, in fig. 6, the user can apply these operators to scroll through PROJECTS instances. This feature is needed since the user will inevitably create more PROJECTS instances than will fit on the screen. The number of instances displayed at any one time is controlled by the interface management software.

On other operation is needed for exploring IS-A-PART-OF linkages. The ↓ (down-arrow) operation locates the objects that are sub-parts of the selected object (disintegration). These operators enable the user to select which object should have its underlying semantic network presented. For example, in fig. 7, by applying the ↓ operator to object 14.4, the objects Km, BETA, and Rf along with their associated semantic networks are displayed. If the user was to apply ↓ operation to CAPM instance 14.175, then fig. 7 would be drawn to show 14.175's supporting network instead.

In summary, the $\leftarrow$ , $\rightarrow$ , and $\downarrow$ operators enable the user to precisely control what part of the semantic network is displayed. The ZOOM-IN and ZOOM-OUT operations allow the user to page back and forth between interrelated semantic networks.

## Copying Objects

There are situations where it is useful for the user to be able to copy part of one decision process to another. For example, the CASH FLOW object for evaluating PRODUCE WIDGETS might use a spreadsheet that is similar in structure to one used to evaluate a 1988 project, produce desks. Hence the user would want to copy the CASH FLOW for 1988 produce desks to CASH FLOW for 1989 PRODUCE WIDGETS. After the copy, the user could revise the spreadsheet calculation for producing desks to generate the proper calculation for producing widgets.

A second situation is seen in the CAPM calculation for 1989 (fig. 7). Assuming that the user applies a single cost of capital value to all 1989 PROJECTS, the user would like to share this calculation with all 1989 PROJECTS but not with 1988 and 1987 PROJECTS. However, the hierarchical decomposition shown in figs. 6 and 7 makes this impossible unless a many-to-many relationship is created between PROJECTS and CAPM. Instead, the user can simply copy the CAPM calculation to all 1989 PROJECTS instead.

By adding the COPY operation to the set of user functions, the user is able to reuse previous decision analyses in ways the DSS designer could not have presumed. The DSS interface imposes the restriction that only objects of the same type can be copied from one to another.

## Support for Functional and Data Domain Processing

The semantic network of objects used in a decision task is a coherent framework which allows the user to understand the conceptual model underlying the DSS. The root object of the network represents a composite model to be used for problems from a general decision class; instances of the root object represent specific decision problems. The levels of objects show the relationships among steps of the task that need to be performed if a user is to reach a decision. Hence, levels of objects can be regarded as levels of goals and subgoals that the user follows in order to make a decision. Horizontal linkages depict choices from which the decision maker may choose. These choices may be specified in advance by the DSS designer; they may also be generated by the decision-maker as s/he experiments with alternative model/data compositions. Hence, the semantic network representation assists the user in functional domain processing.

Furthermore, the semantic network provides the foundation for a direct manipulation user interface. The fact that essentially all objects share a single set of interface operations results in a consistent, well-learned set of basic operations which a user can use to manipulate any object. Hence, bottom-up, data domain processing, can be easily performed; and because any object can be operated on at any time at the discretion of the user, decision tasks can be performed in either a predetermined or an ad-hoc manner.

## Support for Object Specific Representations

Semantic network representation, like those shown in figs. 6 and 7, is only one aspect of the overall user interface; it shows the relationships of objects, i.e., models/data, required in a decision. In addition, each object of the network has its own specific representation which matches the user mental model corresponding to the task. For example in fig. 8, the cash flow model of the capital investment DSS is considered to be one “chunk” of the user interface; its representation is the row-column format of a spreadsheet. In a similar fashion, graphics can represent either discrete or continuous variables. Consequently, the “natural user interface” such as spreadsheet or graph for a given task is preserved. In contrast, formulas are depicted with a semantic network that highlights the input-output objects associated with a specific calculation. This format allows the decision maker to focus on the objects needed in a computation even if s/he has not understood the mathematics involved in deriving the answer.

In short, the decision model is decomposed into "chunks" (objects) which reveal its processing structure. The granularity of chunking is determinated by the DSS designer who studies the user's decision making behavior and preferences.

## Support for User Control

The extent of a user's sense of control is directly related to how effectively the user can identify and evaluate the physical states of the system [22]. In the network representation, the structure of goals-methods is explicitly presented; it allows the user to relate goals and intentions to the user interface. Each object represented in the semantic network provides a “natural” view by which the user can view the effects of each step of his/her decision process; by interrelating the goal structure to objects, an integrated decision framework is provided. This permits each intermediate step to be observed immediately and it can be interrelated to the overall goal structure. Thus, user control can be facilitated effectively.

The graphic network representations shown in figs. 3, 4, 7 and 8 obey the principle of “what you see is what you get” [24]. The semantic network even goes a step further by synchronizing the representations of user knowledge with DSS dialog.

## Dialog Management Software Architecture

The interface manager's main purpose is to provide DSS users with the ability to identify and manipulate decision models needed for decision support quickly. For DSS developers, it represents a highly-efficient interface development tool.

The architecture of the dialog management software which supports the object-oriented approach described in this paper is shown in fig. 9. It relies on an existing object-oriented environment, such as SMALLTALK, which can interface with external programs. The ability to interface with external programs is needed in order to take advantage of available data base management systems (DBMS) and DSS models. The object manager supports object specification and execution. The interface manager interacts with the object manager by translating user actions into messages (i.e., object calls) instructing the objects to carry out the user intentions. The object manager is provided by the object-oriented environment; the interface manager must be implemented within the same environment. The DSS expert defines all object classes needed for decision support and semantic network templates which are input to the interface manager to construct the user interface.

![](/api/attachments/PGYNJMW8/fulltext/images/b1fafe92638d711a0744745663589d5015cf1a08305efa2251bf291189747687.jpg)  
Fig. 9. The dialog management architecture for supporting the semantic network presentation and manipulation.

## Semantic Network Template

To describe the semantic network interface the DSS designer completes a template that describes the initial IS-A and IS-A-PART-OF relationships among objects. This semantic network template is referred to as the S-N template.

The semantic network description is specified in Backus-Naur form (BNF). The two principal operators used (1) the | operator which describes the IS-A relationships among a superclass and its classes and (2) the + operator which describes the

IS-A-PART-OF relationship among an aggregate object and its constituting objects. Objects which may be repeated one or more times are denoted by enclosing it in { }'s in the BNF description. A bracketed object denotes that one or more object instances may be denoted as PRIMARY by the decision maker.

Fig. 10 describes the S-N templates for the DSS shown in figs. 3 and 4. One S-N template is needed for each interrelated semantic network. Additional templates are needed for RESOURCE CONSTRAINTS, CAPITAL CONSTRAINTS, and PROJECT CONSTRAINTS to complete the DSS example.

Note that the S-N template merely describes IS-A and IS-A-PART-OF relationships. It is not a substitute for the mathematical formula that describes the production of the object on the left side of the rule from the objects on the right side. For example, the rule for DCF-Km specifies that three objects are needed: D1, the dividend; Pv, the current market value; and G, the growth rate. The interface manager assumes that D1, Pv and G are the names of object classes which the DSS designer has constructed.

```txt
The S-N template for the higher-level semantic network for CAPITAL BUDGETING:

CAPITAL-BUDGETING <- RESOURCE-CONSTRAINTS +
    CAPITAL-CONSTRAINTS +
    PROJECTS +
    PROJECT-CONSTRAINTS
PROJECTS <- NPV + CAPITAL-OUTLAY + RESOURCE-CONSUMPTION
NPV <- CASH-FLOW + CAPM

The S-N template for the lower-level semantic network for CAPM.

CAPM <- Km + BETA +Rf
Km <- DCF-Km | BROKERAGE-Km
BETA <- HISTORICAL-BETA |
FUNDAMENTAL-BETA
Rf <- 15YR-TBOND | 30YR-TBOND
DCF-Km <- D1 + Pv + G
BROKERAGE-Km <- VALUE-LINE-Km |
MERRIL-LYNCH-Km |
SHEARSON-LEHMAN-Km
HISTORICAL-BETA <- OWN-BETA |
BROKERAGE-BETA
BROKERAGE-BETA <- VALUE-LINE-BETA |
MERRIL-LYNCH-BETA |
SHEARSON-LEHMAN-BETA
```  
Fig. 10. The S-N templates.

## Interface Manager Functions

The user-interface manager is responsible for creating the initial execution network of objects underlying the user presentation. The decision maker communicates his/her intentions to the interface manager by manipulating the semantic network presentation directly as described previously in this paper. The interface manager then translates these user actions into their corresponding messages which are sent to the objects underlying the semantic network presentation. There, within the object, the computation takes place.

For each object specified in the S-N template, there must exist a class definition in the class hierarchy. Each class contains a data structure for managing its member instances and methods for creating new object instances. When an object is created, the newly formed object instance is constructed from its class which describes its data structure and methods for operating on the data.

The data structure of an object includes not only the data needed to represent its internal function, but also basic object attributes such as name, pointers to the object's superclass, sibling, parent, and children objects. The attribute PRIMARY is used to indicate the currently selected object. These additional data items are needed to support the interface manager functions.

The data structure physically links each class with its member object instances or with its member subclass instances as illustrated by fig. 6. The linkages connecting an object to each other object that supplies it with an input value form an execution network. These input-output linkages determine the precedence of operations used to compute the value of an aggregate object.

There are four object-specific methods that must be created by the DSS expert for each object: EXECUTE, GIVE-RESULT, VIEW and NEW. Upon activation of EXECUTE, the method performs the appropriate action underlying an object, such as performing a calculation or a data base operation. When an object instance is instructed to EXECUTE, it sends the GIVE-RESULT message to each of its immediate IS-A-PART-OF objects. This instructs the object to return its current value to the object that sends the message. Since only an object instance contains the requested data, if the receiver of the message is a class, the class forwards the message to each of its subclasses or object instances; if they are subclasses, they also forward the message. Eventually the message is forwarded to an object instance, which then evaluates the PRIMARY attribute and returns the requested results if the attribute is positively marked. The results are then pooled and passed backward to the object instance which initiated the original message.

The operation VIEW is needed to present the data representing the object to the decision maker. If the object instance does not include a VIEW method, the interface manager assumes that the object has an elementary data representation which can be displayed with the semantic network. Finally, the method NEW must be specified for each class in order to create an initialized object instance belonging to that class.

In addition to the four methods that are object specific, there are a number of common messages that each object must respond to in order to construct and maintain the execution network. Because all classes and object instances must respond to these same messages in the same way, these methods are inherited by each object. These methods constitute a major portion of the interface manager and, though they become part of the object, they need not be specified by the DSS developer. Most of the methods are used to maintain the various internal pointers needed for interrelating objects illustrated in fig. 5. Other methods are for creating subclasses and specifying which object instance of a class is considered PRIMARY.

## Error Handling

One important consideration in design of DSS user interfaces is feedback for erroneous user actions. The importance of error handling is highlighted by Hiltz and Kerr [21] who show that the trial and error method is the most widely used learning strategy employed as users learn a new system. Norman [27] identifies several sources of user errors that are particularly relevant to the approach discussed in this paper: mode error, description error and unintentional activation error.

The semantic network interface presented here eliminates mode error by employing a modeless interface design. Description error, caused by the correct action on a wrong item, is handled by the interface by showing the result of user operations to the user immediately. In addition, an UNDO operator allows the user to recover unintended operations. Unintentional activation error, caused by inconsistent command structure, is reduced because the system internal representation and user interface presentation are synchronized and the network driven interface guides user actions.

## Summary and Conclusions

In this paper an approach to dialog management for model identification and integration is described. An example DSS for capital budgeting is used to illustrate the approach.

Because in practice, a decision maker normally relies on a limited number of models for decision support, the approach described here is useful for constructing the user interface of a personalized DSS. When a larger number of models are required, additional levels of classifications that use IS-A and IS-A-PART-OF relationships can be applied to provide expanded model access.

A semantic network of models can serve as the user-interface metaphor to guide user action. The representation outlines each step of the decision process by reference of hierarchical decomposition. Higher-level goals are recursively decomposed into lower-level goals for which there are procedures to satisfy the goal structure. The representation is sufficiently expressive to suggest user alternatives for achieving higher-level goals: the user explores alternatives by directly manipulating the semantic network representation. As a non-procedural description of the decision process, the semantic network representation serves a blue print for guiding the decision maker's thought processes. As results are generated by executing the decision models, they are associated with the semantic network representation for quick and easy access by the decision maker. The network provides an efficient way for DSS users to browse through and to interrelate objects as they search for feasible solutions to the semi-structured problem.

This decision process representation is also useful in assisting users to understand their problem and in planning a solution strategy. With the semantic network representation, decision makers can understand what objects are needed for each decision step even when they have not mastered the mathematics involved in deriving the formulas. The network representation allows DSS users to experiment with any object within the network, without following a strict sequence. The interface automatically assist users in managing their decision space by relating results of analyses to the decision process that generates them. All of these help support functional domain processing.

Data domain processing support is achieved through a set of consistent and simple operations. Simplicity of operation is essential if the cognitive efforts of the decision maker are to be focused on problem application and solution rather than on figuring out how to instruct the system to do what s/he wants done.

The semantic network representation satisfies Bennett's[1] interface guidelines for DSS's: it guides user actions by showing which actions are possible, which steps have been completed, and which remain to be solved.

Finally, the interface representation can be applied broadly to design user interfaces for DSS based on composite quantitative models. The semantic network representation enables each object to have its own specific representation such as spreadsheet, graph, and tabulation. The representation chosen can be task specific, naturally consistent with the task at hand, and consistent with the user's mental model of the task. Also, the network representation can be interpreted as an AND/OR tree with horizontal linkages describing OR conditions and the vertical linkages describing AND conditions. This logic construct is powerful for describing quantitative models that can be hierarchically constructed using the output of other models; the relationships among these models can be described using the IS-A-PART-OF relationship. Variations of models used for the same purpose can be described easily by using the IS-A relationship.

## Future Research

Although the network representation fosters user experimentation, it is incomplete in terms of knowledge encoded and presented. Some procedural knowledge, such as heuristics for model selection based on problem characteristics, cannot be represented in a semantic network easily and it leaves selection of the appropriate object to the user. When compared with production-rule based expert systems, these are a weakness of the current semantic network approach. However, suggested intelligent assistance can be provided if knowledge of selection criteria can be embedded in object specifications. Future research in this area is needed.

A second important research need concerns mechanical/automatic model integration. The semantic network approach to interface development presented here might be incorporated with several model integration approaches, such as the frame-based integration $[3,14]$ , logic programming $[5,7,23]$ , the network approach $[16,17]$ , and the rule-based approach $[26]$ . The S-N templates and object definitions needed for a DSS could be automatically generated as a by-product of the model integration process. Currently, research is being directed at studying this automatic generation the DSS user interface.

## References

[1] Bennett, J.L., Analysis and Design of the User Interface for Decision Support Systems, in: J. Bennett, ed., Building Decision Support Systems, Addison-Wesley, Reading, MA, 1983, pp. 41–64.

[2] Bewley, W., T. Roberts, D. Schroit and W. Verplank, Human Factors Testing in the Design of Xerox's 8010 STAR Workstation, CHI'83, 1983, pp. 72–77.

[3] Binbasioglu, R.W. and M. Jarke, Domain-Specific DSS Tools for Knowledge-based Model Building, Proceedings of HICCS'86 1A, 1986, pp. 503–514.

[4] Blanning, R.W., Conversing with Management Information Systems in Natural Language, Communications of the ACM 27, No. 3, 1984, pp. 201–207.

[5] Blanning, R.W., A PROLOG-based Framework for Model Management, Proceedings of the First International Workshop on Expert Systems 2, 1984, pp. 633–642.

[6] Bobrow, D.G. and D.A. Norman, Some Principles of Memory Schemata, in: D.G. Bobrow and A. Collins, eds., Representation and Understanding, New York, Academic Press, 1975.

[7] Bonczek, R.A., C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York, 1981.

[8] Brigham, E.F. and L.C. Gapenski, Intermediate Financial Management, The Dryden Press, Chicago, IL, 1984.

[9] Brown, P.S. and J.D. Gould, An Experimental Study of People Creating Spreadsheets, ACM Trans. Office Information Systems 5, No. 3, July 1987, pp. 258–272.

[10] Card, S., T. Moran and A. Newell, The Psychology of Human-Computer Interaction, Lawrence Erlbaum Associates, Hillsdale, NJ, 1983.

[11] Carlson, E.D., An Approach for Designing Decision Systems, in: J. Bennett, ed., Building Decision Support Systems, Addison-Wesley, Reading, MA 1983, pp. 15–40.

[12] Carroll, J. and J. Thomas, Metaphor and the cognitive representation of computing systems, IEEE Transactions on Systems, Man, and Cybernetics 12, 1982, pp. 107–116.

[13] Collins, A.M. and M.R. Quillian, Retrieval Time from Semantic Memory, Journal of Verbal Learning and Verbal Behavior 8, 1969, pp. 204–247.

[14] Dolk, D.R. and B. Konsynski, Knowledge Representation for Model Management Systems, IEEE Transactions on Software Engineering SE-10, No. 6, 1984, pp. 619–628.

[15] Douglas, S.A. and T.P. Moran, Learning Text Editor Semantics by Analogy, CHI'83 Proceedings, Dec. 1983, pp. 207–211.

[16] Elam, J.J., J.C. Henderson and L. Miller, Model Management Systems: An approach to Decision Support in Complex Organizations, Proceedings of ICIS'80, 1980.

[17] Evans, J.R. and J.D. Camm, Structuring the Modeling Process for Linear Programming, Proceedings of DSI'87, 1987, pp. 957–959.

[18] Gaines, B., The technology of interaction-dialogue programming rules, Int. J. Man–Machine Studies 14, 1981, pp. 133–150.

[19] Halasz, F. and T. Moran, Analogy Considered Harmful, Proceedings of CHI'81, 1981, pp. 383–386.

[20] Halasz, F.G. and T.P. Moran, Mental models and problem solving in using a calculator, CHI'83 Proceedings, Dec. 1983, pp. 212–216.

[21] Hiltz, S.R. and E.B. Kerr, Learning Modes and Subsequent Use of Computer-Mediated Communication Systems, CHI'86, pp. 149–155.

[22] Hutchins, E.L., J.D. Hollan and D.A. Norman, Direct Manipulation Interfaces, in: D.A. Norman and S.W. Draper, eds., User Centered System Design, Hillsdale, NJ, Lawrence Erlbaum Associates, 1986, pp. 87–124.

[23] Lee, R.M. and L.W. Miller, A Logic Programming Framework for Planning and Simulation, Decision Support Systems 2, No. 1, 1986, pp. 619–628.

[24] Lipkie, D., STAR Graphics: An Object-Oriented Implementation, Computer Graphics 16, No. 3, 1982, pp. 115–123.

[25] Moran, T., The command language grammar: A representation for the user interface of interactive compute systems, Int. J. Man–Machine Studies 15, 1981, pp. 3–50.

[26] Murphy, F.H. and E.A. Stohr, An Intelligent System for Formulating Linear Programs, Decision Support Systems 2, No. 1, 1986, pp. 39–47.

[27] Norman, D., Design, Rules based on Analysis of Human Errors, Communications of the ACM 26, No. 4, 1983, pp. 254–258.

[28] Rasmussen, J., The Human as a System Component, in: Human Interaction with Computers, London, Academic Press, 1980.

[29] Sprague, R. and E.D. Carlson, Building Effective Decision Support Systems, Englewood Cliffs, NJ, Prentice-Hall, Inc., 1982.

[30] Young, R.M., The Machine inside the Machine: User's Models of Pocket Calculations, Int. J. Man–Machine Studies 15, 1981, pp. 51–85.
