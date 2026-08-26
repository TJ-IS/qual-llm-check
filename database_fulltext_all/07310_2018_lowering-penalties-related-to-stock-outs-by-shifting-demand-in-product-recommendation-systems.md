---
otero_id: 7310
otero_key: "85JKHBBU"
title: "Lowering penalties related to stock-outs by shifting demand in product recommendation systems"
authors: "C. Dadouchi; B. Agard"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.08.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
<table><tr><td>PII:</td><td>S0167-9236(18)30125-8</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.08.004</td></tr><tr><td>Reference:</td><td>DECSUP 12978</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>26 March 2018</td></tr><tr><td>Revised date:</td><td>26 June 2018</td></tr><tr><td>Accepted date:</td><td>4 August 2018</td></tr></table>

## Accepted Manuscript

Lowering penalties related to stock-outs by shifting demand in product recommendation systems

C. Dadouchi, B. Agard

![](/api/attachments/85JKHBBU/fulltext/images/45e0677159bb2ce496ff1fd21fd2bb697f445e593eb11ab80cb23e0e8050690f.jpg)

Please cite this article as: C. Dadouchi, B. Agard , Lowering penalties related to stockouts by shifting demand in product recommendation systems. Decsup (2018), doi:10.1016/ j.dss.2018.08.004

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Lowering penalties related to stock-outs by shifting demand in product recommendation systems

C. DADOUCHI<sup>a,b</sup>, B. AGARD<sup>a,c</sup>,

<sup>a</sup>Laboratoire en Intelligence des Donn´ees, CIRRELT D´epartement de Math´ematiques et G´enie Industriel <sup>b</sup>e-mail: camelia.dadouchi@polymtl.ca <sup>c</sup>e-mail: bruno.agard@polymtl.ca

## Abstract

Recommender systems focus on the various algorithms and techniques to get the most accurate prediction of users’ preferences. We propose a method designed to consider actual stock levels in the recommendation process in order to shift demand toward specific products for a specific user. The method is displayed in two phases; the first is a categorization of customers, and in the second, item scores are corrected to take into account customer categorization and a company’s strategy in stock allocation. Low inventory products will be recommended only to high lifetime value customers, and high inventory products will be recommended more often to all users. Based on a real situation from an industrial partner in a B2B context, experiments were conducted on simulated data representing recommender systems’ scores modeled over data. Results indicate that penalties resulting from the recommendation of stock-out products are lowered.

Keywords:

Recommender systems, inventory management, ranking, demand shifting,

## 1. Introduction

The information revolution led to a massive adoption of the web as a trading platform. Traditional tools of gaining and retaining customers have evolved to meet new challenges. Recommender systems (RS) are among the tools used for managing customer relationships [13] .

The definition of RSs difers from one area to another, but is focused on establishing a list of items to recommend to a specific user [7], based on algorithms from diferent disciplines that can predict a user’s interest level in a list of products [32] and suggests, among a wide range of items, those that can meet their specific needs.

In the past three decades, research on RSs focused on the various algorithms and techniques to process data in the most eficient way (memory consumption and speed of computation), in order to obtain the most accurate prediction of a users’ preferences [6, 5]. To the best of our knowledge, there has, as of now, been no RS that considers supply chain constraints and strategies. Nevertheless, previous studies have uncovered several notable findings on the impact of recommender systems on sales, confirming that recommender systems positively afect sales [27, 30].

Current RSs emphasize supply chain management problems by suggesting items that may be out of stock, or close to being out of stock. This results in long-term consequences such as negative word-of-mouth, loss of patronage, customer dissatisfaction and loss of market share [16, 41]. Research in the field of inventory management is consistent and many tools have been successfully implemented to a certain extent, but none is the ultimate solution to stock management [39].

Existing RSs focus on customers’ interests by helping the customer to decide, compare, discover and explore the products by ofering the “right product”, to the “right customer” and increase sales [29]. Furthermore, supply chain constraints are not taken into consideration to improve recommendations from a business point of view.

We propose a methodology that takes into account some supply chain constraints in RSs. We consider stock levels to diminish the occurrence of inventory management issues (out of stock/overstock) by prioritizing customers, based on their value. The contribution of this research is not in the development of a new theory, but in the proposal of a new conceptual framework that brings RSs into supply chain and inventory management.

The remainder of this article is structured as follows: Section 2 describes RS foundations including definitions, objectives, techniques and challenges. The current situation of stock management and demand-shaping is also depicted, followed by a brief synthesis. Section 3 describes the proposed method in 2 phases: (1) customer categorization and (2) product recommendation correction. Section 4 elaborates upon a case study that evaluates improvements resulting from the proposed methodology. Section 5 presents experimental results on the penalties related to stock-outs. The concluding section summarizes the purpose of considering stocks in RSs and indicates new areas to focus on in the near future.

## 2. State of the art

## 2.1. Recommender System

Diferent definitions of RSs exist, but all agree that recommender systems are tools developed in order to assist users [5, 12]. In [7], the authors consider that the diferent definitions agree on two distinctive features:

• A recommender system is personalized. The recommendations it produces are meant to optimize the experience of one user, not to represent group consensus for all.

• A recommender system is intended to help the user select among discrete options. Generally, the items are already known in advance and not generated in a bespoke fashion.

The definitions of RSs focus on establishing a list of items (object / service / good / etc.) to recommend to users. RSs predict a user’s appreciation for a list of unknown products and suggest a wide range of items that will meet their specific needs. The user is the center of the system.

RSs are used in several disciplines, such as government, business, commerce, learning, tourism, e-resource services and group activities [28].

In addition to the two former points, other objectives can be identified: recommender systems may also help to increase cross selling and to improve consumer loyalty [28, 34, 31]. [29] noted the four main functions below: (1) Help to Decide (predicting a rating for a user for an item), (2) Help to Compare (rank a list of items in a personalized way for a user), (3) Help to Discover (provide a user with unknown items that would appreciate) and (4) Help to Explore (provide items similar to a given target item)

To meet those functionalities, three types of recommender systems are identified [1]: (1) Content-based recommendations/filtering recommend items similar to those that the user preferred in the past; (2) Collaborative recommendations/ filtering recommend items that people with similar tastes and preferences have appreciated in the past; and (3) Hybrid approaches/filtering combine the two previous ones.

[38] makes a classification based on the methods of recommendation: (1) memory-based collaborative filtering (CF) techniques: each user is part of a group of people with similar interests and by identifying the “neighbors” of the active user, a prediction for a preference over new items can be produced; (2) model-based CF techniques: models learn to recognize patterns in previous sales and then make predictions for new data; and (3) Hybrid CF techniques: combine CF recommendations with other recommendation techniques such as content-based recommendations.

