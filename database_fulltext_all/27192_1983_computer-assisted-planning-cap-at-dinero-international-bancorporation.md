---
otero_id: 27192
otero_key: "FPR8ZHXJ"
title: "Computer Assisted Planning (CAP) at Dinero International Bancorporation*"
authors: "James R. Doyle; Jack D. Becker"
year: "1983"
journal: "MIS Quarterly"
doi: "10.2307/249055"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Computer Assisted Planning (CAP) at Dinero International Bancorporation
Author(s): James R. Doyle and Jack D. Becker
Source: MIS Quarterly, Vol. 7, No. 3 (Sep., 1983), pp. 33-46
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/249055

Accessed: 09/05/2014 08:02

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Computer Assisted Planning (CAP) at Dinero International Bancorporation\*

By: James R. Doyle
Jack D. Becker

## Abstract

This article describes three inter-related computer based systems that were designed and developed to assist with the implementation of a major long-term strategic planning effort at a multi-billion dollar bank holding company, Dinero International Bancorporation, (DIB). New strategies at DIB included: (1) a major redirection of its marketing efforts to a multi-state mid-western region in the U.S., and (2) to correspond with this new marketing direction, a major change in the bank's image, including a name change.

The first system, the Regional Banking Information System (REBIS) was designed to extract key information from a 1G (gigabyte) bank database. With REBIS, DIB was able to monitor the level of banking activity in a designated region and to measure the performance and level of competition of over 1,000 selected banks with operations in this region.

A second system, the SAS/Dunn and Bradstreet (D & B) system, was designed to analyze and plot key financial characteristics (sales, debt, etc.) of the more than 20,000 selected companies also in the region. Information pertaining to business activity by industry was plotted on maps of the region in order to identify the most desirable marketing opportunities.

Finally, the third system, AUTOTRAC, an automated project tracking system, was used to monitor and control the progress of the DIB name change plan.

Keywords: Financial information systems, banking information systems, strategic planning, strategic information

ACM Categories: 3.3, 3.5, 4.9

## Introduction

The United States banking system in recent years has experienced a number of dramatic changes. Record high interest rates, an unstable economy, and new legislation have each presented new and difficult challenges to the banking executives of both large and small banks $[1, 11, 12, 15]$ . In response to these changes, Dinero International Bancorporation (DIB), a multi-billion dollar bank holding company and its lead bank Dinero Bank (DB) formulated new strategies for the 1980s. This article will discuss the nature of these new strategies and how computers were used by management to refine a portion of these strategies and to aid in their implementation.

Although there has been a growing awareness on the part of corporate managers for relatively sophisticated and automated strategic planning systems $[10]$ , there were relatively few examples in the literature of how these systems were developed and how they were integrated into the corporate strategic planning process $[7]$ . Two of the systems, developed by DIB, were used by top-level management as part of the annual long-range planning process to scan the firm's competitive environment for new opportunities, as well as to avoid potential problems. These environmental scans were performed by an outside consulting firm on several large external databases according to a relatively focused set of predefined goals. From these annual environmental scans, the long-term strategies were refined and short-term objectives were established. A third system, called AUTOTRAC, was used by management at several levels in the firm to monitor and control the progress of both strategic and tactical plans.

## Background

The DIB holding company included over fifteen member banks, all located in one state, as well as a trust operation. The largest member bank was

DB which accounted for approximately 70% of the holding company's assets.

During the decade of the 1970s, DIB pursued the following strategies: (1) acquiring affiliate banks within its state of operation; (2) expanding its less traditional consumer business (e.g., personal bankers, automated teller machines, and savings promotion), while at the same time more aggressively expanding their primary customer base of commercial and industrial accounts, especially in the area of cash management; (3) expanding its correspondent banking operations to well over 1,000 correspondent banks; (4) expanding its international operations to include two foreign-based offices; (5) moving into the agricultural lending business; and (6) opening a domestic loan production office outside their primary service area in the mid 1970s.

Given the increasing competition among banking organizations, shifts in population location, movement of business firms to new locations, and development of new businesses outside of DIB's traditional marketing area, DIB's management recognized that new strategies would be necessary for the 1980s. In 1980, a task force composed of a group of individuals from various departments of DB and several consultants selected by senior management began an extensive examination of DIB's entire banking operations. As a result of this study, a new long-term strategic plan for DIB was formulated.

