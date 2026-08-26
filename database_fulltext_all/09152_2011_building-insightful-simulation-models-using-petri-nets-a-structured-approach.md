---
otero_id: 9152
otero_key: "MS2P8F7N"
title: "Building insightful simulation models using Petri Nets — A structured approach"
authors: "Durk-Jouke van der Zee"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.11.028"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Building insightful simulation models using Petri Nets — A structured approach

Durk-Jouke van der Zee ⁎

Department of Operations, Faculty of Economics & Business, University of Groningen, P.O. Box 800, 9700 AV, Groningen, The Netherlands

## a r t i c l e i n f o

Article history: Received 12 February 2010 Received in revised form 3 November 2010 Accepted 21 November 2010 Available online 26 November 2010

Keywords: Simulation Petri Nets Visualization Problem structuring & solving

## a b s t r a c t

Petri Nets have essential strengths in capturing a system's static structure and dynamics, its mathematical underpinning, and providing a graphical representation. However, visual simulation models of realistic systems based on Petri Nets are often perceived as too large and too complex to be easily understood. This constrains stakeholders in participating in such modeling and solution <sup>fi</sup>nding, and limits acceptance. We address this issue by considering a structured approach for guiding the analyst in creating more insightful models. Key elements are a domain-related reference architecture that supports conceptual modeling coupled with uniform rules for mapping high-level concepts onto low-level Petri Net components. The proposed approach is implemented and illustrated in the manufacturing domain.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Petri Net formalisms have proved to be successful tools for the modeling and simulation of manufacturing systems [6,8,23,41]. Their success is underpinned by their basic strengths in accurately describing a system's static structure and its dynamics, the availability of mathematical analysis methods, and their graphical nature.

Many authors, however, argue that the use of Petri Nets in decision support for the design of manufacturing systems could be further improved if the model's size and complexity could be reduced. These characteristics are seen as hindering more active stakeholder understanding, participation, and acceptance of solutions [2,10,14,26]. In this article, we address this issue by developing guidance that could assist the analyst in de<sup>fi</sup>ning more insightful visual models.

Stakeholders' understanding of visual model elements, and their workings, starts from a recognition of high-level concepts [12,21]. Examples of such concepts within the manufacturing domain relate to machines, buffers, planners, and goods. The selection of concepts and their visual representation follows from the analyst's creativity. This creativity is bounded and guided by implicit or explicit guidelines, that is by good modeling practices and principles [20], domain-related insights [30] and, last but not the least, the logic and libraries that underlie simulation software [11].

Typically, Petri Nets start from a few basic low-level components used to de<sup>fi</sup>ne high-level constructs that resemble manufacturing entities. These low-level beginnings explain model size on the one hand, and the great efforts that the analyst has to put into insightful model structuring on the other. Basically, we assume model structuring to refer to both sound conceptualization, i.e., the choice of entities, their activities, and their relationships considered characteristic of a domain; and formalization, i.e., the mapping of the respective system elements onto model components. In this paper, we consider guidance for the analyst related to both activities.

The purpose of this article is to propose a structured approach to guide the analyst in building more insightful Petri Net simulation models. Key elements of the approach are a reference architecture that captures essential object classes for a domain, and a set of mapping rules for representing the respective objects as Petri Nets. Here, a reference architecture relies on a set of decomposition principles characterizing the <sup>fi</sup>eld of interest. In this paper, the approach is implemented within the manufacturing domain by linking a manufacturing reference architecture [36] to a speci<sup>fi</sup>c Petri Net formalism, i.e., ExSpect™, by de<sup>fi</sup>ning mapping rules. The use of this approach is illustrated and evaluated through a case study.

The remainder of the article is organized as follows. In Section 2, we provide an outline of our approach to guiding analysts in building more insightful Petri Net simulation models. Next, in Sections 3 and 4, we discuss key elements of its implementation in a manufacturing simulation, i.e., a reference architecture plus a set of rules for mapping object classes within the architecture onto basic Petri Net components. This includes a short introduction to ExSpect™. In Sections 5 and 6, we illustrate and evaluate the use of our approach with a case example. Finally, in Section 7, we summarize our main conclusions.

## 2. A structured approach to more insightful Petri Net modeling

In this section, we outline our approach to achieving more insightful Petri Net modeling, starting from the situation illustrated in Fig. 1. The <sup>fi</sup>gure distinguishes between the model cycle for a typical simulation project (see, for example Robinson [24]) and guidance for the analyst in executing modeling activities — as it follows from our approach.

![](/api/attachments/MS2P8F7N/fulltext/images/79e6306448c2639cf6ce564824d820c055dd1b159ba52cbf1716ec10d6c4e75d.jpg)  
Fig. 1. A structured approach for more insightful modeling.

Milestones in a simulation project are a description of a problem situation, a conceptual model, a coded model, and decision support in terms of solutions, and stakeholder understanding. Below, we will discuss the modeling activities that underlie these milestones and relate these to guidance for the analyst.

A description of a problem will usually give some idea of its context, and the dilemma faced by one or multiple stakeholders. Although the quality and detail of a problem description may differ greatly, it will refer, either explicitly or implicitly, to phenomena which are characteristic of a certain domain. This is the net effect of applying those cognitive approaches that are referred to as decomposition and classi<sup>fi</sup>cation [4,29]. Decomposition and classification principles, either implicit or explicit, may be used to capture domain characteristics. For example, in the manufacturing domain, it is common to distinguish between infrastructural elements such as machines and buffers, and movable objects such as goods, staff, and tools. In earlier work [34,37], we identi<sup>fi</sup>ed and summarized several decomposition principles that are of relevance to the manufacturing <sup>fi</sup>eld. As such, they may be helpful to an analyst in typifying a problem situation.

A conceptual model captures the model contents in terms of scope, i.e., the system entities to be modeled, and detail, i.e., the entity attributes to be considered. It serves both as a blueprint for coding and as a decision document, to be agreed upon by both analyst and stakeholders. We propose addressing the need for model detail, and its insightful representation, following from these uses through a reference architecture. A reference architecture refers to a well-de<sup>fi</sup>ned conceptual view of a domain, identifying and characterizing generic object classes and their workings. It builds on a comprehensive (framed) set of domain-related and more general decomposition principles. Note that the use of such a reference architecture should typically be complemented by the application of good modeling practices [20], including model simpli<sup>fi</sup>cation principles and an evolutionary model set-up [25].

