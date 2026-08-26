---
otero_id: 19770
otero_key: "MTSJ9UMC"
title: "Reconciling business intelligence, analytics and decision support systems: More data, deeper insight"
authors: "Gloria Phillips-Wren; Mary Daly; Frada Burstein"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113560"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Reconciling business intelligence, analytics and decision support systems: More data, deeper insight

![](/api/attachments/MTSJ9UMC/fulltext/images/7080b0c411c36dc20b68dd3cced7ce015d2f5f5da5068101b91551f010f653b8.jpg)

Gloria Phillips-Wren <sup>a,\*</sup>, Mary Daly <sup>b</sup>, Frada Burstein <sup>c</sup>

<sup>a</sup> Sellinger School of Business & Management, Loyola University Maryland, Baltimore, MD 21210, USA

<sup>b</sup> Cork University Business School, University College Cork, Cork, Ireland

<sup>c</sup> Department of Human Centred Computing, Monash University, Melbourne, Australia

## A R T I C L E I N F O

Keywords: Business intelligence Analytics Big data Decision support Decision process

## A B S T R A C T

Business Intelligence and Analytics (BI&A) systems have demonstrated their potential to enhance decision making; however, the linkage between BI&A and decision support systems (DSS) has been contested by some, if not completely denied by others. In this research, we investigate the foundations of BI&A by using foundational literature on DSS to open the ‘black box’ of BI&A systems. We argue that BI&A is fundamentally a subfield of DSS that is seeking to convert more data into deeper insight, but it has lost its connection to DSS literature and, thereby, missed research opportunities. In this paper, we first define DSS and BI&A and then present a systematic review of foundational DSS literature to assess their leveraging in BI&A research. By classifying cited DSS articles and citing BI&A articles into four areas: conceptual framework, design & implementation, business value & organizational use, and cognition & decision making, potential research for BI&A is uncovered. We reconcile these two research streams by mapping BI&A frameworks to classical DSS components through interviews with practitioners. The result is formulated as a comparative, process-level architecture for converting data into insight. New research opportunities for BI&A are suggested motivated by foundational DSS literature.

## 1. Introduction

Decision support systems (DSS) are well-established types of infor mation systems with the primary purpose of improving decision making based on data and analysis [7,127]. However, some authors claim that the research field of DSS is no longer current or of interest and has been replaced by the newer fields of Business Intelligence and Analytics (BI&A) and Big Data to enhance decision making [52]. Others suggest that BI&A is a new kind of information system that originated from operations research and has been adopted mainly due to the more recent, ready access to large amounts of ‘big data’ for analysis and modeling [1].

In the early 1990s, the terms ‘Business Intelligence’, ‘Business Ana lytics’, ‘Big Data’, and their variations, were coined to describe a developing information technology that could take advantage of the growing amount of data, extensive interconnectedness, and significant advances in computing [42]. In a widely cited study, Chen et al. [25] discerned BI&A research trends from a comprehensive literature search from the past decade (2000− 2011). They argued that “as a data-centric approach, BI&A has its roots in the long-standing database management field … [while] the analytical techniques are grounded mainly in sta tistical methods developed in the 1970s and data mining techniques developed in the 1980s” ( [25], p. 1166). In contrast, Alter [7] catego rized DSS in terms of their generic functional capabilities: retrieving items of information; providing a mechanism for ‘ad-hoc’ data analysis; providing pre-specified aggregation of data in the form of reports; and estimating the consequences of proposed decisions. As can be seen from this early description, DSS functionality is consistent with the expecta tions of modern BI&A capabilities in terms of data aggregation, ad-hoc data analytics, and support for decision making based on predetermined needs of business users.

Following these competing observations of the connections between DSS and BI&A, in this paper we seek to explore the relationship between these two seemingly different, but related, types of information systems. In doing so we seek to augment and deepen the Chen et al. [25] study by probing the research question: What is the relationship between founda tional DSS research and BI&A research?

In addition, we seek to explore the related questions: (1) Can these two research streams be reconciled in one framework? (2) What research opportunities can be uncovered for BI&A based on the rich

history of DSS research?

We address these research questions by first examining published definitions of BI&A, systematically analyzing DSS publications from its roots in the 1970s to 1991 in leading information systems and man agement journals, and then exploring the linkage between citations of early DSS literature by BI&A researchers. Our premise is that the pur pose of BI&A is to inform and enhance human decision making using computing resources, and, as such, we expected its earliest roots to be in the DSS literature. In fact, some authors define BI&A in these terms, for example, Arnott et al. [11] state that, “Business intelligence (BI) is often used as the umbrella term for large-scale decision support systems (DSS) in organizations” ( [11], p. 58).

To address the related research question one, we adopted the Big Data Analytics framework proposed by Phillips-Wren et al. [104] as a starting point for our exploration. That framework contains compre hensive structural components that facilitate BI&A functionality. We found that we could fully explain the extensions made by BI&A by mapping them to the classical DSS components of database, model base, user interface, and decision maker. In addition, a process perspective on BI&A has been identified as a need for further research [78]. Thus, to address this call to develop a process view on BI&A systems, we con ducted consultations with senior BI&A practitioners. Our consultations with managers, data scientists, vendors and leading developers of BI&A software confirmed the BI&A structural components and, in addition, produced a process-level architecture for BI&A. One of our contribu tions, thus, is in ‘opening the black box’ of BI&A systems and high lighting the evolution that these systems have undergone from traditional DSS to the complex systems that require special skills to convert the vast amount of relevant data into insight to address ‘wicked problems’ [26]. The outcome is an updated comprehensive process-level architecture for BI&A that reconciles it with DSS together with an agenda for future research in BI&A based on the rich history of DSS.

In the following sections we provide theoretical background on BI&A systems and DSS including comparative definitions, the typical archi tectures for both systems, their functionalities, the types of tasks they support, and descriptions of user roles. Then the details of the research methodology are provided, followed by the results of a systematic citation analysis and an empirical study of a BI&A integrated process model framework. We conclude with opportunities for future research in BI&A based on DSS research and contributions.

## 2. Theory and motivation

## 2.1. Defining DSS

In 1980 Sprague [127] published a seminal paper laying out the framework of a DSS and arguing that it was fundamentally different than a Management Information System (MIS). In his view, while a MIS was focused on information, a DSS was an interactive system focused on a decision at a higher level in the organization. He refers to Simon [124] in defining a DSS as “a class of information system that draws on transaction processing systems and interacts with the other parts of the overall infor mation system to support the decision-making activities of managers and other knowledge workers in organizations” ( [127], p. 6]. Sprague com pares a DSS to Simon’s adaptive system that searches for answers in the short run, learns and modifies its behavior in the intermediate time frame, and evolves to accommodate different behavior styles and ca pabilities in the long run.

For the purposes of this paper we subscribe to the above Sprague [127] definition of DSS since it is still relevant to the current vision for computerized DSS and emphasizes the role of this system as an interface between various information sources for the purpose of providing rele vant information to decision makers at all organizational levels.

## 2.2. Defining BI&A

In comparison, there is no agreed upon definition of BI&A. Instead, BI&A is often categorized in terms of its capabilities to handle data types and convert them into knowledge and insight for decision making [25,137,104]. Modern BI&A systems extend DSS by handling traditional structured data such as in structured database management systems (DBMS), and also unstructured data such as images, semi-structured sensor data such as Internet of Things (IoT), and combinations of these data types. In general, the more complex the data types that can be analyzed, the more advanced the BI&A system.

We first approached the question of whether BI&A should be regarded as one area or two. To this end, we traced definitions of BI and of BA. Definitions of BI were surveyed by Chee et al. [24] through 2007, and they traced the first use of the term BI to a 1958 article by Luhn entitled “A Business Intelligence System” [83]. They pointed out that Howard Dresner from Gartner Research is better known as “the father of BI” and regularized the term in 1989. They classified the definitions into three main categories with some overlap: management/process, tech nological, and product/solution. We supplemented their definitions with those from recent publications shown in the Appendix, and, for the purposes of our study, with a focus on management/process. We thus accept the distinct definitions given by Davenport [31]: BI encompasses “tools to support data-driven decisions, with emphasis on reporting” while BA has a “focus on statistical and mathematical analysis for decisions.” Although many authors do not discriminate between the two areas and have adopted BI&A as one field, the distinction is useful in parsing out differences and similarities with DSS.

Consistent with Davenport’s [31] definition, our survey showed that there is a clear emphasis on the decision-making support role of BI [30,45,100] and Analytics [19,32,33,80,117] with most definitions specifying ‘supporting better decision making’ or ‘insight generation’ as the objective of these systems. Following this discovery, we were interested in ascertaining the foundations of DSS and BI&A from the literature to determine if these fields are actually distinct.

## 2.3. DSS foundations

We reviewed foundational DSS publications to ascertain their rela tionship with BI&A. In a seminal article on DSS, Sprague [127] emphasized that DSS is not introduced as “an evolutionary advancement of electronic data processing (EDP) system” or simply for “getting the right information to the right people at the right time” ( [127], p.4). DSS would thereafter be targeted to semi-structured and unstructured deci sion and management tasks. Arnott and Pervan [12] in their review argue that the managerial nature of DSS was axiomatic or self-evident as stated by Gorry and Scott Morton [49].

Sprague [127] and his followers identified a DSS framework as consisting of a decision maker, a database management system, a model base management system, and a user interface that includes “a complex software system for linking the user” to the database and model base ( [127], p. 14). Extracting data to support decision making requires flexibility to respond to varied requests, sometimes logically separate databases, and internal as well as external data sources. These re quirements propelled research in the Database and the Database Man agement System (DBMS) (e.g., [25]). The Model Base supported rapid model creation to enhance decision-making for all types of users while the Model Management System was used to store, catalog, link and facilitate access to models. The User Interface provided access to, and dialogue with, the system. There is also a suggestion that the ‘database includes internal and external data access and management facilities, and that the model base should contain special models for three types of decisions (i.e., tactical, operational, strategic) as well as building blocks for new models as required.

## 2.4. BI&A foundations

BI&A technology has been driven by industry needs and popularized in vendor/practitioner literature. The argument has been put forward that BI&A capabilities outstrip DSS, and some researchers propose that the fields have diverged [12]. Many authors acknowledge that BI&A is a product of the evolution of big data analytics technology and infra structure $[ 2 5 , 6 0 ]$ needed to handle the data explosion. ‘Big data’ are generally characterized by the 3 V’s of volume, velocity and variety: volume for the massive amount of data, velocity for the rapid speed at which data are generated, and variety for the many types of data [104], although some authors add other V’s such as veracity or value. Cloud computing consisting of remote servers provides scalability and flexi bility for many organizations so that data quantity is no longer an issue and enables organizations to collect and store data at speed until ready for processing [112,48]. The opportunity to generate insights from heterogeneous sources of big data to inform future decisions has been one of the major factors driving organizations to invest in BI&A projects.

