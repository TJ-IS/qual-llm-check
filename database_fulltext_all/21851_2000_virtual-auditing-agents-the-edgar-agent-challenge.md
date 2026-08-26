---
otero_id: 21851
otero_key: "HX8KMFPU"
title: "Virtual auditing agents: the EDGAR Agent challenge"
authors: "Kay M Nelson; Alex Kogan; Rajendra P Srivastava; Miklos A Vasarhelyi; Hai Lu"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00088-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Virtual auditing agents: the EDGAR Agent challenge

Kay M. Nelson <sup>a,)</sup>, Alex Kogan <sup>b</sup>, Rajendra P. Srivastava <sup>c</sup>, Miklos A. Vasarhelyi <sup>b</sup>, Hai Lu <sup>a</sup>

<sup>a</sup> School of Accounting and Information Systems, DaÕid Eccles School of Business, The UniÕersity of Utah, Salt Lake City, UT 84112,USA <sup>b</sup> Department of Accounting and Information Systems, Faculty of Management, Rutgers UniÕersity, Newark, NJ 07102-1895,USA <sup>c</sup> Ernst and Young Center for Auditing Research and AdÕanced Technology, DiÕision of Accounting and Information Systems, School of Business, The UniÕersity of Kansas, Lawrence, KS 66045,USA

## Abstract

Intelligent agents can be used as agents of organizational change. This potential exists in the domain of accounting audit, where much of what is currently done manually in batch mode could be done continuously and on-line. We discuss the use of intelligent Internet agents as a way of changing and expanding audit practices in the virtual world. A quality<sup>r</sup>service framework is presented that suggests ways that accounting firms can evolve in this era of on-line opportunities. The EDGAR Agent is presented as an example of an intelligent Internet agent that gathers financial information. The challenges involved in the development of the EDGAR Agent are analyzed, providing insight into the practical aspects of agent technology designed for a specific business domain. A test of the agent is presented, with comments and suggestions from financial practitioners that will be integrated into the research stream. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Intelligent agent; Accounting audit; EDGAR; Agent technology

## 1. Introduction

The virtual world presents many challenges and opportunities to accounting firms. The Internet has exponentially increased the speed and availability of information to consumers. Many of these consumers are the clients of accounting firms that in some respects have previously been taken for granted. This explosion of information has resulted in many of these clients questioning the value of standard accounting services such as auditing<sup>1</sup> that provide accurate yet greatly delayed information. Organizations need to know on a real time basis how they are performing. The investors and management of these organizations would also like to have this knowledge more frequently than is currently provided by the annual audit 9 . Accounting firms that do not re-<sup>w</sup> <sup>x</sup> spond to these client needs will find themselves at a competitive disadvantage. The very existence of the virtual global environment will cause the current accounting audit model to evolve or die.

Table 1  
Requirements for virtual transactions Bhimani 3Ž <sup>w</sup> <sup>x</sup>.

<table><tr><td>Confidentiality</td><td>Communications are restricted to only the parties involved in a transaction</td></tr><tr><td>Authentication</td><td>Assurance that parties are communicating with whom they think they are doing business.</td></tr><tr><td>Data Integrity</td><td>Data sent in a transaction should not be modifiable in transit</td></tr><tr><td>Nonrepudiation</td><td>Neither party can deny participation in a transaction after the fact</td></tr><tr><td>Selective application of services</td><td>Part of a transaction is hidden from view while another part is not</td></tr></table>

Commenting on the audit function, Elliott 10 , p. <sup>w</sup> <sup>x</sup> 106 says:

The information revolution is greatly changing the attest environment, and we must try to understand the nature of the changes in order to determine how best to respond to them. These changes and prospects call for responses to adapt internal and external accounting, accounting education and research, accounting firms, and attest work.

The accounting profession is responding. Recently, the AICPA American Institute of Certified Ž Public Accountants Board has formed a Special . Committee on Assurance Services to develop a strategic plan for identifying and implementing an expanded assurance function<sup>2</sup> resulting from the information revolution 14 .<sup>w</sup> <sup>x</sup>

There is a great need for new types of services. Some of these services will be built on the core competencies that already exist and some will have to be developed. These services will be built around the demand for confidentiality, authentication, data integrity, non-repudiation, and selective application of client services that are dictated by the virtual environment of the Internet 3 . Table 1 illustrates<sup>w</sup> <sup>x</sup> these transaction needs in the virtual world.

## 2. Intelligent agents

Much of the work done in the virtual world will be done by intelligent agents. These agents can be defined as programs that operate autonomously to accomplish unique tasks without direct human supervision. Minsky and Riecken 16 has described intel-<sup>w</sup> <sup>x</sup> ligent agents in a more pragmatic way, describing them as ‘‘go-betweens’’ that possess specialized skills, similar to travel agents or insurance agents. By having intelligent agents do the more mundane and manual tasks of the audit function, the opportunity exists for auditors to become more knowledgeable about and responsive to their clients. Agents should enhance human intelligence and help to make people smarter 18 . In the case of auditors, this can<sup>w</sup> <sup>x</sup> translate to the ability to provide new and innovative services to clients that extend the practice of auditing beyond the traditional scope.

