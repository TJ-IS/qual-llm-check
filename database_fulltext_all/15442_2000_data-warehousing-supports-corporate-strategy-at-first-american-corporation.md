---
otero_id: 15442
otero_key: "KBMS69TA"
title: "DATA WAREHOUSING SUPPORTS CORPORATE STRATEGY AT FIRST AMERICAN CORPORATION"
authors: "Brian L. Cooper; Hugh J. Watson; Barbara H. Wixom; Dale L. Goodhue"
year: "2000"
journal: "MIS Quarterly"
doi: "10.2307/3250947"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DATA WAREHOUSING SUPPORTS CORPORATE STRATEGY AT FIRST AMERICAN CORPORATION<sup>1,</sup> <sup>2</sup>

By: Brian L. Cooper First American Corporation First American Center Nashville, TN 37237-0603 U.S.A. brian.cooper@fanb.com

Hugh J. Watson Terry College of Business University of Georgia Athens, GA 30602 U.S.A. hwatson@terry.uga.edu

Barbara H. Wixom McIntire School of Commerce University of Virginia Charlottesville, VA 22903 U.S.A. bwixom@mindspring.com

Dale L. Goodhue Terry College of Business University of Georgia Athens, GA 30602 U.S.A. dgoodhue@terry.uga.edu

## Abstract

From 1990 through 1998, First American Corporation (FAC) changed its corporate strategy from a traditional banking approach to a customer relationship-oriented strategy that placed FACís customers at the center of all aspects of the companyís operations. The transformation made FAC an innovative leader in the financial services industry. This case study describes FACís transformation and the way in which a data warehouse called VISION helped make it happen. FACís experiences suggest lessons for managers who plan to use technology to support changes that are designed to significantly improve organizational performance. In addition, they raise interesting questions about the means by which information technology can be used to gain competitive advantage.

Keywords: Data warehousing, corporate strategy, organizational transformation, customer relationship management, IS management

ISRL Categories: DA08, DD01, HB19, UF

## Introduction

In 1990, First American Corporation (FAC) lost \$60 million and was operating under letters of agreement with regulators. By 1999, FAC was a profitable, innovative leader in the financial services industry. This change in fortune was the result of an ambitious strategic vision and a major investment in data warehousing that made the vision possible.

FACís transformation was built around a customer relationship-oriented strategy called Tailored Client Solutions (TCS), which positioned FACís customers at the center of all aspects of the companyís operations. Although many organizations espouse customer relationship management (Duncan and Moriarty 1998; Garbarino and Johnson 1999; Peppers and Rogers 1993), FAC redesigned every aspect of its operations to meet its clients' needs as well as its own profitability goals. Underlying these efforts was the recognition that, to succeed with this strategy, it must know its customers exceptionally well and leverage that knowledge in product design, in distribution channel decisions, and in every interaction with its clients.

The execution of this strategy would have been impossible without a data warehouse called VISION that stored information about client behaviors (e.g., products used, transactions), client buying preferences (e.g., attitudes, expressed needs), and client value positions (i.e., profitability). Using information from VISION, FAC:

identified the top 20% of its customers who provided virtually all of the consumer profits, and the 40% to 50% of those who were not profitable;

developed strategies to retain the top highvalue customers;

developed strategies to move unprofitable customers to lower cost distribution channels, different products, or pricing structures that boost profitability, while still focusing on customer needs and preferences;

developed strategies to expand relationships with all customers;

redesigned products and distribution channels to increase profitability and better meet customers' needs and preferences; and

redesigned information flows, work processes, and jobs in order to meet customers needs and increase their use of profitable products.

To implement TCS, FAC senior management concluded there had to be a change in the way its employees thought about banking and about their jobs, shifting from ìbanking by intuitionî to ìbanking by information and analysis.î All of these combined actions moved FAC from losses of \$60 million in 1990 to profits of over \$211 million in 1998.

This article describes FAC's transformation and emphasizes the information technology that was essential to its success. The first sections discuss First American Corporation, the Tailored Client Solutions strategy, and the implementation and use of the VISION data warehouse. The article then explores the way in which the transformation occurred, using frameworks developed by Henderson and Venkatraman (1993) and Kotter (1995). In the process, it addresses several interesting questions about the role of IT and IT assets (Ross et al. 1996) in organizational transformation.

## Need for Change at First American Corporation

In 1998, FAC was a comprehensive financial services holding company headquartered in Nashville, Tennessee. Its holdings included:

ï First American National Bank;

ï First American Federal Savings Bank;

ï Deposit Guaranty;

ï First American Enterprises, Inc.;

