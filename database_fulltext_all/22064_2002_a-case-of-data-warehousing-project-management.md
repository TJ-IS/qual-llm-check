---
otero_id: 22064
otero_key: "BQ4KZVPV"
title: "A case of data warehousing project management"
authors: "Bongsik Shin"
year: "2002"
journal: "Information & Management"
doi: "10.1016/s0378-7206(01)00137-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A case of data warehousing project management

Bongsik Shin<sup>\*</sup>

Information and Decision Systems, College of Business Administration, San Diego State University, 5500 Campanile Drive, San Diego, CA 92182-8234, USA

Received 30 June 2000; received in revised form 3 February 2001; accepted 24 May 2001

## Abstract

The strategic value of data warehousing (DWG) for information management and decision support has been well acknowledged. Given scant research on the topic, this case study was intended to investigate the project planning and implementation approaches taken at one of the biggest insurance companies in the US. The company recognized that improved information management and delivery would be crucial to execute its long-term business goal, and DWG was given the highest priority. On this premise, the company pursued a pilot project. This case investigated project management issues of DWG and methodical approaches adopted by IT staff during the pilot project. <sup>#</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Data warehouse; Data warehousing; Data mart; Decision support system; Project management

## 1. Introduction

Data warehousing (DWG), which implements a shared data warehouse (DW) and/or subject-oriented data mart (DM), has become a central process for decision support-oriented data management. From its beginning as a little-understood experimental concept only a few years ago, it has reached a stage where nobody questions its strategic value. Statistical indicators and surveys show that the number of companies that already own or are currently building the decision support platform is exploding; large enterprises are involved in at least one or more related projects [21]. Databases tuned for operational and transactional use are, in general, not structured to satisfy information demand from managers. There is a growing utility gap between operational systems and decision support systems, making DWG increasingly essential to organizational decision-makers. Its vital role continues to expand as the market becomes more customer-centered and demands sophisticated business intelligence.

The DWG environment contains a large volume of historical data that are both atomic and summarized. Because of the architectural complexity, high implementation cost, and uncertain return on investment, it has been a controversial concept and has sometimes encountered managerial opposition [23]. Despite early skepticism, DWG is spreading through enterprises, as evidenced by a report that 85–90% of the Fortune 500 companies have either adopted or plan to adopt it [13].

Various motives for deploying DWG have been discussed. Above all, industry-wide emergence of stiff competition forces organizations to adopt such measures to improve business competency. Corporate success increasingly depends on the mobilization of business intelligence. Increasing deregulation, globalization, and partnering are major driving forces of DWG in the telecommunications industry [12]. Growing popularity of virtual processes in the form of distributive computing, telework, electronic channel management, and virtual corporations is further fueling the need for the integration of information platforms.

Because DWG is not a product but a process that enables a single view of a business [9], its adoption inevitably entails or results in appropriate re-engineering of business processes. The key component is a ‘‘single, complete, and consistent store of data obtained from a variety of sources and made available to end-users in a way they can understand and use in a business context [6]’’. DWs and DMs differ from operational databases by containing more subject-oriented, integrated, time-variant, non-volatile, stabilized, and ad hoc-oriented data for decision aid [14]. A DM in general is a subset (i.e. a subject area) of associated DW. The former contains granular (or atomic) and/or summarized data that are necessary for a particular business application. Despite the increasing value of DWG, there has been little research on its planning and implementation from a holistic perspective. This case study is intended to investigate the project management approach taken at a large enterprise for a pilot DWG project.

## 2. Data warehousing benefits

The company studied provides individual health and accident insurance services; it has more than 6 million customers and over US\$ 80 billion of life insurance in force. The company developed a longterm plan to invest US\$ 100 million in four phases to improve IT infrastructure including DWG. DWG was expected to benefit the company enormously.

First of all, integration of heterogeneous operational data sources was becoming necessary to supply reliable data for decision support activities. These data sources had evolved independently, which resulted in much data duplication and inconsistency. The company had created operational data stores (ODS)<sup>1</sup> that combined data from transactional systems. Corporate ODS, such as the financial system, had a broad scope that could be accessed across the company; whereas, departmental ODS, such as the client management system, was created for departmental use. They used DWG technology (i.e. star schema) to provide an integrated view of data for operational purposes. They assisted day-to-day business processes, but were not intended for decision support.

