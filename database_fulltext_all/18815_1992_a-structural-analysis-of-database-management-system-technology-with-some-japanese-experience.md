---
otero_id: 18815
otero_key: "NFBU3NU7"
title: "A structural analysis of database management system technology with some Japanese experience"
authors: "Yoichi Hayashi; Hideto Ikeda"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90030-j"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# A structural analysis of database management system technology with some Japanese experience

Yoichi Hayashi

Ibaraki University, Ibaraki, Japan nization, Information resource management, System evaluation.

Hideto Ikeda

Information Processing Center, Hiroshima University, Hiroshima, Japan

This paper proposes a categorization scheme for database management system (DBMS) technology. It also defines the context and technologies of DBMS, which consists of technologies related to (1) Organization and personnel training, (2) Hardware and software, (3) Data management, (4) User services, and (5) Evaluation. The paper, then analyzes the current status and problems of DBMS in Japan, within this framework. The data is based on results derived through postal questionnaires, a sample of a cross section of 218 data processing communities in industrial, financial, educational and governmental organizations and in-depth interviews. Finally, the authors consider the future DBMS technology.

Keywords: Database management, DBMS, Data administration, Data management, Database systems, Operational orga-

![](/api/attachments/NFBU3NU7/fulltext/images/aedf1f920bf14fae8c9ec0920520318d97a250d39678819c9b8b4d6e54a57f1d.jpg)

Yoichi Hayashi is an Associate Professor of Computer and Information Sciences at Ibaraki University. He received his B.E. in Management Science, and his M.E. and Ph.D. in Systems Engineering from the Science University of Tokyo in 1979, 1981 and 1984, respectively. He joined Ibaraki University as an Assistant Professor in 1986 and was a visiting professor at the University of Alabama at Birmingham from 1990 to 1991. He has published many papers in academic journals in the fields of Computer and Information Sciences. His current research interests include database system management, distributed database systems, parallel processing, AI, neural networks, expert systems, fuzzy logic and pattern recognition. He is a member of IEEE, ACM, AAAI, INNS, SCS, NAFIPS, IPSJ, IEICE, and others.

Correspondence to: Y. Hayashi, Department of Computer and Information Sciences, Ibaraki University, Hitachi-shi, Ibaraki 316, Japan. Tel.: (+81) 294-34-3254.

## 1. Introduction

Because of the growing use of Database Management Systems (DBMS), many different types and products have been developed in industry, government, universities, etc. A large quantity of data is currently stored and controlled in them. The expansion of the size of the databases and the number of DBMS applied fields attracts interest in their operation and administration. Some leading organizations which incorporated DBMS into their data processing operation at an early stage have accumulated experience in managing it. Their approach and general concepts have gradually been recognized and adopted in many organizations. However, their systematic operation and administration is still often a problem.

![](/api/attachments/NFBU3NU7/fulltext/images/04e10512d380ffe3ceffebdbd1537b1be9a26a82b002e1d568650263ade4cdb1.jpg)

Hideto Ikeda is an Associate Professor at Information Processing Center of Hiroshima University and acted as the Vice-Director. He recieved his Doctor of Science from Faculty of Science, Hiroshima University by the research on Combinatorial File Organization Schemes. He published research papers on database systems, especially, physical file organization, library automation systems, medical information systems, office automation systems, multimedia information systems, user interfaces and fourth-generation languages. He also directed the development of practical database systems, e.g., library automation systems of Tsukuba University, Hiroshima University, Hospital Automation system of Hiroshima University Hospital, Finance Information Systems of the National Bank of Japan. His current research interests focus on establishing a new data model and user-interface to support multi-media information systems.

When assessing the value of a database system, users are the only people who can provide a true measure of effectiveness. In this sense, it is extremely important to organize concepts and technologies systematically in a way that transcends the individual organization. The idea of Data Administration has been discussed since the early 1970's [10,32]. There has also been a great deal of work on the management aspects of database systems from an operational or organizational perspective; i.e. issues other than purely technical or conceptual ones [12,18,29,33,35]. However, the DBMS technology framework has not yet been fully investigated. There is a lack of published surveys on how and why the database approach and its technology is utilized.

We first describe the necessity to categorize DBMS technology and define the context and our framework. These technologies are roughly classified into five kinds related to (1) Organization and personnel training, (2) Hardware and software, (3) Data management, (4) User services, and (5) Evaluation.

Second, we analyze the current status and problems of DBMS use in Japan within the proposed framework of DBMS technology. The data is based on results derived through a mixture of postal questionnaires and in-depth interviews with selected organizations. The questionnaire was designed according to each subject in the framework of DBMS technology and was sent out to EDP managers of 1500 Japanese organizations in 1985: these organizations were considered to be likely to have a database administration department or section and were selected at random from data processing communities in industrial, financial, educational and governmental organizations. A total of 218 returns (14.5%) was obtained. Considering the nature of postal questionnaires, this seemingly low rate of return is reasonable.

![](/api/attachments/NFBU3NU7/fulltext/images/90e1bb64d80c85c146259a6921d9edda8003625b121e6fa833459ee4ad091ea1.jpg)  
Fig. 1. Life-cycle of database systems

Databases in Japanese organizations in 1985 were sometimes treated in much the same way as application data files, and the DBMS was used as just a sophisticated new file access and management method. In fact, Jardine [21] pointed out that an unthinking excursion into the database world without the proper analysis of data, data relationships, and data value can be dangerous. We believe that the highly focused nature of this survey may have led to a lower rate of response than a general DBMS survey for which the user is not required to possess a great deal of experience in DBMS.

