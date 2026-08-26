---
otero_id: 15206
otero_key: "XC7WN492"
title: "A user-friendly marketing decision support system for the product line design using evolutionary algorithms"
authors: "Georgia Alexouda"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.09.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# A user-friendly marketing decision support system for the product line design using evolutionary algorithms

Georgia Alexouda\*

Department of Applied Informatics, University of Macedonia, 156 Egnatia Str, POB 1591, Thessaloniki 540 06, Greece

Received 8 December 2000; received in revised form 6 September 2003; accepted 13 September 2003 Available online 28 October 2003

## Abstract

A marketing decision support system (MDSS) is presented. It has a user-friendly and easy to learn menu driven interface. Its purpose is to assist a marketing manager in designing a line of substitute products. Optimal product line design is a very important marketing decision. The MDSS uses three different optimization criteria. It examines different scenarios using the ‘‘What if analysis’’. Also, it finds optimal solutions only for small sized problems using the complete enumeration method and near optimal solutions for real sized problems using evolutionary algorithms. The user is not forced to be familiar with the underlying models.

<sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Marketing decision support systems; Product line design; Evolutionary algorithms; Heuristic methods; NP-hard problems

## 1. Introduction

More and more managers are faced with a rapidly changing and highly competitive marketing environment. Marketing managers are forced to become more competitive through better decision making.

A decision can be considered as the output of a productive activity whose inputs include intellectual efforts of an individual or a group of individuals, computing hardware and software, data, etc. The advances in computer technology and the computerbased techniques for handling information allow the development of decision support systems, than can play a crucial role in the progress of a firm [7].

There is an obvious need for tools, which can improve marketing decision making. Many efforts have been made to develop suitable software tools, that can act as consultants for marketing managers. There are many opportunities for applications of information systems in the marketing area. The modern information technology and information systems can assist a company to manage the increasing information flow and improve its quality. There is a growing interest in the use of marketing decision support systems (MDSSs) designed to be used in complicated marketing decision making problems [38].

An MDSS is defined as ‘‘a coordinated collection of data, models, analytic tools and computing power by which an organization gathers information from the environment and turns it into a basis for action’’ [26].

MDSSs can be classified according to the questions they deal with. An MDSS has a functionality level 1, when it can answer questions of type ‘‘What happened’’. These MDSSs can provide information about customers, sales, competitors, etc. An MDSS has a functionality level 2, when it can answer questions of type ‘‘Why did it happen’’. These MDSSs can analyze the effects of own and competitors’ marketing actions. They analyze causes of changes in the market. An MDSS has a functionality level 3, when it can answer questions of type ‘‘What will happen if’’. These MDSSs can forecast the effect of marketing actions by using mathematical models to compute the outcome of different actions. An MDSS has a functionality level 4, when it can answer questions of type ‘‘What should happen’’. These MDSSs intend to find the best marketing strategy in a given situation [41].

The product decision is one of the most important decisions in marketing, because it is costly and difficult to change [25]. The rates of failure of new products and their associated losses are very high [9,19,39]. In today’s competitive environment the development of appropriate new products is necessary for the survival of a firm. It is obvious, that before the eventual production and introduction of a new product a company should study very carefully its development. New products play a key role in the growth of sales [19]. The question is: What can a company do to ensure the success of its new products?

The optimal product design problem is a significant part of the new product development problem and one of the most crucial decisions for a firm [8,12]. A reason for the failure of many new products is bad design [24]. Many researchers and marketing managers have dealt with optimal product design. However, only the right choice of the attributes of a product can not guarantee the success of a new product [34].

The purpose of the MDSS presented in this paper is to assist and improve the design of a line of substitute products. Because the product line design problem is NP-hard [22], it is impossible to solve real sized problems in realistic time by using methods, which guarantee the optimal solution. The proposed MDSS uses evolutionary algorithms (EAs) to find near optimal solutions in reasonable time. The aim of the MDSS is to help a marketing manager, who is not forced to be familiar with the underlying models, to deal with questions of levels 3 and 4. The MDSS can facilitate the decision making process and improve the quality of the decision.

The paper is organized as follows. Section 2 deals with the presentation of the product line design problem. In Section 3 the proposed MDSS is presented. In particular, Section 3.1 deals with the data used in the MDSS, Section 3.2 deals with the models contained in the model base of the MDSS and in Section 3.3, the user-interface of the MDSS is presented. Finally, in Section 4, the conclusions of the paper are summarized.

## 2. The product line design problem

‘‘A product is anything that can be offered to a market to satisfy a want or need’’. ‘‘A product line is a group of products that are closely related because they perform a similar function, are sold to the same customer groups, are marketed through the same channels, or fall within given ranges’’ [24]. When the buyers’ preferences are heterogeneous, it is preferable to design a product line than a single product [25]. In this paper by the term ‘‘product line’’ a line of substitute products is meant.

Multidimensional scaling (MDS) and the conjoint method are the basic approaches for modelling the single product or product line design problem. Conjoint analysis has superior analytical capabilities and MDS has superior graphics and data display features [18].

According to the MDS approach the buyers’ preferences are described in terms of brand and individual ideal point locations in an attribute space. The aim of the MDS method is to identify ‘‘best’’ locations for existing or new products. It is assumed that buyers prefer the products, which are closer to their ideal points [18].

