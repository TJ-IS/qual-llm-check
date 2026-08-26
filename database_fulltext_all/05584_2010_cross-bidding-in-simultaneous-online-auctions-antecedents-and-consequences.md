---
otero_id: 5584
otero_key: "J3RQQJ8X"
title: "Cross-bidding in simultaneous online auctions: Antecedents and consequences"
authors: "Varol O. Kayhan; James A. McCart; Anol Bhattacherjee"
year: "2010"
journal: "Information & Management"
doi: "10.1016/j.im.2010.07.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Cross-bidding in simultaneous online auctions: Antecedents and consequences

Varol O. Kayhan <sup>a,</sup>\*, James A. McCart <sup>b</sup>, Anol Bhattacherjee <sup>b</sup>

<sup>a</sup> Information Systems, University of South Florida – St. Petersburg, 140 Seventh Ave. South, St. Petersburg, FL 33701-5016, United States <sup>b</sup> Information Systems/Decision Sciences, University of South Florida, United States

## A R T I C L E I N F O

Article history: Received 13 March 2009 Received in revised form 22 November 2009 Accepted 1 May 2010 Available online 29 July 2010

Keywords: Online auctions Simultaneous auctions Cross-bidding Empirical research Price discount

## A B S T R A C T

Cross-bidding is a new strategy used in online auctions. The bidder simultaneously monitors several identical auctions, taking advantage of their price differential. We examined the determinants and outcomes of cross-bidding behavior and the contingent factors that shape it. Using empirical data, we demonstrated that cross-bidders can realize significant price discounts compared to non-cross-bidders; the number of experienced bidders in an auction market contributes to more cross-bidding; and this effect is positively moderated by market liquidity of the product being auctioned.

\- 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Online auctions have become liquid markets for a wide variety of goods and services. For instance, the most popular online US auction site eBay had more than 90.1 million active users during the year 2009, who contributed to a gross merchandise volume of more than \$48 billion. Online auctions differ from traditional markets in at least three ways: (1) buyers and sellers are geographically dispersed, (2) prices for goods and services are determined jointly by buyers and sellers based on market supply and demand rather than being fixed by the seller, and (3) all goods and services are eventually sold (market efficiency).

Bidders have been motivated to experiment with different bidding strategies to lower their cost of purchase. One such strategy is ‘‘cross-bidding’’, where a bidder monitors multiple auctions of an identical product, moving back and forth between them, with the goal of winning the one having the lowest possible price [10]. In this strategy, the cross-bidder first identifies a set of simultaneous single-item auctions selling a desired product, then identifies the auction with the lowest standing bid, and finally places a slightly higher bid in this auction. This process is repeated until (1) the bidder wins one of the targeted auctions, (2) the bidder is priced out of the market (i.e., the standing bid exceeds the bidder’s maximum), or (3) all simultaneous auctions have expired.

Though prior studies on online auctions have examined bidding strategies in single-item auctions, very little effort has been directed at cross-bidding. Preliminary research has demonstrated that cross-bidding is an emerging strategy that can lower cost of purchase [1]. However, there is little understanding of the causative factors that drive cross-bidding, or the contingent effects that shape this phenomenon. Thus the goal of our study was to address three research questions: (1) what factors influence cross-bidding, (2) what are the outcomes of cross-bidding, and (3) what contingent factors affect cross-bidding?

We formulated a set of hypotheses, and then tested them using live data derived from auctions of Apple iPod music and video players at eBay.

## 2. Prior research

Research on online auctions started when auction sites such as eBay emerged as a mechanism for trading goods and services over the Internet. While research on offline auctions was predominantly game-theoretic in nature, with Bayesian–Nash equilibrium being the solution space, research on online auctions has tended to be empirical in nature as the game-theoretic assumptions were not adequately generalizable to the Internet [4].

## 2.1. Sequential online auctions

Much of the initial research focused on sequential auctions studying a single auction selling a single item in a market with multiple bidders. These studies centered around three themes: auction design (investigating ways to increase the market efficiency or decreasing the sellers’ surplus by setting secret reserve prices, manipulating the optimal bid increment, and designing alternative auction formats [13]), price determination (examining potential relationships between auction closing prices and seller, bidder, and/or listing characteristics, such as seller feedback ratings [7], auction design, and informativeness of listings [8]), and bidding strategies (exploring the efficacy of alternative strategies with respect to their timing and frequency).

There are several different bidding strategies. We considered only standard auctions where the latest bid price is known and always rises – they are based on a private value concept, where the bidder has decided on an undisclosed, predetermined, maximum price he or she is willing to pay for an item. In a common value auction, the bidder continuously updates his or her bid based on cues from other bidders. The other major strategy is to give the maximum bid to a proxy bidder who acts as a surrogate by incrementally increasing the bid up to the maximum whenever the current bid is exceeded by a competitor. Roth and Ockenfels [12] considered a third bidding strategy that they called ‘‘sniping’’, where bidders attempt to win by bidding only during the last few seconds of an online auction which has a stated closing time, thus attempting to avoid a bidding war. Among other studies, Bapna et al. [5] identified five different types of bidders in online Yankee auctions: early evaluators, middle evaluators, opportunists, sipand-dippers, and participators; and showed that different bidders tend to use different or a combination of bidding strategies.

## 2.2. Simultaneous online auctions

