---
otero_id: 19484
otero_key: "EZBJB4EG"
title: "Data warehouse governance: best practices at Blue Cross and Blue Shield of North Carolina"
authors: "Hugh J. Watson; Celia Fuller; Thilini Ariyachandra"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.06.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Data warehouse governance: best practices at Blue Cross and Blue Shield of North Carolina

Hugh J. Watson<sup>a,</sup>\*, Celia Fuller<sup>b</sup>, Thilini Ariyachandra<sup>a</sup>

<sup>a</sup> Department of Management Information Systems, Terry College of Business, University of Georgia, Athens, GA 30602, USA <sup>b</sup> Blue Cross and Blue Shield of North Carolina, Durham, NC, USA

Received 1 August 2002; accepted 1 June 2003 Available online 28 September 2003

## Abstract

Effective governance is a key to data warehousing success. An example of a company that has excelled in data warehouse governance is Blue Cross and Blue Shield of North Carolina (BCBSNC). The data warehouse has resulted in many organizational benefits, including providing ‘‘a single version of the truth,’’ better data analysis and time savings for users, reductions in head count, facilitation of the development of new applications, better data, and support for customer-focused business strategies. The structures and processes used by BCBSNC for data warehouse governance represent best practices for other companies to follow. For researchers, the experiences at BCBSNC support and add to the body of knowledge about IT governance, in general, and data warehousing governance, in particular. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Blue Cross and Blue Shield of North Carolina; Data warehouse; Data warehousing; Governance; Staffing; Decision support; Training; Benefits

## 1. Introduction

Data warehouses (and smaller scale data marts) have become the focal point for decision support in organizations today. They provide a repository of data that can be used to support queries, reporting, online analytical processing (OLAP), DSS/EIS, and data mining [11]. They are also integral components of strategic business initiatives such as customer relationship management (CRM), electronic commerce, and supply chain integration [9]. Data warehouses resolve a long-standing decision support problem— the need for accurate, clean, well-organized, and accessible data.

Data warehouses are high risk/high return endeavors [15,25]. They offer benefits such as cost savings from the consolidation of multiple, disparate decision support platforms; improvements in the quantity and quality of data used to support decision making; productivity improvements resulting from redesigned work and business processes; and significant organizational transformation enabled by data warehousing [23]. Data warehouses are challenging technical undertakings, however, because of the disparate source systems that must be accessed; new technology that must be selected, implemented, and learned; and the vast quantities of data that must be managed and made available to users [24]. There are also organizational issues that must be addressed, such as maintaining sponsorship, managing expectations, avoiding scope creep, and handling political issues [2,7,12]. For these reasons, data warehousing projects are often over budget and behind schedule, do not meet expectations, or fail completely [27].

Watson et al. [27] studied eight companies that had experienced a data warehousing failure. There were common reasons for failure across many of the companies—weak sponsorship and/or management support, insufficient funding, inadequate user involvement, and organizational politics. With few exceptions, the reasons for failure were organizational rather than technical. As with most IT projects, organizational issues are usually more daunting and critical to success than technical ones [1,7,29].

Effective data warehousing governance is required in order to successfully address both technical and organizational issues. Governance requires creating committees that have the authority and responsibility to carry out their assigned missions. The committees should have the appropriate composition (e.g., size), characteristics (e.g., experience), and structure (e.g., reporting and information flows), and use appropriate processes (e.g., frequency and length of meetings) [18]. When an enterprise data warehouse is built, multiple stakeholders should be involved in the organizational structures that are created and the processes that are followed.

The authors have personally seen the importance and interest in data warehousing governance in their work with The Data Warehousing Institute (TDWI), the leading organization for data warehousing professionals (www.dw-institute.com). Participants in TDWI’s conferences express great interest in data warehousing committee structures and the staffing of the data warehousing team. TDWI also includes data warehousing governance as one of the categories in its annual Best Practices competition, which recognizes the best data warehousing work around the world.

In the following sections, we discuss IT and data warehousing governance. This discussion provides the perspectives needed for understanding and appreciating the case study that is presented next, which describes the data warehousing initiative at Blue Cross and Blue Shield of North Carolina (BCBSNC). BCBSNC is a TDWI Best Practices winner in the data warehousing governance category. Their work can be used as a model by other companies that are seeking insights about how to best govern their data warehouse. It also provides researchers with another company that can be used to develop and validate the emerging conceptualizations and understandings about IT and data warehousing governance [31].

## 2. IT and data warehousing governance

Organizational investments in IT have become increasingly large as companies become more information intensive. It is imperative that these investments be used effectively and efficiently. To ensure this, organizations must put IT governance structures (e.g., committees) and processes in place [18].

Over the past two decades, the IS literature has discussed the IT governance activities that must be performed and who might best perform them, examined the various IT governance arrangements or forms that organizations can use, provided frameworks for understanding the various governance forms, and presented research findings on why organizations select particular governance forms [4,30,31].

The scope of IT governance activities ranges from strategic to operational. In many firms, IT is strategic to how, and how well, the firm competes in the marketplace. It is critical that there is alignment between the business and the IT strategies [13]. On the other hand, IT governance must also address operational issues, such as what end user data access tools to support and what data definitions to use. The scope of IT governance activities requires that there is broad participation in performing them. Multiple stakeholders (e.g., senior management, business unit managers, users, IT, and consultants) must work together in a coordinated manner [3].