Another important reason for conducting DWG at the company was to minimize procedural duplication and deliver information in a more consistent manner. The company’s business units were organized into three different customer levels: individual, group and corporate. However, information requirements from the individual and the group customer business units overlapped. In the traditional non-integrated database environment, therefore, duplicative efforts were difficult to avoid when retrieving the same piece of information. In fact, top management thought that substantial reduction of process overlap alone was enough justification for the multimillion dollar effort. Another potential benefitwasthatusingasingledatasourcecouldfacilitate business process re-engineering at the company [23].

Besides, effective service data management and data delivery process could be achieved by expanding mere departmental and stovepipe knowledge into cross-functional and integrative business intelligence. This could enable the company to better compete by learning from the past, analyzing current situations, and predicting the future [4].

## 3. Research method

The emphasis of this case was on describing the ‘‘what and how’’ aspects of project management [24] taken by the IT staff for the pilot DWG. The mission was completed after 6 months and, during the period, a weekly meeting was held for project planning, monitoring, and management. The author attended each session as an observer with limited responsibility. This experience, therefore, constituted a single case with multiple data sources including open-ended interviews, internal documents, e-mail logs of meeting summaries, and observations.

## 4. Project evaluation: risk assessment

Potential risks of the pilot project were identified and evaluated before its initiation. Risks such as project size and structure, skills of system analysts, and familiarity with technology can negatively impact the outcome of a project [16]. Many system development efforts have ended in failure due to the lack of readiness and incomplete risk management [18]. The chance of failure in initial stage of DWG is reported as high as 50% [23] and, accordingly, systematic identification of innate risks and their effective mitigation are crucial for successful project management.

Risk management becomes systematic when risk factors are determined based on a certain taxonomy scheme [2]. The project team initially identified 59 potential threats and classified them under the categories of external dependencies, organization, planning, business case, and technology-related. Technological risks were again divided into those of environmental, project-related, and operational. The intensity of each risk, then, was assessed based on pre-determined scales (see Table 1 for samples).

Overall, the weighting indicated moderate risks in planning, organizational, and technological aspects.

The assessment revealed uncertainties in many areas of project planning, change control, user-expectation management, scope management, and communication planning.

As for the external dependency-related risks, overlapping scope with existing projects was considered as a main risk factor because complexity of DWG demanded dedicated human resources. The IS department was directly and indirectly involved in several activities, including a financial DM, individual ODS projects, and a comprehensive Y2K project. This overlap could incur problems in resource allocation, end-user support, and system redundancy and leverage.

Organizational risks were regarded relatively weak, because top management was highly supportive of the effort. However, lack of clearly defined key users of the new system could be a threat, as their feedback was critical to a successful DWG endeavor. Also, it was determined that anticipated benefits of DWG might be difficult to attain unless necessary organizational and user changes occurred. The change management could pose a significant challenge to the project because the resistance to new organizational changes has been well documented by existing literature [5].

