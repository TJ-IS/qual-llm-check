---
otero_id: 22435
otero_key: "9SDQEGQ3"
title: "Data management in executive information systems"
authors: "Chang E Koh; Hugh J Watson"
year: "1998"
journal: "Information & Management"
doi: "10.1016/s0378-7206(98)00035-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Data management in executive information systems

Chang E. Koh $^{a,*}$ , Hugh J. Watson $^{b}$

$^{a}$ Bryan School of Business and Economics, University of North Carolina at Greensboro, Greensboro, NC 27412-5001, USA $^{b}$ Terry College of Business, University of Georgia, Athens, GA 30602-6256, USA

Received 18 March 1997; revised 30 September 1997; accepted 18 January 1998

## Abstract

Data management is important in developing and maintaining executive information systems (EISs). An EIS can fail due to the lack of an adequate data infrastructure for this ‘data intensive’ application. From the literature, discussions with developers, consulting experiences, and eight case studies, a set of key data management issues were identified. Three – data security, ownership, and standards – were further studied, using survey data collected from 85 organizations. Canonical correlation analysis was used to investigate the relationship between these issues and potentially related variables. The breadth and depth of information provided were found to be correlated with the difficulty of the issues. The degree of support from key individuals was also found to be correlated with the level of difficulty. © 1998 Elsevier Science B.V. All rights reserved

Keywords: Executive information systems; Executive support systems; Data management

## 1. Introduction

In a relatively short time, executive information systems (EISs) have become important to many organizations. They are providing information to support high-level decision making. EISs are challenging to develop, however, because of the mix of organizational and technical issues involved. Failure rates between 40 and 70 percent are reported [22, 30]. However, when they are successful, executives believe that their company's investment in an EIS was wise [20].

There is a growing body of knowledge about what is required to develop and maintain an EIS. Effective data management is often cited as a key to success because EISs are very data intensive [4, 16]. It has been cited as the most common cause of EIS failure [8]. EIS professionals have identified ‘Making sure EIS data is accurate’ and ‘Combining data from multiple sources’ as major concerns. EIS consultants have observed that ‘More than 90 percent of our effort in the EIS systems we build goes into finding, processing, and guaranteeing the quality of the data.’

There is little in-depth information about EIS data management: the plans; rules; and practices with regard to the collection; processing; and dissemination of EIS data. Normally, it is briefly discussed as a part of case studies. We have talked with hundreds of EIS professionals about their development experiences and data management is a topic that has come up frequently. Because of this, EIS data management was targeted as a topic for study.

## 2. The research method: A multiphase process

We conducted a multiphase study in three parts: (1) literature review; (2) case studies; and (3) survey study. The purpose of the literature review was to gain insights into EIS data management issues. However, because the literature has been incomplete in its coverage, eight case studies were conducted via interviews. The firms were selected on the basis of geographic proximity, but they represent different industries and use different software. Three data management issues became the target of further investigation with data collected from 85 organizations via a questionnaire. This formal process was supplemented by anecdotal information from EIS developers and the authors' consulting experiences.

## 2.1. Phase 1: Literature review

We first identified major data management issues. They were organized into two categories – technical and managerial (see Table 1).

We also reviewed the information systems (IS) diffusion theory literature. According to this theory borrowed from social psychology, a technological or managerial innovation typically passes through a cycle of initiation, adoption, and implementation $[15, 27]$ . The theory states that organizational and environmental factors affect the way organizations diffuse an innovation. IS researchers have tried to establish a similar theoretical foundation, with the major categories including characteristics of the technology, organization structure and culture, task characteristics, etc. [2, 11].

<table><tr><td>Table 1Data management issues identified from the literature</td></tr><tr><td>Managerial issues</td></tr><tr><td>General data administration</td></tr><tr><td>Data resource management</td></tr><tr><td>Data requirements analysis</td></tr><tr><td>Corporate data planning and modeling</td></tr><tr><td>Data integrity and standards</td></tr><tr><td>Data ownership and sharing</td></tr><tr><td>Data security and access control</td></tr><tr><td>Technical issues</td></tr><tr><td>Data management software</td></tr><tr><td>Database administration</td></tr><tr><td>Data modeling and database design</td></tr><tr><td>Data storage</td></tr><tr><td>Data dictionary</td></tr><tr><td>Data security</td></tr></table>

## 2.2. Phase 2: Case studies

Next, we interviewed eight EIS managers from The University of Georgia's database of organizations known or believed to have an EIS. All companies were large; only one had revenues under \$1 billion. The industries represented were: manufacturing (4); utilities (2); government (1); and computer software (1). The EISs were relatively young (only one was older than 5 years) and support a relatively small user base (none served more than 100 users).

While most of the EISs studied were considered either a success or too early to decide, one company had concluded that their EIS was a failure and had abandoned it.

The interviews were structured. First, the EIS managers were asked about the history of their systems and to demonstrate them (except for the failed system). Next, they were asked to describe the major data management issues that surfaced while building or operating the EIS, factors that affected the issues, and approaches for handling the issues. The interviews were tape-recorded.

