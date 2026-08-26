---
otero_id: 27292
otero_key: "BS6UNPRJ"
title: "The Application Profile"
authors: "John L. Batiste"
year: "1986"
journal: "MIS Quarterly"
doi: "10.2307/249251"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
The Application Profile
Author(s): John L. Batiste
Source: MIS Quarterly, Vol. 10, No. 3 (Sep., 1986), pp. 207-213
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/249251

Accessed: 08/05/2014 23:03

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# The Application Profile

By: John L. Batiste
A.O. Smith Data Systems, Inc.
8901 North Kildeer Court
Brown Deer, Wisconsin

## Abstract

MIS performance evaluation generally includes consideration of issues such as timeliness, efficiency, effectiveness, and user satisfaction. Much of this can be subjective. For individual applications more objective criteria are necessary to monitor operational occurrences that affect overall performance.

This article discusses measuring a system's performance with an application profile, describes the components that make up a profile spreadsheet, and highlights benefits derived from its use as a management tool.

Keyword: Application profile, performance measurement, information systems management, control mechanism

ACM Categories: D.2.9, K.6.1, K.6.2, K.6.3, K.6.4

## Introduction

The A.O. Smith Corporation is a diversified manufacturer and supplier of products and services for the transportation, water heating, water supply, air conditioning, refrigeration, heating, agricultural, financial, chemical, power generation, waste water, and petroleum industries. As one of the 500 largest publicly owned manufacturing corporations in the United States, we employ approximately 10,000 persons. Our products are manufactured at 26 plants in the U.S. and abroad.

The A.O. Smith companies and A.O. Smith Data Systems, Inc. (DSI) work together in customer/vendor relationships. DSI charges for products and services based on resources used. Performance management is a critical element in maintaining our intercompany customer/vendor satisfaction.

Performance measurement is gaining attention in the MIS community. McFarlan and McKenney [1] address this and other topics as matters for management control. Efficiency, effectiveness, timeliness, and user satisfaction are the focus of many evaluations. These performance dimensions reflect management practices in planning, project management, operations management, costing policy, and MIS organization; they tend to be somewhat subjective. While many techniques for effective operations management exist, little has been written on objective how-to's for the application manager.

Aside from traditional goals of minimum down time, fast response, accurate data, and correct functional processing, the complete definition of a performance standard varies. Differences in product, sales volume, corporate culture, and software make it virtually impossible to compare, for example, the order entry system from company A to that of company B. For that matter, direct comparisons of similar systems in separate divisions of the same corporation may not be realistic. This article suggests that for each application, the performance standard is the application itself.

Our technique for determining a system's performance is to develop a profile of the application environment and operating characteristics. This concept is not new. It has been applied to other business areas for many years and has generally produced an acceptable control mechanism. The profile is a spreadsheet model of the system that includes environmental data about the level of business activity, significant information processing factors, and the resulting MIS costs.

As an example, a company with a shipping history of two units per order will face a dilemma if sales drop to one unit per order. Revenues are halved, but the cost of computing remains unchanged. It requires the same amount of computer resource to process one unit per order as it does for two units per order. Alternatively, if a two units per order for 100 orders history shifts to one unit per order for 200 orders, computing requirements increase with no change in sales volume.

MIS operations are more complicated than this simple example. Application performance is affected by business issues like seasonality, market promotions, new product releases, production rates or schedules, and so forth, as well as by sales mix and volume. If it is necessary to manage performance for this moving target, then a mechanism that is sensitive to business variations must be employed. In a profile, measures of variation are identified as business volume indicators.

The effect of business change on application software can be viewed in terms of information demands placed on a system. Information processing measures is the name given to this segment. Here, we are concerned with database size and makeup, the transaction load resulting from the business volume, and specific or unique run-time characteristics in the application.

Cost performance is affected by software architecture, business volume and mix, prevailing MIS prices, technology employed, and many other factors. Software operating costs do not necessarily correlate with corporate sales figures. The “bottom line” is recorded in the MIS costs segment.

When combined on a spreadsheet, these three segments provide insights into performance pressures exerted on an application and help managers understand and operate the software as it reacts to those demands.

## Profile Composition

## Business Volume Indicators

