---
otero_id: 19060
otero_key: "5XV896YX"
title: "Building an IS architecture"
authors: "Young-Gul Kim; Gordon C. Everest"
year: "1994"
journal: "Information & Management"
doi: "10.1016/0378-7206(94)90002-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Building an IS architecture Collective wisdom from the field

Young-Gul Kim

University of Pittsburgh, Pittsburgh, USA

Gordon C. Everest

University of Minnesota, Minneapolis, MN, USA

This paper is the result of two years of discussion sessions with a group of managers responsible for the development and maintenance of IS architectures. The paper refines the definition of IS architecture and puts it into broader perspective by defining a set of concrete, thus more manageable sub-architectures: process, data, control and technology architectures. The resulting IS architecture framework should help the management develop a clear understanding of their critical information resources and guide them toward more effective planning and management of those resources. The IS managers in our discussion sessions shared their experiences in developing and maintaining IS architectures for their organizations. While their initial experiences were not very successful, they recognized the benefits of having a well-maintained IS architecture. They were also confident that the shared knowledge would help them avoid the pitfalls they had previously encountered and enable them to develop a successful IS architecture.

Keywords: IS architecture; IS planning; Modeling; Data architecture; Process architecture

## 1. Introduction

The last decade has seen a dramatic change of scope in the use of information technology. From the routine, number-crunching transaction processing systems of the past, information systems (IS) applications evolved to a level of maturity where some of them were used in creating competitive advantages for their organizations. Besides efficiently collecting, organizing, and storing the massive amounts of data, converting them into timely, useful information to support business processes of the organization becomes a critical capability $[8]$ . This is, however, elusive for most organizations due to the tendency of information resources (e.g., data, software, hardware, networks) to outgrow the capabilities of the present IS in size and complexity. It becomes increasingly difficult to manage this vast inventory of information resources without a clear, global understanding of their existence, location, and role as well as the dynamic relationships among them. Various IS architectures have been used to promote such understanding.

![](/api/attachments/5XV896YX/fulltext/images/fde51c9d98d32690ad039d24b240809ce4691e899a5e62b8c4dffa33de568966.jpg)  
ing. He has published in Database, Journal of MIS, Information Systems Management, and the Korean Journal of Operations Research & Management Science.

![](/api/attachments/5XV896YX/fulltext/images/d21eb3ae3dd83f87ba0fea50eceff0866628c6bd917ce7a07b16444a2a16777a.jpg)  
contributing author of the CODASYL Systems Committee technical report entitled: A Framework for Distributed Database Systems: Distribution Alternatives and Generic Architectures.

A recent survey of IS executives $[15]$ picked “Developing an Information Architecture” as the number one among the ten most critical IS management issues facing the IS executives over the next three to five years. McFarlan $[14]$ also observed that the existence of a corporate data architecture made an organization very flexible in dealing with external changes that directly affected the organization’s competitiveness. It is clear that data/information architecture is perceived by many as a critical mechanism to support this new focus on data and information. It is not clear, however, what we mean by data or information architecture. Data architecture, despite its widespread usage, has no standard definition. Much confusion surrounds the information architecture concept. Some interpret it broadly to cover all of information systems planning, design, and development $[18]$ . Others prefer a narrower interpretation, focusing on the interrelationships between processes and data $[3,9]$ . Still others interpret information architecture as a synonym for a global data structure diagram or an enterprise data model $[13]$ .

Based on the literature and the collective thoughts of practicing IS managers who are responsible for developing and maintaining their organizations' IS architecture, the paper attempts to clarify the context within which various IS relevant architectures are developed and interact. Benefits and problems of architecture-based IS management are discussed and recommendations are given to help future architecture developers build a successful IS architecture environment.

## 2. Research method

The major vehicle for this research was a set of monthly discussion sessions that the authors held with a panel of senior IS managers from private and public organizations located in a major metropolitan area in the midwestern United States. These managers were responsible for developing and maintaining IS architectures for their organizations. A total of twenty such sessions was held over a two-year period. Table 1 shows the number and type of participants.

Table 1  
Profile of discussion session participants

