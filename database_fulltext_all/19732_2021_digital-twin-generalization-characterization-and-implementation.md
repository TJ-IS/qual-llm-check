---
otero_id: 19732
otero_key: "FKSTU4N3"
title: "Digital Twin: Generalization, characterization and implementation"
authors: "Eric VanDerHorn; Sankaran Mahadevan"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113524"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Digital Twin: Generalization, characterization and implementation

![](/api/attachments/FKSTU4N3/fulltext/images/073ee751aa9266cbce430eebdf9c39d13592f8b70e3845ca8de13e99bdbd6d17.jpg)

Eric VanDerHorn <sup>a,b</sup>, Sankaran Mahadevan

<sup>a</sup> Department of Civil & Environmental Engineering, Vanderbilt University, Nashville, TN 37235, USA

<sup>b</sup> American Bureau of Shipping, Houston, TX, USA

## A R T I C L E I N F O

Keywords: Digital Twin Decision making Virtual representation Model updating Information fusion

## A B S T R A C T

Digital Twin is one of the promising digital technologies being developed at present to support digital trans formation and decision making in multiple industries. While the concept of a Digital Twin is nearly 20 years old, it continues to evolve as it expands to new industries and use cases. This has resulted in a continually increasing variety of definitions that threatens to dilute the concept and lead to ineffective implementations of the tech nology. There is a need for a consolidated and generalized definition, with clearly established characteristics to distinguish what constitutes a Digital Twin and what does not. This paper reviews 46 Digital Twin definitions given in the literature over the past ten years to propose a generalized definition that encompasses the breadth of options available and provides a detailed characterization which includes criteria to distinguish the Digital Twin from other digital technologies. Next, a process and considerations for the implementation of Digital Twins is presented through a case study. Digital Twin future needs and opportunities are also outlined.

## 1. Introduction

Digital twin technology is part of the rise of new digital technologies that support digital transformation by providing capabilities to enable new business models and decision support systems. Many organizations have already incorporated or are in the process of incorporating data, information, and analytics capabilities as part of their service offerings [1]. Similar to other digitalization concepts, such as the internet of things (IoT), cloud computing, machine learning/artificial intelligence, and augmented reality, the Digital Twin concept has seen increasing interest in recent years in both academia and industry as indicated by the growth of publications, articles, and commercial marketing. The existing literature highlights many of the potential and perceived ben efits of the Digital Twin concept, including reducing costs [2–4] and risk [5]; improving efficiency [6], improving service offerings [7,8], security [9], reliability [10,11] and resilience [12]; and supporting decision making [13–15]. However, the literature is lacking a consistent pre sentation of what the Digital Twin is and how it can be applied to sup port an organization’s operations. In fact, the varied use cases to which the Digital Twin has been associated with have resulted in a wide variety of definitions and frameworks across the industry causing confusion that risks weakening the concept and limits its ability to achieve the stated benefits. To reduce the confusion and unreasonable expectation sur rounding this technology, there is a need for a generalized and consolidated definition of a Digital Twin as well as a characterization of elements of the concept to provide a clear classification of what con stitutes a Digital Twin, distinguishing it from other similar digital technologies.

It is also noted that most of the current Digital Twin literature focuses primarily on technical approaches, analysis methodologies, and the challenges associated with data collection and integration into the Digital Twin. There is a need for examples of practical implementations of Digital Twins that consider the implementation strategies and deci sion support to achieve targeted outcomes with measurable benefits. A strategy for implementing Digital Twins must also consider the current technical and cultural challenges that prevent Digital Twins from real izing their desired benefits. Finally, Digital Twins require the incorpo ration of a variety of different enabling technologies, whose technical maturity and development must also be considered.

This paper evaluates the status of Digital Twins as part of a family of digitalization efforts intended to enhance existing processes and support new services. The contributions of the paper are as follows. First, existing Digital Twin definitions are reviewed and a consolidated defi nition and description of the key characteristics of the Digital Twin is provided (Section 2). Next, the approach and considerations for the implementation of Digital Twins for practical applications are discussed (Section 3). The implementation approach and related considerations are then demonstrated through an industry case study (Section 4).

Finally, current Digital Twin implementation challenges and future needs and opportunities for further development are discussed (Section 5). Section 6 provides concluding remarks.

## 2. Digital Twin definition and characterization

The concept of a Digital Twin originates from Michael Grieves’ 2003 presentation on product life-cycle management based on his work with John Vickers [4]. Grieves and Vicker’s motivation for developing the concept was to shift from the predominantly paper-based and manual product data to a digital model of the product which would become foundational for life-cycle management. Similar concepts such as Cyber Physical Systems (CPS) [16] and Internet of Things (IOT) [17] all focus on the idea of connecting a physical system to data collection, compu tational and/or communication systems, but approaching it from differing perspectives: CPS concept from the system engineering and control perspective, IOT from a networking and IT perspective, and Digital Twin from a computational modeling (machine learning/artifi cial intelligence) perspective.

Grieves provided the first characterization of the Digital Twin concept by stating that it consisted of three components, a physical product in Real space, a virtual representation of that product in the Virtual space, and the connections of data and information that tie the virtual and real products together [4]. Over the past two decades, the interest in Digital Twins has grown across many industries and this has led to a wide variety of definitions and characterizations that has diluted Grieves’ original description, to which this paper seeks to return and generalize.

## 2.1. Digital Twin definitions in the literature