Chen et al. [25] categorized BI&A evolution as generations of BI&A 1.0, BI&A 2.0, and BI&A 3.0. BI&A 1.0 encompasses DBMS-based structured data, BI&A 2.0 includes web and unstructured data, and BI&A 3.0 brings in mobile and sensor data. Thus, this categorization primarily revolves around the broad types of data variety accessible for intelligence and analytics. It can be noted that since DBMS were developed alongside DSS and enabled DSS that relied on data, there appears to be a general consensus that some BI&A systems were based on data-driven DSS [99,138]. Dinis et al. [34] present a recent example of incorporating BI&A functionality within a DSS.

## 2.5. Users and roles in DSS, BI and analytics

Many functionalities afforded by BI&A and associated decision making user groups are the same as, or similar to, those described by early DSS literature, particularly for operational and tactical decisions, albeit extended with wider access to heterogeneous data sources, so phisticated reporting, and visualization. Notably, at the strategic decision-making level that addresses wicked problems, BI&A offers a new functionality that requires the involvement of data scientists to produce new methods and models to deal with the massive amounts of structured and unstructured data. This development was predicted in early DSS literature for systems that required a ‘chauffeur decisionmaker’ to massage the data and interface with the DSS to produce al ternatives for management decision makers [87].

Sprague and Watson [126] assigned various roles associated with DSS development and use. Depending on the level of specificity of the system to the application context, the users varied from managers themselves to the increased need for more technical support when it comes to customization and for creation of new models and software. More recent researchers have also identified various roles and skill sets for those involved in DSS projects. In general, these roles vary in terms of their immediate involvement in the production of the decision recom mendations, the application to a decision scenario producing alterna tives, and the evaluation of the implications of a decision [28].

On the other hand, the roles involved in BI&A processes from the decision support perspective have been identified as an underresearched issue [78]. As a starting point Kowalczyk et al. [78] and other BI researchers (e.g., [137]) recognize a strong link between BI specialists and decision makers. Similarly, early DSS researchers recognized multiple user roles depending on the level of technical competency in either operating custom-built DSS or being involved in adapting DSS tools for their context [127,126]. Maynard et al. [87] identified five major groups of people that are involved at various stages of DSS development and exploitation varying in organizational hierar chy and the types of decisions they make (e.g., tactical, operational or strategic). These suggested roles echo the differentiated use of big data analytics as identified by Phillips-Wren et al. [104] and Watson [137], among others, who suggest that business users may need assistance of data scientists when it comes to exploration of external data and generating unsolicited insights.

Watson [137] proposed nine categories of users involved in a ‘BI/ analytics environment’ that he argues to be a current equivalent of the DSS development environment. The roles and policies that define the boundaries of their operation are generally recognized and referred to as part of BI Governance [42]. Tamm et al. [128] classified BI&A users into two types who approach the task of data analytics from different per spectives: skills to develop new algorithms and models suitable for producing insights from a variety of data sources, and those who use the BI&A system interface to access the suite of models and algorithms needed for their semi-structured tasks.

From the above definitions and comparative analysis, we posit the need for a deeper study of the relationship between these two technol ogies which we explore in the following sections.

## 3. Methodology

The methodology for this study is informed by an inductive process that is based on deriving conclusions from the evidence drawn from data [73]. To collect the data, we searched for the first instance of DSS literature and found initial publications in the early 1970s. We then performed a systematic review of DSS literature published in 14 major MIS journals during two time periods: 1970–1985 and 1986–1991. During 1970–1985, the MIS field investigated the role of MIS in orga nizations and debated whether DSS should be recognized as a separate research stream. The second time period traces the development of the field after the establishment of the journal Decision Support Systems in 1985, which laid claim to DSS as a specialty research field differentiated from the more general MIS, through 1991 when textbooks were pub lished that clearly suggested the field as mature [102,132].

We identified DSS articles by searching for the keywords of ‘decision support systems’, ‘decision support’ or ‘DSS’ in the article’s title as representative of the author’s self-designation as DSS and the tacit approval of the journal editor-in-chief. The DSS field is mature, so we expected the best research from that time period (1970–1991) to be published in journals; thus, we did not investigate conference pro ceedings in this timeframe. This type of bibliographic search using titles has known limitations and could be relaxed in future studies, although it is consistent with previous studies of this sort (e.g., [25]). We identified IS journals within the first 300 pages of Google Scholar results that would be considered part of the MIS research stream, implying that we eliminated psychology journals and journals specific to another business discipline such as marketing. We compared our list of journals with a contemporaneous study of leading MIS journals published in 1984 [134] and found consistency. We then performed a manual search of each journal’s archives to identify relevant DSS articles, together with BI&A articles that cited them.

After identifying DSS-specific articles, we investigated BI&A articles that cited them. To do so, we performed a Google Scholar search for citations of each DSS article and reviewed the citing article’s title for the terms ‘business intelligence’, ‘analytics’ or ‘big data’ (or their acronyms) as consistent with our self-identification schema used to identify DSS articles. Any BI&A article that met these criteria was downloaded for detailed analysis, including conference proceedings. We included pro ceedings since BI&A research is still an emerging area, and research may not have yet been published in mainstream journals. We eliminated other research outputs such as dissertations or course notes on the basis that they are not peer-reviewed research outputs at the same level as journal or mainstream conference papers. We identified the way that the DSS citation was utilized in the BI&A article along with other informa tion such as how BI&A was defined. On the basis of this research, we identified gaps in BI&A literature where the connection between DSS and BI&A research appears to have been lost.

To consider whether the two fields, BI&A and DSS, should indeed be considered as separate research streams, we identified the Big Data Analytics framework proposed by Phillips-Wren et al. [104] as a candidate generic architecture of a BI&A system. That architecture is consistent with others published more recently (e.g., [137]). It appeared that we could establish a clear mapping of this architecture to the components of classical DSS of User/Decision Maker, a Database Man agement System, a Model Base Management System, and a User Inter face. To validate this mapping and update the BI&A framework, we presented the initial concept to the practitioner community through semi-structured interviews.

The purpose of this empirical study was to seek feedback from senior practitioners on their BI&A system in terms of both overall structural components and their process of converting data into actionable in sights, and to identify the decision-making roles required to operation alize the system. Seven interviews were conducted with senior-level BI&A practitioners and leaders from a variety of industries and company sizes as shown in Table 1.

All of these companies have data science teams and personnel with job titles under the general BI&A umbrella, and they utilize these technologies for decision making and innovation. We intentionally selected a range of companies from large to small, established to newer, consulting to specialized, service to innovators, and multinational to localized. We showed the proposed architecture to each practitioner and refined it until agreement was reached. We then cross-checked the final architecture with previous interviewees. We also discussed what future research directions are needed to advance the BI&A field. We stopped interviewing practitioners at the point of saturation and consensus with the architecture.

Finally, with an integrated BI&A and DSS process-level architecture, and following the practitioners’ suggestions, we explored a future research agenda for BI&A that can be envisioned by leveraging DSS seminal literature. To do so, we examined the identified DSS literature that has not been cited by BI&A research, classified each article in terms of topic, and suggested associated research questions for BI&A research.

## 4. Results

## 4.1. Identification of DSS literature and citing BI&A literature

As previously stated, DSS journal articles were identified by the keywords ofdecision support systems', 'decision support' orDSS' in the article’s title. BI&A articles, including proceedings, were identified by ‘business intelligence’, ‘analytics’ or ‘big data’ (or their acronyms) in the title. As Table 2 indicates, a total of 271 DSS articles were published during the period 1970 to 1991. Of these, 29 seminal DSS papers (10.7% of total) are cited 59 times in 44 distinct BI&A articles. During the research period, 1970 to 1991, a solid conceptual foundation and tax onomy of decision support systems was identified [122].

## 4.2. Classification of cited DSS literature

We first describe DSS literature that has been cited by BI&A. To do so, we classified the literature into one of four research categories with definitions shown in Table 3: conceptual framework, design & imple mentation, business value & organizational use, and cognition & deci sion making. The classification conceptual framework generally presents the new concepts, algorithms and major components of a sys tem and their relationships to each other. Design & implementation attempts to identify characteristics to meet objectives and to develop a coherent project plan to instantiate the technology. Business value & organizational use literature focuses on technology within the organi zation including its connections to the outside ecosystem. Finally, cognition & decision making describes human behavior and is often based on psychological and economic literature that has been applied to technology-assisted systems such as DSS.

As can be seen in Tables 4, 29 unique DSS articles were identified using the categories discussed in Table 3. Many of these have multiple citations.

## 4.3. Description of BI&A articles that cite DSS literature

As can be seen in Tables 5, 44 unique BI&A articles were found that cited DSS articles, citing them a total of 59 times as seen in Fig. 1. Ar ticles were published in scholarly journals or conference proceedings, and they were identified according to our criteria explained previously. Of the 44 BI&A articles, 33 are BI articles, and the remaining 11 articles have either ‘analytics’ or ‘big data’ in the title. In Table 5 each article is classified into one of four general research classifications using the schema that was developed for DSS articles shown in Table 4.

We note that the overall trends show the focus of BI&A research on business value & organizational use at 48% while only 18% is on con ceptual framework, the reverse of DSS research. The other two BI&A categories show 25% on design & implementation and 9% on cognition & decision making, similar to DSS articles. In terms of publication fo rums, of the 44 articles, 20 were published in journals, and 24 were published in the proceedings of mainstream conferences.

However, the most recent BI&A articles (2016–2020) predominantly cite design & implementation and conceptual framework articles as seen in Fig. 1. The citing of cognition & decision making and business value & organizational use categories has declined. If BI&A is closely connected to DSS, these observations are useful in determining opportunities for BI&A research by leveraging DSS foundational research. Thus, we examine whether BI&A and DSS can be integrated under one framework to explore their affiliation.

Table 1  
Demographics of empirical study participants.

