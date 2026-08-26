---
otero_id: 9000
otero_key: "9J343XTA"
title: "Price formation and its dynamics in online auctions"
authors: "Ravi Bapna; Wolfgang Jank; Galit Shmueli"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.09.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Price formation and its dynamics in online auctions

Ravi Bapna <sup>a</sup>, Wolfgang Jank <sup>b,⁎</sup>, Galit Shmueli <sup>b,1</sup>

<sup>a</sup> Indian School of Business, Gachibowli, Hyderabad, India

<sup>b</sup> Decision & Information Technologies Department, Robert H. Smith School of Business, University of Maryland, College Park, United States

Received 14 June 2006; received in revised form 11 September 2007; accepted 20 September 2007 Available online 29 September 2007

## Abstract

This research uses functional data modeling to study the price formation process in online auctions. It conceptualizes the price evolution and its first and second derivatives (velocity and acceleration respectively) as the primary objects of interest. Together these three functional objects permit us to talk about the dynamics of an auction, and how the influence of different factors vary throughout the auction. For instance, we find that the incremental impact of an additional bidder's arrival on the rate of price increase is smaller towards the end of the auction. Our analysis suggests that “stakes” do matter and that the rate of price increase is faster for more expensive items, especially at the start and the end of an auction. We observe that higher seller ratings (which correlate with experience) positively influence the price dynamics, but the effect is weaker in auctions with longer durations. Interestingly, we find that the price level is negatively related to auction duration when the seller has low rating whereas in auctions with high-rated sellers longer auctions achieve higher price levels throughout the auction, and especially at the start and end. Our methodological contributions include the introduction of functional data analysis as a useful toolkit for exploring the structural characteristics of electronic markets.

© 2007 Elsevier B.V. All rights reserved.

Keywords: Functional regression analysis; Data smoothing; eBay; Online auction; Auction dynamics; Electronic commerce

## 1. Introduction and background

Auctions have long served as operationally simple mechanisms that coordinate privately held information quickly and accurately to achieve efficient exchange. In doing so, they play a critical role in informing us about the underlying price formation process. Nowhere is this more evident than on eBay, perhaps the world's largest online auction house, where over to a billion items were listed for sale in 2006. The focus of this research is to shed new light on the dynamics of the price formation process of online auctions on eBay. We depart from extant online auction research by conceptualizing the auction price evolution and its first and second derivatives (signifying price velocity and acceleration respectively) as our primary objects of interest. By price velocity we mean the speed of the price increase and similarly by price acceleration we mean the rate at which this speed changes<sup>2</sup>.

There is a growing amount of evidence that dynamics matter in the online environment and that the study thereof can have significant benefits for all parties involved in an online transaction. [12] study eBay auctions and find that price dynamics can be very heterogeneous, even for auctions of the same product. Similarly, [20] study the heterogeneity of dynamics in auctions for modern Indian art. [25] use price dynamics to create real-time forecasting models for ongoing auctions and find that these dynamic models significantly outperform models that use only static information. [11] develop visualizations for the price formation process and its dynamics to study the effect of concurrency among online auctions. Dynamics also matter outside the auction environment. [23] for instance investigate the evolution of open source software projects using dynamic models. An overview of recent advances in dynamic modeling for electronic markets can be found in [13].

Commencing primarily after the seminal piece by [24], the extensive auction theory literature has limited its attention to explanatory power of the static auction price measure. Using online auction price information, researchers have investigated the revenue equivalence across auction formats [16], the impact of mechanism design choices made by sellers [2], the determinants of price [17], consumer surplus levels [6] and the magnitude of reputation premiums (see [8,1]) , ba:pavl:2002. The interested reader is referred to a recent exhaustive survey of online auction research by [3]. In this paper, we emphasize the importance of understanding and exploring the means to the end of getting to the price, namely the price formation process.