Essentially, we assume a conceptual model that captures the problem situation, in terms of high-level manufacturing concepts, as the basis for de<sup>fi</sup>ning the executable coded model. In principle, high-level concepts cannot be mapped onto basic Petri Net components in a straightforward way due to the latter's low-levelness. Typically, highlevel concepts can only be modeled by de<sup>fi</sup>ning aggregates of basic Petri Net components. Our approach suggests the de<sup>fi</sup>nition and use of explicit mapping rules. These rules prescribe a format according to which object classes in the reference architecture should be de<sup>fi</sup>ned in terms of basic Petri Net components or aggregates thereof. The idea of uniformity, which underlies the rules, is meant to support the acquisition of model insight by creating “familiar” and “appealing” net structures.

User interaction with a visual simulation model is facilitated by linking the model to an experimental frame [40]. This de<sup>fi</sup>nes experimental factors, i.e., model entities open to modi<sup>fi</sup>cation in some respect, and model outputs, i.e., observations on model behavior which indicate and/or explain system performance. Alongside performance evaluation through simulation, many Petri Net formalisms also support the use of mathematical methods for system analysis. Given our focus on the graphical qualities of Petri Nets, we do not consider such methods here. However, their possible integration into our approach to develop more insightful Petri Net simulation modeling is considered to be both relevant and an interesting issue for future research.

## 3. Conceptual model — a reference architecture for manufacturing simulation

In this section, we discuss a reference architecture that is suitable for guiding an analyst in de<sup>fi</sup>ning a conceptual model for manufacturing simulation. First, we categorize the decomposition principles that underpin the architecture. Next, we consider essential characteristics of the architecture. Finally, we introduce a method for its use. For more details on these aspects, see Van der Zee and Van der Vorst [36], Van der Zee et al. [38]. Further, applications of the architecture may also be found in Van der Zee et al. [38], and Van der Vorst et al. [33].

## 3.1. Basis of the reference architecture — decomposition principles

The decomposition principles that underlie the reference architecture are shown in Table 1. Principles I – III are rather well-known and follow from the notion of a system boundary (I), basic system logic (II), and queuing systems (III). According to Lefrancois and Montreuil [13], making a distinction between intelligent and non-intelligent entities (IV) permits a more natural and richer presentation and implementation of modeled systems. In such a context, agents represent intelligent beings. Agents are used to implement the decision rules inherent to manufacturing system planning and control. Examples include routines for scheduling, dispatching, and releasing jobs to a machine or department. Further, principles I – IV tend to be valid for a much wider category than only manufacturing systems.

Decomposition principles underpinning the reference architecture for simulating manufacturing [34].

<table><tr><td colspan="2">Decomposition principles</td></tr><tr><td>I</td><td>External and internal entities</td></tr><tr><td>II</td><td>Movable and non-movable entities</td></tr><tr><td>III</td><td>Queues and servers</td></tr><tr><td>IV</td><td>Intelligent and non-intelligent entities</td></tr><tr><td>V</td><td>Infrastructure, flows and jobs</td></tr><tr><td>VI</td><td>Modality: physical, information, and control elements</td></tr></table>

Principles V and VI are somewhat more speci<sup>fi</sup>c to the manufacturing <sup>fi</sup>eld. Manufacturing systems are built up of infrastructural elements such as workstations, information systems, and managers. Flows refer to the objects being exchanged and transformed by this infrastructure as a net effect of jobs being executed (V). Applying the job concept is thought to bring two important advantages [36]. Firstly, the use of this common denominator for all activities, including decision-making, can provide a clear and natural mechanism for event scheduling, where events are related to the start and the completion of jobs. Secondly, having an explicit notion and allocation of company activities will increase the visibility and traceability of decision variables. Note how Principle V integrates two of the original principles underlying the reference architecture (see also, Van der Zee [34]). Finally, the separation of physical, information, and control elements (VI) is expected to facilitate a higher degree of model reusability and a more “natural” model building environment [15,22].

## 3.2. Reference architecture for manufacturing simulation

In this section, we discuss a reference architecture for manufacturing simulation. Our choice of model components is related to the use of decomposition principles – as identi<sup>fi</sup>ed by their Roman numbering. We will use an object-oriented notation for specifying model components [3].

## 3.2.1. Classes and hierarchies

The reference architecture distinguishes between three main object classes: agents, flow items, and jobs (V) as shown in Fig. 2. Agents represent the infrastructural, non-movable, intelligent elements of a manufacturing system such as workstations, information systems, and managers (II, IV). Their decision-making capabilities relate to the transformation of goods or data. System boundaries are re<sup>fl</sup>ected in the concept of internal and external agents (I). With internal agents, such as machines, warehouses, AGV systems, and planners, a distinction is made between processors and storages based on the nature of the dominant resource type (III). For external agents, the architecture separates suppliers from customers (III).

Four types of movable (or <sup>fl</sup>ow) items (II) are included in the reference architecture: goods (such as materials, parts, and semi-<sup>fi</sup>nished products), resources (such as workers, tools, and vehicles), data (monitoring data, demand <sup>fi</sup>gures, etc.), and job de<sup>fi</sup>nitions (VI). Job de<sup>fi</sup>nitions model the <sup>fl</sup>ow of control, i.e., the messages that steer the movement of goods, resources, and data. As such, they initiate and inform agent activities by carrying relevant information related to these activities, such as their input, processing conditions, and the agents to whom the resulting output should be sent.

In a manufacturing system, agents and <sup>fl</sup>ows are linked by jobs, i.e., business activities (V). Further, we assume that each such activity relates to a job. Typically, a job execution links <sup>fl</sup>ow items and agent's resources.

## 3.2.2. Class definitions – agents

The structure for agents follows from their role as intelligent entities (IV). The de<sup>fi</sup>nition used for the structure of an internal agent is inspired by the atomic model as de<sup>fi</sup>ned by Zeigler [41], see Fig. 3a.