Most of the factors mentioned seemed to support those of the information diffusion theorists. The managerial aspects of EIS data management were generally more troublesome than the technical ones. Also many EISs had their own databases, separate from operational ones for several reasons: technical difficulty in linking the EIS directly to the source of data; differences in data definitions and reporting cycles among data sources; and concern for system performance, such as slow response time. Many organizations are aggressively developing data warehouses and data marts to support applications, such as EIS $[13, 19]$ .

## 2.3. Phase 3: Survey

From the previous investigation, it became apparent that several EIS data management issues and the factors that affect them warranted further investigation. Three issues – data security, data ownership, and data standards – were chosen, because their importance and difficulty varied from organization-to-organization. Three other factors appeared to be important: characteristics of the EIS; characteristics of key individuals involved with the system; and characteristics of the organization. A research model and hypotheses were formulated, and data were collected from 85 organizations.

## 3. Issues in EIS data management

Seven major EIS data management issues surfaced: (1) data requirements; (2) data sources; (3) data security and access control; (4) data ownership; (5) data standards; (6) data integrity; and (7) data storage and retrieval. Of these, EIS managers felt that data integrity was the most important and difficult.

## 3.1. Issue 1: Data requirements

Determining EIS requirements involves understanding the nature of executive work, their difficulties in specifying their needs, and analysts' limited understanding of executives' data requirements and limited experience in developing an EIS. Attendees of a practitioner-oriented conference on EIS said that identifying the data requirements of the system was their primary concern $[26]$ . Watson and Frolick $[28]$ identified a portfolio of methods used by companies to determine EIS data requirements. They recommend that organizations employ a combination of methods to derive data needs. Others suggest the use of computer-based collaboration tools $[10, 17]$ . One of the case studies provided an interesting insight: an EIS manager suggested that executives are willing to make time to meet with analysts, but only if the analysts are perceived as being able to deliver a system that meets their needs.

It is also important to monitor executives' changing needs; several companies built a capability to track executives' use of the EIS. They can then observe what applications the executives access, for how long, etc. Applications rarely used should be removed or modified. Furthermore, this tracking system can be used to strengthen security by detecting unusual activities.

## 3.2. Issue 2: Data sources

Organizational data often have compatibility and consistency problems. Developing an EIS uncovers many problems that have gone unnoticed $[23, 31]$ . An important EIS data source is staff personnel who already collect, process, and present information to functional area executives $[21]$ . EISs that include soft information also draw upon external sources, such as news databases, personnel who provide commentaries on the data, and networks of people both inside and outside the firm. News stories are relatively easy to provide. Explanations, assessments, judgments, and opinions can be added as text commentaries, but are labor-intensive. One company recognized the need for soft data and included the name and phone number of the person responsible for supplying the information. Some firms have used e-mail and electronic bulletin boards as a mechanism for sharing staff information.

While EIS and other vendors have made significant progress in developing ‘pipeline’ software to extract data, there still may be a need for custom developed data extraction programs. Once all data sources have been identified, the EIS staff still has to try to combine data from multiple sources and decide how to present it.

## 3.3. Issue 3: Data ownership

People and groups often feel that they ‘own’ organizational data and perceive the data as a source of organizational power. This often results in various data ownership problems.

An EIS often gets data directly from lower levels in the organization, bypassing the normal chain of command. This is potentially threatening to lower-level managers. An extreme reaction is the creation of two sets of books – one for the EIS (it reveals no problems) and the other that is an accurate set.

Some hands-on executives want operational data for mission-critical processes. We found three helpful solutions to this problem. The first is to tell senior management about the dysfunctional aspects of per-using operational data, spotting problems, and calling lower levels of the organization. Another is to ask senior executives to limit the degree of operational data that they access. The third asks data owners to review their data by using a ‘review and release’ cycle, which allows them to check the data before it is made available to the system's users.

Job descriptions can be changed to recognize the added responsibilities of supplying data to the EIS. One radical approach provided the message ‘(person’s name) has not supplied data’ when the data supplier had not provided the necessary data. The effect was dramatic. To encourage and support business analysts to supply data to the EIS, one company set up an information center and provided technical and managerial support.

## 3.4. Issue 4: Data security and access control

For many companies, security is a major consideration in the design of their EISs. One useful security measure is to have a double security system – by user password and PC. Some EIS screens may not be accessible from all PCs. This is useful, for example, in companies where the EIS can be accessed in conference rooms. It prevents the unintentional showing of privileged information. Another approach is to have sensitive information available as menu choices only for users who are authorized to view it.

Is a firm's organizational culture about data availability affected by the implementation of an EIS? It appears that it may be, with freer access being given. As one EIS manager put it, “We started out with a ‘need to know’ attitude but we have moved to a ‘why shouldn’t it be available’ approach.”

It is common for data to be intentionally excluded when they are considered to be sensitive or confidential. For example, a hospital may not include data on patient deaths caused by hospital errors $[29]$ . Strategic plans, sexual harassment charges, and executive bonuses are other probable exclusions. In general, human resources data (e.g., salaries, grievances) are closely held by many companies due to their private nature. One firm monitors the distribution of documents and rebuilds the access list every night to prevent unauthorized access.