An overview of some of the varied lexicon found in the literature is presented in Table 1, based on 46 different definitions found in the literature. Due to space limitations, these various definitions are not listed here, but are provided in GitHub via the link (https://github. com/evanderhorn/DSS\_DT\_Public). In addition to providing a concise statement of what a Digital Twin is, most of the available definitions also include descriptions of selected specific attributes of the Digital Twin, including: representation fidelity, data collection/exchange, synchro nization frequency, and model/simulation capabilities. These defini tions also occasionally include references to the specific use case being considered and the lifecycle phases that apply. After reviewing the breadth of definitions in the literature, a consolidated and generalized definition for a Digital Twin is proposed here as “a virtual representation of a physical system (and its associated environment and processes) that is updated through the exchange of information between the physical and vir tual systems.” This definition is general enough to encompass the 46 reviewed definitions provided in https://github.com/evanderh orn/DSS\_DT\_Public, yet it restricts itself to only the essential elements while avoiding use case-specific Digital Twin characteristics or terminology.

Table 1  
Proposed lexicon vs alternate lexicons.

<table><tr><td>Proposed definition lexicon</td><td>Alternate lexicons used in the literature</td></tr><tr><td>Virtual Representation</td><td>digital, cyber, computerized, computational, living, system model, simulation, counterpart, copy, mirror, part product, instance, substitute, information, clone, description, replication</td></tr><tr><td>Physical System</td><td>physical, real/real-world system, product, object, artifact, production lines, item, world, counterpart, device, parts, twin, entities, element, process state, vehicle, aircraft, structure, asset, component, instance</td></tr><tr><td>Updated</td><td>update, integrate, incorporate, include, synchronization, adapts, reflects, mirror, reflect</td></tr><tr><td>Exchange Information</td><td>connections, communication, collecting data, sensor updates, fleet history, physical knowledge, flight histories, fatigue damage, data space, performance, maintenance, health status</td></tr></table>

The terminology choices for this proposed definition for a Digital Twin can then be reviewed in relation to the terminology used in the other definitions found in the literature. This comparison is focused on the three key components of the proposed definition: virtual representa tion, physical system and updated through the exchange of information.

As mentioned earlier, many of the definitions in the literature combine a definition with specific characterizations about Digital Twins that are unique to the use case(s) that they are describing. Much of the confusion surrounding the Digital Twin concept appears to be in the qualifiers on certain characterizations which are used to designate what constitutes a Digital Twin and what does not. The following sub-sections provide a generalized overview of these characterizations which covers the breadth and variety of descriptions and use cases provided in the literature.

## 2.2. Digital Twin characteristics

Using the generalized definition proposed above, the Digital Twin can be characterized by three primary components: (1) A physical re ality, (2) a virtual representation, and (3) interconnections that ex change information between the physical reality and virtual representation shown in Fig. 1.

The following sub-sections discuss these three components in further detail.

## 2.3. Physical reality

In the Digital Twin literature, a wide variety of terminology has been used to describe the physical reality of interest and the selected termi nology is often domain specific. The term physical reality is proposed here as it is the most general form to represent what may be attempted to be modeled, since physical reality encompasses the entirety of the sys tem, both known and unknown. The physical reality can be decomposed into the physical system, the physical environment, and physical processes.

## 2.3.1. Physical system

The physical system consists of the group of interacting and inter related entities that form a unified whole [18]. This group of entities is often described by its structure or purpose and delineated from other systems by boundaries in space and time. The selection of the boundary often takes advantage of natural segregations associated with the more typical meaning of the word system. For example, the physical system of interest can range from a single machinery part, sub-component or component, to a complete piece of machinery, to a machinery system, to all of the interconnected systems of a single asset. It can be seen that generally, the physical system of interest is man-made, but as the concept of Digital Twin expands to other domains, such as healthcare [19] and agriculture [20], the physical system of interest may be some aspect of the natural environment or the human body.

## 2.3.2. Physical environment

The physical environment is where the physical system of interest resides. The physical system is surrounded and influenced by its physical environment and interacts with the environment through physical pro cesses. The delineation between the physical system and physical environment is often determined based on each specific Digital Twin application. In some applications, this delineation may be simple, but in others it may be complicated. An example of a simple delineation case is the Digital Twin of a manufacturing process such as additive manufacturing. In this case, the physical system of interest is the 3D printer, and the physical environment includes relevant external influences on the process such as room temperature, air flow, ambient vibration, etc. In an example of a more complicated delineation case, the physical system of interest may be a single room in a large building, and the physical environment may include other parts of the building, such as adjacent rooms, ventilation systems, etc. as well as other external factors that impact the building as a whole, such as weather, etc. In many applications, both the physical system and the physical environ ment will be represented in the virtual space. This means that data fo the relevant environmental parameters will be collected from the physical environment and stored in the virtual representation similar to that of the physical system. This allows the physical environment to be reconstructed in the virtual space to allow for simulations, forecasts, and/or decisions to be made which will impact the physical system of interest.

![](/api/attachments/FKSTU4N3/fulltext/images/f3242942592295d6b0a8dbe3a70e0140593065bf826654bb14279a28e31c8696.jpg)  
Fig. 1. Digital Twin components and high-level processes.

## 2.3.3. Physical processes

Physical processes are how the system expresses itself in the physical environment and is the mechanism by which the entities of the system undergo changes in state. For example, in the case of manufacturing, some of the physical processes of interest may include casting, forging, welding, etc. For asset lifecycle management, the processes of interest may be loading processes based on the system’s operation in the envi ronment or degradation processes which can result in the physical sys tem states changing over time. Similar to the physical system and physical environment, the physical processes may also be represented in the virtual space to support simulations, optimization, and forecasting.

## 2.4. Virtual representation

As presented in Table 1, the Digital Twin definitions in the literature use a variety of terminology to discuss the virtual representation. This paper proposes using the term virtual representation as this captures the idea that the entity in the virtual space is merely a representation of an idealized form of the physical reality.

## 2.4.1. Idealized representation of physical reality

It is recognized that any attempt to model the physical reality re quires the idealization of that reality based on some level of abstraction. These idealizations often take the form of data models (data structures) and/or behavior models (mathematical or computational models). A data model here refers to a data structure that retains all the variables describing the reality at the level of abstraction chosen. Behavior models refer to the computational models that describe the how the variables of interest relate to each other. In engineering applications, behavior models are often based on the laws of physics; however, the exact physics that describe the relationships between variables may not al ways be known and use of data-driven models to describe the relation ships between different variables is becoming more prevalent. Reality is then represented in this idealized form by assigning values to the model variables based on the interpretation of the data collected from the physical reality.

The decision on the level of abstraction must be consistent with the intended use case(s) as it will impact data collection processes as well as introduce uncertainty. Due to the abstraction of reality, the evidence collected about that reality must be transformed into data consistent with the virtual representation of the idealized reality. The process by which the data consistent with the idealized representation gives evi dence about reality is called the interpretation process and is shown in Fig. 2.

## 2.4.2. System states and parameters

When describing the types of data and information that are to be managed by the virtual representation, a wide range of terms may be considered, including properties, parameters, states, attributes, character istics, features, variables, and dimensions. As noted earlier, the meaning and use of these terms is often dependent on the technical domain in which they are being referred. A primary motivation for the use of a Digital Twin in many applications is the monitoring of the system as it changes over time. Tracking and modeling these changes within the virtual representation as a function of inputs to the system enables the representation and estimation of past, present, and future behavior to guide decision-making. These objectives align closely with the concept of state space modeling in system identification and as discussed below, state estimation is a common methodology used in the exchange of in formation between the physical reality and the virtual representation. Therefore, in this paper, we propose adopting the terminology used for state space modeling which uses the terms states and parameters to describe the information managed by the virtual representation [21].

In state space modeling terminology, states refer to the aspects of the system that evolve through time based on their previous values and inputs to the system (often externally imposed by the system’s interac tion with the environment). Monitoring the states of the system there fore provides the history of how the system is behaving over time. The term parameters in state space modeling is used to refer to the aspects of the system model that describe how inputs to the system affect the states and how the different states relate to each other over time. In many cases, system parameters remain fixed or are slowly varying over time. Defining the states and parameters for a specific Digital Twin repre sentation is determined by the level of abstraction selected for the idealized representation. This information includes information about the system itself, in addition to its environment and associated processes.

Note that while the system states and parameters retained in the virtual representation provide an idealized representation of the phys ical reality, not all this information is readily exchanged between the physical reality and the virtual representation. This is because not all system states can be directly measurable with available inspection methods, due to limitations of either technology or economics. For example, the state of fatigue damage accumulation may be of interest, but crack initiation is not feasible to monitor, especially in large struc tures. In such cases, the values for these states are assumed based on data not directly associated with the current physical reality of interest (e.g. historical data, design data, etc.) or inferred from the observed data using state estimation. In the example of representing fatigue damage accumulation, measured states, such as structural motion and strain using sensors, can be used in combination with computational models to infer the fatigue damage state. Some of the unobservable system infor mation may also include the system parameters which must be inferred through parameter estimation. This process of determining which states to directly monitor and which states to infer is an important part of the Digital Twin scoping and implementation process.

![](/api/attachments/FKSTU4N3/fulltext/images/c8dbbf761060b13699271b87e89059304c0bf94f0ada46218c95202db40cce2f.jpg)  
Fig. 2. Data abstraction process.

## 2.4.3. Virtual system

The primary component of the virtual representation is the virtual system. The virtual system contains the data and models of the entities of interest from the physical system at a chosen level of abstraction. It is important to note that the virtual system may contain multiple models of the physical system at different levels of abstraction and these models may or may not interact with each other. An example of interaction is aeroelasticity analysis of an airfoil, where the results of the aero dynamics model may be used as input to the structure model and vice versa (two-way coupling).

## 2.4.4. Virtual environment

Like the virtual system, the virtual environment is the virtual rep resentation of the physical environment. Similar to above, the virtual representation of the physical environment is at a chosen level of abstraction.

## 2.4.5. Virtual processes

Virtual processes describe how the virtual system expresses itself at the level of abstraction chosen for the virtual representation. The most common form this takes is a computational model of the corresponding physical processes. These computational models to represent how the physical system undergoes state changes to help generate the insights required to support decision-making.

The computational models used to accomplish this are built based on the relationships established between the inputs and outputs of a given process that changes the system states (e.g. load application and system dynamics, degradation mechanisms, etc.). The relationships between the inputs and outputs of these processes are determined based on known physics or generated via data-driven models using input and output data, or a hybrid of both. Machine learning (ML) and artificial intelligence (AI) techniques can be used to establish simulation models for processes based on the collected data without knowing the specific model form (i.e. a “black-box” model).

Virtual processes play a valuable role in the Digital Twin, as many of the use cases rely on simulated future states rather than the present system state. These include diagnostics and prognostics [10,12,14,22–24], design verification [25], simulation and optimization [2,4,13,22,26–29], and “what-if” scenario and sensitivity analyses [26]. The application of virtual processes on the virtual system alters the virtual system states in a manner similar to how the physical processes alter the states in a physical system. This allows the user of the Digital Twin to hypothesize how the physical system would perform under similar physical processes, thus helping to decide what actions to un dertake based on whether the simulated outcomes are aligned with the desired outcomes.

## 2.5. Interconnection between physical and virtual

The final component of the Digital Twin definition is the interconnection between the physical reality and the virtual represen tation where data/information is exchanged in two directions: physicalto-virtual and virtual-to-physical [30].

## 2.5.1. Physical-to-virtual connection

The physical-to-virtual connection enables the process by which data collected from the physical reality is used to update the states main tained in the virtual representation. In general, the physical-to-virtual connection requires three steps: the process of collecting the relevant information including the direct measuring of the physical reality, interpreting the collected data to a form that is consistent with the level of abstraction and the updating process that uses the data to update the states of the virtual representation.

In the first step, when discussing data collection for the Digital Twin, the Internet of Things (IoT) and sensor technology are commonly referenced [20,31–33]. While not strictly required for a Digital Twin, these technologies are often credited with supporting the increased in terest in Digital Twins since they allow for a larger amount and fre quency of measurements. It is important to note that offline and manual data collection means are also relevant in this context, such as visual inspection, non-destructive evaluation, repair logs, etc.

The second step of the process, interpretation of the collected data (Fig. 2), may typically contain several steps depending on the data, including data processing, data curation and data conversion. An example of this is the conversion of voltage changes in a strain gauge to strain measurements, but a more abstract representation may need further interpretation, for example converting the strain measurements to load cycle counts.

The third step of the process is the use of data to update the states of the virtual representation. In the simplest cases, the measured data corresponds exactly to a state maintained in the virtual representation and the virtual representation is updated such that it reflects the observed physical system state. In many cases, updating of the unob served system states of interest and the model parameters is achieved through the techniques of system identification, which may also involve information fusion, i.e., use of data from multiple sources.

## 2.5.2. Information fusion

The concept of information fusion is focused on combining the multiple available sets of information to create a derived set of infor mation which reduces redundancy and uncertainty. Information fusion techniques can be classified into three categories: (i) data association, (ii) state estimation, and (iii) decision fusion [34]. For the virtual rep resentation update process, the state estimation techniques are of greatest interest, but data association may also be applied where it is necessary to reduce the dimensionality of a large volume of data. Data association and state estimation are part of the physical-to-virtual connection process. Decision fusion may be applied during the virtualto-physical connection process, where a consensus must be made from the outcomes of various analyses as to the actions that will be under taken to affect the states of the physical system of interest.

## 2.5.3. Virtual-to-physical connection

The virtual-to-physical connection is the process that results in the transfer of information from the virtual representation back to the physical reality. This connection closes the loop in the Digital Twin, by allowing the insights and decisions generated through the virtual rep resentation to be realized in the physical system; either through actions that result in a change in the physical system states or actions that collect additional information from the physical system to further update the virtual representation.

This information flow is realized in the physical reality by under taking specific actions which impact the physical process(es) that result in a change of the states of the physical system. As with the physical-tovirtual connection, this process occurs in two steps: (1) the virtual rep resentation is used to determine whether and what change in the physical state is required, and what action is required to achieve the targeted state; (2) then the required actions that impact the necessary physical process(es) are performed to achieve the targeted physical state.

Table 2 summarizes the above descriptions of various elements of a digital twin.

## 2.6. Digital Twin qualifiers

In the review of definitions provided in the literature, it was observed that several definitions included specific qualifiers for certain Digital Twin characteristics to designate what constitutes a Digital Twin and what does not. This section will review the qualifiers mentioned in the literature and then propose a clear set of qualifiers that distinguish Digital Twin from similar technologies while not being overly restrictive.

## 2.6.1. Digital Twin vs digital model

Descriptions of Digital Twins and their usage in the literature often sound similar to more traditional digital modeling approaches, such as computer-aided design (CAD), computer aided engineering (CAE), and product lifecycle management (PLM) tools, which lead to confusion among practitioners as to what distinguishes a Digital Twin from these existing approaches. As these tools are also incorporated and used with Digital Twins, it can be challenging to determine when the use of these tools/models fits the definition of a Digital Twin and when it does not. The two key requirements for a Digital Twin that make it unique from traditional digital modeling approaches are that a Digital Twin repre sents a single instance of the system of interest (i.e. its corresponding physical twin) not a class or fleet of systems and that the Digital Twin updates its description of that system as it changes over time.

Table 2  
Summary description of digital twin components

<table><tr><td>Component</td><td>Description</td></tr><tr><td>Physical reality</td><td></td></tr><tr><td>Physical system</td><td>The portion of the physical reality chosen for modeling which includes all relevant interacting and interrelated entities that form a unified whole</td></tr><tr><td>Physical environment</td><td>The aspects of everything outside the selected physical system which affect that system</td></tr><tr><td>Physical processes</td><td>The functions being performed by the physical system that result in the system undergoing changes in state</td></tr><tr><td>Virtual representation</td><td></td></tr><tr><td>Virtual system</td><td>The data and computational models of the physical system of interest at a chosen level of abstraction</td></tr><tr><td>Virtual environment</td><td>The virtual representation of the physical environment for the physical system of interest</td></tr><tr><td>Virtual processes</td><td>The virtual representations of the corresponding physical processes, used to simulate how physical processes will affect the physical system; these are the primary means to generate insights to meet target outcomes</td></tr><tr><td>Information</td><td></td></tr><tr><td>Interconnection</td><td></td></tr><tr><td>Physical-to-virtual connection</td><td>The means by which information from the physical system is collected, interpreted, communicated and used to update the virtual representation states and parameters</td></tr><tr><td>Virtual-to-physical connection</td><td>The means by which an action is decided and undertaken based on the virtual representation to affect physical processes that result in change of the physical system&#x27;s states and parameters</td></tr></table>

## 2.6.2. Digital Twin vs simulation model

Simulation modeling is the process of using a digital prototype of a physical system to predict how the system will perform in reality [35]. Simulation models are often used during the design phase to understand how the system of interest will perform based on assumed operation, loads, degradation mechanisms, etc. This replication of physical system behavior in a virtual environment can sometimes lead to simulation models being mistaken as Digital Twins. The major difference between a simulation model and a Digital Twin is that the simulation model is predicting future states of a physical system based on a set of initial assumptions, rather than tracking current and past states of a single instance of the physical system. A Digital Twin would then track the actual experienced states as that specific instance of the system is used in operation.

A reason that simulation models may be confused with Digital Twins is that while a simulation model is not by itself a Digital Twin, the use of simulation modeling combined with Digital Twins is common. Often the computational models which are used to infer the current state of the Digital Twin are the same models which can be used in simulation to predict future states. This can be even more advantageous when the parameters of these computational/simulation models are updated to reflect the behavior of the specific instance the Digital Twin is repre senting. These simulation models can then be used to provide additional insights to guide decision-making for optimizing future operations, forecasting degradation mechanisms, and predicting future failures and remaining useful life.

## 2.6.3. Digital Twin vs surrogate model

Surrogate modeling is an engineering method that uses approximate models that are computationally cheaper, such as response surfaces, kriging, support vector machines, neural networks, etc. [36] to mimic the behavior of more computationally expensive physics models. It is likely that the confusion between surrogate models and Digital Twin arises from the similarity in how they both use data to update the knowledge about their form. Surrogate models are constructed using data-driven approaches that use a set of training data (inputs and out puts) from the original simulation model to construct a model that mimics the behavior of the original computational model; this approach is similar to ML/AI models.

Thus surrogate/ML/AI models are similar in concept to the way a Digital Twin uses data from the physical system to update its virtual representation. However, despite this similarity, a surrogate model alone is not a Digital Twin as it does not maintain a virtual represen tation of the states of an instance of a physical system but rather to create a mimicry of a computational model. While a surrogate model is not a Digital Twin, it could be used within a Digital Twin to improve its functionality when the original computational model is too timeconsuming to provide insights within a required decision interval.

## 2.6.4. Digital Twin data interconnection

Descriptions of Digital Twins in the literature often put further qualifiers on the data interconnection component. More specifically, to be considered a Digital Twin it is sometimes required that this data interconnection be online and bi-directional [37–40].

The requirement that the virtual-to-physical connection must result in a change in the physical system states is restrictive. While the insights generated from the Digital Twin should provide feedback that serves a targeted outcome, this outcome may not result in a physical state change. An example of such a use case is using a Digital Twin to prior itize and optimize inspection campaigns of large structures. Identifying the highest risk areas for targeted inspections based on the specific operation of this system increases the probability of detecting anoma lous conditions and reducing overall risk without resulting in a change of state of the physical system.

The second added requirement is that this data interconnection be online [37]. It is implied that online means that the data is exchanged automatically between the physical system and the virtual representa tion and vice-versa. The reason for placing such a requirement on the classification of Digital Twins is likely based on specific use cases. However, such a requirement is overly restrictive and does not account for the many different offline human-in-the-loop (HITL) interactions with the physical system, including data collection methods, such as physical inspection, NDE, maintenance logs, etc., and system repair/ maintenance actions that could be used to update the virtual represen tation of system states. Additionally, there are use cases where the im mediate exchange of information is not required for the decision-making process [14]. It is proposed that the requirement for a Digital Twin be that information be exchanged between the physical system and the virtual representation to update the virtual system states and parame ters. The bi-directional connection from virtual to physical may not al ways result in change in the physical state (e.g. the action could be additional inspection/data collection). Any additional requirements on how (or how often) this data is collected and exchanged should be determined based on the specific use case and implementation.

## 2.6.5. Digital Twin fidelity

Another common Digital Twin qualifier found in the literature is with respect to the fidelity of the Digital Twin virtual representation [10,11,37,41–45]. Many of these definitions argue for the Digital Twin to have the highest level of model fidelity feasible. As discussed earlier, the level of model fidelity directly relates to the level of abstraction of reality that is chosen for the virtual representation. While it is typically assumed that a higher fidelity model ensures that the physical system and virtual representation are more closely aligned, this assumption may not be the case if the data that can be collected from the system is not appropriate for the level of model fidelity. Observation and modeling uncertainties resulting from insufficient data may negate the benefits of the higher fidelity model. Even if the required data could be collected, additional challenges of a high-fidelity approach may also include data storage management, data transfer limitations, computa tional processing power, and turnaround time for decision support.

In addition to the practical limitations of applying a high-fidelity approach, using such a requirement to classify a Digital Twin is chal lenging as there is no accepted definition as to what would constitute a high-fidelity representation. From the reviewed literature it is found that the choice of Digital Twin modeling fidelity is primarily driven by the use case; and there are no papers in literature yet to present a Digital Twin implementation which could be considered high-fidelity. This further supports the argument that the level of model fidelity should not be used to define what is classified as a Digital Twin. The only requirement is that the model be a virtual representation of a specific physical system; the fidelity of that model will be dependent on the use case.

## 2.6.6. Data update frequency

The final commonly mentioned Digital Twin qualifier is the rate at which data is exchanged between the physical system and the virtual representation. As mentioned in the previous sections, information is exchanged bi-directionally between the physical and virtual spaces. An important component of this interconnection is the frequency at which information is exchanged between the physical space and virtual space. In the literature, this update is commonly described as being real-time [37,38] where changes in the physical state are updated in the virtual representation nearly instantly. While such a qualifier represents an ideal Digital Twin, allowing the physical system and virtual system to act nearly synchronous with each other, placing such a requirement on all Digital Twins is not practical with current technology and is not required for many of the use cases.

As different data streams may be available at different frequencies, the update process may occur as the different datasets become available or may be selected to occur at set intervals based on the use case and the frequency in which a decision will need to be made. For example, in [14], a Digital Twin for fatigue crack growth on an aircraft wing collected data during each mission, and state estimation was performed to update the virtual representation after each mission. This frequency was consistent with the decision-making interval for this use case where mission planning was desired on a flight-by-flight basis.

While real-time update of all the system states of interest is ideal, it i often not practical to define a Digital Twin by this requirement given varying frequencies of different data collection systems and HITL data collection efforts. The proposed approach is to instead implement a model updating process appropriate for the specific use case, which utilizes all the available system information at the time of the update to provide the inference of the current system states.

## 2.6.7. Summary of qualifiers

Distinguishing a Digital Twin from other digital modeling and simulation approaches is based on the following qualifiers:

1. The virtual representation represents a single instance of a physical system; and

2. Data/information from the physical system is used to update the states of the virtual representation over time.

Any additional requirements placed on specific characteristics of the Digital Twin, such as the examples provided in this section, should not be included in the definition; rather, they should be based on the specific use case being considered and established during the Digital Twin implementation.

## 3. Digital Twin implementation

Digital transformation is viewed as an enabler of more innovative, optimized, and effective products and processes and is a key component of Industry 4.0 [46]. The practical implementation of Digital Twins aligns with the concept of digital transformation, where a principal objective is the innovation of business models to reflect the value that can derived from data. Similar to the definition and characteristics of a Digital Twin, there is also a breadth and variety of technical elements that comprise a Digital Twin implementation that we seek to generalize. The key aspects of a Digital Twin implementation include specifying intended outcomes, scoping the solution (both defining the physical system of interest and levels of abstraction), creation of the virtual representation, and establishing required data interconnections.

A brief review of current industry implementations of Digital Twins can be generally grouped into three categories: Digital Twin component solutions, commercial off-the-shelf solutions, or custom hybrid combi nations. A large number of the marketed Digital Twin product offerings are component solutions, provided by companies that provide platform services, such as Microsoft [47], or by digital model/digital simulation companies, such as Ansys [48]. These providers typically market Digital Twin approaches that utilize components from their product offerings that can be combined together to create a customer-specific Digital Twin implementation but how the Digital Twin is constructed is left to the end user. This category of solutions has also led to collaborations between companies to enable easier integrations between their capabilities as customers seek functionality that may not be wholly available within a single solution providers product portfolio. The next most common category is off-the-shelf Digital Twin solutions. These are typically provided by the original equipment manufacturer (OEM), such as GE [49], for common industry uses cases. The final group are completely custom hybrid approaches, where the end-user constructs their own solution, usually from a combination of commercial and custom prod ucts. The extent of the industrial application of a hybrid approach is challenging to estimate since it is for an organization’s internal use, however this case may be the most effective at achieving specific outcomes, since the capabilities can be wholly customized to a specific use case and the features can be implemented incrementally based on evaluated cost and business value.

## 3.1. Digital Twin outcome identification

Colin Parris, Vice President of Software Research at the GE Global Research Center, described a Digital Twin as “a living model that drives a business outcome” [32]. Identifying the intended outcomes enables the scope of the Digital Twin to be realistically bounded to achieve these outcomes. The targeted outcomes should be measurable and quantifi able, which allows for the value proposition for a Digital Twin to be defined by its ability to result in a positive change toward the targeted outcomes. These outcomes can be wide-ranging and industry-specific; some common outcomes associated with Digital Twins include including reducing costs [2–4] and risk [5], improving efficiency [6], improving service offerings [7,8], security [9], reliability [10,11], resilience [12], and supporting decision-making [13–15].

## 3.2. Digital Twin scope

When designing the Digital Twin, the principle of parsimony should be observed to ensure that the determined scope can meet the intended outcomes without adding additional complexity or cost that might compromise its feasibility. While Digital Twins may theoretically be used to represent the chosen system to an atomistic level of resolution, the intended application and desired outcomes determine the rationale by which to select the appropriate scope and abstraction level of the Digital Twin.

The first aspect of setting the scope for the Digital Twin is deter mining the portion of the physical reality that will be modeled, which sets the boundary between the physical system of interest and its sur rounding physical environment, as described in the previous section. This boundary should be selected to ensure the appropriate level of detail to achieve the targeted outcomes while minimizing the resulting model complexity.

The second aspect of setting the Digital Twin scope is determining the required level of abstraction. The level of abstraction determines the collection of physical system states that are to be modeled and main tained. The selected level of abstraction also determines the fidelity of the computational models that are to be used. Considering the principle of parsimony, the level of abstraction/model fidelity should be only as detailed as required to achieve the targeted outcomes. Refer to Section 2.6.4 for further discussion.

When scoping the Digital Twin implementation, consideration could be given to supporting models at varying levels of abstraction, allowing the users to switch between the levels as needed to achieve the targeted outcomes. Consideration should also be given to the varying time con stants for the different physical processes being modeled. For example, vibration is typically measured on the order of milliseconds and corro sion is often measured on the order of years. For this to be managed, the Digital Twin must often support models of different levels of abstraction, while ensuring that the shared system states between models of different levels of abstraction remain consistent.

## 3.3. Digital Twin virtual representation

The first element of the virtual representation is creation of the data models. The states of interest, both current and historical, are retained in the data models. In the literature, when discussing data management, cloud computing environments are mentioned [3,41,44]. A cloud-based data management system provides advantages in accessibility, scalable data storage and processing power, and efficient data transfer. Local data storage systems may also be used and may be required in cases where security of the data is a concern. Practical implementations may consider combinations of local and remote data management approaches (edge, mainframe, fog and cloud). Further, data visualiza tion may often be used in conjunction with data models to provide additional insight into the data. The purpose of these visualizations is to represent the raw data in a format that supports more efficient decisionmaking and may include simple statistics, summary data, and data tagged to visual representations of the system of interest.

The second element of the virtual representation is the imple mentation of the relevant computational models. The use of models in Digital Twins is generally for two purposes: the inverse problem and the forward problem. The first is the data fusion and system identification process where states and parameters of the Digital Twin must be esti mated using the observed information (i.e., inverse problem). The sec ond purpose (i.e., forward problem) is to apply virtual processes to the virtual system to simulate how the system states will change based on forecasted changes in the physical environment or the application of physical processes (e.g., loading on a structure). The goal of these sim ulations is to result in action decisions which are transferred from the virtual space to the physical space to result in physical system state changes that support the outcomes. As discussed earlier, computational models can be categorized as either physics-based models or data-driven models, and the selection of the appropriate model is dependent on the available data/information collected from the physical system and the known relationships between the collected data and the states of interest that cannot be directly measured.

In addition to the data models and computational models, visuali zation is a critical aspect of the Digital Twin implementation, in order to provide the decision-maker with a clear interpretation of the data to provide confidence in the decision. Also, visualization tools serve to improve the overall acceptance of the Digital Twin and demonstrate its value to the organizational leadership and non-domain experts.

Since there are very few end-to-end Digital Twin solutions currently available in the market and given the breadth of Digital Twin applica tions and the variety of technologies a Digital Twin employs, it is likely that a hybrid approach that combines custom Digital Twin data man agement systems that can be easily connected to COTS tools will be applied. For this approach to succeed, there will need to be an ongoing effort to facilitate more efficient and consistent data exchange, sup ported by future standards. This has been recognized in the industry and such efforts are currently ongoing [50].

## 3.4. Digital Twin data interconnections

The implementation of Digital Twin data interconnections requires decisions regarding how data is to be collected, the frequency at which the data is collected, and how the data is exchanged between the physical and virtual spaces.

After the Digital Twin creation, ongoing data collection for Digital Twins largely focuses on sensor technology. However, as previously mentioned, offline data collection is also relevant, including inspections and NDE. Further heterogenous data may also be available from log books, maintenance records, pictures/video, subject matter expert opinions, etc. The required technology and processes to collect, process and fuse these data sources should be considered during implementation.

The next aspect of the data interconnection is the frequency at which data is collected and exchanged, also known as the Digital Twin update frequency. This is often driven by the decision interval, which is defined as the time scale on which a decision needs to be undertaken. In cases of operational decision making, the decision interval may be on the order of seconds or minutes, however for asset integrity management cases, the decision interval may be on the order of months or years. It should also be noted that there also may be cases where sensor data is collected at a high frequency, but it is only exchanged with the virtual represen tation on a periodic basis in batch format due to data transfer limitations.

A final consideration is the technology and processes that need to be implemented to support the virtual-to-physical connection. As noted earlier, this exchange may be through the use of the Digital Twin to control actuators in the physical space that result in the states of the physical system changing. Similar to the physical-to-virtual intercon nection, this requires establishing the required data exchange processes and control systems that allow for the Digital Twin to enact the specified actions. Another approach is the use of HITL to use information/insights from the Digital Twin to lead to physical actions which either result in a physical state change or in the collection of additional information from the physical system. In these cases, consideration must be given to existing processes. As the implemented Digital Twin should by design align with these processes, the information exchange and decisionmaking points in the process need to be identified. Once these points are identified, the mechanism by which the information is to be exchanged and the procedures for making decision based on this infor mation should be codified.

## 4. Digital Twin implementation case study

The proposed implementation process is demonstrated through a case study where a Digital Twin is developed to support the ongoing asset integrity management of a naval vessel.

## 4.1. Digital Twin outcomes

It was observed that prescriptive scheduled inspections of the ves sel’s structure often resulted in finding unexpected structural issues that were leading to extended drydock stays resulting in higher costs and reduced mission availability [51]. Based on these observed challenges, the primary outcomes of the Digital Twin implementation are an in crease in the operational availability and a reduction in the associated operational expenses over the life of the asset.

Additionally, secondary outcomes include the reduction of risk associated with emergency response situations where detailed engineering analysis, such as Finite Element Analysis (FEA), is required to answer stakeholder questions before any resumption of operations and the extension of the vessel’s life beyond its original intended design life [51].

## 4.2. Digital Twin scope

Based on the targeted outcomes, the physical system to be repre sented as a Digital Twin is selected to be the hull structure of the vessel. Based on this selection, the corresponding physical environment that is of interest is the local wave environment and local weather environment that the vessel operates in. The physical processes of interest include the loading processes (e.g. wave loads, thermal loads, and cargo loads) and degradation processes (e.g. coating breakdown, corrosion, and struc tural fatigue).

The fidelity of the Digital Twin was maintained at several different levels of abstraction within several data models and computational models based on their intended use. For example, a lower fidelity compartment-based model, shown in Fig. 3, was used for recording the asset condition during visual inspections. The condition and the pres ence of any anomalies are tagged to the relevant compartment and the database supports the storage of accompanying supporting information, such as written reports and pictures. These results are then tagged directly to the relevant structural components in a higher fidelity data model maintained onshore. The higher fidelity model can then be used to generate computational models, such as finite element analysis (FEA) models at varying levels of fidelity based on the analysis requirements. In this use case, the term model fidelity refers to the level of detail at which the structural components are represented. For example, at the lowest level, only the boundaries of each of the structural compartments are represented. At the highest level, every structural component down to an individual bracket is modeled.

The vessel initially had very few sensors available for monitoring the hull structure, so this limited the fidelity of several of the computational models, particularly the loading models. Other data sources were used in combination with computational models to infer the vessel response to the experienced wave conditions and determine the resulting stresses at representative critical areas.

## 4.3. Digital Twin virtual representation

It was determined that no available solution could achieve the tar geted outcomes, so a hybrid approach was adopted which required the integration of several different solutions for both the data models and computational models. It was also recognized that an incremental implementation approach should be adopted to reduce the upfront implementation costs and identify where incremental enhancements to the Digital Twin, both in terms of scope and fidelity, would be best applied to achieve the targeted outcomes. For this use case, a series of data models and computational models were implemented to represent both the system and its corresponding environment.

First, the data model for the virtual system representing the struc tural condition was selected as a CAD-based system that had been optimized for managing marine inspection data. This model also pro vided the necessary fidelity to support all the other planned data models and computational models. The advantage of the selected system is that it also included the lower fidelity compartment-based model for use in the field to collect inspection data. The advantage of using a lowerfidelity model for data entry in the field is the reduced computational requirements for loading and running the model, and the easier data entry, since information is tagged based on the compartment the inspector is in rather than having to tag it to the specific structural component. This aligns with existing inspection processes, and any findings during the inspection can be tagged to the specific structural components in the high-fidelity model by engineers in the office. These two models operate on a shared database, so that inspection results and anomalies tagged in one model are also represented in the other model at the appropriate fidelity which also ensures that the Digital Twin virtual representations remain in synch as a single representation instance.

![](/api/attachments/FKSTU4N3/fulltext/images/7d5d3f0bbf259bcdc1f833eb088d5caedbe3a606a91706187fd2206ebf1329c7.jpg)

![](/api/attachments/FKSTU4N3/fulltext/images/34e154fa01ee975b7b38a338c8ab2f6fb3c3281c887986f572e644f61f2e30d4.jpg)  
Fig. 3. Example Digital Twin models: a) low-fidelity compartment model, b) high-fidelity structural component model