We achieve our goal by leveraging some of the most recent statistical methodological advances in functional data modeling that allow for input and/or output variables to be functional objects. The functional data modeling toolkit that we present permits us to study determinants of an auction's price formation by estimating time varying functional relationships (as opposed to scalar betas) that relate the auction's price formation process to its explanatory factors. Thus, we obtain insights into how the magnitude and significance of an effect, (e.g., the seller's rating), varies as an auction progresses.

Based on prior research, we limit our attention to five sets of explanatory variables and their interactions. To the best of our knowledge, prior applications of functional data modeling with a functional response have not studied interactions between explanatory variables. Yet, auction theory [3,6] informs us that such interactions do play a role in influencing an auction's closing price, and hence can be expected to influence the price formation. Our five sets of explanatory variables include product characteristics, and seller and bidder characteristics as measured by their eBay ratings. They also include seller mechanism design choices, namely the starting price level, the auction duration and the usage of a hidden reserve. Interestingly, our data (described further in Section 4) consist of auctions in three major currencies, namely US Dollar, Great Britain Pound and the Euro. This allows us to examine differences between the US and European markets as well as product item category effects. We elaborate on each of these in Section 3.

We believe that understanding the drivers of an auction's price formation, its velocity and its acceleration is a critical first step towards being able to pursue dynamic mechanism design in the online auction environment. [5] point out that a largely unconsidered aspect of the online auction environment is how the technologically-enhanced information gathering and processing capabilities might be used to perform realtime auction calibration. For instance, given that acceleration leads to change in velocity, which in our context subsequently impacts the price evolution, it is worth considering the impact that dynamic bid increments, designed to nudge a given auction towards a desirable trajectory, would have on an auction's price evolution and on bidding behavior. In this research, we attempt to begin this dialogue by developing a methodological toolset that allows us to understand what factors influence the dynamics of online auctions' price formation.

In the next Section we introduce the methodological toolkit necessary for investigating the dynamic price formation process. This toolkit relies heavily on ideas from what is often referred to as “Functional Data Analysis”.

## 2. Functional models for online auctions

Functional data analysis models are becoming increasingly popular, in particular in statistics and related disciplines. Functional models distinguish themselves from traditional statistical models in that the input and/or the output variables (i.e., x and/or y) can be a functional object rather than simply a data vector. The process of functional auction modeling begins by representing the price path in a single auction by a continuous curve. After the underlying curve is estimated, or “recovered”, we model the relationship between the price path and suitable predictor variables using functional regression modeling. An overview of the functional data analysis process is given in Fig. 1.

## 2.1. Recovering the functional object and data smoothing

There exist a variety of methods for recovering an underlying functional object from a set of data, and these methods are often referred to as data smoothing. Here, we focus on one particular method that provides good flexibility for 1-dimensional smoothing problems: the polynomial smoothing spline.

Consider a polynomial spline of degree $p \mathrm { : }$

$$
\begin{array}{l} f (t) = \widetilde {\beta_ {0}} + \widetilde {\beta_ {1}} t + \widetilde {\beta_ {2}} t ^ {2} + \dots + \widetilde {\beta_ {p}} t ^ {p} \\ \qquad + \sum_ {l = 1} ^ {L} \widetilde {\beta_ {p l}} \big [ (t - \tau l) _ {+} \big ] ^ {p}, \end{array}\tag{1}
$$

where the constants $\tau _ { 1 } , . . . , \tau _ { L }$ are a set of L knots and $u _ { + } = u I _ { [ u } \ge 0 ]$ denotes the positive part of the function u. The choices of L and p strongly influence the local variability of the function f, with larger values resulting in a rougher $\cdot f ,$ exhibiting larger deviation from a straight line. While this may result in a very good data fit, a locally very variable function may not recover or identify the underlying trend very well. One can measure the degree of departure from a straight line by defining a roughness penalty $\mathrm { P E N } _ { m } { = } \int \{ D ^ { m } \bar { f } ( t ) \} ^ { 2 } \mathrm { d } t ,$ where $D ^ { m } f , m { = } 1 , 2 , 3 , . . . ,$ denotes the mth derivative of the function f. For $m = 2$ , for instance, PEN yields the integrated squared second derivative of f which is sensitive to the curvature of the function $f .$

![](/api/attachments/9J343XTA/fulltext/images/f9feb83ed5ef605b37996beeca694e6bc0fab1979a2554db3a4fe3074da0aa10.jpg)  
Fig. 1. Flowchart of the FDA process.

Fitting a polynomial smoothing spline to the observed data $\widetilde { y } _ { 1 } , . . . , \widetilde { y } _ { \underline { { { \mathrm n } } } }$ involves finding the coefficients $( \widetilde { \beta } _ { 0 } , \widetilde { \beta } _ { 1 } , \dots , \widetilde { \beta } _ { p } , \widetilde { \beta } _ { p 1 } , \dots \widetilde { \beta } _ { p L } ) ^ { T }$ of Eq. (1) that minimize the penalized residual sum of squares

$$
Q _ {\lambda , m} = \lambda \times \mathrm{PEN} _ {m} + \sum_ {t = 1} ^ {n} \left\{\widetilde {y} _ {i} - f (t _ {i}) \right\} ^ {2},\tag{2}
$$

where the smoothing parameter $\lambda \geq 0$ controls the tradeoff between the data-fit, as measured by the summation on the right-hand side of Eq. (2), and the local variability of the function $f ,$ measured by the roughness penalty $\mathrm { P E N } _ { m }$ . Minimization of the penalized residual sum of squares Eq. (2) is done in a way very similar to the minimization of the least squares operator in standard regression analysis (see Appendix A for more details).

Smoothing splines are a flexible and computational efficient way to represent complicated relationships among data. Moreover, they allow for a convenient estimation of the curve's derivatives. Consider Fig. 2 for illustration. Suppose an auction receives a total of n bids<sup>3</sup>. Let $\widetilde { y } _ { 1 } , . . . , \widetilde { y } _ { n }$ denote the values of these n bids and let $t _ { 1 } , . . . , t _ { n }$ denote the times when these bids were placed. For a 7-day auction, for instance, the $t _ { i } ^ { \prime } \mathrm { s }$ will be values in the interval [0,6]. The circles in the top panel of Fig. 2 correspond to the scatterplot of the log-bid values, log (y<sup>\~</sup> ), versus the times $\mathrm { t _ { i } } ^ { 4 }$ . The continuous curve in that top panel shows a smoothing spline of order $m { = } 4$ using a smoothing parameter λ = 50.

Functional auction modeling now proceeds as follows. Similar to Fig. 2, we estimate a smoothing spline for each individual auction. This will be our price evolution. Let $f _ { j } ( t )$ denote the smoothing spline pertaining to the jth auction. In subsequent analyses, f (t) is used in place of the original data $\widetilde { y } _ { 1 } , . . . , \widetilde { y } _ { n }$

![](/api/attachments/9J343XTA/fulltext/images/f96e934b7a7c26d81d03279939b79920b2af3815dd6d942becf9bf3de50fac50.jpg)

![](/api/attachments/9J343XTA/fulltext/images/9bb885b741dd67c9aafff09867c20adf05ed8e0ee4c078eed217cf864c2df867.jpg)

![](/api/attachments/9J343XTA/fulltext/images/4df19ce89821ef5cd972269cd6abb06d3c067633926226fdc762ba3a852136f0.jpg)  
Fig. 2. Current price, price velocity (first derivative) and price acceleration (second derivative) for a selected auction. The first graph shows the actual bids (or WTP values) together with the fitted curve.

## 2.2. Curve derivatives and auction dynamics

One of our modeling goals is to capture the dynamics of an auction. While the smoothing spline f(t) describes the magnitude of the current price, it does not reveal the dynamics of how fast the price is changing or moving. Attributes that we typically associate with a moving object are its velocity (or its speed) as well as its acceleration. Note that we can compute the price velocity and price acceleration via the first and second derivative, $f ^ { \prime } ( t )$ and $f ^ { \prime \prime } ( t )$ , of the smoothing spline f (t), respectively.

Consider again Fig. 2 for illustration. The middle panel corresponds to the price velocity $\left( f ^ { \prime } ( t ) \right)$ or the first derivative of the smoothing spline $f ( t )$ . Similarly, the bottom panel shows the price acceleration $( f ^ { \prime \prime } ( t ) )$ . The price velocity has several interesting features. First, note that it starts out at a relatively high mark, at a value of about 0.2. The reason for this is a relatively high starting price which was set at \$72 for this item. On a logscale, this corresponds to a value of $1 0 \mathrm { g } ( 7 2 ) \approx 4 . 2 8$ Thus, the first incoming bid has to overcome this mark. Indeed, the first bid arrives only about 3 h after the opening of the auction and has a value of log(73)≈4.29. This bid corresponds to a significant “instantaneous jump” from zero and the price velocity captures this jump and translates it into a high initial speed.

After the initial high speed, the price increase slows down over the next several days, reaching a value close to zero mid-way through the auction. A close-to-zero price velocity means that the price-increase is extremely slow. In fact, between the end of day 3 and the end of day 4 (i.e. between bid #5 and bid #6 in Fig. 2) the increase in log-price equals 0.01 (=4.58–4.57). This corresponds to an increase of the price by only \$1! This is in stark contrast with the price-increase on the last day where the log-price increases by $0 . 3 6 ~ ( = 4 . 9 7 { - 4 . 6 1 } )$ ), or nearly \$44!

The bottom panel in Fig. 2 represents the priceacceleration. We can see that price acceleration is increasing over the entire auction duration. This implies that the auction is constantly experiencing forces that increase its price velocity. For instance, while 6 bids arrive in the first half of the auction, 9 bids arrive in the second half. With every new bid, the auction experiences new forces. The magnitude of the force depends on the size of the price-increment. Smaller price-increments will result in a smaller force. On the other hand, a large number of small consecutive price-increments will result in a large force. For instance, the last 8 bids in Fig. 2 all arrive during the last day of the auction. While the increment of each of the 8 individual bids is relatively small, they have a large combined effect on the auction, causing the price acceleration to increase by over 45%, from .11 to .16. As pointed out above, this translates to a steep price increase of \$44.

## 2.3. The functional regression model

One of the goals of statistical modeling is to study the change of a response variable in reaction to changes in explanatory variables. In traditional statistical models, both the response variable and predictor variables have either scalar or vector values, representing univariate or multivariate data. In functional modeling, however, these variables may be more general, functional objects. In the context of auction modeling, the response variable is the price evolution $f ( t )$ that describes the process of the price-progress over time. Explanatory variables are auction characteristics like the starting price, the product category, a seller's rating, or a bidder's rating. The functional approach allows that, in addition to the price path, we can also model the price dynamics. Such a model enables us to study those factors that influence the price velocity $f ^ { \prime } ( t )$ and the price acceleration $f ^ { \prime \prime } ( t )$ and subsequently leads to a better understanding of the price formation process.

We first describe the general functional regression model and its estimation process. We use vector notation similar to that of ordinary least squares. Let $\mathbf { Y } ( t ) { = } ( y _ { 1 } ( t )$ 4 $y _ { 2 } ( t ) , . . . , y _ { J } ( t ) )$ be ${ \bf { a } } J \times 1$ vector of functional objects where J denotes the total number of auctions. For instance, if we model the current price, then we set $y _ { j } ( t ) { = } f _ { J } ( t )$ . On the other hand, if want to find a model for the price velocity, we set $y _ { i } ( t ) { = } f _ { i } ^ { \prime } ( t )$ , and so on. Let $\mathbf { Z }$ denote the $J { \times } \left( q { + } 1 \right)$ design matrix,

$$
\mathbf {Z} = \left( \begin{array}{c} 1, z _ {1 1}, \ldots , z _ {1 q} \\ \vdots \\ 1, z _ {J 1}, \ldots , z _ {J q}. \end{array} \right)\tag{3}
$$

For instance, if the first covariate is the starting price of the auction, then we set $Z _ { j 1 } = s t a r t i n g \ p r i c e \ f o r$ auction number j. If the second covariate is the seller's rating then we set $Z _ { j 2 } = s e l l e r r a t i n g f o r$ auction number $j ,$ and so forth. While the model formulation so far strongly resembles ordinary least squares, one of the main differences is that we use parameter curves rather than parameter vectors. Define a q-vector of parameter curves $\beta ( t ) = ( \beta _ { 0 } ( t ) , \beta _ { 1 } ( t ) , \beta _ { 2 } ( t ) , . . . , \beta _ { q } ( t ) )$ At every time point $t , \beta _ { 1 } ( t )$ measures the influence of the first covariate on the average response curve $y ( t )$ . For instance if we set $y ( t ) { = } f ^ { \prime } ( t )$ in order to model the bid acceleration (where t is the day of the auction, and $\beta _ { 1 } ( t )$ denotes the parameter curve corresponding to the starting price), then $\beta _ { 1 } ( 2 )$ measures the average unit change in the price acceleration for a unit increase in the starting price on the second day of the auction (holding all other factors constant). Similarly, $\beta _ { 1 } ( 6 )$ measures this unit change on the sixth day of the auction. Thus, the flexibility of the functional approach stems from the fact that functional regression models capture the change of the covariates influence on the response over time. This is in contrast to traditional models where the parameters remain constant. These varying-parameter models are very useful in the online auction context since the relationship between, say, the starting price and the current price can be expected to change over the course of the auction.

![](/api/attachments/9J343XTA/fulltext/images/db00610a4b902089d4db1c9f2d714f3a5f9caa1a28e2cd1446055dafb3861ec1.jpg)  
Fig. 3. The current average bidder rating over a 7-day auction. The first bidder has a rating of 116 (leftmost circle). The second bidder rates at 105 which results in an average rating of $( 1 1 6 + 1 0 5 ) / 2 = 1 1 0 . 5$ (second leftmost circle). In order to arrive at a continuous representation, we linearly interpolate (solid line).

While the functional regression model allows for a better understanding of the change in the price formation process (and its dynamics), it also allows for new insight into the factors that lead to that change. Consider variables like the bidder rating or the number of bidders. Both of these variables are dynamic. That is, they differ from static variables like the starting price or the seller's rating in that the information changes with every new incoming bid. Consider Fig. 3 which shows the current average bidder rating for some auction. Functional regression models can account for the changing nature of variables by introducing dynamic covariates. Dynamic covariates can reveal additional insight into the bid formation process which would otherwise be lost.

Estimation of the parameter curves proceeds as follows. We attempt to find $\beta ( t )$ such that the expected value of $\mathbf Y ( t )$ equals $\mathbf { Z } \beta ( t )$ for each value of t. This problem can be written similar to the least squares minimization objective of ordinary regression. The objective function

$$
\operatorname{ISSE} (\beta) = \int | | \mathbf {Y} (t) - \mathbf {Z} \beta (t) | | ^ {2} d t\tag{4}
$$

defines the integrated error sum $o f$ squares (ISSE), where $\lvert \lvert \bullet \rvert \rvert$ denotes the Euclidian norm. The goal is to find $\beta ( t )$ that minimizes ISSE. [19] point out that since there is no particular restriction on the way in which $\beta ( t )$ varies as a function of t, one can minimize ISSE by minimizing $| | \mathbf { Y } ( t ) - \mathbf { Z } \boldsymbol { \beta } ( t ) ^ { 2 } \ | |$ on a suitable grid of values $t _ { 1 } , t _ { 2 } , . . . , t _ { n } .$ <sup>Þ - ð Þ jj</sup>This yields a sequence of parameter estimates $\hat { \beta } ( t _ { 1 } ) , \ldots , \hat { \beta } ( t _ { n } )$ . One then reconstructs the <sup>ð Þ ð Þ</sup>continuous parameter vector $\hat { \beta } ( t )$ by simply interpolating between the values $\hat { \beta } ( t _ { 1 } ) , \ldots , \hat { \beta } ( t _ { n } ) ^ { 5 }$

## 2.4. Interpretation of the estimated functional regression model

One of the challenges of functional regression modeling is the careful interpretation of the results.

Consider Fig. 4 for illustration. We see that the parameter curve for the starting price follows a decreasing, S-shaped path. This has several implications. Overall, the parameter curve is positive during the entire auction duration, indicating a positive relationship between the starting price and the current price. In other words, higher starting prices are associated with higher prices at any time during the auction. Note, however, that the parameter curve is at its peak at the auction start $( \hat { \beta } ( 0 ) \approx 0 . 6 2 )$ and then decreases towards day 7, implying that the strength of the relationship between the starting price and the current price is continuously weakening. At the auction end, the parameter estimate has decreased to a value of only $\hat { \beta } ( 7 ) \approx 0 . 4 3$ . The steep <sup>ð Þ</sup>decline in the coefficient towards the auction end implies that the information contained in the starting price loses its usefulness for explaining the auction price as the auction progresses. We will re-visit this interesting finding in the next Section.

## 3. Explanatory variable selection

We elaborate on five sets of explanatory variables, relying heavily on the online auction literature from Economics and Information Systems (IS).

a) Seller's mechanism design choices: sellers, who strive to maximize their revenues, can be expected to strategize on eBay by choosing the appropriate combination of starting price level, auction duration, and the usage of a hidden reserve price. Starting price can be interpreted as an open reserve price and prior research has contrasted the comparative effectiveness of open versus hidden reserve prices on sellers' expected revenue. [18] formulates the optimal (seller revenue maximizing) auction design problem as being equivalent to deriving the optimal open reserve price. [14] in a field experiment selling Pokemon cards, find that hidden (secret) reserve prices make sellers worse off, by reducing the probability of the auction resulting in a sale, deterring serious bidders from entering the auction, and lowering the expected transaction price of the auction. In contrast, [2], based on an econometric estimation, suggest that optimally chosen hidden reserve prices can yield the seller one percent higher revenues. Thus, the evidence seems mixed with respect to how the seller's usage of hidden reserve prices impacts the auction price. In this paper, we extend this line of enquiry to consider if and how starting price levels influence the price formation curve of an auction, its velocity and its acceleration. It is well established that, on eBay, lowering starting prices attracts more bidders [2,17]. In addition, prior research also suggests that when a seller chooses to have her auction last for a longer number of days, this significantly increases the average auction price [17].

![](/api/attachments/9J343XTA/fulltext/images/677a34142303afc48014cadf29e80ade517dc03a1dc4f7eacbc9f9a7638db36c.jpg)  
Fig. 4. The estimated parameter curve (solid line) for a functional regression model of the starting price on the price path (both on the log-scale). The dashed lines represent 95% confidence bounds.

b) Seller characteristics: eBay's feedback reputation system has been widely investigated and studies indicate that sellers with higher reputations engender trust and extract premiums [see [8], [1]]. It can also be argued that sellers with more experience, also proxied by feedback ratings, make better mechanism design choices to maximize expected auction price. Thus, while prior research has shown seller rating to have a positive influence on the final auction price, it is not known how the informational content of this explanatory variable gains, or loses, influence price as the auction progresses.

