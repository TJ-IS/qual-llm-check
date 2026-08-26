---
otero_id: 6724
otero_key: "8KZJGQT9"
title: "Real-Time business data acquisition: How frequent is frequent enough?"
authors: "Malcolm Townsend; Thanh Le Quoc; Gaurav Kapoor; Hao Hu; Wei Zhou; Selwyn Piramuthu"
year: "2018"
journal: "Information & Management"
doi: "10.1016/j.im.2017.10.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Real-Time Business Data Acquisition: How Frequent is Frequent Enough?

Authors: Malcolm Townsend, Thanh Le, Gaurav Kapoor, Hao Hu, Wei Zhou, Selwyn Piramuthu

![](/api/attachments/8KZJGQT9/fulltext/images/cde9bf28d267bd41e79ee640a0db0cc4cadf89a742b7ebea75cf7170ba2f6937.jpg)

PII: S0378-7206(17)30026-5

DOI: https://doi.org/10.1016/j.im.2017.10.002

Reference: INFMAN 3025

To appear in: INFMAN

Received date: 13-1-2017

Revised date: 4-10-2017

Accepted date: 10-10-2017

Please cite this article as: Malcolm Townsend, Thanh Le, Gaurav Kapoor, Hao Hu, Wei Zhou, Selwyn Piramuthu, Real-Time Business Data Acquisition: How Frequent is Frequent Enough?, Information and Management https://doi.org/10.1016/j.im.2017.10.002

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Real-Time Business Data Acquisition: How Frequent is Frequent Enough?

Malcolm Townsend<sup>1</sup>, Thanh Le<sup>2</sup>, Gaurav Kapoor<sup>3</sup>, Hao Hu<sup>4</sup>, Wei Zhou<sup>1</sup>, Selwyn Piramuthu<sup>5,∗</sup>

<sup>1</sup>Information & Operations Management, ESCP Europe, Paris, France <sup>2</sup>Economics, University Paris - Saclay, France <sup>3</sup>CSTEP, Bangalore, India <sup>4</sup>NAOCE, Shanghai Jiaotong University, China <sup>5</sup>Information Systems and Operations Management, University of Florida, Gainesville, FL,USA corresponding author: selwyn@ufl.edu

## Abstract

Effective data acquisition for business process monitoring has become a critical element in today’s business world. While the need for monitoring is generally agreed upon by both researchers and practitioners alike, the means and mechanisms are often vague. This is especially salient with the fast growing availability of various technologies to monitor in realtime through recent advances such as the Internet of Things (IoT), with specific emphasis on Radio-Frequency IDentification (RFID) and associated sensor networks. This study is motivated by the lack of published literature in data acquisition and analytics that specifically addresses sufficient real-time data acquisition for effective managerial monitoring. As a step in addressing this void, we review and extend existing literature in this general area by studying various requirements and information sources that relate to effective management monitoring. We then design an exploratory study to evaluate current managerial monitoring needs and the importance of automated data collection technologies. Results from this study show that the most important latent factor that influences an organization’s information need is its dynamic competitiveness, and consequently, companies with a dynamic supply chain would need a faster transaction and operations data system. The second important latent factor is the behavioral performance, which renders it essential to have a human-centric data system. This study provides evidence for the significance in adopting technologies such as RFID and other IoT systems for real-time monitoring in highly dynamic organizations and offers guidelines for analytical technology adoption for various industries.

Keywords: RFID, process monitoring, monitoring frequency, real-time data acquisition

#

Real-Time <sub>Business</sub> D<sub>a</sub>t<sub>a</sub> Acquisition: <sub>How</sub> Frequent <sub>is</sub> Frequent <sub>Enough?</sub>

## Abstract

Effective data acquisition for business process monitoring has become a critical element in today’s business world. While the need for monitoring is generally agreed upon by both researchers and practitioners alike, the means and mechanisms are often vague. This is especially salient with the fast growing availability of various technologies to monitor in real-time through recent advances such as the Internet of Things (IoT) with specific emphasis on Radio-Frequency IDentification (RFID) and associated sensor networks. This study is motivated by the lack of published literature in data acquisition and analytics that specifically addresses sufficient realtime data acquisition for effective managerial monitoring. As a step in addressing this void, we review and extend existing literature in this general area by studying various requirements and information sources that relate to effective management monitoring. We then design an exploratory study to evaluate current managerial monitoring needs and the importance of automated data collection technologies. Results from this study show that the most important latent factor that influences an organization’s information need is its dynamic competitiveness, and consequently, companies with a dynamic supply chain would need a faster transaction and operations data system. The second important latent factor is the behavioral performance, which renders it essential to have a human-centric data system. This study provides evidence for the significance in adopting technologies such as RFID and other IoT systems for real-time monitoring in highly dynamic organizations and offers guidelines for analytical technology adoption for various industries.

## 1 Introduction

Organizations require information to make the right decisions and to control their operations. Managerial monitoring is the act of gathering information throughout the value chain. In operations control, to ensure compliance with expected performance measures, the actual operations performance is compared with that of planned expected performance. Any deviation between the two requires intervention to rectify the situation. In general, without sufficient monitoring data, managers often are not aware of the exact operational details, precipitating in misaligned opportunity costs and unnecessary delay in recognizing existing issues. However, frequent monitoring can be clearly inefficient and expensive because it involves unnecessary usage of human and computational resources. Although managerial monitoring or performance observation have long been recognized as a critical function for managers, the past two decades have seen an explosion in the use of technologies as a means through which organizations can effectively exercise managerial monitoring (Alge et al. 2014). The emerging extensive use of Information and Communication Technologies (ICT) and sensor networks has contributed to today’s fast growing field of “Big Data.”

Regardless of how often a manager or any other employee decides to monitor processes in an organization, there is a need for an effective mechanism that helps with the implementation and operationalization of this process. Recent advances in sensor network and Internet of Things (IoT)/Radio-Frequency Identification (RFID) technologies (e.g., Bose and Yan 2011, Bose et al. 2011) and their widespread adoption have certainly helped to facilitate this process. For example, sensor network and IoT/RFID technologies enable organizations to automatically monitor business operations throughout the supply chain in real-time. Once implemented, the marginal cost to operate automatic managerial monitoring is generally minimal. The adoption of such an automatic system is constrained primarily by the initial design and associated setup cost. This investment cost can be significant. Nevertheless, automatic tracking systems such as those enabled by IoT/RFID greatly improve the effectiveness and efficiency of managerial monitoring of processes in organizations and their supply chains (Zhou et al. 2016).