<table><tr><td colspan="3">Table 1Risk factors identifieda</td></tr><tr><td>Risk categories</td><td>Risk factors</td><td>Scale</td></tr><tr><td rowspan="2">External dependency</td><td>Overlapping scope with other existing projects</td><td>Y=3, N=0</td></tr><tr><td>Plan requires extensive recruitment of resources</td><td>Y=2, N=0</td></tr><tr><td rowspan="4">Organizational risks</td><td>Number of user areas/decision-makers</td><td></td></tr><tr><td>Key users of data warehousing unidentified</td><td>Y=5, N=0</td></tr><tr><td>Organizational changes required</td><td>Y=2, N=0</td></tr><tr><td>Level of changes required to user procedures</td><td>High = 3, low = 1</td></tr><tr><td rowspan="3">Planning risks</td><td>Critical implementation date was determined</td><td>Y=5, N=0</td></tr><tr><td>Lack of formal control procedures for systems planning</td><td>Y=5, N=0</td></tr><tr><td>Planned resources available</td><td>Y=0, N=5</td></tr><tr><td>Business case risks</td><td>Data warehousing is fundamental to IS strategy</td><td>Y=5, N=0</td></tr><tr><td rowspan="12">Technological risks</td><td>Environmental</td><td></td></tr><tr><td>New/unfamiliar technology</td><td>Y=5, N=0</td></tr><tr><td>Availability of development method/standards</td><td>Y=0, N=2</td></tr><tr><td>Project</td><td></td></tr><tr><td>Complexity of functions</td><td>Low = 0, moderate = 2, high = 5</td></tr><tr><td>Complexity of database</td><td>Low = 0, moderate = 2, high = 5</td></tr><tr><td>Shared databases with undefined applications</td><td>Y=3, N=0</td></tr><tr><td>Number of physical systems interfaces</td><td>0-2:2, &gt;2:3</td></tr><tr><td>Package solutions are unavailable</td><td>Y=0, N=3</td></tr><tr><td>Multilevel hardware implementation required</td><td>Y=2, N=0</td></tr><tr><td>Operational</td><td></td></tr><tr><td>The system should handle high-volume throughput</td><td>Y=3, N=0</td></tr></table>

Technological risk was estimated higher than planning and organizational risks because of the unfamiliarity with involved technologies and because of the need for many physical system interfaces among DWG components. Lack of definition for user applications added to IT uncertainties. Finally, the lack of packaged solutions and expected high-volume throughput for the system were considered as additional IT risks.

In the meantime, the project team had a close look at ‘‘project IS experience’’ and the ‘‘level of confidence’’, since these factors become an indicator for the company’s ability to cope with DWG endeavor. Given the size of 1000 IT staff and their extensive technical experience, it was decided that the level of IS experience and skill confidence did not constitute a significant threat.

In the business case, the main risk was that DWG was fundamental to the company’s long-term business strategy. The project’s failure, therefore, could considerably disrupt the company’s staged IT plans and subsequently affect business operations. Once the project team identified main risk factors, attempts were made to minimize them by introducing mitigation measures.

## 5. Project initiation

## 5.1. Staffing

Individuals of different technical and non-technical backgrounds were assigned to the pilot project team on either a full or part-time basis. Also, managers from both IT and business departments were included to coordinate the effort and provide inputs to the project team. Each participant belonged to one or more of the five entities defined for the project: planning board, project board, project team, key stakeholders and key resources (see Fig. 1). The staffing was based on the internal guidelines of the company for IS projects.

The planning board was responsible for the highlevel effort and its strategic alignment with business processes. It was composed of an End-user Computing Steering Committee (ECSC), a planning manager, and the chief information officer (CIO) as its chair. ECSC provided related feedbacks on DWG from a businessuser perspective.

The project board was responsible for overall practical planning, coordination, and evaluation of the project, with close cooperation from business customers in functional departments. Business customers were responsible for the validation of area data models and follow-up on modeling issues specific to business requirements. The board consisted of a planning manager as the project sponsor and liaison between the boards, a technical representative, and three representatives from customer departments. Since business units of the company were organized according to three customer levels (individual, group, and corporate), one representative from each customer level participated in the project board.

![](/api/attachments/BQ4KZVPV/fulltext/images/4a8d1865e50676f08ab8db910b7f1ebc727df030526c60bc937f2a47c52af7ff.jpg)  
Fig. 1. Project organization.

According to the internal guidelines, key stakeholders should be people whose departments will be affected by the implementation of a new IS. In this project, however, because of the crucial importance of stakeholders’ role, they were directly involved in the planning and project boards.

The project team included members of the ‘‘distributed computing support’’ and the ‘‘data and database services’’ groups from the IT division. The distributed computing support team was created to lead the pilot effort and consisted of five staff members that included a project manager, technical coordinators, and application programmers. Its central responsibility was to coordinate and facilitate the planning and engineering of ‘Compliance Monitoring’ DM and the design of DW logical models. More specifically, the responsibilities included identifying key participants, defining scope and objectives of sessions, scheduling (meetings, participants, equipment and other resources) and providing an overview of DWG. The team developed conceptual models of subject areas and made core entity definitions. It coordinated for the resolution of data model issues and ensured that logical and physical modeling met DM/DW requirements. The team was also responsible for documenting methods and guidelines of DWG for subsequent projects. The data and database services personnel were mainly responsible for assisting database analysis and for developing database logical models by capturing entities, relationships, attributes, and keys associated with the subject areas. They also facilitated training sessions to educate project participants in terms of data modeling concepts, terms and techniques.