## 2. Categorization of database management system technology

## 2.1 Necessity of categorization

In the past ten years, the use of data dictionary systems (DDS) $[1,7,28]$ and information resource management systems (IRMS) $[20,23,24]$ have been accepted and the products were developed. These are tools that help database administrators (DBA) improve control, management, and documentation of information systems. They also support the project management and system design processes. However, a DBA still has many difficult problems which are not solved by means of the DDS and/or the IRMS. Further, IRM is still too new and too big to have significant success stories. Those assigned to it do not always enjoy broad support of a large organization. In a sense, the potential customers do not understand they are the beneficiaries of a successful IRM program. Therefore any action towards implementation should include a strong initializing education process.

Categorization of various technologies related to DBMS is necessary to grasp the essentials of DBMS as a common theme. The categorization enables a DBA to investigate intentionally and effectively the current status of DBMS. It also allows potential users of DBMS technology to find means of determining the problems and to evaluate their future system on effectiveness before implementation. Furthermore, a framework of DBMS technology is useful in structuring textbooks or manuals to train people in the use of DBMS, and the categorization shows where there may be technical problems and suggests how the technologies may be improved.

## 2.2 Context of database management system technology

In this paper, we consider the life-cycle of a database system, as shown in Figure 1, to consist of three stages for planning, development, and operation.

The planning stage includes all work to be done first. The development stage involves work necessary to prepare all information resources, e.g., hardware, software, data, organization, rules, operation manuals, and personnel training. The planned system is sometimes a second or third generation system, with a current one still operational. In this case, migration from the current system to the new one is included in this stage. The operational stage consists of work performed after the system is installed. System monitoring and evaluation are important tasks that must be performed in this stage. System modification or maintenance is usually initiated of the evaluation shows that the operation is incorrect or inefficient.

## 2.3 Domain of database management system technology

We first specify the domain of technologies that are useful for effective and efficient DBMS. Every technology needed in the operational stage is included in the domain, but some others are required in the planning or the development stage to realize an effective and efficient system. A system is often modified or integrated with other systems on the basis of evaluations performed in the operational stage. For easy modification of the system, there are some technologies required in the operational stage. From the viewpoint of the database system life-cycle, we define the domain of DBMS technologies as those technologies for efficient and effective operation in the planning, development, operational, and modification stages.

## 2.4 Structural analysis of database management system technologies

We categorize DBMS technologies as shown in Figure 2. Figures 3–7 illustrate each of the domain technologies. Use of these technologies were investigated empirically in Japan. A brief description of each domain technology follows.

## (1) Technology for organization and personnel training

This category includes every technology dealing with the organization and EDP personnel aspects that provide effective and efficient DBMS. The organizational structure establishes the system management divisions/sections and each task is assigned to the appropriate section. Staff are assigned to sections and trained, within a policy dedicated to advancement and personnel change.

## (2) Technology for management of hardware and software

This category contains technologies related to hardware and software. It includes operations to select, design, confirm, develop and use the hardware/software tools. This category contains all methodologies that can be used for efficient management.

![](/api/attachments/NFBU3NU7/fulltext/images/812edf2f8d4b81a3c989cb9977b4ebdc994e7abf4a1474a4bbd45423ec40abe4.jpg)  
Fig. 2. General view of database management system technology

## (3) Technology for data management

The database is the most important component of a database system in the organization. The most DBMS must be able to store data in a timely manner at minimum cost, maintain data security and integrity, recover data if it is destroyed, access data easily, quickly and flexibly, and reduce storage space. All these functions are classified as part of this category.

## (4) Technology for user services

These technologies support realization of a desirable database system for end-users and help them use it. A system will have three characteristics: flexibility, operability and reliability. Public relations activities, training of end-users, and establishing the charge-back system are important parts of end-user support. These activities are often promoted by the information center (IC) [2,5,6,11].

## (5) Technology for system evaluation

Each of the above information resources (organization, staff, hardware, software, data and end-user) can be evaluated independently. Technologies for each of these independent evaluation are classified in each of the corresponding categories. However, the database system should be evaluated on the whole, because it fulfills some functions by the joint effort of two or more resources. Technologies that can be applied to such whole system evaluations are shown in Figure 7.

## 3. Current status in Japan and problems of DBMS use

Here, we will provide some of the major highlights in our study of the current status and problems of DBMS use in Japan $[13]$ , and analyze these problems within the framework of DBMS technologies. Technical problems of database systems are well understood, but in real DBMS use, there are relatively few of these. The main problems involve people and management.

A survey of 218 database using organizations in Japan highlights some of these problems and indicates how to provide more successful DBMS applications. Almost all respondents (93.5%) were in charge of an EDP division, and/or a system design division, and/or a database management division.

3.1 Operational organization and personnel training

## (1) Organizational structure

The organization of the group that implements the system using the DBMS may be classified into three types: (a) those structured with emphasis on the DB system life-cycle (planning section, development, etc.); (b) those structured according to the data management (e.g. data input division, data administration, and data user group); (c) those having emphasis on their operating function, e.g., for the personnel department or accounting/financial division. Approximately 70% of the 214 organizations are of type (c). See Table 1. On the other hand, about 9% are of type (b).