## 3.5. Issue 5: Data standards

Some terms are used throughout an organization but with slightly different meanings. The term, ‘sign up,’ used at Lockheed–Georgia illustrates this point [12]. A sign up occurs when a customer agrees to buy a plane – a cause for celebration. Prior to the EIS, people in marketing recognized a sign up whenever a customer indicated the intent to buy a plane. In the legal department, the sign up was not recognized until there was a signed contract. Finance waited until there was a down payment.

When building an EIS, it is important to develop already agreed upon definitions for all the terms. It is even wise to create an executive data dictionary in which EIS terms are defined.

Most of the EIS managers believed that data standardization represents a large problem for several reasons: (1) increasing use of electronic data; (2) growing global trading that require data communication across national boundaries; and (3) the continuing trend of corporate restructuring.

## 3.6. Issue 6: Data integrity

Data integrity is crucial to the success of an EIS because even a minor incidence of failure to provide accurate information can lead to a fatal loss of executives' trust in the system $[1]$ . Some EIS managers believe that executives tend to be less forgiving with inaccurate data displayed on screens than those provided on paper reports. A survey conducted by International Data Corporation found 65% of the respondents choose data integrity as one of the critical success factors of an EIS $[9]$ .

## 3.7. Issue 7: Data storage and retrieval

The three major storage locations for EIS data are at the PC level, on a file server, and on a mainframe. Generally, the closer the data are to users the faster the response time, and the more reliable the system. Data proximity, however, increases the need for local storage capacity, with added costs. A common practice is to use a ‘cascading’ approach, where the location of the data depends on how frequently it is used. Regularly used data are cached at the executive’s PC and updated as required.

The cascading of data is consistent with the recommendation that organizations should create decision-support databases that are separate from operational databases $[3, 25]$ . Maintaining separate databases seems to have advantages: (1) the integrity of the system can be protected from changes in the production database; (2) it is easier to filter and add value to data by analyzing them and adding comments; and (3) it improves access time. Organizational interest is seen in the large number of firms that are building data warehouses for decision-support applications [32].

A firm must decide which database technology should be used. Multidimensional queries against relational databases, such as an SQL server, can result in unacceptable response times. The need to quickly ‘slice and dice’ the data has led EIS software vendors to include multidimensional databases in their product offerings. These products are components of on-line analytical processing (OLAP).

A major beverage company initially provided daily updates on gallons of syrup sold. A year later, it was providing updates five times a day, with plans to increase updates even more. If the data are mission-critical, there is a demand for it to be almost real-time. It is argued that an EIS which cannot handle such data demand is likely to fail $[7]$ . The most important motivation for implementing an EIS is to provide more timely access to data $[30]$ .

## 3.8. Additional observations

There were both centralized and decentralized organization structures for the EIS-support staff. While the impact of these alternatives on data management was not a focal point of our study, several possible implications appear. The centralized approach seems to facilitate an organization-wide data perspective, enhanced data security, and standard data definitions. For this reason, many EIS managers favor the centralized approach. A decentralized structure, where functional area personnel support the EIS on a part-time basis, seems to help in data requirements, reducing data ownership problems and potentially increasing the amount of soft information.

There seems to be an interesting two-way interaction between the culture of an organization, data placed in the EIS, and who has access to data. In some organizations, speculative data, such as opinions and rumors, are intentionally excluded, while other organizations encourage their inclusion. Over time, several organizations have allowed freer access to the data in the EIS, suggesting a more open organizational culture.

Multidimensional databases are either replacing or augmenting relational ones for EIS purposes. Even more recent are the efforts of some managers to include more non-numerical data, such as text and image information. Groupware software, such as Lotus Notes, is considered for this purpose. There is also considerable movement to using World Wide Web technologies.

Executives with access to an EIS often use its drilldown capabilities to access mission-critical data that are detailed, current, and accurate. Apparently what information executives need is changing, with executives being more actively engaged in operational and management control than before.

## 4. A further investigation of selected EIS data management issues

As previously stated, the survey dealt with a subset of the EIS issues – data security, data ownership, and data standards.

## 4.1. Research questions

The survey portion of the study was designed to investigate the following three research questions:

1. What is the perceived importance and difficulty of the selected data management issues?

2. What are the perceptions of the factors that potentially affect the data management issues?

3. What are the relationships between the data management issues and factors?

## 4.2. Research variables, model, and hypotheses

We developed a research model with a set of dependent and independent variables as shown in Fig. 1. Lines connecting two variables represent hypotheses postulated about relationships.

## 4.2.1. Dependent variables

The importance and difficulty of the data management issues were the two dependent variables in the study. They vary with the firm. While a company may consider a data management issue important, it may not experience much difficulty with the issue, and vice versa. Consequently, importance and difficulty were considered as two different constructs and measured separately.

![](/api/attachments/9SDQEGQ3/fulltext/images/d647ef25f8386a6eaca2d3b460debf473b2c6cbb88a44c4ee2669af5e6bee038.jpg)  
Fig. 1. The research model.

