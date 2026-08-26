---
otero_id: 1814
otero_key: "RVDPF5YK"
title: "A knowledge based component/service repository to enhance analysts’ domain knowledge for requirements analysis"
authors: "Padmal Vitharana; Hemant Jain; Fatemeh “Mariam” Zahedi"
year: "2012"
journal: "Information & Management"
doi: "10.1016/j.im.2011.12.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A knowledge based component/service repository to enhance analysts’ domain knowledge for requirements analysis

Padmal Vitharana <sup>a,</sup>\*, Hemant Jain <sup>b,1</sup>, Fatemeh ‘‘Mariam’’ Zahedi <sup>b,2</sup>

<sup>a</sup> Whitman School of Management, Syracuse University, Syracuse, NY 13244-2130, USA

<sup>b</sup> Sheldon B. Lubar School of Business, University of Wisconsin – Milwaukee, P.O. Box 742, Milwaukee, WI 53201, USA

## A R T I C L E I N F O

Article history: Received 10 March 2010 Received in revised form 16 March 2011 Accepted 18 September 2011 Available online 22 December 2011

Keywords: Component-based development Requirements analysis Design research Domain knowledge

## A B S T R A C T

Knowledge of the business domain (e.g., insurance claim, human resources) is crucial to analysts’ ability to conduct good requirements analysis (RA). However, current practices afford little assistance to analysts in acquiring domain knowledge. We argue that traditional reuse repositories could be augmented by adding rich faceted information on component/services and artifacts such as businessprocess templates to help analysts acquire domain knowledge during RA. In this paper, we present the design of a Knowledge Based Component Repository (KBCR) for facilitating RA. Then, we report on the design and development of a KBCR prototype. We illustrate its application in a system that is populated with components and process templates for the auto insurance claim domain. An empirical study was conducted to assess its effectiveness in improving RA. Results showed that KBCR enhanced analysts business domain knowledge and helped them better prepare for RA. Our key research contribution is to offer analysts a rich repository (i.e., KBCR) containing domain knowledge that they could utilize to acquire domain knowledge that is crucial for carrying out RA. While repositories of reusable components have been employed for some time, no one has used such repositories to help analysts acquire domain knowledge in order improve the RA of the system.

\- 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Requirements analysis (RA) is one of the most important steps in the systems development process [5]. During RA, analysts identify potential users and their requirements for a new system or a major alteration to an existing system. In the process, analysts examine existing systems and relevant documents, interview stakeholders, deal with users’ conflicting needs, and sometimes develop use cases, scenarios, and prototypes.

Knowledge of the business domain (e.g., insurance claim, human resources) is crucial to analysts’ ability to effectively conduct RA and to successfully design systems. While analysts have expertise in systems development, their knowledge of business domains is often limited. In discussing the importance of domain knowledge, a study found that 28% of the job openings for of Fortune 500 firms required applicant analysts to have knowledge of a specific industry [6]. Domain knowledge helps analysts understand the problem, conduct more effective user interviews, and identify more accurate and comprehensive requirements.

Over the years, component and service-based development have become popular, and repositories containing reusable software assets have become commonplace. As a result, the need for a repository-driven approach to component storage and retrieval in developing business applications is widely acknowledged. However, the primary functions of these repositories have been limited to providing storage and search facilities for software components. Analysts and developers use these components in constructing end applications. To the authors’ knowledge, no one has examined the potential of using these repositories to facilitate the RA process. We argue that since component repositories contain reusable software assets embodying business domain knowledge, they should be designed to assist analysts in understanding the business domain. Existing component repositories can be augmented to facilitate RA by including rich business-oriented, faceted descriptions of the component and other domain artifacts such as business-process templates, use cases, and scenarios. This detail can provide analysts additional information on relevant business processes, how components relate to one another, and the role they play in the process. It can also enhance component search and selection with reference to a business process.

In our research, we extend the previous work of Vitharana et al. [11] who presented a scheme for classifying and describing business components. We augment their design to facilitate RA. The resulting design includes relationships among components, a flexible search facility, and other knowledge artifacts. The enhanced design (called Knowledge Based Component Repository (KBCR)) was used as a blueprint to build a prototype of KBCR in cooperation with a multinational software consulting company. An empirical study was then conducted to assess its effectiveness in facilitating analysts’ interview readiness and user interview questionnaire development during the RA process.

## 2. Review of literature

## 2.1. Role of analyst’s domain knowledge in requirements analysis

Analysts’ knowledge of the domain is particularly crucial in their interactions with users. Lack of adequate domain knowledge makes the RA process more time consuming, error prone, difficult, and costly. Moreover, a lack of domain knowledge leads analysts to rely primarily on users for learning about the domain [4]. Analysts’ dependency on users for domain knowledge puts an additional burden on the users. Furthermore, analysts may form a biased view of the domain due to the users’ professional or political predispositions.

While there are many approaches to requirements elicitation, interviewing is one of the most commonly used; it requires analysts to prepare a set of questions to be answered by the user. Knowledge of the problem domain plays a crucial role in preparing this set of questions. Any lack of adequate knowledge about the domain may force analysts to ask elementary questions about the domain and as a result, increase the interview time, lessen the communication quality, and damage the analysts’ credibility. Moreover, increased domain knowledge allows an analyst to recognize and resolve conflicts.

## 2.2. Objects and components

An object has both a state (based on its attribute values) and a behavior (based on its operations). It reflects a real-world entity in the application domain. A business component contains a specific business function. In many cases, a component that supports a discrete business function needs to deal with multiple objects and have process elements associated with it. For example, in the auto insurance domain, object classes may include customer, account, and vehicle while components include claims, salvage processing, and claim settlement.

