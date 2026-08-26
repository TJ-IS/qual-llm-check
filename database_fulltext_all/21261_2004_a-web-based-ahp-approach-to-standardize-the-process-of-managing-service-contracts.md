---
otero_id: 21261
otero_key: "SYS2EBNU"
title: "A Web-based AHP approach to standardize the process of managing service-contracts"
authors: "R.P. Sundarraj"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00033-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# A Web-based AHP approach to standardize the process of managing service-contracts

R.P. Sundarraj\*

Department of Management Sciences, University of Waterloo, 200 University Avenue West, Waterloo, Ontario, Canada N2L 3G1

Received 28 January 2002; accepted 18 November 2002

Available online 30 April 2003

## Abstract

Despite the gainful use of the Web as a communication medium, recent research suggests that very little work has been done to leverage this new technology for enabling changes in the planning process. This paper, motivated by a situation at a Fortune 100 company, describes a prototype Web-based decision support system (DSS) for the management of service contracts, which are being increasingly purchased by a variety of businesses. The planning for spare parts needed to support service contracts is hampered by unpredictable and extremely low demands, thereby necessitating a subjective manual approach that is inherently non-standardized and non-coordinated among the various constituents of the organization. In this paper, we describe how a Web-based system can enable the standardization of the process of managing and supporting service contracts. In addition, our DSS supports geographically and functionally dispersed decision-making roles, thereby displaying characteristics of an organizational decision support system (ODSS). <sup>D</sup> 2003 Elsevier B.V. All rights reserved

Keywords: Services; Contracts and warranties; Electronic commerce; World Wide Web; Decision support system; Analytical Hierarchy Process; Heuristics

## 1. Introduction

Electronic commerce businesses have been growing at a tremendous rate. Yet, researchers have suggested that most large companies have done little to leverage the Internet, other than as a publishing medium. Only about 5% of large companies conduct transactions via the Web, and the total global value of Web transactions is only about US\$5 billion [15,16]. A number of companies do not know whether the Web will be effective for them, whether to even establish a Web presence or what they can do to increase its effectiveness [6,45]. More importantly, among those who have chosen to use the Web, only a few companies are focusing on changing their back-end planning practices to make the most use of the Web [15,16]. Recent research publications confirm that efforts on using the Web are targeted toward attracting customers and then retaining them through appropriate marketing and personalization strategies. For example, Yen [75] describes a Web-based system that improves three front-end tasks in the apparel industry: generation of a catalog, conducting of searches and monitoring of usage patterns. Efstathiou et al. [19] describe a system of conducting a high-level evaluation of manufacturing organizations. Sen et al. [61] list the incorporation of Web technology as one of the challenges of future decision support systems (DSSs), and Keskinocak et al. [39] write that their system ‘‘is the first decision support system that helps companies identify good one-to-one matches and multi-way matches in business-to-business e-marketplaces.’’

The goal of this paper is to fill this gap by considering a back-end planning process in the services industry. Our paper has been motivated by a situation at Alpha, which is a pseudo-name of a Fortune 100 company having revenues of about US\$52 billion. We describe a prototype Web-based decision support system for standardizing the process of managing service contracts. Alpha supports over 9000 service contracts requiring a same-day response.

The research literature considers service contracts as a crucial component of service management [36]. Service contracts provide an organization with the ability to operate its equipment with reduced downtime, and they are being increasingly purchased by a number of companies as well as governmental agencies. For example, the United States Federal government has signed an US\$8 million, 5-year contract with Trilogic to provide information technology services to federal agencies across the country, without going through a bidding process each time an equipment fails [26]. British Telecom (BT) has signed an £8 million, 3-year service contract with IFR systems to supply maintenance services to BT’s field and laboratory equipment [4]. Likewise, to provide better service to its customers, Dell signed a US\$6 billion agreement with IBM, whereby IBM’s global services will provide warranty services and on-site support for Dell’s customers, beginning early 2000 in the United States and expanding globally thereafter [47]. These examples demonstrate the generality of the problem described in this paper.

From the service organization’s viewpoint, when a customer requests service on an equipment under contract, the necessary service parts must be available to an engineer entrusted with the responsibility of fixing the equipment. The inventory planning needed to support such requests will have to determine whether the needed service parts for the contract be positioned at a central warehouse or at local stockrooms near the customer’s site. Central positioning is advantageous, because stocking quantities can be greatly reduced due to demand-pooling effects [62]. However, for a great number of contracts considered in this paper, the response duration is too short (e.g., 2 h, 4 h) to make central positioning possible, and hence, a local stocking must be used. The derivative questions then are: Which contracts must be supported by stocking the service parts at a local group of stockrooms, given a budget on those stockrooms? How should a manager allocate budgets to a group of local stockrooms? How should contracts be priced?

As we will see, the above-mentioned decisions require that a number of intangible attributes be considered as well, in addition to the demand history of the service parts. These attributes include, for example, the age of the contract and the size of the contract. In addition to these attributes, there is commonality of service parts among the contracts. Given these issues, a decision maker faced with the task of allocating a tight budget among the contracts will have to evaluate a combination of factors (e.g., old large contract versus new small contract) and then make decisions that takes advantage of inter-contract commonalities. At the very least, this decision process is time consuming, in addition to being non-standardized.

This paper describes a prototype Web-based system to aid with the above-mentioned issues. The prototype approach has been suggested in the literature [65,72] and has been applied in a number of recent DSS implementations as well [40,61]. Our system aims to standardize the planning process and to economize on the budget by taking advantage of commonality of service parts among contracts. The underlying model base consists of heuristics combined with the Analytical Hierarchy Process (AHP) model, which has not been applied to such a setting. Our system also has characteristics of an organizational decision support system (ODSS): It offers support to different functional and managerial levels, and it uses the Web communication technology to support people located at varied geographic locations.

The paper is organized as follows. Section 2 describes the unique aspects pertaining to service contract management, leading to an discussion of factors that must be considered in this management problem. Section 3 gives an overview of Alpha, the company whose situation motivated this paper. Sections 4 and 5 describe the components of the Webbased system, and Section 6 discusses the implications of the system, as applied to Alpha. Our concluding remarks are in Section 7.

## 2. Key issues in service contract management

Demands typically serve as the primary inputs to plan for service parts. With this planning approach, the demand is modeled using a statistical distribution, and then the stocking decision is set by trading off stockout costs against inventory costs, as given in

$$
\text { Prob } (\text { stockout }) \times \text { Stockout   cost } = \text { inventory   cost },\tag{1}
$$

where Prob(stockout) denotes the probability of stockout.

This approach would, however, not be sufficient for service contract management. Service operations are often characterized by intangibilities, and this influences the manner by which service contracts are managed. Thus, we propose that demands be used to categorize contracts and that, in addition, a number of intangible attributes be considered in service contract management. Using the research literature, we review these intangible attributes in Section 2.1. The evaluation of such intangible factors leads to a non-standardized management of service contracts; Section 2.2 discusses the importance of the Web in this context.

## 2.1. Intangible issues in contract management

We classify the intangible attributes below into customer-, contract- and product-related ones.

## 2.1.1. Customer-related attributes

Three customer-related attributes are proposed: customer type, the type of application in which the equipment is involved and customer participation.

 Customer Type (CusTyp) indicates the quality expectations and perceptions of the customer. This attribute is important, because unlike manufacturing, in which the quality of a product can be measured against tangible design specifications [36,37], service quality is measured, in part, by whatever the customer perceives it to be [25,36,76]. This means that the service organization has to contend with heterogeneous customer expectations [29,46], with the more stringent customers being given a higher priority in the planning process (see, e.g., Ref. [49] for a discussion on psychological issues affecting a customer’s perception towards waiting). For example, in the service contract management issues presented in this paper, one could envisage different kinds of quality perception by the customer. One customer could be concerned about the service engineer reaching the customer site on time, another could be concerned about whether the problem was fixed on time (even though the engineer was late), while a third customer could be satisfied as long as the equipment was fixed without affecting the company’s bottom line.

 Customer Application Type (CusAppTyp) relates to the manner in which the product under contract is being used by the customer. It is common to envisage heterogeneous uses of the same equipment by various customers [14], and this heterogeneity, in turn, affects the service delivery process as well [36]. When there is heterogeneity, the service provider maintains a different type of service for the same equipment, depending on how equipment failure affects, for example, safety, operational availability and/or finances [14,55]. For example, the computer of the president of an organization would be serviced ‘‘better’’ from a regular employee’s.

Customer Participation (CusPar) relates to whether the customer is part of the service delivery process. Unlike manufacturing, the customer often participates in the production of the service [7,21,36]. The importance of this participation is well-established conceptually [3,7,25], as well as in recent empirical research [21], in which participation is found to have a positive impact on quality and customer satisfaction. Given this finding, a service organization can then, depending on its value proposition, choose to emphasize the set of customers who participate in the service process, or to provide a better-quality service to customers who do not participate and thereby seek to expand the organization’s customer base in that market.

## 2.1.2. Contract-related attributes

In this category, four attributes are considered.

Contract Response Duration (CRes) denotes the time within which the customer’s request must be serviced. This is a key attribute [1]. Empirical research in service management has shown that responsiveness has a significant influence on the perception of service quality [2,76]. In the maintenance management in particular, responsiveness is important, because disruption in an equipment’s operation is typically very expensive [34,44]. The lower the response duration, the greater is the importance of the contract. Because inventory levels of spare parts are generally very low, the spare parts allocation decision becomes crucial when rapid response is required [38].

