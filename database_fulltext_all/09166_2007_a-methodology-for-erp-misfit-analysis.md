---
otero_id: 9166
otero_key: "352G9CSM"
title: "A methodology for ERP misfit analysis"
authors: "Jen-Her Wu; Shin-Shing Shin; Michael S.H. Heng"
year: "2007"
journal: "Information & Management"
doi: "10.1016/j.im.2007.09.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A methodology for ERP misfit analysis

Jen-Her Wu <sup>a,\*</sup>, Shin-Shing Shin <sup>b,1</sup>, Michael S.H. Heng

<sup>a</sup> Department of Information Management, National Sun Yat-Sen University, 70 Lien-Hai Road, Kaohsiung 804, Taiwan <sup>b</sup> Department of Information Science and Management Systems, National Taitung University, 684 Sec. 1, Chung-Hua Road, Taitung 950, Taiwan <sup>c</sup> National University of Singapore, Singapore

Received 2 June 2006; received in revised form 28 November 2006; accepted 1 September 2007 Available online 24 October 2007

## Abstract

Commercial off-the-shelf ERP systems have been adopted by many large companies to support their inter- and intra-business processes. Midsize market firms are now also investing their use. However, research has indicated that about three quarters of attempted ERP projects are unsuccessful: a common problem encountered in adopting ERP software has been the issue of fit or alignment.

This paper presents an ERP selection methodology, grounded in task-technology fits theory, for measuring, at a high-level, the misfit between ERP candidates and the enterprise’s requirements ex-ante implementation. With this approach, organizations can more easily and systematically determine the locations of possible misfit and their degree of importance, thereby understanding the risk in their implementing an ERP. Our research thus contributes practical solutions to the problem of misfit analysis and ERP package selection.

<sup>#</sup> 2007 Elsevier B.V. All rights reserved.

Keywords: ERP; COTS; Goal misfit; Functional misfit; Data misfit; Output misfit; ERP selection

## 1. Introduction

Today, companies are seeking competitive advantages through the use of COTS systems, such as ERP, rather than building systems in-house in an attempt to reduce operating costs, increase productivity, and improve customer services [26,46]. According to Gartner research, new license revenue for ERP will reach a compound annual growth rate of 6.3% by 2009 [7].

An ERP package is a large COTS configurable system that integrates several business functions. A typical ERP package may combine inventory data with financial, sales and human resource data, allowing organizations to price products, produce financial statements, and manage human, material and financial resources [27,43]. ERP software costs millions of dollars, several times as much to implement, and often requires disruptive organizational changes to implement [39,48].

ERP system implementation is complex, involving technology innovation and change management and it has been estimated that about three quarters are unsuccessful [16,30]. A common problem results from misfits: the gaps between the functions offered by ERP and the adopting organization’s requirements [15,22,31]. The misfit types can be clustered into four categories: goal, functional, data and output. Better understanding of these provides insight into ERP selection decisions and thus reduces the risk of project failure [17].

While few authors have investigated the nature of ERP misalignment [40,47], there are even fewer that have provided empirically grounded heuristics and insights into ERP selection. Therefore, the aim of our research was to present an ERP selection methodology that addressed goal, functional, data, and output misfits for use in an organizational environment. The validity and value of the proposed method were demonstrated using a case study.

## 2. COTS system development process and ERP selection

## 2.1. The COTS system development process

The COTS development process is different from traditional software development and presents many challenges. The main differences occur in the requirement definition, COTS selection, high-level design, integration, and testing phases. Among these differences, poor product selection results in some of the blame for failure; an example provided by Maiden and Ncube [24] illustrated this while suggesting that COTS selection was a key decision that impacted all subsequent phases and overall project success. Indeed, they proposed an iterative COTS-based software development process that included direction, requirement, system design, system integration and evaluation phases. The direction phase determined the high-level process objectives. The requirement phase acquired models and validated functional and nonfunctional requirements. The system design phase specified the functional and physical architectures and defined the hardware and software design to meet the requirements. The system integration phase involved product acquisition, prototype integration and integration testing. The integrated system was then to be evaluated against risk and cost criteria. However, little attention was paid to user requirement analysis and systematic support in guiding the selection process.

## 2.2. ERP selection

Several approaches, e.g., from a financial, sociotechnical or functional perspective, have been developed to help select software packages [6,9,43]. Table 1 illustrates these approaches. The financial perspective is based on cost savings and quantifiable implementation benefits. Evaluation methods include Net-Present-Value, Cost–Benefit Analysis, Payback, Return on Investment, etc. [1,13,42]. This approach expresses everything in monetary terms. If the present cash inflow value exceeds the present cash outflow value, including initial capital investment, there will be a positive net present value and, thus, acceptance of the investment. However, in ERP selection, it may not be possible to express everything in dollar figures. Further, ERP implementation is fraught with complementary investments that are intangible and difficult to measure [3].

A number of researchers have shown that normal accounting-oriented, cost–benefit analysis is unable to evaluate IT/IS effectively [8,20]. There is now a belief that the financial perspective does not provide a sufficiently good evaluation of the potential and costs of an ERP system. The critical challenge of ERP implementation is mutual adaptation between the IT and the social organization [18]. Serafeimidis and Smithson [37] argued that the evaluations would be improved by using a perspective that included content, context, and evaluation processes. They broadened the scope of conventional evaluation methods to include the context in which the evaluation took place and the process by which the evaluation was performed.

With respect to the functional perspective, the fitness of the system to the task is the major concern when selecting an IT/IS. The TTF theory, defined by Goodhue and Thompson [11], provided a theoretical basis for performing ex-ante matching of the ERP system functionalities with the business task requirements. Based on this, a close correspondence between ERP package functions and task requirements leads to positive user evaluation and positive performance impact [10]. TTF posits that IS will be used if, and only if, the functions available to the users fit their activities Palvia and Chervany [28] pointed out the need for a fit between the tasks, technologies, and users in the implementation.

Previous research of ERP selection approach

<table><tr><td>Perspective</td><td>Feature</td><td>Method</td></tr><tr><td>Financial</td><td>Evaluate the ERP based on direct cost savings and quantifiable software implementation benefits</td><td>1. Cost-Benefit Analysis [43]2. Net-Present-Value [2]3. Pay-back-period [33]4. Return on Investment [1]5. Internal Rate of Return [1]6. Accounting Rate of Return [42]</td></tr><tr><td>Socio-technical</td><td>Consider ERP systems as complex social and political entities. Evaluate the system based on content, context and evaluation processes factors.</td><td>1. Hughes and Jones [19]2. Kefi [21]</td></tr><tr><td>Functional</td><td>Evaluate the ERP based on the package functions and task requirements</td><td>1. Map [31]2. Accelerated SAP (ASAP) [5]</td></tr></table>

Thus, the four misfit categories arise from incompatibilities between:

\- the ERP package soft and rigid capabilities and the users’ goals and requirements.

\- requirements and the ERP package’s functional processing capabilities.

