---
otero_id: 8056
otero_key: "B77QNWFD"
title: "Is this brand ephemeral? A multivariate tree-based decision analysis of new product sustainability"
authors: "Katsutoshi Yada; Edward Ip; Naoki Katoh"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.03.014"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Is this brand ephemeral? A multivariate tree-based decision analysis of new product sustainability

Katsutoshi Yada <sup>a</sup>, Edward Ip <sup>b,⁎</sup>, Naoki Katoh <sup>c</sup>

<sup>a</sup> Faculty of Commerce, Kansai University, Osaka, Japan <sup>b</sup> Department of Biostatistical Sciences, Wake Forest University School of Medicine, USA <sup>c</sup> Department of Architecture and Architectural Engineering, Kyoto University, Japan

Accepted 30 March 2007 Available online 19 April 2007

## Abstract

Decision tree methodology has become an increasingly important tool set in the field of decision science. We develop a multivariate, tree-based decision system for a new application: the determination of whether a newly launched consumer product should be allowed to continue in a highly competitive market. The system is designed to overcome a shortcoming–the inability to capture multivariate interactions–of traditional decision methods. We apply the proposed method to an instant noodle sales data set that contains 38 million transactions, and compare results across several methods © 2007 Elsevier B.V. All rights reserved.

Keywords: Sequential pattern analysis; New products; EBONSAI; Multivariate decision system; Instant noodle

## 1. Introduction

Globalization, technological innovation, advances in supply chain management, and perhaps most importantly the diversification of consumer needs have led to the proliferation of new brands of consumer goods and services. Every year in the U.S. market approximately 1000 new types of ice cream and other dairy products are launched [28]. In the consumer service industry, one of the leading credit card issuers, Capital One, issues over 1000 new types of credit cards every year to target specific segments of the consumer market [9]. The proliferation of new consumer goods and services is not only restricted to developed countries. In China, for example, for categories such as packaged food (e.g., bottled water) and popular electronics equipment (e.g., mobile phones and Discmans) a substantial number of new brands appear in the market every month—while an equally large number of brands vanish every month. Because of the relatively low overhead for manufacturers to produce goods that are slightly differentiated from existing products, it is common practice for manufacturers to launch multiple items under one brand name, multiple lines of brands, or multiple lines of products under the same or different brand names. Even though not considered entirely innovative, this approach is often used by companies as a defensive strategy in protecting an existing market or as a proactive approach in opening untapped market segments [24]. While some of the new launches will successfully meet the preferences and tastes of specific market segments and survive the initial launching phase, the reality is that others will fail and prove to be ephemeral. Indeed, for consumer packaged goods such as snacks and stationery, it is estimated that only one-quarter to one-third of new launches will survive more than two years [18].

The commoditization of consumer goods and the proliferation of new brands have increasingly shifted the focus of the decision concerning new product launches from the supply chain to the so-called “demand chain” [16]. In order to quickly adjust to changing consumer tastes and preferences, information about consumer reception of a new launch has to be gathered quickly, and a timely assessment of the product must be made before further resources are committed. Because shelf space in retail outlets is limited, new launches generally do not enjoy an extended period of time to prove themselves. Managers are pressured to make quick decisions as to whether a product should be allowed to remain in the market. In many cases, these decisions are based on limited performance data from the initial period of product launching. Prolonged decisions to discontinue unsuccessful products may unnecessarily lead to increased losses and to the wasting of resources that otherwise could have been used for launching new brands or promoting more promising existing brands. On the other hand, prematurely terminating potentially successful products can mean lost opportunities and profits.

In this paper, we propose a method that aims to help managers determine whether a newly launched product should be allowed to remain in the market given only early performance data from the initial phase of the launch. The proposed method is based on a data-driven, multivariate, decision-tree approach, and it is tailored to the action requirements of decision science applications. Organizations have now extensively used data-driven, learning-based systems to support their decision-making processes, and many have reported significant financial gains as a result of such improvements (e.g., [12]). To illustrate the proposed method, we apply it to transaction data from a popular consumer packaged good–the instant noodle cup–which are gathered from its largest market, the Japanese market. Conventional wisdom suggests that the decision to continue or terminate a new product can be based on aggregated sales volume or profit data gathered during the launching period. However, our experience with the packaged food industry in Japan was that such a method might fail. For example, our analysis indicated that in the instant noodle cup market a new launch typically can only achieve a small market share. When a new product has high trial volume (the first purchase) but low repeat volume (the second and future purchases), the product is more likely to fail than one that has smaller trial volume but high repeat rates. A decision that solely relies on early sales volume may identify a potentially weak product that has good initial volume (perhaps because of promotional cuts) as a success and a potentially strong product that does not have high initial volume as a failure.

## 2. Related literature

As far as we know, the literature on decision analysis for continuing or terminating new products in a mature market is sparse. The most recent example that we found is Lin and Cheng [19]. The authors described a fuzzy logic-based decision system that was used to support a go/no go business decision for launching a new product. There are, however, several related literatures—managing new, innovative products and brands; demand forecasting; and new product adoption. The first literature mainly concerns the development and introduction of innovative and often radically designed new products into a market, either traditional or new [5,7]. In particular, Mattsatsinis and Siskos [23] described agentbased intelligent marketing decision-support systems. Thus, their focus was on the marketing and penetration strategies and decisions for new, innovative products rather than on the point of decision after the initial launch of undifferentiated products in a mature market. On the other hand, demand forecast models tend to study demand under the framework of predictive models and models for repeat purchase [10] (for Japanese market application, see Nakanishi [26,27]). Some other recent examples include Cooper et. al. [6], in which a knowledge of a discovery system for tactical planning forecasting was proposed. Although companies do require accurate forecast models to predict sales during and after the launching phase, this specific information is not particularly helpful for predicting the fate of a new launch. Finally, new product adoption literature aims at predicting the trajectory of sales of new products and their diffusion after they are introduced in the market [2,17,21]. All three bodies of literature, while related to our current interest, are not immediately relevant to solving the problems we encountered.

