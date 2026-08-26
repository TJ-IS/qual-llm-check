---
otero_id: 23488
otero_key: "6XQYSC47"
title: "Issues in the design and administration of distributed model management systems"
authors: "Ritu Agarwal; Deb Ghosh"
year: "1992"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1992.13"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Issues in the design and administration of distributed model management systems

RITU AGARWAL

Department of MIS and Decision Sciences, University of Dayton, Dayton, Ohio, USA

DEB GHOSH

Quantitative Business Analysis Department, Louisiana State University, Baton Rouge, Louisiana, USA

Distributed model management systems (DMMS) represent the next frontier in the organizational usage of DSS technology. Due to the growing popularity of distributed computing systems and increased level of modelling activity in most organizations, significant benefits can be realized through the implementation of a DMMS. In several ways, the functions of a DMMS can be viewed as isomorphic to those of a distributed database system.

This paper describes the objectives of a distributed model management system and discusses several important issues that must be considered before constructing the distributed model base. In addition, a layered schema architecture is suggested for designing the DMMS. The proposed architecture facilitates sharing, control, consistency and integration of models, without altering the current model representation schemes. This paper also examines the roles of different individuals responsible for managing the DMMS.

## Introduction

Model management has been a central concern reflected in much of the current decision support systems (DSS) research. Dolk and Konsynski (1984) posit that the DSS philosophy treats models in a manner equivalent to the database philosophy of data management, i.e. the treatment of models as a valuable organizational resource that needs a coherent policy for administration. A model base is conceptualized as a repository of stable, shareable organizational relationships that reflect the individual decision makers' assertions and assumptions about these relationships (Konsynski and Sprague, 1986). Interest in model management has been viewed as a manifestation of the movement away from the data-centred approach, characterized by database management techniques, to a more process-centred view, where models, rather than data, are treated as the stable entities in an organization. The need to maintain consistency, integrity, non-redundancy, and flexibility, and the need to enhance availability of models, has led to the evolution of software popularly known as model base management systems (MBMS). In certain ways, the function of the MBMS can be viewed as isomorphic to those of a database management system (DBMS).

The philosophy underlying the research streams in MBMS is one of abstracting out the procedural and technical aspects of the implementation of models and making these components invisible to the user (Dolk and Konsynski, 1984). A model base is a collection of integrated and shared computer-based models, and the advantages of this integration and sharing include (i) reduction of redundancy, (ii) increase in consistency and flexibility, and (iii) improved control over the decision making process. MBMS is the software that is responsible for both managing the model base and the user interface, i.e. user access to models is gained through the MBMS. The specifications that must be fulfilled by this software include the classical functions of a DBMS, namely, construction of new models, access to and retrieval of existing models, execution of models, and maintenance.

Nolan (1979), in his influential work on the growth and adoption of information technology in organizations, postulated a six-stage model that reflects the way in which information technology permeates organizations. The proliferation of interest in and usage of DSS and models has characterized the 'contagion' stage of the permeation. Thus, logical progression necessitates that the next step be a 'control' phase where an organization develops global policies and procedures to focus the technology into productive channels. The dangers of uncontrolled proliferation are amply evidenced in the problems associated with the development of end-user computing (Alavi and Weiss, 1985), and organizations are sensitive to the need for supervised growth. The evolution of MBMS and the increasing interest in them from a research perspective is symptomatic of that trend. Recently the importance of DSS in an organization has been reiterated in the context of the DSS function (Philippakis and Green, 1988), where the authors define an architecture that can help plan and manage the organization-wide development of DSS.

Contemporary organizations are tending towards an increasing delegation of decision making responsibility and functional specialization, manifest in the form of decentralized organization structures (King, 1983). These factors, coupled with growing geographic dispersion, has led to the emergence of distributed computing systems (DCS), which realize the benefits of cost-reduction, reliability, responsiveness, and extensibility (Katzan, 1979). DCS attempt to disperse the data processing function in order to adhere more closely to organizational structure. The evolution of DCS was followed almost immediately by the concept of a distributed database, with the objective of exploiting the communications facilities provided by the DCS to enhance availability of and control over the data resource. The literature on MBMS has largely assumed that models are being utilized in a centralized computing environment, and as such, the issues and problems related to model base architecture addressed by research are restricted in their generalizability to different computing environments.

