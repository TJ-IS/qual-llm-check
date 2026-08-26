---
otero_id: 1386
otero_key: "ZNR7S4K8"
title: "Boundary Objects in Design: An Ecological View of Design Artifacts"
authors: "Gloria Mark; Kalle Lyytinen; Mark Bergman"
year: "2007"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00144"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
11-2007

# Boundary Objects in Design: An Ecological View of Design Artifacts

Gloria Mark
University of California, Irvine, USA, gmark@ics.uci.edu

Kalle Lyytinen

Case Western Reserve University, USA, kj13@po.cwru.edu

Mark Bergman

Naval Postgraduate School, mbergman@nps.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# Journal of the Association for Information Systems JAIS

Special Issue

Boundary Objects in Design: An Ecological View of Design Artifacts

Mark Bergman
Graduate School of Operations and Information Science (GSOIS)
Naval Postgraduate School
mbergman@nps.edu

Kalle Lyytinen
Weatherhead School of Management
Case Western Reserve University
kalle@case.edu

Gloria Mark
Department of Informatics
University of California, Irvine
gmark@ics.uci.edu

## Abstract:

Traditionally, Systems Analysis and Design (SAD) research has focused on ways of working and ways of modeling. Design ecology – the task, organizational and political context surrounding design – is less well understood. In particular, relationships between design routines and products within ecologies have not received sufficient attention. In this paper, we theorize about design product and ecology relationships and deliberate on how design products – viewed as boundary objects – bridge functional knowledge and stakeholder power gaps across different social worlds. We identify four essential features of design boundary objects: capability to promote shared representation, capability to transform design knowledge, capability to mobilize for action, and capability to legitimize design knowledge. We show how these features help align, integrate, and transform heterogeneous technical and domain knowledge across social worlds as well as mobilize, coordinate, and align stakeholder power. We illustrate through an ethnography of a large aerospace laboratory how two design artifacts – early proto-architectures and project plans – shared these four features to coalesce design processes and propel successful movement of designs across social worlds. These artifacts resolved uncertainty associated with functional requirements and garnered political momentum to choose among design solutions. Altogether, the study highlights the importance of design boundary objects in multi-stakeholder designs and stresses the need to formulate sociology-based design theories on how knowledge is produced and consumed in complex SAD tasks.

Keywords: systems analysis and design, design theory, boundary objects, social worlds, knowledge integration, power alignment, design ecology, functional requirements, stakeholder analysis

\* This is a part of the special issue on System Analysis and Design. Juhani livari was the accepting senior editor. The manuscript was submitted before Kalle Lytinen became Editor-in-chief. He did not participate in the editorial decision. The manuscript was submitted on 27/3/2005, and went through 3 revisions.

Volume 8, Issue 11, Article 1, pp. 546-568, November 2007

# Boundary Objects in Design: An Ecological View of Design Artifacts

## Introduction

Traditionally, System Analysis and Design research (SAD) has focused on ways of working (ter Hofstede and Weide 1992), ways of carrying out design tasks or ways of modeling (Leppänen 2005) and how to represent design products and/or their environments. Design ecology, i.e., the task, organizational, and political context of design, has been less studied. In general, design ecologies consist of functional and political elements (Bergman et al., 2002b) and define: 1) what system(s) can be built and delivered within the given environment, and 2) how stakeholders' interests align with proposed designs to mobilize willingness and resources.

Within ecology studies, a significant portion of the past research has been devoted to implementation challenges and stakeholder involvement (Kwon and Zmud, 1987; Lamsweerde et al., 1998; Lamsweerde and Letier, 2000; Mumford, 2003). Less attention has been paid to the role of design products in shaping and influencing the composition and dynamics of the design ecology (Bergman et al., 2002a, Bergman et al., 2002b). These concerns emerge, in particular, when the design task involves system engineering tasks- i.e. where the design “may include computer hardware, other types of hardware device which are interfaced to the computer and the operational processes which are used when the system is installed in some working environment” (Kotonya and Sommerville, pp. 12). Such situations are becoming common in IS design in general, as business process design and system design increasingly coalesce (Hansen et al. 2007). Therefore, design issues underlying complex system designs are worth considering for IS scholars. When design products are effectively embedded in design ecologies, there will be a significant improvement in SAD practice which will help mitigate against failures that result from a poor understanding of how design artifacts relate to actors and their behaviors in the ecology.

In this paper, we analyze features of SAD products that improve their use in design ecologies in order to mitigate against design failures. In particular, we analyze how design knowledge can be organized and mobilized in these ecologies by being embedded into products in ways that permit designs to proceed when multiple stakeholders (social worlds) are present and interact. We define design knowledge as any stakeholder determination of the data in the design object or its environment that has the capability to enable or advance the design task. We adopt Star and Griesemer's (1989) definition of boundary objects and examine what sorts of interactions boundary objects within complex design ecologies must enable so as to allow designs to proceed. We define such SAD artifacts as design boundary objects – representational artifacts and associated ideas that enable design knowledge to be transferred between social worlds and that facilitate the alignment of their interests (Star and Griesemer, 1989). Through a synthesis of the existing design literature, we formulate four essential features for viable design boundary objects: 1) the capability for common representation, 2) the capability to transform design knowledge, 3) the capability to mobilize for action, and 4) the capability to legitimize design knowledge across social worlds. We show that these features are instrumental in embedding design artifacts in ecologies in ways that enable, propel, and glue together design routines across heterogeneous social worlds and allow designs to proceed. We illustrate the critical role of each feature by investigating in situ the deployment of two design products during the design of safety-critical software and hardware systems for space missions at NASA. We conclude by discussing the consequences of ignoring these features whereby designs get impeded, curtailed, misguided, or halted.

## IS Design activity involving multiple stakeholders

## Design theories and their role in IS design tasks

We define design as the practice of inventing, creating, and implementing (technical) artifacts that depends upon, integrates, and transforms heterogeneous and uncertain domains of knowledge. We frame our study in the context of theories of design and action (Gregor, 2006). These theories identify underlying principles, methods and frameworks that indicate how to transform the current reality into an improved reality by producing new artifacts (Simon, 1996; Gregor and Jones 2007; Walls et al., 1992). These theories involve procedural rationality (Simon, 1996) that guides effective generation and implementation of designs (Gregor, 2006; livari et al., 2004; Walls et al., 1992). Design theories compose and justify procedure choices that inform the mobilization and integration of heterogeneous and uncertain system and domain knowledge during system design and implementation, resulting in for improved designs. $^{i}$

IS research has long been informed by such theories. They draw upon a variety of other disciplines: economics, organizational behavior, and computer science, among others. Designs have also been studied in multiple domains including: management, industrial design, software, mechanical engineering, architecture, and others (Carlile, 2002;

Volume 8 ■ Issue 11 ■ Article 1

Henderson, 1991; Lutters and Ackerman, 2002; Markus and Keil, 1994; Pankoke-Babatz et al., 1997; Boland and Collopy 2004). In this study we are concerned with how the sociology of design knowledge can help formulate guidelines and insights in the context of complex design processes involving multiple heterogeneous social worlds. In addition, we are interested in how to design more effectively so as to mitigate against design failures, i.e., situations where designs fail, do not proceed, or are misguided. Moreover, we assume that such design processes will involve socio-technical interventions and thus demand the stabilization of design artifacts in their social contexts (Bijker and Law, 1994, Bijker et al., 1987).

A central element in any design theory is the notion of a design task—what the designer(s) should accomplish (Simon, 1996; Gregor and Jones 2007). This is typically defined by design goals and anticipated functions of the artifacts-to-be in their operating context (Markus et al., 2002; Orlikowski and Gash, 1994; Walls et al., 1992). Essentially, within complex multi-stakeholder design tasks, designers will depend on heterogeneous and uncertain knowledge. Accordingly, they must discover and coordinate multiple stakeholders' needs or other stakes, and then create solutions that will meet their preferred needs with the minimal time and cost, possibly with the maximal benefit (Hevner et al 2004; March and Smith 1995; Walls et al., 1992). SAD must, accordingly, produce and consume heterogeneous knowledge that allows the design process to find a feasible set of needs across stakeholders, and then generate solutions that will be understood by, and can obtain support among the stakeholders. This requires that designers can successfully integrate and align heterogeneous (sociotechnical) design knowledge across diverse social worlds (Bergman et al. 2002a, 2002b). These worlds form units of collective action in the design context due to their shared commitments, resources, and ideologies (Strauss, 1978; Clarke, 1991). Each world imposes unique requirements related to its individuals, the collective, its work environment, and its tasks that shape the subsequent design.

We define a design problem – the key element of the design task — as a gulf between a current state of the chosen target system — i.e. typically the existing work environment – and the state that is desired by principal stakeholders within one or more social worlds. $^{ii}$ . Each problem is owned by one or more principals who 1) have the institutional power to legitimize the problem by and for the design task, and 2) individually or collectively have the power to bring attention, action, and resources to remove the gulf (Bergman et al., 2002b). Next, we analyze such design problems through the lens of two design ecologies: political and functional. The political ecology is comprised of the institutional power structures surrounding the design; while the functional ecology refers to current and future organizational structures and operations and how technology supports and enables them. These ecologies are intertwined: the political ecology builds, governs, and utilizes the functional ecology to achieve its goals and solve the problems. The functional ecology, in turn, supports, informs, and augments the political ecology to enable desired operations. We analyze the nature of design in such ecologies and discuss the requirements associated with discovering and integrating design knowledge so as to formulate design theories for such contexts.

## The Political Design Ecology

In a political ecology, principals draw upon institutional structures and rules, which determine who has power to make design decisions as well as how and when this power is applied (Fairholm, 1993; Pfeffer, 1981). During SAD this ecology is comprised of two elements: 1) those actors who are entitled to make design decisions by applying organizational power, $^{iii}$ and 2) those actors who control the resources that can be mobilized (Bergman et al., 2002b). In the end, SAD is as much about interactions between social worlds with differing power bases in which actors reside as it is about formulating feasible “functional” solutions.

To be a (political) stakeholder, one must wield at least one of the two types of power. Those stakeholders we call 'principals' have both types of powers. $^{iv}$ A person with no design power is simply an interested observer regardless of his in her institutional or organizational position. Together, political stakeholders form the political ecology of SAD activity. Since there can be and usually are multiple stake holders pursuing different political options in each SAD activity, the political ecology is unique per each SAD activity. This ecology qualifies, selects, and embraces actions among stakeholders necessary to define and attend to design problems. It also determines and wields power to implement selected solutions. It is shaped by constant competition between stakeholders that have different stakes in problems and/or solutions. Therefore, stakeholders must identify and resolve conflicts and stabilize the ecology, at least momentarily, to reach any design solution (March and Olsen, 1976).

The political ecologies in which we are interested consist of multiple sets of stakeholders emanating from heterogeneous social worlds. They include users, system support staff, analysts, designers, system builders, customers, suppliers, and business partners, among others (Laudon and Laudon, 2003; Maier and Rechtin, 2000; Whitten et al., 2003). In appreciating these political ecologies, SAD procedures have to focus on how stakeholders relate to one another as well as to the proposed solution. These relationships also represent alignments between different authority levels and sources of expertise and knowledge (Bergman and Mark, 2003). SAD stakeholders populating different social worlds hold different organizational power, thus their relationships also reflect alignments of power, position, and expertise. During any SAD process, $^{v}$ the alignments must either be maintained or reformed in order to erect a stable political network that allows the design to proceed. Any instability in it will cause social rifts – i.e., power struggles – that can tear apart the design (Pfeffer, 1992). Therefore, agreements about problems, objectives, goals, and requirements must be supported through alliances forged among social worlds. Due to the dynamics of political ecologies, decision making during SAD gets distributed and constantly molded by shifting alliance structures (Orlikowski and Gash, 1994, Pfeffer, 1981, Pfeffer, 1992). These alliances seek constantly to solicit sufficient political weight to curb attacks from those who would rather choose a different design path (Dahl, 1991).

## The Functional Design Ecology

We call the operational part of any socio-technical order that will be changed or affected by SAD, the functional ecology (Bergman et al., 2002a, Bergman et al., 2002b). We define functional ecology as a set of processes and interactions between goals and functions, actors and institutional contexts that give rise to the functions that the system is expected to fulfill. $^{vi}$ Functional ecology frames “what will work and why”: how organizations will operate and how technology can support these operations and associated organizational structures. The majority of SAD efforts focus on shaping the functional ecology: 1) how to define the operational goals of the system-to-be-designed and 2) how to deploy a specific set of technologies — both computational and organizational — to meet these goals.

