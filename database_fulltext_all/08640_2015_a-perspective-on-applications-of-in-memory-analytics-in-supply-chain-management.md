---
otero_id: 8640
otero_key: "FVCJS27B"
title: "A perspective on applications of in-memory analytics in supply chain management"
authors: "G.J. Hahn; J. Packowski"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.01.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A perspective on applications of in-memory analytics in supply chain management

G.J. Hahn <sup>a,</sup>⁎, J. Packowski <sup>b</sup>

<sup>a</sup> Business School, CAMELOT Management Consultants Endowed Assistant Professorship for Supply Chain Management, University of Mannheim, Germany <sup>b</sup> CAMELOT Management Consultants AG, Mannheim, Germany

## a r t i c l e i n f o

Available online xxxx

Keywords: Business analytics In-memory database systems Supply chain management Advanced planning Business intelligence

## a b s t r a c t

Big data, advanced analytics, and in-memory database technology are on the agenda of top management since they are seen as key enablers for enhanced business decision-making. In this paper, we provide a comprehensive perspective on applications of in-memory analytics in the <sup>fi</sup>eld of supply chain management (SCM) that use the aforementioned concepts. Our contribution is threefold: First, we develop a top-down framework to position in-memory analytics applications against extant IT systems in SCM. Second, we conduct a bottom-up categorization of 41 in-memory analytics applications in SCM to provide supporting empirical evidence of the efficacy of the framework. Third, by contrasting top-down and bottom-up perspectives we derive implications for research and industrial practice.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Business analytics and related concepts that describe the analysis of business data for decision-making purposes have received widespread attention in both the academic and business communities [1–4]. Top managers generally see business analytics as a differentiating factor for competitive advantage and thus are increasingly interested in capturing this value potential [5,6]. McAfee and Brynjolfsson [7] report an increase of 5 to 6% in productivity for companies that place in the top third of their industries in the use of business analytics. The positive impact of business analytics capabilities on supply chain performance is also con<sup>fi</sup>rmed in several empirical studies [8–10]. Moreover, Brown et al. [11] and Waller and Fawcett [12] indicate the disruptive potential of data-driven decision-making for business and operations management in particular.

In the slipstream of this development, major software providers hype in-memory database technologies [13,14] that enable real-time business intelligence [15] and support big data analytics, i.e., business analytics using large volumes of complex data [1]. In-memory database systems allow for high-speed processing and analysis of large data volumes [16] by storing data directly in main memory, avoiding timeconsuming hard disk operations [17]. The emergence of in-memory database systems has been further promoted by enhanced data management procedures and multi-core hardware architectures that have recently become available [18]. This raises the question whether novel business applications that build on in-memory database systems will only ‘do things differently’ or will actually allow users to ‘do different things’. vom Brocke et al. [19] investigate similar aspects in their case study from the Hilti Corporation when assessing second-order bene<sup>fi</sup>ts that can be captured by applying in-memory technology.

Piller and Hagedorn [20] describe exemplary use cases and potential bene<sup>fi</sup>ts of business applications enabled by in-memory database technology. Real-time business intelligence represents one speci<sup>fi</sup>c use case that has already been investigated for domain-speci<sup>fi</sup>c applications in customer relationship management (CRM) [21] and supply chain management (SCM) [22]. Further applications in SCM deal with real-time order promising [23] and sales and operations planning (S&OP) [24]. In-memory-enabled applications for supply chain planning are generally seen as on the rise [25], which is con<sup>fi</sup>rmed by a multitude of SCMrelated solutions that have been recently launched [26,27]. The relevant literature, however, lacks a comprehensive overview of relevant use cases of emerging in-memory analytics applications in SCM. More importantly, there is a need for studies that yield implications for research and industrial practice in this <sup>fi</sup>eld.

In-memory technology and business analytics are nothing new to SCM, having accompanied the emergence of Advanced Planning and Scheduling (APS) systems at the end of the 1990s [28]. APS systems have been deployed on top of Enterprise Resource Planning (ERP) systems to overcome their shortcomings in production planning and scheduling [29]. For this purpose, they apply forecasting methods and mathematical optimization models that require in-memory cache technology to perform the calculations [30]. However, APS systems have been criticized for several functional and technical shortcomings [29, 31]. Emerging in-memory technology concepts could provide potential avenues for resolving these problems or even constitute an alternative [24]. Unfortunately, we have yet to see a thorough delineation of APS systems in relation to emerging in-memory analytics applications.

The objective of this paper is to develop a comprehensive perspective on analytics applications in SCM that build on in-memory technology. This perspective could answer the abovementioned question whether emerging in-memory analytics applications will only enhance current practice or will eventually support novel approaches in supply chain decision-making. Our approach is threefold: First, a conceptual top-down framework is derived using grounded literature on business analytics approaches and DSS methodology that allows for a thorough positioning of in-memory analytics applications against extant IT systems in SCM. Following a bottom-up empirical approach, we then examine and systematically structure 41 in-memory analytics applications for SCM to outline the current focus. Lastly, by contrasting topdown and bottom-up perspectives we identify areas with the potential for advancing the use of in-memory analytics in SCM and derive impli cations for both research and practice.

## 2. A framework for analytics applications in SCM

## 2.1. Overview and business analytics approach

In this section, we develop a comprehensive framework for analytics capabilities in SCM (see Fig. 1) using a conceptual deductive approach. For this purpose, we build on two recent publications of Holsapple et al. [3] and Mortenson et al. [4] that discuss the foundations of business analytics. Holsapple et al. [3] describe three taxonomies of analytics orientation that differentiate with respect to the analytics task, result, or bene<sup>fi</sup>t. We adopt the task-oriented taxonomy of analytics to structure the pivotal dimension of our framework since it appears to be the most frequently used option and best serves our purpose of characterizing analytics applications.

The task-oriented taxonomy distinguishes three distinct analytics approaches [3,32]: descriptive, predictive, and prescriptive. Descriptive analytics summarize and convert data into meaningful information for reporting and monitoring purposes, but also allow for detailed investigation to answer such questions as “what has happened?” and “what is happening at the moment?” [4]. Data modeling is a prerequisite when making authoritative predictions about the future using business forecasting and simulation. Accordingly, predictive analytics address the questions “what will happen?” and “why will it happen?” [33]. The questions “what shall we do?” and “why shall we do it?” fall within the scope of prescriptive analytics, which involves deriving optimal planning decisions given the predicted future [32].