<table><tr><td>Position</td><td>Use of BI&amp;A</td><td>Company sector</td><td>Company description</td><td>Company size</td></tr><tr><td>Software developer</td><td>Using Big Data to innovate and develop new products</td><td>Internet analytics. Cloud and cluster computing, artificial intelligence</td><td>Multinational, publicly traded</td><td>Fortune 500</td></tr><tr><td>Chief technology officer</td><td>Using BI&amp;A for consulting to solve difficult applied problems</td><td>Consulting - systems technology, data analytics and visualization, user experience</td><td>Privately held</td><td>51–200 employees</td></tr><tr><td>Managing director of analytics</td><td>Using BI&amp;A to manage energy markets</td><td>Energy provider</td><td>Publicly traded</td><td>Fortune 100</td></tr><tr><td>President and founder</td><td>Using BI&amp;A to develop new cyber security tools</td><td>Engineering services for National Intelligence Community</td><td>Privately held</td><td>2–10 employees</td></tr><tr><td>Vice president</td><td>Using BI&amp;A to develop cyber security solutions</td><td>Consulting - management and technology, analytics, cyber solutions</td><td>Multinational, publicly traded, holding company</td><td>Fortune 500</td></tr><tr><td>Chief product officer</td><td>Using BI&amp;A to identify potential personnel for specialized BI&amp;A positions</td><td>Technology workforce development using AI and data science, digital transformation</td><td>Privately held</td><td>501–1000 employees</td></tr><tr><td>Vice president</td><td>Using BI&amp;A to innovate and provide telecommunications support for defense</td><td>Advanced telecommunication, media, and technology services worldwide</td><td>Multinational, publicly traded</td><td>Fortune 100</td></tr></table>

Table 2  
Number of DSS articles and BI&A citations.

<table><tr><td colspan="2"></td><td colspan="3">1970–1985</td><td colspan="3">1986–1991</td></tr><tr><td>Journal</td><td>Initial publication date</td><td>Number of DSS Papers</td><td>Number of DSS papers cited in BI&amp;A papers</td><td>Number of citations in BI&amp;A papers</td><td>Number of DSS Papers</td><td>Number of DSS Papers cited in BI&amp;A papers</td><td>Number of citations in BI&amp;A Papers</td></tr><tr><td>Journal of Operational Research Society (JORS)</td><td>1950</td><td>2</td><td>0</td><td>0</td><td>7</td><td>0</td><td>0</td></tr><tr><td>Operations Research (OR)</td><td>1952</td><td>1</td><td>1</td><td>1</td><td>7</td><td>0</td><td>0</td></tr><tr><td>Management Science (MS)</td><td>1954</td><td>5</td><td>1</td><td>1</td><td>2</td><td>2</td><td>3</td></tr><tr><td>Sloan Management Review (SMR)</td><td>1959</td><td>4</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>The DATA BASE for Advances in Information Systems (DB)</td><td>1969</td><td>20</td><td>2</td><td>11</td><td>2</td><td>0</td><td>0</td></tr><tr><td>Decision Sciences (DS)</td><td>1970</td><td>7</td><td>2</td><td>3</td><td>11</td><td>0</td><td>0</td></tr><tr><td>Interfaces (I)</td><td>1970</td><td>20</td><td>0</td><td>0</td><td>6</td><td>0</td><td>0</td></tr><tr><td>European Journal of Operational Research (EJOR)</td><td>1977</td><td>11</td><td>0</td><td>0</td><td>25</td><td>2</td><td>2</td></tr><tr><td>Information and Management (IM)</td><td>1977</td><td>16</td><td>1</td><td>1</td><td>18</td><td>0</td><td>0</td></tr><tr><td>MIS Quarterly (MIS Q)</td><td>1977</td><td>18</td><td>8</td><td>21</td><td>12</td><td>4</td><td>7</td></tr><tr><td>Journal of Management Information Systems (JMIS)</td><td>1984</td><td>8</td><td>0</td><td>0</td><td>21</td><td>3</td><td>5</td></tr><tr><td>Decision Support Systems (DSS)</td><td>1985</td><td>1</td><td>0</td><td>0</td><td>44</td><td>1</td><td>2</td></tr><tr><td>Information Systems Research (ISR)</td><td>1990</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Journal of Information Technology (JIT)</td><td>1986</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td></tr><tr><td>TOTALS</td><td></td><td>113</td><td>16</td><td>39</td><td>158</td><td>13</td><td>20</td></tr></table>

Table 3  
Definitions of terms for classifications of DSS articles.

<table><tr><td>Classification</td><td>Definition of classification</td></tr><tr><td>Conceptual framework</td><td>“Comprehensive view ... using the systemic framework as an organizing concept” ([9], p. 1045)</td></tr><tr><td>Design &amp; implementation</td><td>Implementation “is commonly viewed as a series of related activities [such as] initiation, strategic design, technical design, development, conversion, and evaluation” ([141], p. 35])</td></tr><tr><td>Business value &amp; organizational use (includes case studies)</td><td>“The IT resource [is] associated with improved operational efficiencies or competitive advantage” ([92], p. 299)</td></tr><tr><td>Cognition &amp; decision making</td><td>“Concerns with the ways in which decisions are made, and not just with decision outcomes” ([123], p. 498)</td></tr></table>

Table 4  
Classification of cited DSS articles from 1970 to 1991.

<table><tr><td>Classification</td><td>Total number of DSS articles</td><td>Number of DSS articles as % of total</td></tr><tr><td>Conceptual framework</td><td>13</td><td>45%</td></tr><tr><td>Design &amp; implementation</td><td>9</td><td>31%</td></tr><tr><td>Business value &amp; organizational use</td><td>4</td><td>14%</td></tr><tr><td>Cognition &amp; decision making</td><td>3</td><td>10%</td></tr><tr><td>TOTAL unique DSS articles</td><td>29</td><td>100%</td></tr></table>

## 5. Reconciling BI&A and DSS

## 5.1. Structure and process-level architecture of BI&A and big data systems

To ascertain whether BI&A and DSS could be reconciled within one architecture, we reviewed the components of classical DSS as described and diagrammed by Sprague and Watson [126] and Sprague [127]. These consist of a decision maker, a user interface (UI), a database management system (DBMS), a model base management system (MBMS), a database, and a model base. These components are shown in Fig. 2 by the darker shading. We then compared the BI&A and Big Data framework from Phillips-Wren et al. [104] that was developed inde pendently from a consideration of DSS, identified overlaps between BI&A and DSS, and integrated the two architectures as an initial pro posed BI&A framework. The initial architecture was empirically tested with practitioners without identifying DSS components, as described previously in the Methodology section, and modified according to their input.

Table 5  
Classification of BI&A articles that cite DSS articles.

<table><tr><td>Classification of BI&amp;A article</td><td>Total number of BI&amp;A articles</td><td>Number of BI&amp;A articles as % of total</td></tr><tr><td>Conceptual framework</td><td>8</td><td>18%</td></tr><tr><td>Design &amp; implementation</td><td>11</td><td>25%</td></tr><tr><td>Business value &amp; organizational use</td><td>21</td><td>48%</td></tr><tr><td>Cognition &amp; decision making</td><td>4</td><td>9%</td></tr><tr><td>TOTAL unique BI&amp;A articles</td><td>44</td><td>100%</td></tr></table>

Major changes to the initial architecture were suggested by practi tioners and implemented in the final diagram. Practitioners discuss BI&A as a process of converting data into insight for decision makers, and the depiction of process flow thus became a primary consideration. As can be seen near the bottom of Fig. 2, the process flow entails data sourcing, data preparation, data storage & processing, data analysis, and data access & usage. Practitioners also identified the primary groups of decision makers and the organizational context in which BI&A and DSS exist as essential to the BI&A process. These concepts are subsequently discussed in more detail.

We examined the culminating BI&A diagram and found that the major DSS components remained visible, but they had been extended to include new capabilities. We next discuss the extensions of classical DSS components to incorporate the BI&A architecture.

<table><tr><td rowspan="3" colspan="3"></td><td colspan="21">BA/BI Citations</td><td></td></tr><tr><td>2000</td><td>2001</td><td>2002</td><td>2003</td><td>2004</td><td>2005</td><td>2006</td><td>2007</td><td>2008</td><td>2009</td><td>2010</td><td>2011</td><td>2012</td><td>2013</td><td>2014</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td></td></tr><tr><td># citations</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>6</td><td>4</td><td>1</td><td>5</td><td>0</td><td>5</td><td>5</td><td>6</td><td>0</td><td>7</td><td>1</td></tr><tr><td></td><td>DSS Papers</td><td>JRnl</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">Cog &amp; DM</td><td>Robey &amp; Taggart, 1982, [110]</td><td>MIS Q</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[23]</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Green &amp; Hughes, 1986, [53]</td><td>JMIS</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[35]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sharda et al., 1988, [118]</td><td>MS</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[61]</td><td></td><td></td><td>[111]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">BV &amp; Org use</td><td>Donovan et al., 1977, [36]</td><td>DB</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[58]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Houdeshel &amp; Watson, 1987, [63]</td><td>MIS Q</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[79]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ElSherif &amp; ElSawy, 1988, [39]</td><td>MIS Q</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[98]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Van Hee &amp; Wijbrands, 1988, [133]</td><td>EJOR</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>**[85]</td><td></td><td></td></tr><tr><td rowspan="9">Design &amp; Implementation</td><td>Meador &amp; Ness, 1974, [89]</td><td>SMR</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[114]</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Alter, 1978, [7]</td><td>MIS Q</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[74]</td><td></td><td>[57]</td><td></td><td></td></tr><tr><td>Keen, 1980, [71]</td><td>DB</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[140][93][95]</td><td>[94]</td><td></td><td>**[128]</td><td></td><td>[68]</td><td>[113]*[114]</td><td>[125][11]</td><td></td><td></td><td></td></tr><tr><td>Alavi &amp; Henderson, 1981, [3]</td><td>MS</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[78]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Fuerst &amp; Cheney, 1982, [44]</td><td>DS</td><td>2</td><td>[20]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[77]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Meador et al., 1984, [90]</td><td>MIS Q</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>**[135]</td><td></td><td></td><td></td><td></td></tr><tr><td>Sanders &amp; Courtney, 1985, [115]</td><td>MIS Q</td><td>6</td><td>*[20]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>**[119]</td><td></td><td></td><td>*[79]</td><td></td><td></td><td>[14]</td><td>**[21]*[135]</td><td></td><td></td><td></td><td></td></tr><tr><td>Jelassi, 1987, [67]</td><td>DSS</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>*[95]</td><td>*[94]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Eom &amp; Lee, 1990, [40]</td><td>EJOR</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[41]</td><td></td></tr><tr><td rowspan="13">Conceptual Framework</td><td>Sprague, 1980, [127]</td><td>MIS Q</td><td>5</td><td>*[20]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>*[11]</td><td></td><td>[10]*[57]**[96]</td><td></td><td></td></tr><tr><td>Keen, 1981, [70]</td><td>MIS Q</td><td>4</td><td></td><td></td><td></td><td></td><td>[47]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>[109]</td><td></td><td></td><td>**[82]</td><td>[92]</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Franz et al., 1981, [43]</td><td>DS</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>*[79]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Huber, 1981, [65]</td><td>MIS Q</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[88]</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Hackathorn &amp; Keen, 1981, [54]</td><td>MIS Q</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>*[95]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Bonczek et al., 1981, [18]</td><td>OR</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>**[105]</td><td></td><td></td></tr><tr><td>Barki &amp; Huff, 1985, [17]</td><td>IM</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>*[96]</td><td></td><td></td></tr><tr><td>Turban &amp; Watkins, 1986, [131]</td><td>MIS Q</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>**[37]</td><td></td><td></td><td></td><td>**[142]</td><td></td><td></td></tr><tr><td>Goslar, 1986, [50]</td><td>JMIS</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[15]</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Santos &amp; Bariff, 1988, [116]</td><td>MS</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[139]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Silver, 1990, [121]</td><td>ISR</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[62]</td><td></td><td></td><td></td><td></td></tr><tr><td>Silver, 1991, [122]</td><td>MIS Q</td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>[81]</td><td></td><td></td><td></td><td></td><td></td><td>**[38]*[10]</td><td></td><td></td></tr><tr><td>George, 1991, [46]</td><td>JMIS</td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>*[95]</td><td>*[94]</td><td></td><td>[16]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 1. Connections between DSS cited articles and BI&A research. (Note: BI articles are not annotated; \* indicates that the article appeared previously; \*\* indicate BA articles.) References [14–18.20.21,23.35–41.43.44.46.47.50.53.57.61–63.68.74.77.79.81.82,84.85.88–91.93–96.98.105.109–111.114–116.118.119.121 125,131,133,135,139,140,142] are utilized only in the figure.