Contract Size (CSiz) denotes the degree of service provider’s relationship with the customer as far as the contract is concerned. The importance of this attribute arises due to the facts that customer relationships deliver superior profits to the service organization, and that organizations discriminate in favor of their ‘‘high-share’’ customer over their ‘‘low share’’ customer [42]. Pine et al. [52] state that the customer’s dollar volume of current and continuing purchases is critical to the service provider. Emmelhainz and Kovan [20] have shown empirically that the potential revenue from a customer is a key variable for customer segmentation, and that the resulting segmentation itself is then used to tailor a tiered response to the customer’s demands.

Contract Age (CAge) denotes the length of the service provider’s relationship with the customer as far as the contract is concerned. Newer contracts have an element of uncertainty, whereas older ones acquire some of the dynamics of a business relationship, with the service organization learning more about the nuances of the customer’s requirement for that contract [36]. Organizational learning can lead to the customization of service delivery and improvement of quality [28,32,48] and has the potential to influence the internal processes in an organization [32]. Pine et al. [52] give some specific examples of the influences of organizational learning on service delivery. The impact of age on contract management depends on whether the service organization wants to deepen its relationship with an existing market base, or to broaden its set of customers.

Contract Type (CType) denotes whether the service is reactive (i.e., service happens after equipment breakdown) or proactive. Proactive or preventive maintenance is commonly done, because of the cost of disruptions [34,44], and because such maintenance reduces the overall maintenance costs [54] as well as the chances of a breakdown. Because preventive-maintenance services are performed based on factors such as age, condition, elapsed time since last maintenance or failure characteristics [53,73], their timing is somewhat known. This makes the spare part demands for preventive contracts to be more predictable, thereby making it less important for the corresponding service parts to be stocked locally.

## 2.1.3. Product-related attributes

We consider four product-related attributes: the cost of product (which is taken up in Section 4.2), the stage of the product’s life cycle, the criticality of the product and the age of the unit under contract.

 Product Age (PAge) indicates the stage of a product in terms of where it is in its life cycle. PAge is important to service contract management [68,69], because as long as a product is in a mature stage of its life cycle, spare parts can be easily purchased. However, spare parts are difficult to get for end-oflife products.

The nature of the influence of PAge on the stocking decision depends on whom the service provider is [66]. If the service provider is a retailer, then spare parts for end-of-life products would not likely get stocked, but if the service provider is the manufacturer itself or an after-market parts vendors, then spare parts would be stocked for declining products as well [60,66].

 Product Criticality (PCri) indicates the criticality of the product as it is typically used (this distinguishes PCri from CusAppType, which specifies how the product is actually used). The literature has acknowledged the importance of product criticality in making stocking decisions concerning spare parts [31]. This has led researchers to devise schemes for classifying the criticality of a product, by using, for example, expert systems [51] and multicriteria approaches [23]. Certain products such as an Internet Router are inherently critical, and hence, it would be important to locally stock the spares for such products.

 Product Unit Age (PUnitAge) indicates the age of the actual unit under contract (this is different from PAge, which affects the availability of spare parts). The age of a unit plays an important role in maintenance management, with older products being more likely to breakdown, and therefore, being more likely to be stocked for at a nearby stockroom. See, for example, Refs. [63,74,77] for models/policies of how age is factored into maintenance decisions.

Section 2.2 describes how a Web-based system helps in the standardized evaluation of these attributes.

## 2.2. Importance of a Web-based system

Even though the Web has become a ubiquitous communication medium today [50], a majority of Web-based systems thus far are limited to being a publishing medium, or to providing mechanisms for conducting or supporting online shopping, or to designing virtual organizations that support shopping activities. Dutta and Segev [15] estimate that only about 5% of large companies conduct transactions via the Internet and that the total global value of Internet transactions is only US\$5 billion. These researchers argue that only a small percentage of companies is focusing on changing their business practices through the deployment of Web-based systems. Sen et al. [61] list the incorporation of Web technology as one of the challenges of future decision support systems. More recently, Beatty et al. [6] indicate that many firms are still considering whether to establish a Web presence. This is also echoed by Lynn et al. [45] and by Sadowski et al. [58] who state that:

While some SMEs benefit from rapid Internet growth, selling over the Internet or experimenting with new business models, others are barely interested in it.

Because service contract management involves the evaluation of several attributes and of several values per attribute, a large combination of factors need to be compared by the decision maker (i.e., a planner must evaluate a new small contract with respect to an old large contract, etc.). In addition, commonalities among contracts would affect the actual stocking cost. Finally, because contracts are signed from a wide range of geographic places, their management, in turn, involves different people from multiple places. These facts, relating to contract management, result in a number of problems. First, the evaluation of a large combination of attributes is time consuming and could be difficult from a cognitive perspective. Second, over a period of time and over different regions of an organization, there is likely to be significant differences in the manner by decision makers evaluate contracts (e.g., some decision makers may consider all the attributes in Section 2.1, while other might evaluate only a subset), thereby yielding service quality that varies significantly with geographic location and time. Finally, these aforementioned problems occur, even though there is no change in management policy.

In this context, the importance of a Web-based system arises from research [35,70] that shows that the impact of a DSS is enhanced when the decision on hand is characterized by an increase in the number of alternatives to evaluate. By using the Web, the preferences and evaluation of contract attributes can be made uniform. It can be ensured that contracts with similar attributes will be evaluated similarly, at all times that the policy is in effect. In addition, every decision maker will be using the same Web-based set of policies, thereby making the contract management process more uniform. Knowing this process, contract-sales personnel can rely on the system to exactly obtain the cost of supporting a contract and, in turn, make an assessment of the price that must be quoted to the customer for the contract. Further, standardization is also significant to a management team that wants to see operational-level actions to be in consonance with the corporate policy of the service organization.

Finally, we take up the question of whether the Web technology is necessary for the working of the system. First, in a non-Web-based proprietary computing environment, vendors have their own methods for connecting a remote client to a network. Thus, a programmer will have to know the details about this connection mechanism in order to develop the system [33]. This is unlike a Web-based application in which the programmer can create a system without understanding the underlying network details. The only information needed by a client program is the application name and the (server) computer on which the application resides [11,p,18]. In fact, with technologies such as remote method invocation, even the physical name of the server can be abstracted away from the client [11,p,552]; the client, of course, needs to know the logical server name. This simple programming paradigm is also advantageous when the database management system at the server (or the server itself) has to be changed to improve system performance. Again, the code on the client will remain essentially free of changes. Third, because the Web uses a standardized output protocol, namely HTTP, the delivery of the results on the planner’s screen is independent of the computing architecture used by the planner. Because user interfaces are hard to develop and do change over time [8], a lot of programming time can be saved by avoiding the customization of the output to each architecture and to each change of the planner’s computer. For all these reasons, the maintenance costs of a Web-based system can be considerably lower than that of a traditional one. This is significant, because research has shown that maintenance consumes a majority of the system’s costs [5, p. 433].

Thus, in summary, while one could argue that the DSS development could be undertaken using traditional programming, the Web approach offers a number of the aforementioned technical and programming advantages. Section 3 presents a case study that motivated the Web approach.

## 3. Case study

Our problem was motivated by a situation faced by Alpha, a Fortune Global 100 company supplying computing systems worldwide. Alpha’s revenue is around US\$52 billion. Alpha designs, develops, manufactures and markets hardware, software, solutions and services, including enterprise and fault-tolerant solutions, communications products and desktop and portable products. Alpha’s products and services are sold in more than 200 countries, through marketing partners and also directly to businesses and consumers. The problem taken up in this paper occurred at Alpha’s services division whose revenues are US\$6 billion. Given below are the entities of this division relevant to the project.

Sales. This department is involved with seeking out customers to sign contracts with Alpha for the products that they purchase. The responsibilities of sales include setting out the fix time, the equipment that is under contract, the situations under which a contract is applicable and the cost of contract.

Customer. At the other end of the chain is the customer with whom the contract is signed. Customers call a pre-assigned phone number when an equipment fails.

Contract. This instrument between Alpha and the customer specifies the product on coverage, the type of coverage, the duration of coverage and the price.

Service Parts. These are parts that are needed to repair an equipment that is down.

Logistics. This department is responsible for managing the physical inventory at the warehousing system. A two-echelon warehousing system, consisting of a central warehouse and local stockrooms, is employed.

Material Managers. These managers are responsible for setting policies concerning inventory planning, the acquisition of information technology resources to conduct the planning and also for setting business processes for conducting planning. Planners. Planners are responsible for specifying to logistics the spare parts to stock and the stocking location of the part.

Overall, Alpha has over 1500 critical contracts that require a 2-h response and another 7500 that require either a 4- or 8-h response. For a number of the service parts, the actual usage is very low. To give an example, the consumption at divisional-level stockrooms is below 20 units per year (i.e., 1.67 per month)

for a significant number of the parts. Hence, planners find it difficult to distinguish one consumption pattern from another, and to do so consistently over a period of time. In this unclear evaluation mode, planners become risk-averse and, therefore, tend to stock parts unnecessarily. Further, given the worldwide reach of Alpha, various planners adopt their own individual approaches to evaluate contracts and to stock for them. Because of all these reasons, Alpha observed that in recent years, consumption arising from these contracts had dropped disproportionately to the actual inventory stocking. For example, over a 5-year period, the dollar-value of inventory consumption dropped by 47%, whereas the dollar-value of the actual inventory stocking dropped by only 25%, thereby showing Alpha’s management the huge potential for saving on inventory costs (this savings potential also finds support in the research literature [10,38]). Finally, material managers and sales personnel were not able to coordinate their activities with those of the planners. Alpha therefore decided to implement a decision support system with the goal of standardizing the planning process and of optimizing inventory.

