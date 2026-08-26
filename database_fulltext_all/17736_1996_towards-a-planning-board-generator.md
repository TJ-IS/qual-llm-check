---
otero_id: 17736
otero_key: "HJBGC59D"
title: "Towards a planning board generator"
authors: "Marc Wennink; Martin Savelsbergh"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00032-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards a planning board generator

Marc Wennink $^{a,*}$ , Martin Savelsbergh $^{b}$

$^{a}$ Department of Mathematics and Computing Science, Eindhoven University of Technology, P.O. Box 513, 5600 MB Eindhoven, The Netherlands

$^{b}$ School of Industrial and Systems Engineering, Georgia Institute of Technology, Atlanta, GA 30332-020, USA

## Abstract

A planning board is a planning tool that uses the Gantt chart as its main representation mechanism. A planning board generator aims at facilitating the development of planning boards; using a specification of the problem type for which a planning board is to be developed and the desired representations and manipulations, the generator automatically creates a prototype of the planning board. In this paper we discuss our view of a planning board generator and introduce a method to specify problem instances and types.

Keywords: Planning board; Planning board generator; Planning problems; Problem specification; Gantt chart

## 1. Introduction

A planning board is a planning tool that uses a Gantt chart to represent a plan and provides the means to modify the plan by modifying the Gantt chart. A planning board is a useful tool in many problem situations. Unfortunately, developing an automated planning board requires a lot of time and energy. In addition, all problem situations have their own characteristics and require their own specific planning board.

Our goal is to identify common properties of problem situations for which a planning board is useful and to use these properties to develop a planning board generator. Given a specification of the problem situation for which a planning board has to be developed and a description of the desired representations and manipulations, the generator should automatically create an initial version of the planning board.

The purpose of this paper is twofold. First, we will elaborate on our view of a planning board generator. For a given problem type, the planning board generator must be able to generate a planning board that is equipped to deal with the specific characteristics of that problem type. Therefore it is essential that these characteristics can be specified accurately. The second purpose of this paper is to present methods for problem specification.

In Section 2, we discuss our view on planning boards and the planning board generator in more detail. In Section 3, we will introduce a method to specify instances of planning problems. This method serves as a basis for our specification method for problem types, which will be presented in Section 4. Finally, in Section 5, we will discuss some further research topics that must be dealt with in the development of a planning board generator.

![](/api/attachments/HJBGC59D/fulltext/images/a4f43a5f15698aff4ac7dc4b7d2dc51ddb1700dc7545d109e30a44f2aeabc014.jpg)  
Fig. 1. A Gantt chart.

## 2. The planning board generator

## 2.1. Planning boards

An essential element in a planning board is the Gantt chart. An example of a Gantt chart is given in Fig. 1.

This Gantt chart represents the program of a music festival. Sixteen artists and bands have been contracted by the organization, each of which will be performing on one of the four stages during a given time interval. For example, Tom Waits will perform on stage B from seven thirty until nine o'clock.

In general, the horizontal axis in a Gantt chart represents some time period. On the vertical axis, resources are set out, and the rectangles on the chart represent processes. In Fig. 1, the resources are the stages, and the processes are the performances of the artists. In other applications, the resources may be lecture rooms, machines, or vehicles, and processes may be courses that must be given, operations that must be performed, or goods that must be transported. The Gantt chart as a whole represents a plan, i.e., an assignment of processes to resources and time intervals.

In this paper, we deal with planning problems. In these problems, we are given a set of processes, a set of resources, and a set of constraints. The processes must be assigned to the resources and time intervals in such a way that all constraints are satisfied. Planning problems arise in course scheduling, timetabling, production planning, vehicle dispatching, and many other application areas. In all these areas, planning boards are used to support the planner.

Planning boards can play a vital role in complex planning situations by integrating human insight and formal models (Anthonisse et al. [2]). For example, when the quality of a plan has to be assessed, mathematical models can be used to test if all constraints are satisfied or to evaluate some criterion function, and the planner will use his own experience and knowledge of the problem situation to decide whether the plan as a whole is feasible.

Good representations of both the problem and the plan are crucial in order to get the highest benefit from this interaction. Although the Gantt chart is the primary representation in a planning board, other representations, such as data tables and inventory graphs, can also be incorporated. Using various representations of problem data and plans may lead to a better understanding of the problem being solved. Jones [13] discusses the importance of representation and visualization in the context of optimization. In two wonderful books, Tufte [15,16] treats the more general subject of envisioning information.

A planning board should also provide the means to manipulate the presented representations, so as to enable the planner to create and modify plans. The notion of manipulation should be interpreted broadly. In the terminology introduced by Anthonisse et al. [2] with respect to interactive planning systems, manipulations cover the entire spectrum from assistant functions to advisor functions. A planning board must provide the means to store and retrieve plans, to evaluate the quality of a plan, and to modify a given plan manually. On the other hand, the planning board must also be able to construct a plan by itself and to give suggestions for improving a given plan.

A planning board is generally used for more than one particular problem situation. Each such situation will be called a problem instance. A set of problem instances with well-specified common characteristics will be called a problem type. A planning board should be equipped to deal with all possible instances of some problem type. Consider, for example, the problem of assigning nurses to night shifts and day shifts in a hospital. Such a timetabling problem must be solved, say, every month. However, the number of available nurses and their desires with respect to vacation and days off are subject to change. Thus, every month a different instance of the nurse scheduling problem type must be solved, and a planning board must be capable to deal with each possible instance.

The combination of representations and manipulations results in a powerful tool for many different types of planning situations. Each problem type, however, requires its own sets of representations and manipulations. A single Gantt chart will suffice for certain machine scheduling problems, but in more complex production planning problems also inventory graphs are required. Similarly, the quality of a course schedule and the quality of a production plan are evaluated in completely different ways. One can say that each problem type requires its own planning board. Unfortunately, the development of an automated planning board is a highly time consuming process. The aim of our research has been to find out in what way the design of planning boards can be facilitated.

## 2.2. The planning board generator

The ultimate goal of this research is the development of a planning board generator (PBG). Given a specification of the problem type for which a planning board has to be developed and a specification of the desired representations and manipulations, a PBG should automatically create an initial version of the planning board. The context in which a PBG would be used is depicted in Fig. 2.

A planner has to make plans for a number of instances of the same problem type and he thinks that a planning board may be a helpful tool. He therefore asks a planning board designer to build a planning board for that specific problem type. The designer asks for the characteristics of the problem type, the desired representations, and the required manipulations. The designer activates the planning board generator to process this information and to produce an initial version of the planning board.

![](/api/attachments/HJBGC59D/fulltext/images/11acdffa90d6a1fabad1f00b0db31d0aac9c1215895be508db9fa23911190d99.jpg)  
Fig. 2. Context of a planning board generator.

A PBG must be capable of generating planning boards for a broad variety of problem types, including timetabling, course scheduling, and production scheduling problems. At first sight, these problem types have only little in common, but on closer examination we find several common aspects, both in the structure of the problems and in the way that planning boards can be used in solving these problems. Planning boards for these problem types provide the same kinds of representations and allow for the same kinds of manipulations to be performed. It seems a waste of time and energy to implement these common elements for each individual planning board from scratch.

Any automated planning board contains a number of procedures to support various representations and manipulations. Although the functionality of these procedures is almost the same for all planning boards, the actual implementation must be tailored to the specific problem situation for which a planning board is to be designed.

Consider, for example, the procedure for drawing Gantt charts. In a Gantt chart, resources are represented on the vertical axis, the horizontal axis represents some time interval, and rectangles represent processes that are assigned to resources and time intervals. These properties hold for all planning problems. Consider now a particular problem type in which two kinds of resources, machines and employees, appear, time is measured in hours, with ten hours in a day and 5 days in a week, and processes are divided into groups. In a planning board for this problem type, the two kinds of resources, machines and employees, appear separately on the vertical axis of the Gantt chart, the appropriate time system is set out on the horizontal axis, and processes that belong to the same group are represented by rectangles of identical color.

Another example is the “move” manipulation, which enables a planner to determine a new assignment for some process. In all situations, and for all planning problems, the planner must specify which process is to be moved and where it is to be positioned, and it must be checked if the new assignment is feasible. Consider a specific problem type, in which each process must be assigned to a combination of a machine and an employee, and certain precedence constraints must be satisfied. A planning board for this particular problem type will offer the possibility to specify the process that is to be moved, then ask to which machine-employee-combination it is to be assigned and at what time the process must be started. It checks whether the proposed assignment is feasible, the capacity limitations of the resources are not violated, and the precedence constraints are satisfied.

For each of the various representations and manipulations that may be used in planning boards, a PBG will contain a basic implementation. On the basis of the specification of the problem type and the desired representations and manipulations, the PBG will tailor these basic implementations to provide customized implementations that are appropriate for the considered problem type and that match the expressed desires as closely as possible. This tailoring may be as simple as setting certain parameter values and incorporating predefined subroutines in the basic implementations, but it may also involve generating pieces of new code.

Two conflicting objectives arise when the functionality of a planning board generator is discussed. On the one hand, a PBG should be as general as possible, supporting a broad variety of planning problem types; on the other hand, for a given problem type it should be able to generate a powerful planning board that is equipped to deal with the specific characteristics of that problem type in an efficient way. For a PBG to be of any use it is essential that the right balance between generality and efficiency is found.

There are two possible approaches in trying to obtain such a balance. In a “top-down” approach, generally applicable methods are developed, which may be adjusted to specific situations. In a “bottom-up” approach, one develops efficient, problem-specific methods and tries to adjust these in order to deal with more general problem situations. The first approach leads to a guaranteed level of generality, possibly at the cost of efficiency. The main objective in the second approach is efficiency; if the desired level of efficiency cannot be maintained, then no further generalization is pursued.

We think that generality can be achieved for many aspects of a PBG without loss of efficiency, and the top-down approach seems most natural for these aspects. A general problem class will be identified, and methods will be developed that can handle all problems in this class. For aspects of a PBG in which it is not obvious how we can obtain generality while maintaining the desired level of efficiency, we must rely on a bottom-up approach. Ideally, this approach will result in sufficient generality, but we must take into consideration the possibility that methods will be developed that are only suited for specific subclasses of the general problem class. For each such subclass, a library of methods can be created. These methods must be reasonably efficient for all problem types in the considered class.