The key resources offered support roles in the field of business information, technical training, and information repository. Individuals involved in information repository (or library management) provided assistance in locating data definitions from available data repository and entering data definitions into the repository.

## 5.2. Scope management

A DWG venture differs from conventional IS projects in several aspects. Bischoff and Alexander [3] indicated that the complexity resulting from the rapid growth of database volume makes it different from many traditional projects. Gathering articulated user requirements is more difficult, because the type of information needed for decision support is hard to articulate in priori [19]. DWG tools are also more complicated than those of traditional systems [7]. Besides, because of the decision support orientation, system-related issues of DWG become more sensitive to internal politics than those of transactional systems.

The planned DWG was comprised of a shared DW and departmental DMs. Because of the complexity and the lack of project experience in DWG, the shared DW was to be built incrementally in parallel with the pilot DM that would upgrade the existing Compliance Monitoring system. The Compliance Monitoring application was judged an excellent choice for the pilot project for several reasons.

First, the existing Compliance Monitoring system contained some reusable processes such as data extraction. Such reusability of software components could significantly reduce the risk resulting from the unexpected inflation of project scope. This may be especially true for the pilot project run by IT staff with limited prior experience in DWG. Second, existing ODS for Compliance Monitoring application could become the single data source for the planned DM. Data staging is known to consume about 80% of DWG efforts due to its enormous complexity. Accordingly, having a single data import source could significantly help the project scope under control and curtail the risk of project delay and failure [15]. Third, because the IT staff and business customers had worked with the existing Compliance Monitoring system, gathering additional requirements was less complicated. In summary, the pilot project was to achieve following goals:

1. streamline existing data transformation processes and improve reporting and analysis capacity for Compliance Monitoring application;

2. set directions leading to the development of the shared DW and build the initial increment of logical data models for selected subject areas;

3. compile methods, principles, and procedures for future projects and establish consistency in the selection of platforms and tools;

4. establish a standard policy for DWG design, implementation, and support.

## 6. Project execution

## 6.1. Development of the target architecture

The DWG architecture is a formal specification of data structure, communication among components, processing, and presentation of DWG environment [11]. General high-level DWG architecture of the company was based on five main functional entities: operational or transactional data sources, data staging areas, a shared DW, DMs, and end-user applications (see Fig. 2). Legacy databases, purchased data, external data, and data from the financial ODS comprised main operational data sources for the shared DW and DMs. The data staging area was the intermediary place where decision support data were extracted from data sources, cleansed, transformed, and moved to loading places. Two staging processes, one between the ODS and the DW and the other between the DW and DMs, were defined. The shared DW was planned to contain data from 12 subject areas, which reflected key informational dimensions of the company including field (i.e. insurance agents and brokers), reference (i.e. guidelines and policies), organization (i.e. teams and business units), and provider (i.e. doctors and hospitals).

Logical data modeling of subject areas was conducted concurrently with the development of Compliance Monitoring DM. Compliance Monitoring application was to include data pertaining to subject areas of client, field, policy, product, geography and reference. Data structure of the DM was to be elevated to a higher level to quickly satisfy end-users’ pressing information needs. Kimball et al. [15] called it a business process DM. The DWG architecture adopted dependent DM paradigm [9], in which operational data sources mostly provide data for the shared DW, and the shared DW in turn becomes the data source for application-specific DMs which offer more summarized and pre-arranged data for end-users [1].

![](/api/attachments/BQ4KZVPV/fulltext/images/7654e7d31b2d12f8fbfded3afe7daa8364de8f47c93b576daaf8395dc02ab9c9.jpg)  
User Applications  
Fig. 2. Data warehousing architecture.

## 6.2. Implementation strategy