A major focus of IS researchers is whether key ITrelated activities should be delegated to and governed by the business units or performed by a central (usually corporate) IS organization [4,19]. The key activities include developing and maintaining the IT infrastructure, deciding on the use of the technology (including systems development), and managing projects [5,8,20,23]. Researchers have identified three primary IT governance forms or modes—centralized, decentralized, or hybrid—for handling the key activities [23]. They differ in regard to whether central IS, divisional IS, or line management is responsible for performing them. With centralized IS, all key activities are performed by a central IS organization. With divisional IS, the activities are performed by the business units. With a hybrid mode, some activities are performed by central IS (e.g., maintaining the IT infrastructure) while others are performed by the business units (e.g., project management). The literature suggests that many large, divisionalized firms adopt a hybrid governance mode where central IT maintains the infrastructure and the business units plan, build, and use their own applications. Zmud et al. [31] refers to this as a ‘‘federal government role’’ for IS.

IS research has concluded that there is no ‘‘universal’’ governance mode that is best for all organizations [17,20,30]. The best governance solution for an organization depends on its organizational context. For example, Brown [4] has studied a multidivisional firm where a subset of key IT activities, including systems development, is decentralized in some business units, but not in others, and concluded that contextual variables (e.g., business unit autonomy, competitive strategy) can be used to predict the governance arrangements that are made.

Data warehousing governance is a subset of IT governance. It requires that appropriate organization structures and processes are in place, with coordinated inputs from all stakeholder groups. It must cover infrastructure, use, and project management [23]. It is different from IT governance in that it deals with a more limited domain—only those activities and issues related to data warehousing.

Data warehousing governance must address many, varied areas:

. Identifying business needs. There are many potential reasons for developing a data warehouse. The most overarching one is to improve the quality of information in an organization: make it more accurate, better integrated, and accessible from a single source [26]. There are often specific applications that are the drivers behind a data warehousing initiative, such as to support a CRM initiative [6].

. Achieving alignment with company goals. It is well understood that a system that supports business needs is more likely to be successful than one that provides less support [10]. For this reason, there needs to be alignment between warehouse and company goals. Maintaining alignment is an ongoing process. It is not unusual for the goals for a warehouse to become more strategic over time as management becomes more aware of the potential of the warehouse for supporting business strategy.

. Determining information requirements. Users’ information requirements drive what data are stored in the warehouse, the granularity of the data, how much historical data are maintained, and the data model that is used [14]. The greatest challenge is when the data warehouse is designed to support new, cross-organizational information needs. The needs must be identified and agreed upon, the source systems that best meet the needs must be selected, and the reports and queries (to the extent that is possible) must be identified.

. Setting priorities. A data warehouse should be developed in an evolutionary manner [15]. The initial version contains data for one or a few subject areas, and supports applications and users that access the initial data. Often with a 3-month cycle time, additional subject areas, users, and applications are brought on board. A data warehouse is never ‘‘completed.’’ As is frequently heard, ‘‘data warehousing is a journey, not a destination.’’

Priorities for implementing the various subject areas and applications must be set. It is common for multiple business units to want the initial or an early version of the data warehouse to meet their needs. High-level, cross-organizational committees are needed to set the priorities and develop the overall warehouse implementation plan. The committees must select criteria for establishing the priorities (e.g., strength of sponsorship, the readiness of source data, and business need) and then evaluate the implementation alternatives using the criteria.

. Establishing data definitions and models. Two design issues that must be addressed are: (1) what data definitions to use and (2) what data model will allow users to effectively and efficiently run queries across subject areas. Organizations have hundreds of terms (e.g., customer, sale) that have slightly different meanings (such as when a sale is recognized) that vary with the business units. This is a natural consequence of business units defining terms in ways that best serve their purposes. For the warehouse, it is important to agree on data definitions, make sure the definitions are understood, and utilize source systems that are consistent with the definitions.

Warehouses provide users with a dimensional view of the data (e.g., product, place, time), and each of the dimensions has measures (e.g., the time dimension may have hour, day, and month as measures). To query across subject areas, it is necessary for the data model to have consistent dimensions and measures. This is referred to as creating ‘‘conformed dimensions’’ [16]. It is necessary for users to identify and agree upon the dimensions and measures that will be used in the warehouse’s data model.

. Maintaining data quality. Ensuring that the data warehouse contains high quality data is an ongoing concern [22]. Most organizations find that the data in their source systems is even worse than imagined. The combined efforts of the data warehousing staff and business units are required to assess the quality of the data and to put data cleansing processes in place. Initially, the data in the source systems most likely must be accepted as is, with the data being cleansed before it is loaded into the warehouse. In the longer term, there should be initiatives to improve the quality of the data in the source systems, so that there is less downstream cleansing.

Even when the warehouse is operational, data quality issues will continue to arise and require attention. For example, new subject areas will be added with all of the attendant problems of adding new source systems to the extraction, transformation, and loading processes. Changes will be made to existing source systems and these changes have rippling effects on the data warehouse and must be accommodated.

There is only limited research on data warehousing governance [23,28]. However, the existing research is consistent with IT governance research in that it considers the activities that must be performed, who should perform the activities, what the governance alternatives are, frameworks for understanding governance, and what governance alternatives are or should be used. For example, Winter and Meyer [28] discuss the activities that data warehousing governance must address, develop a concept of data ownership that is related to data warehousing governance, and illustrate the application of this concept for data warehousing governance in a large Swiss bank. Based on six case studies, Sujitparapitaya et al. [23] show how the data warehouse architecture used (e.g., enterprise data warehouse, divisional data marts) impacts how companies practice data warehousing governance. For example, companies with enterprise data warehouses are more likely to have centralized IT authority than firms with divisional data marts. This finding shows that data warehousing architecture is a contextual variable for predicting data warehousing governance.