The functional ecology informs the political ecology: only problems that have feasible functional solutions will be considered. Likewise, the political ecology determines which problems and solutions will be select by deploying measures of operational, technical, economic, scheduling, or legal feasibility $^{vii}$ (Dennis and Wixom, 2003, Hoffer et al., 2004, Kendall and Kendall, 2004, Marakas, 2006, Whitten and Bentley, 2006). Finally, the functional ecology is constantly shaped by the political ecology: SAD initiatives must resolve authority and resource challenges while seeking to establish the technical and social feasibility of the chosen functional ecology.

## Design Routines and Design Methodologies

Feasible functional solutions and acceptable political solutions do not emerge in a single step due to task ambiguity and shifting stakeholder disagreements. SAD must therefore rely on organized activities shared between and/or within social worlds that we call here design routines. These routines consist of techniques, rules, and norms that indicate who should do what, when, and how in relation to which artifact in order to produce an acceptable design product. Design routines help identify problems, determine stakeholder requirements, and find solutions in ways that are predictable, codifiable, transferable, and shareable across social worlds. They consist of a number of steps and their ordering rules that show how to arrive at designs that are functionally feasible and politically acceptable. Collectively, the routines can be generalized and their underlying design knowledge made explicit and represented in methodical guidelines that form the backbone of most design methodologies (Lyytinen, 1987).

Design routines, while being enacted, will integrate design knowledge across social worlds. By so doing they also mobilize necessary power to engender designs (Hirscheim et al., 1995). To this end, routines 1) separate concerns to manage and understand issues as principals' problems, and 2), sequence design tasks into steps and generate feedback loops so as to learn from designs in order to reach a feasible functional and desirable political solution. Due to both 1) and 2), design routines promote incremental discovery and resolution of design ambiguities and stakeholder disagreements. Overall, we call movements through design routines a design path. This path consists of partially ordered design activities that are defined by enacted design routines. SAD methodologies, however, does not determine only one single true design path. Instead, design paths will weave together activities associated with routines as needed in order to produce the desired system. This is similar to an annealing process in which design knowledge cycles through a series of expansions and reductions to produce an improved outcome. Design knowledge is expanded when necessary, so as to understand the breadth and impact of uncovered problems and suggested solutions, and then again reduced by focusing on the limited set of feasible problems and solutions.

Principals and other stakeholders can enable, inhibit, or propel movement along design paths depending on the way in which they choose and enact design routines and depending on the outcomes of these activities. Each design routine must produce sufficient knowledge for designers so as to determine which course of action — typically another routine — to pick up next. Dynamic interactions between different routines spark additional problems and solutions, which, in turn, re-shape both functional and political ecologies (Bergman et al., 2002b). Therefore, successful movements along the design path involve enactments of routines that allow design ambiguities and stakeholder disagreements to emerge, and be then clarified and addressed. $^{viii}$

![](/api/attachments/ZNR7S4K8/fulltext/images/b1e5351f74184638bc2e97729f0dad44583a7033203a406edaa7a3b24bf3dc85.jpg)

Overall, we propose that SAD methodologies consist of sets of generalizable routines that can be considered as theories-in-use for design and action (Gregor, 2006). They guide the navigation of effective design paths across functional and political ecologies. We next examine how SAD products are created, mobilized, drawn upon, and manipulated during the enactment of design routines and how such products fulfill a critical role in generating, pruning, and traversing design paths. We call the SAD products connecting design routines crossing multiple social worlds “Design Boundary Objects” (DBO). We argue that they help overcome gaps in design knowledge residing in the functional ecology and resolve gaps in agreement residing in the political ecology.

## Design Boundary Objects

## Boundary Objects

A boundary object is defined as an artifact or a concept with enough structure to support activities within separate social worlds, and enough elasticity to cut across multiple social worlds (Star and Griesemer, 1989). In general, any artifact that is shared between two or more actors at the border of two social worlds can be regarded as a boundary object. Boundary objects tie together actors in multiple social worlds, while being capable of assuming different meanings in each world (Briers and Chua, 2001). Altogether, boundary objects (Star and Griesemer, 1989):

• Inhabit several social worlds,

• Satisfy the institutional requirements of each social world,

\- Are weakly structured in common use, and

• Are strongly structured in local use.

These properties have been studied across multiple and heterogeneous activities and for different types of artifacts including museums (Star and Griesemer, 1989), cargo airway bills (King and Forster, 1995), engineering drawings (Carlile, 2002, Henderson, 1991), medical patient records (Berg and Bowker, 1997), and aircraft maintenance requests (Lutters and Ackerman, 2002).

Boundary objects have also been studied from the perspective of how they are used to coordinate activities across multiple social worlds. These include: information fields that help actors align activities flexibly in control environments (Harper and Hughes, 1993, Heath and Luff, 1992); classification schemes that help determine sufficient responses to diseases (Bowker and Star, 1999); public displays that help inform engineers about design progress (Mark, 2002); or configuration management systems that help maintain a flow of software production (de Souza et al., 2003). Again, design artifacts have been studied primarily for their role as a DBO in coordinating activities across social worlds, while other social functions needed to represent, transform, mobilize, and legitimize heterogeneous design knowledge across social worlds have not been recognized.

Some ethnographic studies have touched on the role of boundary objects during design. Bødker (Bødker, 1998) views design representations as “containers” for multiple ideas and admits their limited capability to communicate across all stakeholder boundaries. Bertelsen (Bertelsen, 1996) argues against the use of abstract representations in favor of materially transforming boundary artifacts. His idea of material artifacts that will mediate the design is similar to the notion of boundary objects, as they must connect heterogeneous activity systems (Bertelsen, 1998; Bertelsen, 2000). His study, however, ignores how the designers must share and communicate explicit and heterogeneous knowledge about the design targets and goals.

Most of these studies focus on boundary objects in a social context that forms a part of operational activities across social worlds. Accordingly, examination of the features of these objects do not reveal how they actively operate during design so as to generate effective design paths. In particular, they ignore what is needed to mobilize and transform design knowledge as well as to legitimize it across social worlds. Therefore, Star and Griesemer's broad definition of boundary objects, though a good starting point, remains too passive to represent the critical functions of artifacts that serve as design boundary objects. We will next clarify this deficiency by examining in more detail the roles of boundary objects during SAD.

## Design Boundary Object

Design boundary objects are needed to overcome gaps in the design knowledge residing in the functional ecology and gaps in agreements residing in the political ecology. Indeed, one can view successful enactments of design routines as successive reductions of the gaps, though this process may not be smooth and linear. Any movement that mediates and reduces these gaps helps propel movement across routines, and by so doing, generates an increasingly refined design path. Hence, it is critical to understand how design boundary objects reduce gaps and how they support hand-offs between different design routines — especially those that take place at the borders of two or more diverse social worlds. To this end, we define a design boundary object (DBO) to be any representational artifact that enables knowledge about a designed system, its design process, or its environment to be transferred between social worlds and that simultaneously facilitates the alignment of stakeholder interests populating these social worlds by reducing design knowledge gaps. Most such DBO's are outcomes of enacted design routines. Examples of SAD boundary objects include: models of software or service architectures, database schemata and E-R diagrams, object class diagrams (and other UML models), data flow diagrams (DFDs), state charts, network or communications models, prototypes, and standardized requirement documents. Each such DBO is normally defined as a genre (type specification) that allows an infinite number of boundary object instances to be generated that will conform to this genre.

![](/api/attachments/ZNR7S4K8/fulltext/images/eac6c5f939770e2a4e582f86edd20fd23e8df85636ae8f8da12cda3e84414000.jpg)

## Four Critical Features of DBOs

Operationally, design boundary objects can be defined as artifacts that 1) enable, propel, and connect – i.e., “glue together” – design routines, 2) align stakeholder interests, and 3) identify and reduce gaps in design knowledge. Altogether, design boundary objects help represent, transform, mobilize, and legitimize design knowledge by facilitating shared understanding and promoting agreements about designs. As shown in Table 1, design boundary objects share four essential features. They: 1) promote shared representation, 2) transform design knowledge, 3) mobilize for design action, and 4) legitimize design knowledge. Table 1 also shows how each feature relates to political and functional ecologies.

<table><tr><td colspan="4">Table 1. Features of Design Boundary Objects</td></tr><tr><td>Features</td><td>Definition</td><td>Design Ecology</td><td>Description</td></tr><tr><td rowspan="2">Promote Shared Representation</td><td rowspan="2">Encapsulates understandings based on a common syntax and semantics, which are shared across social worlds</td><td>Functional</td><td>Form shared functional representations, i.e. data and technical models, prototypes, architectures, specifications, etc. (Sutcliffe and Gault, 2004, Whitten and Bentley, 2006)Transform knowledge at the boundary between social worlds (Carlile, 2002, Karsten et al., 2001)</td></tr><tr><td>Political</td><td>Form shared political representations, i.e. agreements, contracts, “sign-offs,” memorandums of understanding, etc.Perspective sharing, i.e. making sense of other social world’s perspective. (Karsten et al., 2001)</td></tr><tr><td rowspan="2">Transform Design Knowledge</td><td rowspan="2">Manipulate, integrate and transform representations that will propel movement between design routines so as to facilitate finding a feasible functional solution and stabilize the political ecology</td><td>Functional</td><td>Move knowledge from ambiguous to specific; objective/goal to a problem; instable to stable; idea to solution (Henderson, 1991, Pohl, 1996)Realign operational structure to stabilize functional ecologyEnable design traceability (Ramesh and Jarke, 2001)</td></tr><tr><td>Political</td><td>Hand-off of power and control from provider to recipient world(s) (Carlile, 2002)Realign power to stabilize political ecology (Fairholm, 1993, Markus, 1983)Enable agreements traceability</td></tr><tr><td rowspan="2">Mobilize for Design Action</td><td rowspan="2">Source and wield resources and power to propel progress along a design path.</td><td>Functional</td><td>Participate in SAD routines as to invite functional expertise, review solutions, etc.) (Henderson, 1991)Reduce problem ambiguity for solution discovery in a design pathConscribe expertise relevant for problem identification and solution (Henderson, 1991)</td></tr><tr><td>Political</td><td>Participate in decision making, mobilization of resources and allocation of design tasks (Hirscheim et al., 1995)Mobilize bias towards preferred resolution (Hirscheim et al., 1995)</td></tr><tr><td rowspan="2">Legitimize Design Knowledge</td><td rowspan="2">Grant a legitimate status to a boundary object through validation of its content as to align with the stakeholders’ intent.</td><td>Functional</td><td>Certify, verify and validate the truthfulness and correctness of design knowledge (Henderson, 1991)</td></tr><tr><td>Political</td><td>Demonstrate acceptability of goal(s), problem(s) and solution(s) in the given institutional order as to authorize the movement of design knowledge across social worlds (Bergman et al., 2002a)</td></tr></table>

## DBO Features in Context

To understand how each of feature of a DBO is critical for design, consider as an example how groups of engineers use engineering design layouts (Carlile, 2002; Henderson, 1991). First, engineering design layouts convey representations that can be shared between social worlds based on a shared syntax and semantics. They transform the knowledge in order to further refine design knowledge within and across engineering teams. Design layouts also indicate when to mobilize engineers for action, i.e., they invite or conscript those with the required functional expertise and resources to participate in a design procedure (Carlile, 2002), as well as indicate what the most likely next design step activities should be. Finally, design layouts need to meet standards and quality criteria of engineering work in order to be legitimate. We will now discuss each of these roles in more detail.

From a functional ecology perspective, design is about generating and sharing functional representations, i.e., generating and sharing design knowledge through representations from the provider to the recipient via a set of boundary objects. Positioning a design boundary object between a provider and a recipient mobilizes and invites action in the recipient's social world. Design routines are enacted to transform the shared representation into a more specific and refined design boundary object (Dennis and Wixom, 2003; Pohl, 1996; Sommerville, 2000; Whitten et al., 2003). The process also adjusts and expands design knowledge between the provider's and recipient's social worlds (Truex et al., 1999). The goal of these routines is to clarify problems (i.e., reduce scope and ambiguity of design problems and requirements) or generate solutions (i.e., specify solution models, prototypes, and eventually actual systems that address problems). Finally, design boundary objects need to be legitimized as "correct" and "valid" so that the recipient social world will trust and rely upon them.