<table><tr><td>Type of organization</td><td>Number of organizations</td><td>Number of participants</td></tr><tr><td>Computer manufacturer</td><td>2</td><td>3</td></tr><tr><td>Food processing</td><td>2</td><td>4</td></tr><tr><td>State departments</td><td>2</td><td>2</td></tr><tr><td>University</td><td>2</td><td>4</td></tr><tr><td>Airline</td><td>1</td><td>1</td></tr><tr><td>Electronics</td><td>1</td><td>1</td></tr><tr><td>Clothing</td><td>1</td><td>1</td></tr><tr><td>Newspaper</td><td>1</td><td>1</td></tr><tr><td>Utility</td><td>1</td><td>2</td></tr><tr><td>Financial service</td><td>1</td><td>2</td></tr><tr><td>Federal Bank</td><td>1</td><td>1</td></tr><tr><td>Total:</td><td>15</td><td>22</td></tr></table>

The purpose of the monthly discussion sessions was: first, to share each organization's experiences in developing IS architectures to promote deccpr understanding of various contexts where IS architectures are developed; second, based on this shared knowledge, to identify opportunities to pursue and problems to be resolved for the successful development and use of IS architectures. Accordingly, there were two phases in the sessions to allow discussion of the two purposes.

## Phase I - First ten sessions

The first ten sessions were spent in addressing the first purpose: better understanding of IS architecture contexts. Each participant brought documentation of their architecture related work and made presentations of their company environment, IS environment, and the status and strategy of IS architecture development/usage. Based on these shared experiences, the group reviewed the literature on IS architecture and produced a conceptual framework for IS architecture as a basis to guide planning, developing, and maintaining efforts within an architecture project. In addition, to put IS architecture into proper business perspective, discussion also focused on the relation of IS architecture to a broad business planning.

## Phase II - Second ten sessions

In the second set of ten discussion sessions, the panel analyzed the potential benefits from having an organization-wide IS architecture and common problems in developing one. Based on this analysis, recommendations were made to help future architecture developers avoid common pitfalls and succeed in developing an architecture that can be used and maintained to reap the promised benefits.

## 3. Context of IS architecture

Architecture suggests synthesis, putting many parts into a whole to meet an artistic or functional need. It suggests a global view, a grand scheme or framework, showing the component parts and how they fit together. An architecture also implies a model of something to be built or managed. Similarly, an IS architecture portrays a global view of the information resources in an organization, such as data, process, hardware and software. Beyond simply listing the information resources, an IS architecture can be pictured in a diagram of major entities and relationships.

## 3.1. IS architecture framework

We now introduce a framework for IS Architecture (see Figure 1), based on previous work by Zachman [19]. He divides the IS architecture into three major streams: Data (business entity),

![](/api/attachments/5XV896YX/fulltext/images/4271541f2e85d17a0046ef248020527239de7337912fb70b1909df2bdab4100b.jpg)  
Fig. 1. Information systems architecture framework.

Function (business process), and Network (business location). Each consists of six representation levels: scope, business, information system, technology constraints, detailed descriptions, and actual system. His central theme is that one should go through this same cycle of activities in each stream in parallel.

Participants in our discussion sessions having prior IS architecture experience brought in documentation of their system and compared them with Zachman's IS architecture framework. Based on these comparisons, the group modified/ expanded his framework in several ways. First, while it focuses on the development aspect by covering technology constrained and detailed descriptions of actual systems, ours emphasizes the planning aspect of IS architecture by explicitly linking different levels of planning with corresponding levels of architectures. Second, our framework includes the cross reference matrices between major component architectures to facilitate the integration of diverse information resources. Third, we expanded his network stream into a more broad technology architecture that involves not only communication networks but also other key hardware and software configurations (e.g., computers, operating systems, etc.) within an organization. Finally, to support the dynamic IRM environment, we added a fourth dimension to handle the temporal control aspects of all information resources.

Table 2  
Components of an IS architecture

<table><tr><td>Modeled object</td><td>What is modeled</td><td>Dimension</td><td>Diagram/pattern</td></tr><tr><td>process data</td><td>transformations structure</td><td>functional material</td><td>data flow diagram (DFD) structure/IPO chart input → process → output data structure diagram data model relationshipentity ←→ entity</td></tr><tr><td>control technology</td><td>dynamics platform</td><td>temporal tools</td><td>state transition diagram prior state → post statesystem flow chart communication links client ←→ server</td></tr></table>

## 3.2. IS architecture: Components