c) Product characteristics: in contrast to the abovementioned empirical studies on eBay [2,14,17] that controlled for product heterogeneity, our dataset is diverse, covering all but 2 of eBay's 30 major item categories, with prices ranging from 1 cent to about \$1000. This allows us to test the implications of stakes and product attributes on price formation in a far more generalizable setting. [22] have predicted that individuals' behavior will more closely match the predictions of rational behavior as the stakes of the decision increase. Marketing theories suggest that as stakes get higher, consumers get more involved in finding the best price for their product [7]. In addition, we pointed out earlier the strong connection between an auction's current price level and eBay's minimum required increment. Based on these studies, we expect the final auction price, which proxies for an item's value, to have a significant influence on the price formation process. With respect to item categories, issues such as condition of the good, bidder's confidence in the expressed condition of the good, the degree of expertise required in assessing the market value of the good, possibilities of easy resale in electronic markets, the value of private consumption of the good, as well as hedonic aspects of outbidding one's rivals confound any priors with respect to item-categorywise price formation. We will thus let the data speak.

d) Bidder characteristics: we collect information on a bidder's rating as a proxy for their experience on eBay. We expect more experienced bidders to have more confidence in their valuations and hence have a significant influence on the auction's price dynamics.

e) Market characteristics: we are fortunate to have significant data in three prominent currencies, namely US Dollar (USD), Great Britain Pound (GBP) and the Euro. This allows us to test, for the first time, whether price formation differs across geographical markets. While there has been prior research in looking at the efficiency of auction formats across different countries [15], this study represents a first in comparing the price formation processes across countries. Given that eBay was founded in the US and subsequently expanded to UK and Europe, it is reasonable to expect that the US market and its bidders have greater experience with bidding and strategizing. Lastly, as can be expected, we propose that the level of competition in an auction, reflected in the current number of bidders, positively influences the price dynamics, but it is not clear how this effect changes as the auction progresses. We also have data on the total number of bids in an auction. However, total number of bids is highly correlated with the total number of bidders and thus does not add any additional explanatory power to our regression models. Additionally, we examine the interaction between the current number of bidders and the starting price. We describe the number of competing bidders under market characteristics and examine its interaction with starting price. It is well established that, on eBay, lowering starting prices attracts more bidders [2,17]. Yet, we are not aware of any study to date that has examined the time sensitivity of this effect.