The key objective of this work is to investigate the phenomenon of emerging in-memory analytics applications in SCM from two angles: <sup>fi</sup>rst, we examine current focus and development areas of respective applications from a business perspective, and second, we delineate these applications in relation to extant information systems in SCM from an IT perspective. Consequently, we expand the framework into two directions using the disciplinary foundations of business analytics at the intersection of quantitative methods, decision-making, and technology, as described in Mortenson et al. [4]. The business perspective is structured along use cases and methodological requirements corresponding to the discipline of quantitative methods. We decided to add the use case dimension to ease application classi<sup>fi</sup>cation in Section 3. DSS concepts and formal IT systems constitute the IT perspective of the framework, corresponding to the disciplines of decision-making and technology. We explain the dimensions and mapping of the taxonomies in detail in what follows.

## 2.2. Use cases and methodological requirements

To the best of our knowledge, only Piller and Hagedorn [20] provide an overview of application patterns of in-memory data management systems. With respect to analytical applications, they identify four use cases: operational reporting, exploratory analysis of mass data, complex analysis, and adaptive planning. However, they only discuss exemplary applications that are motivated primarily by considerations in the ERP domain and do not deal with the speci<sup>fi</sup>c requirements of SCM. We therefore generalized and extended their framework by surveying conceptual papers on ‘supply chain analytics’ that resulted from a structured literature search on titles, abstracts, and keywords. As a result, we distinguish four use cases of analytics applications in SCM: (i) monitorand-navigate [22,34], sense-and-respond [22], predict-and-act [34,35], and plan-and-optimize [34]. The latter three use cases require a broad set of analytical methods beyond simple data aggregation such as data modeling and mining, (discrete-event) simulation, forecasting, and optimization [12].

Monitor-and-navigate use cases are concerned with periodic reporting and/or continuous monitoring of performance metrics as well as data drill-down to navigate root causes on a more granular level [1,22]. In the supply chain context, this includes location data from GPS and RFID tags to increase visibility into supply chain assets and material <sup>fl</sup>ows [34]. Data mining and modeling build the methodological foundation for reactive sense-and-respond use cases [22]. They help to discover

![](/api/attachments/FVCJS27B/fulltext/images/c6fc0b3d8992927b2de7451303be48b7da044f0e4680342c8b55cc0428cea3a1.jpg)  
Fig. 1. A framework for analytics applications in SCM.

Please cite this article as: G.J. Hahn, J. Packowski, A perspective on applications of in-memory analytics in supply chain management, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.01.003

knowledge and patterns that can be translated into business rules for (semi-)automatic responses to prede<sup>fi</sup>ned business events [22,36]. Data modeling involves the broad set of multivariate statistical methods [1].

Predict-and-act use cases are proactive and apply business forecasting as well as simulation methods to support business decisions [12,35]. Within SCM, forecasting relates mainly to time-series analysis of sales data and the prediction of future demand [29,34,37]. Business simulation serves as an umbrella term for various approaches to managing variability. This covers, i.a., scenario and risk pro<sup>fi</sup>le analysis as well as Monte Carlo and discrete-event simulation [12,38], which can be used, for instance, to evaluate the performance of manufacturing systems. In summary, predictive analytics enable sense-and-respond and predict-andact use cases.

Plan-and-optimize use cases in SCM encompass strategic and operational planning [29,34]: While strategic planning supports the con<sup>fi</sup>guration of supply chain networks, operational planning is concerned with managing material and <sup>fi</sup>nancial <sup>fl</sup>ows along the network. Strategic planning takes a long-term perspective of more than two years, uses aggregated data, and is conducted infrequently as part of strategic initiatives [39]. By contrast, operational planing covers a medium- to shortterm horizon, uses granular data, and is an integral part of day-to-day business [30,34]. Strategic and operational planning correspond to prescriptive analytics approaches since they use optimization methods predominantly [12,29].

## 2.3. DSS concepts and types of IT systems

The literature on DSS distinguishes <sup>fi</sup>ve concepts according to the dominant architectural component that provides the functionality [36]: model-, data-, document-, communications-, or knowledge-driven DSS. Due to this paper's focus on business analytics and supporting technology, data-driven and model-driven DSS are in particular focus. Model-driven DSS use quantitative models and corresponding methods to support decision-making [40]. Consequently, both prescriptive and predictive analytics approaches can be part of a model-driven DSS. Access to and manipulation of large datasets are at the core of data-driven DSS that apply descriptive analytics. However, predictive analytics can also be part of data-driven DSS [36].

Information technology has always played an important role within SCM [41]. Investigating the IT systems landscape, one typically <sup>fi</sup>nds ERP systems, Business intelligence (BI) systems, and APS systems [42]. ERP systems perform mainly Online Transaction Processing (OLTP), e.g., materials management or sales order ful<sup>fi</sup>llment, and serve as the backbone of BI and APS systems [43]. ERP systems also provide rudimentary support for monitoring and navigation, covering aspects of a data-driven DSS. APS systems are model-driven DSS that support strategic and operational supply chain planning following a prescriptive analytics approach [29]. They also provide capabilities for demand planning and scenario analysis and thus support business forecasting and simulation requirements [30].

BI systems are mainly data-driven DSS and provide Online Analytical Processing (OLAP) capabilities for reporting/monitoring and navigation [40]. They typically cover simple forecasting methods and approaches for scenario analysis as part of <sup>fi</sup>nancial budgeting [42], and so they are also model-driven DSS. Besides these formal IT systems, there exists a wide variety of expert systems that support statistical analysis, data mining, and simulation [44]. These special-purpose solutions generally use predictive analytics approaches and exhibit elements of modeland data-driven DSS.

## 2.4. Arena for in-memory analytics applications

Having mapped use cases and types of current IT systems, we can apply the resulting framework to delineate a potential arena for emerging in-memory analytics applications in SCM. Monitor-and-navigate use cases are the key domain of BI systems [40]. Classical BI systems perform

OLAP and thus use only aggregated data which are incrementally loaded from various OLTP systems into so-called data cubes at prede<sup>fi</sup>ned time intervals [22]. With the in-memory database technology, the arti-<sup>fi</sup>cial separation of OLAP and OLTP becomes obsolete and transactional data are immediately available for real-time analytics, which could enable a more exception- and alert-based approach to business process management [18].

