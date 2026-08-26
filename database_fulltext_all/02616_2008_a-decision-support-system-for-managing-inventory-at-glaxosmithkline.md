---
otero_id: 2616
otero_key: "KXWS8S5J"
title: "A decision support system for managing inventory at GlaxoSmithKline"
authors: "Jennifer Shang; Pandu R. Tadikamalla; Laurie J. Kirsch; Lawrence Brown"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.04.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for managing inventory at GlaxoSmithKline

Jennifer Shang <sup>a,</sup>⁎, Pandu R. Tadikamalla <sup>b</sup>, Laurie J. Kirsch <sup>c</sup>, Lawrence Brown <sup>d</sup>

<sup>a</sup> The Joseph M. Katz Graduate School of Business, 230 Mervis Hall, University of Pittsburgh, Pittsburgh, PA 15260, USA

<sup>b</sup> The Joseph M. Katz Graduate School of Business, 258 Mervis Hall, University of Pittsburgh, Pittsburgh, PA 15260, USA

<sup>c</sup> The Joseph M. Katz Graduate School of Business, 361 Mervis Hall, University of Pittsburgh, Pittsburgh, PA 15260, USA

<sup>d</sup> GlaxoSmithKline, 1000 GSK Drive, Pittsburgh, PA 15108, USA

## a r t i c l e i n f o

Article history: Received 22 March 2007 Received in revised form 10 April 2008 Accepted 13 April 2008 Available online 25 April 2008

Keywords: Decision Support Systems Spreadsheet modeling Inventory Consumer healthcare product

## a b s t r a c t

Firms often turn to supply chain software to streamline and standardize operations. A challenge is how to best utilize the data provided by the software. One approach is to import the data into Decision Support Systems (DSS) to build special-purposed decision aids. This paper presents an effective inventory management model for GlaxoSmithKline (GSK). The DSS effectively determines the safety stock level and the number of weeks forward coverage (WFC) for each SKU (Stock Keeping Unit). We discuss GSK's experiences relative to the literature on DSS design, implementation, and usage. This research shows implementing the proposed decision support system would provide GSK a distinct competitive advantage. However, careful implementation is necessary to fully realize the potential of the DSS.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Many contemporary organizations face the challenge of optimizing their global supply chain. One tool to facilitate such optimization is the use of supply chain management (SCM) software packages, including enterprise-wide resource planning (ERP) systems, such as SAP R/3 and Manugistics [9]. Indeed, <sup>fi</sup>rms have invested considerable sums of money in such systems. In 2005, worldwide, <sup>fi</sup>rms spent \$25.4 billion on ERP software, support, and services, and it is estimated that spending increased by 14% in 2006 to \$29 billion [15]. AMR Research predicts that the ERP software market will continue to grow by an average annual rate of 10% [15].

Enterprise-wide SCM software packages are designed to automate many business processes, providing seamless integration across functional modules and a centralized data repository, along with standardized business processes and data. This type of integration facilitates corporate-wide, global decision-making as it makes it feasible to view, combine, and manipulate data across the organization [5]. The availability of such data should improve decision-making in organizations. However, reports in the practitioner and academic literatures suggest that decision-makers often struggle to make sense of the available data and use it wisely. A case study of Dow Corning, for example, highlights this issue. After the global implementation of SAP R/3, some Dow Corning users, who were accustomed to managing operations from a local perspective, were uncertain how to read and interpret company-wide product and inventory <sup>fi</sup>gures [21]. Indeed, organizational and individual learning represents a major challenge facing many <sup>fi</sup>rms that implement SCM software [12,20,27].

This underutilization of data raises the question of how to help decision-makers in organizations harness the incredible wealth of data available in SCM software. Decision Support Systems (DSS), a type of information system designed to support semi-structured or unstructured managerial activity [6,30], are ideally suited to bridge the gap between enterprise systems and decision-makers. DSS, especially in the form of spreadsheets, have become mainstream tools that organizations routinely use to improve managerial decision-making [1,18], often by importing data from enterprise-wide information systems into spreadsheets to address speci<sup>fi</sup>c business problems. Moreover, DSS also have the potential to serve as a catalyst to improve the decision-making process as they provide the capability to organize and share knowledge, as well as to create knowledge, providing structure and new insight to managers [8].

The purpose of this paper is to report on the design, implementation, and usage of a speci<sup>fi</sup>c DSS at GlaxoSmithKline (GSK) that takes advantage of the data in GSK's implementation of Manugsitics software. In the next section, we start with a brief review of the DSS literature. This is followed by a description of GSK, the goals of the DSS project, and the formulation of a GSK business problem as a DSS model and solution. In Section 4, we present the spreadsheet model, including a description of the model itself, the data inputs, and the simulation model. We then provide an explanation of how the DSS can be used. This is followed by a discussion of the model outputs. In Section 7, we comment on the current status of the implementation and future steps for implementing and improving the DSS; we close with a few summary comments.

## 2. Literature review

Decision Support Systems are a class of information systems intended to assist managers in decision-making. Unlike transaction processing or operational systems, DSS incorporate speci<sup>fi</sup>c capabilities, such as “what-if” processing, optimization, and simulation, to support managers as they wrestle with various types of decisions [14,18]. The <sup>fi</sup>rst reported DSS appeared in the 1960s, and the development of the concept of Decision Support Systems, as well as the technology used to implement DSS, blossomed in the 1970s and 1980s [1,2]. As information technology changed, the platform for DSS did also: in the 1990s DSS were increasingly implemented on client/ server platforms as opposed to mainframe computers, and eventually migrated to Internet technologies with vendors now exploring ways of using Grid computing capabilities [2]. Not only is the hardware changing, but the design and functionality of DSS are also evolving. For example, beginning in the 1980s, scholars and practitioners turned their attention to the development of Group Decision Support Systems (GDSS) to support decision-making and communication tasks in groups or teams [2,4]. More recently, practitioners and scholars have been exploring ways to use DSS to support distributed decisionmaking, knowledge management, and business intelligence [1,2,8]. The growth of enterprise-wide software packages, data warehouses, and data marts found in contemporary organizations also fueled changes in DSS capabilities and functionality, as these software technologies supply an enormous amount of data for manipulation and analysis in DSS applications.

