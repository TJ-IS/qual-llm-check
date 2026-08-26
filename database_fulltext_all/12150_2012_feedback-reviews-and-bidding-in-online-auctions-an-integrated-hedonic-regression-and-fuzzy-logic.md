---
otero_id: 12150
otero_key: "WVEX32CY"
title: "Feedback reviews and bidding in online auctions: An integrated hedonic regression and fuzzy logic expert system approach"
authors: ""
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/i.dss.2012.12.025"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Feedback reviews and bidding in online auctions: An integrated hedonic regression and fuzzy logic expert system approach

Jie Zhang <sup>a,</sup>⁎, Edmund L. Prater <sup>a</sup>, Ilya Lipkin

<sup>a</sup> College of Business Administration, University of Texas at Arlington, Box 19437, Arlington, TX 76019, USA <sup>b</sup> Predator/Reaper Simulator program, United States Air Force, Wright Patterson AFB, Dayton, OH 45433, USA

## a r t i c l e i n f o

Available online 30 December 2012

Keywords: Online auction Hedonic regression Fuzzy logic Bidding behavior

## a b s t r a c t

In online auctions, user-generated feedback reviews provide <sup>fi</sup>rst-hand information on the trustworthiness of transaction partners to the community. To examine how the feedback reviews are taken into account of the buyers' bidding decisions and thus affect the <sup>fi</sup>nal winning price of an auction, we thoroughly examine how buyers mentally interpret the seller's reviews and adjust the bids accordingly. With ample bidding results data from a popular auction website eBay.com, this paper adopts an integrated approach of Fuzzy Logic Expert System (FLES) model and a statistical hedonic regression model to examine the research question. In particular, we use the hedonic regression approach to select key variables, which are then entered into a FLES analysis to generate knowledge base regarding the relationships between variables such as item characteristics, auction characteristics and review scores, and the <sup>fi</sup>nal winning price. This integrated approach combines the advantages of both methods, and also overcomes their own limitations. In addition, we also present the insights gained from bidding behaviors utilizing each of the approaches.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

In online auctions, user-generated feedback reviews provide <sup>fi</sup>rst-hand information on the trustworthiness of transaction partners to the community. The literature on consumers' bidding decisions in online auctions has mainly focused on the buyers' trust building based on the feedback system (Ba and Pavlou [3], McDonald and Slawson [20], Melnik and Alm [21], Bajari and Hortacsu [5], Dewan and Hsu [8], Houser and Wooders [13], and Resnick et al. [27], Zhang [38], and Lucking-Reiley et al. [18]). Most of these studies adopted a hedonic regression model. According to hedonic theory, each good is considered as a set of characteristics and the price of the good is explained by the consumers' preferences for all those characteristics (Rosen [28], Epple [9] and Bajari and Benkard [4]). As a result, hedonic regression models are empirical summaries of the relationship between the prices and the characteristics of goods sold. In the research setting of online auctions, the constituent characteristics include detailed product information (name, brand, color, degree of use, etc.), auction settings (starting and ending time, minimum bid, shipping price, etc.), seller and buyer's background (user ID, location, member since, etc.). Hence a hedonic regression model enables us to examine the impact of each variable on the bidding outcome.

Hedonic regression model can provide direct connection between each individual variable to the winning price. However, due to the limitations of this approach, it cannot offer causal and combinatorial explanations to the relationships between the auction parameters and outcomes. Since there are signi<sup>fi</sup>cant amount of variables appearing in each auction, a buyer usually does not decide the bid based on each variable independently, but consider some or all the variables in interactive and complicated ways. To gain additional insights on this problem, it is necessary to explore different methods to systematically evaluate consumer online behaviors.

To overcome the limitation mentioned above, we choose to use a Fuzzy Logic Expert System (FLES) auto rule-generation technique. Fuzzy logic (FL) theory was introduced by Latfeh Zadeh [35–37] and developed over time with the stated goal to broaden the ability of decision analysis to handle imprecise sets by leveraging the role of natural language and probability theory. FL can be found everywhere today; from cars, automatic transmissions, photo cameras to automatic traf<sup>fi</sup>c controller systems. One of the reasons for such a proliferation of FL is its ease of use combined with its robustness in solving dif<sup>fi</sup>cult problems. To that end it is important to understand how this can be applied to online auctions.

When dealing with human subiects, one of the difficulties is the complexity of human decision making. One of the advantages of FL is its use of natural language structure to convey complex decision making criteria in an easy to understand form. Further analysis of the natural language patterns (rules) can shed light into shopper's behavior so as to provide better insight into what drives online interactions between buyers and sellers on eBay. With this approach it is possible to answer the problem posed by Ha et al. [11] on the possibility of having a natural language option to examine complex system of patterns. This in turn will enable marketers to view “how individual predictor variables will in<sup>fl</sup>uence the target and how they would interact”. In this regard we will use a similar technique as Wu and Wu [34] when they used FL to provide e-commerce product recommendations from a trustworthy vendor by utilizing the user's own preferences. Kent [16] also adopted both the regression and FLES approaches to study the causal relationships between multiple variables and a dependent variable. Other studies in the engineering and medical <sup>fi</sup>elds (Andres et al. [2], Hasiloglu et al. [12], Kwok et al. [17]) have concentrated on a straight accuracy comparison between FLES and regression.

To examine how the feedback reviews are taken into account of the buyers' bidding decisions and thus affect the <sup>fi</sup>nal winning price of an auction, we examine how buyers mentally interpret the seller's reviews and adjust the bids accordingly. It is the goal of this paper to present insights gathered from the use of both the hedonic regression model and the FLES model. The hedonic regression model can reveal the independent contribution of each individual variable to the prediction of the winning price after controlling all the other variables. On the other hand, the contribution of FLES is to reveal the detailed inter-relationship among the independent variables and how these variables together affect the bidding behaviors on eBay. We use the hedonic regression approach to select key variables, which are then entered into a FLES analysis to generate knowledge base regarding the relationships between variables such as item characteristics, auction characteristics and review scores, and the <sup>fi</sup>nal winning price. This integrated approach combines the advantages of both methods, and also overcomes their own limitations.

This paper aims to present a better understanding of how customers on eBay adjust their bids according to reviews, through the use of an integrated approach of two models. We present the theories and compare the advantages and disadvantages of each method in Section 2. Variables and data are described in Section 3. Detailed models and results are presented in Section 4. Additionally, practical implications of this study will be presented in Section 5. Section 6 concludes the paper.

## 2. Theoretical background

## 2.1. The strengths and limitations of the hedonic regression approach

Regression analysis focuses on the relationship between a dependent variable and one or more independent variables based on a functional speci<sup>fi</sup>cation. Regression analysis estimates the change of the dependent variable when any one of the independent variables is varied, while the other independent variables are held fixed. Thus, regression analysis can measure not only the impact of an independent variable on the dependent variable, but also the extent of the impact.

However, the regression approach has many limitations suggested by the literature (Ragin [26], Schrodt [30], Kent [16], Ahmed et al. [1]):

First, regression analysis assumes that variables have normal distributions. Non-normally distributed variables (highly skewed variables, platykurtic or leptokurtic distributions or variables with substantial outliers) can distort relationships and signi<sup>fi</sup>cance tests. This assumption limits the application of this method to data samples with multi-modal or categorical types of variables.

Second, regression analysis assumes that each independent variable makes a <sup>fi</sup>xed unit impact on the dependent variable, ignoring the inter-relationships between variables or the possibility that when some conditions are combined, the impact of an individual independent variable may be very different.

Third, the assumptions of additivity and linearity in regression analysis make possible the extrapolated results beyond the range of ob served values.

Fourth, regression analysis ignores asymmetrical relationships between inputs and outcomes and the combinatorial effects of input factors. Thus it fails to distinguish necessary and suf<sup>fi</sup>cient causes.

