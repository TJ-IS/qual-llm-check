---
otero_id: 5578
otero_key: "URS3U5NU"
title: "Design Principles for Virtual Worlds1"
authors: "Alok R. Chaturvedi; Daniel R. Dolk; Paul L. Drnevich"
year: "2011"
journal: "MIS Quarterly"
doi: "10.2307/23042803"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Design Principles for Virtual Worlds
Author(s): Alok R. Chaturvedi, Daniel R. Dolk and Paul Louis Drnevich
Source: MIS Quarterly, Vol. 35, No. 3 (September 2011), pp. 673-684
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/23042803
Accessed: 08-02-2018 09:42 UTC

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://about.jstor.org/terms

# DESIGN PRINCIPLES FOR VIRTUAL WORLDS $^{1}$

Alok R. Chaturvedi
Krannert School of Management, Purdue University, 403 W. State Street,
West Lafayette, IN 47907 U.S.A. {alok@purdue.edu}

Daniel R. Dolk
Naval Postgraduate School, 589 Dyer Road, Mailcode 06/IS,
Monterey, CA 93943 U.S.A. {drdolk@nps.edu}

Paul L. Drnevich

Culverhouse College of Commerce, University of Alabama, 361 Stadium Drive, Tuscaloosa, AL 35487 U.S.A. {dren@ua.edu}

In this research note, we examine the design, development, validation, and use of virtual worlds. Our purpose in doing so is to extend the design science paradigm by developing a set of design principles applicable to the context of virtual environments, particularly those using agent-based simulation as their underlying technology. Our central argument is that virtual worlds comprise a new class of information system, one that combines the structural aspects of traditional modeling and simulation systems in concert with emergent user dynamics of systems supporting emergent knowledge processes. Our approach involves two components. First, we review the characteristics of agent-based virtual worlds (ABVWs) to discern design requirements that may challenge current design theory. From this review, we derive a set of design principles based on deep versus emergent structures where deep structures reflect conventional modeling and simulation system architectures and emergent structures capture the unpredictable user–system dynamics inherent in emergent knowledge processes, which increasingly characterize virtual worlds. We illustrate how these design challenges are addressed with an exemplar of a complex mirror world, a large-scale ABVW we developed called Sentient World. Our contribution is the insight of partitioning ABVW architectures into deep and emergent structures that mirror modeling systems and emergent knowledge processes respectively, while developing extended design principles to facilitate their integration. We conclude with a discussion of the implications of our design principles for informing and guiding future research and practice.

Keywords: IS Design theory, virtual world systems, emergent knowledge processes, agent-based simulation, deep structure, platform as a methodology (PaaM), user-developed content (UDC)

## Introduction

A virtual world is a computer-based simulated environment that offers an increasingly popular and powerful alternative

reality for both management research and practice (Jarvenpaa et al. 2007). Virtual world applications come in many shapes and sizes (e.g., video games, Second Life, flight simulators, Internet social networks, computer models, social network sites, virtual reality, etc.). Some of the promise and popularity of virtual worlds lies in their ability to offer an alternative means to communicate, collaborate, and even to $^{1}$ Molly Wasko was the accepting senior editor for this paper. Ramesh Venkatraman served as the associate editor.

organize economic activity (Jarvenpaa et al. 2007). These virtual alternate realities carry the potential to change dramatically the ways in which we interact with one another in both the real world and the virtual.

While virtual worlds have much in common with other well-known types of information systems, they constitute a separate new class of information system with several unique requirements that need an extension of current design science principles (Hevner et al. 2004). One compelling reason for extension is the convergence between the real and the virtual worlds where there is a fairly crisp requirement not only for delineating between the two worlds, but also for aligning them in ways that allow both analogical reasoning and strategic decision-making to occur. Due in part to the prevalence of emergent knowledge processes (EKPs) (Markus et al. 2002) in virtual worlds, such alignment is a much more dynamic, fluid, and user-directed process than is found in traditional design science and, thus, it requires an extension of the traditional design science paradigm (Hevner et al. 2004). Further, to design and build a virtual world that facilitates convergence with the real world, it must emulate the network-centric, emergent, non-reductionist, and inherently unpredictable dynamics of the real world. For example, the virtual world must have sufficient resolution to capture the subtle details of the real world, while being abstract enough to allow users to understand the intricate relationships that exist therein. Virtual worlds provide such mechanisms in part through a concept of emergent design, which allows end users to become developers of the system itself.

In this research note, we examine the design, development, validation, and use of virtual worlds. Our purpose in doing so is to extend design science by developing a set of design principles applicable to the context of virtual environments, particularly those which use agent-based simulation as an underlying technology. Our central argument is that agent-based virtual worlds (ABVWs) comprise a new class of information system combining the structural aspects of traditional modeling and simulation systems in concert with the emergent user dynamics of systems supporting emergent knowledge processes. Our approach involves two components. First, we review the characteristics of virtual worlds and ABVWs to discern design requirements that may challenge current design theory (Hevner et al. 2004). From this review, we derive a set of design principles based on deep versus emergent structures (Wand and Weber 1994) where deep structures reflect conventional modeling and simulation system architectures and emergent structures capture the unpredictable user–system dynamics inherent in EKPs which increasingly characterize virtual worlds. We illustrate how these design challenges are addressed with an exemplar of a complex mirror world, a large-scale ABVW we developed called Sentient World. Our objective in doing so to determine the necessary derivations of the core principles of design science required for the context of virtual worlds. Our contribution is the insight of partitioning ABVW architectures into deep and emergent structures that mirror modeling systems and EKPs respectively, while developing extended design principles that facilitate their integration. We conclude with a discussion of the contributions of this paper and their implications for informing and guiding future research and practice.

