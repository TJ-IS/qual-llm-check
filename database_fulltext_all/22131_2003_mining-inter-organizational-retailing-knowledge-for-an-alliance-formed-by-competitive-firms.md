---
otero_id: 22131
otero_key: "GQB44BBE"
title: "Mining inter-organizational retailing knowledge for an alliance formed by competitive firms"
authors: "Qi-Yuan Lin; Yen-Liang Chen; Jiah-Shing Chen; Yu-Chen Chen"
year: "2003"
journal: "Information & Management"
doi: "10.1016/s0378-7206(02)00062-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Application

# Mining inter-organizational retailing knowledge for an alliance formed by competitive firms

Qi-Yuan Lin<sup>a</sup>, Yen-Liang Chen<sup>a</sup>, Jiah-Shing Chen<sup>a</sup>, Yu-Chen Chen<sup>b,\*</sup>

<sup>a</sup>Department of Information Management, National Central University, Chung-Li 320, Taiwan, ROC <sup>b</sup>Department of Business Administration, Soochow University, Taipei 100, Taiwan, ROC

Received 12 April 2001; received in revised form 3 January 2002; accepted 22 May 2002

## Abstract

This paper applies data mining techniques to extract retailing knowledge from the POS information provided by an interorganizational information service center in Taiwan. Many mutually competitive retail chains sponsored the data warehouse. They must, of course, protect their secrets, while cooperating to mine the inter-organizational data and thereby extract macrolevel knowledge about consumers’ behavior. Many difficulties arise from this, because each transaction contains only a summary indicating the total sales of a single product in a store during a month and more detailed data are not available. Moreover, with many retail store chains cooperating, the meaning of the quantitative data, such as price and quantity, is difficult to compare and hard to interpret. No previous research addressed this problem. A series of steps were implemented to help solve this problem; they include defining semantic association rules (AR), transforming the quantitative data into semantic data and developing algorithms for mining the knowledge. Finally, we consolidated these ideas and implemented a prototype system. <sup>#</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Data mining; Association rules; Data warehouse; POS; Retail store

## 1. Introduction

In an industry with thin margins, chains of retail stores compete fiercely for customers. The effective management of such businesses is dependent on the quality of its decision-making. However, competitors can easily observe and imitate each other’s initiatives. Thus, having and using knowledge about customers is critical to success, for such knowledge cannot be easily observed or imitated and can create competitive advantage for the business.

It is therefore important to improve the quality of business decisions by analyzing transaction data to discover customers’ purchasing behavior. To discover such knowledge, a retailer must delve into a huge amount of historic data to extract valuable decision information.

Data mining is, perhaps, the most promising solution. It has high applicability in various domains such as the retail industry [3], customer service support [10], and business [2]. Its aim is to discover potentially useful relationships in a large amount of data. Many techniques have been proposed to extract such knowledge. A typical approach is market basket analysis (or association rules discovery) [1], which analyzes customers’ buying habits by finding associations between different items placed in the shopping basket. Such knowledge can help retailers develop marketing strategies by knowing which items are frequently purchased together. For instance, if customers are buying milk, a retailer can determine how likely it is that the customer is also buying bread on the same trip to the supermarket. Such information can lead to cross- or up-selling by helping retailers conduct selective marketing and plan their shelf arrangement.

Because of its great managerial implications, such analysis has received much attention, and a great deal of related research has been performed, including fast algorithms for mining association rules (AR) [9], mining generalized AR [15], mining multiple-level AR [7], mining constrained AR [8], meta-rule guided mining [6], mining AR incrementally [4], mining quantitative AR [14], mining cyclic AR [11], mining interesting AR [12], mining optimized AR [13], and so on.

Since there is already much written about mining AR, building a data mining system for a single retail store is relatively simple: directly apply an existing method. After a number of transactions have been collected, preprocessed, and stored [5], one of the existing methods can be used.

Such methods, however, discover customers’ purchasing behavior for only a single enterprise. For any specific retailer, customers, former customers, and non-customers might behave differently. Therefore, for retail chains with only a moderate or small market share, the POS data collected from their systems can only portray a moderate or small portion of the market, and the knowledge obtained might not show the entire picture. Making decisions based on such knowledge might lead businesses in unfavorable directions. Inter-organizational knowledge is invaluable in such situations.