Zachman believes that an IS architecture is a blueprint for an overall portfolio of information resources within an organization. Information resources represented by an IS architecture include data, process, hardware, system and application software, network, etc. While an information system is actually a single entity, we may have different views of it. Each view focuses on or emphasizes some particular aspect. Table 2 outlines four views of an information system. These focus on process, data, control, and technology. These views are complementary, not substitutes. Corresponding to each view we can develop an abstract model of the information system. This is analogous to the different views or subsystems in the human body – skeletal, cardiovascular, nervous, muscles, etc. An IS architecture is a composite of these component views or models. The collection of abstract models is the object of design and the basis for constructing an information system and managing information resources.

Besides the individual models corresponding to each of the views and some form of composite model, an IS architecture also includes several cross reference matrices that show the relationships between various types of objects. Cross reference matrices are used to show the relationships between any combination of object types. For example, managers and the functional areas where they work are cross referenced. They are then asked to identify their biggest problems, key decisions, or critical success factors. The answer in a given business area is generally based on information (often external, being generated or maintained outside the business area); this defines the major categories of data needed to satisfy the information needs of the business function. Due to the sheer volume of documents involved and the need to keep them up to date, the IS architecture should be created and maintained in a mechanized form, with cross references, indexes for rapid retrieval, and the ability to produce selective reports and diagrams. Design, development, and implementation should progress down each of four components of the IS architecture in parallel. At any level, information and design choices must be propagated across all four. Here is a scenario for a typical use of the four component architectures:

An organization usually purchases computer hardware, communications facilities, and networking software. A technology architecture attempts to assemble these into a working platform to deliver computing power and information to users in the organization. In many organizations, the computing and communications platforms simply evolved, sometimes without a great deal of planning. The process architecture is realized in applications software that may be developed in-house or acquired commercially. While parts of these two architectures are often purchased from vendors, data is almost always generated internally. This may explain why some companies develop a data architecture as their first step towards developing an IS architecture. The above three architectures reveal the snapshots of each of their dimensions. Over time, it is necessary to understand the dynamic nature of information resources, therefore the need for a control architecture.

## 3.3. Process architecture: The product of process modeling

Process modeling focuses on the business functions of an organization to in order to develop a process architecture. In its simplest form, a process architecture consists of a profile of major business functions performed in the organization, how they are sequenced, and the data that is transferred from one to the next. Some prefer to think of it in terms of business events that trigger business transactions. The major business functions can be decomposed into detailed processes, which may be manual or automated. The performance of business functions generally translates to application systems running on one (or more) computer systems. The process architecture may also include a profile of major application systems and how they relate to the major business functions of an organization. Methodologies and diagramming techniques, such as data flow diagrams and process hierarchy charts, represent some of the detailed design products of process modeling at a lower level.

Some understanding of the major business functions is a necessary prerequisite to data planning and the development of a data architecture. This makes it possible to discover the information requirements of the organization. Some designer/developers think it is necessary to provide a detailed definition of processes using data flow diagrams or their equivalent; the definitions are often specified down to the level of accessing individual data files one record at a time. Such a level of detail is not necessary to design the logical data structures for the real world and satisfy the information requirements of the business; all that is needed is a macro level description of the processes needed to carry out the major business functions. Process modeling needs to be iterative, with well defined deliverables at various levels of abstraction.

## 3.4. Data architecture: The product of data modeling

A data architecture takes a global view of the data resources in an organization. In its simplest form, a data architecture consists of a profile of major data categories useful to or used in various functions of an organization. Martin [12] calls these “subject databases”. Each data category is described with a relatively high-level narrative, perhaps accompanied by tables or diagrams. Each description generally ranges from a few paragraphs to a few pages. A typical set of profiles may range from ten to a few hundred. To serve as a basis for planning and setting priorities for subsequent design and development activities, the descriptions must also show:

\- How well the information needs of a business function are currently satisfied.

\- The ownership and usage pattern of a data category.

\- The criticality of each data category to the organization.

A data architecture provides a high-level, global view of an organization's data resources, actual or planned. At a lower level, we will find more detailed data models or logical database structures. Data modeling focuses on a selected part of the data architecture, producing logical data structure diagrams, which provide much greater detail to the definition, structure and characteristics of the data. There may be several data structure diagrams under a single data architecture, which integrates and relates the various underlying data models.