From a political perspective, design boundary objects encapsulate shared political agreements based on each world's perspective taking (Pfeffer, 1981, Pfeffer, 1992, Whitten and Bentley, 2006). For example, a comprehensive, non-conflicting requirements specification conveys an agreement among stakeholders (Lamsweerde, 2000, Lamsweerde et al., 1998). In contrast, competing design proposals (Bergman and Mark, 2002) or a requirements specification that never settles outstanding conflicts (Bergman et al., 2002b) conveys increasing disagreements among competing social worlds. The boundary objects also transform power and mobilize resources by inviting action. By agreeing, the recipient world complies with powers-that-be, and accepts control over the design. By disagreeing, the recipient world challenges the power base or questions the expertise residing in the provider world. This can lead to dropping the commitment, resistance, or a new round of negotiations in order to reach a compromise or a consensus (Bergman et al 2002b) $^{ix}$ . Agreements mobilize action to apply resources to execute agreed design activities. Disagreements – i.e., disconnecting a social world from the design or an effort to establish a different legitimacy within the political or functional ecology – mobilize action to either resolve questions about the political or functional legitimacy or to consider alternative design paths overseen by power structures. Both invite hand-offs between design routines and associated social worlds, thus refining or extending a design path. We will next examine how these four critical features shape the choice of design paths and help identify, share, and transform design knowledge across social worlds that influences both the formation of functional and political ecologies.

## A Case Study: Protoarchitectures and Project Plans as Design Boundary Objects

## Case Study Site

In the case study, we investigated a complex SAD process followed in the Jet Propulsion Laboratory (JPL), a large aerospace organization this is one of NASA's main research laboratories. Our study sought to illustrate how the generation and selection of the next generation aerospace systems took place through sharing multiple design artifacts across diverse social worlds that helped generate and remove alternative design paths. The followed SAD process (and routines) were quite similar across all technologies considered during the study, ranging from complete software solutions (e.g., autonomous spacecraft control) to solutions that were mostly hardware based (e.g., inflatable/deployable structures for solar arrays and antennas). Most of the technologies chosen included significant hardware designs as well as significant software components, as their control systems contained software-based information and knowledge systems. $^{x}$

Our case study focused on project selection in the New Millennium Program (NMP), which, in SAD parlance, covers the early and high level requirements and project scoping and planning. In general, the NMP program selects technologies for space flight validation, and NASA provides a budget for starting up at least one new space flight validation cycle per year. The estimated cost to mature and test selected technologies is in the \$50 million range. Due to limited resources, only one to three technologies could be selected per cycle out of 80 to 100 proposed technologies. Through this and other programs, JPL works routinely with a plethora of academic, commercial, and governmental partners. As a result, JPL has a long established history of involving industrial partners and other NASA laboratories. Because designers in the NMP must adapt their processes to conform to those of other industrial partners, and vice versa, the challenges are quite similar with

Volume 8 ■ Issue 11 ■ Article 1

design challenges found across a broad spectrum of large, complex, and distributed software design processes typical in manufacturing, distribution, or service industries.

We conducted a longitudinal study that followed technology formulation and selection processes in the NMP. In particular, we examined what sorts of DBOs helped share and align design knowledge across social worlds during the project selection. We identified early on two families of DBOs for further investigation that seemed to directly affect design paths. The first design boundary object – a proto-architecture – was essential in reducing uncertainty in the early functional ecology by communicating complex technical knowledge across participating social worlds. The second design boundary object – a project plan – was crucial in reducing instability in the political ecology by stabilizing design routines over time and space and across social worlds. Project plans informed social worlds about the scope and need for designs, their feasibility, and expected costs and the duration of the design. They also conscribed actors across social worlds and mobilized them for action. Though we observed other design boundary objects in our study, these two were the most interesting ones as they were present in multiple SAD steps and were crucial for the success or failure of a particular proposed design. Further, they served as useful examples of DBOs since a proto-architecture represents a design product (meta-design artifact), while a project plan represents an artifact about a design process (Walls et al., 1992).

## Research Methods

We observed NMP's SAD processes in vivo by using ethnography (Emerson et al., 1995; Forsythe, 1999; Glaser and Strauss, 1967; Hughes et al., 1994; Strauss and Corbin, 1998). $^{xi}$ Over a year and a half, we observed four NMP validation cycles. that included hundreds of technologies, which represented hundreds of possible design paths within the four selection cycles.

We applied ethnographic fieldwork methods (Lofland and Lofland, 1995, Pare and Elam, 1997, Strauss and Corbin, 1998) to capture in detail processes used for technology selection. The approach we followed was similar to those that have been used to understand how organizations design, maintain, or repair technology (Orr, 1996) or design new systems (Bellotti and Smith, 2000, Pankoke-Babatz et al., 1997). We applied analytic qualitative techniques to reproduce design processes as observed and uncover differences between documented versus observed practices. This allowed us to identify how DBOs were constructed and applied during each process and how they related to shared routines.

Data collection consisted of: 1) participant observation over five months of the space flight validation process, 2) 46 semi-structured interviews with NMP members (one NASA principal) and 34 group meetings, 3) informal and semi-formal discussions with small groups and JPL members, 4) attendance at five detailed technical presentations of the NMP process, and 5) the study of hundreds of related documents, slide sets, and papers that described the NMP process (Li, 2000, Minning et al., 2000). All interviews and many of the group discussions were audio recorded and transcribed.

The analysis compared the process as professed and documented in routines, usually via documents and slide presentations, and the actual process as enacted (Star and Strauss, 1999). Using an auto-driving method of data review (Belk et al., 1988), we validated the correctness of the observed processes with the NMP staff, who were insistent on making sure that we understood the technical and procedural details correctly. After we had obtained the process description, we analyzed roles that proto-architectures and project plans played in integrating heterogeneous knowledge and aligning political interests. We analyzed what knowledge was identified and transferred, how, by whom, how the actors were conscribed, and how the objects were transformed over the SAD process.

## The NMP Design Practice

The NMP program validates new technologies in space (Li, 2000). Many new technologies are often considered too risky for space missions and hence are off-limits to actual missions. Yet, science missions need new technologies to reduce the cost, allow new types of measurement and enable new capabilities. The NMP was created to help resolve this innovation dilemma. To this end, they mandate the NMP to conduct a “fair and open” competition to determine which technologies should be selected for flight validation. As an NMP manager mentioned: “(This is a competition) between what is the most important thing to do and who can participate or not.”

The NMP selection process follows a formulation-refinement-selection routine (Error! Reference source not found.). $^{xii}$ Fundamentally, the selection process forms multiple, parallel SAD processes that compete for a limited set of implementation resources. It starts by forming technical solutions to meet NMP's general sets of requirements as well as specific customer requirements (Table 2). The theme technologists are the main NMP customer contacts. They communicate technical capacity needs of missions that associate with broad space science research themes. As one technologist expressed, "Our customers are the theme technologists. The guys are the head technologists of all of their theme's missions."

![](/api/attachments/ZNR7S4K8/fulltext/images/3bff8f7c6c8bb17bcec8c06b1162a966aeab53aaa7fb78dc035e46889db09bb4.jpg)

![](/api/attachments/ZNR7S4K8/fulltext/images/7f26caeff36bf15292f2e52cba1ca03dbdeba6531fb7947a0b709ce87e394c43.jpg)

They know what they want." Themes include topics like: Exploration of the Solar System, Sun Earth Connection, Structure & Evolution of The Universe, or Astronomical Search for Origins. $^{xiii}$ The NMP technologists interview the theme technologists who are the subject matter experts as well as the customers of NMP about their technology needs. $^{xiv}$ A sample of these technical capability needs is provided in Table 4. $^{xv}$

The table shows that the technical needs are quite diverse and cannot be rectified by any one single or a small set of technologies. Therefore NMP looks often, beyond a single technology in making its choices about candidates so as to select technologies that represent a family of technological capabilities (America and Wijgerden, 2000, Thompson and Heimdahl, 2001), i.e., scopeable and scalable sets of solutions. One technologist expressed this as follows: "We want to test a range of capabilities in a technology, not an instance. We want it to represent a set of capabilities. Ion engines can be made big or small. They can be grouped together in clusters. That is what we are looking for in technologies. Scalability."

Each selected project candidate covers a subset of the requirements, while a specific union of the candidates would cover the complete set of requirements. Hence, each technology viewed by the NMP as a solution candidate forms its own design path within the greater whole of the NMP lifecycle. Each such design path strings together many “repeatable” NMP design routines. Still, the outcome is never predetermined. Indeed, often issues arise, even late, that can radically alter a solution candidate’s design path. In addition, there are limited resources, so all possible project candidates cannot be funded. Therefore, only a few of the solution candidates are selected for space validation per selection cycle, requiring fierce negotiation and skillful mobilization of the political ecology. Consequently, many customer requirements for one reason or another go unfulfilled in any NMP cycle.

## Design Social Worlds within NMP

We recognized different social worlds at JPL by identifying critical alignments between power levels and diverse engineering expertise. Accordingly, we observed three broad social worlds: organizational, project, and technical (Bergman and Mark, 2003):

Organizational – Actors with organizational authority typically possess a combination of multiple systems engineering expertise and organizational (across multiple projects) management authority. People in this role have the power to start new projects and bring resources to fund the activity. They can also change and end projects. We also call these actors 'NMP principals'.

![](/api/attachments/ZNR7S4K8/fulltext/images/5a1f1a38d5a035473b77f7819b586506ef891afb6531516b5ff9aee79660efdc.jpg)

Project – Actors with project authority possess a combination of system level engineering expertise and system/sub-system level management authority.

Technical – Actors with technical authority possess a combination of engineering expertise across a family of technologies and the organizational position power to identify technologies that need flight validation.

Each NMP participant belongs to least one social world (Table 2). Each participant is dependent on the social world he or she is working with or representing to another social world (Bergman and Buehler, 2003, Bergman and Mark, 2003). All social worlds have one or more leaders in NASA, and more specifically within JPL and NMP. In addition, those with higher authority can override the needs and decisions of those with a lower level of authority. This power difference has to be accounted for in resolving political ecology instabilities along a design path. In the case study, we labeled the NMP social world with the highest design decision power ‘Organizational’. This was followed by ‘Project’, which had the intermediate decision power, followed by ‘Technical’ (Table 2).

<table><tr><td colspan="3">Table 2. NMP&#x27;s Design Social Worlds</td></tr><tr><td>Design Social World</td><td>NMP Group</td><td>Comments</td></tr><tr><td>Organizational</td><td>NASA Administrators (aka NMP Principals)</td><td>Associate Administrators and Division Technologists or Leads</td></tr><tr><td rowspan="4">Project</td><td>NMP Managers</td><td>NMP Managers, NMP Chief Technologist, NMP Chief Architect</td></tr><tr><td>Independent Review Board (IRB)</td><td>Senior Systems Engineers (not associated with candidate projects)</td></tr><tr><td>Suppliers (Providers)</td><td>Technology Providers – Project and Program Managers, Sr. Technologists (government, industry, university).</td></tr><tr><td>System Review Committee (SRC)</td><td>Systems Project Managers and Senior Engineers (not associated with candidate systems)</td></tr><tr><td rowspan="6">Technical</td><td>Customers</td><td>Theme Technologists ( $TTs$ ) $^{xvi}$ </td></tr><tr><td>NMP Technologists</td><td>NMP Technologists or Technical Experts</td></tr><tr><td>Reviewers</td><td>Technologists or Technical Experts (not associated with candidate technologies or review panels)</td></tr><tr><td>Peer Review Panel (PRP)</td><td>Technologists or Technical Experts (not associated with candidate technologies)</td></tr><tr><td>Suppliers (Providers)</td><td>Technology Providers – Engineers and Technologists (government, industry, university).</td></tr><tr><td>System Review Committee (SRC)</td><td>Systems Engineers and Technologists (not associated with candidate systems)</td></tr></table>

## NMP stakeholder needs

All participating social worlds' needs had been reasonably met within the NMP selection process to generate a feasible selection. Therefore, NMP applied a multi-step and multi-level design process to determine which project candidates could be supported. Initial high-level project categories were determined based on the current (at the time of the start of the selection cycle) technical requirements of the NMP customers. NMP applied "web" of requirements, listed in Table 3 to these initial project categories. This list of requirements was developed over a 10-year period and filters out projects that do not initially fit NMP's mission. Therefore, the NMP technologists call these requirements "filters."

The candidates that survive the application of “filters” are then considered by the customers. They rate these candidates from best to worst. The candidates and the ratings are then sent to the project managers who apply general NASA project requirements rating the candidates against these criteria. At this stage, the candidates that fare the worst are culled. The remaining candidates are sent to the NASA administrators – i.e. NMP principals – who apply their own organizational requirements. They search for those candidates that possess the capabilities to support the maximum number of NASA missions and broad objectives. Based on their analysis, a final set of candidates is selected.

From the NMP point of view, these stages form a cumulative filtering process that identifies and removes poor designs, while leaving the "best" candidates for further design. Only those selected for implementation will be flight validated (Error! Reference source not found.). During this selection process, each social world applies its own criteria and commitments to define problems and solutions. Some requirements are shared across the worlds, e.g. cost, timelines, and risk. Yet, most requirements originate from within a single world, and are enforced solely by the associated authority (Table 2).

