---
otero_id: 1158
otero_key: "7S4E6Q5F"
title: "Comprehensive data warehouse exploration with qualified association-rule mining"
authors: "Nenad Jukić; Svetlozar Nestorov"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.07.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Comprehensive data warehouse exploration with qualified association-rule mining

Nenad Jukic´ <sup>a,\*</sup>, Svetlozar Nestorov <sup>b,1</sup>

<sup>a</sup>School of Business Administration, Loyola University Chicago, 820 N. Michigan Avenue, Chicago, IL 60640, USA <sup>b</sup>Department of Computer Science, The University of Chicago, Chicago, IL, USA

Received 10 May 2004; received in revised form 9 July 2005; accepted 11 July 2005 Available online 11 August 2005

## Abstract

Data warehouses store data that explicitly and implicitly reflect customer patterns and trends, financial and business practices, strategies, know-how, and other valuable managerial information. In this paper, we suggest a novel way of acquiring more knowledge from corporate data warehouses. Association-rule mining, which captures co-occurrence patterns within data, has attracted considerable efforts from data warehousing researchers and practitioners alike. In this paper, we present a new data-mining method called qualified association rules. Qualified association rules capture correlations across the entire data warehouse, not just over an extracted and transformed portion of the data that is required when a standard datamining tool is used.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Data warehouse; Data mining; Association rules; Dimensional model; Database systems; Knowledge discovery

## 1. Introduction

Data mining is defined as a process whose objective is to identify valid, novel, potentially useful and understandable correlations and patterns in existing data, using a broad spectrum of formalisms and techniques [9,23]. Mining transactional (operational) databases, containing data related to current day-to-day organizational activities could be of limited use in certain situations. However, the most appropriate and fertile source of data for meaningful and effective data mining is the corporate data warehouse, which contains all the information from the operational data sources that has analytical value. This information is integrated from multiple operational (and external) sources, it usually reflects substantially longer history than the data in operational sources, and it is structured specifically for analytical purposes.

The data stored in the data warehouse captures many different aspects of the business process across various functional areas such as manufacturing, distribution, sales, and marketing. This data explicitly and implicitly reflects customer patterns and trends, business practices, organizational strategies, financial conditions, know-how, and other knowledge of potentially great value to the organization.

Unfortunately, many organizations often underutilize their already constructed data warehouses [12,13]. While some information and facts can be gleaned from the data warehouse directly, through the utilization of standard on-line analytical processing (OLAP), much more remains hidden as implicit patterns and trends. The standard OLAP tools have been performing well their primary reporting function where the criteria for aggregating and presenting data are specified explicitly and ahead of time. However, it is the discovery of information based on implicit and previously unknown patterns that often yields important insights into the business and its customers, and may lead to unlocking hidden potential of already collected information. Such discoveries require utilization of data mining methods.

One of the most important and successful data mining methods for finding new patterns and correlations is association-rule mining. Typically, if an organization wants to employ association-rule mining on their data warehouse data, it has to use a separate datamining tool. Before the analysis is to be performed, the data must be retrieved from the database repository that stores the data warehouse, transformed to fit the requirements of the data-mining tool, and then stored into a separate repository. This is often a cumbersome and time-consuming process. In this paper we describe a direct approach to association-rule data mining within data warehouses that utilizes the query processing power of the data warehouse itself without using a separate data mining tool.

In addition, our new approach is designed to answer a variety of questions based on the entire set of data stored in the data warehouse, in contrast to the regular association-rule methods which are more suited for mining selected portions of the data warehouse. As we will show, the answers facilitated by our approach have a potential to greatly improve the insight and the actionability of the discovered knowledge.

This paper is organized as follows: in Section 2 we describe the concept of association-rule data mining and give an overview of the current limitations of association-rule data mining practices for data warehouses. Section 3 is the focal point of the paper. In it we first introduce and define the concept of qualified association rules. In 3.1 we discuss how qualified association rules broaden the scope and actionability of the discovered knowledge. In 3.2 we describe why existing methods cannot be feasibly used to find qualified association rules. In 3.3 3.4 and 3.5 we offer details of our own method for finding qualified association rules. In Section 4 we describe an illustrative experimental performance study of mining real world data that uses the new method we introduced. And finally, in Section 5 we offer conclusions.

## 2. Association-rule data mining in data warehouses

The standard association-rule mining [1,2] discovers correlations among items within transactions. The prototypical example of utilizing association-rule mining is determining what products are found together in a basket at a checkout line at the supermarket; hence the often-used term: market basket analysis [4]. The correlations are expressed in the following form:

Transactions that contain X are likely to contain Y as well noted as X Y Y, where X and Y represent sets of transaction items. There are two important quantities measured for every association rule: support and confidence. The support is the fraction of transactions that contain both X and Y items. The confidence is the fraction of transactions containing items X, which also contain items Y. Intuitively, the support measures the significance of the rule, so we are interested in rules with relatively high support. The confidence measures the strength of the correlation, so rules with low confidence are not meaningful, even if their support is high. A rule in this context is the relationship among transaction items with enough support and confidence.

The standard association rule mining process employs the basic a-priori algorithm [1,3] for finding sets of items with high support (often called frequent itemsets). The crux of the a-priori approach is the observation that a set of items I can be frequent only if all proper subsets sub(I) are also frequent in recorded transactions. Based on this observation, apriori applies step-wise pruning to the sets of items that need to be counted, starting by eliminating single items that are infrequent. For example, if we are looking for all sets of items (pairs, triples, etc. . .) that appear together in at least s transactions, we can start by finding those items that by themselves appear in at least s transactions. All items that do not appear on their own in at least s transactions are pruned out.

In practice, the discovery of association rules has two phases. In the first phase, all frequent itemsets are discovered using the a-priori algorithm. In the second phase, the association rules among the frequent itemsets with high confidence are constructed. Since the computational cost of the first phase dominates the total computational cost [1], association-rule mining is often defined as the following question pertaining to transactional data, where each transaction contains a set of items:

What items appear frequently together in transactions?

Association-rule data mining has drawn a considerable amount of attention from researchers in the last decade. Much of the new work focuses on expanding the extent of association-rule mining, such as mining generalized rules (i.e. when transaction items belong to certain types or groups, generalized rules find associations among such types or groups) [14,24]; mining correlations and casual structures, which finds generalized rules based on implicit correlations among items, while taking into consideration both the presence and the absence of an item in a transaction [6,22]; finding association rules for numeric attributes, where association rules, in addition to Boolean conditions (i.e. item present in the transactions), may consider a numeric condition (e.g. an item that has a numeric value, must have a value within a certain range) [10,11]; finding associations among items occurring in separate transactions [17,19,27]; etc.

In this paper we introduce qualified association rules as a way of extending the scope of association rule mining. Our method extends the scope of association rule mining to include multiple database relations (tables), in a way that was not previously feasible. This approach is designed to provide a real addition to the value of collected organizational information and is applicable in a host of real world situations, as we will illustrate throughout this paper. Many of the previously proposed association-rule extensions are either applicable to a relatively narrow set of problems, or represent a purely theoretical advance. In addition, they also often require computational resources that may be unrealistic for most of the potential organizational users. In contrast, our proposed method is both broadly applicable and highly practical from the implementation and utilization points of view.

Dimensional modeling [16], which is the most prevalent technique for modeling data warehouses, organizes tables into fact tables, containing basic quantitative measurements of an organizational activity under consideration, and dimension tables that provide descriptions of the facts being stored. Dimension tables and their attributes are chosen for their ability to contribute to the analysis of the facts being stored in the fact tables.

The data model that is produced by the dimensional modeling method is known as a star-schema [7] (or a star-schema extension such as snowflake or constellation). Fig. 1 shows a simple star-schema model of a data warehouse for a retail company.

The fact table contains the sale figures for each sale transaction and the foreign keys that connect it to the four dimensions: Product, Customer, Location, and Calendar.

Consider the data warehouse depicted by Fig. 1. The standard association-rule mining question for this environment would be:

What products are frequently bought together?

This question examines the fact table as it relates to the product dimension only. A typical data warehouse, however, has multiple dimensions, which are ignored by the above single-dimension question, as illustrated by Fig. 2.

![](/api/attachments/7S4E6Q5F/fulltext/images/d3519c5408e4c4cae5b604e09483700dc3f142a15e4adb2408c5f39cf870484f.jpg)  
Fig. 1. Example retail company star-schema.

For example, an analyst at the corporate headquarters may ask the following question:

What products are frequently bought together in a particular region and during a particular month?

This question requires examination of multiple dimensions of the fact table. Standard associationrule mining approach would not find the answer to this question directly, because it only explores the fact table with its relationship to the dimension table that contains transaction-items (in this case Product), while the other dimension tables (the non-item dimensions) are not considered. In fact, by applying standard algorithms directly, we may not discover any association rules in situations when there are several meaningful associations that involve multiple dimensions. The following example illustrates an extreme case scenario of this situation.

Example 1. A major retail chain operates stores in two regions: South and North; and divides the year into two seasons: Winter and Summer. The retail chain sells hundreds of different products including sleeping bags and tents. Table 1 shows the number of transactions for each region in each season as well as the percentage of transactions that involved a sleeping bag, a tent, or both.

Suppose we are looking for association rules with 0.5% support and 50% confidence. Let’s first consider the transactions in all regions and all seasons. There are 500 thousand transactions and only 10 thousand of them involve both a sleeping bag and a tent, so the support of the pair of items is 2% (greater than 0.5%). There are 25 thousand transactions that involve sleeping bags, 23 thousand transactions that involve tents. Therefore the confidence of sleeping bag Y tent is 40% and the confidence of tent Y sleeping bag is 43%. Thus, no association rule involving sleeping bags and tents will be discovered. Let’s consider the transactions in the North region separately. In the North sleeping bags appear in 12 thousand transactions, tents appear in 9 thousand transactions, and both sleeping bags and tents appear together in 4 thousand transactions. The support for both items is 0.8% (greater than 0.5%) but the confidence for rules involving sleeping bag and tent are 33% and 44% (both less than 50%). Thus, no association rule involving bags and tents will be discovered. Similarly, no rules involving both sleeping bag and tent will be discovered in the South, and no associations will be discovered between sleeping bags and tents when we consider all the transactions in each season (Summer and Winter) separately.