This paper addresses the issue of intelligent agency and virtual auditing by providing an example of an agent that renders a value-added service that can potentially be offered in an auditing practice. We call this program the EDGAR Agent since it searches the EDGAR Security and Exchange Commission SECŽ . database for the current 10Q report of listed companies. This paper outlines the challenges faced when developing an intelligent agent for a specific business domain, in this case, the accounting domain of financial reporting.

## 3. The auditing function in the virtual world

Traditionally, the audit function has been limited to the verification and accuracy of financial reporting in an organization. An exception to this has been the area of EDP auditing. This practice began as an additional financial reporting verification process, but in many cases has been extended to verifying the operation of computing systems in the organization. By looking at the EDP function in this way, it seems only natural to assume that the Internet would provide opportunity to extend the financial reporting verification process to provide new and hopefully profitable services to clients in the virtual world.

These new services can be classified into two general categories, quality and service 13 . Tradi-<sup>w</sup> <sup>x</sup> tionally, the practice of auditing has focused on the quality dimension. Through the verification of financial reporting<sup>3</sup>, the quality of information provided by the firm to its stakeholders is assured. This assurance is similar to a radiologist assuring that a medical X-ray is accurate and provides a quality diagnosis, or a building inspector assuring that a house is built to specifications and will hold up the roof.

While doing auditing assurance, many accounting firms have discovered the lucrative practice of business and information systems consulting. This is a natural extension of the assurance process, since business processes and information systems can directly affect the quality of organizational information <sup>w</sup> <sup>x</sup> 8 . These consulting practices focus on the service dimension. Both the quality and service dimensions can be extended under the auditing umbrella in the virtual world, as shown in Table 2.

Internet security is one of the biggest barriers to doing business electronically 5,7 . For intelligent<sup>w</sup> <sup>x</sup> agents to succeed and be accepted, auditors, their clients, and the customers and stakeholders of their clients must believe the Internet is secure. Agents need to be seen as competent and trusted 15 . If the <sup>w</sup> <sup>x</sup> transaction environment is not seen as secure, agents will not be accepted. However, the security issue can be turned into a profit opportunity for auditing practices. Auditors, and their intelligent agents, can extend the quality dimension of the audit practice to include the verification of confidentiality, authenticity, integrity, completeness, and timeliness of information found on the Internet. These security-oriented services would be an extension of the existing core competency of financial verification that already exists in audit practices. By furnishing these verification services, the providing accounting firm would also be seen as competent and trusted, and these traits would be endowed on the intelligent agent that is a proxy for the firm.

Table 2  
Virtual auditing quality<sup>r</sup>service framework

<table><tr><td>Quality</td><td>Service</td></tr><tr><td>Verification of transactions and data</td><td>Nonrepudiation of transactions</td></tr><tr><td>Authentication of transactions and data</td><td>Proxy intelligence searches</td></tr><tr><td>Integrity of transactions and data</td><td>Real time database search and reporting</td></tr><tr><td>Completeness of transactions and data</td><td>Translation to/from English</td></tr><tr><td>Timeliness of transactions and data</td><td>Competitive intelligence</td></tr></table>

Electronic commerce also provides the opportunity for many new consulting services that can be offered under the auditing practice umbrella. These services include the acceptance of agents working under the proxy of an established and trusted accounting firm, in other words, the nonrepudiation of the services or information provided by or sought after by these agents. These agents will act as intermediaries between the auditing firm and its clients, as well as a proxy for the client in the virtual world. These proxies can perform text-based searches for information within the client’s databases and within other databases on the Internet. These database search capabilities provide the opportunity for real time database reporting and updates. Intelligent agents can also provide translation capabilities to clients that may not be English speaking. Finally, agents can constantly search the virtual world to gather information that auditing practices can convert to valuable and salable client competitive knowledge.

Besides these new opportunities, even the traditional audit function will change in the Internet era, especially in terms of the nature of evidence and the way it is accumulated.<sup>4</sup> Intelligent agents will play an important role in this process 19 . For example,<sup>w</sup> <sup>x</sup> in performing analytical procedures<sup>5</sup> as required by the AICPA 1 , the auditor can use an agent to gather <sup>w</sup> <sup>x</sup> industry information through the Internet and perform the analysis irrespective of the place and time.

## 4. The EDGAR Agent

The EDGAR Agent is a first step toward on-line continuous auditing and expanding the role of the audit function in the virtual world 19 . The EDGAR<sup>w</sup> <sup>x</sup> Agent is a category of agent that assists in information access and management 2 . The EDGAR Agent <sup>w</sup> <sup>x</sup> is an easy-to-use intelligent agent that searches the SEC EDGAR database for the current cash balance of a user-specified corporation. The user then is asked to choose the industry group for the company before he<sup>r</sup>she submits the query. The agent then sends the query including the corporation and industry names to the EDGAR database server. There are three possible results to this inquiry. The first is a list of available 10-Q reports, which will be returned if the company name has been found. The second option is the case of no exact match for the company name where the agent will decide to tell the user that the company is not available and asks for another search. The third possible result is that the agent gives the user some name suggestions based on the agent’s point of view. The later outcome is designed to help users who might not know the precise company name used in SEC files.