As with the deployment of any type of information system, implementing DSS presents a number of challenges. The lack of commitment towards the DSS itself [10] and the lack of suf<sup>fi</sup>cient resources (people, technology, or <sup>fi</sup>nancial) can contribute to implementations dif<sup>fi</sup>culties [19]. In their study, Poon and Wagner [19] demonstrate the importance of executive championship, as well as the clear link to business objectives for successful implementations of DSS. A number of studies have also demonstrated that user participation is critical for successfully implementing a DSS, as are user training and perceived bene<sup>fi</sup>ts, organizational receptiveness to change, and a culture of knowledge sharing [7,28].

A number of researchers have examined the use of DSS in <sup>fi</sup>rms, evaluating the systems in terms of their effectiveness and impact on decision-makers. Santhanam and Guimaraes [23] observe that DSS are evaluated in a variety of ways, including usage statistics, user satisfaction scores, and <sup>fi</sup>nancial analyses. They also note that system usage can be predicted and studied using a theoretical framework such as the Technology Acceptance Model or the Theory of Planned Behavior. Some researchers have observed the positive effects of DSS, for example, an increased number of decision alteratives, more quality time spent on decision-making, increased con<sup>fi</sup>dence on the part of decision-makers, and improved decisions [10,29]. However, researchers have reported that DSS can also have unintended negative consequences [7,19]. For example, DSS can be restrictive and may constrain individual decision-making processes [26]. Further, the use of DSS without clear understanding of the problem context may lead to less-than-ideal conformity rather than improved decisionmaking [22].

Inventory management is an essential managerial activity [25]. With the advent of SCM software, <sup>fi</sup>rms have a large amount of data available to them about their inventory, including data about inventory turnover, current levels, and safety stock. However, inventory management is an unstructured and complex problem, and an SCM package may not present the data in the form needed, suggesting that an appropriately designed DSS might help <sup>fi</sup>rms more ef<sup>fi</sup>ciently and effectively manage their inventory. At the start of our project, GlaxoSmithKline executives noted that they consistently maintain a higher inventory level than their competitors, and while they want to ensure adequate inventory to service their customers, they also recognize a need to lower inventory levels to decrease costs. As will be shown, the approach taken to design a Decision Support System for GSK, as well as the DSS itself, contribute to GSK's ability to more effectively manage their inventory while maintaining a high service level to customers. The speci<sup>fi</sup>c goal was to develop a model to determine the best level of safety stock and the accompanying weekly forward coverage at the SKU level for GSK's inventory.

## 3. The <sup>fi</sup>rm and the problem

GlaxoSmithKline (GSK) is a pharmaceutical company headquartered in the UK with operations based in the U.S. It is the second largest pharmaceutical company in the world with \$35 billion in sales, which accounts for 7% of global pharmaceutical sales. The North American headquarters are in Pittsburgh, PA, and Parsippany, NJ. About \$7 billion of GSK's revenues are derived from Consumer healthcare products, which include over-the-counter (OTC) medicines, oral care products and nutritional healthcare drinks, all of which are among the market leaders. In the OTC segment, popular products include Nicorette, Tums, and Contac. The oral care products consist of Aquafresh, Sensodyne, and Polident brand names. GSK also provides nutritional drinks such as Horlicks. Its major competitors in the consumer healthcare markets include Colgate–Palmolive, Johnson & Johnson, P<sup>fi</sup>zer, Procter & Gamble, Unilever, and Wyeth. Thirty-six percent of OTC sales are in North America.

In this project, we focus on 51 brand groups, ten of which have annual sales greater than \$100 million. There are altogether

1200 product types. Annually many new and improved products are introduced, and they replace 20–30% of the existing ones. The GSK supply chain includes four plants, thirty contractors, two co-packing facilities, and four regional distribution centers (RDCs). There are 400 customer warehouses and 25,000 retailer ‘ship-to’ locations. Annually 80,000 customer orders are received, and 20 million cases of products are shipped. Average inventory valuation is \$115 million. In GSK, inventory level is measured in Weeks Forward Coverage (WFC), which is the number of weeks the inventory can cover and is based on the 6- month forecasted demand. Current WFC is 17 weeks. GSK's dollar <sup>fi</sup>ll target is set at 96.6%, whereas that of the new item launches is aimed at 100%.

Although fairly pro<sup>fi</sup>table, compared with competitors, GSK consistently maintains a higher inventory level. Our goal in this project was to develop a model that would determine the best level of safety stock and the accompanying WFC at the SKU level for GSK's products, such as Nicorette and Aquafresh. Determining optimal inventory levels in the multiechelon supply chain setting is a complex problem that requires trade-off of various stochastic variables. While it is desirable to provide a high service level (SL) to customers, it is also important to keep inventory levels low to save on cost. A high inventory level is unhealthy, because it represents an investment with very low return. Since inventory turnover is the cost of goods sold divided by the average inventory level, a low turnover implies excess stock, cash tie-up, sluggish sales, ineffective buying, or vulnerability to falling prices.

## 3.1. Goals and deliverables

Despite the unattractiveness of holding excess inventory, many companies maintain high safety stocks in an attempt to mitigate the probability of inventory backlog and loss of good will. It is a balance many <sup>fi</sup>nd hard to manage. GSK wanted a spreadsheet-based decision support system to determine the most appropriate WFC by SKU, and top management approached us to build such a DSS. The inventory problem is complex because it encompasses many items, i.e. 1200 SKUs, and is accompanied by unreliable forecasts and lead times. On average, the forecast accuracy is at 70%, while that for the special packaged products is at 40–60%. It is obvious that for any supply chain to be effective, the demand and the replenishment planning functions need to integrate seamlessly with the safety stock decision.