The remainder of the paper describes how a Webbased system can serve as an enabler to address these concerns.

## 4. Model

There are two aspects to our model. The first is a methodology for evaluating contracts, while the second aspect seeks to take advantage of common service parts among the contracts.

## 4.1. Standardized evaluation

One approach to standardizing the contract management process is to obtain ordinal preferences of the contractual attributes (given in Section 2.1) and then to rank-order the contracts based on a weighted average of those preferences. This approach would, however, be difficult, because of the need to process a number of factors simultaneously. We therefore compare a pair of attributes at a time—pairwise comparisons (PWCs). Recent field studies also confirm the effectiveness of this approach. In assessing a number of methods to evaluate multiple intangible attributes,

Easley et al. [18] found that a decision-making approach that explicitly accounts for the hierarchical structure of the problem and that utilizes PWCs of attributes ranks alternatives better than one that does not. Easley et. al.’s research studied the evaluation of alternatives by groups of decision makers and is thus significant to our problem, which involves the evaluation of contracts by different planners and managers.

Our method to standardize the management of contracts can be viewed in two levels, as shown in Fig. 1 (in Section 5, we will see how the system design permits both the generalization as well as the simplification of the following methodology). At Level 1, the organization specifies a set of attributes that must be considered for contract management. These attributes are then evaluated with respect to their relevance to organizational policy. The evaluation is performed using PWCs, in which the importance of attribute i over attribute j is recorded on a ratio scale of 1/9 to 9. A 9 indicates the extreme importance of i over j, a 1/9 indicates the extreme importance of j over i, and a 1 indicates equal importance.

Given the wide range of decision makers and that of needs within the organization, preferences are decided by an appropriate combination of managers and planners. A team-developed approach (as in, e.g., Ref. [64]) must be utilized for eliciting the preferences, which must be reviewed periodically for relevance.

![](/api/attachments/SYS2EBNU/fulltext/images/65ddb98974a1890d25fa2aa0fd45c9a2a60bc8011e60f1f72ef4e35b93b42778.jpg)  
Fig. 1. Overview of the standardization process.

The attribute preferences are then evaluated by the AHP model [56], which has not been applied to the inventory planning setting. AHP has been recommended as a useful decision-making approach [18,22], despite concerns such as rank-reversal. AHP involves an eigenvector calculation given by:

$$
\mathbf {A} \lambda = \boldsymbol {w} \lambda ,\tag{2}
$$

where A represents the matrix of PWCs for each contract, w represents the vector of importance weights for attributes, and k represents the eigenvalue.

While Level 1 gives the importance of an attribute, the goal of Level 2 (Fig. 1) is to specify the stocking preference for the contract on each attribute. This is done by specifying stocking preferences for attribute values and contract categories (as mentioned in Section 2.1, demands are used to categorize contracts). In turn, in order to ensure uniformity of evaluation, all contracts with a certain value on an attribute are given the same stocking preference. To illustrate, if the stocking preference is 0.9 for new Category B contracts, 0.83 for old Category B contracts and 0.875 for large Category B contracts, then a new large Category B contract will receive a stocking preference of 0.9 on the CAge attribute and a preference of 0.875 on the attribute CSiz. For an old Category B contract, however, the preference on CAge is 0.83.

Finally, the stocking preference of a contract on each attribute i is combined with the importance of that attribute (ith element of w computed from the AHP step given by Eq. (2)), as given by:

$$
\sum_ {i \in \text { set   of   attributes }} w _ {i} p _ {i},\tag{3}
$$

where $p _ { i }$ is the stocking preference of the contract on attribute i. This calculation yields the importance weight of a contract.

## 4.2. Coping with commonality

The importance weights of the contracts can now be used to decide on the contracts that must be stocked for at a local stockroom. Because of service part commonalities among the contracts, the cost of stocking for a contract i depends not just on the parts needed for servicing the product involved, but also on the parts already present at the intended stocking location and on the stocking decision of other contracts that share service parts with contract i. A simplified summary of the method employed to address this decision is as follows. First, we sort contracts in accordance with their importance levels. This sorting ensures that the most important contracts get considered first before a less important one. Next, a heuristic cost function is computed for each contract–stockroom combination. The idea of the heuristic function is to determine a probabilistic estimate of the additional cost that will be incurred by stocking for the contract at that stockroom. Because of commonalities, this additional cost could be smaller than the total of the cost of all service parts needed for a contract. Contracts are assigned to the stockroom yielding the lowest heuristic cost function. Finally, contracts that can be accommodated within the budget are stocked for. A detailed example illustrating these steps is given in Section 4.3.2.

Because the above methodology standardizes the evaluation of contracts and economizes by taking advantage of inter-contract commonalities, it can serve as a basis for allocating budgets to local stockrooms as well. Managers can use this method to determine the number of contracts that can be supported locally and make a decision on whether this number is acceptable from a service viewpoint.

## 4.3. Illustrations of the methodology

In this section, we illustrate different features of our methodology using a number of examples; Section 4.3.1 deals with AHP and Section 4.3.2 deals with the heuristic.

## 4.3.1. AHP illustrations

Our first two examples are meant to show the usefulness of the AHP approach in standardizing the process of service contract management. Examples 3, 4 and 5 discuss the sensitivity of the AHP solutions to changes in input data.

4.3.1.1. Example 1 (basic AHP). To illustrate how the methodology can be used to standardize decision making, consider a scaled-down example consisting of: (i) three attributes CSiz, CusTyp and CAge; (ii) two values per attribute; and (iii) two product Categories A and B, with Category B contracts having a higher demand as compared to ones in Category A. Consider three contracts given in Table 1a. An examination of the attribute values brings up two issues. First, even for this small example, a decision maker will have to evaluate multitudes of combinations in assessing the three contracts $( 2 \times 2 \times 2 \times 2 = 1 6 )$ . Research literature suggests the effectiveness of a DSS in such combinatorial evaluations [35,70]. Second, two decision makers can differ widely in their evaluation of this same data.

Table 1a  
Illustration of standardization approach

<table><tr><td colspan="4">Characteristics of contracts</td></tr><tr><td></td><td>Contract I</td><td>Contract II</td><td>Contract III</td></tr><tr><td>Category</td><td>A (low)</td><td>A (low)</td><td>B (high)</td></tr><tr><td>CSiz</td><td>Small</td><td>Large</td><td>Large</td></tr><tr><td>CusType</td><td>Critical</td><td>Noncritical</td><td>Noncritical</td></tr><tr><td>CAge</td><td>New</td><td>Old</td><td>Old</td></tr></table>

As a way to ease these issues, first, the attributes are evaluated pairwise, and preferences are given as shown in Table 1b (Level 1 of Fig. 1). For the preferences given therein, managers view a contract’s size to be more important than contract age and customer type. To see the amount of importance of each attribute, we use Eq. (2) to compute the eigenvectors for this PWC matrix and get the importance weights shown in the shaded column of Table 1b. Next, Table 1c shows the stocking preferences for the various attribute values (Level 2 of Fig. 1). Note how contracts that have more critical customers, which are new and large sized, are given higher preferences for stocking as compared to those with inferior values on those attributes. Also note that the stocking preferences are higher for Category B contracts than for Category A. To evaluate how this information can be used on a day-to-day basis to evaluate contracts, we use Eq. (3) to obtain an overall importance of each contract. As an example, for Contract I, Eq. (3) yields:

Table 1b

<table><tr><td colspan="5">Pairwise preferences of attributes (Level 1)</td></tr><tr><td></td><td>CSiz</td><td>CusType</td><td>CAge</td><td></td></tr><tr><td>CSiz</td><td>1</td><td>3</td><td>2</td><td>0.53</td></tr><tr><td>CusType</td><td>0.33</td><td>1</td><td>0.33</td><td>0.14</td></tr><tr><td>CAge</td><td>0.5</td><td>3</td><td>1</td><td>0.33</td></tr></table>

Table 1c

<table><tr><td colspan="3">Stocking preferences for attribute values (Level 2)</td></tr><tr><td></td><td>Category A(Low)</td><td>Category B(High)</td></tr><tr><td>New CAge</td><td>5/6</td><td>7/8</td></tr><tr><td>Old CAge</td><td>1/3</td><td>1/2</td></tr><tr><td>Critical CusType</td><td>5/6</td><td>5/6</td></tr><tr><td>Noncritical CusType</td><td>1/2</td><td>1/2</td></tr><tr><td>Large CSiz</td><td>7/8</td><td>9/10</td></tr><tr><td>Small CSiz</td><td>1/3</td><td>1/2</td></tr></table>

$$
0. 5 3 (1 / 3) + 0. 1 4 (5 / 6) + 0. 3 3 3 (5 / 6) = 0. 5 7.
$$

The results for the other contracts are shown in Table 1d, which suggests Contract III to be the most important. .

4.3.1.2. Example 2 (standardization). Consider a situation in which there is an aggressive company policy to personalize service according to the type of the customer. Such a customization of service has support from the research literature [36]. To translate this policy into the evaluation of a contract, our methodological framework suggests the alteration of attribute weights to appropriately reflect this change. An example set of changed PWCs is given in Table 2a. These PWCs are then evaluated by Eqs. (2) and (3) to obtain the new importance weights. Table 2b shows how the method yields different importance weights for the same contracts. The point is that such a change can be applied throughout the organization.

Next, we consider three kinds of sensitivity analysis, the first relating to changes in one of the importance weights, the second concerning perturbations to the entire PWC matrix and the third to rankreversal, a common problem associated with AHP [17]. All the analyses are conducted using a baseline contract, for which Table 3a gives the PWC matrix (for Level 1 factors) and stocking preference for each factor (Level 2). For this data, the importance weights and decision, computed using AHP, are given in Table 3b. .

