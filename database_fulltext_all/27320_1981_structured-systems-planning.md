---
otero_id: 27320
otero_key: "N98C2J2A"
title: "Structured Systems Planning"
authors: "Jim Highsmith"
year: "1981"
journal: "MIS Quarterly"
doi: "10.2307/249290"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Structured Systems Planning
Author(s): Jim Highsmith
Source: MIS Quarterly, Vol. 5, No. 3 (Sep., 1981), pp. 35-54
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/249290
Accessed: 20-12-2015 20:00 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

Structured
Systems Planning

By: Jim Highsmith

## Abstract

Information systems planning is of growing interest to many MIS practitioners. This article postulates that one key element missing from most literature on systems planning is the transition from a strategic plan to an executable, operational plan. The article then describes the application of “structured” tools and methodology to assist in improving this transition task. The process and the examples explained in the article were taken from the author’s experience in implementing them while at Oglethorpe Power Corporation in Atlanta, Georgia.

Keywords: Systems planning, structured techniques, strategic planning, operational planning
ACM Categories: 2.0, 2.40, 3.5

## Overview

Systems planning is of increasing interest to MIS professionals because of today's fast paced technological environment and the steadily rising cost of information systems. It is a difficult and yet imperative task to direct data processing efforts toward the right corporate objectives. Early works such as Sherman Blumenthal's MIS: A Framework for Planning and Development [2], and more recently IBM's Business Systems Planning (BSP) [3] stress a linkage between the systems plan and the major thrusts of the organization.

A fundamental tenet underlying BSP is that an information systems plan must be integrated with the business plan and should be developed from the point of view of top management and with their active participation . . . The planner can identify the information systems that are needed to logically support the business, and group them into an information systems network [3].

Other authors [5, 9] stress the broader context, impact, rationale, and perspectives on systems planning, and most draw the similar conclusion that once the broad “strategic” plan is completed, the “operational plan” — specified application projects or information systems (BSP) — becomes obvious. This seeming ease of transition to an application project definition is a fallacy that creates problems in implementing many such plans. Arthur Andersen’s Long Range Systems Planning methodology addresses the issue of transition from a strategic to an operational plan, but concentrates, by design, on steps or tasks to be accomplished, not techniques [1]. IBM’s Business Systems Planning seems to ignore the issue.

A tremendously wasteful amount of time and effort can be expended in developing a systems plan because the desired “output” from the plan is not analyzed first. For a plan, just as any other analytical or design document, does not produce anything except paper! Therefore it must be an input to another process before “real” products result. Ken Orr of Ken Orr and Associates, author of Structured Systems Development [6], and Structured Requirements Definition [7], emphasizes the output orientation of each systems development phase. This orientation must extend to systems planning, specifically to developing requirements for an operational plan and providing techniques to assist the transition from a strategic to an operational plan. This transition is one of the more challenging planning tasks.

In Structured Requirements Definition, Orr defines a systems plan as the “identification of the ‘right’ system or application.” Expanding on this, a more complete definition of a plan’s output would be:

\- defined systems or application projects where the definition is specific as to the scope of the work, and boundary/linkages vis-a-vis other systems and databases.

\- the desired sequence of implementation-weighting factors such as the optimal technical implementation sequence and corporate priorities.

\- strategic plans for hardware and systems software.

\- a software development strategy that includes methodology, techniques to be used, technical standards, and personnel.

The remainder of this article will concentrate on the first two items, that is, how to define adequately systems projects within the context of a systems plan.

## Oglethorpe Power Corporation

Since much of this article uses the experiences at Oglethorpe as examples, a brief introduction to the company will be useful.