The conjoint analysis has had several thousand commercial applications and is one of the most widely accepted methodologies [43]. Many researchers have used the conjoint analysis modelling approach in the product line design problem. Conjoint analysis provides a methodology that links attributes directly to buyers’ preferences. Products are described using attributes and attribute levels. The attribute levels denote the values assumed by the attributes. In the conjoint analysis, a small number of different product profiles is tested and the part-worth utilities obtained from each level of the different attributes, are estimated. In this way, the buyers’ welfare matrix is estimated. The utilities of the candidate products can be computed based on the part-worth utilities [24]. There are software products using different conjoint methods to bring unique advantages to different research situations. Lately the choice based conjoint analysis has become the most widely used conjoint technique in the world [32]. Different estimation methods have been developed in order to meet the needs of different research situations. Recently, an alternative to conjoint methods has been developed for dynamic profiling and customized product offerings [35].

Optimal design is one of the main factors, which determine a product line’s success or failure. There are two different approaches to attack the problem. The first approach selects a product line from a finite set of candidate items. Green and Krieger [17] formulated the buyers’ welfare problem and the seller’s profit problem for the product line selection. Because these problems are NP-complete, they used heuristic methods to solve them. They showed that the greedy and the greedy interchange heuristic perform well for the buyers’ welfare problem. McBride and Zufryden [28] proposed a similar formulation and used a general mathematical program solver for the seller’s profit problem that performs well for a special case. Dobson and Kalish [15,16] extended the model of Green and Krieger and proposed heuristics for solving the two problems. The buyers’ welfare problem has been solved efficiently using the greedy interchange heuristic. A new greedy heuristic has been developed for the seller’s profit problem [16].

The second approach constructs product lines directly from part-worths data. The product line design problem can be formulated within the conjoint analysis framework as a 0 –1 integer programming problem [23]. If the number of attributes and the number of attribute levels is large and the most attribute level combinations define feasible products, it can be computationally infeasible to enumerate the utilities of the candidate items. For this class of problems the second approach is more appropriate. Because the product line design problem is NP-hard, we are forced to use heuristic methods to solve it. A dynamic programming (DP) heuristic method has been developed. It mimics a dynamic program using attributes as stages and attribute levels as states. The computational results have shown that the DP heuristic method can find ‘‘good’’ solutions [23]. Later a Beam Search (BS) heuristic method has been developed. The computational results showed that the BS method finds better solutions and takes less computational time than the DP heuristic method [29].

Recently, EA based solution methods have been proposed for the product line design problem. In particular, EAs have been developed for the buyers welfare problem [1], the seller’s return problem [2] and the share of choices problem [3]. The EAs have several advantages in the way they perform the search process. The DP and the BS heuristic methods work with ‘‘partial’’ product profiles (that means, that a level is selected only for some attributes), while the EAs work with ‘‘complete’’ product profiles. In each stage the DP and the BS heuristics investigate further only the most promising ‘‘partial’’ product profiles (according to the attributes, they have examined), and disregard the others. Consequently, it is possible that they disregard a ‘‘good’’ or ‘‘optimal’’ solution in a very early stage. In the EAs for each attribute level there is a possibility to change. Moreover, the EAs work with a big set of candidate solutions. The computational results showed that the EAs are able to find near optimal solutions in reasonable computational time. They find better solutions than the BS method. Moreover, they take less computational time than the BS method for solving the buyers’ welfare problem and the seller’s return problem. The EA based solution methods have been included in the model base of the proposed MDSS.

## 3. The decision support system

A user-friendly MDSS has been developed for the design of a line of substitute products using one of the following criteria: the buyers’ welfare, the seller’s return and the share of choices. The buyers’ welfare criterion can be used by non-profit organizations. However, buyers’ welfare is very important for the survival of every firm. The importance of the seller’s return criterion is obvious. The share of choices criterion is also an important criterion used in the product line design. The market share is essential for

the survival of an enterprise and it has a significant influence on the profit [37]. The MDSS uses the max utility buyer’s choice rule, where the product associated with the buyer’s maximum utility is deterministically chosen. In the buyers’ welfare criterion the product line is designed so that the total relative welfare of all the buyers of the product line is maximized. In the seller’s return criterion the product line is determined to maximize the seller’s marginal return. Finally, in the share of choices criterion the product line is determined to maximize the number of the new customers. The MDSS does not refer to any specific product. The implementation was done using Borland C+ Builder 3.

The structure of the MDSS is presented in Fig. 1. The necessary data, the models used in the MDSS and the user-interface are presented in Sections 3.1, 3.2 and 3.3, respectively. In order to present the MDSS the following example is used: An enterprise constructing automobiles intends to design two 1.4 comfort automobile models. For each automobile model the same ways of payment will be offered. The example used in the paper is not based on a real application.

![](/api/attachments/XC7WN492/fulltext/images/0c4f989aab3e7e94508d46c83a3c4faa99a929f28a18284302d6706a639426ab.jpg)  
Fig. 1. The structure of the MDSS.

## 3.1. Data

The system allows the systematic storage, request, retrieval and maintenance of all the available data. The data of a problem are stored in more than one files. However, in the operations of the system the user must just enter the name of the problem.

## 3.1.1. The product’s attributes and attribute levels

Let $\Omega { = } \{ 1 , 2 , . . . . , K \}$ denote the set of K attributes and $\Phi _ { k } { = } \{ 1 , 2 , . . . . , J _ { k } \}$ the set of $J _ { k }$ levels of attribute $k { \in } \Omega$

In the example used in the paper, it is considered that each of the automobile models can be described in terms of 14 attributes. Description of the 14 attributes and their levels appears in Table 1. The determination of the appropriate attributes and the attribute levels is a very important task in a conjoint analysis study.

## 3.1.2. Buyers’ part worth utilities