Table 1d

<table><tr><td colspan="3">Overall importance of each contract</td></tr><tr><td>Contract I</td><td>Contract II</td><td>Contract III</td></tr><tr><td>0.57</td><td>0.64</td><td>0.71</td></tr></table>

4.3.1.3. Example 3 (changes to importance weights). The sensitivity analysis due to weight changes is often given in well-known AHP packages [71]. In this analysis, the weight of a factor is changed from 0 to 1. With each such change, the weights of the remaining factors are normalized, so that all the resultant weights add to one. That is, if is the weight change in factor $j ,$ the weight of factor k $( k { \neq } j )$ is adjusted by $\partial w _ { k } \big / \sum _ { k } w _ { k }$ . Then, the final stocking weight is computed with the resultant weights of the factors.

Our first two weight changes are to the CusType and PAge attributes. For both these factors, the stocking preferences are high (0.875 and 0.8, respectively, as shown in Table 3a). Hence, as their weights are increased, the final stocking weights for the contract can also be expected to increase. This is demonstrated in Fig. 2a and b. The last weight change is to the CType attribute. In this case, the non-stocking preference is high. Thus, a change in the decision (i.e., from stock to non-stock) could occur with an increase in CType’s weight. This is shown in Fig. 2c. In conclusion, from these changes with this sample data, we see that the AHP results can be intuitively explained and do not appear to be drastically sensitive to changes in the weights. .

Table 2a  
Affecting decisions by policy change

<table><tr><td colspan="4">Pairwise preferences of attributes</td></tr><tr><td></td><td>CSiz</td><td>CusType</td><td>CAge</td></tr><tr><td>CSiz</td><td>1</td><td>0.5</td><td>2</td></tr><tr><td>CusType</td><td>2</td><td>1</td><td>4</td></tr><tr><td>CAge</td><td>0.5</td><td>0.25</td><td>1</td></tr></table>

Table 2b

<table><tr><td colspan="3">Final importance</td></tr><tr><td>Contract I</td><td>Contract II</td><td>Contract III</td></tr><tr><td>0.69</td><td>0.58</td><td>0.61</td></tr></table>

4.3.1.4. Example 4 (PWC matrix perturbation). The perturbation to the PWC matrix is especially important, because slight changes to the matrix can have a significant impact on the overall importance weights. To test how the AHP methodology performs, each element, $a _ { i j } ,$ of the baseline PWC matrix in Table 3a is perturbed to $a _ { i j } + \mathsf { P F } \times U ( 0 , 1 )$ , where $U ( 0 , 1 )$ is a uniform random number between 0 and 1, and PF is a perturbation factor that was changed as follows: 0.2, 0.3, 0.4 and 0.5. The perturbations have been kept deliberately small, because large changes to the data can be expected to produce similar changes to the results as well.

For each PF value, Table 4 gives the weights for the factors, the stocking and non-stocking weights with respect to each factor and the final stocking and non-stocking weights. Again, we see that the results do change, although not radically. .

4.3.1.5. Example 5 (rank-reversal). Rank-reversal is an issue with AHP, discussed in a number of related articles (e.g., Ref. [17]). It is a phenomenon that has been observed when a new factor, whose pairwise comparison vector is a ‘‘near-copy’’ of an existing vector, is added into the PWC matrix. With this addition, the rankings of some of the original factors get reversed. To test, we added a new factor whose PWC numbers are random variations of those for CusType. The two vectors are displayed in Table 5. The results of this change, given in the bottom part of that table, show that the stock weights change, but the rankings of the factors do not. .

## 4.3.2. Illustration of heuristic

4.3.2.1. Example 6: heuristic. Consider a budget of US\$5000 for the five contracts shown in Table 6. The contracts are shown in descending order of their importance weights. For each contract, the table gives the spare parts and their respective costs, the total cost for all the spare parts and the set of feasible stockrooms (i.e., those within the contract’s response duration, CRes). As mentioned in Section 4.2, the heuristic methodology consists of two phases:

Table 3a  
Baseline PWCs and stocking preferences for Examples 3 through 5

<table><tr><td></td><td>CusType</td><td>CusPar</td><td>CusAppType</td><td>CType</td><td>CRes</td><td>CSiz</td><td>CAge</td><td>PAge</td><td>PCri</td><td>PUnitAge</td><td>Stock Pref</td></tr><tr><td>CusType</td><td>1</td><td>2.01</td><td>2.03</td><td>7.04</td><td>7.01</td><td>7</td><td>7.07</td><td>9</td><td>9</td><td>9</td><td>0.875</td></tr><tr><td>CusPar</td><td></td><td>1</td><td>1.54</td><td>6.09</td><td>6.02</td><td>6.02</td><td>6.07</td><td>8.07</td><td>8.02</td><td>8.03</td><td>0.667</td></tr><tr><td>CusAppType</td><td></td><td></td><td>1</td><td>4.08</td><td>4.03</td><td>4.06</td><td>4.01</td><td>8.06</td><td>8.01</td><td>8.06</td><td>0.833</td></tr><tr><td>CType</td><td></td><td></td><td></td><td>1</td><td>2.51</td><td>2.58</td><td>2.56</td><td>4.04</td><td>4.08</td><td>4</td><td>0.333</td></tr><tr><td>CRes</td><td></td><td></td><td></td><td></td><td>1</td><td>2.05</td><td>2.06</td><td>3.04</td><td>3.06</td><td>3.05</td><td>0.2</td></tr><tr><td>CSiz</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1.56</td><td>2.07</td><td>2.02</td><td>2.03</td><td>0.25</td></tr><tr><td>CAge</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1.84</td><td>1.82</td><td>1.83</td><td>0.167</td></tr><tr><td>PAge</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1.33</td><td>1.32</td><td>0.80</td></tr><tr><td>PCri</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1.16</td><td>0.833</td></tr><tr><td>PUnitAge</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>0.714</td></tr></table>

 selecting a suitable stockroom based on a heuristic cost function and

 specifying the stocking decision based on the budget.

Table 7a illustrates the first phase. Contract 1 has no common parts with any of the remaining contracts, and hence, its stocking costs will be the same as the total cost of all its spare parts. Thus, all stockrooms are equally good for stocking this contract; we break this tie arbitrarily by choosing the first stockroom, as shown in the last column of Table 7a. For contract 2, there is no commonality when considering to stock for that contract in stockroom 2. However, when considering to stock for it in stockroom 3, there is a potential commonality with part 6 of contract 5. Because the importance weight is a key determinant for the stocking decision, we use it as a surrogate to measure this potentiality; that is, the pseudo-cost function is computed by the product: (savings due to commonality)  (importance weight of the contract).

Table 3b

<table><tr><td colspan="4">Final weights for factors and alternatives</td></tr><tr><td rowspan="2">Factor</td><td colspan="3">PF=0.2</td></tr><tr><td>Factor&#x27;s weight</td><td>Stock weight</td><td>Non-stock weight</td></tr><tr><td>CusType</td><td>0.309</td><td>0.270</td><td>0.039</td></tr><tr><td>CusPar</td><td>0.237</td><td>0.158</td><td>0.079</td></tr><tr><td>CusAppType</td><td>0.179</td><td>0.150</td><td>0.030</td></tr><tr><td>CType</td><td>0.078</td><td>0.026</td><td>0.052</td></tr><tr><td>CRes</td><td>0.055</td><td>0.011</td><td>0.044</td></tr><tr><td>CSiz</td><td>0.040</td><td>0.006</td><td>0.029</td></tr><tr><td>CAge</td><td>0.035</td><td>0.006</td><td>0.029</td></tr><tr><td>PAge</td><td>0.023</td><td>0.019</td><td>0.005</td></tr><tr><td>PCri</td><td>0.022</td><td>0.018</td><td>0.004</td></tr><tr><td>PUnitAge</td><td>0.021</td><td>0.015</td><td>0.006</td></tr><tr><td>Final weights</td><td></td><td>0.683</td><td>0.317</td></tr></table>

Pseudo  cost of stocking contract 2 in stockroom 3

¼ Total spare parts cost for contract 2

 Importance weight of contract 5

 Cost of part 6

$$
= 2 1 0 0 - 0. 7 \times 2 0 0 = 1 9 6 0
$$

After so computing the pseudo-cost for each feasible stockroom, we determine stockroom 3 to have the lowest pseudo-cost, and hence, assign it to contract 2. By repeating this procedure, the assigned stockroom for each of the other contracts is determined, as shown in Table 7a.

Next, we determine whether the spare parts must be stocked in the assigned stockroom. Table 7b shows the actual cost of stocking for each contract in the assigned stockroom. Contract 1 is stocked, because its stocking cost is with the budget, but contract 2’s stocking cost is over the remaining budget, and cannot therefore, be stocked. Contract 3 has no commonalities with any of the alreadystocked contracts, namely, contracts 1 and 2. This means that the cost of stocking for that contract is the same as the total spare parts cost of 1100 (row 3 of Table 6). This cost is within the remaining budget, hence, contract 3 is stocked for locally. Now, since contract 3 is already stocked, contract 4 has part 9 in common with contract 3, and this reduces the stocking cost of contract 4 by 600, thereby enabling its stocking. Observe how the computation of the pseudo-cost differs from that of the actual stocking cost. In the latter case, if there is a commonality, there is no weighting by the importance weight, and all the part costs get reduced. Finally, contract 5 does not get selected for stocking, as there is no budget left. .