## 2.2. The FLES approach

Fuzzy Logic (FL) is a superset of conventional Boolean logic that has been extended to handle the concept of partial truth. That is, it can handle values between such concepts of Boolean logics of completely true (1) and completely false (0). Classically, this is referred to as the law of the excluded middle and was originally developed as part of Aristotelian logic. FL was introduced in the 1960s as a means to model the uncertainty of natural language. A Fuzzy Logic Expert System (FLES) is a system that uses a collection of fuzzy membership functions and rules, instead of Boolean logic, to reason about data (Kent [16]). The rules in a FLES usually have an ‘If–Then’ form and can be applied to the dataset, or the methodology can auto-generate rules from the given dataset which can be used for estimation (Garratt and Hodgkinson [10]). The set of rules in a FLES, known as the rule base or knowledge base, are formulated as combinations of conditions leading to an outcome.

This approach offers several unique advantages over hedonic regression. First, FLES can be translated into a set of simple rules which can be analyzed in a more user-friendly form (Ha et al. [11]). Secondly, an advantage of using FLES is the ability to use Fuzzy Set Theory with cluster analysis while creating pattern sets and boundaries (Wen et al. [33]). Thirdly, unlike regression models, results of FLES are bounded by actual dataset feasibility limits, thus it is not possible to achieve results outside upper or lower bounds of the stated problem set. For a more detailed discussion of this boundary problem as applied to market de<sup>fi</sup>nition, see Hrushka [14].

On the other hand, FLES cannot assess the relative contribution of potential conditions to an outcome and therefore it cannot pick out the key variables. In our research problem of eBay auctions, the winning bid price depends on as many as 16 factors and each factor is recorded as low, medium or high. That can result in a maximum of 3<sup>16</sup> rules. If we can remove some insigni<sup>fi</sup>cant variables, it will signi<sup>fi</sup>cantly reduce the complexity and improve clarity of the knowledge base. Kent [16] suggests that regression models can “be used in a first stage to select key variables which are then entered into a fuzzy logic model to analyze the asymmetric relationships and alternative ways to an outcome”.

Given these strengths and weakness of the two approaches (summarized in Table 1), we adopt an approach of using a hedonic regression model to select variables that have signi<sup>fi</sup>cant importance to the winning price, and then applying the selected variables to FLES to derive the knowledge base

The strengths and weaknesses of the regression and FLES methods.

<table><tr><td>Regression</td><td>FLES</td></tr><tr><td>Can measure the extent to which each condition is correlated with the outcome variable</td><td>Ignore assessment of the relative contribution of potential conditions to an outcome</td></tr><tr><td>Assume each independent variable makes a fixed unit of contribution to an outcome.</td><td rowspan="2">Study the configuration of conditions relating to an outcome. When some conditions are combined, the contribution of individual factors may be very different, even reversed.</td></tr><tr><td>Do not allow for the possibility that outcomes maybe achieved in more than one way</td></tr><tr><td>Focus on distribution of variables. Cannot handle categorical data</td><td rowspan="2">Ignore variation and distribution in each variable. Can handle categorical data Will not go beyond range</td></tr><tr><td>Linear and additive relationships may obtain extrapolated values out of the practical range</td></tr><tr><td>Symmetrical relationships between dependent and independent variables.</td><td rowspan="2">Can detect asymmetrical relations: focus on conditions that may be sufficient, necessary or both.</td></tr><tr><td>Cannot distinguish between relationships that are sufficient but not necessary or necessary but not sufficient.</td></tr><tr><td>Results are very specification dependent and unstable</td><td>Results are specification independent</td></tr></table>

## 3. Data collection and description of the variables

To study the buyers' bidding behaviors at eBay.com, we used a web agent program to collect transaction and feedback data of eBay auctions of Apple iPod MP3 players with a closing date ranging from February 14 to May 27, 2004. During that period the product experienced unusually high demand for the new generations of iPods and the market price stayed stable, as re<sup>fl</sup>ected on the iPod.com and major electronic product web sites such as CNET.com and PCMag.com. To control the value of the auction items, we only kept transactions of iPods with a capacity of 15 G or 20 G, and removed transactions that did not end up with a sale. We were left with 1768 valid auction transactions, which constitute our primary data sample.

The agent program automatically downloaded the relevant transaction data, including trading item, the seller's user ID and the winning buyer's ID, starting and end date/time, starting bid prices, end prices, number of bidders participated, description of the auction items, and the entire feedback history of the seller and the other bidders from their previous transactions. We focus on what determines the <sup>fi</sup>nal winning price, or SoldPrice of an auction, which is the second highest bid plus an increment according to the bidding policy of eBay. This price is an important indicator of the auction outcome because it directly determines not only a bidder's winning or losing but also the pro<sup>fi</sup>t of the seller.

eBay uses its feedback system to signal the reputation of its users. We measure the reputation of a buyer or seller by the unique number of positive, neutral or negative ratings he/she received from previous transactions up to the end time of the auction. A single customer may report multiple comments. In order to eliminate the bias from the comments of a set of particular customers and also to reduce the effect of reputation manipulation, we count only the <sup>fi</sup>rst comment left by a customer to evaluate the above reputation variables. This is common in the literature, and also consistent with eBay's practice in calculating reputation scores. We measure the seller reputation with variables Pos, Neg, and Neu which are the number of positive, negative and neutral comments from unique registered users, respectively. Other variables SellerScore and PosRatio are the difference between the seller's positive and negative rating numbers from unique users and the ratio of the seller's positive rating number among his/her total rating number, respectively. We use BuyerScore, which is the difference between the buyer's positive and negative rating numbers from unique registered sellers, to measure the experience and reputation of the buyer at eBay.

Characteristics of the auction items are de<sup>fi</sup>ned as Size, Generation, Accessories, and NIB. A standard iPod MP3 player comes with accompanying accessories like Apple earphones, AC adapter, <sup>fi</sup>re wire cable, PC <sup>fi</sup>re wire adapter, etc. The auction items in our sample are homogeneous except for size (15 G or 20 G), generation (the 1st to the 3rd), accessories and degree of usage. A greater capacity or later generation iPod MP3 player is valued more than a smaller or an earlier generation one. Size (0 as 15 G and 1 as 20 G) and Generation (1 to 3) are included as dummies. Extra accessories will increase the value of the item and a brand new iPod is typically worth more than a used one. So we control the accessories and the new or used property of the auction items with the variable Accessories and a dummy variable NIB. The variable Accessories represents the value of the extra accessories included (positive value) or required ones missing (a negative value) in the item. The market prices of the accessories were obtained from the Apple's online store.

The remaining variables capturing the auction's characteristics are: NumofBids, Length, StartingBid, Bold, Reserve and BIN. NumofBids refers to total number of bids appearing in the bid history of an auction. Since we remove those withdrawn or no-bid transactions in the sample, there are at least one bid for each transaction: NumofBids>0. Length is the number of days an action listing lasts. StartingBid is the starting bid amount set by the seller. Bold is a dummy variable and refers to whether the seller boldfaced the listing on search and listing pages. It controls the sellers' effort to grab the buyers' eyeballs. We use the dummy variables Reserve and BIN to indicate whether the seller puts a reserve price and whether the seller adopts the Buy-it-now option in the auction.

Table 2 shows descriptive statistics and correlation matrix of the variables used in our analysis. The winning price ranges from a high of \$780.00 to a low of \$162.50. The mean trading price of 15 G iPods is \$274.21 and the mean trading price of 20 G iPods is \$317.74, which are lower than the market price of \$299.00 and \$399.00 posted on Apple online store during the research period, respectively.

