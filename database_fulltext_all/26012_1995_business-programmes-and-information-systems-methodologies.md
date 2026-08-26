---
otero_id: 26012
otero_key: "NXRVDF2S"
title: "Business programmes and information systems methodologies"
authors: "Don Kelleher"
year: "1995"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1995.tb00095.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Business programmes and information systems methodologies

Don Kelleher

31 Attleborough Road, Nuneaton, Warwickshire, CV11 4HZ, UK

Abstract. An Information Systems Methodology is usually presented as a sequential set of tasks — planning, analysis, design and construction — resulting in a new business application. This classical 'forward-engineering' approach must be adapted to changing business needs — business process redesign, quality management, process and systems templates, advanced technologies, application packages, the reuse of existing information systems resources, and rapid delivery cycles. Using the most general concept of a Business Programme, this paper describes a methodological approach incorporating these modern themes that is qualitatively and quantitatively different from the classical model. It provides a framework for the integration of otherwise independent methodologies, and shows how an entire programme can be formulated, planned and executed. An example is provided, and the approach is justified.

Keywords: application, business programme, EDI, information systems, methodology, packages, process redesign, process reengineering, release strategy, total quality management.

## INTRODUCTION

A business programme is an initiative undertaken by an enterprise in order to change significantly the way that it conducts business. They key defining attributes of a business programme are: (1) significant changes in the way that business is conducted; (2) breakthrough thinking in new business processes and systems; (3) a substantial investment in capital and resources; and (4) implementation consisting of several coordinated projects. At the most general level, a business programme may be stated as a 'problem' — there exists a current situation of the business (the A state), a desired state of the situation (the B state) can be articulated, and a solution in the form of an optimal path from A to B must be discovered, specified and implemented. Examples of business programmes with their associated A and B states are presented in Table 1.

Formal methods to formulate, plan and deliver entire business programmes are needed in order that such programmes can be properly defined and brought to a successful conclusion.

Table 1. Sample business programmes

<table><tr><td>Programme name</td><td>A state</td><td>B state</td></tr><tr><td>Rapid product deployment</td><td>It takes an average of two years to introduce a new product. Competitors introduce new products in six months</td><td>introduce new products in four months or less</td></tr><tr><td>Quick response</td><td>It takes an average of seven days from receipt of an order to delivery of the goods</td><td>It takes an average of two days to ship an order. Rush orders can be handled in under ten hours</td></tr><tr><td>Electronic connectivity</td><td>All business documents are exchanged in paper form. A high percentage are wrong, requiring manual intervention to be resolved</td><td>Business documents are exchanged electronically. The error rate is reduced and human intervention is rarely required</td></tr></table>

Because a substantial part of the investment in a business programme may be consumed by information systems and technology, it may be thought that any one of a number of traditional, accepted application (information system) development methodologies might suffice. A central thesis of this paper is that such methodologies are necessary but not sufficient. There is a need for a larger and different approach than that provided by such methodologies alone, even though they will be incorporated in this larger approach in an important and visible way. This new approach, the business programme methodology (BPM), is described in this paper.

The essential justification for this new approach is that methods for business and systems analysis based on concepts developed in the 1970s and 1980s are no longer sufficient to meet the business needs of the 1990s. A number of distinct agents of change are at work: the reinvention of business processes to compete in a world of global competition; the influence of the quality movement; the adoption of concepts of asset management in information resource management; increasing trends towards outsourcing and package acquisition; the automation of the systems development processes through Computer Aided Software Engineering (CASE) technology; and finally, the explosion in the forms and varieties of technologies to support business process automation.

The paper will develop the above argument as follows. A general methodology model will be presented. The currently available classes of methodologies will be described. BPM will be presented and discussed. The distinguishing characteristics of BPM will be described in sufficient detail so that the practitioners of conventional methodologies may readily see the points of comparison and contrast with BPM. A case study — 'Quick Response' — will be discussed. A selection of techniques used within BPM will be discussed throughout the text. BPM will then be placed in a larger context of programme selection and programme coordination methods. The text of the paper concludes with a summary of the key points. References are provided for all the major concepts. The paper assumes a general familiarity on the part of the reader with current information systems methodologies as applied to business and an appreciation of the current trends affecting these. No references to a business programme methodology as such are provided. The author is unaware of the existence of any. The work produced here is a summary of the author's experiences in applying these concepts. Other forms of the concepts — those not specifically based on the theme of a business programme — have been and are continuing to be developed as a natural evolution of current information systems methodologies. These will be described briefly at the end of the paper and suitable references provided.

## GENERAL FORMS AND CHARACTERISTICS OF A METHODOLOGY

A methodology is a formal, structured, general-purpose approach to the solution of a particular type of problem. For example, a doctor faced with the requirement to diagnose and treat a medical complaint applies a methodology along the following lines: analyse the complaint, study the patient's medical history, examine the patient, select appropriate tests, evaluate the test results, generate alternative hypotheses, make the diagnosis and select an appropriate treatment. Professional people generally, doctors, engineers and sales executives, for example, all apply methodologies appropriate to their work.