<table><tr><td colspan="3">Table 3. NMP “Filters”</td></tr><tr><td>High Level Requirement</td><td>Description</td><td>NMP Design Social World</td></tr><tr><td>Need Across Missions</td><td>How many (future) missions want this technology?</td><td>Organizational</td></tr><tr><td>Strength of Validation</td><td>Is the technology flexible enough to adapt to multiple different types of mission needs?</td><td>Organizational (across missions), Technical (per technology)</td></tr><tr><td>Cost</td><td>Can the technology be validated in budget?</td><td>Organizational (across missions), Project (project plan), Technical (per technology revision)</td></tr><tr><td>Timeliness</td><td>Will the technology be validated in a timeframe that is useful for missions that want to use it?</td><td>Project (project plan), Technical (per technology revision)</td></tr><tr><td>TRL (Technology Readiness Level)</td><td>Is the technology mature enough to be validated?</td><td>Project</td></tr><tr><td>Access to Space</td><td>How do we get the technology into space and where it needs to be for validation?</td><td>Project</td></tr><tr><td>Open and Fair Technology Competition</td><td>Does the technology come from a US provider? Is it allowed to be part of a US government technology bid competition?</td><td>Project</td></tr><tr><td>Flight Justification</td><td>Can this technology only be tested off of the earth, i.e. in space or extraterrestrial body?</td><td>Technical</td></tr></table>

## Examining NMP Design Boundary Objects in Practice

## TWO Families of Design boundary objects: proto-architectures and project plans

NMP technologists produced a family of design products early based on their conceptualization of technology combinations that could meet NMP's filters and a dedicated (sub)set of customer requirements. The NMP technologists called these artifacts 'proto-architectures'. These artifacts were deemed critical in progressing multiple and parallel SAD paths and clarifying the functional ecology early on. They helped address a series of gaps between different design routines initiated during the conceptualization. These gaps emerged between the systems analysis and decision phases and involved technical, project, and organizational worlds. A sample list of proto-architectures is presented in Table 4. As the table demonstrates, a wide, diverse set of technologies could be considered in any cycle and be represented as proto-architectures.

<table><tr><td>Table 4. Examples of NMP Proto-architectures</td></tr><tr><td>Examples of Protoarchitectures</td></tr><tr><td>Gossamer Telescope Systems</td></tr><tr><td>Active wavefront sensing and control of lightweight optical systems</td></tr><tr><td>10-100mN class precision control thrusters for distributed aperture observatories</td></tr><tr><td>Energy resolving detector arrays for submillimeter and UV astrophysics</td></tr><tr><td>5-10K instrument cryocoolers</td></tr><tr><td>Aeroassist and entry descent systems</td></tr><tr><td>Advanced radiation tolerant computing</td></tr><tr><td>Optical communication for outer solar system missions</td></tr><tr><td>Inflatable/deployable structures for solar arrays and antennas</td></tr><tr><td>Power sources and thermal management</td></tr><tr><td>Solar sails: Deployment test</td></tr><tr><td>Picosats: 5kg, 5W sats—platforms for Ionospheric, Magnetospheric, Heliospheric science, flight experiment to include science validation of platform</td></tr><tr><td>Ultra-low power electronics and avionics</td></tr><tr><td>Guidance, navigation and control: Sun and earth sensors for spinning s/c, Position information to 100m well above GPS constellation</td></tr><tr><td>Instrument technology: Compact plasma analyzers w/o large, complex electrostatic optics; Low-threshold, particle detector/analyzer (ions/neutrals, as low as 1keV energy)</td></tr><tr><td>Drag-free inertial sensor</td></tr><tr><td>Actuators for formation flying: tethers</td></tr><tr><td>Autonomous spacecraft control, coordination, and pointing</td></tr><tr><td>Light, large, deployable, high-precision structures</td></tr><tr><td>Cryocoolers: Mirrors and sensors</td></tr><tr><td>Gossamer X-ray optics</td></tr></table>

Project plans extended and refined the design knowledge expressed in technology proposals. They formed key instruments in bridging the gap between the request for proposals (RFP) by the NMP – i.e. submitted technology proposals and final technology proposal selection. In so doing, they defined and coordinated various functional ecologies represented by the competing proposals. In parallel, project plans were utilized to bridge gaps among the NMP, theme technologists (NMP customers), and technology developers (those who supplied the proposals and if awarded, would lead the detailed design and build the new technologies). As such, project plans were instrumental in stabilizing the political ecology by aligning the actors across social worlds into a concerted design effort.

## Design Boundary Object Features in Action

The four features of a design boundary object outlined above indicate whether it is gaining or losing support. The design boundary object features can thus be applied as feature indicators of “successful progress” or “impeding problems” in design. In this section, we explore how these four features were successfully deployed to form successful DBO artifacts – proto-architectures and project plans during the NMP initiative. We also discuss how these features can raise “red flags” about problematic candidates. As such, this information could be acted upon to rescue a candidate functionally or politically. It could also be used to “cut losses” and end a design path that already was severely compromised. Hence, an understanding of design boundary object quality can be used to anticipate design path navigation, $^{xvii}$

## Proto-architectures

Each design candidate was modeled as a proto-architecture to establish an initial proof of design concept. The NMP staff used the term ‘concept’ to mean a design project or idea. Each concept was represented by a ‘quad-chart’. One NMP technologist expressed this as follows: “We create a quad-chart for every concept. It has all of the information we need on one page. It has taken us 8 years to get them right.”

![](/api/attachments/ZNR7S4K8/fulltext/images/5fcffabf4a0ec356caa189784a4f2f85c0336ac5dc6c811a29d2e7d059bdb903.jpg)

Validation Objective: Validate deployment, and characterize effect of space environment on deployed sails for future mission use

\- Characterize structural mechanics and dynamics of the deployment of a solar sail.

\- Characterize the behavior of a deployed sail section
- Assess the combined effects of space environment on sail shape. Environmental effects include microgravity, solar radiation pressure, static charging, and thermal deformations.

\- Validate models to enable scalability for larger sail sections in complete sail systems.

Flight Validation Rationale: Microgravity deployment dynamics cannot be simulated in ground testing.

Suggested Flight Concept: Deploy a sail section from ELV upper stage or carrier spacecraft in GTO.

Cost Range: \~\$12M to \$18M

Missions Applicability:

SEC: SPI, Sub -L1S (Geostorm)

## Technology Requirements

\- Sail section area $>350 \mathrm{~m}^{2}$ - A real density 10 -20 g/m $^{2}$ , including sail film, booms, tensioning hardware, and any other hardware that must remain with the sail after deployment.

\- First mode frequency $>0.03\mathrm{Hz}$

• Film stress > 0.7 N/cm $^{2}$

• Thrust reduction from wrinkling < 5%

\- Successful deployment in space to full section shape without ripping, tearing, or excessive deformation
State of the Art:

• Russia has deployed 20m -diameter sail in space

\- DLR has developed prototype 20m sail
  - A real density $25\mathrm{g} / \mathrm{m}^2$

![](/api/attachments/ZNR7S4K8/fulltext/images/b4efb6d817204832bd32f69d5c2292ed3180ae857119ab4f582eec4491279aa2.jpg)

![](/api/attachments/ZNR7S4K8/fulltext/images/a8a82fa8e10a5ffcaa5f191d37b851ce2de927cc476107d2969dbd5b471bec27.jpg)

An example of a quad-chart is shown in Figure 2. It provides a concise, one-page summary of the key information about the proposed technology. It offers knowledge about the design and its solution and how it meets requirements. Each section of a quad-chart is written in a concise and simple manner so that it can easily traverse between design social worlds (Table 2). The quad-charts we observed contained four types of design knowledge:

(a) A picture of the requested technology (upper left),

(b) A Technology description, applicability, and cost range (lower left),

(c) Technology requirements (upper right), and

(d) A Technology Roadmap that places the technology within its development progression (lower right).

This knowledge was found to be the minimum necessary to communicate sufficient design detail across social worlds as well as to enable decision analysis within each social world.

Design Boundary Object Features of Proto-architectures

We next apply the four DBO features (Table 1) to illuminate: 1) each feature in the context of proto-architectures and 2) how and why proto-architectures form a critical design boundary object by having such features. We start with their role in the functional ecology.

Promote Shared Representation – The shared representations within quad-charts consist of system design pictures, graphs, technical descriptions, costs, timelines, and lists of capabilities and constraints. Quad-charts are common artifacts about designs applied across the whole research laboratory. They are simple enough to be understandable, yet detailed enough in different parts of the quad to provide enough information to all parties involved. NMP technologists and theme technologists are able to quickly determine technological capabilities and constraints of any proto-architecture, i.e., its functional ecology. This allows them to compare and contrast proposed technologies against their requirements. The NMP managers utilized the quad-charts constantly during their reviews. This resulted in making a recommendation for each proto-architecture (i.e. keep, questionable, or drop). Afterward, the results of these reviews $^{xviii}$ were sent along with the quad-charts to aid the organizational world in its decision making. This information was sufficient enough for NASA administrators to make their decisions.

Overall, proto-architectures had both sufficient detail and plasticity to make them shareable. They consisted of enough technical detail to clarify and define the problem-solution pairs as part of the functional ecology. They also enabled social worlds to judge, negotiate, recommend, and decide which technologies would receive their support. One interviewee clarified this:

"The theme technologists talk a lot to each other in these meetings. It is one of the few times they can all get together. They first want to know what the others need. Then, they do a lot of strategizing and deal making. They work together to pick what will work for all of them." ... "They use 'silver bullets' xix to show what they really want."

Further, an NMP manager mentioned:

"We use the results of the theme technologists' discussions to help inform..., make our decisions. We need to choose which concepts to keep or drop. We focus on different criteria...TRL, cost, and access to space. The quad-charts give us the information we need to make our ratings." xx

Hence, promoting shared proto-architectural representations was crucial for determining the functional ecology and stabilizing the political ecology. $^{xxi}$

Transformation – From the functional ecology perspective, a proto-architecture bridged the gap between early systems analysis — what NMP customers want and need — and design processes — how these wants and needs are met. NMP technologists created proto-architectures to meet general filters and high-level customer requirements. They bridged the gaps between requirements analysis and initial solution design, and they presented a framework of models under which a more detailed design could be developed. Proto-architectures were utilized in reviewing, rating, and selecting competing designs across the three design social worlds (i.e. technical, project, and organizational). Those in the technical world reviewed and rated by contrasting a proto-architecture against their own criteria. They also compared proto-architectures against one another. The resulting ratings augmented proto-architectures in communicating design knowledge to the project level and moving to the next SAD stage. xxii

Those in the project world considered the technical ratings and the proto-architectures together to generate their own recommendations. All of the lowest rated proto-architectures were culled during each step. The technical and project ratings and recommendations of the remaining proto-architectures were then sent to NMP principals in the organizational world. They discussed and negotiated amongst themselves to select which proto-architectures would form a basis for a request for (technology) proposals (RFP). The presentation of an RFP to industry, government, and universities signaled a transition from

Volume 8 ■ Issue 11 ■ Article 1

an internal SAD process to an external (i.e. open call) competition. xxiii Altogether, proto-architectures played a crucial transformative function across multiple design processes, as they traversed through multiple social worlds to move designs from ambiguous and general requirements to enough detail to inform specific requests for proposals.

From the viewpoint of political ecology, proto-architectures helped a shift from exploration of multiple initial positions to a stable political support for an RFP across social worlds. Initially, problems received ambiguous, general support and generated rough, initial requirements in the initial list. This set was analyzed by the technical world, which offered stronger support for those that met identified problems and requirements. The proto-architectures with good ratings and theme technologists' support were then recommended to the project world. Those in the project world supported a smaller subset of these proto-architectures. Finally, those in the organizational world lent their support only to a small set, usually 3 to 6 proto-architectures. Hence, we observed a stepwise consolidation of support to a few positions that transformed the political ecology from ambiguous, obscure and isolated, and competing to stable, clarified, and broad political support.

Mobilization to Action – The presentation of proto-architectures, along with their ratings and recommendations, mobilized action in each social world touched by the proto-architectures. Every knowledge gap incurred a mobilization of functional engagement necessary to produce the final selection for an RFP. Proto-architectures enabled this mobilization.