## 4.2.2. Independent variables

The three independent variables were system, individual, and organizational characteristics. For each, component characteristics were selected. Two specific system characteristics were chosen: the breadth and depth of the data. Breadth refers to the extent to which the EIS includes different types of data. For example, data can be provided by functional areas, products or services, geographical locations, and customers or suppliers. Depth refers to the level of detail of data provided. For example, corporate summary, divisional summary, and operational data reflect different levels of detail.

The development and operation of an EIS require the efforts of executives, the EIS-support staff, and data providers. An executive sponsor should champion the project, provide the necessary resources, give encouragement, and handle political resistance $[18]$ .

The sponsor and other executives should be willing to meet with the EIS-support staff to identify data requirements. The EIS-support staff is responsible for developing and maintaining the system and should have business knowledge as well as technical skills. Responsibilities include understanding the system's business objectives, promoting the EIS, managing the project, determining data requirements, working with data providers, and performing necessary technical tasks. In addition, an EIS requires a network of people throughout the organization to make data available to the system in a timely manner.

The organizational characteristics chosen for the study were the centralization and integration of IS activities as they apply to EIS data management. They have been regularly used in IS research $[6]$ . Also, the case studies suggested that centralization and integration might alleviate certain data management problems. The level of centralization assesses the extent to which IS decisions are centrally made and communicated in a firm, whereas the level of integration measures the extent to which different parts of IS are integrated.

## 4.2.3. Research model and hypothesis

We developed six research hypotheses based on the potential relationships between the dependent variables and the independent variables.

H1: There is a relationship between the breadth and depth of information provided by EIS and the importance of the data management issues.

H2: There is a relationship between the breadth and depth of information provided by EIS and the difficulty with the data management issues.

H3: There is a relationship between the support from the key individuals and the importance of the data management issues.

H4: There is a relationship between the support from the key individuals and the difficulty with the data management issues.

H5: There is a relationship between IS centralization and integration and the importance of the data management issues.

H6: There is a relationship between IS centralization and integration and the difficulty with the data management issues.

## 4.3. The survey instrument

A questionnaire asked demographic questions about the organization, its EIS, the respondent, and the data management issues and factors. Its content validity was assessed by eight EIS professionals who suggested several minor changes. Cronbach's alpha was used to insure the instrument's reliability (all items had an alpha of 0.76 or more).

The survey instrument was mailed to 300 EIS professionals drawn from The University of Georgia's EIS database. Four weeks after the initial mailing, a follow-up mailing was sent to non-respondents. Thirteen surveys were returned as being undeliverable and 21 indicated that they did not currently have an EIS. Eighty-five companies (29.5 percent) provided usable data.

## 4.4. Data analysis

## 4.4.1. Demographics

Eighty-eight percent of the responding organizations are located throughout the United States and the rest are in Canada. The most common business activities are manufacturing (32 percent); financial services (20 percent); and communications, utilities, and transportation (18 percent). Eighty-seven percent of the organizations are in the private sector. More than three-quarters have annual revenues over \$1 billion. The average age of the EIS was 35 months and the average number of users was 60. Most respondents were EIS managers or support staff members (64 percent), with an average of 18 years of work, 13 years of IS, and slightly less than 3 years of EIS experience.

## 4.4.2. Importance and difficulty of the data management issues

Two statements were provided about the importance and difficulty of each data management issue. Respondents were asked to indicate on an anchored five-point scale (1=least important; 5=most important) how important or difficult the issue was to the success of the EIS. The two responses were averaged to provide an overall measure. All three issues were rated more important than difficult (see Table 2). Of the three issues, data standards received the highest score in both importance and difficulty. While there was little difference in the importance and difficulty of the data standards and data ownership issues, data security was judged to be appreciably more important than difficult.

Table 2  
Importance and difficulty of the data management issues

<table><tr><td>Question</td><td>Importance</td><td>Difficulty</td></tr><tr><td colspan="3">Data security</td></tr><tr><td>Establishing and implementing data security procedures and standards</td><td>3.02</td><td>2.31</td></tr><tr><td>Protecting data from unauthorized access</td><td>3.36</td><td>2.21</td></tr><tr><td>Overall average</td><td>3.21</td><td>2.25</td></tr><tr><td colspan="3">Data ownership</td></tr><tr><td>Establishing and implementing effective data ownership policies</td><td>3.25</td><td>2.85</td></tr><tr><td>Resolving conflicts resulting from data ownership problems</td><td>3.01</td><td>2.98</td></tr><tr><td>Overall average</td><td>3.13</td><td>2.91</td></tr><tr><td colspan="3">Data standards</td></tr><tr><td>Establishing and implementing standard definitions for key data</td><td>3.93</td><td>3.68</td></tr><tr><td>Reconciling different data definitions used in different parts of the organization</td><td>3.83</td><td>3.99</td></tr><tr><td>Overall average</td><td>3.88</td><td>3.84</td></tr></table>

## 4.4.3. Characteristics of the EIS