In making the SKU level forecasts and establishing replenishment plans, the decision support system (DSS) that we developed not only adapts the traditional inventory management techniques, but also takes into account the interaction of these functions. The proposed model can be easily modi<sup>fi</sup>ed and applied to different product lines that share comparable inventory management and marketing patterns. By changing the input variables, such as lead time, lot size, historical data time period, and monthly forecasts for any GSK product, the corresponding “optimal” results for any speci<sup>fi</sup>ed service level can be obtained. Long term improvement plans such as reducing lot size, increasing review frequency, improving forecast accuracy, and decreasing the number of promotions can also be addressed.

Fig. 1 shows GSK's supply chain planning process. It points to the steps and the course of actions necessary to satisfy customer need. The <sup>fi</sup>rst three steps are to forecast the demand for the planning horizon by combining sophisticated forecasting techniques, computer models, and executive opinions. Production Planning and Inventory Management in step 4 is the focus of this project. This step determines the timing and quantity of production, and converts the information about beginning inventory, forecasts, and customer orders into projected inventory, procurement requirements, and “available-to-promise” inventory. Step 5 centers around distribution management, and step 6 is the performance evaluation of the entire supply chain.

![](/api/attachments/KXWS8S5J/fulltext/images/3964feb11d2ed3fd389a45c33bd9f292dc492a4ad30de9c4d06f98065c9f05d4.jpg)  
Fig. 1. Supply planning process.

A screen shot of the Manugistics system, which GSK currently uses, is given in Fig. 2. It shows where the DSS <sup>fi</sup>ts in the overall inventory management process supported by the Manugistics software. The DSS helps decision-making in row 7, where safety stock (SS) is a user input. There the inventory relationship can be expressed as: On-Hand Inventory+Scheduled Receipts+In-Transit Inventory−Total Demand−Safety Stock= Projected Available. Currently, SS is subjectively determined. The DSS offers a more systematic approach for a better decision

## 3.2. Transforming the GSK problem into a Decision Support System — a conceptual view

We started with a big picture of “converting” GSK's problem into a DSS: the inputs, the model, and the outputs. Fig. 3 gives an overview of the planned DSS. At this stage of our project, the main concerns were the input and the output. We needed to determine the system inputs so that we could request the data from GSK's management. We also needed to articulate the outputs in terms of GSK's needs (“answers” management can use and rely upon).

A reasonable set of input variables seemed to be: historical forecast and demand, month-end inventory, the production batch size, and the lead time. We decided that the outputs from the DSS would be a point estimate of the WFC (which is equivalent to safety stock in traditional inventory management terminology) at the SKU level. In addition to providing this WFC, we wanted to give management the <sup>fl</sup>exibility to study through a simulation model the effects of WFC on the service level.

![](/api/attachments/KXWS8S5J/fulltext/images/59a6626065fc88461bbd50b963c17bbdb40bd88f03f1aeb5c8fe70c94760f5ab.jpg)  
Fig. 2. A screen shot of the Manugistics system and where the safety (SS) decision (in row 7) <sup>fi</sup>ts in the ERP

![](/api/attachments/KXWS8S5J/fulltext/images/5e7fb027ed0bb33b2259a60b941863417e2eb483ce74cfff28d1524997f9606c.jpg)  
Fig. 3. Model outline for proposed DSS.

As we designed the DSS, we worked closely with several managers from GSK, including the Vice-President of Customer Supply, the Business Unit Planning Manager and Site Coordinator, the Director of Customer Service, the Manager of Planning Systems & Forecasting Relationships, and the Director of Distribution. They all provided valuable and timely feedback; the Business Unit Planning Manager and Site Coordinator was especially active and responsive to our needs. Top management were very interested and involved in the project and closely monitored the steps taken to design and build the DSS. Every key procedure and decision were explained to the managers, and the design process was transparent to them. Because of the commitment and involvement of these managers from GSK, there was a high degree of trust in the development team.

## 4. The spreadsheet model

GSK's ordering system is comparable to a Periodic Review System in which the inventory level of each SKU is examined periodically, a month in GSK's case. The periodic review inventory model [16,31], shown in Fig. 4, forms the base for determining the WFC for our model.

Let

R review period, which is a month in GSK's case

$Q _ { t }$ order quantity for the review period t

$S _ { t }$ target inventory level for the time period t

$$
L
$$

$I _ { t }$ on hand inventory at the beginning of t

$d _ { t }$ average weekly demand for the period t

$\sigma _ { t }$ standard deviation of the weekly demand for period t

$\mathtt { S L }$ service level

$B _ { t }$ quantity backordered in period t

$\mathrm { S R } _ { t }$ scheduled receipts in period t

$z$ standard normal percentile, z \~ N(0,1)

Φ the cumulative density function (cdf) of the standard normal distribution.

The following four equations form the foundation of our inventory model:

At the beginning of a review period (R), an order (Q <sub>t</sub>) is placed to bring the inventory position up to the target inventory level (S ).

$$
Q _ {t} = S _ {t} - I _ {t}\tag{1}
$$

Conventionally the target inventory level (S) is assumed to be constant. In the case of GSK, however, this does not apply since many of the company's products are seasonal. GSK's S is the expected demand during the protection interval plus safety stock. It changes with time and can be expressed as

$$
S _ {t} = d _ {t} \cdot (R + L) + z \cdot \sigma_ {t} \cdot \sqrt {(R + L)}\tag{2}
$$

Note that the protection interval is the time between two consecutive review periods (R) plus the lead time (L). At GSK, lead time demand is stochastic. Due to seasonality, the average weekly demand, $d _ { t } ,$ and the standard deviation of the weekly demand, $\sigma _ { t } ,$ vary with the planning horizon. For a given service level SL, the z value is determined as

$$
z = \Phi^ {- 1} (\mathrm{SL})\tag{3}
$$

The Inventory position $I _ { t }$ at the end of the planning horizon, t, is de<sup>fi</sup>ned as the beginning on-hand inventory $\left( I _ { t - 1 } \right)$ at time t, plus scheduled receipts (SR ) minus backorders (B ) and demand, thus

$$
I _ {t} = I _ {t - 1} + \mathrm{SR} _ {t} - B _ {t} - d _ {t}\tag{4}
$$

As with most practical situations, it is clear that GSK's ordering process is more sophisticated and dynamic than the