The state of an agent is related to its attributes and their values. Attributes concern buffers and transformers (III). Buffers model the temporary storage of those <sup>fl</sup>ow items which are the prime subjects of a future job or which have a facilitative role in job execution (resources, information). Also note here that job de<sup>fi</sup>nitions for an agent are stored in the control queue. A transformer re<sup>fl</sup>ects a set of jobs being executed and contains the <sup>fl</sup>ow items that are related to these jobs.

Above, the basic elements of an internal agent have been discussed. Turning to agent functions, we will distinguish between input and output operations, and the local intelligence (IV). The initiation of a job is enabled by rules assembled in the local intelligence (IV). As the <sup>fi</sup>rst rule in initiating a job, the job de<sup>fi</sup>nition with the highest priority in the control queue is investigated. This job may then start if its demands in terms of inputs, capacity, and processing conditions are met.

The notion of local intelligence applies to all agents, including work stations and planners. Where the intelligence for work stations may be limited to elementary rules for the timing and release of jobs, the decision logic for controllers may be comprehensive. The decision logic for controllers may involve a wide range of rules that support, for example, capacity planning, material planning, scheduling, and dispatching.

Alongside the local intelligence element (IV), which is found for internal agents, generators and annihilators are also distinguished for external agents, see Fig. 3b (customer). Generators represent “sources” of <sup>fl</sup>ow items, while annihilators are “sinks” into which <sup>fl</sup>ow items ‘disappear’ (I). Local intelligence may be used to link generators and annihilators.

## 3.2.3. Relationships between agents

Agents communicate with one another by exchanging various types of <sup>fl</sup>ow items, the net results of job execution (V, VI). In this section, we will consider two scenarios within this basic type of relationship in somewhat more detail (Fig. 4a, b):

![](/api/attachments/MS2P8F7N/fulltext/images/e0f2ca99893e0be56443f1f2d5d973cc435f96bd00bd105d17f6176f31550e17.jpg)  
Fig. 2. Reference architecture for manufacturing simulation – main object classes.

![](/api/attachments/MS2P8F7N/fulltext/images/247637834f779a1c12af966c4495d597b2b57dcd8c67522c7816f1cb5c379a79.jpg)  
Fig. 3. Agent de<sup>fi</sup>nitions – internal agent (a); external agent (b).

• The relationship between an internal agent and its controller.

• Relationships between external and internal agents.

Control is assumed to be effected by the sending of job de<sup>fi</sup>nitions from a controller object to an internal agent, denoted as Int in Fig. 4a (VI). Each agent (subordinate) refers to only one controller (manager) from which it receives its job de<sup>fi</sup>nitions, denoted as F(C). Conversely, a subordinate can send information about its status to its controller. Mechanisms such as hierarchical control and coordinated control are embedded in this class structure by allowing higher level controllers to steer the activities of lower level controllers.

For external agents, we distinguish between customers and suppliers (I). Typically, a customer issues an order by sending a demand signal (F(I|D)) to an internal agent of type controller (Fig. 4b). The controller, in turn, speci<sup>fi</sup>es a job de<sup>fi</sup>nition (F(C)) for an internal agent (Int) who is then responsible for delivering the requested items (F(M)), where M refers to the modality. In the case of a supplier, the roles are different: the controller sends an order to a supplier, who has to take care of delivering the requested items.

## 3.2.4. Dynamics structure – agents executing jobs

In line with our job-oriented view, we assume that the execution of jobs by agents is the driving force of business dynamics (V). Job execution is related to a procedural three-phase description [19]. In the A Phase, it is determined which job is to be completed next. Once this job has been identi<sup>fi</sup>ed, time is advanced to the corresponding moment in time when that job will be <sup>fi</sup>nished. Subsequently, the job is “completed” (in the B-Phase), i.e., the resulting output is sent from the agent that carries out the job to other agents. In the C-Phase, a test is carried out to see whether the <sup>fl</sup>ow items that have been received by these agents enable the initiation of new jobs (conditional activities). The three phases are repeatedly run through until the simulation time is up.

(a)  
![](/api/attachments/MS2P8F7N/fulltext/images/dab76ed35505e21b1d03840fb5ebe989ecf0dacc33487dbfb4f8076d9726634e.jpg)  
Fig. 4. Agent relationships – control (a); customers (b).

## 3.3. Method for use

Elementary steps in the application of a reference architecture involve: (1) determining the system boundary, (2) de<sup>fi</sup>ning entities, i.e., agents, <sup>fl</sup>ow items, and jobs, following a top-down re<sup>fi</sup>nement process, and (3) detailing entities in a “bottom-up” process. Details of the respective steps can be found in Van der Zee et al. [38].

## 4. Coded model – mapping manufacturing objects onto Petri Nets

Many Petri Net formalisms have been developed over recent decades, starting from the “classic” Petri Nets proposed by Petri [18]. For an overview of these developments see Murata [16], David and Alla [5], and Jensen [8,9]. In this article, we link our structured approach to the use of a speci<sup>fi</sup>c Petri Net formalism, ExSpect™ [7]. Note that our choice of this formalism does not imply that the approach cannot be implemented using alternative Petri Net formalisms. We merely chose ExSpect™ as a suitable vehicle for illustrating its implementation.

In this section, we <sup>fi</sup>rst give a brief introduction to ExSpect™. More details can be found in Van Hee et al. [39] and Van der Aalst [31,32]. More particularly, we focus on its suitability for embodying high-level manufacturing concepts. In so doing, we set out some initial guidelines for selecting Petri Net formalisms to “<sup>fi</sup>t” the manufacturing domain. Next, we discuss the ExSpect™ language.

## 4.1. ExSpect™ – a brief introduction

Our discussion of ExSpect™ starts with an outline introduction to classic Petri Nets. Following this, extensions introduced within ExSpect™ relative to classic Petri Nets, and their relevance in modeling manufacturing object classes, will be considered.

Classic Petri Nets represent systems by means of a net structure, that is a bipartite directed graph for specifying the static part of the system, and a marking, which re<sup>fl</sup>ects the state of the system, as shown in Fig. 5. The net structure consists of two kinds of nodes: places and transitions. Places and transitions are connected by means of directed arcs. Arcs are only allowed to connect a place with a transition, or a transition with a place. In the <sup>fi</sup>rst possibility, the place is regarded as an input place for a transition, while the latter is regarded as an output place. The marking, or state, of a net corresponds to the assignment of one or more tokens to each place.