In addition to the data models, two computational models were implemented as part of the virtual system. The first was a set of FEA models, including a full-ship model and several local models of critical connections. These models are linked to the high-fidelity condition data model, so that the relevant properties can be updated as the condition changes. The results of the computational models can also be fed back to the condition data model if an anomalous condition is determined from the analysis. The other computational model is the hydrodynamics model, which is used to determine the vessel response to specific wave conditions.

As previously mentioned, there were limited sensors installed aboard the vessel so the vessel response to the environment could not be measured directly. As an alternative, use of location analytics (LA) in tegrated with non-location analytics (NLA), is employed enable spatial modeling of the vessel’s environmental exposure [52]. A data model of the vessel’s GPS position information is fused with wave exposure data from hindcast weather models. By creating a virtual representation of the corresponding environment, this data can be used with the compu tational models in the virtual representation to determine the resultant loading and impact on the structure.

The final models are the degradation process models, which provide virtual representations of the physical degradation processes, particu larly coating breakdown, and corrosion. These models are data-driven models which use machine learning to update the computational model parameters based on the observed data. Developing vesselspecific degradation models is useful in providing forecasts of the future structural condition to be used in determining inspection and repair intervals.

## 4.4. Digital Twin data interconnections

The final component of the implementation is the set of data in terconnections. The first interconnections are the ship-to-shore data exchanges for the limited sensor data and the inspection data collected in the low-fidelity data model. Ships often have limited bandwidth to exchange data, so it is often batched ashore during port visits. A data base replication is performed during these batch data exchanges to ensure that the shore-based and ship-based databases are synchronized.