Order Quantities $\mathsf Q _ { 1 } , \mathsf Q _ { 2 } , \mathsf Q _ { 3 }$ are in Multiples of Lot Size

![](/api/attachments/KXWS8S5J/fulltext/images/4831d7b9041c0cec95dd71898784ee3604ccf14257444fe5ad63d432bbbbe285.jpg)  
Fig. 4. A generic periodic review inventory system.

above traditional model and some of the model's inherent assumptions may not hold. GSK's target inventory level changes with the forecast over the review period. The lead time, the demand, and its distribution during the lead time are not stable. For example, the demand for Nicorette (a smoking cessation product) around the Great American Smokeout Day (the third Thursday of November) and the National Public Health Week (the <sup>fi</sup>rst full week of April) is much higher than usual. Order quantities are subjected to an initial lot size constraint and subsequent incremental batch size restrictions. Simple inventory models like those found in the literature cannot resolve the inventory problem encountered to the accuracy desired, let alone optimize inventory operations. For each SKU, we therefore take advantage of the concepts in Eqs. (1)–(4), and employ spreadsheet modeling techniques to develop a user-friendly Excel-based DSS. A simulation model is then developed to address the various what-if situations. So GSK can visually compare the results and empirically show that the recommended DSS provides the most ef<sup>fi</sup>cient and appropriate SS and WFC, while meeting the required service level.

## 4.1. Data Inputs

The actual data used in the Excel model turned out to be a little more than what we envisioned. The data included forecasts for the next six months, the historical actual demand and past forecast by SKU, the lot size, and the incremental batch size in which the amount of an SKU can be ordered. The data also allowed the user to specify the historical time period to be considered. In the case of an SKU with large variation between actual demand and forecast demand, we might have wanted to specify only a short historical period. Typically, a two-year historical period of monthly data is used to calculate differences between demands and forecasts.

The model also allowed users to specify inclusion or noninclusion of outliers when calculating the standard deviation of SKU demand. The inventory planner would then be informed if huge forecast errors are common for a particular SKU and subsequently would decide if the situation warranted including the outliers. The outliers normally occurred when there were sudden surges of demand of an SKU caused by promotions, non-availability of a similar product in stock, special packaging involving multiple products packed into a single item, etc. Removing these outliers from the model would help the model in not recommending more than the requisite inventory, particularly useful when the inventory manager knew that the likelihood of the surges in demand in the future is negligible. A detailed summary of the inputs for our simulation model is given in Fig. 5.

![](/api/attachments/KXWS8S5J/fulltext/images/25354f457158f3947d5f98816b768efb6dc88359a7b41a8d6bbed4dd34daf073.jpg)  
Fig. 5. Summary of inputs information for the user interface module

## 4.2. Simulation model

The inventory model contains heuristics, and the heuristics are imbedded in the simulation. There are several reasons why a simulation is needed:

(1) Many of the product demands in GSK are seasonal. Average demand and standard deviation of demand vary greatly depending on the planning horizon. Due to the stochastic nature, dynamic data has to be replicated through simulation. Thus simulation is chosen for its suitability for generating weekly demand.

(2) The target inventory level, needed by the spreadsheet modeling, is not constant. It changes with the forecast over time. Such information needed by the heuristic model is best supplied by simulation. Note that the simulation is not to replace the heuristic inventory model. Instead the inventory model uses simulation to generate valuable information that helps decisionmaking.

(3) To answer what-if questions under different safety stock levels, a simulation model is necessary. By experimenting with various levels of SS, one can empirically learn if the recommended SS performs better than the other alternatives, both in terms of inventory and service levels.

Since GSK's demand and replenishment characteristics are dynamic, and most input data vary with time and require continuous monitoring, it made the most sense to build an addin or a stand-alone program to address this situation. The standalone spreadsheet simulation module is described below.

![](/api/attachments/KXWS8S5J/fulltext/images/fe0427e0bca7e759b790c909ed4121f1dc28dc4335a144522af58d32b5c5b239.jpg)  
Fig. 6. Outline of the simulation logic

Nomenclature for the simulation logic of Fig. 6

<table><tr><td> $d_t$ </td><td>Simulated demand at time t</td></tr><tr><td> $F_t$ </td><td>Forecast demand at time t</td></tr><tr><td> $I_t$ </td><td>Inventory on hand at the end of time t</td></tr><tr><td> $-I_t$ </td><td>Unmet demand at the end of t</td></tr><tr><td>LS</td><td>Lot size</td></tr><tr><td>Max SS</td><td>Maximum safety stock allowed</td></tr><tr><td>Min SS</td><td>Minimum safety stock allowed</td></tr><tr><td> $n_t$ </td><td>Number of lots ordered at time t</td></tr><tr><td> $N_s$ </td><td>Total number of simulation steps needed for a specific SKU</td></tr><tr><td> $N_r$ </td><td>Total number of runs in a step specified by the user</td></tr><tr><td>r</td><td>Run (iteration) index in a step</td></tr><tr><td>s</td><td>Step index</td></tr><tr><td>SI</td><td>Step interval for the type (SKU) of safety stock</td></tr><tr><td> $SL_r$ </td><td>Service level in run r</td></tr><tr><td> $SL_s$ </td><td>Average service level in a step s</td></tr><tr><td>SS</td><td>Number of units of safety stock</td></tr><tr><td>t</td><td>Month index</td></tr><tr><td>T</td><td>Number of months in a planning horizon</td></tr><tr><td> $UD_t$ </td><td>Cumulative unmet demand at time t</td></tr><tr><td> $WFC_r$ </td><td>Average number of week forward coverage in run r</td></tr><tr><td> $WFC_s$ </td><td>Average number of week forward coverage in step s</td></tr></table>

## 4.2.1. Demand generation for future time periods

As pointed out above, a natural choice to derive probabilistic data for inventory is simulation. We use the historical error and forecast to simulate monthly demand for the planning horizon, usually six months. Forecasts were provided by GSK's forecasting and planning division, which incorporates opinions from other departments (steps 1–3 of Fig. 1). By <sup>fi</sup>tting the distribution of past forecasting error, we are able to simulate the actual demand. For instance, if the historical error for week t is normally distributed, $N ( \mu _ { t } , \sigma _ { t } )$ then the demand simulated for week t would be

