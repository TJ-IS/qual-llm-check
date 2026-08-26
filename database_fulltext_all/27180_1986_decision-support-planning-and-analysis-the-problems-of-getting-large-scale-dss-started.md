---
otero_id: 27180
otero_key: "XYKGFXMJ"
title: "Decision Support Planning and Analysis: The Problems of Getting Large-Scale DSS Started"
authors: "C. Lawrence Meador; Martin J. Guyote; William L. Rosenfeld"
year: "1986"
journal: "MIS Quarterly"
doi: "10.2307/249035"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Planning and Analysis: The Problems of Getting Large-Scale DSS Started
Author(s): C. Lawrence Meador, Martin J. Guyote and William L. Rosenfeld
Source: MIS Quarterly, Vol. 10, No. 2 (Jun., 1986), pp. 159-177
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/249035

Accessed: 09/05/2014 01:11

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Decision Support Planning and Analysis: The Problems of Getting Large-Scale DSS Started

By: C. Lawrence Meador
Martin J. Guyote
Decision Support Technology, Inc.
18 Coltsway
Wayland, Massachusetts

By: William L. Rosenfeld
Research & Planning, Inc.
222 Third Street
Cambridge, Massachusetts

## Abstract

Developing a large-scale institutional DSS designed to serve multiple managers in different business functions can be a more challenging task than that of developing the much more common one-user, one-function DSS that have evolved over the past few years. In this article we review some of the evidence suggesting that extra effort and rigor in the early planning and analysis stage of large-scale DSS development is worthwhile. We attempt to identify those characteristics of DSS that require different treatment than those available in traditional structured techniques. We then present, in the form of a case study, a hybrid technique which we refer to as DSA (Decision Support Analysis) which has been used effectively in developing large-scale institutional DSS. Finally, we discuss some of the positive and negative experiences that have emerged from using DSA.

Keywords: Decision support system, end user computing, user needs assessment, development methodology, architecture

ACM Categories: D.2.1, H.1.2, H.4.2, J.1, K.4.3, K.6.1

## Introduction

Decision support systems (DSS) are computer-based information systems designed to help managers solve problems in semi-structured decision-making areas. Successful DSS applications have addressed problems and decisions in a broad range of managerial and policy environments (see $[1, 2, 9, 11, 15, 26]$ ). By definition, semi-structured decision-making environments are those not well enough understood to permit complete analytical description. This implies the need (and opportunity) to combine managerial experience and judgement with quantitative computer-based approaches.

Planning and analysis are critical tasks in the development of large, complex DSS environments, especially those designed to support several different business functions. Differences between DSS and traditional MIS and DP applications however, oblige developers to use different analytic methods for DSS. In this article we approach these differences from an applications perspective rather than from a theoretical perspective, though in many regards DSS lacks both theoretical and empirical underpinnings.

The early stage of large scale institutional DSS development, here called the Decision Support Analysis (DSA) stage, includes planning, end user needs assessment, problem diagnosis, management orientation and priority setting.

Five elements incorporated into the DSA approach include structured interviews, decision analysis, data analysis, technical analysis, and management orientation. The use of this approach is illustrated by a case study that analyzes the decision support needs of multiple business functions within the marketing organization of a large manufacturing firm.

## Development of DSS vs. Traditional MIS Systems

Analysis in Traditional Systems Development

The importance of analysis in the development of traditional MIS and DP applications is well established. For example, Boehm [4] has shown that more errors are introduced into a new system through failures in analysis than through failures in design, construction, or implementation. Shooman and Bolsky [23] found that errors in analysis are more costly to correct and have greater impact upon system effectiveness than errors in design and construction. McKeen [12] found that additional time spent in front-end analysis led to less overall development time and cost, and greater user satisfaction with the delivered system. Developers of traditional systems — recognizing the importance of analysis — now give increased time and effort to front-end analysis. Their objective is a detailed prespecification of the full system. However, DSS development typically follows a different approach.

## Analysis in DSS Development

DSS development follows a plan that lays out specific tasks to be performed, and the proper order of performance. Recent research on DSS applications suggests that planning is perceived by DSS users and developers to be a very important activity. However, it is often performed less effectively than is desired $[13]$ . Figure 1 shows a typical DSS development plan that might be suitable for large-scale institutional DSS (sometimes referred to as an organizational support system). The first step in this process, Decision Support Analysis, involves the identification of:

1. high priority applications,

2. high level function requirements for those applications,

3. information characteristics and requirements,

4. appropriate fundamental approaches to addressing user needs, including system architecture and detailed technical requirements, and

5. orientation of users to DSS concepts and their relevance to supporting users' jobs.

The first four areas are used to guide software evaluation and selection, prototype design, and prototype construction. The decision support analysis stage provides initial direction to the entire DSS development process. In addition, management orientation to

DSS that occurs during this stage helps to avoid organizational problems during implementation. It does this by fostering realistic expectations and generating commitment from users.

## Traditional Systems Analysis Methodologies

Many methodologies for analyzing requirements of data processing applications have been developed during the last several years. They include IBM's Business Systems Planning [8], Yourdon's Structured Analysis Techniques [5], SofTech's Structured Analysis and Design Techniques [21, 22], and others.

These methodologies generally share the following characteristics.

1. They are typically used to analyze information flows and data structures for large, structured applications where the scope of the application is fairly well defined in advance.

2. The primary objective is to provide a detailed specification of data flows and structures that can be directly translated into system designs. Designs are then frozen prior to the construction phase. This construction method subdivides large projects among many programmers, thereby requiring greatly detailed specifications in order to avoid massive coordination problems.

3. Given the size of these applications, a second basic objective is to facilitate the translation of the detailed specifications into efficiently designed systems.

4. These methodologies require extensive investments in time and resources to achieve the level of detail required.