Oglethorpe Power Corporation was founded in 1974 to generate and transmit electric power to 39 consumer-owned Electric Membership Corporations (EMC's) of Georgia. The 39 EMC's that comprise Oglethorpe Power serve over 600,000 residential, commercial, and industrial metered consumers, directly affecting Georgians in about 71 percent of the state's land area. With a service area of 40,000 square miles, Oglethorpe is one of America's top ten electric utilities in terms of area covered.

With a plant investment of 1.2 billion dollars, and a rapidly growing company, the requirements for a broad spectrum of systems' services are significant. The company's and the MIS department's philosophy and emphasis on adequate planning has provided opportunities to try new approaches that have already proved beneficial, and show additional promise for the future.

## Structured Philosophies, Methodologies, and Tools

The maturing of software development began as an outgrowth of project management techniques, the “delineation of the tasks to be performed and specified time-frames for each task.” Most development methodologies emerged with a sequence of events covering planning, requirements definition, technical design, and installation, but most were significantly less successful than anticipated. These methodologies provided infinite detail about “what to do,” but did little to explain “how to accomplish” the tasks, nor did they offer useful analytical tools.

Hence, the structured revolution began which has been a revolution only in data processing journals, but a much slower evolution in practice. Beginning with Dijkstra and Mills, and progressing with Ross, Jackson, Constantine, Yourdon, DeMarco, Warnier, and Orr, structured techniques began to answer the “how” questions, provide usable tools, and even alter approaches to systems development.

The structured techniques have evolved backwards as one views the system life cycle, first structured programming, then design, and then analysis; thus, it is inevitable that these techniques would find usefulness in systems planning. However, the wide scope of any planning effort makes their use more difficult to define since planning is less structured, more holistic, and closely tied to business goals, hopefully.

One basic controversy which has developed among the structured development theories and methodologies is that between the “function-centered” versus the “data-centered” approach. In the last several years these two approaches to systems development have come closer together, each drawing on the positive aspects of the other, but the underlying difference is still there. A recognition of these two development approaches is important in analyzing techniques for systems planning.

The function-centered approach, characterized by the work of Ross, Constantine, Yourdon, and DeMarco, maintains a philosophy that both the basic architectural structure of a system and the analytical process used to define it should be based on the functions or tasks to be performed. This approach emphasizes that systems analysis and specification is a process of functional decomposition. Although data storages and flows are an integral part of the analysis, the functions are primary. The technical design step then concentrates on developing a systems architecture based on functional hierarchy.

The data-centered approach, characterized by the work of Warnier, Jackson, and Orr, stresses that the least changing structural component of a system is the data structure and therefore a system's architecture should be data structured. Ken Orr and the staff at Ken Orr and Associates have developed a methodology in which requirements definition consists of: first, a functional analysis; second, an information analysis — what information is needed to perform a function; and finally, a complete, detailed definition of all systems outputs. These outputs, specifically their data structure, are then used as the basis for the architectural design of the system.

## Structured tools

Before delving into the planning process, a brief description of the structured tools used later may be helpful.

\- Data Flow Diagrams. Affectionately known as “bubble charts,” these diagrams are particularly useful in the initial phases of functional analysis at both high and low levels.

\- Entity or Context Diagrams. To some degree these are “high-level” data flow diagrams that address the overall context or objectives of a system. Ken Orr has developed some specific rules for his entity diagrams, which focus on data flows into and out of an organization.

\- Warnier/Orr Charts. These charts can be used in a number of ways for “structuring” procedures (functions) and data. With these charts, the basic control structures of alternation, repetition, sequence, recursion, and concurrency can be depicted. Another form of these charts, Cycle Diagrams, can be used to show time dimension.

## Planning Models

Each of the planning methodologies mentioned earlier, Blumenthal, BSP, etc., develop some type of “model” of an organization’s information systems. Problems with implementing some of these models have occurred.

• They are time consuming to develop.

\- It is difficult to translate the models into definitions for systems applications.

\- There are problems in relating to business plans.

\- It is hard to maintain documentation, therefore the model fails to evolve.

These problems are no different than a list for systems planning in general, but they are reiterated here because developing good models is an important key to translating strategic plans into operating plans.

Drawing from the earlier discussion on functional versus data analysis, it seems two types of models, each equally important, need to emerge from the planning process: a function or process model, which describes major functional responsibilities; and data models, which describe significant data hierarchies.

Several types and levels of models should be used in the successive refinement of strategic plans into executable application projects. In the process to be described, three levels will be discussed, although in practice the number of levels will depend on the needs of the individual organization. These three levels are:

\- strategic models,

\- application group models, and

\- application system models.

## Strategic models

First, at the strategic level, a general model is needed to provide a high level framework. From IBM's Business Systems Planning, "The network should provide a visual depiction of the strategic long range objective of the information systems plan. The network is the logical relationship of information systems, and their external interfaces, deemed necessary to support the information requirements of the organization." Figure 1 shows an early version of the "Information Resource Model" developed for Oglethorpe, which served as this high-level framework.

Although this network model is important, it needs to be supplemented, even at the strategic planning level, with additional detail. These detailed elements consist of:

\- An Entity or Context diagram that begins to define the major external organizational interfaces (see Figure 2).

\- A more detailed diagram that expands each of the network's major functions identified into subfunctions and databases (see Figure 3).

This initial process enables the planner to focus on key business functions and types of information. Although very high level at this point, it provides a framework for further analysis. Two points to concentrate on during this initial work are 1) the functional rather than the organization breakdowns, which is not always easy, and 2) any anticipated new business areas.