Business volume indicators are determined by the application and, to a certain extent, by the characteristics of the company's industry or products. They are chosen by considering what the business managers use to determine level of activity and how those factors affect the application. In manufacturing, for instance, operations focus on production and the human and material resources necessary to meet production goals. Table 1 and the expanded sample in Appendix A show the business volume segment for a manufacturing system profile.

In this example, orders, shipments, units produced, and labor hours booked in making the product were selected as key business volume indicators. Several trends and pieces of information are displayed: average volume is ahead of last year (1985) in orders shipped, units shipped, units produced, and factory labor consumed. Production has exceeded shipment in each of the months shown. Additionally, the average number of units shipped per order is less than in 1985 — the shop and the application system are functioning for fewer units per order on a greater number of orders. These indicators are typical of the type of business activity that is monitored.

<table><tr><td></td><td>JAN</td><td>FEB</td><td>MAR</td><td>APR</td><td> $\dots$ </td><td>DEC</td><td>YTD TOT</td><td>YTD AVG</td><td>1985 AVG</td></tr><tr><td colspan="10">BUSINESS VOLUME:</td></tr><tr><td>— Orders Shipped</td><td>20</td><td>24</td><td>27</td><td>31</td><td> $\dots$ </td><td>.</td><td>274</td><td>27</td><td>22</td></tr><tr><td>— Units Shipped</td><td>91</td><td>98</td><td>111</td><td>133</td><td> $\dots$ </td><td>.</td><td>1,109</td><td>111</td><td>103</td></tr><tr><td>— Units Produced</td><td>95</td><td>100</td><td>135</td><td>140</td><td> $\dots$ </td><td>.</td><td>1,085</td><td>109</td><td>98</td></tr><tr><td>— Std. Labor Hrs. (000)</td><td>44</td><td>49</td><td>64</td><td>68</td><td> $\dots$ </td><td>.</td><td>522</td><td>52</td><td>48</td></tr></table>

Table 1. Business Volume Indicators

This example is for manufacturing, but the concept is applicable elsewhere. For accounts receivable, we could have chosen volume indicators such as invoices, statements, average days past due, active accounts, and checks posted. New orders, order line items, back orders, and order life are typical for order entry. The business volume segment is a use of the key indicator concept described by Rockart [2]. It is the base for relationships that exist between events affecting the business and the application. In each application the indicators differ and may change in significance over the system's life.

## Information Processing Measures

Computing resources used by the application are shown in Table 2.

Transaction and record counts usually show small year-to-year change in stable environments. They are more likely to follow some type of trend or cycle. In the long term, system managers are alerted more by variations in trend than by how much resource is required.

Each database component has some relationship with one or more of the business volume indicators. Components, such as job orders, should correlate with shop floor activity (production and/or labor hours). Excess levels of job order storage signal a need to purge inactive records. Conditions that permit reductions in computing resource usage benefit a business manager through lower cost, and a data center through reclaimed capacity.

Special application characteristics such as the frequency of material requirements planning (MRP) runs are appropriate in this segment. MRP, a manufacturing system function, typically requires more data retrieval and CPU cycles than ordinary processing. It may be run frequently when business volume is changing. MRP processing costs are likely to be significantly less than the business expense avoided by rescheduling material and factory labor.

We have recorded other nonregular occurrences such as full file bill of material explosions and standard cost roll-ups. Parallels exist elsewhere: more than the normal number of trial balance runs in accounts receivable, repricing in order entry, etc. Each of these affect short-term cost and operating performance.

At this point, some specific relationships are shown. Orders shipped are 22.7% ahead of 1985 and standard labor hours are higher by 8.3%. The improved shipping level has resulted in lesser increases in processing volume — 11.5% for transactions and 5.9% for the total database. This suggests that a 10% variation in the current order mix/volume would result in about a 5% change in transactions. The increases in parts, routings, and bills of material indicate that the application is operating under a different set of conditions than it was a year ago. No particular judgement is being made on the example. The figures serve to illustrate the types of information provided for target setting and performance management.