Requirements analysis is costly and may be hard to justify for DSS. Thus traditional methodologies may have to be scaled down and modified to be acceptable to DSS users for the following reasons:

1. Many DSS applications are smaller in scope than traditional MIS or DP applications.

Figure 1. A Tactical Plan for DSS Development  
![](/api/attachments/XYKGFXMJ/fulltext/images/b74395300b41f47c463946d3ae8439252009d7ff99a1cb0fb15181796401f9a3.jpg)

2. The benefits of many DSS applications are hard to quantify.

3. DSS users have difficulty prespecifying their decision support needs without a concrete system to which they can react.

4. The decision support needs of DSS users change frequently.

5. It is more important that DSS be effective than efficient (although efficiency is also, of course, an important goal).

6. Problems to which DSS are applied must often be addressed quickly relative to traditional system development timeframes.

These factors have led many authors to argue for an evolutionary approach to DSS development using prototypes and rapid development tools such as fourth generation languages $[3, 17]$ . However, it is often still taken for granted that evolutionary application development must be preceded by a precise and detailed requirements analysis. This article supports an evolutionary approach for requirements analysis as well.

## DSS Analysis Methodology

Procedures for DSS analysis and design should exhibit the following characteristics.

1. Minimal elapsed time prior to prototype development. Users need a concrete system to which they can react.

2. Robustness — given the preceding constraint, analysis will often be incomplete and fragmentary. The analytic method must compensate for less than perfect data by quickly focusing on the highest priority applications, and on those functional requirements for each application that warrant more detailed analysis.

3. Ability to evolve along with the DSS — the same methodology should be capable of being used to discover initial DSS opportunities, establish initial functional requirements, and evaluate existing systems to identify directions for further growth.

4. The analytic methodology must have user involvement as an important by-product.

5. There should be an orientation toward managerial users and their decision making activity. This implies designing the systems with special emphasis on the user interface(s), and providing procedures and data representations that fit well with specific managers' established activities.

6. At the same time, there should be an emphasis on prescription as well as description. The methodology should capture managers' decision processes and should establish priorities to improve these processes. This includes pinpointing potential applications with the biggest impact on managerial effectiveness and the highest priority functions needed for these applications. To do this well, the analysis of managers' activities should be tied to individual goals plus the overall goals of the organization, that is, to managers' critical success factors [20]. The analyses should explicitly surface information on improving specific business activities, satisfaction with current performance, perceived costs of improvement, and the amount of technological and organizational risk associated with proposed alternatives.

## Decision Support Analysis Approach

Decision Support Analysis is designed to get DSS started quickly and to achieve the results described previously. There are five basic components of the DSA approach: structured interviews with management, decision analysis, data analysis, technical analysis and management orientation. These processes and their intended results are illustrated in Figure 2.

A case study is presented to show the overall flow of the process. The approach presented here is primarily oriented toward planning large-scale institutional DSS in settings where the user community includes multiple managers in different business functions. In other settings, however, it has been tailored to the needs of single business functions and smaller organizations, to the technological sophistication of the organization, and the scope of the DSS. In such cases, specific tasks may be de-emphasized or eliminated in order to proceed more quickly and at lower cost.

Figure 2. Decision Support Needs Assessment Process and Results  
![](/api/attachments/XYKGFXMJ/fulltext/images/fff856c54e02771cfab638202710d4b5f13c067aed1defc391d86c8464b41663.jpg)

The case study organization, which we will refer to as Image Technology Corporation (Imagtec), is a Fortune 100 manufacturer of consumer and industrial products. The corporation has a 500-person sales force in its U.S. and overseas subsidiaries. This sales force is managed from a central line organization supported by staff functions that perform forecasting, sales analysis, promotion analysis, market research, end consumer sales audits, product development, strategic planning and advertising. The marketing function was being supported by a marginally functional set of transaction processing systems but had very little decision support. A number of sophisticated software development tools had been acquired at various times but at the time of this study they were poorly utilized, and the resulting applications suffered from poor integration. The planning effort described here was initiated to develop a “blueprint” for a worldwide marketing information and decision support system (WMIS) and to obtain the necessary management support. The analysis and planning described was conducted by a team of five analysts over a three month period.

## Structured Interviews

The process begins with interviews that allow managers to identify their critical needs, objectives, and priorities. When possible, interviews are conducted with senior management, systems management and staff analysts.

The interview process at Imagtec included one to two hour interviews with more than forty line executives and staff professionals in the above categories, all of whom were involved with the production and use of marketing information. Given the time constraints, two things are key to maximizing the usefulness of the interviews. The first is the use of interview checklists to focus interviews.

Interview checklists should be designed in consultation with one or two key user managers to ensure that all important areas of activity are covered. Broad areas of coverage should include:

1. a brief description of the objectives, scope, and plan of the project;

2. a description of the project methodology;

3. major business objectives/priorities/decisions;

4. areas for improved decision support (manual or automated);

5. interfaces with other groups and organizations (internal and external);

6. projections of future needs;

7. policy issues such as authority, accountability, and degree of direct use;

8. feedback on the interviews.

The checklists should be used in short preliminary sample interviews with a few selected managers, and then revised based on feedback received. By necessity, these interviews will gather impressionistic data, and techniques such as rating scales and semantic differentials are useful in structuring managers' reports of their perceptions and preferences. Aside from making quantitative analyses possible, the use of rating scales facilitates comparison of results from different respondents.

A useful technique in helping to establish priorities is to have the respondents rate lists of issues and/or functional features on two separate dimensions: perceived importance and perceived performance or satisfaction. High priority issues and features are those that are given high importance but low performance/satisfaction ratings.