Figure 3 is essentially a modified data flow diagram that was developed at Oglethorpe in 1979. Showing only major functions and databases, these diagrams were particularly valuable communication devices when talking to managers and making presentations to the MIS steering committee. Although important as a “contextual” picture, these diagrams are time consuming to draw and maintain, and they tend to obscure important functional and data relationships. Therefore, in the current year's planning process, more detailed models are being developed using Warnier/Orr charts for analysis of both functions and data. These charts are used because they:

\- depict the significant business functions and data hierarchy.

\- are reasonably easy to develop and maintain.

\- are good communications tools with nontechnical personnel.

\- provide an easier way to “explode” the models into more detail.

This new function model (see Figure 4) was developed by analyzing the major objectives, responsibilities, functions, and tasks of each organizational unit and placing them in a functional hierarchy. This model concentrates on high level functional tasks, although further decomposition defining lower level tasks is part of the next planning phase.

During the development of the function model(s) the “raw” data for the data models begins to accumulate. Although the general sequence is to analyze the functions first and then the information requirements, any analytical task — particularly planning — is iterative in nature. As each function in the model is determined, the next task is to analyze the information required to perform the function and the resultant output or action. These information needs form the basis for developing data models. The data to support higher level managerial functions will probably be unstructured and external to the organization and should therefore be identified in broad generic terms. As the examined functions become more specific, the data analysis becomes more detailed.

As the information needed to perform functions is identified, data hierarchies begin emerging. Unfortunately, multiple hierarchies begin emerging, often containing the same basic data elements, and confusion and complexity soon reign. One way to attack this confusion is to build “network” data models, as shown in Figure 5.

![](/api/attachments/N98C2J2A/fulltext/images/7a67cbb9c6bbfb3178788285e34d1887edd9e7ebd05669463eddf36cf9a9e7c4.jpg)  
Figure 1. Oglethorpe Power Corporation Information Resource Model

![](/api/attachments/N98C2J2A/fulltext/images/50b122ed99711fdef29317fb1b068d0781566050d80c11a0f5067dc5f68c62cd.jpg)  
Figure 2. Simple Entity Diagram

![](/api/attachments/N98C2J2A/fulltext/images/6d8ba5183f6b8f23f19841512223be82da477f836124ee2b5f340164f3c55dc7.jpg)

![](/api/attachments/N98C2J2A/fulltext/images/1523fbfed96d3bdd90815b4a866eec05e79082d8aa42c4188ebd6b864da6e9b4.jpg)  
Figure 4. Oglethorpe High Level Function Model

## MIS Quarterly/September 1981

![](/api/attachments/N98C2J2A/fulltext/images/2a476c4efba58ad8b469ee97fd779341a44bbd523767789ef172e4ea8b46f501.jpg)  
Figure 5. Network Data Hierarchy

Although this type of data model may have good visual impact, it is difficult to “decompose” into more detailed elements. Looking at Figure 5, it is obvious that each box contains a hierarchy of data itself.

In data analysis, network representations are difficult to understand except at a high level, and access paths between elements tend to be obscure. By developing hierarchical data structures instead of network structures to support each major function, it becomes easier to communicate and therefore to incorporate more detail into the model. These data structures meet the dual objectives to communicate business needs on one hand, and technical requirements on the other. Figure 6 shows a simple example in which one data structure supports a financial statement preparation function. Even though each is simplified, they convey a significant amount of information. Project managers can analyze their data needs by examining one structure, accountants the other. It is then a technical task to combine structures into appropriate databases.

The list below provides a recap of the products of this strategic analysis:

\- a high level network model showing the major business operations,

\- an entity diagram showing external relationships,

\- a function flow diagram showing major functions and databases,

\- a function model showing a hierarchy of functions and subfunctions, and

\- data models that begin to identify and structure business information needs.

## Operational models

Keeping in mind the goal of the systems planning process — the definition of the right application project(s) — the transition from the strategic analytical products just defined to an application project definition involves the following steps:

\- aggregation of functions into application group function models,