The second set of interconnections is the collection of data from third party sources for tracking the position and weather information. This data is collected daily and stored in a shore-based database.

The final data exchange is the digitizing and entry of HITL data. Some of this data is captured and digitized when it is input to the low fidelity data model. However, other sources, such as thickness mea surements are collected by third-party contractors and must be digitized and entered manually in the data model. To reduce the level of manual effort, the data model can be used to generate a thickness measurement plan that is provided to the third-party contractor. After data is input to the provided plan, it can be automatically mapped back into the data model, significantly reducing the manual effort.

## 4.5. Initial results and next steps

One challenge in evaluating Digital Twins is quantifying their value. This is often because they align with an existing process that may pro vide a majority of the business value and the advantage the Digital Twin provides is the digitalization of that process to provide further efficiency or automation. Also, part of the benefit provided by a Digital Twin is as a type of insurance, reducing risks and costs during emergency scenarios which may only occur in rare instances. Finally, as a Digital Twin is intended for use during the entire life of the asset, the accumulated benefits may take time to observe and quantify.

In this case study, while the implementation has not been in use long enough to confirm that the primary outcomes are being achieved, the Digital Twin implementation has been successful in supporting the resolution of an observed structural design deficiency. The availability of the data and models enabled an efficient root cause analysis and supported redesign of the problem region.