The usual specification of a methodology, as illustrated in Figure 1 below, is that it is organized into a set of phases, e.g. the classic planning, analysis, design and construction stages of information systems development. Each phase in turn consists of a number of specific tasks designed to produce a specific work product (also called a deliverable). The tasks utilize specific techniques (and possibly specific tools) to produce the work products.

## INFORMATION SYSTEMS METHODOLOGIES

A large number of general and proprietary information systems methodologies exists. Some of these are listed in the references. They can be usefully divided into the following classes: the forward engineering class, the package evaluation class, the systems re-engineering class and the systems maintenance class.

Figure 1. A simplified methodology model  
![](/api/attachments/NXRVDF2S/fulltext/images/40e399422a8f951fb6b61ba06de75a37553b0801f65b17117f34ef8ccd1346bf.jpg)

Table 2. The classic structure of an information systems development methodology

<table><tr><td>Phase</td><td>Work product</td></tr><tr><td>Planning</td><td>Business requirements definition; the scope; general solution description; preliminary cost/benefit analysis; project plan</td></tr><tr><td>Analysis</td><td>Process model, data model, event model, business rules, current systems analysis</td></tr><tr><td>Design</td><td>General system structure; user interface design (screens and reports); data flows; program structure; program logic specification; database design; performance criteria</td></tr><tr><td>Construction</td><td>Program source and load modules; databases; libraries; testing procedures; conversion and interface routines</td></tr><tr><td>Transition</td><td>Production system; production database; training material; documentation; converted files</td></tr></table>

## The forward engineering class of methodologies

The typical phase structure and a small selection of key work products of each phase of such a methodology are listed in Table 2.

## The package selection methodologies

These methodologies focus on the evaluation, acquisition, installation and modification of commercially available packages that may satisfy the business requirements. The process focuses on comparing the analysis and design features of a desire system with those of candidate solutions that have already been constructed.

## The systems re-engineering methodologies

These methodologies focus on existing in-house applications and re-engineer them to conform to a more modern specification than that used for the original construction. The re-engineering may include such features as (1) the addition of new or modified business functionality; (2) an upgrade to the underlying application and technical architectures (e.g. from an on-line transaction processing system on a mainframe to a knowledge engineering application on a client/server platform); (3) the use of a modern programming language with restructured code.

## The systems maintenance methodologies

These methodologies evaluate requests for enhancements to existing production applications. The evaluation determines the impact of the request — what code, screens and data structures need to be modified and what additional functionality needs to be constructed. Enhancement requests are cost-estimated, prioritized, selected and approved by a management approval process and scheduled for implementation. Implementation involves coding and testing followed by production installation.

## SOME GENERAL CHARACTERISTICS OF INFORMATION SYSTEMS METHODOLOGIES

## Variations

Many variations of the above classes of methodologies exist. These variations are distinguishing features of the methodologies. They may occur by phase, by procedure, by technique or by work product. Variations by technique are evident in the selection of representation schemes, i.e. entity-relationship diagrams, object-oriented class hierarchy diagrams, for example. They are also evident in the selection of techniques to represent technical architectures, client/server architecture being a classic example.

## Development paths

A development path involves the selection of specific phases, tasks, techniques and deliverables as appropriate to a given situation or type of situation. A project manager may determine, for example, that a task 'Assess\_Current\_Situation' is irrelevant in her project, or that the only deliverables that will be produced are those that can be developed and maintained using a particular set of development tools. Development paths essentially involve the customization and scaling of a generic methodology to distinct subclasses of problems within the general class for which the methodology was designed. The selection of the exact development path for a given project is a key project management decision. Development path selection results from the fact that methodologies cannot be 'followed' in a prescriptive way, but rather they must be applied in a selective and intelligent way.

## Phase sequencing and dependency

Referring to Table 2 above, we may introduce the question of phase sequencing and dependency. Sequencing means that there is an implied order in the execution of the phases — planning precedes analysis, which precedes design and so on. Dependency means that the output of one phase is a mandatory input to a subsequent phase — planning identifies those business objects that are to become the subject of analysis and the design phase produces a design to implement the processes defined in the analysis phase. There is some current discussion in the computer press concerning phase sequencing and dependency in methodologies. Two distinctly different approaches are described, the 'waterfall approach' and 'iterative development'. The waterfall approach illustrated in Figure 2 involves a situation of total dependency between phases, i.e. all the deliverables of a phase are exhaustively completed before any tasks of a subsequent phase may commence.

Figure 2. Total phase dependency — the 'waterfall' approach  
![](/api/attachments/NXRVDF2S/fulltext/images/f450743fa284d435a1bea62e1c7d6a30ad8606a0ab17ce44cf059a8ff1bc0d23.jpg)

![](/api/attachments/NXRVDF2S/fulltext/images/3101e3e3d61f006dce0ae453a2d4618673dfe9c51b99354993f664a368f69170.jpg)  
Figure 3. Spiral development à la Boehm