IFC Holdings (formerly INVEST Financial Corporation, the nation's largest third-party marketer of investment products [98.75% ownership], headquartered in Tampa, Florida); and

The SSI Group (the largest processor of hospital healthcare claims in the U.S. [49% ownership], headquartered in Mobile, Alabama).

With operations in Tennessee, Kentucky, Virginia, Mississippi, Arkansas, and Louisiana, FAC had \$20.7 billion in assets, 7,195 employees, 391

FAC loses \$60 million

Dennis Bottorff hired as Chairman and CEO

Brian Cooper hired as Director of Marketing

![](/api/attachments/KBMS69TA/fulltext/images/6b6df0cfa9105d619356f13ee98dd848b3b6603dd08a4955894fb3232fe1f2f9.jpg)

September: Tailored Client Solutions strategy developed

First Quarter: Sybase data warehouse project begins June: Sybase project discontinued

January: NCR contracted to build database June: Data warehouse proof of concept deployed September: Tailored Client Solutions formally announced at Leadership Conference

Data Warehouse rolled out to organization

Figure 1. First American Corporation Timeline

banking offices, and 650 ATMs. It had the largest deposit market share in Tennessee, the second largest deposit market share in Mississippi, and the largest small business and middle market share in Tennessee.<sup>3</sup>

Conditions were not as good, however, in 1991 when Dennis Bottorff became Chairman and Chief Executive Officer (see the timeline of events in Figure 1). The banking industry was experiencing considerable competition, with rival banks contending for a market that was growing only moderately. Because of large financial losses in the previous year, there was concern that FAC would be closed and that the larger banks would ìcome in and pick the pieces they wanted.î Bottorff and his management team started by ìfixing the broken things in the companyî; however, they realized that FAC needed a longterm strategy if it were to survive in the increasingly competitive banking industry.

During 1992 and 1993, senior management considered a variety of competitive business strategies (Porter 1979). FAC could not be the low cost provider because it lacked the economies of scale of larger financial institutions. Product differentiation was not a feasible strategy because other banks could quickly duplicate products that showed promise in the marketplace. It could not compete for large accounts (e.g., Fortune 500 companies), because this market was dominated by large national and international banks. Ultimately, FAC leaders began talking about differentiating themselves on service, which evolved into customer intimacy (Slater 2000; Treacy and Wiersema 1993). To truly be customer intimate, they realized that they ìhad to have better information about our customers than the competition did.î Bottorff recognized that most bankers tended to be product sales or service oriented as opposed to marketing oriented, and that the inclination was to be operationally excellent as opposed to customer savvy. To succeed with a customer intimacy strategy, he would need to ìcreate a basic change in the fundamental way that bankers approach the business.î Bottorff and the management team reasoned that the place from which to drive the change effort was the marketing department.

![](/api/attachments/KBMS69TA/fulltext/images/a848b71ef9d1b92af1439f8613a5c8eb36e6744ba517a286d3aa7f67b46d06c7.jpg)  
Figure 2. Tailored Client Solutions

To move the marketing department from its previous orientation, a ìcustomer savvyî marketing director was brought on board. Unfortunately, Bottorff discovered that although this new person understood the strategy, he ìdidnít really understand how to create a management process that would drive it.î Management began a year-long search for yet another head of marketing, and in 1994 they hired one of the case's co-authors, Brian Cooper, to develop both the new business strategy and the management processes needed to implement it.

## Tailored Client Solutions

In September 1995, the marketing department, senior management, and key members of the finance department worked together to develop a strategy that they called Tailored Client Solutions. Figure 2 shows the four interlocking components of the strategy: excellent client information, a flexible product line focused on mass customization, a consistent sales and service approach centered on meeting client needs, and a distribution management approach focused on channels of choice. All this was coordinated under a broad new brand óìAbout life. About you.î óthat put the customer at the center of everything the bank did.

Client information was the first component of TCS. FAC wanted to know more about its customers, and to utilize that knowledge in every aspect of its business. In addition to demographic information and information about transactions with the bank (e.g., ATM card usage), FAC wanted information about how its customers preferred to do business and how profitable each client relationship was to FAC.

The second part of TCS was a flexible product line. By understanding its clients and having accurate product profitability information, FAC hoped to phase out or modify unprofitable products and design lucrative alternatives for clients.

The third component of TCSóconsistent serviceófocused on determining and meeting client needs. This called for a major shift in sales culture. Historically, representatives would focus on selling products or services that were being promoted with limited regard to their fit with customer needs. In the new environment, a FAC representative would begin a customer relationship by discussing that person's current financial situation and future goals. Then, together, the customer and representative would explore products that would help the client accomplish personal objectives.

Distribution management was the final component of the strategy. Banking services were delivered through various channels (e.g., branch offices, ATMs, PC banking), and banks had to make longterm decisions about the best way to make services available to clients. These decisions required knowledge about how customers used the bank, how they would prefer to use the bank under different circumstances (e.g., if there were a fee for using a teller), and the costs of the alternative distribution channels. With this information, FAC would be able to optimize the design of its distribution channels to meet client needs at the lowest cost.

All four of these strategic components fit under the umbrella of the new brand identity for the bank: ìAbout Life. About You.î The designers of the components of the TCS strategy continuously analyzed the components to ensure that they focused on meeting client needs. In the end, the designers believed each component was valuable and worked together to create a powerful synergy.

Bottorff viewed the strategic planning process as a critical way to force people to think in new ways.

Itís not: here are the goals, go out and tell me what you do. Itís: here are the goals, here are the fundamental strategies, and here are some areas [where you should be thinking] about how to lower the cost of distributionÖhow to build client solutions.

Bottorff and his management team built a set of specific initiatives around the TCS strategy, encouraging people to think and manage differently.

Although people throughout FAC were acutely aware of the companyís instability and recognized that change had to occur, senior management felt that revealing TCS to the organization ìwould have been overwhelming, given where the company was at the time.î For the next two years, the champions of TCS only communicated relevant parts of the strategy to the people involved in developing the various components. Five separate projects, each one representing a major piece of the TCS strategy (e.g., client information, brand identity), were pursued by five separate groups concurrently. Each project was designed to have significant positive financial ìliftî (i.e., impact) and to embody some of the basic changes in the way the bank would operate.

On September 20, 1997, after each component was successfully in place, the complete Tailored Client Solutions strategy was formally announced at the FAC Leadership Conference. The Leadership Conference was also the kickoff for the Destination 2000 challenge to all FAC employees, with the goal that by the year 2000, FAC would join those banks that led the industry in terms of financial performance and valuation measures. A videotape that presented Destination 2000 was distributed to all bank employees, who were encouraged to join the effort and to adapt creatively to the upcoming changes. The theme was reiterated at company-wide meetings, in internal correspondence, and through visible changes in work practices.

An important component of strategy implementation was to change business processes and the incentives related to them. Performance on increasing profitability, retaining clients, and expanding the use of the bankís products became important factors for how employees were evaluated and compensated. For example, on Mondays, branch managers committed to performance objectives for the week, and on Fridays their performance was evaluated. Employee compensation was tied to how well the commitments were met.

## The VISION Data Warehouse

Because every piece of the Tailored Client Solutions strategy demanded better and more accessible information about the client than FAC, or most banks, ever had, senior management realized that it needed information technology to support the strategy. The critical piece of ITóa data warehouse called VISIONówould contain integrated customer information, product profitability information, and distribution revenues and costs. However, the leaders knew much better what information was needed and how to use the information, than they knew how to build the data warehouse. FAC as a company had not made significant investments in IT in the 1980s and the early 1990s. When the Vice President of Operations and Technology joined the company in 1992, "it was an enormous catch-up effort. We spent the first four years doing projects that most of us had done ten years or more before at some other places." When TCS began, FAC had no significant in-house experience in data warehousing. According to project manager Connie White, ìWe all were on the same page strategically, but we really didnít understand what was needed to do this.î

## A False Start Using Internal IT

At first, the IT department was charged with building the warehouse to support TCS; however, from the start the project was hindered by poor decisions about the data warehouse architecture. Several years earlier, the IT department had built a small credit information data mart using Sybase that was part of a risk management and recovery effort for regulation purposes, and they decided to take their Sybase experience and ìbuild a larger version of the first effort.î Internal IT individuals filled the positions on the team, and they seriously underestimated the size and complexity of the project. Also, the limited experiences of those on the IT project team led to several poor decisions. For example, the use of mainframe data extraction, transformation, and loading (ETL) tools was not considered. While the selected software was adequate for small data files, it was not appropriate for an enterprise data warehouse.

After three months, senior management stopped the Sybase project. Marketing had lost faith that the IT department would be able to create a data warehouse to support TCS. Even though it was a significant departure from established practice at FAC, the marketing group lobbied hard internally to contract with NCR to provide hardware, software, and consulting services. They argued that NCR was a leader in the data warehousing field and essential for such a critical component of the TCS strategy. Six months after discontinuing the Sybase project, the contract with NCR was signed.

## A Second Attempt Using External Expertise

The second data warehouse project was staffed with a combination of FAC IT personnel and NCR consultants, with the intention that NCR would transfer knowledge and move FAC up the learning curve over the course of the project. The company was careful to appoint a FAC employee from marketing to manage the process and to ensure that FAC employees were trained and mentored by NCR. In addition, key managers from marketing, finance, and IT completed the leadership team. As a senior IT manager explained, ìwe jumped into the pool because NCR said that they would jump in with us and keep us afloat.î

<table><tr><td colspan="6">Table 1. VISION Project</td></tr><tr><td></td><td>First and Second Quarters 1996</td><td>Second and Third Quarters 1996</td><td>Third Quarter 1996 — First Quarter 1997</td><td>Second Quarter 1997 — First Quarter 1998</td><td>Second Quarter — Fourth Quarter 1998</td></tr><tr><td>Business Goals</td><td>Identify the top revenue producers</td><td>Identify the least profitable customers</td><td>Include actual transaction and product data in profitability formulas</td><td>Understand all aspects of client and product profitability</td><td>Incorporate profitability understandings in business processes</td></tr><tr><td>Technical Goals</td><td>Enhance the existing customer information system with retail revenue</td><td>Enhance the existing customer information system with direct contribution view for consumers</td><td>Enhance existing customer information system with net income after capital charges (NIACC) for consumers</td><td>Deploy the warehouse—proof of concept (consumer)Commercial profitability integration</td><td>Complete production testing of the warehouse</td></tr></table>

The development of VISION included a multiphase effort, with each phase calculated to produce tangible business benefits while moving the overall project forward with technical deliverables. The timeline and goals for VISION are presented in Table 1. The project manager believed that the incremental approach enabled FAC to ìget the end result and bring in the revenues as we worked on the project, as opposed to many companies who go out and want to do everything at one timeóand arenít successful."

The first goal of VISION was implemented in First Quarter 1996 to help managers understand the overall revenue picture. The First Manhattan Consulting Group, a recognized leader in the financial services industry at understanding profitability, provided benchmark data for FAC. Together with First Manhattan, a team of people from the finance department developed revenue, cost, and profit formulas to use with VISION data. These formulas and actual transaction data were added to an existing customer information system within three months, and the project team began to understand exactly which data belonged in the warehouse. Over time, additional products and transaction data were added to VISION, and the profit formulas were enhanced.

During this period, the data warehouse team developed extraction and transformation processes, while modeling the data to be stored in VISION. The legacy systems were quite disparate, and the extraction process was challenging. Basic fields like bank number (i.e., the number that identified an individual bank) were difficult to reconcile across files. For example, some systems had a single field that contained bank number, others had bank numbers stored as a part of a larger field, while others had bank numbers spread across several fieldsóor did not have the field at all. The project team found that it was ìdifficult to transform data into the warehouse view.î

The project team built a data warehouse platform using the NCR 5150M configured with five SMP nodes running the Teradata Relational Data Base System. This configuration provided 1.5 TB of storage to FAC, and at the end of 1998 it supported 200 GB of raw data, which continued to increase by 10 GB per month. The database held 2 million accounts and information about 1.2 million households, and FAC planned to store up to 37 rolling months of history for analysis. Figure 3 shows the warehouse's architecture.

![](/api/attachments/KBMS69TA/fulltext/images/951bc547c352c50ab3f05ad54344664adb7e07bd7d46c66d783dddc3977cccab.jpg)  
Figure 3. The VISION Data Warehouse Architecture

The warehouse utilized over 100 source files that were extracted from 26 legacy applications. From the mainframe environment, VSAM and IMS files were sent by ftp to a file server, where Informaticaís Powermart applied business rules to transform the data (e.g., making customer account numbers consistent across banks). The resulting files were loaded into a warehouse staging area where business users validated the data. After the users examined the files and approved the data quality, the data moved into Teradata base tables that were organized by account and by activity. Concurrently, files from external data sources, such as student loans from Sallie Mae, geographic and financial data from Dun & Bradstreet, and psychographic and demographic appends to data from Harte-Hanks, were incorporated into the warehouse. The process of populating the data warehouse took approximately 10 business days.

Table 2 describes the various kinds of data that existed in VISION after the warehouse was populated. All data could be analyzed at any level of aggregation, from bank-wide or line of business down to individual account or client relationship.

The maintenance of the warehouse was a complex manual process, and the project team soon discovered that they had not created an effective permanent production environment. In First Quarter 1997, after the warehouse was delivered to a handful of analysts, the users noticed irregularities in the data they received. The problem was traced to a combination of software upgrades and changes in the legacy systems that fed the data warehouse. The analysts began to mistrust the warehouse data, and the project team had to deal with credibility issues for several months after the incident. FAC recognized that controls had to be put in place, and the VISION team began to coordinate more closely with the legacy systems support group. ìWe had to change procedures so that any changes to source systems were recognized and accommodated in the data warehouse.î The VISION team also began to investigate how to put automatic controls in place, arrange for proper warehouse management tools, and automate processes where possible. Throughout 1998, the data warehouse team validated the data, rolled out the warehouse, and helped to develop applications for finance and marketing.

<table><tr><td colspan="3">Table 2. VISION Data</td></tr><tr><td>Data</td><td>Description</td><td>Source</td></tr><tr><td>Client Behaviors</td><td>ProductsDelivery ChannelsTransactions</td><td>IBM mainframeSallie Mae</td></tr><tr><td>Client Buying Patterns</td><td>SegmentsAttitudesExpressed Needs</td><td>IBM mainframeDun &amp; Bradstreet geographic and demographic dataHarte-Hanks household data</td></tr><tr><td>Client Value Positions</td><td>Profitability</td><td>IBM mainframeProfitability algorithms</td></tr></table>

## Data Warehouse Team

Eighteen full-time FAC employees eventually comprised the team to support all of the data warehousing initiatives, and Figure 4 shows the teamís organization chart. Warehouse Services managed the extraction, transformation, and load processes and the Warehouse Development teamóthe ìgatekeepersî of the warehouseówere responsible for project management of new and enhanced data feeds. Business Access Tool Support implemented and supported the data access tools; the Analytics group performed analytical studies and ad hoc analysis of warehouse data; and the Data Mart team extracted, transformed, and loaded data into the PAR system, a VISION data mart.

FAC discovered that its required data warehousing skills changed over time. They observed three phases in the warehouse life cycle: design it, build it, and exploit it. Each of these phases required a different set of talents, perspectives, experiences, and skills. Those involved in the design it phase needed a good data architecture background, good logical data modeling skills, and a strong understanding of the business. Those involved in the build it phase needed strong project management, process management, and technical (programming) skills. Those involved in the exploit it phase needed strong technical backgrounds, excellent analytical skills, and, most importantly, the ability to translate the analysis into an actionable marketing plan.

Whatever skills were needed, FAC found the demand for experienced data warehousing personnel to be very high. Members of the data warehouse team continuously received "off the scale" offers from other companies, including consulting firms. On several occasions, a key person left at a critical time, delaying the data warehousing initiative and severely challenging the knowledge transfer process with NCR. Some managers expressed concern about the ability of FAC's IT group to take on the responsibility of maintaining the warehouse once NCR left:

NCR is running it for us right now. They are doing everything, and we have just signed another three month contractÖ. I am really nervous about them leaving because I am not seeing the talent, the infrastructure internally in FAC to continue to run it.

![](/api/attachments/KBMS69TA/fulltext/images/bdd2e5ecaf35f68fb4bedc82c3ba50e55c8a1f0e5492e3d5a7f4305b0c324a8e.jpg)  
Figure 4. Data Warehouse Team Organization Chart

FAC developed an attractive retention program (e.g., bonuses for completion of the project, commitments for additional training) for key people, but it still was difficult to retain them. As late in the project as 1998, three people left within a month of each other for jobs at Big Five Consulting firms, each making double his or her previous salary. FAC found that an effective strategy was to bring in people with a "contract to hire." This approach brought contractors into FAC and provided the bank the opportunity to "take a test drive" before offering them a permanent position.

![](/api/attachments/KBMS69TA/fulltext/images/d2b11ff1121049aa369c3aa2c5853ec691a51c9caef529b76494a2492e52e9a5.jpg)  
Figure 5. The Client-Centric Data Model

## Using VISION

Once the warehouse was in place, 20 marketing and 30 finance analysts were given direct access to warehouse data. For the marketing area, the data warehouse team used Cognos Corporationís tools to create multidimensional cubes of data, which were stored on a local file server. Users accessed these data cubes on the server or downloaded the information to their desktops. They then used the Cognos tool suite, including PowerPlay, Impromptu, and Scenario, to manipulate and analyze the data.

The finance users accessed warehouse data from both a dependent data mart created in an Oracle relational database management system and Cognos cubes. The mart supported a profitability analysis and reporting tool called PAR (Profitability Analysis Reporting), which provides users with predefined reports and allows them to run ad hoc SQL queries against the mart. By providing a data mart, the warehouse team alleviated potential performance degradation on the overall data warehouse.

All of the data were organized around the customer to provide a comprehensive understanding of the customerís demographic characteristics, the products used, transaction activities, interactions with the bank, measures of the clientís relationship to the bank, and psychographic insights about client preferences and propensities (see Figure 5). Analysts explored the data in multiple ways, including ìslicing and dicingî using time, products, geographical regions, and market segments as dimensions; planning marketing campaigns for specific products and markets; and detecting which clients are at risk of leaving the bank.

FAC found that the use of VISION required analysts with different, more advanced skill sets. Not only did they need to know the business, but they also had to be comfortable with data models, databases, SQL, managed query environments (e.g., Cognos), and data mining. Some of the company's analysts were retrained to work in the new warehouse environment, but many did not have the aptitude or inclination for the new kind of analyst work. One marketing analyst explained, ìI didnít sign up to be an IT person. I canít just go out and do focus groups anymore. I have to somehow link my actions to the data warehouse, and I donít understand how to do that.î By 1998, many of the existing marketing and finance analysts either moved to other positions or left the company, and new analysts were brought in to fill the vacancies.

## Applications of VISION

Many applications that were used by FAC to support the attraction, enhancement, and retention of customers relied on the VISION data warehouse. The following applications, organized by the four components of Tailored Client Solutions, illustrate a few of them. They were chosen to show the variety of ways in which the warehouse was used in running the bank.

## Client Information: Customer Preferences and Profiles

Customer preferences are important to many banking decisions, and FAC created preference information in VISION using a technique called ìconjoint analysisî (Chen 2000; Darmon 1999; Green and Rao 1971). The company selected a sample of over 3,000 customers and asked each one what he or she would do under different circumstances. For example, ìWould you use an ATM to make a deposit if the transaction were free and the same transaction performed by a teller cost \$.50? \$1.00?î A number of different "types" of customer were identified from the results. Based on the assumption that if you share demographics and transaction characteristics, you probably share preferences as well, FAC was able to extend its preference information to its entire customer population. Preference and profile information has been used in many ways, including targeting marketing efforts and in designing the best mix of distribution channels. By better understanding the preferences of high value customers, FAC was able to design marketing programs that increased revenues by 15% in this market segment.

## Flexible Product Line: Product Profitability Analysis for Seniors Accounts

It was critical for FAC to know the profitability of its various products. This was a complex calculation that required cost accounting equations and data from over 20 joins in VISION data warehouse tables. As an example of how this information was used, consider its application to Seniors Accounts. Like many banks, FAC offered a free checking account to customers who were 55 and older. Working with VISION, financial analysts discovered that the bank was making money from a few Seniors Accounts, but was experiencing a loss with many others. Further analysis revealed that the average size of the checking account balance was the key difference between profitable and unprofitable accounts. Based on profitability information and input from clients, a redesigned product was introduced that created value for both FAC and its customers. FAC was able to improve its risk-adjusted returns on equity from less than 20% to over 50%, while experiencing no overall loss in account balances.

## Consistent Service: Contact Management System

The contact management system helped FAC develop a one-to-one relationship with its customers by giving service representatives a clear picture of a client's entire banking relationship. Drawing from VISION and other data sources, the application provided personal information about the customer, how profitable the customer was to the bank, how long the customer was with the bank, buying preferences (e.g., serious saver, price shopper), the products used, transaction history, and the customerís financial goals. All of this information was available on the service representativeís desktop computer and supported better informed, more personal interactions with the customer. Because it was a bank-wide system, it also created more consistent, seamless service. A customer could go into any FAC branch and the service representative would have access to the same information about the client. The contact management system was credited with helping improve the retention of high value clients by 1%, which was worth \$4 million in revenue.

## Distribution Management: Distribution Management System

The Distribution Management System (DMS) helped FAC plan distribution channels for various market segments in a way that was profitable to the bank, yet still met the needs and preferences of customers. Using inputs from VISION, such as household profitability, how customers currently use the bank's products, customer preferences, segments and channel costs, and external data that matched potential new customers to the customer segments, DMS calculated the best way to distribute products to customers. Consider an example of the use of DMS. In a particular marketing area, FAC was operating a main bank (a hub), three branch banks (spokes), and various ATMs. Using DMS, it was decided that closing one branch and increasing the number of ATMs would increase the bank's profits while better meeting clientsí needs. In 1998, FAC was able to replace 22 higher cost hub locations with 30 lower cost spoke locations, while still meeting customers needs and preferences. This change created over 20% return on investment.

## Transformation at FAC

The rollout of VISION to the analysts occurred as part of a major organizational transformation in which employees were encouraged to have major shifts in their mindsets. According to the Director of Finance and Marketing Applications, "We reengineered all of finance, changed all of the systems, and made a huge shift in marketing. You saw a real change in how the lines of business do business; you saw the branches really going through a redesign process." Finance moved from being ìbean countersî to aggressively working to find better ways of creating revenue. ìGood customersî began to be determined by the profitability of their overall relationship with FAC. Marketing moved from a ìsuckers and balloonsî mentality to predicting customer actions through careful analysis and using this information to promote profitability.

Across the bank, units that previously took a passive approach to business innovation began to see themselves as responsible for creatively improving the bottom line. For example, accounts payable took an existing internally used purchasing card<sup>4</sup> application and turned it into a product that could be sold to smaller corporate customers. This was quite a shift in mindset for accounts payable, which had never before been involved with revenue creation. According to senior management: ìIt is gratifying to see that VISION has transformed the organization. People think differently now because of it, and new employees donít even know the way we used to think.î

This level of change was not easy or comfortable. Throughout the organization, those who could adapt to frequent changes and who could take the initiative to enhance performance prospered, while those who could not, left. Some areas experienced 100% turnover in one year, and many others experienced 25% to 30% turnover over three years. Those who stayed, however, reported being excited by being part of the new business environment.

The organizational changes that occurred were critical to ensure success for the technological changes. One senior manager cites a ìformulaî that he learned in business school: OO + NT = COO. It says that an old organization (in its thinking), plus new technology, equals a costly old organization. Senior management was careful to change the organization and the technology at the same time; they understood that merely implementing a data warehouse would not solve FACís problems. To support this major shift, a carefully conceived change management program was established before business processes and accompanying jobs were redesigned.

<table><tr><td colspan="7">Table 3. Performance Comparisons with the Sweet 16</td></tr><tr><td>Performance Measures</td><td colspan="2">1996</td><td colspan="2">1997</td><td colspan="2">1998</td></tr><tr><td></td><td>FAC</td><td>Sweet 16</td><td>FAC</td><td>Sweet 16</td><td>FAC</td><td>Sweet 16</td></tr><tr><td>Return on Assets</td><td>1.33%</td><td>1.55%</td><td>1.40%</td><td>1.67%</td><td>1.55%</td><td>1.66%</td></tr><tr><td>Return on Equity</td><td>15.20%</td><td>19.10%</td><td>15.91%</td><td>20.30%</td><td>18.07%</td><td>19.20%</td></tr><tr><td>Earnings per Share Growth</td><td>11.9%</td><td>12.1%</td><td>10.1%</td><td>14.3%</td><td>18.07%</td><td>15.1%</td></tr><tr><td>Productivity (lower is better)</td><td>58.98%</td><td>53.2%</td><td>57.93%</td><td>52.2%</td><td>53.44%</td><td>55.8%</td></tr></table>

In 1997, FAC stated a goal of joining the ìSweet 16î financial services organizations that lead the industry. The Tailored Client Solutions strategy, powered by the VISION data warehouse, appeared to improve the bankís operational and financial performance. Table 3 shows the progress that was made in meeting this ambitious goal, with data from 1996 through 1998.

TCS also affected favorably how other banks perceived FAC. The CEO of Deposit Guaranty (which FAC acquired in 1998) said that FAC was attractive because he wanted to be part of "a financial institution of the future and not a bank of the past." He had learned of FAC's data warehousing initiatives and had not encountered banks of similar or even larger size with the same capabilities.

## Discussion

FAC is not the first organization to use information technology to improve its competitive stance (Prahalad 1999), but the company is quite remarkable in the extent to which it transformed both its technology infrastructure and the organization itself to implement a strategic vision. Why did the effort at FAC create such a positive impact? The strategic alignment model (Henderson and Venkatraman 1993) provides a framework for exploring this issue. Henderson and Venkatraman argue that the effectiveness of the strategic management of IT depends upon alignment among four domains: (1) the business strategy, (2) the organizational infrastructure and processes to carry out the business strategy, (3) the IT strategy, and (4) the IT infrastructure and processes to carry out the IT strategy, as shown in Figure 6. The more extensive the alignment, the better the chance of major strategic impact from information technology.

## Aligning the Four Critical Domains

It is simplistic and not particularly helpful to say that FAC was able to get visible benefits from IT because it succeeded in aligning all four domains. The important question is how the alignment occurred. We believe that establishing each one of these possible links is a significant challenge to organizations.

Henderson and Venkatraman discuss several different patterns by which changes in one domain can ripple through remaining domains and achieve alignment. At FAC, the initial impetus came from business strategy. Dangerous losses in 1990 signaled that long-term viability required a new direction. Eventually the TCS strategy evolved, but it was clear from the outset that it would require major changes in the organizationa infrastructure and a new kind of technology to supply information to those carrying out the strategy. In terms of Figure 6, there needed to be strong arrows from business strategy to organization infrastructure, and from business strategy to IT infrastructure.

![](/api/attachments/KBMS69TA/fulltext/images/32bca835a011dc7fd2f0cf1847610da2ebaa55611d800931a44359d491f4d41e.jpg)  
Figure 6. Strategic Alignment Model (Adapted from Henderson and Venkatraman 1993)

While top management understood the need to change both the organization and the technology, it is not clear that they really appreciated the need to change the organizationís IT strategy. They knew what the IT infrastructure should be able to do and perhaps what it should look like, but their immediate concern was to get VISION implemented. Management was not focusing on the changes to the IT strategy that would make the new infrastructure viable in the long term. This suggests a weak arrow in Figure 6 from IT infrastructure to IT strategy. We will discuss each of the three "alignment arrows" below.

## The First Alignment Arrow: Transforming the Organization

FAC's toughest challenge and most remarkable success was in using its new vision of business strategy to drive a change in its organizational infrastructure. Many organizations have implemented technically excellent data warehouses without the major impact seen at FAC, at least in part because managers and employees have not changed their work processes and associated administrative infrastructures. FAC went beyond these changes and even changed its organizational culture, its

pattern of shared basic assumptionsÖ that worked well enough to be considered valid and, therefore, to be taught to new members as the correct way to perceive, think, and feel in relation to those problems. (Schein 1992, p. 12)

Giddensí (1984) notion of ìstructureî provides a second way of perceiving the changes at FAC. In Giddensí view, an organizationís structure is a collection of implicitly understood and at least partially binding constraints on how events and actions are interpreted, how power and resources can be used, and what kinds of actions are socially acceptable. All of these changed at FAC. For example, the definition of a ìgood customerî had new meaning. Incentive systems shifted to reward (with money and power) different types of behavior and outcomes. Social norms in the organization came to favor innovative behavior and to accept rapid change as normal.

Although the work of Schein and Giddens explains why it is so difficult to change organizations, it is also important to understand how to change them. Kotter (1995) suggests that if organizations hope to succeed in an organizational transformation, they must not omit any one of eight critical steps shown in Figure 7. One possible explanation for FACís success in using a new business strategy to change the organization infrastructure is that its transformation effort followed Kotter's prescriptions almost exactly.

Kotter suggests that organization must first ìestablish a sense of urgency,î where urgency can be based on opportunities as well as threats. Organizational transformation is too difficult to be attempted if key people are not convinced of its necessity. Creating a sense of urgency may require evidence that casts doubt on old assumptions about how the organization should operate and provides links between the disconfirming evidence and critical goals so that many individuals experience anxiety or guilt (Schein 1992). It also is necessary to ìform a powerful guiding coalitionî because transformation actions require such significant, explicit organizational power. The third item on Kotterís list is ìcreating a visionî that will help direct the change effort and devise strategies for achieving that vision. Schein suggests that individuals and organizations have a great capacity for ignoring disturbing evidence and continuing to act in established patterns when they lack a plausible way out of a bad situation. The vision must present a believable course of action, and the coalition must be perceived to be powerful enough to implement it.

All three factors were present at FAC. With the company operating under letters of agreement with regulators, virtually everyone in the organization could see that continuing with the current practices and approaches was a recipe for disaster. The TCS strategy had a guiding coalition that included the CEO and the senior management team, the new Executive Director of Marketing, and key managers in finance. These players shared a consistent view of the direction the bank needed to take. Finally, the TCS strategy was a compelling and believable vision of a new and better future. These combined factors led to a highly committed shift in the articulated strategy for the business at the top levels of the organization (i.e., a new business strategy in the upper left quadrant of Figure 6).

An interesting question is, how urgent does the situation have to be before an organization can hope to successfully implement an IT supported transformation? Is a brush with bankruptcy necessary? We would argue that all of Kotterís first three factors help determine how committed top levels of the organization are to the potential transformation. The more extensive the transformation envisioned, the stronger the commitment must be. Weakness on any one of the factors probably affects the other two, and the chances for successful transformation.

![](/api/attachments/KBMS69TA/fulltext/images/d4d2e9d25ca1b2c22b4e0614927e027ab8afdc232bdc2696f6ea78f0fdab98f3.jpg)  
Figure 7. Steps for Transformation (Adapted from Kotter 1995)

Kotterís next three factors involve driving the strategy into action at lower levels of the organization. The vision must be successfully communicated; others must be empowered to act; and there must be short-term wins. These factors involve motivating employees to invent the specifics of top management's general vision and then reinforcing beliefs in the power of the vision. Interestingly, at FAC only after clear, visible success had been achieved on many of its component parts was the full vision presented to the full company. By this time, individuals across the organization were ready to be believers because they had seen the success of the components and could see the strength of the synergies between components. From that time forward, the vision was communicated in many ways, from companywide meetings to visible changes in work practices.

Because concealing the strategy at first is somewhat contrary to Kotterís prescription, FAC's approach raises an interesting question. Did FAC make a mistake by not clearly communicating the vision throughout the company from the start? It is important to focus on the underlying spirit of these three factorsómotivating middle levels of the organization to build their commitment to act. At FAC, senior management believed that rolling out the vision before its components were proven would have reduced commitment rather than increased it. Perhaps the vision, although conceptually compelling to top management, required such radical changes that the more literal thinkers in middle management would have had trouble visualizing its success. Additionally, the critica enabler of TCS was an innovative information technology that had to be implemented by an IT group that was not perceived to be cutting-edge.

Kotterís final factors involve consolidating changes and institutionalizing them. Although somewhat less apparent in the write-up of the case, FAC attended to these carefully as well.

## The Second Alignment Arrow: Putting in Place the New IT Infrastructure

FACís management team recognized that better information and better information systems were critical to achieving the strategic vision; however, FAC had no substantive in-house experience in data warehousing, and its IT group was weak relative to the task at hand. Just as the management team acted swiftly when the first new marketing director could not orchestrate the needed organizational change, they also acted quickly when it became apparent that the IT group did not have the strength to orchestrate the required technology changes. Because IT was essential for success, they moved quickly to bring in NCR. During the initial versions of the VISION data warehouse, the marketing department acted as CIO, making IT strategy decisions to support the business strategy, while NCR carried them out. After a bumpy effort at knowledge transfer, FACís IT group finally took on the operation and maintenance of the warehouse.

FACís success with this approach raises an interesting question. Ross et al. (1996) argue that organizations must invest in three key IT assetsó

IT infrastructure, the relationship between business management and IT, and IT human resourcesóif they hope to continuously provide new IT applications to the organization. Ross et al. claim that when these assets are required, they cannot be created quickly. That is to say, an organization and its IT assets cannot ìturn on a dime.î However, by using outside IT consultants, FAC did quickly change. FAC's experience brings into question the necessity of investing in the three IT assets in advance of strategic initiatives.

Our answer is that FAC successfully implemented this major technology initiative in spite of its weak IT assets because it blended its own strengths with NCRís to create the needed IT asset base. First, FAC had an exceptionally clear business vision and knew the way in which IT should support it. Therefore, FAC could establish a strong business/IT relationship using a capable consulting firm like NCR. Second, the critical technical infrastructures included data warehousing hardware and software tools, and the existing business application systems. NCR could import hardware and software tools more or less in complete form, and in general, it was not necessary to modify the existing base of business application systems, but simply to draw data from them. Finally, there were two critical areas for IT skills and knowledge: (1) understanding of the existing business application systems to facilitate linking those systems to the warehouse (which IT could provide) and (2) generic data warehousing skills and knowledgeówhich NCR offered. In this way, FAC and NCR together were able to deploy a strong set of IT assets.

## The Third Alignment Arrow: A New IT Strategy

At the start of the VISION data warehouse project, FACís IT group implicitly argued that the IT strategy did not need to change. More specifically, using Henderson and Venkatraman's definition of IT strategy, the IT group felt they could implement the project relying on their existing technology scope (i.e., the Sybase technology), using their existing systemic competencies, and not changing the IT governance practices of in-house development. Even after the marketing department successfully challenged that approach, there was no apparent long-term shift. The reliance on NCR was intended to be short-term; IT felt that its people would be able to learn what they needed to know by interacting temporarily with NCR consultants. Also, there was no recognition that data warehousing would require a different approach to IT management. As late as 1998, the marketing member of the VISION leadership team worried that she did not see the needed policies, disciplines, and skills being put in place within IT.

However, as the success of the VISION project and the overall TCS strategy became apparent, and as the weakness of the existing IT management approach for ensuring its long-term success became obvious, IT put more emphasis on positioning itself to take over. More specifically, it recognized that data warehousing was a different technology that would have to be managed in a different fashion. Among other changes, IT modified the salary structure used for data warehousing positions; it made a number of critical (and expensive) hires; it took steps to keep critical people (e.g., bonuses for completion of the project, commitments for additional training); and it put in place new system development processes that ensured that changes to legacy systems not disrupt the flow of data to the warehouse.

Thus, over time, FACís IT group brought the IT strategy into reasonable alignment with its new IT infrastructure, its organizational infrastructure and processes, and the new business strategy. However, given the late start, it is reasonable to have lingering concerns about its ability to provide excellent support for data warehousing in the long term. Can IT support new business strategic efforts and stay ahead of competitors? Greater strength in the three key IT assets may be necessary to support new initiatives driven by new strategic visions; however, IT's ability to develop that level of strength will remain unknown.<sup>5</sup>

## Reflections on the Overall Strategic Alignment Model in Light of FAC

The strategic alignment model has served to focus the discussion of FACís transformation on three specific links between the four domains: business strategy to organizational infrastructure, business strategy to IT infrastructure, and IT infrastructure to IT strategy. To complete our discussion, it is appropriate to address the full model.

First, there is the question of the sustainability of FACís newly acquired competitive advantage. If NCR could build FAC a data warehouse, they also could build one for a competitor. Does that suggest that any advantage will be short lived? In this case and in general, competitive advantage is derived from a bundle of synergistic assets that provide strategic advantage in a particular situation. Any competitor that wanted to imitate FAC would have to imitate the full bundle of resources. That would mean transforming the organizational culture and infrastructure, as well as installing a data warehouse. Installing a data warehouse may be easily imitable; transforming an organization clearly is not.

In addition to the path FAC followed, Henderson and Venkatraman suggest a number of other paths through which alignment can be achieved, including what we might call a ìtechnological determinismî model in which changes to IT strategy drive a change to the IT infrastructure, which then ripples into the organizational infrastructure. Henderson and Venkatraman make no judgment about the relative difficulty of different paths. However, all paths may not be equally difficult. The experiences at FAC illustrate the challenge of making changes to the organizational infrastructure. It seems hard to imagine that changes on the IT side of the diagram could affect the organizational infrastructure in more than a haphazard, piecemeal fashion, except through changes to the business strategy first. Only a business strategy change seems likely to generate the strong business management commitment needed to meet all of Kotter's requirements for organizational transformation. This appears to limit the ability of IT groups to have major impacts on organizational performance, except (1) in support of the existing business strategy and organizational infrastructure or (2) in very tight partnership with business management.

## Conclusion

Since the 1970s, proponents of information technology have promised that management information systems (MIS) would put the right information in the right hands at the right time, and MIS would radically change the way companies are managed. Unfortunately, reality has fallen far short of the grand promises. One reason for this has been that technology had not advanced to support such ubiquitous access to information. In addition, because large-scale information access has been quite difficult historically; organizations have developed business processes and decisionmaking cultures that avoid the necessity of ìcompleteî information. Data warehouses and other advances in information technology are now solving some of the very difficult technical problems. They make it possible to organize, store, and retrieve huge volumes of information, and to select critical information for a given decision. However, before organizations can realize that ìgrand promiseî of MIS, most will have to reshape their business processes and decision-making cultures to take advantage of the technologyís new capabilities. This is a non-trivial transformation.

As this case demonstrates, FAC moved very far in that direction and reaped the benefits. Not only did the company made a major investment in information technology, but it also engineered a significant organizational transformation. Across the organization, FAC shifted the way its people think about the banking business. It implemented a new customer-centric focus and, to support that focus, it redesigned its products and distribution channels, and changed its business processes. The number of and variety of ways in which FAC took advantage of its new information asset is a testament to its truly organization-wide shift in thinking and culture. Together, these changes resulted in a significant increase in performance measures, including profitability.

The frameworks provided by Kotter and by Henderson and Venkatraman help us to understand better how FAC was able to be successful and to appreciate the immense challenge that FAC faced and solved. This case strongly suggests that it is not the technology alone that leads to significant benefits. Achieving major benefits also requires significant organizational transformation.

Perhaps it is reflective of a certain myopia within the MIS field, but what seems most striking about this case, beyond its exciting use of IT to support a major organizational turnaround, is the fact that the effort was so completely driven by the business players and the business vision. This was not a case of IS planners looking for and finding a way to use IT for competitive advantage. This was not a case of IS planners putting in place a powerful and flexible infrastructure, which was then explored until business and IS leaders discovered competitive uses for it. Rather, business leaders developed a business vision and demanded from IS the technology to support the vision. When the business leaders realized IS did not have the capability to deliver, they quickly went outside to find partners who could.

MIS programs across the country and the world have for years exhorted IS professionals to learn to think like business managers, to gain a business perspective on IT, and to bridge the gap between the technology and the business. This case raises the intriguing possibility that for the biggest impacts, business leaders may be in a far better position to bridge the gap between technology and the business than IS leaders. If business leaders understand the possible contribution of IT, and if they have a vision of the future that requires IT to support it, they will find a way to put that IT in place, regardless of the capabilities of their current IT group.

While not every business will aspire to the radical change seen at FAC, as IT capabilities increase and costs drop, and as increased competition drives more firms to rethink their strategies, the radical change experienced at FAC will become more common. Even organizations that do not desire such dramatic transformations know that many IS projects will involve considerable organization change in order to accommodate the new, highly competitive marketplace. For many firms, data warehousing provides a quantum leap in the availability and quality of information, and it may be a critical component of important organizational changes that are designed to improve bottom-line performance. For these firms as well, the lessons learned at FAC should be very useful.

## References

Chen, K. ìTechnical Note: Mathematical Properties of the Optimal Product Line Selection Problem Using Choice-Based Conjoint Analysis,î Management Science (46:2), 2000, pp. 327-333.

Darmon, R. Y. ìInternal Validity of Conjoint Analysis Under Alternative Measurement Procedures,î Journal of Business Research (46:1), 1999, pp. 67-82.

Duncan, T., and Moriarty, S. E. ìA Communication-Based Marketing Model For Managing Relationships,î Journal of Marketing (62:2), 1998, pp. 1-13.

Garbarino, E., and Johnson, M. S. ìThe Different Roles of Satisfaction, Trust, and Commitment in Customer Relationships,î Journal of Marketing (63:2), 1999, pp. 70-87.

Giddens, A. The Constitution of Society, University of California Press, Berkeley, CA, 1984.

Green, P. E., and Rao, V. E. ìConjoint Measurement for Quantifying Judgmental Data,î Journal of Marketing Research (8:3), 1971, pp. 355- 363.

Henderson, J. C., and Venkatraman, N. ìStrategic Alignment: Leveraging Information Technology for Transforming Organizations,î IBM Systems Journal (32:1), 1993, pp. 4-16.

Kotter, J. P. ìLeading Change: Why Transformation Efforts Fail,î Harvard Business Review (73:2), 1995, pp. 59-67.

Peppers, D., and Rogers, M. The One to One Future: Building Relationships One Customer at a Time, Doubleday, New York, 1993.

Porter, M. ìHow Competitive Forces Shape Strategies,î Harvard Business Review (57:2), 1979, pp. 137-145.

Prahalad, C. K. ìThe New Meaning of Quality in the Information Age,î Harvard Business Review (77:5), 1999, pp. 109-119.

Ross, J. W., Beath, C. M., and Goodhue, D. L. ìDevelop Long-Term Competitiveness Through IT Assets,î Sloan Management Review, (38:1), 1996, pp. 31-42.

Schein, E. H. Organizational Culture and Leadership (2<sup>nd</sup>ed.), Jossey-Bass Publishers, San Francisco, 1992.

Slater, D. ìLoan Star,î CIO (13:8), 2000, p. 100.

Treacy, M., and Wiersema, F. ìCustomer Intimacy and Other Value Disciplines,î Harvard Business Review (71:1), 1993, pp. 84-94.

## About the Authors

Brian L. Cooper, as the Executive Director of Marketing for First American Corporation, was instrumental in developing and implementing the Tailored Client Solutions strategy.

Hugh J. Watson is a professor of MIS and a holder of a C. Herman and Mary Virginia Terry Chair of Business Administration in the Terry College of Business at the University of Georgia. Hugh is the author of 22 books and over 100 articles, including nine in MIS Quarterly. In 1986, he was a second place winner in the SIM competition, won first place in the 1993 and 1999 competitions, and received honorable mention in the 2000 competition. Hugh is currently specializing in data warehousing and is the Senior Editor of the Journal of Data Warehousing and is a Fellow of The Data Warehousing Institute.

Barbara H. Wixom is an assistant professor of Commerce at the University of Virginiaís McIntire School of Commerce, and she received her Ph.D. in MIS from the University of Georgia. Dr. Wixom was made a Fellow of The Data Warehousing Institute for her research in data warehousing, and she has published in journals that include Information Systems Research, Communications of the ACM, Journal of Data Warehousing, and Information Systems Management. In 1999, she won first place in the SIM competition, and she received honorable mention in the 2000 competition. Dr. Wixom's research interests include the use of IT to support organizational decision making, IS success, and the benefits of IT.

Dale L. Goodhue is an associate professor of MIS at the University of Georgiaís Terry College of Business. He received his Ph.D. in MIS from MIT, and has published in Management Science, MIS Quarterly, Decision Sciences, Sloan Management Review and other journals. His research interests include measuring the impact of information systems, the impact of task-technology fit on individual performance, and the management of data and other IS infrastructures/resources.
