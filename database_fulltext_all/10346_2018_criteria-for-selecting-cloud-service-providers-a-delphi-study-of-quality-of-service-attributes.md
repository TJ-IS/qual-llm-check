---
otero_id: 10346
otero_key: "TAQ6E3NF"
title: "Criteria for Selecting Cloud Service Providers: A Delphi Study of Quality-of-Service Attributes"
authors: "Michael Lang; Manuel Wiesche; Helmut Krcmar"
year: "2018"
journal: "Information & Management"
doi: "10.1016/j.im.2018.03.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Technical and Managerial Quality of Services in Cloud Computing: A Delphi Study

Authors: Michael Lang, Manuel Wiesche, Helmut Krcmar

![](/api/attachments/TAQ6E3NF/fulltext/images/a2535694be17f963e70ed2620909ea5628da1d2882e58101ef339362e9747e14.jpg)

PII: S0378-7206(17)30314-2

DOI: https://doi.org/10.1016/j.im.2018.03.004

Reference: INFMAN 3048

To appear in: INFMAN

Received date: 9-4-2017

Revised date: 23-1-2018

Accepted date: 5-3-2018

Please cite this article as: Michael Lang, Manuel Wiesche, Helmut Krcmar, Technical and Managerial Quality of Services in Cloud Computing: A Delphi Study, Information and Management https://doi.org/10.1016/j.im.2018.03.004

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Technical and Managerial Quality of Services in Cloud Computing: A Delphi Study

Michael Lang<sup>1</sup>, Manuel Wiesche<sup>1</sup>, Helmut Krcmar<sup>1</sup>

<sup>1</sup>Chair for Information Systems, Technical University of Munich

Abstract— Identifying relevant Quality of Services (QoS) during Cloud service provider (CSP) selection is critical for cloud customers’ success. Using a Delphi study, sixteen professionals from different cloud service models, company sizes, and industry types identified and ranked QoS attributes based on their relative importance. Our results show consensus on QoS attributes and identify functionality, legal compliance, contract, geolocation of servers, and flexibility as the top five QoS attributes. According to our findings, a combination of technical and managerial QoS attributes are important during CSP selection. Our findings provide guidance to both, CSP and cloud customers to select the “right” CSP.

Key Words — Cloud computing, Cloud service provider selection, Managerial Quality of Service attributes, Technical Quality of Service attributes

## 1 Introduction

Investments in cloud computing have increased tremendously in the past few years [1]. As a consequence, many cloud service providers (CSPs) now participate in this competitive market leading to extremely competitive pricing for services [2, 3]. Not just one, but often several CSPs are able to fulfill basic customer requirements [4, 5]

From the cloud customers’ point of view, selecting the “right” CSP is essential to assure future performance and maintain compliance with laws, policies, and rules [6-9]. When using cloud services, cloud customers pool their resources outside of the firm’s environment and increase their dependency on networks [10]. As a consequence, customers face certain risks such as the risk of information leakage resulting from malicious behavior in shared environments or the risk of service breakdowns because of possible network outages [11]. At the same time, an increasing number of laws, policies, and rules forces cloud customers to consider additional requirements such as data protection [9, 12]. Choosing the wrong

CSP can lead to failure in future service delivery, compromised data confidentiality or integrity, and non-

compliance with established regulations for use of clouds for data storage [13, 14].

To select the “right” CSP, a wide range of technical and managerial Quality-of-Service (QoS) attributes

must be considered. For example, technical QoS attributes such as performance or reliability are

essential to specify characteristics of the CSP in relation to the cloud service itself and can be measured

using specific techniques such as bandwidth or latency tests [15]. Technical QoS attributes are

fundamental for cloud customers who expect providers to deliver advertised characteristics [15].

Transparency, however, is limited within the cloud computing environment, and customers may not have

complete information to assure performance and attain or maintain regulatory compliance [16, 17].

Moreover, the technology associated with cloud computing changes quickly and continually because of

short technology life-cycles [18]. To adequately assess and verify the range of technical QoS attributes,

cloud customers require managerial QoS. Managerial QoS attributes such as geolocation of servers or

monitoring services verify and assure the capabilities and advertised characteristics of a CSP [19].

Web services in general [20], and particularly cloud services, have extremely diverse QoS attributes for

similar characteristics [21, 22]; the quality of security or performance offerings of cloud services, for

example, may be highly variable [4]. Furthermore, not all technical QoS attributes are directly

measurable for cloud customers [19] and not all managerial QoS attributes are directly accessible for

cloud customers and are difficult to quantify [15]. The cloud customer often lacks adequate knowledge

their QoS requirements [17, 23].

Research about the most important QoS in CSP selection provides snapshots in 2011 and 2013. While

Saripalli and Pingali [24] provide a list of 25 ranked cloud vendor selection attributes in 2011,

Repschlaeger et al. [25] ranked 62 low-level QoS attributes in 2013. However, legal conflicts related to

data protection principles between the United States and Europe increased between 2011 and 2015.

Further, the role of information technology (IT) decision makers is evolving from providing and supporting

IT toward integrating and retaining IT quality as public cloud computing becomes mainstream [9]. Hence,

the most important QoS attributes may change over time, but our knowledge about the most important

QoS attributes that consider environmental changes within the cloud market is limited.

Our work investigates the relative importance of QoS-based selection attributes used by customers within a cloud computing environment in 2015. Using a Delphi study design, we examined the opinions of professionals to achieve consensus on the most important QoS attributes for CSP selection. Our results show consensus on QoS attributes and identify functionality, legal compliance, contract, geolocation of servers, and flexibility as the top five QoS attributes. Through a comparison of our results with previous studies, we identified four key changes that have occurred within the cloud market: (1) an increase in the importance of data protection; (2) cloud customers continue to seek value co-creation with CSP; (3) a decrease in the possibility of CSP opportunistic behavior; and (4) the continuation of product uncertainty as a major problem during CSP selection. From a practical point of view, our results not only provide insights to help cloud customers conduct optimal CSP selection decisions, but these results also help CSP to address cloud customers’ needs more effectively through cooperation with independent third parties and the provision of relevant control mechanisms.

The remainder of the paper is organized as follows. First, we present the theoretical background for our study by describing the current state of research on CSP selection processes and QoS attributes. We then explain our methodological approach and describe the three-phase Delphi study applied in our research. In Results, we first present all identified QoS attributes, then the ranking of these attributes provided by the professionals, and a classification of these attributes. Finally, we outline limitations and possible directions for future research and discuss our contribution to literature and practice.

## 2 Research Background

In this section, we first explain the cloud sourcing process in general and define the scope of this study. Then, we point out the state of research on QoS attributes and examine the shortcomings of literature.

## 2.1 Cloud Sourcing Process

Conducting decisions on cloud sourcing is a complex process involving three consecutive steps [15, 26, 27]. These steps include the cloud sourcing decision itself, pre-qualification of possible CSPs, and CSP selection (Figure 1).

In the first step, cloud customers make a decision on cloud sourcing. Inhibiting and facilitating factors for cloud sourcing affect this decision-making [28, 29]. While an increasing strategic importance of services, available risks, or perceived complexity may prevent cloud customers to cloud source services, the possibility to save costs, access specialized resources, increase flexibility, or reduce time to market facilitates cloud customers to cloud source services [12, 26]. Both facilitating and inhibiting factors influence cloud customers to cloud source their services within the initial decision-making step.

In the second step, cloud customers preselect possible CSP depending on functional requirements and boundary restrictions. Only providers that serve required service models (IaaS, PaaS, or SaaS providers) and needed functions or applications (CRM system) are considered [4, 5]. Boundary restrictions on the data, e.g., sensitive data that are liable to specific regulatory requirements such as accounting systems constitute the list of preselected CSPs [15, 30]. This list of CSPs might fulfill the

Cloud customers have to select an appropriate CSP, the third step in the decision-making process. Often several CSPs fulfill basic requirements regarding required service model, required functions, or applications [4]. In addition to functional requirements and boundary restrictions, QoS requirements must be considered [4]. As an example, CSPs warrant different levels of availability usually varying between 98% and 99.999%. Cloud services have a high diversity of different QoS attributes [21]; cloud customers have to select from a plethora of offerings and decide which QoS attributes are relevant and which provider can fulfill their QoS requirements [17].

![](/api/attachments/TAQ6E3NF/fulltext/images/56fa5a37104e46b53a08d509183e16e070f83c28935da5add5b8f9461d73d391.jpg)  
Figure 1. Cloud sourcing process (Step 3 is the focus of this study)

## 2.2 The Challenge to Identify Relevant Quality-of-Service Attributes

Cloud customers base their CSP selection on diverse QoS attributes. QoS attributes describe nonfunctional aspects of web services [4]. QoS attributes are used to evaluate the degree to which a web service meets specified technical and managerial quality requirements in a service request [15, 19]. The technical QoS comprises attributes related to operational aspects of web services, such as usability, efficiency, reliability, and performance [19]. The managerial quality QoS comprises attributes used for capturing service management information such as geolocation of servers or contract [19]. While technical QoS specifies the CSP characteristics of the cloud service itself, managerial QoS provides a source of decision confidence by verifying the capabilities and advertised characteristics of a CSP [15, 31, 32]. To select the right CSP, both technical and managerial QoS attributes must be considered by cloud customers.