Functionally, to bridge the gap between requirements and the reviews of the competing design proposals, technologists were conscripted to form the initial proto-architectures. Then, theme technologists were called to technically review and recommend logical design concepts. Next, to narrow the gap between technical recommendations and project recommendations, NMP managers were conscripted from the project social world to report their ratings. NMP principals from the organizational social world were then called to select and support a few of the proposed proto-architectures. Finally, NMP technologists were once again mobilized to transform the selected proto-architectures into an RFP.

In parallel, the political ecology was mobilized to invite decisions that forged consensus across social worlds as echoed in the final selections. Indeed, if an agreement was not reached, the political support for a proto-architecture waned. This resulted in dropping the proto-architecture from further design.

Legitimization – Initial proto-architectures were made legitimate due to the high quality technical expertise drawn upon. Those proto-architectures that gained technical endorsements from customers also became functionally legitimized. The subset of proto-architectures that received project support received technical validation. This indicated that a proto-architecture represented a feasible combination of technologies and that these combinations could be successfully developed. Finally, the proto-architectures that gained organizational support became officially and fiscally legitimized across NASA as being critical to NASA's mission. Legitimization in the political ecology paralleled these actions. Per each recommendation step, the political “strength” behind the design was either increased or removed. This built up incrementally political legitimacy as the design progressed and the proto-architectures moved between the worlds, resulting in strong political legitimacy for the final choice.

## Project Plans

Design needs a unified, complex design boundary object that integrates and shares knowledge concerning needed design activities. It coordinates design activities, yet maintains separation between its components and associated social worlds. Normally, such boundary objects are called project plans (Dennis and Wixom, 2003, George et al., 2004, Laudon and Laudon, 2003). In the NMP, project plans conform to NASA standards. As per an NMP manager: “(A project plan is a) living document. It is constantly updated throughout all of the phases of a system design, flight and validation.”

Project plans unify action in that they represent how institutionalized social worlds come together to form and implement a viable functional and stable political ecology. Social worlds that are part of a project plan include: engineering – systems, electrical, mechanical, software, propulsion, communications, test and validation; science – biochemistry, physics, etc; project planning – cost, time, risk, and budget analysis; implementation (Error! Reference source not found.) – detailed design and build planning; and flight/infusion (Error! Reference source not found.) – mission planning. They also delineate the project organization – i.e., the authority, roles, and working relationships of those participating within a project. $^{xxiv}$ Hence, project plans consist of collections of plans, design artifacts, and project management information, and success criteria. $^{xxv}$

## Design boundary object Features of Project Plans

We again apply our features framework (Table 1) to have the specific project plans to illuminate 1) how each feature operates in the design context, as well as to show 2) how and why project plans form critical design boundary objects. We start with the functional ecology.

![](/api/attachments/ZNR7S4K8/fulltext/images/9c915dd37e231e3a5db14d05c7aa32046a16d4b376603c849ec14506ef9e2002.jpg)

Promote Shared Representation – Functionally, project plans includes shared representations that go beyond just communicating technical combinations and their requirements. They included budgets, risk assessments, specifications, and plans of design activity. An NMP manager declared “(Project) plans contain roadmaps. They show the direction of a technology, for future planning (by other space science missions).” Hence, the knowledge contained in a project was organized to explain and support SAD task breakdowns, critical paths, timelines, milestones, and schedules which cross, connect, and align social worlds. A project plan had to be made operational in each social world it inhabited, i.e., it had to be able to inscribe behaviors and invite responses in those worlds. Therefore, the people involved had to be able to understand what behaviors and results were expected and what was the set of rules and requirements that guided their responses. Engineers and other actors – financial planners, manufacturing technicians, mission planners, etc. – had to be able to understand, apply, and cohere to the plan. Project managers had to be able to manage the financial, time, and risk elements involved. They also had to be sure that the plan was being followed and was on track. The NASA administrators had to finally ensure that the plans were organizationally executable and the outcomes would further NASA objectives.

Politically, a project plan has to be applicable across all social worlds involved in a particular design path. These social worlds become interrelated to instigate, develop, implement, validate, and ultimately diffuse a new technology. In the NMP, this design path starts within the NASA administration, an organizational world. Eventually, it connects to the NMP managers (project world); as well as NMP technologists, theme technologists, and internal technology providers (technical world). Once a request for proposals is issued, the design path continues on to include industry, university, and government lab technology providers; as well as expert technical reviews and panelists from these domains. Those — first in the technical, and then in project worlds — execute design procedures that produce reviews, ratings, and recommendations on submitted project plans. The results prompt the design path trajectory to proceed back to the NASA administrators for final selection.

The importance of a project plan's shared representations does not end with the final selection. After selection, each plan is implemented by a project team comprised of members from the organizations involved in developing the new technology. Any large, complex system development project conscripts from a wide variety of social worlds. For NMP selected projects, those in mission planning, flight system acquisition, system production operations, test validation, and project resource oversight become part of the design path. Altogether, a project plan must contain shared representations that span a diverse chain of social worlds to enable, frame, focus, guide, and propel a project to form a feasible and ultimately successful design path.

Transformation – Functionally, a project plan outlines how a transformation from problems and requirements to implemented solutions takes place. Beyond that, it provides a governance framework in which design activities occur. By doing so, a project becomes a force in inviting, integrating, and transforming knowledge across all social worlds. A project plan advances knowledge mobilization, acquisition, and integration within and between design worlds to identify and address design issues. It provides the goals and motivation for the endeavor, its governance structure, and constraints and needs of the customers. In short, the plan dictates “the rules of the design path” that enable the design to proceed.

In addition, a project plan is one of the few design boundary objects that captures a holistic view of a design. This is necessary to facilitate the knowledge spillovers from design selection to implementation. Any data and models missing from a project plan will not be taken into account during this transition. This can result in critical knowledge not being recognized in connected social worlds during the implementation. Overall, we observed at the NMP that project plans were crucial in facilitating the transformation of knowledge during the key periods of design.

From the political ecology point of view, a project plan defines the power structure within the project. When agreed upon, the power becomes actualized in the design path, i.e., those in charge are allotted organizational power to manage personnel and resources to execute the plan. In a broader political context, project plans indicate a political reduction from possible design paths to actual, legitimized design path(s). In doing so, some principals will not get their desired problems recognized or addressed. Hence, those who get their projects funded increase their organizational position and resources compared to those who do not. This shapes the political ecology of the organization. $^{xxvi}$ Hence, project plans can be viewed as agents of organizational change, as they re-organize resource allocations and access across social worlds.

Mobilization for Action – Project plans reside in multiple design domains to facilitate sense-making between social worlds. They offer a means of communication to reduce design ambiguity and uncertainty. Moreover, they define the primary framework under which project design issues are identified and resolved. As Carlile (2002) suggests, a project plan must facilitate identification, gathering and application of knowledge necessary to develop a new system (Carlile, 2002). Without it, system design complexities have no functional basis (Davis et al., 1992, Laudon and Laudon, 2003, Maier and Rechtin, 2000). Without such structure, serious problems can emerge during implementation that threaten the viability of the design.

Hence, an important feature that makes a project plan functionally viable is how well it promotes the discovery of discrepancies across social worlds and provides mechanisms to address them.

Politically, a project plan is a call to action. It represents a managing framework for system design, which spans a wide array of social worlds. Those involved in formulating, selecting, or implementing a plan become conscripted. Indeed, those not involved are threatened to be left out of the design decision-making. This leaves non-participants in a position of political vulnerability, whereby events and outcomes will be dictated to them. For example, in the NMP, if a mission has a need for specific technology, it has to have a theme technologist present these needs to technologists to be considered for selection. If the theme technologist cannot or does not defend a desired technology, the selection process moves on without this technology. Accordingly, those who run the space missions would either not receive the technology they wanted or receive a technology that does not conform to their needs. Based on our observations, this is one reason why there were hundreds of project proposals submitted for each selection cycle. Losing political clout would result in desired projects not being funded and implemented, which could have a direct impact on mission planning and long-term NASA strategies. Therefore, project plans were a clarion call to political action.

Legitimization – Diverse technical domains required participants to apply heterogeneous expert knowledge to legitimize a project plan. We observed that as project plans went through reviews, ratings, recommendations, and selections, the plans either gained or lost the support of technical experts across NASA. An NMP manager exclaimed:

These are NASA, but NVI missions. They must conform to NASA roles. They must be accepted by NASA, not just as. Technical experts rated the overall feasibility of each project plan to determine: if followed, will the plan produce technically sound results that are achievable within a given budget and timeframe, while allowing for acceptable risk? Hence, principals from the organizational world took the results from experts and applied their own domain knowledge to determine whether a project plan would functionally fit within and promote the long term goals of NASA. We observed that the final acceptance of a project plan included acceptance of participants from all design social worlds, i.e., technical, project, and organizational (Table 2). Hence, the functional legitimacy of a project plan carried significant importance in the overall operation of NASA and indicated the significance of functional legitimacy achieved by these design boundary objects.

From the viewpoint of political ecology, agreements underpin all technical requirements and governance rules. In system design, a project plan represents a political agreement. It specifies governance structures as well as distribution of power and resources during the design. In the NMP, stakeholder consensus produced by moving through the selection lifecycle steps legitimized the project plan. This was reinforced when organizational power was wielded to fund and implement a selected plan. Conversely, plans that did not reach political consensus were dropped and became de-legitimized.

## Discovering design Issues

Our analysis might give the impression that the studied artifacts were always successful in mobilizing and transforming knowledge across social worlds. In actuality, very few proto-architectures and project plans survived the selection process. We observed that those proposals that were dropped did not enable, mobilize, integrate, or transform critical design knowledge at the boundaries as well as those proposals that succeeded. We can partly explain their failure because they poorly applied one or more of the design boundary object features. In general, we conclude that design boundary object features can become a useful design navigation guide.

Functionally, if a design boundary object involves technical problems that cannot be rectified, it must be dropped. Put simply, its functional legitimization is in question. An NMP technologist declared "If it (a technology) is not ready in time, it's dropped. It may continue to be matured by its own project team. But, it's not ready for NMP." This functional legitimization failure signals that adequate and believable knowledge was not identified and mobilized across social worlds. xxvii Still, there is no perfect design. Hence, functional aspects of a design are being constantly refined through the design until either it is deemed acceptable by a coalition of principals, or it is dropped. NMP called this the 'culling process'. xxviii

Furthermore, throughout the selection process, participants from the technical, project, and organizational social worlds applied different sets of requirements to determine, if a design would still be considered (Bergman and Buehler, 2003). They mobilized different realms of knowledge. In the NMP, the requirements were compared against the capabilities and constraints of proto-architectures to what is required for space flight validation. We observed that proto-architectures were called for various means, including cost, technological immaturity, or safety concerns, including:

"Will this technology endanger or destroy the space shuttle?"

"Does this technology impose a possible radiation risk to the planet (earth)?"

"Does the gravity of the Earth 300 miles out affect the validity of the fight test?"

"What do you think is the real cost of getting the technology ready and shot into space?"

![](/api/attachments/ZNR7S4K8/fulltext/images/e03bd56eccdf83b35cb0700016cc3efe137974eeee8673a704925f7202abb531.jpg)

Hence, even a well executed initial design could be dropped from consideration because it was too costly, dangerous, or was proposed too soon, or too late. These issues with nonfunctional requirements manifest themselves as failures of political mobilization. The opponents of a proto-architecture could draw upon functional legitimization and transformation of design knowledge to support their contention that the design had serious flaws to weaken its position in comparison to other proto-architectures. This showed up as lower ratings within the review panel. And, as the selection process moved on, the lower rated candidates were normally culled from the competition.

In general, as the contours of the design became clearer, the knowledge gaps became larger for problematic solutions. $^{xxix}$ As discussed, stakeholders gain knowledge from proto-architectures about design details and how they address requirements; they gain knowledge from project plans about the design process such as timelines, schedules, and roles. In the NMP, as cost and maturation information became more reliable, comparisons between competing candidates became starker. This made it easier for those rating, reviewing, and selecting to mobilize for or against various candidates. In addition, DBOs knowledge transformation could incur political failures. This could occur when those with institutional or organizational powers decided to move against stakeholders connected to a specific boundary object (Bergman et al., 2002b). We observed this at JPL in a variety of ways. Most of the proto-architectures would fit the requirements of theme technologists. But, some of these early designs were viewed to be too massive, bulky, dangerous, or power hungry (Bergman and Buehler, 2003). The technology itself was questioned, as it included undesired capabilities, constraints, and service demands. One interviewee expressed this vividly:

"Most technologies fit the TA (Technology Announcement $^{xx}$ ) fine. But, it was what else they had that can hurt them. Their size, shape, even the reputation of the provider makes a difference. If they were over budget or late before, that affects their ratings."