## 4. Empirical application and results

## 4.1. Data description

The data used in our analysis consist of a random sample of 1009 auctions that took place on one single day on eBay's auction page. To obtain this sample, we undertook a “title and description”; advanced search of eBay auctions using the phrase “May-13-04.” This returned approximately 10,000 eBay listings with this test string anywhere in the HTML text. Subsequently, after the last of these auctions closed, we obtained the auction information by parsing the HTML pages of only competitive auctions, that is those with at least two submitted bids<sup>6</sup>.

The auctions we considered were carried out in three different currencies, USD, GBP and the Euro. The items auctioned were across a wide variety of categories spanning all but 2 of eBay's 30 high level categories. In order to maintain a smaller cardinality level, we grouped the items into 17 major categories<sup>7</sup>. Only recently have currency and category become part of major eBay studies (see [6]).

For each of these auctions we collected the entire eBay bid-history. That is, for each bid in a particular auction we recorded the time when the bid was placed as well as the amount of the bid<sup>8</sup>. These bid-histories form the basis of our functional model: let $t _ { i }$ denotes the time (in days) of the ith bid and $\widetilde { y } _ { 1 }$ the corresponding bid amount. The smoothing spline from Section 1 is calibrated on the data $\widetilde { y } _ { 1 } , . . . , \widetilde { y } _ { n } ^ { \mathrm { ~ 9 ~ } }$

In addition to the bid-histories, we also collected information on the seller's and the bidders' characteristics, the product and the market characteristics. That is, we recorded the starting price and the duration of the auction, the seller's, bidders' and the winner's rating, the product price, the number of unique bidders and the number of bids placed. The top part of Table 1 shows summary statistics for these 8 variables. Finally, for each auction we recorded the monetary variables starting price, individual bids and final price in their original currency as well as in their USD equivalents<sup>10</sup>. For our subsequent analyses we used the USD equivalents for all three currencies. The bottom part in Table 1 shows the summary statistics broken up by currency.

Table 1  
Summary statistics for continuous variables

<table><tr><td></td><td>Mean</td><td>Median</td><td>Std.Dev.</td><td>Min</td><td>Max</td></tr><tr><td>OpeningBid</td><td>9.24</td><td>2.45</td><td>30.27</td><td>0.01</td><td>650.00</td></tr><tr><td>Price</td><td>51.70</td><td>15.45</td><td>112.06</td><td>0.06</td><td>971.00</td></tr><tr><td>NumberBids</td><td>7.22</td><td>6.00</td><td>5.91</td><td>2.00</td><td>50.00</td></tr><tr><td>NumberBidders</td><td>4.30</td><td>3.00</td><td>2.60</td><td>2.00</td><td>17.00</td></tr><tr><td>BidderRating</td><td>171.29</td><td>57.00</td><td>372.57</td><td>-1.00</td><td>7012.00</td></tr><tr><td>SellerRating</td><td>3424.69</td><td>1550.00</td><td>6334.25</td><td>0.00</td><td>37727.00</td></tr><tr><td>WinnerRating</td><td>157.09</td><td>49.00</td><td>328.60</td><td>-1.00</td><td>3959.00</td></tr><tr><td>DurationOfAuction</td><td>6.44</td><td>7.00</td><td>2.00</td><td>1.00</td><td>10.00</td></tr><tr><td colspan="6">Euro (n = 277)</td></tr><tr><td>OpeningBid</td><td>6.19</td><td>2.25</td><td>16.64</td><td>1.51</td><td>151.26</td></tr><tr><td>Price</td><td>61.18</td><td>23.44</td><td>132.90</td><td>2.26</td><td>1061.83</td></tr><tr><td>NumberBids</td><td>7.27</td><td>5.00</td><td>6.40</td><td>2.00</td><td>38.00</td></tr><tr><td>NumberBidders</td><td>4.33</td><td>3.00</td><td>2.79</td><td>2.00</td><td>17.00</td></tr><tr><td>BidderRating</td><td>171.36</td><td>54.00</td><td>362.82</td><td>-1.00</td><td>2858.00</td></tr><tr><td>SellerRating</td><td>1327.90</td><td>638.00</td><td>1633.23</td><td>1.00</td><td>6621.00</td></tr><tr><td>WinnerRating</td><td>125.09</td><td>46.00</td><td>242.51</td><td>-1.00</td><td>2598.00</td></tr><tr><td>DurationOfAuction</td><td>7.96</td><td>7.00</td><td>2.22</td><td>1.00</td><td>10.00</td></tr><tr><td colspan="6">GBP (n = 98)</td></tr><tr><td>OpeningBid</td><td>9.34</td><td>3.16</td><td>30.92</td><td>0.03</td><td>303.49</td></tr><tr><td>Price</td><td>43.93</td><td>16.30</td><td>93.42</td><td>1.75</td><td>606.97</td></tr><tr><td>NumberBids</td><td>6.42</td><td>5.00</td><td>4.51</td><td>2.00</td><td>21.00</td></tr><tr><td>NumberBidders</td><td>4.01</td><td>3.50</td><td>2.04</td><td>2.00</td><td>11.00</td></tr><tr><td>BidderRating</td><td>98.53</td><td>40.00</td><td>251.95</td><td>0.00</td><td>2375.00</td></tr><tr><td>SellerRating</td><td>757.38</td><td>119.50</td><td>1056.63</td><td>17.00</td><td>3380.00</td></tr><tr><td>WinnerRating</td><td>128.74</td><td>25.00</td><td>421.22</td><td>0.00</td><td>3959.00</td></tr><tr><td>DurationOfAuction</td><td>6.82</td><td>7.00</td><td>1.24</td><td>3.00</td><td>10.00</td></tr><tr><td colspan="6">US (n = 634)</td></tr><tr><td>OpeningBid</td><td>11.71</td><td>3.60</td><td>36.30</td><td>0.01</td><td>650.00</td></tr><tr><td>Price</td><td>56.75</td><td>15.50</td><td>119.78</td><td>0.06</td><td>971.00</td></tr><tr><td>NumberBids</td><td>7.32</td><td>6.00</td><td>5.87</td><td>2.00</td><td>50.00</td></tr><tr><td>NumberBidders</td><td>4.33</td><td>3.50</td><td>2.60</td><td>2.00</td><td>17.00</td></tr><tr><td>BidderRating</td><td>182.51</td><td>64.00</td><td>391.11</td><td>0.00</td><td>7012.00</td></tr><tr><td>SellerRating</td><td>4753.09</td><td>2349.00</td><td>7600.33</td><td>0.00</td><td>37727.00</td></tr><tr><td>WinnerRating</td><td>175.44</td><td>57.00</td><td>343.80</td><td>0.00</td><td>3094.00</td></tr><tr><td>DurationOfAuction</td><td>5.72</td><td>5.00</td><td>1.55</td><td>1.00</td><td>10.00</td></tr></table>

## 4.2. Covariate information

Using the notation from Section 2.3, we define the following regression covariates:

$Z _ { j 1 }$ (log) staring price for auction j

$Z _ { j 2 }$ (log) item's final price (or selling price) for auction j

$Z _ { j 3 }$ (log) seller reputation (+5) for auction j

$Z _ { j 4 }$ (log) current average bidder experience (+5) for auction j

$Z _ { j 5 }$ (log) current number of bidders for auction j