We have found that “generic” lists of issues and features are often of limited usefulness, since such lists necessarily include many extraneous items and omit many important ones for any specific application. Further, they usually have to be reworded to conform to the internal terminology of the organization. However, there may be some classes of applications that lend themselves well to such checklists. One example would be organizational cost management and budget analysis systems, which for most large firms would have similar characteristics, including large, multi-user systems with substantial hierarchical consolidations, financial modeling, automated forecasting, alternative scenario analysis, and flexible reporting. In most cases, however, the issues and functional features must be developed by the team conducting the decision support analysis along with sponsoring senior managers.

The second key to the usefulness of the interview results is the experience and skill of the interviewer. The interviewer should go into the interview with a clear understanding of those characteristics that mark a particular task or decision making activity as a prime candidate for decision support. Examples of these characteristics include:

1. labor intensive calculations are involved;

2. frequent iterations of the calculations are needed to reach consensus on plans;

3. multiple scenarios are required to evaluate uncertainty and form contingency plans;

4. a process that is highly judgemental and cannot be completely programmed;

5. coordination among numerous individuals, so that the DSS can provide structure and a common language to enhance consistency and communication;

6. a task or decision process that has senior management involvement, and thus high visibility and potential impact;

7. a task or decision process that is compartmentalized. This facilitates a phased implementation plan using prototypes;

8. an environment that involves situations of clarification;

The ability to quickly spot high potential DSS applications is important in directing interviews along fruitful paths. This helps uncover as much useful information as possible in the allocated time. The interviewer must walk a fine line, however, between direction that facilitates the manager's identification of needs and putting words into the manager's mouth. The interviewee should be allowed to deviate from the interview checklist to discuss issues and features that may be of particular importance in his or her situation which were not anticipated.

In the early stages of interaction with Imag-tec management, the interview process found that important decisions in advertising, promotion, pricing, and distribution were often made without determining the interrelationships among these areas. Such decisions were often made without an assessment of competitive actions along these same dimensions. Some of these deficiencies were apparent to the Group Vice President for Marketing. The senior manager who had approved the decision support planning and analysis activity initially was himself skeptical and unwilling to go through the structured interview process. Gentle but persistent pressure by the DSS development team eventually convinced him that he should participate in the process as well. Once he became committed through personal involvement in the process, his apparent understanding of it and appreciation for its value increased dramatically.

Significant deficiencies surfaced in the process by which market research impacted product development and strategic competitive positioning decisions. Five separate, independent and typically disparate forecasting processes operated in parallel to, and in competition with each other. No process existed to rationalize the discrepancies for senior management. These findings suggested that decision process integration was to be a major objective of the proposed DSS. Feedback on the overall interview results was provided to each participating manager as soon as analysis had been completed by the DSS development team. Each manager was asked to critique the assessment derived from the interview process for his or her area of responsibility.

## Decision Analysis

At the conclusion of the structured interviews, we develop a conceptual framework to guide the identification of DSS opportunities, system design, project management, and communication of priorities between users and system developers. We call the development of this conceptual framework Decision Analysis, and it is the next step in Decision Support Analysis. (Please note that our use of the term “Decision Analysis” does not refer to the narrow — though well entrenched — view which applies Bayesian statistical theory to analysis of decision problems.) The conceptual framework consists of the output from three tasks which are described below.

## Business Area Analysis

The first step in Decision Analysis is completion of a business area analysis. This process studies representative business units to determine their decision support functional requirements. The analysis is closely tied to the existing organizational structure (as is the definition of the term “business area”). In one client situation, it might refer to corporate divisions, and in another, functional departments or even offices. This lets managers appreciate the extent to which each business unit has unique needs. It also allows for different levels of sophistication in the use of information technology. The result is a set of business area specifications that identify each group’s mission, system objectives, basic functions, shared data, internal data, and reports/analysis needed. These specifications are critiqued and approved by each manager before proceeding to the next step.

## Description of Logical Functional Flow

Once the business area specifications have been developed from an organizational perspective, they are converted to functional flow diagrams. This involves hierarchical decomposition of the decision making activities of the business areas. The purpose of the hierarchical decomposition is the description of the logical relationships among the business functions. Any of a number of analytic methodologies may be used for this purpose (the Structured Analysis and Design Technique (SADT) developed by Softech is illustrative in this regard — see [5, 21, 22]). The primary objective of the functional flow diagrams is to quickly provide a structure for the more detailed analyses that follow, so that only one or two levels of detail are necessary.

One of the functional flow diagrams developed for the Imagtec marketing function is shown in Figure 3. This is an SADT style diagram. A business function is defined as a group of logically related activities (decisions or tasks) required to manage the resources of the business. Thus, at the highest level, four major business functions were identified for the

Figure 3  
![](/api/attachments/XYKGFXMJ/fulltext/images/2f29266640960b15d88c9ffb8cf0a3ee78c084ff556e44fab31c4cb381eee62f.jpg)

Imagtec marketing function: planning, forecasting, sell-in, and sell-through. Manufacturing is shown on the diagram because of its interface with the marketing function at a central point in the ongoing process. The planning function is responsible for directing all of the marketing functions. The forecasting function is responsible for developing the shorter term, more quantitative plans that direct current operations. Manufacturing converts the plan into product. The sell-in process is concerned with moving inventory from Imagtec warehouses to the dealers' warehouses (i.e., "selling into" the dealer network). Finally, sell through is concerned with moving the product from the dealer to the customer (i.e., "selling through" the dealer network to the consumer marketplace).

The logical relationships among functions may be of two kinds. One type of relationship is the subordinate relationship which identifies the specific activities that make up a higher level function. In looking down the hierarchy from any given function, the subfunctions describe how to accomplish the function. On the other hand, looking up the hierarchy from any given function shows why that function is performed. Thus, in Figure 3, the overall forecasting function is broken down into three subprocesses: sales analysis, estimation of sales potential, and sales/production review.

The second type of relationship among functions is shown in Figure 3 by arrows denoting major information flows. These are used both to indicate the major information needs and outputs of any given function and also to establish sequential dependencies among functions.