Let $\scriptstyle \Theta = \{ 1 , \ 2 , \ . \ . , \ I \}$ denote the set of I market segments. Let $b _ { i }$ denote the number of buyers of segment $i { \in } \Theta$ . It is assumed that all buyers of a segment have the same part worth utilities. Let $w _ { i j k }$ denote the part worth utility of level $j { \in } \Phi _ { k }$ of attribute $k { \in } \Omega$ for a buyer of segment $i { \in } \Theta$ . As mentioned earlier, the part worth utilities can be estimated using the conjoint analysis. The utility of a product associated to an individual can be computed by adding the part worth utilities of the selected attribute levels. A buyer really obtains the welfare associated to a new product, only if he buys it. Buyers choose the product from a set of available alternatives that gives them maximum utility.

Each buyer’s part worth utilities are normalized by the MDSS to sum to 1. The normalized part worth utility associated with the level $\scriptstyle j \in \phi _ { k }$ of attribute $k { \in } \Omega$ for each buyer of segment $i { \in } \Theta$ is equal to $w _ { i j k } / \sum _ { k \in \Omega }$ $\textstyle \sum _ { j \in \phi _ { k } } w _ { i j k }$ . The normalized part worth utilities are assumed interpersonally comparable.

The attributes and the attribute levels used in the example of the design of automobile models

<table><tr><td>No.</td><td>Attributes</td><td colspan="3">Attribute levels</td></tr><tr><td rowspan="4">1</td><td>Engine type</td><td>1a</td><td>1b</td><td>1c</td></tr><tr><td>Capacity (cm3)</td><td>1360</td><td>1360</td><td>1360</td></tr><tr><td>Power (bhp/rprn), acceleration</td><td>75/5000</td><td>75/5000</td><td>75/5000</td></tr><tr><td>0–100 km/h (s)</td><td>11.2</td><td>12.5</td><td>12.7</td></tr><tr><td>2</td><td>Transmission</td><td>2a: Manual</td><td>2b: Auto</td><td>-</td></tr><tr><td>3</td><td>Power-assisted steering</td><td>3a: No</td><td>3b: Yes</td><td>-</td></tr><tr><td>4</td><td>ABS (anti-lock brake system)</td><td>4a: No</td><td>4b: Yes</td><td>-</td></tr><tr><td>5</td><td>EBD (electronic brakeforce distribution)</td><td>5a: No</td><td>5b: Yes</td><td>-</td></tr><tr><td>6</td><td>Airbags</td><td>6a: Driver and front passenger Impact-Dependent airbags</td><td>6b: 6a+ Side airbags at the front for driver and front passenger</td><td>6c: 6b+ side airbags for rear-seat passengers</td></tr><tr><td>7</td><td>Material of wheels</td><td>7a: Steel</td><td>7b: Alloy</td><td>-</td></tr><tr><td>8</td><td>Air-conditioning system</td><td>8a: No</td><td>8b: Air-condition</td><td>8c: Clima</td></tr><tr><td>9</td><td>Window lifts electric</td><td>9a: No</td><td>9b: At the front</td><td>9c: 9b+ At the rear</td></tr><tr><td>10</td><td>Central locking with electronic immobilizer</td><td>10a: No</td><td>10b: Yes</td><td>-</td></tr><tr><td>11</td><td>Anti-theft alarm system</td><td>11a: No</td><td>11b: Yes</td><td>-</td></tr><tr><td>12</td><td>Sound system</td><td>12a: No</td><td>12b: Yes</td><td>-</td></tr><tr><td>13</td><td>Warranty</td><td>13a: Basic</td><td>13b: With extras</td><td>-</td></tr><tr><td>14</td><td>Price (Euro)</td><td>14a: 11,000</td><td>14b: 13,000</td><td>14c: 15,000</td></tr></table>

## 3.1.3. Competitive environment and the current products of the enterprise

The product that a buyer prefers before the introduction of the new product line is called the status quo product. The utility offered by the status quo product to a buyer of segment $i { \in } \Theta$ is denoted by $u _ { \iota } ^ { * } .$ The status-quo product may be a current product of the enterprise or a product offered by a competitor. The status-quo products play an important role in the buyers’ choice. A buyer prefers a new product to his status quo product, only if it offers him a higher utility. Let $u s _ { i } ^ { * }$ denote the utility that a buyer of segment $i { \in } \Theta$ obtains from the products offered by the seller before the introduction of the new product line. If the status-quo product of a buyer of segment $i { \in } \Theta$ is offered by the seller then $u s _ { i } ^ { * } = u _ { i } ^ { * }$ , otherwise $u s _ { i } ^ { * } = 0$

For each segment $i { \in } \Theta$ the user of the MDSS must insert u\* and declare if the buyers of the segment are<sub>i</sub> already customers of the enterprise. Based on these data the system computes ${ { u } } s _ { i } ^ { * }$ for each segment $i { \in } \Theta$

## 3.1.4. Seller’s return data

Let $\nu _ { i j k }$ denote the seller’s part return if segment $i { \in } \Theta$ buys a product where level $\scriptstyle j \in \phi _ { k }$ of attribute $k { \in } \Omega$ is used. The seller’s return from segment $i { \in } \Theta$ before the introduction of the new product line is denoted by $r _ { i } .$ . If the status quo product of segment $i { \in } \Theta$ is offered by a competitor, then $r _ { i } = 0$

## 3.2. Models

The models of the proposed MDSS can answer the following questions:

1. ‘‘What will happen if the enterprise designs a particular product line?’’