How frequent is frequent enough? The answer for this question certainly depends on the actual data needs that come from the business strategy and daily operations. There is a sheer lack of published literature on managerial monitoring and business analytics facilitated by technology automation such as that through IoT/RFID and associated sensor networks. To address this void, as a first step, we are interested in determining the need for such technologies across different industries. We are also interested in investigating companies’ priority with respect to managerial monitoring to understand the conditions under which IoT/RFID and associated sensor network systems, and data analytics should be adopted and deployed. To accomplish this, we explore various factors that influence monitoring practice with an implicit consideration of the use of automatic identification and tracking technologies. The hope is that eventually the results from this study, along with related results, could be aggregated to generate guidelines for performance monitoring that are applicable to managers at different levels in an organization, for example, to determine the ideal extent and frequency of monitoring necessary.

The remainder of this paper is organized as follows: In Section 2, we consider managerial monitoring with appropriate help from recent developments in IoT/RFID and related sensor network technologies. We then review relevant literature on the different perspectives of managerial monitoring, including monitoring in business operations, information sources, and managerial monitoring mechanisms. We discuss our exploratory field study on the factors affecting managerial monitoring in Section 3. From consultations with managers across industries, we attempt to prioritize monitoring factors and discover the latent factors. We conclude with discussion on our findings in Section 4.

## 2 Data Requirements for Effective Managerial Monitoring

There are different ways in which information is collected and exchanged in organizations. For example, within a company, it can be in the form of internal reports, intranet, meetings, e-mail, telephone, company procedures, or technical reports. Daft (1983) introduces the concept of information richness to classify the different types of media. He rates different media depending on their richness and concludes that face-to-face conversation is more insightful than formal means and is the preferred media for managers to address complex problems. Managers have

#

a preference for current information. According to Daft, the scale of richest to poorest is faceto-face (Highest); telephone (High); personal letters and memos (Moderate); written, formal bulletins, and documents (Low); a n d numeric formal computer output (Lowest). This ranking was done before the popularity of e-mail, which generally results in invoking immediate response, the Web, and a plethora of technical information systems that have recently come into use.

Information technology includes the integration of hardware, software, and people. Information systems and related technology have become managers’ effective monitoring tool as they help with business visibility, analysis, and eventually problem solving. Moreover, information systems facilitate the collection of data and help to eliminate manual intervention. Ultimately, information systems help managers make appropriate decisions by providing them with better visibility and thereby reducing the extent of uncertainty. There are a number of commonly used information systems for managerial monitoring. For example, RFID is a technology that enables the provision of real-time information that can then be used to track and trace items in supply chains and within organizations. T h e RFID allows for remote access of information on the whereabouts of products fitted with RFID tags. With RFID, it is relatively easy to monitor various parameters of the tagged item in real-time. For example, when item-level RFID tags are used, real-time inventory status of these items can be readily obtained. This information can then be transferred to enterprise resource planning (ERP) systems that are then able to generate status reports for managers and executives.

The issue thereafter is to determine how often such scans should be performed. In the case of a large warehouse, for example, each such scan generates a non-negligible amount of data, which servers are then required to process. Not only are data processing servers expensive but also the resource required is directly proportional to the amount of information that needs to be processed. In addition, associated personnel are required to follow-up on the analysis. Therefore, to control costs, it would be practical to determine the optimal scanning or monitoring frequency.

ERP is an information system that aggregates information from different functions within an organization (e.g., Bose et al. 2008). For example, it can be used to handle real-time information on transactions such as customer orders and allows managers to view the status of resources that are distributed over the entire organization. Warehouse management system (WMS) is commonly part of ERP that tracks the flow of goods in warehouses. As another important component of ERP, materials requirement planning (MRP) is a planning and control software application developed about three decades ago. It is the key element in “push” supply chains where production volume is forecast. Demand forecasts, customer orders, and planning are entered into the master production schedule (MPS) module, which creates a schedule and a detailed description of what needs to be produced. The MRP module receives this information and interrogates the bill of materials (BOM), which lists dependent items that also need to be ordered to produce the final product. MRP checks the inventory database to verify availability of these components. If unavailable, orders are sent to suppliers for replenishment. The MRP triggers work orders on the shop-floor and sets the production schedule. This automation of the procedures decreases the need for manual checking and avoids

related sources of error.

However, with modern automatic tracking and tracing information system, monitoring of both physical goods and human labor is much easier and more accurate nowadays than 10 years ago. The scale and scope of such a system in organizations remain a strategic decision because of the associated large investment. In order to understand this problem, we first investigate the different information requirements at different levels or hierarchies in organizations.

## 2.1 Managerial Monitoring Hierarchical Requirements

Monitoring is the basis of effective management. It is of prime importance that the information received by managers paints a realistic description of the field, thus enabling the best decisions to be reached. However, the information received by these decision makers may be biased, and consequently, the ensuing decision may be less than ideal.

In the traditional way of looking at the enterprise, managers at different levels in the organization are required to make separate decisions based on distinct types of information (Figure 1). The performance metrics are a mixture of strategic, tactical, and operational, which managers at various levels can monitor and influence to improve overall organizational performance. The same information may be required at several different levels and may need to be adapted or modified in some way for it to be more appropriate for that level. For example, information from a lower level may be filtered so as to be readily understood at a higher level.

<table><tr><td></td><td>Top Management</td><td>Middle Management</td><td>Supervisory and Lower-Level Management</td></tr><tr><td>Time Horizon</td><td>Long: years</td><td>Medium: weeks, months, years</td><td>Short: day-to-day</td></tr><tr><td>Level of Detail</td><td>Highly aggregatedLess accurateMore predicted</td><td>SummarizedIntegratedOften financial</td><td>Very detailedVery accurateOften non-financial</td></tr><tr><td>Orientation</td><td>Primarily external</td><td>Primarily internal with limited external</td><td>Internal</td></tr><tr><td>Decision</td><td>Extremely judgmentalUses creativity and analytic skills</td><td>Relatively judgmental</td><td>Heavy reliance on rules</td></tr></table>

Figure 1: Information characteristics across management levels

## 2.1.1 Top Managers (strategic level)