A later stream examined simultaneous auctions, including multiple-item simultaneous auctions and single-item simultaneous auctions. In multiple-item simultaneous auctions, sellers list multiple units of the same product in a single auction, bidders specify both the price and quantity of items they desire, and winning auctions are determined based on price first, and then on quantity of items bid. This type of auction is popular among corporate sellers interested in liquidating excess inventory. Research on such auctions has compared their efficiency and design criteria with their offline counterparts [3], and examined the design and rules of these auctions. One extension of this type of auction is a combinatorial auction, where items of different types are bundled and auctioned together (e.g., a holiday package consisting of airfare, hotel, and car rental), with the expectation that these items will be worth more as a bundle than if sold separately. Research on such auctions has explored alternative designs that could increase market efficiency and maximize sellers’ revenue [11].

A smaller and more recent stream of simultaneous auction research involved single-item simultaneous auctions (referred to as simultaneous auctions), where multiple auctions sell single units of a product at the same time. This is often a consequence of: (1) a large seller base selling identical products of popular products (e.g., iPods) in auctions that are temporally overlapping each other, and (2) software tools that enable bulk listing and simultaneous management of such auctions (e.g., eBay’s TurboLister). Research in this area has assumed that some bidders are able to monitor overlapping single-unit auctions and move costlessly between them. Peters and Severinov proposed a design where bidders could move between simultaneous auctions based on the current standing bid in each auction, and concluded that simultaneous auctions increased market efficiency by matching supply with demand and led to a market characterized as a Bayesian equilibrium. They also proposed an optimal bidding strategy and reported that cross-bidding led to a uniform closing price for all simultaneous auctions in the market.

Anwar et al. examined the extent of cross-bidding and its outcomes, focusing specifically on auctions of computer hardware (CPUs). They found that only a small proportion (around 20%) was cross-bidders, and the closing prices for them were, on average, 9% lower than that for non-cross-bidders. This study is indicative of a recent emergence of interest in simultaneous single-item online auctions in general and the cross-bidding strategy in particular. Though this study provides some evidence of the growing prevalence of cross-bidding and its price effects, it does not address other salient issues such as cross-bidding’s antecedents and contingent factors that may shape the cross-bidding behavior and its outcomes. In the next section, we attempt to explore these issues by theorizing salient antecedents and consequents of crossbidding, along with contingent factors related to cross-bidding, for subsequent empirical testing.

## 3. Theory and hypotheses

## 3.1. Antecedents of cross-bidding

An essential requirement for cross-bidding is the simultaneous occurrence of multiple auctions of the same product ending at approximately the same time. The extent to which multiple auctions of the same product are simultaneously available is termed here as market liquidity. This is a market characteristic that is jointly determined by supply and demand forces in the auction market, rather than by the bidder or seller alone. Simultaneous auctions are a natural consequence of highly liquid markets, characterized by a high demand for the product in question, which motivates a large base of sellers to supply the product to the marketplace. Many of these products tend to be ‘‘hot’’ technology products with limited life spans which, if not liquidated within a short period of time, will be eventually replaced by newer generation products and hence become unsaleable. Examples of such products include central processing units for personal computers and Apple iPod music players, each of which have experienced a substantial amount of cross-bidding on online auction sites such as eBay. Listings of such highly liquid products from multiple sellers often lead to overlapping auctions at any given instant in time. This overlap creates the opportunity for cross-bidders to compare multiple auctions of the same product and move back and forth between these auctions with the goal of minimizing the price paid. This expectation leads to our first hypothesis:

H1. Market liquidity is positively related to greater cross-bidding activity.

Second, for a bidder to cross-bid between competing simultaneous auctions, that bidder must be able to continually monitor these auctions and the standing bids at each auction, and decide on which auction to bid and for what amount. At the same time, she must avoid multiple bids in different auctions at any given point in time, in order to avoid winning multiple items. This process must be managed continually until the end of all auctions. Unlike other popular bidding strategies, cross-bidders cannot place upfront proxy bids (their true private valuation for the desired product), because doing so could result in a higher closing price in one auction and defeat the cross-bidding strategy. Hence, crossbidding requires substantial information processing capability on the bidder’s part, and may not be well-suited for novice bidders. However, experienced bidders, by virtue of their experience with auctions and bidding strategies, are expected to better handle the cognitive overload associated with the cross-bidding strategy, and are more likely to engage in cross-bidding. Therefore, we propose the number of experienced bidders in a particular auction as the second determinant of cross-bidding activity, which is expected to have a positive association with cross-bidding. Note that the number of experienced bidders is an auction characteristic, rather than an individual (bidder) characteristic, because this construct examines the total number of experienced bidders in a given setting rather than the specific experience level of a given bidder. This leads to our second hypothesis:

H2. The number of experienced bidders is positively related to cross-bidding activity.

While market liquidity and number of experienced bidders are both purported to have positive effects on cross-bidding activity, these two independent variables may also interact to further enhance cross-bidding. More specifically, experienced bidders should have a stronger motivation to cross-bid in auctions of products characterized by higher market liquidities than those with lower market liquidities. In contrast, auctioned products with low market liquidities provide fewer choices for bidders in terms of moving back and forth between competing auctions, thereby reducing overall cross-bidding activity. Therefore, we propose a positive interaction between market liquidity and the number of experienced bidders on cross-bidding activity in online auctions:

H3. Market liquidity positively moderates the relationship between the number of experienced bidders and cross-bidding activity.