![](/api/attachments/SYS2EBNU/fulltext/images/d5ffe94a8b9428696e2369c4d78bb18ebbf340e7c7b8aa3a03ad89f8180785ec.jpg)

![](/api/attachments/SYS2EBNU/fulltext/images/0467514223bffe212cf1473cb69dfae38958e2d9c353f2256d4b1231556984cd.jpg)

![](/api/attachments/SYS2EBNU/fulltext/images/b715a77059e5719858e367d5bdfbd6205cdac322327405dae6dad834b6942975.jpg)  
c. CType weight change  
Fig. 2. Sensitivity due to varying the weight of one factor.

## 5. Description of the Web system

We have created a Web-based system incorporating the model proposed in Section 4. Users who want to use the system issue a request via their Web browser. This request is then sent to the system through Microsoft’s Internet Information Server [33], which is a software program for servicing HTTP requests [11]. The logic of the system has been coded in Visual Basic (VB), a Windows-based language that is being used in many applications (see Ref. [72] for examples). VB was chosen for a number of reasons. First, it has the features of a full-fledged programming language along with the convenience of easily developing user interfaces. Second, it provides connectivity to a number of database management systems. Third, it can be compiled, and hence, would provide an execution time that is comparable to that of traditional languages such as C. Finally, it comes with a number of methods that facilitate interaction with the Web (the word method is used in the object-oriented sense).

Table 4  
Sensitivity analysis with PWC matrix perturbations

<table><tr><td rowspan="2">Factor</td><td colspan="3">PF=0.2</td><td colspan="3">PF=0.3</td><td colspan="3">PF=0.4</td><td colspan="3">PF=0.5</td></tr><tr><td>Factor&#x27;s weight</td><td>Stock weight</td><td>Non-stock weight</td><td>Factor&#x27;s weight</td><td>Stock weight</td><td>Non-stock weight</td><td>Factor&#x27;s weight</td><td>Stock weight</td><td>Non-stock weight</td><td>Factor&#x27;s weight</td><td>Stock weight</td><td>Non-stock weight</td></tr><tr><td>CusType</td><td>0.313</td><td> $0.273^a$ </td><td> $0.039^a$ </td><td>0.313</td><td>0.274</td><td>0.039</td><td>0.313</td><td>0.274</td><td>0.039</td><td>0.317</td><td>0.278</td><td>0.040</td></tr><tr><td>CusPar</td><td>0.235</td><td>0.157</td><td>0.078</td><td>0.236</td><td>0.157</td><td>0.079</td><td>0.238</td><td>0.159</td><td>0.079</td><td>0.235</td><td>0.156</td><td>0.078</td></tr><tr><td>CusAppType</td><td>0.180</td><td>0.150</td><td>0.030</td><td>0.179</td><td>0.149</td><td>0.030</td><td>0.178</td><td>0.148</td><td>0.030</td><td>0.177</td><td>0.148</td><td>0.030</td></tr><tr><td>CType</td><td>0.077</td><td>0.026</td><td>0.052</td><td>0.077</td><td>0.026</td><td>0.052</td><td>0.078</td><td>0.026</td><td>0.052</td><td>0.077</td><td>0.026</td><td>0.051</td></tr><tr><td>CRes</td><td>0.055</td><td>0.011</td><td>0.044</td><td>0.055</td><td>0.011</td><td>0.044</td><td>0.056</td><td>0.011</td><td>0.045</td><td>0.056</td><td>0.011</td><td>0.045</td></tr><tr><td>CSiz</td><td>0.040</td><td>0.006</td><td>0.029</td><td>0.040</td><td>0.010</td><td>0.030</td><td>0.040</td><td>0.010</td><td>0.030</td><td>0.039</td><td>0.010</td><td>0.029</td></tr><tr><td>CAge</td><td>0.035</td><td>0.006</td><td>0.029</td><td>0.035</td><td>0.006</td><td>0.029</td><td>0.034</td><td>0.006</td><td>0.028</td><td>0.035</td><td>0.006</td><td>0.029</td></tr><tr><td>PAge</td><td>0.023</td><td>0.019</td><td>0.005</td><td>0.023</td><td>0.019</td><td>0.005</td><td>0.022</td><td>0.018</td><td>0.004</td><td>0.023</td><td>0.018</td><td>0.005</td></tr><tr><td>PCri</td><td>0.022</td><td>0.018</td><td>0.004</td><td>0.021</td><td>0.018</td><td>0.004</td><td>0.021</td><td>0.018</td><td>0.004</td><td>0.021</td><td>0.017</td><td>0.003</td></tr><tr><td>PUnitAge</td><td>0.021</td><td>0.015</td><td>0.006</td><td>0.020</td><td>0.014</td><td>0.006</td><td>0.020</td><td>0.014</td><td>0.006</td><td>0.020</td><td>0.014</td><td>0.006</td></tr><tr><td>Final weights</td><td></td><td> $0.684^b$ </td><td> $0.316^b$ </td><td></td><td>0.684</td><td>0.316</td><td></td><td>0.683</td><td>0.317</td><td></td><td>0.684</td><td>0.316</td></tr></table>

<sup>a</sup> Stock and non-stock weights with respect to CusType.  
<sup>b</sup> Overall stock and non-stock weights (Eq. (3)).

In this section, we first describe the data model used for this prototype and then show some details of the user interface.

## 5.1. Data component

Fig. 3 shows the three types of data tables used in our system. First, there is information on various entities such as contracts, products, stockroom inventory and so on (details of these tables have been suppressed from the figure for simplicity). The second type contains a table to support different user types: planning, budgeting and sales users and users for changing preferences to evaluate contracts.

Table 5  
Inputs and outputs for rank-reversal analysis

<table><tr><td></td><td>CusType</td><td>CusPar</td><td>CusAppType</td><td>CType</td><td>CRes</td><td>CSiz</td><td>CAge</td><td>PAge</td><td>PCri</td><td>PUnitAge</td><td>RankReverF</td></tr><tr><td>RankReverF</td><td>1</td><td>2.05</td><td>2.07</td><td>7.06</td><td>7.05</td><td>7.08</td><td>7.09</td><td>9</td><td>9</td><td>9</td><td>1</td></tr><tr><td>CusType</td><td>1</td><td>2.01</td><td>2.03</td><td>7.04</td><td>7.01</td><td>7</td><td>7.07</td><td>9</td><td>9</td><td>9</td><td>1</td></tr><tr><td rowspan="2">Factor</td><td rowspan="2"></td><td rowspan="2">Factor&#x27;s weight</td><td colspan="2"> $Rank^a$ </td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td></tr><tr><td>Before</td><td>After</td></tr><tr><td>CusType</td><td></td><td>0.236</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CusPar</td><td></td><td>0.176</td><td>2</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CusAppType</td><td></td><td>0.136</td><td>3</td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CType</td><td></td><td>0.058</td><td>4</td><td>4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CRes</td><td></td><td>0.042</td><td>5</td><td>5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CSiz</td><td></td><td>0.031</td><td>6</td><td>6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CAge</td><td></td><td>0.028</td><td>7</td><td>7</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PAge</td><td></td><td>0.019</td><td>8</td><td>8</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PCri</td><td></td><td>0.018</td><td>9</td><td>9</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PUnitAge</td><td></td><td>0.017</td><td>10</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RankReverF</td><td></td><td>0.238</td><td colspan="2">Not ranked</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Overall stock weight</td><td></td><td></td><td>0.683</td><td>0.729</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Overall non-stock weight</td><td></td><td></td><td>0.317</td><td>0.271</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<sup>a</sup> Only the original set of factors are considered in the ranking.

Example data to illustrate heuristic method

<table><tr><td>Contract</td><td>Stock weights</td><td>Spare parts/ part costs (US$)</td><td>Total spare parts cost (US$)</td><td>Feasible stockrooms</td></tr><tr><td rowspan="3">1</td><td rowspan="3">0.9</td><td> $1/1200^a$ </td><td rowspan="3">3000</td><td rowspan="3">{1,2,3}</td></tr><tr><td>2/900</td></tr><tr><td>3/900</td></tr><tr><td rowspan="3">2</td><td rowspan="3">0.87</td><td>4/1200</td><td rowspan="3">2100</td><td rowspan="3">{2,3,5}</td></tr><tr><td>5/700</td></tr><tr><td>6/200</td></tr><tr><td rowspan="3">3</td><td rowspan="3">0.7</td><td>7/300</td><td rowspan="3">1100</td><td rowspan="3">{4,6,7}</td></tr><tr><td>8/200</td></tr><tr><td>9/600</td></tr><tr><td rowspan="2">4</td><td rowspan="2">0.7</td><td>9/600</td><td rowspan="2">1500</td><td rowspan="2">{6}</td></tr><tr><td>10/900</td></tr><tr><td rowspan="3">5</td><td rowspan="3">0.7</td><td>6/200</td><td rowspan="3">1000</td><td rowspan="3">{1,3,4}</td></tr><tr><td>7/300</td></tr><tr><td>11/500</td></tr></table>

<sup>a</sup> Indicates that the spare parts are {1,2,3} with costs of US\$1200, US\$900 and US\$900, respectively.

## 5.1.1. Support for evolutionary implementation

The final set of tables is included to implement different versions of the method in Section 4.1. The implementation of different versions is significant in the context of evolutionary design, a concept that has been proposed for DSSs by a number of researchers (e.g., Refs. [12,59]). Stemming, in part, from the need to provide users with an appropriate set of usable features, evolutionary design calls for the development of a small but usable system, which reflects a portion of the overall problem and which can be refined in response to users’ reactions. Such an approach is expected to improve the overall quality of the system [12,59,72]. Here, we apply this concept to the implementation phase; that is, we provide for the evolutionary (or incremental) implementation of our system. Fig. 3 shows the tables needed for handling different types of envisaged implementations. The logic of the system will read the information in these tables, and, accordingly, it will generate all the input menus and reports needed by the user. It is important to note that changes need to be made in tables only, and not to the code itself—a factor that is important from the software-maintenance perspective.