Top managers deal with the strategic level. Figure 1 sums up some of the characteristics of the types of information and decisions a top-level manager must handle. The top manager’s job is about planning, setting broad objectives, and methods on how to achieve these goals. The outlook

#

is more outward as emphasis is placed on external monitoring such as to determine market trends and interpreting the environment. Top managers use intelligence gathering, which is also known as scanning (Hague and Aiken 1969). According to Daft (1983), the top manager’s objective is to reduce the complexity and uncertainties of the outside world into a broad roadmap, which people within the organization are able to assimilate and work toward. Strategic planning decisions have substantial impact because once taken, it is more difficult to change course. Moreover, the level of information detail tends to favor lower accuracy because of its highly aggregated nature. Top managers monitor metrics of a more financial nature. In addition, theoretically as top managers monitor the external environment more, they may retain an inconsistent view of what actually happens within their own operations. For example, if the environment is smooth, top managers may believe everything is running smoothly, when in reality it is internally chaotic.

## 2.1.2 Middle Managers (tactical level)

Middle management works on a tactical level. They act as management control as they verify that broad objectives set by the top managers are implemented both efficiently and effectively. They work with more methodology than top managers and have more structure. Their outlook is both external and internal. They are often in charge of external sourcing and supplier performance, which are considered to be tactical level responsibilities. Middle managers are required to make more decisions, more often than top managers; however, they monitor less frequently than operational managers.

## 2.1.3 Operational Managers (operational level)

Operational managers ensure that tactical objectives are attained. Non-financial measures are more pertinent at this level. They ensure that tasks are executed efficiently and effectively and they frequently have to make decisions; they may, for instance, have to decide on what products to run for a given day. Schlesinger et al. (1989) assumed that output production from a factory could be modeled by a continuous signal. Traditional manufacturing plants, where change does not occur often, could be modeled by a slow varying signal, while new computer integrated manufacturing (CIM) factories that are more dynamic could be modeled by a higher varying signal. Thus, CIM factories need to be sampled more often to monitor the frequent changes (Schlesinger et al. 1989). Nyquist-Shannon theorem provides guidelines in the telecommunications world on how often a signal needs to be monitored (Shannon 1949). It notes that a continuous signal can be represented by a set of discrete sampled points. The Nyquist sampling rate used to select the sampled points must be at least twice the frequency of the original signal. The original continuous signal can then be reconstituted from the sampled discrete points. That is, the discrete samples are an accurate representation of the original signal if they are taken at least at twice the highest frequency of the original signal.

An illustration can be made where real voice and image is transformed to a digitized format that can either be stored or transmitted. For example, in telephony, when a call is made, the human voice at the caller side is sampled and processed before being sent through a bandwidthlimited communications system. The receiver hears a reconstituted understandable near-replica of the caller’s voice. The key point to consider is on how often the original continuous signal voice is sampled into discrete points, converted from real-world analog signal to digital signal. With a low sampling rate, the voice is garbled and incomprehensible. A higher sampling rate results in a higher quality that is closer to reality. However, this would require storing or transmitting more data, which in turn requires more bandwidth and thus more investment in equipment. The same principle applies for digitally stored music. The stored digitized sampled file is close to an “accurate” representation of the original played piece. A higher quality reproduction will take up more space. The key is to find the optimized sampling rate that allows for coherent reconstitution.

Analogous to the optimum Nyquist sampling rate, we investigate how often and how much a manager should monitor the enterprise to obtain an “accurate” representation of its dynamics. In addition, we consider the human resources dimension and ask the question, “what type of manager should be hired and what type of monitoring behavior should be practiced in the managerial role?”

From the above three descriptions of the different managerial levels, we have seen that the organization is monitored more frequently by the operational manager than the middle manager who in turn monitors more frequently than the top manager. If we are to take Nyquist sampling theorem in conjunction with the traditional hierarchal view of the company, we could argue that the sampling rate should be at least twice the rate of the sampled signal and that the company’s signal frequency diminishes as we go up the hierarchal ladder. From this perspective, the firm is more dynamic at the operator than at the top manager end.

## 2.2 Sources of Information

We have seen from the discussion above that monitoring plays a fundamental role in a manager’s job description. This is in harmony with the fact that to succeed in business, information is crucial. For example, information can provide answers to questions such as what does the customer actually want? What are my competitors doing? Are my operations up to par? And if not, how can I improve them? In this section, we discuss where information comes from, how much information is required, and what type of information is necessary for managers to be able to answer some of these questions.

Daft (1983) referred to organizations as information processing machines, while Mintzberg (1973) portrayed the manager within these organizations as a network nerve center. As previously stated, managers have numerous contacts that are internal and external to the organization. According to Mintzberg, managers spend up to 80% of their time communicating and hence obtaining and exchanging information. The channels of communication (Mintzberg 1973) are both formal and informal. Managers gain insights informally from rumors and coffee-break discussions and also from more formal avenues such as periodic reports and organizational meetings. According to Galbraith (1973), the amount of information that managers a r e required to amass and process is proportional to the uncertainty that they experience. Uncertainty is related to a

#

manager’s lack of visibility. In order to make the correct decision, a manager must understand the current state of the organization. Therefore, when the manager’s level of ignorance or uncertainty is high, more information is necessary to reduce the level of uncertainty in order to make the correct decision for handling the situation. The level of uncertainty in a company is proportional to several factors (Galbraith 1973), including task variability and diversity. When an organization has high task variability, more things can go wrong, unexpected events can occur; and therefore, more information is needed to overcome these difficulties. When a company has high diversity such as the existence of numerous goals and high product variety, more monitoring and information processing is required to ensure that goals are attained.

For the information system to be of any use, the information accumulated by organizations must display several characteristics (Chopra et al. 2010). Information must be pertinent: organizations need to decide on and pin-point what information should be gathered and analyzed. It is futile to collect data that will never be used as it consumes valuable resources and important facts may be missed altogether (Chopra et al. 2010). The information must be accurate because decision-making based on faulty data is unreliable. Timely information is also crucial. Yesterday’s news may be accurate, but an opportunity may be missed. Additionally, information must be accessible. If a manager is unable to read or understand the information, it is useless. Finally, information should be shared. For an organization to work, all stakeholders must be on-board, share a common view, and make decisions together. If each person has his own source of information, people may be talking at cross-purposes (Chopra et al. 2010).