The 10-Q reports are retrieved in filing date order. After clicking on one specific report, the user is given a form where he or she selects the balance sheet, the income statement, or the statement of cash flow. The agent then gives the option of calculating some financial ratios designed to help the user understand the performance of the company through the comparison with the industry average.

![](/api/attachments/HX8KMFPU/fulltext/images/5e7ce7c71da575c707b24fdb070d287f587e884b2d2349a419c6701ecaa7c827.jpg)  
Fig. 1. Other websites or servers.

The first number that can be calculated is the current market value of the company derived from its stock price. The agent also calculates the quick ratio, current ratio, and gross margin over sales.<sup>6</sup> Future capabilities will include calculation of the debt over equity ratio, cash collection time and inventory turnover.<sup>7</sup> The process and the demo forms of EDGAR Agent are shown in Figs. 1 and 2, respectively.

## 5. Challenges in developing the EDGAR Agent

This paper discusses three primary challenges encountered in developing the EDGAR Agent. These three challenges are the speed of the agent itself, the non-standard format of financial statements and the variety of the accounting terms used in the financial statements.

![](/api/attachments/HX8KMFPU/fulltext/images/4b25a2c5bbf57f14654838d03c902ed2de3339f5292ae801de75320f0754476f.jpg)  
Fig. 2. EDGAR search agent.

## 5.1. Speed

Perl is an excellent language to process text files for pattern matching and other built-in functions. However, because it is a scripting language, the running speed of the code is slow compared to that of C<sup>r</sup>C<sup>qq</sup> code, especially when network communication is required. We encountered this problem in the early stage of the agent development. It took several minutes to retrieve the financial statements from the EDGAR database and even more time to calculate the financial ratios. When analyses were made over the network, the speed of the agent was significantly slower due to the communication between the client and the server. With this Remote Procedure Calling RPC process, every request of Ž . the agent resulted in a corresponding response from the server. With the exception of the transfer rate over the Internet, which was beyond our control, we used several ways to improve the speed of the agent Ž . listed below .

Ž . 1 Download the releÕant information once. After the agent was successfully connected to the EDGAR database, the required reports were downloaded and saved in a local server Unix, PC, etc. . IfŽ . the user needed to compare the ratios of a specific company with those of its peer companies, the 10-Q reports of the related companies were downloaded at the same time. To further solve the conflict between the expected and practical speed, a database is currently being constructed where information will be retrieved locally if the information is not outdated.

Ž . 2 Use local computation where the Perl script looks for the reports in the local serÕer. Although the analysis is currently being made by the pure Perl code, we did test the combination of C<sup>qq</sup> and Perl code, considering that many people are the enthusiastic believers of using scripting language along with $\mathrm { C / C + + \ o r \ o r }$ Java to improve performance. In the EDGAR Agent, we found this treatment did not significantly improve speed.

Table 3  
A comparison of Intel and Ford consolidated balance sheets

<table><tr><td>Intel</td><td>Ford</td></tr><tr><td>Assets</td><td>Assets</td></tr><tr><td>Current assets</td><td>Automotive</td></tr><tr><td>Cash and cash equivalents</td><td>Cash and cash equivalents</td></tr><tr><td>Short-term investments</td><td>Marketable securities</td></tr><tr><td>Trading assets</td><td>Total cash and marketable securities</td></tr><tr><td>Accounts receivable, net</td><td>Receivables</td></tr><tr><td>Inventories</td><td>Inventories</td></tr><tr><td>Raw materials</td><td>Deferred income taxes</td></tr><tr><td>Work in process</td><td>Other current assets</td></tr><tr><td>Finished goods</td><td>Net current receivable from Financial Services</td></tr><tr><td>Deferred tax assets</td><td>Total current assets</td></tr><tr><td>Other current assets</td><td>Equity in net assets of affiliated companies</td></tr><tr><td>Total current assets</td><td>Net property</td></tr><tr><td>Property, plant and equipment</td><td>Deferred income taxes</td></tr><tr><td>Less accumulated depreciation</td><td>Other assets</td></tr><tr><td>Property, plant and equipment, net</td><td>Total Automotive assets</td></tr><tr><td>Long-term investments</td><td>Financial Services</td></tr><tr><td>Other assets</td><td>Cash and cash equivalents</td></tr><tr><td>Total assets</td><td>Investments in securities</td></tr><tr><td></td><td>Net receivables and lease investments</td></tr><tr><td></td><td>Other assets</td></tr><tr><td></td><td>Net receivable from Automotive</td></tr><tr><td></td><td>Total Financial Services assets</td></tr><tr><td></td><td>Total assets</td></tr><tr><td>Liabilities and stockholders’ equity</td><td>Liabilities and stockholders’ equity</td></tr><tr><td>Current liabilities</td><td>Automotive</td></tr><tr><td>Short-term debt</td><td>Trade payables</td></tr><tr><td>Accounts payable</td><td>Other payables</td></tr><tr><td>Deferred income on shipments to distributors</td><td>Accrued liabilities</td></tr><tr><td>Accrued compensation and benefits</td><td>Income taxes payable</td></tr><tr><td>Accrued advertising</td><td>Debt payable within one year</td></tr><tr><td>Other accrued liabilities</td><td>Net current payable to Financial Services</td></tr><tr><td>Income taxes payable</td><td>Total current liabilities</td></tr><tr><td>Total current liabilities</td><td>Long-term debt</td></tr><tr><td>Long-term debt</td><td>Other liabilities</td></tr><tr><td>Deferred tax liabilities</td><td>Deferred income taxes</td></tr><tr><td>Put warrants</td><td>Total Automotive liabilities</td></tr><tr><td>Stockholder’s equity</td><td>Financial Services</td></tr><tr><td>Preferred stock</td><td>Payables</td></tr><tr><td>Common stock and capital in excess of par value</td><td>Debt</td></tr><tr><td>Retained earnings</td><td>Deferred income taxes</td></tr><tr><td>Total stockholder’s equity</td><td>Other liabilities and deferred income</td></tr><tr><td>Total liabilities and stockholders’ equity</td><td>Net payable to Automotive</td></tr><tr><td></td><td>Total Financial Services liabilities</td></tr><tr><td></td><td>Stockholders’ equity</td></tr><tr><td></td><td>Capital stock</td></tr><tr><td></td><td>Preferred Stock</td></tr><tr><td></td><td>Common Stock</td></tr><tr><td></td><td>Class B Stock</td></tr><tr><td></td><td>Capital in excess of par value of stock</td></tr><tr><td></td><td>Liabilities and stockholders’ equityForeign currency translation adjustments and otherEarnings retained for use in businessTotal stockholders’ equityTotal liabilities and stockholders’ equity</td></tr></table>