$$
d _ {t} = F _ {t} + N (\mu_ {t}, \sigma_ {t})\tag{5}
$$

where $F _ { t }$ is the forecasted demand for week t.

The difference between the actual demand and the available inventory determines the unmet demand. For each lot size (step), the DSS replicates 200 runs for each SS level.

The service level is the average in each step. This process repeats according to the incremental SS level speci<sup>fi</sup>ed by the user. Summary of the simulation logic is given in Fig. 6. The symbols used in Fig. 6 are listed in Table 1. In Fig. 6, the simulation starts with forecast of the demand, and at the end it shows the most appropriate SS, WFC, and SL for the studied SKU, and graph relationships.

The number of lots to order for time t is approximated by

$$
n _ {t} = \left[ (F _ {t} + F _ {t + 1} - (I _ {t - 1} - \mathrm{SS})) / \mathrm{LS} \right] - n _ {t - 1}\tag{6}
$$

The above equation looks ahead two time periods, i.e. the current and the next month's forecasts $( F _ { t } { + } F _ { t + 1 } ) .$ SS has to be subtracted from the on-hand inventory $\left( I _ { t - 1 } \right)$ since SS is a buffer, not for regular supply. The demand, $\left( F _ { t } { + } F _ { t + 1 } { - } ( I _ { t - 1 } { - } \mathsf { S } \mathsf { S } ) \right)$ , is translated into the number of lots by dividing it by the lot size (LS). Finally, the number of lots, $n _ { t - 1 } ,$ , to arrive from the previous decision is subtracted to account for the scheduled receipt. Note that different SS is simulated at each simulation step. The safety stock decision has signi<sup>fi</sup>cant bearing on the number of lots ordered each month.

The end-of-month inventory at time t equals the beginning inventory plus the number of units received minus the demand at t. That is,

$$
I _ {t} = I _ {t - 1} + n _ {t - 1} * \mathrm{LS} - d _ {t}\tag{7}
$$

Fig. 7 demonstrates such a relationship and shows that computation of the end-of-month inventory for period t depends on the number of lots ordered in period (t−1) and the lot size (LS) of the SKU.

## 5. DSS usage details

Before our DSS came along, GSK sets the forecasted demand for the planning horizon and <sup>fi</sup>ve additional weeks of demand as target inventory level. Over the lead time, the demand $\mu$ is expected to be 12 WFC and the standard deviation σ is 2.74 WFC. For GSK to maintain X=17 WFC is equivalent to a 96.6% service level (SL). That is, z=(17−12) /

![](/api/attachments/KXWS8S5J/fulltext/images/c478c82b46bac59829ad7c4bedcc2b24efe382571ead266e791a44d438d8651c.jpg)  
Fig. 7. End-of-month inventory.

GSK Forecast Model - Data Definition Sheet  
![](/api/attachments/KXWS8S5J/fulltext/images/6287eef2f689600bc6d6cce97eba9ea7309881d603995ccafa2625310cca4cdd.jpg)  
Fig. 8. Data de<sup>fi</sup>nition sheet for the forecasting function.

2.74=1.82; SL=96.6%. The desired SL by GSK is reached. However, excessive inventories are maintained in such a process.

In the proposed DSS, the historical demand and forecast, and the current forecast data along with the lot size information are extracted from GSK's Manugistics systems and copied into the Excel spreadsheets. Although useful, Manugistics, a software application for resource planning and supply chain management, is not <sup>fl</sup>exible enough to incorporate all of the situations encountered. The focal point here is on the safety stock decision in the context of inventory replenishment.

Fig. 8 shows the basic data entry. The inventory planner would enter the brand code, SKU #, the lead time, and the desired service level as the essential inputs. Optional features, such as turning the outliers off and specifying the historical time period, are also available. Fig. 9 includes simulation input functions, such as the number of simulation runs, discrete steps of safety stock levels, number of iterations per step, and minimum and maximum safety stock levels allowed. Parameters for sensitivity analysis can also be speci<sup>fi</sup>ed. For example, if the service level required is 96.6%, then an up and down sensitivity of ±2% would give service levels of 94.6% and 98.6%, which in turn generates different SS and WFC.

A statistical summary of historical data is given in the statistical results section. Simply pressing the Excel buttons in the middle of Fig. 9 (Build Model and Simulate) would run the underlying macros and generate the results. The third button, Organized Data, would summarize all the results for the SKU in a separate spreadsheet, which allows convenient comparisons of different SKUs. Data for analysis are extracted from the database after the Build Model macro is run; they are carefully organized into the desired format and any missing or incorrect data are identi<sup>fi</sup>ed. The inventory algorithms described in Fig. 6 are then executed to compute the “optimal” safety stock level. A simulation macro is executed using the derived safety stock as the base model.

After the simulation macro is run, the cells in the simulation section are <sup>fi</sup>lled and the simulation is replicated for each safety stock level to generate the <sup>fi</sup>nal results. Although dependent on processor speeds, a typical laptop takes only a few seconds to run for a scenario of 200 iterations per step and 15 steps in safety stock level.

## 5.1. Ease of use and versatility

It is straightforward to get acquainted with the model. Once the standard database and other basic information are entered into the spreadsheet, only the brand code, SKU #, and a few other data need to vary to determine the SS for the predetermined service level. There is no system integration issue with this model, as it is exclusively based on Microsoft Excel and does not need any add-in tools.

Each of the 1200 SKUs in GSK can be analyzed using the proposed DSS. Even though aggregation is suggested by the literature, the 1200 SKUs are treated independently at GSK for several reasons:

(1) In the hierarchical process, product line or families are managed in the aggregate production planning; whereas individual products are handled in the master production schedule. Since the safety stock decision is related to the master production schedule, not aggregate planning, it is natural to focus on individual items.

(2) Management prefers to have each of the 1200 SKUs attended to individually. They believe if a DSS can support every item, the overall accuracy of the output would be higher.

(3) GSK would like to compare our recommendations with their actual results at the SKU level. From a user's perspective, the “cost” is very low, i.e. the inputs are quite minimal.

