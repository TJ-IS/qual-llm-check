---
otero_id: 23601
otero_key: "WT9Y2PBC"
title: "The business failure of knowledge-based systems: linking knowledge-based systems and information systems methodologies for strategic planning"
authors: "Nathalie N Mitev"
year: "1994"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1994.18"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The business failure of knowledge-based systems: linking knowledge-based systems and information systems methodologies for strategic planning

NATHALIE N. MITEV

Information Technology Institute, Salford University, Salford, UK

It is first argued that the commercial failure of knowledge-based systems (KBS) is due to the lack of business emphasis of KBS development methodologies. This article outlines the evolution of KBS methodologies and the recent change of emphasis from a technology-driven to a business-led approach. It further examines the 'application identification and selection' activities of two KBS methodologies, KADS and STAGES. Their weaknesses are highlighted and it is argued that an integrated strategic methodological approach to the development of information systems and knowledge-based systems is required. The strategic phase of an IS methodology is then summarized; specific points within it where KBS-related activities could be incorporated are identified. This exercise illustrates how IS methodologies could be used as a basis for the joint strategic planning of IS and KBS systems.

## Introduction

Technical reasons are usually invoked for the commercial failure of knowledge-based systems (KBS). It is argued here that KBS have suffered from a technology-push perspective at the hands of technologists insensitive to business and organizational needs. Early KBS commercial development was driven by the existence of expert system shells and characterized by prototyping; as a reaction, the emergence of KBS methodologies was motivated by a need for well-engineered technical products. KBS development methodologies therefore initially concentrated on techniques and methods tackling knowledge engineering problems (as opposed to traditional programming problems).

More recent issues which need to be addressed by KBS methodologies in order to progress beyond the development of isolated technical artefacts are categorized into strategic issues, design for integration with other information systems, testing and design for maintainability and implementation issues. This represents a shift away from knowledge analysis and design issues and a realization of business, human and organizational factors.

One important contextual factor is the growing need for integrated KBS and information systems (IS) solutions. There is also a corresponding need for more integration between KBS and IS methodologies. The way in which current KBS methodologies support the strategic task of identifying and selecting an appropriate KBS application needs to be examined further. The strategic planning activities of two particular KBS methodologies, KADS (knowledge analysis and design system) and STAGES (structured techniques for the analysis and generation of expert systems), are compared and their limitations emphasized. Despite some overlap, it is shown that STAGES has a much stronger focus on strategic planning issues than KADS, which comes from an Artificial Information (AI) tradition. STAGES draws upon IS planning techniques and adapts them for KBS planning purposes.

There is a strong convergence between KBS and IS at the strategic planning phase. Furthermore, IS methodologies consider the whole of the business and KBS methodologies would benefit from this holistic approach. IS methodologies contain elaborate strategic planning and business analysis activities which could ensure KBS development is more business led and less technology driven. KBS-related matters can be incorporated into the strategic planning phase of a conventional IS methodology; this can be done through linking the final strategic planning stages of an IS methodology to the initial application identification and selection stages of a KBS methodology. It is therefore recommended to use the strategic planning component of a traditional IS methodology and complement it as illustrated below, rather than apply a KBS methodology on its own, particularly if it comes from the AI field, as KADS does.

The first section covers the recent evolution of KBS methodologies. The following section compares KADS and STAGES and identifies their weaknesses and the third section illustrates how to incorporate KBS-related issues into the strategic planning phase of an IS methodology.

## KBS and KBS methodologies

## The failure of KBS

One such commercial developer [of business expert systems for commercial use] estimates that in today's environment there are 100 expert systems failures for every one success (Coats, 1991).

Although a large number of KBS have been developed, the number of operational systems is few (Gupta and Biegel, 1990).

Some argue that the reason why expert systems or KBS have not been a resounding success in the 1980s is that the technology is not mature enough to build systems whose performance can be guaranteed. The technology has limitations due to unresolved theoretical issues. On the other hand, many authors state that if expert systems or KBS have not been successful it is not due to technical failure:

60% of difficulties organisations have with Artificial Intelligence and knowledge-based systems are in fact non-technical (Wainwright, 1991).

The failures have very seldom been technical ones. Most frequently, the development team produces what they consider to be a successful technical response to the business problem described to them, but the system fails to meet business and organisational needs, and remains forever a demonstrator (Thomas, 1991a).

Both lines of argument can be related to the fact that most expert systems development initially started as research initiatives in the academic sector or R & D projects in other organizations. Expert systems may have proved to be successful in a research setting, but these successes are not necessarily reflected commercially because of the requirements and constraints of a commercial environment (Jamieson and Szeto, 1989).

Furthermore, the selection of a suitable expert system application has been prone to a technology-push perspective. The many books and technical papers on expert systems or KBS often have a chapter describing how to select a suitable application area. However, this generally means looking for an application which can suit this particular technology rather than the other way round, i.e. starting from a business problem and seeing which type of technology can solve the business need most effectively. As Montgomery (1991) argues, the search for an application area suitable for expert system development often meant that 'KBS enthusiasts scoured their organizations in search of projects which would serve as a vehicle for promoting both the technology and their own careers'.

This perspective often resulted in significant investments being made before discovering properties that made the application area an undesirable candidate for KBS technologies (Laufmann et al., 1990). In other words, KBS technology may have been the wrong technology for the particular application area and/or other non-technical properties such as business or organizational factors may have been overlooked. In both cases, the question should have been posed the right way round: given a business need and an organizational context, how can an application be identified and which technology can develop it the most effectively, whether KBS technology or not.

The next section briefly reviews the emergence of KBS methodologies and emphasizes the fact that their primary aim was to develop well-engineered products.