The iterative approach (sometime also referred to as the 'Boehm spiral') is illustrated in Figure 3. The approach is characterized by completing a small amount of analysis, following this with a corresponding design, demonstrating this to a user, correcting analysis and design concepts and errors, adding a new piece of analysis and design, and showing this to the user. The whole approach continues in this iterative manner until a complete system is designed and constructed at least to the level of a detailed working prototype.

## OTHER METHODS

The application of formal methodologies to business problems is not limited solely to information systems activities. Two other disciplines at least, total quality management and business re-engineering, involve the formal and rigorous application of methods to the analysis and design of business processes. Frequently, the application of these methods is a precursor to the application of an information systems methodology.

## Total quality management

This is a management practice that pervades an organization from the board room to the shop floor. It is based on a fundamental understanding of the customer's satisfaction criteria relative to the products and services that are sold. The business processes that deliver these products are identified and analysed. Product defects are identified and measured using a variety of statistical techniques. Product defects are traced to defects in the processes that produce the products. These process defects are corrected and improved products — those that better satisfy the customer's satisfaction criteria — are produced. The process-measurement and defect-correction activities continue, leading to a state of 'continuous process improvement' that characterizes the 'quality' approach to management.

## Business re-engineering

Business re-engineering is a 1990s phenomenon. It is based largely on the work of Michael Hammer (1990) as expounded in his now famous paper. The fundamental theory of business re-engineering is that, while continuous process improvement is an admirable goal, there are circumstances in which more drastic measures than mere improvement upon an existing process are required in order to ensure the prosperity if not the survival of the enterprise. These drastic measures involved: (a) the setting of 'outrageous goals' and (b) a radical reinvention of a particular aspect of the enterprise's processes in order to achieve these goals. The popularity of business re-engineering with executives has led to the development of a number of business re-engineering methodologies which are now sold and practised commercially.

## SELECTING AN APPROPRIATE METHODOLOGY

The implicit assumption in selecting a methodology from any of the above classes is that a class of problem has already been identified for which the methodology is an appropriate tool to develop a solution. In choosing a forward engineering methodology it has already been determined that a new information system will be developed, and in choosing the re-engineering methodology it has already been decided that an existing system will be re-engineered to support the requirements. In choosing a business re-engineering methodology over a forward engineering information systems development methodology, the major selection criterion is the requirement to reinvent a business, as opposed to delivering an information systems to support a known business. Though a common set of techniques, especially those relating to the design, representation and implementation of a business process, is used by the quality, the business re-engineering and information systems methodologies, it is generally true that they are seen as separate and distinct methodologies that are applied by different groups of corporate personnel for different purposes.

This separation of the methodologies has a number of distinct disadvantages: (1) business problems are so diverse and flexible that it cannot be assumed that any given problem can be made to fit the general mould of any one of the methodologies described up to this point; (2) the understanding of a business problem and the constraints placed upon the solution may require a delay or a change in the selection of a particular methodology path; and (3) the results of the application of one methodology, for example, business re-engineering, are required inputs to the application of another methodology — an information systems development methodology, for example. In order to overcome these disadvantages and apply all of the methodologies in a holistic and synergistic way, there is a need for a context and a framework for the application and integration of these various methodologies. A context is provided by the concept of a business programme and a framework is provided by the business programme methodology.

## OVERVIEW OF THE BUSINESS PROGRAMME METHODOLOGY

A very general overview of the major phases, sub-phases and a selection of key deliverables of BPM are listed in Table 3.

Table 3. General structure of BPM

<table><tr><td>Phase</td><td>Sub-phase/task</td><td>Work product</td></tr><tr><td>Programme formulation</td><td></td><td>Business problem to be solvedProcesses in scopeCurrent systems/packages for evaluationResource allocationDefinition and schedule of subsequent stages</td></tr><tr><td rowspan="2">Requirements analysis</td><td>Business requirements analysis</td><td>New/re-engineered business processesProcess design specificationsOrganization design</td></tr><tr><td>Systems requirements analysis</td><td>Architecture selectionsApplication general designTechnology selections</td></tr><tr><td rowspan="2">Implementation planning</td><td>Component selection and reuse</td><td>Specification of all components to be used with corresponding change, make or buy recommendations</td></tr><tr><td>Release strategy planning</td><td>Phased delivery strategy</td></tr><tr><td>Release delivery</td><td>Multiple parallel applications of:(1) forward engineering(2) systems reengineering(3) maintenance and(4) package acquisition methodologies</td><td>Implemented functional release consisting of programs, modules, databases, documentation, etc.</td></tr></table>

## PROGRAMME FORMULATION

This stage formulates the programme by defining the fundamental business problem to be solved. It formulates the problem, states the mission of the programme, determines the resources required for subsequent phases, and develops the plans for these phases. The major technique used here is the 'problem-solving process': — describing a current state of the business situation (A state), finding and articulating a desired state (B state), evaluating paths from A to B and selecting the optimal path. The dual approach to understanding the A state and inventing the B state is followed throughout the entire application of the methodology.

## REQUIREMENTS ANALYSIS

Requirements Analysis has two principal components. The first — Business Requirements Analysis — relates to the understanding of the basic process, data and business rules required to deliver the desired state. The second — Systems Requirements Analysis — relates to the requirements for an information systems model for these. These are now described further.