\- definition of application group data models,

\- analysis of function and data relationships that includes development of a time cycle chart, and

\- definition of application project function and data models.

Functional areas that have some business relationship are combined into Application Groups. The Strategic Function Model aggregated functions into a logical business hierarchy. This next step of defining Application Group Models is a process of reaggregating these functions. These groups may closely parallel the major functions identified in the overall systems network, and provide a basis for further decomposition of these functions. This decomposition process has the same purpose as any other analytical task — to break a situation into components that can be conceptually managed. An Application Group might be a Financial Group or an International Banking Group, whereas an Application System might be an Accounts Payable System or a Letter of Credit System. The number of levels and the scope of Application Groups will depend on the size, type, and diversity of an organization. Application Groups could be developed for each division in a highly decentralized corporation, or for an entire corporation of a smaller size. Application Groups are then further subdivided into individual, implementable Application System Projects.

Drawing on past experience is a good beginning for developing Application Group Models, since the objective of a structured planning process is not to start from scratch but to provide tools that enhance prior knowledge. Application Groups might include: Financial, Marketing, Manufacturing, Facility Planning, and Administrative. These might be further divided into General Ledger, Accounts Payable, Sales Forecasting, and Order Processing Applications Systems. Although this division may appear somewhat trivial, by allocating to these Applications groupings the functions identified in the Strategic Function Model, and data and information needs identified in the data models, the scope of individual application systems begins to form.

![](/api/attachments/N98C2J2A/fulltext/images/ca0b8fc18c6bf0e68954c78fb43f546f1a37a3d61832325cfcf172574d2ba9e3.jpg)  
Figure 6. Sample Data Structures Supporting Two Functions

In the process of developing group and system models, two additional types of information must be incorporated:

\- feedback and control mechanisms, and

• function and data relationships.

In his new book, Structured Requirements Definition, Ken Orr discusses feedback and control as one crucial factor in defining the requirements for a system. He states that:

True systems are distinguished by their attributes. From a logical standpoint, true systems are: self-controlling, self-correcting, goal directed, persistent... Management information systems can be developed empirically by surveying managers and asking them what they want to know, or they can be developed based on a scientific analysis of the business (functional) system it supports and the feedback/control required to ensure its successful operations. In the first case, the quality of the system developed is strictly limited by the skills and perceptions of a given set of managers and users at a specific time. In the second case, the quality of the system is based on the fundamental business functions [7].

Applying these concepts to systems planning, each of the major functions identified in the models should be examined for control requirements. For example, the control for various accounting functions may be an internal auditing function. Also, the frequency with which functions and controls are performed provides additional systems requirements. Figure 7 shows a Time Cycle Chart that can be used to visualize the timing or frequency of system activities. Besides providing new function and data requirements, feedback and control analysis is also useful in setting priorities and establishing application system performance criteria.

The analytical steps of analyzing function and data relationships begin to define the scope of individual projects, the sequence of implementation, and the linkages to past and future systems. The two types of functional relationships are priority (functions that should be automated first), and sequence (specifically optimal implementation tion sequence). The priority relationships are based on how critical they are to the business needs expressed in the Corporate Plan and in projected implementation parameters (schedule and resource utilization).

Optimal implementation sequence is determined by analyzing the functional “flow,” i.e., the sequence in which the functions should be performed. This functional flow analysis can be done with high level data flow diagrams, or as shown in Figure 8, a specialized Warnier/Orr chart that Orr calls an Assembly Line Diagram. A preferred designation for this diagram at the planning level may be the more generic term Functional Flow chart.

The priority sequence and the optimal implementation sequence are often in conflict. By recognizing this conflict during the planning process and assessing its impact, the project implementation sequence can hopefully balance these conflicting objectives. The greater the conflict between these two sequences, the more thorough and detailed the planning effort must be.

The final element in the functional relationships is determining the scope of an application project, essentially how many and which functions are incorporated into a particular project. Here again conflicting objectives of greater versus lesser scope must be recognized and incorporated into the planning process.

An analysis of the data relationships provides two types of information:

\- First, it assists in defining a project's scope, since more data usually implies an expanded system.

\- Second, and more importantly, data relationships provide the key linkage information between systems.