These typologies have been the basis of other classifications [8]. An enhanced and more recent classification, including recently-developed advanced methods such as fussy set-based, social network-based, trust-based, context awareness-based and group recommendation approaches, is proposed by [28]. For all of the techniques presented, two types of data can be used: Explicit data, such as user-provided item evaluations (these are generally continuous or ordered data) or Implicit data such as data collected from a user’s historical profile (these are often binary data, for example the history of the purchases of a user).

[2] provides a comparison of recommender systems by summarizing their advantages and disadvantages. Recommendation methods perform the best on explicit (continuous) data, and are not efective on implicit (discrete) data. In B2B, explicit information may not be accessible and available data consists mostly of historical purchases [17].

Currently, recommendation systems are not geared to respond to industrial problems, but rather to commercial interests such as increased sales. The latter is reached by attempting to predict which products each user will be more likely to buy. Some studies have focused on the interests of users according to price by product categories [20] and others on the profits generated by the seller [9]. Supply chain constraints remain poorly covered in actual RSs, according to our research.

## 2.2. Inventory Management

According to [19]. retailers worldwide lose \$1.75 trillion annually due to the cost of overstock, out of stock items, and sales returns. Stock problems are not a new issue and researchers have been working on this challenge for decades.

Inventory management is a crucial part of a company’s performance. Product demand variability can be identified as one of the key sources of uncertainty in any supply chain. Failure to account for significant product demand fluctuations may lead to poor inventory management that afects diferent aspects of the supply chain [39].

In addition, this does not only involve production constraints but also capital management. Dealing with stocks is a delicate task and despite the advances in supply chain management and increased investments in inventorytracking systems, stock outs have been an endemic problem in retail [11]. This is especially true as the web has become one of the main channels of distribution, increasing the long-term consequences of mismanagement from missed sales: store, item or brand switch [35] eventually leading to the loss of market share, customer dissatisfaction, loss of patronage, and negative word-of-mouth [16, 41].

Most grocery shoppers perceive stock outs to be an irritating situation, and evidence suggests that the impact of out-of-stock (OOS) items is enduring and influences future profits [23]. Dealing with stock is still a persistent industrial problem to solve on as many grounds as possible. In the area of production, two main strategies can be used to manage uncertainty: gradually building inventory to hedge against possible future shortages or temporarily increasing capacity by purchasing extra capacity [10]. An additional way to deal with this is to predict customers’ interests and redirect those interests into products that will help manage inventory. Recommender systems can therefore be used in such a way to influence demand for a product and limit the costs of mismanagement of stocks. This is the topic of this article.

The use of an online channel allows an organization to reach a larger customer base; it also amplifies demand variance and operational risk. Matching supply and demand becomes then even more demanding [40] and managing the unforeseen becomes of great value. An important technique to respond to this, is demand shifting (steering); this refers to the ability to promote a substitute for a product when it is OOS, and/or move a sale and marketing tactic from one period to another to accommodate supply constraints. It can do so (1) at the point of sales, by influencing a customer to purchase an alternative product using sales and marketing incentives; or (2) at the point of supply, when the operations planning and manufacturing teams negotiate to shift unconstrained demand into the future due to supply capacity constraints [40].

One of the most famous business best practices of demand shifting in a web based context is the demand shaping done by Dell [25]. Dell “consigns” inventories of components at supplier warehouses. If they uncover components that have excessive inventories, the team would alter the daily list of specially promoted items to include computer configurations that includ these components. In contrast, if they uncover components that had inventory shortages, the team would “de-promote” them. This means taking them of the daily list of specially promoted items, raising their prices, and increasing their delivery lead times [24].

## 3. The proposed method

As presented, RSs, in their structure, do not consider inventory levels. Thus, we suggest an approach to help consider this constraint based on a 2-phase approach to (1) categorize each user, and (2) correct SRs outputs based on the user’s categorization and on the company’s strategy.

## 3.1. Phase 1: Categorization of users

Customer satisfaction leads to customer retention. Making a sale with a new customer is estimated to be up to 5 times more dificult than making an additional sale to an existing customer [21]. Thus, customer defections are among the worst economic events that can happen to a business, and keeping customers with the highest customer value is a business priority.

Categorization of users can be quantitative using metrics such as customer value or qualitative based on a company’s strategy. We propose using a classification to set diferent classes of customers in order to adapt recommendations for priorities. The classification is based on Customer Lifetime Value (CLV), except when legal or ethical constraints are noted, in which case, customer class can be forced to any required specific category. Customers identified as CAT 1 will be high CLV customers or customers with binding contracts and ethical priority. Customers in CAT 2 will be the rest of the customers. It is possible to make sub-distinctions in those (ex: between customers making multiple purchases of low profit items and those making very few purchases).

CLV over a period of time is calculated with formula 1 from [4].

$$
C L V = G C * \sum_ {i = 0} ^ {p. n} \frac {r ^ {i}}{(1 + d) ^ {\frac {i}{p}}} - M * \sum_ {i = 1} ^ {p. n} \frac {r ^ {i - 1}}{(1 + d) ^ {\frac {i + 0 . 5}{p}}}\tag{1}
$$

For i in 0 to $p ,$ representing a period,

GC is the (expected) gross contribution margin per customer per sales cycle,

M is the promotion costs per customer per sales cycle,

r is the retention rate per sales cycle,

n is the length, in years, of the period over which cash flows are to be projected,

d is the yearly discount rate (appropriate for marketing investments),

$p$ is the number of periods (it is not necessary that p to be as an integer).

## 3.2. Phase 2: Correct recommendations

Customer categorization helps determine which customers will have priority when it comes to inventory management. Recommendations do not always result in a purchase, but recommendations highlight items that are predicted to be of interest to a user. Highlighting an item that is low inventory to a low CLV user may go against the company’s interests. When recommending items without considering stock level, as is the case for actual RSs, a user with a low CLV may be recommended with an item soon to be OOS, but this item may be highly critical for another user with high CLV. Hence, since the recommendation is in real time, if the low CLV user buys the item, then the user with a high CLV could be the one facing the OOS situation. This could be partly avoided by redirecting interest of low CLV user to another item.