To assess the predictive power of the methods, we divide the data sample into two sets: the <sup>fi</sup>rst 1199 transaction records are used as training data to generate the rules governing the bidder's behaviors, and the remainder of the data set of 569 samples is used for testing.

## 4. Model

## 4.1. The hedonic regression model

We <sup>fi</sup>rst analyze the eBayer's bidding behavior through a hedonic regression model that takes the characteristics of auction items, auction design and reputations as independent variables and the winning prices of auctions as dependent variables ([3,5,8,13,18,20,38]). The variable Pos is the sum of SellerScore and Neg. Thus it is taken out in the regression model to avoid multi-collinearity. Fifteen independent variables Size, Generation, Accessories, NIB, Neg, Neu, SellerScore, PosRatio, BuyerScore, NumofBids, Length, StartingBid, Bold, Reserve and BIN are entered into the analysis, represented by $X _ { i } i = 1 , 2 , \dots 1 5$

$$
\text { Sold   Price } = \alpha + \sum_ {i = 1} ^ {1 5} \beta_ {i} X _ {i}.\tag{1}
$$

The results in Table 3 show that two variables Bold and Reserve are not statistically signi<sup>fi</sup>cant and therefore do not affect sold price. Product characteristics have a strong impact on closing prices: iPod MP3 players with a large size, recent generation, brand new or more accessories have a higher market price and therefore are bid at a higher price. As to auction design, the seller set a higher starting price, no buy-it-now option, and a longer duration will end up with a higher closing price. Moreover, seller reputation also has an important impact on buyers' bid. Due to the information asymmetry on eBay online auction, the buyers and sellers remain anonymous and are recognized by their own unique ID. Over the virtual cyberspace, the traders do not know each other or see each other. All they know about the counterpart's background are the reputation scores provided by his/her previous traders. Our regression results show that buyers do pay a lot of attention to the review scores: a seller with a high net score or a low negative score is expected to sell their goods with a higher price. At the same time, a buyer with a higher review score are more experienced with eBay auctions. They usually have made a lot of transactions on eBay and hence they can win the auction with a lower price.

In the hedonic regressions models, we use adjusted $R ^ { 2 }$ , which is an indicator of the degree of <sup>fi</sup>tness in order to measure the degree of <sup>fi</sup>tness. The adjusted $R ^ { 2 }$ in the regression model with the training data for the following three models are around the level of 74%.

## 4.2. Fuzzy logic pattern generation

We use FLES for pattern recognition and use the rule-based knowledge patterns to generate practical suggestions on the estimation of sold prices in online auctions. When faced with complex decisions such as the selecting a product from a set of options, consumers may use dif ferent decision strategies. Payne et al. [23] suggest that consumers use a variety of decision strategies such as weighted additive rule, satisfying heuristic, lexicographic heuristic, etc. based on the desired decision's accuracy and the effort level that they are willing to invest in a particular decision problem.

Table 2  
Descriptive statistics of the data sample (N=1768).

<table><tr><td colspan="3"></td><td colspan="3">Variable</td><td colspan="3">Mean</td><td colspan="3">Std. dev.</td><td colspan="3">Min</td><td colspan="3">Max</td></tr><tr><td colspan="3">Dependent variable</td><td colspan="3">SoldPrice</td><td colspan="3">288.68</td><td colspan="3">46.27</td><td colspan="3">162.50</td><td colspan="3">780.00</td></tr><tr><td rowspan="6" colspan="3">Reputation variables</td><td colspan="3">BuyerScore</td><td colspan="3">40.19</td><td colspan="3">121.95</td><td colspan="3">-2</td><td colspan="3">3008</td></tr><tr><td colspan="3">SellerScore</td><td colspan="3">1678.81</td><td colspan="3">2506.53</td><td colspan="3">-1</td><td colspan="3">46,377</td></tr><tr><td colspan="3">PosRatio</td><td colspan="3">0.95</td><td colspan="3">0.17</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td colspan="3">Pos</td><td colspan="3">1722.54</td><td colspan="3">2569.61</td><td colspan="3">0</td><td colspan="3">47,880</td></tr><tr><td colspan="3">Neg</td><td colspan="3">43.73</td><td colspan="3">69.39</td><td colspan="3">0</td><td colspan="3">1403</td></tr><tr><td colspan="3">Neu</td><td colspan="3">57.99</td><td colspan="3">81.61</td><td colspan="3">0</td><td colspan="3">1287</td></tr><tr><td rowspan="4" colspan="3">Item characteristics</td><td colspan="3">Accessories</td><td colspan="3">16.58</td><td colspan="3">287.26</td><td colspan="3">-160</td><td colspan="3">6000</td></tr><tr><td colspan="3">Generation</td><td colspan="3">2.88</td><td colspan="3">0.33</td><td colspan="3">1</td><td colspan="3">3</td></tr><tr><td colspan="3">NIB</td><td colspan="3">0.55</td><td colspan="3">0.50</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td colspan="3">Size</td><td colspan="3">0.32</td><td colspan="3">0.47</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td rowspan="6" colspan="3">Auction characteristics</td><td colspan="3">NumofBids</td><td colspan="3">16.52</td><td colspan="3">12.34</td><td colspan="3">0</td><td colspan="3">57</td></tr><tr><td colspan="3">Length</td><td colspan="3">3.21</td><td colspan="3">2.28</td><td colspan="3">0</td><td colspan="3">10</td></tr><tr><td colspan="3">StartingBid</td><td colspan="3">98.09</td><td colspan="3">124.64</td><td colspan="3">0.01</td><td colspan="3">499</td></tr><tr><td colspan="3">Bold</td><td colspan="3">0.16</td><td colspan="3">0.37</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td colspan="3">Reserve</td><td colspan="3">0.13</td><td colspan="3">0.33</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td colspan="3">BIN</td><td colspan="3">0.22</td><td colspan="3">0.41</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td colspan="18">Correlation matrix</td></tr><tr><td>Variables</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td><td>(11)</td><td>(12)</td><td>(13)</td><td>(14)</td><td></td><td></td><td></td></tr><tr><td>(1) SellPos</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(2) SellNeg</td><td>0.79</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(3) BuyPos</td><td>0.02</td><td>-0.05</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(4) BuyNeg</td><td>0.22</td><td>0.38</td><td>0.18</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(5) Accessories</td><td>-0.04</td><td>-0.04</td><td>-0.02</td><td>-0.04</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(6) Generation</td><td>0.15</td><td>0.19</td><td>0.01</td><td>0.19</td><td>0.02</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(7) NIB</td><td>-0.01</td><td>0.12</td><td>-0.03</td><td>0.33</td><td>-0.05</td><td>0.38</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(8) Size</td><td>-0.11</td><td>-0.17</td><td>-0.11</td><td>-0.12</td><td>-0.04</td><td>-0.48</td><td>-0.20</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(9) NumofBids</td><td>0.01</td><td>-0.03</td><td>-0.02</td><td>-0.005</td><td>-0.03</td><td>0.02</td><td>0.09</td><td>0.04</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(10) Length</td><td>-0.13</td><td>-0.13</td><td>-0.10</td><td>-0.11</td><td>-0.001</td><td>-0.15</td><td>-0.18</td><td>0.16</td><td>0.24</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(11) StartingBid</td><td>-0.06</td><td>-0.05</td><td>0.04</td><td>-0.10</td><td>0.09</td><td>-0.02</td><td>-0.14</td><td>0.02</td><td>-0.81</td><td>-0.21</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(12) Bold</td><td>-0.12</td><td>-0.26</td><td>0.18</td><td>-0.20</td><td>-0.01</td><td>-0.16</td><td>-0.26</td><td>0.05</td><td>0.12</td><td>0.04</td><td>-0.08</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(13) Reserve</td><td>-0.03</td><td>-0.08</td><td>-0.10</td><td>-0.16</td><td>-0.01</td><td>-0.14</td><td>-0.22</td><td>0.17</td><td>-0.07</td><td>0.11</td><td>0.10</td><td>0.01</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>(14) BIN</td><td>0.02</td><td>0.03</td><td>0.13</td><td>0.01</td><td>-0.02</td><td>0.03</td><td>0.03</td><td>-0.08</td><td>-0.63</td><td>-0.45</td><td>0.75</td><td>-0.09</td><td>0.03</td><td>1.00</td><td></td><td></td><td></td></tr></table>