To see how these tables would work, consider, for example, the categorization of contracts. In Example 1 (Section 4.3.1), it was suggested that categorization be applied at Level 2 (see Fig. 1). If this suggestion turns out to be difficult from a business perspective, the DSS implementation can begin with a select set of contracts that are similar to one another, therefore requiring no categorization. This implies that the tables Level1Type and Level2Type must contain just one record (for one category). The data needed for such an implementation (in tables Level1Type and Level2Type and in other tables) is shown in plain text in Fig. 4. Later on, as confidence in the system builds, more contracts get inputted, due to which categorization may be required at one or both levels. This changed implementation can be effected by simply entering the italicized and shaded portions of Fig. 4, and without any changes to the software. The system will prompt the user to input the new set of preferences that are required, and then store them in tables (bolded and shaded portions of the figure).

Illustration of heuristic method

<table><tr><td colspan="5">Stockroom selection</td></tr><tr><td>Contract</td><td>Stockroom considered</td><td>Commonalities gained with that stockroom</td><td>Pseudo-cost of stocking in that stockroom $(c_{ij}^{\prime})^{\text{a}}$ </td><td>Selected stockroom</td></tr><tr><td rowspan="3">1</td><td>1</td><td>None</td><td> $c_{1,1}^{\prime}=3000$ </td><td>1</td></tr><tr><td>2</td><td>None</td><td> $c_{1,2}^{\prime}=3000$ </td><td></td></tr><tr><td>3</td><td>None</td><td> $c_{1,3}^{\prime}=3000$ </td><td></td></tr><tr><td rowspan="3">2</td><td>2</td><td>None</td><td> $c_{2,2}^{\prime}=2100$ </td><td>3</td></tr><tr><td>3</td><td>Part 6 with contract 5</td><td> $c_{2,3}^{\prime}=2100-0.7\times200=1960$ </td><td></td></tr><tr><td>5</td><td>None</td><td> $c_{2,5}^{\prime}=2100$ </td><td></td></tr><tr><td rowspan="3">3</td><td>4</td><td>Part 7 with contract 5</td><td> $c_{3,4}^{\prime}=1100-0.7\times300=890$ </td><td>6</td></tr><tr><td>6</td><td>Part 9 with contract 4</td><td> $c_{3,6}^{\prime}=1100-0.7\times600=560$ </td><td></td></tr><tr><td>7</td><td>None</td><td> $c_{3,7}^{\prime}=1100$ </td><td></td></tr><tr><td>4</td><td>6</td><td>Part 9 with contract 3</td><td> $c_{4,6}^{\prime}=1500-0.7\times600=960$ </td><td>6</td></tr><tr><td rowspan="3">5</td><td>1</td><td>None</td><td> $c_{5,1}^{\prime}=1000$ </td><td>1</td></tr><tr><td>3</td><td>None</td><td> $c_{5,3}^{\prime}=1000$ </td><td></td></tr><tr><td>4</td><td>None</td><td> $c_{5,4}^{\prime}=1000$ </td><td></td></tr></table>

<sup>a</sup> Pseudo-cost of stocking contract i in stockroom j, considering potential commonalities with contracts.

Table 7b

<table><tr><td colspan="6">Stocking decision</td></tr><tr><td>Contract</td><td>Stockroom selected</td><td>Commonalities gained with that stockroom</td><td>Cost of stocking in that stockroom  $(c_{i,j})^a$ </td><td>Stocking decision</td><td>Budget leftb</td></tr><tr><td>1</td><td>1</td><td>None</td><td> $c_{1,1}=3000$ </td><td>1</td><td>2000</td></tr><tr><td>2</td><td>3</td><td>None</td><td> $c_{2,3}=2100$ </td><td>0</td><td>2000</td></tr><tr><td>3</td><td>6</td><td>None</td><td> $c_{3,6}=1100$ </td><td>1</td><td>900</td></tr><tr><td>4</td><td>6</td><td>Part 9 with contract 3</td><td> $c_{4,6}=1500-600=900$ </td><td>1</td><td>0</td></tr><tr><td>5</td><td>1</td><td>None</td><td> $c_{5,1}=1000$ </td><td>0</td><td>0</td></tr></table>

<sup>a</sup> Cost of stocking contract i in stockroom $j ,$ considering actual commonalities with already-stocked contracts.  
<sup>b</sup> Budget left after considering the contract.

The above description presents one example of evolutionary implementation. Other such examples include changes to the set of attributes and to attribute values; again, our data model is such that these changes can be accomplished by adding or deleting entries in the corresponding tables. Section 5.2 will discuss the dialog mechanisms provided by the system.

## 5.2. User interface component

A key input screen is shown in the top part of Fig. 5. Planners can add or delete contracts as well as change

![](/api/attachments/SYS2EBNU/fulltext/images/b484381b1830c357aed4cefd4e6922f0a6e865c9929d94f5dbce11ced4b27d07.jpg)  
Fig. 3. Partial data model for the system.

<table><tr><td>Level1Type</td><td colspan="2">AttributeList</td><td colspan="2">Level1Type</td><td>Level2Type</td></tr><tr><td>Type1</td><td colspan="2">Attribute</td><td>Attribute</td><td>Value</td><td>Type2</td></tr><tr><td>A</td><td colspan="2">CSiz</td><td>CSiz</td><td>Large</td><td>A</td></tr><tr><td>B</td><td colspan="2">CusType</td><td>CSiz</td><td>Medium</td><td>B</td></tr><tr><td></td><td colspan="2">CAge</td><td>CSiz</td><td>Small</td><td></td></tr><tr><td></td><td colspan="2"></td><td>CusType</td><td>Critical</td><td></td></tr><tr><td></td><td colspan="2"></td><td>etc.</td><td></td><td></td></tr></table>

Fig. 4. Illustration of support for evolutionary implementation.

PWCs by clicking on the utilities button. In addition, as shown in the figure, they can operate the system in one of two-planning modes, known as NetChange and MassUpdate. In the NetChange mode, only contracts that are input during the current run are considered. Decisions that have been made prior to the run (i.e., stocking decisions of contracts that were input during a previous run) are taken to remain the same. Then, the decisions on the new contracts are made using the proposed methodology. In the MassUpdate mode, all contracts are considered during the run.

In either mode, the recommended stocking profile then appears, as shown in the bottom part of the Fig. 5. As shown in the figure, an individual planner can simply accept the system’s recommendation (by clicking Save). Alternatively, if the recommendations are not acceptable, the planner can conduct ‘‘what-if’’ analyses by changing stockroom assignments and stocking decisions. The planner can also change the date in the textbox, NextReview, which specifies the minimum date by which the contract can be reviewed by a run of the MassUpdate planning mode. The system also provides a button named drill that can be used to drilldown. What-if analyses and drill-downs are recommended features of decision support systems [43], and as shown in the figure, clicking on this button yields additional information to the planner—the importance of the contract and the additional parts needed to stock for the contract. This would give planners with useful information to better hone-in their what-if analyses.

In addition to the above planning uses, as shown in Fig. 5, managers would be able to conduct what-if analyses between the budget and the number of supported contracts, and sales people would be able to see the incremental budgetary impact of adding/deleting a contract.

![](/api/attachments/SYS2EBNU/fulltext/images/f8f1fd6f31683b2e749fed3014baac1d313549dbbf176a9ef76a349a1fd1e834.jpg)  
Fig. 5. Key input and output screens of system.

## 6. Case study revisited: impact of Web-based system

In this section, we evaluate the impact of the system on the company (Alpha) introduced in Section 3. We first discuss computing impacts and then the managerial implications.

## 6.1. Computing impact

Ten years ago Alpha did not have an integrated planning system. Individual stockrooms had their own system for collecting consumption data, which was then fed into a planning system for calculating the stocking amounts. Both these systems were homegrown legacy systems.

As failure rates decreased with process and quality improvements, however, demands became low and, therefore, they could not be handled by the individual stockroom-planning system. Further, there were other pressures on Alpha to implement an ERP (enterprise resource planning) system. This led to two changes. First, consumption data were all collected into an ERP system and fed into a forecasting package known as LPA. LPA used this consumption data, and aggregated the consumption data, to compute the stocking levels at the central warehouse and at the individual stockrooms. LPA did not consider service contracts and the intangible issues involved in their management. Instead, all of its recommen-

Shaded portions indicate computing implications dations were based on consumption data of the individual service part, without relating to whether the parts were associated with any contract. The recommendations were then fed to the planner’s stockroom system, as shown in Fig. 6 (top half). Then, planners considered the contracts that need to be supported and manually made adjustments to the stocking levels as needed. Clearly, this process is time consuming to the planner, in addition to being inconsistent across time periods and across multiple geographical regions.

The Web-based system allows all planners to manage their contracts by using a single system. Planners use this system to enter contracts and to review stocking recommendation sent from LPA, as shown in Fig. 6 (bottom half). Using the logic given in this paper, the system aggregates LPA’s profiles along with the requirements to support contracts and then automatically feeds the resultant information into the local stockroom system. As before, the local stockroom system sends the planning information to the ERP system.

![](/api/attachments/SYS2EBNU/fulltext/images/444f4c286d28948bfa22799a580b0848e1b545ecf6d9f00833c99f7baa46d318.jpg)  
Fig. 6. Computing implications of contract management system.