## Agent-Based Virtual Worlds

Virtual worlds play an ever increasing role in the process of scientific inquiry. The traditional interplay between theory and experiment typified science from the beginning of the enlightenment until the advent of digital computers in the mid-20 $^{th}$ century, which altered the landscape dramatically and led to the ascendance of modeling and simulation as an integral part of scientific investigation (Hamming 1997). In this era, a model is a formal representation of reality, which implements a theory, and a simulation elicits the behavior of the model, usually over time, thus corresponding to an experiment. Similarly, virtual worlds, especially those emerging from networks of collaboration, constitute what may very well be the next transformative stage in the scientific method. In this new era, one can envision networks of virtual environments linked via shared semantics to form information ecosystems. Underlying this third stage of evolution is a radical shift in our conceptualization of system complexity from one of hierarchical decomposition (Simon 1996) to one of an emergent property of networks (Barabasi 2002; Miller and Page 2006). This confluence of complex adaptive systems and network science relies heavily on computational modeling and the methodology of computational experimentation for the creation and maintenance of virtual environments. The representation of emergent systems, in turn, relies heavily on the technology of agent-based simulation, which originated in the life sciences but has found application across an increasingly broad spectrum. Our focus in this paper is on the use of agent-based simulation in the creation of virtual worlds. First, however, we must parse a little more finely what we mean by virtual worlds and, in particular, agent-based virtual worlds.

The term virtual world is a very broad concept potentially encompassing almost any computer-generated artifact. To better pinpoint where we need to focus our design efforts, we adopt the terminology of the Metaverse Roadmap project (Smart et al. 2007), where virtual worlds are subsumed under the term metaverses, which in turn are characterized around two technology-driven axes of augmentation–simulation and external–intimate. Augmentation typically refers to hardware-intensive technologies used in virtual reality whereas simulation involves technologies for modeling reality, sometimes in the form of parallel worlds. Intimate technologies allow users to have avatars and digital profiles which provide users with agency as actors in the system. External technologies are not individual-based but rather focused on the outer world, for example in the form of societies and economies.

The upper half of the Metaverse Roadmap is oriented primarily toward virtual reality technologies that are beyond the scope of our research. Instead, we focus on the lower half, virtual and mirrored world dimensions of the Metaverse Roadmap where

Virtual worlds increasingly augment the economic and social life of physical world communities [and] ....Mirror worlds are informationally-enhanced virtual models or “reflections” of the physical world. Their construction involves sophisticated virtual mapping, modeling, and annotation tools, geospatial and other sensors, and location-aware and other lifelogging (history recording) technologies (Smart et al. 2007, p. 6, 9).

Virtual worlds include multi-player avatar-based games such as World of Warcraft and sophisticated social environments such as the popular Second Life. Mirror worlds rely more explicitly on simulation technology ranging from basic cellular automata (Wolfram 2002) to very large-scale, human-in-the-loop simulations such as Sentient World Simulation (SWS), a large-scale multi-agent model consisting of over 12 million heterogeneous, intelligent agents representing the virtual populations, leaders, organizations, institutions, infrastructure, and geographies of over 60 nations (McKay et al. 2011).

Agents are central to both virtual worlds, in which they tend to be implemented as avatars, and to mirror worlds, where agents typically have real-world counterparts. Thus ABVWs may refer to both types of virtual environments. ABVWs typically consist of some spatio-temporal landscape of artificial agents, often accompanied by human agents. Artificial agents are software entities generally assumed to have core properties (see Table 1). ABVW systems exhibit emergent behavior in which the effect of local interactions at the microscopic level results in macroscopic patterns. What macroscopic system behavior will emerge from these microscopic interactions is often difficult to predict. In Sentient World, for example, these agents represent an overall population of approximately a billion people, with an agent sampling rate of 1 in 100. In addition, it represents over 40,000 named $^{2}$ infrastructure nodes, 500 named media nodes, 1,200 named leaders, and over 1,000 organizations.

Agent-based simulation, which is the underlying, deep structure, of ABVWs, can reasonably be thought of as a member in the family of simulation paradigms that includes traditional modeling disciplines such as discrete event simulation, system dynamics, and Monte Carlo risk analysis. Indeed there are well over 100 modeling software platforms available for building agent-based applications, although seemingly few, if any, standards for doing so (Nguyen 2008).

Many ABVW applications transcend conventional modeling systems to provide very dynamic and fluid environments where users may have unprecedented degrees of freedom in how they interact with the system (for example, Second Life). The class of information system that bears the closest resemblance to this aspect of ABVW systems is emergent knowledge processes. EKP systems involve a fluid and changeable cast of users whose work profiles cannot be identified a priori, emergent work processes that result in fuzzy initial requirements that only become crisp through a succession of functional prototypes, and a strong emphasis on knowledge flow across an organization (Markus et al. 2002). This description typifies in many ways the situation with ABVWs as well. For example, the Second Life virtual world has no idea of who will choose to join the virtual community or what they will decide to do once they engage. Similarly, Sentient World users may come with a wide spectrum of interests depending upon which view of the “world at large” they wish to explore within the simulation. Requirements, system usage, and validation in these environments emerge from user-generated activities rather than from pre-specified methodologies.