To that end there have been several attempts of using FLES as a clustering solution. As Pedrycz [24] suggested, it is possible to use knowledge oriented hints as a guiding strati<sup>fi</sup>cation principle in a FLES system. Knowledge based hints are classi<sup>fi</sup>ed into three types ([24]): Uncertainty of class membership which implies that categorization of patterns is dif-<sup>fi</sup>cult depending on borderline characteristics of the pattern and pattern class straightforwardness to assess its belongingness; Proximity, which re<sup>fl</sup>ects distance between selected pairs of patterns and quanti<sup>fi</sup>es the selected judgment as to the closeness of some pairs of patterns; Labeling indicates that some knowledge patterns (rules) are labeled or assigned to

Table 3  
Regression results with the training data.

<table><tr><td rowspan="2">Dependent variable: SoldPrice</td><td colspan="2">Model I</td><td colspan="2">Model II</td><td colspan="2">Model III</td></tr><tr><td>Coefficient</td><td>t</td><td>Coefficient</td><td>t</td><td>Coefficient</td><td>t</td></tr><tr><td>Intercept</td><td>53.985</td><td>9.421****</td><td>53.016</td><td>9.164****</td><td>57.108</td><td>10.000****</td></tr><tr><td>NumofBids</td><td>.533</td><td>6.676****</td><td>.508</td><td>6.254****</td><td>.512</td><td>6.353****</td></tr><tr><td>Size</td><td>61.424</td><td>46.169****</td><td>61.504</td><td>45.489****</td><td>61.342</td><td>45.854****</td></tr><tr><td>Generation</td><td>66.299</td><td>35.553****</td><td>66.443</td><td>35.078****</td><td>65.742</td><td>34.936****</td></tr><tr><td>NIB</td><td>14.323</td><td>9.123****</td><td>16.800</td><td>11.779****</td><td>17.042</td><td>12.328****</td></tr><tr><td>Accessories</td><td>.209</td><td>13.443****</td><td>.210</td><td>13.290****</td><td>.211</td><td>13.442****</td></tr><tr><td>Bold</td><td>2.149</td><td>1.276</td><td>1.324</td><td>.788</td><td></td><td></td></tr><tr><td>StartingBid</td><td>.031</td><td>3.081***</td><td>.009</td><td>1.168</td><td>.032</td><td>3.387***</td></tr><tr><td>Reserve</td><td>1.982</td><td>1.202</td><td>2.061</td><td>1.225</td><td></td><td></td></tr><tr><td>BIN</td><td>-5.648</td><td>-2.168**</td><td></td><td></td><td>-10.775</td><td>-4.398****</td></tr><tr><td>Length</td><td>.851</td><td>2.819**</td><td>1.069</td><td>3.911****</td><td>.527</td><td>1.775**</td></tr><tr><td>ByerScore</td><td>-.009</td><td>-1.990*</td><td>-.010</td><td>-2.219****</td><td>-.008</td><td>-1.829**</td></tr><tr><td>SellerScore</td><td>.003</td><td>4.571****</td><td>.003</td><td>4.563****</td><td>.003</td><td>5.244****</td></tr><tr><td>PosRatio</td><td>-1.614</td><td>-5.762****</td><td></td><td></td><td></td><td></td></tr><tr><td>Neg</td><td>-0.279</td><td>-5.475****</td><td>-.106</td><td>-4.328****</td><td>-.118</td><td>-5.117****</td></tr><tr><td>Neu</td><td>0.159</td><td>3.734****</td><td></td><td></td><td></td><td></td></tr><tr><td>R square</td><td>.752</td><td>.741</td><td>.745</td><td></td><td></td><td></td></tr><tr><td>Adj. R square</td><td>.749</td><td>.738</td><td>.742</td><td></td><td></td><td></td></tr></table>

⁎⁎⁎⁎ p valueb0.001.  
⁎⁎⁎ p valueb0.01.  
\*\* p valueb0.1.  
\* p valueb0.5.

Table 4

be part of a knowledge base cluster. These three approaches can be successfully applied to online consumer bidding behavior data as they allow for more ef<sup>fi</sup>cient pattern analysis.

## 4.3. Construction of the FLES model

The model selected for our FLES implementation is based on Mamdani's fuzzy inference system (Mamdani [19]). This model is chosen for the simplicity of implementation and speed of execution. In addition, we adopt centroid defuzzi<sup>fi</sup>cation and Zadeh logical operators, and use the stochastic annealing approach for optimization. Triangular membership function is chosen, with three fuzzy terms per variable. This is selected for the need to optimize execution of the FLES engine. The tradeoffs for a more complicated function were considered but the additional gains on accuracy would not be justi<sup>fi</sup>able due to substantially increased processing load time on the system.

Using the FLES in the above settings, an automatic rule generation algorithm is applied to generate a pattern of customer bidding decisions, using the <sup>fi</sup>nal winning price variable as the desired output trainer. The automatic rule generation algorithm uses a k-mean clustering technique, a method of an unsupervised classi<sup>fi</sup>cation where the data are unspeci<sup>fi</sup>ed and no relational information about this data is available. This method minimizes the within-cluster sum of squared distance between a data point and the cluster center. Thus it can obtain optimal minimum squared-error partitions.

This method creates a set of patterns (vectors) in a multidimensional space. These patterns are then organized in relational groups in order to create unique sets of related vectors for further analysis. To better understand this, assume the sample data set $X = \{ x _ { 1 } , x _ { 2 } , . . . . . x _ { n } \} \subset \mathbb { R } ^ { p }$ where x $( i = 1 , . . . , n )$ is a p-dimensional vector. The fuzzy clustering algorithm generates a partition matrix U(X) of size k x $n ,$ and k clusters $\{ C _ { 1 } , C _ { 2 } , . . . . C _ { k } \}$ . An element of the partition matrix $U , u _ { i j } { \in } [ 0 , 1 ]$ , where $i = \{ 1 , 2 , . . k \}$ and $j = \{ 1 , 2 , . . n \}$ , represents the membership degree of the input set x to cluster $C _ { i }$ . The following

probabilistic constraints are assumed: $0 { < } \sum _ { j = 1 } ^ { n } u _ { i j } { < } n$ for i = 1.. k,

$$
\sum_ {i = 1} ^ {k} u _ {i j} = 1 \text {   for   } j = 1 \dots n, \text {   and   } \sum_ {i = 1} ^ {k} \sum_ {j \mid 1} ^ {n} u _ {i j} = n \text {(Pakhira et al. [22])}.
$$

To apply the k-mean clustering results in order to derive if-then rules from data, each cluster induces a rule by projecting the cluster to the corresponding coordinate spaces. We assign a membership degree of the data point X to the cluster based on a triangular membership function to the x of each data point which in turn generates a set of pattern rules in the form of IF $( \xi _ { 1 }$ is $C _ { 1 }$ and $\xi _ { 2 }$ is $C _ { 2 }$ and … and $\xi _ { p - 1 }$ is $C _ { p - 1 } )$ , THEN $( \xi _ { p }$ is $C _ { p } )$ where $\xi _ { 1 } , . . . , \xi _ { p - 1 }$ are input variables and $\xi _ { p }$ which is the output variable. The samples in the data set that have the result of ${ } ^ { \mathfrak { u } } \xi _ { p }$ is ${ C _ { p } } ^ { \prime \prime }$ form a hyper-cube cluster, which is used to identify the unique online auction bidding patterns.