## KBS methodologies

Many expert systems were initially developed using commercial shells which offer a limited number of knowledge representation techniques. They were developed using the prototyping approach and were built as stand-alone systems. Moreover, KBS were almost invariably developed in end-user departments until recently. 'The whole concept of a KBS seemed inimical to the mind-set of the MIS department' (Montgomery, 1991). As a result early KBS were mostly stand-alone and did not have access to corporate data.

A need for integrating expert and conventional systems and away from building stand-alone expert systems has increasingly been identified (Kerry, 1990; Gillies, 1991; Thomas, 1991a). Hence, prototyping on its own as a development methodology was seen as inadequate – as well as being partly responsible for badly engineered commercial products.

Prototyping and the use of commercial shells may still be useful for the design of small, self-contained, standalone, exploratory or short-lived applications, but the trend is towards bigger KBS, integrated to conventional systems. This necessitates effective design and development methodologies, without which, Jamieson and Szeto (1989) predicted, interest in expert systems would diminish.

Traditional programming methodologies were inappropriate for KBS development, being more suited to well-structured problems. A progression towards developing specific KBS methodologies was inevitable. During their survey of 11 commercial organizations, Jamieson and Szeto (1989) found that for in-house applications expert systems designers were often developing their own methodologies. Amongst professional groups, such as auditors, individual experiences with expert systems have been used to begin the construction of larger KBS and dedicated development methods are being designed (Stuart, 1991).

Existing KBS methodologies vary enormously in their level of detail and orientation and put their emphasis on different aspects of the development process. Hilal and Soltan (1991) provided a descriptive framework which allows the depiction of essential features of a KBS methodology to simplify the comparative study that a knowledge engineer might be involved in. Some methodologies are dedicated to large projects (NASA-developed methodology), some are user-oriented (POMESS - People Oriented Methodology for Expert Systems, an Alvey project), some are mainly concerned with knowledge elicitation (KEMRAS - Knowledge Elicitation Methodology for Research Associations, another Alvey project), while others impose one life-cycle model development encompassing all the stages and implicitly suggesting their applicability in every case (KADS - Knowledge Analysis and Design System, an ESPRIT project). Montgomery (1991) compares various KBS methodologies in terms of their origin and suppliers. The originators are either KBS technologists (KADS, KnAcq, RIME) or will have a strong slant toward conventional information systems practice (STAGES, Model/1, SUMMIT-Dk, etc).

## Evolution of KBS methodologies

Most KBS methodologies have now reached the stage of fully structured methodologies, include such considerations as project management and logical design and resemble a conventional IS approach. It is still accepted that using simple evolutionary development or the prototyping methodology can go a long way for straightforward KBS applications, using expert system shells. But ‘proper’ methodologies are really essential when large or long projects or long-term applications are to be attempted.

The general view is that better methods and techniques are necessary for designing large KBS. Klahr (1991) proposed such improvements as developing quality and testing plans, achieving verifiability and maintainability of systems, defining user acceptance criteria and planning transition to the user community. 'Computer-aided knowledge engineering' tools are now appearing; they include knowledge elicitation and modelling tools, code generation tools, editors and browsers, etc. Newer issues that KBS methodologies have to address can be summarized as follows.

(1) Strategic: how to decide which KBS applications are appropriate for the business organization.

(2) Design: how to embed KBS components in large integrated KBS and IS solutions and how to test and maintain large KBS.

(3) Implementation: the human issues and consequences for individual users and organizations (see Berry and Hart, 1990).

Implementation and design issues are not addressed any further in this paper; the first issue, strategic planning of KBS, will be the main focus of the following sections. However, before concentrating on strategic issues, it is important to briefly mention trends towards greater methodological flexibility, which should accompany closer integration between KBS and IS design.

The scope of a KBS methodology, i.e. the different sizes and types of applications catered for and the different project activities covered, must be flexible. For example, an organization which uses a classical waterfall development life cycle and expects to formalize a specification will find it difficult to adjust to the uncertainties of evolutionary development. Many of these scope issues are alleviated if the methodology is flexible or, in other words, has an ‘open’ philosophy: ‘Is it possible to add new techniques, or to import your organisation’s current methods, practice and tools, to operate under the aegis of the methodology?’ (Montgomery, 1991). In the more advanced of conventional IS methodologies, guidance is now available in the form of a ‘meta-methodology’, to help developers modify the methodology to meet their own requirements (Thomas, 1991a). KBS developers must therefore anticipate possible links between KBS and IS methodologies in order to provide for this openness. This is extremely relevant in the context of integrated KBS and IS solutions.

## Integration with IS methodologies

Most organisations believe that knowledge-based information systems will become a part of the IS environment ( . . . ) They believe that the technology will be absorbed into their mainstream information systems in the future ( . . . ) In the future KBIS will be integrated with other different types of KBIS and IS with the ability to access corporate databases in a distributed environment (Jamieson and Szeto, 1989).

Not all KBS encode human expertise and applications using KBS technology for building conventional systems are becoming prominent. Some such examples are the use of KBS technology as a programming environment to reduce software development time in the American Airlines frequent flier system or to provide a system with more sophisticated functionality such as the Ford's TIES system (Klahr, 1991).

However, learning, understanding and using different formal methodologies for systems development is perceived to be difficult and few organizations are prepared to make the necessary investment. Thomas (1991a) believes that organizations which are able to communicate effectively, including by means of a compatible methodology, between their expert systems activities and their conventional IS activities will be in a powerful position to take advantage of both business and technological opportunities.