The discipline behind the techniques used to develop the diagram may have a further purpose. It may highlight development opportunities that will emerge in the future. Such hierarchical descriptions may eventually be the requisite inputs to computer aided software engineering systems (sometimes referred to as automatic programmers). These can produce at least “first draft” computer code directly from the graphical descriptions. The CAD/CAM (computer aided design/computer aided manufacturing) tradition is now spawning a whole new prototypical generation of these systems development capabilities.

The functional flow diagrams also provide a context for other types of analysis and user communication. In combination with priority ratings given by managers, they can be used to highlight the most important functions to support first. The diagrams are also used to classify and categorize information needs, and to guide system design and project management.

## Specification of Detailed Decision Areas

The final step of Decision Analysis is decision identification and classification. Understanding decision domains allows us to effectively plan decision support. This simple observation is occasionally forgotten. A solid basis is developed for prioritizing DSS development by undergoing a formal process to identify the organization's major regular and ad hoc decisions. Decisions can be analyzed in terms of their complexity, frequency, level of detail, time horizon, accuracy requirements, information sources, and the scope of their information requirements.

One result of the functional flow diagrams is the identification, at the lowest level of the hierarchy, of detailed business functions or decision areas that offer distinct opportunities for decision support. As mentioned above, these lowest level functions should be specified so that they can serve as potential candidates for prototype systems. This means that each should describe a relatively modular task of modest scale that nevertheless has significant impact upon the success of a higher level function.

For the marketing function at Imagtec, a list of 16 detailed functions was derived; three of these are shown in the bottom diagram in Figure 3. A list of sample questions is then derived for each decision area (see Figure 4) that reflects the highest priority information needs. These questions are later used as objectives to guide system design.

## Data Analysis

The next step in DSA is the identification and description of the classes of data used by the

Figure 4. Examples of Key Questions for Sales Production Review

## 2.3 Hold Sales Production Review

![](/api/attachments/XYKGFXMJ/fulltext/images/17961be2583f18cead76d901e52a9b8994bb57db9fc0087f09e2cc4ba9d6b43f.jpg)

## 1. Compare Alternative Forecasts

\- How does marketing's forecast compare to manufacturing's estimate of sales?

\- How does marketing's forecast compare to finance's estimate?

• Is there a consensus on the underlying assumptions?

\- How does the current forecast compare to the annual unit plan?

## 2. Issue Identification/Resolution

\- Does manufacturing have the appropriate level and mix planned?

• Is there a consensus on the forecast?

\- Are there products for which we have excessive or insufficient inventory to meet expected demand?

\- Are there capacity constraints that will limit sales? If so, time/cost to increase capacity?

## 3. Risk Evaluation

\- What is the range of sales potential and where do the marketing and manufacturing sales forecasts fall within that range?

• What are the consequences of various levels of over/under forecasting?

• What can be done to minimize the risk?

functions. This is done through analysis of the functional flow diagrams. The purpose of Data Analysis is to identify commonalities in information requirements and usage among the decision areas. It also allows us to derive design requirements for application databases. These purposes are accomplished through: (1) data classifications to categorize variables of interest for the managers' interviews (e.g. product pricing, inventory levels, competitors' market share), and (2) dimensional representations developed to structure different views of these variables by time, product, market, etc.

For the Imagtec marketing function, 31 different classes of data were identified and described. Detailed elements were documented for each class of data. One of the outputs from this stage was a chart detailing the relationship between the data classes and the decision area. The Data and Function Usage Chart for the Imagtec marketing function is shown in Figure 5. For each data class and decision area the chart shows whether the function uses (U), creates (C), or both uses and creates (B) the data. This chart provides insight into the most frequently used data and the most data intensive decision areas (e.g. estimation of sales potential in forecasting). In this case the chart clearly suggests the need for an integrated database — all of the data is used by more than one decision area. Thus, a central set of management data should be used to eliminate the need to re-enter or recreate data for different applications.

At Imagtec, the marketing function managers had grown weary of a data processing system which overwhelmed them with their own data. The marketing managers participating in this study came to realize the magnitude and complexity of the data resources needed to perform their functions — and thus understood why they currently had little or no reasonable basis for effective quantitative analysis. The prior existence of sophisticated DSS software was of little help. A few well positioned prototypes demonstrating some interactive database retrieval capabilities as well as analysis of sales accounts resulted in a broad management-end user support base.

Figure 5. Data and Function Usage