$Z _ { j 6 }$ a dummy variable indicating US currency in auction j

$Z _ { j 7 }$ a dummy variable indicating usage of secret reserve price in auction j $Z _ { j 8 }$ duration of auction j (in days) $Z _ { j 9 }$ a dummy variable for the product category type in auction j

A few comments are in order. The covariate $Z _ { j 1 }$ is simply the natural log of the starting price for auction $j .$ Similarly, $Z _ { j 2 }$ denotes the item final price<sup>11</sup> on the log scale. The covariate $Z _ { j 3 }$ denotes the log of the seller rating<sup>12</sup>. Since some sellers have negative ratings in the range $( - 4 , . . . , - 1 )$ , we add 5 to each seller's rating before taking logs, thus assuring that the log-transformation is well-defined.

We also include information on the bidder experience. As for the seller ratings, we compute the log of the average bidder rating after adding 5. However, note that in contrast to the seller rating, the average bidder rating does not remain constant throughout the auction. In fact, the average rating of currently participating bidders changes with every new incoming bid. We therefore use a dynamic covariate that takes this change into account. Using an evenly spaced grid of points across the auction duration, say $t _ { 1 , } t _ { 2 , \ldots } , t _ { n } ,$ the current mean bidder rating at $t _ { i }$ is calculated as the average rating of all bidders that participate at or before time $t _ { \mathrm { i } } .$ Taking logs, we denote this covariate by $Z _ { j 4 }$ . Thus, $Z _ { j 4 }$ measures the average experience level of currently participating bidders.

As with the mean bidder ratings, the number of bidders also changes with every new incoming bid. In order to measure the effect of the current number of bidders on the price formation, we create another dynamic covariate $Z _ { j 5 }$ . Using the same grid as above, $Z _ { j 5 }$ denotes the (log of) the total number of bidders that participate at or before $t _ { i } .$ In that sense, $Z _ { j 5 }$ measures the effect of the current competition level.

In order to capture the effect of currency on the auction outcome, we include a dummy variable, $Z _ { j 6 } ,$ which assumes the value one for auctions in US currency and the value zero for auctions in non-US currency (GBP or the Euro). Thus, $Z _ { j 6 }$ measures the geographical market differences in the bidding dynamics between the US and Europe. A similar dummy variable $( Z _ { j 7 } )$ is created for the secret reserve price which is set equal one if the seller uses this option.

Another important factor of price formation is auction duration measured by the covariate $Z _ { j 8 }$ . Most auctions on eBay range from 1 days to 10 days. In order to measure the effect of duration, auctions of different length have to be incorporated into the same functional regression model. Varying-length auctions result in varying-length smoothing splines f (t). In order to align splines of different length, we standardize auction duration into unit-time intervals. After this standardization, every auction has starting time 0 and ending time 1.

Only few other studies before consider a wide variety of product categories. Our data set comprises a total of 17 high-level eBay categories, summarized in Table 2. In order to study price differences due to different categories, model-parsimony suggests reducing this large number into smaller and more homogeneous groups. We accomplish this by curve-clustering.

The basic idea of curve-clustering is as follows (see 13, for more details). Cluster analysis is a multivariate method useful for finding natural segments or groupings within a large set of potentially high- but finitedimensional data. Cluster analysis is a standard exploratory tool and it has found many applications in marketing, finance or others. However, the problem that arises when attempting to generalize the method to the clustering of curves is that a continuous curve is of infinite dimension. Thus, the method cannot be applied directly. [12] overcome this problem by using a lowdimensional representation of the infinite-dimensional curve. Note that the spline-coefficients $\beta ~ = ~ ( \beta _ { 0 } , \beta _ { 1 }$ $. . . , \beta _ { p } , \beta _ { p 1 } , . . . , \beta _ { p L } ) ^ { T }$ determine the curve uniquely within the set of all splines of order m. Furthermore, the dimension of β is finite and typically rather low. Thus, rather than clustering the curve directly, we apply standard tools<sup>13</sup> to the set of spline coefficients.

Table 2  
Break-down of eBay categories

<table><tr><td colspan="2">Category</td></tr><tr><td>Antique/art</td><td>0.79%</td></tr><tr><td>Automotive</td><td>5.45%</td></tr><tr><td>Books</td><td>2.38%</td></tr><tr><td>Business/industrial</td><td>1.19%</td></tr><tr><td>Clothing/accessories</td><td>5.75%</td></tr><tr><td>Coins/stamps</td><td>0.99%</td></tr><tr><td>Collectibles</td><td>10.01%</td></tr><tr><td>Computing</td><td>2.28%</td></tr><tr><td>Consumer electronics</td><td>5.35%</td></tr><tr><td>Health/beauty</td><td>1.09%</td></tr><tr><td>Home/garden</td><td>6.94%</td></tr><tr><td>Jewelry</td><td>2.78%</td></tr><tr><td>Music/movies/games</td><td>23.09%</td></tr><tr><td>Pottery/glass</td><td>8.82%</td></tr><tr><td>Sports</td><td>11.40%</td></tr><tr><td>Tickets/travel</td><td>0.50%</td></tr><tr><td>Toys/hobbies</td><td>11.20%</td></tr><tr><td>Total</td><td>100.00%</td></tr></table>

Table 3  
2 Distinct clusters of eBay categories

<table><tr><td>Cocategory A</td><td>Category B</td></tr><tr><td>Collectibles</td><td>Computers</td></tr><tr><td>Toys &amp; Hobbies</td><td>Jewelry</td></tr><tr><td>Coins &amp; Stamps</td><td>Consumer Electronics</td></tr><tr><td>Books</td><td>Antiques</td></tr><tr><td>Sports</td><td>Clothing &amp; Accessories</td></tr><tr><td>Pottery &amp; Glass</td><td>Automotive</td></tr><tr><td>Music &amp; Movies &amp; Games</td><td></td></tr><tr><td>Travel &amp; Tickets</td><td></td></tr><tr><td>Home &amp; Garden</td><td></td></tr><tr><td>Health &amp; Beauty</td><td></td></tr><tr><td>Business &amp; Industrial</td><td></td></tr></table>

We apply curve-clustering in the following way. First, we calibrate the functional regression model using a dummy variable for each of the 17 different categories. This results in 17 different parameter curves, similar to Fig. 4, one for each of the categories. The goal is to group categories that exhibit similar dynamics. To that end, we use curve-clustering and join categories with similar parameter curves into the same group. This results in two distinct groups of item categories. Table 3 shows the membership for each of these two groups, denoted A and B. The dummy variable $Z _ { j 9 }$ assumes the value one for products in category B.

Our analysis also reveals significant interactions between several variables. While the usage of interaction terms is well understood in traditional statistics, there has been, to date, no application of the interaction-concept to the context of functional data analysis. Generalizing the interaction-concept to functional modeling is not straightforward, in part since its interpretation can be prohibitively complicated. The following results show that the functional interaction term proves very useful, especially in the auction setting.

## 4.3. Results

In the following we provide a detailed discussion of our results<sup>14</sup>.

![](/api/attachments/9J343XTA/fulltext/images/ae3b54f3303d014129457f2e5cb61a6b399b8af6d9bce3a40102df4ecfcad9a2.jpg)  
Fig. 5. Estimated parameter curves for starting price, secret reserve price and auction duration.

## 4.3.1. Seller's mechanism design choices — starting price, reserve and duration

Consider the left-most panel in Fig. 5 that shows the estimated parameter curves associated with the (log-) starting price. The top panel shows the parameter curve for a regression on the current price, f(t), while the middle and the bottom panels correspond to regressions on the price velocity $( f ^ { \prime } ( t ) )$ and price acceleration $( f ^ { \prime \prime } ( t ) )$