Ž . 3 Choose a better local serÕer. The EDGAR Agent code is expected to be platform independent. Initially we worked on an IBM RS 6000<sup>r</sup>350 server where the CPU time has been widely distributed to the extensive Email users. We moved to a DEC AlphaServer 1000A 5<sup>r</sup>400 server that is used primarily for research computing, and the running speed improved as expected.

## 5.2. Format of the financial statements

There are significant differences in the financial statements between companies in the EDGAR database, even when those companies are in the same industry. These format differences directly impact the accuracy of the information returned by the EDGAR Agent. In order to illustrate the point, a simple comparison of the balance sheets of two companies, Intel and Ford Motor, is shown in Table 3. Both are manufacturing companies, but they are in different industries. We can see the obvious differences in format even though they both follow standard accounting format. We performed an analysis of 66 companies across a variety of industries and found that the format variety is reduced for the companies within the same industry. For example, both Motorola and Intel manufacture electronic chips, and their financial statements are very similar. That is the primary reason the user is prompted to input the industry at the beginning of an EDGAR Agent inquiry. Another reason is that it is then easier for a selected company to be compared with its peer companies. Through our industry survey, we found this classification helps eliminate the difficulties caused by the format differences in retrieving and processing the financial statements.

## 5.3. The Õariety of the accounting terms

The most challenging issue in the EDGAR Agent development was how to deal with the variety of the terms used in the financial statements. Neither the SEC nor the AICPA impose standards on these terms. Companies have complete freedom in choosing the names used to describe financial items such as cash. At the current time, we are most concerned with the terms used in the ratio calculations. Some of these have few variety, for example, the term ‘‘Cash’’ is being used by 9.1% companies of our sample, ‘‘Cash and cash equivalents’’ by 69.7%, ‘‘Cash and due from banks’’ by 12.1%, with the remaining 9.1% of the companies using other terms such as ‘‘Cash and interest bearing equivalents’’. In contrast, some terms have significant variety, such as ‘‘Accounts receivable’’, which has more than 20 synonyms in the 66 balance sheets analyzed.

The first approach adopted to deal with the term variety was the use of a direct pattern matching function. The approach worked very well for a few specific tested companies. However, each time we encountered a new synonym that was not included in the judgement criteria written in the agent code, we expanded the criteria. After a while we began to hit a wall because it was almost impossible to make one or two exclusive matching criteria. Using complex judgement criteria greatly decreased the speed of the agent since every component of the criteria had to be checked over the whole file line by line.

Our second approach to this problem was statistic information retrieval 6 . We decomposed each term<sup>w</sup> <sup>x</sup> into single words and assigned a certain probability to each word according to the possibility of its appearance in the corresponding standard term. The corresponding term with the highest probability was then selected. For example, the word ‘‘Cash’’ almost certainly appears in ‘‘Cash and cash equivalent’’, and a very high probability should be assigned. However, it is less likely for the term to appear in the synonyms of ‘‘Accounts receivable’’, so a very low probability should be assigned in this case. Furthermore, ‘‘Cash’’ is impossible to be included in the ‘‘Current liability’’, so the probability is zero. Using C <sup>q q</sup> to write the test code, and with limited tests, it was found the statistic retrieval concept could be adapted to agent development. The drawback to this approach is that it is hard for a developer to learn the correct assignment of probability without an extensive investigation into accounting terminology.

Our chosen approach to solving the terminology problem is a combination of Perl code and a relational database 24,25 . With the assumption that <sup>w</sup> <sup>x</sup> synonyms are close to exclusive if a fairly large sample can be maintained, we believe a table in a relational database will help us overcome the term recognition obstacle. This table has a one-to-many relationship. Carrying the necessary words, the agent goes to the database to search for an exact match. The process is triggered from the agent script to the database interface, then to the ODBC driver and finally to MS Access or Oracle. When the agent determines an exact match in the synonym field of the table, it will retrieve the corresponding standard term and its value. Without an exact match, the agent will retrieve nothing and return. An alternative method being tested is having the agent make an autonomous decision about which standard term is most likely used when there is no exact match. This approach utilizes intelligence within the agent, and the implementation can be the combination of the statistic retrieval approach and this database approach or other artificial intelligence methods.

