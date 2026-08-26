---
otero_id: 22406
otero_key: "K5CY6RWX"
title: "Strategic planning for data warehousing"
authors: "Ashok Subramanian; L. Douglas Smith; Anthony C. Nelson; James F. Campbell; David A. Bird"
year: "1997"
journal: "Information & Management"
doi: "10.1016/s0378-7206(97)00040-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Case Study

# Strategic planning for data warehousing $^{1}$

Ashok Subramanian $^{a}$ , L. Douglas Smith $^{a,*}$ , Anthony C. Nelson $^{b}$ , James F. Campbell $^{a}$ , David A. Bird $^{a}$

$^{a}$ School of Business Administration, University of Missouri - St. Louis, St. Louis, Missouri, 63121, USA $^{b}$ College of Business Administration, University of South Florida - St. Petersburg, St. Petersburg, Florida, USA

Received 10 March 1996; revised 24 March 1997; accepted 8 July 1997

## Abstract

In the course of a major strategic planning exercise for a large municipal government, data warehousing emerged as a tactic for consolidating and sharing information among many City departments with different informational needs and a variety of computing platforms. In this paper, we describe processes and analytical methods for shaping a data warehousing strategy and for determining the contents of the data warehouse. We also present some cautionary conclusions about the development of monolithic data warehouses to serve an entire organization. © 1997 Elsevier Science B.V.

Keywords: Management information systems; Strategic planning; Data warehousing

## 1. Introduction

The municipal information systems of the City of St. Louis serve over 150 departments or subdivisions of City government, several municipal utilities, and numerous external constituencies with widely varying needs. The City's organization is fragmented, with managerial responsibilities distributed among elected officials and senior civil servants. Some of the departments generate revenue or receive grants that provide discretionary funds for MIS services and computer technology; others are service departments that rely upon financial allocations from the Board of Estimate and Apportionment (composed of the Mayor, Comptroller, and President of the Board of Aldermen) for their MIS resources. Some departments engage in their own systems development and support; others use central MIS services.

The City embarked on a major effort to develop a multi-year strategic plan for municipal IS after realizing that it faced several basic problems:

1. There was the classical problem of converting ‘legacy systems’ that are several decades old to take advantage of new technology.

2. The mainframe system failed to provide adequate response in times of peak usage.

3. Sharing of data among departments was impeded by the independent operation of midframe systems in several departments.

4. Client–server systems, geographic information systems, and local area networks were under development without a coherent city-wide strategy.

5. There were organizational concerns about the management of the data resource and maintenance of data integrity in an environment where managerial responsibilities are, by City charter, extremely diffuse.

Strategic planning for MIS in such an environment is an extremely difficult exercise, requiring the voluntary cooperation of elected officials, departmental managers, technical staff, systems analysts, and end-users with very heterogeneous interests and perspectives.

At an early stage in the strategic planning effort, the maintenance and sharing of data among many City departments with different informational needs and various computing platforms emerged as the most pressing issue. Data warehousing, which has been proposed as an effective method of consolidating corporate information and sharing it among organizational entities for analytical purposes and decision support $[11, 14]$ , was proposed as a framework for dealing with the issue. Much of the literature on this topic has focused on the technology required to establish and support data warehouses $[3, 19]$ . More attention needs to be given to procedures for determining when a data warehouse would be effective, gauging potential demand in the user community, and identifying the data elements that should be maintained in various forms $[20, 23]$ . In this paper, we describe planning processes and analytical methods for shaping a data warehousing strategy, for determining the contents, and for projecting where usage will be concentrated. We also relate the results of applying them to municipal IS in a large City. Although our findings are generated from an effort in the public sector, where strategic IS planning is regarded as especially difficult $[16]$ , private corporations face similar problems $[10]$ , and data warehousing is increasingly being recognized as a useful concept. Indeed, in a survey of 250 companies polled in 1995, more than 95% indicated that they planned to build a data warehouse. Just a year earlier, only 15% expressed such an intent $[1]$ . We expect that our methodologies would be equally applicable to organizations in the private sector, and especially useful in the wake of corporate restructuring through mergers and acquisitions.

## 2. Data warehousing

Data warehouses have been described as subject-oriented, integrated, time variant, non-volatile sets of data in support of management's decision making process [22]. They are widely regarded as useful devices for maintaining information from multiple sources and delivering it to managers and analysts who may be using a variety of computer platforms or software with special features and capabilities [21]. Data warehouses may, for example, be composed of hundreds of tables in a relational database constructed to support typical queries [4]. In the case of City government, they would include data describing parcels of land, personal property, voters, permits, licenses, etc.

The creation of a data warehouse, especially on an enterprise-wide scale, is a major undertaking. It involves the development or acquisition of tools for user access, database maintenance, and data transfer and scrubbing. Tools may be designed particularly for that purpose, or may be crafted from general-purpose software, such as statistical packages, relational database systems, or spreadsheet software. Since the development of a full-scale data warehouse with supporting middleware and analytical tools can cost upward of one million dollars, care must be taken to determine the nature of its ultimate use. Clearly, not all information would be placed in the warehouse; not all departments would desire the same information; not all departments are equipped to use information in the same physical format. Before dwelling on the detailed aspects of the warehouse design, therefore, it is useful to perform an information system requirements analysis $[5]$ to determine the types of information required for effective management of operations, organizational control, and strategic planning. It is also necessary to assess the talents and mind-sets of potential users with a view to assessing their readiness for end-user computing $[18]$ . Attention can then be focused productively on the supporting technology and the mechanics of establishing and maintaining a data warehouse.