There are several distinctive features about our approach. First, instead of requiring a forecast model for predicting sales volume for future periods, the approach provides an action-oriented decision tool to help managers arrive at and, perhaps to a lesser extent, justify a “go or no-go” decision. Second, it integrates information from several sources—the product, the customers, and market conditions. Furthermore, the tool allows distinct types of input. For example, it can simultaneously handle sequential pattern data such as sales volume as a function of time and other non-timevarying input. Accordingly, it generates a set of interpretable multivariate induction rules as output.

## 3. Background: managing new launches

In this section, we describe the specific example under which the decision problem arises, which is the instant noodle cup market in Japan. Although the example contains conditions that are rather specific to the instant noodle industry, the problem we illustrate is general in nature. Providers of other consumer products (e.g., snacks) and services (e.g., credit cards) face similar problems, although in different contexts (e.g., the launching and observation period may be longer).

The Japanese instant noodle market is the largest in the world and is approximately U.S. \$4 billion in size. Six major companies–among them Nissin Food, which first launched packaged instant noodles–control approximately 90% of the market [33]. Each manufacturer maintains several lines of products under different brand names. The instant noodles are usually differentiated by factors such as price (a unit sells for U.S. 70 cents to \$2.00 in Japan), flavor (traditional chicken and beef tastes to newer ones such as green tea and cheesecurry), type (e.g., ramen and udon), and package (e.g., cup, bowl, or pillow-like package). In this paper, we focus on instant cup noodles. While the number of new launches differs from year to year, our recent survey showed that there were over 300 new products of instant cup noodles introduced in the year 2002. There are several primary retail channels for instant cup noodles in Japan, including supermarkets, convenience stores, and local grocery stores. Shelf space differs across channels and generally is highly competitive. For example, the shelf space available in a supermarket for instant noodles allows the display of 40 to 50 products, while in convenience stores such as Seven-Eleven™ the competition is more intense, and only 20 to 30 products may be displayed. Fig. 1(a) and (b) show the shelf space of instant noodles in a Japanese supermarket in Osaka. Because of the competition for shelf space, brand managers often have to constantly review performance data and make decisions about which products are to be displayed in each market. More importantly, they are also required to make judicious decisions as to whether or not a newly launched product should be allowed to continue.

The traditional method for making this decision is often based on a combination of aggregated sales data and the experience of brand managers. For example, when early aggregated sales volume is not satisfactory, the brand will be terminated. However, this approach is dependent upon the experience of the individual manager. The decision is also complicated by the fact that for most newly launched products the initial sales volumes are generally small and contain high variance. A seemingly unpopular product in the first two weeks may suddenly gather momentum because it takes time for word of mouth to spread. On the other hand, a product may be seemingly popular in the first two weeks because of the initial promotional price cut–a factor that often confounds the performance of the product during the initial launching period–but fail to sustain its popularity when the price promotion is stopped. Furthermore, aggregated sales data do not take into account the characteristics of who is buying (or not buying) the product. For example, when a large proportion of the consumers are trial buyers and only buy because of the initial price promotion, the use of only aggregated data on sales volume could be misleading.

(a)  
![](/api/attachments/B77QNWFD/fulltext/images/77e5d070df7fa777273407ee5749f3c13a25c0ab04afd17f521a49b6e7690985.jpg)

(b)  
![](/api/attachments/B77QNWFD/fulltext/images/1f43b53178252981d4ee2e806f0477d59c510511dcb0cd975ba1608744f76832.jpg)  
Fig. 1. Shelf space for instant noodles in a typical Japanese supermarket (a) aisle, and (b) shelf.

It is also important to incorporate marketing variables into the decision. Some new items are merely extensions of an existing, strong brand line, and some are designed as flanker brands targeting a different group of consumers from the established brand. In all of these cases, the strength of the existing brand or the reputation of a manufacturer may play a role in increasing the likelihood of survival. Some other marketing variables are more complex. For example, in order to develop new flavors for instant cup noodles, manufacturers often scout famous local restaurants for recipes. Once they have found a marketable recipe, the manufacturer licenses the brand name of the selected restaurant and uses it as the brand name for their new product. Some marketers also use the names of local places as brand names (this is common practice in the bottled water industry). Besides a few brand names that have broad reach, most instant cup noodle brands appeal to local tastes and preferences and will likely survive if the products can sell well in a concentrated region. Such marketing variables, which could enhance the quality of decisions, are generally not made explicit in traditional analysis.

The problem we describe above presents a challenge and an opportunity for decision science researchers and practitioners. To satisfactorily solve the problem, efficient data learning systems that incorporate comprehensive information need to be developed. In this paper, we describe a multivariate, tree-based decision system that directly addresses the shortcomings of traditional methods, and we compare its performance to several commonly used algorithms.

## 4. The decision system

This section describes the decision support system and the data set. Comprising three components, the decision system analyzes historical data and reports interpretable results for supporting marketing decisions. The first component is a preprocessing machine, which extracts relevant input variables from raw transaction data collected from frequent-shopper programs (FSP) from various retail channels. The input variables are then relayed to the second component, the knowledgediscovery machine EBONSAI. Finally, the reporting component reports the set of induction rules. Fig. 2 depicts the decision system.