## 2.3. Related research

The role of decision support systems and, more specifically, graphical interfaces in solving planning problems has been widely discussed in the literature (see, e.g., Anthonisse et al. [2], Fisher [5], Hurrion [8], and Jones [12]). Furthermore, planning boards have been developed for a wide range of problem situations including course scheduling, ship scheduling, timetabling, job-shop scheduling, and production scheduling (e.g., Fisher et al. [6], Moreira and Oliveira [14], and Viviers [17]). In most cases these planning boards are equipped to handle a small and well-specified class of problem instances.

More relevant and more closely related to our research are systems that have been developed in order to deal with a broader class of planning situations and offer wider possibilities for problem specification. Examples of such systems are the systems developed by Jackson et al. [9], Jones and Maxwell [10], and Woerlee [19]. These systems differ from our PBG in that they are developed for a particular application area; material logistics, manufacturing scheduling, and production scheduling respectively. With our PBG, we do not restrict ourselves to a particular application area, but we focus on the underlying general problem structure: processes must be assigned to resources over time. This general structure allows the use of the same representation mechanism (e.g., Gantt charts) and similar manipulations for problems in completely different application areas. We think that this general problem structure can be exploited effectively to facilitate the development and implementation of planning boards for all these application areas.

Although it is not concerned with planning tools that use the Gantt chart as main representation mechanism, the graph-based modeling system (GBMS) of Jones [11] is conceptually very similar to our PBG. Both the GBMS and the PBG aim at facilitating the development of user interfaces for interactive systems. In a GBMS, attributed graphs are used as representation mechanism. The created interface is called an instance editor. An instance editor enables a modeler to add and delete nodes and edges in order to construct a graph of the appropriate type. In a GBMS, the designer specifies a graph type and the manipulations that can be performed on graphs of that type. This specification is sufficient to automatically generate an instance editor for graphs of that type. Using a similar terminology, one can say that a planning board enables a planner to perform manipulations on (representations of) plans in order to construct a solution to a problem of the appropriate type. In our setting, the designer specifies a problem type and the desired representations and manipulations. From this specification, the PBG automatically constructs a planning board for instances of this type.

An important difference between a GBMS and a PBG is the representation mechanism that is used, attributed graphs versus Gantt charts. Another important difference relates to the way in which a graph type or problem type and the corresponding sets of manipulations are specified. Jones's GBMS allows the designer to create his own types of nodes and edges, each with its own set of attributes, and also the manipulations can be developed by the designer. For our PBG we apply a different approach. There exists a general problem class, of which all problem types that the PBG can handle are special cases. The designer of a planning board can describe his particular problem type by specifying the appropriate subclass of the general problem class. Similarly, a set of possible manipulations is given, from which a planning board designer chooses a subset.

The advantage of our approach is that the implementation of the PBG can be specifically equipped to deal with planning problems only, thus yielding a more effective and efficient system. The specification methods that will be presented in Sections 3 and 4 form an illustration of this advantage. These methods exploit the common structural properties of planning problems and enable us to focus on the distinguishing characteristics of problem types. A disadvantage of our approach is that the number of manipulations and representations that can be supported is finite. However, we think that a relatively small number of predefined representations and manipulations will suffice in the design of powerful planning boards for a wide range of planning problems.

An important part of this paper is concerned with specification methods for problem instances and problem types. Therefore, it is interesting to compare its capabilities with those of existing classification schemes, for example for machine scheduling problems (e.g., Conway et al. [4], and Graham et al. [7]). These classification schemes typically use a fixed number of parameters, each describing a particular problem characteristic. Since such a parameter can only specify a characteristic of all the instances of the problem type, these classification schemes do not offer the flexibility that we need in a specification method that is to be used in a PBG that can handle a wide range of application areas. Consider a problem type in which there are two kinds of processes, the first kind possessing deadlines but no release times, the second kind possessing release times but no deadlines. The existing classification schemes only allow us to specify that all processes may possess release times and deadlines. The specification methods presented in this paper do offer the possibility to describe such a problem type correctly. It is worth noting that the translation of a problem type specification in terms of one of the existing classification schemes into a specification using our method can usually be done quite easily.

## 3. Problem instances

As has been discussed in Section 2.2, a precise specification of the problem type for which a planning board should be generated is essential. It is especially important that the designer can specify those characteristics of a problem type that affect the implementation of the representations and manipulations. In this section, we discuss how problem instances can be specified. In Section 4, we show that the proposed method can serve as a basis for a specification method for problem types.

## 3.1. An overview of the specification method

The instance specification method has been developed with the following objectives in mind:

1. It should be possible to specify instances of all problems for which we feel that a planning board provides a useful tool. In fact, the method will implicitly define a general problem class. Note that this class should be fairly large for a PBG to be of any interest.

2. The instance specification method must form the basis of a type specification method. It should, therefore, be possible to specify subclasses of the general problem class by identifying the typical properties of problem instances within such subclasses.

3. It should be possible to use the specification of an instance to efficiently perform some of the tasks of a planning board, such as verifying feasibility of assignments and providing information on various aspects of a plan.

In the specification of problem instances we can use the general problem structure as a starting point: processes must be assigned to resources and time intervals in such a way that certain constraints are satisfied. A problem instance can thus be described by specifying the processes and resources and their properties, the time system, and the constraints that must be satisfied. In the proposed specification method, we make use of attributed graphs. Processes and resources are represented by nodes and their properties by attributes. Examples of attributes are the size of a process, and the capacity of a resource. Various edges, arcs, and auxiliary nodes are introduced to describe relations between objects. In this way, we are able to formulate to which resources we can assign a process and which constraints must be satisfied.

The attributed graph associated with an instance will be called an instance graph. The core structure of the instance graph describes the feasible assignments of processes to resources. Each process and each resource are represented by a node. For each possible choice of resources and each possible combination of resources an auxiliary node is introduced that is connected to the objects involved and, thus, forms a $K_{1,n}$ , where n is the number of objects involved.

Several other relations between objects can be described by graph constructs as well. Binary relations, i.e., relations involving exactly two objects, can be modeled by an edge or an arc. For example a precedence relation indicating that one process has to be performed before an other one. n-Ary relations, i.e., relations involving a set of n objects (n > 2), can be modeled by a $K_{1,n}$ .

Not all aspects of problem instances can be represented in terms of nodes, arcs, and edges. These aspects can be divided into two categories: properties of individual objects, and properties of assignments. Examples of the first category are the sizes of the processes, the capacities of the resources, and the length of the planning period. These properties will be described as attributes of the corresponding nodes, or as attribute of the time system. An example of the second category is the processing time of a process when it is assigned to a particular combination of resources. In order to describe these kinds of properties, attributes of appropriate auxiliary nodes are introduced. The class of instances that can be specified with the proposed method will be called the general problem class.

In the next subsections, the instance specification method will be described in more detail, demonstrating how certain aspects of problem instances can be formulated in terms of attributed graphs. We like to emphasize that in doing so, our primary objective is not to show how specific characteristics of objects and relations between objects can be specified, but to illustrate how attributed graphs can be used to model characteristics of a problem instance. Objects are represented by nodes, properties of objects are represented by attributes, and relations between objects are represented by graph constructs. The proposed specification method can be extended naturally, if necessary, to accommodate some property of an object or some relation between objects by introducing a new attribute or a new graph construct. Consequently, we are confident that our specification method will be able to represent all instances of problems for which a planning board is useful.

In Section 4, we show how problem types can be specified by formulating restrictions on the general problem class. In appendices A and B, we give several examples of problem instances and types in order to demonstrate the power and wide applicability of the introduced methods.

## 3.2. Time

Time plays an important role in planning boards. The way in which time occurs is different for different problems. For a timetabling problem for schools, the planning period may cover five days consisting of eight hours, with an hour being the smallest time unit, whereas for a machine scheduling problem, the planning period may be one working day of 12 hours, with a minute being the smallest time unit. For flexibility purposes we allow the introduction of a time system for each problem instance. This time system consists of time units on different levels. The smallest time unit is specified in the first level, the second smallest time unit in the second level, etc. For the jth time unit also the conversion factor with respect to the $(j-1)$ st time unit is given. For example, a planning period covering one day, with one second being the smallest time unit, is specified in the following way.

number of levels: 4

level 1
unit name: second
level 2
unit name: minute
conversion factor: 60
level 3
unit name: hour
conversion factor: 60
level 4
unit name: day
conversion factor: 24
planning period: 1 day

## 3.3. Resources and processes

## 3.3.1. Resources and their attributes

Depending on the application, a resource can be almost anything. In a production planning application, personnel, money, raw materials, and machines may all be resources. In a time-tabling application for a school, the resources may be classrooms and teachers.

An important concept related to resources is that of a capability. A resource may possess several capabilities, i.e., it may be able to perform various tasks. A mechanic may be qualified to change oil and to repair brakes. A teacher may be qualified to teach mathematics as well as physics.

Although a resource may be able to perform different tasks, some set-up or change-over may be necessary before a particular task can be performed. Such a set-up brings the resource in the required mode. The corresponding set-up time can be either sequence dependent or sequence independent. In the first case, the set-up time is completely determined by the required mode. In the second case, the set-up time depends on the current mode of the resource and the mode that is required. The concept of mode is different from the concept of capability. A sawing machine may possess only one capability, the capability sawing, but several modes, one for each possible size of an object that can be sawn.

Most resources are not free commodities. Their utilization by some process will affect the possibilities for utilization by other processes. Quantities related to the utilization of a resource are usage and consumption.

The usage of resource R by process P at time t is a quantity that indicates to what extent R is occupied by P. The total usage of R at time t, i.e., the sum of the usage of all processes assigned to R at time t, is limited by the capacity of R at time t.

The consumption of resource R by process P during a time interval $[t_{1}, t_{2}]$ is a quantity that indicates to what extent R is consumed by P during that interval. The total consumption of R up to time $t^{*}$ , i.e., the sum of the consumption of R up to $t^{*}$ over all processes assigned to R, is limited by the supply of R up to $t^{*}$ .