## 5. Digital Twin implementation challenges and opportunities

This section highlights the challenges associated with developing and incorporating Digital Twins in practical applications in additional to some possible paths forward. Many of the enabling technologies for Digital Twins are in various states of advancement, progressing as a function of both industry need and technology readiness/maturity. Digital Twin solutions, driven by specific desired outcomes, are being pieced together based on industry need, but there are still some signif icant challenges limiting the Digital Twin technology potential, as dis cussed below.

• Terminology: Consistent terminology needs to be defined to facilitate a common understanding and prevent miscommunication across multiple interacting technical domains and stakeholders.

• Standardization: A wide range of technologies ranging from data collection to insight generation to decision-making need to be stan dardized. However, the standards development process is often slow, resulting in slow wide-scale adoption of digital twins.

• Organizational culture: Cooperation and collaboration in the sharing of data and models is required among multiple stakeholders, with potentially competing business objectives. Fair value, data security and intellectual property rights need to be ensured among the stakeholders.

• Technology Maturity: Digital Twins are likely constructed from a patchwork of technologies and solutions from several different vendors. Technology development needs to prioritize technologies that offer the most meaningful increases in efficiency and effective ness, considering the current technology maturity which impacts the timeline and cost for such development.

• Verification and Validation: The Digital Twin is typically comprised of a number of different models and processes which require both V&V individually and as a comprehensive system. However, since the Digital Twin by definition is unique to the specifically modeled physical system, it may not be possible to validate a single instance, full system model. Extrapolation from individual component model V&V to the full system is challenging.