This discussion of IT and data warehousing governance allows the case study of Blue Cross and Blue Shield of North Carolina to be put in perspective. The case discusses the development of BCBSNC’s data warehouse and the governance committees and processes that are used. The development activities (e.g., determining information requirements) are common to data warehousing projects, but how they were performed (e.g., the opportunity analysis) is probably unique to BCBSNC. Likewise, the governance committees and processes used at BCBSNC are consistent with high-level ‘‘conventional wisdom’’ (e.g., include multiple stakeholders working together in a coordinated manner), but the details of BCBSNC’s practices are noteworthy. As mentioned before, BCBSNC has been recognized by TDWI for best practices in data warehousing governance. Some of the most interesting insights learned at BCBSNC are provided in Section 3.10. Sujitparapitaya et al. [23] have shown that data warehousing architecture is a contextual variable that affects data warehousing governance. BCBSNC implemented an enterprise data warehouse, and the governance practices used are most appropriate for that kind of architecture.

## 3. About Blue Cross and Blue Shield of North Carolina

## 3.1. Company background

Blue Cross and Blue Shield of North Carolina (www.bcbsnc.com), based in Chapel Hill, NC, is North Carolina’s largest health insurer, serving 2.8 million members, including 470,000 served on behalf of other Blue plans. BCBSNC’s HMO and POS products have earned excellent accreditation from the National Committee for Quality Assurance (NCQA), an independent, not-for-profit organization dedicated to measuring the quality of America’s health care. Blue Cross and Blue Shield of North Carolina is an independent licensee of the Blue Cross and Blue Shield Association.

As an organization in the highly competitive health care industry, BCBSNC views being customer-focused as an important element of its strategy for organizational success. The company strives to provide its members effective services such as high quality health care information in order to improve their health.

## 3.2. The business drivers for the CDW

Fundamental deficiencies in the information access and reporting capabilities within BCBSNC were the key drivers that led to the creation of the corporate data warehouse (CDW) in 1997. Prior to its implementation, organizational personnel, including top management, had a general lack of confidence in data quality and information reporting within the organization. Insufficient data definitions, redundancy in data, multiple data extract and transformation processes, lack of accountability, absence of data documentation, and poor communications on data usage were some of the contributing factors underlying the lack of credibility of existing data management systems.

The ever-changing health care regulatory environment further supported the need for consistent and effective data management practices across the organization. In order to ensure that the organization’s practices were in compliance with health insurance regulations such as Health Insurance Portability and Accountability Act (HIPAA), an integrated single repository of corporate data became essential. The warehouse would be the focal point for ensuring that BCBSNC was compliant with HIPAA’s (1) transaction processing, (2) security, (3) code sets, and (4) identifier requirements. Any data included in the warehouse would satisfy HIPAA requirements [21].

In addition, areas within the organization requiring strong decision support capabilities were experiencing great difficulty in accessing and manipulating data to meet their daily needs.

As a result, an information management oversight team, with representatives from the business units and IS, was established to investigate these issues and develop a set of recommendations that addressed them. The final recommendations included establishing a corporate data glossary, working on source data quality initiatives, and creating a corporate data warehouse.

The original mission of the warehouse was to establish a system of record for decision support in the organization, but this mission has evolved over time to be better aligned with the company’s strategic focus and direction. The current mission is to be an ‘‘engine that powers a customer-focused, informationdriven company.’’

## 3.3. Getting started

The CDW project began with the formation of a cross-functional team, composed of members of IS and representatives from the business areas. This team conducted an extensive opportunity analysis of four primary decision support areas: (1) actuarial and underwriting, (2) market analysis, (3) financial analysis, and (4) health services analysis. The opportunity analysis revealed the following business requirements for the data warehouse: (1) establish consistent, timely, and easily accessible data; (2) address data quality issues; (3) develop and document common data definitions and business rules for using data; (4) provide ease of use for nontechnical users; and (5) support sophisticated analytical processes.

The cross-functional team identified the business areas that required decision support capabilities and prioritized the timing of the implementation of eight key subject areas. Fig. 1 shows a sample of the two dozen information opportunities that were discovered (the rows), their priority level (reflected by the shading of the cells), and the eight subject areas (the columns) that were identified to support the opportunities. Joint application development (JAD) sessions conducted during this phase led to the creation of common data definitions with crossfunctional consensus.

In the months that followed, a series of workshops with operational and decision support areas were held to help build a logical data model around the subject areas. These long, arduous logical modeling sessions enabled the team to clearly understand the business processes, information processes, and data needs. The result was a comprehensive data model that has enabled the team to design, implement, and make continuous improvements to the CDW. Fig. 2 presents a sample of the high-level logical data model for the CDW.

![](/api/attachments/EZBJB4EG/fulltext/images/b8063646aee886b0826ac4f1f5c9e352e1c62322cf3fe92d615667c7e092bcf7.jpg)  
Fig. 1. Opportunity analysis.

## 3.4. The current data warehouse