2. ‘‘What product line should the enterprise design in order to maximize the buyers’ welfare?’’

3. ‘‘What product line should the enterprise design in order to maximize the seller’s return?’’

4. ‘‘What product line should the enterprise design in order to maximize the share of choices?’’

In order to answer the first question, the MDSS allows the user to examine different scenarios performing the ‘‘What If Analysis’’. That is, the user can insert a product line profile and the system computes the buyers’ relative welfare, the seller’s marginal return and the additional market share in percent. Also it computes the number of buyers, the number of segments and the segments, that are expected to become new customers of the enterprise. In Table 2, a product line profile containing two different automobile models of the example used in the paper is presented.

In order to answer the next three questions, the MDSS uses two different solution approaches. For each of the three different optimization criteria used in the system, the model base contains an EA and a complete enumeration method. Because the product line design problem is NP-hard, the complete enumeration method can solve only small sized problems.

Table 2  
A candidate product line profile for the example of the design of automobile models

<table><tr><td>No.</td><td>Attributes</td><td>1st Model</td><td>2nd Model</td></tr><tr><td rowspan="4">1</td><td>Engine type</td><td>1360</td><td>1360</td></tr><tr><td>Capacity ( $cm^3$ )</td><td>75/5000</td><td>75/5500</td></tr><tr><td>Max output (bhp/rprn),Acceleration</td><td>11.2</td><td>12.7</td></tr><tr><td>0–100 km/h (s)</td><td></td><td></td></tr><tr><td>2</td><td>Transmission</td><td>Manual</td><td>Manual</td></tr><tr><td>3</td><td>Power-assisted steering</td><td>Yes</td><td>Yes</td></tr><tr><td>4</td><td>ABS (Anti-lock brake system)</td><td>No</td><td>Yes</td></tr><tr><td>5</td><td>EBD (electronic brakeforce distribution)</td><td>No</td><td>Yes</td></tr><tr><td>6</td><td>Airbags</td><td>6a: Driver and front passengerImpact-Dependent airbags</td><td>6b: 6a+ Side airbags at the front for driver and front passenger</td></tr><tr><td>7</td><td>Material of wheels</td><td>Alloy</td><td>Alloy</td></tr><tr><td>8</td><td>Airconditioning system</td><td>Air condition</td><td>Air condition</td></tr><tr><td>9</td><td>Window lifts electric</td><td>At the front</td><td>At the front</td></tr><tr><td>10</td><td>Central locking with electronic immobilizer</td><td>Yes</td><td>Yes</td></tr><tr><td>11</td><td>Anti-theft alarm system</td><td>No</td><td>Yes</td></tr><tr><td>12</td><td>Sound system</td><td>No</td><td>Yes</td></tr><tr><td>13</td><td>Warranty</td><td>Basic</td><td>With extras</td></tr><tr><td>14</td><td>Price (Euro)</td><td>13,000</td><td>15,000</td></tr></table>

The EAs can solve large sized problems, but they cannot guarantee the optimal solution. They take only few seconds to solve real sized problems.

The natural evolution has provided inspiration for developing EAs. EAs work with a set of candidate solutions called population. The population is initialized randomly or using problem specific information. EAs are iterative procedures. Each iteration of an EA is called a generation. EAs seek to improve the quality of the population using a process that mimics that of natural selection and adaptation. A function is used for the fitness evaluation of the candidate solutions. The crossover and the mutation operator are performed in selected solutions from the population to develop the next population. The crossover operator combines candidate solutions to create new candidate solutions. The mutation operator performs random modifications on the candidate solutions. This procedure is repeated until a predefined stopping condition is met.

EAs have often proven a powerful tool for solving problems of many scientific fields. In the last years many real applications of EAs have been developed. More and more researchers of other scientific fields express their interest in the application of EAs [13,20,30]. In the last years some researchers expressed their interest in using EAs in marketing problems, e.g. market segmentation, pricing, site location problem, learning models of consumer choice [20,30]. Furthermore, many researchers developed EAs for integer programming problems. EAs have been proposed for the travelling salesman problem [10,33], the generalised assignment problem [11,42], the set covering problem [4], the packing of polygons [21], etc.

A generic form of EAs can be stated as follows [31]:

Generate an initial population of candidate solutions Repeat

Fitness evaluation of current population Selection

Application of the EA operators Until the stopping condition is satisfied.

An EA approach for solving the single product design problem has been developed [6] and used by a decision support system [5]. It uses the buyers welfare or the share of choices criterion. It can find solutions close to optimal in reasonable computational times. Moreover, it is able to find better solutions than a dynamic programming heuristic method.

The MDSS presented in the current paper, uses EAs for solving the product line design problem. In the EAs used by the MDSS, each item of the population corresponds to a product line profile. Let P denote the set of the candidate product lines. $M = \left| P \right|$ is the population size. The elements of the population matrix $\mathrm { P O P } _ { p m k } ,$ where $p { \in } P , m { \in } \Psi$ and $k { \in } \Omega ,$ , denote the selected level of each attribute. That is, if level $\scriptstyle j \in \phi _ { k }$ of attribute $k { \in } \Omega$ is assigned to product $m { \in } { \Psi }$ of product line $p { \in } P ,$ then $\mathrm { P O P } _ { p m k } { = } j .$

Each EA uses a different fitness evaluation function according to its optimization criterion. The utilities of the PN different products of each product line which are assigned to a buyer of each segment are stored in matrix PR $\mathrm { O D U T I L } _ { M ^ { * } I ^ { * } \mathrm { P N } } .$ . Its elements are computed as follows:

$$
\text { PRODUTIL } _ {p i m} = \sum_ {k \in \Omega} w _ {i (P O P _ {l m k}) k}, p \in P, i \in \Theta , m \in \Psi
$$

Let mVdenote the index m such that $\mathrm { P R O D U T I L } _ { p i m ^ { \prime } } =$ $\mathrm { m a x } _ { m \in \mathcal { V } } \mathrm { P R O D U T I L } _ { p i m } ,$ , where $p { \in } P$ and $i { \in } \Theta$ . As mentioned earlier, a buyer really obtains the welfare associated to a product, only if he buys it. The welfare that a buyer of segment $i { \in } { \Theta }$ will obtain from product line $p { \in } P$ is stored in matrix $\mathrm { W E L F A R E } _ { M ^ { * } I } .$ If $\mathrm { P R O D U T I L } _ { p i m ^ { \prime } } { > } u _ { i } ^ { * }$ , that is, if segment $i { \in } \Theta$ would buy the item mVof the product line $p { \in } P ,$ then WEL $\mathrm { F A R E } _ { p i } = \mathrm { P R O D U T I L } _ { p i m \ l }$ otherwise $\mathrm { W E L F A R E } _ { p i } { = } 0$ . To account for cannibalization the buyers’ relative welfare is considered in the optimization. The total buyers’ relative welfare for each product line is stored in matrix TOTAL\_ $\mathrm { W E L F A R E } _ { M } .$ . Its elements are computed as follows:

$$
\text { TOTAL\_WELFARE } _ {p} = \sum_ {i \in \Theta} b _ {i} (\text { WELFARE } _ {p i} - u s _ {i} ^ {*}),
$$

$$
p \in P.
$$

According to the buyers’ welfare criterion TOTAL\_WELFARE is the fitness evaluation of the population element $p { \in } P .$

For each product line $p { \in } P$ the seller’s return associated to segment $i { \in } \Theta$ is stored in matrix $\mathrm { R E T U R N } _ { M ^ { * } I } .$ If $\mathrm { P R O D U T I L } _ { p i m ^ { \prime } } { > } u _ { i } ^ { * }$ , that is, if segment $i { \in } \Theta$ would buy the item mV of the product line $p { \in } P ,$ then $\mathrm { R E T U R N } _ { p i } = \sum _ { k \in \Omega } \nu _ { i ( \mathrm { P O P } _ { p m _ { k } ^ { \prime } } ) k }$ , otherwise $\mathrm { R E T U R N } _ { p i } { = } 0$ . To account for cannibalization the seller’s marginal return is considered in the optimization. The total marginal return to the seller from each product line $p { \in } P$ is stored in matrix TOTAL<sup>\_</sup> $\mathrm { R E T U R N } _ { M } .$ . Its elements can be computed as follows:

$$
\text { TOTAL\_RETURN } _ {p} = \sum_ {i \in \Theta} (\text { RETURN } _ {p i} - r _ {i}), p \in P.
$$

If two or more items of a candidate product line have the highest utility to a buyer then the most pessimistic case is taken into account. In other words, it is assumed that the buyer will prefer the item with the lowest seller’s marginal return. According to the seller’s return criterion TOTAL ${ \mathrm { R E T U R N } } _ { p }$ is the fitness evaluation of the population element $p { \in } P .$

To account for cannibalization the share of choices is maximized over the subset $\theta ^ { \prime } \subseteq \theta$ of buyers whose status-quo product is offered by a competitor. If $\mathrm { P R O D U T I L } _ { p i m ^ { \prime } } { > } u _ { i } ^ { * }$ , that is, if segment $i \in \Theta ^ { \prime }$ would buy one of the items of the product line $p { \in } P ,$ then $\mathrm { S O C } _ { p i } { = 1 }$ , otherwise $\mathrm { S O C } _ { p i } { = } 0$ . The number of new customers of each candidate product line is stored in matrix $\mathrm { T O T A L \_ S O C } _ { M } .$ Its elements can be computed as follows:

$$
\text { TOTAL\_SOC } _ {p} = \sum_ {i \in \Theta^ {\prime}} b _ {i} \text { SOC } _ {p i}, \text { where } p \in P
$$

According to the share of choices criterion $\mathrm { T O T A L \_ S O C } _ { p }$ is the fitness evaluation of the population element $p { \in } P .$

In each generation of the EA using the buyers’ welfare criterion and the EA using the seller’s return criterion the best items of the current population are selected to produce the 40% of the next population. Moreover, the 40% and 20% of the new population elements are produced using the uniform crossover operator and the mutation operator, respectively. The above iterative process is repeated until the best candidate solution does not improve in 10 consecutive generations. The population size is set equal to 150, that is $M = 1 5 0$

In each generation of the EA using the share of choices criterion the 45%, 45% and 10% of the new population elements are produced using the selection method, the uniform crossover operator and the mutation operator respectively. When in 20 consecutive generations the best candidate solution does not improve, the EA terminates. The population size is set equal to 180, that is M = 180.

![](/api/attachments/XC7WN492/fulltext/images/a4cd260874ee0028cfb9a878eb4249f5a64a2dbc685655b18fac3883a55d103f.jpg)  
Fig. 2. The main window of the MDSS.

![](/api/attachments/XC7WN492/fulltext/images/c4b394aedc1eda4649b81e7c34ee5ba1ebf48118565c9c73c5cad3047a635f17.jpg)  
Fig. 3. The first window of the New choice of the Problem menu: Entry of the attributes and the numbers of the attribute levels.

