---
otero_id: 7648
otero_key: "FUT3YCA2"
title: "A decision support system for product design selection: A generalized purchase modeling approach"
authors: "B. Besharati; S. Azarm; P.K. Kannan"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.01.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for product design selection: A generalized purchase modeling approach

B. Besharati<sup>a</sup>, S. Azarm<sup>a,T</sup>, P.K. Kannan<sup>b</sup>

<sup>a</sup>Department of Mechanical Engineering, A. James Clark School of Engineering, University of Maryland, College Park, MD 20742, United States

<sup>b</sup>Department of Marketing, Robert H. Smith School of Business, University of Maryland, College Park, MD 20742, United States

Available online 23 February 2005

## Abstract

Selection of a final design for a new product that is to be introduced in the market is a very critical step in the new product development process. The selection needs to consider three factors of importance: anticipated market demand for the design, designers’ preferences, and uncertainty in achieving predicted design attribute levels under different usage conditions and situations. We propose a generalized purchase modeling approach that considers all of the above factors and develop a customer based expected utility metric that forms the basis for a Decision Support System (DSS) for supporting the selection in product design. We illustrate the modeling approach and the use of DSS with the help of a case example that highlights the utility of the proposed DSS.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Product design selection; Selection under uncertainty; Multi-attribute decision making

## 1. Introduction

The final decision to select a particular design for a given product is perhaps the most critical stage in product design development. Obviously, such a decision is influenced by many factors, the specifics of which are not known a priori during the design stage. As such, a quantitative basis for comparison and selection of the best design solution among a host of alternatives could greatly impact the eventual success or failure of a product in the market. The importance of this issue prompts for more sophisticated design selection criteria and methods to incorporate all important factors of interest into the selection of a single final design.

There are three main factors that influence a successful product design selection: 1) market demand based on customers’ preferences; 2) designer’s preferences based on his/her knowledge and experience with design issues and market issues; and 3) uncertainty in achieving the predicted design attribute levels (or performance). For example, a design alternative may fail to become a successful product if it does not gain and maintain enough market demand. On the other hand, considering the market demand by itself does not secure a successful product in the market. For instance, introducing a product at low price into the market might increase the initial product demand significantly. However, it may not be possible to sustain such a demand in the longer run (repurchase of the product) due to the poor performance (and reliability) with respect to some of the product attributes. A designer’s knowledge and experience can be very useful in predicting product performance if customers’ evaluations are not known a priori. As such, the designer’s preferences can be used to specify the product performance in terms of its attributes, which customers may not know or consider at the point of purchase. Also, a designer can incorporate the specifics of competitive products in his/her preference function so that the new design can be appropriately positioned in the market relative to competition [22]. Finally, because of the uncertainty in product design parameters (such as, manufacturing tolerances and variations in the product usage environment), the design attribute levels can deviate from their nominal values and affect the product performance. Such uncertainty can make or break a product in the market and it is, thus, important to consider these variations in selecting a final product design.

There are many individual and group decision making techniques in the literature that can be used for product design selection, among which Multi-Attribute Utility Theory (MAUT) [19], Analytical Hierarchy Process (AHP) [25], and Conjoint Analysis [16,17] are used extensively. While many of these techniques address a subset of the above identified factors, none of them address all three factors simultaneously. For instance, MAUT employs the von Neumann and Morgenstern (vNM) utility theory to model an individual’s (a designer’s or customer’s) preferences [28]. Many applications of MAUT that are used for modeling a decision maker’s preferences for rank ordering and selection among a set of alternatives can be found in marketing and management science literature [4,9,11]. However, applications of MAUT for customer elicitation using a lottery technique are mostly limited to highly educated respondents [18], which may be applicable to a small segment of the market. While AHP is relatively easier to implement for any customer group [15], its simplification and unwanted rank reversal may sacrifice its predictive validity especially when the design attributes are significantly correlated. Conjoint Analysis (CA) is another approach for multi-attribute decision making problems where the focus is preference elicitation at the individual customer level. Two types of conjoint models are discussed in the literature: compositional (self explicated) and decompositional. In the self explicated methodology, the customers are asked to give the importance weight for each attribute followed by the rank ordering of distinct levels for each attribute. There are several issues related to the self explicated approaches. First, the customers may not be able to provide the accurate information in terms of the weights (e.g., due to socially accepted values). Moreover, there is a low chance of detecting potential nonlinearity in partworth (e.g., utility) function. Conversely, in decompositional approaches the customers are only asked to express their preference or choice among the product profiles, and it is the researchers’ responsibility to ensure that relevant attributes considered in the profile generation. In most cases, the preference model is presumed to be of the same general structure for all individuals in a population sample [17]. As such, even by allowing an error term, a CA model might not represent the precise behavior of all individuals in the sample. In other words, different segments (or even individuals) in the market may have different preference structures. Therefore, a reasonably accurate customer categorization (market segmentation) is perhaps the most critical step in the marketing study [24].

In addition, in order to overcome preference aggregation problems and account for choice uncertainty, a conjoint model can be based on a discrete choice model that utilizes an individual’s selection behavior [20]. Among the discrete choice models, the probabilistic-based models such as multinomial logit [5,21], probit [12], mixed logit–probit [7], and also deterministic models such as the first choice model [26] are based on the customers’ utilities. All of the above-mentioned selection models are compensatory, and are likely to select the product with the highest customer utility. However one can argue that the purchase decision rules can be non-compensatory. In other words, many customers may not choose the product with the highest aggregated utility due to economic or other considerations (e.g., purchase reservation prices). This issue eventually makes the pure compensatory decision rules difficult to implement, especially in industrial markets where decision rules are not purely compensatory. Hence, the choice model needs to allow for the consumers’ acceptable bounds on each attribute while taking into account their interactions. In many situations in industrial markets the manufacturers (i.e., product components consumers) set acceptable bounds on the product specifications (i.e., clearly explicated decision rules for selection of equipments). Our methodology takes into account both compensatory and non-compensatory decision rules through our generalized purchase modeling approach. The customers purchase decision rules is obtained using a self explicated technique. Moreover, our approach not only considers the customers purchase criteria and designer’s preferences in the selection of the product design, but also it allows for the uncertainties in attaining the specified nominal attribute levels. A decision support system based on the three mentioned factors will, therefore, be market focused and also take into account the realities of the design development process.

There are several market-based DSS methodologies reported in the literature to aid product selection [10,23], single product design selection [2,3], and product line design [1]. The selection criteria in these methods are mostly either based on maximization of the market share, the seller’s return or minimization of job completion time. Nevertheless, there are uncertainties involved with each of the mentioned problems that can affect the results significantly. We propose a generalized purchase function, an extension of our approach [6] to model the customer purchase behavior to capture the impact of all the above mentioned three factors. The customers purchase criteria (captured using a self-explicated approach) can be given as an input to our newly developed DSS for final product design selection. The capability of the new DSS to handle sophisticated and realistic decision-making situations is demonstrated with an example in industrial market, i.e., product design selection of a power electronic module.