We are interested in the architecture of model bases in a distributed computing environment. The constraints imposed by the fact that an organization is geographically dispersed raises a set of problems that have yet to be addressed at length by the model management community. The need for managing models created by multiple users has been recognized recently by Liang (1988) in the form of an architecture for group model management systems. However, the issue of how to manage the distribution of and control over these multiple user models is not addressed. Distributed model bases will become evident in the not too distant future, and while we have adequate experience in the management of distributed databases, not all of those experiences are transferable to the model management scenario.

There are several compelling productivity, economic and control related justifications for a distributed model base. First, decision processes in a distributed computing environment are characterized by a local need for information to support decision making. This necessarily leads to construction of models at individual sites, and a distributed model base would widen the availability of these models to other sites who may need to access them. Second, the construction of a distributed model base itself can realize significant cost reductions as models are allocated coherently to computing sites, with the costs of storage and communication factored in. Finally, redundancy can be decreased and control over models increased by employing a rational distribution strategy.

This paper examines issues viewed as central to the development of distributed model bases: the first issue relates to the design and management of a distributed model management system (DMMS). Here we present an architecture for schema design and specify the functions to be performed by individuals responsible for the construction and management of the distributed model base. In addition, some factors that must be recognized while distributing models and tools within an organization are discussed.

In the second section of this paper, we elucidate the objectives of distributed model management system, and highlight certain economic and non-economic issues that must be considered before designing a distributed model base. These objectives are used subsequently in the third section to specify an architecture for logical schema design. The fourth section describes the model administration function and the individuals responsible for implementing it. The final section concludes this paper and presents some directions in which we feel further research would be pertinent.

## Objectives of distributed model management

Increasing technological sophistication among end-users and the wide-spread availability of microcomputers are the two phenomena primarily responsible for the growth witnessed in modelling activity. This fact, juxtaposed with the reality that more and more organizations are decentralizing their decision making functions and computing environments, highlights the need for an approach to distributed model management. The isomorphism between model management and data management has already been identified for the centralized case (Dolk and Konsynski, 1984), and we extend that isomorphism to a distributed computing environment.

An important first step in any system specification is to identify the functionality that the system will be expected to deliver. The pervasiveness of end-user application development and modelling is an outcome of several cogent arguments in favour of the decentralization of computing activities. These include the need to satisfy special computing needs of user departments, the need to maintain organizational integrity in operations that are dependent on computing, the need to allow organizational units sufficient autonomy in the conduct of their tasks to optimize creativity and performance at the unit level, etc. (King, 1983). Many of the objectives of distributed model management can be extracted from these arguments and the objectives of distributed data management.

The objectives of distributed model management can be

categorized into two classes:

(i) Model base objectives, which specify the requirements to be fulfilled by the design and architecture of the model base. These include availability, consistency, resource sharing, non-redundancy, logical/physical independence, and standardization.

(ii) Communication objectives, which place constraints on system design in that a certain level of service must be provided to network users. Increased reliability of the distributed system, and reduction of long distance communication delays are considered to be the major communication objectives.

The availability and resource sharing objectives are closely linked and attempt to increase the productivity and cost-effectiveness of organizational model usage. In a distributed computing environment, it is desirable to take advantage of the communications network to enable users at remote sites to use resources located at other sites. These resources may be in the form of modelling tools and software, or specific models that users have developed. Resource sharing is possible only when there exists an organizational inventory of tools and models.

Non-redundancy implies that the objects maintained in the system are stored only at one location. This objective helps promote model integrity in that changes and updates to models are reflected immediately in all instances (copies) of the model. The implementation of non-redundancy is also instrumental in addressing the problem of multiple versions of the same model developed independently of one another. In a distributed environment, it is more important to judiciously control the amount of redundancy, since greater availability can be achieved when multiple copies of an object are stored on the network.

The areas in which an integrated approach to distributed model management can realize the maximum pay-off are those of consistency and standardization. Models developed by users who have limited knowledge of the larger organization can contain incorrect, simplifying assumptions about organizational relationships. In such situations the work of the modelling activity is limited, since the basis upon which decisions are made may be erroneous. The identification and surfacing of ‘correct views’ of organizational relationships occurs in the process of developing an integrated model base and ensures that any users who need to use these relationships are doing so in a consistent and valid manner. Note that ‘correct’ relationships in the model context does not possess a normative connotation, but rather that correctness is a function of organizational definition.

The communications objectives primarily address efficiency considerations in the flow of information through the network topology. In distributed data management the provision of an acceptable response time is a major design objective, where the response time depends on the complexity of the query initiated, and the congestion on the paths along which the data must travel. Since models are users of data, the increase in response time for a model is the incremental time required for model solution. In this research we focus on the model base objectives. It is assumed that a communications network is already in place.