These parameters influence the performance of the EAs. From our experience on a wide range of different problem sizes the selected parameters perform well. For more details about the EAs used in the MDSS, see Refs. [1 – 3].

## 3.3. User-interface

The user-interface of a decision support system can influence its acceptance by the user. In order to achieve the acceptance of a decision support system, the user’s skills, needs and expectations must be seriously considered in the design and implementation of the user-interface [27,36]. The interaction style can influence the user’s attitudes toward software packages. The more common the interface, the less effort and training for a user to learn to use it [14,40].

In order to improve the MDSSs chances for success, a menu-driven user-interface with common easyof-use features such as grid formats, navigators for grids and pop-up menus, has been chosen. Short cuts are used to perform an action quickly. Tools provide an easy to understand visible way to present options to the user. It is assumed that the end-users are familiar with using the Windows environment. No special knowledge about the underlying models is required to use the system. The end-users have to insert the necessary data and the results of the models appear in an easy to understand form. There are many benefits to be gained by the selected user-interface, such as facilitation of learning, reduced error rates, etc.

![](/api/attachments/XC7WN492/fulltext/images/ee21031f0e8b0515d72305b27f6688e96ca95d2d8c696822cc8df21ff57ef29a.jpg)  
Fig. 4. The completed first window of the New choice of the Problem menu.

![](/api/attachments/XC7WN492/fulltext/images/c4498f3fed2c8f9a46fc940e5c625f6656f2d59fbbe7d04fbc0a2b3239710ef7.jpg)  
Fig. 5. The second window of the New choice of the Problem menu: Entry of the attribute levels.

Indicatively, some of the windows of the MDSS are presented. The main window is presented in Fig. 2. The menu bar appears at the top of the window and includes the following menus: Problem, Edit, What If Analysis, Solvers and Help. Each menu option can be selected using the mouse or the keyboard. The status bar appears at the bottom of the window and informs the user about the results of his commands. In the beginning the status bar prompts the user to insert a problem. The Problem menu provides familiar choices such as New, Open, Save, Save As, Print, Close and Exit. Windows common dialog boxes are used for operations such as opening, saving and printing problems. The Help command allows the user to choose the subject he wants information about. It provides all necessary instructions for using the MDSS.

![](/api/attachments/XC7WN492/fulltext/images/93e6430fcdf5d1d4a09581bd5bd5e50907e90d099e6ca75cf4d2702ec8ec2674.jpg)  
Fig. 6. The completed second window of the New choice of the Problem menu.

![](/api/attachments/XC7WN492/fulltext/images/8fc5bab5592daac54af3f3bb50cbaad4ce733d1f281b53e46b6e4befadc07419.jpg)  
Fig. 7. The third window of the New choice of the Problem menu: Entry of the data of segments.

The New choice from the Problem menu displays the window shown in Fig. 3. In the beginning of the data entry process, the MDSS prompts the user to input the attributes and the number of attribute levels in a grid format. Using a grid format, for the data entry process, is both easy to learn and easy to use. The first column corresponds to the attributes and the second column corresponds to the number of the attribute levels. The navigator provides the user with a simple control for navigating through the records and manipulating them. In particular, the navigator consists of a series of buttons, that allow the user to go to the first record, go to the previous record, go to the next record, go to the last record, insert a new record, delete the current record, modify the current record, post data changes and cancel data changes. The completed window for the example used in the paper is presented in Fig. 4.

After pressing the ‘‘Continue’’ button the window shown in Fig. 5 is displayed. The attributes are displayed in the first column of the table and the user is asked to insert the levels of each attribute in the next columns. In the abundant columns of some attributes the symbol ‘‘\*’’ is displayed. The completed window for the example used in the paper is presented in Fig. 6.

When the user has finished entering the attribute levels, the system waits for him to insert the segments and the number of buyers of each segment in the window shown in Fig. 7.

In the next window with the caption ‘‘Data of Buyers’ Welfare’’ (Fig. 8), the first column corresponds to the segments, the second column to the attributes and the third column to the attribute levels. The user is asked to insert the corresponding part worth utility in the last column.

In the next window (Fig. 9) the first column corresponds to the segments and its elements are displayed by the system. In the two next columns the user has to enter the status-quo products and their utilities. In the forth column the user is asked to indicate, if the segment is already customer of the enterprise, using a pop-up menu, which contains the choices: ‘‘Yes’’ and ‘‘No’’. In the last column, for each segment the user has to insert the seller’s return before the introduction of the new product line. For the segments whose status-quo product is offered by a competitor, the system sets the value of 0.

![](/api/attachments/XC7WN492/fulltext/images/429d9c83092f917e9e0aa53f0bafcea4e95a2a145cdbac36619df53564d68c38.jpg)  
Fig. 8. The forth window of the New choice of the Problem menu: Entry of the buyers’ welfare matrix.

![](/api/attachments/XC7WN492/fulltext/images/a06f747e90596f03cdf88adfd08fcca1c585b7a5f2f068f0429d4b1ced68743b.jpg)  
Fig. 9. The fifth window of the New choice of the Problem menu: Entry of the status-quo products.

The next window prompts the user to insert the seller’s part return data. As shown in Fig. 10, the system displays the elements of the first three columns. The first column corresponds to the segments, the second column to the attributes and the third column to the attribute levels. The user is asked to insert the corresponding seller’s part return data in the last column. This is the last step in the data entry process.

After completing the data entry process, the user can proceed with performing the ‘‘What if analysis’’ or solving the problem using one of the optimization criteria.