Predictive analytics approaches have been covered mainly by special-purpose solutions so far and thus have been reserved for expert users. In-memory database systems offer a small but increasing number of built-in functions for predictive analytics [45]. These libraries include, i.a., methods for regression as well as time-series analysis and implement interfaces to statistical computing packages such as R [45]. This allows for the development of business applications that make predictive analytics available to a broader group of non-expert users, as has happened with optimization models and APS systems. Near real-time data availability is a necessary prerequisite for applications that support sense-and-respond and predict-and-act use cases [22,35]. This could involve real-time operations process control using sensor-based data or (semi-)automated supply chain orchestration at the supply- and demand-side interfaces [25,37].

APS systems are prevalent in business for strategic and mostly operational supply chain planning, but have been criticized for having four major shortcomings: First, they do not allow for event-driven, integrated, and interactive planning due mainly to the hierarchical planning paradigm [29]. To make matters worse, <sup>fi</sup>xed rolling schedules, separate planning models with various data structures and metrics, and batchoriented green<sup>fi</sup>eld planning even induce planning nervousness and lead to inconsistent as well as partly obsolete planning results [24,29]. Improvements based on in-memory technology have already helped to overcome these problems using integrated and scalable models that also enable event-driven and incremental planning in an interactive environment [24,26].

The second shortcoming of APS systems relates to their lack of integration into <sup>fi</sup>nancial planning and cost accounting as well as into shop <sup>fl</sup>oor control and manufacturing execution [29]. Since in-memory database technology supports integrated data models across transactional and analytical applications, we expect to see applications that address this gap. Third, topics such as manufacturing systems design and lot-sizing are not or only marginally covered in APS systems [31].

Fourth, APS systems follow a deterministic planning approach [31] that accommodates variability only in an indirect way via safety margins and sensitivity analyses [29]. A more sophisticated approach to managing variability has been introduced recently with the lean planning paradigm [46] and corresponding modules for APS systems targeted at process industries [28]. Following the lean philosophy [47], lean planning aims at reducing variability by establishing a regular and stable demand-driven production <sup>fl</sup>ow via cyclic schedules that ease coordination of interlinked planning processes along the value chain [28]. Lean planning represents a pragmatic approach to managing variability with documented bene<sup>fi</sup>ts from several case studies [28,46]. However, the shortcoming regarding the lack of a stochastic planning approach in APS systems remains.

## 3. Emerging in-memory analytics applications in SCM

## 3.1. Overview and approach

The starting point for our survey is the current Gartner report on in-memory database management systems that contains 16 vendors [48]. However, we could <sup>fi</sup>nd only self-standing in-memory analytics applications that are built on the Oracle Exalytics and SAP HANA platforms. We include all applications that cover supply chain planning and execution capabilities [49] or support integrated business planning and execution in the value chain context [42]. Consequently, classical planning processes such as mid-term S&OP and transactional processes, including purchase-to-pay, plan-to-ship, and order-to-cash, are in scope. Solutions have to be self-standing applications that are more than merely re-implementations of existing solutions using in-memory technology support. We also exclude solutions that provide only frameworks to develop mobility, reporting, and/or visualization features. Finally, applications and solutions need to be of<sup>fi</sup>cially released by May 2014.

In the context of Oracle's Exalytics platform, we identi<sup>fi</sup>ed eleven in-memory applications [50]. Oracle also provides a set of prepackaged reports and data models for real-time reporting that lack self-standing application functionality and thus were not considered in this survey. Six solutions were excluded since they are re-implementations of existing applications with a focus on scalability and processing speed [14,26]. Another three solutions do not deal with value chain-related topics and thus are out of scope. We could not <sup>fi</sup>nd any applications or solutions from third-party vendors that are built on Oracle's inmemory platform. Consequently, two applications remained from the Oracle ecosystem for this survey.

Within the SAP ecosystem, we identi<sup>fi</sup>ed 35 applications directly provided by SAP [51] of which 18 do not belong to the value chain context. One application was removed since it represents the reimplementation of an existing application using in-memory technology support. Furthermore, there is a larger set of applications from thirdparty vendors and solution providers that are built on the SAP HANA platform. To this end, we identi<sup>fi</sup>ed 98 solutions from four sources: (i) 11 released SAP-certi<sup>fi</sup>ed partner solutions [52], (ii) 38 solutions presented as the result of two SAP-initiated competitions among solution providers in 2013 [27,53], (iii) 44 solutions for procurement, manufacturing, SCM, and sales listed in SAP's marketplace [54], and (iv) <sup>fi</sup>ve solutions presented during a conference hosted at MIT in November 2012 [55].

Removing seven duplicates and ten solutions that cover functionality only for mobility, reporting, and/or visualization support, we obtain 81 self-standing in-memory analytics applications of which 54 do not belong to the value chain context. Four applications were excluded since they represent re-implementations of existing solutions using in-memory technology support. Consequently, this investigation resulted in 23 additional applications and a total of 39 applications from the SAP ecosystem.

The 41 applications in focus of this survey were categorized along two dimensions: use case and functional domain. We applied the de<sup>fi</sup>nition of the four use cases described above including the related methodological requirements. For the categorization with respect to the functional domain, we used the following de<sup>fi</sup>nitions [49,42]: Operations management covers the classical value chain activities of procurement, production, and distribution, while sales management is concerned with all decisions at the customer interface regarding selection of the product–market portfolio, pricing and sales volume planning, and operational order promising. Integrated business management considers aspects of coordinating sales and operations management decisions as well as <sup>fi</sup>nancial and risk management implications in supply chain decision-making. To ensure a high degree of inter-subjectivity of the categorization, we followed a two-step approach of discursive alignment of interpretation [56]: First, all 41 applications were classi<sup>fi</sup>ed by both authors independently. Secondly, deviating classi<sup>fi</sup>cations were discussed intensively until consensus could be reached. The results are summarized in Table 1.

## 3.2. Monitor-and-navigate use cases

There is a large set of dashboard applications that support process execution in sales and operations management, allowing for real-time tracking and investigation of prede<sup>fi</sup>ned performance metrics [27,52]. These applications support speci<sup>fi</sup>c activities in purchase-to-pay, plan-to-ship, and order-to-cash processes. This includes purchasing and goods receipt processing (1–2), product/recipe, equipment, and manufacturing process management (3–6), inventory, warehouse, and distribution management (7–10) in the operations domain as well as sales order tracking and ful<sup>fi</sup>llment (11–14), and collections processing (15) in the sales domain. A group of applications in the sales domain (16–18) is tailored speci<sup>fi</sup>cally to the needs of retail store managers supporting sales and inventory navigation [53,54]