More specifically, what are these sources of data from which organizations must choose? Below, we discuss internal and external data resources.

## 2.3 Internal Information

Logistics handles the in-bound raw materials and components for production and the out-bound distribution of end products. Different functions embody logistics: transportation, storage, and distribution. Each of these functions produces and requires information in response to customer requirements. For instance, decisions are made for scheduling, routing, and choosing the relevant mode of transport. Additionally, data may be collected to track vehicles or measure inventory storage level and location.

In operations, each machine that assembles, packages, and manufactures generates information, which is collected to verify that everything is running smoothly and on target. Information is required to plan production runs, to organize maintenance schedules, and to calculate the number of machines and personnel necessary for production.

Marketing and sales information is needed to ascertain how to promote items, what pricing should be employed to make a profit, and in general how to convince buyers to purchase the articles and to facilitate their eventual reception. Service relates to added value activities such as after sales support, training, and maintenance programs. Information on customer satisfaction levels might be gathered and services tailored in response to customer needs.

Porter’s non-core activities involve infrastructure of the firm, human resources, research and development (R&D), and procurement (Porter 1985). Infrastructure includes quality and finance. Companies generate cost accounting data, which inform management on sales and actual incurred costs. For example, activity-based costing (ABC) techniques allocate overhead costs to different specific activities. From this information, management would then be in a position to decide on what operations need to be streamlined or dropped. Financial accounting information is also generated to satisfy external interest in the position of the company. Company balance sheets, income statements, and cash flow are published to communicate the financial position of the company so that shareholders can decide whether to invest or not and for government officials to know what income tax to apply. Other non-core activities include procurement, items that should be purchased, activities that produce contracts and tenders, and other information. Human resources produce information such as job opportunities, training initiatives, and employee satisfaction surveys.

The above briefly touches on some aspects within a company that generate information that needs to be monitored.

## 2.4 External Information

External sources of information originate from outside the firm. They may be macro-environmental phenomena, activities that the firm has outsourced or information from partners, and customers with whom the firm does business.

The most important source of external information is the customer. Firms need to respond to the requirements of customers. For instance, the firm’s pricing policy, range of offered services, lead times, and product availability are determined by analyzing customer requirements. This is crucial with custom-made products, where accurate specifications and requirements need to be relayed from the customer to operations. The same applies for the buyer’s buyer. To illustrate this, if a supplier receives orders from a buyer and if the buyer’s buyer is no longer purchasing, there is a chance that orders will dry up. Consequently, alternative sales channels would need to be investigated in order for the business to survive.

Suppliers also produce information such as the quality of goods that they offer or the amount of time required between order placement and goods delivery (lead time). In addition, different transactions between buyers and suppliers, such as the transfer of order and payment details, and generate data. Frequently, supplier’s supplier knowledge can be beneficial. For example, in the case of the recent catastrophe in Japan, car retailers required information not only from car manufacturers themselves but also from parts suppliers as a massive shortage of parts resulted in the inability to maintain car production and to meet demand. Information sources also include the macro-environment. The PESTLE (Collins 2010) model synthesizes the different macro-environmental factors, which affect businesses. They include political, economic, social, technological, legal, and environmental factors. For instance, gathering information about possible tax incentives, country stability, market trends, technological advances, employment law, and environmental policy is required to make the right decisions.

Outside information needs to be analyzed and understood. Weick (1979) suggested that firms

#

reduce the uncertainty associated with different interpretations of outside information. Managers should discuss the various available information and converge to a common understanding. Organizations have difficulty dealing with ambiguity and need a basis from which to work and get things done. In this vertical processing structure, top-level managers reduce the ambiguity of the information to an acceptable level for the use of others in the company (Daft 1983).

## 2.5 Data Acquisition Strategies in Supply Chain Management: Example of RFID

There are two monitoring mechanisms: event driven and periodical review. In event- driven systems, a notification is brought to the attention of an operator once a certain pre-defined boundary level has been exceeded. It is a type of alert or alarm. In a communications context, it is similar to the network systems monitoring protocol SNMP, where traps or alerts are raised to a master supervisor in the event of a problem in the network.

In periodical review monitoring, the system is polled after a pre-determined amount of time and information is collected and then analyzed. Performing periodical reviews on everything is generally too expensive without an automatic monitoring mechanism.

## 3 Exploratory Study

We compare the hypothetical issues that influence managerial monitoring determined from the above literature review with factors extracted, using factor analysis, from a list of variables obtained from field research data conducted through an exploratory questionnaire that professionals working in different industries were asked to complete.

From our literature review, we have come up with a number of factors that affect managerial monitoring. With RFID-based automated monitoring as the basis, we aim to test the following questions in our study:

1) Do professionals believe the issues determined from the above literature review actually affect managerial monitoring in the workplace?

2) Are there any other as yet unobserved or undetermined issues that could affect managerial monitoring?

3) Can issues affecting managerial monitoring be explained by a simple underlying set of factors?

## 3.1 Factor Selection & Questionnaire Design

A questionnaire was created to find answers to “What are the issues that affect monitoring effectiveness and efficiency?” We developed 23 different questions based on a comprehensive literature review of managerial monitoring, which encompassed the various issues we wish to study. The questions comprise statements followed by a 5-point Likert scale that ranged from “Strongly Disagree” to “Strongly Agree” [Strongly Disagree (SD), Disagree (D), Neither Disagree nor Agree (N), Agree (A), and Strongly Agree (SA)]. According to Hair et al. (2007), a 5-point Likert scale is ideal. Respondents to a wider scale are less likely to select all the choices within the scale. The 5-point Likert scale results are translated numerically [1: Strongly Disagree (SD); 2: Disagree (D); 3: Neither Disagree nor Agree (N); 4: Agree (A), and 5: Strongly Agree (SA)].

The online survey was sent to several hundred professionals with different backgrounds including alumni and current MBA students with managerial experience of a European business school. A pre-selection questionnaire was also included at the beginning to determine the demographics of the respondents.

The questions were posed to verify the hypothetical issues that were developed from our literature review. The following table contains the final questions with associated issue.

Q1 I spend a significant portion of my workday seeking information.

Q2 I am more likely to gather and analyze internal company information rather than external company information.

Q3 Information gathered by my company is chiefly sufficient, adequate, timely, relevant, and useful for company operations.