The Edit command displays the six windows presented earlier, that contain the input data of the current problem. The user is enabled to modify the data of the buyers’ welfare and the seller’s return.

The What If Analysis choice displays the window shown in Fig. 11, which prompts the user to enter the number of items of the product line. The user has to enter a product line profile using a pop-up menu, which contains the levels of each attribute. The output from the What If Analysis option displays the buyers’ relative welfare, the seller’s marginal return and the additional market share in percent. Also it presents the number of buyers, the number of segments and the segments, that are expected to become new customers of the enterprise. The user is enabled to send the results of the ‘‘What if analysis’’ to the printer.

![](/api/attachments/XC7WN492/fulltext/images/4293e12a946930765c9408ae31ac63aa19ded38d3bcee9b000b50767ea8f08f2.jpg)  
Fig. 10. The last window of the New choice of the Problem menu: Entry of the seller’s return matrix.

![](/api/attachments/XC7WN492/fulltext/images/f78225e2ae2158d7758cbaacd957eb696dc5e08f3d1208d2da91c8592cf4682e.jpg)  
Fig. 11. Entry of data for the ‘‘What If Analysis’’.

The Solvers menu, as shown in Fig. 12, allows the user to choose the optimization criterion of interest. He is enabled to choose among the buyers’ welfare, the seller’s return and the share of choices criteria. Then he can select and execute one of the two available solution methods (either the complete enumeration method or the EA). The solution methods contained in the model base have been described in Section 3.2. The system begins the solution process by asking the user to insert the number of items of the product line. Then, the selected solution method is performed and the buyers’ relative welfare, the seller’s marginal return and the additional market share in percent are displayed. Also the system presents the number of buyers, the number of segments and the segments, that are expected to become new customers of the enterprise. Moreover, the proposed product line profile is displayed. The user is enabled to send the results to the printer to obtain a hard copy printout of the results of the selected solution method.

Alternatively, the end-user may use the tools to communicate with the system. The tools of the

![](/api/attachments/XC7WN492/fulltext/images/47f895a0a89a4195c6f81730e5bec50bf35141e7f1de39f46d3c58943b968e89.jpg)  
Fig. 12. The solvers menu.

MDSS, shown in Fig. 2, enable the user to insert a new problem, open an existing problem, save a problem, print the input data of the current problem, edit the current problem, perform the ‘‘What if analysis’’, perform the corresponding enumeration method for each of the optimization criteria, perform the corresponding EA for each of the optimization criteria and get help.

As shown, a user who is familiar with other Windows applications can easily use the proposed MDSS.

## 4. Conclusions

To summarize, an MDSS for the product line design problem has been presented. It can be used as a marketing manager’s consultant. It allows the decision-maker to examine different scenarios by using the ‘‘What if analysis’’. Moreover, the system uses EAs, which are capable of finding near optimal solutions for real sized problems in reasonable time. Only for small problem sizes it uses the complete enumeration method to find an optimal solution. It deals with the buyers’ welfare problem, the seller’s return problem and the share of choices problem.

The Windows environment and the Borland C+ Builder 3 used for the system development, offer a friendly and easy to learn graphical interface for the end-users. The user is able to communicate with the MDSS in a number of different ways using menu options, shortcuts or tools. The system does not require that the user has special knowledge about computers and he is not forced to be familiar with the underlying models. Also, the user can obtain help by the system. However, it is assumed that he has some familiarity with the use of the Windows environment.

Marketing managers are often faced with difficult problems, which can be solved only using heuristic methods. Heuristic methods don’t guarantee the optimal solution. For that reason it is desirable for an MDSS which deals with such problems to include in its model base heuristic methods, which find near optimal solutions.

The proposed MDSS can be improved by using more than one heuristic methods to attack the problem. EAs work with a set of candidate solutions. The first set of candidate solutions can include the solutions of other methods. By this way EAs can be used as a second step of other heuristic methods. The fact, that they can in many cases improve the solutions of other methods, is an important advantage.

The MDSS can be improved to consider more than one objectives simultaneously and suggest more than one different solutions. Furthermore, the MDSS can be extended to assist a broad range of marketing decisions.

## References

[1] G. Alexouda, K. Paparrizos, A genetic algorithm approach to the buyers’ welfare problem of product line design: a comparative computational study, Yugoslav Journal of Operations Research 9 (2) (1999) 223 – 233.

[2] G. Alexouda, K. Paparrizos, A genetic algorithm approach to the product line design problem using the seller’s return criterion: an extensive comparative computational study, European Journal of Operational Research 134 (1) (2001) 167 – 180.

[3] G. Alexouda, An Evolutionary Algorithm Approach to the Share of Choices Problem in the Product Line Design, Computers and Operational Research (accepted).

[4] K. Al-Sultan, M. Hussian, J. Nizami, A genetic algorithm for the set covering problem, Journal of the Operational Research Society 47 (5) (1996) 702–709.

[5] P. Balakrishnan, V. Jacob, Triangulation in decision support systems: algorithms for product design, Decision Support Systems 14 (4) (1995) 313–327.

[6] P. Balakrishnan, V. Jacob, Genetic algorithms for product design, Management Science 42 (8) (1996) 1105 – 1117.

[7] R. Bonczek, C. Holsapple, A. Whinston, Foundations of Decision Support Systems, Academic Press, New York, 1981.

[8] M. Bruce, M. Whitehead, Putting design into the picture: the role of product design in consumer purchase behavior, Journal of the Market Research Society 30 (1988).

[9] Business Week, Flops: Too Many New Products Fail (16 August 1993).