Unfortunately, data needed to mitigate this problem are often available only through a third party or a competitor. To overcome such barriers, retail chains can cooperate by gathering comprehensive data to discover macro-level knowledge of the consumers’ behavior. This presents difficulties, because retail chains are, of course, competitive in nature. A retailer is likely to hesitate at disclosure of details but may provide summarized data.

This transaction structure differs from the typical model; new methods need to be developed for mining such aggregated transaction data.

## 2. Background

Computer and Communication Research Labs (CCL) is a division of Industrial Technology Research Institute (ITRI) in Taiwan. ITRI was established and is sponsored by the Taiwan government; CCL is partially public and partially private in nature and was designated by the Taiwan government to be responsible for a nationwide electronic commerce project: the POS information service center project. Many chains of retail stores are joining this effort.

Its goal is to build and maintain a POS data warehouse to store all retail data from chains joining the alliance. The obligation of these chains is to submit sales data to the center once a month. In return, they are allowed entry into an Internet-based querying system. There they can view various summary reports and statistics concerning sales figures in the Taiwan retail market.

A transaction typically consists of a unique identifier, customer identifier, transaction date (or time), and the items purchased. However, the data submitted to the system are quite coarse; the sales for each product in each store during a month are aggregated to a single transaction. Therefore, each transaction contains: time (year/month), store, product, total-quantity-sold, and total-income.

Since data are stored in multidimensional models, store and product can be further generalized into higher-level concepts. The store can be generalized into style/type (convenience store, supermarket, stores for bundled sale), company, and city, which can be further generalized into district. The product can be successively generalized into a series of concepts including type, class and category (category being the most general).

Near the end of 1999, after seeing the value and widespread usage of data mining in the retail industry, CCL invited the authors to determine how to add further value to the information stored in the data warehouse. After thorough examination, we found several difficulties arisen from the above unique transaction structure.

1. The transaction contained only a summarized result indicating the total sales of a single product in a store during a month. Thus, it was impossible to tell what items were purchased together in a single shopping trip.

2. Although the transaction gives the quantity of a certain product sold in a store in any given month, the meaning of this quantity was unclear. For instance, if a retailer sold 600 bottles of milk in a month at a particular store, this may have different interpretations, depending on the normal turnover and any seasonal variation. In Taiwan, the boom season of milk sales is in summer and the slack time is in winter. Therefore, 600 bottles may appear dismal if the sales occurred in a store located in downtown Taipei in July, but it may be very positive in February in a store located in a small town.

3. Although the transaction in the CCL can tell us the average price of a certain product in a store in any given month, the meaning is unclear. For instance, if a retailer charges NT\$ 50 dollars for a bottle of milk, this price can be interpreted differently depending on the type of business and its seasonal variation. Usually, the price in a convenience store is higher than that in a supermarket, which is higher than it would be in a store for a bundled sale. Furthermore, the price of milk in summer is much higher than in winter. It is therefore impossible to tell a price of NT\$ 50 is high or low.

It is therefore clear that the conventional methods for dealing with transaction databases may not work. Yet one cannot simply declare these data unfit for mining. If an inter-organizational analysis of POS data is valuable to retail chains, then what is the valuable information we can find from the database?

## 3. Semantic association rules

In conventional transaction databases, an association rule is an implication of the form X ! Y, where X and Y are a subset of items and X \ Y ¼ ;. This rule indicates that if a consumer bought X, then it is likely that he or she will also purchase Y during the same shopping trip. But it is impossible to determine these kinds of rules because such data are not recorded. Therefore, we developed the following semantic asso ciation rules:

 between products;

 between stores;

 between companies;

 between stores in their turnovers.

We used semantic terms for describing quantity volume, price standard, turnover variation, quantity variation, and price variation. For volume, the semantic terms that could be applied were ‘‘large’’, ‘‘medium’’, and ‘‘small’’ quantity. As to price standard, the possible terms were ‘‘high’’, ‘‘medium’’, and ‘‘low’’. For turnover variation, quantity variation and price variation, we used the ‘‘increased’’, ‘‘the same’’, or ‘‘decreased’’.

All these semantics terms can be applied in the four kinds of rules. The product rule describes the price or quantity relationships between different products. For example, a rule could be as follows.

‘‘Product A’s price is high’’ and ‘‘Product B’s price is low’’ ! ‘‘Product A’s quantity is small’’ and ‘‘Product B’s quantity is increased’’.

The store rule describes the price or quantity relationships between products in different stores. As an example, a rule may be as follows.