## 2.3. Component repositories

Reusable artifacts are often identified as part of the application development process, and are subsequently classified and archived in a repository for future search and retrieval. Some of the common representational methods for classifying reusable artifacts include enumerated, keyword-based, and faceted representations. Although most of the earlier studies focused on cataloging the programming code (i.e., source modules and object classes), recently there has been interest in representational methods for business components and web services. Current component repositories typically contain information about available components and their characteristics with varying degrees of detail and precision. In many cases, they store component names, descriptions, and technical interface details, and are suitable for use by analysts during the design and construction (including component assembly) stages of a system’s development.

To date, one of the more comprehensive approaches to classifying artifacts is the Reusable Asset Specification (RAS) developed by the Object Management Group (OMG). RAS offers an open standard for packaging and managing any set of software artifacts for subsequent reuse. A RAS asset might be any software artifact such as a use case, design model, or code sample. Thus it is not especially geared towards specifying, archiving, searching, and retrieving reusable components. RAS does not conform to a particular architecture because it does not offer a mechanism to partition a domain into salient assets and their structures, such as business processes and relationships between assets.

## 2.4. Domain knowledge representation

Software embodies knowledge about a particular domain [9], and its successful creation requires domain analysis for creating reusable assets. Two approaches are predominantly used in designing components: in a top-down approach, domain engineers segment the domain into a set of reusable assets. This iterative exercise incorporates concepts in decomposition/aggregation and generalization/specialization. Alternatively, low-level assets such as objects have been used to develop higher level assets such as business components. Vitharana et al. [10] proposed a methodology for component fabrication and argued that the business strategy of component development companies should guide the design of reusable business components. They linked business strategy with component design through managerial goals (cost effectiveness, ease of assembly, customization, reusability, and maintainability). These goals are then mapped to technical features (coupling, cohesion, number of components, component size, and complexity). They developed a formal model, called Business Strategy-based Component Design, that uses a domain model to derive the component structure by grouping appropriate object classes to achieve the desired business strategy.

We used this approach to create components for our repository. Since the domain analysis is conducted for a particular domain, the knowledge is embedded in the components resulting from domain analysis and component design. Facts collected during knowledge acquisition, domain modeling, and resulting reusable assets should therefore be subjected to expert validation.

While domain analysis does result in a set of reusable components, it also generates useful domain-level information such as business processes and relationships between components. Conventional component repositories focus only on storing details about components, mostly technical in nature Hence, existing repositories are not intended to improve the analysts knowledge of the problem domain.

## 3. A Knowledge Based Component Repository

## 3.1. KBCR design

We designed a knowledge-based component repository (KBCR) to support the storage and retrieval of components as well as to facilitate the RA process. The KBCR included the following features:

\- A structured description of the ‘‘basic information’’.

\- A business oriented description of the ‘‘facet information’’.

\- Business-process templates.

\- Relationships among the components.

\- A flexible search capability.

This enhanced KBCR augments the work of Vitharana et al. whose design included only the first two features.

Auto insurance claim handling was selected as the problem domain for our work. Domain experts from the collaborating multinational software consulting firm created a domain model for the auto insurance claim using the UML notation. Once the components were designed and constructed, they were classified, described, and stored in the KBCR. We used examples from the auto insurance claim handling domain to illustrate the design of the KBCR. The following sections describe the KBCR architecture which is illustrated in Fig. 1.

![](/api/attachments/RVDPF5YK/fulltext/images/e48e4b1f190300f8c149f46a3198095e480bfc27447dcd997199e3ec138bb2d8.jpg)  
Fig. 1. KBCR architecture.

Table 1 Basic information.

<table><tr><td>Name</td><td>Description</td></tr><tr><td>Component ID</td><td>Unique identifier of the component.</td></tr><tr><td>Component name</td><td>Name of the component.</td></tr><tr><td>Component description</td><td>Description of component and its related domain.</td></tr><tr><td>Component version</td><td>Version of the component.</td></tr><tr><td>Domain</td><td>Business domain to which the component belongs.</td></tr><tr><td>Business function</td><td>Functions of the component from business perspectives.</td></tr><tr><td>Deployment environment</td><td>The deployment environment for deploying and using the component.</td></tr><tr><td>DBMS environment</td><td>The database in which the component data are stored.</td></tr><tr><td>Operating system</td><td>Operating system required to deploy the component.</td></tr><tr><td>Programming language</td><td>Programming languages used in developing the component.</td></tr><tr><td>Primary industry</td><td>The main industry to which the component belongs.</td></tr><tr><td>Cost</td><td>Cost of acquiring the component and transacting with it.</td></tr><tr><td>Expiration</td><td>Expiration date of the component, if any.</td></tr><tr><td>License type</td><td>License type (permanent, temporary, limited, etc.).</td></tr><tr><td>Owner</td><td>Name of the component owner.</td></tr><tr><td>Owner URL</td><td>The component owner&#x27;s website address.</td></tr><tr><td>Component URL</td><td>The website address where the component is available.</td></tr><tr><td>Database URL</td><td>Pointer to database where the component data is stored.</td></tr></table>

Each component was described and represented at several levels of abstractions, including component, interfaces or services, methods, parameters, and exceptions. Providing details at multiple levels of abstraction helps analysts assess the components’ utility. Each level of abstraction includes a set of ‘‘basic information’’ and ‘‘facet information.’’