Identifying relevant QoS attributes is difficult [23]. Web services in general [20], and particularly cloud services, have a high diversity of QoS levels for similar functionalities [21, 22]. Each QoS attribute comprises different meanings. As an example, the performance attributes cover CPU performance, memory performance, and provision time, which highly influence the quality of the underlying infrastructure [33]. Cloud customers also must consider different QoS attributes related to runtime or functional, transaction support, configuration management, and security when selecting CSP [20, 34- 36].

Not all attributes of CSP are accessible or can be easily measured [37]. Almost two-thirds of CSPs do not advertise concrete prices to avoid margin cutting price wars [38]. Furthermore, the security configuration and capabilities of CSPs are not easy to quantify [18, 37]. In addition to direct information publicly available from CSPs, cloud customers might also consider indirect information from cloud certificates during CSP selection [39].

In light of these challenges in identifying relevant QoS attributes, cloud customers may require support in the selection of CSP [40].

## 2.3 Approaches to Identify Relevant Quality-of-Service Attributes for Cloud Service Provider Selection

To support cloud customers during CSP selection decisions, Saripalli and Pingali [24] used a short-list of cloud vendor selection attributes and ranked 25 QoS attributes in 2011. In 2013, Repschlaeger et al. [25] identified 62 low-level QoS attributes in literature, combined these into 21 QoS attributes and 6 QoS categories, and then ranked the low-level attributes. While Saripalli and Pingali [24] focus mainly on technical QoS attributes, Repschlaeger et al. [25] identify a growing number of managerial QoS attributes related to data protection issues. The importance of managerial QoS attributes has increased because cloud technology and the legal environment change rapidly owing to short life-cycles and inherent cloud computing characteristics [18, 41] (Table 1).

Table 1. Managerial and technical QoS attributes as identified by Saripalli and Pingali [24] and Repschlaeger et al. [25]

<table><tr><td>Study</td><td>Managerial QoS attributes</td><td>Technical QoS attributes</td><td>Publication date</td></tr><tr><td>Saripalli and Pingali [24]</td><td>4 QoS attributes</td><td>21 QoS attributes</td><td>2011</td></tr><tr><td>Repschlaeger et al. [25]</td><td>8 QoS attributes</td><td>13 QoS attributes</td><td>2013</td></tr></table>

However, prior findings are limited because of changes in the legal environment and the changing role of IT decision makers, and they ignore interdependencies between technical and managerial QoS attributes: Cloud customers are challenged to stay compliant with laws, policies, and rules that specify selection requirements. A diversity of different levels for data protection regulation, laws, and rules exist because of a fragmented legal environment relating to data protection [12, 42]. Legal conflicts between the United States and Europe in data protection principles increased between 2011 and 2015 [41]. One result of this conflict resulted in invalidation of the Safe Harbor Agreement between the United States and Europe in 2015. Cloud customers want a QoS that enhances compliance with regulations that govern data protection.

Cloud customers face also new challenges to integrate a variety of different cloud services into existing IT infrastructures [9]. Cloud services as a special form of IT outsourcing can become obsolete overnight due to changes in business strategy [43]. To quickly adopt and integrate new services, companies seek for partnerships to digitalize their processes and products [44].

Further, when ranking QoS attributes, cloud customers must consider the advantages and disadvantages of possible related technical and managerial QoS attributes on several dimensions. For example, a more detailed contract may have a negative influence flexibility regarding the possibility to carry out speedy changes [45]. Saripalli and Pingali [24] and Repschlaeger et al. [25] used point-wise approaches (simple additive weighting and analytical hierarchy process, respectively), which do not consider dependencies between QoS attributes [46].

To overcome these limitations, this study investigates how cloud customers respond to environmental changes in 2015 and considers independencies between and within technical and managerial QoS attributes.

## 3 Research Approach

To address our research aim, we needed input from professionals with extensive experience in the cloud computing field and chose the Delphi approach as our research method as it allows aggregation of responses through an iterative process of controlled feedback [47, 48]. The Delphi method is recommended when “the problem does not lend itself to precise analytical techniques but can benefit from subjective judgments on a collective basis” [49]. The Delphi method allowed us to gain insights into the most important QoS attributes and their relative importance as identified by the collective experience of our professional panel [50] and to consider possible dependencies between QoS attributes [24, 46, 51]. The Delphi process stops when a reasonable level of consensus or another predefined stop criterion is achieved [50].

## 3.1 Panel Selection

We recruited professionals with significant work experience in the field of cloud computing to obtain valid and robust results [48]. We located our panel of professionals, responsible for decision-making on CSP selection at their place of employment, at cloud computing workshops and through a special interest group for cloud computing on a social network website. Professionals practicing in this field and known to the researchers were also included. All potential professionals were asked predefined questions regarding their cloud experience and use of cloud deployment and cloud delivery models. To ensure a reliable panel, we excluded novice persons (those with less than one year of cloud experience), private and hybrid cloud users, and cloud service users who use cloud services less frequently than once a day. We screened our professionals to make sure that as many types of industries as possible were included in the study resulting in representation of organizations of different sizes using various types of cloud service models in the sample. An overview of the panel selection criteria is presented in Table 2.

Table 2. Professional panel selection criteria

<table><tr><td>#</td><td>Selection criteria</td><td>Description</td></tr><tr><td>1</td><td>Cloud service decision maker</td><td>Professionals who are cloud service decision makers.</td></tr><tr><td>2</td><td>Non-novice person</td><td>Professionals with more than one year of cloud experience.</td></tr><tr><td>3</td><td>Public cloud user</td><td>The employing organization uses public cloud services.</td></tr><tr><td>4</td><td>Frequent cloud service user</td><td>Only professionals who use cloud service at least once a day will be considered.</td></tr><tr><td>5</td><td>Diversity of used cloud service models</td><td>At least three types of cloud service models (IaaS, PaaS, and SaaS) should be represented in the sample.</td></tr><tr><td>6</td><td>Diversity of organizational sizes</td><td>Organizations of all sizes (large-, medium-, and small-size organizations) should be represented.</td></tr><tr><td>7</td><td>Diversity of industries</td><td>Panelists should be employed by diverse industries.</td></tr><tr><td>8</td><td>Diversity of organizations</td><td>Panelists should be employed by diverse organizations.</td></tr></table>

We invited 32 professionals fitting our selection criteria, of whom 19 participated in the first round of the study resulting in an effective response rate of 59%; no obvious response bias regarding our selection criteria was observed. Our panel had experience with three cloud service models (Infrastructure-, Platform-, and Software-as-a-Service), represented as small-, medium-, and large-sized organizations, and which came from different industries (financial services, manufacturing, software development, railway, media, energy, data analytics, public administration, and wholesale). While some of the panelists were responsible for CSP selection within their company, others served as consultants and were frequently challenged with CSP selection for their customers. Each panelist worked for a different company. The profile of the panel indicates considerable CSP selection experience for diverse service models, industries, and company sizes, thus establishing the credibility of the panel (Table 3).

Table 3. Overview of characteristics of panel professionals

<table><tr><td>#</td><td>Position</td><td>Company category</td><td>Geography of operation</td><td>Cloud service model</td><td>Industry</td></tr><tr><td>1</td><td>IT-Manager</td><td>LO (&gt;250)</td><td>Worldwide</td><td>SaaS</td><td>Energy</td></tr><tr><td>2</td><td>Business Intelligence</td><td>LO (&gt;250)</td><td>Germany</td><td>IaaS</td><td>Media</td></tr><tr><td>3</td><td>CEO</td><td>MO (50-249)</td><td>Germany</td><td>SaaS</td><td>Manufacturing</td></tr><tr><td>4</td><td>CEO</td><td>SO (10-49)</td><td>UK</td><td>IaaS and PaaS</td><td>Financial services</td></tr><tr><td>5*</td><td>COO</td><td>SO (10-49)</td><td>Germany, Switzerland, and Austria</td><td>SaaS</td><td>Communication</td></tr><tr><td>6</td><td>Consultant (Manager)</td><td>LO (&gt;250)</td><td>Worldwide</td><td>SaaS, PaaS, and IaaS</td><td>IT-Consultant</td></tr><tr><td>7</td><td>Consultant (Partner)</td><td>LO (&gt;250)</td><td>Worldwide</td><td>SaaS, PaaS, and IaaS</td><td>IT-Consultant</td></tr><tr><td>8</td><td>Consultant (Senior)</td><td>LO (&gt;250)</td><td>Worldwide</td><td>SaaS, PaaS, and IaaS</td><td>IT-Consultant</td></tr><tr><td>9</td><td>Consultant (Partner)</td><td>LO (&gt;250)</td><td>Worldwide</td><td>SaaS, PaaS, and IaaS</td><td>IT-Consultant</td></tr><tr><td>10*</td><td>IT-Manager</td><td>LO (&gt;250)</td><td>Worldwide</td><td>SaaS</td><td>Software development</td></tr><tr><td>11</td><td>Project Manager</td><td>LO (&gt;250)</td><td>Germany</td><td>IaaS</td><td>Public administration</td></tr><tr><td>12</td><td>IT-Manager</td><td>LO (&gt;250)</td><td>Germany</td><td>IaaS</td><td>Data analytics</td></tr><tr><td>13</td><td>IT-Manager</td><td>MO (50-249)</td><td>Germany</td><td>SaaS</td><td>Financial services</td></tr><tr><td>14</td><td>IT-Manager</td><td>LO (&gt;250)</td><td>Worldwide</td><td>PaaS and IaaS</td><td>IT service</td></tr><tr><td>15</td><td>Project Manager</td><td>LO (&gt;250)</td><td>Germany</td><td>IaaS and SaaS</td><td>Railway</td></tr><tr><td>16</td><td>IT-Manager</td><td>LO (&gt;250)</td><td>Worldwide</td><td>IaaS and PaaS</td><td>Manufacturing</td></tr><tr><td>17</td><td>COO</td><td>SO (10-49)</td><td>Germany and Asia</td><td>IaaS and PaaS</td><td>Software development</td></tr><tr><td>18</td><td>CEO</td><td>SO (10-49)</td><td>Germany</td><td>SaaS</td><td>Wholesale</td></tr><tr><td>19*</td><td>CEO</td><td>SO (10-49)</td><td>Germany</td><td>SaaS</td><td>Software development</td></tr></table>