The organizational impact of this approach is discussed next.

## 6.2. Managerial implications

In this section, we show how the system has implications throughout the organization, and thus, possesses some characteristics of an ODSS. ODSSs have three main characteristics [9,24,27,30,41,67]. First, they focus on an organizational task or decision that affects several organizational units. Second, an ODSS cuts across organizational boundaries. Third, ODSS may involve communication technologies. Although the concept of an ODSS has been introduced over two decades ago, few ODSSs have been created to date (some examples are given in Refs. [40,61]). For example, in their recent paper, Sen et al. [61] remark that the system presented in their paper ‘‘represents one of the few documented examples of ODSSs.’’

We present the implications of the system from three perspectives.

## 6.2.1. Supporting geographically dispersed planners

Currently, the planning function at Alpha is very tedious. Planning is done manually and on a contractby-contract basis; that is, as and when a contract arrives and without considering other contracts. There is therefore little possibility to optimize inventory across contracts. Planners are also not aware of the full dollar impact of supporting a contract. Moreover, even if a particular planner were to evaluate a contract by considering other contracts, the process of having to re-think the logic of the evaluation is time consuming and could be inconsistent from time to time. Finally, the planning process of one person may be totally different from that of another. All of these issues run counter to the business climate in which companies are implementing uniform business processes globally.

Our DSS can greatly ease the time consuming process of evaluating contracts. The evaluation itself can be standardized from one time period to another and from one planner to another. The system can examine possible commonalities of service parts and make a recommendation that economizes the cost of stocking for a contract. Further, rather than being totally prescriptive, our DSS provides a way for planners to experiment with alternate solutions based on their experience. Research has shown that an inflated reliance on a DSS can lead to lower quality decisions, stemming, in part, from the decision maker ignoring other sources of information or other solution alternatives to the problem [13,43]. With this phenomenon in mind, we have allowed planners to change the system-recommended stockroom assignment and stocking decision and have the system evaluate the cost effect of their changes (what-if button of Fig. 5). They can then click on the SystemReco button to get back the system’s recommendations. To help explain the cost effects, we have provided the Drill button that gives a synopsis of key information, including the additional service parts needed to stock for the contract and the total cost of those parts.

## 6.2.2. Supporting managers

Regional managers at Alpha currently set budgets with purely corporate goals in mind. The details of contracts that need to be supported are not fully considered in the decision process, nor are commonalities among contracts exploited to trim budgets. Commonalities are hard to observe using a manual process, especially for managerial-level users who may not be intimately be aware of the day-to-day events. Our system first provides decision support for this budgetary process. With a system to allocate budgets efficiently, a manager can more accurately see the relationship between the budget and the percentage of contracts supported. Managers can also perform what-if analyses by changing the budget levels up or down (Fig. 5). The system will evaluate the level of support afforded by the new budget. All of these types of information can then be used to balance corporate mandates with field-level realities. Another useful implication for the manager is the ability of the system to factor in organizational preferences into day-to-day decision-making activities (e.g., importance of Cus-Type as illustrated by Example 2). While other forms of (written or oral) communication can be used to infuse such priorities into the decision process, such methods may be very time consuming and difficult to implement.

## 6.2.3. Supporting contract-sales personnel

Finally, the third implication of the system is in the pricing of contracts. The logic of contract pricing must consider not only the size of the contract, but also the

actual dollar amount needed to support the contract. For example, a product that is core to a company and that is on a number of contracts is likely to have service parts stocked for it; therefore, the incremental cost of supporting an additional contract for the product may not be high. Without the system, sales people at Alpha do not know such information and do not factor it into their decisions. This gap can be filled by using the system.

These implications are summarized in Fig. 7. The unshaded portions therein indicate how decisions are currently made at Alpha, while the shaded portions provide the effects of system. We note from the figure that the system can offer support for a wide range of activities (from planning to managerial), as well as for a range of geographic locations and functional areas. We therefore conclude that it has characteristics of an ODSS.

![](/api/attachments/SYS2EBNU/fulltext/images/8c288fee77233b0b56fd9e3425dc7707dd5f3c4be2fae19ca6e17eebc439a1f0.jpg)  
Fig. 7. Managerial implications of the DSS.

## 7. Conclusions

In today’s business environment, it has become a norm to sell warranty contracts along with product sales. In this paper, we have seen how the inventory planning of the service parts to support such contracts has to contend with a number of difficulties that call for the evaluation of both tangible and intangible factors. This evaluation, which is inherently subjective in nature, is further compounded by the wide geographic distribution of contracts with their own unique characteristics and by the commonality of inter-contract service parts. Our paper has shown how the emerging Web technology, with its wide reach, can be used to standardize the evaluation of these varied factors within a budget. A heuristic approach and the Analytical Hierarchy Process method, which has not been applied to an inventory planning situation, are built into the model component of our DSS.

Overall, the contributions of our work are as follows. First, we have shown how the Web can be used to make changes in the planning process; recent research suggests that such a use of the Web is limited. Second, from a modeling perspective, inventory problems have generally been addressed in the research literature by some form of statistical technique to model uncertainties in demands. This paper has introduced an important real-world case that requires the consideration of subjective factors in inventory planning. Third, we have shown how our system can have organizational support characteristics.

The system has a few limitations. First, since the underlying methodology uses AHP, it is possible for the user to encounter rank-reversal when the number of factors is increased indefinitely. Although an argument can be made in favor of rank-reversal by appealing to its existence in the well-accepted methodology of linear programming $[ 5 7 , \mathsf { p } , 2 6 4 ]$ , it is not clear whether all users would be comfortable with the rank-reversal phenomenon. Second, the system would not suitable for situations in which a planner wants to keep independent control of contract management. Further, even if the goal of standardization is agreed to in principle, the process of arriving at standardized preference numbers can be time consuming. Finally, this exercise would have to be undertaken periodically, in order to ensure that the system reflects the latest organizational policies.

We conclude the paper with a discussion of some possible directions for future research. First, we must conduct simulations to test the sensitivity of the AHP solutions to changes in input data. Second, commonality is a key factor that can be exploited to reduce inventory costs. The heuristic must be evaluated to see how effectively it reduces costs. Alternatively, an optimization approach can be devised to take advantage of commonality. Third, although the demands are generally low, there appears to be some differences in their levels. It would be useful to perform an analysis (e.g., cluster analysis) to discern the patterns, if any, among the demands, and then to exploit those patterns in the development of a better solution algorithm.

## References

[1] A. Almeida, Multicriteria decision making on maintenance: spares and contracts planning, European Journal of Operational Research 129 (2001) 235– 241.

[2] S. Andaleeb, A. Basu, Do warranties influence perceptions of service quality, Journal of Retailing and Customer Services 5 (2) (1998) 87 – 91.

[3] R. Anderson, D. Granbois, D. Rosen, The effects of consumership on financial satisfaction: are good customers more satisfies? Developments in Marketing Science XVII (1994) 427– 431.

[4] Anonymous, IFR wins BT service contract, Test and Measurement Europe 8 (2) (2000, April) 4.

[5] R. Banker, G. Davis, S. Slaughter, Software development practices, software complexity and software maintenance performance: a field study, Management Science 44 (4) (1998) 433 – 450.

[6] R. Beatty, J. Shim, M. Jones, Factors influencing corporate web site adoption: a time-based assessment, Information and Management 38 (6) (2001) 337– 354.

[7] D. Bowen, B. Schneider, Services marketing and management: implications for organizational behavior, in: B. Stow, L. Cummings (Eds.), Research in Organizational Behavior, vol. 10, JAI Press, Greenwich, CT, 1988, pp. 43 – 80.

[8] E. Braude, Software Engineering, Wiley, New York, 2001.

[9] T. Bui, M. Jarke, Communications requirements for group decision support systems, Journal of Management Information Systems 2 (4) (1986) 8 – 10.

[10] M. Cohen, P. Kleindorfer, H. Lee, D. Pyke, Multi-item con-

strained (s,S) policies for spare parts logistics systems, Naval Research Logistics 39 (1992) 561– 577.

[11] D. Comer, Computer Networks and Internets, 3rd ed., Prentice-Hall, Upper Saddle River, NJ, 2001.

[12] J.C. Courban, M. Bourgeois, The information systems designer as a nurturing agent of a socio-technical process, in: H. Lucas, et al. (Eds.), Information Systems Environment, North-Holland, New York, 1980, pp. 139 – 168.

[13] F.D. Davis, J.E. Kottemann, User perception of decision support effectiveness: two production planning experiments, Decision Sciences 25 (1) (1994) 57 – 78.

[14] R. Dekker, M. Kleijn, P. de Rooji, A spare parts stocking policy based on equipment criticality, International Journal of Production Economics 56/57 (1998) 69– 77.

[15] S. Dutta, A. Segev, Business transformation on the Internet, European Management Journal 17 (5) (1999) 446.

[16] S. Dutta, S. Kwan, A. Segev, Business transformation in electronic commerce: a study of sectoral and regional trends, Re search Report 98-WP-1029, University of California, Berkeley, CA, 1998.

[17] J. Dyer, Remarks on the analytic hierarchy process, Management Science 36 (3) (1990) 249– 258.

[18] R.F. Easley, J.S. Valacich, M.A. Venkataramanan, Capturing group preferences in a multicriteria decision, European Journal of Operational Research 125 (2000) 75– 83.

[19] J. Efstathiou, A. Calinescu, G. Blackburn, A web-based expert system to assess the complexity of manufacturing in organizations, Robotics and Computer Integrated Manufacturing 18 (2002) 305– 311.