<table><tr><td></td><td>JAN</td><td>FEB</td><td>MAR</td><td>APR</td><td> $\dots$ </td><td>DEC</td><td>YTD TOT</td><td>YTD AVG</td><td>1985 AVG</td></tr><tr><td colspan="10">INFO. PROC. MEASURES:</td></tr><tr><td>— Transactions (000)</td><td>15.8</td><td>20.1</td><td>29.9</td><td>32.6</td><td> $\dots$ </td><td>.</td><td>213.6</td><td>21.4</td><td>19.2</td></tr><tr><td colspan="10">— Database (000):</td></tr><tr><td>Parts</td><td>10.5</td><td>10.7</td><td>10.7</td><td>10.7</td><td> $\dots$ </td><td>.</td><td></td><td>10.8</td><td>10.1</td></tr><tr><td>Routings</td><td>21.7</td><td>21.9</td><td>22.1</td><td>21.8</td><td> $\dots$ </td><td>.</td><td></td><td>21.7</td><td>20.8</td></tr><tr><td>Bills of Material</td><td>54.3</td><td>54.6</td><td>55.1</td><td>54.5</td><td> $\dots$ </td><td>.</td><td></td><td>53.9</td><td>50.6</td></tr><tr><td>Job Orders</td><td>4.8</td><td>4.7</td><td>6.1</td><td>6.7</td><td> $\dots$ </td><td>.</td><td></td><td>5.3</td><td>5.1</td></tr><tr><td>Total</td><td>91.3</td><td>91.9</td><td>94.0</td><td>93.7</td><td> $\dots$ </td><td>.</td><td></td><td>91.7</td><td>86.6</td></tr><tr><td>MRP Runs</td><td>4</td><td>5</td><td>6</td><td>7</td><td> $\dots$ </td><td>.</td><td>54.0</td><td>5.4</td><td>5.0</td></tr></table>

Table 2. Information Processing Measures

## MIS Costs

The format of the MIS costs segment depends on how services are charged. Table 3 shows operating charges for processing, storage, MIS manpower, and a subtotal for operations.

Development expense is shown below the operations total. Its value can be more volatile than operating costs and depends on the amount of application project work. Progress reporting on development projects is handled as a separate issue. In profile analysis, simply recording the development expense is sufficient. Operating costs show the effect of individual projects completed in previous months. If the application is subject to license fee or royalty, this is also reported. The purpose of the cost segment is to display all MIS expenses for the application.

Below the total charges line is a row called “weeks in period.” The 4, 4, 5 values indicate that January and February are four week accounting periods and March contains five weeks for accumulating data. Given uniform business activity, March costs should, on the average, be 25% higher than either of the previous two months. This entry is used to recognize the effect of accounting cycle variations.

Many MIS organizations charge for resources used and offer incentives for processing at other than peak hours of demand. Typically, a base price is established for first shift computing, discounts are applied to overnight or weekend processing, and premiums are in effect for priority work. This raises the question of managing costs when charges depend not only on the amount of processing performed, but also on when it is scheduled. That problem is resolved by developing a service factor index, the last entry in Table 3. The index is derived by dividing the actual processing charge by the base price value of that work. An index less than 1.0 indicates use of discounted evening or weekend rates; a value greater than 1.0 shows processing service purchased at a premium. The index removes time-of-processing considerations from the data.

The completion of the cost segment permits the final comparison of business volume, processing measures, and dollars. Appendix A shows average monthly business activity, transaction level, database size, and computing expense are all greater than the previous year, but MIS operating cost per unit shipped is lower. Additional management information contained in the sample is left for the reader's review. The particular items of performance to be managed vary from system to system and manager to manager.

## Lessons Learned

Our experience over the past few years has shown that application expense and performance issues are better appreciated when we have used profile measurement than when we have not. The profile is a factual, condensed summary that can calm unpleasant emotion on the cost and performance topic. From a management viewpoint, the profile provides a picture of the business application area today, a starting point for estimating what it will be tomorrow, and a context to ask if the application's performance will meet that requirement. In the words of one of our vice-presidents, profiles took the “black magic” out of MIS cost and value discussions.