## 3.2. Outcomes of cross-bidding

Given that cross-bidding entails significant time and effort on the bidders’ part to monitor and move between online auctions, the natural question is what benefit, if any, can be realized from such activity? Cross-bidding tends to lower bidders’ final bid price by increasing their visibility of price information across multiple auctions of the same product, providing this bidder with a greater set of auctions to choose from and an opportunity to select the lowest priced auction among these auctions. Among prior empirical research, Anwar et al. showed that cross-bidders, who won CPU auctions on eBay, paid 9% lower closing prices than non-crossbidders, and McCart et al. [9] found that cross-bidders, who won iPod auctions on eBay, paid 4% lower closing prices than non-crossbidders. If price discount is measured as the difference between the closing price of one specific auction and the average closing prices of auctions of the same product on that day, cross-bidding should lead to larger price discounts. This leads to our fourth hypothesis:

H4. Cross-bidding leads to greater price discounts than non-crossbidding.

The presence of non-cross-bidders creates transient periods of information asymmetry about product availability and prices in the marketplace; cross-bidders can leverage this to their advantage by moving between auctions. If all bidders started crossbidding, then the informational advantage of cross-bidding would disappear, and all bidders would be worse off because they would have to process greater volumes of information without receiving any reward.

## 4. Research methods

## 4.1. Data collection

Empirical data from live eBay auctions were used to test our hypotheses. We collected data related to auction listing, sellers, and bidders on six models of Apple iPod audio/video player {Shuffle, Nano (2, 4, and 8 GB)} and video iPods (30 and 80 GB) over a 4-month period during late 2006 and early 2007. Our selection of these products was motivated by the fact that iPod was one of the most popular items on eBay at that time. High demand attracted many sellers, which translated into thousands of listings, and, in many cases, simultaneous listings. Hence, our sample fit well to our needs. Furthermore, the large supply of iPod auctions improved market liquidity, making them less susceptible to artificial price manipulation.

We used a Java program that searched listings on eBay using the keyword ‘‘iPod’’. To ensure product comparability across auctions; we excluded iPod listings that were bundled with accessories or those that were used or refurbished. Our Java program downloaded the unique listing number; title; start date; and end date of each iPod listing into a database on a daily basis. After the auctions ended; the program accessed each auction page using its listing number; downloaded all bid and bidder information for that listing; parsed the text and populated database fields such as bidder names; amounts of bids; and closing prices.

Our sample database consisted of detailed information on 23,919 iPod auction listings over the 4-month course of our study. Among these auctions, 2205 were unsuccessful in that they failed to attract a single bid (e.g., due to high initial starting price) or did not meet their secret reserve price. Of the remaining 21,714 auctions, several auctions listed refurbished, reconditioned, and used iPods as well as iPods that were bundled with accessories, gift cards, and various other products. Although our Java program filtered out most of these, our sample still included auctions that had inaccurate product descriptions. Additional manual cleaning removed used, refurbished, or bundled iPods, eliminating 8330 more auctions from our data set, leaving us with a final sample of 13,384 auctions.

To identify simultaneous auctions, for each auction in our data set, we examined a 10-min time window, from 5 min before the scheduled closing time of that auction to 5 min after. Any other auction that ended within this 10-min window was considered to be simultaneous with the original.

Our use of a 10-min window was motivated by several considerations. First, we needed auctions that ended in close proximity to one another, to allow for cross-bidders to move back and forth between auctions. Second, Roth and Ockenfels reported that most bidding activity in online auctions tended to occur toward their end (within their last 5 min), and thus a 10-min window was deemed appropriate. Third, we examined different time windows ranging from 4 min to 30 min and found that the 10- min window was not significantly different from other time windows for studying cross-bidding.

Using the 10-min window approach, we identified 7082 auctions (out of 13,384) that were not simultaneous with any other auction in our data set. We grouped the remaining 6302 auctions (simultaneous) using the 10-min window, and identified 3150 sets of auctions. Each auction set had two or more simultaneous auctions, within which cross-bidding could occur. The distribution of auction sets by iPod category, along with the total number of auctions in each set, is shown in Table 1.

## 4.2. Measurement of variables

Market liquidity. Market liquidity was defined as the number of simultaneous auctions available to a bidder for employing the cross-bidding strategy. This was measured as the total number of simultaneous iPod auctions within an auction set, i.e., a count of auctions ending within the same 10-min window of closing.

Number of experienced bidders. For each auction, we identified experienced bidders by using eBay’s bidder feedback scores, which were calculated as the arithmetic difference between the number of positive ratings and the number of negative ratings per eBay user. We set a threshold value for bidder experience at 10, so that bidders with feedback scores of 10 or more were considered experienced. Selecting this threshold reflected eBay’s views on experience of their client.

Table 1  
Distribution of all iPod auctions

<table><tr><td>Apple iPod model</td><td>Number of sets of auctions</td><td>Total number of auctions</td></tr><tr><td>Shuffle (1 GB)</td><td>257</td><td>593</td></tr><tr><td>Nano (2 GB)</td><td>570</td><td>1,105</td></tr><tr><td>Nano (4 GB)</td><td>1,460</td><td>2,872</td></tr><tr><td>Nano (8 GB)</td><td>158</td><td>335</td></tr><tr><td>Video (30 GB)</td><td>490</td><td>931</td></tr><tr><td>Video (80 GB)</td><td>215</td><td>466</td></tr><tr><td>Total</td><td>3,150</td><td>6,302</td></tr></table>