Q4 My company’s operations are fast moving and are in constant evolution.

Q5 My company’s logistics (transportation, storage, and distribution) run smoothly.

Q6 My company often launches new products and/or services.

Q7 My company’s suppliers often come up with new innovations.

Q8 My company is satisfied with the level of service and reliability offered by suppliers (e.g., few delays in deliveries of materials or services, acceptable quality, and level of services).

Q9 My company’s buyers requirements and demand are stable.

Q10 Projects within my company meet expectation (e.g., within budget and on time) more often.

Q11 For Projects, my company follows a set methodology and guidelines (e.g., PMBOK).

Q12 My company follows set monitoring policy for normal operations.

Q13 My company monitors suppliers closely.

Q14 My company has no time or resources to monitor operations.

Q15 My company monitors closely what is happening on the market side.

Q16 My company has put in place different types measurements or metrics for periodic monitoring.

Q17 Monitoring of routine operations is mostly event driven. I hardly look at operations unless a problem occurs.

My Company relies heavily on IT to facilitate monitoring and data collection. Q19

My Company is financially sound.

Q20 The external political situation (government policies and regulations) that affects the company is stable.

Q21 More effort (time and resources) is spent on monitoring external issues (political, economic, social, environmental, technological, and legal) than internal ones.

Q22 Investing on up to date technology brings competitive advantage to my company.

Q23 My company invests heavily in purchasing and upgrading IT systems, which are used for collecting and managing data (e.g., servers, applications, etc.).

<table><tr><td>Category</td><td>Questionnaire Number</td></tr><tr><td>Behavioral</td><td>Q1,Q12,Q13,Q15,Q17</td></tr><tr><td>External Environment</td><td>Q20,Q21,Q22,</td></tr><tr><td>Information Infrastructure</td><td>Q3,Q18,Q23</td></tr><tr><td>Hierarchical</td><td>Q2,Q16</td></tr><tr><td>Operational Dynamics</td><td>Q4,Q5,Q6,Q14,Q19</td></tr><tr><td>Supply Chain Dynamics</td><td>Q7,Q8,Q9,Q10,Q11,</td></tr></table>

Figure 2: Categories summary and associated questions

Figure 2 summarizes the factors presented in the 23 questions. The questionnaire was initially placed online using Google online documents, Google Forms. Over 80 responses were obtained. To reach respondents located in China, we also placed the same questionnaire on SurveyGizmo, creating an additional 30 responses. The survey was left online for approximately 2 months, resulting in a total of 110 valid responses.

## 3.2 Response Summary

The majority of those surveyed (69%; 76 people) were from “private companies,” while 19.1% worked for a public company (Figure 3).

<table><tr><td>Response Sector</td><td>Number</td><td>Percentage</td></tr><tr><td>Independent consultant</td><td>8</td><td>7.27%</td></tr><tr><td>Private Company</td><td>76</td><td>69.09%</td></tr><tr><td>Public Company</td><td>21</td><td>19.09%</td></tr><tr><td>Self-employed</td><td>2</td><td>1.82%</td></tr><tr><td>Other</td><td>3</td><td>2.73%</td></tr></table>

Figure 3: Summary of firm types

We collected responses from various industries, including ICT (27.3%), traditional manufacturing (16.4%), and automotive (12.7%). A summary is provided in Figure 5. The leading functional domains (Figure 5) include “Information Systems and Technology” (17.3%), “Products & Service Development” (14.5%), “Procurement” (10.9%), and “Operations” (10.9%).

<table><tr><td>Sector</td><td>Frequency</td><td>Percentage</td></tr><tr><td>Aerospace and Defense</td><td>1</td><td>0.91%</td></tr><tr><td>Automotive</td><td>14</td><td>12.73%</td></tr><tr><td>Banking</td><td>1</td><td>0.91%</td></tr><tr><td>Chemical and Pharmaceutical</td><td>8</td><td>7.27%</td></tr><tr><td>Consulting</td><td>3</td><td>2.73%</td></tr><tr><td>Defense Industry</td><td>1</td><td>0.91%</td></tr><tr><td>Distribution, Retail, and Wholesale</td><td>7</td><td>6.36%</td></tr><tr><td>Education</td><td>1</td><td>0.91%</td></tr><tr><td>Energy and Utilities</td><td>7</td><td>6.36%</td></tr><tr><td>Finance</td><td>1</td><td>0.91%</td></tr><tr><td>Food and Beverage</td><td>2</td><td>1.82%</td></tr><tr><td>Government</td><td>2</td><td>1.82%</td></tr><tr><td>Health Care</td><td>5</td><td>4.55%</td></tr><tr><td>Hospitality</td><td>1</td><td>0.91%</td></tr><tr><td>Information and Communication</td><td>30</td><td>27.27%</td></tr><tr><td>Industry and Manufacturing</td><td>18</td><td>16.36%</td></tr><tr><td>Insurance</td><td>1</td><td>0.91%</td></tr><tr><td>IT Manufacturer</td><td>1</td><td>0.91%</td></tr><tr><td>Law</td><td>1</td><td>0.91%</td></tr><tr><td>Media</td><td>5</td><td>4.55%</td></tr><tr><td>Total</td><td>110</td><td>100.00%</td></tr></table>

Figure 4: Summary of industry sectors

The highest response came from the non-managerial level (30%). Non-managerial encompasses specialists who may actually be performing managerial tasks without having a manager’s title. Project managers accounted for 21.8%, while 18.2% of respondents considered themselves to be middle managers. We could simplify these management level roles to the three levels described in Part I: “Top manager,” “Middle manager,” and “Lower manager- supervisor.” If we consider Senior manager and Senior leadership executive to be “Top management,” keep “Middle manager” and consolidate the rest into “Lower manager,” we obtain the following distribution for the sample space: 20% “Top manager,” 18.6% “Middle manager,” and the rest 61.4% “Operational manager - Local supervisor.”

Survey results were received from countries including Canada, USA, Vietnam, China, Singapore, UK, Sweden, Germany, and Spain. Because Google Form is blocked in China, all of the 24 valid responses from China are obtained from SurveyGizmo.

## 3.3 Managerial

## Implications

Figure 6 summarizes the questionnaire results including mean and standard deviation of each factor. Field (2003) suggests eliminating any data variables, or question answers, that have means that are off the scale. Here, the means vary between 2.4 and 3.76. Standard deviations are in the range from 0.93 to 1.22. Scanning through Figure 6 reveals that the answers to each