Since 1997, the data warehousing initiative has evolved and delivered data and functionality in phases as identified and prioritized by the business areas. The current CDW supports a broad set of applications for more than 200 users in the business areas of sales and marketing, financial services, corporate analysis and risk assessment, corporate audit, and health quality improvement. It draws data from 12 source systems, including 5 legacy claims processing systems, 6 external and third-party data sources, and a new managed care claims processing system introduced by the company. Fig. 3 presents the detail tables in the eight subject areas identified in the logical model as well as five summary tables and two clinical constructs. Clinical constructs are complex tables for inpatient and outpatient cases and the associated professional health services. For example, a patient case might include the initial visit to a physician, the tests run at a diagnostic center, and the follow up appointment with the physician to review the test results and develop a treatment plan.

![](/api/attachments/EZBJB4EG/fulltext/images/ea96621e42f8496ea5472d566331c12dc3700ad3b6d28c96ad01c8c3814f8504.jpg)  
Fig. 2. The logical data model.

At present, the CDW environment has more than 200 tables, 1500 data elements, and 2.5 terabytes of data storage. The hardware architecture is massively parallel processing (MPP) with 17 nodes each with 4 processors for a total of 68 processors to support the high processing capabilities required by the CDW’s production, test, and development environments.

![](/api/attachments/EZBJB4EG/fulltext/images/758a68564e150ab96ffaa87fac8d63cb4228248fd80acf7f8bb86767fe8559bb.jpg)  
Fig. 3. The corporate data warehouse.

## 3.5. Decision support and the data warehouse

Decision support was common at BCBSNC prior to the development of the warehouse. The applications were ‘‘stovepipe’’ in nature, however, with the business units operating independently. They used their own processes for accessing data from operational systems; employed their own data definitions, business rules, and analytical processes; and presented and interpreted output in ways that best served their unit’s purposes. Not surprisingly, the different units had inconsistencies in their analyses (i.e., ‘‘dueling spreadsheets’’), and there was limited ability to do cross-organizational analyses. These problems sparked interest in the data warehouse.

The data warehouse provides the data infrastructure that is needed for decision support. Most applications are customer built. Both (in-house) decision support consultants and end users build applications using the warehouse. The consultants do not build applications on their own; rather, they act as facilitators, provide technical expertise, and work with end users in all phases of the development process. Some end users develop applications using access, SAS, or Business Objects as the data Access tools.

There are five full-time decision support consultants. They write SQL queries, know how to use the various data access tools (e.g., Business Objects), and understand the data in the warehouse. Most have MBAs and several of them worked in the business units before becoming consultants.

The most sophisticated analytical applications (e.g., statistical analyses, simulations) are in the actuarial area. BCBSNC has recently filed to become a for profit organization. If approved, advanced analytics in marketing, health care services, and finance will become critical.

Most of the decision support applications reside within the business units but the warehouse has facilitated the development of cross-organizational applications. As an example of the latter, BCBSNC is currently working on a system called the Management Report. It will provide executive level information on key financial and other measures. It will automate a manual effort that currently is performed every month by multiple people who collaborate to create a spreadsheet in order to provide the needed information. Also ‘‘on the radar’’ is the building of a more formal executive information system that will use the warehouse.

The warehouse is affecting how BCBSNC is managed. Over the past few years, there has been a dramatic increase in more fact-based decision making. At the executive level, there is the expectation that when assertions are made, there will be numbers to back them up.

## 3.6. Data warehouse governance

From the inception of the warehouse project, the data warehouse governance structure has played a key role in the CDW’s ability to meet business needs and to adapt to organizational change. This is due to the cross-functional, multi-level nature of the governance structure that supports the data warehousing effort. Fig. 4 shows the current governance structure, its composition, and major activities. The governance structure has gradually evolved over the years to include three groups that correspond with the three different levels of the organizational hierarchy. The groups are: the Vice President Data Oversight Team, the Data Development Oversight Team, and the Business Requirements Group.

To ensure effective communication between the CDW team (i.e., the data warehouse staff) and the different levels of organizational hierarchy, a member of the CDW team chairs and facilitates the activities of each of the governance groups (the CDW team structure is described in greater detail in Section 3.7). The manager of the Business Information Design and Architecture group of the CDW team is accountable for facilitating the Business Requirements Group (BRG), the director of the CDW team chairs the Data Development Oversight Team (DDOT), and the Vice President of Decision

![](/api/attachments/EZBJB4EG/fulltext/images/5e9a84f285a8e0aaf843102fe98e4d8b5d7916f33715730946edabb6469fb194.jpg)  
Fig. 4. Current governance structure.

Support chairs the Vice President Data Oversight Team (VPDOT).

## 3.6.1. VPDOT: the Vice President Data Oversight Team

This officer level, cross-functional team includes a business leader from each of the major divisions within the organization. They meet as needed and provide high-level direction for the entire warehouse initiative. For instance, they provide prioritization criteria and strategic guidance for the CDW project and deal with resource management and prioritization issues when the DDOT cannot resolve them. The VPDOT focuses on ensuring the alignment of the direction of the CDW with the corporate direction.

## 3.6.2. DDOT: the Data Development Oversight Team

This director/manager level team performs most of the project and resource prioritization tasks. It establishes the schedules and priorities for development phases, enhancements, and functionality of the warehouse within budgeted resources. Additionally, it helps resolve cross-functional issues. The DDOT initially met bi-monthly, but due to the high volume of planning and prioritization required, the meetings are currently conducted on a monthly basis.

## 3.6.3. BRG: the Business Requirements Group