Overview of emerging in-memory analytics applications in SCM.

<table><tr><td rowspan="2">Use case</td><td colspan="3">Functional domain</td></tr><tr><td>Operations management</td><td>Sales management</td><td>Integrated business management</td></tr><tr><td>Monitor-and-navigate</td><td>1 SAP SB* for Purchasing2 SAP Invoice and Goods Receipt Reconciliation3 SAP SB for Product Lifecycle Management4 pol Solutions OEE Maschinendaten Cockpit (Equipment Data Cockpit)5 SAP OEE Management6 Systema Big Data Real Time Analysis for Manufacturing7 SAP SB for Inventory Management8 SAP SB for Extended Warehouse Management9 SAP SB for Transportation Management10 SAP SB for Event Management</td><td>11 Infosys RFID-enabled Order Tracking12 Uniorg Order Tracking13 SAP SB for Sales Order Fulfillment14 Oracle JD Edwards EnterpriseOne In-Memory Sales Advisor15 SAP Collection Insight16 Weissbeerger Alcohol Analytics17 NexVisionIX IX-Decision18 FIT Solutions TRENDBOX</td><td>19 SAP SB for Advanced Planning and Optimization20 SAP Supply Chain Info Center21 SAP Working Capital Analytics</td></tr><tr><td>Sense-and-respond</td><td>22 SAP Supplier Infonet23 Infosys SC Risk Management24 MHP Realtime Quality Assurance25 WarwickAnalytics SigmaGuardian</td><td>26 SAP Demand Signal Management</td><td>-</td></tr><tr><td>Predict-and-act</td><td>27 Gicom SKM Strategic Condition Management28 Infosys Asset Optimization29 Clockwork Insight LCM30 Infosys SC Performance Simulator</td><td>31 IBM Filialbestandsoptimierung (Branch Inventory Optimization)32 J&amp;M Weather-correlated Planning33 OPAL Forecast34 CubeServ Aktives Preismanagement (Proactive Pricing)35 Ciber Profit Boost Sales36 We Predict Indico</td><td>37 Trufa SCOOP38 Cundus Bandbreitenplanung (Range Planning)</td></tr><tr><td>Plan-and-optimize</td><td>39 CAMELOT Logistic Transport Cost Analyzer40 Oracle SCM In-Memory Logistics Command Center</td><td>-</td><td>41 SAP Sales and Operations Planning</td></tr></table>

\*. SB = Smart Business

Please cite this article as: G.J. Hahn, J. Packowski, A perspective on applications of in-memory analytics in supply chain management, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.01.003

G.J. Hahn, J. Packowski / Decision Support Systems xxx (2015) xxx–xxx

Three applications (19–21) assume a more comprehensive perspective on value chain processes [51]. They support supply chain planners by tracking planning metrics such as forecast accuracy and stock coverage and deal with cash cycle management as well as corresponding metrics such as days sales and payables outstanding. Furthermore, they provide decision support by visualizing and/or simulating a range of planning scenarios.

## 3.3. Sense-and-respond use cases

Sense-and-respond applications go one step further and apply predictive analytics to discover patterns in the data and to derive corresponding responses for real-time decision-making. They can be categorized in accordance with the three major risk sources in SCM [57]: supply, operations, and demand risk. Our survey includes two applications for supply risk management: SAP Supplier Infonet (22) tracks supplier-related metrics also from third-party sources to observe (negative) changes in supplier performance and to identify sourcing alternatives [51]. Infosys SC Risk Management (23) investigates the impact of disruptions and breakdowns in the supply chain on order ful<sup>fi</sup>llment by highlighting critical orders and <sup>fi</sup>nding alternative sourcing, manufacturing, and/or distribution opportunities [58].

MHP Real-time Quality Assurance (24) is concerned with operations risk due to quality issues. The solution monitors data from engine test benches at automotive manufacturers which allows for early cancelation of defective test runs [59]. In a stage of extension, further data will be collected during endurance testing and evaluated against the data from the test bench to adjust test settings automatically [27]. Exploratory root cause analysis with respect to operations risks from product or process faults is in the focus of WarwickAnalytics SigmaGuardian (25) [60].

SAP Demand Signal Management (26) represents an application for sensing changes in end-customer demand by integrating data from various sources such as internal sales as well as external point-of-sale, market research, and social media data. Reporting and analytics are connected to other applications such as SAP Trade Promotion Planning to derive corresponding measures that mitigate demand risk [51].

## 3.4. Predict-and-act use cases

Our survey covers 12 applications for predict-and-act use cases. Gicom SKM Strategic Condition Management (27) provides insight into purchasing spend and uses simulation to support strategic procurement by predicting the impact of changes to purchase volumes and discount rates [54]. Infosys Asset Optimization (28) and Clockwork Insight LCM (29) concern predictive maintenance in operations management and provide visibility into equipment-related metrics such as availability and utilization [58,61]. Infosys SC Performance Simulator (30) investigates the trade-off between delivery and cost effectiveness in supply chains and uses predictive analytics to connect performance levers such as quality and timeliness as well as productivity and unit cost [58]. By this means, the application assumes a more comprehensive perspective on operational performance in contrast to APS systems that are focused mostly on timeliness and productivity.

Within the domain of sales management, IBM Filialbestandsoptimierung (Branch Inventory Optimization) (31) facilitates the re-allocation of retail stocks across branches, which is especially relevant for products with a <sup>fi</sup>nite selling season such as fashion items. The application uses predictive analytics to forecast sales as well as inventory coverage and proposes corresponding stock transfers to avoid lost sales and costly end-of-season markdowns [27]. J&M Weather-correlated Planning (32) and OPAL Forecasting (33) apply multivariate statistical methods to integrate weather data into demand forecasting for fresh food supply chains [27,62].

Pricing and sales margin improvements are in focus of CubeServ Aktives Preismanagement (Proactive Pricing) (34) and Ciber Profit Boost

Sales (35), which apply cluster and regression analyses to sales order data for this purpose [27,63]. We Predict Indico (36) supports automotive manufacturers with respect to the analysis and prediction of component reliability to manage aftersale costs due to customer claims [64].