The need for KBS methodologies to complement the conventional software methodologies in use today is now being more widely recognized. It is realized that ‘the easier a KBS methodology can fit in, or at least complement existing methodologies, the easier it is for organizations to adopt KBS development’ (Klahr, 1991). Therefore, the overall trend in expert systems development is for closer integration with conventional IS development projects. Expert system methodologies will be increasingly integrated with and may indeed form part of conventional methodologies.

On the other hand, knowledge engineering has been characterized in terms of its differences from software engineering. Killin et al. (1991) have examined the similarities and differences between them and have found that structured approaches to the two disciplines follow a pattern of convergence and divergence. There is divergence between the two methods at the feasibility and analysis stages, convergence at the design and coding stages, divergence during testing and debugging, convergence at the implementation stage and divergence during maintenance. Killin et al. (1991) examined each development stage in detail and concluded that there are more or at least as many similarities between IS and KBS developments as there are differences.

Davenport et al. (1991) tried to integrate the KADS methodology with a conventional method, IEM and its CASE tool. They found that, for instance, relating the KADS model of expertise to the conventional analysis was not easy. They summarize the main problems regarding the integration of IS and KBS methodologies as follows (Davenport et al., 1991):

(1) the data orientation of conventional methods;

(2) the conventional nature of the human-computer interfaces;

(3) the strategies for identifying KBS applications.

Tansley and Farrell (1991) used KADS in the development of a small embedded KBS where KBS is mixed with conventional software technology and found KADS effective enough. However, the handling of large and more complex mixtures of conventional and KBS functionality is still seen as an unresolved problem. As has been seen in this subsection, linking KBS and IS methodologies is being seriously investigated. However, it seems that most of this work is concentrating on technical aspects, i.e. modelling and interface design, rather than strategic planning.

## Limited strategic planning

Most KBS development methodologies have concentrated almost entirely on technical issues and little on business, strategic or organizational issues. Strategic issues are rarely considered and, as a result, expert system groups are often poorly regarded by users and conventional IS developers within their organizations.

Jamieson and Szeto (1989) found that the methodologies they reviewed from the literature lacked consideration of the activity of project selection; the methodologies often assume that an application exists and that the justification for its development will be carried out at the feasibility stage. However, in a commercial environment, organizations examine a number of potential areas for systems development and they need to determine which applications can be considered vital to the organization.

Several KBS methodologies have added some project identification and selection activities which take place before the feasibility stage. These activities help identify and prioritize potential KBS applications according to predetermined criteria. Depending on the organization, some identification criteria can be areas of high staff turnover, experts hard to find, considerable training required, retention of expertise required and competitive advantage. Critical success factors can also be used as one of the means to identify and prioritize potential applications. Some selection criteria can be the existence of development tools, management problems, integration with existing systems and financial viability of the project.

Laufmann et al. (1990) introduce the concept of expert systems to help pick the right expert system application. The DTI 'Knowledge at Work' technology transfer programme, designed to help management in UK companies make informed judgments about the use of KBS and to help them reap the benefits of this innovative technology, offers an 'Expert Guide' software package; it will assess the feasibility of a potential KBS application (DTI, 1992). Another DTI guide to KBS in the UK (DTI and Touche Ross Management Consultants, 1992) recommends following the same disciplined, structured approach when developing KBS as when developing any other system. However, it does not present any methodological approach to KBS strategic planning and does not provide methods or techniques to support the identification and selection of KBS applications.

Methodologies should help analyse the applicability of KBS technologies to specific problems; procedures are needed for assessing potential tasks for KBS applications to help determine early on whether KBS techniques are inappropriate or disadvantageous in solving a business problem. Laufmann et al. (1990) suggest scoring boxes which consider a variety of factors, which lend positive or negative support to using a KBS approach. Their experience suggests that users who take the time to use this procedure will make better decisions about potential KBS applications at an earlier point in the analysis process.

Existing work on strategic planning of KBS is piecemeal, fragmented and isolated from other IS planning exercises. The next section compares two major KBS methodologies with respect to their application identification and selection activities.

## Application identification and selection for KBS development

Two KBS methodologies, perhaps the two best known ones, KADS and STAGES, are briefly introduced and compared; each is then examined in more depth with respect to the application identification and selection activities they both present as the starting point of their methodological approach to KBS development.

## KADS

KADS is a structured methodology similar to conventional systems development methodologies in that development is separated into the phases of analysis, design, coding and maintenance. KADS provides techniques to support the acquisition and modelling of human expertise during the analysis phase (Hickman et al., 1989). KADS is also supported by a prototype knowledge engineering work-bench. KADS has been applied to many business areas, such as credit card fraud detection (Killin, 1990), marketing planning, company pension product advice, order picking and sequencing and printed circuit board bonding alarm diagnosis.

The KADS II project will provide a more complete and integrated set of support tools. Its aim is to bridge the gap between KBS development methods and other methodologies, in order to facilitate acceptance and compatibility with more conventional approaches to systems development, not only in terms of structure and contents but also in delivery environment (KADS II, 1990).

KADS is seen as having been seminal and a major influence in many KBS methodologies (Montgomery, 1991). Model/1, which is internal to Arthur Andersen, is based on KADS. Hilal and Soltan (1991) view KADS as a well-tested methodology, with both academic and commercial strengths. They point to its emphasis on modelling expert thinking and expertise and to its unique approach to implementation-independent conceptual models. They consider that its structured approach is easy to comprehend but that the language used during the analysis stage is difficult to learn and apply. They also estimate that KADS makes the implicit assumption that it should apply to all KBS development processes, regardless of size, expertise, users and developers.