## 5.2. Extension of the data management system and database

New enabling technologies extend the capabilities envisioned by a traditional DSS framework. Multiple types of data are now available to the analyst as shown on the left-hand side of Fig. 2, and the more varied the data types considered, the more complex the BI&A system. Tradi tional structured, transactional data were available to Sprague [127] and were supplemented with external, non-transactional, non-account ing data. However, the advent of accessible cloud computing and rapid transference technologies such as 5G extend traditional DBMS to include unstructured and semi-structured data and to reach further bevond organizational boundaries.

To handle big data at speed and high velocity, stream processing is a technology often implemented with Artificial Intelligence (AI) to continuously query the data stream and detect prescribed conditions within a small timeframe of receiving data. On the other hand, batch processing allows data to build to a point and then treats them as a group. Technologies such as a lambda architecture are designed for big data to take advantage of both batch processing and near real-time stream processing with a hybrid approach [86].

Data are collected in a holding area sometimes called a ‘data lake [112,48] and retrieved for processing through Data Wrangling, the process of identifying, collecting, merging, and preprocessing one or more data sets to make data useful for analytics or to train a machine learning model [69]. Data Cleansing is needed to fix messy data such as handling missing values and inconsistencies, removing outliers for consistency and accuracy, converting data types, or normalizing data. Data can then be loaded for processing through a traditional ETL (extract, transform, load) process or using a newer practice called data prep as an agile process [112].

Data can be loaded into a consolidated or distributed enterprise data warehouse and accessed for analysis with a DBMS. Specialized databases called data marts for users with specific needs are often created. In addition, new technologies allow massive amounts of data to be distributed across multiple processors using a computing cluster and processed using systems such as Hadoop or Spark [69 ] in timeframes that are reasonable for decision makers.

![](/api/attachments/MTSJ9UMC/fulltext/images/b438b55ddfb7876de12842467795e1644d017820822c1c93df23cf0af7c535ba.jpg)  
Fig. 2. Architecture for BI&A and Big Data Systems compared to classical DSS. Note: Classical DSS components are indicated by darker shading

## 5.3. Extension of the model management system and model base

Sprague [127] envisioned a Model Management System that accessed a model base consisting of strategic, tactical and operational models along with model building blocks that were embedded in the DSS with a robust modeling language and a management system. As intelligent methods such as AI became available in the 1980s, DSS exploited these advances to better model human problem-solving ca pabilities [51]. DSS applications in domains such as healthcare have been successfully developed and continue to demonstrate the feasibility and usefulness of these approaches [55]. These intelligent-DSS (IDSS) incorporate methods such as rule-based techniques, probabilistic and decision-theoretic models, machine learning (ML), and uncertainty representation to impact both the process of, and outcomes from, deci sion making [104].

Current ML and AI techniques continue this vision but revolutionize the types of models that can be developed. Today the modeler can create exploration models using ML in a sandbox environment and generally use one of three approaches: supervised learning driven by the modeler to produce a specific result; unsupervised learning to identify hidden structure in data; and reinforcement learning that provides a reward in a semi-supervised learning algorithm [69].

Big data challenge the decision maker with their size and scope to find patterns that are not observable with earlier graphical representa tions. Data visualization technologies have evolved to provide flexible and accessible renderings of very large datasets to support interpretation by interactively pairing the representation to the type of data. For example, high cardinality, or many unique values, can be handled by allowing the user to zoom into specific regions of the data representation or to filter data easily. In addition, location analytics can combine geographical information with data of interest, and forecasting can be incorporated.

## 5.4. Extension of the user interface

As previously mentioned, the User Interface for a DSS was envisioned as handling a variety of dialogue styles with the user, accommodating user actions with different media types, presenting data in a variety of formats, and providing flexible support for the user’s personal knowledge base. The user interface of today has grown in sophistication and support for multi-criteria decision making through features such as dashboards, and it expands the essential features discussed by Sprague [127]. Fig. 2 suggests that users interact with the BI&A user interface with a purpose of descriptive, predictive or prescriptive analytics, or adhoc exploration of data. Descriptive analytics provides statistical infor mation about the data and uses techniques such as clustering or asso ciation to find linkages between data elements. Predictive analytics uses techniques such as regression or neural networks to predict a future state based on historical patterns in data. Prescriptive analytics attempts to find optimal outcomes using methods such as optimization or genetic algorithms. Finally, ad-hoc exploration, as the name suggests, is a nondirected search for interesting patterns that may assist the decision maker.

## 5.5. Extension of the decision maker role

The classical view of the user or manager is a person faced with a problem requiring a decision, taking action, and being held accountable for the consequences. In Fig. 2, that person is shown as the Decision Maker. Sprague [127], among others, recognized that other roles, though not necessarily distinct people, are needed in the development and operation of a DSS. For example, an intermediary or staff assistant was suggested as a possible aide to the decision maker. Fig. 2 indicates that there could be intermediaries between the decision maker and the DSS, or they may be the same person. In addition, Sprague suggested a DSS builder to configure the DSS, a technical supporter to add compo nents, and a ‘toolsmith’ to develop new technology. We have not delineated these engineering-type roles in Fig. 2 and focus instead on the decision maker.

Fig. 2 shows three distinct, but sometimes overlapping, types of system users and a decision maker who may be a separate person or one of the three users [104.138]. The Business User is generally interested in specific information to address tailored questions. For example, dash boards can be created to deliver specific information from a data mart, or pre-developed queries can be accessed by the business user. In gen eral, the business user is a consumer of descriptive and predictive ana lytics targeted to their business decision. The second type of user is referred to as an Analytics Expert, and this person is able to perform analysis using sophisticated analytics software and data preparation techniques. The analytics expert has computer coding skills applicable to some applications and the ability to employ visualization technolo gies to aid analysis.

The Data Scientist is an adaptable, highly technically adept person who has the capability to move freely throughout the process-flow from back-end data sourcing to front-end decision making. This person has advanced computer coding and statistical analysis skills that allow them to move data into and bring data from the data lake, utilize cluster computing, interact with data wherever they reside, create new models and visualizations, interpret results, develop innovations usingaudits data, and guide decision making for wicked problems. In many organi zations, the data scientist role is fulfilled by several people with deep expertise in one or more of these skillsets. We suggest the fluidity of the role in the various organizations represented in our practitioner in terviews by indicating in Fig. 2 that the Data Scientist can directly access any component.

Based on our interviews with practitioners and managers shown in Table 1, the data scientist role may depend on the company and in dustry. In consulting companies, data scientists may support multiple projects in a data architect role. However, in a single-industry company, data scientists provide insight directly to a decision maker who may be a manager. In technology-focused companies, the data scientist may be a decision maker. We use the term ‘decision maker’ to indicate someone who provides an answer or a recommendation to a decision problem; the decision maker is not necessarily an implementor, and there may be additional managerial oversight. Thus, we envision the data scientist as adaptable to their role depending on the industry. However, in all cases, the data scientist is highly technical with advanced computer science and statistical skills that give them the ability to move throughout the computing environment.

## 5.6. Extension of the organizational context

Sprague [127] expressed the difference between a Management In formation System (MIS) and a DSS in terms of organizational use. At the lowest level was Electronic Data Processing (EDP) with a focus on data, storage, processing, flows and reporting at the operational level. Moving up a level, an MIS had an information focus aimed at middle level managers, structured information flow, integration of business func tionalities, and inquiry and report generation. A DSS was viewed as decision-focused aimed at executive decision makers, an emphasis on flexibility and response time, user initiation and control, and support for individual differences. It was recognized early in the development of DSS that providing decision support within an organizational context leads to management control issues [54].

Thus, Fig. 2 shows an extended organizational context for BI&A systems that includes data management and governance, audits, secu rity, legal and regulatory considerations that reach outside of the organizational boundary [104,138]. Governments have passed laws regulating data storage and use, and the value of data as an asset has led to the need to secure data. Internally, data require management and clear governance to ascribe access, modification, and usage rules.

This study demonstrates that the BI&A and big data systems archi tecture has expanded Sprague’s original DSS architecture. The features and components of a DSS are clearly visible. However, one might argue that the data lake, sandbox, and data scientist create a complementary data architecture to the DSS that could not be envisioned by Sprague due to the significant advances in enabling technologies required for their implementation and use. Fig. 2 supports this view as well. Thus, we suggest that BI&A can be considered a special category of DSS that could be associated with ‘data-driven DSS’ [106]. Consequently, we turn to BI&A research opportunities arising from DSS literature.

## 6. Opportunities for BI&A research based on DSS

The review of early DSS literature and citation patterns in BI&A papers along with our reconciled architecture led us to identify research gaps in BI&A literature than could be advanced with a DSS-informed agenda for future research. In this section we present these gaps and a research agenda leveraging the proposed classification and relevant foundational DSS papers that have not been utilized in BI&A research.