Cross-bidding activity. For each of the auctions, we measured cross-bidding activity as its number of cross-bidders. A given bidder was designated as a cross-bidder if he or she bid on at least two simultaneous auctions (ending within a 10-min window of each auction closing) of the same iPod category.

Price discount. Price discounts obtained by cross-bidders, our dependent variable of interest, were calculated as the difference between the daily average closing prices of auctions in that iPod category and the closing price of a given auction. We used the daily average price for this computation instead of the average iPod prices across our entire sample because iPod prices declined throughout the 4-month duration of our study and the average monthly prices for the first month were significantly higher than those for the last month. Our measure of price discount was similar to that of price premium that has been used extensively in economics and online auction literature [2]. Since different sellers charged different shipping fees, in order to ensure comparability across auctions and accurately capture the overall bidder cost for a given item, we included the shipping fees in our computation of price discount. In fact, we analyzed our data both with and without the shipping fees, and the results were not significantly different.

## 4.3. Control variables

We included product category as a control variable in our data analysis. Since our dataset spanned six different models of iPods (Shuffle; Nano – 2, 4, and 8 GB; and Video – 30 and 80 GB), it was possible that some of the variance in auction prices could be attributable to a particular model, particularly if all models were not equally attractive to bidders. Hence, an ordinal variable was created in increasing order of iPod model price (1 = Shuffle; 2 = Nano 2 GB; . . .; 6 = Video 80 GB).

## 5. Data analysis and results

Data analysis was conducted in two phases using multiple regression models. The first phase examined the antecedents of cross-bidding, as captured in Hypotheses H1–H3, while the second examined the outcomes of cross-bidding, as represented in

Hypothesis H4. Two separate models were required because the unit of analysis was different between the models; in the first our dependent variable was cross-bidding activity, hence the unit of analysis was an auction set, while in the second the dependent variable was price discount achieved by a winning cross-bidder (relative to a non-cross-bidder) in a given auction, and the unit of analysis was an individual auction.

## 5.1. Antecedents of cross-bidding

Model 1 (Hypotheses H1–H3) was tested using a multiple regression model with cross-bidding activity as the dependent variable, market liquidity and number of experienced bidders were the independent variables, along with an interaction term between market liquidity and number of experienced bidders; product category was the control variable.

Prior to hypotheses testing, we checked our dataset for potential outliers using a two-phase analysis. The first phase checked that the auctions sets consisted of auctions listing identical and comparable iPods. We computed the average closing price of each auction set and plotted the distribution against product category. Based on this plot, we found 37 auctions sets whose average closing price was outside three standard deviations of the mean closing price of their iPod category. A closer examination revealed that the auctions in these sets listed noncomparable products such as misclassified iPods, or those that were sold for very high prices, possibly due to shill-bidding in which auction sellers or their accomplices bid on the listing in order to drive up the auction bids. These 37 auction sets were dropped from our sample, reducing it to 3113.

In the second phase of our outlier analysis, we looked at the studentized residuals and Cook’s distances of each set by fitting a preliminary model to identify influential observations in our sample. Outliers are considered to be influential if they have a studentized residual greater than three or a Cook’s distance larger than one. We observed 54 such auction sets in our remaining sample; these had large numbers of simultaneous auctions, attracted a large number of bidders, and consequently resulted in competitive bidding. Since such circumstances are not uncommon in online auction markets, we decided to retain these observations.

The descriptive statistics of our sample are presented in Table 2. This shows that our sampled auction sets had a mean market liquidity measure of 3 (standard deviation = 2). This implied that, on average, three iPod auctions were running simultaneously at any given time. Each auction set had an average of 27 bidders, and a mean of 15 experienced bidders with a feedback score exceeding 10 (standard deviation = 8). Average cross-bidding activity in each auction was 3, suggesting that there were about three crossbidders per auction.

Next, we examined the bivariate correlations and variance inflation factors (VIF) to check for multicollinearity. Our initial analysis showed that the interaction term was highly correlated with the main effect variables. Since high correlations may bias beta estimates, we standardized the main effects variables to avoid multicollinearity. The correlation coefficients of the standardized main effects and the corresponding interaction term as well as the VIF values of each variable are shown in Table 3. Following standardization, the main effects and interaction term were still moderately correlated. However, the VIF values of all variables were less than 10, which is the commonly accepted threshold for multicollinearity. Since the VIF values were within the acceptable range, we proceeded with our analysis without further modification.

Table 2  
Descriptive statistics of 3113 set of auctions.

<table><tr><td>Apple iPod model</td><td>Number of sets</td><td>Number of auctions</td><td>Average market liquidity</td><td>Average number of bidders</td><td>Average number of experienced bidders</td><td>Average number of cross-bidding activity</td></tr><tr><td>Shuffle (1 GB)</td><td>252</td><td>572</td><td>3</td><td>20</td><td>13</td><td>2</td></tr><tr><td>Nano (2 GB)</td><td>567</td><td>1,094</td><td>3</td><td>22</td><td>12</td><td>1</td></tr><tr><td>Nano (4 GB)</td><td>1,441</td><td>2,836</td><td>3</td><td>32</td><td>17</td><td>3</td></tr><tr><td>Nano (8 GB)</td><td>155</td><td>291</td><td>2</td><td>24</td><td>14</td><td>3</td></tr><tr><td>Video (30 GB)</td><td>487</td><td>924</td><td>3</td><td>25</td><td>14</td><td>4</td></tr><tr><td>Video (80 GB)</td><td>211</td><td>463</td><td>3</td><td>22</td><td>12</td><td>2</td></tr><tr><td>All Models</td><td>3,113</td><td>6,103</td><td>3 (2)</td><td>27 (15)</td><td>15 (8)</td><td>3 (5)</td></tr></table>