![](/api/attachments/MS2P8F7N/fulltext/images/80de3837107b027bd4906a3929b01ad2c0c22a7892359477aec607ff3aa0b6de.jpg)  
Fig. 5. Classic Petri Nets – notation and case example.

State changes are modeled within Petri Nets through the <sup>fi</sup>ring of a transition. Firing a transition amounts to the consumption of a speci<sup>fi</sup>ed number of tokens from all its input places and the production of tokens for all of its output places. A transition is only allowed to <sup>fi</sup>re (i.e. it is enabled) if there are suf<sup>fi</sup>cient tokens available in all of its input places. The <sup>fi</sup>ring of a transition is considered indivisible or atomic. An illustration of a <sup>fi</sup>ring mechanism and the associated state changes are illustrated in Fig. 5 (I, II, III). Note how the <sup>fi</sup>ring of transition T1, then allows transition T2 to <sup>fi</sup>re. The net structure in Fig. 5 may be used to model simple processes, such as secretaries' duties in dealing with mail (for example, putting a letter in an envelope (T1) and putting a stamp on the envelope (T2)), or a simple assembly operation involving two machines (T1, T2).

ExSpect™ extends classic Petri Nets through the notions of color, time, and hierarchy [31,32]. We will now brie<sup>fl</sup>y consider these extensions, and their relevance, starting from our reference architecture. Whereas classic Petri Nets do not allow tokens to be further detailed, ExSpect™ allows token attributes, or “colored” tokens. An important advantage of using colored tokens is the possibility to reduce model size by adding detail to tokens instead of creating more elaborate net structures – as would be the case with classic Petri Nets. Further, from a manufacturing perspective, token attributes assist in more natural modeling as they allow one to model <sup>fl</sup>ow items such as goods and data in a realistic way, see also Section 3.2.

ExSpect™ supports model structuring by allowing for hierarchy, i.e., representing systems as an aggregate of subsystems. As such, a construct labeled “system” is introduced. A system is an aggregate of places, transitions, and possibly subsystems. The notion of systems helps in creating a model overview for both analysts and stakeholders. Within the context of manufacturing systems it is helpful to identify and represent high-level concepts such as machines, planners, and buffers. We addressed, in Section 3.2, how these are referred to as agents in our reference architecture.

Logistic performance analysis of manufacturing systems requires the notion of time. Classic Petri Nets are not capable of handling quantitative time. ExSpect™ allows for stochastic delays, which are associated with time stamps linked to tokens. Time stamps specify the moment the respective tokens become available. Linking model dynamics with tokens enables a straightforward representation of jobs: as composites of one or more <sup>fl</sup>ow items being transformed until a pre-speci<sup>fi</sup>ed completion moment.

Fig. 6 shows a small example of an ExSpect™ net structure. Note that ExSpect™ addresses transitions as processors, and places as channels. Token colors are given in brackets. Further, time stamps are given for each token, specifying the moment (t) when it becomes available. For example, the token representing a pair of green shoes, will be available at t=1 and the <sup>fi</sup>ring of processor T1 is enabled at t=1, given the presence of both shoes and shoelaces. The subsequent <sup>fi</sup>ring of processor T2 is possible if both a box and the combination of shoes and shoelaces are available. Note how the time stamp of the latter entity follows from the execution of processor T1. The system concept (denoted as a rectangle) may be used to represent the “shoe shop”, rather than a single operation. In turn, this system may be used as a building block in a larger manufacturing system.

## 4.2. ExSpect™ – language

In this section, we consider the basic language constructs of ExSpect™, and link these to the basic elements of the underlying Petri Net formalism, see Section 4.1. For more detail and background see Van der Aalst [31,32] and ExSpect™ [7]. ExSpect™ distinguishes four kinds of de<sup>fi</sup>nitions: type definitions, function definitions, processor definitions, and system definitions. Type de<sup>fi</sup>nitions are used to specify token values. Each channel (place) has a type, and this determines the values for the tokens it may contain. The type system of ExSpect™ considers primitive types, such as booleans, numerals, reals, and strings, plus type constructors, which allow one to specify lists, sets, records, etc. As an example, a car may be speci<sup>fi</sup>ed as:

![](/api/attachments/MS2P8F7N/fulltext/images/b6f49111252c0d48f6ce99b2142dd7227cde062eaf0cd1705ec2533d79001d7f.jpg)  
Fig. 6. ExSpect™– case example.

car: [id: str, color: str, year: num]

The above type definition may be used to specify the car's license plates, its color, and the year it was built. It builds on a type constructor, i.e., a record, denoted as “[…]”, and two primitive types, i.e., num and str, referring to numerical and string values.

Functions respond to the need to specify values for tokens that are produced as a net effect of <sup>fi</sup>ring processors. Many common functions are available within ExSpect™ as standard features, concerning settheoretical, logical, and numerical constants and functions. For example, the following function may be used to compute the surface of a rectangle:

surface [x: real, y: real] := x\*y : real;

Processor definitions are used to describe transitions. De<sup>fi</sup>nitions consist of a header and a contents part. The header speci<sup>fi</sup>es the processor's name, interaction structure, and parameters. The interaction element details input channels, output channels, and stores. Note that stores refer to a special kind of place, one which always contains exactly one token. The contents part consists of concurrent assignments of expressions to output channels and to stores. Expressions may include the use of functions. For example, a machine operation may be modeled as:

```txt
proc machine [in start: part,
    out finish: part,
    val t : real]
:= finish <- operation(start) delay t;
```

Note how the duration of the operation (a function) is represented by adapting the time stamp of the respective part (token) by including a delay of duration t.

Similar to the processor de<sup>fi</sup>nition, a system definition also consists of a header and a contents part. The header details value, function, processor, and system parameters, and the interaction structure, in a similar way to the processor de<sup>fi</sup>nition. The contents part refers to a listing of all its elements, i.e., channels, stores, and processors. For example, if we consider a system that consists of a gas station and car wash:

```txt
sys car_service [in x:car, out y:car, t:real]
:=
channel cleaned_cars: init [id: 1, color: purple, year: 1990],
carwash (in x, out cleaned_cars),
gas station (in cleaned_cars, out y, val t);
```

The gas station and the car wash are represented by two processors. These processors are linked through a channel: cleaned cars. The channel is initialized by de<sup>fi</sup>ning a single token of type car.

4.3. Mapping high-level manufacturing concepts using ExSpect™ basic model components

4.3.1. Object classes – flow items, agents, and jobs

Our reference architecture for manufacturing systems distinguishes three main object classes, i.e., agents, <sup>fl</sup>ow items, and jobs, see Section 3.2. In Section 4.1 we informally linked the respective classes to ExSpect™. We showed how flow items can be represented naturally by tokens. Type definitions allow one to specify differences among <sup>fl</sup>ow items in a straightforward way, by associating them with token attributes.

Our proposal is to specify internal agents as systems using the following generic format:

```txt
(* INTERFACE *)
sys internal_agent [in X, out Y, con Z, val id: A ... ]
:=
(* BUFFERS *)
store Input_Buffer : B init ...
store Control_Queue : C init ...
...
(* TRANSFORMERS *)
channel Transformer : D init ...
...
(* INPUT OPERATIONS *)
input (in x, out Input Buffer | pre x.receiver = id)
inputc (in x, out Control_Queue | pre x.receiver = id)
...
(* LOCAL INTELLIGENCE FOR EXECUTION *)
local_intelligence (in Input_Buffer, Control_Queue, <BUFFERS>, out <TRANSFORMERS> | pre check(Control_Queue, Input_Buffer, <BUFFERS>))
...
(* OUTPUT OPERATIONS *)
output (in <TRANSFORMER>, out y)
...;
```

To support our discussion on the de<sup>fi</sup>nition of the internal agent, we graphically depict a typical agent structure as a Petri Net model in Fig. 7. The header of the system de<sup>fi</sup>nition speci<sup>fi</sup>es input and output channels. These re<sup>fl</sup>ect the in<sup>fl</sup>ow and out<sup>fl</sup>ow of various types of <sup>fl</sup>ow items. We set no a-priori restrictions on their speci<sup>fi</sup>cation, except for the presence of an input channel linking the agent with its controller (“con Z” in the header), see also Section 3.2.3. The body of the system de<sup>fi</sup>nition models the agent's internal structure in a generic way. This format is meant to characterize a skeleton architecture that speci<sup>fi</sup>es default elements of an agent´s structure and relationships. The architecture may be enriched and extended in practical use.

![](/api/attachments/MS2P8F7N/fulltext/images/c95452305a435c9c9d0d3cc1614de62c214dec3760741df44dc16270963ce426.jpg)  
Fig. 7. Petri Net models of agents – internal agent (a) and external agent (b).

The skeleton architecture includes an input buffer (Input\_Buffer), control queue (Control\_Queue), transformer (Transformer), and operations, i.e., input, output, and local intelligence. The respective operations link input channels $( " \mathrm { X } " $ in system header) with Input\_Buffer and Control\_Queue (input, inputc); Transformer and output channels (“Y” in the system header); and Control Queue, Input\_Buffer, and Transformer (local\_intelligence). Following ExSpect™ logic, operations are modeled by processors, whereas buffers and transformers are represented by stores and channels.

The practical use of the agent's system de<sup>fi</sup>nition requires the detailing of type de<sup>fi</sup>nitions, processors, and functions. Further, the above skeleton architecture allows the inclusion of additional facilitative buffers (bBUFFERSN) and transformers (bTRANSFORMERSN) dedicated to speci<sup>fi</sup>c <sup>fl</sup>ow items. This option may enhance model transparency. Note how the system de<sup>fi</sup>nition of an external agent follows from pruning the system de<sup>fi</sup>nition of the internal agent.

Jobs are associated with activities described by the local\_intelligence processor. Their dynamics are re<sup>fl</sup>ected by (sub)sets of <sup>fl</sup>ow items (tokens) contained in transformers. The respective sets refer to the inputs required for a speci<sup>fi</sup>c job, such as goods and tools, as re<sup>fl</sup>ected by alternative types of tokens. Jobs are initiated as a net result of executing (<sup>fi</sup>ring) the local intelligence, see Section 3.2.4.

4.3.2. Relationships between agents

Agent relationships are modeled by linking them through a common channel that connects their respective output and input channels. Control relationships are modeled by connecting each agent to a single controller, i.e., a supervising agent, see Section 3.2.3.

## 4.3.3. Dynamics structure – agents executing jobs

In our reference architecture, we relate dynamics to job execution. Job initiation is associated with the execution of local intelligence, by <sup>fi</sup>ring the respective processor. The preconditions for <sup>fi</sup>ring amount to the availability of job de<sup>fi</sup>nitions and the associated job inputs, see Section 3.2.4. Firing involves the setting of time stamps for those tokens modeling <sup>fl</sup>ow items, i.e., being subject to a job. In turn, time stamps set the bound events of job completion.

## 5. Case example – supply of re<sup>fi</sup>ned oils for margarine production

In this section, we present a case example to illustrate the guidance offered to an analyst in building more insightful simulation models based on Petri Nets. The case concerns the supply of re<sup>fi</sup>ned oils for producing margarine and was motivated by a project in industry involving a large manufacturer of margarine [1,27]. The basic ingredients of margarine are oils and fats. The manufacturer had decided to concentrate its re<sup>fi</sup>nery facilities for producing oils and fats at a single location. This decision forced a redesign of the transportation system for supplying the margarine production facilities. Here we will consider the supply system for a single production facility.

## 5.1. System description

The supply system is made up of transportation facilities, i.e., trucks, unloading stations, and a number of storage tanks. The re<sup>fi</sup>nery is located about a half-hour drive from the production facility. System complexity stems from restrictions on the use of resources, and the need to tightly tune supply operations in order to (1) guarantee a high service level at the production lines, (2) avoid overstocks, i.e., truck loads which cannot be unloaded because storage tanks are not available, and (3) reduce waiting costs at the unloading stations. Redesign of the supply system involves both its infrastructure and its control.