\- requirements and the ERP package in terms of data format or the relationships among the entities of the underlying data model.

\- requirements and the ERP package in terms of presentation format and output information content.

From a TTF standpoint, the ERP selection methodology involves the fit between the enterprise requirements and ERP provided functions. Therefore, we focus on the requirement phase of the software development process. This entails requirement modeling and misfit matching. The requirement modeling consists of four information levels: goal, scenario, design, and issue [14]. The later two deal with behavior and can be combined a single level termed activity. Therefore, based on TTF and Holbrook, we present an ERP requirement modeling architecture that consists of three levels, as shown in Fig. 1. The enterprise area represents the area or areas in which the firm intends to implement the ERP system (e.g., procurement, production, and customer service). The scenario level defines all interactions within the enterprise area; e.g., the procurement area includes scenarios such as internal procurement and stock material procurement. Every scenario is accomplished through a process flow made up of activities and their connections. For instance, internal procurement may consist of purchase requisition, purchasing, goods receipt and so on. Activity is collected in a repository and one activity can be used in different scenarios. For example, a purchase requisition can be used in both internal procurement and stock material procurement, which belong to the procurement area.

![](/api/attachments/352G9CSM/fulltext/images/499ff1cbb3b01d0560488859ba16a5a35373b95d41284a2efc41db5ab33dbb62.jpg)  
Fig. 1. COTS-based software development process.

## 2.2.1. The enterprise area level

The enterprise area level contains goals that are accomplished using scenarios at the next level. The main work at this level is therefore to identify the firm’s goals. A goal-oriented approach has been found useful in software requirements engineering [35]. It is useful in aligning system functions with enterprise goals by removing unnecessary details and focusing attention on those goals that must be achieved and the strategies needed to achieve them. An approach to achieve this was proposed by Rolland and Prakash. It uses a map notion to represent ERP goals/strategies and to thus to measure the gap between the organization’s goals and the implicit goals of the ERP package. However, it is not easy for domain experts to deal with such fuzzy goal concept [32]. In some projects, a vague goal statement makes it difficult to evaluate the process [29]. In addition, enterprise goals seldom reveal the actual situation but instead represent an idealized environment. Hence, enterprise goal seeking is not an easy task. Additionally, a language mismatch often exists between ERP experts and organization stakeholders: generally, ERP experts focus on the functions and modules while stakeholders concentrate their attention on enterprise goals.

## 2.2.2. The scenario and activity levels

Scenario and activity levels provide a conceptual link between the enterprise and subsequence system design. This scenario contains procedures for achieving enterprise area goals. Stakeholders use it to represent the enterprise and how it performs. For an ERP vendor, this shows how the system design can accomplish the objectives of the enterprise. It thus bridges the gap between the enterprise and system design by deciding what features of the ERP would be needed and how the enterprise requirements can be satisfied by it. In essence, this is a behavioral specification that captures how the system reacts to its environment [45].

The requirements will thus provide a way to discriminate between different software packages [25]. Scenarios and activities are used in the selection process and support effective goal matching. While selecting ERP software, it is necessary to be flexible in identifying the critical requirements [41]. It is important to appraise critical requirements in detail at the scenario and activity levels. To do so, the evaluation process can be divided into three levels: enterprise, scenario and activity. Only critical requirements that have been matched need to be examined in detail at the next level.

Much research has addressed the enterprise (goal misfit) and system design level [12]. Surprisingly, research at the scenario and activity level is sparse. The requirements should be determined in sufficient detail to allow effective selection. However, many software developers do not want to spend time acquiring and modeling requirements. We developed an ERP selection approach that is convenient to use with an output that can be reused in the subsequent implementation phase.

## 3. Modeling tools

The tools for acquiring the enterprise, scenario, and activity level requirements are goal-based use case, activity diagram, drawing and data glossary, respectively. A scenario has a corresponding procedure that contains three elements: activity, condition, and connection. Activity is a description of a work component that forms a step in a scenario. Condition is an element that determines the execution sequence for activities within a scenario. A connection bridges two activities and indicates the flow direction within the scenario. The activity diagram is used to model the activity flow controlled by conditions and connections. A drawing represents the input and output visual layout of an activity. The data glossary is used to describe the activity data information. Once the enterprise model has been built using a goal-based use-case diagram, the corresponding scenario can be represented by an activity diagram. The detailed information of an activity is depicted using a drawing and the data glossary.

## 3.1. Goal-based use case

The use case is valuable in goal modeling. A goalbased use-case approach was proposed as a way to extend the use-case approach [23]. It concentrates on why the ERP system is constructed and provides a way to analyze the gaps at the goal level. This focuses on how to structure and elicit the firm’s requirements using a three-step approach: (1) identify actors, (2) identify goals, (3) build the goal-based use-case model.

The goal-based use-case approach classifies goals into two facets: soft and rigid goals. A rigid goal is a target system’s minimum requirement; it must be completely satisfied. A soft goal can be partially satisfied; it describes a desirable property. If a rigid goal is not satisfied by an ERP, any soft goal becomes meaningless. It has been found that the use case enforces use-oriented decomposition of the requirement analysis from the beginning [44]. Therefore, at the start of the ERP selection phase this approach is appropriate for describing the match between enterprise and ERP package goals.

## 3.2. Activity diagram

An activity diagram represented using UML is commonly used today in modeling business process flow [34]. It includes several elements: Activity, Start Activity, End Activity, Transition, Fork, Branch, Merge, and Join. The first three elements encompass the activity. The fourth element represents the connection. Merge and Join represent the precondition. Fork and Branch represent the postcondition. Although the activity diagram can easily represent a scenario, it cannot effectively represent detailed input and output information for each activity. Therefore, to support this, other tools must be added.

## 3.3. Drawing and data glossary

A drawing is a way of effectively expressing input and output information, such as the title, presentation position, lines, figures, and tables; these are widely used in systems analysis and design. However, a drawing cannot express information such as the data length, type, format, formula, rule, range, and limits, which are important for data and output misfit identification. Hence, for each drawing, a data glossary is used to express the detailed information.

One data glossary record format might contain the Data\_type, Origin\_type, Source\_field, and Computing\_rules that describe the data fields that make up an activity. Five major Data types and six Origin\_types are shown in Table 2 [4]. The Origin\_type indicates the types of source values for each data field. For example, Computation-Triggered (‘C’) means that the data field is computed from one or more data fields. Its computing expression is stored in a Computing\_rule. If the origin type of data field is ‘A’, ‘V’ or ‘AV’, its origin will be recorded in the Source\_field.

Table 2  
Major data types and origin types