![](/api/attachments/7S4E6Q5F/fulltext/images/4a32e695f6b9a1b6b251adbaf1b17fff6e73eb7f1324ea42e328a50ec1f0127f.jpg)  
Fig. 2. Association-rule data mining scope for the example retail company star schema.

Table 1  
Transaction statistics (in thousands) for Example 1

<table><tr><td></td><td>Total</td><td>Bags</td><td>Tents</td><td>Both</td></tr><tr><td colspan="5">North</td></tr><tr><td>Winter</td><td>150</td><td>8</td><td>2</td><td>1</td></tr><tr><td>Summer</td><td>100</td><td>4</td><td>7</td><td>3</td></tr><tr><td colspan="5">South</td></tr><tr><td>Winter</td><td>100</td><td>4</td><td>8</td><td>3</td></tr><tr><td>Summer</td><td>150</td><td>9</td><td>6</td><td>3</td></tr></table>

These conclusions (no association rules) are rather surprising because if each combination of region and season were considered separately the following association rules would be discovered:

n sleeping bag Y tent; in the North during the Summer (sup =0.60%, conf=75%)

n sleeping bag Y tent; in the South during the Winter (sup = 0.60%, conf = 75%)

n tent Y sleeping bag; in the South during the Summer (sup =0.60%, conf=50%)

Standard association rule mining cannot discover these association rules directly, because it does not account for non-item dimensions.

In addition to the possibility of suppressing some of the existing relevant rules (as illustrated by Example 1), another type of problem can arise when multiple dimensions are not considered: an overabundance of discovered rules may hide a smaller number of meaningful rules. Example 2 illustrates an extreme case scenario of this situation.

Example 2. Another major retail chain also operates stores in two regions: South and North; and divides the year into two seasons: Winter and Summer. This retail chain sells hundreds of different products including Product A, Product B, and Product C. Table 2 shows the number of transactions for each region in each season; the number of transactions that involved Product A, Product B, Product C; as well as the number of transactions that involved Product A and Product B together, Product A and Product C together, and Product B and Product C together.

Suppose we are looking for association rules with 0.50% support and 50% confidence. If we consider the transactions in all regions and all seasons we will discover that every possible association rule involving two items satisfies the threshold, as shown below:

$$
\text {■ Product A} \rightarrow \text {Product B} (\sup = 1.00\% , \text {conf} = 55 \%)
$$

n Product B Y Product A (sup = 1.00%, conf=67%)

n Product A Y Product C (sup = 1.00%, conf = 55%)

n Product C Y Product A (sup = 1.00%, conf = 50%)

Table 2  
Transaction statistics (in thousands) for Example 2

<table><tr><td></td><td>Total</td><td>A</td><td>B</td><td>C</td><td>A and B</td><td>A and C</td><td>B and C</td></tr><tr><td colspan="8">North</td></tr><tr><td>Winter</td><td>200</td><td>2</td><td>3</td><td>3</td><td>2</td><td>2</td><td>2</td></tr><tr><td>Summer</td><td>100</td><td>1</td><td>2</td><td>4</td><td>1</td><td>0</td><td>2</td></tr><tr><td colspan="8">South</td></tr><tr><td>Winter</td><td>100</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Summer</td><td>200</td><td>7</td><td>3</td><td>4</td><td>2</td><td>3</td><td>1</td></tr></table>

$$
\begin{array}{l}\text {■ Product B} \rightarrow \text {Product C} (\sup = 1.00 \%,\\\text {conf} = 67 \%)\end{array}
$$

$$
\begin{array}{l}\text {■ Product C} \rightarrow \text {Product B} (\sup = 1.00\% ,\\\text {conf} = 50\%).\end{array}
$$

In this example, any combination of two of the three products is correlated. Thus, it is difficult to make any conclusions, reach any decisions, and take any actions. This problem occurs when a mining process produces a very large number of rules, thus proving to be of little value to the user. However if we consider each region and season separately we will find only one rule within the given support and confidence limit:

n Product C Y Product A; in the South during the Summer $( \mathrm { s u p } ^ { 3 } = 0 . 5 0 \%$ , conf = 75%).

Isolating this rule may provide valuable additional information to the user. The above two examples illustrate two types of situations in which association rules that consider both item-related dimension (e.g. Product) and non-item related dimensions (e.g. Region, Session) add new insight into the nature of data to the user. Section 3 describes the method that enables such discoveries.

## 2.1. Related work

Recent work on mining the data warehouse has explored several approaches from different perspectives. Here we give a brief overview.

Both Refs. [15,21] extend OLAP techniques by finding patterns in the form of summaries or trends among certain cells of the data cube. While both papers examine multiple dimensions of the data warehouse, neither discovers correlations among multiple values of the same dimension. For example, the techniques detailed in Ref. [15] can discover that <sup>b</sup>the average number of sales for all camping products combined (tents and bags) is the same during the Winter in the South and during the Summer in the North.<sup>Q</sup> However, their framework does not handle association rules involving multiple products bought in the same transactions, e.g. <sup>b</sup>number of transactions involving both tents and bags is the same during the Summer in the North and for all seasons in the South<sup>Q</sup>. The framework presented in Ref. [21] can find summarized rules associated with a single item. For example, it can reduce the fact that <sup>b</sup>during the Winter the number of tents sold in the South is equal or greater than the number sold in the North<sup>Q</sup> to the rule that <sup>b</sup>during the Winter the number of sales for all camping products in the South is equal or greater than the number of sales in the North<sup>Q</sup>, if such a reduction holds. However, rules about multiple products sold in the same transaction lie beyond this framework.

The focus of Ref. [25] is on finding partitions of attribute values that result in interesting correlations. In contrast to our work, quantitative rules involve at most one value or one value range for each attribute. For example, <sup>b</sup>transactions involving a tent in the North are likely to occur during the Summer <sup>Q</sup> is a quantified rule, whereas <sup>b</sup>transactions involving a tent in the North are likely to involve a bag <sup>Q</sup> is a qualified rule that falls outside of the scope of quantified rules because it involves two values of the Product dimension.

Generalized association rules [24] and multiplelevel association rules [8] capture correlations among attribute values, possibly at different levels, within the same dimensional hierarchy but not across multiple dimensions. For example, <sup>b</sup>transactions involving sporting goods tend to involve sunscreen<sup>Q</sup> is within the framework of generalized rules and multi-level rules, while the qualified rule <sup>b</sup>transaction involving sporting goods tend to involve sunscreen in the summer<sup>Q</sup> is beyond their scope.

A precursor to qualified association rules is discussed in Ref. [18] with the focus on dealing with aggregate rather than transactional data.

## 3. Qualified association rules

Standard association rules express correlations between values of a single dimension of the star schema. However, as illustrated by Examples 1 and 2, values of the other dimensions may also hold important correlations. For example, some associations become evident only when multiple dimensions are involved. In Example 1, sleeping bags and tents appear uncorrelated in the sales data as a whole, or even when the data is considered separately by region or season. Yet, several association rules are discovered if the focus is on the data for a particular region during a particular season. One such rule is <sup>b</sup>sleeping bag Y tent<sup>Q</sup> for the transactions that occurred in the North region during the Summer season. This association rule involves more than just a pair of products; it also involves the location as well as the time period of the transaction. In order to capture this additional information, we can augment the association rule notation as illustrated by the following qualified association rule:

sleeping bag Y tent½region ¼ North;

season ¼ Summer:

We define qualified association rule as follows: Let T be a data warehouse where X and Y are sets of values of the item-dimension. Let $\mathcal { Q }$ be a set of equalities assigning values to attributes of other (nonitem) dimensions of T. Then, X Y Y [ Q] is a qualified association rule with the following interpretation: Transactions that satisfy $\boldsymbol { Q }$ and contain X are likely to contain Y.

For a more detailed definition consider a star schema with $d$ dimensions. Let the fact table be $F$ and the dimensions be $D _ { 0 } . . . D _ { d }$ . The schema of dimension table $D _ { i }$ consists of a key $k _ { i }$ and other attributes. The schema of the fact table F contains the keys for all dimensions, $k _ { 0 } . . . k _ { d } ,$ and a transaction id attribute tid.

Without loss of generality, we can assume that the item dimension is $D _ { 0 } ,$ so the set of all items is $d o m a i n ( k _ { 0 } )$ . For all other dimensions $D _ { j }$ we can assert that the functional dependency $t i d \longrightarrow k _ { j }$ holds for F (i.e. each value of tid in the fact table determines one and only one vale of $\cdot _ { k _ { j } }$ in the non-item dimension table $D _ { j } )$

We define a qualifier to be a set of equalities of the form: attr = value where attr is a non-key attribute of any of the non-item dimensions and value is a constant. For example, {region = North} is a qualifier and so is {season = Summer; region =South}.

We define a valid qualifier to be a qualifier that contains at most one equality for each non-item dimension. Examples of valid qualifiers are {season= Summer; region = South} and {region =South; gender = Male}; while examples of invalid qualifiers are: {region= North; region = South} and {season = Summer; month = July}. In this paper, we only consider valid qualifiers, and for brevity, refer to them as qualifiers.

Now, we define a qualified association rule:

$$
X \to Y [ Q ]
$$

where X and Y are itemsets $( X \subset d o m a i n ( k _ { O } ) ; Y \subset$ domain $\left( k _ { \theta } \right) )$ and Q is a qualifier. For example,

sleeping bagYtent½region ¼ North;

season ¼ Summer

is a qualified association rule. The intuitive interpretation of this rule is that if a transaction includes a sleeping bag in the North region during the Summer season, then the transaction is likely to also include a tent.

Before defining the support and confidence of a qualified association rule, we need to define the support of a qualified itemset. Let I be an itemset and Q a qualifier. Then, I[Q] is a qualified itemset. For example, {sleeping bag, tent} [region = North, season = Summer] is a qualified itemset. The s<sup>\_</sup>count of a qualified itemset I[Q], denoted as s<sup>\_</sup>count(I[Q]), is the number of transactions that contain the itemset and satisfy all equalities in Q.