[20] M. Emmelhainz, C. Kovan, Using information as a basis for segmentation and relationship marketing: a longitudinal case study of a leading financial services firm, Journal of Market Focused Management 4 (1999) 161–177.

[21] C.T. Ennew, M.R. Binks, Impact of participative service relationships on quality, satisfaction, and retention: an exploratory study, Journal of Business Research 46 (1999) 121– 132.

[22] E. Forman, S. Gass, The analytic hierarchy process—an exposition, Operations Research 49 (4) (2001) 469 – 486.

[23] P. Gajpal, L. Ganesh, C. Rajendran, Criticality analysis of spare parts using the analytical hierarchy process, International Journal of Production Economics 35 (1994) 293 – 298.

[24] J.F. George, The conceptualization and development of organizational decision support systems, Journal of Management Information Systems 8 (4) (1992) 5 – 22.

[25] C. Groonroos, Service Management and Marketing, Lexing ton Books, Lexington, MA, 1990.

[26] M. Guzzo, Trilogic receives five-year \$8 million government service contract, Pittsburgh Business Times 18 (26) (1999) 7.

[27] R.D. Hackathorn, P.G.W. Keen, Organizational strategies for personal computing in decision support systems, MIS Quarterly 5 (3) (1981) 21–27.

[28] B. Hennestad, Infusing the organization with customer knowledge, Scandinavian Journal of Management 15 (1999) 17–41.

[29] C. Hope, A. Muhlemann, Service Operations Management, Prentice-Hall, Englewood Cliffs, NJ, 1997.

[30] G.P. Huber, The nature of organizational decision making and

the design of decision support systems, MIS Quarterly 5 (2) (1981) 1 – 10.

[31] J. Huiskonen, Maintenance spare parts logistics: special characteristics and strategic choices, International Journal of Production Economics 71 (2001) 125– 133.

[32] G. Hult, D. Ketchen, T. Reus, Organizational learning capacity and internal customer orientation within strategic sourcing units, Journal of Quality Management 6 (2001) 173 – 192.

[33] A. Jones, Visual Basic Developer’s Guide to ASP and IIS, Sybex Press, San Francisco, CA, 1999.

[34] P. Jonsson, Toward a holistic understanding of disruptions in Operations Management, Journal of Operations Management 18 (2000) 701– 718.

[35] S. Kanungo, S. Sharma, P.K. Jain, Evaluation of a decision support system for credit management decisions, Decision Support Systems 30 (2001) 419– 436.

[36] U. Karmarkar, R. Pitbladdo, Service markets and competition, Journal of Operations Management 12 (1995) 397–411.

[37] D. Kellogg, W. Nie, A future of strategic service management, Journal of Operations Management 13 (1995) 323–337.

[38] W. Kennedy, W. Patterson, L. Fredenhall, An overview of recent literature on spare parts inventories, International Journal of Production Economics 76 (2002) 201 – 215.

[39] P. Keskinocak, R. Goodwin, F. Wu, R. Akkiraju, S. Murthy, Decision support for managing an electronic supply chain, Electronic Commerce Research 1 (2001) 15 – 31.

[40] Y. Kim, H. Kim, J. Yoon, H. Ryu, Building an organizational decision support system for Korea Telecom: a process redesign approach, Decision Support Systems 19 (1997) 255–269.

[41] J.L. King, S.L. Star, Conceptual foundations for the development of organizational support systems, Proceedings of the Twenty-Third Annual Hawaii International Conference on Systems Sciences, IEEE Computer Press, Los Alamitos, CA, 1990, pp. 143 – 151.

[42] S. Knox, Loyalty-based segmentation and customer development process, European Management Journal 16 (6) (1998) 729–737.

[43] J.E. Kottemann, F.D. Davis, W.E. Remus, Computer assisted decision making: performance, beliefs and the illusion of control, Organizational Behavior and Human Decision Processes 57 (1) (1994) 26–37.

[44] O. Ljumgberg, Management of OEE as a basis of TPM activities, International Journal of Operations and Production Management 18 (5) (1998) 495– 507.

[45] G. Lynn, S. Lipp, Al. Akgun, A. Cortez, Factors influencing the adoption and effectiveness of the world wide web in marketing, Industrial Marketing Management 31 (2002) 35 – 49.

[46] Q. Ma, M. Tseng, B. Yen, A generic model and design representation technique of service products, Technovation 22 (2002) 15– 39.

[47] J. Madden, L. Dicarlo, Dell, IBM cut new deal, PC Week (1999, October) 12.

[48] J. Narver, S. Slater, B. Tietje, Creating a market orientation, Journal of Market Focused Management 2 (1998) 241 – 255.

[49] W. Nie, Waiting: social and psychological perspectives in operations management, OMEGA 28 (2000) 611 – 629.

[50] G.C. O’Connor, B. O’Keefe, Viewing the Web as a marketplace: the case of small companies, Decision Support Systems 21 (1997) 171– 183.

[51] D. Petrovic, R. Petrovic, SPARTA II: further development in an expert system for advising on stocks of spare parts, International Journal of Production Economics 24 (1992) 291– 330.

[52] B. Pine, D. Peppers, M. Rogers, Do you want to keep your customers forever? Harvard Business Review (1995, March – April) 103– 114.

[53] L. Pintelon, L. Gelders, Maintenance management decision making, European Journal of Operational Research 58 (1992) 301– 317.

[54] A. Raouf, M. Ben-Daya, Total maintenance management: a systematic approach, Journal of Quality Management 1 (1) (1995) 6 – 14.

[55] W. Rustenberg, G. van Houtum, W. Zijm, Spare parts management at complex technology-based organizations: an agenda for research, International Journal of Production Economics 71 (2001) 177– 193.

[56] T. Saaty, The Analytical Hierarchy Process, McGraw-Hill, New York, 1980.

[57] T. Saaty, An exposition of the AHP in Reply to the paper ‘Remarks on the Analytic Hierarchy Process’, Management Science 36 (3) (1990) 259–268.

[58] B. Sadowski, C. Maitland, J. van Dongen, Strategic use of the Internet by small- and medium-sized companies: an exploratory study, Information Economics and Policy 14 (2002) 75– 93.

[59] V.L. Sauter, J.L. Schofer, Evolutionary development of decision support systems: important issues for early phases of design, Journal of Management Information Systems 4 (4) (1988) 77– 82.

[60] B. Schweber, Who said anything about spare parts? EDN 43 (3) (1998) 31.

[61] T. Sen, L. Moore, T. Hess, An organizational decision support system for managing the DOE hazardous waste cleanup program, Decision Support Systems 29 (2000) 89 – 109.

[62] C. Sherbrook, Optimal Inventory Modeling of Systems, Wiley, New York, 1992.

[63] D. Sherwin, P. Jonsson, TQM, maintenance and plant availability, Journal of Quality in Management 1 (1) (1995) 15 – 19.

[64] R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[65] R. Sprague, H. Watson, Decision Support for Management, Prentice-Hall, Upper Saddle River, NJ, 1996.

[66] P. Suomala, M. Sievanen, J. Paranko, The effects of customization on spare part business: a case study in the metal industry, International Journal of Production Economics 79 (2002) 57 – 66.

[67] E.B. Swanson, R. Zmud, Distributed decision support systems: a perspective, Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences, vol. III, IEEE Computer Press, Los Alamitos, CA, 1990, pp. 129– 136.

[68] R.H. Teunter, L. Fortuin, End-of-life service: a case study, European Journal of Operational Research 107 (1998) 19– 34.

[69] R.H. Teunter, L. Fortuin, End-of-life service, International Journal of Production Economics 59 (1999) 487 – 497.

[70] P. Todd, I. Benbasat, An experimental investigation of the relationship between decision makers, decision aids and decision making efforts, Infor 31 (2) (1993) 80 – 100.

[71] E. Triantaphyllou, A. Sanchez, A sensitivity analysis approach for some deterministic multicriteria decision making methods, Decision Sciences 28 (1) (1994) 151 – 194.

[72] E. Turban, J. Aronson, Decision Support Systems and Intelligent Systems, Prentice-Hall, Upper Saddle River, NJ, 1998.

[73] H. Wang, A survey of maintenance policies of deteriorating systems, European Journal of Operational Research 139 (2002) 469– 489.

[74] R. Yam, P. Tse, L. Li, P. Tu, Intelligent predictive decision support system for condition-based maintenance, International Journal of Advanced Manufacturing Technology 17 (2001) 383– 391.

[75] B. Yen, Electronic commerce front-end in apparel supply chain, Computers and Industrial Engineering 42 (2002) 471 – 480.

[76] V. Zeithaml, L. Berry, A. Parasuraman, Communications and control processes in the delivery of service quality, Journal of Marketing (1988, April), 35–58.

[77] M. Zuo, B. Liu, D. Murthy, Replacement repair for multistate deteriorating products under warranty, European Journal of Operational Research 123 (2000) 519– 530.

R.P. Sundarraj is an Associate Professor of Information Systems at the University of Waterloo. He obtained his Bachelor in Electrical Engineering from the University of Madras, India, and his MS and PhD in Management Science from the University of Tennessee, Knoxville, in 1988 and 1990, respectively. Professor Sundarraj’s research encompasses the development of methodologies for the efficient design and management of emerging information systems, as well as the use of massively parallel computing for solving largescale problems. His research has been published in many journals such as ACM Transactions, IEEE Transactions, Mathematical Programming, European Journal of Operational Research and International Journal of Production Economics. In addition, Professor Sundarraj has consulted with Fortune 100 companies on the development of decision support and Web-based systems for materials and marketing management.