left study after iteration 1 of round 3.  
LO = Large-sized organization; MO = Medium-sized organization; SO = Small-sized organization

## 3.2 Data Collection and Analysis Method

We followed a modified version of the Delphi method, as proposed by Schmidt [50], to investigate the relative importance of QoS attributes. Data were collected through brainstorming and semi-structured interviews allowing us to develop a deep understanding of the identified QoS attributes and reasoning behind the participants’ individual rankings. Similar to Schmidt et al. [52], our study design had four stages: the preparation stage and the three subsequent Delphi rounds (Figure 2). We started our first Delphi round in May 2015 and completed the study in October 2015. Activities during the preparation stage included planning of the study and establishment of the professional panel using our selection criteria as described above.

An overview of our research process is shown in Figure 2.

![](/api/attachments/TAQ6E3NF/fulltext/images/0c1e6d12cc6ee538ffdacbdb26c7542a6b3c3fad71ae30052e2a79719ee3cd42.jpg)  
Figure 2. Research process based on Schmidt et al. [52]

In round 1, brainstorming and semi-structured interviews with each professional were arranged and conducted to identify as many QoS attributes as possible (see Appendix A). While brainstorming enabled us to obtain a large quantity of possible relevant QoS attributes, the semi-structured interviews provided additional information and some QoS attributes not mentioned during brainstorming.

After interviewing the professionals, the gathered information was transcribed, analyzed, and synthesized. To aggregate the findings across all interviews, we adapted the method of Strauss and

Corbin [53] and used open and axial coding to identify all relevant QoS attributes. To ensure consistent coding, two researchers independently read and coded all interview transcripts line-by-line using phrases from the transcripts describing QoS attributes (open coding) and discussed any conflicting results. This open coding process resulted in a list of 69 codes and 360 phrases. The resulting discussions and the rich body of information within the transcripts provided us with necessary background information for the subsequent axial coding (see Appendix B). After completing the axia coding, we reached a final list of 31 unranked QoS attributes.

As members of our panel had different job positions and came from different industries, it was fundamental to assure each professional had the same understanding of each single QoS attribute. To assure common understanding, the panelists were asked to make corrections and validate the attribute descriptions resulting in several changes and clarifications being made to the descriptions. After this clarification process, our panel agreed on the QoS descriptions (see Appendix C).

During round 2, we pared the consolidated list of QoS attributes into a more manageable set for the ranking phase [48]. Following the suggestion by Schmidt [50], we presented the professionals with a randomized list of the 31 unranked QoS attributes from round 1 and asked each professional to select (not rank) the most important attributes (at least 10 and at most 20 QoS attributes) for CSP selection. We provided a brief definition for each QoS attribute to assure that all professionals had the same understanding of each. All 19 professionals provided responses in round 2. After the responses were consolidated, a cut-off value was defined to yield a list of 12 to 15 items for the subsequent ranking phase [54]. Using this process, we chose a cut-off value of 60% and identified a pared list that included 13 of the most important QoS attributes.

The pared list was transferred to round 3 of the study for ranking. We sent the manageable list of 13 QoS attributes for CSP selection from the selection round 2 in randomized order to each of our professionals and asked them to rank the QoS attributes in order of priority. We also asked the professionals to explain their reasoning for the chosen ranking. This information was shared with the professionals in subsequent iterations. To measure the degree of consensus among our professionals, we followed the approach of Schmidt [50] and used Kendall’s coefficient of concordance (W). Kendall’s W is frequently used in Delphi studies and is applied to indicate whether a consensus among the panelists has been reached and the relative strength of the consensus [50]. When Kendall’s W is greater than 0.7, strong consensus has been reached; values between 0.5 and 0.7 indicate moderate consensus, and values less than 0.5 indicate little consensus among panelists [50]. Nineteen professionals participated in the first iteration of ranking in round 3, which yielded a Kendall’s W value of 0.22 indicating relatively weak consensus.

Following Schmidt [50], we decided to continue the ranking process until the coefficient of concordance indicated a moderate consensus. Therefore, we conducted two further iterations within round 3. This time we provided the following additional information to each professional as controlled feedback: (I) the average rank of each criterion, (II) the ranking given by that professional for each criterion at the prior iteration of ranking, and (III) the percentage of professionals who ranked that criterion within the top 50%. As a fourth controlled feedback (IV), we provided a summary of all comments made by the professionals for each criterion collected within the prior iteration. Similar to Singh et al. [54], we believed that this additional information would help the professionals to consider their own ranking in light of the group’s ranking, thus providing them the opportunity to adjust their ranking where it made sense to do so. Sixteen professionals participated in the second iteration, yielding a Kendall’s W of 0.32. The Kendall’s W was 0.69 in our third iteration in which 16 professionals participated, suggesting that a moderate level of consensus had been reached. According to the rankings made by the professionals during iteration three of round 3, Kendall’s W almost doubled. However, such improvements in Kendall’s W after round 2 are quite common [51, 54]. We believe this result may be because the professionals were able to reflect on their own ranking in light of the panel’s ranking by considering the controlled feedback of two iterations. This additional information most likely helped the professionals to reach a group consensus.

## 4 Results and Discussion

In the following, we present results from the first round of our Delphi study and report on the QoS attributes that were derived from the exploratory interviews. We illustrate examples of interview quotes used to produce the list of QoS attributes. We then present the results from the second and third rounds of our Delphi study, where the attributes were pared and ranked. Finally, we provide a CSP selection framework according to a classification of our results.

## 4.1 Identification of QoS Attributes

The first round (exploratory interview phase) of our Delphi study included interviews (see Appendix D) and brainstorming. The resulting 31 unranked QoS attributes for CSP selection are listed in Table 4 and briefly described in Appendix E.

Table 4. List of 31 unranked QoS attributes for cloud service provider selection

<table><tr><td>No.</td><td>QoS attribute</td><td>No.</td><td>QoS attribute</td><td>No.</td><td>QoS attribute</td></tr><tr><td>1</td><td>Assurance statement *</td><td>12</td><td>Flexibility</td><td>22</td><td>Ownership *</td></tr><tr><td>2</td><td>Benchmark *</td><td>13</td><td>Functionality</td><td>23</td><td>Personal contact *</td></tr><tr><td>3</td><td>Business process transparency *</td><td>14</td><td>Geolocation of servers</td><td>24</td><td>Process maturity *</td></tr><tr><td>4</td><td>Certification</td><td>15</td><td>In-house recommendation *</td><td>25</td><td>Reputation *</td></tr><tr><td>5</td><td>Cloud exit strategy *</td><td>16</td><td>Integration</td><td>26</td><td>Standard operating environment *</td></tr><tr><td>6</td><td>Contract</td><td>17</td><td>Interoperability</td><td>27</td><td>Support</td></tr><tr><td>7</td><td>Control</td><td>18</td><td>Legal compliance</td><td>28</td><td>Test of solution *</td></tr><tr><td>8</td><td>Deployment model</td><td>19</td><td>Market share *</td><td>29</td><td>Third-party recommendation *</td></tr><tr><td>9</td><td>External business communication</td><td>20</td><td>Monitoring</td><td>30</td><td>Track record</td></tr><tr><td>10</td><td>Failure preventive measures</td><td>21</td><td>Open communication</td><td>31</td><td>Transparency of activities</td></tr><tr><td>11</td><td>Financial performance *</td><td></td><td></td><td></td><td></td></tr></table>

\* new QoS attributes not represented in earlier lists

As our first objective was to develop a list of QoS attributes with a wide coverage of possible QoS attributes, we expected some differences between our list and the combination of previous lists. Given the radical legal, technological developments and changing role of decision makers within the cloud computing market within the past few years, we expected to find that (1) some risk items have remained relatively stable, while (2) others have declined in importance over time. Because previous studies tended to generate QoS attributes according to literature, we expected that (3) the list resulting from our disciplined Delphi approach would contain some unique items not detected in earlier studies.

To address the three points outlined above, we adapted the approach of Schmidt et al. [52] and compared our list to a merger of other QoS attributes lists from Repschlaeger et al. [25] and Saripalli and Pingali [24]. A combination of these two lists and our list was therefore used for this comparison. The results of this analysis are presented in Table 4 and illustrated in Figure 3.