<table><tr><td>Functional Domain</td><td>Number</td><td>Percentage</td></tr><tr><td>Customer Service</td><td>6</td><td>5.45%</td></tr><tr><td>Environment</td><td>1</td><td>0.91%</td></tr><tr><td>Finance</td><td>6</td><td>5.45%</td></tr><tr><td>Human Resources</td><td>4</td><td>3.64%</td></tr><tr><td>Information Systems and Technology</td><td>19</td><td>17.27%</td></tr><tr><td>Marketing</td><td>7</td><td>6.36%</td></tr><tr><td>Operations</td><td>12</td><td>10.91%</td></tr><tr><td>Procurement</td><td>12</td><td>10.91%</td></tr><tr><td>Products and Services Development</td><td>16</td><td>14.55%</td></tr><tr><td>Project Management</td><td>1</td><td>0.91%</td></tr><tr><td>Quality and Customer Services</td><td>1</td><td>0.91%</td></tr><tr><td>Research and Development</td><td>1</td><td>0.91%</td></tr><tr><td>Risk and Compliance</td><td>3</td><td>2.73%</td></tr><tr><td>Sales</td><td>12</td><td>10.91%</td></tr><tr><td>Strategy</td><td>4</td><td>3.64%</td></tr><tr><td>Other</td><td>5</td><td>4.55%</td></tr><tr><td>Total</td><td>110</td><td>100.00%</td></tr></table>

Figure 5: Summary of functional domains

question are normally distributed with no outlying values.

Figure 7 shows the same questions now grouped by extracted components post factor analysis. Comparing the two, we can deduce that there is little in common between the theoretical and factor analyzed groups. However, taking into account the new components, we can make some observations and perhaps come to some insights on what latent factors exist.

Before rotation, we had a total of 13 variables, which loaded onto the first factor after rotation (Figure 8), this reduced to:

• <sub>7 variables loading onto Factor 1</sub>

• <sub>4 on factor 2</sub>

• <sub>4 on factor 3</sub>

• <sub>2 on factor 4</sub>

• <sub>2</sub> <sub>on</sub> <sub>factor</sub> <sub>5</sub>

• <sub>1 on factor 6</sub>

3 on factor 7

Component 1 groups variables that refer to financial stability, investment in IT, and company dynamics. We could perhaps state that this group relates to companies that are in sectors of growth, fast moving, and that possess the means to invest. They need to monitor what is

<table><tr><td></td><td>Mean</td><td>Std. Deviationa</td><td>Analysis Na</td></tr><tr><td>I spend a significant portion of my workday seeking information</td><td>3.37</td><td>1.012</td><td>110</td></tr><tr><td>I am more likely to gather and analyze internal company information rather than external company information</td><td>3.22</td><td>1.112</td><td>110</td></tr><tr><td>Information gathered by my company is adequate, timely, relevant, and useful for company operations</td><td>3.17</td><td>1.057</td><td>110</td></tr><tr><td>My company&#x27;s operations are fast moving and are constantly changing/evolving</td><td>3.39</td><td>1.134</td><td>110</td></tr><tr><td>My company&#x27;s logistics (transportation, storage, and distribution) run smoothly</td><td>3.23</td><td>1.011</td><td>110</td></tr><tr><td>My company often launches new products and/or services</td><td>3.6</td><td>1.06</td><td>110</td></tr><tr><td>My company&#x27;s suppliers often come up with new innovations</td><td>3.04</td><td>0.985</td><td>110</td></tr><tr><td>My company is satisfied with the level of service and reliability offered by suppliers (e.g., few delays in deliveries of materials or services, acceptable quality, and level of service....)</td><td>3.18</td><td>0.93</td><td>110</td></tr><tr><td>My company&#x27;s buyers requirements and demands are stable</td><td>3.23</td><td>0.992</td><td>110</td></tr><tr><td rowspan="2">Projects within my company meet expectations (For example: within budget, on time) more often Projects follow a set methodology (PRINCE2, PMP PMBOK, etc.).</td><td>3.27</td><td>1.013</td><td>110</td></tr><tr><td>3.18</td><td>1.198</td><td>110</td></tr><tr><td>My company has implemented and complies with a monitoring policy for day-to-day/routine operations.</td><td>3.42</td><td>1.152</td><td>110</td></tr><tr><td>My company monitors suppliers closely</td><td>3.26</td><td>1.114</td><td>110</td></tr><tr><td>My company has no time or resources to monitor operations</td><td>2.4</td><td>1.051</td><td>110</td></tr><tr><td>My company monitors closely what is happening in the market (competition, customer trends, etc.)</td><td>3.89</td><td>1.017</td><td>110</td></tr><tr><td rowspan="2">My company has implemented performance metrics, which I periodically monitor (KPI, Dashboards, etc.). I only review operations if a significant problem occurs</td><td>3.41</td><td>1.221</td><td>110</td></tr><tr><td>2.95</td><td>1.144</td><td>110</td></tr><tr><td>My company relies heavily on IT to facilitate monitoring and data collection</td><td>3.67</td><td>1.118</td><td>110</td></tr><tr><td>My company is financially sound</td><td>3.76</td><td>1.066</td><td>110</td></tr><tr><td>The external political situation (government policies and regulations) that affects the company is stable</td><td>3.37</td><td>1.188</td><td>110</td></tr><tr><td>More effort (time and resources) is spent on monitoring external issues (political, economic, social, environmental, technological, and legal) than internal ones</td><td>2.65</td><td>1.046</td><td>110</td></tr><tr><td>Investing in cutting edge/leading IT technology gives my company a competitive advantage</td><td>3.47</td><td>1.115</td><td>110</td></tr><tr><td>My company invests heavily in purchasing and upgrading IT systems, which are used for collecting and managing data (e.g., Servers, applications, RFID, ERP, etc.)</td><td>3.32</td><td>1.173</td><td>110</td></tr></table>

Figure 6: Summary of questionnaire result