<table><tr><td></td><td>JAN</td><td>FEB</td><td>MAR</td><td>APR</td><td> $\dots$ </td><td>DEC</td><td>YTD TOT</td><td>YTD AVG</td><td>1985 AVG</td></tr><tr><td colspan="10">MIS COSTS ($-000):</td></tr><tr><td>— Processing</td><td>5.3</td><td>6.1</td><td>7.5</td><td>8.8</td><td> $\dots$ </td><td>.</td><td>63.0</td><td>6.3</td><td>5.9</td></tr><tr><td>— Storage</td><td>0.2</td><td>0.2</td><td>0.2</td><td>0.2</td><td> $\dots$ </td><td>.</td><td>1.8</td><td>0.2</td><td>0.2</td></tr><tr><td>— MIS Manpower</td><td>0.7</td><td>0.8</td><td>1.3</td><td>1.1</td><td> $\dots$ </td><td>.</td><td>12.2</td><td>1.2</td><td>1.3</td></tr><tr><td>Operations Total</td><td>6.2</td><td>7.1</td><td>9.0</td><td>10.1</td><td> $\dots$ </td><td>.</td><td>77.0</td><td>7.7</td><td>7.4</td></tr><tr><td>Development</td><td>0.9</td><td>0.4</td><td>0.5</td><td>0.1</td><td> $\dots$ </td><td>.</td><td>11.7</td><td>1.2</td><td>1.1</td></tr><tr><td>TOTAL CHARGES</td><td>7.1</td><td>7.5</td><td>9.5</td><td>10.2</td><td> $\dots$ </td><td>.</td><td>88.7</td><td>8.9</td><td>8.5</td></tr><tr><td>Weeks in period</td><td>4</td><td>4</td><td>5</td><td>4</td><td> $\dots$ </td><td>.</td><td></td><td></td><td></td></tr><tr><td>Service Factor Index</td><td>0.78</td><td>0.80</td><td>0.81</td><td>0.83</td><td> $\dots$ </td><td>.</td><td></td><td>0.79</td><td>0.78</td></tr></table>

Table 3. MIS Costs

The analysis of business volume and information processing relationships serves to justify (or at least support) the related expense for a system. This is an important part of application management. Additionally, profile reviews show where to look for improvements in system quality. This approach has uncovered needs to change file processing techniques, add or delete peripheral function, enhance data editing, or tighten the integration of related applications. These changes benefitted performance, and were prompted by analysis of the application and its changing environment.

This article addresses performance measurement from an environment and change management perspective. Another way to affect cost performance is to alter the price of the services. However, price changes may not be that simple, since they influence customer behavior. When the price of a component changes, 'or the makeup of components change, questions arise. The profile can serve as a model for pricing considerations.

The learning curve for new applications is highly visible in a profile. Operational costs for newly installed systems are nearly always higher than when the tuning phases of software implementation are complete. Conversely, the performance of aged software that has not kept up with technological advances can deteriorate when compared to newer applications. The profile is an excellent means to monitor this process.

Our use of profiles takes place in an environment where MIS resources are invoiced as consumed. If that is not the case, profiles may still be useful in managing the computational arena. Monies may not be charged to users, but the cost of the MIS function eventually appears in profitability figures. In that type of environment, emphasis can be on resource utilization or in determining a need for increased computing power. There, MIS “costs” such as CPU cycles, the amount of data stored, memory usage, and MIS staff hours are meaningful. That information is as valid for utilization and performance analysis as chargeback in fully-costed accounting. Software tuning opportunities uncovered by profiles are fairly independent of the method used to pay for services.

## Risks In Application

It has been noted that the spreadsheet resembles a set of simultaneous equations that could benefit from a more rigorous modeling. Experience indicates this may not be true. External influences present trends, but there can be a surprise or two when the monthly data is tallied. These surprises limit the value of a mathematical model. Although there are many relationships in a profile, there is little indication of an independent variable or group of variables on which all others are precisely and consistently dependent.

The more subjective attributes of performances must be kept in mind. Issues of timeliness and effectiveness, for instance, may be addressed. If an application is experiencing a cycle of late reports, errors, or reruns, it may be necessary to add profile entries to count and assist in the identification and correction of these occurrences.

Casual performance comparisons of similar software in different environments can lead to misconceptions. To use manufacturing as an example, the operation and cost for an installation with a two-level bill of material will be considerably different than those for the same software installed at a plant with a five-level bill of material.

## Management Implication

While it is difficult to predict what may develop from profile analysis, we have seen changes occur in management's style as a result of using this approach. Executive decisions on system operation and utilization have become longer term in scope. Profiles identify the causes of change: the effects of run frequency or input handling change, software modification, increased transaction loads, and so forth, all become evident. Short-term emotional reaction to operating and cost variation is significantly reduced. Much of the improved outlook is attributed to thinking about systems in terms of quarters or years instead of weeks and months.