The relationship between database systems organization and the overall organizational structure is fragmentary and mixed. The organizational structure typology proposed by Mintzberg $[26,27]$ has been used in a number of research studies. According to this typology, many of the organizations responding were of type “Machine Bureaucracy” or “Divisionalized Form A”. The former structure is naturally associated with mass production technology: e.g., large automobile, airline, and steel companies. The second structure is a market-based set of divisions that are decentralized from the perspective of the overall organization, but centralized within a division. Examples of this type of organization are usually found in the private sector of an industrialized economy-e.g., the vast majority of the Fortune 500.

Generally, database systems to support major business functions are first constructed. Therefore, organization of type (c) become a majority.

![](/api/attachments/NFBU3NU7/fulltext/images/2e4fca7fac2e420d47ce9600e76d7334427a193b27da0ee3ba82f3f48293f84a.jpg)  
Fig. 3. Technology for organization and personnel training

Furthermore, most organizations responding were of type “Divisionalized Form A”.

(2) Separation of development and operation of database systems

The relation between development, operation, and maintenance of the DBMS applications has always presented organizational problems for DBMS managers. Table 2 shows that 81 organizations of the 218 respondents (37.2%) separate their sections into development, operation and maintenance groups. There are real technical difference in the skills needed for development, operation, and maintenance. In separated situation, we must pay attention to motivation of the operation staffs, as these tend to seem loving jobs.

The reason why many organizations do not separate into three groups appears to be associated with the problems associated with maintenance work and unexpected overruns. In a non-separated situation, some potential problems may occur:

\- Personnel turnover increases to the point where it becomes troublesome.

\- It becomes difficult to produce easy-to-understand documents for operation and maintenance.

\- Implementation of database systems applications often depend on individuals who are otherwise engaged (e.g., in operation and/or maintenance work).

## (3) Personnel training

Staff training is divided into four groups of courses as follows:

\- basic concepts of database systems.

(46–69%)

\- special needs for on-line systems.

(31-41%)

![](/api/attachments/NFBU3NU7/fulltext/images/51836aa9f3d79cb58dac02eecf0c5e06f4380a11411473940eea960c7defe78f.jpg)  
Fig. 4. Technology for management of hardware and software

\- Operation of database systems.

(15–29%)

End-user support and query languages.

(8-14%)

Among these groups, the current interest in end-user support is not especially high. Moreover, only 8.3% of 218 organizations expressed interest in data gathering/entry.

## (4) Personnel improvement

Table 3 indicates the level of personnel change from the operation division to the end-user division and vice versa. Thirty-five percent of the 197 organizations adopt a policy encouraging change. Such personnel movement effectively transfers end-users requirements to the operation division. However, a merely 2% of the organizations responding have a policy of periodic personnel movement between operations and end-users divisions. This suggests some difficulty in personnel change.

Personnel moved from the development division transfer software development knowledge. However, periodic moves from the operation division to the development division are only performed in 5.6% of the 197 organizations. Aside from a few executives, such as the Vice President of the EDP division, almost all managers and staff in the EDP division have few personnel moving to other divisions. In particular, DBAs and the IC staffs are viewed as highly qualified but they are not often recognized in the formal EDP personnel system. Therefore, their career path to general manager is limited and their chances of promotion are uncertain. This may be due to the special technology base and short history (say 30 years) of the EDP division. Generally, the EDP division is unsociable.

![](/api/attachments/NFBU3NU7/fulltext/images/fc7cd0d80878658c2d791ba301143c562773360d0f2ea1e0033a7a22e617346c.jpg)  
Fig. 5. Technology for data management

## 3.2 Hardware and software to manage database systems

## (1) Operating system

The results from the survey show that 81.6% of the organizations have no interest in operating systems, that is, the operating system has been unchanged since it was initially installed by the vendor. On the other hand, 10.6% of the operating systems were generated and tuned using a standard system generation strategy. Needless to say, maintenance changes involving tuning of the DBMS are better managed by the vendor, who knows the system much better than the EDP staff. Organizations using DBMS generally must employ experienced system programmers who are familiar with the system. However, knowledge of

DBMS by EDP personnel and/or user support by the vendor is not sufficient for tuning tasks.

Organizations which modify the DBMS to enhance its efficiency are considerably rarer (5.0%). DBMS packages typically augment or modify the access mechanisms of the operating system.

## (2) DBMS and host languages

Table 4 suggests that almost all organizations use standards interfaces, i.e., they do not want to leave the choice of interfaces and access methods to programmers. On the other hand, data maintenance and productivity of software production staff concern a majority of the organizations. The users who have standard user interfaces belong to one of three groups:

\- The first selects standard facilities for interfaces developed from components of DBMS; they then insist that programmers use them. The standard includes specification of access paths, data schema and the order of instructions; it also requires limited use of utilities and commands supported by the DBMS.

![](/api/attachments/NFBU3NU7/fulltext/images/4f30377eb1abe344dfd51e2c75f1a039f268a178b93ec2d5abe04cb6da33fe78.jpg)  
Fig. 6. Technology for user services

\- The second develops special facilities that ensure independence of the application programs from the underlying DBMS. This allows the replacement of an underlying DBMS with only small changes to the interface programs.

\- The third develops interfaces using the tools of the DBMS or of the host languages and utilizes them to reduce the redundancy of developed programs. For example, some interfaces to COBOL programs are cataloged in the library and can be called out by a program.

## (3) Utility programs and user commands

Table 5 shows that utility programs are enhanced by 31.1% of the organizations and that limited work with utilities and user commands are second in popularity at 28.9%. Since user commands have various functions to aid both end-users and DBA, this seems reasonable.

Sibley [34] has discussed the implication and scope of standardization of the field of database systems, especially user interfaces, end-user, system maintainer, and administrator needs. He has also considered what parts should be standardized.