![](/api/attachments/TAQ6E3NF/fulltext/images/ab5d34a9e5d85303505cd3f0977b4a0964c45f07dd7c8b7683d05376c242843d.jpg)  
Figure 3. Comparison of QoS attribute lists

The first subset of QoS attributes we consider are those we expected would remain stable over time. Although there were 17 QoS attributes identified by our panel, which could be matched in some way with 31 QoS attributes in the combined list, there is not a strict one-to-one correspondence. As an example, according to our definition (see Appendix E), functionality covers QoS attributes of the combined list, such as security or availability. In that case, functionality serves as a surrogate for some low-level QoS attributes mentioned in the combined list. Nine of these 17 QoS attributes have been identified within each list and could be matched in some way across the lists. Several attributes such as compliance or monitoring possibilities could be directly matched across all lists.

Regarding the second point, our analysis revealed two QoS attributes identified in earlier studies but not represented in our list (and are thus not presented in Table 5). Interestingly, autonomy and graphics agility, not considered QoS attributes in our list, are related to technological issues. It appears that the importance of these attributes has diminished over the past few years, perhaps due to a more mature cloud market.

The third point involves the 14 new QoS attributes identified by the panel but not mentioned in previous studies. Thus, our list of attributes greatly increases the coverage of known QoS factors and suggests that some new elements of QoS attributes have emerged during the past few years, for instance, managerial QoS attributes. Three major groups of QoS factors surface from these 14 new QoS attributes.

Three of the new QoS attributes relate to partnering with cloud customers to co-create value. While cloud resources are exchangeable commodities, cloud customers want a good relationship to co-create value with the CSP. This might have changed in recent years because companies are increasingly challenged to digitalize their processes and products and seek certain platform strategies. Hence, cloud customers need reliable CSP with good financial performance and market share to assure that longterm relationships have a personal contact.

A second major topic deals with lock-in effects. This is an interesting finding as it points out the cloud customers’ awareness and proactive behavior to assure flexibility, also in the long-term. To date, cloud services can become obsolete overnight because of changes in business strategy. Therefore, the demand for cloud service exit strategies and standardized operating environment is high.

The third major topic of new QoS addresses how cloud customers bring themselves up to speed on CSPs’ data protection capabilities. Laws in place force cloud customers to take responsibility for the cloud services they use and data transferred. To address this issue, cloud customers assure legal compliance by reading assurance statements of the CSP. Further, cloud customers rely on a good reputation of CSP or the recommendation of a third party. Such QoS provides cloud customers indirectly information about the capabilities of a possible CSP to protect data.

## 4.2 Ranking of Quality-of-Service Attributes

In round 2, the professionals pare the list of 31 QoS attributes retaining only, in their opinion, attributes of greatest importance. Table 5 presents the 13 most important QoS attributes as identified by the professionals, their average rank, the Kendall’s W value for each ranking iteration in round 3, and the final ranking of the QoS attributes.

Table 5. Ranking from iterations one to three and final ranking of the most important QoS attributes for selecting a cloud service provider

<table><tr><td>QoS attribute</td><td>Iteration 1 average rank</td><td>Iteration 2 average rank</td><td>Iteration 3 average rank</td><td>Final rank</td></tr><tr><td>Functionality</td><td>2.95</td><td>2.6</td><td>1.56</td><td>1</td></tr><tr><td>Legal compliance</td><td>4.79</td><td>4.53</td><td>2.56</td><td>2</td></tr><tr><td>Contract</td><td>6.42</td><td>5.20</td><td>3.94</td><td>3</td></tr><tr><td>Geolocation of servers</td><td>5.42</td><td>5.27</td><td>4.25</td><td>4</td></tr><tr><td>Flexibility</td><td>6.11</td><td>6.40</td><td>5.75</td><td>5</td></tr><tr><td>Integration</td><td>7.26</td><td>7.40</td><td>6.88</td><td>6</td></tr><tr><td>Transparency of activities</td><td>7.21</td><td>7.07</td><td>7.44</td><td>7</td></tr><tr><td>Certification</td><td>8.21</td><td>7.20</td><td>8.19</td><td>8</td></tr><tr><td>Monitoring</td><td>8.42</td><td>8.27</td><td>8.75</td><td>9</td></tr><tr><td>Support</td><td>7.89</td><td>8.20</td><td>9.00</td><td>10</td></tr><tr><td>Control</td><td>8.21</td><td>8.67</td><td>9.25</td><td>11</td></tr><tr><td>Deployment model</td><td>8.79</td><td>9.67</td><td>11.56</td><td>12</td></tr><tr><td>Test of solution</td><td>9.32</td><td>10.53</td><td>11.88</td><td>13</td></tr><tr><td>Kendall&#x27;s W*</td><td>0.22</td><td>0.32</td><td>0.69</td><td></td></tr><tr><td colspan="5">*Kendall&#x27;s W &gt; 0.7 = strong consensus among panelistsKendall&#x27;s W from 0.5 to 0.7 = moderate consensus among panelistsKendall&#x27;s W &lt; 0.5 = little consensus among panelists</td></tr></table>

As mentioned, iteration 3 yielded a Kendall’s W value of 0.69 indicating that our predefined stop criterion of a moderate consensus was achieved. Because our panel of professionals was highly diverse in regard to the type of cloud service model used, size of company, and type of industry represented, we conclude that a reasonable degree of confidence in the ranking is reached [50].

To better understand what the most important QoS attributes are, we compared rankings between each iteration. Interestingly, the ranking of the top 5 QoS attributes (functionality, legal compliance, contract, geolocation of servers, and flexibility) remained stable during each iteration. This suggestion of a high and stable consensus regarding these attributes could be interpreted as a universal indicator of the most important QoS attributes during CSP selection decisions.

In contrast, the priority of QoS attributes with a ranking of 6 to 13 slightly changed during each iteration.

Hence, our controlled feedback after two iterations might have helped the professional to reflect on their own ranking in light of the overall panel’s ranking. Although we reached an overall moderate consensus by the panelists, our results indicate that factors ranked between 6 and 13 might vary individually in terms of their importance during CSP selection decisions.

Finally, the panel considered dependencies between QoS attributes during the controlled feedback. For example, one professional who used domestic cloud solutions mentioned, “[l]egal compliance is located worldwide and remarked regarding the importance of contracts, “[i]n countries where the industry is less regulated, the contracts have to be more detailed.” It seems our panel ranked the most important QoS attributes by also considering dependencies between the attributes.

## 4.3 Classification of Quality-of-Service Attributes

To select the right CSP, both technical and managerial QoS attributes must be considered by cloud customers. To provide guidance, we classify our results in the most important technical and managerial QoS attributes according to our interviews and the ontology of Zhou et al. [15].

Table 6. CSP selection framework based on technical and managerial QoS attributes

<table><tr><td colspan="2">Technical Quality-of-Service Attributes</td><td colspan="2">Managerial Quality-of-Service Attributes</td></tr><tr><td>Attribute</td><td>Classification Motivation</td><td>Attribute</td><td>Classification Motivation</td></tr><tr><td>Functionality</td><td>Defines cloud service-related QoS functionalities such as availability or performance attributes.</td><td>Legal compliance</td><td>Defines the legal environment where data are processed or stored within the cloud service.</td></tr><tr><td>Flexibility</td><td>Defines the latency of the CSP as cloud service-related changes are requested.</td><td>Contract</td><td>Contracts provide an incentive structure surrounding the cloud relationship including rights and obligations for both parties.</td></tr><tr><td>Integration</td><td>Defines the interfaces, protocols, and characteristics of the cloud service.</td><td>Geolocation of servers</td><td>Defines the geolocation where data are processed within the cloud service.</td></tr><tr><td>Control</td><td>Mechanisms comprising tools and approaches enabling individuals to configure and control outcomes of the cloud service.</td><td>Transparency of activities</td><td>Assures that all CSP-related activities will perform as specified by a predetermined set of widely accepted agreements and rules.</td></tr><tr><td></td><td></td><td>Certification</td><td>Defines an endorsement from a third party attesting that a (potential) partner adheres to the organization&#x27;s policies and standards.</td></tr><tr><td></td><td></td><td>Monitoring</td><td>Assures that all cloud service-related transactions will perform as specified by a predetermined set of widely accepted agreements and rules.</td></tr><tr><td></td><td></td><td>Support</td><td>The degree to which the vendor provides support to the client while, e.g.,</td></tr></table>

<table><tr><td></td><td>evaluating, testing, and selecting services.</td></tr><tr><td>Deployment model</td><td>Former mechanism to assure data security and privacy.</td></tr><tr><td>Test of solution</td><td>Provides proof of concept for service quality and interoperability to avoid future service failures and assure interoperability of the cloud service.</td></tr></table>

The technical QoS consists of attributes (functionality, flexibility, integration, and control) related to operational aspects of the cloud service. The managerial QoS consists of attributes (contract, legal compliance, geolocation of services, transparency of activities, certification, monitoring, test of solution, and support) used for capturing cloud service management information. Overall, both technical and

## 5 Contribution to Literature and Practice