Our approach to strategic planning for data warehousing melds elements from various methodologies, such as business systems planning (BSP), strategic data planning (SDP), strategic information systems planning (SISP), information technology planning (ITP), critical success factors (CSF), frequently asked questions (FAQ), strategic business objectives (SBO), etc. [2, 7, 9, 12, 13, 15]. It thus uses a combination of top-down and bottom-up approaches designed to address organizational issues, managerial processes, the IS infrastructure, and the management of IS resources.

## 3. Overview of the planning process

As already indicated, the planning for data warehousing took place within a broader strategic planning exercise for municipal IS. At all levels, mechanisms were employed to foster creative thinking, provide necessary education, and produce consensus. Key elements were:

1. Use of a strategic planning oversight committee for the entire process and subcommittees for investigative thrusts in MIS, communications technology, and geographic IS. The committees helped to identify critical issues and to build consensus for the plan. This top-down perspective is consistent with BSP and SSP methodologies.

2. Provision of departmental orientation sessions to prepare managers and technical staff for their participation. These sessions were to encourage managerial involvement and to refine goals for the study.

3. Compilation of departmental MIS surveys to describe functions, needs for information, interdepartmental patterns of communication, and usage of technology by representatives of each category of employee in the department. These surveys had some top-down aspects in common with BSP, SBO, FAQ and CSF, but also provided detail with more of a bottom-up character that would be used to construct a data usage matrix similar to that which would result from an IE exercise.

4. Use of technology surveys to describe current configurations of information technology and to derive suggestions for improvements from operational staff, similar to that from a re-engineering effort.

5. Provision of presentations to educate managers and staff regarding current systems and their capabilities. BSP stresses the education of those responsible for the production of the strategic plan. Our orientation exercises, however, revealed a general lack of understanding of systems in place, information available throughout the organization, and alternative mechanisms for accessing data. Concurrent education of departmental personnel (with presentations on current databases, prototypes for data extraction and analysis, and applications of geographical IS) and systems professionals (who attended seminars on data warehousing) were considered vital for an objective assessment of current capabilities and recognition of opportunities.

6. Creation of a data-usage matrix to illustrate interdepartmental information usage. We extended standard matrix representations of data usage to include information about temporal requirements of data, nature of data usage, platforms employed, and number of sources used.

7. Production of project profiles for current and potential MIS initiatives in each department. We grouped suggestions with similar characteristics into ‘meta-projects’ that crossed departmental boundaries for subsequent consideration in the tactical planning for MIS initiatives.

8. Production of MIS planning profiles for each of 35 major departments. These profiles provided a consolidated view of managerial processes and informational requirements that could be used for building integrated systems.

9. Consideration of organizational issues for the planning and management of MIS resources. These are often treated as constraints in BSP and SSP exercises. Instead, we invited the oversight committees and subcommittees to deal with these issues by using nominal group techniques [8]; we also invited departmental staff to make any suggestions in their responses to the MIS surveys.

10. Feedback to departmental managers before consolidation of information in the production of the plan. This step ensured the accuracy of findings from the departmental surveys, provided assessments of the potential impact of alternative initiatives, and built consensus for the final plan.

11. Study and depiction of the current computing infrastructure. In this phase, a bottom-up perspective prevailed as physical configurations were studied and current system performance was assessed.

12. Evaluation of alternative topologies for the computing infrastructure and recommendation of a preferred alternative. Returning to an enterprise-wide view, we considered alternative configurations of mainframe computers, client-server systems, and stand-alone PCs.

13. Study of practices in other cities. Through surveys of other cities and a site visit, we performed a study of ‘best practices.’ This lent authority and credibility to our final recommendations. With our findings, we were able to respond to skepticism by citing others’ successes when using our proposed strategies.

14. Review of reports from past planning efforts and documentation pertaining to current systems, thus using traditional EDP planning procedures.

15. Use of the oversight subcommittees in refining draft recommendations. Extensive feedback and iterative production of final recommendations ensured that no surprises occurred during the presentation of the final plan.

In Appendix A we show the nominal group exercise used to launch the strategic planning process; it reveals how data warehousing emerged as a strategy for managing the maintenance and sharing of data.

## 4. Departmental surveys

Data regarding information usage and flows were obtained from a structured, open-ended, MIS survey administered within each major department and within each major departmental subdivision (143 surveys in all). The survey, shown in Appendix B, addressed a variety of issues important to the development of a strategic plan for IS, including those that are relevant to data warehousing. Background information was requested regarding the size of the department, historical expenditures for computing technology, the department's mission and goals, departmental functions, and the computing technology used to support these functions. Particularly germane to data warehousing, the types of information generated by or used by the department were identified. Then, for each of the information types, the flows between the responding department, and other City departments or external entities were described, and allowable time intervals between updates of the database were stated. A set of questions addressed special requirements for privacy or security of data, current problems with information processing, opportunities for improving the ways in which information is acquired or processed, possible changes in the organization of support for MIS activities and delivery of computing services, and possible changes in the City's processes for planning and budgeting improvements in municipal IS and the supporting technology. Each department was asked to recommend a set of MIS initiatives or projects that would improve its productivity.

A complementary technology usage survey was administered to a representative of each employee category in each department of the City (158 surveys representing 2700 employees). In this survey, we inquired about the hardware and software available and the uses to which they are put. We probed further to determine the level of end-user computing expertise and the ability to develop and maintain applications within the department.

Functional profiles for each major department were prepared from the responses to the MIS surveys. These profiles included:

1. the mission and functions of the department and its subdivisions.

2. the types of information used or generated by the department.

3. the associated computing platform or storage medium and the functions supported by the information.

4. the transmission of information to or from other departments or external entities.