After running the rule generation algorithm, a set of rules is tested on the quality of pattern matching for the same data set. The process is repeated until a best possible set of rules with the maximum number of pattern matching is created. We developed our customized software to implement the above FLES algorithms using the eBay auction data sample described in Section 3 as inputs and output.

## 4.4. Description of the FLES model encoding

Applying our FLES program based on the above theory to our training data set, we obtain a FLES rule set. A typical rule generated by FLES can be described as “a 20 GB, third-generation, new-in-box iPod MP3 player with standard accessories listed at eBay.com with a low starting price and medium duration, where the seller has a medium feedback score and a high sold $p r i c e "$ . To further analyze them, we encode the value of each condition with an integer. Thus, the fuzzy rules are stored in an integer format with a three-value fuzzy score. Integer format in effect will allow additional analysis later on the values of ranges of the variables. This approach provides for easy use of fuzzy logic rules encoding. The encoding scheme for the FLES rules is as follows: a “Low” is coded as 1, “Not Low” as −1, and a “Don't care” condition as 0; similarly “Medium” condition as 2, “Not Medium” as $^ { - 2 , }$ , “High” as 3, and “Not High” as −3. We randomly pick two rules to demonstrate the encoding of the conditions in Table 4.

## 4.5. FLES model ranges and validation

Our FLES program then uses the training data set to adjust the membership functions dynamically. This approach allows the data to choose the ranges of each set of member functions. During the initial setup of FLES model, system selects three membership degrees: Low, Medium, and High. Our customized program adjusts the range boundaries to accommodate the data set dynamically. For example, the initial range of SellerScore is from 0 to 1, while the actual data range is from −1 to 46,377. During rule generation, the range of Seller Score is adjusted accordingly. K-clustering analysis is used to best <sup>fi</sup>t the data to our membership degrees, i.e. Low, Medium, or High. For example, Fig. 1 shows the membership functions of different degrees of the variables seller Score, NumofBids, StartingBid and SoldPrice. The values of the critical points of the Low Seller Score membership function are: 2374.87 for the left point, 6042.73 for the left <sup>fl</sup>ex point, 9710.6 for the center point, and 46,377 for the right point. The values of the left, left <sup>fl</sup>ex, center, right <sup>fl</sup>ex, and right points for the Medium NumOfBids membership function are 3.61, 11.48, 19.35, 25.57 and 31.79, respectively.

These adjusted values are used to auto generate rules from the training data. The rules represent a condensed version of the dataset itself. Similar patterns are grouped into a combined pattern/rule, which allows us to simplify the rule set. As a result, we obtain 313 rules that describe eBay users' bidding decisions, a much smaller number compared with the sample size, while being completely representative of the original dataset.

## 4.6. The frequency table

During pattern merging and analysis, we also create a frequency table to show the frequency of a condition appearing in the knowledge base and therefore demonstrate common customer bidding decision factors that lead to a certain degree of sold prices. The frequency table is strati<sup>fi</sup>ed into three categories: Low, Medium and High, based on the sold price. The variables are analyzed by dominant percentage of the category that stays constant when contributing to the <sup>fi</sup>nal sold price. In addition if the variable frequency percentage is less than 40%, this variable is not considered as signi<sup>fi</sup>cant. The 40% cutoff is determined to be a good indicator as to degree of participation of that variable on the <sup>fi</sup>nal sold price of the item, therefore anything less than that would not be considered.

Looking at Table 5, the frequency distribution for the ‘Reserve’ variable was strati<sup>fi</sup>ed into High sold price rules. We conclude that this variable is signi<sup>fi</sup>cant, as 69.1% of the time FLES rules preferred to have a low reserve price that contributed highly to a high sold price.

The fuzzy logic rule set.

<table><tr><td>Rule#</td><td>Size</td><td>Generation</td><td>NIB</td><td>Accessories</td><td>StartingBid</td><td>NumofBids</td><td>BIN</td><td>Length</td></tr><tr><td>193</td><td>1</td><td>3</td><td>1</td><td>3</td><td>2</td><td>2</td><td>1</td><td>3</td></tr><tr><td>65</td><td>-2</td><td>3</td><td>1</td><td>3</td><td>1</td><td>3</td><td>1</td><td>1</td></tr><tr><td colspan="2">BuyerScore</td><td colspan="2">SellerScore</td><td>PosRatio</td><td>Pos</td><td>Neg</td><td>Neu</td><td>SoldPrice</td></tr><tr><td colspan="2">1</td><td colspan="2">1</td><td>2</td><td>1</td><td>1</td><td>1</td><td>3</td></tr><tr><td colspan="2">1</td><td colspan="2">1</td><td>2</td><td>1</td><td>1</td><td>1</td><td>3</td></tr></table>

![](/api/attachments/WVEX32CY/fulltext/images/c2c2886b6e19a4ef98a1ab1fb7825260bcf3ce1bdfe5c73e44e8b389704e1bce.jpg)

![](/api/attachments/WVEX32CY/fulltext/images/f46b77fa5a098457435743ded8e41b246b9b6726a5ea374380c426cc5d4edbd9.jpg)

![](/api/attachments/WVEX32CY/fulltext/images/16a12f7ce1d89d8a01a1b994255f1b642ef7068913bfdbbd076c8156827e0088.jpg)  
Fig. 1. The membership functions of different degrees of the variables.

Table 6 shows the frequency distribution for the Length variable, which is strati<sup>fi</sup>ed into High sold price rules. Based on the information in Table 6, we conclude that the length of an auction cannot signi<sup>fi</sup>- cantly contribute to a high sold price, as there is no clear preference to have Low, Medium, or High levels of auction length in the rules of a high sold price.

![](/api/attachments/WVEX32CY/fulltext/images/6bdec378a4d47e7ebaf7446f224346b8e9547c3453cbcd76309990521439fe60.jpg)

To better understand buyer and seller strategies, we construct the frequency Table 7 based on the frequency that a particular condition occurs in the pattern rule set for High, Medium, or Low SoldPrices. For example, a High level of Size condition (20 GB) occurs 81.9% of the time when an auction ends up with a High SoldPrice. For those auction transactions with a Medium SoldPrice, Low Size (15 GB) appears 57.9% of the time; and for those auction transactions with a Low SoldPrice, the frequencies of high and low Sizes are 57.7% and 41%, respectively. This breakdown leads to several major conclusions. One of the most important conclusions from this table is that, if size of the product is high, then it is highly possible that the <sup>fi</sup>nal SoldPrice will also be high, suggesting that this variable is a very good indicator of high SoldPrice. In contrast, low size items may end up with a medium or low SoldPrice. Similar analysis is conducted for all the other variables, with emphasis on the frequency of the condition in the knowledge base. This in turn classi<sup>fi</sup>es each variable as a contributing agent for different high, medium, and low <sup>fi</sup>nal SoldPrice. In Table 7, we highlight in boldface the percentage of occurrence frequency that is signi<sup>fi</sup>cant and the highest among the contributors for the SoldPrice.

## 4.7. Prediction accuracy

The quality of the rules is evaluated by the number of samples that are correctly classi<sup>fi</sup>ed over the total sample size of the test data. The fuzzy model on a training data set of 1199 variables generates a predication accuracy of 89%. To validate the accuracy of the rules generated by FLES, we use the membership functions generated from the above training set to predict the memberships of SoldPrices for the rest of the 569 transactions. Among those transactions, the rules can accurately predict the realized sold prices of 402 transactions. Thus the predication accuracy of the test data set is 71%.