DWG can take different planning and implementation paths: top–down, bottom–up, or parallel (hybrid) mode. With top–down, a full-scale shared DW is constructed prior to the introduction of smaller DMs. This approach tacitly assumes that a shared DW will contain all attributes needed for business applications and a DM would comprise a subset (typically more summarized) of the DW for a particular business application.

This monolithic method can entail serious risks, though. Above all, there is no such concept as the final DW because of its dynamic and evolutionary nature. The system and the data structure have to be continuously modified and updated to meet the changing information demand at an organization [22]. Also, a full-scale DW project demands a large-scale resource commitment, planning efforts, and development time. Studies indicate that the delay of system delivery caused by various risk factors constitutes a main reason for DWG failure [11].

Besides, the all-at-once approach requires complicated and time-consuming enterprise modeling [25]. A detailed corporate data model captures the holistic view of business processes and source data. This facilitates the development of logical and physical DWG models and therefore can speed up overall project completion [17]. Although many companies possess enterprise-level data models, the studied firm did not own them because of the organizational culture that valued each focus group’s (or business unit’s) activities. Management’s attitude had naturally been ‘‘if it works, do not change it’’.

In the bottom–up approach, subject field DMs are independently designed and constructed and they become the foundation of a full-scale DW. This method is based on the tacit assumption that the removal of data redundancies among DMs and their integration will be adequate to produce an enterprise

DW. It inherits a risk, however, that makes the relative role of the DW and DM systems vague [8]. The DMcentric paradigm may also constrain system flexibility and responsiveness necessary for dynamic decision support at an enterprise [1]. Besides, possible proliferation and uncontrolled growth of DMs without regard to cross-functional or cross-departmental information requirements can severely undermine benefits of ideal DWG [8].

The company decided that the Compliance Monitoring DM be implemented along with the incremental construction of logical data models for selected DW subject areas (see Fig. 3). The hybrid approach was justified for several reasons. First, the DM could be implemented quickly and still be highly beneficial to end-users who could not wait for the completion of the shared DW. For many people, departmental or application-specific DMs offer the level of data granularity sufficient to produce reports and to conduct necessary data analysis. In fact, a DW with high data granularity would be more suitable for power applications such as data mining and cross-functional processing. The hybrid approach, therefore, allows rapid deployment of a decision support system for a particular business application that needs immediate attention.

Second, this approach allows DM activities to have a certain degree of independence from those of a DW. Also, DM project experience could render valuable insights concerning the incremental implementation of a DW. Given the lack of DWG experience at the company, the DM pilot project could become a learning opportunity for subsequent DWG projects. Besides, the availability of a single data source for the pilot DM, the familiarity with the existing Compliance Monitoring system, and the reusability of existing processes significantly reduced project risks and simplified requirement analysis and logical modeling, further justifying the hybrid approach.

The parallel implementation does not mean that the project team took a DM-centric strategy for data management. The DM-centric strategy, where subject DMs dominate data management and knowledge extraction, may offer short-term benefits including faster and cheaper processing and higher manageability. However, it is not as integrated, atomic, and cross-functional as a DW-centric environment, which can decrease flexibility and effectiveness in cross-functional queries, return on investment, and user information satisfaction [1].

![](/api/attachments/BQ4KZVPV/fulltext/images/a8f2837741e2384b75babac651844e490a8ee4e3766926faedb053ed512b2d29.jpg)  
Fig. 3. Hybrid data warehousing implementation.

The company chose a decision support environment where the shared DW and subject DMs are complementary, where the DW was more focused on extracting and loading data from operational sources, and where DMs’ emphasis was on the delivery of application-specific information through OLAP and reporting tools. Meanwhile, users (especially power users) still needed to access the shared DW because a DM had limitations in producing information of high granularity and in enabling cross-referencing among subject areas. Fig. 3 describes the procedural avenue adopted for the parallel implementation of pilot DM and DW data modeling. The data model of the shared DW would be defined separately for each subject area. Application requirements and DMs’ data structure were to become the reference source for the DW modeling.

## 6.3. Project support processes

Many businesses do not own adequate domain knowledge and project management skills necessary for DWG. In this case, availability of methodological guidance can significantly reduce project-related uncertainties and risk of failure [20]. In fact, one of the roadblocks for the pilot effort was the absence of such support processes that could methodically guide IT managers and system development staff during the project life cycle. The project team, therefore, took advantage of the pilot project as an opportunity to develop guidances for subsequent endeavors.