## Business requirements analysis

## Current state analysis

Business process analysis. The current business processes, those that belong to the A state, are analysed. The work products are analysed, defects are identified and explored. The processes are compared with the general B state requirements as they are developed to determine whether the current business process is sufficient to meet the needs, whether the process needs to be re-engineered or a new process needs inventing. Analysis of the current process includes analysis of the procedures used to implement the process as well as the workflows involved.

Current information systems analysis. An inventory is made of all business information systems (applications) in the scope of the programme, whether currently in use or planned to be used. Systems that are determined to have an impact on the programme are selected for detailed analysis. This analysis will be a key input to determining the role that the system will play in implementing the programme. The information collected here is useful to the construction of the model of the solution. It is also used to coordinate solution delivery activities at a detailed level. The first level of analysis of current systems is for their business content, to understand and capture the process, data and rules that they contain.

Vendor package analysis. This task analyses the marketplace to identify those vendors and products which may have potential to be used in the delivered solution. If a suitable product is found it may be subject to further analysis to determine: (1) if it is a source of the definition of the new business process and rules and (2) if it is a suitable implementation of the new process and rules.

## Desired state specification

Business process design. This task identifies and describes the business processes that are required to implement the desired state. These processes may be existing ones that require no change, re-engineered processes or newly invented processes.

Organization design. This task maps the individual business processes to a set of job descriptions and an organization hierarchy. It defines who in the organization is responsible for the execution of the processes (unless they are fully automatic). Responsibility for monitoring, controlling and planning the processes is specified, in particular, 'process ownership' is assigned to job types and organizations.

Process specification. This task specifies the business processes using formal representation mechanisms. These mechanisms include an activity hierarchy diagram, a process logic diagram, business rules, events, process dependencies, etc. Business processes generate and use business data, and business data are shared across many processes. The specification of a process therefore involves reference to a common data model. Such data model may be represented in a formal way as an entity-relationship model or as an object-association model. (It is beyond the scope of this paper to provide a definition or explanation of the preceding modelling concepts. The reader is assumed to have some familiarity with these concepts already. Details of these are provided in the references, in particular the Information Engineering Methodology by James Martin & Co.)

In conducting the above phases and tasks the business and systems analysts will apply a number of techniques that are not usually specified in information systems methodologies. These include: business process design, work-flow analysis across value streams (a value stream is a cross-functional set of processes involving the entire set of processes required to deliver a product to a customer), defect analysis techniques as applied to business processes, statistical analysis techniques to quantify and assess defects, among others. A number of sources of such techniques are listed in the references section.

## Systems Requirement Analysis

Current State Analysis. The information systems previously identified that have been analysed for business process and business rules and which have a potential to be reused in the final solution are analysed again. This time they are analysed from an architecture, design, technology and performance perspective.

Desired State Specification. Application General Design involves the specification of the major features and functions of the systems (applications) required to implement the desired state. Essentially it involves mapping the business processes and data already defined to a systems form and structure. This in turn involves the mapping of these components to a set of architectures and the selection of appropriate architectures and technologies. The architectures include such things as real-time process automation systems, knowledge-engineering systems, on-line-transaction processing systems, background transaction processing systems, client/server systems, distributed processing and so on.

Technology Selection. This task maps the general design to an available set of technologies and selects the most appropriate. Here we choose specific vendor products for the usual hardware, software and network components of information systems implementations. In addition, we may choose from a myriad of other technologies that are now available to support business process automation — bar-code scanners, voice response utilities, swipe cards, image storage and retrieval technologies, and robotics.

## IMPLEMENTATION PLANNING

## Component selection

The strategy for selecting the source of the various components of the general design includes the following elements:

Reuse. Using an existing application according to its original scope, functionality and architecture, enhancing it within that framework if required.

Re-engineer. Reconstructing an existing application with significant modifications in scope, functionality or architecture.

Acquire. Acquire, install and perhaps modify an application package or reusable component library.

Construct. Design and construct from first principles a new application using either in-house or contracted development resources.

## Release strategy planning.

This task defined the number and content of the releases that will be required to deliver the total solution as defined by the general design. Each release delivers a partial solution, brings benefit to the business, and can be cost-justified in its own right. It can be anticipated that it will take several releases to deliver the entire solution defined in the general design. Releases will be planned for maximum business priority and benefit. Any one release may be as simple as an enhancement to an existing application or as complex as the whole series of tasks listed below:

Parallel design and construction of new applications

Package acquisition, modification and installation

Current systems re-engineering

Interfaces and conversions

Current system retirement

Current datastore retirement

Data conversion and purification.

## RELEASE DELIVERY

Release delivery involves the detailed specification, design, construction and transition of the partial solution defined by the release in question. As a practice matter, any one release delivery decomposes into a number of separate but related projects, each addressing a major component of the solution. This decomposition is determined by the R/R/A/C decision already made. The R/R/A/C decision may apply to multiple information systems as shown below:

Programme release n = Reuse of information system A release n +

Reuse of information system B release m +