In order to correct recommendations based on stock levels it is important to use accurate, up-to-date information. Nowadays, many Advanced Planning Systems allow full visibility of the supply chain and assist in the coordination and decision making in the supply chain [36]. Multiple inventory counting systems can be implemented to monitor current levels of each item keeping track of all removals and replenishments from inventory [37]. For the purpose of this paper we consider the data that monitor current levels of each item. Advanced planning systems usually include modules that allow safety stocks and the exected demand per item to be calculated. Safety stocks along a supply chain have been described by [18] as the minimum level of stock to absorb demand uncertainties and to avoid lost sales and backorders. Because of the diferent replenishment cycles, the demand can be met without losing the sale or having backorders, if a replenishment is expected in the time window in which the retailers can secure the sale. In this case, the items with low inventory that expect a replenishment are considered in the normal range of stock levels, and taken into account in Step 7. Also, expected stock levels can be defined as the remaining stock calculated based on the expected demand. Expected demand is a forecast of demand on a period of time. Those two quantities define the range in which the stock level is expected to be. Reaching the safety stock level implies risks for inventory management; likewise, a stock level that is higher than the “expected stock” may result in excess stock. Stock slows the cash flow [15] and can lead to losses, especially for perishable items. This results in grocery retailers losing up to 15% as a result of damage and spoilage [14]; therefore, having a contingency plan using recommender systems to act upon short-term to shift demand may help avoid shortage or excessive stock.

Phase 2 is supported by 9 steps, as depicted in Figure 1. This figure gives an overview of the proposed method to adapt recommendations to stock levels and a user’s categorization. Depending on stock levels and a customer’s categorization, constants A and B permit reordering recommended items.

Multiplying the score of an item in the list by a high constant makes the recommendation of the given item in the first rank of the recommendation list. Constant A must remain superior to the other constants used for a given user. Thus, items at risk of being OOS will always be recommended at the top of the list. Multiplying the scores for items that are out of stock by is a way to disfavor the items’ recommendations, since the item is currently unavailable.

Constant B is used to give the item a higher rank in the recommendation list compared to items with a normal range of stock in order to promote sale. B is a constant that is higher than 1 but inferior to A in order to make items from step 5 second priority. is calculated based on how important the overstock is by using a calculated rate that could, for example, use formula 2.

![](/api/attachments/85JKHBBU/fulltext/images/cf671b9bd2561342aaaf5dcdc942ef8b58e8552216a628a8317f7992bb117116.jpg)  
Figure 1: Recommendation adjustment based on stock levels and customer categories

$$
B (i) = \frac {A c t u a l s t o c k (i)}{P r e d i c t e d s a l e s (i)}\tag{2}
$$

Alternative choices are considered for the first Y items that are proposed to user j. An alternative item could be the next item in the X recommended items for user j, or an item supposed to be equivalent to i. If an alternative item is OOS, it is proposed to select the next available alternative item from the X first recommendations. If all of the alternatives are low in stock, we recommend a diferent item that is not out-of-stock. If all of the items are

OOS, then it recommends one of the remaining items with the highest scores.

## 4. Pedagogical case study

In this section, we validate the results and improvements permitted by the proposed method. Section 4.1 exposes the context of the case study. Section 4.2 presents a data description and a company’s strategy used for the case study. Section 4.3 presents the status quo results using an actual recommender system, section 4.4 shows the results from the proposed methodology and compares the performance with results from section 4.3.

## 4.1. Context

This study is based on a real-life situation with our industrial partner. The partner uses two coexisting distribution channels: store-based and website-based. The company is specialized in business to business commerce with diferent customers from various fields and levels of importance.

The industrial partner uses a classical recommender system, which suggests items without considering stock levels. This may result in the recommendation of out-of-stock items. Currently, the importance of certain users and the fields of activity are not used to prioritize recommendations when stock levels are low. Here, we compare the benefits resulting from the execution of their current RS and from our proposed methodology.

## 4.2. Data description

In order to illustrate the implementation of this method, we simulated and scaled data to a smaller sample, keeping a similar structure as the existing one with our industrial partner. 17 items are separated into 8 categories.

Each category is represented by a single capital letter (A – H). Items from the same category are supposed to have similar usefulness and are considered interchangeable. 10 users with diferent profiles will make orders. Table 1 presents recommendation scores for the 10 users and 17 items.

Table 1: Simulated recommender systems’ scores

<table><tr><td>Cat</td><td colspan="5">A</td><td colspan="4">B</td><td colspan="2">C</td><td>D</td><td>E</td><td colspan="2">F</td><td>G</td><td>H</td></tr><tr><td>Ids</td><td>a1</td><td>a2</td><td>a3</td><td>a4</td><td>a5</td><td>b1</td><td>b2</td><td>b3</td><td>b4</td><td>c1</td><td>c2</td><td>d</td><td>e</td><td>f1</td><td>f2</td><td>g</td><td>h</td></tr><tr><td>User 1</td><td>0.491</td><td>0.2</td><td>0.238</td><td>0.677</td><td>0.874</td><td>0.741</td><td>0.029</td><td>0.949</td><td>0.632</td><td>0.604</td><td>0.156</td><td>0.701</td><td>0.036</td><td>0.134</td><td>0.142</td><td>0.606</td><td>0.759</td></tr><tr><td>User 2</td><td>0.314</td><td>0.886</td><td>0.058</td><td>0.539</td><td>0.408</td><td>0.559</td><td>0.153</td><td>0.811</td><td>0.565</td><td>0.245</td><td>0.727</td><td>0.218</td><td>0.815</td><td>0.335</td><td>0.854</td><td>0.918</td><td>0.108</td></tr><tr><td>User 3</td><td>0.016</td><td>0.253</td><td>0.828</td><td>0.942</td><td>0.084</td><td>0.977</td><td>0.473</td><td>0.466</td><td>0.935</td><td>0.802</td><td>0.298</td><td>0.256</td><td>0.096</td><td>0.238</td><td>0.323</td><td>0.299</td><td>0.07</td></tr><tr><td>User 4</td><td>0.259</td><td>0.759</td><td>0.138</td><td>0.724</td><td>0.912</td><td>0.532</td><td>0.08</td><td>0.816</td><td>0.757</td><td>0.358</td><td>0.839</td><td>0.315</td><td>0.945</td><td>0.738</td><td>0.876</td><td>0.035</td><td>0.397</td></tr><tr><td>User 5</td><td>0.467</td><td>0.472</td><td>0.65</td><td>0.42</td><td>0.986</td><td>0.381</td><td>0.619</td><td>0.895</td><td>0.926</td><td>0.825</td><td>0.578</td><td>0.393</td><td>0.956</td><td>0.599</td><td>0.078</td><td>0.851</td><td>0.711</td></tr><tr><td>User 6</td><td>0.452</td><td>0.338</td><td>0.671</td><td>0.84</td><td>0.792</td><td>0.881</td><td>0.538</td><td>0.544</td><td>0.26</td><td>0.149</td><td>0.692</td><td>0.757</td><td>0.181</td><td>0.851</td><td>0.497</td><td>0.794</td><td>0.798</td></tr><tr><td>User 7</td><td>0.348</td><td>0.118</td><td>0.16</td><td>0.781</td><td>0.517</td><td>0.624</td><td>0.093</td><td>0.933</td><td>0.113</td><td>0.815</td><td>0.579</td><td>0.16</td><td>0.396</td><td>0.382</td><td>0.735</td><td>0.092</td><td>0.442</td></tr><tr><td>User 8</td><td>0.865</td><td>0.737</td><td>0.454</td><td>0.85</td><td>0.59</td><td>0.873</td><td>0.804</td><td>0.827</td><td>0.149</td><td>0.932</td><td>0.852</td><td>0.315</td><td>0.636</td><td>0.014</td><td>0.444</td><td>0.38</td><td>0.598</td></tr><tr><td>User 9</td><td>0.124</td><td>0.814</td><td>0.464</td><td>0.045</td><td>0.119</td><td>0.856</td><td>0.572</td><td>0.222</td><td>0.649</td><td>0.171</td><td>0.111</td><td>0.356</td><td>0.613</td><td>0.723</td><td>0.822</td><td>0.641</td><td>0.969</td></tr><tr><td>User 10</td><td>0.916</td><td>0.434</td><td>0.827</td><td>0.143</td><td>0.501</td><td>0.276</td><td>0.476</td><td>0.863</td><td>0.846</td><td>0.384</td><td>0.789</td><td>0.016</td><td>0.075</td><td>0.768</td><td>0.699</td><td>0.296</td><td>0.75</td></tr></table>