## 6.1. Conceptual frameworks for BI&A

More research is needed to reconcile various definitions of what constitutes BI&A in a similar way to DSS. DSS research has a solid conceptual foundation including taxonomies of decision support sys tems that have been commonly accepted (e.g. [8,122,107]). Analyzing recent BI&A publications, we conclude that there is no clear taxonomy for BI&A systems, and, moreover, there is confusion about how to define such a system to differentiate it from a traditional Business Information System (BIS). Holsapple et al. [60] proposed a classification of business analytics (BA) from six different definitional perspectives and proposed a framework that classifies the relationship between these perspectives. The factors underlining these perspectives include: (1) a movement or culture of fact-based decision making; (2) a collection of BA practices and technologies; (3) an organizational transformation process changing the enterprise system; (4) a set of capabilities; (5) specific activities to drive business actions; and (6) a decisional paradigm to improve deci sion making. They put forward these perspectives as well justified within the BA paradigm and definitions, with a clear link to the purpose of the BA systems as supporting organizational decision making. Arnott et al. [11] similarly identified BI use for decision making and linked it to classical DSS frameworks proposed by Gorry and Scott Morton [49]. They looked at classes of systems and task types as major factors for defining the unique role of BI in organizations. Both of these groups of authors cite some DSS literature, in particular seminal books. However, there is an untapped opportunity to correlate these and similar attempts with the foundational DSS research papers, particularly those we have identified as discussing new models and approaches in decision support (e.g., [66]). We call for a comprehensive study of the primary di mensions of BI&A that can be utilized to define different classes of BI&A.

## 6.2. Design & implementation of BI&A systems

## 6.2.1. BI&A stakeholders, users and roles

In the papers reviewed in this study and from the empirical data collected from the BI&A practitioners, we conclude that during the BI&A process cycle there are many roles and stakeholders who are involved in the system design, development and operation. DSS researchers identi fied five such roles. BI&A literature suggests a number from three pri mary users [104] to nine [137]. Our empirical study with BI&A practitioners confirmed the generic roles of decision makers and linked them to organizational needs. More studies are required to determine who are and should be involved at various stages of systems develop ment, and the optimal, necessary and sufficient constitution of the BI&A team to make such system implementation and deployment process viable. Such studies could also inform universities on the types of courses to be offered to train future BI&A specialists.

## 6.2.2. Process model for BI&A

In this paper we proposed a process model to operationalize the generic BI&A architectural components. The process model was devel oped and validated through discussion with senior practitioners. Further empirical studies are required to substantiate the results and complete the loop of design theory development for BI&A.

This leads to the next research gap related to the need for more theoretical/conceptual BI&A frameworks to be proposed, tested and evaluated [2,103]. The methodologies for DSS development have been studied by Keen [72] and reviewed by Alavi and Joachimsthaler [4]. Alavi and Joachimsthaler conducted a comprehensive study of the roots of design & implementation for DSS that provides a useful conceptual research framework as a starting point.

From these early studies the overall assumption of the evolutionary nature of DSS development has been formalized as successive proto typing driven by internal and environmental causal factors [13]. There are some attempts to propose a similar set of development methods for BI&A systems. There are also research studies that have tried to apply EIS/DSS development methodologies to BI [113]. However, there is still room for further analysis of the similarities and differences in unique methodological approaches to BI&A systems development, especially taking into consideration their dependency on vendor-based or open source basic functionality and their need for adaptation and custom ization to users and organizational requirements that are typically dy namic and subject to change over time.

## 6.3. Business value & organizational use of BI&A

The needs and objectives for BI&A implementation and use are argued mainly from the industry needs and requirements perspective. Such arguments were defined by Holsapple et al. [60] as “BI move ments.” In a recent study, Arnott et al. [10] investigated whether busi ness intelligence systems are different from decision support systems and other business information systems. Their conclusion was that all three systems represent IT artefacts that support managerial decision making, with “traditional” BI being focused on processing structured data for well-understood process and decisions. We support their conclusion that BI&A systems should have a major objective of providing timely insight into organizational operational processes. This requires further research into the nature of organizational decisionmaking processes from BI&A business value perspectives. The seminal studies on the nature of organizational decision making by Huber [65] and Keen [70], as well as studies of MIS [49] provide useful lenses in such research endeavors.

More empirical field studies or analyses of secondary case studies should be undertaken to look at typical BI outcomes in specific devel opment contexts. There is an opportunity to look back at older DSS papers about organizational use that propose innovative roles for DSS within organizational settings to identify relevant lessons learned, especially those related to specific industrial contexts such as airline management [76] or public sector DSS [59]. Such studies could also help prevent future BI&A failures by applying lessons from the past.

## 6.4. Cognition & decision making using BI&A

In our analysis we came across many theoretical frameworks for BI&A that were not informed by seminal DSS literature. There is a lack of research focused on how BI&A affects decision making. On the other hand, we identified a few DSS papers that could further enhance and enrich future development for BI&A. DSS history is replete with knowledge-based and AI-informed models that can provide fodder for BI&A systems. For example, Knowledge-based-DSS [27], Intelligent DSS [108], Active DSS [67], and Knowledge Management-based DSS [22] could spur new ideas for BI&A. DSS literature can also provide a variety of useful architectural frameworks and lessons learned to avoid the mistakes that resulted in DSS abandoning the integration of AI for de cades. This consideration addresses one of the suggestions we obtained from the empirical study participants to include AI features into BI&A functionality.

## 6.5. Methodological guidelines for researching BI&A

The methodologies for conducting rigorous research on BI&A have not been a subject to rigorous investigation. Since the short history of BI&A is dominated by a practitioner-oriented literature, a danger of research bias should be considered. If the evidence is derived from the vendors’ case studies, alternative data sources should be sought to ensure a balanced answer to the research questions. Although case study research is a suitable research method to study implementations of BI&A systems in organizational contexts, a critical realist [97] methodology can be a more suitable epistemological position than an interpretive one. If interpretive perspective is chosen still, a carefully selected data source should be selected and well justified as part of the research design. For example, examination of related documents using protocol analysis and looking at the BI&A process using, for example, the proposed DSSgrounded process-level architecture, could provide relevant sources for triangulation and critical reference points.

## 6.6. Summary of DSS-informed research opportunities in BI&A

By leveraging uncited DSS foundational literature, we suggest that there are opportunities to extend BI&A research. In Table 6 we connect BI&A research gaps and associated questions to relevant DSS references and methods.

## 7. Conclusions and contributions

This paper focused on the underlying roots of BI&A and investigated the linkage between foundational DSS research and contemporary topics of ‘business intelligence’, ‘analytics’ and ‘big data’. We argue that BI&A is fundamentally a subfield of DSS that seeks to convert more data into deeper insight, but it has lost its connection to DSS foundational liter ature. To demonstrate, we presented a systematic review of foundational DSS articles and corresponding BI&A literature that cites them. By classifying DSS research into four areas: conceptual frameworks, design & implementation, business value & organizational use, and cognition & decision making, we uncover research opportunities for BI&A. To further investigate the connection between DSS and BI&A, we developed a BI&A framework collaboratively with practitioners and mapped it to classical DSS components. The result is a comparative, process-level architecture for converting data into insight that reconciles these two research streams. The overall findings were summarized as a set of new research opportunities for BI&A by exploiting unexplored DSS founda tional literature, especially in cognition & decision making and con ceptual frameworks.

Our contributions to the literature are:

• a structured literature review evaluating the linkage between BI&A and DSS research;

• a classification of DSS research into four categories;

• a comparative, process-level architecture for BI&A mapped to DSS components that integrates these two research streams;

• future opportunities for BI&A research by leveraging foundational DSS literature.

When viewed in the larger context of DSS, BI&A offers the promise of converting more data into deeper insight to improve cognition and de cision making. DSS literature demonstrates the business value that can be rendered from a data-driven approach. However, as DSS history demonstrates, the organizational context, culture, system design, and implementation strategies all influence how well this goal is achieved. DSS research also shows that clear conceptual frameworks and roles are needed to coordinate the workforce toward organizational goals. This paper takes a step toward opening the black box of BI&A in organiza tions and suggesting opportunities to leverage the rich research foun dations of the past.

Our research has limitations. The sample of papers we analyzed could be expanded. For example, we could have included article ab stracts in our search criteria or have included articles from other fields such as psychology that are embedded in DSS literature. Although the main conclusions of our study are well illustrated based on our sample, additional research opportunities for BI&A could have been uncovered with a broader literature review.

Table 6  
BI&A research gaps and opportunities for future research leveraging DSS.

<table><tr><td>Research gap</td><td>Suggested research questions</td><td>Suggested relevant DSS references</td><td>Research methods and techniques</td></tr><tr><td>Conceptual frameworkBI&amp;A definitions</td><td>What are the distinct types of BI&amp;A systems? What primary dimensions should be considered to differentiate BI&amp;A taxonomy?</td><td>[6,8,56,66,122]</td><td>Surveys; Multiple case studies; Systematic literature analysis</td></tr><tr><td>Design &amp; implementationBI&amp;A stakeholders, users and roles</td><td>Who are the stakeholders in BI&amp;A implementation and use? What impact does the constitution of the team make on the organizational success of BI&amp;A? What skill sets are needed for an effective BI&amp;A team?How is team composition related to the problem to be solved?</td><td>[5,72,120]</td><td>Case studies; Surveys; In-depth interviews</td></tr><tr><td>Process model of BI&amp;A design</td><td>What are the methods for effective design &amp; implementation of BI&amp;A?Are agile methods appropriate for BI&amp;A? How to evaluate BI&amp;A?</td><td>[2,3,4,72,75]</td><td>Multiple case studies; Action research</td></tr><tr><td>Business value &amp; organizational useObjectives and drivers for BI&amp;A use to improve organizational performance</td><td>How can BI&amp;A implementation contribute to improved organizational performance? What organizational functions are most positively impacted by BI&amp;A?</td><td>[65,71,49,101,29,72,136]</td><td>Case studies; Secondary case studies; Action research; Design Science research</td></tr><tr><td>Cognition &amp; decision makingTheoretical considerations of decision making</td><td>How does BI&amp;A affect decision making? Is AI more effective than human decision making in BI&amp;A? How are unusual events treated in BI&amp;A? How does stress affect decision making in BI&amp;A use?</td><td>[27,66,108,67,72,129]</td><td>Field experiments; Design Science research; Action research</td></tr><tr><td>Research MethodsMethodological guidelines</td><td>How can BI&amp;A research be conducted to ensure rigorous and quality outcomes and insights? What methods are needed to generalize BI&amp;A empirical research?</td><td>[64,72,130]</td><td>Critical realism-based case studies; Protocol analysis; Process tracing</td></tr></table>