The parameter curve in the top graph is positive throughout the entire auction, starting at about 0.7 and ending just below 0.1. A positive parameter implies a positive relationship between the starting price and current price. Note that this relationship is statistically significant as indicated by the very tight confidence bounds (dashed lines) that remain above zero throughout<sup>15</sup>. The implication is that the higher the starting price, the higher the current price. However, although the parameter remains positive, it gradually declines in magnitude towards the auction end. The decreasing magnitude implies that the impact of the size of the starting price on the price formation process reduces throughout the auction. In other words, the information contained in the starting price loses its usefulness for explaining the current price. Consistent with auction theory, we observe that the starting price influences entry into the auction and has higher signaling value in the early stages of the price formation process. We know, for instance, that more experienced sellers make better mechanism design choices that attract a higher number of bidders [6]. This effect tends to lessen as the auction rounds progress and the competitive elements of the auction on hand take over. This also motivates us to consider the interaction between the number of bidders and the starting price, as described in Section 4.3.2.

The impact of the starting price on the price dynamics can be seen in the middle and bottom panels. The middle panel shows that the parameter curve associated with the price velocity is negative throughout the auction. This negative relationship means that higher starting prices result in slower price increases. The higher the starting price, the smaller the difference to an item's valuation. Bidders, unclear about the exact valuation, can be expected to place smaller increments above the starting price, resulting in lower auction dynamics and thus a slower price formation.

![](/api/attachments/9J343XTA/fulltext/images/f7b65e6cfe8b533ad77962664ee76da8585a87b30da33f6d4c5078f27b175015.jpg)

![](/api/attachments/9J343XTA/fulltext/images/b488cdab41c49d9a5a897ef75b42162d800a51b288cc00575e185a73909299b9.jpg)

Yet even more information about the price formation process can be extracted from the relationship between the starting price and the price acceleration in the bottom panel. It is most noteworthy that the parameter curve changes its sign from positive to negative about mid-way through the auction and decreases further to the end. The negative parameter estimate at the auction end implies that high starting prices are associated with a high negative price acceleration, or price deceleration. Put differently, auctions with high starting prices experience a slowdown in the price increase at the end of the auction and vice versa. This finding is interesting in light of the commonly encountered phenomenon of bid sniping.

![](/api/attachments/9J343XTA/fulltext/images/303181397eb340fc7ec05128d2864c2a0191c14e7a567debf3c2347907e7680d.jpg)

![](/api/attachments/9J343XTA/fulltext/images/8976e9d0481333c228be31a0bddee70089c7128223374eed9c2c80877f862259.jpg)

![](/api/attachments/9J343XTA/fulltext/images/b9a26fe93e8f88ec87e0fadab0aa2f8dbcc19ca06837e16de22958fb67bb70a4.jpg)

![](/api/attachments/9J343XTA/fulltext/images/91d383b4b26e0b3fe2d070d195cd98347b77e22d3ab34676f1a6e1c4a3466f7f.jpg)

![](/api/attachments/9J343XTA/fulltext/images/6bdc0d2fb7b67e45f4aae8e32c9bf4581096c09e9ddfb128db60751dd8d2f91a.jpg)

![](/api/attachments/9J343XTA/fulltext/images/3578c6e493f1cfda0ec95a1c6e608269c4544febbf3f8945f4e71105977e959f.jpg)

![](/api/attachments/9J343XTA/fulltext/images/7eda9be89979ee30e412e7a2f34604a83b619a45edbf1f2720f319af578557c5.jpg)

![](/api/attachments/9J343XTA/fulltext/images/02f13efdfdcd8f28a381b00e8a206db166a4d6f8d39e999373447ba747bfaa19.jpg)

![](/api/attachments/9J343XTA/fulltext/images/36d4b99b1d8ca46c8491e3122d1dac6f4f12cb96806ef682048c6b8dfe7c5b1b.jpg)

![](/api/attachments/9J343XTA/fulltext/images/236ecbdca5ec4a481dbf186a2822a95757eab4767d498aef31109ef85efd0416.jpg)  
Fig. 6. Estimated parameter curves for number of bidders and their interaction with the starting price, seller reputation and its interaction with auction duration

It is observed that the usage of a hidden reserve price has a positive impact on the price level, but during the second half of the auction, such a tool used by the seller results in slower price increases than in non-reserve auctions.

The relationship between auction duration and price formation is strongest during the middle of the auction and has a negative sign. While eBay's auctions experience heavy participation at the beginning and at the end, the auction-middle is typically marked by a “draught” with only few incoming bids. Our analysis shows that this draught is stronger in longer-lasting auctions. On the other hand, participation is typically heavy at the auction end and our analysis of the price velocity shows that at the end the auction dynamics are larger for longer lasting auctions.

## 4.3.2. Competition — number of bidders and interaction with opening bid

The first panel in Fig. 6 shows the effect of the current number of bidders. The top graph shows that, not surprisingly, the number of bidders is positively associated with the current price. A larger number of bidders results in increased competition for the item and thus in a higher (final) price. Interestingly, though, the strength of this relationship is strongest in the middle of the auction. (Note the ∩-shape of the graph.) The middle of the auction typically experiences the smallest amount of bidder participation, marked by “evaluators” who place only a single bid and do not return until the auction is over (see [4]). These evaluators typically place higher bids than the average bidder, resulting in a stronger price increase per bidder.

The middle and bottom graph reveal the impact of competition on price dynamics. Note the decreasing parameter curves for both the price velocity and acceleration. eBay's auctions typically experience most bidding activity at the end. This is commonly described as bid sniping where, during the last moments, bidders compete heavily with each other since the winner takes it all. A high competition level is therefore not uncommon at the auction end, in contrast to earlier stages of the auction. The coefficients of the price dynamics thus suggest that the same competition level early in the auction results in a much stronger price velocity and acceleration than at the auction end.

It is rewarding to carefully examine the interaction between the number of bidders and the starting price. The shape of the parameter curve is almost exactly the opposite of the main effect of the number of bidders. In particular, the interaction for the price evolution is negative! The implication is that, although the current number of bidders has a positive effect on the price formation process, the magnitude of this effect is reduced for a large starting price. A similar moderating effect can be seen for the auction dynamics.

## 4.3.3. Seller reputation and interaction with auction duration

We observe that seller ratings, which also proxy for experience, negatively correlate with price levels and are moderated by the auction duration. Since we observe a negative main effect and a positive interaction effect, we conclude that in longer auctions, higher seller ratings result in higher price levels. Looking at the dynamics, we also observe that the effect weakens as duration increases.

## 4.3.4. Market characteristics — item value, currency, category

The impact of the item's value is shown in the left-most panel of Fig. 7. As in the case of the starting price, the relationship between value and the current price (top graph) is positive throughout the auction, implying that auctions with higher-valued items attract higher bids. However, in contrast to the starting price, the strength of this relationship increases steadily. This is not surprising: at the beginning of the auction, it appears that bidders either have not yet formed a clear opinion about the item's valuation or are not yet willing to fully reveal their valuation. Either way, the price formation is not strongly associated with the item's value. This changes at the end of the auction. At the end, bidders receive an ever increasing amount of information, from other participants and also possibly from outside sources. As the auction closes they are also more willing to reveal their true valuation in order to win the item. It is reasonable to assume towards the end that eBay's second-price mechanism induces truth-telling. Using the lens of William Vickrey's (1961) stylized model, eBay's mechanism is a hybrid between an open ascending English auction and a sealed bid second price auction. For such hybrid mechanisms multiple equilibria are likely to exist and are being currently explored [2,9]. Towards the end of the auction it is straightforward to prove that the absence of any response time to other bidders makes truth-telling sniping a weakly dominant strategy, and the eBay auction resembles a second-price sealed bid auction. Thus the strength of the relationship increases.

As for the dynamics, we can see that towards the auction end higher prices are associated with an increase in bidding dynamics. Indeed, while an item with a higher price strongly correlates with a faster price increase (middle graph), it is also associated with a faster rate of increase (bottom graph). These two graphs suggest that for auctions with highly valuable items, fast price accelerations at closing can be expected. One explanation is that bidders for high-value items are more pricesensitive and act more strategically in placing their bids compared to bidders for inexpensive goods. It also suggests that bid sniping is more prevalent in high-value auctions.

![](/api/attachments/9J343XTA/fulltext/images/110ea58b7a3a64ac0c5800f80e78664436c072be8f82cdea8a5a1b8228be5e30.jpg)  
Fig. 7. Estimated parameter curves for item value, currency, category and bidder experience.