(i) Basic information. This describes the salient descriptors, architecture, and technical environment that can be used to narrow down the search to those components suitable for the target environment. Table 1 provides a brief description of various types of basic information stored in a KBCR.

(ii) Facet information. This is the domain knowledge embedded in a component. It is represented in terms of the seven facets: synonym, role, rule, function/task, action/event, and user. For example, the Rule facet describes the business rules embedded in a component, while the Function/Task facet portrays the business functions and tasks performed by the component. Table 2 describes facets supported by the KBCR with examples given from the auto insurance claim handling domain.

(iii) Business-process templates. This consists of details that provide domain information beyond a single component involving process (or activity) diagrams, sequence diagrams, or other documentation that is stored as ‘‘design documents’’ in KBCR. Although the primary focus of domain analysis is to derive a set of reusable assets, the intermediary artifacts such as use cases and process diagrams also embody domain knowledge [1]. Use cases illustrate interactions between actors and systems in a domain. For example, a use case for insurance claim handling would show how different users (customers and claim handlers) interact with various parts of the system for claim initiation and arbitration. Process or activity diagrams depict domain processes, their sequence, and relationships. Thus, when analysts are unfamiliar with the domain of the system, they can review the domain artifacts such as use cases and process diagrams with component-level details, to understand the domain by examining how various actors might interact with the system and how domain processes relate to each other. It should be noted that these artifacts are not intended to represent specific business process or business rules but are meant to represent typical processes and rules at the domain level.

Table 2 Facet information.

<table><tr><td>Facet</td><td>Description</td></tr><tr><td>Synonym</td><td>A synonym is another possible name for a component.</td></tr><tr><td>Role</td><td>A component could be described in terms of the role it plays in potential applications. For example, the role of the “Claim Settlement” component handles the claim settlement activity.</td></tr><tr><td>Rule</td><td>Components are typically developed for business domains, which inherently contain business rules. Therefore, a component could be described in terms of business rules supported by the component. For example, one of the business rules for the “Claim Intimation” component may be that the customer must initiate the claim within a specified time period after an accident has taken place.</td></tr><tr><td>Function/task</td><td>A component provides some functionality or supports one or more tasks in a business process. Accordingly a component could be described in terms of its functionality or tasks. For example, typical functions/tasks of the “Arbitration” component include the initiation of the arbitrationprocess and the storage of its related details.</td></tr><tr><td>Element/part</td><td>A component represents abstraction of a business domain or sub-domain. This abstraction may contain elements or parts of the component. Using this facet, one could identify the component based on elements or parts that makes up the component. For example, elements of “Injury Treatment” components might include injuries, types of treatment, clinic, and medical report.</td></tr><tr><td>Action/event</td><td>Using this, one could classify a component based on actions or events that are supported by the component. For example, possible actions/events of a “Claim Investigation” component might include interviewing witnesses and reviewing police report.</td></tr><tr><td>User</td><td>The &#x27;User&#x27; facet characterizes a component in terms of possible types of applications and users of the component, since a component could be used by multiple applications and different users. For example, users of a “Claim Assessment” component might include the insurance claim handling software, assessors, and claim handlers.</td></tr></table>

Thus, the KBCR can maintain business-process templates that capture the typical business processes and workflow used in the domain. Business-process templates along with descriptions represent the best practices of the firm and/or industry. The process templates can be organized in a hierarchical manner and thus one or more sub-processes of the business process can be exploded down to the nth level until an elemental level is reached. Fig. 2 shows examples of process templates corresponding to business process and workflow for the auto insurance claim handling domain. These templates were developed in consultation with domain experts. Users of the KBCR are able to modify pre-existing templates dynamically based on their needs. The modified template could then be added to the KBCR for future use.

(iv) Relationships among components. In studying the system development process, several researchers have examined how conceptual models influence analysts’ understanding of the problem domain. Burton-Jones and Meso [3] found that conceptual models such as class diagrams enhance analysts’ understanding of the domain and assist them in designing the system. Thus, the hierarchical relationships among components are maintained in the KBCR. These show places where a coarse grain component is composed of a number of finer grain components. On the other hand, UML offers sequence diagrams to depict interactions among objects. Such diagrams show participating objects and interactions among them, arranged in sequence generally with respect to a particular use case. We extended this concept to sequential relationships among components in the form of preceding and succeeding relationships based on the typical business processes in which the components are used.

(v) Search capability. By searching and examining various KBCR artifacts, users can acquire the domain knowledge embedded in them. Thus, a search capability is an important part of a KBCR. At the component level, keywords can be used to search for components and a search can be initiated for various types of component information including faceted information. For example, a KBCR user could make a broad search in an industry (e.g. auto insurance) or a business function (e.g. claim processing) and then narrow down the search.

Search results provide a set of information and links to those components that match the search; they may also provide components that are ‘‘related’’ to the matched components. This allows users to explore for components that have a sequential relationship with a component resulting from the search. Another aspect of search functionality may involve the information and navigation of the component hierarchy. The component structure is provided in a hierarchical structure that the user can traverse and search. Thus, the user-friendly search interface provides a useful set of information for search and navigation, guides the user on how to narrow down the search, and helps users explore the relationships between components, providing users with an insight into the structure of the domain.

The enhanced KBCR can therefore serve as a rich source of business domain knowledge. The additional facet information provided at component, interface, method, parameter, and exception levels, along with component design documents, thus provide detailed information on many aspects of the domain. Hence, a varying level of domain abstractions is offered to help analysts during the requirement analysis and subsequent design stage.