Many features of KADS are being adapted and included in GEMINI, the General Expert Systems Methodology Initiative, backed by the CCTA (Central Computing and Telecommunications Agency), the MOD (Ministry of Defence) and DTI and intended as an open standard, seen as the equivalent of SSADM for conventional information systems (Flood, 1990; GEMINI, 1991). It may also be noted at this point that GEMINI does not appear to have a strategic planning stage or component, in the sense envisaged in this article.

## STAGES

STAGES is designed to be compatible and 'linkable' to traditional information systems methodologies such as SSADM or Information Engineering. Its origin is in the IS discipline, as opposed to KADS. KADS is being used more widely and has been published and taught extensively since 1986. STAGES was first published in 1989, is less well tested than KADS, does not have full tool support and is more suited to smaller projects than KADS (Montgomery, 1991). On the other hand, it is easier to understand.

One aim of STAGES is to be usable by information engineers and it therefore uses techniques and concepts which are already familiar to information systems designers. Compatibility between KBS and IS methodologies seems high on their agenda, as well as compatibility with GEMINI (Thomas, 1991b).

STAGES is based on extending the principles of conventional software engineering methodologies, rather than on inventing an entirely new approach: a software engineering flavour means that STAGES is more easily learnt by existing IT staff and it facilitates integration. In STAGES explicit links are made between system analysis and knowledge analysis; during system modelling expert system components are identified and non-expert components are passed to the data and process design stages of SSADM or Information Engineering (Thomas et al., 1991).

## Application identification and selection in KADS

In KADS, ‘application surfacing’ $^{1}$ corresponds to application identification and selection. It covers the early stages of a KBS project. KADS application surfacing is followed by ‘application scoping’ which corresponds to a technical and financial feasibility study. KADS application surfacing and scoping are separate and distinct phases. The results of the scoping phase serve as a basis for the subsequent phase, the analysis (see Figure 1), which includes system requirements, organizational requirements and project requirements. Application surfacing is detailed below and the equivalent activity in STAGES will then be presented and compared to KADS.

The KADS application surfacing exercise is carried out by knowledge engineers and assumes that some business areas may have been identified previously. Application surfacing is divided into identification and assessment.

![](/api/attachments/WT9Y2PBC/fulltext/images/410c2b276dbdfa2cca6ba98433421f08410876d31ac221736d91ab1dd3ed833d.jpg)  
Figure 1 High-level KADS activities (adapted from KBSC (1990a, b))

Identification covers the definition of the problem, domain knowledge, functions, operational environment, expert or problem-solving tasks, users and the assessment of interface issues. The knowledge engineer may try to match his or her knowledge and experience of building KBS to global descriptions of the domain, using a few examples of what types of business problems are solved and in what way. The application identification enables the establishment of whether the domain and expert task appear to be suitable for imitation by computer and whether some subtask or subdomain can be defined that may suit the needs of the expert, user and environment when automated and that may support the functions that users and/or experts perform. A list of questions or issues to be considered provide a ‘methodical emphasis on the knowledge implicit in the procedures and processes of the organisation’ (KBSC, 1990b). Some examples of questions can be found in Appendix 1.

Application assessment consists of high-level scoping, first-cut technical feasibility and cost justification tasks. Once the application has been identified, questions concentrate on high-level requirements for functionality, modality, interface issues and constraints for that application. The questions examine the background, terms of reference and business feasibility, the organizational context, personnel constraints and operational feasibility and the technical feasibility (domain, task, etc.).

Some recommendations are made concerning the overall feasibility and risk assessment and some cost justification is carried out. The budget and benefits are estimated. The subsequent phase, application scoping, will use the results and carry out a full technical and financial feasibility study.

## Application identification and selection in STAGES

In STAGES, application identification and selection provide

(1) methods for identifying possible areas of benefit to the business where expert systems might be applied;

(2) methods for determining if expert systems are the right solution for the identified areas through the use of criteria which a domain must satisfy to be a candidate for expert system technology.

It is followed by a full feasibility study on potential candidates which consists of a technical and organizational feasibility and investment appraisal. This is similar to the application scoping activity carried out by KADS.

When compared to KADS, STAGES has a much stronger focus on strategic planning issues. KADS application surfacing is concerned with ensuring that all possible applications are examined in the light of their KBS potential. It is conducted by knowledge engineers who try to match their KBS experience to the particular business problems inspected. These applications are then further studied and the ones which provide cost-effective knowledge-based solutions to business problems are selected.

With STAGES, expert systems are seen as being part of the overall IS strategy so IS planning techniques, derived from Information Engineering, are used to identify opportunities. These techniques take into account business objectives and strategy, critical success factors, IT strategy and infrastructure, organizational and functional diagrams, data and information flows and requirements and knowledge sources (experts, technicians, whose knowledge is critical to the success of the business). These techniques have been adapted and are used in a systematic way through management meetings, interviews, idea generation exercises, etc. The information is then appraised through ‘classification grids’ where each business function/decision is rated on its contribution to organizational goals and its knowledge intensity. The product of the two gives a measure of the degree of benefit to the organization of building an expert system to support that area or function. This is not done as thoroughly in KADS.

Potential applications are screened by seeing whether they satisfy several criteria, which are similar to the assessment criteria of KADS application surfacing described above. Examples of criteria can be found in Appendix 2.

The STAGES application identification and selection is also followed by a scaled-down feasibility study, which corresponds approximately to some of KADS application surfacing assessment subtasks. Having identified the knowledge-intense processes and functions, the scaled-down feasibility study covers development costs, risks and tangible and intangible benefits. The next step in STAGES after application identification and selection is a full feasibility study which is analogous to KADS application scoping.