## Public data

The data and figures used in this article can be found on my public Google Drive site by following the link: https://drive.google.com/driv e/folders/11TejkOVP7ouB4rELQXmu2wnQjOI0iPHP?usp=sharing.

## Acknowledgements

We thank the data scientists and BI&A practitioners who wish to remain anonymous for their consultations and discussions about BI&A architectures. We also sincerely thank the reviewers whose comments and suggestions improved the quality of the paper.

Appendix A. Definitions of business intelligence (BI) and business analytics (BA) in literature

<table><tr><td>Type</td><td>Year</td><td>Author</td><td>Definition</td></tr><tr><td>BI</td><td>1958</td><td>Luhn [83]</td><td>The ability to apprehend the interrelationships of presented facts in such a way as to guide action toward a desired goal</td></tr><tr><td>BI</td><td>2004</td><td>Negash [100]</td><td>BI systems combine data gathering, data storage, and knowledge management with analytical tools to present complex internal and competitive information to planners and decision makers</td></tr><tr><td>BI</td><td>2006</td><td>Davenport [30]</td><td>The term IT people use for analytics and reporting processes and software. BI... encompasses a wide array of processes and software used to collect, analyze, and disseminate data, all in the interests of better decision making</td></tr><tr><td>BA</td><td>2007</td><td>Davenport &amp; Harris [32]</td><td>BA is concerned with the extensive use of data, statistical and quantitative analysis, explanatory and predictive model, and fact-based management to drive decisions and actions</td></tr><tr><td>BI</td><td>2008</td><td>Hayen [58]</td><td>BI applications include the activities of DSS, query and reporting, online analytical processing (OLAP), statistical analysis, forecasting and data mining ... a mainstream activity within the broad array of DSS deployments</td></tr><tr><td>BA</td><td>2012</td><td>Boyd [19]</td><td>Analytics is the scientific process of transforming data into insight for making better decisions</td></tr><tr><td>BI</td><td>2014</td><td>Davenport [31]</td><td>Tools to support data-driven decisions, with emphasis on reporting</td></tr><tr><td>BA</td><td>2014</td><td>Davenport [31]</td><td>Focus on statistical and mathematical analysis for decisions</td></tr><tr><td>BA</td><td>2014</td><td>Holsapple, Lee-Post &amp; Pakath [60]</td><td>Evidence-based problem recognition and solving that happen within the context of business situations</td></tr><tr><td>BI</td><td>2016</td><td>Larson &amp; Chang [80]</td><td>Gartner (2013) and Halpern (2015) have extended BI to be an umbrella term which includes applications, tools, infrastructure, and practices to enable access and analysis of information to optimize performance and decision-making</td></tr><tr><td>BA</td><td>2017</td><td>Seddon, Constantinidis, Tamm, &amp; Dod [117]</td><td>Business analytics (BA) as the use of data to make sounder, more evidence-based business decisions,</td></tr><tr><td>BI</td><td>2018</td><td>Power &amp; Heavin [107]</td><td>Umbrella term that describes a set of concepts and methods to improve business decision making by using fact-based decision support systems; also refers to a set of software tools that can be used to extract and analyze data from corporate databases</td></tr><tr><td>BA</td><td>2018</td><td>Delen &amp; Ram [33]</td><td>Business analytics is the art and science of discovering insight – by using sophisticated mathematical, statistical, machine learning, and network science methods along with a variety of data and expert knowledge – to support better and faster/timely decision making</td></tr><tr><td>BI</td><td>2019</td><td>Arnott, Gao, Lizama, Meredith &amp; Song [10]</td><td>BI systems are large-scale systems that combine information technologies, data reporting, and analytic processes in order to support decision making in an organization</td></tr></table>

## References

[1] N.U. Ain, G. Vaia, W.H. DeLone, M. Waheed, Two decades of research on business intelligence system adoption, utilization and success – a systematic literature review, Decis. Support. Syst. 125 (2019) 113113.

[2] J.A. Akoka, A framework for decision support systems evaluation, Inf. Manag. 4 (3) (1981) 133–141.

[3] M. Alavi, J.C. Henderson, An evolutionary strategy for implementing a decision support system, Manag. Sci. 27 (11) (1981) 1309–1323.

[4] M. Alavi, E.A. Joachimsthaler, Revisiting DSS implementation research: a metaanalysis of the literature and suggestions for researchers, MIS Q. 16 (1) (1992) 95–116.

[5] S. Alter, Why is man-computer interaction important for decision support systems? Interfaces 7 (2) (1977) 109–115.

[6] S. Alter, A taxonomy of decision support systems, Sloan Manag. Rev. 19 (1) (1977) 39–56 (pre-1986).

[7] S. Alter, Development patterns for decision support systems, MIS Q. 2 (3) (1978) 33–42.

[8] S. Alter, Decision Support Systems: Current Practice and Continuing Challenges, Addison-Wesley, Reading, MA, 1980.

[9] G. Ariav, M.J. Ginzberg, DSS design: a systemic view of decision support, Commun. ACM 28 (10) (1985) 1045–1052.

[10] D. Arnott, S. Gao, F. Lizama, R. Meredith, Y. Song, Are business intelligence systems different to decision support systems and other business information systems? Proc. Aust. Conf. Inform. Syst. (2019) 624–634.

[11] D. Arnott, F. Lizama, Y. Song, Patterns of business intelligence systems use in organizations, Decis. Support. Syst. 97 (2017) 58–68.

[12] D. Arnott, G. Pervan, A critical analysis of decision support systems research, J. Inf. Technol. 20 (2) (2005) 67–87.

[13] D. Arnott, Decision support systems evolution: framework, case study and research agenda, Eur, J. Inf, Syst, 13 (4) (2004) 247–259.

[14] A. Audzeyeva, R. Hudson, How to get the most from a business intelligence application during the post implementation phase? Deep structure transformation at a UK retail bank Fur J Inf Syst 25 (1) (2016) 29–46

[15] E. Baker, L. Chasalow, Factors contributing to business intelligence success: the impact of dynamic capabilities, Am. Conf. Inform. Syst. (2015).

[16] E. Baker, Relational model bases: a technical approach to real-time business intelligence and decision making, Commun. Assoc. Inf. Syst. 33 (1) (2013) 23.

[17] H. Barki, S.L. Huff, Change, attitude to change, and decision support system success, Inf. Manag, 9 (5) (1985) 261–268.

[18] R.H. Bonczek, C.W. Holsapple, A.B. Whinston, A generalized decision support system using predicate calculus and network data base management, Oper. Res. 29 (2) (1981) 263–281.

[19] A.E. Boyd, Profit Centre: Revisiting ‘What is analytics’. Analytics Magazine, July/ August 6. Available from. http://analytics-magazine.org/profit-center-revisiti ng-what-is-analytics/.INFORMS, 2012.

[20] M.K. Brohman, M. Parent, M.R. Pearce, M. Wade, The business intelligence value chain: Data-driven decision support in a data warehouse environment: An exploratory study, in: Proceedings of the 33rd Annual Hawaii Internationa Conference on System Sciences, 2000.

[21] D. Bumblauskas, D. Gemmill, A. Igou, J. Anzengruber, Smart maintenance decision support systems (SMDSS) based on corporate big data analytics, Expert Syst. Appl. 90 (2017) 303–317.

[22] F. Burstein, S.A. Carlsson, Decision support through knowledge management, in: Handbook on Decision Support Systems 1, Springer, Berlin, Heidelberg, 2008, pp. 103–120.

[23] G. Cao, Y. Duan, The affordances of business analytics for strategic decisionmaking and their impact on organizational performance, Proc. Pacific Asia Conf. Inform, Syst, 255 (2015).

[24] T. Chee, LK. Chan. M.H. Chuah. C.S. Tan, S.F. Wong, W. Yeoh. Business intelligence systems: state-of-the-art review and contemporary applications. Symposium Prog, Inform. Commun, Technol. 2 (4) (2009) 16–30.

[25] H. Chen, R.H. Chiang, V.C. Storey, Business intelligence and analytics: from big data to big impact. MIS O. (2012) 1165–1188.

[26] C. Churchman, Wicked problems, Manag. Sci. 14 (4) (1967). B-141–B-146.

[27] J.F. Courtney Jr., D.B. Paradice, N.H. Ata Mohammed. A knowledge-based DSS for managerial problem diagnosis, Decis. Sci. 18 (3) (1987) 373–399

[28] C. Csaki, ´ The Mythical Decision Maker: Models of Roles in Decision Making. Encyclopedia of Decision Making and Decision Support Technologies, IGI Global. 2008. pp. 653–660.

[29]. K.F. Curley, LL. Gremillion, The role of the champion in DSS implementation, Inf Manag, 6 (4) (1983) 203–209.

[30] T.H. Davenport, Competing on analytics, Harv. Bus. Rev. 84 (1) (2006) 98.

[31] T.H. Davenport, How strategists use “big data” to support internal business decisions, discovery and production, Strateg. Leadersh. 42 (4) (2014) 45–50.

[32] T.H. Davenport, J.C. Harris, The architecture of business intelligence, in: Competing on Analytics: The New Science of Winning, 2007. Available from, htt ps://whitepapers.em360tech.com/wp-content/files\_mf/white\_paper/Accenture\_ BI\_analytics\_white\_paper.pdf.

[33] D. Delen, S. Ram, Research challenges and opportunities in business analytics, J. Business Anal. 1 (1) (2018) 2–12.

[34] D. Dinis, A.P. Teixeira, A. Barbosa-Póvoa, ForeSim-BI: a predictive analytics decision support tool for capacity planning, Decis, Support, Syst. 131 (2020) 113266.

[35] G. Dodson, D. Arnott, G. Pervan, The use of business intelligence systems in Australia, Proc, Aust, Conf, Inform, Syst, 74 (2008)

[36] J.J. Donovan, S.E. Madnick, Institutional and ad hoc DSS and their effective use, Database Adv. Inf. Syst. 8 (3) (1977) 79–88

[37] D.A. Doppner, ¨ D. Schoder, H. Siejka, Big data and the data value chain: Translating insights from business analytics into actionable results-the case of unit load device (ULD) management in the air cargo industry, in: Proceedings of the European Conference on Information Systems. Munster, GE, 2015, p. 7.

[38] S. Ebrahimi, K. Hassanein, Empowering users to detect data analytics discriminatory recommendations, Proc. Int. Conf. Inform. Syst. 2886 (2019).