<table><tr><td rowspan="2"></td><td colspan="4">GEOGRAPHY</td><td colspan="3">ACTUALS</td><td colspan="4">EXTERNAL PLANS AND DATA</td><td colspan="4">PRODUCT</td><td colspan="4">PREDICTIONS/ DIRECTIONS</td><td colspan="4">PLANS</td></tr><tr><td>Legend: C = createU = useB = both</td><td>Sales OrganizationDealerChannelEnd UserCounty</td><td>OrdersShipmentseRetailSell InventoryCompany InventoryPromotion History</td><td>CanusylDemographics</td><td>Psychographics</td><td>EconomicitiesManufacturingFinance Plans</td><td>PriceFeatures</td><td>Margin</td><td>Consumer Demand</td><td>Related Products</td><td>Long Range Plans</td><td>Annual Unit Plan</td><td>Forcasts</td><td>Computative Assessments</td><td>Marketing Plan</td><td>Product Plan</td><td>Pricking/PositioningPromotions</td><td>Advertising Plans</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">PLAN</td><td>Assess Market and Industries</td><td>B U</td><td></td><td>U U</td><td>U</td><td>U</td><td></td><td>U U</td><td>U</td><td>U</td><td></td><td>U</td><td>U</td><td></td><td>U</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Set Product/ Marketing Direction</td><td>U U</td><td>U</td><td>U U</td><td></td><td>U</td><td>U</td><td>U</td><td>U</td><td>B B B</td><td>B</td><td>U</td><td>B</td><td>U</td><td>U</td><td></td><td>B B</td><td>B</td><td>U</td><td>C</td><td></td><td></td><td></td></tr><tr><td>Research New Concepts/Products</td><td></td><td>U</td><td></td><td></td><td></td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>C</td><td>U</td><td></td><td></td><td>U</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Develop Long Range Plans</td><td>U U U</td><td>U</td><td>U</td><td></td><td></td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>C</td><td>U</td><td>U</td><td>U</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">FORECAST</td><td>Sales Analysis</td><td>U U U</td><td>U</td><td>U U U</td><td>U</td><td>U B</td><td>U</td><td>U</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>U</td><td>U</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Estimate Sales Potential</td><td>U U U</td><td>U</td><td>U U U</td><td>U</td><td>U U U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>B B</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td></td><td></td></tr><tr><td>Hold Sales/ Production Review</td><td></td><td>U</td><td></td><td></td><td></td><td></td><td></td><td>U</td><td></td><td></td><td></td><td></td><td></td><td>U</td><td>U</td><td>U</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="5">SELL-IN</td><td>Maximize Sales Effectiveness</td><td>C C U</td><td>U</td><td>U U</td><td>U</td><td></td><td>U</td><td></td><td></td><td>U</td><td>U</td><td>U</td><td></td><td>U</td><td>C</td><td>U</td><td>U</td><td>U</td><td>C</td><td></td><td></td><td></td><td></td></tr><tr><td>Define Promotions and Programs</td><td></td><td>U</td><td></td><td></td><td>U</td><td>U</td><td>U</td><td></td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td></td><td>B</td><td>U</td><td>C</td><td>B</td><td></td><td></td></tr><tr><td>Sell to Dealer</td><td>U U U</td><td>U</td><td>C U</td><td>B C</td><td></td><td>U</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>U</td><td>U</td><td></td><td></td><td></td><td>U</td><td></td><td></td><td></td></tr><tr><td>Distribute Product</td><td>U U U</td><td>U</td><td>U C U</td><td>B U</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Track the Sales Force Program</td><td>U U U</td><td>U</td><td>U U</td><td>U</td><td></td><td></td><td></td><td></td><td></td><td></td><td>U</td><td></td><td></td><td>U</td><td>U</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">SELL-THROUGH</td><td>National Dealer/ Co-op Advertising</td><td>U U U</td><td>U</td><td>U U U</td><td>U U U</td><td>U</td><td>U</td><td>U</td><td></td><td></td><td></td><td></td><td></td><td></td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td></td><td></td></tr><tr><td>Sell To Consumers</td><td></td><td>C U</td><td></td><td>C</td><td></td><td></td><td></td><td></td><td>U</td><td>U</td><td>U</td><td>U</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Retail Market Analysis</td><td>U U</td><td>U</td><td>U U B</td><td>U</td><td>U</td><td>U</td><td>U</td><td></td><td>U</td><td>U</td><td>B</td><td>U</td><td></td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td></td><td></td></tr><tr><td>Conduct Market Research</td><td>U U U</td><td>U</td><td></td><td></td><td></td><td>U</td><td>U</td><td>U</td><td></td><td>U</td><td>B</td><td>U</td><td></td><td></td><td></td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td><td></td><td></td></tr></table>

One of the key elements in effective DSS is a set of well designed, multidimensional data structures that allow alternative views of important business variables. Research confirms that end users perceive the need for such capabilities $[10]$ . Different responsibilities imply different views of strategic and operational information. At the same time, effective communication between managers requires consistent procedures for structuring and aggregating information across several dimensions. Some of the keys to effective design of the multidimensional data structure include:

1. Easy multidimensional access — Each manager and analyst must be able to access information at different levels using consistent procedures and commands.

2. Easy restructuring of information — Dimensions change over time. Product lines and markets are combined, added, and dropped, as are entire businesses and subsidiaries. The user should have the ability to restate and/or recalculate historical and forecasted information in terms of new dimensions or new values on existing dimensions.

3. Manageable dimensionality — Humans can only handle a certain level of complexity in information. Although computers can be made to deal with unlimited dimensionality in a database, we find that for managers using the database, an upper limit on the number of usable dimensions may be in the range of five to seven in a single data structure. A typical example would include the dimensions of time, product, market, division, and geographical region for actual and forecast data. Managers sometimes find it useful to picture multidimensional databases in terms of a series of information “cubes.”

4. Use of "information bases" rather than databases whenever possible — We distinguish between information bases and transaction-processing databases in the following ways. (1) Information bases are relatively small, and usually highly aggregated, reflecting the fact that managers usually overestimate the amount of transaction detail required to satisfy their query and analysis needs. (2) Information bases have a much greater orientation toward future time periods than transaction-processing databases, which tend to focus on recent history. (3) Information bases provide value-added information through the addition of appropriate external data. (4) Information bases are optimized for efficient access and analysis, rather than for efficient updating and storage. (5) Information bases emphasize multiple scenarios and alternative views rather than consistency and completeness. (6) Information bases are constantly evolving.

For most DSS applications it is more cost effective to provide managers with interactive access to several small, highly summarized extracts providing alternative views of the data, rather than to provide access to large transaction files. This also helps to ensure the security and integrity of transaction files and databases. The information bases will satisfy 90-95% of user's queries, and the remainder can be processed via batch procedures.

The ultimate architecture for the integrated marketing databases at Imagtec took on the following characteristics. Using “inverted list” technology, simple databases were constructed. A series of databases were implemented, the largest of which contained relevant sales information for every product/customer combination in the prior 24 to 26 months. This file was accessed only on an exception basis, after higher level summary files (i.e., information bases) had enabled an area of interest to be identified.