## Goals and Objectives

The overall goal of DIB was to become a pre-eminent regional banking organization. In the early 1980s DIB began implementing a number of strategic plans relevant to this goal. Among these were the following:

1. To create a strong regional image, DIB would increase its presence in selected regional markets as well as its present state of operation.

2. DIB would establish separate planning units for each market.

3. Each division in the lead bank, the trust company and other affiliate and support units, would define their own plans within the context of overall corporate strategies and objectives.

4. In order to build market presence, DIB changed its name to one that conveyed the basic strategy of it becoming a pre-eminant regional banking organization. In addition, the names of each holding company bank would also be changed to a common name along with a location designation.

## Criteria for Strategic Information

As King [10] observed “. . . for a strategic information system to be cost-effective, it must be developed according to specified criteria which ensure its relevance and usefulness.” They are:

1. a recognition that much of the new strategic information will emanate from new external sources of data,

2. the strategic data must be collected and evaluated for some specific strategic purpose, and

3. the strategic information supplied must be integrated into a regular (e.g., annual) planning cycle of the firm.

All of these criteria were satisfied by the planning systems installed at DIB and are discussed below.

## Computer Assistance to Planning and Implementation

It became obvious to the planners at DIB that a strategic plan of this magnitude would require some form of computer based information system. Detailed tactical planning at the regional level would require enormous volumes of data processing to assess the strengths and weaknesses of other financial institutions in the region as well as the location and size of different market segments in this region. In order to assess the financial characteristics of the new regional marketplace, two large external databases were utilized: (1) the Federal Reserve Bank/Federal Deposit Insurance Corporation (FRB/FDIC) Report of Condition (RCON) and Report of Income and Dividends (RIAD) databases, and (2) the Dun and Bradstreet (D & B) Commercial and Industrial Statistics database.

## Data sources

The FRB/FDIC and RIAD databases contained over 500 financial variables (balance sheet and income statement data) for every insured bank in the U.S. (or about 14,000 banks). Of these, approximately 8,000 were located in the study region. The bank balance sheet data (RCON) was available on a quarterly basis, while the income statement data (RIAD) was available on a semi-annual basis. Five years of data were actually used or about one billion characters.

The D & B database consisted of demographic, industrial classification and operational and financial data (e.g., number of employees, revenues, debts) for the approximately 25,000 companies over \$10 million in revenues during 1979 within the target region (about 2.5 million characters).

## Computer information systems

In order to process the over one billion characters the databases contain, two new computer information systems were developed:

1. The Regional Banking Information System (REBIS) — REBIS was designed to permit easy comparison of key financial growth and performance characteristics of selected banks.

2. The SASGRAPH CALCOMP/D & B (SAS/D & B) computer graphics system — The SAS/D & B system was designed to display commercial and industry activity of selected industries on color-coded regional maps.

Finally, a third computer based system, AUTOTRAC (an automated project tracking system) which had been in use at the lead bank since 1978, was used to monitor and control the planning and implementation of the name change project [2, 3].

## The Regional Banking Information System (REBIS)

A major marketing consideration for any financial institution, but especially for banks, is the degree of competition it faces among other bank organizations. In banking there are two important dimensions of the competitive analysis that must be determined:

1. the geographical area in which the competition will be taking place, and

2. the type of banks and banking services for which the organization will be competing.

With regard to geographical area, the predominant thinking at DIB was that interstate banking would soon become a reality. In addition, extensive primary and secondary research presented to senior management indicated that the future thrust of DIB should be directed toward a regional approach — regional companies, regional organization, and regional competition. Thus, senior management agreed that a regional approach should be adopted and a multi-state regional area was identified, based upon research and management's perception of its regional market.

Within this region it then became necessary to identify the other banks and bank holding companies with which DIB felt it would be competing. In bank marketing analysis not all banks or bank holding companies in the same area can be considered competitive due to different market directions (consumer versus wholesale banks, strong auto lenders, weak credit card holders, etc.). These directions can generally be inferred by the size of various financial characteristics (assets, deposits, etc.). Thus, a set of criteria was developed to enable a useful comparison of banks within the region.

The next stage of this analysis was to determine the most effective means of competing in this market place. In this regard DIB had several possible alternatives:

1. form new banks,

2. establish representative or so-called loan production offices, or