• Automation: A prominent targeted outcome in many digital twin implementations is to reduce the manual effort through automation of data exchange and analysis. While development efforts are un derway, there is still a strong reliance on human-in-the-loop as part of current solutions.

Digital Twins incorporate a variety of technologies from several different fields. The associated development needs and opportunities can be related to several general categories:

• Connecting previously unconnected data sources: Connecting data and models that existed in previously independent silos, with the aim of increasing the efficiency and speed at which asset information can be kept current and exchanged between these silos.

• Development of Computational Models: Improving model accuracy and fidelity, reducing the model uncertainty, and development of artificial intelligence/machine learning models.

• Uncertainty Quantification: Quantifying, reducing and communi cating the uncertainties that arise in the data and models, such as propagation of measurement noise and errors, modeling errors and approximations, and nuisance parameters in the model.

• Improvement of Output Delivery/Visualization: Visualization tech niques that present insights in an intuitive and interactive manner and support decisions, including augmented reality/virtual reality capabilities.

• Improvement of Data Infrastructure and Management: Communica tion infrastructure such as 5G, satellite communication, and improved network capabilities, in order to facilitate larger volume and higher frequency data transfer, local technologies such as wireless sensors, RFID, and IOT to allow greater flexibility in data transfer between data collection components and communication systems, and cloud computing for scalable and cost-efficient data processing and storage.