<table><tr><td>Data_type</td><td colspan="2">Meaning</td></tr><tr><td colspan="3">Five major data types</td></tr><tr><td>CH(n)</td><td colspan="2">Character string of length n</td></tr><tr><td>CHV(n)</td><td colspan="2">Character string of variable length, where n is the maximum length of the string</td></tr><tr><td>NUM(n)</td><td colspan="2">An integer, where n is the number of digits</td></tr><tr><td>NUM(m).NUM(n)</td><td colspan="2">A number with decimal point, where m and n denote the number of digits before and after decimal point, respectively</td></tr><tr><td>DATE(mm/dd/yyyy)</td><td colspan="2">Date type record the particular date, where mm, dd and yyyy represent the month, day and year of the date, respectively</td></tr><tr><td>Origin_type</td><td>Symbol</td><td>Meaning</td></tr><tr><td colspan="3">Six major origin types</td></tr><tr><td>User-Triggered</td><td>U</td><td>User enters value</td></tr><tr><td>System-Triggered</td><td>S</td><td>System enters values without referencing any value in current activity</td></tr><tr><td>Computation-Triggered</td><td>C</td><td>Value is computed from one or more fields in current activity</td></tr><tr><td>Activity-Triggered</td><td>A</td><td>Value is identically transferred from another activity</td></tr><tr><td>Value-Triggered</td><td>V</td><td>Value displayed because of a value of a field in current activity</td></tr><tr><td>Activity-Value-Triggered</td><td>AV</td><td>Value displayed because of a value of a field in another activity</td></tr></table>

## 4. ERP system selection methodology

The selection process consists of three phases: goal, functional, and data/output misfit matching, as shown in Fig. 2.

## 4.1. Goal misfit matching

Goal misfit matching consists of two steps. In the first step, a goal-based use-case models the goals in the enterprise against the capabilities if the candidates. In the second, the firm in conjunction with the vendor analyzes the output for each rigid goal. If this rigid goal is not matched, a misfit exists, but if the rigid goal is matched, soft goal matching will be performed and a goal matching report generated. Based on this, both the firm and vendor know the location of the goal misfits, and thus whether the firm’s minimum requirements are achieved and how many desired soft goals are satisfied.

## 4.2. Functional misfit matching

Next, functional misfit matching (at the scenario level) is performed. This consists of scenario modeling and matching appraisal.

## 4.2.1. Scenario modeling

Scenario modeling involves the comparison of required business process flow and the capabilities of the best practice candidate using the activity diagram, drawing, and data glossary for further requirement mapping and gap analysis. All activities at the scenario level are identified and then all input and output information for each activity is defined using a drawing and the data glossary. Once this is completed, there are two separate sets of scenarios representing the firm requirement and most likely candidate capabilities.

## 4.2.2. Scenario matching appraisal

The scenario matching appraisal is intended to show where the misfits lie based on the scenario modeling results.

4.2.2.1. Activity correspondence identification. This first step of the appraisal identifies the activity provided by the candidate system based on the firm’s activity for each scenario. The comparison is performed by finding out how and what activity the firm needs and matching them with capabilities of the candidate ERP. This is a semi-structured process that involves intensive domain knowledge. We assume that the matching is either perfect (equal) or different. Algorithms have been generated to detect semantically similarity or identical usage; however, a training program is needed; this can be given by a consultant.

4.2.2.2. Scenario matrix model generation. This step transforms the activity diagram into a scenario matrix that simplifies the matching complexity [38]. The two activity diagrams that represent firm’s requirement and the best candidate capabilities are transformed into two scenario matrices. The scenario matching can then be done performed. The scenario matrix is adopted from the adjacent matrix in graph theory to show the relative similarity in scenario matching. The scenario matrix has with rows and columns labeled by activity, except for the last column and row represented by FB (the Fork and Branch postconditions) and MJ (the Merge and Join preconditions), respectively.

![](/api/attachments/352G9CSM/fulltext/images/5a020249302fd56f4c36c4d3149d5512546f561fb7abcfa0c7316268c0414950.jpg)  
Fig. 2. Methodology for ERP selection.

Each cell is labeled; e.g., $( a _ { i } , ~ a _ { j } ) = 1$ if $a _ { i }$ has a connection pointing to $a _ { j } .$ . Otherwise, the cell is blank or

0. Similarly, each cell $( a _ { i } , \mathrm { F B } ) = 1$ , if the postcondition of $a _ { i }$ is Fork, otherwise it is 0 (the Branch condition). When an activity has only one succeeding activity, its postcondition can be regarded as a Branch. Similarly, for each cell (MJ, $a _ { j } ) = 0$ , if the precondition is Merge, otherwise it is represented by 1 (the Join condition). When an activity has only one predecessor activity, its precondition can be regarded as Merge (represented by 0). In addition, the postcondition of an end activity or the precondition of a start activity within a scenario is labeled ‘5’. The algorithm that automatically transforms a scenario into a scenario matrix model is:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: A scenario
Output: A scenario matrix
Begin
(1) Initialize an  $(n + 1) \times (n + 1)$  matrix, where n is the number of activities in the scenario
(2) Enter the first n rows using all the activities and the last row with MJ
(3) Enter the first n columns using all of the activities in the same sequence with the first n rows and label the last column with FB
(4) For each activity  $a_{i}$  within this scenario
(4.1) IF activity  $a_{i}$  has a connection pointing to  $a_{j}$, THEN fill cells  $(a_{i}, a_{j})$  with 1, OTHERWISE fill with 0
(4.2) IF the postcondition of activity  $a_{i}$  is Fork, THEN fill cells  $(a_{i}, FB)$  with 1
(4.3) IF the postcondition of activity  $a_{i}$  is Branch, THEN fill cells  $(a_{i}, FB)$  with 0
(4.4) IF activity  $a_{i}$  has only one succeeding activity, THEN fill cells  $(a_{i}, FB)$  with 0
(4.5) IF the precondition of activity  $a_{i}$  is Merge, THEN fill cells  $(MJ, a_{i})$  with 0
(4.6) IF the precondition of activity  $a_{i}$  is Join, THEN fill cells  $(MJ, a_{i})$  with 1
(4.7) IF activity  $a_{i}$  has only one predecessor activity, THEN fill cells  $(MJ, a_{i})$  with 0
(4.8) IF activity  $a_{i}$  is the end activity, THEN fill cells  $(a_{i}, FB)$  with 5
(4.9) IF activity  $a_{i}$  is the start activity, THEN fill cells  $(MJ, a_{i})$  with 5
Repeat this process until all activities have been examined
End
</div>

4.2.2.3. Scenario matching. This step identifies the connection and condition misfits. The function, MisFit $( \mathrm { P _ { F } P _ { E } } )$ , is used to find them. This information helps a firm and its vendor to understand the functional misfit between their processes. The detailed description is given in Appendix A.

## Definition.

$$
\operatorname{MisFit} \left(\mathrm{P} _ {\mathrm{F}}, \mathrm{P} _ {\mathrm{E}}\right) = \mathrm{M} ^ {*} \left(\mathrm{P} _ {\mathrm{F}}\right) - \mathrm{M} ^ {*} \left(\mathrm{P} _ {\mathrm{E}}\right) = \left[ \mathrm{MP} _ {i j} \right] _ {\mathrm{mxm}}\tag{1}
$$