<table><tr><td colspan="6">Reserve</td></tr><tr><td></td><td></td><td>Frequency</td><td>Percent</td><td>Valid percent</td><td>Cumulative percent</td></tr><tr><td rowspan="4">Valid</td><td>-2</td><td>3</td><td>3.2</td><td>3.2</td><td>3.2</td></tr><tr><td>1</td><td>65</td><td>69.1</td><td>69.1</td><td>72.3</td></tr><tr><td>3</td><td>26</td><td>27.7</td><td>27.7</td><td>100.0</td></tr><tr><td>Total</td><td>94</td><td>100.0</td><td>100.0</td><td></td></tr></table>

It turns out that the prediction accuracy of FLES for the test data is in the same level as the R square for the regression models based on the test data, 71% vs. 73%. And the average prediction accuracy of FLES for the whole data set is 80%, signi<sup>fi</sup>cantly higher than the R square of the regression approach for the whole data set, 74.3%.

## 5. Discussion

## 5.1. Suggested seller strategies

The results from the two approaches provide rich business insights for eBay buyers, sellers as well as the management. Speci<sup>fi</sup>cally, the results of the Hedonic regression model (Table 3) and the fuzzy rules and the frequency table (Table 7) suggest crucial factors and conditions that affect the winning prices of online auctions.

Our regression results suggest that the sellers' auction design choice of boldfacing the listing title and setting a secret reserve price are insigni<sup>fi</sup>cant in explaining the closing price. There are mixed <sup>fi</sup>ndings in the literature regarding the impacts of these two variables on the closing price. Bajari and Hortacsu [5] found that using a secret reserve price reduces seller revenue; but Lucking-Reiley et al. [18] suggested the presence of a secret reserve price increase the auction price. Possible reasons for our <sup>fi</sup>nding are that while setting a secret reserve price can prevent the item from being sold at an unsatisfactory low price, it may also deter serious bidders from entering the auction, lower the expected sold price and reduce the sold probability of the auction item.

<table><tr><td colspan="6">Length</td></tr><tr><td></td><td></td><td>Frequency</td><td>Percent</td><td>Valid percent</td><td>Cumulative percent</td></tr><tr><td rowspan="6">Valid</td><td>-3</td><td>4</td><td>5.1</td><td>5.1</td><td>5.1</td></tr><tr><td>-1</td><td>2</td><td>2.6</td><td>2.6</td><td>7.7</td></tr><tr><td>1</td><td>30</td><td>38.5</td><td>38.5</td><td>46.2</td></tr><tr><td>2</td><td>18</td><td>23.1</td><td>23.1</td><td>69.2</td></tr><tr><td>3</td><td>24</td><td>30.8</td><td>30.8</td><td>100.0</td></tr><tr><td>Total</td><td>78</td><td>100.0</td><td>100.0</td><td></td></tr></table>

Table 7  
Frequency table distribution for variable.

<table><tr><td rowspan="2">Degree of membership SoldPrice</td><td colspan="3">High</td><td colspan="3">Medium</td><td colspan="3">Low</td></tr><tr><td>Membership</td><td>Contributes</td><td>Percent</td><td>Membership</td><td>Contributes</td><td>Percent</td><td>Membership</td><td>Contributes</td><td>Percent</td></tr><tr><td rowspan="2">Size</td><td>High</td><td>Yes</td><td>81.9%</td><td>Low</td><td>Yes</td><td>57.9%</td><td>Low, High</td><td>Yes</td><td>41.0%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>57.7%</td></tr><tr><td rowspan="2">Generation</td><td>High</td><td>Yes</td><td>89.4%</td><td>High</td><td>Yes</td><td>69.3%</td><td>Med, High</td><td>Yes</td><td>47.4%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>47.4%</td></tr><tr><td rowspan="2">NIB</td><td>Low, high</td><td>Yes</td><td>51.1%</td><td>Low</td><td>Yes</td><td>71.4%</td><td>Low</td><td>Yes</td><td>91%</td></tr><tr><td></td><td></td><td>46.8%</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Accessories</td><td>Med</td><td>Yes</td><td>59.6%</td><td>Med</td><td>Yes</td><td>64.3%</td><td>Med</td><td>Yes</td><td>55.1%</td></tr><tr><td>NumofBids</td><td>Low</td><td>Yes</td><td>40.4%</td><td>Med</td><td>Yes</td><td>40.7%</td><td>Low</td><td>Yes</td><td>64.0%</td></tr><tr><td>StartingBid</td><td>Low</td><td>Yes</td><td>44.7%</td><td>Low</td><td>Yes</td><td>40.0%</td><td>Med</td><td>Yes</td><td>56.4%</td></tr><tr><td>BIN</td><td>Low</td><td>Yes</td><td>76.6%</td><td>Low</td><td>Yes</td><td>77.1%</td><td>Low</td><td>Yes</td><td>71.8%</td></tr><tr><td>Length</td><td>N/A</td><td>No</td><td>N/A</td><td>N/A</td><td>No</td><td>N/A</td><td>N/A</td><td>No</td><td>N/A</td></tr><tr><td>BuyerScore</td><td>Low</td><td>Yes</td><td>79.8%</td><td>Low</td><td>Yes</td><td>70.7%</td><td>Low</td><td>Yes</td><td>71.8%</td></tr><tr><td>SellerScore</td><td>Low</td><td>Yes</td><td>83.0%</td><td>Low</td><td>Yes</td><td>83.6%</td><td>Low</td><td>Yes</td><td>84.6%</td></tr><tr><td>SellerPosRatio</td><td>High</td><td>Yes</td><td>90.4%</td><td>Med</td><td>Yes</td><td>88.6%</td><td>Med</td><td>Yes</td><td>88.5%</td></tr><tr><td>SellerNeg</td><td>Low</td><td>Yes</td><td>90.4%</td><td>Low</td><td>Yes</td><td>92.9%</td><td>Low</td><td>Yes</td><td>87.2%</td></tr><tr><td>SellerNeu</td><td>Low</td><td>Yes</td><td>92.6%</td><td>Low</td><td>Yes</td><td>94.3%</td><td>Low</td><td>Yes</td><td>85.9%</td></tr><tr><td>SellerPos</td><td>Low</td><td>Yes</td><td>83.0%</td><td>Low</td><td>Yes</td><td>84.3%</td><td>Low</td><td>Yes</td><td>84.6%</td></tr></table>

Note: The bold-face values represent the largest frequency values across H, M and L sold price cases.

## 5.2. Obtaining a high sold price

To obtain a high sold price at eBay, the product has to be a high-end one. That is, iPods with a larger storage or a newer model have higher value and thus can potentially attract higher bids. The seller's ratio of positive rating has to be high. One other factor is that the buyer score is low. For eBay transactions, quality is a major uncertainty. For example, recent research by Popkowski et al. [25] found that buy-now prices and a bidder's willingness to pay are moderated by the dif<sup>fi</sup>culty of assessing the products actual value. Since, it is dif<sup>fi</sup>cult to measure the quality of a used item based on someone else's personal opinions the new-in-box term works as a guarantee that the item has the same quality level as any new one sold in a store. Used items lose that quality assurance and therefore tend to be sold for a low price.

The seller's reputation pro<sup>fi</sup>le is a measure for his/her trustworthiness. In such a virtual marketplace as eBay, transactions are conducted between complete strangers who know each other only by an ID name. To build trust among eBay users and to make sure the market exist, eBay asked the users to rate his/her partners based on the trading experiences so that the rating score can signal the honesty of a user. There are a variety of indices, based on the rating score, to measure the players' reputation, that is, positive score, negative score, ratio of positive score and negative one, and a net score (positive score minus negative score). Among those reputation indices, we <sup>fi</sup>nd that the ratio of positive and negative score has the highest impact on high sold price results. The higher the value of this ratio, the higher the probability this consumer is trustable. Therefore the bidders are willing to bid high.