3. acquire existing banks or bank holding companies [4, 5].

## The development of the automated system — REBIS

Taking all of these factors into account, the Regional Banking Information System (REBIS) was designed to permit financial and geographical analysis of bank data. The REBIS system identified well over 1,000 banks in the target market area that: (1) would be potential customers for correspondent banking services; or (2) would be potential candidates for acquisitions, in the event that interstate banking be approved in the 1980s; or (3) would be potential competitors within the regional and/or local market area [6]. (See Figure 1 for a sample report).

The detailed design of REBIS was conducted in the following stages. First, the available data sources were identified (FRB/FDIC, RCON, and RIAD databases). Next, a supplier of these external data sources, an outside consultant, was contacted to assist in the design of the system. Since there were over 8,000 banks in the target region and since most of these would neither be considered competition nor possible acquisition candidates, a list of key selection criteria was formulated.

Working primarily with representatives of senior management (user coordinators [9]), the task force determined that the appropriate selection criteria fell into four categories [8, 13]:

1. Bank identification. A specific name and identification number, of course, but, also whether a bank was a member of a holding company.

2. Location. This included the city, state, county, Standard Metropolitan Statistical Area (SMSA), and Federal Reserve District in which a bank was located.

3. Type and level of activity. The specific types and levels of activities were chosen by senior management to allow competitive comparisons, e.g., equity capital, bankers' acceptances, total assets and commercial and industrial loans; commercial and industrial loans are the primary source of loan activity and earnings for all banks in general and those banks primarily competitive with DIB in particular, while bankers' acceptances provide a measure of trading activity.

4. Performance. Leverage, net profits, return on assets, and a loan loss ratio were the measures chosen.

Although initially there were only eight specific performance characteristics chosen for inclusion in the REBIS reporting system, the system was designed to easily accommodate additional financial characteristics should management desire them.

A final dimension of the competitive comparisons involved the analysis of performance over time. Because of fluctuations during a year and the nature of bank reporting, it was decided that average quarterly balances provided the most accurate measure of financial performance. For example, in Figure 1, the annualized average growth in average total assets was 19.7%, with 1981 average total assets computed at \$4.124 billion and year-end total assets reported at \$4.612 billion, almost a \$500 million difference.

## The use of REBIS

The first use of REBIS in early 1980 was to analyze competitive activity within the study region and to evaluate future strategies. Since this initial use of year-end 1979 data, senior management has requested complete updates of the REBIS system for 1980, 1981, and 1982. In addition to the report shown in Figure 1, which was the primary analytical report, a variety of summary reports were prepared for senior management to aid in the analysis and monitoring of banking competition and performance in the initial study region as well as other designated regions. For example, reports were provided to rank banks and bank holding companies in specific geographic areas by size, holding company, and return on assets. Bank calling officers from a number of different divisions were also provided with copies of selected REBIS reports to assist them with evaluating specific banks relative to their sales efforts and with developing their marketing services.