For the case study, we consider the top 3 items with the highest score for each user (Y = 3) and we keep a total of the top 6 items (X = 6) to improve recommendations. In Table 1, for each user, the 3 items with the highest scores are in bold. For example, for user 1, the suggested items are b3, a5 and h, which have the highest scores for user 1.

Table 2 shows for each item, the inventory levels (Stock), safety stock levels (SS) and expected stock (Exp. Stock), at the initial time. In order to facilitate the reader’s understanding, information about stock level is fixed for the period that is considered. In a real application, stock levels may vary pending on other sales made outside the RS and replenishments. Thus, stock levels should be retrieved directly from the inventory system at each evaluation of step 2 and step 6. For example, for item a1, initial stock level is 0, safety stock level is 5, and expected remaining stock is 8.

Table 2: Product inventory levels (Stock), safety stock levels (SS) and expected stock (Exp. Stock), at initial time

<table><tr><td>Item</td><td>Stock</td><td>SS</td><td>Exp. stock</td><td>Item</td><td>Stock</td><td>SS</td><td>Exp. stock</td></tr><tr><td>a1</td><td>0</td><td>5</td><td>8</td><td>c1</td><td>4</td><td>5</td><td>8</td></tr><tr><td>a2</td><td>8</td><td>5</td><td>8</td><td>c2</td><td>6</td><td>2</td><td>6</td></tr><tr><td>a3</td><td>30</td><td>20</td><td>35</td><td>d</td><td>10</td><td>8</td><td>15</td></tr><tr><td>a4</td><td>4</td><td>5</td><td>10</td><td>e</td><td>6</td><td>5</td><td>10</td></tr><tr><td>a5</td><td>8</td><td>5</td><td>10</td><td>f1</td><td>30</td><td>5</td><td>15</td></tr><tr><td>b1</td><td>2</td><td>5</td><td>10</td><td>f2</td><td>5</td><td>10</td><td>15</td></tr><tr><td>b2</td><td>10</td><td>8</td><td>12</td><td>g</td><td>20</td><td>15</td><td>30</td></tr><tr><td>b3</td><td>2</td><td>5</td><td>12</td><td>h</td><td>5</td><td>3</td><td>6</td></tr><tr><td>b4</td><td>1</td><td>10</td><td>5</td><td></td><td></td><td></td><td></td></tr></table>

## Phase 1: Categorization of the users