Re-engineer of information system C release p +

Acquire vendor package D release q

Construct information system E release 1 +

Construct information system F release r

For each such system to be reused, re-engineered, acquired or constructed a complete structure of tasks required to effect the desired result needs to be specified and applied. It is beyond the scope of this paper to specify such a set of tasks and work products. Suffice it to say that each such project will be supported by either a forward-engineering methodology, a current systems maintenance methodology, a re-engineering methodology or a package acquisition methodology. For these, readers may refer to the references or apply their own methodologies and experiences. At the programme level there is a further requirement to specify testing and release coordination as a whole, as well as a requirement to conduct transition (production rollout) planning both at the programme level and at the release level.

## DISTINGUISHING FEATURES OF THE BUSINESS PROGRAMME METHODOLOGY

The business programme methodology has a number of features that distinguish it from the classes of methodologies described above, and in particular, from the forward engineering class of information systems development methodologies. These features include scope, requirements analysis, component selection and reuse, release strategy planning, methods integration and dynamic development path selection. These are discussed in the following sections.

## Scope of the programme

The scope of this programme is defined by the set of business object-types (business processes, data, organizational units and current systems) that are addressed by the programme. It is usually reasonably clear when a conventional development methodology is applied to a given situation what the general scope of the problem domain is. For example, when an organization that does not already have an order entry system initiates a project to construct such a system, the project manager may safely assume that the scope of the project is primarily based on the processes and data of order-taking and that it is based in a secondary way on related things such as products, customers and contracts. The scope of a business programme called Quick Response or Electronic Connectivity, for example, is not at all obvious at the outset. The scope needs to be determined, and the concept of scope is different from that which is ordinarily understood by a typical application development project. The fundamental differences in scope can be illustrated in Figure 4.

The conventional scope of an area of interest, an order entry system, for example, can be determined and expressed in a relatively simple way, as shown in Fig. 4. The relationship of business processes to data is shown in matrix form illustrating the actions (create, read and update) of the processes on the data. In the very simplistic case shown, the project manager may focus analysis and design activities on the three processes — Take-Order, Fill-Order and Ship-Order. In the case of a business programme called Quick Response, it is quite likely that all of the above processes and data are involved. The programme manager is therefore required to understand the degree and impact of the involvement of all the above components in order to have an accurate estimate of the size, complexity, costs and benefits of formulating and implementing the programme.

![](/api/attachments/NXRVDF2S/fulltext/images/ebe5e92dc0c8b90abca489c2c76a0c72668ed5a2d408df7f19045f04f932486c.jpg)  
Figure 4. Illustration of scope of systems vs business programmes

## Business requirements analysis

From the 1970s to the late 1980s, the requirements placed on information systems could be described in the following way. Business processes, e.g. order entry and order fulfilment, are defined in policy and procedures manuals and they are operated by the business personnel. Data results from the execution of these processes that must be recorded, stored, retrieved and processed. Information systems are constructed to implement these data management functions. Such systems automate the data management aspects of the business processes. They do not automate the processes themselves, which are still operated by humans with the aid of an information systems tool.

Today, the transaction processing and executive information systems of most organizations have mostly been built. Competitive advantage is no longer gained from the delivery of passive information systems for an established set of business processes but rather from the invention of a whole new way of doing business. This new way of doing business needs be defined by a method that is capable of inventing new business processes and by reinventing existing processes. The traditional approaches to requirements analysis typically involve a business analyst acquiring an understanding of a business area. That understanding is then represented in a complete and formal way using established representation techniques (e.g. a data model and an activity model) such that it can be interpreted by others and used as a basis for the design of a conventional information system. Such a view of requirements analysis is no longer sufficient. What is needed now is not just to understand the situation as it exists but to radically improve upon what is found. This requires new methods for problem solving generally and for business process redesign particularly. This requires vastly enhanced methods and tools and a new kind of system — a process automation system. The analytic techniques available in current application development methodologies do not generally satisfy this requirement.

A conventional methodology might specify the requirements of an information systems: (1) they can be captured in plain English by interviewing the users of the business process in the scope of the system and (2) they can be represented in a logical design consisting of business process, data, and rules in a formal representation language. The Business Programme Methodology would prescribe that the invention of new ways of doing business are satisfied by a 'Business Process Design' process — a facility to invent a business process that did not already exist, to radically re-engineer an existing process and to discard obsolete or dysfunctional processes.

## Component selection and reuse

Organizations now have an enormous investment in the systems that run their business. This investment must be managed in such a way that it is protected and so that it is reused to support the new ways of doing business. It must not and need not be seen as an obstacle to doing business in a new way. Organizations also have a larger choice in the selection of sources of information systems than before. These choices consist of in-house development, contracted development, purchased package applications and reusable libraries. These choices result in the need to formulate an implementation strategy for business programmes that require systems support. The decision to reuse, re-engineer, acquire or construct an application or application components (abbreviated to the R/R/A/C decision) is one of the key decisions to be made by a programme manager, therefore a well-defined management method and a clearly delineated point for making that decision are needed. When the decision has been made, it permits the description of individual projects within the programme and then the relevant methodologies of forward engineering, package installation and redevelopment may be applied as appropriate on these projects individually. A further implication of the above is that the forward engineering class of methodologies in its current form is becoming increasingly inadequate to meet the current needs of business.