Formally, support is defined as follows. Let $I { = } \left\{ e _ { 1 } ; . . . . , e _ { m } \right\}$ and $\mathcal { Q } = \{ a _ { 1 } { = } \nu _ { 1 } , \ldots , a _ { p } { = } \nu _ { p } \}$ . Without loss of generality we can assume that $a _ { i }$ is an attribute of $D _ { i }$ . Then, s<sup>\_</sup>count(I[Q]) is equal to the size of the following set:

$$
\begin{array}{c} S = \big \{t | \exists f _ {i} \in F; i = 1.. m; d _ {j} \in D _ {j}; j = 1.. p; f _ {i} [ t i d ] \\ = t; f _ {i} [ k _ {0} ] = e _ {i}; f _ {i} \big [ k _ {j} \big ] = d _ {j} \big [ k _ {j} \big ]; d j \big [ a _ {j} \big ] = v _ {j} \big \}. \end{array}
$$

The set S consists of all transaction IDs t, for which there are m tuples (i.e. records or table rows) in F that satisfy the following conditions:

n all m tuples have t as their tid.

n all m tuples agree on all dimension key attributes except $k _ { 0 } .$

n for every attribute $k _ { j } ,$ its single value in all m tuples is the value of attribute $k _ { j }$ of a tuple in dimension table $D _ { j }$ whose value of attribute $a _ { j }$ is $\mathrm { v } _ { j } .$

These conditions are illustrated in Fig. 3.

For example, for the qualified itemset $I { = } \{ b a g , $ $t e n t \} [ Q ]$ , the set S would consist of all transaction IDs representing transactions that satisfy the qualifying condition $\mathcal { Q } ,$ , for which there are 2 tuples (one for bag, one for tent) in the fact table that agree on all attributes except for $k _ { 0 }$ (attribute $k _ { 0 }$ points to bag for one tuple and to tent for the other). In other words, set S would capture transaction IDs of all transactions: (1) where bag and tent were sold together (2) which satisfy the qualifying condition (e.g. within a particular region and season).

![](/api/attachments/7S4E6Q5F/fulltext/images/6ea7c068344c5b2974df93547c08a2d479f376928242169dc453c20999ecc933.jpg)  
Fig. 3. Definition of support for qualified itemsets.

Now, we can define the support and confidence of a qualified association rules as follows:

$$
s u p p o r t (X \to Y [ Q ]) = \frac {s \_ c o u n t ((X \cup Y) [ Q ])}{s \_ c o u n t (\emptyset [ \emptyset ])}
$$

$$
\text { confidence } (X \to Y [ Q ]) = \frac {s \_ c o u n t ((X \cup Y) [ Q ])}{s \_ c o u n t (X [ Q ])}
$$

Note that $s \_ c o u n t ( \emptyset [ \emptyset ] )$ is simply the number of transactions in the fact table F.

The support and confidence of the rules in G were computed using these definitions.

## 3.1. Discussion

While qualified association rules are natural extensions of standard association rules, they contain more detailed and diverse information which offer several distinct advantages.

First, the phenomenon that brings a qualified rule to existence can be explained more easily. In Example 2, standard association rule mining found the correlations between products A, B, and C within the specified confidence and support threshold for all sales.

However, only the qualified rule would give the explanation that, once regions and seasons are considered separately, the correlation of sales between products A, B, and C holds exclusively for products C and A in warm weather conditions (because the found qualified rule contains South region and Summer season).

Second, qualified rules tend to be local, in a sense of location or time, and thus more actionable. For example, it is much simpler to devise a marketing strategy for sleeping bags and tents that applies to a particular region during a particular season than a general strategy that applies to all regions during all seasons.

Third, for the same support threshold, the number of discovered qualified association rules is likely to be much smaller than the number of standard association rules. The reason is that qualified rules involve more attributes and thus transactions that support them fit a more detailed pattern than standard rules. Even though the overall number of qualified rules is likely to be much less than the number of standard rules, there may be some items that are involved only in qualified rules (as shown in Example 1). Intuitively, standard rules show associations of a coarser granularity while qualified rules show finer, more subtle associations.

Before we continue the discussion of qualified association rules, let us recall the process of standard association-rule mining. Given a set of transactions, and support and confidence thresholds (based on initial beliefs and intuition of the analyst), the process discovers association rules among items that have support and confidence higher than the chosen thresholds. With this setting, the only parameters that the analyst controls directly are the support and confidence thresholds. Very often the result of this mining process is one of two extremes. The number of discovered rules is either overwhelmingly large (tens of thousands) or very small (dozens) [28]. In both cases, the user has no other recourse but to revise the support and confidence and run the mining process again. As a post-processing step, the analyst may decide to focus on certain items, but that goes against the notion of mining and will be very inefficient; in fact, given an unlimited amount of time, the user may very well compute the support and confidence of the items involved in association rules directly using OLAP.

Since the mining process often takes hours [20], most users are not likely to continually refine the thresholds. Thus, the mining process is often seen as not particularly useful to non-technical users.

In contrast, the process of mining qualified association rules requires more input from the user and thus affords more control and lends itself to customization. Since qualified association rules involve attributes of non-item dimensions, the user needs to specify these attributes. For example, the user can ask for association rules that involve a region and a season in addition to products. Note that the user does not need to specify the particular values of the attributes. The actual values are discovered as part of the mining. This mining process differs from the one-sizefits-all approach for standard association rules. Different users can ask mining questions involving different attributes of the dimensional hierarchies. For example, a marketing executive who is interested in setting up a targeted marketing campaign can ask the following:

Find products bought frequently together by customers of a particular gender in a particular region.

A sample association rule discovered by this question may be: ice cream Y cereal (region = California, gender = female). Discovering that ice cream and cereal sell well together in California with female customers can facilitate creating a more focused and effective marketing campaign that is at the same time less costly (e.g. ads for ice cream and cereal can appear on consecutive pages of a local femaletargeted magazine).

On the other hand, a vice president in charge of distribution may ask the following:

Find products bought frequently together in a particular city during a particular month.

A sample association rule discovered by this question may be: sleeping bag Y tent (city = Oakland, month = May). Such a rule is of more value for managing and planning the supply-chain than the equivalent standard association rule since it clearly identifies the location and the time period (e.g. it can indicate that the shipping of sleeping bags and tents to certain stores should be synchronized, especially during certain time periods).

## 3.2. Mappings to standard association rules

Let us consider several ways in which we can try to map qualified rules to standard rules and attempt to mine for them in data warehouses by applying standard association-rule mining algorithms. In other words, let us examine if there is a feasible way to find qualified association rules in data warehouses by using currently existing methods (i.e. standard association rules mining) included with the standard mining tools.

The first mapping is based on considering each value of a qualifier as just another item and adding this item to the transaction. Thus, the problem of finding association rules with qualified attributes $a _ { i }$ of dimension $D _ { i }$ for $i = 1 , \ldots k$ can be converted to the problem of finding standard association rules by adding to each transaction $k$ new items: the values of $a _ { i } .$ The new set of all items becomes domain $( k _ { 0 } ) \cup ( \cup _ { i = 1 } ^ { k }$ $d o m a i n ( a _ { i } ) )$ . For a concrete example, consider a transaction that involved a sleeping bag and a tent and happened in the North region during the Summer season. After the mapping, the <sup>b</sup>new<sup>Q</sup> transaction will contain four items: sleeping bag, tent, North, and Summer.

There are several problems with this approach. Essentially, the process will compute all standard association rules for the given minimum support, all qualified rules, and other rules that are qualified by only a subset of the original qualifier. Thus, the majority of the found rules will not involve all qualified dimensions and must be filtered out at the end of the process. Furthermore, when mining qualified rules, the range of <sup>b</sup>appropriate<sup>Q</sup> minimum support values will be lower than the range for mining standard rules over the same data. By appropriate, we mean that the number of discovered rules is not too large and not too small. Consequently, a minimum support value that is <sup>b</sup>appropriate<sup>Q</sup> for qualified rules may not be <sup>b</sup>appropriate<sup>Q</sup> for standard rules. For such values, this approach will be very inefficient, since it generates all standard rules along with the qualified rules, while using the same support values. Using the same support threshold will make the number of discovered standard rules many times more than the number of qualified rules (as will be illustrated later in Section 4 that shows the results of experiments). Another shortcoming of this approach is that a mining algorithm will make no distinction between attribute values of item dimension and non-item dimension. Thus, the algorithm may try to combine incompatible items, e.g. North and South, as part of the candidate generation process. Recall the basic a-priori algorithm for finding frequent itemsets, employed by standard association rule mining. The first step of the a-priori algorithm, when applied to the first mapping, will find all frequent itemsets of size 1. It is likely that most dimension values will turn up frequent. The second step of a-priori, which is usually the most computationally intensive step, will generate a candidate set of pairs, $_ { \mathrm { C } 2 = \mathrm { L } 1 \times \mathrm { L } 1 }$ whose support will be counted (where L1 represents all frequent itemsets of size 1.) This candidate set C2 will include many impossible pairs formed by putting matching two values of the same dimension attribute (e.g. {Summer; Winter}). These shortcomings can be addressed by handling items and dimension attributes differently, which is in fact the very idea that motivates qualified association rules.

The second mapping of qualified to standard rules is based on expanding the definition of an item to be a combination of an item and qualified attributes. For example, (tent, South, Winter) will be an item different than the item (tent, South, Summer). The main problem with this approach is that the number of items is increased dramatically. The number of items will grow to:

$$
\left| \operatorname{domain} \left(k _ {0}\right) \right| \prod_ {i = 1} ^ {k} \left(\left| \operatorname{domain} \left(k _ {i}\right) \right|\right).
$$

The growth can be many orders of magnitude greater than the original number of items, which can make the process unmanageable. For example suppose we consider day<sup>\_</sup>of<sup>\_</sup>year and zip<sup>\_</sup>code attributes of non-item dimensions. Then the number of items will increase about 365 \* 42,000\~15 million times. Thus, if the number of items was 100,000 the new number of items will be 1.5 trillion. In addition to having to consider an enormously inflated number of items, mining algorithms will run into same problem of matching up incompatible items as described above.