<table><tr><td colspan="12">Regional Banking Information System</td></tr><tr><td colspan="12">REBIS11H05/07/82</td></tr><tr><td colspan="12">Holding company # 1st NB Of Kaanapali Kaanapali, IA 0016 09 5120 053 County #(FIPS code)</td></tr><tr><td>Cert No: 05199 Bank ID: 09274037</td><td>As Of — 12/31/81 ($000)</td><td>1977 Balance ($000)</td><td>Annual Change 77-78 (%)</td><td>1978 Balance ($000)</td><td>Annual Change 78-79 (%)</td><td>1979 Balance ($000)</td><td>Annual Change 79-80 (%)</td><td>1980 Balance ($000)</td><td>Annual Change 80-81 (%)</td><td>1981 Balance ($000)</td><td>Annualized Average Growth (%)</td></tr><tr><td>Equity Capital (1)</td><td>213,949</td><td>143,802</td><td>7.0</td><td>153,937</td><td>9.9</td><td>169.198</td><td>10.0</td><td>186,060</td><td>10.0</td><td>204,628</td><td>9.2</td></tr><tr><td>Total Assets (1)</td><td>4,612,549</td><td>2,012,787</td><td>17.6</td><td>2,367,586</td><td>23.8</td><td>2,930,230</td><td>18.5</td><td>3,470,994</td><td>18.8</td><td>4,124,725</td><td>19.7</td></tr><tr><td>Leverage (TA/EC)</td><td>22</td><td>14</td><td></td><td>15</td><td></td><td>17</td><td></td><td>19</td><td></td><td>20</td><td></td></tr><tr><td>Net Profits</td><td>32,609</td><td>17,331</td><td>28.1</td><td>22,208</td><td>13.3</td><td>25,157</td><td>12.6</td><td>28,332</td><td>15.1</td><td>32,609</td><td>17.3</td></tr><tr><td>Return On Assets (%*100)</td><td>71</td><td>86</td><td></td><td>93</td><td></td><td>85</td><td></td><td>81</td><td></td><td>79</td><td></td></tr><tr><td>Comm. and Indust. Loans (1)</td><td>1,342,653</td><td>475,614</td><td>18.1</td><td>561,765</td><td>28.5</td><td>721,655</td><td>17.9</td><td>851,184</td><td>32.6</td><td>1,128,445</td><td>24.3</td></tr><tr><td>Loan Loss Ratio (2:%*100)</td><td>43</td><td>80</td><td></td><td>6</td><td></td><td>5</td><td></td><td>49</td><td></td><td>43</td><td></td></tr><tr><td>Bankers Accepts (1) (3)</td><td>300,077</td><td>26,498</td><td>40.9</td><td>37,346</td><td>176.8</td><td>103,362</td><td>76.9</td><td>182,872</td><td>31.7</td><td>240,821</td><td>81.6</td></tr></table>

Figure 1. Sample Regional Banking Information System (REBIS) Report

## The benefits of REBIS

Without the REBIS reporting system, senior management would have found it virtually impossible to monitor and evaluate the competitive activity in a multi-state region. Although most of the benefits from REBIS were intangible, the frequent use of these reports by both senior management and calling officers was an indirect measure of their benefits. In addition, tangible evidence of the regional expansion efforts have continued during the early 1980s with the addition of four new domestic loan production offices in four other states.

## The SAS/D & B System

A major contributor to the earnings of banking organizations such as DIB are commercial and industrial loans. As with the different levels of banks and their marketing directions, there are also different types and levels of businesses, e.g., Fortune 500, chemical industry, and transportation. Following the approach used in constructing REBIS, senior management targeted the same initial multi-state study region for investigating the marketing direction for increasing their commercial and industrial loan activity. However, where REBIS identified the bank with which DIB would compete, the SAS/D & B system was used to identify those businesses with which DIB would be attempting to establish a relationship.

As a first step, extensive research presented to senior management indicated that new marketing efforts should be directed toward middle market companies (\$5-200 million sales). In conjunction with the Dun and Bradstreet organization, DIB constructed a database that contained all businesses within certain sales ranges and selected information for each business. Thus, for the over 20,000 identified businesses in the region, each was first identified by a series of types, e.g., real estate or transportation, and then individual business characteristics were identified, e.g., total debt or cash.

## The development of the automated SAS/D & B system

Given the enormous volume of information available, senior management recognized that it needed to be able to display the data in some aggregate form so that meaningful conclusions could be derived. The SAS/D & B system was designed for this purpose. In particular, although senior management felt that the D & B data provided a sufficient identification on a business by business basis, some means for viewing the distribution of these companies in a concise manner was needed in order to conduct any analyses. Maps were felt to be the best method for viewing this information. Maps with data displays had been previously constructed, but these had been manually prepared and proved to be time consuming and expensive, while they also showed that they could not adequately display the significant volume of D & B information. Computer mapping techniques were proposed and accepted by management. The mapping techniques consisted of using the Statistical Analysis System (SAS) to construct the statistical databases, a CALPREP/CALFORM mapping routine, and finally, plotting the data on a CALCOMP model 1051. Maps were created on a county by county basis for states within the study region which presented the location of companies in an aggregate form for seven different categories, e.g., cash, number of companies (see Figure 2).

## The use of the SAS/D & B system

Over 200 maps were produced along with copies, and were first used by the task force to analyze specific business characteristics, i.e., locational patterns by industry type. After initial analysis, the maps were distributed to various department heads, who were concerned with a specific industry or location that had been plotted. The department head then was able to plan a marketing strategy with the group using the maps as a basis. The first set of maps led to various conclusions in terms of patterns of concentration by state and counties within states. Based upon the task force's conclusions, maps were used for presentation to senior management in terms of making recommendations for further marketing efforts.