As well as emphasizing strategic issues and using IS strategic planning techniques during application identification, STAGES includes a well-defined identification and selection process which does not seem to be provided in KADS application surfacing. This process is summarized in Appendix 3.

## Linking KBS strategy to strategy formulation phases of IS methodologies

It is clear that there is an overlap between the application identification and selection in KADS and STAGES. Nevertheless, it can be said that application surfacing and pre-scoping in KADS do not consider the strategic aspects of the use of KBS (and IS in general) in organizations. Davenport et al. (1991) are also critical of the KADS surfacing and pre-scoping exercise in that it requires that someone in the business area has some understanding of what KBS are. 'The KADS guidelines do not describe what to look for in identifying KBS. This is left to experienced knowledge engineers' (Davenport et al. 1991). They had to complement the exercise by taking a high-level view of the systems the IT department provides and identifying those areas in which AI techniques can be used and by performing a stakeholder analysis of the surfaced applications, to determine which offered the greatest benefit to the business as a whole.

Candidate KBS applications should be examined in terms of their value to the business. A KBS strategy should relate to the business strategy and also to the IS strategy of the organization. Incorporating a knowledge viewpoint to the IS strategy exercise would ensure that a global high level view is adopted and that the potential of some application of KBS technology is realized; it should also facilitate integration between KBS and conventional systems. It is argued here that joining the information and knowledge perspectives in the initial analysis of the organization and its business is necessary in order to produce a business-driven IS–KBS strategy.

STAGES' use of IS strategic planning techniques reflects an attempt to link it to conventional IS methodologies at the strategic planning level. Thomas (1991a)

estimates that there is a 70% overlap between the KBS and IS approach at the strategic planning level. However, it is not clear how the KBS and IS strategy components should be related and run in practice and which links should exist between KBS and IS methodologies and at which stages. It was stated in the section on Integration with IS methodologies that there is a pattern of divergence and convergence between KBS and IS methodologies at the different development stages (Killin et al., 1991). Whether it is possible to have a more integrated approach between information engineering and knowledge engineering during the analysis is unlikely to be resolved in the short-term. One practical answer, already adopted by STAGES, is to create bridges between knowledge analysis and the conventional systems analysis. Ideally, a ‘common’ methodology could have an IS stream and a KBS stream which would run in parallel, with bridges across the two approaches and common activities where appropriate.

It is argued here that there is convergence between KBS and IS at the strategic planning phase. Davenport et al. (1991) have found that the difference between KADS and an IS methodology such as IEM, at the business analysis stage, is that

IEM begins by considering the whole of the business and generating an information model to cover this scope. KADS doesn't take this holistic view, it attempts to identify only KBS within the organisation and usually from the perspective of some part of the business. Both of these positions mean that some applications, particularly those relating to strategic or tactical decision-making do not emerge as problem areas, despite the potential of the technology for addressing these problems (Davenport et al., 1991).

There is clearly a need for a combined approach. A more integrated KBS–IS methodology should offer means to blend those two positions during the strategic planning and business analysis stages of systems development.

## 4FRONT methodology

Incorporating a KBS approach into a conventional IS methodology strategic planning phase was attempted using an IS methodology called 4FRONT (Mitev, 1991). Furthermore, it was argued that KBS should be seen in the context of all information systems. Potential KBS applications should be selected and ranked as applications amongst other potential information-based applications. Reconciling the two viewpoints should encourage routine use of expert systems where appropriate, as well as supporting the development of more integrated KBS and IS systems. Looking at KBS and conventional IS together at the strategic level is more beneficial than creating an isolated KBS strategy component. The benefits are

(1) better integration between all types of information systems, integrating data, information and knowledge (between which boundaries are fuzzy anyway);

(2) a more global view of the use and impact of all information systems on organizations;

(3) by adopting a common methodological strategic component for KBS and conventional IS, a rapprochement between KBS and IS methodologies and practitioners is effected.

The strategic phase of 4FRONT, called 4FRONT-strategy, (Deloitte and Touche, 1991a) was examined; areas and tasks in the 4FRONTstrategy methodology where a KBS approach or concern should be added or integrated were suggested. Suggestions were made as to where the KADS methodology could be linked to the 4FRONT methodology. It was suggested that 4FRONT and KADS could then be seen as parallel ‘methodological branches’ during the feasibility and analysis phases.

The 4FRONT methodology is briefly introduced below and 4FRONTstrategy is then described in more detail. A few examples of specific tasks in the 4FRONTstrategy methodology where a KBS-related concern could be added or incorporated are given. Links with KADS application surfacing and scoping are finally suggested.

The 4FRONT methodology covers system development methods and management methods. The first component is concerned with strategic planning and is 'a method for designing an IS environment for an enterprise' (Deloitte and Touche, 1991a). 4FRONT-strategy consists of three major activities.

(1) A method for developing and agreeing upon a statement of IS direction. The method describes the analysis required to determine how well existing IS support the business needs and objectives of the enterprise. This analysis covers both internal and competitive perspectives which result in an understanding of the major business and systems issues which must be addressed by the organization.

(2) A method for developing a high-level plan which shows the architecture and projects needed to implement the IS strategy. These projects are supported by a high-level estimate of costs and benefits and the duration of the implementation is estimated. The modelling process begins with a more detailed analysis of the business, which becomes the basis for IS. In the final phase the IS strategic plan is prepared which summarizes the complete IS architecture and which contains a high-level cost-benefit analysis.

(3) A method for developing detailed project plans for the implementation of the IS strategic plan. The IS tactical plan comprises a timetable, costs, benefits and resources needed.

Each of these three activities will now be examined in more detail and an indication will be made as to where KBS-related concerns could be incorporated.