First, critical performance areas were identified to emphasize key success points of DWG. They were classified under eight discrete categories: data integrity, information delivery, metadata management, data integration, DW support, DM support, data/database services,andprocess/toolssupport.Thefirstfourcategories are associated with data and information management and the subsequent four categories defined major support, service, and development activities of DWG.

## 6.3.1. Data/knowledge management areas

1. Data integrity: data/rules definition, data transformation, source/target mapping, data cleansing, data validation, data security, and data management.

2. Data integration: change management, conflict management, and model integration.

3. Information delivery: data acquisition, transfer and load, and report development and delivery.

4. Metadata management: model development, metadata inventory, query management, report management, rules management, and report monitoring.

## 6.3.2. Project support areas

1. DW support: DW direction/architecture, subject area development, shared application development, warehouse administration, warehouse configuration, and warehouse security.

2. DM support: requirements definition, star schema modeling, source identification and transformation, multidimensional database development support, OLAP application development support, and DM mentoring.

3. Data and database services: entity relationship modeling, database development, database tuning and performance, and multidimensional database.

4. Process/tools support: repository and OLAP tools.

The project team also defined a high-level support procedure to render consistency in systems construction, testing, and production support (see Fig. 4). The definition of support procedure focused on four dimensions: logical design; database (relational and multidimensional) development; analysis and reporting applications deployment; and extraction, transformation and loading (ETL) tools development. Data transformation by ETL tools undertakes such tasks as cleansing, reconciliation, enhancement, summarization, and aggregation of operational or transactional data. The dimensions, except for the logical design, were then further divided into the stages of ‘‘construction and unit test support’’, ‘‘system test support’’, ‘‘customer acceptance test support’’, and ‘‘production support’’.

<table><tr><td>Dimensions</td><td colspan="4">Support category</td></tr><tr><td>Data mart design support</td><td colspan="4">Logical design</td></tr><tr><td>Relational database</td><td rowspan="4">Construction and unit test</td><td rowspan="4">System test</td><td rowspan="4">Customer acceptance test</td><td rowspan="4">Production</td></tr><tr><td>Multi-dimensional database</td></tr><tr><td>Analysis &amp; reporting tools</td></tr><tr><td>Extraction, transformation, and loading tools</td></tr></table>

Fig. 4. High-level data warehousing support processes.

More detailed support activities were then defined in each stage. For instance, for the ‘‘construction and unit test support’’ of a multidimensional database, support activities were composed of (1) creating multidimensional database applications on a test server, (2) setting up and maintaining development and testing users, (3) setting up and maintaining development and testing user groups, and (4) assigning access privileges.

## 7. Project closure and future plans

On the completion of the pilot project, the team achieved several goals. It established a plan that integrated business information strategy and technical directions of DWG. It compiled procedural and methodical directions to support ensuing DWG projects. Compliance Monitoring DM was deployed on an AIX platform and an OLAP tool was deployed to support the application. Also, logical data models for the selected subject fields of the corporate DW were developed.

From the experience of the pilot project, they emphasized that initiation of ensuing projects be based on the rigorous validation of existing organizational, technical, data, and application architectures (see Fig. 5). As for the organizational architecture, suggestion was made to review the general information management strategy in terms of data management, roles and responsibilities, information requirements from business areas, and necessary organizational changes.

As for the data and application architectures, it was recommended that increments of data and applications be made based on the review of existing data structures and application processes and guidelines, the determination of data and application requirements, and the prioritization of requirements.

Suggested evaluation of the technical architecture focused on upgrading OLAP applications, managing metadata, and deploying ETL tools. The OLAP upgrade was regarded important, as the new version was to support web-based processing and multidimensional databases. Better management of metadata was thought crucial in future projects. Unreliability of legacy metadata and the lack of metadata management strategy created much difficulty in undertaking the pilot project in a consistent manner. Besides, it was pointed out that complete dependence on manual programming for data staging without the support of automated ETL tools had to be re-evaluated since the staging was the most demanding and timeconsuming process.