ABVWs appear to be a hybrid of conventional modeling systems and systems characterized by EKPs. ABVWs comprise a new class of information systems with a different dynamic governing the relationship between requirements and users. Thus, they require an extension of the corresponding information system design principles (e.g., Hevner et al. 2004; Markus et al. 2002) to accommodate not only the relatively structured modeling dimension inherent in agent-based simulation, but also the unique dynamic, emergent processes of requirements, system usage, and validation inherent in virtual worlds.

<table><tr><td colspan="2">Table 1. Core Properties of Software Agents in Agent-Based Virtual Worlds</td></tr><tr><td>Property</td><td>Description</td></tr><tr><td>Autonomy</td><td>Absence of a central, or top-down, controller</td></tr><tr><td>Local interactivity</td><td>Agents react to, and/or interact with, neighboring agents and with other aspects of the environment</td></tr><tr><td>Spatial presence</td><td>Agents typically are positioned in, and act in, some form of an n-dimensional space</td></tr><tr><td>Rules of engagement</td><td>Agents “behave” according to specified rules or heuristics that may change over time</td></tr><tr><td>Perception</td><td>Agents can sense their neighborhood (e.g., the presence of other agents residing therein)</td></tr><tr><td>Memory</td><td>Agents may be able to record some of their perceptions</td></tr><tr><td>Communication</td><td>Agents may be able to communicate with other agents</td></tr><tr><td>Motion</td><td>Agents may be allowed to move around in their landscape</td></tr></table>

## Requirements and Objectives of Sentient World Simulation

Sentient World is a scientifically viable experimental platform for generative social science (Epstein 2007). As such, it presents formidable design challenges. The overall design objective for Sentient World was to develop a framework for designing high-performance, controlled systems to emulate highly uncertain environments in which not only the relative, Bayesian probabilities of possible outcomes may be unknown, but even the outcomes themselves may not be predictable a priori. The high level requirements of this complex system are to

• Capture social, political, economic, and media/communication dimensions of countries.

\- Support strategic military decision making and provide for maintaining situational awareness, as well as generating and evaluating possible courses of action.

\- Maintain near real-time fidelity, exhibiting near real-time accuracy and timeliness in underlying knowledge bases so that the environment is not far removed from the real world it emulates. This tight coupling shortens the decision loop between problem identification and the evaluation and execution of alternative courses of action.

\- Support multiple levels of spatial and temporal granularity, from regions encompassing multiple countries to provinces and cities within countries, and temporal levels of analysis from hours to months.

• Support human-in-the-loop participation and interaction.

## Application of Sentient World

Sentient World–Afghanistan was field tested in Afghanistan from March 1, 2007, until March 31, 2008, in support of the International Security Assistance Force (ISAF). The purpose was to assess the applicability of a complex ABVW modeling and simulation system with a reach-back capability to provide detailed analytical support for planning and decision making. Sentient World provided a planning and decision support framework for diplomatic, information, military, and economic (DIME) actions on political, military, economic, social, informational, and infrastructure (PMESII) dimensions of operations using a comprehensive whole-of-government approach (WGA). Sentient World incorporated multi-scale, multi-sided perspectives of the combined operational environment to highlight the economic, political, and cultural factors that influence military and nonmilitary outcomes at the district, province, national, and the regional levels. Over 6,000 events and 53,000 actions were executed on 398 Afghanistan districts with a total of approximately 18,000 named entities and over 2.5 million agents representing citizens of Afghanistan. From our experience in the development and field testing of this very large-scale mirror world simulation, a set of design principles evolved that we found to be invaluable in managing the complexity of the system.

## Design Principles for Virtual Worlds

Leveraging Wand and Weber's (1994) framework of information structure, we segment the design principles for virtual worlds into two primary categories corresponding to the modeling/simulation dimension, termed deep structure (DS) and the emergent knowledge process dimension, termed emergent structure (ES) (Table 2). These categories map to the micro-level and macro-level dimensions of emergent systems respectively. In Sentient World, we use a static, DS level for building and testing agents. DS enforces the implementation of the ABVW methodology and is embedded in the platform, and hence the name platform as a methodology (PaaM). ES is a dynamic, transient, user-generated level intended for generating and interpreting the emergent, macro-level behavior manifested in the virtual world. The synthetic environment for analysis and simulation (SEAS) $^{3}$ platform supports the modeling and simulation component of Sentient World. Using Sentient World as the ABVW exemplar artifact, we describe each of the principles in more detail below.