## 6. Conclusion

This paper has sought to generalize the characterization of the Dig ital Twin and provide a consolidated definition that can be used to clearly classify what is and is not a Digital Twin. After providing a definition and characterization, the process by which Digital Twins can be practically implemented was discussed, highlighting the key design decisions and implementation strategies. This approach was explored through a representative case study.

The design and implementation of a Digital Twin, including the de tails of its components, should be driven by desired outcome(s). This will help to set the requirements for the required data, models, and processes to update the models based on the data. Digital Twin implementations require the incorporation of a variety of different enabling technologies, and bringing these technologies together is still an ongoing challenge. Several approaches can be considered: build a Digital Twin using existing commercial tools, construct a Digital Twin from commercial components, or a hybrid approach.

Some of the challenges to Digital Twin implementation are technical in nature and can be resolved through continued research and devel opment. Other challenges are cultural and will require disrupting cur rent operating models and ways of thinking. The Digital Twin concept is clearly still evolving, as seen in the diversity of new industries and use cases that Digital Twins are being applied to. This continued concept evolution is also apparent in the lack of concrete examples demon strating the clear benefits of Digital Twins in practice. Despite the con cept’s popularity, this has raised questions regarding the technology’s ability to provide tangible improvements over existing processes. Answering these questions will require successful demonstrations of the technology’s value.

## Acknowledgement

This research was partly supported by funding from the American Bureau of Shipping (ABS). The support is gratefully acknowledged.

## References

[1] D. Delen, H. Demirkan, Data, information and analytics as services, Decis. Support. Syst. 55 (2013) 359–363, https://doi.org/10.1016/j.dss.2012.05.044.

[2] Z. Ben Miled, M.O. French, Towards a reasoning framework for digital clones using the digital thread, in: 55th AIAA Aerosp. Sci. Meet, American Institute of Aeronautics and Astronautics, Reston, Virginia, 2017, https://doi.org/10.2514/ 6.2017-0873

[3] L. Hu, N. Ngoc-Tu, W. Tao, M.-C. Leu, X.F. Liu, M.R. Shahriar, S.M. Nahian Al Sunny, Modeling of cloud-based digital twins for smart manufacturing with mt connect, Proc. Manuf. 26 (2018) 1193–1203, https://doi.org/10.1016/j. promfg.2018.07.155.

[4] M. Grieves, Digital Twin : Manufacturing Excellence through Virtual Factory Replication. White Paper. 2014.

[5] H. Millwater, J. Ocampo, N. Crosby, Probabilistic methods for risk assessment of airframe digital twin structures. Eng. Fract. Mech. 221 (2019) 106674.

[6] A. Kusiak, Smart manufacturing must embrace big data, Nature. 544 (2017) 23–25.

[7] V. Martinez, A. Neely, A. Ouyang, C. Burstall, D. Bisessar, Service business model innovation: The digital twin technology, in: EurOMA Conf, 2018.

[8] J. Meierhofer, S. West, M. Rapaccini, C. Barbieri, The Digital Twin as a service enabler: From the service ecosystem to the simulation model, in: Lect. Notes Bus. Inf. Process, Springer, 2020, pp. 347–359, https://doi.org/10.1007/978-3-030- 38724-2\_25.

[9] R. Bitton, T. Gluck, O. Stan, M. Inokuchi, Y. Ohta, Y. Yamada, T. Yagyu, Y. Elovici, A. Shabtai, Deriving a cost-effective digital twin of an ICS to facilitate security evaluation, in: Lect. Notes Comput. Sci. (Including Subser. Lect. Notes Artif. Intell. Lect. Notes Bioinformatics), Springer Verlag, 2018, pp. 533–554.

[10] E.H. Glaessgen, D.S. Stargel, The digital twin paradigm for future NASA and U.S in: Air force vehicles. Collect. Tech. Pap. - AIAA/ASME/ASCE/AHS/ASC Struct. Struct. Dyn. Mater. Conf, 2012, pp. 1–14, https://doi.org/10.2514/6.2012–1818.

[11] K. Reifsnider, P. Majumdar, Multiphysics stimulated simulation Digital Twin methods for fleet management, in: 54th AIAA/ASME/ASCE/AHS/ASC Struct. Struct. Dyn. Mater. Conf, American Institute of Aeronautics and Astronautics, Boston, Massachusetts, 2013.

[12] P.M. Karve, Y. Guo, B. Kapusuzoglu, S. Mahadevan, M.A. Haile, Digital twin approach for damage-tolerant mission planning under uncertainty, Eng. Fract. Mech. 225 (2020) 106766.

[13] M. Macchi, I. Roda, E. Negri, L. Fumagalli, Exploring the role of Digital twin for asset lifecycle management, IFAC-PapersOnLine. 51 (2018) 790–795.

[14] C. Li, S. Mahadevan, Y. Ling, S. Choze, L. Wang, Dynamic Bayesian network for aircraft wing health monitoring digital twin, AIAA J. 55 (2017) 930–941.

[15] C. Zhou, J. Xu, E. Miller-Hooks, W. Zhou, C.H. Chen, L.H. Lee, E.P. Chew, H. Li, Analytics with digital-twinning: a decision support system for maintaining a resilient port, Decis. Support. Syst. 113496 (2021), https://doi.org/10.1016/j. dss.2021.113496

[16] E.A. Lee, S.A. Seshia, Introduction to Embedded Systems, a Cyber-Physical Systems Approach, Second ed., MIT Press, 2017.

[17] K. Ashton, The “Internet of Things” Thing, RFiD J, 2009.

[18] Merriam-Webster.com, system, Merriam-Webster, 2011. https://www.merriam-we bster.com (accessed March 28. 2020)

[19] A. Mohammadi, M.G. Jahromi, H. Khademi, A. Alighanbari, B. Hamzavi, M. Ghanizadeh, H. Horriat, M.M. Khabiri, A.J. Jahromi, Understanding kid’s digital twin, in: Int’l Conf. Inf. Knowl. Eng, 2018, pp. 41–46.

[20] C. Verdouw, J.W. Kruize, Digital twins in farm management: Illustrations from the FIWARE accelerators SmartAgriFood and Fractals. in: Zth Asian-Australasian Conf Precis. Agric, 2017, pp. 1–5, https://doi.org/10.5281/zenodo.893662.

[21] A. Tangirala, Principles of System Identification: Theory and Practice, CRC Press, 2017.

[22] W. Kritzinger, M. Karner, G. Traar, J. Henjes, W. Sihn, Digital twin in manufacturing: a categorical literature review and classification, IFAC PapersOnLine, 51 (2018) 1016–1022.

[23] Q. Qi, F. Tao, Digital Twin and Big Data Towards Smart Manufacturing and Industry 4.0: 360 Degree Comparison 6. JEEE Access. 2018. pp. 3585–3593.

[24] K. Wärmefiord. R. Söderberg, L. Lindkvist. B. Lindau, J.S. Carlson. Inspection data to support a digital twin for geometry assurance, in: Vol. 2 Ady. Manuf, American Society of Mechanical Engineers, 2017, https://doi.org/10.1115/IMECE2017- 70398.

[25] J. Guo, N. Zhao, L. Sun, S. Zhang, Modular based flexible digital twin for factor design, J. Ambient. Intell, Humaniz, Comput. 10 (2019) 1189–1200.

[26] G. Baruffaldi, R. Accorsi, R. Manzini, Warehouse management system customization and information availability in 3pl companies: a decision-support tool, Ind. Manag. Data Syst. 119 (2019) 251–273, https://doi.org/10.1108/IMDS 01-2018-0033.

[27] S. Boschert, R. Rosen, Digital twin—The simulation aspect, in: Mechatron. Futur, Springer International Publishing, Cham, 2016, pp. 59–74.