![](/api/attachments/BQ4KZVPV/fulltext/images/e0cc3122756499f4a05372a08650b486ea8740cdf50c40188745655950d7f8c0.jpg)  
Fig. 5. Iterative validation of data (a) and application (b) architectures.

## 8. Lessons of the project management

Main lessons learned during the pilot experience were gathered from interviews with the project manager. The first lesson emphasized the vital role of process involvement by business units and prospective end-users. Active involvement from business customers was viable only when top management was behind the project. The lack of serious commitment from some business sponsors appointed in the planning and project boards created a roadblock in carrying out the pilot project. The partnership was crucial for adequate requirements definition, the business justification of the project, user buy-in for the final product, the management of user expectations, and the determination of system benefits in terms of return on investment.

Manageable project scope bears less developmental risk because DWG demands large-scale mobilization of organizational resources (both tangibles and intangibles) [20]. Even a single DM project can be too big in its scope when there is limited DWG experience [16]. In this case, starting it at a smaller scale reduces the risk of failure and minimizes the potential impact failure will have on future efforts. Meanwhile, the project should not be so trivial that it loses organizational attention and commitment. In addition, given the dynamic nature of decision support needs, an incremental approach will make the system more current.

Using packaged tools for data staging is crucial. About 80% of DWG effort is spent on data staging that includes data extraction (or migration), cleansing, transformation, loading, and reconciliation [14]. This project was not an exception. Application developers manually programmed data staging processes instead of using packaged tools. However, poor metadata documentation and the lack of integrity in the source data in the form of missing values, overlapping values, inconsistently formatted values, and illegal values created tremendous overhead during data staging. Resolving complicated data conversions with in-house developed programs delayed the project about a month longer than originally planned.

Marketing of the new system throughout the project cycle was necessary to attract cooperation and commitment from business customers and to facilitate adoption by target users. Since the pilot project was intended to improve informational capacity of existing Compliance Monitoring application rather than to create a brand new system from scratch, marketing efforts should have been placed on differentiating the new system from the old one. Unless target users could see tangible benefits from the new system, they had little justification to switch. Some prospective users were reluctant to replace the legacy ad hoc query tool with the new OLAP tool because of the learning curve. To facilitate the migration, system designers and developers should take a user-centric approach in selling the DWG concept [10].

Metadata-centric system design and implementation based on conformed (overlapping) dimensions and facts prevent DMs from becoming a stovepipe system, which does not allow interoperability with others [15]. As certain data are shared among several subject areas, overlapping dimensions and their metadata should be pre-established and consistently used during the DWG endeavor. This was not effectively done in the pilot project partially due to limited experience and partially due to the lack of adequate metadata tools. Metadata tool sets should be able to enforce the consistency and integrity between logical and physical metadata, offer active documentation of transformation rules, and enable automated generation of data definition language.

## 9. Concluding remarks

As all indicators show, DWG is becoming a strategic nerve center at an enterprise. As it transforms and redefines the way business gets done, more corporations will mobilize the system to achieve operational efficiency and competitive advantages. Traditional use of databases for localized productivity enhancement no longer constitutes a distinctive strategic weapon. Firms need to redesign the way business is conducted via an integrated computing paradigm. New applications that take advantage of DWG capacity are continuously emerging. Enterprise resource planning, advanced intelligence networks in telecommunications, customer relationship management and profiling, and organizational knowledge management are among them. Although their strategic focus is heterogeneous in nature, the true potential of these applications cannot be realized until a unified DWG architecture is in place to support them. Its strategic importance as a cornerstone for enterprise information management cannot be overemphasized. The studied company developed a four-phase IT strategy to boost business competition, and DWG was given the highest priority. On this premise, the company pursued the pilot project. This case investigated important project management issues of DWG and methodical approaches adopted by the IT staff in undertaking the project.

## Acknowledgements

I would like to show my gratitude to Professor Sibley for his invaluable advice that made this paper possible.

## References

[1] R. Armstrong, The fallacy of data mart centric strategies, White Paper, NCR Corporation, 1996.

[2] R.L. Baskerville, J. Stage, Controlling prototype development through risk analysis, MIS Quarterly, 1996, pp. 481–554.