The empirical results of this study support cloud customers during CSP selections by identifying the most important technical and managerial QoS attributes for CSP selection as best practices. Usually several CSPs can fulfill cloud customers’ basic requirements [4, 5]. By considering technical and managerial QoS attributes, cloud customers can determine the “right” CSP to assure future cloud service performance and compliance with laws, policies, and rules [6-8]. Because cloud customers often lack knowledge to determine relevant QoS attributes [17, 23], we provide a list of the most important QoS attributes for CSP selection in 2015. The QoS attributes in the descending order of relevance are functionality, legal compliance, contract, geolocation of services, flexibility, integration, transparency of activities, certification, support, control, deployment model, and test of solution.

## 5.1 Limitations and Future Research Directions

As with any study, the results of the current study must be interpreted in the context of the limitations and constraints regarding generalizability, professional selection, and abstraction level of QoS attributes for CSP selection.

First, the study results are based on the participation of 16 professionals and may not be generalizable to a larger population or prescriptive in nature. However, the rich data resulting from our interviews in combination with the Delphi ranking provide an initial starting point for future research. Being able to analyze results from a larger group of cloud computing decision makers from an extended pool of firms or countries, or for other cloud delivery models (such as private cloud), would be advantageous for future

research.

Second, our professionals were not chosen randomly, and we did not attempt to control for the criticality (in terms of data sensibility) of cloud services they used. However, because Delphi studies also require a high effort from participants, using a convenience sample is quite common [51]. Future studies using a larger, randomized sample controlling for criticality of used cloud services and employing research techniques such as survey designs could enhance generalizability of results.

Third, we considered QoS attributes for CSP selection decision on a high abstraction level. To provide further insights, future research might use our results as a research agenda for investigating technical and managerial QoS attributes on a lower abstraction level. Researchers could combine previous results on QoS attributes with our decision framework and focus on the impact of the most important managerial QoS attributes including legal compliance, privacy issues, contract-related aspects, different pay-peruse models, or the impact of geolocation of servers on CSP selection.

Finally, the legal environment is continuously changing. While the Safe Harbor agreement was struck down in 2015, the EU-US Privacy Shield was accepted by the EU in 2016. Our research illustrates a snapshot of 2015 when, for the first time, such a well-known agreement was struck down. Therefore, our study provides important insights about how the relative importance of QoS attributes evolves over time and which cloud market changes take place. Future research might use these insights to further investigate CSP adoption and selection decisions by considering, e.g., cloud security platforms [55].

## 5.2 Contribution to Literature

On the basis of our identification of the most important QoS attributes (Section 4.2), we identify and compare how the most important QoS attributes differ between 2011 and 2015. Figure 4 provides an overview of the newly identified QoS and the relative importance of QoS in 2015 (this study), 2013 [25], and 2011 [24].

![](/api/attachments/TAQ6E3NF/fulltext/images/f3bcf01e4aa539acba7f2c6f20145c6c46e6d7b28c08f56dd2bb74e933ebd4bf.jpg)  
Figure 4. Relative importance of QoS as identified by this study in comparison to Repschlaeger et al. [25] and Saripalli and Pingali [24]<sup>1</sup>

We identify an increasing importance of managerial QoS related to data protection aspects. Such QoS attributes are “legal compliance”, “geolocation of servers”, “transparency of activities”, and “deployment model.” According to our professionals, such QoS attributes are important to gain confidence on adequate data protection. While the geolocation of a server affects data protection through local laws in place, the transparency of activities helps cloud customers decide whether data protection mechanisms are compliant with legal and internal requirements. Further, the deployment model helps cloud customers to gain confidence about the separation of companies’ data from third-party data.

During the studies of Saripalli and Pingali [24] in 2011, of Repschlaeger et al. [25] in 2013, and our study in 2015, the relative importance of “legal compliance” increased. In comparison to Saripalli and Pingali [24], Repschlaeger et al. [25] identified “geolocation of servers”, “transparency of activities”, and “deployment model” as new managerial QoS attributes. Within our study, while the relative importance of “geolocation of servers” and “deployment model” remains important, the relative importance of “transparency of activities” increases.

We assume that the changing legal environment is responsible for the increasing importance of QoS related to data protection issues [12]. Cloud customers have the ability to assure data protection [56]. Hence, cloud customers increasingly want QoS to protect their data and be able to maintain compliance with guidelines for data protection.

We identify an increasing importance of QoS related to value co-creation between cloud customers and CSP. Such QoS attributes are “flexibility”, “integration”, and “support.” According to our professionals, they look for partnerships to digitalize their processes. Cloud customers value the knowledge of different CSPs regarding the integration of digital products and services. This is particularly important because cloud customers face increasing competition and a need to optimize their value creation.

The relative importance of “flexibility” and “integration” remained stable between 2011 [24], 2013 [25], and 2015 (this study). In comparison to Saripalli and Pingali [24], Repschlaeger et al. [25] identified “support” as a new managerial QoS attribute. In our study, the relative importance of the manageria QoS “support” decreased but remained within the top 10 of the most important QoS attributes.

We assume the rising market competition forces cloud customers to establish a partnership with CSP to co-create value [44]. Within volatile markets, cloud customer have to quickly adopt their business strategies [43]. Because of the unforeseen events, existing cloud services can become obsolete overnight [43]. To compete in such markets, cloud customers need flexible cloud services that are easy to integrate into their IT landscape. To enable a flexible integration of cloud services, cloud customers rely on CSPs’ support capabilities and co-create value for their customers [44].

We identified a decreasing importance of technical and managerial QoS attributes related to avoidance of a CSPs’ opportunistic behavior. These QoS attributes are “contract”, “control”, and “monitoring”. According to our professionals, a huge variety of comparable cloud services are available on-demand. Because of the standardization of cloud services, contracts become standardized and easy to compare. Cloud customers commonly use communities including other cloud customers to gain insights about the accuracy and quality of possible CSPs.

The relative importance of contracts decreased between 2013 [25] and 2015 (this study) but remained within the top 3 of the most important QoS attributes. The relative importance of control decreased between 2011 [24], 2013 [25], and 2015 (this study). The relative importance of “monitoring” also decreased between 2011 [24] and 2013 [25] tremendously but slightly increased in 2015 (this study).

We assume, through the increasing transparency within the cloud market, the possibility of a decrease in CSPs’ opportunistic behavior. Companies have access to global and exchangeable cloud resources because of increasing competition in the cloud market [57]. Standardized cloud services and features such as control possibilities enable customers to acquire cloud services from a variety of different CSPs [2, 32]. Should a CSP act in a dishonest manner, the cloud customer can quickly change the CSP. Distributed knowledge about the dishonest behavior of the CSP would prevent new cloud customers from acquiring cloud services from them. Cloud customers know that the possibility of CSPs opportunistic behavior decrease and, therefore, the relative importance of QoS attribute such as standardized contracts or monitoring possibilities decrease.

Finally, we identify the new QoS “test of solution”, which is related to product uncertainty during CSP selection decisions. According to our professionals, they particularly use a free trial version of cloud services to investigate if the new cloud service fits the existing IT infrastructure and if potential users are able to use such services. This testing procedure helps cloud customers during their CSP selection decision to assess if the cloud service will meet all requirements.

We assume the new identified managerial QoS “test of solution” is required by cloud customers because of the increasing amount of CSP, who offers a variety of unknown cloud services. Cloud customers face product uncertainty during the CSP selection decision due to information asymmetries [12]. Because an increasing amount of CSP enters the cloud market, cloud customers use a test of solution to verify if their requirements are met and the cloud service can be integrated into existing information systems [58].

Table 7 summarizes our results about the changes in the cloud environment between 2011 and 2015.

Table 7. Changes in the importance of QoS due to changes in the cloud environment

<table><tr><td>Category</td><td>Changing environment</td><td>Relevant QoS</td><td>QoS type</td><td>Newly identified QoS</td></tr><tr><td>Data protection</td><td>Increasing amount of laws, policies, and rules in place increases the importance of data protection</td><td>Legal compliance, geolocation of servers, and transparency of activities</td><td>Managerial</td><td>Yes, partly</td></tr><tr><td>Value co-creation</td><td>Increasing market competition forces the cloud customer to establish a partnership with CSP</td><td>Flexibility, integration, and support</td><td>Managerial and technical</td><td>Yes, partly</td></tr><tr><td>Opportunistic behavior</td><td>Increasing transparency within the cloud market decreases the possibility of CSPs' opportunistic behavior</td><td>Contract, control, and monitoring</td><td>Managerial and technical</td><td>No</td></tr><tr><td>Product</td><td>Increasing amount of CSP</td><td>Test of solution</td><td>Managerial</td><td>Yes</td></tr><tr><td>uncertainty</td><td>offers unknown cloud services</td><td></td><td></td><td></td></tr></table>

## 5.3 Contribution to Practice

According to our results, the combination of technical and managerial QoS attributes is important during CSP selection to assure future cloud service performance and success. While technical QoS attributes help cloud customers to select the best possible CSP to meet organizational requirements [59], managerial QoS attributes verify the capabilities of the CSP, increase predictability in the cloud service exchange relationship, and provide confidence in decision-making [15, 17, 21]. As cloud customers need to be confident to conduct optimal CSP selection decisions and not all necessary information for decision-making is available, they use managerial QoS attributes. For example, cloud customers are unable to predict future availability of the cloud service because of a lack of complete information. To assure future availability, cloud customers use contracts including predefined penalties in case the CSP does not offer the services as stipulated in the contract. The combination of technical and managerial QoS attributes is particularly important to assure future performance and conduct optimal CSP selection decisions (Table 6).