The objectives specified above provide the starting point for the design of a distributed model base. The extent to which any objective can be achieved and the relative importance accorded to each objective needs to be specified through a planning activity and through an extensive analysis of model usage in the organization. User requirements for relationships and solvers impinge upon the decision as to where they should be located. This point is elaborated upon in a later section.

## Designing distributed model bases

Conceptually, a distributed model base (DMB) is similar to a distributed data base in that it can improve organizational control over resources, while increasing the availability of these resources. However, a critical difference between the two types of systems stems from the importance of semantics in a DMB. Models typically capture a causal relationship between inputs and outputs (Blanning, 1989) and this relationship must be understood prior to utilizing a model for a given user problem. Thus, cognizance of this causality becomes an important prerequisite for a network user to access or modify an existing model in the DMB. The DMB is expected to overlay the distributed data base, and a certain level of knowledge and experience is expected of decision makers who construct and interpret models (Blanning, 1989). In this section, we discuss four sets of issues (economic, organizational, those related to the modelling activity, and technical) that must be considered before designing a DMB.

## Economic factors

Economic factors constitute tangible costs that an organization may have to incur in order to distribute the modelling activity. These costs will generally contain the following components:

EC1: Cost of purchasing and storing solvers. Costs associated with solver acquisition can be particularly significant in the case of mainframe dependent modelling. Note, however, that these are one time as opposed to the recurring costs identified below.

EC2: Cost of model storage. With the continuing rapid decline in storage costs, it is expected that this cost component will cease to be significant in the long run.

EC3: Cost of communicating model queries from one location to a remote site. While communication costs are also declining, the decline is at a slower rate than storage costs. At the current time, these costs continue to be an important design criterion for distributed computing in general, and must be addressed carefully.

EC4: Cost of model updates. Model updates may be initiated from local or remote locations, depending on the location of the model vis-à-vis its developer. In the latter case, there is a definite cost associated with the remote access required to update a model.

## Organizational factors

Organizational factors pertain to concerns related to the security and integrity of the distributed model base. They also include issues related to managing the DMB.

OC1: Security of models: though the intent of a DMB is to increase the organization-wide sharing of models and to avoid 're-inventing the wheel', tighter control procedures may be required in order to restrict and control access to models. The design of a DMB must provide for security, in a manner similar to a distributed data base.

OC2: Model ownership: at what point does a model developed by an individual become public domain? Who decides when a model is ready to go ‘public’? Is the owner the sole person with the authority to perform model updates? These questions necessitate the development of policies and procedures to control the modelling activity.

OC3: Role and duties of the model base administrator: in organizations where the modelling activity is fairly widespread, it may be beneficial to identify a separate individual responsible for managing the distributed model base. For organizations already using a distributed database, the additional tasks could be made the responsibility of an existing model base administrator.

OC4: Nature of organizational dispersion: for organizations with a highly functional geographic dispersion, locality of reference for models would be high. In other words, model usage between locations would be low. The system then reduces to a collection of independent sub-systems with very little interaction between sub-systems. In such a situation, one might question the worth of developing a distributed model base.

Factors related to the modelling activity

MC1: Who would be responsible for quality assurance of models? Should there be a central site that performs this task? Or should it be performed at local sites? The answer to this question may depend upon additional factors such as the nature of organizational dispersion and the existence of a distributed database.

MC2: In order to avoid inappropriate modelling, storing and displaying model assumptions are crucial tasks. How will this be undertaken?

MC3: For ad hoc modelling, it is often necessary to chain together existing models. In a distributed setting, chaining may become extremely difficult due to incompatible machines at different locations. Additional communications costs may also be incurred if a significant amount of model chaining is required. Would it be worthwhile then to allocate models as some form of logical clusters, if it is known ahead of time that some models are more likely than others to be chained together?

## Technical factors

TC1: Model representation (Dolk and Konsynski, 1984). This factor primarily affects the conceptual design of a DMB, though it can have implications for the physical design as well. In this research, we assume the conceptual design of the model base to be given.

TC2: Telecommunications network design. Organizations which already use distributed computing will have a telecommunications network in place. The design of this network will impact the design of the distributed model base. If the network is just local area then perhaps a centralized model base is feasible. A different design strategy may be required for a medium area network (MAN) (i.e. a group of local area networks at each site, connected via a wide area network. This type of network is fairly common in large cities).