The basis for constructing these critical summary files came from the decision and data analyses conducted with each marketing manager. Thus, the manager's own perspectives on his or her business was exactly the view they utilized to access their sales data. Finally, menu-based dialogues were constructed and data dictionaries were built to ensure ease of use and flexibility in building and accessing these critical tools (see Figure 6).

Figure 6. Imagtec DSS Architecture Summary  
![](/api/attachments/XYKGFXMJ/fulltext/images/64ece1810434d147a703d7faaeee7407148cb4cc7c793a0b943aef24718af301.jpg)

## Technical Analysis

Technical Analysis translates needs identified in the previous stages into a proposed system design with technical requirements for hardware and software. The results of this process will, of course, vary for each application. However, we have found that many issues appear time and again. These are described below in the context of the Imagtec environment:

There are a number of technical performance issues relative to the design, implementation, deployment, and operational use of the Imagtec systems. Some of the technical issues are functional in nature; many of them have important performance implications. The Imagtec marketing DSS had to provide considerably expanded functional capabilities over existing systems with acceptable performance parameters; achieving adequate performance turned out to be both complex and resource consuming.

A number of these technical requirements included:

\- Increased access to information, including ability for multiple users to remotely and interactively review and analyze information.

\- More timely delivery of information from operational systems to DSS end users; this capability, of course, depends upon the originating source of the data and its ready availability to the DSS.

\- Improved modeling and simulation capabilities to fully support expanded modeling, "what-if" and statistical analysis.

\- Interactive development of ad hoc database and information base extracts and reporting.

\- A high degree of overall systems reliability, including that of the host hardware, telecommunications, and support software, as well as that of the DSS support routines and application modules.

\- Comprehensive security and integrity mechanisms which are effective to protect individual and group activities without being unduly awkward to use or generating excessive system overhead.

\- Dual modes of DSS user interface — to enable novice users to operate in a fully prompted mode and enable expert users to bypass unneeded prompts and operate in a concise prompt or command driven mode.

\- Display of data/information in a variety of formats: on screen, hard copy from screen, batch system or multi-copy, multi-destination routing, and routing to remote devices such as local area networks (LAN), "gateways," intelligent terminals, and personal computers.

\- Choice of terminal devices to include online access via either full screen video/keyboard device or line by line hardcopy device, at user option, leased line and dial up methods of access.

\- Flexible and convenient access to personal databases for personal experimentation, with ease of creating, modifying, deleting, and/or sharing the personal database.

\- Appropriate use of batch processing, rather than online interactive processing, where the amount of processing, cost factors, and user response requirements dictate.

Once an initial system design architecture has been chosen, it must be translated into a set of requirements to guide software evaluation and selection. A summary list of features to consider in a DSS development language, for example, is shown in Figure 7. The requirements drawn up must address technical issues relative to the design, implementation, deployment, and operational use of the DSS. Many of the technical issues are functional in nature, and have important performance implications. Some of those listed in Figure 7 for the Imagtec DSS explicitly appeared in the user needs assessment (e.g., "what if" analysis capabilities), whereas others had to be inferred (e.g. the need for multidimensional data access). In addition to functional features, the important issues of implementation and ongoing support of any DSS should be reflected in characteristics such as the syntactic complexity and readability of the command language (which affects end user orientation and programmer productivity), security considerations [16], and the types of training and support offered by the vendor. A fuller discussion of other software features relevant to Technical Analysis of DSS is given in [14].

## A. FUNCTIONS AND FEATURES

1. MODELING — able to calculate with the information in the system, do optimization, "what-if" analysis

2. PROCEDURALITY — ability to solve equations independent of their ordering, symbolic reference of data

3. DATA MANAGEMENT — number of dimensions, handling of sparse data, ad hoc inquiry

4. REPORT GENERATOR — ability to produce high quality formal reports quickly and easily

5. GRAPHICS — line, pie, bar, quality of output

6. STATISTICS & ANALYSIS — descriptive statistics, regression, significance tests

7. PROJECT MANAGEMENT — PERT/CPM, multi-level work breakdown structure

8. OPERATIONS RESEARCH — linear, integer, dynamic programming

9. FORECASTING & ECONOMETRICS — time series analysis, seasonalization, smoothing

10. EXTERNAL DATABASES & INTERFACES

11. SECURITY — database, file, model, class of user

## B. EASE OF USE

1. END USER — analysis performed directly by person who needs the information

2. PROGRAMMER/ANALYST — interested in the quality of the editor, data management, report writer, etc.

3. AD HOC INQUIRY — end user answering questions for which no standard report is available

## C. FACILITIES

1. DOCUMENTATION — for user, programmer, operations

2. TRAINING — novice/advanced, systems/user

3. SUPPORT — consultant, hot line

4. HOST HARDWARE — computers supported

5. OPERATING ENVIRONMENT — operating systems, disk requirements, etc.

6. AVAILABILITY IN-HOUSE & ON TIMESHARE

## D. MARKET POSTURE

1. PRICING — lease, rent, purchase

2. INSTALLATIONS — number of users, length of use

3. TARGET MARKET — type of business actively pursued by the vendor

4. PLANS — commitment to DSS as a business area, amount of R&D

5. USER PERCEPTIONS — degree of use and support, functions used

6. VENDOR VIABILITY — size of company, revenues, etc.

## Management Orientation

User needs assessment should serve to educate the DSS developer about the types of systems to build and how they will be used. The needs assessment process, along with Management Orientation, helps to educate potential users and other managers about the concept of DSS and what they can realistically expect the proposed system to do for them. Further, Management Orientation should indicate how the DSS should be effectively used. The educational needs of users depends upon their previous experience with computers and how they plan to use the proposed system (either directly or through intermediaries). Regardless of the exact topics covered, the basic objectives of the Management Orientation process are to promote:

1. information sharing among developers and users,

2. attitude change among users and developers,

3. skill building among the DSS development team members, and

4. actions motivated to ensure commitment to development and use.

The Management Orientation process at Imagtec took place in three steps. First, the managerial community (about 40 line managers and staff professionals) was briefed in detail on the specific design characteristics and utilization implications for each of their functional areas. Second, senior marketing management and information systems management were briefed on the organizational impacts and benefits and costs of implementation of the system. These two sets of orientations were conducted by the development team. Finally, after an indepth briefing, the Chief Operating Office of Imagtec presented implementation recommendations for final approval to the Board of Directors. The Board accepted the plan and implementation was begun.

## Discussion

By following an effective Decision Support Analysis process, the organization can more quickly and confidently proceed with DSS development. Management priorities are known.

User needs have been analyzed, documented, and structured in an overall framework. Data requirements are understood and integrated within that framework. Technical plans have been developed to create an appropriate environment for system development, and criteria have been established to guide appropriate technology selection. Most importantly, manager involvement and education provide direction, build support, encourage the acceptance of appropriate responsibilities, and create realistic expectations.

These results of Decision Support Analysis guide the DSS development process through detailed design, prototype development, and full-scale operational deployment. The plans and priorities established in these initial stages, together with careful project management during construction and implementation, help to guarantee a system that will effectively support users in high priority tasks.

In the Imagtec case study, a DSS development plan was created for 16 major business functions within 10 functional areas of the marketing organization in three months (less detailed planning, using the same DSA approach for smaller organizations, has been completed in six weeks). The identification of priority projects proved, in this case, to be critical because funding only allowed development to proceed in certain areas.

The DSS development manager at Imagtec used the overall plan to identify potential high payoff projects for development, to place them in context, and to ensure integration of the separate efforts. The use of this particular approach to analysis and design at Imagtec also served other very practical purposes. The marketing information systems organization was initially viewed as a group of systems engineers whose job it was to analyze, design and implement systems. DSA allowed that role to be expanded into a partnership with key marketing managers in the identification of critical areas of improvement in the decision making process. This was initiated at the middle management level, not as a top executive Critical Success Factors study, but simply as a user needs assessment aimed at producing more useful information to marketing managers.

The process was able to identify critical needs, achieve a consensus on priorities, and ultimately received funding from senior management. It was even able to withstand some fairly critical organizational changes. Shortly after the DSS planning process was completed, the senior manager who sponsored the study was reassigned to an entirely different project activity. This might have led to complete abandonment of the DSS development project were it not for the then existing shared perspectives and goals of Imagtec marketing managers as well as careful documentation of objectives, approach, benefits and impacts.

The resulting architecture and individual project plans have continued with varying degrees of success. The implementations of prototypes for marketing managers most closely associated with the project have been far the most successful. The overall objective of marketing data integration has suffered due to the discontinuity of management sponsorship. However, a marketing organization once overwhelmed with data has some useful information and increased confidence in an information systems organization and its new technologies and methodologies. Most importantly, it has a plan and an architecture that in time can bring more information to bear on its critical marketing decisions.

These benefits, of course, have their associated costs. The decision to perform Decision Support Analysis adds up-front costs to the development effort, and delays the development of prototypes. In the case of Imagtec, for example, four man-months of effort over three calendar months were required. This may seem antithetical to the DSS philosophy of quick prototype development. However, we observe in many cases that large-scale, institutional DSS such as the Imagtec application resemble large scale transaction processing applications in that the costs of initial analysis are usually more than offset by a reduced risk of project failure, and by lower costs in all other phases of development. Large-scale, institutional DSS represent a hybrid case somewhere between personal DSS and large transaction processing systems, and the approaches to analysis and design should reflect this. In the Imagtec setting, it was possible to start implementation of prototypes in some areas before Decision Support Analysis was completed.

## Conclusion

It has been suggested that there are natural stages of evolution and maturity in the use of organizational information systems. Some suggestive anecdotal evidence for such conclusions has been presented. It has often been observed (or at least argued) in biology that “ontogeny recapitulates phylogeny” — that is, particular organisms, in their development, go through stages that resemble some of their ancestral forms [24]. Perhaps DSS development methodology will (or should) recapitulate some of its own predecessors by implementing some of the lessons learned and techniques invented by those innovators who have contributed to the improvement and relevance of information systems development and utilization for a wide range of earlier, larger and more traditional application domains.

We note that many instances of important evolutionary progress in new fields have arisen from a combination of judicious use of good ideas from prior disciplines and a willingness to abandon those ideas that don't apply to the new endeavors. We don't necessarily advocate the particular approach to Decision Support Analysis that has been described in this article for all large-scale DSS development efforts, but we do believe that the use of an explicit, consistent, and repeatable methodology has value in structuring specific development projects as well as institutionalizing successful practices. Improvements from an established baseline may be easier and more relevant, as well as more effective, than always starting from scratch.

## Acknowledgement

The methodology presented and the case cited are based on client activities at Research and Planning Inc.

## References

[1] Alter, S.L. Decision Support Systems: Current Practice and Continuing Challenge, Addison-Wesley, Reading, Massachusetts, 1980.

[2] Bennet, J.L. Building Decision Support Systems, Addison-Wesley, Reading, Massachusetts, 1983.

[3] Berrisford, T. and Wetherbe, J. "Heuristic Development: A Redesign of Systems Design," MIS Quarterly, Volume 3, Number 1, March 1979, pp. 11-19.

[4] Boehm, B. "Quantitative Assessment," Datamation, Volume 19, Number 5, May 1973, pp. 49-57.

[5] Constantine, L. and Yourdon, E. Structured Design, Prentice-Hall, Englewood Cliffs, New Jersey, 1979.