Two applications have been identi<sup>fi</sup>ed for the domain of integrated business management: Trufa SCOOP (37) aims at identifying levers for optimizing cash cycle management via correlation analysis and simulation of order-to-cash process metrics [65]. Monte Carlo simulation is applied in Cundus Bandbreitenplanung (Range Planning) (38) to quantify the risk impact of uncertain business parameters [66].

## 3.5. Plan-and-optimize use cases

CAMELOT Logistic Transport Cost Analyzer (39) and Oracle SCM In-Memory Logistics Command Center (40) enable interactive analyses and scenario simulations of logistics networks [67,50]. This includes what-if analyses concerning operational performance levers such as delivery service levels and impact analyses of changes in external business parameters including exchange rates, fuel prices, and carrier rates. These applications can also be used to evaluate strategic network con-<sup>fi</sup>gurations with respect to location, route or product–market selections. By this means, they complement planning in APS systems at the strategic and tactical levels by providing a more granular and accurate view insofar as transactional data are used to model the network <sup>fl</sup>ows. For the sales domain, we could not identify novel applications that support plan-and-optimize use cases.

SAP Sales and Operations Planning (41) supports collaborative S&OP by connecting statistical forecasting for demand planning with rough-cut multi-level supply planning that uses heuristic and optimization-based approaches. A number of planning views can be created to simulate the effect of changes on speci<sup>fi</sup>c metrics, which in turn can be populated back to the baseline scenario [51]. In this respect, the application combines only well-established functionality from APS systems but strengthens the aspects of collaborative and interactive planning that improve the traceability of results and ease cross-functional coordination [29].

## 4. Implications for research and industrial practice

Contrasting top-down and bottom-up perspectives on in-memory analytics applications in SCM, we now discuss implications for research and industrial practice. Half of the applications considered in the survey support monitor-and-navigate use cases with respect to a broad range of operational value chain processes. This con<sup>fi</sup>rms the initial hypothesis that real-time analytics using transactional data – in contrast to conventional OLAP-based BI using aggregated data – represents a novel and promising <sup>fi</sup>eld of application in SCM that is enabled by in-memory database technology. Consequently, this group of applications has received concentrated attention from software providers, which can be explained by the fact that read-only applications with limited analytical capabilities are easier to implement compared with write-access applications given the architecture of in-memory database systems [24]. Further research is needed to evaluate whether promised secondorder bene<sup>fi</sup>ts of this novel type of application can be veri<sup>fi</sup>ed due to a more proactive and event-driven business management approach.

The group of sense-and-respond applications is currently rather small and thus provides ample development opportunities, especially in the <sup>fi</sup>eld of manufacturing execution. One might think of more sophisticated approaches such as statistical process control or automated exploratory data analysis to manage operations risk, aiming at improved product quality and process ef<sup>fi</sup>ciency [12,68]. Real-time analytics applications as outlined above in combination with sensorbased technology could serve as a starting point for these approaches, which involve substantial value potential of 10 to 25% in operating cost reductions [37]. Corresponding applications would also address the abovementioned de<sup>fi</sup>cit of APS systems by closing the gap between the planning and execution levels in operations management. Integrated business management tools represent a second avenue for further development by connecting supply- and demand-side sense-and-respond applications that allow for bi-directional orchestration of the value chain [25,69].

Applications for predict-and-act use cases cover a broad range of forecasting and simulation approaches in sales and operations management as well as integrated business management. Consequently, topics such as predictive maintenance or aftersales management, pricing and margin management, and <sup>fi</sup>nancial performance and risk management are integrated into the value chain context. The af<sup>fi</sup>nity of in-memory database systems for predictive analytics might be one explanation for this comparably large group of applications for predict-and-act use cases in this survey. Due to the integrated data model that contains material and <sup>fi</sup>nancial <sup>fl</sup>ow information from transactional ERP systems, the investigated applications provide avenues for resolving the inadequate functional integration of APS systems into adjacent domains such as marketing and <sup>fi</sup>nance. One major direction for further development could be the integration of predictive queuing and discrete-event simulation methodology into packaged predictive analytics libraries. This would provide the opportunity to develop analytics applications for performance evaluation and design of manufacturing systems [70] that use transactional data from manufacturing execution systems for this purpose.

APS systems play a dominant role in SCM with a focus on plan-andoptimize use cases, which might provide an explanation for the rather small set of emerging in-memory analytics applications in this <sup>fi</sup>eld. Despite this, the survey shows that there is an arena for corresponding applications that complement APS systems with improved scenario analysis and detailed network modeling capabilities. Moreover, there are several uncovered areas in the domains of sales management and integrated business management. Perhaps it would be possible to apply classical operations research methods from revenue management [71] to larger sets of sales order data in real time. Furthermore, aspects of working capital management and especially cash cycle as well as liquidity management are not covered in operational planning although they are closely related to S&OP [42].

Unfortunately, the survey on emerging in-memory analytics applications in SCM has not revealed novel approaches to managing variability in supply chains. For instance, variability originates from uncertain planning parameters such as demand volumes or cost rates and stochastic in<sup>fl</sup>uences that impact on equipment availabilities, processing times, or production yields. Both dimensions of variability are typically addressed separately: stochastic programming-based approaches including their robust and data-driven extensions are concerned mostly with parameter uncertainty [72,73] while queuing theory-related methods focus on modeling the behavior of stochastic manufacturing systems [44,70]. Consequently, a uni<sup>fi</sup>ed stochastic planning approach that addresses both external parameter uncertainty and stochasticity in internal operations is still open for research. Since both approaches combine predictive and prescriptive analytics [44,74], in-memory database systems could provide an appropriate platform for implementation. However, a modeling framework for non-expert users that can be applied to real-life large-scale problems in a day-to-day planning environment would be a necessary prerequisite from the practice perspective.

Our conclusion is that emerging in-memory technology has further enhanced and expanded the landscape of analytics applications that provide decision support for a more diverse set of use cases compared with the narrow focus of incumbent APS systems on plan-andoptimize use cases. By integrating processes at the interface with marketing and <sup>fi</sup>nance, in-memory analytics applications extend the operations-centric view of SCM to a value chain perspective. This includes product and engineering-related topics as well as aspects of aftersales management that are closely interlinked with core supply chain activities. Besides horizontal integration with adjacent domains, we also see concepts and applications that promote vertical integration of the planning level with shop <sup>fl</sup>oor control.