<table><tr><td colspan="2">Table 2. Design Principles for Agent-Based Virtual Worlds</td></tr><tr><td colspan="2">Deep Structure Principles</td></tr><tr><td>Principle</td><td>Sentient World Features</td></tr><tr><td>Principle DS1: Platform as a methodology for citizen programmers to contribute content</td><td>Dynamic data and model sourcing; virtual execution environment; logical compiler; experiment manager; grid computing</td></tr><tr><td>Principle DS2: Model formulation: Formal knowledge representation of models and simulation artifacts and associated model repository</td><td>SEAS conceptual model for agent behavior; agent model specification language</td></tr><tr><td>Principle DS3: Model execution: Independence of models, solvers, and data</td><td>Runtime binding of models, solvers, and data</td></tr><tr><td>Principle DS4: Model interpretation: Experimental design and sensitivity analysis specification IDE</td><td>Experiment manager IDE for specifying experimental designs; multiple levels of analysis; time and space granularity specification</td></tr><tr><td>Principle DS5: Model validation: Validate agent behaviors</td><td>Model bullpen for testing models within virtual world</td></tr><tr><td>Principle DS6: Model maintenance: Facilitate model reuse and integration</td><td>Society of simulations; backplane for social science model integration</td></tr><tr><td colspan="2">Emerging Structure Design Principles</td></tr><tr><td>Principle</td><td>Deep Structure Facilitators</td></tr><tr><td>Principle ES1: Accommodate diverse users (citizens)</td><td>DS1</td></tr><tr><td>Principle ES2: Citizen-centric views of the virtual world</td><td>DS2, DS5</td></tr><tr><td>Principle ES3: Allow, sustain, and protect user-created content</td><td>DS1, DS2, DS3, DS4, DS5</td></tr><tr><td>Principle ES4: Multiple levels of computational experimentation</td><td>DS3, DS6</td></tr><tr><td>Principle ES5: System must reconcile real and virtual worlds</td><td>DS3</td></tr></table>

## Deep Structure Design Principles for Virtual Worlds

The deep structure design principles emanate largely from well-known objectives of generalized model and data management systems. However, there are two significant differences (1) the platform is the methodology and (2) the end user is both the developer and the user. Keeping these differences in mind, the principles below are designed to support the modeling life cycle of model formulation, execution, interpretation, validation, and maintenance.

## Principle DS1: Platform as a Methodology (PaaM) for Citizen Programmers to Contribute Content

Sentient World was designed to allow users to contribute content in the form of data, models, scenarios, and intervention policies. While traditional information systems are developed by a few expert programmers, the bulk of the content in virtual worlds emanates from a very large number of end users. Sentient World, like Second Life, provides a consistent methodology and platform for users to design, develop, execute, and share content. Sentient World is a platform-based methodology to support emergent, user-generated ABVWs. Behaviors of citizen programmers (CPs) in the ABVW ecosystem are characterized as follows:

• Play dual roles of developer and user of content

\- Are highly diverse, but have limited views of the vast content space

\- Dynamically reveal their requirements as they become more aware and knowledgeable about their own needs and capabilities

\- Rely on the community to build and/or provide reliable models and data that they can use/reuse confidently

\- Tend to use models and data that are not directly in their areas of expertise

\- Combine data and models of varying spatial and temporal granularities

Given these characteristics of the user community, the Sentient World platform provides the discipline of structured methodology, consisting of five core components (Figure 1):

1. Dynamic model sourcing: Sentient World uses an agent-based framework to design, build, share, use, and reuse models of individuals, organizations, institutions (governments), infrastructures, geographies, markets, and events. Intra-agent components such as cognition, message flows, and behavior can also be modeled. Using this framework, users can develop models based on theories from diverse fields such as neuroscience, psychology, economics, social psychology, sociology, and political science.

2. Dynamic data sourcing: parameterization, configuration, calibration, and validation can be performed using the data stored in the internal databases (eXtensible Node Archives or xNA), external databases, or through mining other open source resources. Beyond theory testing, dynamic data sourcing provides a mechanism for grounded theory building in a semi-automated manner where new theories may be developed and tested.

3. Logical compiler: Sentient World consists of a lightweight compiler-like functionality to execute models. The compiler includes suggestion and language engines to match data to models (in six different languages), error-check, and test for data completeness.

4. Virtual execution environment (VEE): ABVWs are typically computationally demanding, rising exponentially with the number of agents. The computational requirements posed by Sentient World necessitate exploration of frontiers in both computer processing and data storage disciplines. The execution environment must be highly scalable to support processing of models that contribute incrementally to the system, and also support heterogeneous hardware architecture through virtualization technology. These aspects ensure flexibility. The scale of the computation performance also requires a highly distributed, grid-computing-based execution platform to allow the usage of computational resources around the world. Grid computing formalizes the distribution of and enables incremental addition of computing resources.

5. Experiment manager: Sentient World provides an interface for configuring an excursion from the Sentient World reference world to meet the individual needs of a user, such as

\- Exploring multiple courses of action by taking different sets of actions in identical copies of the reference world

\- Using proprietary or open source data in a controlled experiment without interfering with the publicly accessible Sentient World

\- Constructing a synthetic environment for only a portion of the world or including only certain models, simulations, tools, visualizations, or data sources

\- Conducting simultaneous excursions in different areas of the world and merging the nonproprietary and public results

\- Persisting significant simulation results in the database, tagged with this excursion's identifier, for later analysis and cross-excursion analysis

## Principle DS2: Model Formulation: Formal Knowledge Representation, Simulation Artifacts, and Associated Model Repository

A key characteristic of generalized modeling systems is a uniform way of representing models that are simultaneously human readable and computer executable. Agent-based simulation software is typically remiss in this regard in that most such systems require users to be fluent in object-oriented programming. The SEAS conceptual model for agents and accompanying model specification language allow users to specify agent attributes and behaviors at a high level of abstraction, and to store these in a model repository (Chaturvedi et al. 2005).

## Principle DS3: Model Execution: Independence of Models, Solvers, and Data

This principle is a corollary of the well-established premise in database management that data should be application independent. In ABVWs, it is critical that models, data, and solvers be interchangeable to promote the utmost flexibility and reuse. Models, data, and solvers (algorithms) should only be bound at runtime as is the case with Sentient World.