‘‘Product A’s price in Store S-1 is high’’ ! ‘‘Product A’s quantity in Store S-1 is low’’ and ‘‘Product B’s price in Store S-2 is high’’.

Similarly, the company rule indicates the price or quantity relationships between products in different companies. An example is given as follows.

‘‘Product A’s price in Company C-1 is decreased’’ ! ‘‘Product B’s price in Company C-2 is decreased’’ and ‘‘Product B’s quantity in Company C-2 is increased’’ and ‘‘Product A’s quantity in Company C-1 is the same’’.

Finally, the turnover rule describes the turnover relationships between stores. A possible rule may be as follows.

‘‘Store S-1’s turnover is increased’’ ! ‘‘Store S-2’s turnover is decreased’’.

These rules can help in understanding when relationships between products are complementary, competitive, or independent in their quantities or prices. They can also be used to analyze the relationships between stores and companies. From the analysis, we can tell which stores influence the sales of certain products. Moreover, these rules can aid in designing a pricing strategy. In other words, we can identify those products that are price-sensitive and those that are price-insensitive.

Furthermore, we can use such rules to check whether cutting prices of selected products may increase the sales of other products or improve the overall turnover. Similarly, the rules can show whether raising prices of selected products will harm the sale of others significantly.

## 4. The definitions of semantic terms

Price standard is used to judge if the price of a product in a store is cheaper or more expensive than in other stores. Here, the targets of comparison are stores of the same business style and in the same time period, because such factors generally have a significant effect on prices. It is wrong to compare the prices in convenience stores with those offering bundled sale or during different time periods.

We therefore pre-compute the average prices $\mathsf { A P } _ { j , \boldsymbol { \mathrm { b } } , m }$ for every product $j ,$ every business style $\mathbf { b } ,$ and every month m. Moreover, we pre-compute their standard deviations $\mathrm { S P } _ { j , \mathbf { b } , m } .$ All these data, including average prices and standard deviations, are stored in a data warehouse. When we need to determine if a product’s price is comparatively low or high, we compare it with the average price of the same product for the same business style in the same month. This may be written as

$$
Z - P _ {j, \mathrm{b}, m} = \frac {\text { the   price } - \mathrm{AP} _ {j , \mathrm{b} , m}}{\mathrm{SP} _ {j , \mathrm{b} , m}}\tag{1}
$$

If $Z - P _ { j , \mathbf { b } , m }$ is larger than x, then we call it $h i g h ,$ , but if it is smaller than x, it is low. If neither holds, it is a medium price. Here, x is the price deviation threshold, and the users can determine the value of x at their discretion.

In our project, we partitioned the price interval into three parts: low, high, and medium. Since the partition is at the users’ discretion, it could be partitioned into five. We do not recommend more than this, as it is difficult for users to differentiate between too many intervals.

Quantity volume is used to judge if the sales amount of a product in a store is a large or small. This is difficult, because it depends on the size of the store. For a store in downtown Taipei, sales of 600 bottles of milk in a month may be small, but for a store in a small town, the same figure may be large. Furthermore, the semantics of quantity depend on the product, because some sell often and in great quantities while others sell rarely and in smaller quantities. For example, daily commodities and expendables such as tissues, milk, juice, etc. are in the former category, while machinery and electric appliances are in the latter.

We therefore pre-compute the average of the turnovers of all stores for every business style, as well as determining their standard deviation. For business style b, let these two values be denoted as $\mathrm { A T _ { b } }$ and $\mathrm { { S T } _ { b } . }$ In addition, for each product and each business style, we pre-compute the average of sales quantities of all stores, as well as their standard deviation. For business style b and product $j ,$ let these two values be denoted as $\mathbf { A Q } _ { \mathbf { b } , j }$ and ${ \mathrm { S Q } } _ { \mathrm { b } , j } .$ From these statistics, we can determine the scale of store i by using the formula:

$$
Z - T _ {i} = \frac {\text { the   turnover   of   store } i - \mathrm{AT} _ {\mathrm{b}}}{\mathrm{ST} _ {\mathrm{b}}}\tag{2}
$$

Furthermore, the following formula can be used to determine the relative position of the sales quantity of product j in store i compared to other stores:

$$
\begin{array}{r l} & Z - Q _ {i, j} \\ & = \frac {\text { the   sales   quantity   of   product } j \text { in   store } i - \mathrm{AQ} _ {\mathrm{b} , j}}{\mathrm{SQ} _ {\mathrm{b} , j}} \end{array}\tag{3}
$$