Numbers in parentheses are standard deviations.

Table 4  
Correlation matrix for model 1.

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4VIF</td></tr><tr><td>1Market liquidity</td><td>1</td><td></td><td></td><td>2.97</td></tr><tr><td>2Number of experienced bidders</td><td>0.72***</td><td>1</td><td></td><td>2.15</td></tr><tr><td>3Market liquidity × number of experienced bidders</td><td>0.73***</td><td>0.60***</td><td>1</td><td>2.18</td></tr><tr><td>4Product category</td><td>0.02</td><td>-0.01</td><td>-0.001</td><td>1.00</td></tr></table>

\*\* $\begin{array} { r } { p < 0 . 0 0 1 . } \end{array}$

The results of the regression model for the antecedents of crossbidding are presented in Table 4. Model 1 was statistically significant and explained 55% of the variance in the dependent variable (adjusted R-square = 55%). The interaction term between market liquidity and number of experienced bidders was positively related to cross-bidding, providing empirical support for Hypothesis H3. However, this significant interaction effect rendered the main effects (Hypotheses H1 and H2) uninterpretable [6]. For instance, Hypotheses H1 stated that market liquidity had a direct impact on cross-bidding activity, when all other variables were held constant. However, Hypothesis H3 showed that the impact of market liquidity on cross-bidding activity depended on the number of experienced bidders, and hence ‘‘all other variables’’ (i.e., number of experienced bidders) could not be held constant. We therefore tested Hypotheses H1 and H2 indirectly by analyzing the marginal effects of market liquidity and number of experienced bidders on cross-bidding activity after accounting for the interaction between the two variables.

The analysis for two different levels of market liquidity is shown in Fig. 1. From this, we see that when market liquidity was two (i.e., for two simultaneous auctions), each additional experienced bidder translated into a 0.59 unit increase in cross-bidding activity between the simultaneous auctions. Also, when there were four simultaneous auctions, each additional experienced bidder translated into 1.09 unit of increase in the cross-bidding activity.

Finally, though not central to our hypotheses, the control variable, product category, had a significant positive effect on cross-bidding activity, indicating that more expensive products led to more cross-bidding activity. As a final step, we checked the assumptions of regression to see if the analysis suffered from non-normal residuals or heteroscedasticity. A visual inspection of the histogram of residuals showed that the residuals were normally distributed. Also, when we plotted residuals against predicted values, the output did not reveal any recognizable pattern, satisfying the equal variances assumption of multiple regression.

Multiple regression results for model 1.

<table><tr><td>Model</td><td>Cross-bidding activity =  $\beta_0 + \beta_1$  market liquidity +  $\beta_2$  number of experienced bidders +  $\beta_3$  (market liquidity × number of experienced bidders) +  $\beta_4$  product category</td></tr><tr><td>Global-F</td><td>946 (p&lt;0.0001)</td></tr><tr><td>Adj. R-square</td><td>55%</td></tr><tr><td>N</td><td>3,113</td></tr><tr><td>Variable</td><td>Beta estimate</td></tr><tr><td>Market liquidity</td><td>1.22***</td></tr><tr><td>Number of experienced bidders</td><td>0.09***</td></tr><tr><td>Market liquidity × number of experienced bidders</td><td>0.25***</td></tr><tr><td>Product category</td><td>0.40***</td></tr></table>

\*\*\* p < 0.001.

![](/api/attachments/J3RQQJ8X/fulltext/images/6ada10be0fbd51ce5e23414eefbf998e2fd4d6264651d3459cd12c436965a197.jpg)  
Fig. 1. Marginal effects on cross-bidding activity

## 5.2. Outcomes of cross-bidding

The outcome of cross-bidding (Hypothesis H4) was tested using an ANOVA by comparing the price discounts of cross-bidders versus non-cross-bidders. We used individual auctions (rather than auction sets) as the unit of analysis, and hence we had a sample of 6302 simultaneous auctions where cross-bidding could occur. To see if this data sample suffered from any outliers, we conducted a fresh outlier analysis by examining the price discounts realized in our sample of these auctions and identifying observations whose price discount was not within three standard deviations of the mean price discount. 67 observations were identified as having highly erratic price discounts. Further examination of these showed that they did not list products comparable to their counterparts, listed products that were different from what was advertised, or had questionable closing prices raising concerns of shilling. Hence, those auctions were dropped, reducing our sample to 6235 auctions.

Descriptive statistics of this sample are presented in Table 5. As seen from this table, the 6235 final iPod auctions in our sample attracted a total of 62,962 bidders, of which 9414 (15%) engaged in cross-bidding activity. However, only 310 of them (5%) were won by cross-bidders. The prevalence of non-cross-bidders in our sample presumably drove up the average closing price close to the retail prices of the iPod (see Table 5).