where $\mathbf { M } ^ { * } ( \mathbf { P } _ { \mathrm { F } } )$ and $\mathrm { { \cal M } ^ { * } ( P _ { E } ) }$ are scenario matrix models of scenarios $\mathrm { P _ { F } }$ and $\mathrm { P _ { E } }$ and m is the number of activities in the union of $\mathrm { P _ { F } }$ and $\mathrm { P _ { E } }$ plus 1.

## 4.3. Data/output misfit matching

Data and output misfits occur at the activity level. Fig. 2 depicts the misfit identification process, which has two sub-steps.

## 4.3.1. Output misfit analysis

This step identifies and analyses the field correspondence (output misfits) and data glossary in two substeps: field correspondence identification and Data\_type and Origin\_type analyses.

4.3.1.1. Field correspondence identification. This step is used to check whether each data field needed by the firm exists in the corresponding activity of the candidate. If it does not exist, we mark it as an output misfit.

4.3.1.2. Data\_type and Origin\_type analysis. This step determines the Data\_type and Origin\_type fields for each activity and records it in the data glossary. This provides a basis for identifying the Data\_type and Origin\_type data misfit. The algorithm is:

```csv
Output misfit analysis
Input: Corresponding activity couples
Output: 1. Correspondence field couples
2. Field misfits (output misfit)
3. Data glossary for each required and target activity
Begin
(1) For each activity couple in the scenario sequence
(1.1) For each field in the required activity
(1.1.1) Find the target field that carries the same information as that of the required field
(1.1.1.1) IF there is a corresponding target field, THEN mark the required field and target field as corresponding ones
(1.1.1.2) OTHERWISE IF there is no such target field, THEN mark the gap as an output misfit
(2) For each activity couple in the scenario sequence
(2.1) Analyze the Data_type of each field in the activity
(2.2) Fill Data_type of each field into data glossary
(2.3) Analyze the Origin_type of each field in the activity
(2.3.1) Determine the Origin_type
(2.3.2) IF the Origin_type is ‘A’, ‘V’ or ‘AV’, THEN determine its Source_field
(2.3.3) IF the Origin_type is ‘C’, THEN analyze its Computing_rule
(2.4) Fill Origin_type, Source_field, and Computing_rule into the data glossary
End of output misfit analysis
```

## 4.3.2. Data misfit analysis

This step identifies the data misfit for each activity, including Data\_and Origin\_type misfits. It has of four sub-steps: activity selection, field selection, Data\_type misfit analysis (data misfit), and Origin\_type misfit analysis (data misfit).

4.3.2.1. Field selection. Here, a decision is made of which field in the activity should be analyzed first. This is normally the most independent ones, i.e. those that have no relations with others. This entails selection of the $\mathbf { \hat { U } } ^ { \dag }$ (User-Triggered) and $\mathbf { \partial } ^ { \ast } \mathbf { S } ^ { \ast }$ (System-Triggered) fields because they are independent of others.

Next, the secondary independent fields are selected from those with a relationship with the independent fields using them to analyze data misfits. That is, the ‘A (Activity-Triggered) and ‘AV’ (Activity-Value-Triggered) fields. Finally the ‘V’ (Value-Triggered) and ‘C’ (Computation-Triggered) fields are analyzed.

4.3.2.2. Data\_type misfit analysis. The data type format misfit (data misfit) is next examined by comparing the data glossaries for the activities. The five data types are clustered into three categories: Character [CH(n) or CHV(n)] Number [NUM(N) or NUM(m)], and Date [DATE(mm/dd/yyyy)]. Different data category is not compatible with other data type. Therefore, when the date’s field category is mismatched, it is marked as a format misfit (data misfit).

4.3.2.3. Origin\_type misfit analysis. This is found by comparing the data glossaries of the activities.

Let R denote the required field and T the target field and Rs and Ts the source fields of R and T, respectively. There are three possibilities:

\- If the Origin\_type of R is ‘U’ or ‘S’, then there are no misfits in the source field, since the R and T values do not depend on other fields.

\- If the Origin\_type of R is ‘A’, ‘V’ or ‘AV’, then we it is necessary to analyze whether Rs and Ts are in corresponding fields. If Rs and Ts are not, then there is a format misfit in Origin\_type. If Rs and Ts are in corresponding fields and there is a format misfit in Origin\_type between Rs and Ts, there is a format misfit in Origin\_type between R and T also.

\- If R’s Origin\_type is ‘C’, we check whether the computing rules of R and Tare the same. If the rules are not the same, then obviously there is a format misfit.

The algorithm is:

Data misfit analysis Input: 1. Corresponding activities and field correspondence pairs 2. Data glossary for each corresponding activity couple Output: Data misfits in Data\_type and Origin\_type Begin For each firm’s activity that has corresponding target activity in the scenario sequence For each required fields (1) Field selection: From the unanalyzed required fields that have corresponding target fields in the selected activity (1.1) IF there are fields with Origin\_type ‘U’ or ‘S’, THEN select one arbitrarily (1.2) ELSE IF there are fields with Origin\_type ‘A’ or ‘AV’, THEN select one arbitrarily

(1.3) ELSE select one of the fields with Origin\_type ‘V’ or ‘C’ arbitrarily

(2) Data\_type misfit analysis: IF there is data type misfit between selected field and corresponding target fields, THEN mark it as a format misfit (data type)

(3) Origin\_type misfit analysis: IF there is an origin type misfit between the selected field and corresponding target fields, THEN mark it as a format misfit (origin type)

End of Data misfit analysis

## 5. Case study

The Athletics Equipment Industry Corporation (AEIC) is a medium-sized enterprise with about 600 employees in 3 countries and an annual turnover of US\$ 28 million, having about 95 parts suppliers, 35 customers and 4 production plants in Taiwan and Mainland China. Its main products included baseball bats, bicycle frames, golf balls, and golf clubs. Ninety percent of the operations consisted of OEM/ODM for a famous Japanese company. In order to increase the efficiency of its operations, AEIC decided to adopt an ERP system. However, it was not easy to select an appropriate one.

To implement the system, AECI formed a special group, the ERP Project Team consisting of top management, MIS staffs, and key-users. The users were selected from operating departments and were intimately familiar with business processes, and had domain knowledge of their areas. They helped to determine the user requirement, select the appropriate vendor and act with them and the implementation contractor (or consultants) in completing the requirements definition and implementation phases. Finally, once the ERP system had been implemented, the keyusers trained the end-users.

Using the methodology we developed, AEIC input their requirements as criteria to determine the match of the potential ERP with their needs. Before evaluating each ERP, they kept in close contact with consultants, joining a short training course to understand the specific ERP functions and the terms used by each vendor.

The SAP was chosen and successfully implemented within a year. We used SAP R/3 and AEIC to illustrate the application value and the usability of our methodology. The team first appraised the enterprise area (goal misfit), and then the scenario (functional misfit) of the matched rigid and soft goals in the enterprise. Finally, they appraised the activity (data and output misfit). The more detailed the matching performed, the better the ERP fit they achieved but the greater the resources consumed.