Since a bigger store is expected to sell more, we say a product j sells a large quantity in store i if $[ Z - Q _ { i , j } -$ $Z - T _ { i } \geq x ]$ , and a small quantity if $[ Z - Q _ { i , j } - Z -$ $T _ { i } \leq - x ]$ . Otherwise, it is a medium quantity. Here, x is the quantity deviation threshold, and we can determine the value of x at our discretion.

By comparing the sales figures for the current month with the previous figures, a cut off point can be devised: thus, if it increased more than x%, then we mark it as increased, but a decrease of more than x%, would be flagged as a decrease. Otherwise, it is the same.

Fig. 1 depicts the complete processes, with the gray boxes as the final output of the semantic terms. The process of pre-computation can be controlled by a trigger mechanism so that computation is made periodically or driven by events. Usually, such pre-computation processes are scheduled to run at midnight to limit any effect on normal operations.

## 5. The algorithms

After finishing the pre-computation, the quantitative data, such as total-quantity-sold and total-income, are transformed into the corresponding semantic terms. For price, two attributes, price standards and price variation, are derived. For sold-quantity, we also derive two attributes, quantity volume and quantity variation. For the store’s turnover, turnover variation is the attribute. Therefore, the original database has been transformed into two tables.

![](/api/attachments/GQB44BBE/fulltext/images/1cc86f6aada5dd5abbea5cd5580626820b4d072a8bfa3860662f15de5f721a22.jpg)  
Fig. 1. The chart to show how the data are pre-computed.

Table 1 (Store, Product, Year-Month, Price-Standard, Price-Variation, Quantity-Volume, Quantity-Variation).

Table 2 (Store, Year-Month, Turnover-Variation).

In these tables, we use an H to denote a high price, large quantity, or increased variation. Similarly, L is used to represent a low price, small quantity, or decreased variation. M is for a medium price, medium quantity, or no variation. To make the database more efficient, we used the events PS, PV, Q, QV, and TV to represent, respectively, Price-Standard, Price-Variation, Quantity-Volume, Quantity-Variation, and Turnover-Variation. Table 1 can be further transformed into

Table 3, which complies with the conventional transaction structure.

Table 3 (Store, Product, Year-Month, {(Event, Event-value)}).

Here, (Event, Event-value) means that the Event with its Event-value occurred. Since many events may happen in a single record, we use the symbols { } to denote ‘‘a set of occurred events’’. For example, (S-1, P-1, 1999-July, {(PS, H), (PV, H), (Q, L), (QV, L)}) means that store S-1 sold product P-1 at a high price but in a small quantity in July 1999 and that, compared to last month, its price rose but its quantity decreased. Similarly, (S-2, P-1, 1999-July, {(PS, M), (PV, M), (Q, M), (QV, L)}) indicates that store S-2 sold product P-1 at a medium price and in medium quantity in July 1999 and though there is no price variation, its quantity is less than that of the previous month.

By viewing a set of events as a set of purchased items, each record can be viewed as a traditional transaction record. Therefore, the known algorithms for mining association rules in the traditional transaction database can be applied to find semantic rules. After examining the format of Table 3, however, we found that it required more aggregations and transformations before we could apply the existing algorithms to get the semantic rules. Thus, we built a table that can generate the product rules by directly applying the existing mining algorithms.

Create Table 4 (Store, Year-Month, {(Product, Event, Event-value)})

Select Store, Year-Month, {(Product, Event, Event-value)}

From Table 3 (Store, Product, Year-Month, {(Event, Event-value)})

Group by Store, Year-Month

An example in Table 4 could be (S-1, 1999-July, {(P-1, PS, H), (P-1, PV, H), (P-1, Q, L), . . .}). Since there is a concept hierarchy along product dimensions (i.e. type, class, and category), and thus, the table can be further generalized into:

Table 4<sup>0</sup> (Store, Year-Month, {(Type or Class or Category, Event, Event-value)}).

Thus, we can generate not only the product rules but also the semantic association rules between higher concepts. Therefore, we can generate product rules on four different levels. An example is ‘‘Almarai low-fat fresh milk ! milk ! dairy ! food’’. An example of a higher-level rule may be: (milk’s price is low ! bread’s quantity is increased).

Since each record plays the same role as a transaction in a conventional transactional database, the derivation of large item sets and association rules can all be made by applying the existing algorithms.