## (4) Other considerations

A data dictionary/directory (DD/D) is used in 27% of the organizations. Recently, it has been popularized as a tool for the database system management.

Active data dictionary systems, which are automated and integrated into the DBMS, are sometimes difficult to manage and use. EDP organization must make a major commitment of necessary resource when they decide to acquire and manage a DDS. Ideally, the data administration team should include data dictionary specialists.

![](/api/attachments/NFBU3NU7/fulltext/images/15b11fb81f323ac83d35de4423427bb1eb19597f94915b09ca717bb47d7ddeae.jpg)  
Fig. 7. Technology for system evaluation

Table 1  
Organizational structure of database management.

<table><tr><td>Grouping policy</td><td>No. of firms</td><td>% (N = 214)</td></tr><tr><td>Divided into groups corresponding to the structure of information user divisions, that is, Personnel, Accounting, Finance and technical literature, etc.</td><td>146</td><td>68.2</td></tr><tr><td>Divided into groups by technical functions of database management, that is, key puncher, database manager, programmer, etc.</td><td>20</td><td>9.4</td></tr><tr><td>Organized with another policy.</td><td>48</td><td>22.4</td></tr></table>

## 3.3 Data management

## (1) Quality control of data

A majority (71.6%) of the 211 organization consider data quality in the development stage (See Table 6). About one half of the organizations develop special application programs in order to reject invalid data. 27% of the respondents used integrity control functions originally supported in the DBMS. Since these functions are generally insufficient to preserve validity and consistency of data, special application program are required.

In fact, Honkanen [19] has examined three major DBMSs, IBM's DB2 (SQL/DS), Cullinet's IDMS/R, and Cincom's Supra to determine how integrity is being solved. Unfortunately, presentation of integrity is still a major problem. The data value, entity, and referential integrity problems were examined. System enforcement of data value integrity in DB2 and IDMS/R is limited to ensuring that the input value is consistent with the stated data type. Both DB2 and IDMS/R require DBA intervention for the support of referential integrity. Further both IDMS/R and Spura require user defined null values.

Table 2  
Separation of development and operation.

<table><tr><td>Organization structure</td><td>No. of firms</td><td>% (N = 218)</td></tr><tr><td>Separated</td><td>81</td><td>37.2</td></tr><tr><td>Not separated</td><td>130</td><td>59.6</td></tr><tr><td>Neither</td><td>7</td><td>3.2</td></tr></table>

## (2) Security control

Table 7 shows that passwords are used to control security in most responding organizations. Assignment of DBAs to the problem of maintaining security control and retaining audit trails of database transactions is performed in less than 30% of the organizations. Specification of rules on security is found in a minority of the 206 organizations, suggesting that systematic control of data security is not adequate.

The DDS can be used as an audit tool in all phases of the database systems development lifecycle. The number of organizations using DDS (58, See 3.2-(4)) approximately coincides with the number of organizations using audit trails of database transactions.

The EDP auditor is also concerned with manual internal controls; for example, access control over tapes or disk packs are manual controls. It is not uncommon for the EDP auditor to use procedure and policy manuals, as well as to document manual controls. DDS can be useful for maintaining the documentation associated with manual internal controls. In this sense, it is expected that the number of DDS users will increase.

Table 3  
State of personnel changes.

<table><tr><td rowspan="3">Division which accepts personnel exchanges with operation division</td><td colspan="6">State of personnel change</td></tr><tr><td colspan="2">Periodic</td><td colspan="2">Non-periodic</td><td colspan="2">No exchange</td></tr><tr><td>No.</td><td>%</td><td>No.</td><td>%</td><td>No.</td><td>%</td></tr><tr><td>End-user division</td><td>4</td><td>2.0</td><td>65</td><td>33.0</td><td>128</td><td>65</td></tr><tr><td>Development Division</td><td>11</td><td>5.6</td><td>96</td><td>48.7</td><td>90</td><td>45.7</td></tr><tr><td>Others</td><td>3</td><td>1.7</td><td>57</td><td>32.4</td><td>116</td><td>65.9</td></tr></table>

Table 4  
Interfaces with DBMS.

<table><tr><td>Approach to develop interfaces</td><td>No. of firms</td><td>% (N = 214)</td></tr><tr><td>Some standard facilities of DBMS are used</td><td>83</td><td>38.8</td></tr><tr><td>Special facilities are developed</td><td>64</td><td>29.9</td></tr><tr><td>Standard interfaces are cataloged by DBA and used (e.g. copy phrase)</td><td>35</td><td>16.4</td></tr><tr><td>Others</td><td>32</td><td>14.9</td></tr></table>

## (3) Database recovery

Almost all organizations (90.2%) keep backup copies of data. Approximately 60% of the organizations also make use of database recovery facilities other than those in the DBMS. Special recovery programs are developed by 10% of the respondents. About a quarter of the organizations have had experiences where it was necessary to recover crashed data by recovery of the database from a dump. However many current DBMSs have not yet provided completely satisfactory data recovery procedures.

## (4) Database system integration

Table 8 shows that about 90% of the organizations feel that they need system integration. However, only 14.5% of the organization actually implement it.

Generally, the integration of heterogeneous database systems that are currently in operation is difficult because:

\- There is no commercial DBMS that can support every application system without reducing functionality and performance. The current commercial DBMS's were designed with old hardware architectures in mind and thus cannot be easily altered to take advantage of newer hardware.

Table 5  
Use of utility programs and user commands.