## IS direction

First, the business direction and needs are reviewed, then an internal assessment is conducted of how well existing IS support the business needs, an external assessment is carried out to study the competitive environment, IS issues and opportunities are defined and, finally, an IS strategic direction is established.

The review of business direction and needs is done through interviews with senior managers. Information systems and IS organization are surveyed and their quality appraised. IS use in other organizations serving the same market is assessed. The company's customers and suppliers, government agencies which depend on the company's information systems are surveyed. Technology trends are examined to try to understand the leverage other companies have using IT. The results are put together to identify the key issues and opportunities which provide the greatest potential to the enterprise for the utilization of IS.

Some examples of specific tasks where a KBS focus could be added are now given. Regarding concepts and techniques used, knowledge modelling should be added to process and entity modelling techniques and problem-solving requirements added to information requirements which support business functions. With respect to participants, roles and responsibilities, KBS specialists could have a role to play in the planning team, the technical team and as method analysts and user representatives could be domain experts.

When describing the organization structure and location, some consideration should be given to the location and availability of experts. During the definition of business purpose and direction, problem-solving or knowledge requirements should be added and linked to business objectives and Critical Success Factors (CSFs). An example of a CSF which could be supported by a KBS-related application is ‘reduce complexity’.

When evaluating current application systems, a KBS approach would be useful in identifying their limitations and uncover scope for new applications. Some further categorization of application types should include KBS applications, which can also support operational or planning and control functions (e.g. expert decision support systems, consultation systems, coaching systems, etc.). When evaluating user satisfaction, it would be useful to include problems and dissatisfaction with problem-solving or knowledge-related tasks.

When application and data strategies in other companies are assessed, awareness of KBS-related activities should be added (e.g. a credit card fraud detection expert system developed by a competitor). When evaluating external users' needs, their problem-solving tasks and knowledge requirements should be examined together with their information requirements.

IS leverage opportunities in supporting the business direction and needs are identified by looking at CSFs, functions, strategic targets, etc. Some awareness of KBS-based solutions may help identify more opportunities.

## IS strategic plan

The second activity is concerned with the development of an architectural model for IS support of the enterprise based on the IS direction defined in the previous activity. Five models are developed: a business model, a data architecture, an application architecture, a technology architecture and an IS organization strategy.

When developing the business model, the possible impact of IS on business issues, problems, opportunities and concerns are examined. Management, organizational, strategic and resource issues are considered. Knowledge or problem-solving requirements should be added and related to data and information requirements associated with business activities and functions.

Similarly, when developing the data architecture, entities are identified and are related to the business functions. Inference and domain layers should also be identified by reviewing the problem-solving and knowledge requirements of business activities.

Applications which support the functions and activities are also identified and pieces of functionality are separated out. Applications are grouped into information systems. KBS applications should be identified and incorporated at this stage, to ensure their integration with other applications and information systems.

## IS tactical plan

The third and final activity is responsible for tactical planning and detailed project plans are developed. The method describes the development of a portfolio of projects which actually implement the IS strategy.

Detailed project descriptions are developed: development areas are analysed in depth, including data projects (data and process models), application projects and technology projects. The suggested technical approaches for each project are examined and evaluated to ensure that the portfolio of requirements is compatible with the IS strategic plan initially defined. Projects are integrated, their impact analysed, priorities are reviewed and the project sequence revised. The costs and benefits and the resource requirements are calculated.

Some suggested points at which the KADS application surfacing (see Figure 1) could be linked into the tactical plan are during the analysis of development areas: when establishing the Information Resources Management (IRM) functions and formalizing the IRM planning process, when refining application projects and during the development of data models and when refining and reviewing the technology projects.

KADS application scoping could be linked into the evaluation of development areas: when evaluating the application, data and technology approaches to reconcile and integrate the projects and when completing the project impact analysis, i.e. estimating costs and benefits, analysing business impact and evaluating the risks.

## Conclusions

Having introduced KBS and KBS methodologies and highlighted their lack of business emphasis, this article examined the application identification and selection activities of two KBS methodologies, KADS and STAGES. It then discussed and recommended an integrated strategic methodological approach to the development of information systems and knowledge-based systems. 4FRONT IS methodology strategic phase was summarized, specific points within it where KBS-related activities could be incorporated were identified and it was suggested how KADS could be linked to 4FRONTstrategy.

However limited, this exercise shows that using an IS methodology as a basis for strategic planning and incorporating into it some KBS elements should be more valuable than designing an isolated KBS strategy component. It is a comprehensive way of reintroducing a business emphasis in the development of KBS. 4FRONT is an example of a conventional IS methodology which allows many business and IS aspects to be systematically examined at different levels in an incremental way, reflecting the complexity with which IS and business strategy issues are interrelated. Incorporating KBS elements into an IS methodology such as 4FRONT makes it possible to have a high-level view of potential KBS applications in complex business and IS environments and to prioritize them according to the respective contributions KBS and IS can make to business objectives. Adding a KBS-related approach to the strategic planning of information systems could also enrich IS strategies and perhaps help uncover useful KBS-IS integrated applications. Including strategic planning and business analysis activities may ensure that KBS are business led rather than technology driven (or even marketing driven) as has been the case in the past.

The work presented in the previous section consists of indicating precise points and subtasks within the strategic phase of this particular IS methodology, where KBS elements could be incorporated. It is only a starting point. Subsequent work should concentrate on

(1) exploring the exact nature of IS and KBS strategic planning tasks, for example, the identification of IS and KBS potential benefits and the assessment of their human and organizational implications;

(2) how to integrate them and how compatible KBS and non-KBS techniques are;