While the above syntactic problems are real and challenging, there are two even deeper challenges underlying them. These challenges are semantic and contextual 21 . Semantic challenges exist in the way <sup>w</sup> <sup>x</sup> information is interpreted by auditors, and how intelligent agents will deal with this. Context challenges arise when agents search the web at large and find financial information on web sites, but need to determine if the context of this information is relevant for retrieval. These issues are currently being studied by other members of our research team in parallel with the Edgar agent development.

The challenges to building the EDGAR Agent demonstrate the constraints placed on the technical development of intelligent agents. While our agent is relatively simple from a technical perspective, the ‘‘messy’’ world of financial reporting required some creative solutions to problems not found in the pure laboratory environment. Our next step in dealing with these ‘‘messy’’ problems was to conduct a limited, preliminary field test of the agent.

## 6. Preliminary field test of the EDGAR Agent

The Edgar agent was reviewed by thirty professionals representing the management, accounting, and finance areas. These respondents were members of a business school graduate program and all had some current or previous work experience. The instrument used to evaluate the agent is included in Appendix A of this document, and was based on previously validated measures 22,23 . While the statistical data <sup>w</sup> <sup>x</sup> presented below in Table 4 is interesting and useful for design purposes, the feedback we received in comment form was even more insightful.

One of the things that came through strongly was the issue of trust in Internet data. While most of our respondents thought the information looked good and could be useful, they indicated that they had no way of knowing if the data was accurate. For example:

The responses of N<sup>r</sup>A are indicative of the fact that I did not audit the results for accuracy; presuming that the results are accurate, the information is very useful.

I did a comparison to Bloomberg data on a few companies. The data pulled from Bloomberg varied slightly in several areas. We would like to know why they vary. The comparison was with ADM after the close on November 18.

Table 4  
EDGAR agent evaluation results N<sup>s</sup>30, seven-point Likert scale

<table><tr><td>Item</td><td>Mean</td><td>STD</td></tr><tr><td>The quality of data produced</td><td>5.69</td><td>0.84</td></tr><tr><td>The format of the output</td><td>3.62</td><td>1.53</td></tr><tr><td>The accuracy of the data</td><td>4.10</td><td>2.17</td></tr><tr><td>The timeliness of response</td><td>5.54</td><td>1.24</td></tr><tr><td>The speed of response</td><td>5.69</td><td>1.16</td></tr><tr><td>The structure and organization of the screens</td><td>4.62</td><td>1.02</td></tr><tr><td>The look and feel of the agent</td><td>4.00</td><td>1.70</td></tr><tr><td>Overall quality</td><td>5.00</td><td>0.80</td></tr><tr><td>Ease of use</td><td>5.62</td><td>1.02</td></tr><tr><td>User friendliness</td><td>5.00</td><td>1.33</td></tr><tr><td>Understandability of on-screen instructions</td><td>5.54</td><td>1.03</td></tr><tr><td>Understandability of output</td><td>5.31</td><td>1.16</td></tr><tr><td>Usability of the agent</td><td>5.31</td><td>0.93</td></tr><tr><td>Usefulness of data produced</td><td>4.92</td><td>1.89</td></tr><tr><td>Commercial applicability of the agent</td><td>5.50</td><td>0.98</td></tr></table>

Based on the above comment, we checked that particular data point and found that we were accurately reporting numbers from Edgar and the stock market. However, Bloomberg 20 was reporting dif-<sup>w</sup> <sup>x</sup> ferent data, showing that even ‘‘official’’ sources on the Internet seem to be varying slightly. These comments and our follow-up investigation indicate that Internet security and accuracy are issues that must be addressed for agent technology to be used successfully in real business domains such as auditing.

The other comments were primarily around formatting issues.

I like the fact that you always have the option of a link back to the search page, rather than having to use the back key in the search engine. The program is very plain, while it is easy to read, a ‘‘nicer package’’ would make it seem more professional. The format of the output forced me to scroll over an inch to see the last column and then I couldn’t see what the first column said. Maybe lines would help readability.

Based on these comments, we are currently updating our user interface using focus groups of financial professionals as respondents.

## 7. Discussion and future research

In addition to financial information, intelligent agents have the capability of searching the Internet for environmental and competitive information about a firm or its clients that is present in the media. The ability of agents to search in full text mode will allow them to be trained to search for competitive threats and opportunities. Different types of artificial intelligence can be used so that agents learn as they search. Neural networks are one type of tool that have the potential to build continuously learning agents 17 . <sup>w</sup> <sup>x</sup>

Intelligent agents that can provide not only financial information and calculations about a company, but also can reconcile this information with environmental data have the potential to be marketed as a value-added service to clients of accounting firms. This service can be used internally by the client company for auditing and decision-making, or could be used externally by the client to assess and make decisions about the competitive environment. In this way, accounting firms can extend existing audit and consulting services under the quality<sup>r</sup>service framework. As accounting firms enable their clients to gather information and participate in the virtual global world, they will also profit from providing security and authentication of transactions as they are performed.