<table><tr><td>Approach</td><td>No. of firms</td><td>% (N = 190)</td></tr><tr><td>Original development by users</td><td>17</td><td>8.9</td></tr><tr><td>Installed by vendors and enhanced by users</td><td>59</td><td>31.1</td></tr><tr><td>Limited use of utilities and user commands that are supported by DBMS or OS</td><td>55</td><td>28.9</td></tr><tr><td>Others</td><td>59</td><td>31.1</td></tr></table>

Table 6  
Quality control of data.

<table><tr><td>Approach</td><td>No. of firms</td><td>% (N = 211)</td></tr><tr><td>Use integrity control functions originally supported in DBMS</td><td>57</td><td>27.0</td></tr><tr><td>Develop special application programs to reject invalid data</td><td>107</td><td>50.7</td></tr><tr><td>Consider data quality control in the development stage</td><td>151</td><td>71.6</td></tr><tr><td>Organize special data verification groups</td><td>34</td><td>16.1</td></tr><tr><td>Train end-users and data entry personnel</td><td>61</td><td>28.9</td></tr><tr><td>Others</td><td>6</td><td>2.8</td></tr></table>

\- It is very difficult to implement the development environment, e.g., hardware, software and manpower.

\- Integration cost exceeds the expected benefit of integration.

\- It is difficult to control very large applications using database systems.

\- Because of lack of understanding and commitment by top management, the controls needed for integrated system development are not properly implemented, or are subverted by allowing exceptions without understanding their consequences.

## 3.4 User services

## (1) Users needs

Table 9 tabulates the needs of end-users. More than half of the organizations listed quick response for database access, easy-to-use end-user

Table 7  
Methods for data security.

<table><tr><td>Methodology</td><td>No. of firms</td><td>% (N = 206)</td></tr><tr><td>Control by password</td><td>159</td><td>77.2</td></tr><tr><td>Assignment of DBAs</td><td>51</td><td>24.8</td></tr><tr><td>Cryptographic coding of data</td><td>10</td><td>4.9</td></tr><tr><td>Manual auditing of database</td><td>8</td><td>3.9</td></tr><tr><td>Audit trails of database transactions</td><td>61</td><td>29.6</td></tr><tr><td>Specification of security control rules</td><td>38</td><td>18.4</td></tr><tr><td>Others</td><td>27</td><td>13.1</td></tr></table>

Needs of end-users.  
Table 8  
Database system integration.

<table><tr><td>Methodology</td><td>No. of firms</td><td>% (N = 214)</td></tr><tr><td>Integration has never been attempted although we think it necessary</td><td>86</td><td>40.2</td></tr><tr><td>One database was initially designed as an integrated system</td><td>22</td><td>10.3</td></tr><tr><td>Almost all major databases have already been integrated</td><td>9</td><td>4.2</td></tr><tr><td>A portion of the databases have been integrated</td><td>71</td><td>33.2</td></tr><tr><td>We do not think it necessary</td><td>17</td><td>7.9</td></tr><tr><td>Others</td><td>9</td><td>4.2</td></tr></table>

language and data independence as important requirements of end-users. These characteristics have direct effects upon the design and choice of the DBMS. On the other hand, interests of programmers who are in charge of application development are summarized in Table 10. According to the survey, 68.4% of the organizations think that logical database models are important for programmers. It is necessary to understand how logical database models reflect the real world. In general, such understanding of the logical database models has strong influence on the productivity of software. About half of the organizations also listed user interface of DBMS as an important interest of programmers.

<table><tr><td>Needs</td><td>No. of firms</td><td>% (N - 213)</td></tr><tr><td>Availability of database anytime, anywhere</td><td>96</td><td>45.1</td></tr><tr><td>Data independence (Logical structure of databases is independent of physical organization)</td><td>113</td><td>53.1</td></tr><tr><td>Flexible formatting of results</td><td>83</td><td>39.0</td></tr><tr><td>Help-capabilities for end-users</td><td>36</td><td>16.9</td></tr><tr><td>Easy-to-use documentation</td><td>56</td><td>26.3</td></tr><tr><td>Retrievals with inference functions</td><td>20</td><td>9.4</td></tr><tr><td>Capability for ad hoc retrieval</td><td>83</td><td>39.0</td></tr><tr><td>Capability for database updating from terminals</td><td>70</td><td>32.9</td></tr><tr><td>Quick response for database access</td><td>133</td><td>62.4</td></tr><tr><td>Easy-to-use end-user language</td><td>114</td><td>53.5</td></tr><tr><td>Data processing capability from terminals</td><td>56</td><td>26.3</td></tr><tr><td>Image data processing capability</td><td>26</td><td>12.2</td></tr><tr><td>Integration with office automation systems</td><td>73</td><td>34.3</td></tr></table>

Table 10  
Interests of programmers.

<table><tr><td>Interest</td><td>No. of firms</td><td>% (N = 209)</td></tr><tr><td>Logical database model (relational, network, hierarchical)</td><td>143</td><td>68.4</td></tr><tr><td>User interface of DBMS (Host language, Report generator, etc.)</td><td>107</td><td>51.2</td></tr><tr><td>Fourth generation language (4GL)</td><td>58</td><td>27.8</td></tr><tr><td>Intelligent terminals (Screen editor, local processing capability, etc.)</td><td>56</td><td>26.8</td></tr><tr><td>System resources (Processing capability, storage capacity, etc.)</td><td>76</td><td>36.4</td></tr><tr><td>Others</td><td>3</td><td>1.4</td></tr></table>