![](/api/attachments/URS3U5NU/fulltext/images/6e0be10b46730e8ecbfb36393eb615f5347329554dbfadfe9136d5e0788e8f54.jpg)  
Figure 1. Sentient World Platform and Structured Methodology

## Principle DS4: Model Interpretation: Experimental Design and Sensitivity Analysis

Simulations typically consist of a structural model (agents in ABVWs) coupled with an experimental design to observe the dynamic behavior of the model. Users must be able to specify robust experimental designs incorporating multiple levels of analysis and specifying appropriate spatial and temporal granularity. Sentient World, for example, implements individual, state, interstate, and system levels of analyses using the experiment manager. Granularity resolution of space and time is especially critical for very large-scale simulations, such as Sentient World, consisting of multiple agents and elaborate hierarchies.

## Principle DS5: Model Validation: Validate Agent Behaviors

ABVWs are notorious for being difficult to validate because the macro-behavior of the system emerges from a large number of localized nonlinear interactions at the micro-level. At the deep structure level, it is critical that agent behaviors be stringently tested in order to ensure the highest level of micro-level integrity. Without confidence that the localized agents are behaving as intended, it is impossible to draw meaningful conclusions about the resultant system behavior. The experiment manager again is an indispensable part of this validation process in its support of constructing and running models without compromising the shared public version of Sentient World. Different agent models can in effect be executed and tested off line while still operating within the overall context of the Sentient World environment.

## Principle DS6: Model Maintenance: Facilitate Model Reuse and Integration

Simulations are typically expensive to build and tend to be application-specific with a commensurate low level of reusability. Modularity and abstraction as facilitated in a conceptual framework such as the society of simulations (Chaturvedi 2006) are critical to implementing a more generalized environment where models, simulations, and data can be integrated with reasonable effort. A uniform model representation also contributes significantly to reuse and integration. The experiment manager facilitates a high degree of this modular flexibility in Sentient World by implementing the independence of models, simulations, data, solvers, and visualization tools within this system, as summarized in DS3. Users can “mix and match” the various components available in Sentient World to craft a virtually unlimited universe of excursions.

## Emergent Structure Design Principles for Virtual Worlds

Whereas DS design principles address platform infrastructure, ES design principles allow users to explore the virtual world environment by leveraging various features of the infrastructure. To develop the ES design principles discussed below, we modified and extended the design principles for EKPs enumerated by Markus et al. (2002). We retain the basic structure of EKP theory while generalizing the principles to accommodate the new class of ABVW systems. The major differentiating factor is the emphasis on user-created content and the higher degree of emergence that it entails. This extension results in highly dynamic and evolving requirements which tend to remove the developer from the requirements, design, and testing aspects of information systems development. Each of the ES principles is facilitated by one or more deep structure principles as we indicate below.

## Principle ES1: Accommodate Diverse Users (Citizens)

One of the defining traits of emergent knowledge processes is that we do not know the users a priori or what their requirements will be. This is particularly true for an ABVW such as Second Life, where a user can adopt one of a large number of existing avatars, or Sentient World, where users may build and/or execute an essentially unpredictable number of models. The PaaM approach of DS1 provides a versatile array of tools for users to create, manage, and coordinate models and data. The advantage of a powerful, formal generalized agent representation (DS2) is also instrumental in supporting a wide universe of users who can generate multiple versions of individuals, institutions, and states.

## Principle ES2: Citizen-Centric Views of the Virtual World

This principle is the ABVW knowledge counterpart of the data view concept underlying relational database theory (Date 2003). Users typically will only be interested in a subset of the overall environment at any point in time. Principles DS1, DS3, and DS6 allow citizens to develop, reuse, and interchange models, data, and solvers to construct their own lens into the virtual world.

## Principle ES3: Allow, Sustain, and Protect User-Created Content

The ability to allow and sustain user-created content delineates ABVWs most succinctly from EKPs. Citizens, not developers, generate the system content (Principles DS1–

DS6), and this content may evolve (or devolve, as is sometimes the case with as Wikipedia, for example) without explicit centralized control from a systems administrator. Once the virtual world provides the ability for the user to create content, there must be mechanisms in place for users not only to share their content via some form(s) of marketplace, but also to protect it. Second Life, for example, allows players to own artifacts they create and sell them both in virtual and real space. Sentient World allows users to create and own excursions as configurations of models, data, and solvers that can be shared and/or protected as they desire. This attribution of intellectual property to user-generated artifacts within the virtual environment is a sharp discriminator between ABVWs and more traditional information systems and software products. This attribute also leads to a host of legal ramifications surrounding intellectual property and individual rights within virtual worlds.

## Principle ES4: Multiple Levels of Computational Experimentation

ABVWs must allow users to explore and experiment within the virtual world. Experiments may be very loosely structured (e.g., trial and error in video games) or more rigorous as in simulations (Principles DS1 and DS4). Sentient World consists of both artificial agents as well as human agents. Artificial agents may comprise persons such as leaders, citizens, soldiers, and/or other entities known to function in the real-world environment under simulation such as institutions, organizations, infrastructure, and businesses. A human agent represents a human being that participates in the simulation and represents “human-in-the-loop” capability. Both artificial and human agents can interact with other agents as well as with the environment. The roles between artificial and human agents may also be interchangeable, depending on the specifics of the particular simulation.