![](/api/attachments/FPR8ZHXJ/fulltext/images/0093cab592e0677a95247276cab1797311d8b21eec66f101ae4088707d1aca1d.jpg)  
\$40 million or more sales.

Figure 2. Sample Study Region by County Extractive Industries

MIS Quarterly/September 1983

Based upon senior management's direction, another series of maps was produced which gave greater detail by company type and location. In this regard businesses were plotted by the type of information available, i.e., debt, and by different sales levels.

## The benefits of the SAS/D & B system

The SAS/D & B system provided concise analysis for planning overall organization strategy while also allowing individual units of organizations to determine effective marketing plans. Based in part on this analysis of geographical concentration, the four regional offices were opened in the early 1980s. A tangible indication of the usefulness of the SAS/D & B system was that DIB's commercial loans increased 29% in 1981 versus a total increase in the composite loan portfolio of only 22%. It may be too early to determine to what extent these results were attributable to the recent regional planning efforts.

## The Autotrac System

The Automated Project Tracking System (AUTOTRAC) was designed in 1978 [2, 3]. AUTOTRAC is an easy to update and maintain automated system which monitors the progress of projects performed within the organization in terms of those departments and individuals responsible for their completion. With regard to the DIB name change plan, from 300-400 projects were being monitored at any given time. More than sixty managers and fifty divisions, including the Chairman of the Board of DIB, have had projects included in the AUTOTRAC system (see Figure 3). Essentially, as Figure 3 indicates, the AUTOTRAC reports contained a project description, that phase of the plan which was being implemented, which department and individual requested the project, who was responsible for a project's completion, and the progress of its implementation, i.e., starting date, due date, whether completed, and on going. The AUTOTRAC system does not attempt to capture all of the detailed and complex interrelationships among projects that critical path analysis or PERT would attempt, but rather its purpose is to provide a simple time and responsibility comparison of projects on a regular periodic basis, usually weekly. The ultimate goal of the system was to provide management with a tool that would help monitor and control corporate-wide project completions and would assist management decision making at all management levels (corporate wide, division or department, and individual manager).

The main purpose of AUTOTRAC was to monitor and control the implementation phase of the planning process. Senior management identified DIB's various levels of goals and, then, along with management, designated various objectives to achieve these goals. AUTOTRAC listed these objectives throughout the corporation and tracked their implementation as well as any modification or updating to the planning process.

## The development of the AUTOTRAC system

AUTOTRAC was specially tailored for DIB through the combined efforts of an outside consultant and the Director of Marketing (DB) to track the progress of marketing projects. When the Director of Marketing became the Director of Planning, DIB, the system was modified to track corporate-wide project completions. The DIB name change became just another application of the simple, yet flexible AUTOTRAC System. When the name change project concluded, another version of AUTOTRAC was initiated to begin tracking the progress of DIB's new strategies at both the lead bank, the affiliate banks, the trust company, and the regional offices (see Figure 4). As Figure 4 shows, the modified affiliate AUTOTRAC report includes an extra level of identification at the bank level, as well as a means of including amount of money budgeted for each project.

## The benefits of the AUTOTRAC system

AUTOTRAC was designed to be incorporated across all levels of an organization. The authors' continuing relationship with DIB has shown that management, employees and the entire organization have benefited from the system. While the direct financial benefits of AUTOTRAC to DIB or DB are at this writing difficult to measure, several intangible benefits have already been observed. These benefits can be seen as chiefly accruing in the following areas: (1) management benefits, (2) employee benefits, and (3) organizational benefits. Each of these will be discussed below.