## Release strategy planning

The architecture and general design (inclusive of all of the process, data and rule models and the organizational models) represent the ultimate, complete implementation of the programme. As with all investment decisions, the question of the timing and the amount of the return on the investment must be addressed. It is, unfortunately, in the nature of large and complex business programmes that it may take several years to implement them. This entails high cost, high risk and a delayed return on investment. The benefits can be accelerated and the risks reduced by the selection of a release strategy. More than that, a good release strategy is good project management strategy. An accelerated delivery schedule keeps the sponsors interested and increases confidence that the programme can deliver the solution. Early successes are more likely to result in continued funding than are prolonged projects with no end in sight for a long time.

Release strategy planning is half-way between the waterfall approach and the iterative approach described in phase sequence and dependency above. It is based on the premise that a vision of the solution as a whole should be specified and evidently feasible before investing in any part of the solution, and that a solid, comprehensive set of requirements are not only desirable but necessary for useful design and construction to commence. It represents an 'incremental' mode of delivery.

## Methodology integration

It will now be evident that the business programme methodology is a generic framework that encompasses a number of diverse and otherwise unrelated methodologies. The application of any one of these methodologies occurs at a project level within the overall programme, i.e. the fundamental project management concept is that of a programme consisting of a number of constituent projects. This integration occurs in the context of a 'super' phase structure as shown: programme formulation, requirements analysis, implementation planning, release delivery.

## Dynamic development path selection

Any methodology that resulted from the simple union of the techniques and work products of all the various methodologies described above would prove to be very large and unwieldy. There is a requirement to select a path through the entire methodology that is appropriate to the problem at hand and to choose a set of techniques for each work product to be produced. Experience with business programmes generally shows that such decisions cannot be made once and for all at the outset of the programme in a phase known as the 'planning' phase. This situation is dealt with as follows: planning is a continuous process that applies throughout all phases. Planning in the programme formulation phase will determine whether and to what degree current systems analysis, vendor package analysis and work-flow analysis will be conducted in the requirements analysis phase. When conducting requirements analysis one technique may be determined to be more appropriate than another, e.g. an object-oriented approach versus a more conventional process/data representation mechanism. Thus the techniques and work products of requirements analysis are selected dynamically as required by the programme rather than being set in a prescriptive way by a fixed methodology. Generally speaking though, implementation planning including general design and release strategy planning must be completed before a complete delivery schedule can be estimated or a complete cost/benefit analysis can be written.

## The role of the information technology professional in the organization

Another consequence of all of this is that the role of the information systems professional is changing. Whereas a systems analyst would ordinarily be expected to interpret the requirements of a business user in support of a systems design project, in the new paradigm systems analysts are becoming business process engineers, i.e. they are expected to show the way in the invention of new business processes. Project leaders would ordinarily be expected to manage a group of systems analysts, designers and programmers in the design and construction of a new information system. In the new paradigm they are expected to function as business programme managers with a vastly increased scope of responsibility, for managing business professionals as well as information technology in the formulation of a programme and in the specification of a solution. They are now key players in major business investment decisions, and they are responsible for managing not one but multiple coordinated projects within a programme.

## CASE STUDY

Three examples of business programmes have already been cited: Rapid Product Deployment, Quick Response and Electronic Connectivity. The third programme, Electronic Connectivity, is frequently seen as an enabler and critical success factor of the other two and is usually managed as a separate but related programme in its own right. The paper now discusses the Quick Response programme as an illustration of the concepts under discussion.

Quick Response is usually encountered in the wholesale and retail trades. Retailers of consumer products acquire products from wholesalers and stock them in their warehouses and on the shelves in their retail outlets. Orders for products placed with wholesalers are usually bulk orders and are placed well in advance of sale, often up to several months. Orders by the retailers are frequently placed by a central buying location for a number of retail outlets and the stock is stored in a central location. Orders are placed by a retail buyer in manual conversation with a wholesale sales representative who writes up the order on an order form and submits it to the order entry department by mail, by voice or by facsimile. This order is then captured by entering it into the Order Entry information system. This situation is illustrated in Figure 5.

Figure 5. Wholesale/retail process before Quick Response  
![](/api/attachments/NXRVDF2S/fulltext/images/262555f6e16ce0f9986204df4cede30f489ce4951ef5ca479dc83e8309c41e17.jpg)  
© 1995 Blackwell Science Ltd, Information Systems Journal 5, 137–157

This situation is distinctly disadvantageous to the retailer. Capital may be tied up in stock in central inventory. Costs are incurred in the distribution from central stores to retail outlets. Stock may be returned or wasted unless sold quickly and in quantity. Unsold stock consumes valuable shelf-space. Discounted pricing may result in reduced profits or even in a loss. When the product has been distributed to the outlets, demand for the product may be less than expected for any one of a number of reasons, including changing consumer tastes, pricing or competitive products.