The behavior of human agents is not predetermined, but rather is played out by the user participating in the ABVW. The human agent is free to act within the capabilities and constraints imposed by the parameters of the particular ABVW. By contrast, the behavior of artificial agents is modeled as a “forward” problem and hence is constrained by a predetermined set of rules. These rules, however, can vary for a number of reasons. For one, the values of certain parameters describing the rules are either generated from published research and/or empirical or sensed data when available.

A higher level and more complex artifact in Sentient World is an organization. It is modeled as an “inverse” problem because the behavior of an organization is determined by the behaviors of its membership, its processes, and leadership. As such, the behavior of an organization is emergent and transient.

## Principle ES5: System must Reconcile Real and Virtual Worlds

The aforementioned emergence of intellectual property issues within virtual space is one dimension where real and virtual worlds may be seen to converge (or possibly collide). Marketplaces can also be viewed as a mechanism wherein the two worlds coalesce. When virtual artifacts gain real economic value, for example (as they do in Second Life, where marketplaces exist for both real and virtual currencies), then “real” money can be used to make transactions in virtual space or vice versa.

Perhaps the most crucial element in reconciling real versus virtual worlds is the issue of validation. We have discussed the deep structure version of validation regarding agent behaviors. The emerging structure counterpart of validation is, however, much more difficult to characterize. How does one validate his/her experience in a flight simulator or in Second Life, for example? Validation strategies are key components, and perhaps the most difficult aspects of ABVWs. Tension exists between the conventional analytical model-based view of validation and the user-based perception of what is valid in VW space. Internal consistency is usually desirable in virtual worlds, but alignment with the external, real world is not always a requirement. What we have found in our experience with Sentient World is that validation itself is an emergent property and highly dependent on the purpose of the underlying virtual world. If the purpose of using a flight simulator is training, then validation is much different than if the primary purpose is entertainment or strictly game playing. Similarly, if the purpose of using Sentient World is anticipation, then we would apply much stricter criteria than if the purpose is exploring possible futures or illuminating the military decision landscape. Equifinality and multi-finality make the identification of cause and effect fuzzy at best in the case of predictive analysis, but provide motivation for further exploration in the landscape of “what might be.” It is our belief that validation of virtual and mirror worlds will increasingly be seen as a socially defined construct in juxtaposition to the much more rigid notions that apply in traditional analytical modeling. In the next section, we offer observations from our experience with Sentient World in support of this conjecture.

## Observations and Discussion

In this section, we discuss some of the observations that we can draw from the paper. These observations include outcome convergence and multi-finality and equifinality processes.

## Outcome Convergence

Remarkably, over time, emergent designs show a convergence toward a limited number of possible combinations of components. This observation is consistent with self-organization in systems theory, which states that systems are ordered and exhibit regularities in structure (Skyttner 2001). In an ABVW context, a self-organized design is an irreversible process of the emergence of a relatively stable structure from a random initial condition in the absence of any external intervention. This is a noncausal creative process in which new innovations are realized through interaction among the participating members of the community. What makes this process different from the traditional design process is that both innovation and structure coevolve due to the inner dynamism of the community of users.

The ABVW social design process is governed by three simple principles: (1) maintain the internal structure, (2) complete the goal irrespective of changing conditions, and (3) remove bad goals and preserve the good ones. When considered over a reasonable time horizon, ABVW designs do not jump from one state of random design to another, but move from one relatively stable state of interrelation among their components to another stable state. This process is similar to the self-organizing flocking behaviors in ad hoc sensor network design observed by Olfat-Saber (2006). These stable states are called “attractor states” (Beer 1995). The likelihood of changes of system components toward those present in attractor states are greater than the probability of changes away from them. This behavior is very similar to what is observed in “buzz” creation in social media. A given design may oscillate between two or more attractor states whereas the intervening patterns that are less likely are often represented as occupying “boundary” areas. This principle has also been observed in psychology and is called the set point theory (Tversky and Kahneman 1981) and spontaneous organization in market economies (Hayek 1948; Vanberg 1986). As such, stable designs are emergent patterns of co-occurrence of a limited number of dimensions. However, the ways in which patterns of components interact may vary enormously between designs at the level of the individual and the published goals. For example, variation among designs emerges in part from the influence of developers on one another, as well as a host of platform model and data factors.

## Multi-Finality and Equifinality Processes

Processes that link requirements to emergent design may be both multi-final and equifinal. Sentient World's social design process, like any open system, exhibits characteristics of multi-finality and equifinality. That is, over time, a given set of conditions may lead to a multitude of end states (multi-finality), and many different conditions may lead to the same end-state (equifinality) (Beven 2006; von Bertalanffy 1950). When data on different trends and individual needs of the users are integrated, they show characteristics of multi-finality and equifinality. The influences of internal and external data sources, models, and requirements on users may also occur through multi-final or equi-final pathways. Such designs would need to consider the following situations that exhibit a diversity of outcomes, given single operating requirements, or those that exhibit a single outcome, despite being exposed to different operating requirements. Currently, there are only ad hoc policies to resolve the issues of multi- and equifinality. These policies also emerge in the community to overcome the validation challenges. For example, the user community may select only certain end-states as a valid design in the case of multi-finality.

The set of design principles presented above is intended as a high level guide for citizen developers as well as a prelude to developing new design theory for virtual worlds. However, we do not make any claims for completeness as there are many areas, such as data visualization, where it is not possible to imagine all the contingencies and, therefore, we are not able to address all of them explicitly. We see our design principles as being necessary, but not sufficient in this regard. In the next section, we conclude with some of the implications of our virtual world design principles for research and practice.