## 5.2. Conceptual model

As a <sup>fi</sup>rst step in modeling this situation, we considered a conceptual model for the supply system. The scope and level of detail are captured in our choice of agents and their attributes. Example agent de<sup>fi</sup>nitions are given in Fig. 8 representing the queue of trucks at the unloading stations (Queue) and the queue manager (Queue Manager). Jobs cover the moving of trucks towards the unloading stations, and the decisionmaking of the queue manager. Local data, i.e. OperatorData, QueueData, and PlannerData, support local decision-making by capturing agent status, and data on related agents. Note how information on truck arrivals (cf. the Output operation for the Queue) triggers decisionmaking for the queue manager.

## 5.3. Coded model

Fig. 9 shows the Petri Net simulation model that we built starting from the conceptual model, and the mapping rules proposed in Section 4.3. The <sup>fi</sup>gure represents those agents responsible for the physical <sup>fl</sup>ows of goods and resources (oil, trucks), i.e., OilRe<sup>fi</sup>nery, Queue, UnloadingStation1, UnloadingStation1.2, Tanks, and MargarineProduction, and their planning and control, i.e., SalesDepartment, PlanningOilDeliveries, QueueManager, LoadManager, and TankController. Here, SalesDepartment and MargarineProduction may be considered as external agents. Adequate planning and control of the supply system requires a detailed tuning of activities, represented by the <sup>fl</sup>ows of data. For example, new deliveries of oil from the storage tanks to the production lines are only allowed at the moment that the production lines complete a job. The manager of the storage tanks (TankController) is informed about respective job completions by messages (TankData). Note how ExSpect™ allows one to adapt the graphical system notation (cf. Figs. 5–7) to re<sup>fl</sup>ect some of the agent's characteristics. For example, the OilRe<sup>fi</sup>nery and Margarine-Production agents are displayed as “factories”.

Given the underlying conceptual model, each agent is de<sup>fi</sup>ned according to the mapping rules proposed in Section 4.3. Examples of Petri Net models for the Queue and QueueManager agents are given in

![](/api/attachments/MS2P8F7N/fulltext/images/6c708180aaa9a0a5d6cffdb6ab0dfef5f6d252b1978f9e3e62f135f7d06a10f7.jpg)  
Fig. 8. Class de<sup>fi</sup>nition for queue and queue manager agents.

![](/api/attachments/MS2P8F7N/fulltext/images/6d4e581d497d51640420ae0880015d48d75c44df6130c1b815501ce4a3bc73c4.jpg)  
Fig. 9. Petri Net simulation model of the supply system.

![](/api/attachments/MS2P8F7N/fulltext/images/46381f53dbf2a8c9183df46edf32237089673b8071d94beba49af1c175ed0e32.jpg)  
Fig. 10. Petri Nets model for queue agent.

![](/api/attachments/MS2P8F7N/fulltext/images/6e479076cd9f4c25ab19149c7370fb4a8e74bea4fb69cb24d4e493cf1a1336d4.jpg)  
Fig. 11. Petri Nets model for queue manager agent.

Figs. 10 and 11. In line with the discussion in Sections 3 and 4 and the conceptual model (Fig. 8), the respective models distinguish between input and output operations, local intelligence, and transformers.

## 6. Discussion – evaluation of the approach

In the preceding sections we have outlined, implemented, and illustrated a structured approach to simulation modeling. In this section, we make an initial assessment of its added value in guiding an analyst toward creating more insightful Petri Net simulation models.

## 6.1. Scope

Essentially, the scope of the approach is determined by its implementation, i.e., the choice or construction of decomposition principles, reference architecture, mapping rules, and Petri Net formalism. The approach itself is not domain-speci<sup>fi</sup>c, and addresses the general class of discrete event dynamic systems [28].

Implementing the approach then makes it domain-speci<sup>fi</sup>c, through the construction of a reference architecture – starting from the choice of underlying decomposition principles that are likely to be linked to a certain <sup>fi</sup>eld of interest. For example, the reference architecture discussed in this paper (Section 3) might be quali<sup>fi</sup>ed as ‘machine-oriented’, describing <sup>fl</sup>ows as passive objects that are operated upon [11]. An alternative view, not embedded in our reference architecture, is a ‘material-oriented’ view, which starts from the <sup>fl</sup>ow items, which then display autonomous behavior in acquiring passive resources. In other words, systems that foresee the intelligent behavior of movable entities may be less easily captured by the reference architecture. In this respect, one may think of large-scale transportation systems, or team-operated manufacturing cells.

In principle, the choice of Petri Net formalism and the construction of mapping rules should enable full coverage of the domain being addressed by the reference architecture. Here, coverage relates to their abilities to model relevant object classes, their relationships, and their dynamics. As an example of rules creating constraints, our mapping rule suggesting linking jobs to a set of tokens (Section 4.3.3) may hinder the modeling of job pre-emption. This is because the tokens in ExSpect™ are accessible no earlier than the moment indicated by their time stamp.

## 6.2. Guidance

Our approach is meant to guide an analyst in two respects. Firstly, the simulation project is supported by a clear notion of modeling phases and associated support. Next, by suggesting and characterizing the use of domain-based “tools”, i.e., decomposition principles, reference architecture, mapping rules, and Petri Net formalism, the analyst is assisted in model building. The relevance of this explicit support for the analyst seems high where Petri Nets are to be used for model coding – both with respect to modeling effectiveness (see Section 6.3) and ef<sup>fi</sup>ciency. This follows from the use of low-level basic components within the Petri Net. This characteristic places high demands on the analyst in terms of the choice of entities – and their detailing in order to guarantee visual models that are transparent to stakeholders.

## 6.3. Model transparency

Essentially, modeling support for the analyst, as offered by our approach, is meant to enhance model transparency. Here, we relate model transparency to stakeholders' understanding of the visual simulation model and its workings. The added value of our approach is discussed starting with a comparison of models built using our approach with ad-hoc model development. Typically, ad-hoc modeling may negate model transparency in two ways: by proposing model constructs that have little appeal to the domain and/or having a noninsightful visual presentation of the model constructs. The <sup>fi</sup>rst issue is essentially addressed in our approach by the reference architecture, and the second issue in our de<sup>fi</sup>nition of mapping rules. In this paper, we restrict the discussion to the second issue. Elaborate discussions on the added value of the reference architecture, in terms of model contents, may be found in Van der Zee and Van der Vorst [36] and Van der Zee [34].