As our results stem from consensus among professionals, they provide not only guidance for new and existing cloud customers during CSP selection but also information for CSP to better address cloud customers’ needs.

Our results provide a starting point for new cloud customers to identify relevant QoS attributes when making CSP comparisons and during the CSP selection process. Using our results, new cloud customers can compare and select CSP by focusing on the most important technical and managerial QoS attributes. Because our professional panel was not able to reach a strong consensus on the importance of QoS attributes, persons charged with making cloud decisions should adapt this list to better accommodate individual requirements.

Existing cloud customers are informed about CSP selection because the relative importance changed during 2011 and 2015. Therefore, in line with new cloud customers, existing cloud customers get an updated guidance during CSP comparison and selection decisions.

Our results can also assist new and existing cloud customers to select adequate control mechanisms during use of cloud services. While the list of the most important QoS attributes is important when making CSP selection, several managerial QoS attributes can also help cloud customers to control CSP by using contracts, transparency of activities, monitoring, and certificates. While contracts provide a tool to implement predefined penalties in case a CSP not provide the services as stipulated in the contract, transparency of activities, monitoring, and the continuance of certificates may provide cloud customers with some control over the CSP. From a CSP perspective, these results provide a better understanding about cloud customers’ needs during CSP selection decisions and required control mechanisms during cloud service usage.

Cooperation with third parties and the cloud customer seems important for CSP. While several attributes are associated with the offered cloud service itself, our results show that CSP should also focus on QoS attributes such as geolocation of services or certification requiring cooperation with third parties. Geolocation of services not only defines QoS attributes such as latency but also influences legal compliance requirements of customers [60]. IaaS providers should consider data centers in different countries, while PaaS and SaaS providers might use different IaaS service providers in different countries if they themselves do not offer an adequate infrastructure. Certification of cloud services needs an endorsement conducted by a third party [39]. CSPs might use such endorsements not only to address customers’ needs but also to identify potential improvements through an independent third party. Furthermore, CSP should establish suitable relationships with cloud customers using features such as support possibilities to co-create value. Overall, to address customers’ needs, CSPs might consider third parties to address customer compliance, latency, or support requirements, or to extend transparency within their services.

Our results provide guidance for CSP regarding required control mechanisms. Cloud customers’ demand transparency of CSP’ activities, monitoring solutions, and up-to-date certificates. Therefore, CSP should implement and communicate these mechanisms to satisfy existing cloud customers and as a means of acquiring new customers. As a communication example, CSP could promote these mechanisms on their webpage to address customers’ needs during their CSP selection and control process.

## 6 Conclusion

Using an exploratory Delphi study design, we investigated the most important QoS attributes for the selection of CSP as identified by a panel of professionals. Through consensus, we identified the 13 most important QoS attributes for CSP selection and ranked their importance in 2015. We further showed that our results for QoS attributes comprise technical QoS attributes and managerial QoS attributes, both of

which are important during CSP selection.

Our main contribution to what is already known about CSP selection is threefold. First, our results show that cloud customers require an extensive variety of managerial QoS attributes during CSP selection. This finding supports prior research on cloud customer uncertainty in an ever-changing cloud environment. Second, a comparison of the most important QoS attributes in this study with those reported in previous studies identifies the following four key changes that take place within the cloud market: (1) The importance of increasing data protection; (2) The cloud customer’s pursuit of value co creation CSP; (3) The possibility of a decrease in CSPs’ opportunistic behavior; and (4) Product uncertainty remains a major problem during CSP selection. Third, we contribute to practice by providing a comprehensive overview of the most important technical and managerial QoS attributes to be considered when making cloud computing investment decisions. On the one hand, (potential) cloud customers get informed during CSP selection decision what the relevant QoS attributes are. On the other hand, our results show CSPs which QoS attributes and related control mechanisms are demanded from a customer perspective.

To conclude, given the ever-changing cloud environment, our results contribute to research and practice by pointing out the most important QoS attributes as identified by cloud customers in 2015. Further, our study provides a comparison of the most important QoS attributes with those as reported in previous studies. We hope that this study provides a starting point for future information systems research to further elaborate cloud decision criteria and dynamics that occur in the cloud market.

This research was funded by the German Federal Ministry for Education and Research (grant. No. 16KIS0078).

## References

1. Woods, V. Gartner says worldwide public cloud services market is forecast to reach \$204 billion in 2016. 2016 Accessed on 2016-06-01]; Available from: http://www.gartner.com/newsroom/id/3188817.

2. Truong-Huu, T. and C.-K. Tham, A novel model for competition and cooperation among cloud providers. IEEE Transactions on Cloud Computing, 2014. 2(3): p. 251-265.

3. Karunagaran, S., S. Mathew, and F. Lehner, Differential adoption of cloud technology: A multiple case study of large firms and SMEs, in International Conference on Information Systems. 2016: Doublin.

4. Garg, S.K., S. Versteeg, and R. Buyya, A framework for ranking of cloud computing services. Future Generation Computer Systems, 2013. 29(4): p. 1012-1023.

5. Schrödl, H., Purchasing Cloud-Based Product-Service Bundles in Value Networks-the Role of Manageable Workloads, in European Conference on Information Systems. 2012: Barcelona.

6. Garrison, G., S. Kim, and R.L. Wakefield, Success factors for deploying cloud computing. Communications of the ACM, 2012. 55(9): p. 62-68.

7. Garrison, G., R.L. Wakefield, and S. Kim, The effects of IT capabilities and delivery model on cloud computing success and firm performance for cloud supported processes and operations. International Journal of Information Management, 2015. 35(4): p. 377-393.

8. Weinhardt, C., et al., Cloud computing – A classification, business models, and research directions. Business & Information Systems Engineering, 2009. 1(5): p. 391-399.

9. Ragowsky, A., et al., Do Not Call Me Chief Information Officer, but Chief Integration Officer. A summary of the 2011 detroit CIO roundtable. Communications of the Association for Information Systems, 2014. 34(1): p. 1333-1346.

10. Brender, N. and I. Markov, Risk perception and risk management in cloud computing: Results from a case study of Swiss companies. International Journal of Information Management, 2013. 33(5): p. 726-733.

11. Subashini, S. and V. Kavitha, A survey on security issues in service delivery models of cloud computing. Journal of Network and Computer Applications, 2011. 34(1): p. 1-11.

12. Schneider, S. and A. Sunyaev, Determinant factors of cloud-sourcing decisions: reflecting on the IT outsourcing literature in the era of cloud computing. Journal of Information Technology, 2016. 31(1): p. 1-31.

13. Ghafori, V. and R.M. Sarhadi, Best cloud provider selection using integrated ANP-DEMATEL and prioritizing SMI attributes. International Journal of Computer Applications, 2013. 71(16): p. 18-25

14. Whiteside, F., et al., Challenging security requirements for US government cloud computing adoption. 2012, NIST: NIST Cloud Computing Public Security Working Group.

15. Zhou, J., E. Niemela, and P. Savolainen, An integrated QoS-aware service development and management framework, in Working IEEE/IFIP Conference on Software Architecture. 2007: Mumbai. p. 13-13.

16. Godse, M. and S. Mulik, An approach for selecting software-as-a-service (SaaS) product, in IEEE International Conference on Cloud Computing. 2009, IEEE: Los Angeles. p. 155-158.

17. Huang, J. and D.M. Nicol, Trust mechanisms for cloud computing. Journal of Cloud Computing: Advances, Systems and Applications, 2013. 2(9): p. 1-14.

18. Lins, S., S. Schneider, and A. Sunyaev, Trust is good, control is better: Creating secure clouds by continuous auditing. IEEE Transactions on Cloud Computing, 2016. PP(99).

19. Tran, V.X., H. Tsuji, and R. Masuda, A new QoS ontology and its QoS-based ranking algorithm for web services. Simulation Modelling Practice and Theory, 2009. 17(8): p. 1378-1398.

20. Ran, S., A model for web services discovery with QoS. ACM SIGecom Exchanges, 2003. 4(1): p. 1-10.

21. Ghosh, N., S.K. Ghosh, and S.K. Das, SelCSP: A framework to facilitate selection of cloud service providers. IEEE Transactions on Cloud Computing, 2015. 3(1): p. 66-79.

22. Petri, I., et al., Market models for federated clouds. IEEE Transactions on Cloud Computing, 2015. 3(3): p. 398-410.

23. Ramacher, D.-I.R. and L. Mönch, Robust multi-criteria service composition in information systems. Business & Information Systems Engineering, 2014. 6(3): p. 141-151.

24. Saripalli, P. and G. Pingali, Madmac: Multiple attribute decision methodology for adoption of clouds, in IEEE International Conference on Cloud Computing 2011: Washington. p. 316-323.

25. Repschlaeger, J., et al., Decision model for selecting a cloud provider: A study of service model decision priorities, in Americas Conference on Information Systems. 2013: Chicago.

26. Luoma, E. and T. Nyberg, Four scenarios for adoption of cloud computing in china, in European Conference on Information Systems. 2011: Helsinki.

27. Moe, C.E., M. Newman, and M.K. Sein, The public procurement of information systems: dialectics in requirements specification. European Journal of Information Systems, 2017. 26(2): p. 143-163.