## Implications and Conclusions

In this paper, we have argued that virtual worlds comprise a new class of information systems with different dynamics and unique requirements for governing the relationship between requirements and users. These unique requirements include not only a focus on user-created content as opposed to prespecified requirements, but also the spectrum of fuzzy versus crisp convergence between the real and the virtual spheres. In the case of Sentient World, there is a fairly crisp requirement for delineating not only between real and virtual worlds, but also for aligning them in a way that allows analogical reasoning and, subsequently, strategic decision making to occur. We have argued that such alignment is a much more dynamic, fluid, and user-directed process with virtual worlds due to these emergent properties and, as such, it requires a new set of design principles to build such agent-based environments.

## Implications of Virtual Worlds for Research and Practice

## Implications for Research

Integration of different research methodologies into a unified virtual world for scientific investigation: Building ABVWs requires integrating analytical, empirical, and computational methods in a structured manner. Analytical methods gives elegant closed-form solutions to narrow, but well-defined, problems; empirical methods allow researchers to test theories at different levels of analyses; and computational methods allow researchers to build high fidelity simulations. However, none of these methods are particularly effective for studying large-scale problems. Combining all three methods with fast and accurate semantic mining and high performance computing to create an ABVW facilitates the development and application of new theories and insights. The issues and implications of such integration is a fertile area for future research, which is in need of much clarification and refinement.

Use of grounded approaches to formalize data collection for populating ABVW: Semantic data mining coupled with social tagging creates an exciting new means for grounded theory building. Open coding can be done through semantic data mining of a very large number of documents rapidly and relatively accurately. Social tagging can then be used to perform axial coding in a more democratic manner. Thus, one can apply semi-automated grounded theory building to support the full range of theoretical research—exploratory, explanatory, and confirmatory.

Design science implications for user-generated content: Just as the advent of e-business converted end customers into “employees,” platform-based virtual worlds are transforming users into developers. This phenomenon seems destined to accelerate, resulting in huge variability in skill sets. As such, there are research opportunities to adapt, transform, and/or extend design science principles to accommodate citizen developers in a more structured manner.

## Implications for Practice

Virtual worlds can effectively support mission-critical decision making: Our experience using Sentient World illustrates that ABVW can be effectively deployed to support decision making in complex operational environments. Involving personnel of diverse backgrounds, missions, and training results in plurality of thoughts and ideas which, in turn, yields a more complete and multidimensional analysis.

Collaboration in virtual worlds is more complex and deep; the very assumptions behind ideas can be challenged and modified; ideas can be “run,” tested, evaluated, implemented, and monitored. The challenge for practice is to develop a structured methodology for ABVW that manages the emergent process while preventing chaos.

Practical knowledge sharing: ABVW requires integration not only of different methodologies, but also of knowledge from different disciplines. The risk of such integration being poorly executed is not only a potentially bad system, but a potentially dangerous one as well. A community-based approach based on emergent worlds may mitigate this risk by generating more stable attractor states.

Citizen development: Organizations should encourage users to become involved in virtual world projects because higher participation leads to higher fidelity of the emergent virtual worlds. An organization can gainfully deploy virtual worlds to enhance its institutional memory, employees' IQ, collaboration, and plurality of thoughts.

## Conclusions

The ascendance of virtual worlds has given rise to a new dynamic between system and user requirements, which in turn requires an extended set of design principles for developing virtual worlds. We have partitioned these design principles into deep structure, which resembles analytical modeling and simulation systems, and emergent structure, which captures the fluid interaction inherent in emergent knowledge processes. The major differentiating factor is the emphasis upon user-created content and the higher degree of emergence that entails. Our extension results in highly dynamic and evolving requirements which tend to remove the developer from the requirements, design, and testing aspects of information systems development. We hope this research note may encourage and motivate other scholars to join us in this area of academic inquiry and application.

## Acknowledgments

This research is partially funded by National Science Foundation grant # 0720677. The authors would like to thank the anonymous reviewers, associate editor, and senior editors for their valuable comments on the manuscripts. The authors would also like to thank Simulex Inc, its founder Alok Chaturvedi, and its developers for making the Sentient World technology and data available to the authors for this research.

## References

Barabasi, A. L. 2003. Linked: How Everything Is Connected to Everything Else and What it Means, New York: Plume Publishing.

Beer, R. 1995. “A Dynamical Systems Perspective on Agent-Environment Interaction,” Artificial Intelligence (72:1-2), pp. 173-215.

Beven, K. 2006. “A Manifesto for the Equifinality Thesis,” Journal of Hydrology (320:1-2), pp. 18-36.

Chaturvedi, A., Dolk, D., Mehta, S., and Ayer, R. 2005. “Agent-Based Simulation for Computational Experimentation: Developing an Artificial Labor Market,” European Journal of Operational Research (166), pp. 694-716.

Chaturvedi, A. 2006. “A Society of Simulation Approach to Dynamic Integration of Simulations,” in Proceedings of the 38 $^{th}$ Winter Conference on Simulation, Monterey, CA, pp. 2125-2131.

Date, C. J. 2003. An Introduction to Database Systems ( $8^{th}$ ed.), Reading, MA: Addison-Wesley Publishing.

Epstein, J. M. 2007. Generative Social Science: Studies in Agent-Based Computational Modeling, Princeton, NJ: Princeton University Press.