We also investigated interest in fourth-generation languages (4GL) [25] such as Natural, Mapper, and Focus. Table 11 shows the ratios of organizations who feel that 4GLs are important. Generally, interest in the 4GL is not yet very high, as shown in Table 10.

However, users of DBMS supplied by independent vendors, e.g., ADABAS, MODEL204, TOTAL are interested in 4GL (33% of all DBMS users). The 4GL is one of the most important tools of the Information Center and end-user computing (EUC) [4,30,31]. EUC has been defined as a process and/or an environment in which the user develops applications. The importance of the participative approach, such as the IC and the EUC, had not been recognized in Japan by 1985. In fact, Rockart and Flannery have concluded that “end-user computing is still poorly understood; the majority of research on the EUC has been a mass of exhortative literature and occasional case studies.” We believe that this conclusion is still applicable in many Japanese organizations.

On the other hand, the American Management Association estimated that by 1985 one third of all American firms had implemented an IC. When the AMA polled 295 companies in 1988, 58 percent had a discrete unit that supported the EUC [3]. These statistics show that the spread of the EUC in general and the IC in particular has been extremely rapid in the U.S.

Table 11  
DBMS-user interest in 4GL.

<table><tr><td colspan="9">DBMS (%)</td></tr><tr><td>IMS</td><td>ADABAS</td><td>TOTAL</td><td>DMS</td><td>ADM</td><td>PDM</td><td>ADBS</td><td>IDS</td><td>AIM</td></tr><tr><td>18.6</td><td>32.5</td><td>33.3</td><td>22.2</td><td>23.5</td><td>11.8</td><td>9.5</td><td>8.3</td><td>10.3</td></tr></table>

(2) Charging for database use

The survey showed that 115 of the 211 organization have not established a charge-back policy for database use. It seems that database management cost are budgeted as part of the whole EDP cost (and thus as overhead). In cases where a charge-back system is adopted, 58 of the remaining 96 organizations charge cost according to amount of hardware resources used. In some cases, non-EDP divisions share the whole cost for database system management (4.3%): then cost for database use is treated as a general and administration (G & A) expense.

Charge-back policy is often inconsistent in assigning the overhead and operating costs for data base system use in different departments and/or divisions of a company. For example, some systems and programming departments are considered to be a part of the total corporate overhead. In such a case, internal database system development is essentially cost free. On the other hand, a software purchase is sometimes treated as a direct cost billable to the department requesting it. Exploratory research on the IC by Carr has reported that all firms surveyed support the Cost of the IC staffs and public facilities via overhead accounts. The provision of such free accounts is a moot point.

## 3.5 System evaluation

## (1) Evaluation activity

Approximately 60% of the organizations do not perform system evaluation. Periodic or nonperiodic evaluations are executed by 10.7% and 29.9% of the organizations respectively. 87 organizations execute system evaluation.

Table 12  
Purposes of evaluation.

<table><tr><td>Purpose</td><td>No. of firms</td><td>% (N = 87)</td></tr><tr><td>Monitoring use of database</td><td>72</td><td>82.8</td></tr><tr><td>Cost performance</td><td>17</td><td>19.5</td></tr><tr><td>Monitoring use of hardware resources</td><td>55</td><td>63.2</td></tr><tr><td>Others</td><td>6</td><td>6.9</td></tr></table>

## (2) Purposes of evaluations

Table 12 shows the reasons organizations give for performing evaluations. There are mainly to monitor the use of database and hardware resources.

The evaluations cover the overall items of database system management. Almost all items occur in the operational stage as follows:

\- Effectiveness of database use

\- Utilization of DASD

\- Average response times

\- Access efficiencies

\- Utilization rate of hardware resources

\- Utilization rate and error rate for each command

\- Troubleshooting

## (3) Group performing evaluation

Table 13 shows that most evaluators (67.8%) are part of the staff inside the organization. They are part of in-house evaluation teams that are organized as a regular or irregular project. The special team usually consists of DBAs, EDP-personnel, etc. There are a few (1.2%) organizations who contract for evaluation by outside experts or consultants. The remaining 27 organizations listed the DBA, the EDP division, the system development division, etc. as evaluators. Indeed, Sibley has suggested that the DBA has the dual responsibility of guiding the acquisition of DBMS software and providing a foundation system on which to build future applications [35].

Table 13
Evaluators.

<table><tr><td>Evaluators</td><td>No. of firms</td><td>% (N = 87)</td></tr><tr><td>In-house evaluation team established</td><td>31</td><td>35.6</td></tr><tr><td>Special project organized as required</td><td>28</td><td>32.2</td></tr><tr><td>Outside experts or consultants</td><td>1</td><td>1.2</td></tr><tr><td>Others</td><td>27</td><td>31.0</td></tr></table>

Table 14
Difficulty of evaluation activity.

<table><tr><td>Difficulty</td><td>No. of firms</td><td>% (N = 189)</td></tr><tr><td>Evaluation of Cost</td><td>14</td><td>7.4</td></tr><tr><td>Establishing evaluation standards</td><td>123</td><td>65.1</td></tr><tr><td>Effective evaluation methods are unknown.</td><td>40</td><td>21.2</td></tr><tr><td>Establishment of evaluation objectives</td><td>65</td><td>34.4</td></tr><tr><td>No effective approach</td><td>20</td><td>10.6</td></tr><tr><td>No interest in evaluation</td><td>31</td><td>16.4</td></tr><tr><td>Others</td><td>11</td><td>5.8</td></tr></table>

## (4) Difficulty of evaluation activity