However, we observe only modest progress from a methodological point of view since all of the abovementioned applications use well-established analytics approaches. Moreover, aspects of optimal lot-sizing and manufacturing systems design are still not covered appropriately and the lack of a stochastic planning approach in APS systems remains the single most critical issue from both the research and practice perspectives. At this time, we have to conclude that supply chain managers will only do things (slightly) differently and not start doing different things as a result of emerging in-memory-enabled decision support.

## 5. Conclusion and outlook for further research

In this paper, we provided a comprehensive perspective on applications of in-memory analytics in SCM to answer the question whether novel approaches will fundamentally change supply chain decisionmaking. The paper was structured around three contributions: First, a conceptual framework was developed from the top-down to unify multiple taxonomies and to typecast coherent use cases, allowing us to identify a potential arena for in-memory analytics applications. Second, 41 in-memory analytics applications for SCM were mapped from the bottom-up to the framework to provide an overview of current focus and perspectives for further development. In a <sup>fi</sup>nal step, we derived implications for research and industrial practice in this <sup>fi</sup>eld by contrasting the aforementioned top-down and bottom-up perspectives.

Our <sup>fi</sup>ndings can be summarized as follows: Analytical DSS in SCM can be structured along four use cases according to the required capabilities and underlying methodologies. Monitor-and-navigate use cases are well-established and supported by BI systems. The bene<sup>fi</sup>ts of in-memory database technology in this <sup>fi</sup>eld relate mainly to real-time data availability and uni<sup>fi</sup>ed data models integrating transactional and analytical business processes. Consequently, a large set of dashboard applications has emerged that support operational processes with analytical insights.

In the survey, we found a small but growing number of in-memory analytics applications that support sense-and-respond use cases and a comparably larger group of applications for predict-and-act use cases. This development is consistent with current coverage of analytical decision support in SCM since those applications close functional gaps or simply adopt proven functionality from special-purpose solutions. In-memory database technology provides the corresponding platform with an integrated data model and functional libraries that make predictive analytics capabilities available to a broader group of non-expert users. By this means, the evolution of in-memory analytics proves to be highly analogous to the development and diffusion of APS systems.

APS systems have strongly bene<sup>fi</sup>ted from advancements in inmemory technology that have helped to resolve architectural shortcomings and to further improve performance of plan-and-optimize use cases. Managing variability and thus resolving the deterministic planning approach of APS systems remains the most critical development area in our opinion. With lean planning, however, a practice-oriented approach has been presented that at least aims at reducing the impact of variability as long as there is no comprehensive stochastic planning approach to resolve the variability issue in APS systems. We therefore conclude that supply chain managers will, for the time being, only do things (slightly) differently and not start doing different things.

Opportunities for further research include in-depth analyses of in-memory analytics applications for SCM to investigate their technical architecture, methodological contribution, and potential business bene<sup>fi</sup>ts in greater detail. A further opportunity would be to survey companies that have successfully implemented emerging in-memory analytics applica tions in SCM in order to study how processes, organizational structures, and operational performance have been in<sup>fl</sup>uenced by the adoption.

Please cite this article as: G.J. Hahn, J. Packowski, A perspective on applications of in-memory analytics in supply chain management, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.01.003

## Acknowledgment

We are grateful to Laura Huver who has supported this research by gathering relevant literature and information about in-memory analytics applications. We also thank Dr. David Francas for his valuable comments on previous versions of this article.

## References

[1] H. Chen, R.H.L. Chiang, V.C. Storey, Business intelligence and analytics: From big data to big impact, MIS Quarterly 36 (2012) 1165–1188.

[2] F. Acito, V. Khatri, Business analytics: why now and what next? Business Horizons 57 (2014) 565–570

[3] C. Holsapple, A. Lee-Post, R. Pakath, A uni<sup>fi</sup>ed foundation for business analytics Decision Support Systems 64 (2014) 131–141.

[4] M.J. Mortenson, N.F. Doherty, S. Robinson, Operational research from taylorism to terabytes: a research agenda for the analytics age, European Journal of Operational Re search (2014). http://dx.doi.org/10.1016/j.ejor.2014.08.029.

[5] S. LaValle, E. Lesser, R. Shockley, M.S. Hopkins, N. Kruschwitz, Big data, analytics and the path from insights to value, MIT Sloan Management Review 52 (2011) 21–31.

[6] D. Barton, D. Court, Making advanced analytics work for you, Harvard Business Review 90.(2012).78-83

[7] A. McAfee, E. Brynjolfsson, Big data: the management revolution, Harvard Business Review 90 (2012) 60–68.

[8] P. Trkman, K. McCormack, M.P.V.d. Oliveira, M.B. Ladeira, The impact of business analytics on supply chain performance, Decision Support Systems 49 (2010) 318–327.

[9] M.P.V.d. Oliveira, K. McCormack, P. Trkman, Business analytics in supply chains: the contingent effect of business process maturity, Expert Systems with Applications 39 (2012) 5488–5498.

[10] B. Chae, C. Yang, D. Olson, C. Sheu, The impact of advanced analytics and data accuracy on operational performance: a contingent resource based theory (RBT) perspective, Decision Support Systems 59 (2013) 119–126.

[11] B. Brown, M. Chui, J. Manyika, Are you ready for the era of ‘big data’? McKinsey Quarterly 4 (2011) 24–35.

[12] M.A. Waller, S.E. Fawcett, Data science, predictive analytics, and big data: a revolution that will transform supply chain design and management, Journal of Business Logistics 34 (2013) 77–84.

[13] C. Bryant, Computing innovation powers SAP's makeover, 01/23/2013 (ft.com) http://www.ft.com/intl/cms/s/0/53b5848a-649a-11e2-9711-00144feab49a.html.