The third mapping is based on partitioning the data according to the values of the qualified attributes, and finding standard association rules for each partition. For example, the data from Example 1 would be partitioned into 4 different sets, one for each of the 4 combinations of values for region and season. This approach is in fact feasible if fact tables can be prejoined with all of their dimensions and then loaded into a separate data mining tool, where the data can be re-partitioned for each query. While ad-hoc re-partitioning of the data on-demand (e.g. every time another set of qualified association rules is mined), may in fact be a feasible strategy for single fact table data-marts that contain relatively small amounts of data, this approach is simply not an option for most corporate data warehouses where fact tables can contain hundreds of millions or billions of records occupying terabytes of disk space. Even if we store separately the results of joining each fact table with all their related dimensions as a single table, the number of partitions in each such table may become too large and the startup cost of setting up each partition and running an algorithm on it would dominate the total cost. Furthermore, when this approach is applied within the data warehouse (i.e. directly on the fact and dimension tables), the run on each partition will access the entire data (reading only the blocks that contain data from the current partition will result in many random access disk reads that are slower than reading the entire data sequentially) unless the data happens to be partitioned physically along the qualified dimensions.

As we described here, none of the discussed approaches that involve applying standard association-rule mining directly, provide a practical and efficient solution for discovering qualified association rules in data warehouses. However, all three mappings emphasize the need for a new method that treats items and non-item dimension attributes differently. The principle of treating items and non-item dimension attributes differently is what underlines our definition of qualified association rules. In the remainder of this paper we present a framework and methodology for finding qualified association rules efficiently.

## 3.3. Framework—a-priori for qualified itemsets

For standard itemsets, the a-priori technique is straightforward. For any frequent itemset I, all of its subsets must also be frequent. If the size of I is n (i.e. I consists of n items) then I has $2 ^ { n } - 1$ proper subsets. Each of these subsets must be frequent. Conversely, if any of these subsets is not frequent, then I cannot be frequent. The situation is more complicated for qualified itemsets. Consider a qualified itemset $I [ Q ]$ . Let the size of I be n and let the size of Q, which is the number of qualified dimension attributes, be q. If

$I [ Q ]$ is frequent then it follows directly from the definition of support for qualified itemsets that any qualified itemset $I ^ { \prime } \left[ Q ^ { \prime } \right]$ must also be frequent, where $I ^ { \prime } \subseteq I$ and $Q ^ { \prime } \subseteq Q$ . The number of such qualified itemsets is $2 ^ { n + q } - 1$ . For example, suppose that for a given data {bag, tent} [season = Summer, region = North] is frequent (frequent means more than $\psi$ transactions where $\psi$ is the minimum support, e.g., $\psi = 1 0 , 0 0 0 )$ . Then, there are 15 other qualified itemsets that must also be frequent. Let us examine four of them along with their interpretations:

<sup>!</sup> F[region = North] is frequent means that there must be more than $\psi$ transactions that occurred in the North.

<sup>!</sup> {bag}[F] is frequent means that there must be more than w transactions involving a bag.

<sup>!</sup> {tent}[season = Summer, region = North] is frequent means that there must be more than $\psi$ transactions involving a tent that occurred in the North during the Summer.

<sup>!</sup> {bag, tent}[season = Summer] is frequent means that there must be more than w transactions involving a bag and a tent that occurred during the Summer.

Intuitively, this shows that a-priori leads to more <sup>dd</sup>diverse<sup>TT</sup> set of statements for qualified itemsets than for standard itemsets. Next we formalize this intuition.

Let the set of all frequent standard itemsets of size k be $L ^ { k } .$ . According to a-priori, any subset of any itemset in $L ^ { k }$ must also be frequent. Thus, any itemset of size $l , l { < } k$ , that is a subset of an itemset in ${ \bf \ddot { \boldsymbol { L } } } ^ { k } ,$ , must be in $L ^ { l }$ . We shall say that $L ^ { k }$ succeeds $L ^ { l } ,$ for $l < k ,$ and write $L ^ { k } \succ L ^ { l }$ . Note that d is a total ordering of all $L ^ { i }$ . This ordering dictates the order in which $L ^ { i }$ should be computed.