After using profiles, executive management has been more inclined to involve the MIS staff in business decisions requiring future systems activity. Decisions on physical plant moves or process relocation lead to questions of combining or separating application systems. Major product promotions can result in volume and type of processing changes. Special discount sales programs may require software modification to handle the accounting. Successfully communicating implications found in profiles has “opened the doors,” so to speak, and the MIS staff has been invited to participate in substantive management discussion earlier in the decision cycle.

There has been a marked improvement in the ability to respond to undesirable trends before more serious consequences develop. Managers detecting unexpected change in a factor tracked by the profile have acted while the problem had hundred dollar impact instead of emotionally reacting when thousand dollar effects had spread throughout the operation.

In addition to providing executives with a firmer understanding of system performance, there has usually been an increased appreciation of software behavior. This understanding has given rise to improved relationships between the MIS staff and the end user community.

## Conclusion

We have applied profile analysis to an accounts receivable application, to two large customer order service systems, and more than a half-dozen manufacturing system installations. The complex interdependencies in large and changing applications suggest a need for demographic review and analysis on a regular schedule. Information system requirements, people interacting with systems, and businesses surrounding applications are not static. The effect of these changing conditions on an MIS department and on users of MIS services requires more than casual attention. This is the substance of operations management. Profiles assist in successfully meeting the challenge.

## References

[1] McFarlan, F.W. and McKenney, J.L. Corporate Information Systems Management: The Issues Facing Senior Executives, Richard D. Irwin, Inc., Homewood, Illinois, 1983.

[2] Rockart, J.F. “Chief Executives Define Their Own Data Needs,” Harvard Business Review, Volume 57, Number 2, March-April 1979, pp. 81-93.

## About The Author

John L. Batiste is an Account Manager with A.O. Smith Data Systems, Inc. He holds a Bachelor of Science degree in Electrical Engineering from the University of Wisconsin. Before joining Data Systems, John was employed as an assistant project engineer at the University of Wisconsin Space Astronomy Laboratory and had served with the United States Air Force. Mr. Batiste is certified as a Practitioner by the American Production and Inventory Control Society, and has been a guest lecturer in the Materials Management Program at Cleveland State University.