Hamming, R. W. 1997. The Art of Doing Science and Engineering: Learning to Learn, Amsterdam: Gordon and Breach Science Publishers.

Hayek, F. 1948. Individualism and Economic Order, Chicago: University of Chicago Press.

Hevner, A. R., March, S. T., Park, J., and Ram, S. 2004. “Design Science in Information Systems Research,” MIS Quarterly (28:1), pp. 75-105.

Jarvenpaa, S., Leidner, D., Teigland, R., and Wasko, M. 2007. "MISQ Special Issue: New Ventures in Virtual Worlds," MIS Quarterly Call for Papers.

Markus, M. L., Majchrzak, A., and Gasser, L. 2002. “A Design Theory for Systems that Support Emergent Knowledge Processes,” MIS Quarterly (26:3), pp. 179-212.

McKay, S., Chaturvedi, A., and Adams, D. D. 2011. “A Process for Anticipating and Shaping Adversarial Behavior,” Naval Research Logistics (58:3), pp. 255-280.

Miller, J., and Page, S. 2007. Complex Adaptive Systems: An Introduction to Computational Models of Social Life, Princeton, NJ: Princeton University Press.

Nguyen, C. 2008. “Developing a Conceptual Architecture for a Generalized Agent-Based Modeling Environment (GAME),” Master’s Thesis, Naval Postgraduate School (available at http://edocs.nps.edu/npspubs/scholarly/theses/2008/Mar/08Mar\_Nguyen.pdf).

Olfati-Saber, R. 2006. “Flocking for Multi-Agent Dynamic Systems: Algorithms and Theory,” IEEE Transactions on Automatic Control (51:3), 401-420.

Simon, H. 1996. The Sciences of the Artificial ( $3^{rd}$ ed.), Cambridge, MA: MIT Press.

Skyttner, L. 2001. General Systems Theory: Ideas and Applications, Singapore: World Scientific.

Smart, J., Cascio, J., and Paffendorf, J. 2007. “Metaverse Roadmap: Pathways to the 3D Web: A Cross-Industry Public Foresight Project” Metaverse Roadmap (http://www.metaverseroadmap.org/MetaverseRoadmap Overview.pdf).

Tversky, A., and Kahneman, D. 1981. “The Framing of Decisions and the Psychology of Choice,” Science (211:4481), pp. 453-458.

Vanberg, V. 1986. “Spontaneous Market Order and Social Rules,” Economics and Philosophy (2), pp.75-100.

von Bertalanffy, L. 1950. “Theory of Open Systems in Physics and Biology,” Science (111:2872), pg 23-29.

Wand, Y., and Weber, R. 1995. “On the Deep Structure of Information Systems” Information Systems Journal (5:3), pp. 203-223.

Wolfram, S. 2002. A New Kind of Science, Champaign, IL: Wolfram Media, Inc.

## About the Authors

Alok R. Chaturvedi is a professor in Purdue University's Krannert Graduate School of Management and the founder, chairman, and CEO of Simulex Inc., a modeling and simulation company located in Purdue Technology Park. Dr. Chaturvedi is the founding director of Purdue Homeland Security Institute and has also served as an adjunct research staff member at the Institute for Defense Analyses in Alexandria, Virginia, a leading think tank on national and homeland securities matters. He received his Ph.D. in Management Information Systems and Computer Science from the University of Wisconsin-Milwaukee. Dr. Chaturvedi led the development of the synthetic environment for analysis and simulation (SEAS), a platform for large-scale multi-agent simulations. SEAS is extensively used by the U.S. Department of Defense for war games, experimentations, planning, analysis, operations, and shaping in multiple theaters. The National Training Simulations Association recognized SEAS as the best simulation for analysis in all of the Department of Defense for the year 2005. Dr. Chaturvedi is the principal investigator and the project director for several major grants from the

National Science Foundation, Indiana 21 $^{st}$ Century Research and Technology Fund, the Office of Naval Research, the Defense Acquisition University, and several Fortune 500 companies. He has been involved with several government task forces on important public policy and national security matters. He was named in Federal 100 by Federal Computer Weekly and was awarded the “Sagamore of the Wabash” by the Governor of Indiana, the highest civilian award for his service to the State.

Daniel Dolk is professor emeritus of Information Sciences at the Naval Postgraduate School, Monterey, CA. Dr. Dolk's research interests focus on the many dimensions of the confluence of model management and decision support, including meta-model representations of optimization models, integrated modeling environments for agent-based modeling and simulation, and most recently predictive analytics as a service. He is currently investigating the use of meta-modeling to facilitate interoperability of heterogeneous information sources and predictive analytics in grid and cloud environments. Dr. Dolk is Chair of the Decision Technologies, Service Science and Mobile Services Track for the Hawaii International Conference on System Sciences and vice chair of the IFIP Working Group 7.6 on Systems Modeling and Optimization.

Paul Louis Drnevich is an assistant professor of strategic management at the University of Alabama. Dr. Drnevich's research interests include competitive advantage and value creation/appropriation and the effects of the dynamics of environmental uncertainty on performance, the implications of capabilities and environmental factors for innovation and performance in entrepreneurial ventures and small business, and the use of virtual environments and agent-based simulations to study strategic decision making in intra- and interorganizational networks. He has published in Strategic Management Journal, MIS Quarterly, Decision Sciences, Academy of Management Learning and Education, Journal of Small Business Management, and Journal of Managerial Issues, among other venues.