Several of the criteria described above [e.g. TC2, MC1, MC2, OC2, OC3] are really policy-related issues that need to be resolved prior to the construction of a distributed model base. Other factors such as OC1, MC3, and TC1 must be incorporated in the conceptual design of the DMB. Some remaining criteria are non-quantifiable and cannot be incorporated into any analytic formulations of the model allocation problem. However, they may be used as constraints in analysing a given physical design for acceptability. Criterion OC4 can be indirectly captured in an analytic formulation by the demand on models from each site in the network. While it would be desirable to represent models uniformly so as to obviate the need for storing procedural details, the feasibility of enforcing such representation standards in an organizational setting is still a moot issue. Until that time, the dependency between models and the tools required to solve them will exist.

As is the case with distributed databases, we anticipate that the design of a DMB would involve a two-stage process of conceptual design followed by physical design. While conceptual design refers to a global organization of all the entities of interest and other issues such as concurrency control, etc., physical design delineates how these entities will be partitioned and the manner in which partitions will be allocated to individual sites in the network.

In distributed database design, the entities to be allocated depend on the conceptual schema underlying the global database and the logical manner in which the data are organized (Ceri and Pelagatti, 1984). In DMB design, a natural partition of entities already exists in the form of models and solvers. While it would be desirable to integrate all the models developed within an organization into a single conceptual schema prior to allocation, we do not address that issue here.

## Distributed model base design

There are two issues that are of concern in the distributed model base scenario. The first relates to the design and architecture of the distributed model base and can be viewed as a meta-modelling activity that models currently existing models in the organization. The questions to be addressed by this meta-modelling activity include: (1) what are the objects or units of interest that must be stored, given the constraints of the organizational arrangements, and (2) how should this storage be structured so as to satisfy user access requirements, organizational control requirements, and maintenance of model consistency.

The second issue in distributed model base management relates to the role, duties, and location of the individuals responsible for establishing and managing the distributed model base. It has been recognized that the model management activity will supersede the data management activity in the not too distant future (Konsynski and Sprague, 1986) and organizations need to be aware of the resource commitment in terms of personal requirements.

In general, two broad approaches have been suggested for the design of distributed database management systems (Adiba et al., 1979). The top-down approach is appropriate when the database philosophy is already in operation in an organization or when it is desired to induce cooperation among homogeneous database management systems. A global design strategy is applicable in the top-down design approach. However, when heterogeneous databases are already in use in different organizational units, a bottom-up approach is needed to integrate and unify these databases. In many organizations, user developed models using different modelling tools and hardware/software configurations exist currently. Owing to this heterogeneity, and since the activity of model development has preceded the integration and control activity, we focus on the latter bottom-up approach.

A model is defined as a user-constructed collection of logically related organizational relationships that transform a set of input variables (IV) to obtain values for a set of decision variables (DV), using a particular solution technique. The solution procedure is associated with a particular solver. An example of a model is, thus, a series of forecasting relationships that express how sales forecasts in future time periods are dependent on actual sales levels in previous time periods, advertising expenses and product price. This model is solved using a statistical software such as SAS. It must be noted that the forecasting relationships are represented in a form that is recognizable to SAS.

The heterogeneity in the organization's current modelling activity results from the relation-solver dependency which impacts the models representation scheme. With the methodology proposed in this paper, we attempt to facilitate organization wide model sharing and the use of existing models to construct larger ones. We assume that the existing model representation technique remains unaltered.

At the lowest level, the organizational relationships (henceforth referred to as models) form the basic unit of allocation to geographically dispersed locations. In practice, these relation sets are often sequenced to form larger models, that are used for decision making in specific application areas. These model sets are referred to as meta-models. In a distributed environment, meta-models exhibit logical integration, though individual models can be physically dispersed over a geographic region. At the highest level, meta-models along with the associated solvers and data form specific instances of the model solving activity.

We propose a layered schema architecture for a DMMS. In the first phase of the distributed model base design, models employed by individual decision makers must be elicited. This information is used to construct the Global Model Schema (GMS). The GMS is the lowest layer in the schema hierarchy and serves to address the problem of the same logical relationships surfacing in different physical forms in different organizational units due to differences in terminology and data definitions. Knowledge maintained about each model in the GMS includes:

(1) 'Ownership' of the relation set, i.e. the organizational unit or individual responsible for its definition;