<table><tr><td rowspan="2"></td><td colspan="15">Appendix AManufacturing System ProfileNovember 9, 1986</td></tr><tr><td>JAN</td><td>FEB</td><td>MAR</td><td>APR</td><td>MAY</td><td>JUNE</td><td>JULY</td><td>AUG</td><td>SEPT</td><td>OCT</td><td>NOV</td><td>DEC</td><td>YTD TOT</td><td>YTD AVG</td><td>1985 AVG</td></tr><tr><td colspan="16">BUSINESS VOLUMES:</td></tr><tr><td>— Orders Shipped</td><td>20</td><td>24</td><td>27</td><td>31</td><td>40</td><td>38</td><td>28</td><td>24</td><td>22</td><td>20</td><td></td><td></td><td>274</td><td>27</td><td>22</td></tr><tr><td>— Units Shipped</td><td>91</td><td>98</td><td>111</td><td>133</td><td>159</td><td>138</td><td>116</td><td>90</td><td>91</td><td>82</td><td></td><td></td><td>1,109</td><td>111</td><td>103</td></tr><tr><td>— Units Produced</td><td>95</td><td>100</td><td>135</td><td>140</td><td>125</td><td>120</td><td>115</td><td>95</td><td>85</td><td>75</td><td></td><td></td><td>1,085</td><td>109</td><td>98</td></tr><tr><td>Std. Labor Hrs. (000)</td><td>44</td><td>49</td><td>64</td><td>68</td><td>62</td><td>59</td><td>54</td><td>45</td><td>40</td><td>37</td><td></td><td></td><td>522</td><td>52</td><td>48</td></tr><tr><td colspan="16">INFO. PROC. MEASURES:</td></tr><tr><td>— Transactions (000)</td><td>15.8</td><td>20.1</td><td>29.9</td><td>32.6</td><td>27.9</td><td>23.4</td><td>21.8</td><td>17.0</td><td>14.1</td><td>11.0</td><td></td><td></td><td>213.6</td><td>21.4</td><td>19.2</td></tr><tr><td colspan="16">— Database (000):</td></tr><tr><td>Parts</td><td>10.5</td><td>10.7</td><td>10.7</td><td>10.7</td><td>10.8</td><td>10.8</td><td>10.8</td><td>10.9</td><td>11.0</td><td>11.1</td><td></td><td></td><td></td><td>10.8</td><td>10.1</td></tr><tr><td>Routings</td><td>21.7</td><td>21.9</td><td>22.1</td><td>21.8</td><td>21.3</td><td>21.4</td><td>21.3</td><td>21.6</td><td>22.0</td><td>22.2</td><td></td><td></td><td></td><td>21.7</td><td>20.8</td></tr><tr><td>Bills of Material</td><td>54.3</td><td>54.6</td><td>55.1</td><td>54.5</td><td>52.6</td><td>52.9</td><td>52.3</td><td>53.5</td><td>54.1</td><td>54.6</td><td></td><td></td><td></td><td>53.9</td><td>50.6</td></tr><tr><td>Job Orders</td><td>4.8</td><td>4.7</td><td>6.1</td><td>6.7</td><td>6.9</td><td>5.8</td><td>5.5</td><td>4.9</td><td>4.1</td><td>3.8</td><td></td><td></td><td></td><td>5.3</td><td>5.1</td></tr><tr><td>Total</td><td>91.3</td><td>91.9</td><td>94.0</td><td>93.7</td><td>91.6</td><td>90.9</td><td>89.9</td><td>90.9</td><td>91.2</td><td>91.7</td><td></td><td></td><td></td><td>91.7</td><td>86.6</td></tr><tr><td>— MRP Runs</td><td>4</td><td>5</td><td>6</td><td>7</td><td>6</td><td>7</td><td>6</td><td>5</td><td>4</td><td>4</td><td></td><td></td><td>54.0</td><td>5.4</td><td>5.0</td></tr><tr><td colspan="16">MIS COSTS ($-000):</td></tr><tr><td>— Processing</td><td>5.3</td><td>6.1</td><td>7.5</td><td>8.8</td><td>7.3</td><td>7.2</td><td>6.6</td><td>5.1</td><td>4.9</td><td>4.2</td><td></td><td></td><td>63.0</td><td>6.3</td><td>5.9</td></tr><tr><td>— Storage</td><td>0.2</td><td>0.2</td><td>0.2</td><td>0.2</td><td>0.2</td><td>0.2</td><td>0.1</td><td>0.1</td><td>0.2</td><td>0.2</td><td></td><td></td><td>1.8</td><td>0.2</td><td>0.2</td></tr><tr><td>— MIS Manpower</td><td>0.7</td><td>0.8</td><td>1.3</td><td>1.1</td><td>1.7</td><td>2.8</td><td>0.2</td><td>1.3</td><td>0.3</td><td>2.0</td><td></td><td></td><td>12.2</td><td>1.2</td><td>1.3</td></tr><tr><td>Operations Total</td><td>6.2</td><td>7.1</td><td>9.0</td><td>10.1</td><td>9.2</td><td>10.2</td><td>6.9</td><td>6.5</td><td>5.4</td><td>6.4</td><td></td><td></td><td>77.0</td><td>7.7</td><td>7.4</td></tr><tr><td>Development</td><td>0.9</td><td>0.4</td><td>0.5</td><td>0.1</td><td>0.4</td><td>0.8</td><td>1.9</td><td>2.8</td><td>3.5</td><td>0.4</td><td></td><td></td><td>11.7</td><td>1.2</td><td>1.1</td></tr><tr><td>TOTAL CHARGES</td><td>7.1</td><td>7.5</td><td>9.5</td><td>10.2</td><td>9.6</td><td>11.0</td><td>8.8</td><td>9.3</td><td>8.9</td><td>6.8</td><td></td><td></td><td>88.7</td><td>8.9</td><td>8.5</td></tr><tr><td>Weeks in period</td><td>4</td><td>4</td><td>5</td><td>4</td><td>4</td><td>5</td><td>4</td><td>4</td><td>5</td><td>4</td><td>4</td><td>5</td><td></td><td></td><td></td></tr><tr><td>Service Factor Index</td><td>0.78</td><td>0.80</td><td>0.81</td><td>0.83</td><td>0.82</td><td>0.79</td><td>0.79</td><td>0.76</td><td>0.74</td><td>0.74</td><td></td><td></td><td></td><td>0.79</td><td>0.78</td></tr></table>