<table><tr><td colspan="9">For: Becker, Jack D.Dinero International BancorporationAUTOTRAC — Responsible Party ReportJuly 6, 1982</td></tr><tr><td>Project Number</td><td>Request Date</td><td>Responsible Department — Initials</td><td>Project Description</td><td>Responsible Party — Name</td><td>Planned Starting Date</td><td>Due Date</td><td>C C</td><td>Remarks</td></tr><tr><td>1037-0</td><td>4/20/82</td><td>Marketing JDB</td><td>Write employees presentation.</td><td>Becker, Jack D.</td><td>4/15/82</td><td>6/10/82</td><td>C</td><td>*Completed*</td></tr><tr><td>1118-1</td><td>5/26/82</td><td>Marketing JDB</td><td>Write affiliate check list.</td><td>Becker, Jack D.</td><td>6/1/82</td><td>6/15/82</td><td>C</td><td>*Completed*</td></tr><tr><td>1118-2</td><td>5/26/82</td><td>Marketing JDB</td><td>Appoint affiliate manager.</td><td>Becker, Jack D.</td><td>6/1/82</td><td>6/15/82</td><td>C</td><td>*Completed*</td></tr><tr><td>1135-0</td><td>6/10/82</td><td>Marketing JDB</td><td>Write JRD employee speech.</td><td>Becker, Jack D.</td><td>6/10/82</td><td>6/20/82</td><td>C</td><td>*Completed*</td></tr><tr><td>1136-0</td><td>6/10/82</td><td>Marketing JDB</td><td>Write JPM employee speech.</td><td>Becker, Jack D.</td><td>6/10/82</td><td>6/20/82</td><td>C</td><td>*Completed*</td></tr><tr><td>1092-0</td><td>4/20/82</td><td>Executive JDB</td><td>Give sign co. the approved graphics and have them start making panels for approval.</td><td>Becker, Jack D.</td><td>6/1/82</td><td>7/1/82</td><td></td><td></td></tr><tr><td>1117-0</td><td>4/20/82</td><td>Marketing JDB</td><td>Meet special with L. River to determine what changes or impact, if any, on DD systems.</td><td>Becker, Jack D.</td><td>5/1/81</td><td>7/1/81</td><td>C</td><td>*Completed*</td></tr></table>

Figure 3. Sample AUTOTRAC Report

<table><tr><td colspan="10">03/02/82 Due Date OrderFor: Doyle, James R.Dinero International BancorporationAUTOTRAC — Affiliate Project Control SystemPeriod Ending: 02/26/82</td></tr><tr><td>Project Number</td><td>Request Date</td><td colspan="2">Requestor Bank-Dept — Initials</td><td>Project Type</td><td>Project Description</td><td>Responsible Bank-Dept — Initials</td><td>Due Date</td><td>Budget Code — Amount</td><td>Remarks</td></tr><tr><td>1039-00</td><td>1/04/82</td><td>Papeg Adver</td><td>WS</td><td>P005</td><td>Testimonial advertising</td><td>DBMIN Marketing JDB</td><td>3/01/82</td><td>215-$25000</td><td></td></tr><tr><td>1050-00</td><td>1/04/82</td><td>Chist Retail</td><td>TA</td><td>P005</td><td>Retail business seminars.</td><td>DBMIN Marketing JDB</td><td>3/01/82</td><td>811-$ 5000</td><td></td></tr><tr><td>1067-00</td><td>1/04/82</td><td>Dolum personnel</td><td>BR</td><td>P005</td><td>Employee incentive program.</td><td>DBMIN Marketing JDB</td><td>3/01/82</td><td>-$ 0</td><td>On-Going</td></tr><tr><td>1005-00</td><td>1/04/82</td><td>Trans marketing</td><td>SB</td><td>P005</td><td>Seminars for retail business-obtain speakers.</td><td>DBMIN Marketing JDB</td><td>3/31/82</td><td>-$ 0</td><td></td></tr><tr><td>1012-00</td><td>1/04/82</td><td>Trans marketing</td><td>SB</td><td>PRPGM</td><td>P.R. Image program</td><td>DBMIN Marketing JDB</td><td>4/01/82</td><td>385-$15000</td><td></td></tr></table>

Figure 4. Sample AUTOTRAC Affiliate Report

## Management Benefits

The AUTOTRAC system benefited the management of DIB at all levels immediately by providing a corporate-wide system that could accurately monitor the progress of marketing and corporate plans. This system also benefited management by requiring them to more carefully define their plans and identify those individuals who were responsible for their implementation. In addition, AUTOTRAC was able to provide all levels of management with a clearer perception of the overall corporate planning process, as well as the status of their projects and plans.

## Employee Benefits

Employees at first viewed AUTOTRAC somewhat skeptically as “big brother,” but after a number of informal training tutorials they were able to better recognize and appreciate their overall contribution to the functioning of DIB. Employees benefited by recognizing how important it was for them and management to work together as a team for the organization’s benefit. Employees also benefited from AUTOTRAC by being able to relate their projects to other employee’s projects and to broader corporate goals. Finally, at a more practical level, the system provided employees with a “Things I Must Do” scratch pad that was a benefit in their day-to-day work.