## 3.2. Prototype implementation

The initial version of the KBCR prototype was implemented in 2004. Since then, it has gone through two revisions. Here, we discuss the implementation details of the current (latest) version.

The KBCR prototype is a web-based application. The technologies used in its implementation were Java, Java Server Pages, XML, and the Oracle database system. XML was chosen in order to accommodate the semi-structured nature of the component knowledge and to support a context sensitive component search. The structured description of the component (basic information) such as name, domain, and deployment environment was stored in an Oracle database. Business-oriented faceted descriptions of the component (i.e., facet information) such as facet descriptors for functionality, business rules, and roles of the component at various levels of abstraction were semi-structured in nature and hence were coded in XML. The prototype implemented the role-based security, which gave access and update rights to users based on their roles. It also supported a complete workflow for component submission, review, and approval process.

![](/api/attachments/RVDPF5YK/fulltext/images/c8f09457dc1828d6b3061046fba1055192ccb65315c342cb6fc67df9bc95e18f.jpg)  
Fig. 2. A typical business process for auto insurance claim handling.

Fig. 3 illustrates the search page of the KBCR prototype. An analyst can search for a component by typing keywords, selecting one or more fields from basic information or entering one or more words describing facet information (illustrated in Structured Description and Business-oriented Description in Fig. 1). Users can narrow down search results by searching within results of the previous search. While keywords are matched against both the database and the XML knowledge-base, the basic information (e.g., component name) and facet information (e.g., rules) are matched against the database and XML knowledge-base, respectively. Fig. 4 shows the results of a typical search when ‘‘Finance and Insurance’’ is selected as the primary industry and ‘‘claim’’ is typed as the keyword. As shown at the top of Fig. 3, SearchComponent and SearchTemplate options allow the analyst to search for components and business process templates, respectively.

Since the analyst might have little or no knowledge of the application domain, names, description and all basic and facet information of components were designed to be straight-forward and descriptive. The following segment illustrates the ‘‘description’’ for the Settlement component (provided by the domain experts of the collaborating firm):

![](/api/attachments/RVDPF5YK/fulltext/images/32a4d960c49a972bd798ae6d9f5f25b2d5490b9c6c01ce5d93b8fa741f3baa89.jpg)  
Fig. 3. Search page for component knowledge-base.

This component stores and retrieves details of the amount for which the claim is settled. A single claim can have many settlements (e.g., an initial ad hoc payment and a final settlement after it undergoes a full claims handling). In addition, the claimant can come back and request a higher amount for damages that were not known previously. Settlement can be of two types: (i.) No loss settlement is where the claimant takes the salvage items and the amount paid is the gross loss less the salvage value; and (ii.) Total loss settlement is where the salvage item is given to the insurance company and the settlement paid to the claimant.

Fig. 5 illustrates a screen shot of sample basic information. The tree structure on the left allowed the KBCR users to traverse through various levels of abstraction (such as component and method) while details about the abstraction were displayed on the right-hand side of the screen.

The top of the screen shows the various management functions, such as ‘‘review component,’’ ‘‘submit component,’’ and ‘‘search component’’ supported by the KBCR; the bottom of the screen shows the component related functions, such as ‘‘update,’’ ‘‘new version,’’ ‘‘design documents’’ and ‘‘related component.’’ Fig. 6 shows a screen shot of sample facet information at the interface level for the claim intimation component. (Note: In the KBCR prototype, the term facet information was changed to additional information to increase the user-friendliness of the interface.)

Analysts could also search the KBCR for process templates representing important processes and sub-processes. The template description and search work was similar to those used for components. Process diagrams in templates used the Business Process Modeling Notations adopted by Microsoft Visio for creating templates. The KBCR can automatically call the VISIO to display the template. By clicking on + and  symbols, the processes can be expanded or contracted as shown in Fig. 2.

## 4. Assessing the impact of using KBCR

Assessment of the effectiveness of using the KBCR was made by an empirical investigation.

## 4.1. Assessment model

One of the important stages of RA is the design of user interview questions. We posit that access to the KBCR enhances analysts’ domain knowledge, which helps them to prepare for user interviews. We further posit that access to the KBCR directly enhances the quality of the user interview questionnaire. Fig. 7 shows the assessment model. The KBCR prototype was examined to assess the extent to which it helped the analyst in preparing for user interviews and developing interview questions.

<table><tr><td colspan="6">ManageComponent ReviewComponent SubmitComponent SubmitTemplate ShoppingCart SearchComponent SearchTemplate Help Logout</td></tr><tr><td rowspan="7"></td><td colspan="5">Search ResultsDisplaying 1 to 5 of 7 Results</td></tr><tr><td>ComponentId</td><td>Version</td><td>Name</td><td colspan="2">PrimaryIndustry</td></tr><tr><td>4</td><td>1</td><td>Claim Intimation</td><td colspan="2">Finance and Insurance</td></tr><tr><td>39</td><td>1</td><td>Auto Damage Claim</td><td colspan="2">Finance and Insurance</td></tr><tr><td>38</td><td>1</td><td>Structure Damage Claim</td><td colspan="2">Finance and Insurance</td></tr><tr><td>42</td><td>1</td><td>Party</td><td colspan="2">Finance and Insurance</td></tr><tr><td>46</td><td>1</td><td>Settlement</td><td colspan="2">Finance and Insurance</td></tr><tr><td colspan="6"></td></tr></table>

Fig. 4. Results of a search.