Consider qualified itemsets. Let $L _ { [ A ] } ^ { k }$ be the set of all frequent itemsets of size k qualified in all dimension attributes in A. According to a-priori, any qualified itemset $I [ Q ]$ that is a subset of a qualified itemset in $L _ { [ A ] } ^ { k }$ must also be frequent. If the size of I is l, and the set of attributes in $\boldsymbol { Q ^ { \prime } }$ is $A ^ { \prime }$ then $I ^ { \prime } \left[ Q ^ { \prime } \right]$ must belong to $L _ { [ A ^ { \prime } ] } ^ { k }$ . While in the case of standard itemsets there are only k such sets, for qualified itemsets there are $( k + 1 ) 2 ^ { a } - 1$ such sets, where a is the size of A. We shall say that $L _ { [ A ] } ^ { k }$ succeeds $L _ { [ A ^ { \prime } ] } ^ { l }$ and write $L _ { [ A ] } ^ { k } \succ$ $L _ { [ A ^ { \prime } ] } ^ { l }$ iff $k \ \geq l , \ A ^ { ' } \ \supseteq \ A ^ { \prime }$ and $( k , \ A ) \neq ( l , \ A ^ { \prime } \ )$

The following example illustrates qualified itemsets.

Example 3. This example shows the values of all ${ \cal L } _ { [ \mathcal { Q } ] } ^ { k } { \preceq } \bar { { \cal L } } _ { [ s e a s o n , r e g i o n ] } ^ { 2 }$ for the data from Example 2 within the specified support threshold (0.5% which is 3000 transactions). For brevity we denote qualified itemsets by concatenating items, e.g. AB instead of $\{ \mathrm { A } , \mathrm { B } \}$ , and replacing equalities by just the abbreviated attribute values, e.g. [Sm] instead of [season =Summer].

$$
\bullet L _ {[ s e a s o n ]} ^ {0} = \{\emptyset [ W i ], \emptyset [ S m ] \}
$$

$$
L _ {[ r e g i o n ]} ^ {0} = \{\emptyset [ N ], \emptyset [ S ] \}
$$

$$
\begin{array}{l} \bullet L _ {[ s e a s o n, r e g i o n ]} ^ {0} = \{\varnothing [ W i, N ], \varnothing [ S m, N ], \varnothing [ W i, S ], \\ \varnothing [ S m, S ] \} \end{array}
$$

$$
\bullet L _ {[ \emptyset ]} ^ {1} = L ^ {1} = \{A, B, C \}
$$

$$
\begin{array}{l} \bullet L _ {[ s e a s o n ]} ^ {1} = \{A [ W i ], A [ S m ], B [ W i ], B [ S m ], C [ W i ], \\ C [ S m ] \} \end{array}
$$

$$
\bullet L _ {[ r e g i o n ]} ^ {1} = \{A [ N ], A [ S ], B [ N ], B [ S ], C [ N ], C [ S ] \}
$$

$$
\bullet L _ {[ \text { season }, \text { region } ]} ^ {1} = \{B [ W i, N ], \quad C [ W i, N ], \quad C [ S m, N ],
$$

$$
A [ S m, S ], B [ S m, S ], C [ S m, S ] \}
$$

$$
\bullet L _ {[ \emptyset ]} ^ {2} = L ^ {2} = \{A B, A C, B C \}
$$

$\cdot \cal { L } _ { [ s e a s o n ] } ^ { 2 } = \{ A B [ W i ] , \ A B [ S m ]$ , AC[Wi], AC[Sm], $B C [ W i ] , B C [ S m ] \}$

$$
\begin{array}{l} \bullet L _ {[ r e g i o n ]} ^ {2} = \{A B [ N ], A B [ S ], A C [ S ], B C [ N ] \} \\ \bullet L _ {[ s e a s o n, r e g i o n ]} ^ {2} = \{A C [ S m, S ] \} \end{array}
$$

Note that there is no total ordering of these sets, for example, $L _ { [ s e a s o n , r e g i o n ] } ^ { 1 } \prec \succ L _ { [ s e a s o n ] } ^ { 2 }$ (i.e. neither $L _ { [ s e a s o n , r e g i o n ] , } ^ { 1 } \setminus L _ { [ s e a s o n ] } ^ { 2 } \mathrm { n o r } L _ { [ s e a s o n , r e g i o n ] } ^ { 1 } \prec L _ { [ s e a s o n ] } ^ { 2 }$ holds.). All $\mathring { L } _ { [ A ] } ^ { k }$ succeeded by $L _ { [ s e a s o n , r e g i o n ] } ^ { 2 }$ are organized in the hierarchy shown in Fig. 4.

Since d defines only a partial order over $L _ { [ A ] } ^ { k } ,$ there are many possible sequences in which they may be computed. Consider our running example of finding pairs of products bought frequently together in the same region and during the same season. One possibility is to first find all frequent products $( L _ { [ \mathcal { O } ] } ^ { 1 } )$ Then, find frequent products for a particular season $( L _ { [ s e a s o n ] } ^ { 1 } )$ , then frequent products for a particular season and region $( \boldsymbol { L } _ { [ s e a s o n , r e g i o n ] } ^ { 1 } )$ , and finally pairs of products for a particular season and region $( L _ { [ s e a s o n , r e g i o n ] } ^ { 2 } )$ . Another possibility is to first find frequent products for a particular region $( L _ { [ r e g i o n ] } ^ { 1 } )$ then frequent products for a particular season $( L _ { [ s e a s o n ] } ^ { 1 } ) ,$ the frequent pairs of products $( L _ { [ \mathcal { O } ] } ^ { 2 } ) .$ , and finally pairs of products for a particular season and region $( L _ { [ s e a s o n , r e g i o n ] } ^ { 2 } )$

![](/api/attachments/7S4E6Q5F/fulltext/images/1cd623fe359938632931e37230142faa81c4fb28b5814b700e5ce91c44ee5f89.jpg)  
Fig. 4. Lattice of successors.

Note that there are no such alternatives when standard association rules are used. Optimization techniques based on a-priori are essentially rule-based since the actual sizes of the initial data and intermediate result do not influence the sequence of steps. In fact, the sequence is always the same.

For qualified association rules, the sequence of steps is not always the same because of different possible alternatives as illustrated above. Intuitively, the source of alternatives is the fact that non-item dimensions are not symmetric and comparable.

Before we describe an algorithm for choosing an efficient sequence (in Section 6.2), we discuss the individual steps and their interaction within a sequence. The crux of our method (and of a-priori for that matter) is to use the result of a simpler query (which represents a portions of the entire query) to speed up the computation of the entire query. For example, if we are looking for pairs of item qualified by season and region $( L _ { [ s e a s o n , r e g i o n ] } ^ { 2 } )$ , we can eliminate all tuples from $F$ that do not contribute to the computation of frequent items qualified by season $( L _ { [ s e a s o n ] } ^ { 1 } )$ . Then, we can use the reduced fact table to compute the qualified pairs. Generally, every step in our framework has two parts:

## 1. compute $L _ { [ A ] } ^ { k } ,$

## 2. use the computed compute $L _ { [ A ] } ^ { k }$ to reduce F.

This framework is similar to query flocks [26] and can be adapted to handle iterative, candidate-growing, algorithms, such as a-priori [1]. Instead of reducing the size of the fact table in step 2, we can use $L _ { [ A ] } ^ { k }$ to generate the new candidate set for the next iteration of the algorithm.

Next, we detail the two-part step and the interaction within a sequence.

## 3.3.1. Computing $L _ { [ A ] } ^ { k }$

First, we express $L _ { [ A ] } ^ { k }$ in relational algebra. Without loss of generality, we assume that $A = \left\{ A _ { 1 } , . . . . , A _ { m } \right\}$ and $A _ { i }$ is attribute of dimension table $D _ { i }$

$$
\sigma_ {c o u n t (T I D) > = \psi} \left(\gamma_ {I _ {k}, A} \left(F _ {k} \triangleright \triangleleft D J\right)\right)
$$

where $F _ { k }$ is a k-way self-join of the fact table F on $T I D , \ I _ { k }$ is a set of the keys $( K _ { 0 } )$ of the item dimension from each of the k copies of the fact table, DJ is a cross product of $D _ { 1 } , \ldots , D _ { m } , \ \gamma$ is the aggregation operator, and $\psi$ is the minimum support.

In SQL, $L _ { [ A ] } ^ { k }$ can be computed as follows:

SELECT F1 $. \mathrm { K 0 , \ldots , }$ Fk.K0, A1, . . . , Am FROM F AS F1, . . . , F AS Fk, $\mathrm { D 1 , \ldots }$ , Dm WHERE F1.TID= F2.TID. . . AND F1.TID= Fk.TID AND F1.K1= D1.K1. . . AND F1.Km= Dm.Km GROUP BY F1.K0, . . . , Fk.K0, A1, . . . , Am HAVING COUNT (DISTINCT F1.TID)<sup>N</sup>=:minsup

## 3.3.2. Reducing the fact table F with $L _ { / A / } ^ { k }$

First, consider the case when $k = 1$ and $A = \emptyset$ Then $L _ { [ \mathcal { O } ] } ^ { 1 } .$ as a relation, has only one attribute, $K _ { 0 } .$ The fact table is reduced by semijoining it with $L _ { [ \mathcal { O } ] } ^ { 1 } \mathrm { : }$

$$
F \stackrel {{\leftarrow}} {{\triangleright}} \triangleleft \sigma_ {\text { count } (T I D) > = \psi} \left(\gamma_ {K _ {0}} (F)\right)
$$

Let $A = \left\{ A _ { 1 } , . . . , A _ { m } \right\}$ . Then $L _ { [ A ] } ^ { 1 }$ has, in addition to $K _ { 0 } ,$ attributes $A _ { 1 } , . . . , A _ { m }$ . Therefore, the reduction of F has to involve DJ in addition to $L _ { [ A ] } ^ { 1 } \mathrm { : }$

$$
F \stackrel {{\longleftarrow}} {{\triangleright}} \triangleleft (D J \triangleright \triangleleft \sigma_ {c o u n t (T I D) > = \psi} (\gamma_ {K _ {0}, A} (F _ {k} \triangleright \triangleleft D J)))
$$

In the general case, for $k > 1$ , where $I _ { 1 }$ is the first attribute in $I _ { k } ,$ , we can express the reduction as follows:

$$
\begin{array}{l} X = F _ {k} \triangleright \triangleleft D J \triangleright \triangleleft \sigma_ {\text { count } (T I D) > = \psi} \big (\gamma_ {I _ {k}, A} \big (F _ {k} \triangleright \triangleleft D J \big) \big) \\ F \stackrel {{\longleftarrow}} {{\triangleright}} \triangleleft \pi_ {T I D, I _ {1}, K _ {I} \ldots , K _ {m}} (X). \end{array}
$$

Intuitively, we need the TID in the last expression, in order to connect the items in the qualified itemsets.

## 3.3.3. Computing a sequence of $L _ { [ A ] } ^ { k }$

So far, we considered computing $\overset { - } { L } _ { [ A ] } ^ { k }$ individually. In this section we consider, what happens when we compute several of them. In particular, we examine how to use a computed $L _ { [ A ] } ^ { k }$ to speed up the computation of another $L _ { [ B ] } ^ { l }$ . We consider all three possible cases:

$L _ { [ A ] } ^ { k } \succ L _ { [ B ] } ^ { l }$ . In this case, using the computed set of frequent qualified itemsets does not help. The reason is that $L _ { [ B ] } ^ { l }$ can be arbitrarily large regardless of the size $L _ { [ A ] } ^ { k }$ . In an extreme case $\boldsymbol { L _ { [ A ] } ^ { k ^ { - } } }$ can be empty and $L _ { [ B ] } ^ { l }$ can be as large as possible.

$\cdot \ { \cal L } _ { [ A ] } ^ { k } \prec \bar { { \cal L } } _ { [ B ] } ^ { l } .$ . This is the case that corresponds to the condition in a-priori. The computed set can be used in computing $\bar { L } _ { [ B ] } ^ { l }$ as shown in a-priori.

$\cdot \ { \cal L } _ { [ A ] } ^ { k } \ \prec \succ \ L _ { [ B ] } ^ { l }$ . In this case, using an argument similar to the first case, we can show that the computed set does not help.

Thus, the order of computation affects the actual result, so we will use a different notation to denote that the computation of the frequent qualified itemsets is happening in context of other computations. We define $R _ { A } ^ { k }$ to be the computation of $L _ { [ A ] } ^ { k }$ on the current reduced fact table $F \colon$

$$
R _ {A} ^ {k} = \sigma_ {\text { count } (T I D) > = \psi} \left(\gamma_ {I _ {k}, A} \left(F _ {k} ^ {\text { red }} \triangleright \triangleleft D J\right)\right)
$$

where $F _ { k } ^ { r e d }$ is a k-way self join of what remains of the fact table after the previous reduction. For the first reduction $F _ { k } ^ { r e d } { = } F _ { k }$

## 3.4. Optimization algorithm

We can show that the plan space for the optimization problem is double-exponential in number of qualified dimensions. Consider all reducers at level 1. Since we have m dimensions and a reducer involves any subset of these dimensions, then the number of possible reducers is $2 ^ { m }$ . A plan involves any subset of all possible reducers, so the number of possible plans for one level is $2 ^ { 2 ^ { \overset { \cdot } { m } } }$ . If we consider n levels, then the total number of possible plans is $2 ^ { n 2 ^ { m } }$

The number of possible reducers is $n 2 ^ { m }$ where n is the maximum itemset size and m is the number of qualified dimensions. Since a plan is any subset of these reducers, the plan space is at least $\bar { 2 } ^ { n 2 ^ { m } }$

The algorithm uses the following definitions. Let $R _ { A } ^ { k }$ be a reducer and let $P$ be a sequence of reducers. Then we define the following:

$c o s t ( R _ { A } ^ { k } , P )$ as the cost of computing $R _ { A } ^ { k }$ after all reducers in $P$ have been computed and applied. $\cdot f r a c ( R _ { A } ^ { k } , P )$ is the fraction of the fact table that is reduced by applying $R _ { A } ^ { k }$ after all reducers in P have been applied.

We propose a greedy algorithm for finding a plan for computing $R _ { A } ^ { k }$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input:  $R_{A}^{k}$ 
Output: P
begin
    $P=\emptyset$ 
    /*V contains all reducers succeeded by  $R_{A}^{k}$ 
    including  $R_{A}^{k}$  */
    $V=\{R_{j}^{i}|1\leq i\leq k,J\subseteq A\}$ 
    repeat
    choose  $R_{B}^{l}$  from V such that
    cost( $R_{B}^{l},P$ )/frac( $R_{B}^{l},P$ ) is minimal.
    append  $R_{B}^{l}$  to P
    remove  $R_{B}^{l}$  from V
    until (l=k and A=B)
    return P
end
</div>

The algorithm starts with the full set of options to choose from: all reducers that are succeeded by $R _ { A } ^ { k }$ and therefore can help in computing $R _ { A } ^ { k }$ . Then, iteratively, the reducer that has the smallest cost per unit of reduction is chosen until this reducer is $R _ { A } ^ { k }$

However, we can improve this algorithm in several ways. The first improvement is based on the following observation:

If $R _ { A } ^ { k } \in { \cal P }$ and $R _ { A } ^ { k } { \succeq } R _ { B } ^ { l }$ then, $f r a c ( R _ { B } ^ { l } , P ) = 0$ . Once a reducer is applied, there is no further reduction by reducers dominated by the first one. Therefore, we can limit the set of possible choice V by removing all reducers dominated by the last chosen reducer.

The second improvement is to consider all reducers of each level separately. Such levelwise approach is appropriate for several reasons. First, it allows us to find all frequent qualified itemsets regardless of their size because we compute $L _ { [ A ] } ^ { i }$ for all i not just $i { = } k$ Second, we can compute the confidence of a qualified association rule without an additional pass over the data. Third, it allows us to use better cost and reduction estimates since we only compare reducer at the same level.

The greedy levelwise algorithm (improved as described) is shown below:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input:  $R_{A}^{k}$ 
Output: P
begin
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$P=\emptyset$ 
for  $i=1..k$ $V=R_{J}^{i}\mid J\subseteq A\}$ 
repeat
    choose  $R_{B}^{l}$  from V such that  $cost(R_{B}^{l},P)/frac(R_{B}^{l},P)$  is minimal.
    append  $R_{B}^{l}$  to P
    remove  $R_{B}^{l}$  from V
    remove  $R_{C}^{l}$  from V for  $C\subset B$ 