With respect to the currency effect, since we control for an item's final price, it is not surprising that the coefficient of the price path is near zero at the auction end. However, the dynamics are more interesting. Overall, US auctions experience faster price movement at the auction-end than their European counterparts. We also find that compared to European auctions, the price levels of US auctions are on average 4% higher during the first half of the auction. These results indicate that the US market, in contrast to Europe, is characterized by both early bidding and late bidding. While late bidding appears to be the dominant strategy in the European market, it is stronger in the US. This may indicate a fundamental cross-cultural difference in bidding habits.

We find that prices of category B items are somewhat lower than category A items throughout the auction. The rate of price increase for category B items (Jewelry, Clothing, Antiques etc.) starts out slower than category

A, but from mid-auction it catches up and subsequently increases at a faster rate.

## 4.3.5. Current average bidder experience

Recall that in contrast to the seller rating, the average bidder rating does not remain constant throughout the auction. In fact, the average rating of currently participating bidders changes with every new incoming bid. We therefore use a dynamic covariate (average experience level) that takes this change into account. We observe a negative relationship with the current price, suggesting that experience pays off in terms of a lower price. However, once again the dynamics shed more light: It is evident that a higher experience level is suggestive of enhanced strategizing on the part of the bidders. We observe that early in the auction, high experience leads to slow price formation. This indicates that experienced bidders appear to hold back their valuations and do not bid early, a rational consistent with the literature on sniping [21].

## 5. Conclusion

In this paper, using a random sample of 1009 eBay auctions, we demonstrate how functional data modeling can be applied to understand the process of price formation and its dynamics in online auctions on eBay. We believe that such an understanding enhances researchers' ability to examine the drivers of the price formation process of online auctions. It facilitates new conversations regarding the temporal nature of the various effects and their interactions, and provides important clues to practitioners using such mechanisms to serve their selfinterest (sellers maximizing revenue, bidders maximizing surplus, auction sites maximizing profit). Our key finding is that there is almost little or no informational content in the middle stages of an eBay online auction's price formation process. This finding suggests that there is significant scope for enhancing the price formation contribution of the early and middle stages of ebay's auction mechanism. We find that the incremental impact of an additional bidder's arrival on the rate of price increase is smaller at the end of the auction. This suggests that towards the closing sniping stages of the auction, ebay's progressive mechanism verifiably turns into a sealed bid second price mechanism. We find that “stakes” do matter and that the rate of price increase is higher for more expensive items<sup>16</sup>, especially at the start and end of an auction. It is observed that higher seller ratings (which correlate with experience) positively influence the price dynamics, but the effect is weaker in auctions with longer durations. In an interesting cross-cultural effect, we find that compared to European auctions, US auctions get 4% higher price levels during the first half of the auction. After that the price levels are comparable. The second order dynamics of this effect suggest that the main difference is in the middle of the auction. While US auctions have faster price increases during the beginning and end of the auction, they are slower than European auctions during the middle duration. Another interesting finding is that price level is negatively related to auction duration when the seller has a low rating! However, in auctions with high-rated sellers longer auctions achieve higher price levels throughout the auction, and especially at the start and end. This suggests that new and inexperienced sellers are better off using shorter auction durations initially, and then switching to longer durations as their reputation increases. To the best of our knowledge, prior research has not shown the effects of interactions between a seller's ratings and their mechanism design choices, even in a static environment.

While IT centric sites such as eBay facilitate billions of dollars of economic exchange, it is our belief that the research community is yet to fully exploit the enhanced information processing capabilities towards the design science [10] of electronic markets. We find it intriguing that eBay uses a pre-determined and static bid increment schedule for every single one of the billions of auctions it conducts. Recent work [4] suggests that by adopting suboptimal bid increments the mechanism is potentially leaving significant money on the table at the cost of the sellers. Consider the case of an auction possessing above average acceleration towards the final closing stages. Since acceleration leads to higher velocity, which leads to higher price, a hypothetical “design science enabled auction mechanism” would anticipate higher bidding intensity and be willing to set a higher “target” for the bidders. Given eBay's hard closing time, the only way the mechanism can adapt the target is by setting a higher than (current) one percent bid increment to add to the second highest bid. Clearly, it would not want to do this in auctions that do not have increasing intensity, as it would increase the likelihood of an otherwise eligible bidder falling through the crack! We believe that the study of dynamic mechanisms design aspects, such as dynamic bid increments and dynamic buy-it-now prices, and their accompanying endogeneity issues, promises to be an exciting area of future research. This study contributes by seeding the dialogue with comprehensive descriptive empirical insights of the dynamics of the price formation process.

## Appendix A. Estimation of the smoothing spline

To describe the minimization of the penalized residual sum of squares in Eq. (2), we define the $( L + p + 1 )$ vector of spline basis functions

$$
\mathbf {x} (t) = \left(1, t, t ^ {2}, \dots , t ^ {p}, \left[ (t - \tau_ {1}) _ {+} \right] ^ {p}, \dots , \left[ (t - \tau_ {L}) _ {+} \right] ^ {p}\right)\tag{5}
$$

and note that we may write the spline in Eq. (1) as $f ( t ) = \mathbf { x } ( t ) \widetilde { \beta } ,$ where $\widetilde { \beta } = ( \widetilde { \beta } _ { 0 } , \widetilde { \beta } _ { 1 } , \dots , \widetilde { \beta } _ { p } , \widetilde { \beta } _ { p 1 } , \dots , \widetilde { \beta } _ { p L } )$ is <sup>ð</sup>the $( L + p + 1 )$ <sup>¼ ð Þ</sup>parameter vector. The roughness penalty can now be written as

$$
\mathrm{PEN} _ {m} = \widetilde {\beta} ^ {\prime} \mathbf {D} \widetilde {\beta},\tag{6}
$$

where the symmetric positive semi-definite penalty matrix D is defined as

$$
\mathbf {D} = \int \left\{D ^ {m} \mathbf {x} (t) \right\} ^ {\prime} \left\{D ^ {m} \mathbf {x} (t) \right\} d t.\tag{7}
$$

We can now rewrite the penalized residual sum of squares in Eq. (2) as

$$
Q _ {\lambda , m} = \lambda \widetilde {\beta} ^ {\prime} \mathbf {D} \widetilde {\beta} + \sum_ {i = 1} ^ {n} \left\{y _ {i} - \mathbf {x} (t _ {i}) \widetilde {\beta} \right\} ^ {2}.\tag{8}
$$

Let $( \widetilde { \mathbf { y } } { = } \widetilde { y } _ { 1 } { , } . . . , \widetilde { y } _ { n } ) ^ { \prime }$ denote the vector of the observed bids and define the matrix of spline basis functions

$$
\mathbf {X} = \left( \begin{array}{c} \mathbf {x} (t _ {1}) \\ \mathbf {x} (t _ {2}) \\ \vdots \\ \mathbf {x} (t _ {n}) \end{array} \right).\tag{9}
$$

Eq. (8) can now be rewritten as

$$
Q _ {\lambda , m} = \lambda \widetilde {\beta} ^ {\prime} \mathbf {D} \widetilde {\beta} + (\tilde {\mathbf {y}} - \mathbf {X} \widetilde {\beta}) ^ {\prime} (\tilde {\mathbf {y}} - \mathbf {X} \widetilde {\beta}).\tag{10}
$$

Setting the gradient of the right hand side of Eq. (10) equal to zero and rearranging terms yields the estimating equations

$$
\left(\mathbf {X} ^ {\prime} \mathbf {X} + \lambda \mathbf {D}\right) \widetilde {\beta} = \mathbf {X} ^ {\prime} \widetilde {y}.\tag{11}
$$

Solving for $\widetilde { \beta }$ in Eq. (11) gives the penalized spline estimator

$$
\hat {\tilde {\beta}} _ {p s} = (\mathbf {X} ^ {\prime} \mathbf {X} + \lambda \mathbf {D}) ^ {- 1} \mathbf {X} ^ {\prime} \widetilde {y}.\tag{12}
$$

We note that the Hessian matrix of Eq. (10) is

$$
2 \left(\mathbf {X} ^ {\prime} \mathbf {X} + \lambda \mathbf {D}\right).\tag{13}
$$