(4) Aggregation is not in GSK's practice. This is mainly because improved and new products are frequently introduced to replace existing products.

When a new SKU is launched, a similar SKU's historical demand and forecast during its initial period can be used to approximate the optimal inventory levels. The only exception is when demand patterns do not resemble existing SKUs (e.g., the special packaged goods have little or no data, and no comparable items exist). However, the exceptions are far too few to be considered as a liability.

![](/api/attachments/KXWS8S5J/fulltext/images/ef6550663951a0caa0257512e030e24b830494193c755f76a8efc6ed9566a223.jpg)  
Fig. 9. A screen shot of the model.

## 6. Model outputs

## 6.1. Service level vs. safety stock

The main output of the DSS is a graph that shows the relationship between the service level (SL) and the safety stock (SS). Fig. 10 is a sample output for a Nicorette SKU. The service level is shown as a fraction on the Y-axis, whereas the safety stock above the forecasted demand is given on the X-axis. As expected, the service level of the SKU increases as the safety stock increases at a very high rate before <sup>fl</sup>attening. We <sup>fi</sup>nd that a safety stock above 1500 units increases the service level only marginally. At <sup>fi</sup>rst glance, it seems that 1500 units SS is the optimal safety stock that needs to be maintained. The minimal safety stock required depends, however, on the service level desired for the business and the costs associated with maintaining additional units of safety stock.

![](/api/attachments/KXWS8S5J/fulltext/images/ca9a5d67937653676d071d1f02abc4bc0eec83f35b68499abadfff5fb9690276.jpg)  
Fig. 10. Safety stock vs. service level.

![](/api/attachments/KXWS8S5J/fulltext/images/75b2e284f84950160739dd142712ea42819b11de929fc38cab670b0d1a219a5d.jpg)  
Fig. 11. An example of the recommended WFC vs. the actual end-month WFC.

Fig. 10 shows two curves: the SL-Simulated curve predicts the service level, given the associated safety stock and simulated demand; the other curve, SL-Actual, shows how the actual service level for the historical period would have been had the associated safety stock been maintained. The two curves are very similar; not only in the given example, but also in nearly all SKUs. Thus, GSK would be able to achieve a desired service level by following the safety stock levels recommended in the graph. GSK would also <sup>fi</sup>nd it useful to experiment with different service levels for different products by changing the inputs in Fig. 8, since the cost of maintaining inventory deviates extensively across brands.

## 6.2. Recommended WFC vs. actual WFC

Fig. 11 shows GSK's inventory (in terms of WFC) for a Nicorette SKU for 18 months between March 2003 and Sept 2004. Note that the inventory in WFC varies since the forecasted demand for the SKU <sup>fl</sup>uctuates across time. The top curve (WFC based on Actual M-E-Inv) represents the actual month-end inventory levels that GSK actually maintained for the SKU under consideration. The curve at the bottom is the recommended WFC based on a 96.6% SL management desires. The two straight lines in Fig. 11 represent the average SKU level over the time period considered in the graph. Note that the actual inventory maintained (the top line) for the speci<sup>fi</sup>c Nicorette SKU is much higher (at an average of 24.06 weeks) as opposed to the recommended (5.46 weeks) inventory. The higher WFC has resulted in a 100% service level for the SKU, but it came at the expense of maintaining an unwarranted high inventory for the targeted SL of 96.6%.

Not all SKUs at GSK are maintained at a higher than required WFC. Since, traditionally, inventory planning was done mostly through intuition and experience, many SKUs had higher than required WFC for the targeted service level and few had lower than required WFC, thus prompting high overall inventory levels in achieving the targeted service level. For a particular SKU, Fig. 11 helps inventory planners to see whether the actual WFC maintained deviates from the required WFC and by how much. The planners could then order less when the actual WFC is higher than required, without worrying about adverse effects on the service level.

Fig. 12 illustrates further how the WFC has to change in order to provide 96.6%±2% service levels. Note that Fig. 11 shows the weeks of inventory GSK needs to maintain to serve at 96.6% SL, whereas Fig. 12 provides a visual understanding of how the inventory levels need to change to reach a different service level. To attain the same incremental service level improvement, those products that are already at the high service level require higher incremental inventory. Fig. 12 shows that increasing the service level from 94.6% to 96.6% requires an increase in WFC of 1.11 weeks as compared to 2.17 weeks of increase in WFC to increase from 96.6% to 98.6%. The numbers agree with Fig. 10 where marginal improvements in service level beyond 97% require a higher increase in safety stock.

![](/api/attachments/KXWS8S5J/fulltext/images/4b4d5067415651504ebb042d60148e53038c2719611d0ddde37a85f9a56412f1.jpg)  
Fig. 12. Sensitivity analysis of a speci<sup>fi</sup>c product.

## 7. Summary and discussion

## 7.1. Current status and potential improvements

Currently, GSK is evaluating the advantages and disadvantages of implementing such a stand-alone system within the corporate culture of using an already implemented and established ERP system (Manugistics). Top management at GSK is very much impressed by the potential bene<sup>fi</sup>ts of the system, and note two speci<sup>fi</sup>c advantages. First, GSK regards the DSS as theoretically sound. The system has a strong mathematical foundation, and the results are con<sup>fi</sup>rmed by the simulation method. Second, GSK managers believe the system is user-friendly and <sup>fi</sup>nd it easy to use. Thus, GSK executives understand and appreciate that using the DSS can lead to more ef<sup>fi</sup>cient and effective inventory management.

On the other hand, these same GSK executives point out that the system offers a new approach, and its use and implementation differs from its current operation, which is supported by Manugistics. Consequently, there is some resistance in adopting the system by employees, partly due to concerns of job security. The members of the staff responsible for such functions at this time feel marginalized and worry about their future at GSK.