[10] S. Chatterjee, C. Carrera, L. Lunch, Genetic algorithms and traveling salesman problems, European Journal of Operational Research 93 (3) (1996) 490– 510.

[11] P. Chu, J. Beasley, A genetic algorithm for the generalised assignment problem, Computers and Operations Research 24 (1) (1997) 17 – 23.

[12] R. Cooper, E. Kleinschmidt, New products: what separates winners from losers, Journal of Product Innovation Management 4 (3) (1987) 169 – 184.

[13] L. Davis, Handbook of Genetic Algorithms, Van Nostrand Reinhold, New York, 1991.

[14] S. Davis, S. Wiedenbeck, The influence of interaction style and experience on user perceptions of software packages, International Journal of Human-Computer Studies 46 (5) (1997) 563–588.

[15] G. Dobson, S. Kalish, Positioning and pricing a product line, Marketing Science 7 (2) (1988) 107 – 125.

[16] G. Dobson, S. Kalish, Heuristics for positioning and pricing a product line using conjoint and cost data, Management Science 39 (2) (1993) 160 – 175.

[17] P. Green, A. Krieger, Models and heuristics for product line selection, Marketing Science 4 (1) (1985) 1 – 19.

[18] P. Green, A. Krieger, Recent contribution to optimal product positioning and buyer segmentation, European Journal of Operational Research 41 (1989) 127–141.

[19] G. Gruenwald, New Product Development, 2nd ed., NTC Business Books, Illinois, 1992.

[20] S. Hurley, L. Moutinho, N. Stephens, Solving marketing optimization problems using genetic algorithms, European Journal of Marketing 29 (4) (1995) 39– 56.

[21] J. Jakobs, On genetic algorithms for the packing of polygons, European Journal of Operational Research 88 (1) (1996) 165–181.

[22] R. Kohli, R. Krishnamurti, Optimal product design using conjoint analysis: computational complexity and algorithms, European Journal of Operational Research 40 (2) (1989) 186–195.

[23] R. Kohli, R. Sukumar, Heuristics for product-line design using conjoint analysis, Management Science 36 (12) (1990) 1464–1478.

[24] P. Kotler, Marketing management: analysis, planning, implementation and control, 9th ed., Prentice-Hall International, New Jersey, 1997.

[25] G. Lilien, P. Kotler, S. Moorthy, Marketing Models, Prentice Hall International Editions, New Jersey, 1992.

[26] J. Little, Decision support systems for marketing managers, Journal of Marketing 43 (3) (1979) 9 – 26.

[27] G. Marakas, Decision Support Systems in the 21th Century, Prentice-Hall, New Jersey, 1999.

[28] R. McBride, F. Zufryden, An integer programming approach to the optimal product line selection problem, Marketing Science 7 (2) (1988) 126–140.

[29] S. Nair, L. Thakur, K. Wen, Near optimal solutions for product line design and selection: Beam search heuristics, Management Science 41 (5) (1995) 767 – 785.

[30] V. Nissen, An overview of evolutionary algorithms in management applications, in: J. Biethahn, V. Nissen (Eds.), Evolutionary Algorithms in Management Applications, Springer, Berlin, 1995, pp. 43–97.

[31] V. Nissen, J. Biethahn, An introduction to evolutionary algorithms, in: J. Biethahn, V. Nissen (Eds.), Evolutionary Algorithms in Management Applications, Springer, Berlin, 1995, pp. 3 – 43.

[32] B. Orme, Which Conjoint Method Should I Use? Sawtooth Software: Research Paper Series (2003), www.sawtoothsoftware. com.

[33] J.-Y. Potvin, Genetic algorithms for the traveling salesman problem, Annals of Operations Research 63 (1996) 339–370.

[34] N. Rackhan, From experience: why bad things happen to good new products, Journal of Product Innovation Management 15 (3) (1998) 201 – 207.

[35] T. Raghu, P. Kannan, H. Rao, A. Whinston, Dynamic profiling of consumers for customized offerings over the Internet: a model and analysis, Decision Support Systems 32 (2) (2001) 117– 134.

[37] D. Szymanski, S. Bharadwaj, R. Varadarajan, An analysis of the market share—profitability relationship, Journal of Marketing 57 (3) (1993) 1 – 18.

[36] V. Sauter, Decision Support Systems, Wiley, New York, 1997.

[38] J. Talvinen, Information systems in marketing. Identifying opportunities for new applications, European Journal of Marketing 29 (1) (1995) 8 –26.

[39] G. Urban, J. Hauser, Design and Marketing of New Products, 2nd ed., Prentice-Hall, New Jersey, 1993.

[40] S. Wiedenbeck, S. Davis, The effect of interaction style and training method on end user learning of software packages, Interacting with Computers 11 (2) (1998) 147– 172.

[41] B. Wierenga, P. Ophuis, E. Huizingh, P. Campen, Hierarchical scaling of marketing decision support systems, Decision Support Systems 12 (3) (1994) 219– 232.

[42] J. Wilson, A genetic algorithm for the generalised assignment problem, Journal of the Operational Research Society 48 (8) (1997) 804–809.

[43] D. Wittink, P. Cattin, Commercial use of conjoint analysis: an update, Journal of Marketing 53 (3) (1989) 91 – 96.

Georgia Alexouda. Her undergraduate degree and PhD is from the Department of Applied Informatics in the University of Macedonia, where she teaches Decision Support Systems. Her research interests are in Decision Support Systems, Evolutionary Algorithms, Heuristic Methods, NP-complete and NP-hard problems, Multiobjective optimization and Information Systems in Marketing.