This group has been involved in the development of the warehouse almost since the inception of the warehouse project and is composed of CDW power users as well as representatives from the primary decision support areas that were involved in the initial opportunity analysis. The purpose of this group is to discuss and communicate CDW development and use issues with CDW team members and users. Much of their focus is on the development of data. For example, they develop the rules for populating the CDW and cross-functional data definitions. The Business Requirements Group meets biweekly in order to make day-to-day decisions on data quality problems, production data fixes, data stewardship issues, and other daily project management decisions.

Since 1997, there has been turnover in BCBSNC’s CEO, CIO, and most of the Senior Vice President positions. Despite these changes in the upper management of the company, where the main source of sponsorship and direction for the CDW project lies, the original requirements and priorities described in the initial opportunity analysis have not changed. Although requirements that drive the direction of the CDW are owned by the leadership of the business areas, any changes in direction and enhancements are quickly and effectively communicated to the CDW team via the VPDOT, DDOT, and the BRG. As a result, CDW awareness of needed changes in direction occurs early in the process. The frequency of meetings with these groups and the buy-in these groups have to the data warehouse development process support good communications, healthy debate, and a commitment to consensus on the vision and direction for the CDW.

## 3.7. The CDW team

In addition to the cross-functional, multiple level governance structure, a strong warehouse team is critical to the successful execution and continued development of a data warehouse in a business environment that is changing rapidly. Since the introduction of the data warehouse, the data warehousing team has undergone continuous restructuring and evolution in order to serve the changing needs of the different stakeholders within the organization, including upper management, regulatory bodies, the governance groups, and the user community in different business areas.

In 2001, the CDW team was restructured to four groups to better adapt to the changing business environment: the Decision Support Consulting Team, the Business Information and Design and Architecture Team, the DW Project Management and Development Team, and the DW Operations and Quality Control Team. Fig. 5 provides a detailed listing of the roles and responsibilities of each of the four teams.

The Business Information Design and Architecture team is responsible for the identification of high-level needs and requirements of new development projects, design and data analysis, logical data modeling and business rules, and meta-data specification. The Project Management and Development group manages the technical design and ETL tool development and testing. The Data Warehouse Operations and Quality

![](/api/attachments/EZBJB4EG/fulltext/images/fb4e39a749e444623fa0c64b0f148df289d648348723f41ad45abc0d43eab463.jpg)  
Fig. 5. CDW team structure.

Control team is responsible for the operation of the data warehouse. Finally, the Decision Support Consulting team manages training and educating the users on the current functionality of the data warehouse. This team interacts with users in the field and provides one-on-one mentoring and training where required. They also work closely with users in various business areas to identify new needs, functionality, and business areas to be served. It is interesting to note that the Decision Support Consulting team does not produce reports or do analyses; rather, their role is to support these functions which happen in business areas.

## 3.8. Training users

Along with the recent restructuring of the CDW team, training practices have also evolved. As a result of the close working relationship between the decision support consultants and the business areas, a new approach to training has been implemented. Previously, users were given computer-based training (CBT) designed to provide skills on specific tools (e.g., Business Objects, SQL\*Plus). In addition, the CDW staff conducted classes on data warehousing concepts and the data in the warehouse. With this approach, users found it difficult to apply the skills learned to their daily work. In response, the decision support consultants designed a training program that targets the users’ specific job functions (i.e., the reports and analyses they need to perform). Users bring a specific work-related project to the training course, and in the course of 1 day per week over 4 weeks, complete the project using skills learned during the course. At the end of the training program, the users make a presentation of their project accomplishments and leave the training session with a better understanding of how to utilize the data warehouse in their work. The user project presentations also serve as a means of educating other users on the potential uses of the warehouse. The training sessions at BCBSNC have been met with great enthusiasm by the user groups and have proven to be an effective strategy for educating the user community.

The ongoing user support provided by the CDW staff is an additional source of assistance and exposure of the data warehouse to current and potential users. The Reporter/User Group Meetings provide a bi-weekly open forum for users of all levels to discuss topics of interest and cover all methods of accessing the warehouse. Consequently, on alternate weeks, users have access to training laboratories that present in-depth presentations on business cases and advanced query concepts as well as provide one-on-one coaching.

## 3.9. Benefits

BCBSNC has gained a wide range of benefits from its data warehouse. The most obvious benefit has been the creation of a ‘‘single view of the truth;’’ that is, a single source of organization-wide data. The cross-functional team approach to CDW development led to consensus in data definitions, identification of the best source systems to use for reporting and analysis purposes, and greater data accuracy. This resulted in valid and consistent reporting across the organization, which was the primary requirement of the CDW.

In addition, the warehouse has led to numerous other tangible and intangible benefits. Its introduction has promoted a better understanding of the use and efficiencies that can be gained through relational databases. The comprehension and ability to conduct better technical cost analyses has led to the retirement of a marketing information system. It also allowed the actuarial and underwriting areas to attain head count savings by reassigning and eliminating programming staff.

The use of the warehouse has also contributed to better data analysis and time savings by users. Corporate analysts spend less time compiling data and more time analyzing data. Fig. 6 presents a sample of some of the benefits and savings in reporting and processes that BCBSNC is currently reaping from the CDW. The cost savings also extend to costs associated with accessing data from external sources. For instance, the CDW eliminated a cost of

US\$20,000 associated with obtaining data from a vendor to support legislative activities.

The warehouse also eased the establishment of the new claims system, which introduced new products, benefits, and a new way of providing service to BCBSNC customers. The new system was an unexpected addition to the original requirements for the CDW team. As BCBSNC customers were gradually migrated to the new products and benefits, the consolidation of data from the existing systems and the new system was critical. The data warehouse became the means of data consolidation from both core systems and a key component in the transition.