## 4.1. Data description

The raw transaction data sample collected from our FSP system contains 38 million transactions from 43,363 customers. The data set includes purchase history collected by a system of seven retail stores in a supermarket store chain from August 2000 to October 2001. At least three weeks of data were collected after the release of each product, and there were a total of 579 new products of instant noodles introduced during this period of time. Fig. 3 shows the distribution of the survival time for this sample of new launches. It can be seen that the new launches approximately cluster into several classes:

![](/api/attachments/B77QNWFD/fulltext/images/e7d726c18324681a5d18bac726cbf2fffa845590a507a5c328a6fd6c5de7a964.jpg)  
Fig. 2. System architecture for a decision system for newly launched products.

![](/api/attachments/B77QNWFD/fulltext/images/c873512b85b2d2afc309a1a73bd044aaf7a9e6623e9155853b29beefc5bc9ef8.jpg)  
Fig. 3. The distribution of survival time of new products. The horizontal axis indicates range of days. The vertical axis indicates counts of brands.

Class I These products quickly disappeared from the shelf within 30 days after launching.

Class II These products survived for 2 to 4 months and eventually vanished from the shelves.

Class III These products lingered on for 5 to 8 months. Class IV These products survived for more than 8 months.

A portion of products from Class I in fact consisted of test market cup noodles. Test market products were only launched to gather pilot data on how the market would respond to an experimental new product. By design, test market products were not intended to last, and so this class of products was excluded in the subsequent analysis. In order to focus our analysis on surviving and non-surviving brands, we collapsed Class II and III and defined the combined class as non-survivors, whereas Class IV was defined as survivors. The variable that indicated survival status was denoted by SURV. This variable will be used as our primary outcome variable in the subsequent analysis.

As a result of the above classification and the exclusion of test brands, the final sample (n = 447) contained 247 non-survivor and 200 survivor brands. We used ten-fold cross validation to evaluate the performance of EBONSAI and other methods. A tenfold cross validation first randomly partitioned the data set into 10 subsets of approximately equal size. Then a specific method (e.g., EBONSAI) was trained 10 times, each time leaving out one of the subsets from training. This “hold-out” subset is subsequently used to evaluate the performance of the method. The ten-fold cross validation approach to evaluation ensures an objective assessment of how the system may perform with a new and unseen data set.

To predict survival, three sources of information– customer information, product attributes, and marketing information–were used. Customer information was extracted from the FSP raw data by the preprocessing machine. It included the variables REPR and RHU-SER, which respectively represented the repeat purchase rate and the ratio of heavy instant cup noodle users. REPR was defined as the proportion of buyers who had purchased the product in the previous week and also bought in the current week. A heavy user was defined as someone who fell into the top 33% of the buyers by volume (number of units). Both variables are time-varying (i.e., these variables changed over time). Specifically, they were coded as a time sequence of alphabets, with each alphabet indicating the status at a specific time point. The second source of information, product attributes, included the variables MANUF and TASTE. They were categorical variables, respectively representing the manufacturer of the product and the flavor of the product, and both were non-time-varying. The third category of variables was related to sales and pricing: SALES was weekly sales volume of each product, which was a timevarying variable; REDPRICE was the largest discount ratio of sales price to regular price for the first three weeks after the release date (value is between 0 to1); and DISC was the time at which the product was first sold with a discounted price (value: 1st week, 2nd week, or 3rd week). Table 1 shows the list of important input variables to the decision system and their summary statistics. Except for the variables REPR and RHUSER, the correlations among the other variables were not significant. The correlation between REPR and RHUSER was approximately 0.48 (both measured at the 3rd week).

Descriptive statistics of important variables in the model. The week number is represented as (1), (2), and (3)

<table><tr><td>Variables</td><td>Average</td><td>Standard deviation</td><td>Data type</td></tr><tr><td>SALES(1)</td><td>3.01</td><td>1.41</td><td>Time-varying</td></tr><tr><td>SALES(2)</td><td>3.07</td><td>1.40</td><td>Time-varying</td></tr><tr><td>SALES(3)</td><td>3.05</td><td>1.41</td><td>Time-varying</td></tr><tr><td>REDPRICE</td><td>0.94</td><td>0.12</td><td>Non-time-varying 0-1</td></tr><tr><td>DISC</td><td>0.56</td><td>1.03</td><td>Non-time-varying (1,2,3)</td></tr><tr><td>REPR(2)</td><td>2.10</td><td>1.06</td><td>Time-varying</td></tr><tr><td>REPR(3)</td><td>1.86</td><td>1.16</td><td>Time-varying</td></tr><tr><td>RHUSER(1)</td><td>2.99</td><td>1.42</td><td>Time-varying</td></tr><tr><td>RHUSER(2)</td><td>2.66</td><td>1.62</td><td>Time-varying</td></tr><tr><td>RHUSER(3)</td><td>2.46</td><td>1.74</td><td>Time-varying</td></tr></table>

## 4.2. Knowledge discovery engine: EBONSAI