Since the matrix X′X is positive definite and $\lambda D$ is positive semi-definite, the Hessian matrix is positive definite and, hence, $\hat { \beta } _ { p s }$ in Eq. (12) indeed minimizes the penalized residual sum of squares in Eq. (10).

## References

[1] Sulin Ba, Paul A. Pavlou, Evidence of the effect of trust building technology in electronic markets: Price premiums and buyer behavior, MIS Quarterly 26 (2002) 269–289.

[2] Patrick Bajari, Ali Hortacsu, The winner's curse, reserve prices and endogenous entry: Empirical insights from ebay auctions, Rand Journal of Economics 3 (2) (2003) 329–355.

[3] Patrick Bajari, Ali Hortasu, Economic insights from internet auctions, Technical report, Duke University working paper, 2004, (available at www.econ.duke.edu/\~bajari/auction\_survey.pdf).

[4] Ravi Bapna, Alok Gupta, Paulo Goes, Analysis and design of business-to-consumer online auctions, Management Science 49 (2003) 85–101.

[5] Ravi Bapna, Paulo Goes, Alok Gupta, Yiwei Jin, User heterogeneity and its impact on electronic auction market design: an empirical exploration, MIS Quarterly 28 (2004) 1.

[6] Ravi Bapna, Wolfgang Jank, and Galit Shmueli. Consumer surplus in online auctions. Information Systems Research (in press) (Available at SSRN: http://ssrn.com/abstract=840264).

[7] Marcel Cohen, Consumer involvement — driving up the cost, Consumer Policy Review 10 (4) (2000) 122–125.

[8] Chrysanthos Dellarocas, The digitization of word-of-mouth: promise and challenges of online reputation mechanisms, Management Science (2003) (October Issue).

[9] Kevin Hasker, Raul Gonzalez, Robin C. Sickles, An analysis of strategic behavior and consumer surplus in eBay auctions, Technical report, Rice University working paper, 2001, (www. ruf.rice.edu/\~rsickles/paper/auction.pdf).

[10] Alan R. Hevner, Salvatore T. March, Jinsoo Park, Sudha Ram, Design science in information systems research, MIS Quarterly 28 (2005) 75–105.

[11] V. Hyde, W. Jank, G. Shmueli, Investigating concurrency in online auctions through visualization, The American Statistician 60 (3) (2006) 241–250.

[12] W. Jank, G. Shmueli, Studying Heterogeneity of Price Evolution in eBay Auctions via Functional Clustering, in: Adomavicius, Gupta (Eds.), Handbook of Information Systems Series: Business Computing, Elsevier, 2006.

[13] W. Jank, G. Shmueli, Functional data analysis in electronic commerce research, Statistical Science 21 (2) (2006) 155–166.

[14] Rama Katkar, David Lucking-Reiley, Public versus secret reserve prices in eBay auctions: results from a pokémon field experiment, Technical report, Working paper, University of Arizona, 2000.

[15] Paul Klemperer, How (not) to run auctions: the european 3 g telecom auctions, European Economic Review 46 (4–5) (2002) 829–845.

[16] David Lucking-Reiley, Using field experiments to test equivalence between auction formats: magic on the internet, American Economic Review 89 (5) (1999) 1063–1080.

[17] David Lucking-Reiley, Doug Bryan, Naghi Prasad, Daniel Reeves, Pennies from eBay: the determinants of price in online auctions, Technical report, University of Arizona working paper, 2000, (available at http://eller.arizona.edu/ reiley/papers/PenniesFromEBay.pdf).

[18] Roger Myerson, Optimal auction design, Mathematics of Operation Research 6 (1981) 58–73.

[19] J.O. Ramsay, B.W. Silverman, Functional data analysis, second edition. Springer-Verlag, New York, 2005.

[20] S.K. Reddy, M. Dass, Modeling online auction dynamics of fine art using functional data analysis, Statistical Science 21 (2) (2006) 179–193.

[21] A.E. Roth, A. Ockenfels, Last-minute bidding and the rules for ending second-price auctions: evidence from ebay and amazon auctions on the internet, The American Economic Review 92 (4) (2002) 1093–1103.

[22] Vernon L. Smith, James M. Walker, Monetary rewards and decision cost in experimental economics, Economic Inquiry 31 (1993) 245–261.

[23] K. Stewart, D. Darcy, S. Daniel, Opportunities and challenges applying functional data analysis to the study of open source software evolution, Statistical Science 21 (2) (2006) 167–178.

[24] William Vickrey, Counterspeculation, auctions, and competitive sealed tenders, Journal of Finance 16 (1961) 8–37.

[25] S.Wang,W. Jank, G. Shmueli, Explaining and forecasting online auction prices and their dynamics using functional data analysis, Journal of Business and Economic Statistics (in press).

![](/api/attachments/9J343XTA/fulltext/images/a0f9303fb6f3c1eb50da3461138e0d71d8ef232fddfba6f92c48fb830c040161.jpg)  
Dr. Ravi Bapna is the Executive Director of the Centre for Information Technology and the Networked Economy (CITNE) at the Indian School of Business, as well as a tenured Associate Professor in the Information Systems area. He teaches in the ISB's PGP and Executive Education programmes. Prior to joining the ISB, Professor Bapna was an Associate Professor and Ackerman Scholar in the Operations and Information Management Department at the School of Business,

University of Connecticut. His research interests are in the areas of Online Auctions, E-market Design, Grid Computing, and the Economics of Information Systems. His research has been extensively published in a wide array of journals such as Management Science, Informs Journal on Computing, Statistical Science, Information Systems Research, Journal of Retailing, MIS Quarterly, Decision Sciences, CACM, Naval Research Logistics, DSS, EJOR and ITM. He was awarded the prestigious Ackerman Scholar Award for outstanding research at the University of Connecticut. He contributes regularly to popular press outlets such as India Knowledge @ Wharton, The Economic Times and Business Today. Professor Bapna has been invited to present his research at the Federal Trade Commission, Washington DC, Telecom Regulatory Authority of India (TRAI), Carnegie Mellon University, New York University, University of Maryland, IIM-Calcutta, National Chengchi University, Taiwan, University of Washington, National University of Singapore and University of Minnesota, among others. He serves on the editorial board of the flagship journals MIS Quarterly, as well as for the journal Production and Operations Management. He also serves as ad-hoc AE for Management Science. He regularly serves on programme committees of major international IS conferences and workshops, and is the Co-Chair of the First International Symposium of Information Systems to be held at the ISB. He is a member of the Nasscom Innovation Institute, a think-tank to foster innovation in the Indian IT/ITeS industry. Professor Bapna completed his Bachelor's degree in Computer Engineering from the Manipal Institute of Technology and received his doctorate degree from the University of Connecticut, where his thesis was in the area of Information Systems.

![](/api/attachments/9J343XTA/fulltext/images/cf9d2465a3ad8ca8494b6a117dbea0eec779ac3f83a392f26efa771caceaedab.jpg)

Wolfgang Jank is an Associate Professor in the Smith School of Business at the University of Maryland. He joined the University of Maryland in August 2001. He is interested in data-driven problems and challenges in electronic commerce, marketing, operations management and aviation. His methodologi cal interests focus on stochastic estimation and optimization, functional data analysis, information visualization and methods for spatial and temporal data. Wolfgang Jank received his Master’s degree in Mathematics from the Technical University of Aachen. He received his Ph.D. in Statistics from the University of Florida. He is a member of the American Statistical Society, the Institute of Mathematical Statistics, the European Network for Business and Industrial Statistics, the Association for Computing Machinery and INFORMS. He is past president of the University of Florida's chapter of the statistical honor society Mu Sigma Rho.

![](/api/attachments/9J343XTA/fulltext/images/f9595b356cf1f87dd4aacf7508f3dcc9f0dbb1f8bb7e3e3df6dc1928cbece70e.jpg)  
Galit Shmueli is an Associate Professor of Statistics at the Robert H. Smith School of Business, University of Maryland, College Park. She holds an M.Sc. and Ph.D. in Statistics from the Israel Institute of Technology. Her research focuses on statistical methods for modern data structures with applications to eCommerce and biosurveillance.