The breadth and depth of the data provided were the characteristics of the EIS that were of primary interest. To investigate breadth, respondents were given four categories – data by functional area, products or services, geographical areas, and customers or suppliers – and were asked to check all that are provided by their EIS. Respondents were also given an ‘other’ choice to list any additional categories. Nearly all of the systems (95 percent) allow users to access data by functional area. Other categories are provided to a lesser degree; 60 percent of the firms provide data by product or service, 64 percent by geographical area, and 28 percent by customer or supplier. Other (15 percent) categories reported included business units or segments, projects, news and events, facilities, strategic initiatives, and market channels.

Table 3  
Breadth and depth of the data provided

<table><tr><td>Data category</td><td>Average score</td></tr><tr><td colspan="2">Breadth of data</td></tr><tr><td>By functional area</td><td>2.95</td></tr><tr><td>By product or service</td><td>3.49</td></tr><tr><td>By geographical area</td><td>3.53</td></tr><tr><td>By customer or supplier</td><td>3.29</td></tr><tr><td>By other categories</td><td>3.31</td></tr><tr><td>Overall average</td><td>3.16</td></tr><tr><td colspan="2">Depth of data</td></tr><tr><td>By functional area</td><td>2.85</td></tr><tr><td>By product or service</td><td>3.06</td></tr><tr><td>By geographical area</td><td>3.04</td></tr><tr><td>By customer or supplier</td><td>2.96</td></tr><tr><td>By other categories</td><td>3.00</td></tr><tr><td>Overall average</td><td>2.89</td></tr></table>

The level of breadth and the level of depth of data provided by an EIS were measured for each category by an anchored five-point scale (1=lowest; 5=highest). Table 3 shows average scores of breadth and depth of data for each of the five categories as well as aggregated overall averages. Firms reported that they provided data at a considerably lower level of breadth by functional area than other data categories. On the other hand, no significant differences were noticed among the data categories in the level of depth of data provided.

## 4.4.4. Characteristics of individuals

Support from executives, data providers, and the EIS staff for the system in general and data management in particular were the characteristics of interest. For each group, a set of statements was provided that indicated an important type of support. Respondents were asked to rank them using an anchored five-point scale (1=strongly disagree; 5=strongly agree). Overall, the EIS-support staff received a higher rating than executives or data providers (see Table 4). However, this finding should be interpreted with caution because the study surveyed professionals who might have biased opinions because of their positions.

Table 4

<table><tr><td>Question</td><td>Average score</td></tr><tr><td>Executives</td><td></td></tr><tr><td>Our executives are supportive by providing necessary resources for the EIS project</td><td>3.64</td></tr><tr><td>Our executives provide encouragement to the EIS staff</td><td>3.47</td></tr><tr><td>Our executives are readily available to discuss matters important to the EIS project</td><td>3.18</td></tr><tr><td>Our executive users are willing to discuss their information needs with the EIS-support staff</td><td>3.55</td></tr><tr><td>Our executives handle any political resistance to the EIS</td><td>3.00</td></tr><tr><td>Overall average</td><td>3.37</td></tr><tr><td>Data providers</td><td></td></tr><tr><td>Managers who provide data for our EIS (data providers) are willing to supply the data</td><td>3.48</td></tr><tr><td>Data providers deliver necessary data to the EIS on time</td><td>3.32</td></tr><tr><td>Data providers understand and support the objective of the EIS</td><td>3.35</td></tr><tr><td>Overall average</td><td>3.38</td></tr><tr><td>EIS staff</td><td></td></tr><tr><td>The EIS staff is successful in developing applications as planned</td><td>3.84</td></tr><tr><td>The EIS staff is successful in working with necessary technical components (e.g., hardware, software, and communication)</td><td>4.04</td></tr><tr><td>The EIS staff is aware of the benefits of the EIS</td><td>4.29</td></tr><tr><td>The EIS staff understands the business objectives served by the EIS</td><td>4.01</td></tr><tr><td>The EIS staff is effective in communicating with executive users about executives&#x27; information needs</td><td>3.52</td></tr><tr><td>The EIS staff is effective in communicating with the data providers about the need to supply data</td><td>3.69</td></tr><tr><td>Overall average</td><td>3.90</td></tr></table>

## 4.4.5. Characteristics of the organization

The two organizational characteristics of interest were the amount of centralization and integration of IS in general and data management in particular. Respondents were given a set of statements for each characteristic and asked to rank them on an anchored five-point scale (1=least centralized or integrative and 5=most centralized or integrative). The average ranking for each statement and the overall average for each characteristic are shown in Table 5. Of the two characteristics, the responding organizations rank higher on centralization than integration.

Table 5  
Amount of IS centralization and integration