EBONSAI, or Extended-BONSAI is a tree-based, rule-induction engine that classifies pattern data in the form of character substrings. EBONSAI extends the work of BONSAI, which was first developed by Shimozono et al. [31]. The underlying concept of BONSAI originates from Arikawa et al. [1], in which the authors applied the idea to the identification of genome sequences. Effectively, EBONSAI is a multiattribute version of a commonly used induction method, ID3, of which later versions are known by other names such as C4.5 and C5.0 [29,30]. A rule-induction engine achieves automatic learning from a set of examples (called a training or learning set), for which the outcome is known. With sufficient examples, the system generates induction rules that mimic the decision outcome of the examples in the training set. Many tree-based, rule-induction methods, including ID3 and EBONSAI, create a tree from a series of binary splits on attributes. The collection of splits partitions the attribute space into a set of non-overlapping rectangles.

The unique feature of EBONSAI is its treatment of string variables (e.g., weekly observations of an outcome such as a high or low pattern of sales). Instead of treating a string as comprising individual variables in splitting, EBONSAI seeks “regular patterns” to optimize splits [13]. An example of a character substring is an observed sales pattern for a five-week period: (VH,H,M, L,L), in which we first see a very high level of sales (VH) in the first week, then a high level of sales (H) in the second week, then moderate sales (M) in the third week, and finally low sales (L) in the fourth and fifth weeks. Now, when a high proportion of failure cases contain the pattern (VH,H,M,L,L), a learning algorithm may want to include the string as a criterion for splitting the data—namely, partitioning the data into those that contain the pattern and those that do not. In general, EBONSAI treats patterns as strings of categories, and the collection of categories is called the alphabet set. For example, {VH,H,M,L} forms an alphabet set. Details of the learning algorithm will be provided in the following subsections.

EBONSAI has the following new features that were absent in BONSAI: (1) the ability to handle numeric and categorical data, (2) the use of character strings in splitting and forming decision trees, and (3) the ability to search for a given pattern at any position within a string (e.g., at the beginning or the end of a string pattern).

EBONSAI comprises two engines—the data transformation engine (DTE) and the inference engine (IE). DTE transforms data into the appropriate character strings suitable for input into IE, then IE applies a greedy algorithm to search over the space that contains combinations of character strings to identify the appropriate candidate for splitting the data space. We separately describe the two engines below.

## 4.2.1. Data transformation engine

DTE transforms pattern data into character strings. The term “pattern data” refers to time-varying input: SALES, REPR, and RHUSER. The variable SALES, for example, is a d-tuple (from $d$ weeks of sales data) and is required to be transformed into a string of characters in which each character represents a category of level of sales. The transformation takes place in two steps. First, each continuous variate is discretized into k levels, where k is predetermined. Second, the d-tuple of the continuous variates is mapped to a corresponding $d -$ tuple of the categorical variable. Note that the order of the d-tuple is important and that each d-tuple will be treated as multivariate data in the implementation of the inference engine. Fig. 4 illustrates the two-step transformation procedure of DTS.

We use the following method to determine the number of categories (k) in discretizing a continuous variable. First, we use two values of k = 3,5 for each time-varying input. As a result, there are altogether $2 ^ { d }$ possible ways to create a transformed data set, which we call the k-subsample. Second, we apply the learning algorithm to each of the $2 ^ { d }$ k-subsamples. As we shall see later, the result from EBONSAI is rather robust with regard to the choice of the value of k.

![](/api/attachments/B77QNWFD/fulltext/images/ac7cc92b97c757eb363f9ec84e5367fb7a09af1740a17ea23c910d7a5245dafc.jpg)  
Fig. 4. The two-step transformation procedure for input variables.

## 4.2.2. Inference engine

IE is designed to learn from the data (the training set) a set of induction rules (K), so that K can be used to classify new observations. EBONSAI is distinguished from other tree-based methods in its ability to process pattern strings. When the attributes are not strings, EBONSAI is functionally similar to ID3. However, when some of the variables contain strings, such as five-week sales volume (VH,H,M,L,L), EBONSAI performs differently from ID3 in that it will search for candidate regular patterns for an optimal split. Generally, the space of candidate regular patterns is quite large—e.g., besides VH,H,M,L,L there may be other candidate regular patterns such as H, VH, L, M, M that are eligible to compete for being the optimal split. EBONSAI applies a greedy algorithm to select the optimal split among a pool of possible combinations of patterns, and the algorithm then recursively searches for optimal splits in the subsequently partitioned data spaces. As with other tree-based algorithms, one can either terminate splitting when a predetermined criterion is reached or prune an overly grown tree by first allowing the splitting process to continue until the recursively partitioned data spaces become very small. However, unlike traditional classifying learning algorithms such as ID3 and CART [4], which recursively partition the data space by univariate splits, EBONSAI splits the data space by combinations of regular patterns of varying lengths.

Specifically, let $P$ and N, respectively, denote the set of positive and negative examples. In the current application, $P$ is the set of surviving brands, and N is the set of failed brands. A regular pattern π is defined as a string $\alpha _ { 0 } x _ { 1 } \alpha _ { 1 } x _ { 2 } . . . x _ { k } \alpha _ { k }$ where each $\alpha _ { i }$ is a constant substring and each $x _ { i }$ is a variable that matches any string. Thus, the pattern $\alpha _ { 0 } x _ { 1 } \alpha _ { 1 } x _ { 2 } . . . x _ { k } \alpha _ { k }$ represents a string that contains the specific substrings $\alpha _ { 0 } , \alpha _ { 1 } . . . \alpha _ { k } ,$ and in that order. Each $\alpha _ { i }$ is some substring in the set P ⋃ N. For any regular pattern of π generated from P and N the cost function E (π) is given by