![](/api/attachments/RVDPF5YK/fulltext/images/6f1fd97296c7c67b4d668952fa36321941dcf572bf03b19391683664a823bdc6.jpg)  
Fig. 5. A sample of basic information for components.

The participants of the controlled experiment were divided into two groups: one with access to the KBCR (treatment group) and the other without access (the control group). The latter followed a traditional approach in which the analyst learned about the domain and proposed system through available documents, reports, and existing systems. In our experiment, this information was provided as a detailed problem description. We acknowledge that there may be other ways of acquiring domain knowledge, but they are not easily available or widely used.

## 4.2. Hypothesis development

Since the KBCR is designed to assist analysts in their RA task, Task Technology Fit (TTF) is a good method of assessing KBCR’s effectiveness in improving task outcomes. Lin and Huang [7] have also adopted TTF for studying knowledge management systems. In our experiment, the task corresponds to an analyst developing a user interview questionnaire. TTF theory posits that the fit between task and technology enhances performance.

![](/api/attachments/RVDPF5YK/fulltext/images/1eb23a703524c186ad5b87f82038b5893f28aafa0955a87b230fa939cd721f02.jpg)  
Fig. 6. A sample of the facet information for components

![](/api/attachments/RVDPF5YK/fulltext/images/944e2fe2f371fa6c9083e61d157e0de59f10d71133c9bbcd2575a058e8eed174.jpg)  
Fig. 7. The KBCR assessment model.

In our study, access to the KBCR distinguished treatment and control groups. The performance was modeled from two ways. The first determined how analysts felt about their own understanding of the domain knowledge and how well they were prepared for RA interviews (a self-assessment perspective) in which analysts compared their own knowledge and ability before and after exposure to the KBCR. Two constructs in the model captured analysts’ self perceptions: domain knowledge, and interview readiness. We argue that access to the KBCR leads to increased domain knowledge, which in turn makes analysts feel better prepared for embarking on user interviews, see Fig. 7. The second assessment was analysts’ relative performances. In here, analysts’ performance when developing interview questions was compared between those who had and those who did not have access to the KBCR. Assessing relative performance required third-party judges to compare and rate analysts’ measurable performance outcomes. In our study the quality of interview questions was rated by thirdparty judges. We believe that performance improves when analysts have access to the KBCR. The analysts’ initial domain knowledge was used as a control variable to account for the variability of domain knowledge at the start of our study. Hence, we posit:

$\mathbf { H _ { 1 } } .$ Access to the KBCR enhances analysts’ self-reported domain knowledge.

$\mathbf { H } _ { 2 } .$ Analysts’ domain knowledge enhances their self-reported user interview readiness.

$\mathbf { H } _ { 3 } .$ Access to the KBCR enhances analysts’ user interview questionnaire quality.

## 4.3. Variable measurement

An instrument was developed based on a literature survey of items used to measure analysts’ domain knowledge and selfreported interview readiness (see Appendix 1). Pre-testing and card sorting methods were used to ensure validity and reliability of the constructs. We created a website for deploying the survey instrument to collect data from participants at different stages during the experiment. Prior to the main study, a pilot study was conducted; 11 students from a graduate information systems course participated in this pilot study to test the survey instrument, the website, and the overall logistics of the experiment. Based on this, several minor changes to the survey instrument and website were made. See Fig. 8 for a sample page of the survey.

## 4.4. Experimental design and data collection

We tested the hypotheses by using an empirical investigation: a controlled experiment. The task was to develop interview questions for requirement analysis of a new system for auto insurance claim handling. Participants were randomly assigned to one of two groups; the treatment group had access to the webbased KBCR while the control group did not; otherwise both groups were given the same information. We chose a single domain to control for domain-type bias. The KBCR contained 30 components and 12 business process templates.

At different stages of the experiment, the research study website presented participants with different parts of the survey instruments. At the time of the registration, the data on participant’s initial domain knowledge and participant demographic information were collected. Upon uploading the interview questions, participants filled out the survey on perceived domain knowledge (post study) and perceived interview readiness. Quality of interview questionnaires was assessed by two independent raters. The access to the KBCR was provided via a hyperlink from the website, which opened a separate window containing the KBCR. All participants were told to prepare the user interview questionnaire offline and upload it to the website.

Participants were students recruited from two universities in the U.S.; one in the Northeast and the other in the Midwest. In both universities, participants with a background in system analysis and design were sought. Professors who taught undergraduate and graduate courses with the desired subject characteristics were asked to solicit their students’ participation. Participants were given assignment credit for participating in the study. (There was a different assignment for those who chose not to participate.) In addition, four randomly drawn cash prizes of \$100 were offered as an incentive for the completion of the experiment.

One of the researchers visited each class at the beginning of the experiment and gave a 20 min presentation on the research project. During the presentation, students were informed of the objective of the study, their role, and the incentives for participation. They were instructed not to collaborate with others and not to seek additional information from other sources beyond that provided to them. Students were given written instructions explaining the experimental task (see Appendix 2 for protocol details). Interested students were told to visit the study website for their initial registration and ongoing participation. During the class visit, the use of the KBCR and its features (e.g., search, navigation, etc.) were briefly demonstrated. Because study participants did not have any prior knowledge of KBCR, some of the search and navigation features were simplified (in the Basic Information section, only Component Name was included in the search page). A comprehensive help function for the KBCR was developed and made available to the participants. This function contained text and screen shots and was available on the KBCR when the participants first visited it. They were informed that only some of them would have access to the KBCR. The experiment started several weeks into the semester and lasted for about four weeks.