Based on the different kinds of utilization the following distinction between resources can be made (see also Błazewicz et al. [3]):

\- Renewable resources: Resources for which only their total usage at every moment is constrained. An example of such a resource is a painting machine, which can paint all day but no more than one object at the same time.

\- Non-renewable resources: Resources for which only their total consumption up to any given moment is constrained. An example of such a resource is finances.

\- Doubly constrained resources: Resources for which both total usage and total consumption are constrained. An example is personnel. An employee can perform only a limited number of tasks at the same time and can perform these tasks only during a limited number of man hours.

Usage and consumption can both occur in either continuous or discrete quantities. A painting machine may be able to paint up to ten objects at the same time. Its capacity then is ten units, and the assignment of a painting job to this machine implies a usage of one unit. It is impossible to paint half objects, and therefore usage, in this case, is a discrete quantity. The storage capacity of a truck, in contrast, can be used in continuous quantities. With respect to consumption, fuel will be consumed in continuous quantities, but in assembling a car steering wheels will be consumed in discrete quantities.

Mostly, usage and consumption will be modeled as one-dimensional quantities. Multi-dimensionality, however, is possible. For an employee there may exist a limit on the number of hours per day he may work (e.g., 10 hours) as well as a limit on the number of hours per week (e.g., 40 hours). This cannot be modeled by supplies that replenish the “hours-inventory” to 10 at the beginning of each day, because the week-limit may then be exceeded. By modeling consumption and supply as two-dimensional quantities we can solve this problem. Another example of two-dimensional usage is found in transportation problems, where the usage of a truck is limited with respect to volume as well as weight.

The capacity and supply of a resource may change during the planning period as a result of instance-dependent and plan-dependent factors. For example, during a certain period the capacity of some machine may be smaller than normal because of maintenance, or the supply of some half-product will increase at the moment that a process that represents the production of that half-product is completed. Instance-dependent changes in capacity and supply will be modeled in terms of attributes of the resources. Plan-dependent changes in the supply of a resource will be modeled as (possibly negative) consumption of that resource. Similarly, the available capacity of a resource is reduced when it is used by a process, and it is increased again as soon as that process is completed.

A resource that possesses several capabilities may have different performance levels with respect to these different capabilities. The aforementioned mechanic may be very fast in changing oil, but he may be very slow when it comes to repairing brakes. In order to handle such differences, resource characteristics related to speed, usage, and consumption have to be specified for each of its capabilities.

A resource node has the following attributes:

availability periods: A set of time intervals specifying the time periods during which the resource is available.

category: An indicator that specifies the type of resource, i.e., renewable, non-renewable, or doubly constrained.

number of modes: A natural number. For each mode the following must be specified:

name: A name that uniquely identifies the mode. set-up time: A function of the status of the resource, i.e., the active mode, that computes the set-up time that is needed to bring the resource into this mode.

usage: This attribute consists of three sub-attributes.

divisibility: An indicator that specifies whether usage of the considered resource is modeled as a continuous or as a discrete quantity. In case usage is continuous the value is 0 and in case usage is discrete the value is the discretization unit.

dimension: A natural number representing the dimension of usage of the considered resource. capacity: A function of time, describing the plan-independent capacity.

consumption: This attribute consists of three sub-attributes.

divisibility: An indicator that specifies whether consumption of the considered resource is modeled as a continuous or as a discrete quantity. If consumption is continuous the value is 0 and if consumption is discrete the value is the discretization unit.

dimension: A natural number representing the dimension of consumption.

supply: A function of time, describing the plan-independent supply.

number of capabilities: A natural number. For each capability the following four sub-attributes must be specified:

name: A name that uniquely identifies the capability. If different resources possess the same capability, the same name must be used when referring to this capability.

speed: A real number that is used to determine the duration of a process when that process is assigned to this resource. It is not necessarily equal to the actual speed of the resource, as will be illustrated in Section 3.4.

usage factor: A real number that is used to determine the usage of the resource when a process is assigned to this resource. If this resource is used in combination with other resources, then this attribute is also used to determine the usage of those resources. In Section 3.4 we will discuss the use of the usage factor extensively.

consumption factor: A real number that is used to determine the consumption of the resource when a process is assigned to this resource. If this resource is used in combination with other resources, then this attribute is also used to determine the consumption of those resources. We will discuss the use of the consumption factor extensively in Section 3.4.

The usage attribute is specified only for renewable and doubly constrained resources, the consumption attribute for non-renewable and doubly constrained resources. These attributes represent plan-independent properties of a resource. Usage and consumption occur only during the time intervals in which processes are assigned to that resource, and the used and consumed amounts will be different for different processes. It is therefore not possible to model usage and consumption in terms of resource attributes. Furthermore, actual usage and consumption may occur only during part of the total processing time. For example, a production run may require a machine for the entire period, whereas it may require an employee to start the machine only for the first five minutes of the period. Similarly, the entire required amount of raw materials may be consumed at the beginning of the process, whereas fuel may be consumed at a constant rate during the processing period. The specification of these usage and consumption patterns will be discussed in Section 3.4.

## 3.3.2. Processes and their attributes

A process can be anything that must be assigned to a set of resources and a time interval in order to obtain a feasible plan. In a timetabling problem for a school, the processes may be the lessons that must be assigned to teachers, class-rooms, and time intervals. In a machine scheduling problem, the processes are the tasks that must be assigned to machines and time intervals.

There are two kinds of processes: non-repetitive and repetitive processes. A non-repetitive process is performed only once. A repetitive process can be performed an arbitrary number of times; the number of repetitions is determined by the planner by specification of the processing interval.

A process node has the following attributes:
name: A name that uniquely identifies the process.

type: An indicator that specifies whether the process is non-repetitive or repetitive.

mode: An indicator that specifies the mode in which the resource(s) to which the process is assigned have to be.

size: A real number that is used to determine the duration of the process in case of a non-repetitive process, or to determine the length of one repetition in case of a repetitive process.

usage intensity: A vector that is used to determine the usage of the resource(s) that the process is assigned to.

consumption intensity: A vector that is used to determine the consumption of the resource(s) that the process is assigned to.

release time: A point in time before which the process cannot be performed.

deadline: A point in time after which the process cannot be performed.

due date: A point in time by which the process preferably should be completed.

split: An indicator that specifies whether the process may be preempted or not. It has value 0 if the process, once started, cannot be interrupted, 1 if the process may be temporarily stopped and later resumed using the same resources, and 2 if the process can also be resumed using other resources.

## 3.4. Specifying feasible assignments

In this section, we discuss requirement relations. Requirement relations are relations between processes and resources indicating which resources can be used to perform a process. We use an incremental approach with respect to requirement relations. We start with simple requirements, i.e., processes requiring a single capability, and continue with more complicated requirements, i.e., processes requiring combinations of capabilities and processes requiring one of several combinations of capabilities. At the end of this section we will discuss how aspects related to feasible assignments such as duration, set-up times, usage, and consumption are modeled.

## 3.4.1. Processes requiring a single capability

A process that requires a specific capability can be assigned to any resource that possesses that capability. In fact, a choice has to be made between all resources that possess the required capability. Such a choice is modeled by a $K_{1,n}$ , in which the auxiliary node, the capability node, is connected to all nodes representing resources that possess the considered capability. For each capability that is required by some process, a capability node is introduced, and the associated $K_{1,n}$ is formed. The requirement relation is modeled by an edge connecting the process node and the capability node that represents the required capability.

A capability node has only one attribute:

name: The name uniquely identifies the capability. It must be the same as the name, given as a resource attribute, of the capability it represents.

An example is given in Fig. 3. Processes $P_{1}$ and $P_{2}$ require capability $C_{1}$ , which is possessed by resources $R_{1}$ and $R_{2}$ . Process $P_{3}$ requires capability $C_{2}$ , which is possessed by resources $R_{2}$ and $R_{3}$ .

## 3.4.2. Processes requiring a combination of capabilities

In many problems, performing a process requires the use of a combination of resources, or, better, a combination of capabilities. Both paint and a painter are needed to paint an object. Lessons cannot be taught unless a teacher and a classroom are available. Such a combination of capabilities is again modeled by a $K_{1,n}$ . The auxiliary node, the capability set node, is connected to all capability nodes representing the required capabilities. If a process requires a particular combination of capabilities, this is modeled by introducing an edge connecting the process node and the corresponding capability set node. The process can be performed by any combination of resources that possesses all capabilities in the capability set.

![](/api/attachments/HJBGC59D/fulltext/images/1e7b2176984000038a2d826b48615bc8a3e807d7add9d1709853879a1a67ba3f.jpg)  
Fig. 3. Processes requiring a single capability.

Note that, although any combination of capabilities may be considered as a capability set, only those combinations that are actually required by the processes are of interest.

A capability set node has several attributes. However, most of them will be introduced when we discuss duration, consumption, and usage in more detail. Here, we only introduce one attribute:

name: A name that uniquely identifies the capability set.

An example of requirement relations dealing with capability sets is given in Fig. 4.

Processes $P_{1}$ and $P_{2}$ both require a resource possessing the capability $C_{1}$ and a resource possessing capability $C_{3}$ . The resource combination $\{R_{1}, R_{4}\}$ would satisfy these requirements. Process $P_{3}$ requires a resource with the capability $C_{2}$ and a resource with the capability $C_{3}$ . The combination $\{R_{3}, R_{4}\}$ is feasible. The combination $\{R_{2}, R_{4}\}$ is feasible for all three processes.

3.4.3. Processes requiring one of several combinations of capabilities

Sometimes, a process does not require a specific combination of capabilities, but one of several alternative capability sets. In such a case, we say that the process requires a particular function. This is modeled by a $K_{1,n}$ , in which the auxiliary node, the function node, is connected to all capability set nodes between which a choice can be made. If a process requires a function, a choice between the associated capability sets is to be made. The process then can be performed by any set of resources that possesses all capabilities in the chosen capability set.