An organization-wide effort to improve data quality is another initiative that was driven by the development of the CDW. As part of the monthly CDW load process, source data are evaluated and reports documenting differences are broadcast to the business areas. This has enabled the warehouse team to drive operational business areas to correctly capture data in the source systems, resulting in greater data accuracy and cost savings through more efficient data loading to the CDW.

In addition to satisfying its primary goal of improving reporting, the data warehousing effort has enabled BCBSNC to effectively pursue its customer-focused corporate information management strategy. For example, there are future plans to capture and store data from additional customer touchpoints, such as the call center and the corporate website, in order to better understand customer behavior and improve customer service. Visitors to the corporate website who are known (such as BCBSNC members) will be able to experience dialogs that are customized to best meet their needs and support BCBSNC’s marketing efforts. Knowledge of a customer’s projected lifetime value will be made available to operational personnel, such as customer service representatives. All of these customer relationship management-oriented applications will be enabled by the enhanced CDW.

Despite being subject to a competitive, dynamic business environment, a difficult regulatory environment, and a changing corporate management, the effective governance practices at BCBSNC have helped the company establish a successful CDW. It enabled the organization to change from a one-dimensional mindset in different business areas to a crossfunctional consensus on data and processes critical to the overall operation of the organization.

<table><tr><td>Report/Process</td><td>Description</td><td>Savings/Benefit</td></tr><tr><td>Renewal Reports – Large Groups</td><td>Automated download of data into rating model as well as an application specific Business Objects Universe for ad hoc reporting.</td><td>• Available within 2 hours of request (before 4-5 day process)• Data retained for 30 days• Data entry eliminated• Drill down capability• Improved reporting</td></tr><tr><td>Renewal Reports – Small/Medium Groups</td><td>Streamlined, working report designed to capture underwriting decisions.</td><td>• Eliminated end-user job (19 hour process)• Reduced end-user working days from 12 to 5• Provides better documentation of underwriting decisions.</td></tr><tr><td>Policy Year Loss Ratios</td><td>Application specific Business Objects Universe</td><td>• Information not available previously• End-user designs own reports as needed</td></tr><tr><td>Active Life Reserves</td><td>Scheduled download of data</td><td>• Overnight plus mainframe job reduced to 20 minute query• Eliminated end user job scheduling and maintenance</td></tr><tr><td>Quarterly Rate Reviews</td><td>Data Mart designed to contain data for Benefit Adjustment Factor Model and Stop Loss Analysis in addition to Quarterly Rate Reviews</td><td>• Macro-driven procedures utilized to create data mart (initiated by end-user as needed)• Dates and hags are in sync within all the tables• Eliminated programmer dependent jobs</td></tr><tr><td>Ad Hoc Requests</td><td>Corporate Analysis Production Business Objects Universe</td><td>• Corporate Analysts trained to go directly to CDW• Ability to analyze claims data</td></tr><tr><td>Facility/Professional duplicate Billing</td><td>Analysis with Corporate Audit for procedure codes billed for both facility/prof.</td><td>• Increasing trend over the last several years (approx. $1 million)• Working with hospitals to correct</td></tr></table>

Fig. 6. Example uses of the CDW.

## 3.10. Lessons learned

The experiences at BCBSNC substantiate and enhance the emerging understandings of effective data warehouse governance. Some of the experiences, such as the importance of having cross-functional committees, are part of the emerging ‘‘conventional wisdom’’ for data warehousing. There are other experiences at BCBSNC, however, that provide richer insights into data warehouse governance. These are presented and discussed as lessons learned.

3.10.1. Lesson #1: senior management participation is necessary but not sufficient—management needs to be passionately involved

Even though the Vice President Data Oversight Team has the responsibility for setting the strategic direction for the data warehouse, some of the members of the committee are not as passionate about the warehouse and are comfortable delegating decision making to others. Cross-functional participation is important, but active participation is what is really needed. The committee members need to be a ‘‘passionate advocate’’ for information. Rather than having all of the business units represented on the committee, only senior managers who have a strong interest in the warehouse, want to link the warehouse closely to business strategy, and use the warehouse heavily in their business units, are critical to the composition of the committee. As a result, the vice-president level committee may be smaller, but more interested and dedicated to the warehouse.

## 3.10.2. Lesson #2: data quality should be a strategic issue

It is easy and tempting to treat data quality as a tactical issue. With this approach, data are extracted from source systems and data cleansing processes are used to improve the data’s quality. Little effort and few resources are used to improve the quality of the data in the source systems themselves. Also, limited attention is devoted to improving the quality of data that are external to the warehouse.

When the warehouse becomes of strategic importance to the company and the company’s data warehouse experience grows, data quality becomes more of a strategic issue. Consequently, data quality should draw the attention and support of senior management, resources must be devoted to improving data quality at the source system level, and everyone in the organization must be more cognizant of the importance of data quality. The data warehouse must also become the official, ‘‘single version of the truth’’ for decision support data.

3.10.3. Lesson #3: multiple committees are needed, some with a business focus, others with a technical focus

Initially at BCBSNC, there were fewer data warehouse governance committees, and the committees had mixed memberships. Some committee members had a business focus, while others had a technical focus. This arrangement did not work well. The business members were not interested in the technical discussions, and the technical members were only slightly more interested in the business issues. Over time, attendance at meetings dropped off.