Since buyers receive positive ratings 99.7% of the time, their reputation score is a measure of their experiences of trading at eBay. A low buyer score can be interpreted as an inexperienced eBay user, who tends to incur the winner's curse and bids more than his/her true valuation. This result is also consistent with our regression results.

## 5.3. Obtaining a medium sold price

Auctions will end with a medium closing price at eBay if the product has a medium value of accessories, the seller's numbers of negative and neutral ratings are low, and the seller chooses not to offer a buy-it-now option.

For eBay transactions, quality is a major uncertainty. It is dif<sup>fi</sup>cult to measure the quality of a used item based on somebody else's personal opinions. Therefore the new-in-box term works as a guarantee that the item should have the same quality level as any new one sold in a store. Used items lose the quality assurance and therefore tend to be sold for a low price. The value of accessories increases the bidders' valuation of the product. Therefore, it is clear that medium value of accessories drives medium sold price.

Again, sellers' reputation places an important role in the closing prices. Our regression results suggest that bidders are more sensitive to negative and neutral ratings than positive ones. Hence, the minimum condition for the good not be sold at a low price is that there are not too many negative and neutral ratings. That is the condition for the good to be sold at a medium price. It has no requirement on number of positive ratings.

Our regression results suggest that the buy-it-now option reduces the closing price, because sellers choose to set this option for liquidity. Usually the buy-it-now price equals the valuation of the seller. A bidder with a value higher than the buy-it-now price buys at that price and ends the auction. Thus the seller may lose more potential high bids for an immediate sale. Therefore, sellers, who intend to sell a medium or high price, should not choose the buy-it-now option in the auction.

## 5.4. Obtaining a low sold price

Our results also suggest that auctions closed with low prices sell used iPods and receive small number of bids. The seller has a low positive rating and a low net score. He/She does not boldface the title to attract the eyeball of the bidders, but sets a medium starting price.

Number of bids signals the quality of the product or the credit of the seller from the other users' bidding activities. Therefore, for two auctions with some uncertainty but other identical characteristics, a bidder tend to bid on the auction with a higher number of bids for the belief that the other users' bids carry information. Therefore during the auction low number of bids make buyers balk from bidding. On the other hand, the auction mechanism on eBay is second-price auction. A large enough trading volume is a required to re<sup>fl</sup>ect the consumers' true valuation. Otherwise it will result in low closing prices.

A seller with a low positive rating number and a low net score is likely to be either inexperienced or dishonest. Either factor will reduce the trust from the buyers, thus lower their bids. A high starting price will screen out low value buyers and prevent them from bidding. Therefore, it may reduce number of bids and reduce closing prices for the reason exposited above. However, the regression results of both Section 4.1 and Katkar and Lucking-Reiley [15] suggest that

[27] P. Resnick, R. Zeckhauser, J. Swanson, K. Lockwood, The value of reputation on eBay: a controlled experiment, Experimental Economics 9 (2) (2006) 79–101.

starting price increases seller revenue. It may be due to the advertising effect that a low starting price attracts more buyers and boost up bids. Our fuzzy rule sets also posit that a medium starting price is one of the factors for the items to be undersold. Given the above unfavorable conditions, the seller not advertising his/her listing of the iPod is another condition for the item to be closed at a low price.

## 5.5. Sniping effects

Contrary to the <sup>fi</sup>ndings in our regression results and most of the previous studies that a longer duration will increase the seller pro<sup>fi</sup>ts (Melnik and Alm [21], Lucking-Reiley et al. [18], Cabral and Hortacsu [7]), auction duration is found with no effect on high, medium or low sold price transactions. We explain this with the persistent “sniping” (last-minute bidding) behaviors of bidders reported by some recent work (Roth & Ockenfels [29], Bapna [6]). The auction mechanism of eBay is a second-price auction with a hard end time, which gives bidder incentive to wait to bid at the last minute to avoid a bidding war. This bidding strategy is further supported by many automated sniping software agents such as eSnipe.com, auctionSniper.com, etc. When most of the bidders snipe, a signi<sup>fi</sup>cant amount of bids appear at the last minute of the auction. Therefore the closing price does not re<sup>fl</sup>ect the consumers' true valuation and has no relationship with the duration of the auction.

## 6. Conclusions

We used a FLES approach, besides a hedonic regression model, to analyze customers' bidding behavior at the online auction website eBay. Our results provide comparative validity to both approaches. Hedonic regression offers bene<sup>fi</sup>ts such as straightforward linear relationships, and a more de<sup>fi</sup>nite statistical association between exogenous factors and bidders' decision. However, FLES provides nonlinear relationship interactions, individual predictor behavior, and a chance to explore what drives the relationships to be interdependent as well as their causes. In this regard the results are similar to what was found by Wedel et al. [32] when they found that the main difference between traditional and Fuzzy Clustering Regression (FCR) was that FCR is applicable to a wider variety of retail problems than Overlapping Cluster Regression (OCR).

To that end this paper is more exploratory in nature with real life application. In this case the use of eBay information provides an ample source of buyer/seller interaction in non-biased way, as both the buyer and seller have access to the identical information provided on the website during the auction event. The results indicate merit to this approach as the insights provided can be used to optimize both the buyer selling for a higher price and the seller attempting to get a good deal during the auction

The hedonic regression model can evaluate the relative contribution of a variable to the dependent variable. The Fuzzy Logic approach demonstrates the following major advantages:

• One of the key advantages of FLES over a regression model is that the model will be bounded by practical answers. In other words, with Fuzzy it is not possible to provide an answer that is out of bounds of the original dataset. That is, if upper bound is 300 then the fuzzy answer will never produce results above that, preventing practitioners from receiving results that are impossible in the real world.

• Secondly, the fuzzy knowledge dataset provides a simpli<sup>fi</sup>ed view of the data in the If–Then form. It is far easier to understand the natural language analyses without the requirements of understanding mathematical concepts than the mathematical equations of the regression models.

• Finally, richer information of the knowledge rules can provide additional insights into common business practices that would otherwise be obfuscated by the regression model. For example, if a buyer has a low reputation score and the iPod has low con<sup>fi</sup>gurations then the <sup>fi</sup>nal price will be high, and if a buyer has high reputation score and iPod has low con<sup>fi</sup>gurations then the <sup>fi</sup>nal price will be medium. In this case the reputation level of the buyer is a clear driving factor for the <sup>fi</sup>nal price.

In summary, with regard to the use of FL, our <sup>fi</sup>ndings are similar to those of Steenkamp and Wedel (pg. 316) [31] when they found that “Fuzzy Clustering methods appear to combine the managerial appeal of clustering methods with a more realistic description of the market place, in which consumers do not always belong to one single segment”. Inasmuch as our <sup>fi</sup>ndings agree with theirs, we recommend that researchers add this integrated regression/FL approach to their toolset.

## References

[1] M.A. Ahmed, M.O. Saliu, J. Al-Ghamdi, Adaptive fuzzy logic based framework for software development effort prediction, Information and Software Technology 47 (1) (2005) 31–48

[2] S. Andres, A. Gomez, Estimating a fuzzy term structure of interest rates using fuzzy regression techniques, European Journal of Operational Research 154 (3) (2004) 804–818.

[3] S. Ba, P. Pavlou, Evidence of the effect of trust building technology in electronic markets: price premiums and buyer behavior, MIS Quarterly 26 (3) (2002) 1–26.

[4] P. Bajari, C.L. Benkard, Demand estimation with heterogeneous consumers and unobserved product characteristics: a hedonic approach, Journal of Political Economics 113 (6) (2005) 1239–1276.