Customers are separated into categories. CAT1: high priority customer, includes customers with the highest CLV, customers with binding contracts for priority delivery, customers with ethical requirements for delivery (i.e. medium or low priority customers are subdivided in CAT2.1: medium priority customers, and CAT2.2: low priority customers.

For the simulation, we consider that each user belongs to a category as provided in 3. Similar to the real dataset, the proportions were set as follows: 20% of the customers were CAT 1 and the remaining 80% are randomly separated between CAT2.1 and CAT2.2.

We allocate diferent penalties for each category of unsatisfied users (See Table 4): Penalty is the loss in the long-run of average demand rate, which is afected by backorders [26]. The loss of a customer in category CAT1 is estimated to cause a damage of 100

The data described in this section will be used independently in sections

Table 3: Categorization of users

<table><tr><td>Users</td><td>CAT</td><td>Users</td><td>CAT</td></tr><tr><td>User 1</td><td>CAT2.2</td><td>User 6</td><td>CAT2.2</td></tr><tr><td>User 2</td><td>CAT2.1</td><td>User 7</td><td>CAT2.2</td></tr><tr><td>User 3</td><td>CAT2.2</td><td>User 8</td><td>CAT1</td></tr><tr><td>User 4</td><td>CAT2.1</td><td>User 9</td><td>CAT2.2</td></tr><tr><td>User 5</td><td>CAT1</td><td>User 10</td><td>CAT2.1</td></tr></table>

Table 4: Penalties based on clients’ categories

<table><tr><td>Categories</td><td>Penalties</td></tr><tr><td>CAT1</td><td>100</td></tr><tr><td>CAT2.1</td><td>10</td></tr><tr><td>CAT2.2</td><td>5</td></tr></table>

4.3 and 4.4 to evaluate the results of the use in a state of the art system and to simulate the impact of the use of the proposed method. Recommendations in real life are made in real time, customer by customer. In order to illustrate the situation, we consider:

1. Customers come in the chronological order depicted in Table 3.

2. Customers buy all of the recommended items (X=3 for the example). This represents a worst-case scenario for OOS evaluation.

3. Customers only buy one of each recommended item.

## 4.3. Status quo: Results from actual systems

This section presents inventory variations related to the use of traditional RSs. Data from Tables 1 to 4 are considered. Each user receives a recommendation of the three highest ranked items in Table 1. So User 1 is recommended items b3, a5 and h. Considering he buys the recommended items, the stock will diminish for each of those items and become b3: 1, a5: 7 and h: 4, before going to the next user.

By going this way, from one user to another and simulating the efect of a purchase for each possible recommended item, it is apparent that some recommendations will include OOS items. The final results is provided in Table 5. This shows, for each costumer, the recommended items and how the stock levels evolved. Items that are out of stock are identified with (-1). This leads to some unsatisfied users and to penalties. The total penalty equals 335 with this strategy. The following section will show how the proposed method decreases penalties related to stock mismanagement by adapting the recommendations based on stock levels.

Table 5: Penalties related to the OOS for each user

<table><tr><td>Users</td><td>CAT</td><td>i1</td><td>i2</td><td>i3</td><td>Penalty</td></tr><tr><td>User 1</td><td>CAT2.2</td><td>b3: 1</td><td>a5: 7</td><td>h: 4</td><td></td></tr><tr><td>User 2</td><td>CAT2.1</td><td>g: 19</td><td>a2: 7</td><td>f2: 4</td><td></td></tr><tr><td>User 3</td><td>CAT2.2</td><td>b1: 1</td><td>a4: 3</td><td>b4: 0</td><td></td></tr><tr><td>User 4</td><td>CAT2.1</td><td>e: 5</td><td>a5: 6</td><td>f2: 3</td><td></td></tr><tr><td>User 5</td><td>CAT1</td><td>a5: 5</td><td>e: 4</td><td>b4: -1</td><td>100</td></tr><tr><td>User 6</td><td>CAT2.2</td><td>b1: 0</td><td>f1: 29</td><td>a4: 2</td><td></td></tr><tr><td>User 7</td><td>CAT2.2</td><td>b3: 0</td><td>c1: 3</td><td>a4: 1</td><td></td></tr><tr><td>User 8</td><td>CAT1</td><td>c1: 2</td><td>b1: -1</td><td>a1: -1</td><td>200</td></tr><tr><td>User 9</td><td>CAT2.2</td><td>h: 3</td><td>b1: -1</td><td>f2: 2</td><td>5</td></tr><tr><td>User 10</td><td>CAT2.1</td><td>a1: -1</td><td>b3: -1</td><td>b4: -1</td><td>30</td></tr><tr><td colspan="4"></td><td>Total</td><td>335</td></tr></table>

## 4.4. Results of the proposed methodology

The same data from Tables 1 to 4 are considered with the methodology proposed in section 3.2. Each user is processed and each stock level is updated. As an example, we selected Y=6 items in the list of possible suggested items. A detailed step by step application of the method is presented for all users. Users 1, 2, 5 and 6 enable showing all possible options covered by the methodology.

## For user 1

Step 1: We extract the Y=6 top items from Table 1. Products b3, a5, h, b1, d, and a4 are considered.

Step 2: For each item, we extract product inventory information from Table 2 and if the quantity in stock is lower than the safety stock we go to Step 3 (this is for items b3, b1 and a4), or else we will go to Step 6 (this is for items a5, h and d).

Step 3: There is a risk of OOS for b3, b1 and a4, but only b3 is in the X=3 best items. Active user1 is CAT2.2 (see Table 3) so go to Step 4 .

Step 4: We need alternative choices for b3. b1 is an alternative to b3 in the recommendation list, but b1 is also at risk for OOS. b1 is not an option, so we take the next in line, which is d. d takes the place and score of b3.

Step 6: For items a5 and h, the quantity in stock is inferior to the expected stock (see Table 2), the next step is Step 7.

Step 7: No changes in the score for a5 and h. Go to Step 9.

Step 9: Recommend a re-ordered list of 3 unique first items.

Initial and adapted recommendations for user 1 are presented in Table 6, only the X=3 first items are presented to the user.

Following our hypothesis, user 1 takes items d, a5 and h, quantities in stock for those items that are updated: d: 9, a5: 7 , h: 4

## For user 2

Step 1: We extract the Y=6 top items from Table 1. Products g, a2, f2,

Table 6: Recommendation summary for user 1

<table><tr><td colspan="2">Initial recommendation</td><td colspan="2">Adapted recommendation</td></tr><tr><td>Item</td><td>Rec scores</td><td>Item</td><td>Rec scores</td></tr><tr><td>b3</td><td>0.949</td><td>d</td><td>0.949</td></tr><tr><td>a5</td><td>0.874</td><td>a5</td><td>0.874</td></tr><tr><td>h</td><td>0.759</td><td>h</td><td>0.759</td></tr><tr><td>b1</td><td>0.741</td><td>b1</td><td>0.741</td></tr><tr><td>d</td><td>0.701</td><td>d</td><td>0.701</td></tr><tr><td>a4</td><td>0.677</td><td>a4</td><td>0.677</td></tr></table>

e, b3, and c2 are considered.

Step 2: For each item, we extract product inventory information from Table 2, updated from previous sales, and if the quantity in stock is lower than the safety stock we go to Step 3 (it is for items f2 and b3) or else we go to go to Step 6 (this is for items g, a2, e, and c2).

Step 3: There is a risk of OOS for f2 and b3, but only f2 is in the X=3 best items. Active user2 is $\mathrm { C A T 2 . 1 }$ (see Table 3) go to Step 4 .

Step 4: We need alternative choices for f2. An alternative from the list of the 6 top recommendations, with a stock that is superior to Safety Stock level, is e. We replace f2 with e and keep f2’s score.

Step 6: For item a2 and g, quantity in stock is higher than the expected stock go to Step 7.

Step 7: No changes in score for a2 and g. Go to Step 9.

Step 9: Recommend a re-ordered list of 3 unique first items.

Initial and adapted recommendations for user 1 are presented in Table 7, only the X=3 first items are presented to the user.

Following our hypothesis, user 2 takes items g, a2 and e; the quantities in stock for those items that are updated are: g: 19, a2: 7 , e: 5

Table 7: Recommendation summary for user 2

<table><tr><td colspan="2">Initial recommendation</td><td colspan="2">Adapted recommendation</td></tr><tr><td>Item</td><td>Rec scores</td><td>Item</td><td>Rec scores</td></tr><tr><td>g</td><td>0.918</td><td>g</td><td>0.918</td></tr><tr><td>a2</td><td>0.886</td><td>a2</td><td>0.886</td></tr><tr><td>f2</td><td>0.854</td><td>e</td><td>0.854</td></tr><tr><td>e</td><td>0.815</td><td>e</td><td>0.815</td></tr><tr><td>b3</td><td>0.811</td><td>b3</td><td>0.811</td></tr><tr><td>c2</td><td>0.727</td><td>c2</td><td>0.727</td></tr></table>

## For users 3 and 4

The same procedure applies to users 3 and 4. The users are from CAT2, presented with recommendations of items with normal to low stock levels. The recommendation scores are kept the same and items are replaced with alternatives for low inventory items. Alternative choices at Step 4 are either the next item available in a large enough quantity to be recommended (>SS) or an item from the same category as the replaced item.

User 3 takes items a3, a5 and b2, quantities in stock for those items are updated: a3: 29, a5: 6, b2: 9, and user 4 takes items c2, a5 and a2, quantities in stock for those items are updated: c2:5, a5: 5, a2: 6.

## For user 5

This user goes to Step 5 for items a5, e, b4, b3, g, and c1. The recommendation scores are adapted using constant A in order to prioritize the items with low inventory for users in CAT1. For items that are out of stock, the score is set to 0 so the item is never recommended. Constant A has to be higher than the highest ratio of (stock to expected stock). In this example, A is set to 10. Recommendations for user 5 are in Table 8, and user 5 takes items g, a2 and e, quantities in stock for those items that are updated: a5: 4, e:4, b4: 0.

Table 8: Recommendation summary for user 5

<table><tr><td colspan="2">Initial recommendation</td><td colspan="2">Adapted recommendation</td></tr><tr><td>Items</td><td>Rec Scores</td><td>Items</td><td>Rec Scores</td></tr><tr><td>a5</td><td>0.986</td><td>a5</td><td>0.986 x 10=9.86</td></tr><tr><td>e</td><td>0.956</td><td>e</td><td>0.956 x 10 = 9.56</td></tr><tr><td>b4</td><td>0.926</td><td>b4</td><td>0.926 x 10=9.26</td></tr><tr><td>b3</td><td>0.895</td><td>b3</td><td>0.895</td></tr><tr><td>g</td><td>0.851</td><td>g</td><td>0.851</td></tr><tr><td>c1</td><td>0.825</td><td>c1</td><td>0.825 x 10 = 8.25</td></tr></table>

## For user 6

User 6 goes to Step 8 for item f1. We will multiply the f1 score of the item by constant B.

$$
B (f 1) = \frac {A c t u a l s t o c k (f 1)}{P r e d i c t e d s a l e s (f 1)} = \frac {3 0}{1 5} = 2
$$

The new score for $f 1 = 0 . 8 5 1 * 2 = 1 . 7 0$ . User 6 takes items f1, h and $\mathrm { g } ,$ and the quantities in stock for those items are updated: f1:29, h:3, g:18.

## For users 7 through the end

In presenting users 1 to 6, all possibilities of the proposed methodology are covered, and each step in the method has been presented. User 7 takes items b2, c2 and a3. User 8 takes items c1, b1 and c2. User 9 takes f1, h and b2. User 10 takes f1, h and b2.

The new recommendation list contains no OOS items; thus, no penalties have been applied to the company. For example, instead of assigning item b1 to a user with low value to the company, it was only recommended to high value customers; that way, the penalty is lower, thanks to the better allocation of stock.

## 5. Experimental Results

In order to visualize the efects of the implementation of our method on the penalties related to stock-outs, as well as to review the accuracy of the recommendations, we conducted an experiment on a larger set of products and users and compared the proposed method to the traditional method.

The data used in the experimental example has been inspired from an industrial partner dataset (that cannot be published) and contains its main characteristics. Historical purchases lead to a very sparse matrix and diferent recommender systems that were tested on that data, resulting in a list of items with a recommendation score. Since the recommendation score is onl input data, and no specific recommender system is linked to the methodology, we generated scores that represent a RS output. In addition, exploratory data analyses on the real dataset reveal customers’ behaviours and items’ categories that led to the characteristics used in the simulated data: (1) Items from the catalogue are segmented into 16 diferent categories each one representing an industrial field; (2) a limited number of customers generated 20% of the company’s revenue. After testing the method with many examples, we concluded that if kept in the same proportions (those of the industrial partners), the size of the sample does not impact the efect on the penalties and accuracy of recommendations, and therefore the conclusions remain the same.

## 5.1. Data description

To evaluate the method, we selected the following parameters:

• 500 items are separated into 5 categories. Each category is represented by a single capital letter (A – E). Items from the same category are used in the same field (i.e., Medical, Industrial, Agriculture, etc.).

• We have 1000 users with diferent profiles. From those, we randomly and chronologically generate 1500 entrances in the recommender system, that means that the same user can appear more than once and simulates the fact that a user can purchase more than once and also that some users may make no purchase at all.

• For the proposed method: X = 6, Y = 15, Bmax = 100 and A = 1000.

## 5.2. Results

All of the hypotheses presented in sections 3 and 4 remain unchanged. Using Rstudio [33], we run the methods on the data presented above and get the following results.

The graph presented in Figure 2 shows the cumulative penalties related to stock-outs with the two methods. The blue line represents the penalties related to the traditional recommendation technique and the red line represents the penalties related to the proposed method, with consideration made to stock levels and the customer category.

The graph shows three phases, in the first (P1), the slope of the penalties curve for the traditional recommendation (blue) is positive but small compared to the proposed method (red), which shows a neutral slope. This can

## ACCEPTED MANUSCRIPT

![](/api/attachments/85JKHBBU/fulltext/images/33d637581df37a50634cbc6272d843e8e847ed9b8d0b28ec82cf45ff09cbdcf5.jpg)  
Figure 2: Cumulative penalties according to customers’ arrivals, for both methods

be explained by the fact $\operatorname { t h a t } , \mathrm { a t }$ the beginning of the recommendation process, the majority of the items have suficient stock levels; only few products However, no OOS are recommended using the proposed method.

In the second phase (P2), the gap between the two methods starts to get larger. The penalties increase steadily for the traditional RS (blue) in contrast with the proposed method (red), which maintains the penalties to 0 all along P2. This can be explained by the fact that the second method presents alternatives for items that demonstrate low stock, delaying the stock-outs and shifting demand to other products instead of highlighting the ones that are already low in stock. At this step, we can argue that the accuracy of the recommendation will get lower when presenting alternatives to the products. Figure 3 presents the efect on the recommendation scores. Although accuracy decreases, it is important to remember the objectives behind the recommendations presented in (section 2.1) such as (2) increasing cross selling by ofering additional products to customers, and (3) improving consumer loyalty [28, 34, 31].

Since a product that is OOS cannot be sold, making a 100% accurate recommendation for a product, but not being able to meet user’s need for that product, is useless. Consequently, having an accurate recommendation may be irrelevant in some situations, such as when dealing with shortages. By suggesting products that are low in stock to all customers, we sell products that are in high demand to random customers without favoring those with high value, making the occurrence of the OOS random. Also, when a product is OOS, neither (2) nor (3) can be achieved, and the cost of a stock out on the business is not controlled.

In the third phase (P3), we can see that both methods have the same increasing tendency in the slope of the curve. This can be explained by the fact that more items are out of stock and the alternatives are more limited. Although the slope is positive for both methods, the one we recommend keeps the penalties lower. Also, by postponing the occurrence of a stock out, we get more time to deal with the issue and replenish the stocks (the arrival of customers is also implicitly the time stamp).

Figure 3 presents a parallel between cumulative penalties presented in (Figure 2), the diference between the cumulative penalties incurred by each method, and a comparison of the mean score of recommendations for all users.

![](/api/attachments/85JKHBBU/fulltext/images/c9496a34fa6ec36b4f9f00582e73ecf78dbbde4151092645191e0c954b94916a.jpg)  
Figure 3: Impacts of the proposed method on recommendation scores

It is observed that in the first phase (P1), the diference between the two methods is the highest, the diference between the penalties increases in (P1) and (P2) and stabilises in (P3), the same occurs with regards to the accuracy of the recommendation. We can see that, in (P1), there is a notable diference in the scores of the recommended products. Since we suggest alternatives for products that are low in stock, the scores of the recommendations are lower. In order to keep the recommendations relatively good, we only select alternatives from the top 15 recommendations and not from all available items. Although the recommendation scores are lower than those from the traditional method, they are still relatively close and stabilize completely in (P3). This is because both methods present the same products as a result of a lack of viable alternatives with suficient stock.

After testing our method with diferent sizes of products, users, recommendation sizes and families, we have concluded that if kept in the same proportions (based on the data presented by our industrial partners), the size of the sample will not impact the efect on the penalties and accuracy of recommendations and therefore the conclusions remain the same.

## 6. Conclusion

The proposed approach consists of an adaptation of recommender systems, using well-established customer relationship management concepts. The focus is to help companies shape demand with an execution process by acting upon short-term demands to recover from excess and short inventory positions and limit the consequences of the mismanagement of stocks.

Recommendation systems have become essential in e-commerce; they collect and process intelligence gathered about customers by the company. These systems have been used to allow a user to reduce search time and improve the user experience, which in turns helps in the retention of the user for the company. Recommender systems are also used to increase cross-selling. Some customized RSs can even consider the profits on items and maximize the profit potential of a recommendation.

However, the development of RSs mainly focuses on commercial interests of the customers. Our goal has been to develop an area of RSs that can meet industrial interests at the same time. Our attempt at doing so has been by adapting recommendations according to categorization of customers. The importance of a customer is variable and depends on the area of activity of a company, its strategies and policies. Diferent indicators of customer importance can be used and incorporated into Step 1 of our method. Those categories of customers enable favoring certain customers over regular customers, and make sure that the long-term impact on the company is monitored.

However, the proposed approach relies on the accuracy of recommendations and stock management.

## Limitations and perspectives

Recommender systems are based on many diferent techniques. As stated in the state of the art, those techniques lead to diferent kinds of recommendations, depending on the available data and the purpose behind the recommendation. Using recommender systems is not trivial and making the right choices directly influences the accuracy of the recommended items. It is of high importance to obtain a customized recommender system in order to align with businesses interests without altering the perceived customer trust in the technology, since it is considered a key component in marketing and e-commerce literature [3]. Trust formation can be described in terms of six dimensions: consumer behavioral, institutional, information, product, transaction, and technology. By manipulating the recommender system, information and technology are impacted [22]. Making bad recommendations will result in a mistrust of the system, and will be of no use for demand shifting.

Most companies track stock, whether it is online or on ERPs. Therefore, getting a good approximation of the current inventory is usually possible in most cases. Our aim is not to improve inventory management systems, but to deal with the consequences of stock mismanagement in real time. Thus, we consider that the existing system considers demand, seasonality, average replenishment time, while determining safety stocks. If the safety stocks and the prediction of stock consumption is not calculated efectively, it can lead to unnecessary actions on recommendations that can lower accuracy without helping the business.

Future work includes developing a better way of choosing alternative items at (Step 4) in our proposed method. Considering the similarities in terms of the usefulness of the items, or the similarities of an item’s features, could be used to improve alternative choices and make them systematic. In addition, we consider only the customer categories and the stock information for an item; many other supply chain constraints could be considered, such as logistic constraints on stock location, delivery points, warehouse storage capacity, trends in raw material prices and the margin of products.

## Acknowledgments

The authors would like to acknowledge our industrial partner (Air Liquide) and the National Sciences and Engineering Research Council of Canada (NSERC) for funding this work under grant RDCPJ 492021-15, and for providing other support for this research. We would also like to express our gratitude to Mehdi Miah for sharing his expertise on the coding of the methodology.

## 7. References

[1] Adomavicius, G. and Tuzhilin, A. (2005). Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE transactions on knowledge and data engineering, 17(6):734– 749.

[2] Bauer, J. and Nanopoulos, A. (2014). Recommender systems based on quantitative implicit customer feedback. Decision Support Systems, 68:77– 88.

[3] Beatty, S. E., Mayer, M., Coleman, J. E., Reynolds, K. E., and Lee, J. (1996). Customer-sales associate retail relationships. Journal of retailing, 72(3):223–247.

[4] Berger, P. D. and Nasr, N. I. (1998). Customer lifetime value: Marketing models and applications. Journal of interactive marketing, 12(1):17–30.

[5] Bobadilla, J., Ortega, F., Hernando, A., and Bernal, J. (2012). A collaborative filtering approach to mitigate the new user cold start problem. Knowledge-Based Systems, 6:225–238.

[6] Burke, R. (2002). Hybrid recommender systems: Survey and experiments. User modeling and Customer-Adapted Interaction, 12(4):331–370.

[7] Burke, R., Felfernig, A., and G¨oker, M. H. (2011). Recommender systems: An overview. Ai Magazine, 32(3):13–18.

[8] Candillier, L., Meyer, F., and Boull´e, M. (2007). Comparing stateof-the-art collaborative filtering systems. In International Workshop on

Machine Learning and Data Mining in Pattern Recognition, pages 548– 562. Springer.

[9] Chen, L.-S., Hsu, F.-H., Chen, M.-C., and Hsu, Y.-C. (2008). Developing recommender systems with the consideration of product profitability for sellers. Information Sciences, 178(4):1032–1048.

[10] Cinar, E. and Gollu, R. (2012). An inventory model with capacity flexibility in the existence of advance capacity information. Decision Support Systems, 53(2):320–330.

[11] Corsten, D. and Gruen, T. (2003). Desperately seeking shelf availability: an examination of the extent, the causes, and the eforts to address retail out-of-stocks. International Journal of Retail & Distribution Management, 31(12):605–617.

[12] Dadouchi, C. and Agard, B. (2017). Etat de l’art sur les syst\`emes de <sup>´</sup> recommandation. In 12\`eme Congr\`es International de Genie Industriel, Compi\`egne, France.

[13] Demiriz, A. (2004). Enhancing product recommender systems on sparse binary data. Data Mining and Knowledge Discovery, 9(2):147–170.

[14] Ferguson, M. and Ketzenberg, M. E. (2006). Information sharing to improve retail product freshness of perishables. Production and Operations Management, 15(1):57.

[15] Fernandes, R., Gouveia, J., and Pinho, C. (2010). Overstock–a real option approach. Journal of Operations and Supply Chain Management, 3(2):98–107.

[16] Fitzsimons, G. J. (2000). Consumer response to stockouts. Journal of consumer research, 27(2):249–266.

[17] Gatzioura, A. and S\`anchez-Marr\`e, M. (2015). A case-based recommendation approach for market basket data. IEEE Intelligent Systems, 30(1):20–27.

[18] Graves, S. C. and Willems, S. P. (2000). Optimizing strategic safety stock placement in supply chains. Manufacturing & Service Operations Management, 2(1):68–83.

[19] Group, I. (2015). Retailers and the ghost economy \$1.75 trillion reasons to be afraid. Research Study.

[20] Guo, J., Gao, Z., Liu, N., and Wu, Y. (2018). Recommend products with consideration of multi-category inter-purchase time and price. Future Generation Computer Systems, 78:451–461.

[21] Hart, C. W., Heskett, J. L., and Sasser, J. W. (1990). The profitable art of service recovery. Harvard business review, 68(4):148–156.

[22] Jarvenpaa, S. L., Tractinsky, N., and Vitale, M. (2000). Consumer trust in an internet store. Information technology and management, 1(1-2):45– 71.

[23] Kim, M. and Lennon, S. J. (2011). Consumer response to online apparel stockouts. Psychology & Marketing, 28(2):115–144.

[24] Lapide, L. (2005). Benchmarking best practices. The Journal of Business Forcasting, 6:29–32.

[25] Lapide, L. (2013). Supply’s demand-shaping roles. The Journal of Business Forecasting, 32(3):18.

[26] Liberopoulos, G., Tsikis, I., and Delikouras, S. (2010). Backorder penalty cost coeficient “b”: What could it be? International Journal of Production Economics, 123(1):166–178.

[27] Lin, Z. (2014). An empirical investigation of user and system recommendations in e-commerce. Decision Support Systems, 68:111–124.

[28] Lu, J., Wu, D., Mao, M., Wang, W., and Zhang, G. (2015). Recommender system application developments: a survey. Decision Support Systems, 74:12–32.

[29] Meyer, F. (2012). Recommender systems in industrial contexts. PhD thesis, Universite de Grenoble, Ecole Doctorale Mathematiques, Sciences et Technologies de l’Information, Informatique, Grenoble, France.

[30] Pathak, B., Garfinkel, R., Gopal, R. D., Venkatesan, R., and Yin, F. (2010). Empirical analysis of the impact of recommender systems on sales. Journal of Management Information Systems, 27(2):159–188.

[31] Resnick, P. and Varian, H. R. (1997). Recommender systems. Communications of the ACM, 40(3):56–58.

[32] Ricci, F., Rokach, L., Shapira, B., and Kantor, P. B. (2011). Recommender Systems Handbook. Springer-Verlag New York, Inc., New York, USA, 1st edition.

[33] RStudio Team (2015). RStudio: Integrated Development Environment for R. RStudio, Inc., Boston, MA.

[34] Shardanand, U. and Maes, P. (1995). Social information filtering: algorithms for automating word of mouth. In Proceedings of the SIGCHI conference on Human factors in computing systems, pages 210–217. ACM Press : Addison-Wesley Publishing Co.

[35] Sloot, L. M., Verhoef, P. C., and Franses, P. H. (2005). The impact of brand equity and the hedonic level of products on consumer stock-out reactions. Journal of Retailing, 81(1):15–34.

[36] Stadtler H., Kilger C., M. H. (2015). Supply Chain Management and Advanced Planning. Springer, Heidelberg.

[37] Stevenson, W. (2007). Operations Management. McGraw-Hill, Boston, MA, 4th edition.

[38] Su, X. and Khoshgoftaar, T. M. (2009). A survey of collaborative filtering techniques. Advances in Artificial Intelligence, 2009:4:2–4:2.

[39] Wild, T. (2017). Best practice in inventory management. Institute of Operations Management, Taylor & Francis.

[40] Wu, Z . and Wu, J. (2015). Price discount and capacity planning under demand postponement with opaque selling. Decision Support Systems, 76:24–34.

[41] Zinn, W. and Liu, P. C. (2001). Consumer response to retail stockouts. Journal of business logistics, 22(1):49–71.

## Biography

![](/api/attachments/85JKHBBU/fulltext/images/78391b214610fe2c66f1d2831e6921c9219ade1b92069cd05fc8ec1adb7562c1.jpg)

Camélia Dadouchi, received her bachelor in Industrial Engineering from École Polytechnique de Montréal in (2015) and is currently a Ph.D candidate at École Polytechnique de Montréal and a member of both the Laboratoire d’Intelligence des Données (LID) and the CIRRELT . Her main research interests include recommender systems, electronic commerce, processes and logistics. Her current research focuses on using recommender systems as a way of leveraging industrial constraints related to stocks, logistics.

![](/api/attachments/85JKHBBU/fulltext/images/4753631b0e39ce901233424a6d155e9b47d775a091dd6396c21fdf4edc3e5726.jpg)

Bruno Agard is Full Professor in Industrial Engineering at École Polytechnique de Montréal, Québec, Canada. He graduated in Manufacturing from École Normale Supérieure de Cachan (1998). He received his Ph.D. in Industrial Engineering (2002) from the Institut National Polytechnique de Grenoble, France.

![](/api/attachments/85JKHBBU/fulltext/images/63ff9a470f9ac2708535ff79c6b857a0fb696ef4e2658fc32d228fb618da7a32.jpg)  
Figure 1

![](/api/attachments/85JKHBBU/fulltext/images/10caa01635b39f130914de716003844f56a9c6a081dee7fdbec33de584dd63af.jpg)  
Figure 2

![](/api/attachments/85JKHBBU/fulltext/images/ac89081e2cf668639e6ef2d78f9a4dec76c338b4c1c414ec637232c7e1b46a95.jpg)  
Figure 3