(3) testing them in real-life situations and refining the resulting IS-KBS strategy by practical KBS strategy work within an IS environment.

Experience in approaching KBS and IS together and in developing compatible methodologies, particularly at the strategic planning stage, should help link these two disciplines and build the integrated IS and KBS which are now required.

Whether KBS and IS methodologies should merge, run in parallel, have some separate activities and some others in common is not addressed here and requires more research. It seems that STAGES' strategic planning phase uses (and adapts) IS strategic planning techniques, but is run on its own. It would be useful to compare this approach to a more integrated one, whereby KBS and IS strategic planning are conducted concurrently. The size of projects, the nature of the organizations, the teams involved, etc., will matter.

KADS is an example of a KBS development approach coloured by a technologist approach, since it belongs to the AI tradition. STAGES, on the other hand, is more concerned with methodological compatibilities and integration of the IS and KBS approaches. They both have useful features and complement each other. It is not suggested here to homogenize methodologies. Instead, building on their differences should be a high priority. Methodologies have different identities, histories and inclinations. The trend towards flexible, 'open' and 'meta-methodologies' is indicative of a desire to build upon these individualities. Flexible methodologies draw upon the strengths of various methodologies and cater for alternatives according to the needs, experiences and attitudes of the business and technical experts involved. KBS isolation and parochialism cannot be allowed to survive in this context and may well have contributed to many of the failure stories.

## References

Berry, D. and Hart, A. (1990) Expert Systems: Human Issues (Chapman & Hall, London).

Coats, P.K. (1991) A critical look at expert systems for business

information applications. Journal of Information Technology, 6 (3/4), 208–15.

Davenport, C., Pinch, G., Carter, G. and Cretney, P. (1991) British Gas's experience of using the KADS methodology, in Knowledge-based Systems Methodologies Workshop, Proceedings of the First SGES International Workshop, London, 3–4 December (British Computer Society Specialist Group on Expert Systems).

Deloitte and Touche (1991a) 4Front Strategy. Vol. 1. Strategy-4direction. Strategy4development. Method Guide. Release 2.0. (Deloitte Ross Tohmatsu International, Wilton, CT).

Deloitte and Touche (1991b) 4Front Strategy. Vol. 2. Plan-4 development. Method Guide. Release 2.0 (Deloitte Ross Tohmatsu International, Wilton, CT).

DTI (1992) Support tools available from the DTI. DTI: Knowledge at Work Bulletin, 3, 8–9.

DTI and Touche Ross Management Consultants (1992) Knowledge-based Systems: Survey of UK Applications (The Enterprise Initiative Innovation Report, DTI, London).

Flood, G. (1990) Government gears up for Gemini marketing push. Computer Weekly, News Section.

GEMINI (1991) The GEMINI Handbook (developed by Ernst & Young, Touche Ross, Logica, SD-Scicon, BIS Applied Systems, Masons, HIQ Systems Ltd for the CCTA, MOD, HM Customs and Excise, DoH and DSS). (Draft copy for review purposes only.)

Gillies, A.C. (1991) The Integration of Expert Systems into Mainstream Software (Chapman & Hall, London).

Gupta, U.G. and Biegel, J. (1990) Expert systems can fail, in Svreck, B. and McRae, J. (eds), Simulation, Reality in the 90's, Proceedings of the 22nd Annual Summer Computer Simulation Conference, Calgary, Canada, 16–18 July (SCS Publications, San Diego, CA).

Hickman, F.R., Killin, J.L., Land, L., Mulhall, T., Porter, D. and Taylor, R.M. (1989) Analysis for Knowledge-based Systems: A Practical Guide to the KADS Methodology (Ellis Horwood and John Wiley, London).

Hilal, D.K. and Soltan, H. (1991) A suggested descriptive framework for the comparison of knowledge-based system methodologies. Expert Systems, 8 (2), 107–14.

Jamieson, R. and Szeto, R. (1989) Impact of knowledge-based information systems on organisations. Journal of Information Technology, 4 (3), 145–58.

KADS II (1990) KADs II. Esprit II Technical Annex for Project P5248. Area: Systems and Knowledge Engineering. Slot 1.2.3: Models, Methods, and Tools for KBS Life Cycle (partners: Cap Gemini Innovation, Netherlands Energy Research Foundation, Entel SA, IBM France, Lloyds Register, Swedish Institute of Computer Science, Siemens AG, Touche Ross MC, University of Amsterdam, Free University of Brussels).

KBSC (1990a) KADS Methodology Package. Vol. 1: Overview.
Vol. 2: Analysis (Touche Ross Management Consultants, Knowledge-Based Systems Centre, London).