Possibly no other piece of planning information is as important, or as frequently missing, as that concerned with linkages between current systems, those under development, and future systems. A brief, simple example may illustrate the point. If a payroll system is being designed as part of a financial application group implementation, the data hierarchy might look like the one in Figure 9. A project control system is also anticipated, but its priority is low, so implementation is scheduled several years hence. Knowing the project control system is in the plan, the payroll system designers might traditionally allow for “Project Number” in their labor distribution design. The problem arises three years later when the Project Control System design requires salary cost by project, and task! Back to the drawing board with payroll. By spending enough time developing a data structure for the project control system in a systems plan, specific linkages or access paths, can be better anticipated and allowances made in the design.

![](/api/attachments/N98C2J2A/fulltext/images/eec6656c4e716be6c1cf88150d2fae49ae77b8dda96d8382026c3d14b0456336.jpg)  
Figure 7. Time Cycle Chart

![](/api/attachments/N98C2J2A/fulltext/images/35f3e8045be6981a20003e867645994356b515c6e49076693e9fe9ff1b2cfd26.jpg)  
Figure 8. Functional Flow Chart (Assembly Line Diagram)

![](/api/attachments/N98C2J2A/fulltext/images/ec9e4941b4a4a7e695a78a425e4aca6d9ec85f071d08cb41301079311389a74c.jpg)  
Figure 9. Data Model Linkages

Scope, or boundary conditions, and linkage are symbiotic because expanding the scope, or functions, increases the information needs, which in turn changes the data linkage points for a specific system. The only valid mathematical formula that can be used as a guide here is:

As functions included in the scope approach maximum, the number of data linkages approach minimum, and the implementation period approaches infinity.

## Issues

Several important issues arise in this type of detailed planning. To some extent the procedure outlined so far appears suspiciously similar to the approach used in attempting to build the mammoth MIS systems of the late 1960's, most of which were disastrous. Some reactions to the failure of many of these systems have been to forget planning at all, a growing interest in decision support systems (“let’s try different approaches and see what happens”), and in relational databases (“If we can collect enough data and infinitely restructure it, we will be covered”). If the 1960's were characterized by over-optimism, the 1970's leaned toward resignation.

But the development and maintenance of information systems has become too expensive, regardless of the controversy about relative growth of hardware versus software costs, for any of the above approaches to be completely effective for an organization. Many monstrous MIS systems that absorb 5+ years to develop have been dated before implementation. Large, expensive databases contain far more data than necessary, not because of poor design, but because the link to corporate needs is unclear. The design practices of the 1960's which compelled us to leave "blank" fields in records for future enhancements has evolved to the current philosophy of "adding extra data we may need someday, which is OK because the database system will handle it."

One way to begin solving these dilemmas is by developing better tools to focus data processing efforts. The hope and intent of the planning process just described is to help forge that link between information systems expectations and results.

## Model maintenance

Each application system project emerges from the planning process defined as a set of models. During each successive implementation stage — functional specification, technical design, installation, and operation — the system changes to reflect increased knowledge. The ongoing planning process is enhanced when these models are updated to reflect changes. Systems planning should be a continuous process, with heavier emphasis during the annual planning cycle, but it is not an activity to be rushed through once a year and then put on the shelf. The models should be used as a constant reference point during systems development and ongoing planning.

The degree of detail maintained in the planning models is unique to each organization. Because the key elements to the operations or project definition phase of planning are scope and linkages, these must be updated continuously or subsequent planning may proceed from an erroneous basis. As more detailed planning and development work is done, the information about functions and data may indicate a restructuring of the high levels.

## Evolution of Systems Planning at Oglethorpe

Although various aspects of the planning process at Oglethorpe have been mentioned, this section outlines a brief chronology of its evolution. The starting point for systems planning at Oglethorpe has been the annual Corporate Business Plan. This plan spans a five year period with detailed concentration on the upcoming year. Efforts in 1979, and again in 1980, have been to integrate more closely the corporate and systems planning processes. When the managers have developed their business objectives, the MIS requirements to assist in meeting those objectives are identified. The priority of MIS projects then closely parallels corporate priorities. The MIS Steering Committee sets priority, scheduling, and personnel levels based on MIS's estimate for each project.

## Past methodology

During the 1979 planning cycle we decided something beyond a definition of individual projects was needed — a framework to aid communications with user department heads and the Steering Committee, and to provide MIS with a plan that transcended individual application systems. What developed was the “Information Resource Model,” shown previously in Figure 1. The model comprised components from IBM’s Business Systems Planning modified data flow diagrams, and very brief high level database descriptions. In the presentation of the model, several reasons were outlined for its development:

• to facilitate communications between MIS and client departments,

• to offer another perspective on organizational relationships,

• to assist in determining system development priorities,

\- to assist in determining the optimal development sequence,

\- to facilitate development of “multi-use” databases, and

\- to provide a plan for linking systems together.

Requirements for the model included minimizing technical terminology, maximizing visual impact, and providing a tool to be used at all organizational levels.

The Information Resource Model, the more detailed functional flow models, and the brief database descriptions became the framework upon which individual projects were assigned. This framework proved useful over the ensuing year during development projects and in talking to users about the context of new systems ideas.

## Enhancements to the 1979 process

During 1979 Oglethorpe undertook a study to determine which of the various structured development techniques/methodologies to implement.

The decisions to implement Warnier/Orr structured development techniques, install Method/1: Systems Development Practices, and install Ken Orr and Associates STRUCTURE(S) software package as a structured documentation tool, provided new tools for enhancing the 1980 planning process.

The primary systems planning focus in 1980, which is currently underway, is to complete an extensive application group plan for the development of corporate financial systems. Extensive requirements in this area within the next fourteen years dictated a careful approach to establish the proper system's scope and avoid duplicate effort, conflicting data, and systems rework.

The results, or output, from this plan will include:

\- a Financial Application Group Function Model,

• Financial Application Group Data Models,

\- a Financial Application Group Time Cycle Model,

\- identification, description, and prioritization of Systems Projects,

\- general requirements/needs for all systems in this Systems Group, and

\- implementation alternatives including overall software strategy.

In the process of completing this plan, structured techniques and tools will be used where appropriate. Warnier/Orr charts are being used to illustrate the Function and Data Models (see

Figure 10). Entity or context diagrams are being used to show major corporate interfaces with other organizations and among internal departments (see Figure 11). Using the STRUCTURE(S) package is enabling us to easily modify the models during the planning stage, providing permanent documentation, and will allow easier maintenance of the models as actual projects are undertaken.

The Systems Planning and Functional Specification sections of Method/1 have identified and organized the tasks that need to be considered, and have been supplemented with structured techniques for actually accomplishing the tasks. During the 1980 planning process we have begun developing an overall function model for the organization, although time constraints will limit detail outside the Financial Area.

## Future plans

Our future plans are essentially to refine the techniques currently in use and to expand the models in more detail. How much detail is still a question that will evolve with additional experience. Balancing the needs for enough detail for adequate planning against the accumulation of excessive detail, which hampers analysis with trivia, will be a continuing effort. As we build on these models, they will become even more important to application system specification and design.

## Reflections

This section has been called “reflections” rather than “conclusions” because I feel it presumptuous to conclude anything in the somewhat ethereal realm of planning, particularly systems planning. Information systems literature abounds with predictions of trends to come in hardware, software, office automation, the demise of programmers, and the rise of “user friendly” systems. Some of the following may sound suspiciously like those predictions, but I prefer to call them reflections.

Some of the techniques discussed in this article are in the early stages of development and use at Oglethorpe. We are in the experimental stage, without quantifiable results. The intangible results, however, point toward a better vehicle for communications with user management, our MIS Steering Committee, and toward a better definition of systems projects, but the true measures are still in the future.

![](/api/attachments/N98C2J2A/fulltext/images/f8ac20b7f41bfd7dd3db7e4f6ec54570a2a7d88a8d162fb0ab688ea085821876.jpg)  
Figure 10. Financial Plan Functional Model

![](/api/attachments/N98C2J2A/fulltext/images/23586f5744517e1ba88eae2ac9e7dcddbbf2d9b86244e797a8a47481b60e1ff5.jpg)  
Figure 11. Financial Systems Plan: Entity Diagram for Construction Work-in-Progress

The trends in software engineering over the past ten years have been backwards through the systems life cycle, from structured programming to structured design, to structured requirements definition to structured planning. I hesitate to use “structured” in the last two stages since there is more depth to the concepts than the word structured connotes. At each stage the benefits appear to increase and broaden, with an emphasis on the “appear,” since at each stage the measurement becomes exceedingly more difficult.

At the risk of being accused of extrapolating from the unproven benefits of structured requirements definition to the nebulous benefits of structured planning, I think the benefits of structured systems planning are potentially very significant. Realizing these benefits requires the development of a viable, detailed, and structured operational plan that bridges the gap between strategic MIS planning and the initiation of specific application systems projects.