28. Benlian, A. and T. Hess, Opportunities and risks of software-as-a-service: Findings from a survey of IT executives. Decision Support Systems, 2011. 52(1): p. 232-246.

29. Oliveira, T., M. Thomas, and M. Espadanal, Assessing the determinants of cloud computing adoption: An analysis of the manufacturing and services sectors. Information & Management, 2014. 51(5): p. 497-510.

30. Rieger, P., H. Gewald, and B. Schumacher, Cloud-Computing in Banking Influential Factors, Benefits and Risks from a Decision Maker's Perspective, in Americas Conference on Information Systems. 2013: Chicago.

31. Lang, M., M. Wiesche, and H. Krcmar, Conceptualization of Relational Assurance Mechanisms - A Literature Review on Relational Assurance Mechanisms, Their Antecedents and Effects, in International Conference on Wirtschaftsinformatik. 2017: St. Gallen.

32. Lang, M., M. Wiesche, and H. Krcmar. Perceived Control and Privacy in a Professional Cloud Environment. in Hawaii International Conference on System Sciences. 2018. Big Island, Hawaii.

33. El Zant, B. and M. Gagnaire, Towards a unified customer aware figure of merit for CSP selection. Journal of Cloud Computing, 2015. 4(24): p. 1-23.

34. Wang, X., J. Zhu, and Y. Shen, Network-aware QoS prediction for service composition using geolocation. IEEE Transactions on Services Computing, 2015. 8(4): p. 630-643.

35. Saleem, M.S., et al., Personalized decision-strategy based web service selection using a learning-to-rank algorithm. IEEE Transactions on Services Computing, 2015. 8(5): p. 727-739.

36. Wiesche, M., M. Schermann, and H. Krcmar, Understanding the enabling design of IT risk management processes, in International Conference on Information Systems. 2015: Fort Worth.

37. Cayirci, E., et al., A risk assessment model for selecting cloud service providers. Journal of Cloud Computing, 2016 5(1): p. 14.

38. Koehler, P., et al., Customer heterogeneity and tariff biases in cloud computing, in International Conference on Information Systems. 2010: St. Louis. p. 106.

39. Sunyaev, A. and S. Schneider, Cloud services certification. Communications of the ACM, 2013. 56(2): p. 33-36.

40. Berry, D., et al., Clouds on the horizon, in Guidelines for cloud vendor selection. 2016, KPMG.

41. Dove, E.S., et al., Genomic cloud computing: legal and ethical points to consider. European Journal of Human Genetics, 2015. 23(10): p. 1271-1278.

42. Currie, W. and J. Seddon, A cross-country study of cloud computing policy and regulation in healthcare, in European Conference on Information Systems. 2014: Tel Aviv.

43. Rai, A., L.M. Maruping, and V. Venkatesh, Offshore information systems project success: the role of social embeddedness and cultural characteristics. Management Information Systems Quarterly, 2009. 33(3): p. 617-641.

44. Pagani, M., Digital business strategy and value creation: Framing the dynamic cycle of control points. Management Information Systems Quarterly, 2013. 37(2): p. 617-632

45. Gopal, A. and B.R. Koka, The asymmetric benefits of relational flexibility: Evidence from software development outsourcing. Management Information Systems Quarterly, 2012. 36(2): p. 553-576.

46. Kritikos, K. and D. Plexousakis, Mixed-integer programming for QoS-based web service matchmaking. IEEE Transactions on Services Computing, 2009. 2(2): p. 122-139.

47. Dalkey, N. and O. Helmer, An experimental application of the Delphi method to the use of experts. Management Science, 1963. 9(3): p. 458-467.

48. Okoli, C. and S.D. Pawlowski, The Delphi method as a research tool: an example, design considerations and applications. Information & Management, 2004. 42(1): p. 15-29.

49. Linstone, H.A. and M. Turoff, The Delphi method: Techniques and applications. Vol. 29. 1975, Boston, USA: Addison-Wesley Publishing.

50. Schmidt, R.C., Managing Delphi Surveys Using Nonparametric Statistical Techniques. Decision Sciences, 1997. 28(3): p. 763-774.

51. Pare, G., et al., A systematic assessment of rigor in information systems ranking-type Delphi studies. Information & Management, 2013. 50(5): p. 207-217.

52. Schmidt, R., K. Lyytinen, and P.C. Mark Keil, Identifying software project risks: An international Delphi study. Journal of Management Information Systems, 2001. 17(4): p. 5-36.

53. Strauss, A.L. and J.M. Corbin, Basics of qualitative research. Vol. 15. 1990, Newbury Park, USA: Sage

54. Singh, R., M. Keil, and V. Kasi, Identifying and overcoming the challenges of implementing a project management office. European Journal of Information Systems, 2009. 18(5): p. 409-427.

55. Schreieck, M., M. Wiesche, and H. Krcmar. Design and Governance of Platform Ecosystems-Key Concepts and Issues for Future Research. in European Conference on Information Systems. 2016. Istanbul.

56. Goodman, S., Protecting privacy in a b2b world. Mortgage Banking, 2000. 60(7): p. 83-87.

57. Chen, P.-y. and S.-y. Wu, The impact and implications of on-demand services on market structure. Information Systems Research, 2013. 24(3): p. 750-767.

58. Yan, J.K. and R. Wakefield. Cloud Storage Services: Converting the Free-Trial User to a Paid Subscriber. in International Conferences on Information Systems. 2015. Fort Worth.

59. Wang, P. and X. Du, QoS-aware service selection using an incentive mechanism. IEEE Transactions on Services Computing, 2016.

60. Ramgovind, S., M.M. Eloff, and E. Smith, The management of security in cloud computing, in Information Security for South Africa. 2010, IEEE: Johannesburg. p. 1-7.

61. Gallupe, R.B., L.M. Bastianutti, and W.H. Cooper, Unblocking brainstorms. Journal of Applied Psychology, 1991. 76(1): p. 137-142.

## Authors

## Michael Lang

Technische Universität München,

Chair for Information Systems

Boltzmannstraße 3,

85748 Garching, Germany

+49 89 289 19527

michael.lang@in.tum.de

Michael Lang is a PhD student at the Chair for Information Systems, Technical University of Munich (TUM). He graduated in finance and information management from TUM and Universität Augsburg, Germany, and received the Master of Science with Honors in 2014. His main research interests is on decision-making in cloud sourcing projects as well as on cloud privacy and certification of cloud computing infrastructures.

Manuel Wiesche (corresponding author)

Technische Universität München,

Chair for Information Systems

Boltzmannstraße 3,

85748 Garching, Germany

+49 89 289 19539

wiesche@in.tum.de

Manuel Wiesche is a postdoctoral researcher at the Chair for Information Systems, Technische Universität München, Munich, Germany. He graduated in Information Systems from Westfälische Wilhelms-Universität, Münster, Germany and holds a doctoral degree in Information Systems from the Technische Universität München. His current research experiences and interests include IT risk management, IT-enabled management control systems, and personality of software developers. His research has been published in the Management Information Systems Quarterly, Journal of Management Accounting Research, and a number of refereed conference proceedings such as ECIS and HICSS.

Helmut Krcmar

Technische Universität München,

Chair for Information Systems

Boltzmannstraße 3,

85748 Garching, Germany

krcmar@in.tum.de

Helmut Krcmar is a Full Professor of Information Systems at the Chair of Information Systems, Technische Universität München (TUM), Germany. He worked as a Post Doctoral Fellow at the IBM Los Angeles Scientific Center, as Assistant Professor of Information Systems at the Leonard Stern School of Business, NYU, and at Baruch College, CUNY. From 1987 to 2002 he was Chair for Information Systems, Hohenheim University, Stuttgart. His research interests include information and knowledge management, service management, business process management, and information systems in health care and electronic government. His work has appeared in the Management Information Systems Quarterly, Journal of Management Information Systems, Wirtschaftsinformatik, the Information Systems Journal, and the International Journal of Medical Informatics.

## Appendix

## Appendix A

At the beginning of the one-to-one brainstorming, the researcher explained the research target, motivated the participant to state as many QoS attributes as possible, and restrained from judging or evaluating any responses [61]. Subsequently, the researcher conducted a semi-structured interview with each participant. On the basis of our research target, the semi-structured interview guide included questions to identify technical QoS attributes, operation-related aspects, and managerial QoS attributes to help participants reach a certain level of confidence during CSP selection decisions. Questions related to technical QoS included “Which operational requirements must or should a cloud service provider meet?”. Questions related to managerial QoS attributes included “What information during your selection decision helps you to select the right CSP?”. The research included some of the mentioned QoS from the brainstorming within the semi-structured interview to collect background information. After each interview, the authors discussed the results and iteratively adjusted the semi-structured interview guide. Figure 5 illustrates an overview of the QoS attribute identification process.

![](/api/attachments/TAQ6E3NF/fulltext/images/85247a96d6aaadf666f2015c54a69f1fdb389f79a8481d717ba35180b4ba94ce.jpg)  
Figure 5. QoS attribute identification process

## Appendix B

As an example of our coding process, Table 8 outlines selected codes and selected derived QoS attributes.

Table 8. Examples of codes and derived QoS attributes for cloud service provider selection