Project candidates that met technology requirements $^{xxxi}$ could not be guaranteed success. Their “detractor” qualities could inhibit eventual selection. When issues were raised by respected members of review committees, their expert opinions carried a great deal of weight. This motivated other members to drop their support by way of a lower rating or recommendation. In other words, important issues with the shared representation mobilized action against the project plan (or proto-architecture). This reduced the need for further knowledge transformation and resulted in politically de-legitimizing the candidate. Indeed, during the project plan reviews, the main reason cited for culling project plans was because of perceived and demonstrated negative requirements based on received design knowledge.

In summary, examining the four features of a DBO can indicate whether a particular design problem or solution is gathering or losing support. Those that are losing support should be re-examined to determine if changes can be made to rescue them. Conversely, those gaining support can become more assured of an increasingly likely successful outcome. In general, reviews of the design boundary objects features can be utilized as indicators of “successful progress” or “impeding issues” in design. Therefore, an understanding of the DBO quality by analyzing its features can improve design path navigation.

## Conclusions

In this paper we have demonstrated the critical role of boundary objects in advancing design. We defined design boundary objects by expanding earlier definitions of boundary objects with four essential features. These features are: the capability to promote shared representation, the capability to transform design knowledge, the capability to mobilize for design action, and the capability to legitimize design knowledge. These features can inform formulation of a design theory (Gregor, 2006), which recognizes design as a purposeful dance across functional and political ecologies. These features allow us richly describe the roles of DBOs in design. We illustrate the value of these four features by studying a complex technology selection process within the New Millennium Program (NMP) at the Jet Propulsion Laboratory (JPL). Our framework helped clarify the complexities and intricacies that needed to be overcome when design routines were enacted between diverse social worlds in the NMP. We observe that recognizing such needs is crucial if we are to develop SAD methodologies that help better incorporate organizational, political, and technical sensitivities of design into their guidelines.

In general, DBOs both enable and propel SAD processes. It is the flexibility of DBOs that allows them to successfully bridge social worlds, whereby designs can be continually refined into viable specifications that can invite political consensus. They are built and applied within and across design paths. These paths and associated design routines promote — through feedback — mappings between functional ecology resolution and political ecology stabilization. If the DBOs in these paths are “flawed” – as can be determined by examining their four features – the design process will most likely suffer and can be prematurely halted. Still, this feedback could “right the course” of a design path trajectory.

From a theoretical stance, we assert that design boundary objects augment current strands of design theory (Hevner et al 2004; March and Smith 1995; Walls et al., 1992) that have primarily focused on design tasks associated with specific design products or processes, but largely neglected broader issues of design sociology. The inclusion of design boundary objects into design theory vocabulary addresses an ontological weakness in the existing theorizing – in particular its lack of 1) the analysis connections between design products, processes, and ecologies, 2) the identification of “design propulsion forces” that define design paths and mobilize design process activities, and 3) acknowledgment of the roles of the functional and political ecologies in design, especially in determining successful and failed outcomes. This has direct implications on our thinking of design epistemologies, knowledge integration, and design product transformation. It helps articulate how design knowledge is produced, shared, and made legitimate both functionally and politically, as well as how such knowledge relates to procedural guidelines embedded in current SAD methodologies. We expect that such a proposed expanded view of design helps enhance SAD methodologies that are geared toward creating large software systems (Boehm, 1988, McConnell, 1996, Truex et al., 1999, Wood and Silver, 1995). Yet, additional research is needed to redefine design theories based upon in-depth observations of SAD practices involving knowledge acquisition, integration, and transformation that move in parallel with political alignment formation (or disintegration) across social worlds. We hope that investigations of this sort help improve design theory and in the end increase our success rate of designing large software systems.

## Acknowledgements

The research was supported by the National Science Foundation under grants no. 0205724, 0093496, and 0613606 and by the Center for Research on Information Technology and Organization (CRITO). The authors want to thank JAIS Senior editors and two reviewers for their constructive criticisms and JPL employees who contributed to this effort.

## References

Alvarez, R. and J. Urla (2002) "Tell me a good story: using narrative analysis to examine information requirements interviews during an ERP implementation," ACM SIGMIS Database (33) 1, pp. 38-52.