(2) The set of user supplied input variables, data that can be accessed from existing databases, and the decision/output variables;

(3) The purpose and assumptions behind the model;

(4) The model's security protocol, i.e. the organizational unit or individual authorized to redefine it;

(5) Identifiers of location(s) where this model is stored;

(6) Solver(s) required for processing the model; and

(7) A cross referencing to the meta-models that currently use this set of relations.

The exercise of constructing the GMS will serve the dual objectives of making explicit assumptions used by the decision maker in model construction, and ensuring the consistent construction of models across the organization. In the distributed environment, knowledge about the solver required for model execution also serves to highlight the constraints on model solution in that not all models may be solvable at all sites due to hardware/software restrictions.

Models are reusable components that are sequenced to form meta-models. Known meta-models are logically described in the Global Meta-Model Schema (GMMS). Each meta-model in the GMMS is annotated with a description of its semantics, the problem entity or system that it models, a cross referencing to the models that are used by it, and the organizational unit where it is defined. The location of each meta-model's individual components, and the security protocols can be obtained from the GMS and need not be stored in the GMMS.

The final directory maintained by the DMMS is the Global Solver Schema (GSS). The GSS contains an inventory of the modelling tools (e.g. spread-sheet packages, statistical analysis software, procedural languages, mathematical programming software, etc.) available in the organization. The GSS can be viewed as an 'information centre' for solution techniques. Knowledge about where a tool can be obtained is essential for increasing its availability. This impacts user productivity who will be now able to exploit the communications network to construct and execute models that cannot be solved locally.

Several benefits are evident from this layered schema architecture. First, different levels of logical abstractions of models will allow the model base to be utilized by users with varying levels of familiarity with and expertise in modelling. This should positively impact the diffusion of modelling with the organization. Second, the abstractions, and the modularity thus achieved, will allow the system administrator to manage the complexity of the model base very easily. Third, a high degree of logical/physical independence can be accommodated through the construction of schemas. Finally, management will be able to exercise the requisite degree of control and ensure a certain level of integrity in organizational decision making.

Each of the directories described above can be centralized, i.e. maintained at a single location, local, i.e. partitioned based on access needs, usage patterns, and storage costs at remote sites, or distributed, where each location maintains copies of the directory. The decision on what type of directory allocation to adopt is contingent upon a variety of factors, which include model usage (high or low), the type of DSS development that is most prevalent (ad hoc or institutional), the degree of control desired, the security requirements, and the functional dispersion of the organization. For example, in the case where a high degree of control is required, centralization of the directories would be appropriate, whereas for technologically sophisticated users who have been involved in modelling for some time, a certain degree of autonomy through local directories would be more suitable.

## Distributed model base administration

Model administration has been identified as a new organizational function whose mandate is to coordinate, guide, manage, and control the modelling activity in an organization. The onus of model administration falls upon two key individuals: the model administrator (MA), who is concerned with planning and control, and the model base administrator (MBA), who is responsible for the technical configuration of the MBMS (Dolk and Konsynski, 1985).

The role of the model administrator is a strategic, managerial one, where duties include the formulation of policy which delineates the role of modelling in the organization, and the design and implementation of strategies for the organization-wide utilization of models. The MA would also be responsible for auditing the model base to verify its consistency and security arrangements. The MBA is described as a technical specialist who designs, operates, and maintains the model management system. For distributed model management systems, this role may be replicated in a number of individuals, called local model base administrators (LMBA), who are responsible for the design and maintenance of model bases at local computing sites.

In DMMS, a third role is necessary for the management of the distributed model base. This role, embodied in the duties of the model distribution administrator (MDA), is similar in focus to that of the data distribution administrator (Martin, 1981). The MDA is responsible for defining and implementing the model distribution strategy. (S)he must be located at the central site in the distributed organizational configuration, as this location allows a global evaluation of the needs of local sites. The types of decisions to be made by the MDA include the allocation of models and solvers for storage at local sites. Notice, that for an organization which does not exhibit a high degree of functional dispersion (e.g. a bank, where each local office performs essentially the same functions), the role of the MBA and MDA can be accomplished by a single individual. However, for an organization where its geographical distribution mirrors its functional distribution (e.g. a manufacturing facility, with distinct production, sales, and marketing sites), the needs of local sites for relationships will tend to be highly disparate. Further, such a scenario has implications for consistency maintenance as local users will have a greater need for relationships defined at other sites. In this case, a distribution of duties between the MBA and MDA would be more appropriate.

## Conclusion