Table 3  
![](/api/attachments/RVDPF5YK/fulltext/images/dd4f36008c1b4210a1497140b05a79d6dacadf6147f58d86a5cb2f04e338af32.jpg)  
Fig. 8. Sample page of the web-based survey instrument.

## 4.5. Data analysis

A total of 34 students completed the experiment. The very involved nature of the experiment lasting most of the semester and the particular population sought limited the number of students who could participate in the study. In the data analysis, we included only those who completed the entire exercise (all the steps listed in Appendix 2). Those who did not complete the exercise withdrew from the research study. The demographics of the treatment and control groups were not statistically significant. Females represented about 41% of the sample. Fifteen (out of the 34 who completed the task) had access to the KBCR.

The three latent constructs in the model—analyst’s initial domain knowledge (control variable), analyst’s domain knowledge upon completion of the study, and interview readiness—were factor analyzed separately since each referred to a different level of the analysis. In each case, a single eigenvalue above 1.0 emerged. Items for each construct loaded well into a single factor with factor scores ranging from 0.92–0.97, 0.95–0.97, and 0.93–0.96, respectively. This provided support for the convergent validity of the constructs (Table 3).

The measurement of each construct involved a ‘‘general’’ or omnibus item that directly represented the construct. The factor analyzed scale for each construct was regressed with the general item for that construct. Each regression was statistically significant (p < 0.0001), which provided support for criterion validity as well as additional evidence for convergent validity of the constructs.

Since each level in the model involved only one construct, discriminant validity was not an issue in our model. Cronbach’s alpha and AVE were computed to assess the reliability of the three constructs (see Table 3). Traditional guidelines require Cronbach alpha values to be greater than 0.7 and AVE greater than 0.5. Hence, all three scales exhibited high reliability. The questionnaire quality was assessed by two external judges with experience in systems analysis and design. Over a two-week period, they were trained on how to rate questionnaires. Using a 0–10 scale, they were asked to rate each questionnaire for quality along 10 dimensions: initiation/ reporting, claim investigation, claim assessment, claim settlement, injury treatment, claim subrogation, salvage processing, claim dispute, system features, and other. The first dimension referred to those entries corresponding to customer initiation and reporting of the claim (e.g., can a customer submit a claim online?). The judges were given detailed written instructions on the meaning of the 10 dimensions: they were provided to allow the judges to rate the quality of each questionnaire. Based on these ratings, the judges were also asked to arrive at an overall quality rating for each questionnaire (using a 0–10 scale).

Reliability scores for the three constructs

<table><tr><td>Construct</td><td>Factor loading range</td><td>AVEa</td><td>Cronbach&#x27;s alpha</td></tr><tr><td>Initial domain knowledge</td><td>0.92–0.97</td><td>0.89</td><td>0.97</td></tr><tr><td>Domain knowledge (at conclusion)</td><td>0.95–0.97</td><td>0.93</td><td>0.98</td></tr><tr><td>Interview readiness</td><td>0.93–0.96</td><td>0.89</td><td>0.96</td></tr></table>

<sup>a</sup> AVE = average variance explained.

![](/api/attachments/RVDPF5YK/fulltext/images/becac2b356a3c8ddc318729b19e62d2e75b03a56f234ca14fb9a06db3e3be351.jpg)  
Fig. 9. The estimated KBCR assessment model.

To train the judges, the researchers used 2 questionnaires from the pilot study and walked the judges through the rating process, asking them how they would rate each of the 10 dimensions for quality as well as the overall questionnaire quality. Then, they were asked to rate the remaining questionnaires from the pilot study on their own over the next two weeks. In a second session, the judge’s ratings were compared and differences reconciled. Next, the judges were given a 3-week period to rate the 34 questionnaires used in the study. The raters did not know whether the participant had access to the KBCR or not. While judges rated each of the 10 dimensions for every questionnaire, only the overall quality rating was used in the analysis. The 10 dimensions provided a uniform basis for the judges to rate the overall quality of questionnaires. Doing so made the overall quality ratings comparable across the two judges and made it possible to reconcile differences in an objective fashion.

After the researchers received the judges’ ratings, the absolute differences between them for quality were computed. A third session with the judges was used to reconcile the ratings in cases where differences exceeded 2 points (on the 0–10 scale). During this exercise, judges discussed the differences and came to a consensus in the presence of the researchers. Interrater reliabilities were computed for ratings prior to and after reconciling differences. These reliability values for judges’ initial ratings for quality was 0.87. Only two quality ratings (out of 34) needed reconciliation. Inter-rater reliability for judges’ reconciled ratings was 0.90. The average of ratings by the two judges (after the reconciliation) was used in the analysis.

Regression analysis was used to test the model. Fig. 9 shows the results of the data analysis. When testing hypotheses H –H , analysts’ initial domain knowledge was included as a control variable. Results revealed that access to the KBCR significantly enhanced analyst’s (post-study) knowledge of the domain, providing support for H (path coefficient = 0.43, p = 0.02). The high value of the R<sup>2</sup> indicates that access to the KBCR explained 76% of the variability in the analyst’s domain knowledge. Hypotheses H was used to test the mediating effects of analysts’ (post-study) domain knowledge on their readiness for the user interview. Results revealed that (post-study) domain knowledge mediated the relationship between access to the KBCR and analysts’ interview readiness (path coefficient = 0.40, p = 0.02), supporting H . Furthermore, access to the KBCR directly impacted quality (path coefficient = 1.34, p = 0.03) of the questionnaire, thus lending support for H<sub>3</sub>.