Table 14 shows that 65% of the organizations point out difficulties in establishing evaluation standards. Stating the objectives is second in difficulty, according to 34.4% of the organizations. On the other hand, only 16.4% of the organization have no interest in evaluation.

A crucial question, that is often overlooked in the debate among the various DBMS technologies, is “Who is the user of a DBMS?” As each end-user is concerned with how well the application system meets his or her needs and how much their specific query will cost, an evaluation standard is difficult to establish.

## 4. Future technologies in DBMS

There are still a number of problems to be solved in DBMS technology. Although new approaches and software such as the IC, IRM, EUC, DDS and 4GL, have been proposed, their value and effectiveness has not yet been established in real organizations. We believe DBMS technologies deserve research attention as follows:

## (1) Multimedia database management technology

It is desirable to develop a DBMS that can manage various types of data, e.g., graphics, image, spatial, voice, character, and numeric data. There is a need for storing large (several megabyte) bit string of images in a DBMS. Spatial applications are typically found in geographical databases containing encoded information such as that found on maps.

There are few researchers investigating better end-user interface to multimedia databases or application development tools. But, spreadsheets, WYSIWYG interfaces, Hypercard, etc. have caused a revolution in human interfaces.

Computer Aided Software Engineering (CASE), Computer Integrated Manufacturing (CIM) and spatial applications need new kinds of object types. It is expected that extendible DBMSs and object-oriented DBMS $[8,22]$ can provide powerful tools. But, the real problem is that “object-oriented” means many different things. It is assumed, however, that the terminology will stabilize and some coherency of system goals will emerge.

## (2) System integration technology

Some organizations have already integrated database systems with word processors and personal computers. In addition to the integration of heterogeneous database systems, integration with telephone, facsimile, videotex, and other software will also be effective as a means of promoting better understanding between divisions as well as effective and efficient DBMS usage.

## (3) System migration technology

It is expected that DBMS and DDS will become easier to use. The problem of data translation in a heterogeneous computing environment has been discussed and most people incorrectly believe it to be a solved research problem. However, installation of new tools is impossible without the development of effective system migration technologies. System migration technologies are still needed in real organizations.

## (4) Distributed DBMS

Recently, there has been concentrated commercial activity in this area, and several vendors are hard at work on heterogeneous (or federated) distributed DBMSs. The really hard problems in this area center around system administration of a large scale distributed DBMS. Managing this environment (e.g., installing new updates of modules and new users) is a major problem for current systems. It is very important to organize various technologies related to distributed DBMS systematically in a way that transcends individual organization $[15,17]$ .

## (5) Multi-processor support

Recently multi-processors have been popularized as general purpose computers. In particular, tightly coupled shared memory systems of MIMD (multiple instruction multiple data stream) computers, such as the Sequent symmetry system, are promising for mission-critical on-line transaction processing (OLTP). The big benefit from such parallelism is the ability to give a user real time response and to hold locks for shorter periods of time.

Some recent DBMSs deliver high cost/performance by taking advantage of today's powerful and cost effective parallel computers.

(6) Integration of artificial neural networks with DBMS

As a whole, we have become adept at collecting, storing, and maintaining facts and statistics about the organization. Though we have become skilled at collecting data, using it as a strategic tool for enhancing business performance has lagged.

Integration of Artificial Neural Networks (ANN) [36] with DBMS is already being studied in several ways such as:

(a) extraction of rules from a given or trained neural network (knowledge base) [9,14,16], and

(b) information retrieval and query processing using ANNs.

Possible benefits of this integration are facilitated acquisition of knowledge bases, and better retrieval of information and queries embedded with partial cues and/or noise. It is also expected that the Entity-Relationship model can aid in database design, when not enough information is available about all entities and relationships.

## Acknowledgements

The efforts of both Dr. Sibley, chairman of the Editorial Board, and anonymous reviewers are gratefully acknowledged. Their careful reading of the original manuscript lead to many critical comments which were indeed valuable.

The authors would like to thank each member of the research project on Operational Technology of Database Systems at the Software Technology Center of Information Technology Promotion Agency (IPA), Japan, who contributed to the survey of DBMS technology in Japan. The authors also wish to express most sincere appreciation to Dr. Hidetoshi Kawai of Iwaki-Meisei University and Dr. Fumihiko Kamijo of Tokai University for their constructive comments.

## References

[1] Allen, F., Loomis, M. and Mannino, M. "The Integrated Directory/Dictionary System", ACM Computing Surveys, Vol. 14, No. 2, 1982, pp. 245–286.

[2] American Management Association, The 1985 AMA Report on Information Centers, New York, 1985.

[3] American Management Association, The 1988 AMA Report on End-User and Departmental Computing, New York, 1988.

[4] Benson, D.H. “A Field Study of End User computing: Findings and Issues”, MIS Quarterly, Vol. 7, No. 4, 1983, pp. 35–45.

[5] Bergeron, F., Rivard, S. and Serre, L.D. “Investigating the Support Role of the Information Center”, MIS Quarterly, Vol. 14, No. 3, 1990, pp. 246–260.

[6] Carr, H.H. “Information Centers: The IBM Model vs. Practice”, MIS Quarterly, Vol. 11, No. 3, 1987, pp. 325–338.

[7] Data Dictionary System Working Party of the British Computer Society, Report, Joint Issue, Data Base, Vol. 9, No. 2 and SIGMOD Record, Vol. 9, No. 4, 1977.