To assess the relevance of the proposed mapping rules for the transparency of a Petri Net model, we consider the effects of their use on model size and complexity. In Section 1, we noted how these model qualities can hinder active stakeholder participation. The case example in Section 5 will be used to illustrate our reasoning:

• Model size: essentially, model size, in terms of the number of model components and their relationships, is assumed to in<sup>fl</sup>uence the ability of stakeholders to achieve a model overview. Typically, achieving an overview of a large model is improved by having a hierarchical model set-up, in which higher level models may be decomposed into multiple smaller sub-models. It is up to an analyst to specify the hierarchy and, contrary to ad-hoc approaches; our mapping rules offer explicit support for establishing a hierarchy through the notion of agents, that encompass a limited set of wellde<sup>fi</sup>ned components (see Figs. 7, 9–11). In principle, the agent notion adds one, basic, level to the model hierarchy. Note that large models may require more levels to ensure a good model overview. As a general rule, “splitting” higher level models should result in loosely coupled sub-models, each giving a clear overview of a cluster of related model elements [4]. The points of reference for a manufacturing simulation might be, for example, existing or new organizational structures in terms of departments and companies, and stocks decoupling manufacturing operations.

• Model complexity: the basic components of a Petri Net allow one to represent manufacturing entities in various ways – all of which are logically correct. In principle, such <sup>fl</sup>exibility is helpful by adding to Petri Nets' descriptive power. However, exploiting it excessively, as may occur in ad-hoc approaches, may increase model complexity signi<sup>fi</sup>cantly – making it dif<sup>fi</sup>cult for the stakeholder, and maybe even the analyst. By prescribing agent net structures based on a standard format we aim to avoid such complexity (see Figs. 7, 10, 11).

## 6.4. Enhancing support

We consider having a set of rules for mapping domain-related high-level concepts to Petri Nets as an essential element of our approach. This leaves open the possibility of creating more permanent support by designing comprehensive libraries of high-level building blocks that refer to generic net structures made up of basic Petri Net components.

## 7. Concluding remarks

In this article, we have addressed the creation of insightful visual simulation models based on Petri Nets. While Petri Nets are known for their qualities in accurately modeling and representing real systems, Petri Net models of real situations are often found to be too large and complex to be understood by non-experts. In response, we propose a structured approach for guiding the analyst in developing a model that provides greater insight to stakeholders.

Key elements of the approach are a reference architecture that captures the essential object classes of a domain, and a set of mapping rules for representing the respective objects as Petri Nets. Here, the reference architecture builds on elementary decomposition principles that characterize the <sup>fi</sup>eld of interest. As an illustration, the approach was implemented for the manufacturing domain by linking a manufacturing reference architecture to a speci<sup>fi</sup>c Petri Net formalism, i.e., ExSpect™, using mapping rules, and its use illustrated with a case example.

The reference architecture allows analysts to start from a clear and appealing – and shared – idea of the essential object classes within a domain, rather than having to create a vision of their own. Further, the mapping rules help to bridge the perceived “gap” between the highlevel manufacturing concepts and the low-level components of the Petri Net in a uniform way. This enhances model transparency both for stakeholders and for analysts. We view transparency as the basis for model effectiveness in terms of better quality and credible solutions, as well as for modeling ef<sup>fi</sup>ciency, i.e., minimizing the analyst's efforts in building, adapting, and re-using models.

An avenue for future research is to use our approach for other types of formalisms, such as DEVS [17,35,41]. Further, the approach should be validated through alternative implementations (in terms of choice of domain and formalism), and re<sup>fi</sup>nements are possible in its implementation within the manufacturing domain.

## References

[1] J. Alblas, The UniOil Supply Chain, MSc thesis, University of Twente, The Netherlands, 1994.

[2] K.D. Barber, F.W. Dewhurst, R.L.D.H. Burns, J.B.B. Rogers, Business-process modelling and simulation for manufacturing management – a practical way forward, Business Process Management Journal 9 (4) (2003) 527–542.

[3] G. Booch, Object-oriented analysis and design with applications, Benjamin Cummings, Redwood City, 1994.

[4] A. Burton-Jones, P.N. Meso, An empirical test of decomposition principles in object-oriented analysis, Information Systems Research 17 (1) (2006) 38–60

[5] R. David, H. Alla, Petri Nets for the modeling of dynamic systems – a survey, Automatica 30 (2)(1994)175–202

[6] F. DiCesare, H. Harhalakis, J.M. Proth, M. Silva, F.B. Vernadat, Practice of Petri Nets in manufacturing, Chapman & Hall, London, 1993.

[7] ExSpect, User Manual. Diemen: Deloitte & Touche Bakkenist8Available via, http:// www.exspect.com/19998[accessed February 12, 2010].

[8] K. Jensen, Coloured Petri Nets: Basic Concepts, Analysis Methods and Practical Use, Volume 1, Basic Concepts, Monographs in Theoretical Computer Scienc, 2nd ed, Springer-Verlag, Berlin, 19978, 2nd corr. Printing,

[9] K. Jensen, Petri Nets World – online services for the international Petri Nets community, 20098Available via, http://www.informatik.uni-hamburg.de/TGI/PetriNets/8 [accessed February 12, 2010].

[10] S. Kamper, On the appropriateness of Petri Nets in model building and simulation, Systems Analysis Modelling Simulation 8 (9) (1991) 689–714.

[11] W. Kreutzer, System simulation – programming styles and languages, Addison-Wesley, Sydney, 1986.

[12] F. Kuo, Managerial intuition and the development of executive support systems, Decision Support Systems 24 (2) (1998) 89–103.

[13] P. Lefrancois, B. Montreuil, An object-oriented knowledge representation for intelligent control of manufacturing workstations, IIE Transactions 26 (1) (1994) 11–26.