[3] J. Bischoff, T. Alexander, Developing a data warehouse, Datamation 43 (6), 1997, pp. 21.

[4] B.H. Boar, Understanding data warehousing strategically, in: R. Barquin, H. Edelstein (Eds.), Building, Using, and Managing the Data Warehouse, Prentice-Hall, Englewood Cliffs, NJ, 1997.

[5] F. Damanpour, Organizational innovation: a meta-analysis of effect of determinants and moderators, Acad. Manage. J. 34 (3), 1991, pp. 355–590.

[6] B. Devlin, Data Warehouse: From Architecture to Implementation, Addison-Wesley, Reading, MA, 1997.

[7] P. Dorsey, Data warehouses, ad hoc query tools and other ways to destroy your company, White Paper, Dulcian Inc., 1996. <http://www.dulcian.com/destroy.htm>.

[8] J.M. Firestone, Data warehouses and data marts: a dynamic view, White Paper, Executive Information Systems Inc. (27 March 1997). <http://www.softwarejobs.com/firestone.html> (26 May 1999).

[9] S.R. Gardner, Building the data warehouses, Commun. ACM 41 (9), 1998, pp. 52–60.

[10] K. Glassey, Seducing the end-user, Commun. ACM 41 (9), 1998, pp. 62–69.

[11] P. Gray, H. Watson, Decision Support in the Data Warehouse, Prentice-Hall, Englewood Cliffs, NJ, 1998.

[12] L. Handen, P. Boyle, Data warehousing: managing knowl edge, Telecommunications 32 (1), 1998, pp. 61–68.

[13] Hyperion Co. The role of the OLAP server in a data warehousing solution, White Paper, 1999. <http://www.hyperion.com/whitepapers.cfm>.

[14] W.H. Inmon, Building the Data Warehouse, 2nd Edition, Wiley, New York, 1996.

[15] R. Kimball, L. Reeves, M. Ross, W. Thornthwaite, The Data Warehouse: Lifecycle Toolkit, Wiley, New York, 1998.

[16] F.W. McFarlan, J.L. McKenny, Corporate Information Systems Management—The Issues Facing Senior Management, Irwin, Homewood, IL, 1983.

[17] D. Meyer, C. Cannon, Building a Better Data Warehouse, Prentice-Hall, Englewood Cliffs, NJ, 1998.

[18] A.H. Murtaza, A framework for developing enterprise data warehouses, Information Systems Management, 1998, pp. 21–26.

[19] K. Orr, Data warehouse technology, White Paper, The Ken Orr Institute, 1998.<http://www.kenorrinst.com/dwpaper.html> (26 May 1999).

[20] T. Saarinen, A. Vepsalainen, Managing the risks of information systems implementation, Eur. J. Inform. Syst. 2 (4), 1993, pp. 283–295.

[21] A. Sen, V.S. Jacob, Industrial-strength data warehousing, Commun. ACM 41 (9), 1998, pp. 28–31.

[22] A. Subramanian, L.D. Smith, A.C. Nelson, J.F. Campbell, D.A. Bird, Strategic planning for data warehousing, Inform. Manage. 33, 1997, pp. 99–113.

[23] H. Watson, B. Haley, Managerial considerations, Commun. ACM 41 (9), 1998, pp. 32–37.

[24] R.K. Yin, Case Study Research: Design and Methods, Sage, Beverley Hills, CA, 1989.

[25] G. Zagelow, Data warehousing—client/server for the rest of the decade, in: R. Barquin, H. Edelstein (Eds.), Building, Using, and Managing the Data Warehouse, Prentice-Hall, Englewood Cliffs, NJ, 1997.

Bongsik Shin is an assistant professor at the Department of Information and Decision Systems at San Diego State University. He earned a PhD from the University of Arizona. He has published in such journals as Communications of the ACM, IEEE Transactions on Systems, Man, and Cybernetics, IEEE Transaction on Engineering Management, Journal of Data Warehousing, Journal of Organizational Computing and Electronic Commerce, Journal of Systems Integration, and Journal of Database Management. His current research interests include data warehousing and data mining, telework, and e-commerce.