Functions may be useful for production problems in which different production modes occur, which imply the possible use of totally different resources, e.g., production by hand or by machine.

## A function node has only one attribute:

name: A name that uniquely identifies the function.

An example of requirement relations with functions is given in Fig. 5. Processes $P_{1}$ and $P_{2}$ both require function $F_{1}$ , implying that they must be performed by resources possessing the capabilities in capability set $CS_{1}$ or by resources possessing the capabilities in $CS_{2}$ .

In summary, three different types of $K_{1,n}$ 's may occur in the subgraph representing the requirement relations. The auxiliary nodes are the capability nodes, the capability set nodes, and the function nodes, respectively. The first $K_{1,n}$ represents a choice relation between resources possessing the same capability. The second states that a particular combination of capabilities is required. The third again represents a possibility for choice, now between several capability sets. Each process node is connected, via a requirement edge, to either a capability node, or a capability set node, or a function node.

![](/api/attachments/HJBGC59D/fulltext/images/1ed15566acbb601dfa8a1c5945921c0dd8a70329e5083810530fef0b44e554b0.jpg)  
Fig. 4. Processes requiring a combination of capabilities.

![](/api/attachments/HJBGC59D/fulltext/images/28a6f234efd3fc4ca2714a0bcb3c96c9387c00e6b1adbd47e0a1158e6c582156.jpg)  
Fig. 5. Processes requiring one of several combinations of capabilities.

## 3.4.4. Duration, set-up times, usage, consumption

The subgraph representing the requirement relations enables us to identify for each process the resources to which it can be assigned. Given such an assignment, we want to determine the following (assuming that the considered process is non-repetitive):

\- The set-up times required to bring the resources in the correct modes.

\- The duration of the process: the time to complete the process. Together with the starting time of the process, the duration determines the processing interval.

\- The usage pattern of each resource that is used: the time interval within the processing interval during which the process occupies the resource and the amount of the resource that is occupied by the process during this time interval.

\- The consumption pattern of each resource that is consumed: the time interval within the processing interval during which the process consumes the resource and the amount of the resource that is consumed by the process during this time interval. We will assume that consumption takes place at a constant rate. Instantaneous consumption can be modeled by specifying an infinitesimal time interval.

In case of repetitive processes, a set-up is only performed at the beginning of the first repetition, and the duration corresponds to the length of one repetition. We will assume that the usage and consumption patterns will be the same for every repetition. If, for example, at the beginning of a repetition a certain amount of raw materials is consumed, the same amount will be consumed at the beginning of all other repetitions.

The set-ups are much easier to deal with than duration, usage and consumption, because the set-up time of a particular resource does not depend on the other resources that are used. Given an assignment of a process to a combination of resources, for each of those resources the set-up time can be computed using the mode attribute of the process and the set-up attribute of the considered resource. The duration of the process, as well as the usage and the consumption of a specific resource, may depend on all the resources that occur in the assignment. For example, when a process requires a machine and fuel, the consumption of fuel will not only depend on the process but also on the machine that is actually used.

When a process requires a single capability, duration, consumption, and usage can easily be determined. The duration of the process is computed as the quotient of the size attribute of that process and the speed attribute of the resource it is assigned to. The interval during which any consumption or usage occurs is equal to the processing interval. The consumed amount is computed as the product of the consumption intensity attribute of the process and the consumption factor attribute of the resource, and the used amount is computed as the product of the usage intensity and the usage factor attributes.

The situation is more complicated when a process requires a combination of capabilities. In order to deal with these complications, we introduce several attributes for the capability set nodes. The first deals with the duration of the process.

duration: A function of the size attribute of the process and the speed attributes of the resources that computes the duration, i.e.,

$$
d \left(s _ {0}, s _ {1}, \dots , s _ {n}\right),
$$

where $s_{0}$ is the value of the size attribute of the process, n is the number of capabilities in the capability set, and $s_{i}$ ( $i = 1, \ldots, n$ ) is the value of the speed attribute of the resource possessing capability i.

Suppose the capability set consists of the capabilities machine, employee, and material. Let $s_{0}$ be the size attribute of the process, and let $s_{1}$ , $s_{2}$ , and $s_{3}$ be the speed attributes of the machine, the employee, and the raw material, respectively. If the speed is completely determined by the speed of the machine, the following duration function is used:

$$
d \left(s _ {0}, s _ {1}, s _ {2}, s _ {3}\right) = s _ {0} / s _ {1}.
$$

If the ability of the employee to work with that machine plays a role, the duration function may be something like

$$
d \left(s _ {0}, s _ {1}, s _ {2}, s _ {3}\right) = s _ {0} / v _ {s _ {1}, s _ {2}},
$$

where $V=\{v_{ij}\}$ is some predefined matrix, $v_{ij}$ being the speed at which a process is performed when the value of the speed attribute of the used machine is i and the value of the speed attribute of the used employee is j. Note that in this case the speed attributes do not reflect the actual speed of the resources, but are merely indices used to extract the correct values from a matrix.

For each capability in the capability set, the following two attributes are specified in order to describe the usage pattern.

usage interval: A function of the starting time and the duration of the process that computes the time interval during which usage of the resource possessing the considered capability takes place, i.e., $[t_{1}, t_{2}] = t_{u}$ (start, duration).

usage volume: A function of the usage factor attribute of the process and the usage intensity attributes of the resources that computes the volume used, i.e.,

$$
v _ {u} \left(i ^ {u}, f _ {1} ^ {u}, \dots , f _ {n} ^ {u}\right),
$$

where $i^{u}$ is the value of the usage intensity attribute of the process, n is the number of capabilities in the capability set, and $f_{i}^{u}$ ( $i = 1, \ldots, n$ ) is the value of the usage factor attribute of the resource possessing capability i.

Let us again consider the example with the capability set consisting of the capabilities machine, employee, and material. Some machines require an employee during the first five minutes for starting it up, whereas others do not. This can be modeled by assigning a value of 1 to the usage factor attributes of the machines that do require an employee ( $f_{1}^{u} = 1$ ), and a value of 0 to those that do not ( $f_{1}^{u} = 0$ ), and by applying the following usage pattern:

$t_{u}$ (start, duration)

$$
= [ \text { start }, \text { start } + 5 ], v _ {u} (i ^ {u}, f _ {1} ^ {u}, f _ {2} ^ {u}, f _ {3} ^ {u}) = f _ {1} ^ {u}.
$$

For each capability in the capability set, the following two attributes are specified in order to describe the consumption pattern.

consumption interval: A function of the starting time and the duration of the process that computes the time interval during which consumption of the resource possessing the considered capability takes place, i.e.,

$$
\left[ t _ {1}, t _ {2} \right] = t _ {c} (\text { start }, \text { duration }),
$$