Why is this planning important? The rationale is both technical and organizational. The technical reasons revolve around the deluge of goodies emerging from computer hardware factories — microprocessors, communications networks, office automation, robotics — the list keeps growing. And on the software side, we have the emergence of better development techniques, “user friendly” systems, and a plethora of software packages. With so many possibilities and the growing ability to produce software, sometimes more quickly, doing the “right” things takes considerable planning.

Although production of software for a specified task may take less time, the growing complexity of software projects often means years in development. This delay creates organizational “credibility” problems between MIS and other parts of the company. The standard approach to this problem is to divide the project into phases, or versions, to provide results in some reasonable time frame. But where do we draw the box around Phase I, II, or III? The risk of future integration problems increases proportionally to the decrease in the scope of each phase, particularly the first. The development of detailed function and data models as part of an operational planning process, and the ongoing maintenance of this information systems architecture as systems are implemented, will begin to reduce the risks of integrating systems and the overall development time. Whether it will assist MIS organizations in bringing increasingly technical sophistication to bear more effectively on corporate objectives is a hypothesis for continuing evaluation.

Any pursuit of and resource commitment to systems planning is the result of a hypothesis that planning will have a significant impact on MIS performance in providing information systems services to the corporation. Peter Drucker postulates that in the realm of management decision making there are no facts, only hypotheses that must be subjected to scrutiny.

Managers who make effective decisions know that one does not start with facts. One starts with opinions...No one has ever failed to find the facts he is looking for...We start out with untested hypotheses...One does not argue them; one tests them [4].

Sometimes in the data processing community, and the technical community at large, we become enamored with “facts” and tend to immediately descend on one side of an issue or another — distributed processing is great, distributed processing is a fad. The nuturing of ideas, taking the essence of an idea or a hypothesis, adapting it to our own environment, and enhancing it with other ideas, is often lost in the scramble to choose sides on an issue. Nontechnical endeavors such as politics, art, and literature seem to cultivate a better appreciation and understanding of ideas and their power. Theodore White, one of our best political philosophers, describes the essence of the power of ideas in his recent book, In Search of History. “Im tirtsu, ayn zeh hagadah: If you will it to be so, this is not legend” [8]. Many of the “issues” in the data processing community — systems planning, structured development techniques, office automation, etc. — should be approached from the perspective, at least initially, of learning and extracting the positive rather than the negative. I hope this article can be approached with that perspective.

## References

[1] Method/1: Systems Development Practices, Arthur Anderson & Co., Chicago, Illinois, 1979.

[2] Blumenthal, S.C. Management Information Systems: A Framework for Planning and Development, Prentice-Hall, Inc., New Jersey, 1969.

[3] Business Systems Planning — Information Planning Guide, GE20-0527-1, IBM Corporation, White Plains, New York, 1975, p. 1.

[4] Drucker, P.F. Management: Tasks, Responsibilities, Practices, Harper & Row, New York, New York, 1973, p. 470.

[5] King, W.R. "Strategic Planning for Management Information Systems," MIS Quarterly, Volume 2, Number 1, March 1978, pp. 27-37.

[6] Orr, K.T. Structural Systems Development, Yourdon, Inc., New York, New York, 1977.

[7] Orr, K.T. Structured Requirements Definition, Ken Orr & Associates, Inc., Topeka, Kansas, 1981.

[8] White, T.H. In Search of History, Harper & Row, New York, New York, 1978, p. 24.

[9] Zachman, J.A. "The Information Systems Management System: A Framework for

Information Systems Planning," Proceedings of the Ninth Annual Society for Management Information Systems Conference, 1977.

## About the Author

Jim Highsmith is director of planning and market development for Ken Orr and Associates, Inc., in Topeka, Kansas, where he has responsibility for all marketing, market development, and corporate planning activities. He is also working with Ken Orr in expanding the Data Structured Systems Development methodology in the planning phase of the systems life cycle. Previously, Highsmith was systems and programming manager for Oglethorpe Power Corporation in Atlanta, Georgia, and business systems coordinator for the Refining Department of Exxon, U.S.A.

Highsmith holds a bachelor of science degree in electrical engineering from North Carolina State University, a master of science degree in management from the University of South Florida, and a CPA certificate. He is the author of several articles, including a prior contribution to the MIS Quarterly. He is a member of SMIS and the American Institute of Certified Public Accountants.