<table><tr><td rowspan="2">Component</td><td colspan="3">Initial Eigenvalues</td></tr><tr><td>Total</td><td>% of Variance</td><td>Cumulative %</td></tr><tr><td>1</td><td>4.834</td><td>21.019</td><td>21.019</td></tr><tr><td>2</td><td>2.177</td><td>9.467</td><td>30.486</td></tr><tr><td>3</td><td>1.711</td><td>7.438</td><td>37.924</td></tr><tr><td>4</td><td>1.498</td><td>6.513</td><td>44.437</td></tr><tr><td>5</td><td>1.294</td><td>5.626</td><td>50.063</td></tr><tr><td>6</td><td>1.159</td><td>5.037</td><td>55.101</td></tr><tr><td>7</td><td>1.078</td><td>4.689</td><td>59.79</td></tr><tr><td>8</td><td>0.985</td><td>4.281</td><td>64.07</td></tr><tr><td>9</td><td>0.851</td><td>3.699</td><td>67.769</td></tr><tr><td>10</td><td>0.843</td><td>3.667</td><td>71.436</td></tr><tr><td>11</td><td>0.797</td><td>3.463</td><td>74.899</td></tr><tr><td>12</td><td>0.746</td><td>3.245</td><td>78.145</td></tr><tr><td>13</td><td>0.725</td><td>3.152</td><td>81.296</td></tr><tr><td>14</td><td>0.662</td><td>2.879</td><td>84.175</td></tr><tr><td>15</td><td>0.594</td><td>2.584</td><td>86.759</td></tr><tr><td>16</td><td>0.535</td><td>2.324</td><td>89.084</td></tr><tr><td>17</td><td>0.494</td><td>2.149</td><td>91.233</td></tr><tr><td>18</td><td>0.421</td><td>1.832</td><td>93.065</td></tr><tr><td>19</td><td>0.398</td><td>1.731</td><td>94.796</td></tr><tr><td>20</td><td>0.374</td><td>1.625</td><td>96.421</td></tr><tr><td>21</td><td>0.315</td><td>1.368</td><td>97.789</td></tr><tr><td>22</td><td>0.275</td><td>1.196</td><td>98.986</td></tr><tr><td>23</td><td>0.233</td><td>1.014</td><td>100</td></tr></table>

Figure 7: Variance analysis matrix per factors

<table><tr><td>Latent Factor</td><td>Loading Variables</td></tr><tr><td>Component 1</td><td>Q22, Q4, Q23, Q6, Q15, Q19, Q18</td></tr><tr><td>Component 2</td><td>Q12, Q13, Q14, Q16</td></tr><tr><td>Component 3</td><td>Q9, Q20, Q3, Q10</td></tr><tr><td>Component 4</td><td>Q2, Q21</td></tr><tr><td>Component 5</td><td>Q17, Q8</td></tr><tr><td>Component 6</td><td>Q5</td></tr><tr><td>Component 7</td><td>Q11, Q1, Q7</td></tr></table>

Figure 8: Question loading on latent components

happening in the market place and are prepared to invest in monitoring equipment to ensure that they remain competitive. In component 2, variables are more related to monitoring policies and techniques in place. Monitoring is dictated by monitoring tools and methods. Variables loading highly onto component 3 have a stability theme. Projects run on time, a n d the external situation is stable in terms of market and political situation. The information acquired is deemed to be adequate. Component 4 relates to hierarchy, where the emphasis is placed on monitoring externally or internally to the company. Component 5 gathers together supplier reliability and monitoring only in the event of a problem. This could be a hands-off approach, where as long as things are perceived to be running smoothly on the supplier side, no monitoring is done. Component 6 contains only one variable regarding the smooth running of company logistics. For component 7, the variance that can be explained by factors Q11, Q1, and Q7 in our study seem to contribute very little to overall managerial monitoring in companies.

<table><tr><td>Component</td><td>Possible Latent Factor</td><td>Characteristics</td></tr><tr><td>Component 1</td><td>Dynamic competitiveness</td><td>A Company’s “clockspeed” in terms of operations, suppliers, and marketplace is correlated with investment in IT for monitoring purposes.</td></tr><tr><td>Component 2</td><td>Methodology and behavioral</td><td>Monitoring best practice policies, certifications, and performance metrics (KPIs, Dashboards).</td></tr><tr><td>Component 3</td><td>Information seeking</td><td>External as opposed to internal information monitoring. Certain jobs within a company require searching for information.</td></tr><tr><td>Component 4</td><td>Supply Chain Dynamics</td><td>Supply Chain Dynamics, stability of suppliers, buyers, and adequacy of information.</td></tr><tr><td>Component 5</td><td>Stability</td><td>Company logistics and government policy.</td></tr></table>

Figure 9: Managerial implications

To gain a better insight into the collected data, several parameters in the factor analysis were adjusted. Here, results are presented with t h e 5 components extraction and direct Oblimin rotation. The Oblimin rotation is used if we sense that there might be a degree of correlation between the different factors (Field 2003). Furthermore, we can see that there exists non-negligible correlation between factor “1” and factor “4,” although the correlation is not very significant.

The components have similarities with the previous extraction (Figure 9). Component 1 encompasses a company’s need to monitor the competition. For instance, more monitoring may be needed in a fast “clockspeed” market (Fine 1998). Investment in IT is correlated with the “clockspeed” of a company; i.e., a company that often launches new products may result in more information gathering and therefore more monitoring. Interestingly, this is also related to the suppliers often coming up with new innovations leading to more IT investment. For Component 2, monitoring policies are grouped together. It can be noted that Q17 (“I only review operations if a significant problem occurs”) and Q14 (“my company has no time or resources to monitor operations”) are negatively correlated with the other variables in the category. This could be considered to be behavioral and also company culture. Best practices in monitoring are implemented and followed within the company. Component 3 ties together information seeking activities. Possibly certain job descriptions require a substantial amount of information gathering. Component 4 contains many of the theoretical supply chain dynamic variables. In Component 5 external stability is connected with how smoothly logistics run. Surprisingly, Q20 and Q5 are negatively correlated. Thus, we can say that the more unstable government policies, the more smoothly a company’s logistics are.

## 4 Conclusions

In order to discover effective business data acquisition based on ICT, we studied various requirements and information sources for effective management monitoring. To accomplish this, we conducted an exploratory study to evaluate current managerial monitoring needs and the importance of automated data collection technologies such as RFID among many others. Our study shows that the most important latent factor, which influence a company’s information need, is its dynamic competitiveness. The second important latent factor appears to be associated with the behavioral performance. Our study shows the importance of automated data system for high dynamic business processes and in high-speed supply chains.