5. the temporal requirements for the various types of information (e.g., whether up-to-date data or periodically summarized data are required).

6. the list of recommended MIS projects or initiatives.

Departmental managers were asked to consider information as a strategic resource and to articulate potential uses or flows of information as well as the current usage. A sample extract showing the mission and functions of a division of the personnel department is provided in Table 1. In Table 2, we list the types of information used in that division. To make sure that we properly understood and represented the concerns, we held individual meetings with department heads and their chosen representatives in which we presented our summaries of findings from the MIS Survey and the Technology Survey. In these meetings, we obtained clarifications, corrections, and verification of the accuracy of our summaries.

Table 1
Sample Functional Profile

<table><tr><td colspan="2">Department Name: Department of Personnel</td></tr><tr><td colspan="2">Area: Compensation and Employee Relations</td></tr><tr><td>Ronald Marshall, Manager</td><td>622-3565</td></tr><tr><td colspan="2">Mission: to administer the following city-wide programs:</td></tr><tr><td colspan="2">Safety</td></tr><tr><td colspan="2">Appeal</td></tr><tr><td colspan="2">Drug and alcohol testing</td></tr><tr><td colspan="2">Functions:</td></tr><tr><td colspan="2">(1) administer safety program, report injuries, gather safety data and accident/injury data</td></tr><tr><td colspan="2">(2) handle appeals and compile grievance reports</td></tr><tr><td colspan="2">(3) administer drug and alcohol program and compile related reports.</td></tr></table>

Table 2

<table><tr><td colspan="2">Sample Information Types</td></tr><tr><td>Information Entities Used</td><td>Functional Narrative</td></tr><tr><td>Safety Program</td><td>The safety program information is used to administer safety programs, prepare accident-injury reports and lost – time salary expense reports.</td></tr><tr><td>Location: Minicomputer, PC</td><td></td></tr><tr><td>Update needs: Monthly</td><td></td></tr><tr><td>From: All departments</td><td></td></tr><tr><td>To: Concerned department</td><td></td></tr><tr><td>Appeal Program</td><td>The appeal program information is used to track grievances and prepare grievance reports, monthly examination reports and service rating reports.</td></tr><tr><td>Location: PC</td><td></td></tr><tr><td>Update needs: Monthly</td><td></td></tr><tr><td>From: All departments</td><td></td></tr><tr><td>To: Internal</td><td></td></tr><tr><td>Drug and Alcohol Report</td><td>The drug and alcohol report is used to track positive and negative drug alcohol tests and prepare related reports.</td></tr><tr><td>Location: PC</td><td></td></tr><tr><td>Update needs: Monthly</td><td></td></tr><tr><td>From: Healthline Corporate Health services</td><td></td></tr><tr><td>To: Not specified</td><td></td></tr></table>

## 5. Construction of an information usage matrix

Data exist in organizations in two forms: (1) current operational data about individual entities or transactions, and (2) frozen extracts that show the status of selected entities at chosen points in time, or that consolidate and summarize information about changes in states through time. The former we shall call 'current'; the latter we shall call 'frozen.' Other authors use the term 'operational' for data that support business transactions and 'summarized' for data that are intended for end-user analysis and decision support. From the information-usage parts of the departmental profiles, we created an information usage matrix (how each department produces and shares information with others). In preparing the matrix, we created broad categories of information types to allow a manageable consolidation of data for the thirty-five major departments of the City. We also ignored information that was mentioned by only one department or division, as it would not be included in the warehouse. Entries in the matrix contain three groupings. The first refers to the type of computer system used to furnish the information. The second pertains to the manner in which the information is used by the department. The third distinguishes whether absolutely up-to-date data (as in an on-line master file or hard-copy archive) are needed or whether 'frozen' extracts or summaries are used. The following codes were used:

## - Delivery system

H=hard copy; M=main frame computer (e.g., IBM 4381); m=mid-frame computer (e.g., IBM AS/400); S=local server (e.g., a work station serving as a file server); P=stand-alone personal computer; O=on-line service from an external source (e.g., Internet)

## • Use of the information

C=creating elements of data in the information category that are added to a database; U=updating elements of data in the information category; R=reading information for inquiries, reports or analysis;

## - Temporal status

c=current (up-to-date); f=frozen.

Multiple designations are possible in each category. For example, MS : UR : cf would apply if a type of information were maintained (updated) by a department on the mainframe, and downloaded periodically to a local server for analytical purposes. An illustrative excerpt from the information usage matrix is given in Table 3.

In examining the information usage in aggregate, we observed a considerable need for sharing both current data and frozen extracts among departments. Further analysis of the functional profiles for the individual departments, however, revealed that the needs for current data (other than for direct data entry or transaction processing) are primarily for routine cross-checking of information in connection with some transaction. Analysis and periodic reporting relied more on frozen data. The need for complex integration of data from multiple sources was more prevalent for frozen than for current (up-to-date) data.