With the current arrangements, the VPDOT and DDOT deal primarily with the business issues, while the Business Requirements Group works with the CDW team on technical matters. However, business and technical issues are shared with all of the committee members. Emailing and posting on a website the agendas, minutes, documents, and actions associated with the various committee meetings accomplishes this. It has been BCBSNC’s experience that without aggressive communications, important business and technical issues are not adequately shared.

3.10.4. Lesson #4: do not underestimate the need for educating committee members

It is important for the warehouse staff to recognize that many committee members do not fully understand data warehousing and especially the technical complexity that is involved. A good understanding of warehousing is critical to creating realistic expectations of what can be done, the timeframe for doing it, and resources that are needed. Part of each committee meeting should be spent on educating committee members about data warehousing.

## 4. Conclusion

BCBSNC has achieved great success with data warehousing, and a major reason for the success is the strong data warehousing governance that is in place. Let us reconsider the critical areas for data warehousing governance and how BCBSSNC has addressed them.

The starting point for a data warehousing initiative is the clear identification of business needs. BCBSNC recognized that it had fundamental deficiencies in its information access and reporting capabilities, which were being manifested in multiple ways. In response, senior management formed an information oversight committee with representatives from the business units and IS to investigate the problems and develop a recommended course of action. One of the recommendations was the building of a data warehouse.

The business needs for the warehouse have evolved over time. The Vice President Data Oversight Team, which includes business leaders from each of the major divisions of the company, ensures that the direction for the CDW is aligned with company goals. The current focus is on helping BCBSNC become a more customer-focused, information-driven company.

The CDW team and representatives from the business areas conducted an opportunity analysis to determine the information requirements that were used in building the initial version of the warehouse. On an ongoing basis, the Business Requirements Group is responsible for handling information requirements. This is a very ‘‘nuts and bolts’’ oriented group that receives suggestions for change, reviews them carefully, and identifies those that should be implemented. When an information requirement warrants a project rather than a minor change (i.e., more than 10 days of effort), it goes on the list of projects that are reviewed by the Data Development Oversight Team for approval.

The group that identified the information requirements for the initial version of the warehouse also prioritized the implementation of the eight subject areas. Since then, the business areas have prioritized how changes and enhancements to the warehouse should be made. At the highest level, the Vice President Data Oversight Team sets priorities. At the project level, the Data Development Oversight Team sets priorities and schedules for the projects.

The cross-functional team that conducted the opportunity analysis also came to consensus on common data definitions. Then in a series of workshops with the operational and decision support areas, a logical data model was developed. This initial data model continues to serve BCBSNC well and has required only minor fine-tuning. The Business Requirements Group has the ongoing responsibilities for cross-functional data definitions and making sure that the data model meets emerging needs.

Maintaining data quality is an ongoing concern. Data problems are often identified by the Reporter/ User Group, which meets every other week. Depending on the nature and severity of the problem, it may be addressed by the CDW staff directly, the Business Requirements Group, or the Data Development Oversight Team.

BCBSNC has experienced turnover in the CEO, CIO, and most of the Senior Vice President positions. Despite these changes in upper management, the CDW has continued to thrive. Effective data warehouse governance has provided the continuity and ongoing direction that has been required.

The structures and processes used by BCBSNC for data warehouse governance can be considered to be best practices for other companies to follow. Of particular note, BCBSNC uses multi-level, crossfunctional committees. At the highest level, the Vice President Data Oversight Committee has senior management representatives from all of the major divisions within the organization. It provides strategic direction for the warehouse and handles resource acquisition and allocation. Next, the Data Development Oversight Team is comprised of crossfunctional managers who set the priorities for the warehouse, manage the resources allocated to the warehouse, and resolve cross-functional conflicts. Finally, the Business Requirements Group is made up of power users and representatives from the various decision support areas in the company. This group communicates and discusses data warehouse development and use issues with the data warehouse staff. It also deals with data management issues. Collectively, these three committees handle all of the critical areas of data warehouse governance.

There is no single way to organize for and execute data warehouse governance. The approach used at BCBNNC has been recognized for best practices, but there is a need to study additional organizations that excel in data warehousing governance. Such a study would likely find additional best practices. It would also allow a comparison across companies in order to identify a core of best practices. Based on previous data warehousing governance research, one would expect several different best practices in companies implementing departmental data marts [23].

Research has examined factors associated with data warehousing success [11,29]. Data warehouse governance has not been used as a predictor variable in this research, even though some of the factors (e.g., management support, user participation) are related to data warehouse governance (e.g., alignment with company goals, identifying information requirements). It would be useful to restudy data warehousing success using a research model that more directly incorporates the factors associated with effective data warehouse governance.

The experience at BCBSNS suggests that there are multiple factors associated with effective data warehouse governance—cross-functional committees, which serve different yet complimentary roles; coverage of the areas associated with data warehouse governance, such as establishing data definitions and models. It would be useful to validate the data warehouse governance findings at BCBSNC in an empirical study of a large sample of firms.

## References

[1] L. Agosta, Planning a data warehouse? Assemble a crossfunctional team, DM Review (2002 March) 50.

[2] J. Ang, S.H. Teo Thompson, Management issues in data warehousing: insights from the housing and development board, Decision Support Systems 29 (1) (2000) 11 – 20.

[3] A.C. Boynton, R.W. Zmud, G. Jacobs, The influence of IT management practice on IT use in large organizations, MIS Quarterly 18 (3) (1994) 299 – 318.