Direct research resulting from this study will extend and refine the EDGAR Agent’s capabilities for gathering, isolating and analyzing key financial data from the EDGAR database. Additional refinements will include intelligence on the home computer that calculates financial ratios in a way that is useful and meaningful for corporate decision-makers. The EDGAR Agent lays the foundation for additional research in the area of on-line financial reporting and virtual auditing. For example, one can integrate such an agent with artificial neural networks to develop models for predicting bankruptcies 11 , potentials for management fraud 12 , or for going concern <sup>w</sup> <sup>x</sup> judgments 4 with timely information of the client <sup>w</sup> <sup>x</sup> and the industry.

We plan to gradually build up the EDGAR Agent into the FRAANK Financial Reporting and Audit- Ž ing Agent With Net Knowledge Agent capable of. demonstrating numerous features of a universal online auditor’s assistant. We envision the FRAANK Agent Fig. 3 as having multi-tier architecture withŽ . the agent’s logic clearly separated from the end user interface on the one hand, and from the data and knowledge sources on the other hand.

The current implementation of the EDGAR Agent as a monolithic Perl program will be redesigned for the modular architecture presented above. The FRAANK Agent will include the programming logic written in PERL, KQML and Java, and the data and knowledge sources implemented in an SQL database, with the internal communications implemented using ODBC over TCP<sup>r</sup>IP. The heterogeneity of the implementation is the result of choosing the most appropriate tool for each task. Thus, the analysis and information extraction from natural text documents will be implemented in Perl and KQML, while mobile applets that FRAANK might need to spawn will be written in Java.

We plan to continuously develop and enhance the AI capabilities of the FRAANK Agent. It is however not realistic to expect that a single agent can embody all the sophisticated stand-alone expert systems developed for the accounting and auditing professions. Important steps on the way leading from the EDGAR Agent to the FRAANK Agent will include:

<sup>Ø</sup> More detailed analysis of SEC filings to extract financial statements and compute financial ratios.

Such analysis will require the creation and incorporation into our agent of a data source of accounting terms and their synonyms.

<sup>Ø</sup> Interaction with additional information sources, e.g., querying a stock quote server to compute the current market value of a company, which can be used to compute Altman’s Z-factor.

<sup>Ø</sup> Formal representation and learning of the structure of external information sources aimed at finding important financial and accounting information in companies’ Web sites of arbitrary structure.

<sup>Ø</sup> Collaboration with external agents, e.g., the use of existing ‘‘news agents’’ for gathering recent non-financial information about companies.

This stream of research could lead to the development of intelligent agents that continuously access and search client databases for information and report this information back to the auditing firm. It is clear that such agency would require a high degree of competency on the part of the agent as it acts as a proxy for the human auditor. This type of agency also requires a high level of authentication and verification that the information found in the database is up-to-date and factual. For the client of an accounting firm to allow such an agent into its database, a high level of trust is required. However, the rewards of such a relationship would be worthwhile to both the accounting firm and its client. A close partnership would be developed whereby the accounting firm no longer provides only historical information and verification to the client, but also provides valuable decision-making and competitive knowledge. The intelligent agent becomes the third partner in a relationship whose goal is to make the client organization more profitable.

The FRAANK Agent Architecture  
![](/api/attachments/HX8KMFPU/fulltext/images/2a3b795947e93671d9479c256fcc46292893b22beb3a946a6953e9eb417d5c9e.jpg)  
Fig. 3. The FRAANK Agent architecture.

## Appendix A. User questionnaire

A.1. The UniÕersity of Kansas study of intelligent internet agents

The following questionnaire asks a series of questions about a developmental intelligent agent, FRAANK. It is important that you answer the questions in the survey carefully and honestly. This research will only be of value if you tell us what you really think. Please contact Kay Nelson at KU if you have questions 785 865-7529 or knelsonŽ . @ukans.edu

Your participation in this research is voluntary. If you object to the questionnaire or to a specific question, you may chose not to respond. Your cooperation is strongly desired, and the KU research team has taken measures to ensure that your responses remain confidential. All answers to this questionnaire will be kept strictly confidential. At no time will this questionnaire be shown to anyone else in your organization. Responses will be reported only at the company level, not at the individual project level. Once the data has been collected and entered into the computer, completed questionnaires will be destroyed, leaving only the coded data as a record of responses.

Thank you for your participation in this study. Please e-mail responses to Kay Nelson, knelson @ukans.edu.

The following demographic information is for purposes of project tracking only. This information, as well as all information in this questionnaire will be seen only by the researcher and will be kept strictly confidential under The University of Kansas research guidelines.

## 1. Name

2. Employer

3. Employer Unit<sup>r</sup>Department

4. Academic program

5. Credits completed toward degree

6. Age

7. Gender \_\_\_\_F \_M

8. Number of Years Using Internet

9. Internet Expertise Check one Ž . Novice Average Expert

10. Average number of hours spent weekly on the Internet

11. Have you ever purchased anything via the Internet? \_\_\_\_Y \_\_\_\_N

12. Have you used a credit card on the Internet? \_Y \_\_\_\_\_N

13. Name of Internet provider KU Other please specify Ž .