[39] H. El Sherif, O.A. El Sawy, Issue-based decision support systems for the Egyptian cabinet. MIS O. (1988) 551–569.

[40] H.B. Eom, S.M. Lee, Decision support systems applications research: a bibliography (1971–1988), Eur. J. Oper. Res. 46 (3) (1990) 333–342.

[41] S. Eom, DSS, BI, and data analytics research: current state and emerging trends (2015–2019), Int. Conf. Decision Support Syst. Technol. (2020) 167–179.

[42] E. Foley, M.G. Guillemette, What is business intelligence? Int. J. Business Intellig. Res. 1 (4) (2010) 1–28.

[43] L.S. Franz, W.M. Lee, J.C. Van Horn, An adaptive decision support system for academic resource planning, Decis. Sci. 12 (2) (1981) 276–293.

[44] W.L. Fuerst, P.H. Cheney, Concepts, theory, and techniques: factors affecting the perceived utilization of computer-based decision support systems in the oil industry, Decis. Sci. 13 (4) (1982) 554–569.

[45] S. Gbosbal, S.K. Kim, Building effective intelligence systems for competitive advantage: the problems with business intelligence systems, Sloan Manag. Rev. 28 (1) (1986) 49.

[46] J.F. George, The conceptualization and development of organizational decision support systems, J. Manag. Inf. Syst. 8 (3) (1991) 109–125.

[47] M. Gibson, D. Arnott, I. Jagielska, Evaluating the intangible benefits of business intelligence: Review & research agenda, in: Proceedings of the 2004 IFIP International Conference on Decision Support Systems: Decision Support in an Uncertain and Complex World. Prato, Italy, 2004, pp. 295–305.

[48] A. Gorelik. The Enterprise Big Data Lake: Delivering the Promise of Big Data and Data Science. O’Reilly Media, Available from, https://www.oreilly.com/library/ view/the-enterprise-big/9781491931547/ch01.html. 2019

[49] G.A. Gorry, M.S. Scott Morton, A framework for management information systems, Sloan Manag. Rev. 30 (3) (1989) 49–61.

[50] M.D. Goslar, Capability criteria for marketing decision support systems, J. Manag. Inf. Syst. 3 (1) (1986) 81–95.

[51] H.W. Gottinger, P. Weimann, Intelligent decision support systems, Decis. Support. Syst. 8 (4) (1992) 317–332.

[52] P. Gray, Business intelligence: A new name or the future of DSS, in: T. Bui H. Sroka. S. Stanek. J. Gohuchowski (Eds.). DSS in the Uncertainty of the Internet age. University of Economics. Katowice. 2003.

[53] G.I. Green, C.T. Hughes, Effects of decision support systems training and cognitive style on decision process attributes, J. Manag, Inf. Syst. 3 (2) (1986) 83–93.

[54] R.D. Hackathorn, P.G. Keen, Organizational strategies for personal computing in decision support systems, MIS O. (1981) 21–27.

[55] P.D. Haghighi, F. Burstein, A. Zaslavsky, P. Arbon, Development and evaluation of ontology for intelligent decision support in medical emergency management for mass gatherings, Decis. Support. Syst. 54 (2) (2013) 1192–1204.

[56] J. Hansen, L.E. Heitger, L. McKell, Computer-aided modelling of decision-support systems, J. Oper. Res. Soc. 29 (8) (1978) 789–802.

[57] N.R. Hassan, The origins of business analytics and implications for the information systems field, J. Business Anal. 2 (2) (2019) 118–133.

[58] R.L. Hayen, Direction in business intelligence: an analysis of applications, Proc Am. Conf. Inform. Syst. 334 (2008)

[59] J.C. Henderson, D.A. Schilling, Design and implementation of decision support systems in the public sector, MIS Q. (1985) 157–169.

[60] C. Holsapple, A. Lee-Post, R. Pakath. A unified foundation for business analytics Decis, Support, Syst, (2014) 130–141

[61] C.K. Hou, K.N. Papamichail, The impact of integrating enterprise resource planning systems with business intelligence systems on decision-making performance: An empirical study of the semiconductor industry, Int. J. Technol Pol. Manag. 10 (3) (2010) 201–226.

[62] W. Hou, S. Gao, Managerial use of mobile business intelligence: an exploratory study, Proc. Pacific Asia Conf. Inform. Syst. 61 (2017).

[63] G. Houdeshel, H.J. Watson, The management information and decision support (MIDS) system at Lockheed-Georgia, MIS Q. (1987) 127–140.