While the terms “information” and “data” are frequently used interchangeably, there is now a rather widely accepted distinction. Data is the encoded representation of real world objects, events, and facts, while information is derived from data and useful in problem solving or decision making $[4,5]$ . Typically, information is abstracted from data through evaluations or processing. Accordingly, the term, data architecture, seems to be easier to comprehend and communicate than the term, information architecture. The difficulty of visualizing the construct of information may have been the major reason why we find so many ambiguous and inconsistent definitions of it in the literature.

## 3.5. Control architecture: The product of dynamic modeling

A control architecture provides a temporal view on the dynamics of data, application, and technology. Unlike the large number of modeling formalisms (e.g., conceptual data models, DFDs, and system flow charts) in the other dimensions, the temporal dimension suffers from the lack of any established formalism. Even where temporal representation is available, there are not many tools to implement this in actual databases or applications. Snodgrass [16] notes the scarcity of commercial DBMSs to support the time dimension. He identifies, among many, the lack of a standard query language, inappropriate data structure, and the requirement for massive, yet unfamiliar, storage devices (e.g., optical disks) as typical roadblocks to the development of the truly temporal DBMS. Much needs to be done to enhance conceptual understanding of and tool development for the temporal dimension. The control architecture promotes such understanding and suggests a set of requirements for tool developers. The three IS areas where a control architecture will make an immediate contribution are developmental control, operational control, and maintenance control.

Developmental control handles all the changes occurring in the process of new application development over time. Also called version control or software configuration management $[1]$ , developmental control records various aspects (who, what, and when) of each change made. Differentiation of a test status from a production status allows documentation of the evolving systems and uncompleted changes to a production system by maintaining the same metadata in multiple status over time $[11]$ .

Operational control concerns the performance and integrity of current data, applications, and technology configuration. For many realtime or “active” database and transaction processing systems, integrity of the system depends entirely on sophisticated control over concurrent access and processing by multiple users. Such systems are likely to be very performance sensitive, since every response to a user request should be within limited time. Modeling the events that trigger these processes along with prior and post states of the object system will help designers to understand the complex control issues in the realtime environment.

Over time, every data, application, and technology goes through a lifecycle of its own. When the current performance is unacceptable or there emerges a new business requirement, some or all are affected. The database may need to be restructured or reorganized; applications may have to be rewritten; hardware and system software may need to be upgraded or entirely replaced. This is when maintenance control becomes a critical issue. How can we manage these changes without severely disrupting the existing operations of the business? What will be the impact of a certain change to specific parts of the organization? Who are in charge of what? Answers to these questions must be available within the control architecture to manage changes as smoothly as possible. Some of these are included in the “impact analysis” portions of modern data dictionary systems.

## 3.6. Technology architecture: The product of platform modeling

Platform modeling leads to the development of a technology architecture. The term “platform” is widely used in engineering circles to refer to the computer and communications facilities on which application systems run. The platform consists of the computer hardware and communications networking facilities. Platform modeling deals with the spatial dimension or the “where” question – where the systems/processes will run, where the users are located, and where the data is stored – and then addresses the question of how to get them all connected. Some prefer to call it hardware configuration management or network planning to emphasize the connectivity.

Larger organizations often have multiple (heterogeneous) platforms for running application systems. One of the big challenges facing organizations today is to interconnect existing platforms and to interface, even integrate, the applications on various computing platforms. Toward this end, there has been considerable activity toward Open Systems in national and international standards making bodies. While these efforts will eventually produce a set of mature standards on various technologies, it is each organization's task to configure its technology environment to support its current business needs effectively, while remaining well positioned for complying with future standards. This is an enormous challenge for any IS executive facing an unprecedented rate of technological advance. When an organization has a well-defined, well-maintained technology architecture, it should be able to monitor the performance of its technology components (e.g., computers, networks), predict future performance based on estimated business requirements, and implement necessary adjustments (e.g., upgrading, conversion, replacement) before its business is affected by the technology snag.

## 4. Relations of IS architecture to business planning

An IS architecture should stem from and be driven by the focus, direction, and priorities established in the business plan of an organization [10]. The organization is served by the IS architecture, using the information in the various categories through the IS in the architecture. The vertical chain through business planning and IS planning is detailed in Table 3, based entirely on the comments from and discussions among participants experienced in developing an IS architecture for their organization. These are strictly real world perceptions. To our participants, it was often not the formally stated missions or objectives but the informally perceived ones that drove the organizational/business planning process and determined its outcome.

## 5. Benefits of IS architecture