## A.2. Instructions

To complete the survey, please go to the following URL: http:<sup>rr</sup>pink7.busmis.ukans.edu<sup>r</sup>Fraank<sup>r</sup> agent.pl

Please test the companies listed below following the directions provided on the agent. When you are finished, please complete the following survey and email it to knelson@ukans.edu. If possible, please respond by Friday, November 20th. All respondents will receive a token gift with the KU Logo.

Company list:

Rainbow Technologies

Rainbow Rentals

Sunquest Information Systems

Sunglass Hut

Sunrise Assisted Living

Sanifill Texaco Computer Motion Computer Task Group Green Mountain Coffee Charles River Express Scripts

This following questions ask for information about how well the Edgar Agent performed when you tested it. Please read each question individually and answer it to the best of your ability place theŽ appropriate number or N<sup>r</sup>A after the question in the space provided ..

Ž . 1 Rate the performance of the Edgar Agent on the following characteristics:

<table><tr><td>Not appli-cable</td><td colspan="2">Poor performance</td><td colspan="3">Average Performance</td><td colspan="2">Excellent performance</td></tr><tr><td>N/A</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr></table>

a. The quality of data produced: \_\_

b. The format of the output: \_\_\_

c. The accuracy of the data: \_\_\_

d. The timeliness of response: \_\_\_

e. The speed of response: \_\_\_

f. The structure and organization of the screens:

g. The look and feel of the agent: \_\_\_

h. Overall quality: \_\_\_

i. Ease of use: \_\_\_

j. User friendliness: \_\_\_

k. Understandability of output: \_\_\_

l. Understandability of on-screen instructions:

m. Usability of the agent:

n. Usefulness of data produced: \_

o. Commercial applicability of the agent:

Please add any additional comments about FRAANK.

## References

<sup>w</sup> <sup>x</sup> 1 American Institute of Certified Public Accountants, in: AICPA Professional Standards Vol. 11996, AU Section 329.

<sup>w</sup> <sup>x</sup> 2 G. Aparico, The Role of Intelligent Agents in the Information Infrastructure, IBM, 1995.

<sup>w</sup> <sup>x</sup> 3 A. Bhimani, Securing the commercial internet, Communications of the ACM 39 6 1996 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 S.F. Biggs, M. Selfridge, R. Krupka, A computational model of auditor knowledge and reasoning process in the goingconcern judgment, Auditing: A Journal of Practice and Theory, Supplement 1992 .Ž .

<sup>w</sup> <sup>x</sup> 5 N. Borenstein et al., Perils and pitfalls of practical cybercommerce, Communications of the ACM 27 7 1996 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 L. Egghe, R. Rousseau, Topological aspects of information retrieval, Journal of the American Society for Information Science 49 13 1998 .Ž . Ž .

<sup>w</sup> <sup>x</sup>7 K. Crowston, Market-enabling internet agents, in: Proceedings of the Thirtieth Annual Hawaii International Conference on System Sciences, 1997.

<sup>w</sup> <sup>x</sup> 8 T.H. Davenport, Process Innovation: Reengineering Work through Information Technology, Harvard Business School Press, Boston, MA, 1992.

<sup>w</sup> <sup>x</sup> 9 A.A. Arens, J.K. Loebbecke, AUDITING: An Integrated Approach, Prentice Hall, NJ, 1994.

<sup>w</sup> <sup>x</sup> 10 R.K. Elliott, Confronting the future: choices for the attest function, Accounting Horizons 8 3 1994 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 K. Fanning, K. Cogger, A comparison analysis of artificial neural networks for financial distress, International Journal of Intelligent Systems in Accounting and Management 3 4Ž . Ž . 1994 .

<sup>w</sup> <sup>x</sup> 12 K. Fanning, K. Cogger, R. Srivastava, Detection of management fraud: a neural network approach, International Journal of Intelligent Systems in Accounting and Management 4 Ž . 1995 .

<sup>w</sup> <sup>x</sup> 13 P. Konana et al., Pricing of information services using real-time databases: a framework for integrating user preferences and real-time workload, in: Proceedings of the Seventeenth International Conference on Information Systems De-Ž cember, 1996 , 1996..

14 R. Lea, Opportunities for assurance services in the 21st century: a progress report of the special committee on assurance services, in: Proceedings of the 1996 Deloitte and Touche<sup>r</sup>University of Kansas Symposium on Auditing Problems May 1997 .Ž .

<sup>w</sup> <sup>x</sup> 15 P. Maes, Agents that reduce work and information overload, Communications of the ACM 27 7 1994 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 M. Minsky, D. Riecken, A conversation with Marvin Minsky about agents, Communications of the ACM 27 7 1994 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 T. Mitchell et al., Experience with a learning personal assistant, Communications of the ACM 37 7 1994 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 18 D. Norman, How might people interact with agents, Communications of the ACM 37 7 1994 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 19 M.A. Vasarhelyi, The CPAS<sup>r</sup>CCM experiences: prospectives for AI<sup>r</sup>ES research in accounting, in: Proceedings of the 1996 Deloitte and Touche<sup>r</sup>University of Kansas on Auditing Problems May 1996 .Ž .

<sup>w</sup> <sup>x</sup> 20 Bloomberg Financial Services, http:<sup>rr</sup>www.bloomberg. com<sup>r</sup>welcome.html.