The different reactions of the managers and staff are consistent with the rich literature on implementing systems in organizations. Empirical studies in DSS as well as the broader Information Systems literature have repeatedly demonstrated that those who actively participate in the design and implementation of a system, who recognize the bene<sup>fi</sup>ts of the system, and who have good relationships with the project team, are more likely to embrace the system and use it [7,10–12,19]. In addition, highly complex systems require more training than systems that are routine or that require no new skills to utilize [24], and user training has been shown to be an important antecedent for successful DSS implementations [7]. It is no surprise then that top managers at GSK — who have been involved with the design of this DSS, understand how to use the system, and realize its potential bene<sup>fi</sup>ts — have a favorable disposition toward the DSS.

In contrast, the implementation literature notes that employees who are marginalized, feel threatened by the DSS, stand to lose power in an organization, or <sup>fi</sup>nd the new system overly complex and dif<sup>fi</sup>cult to learn, often resist the implementation of a new information system and may even sabotage the deployment process [13,20,27]. This suggests that it is important to address the concerns of GSK staff to ensure a successful implementation, and indeed, GSK is taking such steps. For example, a formal implementation plan is being developed. Further training is under way to ensure full acceptance of the DSS by those impacted by its deployment. In addition, executives have increasingly voiced their assurance that the DSS will not replace individuals at GSK.

As to future improvements for the DSS itself, we suggest updating the historical data and re-running the model every month. It is possible to enhance the bene<sup>fi</sup>ts of the model by increasing the frequency of model updates and data analysis, but this enhancement will increase the efforts in data input and re-running the model.

## 7.2. Summary

Traditionally, the inventory and safety stock decisionmaking at GSK heavily depended on intuition, experience, and subjective judgment. The process was overly simpli<sup>fi</sup>ed and although it functioned acceptably, management was aware that it could be greatly improved. The proposed Excelbased DSS inventory model is sensible and easy to use. For a speci<sup>fi</sup>ed service level, the Excel-based DSS determines the “optimal” inventory level and the corresponding safety stock for each SKU. Aside from the basic functions, advanced features such as the ability to select the historical period, the option of removing outlier data, sensitivity parameters, the number of simulation runs, step intervals for the safety stock, etc. are available to tailor the system to the user's needs.

The ultimate goal of any supply chain is to deliver goods and services to customers at the desired quantities and time, and at the minimum cost. Forecasting demand in a multiechelon supply chain is a complex task and most often is not perfect. In the GSK case, there is also an uncertainty in the manufacturing lead time, transportation time between the manufacturers and the distribution center, and between the distribution center and the customer. There is also a constraint on the ordering size, as a particular product will always have a minimum order quantity requirement and an incremental batch size above the minimum order quantity. To maintain an appropriate inventory level so as to attain desirable customer service and customer satisfaction, the system must take into account the forecasting errors, demand uncertainties, and the minimum batch size requirement.

The model outputs provide not only point estimates of the requisite inventory for a speci<sup>fi</sup>ed service level, but also the “optimal” inventory levels GSK would need to maintain a range of service levels. A higher WFC recommended by the model indicates that the inventory level for the particular SKU need to be increased to achieve the targeted service level of 96.6%; whereas a lower WFC, which is normally the case, indicates that the current inventory levels could be reduced while still achieving the targeted service level. Note that the spreadsheet model we developed does not use any add-in simulation software like @RISK [17] or CRYSTAL BALL [3]. The simulation logic is ingrained in the spreadsheet itself by a series of complex macros, which makes the tool usage more routine while tailoring the simulation outputs to our requirements in the spreadsheet.

Many companies in today's Internet age are still making inventory decisions on the basis of past experience and a subjective opinion of the future. One of the contributions of this paper is the proposed spreadsheet-based DSS that predicts the appropriate requisite inventory quantity for a pre-determined service level. This paper also contributes to the literature by showing how DSS can bridge the gap between enterprise systems such as Manugistics and decision-makers. Implementing the proposed DSS would provide GSK a distinct competitive advantage. However, to fully realize the bene<sup>fi</sup>ts of the DSS, GSK must also take steps to successfully implement the system and to ensure that employees use it.

## Acknowledgements

We are grateful for GSK's assistance in completing this project, particularly to Mr. Rich Mirilovich, Manager, Planning

Systems & Forecasting Relationships; and Ms. Noreen Coleman, Business Unit Planning Manager & Site Coordinator, for the constant support and guidance throughout the project. We would also like to thank the Katz students who participated in this project.

## References

[1] D. Arnott, G. Pervan, A critical analysis of decision support systems research, Journal of Information Technology 20 (2) (2005).

[2] H.K. Bhargava, D.J. Power, D. Sun, Progress in web-based decision support technologies, Decision Support Systems 43 (4) (2007).

[3] Decisioneering, Inc. 2008, http://www.decisioneering.com.

[4] G. DeSanctis, B.R. Gallupe, A foundation for the study of group decision support systems, Management Science 33 (5) (1987).

[5] T.F. Gattiker, D.L. Goodhue, What happens after ERP implementation: understanding the impact of interdependence and differentiation on plant-level outcomes, MIS Quarterly 29 (3) (2005).

[6] G.A. Gorry, M.S. Morton, A framework for management information systems, Sloan Management Review 13 (1) (1971).

[7] E. Hartono, R. Santhanam, C. Holsapple, Factors that contribute to management support system success: an analysis of <sup>fi</sup>eld studies, Decision Support Systems 43 (1) (2007).

[8] C.W. Holsapple, A.B. Whinston, Decision Support Systems: A Knowledge-based Approach, West Publishing, St. Paul, MN, 2000.

[9] JDA Software, Inc. 2008. http://www.jda.com.

[10] S. Kanungo, S. Sharma, P.K. Jain, Evaluation of a decision support system for credit management decisions, Decision Support Systems 30 (4) (2001).

[11] L.J. Kirsch, C.M. Beath, The enactments and consequences of token, shared, and compliant participation in information systems development, Accounting, Management and Information Technologies 6 (4) (1996).

[12] D. Ko, L.J. Kirsch, W.R. King, Antecedents of knowledge transfer from consultants to clients in enterprise system implementations, MIS Quarterly 29 (1) (2005).

[13] M.L. Markus, Power, politics, and MIS implementation, Communications of the ACM 26 (6) (1983).

[14] B.C. McNurlin, R.H. Sprague, Information Systems Management in Practice, Prentice–Hall, Upper Saddle River, NJ, 2002.