<table><tr><td>Question</td><td>Average score</td></tr><tr><td colspan="2">Centralization</td></tr><tr><td>IS activities at our firm are highly centralized</td><td>3.45</td></tr><tr><td>Standard operating procedures (e.g., rules, policies, forms, etc.) have been well established and used to coordinate different IS activities</td><td>3.31</td></tr><tr><td>Most decisions regarding materials, resources, and services needed for IS operations are centrally made at the corporate level</td><td>3.35</td></tr><tr><td>Each unit within IS communicates with other IS units through formal channels (e.g., written letters, memos, and reports)</td><td>2.91</td></tr><tr><td>Overall average</td><td>3.25</td></tr><tr><td colspan="2">Integration</td></tr><tr><td>Most IS applications extensively integrate data from many different data bases</td><td>2.91</td></tr><tr><td>Most IS applications share the some corporate databases</td><td>2.66</td></tr><tr><td>Most IS applications produce output compatible to each other</td><td>2.66</td></tr><tr><td>Our organization has a corporate-wide data administration function</td><td>2.93</td></tr><tr><td>Our organization extensively utilizes a corporate-wide data dictionary</td><td>2.24</td></tr><tr><td>Overall average</td><td>2.68</td></tr></table>

## 4.4.6. Tests of the hypotheses

Canonical correlation analysis was used to test the six hypotheses. It identifies and measures the association between two sets of variables, each of which consists of several component variables [14]. For example, when used with the first hypothesis, the characteristic of the EIS includes the breadth and depth of the information provided, and the importance of the data management issues includes the importance of data security, data ownership, and data standards. Table 6 summarizes the results from the statistical analysis of the six hypotheses.

All of the canonical correlations are positive but only H2 and H4 are supported at a 0.05 level of significance. The positive sign of each canonical correlation should not be interpreted as an indication of a positive relationship. A canonical correlation identifies only the magnitude of the relationship between two sets of variables and not its direction. The results of the hypothesis tests present empirical evidence for possible connections between the data management issues and factors. The first connection exists between the level of difficulty with the data management issues and the depth and breadth of data provided in an EIS (H2) and the second between the difficulty with the issues and the level of support from the key people involved in the EIS (H4).

Additional insights were gained by investigating the relationships between the component variables of the data management variables and the factors that affect them. The results of a simple correlation analysis with the component variables are provided in Table 7, which shows all significant relations as highlighted with a superscript letter b (for p<0.01).

Other significant simple correlations are shown with a superscript letter a for a 0.05 level of significance. The most interesting significant relationships are the negative correlations between the importance

Table 6  
Summary of statistical analysis of hypotheses

<table><tr><td>Hypothesis</td><td>Independent variable set</td><td>Dependent variable set</td><td>Canonical correlation</td><td>F-square</td><td>Prob Pr</td></tr><tr><td>H1</td><td>Breadth and depth of data provided</td><td>Importance of data management issues</td><td>0.32</td><td>1.47</td><td>0.19</td></tr><tr><td>H2</td><td>Breadth and depth of data provided</td><td>Difficulty of data management issues</td><td>0.40</td><td>2.58</td><td> $0.02^a$ </td></tr><tr><td>H3</td><td>Support from key people</td><td>Importance of data management issues</td><td>0.28</td><td>1.34</td><td>0.22</td></tr><tr><td>H4</td><td>Support from key people</td><td>Difficulty of data management issues</td><td>0.38</td><td>1.95</td><td> $0.05^a$ </td></tr><tr><td>H5</td><td>IS centralization and integration</td><td>Importance of data management issues</td><td>0.16</td><td>0.48</td><td>0.82</td></tr><tr><td>H6</td><td>IS centralization and integration</td><td>Difficulty of data management issues</td><td>0.16</td><td>0.51</td><td>0.80</td></tr></table>

$^{a}$ Supported at a 0.05 level of significance.