until (B=A)
return P
end
</div>

The algorithm tackles each level separately by applying the general greedy algorithm to the set of all reducers at each level.

## 3.5. Cost estimation

Finding closed formulas or even close estimates for cost (cost) and reduction (frac) functions is a hard problem. The information required in order to make the estimation tight can only be obtained after mining the data. Thus, we focus our attention on relatively simple models that lead to the selection of efficient plans by the levelwise greedy algorithm. In our future work, we will consider using the mining results from previous queries to make even better estimates.

First, let us consider the cost function: $c o s t ( R ^ { k } { } _ { A } , P )$ and let $A = \left\{ A _ { 1 } , . . . . , A _ { m } \right\}$ , where $A _ { i }$ is attribute of $D _ { i } .$ Let the size of the fact table be $f$ and the sizes of the dimension tables be $d _ { i } .$ . Recall that there are two steps of each reduction: computing and applying the reducer. The reducer is computed as follows:

$$
\sigma_ {c o u n t (T I D) > = \psi} \left(\gamma_ {I _ {k}, A} \big (F _ {k} \triangleright \triangleleft D J \big)\right).
$$

Before we tackle the general case, consider the case when k = 1 and $A = \emptyset$ . Then we can rewrite the expression as follows:

$$
\sigma_ {c o u n t (T I D) > = \psi} \left(\gamma_ {K _ {0}} (F)\right).
$$

The cost of this expression is the cost of accessing and aggregating F. Since most database systems implement aggregation using sorting, and sorting requires reading F a small number of times (e.g. using two phase merge sort) the cost is linear in $f .$ Consider the case when k = 1 and A is not empty.

Then the expression can be written as:

$$
\sigma_ {c o u n t (T I D) > = \psi} \left(\gamma_ {K _ {0 ^ {\cdot A _ {1}}, \dots , A _ {m}}} \left(F \triangleright \triangleleft D _ {1} \triangleright \triangleleft \dots \triangleright \triangleleft D _ {m}\right)\right).
$$

Because of the star schema every tuple in F joins with exactly one tuple from each $D _ { i }$ . Thus, we can estimate the cost of this reducer is linear in the sum of the sizes of the dimension tables. In the general case it is difficult to estimate the size of $F _ { k }$ . Fortunately in the levelwise greedy algorithm we only compare reducers at the same level so the exact value is not important.

Since the cost is linear in the size of the fact table and in the sum of the sizes of the dimension tables, the formula for the cost is:

$$
\operatorname{cost} \left(R _ {A} ^ {k}, P\right) = c _ {1} f _ {k} \left(\sum_ {i = 1} ^ {m} 2 d _ {i} + \text { sizeof } \left(R _ {A} ^ {k}, P\right)\right) + c _ {2}
$$

where $c _ { 1 }$ and $c _ { 2 }$ are system dependent constants. We count each $d _ { i }$ twice because both the computation and application of $R _ { A } ^ { k }$ involve dimension table $D _ { i }$ whereas $R _ { A } ^ { k }$ is used only in the application.

Next we estimate the fraction function that also determines $s i z e o f ( R _ { \mathrm { A } } ^ { k } , P )$ we need to estimate the number of different qualified itemsets that are frequent.

The estimate of the fraction of all tuples in the fact table that will be eliminated by a reducer $R _ { A } ^ { k }$ depends crucially on the distribution of the values in $F .$ The simple assumption that this distribution is uniform leads to straightforward calculations and has been used successfully in optimizing join ordering and view materialization. In our case, however, the uniformity assumption is clearly at odds with the goal of mining associations. In fact, mining association-rules is meaningless for uniformly distributed data since any combination is equally likely. Recent research has shown empirically [5] that large datasets, especially transaction-based ones, tend to have a skewed distribution that can be approximated by the Zipfian distribution. The Zipfian distribution is characterized by the property that the number of occurrences of each value is inversely proportional to its rank. Thus, if the most frequent value occurs x times, then the n-th most frequent value occurs x / n times. The rest of our analysis is based on the assumption that the data follows a Zipfian distribution. However, other distributions can be handled in a similar fashion.

First, consider the simplest case when $k = 1$ and A is empty. Let the number of different items (values of attribute $k _ { 0 } )$ that occur in $F$ be $p { = } d o m a i n ( K _ { 0 } )$ , and let the size of $F$ be $f .$ Then, if the most frequent item occurs x times, we have the approximate equality:

$$
x \sum_ {i = 1} ^ {p} \frac {1}{i} \approx f.
$$

The sum of the first $p$ members of the harmonic series can be approximated by ln $p { + } 0 . 5 7 7$ . Then, we have:

$$
x \approx \frac {f}{\ln p + 0 . 5 7 7}.
$$

If the minimum support threshold is $\psi _ { ; }$ , then the number of items that occur at least $\psi$ times is approximately $y$ (the $y$ most frequent ones), where $x / y \approx \psi$ Substituting for x we get the formula for $y \colon$

$$
y \approx \frac {f}{\psi (\ln p + 0 . 5 7 7)}.
$$

Note that $s i z e o f ( R _ { \oslash } ^ { 1 } , { \cal P } ) ) = y .$ The y most frequent items appear in approximately $x \textstyle \sum _ { i = 1 } ^ { y } { \frac { 1 } { i } }$ tuples of $\cdot f .$ Thus, we can derive frac $( R _ { \mathcal { O } } ^ { 1 } , \mathcal { O } )$ as follows:

$$
1 - \frac {x \sum_ {i = 1} ^ {y} \frac {1}{i}}{f}.
$$

After substituting the values of x and $y$ and algebraic manipulation we get:

$$
\operatorname{frac} \left(R _ {\emptyset} ^ {1}, \emptyset\right) \approx \frac {\ln \frac {p \psi (\ln p + 0 . 5 7 7)}{f}}{\ln p + 0 . 5 7 7}.
$$

Let us consider the case when $k = 1$ and $A = \{ A _ { 1 } , \ldots ,$ $A _ { m } \}$ . We shall assume that values of the tuple $K _ { 0 } ,$ $A _ { 1 } , . . . , A _ { m }$ follow a Zipfian distribution. Thus, we can apply the above formula with a different $p \mathrm { : }$ the number of different combinations of values of $K _ { 0 } , A _ { 1 } , \ldots$ $A _ { m }$ that occur in the data. Without any additional information we can assume that all combinations are possible but their number cannot exceed the number of tuples in F. Thus, in this case $p { = } m i n ( d o m a i n ( K _ { 0 } )$ $\Pi _ { i = 1 } ^ { m } \ d o m a i n ( A _ { i } ) , f )$

In general, for $k > 1$ , the computation of the fraction function is much more complex. We will show how to reduce the case $k = ~ 2$ to an approximately equivalent case with $k = 1$ . Using a composition of $k - 1$ such reductions we can reduce the case for any $k > 1$ to the case $k = 1$ . Recall that the last reducer computed and applied by the levelwise greedy algorithm (described in Section 6.2) at level 1 is $\dot { R _ { A } ^ { 1 } }$ . By running several simple queries over $R _ { A } ^ { 1 }$ we can find the number of different values in the reduced fact table $F$ for any attribute $A _ { i } ,$ i.e. the new $d o m a i n ( A _ { i } )$ . Also, we can find the number of different items (values of $K _ { 0 } )$ , the total number of tuples left and the total number of transactions. Thus, we can estimate the average number of items per transactions and the total number of pairs of items, which is the size of $F _ { 2 } ,$ where ${ \cal F } _ { 2 } { = } { \cal F } { \triangleright } { \triangle } _ { \mathrm { T I D } { = } \mathrm { T I D } } { \cal F } .$ Consider the non-materialized table $F _ { 2 }$ and consider a pair of items to be a new item. Each reducer at level 2 acts as a level 1 reducer for this new table and items. We assume that a reduction of the new table of pairs will correspond to the same reduction of $F .$ Therefore, we can use the method outlined for $k = 1$ in this situations. Note that we use this method only to choose the reducers at level 2; not to implement them. These reducers are applied to the fact table $F ;$ not the table of pairs.

So far, we derived formulas only for $f r a c ( R _ { A } ^ { k } , \emptyset )$ Now we consider the interaction among different reducers. Suppose $R _ { A } ^ { k }$ is chosen first. We need to define $f r a c ( R _ { B } ^ { k } , \{ R _ { A } ^ { k } \} )$ . We consider the three possible cases:

$A \supset B .$ . Then $L _ { [ A ] } ^ { k } \succ L _ { [ B ] } ^ { k }$ and therefore the fraction is 0. For example, eliminating all tuples with nonfrequent items, after eliminating all tuples with non-frequent items qualified with a season, does not help at all.