[28] J. Guo, N. Zhao, L. Sun, S. Zhang, Modular based flexible digital twin for factory design, J. Ambient. Intell. Humaniz. Comput. 10 (2019) 1189–1200.

[29] E. Negri, L. Fumagalli, M. Macchi, A review of the roles of digital twin in CPS-based production systems. Proc, Manuf, 11 (2017) 939–948

[30] D. Jones, C. Snider, A. Nassehi, J. Yon, B. Hicks, Characterising the Digital twin: systematic literature review, CIRP J. Manuf. Sci. Technol. (2020) 36–52.

[31] A. Madni, C. Madni, S. Lucero, Leveraging Digital twin Technology in Model-Based Systems Engineering, Systems. 7 (2019) 7, https://doi.org/10.3390/ systems7010007.

[32] Digital Twins - Rise of the Digital Twin in Industrial IoT and Industry 4.0. http s://www.i-scoop.eu/internet-of-things-guide/industrial-internet-things-iiot-savin g-costs-innovation/digital-twins/, 2021 (accessed April 1, 2020).

[33] A. Canedo, Industrial IoT lifecycle via digital twins, in: Proc. Elev. IEEE/ACM/IFIP Int. Conf. Hardware/Software Codesign Syst. Synth. - CODES ’16, ACM Press, New York, New York, USA, 2016, p. 1, https://doi.org/10.1145/2968456.2974007.

[34] F. Castanedo, A review of data fusion techniques, Sci. World J. 2013 (2013) 704504.

[35] C. Yin, A. McKay, Introduction to modeling and simulation techniques, in: Isc. ITCA 2018 - 8th Int. Symp. Comput. Intell. Ind. Appl. 12th China-Japan Int. Work. Inf. Technol. Control Appl. Fuji Technology Press Ltd. 2018

[36] M.J. Asher, B.F.W. Croke, A.J. Jakeman, L.J.M. Peeters, A review of surrogate models and their application to groundwater modeling, Water Resour. Res. 51 (2015) 5957–5973.

[37] Z. Liu, N. Mevendorf, N. Mrad. The role of data fusion in predictive maintenance using digital twin, in: AIP Conf. Proc, AIP Publishing, 2018, p. 020023.

[38] M. Abramovici, J.C. Göbel. P. Savarino, Reconfiguration of smart products during their use phase based on virtual product twins, CIRP Ann. 66 (2017) 165–168.

[39] N. Demkovich, E. Yablochnikov, G. Abaev, Multiscale modeling and simulation for industrial cvber-physical systems, in: 2018 IEEE Ind. Cyber-Physical Syst. IEEE. 2018, pp. 291–296, https://doi.org/10.1109/ICPHYS.2018.8387674

[40] B. Schleich, N. Anwer, L. Mathieu, S. Wartzack, Shaping the digital twin for design and production engineering, CIRP Ann. 66 (2017) 141–144.

[41] M. Shafto, M. Conroy, R. Doyle, E. Glaessgen, C. Kemp, J. LeMoigne, L. Wang, DRAFT modeling, simulation, information technology & processing roadmap - technology area 11, Natl. Aeronaut. Sp. Adm. 27 (2010). https://www.nasa.gov/ pdf/501321main\_TA11-MSITP-DRAFT-Nov2010-A1.pdf.

[42] P.K. Majumdar, M. FaisalHaider, K. Reifsnider, Multi-physics response of structural composites and framework for modeling using material geometry, in: 54th AIAA/ ASME/ASCE/AHS/ASC Struct. Struct. Dyn. Mater. Conf, American Institute of Aeronautics and Astronautics, Reston, Virginia, 2013, https://doi.org/10.2514/ 6.2013-1577.

[43] M. Grieves, J. Vickers, Digital twin: Mitigating unpredictable, undesirable emergent behavior in complex systems, in: Transdiscipl. Perspect. Complex Syst, Springer International Publishing, Cham, 2017, pp. 85–113.

[44] K.M. Alam, A. El Saddik, C2PS: a digital twin architecture reference model for the cloud-based cyber-physical systems, IEEE Access. 5 (2017) 2050–2062.

[45] B.A. Talkhestani, N. Jazdi, W. Schloegl, M. Wevrich, Consistency check to synchronize the digital twin of manufacturing automation based on anchor points. Procedia CIRP 72 (2018) 159–164, https://doi.org/10.1016/j.procir.2018.03.166.

[46] C.-A. Schumann, J. Baum, E. Forkel, F. Otto, Digital transformation and industry 4.0 as a complex and eclectic change, in: 2017 Futur. Technol. Conf, 2017 pp. 645–650.

[47] R. Stackowiak, R. Stackowiak, Azure IoT solutions overview, in: Azur. Internet Things Reveal, Apress, 2019, pp. 29–54, https://doi.org/10.1007/978-1-4842- 5470-7\_2.

[48] Digital Twin Physics-Based Simulation & Analytics. https://www.ansys.com/ products/systems/digital-twin (accessed April 22, 2020). 2021.

[49] GE Power Digital Solutions, GE Digital Twin: Analytic Engine for the Digital Power Plant, 2016 https://www.ge.com/digital/sites/default/files/download\_assets/D gital-Twin-for-the-digital-power-plant-.pdf (accessed April 22, 2020).

[50] F. Perabo, D. Park, M.K. Zadeh, O. Smogeli, L. Jamt, Digital twin modelling of ship power and propulsion systems: Application of the open simulation platform (OSP), in: IEEE Int. Symp. Ind. Electron, IEEE Inc., 2020, pp. 1265–1270.

[51] U.S.G.A. Office, Navy Readiness, Actions Needed to Maintain Viable Surge Sealift and Combat Logistics Fleets (Publication No. GAO-17-503). https://www.gao.gov products/GAO-17-503, 2017.

[52] J.B. Pick, O. Turetken, A.V. Deokar, A. Sarkar, Location analytics and decision support: reflections on recent advancements, a research framework, and the path ahead, Decis. Support. Syst. 99 (2017) 1–8, https://doi.org/10.1016/j. dss.2017.05.016.

Eric VanDerHorn received his B.S. and M.S. degrees from Washington University in St. Louis in 2010. Currently, he is pursuing his Ph.D. degree in Vanderbilt University, and is expected to graduate in early 2021. He has been employed at the American Bureau of Shipping since 2010 with a range of roles in the lifecycle management of marine and offshore structures; including structural health monitoring, fracture mechanics, and damage structure assessment for emergency response. He is currently a product manager leading the development of digital twin solutions for structural integrity management of marine and offshore structures. His current research interests include uncertainty quan tification, reliability assessment, risk analysis, and data analytics.

Sankaran Mahadevan is John R. Murray Sr. Professor of Engineering, and Professor of Civil and Environmental Engineering at Vanderbilt University, Nashville, Tennessee, where he has served since 1988. His research interests are in the areas of uncertainty quantification, model verification and validation, reliability and risk analysis, design optimization, and system health monitoring, with applications to civil, mechanical and aerospace systems. His research has been extensively funded by NSF, NASA, FAA, DOE, DOD. DOT. NIST. GE. GM. Chrysler, Union Pacific. American Railroad Association, and Sandia, Idaho. Los Alamos and Oak Ridge National Laboratories. His research contribu tions are documented in more than 6o0 publications. including two textbooks on reli ability methods and 280 journal papers. He has directed 42 Ph.D. dissertations and 24 M. S. theses, and has taught several industry short courses on reliability and risk analysis methods. He is a Fellow of AIAA and EMI (ASCE). His awards include the NASA Next Generation Design Tools award (NASA), the SAE Distinguished Probabilistic Methods Educator Award, SEC Faculty Award, and best paper awards in the MORS Journal and the SDM and IMAC conferences. Professor Mahadevan obtained his B.S. from Indian Institute of Technology. Kanpur. M.S. from Rensselaer Polytechnic Institute. Troy. NY. and Ph.D from Georgia Institute of Technology, Atlanta, GA.