[64] R.A. Howard, Decision analysis: practice and promise, Manag, Sci, 6 (1988 679–695.

[65] G.P. Huber, The nature of organizational decision making and the design of decision support systems. MIS O. 5 (2) (1981) 1–10.

[66] G.P. Huber, Cognitive style as a basis for MIS and DSS designs: much ado about nothing? Manag, Sci, 29 (5) (1983) 567–579.

[67] M.T. Jelassi, K. Williams, C.S. Fidler, The emerging role of DSS: from passive to active. Decis, Support, Syst, 3 (4) (1987) 299–307.

[68] B. Johansson, D. Alkan, R. Carlsson, Self-Service BI does it Change the Rule of the Game for BI Systems Designers. Proceedings of the CEUR Workshop 1420, 2015,

[69] M.T. Jones, Data, structure, and the data science pipeline. IBM Article (2018) 1–9

[7o] P.G. Keen, Value analysis: justifving decision support systems, MIS O. 5 (1)

[71] P G. Keen. Adaptive design for decision support systems DATABASE Ady Inform Svst, 1. (4–5) (1980).15–25

[72] P.G. Keen, Decision support systems: translating analytic techniques into usefu tools, Sloan Manag, Rey, 21 (3) (1980) 33 (pre-1986).

[73] M. Ketokivi, S. Mantere, Two strategies for inductive reasoning in organizational research, Acad. Manag. Rev. 35 (2) (2010) 315–333.

[74] N.G. Kim, S.K. Kim, How user’s participation in feasibility study enhances use of business intelligence systems, J. Inform. Technol. Appl. Manag. 24 (3) (2017) 1–21.

[75] W.R. King, J.I. Rodriguez, Note—participative design of strategic decision support systems: an empirical assessment, Manag. Sci. 27 (6) (1981) 717–726.

[76] R.L. Klaas, A DSS for airline management, in: ACM SIGMIS Database: The DATABASE for Advances in Information Systems 8(3), 1977, pp. 3–8.

[77] O. Kohnke, T.R. Wolf, K. Mueller, Managing user acceptance: an empirica investigation in the context of business intelligence standard software, Int. J. Inf Syst. Chang. Manag. 5 (4) (2011) 269–290.

[78] M. Kowalczyk, P. Buxmann, J. Besier, Investigating business intelligence and analytics from a decision process perspective: a structured literature review, Eur. Conf. Inform. Syst. 126 (2013).

[79] U. Kulkarni, J.A. Robles-Flores, Development and validation of a BI success model, in: Proceedings of the Nineteenth Americas Conference on Information Systems. Chicago, Illinois, 2013, pp. 15–17.

[80] D. Larson, V. Chang, A review and future direction of agile, business intelligence, analytics and data science, Int. J. Inf. Manag. 36 (5) (2016) 700–710.

[81] X. Li, J.P.A. Hsieh, A. Rai, Motivational differences across post-acceptance information system usage behaviors: an investigation in the business intelligence systems context, Inf. Syst. Res. 24 (3) (2013) 659–682.

[82] N. Ludwig, S. Feuerriegel, D. Neumann, Putting big data analytics to work: feature selection for forecasting electricity prices using the LASSO and random forests, J. Decis. Syst. 24 (1) (2015) 19–36.

[83] H.P. Luhn, IBM Systems Journal, 1958. Reported in T. Chee, L.K. Chan, M.H. Chuah, C.S. Tan, S.F. Wong, W. Yeoh, Business intelligence systems: state-of-theart review and contemporary applications, in: Symposium on Progress in Information & Communication Technology 2(4), 2009, pp. 16–30.

[84] D. MacKrell, M. Van den Boogaard, Making sense of business intelligence: proposing a socio-technical framework for improved decision making in not-forprofit organizations, in: Proceedings of the 23rd Australasian Conference on Information Systems, 2012, pp. 1–9.

[85] S. Maldonado, R.G. Gonz´alez-Ramírez, F. Quijada, A. Ramírez-Nafarrate, Analytics meets port logistics: A decision support system for container stacking operations, Decis. Support. Syst. 121 (2019) 84–93.

[86] N. Marz, J. Warren, Big Data: Principles and Best Practices of Scalable Real-Time Data Systems, Manning Publications Co., New York, NY, 2015.

[87] S. Maynard, F. Burstein, D. Arnott, A multi-faceted decision support system evaluation approach, J. Decis. Syst. 10 (3–4) (2001) 395–428.

[90] C.L. Meador, M.J. Guyote, P.G. Keen, Setting priorities for DSS development, MIS 0. 8 (2) (1984) 117–129.

[89] C.L. Meador, D.N. Ness, Decision support systems: an application to corporate planning, Sloan Manag. Rev. 15 (2) (1974) 51 (pre-1986).

[88] W. McHenry, Linking decision artifacts: a means for integrating business intelligence and knowledge management. Electron. J. Knowl. Manag. 14 (2) (2016) 91–102.

[91] N.P. Melville, K. Kraemer, V. Gurbaxani, Information technology and organizational performance: an integrative model of IT business value, MIS Q. 28 (2) (2004) 283–322.

[92] N.P. Melville, O. Zik, Energy Points: A new approach to optimizing strategic resources by leveraging big data, in: Proceedings of the 49th Hawaii International Conference on System Sciences, 2016, pp. 1030–1039.

[93] A.B. Mendes, BI and data warehouse solutions for energy production industry: Application of the CRISP-DM methodology, in: A. Respicio, F. Adam, G. Phillips-Wren, C. Teixeira, J. Telhada (Eds.), Proceedings of the IFIP WG8.3 DSS, Bridging the Socio-Technical Gap in Decision Support Systems. Vol 212 of Frontiers in Artificial Intelligence and Applications, 2010, pp. 211–222.

[94] R. Meredith, P. O’Donnell, A framework for understanding the role of social media in business intelligence systems, J. Decis. Syst. 20 (3) (2011) 263–282.

[95] R. Meredith, P.A. O’Donnell, A functional model of social media and its application to business intelligence, in: A. Respicio, F. Adam, G. Phillips-Wren, C. Teixeira, J. Telhada (Eds.), Proceedings of the IFIP WG8.3 DSS, Bridging the Socio-Technical Gap in Decision Support Systems. Vol. 212 of Frontiers in Artificial Intelligence and Applications, 2010, pp. 129–140.

[96] G.J. Miller, The influence of big data competencies, team structures, and data scientists on project success. in: Proceedings of the JEEE Technology & Engineering Management Conference, 2019, pp. 1–8.

[97] J. Mingers. A. Mutch. L. Willcocks. Critical realism in information systems

[98] A. Mourady, A. Elragal, Business intelligence in support of eGov healthcare decisions, in: Proceedings of the European, Mediterranean & Middle Eastern Conference on Information Systems. Athens, Greece, 2011, pp. 285–293.

[99] S. Negash, P. Gray, Business intelligence, in: Handbook on Decision Support Systems v2, Springer, 2008, pp. 175–193.

[100] S. Negash, Business Intelligence. Communications of the Association for Information Systems. Article 15. 2004, p. 13

[1011 D. Ness. C.R. Sprague. An Interactive Media Decision Support System. Sloan Management Review: Cambridge 14(1). 1972, pp. 51–61.

[102] D. Olson, F. Courtney Jr., Decision Support Models and Expert Systems. Macmillan, New York, 1992.

[103] G. Phillips-Wren, M. Mora, G. Forgionne, J.N.D. Gupta, An integrative evaluation framework for intelligent decision support systems, Eur, J. Oper, Res, 195 (3) (2009) 642–652.

[104] G. Phillips-Wren, L.S. Iyer, U. Kulkarni, T. Ariyachandra, Business analytics in the context of big data: a roadmap for research, Commun. Assoc. Inf. Syst. 37 (1) (2015) 23.

[105] A. Polyakova, M. Loginov, E. Strelnikov, N. Usova, Managerial decision support algorithm based on network analysis and big data, Int. J. Civ. Eng. Technol. 10 (2) (2019) 291–300

[106] D. Power, A Brief History of Decision Support Systems. DSSResources.COM, World Wide Web. version 4.0. 4.1. 2007.

[107] D. Power, C. Heavin, Data-based Decision Making and Digital Transformation, Business Expert Press. 2018

[108] H.R. Rao, R. Sridhar, S. Narain, An active intelligent decision support system—architecture and simulation, Decis. Support. Syst. 12 (1) (1994) 79–91.

[109] A. Riabacke, A. Larsson, M. Danielson, Business intelligence as decision support in business processes: An empirical investigation, in: Proceedings of 2nd International Conference on Information Management and Evaluation (ICIME) 2011, pp. 384–392.

[110] D. Robey, W. Taggart, Human information processing in information and decision support systems, MIS O. (1982) 61–73.

[111] E. Rubin, A. Rubin, The impact of business intelligence systems on stock return volatility, Inf. Manag, 50 (2–3) (2013) 67–75

[112] P. Russom, Data lakes: Purposes, Practices, Patterns, and Platforms. TDWI White Paper, Available: https://www.sas.com/content/dam/SAS/en\_us/doc/whitepape r2/tdwi-data-lakes-108964.pdf, 2017.

[113] E.R. Safwan, R. Meredith, F. Burstein, Towards a business intelligence systems development methodology: Drawing on decision support and executive information systems, in: Proceedings of the Pacific Asia Conference on Information Systems, 2016, p. 136.

[114] E.R. Safwan, R. Meredith, F. Burstein, Business Intelligence (BI) system evolution: a case in a healthcare institution, J. Decis. Syst. 25 (sup1) (2016) 463–475.

[116] B.L. Santos, M.L. Bariff, A study of user interface aids for model-oriented decision support systems, Manag. Sci. 34 (4) (1988) 461–468.

[117] P.B. Seddon, D. Constantinidis, T. Tamm, H. Dod, How does business analytic contribute to business value? Inf, Syst. J. 27 (3) (2017) 237–269

[118] R. Sharda, S.H. Barr, J.C. McDonnell, Decision support system effectiveness: a review and an empirical test, Manag. Sci. 34 (2) (1988) 139–159.

[119] R. Sharma, P. Reynolds, R. Scheepers, P.B. Seddon, G. Shanks, G. Business analytics and competitive advantage: A review and a research agenda, in: A. Respicio, F. Adam, G. Phillips-Wren, C. Teixeira, J. Telhada (Eds.), Proceedings of the IFIP WG8.3 DSS, Bridging the Socio-Technical Gap in Decision Support Systems Vol 212 of Frontiers in Artificial Intelligence and Applications. 2010

[120] M.S. Silver, Descriptive analysis for computer-based decision support: special focus article, Oper, Res, 36 (3) (1988) 904–916.

[121] M.S. Silver, Decision support systems: directed and nondirected change, Inf. Syst. Res. 1 (1) (1990) 47–70.

[122] M.S. Silver, Decisional guidance for computer-based decision support, MIS Q. (1991) 105–122.

[123] H. Simon, Rational decision making in business organizations. Am. Econ, Rev, 69 (4) (1979) 493–513.

[124] H. Simon, The New Science of Management Decision. 3rd Revised Edition (1960), Prentice-Hall, Englewood Cliffs, NJ. 1977

[125] Y. Song, D. Arnott, S. Gao, A model of business intelligence systems use in Chinese organizations, in: Proceedings of the Australasian Conference on Information Systems: Data, Knowledge and Decisions, 2017, pp. 1–11.

[126] R.H. Sprague, H.J. Watson, Bit by bit: toward decision support systems, Calif. Manag. Rev. 22 (1) (1979) 60–68.

[127] R.H. Sprague, A framework for the development of decision support system, MIS Q. 4 (4) (1980) 1–26

[128] T. Tamm, P. Seddon, G. Shanks, Pathways to value from business analytics, in: Proceedings of the 34th International Conference on Information Systems. Milan, Italy, 2013.

[129] H. Thomas, D. Samson, Subjective aspects of the art of decision analysis: exploring the role of decision analysis in decision structuring, decision support and policy dialogue, J. Oper. Res. Soc. 37 (3) (1986) 249–265.

[130] P. Todd, I. Benbasat, Process tracing methods in decision support systems research: exploring the black box. MIS O. (1987) 493–512

[131] E. Turban, P.R. Watkins, Integrating expert systems and decision support systems, MIS Q. (1986) 121–136

[132] E. Turban, Decision Support and Expert Systems: Management Support Systems, Prentice-Hall, Upper Saddle River, NJ. 1993. ISBN:978-0-02-421691-5.

[133] K.M. Van Hee, R.J. Wijbrands, Decision support system for container terminal

[134] D.R. Vogel. J.C. Wetherbe, MIS research: a profile of leading journals and

[135] Y. Wang, T.A. Byrd, Business analytics-enabled decision-making effectiveness through knowledge absorptive capacity in health care, J. Knowl. Manag. 21 (3) (2017) 517–539.

[136] H. Watson, M.M. Hill, Decision support systems or what didn't happen with MIS. Interfaces 13 (5) (1983) 81–88

[13z]. H Watson Revisiting Ralph Sprague's framework for developing decision support systems, Commun. Assoc. Inf. Syst. 42 (2018) 1.

[138] H. Watson, Update tutorial: big data analytics: concepts, technology, and applications, Commun. Assoc. Inf. Syst. 44 (2019). Article 1.

[139] B. Wixom, H. Watson, The BI-based organization, Int. J. Business Intellig. Res. 1 (1) (2010) 13–28.

[140] I. Yermish, V. Miori, J. Yi, R. Malhotra, R. Klimberg, Business plus intelligence plus technology equals business intelligence, Int. J. Business Intelligence Res. 1 (1) (2010) 48–63.

[141] R.W. Zmud, J.F. Cox, The implementation process: a change approach, MIS Q (1979) 35–43.

[142] H.M. Zolbanin, D. Delen, D. Crosby, D. Wright, A predictive analytics-based decision support system for drug courts. Inf. Syst. Front. (2019) 1–20.

Gloria Phillips-Wren is a Professor in the Department of Information Systems, Law and Operations Management in the Sellinger School of Business and Management at Loyola University Maryland, USA. She is founder and co-editor-in-chief of Intelligent Decision Technologies (IDT) and Associate Editor of the Journal of Decision Systems (JDS). Dr. Phillips-Wren is a past-chair of the Special Interest Group on Decision Support and Ana lytics (SIGDSA) under the Association of Information Systems (AIS), Secretary of IFIP WG8.3 Decision Support (DS), and leader of a focus group for Knowledge Engineering Systems (KES) International in intelligent decision technologies. Her research interests and publications are in decision making and support, analytics, business intelligence, health care IT, and strategic uses of technologies such as social media. Her work appears in Omega, Journal of Network and Computer Applications, European Journal of Operational Research, Communications of the Association of Information Systems, Journal of Organizational Computing and Electronic Commerce, Expert Systems with Applications, Big Data, IT & People, among others. She has also published 13 books (including co-edited), along with numerous book chapters and conference proceedings.

Mary Daly is a lecturer and researcher in Business Information Systems in the Cork Uni versity Business School, University College Cork, Ireland. Her teaching covers undergraduate, postgraduate and executive education modules. She is academic director for the MSc Business Information and Analytics program. Her research interests are pri marily associated with organizational decision making and the use and role of IS that support managerial decision making. Prior to joining UCC in 2004, her career spanned international companies, multinational corporations, and indigenous manufacturing and distribution companies where she provided IT management, project management and process improvement expertise for enterprise systems.

Frada Burstein is a Professor at the Faculty of Information Technology, Monash Uni versity, Melbourne, Australia. At Monash University, Prof. Burstein initiated and led the Knowledge Management Research Program, which comprised a virtual, industry spon sored Knowledge Management Laboratory. She was awarded over \$10m in Australian dollars funding for research projects and scholarships from the Australian Research Council and industry, including two projects in emergency management decision support, and most recently on supporting medical reasoning. Her current research interests include business intelligence, mobile and real-time decision support, and health informatics. Her work appears in journals such as Decision Support Systems, Journal of Organizational Computing and Electronic Commerce, Journal of the American Society for Information Science and Technology, Journal of Information Technology, European Journal of Operations Research, and Knowledge Management Research and Practice. Prof. Burstein is a Senior Editor for Decision Support Systems and a former Co-Editor for Journal of Decision Systems and VINE: The journal of information and knowledge management systems. Prof. Burstein has been a guest editor of a few special issues of journals and collections of research papers. The most substantial work was a set of two volumes of Handbook of Decision Support Systems, pub lished by Springer. She is a Fellow of the Australian Computer Society and Distinguished Member of the Association for Information Systems. Full research profile available at: http s://research.monash.edu/en/persons/frada-burstein