[14] D. Henschen, Oracle In-Memory Apps: Hunting Hana, InformationWeek, 04/11/2013. (URL: http://www.informationweek.com/software/information-management/oraclein-memory-apps-hunting-hana/d/d-id/1109489).

[15] S. Chaudhuri, U. Dayal, V. Narasayya, An overview of business intelligence technology, Communications of the ACM 54 (2011) 88–98.

[16] P. Loos. I. Lechtenbörger, G. Vossen, A. Zeier, I. Krüger. I. Müller. W. Lehner, D. Kossmann B. Fabian O. Günther R. Winter In-memory databases in business information systems, Business & Information Systems Engineering 3 (2011) 389–395.

[17] H. Garcia-Molina, K. Salem, Main memory database systems: an overview, IEEE Transactions on Knowledge and Data Engineering 4 (1992) 509–516.

[18] H. Plattner, A. Zeier, In-Memory Data Management: Technology and Applications, second ed. Springer, Heidelberg, 2012.

[19] J. vom Brocke, S. Debortoli, O. Müller, N. Reuter, How in-memory technology can create business value: insights from the Hilti case, Communications of the Association for Information Systems 34 (2014) 151–168.

[20] G. Piller, J. Hagedorn, Business bene<sup>fi</sup>ts and application capabilities enabled by inmemory data management, in: W. Lehner, G. Piller (Eds.), Innovative Unternehmensanwendungen mit In-Memory Data Management, German Informatics Society, 2011, pp. 45–56.

[21] O. Acker, F. Gröne, A. Blockus, C. Bange, In-memory analytics: strategies for real-time CRM, Journal of Database Marketing and Customer Strategy Management 18 (2011) 129–136.

[22] B. Sahay, J. Ranjan, Real time business intelligence in supply chain analytics, Information Management & Computer Security 16 (2008) 28–48.

[23] C. Tinnefeld, J. Krüger, J. Schaffner, A. Bog, A database engine for <sup>fl</sup>exible real-time available-to-promise, IEEE Symposium on Advanced Management of Information for Globalized Enterprises, 2008, pp. 1–5.

[24] D. Schmalzried, C. Cundius, R. Franke, C. Lambeck, R. Alt, W. Zimmermann, R. Groh, Inmemory basierte real-time supply chain planung, in: R. Alt, B. Franczyk (Eds.),Proceedings of the 11th International Conference on, Wirtschaftsinformatik, 2013, pp. 197–211.

[25] T. Payne, Hype Cycle for Supply Chain Planning, Gartner, 2013.

[26] S. Banker, G. Gorbach, Oracle's New In-Memory Value Chain Planning Applications, ARC Adviory Group, 2013.

[27] SAP, SAP HANA partner race, URL: http://global.sap.com/germany/campaigns/2012\_ in-memory/partner-race/race.epx2013 (Last accessed: 05/31/2014).

[28] J. Packowski, LEAN Supply Chain Planning: The New Supply Chain Management Paradigm for Process Industries to Master Today's VUCA World, CRC Press, Boca Raton, 2013..

[29] H. Stadtler, Supply chain management and advanced planning: basics, overview and challenges, European Journal of Operational Research 163 (2005) 575–588.

[30] J.T. Dickersbach, Supply Chain Management With APO: Structures, Modelling Approaches and Implementation of SAP SCM 2008, third ed. Springer, Berlin, 2009.

[31] H. Tempelmeier, Supply chain planning with advanced planning systems, Proceedings of the 3rd Aegean International Conference on Design and Analysis of, Manufacturing Systems, 2001, pp. 1–10.

[32] J.R. Evans, Business analytics: the next frontier for decision sciences, Decision Line 43 (2012) 4–6.

[33] D. Delen, H. Demirkan, Data, information and analytics as services, Decision Support Systems 55 (2013) 359–363.

[34] G.C. Souza, Supply chain analytics, Business Horizons 57 (2014) 595–605.

[35] J. O'Dwyer, R. Renner, The promise of advanced supply chain analytics, Supply Chain Management Review 15 (2011) 32–37.

[36] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2002) 111–126.

[37] J. Manyika, M. Chui, B. Brown, J. Bughin, R. Dobbs, C. Roxburgh, A.H. Byers, Big Data: The Next Frontier for Innovation, Competition, and Productivity, McKinsey Global Institute, 2011.

[38] D.R. Anderson, D.J. Sweeney, T.A. Williams, J.D. Camm, M. Kipp, An Introduction to Management Science: Quantitative Approaches to Decision Making, 13th ed. South-Western/Cengage, Mason, 2012.

[39] M. Goetschalckx, B. Fleischmann, Strategic network design, in: H. Stadtler, C. Kilger (Eds.), Supply Chain Management and Advanced Planning: Concepts, Models, Software, and Case Studies, Springer, Berlin, 2008, pp. 117–132.

[40] D.J. Power, R. Sharda, Model-driven decision support systems: concepts and research directions, Decision Support Systems 43 (2007) 1044–1061.

[41] A. Gunasekaran, E. Ngai, Information systems in supply chain integration and management, European Journal of Operational Research 159 (2004) 269–295.

[42] G.J. Hahn, H. Kuhn, Designing decision support systems for value-based management: a survey and an architecture, Decision Support Systems 53 (2012) 591–598.

[43] B. Reuter, J. Rohde, Coordination and integration, in: H. Stadtler, C. Kilger (Eds.), Supply Chain Management and Advanced Planning: Concepts, Models, Software, and Case Studies, Springer, Berlin, 2008, pp. 247–261.

[44] D. Armbruster, R. Uzsoy, Continuous dynamic models, clearing functions, and discrete-event simulation in aggregate production planning, in: P. Mirchandani (Ed.), Tutorials in Operations Research, INFORMS, Hanover, 2012, pp. 103–126.

[45] SAP, SAP HANA Predictive Analysis Library (PAL) Reference: SAP HANA Appliance Software SPS 07, URL: http://help.sap.com/hana/SAP\_HANA\_Predictive\_Analysis\_ Library\_PAL\_en.pdf2014 (Last accessed: 03/13/2014).

[46] A. Pool, J. Wijngaard, D.-J. van der Zee, Lean planning in the semi-process industry: a case study, International Journal of Production Economics 131 (2011) 194–203.

[47] J.P. Womack, D.T. Jones, Lean Thinking: Banish Waste and Create Wealth in Your Corporation, second revised and updated ed. Free Press, New York, 2003.

[48] R. Edjlali, D. Feinberg, Who's Who for In-Memory DBMSs, Gartner, 2014.

[49] H. Meyr, M. Wagner, J. Rohde, Structure of advanced planning systems, in: H. Stadtler, C. Kilger (Eds.), Supply Chain Management and Advanced Planning: Concepts, Models, Software, and Case Studies, Springer, Berlin, 2008, pp. 109–115.

[50] Oracle, Collaborate resource library, URL: http://www.oracle.com/us/products/applications/collaborate-resource-library-1931221.html 2014 (Last accessed: 05/31/ 2014).

[51] SAP, SAP help portal: SAP HANA innovations for SAP business suite, URL: http:// help.sap.com/in\_memory2014 (Last accessed: 05/31/2014).