An IS architecture provides a framework in which informed decisions can be made by lower level organizational units. It can guide decisions on which databases and which application systems should be built. It provides information on the required scope for a development project to ensure that the resulting application system and its data will fit into the overall IS plan. Most importantly, an IS architecture shows how the defined categories of data meet the information requirements of the business functions, which in turn serves to meet the strategic objectives of an organization. It provides a global view of the information resources of an organization and establishes the basis for setting priorities on subsequent application development projects. Several benefits stem from the development and use of an IS architecture. While some of these may be well established, others deal more with promise and speculation and these require empirical research to determine the extent of their benefit.

```txt
Table 3
The business planning chain and IS architecture

Organization / business planning
Inputs:
Informal mission & objective of the organization.
(often unstated but nonetheless real and influential)
Organizational environment.
(politics, markets, competitors, etc.)
Formally stated mission, plans, direction.
(often overly general, broad and of little influence).

Outputs:
Corporate strategic plan – allocation and schedule of corporate resources.
Critical success factors
Key decisions made; key problems faced ⇒ priorities.
Identification of global & critical information needs.

Information systems planning
Inputs:
Data inventory (manual and computerized; formal and informal)
Application systems inventory
Assessment of present and future technologies.
Resource and performance requirements.

Outputs:
Information Systems Architecture: basis for scoping and setting priorities for subsequent activities of
– database design
– systems development and implementation
– IT platform configuration

– Process Planning
Process Architecture – profile of major business functions.

– Data Planning
Data Architecture – global, high-level diagram showing data categories and relationships

– Control Planning
Control Architecture – temporal view on the dynamics of data, application, and technology

– Technology Planning
Technology Architecture – profile of key hardware, software, and communication platforms
```

## 5.1. Providing an integrated view of information resources

An IS architecture focuses on the whole of an organization. Of course, the scope must still be consciously chosen, because there are many possible “systems”. By taking a global view of an organization, an IS Architecture can provide a road map for planning detailed process and data modeling activities that can subsequently support IS development. The road map reveals, through a cross reference matrix, relevant relationships between major data categories and business processes in the organization. It enables organizations to identify the relevant clients or parties that must be considered when developing an IS architecture. The matrix also makes it possible to assess the impact of a proposed change in application development project prior to its actual implementation. By allowing development personnel to see the overall picture of their information resources, it becomes easier to eliminate uncontrolled data redundancies and to resolve conflicts of use, interpretation, standards, and ownership of specific data resources before actual development begins. Thus, a global view of data seen by everyone facilitates data integration and data sharing across diverse applications.

## 5.2. Providing a more stable base for IS development

Systems development with a strong process orientation tends to meet data requirements by creating stand-alone data files and data descriptions. These are often redundant or inconsistent across projects. Such a phenomenon quickly results in unacceptably low data sharing among projects, an inflexible application development environment, and significant threats to data integrity. Perhaps, then, the most significant benefit of an IS architecture is that, contrary to the heavy process orientation of past IS practices, it focuses attention on both process and data. Finally, data is treated as a core information resource to be planned and managed, not as an unplanned byproduct of application development. As such, databases are more likely to be planned, designed, and developed in their own right, the job is likely to be done better and independent of any particular application system. Organizations need a five year development plan for data resources to parallel the five year plan for the development of application information systems.

A stronger focus on data resources provides a more stable base on which to plan for and develop information systems. It is argued that, as long as the basic business of an organization does not chance, the types of data needed remain basically the same. Sweet $[17]$ also argues that durability results from a focus on data, because database design focuses on modeling the underlying business reality. Changes in information requirements almost always result from changes in the basic business or organizational activities, whereas changes in business functions often occur without change to the information requirements. Changes to a business process may not be reflected in the high-level description but in subprocesses. People, organizational arrangements, applications, key problems of the day, and what factors are considered critical to success can change, whereas the objects of the fundamental business activities remain relatively unchanged.

## 5.3. Planning and prioritizing development projects

An IS architecture itself is not a plan or schedule for implementation of systems or the allocation of resources, but it does provide the basis for planning and prioritization of the development of databases and applications by indicating how well information needs are currently satisfied and which needs are more critical to the organization. Each development project typically focuses on a piece of the overall IS architecture. Choosing which parts of the IS architecture are to be selected for detailed design and implementation involves management, who must assess the following factors:

\- Criticality of the needs

\- Current capability - the extent to which the needs are currently being satisfied