[8] Fishman, D.H., Beech, D., Cate, H.P., Chow, E.C., Connors, T., Davis, J.W., Derrett, N., Hoch, C.G., Kent, W., Lyngbaek, P., Mahbod, B., Neimat, M.A., Ryan, T.A. and Shan, M.C. “Iris: An Object-Oriented Database Management System”, ACM Transactions on Office Information Systems, Vol. 5, No. 1, 1987, pp. 48–69.

[9] Gallant, S.I. "Connectionist Expert Systems", Communications of the ACM, Vol. 31, No. 2, 1988, pp. 152–169.

[10] Gillenson, M.L. “Trends in Data Administration”, MIS Quarterly, Vol. 9, No. 4, 1985, pp. 317–325.

[11] Hammond, L.W. “Management Considerations for an Information Center”, IBM Systems Journal, Vol. 21, No. 2, 1982, pp. 131–161.

[12] Hayashi, Y. “Operational Technology Problems on Practical Database Systems in Japan and Their Structural Analysis”, Proceedings of the IEEE Ninth International Computer Software and Application Conference (COMPSAC'85), Chicago, IL, 1985, pp. 360–367.

[13] Hayashi, Y., ed., “Survey of Database System Management Technologies”, Technical report no. 59-049, Software Technology Center of Information-technology Promotion Agency (IPA), Japan, 1985, 272 pp. (in Japanese).

[14] Hayashi, Y. and Imura, A. "Fuzzy Neural Expert System with Automated Extraction of Fuzzy If-Then Rules from a Trained Neural Network", Proceedings of the First International Symposium on Uncertainty Modeling and Analysis (ISUMA'90), MD, 1990, pp. 489–494.

[15] Hayashi, Y. "Expert System for Optimal Design and Operation Management in Distributed Database Systems

(Part I)”, Technical report, Vol. 4, No. 87-01035, The Telecommunications Advancement Foundation, Japan, 1990, pp. 714–726 (in Japanese).

[16] Hayashi, Y. "A Neural Expert System with Automated Extraction of Fuzzy If-Then Rules and Its Application to Medical Diagnosis", In: Touretzky, D.S. and Lippman, P., eds., Advances in Neural Information Processing, Vol. 3, Morgan Kaufmann, San Mateo, CA, 1991, pp. 578–584.

[17] Hayashi, Y. “Expert System for Optimal Design and Operation Management in Distributed Database Systems (Part II)”, Technical Report, Vol. 5, No. 88-01048, The Telecommunications Advancement Foundation, Japan, 1991, pp. 489–495 (in Japanese).

[18] Ho, S.S.M. “Use and Organizational Implications of Database Systems: Some Hong Kong Experiences”, Data Base, Vol. 15, No. 3, 1984, pp. 27–36.

[19] Honkanen, P.A. “The Integrity Problem, and What Can Be Done About It Using Today’s DBMSs”, Data Base, Vol. 20, No. 3, 1989, pp. 21–27.

[20] Ikeda, H., Ishihara, W. and Kobayashi, Y. “Design and Application of Data Dictionary/Directory System”, Proceedings of the Advanced Database Symposium (IPSJ), 1981, pp. 61–70.

[21] Jardine, J.A. “Data Base Management Systems... the EDP Poker Game”, Canadian Datasystems, Vol. 6, No. 8, 1974, pp. 46–49.

[22] Kim, W. and Lochovsky, F.H., eds., Object-Oriented Concepts, Databases, and Applications, Addison-Wesley, Reading, MA, 1989.

[23] Lefkovits, H.C., Sibley, E.H. and Lefkovits, S.L. Information Resource / Data Dictionary System, QED Information Science, Wellesley, MA, 1983.

[24] Martin, J. Strategic Data-Planning Methodologies, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[25] Martin, J., Fourth-Generation Languages, Vol. 1, Prentice-Hall, Englewood Cliffs, NJ, 1985.

[26] Mintzberg, H., The Structuring of Organizations, Prentice-Hall, Englewood Cliffs, NJ, 1979.

[27] Mintzberg, H. “Organization Design: Fashion of Fit”, Harvard Business Review, Vol. 59, No. 1, 1981, pp. 103–116.

[28] Navathe, S.B. and Kerschberg, L. "Role of Data Dictionaries in Information Resource Management", Information and Management, Vol. 10, 1986, pp. 21–46.

[29] Revell, N. “Managing the Development of Database Systems”, Information and Management, Vol. 4, 1981, pp. 197–205.

[30] Rivard, S. and Huff, S.L. “An Empirical Study of Users as Application Developers”, Information and Management, Vol. 8, No. 2, 1985, pp. 85–102.

[31] Rockart, J.F. and Flannery, L.S. "The Management of End User Computing", Communications of the ACM, Vol. 26, No. 10, 1983, pp. 776–784.

[32] Sibley, E.H and Turner, J.A. "Data Base Management: A Framework for Effective Use", Proceedings of the Second Jerusalem Conference on Information Technology: Computers for Social and Economic Technology, Vol. 1, 1974, pp. 273–289.

[33] Sibley, E.H. “The Impact of Database Technology on Business Systems”, In: Gilchrist, B., ed., Information Processing 77, North-Holland, Amsterdam, 1977, pp. 589–596.

[34] Sibley, E.H. “Standardization and Database Systems”, Proceedings of the International Conference on Very Large Data Bases, 1977, pp. 144–155.

[35] Sibley, E.H. “How to Select and Evaluate a DBMS”, Journal of Information Systems Management, Vol. 2, No. 2, 1985, pp. 40–49.

[36] Simpson, P.K., Artificial Neural Systems, Pergamon Press, New York, 1990).