<table><tr><td></td><td>Parcel, Commercial</td><td>Parcel, Residential</td><td>Personal Property, Residential</td><td>Personal Property, Commercial</td><td>Plat Maps</td><td>Permit, Building</td><td>Permit, Other</td><td>Licenses, Business</td><td>Licenses, Liquor</td></tr><tr><td colspan="8">Airport</td><td>H : R : f</td><td>H : R : f</td></tr><tr><td rowspan="2">Assessor</td><td>MH : CU : c</td><td>MH : CU : c</td><td>MH : CU : c</td><td>MH : CU : c</td><td>H : CU : c</td><td>M : R : c</td><td></td><td></td><td></td></tr><tr><td>H : R : f</td><td>H : R : f</td><td>H : R : f</td><td>H : R : f</td><td>H : R : f</td><td>H : R : f</td><td></td><td></td><td>H : R : f</td></tr><tr><td>Board of Aldermen Board of Elections</td><td>H : R : cf</td><td>H : R : cf</td><td>H : R : cf</td><td>H : R : cf</td><td>H : R : cf</td><td>H : R : cf</td><td>H : R : cf</td><td>H : R : cf</td><td>H : R : cf</td></tr><tr><td>Board of Pubic Service Budget Division</td><td>H : R : f</td><td>H : R : f</td><td></td><td></td><td></td><td>H : R : f</td><td></td><td></td><td></td></tr><tr><td>CEMA</td><td>HS : R : f</td><td>HS : R : f</td><td>HS : Rf</td><td>HS : R : f</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Table 3
Excerpt from the Information Usage Matrix

## 6. Analysis of information usage patterns and proposed MIS initiatives

Selection of information entities for the data warehouse and identification of its prospective users are facilitated by three summary data matrices and an analysis of projects proposed in response to the MIS Survey. The first summary matrix (Table 4) simply identifies all departments that need information entities in frozen form; the second identifies all departments that need information entities in current form; the third identifies all departments that need information entities in both forms. Data entities used by many departments in frozen form are logical candidates for inclusion in the data warehouse. Departments requiring a large number of different entities from a variety of data sources in frozen form are expected to be the prime users of the data warehouse.

The project recommendations may be reviewed to indicate usage of the data warehouse that may occur from new MIS initiatives. In the City, there were 363 recommendations from departments or subdivisions for MIS projects or initiatives ranging from major computer upgrades and applications development efforts to a need for minor connections between existing systems. Clustering the recommendations in a platform hierarchy from mainframe to server to stand-alone PC, we found the following projects requiring investments in technology, software, or systems development:

75 for the mainframe

111 for network servers

171 for desktop computers.

In addition, there were 71 recommendations for electronic communication of data or ‘other effort,’ such as data cleansing. This rough metric gives a strong indication that a considerable number of the City’s MIS initiatives involve the mainframe computer; a greater number involve network servers; an even more involve stand-alone PC’s.

Table 5 illustrates how we summarized the projects for this phase of the analysis. For each of the project recommendations, we estimated (as low, medium, or high and indicated by one, two, or three check marks, respectively) the incremental investment in technology, the systems development effort, and software investment required on each type of platform. We also indicated whether the corresponding data would be obtained: (1) in current (up-to-date) form from a single database, (2) in current form from multiple databases, (3) in frozen form from a single database, or (4) in frozen form from multiple databases (including hard copy). The departments with interests in projects requiring data from multiple databases in frozen form should be prime users of the data warehouse.

Eighty-nine of the 363 projects used data from multiple databases in frozen form. On further investigation, we observed that these projects were concentrated in 23 departments. Within that group, two-thirds of the projects emanated from six departments. Four of those departments (streets, water department, public safety, and community development) were involved in the construction of geographic IS (GIS) for their individual analytical purposes. Complementary statistics produced from Table 4 lead to similar conclusions about the concentration of interest in the data warehouse. Fifty-five percent of the department-entity combinations (110 of 203) were concentrated in six departments. Three of those (community development agency, water, streets) primarily needed GIS-related data.

Departmental analysts and managers expressed concerns about data administration in a warehousing context. In the course of their analysis, user departments expect to produce information that would be relevant to some other departments and which therefore should be placed in the data warehouse. They also expect to identify and correct errors in some of the detailed extracts from the data warehouse as they uncover inconsistencies. Analysts and managers stressed the importance of communicating problems to all relevant parties and for applying corrections to the original operational data from which the extracts are derived. With new information generated by users of the data warehouse, and feedback to correct errors at the original source, the flows of information in a data warehousing environment are better represented by a cyclical network than by a tree. This non-hierarchical pattern for usage and maintenance of the data has both organizational and technical ramifications for maintenance of a data warehouse.

The construction of a data warehouse should be viewed as an evolutionary process. Any formal planning methodology will overlook some opportunities for sharing data that could add future value to the organization. With data warehousing, particular attention need to be given to the risk of leaving useful information hidden in individual departments. In our 'top-down' specification of informational needs, we essentially used a 'demand-pull' model for populating the data warehouse. As part of our strategic planning process, however, we also had data managers conduct sessions in which they described the contents of databases currently maintained on various systems. Representatives from all City departments or subdivisions were invited to attend. Similar communication and education will be required on an ongoing basis to help to identify new opportunities for sharing data. A combination of formal and informal efforts on the part of data administrators, departmental managers, and users is required to maintain an appropriate evolutionary culture [17].

Table 4
Excerpt from matrix showing inter-departmental use of frozen extracts