[5] P. Bajari, A. Hortacsu, The winner's curse, reserve prices and endogenous entry: empirical insights from eBay auctions, The RAND Journal of Economics 34 (2) (2003) 329–355.

[6] R. Bapna, When snipers become predators: can mechanism design save online auctions? Communications of the ACM 46 (12) (2003) 152–158.

[7] L. Cabral, A. Hortacsu, The dynamics of seller reputation: evidence from eBay, The Journal of Industrial Economics 58 (1) (2010) 54–78.

[8] S. Dewan, V. Hsu, Adverse selection in reputations-based electronic markets: evidence from online stamp auctions, The Journal of Industrial Economics 52 (2004) 497–516.

[9] D. Epple, Hedonic prices and implicit markets: estimating demand and supply functions for differentiated products, Journal of Political Economy 95 (1) (1987) 59–80

[10] P.W. Garratt, A.C. Hodgkinson, A neurofuzzy cost estimator, Proceeding of the 3rd International Conference on Software Engineering and Applications, (SAE) IASTED/Acta Press, Anaheim, California, 1999, pp. 401–406

[11] K. Ha, S. Cho, D. Maclachlan, Response models based on bagging neural networks, Journal of Interactive Marketing 19 (1) (2005) 17–30

[12] A. Hasiloglu, M. Yilmaz, O. Comakli, I. Ekmekci, Adaptive neuro-fuzzy modeling of transient heat transfer in circular duct air flow International Journal of Thermal Sciences 43 (11) (2004) 1075–1090.

[13] D. Houser, J. Wooders, Reputation in auctions: theory, and evidence from ebay, Journal of Economics and Management Strategy 15 (2) (2006) 353–369.

[14] H. Hruska, Market de<sup>fi</sup>nition and segmentation using fuzzy clustering methods, International Journal of Research in Marketing 3 (2) (1986) 1 17–1 34.

[15] R. Katkar, D. Lucking-Reiley, Public versus secret reserve prices in eBay auctions: results from a Pokemon <sup>fi</sup>eld experiment, Working Paper, National Bureau of Economic Research, 2001.

[16] R.A. Kent, Cases as con<sup>fi</sup>gurations: using combinatorial and fuzzy logic to analyze marketing data, International Journal of Market Research 47 (2) (2005) 205–228.

[17] H.F. Kwok, D.A. Linkens, M. Manfouf, G.H. Mills, Adaptive ventilator FiO : advisor use of non-invasive estimations of shunt, Arti<sup>fi</sup>cial Intelligence in Medicine 32 (3) (2004) 157–169.

[18] D. Lucking-Reiley, D. Bryan, N. Prasad, D. Reeves, Pennies from eBay: the determinants of price in online auctions, The Journal of Industrial Economics 55 (2) (2007) 223–233.

[19] E.H. Mamdani, S. Assilian, An experiment in linguistic synthesis with a fuzzy logic controller, International Journal of Man-Machine Studies 7 (1) (1975) 1–13.

[20] C.G. McDonald, V.C. Slawson Jr., Reputation in an internet auction market, Economic Inquiry 40 (3) (2002) 633–650.

[21] M.I. Melnik, J. Alm, Does a seller's reputation matter? Evidence from eBay auctions, The Journal of Industrial Economics 50 (3) (2002) 337–349.

[22] M.K. Pakhira, S. Bandyopadhyayb, U. Maulikc, Validity index for crisp and fuzzy clusters, Pattern Recognition 37 (3) (2004) 487–501.

[23] J.W. Payne, R.J. Bettman, E.J. Johnson, The Adaptive Decision Maker, Cambridge University Press Cambridge, NY 1993

[24] W. Pedrycz, Fuzzy clustering with a knowledge-based guidance, Pattern Recognition Letters 25 (4) (2004) 469–481.

[25] T.L. Popkowski Leszczyc, C. Peter, Y. He Qiu, Empirical testing of the reference-price effect of buy-now prices in internet auctions, Journal of Retailing 85 (2) (2009) 211–221.

[26] C.C. Ragin, Redesigning Social Inquiry, Chicago University Press, Chicago, 2008.

[28] S. Rosen, Hedonic prices and implicit markets: product differentiation in pure competition, Journal of Political Economy 82 (1) (1974) 34–55.

[29] A.E. Roth, A. Ockenfels, Last-minute bidding and the rules for ending second-price auctions: evidence from eBay and Amazon auctions on the internet American Economic Review 92 (4) (2002) 1093–1103

[30] P. Schrodt, Beyond the linear frequentist orthodoxy, Political Analysis 14 (2006) 335–339.

[31] Jan-Benedict E.M. Steenkamp, M. Wedel, Segmenting retail markets on store image using a consumer-based methodology, Journal of Retailing 67 (3) (1991) 300–320.

[32] M. Wedel, Jan-Benedict E.M. Steenkamp, Fuzzy clusterwise regression approach to bene<sup>fi</sup>t segmentation, International Journal of Research in Marketing 6 (4) (1989) 241–258.

[33] K. Wen, K. Peng, Market segmentation via structured click stream analysis, Industrial Management & Data Systems 102 (9) (2002) 493–502.

[34] Z. Wu, H. Wu, An agent-based fuzzy recommendation system using shoppers preferences for E-commerce applications, International Journal of Uncertainty Fuzziness and Knowledge-Based Systems 18 (4) (2010) 471–492.

[35] L.A. Zadeh, Fuzzy logic and approximate reasoning, Synthese 30 (3–4) (1975) 407–428.

[36] L.A. Zadeh, Toward a theory of fuzzy information granulation and its centrality in human reasoning and fuzzy logic, Fuzzy Sets and Systems 90 (2) (1997) 111–127.

[37] L.A. Zadeh, Toward a perception-based theory of probabilistic reasoning with imprecise probabilities, Journal of Statistical Planning and Inference 105 (1) (2002) 233–264.

[38] J. Zhang, The role of players and reputation: evidence from eBay online auctions, Decision Support Systems 42 (3) (2006) 1800–1818.

Jie Zhang is an Assistant Professor of Information Systems in the College of Business Administration at the University of Texas at Arlington. She received her Ph.D. in Computer Information Systems from William E. Simon Graduate School of Business in the University of Rochester. She employs analytical and empirical techniques to examine a number of issues in electronic retail channels, online reputation and feedback systems, software pricing and licensing models, online search behaviors, and website designs. Her research appears in Information Systems Research, Journal of Management Information Systems, Journal of Economics and Management Strategies, Decision Support Systems, Communications of the ACM, among others.

Edmund L. Prater is an Associate Professor of Operations Management in the College of Business Administration at the University of Texas, Arlington. He received his Ph.D in Operations Management from the Georgia Institute of Technology. He also holds a B.S. in Electrical Engineering from Tennessee Technology University and M.S. degrees in both Electrical Engineering and Systems Analysis from Georgia Tech. Prior to obtaining his Ph.D., he was Senior Manager of the Technology Assessment Group at BellSouth where he was in charge of Arti<sup>fi</sup>cial Intelligence Development. He has published in JOM, IJOPM and IJPDLM among other outlets. His current research interests include international supply chains, small and medium sized businesses, and health care.

Ilya Lipkin is the Lead Engineer for the Predator/Reaper Simulator program at the USAF Simulators Division, Wright-Patterson AFB. He was previously a Lead Engineer for Global Hawk Simulator program Wright-Patterson AFB, and software engineer for Expeditionary Fighting Vehicle at Hill AFB. His current research interests include arti<sup>fi</sup>- cial intelligence, human knowledge capture and analysis, neural networks, fuzzy logic, user interface design, software engineering, and UML. Lipkin has a Bachelor degree in computer engineering, a Master's degree in computer engineering, an MBA in operations management, and PhD in Software Project Productivity.