## 5.1. SAP packages and modules

ERP implementation is a complex exercise in change management. However, it is a strategy that may shorten the time-to-production, increase the quality of the design, and raise the success rate of project implementation.

The SAP R/3 system currently has over 1000 predefined processes that provide financial, logistics, and human resource modules in a repository [36]. SAP classifies its packages into three types: Baseline, Industry and Cross-Industry. Baseline package provides the general solutions used in most industries. The special requirements are dealt with by Industry and Cross-Industry packages. In our study, we used the SAP Best Practice J49: Procurement of Stock Material in Baseline Package (U.S.) V2.5 released in August 2005 (http:// help.sap.com) as the comparison target. It provided a preconfigured procurement module to help a company realize e-business benefits faster and less expensively.

## 5.2. Goal misfit matching

According to the requirement document produced by AEIC, the goal-based use cases were built by the ERP project team for each enterprise area (such as procurement, production, and customer service). For simplicity, we adopted procurement business for stock material (needed by AEIC) as an example to demonstrate our methodology. Its goal-based use case contained eight use cases, four rigid goals and two soft goals, as depicted in Fig. 3. After reviewing the diagram and discussing them with consultants, the ERP project team felt that all functions were satisfied by SAP except that of application approval. SAP provided various approval functions, but it did not provide the parallel approval required by AEIC. Therefore, there was a goal misfit.

## 5.3. Functional misfit matching

## 5.3.1. Scenario modeling

The procurement scenario required by AEIC and the equivalent SAP scenario (J49: Procurement of Stock Materials) were modeled using activity diagrams, drawing and a data glossary as shown in Fig. 4. Both the scenarios contained the business flow with external organization or internal division information. For external organizations, the major job of the ERP system was to integrate with internal business processes. The functions that linked other firms were supported by other systems, such as supply chain management. Therefore, in the scenario modeling phase, it was reasonable to eliminate the external organization information. For internal divisions, SAP R/3 could assign functions to every division dynamically, even though the divisional information had not been included in the scenario modeling. Once the scenario model was constructed, the scenario matching appraisal could be performed.

![](/api/attachments/352G9CSM/fulltext/images/ebcd10f466ab603ceba523cc05e02121fc9010f4a45ae6ece0cbc28ef1237aee.jpg)  
Fig. 3. The goal-based use cases of AEIC’s procurement business for stock materials.

AEIC's procurement scenario $( \mathrm { P _ { F } } )$  
![](/api/attachments/352G9CSM/fulltext/images/76cd64be492058c39423bff2fdb241966c5cad6355132ba9008f0426ab35adbe.jpg)  
Fig. 4. Procurement scenarios of AEIC and SAP.

## 5.3.2. Scenario matching appraisal

5.3.2.1. Activity correspondence identification. Next, the team could identify the activity correspondence between $\mathrm { P _ { F } }$ (AEIC’s process) and $\mathrm { P _ { E } }$ (the ERP package process). The matching was based on how and which activity AEIC needed and then identifying the corresponding activities in SAP. This comparison was semi-structured and involved domain knowledge.

In summary, seven pairs of activities were found to be identical. These activities were ‘Create Purchase Requisition’, ‘Create Request for Quotation’, ‘Maintain Quotation’, ‘Compare Price’, ‘Update Info Record’, ‘Create Purchase Order’ and ‘Receive Goods’. The ‘Negotiate Price’ was not found in SAP R/3. This identification step appeared simple and trivial, but it was necessary and useful to identify and store the mapping for reuse in a large system.

5.3.2.2. Scenario matrix model generation. Once completed, the two scenarios could be further transformed into scenario matrices including the activity, condition, and connection information. $\mathrm { P _ { F } }$ and $\mathrm { P _ { E } }$ were transformed into scenario matrices and represented as $\mathbf { M } ^ { * } ( \mathrm { P _ { F } } )$ and $\mathbf { M } ^ { * } ( \mathrm { P _ { E } } )$ , respectively.

5.3.2.3. Scenario matching. After the scenario matrices for both the AEIC and SAP candidate had been constructed, the appraisal function was triggered to calculate the condition and connection misfit by function $\mathbf { M i s F i t ( P _ { F } , P _ { E } ) }$ The connection misfits included: ‘Create Purchase Requisition’ ! ‘Create Request for Quotation’, ‘Compare Price’ ! ‘Negotiate ‘Negotiate Price’, ‘Negotiate Price’ ! ‘Update Info Record’ and ‘Update Info Record’ ! ‘Create Purchase Order’. There were no postcondition and precondition misfits.

After the functional misfit had been determined, we continued to analyze the reason for the misfit. We found two connection misfits, ‘Negotiate Price ! Update Info Record’ and ‘Compare Price ! Negotiate Price’. Obviously, these two resulted from the activity misfit, ‘Negotiate Price’. The other two connection misfits were ‘Create Purchase Requisition’ ! ‘Create Request for Quotation’ and ‘Update Info Record’ ! ‘Create Purchase Order’, but their corresponding activities were

provided by SAP R/3, which had configured the business flow. However, this did not mean that SAP R/3 failed to handle the condition. There were four possible situations: (1) fail, (2) BPR, (3) add-on, (4) reconfiguration. The first implied that SAP R/3 could not provide the scenario required by the firm which could then not adopt R/3. The second situation meant that SAP R/3 could provide the scenario and the firm decided to perform BPR and adopt the SAP scenario. The third situation meant that SAP did not provide the function, but that the firm decided in spite of this to adopt SAP R/3. In this situation, the firm could achieve the function by add-on. However, from the experience we gained from applying our method and learning from the SAP consultant, an add-on was often applied to a new report and additional data field, but seldom to a scenario, because scenario flow control is complicated and whenever the SAP R/3 system was updated, the added on scenario had to be examined and possibly changed back to the original setting, or realtered to make it compatible. The adopting firm could therefore waste time checking the add-on function and this might be performed incompletely. In the fourth situation, SAP R/3 could be reconfigured to satisfy the firm’s demand. In our case study, after discussing with the consultant, SAP R/3 could provide the scenario. The misfit was due to the SAP pre-configuration.

![](/api/attachments/352G9CSM/fulltext/images/91342dbf6cf98416299cdd6d62f0e9f1fbbd3539db7d45ef8e1ea2aa27fa5a2d.jpg)  
AEIC's Create Purchase Order' (A\_PO)

## 5.4. Data and output misfits matching

## 5.4.1. Output misfit analysis

For simplicity, we considered the data and output misfits using two sequential activities: ‘Create Purchase Order’ (A\_PO) and ‘Receive Goods’ (A\_GR) (see Fig. 5). The drawing (S\_PO, transaction code ME21N) of ‘Create Purchase Order’ provided by SAP was located at the menu, Logistics ! Materials Management ! Purchasing ! Purchase Order ! Create ! Vendor/ Supplying Plant Known in SAP R/3. The corresponding drawing (S\_GR, transaction code MIGO) of ‘Receive Goods’ provided by SAP was located at the menu, Logistics ! Materials Management ! Purchasing ! Purchase Order ! Follow-On Functions ! Goods Receipt in SAP R/3.

![](/api/attachments/352G9CSM/fulltext/images/c6db32eab70ccd309a4d94a1b7683c18c15e4162d26f53a652703f208b2c3871.jpg)

![](/api/attachments/352G9CSM/fulltext/images/4218064801715b046bf77e45bb5a1fe71a59e39720d4ef6ad0ad29990cc2ec1e.jpg)  
SAP's ‘Create Purchase Order' (S\_PO)

AEIC's Receive Goods' (A\_GR)  
![](/api/attachments/352G9CSM/fulltext/images/ed524441e07d22f75ed0bb40068eabe393468115348355775165dcaeff69da69.jpg)  
SAP's 'Receive Goods' (S\_GR)  
Fig. 5. The drawings of ‘Create Purchase Order’ and ‘Receive Goods’.

We analyzed the field correspondence first. There were 21 and 16 fields in AEIC’s ‘Create Purchase Order’ and ‘Receive Goods’, respectively. The partial fields provided by SAP included 20 and 12 fields. Thus, there were five required fields, A\_PO:PurchaseO\_ DeliveryDate, A\_GR:Receive\_TestType, A\_GR:A\_ Receive\_InvoiceDelay, A\_GR:A\_Receive\_InvoiceDelayReason and A\_GR:A\_Receive\_Forfeit, that had no corresponding fields. We found these to be field misfits (output misfit).

## 5.4.2. Data misfit analysis

Before the data misfit analysis of the data glossaries was performed, the compatibility of the data types in our methodology had to be compared with those in SAP. This step measured the data misfit. We first analyzed these fields whose Data\_type were ‘U’ or ‘S’. There were three format misfits and one origin misfit. The origin type of A\_PO:PurchaseO\_ItemNo was ‘S’, meaning that the value was generated by the system and could not be edited by the user. AEIC did not allow the purchase order item number to be edited by the user. However, the corresponding field’s origin type was ‘U’ in SAP R/3, which did not provide such a function. AEIC decide to include this function by an add-on.

After analyzing the ‘U’ and ‘S’ type fields, we analyzed the ‘A’ or ‘AV’ type fields in AEIC. There were six pairs of ‘A’ or ‘AV’ fields. No misfit existed in the ‘A or ‘AV’ type field. We finally analyzed the misfit of ‘V’ or ‘C’ type fields. There were four pairs of corresponding fields with ‘V’ or ‘C’ type. There was no misfit.

The overall misfit results are summarized in Table 3. This provides a good starting point for a manager to determine whether an ERP candidate is suitable or not for his or her firm. Based on these results, AEIC could consider factors, such as the firm’s core business processes, finance, human resource, project schedule, etc. in order to make an appropriate selection among ERP candidates.

The misfit analysis summary between AEIC and SAP best practice

<table><tr><td>Misfits</td><td>Solution/explanation</td></tr><tr><td>Goal misfits</td><td></td></tr><tr><td>The soft goal, application approval, was satisfied to a degree, because SAP R/3 did not provide the parallel application approval.</td><td>Fit/all rigid goals had been achieved, i.e. the SAP Best Practice satisfied the minimal requirement of AEIC. It was worth doing the following comparison and determined the solution to parallel application approval.</td></tr><tr><td>Functional misfits</td><td></td></tr><tr><td>1. Activity misfit: Negotiate Price</td><td>Reconfiguration/reconfiguring SAP Best Practice to satisfy AEIC&#x27;s requirement</td></tr><tr><td>2. Connection misfits: ‘Create Purchase Requisition’ → ‘Create Request for Quotation’ ‘Compare Price’ → ‘Negotiate Price’ ‘Negotiate Price’ → ‘Update Info Record’ ‘Update Info Record’ → ‘Create Purchase Order’</td><td>Reconfiguration/reconfiguring SAP Best Practice to satisfy AEIC&#x27;s requirement</td></tr><tr><td>Output misfit</td><td></td></tr><tr><td>1. A_PO:PurchaseO_DeliveryDate</td><td>BPR/AEIC agreed with consultant&#x27;s suggestion and used the default function provided by SAP R/3</td></tr><tr><td>2. A_GR:Receive_TestType</td><td>BPR/AEIC agreed with consultant&#x27;s suggestion and referred to the information in the master data about materials provided by SAP R/3</td></tr><tr><td>3. A_GR:Receive_InvoiceDelay</td><td>Add-on/AEIC asked vendor to include this function by add-on</td></tr><tr><td>4. A_GR:Receive_InvoiceDelayReason</td><td>Add-on/AEIC asked vendor to include this function by add-on</td></tr><tr><td>5. A_GR:Receive_Forfeit</td><td>Add-on/AEIC asked vendor to include this function by add-on. Forfeit = Purchase price *Forfeit rate *Delay time</td></tr><tr><td>Data misfit</td><td></td></tr><tr><td>1. A_PO:PurchaseO_Staff</td><td>BPR/AEIC agreed with consultant&#x27;s suggestion and used the default data type provided by SAP R/3</td></tr><tr><td>2. A_PO:PurchaseO_ItemNo</td><td>Add-on/AEIC ask vendor to achieve this function by add-on</td></tr><tr><td>3. A_PO:PurchaseO_UnitPrice</td><td>BPR/AEIC agreed with consultant&#x27;s suggestion, because the default data type in SAP R/3 could satisfy their requirement according to the purchase orders over the years</td></tr><tr><td>4. A_GR:Receive_Status</td><td>BPR/AEIC agreed with consultant&#x27;s suggestion, because the status information is enough</td></tr></table>

## 6. Conclusion

The paper has presented an approach for identifying goal (enterprise level), functional (scenario level), data, and output misfits (activity level) in ERP selection. A case study has also been implemented to demonstrate the feasibility of the method. Although selecting an ERP is complex, our approach helps in selecting a suitable ERP system and shows advantages.

## Appendix A. Evaluation function

The contribution of the paper is threefold. First, it provides a systematic method that reduces the difficulty and complexity in identifying goals, functional, data, and output misfits. It integrates several concepts and models into the process to facilitate misfit identification. Second, the method with modeling tools (e.g., UML, drawing) provides a conceptual link between the enterprise requirement and subsequence system design and allows a form’s IT professionals and users and its consultants discuss on the requirement at different levels of details. This also provides a way to its convenient use with an output that can be reused in the subsequent implementation phase.

## Acknowledgements

The authors thank Edward Yang and his SAP team. Mr. Yang is a certified consultant with SAP and the vice general manager at InfoFab Inc., a SAP implementation firm. Without their cooperation and full support, this investigation could not have been undertaken. This research was supported by the National Science Council of Taiwan under grant #NSC 93-2416-H-110-015 and #NSC 95-2221-E-276-001 and was partially supported by Aim for the Top University Plan of National Sun Yat-Sen University and the Ministry of Education, Taiwan.

$\mathbf { M i s F i t ( P _ { F } , P _ { E } ) }$ : Identifying where the connection and condition misfits lie, as follows.

Definition. MisFit $( \mathrm { P _ { F } , P _ { E } } ) = \mathbf { M } ^ { * } ( \mathrm { P _ { F } } ) - \mathbf { M } ^ { * } ( \mathrm { P _ { E } } ) = [ \mathbf { M } -$ $[ \mathrm { M P } _ { i j } ] _ { \mathrm { m x m } } ,$ where $\mathbf { M } ^ { * } ( \mathrm { P _ { F } } )$ and $\mathbf { M } ^ { * } ( \mathrm { P _ { E } } )$ are scenario matrix models of $\mathrm { P _ { F } }$ (Firm’s process) and $\mathrm { P _ { E } }$ (ERP package’s process), and m is the number of activities in the union of $\mathrm { P _ { F } }$ and $\mathrm { P _ { E } }$ plus 1, and satisfies:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\mathrm{MP}_{ij} = \left\{ \begin{array}{ll}\text{Connection (except last column/row)} : &amp; \\ 1, &amp; \mathrm{P_F}\text{ has a connection from the ith process group to jth one, but } \mathrm{P_E}\text{ hasn't.}\\ 0, &amp; \text{Both } \mathrm{P_F}\text{ and } \mathrm{P_E}\text{ has a connection from the ith process group to jth one.}\\ -1, &amp; \mathrm{P_F}\text{ hasn't a connection from the ith process group to jth one, but } \mathrm{P_E}\text{ has.}\\ \text{Postcondition - Fork/Branch (last column)} : &amp; \\ 0, &amp; \text{The ith process group in both } \mathrm{P_F}\text{ and } \mathrm{P_E}\text{ has the same postcondition.}\\ \text{Other,} &amp; \text{The post condition of the ith process group in } \mathrm{P_F}\text{ and } \mathrm{P_E}\text{ are different.}\\ \text{Precondition - Merge/Join (last row)} : &amp; \\ 0, &amp; \text{The jth process group in both } \mathrm{P_F}\text{ and } \mathrm{P_E}\text{ has the same precondition.}\\ \text{Other,} &amp; \text{The precondition of the jth process group in } \mathrm{P_F}\text{ and } \mathrm{P_E}\text{ are different.} \end{array} \right\}$
</div>

The mismatch result between $\mathrm { P _ { F } }$ and $\mathrm { P _ { E } }$ is divided into three parts, i.e., connection, postcondition and precondition. In the connection part, if the matrix element $V _ { i j }$ in $\mathbf { M i s F i t ( P _ { F } , P _ { E } ) }$ is 1, it means that $\mathrm { P _ { F } }$ has a connection from activity $a _ { i }$ to $a _ { j } ,$ but $\mathrm { P _ { E } }$ does not. That is a mismatch connection. In the postcondition part, elements $\cdot _ { 0 } \cdot \mathrm { \ }$ mean that activity in $\mathrm { P _ { F } }$ and $\mathrm { P _ { E } }$ has the same postcondition; ‘Other’ means that activity in $\mathrm { P _ { F } }$ and $\mathrm { P _ { E } }$ has different postcondition. Similarly, elements $\cdot _ { 0 } \cdot \mathrm { ~ }$ in the precondition means that activity in $\mathrm { P _ { F } }$ and $\mathrm { P _ { E } }$ has the same precondition. ‘Other’ means that the $\mathrm { P _ { F } }$ and $\mathrm { P _ { E } }$ activity has a different precondition.

## References

[1] C.J. Bacon, The use of decision criteria in selecting information systems/technology investments, MIS Quarterly 16 (3), 1992, pp. 335–353.

[2] J. Ballantine, S. Stray, Financial appraisal and the IS/IT investment decision making process, Journal of Information Technology 13 (1), 1998, pp. 3–14.

[3] E. Brynjolfsson, The IT Productivity Gap, Optimize, July 21, 2003, http://ebusiness.mit.edu/erik/Optimize/pr\_roi.html.

[4] J. Coobineth, M.V. Mannino, V.P. Tseng, A form-based approach for database analysis and a design, Communications of the ACM 35 (2), 1992, pp. 108–120.

[5] M. Daneva, Lessons learnt from five years of experience in ERP requirements engineering, in: Proceedings of the 11th IEEE

International Requirements Engineering Conference, Monterey, CA, 2003, pp. 45–54.

[6] M.T. Dishaw, D.M. Strong, Extending the technology acceptance model with task–technology fit constructs, Information & Management 36 (1), 1999, pp. 9–21.

[7] C. Eschinger, Forecast: ERP Software, Worldwide 2005–2009 Update (Executive Summary), Gartner, October 24, 2005.

[8] B. Farbey, F. Land, D. Targett, Evaluating investments in IT, Journal of information Technology 7 (2), 1992, pp. 109–122.

[9] X. Franch, J.P. Carvallo, Using quality models in software package selection, IEEE Software 20 (1), 2003, pp. 34–41.

[10] D.L. Goodhue, Development and measurement validity of a task-technology fit instrument for user evaluations of information systems, Decision Sciences 29 (1), 1998, pp. 105–138.

[11] D.L. Goodhue, R.L. Thompson, Task-technology fit and individual performance, MIS Quarterly 19 (2), 1995, pp. 213–236.

[12] J.A. Hernandez, SAP R/3 Implementation Guide, McGraw-Hill, New York, 1999.

[13] B. Hochstrasser, Justifying IT investments, in: Proceedings of the Advanced Information Systems Conference, The New Technologies in Today’s Business Environment, 1992, pp. 17–28.

[14] C.H. Holbrook, A scenario-based methodology for conducting requirements elicitation, ACM SIGSOFT Software Engineering Notes 15 (1), 1990, pp. 95–104.

[15] C.W. Holsapple, M.P. Sena, The decision-support characteristics of ERP systems, International Journal of Human–Computer Interaction 16 (1), 2003, pp. 101–123.

[16] C.W. Holsapple, M.P. Sena, ERP plans and decision-support benefits, Decision Support Systems 38 (4), 2005, pp. 575–590.

[17] C.W. Holsapple, Y.M. Wang, J.H. Wu, Empirically testing user characteristics and fitness factors in enterprise resource planning success, International Journal of Human–Computer Interaction 19 (3), 2005, pp. 323–342.

[18] K.K. Hong, Y.G. Kim, The critical success factors for ERP implementation: an organizational fit perspective, Information & Management 40 (1), 2002, pp. 25–40.

[19] J. Hughes, S. Jones, Reflections on the use of grounded theory in interpretive information systems research, Electronic Journal of Information Systems Evaluation 6 (1), 2004.

[20] Z. Irani, Information systems evaluation: navigating through the problem domain, Information & Management 40 (1), 2002, pp. 11–24.

[21] H. Kefi, IS/IT evaluation: a context-based and process-oriented perspective, Electronic Journal of Information Systems Evaluation 6 (1), 2004.

[22] D. Kunda, L. Brooks, Identifying and classifying processes (traditional and soft factors) that support COTS component, European Journal of Information Systems 9 (4), 2000, pp. 226–234.

[23] J. Lee, N.L. Xue, Analyzing user requirements by use cases: a goal-driven approach, IEEE Software 16 (4), 1999, pp. 92–101.

[24] N.A.M. Maiden, C. Ncube, Acquiring COTS software selection requirements, IEEE Software 15 (2), 1998, pp. 46–56.

[25] N.A.M. Maiden, C. Ncube, A. Moore, Lessons learned during requirements acquisition for COTS systems, Communications of the ACM 40 (12), 1997, pp. 21–25.

[26] P. Mandal, A. Gunasekaran, Issues in implementing ERP: a case study, European Journal of Operational Research 146 (2), 2003, pp. 274–283.

[27] M.L. Markus, C. Tanis, P.C.V. Fenema, Enterprise resource planning: multisite ERP implementations, Communications of the ACM 43 (4), 2000, pp. 42–46.

[28] S.C. Palvia, N.L. Chervany, An experimental investigation of factors influencing predicted success in DSS implementation, Information & Management 29 (1), 1995, pp. 43–53.

[29] C. Potts, K. Takahashi, A.I. Anton, Inquiry-based requirements analysis, IEEE Software 11 (2), 1994, pp. 21–32.

[30] S.S. Rao, Enterprise resource planning: business needs and technologies, Industrial Management & Data Systems 100 (2), 2000, pp. 81–88.

[31] C. Rolland, N. Prakash, Bridging the gap between organizational needs and ERP functionality, Requirements Engineering 5 (3), 2000, pp. 180–193.

[32] C. Rolland, C. Souveyet, C.B. Achour, Guiding goal modeling using scenarios, IEEE Transactions on Software Engineering 24 (12), 1998, pp. 1055–1071.

[33] P.G. Sassone, W.A. Schaffer, Cost Benefit Analysis, Academic Press, New York, 1978.

[34] T.P. Schambach, K.A. Walstrom, Systems development practices: Circa 2001, Journal of Computer Information Systems 43 (2), 2002–2003, pp. 87–92.

[35] A.W. Scheer, F. Habermann, Enterprise resource planning: making ERP a success, Communications of the ACM 43 (4), 2000, pp. 57–61.

[36] J.E. Scott, L. Kaindl, Enhancing functionality in an enterprise software package, Information & Management 37 (3), 2000, pp. 111–122.

[37] V. Serafeimidis, S. Smithson, Information systems evaluation in practice: a case study of organizational change, Journal of Information Technology 15 (2), 2000, pp. 93–106.

[38] H.A. Simon, The Sciences of the Artificial, 3rd ed., The MIT press, Cambridge, Massachusetts, 1996, pp. 208–210.

[39] C. Soh, S.S. Kien, J. Tay-yap, Enterprise resource planning: cultural fits and misfits: is ERP a universal solution? Communications of the ACM 43 (4), 2000, pp. 47–51.

[40] C. Soh, S.K. Sia, W.F. Boh, M. Tang, Misalignments in ERP implementation: a dialectic perspective, International Journal of Human–Computer Interaction 16 (1), 2003, pp. 81–101.

[41] I. Sommerville, Integrated requirements engineering: a tutorial, IEEE Software 22 (1), 2005, pp. 16–23.

[42] C.J. Stefanou, A framework for the ex-ante evaluation of ERP software, European Journal of Information Systems 10 (4), 2001, pp. 204–215.

[43] K.Y. Tam, Capital budgeting in information systems development, Information & Management 23 (6), 1992, pp. 345– 357.

[44] K. Weidenhaupt, K. Pohl, M. Jarke, P. Haumer, Scenarios in system development: current practice, IEEE Software 15 (2), 1998, pp. 34–45.

[45] A. Wexelblat, Report on Scenario Technology. MCC Technical Report STP-139-87, Microelectronics and Computer Technology Corporation, Austin, TX, 1987.

[46] J.H. Wu, Y.M. Wang, Measuring ERP success: the key-users’ viewpoint of the ERP to produce a viable IS in the organization, Computers in Human Behavior 23 (3), 2007, pp. 1582–1596.

[47] J.H. Wu, C.T. Hsieh, S.S. Shin, C.C. Wu, A methodology for evaluating data and output misfits in commercial off-the-shelf ERP systems, Journal of Information Technology and Information Management 14 (4), 2005, pp. 27–44.

[48] J.H. Wu, Y.M. Wang, Measuring ERP success: the ultimate users view, International Journal of Operations & Production Management 26 (8), 2006, pp. 882–903.

![](/api/attachments/352G9CSM/fulltext/images/37ee1edc8f1f07699fc60f7162ee270ada8676ad16c648ec3118fea2448e7667.jpg)  
Jen-Her Wu is Professor of Information Management at National Sun Yat-Sen Uni versity. He has published two books (Sys tems Analysis and Design, Object-oriented Systems Analysis and Design) and over 50 papers in professional journals such as Information & Management, Computers in Human Behavior, Decision Support Systems, International Journal of Human–Computer Interaction, and  
others. His current research interests include information systems development and management, human–computer interaction, electro nic commerce and innovation, and knowledge management. He also serves as an associate editor of Computers in Human Behavior and on the editorial board of Information & Management.

![](/api/attachments/352G9CSM/fulltext/images/a069da4abd994412dc61b7450903b43b36080a800b6c76bd66020a667b423dbd.jpg)

Shin-Shing Shin is Assistant Professor of Information Science and Management Systems at National Taitung University. He received a Ph.D. degree in Information Management at National Sun Yat-Sen University and earned an MS degree in Elec trical Engineering at National Taiwan University. Prior to his doctoral study, he worked as a project manager in software industry for many years. His research interests include system evaluation and software

engineering. His research articles have appeared in such journals as Information & Management, Journal of International Technology and Information Management, Journal of Internet Technology, and others.

![](/api/attachments/352G9CSM/fulltext/images/2f532580745f79a10c89ca4ea7f699bcbe039ed45f61d5e4f1adf2c1b37d271c.jpg)

Michael S.H. Heng is Senior Research Fellow at East Asian Institute, National University of Singapore. He has held academic positions in Malaysia, The Netherlands, Australia, China and Singapore. He obtained his Ph.D. from the Free Univer sity of Amsterdam. His current research interests include globalization, rise of Asia, eBusiness, IS development and IS maintenance. He is the Asia Pacific Editor of the International Journal of Electronic

Customer Relationship Management and Associate Editor of the Journal of Electronic Commerce Research and Asia Pacific Journal of Management Science. He is also a co-editor of the book Supply Chain Management: Issues in the New Era of Collaboration and Competition.