Distributed model management systems represent the next frontier in the organizational usage of DSS technology. This paper has described the objectives of a DMMS, suggested an architecture for designing a DMMS, and examined the role of individuals responsible for managing the DMMS. In addition, some issues that must be addressed before a model allocation strategy is implemented have been noted.

The architecture presented here satisfies the organizational and individual objectives of control, flexibility, and reusability. It has applications in group decision support systems (GDSS), where the model base of the GDSS need only contain the schemas. At a very simplistic level, the different schemas proposed in this paper can be implemented as database files. More importantly, the architecture suggests some principles for structuring model bases that are applicable to a centralized environment also.

In this research, we have focussed on organizations where modelling activity has preceded the need for integration and control. The bottom-up approach utilized does not address the problem of diverse model representation schemes that may complicate the process of remote model access and sequencing of individual models to form meta-models. Future research should address the model representation issue in the DMMS context.

Though we raise issues that must be addressed before a model allocation strategy is obtained, no attempt has been made to develop a methodology, incorporating these issues, that will provide assistance to the model distribution administrator. Future research should attempt to provide support for this task.

## References

Adiba, M., Chupin, J.C., Demolombe, R., Gardarin, G. and Le Bihan, J. (1979) Issues in distributed data base management systems: a technical overview, in IEEE Tutorial: Centralized and Distributed Data Base Systems, IEEE Computer Society.

Alavi, M. and Weiss, I.R. (1985) Managing the risks associated with end-user computing. Journal of Management Information Systems, 11, 5–20.

Blanning, R. (1989) Model management systems, in Decision Support Systems: Putting Theory into Practice, Sprague, R.H. and Watson, H.J. (eds) (Prentice-Hall, Englewood Cliffs, NJ), pp. 156–169.

Ceri, S. and Pelagatti, G. (1984) Distributed Databases: Principles and Systems. (McGraw Hill, New York).

Dolk, D.R. and Konsynski, B.R. (1985) Model management in organizations. Information and Management, 9, 35–47.

Dolk, D.R. and Konsynski, B.R. (1984) Knowledge representation for model management systems. IEEE Transactions on Software Engineering, SL-10, 6, 619–28.

Katzan, H., Jr. (1979) Distributed Information Systems. (Petrocelli, New York).

King, J.L. (1983) Centralized versus decentralized computing: organizational considerations and management options. ACM Computing Surveys, 15, 319–49.

Konsynski, B. and Sprague, R.H. Jr. (1986) Future research directions in model management. Decision Support Systems, 2, 103–109.

Liang, T-P. (1988) Model management for group decision support. MIS Quarterly, 12, 667–80.

Martin, J. (1981) Design and Strategy for Distributed Data Processing. (Prentice Hall, NJ).

Nolan, R.L. (1979) Managing the crisis in data processing. Harvard Business Review, 57, 115–26.

Philippakis, A.S. and Green, G.I. (1988) An architecture for organization-wide decision support systems, in Proceedings of the 9th International Conference on Information systems, Minneapolis, MN, Nov. 1988, 257–63.

## Biographical notes

Ritu Agarwal is an Assistant Professor in the Department of MIS and Decision Sciences at the University of Dayton, USA. She received her PhD in MIS and MS in Computer Science from Syracuse University in 1988. Professor Agarwal's publications have appeared and are forthcoming in Journal of MIS, Information and Management, OMEGA, Decision Support Systems, Knowledge-Based Systems, International Journal of Man-Machine Studies and elsewhere, and she has presented papers in several national and international meetings. Her research interests are in knowledge acquisition, knowledge-based system development and validation, decision support systems, and group decision making.

Address for correspondence: Ritu Agarwal, Dept. of MIS and Decision Sciences, University of Dayton, Dayton, OH 45469-2130, USA.

Deb Ghosh is an Assistant Professor in MIS in the Department of Quantitative Business Analysis at Louisiana State University, Baton Rouge, USA. He received his PhD in MIS from Syracuse University in 1988. Deb Ghosh's publications have appeared and are forthcoming in INFORS, European Journal of

Operational Research, OMEGA, Annals of O.R., Journal of Database Administration and Computers and Operations Research. He has also presented papers at several national and international meetings. His current research interests are in Distributed Computing, Tele-Communications, and Decision Support Systems.

Address for correspondence: Deb Ghosh, Dept. of Q.B.A., 3187 CEBA, Louisiana State University, Baton Rouge, LA 70808, USA.