Next, to generate store rules, we built a subsequent table from Table 3:

Create Table 5 (Year-Month, {(Store,

Select Year-Month, {(Store, Product, Event, Event-value)}

From Table 3 (Store, Product, Year-Month, {(Event, Event-value)})

As an example, an entry in Table 5 could be (1999- July, {(S-1, P-1, PS, H), (S-1, P-1, PV, H), (S-1, P-1,

Q, L), . . .}). Thus, the store rules can be derived by directly applying the existing algorithms for mining association rules.

Our next problem was to derive the company rules. Since the concept ‘‘store’’ is more specific than ‘‘company’’, we could generalize Table 5 into Table 6, from which the company rules can be discovered by using existing mining methods.

Table 6 (Year-Month, {(Company, Product, Event, Event-value)}).

But there is a pitfall lying in wait. Here, a company usually has many stores. Because of this one-to-many mapping, it is possible that the values from stores in the same company may contradict one another. For example, company C-1 has four stores S-1, S-2, etc. and they have the following events for product P-1: (S-1, P-1, Q, H), (S-2, P-1, Q, M), (S-3, P-1, Q, H) and (S-4, P-1, Q, L). What is the most appropriate semantic value that can be assigned to the quantity of company C-1? We decided to use the following index:

$$
I _ {\mathrm{c}} = N _ {\mathrm{H}} - N _ {\mathrm{L}}\tag{4}
$$

where $N _ { \mathrm { H } }$ is the number of stores in company $\cdot _ { \mathrm { c } } \cdot$ whose event-values are H, and similarly $N _ { \mathrm { L } }$ with event-values L. Then, let N denote the total number of stores in company $\cdot _ { \mathrm { c } } \cdot$ . We then define the event-value of company $\cdot _ { \mathrm { c } } \cdot$ according to the following formula:

$$
\text { event - value } = \left\{ \begin{array}{l l} \mathrm{H}, & \text { if } I _ {\mathrm{c}} \geq x \times N \\ \mathrm{L}, & \text { if } I _ {\mathrm{c}} \leq - 1 \times x \times N \\ \mathrm{M}, & \text { otherwise } \end{array} \right.\tag{5}
$$

In this formula, x is a real value between 1 and 0, and its value must be set at the discretion of the user. By performing this transformation, each event of each product in each company has one value. Therefore, the traditional mining algorithms can be applied again to derive the company rules.

Finally, our last problem was in deriving the turnover rules. To this end, we built Table 7 from Table 2 as follows:

Create Table 7 (Year-Month, {(Store, Turnover-Variation)})

Select Year-Month, {(Store, Turnover-Variation)}

From Table 2 (Store, Year-Month, Turnover-Variation)

Group by Year-Month

An example record in Table 7 would be: (1999-July, {(S-1, H), (S-2, H), (S-3, L), . . .}). This means that stores S-1 and S-2 sold more in July 1999, but store S-3 sold less in the same period. Obviously, the turnover rules can be derived by directly applying the existing algorithms for mining association rules.

## 6. System flowchart and components

The system we built is intended to be used in Taiwan, therefore, all its interfaces are designed in

Chinese. The interfaces described, are thus, translations of the original Chinese version.

Fig. 2 is a flowchart of the system. The major steps in using the system are as follows.

(1) Select the kind of rules of interest.

(2) Specify the range of data from which knowledge will be retrieved.

(3) Specify the rule format so that only those complying with this meta-pattern will be considered.

(4) Set the mining parameters.

![](/api/attachments/GQB44BBE/fulltext/images/c47f8dbda0478aad852e4192e6594776331648d042a07a3c1f058ce1e91af190.jpg)  
Fig. 2. The system flowchart.

![](/api/attachments/GQB44BBE/fulltext/images/e60e4b7dc30ae2632d269bf908f37c87a93d533c96751c8d400df9761b47a47a.jpg)  
Fig. 3. Defining the data range for finding product rules.

(5) Start the execution of the mining algorithm. There is an implicit post-processing step that is unknown to the user. The aim of this step is to remove rules that hold no interest for them.

(6) Display the discovered rules.

Fig. 3 shows the interface used when specifying the data range for finding product rules. Two things should be specified: those stores to be placed in consideration (designated by listing the store names or including those located in a certain city by specifying the city name and assigning ‘‘All’’, etc.) and the time range.

The interfaces dealing with the store rules and turnover rules are identical to Fig. 3 and therefore not shown. Fig. 4 shows the interface in specifying the data range for finding company rules. Since a retail company is usually found in many regions, we cannot specify its data range by geographical attributes. Therefore, we request users to list all companies that must be included.

Fig. 5 allows users to specify the maximum number of items on the left-hand side as well as the right-hand side. For each item on both sides, we can remove any restrictions by assigning ‘‘All’’ to all the field, or we can restrict it by specifying the category in which it belongs, the class in which it belongs, as well as its type or product name. This allows a user to list only those rules that are valuable and interesting.

Fig. 6 shows how to restrict the rule format for store rules. Since an item in the store rules involves both the store name and the product name, the system asks a user to specify a store and product. The store is designated by its district, city, or store name, and the product is specified in the same way as previously. Finally, we omitted the interfaces for specifying the rule formats of turnover rules and company rules, because they are similar to those for store rules or product rules.

Before running the mining algorithm for a product rule, there are a few parameters that need to be set (Fig. 1). The first two are the minimum support and confidence thresholds. Next, the user must specify the event types that occur in the rules: there are four which specify the price standard, price variation, quantity volume, and quantity variation. If price standards are checked, then the generated rules will contain the events related to price standards. Next, two parameters can be used to set the number of standard deviations away from the average that defines high (low) price or a large (small) quantity. Finally, the last two parameters define percentage of increase (decrease) over the last month is to be called an ‘‘increased’’ (‘‘decreased’’) price or ‘‘increased’’ (‘‘decreased’’) sales quantity. The interfaces for setting parameters of the other rules are all similar and therefore not shown (Fig. 7).

![](/api/attachments/GQB44BBE/fulltext/images/af3b385eb02fdcb9437bff9d7ccd81e0470e8a21bb7d68e644ed10955e70ed90.jpg)  
Fig. 4. Defining the data range for finding company rules.

![](/api/attachments/GQB44BBE/fulltext/images/908ef126c2382ed1ae3b5d51a385004721b28173d820e3924b0569b2c98eca26.jpg)  
Fig. 5. Specifying the rule format in generating product rules.

![](/api/attachments/GQB44BBE/fulltext/images/e503ee8dea5fc30fb91b33faa94a53f7dbc0df6823a19858a13f1a4036218e88.jpg)  
Fig. 6. Specifying the rule format in generating store rules.

![](/api/attachments/GQB44BBE/fulltext/images/59ec3c970874d52a23bdc436f36810f6f24acbbe2bcf11ff0e0d84381403751e.jpg)  
Fig. 7. Setting the parameters before running the mining algorithm.

After executing the algorithm for generating association rules, we have a post-processing step to remove any uninteresting rules. This is still an open research problem, and we do not mean to imply that it is an easy task. We remove those rules that are obviously redun dant: any rule that is already implied by another, more general one and any whose right-hand side is implied by other rules with the same left-hand side.

## 7. Conclusion

Existing data mining methods can help retailers discover customers’ purchasing behavior for a single enterprise. Valuable inter-organizational knowledge is still missing. For retail chains with small or moderate market share, analysis may reveal only a small portion of the consumers’ behavior, decreasing the effectiveness of their management decisions. To resolve these problems, an alliance was formed to share POS information across enterprises. Unfortunately, due to the competitive nature among these firms, only aggregated POS data was provided. This causes some new problems.

We have resolved most of the difficulties by designing semantic association rules, transforming the quantitative data into semantic data and developing algorithms for mining knowledge. Finally, we developed a prototype system.

There are some managerial implications. The new mining method opens an avenue to new inter-organi zational retailing knowledge. By sharing such knowl edge, retailers can build partnerships and improve relationships with their supply chain partners. Finally, it also opens an avenue for small and medium retail chains to discover market knowledge and examine the landscape of the retail markets.

## Acknowledgements

This research is supported in part by the Computer and Communication Research Labs of Industrial Technology Research Institute under grant N4-89008.

## References

[1] R. Agrawal, R. Srikant, Fast algorithms for mining association rules, in: Proceedings of the 20th International Conference on Very Large Databases, Santiago, Chile, 1994.

[2] I. Bose, R.K. Mahapatra, Business data mining—a machine learning perspective, Information & Management 39 (3), 2001, pp. 211–225.

[3] M.S. Chen, J. Han, P.S. Yu, Data mining: an overview from a database perspective, IEEE Transactions on Knowledge and Data Engineering 8 (6), 1996, pp. 866–883.

[4] D. Cheung, S.D. Lee, B. Kao, A general incremental technique for maintaining discovered association rules, in: Proceedings of the 5th International Conference On Database Systems For Advanced Applications, Melbourne, Australia, 1997.

[5] A. Feelders, H. Daniels, M. Holsheimer, Methodological and practical aspects of data mining, Information & Management 37 (5), 2000, pp. 271–281.

[6] Y. Fu, J. Han, Meta-rule-guided mining of association rules in relational databases, in: Proceedings of the 1995 International Workshop on Knowledge Discovery and Deductive and Object-Oriented Databases, Singapore, 1995, pp. 39– 46.

[7] J. Han, Y. Fu, Mining multiple-level association rules in large databases, IEEE Transactions on Knowledge and Data Engineering 11 (5), 1999, pp. 798–805.

[8] J. Han, L.V.S. Lakshmanan, R.T. Ng, Constraint-based, multidimensional data mining, Computer 32 (8), 1999, pp. 46–50.

[9] J. Han, J. Pei, Y. Yin, Mining frequent patterns without candidate generation, in: Proceedings of the 2000 ACM-SIGMOD International Conference on Management of Data, Dallas, TX, 2000.

[10] S.C. Hui, G. Jha, Data mining for customer service support, Information & Management 38 (1), 2001, pp. 1–13.

[11] B. Ozden, S. Ramaswamy, A. Silberschatz, Cyclic association rules, in: Proceedings of the International Conference on Data Engineering, 1998.

[12] B. Padmanabhan, A. Tuzhilin, Unexpectedness as a measure of interestingness in knowledge discovery, Decision Support Systems 27 (3), 1999, pp. 303–318.

[13] R. Rastogi, K. Shim, Mining optimized association rules with categorical and numeric attributes, in: Proceedings of the 14th International Conference on IEEE Data Engineering, Orlando, FL, 1998.

[14] R. Srikant, R. Agrawal, Mining quantitative association rules in large relational tables, in: Proceedings of the ACM-

SIGMOD 1996 Conference on Management of Data, Montreal, Canada, 1996.

[15] R. Srikant, R. Agrawal, Mining generalized association rules, in: Proceedings of the 21st International Conference on Very Large Databases, Zurich, Switzerland, 1995.

![](/api/attachments/GQB44BBE/fulltext/images/02b70617828eb7de8d3000fd917ec53fab0d54afa9219087e1664e909f172f4b.jpg)  
Qi-Yuan Lin received the MS degree in information management from National Central University, Chung-Li, Taiwan. Currently, he serves in the army of Taiwan for a period of 2 years to fulfill the military obligation. His research interests include data warehousing, information systems and EC technologies.

![](/api/attachments/GQB44BBE/fulltext/images/12bd76652b575ce2c412528c49d3c668b68377bd027db737daf55cc2b84466a5.jpg)

Yen-Liang Chen is a professor in the Department of Information Management, National Central University, Chung-Li, Taiwan. He received the BSc degree in industrial management from National Cheng Kung University, Tainan, Taiwan and the MS degree in industrial engineering from National Tsing Hua University, Hsinchu, Taiwan. He received his PhD degree in computer science from National Tsing Hua Uni versity, Hsinchu, Taiwan. His current research interests include operations research, data mining and data warehousing.

![](/api/attachments/GQB44BBE/fulltext/images/e07e7bf446d8cb33d1114e5105f97174aaa25f512e19628e36a19133cd994efe.jpg)  
Jiah-Shing Chen is an associate professor in the Department of Information Management at National Central University, Taiwan. He received his PhD degree in computer science from State University of New York at Buffalo in 1992. His current research interests include artificial intelligence, intelligent information systems, soft computing, data mining and e-commerce.

![](/api/attachments/GQB44BBE/fulltext/images/43ba107f8a87fffc3320de438f7a4116be572aeb9a197972243b15c32963b5a4.jpg)

Yu-Chen Chen is an assistant professor in the Department of Business Administration at Soochow University, Taiwan. He received a MSc in industrial engineering in 1984 at National Tsing-Hua University, Taiwan, and a PhD in information management in 1999 from National Central University, Taiwan. He worked in Institute for Information Industry as a project manager from 1984 to 1998. His current interests

include knowledge management, IT adoption and implementation, electronic commerce, and supply chain management.