\- Feasibility of implementation - technical, organizational, and operational

\- Level of resources required - people, skills, hardware, software

\- Expected payoff in satisfying the needs.

## 6. Problems of architecture development

The participants in our discussions were asked what they considered the major problems in developing and maintaining an IS architecture. By sharing and understanding their difficulties, participants were able to identify some common pitfalls in an IS architecture project.

## Pitfall #1. Unrealistic scope

The major failure, consistent with the findings of Goodhue et al. [6], was that they spent too long and put too much detail into the IS architecture. Perhaps their expectation was not realistic. The objective seemed to have been to develop a detailed description of all the information resources at all levels of the organization.

## Pitfall #2: Unusable, unmaintainable output

After spending a great deal of time, most ended up with stacks of paper documentation that they felt was too conceptual, bulky, and inflexible to be of real use. Because of the substantial changes that occur, the sheer volume of the paper-based architecture prevented its being updated regularly, thus discouraging its later usage.

## Pitfall #3: Insufficient staff

Despite warnings that authors such as Hoffer et al. [7] make against the normal lack of resources committed to the planning process, the staff was often less than optimal. This may have been because the staff had too much to do. But, more seriously, in many organizations, the architecture project was not given a high priority that deserves sufficient staffing. One manager from a large financial service company which had 878 IS personnel and \$60 M of annual IS budget, in discussing their IS architecture project, confessed that “I am the only one assigned to work on this (in my spare time)”.

Pitfall #4: Lack of interest among non-IS departments

To build a truly organization-wide IS architecture, inputs from various functional departmental managers are necessary. Unfortunately, not many functional managers are willing to spend their time and resources on a project of seemingly no direct interest to their departments. Some participants said that they found it very difficult to identify and change the existing ownership of data and to resolve different views and sharing of the same data among different functional departments.

## Pitfall #5: Discontinuity of planning

Participants also noted a lack of continuity in planning at corporate and divisional levels. Business plans were unstated, poorly stated, or irrelevant. The real objectives and driving organizational concerns were only known informally, at best. Indeed, when organizational goals and strategies are not taken into account, planning efforts are likely to be viewed unsatisfactory.

## Pitfall #6: Short-lived commitment from the top

Top management commitment tends to be short-lived: they preferred to see results in months not years and thus there are few incentives for planning or developing beyond divisional levels. There is no continuing, sustained focus from the top to force new systems development projects to fit into the IS architecture.

## 7. Recommendations

When asked how to avoid these pitfalls, panel participants suggested that companies planning to implement an organization-wide IS architecture should:

Keep the scope at a high level.

The primary purpose should be to develop a high-level blueprint that can then provide the basis for selecting subsequent design and development projects. The blueprint should display the highest one or two levels of each component architecture, where each should contain 10 or fewer objects of critical interest. Such a blueprint will be useful to show how the intermediate and lower level pieces fit together and where priorities should be placed. The IS architecture thus becomes more a management planning aid than a complete description of all of the information resources in the organization.

Avoid the big bang approach.

There was general agreement that a modest, sustained effort is better than a large effort at developing an IS architecture. Consistent with the prior suggestion $[2]$ , participants felt that an 80/20 rule could be followed to good advantage. With a constantly changing business environment, the quick delivery of a reasonably robust architecture, followed by its continuous refinement, was seen as far more effective.

Eliminate the paper-based architecture.

To avoid falling into the same pitfall of producing an unusable and unmaintainable architecture, participants found it inevitable to computerize the process and products of the IS architecture project. Thanks to the arrival of advanced repository tools, such as Computer Aided Software Engineering (CASE) or Information Resource Dictionary System (IRDS), organizations will find it much easier to computerize the development of an IS architecture and be very likely to maintain it, too, reaping all the promised benefits.

Make an effective sales pitch.

To be successful, IS architecture projects requires aggressive selling to non-IS departments. Only when they are firmly convinced of the promised benefits, will non-IS managers be willing to commit their time and resources to the project and be open-minded in discussing any inter-departmental conflicts in the ownership and use of information resources.

Secure an architecture champion.

Unlike application development projects for specific functional areas, IS architecture development usually has no sponsoring functional area, making it extremely vulnerable to internal politics and in resource allocation battles among functional areas. It is critical, therefore, for an IS architecture team to have at least one strong advocate of the project among the top management; this advocate will help the team in gathering necessary information requirements and in enforcing the necessary standards on the use and maintenance of organizational information resources.