Table 7  
Simple correlation analysis of component variables

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">System</td><td colspan="3">Individuals</td><td colspan="2">Organization</td></tr><tr><td>Breadth</td><td>Depth</td><td>Executives</td><td>Data providers</td><td>EIS staff</td><td>Centralization</td><td>Integration</td></tr><tr><td rowspan="2">System</td><td>Breadth</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Depth</td><td> $0.23^a$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">Individuals</td><td>Executives</td><td>0.16</td><td>-0.04</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Data providers</td><td>0.19</td><td>0.11</td><td> $0.34^b$ </td><td></td><td></td><td></td><td></td></tr><tr><td>EIS staff</td><td>0.09</td><td>0.01</td><td> $0.46^b$ </td><td> $0.39^b$ </td><td></td><td></td><td></td></tr><tr><td rowspan="2">Organization</td><td>Centralization</td><td>0.13</td><td>0.15</td><td> $0.34^a$ </td><td>0.19</td><td>0.19</td><td></td><td></td></tr><tr><td>Integration</td><td>0.09</td><td>0.03</td><td> $0.33^b$ </td><td>0.05</td><td>0.19</td><td> $0.57^b$ </td><td></td></tr><tr><td rowspan="3">Importance of issues</td><td>Security</td><td>-0.01</td><td>0.05</td><td>0.21</td><td>0.14</td><td>0.05</td><td>0.01</td><td>0.09</td></tr><tr><td>Ownership</td><td>-0.09</td><td> $-0.22^a$ </td><td>0.04</td><td>-0.03</td><td>0.14</td><td>-0.02</td><td>-0.04</td></tr><tr><td>Standards</td><td>0.02</td><td>0.12</td><td>0.16</td><td>0.01</td><td>0.21</td><td>0.13</td><td>0.08</td></tr><tr><td rowspan="3">Difficulty of issues</td><td>Security</td><td>-0.16</td><td>0.02</td><td>0.08</td><td>0.01</td><td> $-0.28^b$ </td><td>-0.11</td><td>-0.07</td></tr><tr><td>Ownership</td><td>-0.04</td><td> $-0.34^b$ </td><td>0.08</td><td>-0.11</td><td>0.01</td><td>-0.08</td><td>-0.05</td></tr><tr><td>Standards</td><td>0.05</td><td>0.11</td><td>0.02</td><td>-0.18</td><td>0.04</td><td>0.05</td><td>-0.09</td></tr><tr><td rowspan="2" colspan="2"></td><td colspan="3">Importance of issues</td><td colspan="4">Difficulty of issues</td></tr><tr><td>Security</td><td>Ownership</td><td>Standards</td><td>Security</td><td>Ownership</td><td>Standards</td><td></td></tr><tr><td rowspan="2">System</td><td>Breadth</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Depth</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">Individuals</td><td>Executives</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Data providers</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EIS Staff</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">Organization</td><td>Centralization</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Integration</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">Importance of issues</td><td>Security</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ownership</td><td> $0.36^b$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Standards</td><td>0.01</td><td> $0.25^a$ </td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">Difficulty of issues</td><td>Security</td><td> $0.34^b$ </td><td>0.10</td><td>-0.17</td><td></td><td></td><td></td><td></td></tr><tr><td>Ownership</td><td>0.19</td><td> $0.61^b$ </td><td>0.01</td><td>0.18</td><td></td><td></td><td></td></tr><tr><td>Standards</td><td>-0.13</td><td>0.02</td><td> $0.50^b$ </td><td>-0.15</td><td>0.13</td><td></td><td></td></tr></table>

$^{a}$ p<0.05.  
$^{b}$ p<0.01.

and difficulty of the data ownership issues and EISs that provide data at greater depth. One might expect that providing more in-depth data would increase the data ownership problems.

## 4.5. Discussion

The findings from the survey study provide several insights into EIS data management. First, of the issues studied, EIS professionals regard data standards to be the most important and difficult. While data standards are important and may be a difficult issue to manage in any application, they are particularly challenging in EIS because of the variety of data sources that cross functional boundaries and management hierarchies.

When asked to evaluate the three data management issues, the EIS professionals consistently assigned a higher score to the importance rather than the difficulty of the issues. This gap was particularly significant with data security.

The interpretation and implications of the significant relationships appear to be straightforward. The first (H2) suggests a connection between the breadth and depth of data and the level of difficulty with the data management issues and the second (H4) supports the conventional wisdom: with more support from key individuals, there are fewer data management problems $[5, 24]$ . However, we discovered an interesting but puzzling finding when we analyzed the relationships between component variables within each variable group using simple correlation analysis (see Table 7). Contrary to what might be expected, there was a negative correlation between the importance and difficulty of the data ownership issue and the depth level of data provided in the EIS. That is, as the depth level increased, the data ownership issue became less difficult. To explore this issue further, several EIS professionals who reported such an inverse relationship were contacted for their explanation. They suggested that firms may provide data in greater detail only when they feel confident in handling data ownership problems. Thus, when a company provides data at a great depth, the data ownership problems already have been resolved.

## 5. Conclusions

The quantitative findings suggest how important and difficult selected data management issues are likely to be and how selected factors affect them. Our study of EIS data management was conducted within the scope and context of today's systems. Several factors, including advances in information technology, a growing awareness of the kinds of information that can be provided, and executive demand for richer information, are pushing many EISs beyond their current, traditional contents. These changes are likely to create or modify data management issues.

## References

[1] W. Boltz, Executive information systems design, Infosystems 34(5), 1987, pp. 70.

[2] J.A. Brancheau, G.B. Davis, J.C. Wetherbe, The diffusion of end-user information technology: Conceptual model and propositions for research, Working Paper, MIS Research Center, University of Minnesota, Minneapolis, MN, 1987.

[3] M. Chen, The development of a repository-based executive information system, Journal of Management Information Systems 11(4), 1995, pp. 33–63.

[4] F. Crockett, Revitalizing executive information systems, Sloan Management Review 33(4), 1992, pp. 39–47.

[5] D.W. De Long, J.F. Rockart, Identifying the attributes of successful executive support system implementation, DSS-86 Transactions, The Institute of Management Sciences, 1986, pp. 41–54.

[6] Ein-Dor, E. Segev, Organizational context and MIS structure: Some empirical evidence, MIS Quarterly 6(3) (1982) 55–68.

[7] D. Friend, EIS: Straight to the point, Information Strategy: The Executive's Journal 4(4), 1988, pp. 25–30.

[8] D. Friend, Information navigation: Blurring the line between DSS and EIS, DSS-89 Transactions, The Institute of Decision Sciences, 1989, p. 11.

[9] D. Friend, EIS and the collapse of the information pyramid, Information Center 6, 1990, pp. 22–28.