A distinctly new and different way of conducting business can be found. It consists of reducing or eliminating the retailer central warehouse and by stocking the retail outlets directly from the wholesaler's distribution centre. Because of the smallness of the stock-warehousing facilities at the retail outlets, stock must be replenished frequently, perhaps on a daily basis, directly from the wholesaler's warehouse. Because the frequency and the sizes of orders are based entirely on the immediate consumer demand for the products, orders are placed on a 'just-in-time' basis and not necessarily far in advance of sale. A particularly strong, peak demand at one or more locations may result in an emergency order to replenish stock.

All of this places a demand on the wholesaler to be able to respond to orders from a large number of locations in a very short period of time, in days and sometimes in hours. This situation cannot be satisfied by human operators passing paper messages during normal office hours. The solution to this problem involves reinventing the concepts and procedures of order-taking and of changing the responsibilities of the personnel involved.

Order-taking can be reinvented by allowing the retail outlets to place their own orders directly with the wholesaler. The retailer central purchasing office and the account management function of the wholesaler will have agreed in advance general policies and terms that govern the order transactions, e.g. required volume targets, price bands, allowable product substitutions and allowable delivery schedules. Any order that fits within these general parameters is accepted and processed. An electronic data interchange (EDI) network is established between the retail outlets and the wholesaler. Orders are transmitted electronically, eliminating the need for paper messages. All of this has a dramatic impact on the processes, procedures, systems and personnel of the wholesaler.

The process 'Take\_Order' ordinarily executed by the wholesaler's sales staff is now redundant and is eliminated as an active business process. The sales staff no longer take orders. Their role has changed. They are now responsible for negotiating general order-taking terms (as opposed to the content of a specific order) and for monitoring performance. They no longer act as individuals with their own exclusive territories, accounts and quotas. They are members of account management teams who are rewarded on the basis of their relative contribution to results. This new way of working is formalized in new business processes — Negotiate\_Order\_Terms and Monitor\_Account\_Revenue\_Performance. Because the procedure of order-taking has changed from a manual, paper-based method to an electronic one, new processes are required to implement that way of doing business. These processes include: Evaluate\_Account\_EDI\_Facilities, Accept\_Account\_onto\_EDI Network, Develop\_Account\_EDI\_Profile and Interpret\_Electronic\_Document among others. All of these processes must be invented, defined and implemented. The process Interpret\_Electronic\_Document, in particular, will be fully automated using sophisticated data-processing techniques, e.g. knowledge-engineering technology.

The impact on information systems is also dramatic. New systems — including those required to manage EDI transmissions and the translations — are required. Most of the required functionality may be acquired from external sources. New information systems facilities must be constructed to support the newly invented processes Negotiate\_Order\_Terms and Monitor\_Account\_Revenue\_Performance. It may be necessary to construct new systems functionality to support the process Interpret\_Electronic\_Document because of the unique and proprietary data and interpretation rules involved. An order-entry system will already be in use. It will have been designed as a traditional on-line transaction processing system operated by data entry clerks. It must now be re-engineered to do the following things: receive and transmit orders over an EDI network, produce messages that are meaningful to the systems and personnel of retail outlets, operate in a real-time, continuously available mode. The downstream logistics systems for managing stock and for scheduling and making deliveries are similarly affected, though the impact is not described here.

So far our discussion of electronic documents has been limited to purchase orders. Electronic orders are necessary but not sufficient for Quick Response (Fig. 6). Other documents needed include: purchase order acknowledgement, stock level, and invoice. The formulation and planning of the programme must take account of these too.

A complete discussion of the architecture and general design required is beyond the scope of this paper. Suffice it to say that the architecture involves real-time, intelligent, automatic, integrated systems operating on continuously available platforms deploying client/server concepts and connected via a network supporting large-volume EDI transmissions.

Because it is now evident that the scope of the Quick Response is very large indeed, it may be subdivided. Electronic Connectivity may be identified as a distinct but related programme within the Quick Response umbrella. Release strategy planning within the electronic connectivity programme may choose to implement electronic formulation, transmission and interpretation of inbound purchase orders first, invoices second and so on.

Figure 6. Wholesale/retail processes with Quick Response  
![](/api/attachments/NXRVDF2S/fulltext/images/8dcba78d49422c60ec20ff80a30fbfac3f64720f23378c461da16fe3d5eda8c2.jpg)  
© 1995 Blackwell Science Ltd, Information Systems Journal 5, 137–157

## BPM IN A LARGER CONTEXT

The methodology presented so far has dealt with the formulation and implementation of a business programme. Useful as that is, there are two other major issues to be addressed — business programme selection and business programme coordination. Business programme selection deals with the generation, evaluation and prioritization of all those programmes that the enterprise might invest in. These candidate programmes and their selection result from the application of strategic business planning methods. Business programme coordination coordinates the activities of multiple parallel and overlapping programmes. It is beyond the scope of this paper to specify these further.

## IMPLEMENTING BPM IN PRACTICE