The results of an ANOVA comparing the price discounts of winning cross-bidders versus non-cross-bidders are presented in Table 6. The model was statistically significant, showing that the mean price discount of cross-bidders was statistically different from the mean price discount of non-cross-bidders. The comparison of the means showed that cross-bidders, on average, realized a \$3.11 price discount across all iPod models, while non-crossbidders, on average, paid \$0.16 more than the average closing prices.

As a follow-up, we conducted pairwise comparisons of the closing price of winning cross-bidders versus winning non-crossbidders for each iPod category. The results are presented in Table 7, showing that cross-bidders enjoyed higher price discounts than non-cross-bidders for all iPod categories except for the 80 GB Video iPods. Though cross-bidders paid slightly more than the average closing price of a typical 80 GB Video iPod on average than non-cross-bidders, this difference was not significant, and may be an artifact of the low sample size of winning cross-bidders in this category (N = 25) at the time of the study.

Table 5  
Descriptive statistics for the outcomes of cross-bidding.

<table><tr><td>Apple iPod model</td><td>Number of auctions</td><td>Total number of bidders</td><td>Total number of cross-bidders</td><td>Total number of winning cross-bidders</td><td>Mean closing price (S.D.)</td><td>Retail pricea</td></tr><tr><td>Shuffle (1 GB)</td><td>589</td><td>4,978</td><td>958</td><td>31</td><td>$81.51 (12.45)</td><td>$79</td></tr><tr><td>Nano (2 GB)</td><td>1,101</td><td>10,747</td><td>945</td><td>43</td><td>$150.62 (18.83)</td><td>$149</td></tr><tr><td>Nano (4 GB)</td><td>2,836</td><td>30,853</td><td>4,191</td><td>132</td><td>$191.96 (15.79)</td><td>$199</td></tr><tr><td>Nano (8 GB)</td><td>328</td><td>3,230</td><td>636</td><td>30</td><td>$225.28 (21.31)</td><td>$249</td></tr><tr><td>Video (30 GB)</td><td>921</td><td>8,890</td><td>1,804</td><td>49</td><td>$235.09 (19.85)</td><td>$249</td></tr><tr><td>Video (80 GB)</td><td>460</td><td>4,264</td><td>880</td><td>25</td><td>$324.70 (18.12)</td><td>$349</td></tr><tr><td>All models</td><td>6,235</td><td>62,962</td><td>9,414</td><td>310</td><td></td><td></td></tr></table>

<sup>a</sup> The retail price of the iPod at the time the study was conducted.

As a final step, we checked for the normality and homoscedasticity assumptions of ANOVA. The normality assumption was tested by plotting histograms of price discount within the crossbidder and non-cross-bidder groups. Price discount was found to be normally distributed within both histograms, satisfying the normality requirement of ANOVA. The homoscedasticity assumption was tested using Bartlett’s test, which found that the group variances were not significantly different (Chi-square = 0.72, p = 0.40), satisfying the equality of variance assumption.

## 6. Discussions and conclusions

## 6.1. Key findings

We found that cross-bidding behavior has two important determinants: (1) market liquidity, defined as the number of simultaneous auctions that are available to bidders at any given instant, and (2) number of experienced bidders. Apparently, as the number of simultaneous auctions increased, more bidders engaged in cross-bidding and this tendency increased with greater numbers of experienced bidders in the market. Experienced bidders are, of course, more likely to handle the cognitive overload imposed by cross-bidding.

ANOVA results for model 2.

<table><tr><td>Model</td><td colspan="2">Price discount =  $\beta_0 + \beta_1$  cross-bidding $^a$ </td></tr><tr><td>Global-F</td><td>14.17***</td><td></td></tr><tr><td>N</td><td>6,235</td><td></td></tr><tr><td></td><td>Cross-bidders</td><td>Non-cross-bidders</td></tr><tr><td>Sample size</td><td>310</td><td>5,925</td></tr><tr><td>Average price discount</td><td>$3.11</td><td>-$0.16</td></tr></table>

p < 0.001.  
<sup>a</sup> Coded as a dummy variable: 1 = cross-bidder; 0 = non-cross-bidder.

Price discount of each bidder type in each product category.

<table><tr><td>Apple iPod model</td><td>Cross-bidders</td><td>Non-cross-bidders</td><td>p-Value</td></tr><tr><td>Shuffle (1 GB)</td><td>$0.52</td><td>$0.03</td><td>0.72</td></tr><tr><td>Nano (2 GB)</td><td>$1.11</td><td>-$0.05</td><td>0.58</td></tr><tr><td>Nano (4 GB)</td><td>$4.64</td><td>-$0.23</td><td>&lt;0.001</td></tr><tr><td>Nano (8 GB)</td><td>$3.12</td><td>-$0.31</td><td>0.23</td></tr><tr><td>Video (30 GB)</td><td>$4.34</td><td>-$0.27</td><td>0.03</td></tr><tr><td>Video (80 GB)</td><td>-$1.71</td><td>$0.10</td><td>0.57</td></tr><tr><td>All models</td><td>$3.11</td><td>-$0.16</td><td>&lt;0.001</td></tr></table>

Our results were based on a 10 min time window. In order to assess the consequent generalizability of our findings, we conducted a sensitivity analysis, in which we ran the regression model for antecedents on data sets based on different time windows (i.e., 4, 6, 8, 10, 12, 14, 16, 18, 20, 30 min windows). The resulting analysis is shown in Fig. 2.