The organization of the rest of this paper is as follows. In Section 2, a description of the Customerbased Expected Utility (CEU) metric is provided, along with a generalized DSS to model customer purchase decision. Section 3 is devoted to an application of the proposed methodology to an example: product design selection for power electronic modules. Finally, the concluding remarks of the paper are provided in Section 4.

## 2. Methodology

As discussed in the previous section, we account for three factors that impact product design selection significantly: 1) market demand; 2) uncertainty in achieving nominal attribute levels; and 3) designer’s preferences. The overall framework of our approach is shown in Fig. 1. A number of product alternatives are generated within the design process. The product attributes (both performance and market related) can be obtained using design simulation tools and marketing models. The main objective of this paper is to present a DSS that aggregates the above factors into a single-valued (scalar) metric, one that accounts for the utility function of the designer, the product’s demand (based on customer’s preferences), and the uncertainty in attaining a desired attribute level. Thus, our DSS can be used to identify the optimal product design from a large set of product design alternatives. In the following subsections, each of the factors used in our DSS is discussed separately.

## 2.1. Normalized market demand

We define the normalized market demand of a product as the percentage of customers in a market who decide to purchase a product with a given combination of attribute levels. One could predict whether or not a customer buys a certain product with a combination of attribute levels. By aggregating such a purchase decision over a representative sample of customers, the demand of a product can then be estimated. Here, it is assumed that the customers have prior experiences with similar existing products in the market and therefore, they can evaluate the product and make a purchase decision based on the product attributes. The non-compensatory choice models do not make tradeoffs among the attributes directly such as compensatory models do (e.g., multi attribute utility function). The three most important noncompensatory approaches are the conjunctive, disjunctive and lexicographic [14]. In the following, we define a generalized purchase decision model, and relate it to noncompensatory choice models.

![](/api/attachments/FUT3YCA2/fulltext/images/e9e350ea27bb8ac68e797dedd2b9cb7c9da22b0bf2bd7d9f90a5ad0447f3419f.jpg)  
Fig. 1. Overall product design selection framework.

## 2.1.1. Generalized purchase decision

A customer’s purchase decision function $D _ { \mathfrak { p } } ( \mathbf { x } )$ is defined as follows:

$$
D _ {p} (\mathbf {x}) = \left\{ \begin{array}{l l} 1 & \text { If   customer   buys   a   product   at } \mathbf {x} \\ 0 & \text { If   customer   does   not   buy   a   product   at } \mathbf {x} \end{array} \right. \begin{array}{l} (\mathbf {x} \text { is   within   customer's   acceptable   ranges }) \\ (\text { Otherwise }) \end{array}\tag{1}
$$

where $\mathbf { x } { = } ( x _ { 1 } , . . . . , x _ { n } )$ is the vector of design attributes.

The above definition does not clearly address the relation between components (attributes) of vector x. To address the issue of the interactions between attributes, we introduce the noncompensatory customer choice models: Conjunctive. In a conjunctive choice model, the customer would purchase the product only if all of the attributes of the product are within the customer’s acceptable ranges. If any attribute is deficient, the purchase decision function for that design alternative becomes zero.

$$
D _ {p} (\mathbf {x}) = \left\{ \begin{array}{l l} 1 & \text {   If   customer   buys   a   product   at   } \mathbf {x} \\ 0 & \text {   If   customer   does   not   buy   a   product   at   } \mathbf {x} \end{array} \right. \quad \text {(All   attributes   are   within   customer's   acceptable   ranges)} \quad \text {(Otherwise)}\tag{2}
$$

Disjunctive. In a disjunctive model it is sufficient that at least one attribute of the product satisfies the customer. For instance, under the conjunctive model, the customer may insist on purchasing a light weight and inexpensive product. However under the disjunctive model the customer would settle for a product with either low weight or low price.

$$
D _ {p} (\mathbf {x}) = \left\{ \begin{array}{l l} 1 & \text { If   customer   buys   a   product   at } \mathbf {x} \\ 0 & \text { If   customer   does   not   buy   a   product   at } \mathbf {x} \end{array} \right. \quad \text {(At least one attributes is within customer's acceptable ranges)}\tag{3}
$$

Lexicographic. In a lexicographic model all attributes of the product are considered in a hierarchical manner from the most important to the customer all the way to the least important. In other words, the product is evaluated based on the most influential attribute first, and if there is a tie, the second most influential attribute is used and so on until there is no tie among the products under consideration.

![](/api/attachments/FUT3YCA2/fulltext/images/358f1848bc00778bd397db9a513436e44c23a2143bcacbfbbeb8384105cfb152.jpg)  
Fig. 2. Binary decision diagram representation of a customer choice model.

A customer’s preferences with respect to several attributes may be too complicated to be modeled simultaneously by one of the above-mentioned choice models. However a combination of noncompensatory models can capture the interactions among attributes more naturally. For example, the following customer’s purchase scenario cannot be handled with a pure disjunctive or conjunctive choice model:

<sup>b</sup>The price should not be over \$100, and the weight needs to be no more than 3 lbs, but if the product is on sale for less than \$60, then I am willing to buy one that is up to 5 lbs in weight<sup>Q</sup>.

By using Boolean expression, we can model the above customer’s purchase decision, as shown in Eq. (4). The binary decision diagram of such a customer is depicted in Fig. 2. The solid lines in Fig. 2 are used when the statement (or event) holds, while the dashed lines indicate that the event does not hold. For a thorough description of binary function representations, see [8].

$$
D _ {p} (\mathbf {x}) = \left\{ \begin{array}{l l} 1 & [ (\text { cost } <   1 0 0) \land (\text { weight } <   3) ] \lor [ (\text { cost } <   6 0) \land (\text { weight } <   5) ] \\ 0 & \text { Otherwise } \end{array} \right. = \left\{ \begin{array}{l l} 1 & (A \land B) \lor (C \land D) \\ 0 & \text { Otherwise } \end{array} \right.\tag{4}
$$

The customer purchase decisions can be modeled by a combination of the aforementioned noncompensatory choice models. Basically it is possible to represent every Boolean expression using a Conjunctive Normal Form (CNF) or Disiunctive Normal Form (DNF) and either one can be converted to the other The CNF can be constructed by the conjunction of disjunctive expressions. The general form of CNF is shown in Eq. (5).

$$
\left(t _ {1} ^ {1} \vee t _ {2} ^ {1} \vee t _ {3} ^ {1} \vee \dots \vee t _ {k _ {1}} ^ {1}\right) \wedge \dots \wedge \left(t _ {1} ^ {l} \vee t _ {2} ^ {l} \vee t _ {3} ^ {l} \vee \dots \vee t _ {k _ {l}} ^ {l}\right) \equiv \bigwedge_ {j = 1} ^ {l} \left(\bigvee_ {i = 1} ^ {k _ {j}} t _ {i} ^ {j}\right)\tag{5}
$$

Likewise, DNF can be shown as in Eq. (6).

$$
\left(t _ {1} ^ {1} \wedge t _ {2} ^ {1} \wedge t _ {3} ^ {1} \wedge \dots \wedge t _ {k _ {1}} ^ {1}\right) \vee \dots \vee \left(t _ {1} ^ {l} \wedge t _ {2} ^ {l} \wedge t _ {3} ^ {l} \wedge \dots \wedge t _ {k _ {l}} ^ {l}\right) \equiv \bigvee_ {j = 1} ^ {l} \left( \begin{array}{c} k _ {j} \\ \wedge \\ i = 1 \end{array} t _ {i} ^ {j}\right)\tag{6}
$$

The purchase decision of the customer shown in Fig. 2 is defined as a DNF. However, it can be converted to CNF as shown in Eq. (7).

$$
D _ {p} (\mathbf {x}) = \left\{ \begin{array}{l l} 1 & (A \lor C) \land (B \lor C) \land (A \lor D) \land (B \lor D) \\ 0 & \text { Otherwise } \end{array} \right.\tag{7}
$$

For a given sample of customers, the normalized demand q of a product with a vector of attribute x can be calculated by:

$$
q (\mathbf {x}) = \frac {\sum_ {i = 1} ^ {N} D _ {p _ {i}} (\mathbf {x})}{N}\tag{8}
$$

where N stands for the total number of customers in the sample, and $D _ { \mathfrak { p } _ { i } }$ refers to the purchase decision of the ith customer in the sample.

In obtaining the normalized demand, the purchase decision rules for each customer are captured through a selfexplicated approach. Every customer expresses his/her purchase decision criteria in one of the above mentioned normal forms. In this model, it is assumed that the sampling errors are insignificant (i.e., the sample resembles the whole population). In industrial markets, which is the focus of our study, it is quite common for sales team to interact with customers to understand client requirements and criteria better. In many cases, clients may explicitly provide their specific criteria and information on acceptable upper and lower bounds on attributes (arising from performance and quality considerations). However, tradeoff information between attributes is generally not provided. This information is obtained directly through self-explicated responses (as in a conjoint study) from the buyers/buyer segments.

## 2.2. Uncertainty in achieving nominal attribute levels

In a product design process, it is common to use design simulation tools. These tools can help to simulate the performance (design attributes) of a design to the variation in input parameters. The uncertainty in an attribute level is generally due to uncontrollable randomness in input design parameters (such as manufacturing tolerances, deviation in the source voltage and frequency, and changes in the environment temperature). As a result, the design attribute levels may deviate from the nominal values. When there is enough information (e.g., data) about the uncertainty in input parameters, an appropriate probability distribution can be constructed. The variations in the design attribute levels can be modeled by mapping from the input design parameters space to the design attribute space through the design simulation tools. Monte Carlo simulation is one of the common methods for modeling the uncertainties by constructing a design attribute distribution, hereafter referred to as $p _ { i } .$ In Monte Carlo simulation, a sample of possible input design parameters (representing an appropriate distribution) is selected and mapped into the corresponding attribute levels, which in turn creates a probability distribution for the uncertainty in an attribute level. Such mappings can be performed by the functional form of the design performance attributes (if available) or by the design simulation software (e.g., numerical results of a finite element analysis, computational fluid dynamics, etc.). As an example, we can estimate the overall weight of a product (e.g., a single chip module) by adding the weight of the chip and the PCB board. Then, the variability in the total weight of the module can be estimated by sampling the weight of each component (Chip and PCB) and calculate the total weight by adding up the component weights.

It should be noted that many important aspects of a product can be simulated by using design simulation software. The performance and quality of a product is then directly assessed by examining the impact of product design attributes on product quality and performance based on the simulation output results. For example, in power electronic device development, the thermal performance of a device (e.g., junction temperature) and the development cost (e.g., planning, design, parts, assembly, etc.) are two attributes that represent the quality and performance of that design alternative. Our methodology uses the design simulation software and subsequently takes the performance and quality aspects of each design alternative into account during the selection process.

The proposed design selection approach is able to allow for the uncertainties in the design performance attributes and capture the customers’ purchase decisions along with the designer’s preference for selecting the optimal product design.

## 2.3. Designer’s preference

The designer’s preference is one of the key elements in product design and development. It reflects the designer’s experience and expertise of the design and knowledge of the market. Moreover, it enables the consideration of potential design alternatives that are promising from the designer’s (or producer’s) point of view (for example, identifying designs that can have superior performance and reliability or designs that can offer better competition along several dimensions, which consumers may not have knowledge about). Thus, the designer’s preference in our DSS is used to ensure the quality of the product that may not be explicitly known to ordinary customers. This issue becomes more demanding when we plan to launch a product that has desired performance in long term both in the market and field. We have used a MAUT approach [19] to capture the designer’s preferences. As mentioned earlier, MAUT is an effective and powerful methodology for preference modeling especially where only a single respondent (i.e., the designer) is able to understand and respond to lottery technique questions. Although there are several forms of the utility function that can be used to model the designer’s preferences, for our DSS we have chosen a multiplicative form that is able to handle the interaction among the attributes. Also, with respect to each individual attribute a quadratic form of the utility function is used. The general form of a multiplicative utility function is shown in Eq. (9). The details of capturing the designer’s utility function (U) and the scaling constants k’s and K are beyond the scope of this paper.

$$
U(\mathbf{x}) = \sum_{i = 1}^{n}k_{i}u_{i}(x_{i}) + K\sum_{\substack{i = 1\\ j > i}}^{n}k_{i}k_{j}u_{i}(x_{i})u_{j}(x_{j}) + K^{2}\sum_{\substack{i = 1\\ j > i\\ l > j}}^{n}k_{i}k_{j}u_{i}(x_{i})u_{j}(x_{j}) + \dots +K^{n - 1}\prod_{i = 1}^{n}k_{i}u_{i}(x_{i})
$$

$$
u _ {i} (x _ {i}) = a _ {i} x _ {i} ^ {2} + b _ {i} x _ {i} + c _ {i}\tag{9}
$$

where K is the scaling constant calculated from Eq. (10).

$$
1 + K = \prod_ {i = 1} ^ {n} (1 + K k _ {i}).\tag{10}
$$

## 2.4. Customer based expected utility metric

Suh [27] introduced a metric known as a probability of success in product design that combined the uncertainty in each attribute level with a customer’s acceptable range. As shown in Fig. 3, Suh’s metric is defined as the area under the probability density function (PDF) that falls within a customer acceptable range for that attribute (i.e., the overlap between the design and customer ranges). In essence, Suh’s metric reflects the probability that the product attribute level will fall in the range that a customer deems desirable or acceptable.

![](/api/attachments/FUT3YCA2/fulltext/images/95510cec4efab6a9225fff7773bef01ec824ac26d9ee06d61977fbd4b5318b1b.jpg)  
Fig. 3. Probability of success [27].

Using the terminology introduced in this paper, Suh’s probability of success, $P _ { \mathrm { s } } ,$ can be reformulated as:

$$
P _ {\mathrm{s}} = \iint \dots \int D _ {p} (\mathbf {x}) p (\mathbf {x}) \mathrm{d} x _ {1} \mathrm{d} x _ {2} \dots \mathrm{d} x _ {n}\tag{11}
$$

where $D _ { p } ( \mathbf { x } )$ is the purchase decision function, and $p ( \mathbf { x } )$ is the joint probability distribution for design attributes. In formulating our metric, we extend Suh’s probability of success measure by taking into account not only the uncertainty in the design but also customer’s purchase decision and the designer’s preference. We define the Customer-based Expected Utility (CEU) metric by weighting Suh’s probability of success measure with the designer’s utility over the ranges of attributes that are of interest to the customer. As shown in Eq. (12), CEU is an estimate of the expected designer’s utility under the condition that the attribute level falls in the acceptable range of customer. If the designer and customer share the same acceptable range for the product attributes (i.e., complete overlap of the customer’s range and designer’s range), then the CEU metric turns into the designer’s expected utility, and the customer input does not play a role in the utility calculation for that particular design. On the other hand, if there is no overlap between the designer’s range and customer’s range for a design alternative, then it implies that the design is not likely to succeed in the market $( \mathrm { i . e . , }$ zero probability of success), yielding the lowest CEU, which is equal to zero. The reason for incorporating the designer’s preferences in the CEU metric is to ensure the consideration of quality and performance of the product that may not be explicitly known to ordinary customers. In addition, the appropriate product positioning in the market can also be considered using the designer’s preferences. In the case that several design alternatives are within the customer acceptable ranges and exhibit acceptable technical performance, the designer can choose to give a higher utility to the alternative that is different from the current competitive products in the market. There are many real world industrial situations in which the designer’s preference and his/her knowledge about the customer requirements play a key role in the success of the product development. The new design for Airbus A380 [22] is an example where the design project manager could decide on several technical challenges to satisfy conflicting customers’ requirements in the presence of competition.

Basically, the most influential part of the CEU is decided by the customers in terms of their acceptable range for each attribute. The successful product design candidates are the ones that can accommodate the widest customer range, and among those (if there is a tie), the one with the highest designer’s utility is selected by our DSS.

Next, the application of the CEU metric is discussed for different cases of single/multiple market segments.

## 2.4.1. Case 1: market characterized by a single segment

In this case there is only one segment characterizing the market whose purchase decision for a product is captured by function $D _ { \mathrm { { p } } } .$ . The uncertainty at a single attribute level is given by a probability distribution function p. Fig. 4 demonstrates these functions along with the designer’s utility U in the case of a single attribute x.

![](/api/attachments/FUT3YCA2/fulltext/images/f030fefb58949af7e4d2fafc02f1a4b20d48a26846ffa4660f6de96a26392d13.jpg)  
Fig. 4. The components of CEU for a single customer.

![](/api/attachments/FUT3YCA2/fulltext/images/724e337df77616cc07ea7dd14594e8b86d21da5f4f705b048c01c2d523ac0650.jpg)  
Fig. 5. The components of CEU for multiple segments (single attribute).

The CEU of a design alternative can then be defined as follows:

$$
\mathrm{CEU} (\mathbf {x}) = \iint \dots \int D _ {p} (\mathbf {x}) p (\mathbf {x}) U (\mathbf {x}) \mathrm{d} x _ {1} \mathrm{d} x _ {2} \dots \mathrm{d} x _ {n}\tag{12}
$$

where $D _ { \mathfrak { p } } ( \mathbf { x } )$ is purchase decision function, $p ( \mathbf { x } )$ is the joint probability distribution for design attributes, and $U ( \mathbf { x } )$ is the designer’s utility function. The CEU function reflects the expected value of the designer’s utility while accounting for the market information $( \mathrm { i . e . }$ , desired range and purchase decision of attributes). According to this metric, a design alternative with the set of attribute values that are not able to satisfy the market (i.e., not within the range of attributes as wanted by customers) will yield a zero CEU value. On the other hand, a design alternative for which the design and the market have the maximum common range and at the same time has its highest designer’s utility yields the highest CEU value. Such an alternative is the one, among all alternatives under consideration, which is most likely to satisfy the customers while also being preferred by the designer.

However, real-world product design selection usually involves a market with numerous customers whose purchase decisions might be different or even conflicting with one another. The next subsection focuses on multisegment market.

## 2.4.2. Case 2: multiple segments

To account for multiple-segment preferences, the normalized demand of a product is used instead of a purchase decision function in formulating the CEU metric. In Fig. 5, the normalized demand of a product, $q ( \mathbf { x } )$ , is shown as a function of the vector of attribute levels. As mentioned before, demand can easily be obtained by aggregating the purchase decisions $D _ { \mathfrak { p } }$ of each customer segment in the market.

![](/api/attachments/FUT3YCA2/fulltext/images/7dd692500d58df0a17812d46f48a3f1cef2b773dbc843de60702f7308f39becf.jpg)  
Fig. 6. The components of CEU for multiple segments (two attributes).

Therefore, the CEU of a design alternative can be obtained by replacing the individual’s $D _ { \mathrm { p } }$ in Eq. (12) with an estimated normalized demand q(x) obtained from Eq. (8).

$$
\operatorname{CEU} (\mathbf {x}) = \iint \dots \int q (\mathbf {x}) p (\mathbf {x}) U (\mathbf {x}) d x _ {1} d x _ {2} \dots d x _ {n}.\tag{13}
$$

Fig. 6 shows an example of the most general case for product design selection.

The next section describes the general selection (DSS) framework based upon the proposed CEU metric.

## 3. DSS for design selection

The DSS for the design selection process is shown in Fig. 7. It is assumed that the design input parameters are subject to a random variation (or noise) due to environmental and/or other conditions. The design simulation model receives the values of design parameters as input and returns the values of attribute levels as output. A Monte Carlo simulation is employed to sample uncertainties in the design parameters and compute the PDF of attribute levels (i.e., p(x)). Next, the designer’s utility and also the generalized purchase decisions for each market segment are obtained. The normalized demand of a design alternative is then estimated by aggregating the purchase decisions. Finally the CEU metric is calculated for a given design alternative. This procedure has to be performed over all design alternatives under consideration, and the output of the DSS is the alternative with the highest CEU value that meets both designer’s preferences and market demand the best.

## 3.1. Case example

The proposed DSS is applied to the design and selection of a power electronic device with three performance attributes. The attributes are: manufacturing cost $( x _ { \mathrm { { c } } } ) _ { : }$ , junction temperature $( x _ { \mathrm { T } } )$ , and thermal cycles to failure $( x _ { \mathrm { F } } )$ . As a demonstration of our approach, we only consider 10 design alternatives (that have tradeoffs with respect to one another) for their rank ordering.

![](/api/attachments/FUT3YCA2/fulltext/images/85bef93bb7883d513468070dd123d39ba3fe29d1527626836f7c315b2537bd00.jpg)  
Fig. 7. DSS for design selection.

![](/api/attachments/FUT3YCA2/fulltext/images/becb0cb693e6b18cbd9cabccf0b4c6c29f59f3d4970db50f35a559ee214bce83.jpg)  
Fig. 8. DSS user interface—main window.

Three design disciplines are involved to simulate the performance of each design alternative given the input design parameters (e.g., the geometry of power chips on the module, coolant flow rate, ambient temperature, market prices). A screenshot of the DSS user interface is shown in Fig. 8. Most of the engineering design simulators do not provide a closed functional form for the output responses as a function of inputs (e.g., finite element models, computational fluid dynamics simulators). An evolutionary algorithm, Multi-Objective Genetic Algorithm (MOGA), is used in our case study to help with searching the design space. (Details of MOGA is beyond the scope of this paper, however, for a review of MOGAs and other evolutionary algorithms refer to [13].) The solution from a multi-objective optimization problem as stated in this example is a set of design alternatives (called a Pareto set). The goal is to use our DSS for selection of the most promising design alternative from this set of Pareto alternatives.

Based on historical market data and design laboratory experiments, an appropriate distribution is fit to the data collected for input design parameters. Fig. 9 shows the design alternative generation process. Using the distribution obtained for input design parameters, a Monte Carlo simulation is performed. With the Monte Carlo simulation, the design alternative generator (i.e., multi-objective genetic algorithm optimizer) is used for all sampled input parameters to obtain distributions of the output performance attribute levels. It is determined that the normal distribution is the best fit for all three attributes. For simplicity, it is also assumed that the probability distributions of the attributes are statistically uncorrelated. The nominal values of attribute levels for these alternatives are shown in Table 1. The standard deviation for junction temperature is estimated as $3 . 5 ~ ^ { \circ } \mathrm { C } ,$ , for cycles to failure 100 cycles, and for cost \$1.67. It is assumed that there is a fixed profit margin of \$100 on each product (and it is the same for each design alternative.) To enter design attributes information, the user needs to click on Design Attribute Definitions and enter the appropriate values for each attribute as shown in Fig. 10. There are mainly three segments in the market for this power electronic device, namely, power vehicles, naval ships, power adaptors.

![](/api/attachments/FUT3YCA2/fulltext/images/db05644a9092da1c9fbb410d4bfeb337791bd941c563aed5fa026c76746f1124.jpg)  
Fig. 9. Design alternative generation process (the distributions shown here are only schematic.).

Table 1 Description of design alternatives

<table><tr><td>Design #</td><td>Junction temperature (°C)</td><td>Cycles to failure</td><td>Manufacturing cost (US$)</td></tr><tr><td>1</td><td>126</td><td>22,000</td><td>85</td></tr><tr><td>2</td><td>105</td><td>38,000</td><td>99</td></tr><tr><td>3</td><td>138</td><td>14,000</td><td>65</td></tr><tr><td>4</td><td>140</td><td>13,000</td><td>60</td></tr><tr><td>5</td><td>147</td><td>10,600</td><td>52</td></tr><tr><td>6</td><td>116</td><td>27,000</td><td>88</td></tr><tr><td>7</td><td>112</td><td>32,000</td><td>92</td></tr><tr><td>8</td><td>132</td><td>17,000</td><td>75</td></tr><tr><td>9</td><td>122</td><td>23,500</td><td>85</td></tr><tr><td>10</td><td>135</td><td>15,000</td><td>62</td></tr></table>

Next, the utility of the designer over each attribute of the product is captured. In this example, we use a linearly additive utility function with utility-independent attributes. The designer is assumed to show a slight risk taking behavior towards the cost of the product, but his preference behavior towards the failure and also temperature of the product is assumed to be risk averse. On the other hand the designer considers that the cost of the product is more important than the cycles to failure which is more important than the junction temperature. Using the methodology introduced by Keeney and Raiffa [19], the scaling constants of the utility function are estimated as (although it is integrated in the DSS, the details of computing the utilities are beyond the scope of this paper; see [19].): $k _ { \mathrm { c } } { = } 0 . 6 0 , ~ k _ { \mathrm { F } } { = } 0 . 2 5$ $k _ { \mathrm { T } } { = } 0 . 1 5$ and obtain

$$
u _ {\mathrm{c}} (x _ {\mathrm{c}}) = 2 \times 1 0 ^ {- 4} x _ {\mathrm{c}} ^ {2} - 0. 0 5 x _ {\mathrm{c}} + 2. 8 8
$$

$$
u _ {\mathrm{T}} (x _ {\mathrm{T}}) = - 2 \times 1 0 ^ {- 4} x _ {\mathrm{T}} ^ {2} + 0. 0 3 x _ {\mathrm{T}} + 0. 0 0 2
$$

$$
u _ {\mathrm{F}} (x _ {\mathrm{F}}) = - 9 \times 1 0 ^ {- 1 0} x _ {\mathrm{F}} ^ {2} + 7. 6 \times 1 0 ^ {- 5} x _ {\mathrm{F}} - 0. 6 1
$$

$$
U (\mathbf {x}) = k _ {\mathrm{c}} u _ {\mathrm{c}} (x _ {\mathrm{c}}) + k _ {\mathrm{T}} u _ {\mathrm{T}} (x _ {\mathrm{T}}) + k _ {\mathrm{F}} u _ {\mathrm{F}} (x _ {\mathrm{F}})\tag{14}
$$

where $x _ { \mathrm { c } } , \ x _ { \mathrm { T } } ,$ and $x _ { \mathrm { F } }$ are the manufacturing cost, junction temperature and cycles to failure respectively. $k _ { \mathrm { c } } , k _ { \mathrm { T } } ,$ and $k _ { \mathrm { F } }$ are their scaling constants, $u _ { \mathrm { c } } , u _ { \mathrm { T } } ,$ and $u _ { \mathrm { F } }$ are the single attribute utilities, and U is the multiattribute utility for design alternative x.

![](/api/attachments/FUT3YCA2/fulltext/images/635963d5657be4a5bab8a2bc1aa8e32a5fd7878f71ae5737d4890880702bf5e9.jpg)  
Fig. 10. Design definitions.

![](/api/attachments/FUT3YCA2/fulltext/images/e8edd50bd3288a393356ef30e5ea8f280c2176455daf1733f46c7fdf208d5068.jpg)  
Fig. 11. Designer’s utility definition with respect to design attributes.

User can enter the designer’s utility function by clicking on the Designer’s Utility Definition button on the main DSS window as depicted in Fig. 11. As we mentioned in Section 2.3, the individual elements of the multiplicative utility function (i.e., utility function with respect to each individual attribute) are assumed to be of quadratic form. However, one may argue that the quadratic form of individual utilities or the multiplicative model may not be able to address the designer’s preferences for all occasions. In that case, our DSS can take a custom utility function simulator. The custom utility simulator is an executable program that takes the attribute levels for each product from the main DSS software and writes the corresponding overall designer utility into a text file (named utility.txt). The schematic framework of this connection between the DSS and utility simulator is shown in Fig. 12.

To demonstrate the application of CEU metric, several scenarios with no customer information and with different customer’s purchase decisions are illustrated in the scenarios below.

Scenario 1—no market information: In this scenario, only the designer’s preferences are accounted for (i.e., via a utility function) while the customer’s purchase decision is ignored as appropriate information is not available. The vNM expected utility (EU) of the designer can be calculated for each design attribute and then aggregated as shown below:

$$
\mathrm {EU_ {c}} = \int \frac {1}{\sqrt {2 \pi} \sigma_ {\mathrm{c}}} u _ {\mathrm{c}} (x _ {\mathrm{c}}) \mathrm{e} ^ {\frac {- (x _ {\mathrm{c}} - \mu_ {\mathrm{c}}) ^ {2}}{2 \sigma_ {\mathrm{c}} ^ {2}}} \mathrm{d} x _ {\mathrm{c}}
$$

$$
\mathrm{E} \mathrm{U} _ {\mathrm{T}} = \int \frac {1}{\sqrt {2 \pi} \sigma_ {\mathrm{T}}} u _ {\mathrm{t}} (x _ {\mathrm{T}}) \mathrm{e} ^ {\frac {- (x _ {\mathrm{T}} - \mu_ {\mathrm{T}}) ^ {2}}{2 \sigma_ {\mathrm{T}} ^ {2}}} \mathrm{d} x _ {\mathrm{T}}
$$

$$
\mathrm{EU} _ {\mathrm{F}} = \int \frac {1}{\sqrt {2 \pi} \sigma_ {\mathrm{F}}} u _ {\mathrm{F}} (x _ {\mathrm{F}}) \mathrm{e} ^ {\frac {- (x _ {\mathrm{F}} - \mu_ {\mathrm{F}}) ^ {2}}{2 \sigma_ {\mathrm{F}} ^ {2}}} \mathrm{d} x _ {\mathrm{F}}
$$

$$
\mathrm{EU} = k _ {\mathrm{c}} \mathrm{EU} _ {\mathrm{c}} + k _ {\mathrm{T}} \mathrm{EU} _ {\mathrm{T}} + k _ {\mathrm{F}} \mathrm{EU} _ {\mathrm{F}}\tag{15}
$$

where $\mu _ { \mathrm { c } } , \ \sigma _ { \mathrm { c } }$ and $\mu _ { \mathrm { T } } , ~ \sigma _ { \mathrm { T } }$ and $\mu _ { \mathrm { F } } , ~ \sigma _ { \mathrm { F } }$ stand for the means and standard deviations of cost, junction temperature and cycles to failure, respectively, and $u _ { \mathrm { c } } ( x _ { \mathrm { c } } ) , u _ { \mathrm { T } } ( x _ { \mathrm { T } } )$ and $u _ { \mathrm { F } } ( x _ { \mathrm { F } } )$ and scaling constants $k _ { \mathrm { c } } , k _ { \mathrm { T } }$ and $k _ { \mathrm { F } }$ are given in Eq. (14). (It is assumed that the designer’s utility is zero outside the design range.) The Expected Multi-Attribute Utility (EU) of each design alternative is then calculated from the above equations, as listed in Table 2.

The EU ranking of Table 2 can be interpreted as follows: (i) cost is more important to the designer than cycles to failure than junction temperature, and (ii) design alternatives with lower costs are of more interest to the designer. Therefore, the design alternative 5 has the highest EU.

Scenario 2—single segment: In this case, the market information is also accounted for in the selection process. Suppose that a segment of the market seeks a device with the following specifications:

<sup>!</sup> The device has to endure at least 25,000 cycles, or its junction temperature must remain less than $1 3 0 ~ ^ { \circ } \mathrm { C }$

![](/api/attachments/FUT3YCA2/fulltext/images/a67f3be2e8326b3cb77fd028b12f4195f75f6cf9e6483b854c4819bca1efe813.jpg)  
Fig. 12. Interaction between the DSS and the custom utility simulator.

Table 2 Designer’s expected utilities

<table><tr><td>Alternative</td><td> $EU_c$ </td><td> $EU_T$ </td><td> $EU_F$ </td><td>EU</td></tr><tr><td>1</td><td>0.25</td><td>0.61</td><td>0.64</td><td>0.40</td></tr><tr><td>2</td><td>0.09</td><td>0.95</td><td>0.99</td><td>0.45</td></tr><tr><td>3</td><td>0.61</td><td>0.33</td><td>0.29</td><td>0.49</td></tr><tr><td>4</td><td>0.73</td><td>0.28</td><td>0.23</td><td>0.54</td></tr><tr><td>5</td><td>0.93</td><td>0.09</td><td>0.10</td><td>0.60</td></tr><tr><td>6</td><td>0.21</td><td>0.79</td><td>0.81</td><td>0.45</td></tr><tr><td>7</td><td>0.16</td><td>0.85</td><td>0.93</td><td>0.46</td></tr><tr><td>8</td><td>0.41</td><td>0.48</td><td>0.43</td><td>0.43</td></tr><tr><td>9</td><td>0.25</td><td>0.69</td><td>0.69</td><td>0.43</td></tr><tr><td>10</td><td>0.68</td><td>0.41</td><td>0.34</td><td>0.55</td></tr></table>

<sup>!</sup> The customer is willing to purchase the device if the price is less than \$170 (i.e., manufacturing cost less than \$70), and it lasts at least 20,000 cycles.

This translates into the following purchase decision function (a disjunctive normal form):

$$
D _ {p} (\mathbf {x}) = \left\{ \begin{array}{l l} 1 & [ (x _ {\mathrm{F}} \geq 2 5, 0 0 0) \vee (x _ {\mathrm{T}} \leq 1 3 0) ] \vee [ (x _ {\mathrm{c}} \leq 7 0) \wedge (x _ {\mathrm{F}} \geq 2 0, 0 0 0) ] \\ 0 & \text { Otherwise } \end{array} \right.\tag{16}
$$

We define: $A \equiv \{ \mathbf { x } | x _ { \mathrm { F } } { \boldsymbol { \Sigma } } 2 5 , 0 0 0 \} ; B \equiv \{ \mathbf { x } | x _ { \mathrm { T } } { \boldsymbol { \leq } } 1 3 0 \}$ ; $C { \equiv } \{ \mathbf { x } | x _ { \mathrm { c } } { \le } 7 0 \}$ ; and $D \equiv \{ { \bf x } | x _ { \mathrm { F } } { \geq } 2 0 , 0 0 0 \}$ . The set corresponding to purchase decision of 1 can be written as: S=A[B[(C\D).

The binary decision diagram of the above-mentioned customer’s purchase decision function is depicted in Fig. 13.

![](/api/attachments/FUT3YCA2/fulltext/images/d790f9b942ed04720be0283281d6ea787f7fcef39294791f0d3758cf85f2a0ee.jpg)  
Fig. 13. Binary decision diagram for the customer’s purchase decision function.

We need to keep in mind that the above-mentioned sets are not mutually exclusive. In other words, it is necessary to account for the overlaps between the sets and subtract the intersections. For instance:

$$
\begin{array}{l} \int D _ {p} (\mathbf {x}) U (\mathbf {x}) p (\mathbf {x}) \mathrm{d} \mathbf {x} = \int_ {A} U (\mathbf {x}) p (\mathbf {x}) \mathrm{d} \mathbf {x} \\ + \int_ {B} U (\mathbf {x}) p (\mathbf {x}) \mathrm{d} \mathbf {x} + \int_ {C \cap D} U (\mathbf {x}) p (\mathbf {x}) \mathrm{d} \mathbf {x} \\ - \int_ {A \cap B} U (\mathbf {x}) p (\mathbf {x}) \mathrm{d} \mathbf {x} - \int_ {A \cap C \cap D} U (\mathbf {x}) p (\mathbf {x}) \mathrm{d} \mathbf {x} \\ - \int_ {B \cap C \cap D} U (\mathbf {x}) p (\mathbf {x}) \mathrm{d} \mathbf {x} + \int_ {A \cap B \cap C \cap D} U (\mathbf {x}) p (\mathbf {x}) \mathrm{d} \mathbf {x}. \end{array}\tag{17}
$$

Now, the CEU of each design alternative can be calculated using Eq. (12) and (16) for the two attributes:

$$
\mathrm{CEU} (\mathbf {x}) = \iiint D _ {p} (\mathbf {x}) U (\mathbf {x}) p (\mathbf {x}) \mathrm{d} x _ {\mathrm{c}} \mathrm{d} x _ {\mathrm{T}} \mathrm{d} x _ {\mathrm{F}}\tag{18}
$$

The results are tabulated in Table 3.

According to Table 3, the design alternatives that are less satisfactory to the market (i.e., outside the customer range) are ranked lower. Alternatives 4 and 5 are completely outside the customer range, yielding a zero CEU value. Alternatives 3, 8 and 10 have nominal attribute levels outside but close to the boundary of ranges defined by the customer. In other words, they are likely to fall inside the customer ranges yielding negligible CEU. In contrast, alternatives 1, 2, 6, 7, and 9 are in the customer range with respect to all attributes. Among them, alternatives 6,7, and 9 have a wider acceptable customer range of attribute levels, and therefore have higher CEU values. Nevertheless, the designer’s utility value of alternative 7 is higher than that of 6 and 9, and thus, alternative 7 is ranked the highest in the set.

Table 3  
CEU of design alternatives

<table><tr><td>Alternative</td><td>CEU</td></tr><tr><td>1</td><td>0.24</td></tr><tr><td>2</td><td>0.22</td></tr><tr><td>3</td><td>0.05</td></tr><tr><td>4</td><td>0.00</td></tr><tr><td>5</td><td>0.00</td></tr><tr><td>6</td><td>0.33</td></tr><tr><td>7</td><td>0.34</td></tr><tr><td>8</td><td>0.10</td></tr><tr><td>9</td><td>0.31</td></tr><tr><td>10</td><td>0.04</td></tr></table>

![](/api/attachments/FUT3YCA2/fulltext/images/16c1feb8e44eb03c3d452aa25a67fb7285380b8ad2da3b0700aa6665d354dc35.jpg)  
Fig. 14. Market segments preference information.

Now, we can quantitatively compare the vNM expected utility metric (EU) with our metric (CEU) by evaluating the results in scenario 1 and scenario 2. In scenario 1 since the low cost is preferred by designer, alternative 5 with a big cost difference (than other alternatives) will be the output of the vNM expected utility method. However, in presence of the given customer requirements, design alternative 5 fails to satisfy the customer technical needs in terms of cycles to failure and is eliminated. Conversely, design alternative 7, which is the second most expensive alternative, has the highest CEU value because its attribute levels fall in the middle of the customer ranges, and also yields a high designer’s utility.

Scenario 3—multiple segments: Assume in this case, there are four customer segments involved. The purchase decisions are defined as following:

<sup>!</sup> Segment 1: The device needs to tolerate at least 20,000 cycles. Its junction temperature should not exceed $1 3 0 ~ ^ { \circ } \mathrm { C } .$ The available budget for this purchase is no more than \$185 per product item.

<sup>!</sup> Segment 2: The desired device needs to have one of the following criteria: endurable more than

35,000 cycles, junction temperature less than 110 8C, the price less than \$160.

<sup>!</sup> Segment 3: The budget does not exceed \$185 per product item and the eligible device needs to satisfy either one of the following criteria: lasting more than 2000 cycles, junction temperature less than 130 8C.

<sup>!</sup> Segment 4: The desired device should tolerate at least 3000 cycles and its junction temperature should not exceed $1 1 0 ~ ^ { \circ } \mathrm { C }$

The user can enter the market segment preference information by clicking on Market Segment Data button on main DSS window as shown in Fig. 14.

The CEU of each design alternative can be calculated as follows:

$$
\mathrm{CEU} (\mathbf {x}) = \iiint q (\mathbf {x}) U (\mathbf {x}) p (\mathbf {x}) \mathrm{d} x _ {\mathrm{c}} \mathrm{d} x _ {\mathrm{T}} \mathrm{d} x _ {\mathrm{F}}\tag{19}
$$

and the results of the DSS program are shown in Fig. 15.

A closer look at the results shown in Fig. 15 reveals that those alternatives that are within the market acceptable ranges and at the same time yield the highest designer’s utility are ranked higher by this metric. Alternatives 3, 6, 7, 8, and 10 are outside all customers’ ranges yielding zero CEU. Moreover, alternatives 4 and 5 are acceptable for only one customer resulting in relatively low CEU. The remaining alternatives are acceptable to two customers, and among them alternative 2 gets the highest CEU because of its higher designer’s utility value.

![](/api/attachments/FUT3YCA2/fulltext/images/a519ff689824db42185248c1d64a04a30bed0ad883c063b9bc67b7b6a3c402ad.jpg)  
Fig. 15. Final results.

## 4. Concluding remarks

The customer-based expected utility metric presented in this paper accounts for uncertainties associated with design attribute levels as well as the success of the product in the market and its desirability to the designer. As demonstrated in the examples, the approach guides the designer to determine which of the alternatives could possibly satisfy more customers and thus gain a higher potential demand. The generalized definition of the purchase decision function can model the customers’ choice patterns more suitably than a pure conjunctive choice model. Such generalized model allows for the interaction among attributes from customers’ point of view. It is shown that those alternatives that fall outside the customer range have a lower chance of success (i.e., lower CEU value) than those within the range. Although the proposed approach is unique in the sense that it accounts for both customers’ and designer’s preferences as well as manufacturing uncertainties, it has some limitations. The designer and the customers share the same attributes. This may be a valid assumption for many cases; however, one could face a situation where the designer deals with technical attributes that are not of any interest to a customer (or are beyond customer’s knowledge). One way to handle such situations is to consider no customer preference for those technical attributes, and proceed with Eq. (11) without any bounds for those specific attributes. As we mentioned, the CEU metric maps three important factors: product demand, uncertainties, and the designer’s preferences, into a single scalar for design selection. However, one may argue that there are several other important factors that affect the product development and are not considered in the CEU metric. While the engineering design related factors such as performance and quality of the product can be modeled as product attributes, some of the market related issues such as pricing strategies and advertising may not be directly addressed by our metric.

Also, our purchase decision modeling is based on the buy/no buy decision of each customer. In other words, the approach does not address whether or not the customers decide to buy which competitive product (i.e., market share estimate). However, we argue that the designer should have good knowledge of the market including the competitive products. In general, the designer looks for attributes or dimensions along which they can do better with respect to competitive products—this can be captured by giving higher weights to the designer’s preferences for attributes that make the new product different and better than the competition. In the validation stage, a choice based conjoint study could then be conducted to directly evaluate the impact of competitive products. Finally, the presented approach is only for introducing a single product in the market and the issues of product families and cannibalization effects are among the next steps of our future research.

Overall our approach (or a variation of it) will have value in both academic and industrial settings. In industrial design development teams, where there are multiple disciplines involved in the product design, there are always tradeoffs among several design alternatives with respect to each discipline. Similarly, in academic problems, when we deal with a multi-objective optimization case study, there are many design alternatives that are equally optimum and feasible with respect to the design objectives and constraints. In both situations, selecting a product design (or a family of products) from this set is not a trivial task. A decision support tool such as the one that we have developed for this research can help the managers and practitioners make such decisions.

## Acknowledgments

The work presented here is supported in part by the ONR Contract N000149810842, and in part by the NSF Grant DMI-0200029. Such support does not constitute an endorsement by the funding agency of the opinions expressed in the paper.

## References

[1] G. Alexouda, A user-friendly marketing decision support system for product line design using evolutionary algorithms, Decision Support Systems 35 (4) (2005).

[2] P.V. Balakrishnan, V.S. Jacob, Triangulation in decision support systems: algorithms for product design, Decision Support Systems 14 (4) (1995 Aug.).

[3] P.V. Balakrishnan, V.S. Jacob, Genetic algorithms for product design, Management Science 42 (8) (1996 Aug.).

[4] T. Bedford, R. Cooke, A new generic model for applying MAUT, European Journal of Operational Research 118 (3) (1999 Nov.).

[5] M. Ben Akiva, S.R. Lerman, Discrete Choice Analysis, MIT Press, Massachusetts, 1985.

[6] B. Besharati, S. Azarm, A. Farhangmehr, A customer-based expected utility metric for product design selection, CD-ROM proceedings of the ASME IDETC (Montreal, Canada, Sept.), 2002.

[7] D. Brownstone, K. Train, Forecasting new product penetration with flexible substitution pattern, Journal of Econometrics 89 (1–2) (1998 Nov.).

[8] R.E. Bryant, Symbolic Boolean manipulation with ordered binary-decision diagrams, ACM Computing Surveys 24 (3) (1992 Sep.).

[9] J. Butler, D.J. Morrice, P.W. Mullarkey, A multiple attribute utility theory approach to ranking and selection, Management Science 47 (6) (2001 Jun.).

[10] H.R. Choi, H.S. Kim, B.J. Park, Y.J. Park, A.B. Whinston, An agent for selecting optimal order set in EC marketplace, Decision Support Systems 36 (4) (2004 (Mar.)).

[11] R. Clemen, Making Hard Decisions: An Introduction to Decision Analysis, Duxbury Press, California, 1996.

[12] C.F. Daganzo, Multinomial Probit: The Theory and Application to Demand Forecasting, Academic Press, New York, 1979.

[13] K. Deb, Multi-objective Optimization Using Evolutionary Algorithms, John Wiley & Sons, Chichester, 2001.

[14] J. Eliashberg, G.L. Lilien, Handbooks in Operations Research and Management Science, Marketing, vol. 5, NorthHolland, Amsterdam, 1993, pp. 27– 82.

[15] E.H. Forman, S.I. Gass, The analytical hierarchy process—an exposition, Operations Research 49 (4) (2001 Jul.–Aug.).

[16] P.E. Green, V.R. Rao, Conjoint measurement for quantifying judgmental data, Journal of Marketing Research 8 (1971 Aug.).

[17] P.E. Green, V. Srinivasan, Conjoint analysis in consumer research: issues and outlook, Journal of Consumer Research 5 (2) (1978 Sep.).

[18] J.R. Hauser, G.L. Urban, Assessment of attribute importance and consumer utility functions: von Neumann–Morgenstern theory applied to consumer behavior, Journal of Consumer Research 5 (4) (1979 Mar.).

[19] R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives, John Wiley and Sons, New York, 1976.

[20] J.J. Louviere, D.A. Hensher, J.D. Swait, Stated Choice Methods: Analysis and Applications, Cambridge University Press, New York, 2000.

[21] D. McFadden, Conditional logit analysis of qualitative choice behavior, in: P. Zarembka (Ed.), Frontiers in Econometrics, Academic Press, New York, 1973.

[22] D. Michaels, For airbus making huge jet requires new juggling acts, Wall Street Journal (2004 May 27).

[23] M. Parameswaran, J. Stallaert, A.B. Whinston, A marketbased allocation mechanism for the DiffServ framework, Decision Support Systems 31 (3) (2001 Aug.).

[24] T.S. Raghu, P.K. Kannan, H.R. Rao, A.B. Whinston, Dynamic profiling of consumers for customized offerings over the internet: a model and analysis, Decision Support Systems 32 (2) (2001 Dec.).

[25] T.L. Saaty, The Analytical Hierarchy Process, McGraw-Hill, New York, 1980.

[26] S.M. Shugan and V. Balachandran, A Mathematical Programming Model for Optimal Product Line Structuring, Discussion paper No. 265, The Center for Mathematical Studies in Economics and Management Science, Northwestern University (1977).

[27] N.P. Suh, Axiomatic Design: Advances and Applications, Oxford University Press, New York, 2001.

[28] J. Von Neumann, O. Morgenstern, The Theory of Games and Economic Behavior, Princeton University Press, New Jersey, 1947

Babak Besharati is a Ph.D. candidate in Department of Mechanical Engineering at A.J. Clark School of Engineering. His research is mainly on Product Design Selection, Multidisciplinary Design Optimization, and Robust Design. He started his work on a new product development research project since 2002. Through this research, he has worked on a framework for the integration of design and marketing disciplines and particularly developed metrics for product design selection and design robustness. The support of Black & Decker Corporation, National Science Foundation and Office of Naval Research have provided a basis to publish his work and apply it to a number of real world product design problems.

Shapour Azarm is a Professor of Mechanical Engineering at the University of Maryland, College Park. He specializes in design optimization and design decision making. He is an Associate Editor of the ASME (American Society of Mechanical Engineers) Transactions, Journal of Mechanical Design; International Journal of Mechanics Based Design of Structures and Machines; and International Journal of Reliability and Safety. He was formerly the Conference and Paper Review Chair of the ASME Design Automation Conference and Chair of the ASME Design Automation Committee. Dr. Azarm is a Fellow of the ASME. He received his Ph.D. in 1984 from the University of Michigan, Ann Arbor.

P.K. Kannan is Harvey Sanders Associate Professor of Marketing at the Robert H. Smith School of Business at the University of Maryland. His current research stream focuses on new product/ service design and interface issues between marketing and manufacturing, centering on information products and product lines, and marketing and product development on the Internet. He has received grants from Mellon Foundation, SAIC, and PricewaterhouseCoopers for his work in this area and research papers have been published in

Management Science, Journal of Academy of Marketing Science, and Communications of the ACM. He received a grant from the National Science Foundation focusing on his work in new product develop ment with a focus on integrating marketing and engineering processes. Dr. Kannan is an Associate Editor for Decision Support Systems and serves on the editorial board of the Journal of Service Research, Journal of Business Research, Journal of the Academy of Marketing Science, and the International Journal of Electronic Commerce. He has corporate experience with Tata Engineering and Ingersoll-Rand and has consulted for companies such as Frito-Lay, Pepsi Co, Giant Food, Black & Decker, SAIC, Fannie Mae, and IBM.