[14] M.R.P. Barretto, L. Chwif, R.J. Paul, Combining the best of the two: an activity cycle diagram/condition speci<sup>fi</sup>cation approach, Proceedings, UKSIM 1999, Simulation Society, United Kingdom, 1999, pp. 93–98.

[15] J.H. Mize, H.C. Bhuskute, D.B. Pratt, M. Kamath, Modelling of integrated manufacturing systems using an object-oriented approach, IIE Transactions 24 (3) (1992) 14–26.

[16] T. Murata, Petri Nets: properties, analysis and applications, Proceedings of the IEEE 77 (4) (1989) 541–580

[17] P. Ninios, K. Vlahos, D.W. Bunn, OO/DEVS: a platform for industry simulation and strategic modelling, Decision Support Systems 15 (3) (1995) 229–245.

[18] C.A. Petri, Kommunikation mit Automaten. PhD thesis, Institut für instrumentelle Mathematik, Bonn, Germany, 1962

[19] M. Pidd, Computer simulation in management science, 4th ed.Wiley, Chichester, 1998.

[20] M. Pidd, Tools for thinking – modelling in management science, 2nd ed. Wiley, Chichester, 1999.

[21] W. Pracht, Model visualization: graphical support for DSS problem structuring and knowledge organization, Decision Support Systems 6 (1990) 13–27.

[22] D.B. Pratt, P.A. Farrington, C.B. Basnet, H.C. Bhuskute, M. Kanath, J.H. Mize, The separation of physical, information, and control elements for facilitating reusability in simulation modeling, International Journal of Computer Simulation 4 (3) (1994) 327–342.

[23] L. Recalde, M. Silva, J. Ezpeleta, E. Teruel, Petri Nets and manufacturing systems: an examples driven tour, Lecture Notes in Computer Science 3098 (2004) 742–788.

[24] S. Robinson, Simulation – the practice of model development and use, Wiley, Chichester, 2004.

[25] S. Robinson, Conceptual modelling for simulation Part I: de<sup>fi</sup>nition and requirements Journal of the Operational Research Society 59 (3) (2008) 278–290.

[26] J. Ryan, C. Heavey, Process modeling for simulation, Computers in Industry 57 (1) (2006) 437–450.

[27] J.P. Schippers, Een <sup>fl</sup>exibel simulatiemodel ten behoeve van de evaluatie van diverse besturingsalgoritmen voor de supply chain van een margarinefabriek, Technical Report, University of Twente, The Netherlands, 19958, (in Dutch)

[28] L. Schruben, E. Yucesan, Modeling paradigms for discrete event simulation, Operations Research Letters 13 (1993) 265–275.

[29] E. Smith, D. Medin, Categories and Concepts, Cambridge University Press, Cambridge, 1981.

[30] E.C. Valentin, A. Verbraeck, Requirements for domain speci<sup>fi</sup>c discrete event simulation environments, in: M.E. Kuhl, N.M. Steiger, F.B. Armstrong, J.A. Joines (Eds.), Proceedings, 2005 Winter Simulation Conference, IEEE, Piscateway, New Jersey, 2005, pp. 654–663.

[31] W.M.P. van der Aalst, Timed Coloured Petri Nets and their Application to Logistics, PhD thesis, University of Eindhoven, The Netherlands, 1992

[32] W.M.P. van der Aalst, Putting high-level Petri Nets to work in industry, Computers in Industry 25 (1994) 45–54.

[33] J.G.A.J. van der Vorst, S. Tromp, D.J. van der Zee, Simulation modelling for food supply chain redesign – integrated decision making on product quality, sustainability and logistics, International Journal of Production Research 47 (23) (2009) 6611–6631.

[34] D.J. van der Zee, Developing participative simulation models – framing decomposition principles for joint understanding, Journal of Simulation 1 (3) (2007) 187–202.

[35] D.J. van der Zee, Building insightful simulation models using formal approaches – a case study on Petri Nets, in: M.D. Rossetti, R.R. Hill, B. Johansson, A. Dunkin, R.G Ingalls (Eds.), Proceedings, 2009 Winter Simulation Conference, IEEE, Piscateway New Jersey, 2009, pp. 886–898.

[36] D.J. van der Zee, J.G.A.J. van der Vorst, A modeling framework for supply chain simulation – opportunities for improved decision-making, Decision Sciences 36 (1) (2005) 65–95.

[37] D.J. van der Zee, J.G.A.J. van der Vorst, Guiding principles for conceptual model creation in manufacturing simulation, in: S.G. Henderson, B. Biller, M.-H. Hsieh, J. Shortle, J.D. Tew, R.R. Barton (Eds.), Proceedings, 2007 Winter Simulation Conference, IEEE, Piscateway, New Jersey, 2007, pp. 776–784.

[38] D.J. van der Zee, A. Pool, J. Wijngaard, Lean engineering for planning systems redesign – staff participation by simulation, in: S.J. Mason, R.R. Hill, L. Moench, O. Rose (Eds.), Proceedings, 2008 Winter Simulation Conference, IEEE, Piscateway, New Jersey, 2008, pp. 722–730.

[39] K.M. van Hee, L.J. Somers, M. Voorhoeve, A modeling environment for decision support systems, Decision Support Systems 7 (3) (1991) 241–251.

[40] B.P. Zeigler, Theory of Modelling and Simulation, Wiley, New York, 1976.

[41] B.P. Zeigler, Object-oriented simulation with hierarchical, modular models, intelligent agents and endomorphic systems, Academic Press, London, 1990.

![](/api/attachments/MS2P8F7N/fulltext/images/cb12a445069876ece8ff5a527809e702126f9d1804493b5149c0e4e96b6eda88.jpg)

Durk-Jouke van der Zee is an associate professor of Operations at the Faculty of Economics and Business, University of Groningen, The Netherlands. He received his MSc and PhD in Industrial Engineering at the University of Twente, The Netherlands. He teaches in the areas of operations management and industrial engineering. His research interests includ simulation methodology and applications, simulation & serious gaming, manufacturing planning & control, and <sup>fl</sup>exible manufacturing systems. Publications of his work can be found in leading journals, such as Decision Sciences, International Journal of Production Research, International Journal of Production Economics, Journal of Simulation, IIE Transactions, and Transportation Research B.