Here, all of the regression models were significant at an alpha level of 0.001. Also, the explanatory power of the models increased as the time window increased. This can be expected, as increasing the time window resulted in finding more simultaneous auctions, and thus explaining more cross-bidding activity between them. Although the beta coefficients of the regression variables looked stable across different time windows, one exception was the interaction term, which increased as the time window increased. This merely suggested that larger time windows induced more simultaneous auctions and more bidders at a point in time, which in turn fueled the amount of cross-bidding in the simultaneous auctions, reinforcing our hypotheses about the antecedents of cross-bidding.

We also observed that cross-bidders tended to realize greater price discounts than non-cross-bidders, by virtue of the former group’s greater knowledge of price information across simultaneous auctions of the same product, and their willingness to leverage this advantage by moving between the auctions. On the other hand, non-cross-bidders were more likely to be involved in a bidding war as they participated in only one auction.

As before, we conducted a sensitivity analysis for the outcomes of cross-bidding as well, in order to see if the results reported for 10-min window were different from other time windows. The corresponding analysis is presented in Fig. 3, which shows the results of ANOVA for each of the time window.

![](/api/attachments/J3RQQJ8X/fulltext/images/86a8aefd20e3a93b0ee6f5d9dda7a7835802eac9871c9cb75588de008a078ca5.jpg)  
ML: market liquidity; NEB: number of experienced bidders; CAT: product category (\*): All Global-F values are significant at p<0.001  
Fig. 2. Sensitivity analysis of antecedents.

![](/api/attachments/J3RQQJ8X/fulltext/images/a8fe9857860234c77a5b0dcaa81669f089135b0fb0c1aef1685ae89e1d835a22.jpg)  
Fig. 3. Sensitivity analysis of outcomes

The results show that cross-bidders’ price discount was higher than non-cross-bidders’ price discount for each time window $( p < 0 . 0 0 1 )$ ). The price discounts of cross-bidders were between \$3.25 and \$2.30, while the price discounts of non-cross-bidders were approximately \$0.20 for each time window; the price discounts of cross-bidders decreased as the time window increased. This finding could be expected; the ability of a crossbidder to move between simultaneous auctions is reduced when the auctions ended at different times.

We therefore validated bidder experience to be a salient determinant of cross-bidding, price discount to be an important outcome, and market liquidity tobea contingent variable influencing the antecedents. Market liquidity is a contingent variable (rather than an independent variable) because it is not endogenous to bidder or seller, but is an exogenous factor shaped by the supply and demand of a given product in the auction marketplace.

## 6.2. Limitations of the study

Since we employed data from live eBay auctions, we had no control over extraneous factors such as market fluctuations or irrational bidding that could skew our results. Second, we collected data regarding Apple iPod auctions only. This choice resulted in a large dataset, which was important since cross-bidding occurred in only 5% of our observed sample of simultaneous auction sets. However, our findings may not necessarily generalize to other products such as less technologically sophisticated products, or on otheronlineauctionssites.Third,weanalyzedcross-biddingthatwas observable, entailing placing successive bids in simultaneous auctions. If a bidder employed a ‘‘silent’’ cross-bidding strategy by only monitoring simultaneous auctions and placing a single last minute bid in one of them, we could not have identified this bidder as a cross-bidder, and may have misclassified him or her as a non-crossbidder. Identification and analysis of silent cross-bidders would require clickstream data for each bidder (i.e., the auction pages viewed by each bidder). Since our empirical data consisted solely of explicit cross-bidding behavior, our analysis might therefore have been an underestimate of the true extent of cross-bidding. Finally, anecdotal evidence suggests that eBay auction data tend to have a high degree of random error or noise, which makes it difficult to determine statistical inferences based on the data. It is possible that our results would have been different if we had been able to obtain ‘‘cleaner’’ data.

## 6.3. Implications in practice

Our study showed that cross-bidding tends to lower bidders winning prices. Although the price discounts here may seem relatively small, such discounts may be magnified for more expensive products, such as \$2000 notebook computers. Bidders may realize discounts even if they are bidding on simultaneous auctions that sell similar but non-identical products. As long as bidders do not exceed their valuation of the auctioned items, they may lower their cost of purchase by continuously switching between auctions and avoiding price wars in a single auction. However, cross-bidding is not suited for bidders lacking the motivation or ability to manage a high cognitive overload, and potential cross-bidders should carefully weigh the benefits and costs of cross-bidding before using this strategy.

Cross-bidding also has important implications for auction sellers. Since bidding is a zero-sum game, any price discounts accruing to cross-bidders translate into lost revenues for sellers in online auctions. Sellers should minimize the adverse consequences of cross-bidding by choosing auction times to minimize loss. Though sellers cannot entirely control bidder behavior, they may be able to minimize cross-bidding activity by minimizing the amount of overlap of their auction with others or by having different ending times. Likewise, they may be able reduce the impacts of cross-bidding by selling products, such as antiques, used merchandise, or one-of-a-kind products, that are less likely to attract simultaneous auctions.

However, a large seller base of a highly desired product will inevitably lead to overlap between auctions. Similarly, a large inventory of products that need to be sold quickly may lead to the use of bulk listing software resulting in many auctions with similar starting and ending times.

Finally, cross-bidding has implications for vendors of auction services; they may provide software-based tools to identify and monitor simultaneous auctions, and even allow for automated cross-bidding across a set of pre-identified simultaneous auctions. In doing so, they may help alleviate the cognitive overload faced by bidders in managing the cross-bidding strategy.