[4] C.V. Brown, Examining the emergence of hybrid IS governance solutions: evidence from a single case site, Information Systems Research 8 (1) (1997) 69– 94.

[5] C.E. Clark, N.C. Cavanaugh, C.V. Brown, V. Sambamurthy, Building change-readiness capabilities in the IS organization: insights from the Bell Atlantic experience, MIS Quarterly 21 (4) (1997) 425 – 455.

[6] B.L. Cooper, H.J. Watson, B.H. Wixom, D.L. Goodhue, Data warehousing supports corporate strategy at First American, MIS Quarterly 24 (4) (2000 December) 547–567.

[7] S. Crofts, Twenty steps to data warehousing success, Journal of Data Warehousing 3 (2) (1998 Summer) 19–23.

[8] J. Cross, M. Earl, J. Sampler, Transformation of the IT function at British petroleum, MIS Quarterly 21 (4) (1997) 401– 424.

[9] W.W. Eckerson, Evolution of data warehousing: the trend toward analytical applications, The Patricia Seybold Group (1999 April) 1 – 8.

[10] M. Ginzberg, Steps toward more effective implementation of MS and MIS, Interfaces 8 (3) (1978 May) 57– 63.

[11] P. Gray, H.J. Watson, Decision Support in the Data Warehouse, Prentice-Hall, Upper Saddle River, NJ, 1998.

[12] B. Haley, Implementing successful data warehouses, Journal of Data Warehousing 3 (2) (1998 Summer) 48 – 51.

[13] J.C. Henderson, N. Vankatraman, Strategic alignment: leveraging information technology for transforming organizations, IBM Systems Journal 32 (1) (1993) 4 –16.

[14] W.H. Inmon, Building the Data Warehouse, 2nd ed., Wiley, New York, 1996.

[15] S. Kelly, Data Warehousing in Action, Wiley, New York, 1997.

[16] R. Kimball, The Data Warehouse Toolkit, Wiley, New York, 1992.

[17] J.L. King, Centralized versus decentralized computing: organizational considerations and management options, Computing Surveys 15 (4) (1983 December) 320–349.

[18] N. Korac-Kakabadse, A. Kakabadse, IS/IT governance: need for an integrated model, Corporate Governance 1 (4) (2001) 9 – 11.

[19] J.F. Rockart, L. Ball, C.V. Bullen, Future role of the information systems executive, MIS Quarterly 13 (2) (1992) 119 – 134 (special issue).

[20] V. Sambamurthy, R.W. Zmud, Arrangements for information technology governance: a theory of multiple contingencies, MIS Quarterly 23 (2) (1999) 261 – 290.

[21] J. Schwartz, HIPAA Compliance, CRN, 2003 March 24, pp. 6A – 8A.

[22] G. Shanks, P.A. Darke, Framework for understanding data quality, Journal of Data Warehousing 3 (3) (1998 Summer) 46 – 51.

[23] S. Sujitparapitaya, B. Janz, M. Gillenson, The contributions of IT governance solutions to the implementation of data warehouse practice, Journal of Database Management 14 (2) (2003 April–June) 52–69.

[24] B. Vatanasombut, P. Gray, Factors for success in data warehousing: what the literature tells us, Journal of Data Warehousing 4 (3) (1999 Summer) 25 – 33.

[25] H.J. Watson, B.J. Haley, Data warehousing: a framework and survey of current practices, Journal of Data Warehousing 2 (1) (1997 January) 10–17.

[26] H.J. Watson, B.J. Haley, Managerial considerations with data warehousing, Communications of the ACM 41 (9) (1998 September) 32– 37.

[27] H.J. Watson, J.G. Gerard, L.E. Gonzalez, M.E. Haywood, D. Fenton, Data warehousing failures: case studies and findings, Journal of Data Warehousing 4 (1) (1999 Spring) 44 – 55.

[28] R. Winter, M. Meyer, Organization of data warehousing in large service organizations: a matrix approach based on data ownership and competence centers, Journal of Data Warehousing 6 (4) (2001 Fall) 23–29.

[29] B.H. Wixom, H.J. Watson, An empirical investigation of the factors affecting data warehousing success, MIS Quarterly 25 (1) (2001 March) 17 – 41.

[30] R.W. Zmud, Design alternatives for organizing information systems activities, MIS Quarterly 8 (2) (1984 June) 79 – 93.

[31] R.W. Zmud, A.C. Boynton, G.C. Jacobs, The information economy: a new perspective for effective information systems management, Data Base 18 (1) (1986) 17 – 23.

Hugh J. Watson is a Professor of MIS and holder of a C. Herman and Mary Virginia Terry Chair of Business Administration in the Terry College of Business at the University of Georgia. He is the author of 22 books and over 100 scholarly journal articles. He is the Senior Editor of the Business Intelligence Journal and the Senior Director of the Teradata University Network.

Celia Fuller is Director of the Corporate Data Warehouse at Blue Cross and Blue Shield of North Carolina. She has over 20 years of experience in business intelligence, data warehousing, decision support systems, data management, analysis, evaluation, and physician profiling in healthcare, insurance, and government sectors. The BCBSNC data warehouse has won two best practices awards from The Data Warehousing Institute. She has published the results of her projects and is a regular speaker at conferences and symposia.

Thilini Ariyachandra is a doctoral candidate in MIS in the Terry College of Business at the University of Georgia. Her research is focused on the selection, design, implementation and success evaluation of decision support systems in organizations. Her research has been published in Information Systems Management and in national and international conference proceedings.