## 5. Discussion

The objective of our study was to present a knowledge-based component/service repository to assist analysts during the RA process. Results supported our central premise that access to the knowledge-base enhanced analyst’s knowledge of the domain. Since domain knowledge holds the key to success in RA, this was a significant finding.

Interviewing is one of the most common approaches to identifying requirements. As the first step in this exercise, the analyst constructs a set of questions that would be subsequently posed to the user during the interview. Hence, knowledge of the domain plays a key role in an analyst’s ability to generate interview questions. However, because of the lack of an easy way to acquire domain knowledge, the interview has been used by the analyst to get a better understanding of the domain. This did not allow the analyst to focus on the identification of user requirements. Here, we showed how component/service repositories could be enhanced to store and provide domain knowledge. As a result, analysts were able to focus on identifying user requirements instead of trying to learn about the domain while interviewing users for their needs.

The KBCR embodied domain knowledge that provides relevant background information to analysts, thus aiding them to prepare for user interviews. Compared to those without access to the KBCR, analysts constructed a better interview questionnaire.

## 6. Managerial implications, and limitations

IT project managers, especially those who regularly undertake multiple projects in the same domain, could implement our KBCR design method to facilitate component reuse and to assist their analysts during the RA process. Access to the KBCR could improve analysts’ domain knowledge, a key ingredient for their success in RA. Moreover, access to the KBCR had a direct impact on analysts’ performance in terms of quality of the interview questionnaire.

Besides utilizing the KBCR for RA, it could also be used to train novice analysts. With greater availability of KBCRs and their reusable artifacts, novice analysts could garner a better understanding of the domain as they engage in RA. Moreover, when the same analysts engaged in the subsequent design stage, they could expect a smoother transition from RA to design as they were already aware of the intricacies of the application domain and its necessary components. However, it should be noted that these knowledge bases and components could reflect any biases or limitations of those who built them.

There are several limitations in our study. The sample size was relatively small and the experimental study employed students as proxies for seasoned analysts. Moreover, there might be some bias with respect to the self-reported (post-study) domain knowledge. Finally, there might be anchoring and adjustment (A&A) when analysts compose interview questions after using the KBCR. A&A postulates that when people are given a problem and an initial reference point (i.e., an anchor), they start with that point and make adjustments to it to reach the solution [2,8]. In fact, analysts may determine requirements based on what is in a repository rather than what is really needed. Repositories should be used by analysts as a support tool to gain a better understanding of the domain and to assist them in formulating questions for interviews and should not be perceived as a replacement for careful and detailed RA.

## Acknowledgments

The authors thank Information & Management Editor-in-Chief Edgar Sibley and the review team for guidance through the review process. This research was partly funded by grants from the Earl V. Snyder Innovation Management Center at the Whitman School of Management, Syracuse University. The authors would also like to thank the multinational consulting company for their support during this research.

## Appendix 1. Survey instruments

## Domain knowledge

A 0 to 100 continuous scale ranging from very low to very high

## I characterize

1. My understanding of the various aspects of the insurance claim handling as

2. My understanding of what insurance claim handling involves as

3. My grasp of the key issues relevant to the insurance claim handling as

4. My expertise in the insurance claim handling as

5. My ability to answer questions in the insurance claim handling as

## Interview readiness

A 0 to 100 continuous scale ranging from very low to very high

With respect to my forthcoming interview, I rate

1. My confidence in being prepared for interviewing the users as

2. My understanding of what to ask the users as

3. My ability to successfully interview the users about their requirements as

4. The level of my comfort in interviewing the users could be characterized as

## Appendix 2. Experimental task

Participants were informed of their role in the requirements analysis research study, creation of user interview question list, and its subsequent role in interviewing users. Their role was to act as analysts. As part of a requirements analysis exercise, they were asked to generate a user interview questionnaire for a new computer system for auto insurance claim handling. The questions in the questionnaire were to be subsequently used for interviewing users to identify requirements. Requirements here refer to the features desired by the users of the new system. The system needs to include all relevant capabilities from customer’s initial submission of the claim to the insurance company to final claim resolution between the insurance company and the customer. Specifically, they were informed that the new system must support following overarching features:

\- claim investigation,

\- claim assessment,

\- claim settlement,

\- injury treatment,

\- claim subrogation—the process by which one insurance compa ny seeks reimbursement from another company or person for a claim it has already paid,

\- salvage processing—bid for or sell the salvage items, such as a car, that are involved in the claim,

\- claim dispute—if parties cannot agree on the financial settlement, the arbitration process will be initiated.

To accomplish this task, analysts were asked to complete the following steps in the given sequence.

1. Register at the research website using analyst’s father’s and mother’s first name and his/her initials.

2. Complete the first set of surveys.

At this time, analysts were randomly chosen and given access to a knowledge base (KB) repository.

3. Generate a questionnaire for your interview with the user of the new system for auto insurance claim handling.

To assist analysts in developing interview questions, they were offered the following set of sample questions for a hypothetical ‘‘student registration’’ system:

(a) At most, how many times would a student register for courses in a given year?

(b) What information would a student need before he/she is able to register for a particular course (e.g., are there any prerequisites for a particular course)?

(c) Are particular students (e.g., seniors) allowed to register before others (e.g., juniors)?

(d) Would something prevent a student from registering for a particular course? If so, what?

4. Upload the questionnaire to the website and complete a set of surveys.

## References