[52] SAP, SAP HANA certi<sup>fi</sup>ed partners, URL: http://www.saphana.com/community/ learn/partners/certified-partners2014 (Last accessed: 05/31/2014).

[53] SAP, SAP startup challenge <sup>fi</sup>nalists, URL: http://www.saphana.com/community/ learn/startups/sap-hana-startup-challenge/finalists2013 (Last accessed: 05/31/ 2014).

[54] SAP, SAP HANA marketplace, URL: http://marketplace.saphana.com2014 (Last accessed: 05/31/2014).

[55] MIT, Technology in manufacturing: improving supply chain performance, URL: http://supplychain.mit.edu/november-14-2012-conference-presentations2012 (Last accessed: 05/31/2014)

[56] R. Wilding, S. Seuring, S. Gold, Conducting content-analysis based literature reviews in supply chain management, Supply Chain Management 17 (2012) 544–555.

[57] O. Tang, S.N. Musa, Identifying risk issues and research advancements in supply chain risk management, International Journal of Production Economics 133 (2011) 25–34.

[58] R. Makad, In-memory processing: a case study, URL: http://techtv.mit.edu/genres/ 20-entrepreneurship/videos/21692-supply-chain-innovation-conference-in-memory-processing-a-case-study2012 (Last accessed: 05/31/2014).

[59] MHP, SAP HANA partner race: Interview mit Dr. Hagen Radowski, URL: http://www. youtube.com/watch?v=\_\_bDSxjeiGQ2013 (Last accessed: 05/31/2014).

[60] D. Somers, Removing Hypotheses for Fault-Finding in Six Sigma to Revolutionise Quality Management, Supply Chain Digital, 02/20/2014. (URL: http://www. supplychaindigital.com/global\_logistics/removing-hypotheses-for-fault-<sup>fi</sup>nding-insix-sigma-to-revolutionise-quality-management).

[61] Clockwork, Clockwork predictive analytics and SAP's HANA, URL: http://vimeo.com/ channels/548395/639229612013 (Last accessed: 06/04/2014).

[62] OPAL, Forecasting the supply chain with SAP HANA cloud, URL: http://www. youtube.com/watch?v=8qIERdjXQTM2014 (Last accessed: 06/02/2014).

[63] Ciber, Pro<sup>fi</sup>t Boost Sales solution overview, URL: http://www.ciber.com/us/index. cfm/insights/video-library/?q=profit-boost-sales-solution-overview2014 (Last accessed: 05/31/2014)

[64] We Predict, We predict with SAP HANA, URL: http://vimeo.com/973806602014 (Last accessed: 06/04/2014)

[65] Trufa, Trufa SCOOP (Seeking Cash Opportunities in Operational Processes), URL: https://www.youtube.com/watch?v=a5zA1-Y3LTM2014 (Last accessed: 05/31/ 2014).

[66] Cundus, Bandbreitenplanung: Verzahnung von Planung und Risikomanagement, URL: http://www.youtube.com/watch?v=ENNaAWZZONE2013 (Last accessed: 05/31/ 2014).

[67] CAMELOT Management Consultants, CAMELOT Logistic Transport Cost Analyzer, URL: http://www.youtube.com/watch?v=XZ9PjKphsZ42013 (Last accessed: 05/31/2014).

[68] J.S. Oakland, Statistical Process Control, sixth ed. Butterworth-Heinemann, Burlington, 2008.

[69] L. Cecere, Market-Driven S&OP: A Guidebook on How to Build a Market-driven S&OP Process, Supply Chain Insights, 2012.

[70] W.J. Stewart, Probability, Markov Chains, Queues, and Simulation: The Mathematical Basis of Performance Modeling, Princeton University Press, Princeton, 2009.

[71] K.T. Talluri, G. van Ryzin, The Theory and Practice of Revenue Management, Kluwer, Boston, 2005

[72] J.R. Birge, F. Louveaux, Introduction to Stochastic Programming, Springer, New York, 2011.

[73] V. Gabrel, C. Murat, A. Thiele, Recent advances in robust optimization: an overview, European Journal of Operational Research 235 (2014) 471–483.

[74] N.D. Domenica, G. Mitra, P. Valente, G. Birbilis, Stochastic programming and scenario generation within a simulation framework: an information systems perspective, Decision Support Systems 42 (2007) 2197–2218.

![](/api/attachments/FVCJS27B/fulltext/images/a11d8dda3e24212dc7bf86912cb67648a98c767bbe9bdcc40b938ca5d3e27e1b.jpg)

Gerd J. Hahn is an Assistant Professor for Supply Chain Management at the University of Mannheim, Germany. Prior to this, he has worked several years as a management consultant on strategic IT management issues. He received his Ph.D. in Management Science from Catholic University of Eichstaett-Ingolstadt in 2011. His research has been published in the Journal of the Operational Research Society, the International Journal of Production Economics, Decision Support Systems, and several conference proceedings. He has presented his work at the Annual Meeting of the POM Society, the European Conference on Operational Research, and the INFORMS Annual Meeting. His research interests focus on decision support and IT systems in supply chain management, supply chain

performance and risk management, supply chain <sup>fi</sup>nance, and robust optimization methods.

![](/api/attachments/FVCJS27B/fulltext/images/76661ed8efbfeade7a4e0847c7a113f1ca37589cd4d846cad5d9bddb4b7b19d3.jpg)

textbook LEAN Supply Chain Planning: The New Supply Chain Management Paradigm for Process Industries to Master Today's VUCA World, published by CRC Press, 2013.

Josef Packowski is co-founder and Managing Partner of the Camelot Consulting Group, an international consulting group focused on value chain management, based in Mannheim, Germany. He received his doctoral degree in Business and Information Technology from Saarland University. Besides his professional work, he is a lecturer for Supply Chain Management and Advanced Planning Systems at the University of Mannheim. He is a respected industry consultant with over 25 years of experience and has advised companies such as Astellas, Astra-Zeneca, Bayer, BASF, DSM, Henkel, Lyondell Basell, Merck, Novartis, Roche, and Sabic. He is invited regularly as plenary speaker at industry symposia and he is co-author of several articles in practitioners' journals on process industries. Furthermore, he is the author of the

Please cite this article as: G.J. Hahn, J. Packowski, A perspective on applications of in-memory analytics in supply chain management, Decision Support Systems (2015), http://dx.doi.org/10.1016/j.dss.2015.01.003