<table><tr><td></td><td>Parcel Comm.</td><td>Parcel Res.</td><td>Pers Prop. Res.</td><td>Pers Prop. Com.</td><td>Plat maps</td><td>Permit Bldg.</td><td>Bus Licenses</td><td>License Liquor</td><td>Motor Vehicle</td><td>...</td><td>Elections</td><td>Employee &amp; Req.</td><td>Purch &amp; Budget</td><td>Accts. &amp; Bids</td><td>Contract &amp; Bids</td><td>RFPs &amp; PEOs</td><td>Utilities &amp; CBL</td><td>Environment</td><td>Demographics</td><td>Mapping data</td><td>City Facilities</td><td>Public Works</td><td>Legislation</td><td>Court Cases</td><td></td></tr><tr><td>Airport</td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td>...</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>8</td></tr><tr><td>Assessor</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>9</td></tr><tr><td>Alderman</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td>...</td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td></td><td>22</td></tr><tr><td>Elections</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4</td></tr><tr><td>Public</td><td>X</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>...</td><td></td><td>X</td><td></td><td>X</td><td>L</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>7</td></tr><tr><td>Budget Div.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>2</td></tr><tr><td>CEMA</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td>7</td></tr><tr><td>Circuit Atty</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3</td></tr><tr><td>Circuit Clerk</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>3</td></tr><tr><td>Cir Court/Admin.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>Circuit/Probate</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>Counselor</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4</td></tr><tr><td>Marshall</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>City Court</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>Collector/Rev.</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>9</td></tr><tr><td>CDA</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td>...</td><td></td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>20</td></tr><tr><td>Comptroller</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td>...</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td>X</td><td></td><td>23</td></tr><tr><td>CREA</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>2</td></tr><tr><td>Personnel</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3</td></tr><tr><td>Safety</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td>...</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>9</td></tr><tr><td>Health &amp; Hospital</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>Human Service</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td>4</td></tr><tr><td>Jury Supv.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>2</td></tr><tr><td>Lic Collector</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>7</td></tr><tr><td>Mayor</td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>16</td></tr><tr><td>Med Exam</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>Parks/Rec.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td>3</td></tr><tr><td>Police</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>Rec. of deeds</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>Register</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>Sheriff</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>SLATE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>Street Dept.</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td>...</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td>11</td></tr><tr><td>Supply Div.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>Water Div.</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>...</td><td></td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td>18</td></tr><tr><td></td><td>12</td><td>11</td><td>5</td><td>5</td><td>6</td><td>7</td><td>5</td><td>6</td><td>4</td><td>...</td><td>2</td><td>10</td><td>5</td><td>17</td><td>4</td><td>1</td><td>9</td><td>6</td><td>6</td><td>8</td><td>4</td><td>7</td><td>4</td><td>10</td><td>203</td></tr></table>

<table><tr><td colspan="17">Table 5Format for Summarizing Characteristics Of Proposed Projects</td><td></td></tr><tr><td>Project Description and Anticipated Benefits (EI=estimated impact)</td><td colspan="4">Technology Investment MF=main frame PC=PC or workstation S=serve C=communications</td><td colspan="4">Systems Development MF=main frame PC=PC or workstation S=server C=communications</td><td colspan="4">Software MF=main frame PC=PC or workstation S=server C=communications</td><td>Other Effort</td><td colspan="3">Data Required S=single database M=multiple databases C=current F=frozen</td><td></td></tr><tr><td>(1=low, 5=high)</td><td>MF</td><td>PC</td><td>S</td><td>C</td><td>MF</td><td>PC</td><td>S</td><td>C</td><td>MF</td><td>PC</td><td>S</td><td>C</td><td></td><td>SC</td><td>MC</td><td>SF</td><td>MF</td></tr><tr><td>Develop a new dispatching system that displays available equipment, recommends equipment to dispatch, and links to hazardous materials database and incident reporting system. This will allow better equipment management (most beneficial during major incidents). A link to hazardous materials database can improve safety. A link to incident reporting system improves accuracy and speed of incident reporting. (DPS, Fire Dept., EI=4)</td><td></td><td></td><td></td><td></td><td></td><td>✓✓✓</td><td>✓✓</td><td>✓</td><td></td><td>✓✓</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td>✓</td></tr><tr><td>Introduce the automation of docket information for Judges to eliminate a manual process. (City Courts, Docket and Preparation, EI=3)</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Provide for automated routing for pickups to be accessed by foreman. (Street - Refuse Division, EI=1)</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✓✓✓</td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td></td></tr></table>

## 7. Outcomes

Eighteen months after the completion of the strategic plan for municipal IS we revisited the City to discuss progress in its implementation. The comprehensive plan called for a major reorganization of IS services, a change from a mainframe-centric to a network-centric philosophy (with the mainframe serving as a major node), and the adoption of the data warehousing strategy. The recommendations for computer architecture were readily accepted. Upgrades to the mainframe and establishment of gateways to desktop computers began shortly after presentation of the strategic planning report, despite an immediate change in management. The data warehousing strategy was accepted and development began, but modestly as suggested, for information pertaining to real property (physical characteristics, zoning, assessment, and taxation). For some time, the development was mired in debates about where to locate the relational databases and servers and what software to use. At issue were the loci of responsibility for maintenance and sharing of data. It took over a year and the appointment of a new director of MIS (or CIO) to motivate implementation of the 'softer' recommendations regarding the general organization and management of MIS services. Decisions and cooperative action to implement the data warehousing strategy are expected to occur more rapidly under the new organizational structure. Lincoln [16] asserts that organizational impedances to the effective development and maintenance of MIS are more imposing than the technological constraints. Our experience bears this out. Nevertheless, the City reports that it is using the Strategic Plan to guide the data warehousing initiative.

## 8. Conclusion

The development of analytical models and DSS in organizations is often hindered by the lack of data in a convenient and relevant form. Data warehousing is advocated as a solution to this problem. We have presented an analytical framework for the determination of potential users, applications, and information entities for a data warehouse and described the insight we derived from applying it to municipal IS.

In the case of St. Louis City, we undertook a comprehensive strategic planning exercise and encouraged managers throughout the project to consider information in a value-added context and as a potential resource for analysis and decision support. The planning process combined top-down and bottom-up perspectives and included education of participants.