[6] Donovan, J.J. and Madnick, S.E. "Institutional and Ad hoc Decision Support Systems and Their Effective Use," Working Paper CR14-27, Massachusetts Institute of Technology, Cambridge, Massachusetts, 1977.

[7] Hamilton, M. and Zeldin, S. "The Functional Life Cycle Model and Its Automation: USE.IT," Journal of Systems and Software, Volume 3, Number 1, March 1983.

[8] International Business Machines Corporation. "Information Systems Planning Guide," White Plains, New York, 1978.

[9] Keen, P.G.W. and Scott Morfon, M.S. Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, Massachusetts, 1978.

[10] Kuhn, T.H. The Structure of Scientific Revolutions, The University of Chicago Press, Chicago, Illinois, 1962.

[11] Little, J.D.C. "Models and Managers: The Concept of a Decision Calculus," Management Science, Volume 16, Number 8, April 1970, pp. B466-485.

[12] McKeen, J.D. “Successful Development Strategies for Business Applications Systems,” MIS Quarterly, Volume 7, Number 2, September 1983, pp. 47-59.

[13] Meador, C.L., Guyote, M.J. and Keen, P.G.W. “Setting Priorities for DSS Development,” MIS Quarterly, Volume 8, Number 2, June 1984, pp. 117-129.

[14] Meador, C.L. and Mezger, R.A. "Selecting an End User Programming Language for DSS Development," MIS Quarterly, Volume 8, Number 4, December 1984, pp. 267-281.

[15] Meador, C.L. and Ness, D.N. "Decision Support Systems: An Application to Cor-

porate Planning," Sloan Management Review, Volume 14, Number 2, 1974, pp. 51-68.

[16] Meldman, J.A. "SMR Forum: Educating Toward Ethical Responsibility in MIS," Sloan Management Review, Volume 23, Number 2, Winter 1982, pp. 73-75.

[17] Ness, D.N. "Interactive Systems: Theories of Design," paper presented at the Wharton Office of Naval Research Conference on DSS, University of Pennsylvania, Philadelphia, Pennsylvania, November 4-7, 1975, pp. 1-24.

[18] Nolan, R.L. "Managing the Crisis in Data Processing," Harvard Business Review, Volume 57, Number 2, March-April 1979, pp. 116-118.

[19] Nolan, R.L. and Norton, D.P. "Recharter DP to the Advance Stages," Stage by Stage, Volume 2, Number 3, 1984, pp. 1-5.

[20] Rockart, J.F. "Chief Executives Define Their Own Data Needs," Harvard Business Review, Volume 57, Number 2, March-April 1979, pp. 81-93.

[21] Ross, D.T. and Schoman, K.E. "Structured Analysis for Requirements Definition," IEEE Transactions on Software Engineering, Volume SE3, Number 1, January 1977, pp. 6-15.

[22] Rudkin, R.I. and Sheve, K.D. "Structured Decomposition Diagram: A New Technique for System Analysis," Datamation, Volume 25, Number 11, October 1979, pp. 130-146.

[23] Shooman, M.L. and Bolsky, M.I. "Types, Distribution, and Test and Correction Times for Programming Errors," International Conference on Reliable Software Proceedings, Los Angeles, California, 1975, pp. 347-357.

[24] Simon, H.A. The Sciences of the Artificial, Massachusetts Institute of Technology, Cambridge, Massachusetts, 1969.

[25] Sprague, Jr., R.H. and Carlson, E.D. Building Effective Decision Support Systems, Prentice-Hall Inc., Englewood Cliffs, New Jersey, 1982.

[26] Urban, G.L. "Building Models for Decision Makers," Interfaces, Volume 4, Number 3, May 1974, pp. 1-11.

[27] Zmud, R.W. "Management of Large Software Developments," MIS Quarterly, Volume 4, Number 2, June 1980, pp. 45-55.

## About the Authors

C. Lawrence Meador is Chairman of the consulting firm Decision Support Technology, Inc. and serves on the Board of Directors of Software Productivity Research, Inc. He received his graduate degrees from the Sloan School of Management and the School of Engineering, MIT. He is also on the academic staff of MIT where he has held various teaching and research appointments for the past twelve years. At MIT he earlier served as a founding member of the Clinical Decision Making Group at the Laboratory for Computer Science, and was Assistant Director of the Sloan School Center for Information Systems Research. His consulting experiences have focused on decision support and knowledge-based systems with particular emphasis on strategic and tactical planning applications. His current research is concerned with future DSS technologies and their impacts, planning large-scale DSS environments, and software technology evaluation and development. He is an editor of the international journals Computer Communications and Comunicacion e Informatica.

Martin J. Guyote is a Senior Consultant and Product Manager with Decision Support Technology, Inc. He received his M.S. and Ph.D. degrees in Cognitive Science at Yale University, and his M.S. degree in Management from the Alfred P. Sloan School of Management at MIT, and has been on the faculty of Boston

University. His research and consulting has included the areas of decision support systems, software productivity, quality and reliability, organizational decision making and organizational psychology. His activities include hardware and software evaluation, decision analysis, user needs assessment, DSS design, development and implementation and research into the issues of DSS and artificial intelligence. He has contributed book chapters and articles to several industry and academic journals.

William L. Rosenfeld is Vice President of Research and Planning, Inc. He received his B.A. in Mathematics and his M.S. in Computer Systems from the State University of New York at Binghamton. He has managed and implemented a number of decision support systems including a model used to evaluate the case flow/profitability of R&D programs as they progress through the project life cycle, an operational expense planning model used to develop and analyze estimates of expenses along several dimensions, and the refinement of a large model that supports financial evaluation of strategic alternatives and scenarios. Prior to his current job, he was a consultant for SofTech, Inc. where he managed the specification, design, and implementation of their in-house labor accounting systems. He also planned and developed a procurement management system for the Department of Energy.