KBSC (1990b) Knowledge-Based Systems Application Surfacing and Scoping within the KADS Methodology (Touche Ross Management Consultants, Knowledge-Based Systems Centre, London.

Kerry, R. (1990) Integrating Knowledge-based and Database Management Systems (Ellis Horwood, London).

Killin, J. (1990) Combatting credit card fraud with knowledge-based systems, in Proceedings of CompSec 90 International (Elsevier Advanced Technology, Oxford).

Killin, J., Morgan-Gray, L. and Porter, D. (1991) Knowledge engineering within software engineering: similarities and differences, in Knowledge-based Systems Methodologies Workshop, Proceedings of the First SGES International Workshop, London, 3–4 December. (British Computer Society Specialist Group on Expert Systems).

Klahr, P. (1991) Strategic implications of KBS methodologies, in Knowledge-based Systems Methodologies Workshop, Proceedings of the First SGES International Workshop, London 3–4 December (British Computer Society Specialist Group on Expert Systems).

Laufmann, S.C., Devaney, D.M. and Whiting, M.A. (1990) A methodology for evaluating potential KBS applications. IEEE Expert, 5 (6), 43–62.

Mitev, N.N. (1991) Integrating IT and KBS strategies: linking KADS, a knowledge-based systems methodology with 4FRONT, an information systems methodology, MBA thesis, Information Management Division, City University Business School.

Montgomery, A. (1991) Choosing the right methodology for the application, in Knowledge-based Systems Methodologies Workshop, Proceedings of the First SGES International Workshop, London, 3–4 December (British Computer Society Specialist Group on Expert Systems.

Stuart, R. (1991) The development of a KBS method for computer audit, in Knowledge-based Systems Methodologies Workshop, Proceedings of the First SGES International Workshop, London, 3–4 December (British Computer Society Specialist Group on Expert Systems).

Tansley, D.S.W. and Farrell, V.A.M. (1991) Requirements analysis for KATE (knowledge-based ASIX timescale estimator) using KADS, in Knowledge-based Systems Methodologies Workshop, Proceedings of the First SGES International Workshop, London, 3–4 December (British Computer Society Specialist Group on Expert Systems.

Thomas, M. (1991a) What constitutes a KBS methodology? in Knowledge-based Systems Methodologies Workshop, Proceedings of the First SGES International Workshop, London, 3–4 December (British Computer Society Specialist Group on Expert Systems).

Thomas, M. (1991b) The STAGES methodology. Manufacturing Intelligence (DTI Enterprise Initiative), 6, 10–13.

Thomas, M.E., Taylor, R.P. and Cumbermack, M. (eds) (1991) STAGES — Structured Techniques for Analysis and Generation of Expert Systems. Version 3.1 (Expert Systems Group, Ernst & Young Management Consultants, London).

Wainwright, C. (1991) Identifying investment in knowledge as a commodity. Manufacturing Intelligence (DTI Enterprise Initiative), 6, 6–9.

## Biographical notes

Nathalie Mitev is currently a lecturer at the Information Technology Institute, Salford University. She was previously a lecturer at Manchester Metropolitan University in the Department of Computing and for several years at City University in the School of Informatics and at City University Business School, where she also completed an MBA in Information Technology Management. She has taught business and management topics to IT students as well as IT to business students, at postgraduate and undergraduate levels.

Her current research interests are information management and the management and organizational aspects of information systems. She has previously done research and published extensively in the area of information and text retrieval and user interface design and she contributed to the design of the first UK on-line public access catalogue, sponsored by the British Library R&D Department.

She has also held several information and computing jobs, both industrial and research-oriented, in the UK and in France, where she was born and educated up to MPhil level before moving to the UK where she has lived for the last 10 years. Her academic qualifications include an MBA in IT Management (City University), an MPhil (Bordeaux) in Information and Communication Sciences, a postgraduate computing degree (Lyon) and an MSc in Information and Computing Sciences (Paris).

Address for correspondence: Nathalie Mitev, Information Technology Institute, Ashworth Building, Salford University, Salford M5 4WT, UK.

## Appendix 1: KADS application identification

## Examples of identification questions (KBSC, 1990b)

## Problem definition

1. Does everyone agree that the problem only affects one/two aspects of the organization activities?

2. Does everyone agree what the problem is?

3. If the problem is not currently solved, why not?

4. Can solutions be identified?

## Domain knowledge

1. Is there general consent on what constitutes domain knowledge?

2. Is the domain knowledge well organized?

3. Does the organization depend on the knowledge?

5. Is the knowledge reliable or well-tested?

## Expert/skill base

1. Is it easy to explain what steps are taken to arrive at a solution?

2. Is knowledge for arriving at a solution easily distinguishable from knowledge to justify a solution?

## Function

1. Can a function(s) for a possible KBS be easily identified?

2. Is the function of the future KBS easily identifiable within the organizational environment?

## Environment

1. Are input data reliable/deterministic?

2. Is 'no solution' acceptable?

## User

1. Are potential users well acquainted with the domain?

2. Do problem statements require few interactions/negotiations?

## Appendix 2: STAGES application selection criteria (Thomas et al., 1991)

1. The domain is related to an area of significant importance to the business.

2. There must be one/several experts able, interested, willing to assist in the design, development, implementation and evaluation of a system.

3. The domain must be of manageable size or capable of being decomposed into modules of a manageable size.

4. The domain is a clearly identifiable and self-contained business function.

5. The problems of a domain are recurrent business problems.

6. The domain is one in which the expertise required to solve the problems which arise is scarce or expensive.

7. The problems of a domain must be sufficiently complex to demand expertise for their resolution.

8. The expertise related to the domain must not be too volatile.

## Appendix 3: STAGES identification and selection process (Thomas et al., 1991)

1. Understand the organization (mission, strategy, structure, goals, objectives, CSFs and expertise bottleneck) by setting up meetings with senior management, obtaining key documents, etc. and organizing further interviews to construct and elaborate on documents, charts, etc. (functional decomposition, key decisions, CSFs, key data flows, key information requirements, IT strategy, and IT infrastructure).

2. Generate ideas to identify key business areas, functions and decisions, using the IS planning techniques introduced above (reform impact analysis and strategic value analysis) and noting expertise contribution and intensity.

3. Generate candidate applications using the identification methods outlined above (knowledge inventory and intensity, classification grids and opportunity indicators).

4. Screening the applications using the criteria highlighted above, including risk analysis.

5. Scaled down feasibility study where the main issues for candidate applications such as corporate benefits and time constraints are examined.

6. Prepare business case for each application (costs, benefits and risks) and present to planning committee.