[10] M.N. Frolick, B.P. Robichaux, EIS information requirements determination: Using a group support system to enhance the strategic business objectives method, Decision Support Systems 14(2), 1995, pp. 157–170.

[11] M.J. Ginzberg, The impact of organizational characteristics on MIS design and implementation, Working Paper, Center for Research on IS, New York University, NY, 1980.

[12] G. Houdeshel, H.J. Watson, The management information and decision support (MIDS) system at lockheed-georgia, MIS Quarterly 11(1), 1987, pp. 127–140.

[13] W. Inmon, Building the Data Warehouse, John Wiley & Sons, New York, 1992.

[14] R.A. Johnson, D.W. Wichern, Applied Multivariate Statistical Analysis, 2nd ed., Englewood Cliffs, NJ: Prentice-Hall, 1988.

[15] J.R. Kimberly, Managerial innovation in adapting organizations to their environments, in: P.C. Nystrom, W.H. Starbuck (Eds.), Handbook of Organizational Design, vol. 1, Oxford University Press, 1981.

[16] C.E. Koh, A Study On EIS Data Management Issues and Factors Affecting the Issues, Unpublished dissertation, The University of Georgia, Athens, GA, 1992.

[17] C.E. Koh, R. Herschel, Using groupware to support EIS development, International Journal of Information and Management Science 7(4), 1996, pp. 65–80.

[18] K. Overton, M.N. Frolick, R.B. Wilkes, Politics of implementing EISs, Information Systems Management 13(3), 1996, pp. 50–57.

[19] F.R. McFadden, H.J. Watson, The world of data warehousing: Issues and opportunities, Journal of Data Warehousing 1(1), 1996, pp. 61–71.

[20] J.H. Nord, G.D. Nord, Executive information systems: A

study and comparative analysis, Information and Management 29(2), 1995, pp. 95–106.

[21] A. Paller, R. Laska, The EIS Book: Information Systems for Top Managers, Homewood, IL: Dow Jones-Irwin, 1990.

[22] D. Raths, The politics of executive information systems, Infoworld 11(20), 1989, pp. 47–52.

[23] J.F. Rockart, D.W. De Long, Executive Support Systems: The Emergence of Top Management Computer Use, Homewood IL: Dow Jones-Irwin, 1988.

[24] C. Sheridan, A blueprint for developing an executive information system. Planner, Execucom Systems Corp., Austin, TX 11(3) (1989) 4–8.

[25] R.H. Sprague, H.J. Watson, Decision Support Systems: Putting Theory into Practice, 3rd ed., Englewood Cliffs, NJ: Prentice Hall, 1993.

[26] S. Stecklow, The new executive information systems, Lotus (1989) 51–53.

[27] V.A. Thomson, Bureaucracy and innovation, Administrative Science Quarterly 10(1), 1965, pp. 1–20.

[28] H.J. Watson, M.N. Frolick, Determining information requirements for an EIS, MIS Quarterly 17(3), 1993, pp. 255–269.

[29] H.J. Watson, M.T. O'Hara, C.G. Harp, G.G. Kelly, Including soft information in EISs, Information Systems Management 13(3), 1996, pp. 66–77.

[30] H.J. Watson, R.K. Rainer, C.E. Koh, Executive information systems: A framework for development and a survey of current practices, MIS Quarterly 15(1), 1991, pp. 13–30.

[31] H.J. Watson, R.T. Watson, S. Singh, D. Holmes, Development practices for executive information systems: Findings of a field study, Decision Support Systems 14(2), 1995, pp. 171–184.

[32] K. Watterson, The changing world of EIS, Byte 19(6), 1994, pp. 183–193.

![](/api/attachments/9SDQEGQ3/fulltext/images/8c906966dd448d7b71080036f6b705770a2e90cf9aa3dd171769e06d9235c356.jpg)

Chang E. Koh is a faculty member at the Department of Information Systems and Operations Management in the Bryan School of Business and Economics at the University of North Carolina at Greensboro. His current major research and consulting focus is on electronic commerce, the Internet, and end-user computing issues. He has also studied data management issues associated with the use of computers by end users,

particularly executives. His article on EIS appeared in MIS Quarterly and International Journal of Information and Management Science. He received a Ph.D. in Information Systems from the University of Georgia.

![](/api/attachments/9SDQEGQ3/fulltext/images/646b7c5ae6ee86f47b028389dc5e9f6bbe640e8c1481b4f19f7a3f54e30edcc0.jpg)

Hugh J. Watson is Professor of MIS and holds the C. Herman and Mary Virginia Terry Chair of Business Administration at The University of Georgia. His speaking, research, and consulting focus on the design of information systems to support decision making. Dr. Watson is the author of over 100 articles and 22 books, including Decision Support in the Data Warehouse, Prentice-Hall, 1998. Alan Paller, founder of the EIS institute

and the Data Warehousing Institute describes Hugh as “the nation’s (U.S.) foremost authority on EIS” and “a walking encyclopedia of what works and does not work in executive information systems.” Most recently he was a consultant on the development of a highly successful executive information system at the World Bank. His is the senior editor of the Journal of Data Warehousing and is a Fellow of The Data Warehousing Institute.