America, P. and J. Wijgerden (2000) "Requirements Modeling for Families of Complex Systems," Lecture Notes in Computer Science (1951pp. 199-209.

Belk, R. W., J. F. Sherry, and M. Wallendorf (1988) "A Naturalistic Inquiry to Buyer and Seller Behavior at a Swap Meet," Journal of Consumer Research (14) March, pp. 449-470.

Bellotti, V. and I. Smith. (2000) Informing the design of an information management system with iterative fieldwork. Symposium on Designing Interactive Systems, 2000, pp. 227-237.

Berg, M. and G. Bowker (1997) "The Multiple Bodies of the Medical Record," Sociological Quarterly (38) 3, pp. 513-537.

Bergman, M. and M. G. Buehler. (2003) Addressing an Inadequacy in Quantitative Analysis: Examining NMP Technology Selection. IEEE Aerospace 2003, Big Sky, MT, 2003 2.0504.

Bergman, M., J. L. King, and K. Lyytinen (2002a) "Large Scale Requirements Analysis as Heterogeneous Engineering," Scandinavian Journal of Information Systems (14pp. 37-55.

Bergman, M., J. L. King, and K. Lyytinen (2002b) "Large Scale Requirements Analysis Revisited: The need for Understanding the Political Ecology of Requirements Engineering," Requirements Engineering Journal (7) 3, pp. 152-171.

Bergman, M. and G. Mark. (2002) Exploring the Relationship between Project Selection and Requirements Analysis: An Empirical Study of the New Millennium Program. RE 2002, Essen, Germany, 2002, pp. 247-254.

Bergman, M. and G. Mark. (2003) In Situ Requirements Analysis: A Deeper Examination of the Relationship between Requirements Formation and Project Selection. RE 2003, Monterey, CA, 2003.

Bertelsen, O. W. (1996) The Festival Checklist: design as the transformation of artefacts. PDC '96, Palo Alto, 1996, pp. 93-101. Proceedings of the Participatory Design Conference.

Bertelsen, O. W. (1998) Elements of a Theory of Design Artefacts. Ph.D. dissertation, University of Aarhus.

Bertelsen, O. W. (2000) "Design artefacts: Towards a design-oriented epistemology," Scandinavian Journal of Information Systems (12).

Bijker, W. and J. Law (eds.) (1994) Shaping technology / building society: studies in sociotechnical change, Cambridge Ma: The MIT Press.

Bijker, W. E., T. P. Hughes, and T. J. Pinch (1987) The social construction of technological systems: new directions in the sociology and history of technology. Cambridge, Mass.: MIT Press.

B∅dker, S. (1998) "Understanding Representation in Design," Human-Computer Interaction (13pp. 107-125.

Boehm, B. W. (1988) "A spiral model of software development and enhancement," IEEE Computer (21) 5, pp. 61-72.

Boland R., and Collopy F. (eds) (2004) Managing as Designing. Stanford, CA Stanford University Press.

Bowker, G. and S. L. Star (1999) Sorting Things Out: Classification and Its Consequences. Cambridge, MA: MIT Press.

![](/api/attachments/ZNR7S4K8/fulltext/images/2db091d4d4be8dabe93a008e824b83ea67129418d1bdbe33071ead225854096d.jpg)

Briers, M. and W. F. Chua (2001) "The role of actor-networks and boundary objects in management accounting change: a field study of an implementation of activity-based costing," Accounting, Organizations, and Society (26pp. 237-269.

Carlile, P. R. (2002) "A Pragmatic view of Knowledge and Boundaries: Boundary Objects in New Product Development," Organizational Science (13) 4, pp. 442-455.

Clarke, A. (1991) Social Worlds/Arenas Theory as Organizational Theory, in D. Maines (Ed.) Social Organization and Social Process, New York: Aldine De Gruyter, pp. 119-158.

Dahl, R. A. (1991) Modern political analysis, 5th edition. Englewood Cliffs, N.J.: Prentice Hall.

Davis, G. B., A. S. Lee, K. R. Nickelss, S. Chatterjee et al. (1992) "SOS: Diagnosis of an Information Systems Failure- a framework and interpretive process," Information and Management (23pp. 293-318.

de Souza, C. R. B., D. Redmiles, G. Mark, J. Penix et al. (2003) Management of Interdependencies in Collaborative Software Development: A field study. ACM-IEEE International Symposium on Empirical Software Engineering (ISESE 2003), 2003.

Dennis, A. and B. H. Wixom (2003) Systems Analysis & Design, 2nd edition. Hoboken: Wiley.

Doerr, B. S., T. Venturella, R. Jha, C. D. Gill et al. (1999) Adaptive scheduling for real-time, embedded information systems. Digital Avionics Systems Conference, St Louis, MO, 1999, pp. 2.D.5-1 - 2.D.5-9.

Emerson, R. M., R. I. Fretz, and L. L. Shaw (1995) Writing Ethnographic Fieldnotes. Chicago, IL: University of Chicago Press. Fairholm, G. W. (1993) Organizational power politics: tactics in organizational leadership. Westport, Conn.: Praeger.

Forsythe, D. E. (1999) "It's Just a Matter of Common Sense": Ethnography as Invisible Work," JCSCW(8) 1/2, pp. 127-145.

George, J. F., D. Batra, J. S. Valacich, and J. A. Hoffer (2004) Object-Oriented Systems Analysis and Design, 1st edition. Upper Saddle River: Pearson/Prentice Hall.

Glaser, B. and A. Strauss (1967) The Discovery of Grounded Theory: Strategies for Qualitative Research. Chicago: Aldine Publishing Company.

Gregor, S. (2006) "The Nature of Theory in Information Systems," Management of Information Systems Quarterly (30) 3, pp. 611-642.

Gregor, S., and Jones D (2007) "The Anatomy of a Design Theory", Journal of the Association of Information Systems, (5), 8, pp. 312-335

Hage, J. (1980) Theories of Organizations. London: John Wiley & Sons Inc.

Hansen S., Berente N., Lyytinen K. (2007): "Principles of Requirements Processes at the Dawn of 21st Century", submitted to Informatics, earlier version available at www.case.weatherhead/requirements

Harper, R. H. R. and J. A. Hughes (1993) What a f-ing system! Send 'em all to the same place and then expect us to stop 'era hitting. Managing technology work in air traffic control, in G. Button (Ed.) Technology in Working Order. Studies of work, interaction, and technology, London: Routledge, pp. 127-144.

Heath, C. and P. Luff (1992) "Collaboration and Control. Crisis Management and Multimedia Technology in London Underground Control Rooms," Computer Supported Cooperative Work (1) 1-2, pp. 69-94.

Henderson, K. (1991) "Flexible sketches and inflexible data-bases: Visual communication, conscription devises and boundary objects in design engineering," Science Technology and Human Values (16) 4, pp. 448-473.

Hevner A., March S., Park J., Ram S. (2004): "Design Science in Information System Research", MIS Quarterly, 28, 1, pp. 75-105

Hirscheim, R. A., H. Klein, and K. Lyytinen (1995) Information Systems Development and Data Modeling, Conceptual and Philosophical Foundations. Cambridge: Cambridge University Press,.

Hoffer, J. A., J. F. George, and J. S. Valacich (2004) Modern Systems Analysis and Design, 4th edition. Upper Saddle River: Prentice Hall.

ter Hofstede A.H.M. and van der Weide, T.P., "Formalization of techniques: chopping down the methodology jungle", Information and Software Technology, 34(1), 1992, pp. 57-65

Hughes, J., V. King, T. Rodden, and H. Andersen. (1994) Moving out from the control room: ethnography in system design. CSCW, Chapel Hill, NC, 1994, pp. 429-439.

livari, J., R. Hirschheim, and H. K. Klein (2004) "Towards a distinctive body of knowledge for Information Systems experts: coding ISD process knowledge in two IS journals," Information Systems Journal (14) 4, pp. 313-342.

Karsten, H., K. Lyytinen, M. Hurskainen, and T. Koskelainen (2001) "Crossing boundaries and conscripting participation: representing and integrating knowledge in a paper machinery project," European Journal of Information Systems (10pp. 89-98.

Kendall, K. E. and J. E. Kendall (2004) Systems Analysis and Design, 6th edition. Upper Saddle River: Prentice Hall.

King, J. L. and P. Forster (1995) Information Infrastructure Standards in Heterogeneous Sectors: Lessons from the Worldwide Air Cargo Community, in B. Kahin and J. Abbate (Eds.) Standards Policy for Information Infrastructure, Cambridge, MA: MIT Press, pp. 653-667.

Kotonya R. and Sommerville I. (1998) Requirements Engineering, John Wiley&Sons, Chichester

Kwon, T. H. and R. W. Zmud (1987) Unifying the Fragmented Models of Information Systems Implementation, in R. Boland and R. A. Hirscheim (Eds.) Critical Issues in Information Systems Research, Chichester, England: Wiley, pp. 227-251.

Lamsweerde, A. v. (2000) Requirements engineering in the year 00: a research perspective. 22nd International Conference on Software Engineering, Limerick, Ireland, 2000, pp. 5-19.

Lamsweerde, A. v., R. Darimont, and E. Letier (1998) "Managing Conflicts in Goal-Driven Requirements Engineering," IEEE Transactions on Software Engineering (24) 11, pp. 908-926.

Lamsweerde, A. v. and E. Letier (2000) "Handling Obstacles in Goal-Oriented Requirements Engineering," IEEE Transactions on Software Engineering (26) 10, pp. 978-1005.

Laudon, K. C. and J. P. Laudon (2003) Management Information Systems, 8th edition: Prentice Hall.

Li, F. K. (2000) New Millennium Program Plan. NASA, JPL.

Littlejohn, K., M. V. DelPrincipe, and J. D. Preston (2000) "Embedded information system re-engineering," IEEE Aerospace and Electronic Systems Magazine (15) 11, pp. 3-7.

Lofland, J. and L. H. Lofland (1995) Analyzing social settings: a guide to qualitative observation and analysis, 3rd edition. Belmont, Calif.: Wadsworth.

Lutters, W. G. and M. S. Ackerman. (2002) Achieving Safety: A Field Study of Boundary Objects in Aircraft Technical Support. CSCW, New Orleans, LA, 2002, pp. 266-275.

Leppänen M. (2005): "An ontological Framework and Methodical Skeleton for Method Engineering- A contextual approach", PhD Thesis, University of Jyväskylä,

March S., Smith J. (1995): "Design and Natural Science Research on Information Technology", Decision Support Systems, 15, 4, pp 251-266.

Lyytinen, K. (1987) "Different perspectives on information systems: problems and solutions," ACM Computing Surveys (CSUR) (19) 1, pp. 5-46.

Maier, M. and E. Rechtin (2000) The Art of Systems Architecting, 2nd edition. Boca Raton: CRC Press.

Marakas, G. M. (2006) Systems Analysis & Design, 2nd edition. New York: McGraw-Hill/Irwin.

March, J. G. and J. P. Olsen (1976) Ambiguity and choice in organizations. Bergen: Universitetsforlaget.

Mark, G. (2002) "Extreme Collaboration," Communications of ACM (45) 6, pp. 89-93.

Markus, M. L. (1983) "Power, Politics and MIS implementation," Communications of the ACM (26pp. 430 - 444.

Markus, M. L. and M. Keil (1994) "If We Build It, They Will Come - Designing Information Systems That People Want to Use," Sloan Management Review (35) 4, pp. 11-25.

Markus, M. L., A. Majchrzak, and L. Gasser (2002) "A Design Theory for Systems that Support Emergent Knowledge Processes," MIS Quarterly (26) 3, pp. 179-212.

McConnell, S. (1996) Rapid Development, 1st edition. Seattle: Microsoft Press.

Minning, C. P., M. G. Buehler, T. Fujita, F. Lansing et al. (2000) Technology Selection and Validation on New Millennium Flight Projects. Aerospace 2000, Big Sky, MT, 2000.

Mumford, E. (2003) Redesigning Human Systems. Hershey, PA: Information Science Publishing.

Orlikowski, W. J. and D. C. Gash (1994) Technological frames: making sense of information technology in organizations, in ACM Transactions on Information Systems, vol. 12, pp. 174.

Orr, J. E. (1996) Talking about machines: an ethnography of a modern job. Ithaca, N.Y.: ILR Press.

Pankoke-Babatz, U., G. Mark, and K. Klöckner. (1997) Design in the PoliTeam- project: evaluating user needs in real work practice. DIS, Amsterdam, The Netherlands, 1997, pp. 277-287.

Pare, G. and J. Elam (1997) Using Case Study Research to Build Theories of IT Implementation, in J. L. Allen S. Lee, and

Pfeffer, J. (1981) Power in organizations. Marshfield, Mass.: Pitman Pub.

Pfeffer, J. (1992) Managing with power: politics and influence in organizations. Boston, Mass.: Harvard Business School Press.

Pohl, K. (1996) Process-centered requirements engineering. New York, NY: Wiley.

Ramesh, B. and M. Jarke (2001) "Toward reference models for requirements traceability," IEEE Transactions on Software Engineering (27) 1, pp. 58-93.

Simon, H. A. (1996) The Sciences of the Artificial, 3rd edition. Cambridge, Mass.: MIT Press.

Sommerville, I. (2000) Software Engineering, 6th edition: Addison-Wesley.

Star, S. L. and J. R. Griesemer (1989) "Institutional Ecology, 'Translations' and Boundary Objects: Amateurs and Professionals in Berkeley's Museum of Vertebrate Zoology, 1907-39," Social Studies of Science (19pp. 387-420.

Star, S. L. and A. Strauss (1999) "Layers of Silence, Arenas of Voice: The Ecology of Visible and Invisible Work," JCSCW(8) 1/2, pp. 9-30.

Strauss, A. (1978) A Social Worlds Perspective, in, vol. 1 N. Denzin (Ed.) Studies in Symbolic Interaction, Greenwich, CT: JAI Press, pp. 119-128.

Strauss, A. L. and J. M. Corbin (1998) Basics of qualitative research: techniques and procedures for developing grounded theory, 2nd edition. Thousand Oaks: Sage Publications.

![](/api/attachments/ZNR7S4K8/fulltext/images/07139f4f6ebee665ca097de3ec47c8de3f3da68c635818cf0bab7a69a0adca20.jpg)

Sutcliffe, A. and B. Gault (2004) "The ISRE Method for Analyzing System Requirements with Virtual Prototypes," Systems Engineering (7) 2, pp. 123-143.

Thompson, J. M. and M. P. E. Heimdahl. (2001) Extending the Product Family Approach to Support n-Dimensional and Hierarchical Product Lines. RE'01, Toronto, Canada, 2001, pp. 56-64.

Truex, D. P., R. Baskerville, and H. Klein (1999) "Growing systems in emergent organizations," Communications of the ACM (42) 8, pp. 117 - 123.

Walls, J. G., G. R. Widmeyer, and O. A. El Sawy (1992) "Building an Information System Design Theory for Vigilant EIS," Information Systems Research (3) 1, pp. 36-59.

Whitten, J. L. and L. D. Bentley (2006) Systems Analysis & Design Methods, 7th edition. New York: McGraw-Hill/Irwin.

Whitten, J. L., L. D. Bentley, and K. Dittman (2003) Systems Analysis & Design Methods, 6th edition. New York: McGraw-Hill/Irwin.

Wood, J. and D. Silver (1995) Joint Application Development, 2nd edition. New York: John Wiley & Sons.

Yu, E. (1997) Towards modelling and reasoning support for early-phase requirements engineering. Requirements

Engineering, The Third International Symposium, Annapolis, MD, 1997, pp. 226-235.

$^{i}$ Our work fits with Gregor's Type I Theory – Theory for analyzing. (Gregor 2006)--since it is about describing a critical aspect of design, i.e. design boundary objects. It also informs her type five theory: Theory for Design and Action. As a theory of analyzing it is aimed at formulating classifications and patterns through vocabulary, concepts, metaphors etc. that make it possible to make sense of a complex design processes and their dynamics and outcomes. It can thus later offer a basis for formulating prescriptive/normative artifacts to guide/support design-theory of design and action.

$^{ii}$ The “gap” concept is similar to that espoused Hage, J. (1980). Hage discusses that an impetus to action of an organization is the gap between what is and what could be. We tighten this definition somewhat by applying Simon, (1996). He focuses design on gaps between what is and what should be. Hence, there is a more directed and concerted thought behind the selection of the gaps, i.e. problems, the resources required to address them, and the expected benefits of “crossing the gap.”

$^{iii}$ This power can be indirect, such as the influence exerted by important user groups, professional societies, legal institutions (i.e. governments), and key customers, suppliers, or users. Still, even these groups' voices can only be heard if they are given the organizational authority to influence the determination of design problems and solutions.

$^{iv}$ In the SAD literature, principals are sometimes known as business or process owners (Whitten, and Bentley (2006, Hoffer and Valacich 2004, Kendall and Kendall 2004). Those who have the power to direct or influence the course of a design path are called stakeholders. This includes, customers and user groups, suppliers, managers, technologists and other experts, SAD analysts and designers, system builders, lawyers, and so forth. In general, principals have political authority over other stakeholders during design due to their control of both authority and resource power Bergman, et al., (2002b).

$^{v}$ An SAD exercise is any application of systems analysis and design methods to produce new or modified system(s) in order to solve stakeholders' problems or realize opportunities.

$^{vi}$ This follows from the use of ecology in sociology that is concerned with “the spacing and interdependence of people and institutions” (The Random House College Dictionary, 1988). Here it defined as spacing and interdependence between actors, systems, functions and institutions.

Feasibility analysis is a large subject area unto itself and beyond the scope of this paper. General definitions of four feasibility areas are as follows: Operation feasibility refers to the processes and operating procedures of an organization and examines the impact of the proposed change on these organizational operations. Technical feasibility examines the questions: "How can this system be designed and built?" "What are its capabilities and constraints?" "Does the project have access to the necessary expertise to create the system?" "Should the system be built or bought, or a combination of Consumer-Off-The-Shelf (COTS) and customer work?" Economic feasibility examines the cost-benefit of proposed solutions and their risk-reward tradeoffs. Schedule feasibility explores whether design can produce a system can be delivered on time, as well as within budget, satisfying the stakeholders' requirements.

viii It is possible that no viable solution is either functionally feasible or politically stable. The London Stock Market “Big Bang” is an example of this (Bergman et al., 2002a), where both irresolvable political tensions and technical immaturity contributed to the multi-billion failure.

$^{ix}$ It is possible that there are no functional issues and political conflicts contained with a provider's design boundary object. We do not intend to imply a deterministic view of design path choice. Instead, DBOs are utilized to reduce gaps between design procedures, but they do not determine the direction or ultimate success of a chosen path which is controlled by the stakeholders—primarily the principals.

\* The technologies designed during the NMP process do not in general resemble information systems seen in organizations although some technologies, like the space internet build upon similar foundation. These are mostly embedded information systems that involve complex system engineering tasks (Doerr et al., 1999, Littlejohn, K. et al., 2000). At the same time they involve design tasks that are similar to ones faced when a complex IS must be embedded into an organization (Yu, E., 1997, Alvarez, R. and J. Urla, 2002). Therefore, their design involves deployment of similar SAD methods as during the design of more traditional information systems and their design products and processes have similarities. These systems are not subject to as much post-production change as organizational IS due to the constraints set up by space flight and embedded hardware. Yet, insights obtained from the SAD processes and the use of design products applied to building these systems illuminate also complex design ecologies typical to many IS development situations. Therefore, our study can help inform also typical SAD practices. Organizational IS development may have, however, more specialized SAD processes and ecologies which need to be revealed by future research.

Volume 8 ■ Issue 11 ■ Article 1

![](/api/attachments/ZNR7S4K8/fulltext/images/fdbdb5d9df354f82a9cb56875600170c4e1a430c328fcc9b056ce9ff81c6a5f4.jpg)

$^{xi}$ This paper only reports on a subset of the findings, i.e. those findings that inform the use of design boundary objects in the design procedures applied by the New Millennium Program with in JPL.

$^{xii}$ An examination of the relationships between formulation and implementation (i.e. detailed design and building of a system) and flight/infusion (i.e. sending the flight system into space, executing the validation mission, and infusing the validated technology to the NASA customers) is beyond the scope of this paper.

xiii To find out more about space science themes, go to the NASA website at http://www.nasa.gov/home/index.html.

$^{xiv}$ Theme technologists are “extreme” customers. Each of them has multiple decades of experience. They are world-class experts in their fields. They know technology and space flight intimately. Hence, they are “extreme” as compared to an average consumer customer. Still, in highly specialized organizations, i.e. healthcare, avionics and aerospace, utilities, defense, media, and finance industries, it is not unusually to interact with highly qualified customers. Hence, we assert the customer base of NMP is a representative sample the “extreme” customer base in industry.

$^{xv}$ These technical requirements were for the ST8 (Space Technology 8) NMP selection cycle.(Bergman and Buehler 2003).

$^{xvi}$ Each Theme Technologist represents a large social (i.e. a NASA Theme). Still, collectively, they form the NMP customers' social world.

$^{xvii}$ Determining how to measure design boundary object quality is the subject further research.

$^{xviii}$ The review results by the technical social world became a design boundary object for the subsequent project social world. The review results of the project social world became another DBO (along with the technical results DBO) for the organizational social world. In addition, the project results were examined by the technical social world before they were sent to the organizational social world to allow some reflection and refinement of proto-architectures. The organizational social world's recommendations and selection became a DBO for the project and technical social worlds that was utilized to examine and refine the design and review procedures for the next NMP selection cycle. This design procedure is documented in Bergman and Buehler (2003).

$^{xix}$ The reference to ‘silver bullet’ here refers to the idea that there was no single way to address the theme technologists’ requirements.

$^{xx}$ The details of this process are discussed in much greater detail in Bergman and Buehler (2003).

$^{xxi}$ Those proto-architectures that were rated lowly incurred a destabilization of a political ecology. In other words, bad ratings and recommendations reduced political support by one or more design social worlds. This loss of support resulted in the proto-architecture being culled from further consideration.

xxii Ratings were contained in their own document, separate from proto-architecture quad-charts. These ratings documents were thus also design boundary objects.

xxiii Proto-architectures were supplanted by an RFP and thus were not part of this competition. RFPs are also important design boundary objects.

$^{xxiv}$ These were called pre-alpha, alpha, and beta-teams. The project team structure changed and become more detailed as a project progressed.

$^{xxv}$ There is nothing in the boundary object properties to prevent a boundary object from being composed of many “subobjects.” Indeed, it is arguable that many boundary objects consist of many isolated, yet related parts that make it a functional whole, yet plastic enough to fit across multiple social worlds. For example, an airway bill has many different sections. It has a customer section (origin and destination information), contents, authorizations, and delivery history. Each of these is useful for different groups (i.e. social worlds) that deal with a delivered item individually. Together, it is useful for the whole delivery process. See King and Forster (1995) for a further discussion of airway bills and the cargo transfer process.

$^{xxvi}$ It should be noted that everyone participating in NMP project knew the political stakes of winning and losing, i.e. being or not being selected for funding. Hence, the employed design selection process had to account for the expected dissent to the results. This is one of the main reasons why NMP had many selection cycles, at least one a year. This allowed the “losers” to try again and become “winners” in future. The aim of this policy was to lessen the resistance to selected winners by allowing losers another shot in the next round. Hence, we observed that the NMP selection process sought to balance functional and political ecology needs through their design processes.

xxvii As witnessed in ST5 (an NMP selection cycle), a coordinated flight project was severely threatened by the discovery of a cable that had not been space flight validated and considered too technically immature to be part of the design. "Do the flex cables that connect the boards need to be validated? We don't know how they perform in space. Still, they are just ribbon cables. Do we have to wait to validate the whole system on the next cycle until after the flex cables are validated?" The guiding NMP technologist and the project candidate team leaders worked feverishly over six weeks to discuss and resolve this problem with concerned system engineers and NASA experts. They finally reached a compromise to include the cable as part of the flight test plan. Other observed technical candidates either did not make this effort or could not find convincing enough data to support their view. These candidates were subsequently dropped.

xxviii Culling processes are quite common across SAD practice (Maier and Rechtin 2000). Without culling competing designs, no consensus could ever be reached as to which design(s) are selected to focus resources and attention. This “reduction process” is necessary in order to focus attention and resources on building a functionally viable and politically acceptable system.

$^{xxix}$ In addition, as design knowledge becomes clearer, the true complexity of problems emerges. This can radically alter a design path to re-consider and better define the design problem(s) and then reconsider the solutions. The danger in doing this can be a substantial loss of political support.

$^{xxx}$ NMP called their request for proposals (RFP) “technology announcements” (TA). This was later changed in ST8 to fit with the more commonly used NASA term.

$^{ii}$ These requirements are stated in requests for proposals derived from protoarchitectures.

## About the Authors

Kalle Lyytinen is Iris S. Wolstein professor Case Western Reserve University, USA, adjunct professor at University of Jyvaskyla, Finland, and visiting professor at University of Loughborough U.K. He serves currently on the editorial boards of several leading information systems journals including Journal of AIS (Editor-in-Chief), Journal of Strategic Information Systems, Information&Organization, Requirements Engineering Journal, Information Systems Journal, Scandinavian Journal of Information Systems, Journal of Information Technology, and Information Technology and People, among others. He is AIS fellow (2004), and the former chairperson of IFIP 8.2 and a founding member of SIGSAND. He also led the research team that developed and implemented MetaEdit+ which is the leading domain modeling and metaCASE platform globally. He has published over 180 scientific articles and conference papers and edited or written eleven books on topics related to nature of IS discipline, system design, method engineering, organizational implementation, risk assessment, computer supported cooperative work, standardization, and ubiquitous computing. He is currently involved in research projects that looks at the IT induced radical innovation in software development, IT innovation in architecture, engineering and construction industry, requirements discovery, modeling and coordination for large scale systems, and the adoption of broadband wireless services in the U.K., South Korea and the U.S.

Mark Bergman is an Assistant Professor of Information Sciences within the Graduate School of Operations and Information Science (GSOIS) at the Naval Postgraduate School in Monterey, CA. His current research interests are on modernizing systems analysis and design methodologies based on understanding what differentiates poor, good, and great systems. Furthermore, he has general interests in socio-technical systems analysis and design, computer supported cooperative work (CSCW), human-computer interactions (HCI), and systems-of-systems engineering. He has a B.S. (1983) from the University of California, Berkeley in EECS (Electrical Engineering and Computer Science), and an M.S. (1997) and Ph.D. (2003) from the University of California, Irvine in ICS (Information and Computer Science).

Gloria Mark is Professor in the Department of Informatics, University of California, Irvine since 2000. Dr. Mark received her Ph.D. in Psychology from Columbia University. Prior to UCI, she was a Research Scientist at the GMD (German National Research Center for Information Technology), in Bonn, Germany, a visiting research scientist at the Boeing Company, and a research scientist at the Electronic Data Systems Center for Advanced Research. Dr. Mark's research focuses on the design and evaluation of collaborative systems. Her current projects include studying multi-tasking of information workers, technology use in disrupted environments and worklife in the network-centric organization. In 2006, she received a Fulbright scholarship to conduct research at the Humboldt University in Berlin. Dr. Mark has published in numerous conferences and journals including the ACM CSCW, ACM CHI, ECSCW, ACM DIS, ACM Group, and IEEE RE conferences and CSCW, CACM, and ISR journals. She was program chair for the ACM CSCW'06 and ACM Group'05 conferences and is on the editorial board of Computer Supported Cooperative Work: The Journal of Collaborative Computing, and e-Service Quarterly.

Copyright © 2007, by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers for commercial use, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via e-mail from ais@gsu.edu.

ISSN: 1536-9323

Editor
Kalle Lyytinen
Case Western Reserve University, USA

<table><tr><td colspan="4">Senior Editors</td></tr><tr><td>Izak Benbasat</td><td>University of British Columbia, Canada</td><td>Robert Fichman</td><td>Boston College, USA</td></tr><tr><td>Varun Grover</td><td>Clemson University, USA</td><td>Rudy Hirschheim</td><td>Louisiana State University, USA</td></tr><tr><td>Juhani Iivari</td><td>University of Oulu, Finland</td><td>Robert Kauffman</td><td>University of Minnesota, USA</td></tr><tr><td>Frank Land</td><td>London School of Economics, UK</td><td>Jeffrey Parsons</td><td>Memorial University of Newfoundland, Canada</td></tr><tr><td>Suzanne Rivard</td><td>Ecole des Hautes Etudes Commerciales, Canada</td><td>Bernard C.Y. Tan</td><td>National University of Singapore, Singapore</td></tr><tr><td>Yair Wand</td><td>University of British Columbia, Canada</td><td></td><td></td></tr><tr><td colspan="4">Editorial Board</td></tr><tr><td>Steve Alter</td><td>University of San Francisco, USA</td><td>Michael Barrett</td><td>University of Cambridge, UK</td></tr><tr><td>Cynthia Beath</td><td>University of Texas at Austin, USA</td><td>Anandhi S. Bharadwaj</td><td>Emory University, USA</td></tr><tr><td>Francois Bodart</td><td>University of Namur, Belgium</td><td>Marie-Claude Boudreau</td><td>University of Georgia, USA</td></tr><tr><td>Susan A. Brown</td><td>University of Arizona, USA</td><td>Tung Bui</td><td>University of Hawaii, USA</td></tr><tr><td>Dave Chatterjee</td><td>University of Georgia, USA</td><td>Patrick Y.K. Chau</td><td>University of Hong Kong, China</td></tr><tr><td>Wynne Chin</td><td>University of Houston, USA</td><td>Ellen Christiaanse</td><td>University of Amsterdam, Nederland</td></tr><tr><td>Mary J. Culnan</td><td>Bentley College, USA</td><td>Jan Damsgaard</td><td>Copenhagen Business School, Denmark</td></tr><tr><td>Samer Faraj</td><td>University of Maryland, College Park, USA</td><td>Chris Forman</td><td>Carnegie Mellon University, USA</td></tr><tr><td>Guy G. Gable</td><td>Queensland University of Technology, Australia</td><td>Dennis Galletta</td><td>University of Pittsburg, USA</td></tr><tr><td>Hitotora Higashikuni</td><td>Tokyo University of Science, Japan</td><td>Kai Lung Hui</td><td>National University of Singapore, Singapore</td></tr><tr><td>Bill Kettinger</td><td>University of South Carolina, USA</td><td>Rajiv Kohli</td><td>College of William and Mary, USA</td></tr><tr><td>Chidambaram Laku</td><td>University of Oklahoma, USA</td><td>Ho Geun Lee</td><td>Yonsei University, Korea</td></tr><tr><td>Jae-Nam Lee</td><td>Korea University</td><td>Kai H. Lim</td><td>City University of Hong Kong, Hong Kong</td></tr><tr><td>Mats Lundeberg</td><td>Stockholm School of Economics, Sweden</td><td>Ann Majchrzak</td><td>University of Southern California, USA</td></tr><tr><td>Ji-Ye Mao</td><td>Remnin University, China</td><td>Anne Massey</td><td>Indiana University, USA</td></tr><tr><td>Emmanuel Monod</td><td>Dauphine University, France</td><td>Eric Monteiro</td><td>Norwegian University of Science and Technology, Norway</td></tr><tr><td>Mike Newman</td><td>University of Manchester, UK</td><td>Jonathan Palmer</td><td>College of William and Mary, USA</td></tr><tr><td>Paul Palou</td><td>University of California, Riverside, USA</td><td>Yves Pigneur</td><td>HEC, Lausanne, Switzerland</td></tr><tr><td>Dewan Rajiv</td><td>University of Rochester, USA</td><td>Sudha Ram</td><td>University of Arizona, USA</td></tr><tr><td>Balasubramaniam Ramesh</td><td>Georgia State University, USA</td><td>Timo Saarinen</td><td>Helsinki School of Economics, Finland</td></tr><tr><td>Rajiv Sabherwal</td><td>University of Missouri, St. Louis, USA</td><td>Raghu Santanam</td><td>Arizona State University, USA</td></tr><tr><td>Susan Scott</td><td>The London School of Economics and Political Science, UK</td><td>Olivia Sheng</td><td>University of Utah, USA</td></tr><tr><td>Carsten Sorensen</td><td>The London School of Economics and Political Science, UK</td><td>Ananth Srinivasan</td><td>University of Auckland, New Zealand</td></tr><tr><td>Katherine Stewart</td><td>University of Maryland, USA</td><td>Mani Subramani</td><td>University of Minnesota, USA</td></tr><tr><td>Dov Te&#x27;eni</td><td>Tel Aviv University, Israel</td><td>Viswanath Venkatesh</td><td>University of Arkansas, USA</td></tr><tr><td>Richard T. Watson</td><td>University of Georgia, USA</td><td>Bruce Weber</td><td>London Business School, UK</td></tr><tr><td>Richard Welke</td><td>Georgia State University, USA</td><td>George Westerman</td><td>Massachusetts Institute of Technology, USA</td></tr><tr><td>Youngjin Yoo</td><td>Temple University, USA</td><td>Kevin Zhu</td><td>University of California at Irvine, USA</td></tr><tr><td colspan="4">Administrator</td></tr><tr><td>Eph McLean</td><td>AIS, Executive Director</td><td colspan="2">Georgia State University, USA</td></tr><tr><td>J. Peter Tinsley</td><td>Deputy Executive Director</td><td colspan="2">Association for Information Systems, USA</td></tr><tr><td>Reagan Ramsower</td><td>Publisher</td><td colspan="2">Baylor University</td></tr></table>