One of the main recommendations was for the City to change from a mainframe-centered to a network-centric computing topology. The data warehouse was seen as a natural device to aid in this transition. We would, however, caution against the development of a monolithic data warehouse that is supported by highly standardized desk-top tools throughout an organization. In the City, a surprising number of recommended MIS projects pertained to routine business operations and transaction processing that simply required the integration of 'current' data from operational databases. A smaller proportion pertained to integration and analysis of 'frozen' data in a manner for which the warehouse is most suited.

Integration of ‘frozen’ data from a variety of internal and external sources and sharing it among departments for analysis and decision-support was, however a high priority for some departments. With the help of functional profiles for each department, data usage matrices, and MIS project profiles that were produced from a comprehensive strategic planning effort, we predict that usage of the data warehouse will be far from uniform. We also find a need for informational loops from departments back to the operational databases and data warehouse as errors in the data are corrected and as complementary information is added by end-users during the course of their unstructured analyses. We suspect that similarly non-uniform patterns of expected usage and non-hierarchical generation and maintenance of information will occur in most organizations.

We believe that the key to a successful data warehousing effort is to perform a strategic analysis. As users' information needs change, the information usage matrix and corresponding data model of the organization must be updated and modified. Corresponding organizational changes would probably be required for data management. Considering the high cost of data warehousing technology and the inherent risks of failure, we concur with recommendations that the implementation begin with the creation of small warehouses or data marts for prime users with considerable end-user computing experience. Much of the potential benefit from data warehousing may be realized from using the concept on a selective basis and at a modest scale.

## Acknowledgements

Mimi Duncan, Dolly Matthew, Lenis Boswell and Nancy Tabor provided valuable assistance in the definition of information entities and creation of the information usage matrix. We are grateful to these individuals, to others on our twenty-member project team, to City departmental managers, MIS technical staff, members of the Strategic Planning Oversight Committee, MIS Subcommittee, Technology Subcommittee, and GIS Subcommittee who participated in the study. Without the cooperation and involvement of all these parties, the successful completion of the study would have been impossible. We are glad to acknowledge our colleague, Professor Kailash Joshi, who suggested that we adopt a data warehousing strategy to deal with technological and organizational issues in the sharing of data.

## Appendix A

## Preliminary Nominal Group Exercise

The importance of considering IS products and services within a broader organizational context [6] and the potential utility of an hierarchical approach to IS strategic planning are well recognized. Accordingly, we initiated the strategic planning exercise with a top-down perspective. A Strategic Planning Oversight Committee was formed with representation from thirty-five major (umbrella) departments of the City. Each departmental manager was asked to select the individual that he or she judged could best represent the department's interests. Generally, a high-level supervisor responsible for departmental operations (i.e., an IS user) was chosen. In a few instances, the department selected individuals who had taken a leading role in the development of departmental information systems. The computer systems groups were represented by their directors and senior analysts.

The first activity was a group elicitation exercise (using the nominal group technique) involving all members of the Strategic Planning Oversight Committee. Its purpose was to achieve consensus on the critical issues for the development of an effective MIS plan, to obtain a city-wide perspective on MIS needs and to set the stage for cooperation among the various parties in the information gathering process. We gave an overview of our philosophy and work plan for the strategic planning exercise at the first meeting of the Strategic Planning Oversight Committee, and we asked them to address the following questions, in turn, within the nominal group discussion format [8]:

1. What problems should be addressed as we study the City's municipal information systems, computer technology, and communications systems?

2. What opportunities should we consider as we develop a comprehensive plan for the City's municipal information systems?

3. What obstacles would you anticipate in implementing a comprehensive plan for municipal information systems in the City of St. Louis?

The nominal group technique was employed to ensure that the ideas of each participant were presented for consideration in a format that encourages individual thought, stimulates new thoughts by sharing ideas, and prevents dominance by a vocal minority. Participants were asked to write down their thoughts in response to the question under discussion. Then each participant, in turn, was invited to present the item at the top of his list (or the next item if the top item had been presented previously). The moderator paraphrased each item. Discussion was limited to questions for clarification from other participants (i.e., no debate occurred on the merits of the item). The item, as clarified, was posted for further consideration. The process was repeated in a round-table manner with each individual adding a single item from his or her list until all the items on the individual lists were included. At the end, the moderator had the group identify similar themes, and consolidate items where possible. Then, individual participants were asked to review the posted list of items and to submit, in writing, the list of 'top five' problems, from Question 1, the 'top five' opportunities from Question 2, and the 'top three' obstacles from Question 3. We computed median values of individuals' priority rankings in order to represent the group's consensus. The results of the 'voting' were shared at subsequent meetings of the oversight subcommittees and were used to focus our inquiry throughout the study.

According to the consolidated rankings, the top two problems and opportunities identified by the Strategic Planning Oversight Committee pertained to the sharing of data among departments. The members cited the existence of islands of incompatible (or unconnected) computer systems and the related inability to consolidate data and share information in a timely manner. Logically, the integration of material from individual information systems was ranked highest among opportunities to effect improvements in the municipal information systems. Members of the committee specifically advocated the development of a city-wide policy with respect to the sharing of information and the provision of a ‘seamless’ connection among the various repositories of data. To overcome obstacles to the successful implementation of a comprehensive strategic plan for municipal information systems, they stressed the importance of encouraging a philosophy that treats information as a city-wide resource, the sharing of which should be restricted only by legislated mandate or generally accepted needs for confidentiality. A primary outcome of the nominal group exercise was thus a recognition of the need to integrate diverse systems with the primary objective of sharing cross-functional data.

Although the oversight committee stressed inter-departmental sharing of data as its highest priority, it was not clear how this should be accomplished. Technically, it could be accomplished by any combination of inter-departmental file servers, universal access to a large centralized data base, or creation of a data warehouses or 'data marts.' Data warehousing seemed to be a natural fit to the fragmented organizational setting and its related problems, but more insight about the nature of inter-departmental information flows and uses of information were required to evaluate the potential of data warehousing or to develop an effective data warehousing strategy. A systematic approach for acquiring that insight is the main topic of this paper.