<sup>w</sup> <sup>x</sup> 21 S. Madnick, Are We Moving Toward an Information Super-Highway or a Tower of Babel? The Challenge of Large-Scale

Semantic Heterogeneity, Working paper, Sloan School of Management, Massachusetts Institute of Technology, 1997.

<sup>w</sup> <sup>x</sup> 22 K.M. Nelson, M. Ghods, Technology flexibility: conceptualization, validation, and measurement, European Journal of Information Systems 1998 December.Ž .

<sup>w</sup> <sup>x</sup> 23 K.M. Nelson, M. Ghods, Measuring quality during software maintenance: an empirical analysis, Decision Support Systems 1998 October.Ž .

<sup>w</sup> <sup>x</sup> 24 C. Wong, Web Client Programming with Perl: Automating Tasks on the Web, O’Reilly and Associates, Sebastopol, CA, 1997.

<sup>w</sup> <sup>x</sup> 25 L. Wall, T. Christiansen, R.L. Schwartz, Programming Perl, 2nd edn., O’Reilly and Associates, Sebastopol, CA, 1996.

![](/api/attachments/HX8KMFPU/fulltext/images/abd4381939186c45924db2f335d27bb6129e81d42a517aaf6086e9d93f36714e.jpg)

Dr. Kay Nelson is an assistant professor of Information Systems at The University of Utah. Dr. Nelson has industry and academic experience both in the U.S. and overseas. She works extensively in the area of organizational and information technology flexibility, strategy, business value, and measurement. Dr. Nelson holds a Ph.D. from the University of Texas at Austin in Management Science and Information Systems with minors in Technology Management

and Organizational Behavior. Dr. Nelson has published in the areas of software engineering and IS<sup>r</sup>Business partnership in publications such as MIS Quarterly and Decision Support Systems. Dr. Nelson was the recipient of the International Conference on Information Systems ICIS best paper award in 1993 andŽ . recently won another best paper award at the Workshop on Information Technologies and Systems WITS .Ž .

![](/api/attachments/HX8KMFPU/fulltext/images/9b7479247664f7c06b8ef85bf8c34f3219132625fbb3b03d69e3778c705c6dfe.jpg)

Dr. Alexander Kogan received the Ph.D. in Computer Science from the USSR Academy of Sciences, Moscow, and an MS degree in Applied Mathematics and operations research from the Moscow Institute of Physics and Technology Ž . Phystech , in 1988 and 1984, respectively. He is currently an Assistant Professor of Accounting and Information Systems with the Faculty of Management, Rutgers University, Newark. His research interests are in the areas of

expert systems, artificial intelligence, knowledge-based decision support systems, accounting information systems, accounting problems of Internet infrastructure and electronic commerce, productivity accounting, logical analysis of data, Boolean functions, and reasoning under uncertainty. Dr. Kogan has published over 40 technical papers in these areas.

![](/api/attachments/HX8KMFPU/fulltext/images/597afd7456fde0da2780523f22136300dbf2c0952f72c5696cc901e2fa7c6008.jpg)

Dr. Rajendra P. SriÕastaÕa is Ernst and Young Distinguished Professor of Accounting and Director of the Ernst and Young Center for Auditing Research and Advanced Technology at the School of Business, University of Kansas. He holds a Ph.D. in accounting from the University of Oklahoma, Norman 1982 and aŽ . Ph.D. in physics from Oregon State University, Corvallis 1972 . ProfessorŽ . Srivastava’s publications have appeared in The Accounting Review, Journal of

Accounting Research, Auditing: A Journal of Practice and Theory, and International Journal of Intelligent Systems. He received the 1996 Award for Notable Contribution to AI and Expert Systems Research in Accounting from the AI<sup>r</sup>ES Section of the American Accounting Association. His current research interests are evidential reasoning in auditing, and on-line continuous auditing.

Dr. Miklos. Vasarhelyi is the director of the Rutgers Accounting Research Center and was area chairman for three years. Prof. Vasarhelyi visited at the Theseus Institute in France and is ‘‘Professeur Vacataire’’ at that institution. He was Associate Professor and Director of the Accounting Research Center of the Graduate School of Business, Columbia University and Assistant Professor of Accounting at the University of Southern California. Creator and coordinator of the MBA program at the Catholic University of Rio de Janeiro, as well as Executive Director of the Rio Data Center. Prof. Vasarhelyi has been associated with the AT and T Bell Laboratories since 1985. His work has concentrated in the areas of financial systems architectures, internal audit and expert systems.

![](/api/attachments/HX8KMFPU/fulltext/images/2be286de5b5f91a189e3daf19bc368773fe1c28e0b77bbc3349b189bdf716ff6.jpg)

Hai Lu is a doctoral student in Accounting Information Systems at the University of Kansas. He received his MS and Ph.D. in Optoelectronic Engineering from Chinese Academy of Sciences. His current research interests include the application of information technology in auditing domain and the information disclosure related to the internet. He was a visiting scientist at CSIRO Division of Telecommunication and Engineering Physics in Australia from 1991–1993

and a visiting scholar at Marshall School of Business in University of Southern California in Fall 1998. He has previously published several articles in Review of Scientific Instruments.