where start is the starting time of the process, and duration is the value computed by the function given in the {duration attribute described above.

consumption volume: A function of the consumption factor attribute of the process and the consumption intensity attributes of the resources that computes the volume consumed, i.e.,

$$
v _ {c} \left(i ^ {c}, f _ {1} ^ {c}, \dots , f _ {n} ^ {c}\right),
$$

where $i^{c}$ is the value of the consumption intensity attribute of the process, n is the number of capabilities in the capability set, and $f_{i}^{c}$ ( $i = 1, \ldots, n$ ) is the value of the consumption factor attribute of the resource possessing capability i.

Consider again the capability set again consisting of the capabilities machine, employee, and material, and let the material capability be the only one that is possessed by non-renewable resources. If a process consumes a fixed amount of the material at a constant rate during the entire interval, the consumption pattern for the material capability is as follows:

$$
t _ {c} (\text { start }, \text { duration })
$$

$$
= [ \text { start }, \text { start } + \text { duration } ], v _ {c} (i ^ {c}, f _ {1} ^ {c}, f _ {2} ^ {c}, f _ {3} ^ {c}) = i ^ {c},
$$

where the value of the consumption intensity attribute $(i^{c})$ equals the fixed consumed amount.

The attributes of the capability sets allow us to specify complex consumption and usage patterns for a large variety of problems. Obviously, assigning the correct values to the different process and resource attributes is important. Sometimes it may be necessary to assign to, for example, the speed attribute of a resource, a value that has little to do with the actual speed of that resource.

Example 3.1 We consider the problem of making coffee, more specifically the capability set MakeCoffee consisting of the capabilities CoffeeMachine, Filter, GroundBeans, Water, and Coffee.

There are two resources that possess the capability CoffeeMachine. Machine A can make one liter of coffee in 15 minutes, machine B does it in 10 minutes. Making one liter of coffee requires 0.10 units of GroundBeans, consumed at the beginning of the processing interval, and 1 liter of water, consumed gradually during the entire processing interval. Independently of the amount of coffee to be made, one filter is required, consumed at the start.

If we want to perform the process 0.8 Coffee, making 0.8 liter of coffee, we model this by assigning the value 0.8 to the consumption intensity attribute as well as to the size attribute of the process. Furthermore, we assign the values 4/60 and 6/60 to the speed attributes of resource A and B respectively, and use one minute as time unit.

The attributes of the capability set MakeCoffee then are:

duration: size/CoffeeMachine.speed

(CoffeeMachine)

usage interval: [start, start + duration]

usage volume: 1

(Filter)

consumption interval: [start, start]

consumption volume: 1

(GroundBeans)

consumption interval: [start, start]

consumption volume: consumption intensity
\* 0.10

consumption interval: [start, start + duration]
consumption volume: consumption intensity (Coffee)

consumption interval: [start, start + duration]
consumption volume: - consumption intensity

## 3.5. Other relations between objects

Specifying the requirement structure, i.e., specifying for each process the combinations of resources it can be assigned to, is only part of the specification of a problem instance. Usually various other relations exist between processes and resources. Many of these can easily be specified in the instance graph.

## 3.5.1. Precedence relations

A precedence relation indicates that the set of allowed start and completion times of some process depends on the start or completion time of some other process. Precedence relations are binary relations that can be represented by arcs between process nodes in the instance graph. We distinguish four types:

\- A finish-to-start relation indicates that process $A$ must be completed before some process $B$ is started.

\- A start-to-start relation indicates that process $A$ must be started before process $B$ is started.

\- A start-to-finish relation indicates that process $A$ must be started before process $B$ is completed.

\- A finish-to-finish relation indicates that process $A$ must be completed before process $B$ is completed.

A time-lag may be associated with each of the four types of precedence relations. For example, a finish-to-start relation can be stated as “process A must be completed at least 10 minutes before process B starts.”

The attributes of precedence arcs are:

type: Either finish-to-start, or start-to-start, or start-to-finish, or finish-to-finish.

time lag: The minimum and maximum allowed time lag.

## 3.5.2. Common resource relations

A set of processes may be related because they have to be processed on the same set of resources. Such an n-ary relation is specified as a $K_{1,n}$ ; the auxiliary node is the common resource set node.

The only attribute of a common resource set node is:

name: A name that uniquely identifies the common resource set.

In case of a common resource relation between several processes, there is no need for individual requirement edges. Instead the requirement edge will connect the common resource set node to a capability node, a capability set node, or a function node. In this light, the common resource relation can be seen as an obligation relation, in contrast to the choices represented by functions and capabilities. As soon as one of the processes in a common resource set is assigned to a particular resource combination, all other processes in that set have to be assigned to the same resource combination.

## 3.5.3. Process group relations

A set of processes may be related for some other reason than common resources. Such an n-ary relation is represented by a $K_{1,n}$ ; the auxiliary node is the process group node. For instance, the notion of a job in machine scheduling problems can be modeled as a process group.

The attributes of the process group node are:

name: A name that uniquely identifies the process group.

release time: No process in the process group can be performed before its release time.

deadline: No process in the process group may be completed after its deadline.

due date: All processes should preferably be completed by their due date.

exclusion: If this attribute has the value true, then no two processes in the process group may be performed at the same time.

Note that release time, deadline, and due date can be specified for all processes in a process group separately, but even when the exclusion attribute has the value false, the introduction of a process group can be useful for emphasizing characteristic structures in problem instances.

## 3.5.4. Resource group relations

Similarly to process groups, resource groups can be used to emphasize certain relations between resources. The introduction of resource groups imposes no additional restrictions on the set of feasible plans.

The attribute of the resource group node is:

name: A name that uniquely identifies the resource group.

## 3.6. Extensions

In the previous sections, we have shown that it is possible to specify many different aspects of the problem instances that we are interested in by using attributed graphs. The combined use of graph elements and attributes has enabled us to deal with such diverse problem characteristics as precedence constraints, resources possessing the same capabilities, and complex consumption patterns. Our general problem class, i.e., the class of problem types of which instances can be specified with our method, includes a large variety of problems that are of theoretical or practical interest. However, there still exist many problem instances that currently cannot be specified. This is not a consequence of the lack of expressive power of attributed graphs, but it is a consequence of the selection criteria that we have applied with respect to the problem characteristics that we wanted to be able to specify. These selection criteria have been chosen somewhat arbitrarily. The main goal of this chapter is to show that it is possible to develop a method that allows us to specify a fairly large class of interesting problem types. Both the notions “fairly large” and “interesting” are subjective, but we think that they do apply to the general problem class that is induced by our specification method.

## 3.7. Views of the instance graph

In the sections above, we have discussed the various components that can be used to specify a problem instance in terms of an instance graph. The specification of the nodes, arcs, edges, and $K_{1,n}$ 's with their associated attributes results in an instance graph that represents all information about the problem instance under consideration. During the planning process, a planner may want to view parts of this information. If he wants to make an assignment for a particular process, he may be interested in the set of resources to which the considered process can be assigned, or he may want to know which other processes have a precedence relation with the considered process. This kind of information can easily be obtained because it corresponds to relatively small subgraphs of the instance graph. Such a subgraph will be called a view of the instance graph. Many views can be defined. A few examples follow below.

![](/api/attachments/HJBGC59D/fulltext/images/661439a9bd280d2e926fc8be707a6ae2fb5df6f64593268e499e80a4590eba8a.jpg)  
Fig. 6. A precedence view.

Assignment view: This view presents for a set of processes the resources to which it can be assigned, i.e., all the paths originating from one of the processes and ending at a resource. Examples of this view have already been given in Figs. 3–5. Process view: This view presents for a set of processes the process groups and common resource sets to which they belong.

Resource view: This view presents for a set of resources the resource groups and capabilities to which they belong.

Precedence view: This view presents for a set of processes the precedence relations between them. An example is given in Fig. 6. The arc from node B to node C implies that process B must be started at least 5 time units and at most 20 time units before process C is started.

A view is a convenient mechanism to present parts of the information embedded in the instance graph. Note that it is possible that a view contains some redundancy. For example, when a particular capability is possessed by only one resource, the corresponding capability node can be considered as redundant. By connecting the process, common resource set, function, and capability set nodes that are connected to that capability node, directly to the corresponding resource node, a view can be reduced to a smaller, possibly more insightful one.

## 4. Problem types

In general, planning boards are not developed as a tool for solving one particular problem instance, but as a tool for solving a set of problem instances with similar characteristics. We use the term problem type to refer to a set of problem instances satisfying certain conditions. The general problem class, i.e., the set of all problem instances that can be specified with the aid of the instance specification method, is a problem type itself.

A PBG requires information about the characteristics of the problem type for which a planning board has to be generated and about the desired representations and manipulations. Information about the desired manipulations could be something of the following sort: the planning board must support the reassignment of a process. If at a given moment process A is assigned to resource $R_{1}$ with start time $t_{1}$ , the user should be able to reassign process A to resource $R_{2}$ with start time $t_{2}$ . It should be obvious that the implementation of such a manipulation will depend on the problem type. For a problem type in which all resources are available during the whole planning period, checking the feasibility of a reassignment is much easier than for a problem type in which the resources are only available during certain time intervals.

In fact, the main purpose of the specification of a problem type is to provide the necessary information to implement the desired manipulations and representations as efficiently and effectively as possible. Consequently, the specification of a problem type should provide information on those common characteristics of the various problem instances that are important for the development of manipulations and representations. Therefore, care should be taken to ensure that the specification of the problem type is accurate. It should contain all problem instances for which the planning board is to be used, but as few others as possible because they may lead to a planning board that is less efficient and effective than possible.

Problem types will be specified by formulating restrictions on the instance graph. A problem type is then the set of all instances that satisfy the given restrictions.

## 4.1. Restrictions on the instance graph

The characteristics of a problem instance are defined by the structure of the associated instance graph and the values of the attributes of the various graph elements. We can therefore distinguish two types of restrictions: on the graph structure and on the attribute values.

## 4.1.1. Restrictions on the graph structure

Characteristics of a problem type that can be specified in terms of restrictions on the graph structure relate to the presence or absence of the various graph elements and to the way these graph elements are interconnected.

Consider the well-known job shop scheduling problem. The restrictions that have to be imposed on the graph structure are the following:

\- The only node types that appear are process, resource, capability, and process group.

• Each capability node is connected to exactly one resource node.

• Each requirement edge connects a process to a capability.

\- Precedence relations occur in chains and only involve processes in the same process group.

If the problem type becomes more complex, it is not always possible to specify restrictions that are valid for all graph elements of the same type. For example, consider the extension of the job shop scheduling problem in which each task requires both a machine and some raw material. In an instance graph, this extension would be modeled with a capability set node that specifies that a machine and some raw material are required for a task. However, in a type specification it is insufficient to specify that capability set nodes exist and that each capability set node is connected to exactly two capability nodes, because also instances in which a task is assigned to two machines would satisfy this restriction.

In order to deal with such problems, we need to be able to distinguish nodes of the same type. The notion of a node group is introduced precisely for that reason. A node group is a group of nodes of the same type that are subject to the same restrictions. In the above extension of the job shop scheduling problem, we would introduce two capability node groups, Machine and Inventory, and impose the following restrictions:

\- The only node types that appear are process, resource, capability, capability set, and process group.

• Each capability node is connected to exactly one resource node.

\- Each capability set node is connected to exactly one capability node in the node group Machine and to exactly one capability node in the node group Inventory.

• Each requirement edge connects a process to a capability set.

\- Precedence relations occur in chains and only involve processes in the same process group.

Besides restrictions on the presence or absence of the various graph elements and on the way they are interconnected, it is often necessary to also impose restrictions on the number of them. For example, if the raw material in our extension of the job shop scheduling problem is the same for all tasks, one should be able to specify that the number of nodes in the node group Inventory is precisely one.

## 4.1.2. Restrictions on the attributes

Characteristics of a problem type that can be specified in terms of restrictions on the attributes of the graph elements relate to their domains. The domain of an attribute is its set of admissible values. In a problem type specification it is possible to reduce a domain by specifying restrictions on the set of admissible values. Attribute restrictions are specified for node groups.

## 4.2. Specifying problem types

In this subsection, we present a syntax which can be used to specify the restrictions discussed in Section 4.1 more formally. The syntax can be modified or extended in order to deal with other kinds of restrictions. In Appendix B several problem types are specified using this syntax.

## 4.2.1. Node groups

The first part of the specification of the problem type concerns the node groups that appear in an instance. For each node type the associated node groups and a specification of the number of nodes in these node groups have to be given. For example,

PROCESS

Task2 $\{1,\ldots,\infty\}$

indicates that there are three node types and four node groups. The node groups Task1 and Task2 may have an arbitrary number of nodes, the node group Machine may have one up to four nodes, and the node group Type has precisely one node.

Instances with five or more resources or more than one capability do not belong to this problem type. Also instances with common resource set nodes, function nodes, capability set nodes, process group nodes, or resource group nodes do not belong to this problem type.

In the example above, the number of nodes in a node group is restricted to be in a specified set, e.g., $\{1\}$ , $\{1,\ldots,4\}$ , and $\{1,\ldots,\infty\}$ . In addition to specifying a set, it is also possible to relate the cardinality of a node group to the number of nodes in another node group. For example,

$$
\begin{array}{l l} \text {RESOURCE: } \\ \text {Machine} & \{2, \ldots , 1 0 0 \} \\ \text {CAPABILITY: } \\ \text {Type} & \# (\text {Machine}) \end{array}
$$

would indicate that the number of nodes in the node group Type is equal to the number of nodes in the group Machine.

## 4.2.2. Graph structure

The second part of the specification of a problem type concerns the structure of the instance graphs. It deals with n-ary relations, requirement edges, and precedence arcs.

For each of the $K_{1,n}$ 's associated with the node groups, the node groups to which they can be connected and a specification of the cardinality of these node groups have to be given. For example,

CAPABILITY:

Machine #(Machine)

CAPABILITY SET:

Transform

Type {1}

InputInv {1}

OutputInv {1}

indicates that each node in the node group Type is connected to all nodes in the node group Machine, and that each node in the node group Transform is connected to one node in the node group Type, one in the node group InputInv, and one node in the node group OutputInv.

Requirement edges connect process nodes and common resource set nodes to function nodes, capability set nodes, and capability nodes. Restrictions on the possible positions of requirement edges are specified for all relevant node groups. For example,

REQUIREMENT EDGES:
Task Type
CRSet1 Mode1
CRSet2 Mode2

indicates that (process) nodes in the node group Task are connected by a requirement edge to (capability) nodes in the node group Type, and that (common resource set) nodes in the node groups CRSet1 and CRSet2 are connected by a requirement edge to (function) nodes in the groups Mode1 and Mode2, respectively.

Precedence arcs usually occur between processes in the same node group or in the same process group. Furthermore, the graphs describing precedence relations often have a special structure, such as chains or trees. The structure of the precedence graph is specified for all relevant node groups. For example, suppose Group1,...,Group4 are process node groups, and Job is a node group of process groups. Then,

<table><tr><td colspan="2">PRECEDENCE ARCS:</td></tr><tr><td>Group1</td><td>intree</td></tr><tr><td>Group2</td><td>outtree</td></tr><tr><td>Group3 ∪ Group4</td><td>general</td></tr><tr><td>Job</td><td>chain</td></tr></table>

indicates, that the subgraph induced by precedence arcs of (process) nodes in the node group Group1 is an intree, that the subgraph induced by precedence arcs of (process) nodes in the node group Group2 is an outtree, and that the subgraph induced by precedence arcs of (process) nodes in the node groups Group3 and Group4 does not have a special structure. Furthermore, for each process group in the node group Job the following must hold: the subgraphs induced by precedence arcs of nodes representing processes in that process group are chains,

## 4.2.3. Attributes

The third part of the specification of a problem type concerns the attributes of the different objects. For each node group as well as for the precedence arcs, a domain is specified for each attribute. For example,

PROCESS:
Task
type non-repetitive
size {1,2}
RESOURCE:
Machine
category non-renewable
PRECEDENCES:
Group1
type {finish-to-start,start-to-start}
time lag [0, 50]

indicates that processes in the node group Task are non-repetitive and have size 1 or 2, that resources in the node group Machine are non-renewable, and that the precedence relations between nodes in the node group Group1 are either finish-to-start or start-to-start with a minimum time lag of 0 and a maximum time lag of 50 time units.

It is also possible to enforce two attributes to take on the same values. For example,

PROCESS:
Task
size {1, . . . , ∞}
consumption intensity size

indicates that the size attribute of processes in the node group Task can take on any positive integer value, and that the value of the consumption intensity attribute is equal to the value of the size attribute.

The attributes of capability sets are functions of attributes of other objects. In the problem type specification, either these functions are completely specified, or restrictions on their shape are imposed. In referring to attributes of other objects we apply a two-field notation: object.attribute, where object is a node group. When misinterpretation is impossible, it suffices to only state attribute. For example,

CAPABILITY SET:
ResourceSet
duration size/MacCap.speed (MacCap)
usage interval [start, start + duration]
usage volume 1
(InvCap)
consumption interval [start, start]
consumption volume: a \* consumptionintensity
    a ∈ (0, ∞)

indicates that for a capability set in the node group ResourceSet the duration function is defined as the quotient of the size of the process and the speed of the resource possessing a capability in the node group MacCap. Furthermore, that resource is used during the entire processing interval, the resource possessing a capability in the node group InvCap is consumed at the beginning of the processing interval, and the function that is used for computing the consumed volume is a linear function of the consumption intensity attribute of the process.

When certain attributes of objects are irrelevant for the problem type we want to specify, for example the {due date attribute in case no due dates occur, this can be indicated by “does not apply”. If no domain is specified for an attribute of an object, we assume that the default domain specifications apply. The default domain specifications for the different attributes are the following:

ATTRIBUTES
PROCESS:
type non-repetitive
mode does not apply
size (0, ∞)
usage intensity 1
consumption intensity does not apply
release time does not apply
deadline does not apply
due date does not apply
split 0
RESOURCE:
availability periods does not apply
category renewable
number of modes 0
usage
divisibility 1
dimension 1
capacity c(t) = 1
consumption
divisibility 1
dimension 1

<table><tr><td>supply</td><td> $s(t) \in \{1, \dots, \infty\}, t = 0$  $s(t) = 0, t \neq 0$ </td></tr><tr><td>number of capabilities</td><td>no default</td></tr><tr><td>spread</td><td>1</td></tr><tr><td>usage factor</td><td>1</td></tr><tr><td>consumption factor</td><td>does not apply</td></tr><tr><td colspan="2">CAPABILITY SET:</td></tr><tr><td>duration</td><td>no default</td></tr><tr><td>usage interval</td><td>no default</td></tr><tr><td>usage volume</td><td>no default</td></tr><tr><td>consumption interval</td><td>no default</td></tr><tr><td>consumption volume</td><td>no default</td></tr><tr><td colspan="2">PROCESS GROUP:</td></tr><tr><td>release time</td><td>does not apply</td></tr><tr><td>deadline</td><td>does not apply</td></tr><tr><td>due date</td><td>does not apply</td></tr><tr><td colspan="2">PRECEDENCES:</td></tr><tr><td>type</td><td>finish-to-start</td></tr><tr><td>time lag</td><td> $[0, \infty]$ </td></tr></table>

Time occurs in the problem type specification in a similar way as attributes. In the default time system, there is only one level and there is no restriction on the length of the planning period:

<table><tr><td colspan="2">TIME:</td></tr><tr><td>number of levels</td><td>1</td></tr><tr><td>planning period</td><td>{1,...,∞}</td></tr></table>

## 5. Concluding remarks

In this paper, we have introduced the concept of a planning board generator (PBG). Given a specification of the problem type for which a planning board has to be developed and a specification of the desired representations and manipulations, a PBG should automatically create an initial version of the planning board.

An important aspect of a PBG is the problem specification. Any planning problem is characterized by the processes and resources, the time system, and the constraints that must be satisfied when processes are assigned to resources and time intervals. The constraints are expressed in terms of properties of the processes and resources or in terms of relations between processes and resources. This problem structure has enabled us to develop a general method, based on attributed graphs, for the specification of problem instances. Nodes represent processes and resources. Attributes of nodes represent properties of the corresponding objects. Graph constructs like arcs, edges, and $K_{1,n}$ 's are introduced to represent relations between objects. In Section 3, a detailed description of a number of properties of processes and resources and various kinds of relations is given. The presented instance specification method can easily be extended or modified in order to deal with elements of planning problems that have not been discussed. The instance specification method has served as a basis for the problem type specification method discussed in Section 4. A problem type is a set of instances that satisfy certain restrictions. In the type specification method, these restrictions are formulated as restrictions on the attributes and the structure of the instance graph.

After the designer of a planning board has provided the PBG with information about the problem type and the desired representations and manipulations, this information must be processed and an initial version of a planning board must be produced. To a large extent, this comes down to tailoring basic implementations of procedures to the formulated desires. Since the function of an automated planning board is to support the representation and manipulation of plans, the plan plays a central role in most procedures. The implementation of a procedure determines how a plan is represented or how it can be modified. If we want to develop powerful basic implementations, we must be able to refer to elements of plans in a uniform way for different problem types. One natural possibility is to extend the instance graph of Section 3 in such a way that it can represent plans as well, for example by introducing an assignment attribute for processes. This attribute would contain the resources and the time intervals that a process is assigned to and, when required, other relevant information.

As soon as we have mechanisms to store information about instances and plans, it is possible to develop general procedures for representing and modifying these plans. Such a procedure can be designed, for example, for drawing a Gantt chart. Information about the problem type and desires of the planner can then be used to set certain parameters, ensuring that the time system and the resources are represented properly on the axes. The information stored in the assignment attribute can then immediately be translated into rectangles drawn at the right position. Similar procedures can be formulated for data tables, inventory graphs, and other representation mechanisms, and for several simple manipulations like moving a process from one set of resources to another.

However, the situation becomes more complicated when manipulations involve the use of algorithms. On the one hand, it is clear that having a single algorithm for the entire general problem class is impossible, since such an algorithm is bound to be very time consuming or to give bad results when applied to specific subclasses. On the other hand, it is also clear that having a separate algorithm for each problem type is also impossible, since the number of problem types is too large. A bottom-up approach may be successful: we identify algorithms that are efficient for certain problem types and modify them in such a way that they can handle a wider problem class. In the end, this approach should lead to a limited number of reasonably efficient and effective algorithms for large problem classes. For each such problem class, a library of algorithms can be created. We are currently working on the design of such algorithms for a large class of machine scheduling problems (see Wennink [18]).

## Appendix A. Examples of problem instances

In this appendix we describe the instance graphs, or parts of it, of three problem instances. The first example shows what kinds of connections between the different types of nodes are possible. In the second example, we consider a timetabling problem for a school. The third example deals with a factory scheduling problem with a non-trivial consumption pattern.

Example A.1. We consider the following production planning problem. Four products of two different types are to be made. Products 1 and 2 are products of the first type, products 3 and 4 are of the second type. Processes P1, P2, P3, and P4 represent the production of products 1, 2, 3, and 4. There is a fifth process, M, which represents some maintenance activities. Performing P1 can be done in two modes, the normal node or the special mode, P2 requires the special mode. In both modes an employee and a machine of the type MT1 are used, but some machines of that type can only be used in the special mode and others only in the normal mode. The processes P3 and P4 require a machine of the type MT2 and an employee. The combination that is used for P3 must also be used for P4. The maintenance process is to be performed by one of the employees. The instance graph for this problem is given in Fig. 7.

This example illustrates that all different kinds of resource requirements discussed in Section 3.4 can occur in the same problem instance. Process P1 requires a function, process P2 requires a capability set, and process M requires a capability. Furthermore, since processes P3 and P4 must be performed on the same combination of resources, there is an associated requirement edge connecting the corresponding common resource set node with, in this case, a capability set node. □

Example A.2. We consider the following timetabling problem. Each week, each group of pupils has to get lessons in different subjects during a specified number of hours. Some lessons require teachers with full qualification, others require teachers with partial qualification. Most lessons can be given in normal classrooms, but for some subjects the lessons require special rooms. Chemistry lessons, for example, must be given in rooms in which experiments with chemicals can be performed.

We can describe this situation in the following way. The processes are the lessons given to the different groups. They are non-repetitive. An example is the chemistry lesson for group 3. There are two kinds of resources: teachers and classrooms. A teacher can have several capabilities, representing the subjects he is qualified to teach and the levels of qualification. Since a teacher may be fully qualified for one subject and partially qualified for the other, it is necessary to introduce capability nodes for each possible combination of subject and qualification. A classroom also may have several capabilities. A particular classroom may be suited for chemistry lessons, as well as normal (for example, English) lessons.

Each lesson requires a particular kind of classroom and a particular kind of teacher. These requirements are represented by requirement edges connecting the processes and capability sets. Each capability set consists of two capabilities, one representing the required kind of classroom, the other representing the required kind of teacher. For example, the lesson English for group 4 requires the capability set E - F, representing a normal classroom and a teacher with full qualification for the subject English.

![](/api/attachments/HJBGC59D/fulltext/images/7c5f68f386abe1f93b3713f283d0cdc8162c9df725265cc77cfe9337ad591b35.jpg)  
Fig. 7. A production planning problem instance.

A part of an instance is depicted in Fig. 8. Only the lessons English and chemistry for groups 3 and 4 and not all teachers and classrooms are considered.

The planning period will consist of 5 days of say 8 hours. The resources are renewable resources with capacity 1. A process uses both kinds of resources fully during the entire processing interval, which is always one hour. □

Example A.3. Jones and Maxwell [10] give an example of a factory scheduling problem. There are three processes, 1MSUB, 2MSUB, and ASSEM. Process 1MSUB uses a machine of the type A-MILL and materials MAT1 and MAT2 to create half-products SUB1. Process 2MSUB uses the machine MILL and the half-product SUB3 to create another half-product, SUB2. Process ASSEM is performed by a worker, who assembles half-products SUB1 and SUB2 to create the end-product WIDGET. The reduced assignment view of this instance is given in Fig. 9.

All processes are repetitive. The machines are renewable resources; the materials, half-products, and end-products are non-renewable resources. The machines have capacity 1 and are always used up to capacity. The materials are consumed at a constant rate during the processing period, and the half products and end products are consumed (produced) at the beginning (end) of each repetition.

![](/api/attachments/HJBGC59D/fulltext/images/ddff771eb580aa3f29a2bad5096cd1c6fcb9796f7315ee77cb13ca85b9e97c35.jpg)  
Fig. 8. Part of a timetabling instance.

![](/api/attachments/HJBGC59D/fulltext/images/c778faa4cfc7f5604cbe0d5421b1f645e91e8ad1bdd809c776f60ef586fc09e3.jpg)  
Fig. 9. A reduced assignment view of a factory scheduling instance.

We consider the capability set $CS1$ . The duration solely depends on the $MILL$ that is used, and the consumed volumes are completely determined by the consumption intensity $(i^{c})$ of the process and the consumption factor of the considered resource $(f^{c}(\cdot))$ . The attributes of capability set CS1 then are: name: $CS1$

duration: = size/A-MILL.speed

(MAT1)

consumption interval: [start, start + duration]
consumption volume: consumption intensity/MAT1.comsumptionfactor
(MAT2)

consumption interval: [start, start + duration]
consumption volume: consumption intensity/MAT2.consumptionfactor
(A-MILL)

usage interval: [start, start + duration]
usage volume: 1
(SUB1)

consumption interval: [start + duration, start + duration]
consumption volume: - consumption intensity/SUB1.consumptionfactor

## Appendix B. Examples of problem types

Example B.1. The simple job shop scheduling problem type discussed in Section 4.1, in which each task requires one specific machine, can be specified as follows:

$$
\{1, \dots , \infty \}
$$

Machine $\{1,\dots ,\infty \}$

MacCap #(Machine)

$$
\{1, \dots , \infty \}
$$

Note that although non-repetitive and renewable are the default values for the type and category attributes, we have explicitly mentioned them in the problem type specification for clarity. □

Example B.2. In Appendix A, an example of a timetabling problem has been discussed. Lessons must be assigned to teachers and classrooms, and the feasibility of an assignment depends on the qualification of the teacher (what subject, full or partial qualification) and the properties of the classroom (chemistry lessons require specific facilities for performing experiments). The example can be seen as an instance of the problem type in which each lesson (process) requires a combination (capability set) of a type of classroom and a specific qualification (both capabilities).

In the terminology of our specification method, these restrictions can be formulated in the following way. We only give the node groups and the graph structure restrictions that are related to the processes, resources, capabilities, and capability sets.

NODE GROUPS
PROCESS:
Lesson {1,...,∞}
RESOURCE:
Teacher {1,...,∞}
Classroom {1,...,∞}
CAPABILITY:
Qualification {1,...,∞}
ClassroomType {1,...,∞}
CAPABILITY SET:
Room & Qual {1,...,∞}
GRAPH STRUCTURE
CAPABILITY:
Qualification
Teacher {1,...,∞}
ClassroomType
Classroom {1,...,∞}
CAPABILITY SET:
Room & Qual
ClassroomType {1}
Qualification {1}
REQUIREMENT EDGES:
Lesson Room & Qual
□

Example B.3. Anthonisse et al. [1] describe resource-constrained project scheduling (RCPS) as follows.

A set of tasks is to be processed by a set of resources. For each task, there is a release time and a deadline, which define a time interval in which the task must be processed. Once a task is started it must be completed without interruption. For any two tasks, there are a lower bound and an upper bound on the length of the time period between the completion of one task and the start of the other. (...)

A function may be performed by various combinations of resources, each with its own speed. In general, each function has a class of feasible resource sets, and the processing time of a task depends on the feasible resource set that is chosen to perform the function it requires. The processing time is the amount of work (i.e., the number of units of the function) required by the task divided by the speed of the feasible resource set.

No resource can be allocated to two tasks at the same time. If a set of resources is allocated to a task, then each of its constituent resources is occupied by that task from its starting time until its completion time. For each resource there is a set of time intervals during which the resource is available.

We will now describe this problem type with our specification method.

The time system is the default system. There is only one time unit, and the planning period can be as small or as large as one wants.

Four kinds of objects are distinguished in the description above: tasks, resources, resource sets, and functions. In our terminology, they are processes, resources, capability sets, and functions, respectively. In fact, a fifth kind of object, the project, is considered, which is equal to the process group. Beside these five objects, our method requires capability nodes. Each resource has a unique capability. Therefore, the number of capability nodes is equal to the number of resource nodes. There are no restrictions on the number of nodes of any of the other types.

NODE GROUPS
PROCESS:
Task {1,...,∞}
RESOURCES:
Resource {1,...,∞}
CAPABILITY:
ResCap #(Resource)
CAPABILITY SET:
ResourceSet {1,...,∞}
FUNCTION:
Function {1,...,∞}
PROCESS GROUP:
Project {1,...,∞}

Each resource possesses a unique capability. Therefore, each capability node (belonging to the node group ResCap) is connected to one resource node. The capability $K_{1,n}$ 's are in fact $K_{1,1}$ 's. The ResourceSets may consist of any number of resources, or better, of any number of capabilities. Each function node may be connected to any number of ResourceSet nodes (possibly one), and each process requires a function. For each Project, the number of tasks in it is completely instance dependent. Precedence relations are only possible between tasks in the same Project.

## GRAPH STRUCTURE

GRAPH STRUCTURE
CAPABILITY:
ResCap
Resource {1}
CAPABILITY SET:
ResourceSet
ResCap {1,...,∞}
FUNCTION:
Function
ResourceSet {1,...,∞}
PROCESS GROUP:
Project
Task {1,...,∞}
REQUIREMENT EDGES:
Task Function
PRECEDENCE ARCS:
Project general

All processes are non-repetitive. The usage intensity does not apply, because it is not required in order to describe usage in the capability set attribute. The consumption intensity does not apply because all resources are renewable. The size attribute of processes, and the release time, deadline, and due date attributes of Projects and processes may take on any value. The tasks cannot be preempted.

Only renewable resources occur. A resource cannot be used for different tasks at the same time. Hence, the capacity is constantly 1, and the usage discretization unit is also 1. The speed is not determined by individual resources, but only by the resource set as a whole. Therefore, the speed attribute does not apply. Also, the usage factor and the consumption factor do not apply.

Since no consumption occurs, the consumption attributes do not apply. The duration is determined as the quotient of the size attribute of the process and a number representing the speed of a resource combination that is different for each capability set. Each resource that a process is assigned to is used during the entire processing interval. The used volume is equal to one for each resource.

The precedence relations are always of the finish-to-start type. There are no restrictions on the corresponding time lags.

ATTRIBUTES
PROCESS:
Task
type non-repetitive
usage intensity does not apply
consumption intensity does not apply
release time [0,∞)
deadline [0,∞)
due date [0,∞)
RESOURCE:
Resource
category renewable
number of capabilities 1
(ResCap, 1)
speed does not apply
usage factor does not apply
consumption factor does not apply
CAPABILITY SET:
ResourceSet
duration a \* size
a ∈ (0,∞)

<table><tr><td colspan="2">(ResCap)</td></tr><tr><td>usage interval</td><td>[start,start+duration]</td></tr><tr><td>usage volume</td><td>1</td></tr><tr><td colspan="2">PROCESS GROUP:</td></tr><tr><td colspan="2">Project</td></tr><tr><td>release</td><td>[0,∞)</td></tr><tr><td>deadline</td><td>[0,∞)</td></tr><tr><td>due date</td><td>[0,∞)</td></tr><tr><td colspan="2">PRECEDENCES:</td></tr><tr><td colspan="2">Project</td></tr><tr><td>time lag</td><td>[[0,∞),[0,∞)]</td></tr></table>

Anthonisse et al. [1] give an example of a problem instance of the RCPS type. The corresponding instance graph is given in Fig. 10. □

Example B.4. Jones and Maxwell [10] discuss factory scheduling problems. In these problems three kinds of objects occur: processes, inventories, and machines. Processes are performed on one machine and consume and produce the contents of inventories.

In their article, Jones and Maxwell introduce a specification method that is based on networks. We can describe this problem type with our specification method as well.

We introduce three resource node groups. One node group consists of nodes that represent machines, the other two represent continuous inventories and discrete inventories, respectively. The reason for introducing two inventory node groups is that different restrictions on the attribute values can be specified for continuous and discrete inventories.

![](/api/attachments/HJBGC59D/fulltext/images/bb0b8d078d1e99384217000e3eb495c8af30fb2014379b124a2adb9eb75d2269.jpg)  
Fig. 10. The RCPS instance.

Since different consumption patterns apply when an inventory serves as input or occurs as output of a process, for each of both types of inventory two capability node groups are introduced. There are no functions, common resource sets, process groups, and resource groups.

## NODE GROUPS

<table><tr><td colspan="2">PROCESS:</td></tr><tr><td>Process</td><td>{1,...,∞}</td></tr><tr><td colspan="2">RESOURCE:</td></tr><tr><td>Machine</td><td>{1,...,∞}</td></tr><tr><td>ContInventory</td><td>{1,...,∞}</td></tr><tr><td>DiscInventory</td><td>{1,...,∞}</td></tr><tr><td colspan="2">CAPABILITY:</td></tr><tr><td>MachineType</td><td>{1,...,∞}</td></tr><tr><td>ContInInv</td><td>{1,...,∞}</td></tr><tr><td>ContOutInv</td><td>{1,...,∞}</td></tr><tr><td>DiscInInv</td><td>{1,...,∞}</td></tr><tr><td>DiscOutInv</td><td>{1,...,∞}</td></tr><tr><td colspan="2">CAPABILITY SET:</td></tr><tr><td>ResourceSet</td><td># (Process)</td></tr></table>

There may be several machines of a particular type. For each process, the actually required inventories are completely specified. Hence, the corresponding $K_{1,n}$ 's connecting capabilities and resources are simple edges. Each ResourceSet consists of one machine type and an arbitrary number of inventories, which can be discrete or continuous, and can serve as input or occur as output. There are no precedence relations.

## GRAPH STRUCTURE

$$
\{1, \dots , \infty \}
$$

$$
\{0, \dots , \infty \}
$$

ContOutInv {1,...,∞}
DiscInInv {1,...,∞}
DiscOutInv {0,...,∞}
REQUIREMENT EDGES:
Process ResourceSet

The time system is again simple. There is only one time unit, and the planning period can be as small or as large as one wants.

All processes are repetitive processes. The size attribute can take on any value. Jones and Maxwell introduce a process attribute (Time/Lot) that deals with both the duration of one repetition and the consumption. In our approach, we enforce the size attribute and the consumption intensity to take on the same value. The usage intensity does not apply. We assume that a process may not be interrupted during a repetition, hence the split attributes have value 0. There are no release times, deadlines, and due dates.

Machines are renewable resources, with capacity equal to 1. They may have several capabilities, all representing a particular MachineType. Since the duration of a process is uniquely determined by the size of that process, the speed attribute for machines does not apply. Similarly, usage factor and consumption factor do not apply.

The inventories are non-renewable resources. The resources of the ContInventory type have continuous divisibility, the resources of the DiscInventory type have discrete divisibility. Again, the speed, usage factor, and consumption factor attributes do not apply. The supply attribute can take on any value.

Consumption patterns for the different inventories depend on whether they are discrete or continuous and on whether they are used as input or as output. The consumed volumes are determined by dividing a number that is different for each ResourceSet by the consumption intensity of the process. This number is positive if the inventory is used as input, and negative if the inventory is used as output. Consumption of the continuous inventories occurs during the entire processing period; consumption of discrete inventories occurs at the beginning (when used as input), or at the end (when used as output), of each repetition.
ATTRIBUTES
PROCESS:
Process
type repetitive

usage intensity
consumption intensity
RESOURCE:
Machine
category
number of capabilities
(MachineType, {1,...,
speed
usage factor
consumption factor
ContInventory
category
consumption
divisibility
supply
number of capabilities
(ContInInv, 1)
speed
usage factor
consumption factor
(ContOutInv, 1)
speed
usage factor
consumption factor
DiscInventory:
category
consumption
supply
number of capabilities
(DiscInInv, 1)
speed
usage factor
consumption factor
(DiscOutInv, 1)
speed
usage factor
consumption factor
CAPABILITY SET:
ResourceSet
duration
(Machine)
usage interval
usage volume
(ContInInv)
consumption interval
consumption volume does not apply size

renewable
{1,...,∞}
)

does not apply
does not apply
does not apply

non-renewable

$$
\begin{array}{l} 0 \\ s (t) \in [ 0, \infty) \\ 2 \end{array}
$$

does not apply
does not apply
does not apply

does not apply
does not apply
does not apply

non-renewable

$$
\begin{array}{l} s (t) \in \{0, \ldots , \infty \} \\ 2 \end{array}
$$

does not apply
does not apply
does not apply

does not apply
does not apply
does not apply

size

[start, start + duration] 1

[start, start + duration] a/consumptionintensity $a \in (0, \infty)$

(ContOutInv)
consumption interval
consumption volume

$$
\begin{array}{l} \text {[ start, start + duration]} \\ a / \text { consumptionintensity } \\ a \in (- \infty , 0) \end{array}
$$

(DiscInInv)
consumption interval
consumption volume

$$
\begin{array}{l} \text {[ start, start]} \\ a / \text { consumptionintensity } \\ a \in (0, \infty) \end{array}
$$

(ContOutInv)
consumption interval

consumption volume

$$
\begin{array}{l} \left[ \text {start + duration, start} \right. \\ \left. + \text {duration} \right] \\ a / \text {consumptionintensity} \\ a \in (- \infty , 0) \end{array}
$$

In Appendix A we have already discussed an instance of this problem type. The graph given in Fig. 9 does not fit in the specification of the problem type above since it represents a reduced view. In the complete graph the connections between capability sets and resources are always established via capabilities. The resource SUB2 would be connected to two capability nodes, one representing the use of SUB2 as input and one representing the use of SUB2 as output. MAT2 on the other hand, although also occurring in two capability sets, would be connected to only one capability node, since it is only used as input. □

## References

[1] J.M. Anthonisse, K.M. van Hee, J.K. Lenstra (1988). Resource-Constrained Project Scheduling: an International Exercise in DSS Development. Decision Support Systems 4, 249–257.

[2] J.M. Anthonisse, J.K. Lenstra, M.W.P. Savelsbergh (1988), Behind the Screen: DSS from an OR Point of View. Decision Support Systems 4, 413-419.

[3] J. Blazewicz, W. Cellary, R. Słowinski, J. Weglarz (1986). Scheduling under Resource Constraints — Deterministic Models. Annals of Operations Research 7.

[4] R.W. Conway, W.L. Maxwell, L.W. Miller (1967). Theory of Scheduling, Addison-Wesley, Reading, MA.

[5] M.L. Fisher (1985). Interactive Optimization. Annals of Operations Research 5, 541–556.

[6] M.L. Fisher, M.B. Rosenwein (1989). An Interactive Optimization System for Bulk-Cargo Ship Scheduling. Naval Research Logistics 36, 27–42.

[7] R.L. Graham, E.L. Lawler, J.K. Lenstra, A.H.G. Rinnooy Kan (1979). Optimization and Approximation in Deterministic Sequencing and Scheduling: A Survey. Annals of Discrete Mathematics 5, 287–326.

[8] R.D. Hurrion (1986). Visual Interactive Modelling. European Journal of Operational Research 23, 281–287.

[9] P. Jackson, J.A. Muckstadt, C.V. Jones (1989). COSMOS: A Framework for a Computer-aided Logistics System. Journal of Manufacturing and Operations Management 2, 122–148.

[10] C.V. Jones, W.L. Maxwell (1986). A System for Manufacturing Scheduling with Interactive Computer Graphics. IIE Transactions 18, 298–303.

[11] C.V. Jones (1990). An Introduction to Graph-Based Modeling Systems, Part I: Overview. ORSA Journal on Computing 2, 136–151.

[12] C.V. Jones (1992). User interfaces, in: E.G. Coffman Jr., J.K. Lenstra, A.H.G. Rinnooy Kan (eds.), Computing, Handbooks in OR & MS 3, Elsevier Science Publishers B.V., North-Holland, Amsterdam.

[13] C.V. Jones (1994). Visualization and optimization. ORSA Journal on Computing 6, 221–257.

[14] N.A. Moreira, R.C. Oliveira (1991). A Decision Support System for Production Planning in an Industrial Unit. European Journal of Operational Research 55, 319–328.

[15] E.R. Tufte (1983). The Visual Display of Quantitative Information. Graphics Press, Cheshire.

[16] E.R. Tufte (1990). Envisioning Information. Graphics Press, Cheshire.

[17] F. Viviers (1983). A Decision Support System for Job Shop Scheduling. European Journal of Operational Research 14, 95–103.

[18] M. Wennink (1995). Algorithmic Support for Automated Planning Boards. Ph.D. Thesis, Department of Mathematics and Computing Science, Eindhoven University of Technology.

[19] A.P. Woerlee (1991). Decision Support Systems for Production Scheduling. Ph.D. Thesis, Econometric Institute, Erasmus University Rotterdam.