## Organizational Benefits

Overall AUTOTRAC benefited the corporation by encouraging a more participatory management approach to planning and thereby helping to more clearly define both the goals of the organization and the roles of management and employees. AUTOTRAC, in essence, is an automated form of management by objectives (MBO). Thus, for those organizations that practice MBO, AUTOTRAC would blend very favorably with their existing management systems. However, due to its design flexibility AUTOTRAC may be tailored to the prevailing management style within an organization.

## Impact of Automated Systems on the Planning Process

The usefulness of all three automated systems has been confirmed in part by the frequency and variety of reports which have been requested by DIB management. The REBIS system, which was first used with year-end 1979 data, has been updated for year-end 1980, 1981, and 1982 financial data. To date, more than a dozen different types of reports have been produced by the REBIS system. The SAS/D & B system has been used to produce over 200 individual graphs for planning and presentation purposes. The AUTOTRAC system was used to monitor the DIB name change plan for over one year and was later enhanced to monitor the progress of all affiliate banks and units responsible for implementing the various strategic and tactical planning efforts.

Although it was difficult to impute any direct financial impacts to any of these automated planning tools, it was possible to observe DIB's expansion into four new regional loan production offices and a significant increase in commercial loan activity.

## Future Directions

As has been noted throughout this article, all three systems have been used extensively. Consequently there have been on-going requirements to modify or enhance each of the three systems. Several of the possible directions that each of the systems may be evolving will now be discussed.

## REBIS's future

Since its initial development the REBIS system was modified due to a variety of learning curve experiences. For example, (1) while states were selected as the initial geographic unit of study, analyses indicated that Standard Metropolitan Statistical Areas (SMSA) were a better unit for relevant analysis; (2) certain selected financial characteristics were changed, added, or deleted as the study progressed; and finally, (3) the initial study region was changed to include additional market areas, when desired growth objectives could not be attained within the initial study area.

Senior management has recently expressed the desire to be able to query the REBIS database in an interactive mode. The query capabilities would include not only such common features as selection, sorting, and counting, but in addition, would include such features as color graphic displays with both the traditional line graph and bar chart options, as well as the color geographic-area mapping initially produced. This type of evolutionary transition from batch-oriented management information systems to more user-oriented interactive decision support systems has been recently noted in a wide assortment of applications $[14]$ . Finally, in an attempt to capture a more accurate assessment of the rapidly changing competitive environment for banks, the REBIS reporting system will be expanded to include other financial institutions within a targeted region, such as savings and loan associations and credit unions.

## SAS/D & B system's future

When viewed at the county level, the SAS/D & B maps permitted only a generalized picture of business concentration. For more in-depth analysis, calling officers would need a finer breakdown of businesses within a metropolitan area. As more expertise is acquired, detailed local maps could be provided, at the census tract or street block level.

Another future direction of the SAS/D & B system would be in displaying and analyzing the growth patterns of selected businesses during a specified time period as well as modeling growth projections.

Just as the REBIS data may be entered into the SAS graphing system, so also might regional census data be entered and displayed on color-highlighted area maps. With this data DIB would be able to more effectively integrate the analysis of individual customer trends into the regional competitive market analysis.

## AUTOTRAC's future

The future enhancements of AUTOTRAC at DIB would include:

1. implementing the system at the corporate level in such a way that the plans of DIB's major subunit, (i.e., DB, the affiliate banks, the trust company and regional offices) are tied to corporate-wide plans and objectives;

then,

2. implementing AUTOTRAC at each subunit so that the activities within the subunit may be related to individual subunit plans; and

finally,

3. using AUTOTRAC more to monitor not only the times of project completions, but also as a tool for comparing the actual costs and budgeted costs for those project completions.

Regardless of the type of enhancements or the level of the organization at which AUTOTRAC was incorporated, it was discovered that the only way for this type of system to succeed was to very carefully and intimately introduce the system to each user of the system. Without consensus AUTOTRAC will not function at its optimal level.

## Summary

This article attempted to show how a banking organization was able to use three computed automated systems to assist both senior management and middle management in the development of a strategy for expansion into a multi-state regional market place. The first system, REBIS, was shown to be an effective tool, used by both senior management and bank calling officers, for evaluating the level of competitive activity from other financial institutions (namely, other banks) within the targeted region.