<table><tr><td>Selected codes (total 69)</td><td>QoS attributes (total 31)</td></tr><tr><td>certificate renewal reporting</td><td rowspan="2">Certification</td></tr><tr><td>certification authority</td></tr><tr><td>penalties in contract</td><td rowspan="2">Contract</td></tr><tr><td>service level agreements</td></tr><tr><td>network security specification</td><td rowspan="2">Functionality</td></tr><tr><td>performance</td></tr><tr><td>geolocation of servers</td><td rowspan="2">Geolocation of servers</td></tr><tr><td>home market provider</td></tr><tr><td>dashboard of service level agreement</td><td rowspan="2">Monitoring</td></tr><tr><td>data modification report</td></tr><tr><td>providers' service hotline</td><td rowspan="2">Support</td></tr><tr><td>providers support</td></tr><tr><td>free system releases</td><td rowspan="2">Test of solution</td></tr><tr><td>test of solution</td></tr><tr><td>sub-providers clarity</td><td rowspan="2">Transparency of activities</td></tr><tr><td>transparency of failure handling</td></tr></table>

## Appendix C

Members of our professional panel had different job positions and were from different industries, it was fundamental to assure that each panel member had the same understanding of each single QoS attribute. On the basis of the interviews, the researchers provided an initial description of each QoS. Participants were then asked to comment on the description using two options: the participant either had minor issues with the description and could provide possible extensions or minor changes, or the participant had major issues and disagreed with the provided description or had fundamental change requirements. In the case of major issues, the researchers discussed the change requirement during a follow-up telephone interview and, if required, adjusted the description accordingly. For example, major issues arose for legal compliance and geolocation of servers. Initially, geolocation of servers and legal compliance were used as synonyms. Following discussion, the researchers decided to split these constructs according to the opinions of the participants. After the changes were introduced, the participants were asked to make any further corrections and again validate the resulting descriptions. After two iterations, the participants agreed on the provided QoS descriptions.

Figure 6 illustrates an overview on the QoS attribute description process.

![](/api/attachments/TAQ6E3NF/fulltext/images/af54d3234b557e8c3e6b9e0747b8a760a34328332a97d63e5f4f535b84e74929.jpg)  
Figure 6. QoS attribute description process

## Appendix D

Selected quotes from our professional panelists:

Cloud customers use certificates during the CSP selection process to assure data protection. Certificates inform the cloud customer that an authority conducted an audit to verify that the CSP is compliant with a range of certification criteria. Cloud customers use certificates to have a standardized tool to compare the capabilities of the CSP. One of our professionals illustrates the value of certificates during CSP selection:

“Certificates can help to directly compare different CSP. Based on certificates I can say ‘ok, this cloud solution is certified for data security to 95% and this is 99% data-secured.’ Then my decision would probably always be to go with the higher certificate.” (Business Intelligence Manager #2)

Cloud customers may have limited knowledge about verification of the capabilities of CSP. Cloud customers outsource their information systems and buy services on-demand from the CSP, which may mean that knowledge and capabilities are no longer within the cloud customers’ company [12]. To assure compliance with existing laws and protect data, certification authorities support cloud customers during CSP selection by providing a certification attestation. One of our professionals described the value of certificates during CSP selection as follows:

“We do not have the resources to investigate the infrastructure and processes of possible CSP by ourselves. We rely on judgements of auditors who frequently conduct cloud audits. Those guys are well experienced and even more capable than we are in regard to evaluating the CSP.”

## (IT-Manager #14)

Information on the geolocation of servers is valuable for the cloud customer. Regional laws in place affect the level of compliance CSP reaches. While the European zone established a high level of data protection laws (for example, with regard to China), data protection laws are limited [41]. Cloud customers use such information to indirectly assure data protection and select CSP according to their own requirements. As noted by a professional, the knowledge of the geolocation of servers is a precondition to consider a CSP during the selection process.

“Personally for me I would prefer the servers not to be in China or in Russia and I can probably guarantee 100% that none of [CSP 1]s’, [CSP2]s’, or [CSP3]s’ servers are in those countries. And if this is a less-known company and a less-known provider, the geolocation of servers would be even more important during my selection decision.” (Consultant Manager #6)

A cloud exit strategy articulates clear steps, which are required to run through when and if a business customer decides to exit the cloud service in future. A cloud service strategy can become obsolete overnight due to changes in business strategy [43]. To remain flexible, cloud customers require a cloud exit strategy to export data to their own IT landscape or migrate data from one cloud service to another

“I want to know in advance if and exactly how a certain CSP is capable to perform an export from their service landscape. Unfortunately, from what I have seen and heard in many cases same provider requires sometimes a lot of effort.” (Senior Consultant #8)

Test of solution refers to the possibility to use a free trial version of the cloud service. A variety of possible CSPs and offered services exist. At the same time, cloud customers have individual information systems in place and employees with different skills and competencies. To assure the possible cloud service fits to existing information systems and the targeted employee is capable of using these systems, cloud customers may try out a trial version of available services.

“I am also experimenting now with [the Cloud Service] from [CSP] and I am looking to test if it is potentially interesting and comfortable.” (Consultant Manager #6)

## Appendix E

Table 9. Description of the 31 unranked QoS attributes for cloud service provider selection

<table><tr><td>QoS attribute</td><td>Description provided by professional panel</td></tr><tr><td>Assurance statement</td><td>Self-provided assurance statements of a CSP to address trust-related issues.</td></tr><tr><td>Benchmark</td><td>A CSP has high scores in an unbiased comparison of IT performance relative to peer organizations and those considered best-in-class.</td></tr><tr><td>Business process transparency</td><td>Transparency of CSP's organization structure, internal processes, roadmap, and development objectives.</td></tr><tr><td>Certification</td><td>A CSP is certified by an independent authority in accordance with established requirements or standards.</td></tr><tr><td>Cloud exit strategy</td><td>A CSP articulates clear cloud exit steps, which will take place when and if a business customer decides to exit its cloud in the future.</td></tr><tr><td>Contract</td><td>The provider offers understandable contractual arrangements including a clear cost structure (e.g., consumption-based pricing model).</td></tr><tr><td>Control</td><td>A CSP provides remote access tools to provide proactive control of data, functionalities, and processes (e.g., customization).</td></tr><tr><td>Deployment model</td><td>A clearly defined deployment model in terms of ownership, control of architectural design, and degree of available customization (e.g., private cloud, hybrid cloud, community cloud, and public cloud).</td></tr><tr><td>External business communication</td><td>Information about a CSP, its vision, services, and pricing is communicated clearly on provider's website, info sheets, etc.</td></tr><tr><td>Failure preventive measures</td><td>A CSP communicates unsuccessful preventive measures and mechanisms.</td></tr><tr><td>Financial performance</td><td>A CSP performs well financially, in terms of profit, revenue, equity, etc.</td></tr><tr><td>Flexibility</td><td>A customer can independently adjust the obtained capabilities, and the adjustments are carried out automatically within a short period of time and with transparent costs.</td></tr><tr><td>Functionality</td><td>The set of functions or capabilities (performance, availability, security, and scalability requirements) associated with the cloud solution matches the demands of the customer.</td></tr><tr><td>Geolocation of servers</td><td>Geographical location of providers' servers is suitable in terms of data protection legislation and user latency.</td></tr><tr><td>In-house recommendation</td><td>A CSP is highly recommended by a colleague, an IT-department member, or similar within a company.</td></tr><tr><td>Integration</td><td>Configuration of the service enables its smooth integration into the IT landscape of the business.</td></tr><tr><td>Interoperability</td><td>A customer can save and export data in standard formats, the cloud service offers open interfaces for integration with other cloud services or applications, and customers can access the cloud service location independently through various devices.</td></tr><tr><td>Legal compliance</td><td>Because of its geographical location, policies, etc., a CSP complies with legal and regulatory requirements of the customer.</td></tr><tr><td>Market share</td><td>The actual market share of a CSP.</td></tr><tr><td>Monitoring</td><td>A manual or automated IT monitoring and management technique, which provides transparency of cloud service quality.</td></tr><tr><td>Open communication</td><td>A CSP openly communicates previous incidents, failures, and their handling and predefines channels to report straightforwardly such situations if they occur in the future.</td></tr><tr><td>Ownership</td><td>Evident ownership of service hardware, software, etc. (by a CSP, a sub-provider, or others)</td></tr><tr><td>Personal contact</td><td>A CSP provides and establishes a strong personal contact.</td></tr><tr><td>Process maturity</td><td>The maturity of the business processes of the provider align with established best practices in the IT service sector.</td></tr><tr><td>Reputation</td><td>A CSP has earned a strong reputation in industry over time, confirmed by customer's portfolio, and evident in media, internet, or other information resources.</td></tr><tr><td>Standard operating environment</td><td>Consistency across operations enabling an easier cloud exit if necessary.</td></tr><tr><td>Support</td><td>A CSP possesses a responsive service support, which provides all operative processes necessary for the handling of service interruptions andfor implementation of changes.</td></tr><tr><td>Test of solution</td><td>A CSP enables convenient trial periods of a service.</td></tr><tr><td>Third party recommendation</td><td>A CSP is highly recommended by a third party.</td></tr><tr><td>Track record</td><td>A CSP has a track record free of vulnerability incidents (such as data loss, data leakage, or hardware failure) widely known through media.</td></tr><tr><td>Transparency of activities</td><td>Transparency of security, data privacy, data access, cloud architecture, service level competencies, etc.</td></tr></table>