$A \subset B .$ Then $L _ { [ A ] } ^ { k } \prec L _ { [ B ] } ^ { k }$ and thus any tuple eliminated by the second reducer is also eliminated by the first. Therefore: $f r a c ( R _ { B } ^ { k } , \{ R _ { A } ^ { k } \} ) = ( f r a c ( R _ { B } ^ { k } ,$ $\textcircled { \scriptsize { \times } } ) - f r a c ( R _ { \cal A } ^ { k } , \emptyset ) ) / ( 1 - f r a c ( R _ { \cal A } ^ { k } , \emptyset )$

$A \ \not \subset B \ \not \subset A$ . In this case, the exact value cannot be determined but we can get an estimate as follows. Let the fraction of tuples eliminated by both $R _ { A } ^ { k }$ and $R _ { B } ^ { k }$ be $z ;$ and let frac $( R _ { A } ^ { k } , \mathbf { \omega } _ { \bigcirc } ) = f _ { A } , f r a c { ( R _ { B } ^ { k } , }$ $\mathbf { \nabla } \mathcal { Q } ) = f _ { B } ,$ , and $f r a c ( R _ { \mathrm { A } } ^ { k } \cup _ { \mathrm { B } } , \emptyset ) = f _ { A B }$ . The following contingency table reflects the constraints we have:

<table><tr><td>reduced</td><td>by  $R_B^k$ </td><td>not by  $R_B^k$ </td></tr><tr><td>by  $R_A^k$ </td><td>z</td><td> $f_A - z$ </td></tr><tr><td>not by  $R_A^k$ </td><td> $f_B - z$ </td><td> $z + f_{AB} - f_A - f_B$ </td></tr></table>

Without any additional information a good estimate for z is in the middle of the range of possible values given by:

$$
\left[ f _ {A} + f _ {B} - f _ {A B}, \frac {f _ {A} + f _ {B}}{2} \right].
$$

Then:

$$
z = \frac {3 f _ {A} + 3 f _ {B} - 2 f _ {A B}}{2}.
$$

Therefore, we have:

$$
\begin{array}{l} f r a c \big (R _ {B} ^ {k}, \big \{R _ {A} ^ {k} \big \} \big) = \big (f r a c \big (R _ {B} ^ {k}, \emptyset \big) - 3 f r a c \big (R _ {A} ^ {k}, \emptyset \big) \\ \qquad + 2 f r a c \big (R _ {A \cup B} ^ {k}, \emptyset \big) \big) \\ \qquad / 4 \big (1 - f r a c \big (R _ {A} ^ {k}, \emptyset \big) \big). \end{array}
$$

Thus, we determine how to update the frac function after any reducer is computed and applied which is needed by the optimization algorithm.

## 4. Experiments and performance

For our experiments we used Oracle 9i RDBMS running under SunOS 5.9. We used subsets of data from a 23 terabytes corporate data warehouse that stores data for a major US-based retailer over 2-year period. In our experiments we mined both association rules and qualified association rules. In this paper, we present the results of queries that are typical for our experiments.

Table 3  
US retailer-associations rules found (top 20 with highest support)

<table><tr><td>ItemKey1</td><td>ItemKey2</td><td>Total</td></tr><tr><td>31,107</td><td>31,167</td><td>22,973</td></tr><tr><td>14,925</td><td>14,927</td><td>22,384</td></tr><tr><td>14,925</td><td>31,167</td><td>22,238</td></tr><tr><td>4835</td><td>4841</td><td>21,441</td></tr><tr><td>4515</td><td>4519</td><td>21,280</td></tr><tr><td>4833</td><td>4841</td><td>20,658</td></tr><tr><td>31,167</td><td>31,257</td><td>20,540</td></tr><tr><td>4841</td><td>14,925</td><td>20,171</td></tr><tr><td>4835</td><td>4843</td><td>19,088</td></tr><tr><td>31,167</td><td>31,305</td><td>18,568</td></tr><tr><td>4843</td><td>31,167</td><td>18,456</td></tr><tr><td>31,049</td><td>31,167</td><td>18,055</td></tr><tr><td>4835</td><td>14,925</td><td>17,650</td></tr><tr><td>4833</td><td>4843</td><td>17,635</td></tr><tr><td>3325</td><td>3341</td><td>17,150</td></tr><tr><td>4841</td><td>31,167</td><td>16,902</td></tr><tr><td>4833</td><td>31,167</td><td>16,871</td></tr><tr><td>4833</td><td>14,925</td><td>16,203</td></tr><tr><td>4519</td><td>4769</td><td>16,041</td></tr><tr><td>4841</td><td>4843</td><td>15,973</td></tr><tr><td>...</td><td>...</td><td>...</td></tr></table>

Table 4  
US retailer—qualified associations rules found

<table><tr><td>ItemKey1</td><td>ItemKey2</td><td>Month</td><td>Region</td><td>Total</td></tr><tr><td>3237</td><td>3287</td><td>12</td><td>5</td><td>1860</td></tr><tr><td>3237</td><td>3287</td><td>12</td><td>4</td><td>1816</td></tr><tr><td>153</td><td>3237</td><td>12</td><td>4</td><td>1755</td></tr><tr><td>14,925</td><td>14,927</td><td>12</td><td>2</td><td>1712</td></tr><tr><td>14,925</td><td>14,927</td><td>12</td><td>1</td><td>1645</td></tr><tr><td>153</td><td>155</td><td>12</td><td>4</td><td>1600</td></tr><tr><td>3237</td><td>3817</td><td>12</td><td>5</td><td>1574</td></tr><tr><td>14,925</td><td>31,167</td><td>12</td><td>2</td><td>1564</td></tr><tr><td>3807</td><td>14,925</td><td>12</td><td>5</td><td>1557</td></tr><tr><td>3237</td><td>4519</td><td>12</td><td>5</td><td>1549</td></tr><tr><td>4519</td><td>4769</td><td>1</td><td>4</td><td>1543</td></tr><tr><td>4519</td><td>4769</td><td>1</td><td>5</td><td>1537</td></tr><tr><td>153</td><td>3287</td><td>12</td><td>4</td><td>1535</td></tr><tr><td>153</td><td>14,925</td><td>12</td><td>4</td><td>1524</td></tr><tr><td>3237</td><td>3567</td><td>12</td><td>4</td><td>1521</td></tr><tr><td>3237</td><td>3441</td><td>12</td><td>5</td><td>1515</td></tr><tr><td>4835</td><td>14,925</td><td>12</td><td>5</td><td>1505</td></tr><tr><td>3237</td><td>4519</td><td>12</td><td>4</td><td>1501</td></tr></table>

Our first experiment consists of two queries and it uses a schema that is nearly equivalent to the schema shown in Fig. 1, with one difference being the absence of the customer dimension. The first query finds regular association rules based on the following question:

Find all pairs of items that appear together in more than 1500 transactions.

The implementation of this query involves pruning of all items that do not appear in more than 1500 transactions. The result of the query is more than 1500 pairs of items. We show the 20 most frequent ones in Table 3.

The second query finds qualified association rules and is based on the following question

Find all pairs of items that appear together in more than 1500 transactions in the same region during the same month.

The implementation of this query involves pruning all item-region pairs that do not appear in more than 1500 transactions. The result of this query, shown in Table 4, is a set of eighteen rules, where each rule involves two items, a month, and a region. The rules are ordered by frequency (the most frequent appears at the top of the table).

<table><tr><td colspan="8">The number of discovered standard and qualified association rules</td></tr><tr><td>Minimum support (000)</td><td>20</td><td>10</td><td>5</td><td>2</td><td>1.5</td><td>1</td><td>.5</td></tr><tr><td>No. of qualified rules</td><td>0</td><td>0</td><td>0</td><td>0</td><td>18</td><td>255</td><td>3231</td></tr><tr><td>No. of standard rules</td><td>8</td><td>105</td><td colspan="5">more than 5000</td></tr></table>

When we compare the two tables, we first notice that by and large they contain different itemsets. For example, compare the top two pairs in each set (31,107, 31,167—Table 3 and 3237, 3287—Table 4). The pair (3237, 3287) is not in the top 20 frequent pairs; however, when month and region are qualified it stands out as the most frequent pair (for Region 5 and December). On the other hand, the pair (31,107, 31,167) is the most frequent pair overall but when month and region are qualified this pair is not frequent, for any month and region combination.

This experiment illustrates that qualified association rules can reveal additional valuable information that would not have been discovered using standard association rules mining. In this case standard association rules find the correlated sales that are spread among many markets and months (which may be used, for example, when planning a long-term nationwide or global marketing campaign), while qualified association rules find the correlated sales that are concentrated in particular markets over particular time periods (which may be used, for example, when planning a series of shorter term marketing campaigns with regional focus). As shown in this real-world example, the standard and qualified rules can involve completely different sets of items.

In our second experiment, we compared the number of discovered qualified association rules with the number of standard association rules mined from the same set, while varying the value of minimum support. The results are shown in Table 5.

As expected, for lower values of minimum support, the number of standard rules is overwhelming (examining and making decisions based on thousands of rules is usually not realistic), while the number of qualified rules is still manageable. Furthermore, for lower values of minimum support, the cost of finding all standard rules is extremely high, because the first step of a-priori results in a very small reduction of the possible pairs of items. This observation supports our argument (stated in 4.1) that it is not feasible to use standard association rule mining to find qualified rules, by simply considering value of each qualifier as just another item added to the transaction.

![](/api/attachments/7S4E6Q5F/fulltext/images/0b86afc61289798ba018b2c6a703143f12c888a182c1aa757ec03455c38d334a.jpg)  
Fig. 5. Cost estimates for the choice of first step of the greedy plan.

Our next set of experiments focuses on the optimization process and performance. We detail our findings for the mining problem of finding frequent pairs of items qualified by season and region $L _ { [ s e a s o n , r e g i o n ] } ^ { 2 } .$ First, we considered how the first step of the plan picked by the greedy algorithm changes with respect to the minimum support, as shown in Fig. 5.

When the support was relatively low, less than 1000, the first step that was chosen was $R _ { s e a s o n } ^ { 1 }$ month. For support greater than 1000, $R _ { \mathcal { O } } ^ { 1 }$ is the winner. These results confirm our intuition, since for higher support the expected reduction from considering just items is significant, whereas for low minimum support this reduction is negligible and offsets the lower cost of $R _ { \mathcal { O } } ^ { 1 }$

Finally, we compared the performance of the plan picked by the levelwise greedy algorithm against the fixed plan that corresponds to the second mapping of qualified association rules to standard association rules as described in Section 3.2 (we chose the second mapping as a representative; similar conclusions would hold for the comparison with both the same conclusions would hold for first and third mapping). As we mentioned in Section 3.2, approaches based on standard association rule mining, could be used, in theory, to find qualified association rules. However, the performance cost for such approaches is significantly higher than the cost of our approach, which is designed especially for finding qualified association rules. This is illustrated by the performance numbers summarized in Table 6.

While the actual numbers are system dependent, our algorithm clearly outperforms the statically chosen sequence corresponding to bundling together item, region and dimension. The main reason for the stark difference in performance is that the bundling precludes any opportunities for reduction which is crucial in speeding up the first few steps of the sequence of reducers.

Table 6  
Running times for the plans produced by the greedy algorithm and the static a-priori plan

<table><tr><td>Minimum support</td><td>Greedy algorithm run time</td><td>Adapted a-priori run time</td></tr><tr><td>500</td><td>465</td><td>1040</td></tr><tr><td>1000</td><td>135</td><td>306</td></tr><tr><td>1500</td><td>81</td><td>180</td></tr><tr><td>2000</td><td>66</td><td>141</td></tr></table>

## 5. Conclusions

In this paper, we presented a new data-mining framework, called qualified association rules, that is tightly integrated with database technology. We showed how qualified association rules can enable organizations to find new information within their data warehouses relatively easily, utilizing their existing technology.

We were motivated by the observation that existing association-rule based approaches are capable of effectively mining data warehouse fact tables in conjunction with the item-related dimension only. We introduced qualified association rules as a method for mining fact tables as they relate to the attributes from both item and non-item dimensions. Standard association rules find coarser granularity correlations among items while qualified rules discover finer patterns. Both types of rules can provide valuable insight for the organization that owns the data. Combined information, extrapolated by examining both standard and qualified association rules, is much more likely to truly reveal the nature of the data stored in the corporate data warehouse and the knowledge captured in it. The existing methods are suited to provide only partial information (standard rules) from data warehouses and, in most cases, require that the data must be retrieved from the database repository and examined by using separate software. Our method provides a more complete view of the data (both standard and qualified rules), while allowing the data to remain in the data warehouse and using the processing power of the database engine itself. State-of-the-art RDBMS query optimizers cannot handle mining qualified association rules directly. Our approach, using an external optimizer, leverages their strength and works around their weaknesses, thus making the mining processing effective and efficient.

Besides integrated analytical data collections, such as data warehouses or data marts, many other data repositories are organized in a dimensional-like fashion. For example, it is very common for regular operational databases and files to include tables that contain transactional records composed of a transaction identifier, quantifying data, and foreign keys to other tables involved in the transaction. Any data that is organized and stored in this way can be mined efficiently with qualified association rules, adding a new and valuable insight, as we argued in this paper.

We have conducted experiments that implement our approach on real-life data and the results support the viability of our integration approach as well as the appropriateness of qualified association rules. Our future work will include further performance studies with additional data sets, using different hardware platforms and various types of indexes.

## References

[1] R. Agrawal, R. Srikant, Fast algorithms for mining association rules, Proceeding of International Conference on Very Large Databases vldb- Santiago de Chile, Morgan Kaufmann, San Francisco, CA, 1994, pp. 487– 499.

[2] R. Agrawal, T. Imielinski, A. Swami, Mining association rules between sets of items in large databases, Proceeding of ACM SIGMOD International Conference-Washington D.C., ACM Press, New York, NY, 1993, pp. 207– 216.

[3] R. Agrawal, H. Mannila, R. Srikant, H. Toivonen, A. Verkamo, Fast Discovery of Association Rules, in: U.M. Fayyad, G. Piatetsky-Shapiro, P. Smyth, R. Uthurusamy (Eds.), Advances in Knowledge Discovery and Data Mining. AAAI/ MIT Press, Menlo Park, CA, 1996, pp. 307–326.

[4] M. Berry, G. Linoff, Data mining techniques for marketing, Sales and Customer Support, Wiley and Sons, New York, NY, 1997.

[5] Z. Bi, C. Faloutsos, F. Korn, The <sup>dd</sup>DGX<sup>TT</sup> distribution for mining massive, skewed data, Proceedings of the Seventh ACM SIGKDD International Conference on Knowledge Discovery and Data Mining-San Francisco, CA, ACM Press, New York, NY, 2001, pp. 17– 26.

[6] S. Brin, R. Motwani, C. Silverstein, Beyond market baskets: generalizing association rules to correlations, Proceeding of ACM SIGMOD International Conference-Tucson, Arizona, ACM Press, New York, NY, 1997, pp. 265 – 276.

[7] A. Chaudhuri, U. Dayal, An overview of data warehousing and OLAP technology, ACM SIGMOD Record 26 (1) (1997) 65– 74.

[8] A. Chen, P. Goes, J. Mardsen. A Query-Driven Approach to the Design and Management of Flexible Database Systems. Journal of Management Information Systems 19(3) (Winter 2002-2003), 121–154.

[9] H.M. Chung, P. Gray, Special section: data mining, Journal of Management Information Systems 16 (1) (1999 (Summer)) 11 –16.

[10] T. Fukuda, Y. Morimoto, S. Morishita, T. Tokuyama, Mining optimized association rules for numeric attributes, Proceedings

of the Fifteenth ACM SIGACT-SIGMOD-SIGART Symposium on Principles of Database Systems-Montreal, Canada, ACM Press, New York, NY, 1996, pp. 182– 191.

[11] T. Fukuda, Y. Morimoto, S. Morishita, T. Tokuyama, Data mining with optimized two dimensional association rules, ACM Transactions on Database Systems 26 (2) (2001) 179– 213.

[12] K. Glassey, Seducing the end user, Communications of the ACM 41 (9) (1998) 52 – 60.

[13] N. Gorla, Features to consider in a data warehousing system, Communications of the ACM 46 (11) (2003) 111 –115.

[14] J. Han, Y. Fu, Discovery of multiple-level association rules from large databases, Proceeding of International Conference On Very Large Databases VLDB-Zurich, Switzerland, Morgan Kaufmann, San Francisco, CA, 1995, pp. 420– 431.

[15] J. Han, J. Lakshmanan, J. Pei, Quotient cube: how to summarize the semantics of a data cube, Proceeding of International Conference On Very Large Databases VLDB-Hong Kong, China, Morgan Kaufmann, San Francisco, 2002, pp. 778– 789.

[16] R. Kimball, L. Reeves, M. Ross, W. Thornthwhite, The Data Warehouse Lifecycle Toolkit, Wiley and Sons, New York, NY, 1998.

[17] H. Lu, L. Feng, J. Han, Beyond intratransaction association analysis: mining multidimensional intertransaction association rules, ACM Transactions on Information Systems 18 (4) (2000) 423– 454.

[18] S. Nestorov, N. Jukic, Ad-hoc association-rule mining within the data warehouse, Proceedings of the Thirty-sixth Annual Hawaii International Conference on System Sciences HICSS-Big Island, Hawaii, IEEE, Los Alamitos, CA, 2003.

[19] J. Pei, J. Han, W. Wang, Mining sequential patterns with constraints in large databases, Proceedings of ACM Conference on Information and Knowledge Management-CIKM-2002, McLean, Virginia, ACM Press, New York, NY, 2002, pp. 18 – 25.

[20] S. Sarawagi, S. Thomas, R. Agrawal, Integrating mining with relational database systems: alternatives and implications, Proceedings of ACM SIGMOD Conference-Seattle, Washington, ACM Press, New York, NY, 1998, pp. 343– 354.

[21] G. Sathe, S. Sarawagi, Intelligent rollups in multidimensional OLAP data, Proceedings of International Conference on Very Large Databases VLDB-Rome, Italy, Morgan Kaufmann, San Francisco, CA, 2001, pp. 531 – 540.

[22] C. Silverstein, S. Brin, R. Motwani, J. Ullman, Scalable techniques for mining causal structures, Proceedings of International Conference on Very Large Databases VLDB-New York City, Morgan Kaufmann, San Francisco, CA, 1998, pp. 594–605.

[23] P. Smyth, D. Pregibon, C. Faloutsos, Data-driven evolution of data mining algorithms, Communications of the ACM 45 (8) (2002) 33– 37.

[24] R. Srikant, R. Agrawal, Mining generalized association rules, Proceeding of International Conference On Very Large Databases VLDB-Zurich, Switzerland, Morgan Kaufmann, San Francisco, CA, 1995, pp. 407– 419.

[25] R. Srikant, R. Agrawal, Mining quantitative association rules in large relational tables, Proceeding of ACM SIGMOD Inter-

national Conference-Montreal, Canada, ACM Press, New York, NY, 1996, pp. 1 –12.

[26] S. Tsur, J. Ullman, S. Abiteboul, C. Clifton, R. Motwani, S. Nestorov, A. Rosenthal, Query flocks: a generalization of association-rule mining, Proceedings of ACM SIGMOD Conference-Seattle, Washington, ACM Press, New York, NY, 1998, pp. 1 – 12.

[27] A. Tung, J. Han, H. Lu, L. Feng, Efficient mining of intertransaction association rules, IEEE Transactions on Knowledge and Data Engineering 15 (1) (2003) 43– 56.

[28] K. Wang, Y. He, J. Han, Mining frequent itemsets using support constraints, Proceedings of International Conference on Very Large Databases VLDB-Cairo, Egypt, Morgan Kaufmann, San Francisco, CA, 2000, pp. 43–52.

![](/api/attachments/7S4E6Q5F/fulltext/images/888a8d98fee3db0deebee70cd745ad24ea29c616d0544f13e1a3e2f684d72394.jpg)  
Nestorov is a co-founder of Mobissimo.com.

Nenad Jukic´ is an Associate Professor of Information Systems and the Director of Graduate Certificate Program in Data Warehousing and Business Intelligence at Loyola University Chicago Graduate School of Business. Dr. Jukic´ received a B.S. in Electrical Engineering and Computer Science from the University of Zagreb, Croatia. He received a M.S. and Ph.D. in Computer Science form the University of Alabama. Dr. Jukic´ conducts active

research in various information technology related areas, including database management, e-business, data warehousing/business intelligence, and data mining.

![](/api/attachments/7S4E6Q5F/fulltext/images/54e98096814d96104385d42f7de74468a0cded919f6ab4009ea7e49f60939b0d.jpg)

Svetlozar Nestorov is an Assistant Professor of Computer Science at the University of Chicago. Dr. Nestorov received his B.S., M.S., and Ph.D. in Computer Science from Stanford University. Dr. Nestorov is involved in active research in a spectrum of areas including artificial intelligence, computational science, bioinformatics, information integration, and web technologies. He has advised and collaborated with a number of startups, including Google. Dr.