In this study, we considered the role of managerial monitoring in business operations. Specifically, we discussed the traditional views of managerial roles and suggested a new perspective, where monitoring would be regarded as the pillar upon which all other managerial roles are based upon. We then looked at characteristics of information and its sources from a supply chain standpoint: Internal and external to businesses. We also presented an account of the different information channels. This was followed by an illustration of the two main monitoring mechanisms: event driven and periodical review. Hierarchy in management and the type of information different levels require was then described. Here, an analogy was made between the monitoring frequency at each management level and Nyquist’s sampling rate.

Based on this, we hypothesized that at

an operational level, a higher sampling rate would be required compared to a lower sampling rate at the top management level. We then looked at monitoring the supply chain. Characteristics of traditional supply chains were compared with those of new supply chains. As supply chains had to adapt to different market environments, we argued that perhaps different monitoring policies were required for different types of supply chains. Project management methodologies were then described, where monitoring in projects has been largely studied and where different theories on optimum monitoring frequency have emerged. To conclude, our review of related literature, we summarized the hypothetical issues affecting managerial monitoring that we inferred. These were “operational dynamics,” “supply chain dynamics,” “hierarchal,” “behavioral,” “information infrastructure,” and “external environment.”

Although our findings do not contradict the traditional view of data acquisition and managerial monitoring, this research offers some practical guidelines for today’s managers when business analytics is essential in their daily job. From an IT investment perspective, it also offers guidelines for an organization to determine how to reduce overspending on redundant equipment that track information that is never used. In addition, finding the underlying factors may well avoid catastrophes such as that which affected Tepco as a simple set of underlying factors may well make it easier for recruiter to hire the right manager for the right job. Future extensions to this study can be directed at the investigation of the degree of impact of discovered latent factors on managerial monitoring effectiveness. Based on this research, it is also interesting to study the efficient mechanisms for different companies to optimize their managerial monitoring practices.

## References

[1] Alge, B. J., & Hansen, S. D. (2014). Workplace monitoring and surveillance research since “1984”: A review and agenda. The psychology of workplace technology, New York, NY, 209-237.

[2] Bose, I., Lui, A.K.H., Ngai, E.W.T. (2011) The Impact of RFID Adoption on the Market Value of Firms: An Empirical Analysis. Journal of Organizational Computing and Electronic Commerce, 21(4), October, 268-294.

[3] Bose, I., Yan, S. (2011) The Green Potential of RFID Projects: A Case-based Analysis. IEEE IT Professional, 13(1), 41-47.

[4] Bose, I., Pal, R., Ye, A. (2008) ERP and SCM Systems Integration: The Case of a Valve Manufacturer in China. Information & Management, 45(4), 233-241.

[5] Chopra, S., Meindl, P. (2010) Supply Chain Management: Strategy, Planning, And Operation, Pearson, New Jersey.

[6] Collins, R. (2010) A Graphical Method for Exploring the Business Environment. http://users.ox.ac.uk/ kell0956/docs/PESTLEWeb.pdf

[7] Daft, R.L. (1983) Learning the Craft of Organizational Research. Academy of Management Review, 8(4), 539-546.

[8] Field, A. (2003) Discovering Statistics using SPSS for Windows. Sage Publications, London.

[9] Fine, C. H. (1998) Clockspeed: Winning Industry Control in the Age of temporary Advantage. Basic Books, New York.

[10] Galbraith, J.R. (1973) Designing Complex Organizations. Addison-Wesley Longman. Boston, MA.

[11] Hair, J.F., Money, A.H., Samouel, P., Page, M. (2007) Research Methods for Business. John Wiley, New Jersey.

[12] Hague, J., and Aiken, M. (1969) ”Routine Technology, Social Structure and Organizational Goals,” Administrative Science Quarterly, 14, 366-76.

[13] Mintzberg, H. (1973) The Nature of Managerial Work. Harper and Rowe.

[14] Porter, M. E. (1985) Competitive Advantage. The Free Press, New York.

[15] Schlesinger, R.J., Ballew,V.B. (1989) An application of the sampling theorem to data collection in a computer integrated manufacturing environment. International Journal of Computer Integrated Manufacturing, 2(1), January.

[16] Shannon, C.E. (1949) Communication in the presence of noise. Proceedings of the Institute of Radio Engineers, 37(1), 10-21.

[17] Weick, K.E. (1979) The Social Psychology of Organizing. Second Edition. McGraw-Hill.

[18] Zhou, Z., W., Jia, G., Hu, C., Xu, X., Wu, X., & Pan, J. (2016). A method for realtime trajectory monitoring to improve taxi service using GPS big data. Information & Management.

#

## Biography

Wei Zhou holds a Ph.D. degree in Information Systems and Operations Management from the Warrington College of Business Administration, University of Florida. He also has a master degree in electrical engineering (M.S.E.E.) from the University of Nebraska - Lincoln, and bachelor degree from Shanghai Jiaotong University. Currently he is an associate professor in the Information and Operations Management Department of ESCP Europe Paris Campus.

Wei Zhou was nominated as one of the "Star Professors" in the business schools in France by L'etudiant. weblink: "http://www.letudiant.fr/educpros/enquetes/a-la-rencontre-des-profs-stars-enecole-de-commerce.html"[article in French]

Wei Zhou has teaching interests in Electronic Commerce, Business Analytics, management science and supply chain management. His areas of research interests are in data mining, mechanisms for Web-enabled e-commerce applications, knowledge-based systems, effectively utilizing information for decision support through analytical models and simulation and supply chain management. His work has been published or accepted in Annals of Operations Research, Decision Support Systems, European Journal of Information Systems, European Journal of Operations Research, IEEE Letters, International Journal of Electronic Commerce, International Journal of Production Economics, International Journal of Production Research, Journal of Business Ethics, Journal of Organizational Computing and Electronic Commerce and Optical Engineering, among others.

Wei Zhou has served as ad-hoc reviewer for Decision Support Systems, European Journal of Information Systems, European Journal of Operational Research, Information Systems and e-Business Management, International Journal of Computer Systems Science and Engineering, International Journal of Electronic Commerce, International Journal of Production Economics and Transportation Research. He is an member of: INFORMS, AIS, DSI, IEEE and SPIE.

Selwyn Piramuthu is Professor of Information Systems at the University of Florida. His research interests include RFID systems.