## 6.4. Implications for research

Given that our current understanding of online bidding strategies is based primarily on single-item sequential auctions, our study provided an illustrative example of how researchers can expand the body of knowledge. Our identification of some of the antecedents (e.g., bidder experience), consequents (e.g., price discounts), and contingent factors (e.g., market liquidity) related to cross-bidding provides a start for building a comprehensive theory of crossbidding. Finally, though not explicitly examined here, the crossbidding strategy may be limited by certain boundary conditions. For example, it may work if only a small portion of bidders, but not the entire population, cross-bid. If all bidders in the market monitor and bid on competing simultaneous auctions, the informational advantage held by cross-bidders is lost. If bidders employ a cross-bidding strategy in simultaneous auctions of non-identical (but similar) products, they may incur more cognitive load due to the variation in their valuation of the auctioned items.

## References

[1] S. Anwar, R. McMillan, M. Zheng, Bidding behavior in competing auctions: evidence from eBay, European Economic Review 50 (2), 2006, pp. 307–322.

[2] S. Ba, P.A. Pavlou, Evidence of the effect of trust building technology in electronic markets: price premiums and buyer behavior, MIS Quarterly 26 (3), 2002, pp 243-268

[3] R. Bapna, P. Goes, A. Gupta, A theoretical and empirical investigation of multi item online auctions, Information Technology and Management 1 (1), 2000, pp 1–23.

[4] R. Bapna, P. Goes, A. Gupta, Replicating online Yankee auctions to analyze auctioneers’ and bidders’ strategies, Information Systems Research 14 (3), 2003, pp. 244–268.

[5] R. Bapna, P. Goes, A. Gupta, Y. Jin, User heterogeneity and its impact on electronic auction market design: an empirical exploration, MIS Quarterly 28 (1), 2004, pp 21–43.

[6] T.A. Carte, C.R. Russell, In pursuit of moderation: nine common errors and their solutions, MIS Quarterly 27 (3), 2003, pp. 479–501.

[7] J.H. Gilkeson, K. Reynolds, Determinants of Internet auction success and closing price: an exploratory study, Psychology and Marketing 20 (6), 2003, pp. 537–566.

[8] O.B. Kwon, C.R. Kim, E.J. Lee, Impact of information design factors on consumer ratings of web based auction sites, Behaviour and Information Technology 21 (6), 2002, pp. 387–402.

[9] J.A. McCart, V.O. Kayhan, A. Bhattacherjee, Cross-bidding in Simultaneous Online Auctions: Bidder Characteristics and Outcomes, Communications of the ACM 52 (5), 2009, pp. 131–134.

[10] M. Peters, S. Severinov, Internet auctions with many traders, Journal of Economic Theory 130 (1), 2006, pp. 220–245.

[11] E.J. Pinker, A. Seidman, Y. Vakrat, Managing online auctions: current business and research issues, Management Science 49 (11), 2003, pp. 1457–1484.

[12] A.E. Roth, A. Ockenfels, Last-minute bidding and the rules for ending second-price auctions: evidence from eBay and Amazon auction on the Internet, The American Economic Review 92 (4), 2002, pp. 1093–1103.

[13] P.R. Wurman, M.P. Wellman, W.E. Walsh, A parametrization of the auction design space, Games and Economic Behavior 35, 2001, pp. 304–338.

![](/api/attachments/J3RQQJ8X/fulltext/images/68c42b72b9884be99ce4f4a7e1c2218869a153b526300b7d280c82d3b74b38fa.jpg)  
Varol O. Kayhan is an assistant professor of information systems at the University of South Florida – St. Petersburg. He earned a Ph.D. in Business Administration from the University of South Florida in 2010. Varol’s research interests include governance of knowledge in electronic repositories, healthcare informatics, and online auctions. His research has been published in the Communications of the ACM, Journal of Computer Information Systems, Healthcare Management Science, and Information Systems Management.

![](/api/attachments/J3RQQJ8X/fulltext/images/f1b0b0851e8bd6ce1b305e87047162c35228d26eec6a6a53aac90d68466ba9aa.jpg)

![](/api/attachments/J3RQQJ8X/fulltext/images/9afd065140169a067942ffa03928a883783029392a9e34378d2f0642f23b881b.jpg)

James A. McCart is a health science specialist at the James A. Haley Veterans Hospital, HSR&D/RR&D Center of Excellence: Maximizing Rehabilitation Outcomes. He received his Ph.D. in Business Administration from the University of South Florida. His research interests are in the area of Web behavior and healthcare informatics. His research has been published in such journals as the Communications of the ACM and the Journal of Computer Information Systems.

Anol Bhattacherjee is a tenured professor of information systems and the Citigroup/Hidden River Fellow at the University of South Florida. He received his Ph.D. and MBA degrees from the University of Houston and M.S. and B.S. degrees from the Indian Institute of Technology. His research interests include post-adoptive usage of information technology, knowledge creation/transfer in social networks, and medical informatics. Anol has published 46 refereed journal articles that have received over 2000 citations in Google Scholar. His research has been published in MIS Quarterly (five times), Information Systems Research,

Journal of MIS (four times), Decision Sciences, European Journal of Information Systems Decision Support Systems, IEEE Transactions, and Data Base, and Information & Management (three times), among other journals. Anol has also served on the editorial board of MIS Quarterly for 4 years.