Implementing BPM in practice requires a number of things. First, of course, there must be a business programme along with the sponsorship, the funds and the personnel to define and implement it. Second, in a technical sense, the programme manager needs access to the definition of a variety of different methodological approaches. These may be acquired from a variety of different sources and assembled in 'do it yourself' fashion. Many of the large accountancy firms and systems delivery houses offer a variety of different products from which to choose. The products that the author has used are the Information Engineering Methodology and Enterprise Engineering, both from James Martin & Co. Since the inception of this paper Enterprise Engineering has emerged as an 'umbrella' methodology for a variety of methodological approaches. The reader should be aware that the total number of techniques that may be used is in the hundreds, and that many of them must be learned and practised for the first time when a business programme is initiated. In the author's experience the techniques that present the most difficulty to the novice practitioner include: programme formulation, business process design, statistical analysis techniques, architecture selection, release strategy planning and release coordination.

## SUMMARY

Most of our project leaders have learned their skills in a world where application development, designing and building an order-entry system, for example, was the major job requirement. They would have learned and applied a forward engineering application development methodology. Today, however, most organizations have already built or acquired their core business applications. Requirements for new application functionality are related to major business programmes and these programmes generally have the following characteristics: they must design and implement radically new business processes and procedures; they must deliver the highest possible degree of error-free process automation; and, since speed is the essence of competitive advantage, they must be delivered quickly. Business programmes are rarely, if ever, nicely aligned along recognizable existing application boundaries, but may be dispersed through a variety of processes, procedures and systems.

The approach outlined in this paper shows how business programmes may be supported in a methodological way. The programme formulation phase formulates the nature and scope of the problem to be solved. Requirements analysis specifies the details of the solution in a newly invented or redesigned set of business processes. General design and implementation planning selects the best architectures and technologies to automate the business processes, minimize the time to delivery and reuses the investment in current systems assets. Release strategy planning partitions the solution into deliverable partial solutions and consequently further shortens the time to delivery, accelerates the return on investment, and reduces the risk of failure. Release delivery applies the best of construction techniques — concepts of rapid application development, automated tools for development and re-engineering and of integrating the new and re-engineered components with existing and purchased systems components.

Altogether, this constitutes a requirement for, and an approach to, systems delivery that is qualitatively and quantitatively different from classical application development life-cycles. This requirement is being addressed in a number of ways: by a vastly expanded array of methodologies, by changing the role of the information technology professional in the organization, and by automated tools to deliver and apply the various methodologies. Some established concepts are being displaced, the classical, waterfall information systems development methodologies among them. Some technologies are being reconsidered. A highly formalized forward-engineering systems development methodology automated by CASE (Computer Aided Software Engineering) tools will transform the systems development process and reduce the backlog. Such tools are a vital force now and in the future, though the application of any one of them lies in a small domain of the entire set of concepts described here. The most promising approach now being explored and prepared for commercial delivery is that of a methodological expert system operating on a knowledge base of techniques invoking, controlling and integrating a set of development tools. Such tools create, maintain and reuse the work products of all the techniques used in formulating and delivering business programmes. The benefits of such tools will vastly extend the ability of business to apply the concepts outlined in this paper. They will also, it is to be hoped, prevent a return to the days when the planning, analysis and design of systems was an arcane art practised by a handful of experts.

## REFERENCES

Berenson, M.L. & Levine, D.M. (1992) Basic Business Statistics. Prentice-Hall, Englewood Cliffs, NJ.

Berson, A. (1992) Client/Server Architecture. Series on Computer Communications. McGraw-Hill, New York.

Hammer, M. (1990) Re-engineering work — don't automate, obliterate. Harvard Business Review, 68, 104–113.

Harrington, H.J. (1991) Business Process Improvement. McGraw-Hill, New York.

Krick, E.V. (1962) Methods Engineering. John Wiley, New York.

Martin, J. & Odell, J. (1993) Principles of Object-Oriented Analysis and Design. Prentice-Hall, Englewood Cliffs, NJ.

Masaki, K. (1991) The Key to Japan's Competitive Advantage. McGraw-Hill, New York.

Norris, M. & Rigby, P. (1992) Software Engineering Explained. John Wiley, New York.

Ryan, T.P. (1989) Statistical Methods for Quality Improvement. John Wiley, New York.

Spurr, K. & Layzell, P. (1992) CASE: Current Practice, Future Prospects. John Wiley, New York.

Yourdan, E. & Coad, P. (1990) Object-Oriented Analysis. Prentice-Hall, Englewood Cliffs, NJ.

## Proprietary methodologies

Information Engineering Methodology™; Enterprise Engineering Methodology™; Systems Redevelopment Methodology™ from James Martin & Co., 2100 Reston Parkway, Reston, VA 2209, USA or 11 Windsor Street, Chertsey, Surrey, KT16 4AY, UK.

Systems Refurbishment Methodology™ from Computer Horizons Corp., 49 Old Bloomfield Avenue, Mountain Lakes, NJ 07046-1495, USA.

## Biography

Don Kelleher is a consultant who specializes in business programme methodologies and solutions delivery. He holds a BA (Hons.) degree and an MA degree in mathematical physics, as well as an MSc in computer science.