## Appendix B

## MIS survey instrument

## B.1 Municipal information systems survey for ST. louis City departments

## B.1.1 Form 1

Introduction: On the pages that follow, you will be asked to describe the general mission, goals, and functions of this department. linen you will be asked to describe ways in which work processes and computer systems might be improved to take advantage of new technologies. Finally, you will also be asked to describe the general types of information this department receives, uses and/or transmits. If you have any questions regarding this questionnaire, please contact xxxxxxxxxxxxxxx at xxx-xxxx.

1. Department Name: \_\_\_\_

2. Total number of employees in this department:

5. What is the total annual budget for your department? \_\_\_\_ Now consider expenditures for information technology and services. Approximately how much has your department spent last year and over the past five years on:

<table><tr><td></td><td>Last year</td><td>Past 5 years</td></tr><tr><td>a. Hardware acquisition</td><td>____</td><td>____</td></tr><tr><td>b. Software acquisition</td><td>____</td><td>____</td></tr><tr><td>c. Training</td><td>____</td><td>____</td></tr><tr><td>d. Maintenance</td><td>____</td><td>____</td></tr><tr><td>e. Internal systems analysis and development</td><td>____</td><td>____</td></tr><tr><td>f. External consultants for MIS</td><td>____</td><td>____</td></tr><tr><td>Total</td><td>____</td><td>____</td></tr></table>

6. Briefly describe the primary mission and goals of this department.

7. Please list the primary functions performed by this department and indicate the type of computer support on which they depend (i.e., main frame, mini-computer, or PC).

8. Please indicate and describe, if necessary, the general types of information that are currently received, generated and/or used by this department in the performance of its primary functions. (Please complete Form 2 for each type of information.) Include information gathered or transmitted by telephone, television, on-line information services, video conference or any other type of communication.

B.2 Municipal information systems survey for St. Louis City departments

## B.2.1 Form 2

(Use a separate form for each type of information listed in Item 8 of Form 1)

Department\_\_\_\_ Type of information\_\_\_\_

1. Please name the city department(s) and/or source(s) external to city government from which this department acquires this information.

2. Please list any alternative city department(s) or external source(s) from which the information can be acquired. (Please specify.)

3. Please name the city department(s) and/or source(s) external to city government to which this department sends this information.

4. What does this department do with this information (check all that apply)? When appropriate, please indicate the name of the computer system, report, or form used. (Include person to person contacts by telephone or other communication medium.)

\_\_\_\_Create or enter\_\_\_\_

Update or delete

\_\_\_\_File/Store: Hardcopy\_\_\_\_

Computer

\_\_\_\_Perform inquiries by computer\_\_\_\_

\_\_\_\_Receive reports in hardcopy format\_\_\_\_

\_\_\_\_Create reports in hardcopy format\_\_\_\_

\_\_\_\_Used to perform various tasks\_\_\_\_

5. How current must the information be for its most urgent use?

Immediate Hourly Daily

Weekly\_\_\_\_Monthly\_\_\_\_Yearly

## B.2.2 General questions

1. Briefly describe any necessary provisions for security of data or legal requirements (specific statues and ordinances) regarding the information which this department receives, distributes, or uses.

2. The following questions pertain to current problems with information processing and with opportunities to improve the way that information is acquired or processed.

a. Please describe any functions or processes which you feel should be computerized or for which processes should be changed. Briefly describe the benefits of each.

b. What new information could help the department perform its functions better? How should that information be provided? Briefly describe the associated benefits.

3. What changes should we consider in the organization of support for management information systems activities and the delivery of computing services?

4. What changes should we consider in the City's processes for planning and budgeting improvements in municipal information systems and supporting technology?

5. In conclusion, please summarize the major projects or initiatives regarding management information systems or computing technology that should be undertaken over the next three to five years to improve the functioning of your department (or division). For each of these projects, please rate their impact on a scale from one (minor impact on productivity) to five (major impact on productivity). If possible, you might also assign as estimated dollar benefit to the projects you list.

## B.2.3 Supplemental materials

Please provide each of the following items with your responses to the MIS Survey.

1. An organizational chart of the department.

2. Copies of pending requests for computer services or equipment.

3. Copies of reports from pervious information system studies performed for the department.

The following items (4,5,6) may be provided if they help to communicate the fundamental types of information used in the department, obtained from an external source, or conveyed to an external unit:

4. Completed (not blank) forms which are referenced in the survey.

5. Sample pages of reports which are referenced in the survey.

6. Printed copies of on-line computer application screens most frequently used to perform the primary functions of this department.

## References

[1] ADS data warehousing survey, The Meta Group Inc. (1995) 1–12.

[2] R. Agarwal, L. Roberge and M. Tanniru, MIS planning: A methodology for systems prioritization, Information and Management 27, 1994, pp. 261–274.

[3] E. Appleton, The right server for your data warehouse, Datamation 41(5), 1995, pp. 56–58.

[4] J. Bischoff, Achieving warehouse success, Database Programming and Design (1994) 27–33.

[5] B. Bowman, G. Davis and J. Wetherbe, Three stage model of MIS planning, Information and Management 6, 1993, pp. 11–25.

[6] A.C. Boynton and R.W. Zmud, Information technology planning in the 1990's: Directions for practice and research, MIS Quarterly 12(1), 1987, pp. 59–71.