[15] T.P. Morgan, AMR research says ERP software sales to hit \$29 billion this year, The Linux Beacon 3 (39) (2006) http://www.itjungle.com/tlb tlb101706-story10.html

[17] Palisade Corporation, http://www.palisade.com2008.

[16] M. Muller, Essentials of Inventory Management, American Management Association, New York, 2003.

[18] G. Pervan, L. Wilcocks, Introduction to the special issue on decision support systems, Journal of Information Technology 20 (1) (2005).

[19] P. Poon, C. Wagner, Critical success factors revisited: success and failure cases of information systems for senior executives, Decision Support Systems 30 (4) (2001).

[20] D. Robey, J. Ross, M. Boudreau, Learning to implement enterprise systems: an exploratory study of the dialectics of change, Journal of Management Information Systems 19 (1) (2002).

[21] J. Ross, Dow Corning corporation C: transforming the organization, Center for Information Systems Research Working Paper No. 305, Massachusetts Institute of Technology, 1999.

[22] F. Rowe, Are decision support systems getting people to conform? The impact of work organisation and segmentation on user behaviour in a French bank, Journal of Information Technology 20 (2) (2005).

[23] R. Santhanam, T. Guimaraes, Assessing the quality of institutional DSS, European Journal of Information Systems 4 (3) (1995).

[24] R. Sharma, P. Yetton, The contingent effects of training, technical complexity, and task interdependence on successful information systems implementation, MIS Quarterly 31 (2) (2007).

[25] E. Silver, D.F. Pyke, R. Peterson, Inventory Management and Production Planning and Scheduling, Wiley, 1998.

[26] M. Silver, User perceptions of decision support system restrictiveness: an experiment, Journal of Management Information Systems 5 (1) (1988).

[27] C. Soh, S.S. Kien, J. Tay-Yap, Cultural <sup>fi</sup>ts and mis<sup>fi</sup>ts: is ERP a universal solution? Communications of the ACM 43 (4) (2000).

[28] T.S.H. Teo, Meeting the challenges of knowledge management at the housing and development board, Decision Support Systems 41 (1) (2005).

[29] P. Todd, I. Benbasat, An experimental investigation of the impact of computer based decision aids on decision making strategies, Information Systems Research 2 (2) (1991).

[30] E. Turban, J.E. Aronson, T.P. Liang, R. Sharda, Decision Support and Business Intelligence Systems, Prentice Hall, 2007.

[31] P.H. Zipkin, Foundations of Inventory Management, McGraw-Hill/Irwin, 2000.

Jennifer Shang received her Ph.D. in Operations Management from the University of Texas at Austin. She teaches operations management, simulation, statistics, and Process and Quality Improvement courses. Her main research interests include multi-criteria decision making and its application to the design, planning, scheduling, control, and evaluation of production and service operational systems. She has published in various journals, including Management Science, European Journal of Operational Research, IEEE Transactions on Engineering Management, and International Journal of Production Research. She has won the 2005 EMBA Distinguished Teaching Award and several Excellence-in-Teaching Awards from the MBA/EMBA programs at Katz Business School

Dr. Tadikamalla is a professor of business administration in the Katz Graduate School of Business at the University of Pittsburgh. Dr. Tadikamalla has a B.S. degree in Mechanical Engineering from India. He received his M.S. and Ph.D. in Industrial and Management Engineering from the University of Iowa. Dr. Tadikamalla is an Associate Editor of OMEGA: The International Journal of Management Science. His research interests lie in simulation methodology and statistical techniques. Dr. Tadikamalla has published over 50 research articles in several professional journals. He teaches courses in Decision Models, Statistical Techniques for Management, Simulation, and Six Sigma. He emphasizes real-life problem solving in the classroom. Through MBA project courses and consulting, he has solved large-scale, real-life problems for several corporations. Dr. Tadikamalla received several awards in recognition of his dedication to and excellence in teaching. Dr. Tadikamalla spends his spare time in volunteer work. He served as the President Chairman, and Treasurer of SV Temple in Pittsburgh, a major Hindu temple in the western hemisphere.

Laurie J. Kirsch (Ph.D., University of Minnesota), is Professor of Business Administration at the University of Pittsburgh. Her research explores the exercise of control and the transfer of knowledge in the IS context, examining how stakeholders can better manage IS initiatives. Dr. Kirsch has published her research in leading scholarly journals such as MIS Quarterly, Management Science, Organization Science, Information Systems Research, and Accounting Management and Information Technologies. She is active in the Association for Information Systems, the International Conference on Information Systems, and the Academy of Management, where she recently completed a <sup>fi</sup>ve year rotation through the leadership positions of the Organizational Communication and Information Systems (OCIS) division. In 2004, she served as the ICIS Program Co-Chair Dr Kirsch serves, or has served on the editorial boards of MIS Quarterly, Management Science, Information and Organization, Decision Sciences, MISQ Executive, and The Journal of Strategic Information Systems. She is currently a senior editor for Information Systems Research.

Lawrence H. Brown is currently Vice President of the North America Supply with GlaxoSmithKline Consumer Healthcare, a \$2.1 billion dollar consumer healthcare company. He is the Global Manufacturing and Supply representative to the North American Leadership Team for Consumer Healthcare and member of the Global Contract Manufacturing Leadership Team. Prior to joining GlaxoSmithKline. Mr. Brown had held senior level management positions at ConAgra Frozen Foods, a \$1.8 billion division of Con Agra Corp; at Neo Consulting Inc a sales consulting firm focusing on development of leading edge sales organizational strategies and dynamic sales/business solutions; at Canada Dry & Sunkist Brands with Cadbury Beverages, North America, a \$1.0 billion dollar soft drink franchiser and at All American Bottling Corporation, a top twenty, national soft drink bottler and seller of Seven-Up. Dr. Pepper, RC. Canada Dry and other nationally known soft drink brands. He holds a BSBA degree from the University of Tulsa. Mr. Brown is currently a member of the CPHA Logistics Steering Committee NACDS Logistics Board and Wal-Mart Supply Chain Board.