$$
E (\pi) = \frac {p _ {1} + n _ {1}}{| P | + | N |} I (p _ {1}, n _ {1}) + \frac {p _ {0} + n _ {0}}{| P | + | N |} I (p _ {0}, n _ {0}),\tag{1}
$$

where $p _ { 1 } ( n _ { 1 } )$ denotes the number of positive examples in $P ( N )$ that match $\pi , p _ { 0 } ( n _ { 0 } )$ denotes the number of positive examples in $P ( N )$ that do not match $\pi ,$ and

$$
I (p, n) = - \frac {p}{p + n} \log \frac {p}{p + n} - \frac {n}{p + n} \log \frac {n}{p + n},\tag{2}
$$

and 0 if either $p$ or n is 0. The cost function is similar to the Gini or the entropy function, which are used in

CART and other tree-based methods. They basically measure how well a split performs in separating the examples into homogeneous groups. EBONSAI uses a greedy algorithm to search for a pattern π that minimizes the cost E(π) at a node.

Because the set of all possible regular patterns can get extremely large, EBONSAI employs an alphabet indexing procedure to simplify the search. Alphabet indexing is a mapping from an alphabet that contains a large number of symbols into another alphabet with fewer symbols. A good alphabet indexing can reduce the search space and still keep enough information for the classification of the positive and negative examples. The indexing procedure employs a leap-and-bound search algorithm that starts by randomly selecting two small subsets of positive and negative examples and an index that is randomly generated—e.g., VH, H, M, L,L can be given an index $( 1 , 0 , 0 , 0 , 0 )$ . Then the algorithm searches a new index (by randomly flipping the 1's and $0 ^ { \circ } \mathrm { s } )$ from its neighborhood in such a way that the new index has a score that is best within that neighborhood [14]. The score is defined in such a way as to reflect the average success rates of classifying the positive and negative examples.

With the flexibility in directly handling strings, EBONSAI can incorporate substrings of the form ˆα and $\alpha \$ 1$ , which respectively represent the initiation and the termination of the sequence α. This feature, which is not present in the original BONSAI, can be quite powerful. For example, a certain pattern appearing at the beginning of the launching period may have greater predictive power than the same pattern appearing at other positions.

Statistically speaking, EBONSAI uses multivariate split to preserve positional information and possible interaction between variables. This has an important advantage over systems that are based upon univariate split, which is implemented in machine learning algorithms such as C4.5 and CART. We provide a simple example to illustrate how character string-based systems can overcome a shortcoming in univariate systems. A similar example is used in Giuffrida et al. [11]. Table 2 shows a simple data set that contains the variable on sales volume of the first two weeks– SALES1 and SALES2–and the target variable SURV (0 = not survive, 1 = survive). An inspection of the data reveals that neither SALES1 nor SALES2 alone have strong predictive power. However, there is strong interaction between the two variables. A strong rule exists within the data: “If SALES1= L and SALES2=L, then $\mathrm { S U R V } { = } 0 . ^ { \mathfrak { P } }$ When EBONSAI was applied to the data set, it successfully recovered the strong rule. Fig. 5a shows the tree from EBONSAI induced by the data.

An example data set to illustrate the shortcoming of learning based on a univariate split

<table><tr><td>SALES1</td><td>SALES2</td><td>SURV</td></tr><tr><td>L</td><td>H</td><td>1</td></tr><tr><td>L</td><td>M</td><td>1</td></tr><tr><td>L</td><td>VH</td><td>1</td></tr><tr><td>VH</td><td>L</td><td>1</td></tr><tr><td>H</td><td>L</td><td>1</td></tr><tr><td>M</td><td>L</td><td>1</td></tr><tr><td>L</td><td>L</td><td>0</td></tr><tr><td>L</td><td>L</td><td>0</td></tr><tr><td>L</td><td>L</td><td>0</td></tr></table>

Algorithms that are based on a univariate split cannot exactly recover the strong rule—they may determine that no split can improve the performance of the tree or rely purely on univariate splits to recover the rule. Fig. 5b shows the tree obtained via ID3 [11]. Indeed, when the dimensionality of the multivariate problem increases, the interaction pattern between variables will become increasingly complex. Accordingly, the univariate approach will become even less powerful in detecting and summarizing potentially strong or interesting rules. EBONSAI is designed to overcome this difficulty.

## 5. Results and comparison with other methods

The decision tree that EBONSAI produced from the instant noodle training data set contained 10 terminal nodes. Fig. 6 shows the overall EBONSAI tree. Like other decision trees such as CART, the EBONSAI tree allows classification of new cases through a sequence of decisions. For example, at the first decision node, a brand is predicted not to survive if in the first three weeks it has not aggressively discounted the product (REDPRICE greater than 0.81).

We evaluated the performance of EBONSAI using several measures commonly employed in the literature: Recall, Precision, F-measure, and Matthews correlation coefficient [22,32]. Table 3 shows the cross-tabulation of the actual versus the predicted outcome for the variable SURV. The reported measures of accuracy are defined by the following set of equations:

Recall: $R = { \frac { \mathrm { T P } } { \mathrm { T P } + \mathrm { F N } } } ,$

Precision: $P = { \frac { \mathrm { T P } } { \mathrm { T P } + \mathrm { F P } } } ,$

$$
F \text {-measure:} F = \frac {2 \times R \times P}{R + P}, \text { and }
$$

Matthews correlation coefficient:

$$
C = \frac {\mathrm{TP} \times \mathrm{TN} - \mathrm{FP} \times \mathrm{FN}}{\sqrt {(\mathrm{TP} + \mathrm{TN}) (\mathrm{TN} + \mathrm{FP}) (\mathrm{TP} + \mathrm{FP}) (\mathrm{TN} + \mathrm{FN})}}.
$$

The estimated values for the measures R, P, F, and C for EBONSAI were respectively 0.62, 0.87, 0.72, and 0.26. For R, P, and $F ,$ higher value suggests better performance. For the Matthews correlation coefficient C, the interpretation is similar to the Pearson correlation, for which a value of 1 corresponds to a perfect correlation (prediction). The results of higher P and lower R partly reflect the choice of the cost matrix, which reflects the extent to which a marketer is willing to trade off the risk in misclassifying a true survivor as a non-survivor, and vice versa. After consulting with the marketing experts in the industry with regard to misclassifying a surviving brand as a non-survivor, we imposed a penalty 1.235 times as large as for misclassifying a non-surviving brand as a survivor. This skewed the decision tree toward tending to include more predicted survivors.

We also compared the predictive accuracy between EBONSAI and three other commonly used machine learning methods: C4.5, neural network, and logistic regression. Comparisons between neural network and decision tree methods have been reported in the decision science and machine learning literature [3,20]. As described above, we evaluated the accuracies of the

![](/api/attachments/B77QNWFD/fulltext/images/5b3cad9e650644c77a3487d4465468e6ae98494e90403fdb2f3b2c75a5dc5f11.jpg)  
Fig. 5. a. The tree obtained from EBONSAI applied on the data set in Table 2. b. Single node produced by ID3 applied to data set in Table 2.

<table><tr><td>Original character</td><td>1</td><td>2</td><td>3</td></tr><tr><td>Transformed character</td><td>1</td><td>2</td><td>2</td></tr></table>

<table><tr><td>Original character</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Transformed character</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td></tr></table>

![](/api/attachments/B77QNWFD/fulltext/images/710d184dcc23bff0e16b4f799112d9c07174486a2f1a61c08ba5839ab71a038b.jpg)  
Fig. 6. The l EBONSAI tree for classifying survival status of new instant noodle brands. A higher number implies a higher level of the quantitative variable.

four methods using ten-fold cross validation. For neural network, we used an architecture with one hidden layer with 20 nodes and the back-propagation algorithm for training.

Fig. 7(a)–(d) displays the recall, precision, Fmeasure, and Matthews correlation coefficient of EBONSAI and the other methods from ten-fold cross validation. Recall that we created different k-subsamples to evaluate the effect of discretizing the continuous variable sales volume into k levels (k = 3,5). The label for each set of bar charts represents how the value of k varies over the time span. From Fig. 7, EBONSAI appears to dominate the other methods on precision, Fmeasure, and Matthews correlation. For recall, EBON-SAI is comparable to the other methods and is superior to logistic regression. From inspecting the graphs, all methods seem rather robust in the way the continuous variable is discretized.

Table 3  
Classification of prediction outcomes. TP: True positives, TN: true negatives, FP: false positive, and FN: false negative

<table><tr><td></td><td>Predicted positive</td><td>Predicted negative</td></tr><tr><td>Actual positive</td><td>TP</td><td>FN</td></tr><tr><td>Actual negative</td><td>FP</td><td>TN</td></tr></table>

In order to see how the prediction accuracy of EBONSAI varies by changing its pruning parameter, we performed some experiments. Pruning parameters are used to indicate the complexity of a tree model. To find an optimal pruning parameter, one needs to solve the trade-off between pruning the tree too much (resulting in the introduction of bias) and pruning too little (resulting in excessive variance). Using C4.5 as a benchmark for comparison, we varied the pruning parameter of both trees. For both C4.5 and EBONSAI, we followed Quinlan [29] and used the upper confidence limit of error rate, which is defined as the proportion of misclassified cases at each node, as the pruning parameter. A lower value of the pruning parameter allows the model to keep nodes that do not perform too well and will result in a larger tree, and vice versa. Fig. 8 illustrates the change in the Matthew correlation coefficient (C) of EBONSAI and C4.5 with respect to the change of pruning parameters using ten-fold cross validation. From Fig. 8, it appears that both EBONSAI and C4.5 maintain a reasonably stable level of accuracy within a range of pruning parameters. The graphs for other measures look very similar to Fig. 8 and are not shown here.

(a)  
![](/api/attachments/B77QNWFD/fulltext/images/9f48708574f70a3f93795d696c745f70067d32341338a58500d390e73f343684.jpg)  
(b)

(c)  
![](/api/attachments/B77QNWFD/fulltext/images/e41f595c61ffacf91880f20d24d29450719db4fa1e8e889e810b075705dc9bd1.jpg)

![](/api/attachments/B77QNWFD/fulltext/images/0eab4320e9f56315585097f5d4bab0942a94314f649552ae776ec86597b6133c.jpg)

![](/api/attachments/B77QNWFD/fulltext/images/9c7f84269063a246ef5db79960a4877b8e157839b0a1d75431ba6b724746e411.jpg)  
(d)  
Fig. 8. Comparing EBONSAI and C4.5 with varying pruning parameter (upper confidence limit of error rate) for Matthews correlation coefficient.

![](/api/attachments/B77QNWFD/fulltext/images/cf86161dd9f60e1925b9c4cc3a8c9be0464c6c3d1bb9efd97bbcc7faee73be15.jpg)  
Fig. 7. Comparison of EBONSAI, C4.5, logistic regression, and neural network for predicting survivor and non-survivor brands on performance measures: (a) Recall, (b) Precision, (c) F-measure, and (d) Matthews correlation coefficient.

## 6. Discussion and conclusion

Companies that provide consumer goods and services are facing tremendous challenges. The marketplace is becoming increasingly commoditized, with fastchanging market conditions, as competitors continually enter and exit the market. Managers and marketers have to make decisions under time constraints and often without full information. To manage the risk that is associated with the uncertain outcomes, a disciplined approach to decision making, based on data and modern decision tools, can be more profitable than relying on ad hoc methods or experience alone.

In this paper, we showed how detailed data that are routinely collected from business transactions, coupled with innovative technology, can be combined to help managers arrive at decisions concerning the sustain ability of newly launched consumer products. An important feature of our approach is the use of string patterns for tree growing, which has demonstrated that it can lead to improvement over methods that are based on univariate splits. Like other tree-based methods, our approach provides managers with a set of interpretable induction rules. One way for managers to use EBONSAI is to directly apply the tree for future prediction and extrapolation: A new brand will be passed through the decision tree to derive a predicted outcome. A manager can then act upon the predicted outcome to discontinue (continue) the brand if the predicted outcome is negative (positive). Because not all terminal nodes in the decision tree are created equal, a manager can also rely on probability measures for failure/survival at each terminal node to assist in arriving at an actual decision. An alternative approach is to use the decision tree as a discussion tool for extracting marketing rules from the full tree. Using the tree from Fig. 6 as an example, the first two decision nodes suggest that for survival brands, during the first three weeks, their discount levels are neither too moderate (less than 19%) nor too aggressive (more than 52%). Some other rules derived from Fig. 6 are also rather intriguing and can provide other useful marketing insights. For example, (after the first two decision nodes on pricing) the tree shows that when sales volume goes down (pattern 221), but proportion of heavy users goes up (pattern 112), the brand is likely to survive. On the other hand, if pricing point can be held stable (price discount between 19 to 31%), and repeat users level is high (pattern 22), the brand is still likely to survive. The rules for repeat purchase rate in the decision tree generally suggests that there may be a strong need to sustain repeat purchase rate–not necessarily overall sales–at the third week after launching. From our field experience, some managers did use the tree-as-discussion-tool approach to create marketing plans and strategies. For example, based upon the extracted rule for repeat purchase rate, they concentrated sales promotion to target repeat buyers during the third week after launching. While our analyses are directed toward a specific industry–instant cup noodles–we believe that our methodology is rather general and can be easily adapted to other consumer product industries.

A limitation of the study reported in this paper is that we have neither included new product development process variables nor marketing strategy variables. Both of these may provide insight into why a new product will succeed. For example, how a company originates and manages the new product development process may create a strategic advantage in the product's long-term success [8]. Further, competitive forces in the market and their reactions will also shape the destiny of a new launch [15]. In a future study, we plan to design methods to measure these attributes and to incorporate them into the decision model.

## References

[1] S. Arikawa, S. Miyano, A. Shinohara, S. Kuhara, Y. Mukouchi, T. Shinohara, A machine discovery from amino acid sequences by decision trees over regular patterns, New Generation Computing 11 (1993).

[2] F.M. Bass, A new product growth for consumer durables, Management Science 15 (1969).

[3] S. Bhattacharyya, P.C. Pendharker, Inductive, evolutionary, and neural computing techniques for discrimination: a comparative study, Decision Science 29 (1998).

[4] L. Breiman, J.H. Friedman, R. Olshen, C. Stone, Classification and Regression Trees, Wadsworth and Brooks, Monterey, CA, 1984.

[5] M.A. Cohen, J. Eliashberg, T.H. Ho, New product development: the performance and time to market trade-off, Management Science 42 (2) (1996).

[6] L. Cooper, P. Baron, W. Levy, M. Swisher, P. Gogos, PromoCast: a new forecasting method for promotion planning, Marketing Science 18 (3) (1999).

[7] M. Crawford, A. Di Benedetto, New Products Management, 7th ed. Irwin/McGraw Hill, New York, 2003.

[8] J.E. Ettlie, M. Subramaniam, Changing strategies and tactics for new product development, Journal of Product Innovation Management 21 (2004).

[9] C. Fishman, This Is a Marketing Revolution, Fast Company, May 1999.

[10] L.A. Fourt, J.W. Woodlock, Early prediction of market success for new grocery products, Journal of Marketing 25 (2) (1960).

[11] G. Giuffrida, W. Chu, D.M. Hanssens, Mining classification rules from data sets with a large number of multi-value attributes, in: C. Zaniolo, P.C. Lockmann, M.H. Scholl, T. Grust (Eds.), Advances in Database Technology, Springer, Berlin, 2000.

[12] S. Goonatilake, Intelligent systems for finance and business: an overview, in: S. Goonatilake, P. Treleaven (Eds.), Intelligent

Systems for Finance and Business, John Wiley & Sons, New York, 1995.

[13] Y. Hamuro, H. Kawata, N. Katoh, K. Yada, A machine learning algorithm for analyzing string patterns helps to discover simple and interpretable business rules from purchase history, progress in discovery science, LNAI 2281 (2002).

[14] Y. Hamuro, N. Katoh, E.H. Ip, S. Cheung, K. Yada, Combining information fusion with string pattern analysis: a new method for predicting future purchase behavior, in: C. Torra (Ed.), Information Fusion in Data Mining, Springer-Verlag, Berlin, 2003.

[15] E.J. Hultlink, F. Langerak, Launch decision and competitive reactions: an exploratory market signaling study, Journal of Product Innovation Management 19 (2002).

[16] E.B. Kahn, L. McLister, Grocery Revolution: The New Focus on the Consumer, Addison Wesley, New York, 1997.

[17] S. Kalish, A new product adoption model with pricing, advert ising, and uncertainty, Management Science 31 (1985).

[18] P. Kotler, Marketing Management, Prentice Hall, New York, 2000.

[19] C.T. Lin, C.J. Cheng, A fuzzy logic-based approach for new product go/no-go decisions at the front end, IEEE Transactions on Systems, Man and cybernetics. Part A 34 (1) (2004).

[20] O.R. Liu Sheng, C.P. Wei, P.J. Hu, N. Chang, Automated learning of patient image retrieval knowledge: neural networks versus inductive decision trees, Decision Support Systems 20 (2000).

[21] V. Mahajan, E. Muller, Y. Wind, New Product Diffusion Model, Kluwer Academic Press, Boston, 2000.

[22] B. Matthews, Comparison of the predicted and observed secondary structure of T4 Phage Lysozyme, Biochimica et Biophysica Acta 405 (1975).

[23] N. Mattsatsinis, Y. Siskos, Intelligent Support Systems for Marketing Decisions, Springer, New York, 2002.

[24] P. Nakache, Marketing the unmarketable, Harvard Management Update (1997 (September)).

[26] M. Nakanishi, Advertising and promotion effects on consumer response to new products, Journal of Marketing Research 10 (1973).

[27] M. Nakanishi, Frontier in Consumer Behavior Analysis, Seibundo-Shinkosha, Japan, 1984.

[28] New Product News, Health Benefits Included (1999). http:/ www.preparedfoods.com/archives/1999/9904/9904northamer. htm#efforts.

[29] J.R. Quinlan, Induction of decision trees, Machine Learning (1986)

[30] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufman, Los Altos, CA, 1993.

[31] S. Shimozono, A. Shinohara, T. Shinohara, S. Miyano, S. Kuhara, S. Arikawa, Knowledge acquisition from amino acid sequences by machine learning system bonsai, Transactions of Information Processing Society of Japan 35 (1994).

[32] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques With JAVA Implementations, Morgan Kaufmann, San Francisco, 2000.

[33] Yano Research Institute, International Business Development Department, Market Share in Japan, Yano Research Institute Ltd, Tokyo, Japan, 2002.

## Further Reading

[25] H. Nakamura, Marketing of New Products, Chuokeizai-sha, Japan, 2001.

Katsutoshi Yada is Professor of Management Information Systems in the Faculty of Commerce, Kansai University, Osaka, Japan. He was previously an Assistant Professor in the Department of Business Administration, Osaka Industrial University, Osaka, Japan, from 1997 to 2000. He received his M.A. and Ph.D. in Business Administration from Kobe University of Commerce, Hyogo, Japan, in 1994 and 2002, respectively. His present research interests include data mining for marketing, and information strategy concerning data mining. He has been chairman and member of various program committee in many international data mining conferences. He is a member of IEEE, AMA and AMS.

Dr. Edward Ip is Associate Professor in the Department of Biostatistical Sciences at Wake Forest University School of Medicine. He also has a joint appointment in the Section of Social and Behavioral Sciences, Department of Social Sciences and Health Policy. His training is in statistics and psychometrics. Prior to his appointment at WFUSM, he was assistant professor in statistics at the Marshall School of Business, University of Southern California. He has also worked as associate research scientist at the Large-scale Assessment Group, Psychometric and Statistics Division, Educational Testing Service. He received his Master in Education with concentration in both Education Psychology, and Research and Evaluation Methodology (1990), and Ph.D. in Statistics (1995), all from Stanford University.

Dr. Ip's research interest is in psychometric methods and their applications to psychological, educational, business, and health-related measurements.

Prior to coming to WFUSM. He has published journal articles in Psychometrika, British Journal of Mathematical and Statistical Psychology, Journal of the American Statistical Association, Journal of Multivariate Analysis, and Sociological Methods in Research. Dr. Ip is the recipient of two current National Science Foundation awards for conducting statistical research in longitudinal analysis and item response analysis. Currently, he is Associate Editor the Journal of Educational and Behavioral Statistics, which is jointly published by the American Statistical Association (ASA) and the American Educational Research Association. He is a member of ASA and Psychometric Society.

Naoki Katoh is Professor in the Department of Architecture and Architectural Engineering, Kyoto University. He received a BS and MS in Applied Mathematics and Physics from Kyoto University in 1973 and in 1975 respectively. He received his Ph.D. in Applied Mathematics and Physics from Kyoto University in 1981. He was an Assistant Professor during 1981–1982, an Association Professor during 1982– 1990, and a Professor during 1990–1997, at Department of Management Science of Kobe University of Commerce. In 1997 he jointed Kyoto University. His papers have appeared in several journals, including SIAM Journal of Computing, SIAM J. Discrete Mathematics, JACM, Mathematics of Operations Research, Discrete Computational Geometry, J. of Algorithms, IEEE Transactions on Software Engineering, Discrete Applied Mathematics, Data Mining and Knowledge Discovery, Theoretical Computer Science, Computational Geometry: Theory and Applications and others. He is a coauthor of “Resource Allocation Problems: Algorithmic Approaches” (MIT Press,1988). He had been a guest editor of special issues in Discrete Applied Mathematics and Algorithmica. He is currently on the Editorial Board of Computational Geometry: Theory and Applications. His research interests include the design and analysis of combinatorial and geometric algorithms, data mining and architectural information systems.