## 8. Conclusion

As we move through the 1990s, we witness a slow, but clear shift of focus in IS management: from building a monolithic, proprietary system to building a flexible, open IT environment. Essential to establishing such an IT environment is our capability to understand the critical components of the environment and their relationships with each other. IS architecture helps us achieve that understanding.

This paper has refined the definition of IS architecture and put it into broader perspective by defining a set of concrete, thus more manageable sub-architectures: process, data, control, and technology architectures. The resulting IS architecture framework should help the management develop a clear understanding of their critical information resources and guide them towards more effective planning and management of those resources. The IS participants in our discussion sessions shared their experiences in developing and maintaining IS architectures for their organizations. From their initially unsuccessful project, they were able to identify six common pitfalls to be avoided for the future success of architecture projects. They firmly believe that, since the potential benefits of having a well-planned and well-maintained IS architecture were so extensive, giving up on an IS architecture project would pose a bigger risk. Shared knowledge from these discussion sessions would certainly help them avoid the pitfalls they had previously encountered and enable them to develop a successful IS architecture.

## Acknowledgment

The authors wish to thank the participants of the IS architecture discussion sessions at the University of Minnesota's MIS research center. Special thanks go to the chairman of the editorial board, Professor Edgar H. Sibley, for his personal and superb editorial help.

## References

[1] Bersoff, E.H. and Davis, A.M. "Impacts of Life Cycle Models on Software Configuration Management," Communications of the ACM (34:8), August 1991, 104-118.

[2] Brancheau, J.C. and Wetherbe J.C. "Information Architecture: Methods and Practice," Information Processing and Management (22:6), 1986, 453-463.

[3] Brancheau, J.C., Schuster, L., and March S.T. “Building and Implementing an Information Architecture: The Pillsbury Approach,” Data Base, Spring 1989, 9–17.

[4] Davis, G.B. and Olson, M.H. Management Information Systems: Conceptual Foundations, Structure, and Development, 2nd Ed., McGraw-Hill, 1985.

[5] Everest, G.C. Database Management: Objectives, System Functions, and Administration, McGraw-Hill, 1986, 816 pages.

[6] Goodhue, D.L., Kirsch, L.J., Quillard, J.A., and Wybo, M. D. “Strategic Data Planning: Lessons From the Field,” MIS Quarterly (16:1), March 1992, 11–34.

[7] Hoffer, J.A., Michaele, S.J., and Carroll, J.J. “The Pitfalls of Strategic Data & Systems Planning: A Research Agenda,” Proceedings of the Twenty-Second Hawaii International Conference on Systems Sciences, Kona, HA, January 1989.

[8] Hopper, M.D. “Rattling SABRE – New Ways to Compete on Information,” Harvard Business Review, May–June 1990, 118–125.

[9] IBM Corporation, Business Systems Planning - Information Systems Planning Guide, Publication No. GE20-0527, Armonk, NY, 1984.

[10] Lederer, A.L. and Sethi, V. “Critical Dimensions of Strategic Information Systems Planning,” Decision Sciences (22:1), Winter 1991, 104–119.

[11] March, S.T. and Kim, Y. “Information Resource Management: A Metadata Perspective,” Journal of MIS, 1988–89 Winter.

[12] Martin, J. Strategic Data-Planning Methodologies, Prentice-Hall, 1982.

[13] McFadden, F.R. and Hoffer, J.A. Data Base Management, Benjamin-Cummings, 1991.

[14] McFarlan, F.W. In Editor's Comments for MIS Quarterly (11:1), 1987 March.

[15] Niederman, F., Brancheau, J.C., and Wetherbe, J.C. "Information Systems Management Issues in the 1990s," MIS Quarterly, December 1991, 475–500.

[16] Snodgrass, R. “Temporal Databases: Status and Research Directions,” ACM SIGMOD RECORD (19:4), December 1990, 83–89.

[17] Sweet, F. “Lesson One: Durable, Doable Databases,” Datamation (31:16), August 15, 1985, 83–84.

[18] Wetherbe, J.C. and Davis, G.B. “Developing a Long-Range Information Architecture,” Proceedings of AFIPS National Computer Conference, 1983, 262–269.

[19] Zachman, J.A. “A Framework for Information Systems Architecture,” IBM Systems Journal (26:3), 1987.