The second system, the SAS/D & B system, provided senior management and various divisional units with a means of examining patterns of commercial and industrial business activities on a regional map. Hence, generally believed hypotheses of business expansion could be objectively evaluated.

The last system, AUTOTRAC, was shown to be a flexible and useful tool for tracking project completions at both corporate-wide and individual bank subunit levels. The versatility of the project tracking system was illustrated by examining its use in the recent name change project at DIB, which encompassed all subunits of the bank as well as a number of outside organizations. Individually each of these systems effectively supported a particular dimension of an overall corporate-wide goal to be a pre-eminent regional banking organization.

## References

[1] "Bank Scoreboard: How the Top 200 Banks Performed in 1981," Business Week, April 12, 1982, pp. 87-102.

[2] Becker, J.D. and Doyle, J.R. “An Automated Project Tracking System — A Case Study,” Proceedings of the Twelfth Annual Hawaii International Conference on System Sciences, Volume II, W. Remus and R.H. Sprague, eds., Western Periodicals Co., January 1979, North Hollywood, California, pp. 1-10.

[3] Becker, J.D. and Doyle, J.R. "AUTOTRAC — A Decision Support System for Corporate Planning," Applied Systems and Cybernetics — Proceedings of the International Congress on Applied Systems Research and Cybernetics, Pergamon Press, New York, New York, 1981, pp. 909-915.

[4] Bradley, J.W. and Korn, D.H. "The Changing Role of Acquisitions," The Journal of Business Strategy, Volume 2, Number 4, Spring 1982, pp. 30-42.

[5] Curry, T.J. "The Pre-Acquisition Characteristics of Banks Acquired by Multibank Holding Companies," Journal of Bank Research, Volume 12, Number 2, Summer 1981, pp. 82-89.

[6] Doyle, J.R. and Becker, J.D. "Competitive Position and Bank Planning," University of Missouri, St. Louis, Working Paper, presented at Joint National Meeting of

TIMS and ORSA, St. Louis, Missouri, May 1978.

[7] Fahey, L., King, W.R., and Narayanan, V.K. "Environmental Scanning and Forecasting in Strategic Planning — The State of the Art," Long Range Planning, Volume 14, Number 1, February 1981, pp. 32-39.

[8] Ford, W.F. and Olson, D.A. "How 1,000 High-performance Banks Weathered the Recent Recession," Banking, Volume 70, Number 4, April 1978, pp. 36-48.

[9] Kaiser, K.M. and King, W.R. “The Manager-Analyst Interface in Systems Development,” MIS Quarterly, Volume 6, Number 1, March 1982, pp. 49-59.

[10] King, W.R. “Information for Strategic Planning: An Analysis,” Information and Management, Volume 1, Number 2, June 1978, pp. 59-66.

[11] “The New Banking Forces New Strategies,” Business Week, July 13, 1981, pp. 56-61.

[12] "New Era for Banking," Business Week, April 21, 1980, pp. 92-118.

[13] Sapp, R.W. "Banks Look Ahead — A Survey of Bank Planning; The Magazine of Bank Administration, Volume 56, Number 7, July 1980, pp. 33-40.

[14] Sprague, R.H., Jr. “A Framework for the Development of Decision Support Systems,” MIS Quarterly, Volume 4, Number 4, December 1980, pp. 2-26.

[15] "Wholesale Banking's New Hard Sell," Business Week, April 13, 1981, pp. 82-86.

## About the Authors

James R. Doyle is President of James R. Doyle, Associates. He received his graduate degree in Planning and Economics from Southern Illinois University. Mr. Doyle publishes a variety of financial information on a nationwide basis, and also serves as a consultant to various financial institutions, and public and private organizations. He has published articles in professional journals and the book Applied Systems and Cybernetics (Pergamon Press, 1981). He has also served on the faculty of St. Louis University.

MIS Quarterly/September 1983 45

Jack D. Becker is Assistant Professor of Management Information Systems at the University of Missouri-St. Louis. He received his Ph.D. in Business Administration from Washington University. He has published numerous articles in professional journals and proceedings. His teaching interests include systems analysis and design and financial information systems. Dr. Becker has served as a consultant to numerous banks, public and private corporations, government agencies, and non-profit organizations.