[7] M. Chen, A model-driven approach to accessing managerial information: A repository-based executive information system, Journal of Management Information Systems 11(4), 1995, pp. 33–63.

[8] A. Delbecq, A.H. Van de Hen, D.H. Gustafson, Group techniques for program planning: A guide to nominal group and Delphi processes, Scott Foresman and Co., Glenview IL, 1975.

[9] D. Goodhue, L. Kirsch, J. Quillard and M. Wybo, Strategic data planning: Lessons from the field, MIS Quarterly 16(1), 1992, pp. 11–34.

[10] D. Goodhue, J. Quillard and J. Rockart, Managing the data resource: A contingency perspective, MIS Quarterly 12(3), 1988, pp. 373–394.

[11] R. Hackathorn, Data warehousing energizes your enterprise, Datamation 41(2), 1995, pp. 38–45.

[12] J.C. Henderson and J.G. Sifonis, The value of strategic IS planning: Understanding consistency validity, and IS markets, MIS Quarterly 12(2), 1988, pp. 187–199.

[13] W. Inmon, Building the Data Warehouse, QED Technical Publishing Group (1992).

[14] R. Kimball and K. Strehlo, Why decision support fails and how to fix it, Datamation 40(11), 1994, pp. 40–43.

[15] A. Lederer and V. Sethi, The implementation of strategic IS planning methodologies, MIS Quarterly 12(3), 1988, pp. 373–394.

[16] T.J. Lincoln, Information systems constraints – A strategic view, Information Processing: Proceedings of the IFIP Congress, IFIP Congress (1980) 907–911.

[17] C.C. Marshall, Frank M. Shipman and R.J. McCall, Making large-scale information resources serve communities of practice, Journal of Management Information Systems 11(4), 1995, pp. 65–86.

[18] R. Mirani and W. King, Impacts of end-user and information center characteristics on end-user computing support, Journal of Management Information Systems 11(1), 1994, pp. 141–166.

[19] K. Orr, Data warehouse technology, Information Builders White Paper (1995) 1–21.

[20] K. Parsaye, The sandwich paradigm, Database Programming and Design (1995) 50–55.

[21] A. Radding, Support decision makers with a data warehouse, Datamation 41(5), 1995, pp. 53–56.

[22] Software AG Technical Literature, The decision maker's goldmine: The data warehouse, Datamation 41(5)(1995)s6-s13.

[23] C. White, The key to a data warehouse, Database Programming and Design (1995) 23–25.

![](/api/attachments/K5CY6RWX/fulltext/images/2ec82d5bb97078c54c0529aa33781199478d8baaafbaa95fbf624e2f350c783a.jpg)  
Ashok Subramanian is an Associate Professor of Management Science and Information Systems at the University of Missouri, St. Louis. Dr. Subramanian has a Ph.D. in Management Information Systems from the University of Houston. His research interests include Telecommunications technologies, applications, and policies; distributed computing technologies such as client-server comput-

ing; object oriented systems development; and computer personnel issues such as productivity. He has worked as a consultant in the areas of open system architecture development; the development of corporate standards, policies, and procedures for managing corporate computer networks. His papers have appeared in Information and Management, Omega, and the Journal of Information Technology Management.

![](/api/attachments/K5CY6RWX/fulltext/images/c420f1af7aa6606fa63ecbb2dd2cdaed75c0931d8c1d30fd1e94f8232b73ed12.jpg)

L. Douglas Smith is Professor of Management Science and Information Systems and Director of the Center for Business and Industrial Studies at the University of Missouri - St. Louis. He holds a Ph.D. in Management Sciences from the University of Minnesota and an M.B.A. and B.Sc. (Physics) from McMaster University. Smith's previous IS articles have appeared in MIS Quar-

terly, JMIS, Decision Sciences, Information and Management, Omega, and INFOR. His research has emphasized the development of models and computer-based systems for the solution of managerial problems.

![](/api/attachments/K5CY6RWX/fulltext/images/febcd19eadf10715ba993661553335fddc4d101b4966f7ede5bfe835f7fc6c7b.jpg)

Anthony C. Nelson is an Assistant Professor of MIS in the University of South Florida. He received his Ph.D. in MIS from the University of Pittsburgh's Katz Graduate School of Business in 1991, and BS in Management from the North Carolina A&T State University in 1980. He has held IS positions with several large manufacturing and banking firms, and has performed consulting work for city governments, IS consulting firms, and small businesses. His current research interests include IS personnel issues, CASE technology impacts, and IT implementation and diffusion. His papers have appeared in the Journal of Information Technology Management, Interfaces, and Information and Management.

![](/api/attachments/K5CY6RWX/fulltext/images/cabc8db2cf250246715d7e2166723eecc86d664dc86aa69509957be95a8a55aa.jpg)

James Campbell is an Associate Professor of Management Science & Information Systems in the School of Business Administration at the University of Missouri - St. Louis. He received his Ph.D. in Operations Research and Industrial Engineering from the University of California - Berkeley. His research interests include decision support systems, geographic information systems, and mathematical modeling of

problems in transportation, location and logistics. His publications have appeared in Operations Research, European Journal of Operational Research, and Transportation Research.

![](/api/attachments/K5CY6RWX/fulltext/images/edf801ff5ec677902826ddd30a411a5be563773f2d1276c96bee599d96c929b5.jpg)

David Bird is Instructor of Management Information Systems at the University of Missouri - St. Louis. Mr. Bird holds a M.S. in Applied Mathematics and Computer Science from Washington University in St. Louis. His work has been published in INFOR, Journal of Systems Management, Journal of Educational Data Processing, and Decision Sciences. His research interests are in the development of decision

support systems for scheduling and dispatching.