[1] M.I. Aguirre-Urreta, G.M. Marakas, Comparing conceptual modeling techniques: a critical review of the EER vs. OO empirical literature, The DATABASE for Advances in Information Systems 39 (2), 2008, pp. 9–32.

[2] G. Allen, J. Parsons, Is query reuse potentially harmful? Anchoring and adjustment in adapting existing database queries Information Systems Research 21 (1), 2010, pp. 56–77.

[3] A. Burton-Jones, P.N. Meso, Conceptualizing systems for understanding: an empirical test of decomposition principles in object-oriented analysis, Informa tion Systems Research 17 (1), 2006, pp. 38–60.

[4] J. Coughlan, R.D. Macredie, Effective communication in requirements elicitation: a comparison of methodologies, Requirements Engineering 7, 2002, pp. 47–60.

[5] J.S. Hsu, C. Chan, J. Liu, H. Chen, The impacts of user review on software responsiveness: moderating requirements uncertainty, Information & Manage ment 45, 2008, pp. 203–210.

[6] C.K. Lee, Analysis of skill requirements for systems analysts in Fortune 500 organizations, Journal of Computer Information Systems 45 (4), 2005, pp. 84–92.

[7] T. Lin, C. Huang, Understanding knowledge management system usage antecedents: an integration of social cognitive theory and task technology fit, Information & Management 45, 2008, pp. 410–417.

[8] J. Parsons, C. Saunders, Cognitive heuristics in software engineering: applying and extending anchoring and adjustment to artifact reuse, IEEE Transactions on Software Engineering 30 (12), 2004, pp. 873–888.

[9] E. Rubin, Y. Wand, A framework supporting the utilization of domain knowledge embedded in software, Twenty-Sixth International Conference on Conceptual Modeling, vol. 83, Auckland, NZ, 2007, pp. 85–90.

[10] P. Vitharana, H. Jain, F.M. Zahedi, Strategy-based design of reusable business components, IEEE Transactions on Systems, Man, and Cybernetics 34 (4), 2004, pp. 460–474.

[11] P. Vitharana, F.M. Zahedi, H. Jain, Knowledge based repository scheme for storing and retrieving business components: a theoretical design and an empirical analysis, IEEE Transactions on Software Engineering 29 (7), 2003, pp. 649–664.

![](/api/attachments/RVDPF5YK/fulltext/images/c5b7ce1a33c0903fca3f3e17c469c49d461559ebf3e1be15c103e0e770fe4bea.jpg)

Padmal Vitharana is an associate professor of information systems in the Whitman School of Management at Syracuse University. He received his Ph.D. from the University of Wisconsin – Milwaukee. His research expertise and interests lie in component/ service-based development, systems analysis and design, and software quality management. His research has been published in leading journals such as the IEEE Transactions on Software Engineering, IEEE Transactions on Systems Man and Cybernetics Journal of MIS, Marketing Science, Communications of the ACM, Database for Advances in Information

Systems, Communications of the AIS, Information Resource Management Journal, and Information & Management. He serves as an associate editor of Commu nications of AIS. He recently served as one of the guest editors for the Special Issue on Architecture & Design for Application Agility in the Information Technology and Management.

![](/api/attachments/RVDPF5YK/fulltext/images/54af04db3c66bbbc9a2b3d7c20f356ab2a7c6eedf358179858910c501aa971a1.jpg)

Hemant Jain is TCS Wisconsin Distinguished at University of Wisconsin – Milwaukee. Dr. Jain specializes in information system agility through web services, service oriented architecture and component based development real time enterprises and health care informatics He has published in leading journals including Information Systems Research, MIS Quarterly, IEEE Transactions on Software Engineering, Journal of MIS, IEEE Transactions on Systems Man and Cybernetics, Naval Research Quarterly, Decision Sciences, Decision Support Systems, Communications of ACM, and Information & Management. He served as Associate Editor-in-Chief of IEEF

Transactions on Services Computing and is Associate Editor of Journal of AIS. He received his Ph.D. in information system from Lehigh University, an M.Tech. form IIT Kharagpur and B.E. from University of Indore.

![](/api/attachments/RVDPF5YK/fulltext/images/bfb501f7d37517f81c9fdb915da475a64332806ee52a8d308cdea73a2556d0d9.jpg)

Dr. Fatemeh ‘‘Mariam’’ Zahedi is a professor and Roger L. Fitzsimonds Distinguished Scholar at the Sheldon B. Lubar School of Business, University of Wisconsin – Milwaukee and MIS Quarterly Senior Editor 2009- present. She was appointed as Wisconsin Distinguished Professor in 1997–2007. She has received her doctoral degree from Indiana University. Her present areas of research include web design issues including IS design intelligent interface, personalization and trust, loyalty, DSS, and policy and decision analysis. She has published more than 100 papers in major refereed journals, refereed proceedings and refereed books chapters. Her journal publications include: Information Systems Research, Management Science Journal of MIS, MIS Quarterly, Information & Management, Decision Support Systems, IEEE Transactions on Software Engineering, IEEE Transactions on Systems, Man, and Cybernetics, DATABASE, Decision Sciences, Organizational Computing and E-Commerce, Communications of the ACM, IEEE Transactions on Professional Communications, IIE Transactions, European Journal of Operations Research, Operations Research, Computers and Operations Research, Journal of Review of Economics and Statistics, Empirical Economics; Socio-Economic Planning Sciences, Interfaces, and others. She is the author of two books in Quality Information Systems and Intelligent Systems for Business: Expert Systems with Neural Network. She has received several of awards for her teaching quality and research publications.
