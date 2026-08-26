---
otero_id: 4678
otero_key: "X5RSQ8PG"
title: "Price discovery in combinatorial auctions using Gibbs Sampling"
authors: "Joni L. Jones; Richard W. Andrews"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.10.011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Price discovery in combinatorial auctions using Gibbs Sampling

Joni L. Jones <sup>a,\*</sup>, Richard W. Andrews

<sup>a</sup>Information Systems and Decision Sciences, College of Business Administration, University of South Florida, 4202 East Fowler Avenue, CIS1040 Tampa, FL 33620-7800, United States

<sup>b</sup>Statistics and Management Science, University of Michigan Business School, United States

Received 30 September 2003; received in revised form 17 October 2004; accepted 18 October 2004 Available online 19 November 2004

## Abstract

Considerable research discusses the advantages and disadvantages of combinatorial auctions. This study addresses a disadvantage, the loss of price discovery for the individual items sold as bundles. Prior studies confirm that there may not be a unique unit-level equilibrium price. We claim a distribution of prices satisfy a given allocation and describe a technique to determine these distributions. Gibbs Sampling allows us to discover characteristics of combinatorial auctions based on the allocated bids. We extract the market-influenced unit-level price, bidder profit, reservation discount distributions and are able to find patterns that depict synergies between products. The posterior distribution provides insights useful to managerial decision making.

<sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Pricing; IS implementation; Combinatorial auctions; Gibbs Sampling; Bayesian estimation; Markov processes/chains; Decision analysis; Simulation

## 1. Introduction

Auctions have been used historically as a method of price discovery especially for items where demand and value vary greatly [4,8,14], however in combinatorial auctions individual item price discovery is forfeited. Combinatorial auctions allow bidders to create and submit a single bid for a collection or bundle of items [17]. Although, there have been numerous studies that have looked at equilibrium prices in combinatorial auctions they have been limited to the discovery of bundle equilibrium prices and not individual item prices [5,16,18]. Discovering equilibrium for individual items has been hampered by the fact that prices are known for only the bundles that are allocated. In the absence of an allocation of bundles consisting of single items the component prices remain undiscovered. In the case of multiple homogeneous products component prices may be non-anonymous, meaning that buyers may win identical products but pay different prices [16].

Individual item price discovery has been limited to approximation techniques whose goal was to discover the maximum component price that when summed equals the winning bundle price and minimizes the gap between these prices and the sum of the components in the corresponding loosing bids [7,15]. See Ref. [19] for a comparison of the techniques. These studies confirm that there may not be a unique equilibrium; rather many component prices can satisfy an allocation. We claim that there is a distribution of prices that satisfy a given allocation and this study attempts to determine these price distributions.

We are motivated by the fact that individual item prices provide the foundation from which to build bundle values in the absence of a winning bundle composed of the desired combination of goods. However, as stated previously, a single value may not represent the equilibrium price for bundle components. Therefore, this study describes a method to extract a distribution of market-influenced prices for individual items from winning allocations. These prices can be used to provide signal information to help bidders formulate reentering bids in iterative combinatorial auctions. Here we are attempting to assist bidders in these complex environments where simply displaying winning combinations and their associated bids may not be easily decomposed to extract information pertinent to bidder’s decision making needs.

Unit level value information is vital to managerial decision-making. Product managers need to be able to assess the product’s market value and thus its contribution to marginal costs. Additionally, unit prices can be used to formulate pricing and bundling decisions in fixed price markets. These considerations, when added to the knowledge gathered from an analysis of the bundle prices, eliminate the information gaps inherit in combinatorial auction price discovery. We use a Bayesian approach which employs Gibbs Sampling to determine the unit price distributions. Gibbs Sampling is a straight-forward application of Markov Chain Monte Carlo methods and when used in a Bayesian context allows unknown posterior distributions to be generated from known full conditional distributions. See Ref. [11] and Ref. [6] for a basic explanation of Gibbs Sampling and Ref. [12] for a thorough explanation of its foundations and applications. With Gibbs Sampling the full conditional distributions are used to sequentially produce a Markov Chain whose steady state distribution represents the joint posterior distributions of interest.

Since its introduction into Bayesian statistical analysis [10] the Gibbs Sampling technique has been used extensively in applications to hospital admissions [3], fuel economy [2], marketing [1], finance [9], and many other fields. This paper represents its first use in auction literature. In combinatorial auctions where the computational complexity prevents direct discovery of unit prices, Gibbs Sampling provides an attractive solution methodology by supplying the distribution of unit prices and other characteristics of a given allocation.

## 2. Model

The Gibbs price discovery procedure starts with data representing an allocation from a combinatorial auction and extracts from the data individual item price distributions. The process of assigning list prices, sequential bidding, and allocation renders a situation in which the values of the bundles are specified; however, the final price of a single unit has not been explicitly stated. The purpose of this section is to describe a Bayesian procedure that yields estimated distributions for the unit price of each unit.

The procedure is a full Bayesian approach that takes into account all the data and yields posterior distributions for all quantities of interest. Because of the complexity of the model, tractable closed form posterior distributions are impossible to derive and this leads to the use of Gibbs Sampling.

We define the following quantities that will be used in the presentation of the model.

$Y _ { i } { = } \mathrm { f i n a l }$ bid amount (in US\$1000) by the ith bidder; $i { = } 1 , 2 , \ldots , I ,$

I=the number of accepted bids in the data set.

The values of $Y _ { i }$ are the known final bid amounts.

/<sub>j</sub>=unit value of jth product, $j = 1 , 2 , \ldots , J ,$

$Z _ { j } = \mathrm { t h e }$ suggested list price of a individual unit of the $j \mathrm { t h ~ p r o d u c t } , j \mathrm { = 1 } , 2 , \ldots , J ,$

J=the number of products in the data set.

The $Z _ { j } \mathrm { ' s } ,$ suggested list prices, are set and known to both the seller and the buyers. The unit prices, $\phi _ { j } \mathbf { \bar { s } } ,$ are the unknown quantities of primary interest.

The allocation procedure yields:

$K _ { i , j }$ =the number of units of the jth product awarded to the ith customer.

This procedure works with any nature of matrix of $\vec { K _ { i , j } \mathrm { ~ s ~ } }$ even sparsely populated ones common in combinatorial auction allocations.

We also define

$p _ { i } { = }$ the margin (profit/loss) to the seller acquired from bidder i.

This margin quantity, $p _ { i } ,$ represents the mean of the difference between the final bid amount and the sum of the unit prices included in that bid. These profit margins, which may be negative, will be discussed thoroughly after the results of the estimation are presented.

Using these quantities, the model is:

$$
Y _ {i} = \sum_ {j = 1} ^ {J} K _ {i, j} \phi_ {j} + \varepsilon_ {i}\tag{1}
$$

$$
\begin{array}{l} \phi_ {j} \sim \text { Normal } (\beta Z _ {j}, \sigma_ {\phi} ^ {2}) \text {(independent)} j = 1, \ldots , J, \\ \varepsilon_ {i} \sim \text { Normal } (p _ {i}, \sigma^ {2}) \text {(independent)} i = 1, \ldots , I. \end{array}
$$

The normal distribution is used for ease of computation and because the unit value of a product can be considered conceptually as additive in characteristics. We also chose this distribution because we assume that the buyer’s unit values will fall close to the suggested list price with the variation diminishing as the distance from the mean increases. The distribution used should reflect the characteristics of the data. The formulation would need to be modified to reflect the chosen distribution and its conjugate priors.

This model sets the bids as the linear sum of the unit prices weighted by the known allocation. The marginal profit, $p _ { i } ,$ , is included as the mean of the error term, e. The list price, $Z _ { j } ,$ is included in the model by making the mean of the random component unit price a proportion, $\beta ,$ , of the associated list price. In addition to the unknown unit prices, $\phi _ { j } \mathbf { \bar { s } }$ and the bid profits, ${ p } _ { I } \mathbf { \ ' } _ { \mathbf { s } , }$ this model has introduced three parameters that need to be estimated.

They are:

$\sigma ^ { 2 } \overline { { \overline { { \mathbf { \Lambda } } } } }$ =the error variance of the bid equation,

$\sigma _ { \phi } ^ { ~ 2 }$ =the variance of the unit prices and,

$\beta =$ =the proportion of the unit price which sets the mean for the associated $\phi$

Eq. (1) constitutes the likelihood function of the Bayesian approach. We now specify prior distributions on the parameters. We use potentially high variance conjugate prior distributions because conjugate distributions are convenient for obtaining the full conditional distributions needed in Gibbs Sampling and they allow us to realistically express our prior beliefs. We are using non-informative prior distributions except for the variance.

The assigned prior distributions are:

$$
\begin{array}{l} p _ {i} \sim \text { Normal } (\delta , \theta^ {2}) \text {(independent for every i)}, \\ \sigma^ {2} \sim \text { Inverse Gamma } (a _ {1}, b _ {1}), \\ \sigma_ {\phi} ^ {2} \sim \text { Inverse Gamma } (a _ {2}, b _ {2}), \text { and } \\ \beta \sim \text { Normal } (\tau , \gamma^ {2}). \end{array}
$$

The likelihood function and the assigned prior distributions can be summarized in the distribution of all quantities. This is represented as follows:

$$
\begin{array}{l} \prod_ {i = 1} ^ {I} N \left[ Y _ {i} - \sum_ {j = 1} ^ {J} K _ {i, j} \phi_ {j} - p _ {i} | 0, \sigma^ {2} \right] \times \prod_ {j = 1} ^ {J} N \left[ \phi_ {j} - \beta Z _ {j} | 0, \sigma_ {\phi} ^ {2} \right] \\ \times \prod_ {i = 1} ^ {I} N [ p _ {i} | \delta , \theta^ {2} ] \times N [ \beta | \tau , \gamma^ {2} ] \times I G [ \sigma^ {2} | a _ {1}, b _ {1} ] \\ \times I G [ \sigma_ {\phi} ^ {2} | a _ {2}, b _ {2} ]. \end{array} \tag {2}
$$

Using this joint distribution of all quantities it is straight forward to derive the full conditional of each unknown quantity where the conditioning is on everything else. These full conditional distributions are necessary to use the Gibbs Sampling procedure. Each full conditional will be presented in the order they are used within the Gibbs Sampler and, when required, the settings of the prior parameters will be discussed. The full conditional for each quantity generated is presented conditional on all other quantities, parameters and data. We use the term <sup>b</sup>Rest<sup>Q</sup> after the conditioning sign to indicate all the other quantities. The full conditional can be calculated by expanding the terms of the joint distribution that include the parameter of interest.

## 2.1. Error variance of the bid equation—r<sup>2</sup>

The terms from the joint distribution of all quantities which will be used in finding the full conditional distribution on $\sigma ^ { 2 }$ are:

$$
\prod_ {i = 1} ^ {I} N \left[ Y _ {i} - \sum_ {j = 1} ^ {J} K _ {i, j} \phi_ {j} - p _ {i} | 0, \sigma^ {2} \right] \times I G \left[ \sigma^ {2} \mid a _ {1}, b _ {1} \right],\tag{3}
$$

or

$$
\begin{array}{l} P (\sigma^ {2} | \bullet) \propto \prod_ {i = 1} ^ {I} \frac {1}{\sqrt {2 \pi \sigma}} \\ \times \exp \left(- \frac {1}{2 \sigma^ {2}} \left(\left(Y _ {i} - \sum_ {j = 1} ^ {J} K _ {i, j} \phi_ {j} - p _ {i}\right) - 0\right) ^ {2}\right) \\ \times \frac {b _ {1} ^ {a _ {1}}}{\Gamma (a _ {1})} \sigma^ {2 ^ {- (a _ {1} + 1)}} e ^ {\left(\frac {- b _ {1}}{\sigma^ {2}}\right)}. \end{array}
$$

After completing the math the resulting full conditional distribution is:

$\mathrm { { \sigma } } ^ { 2 } |$ Rest\~Inverse Gamma

$$
\begin{array}{l} a _ {1} ^ {\prime} = a _ {1} + \frac {I}{2} \\ b _ {1} ^ {\prime} = b _ {1} + \frac {1}{2} \sum_ {i = 1} ^ {I} \left(Y _ {i} - \sum_ {j = 1} ^ {J} K _ {i, j} \phi_ {j} - p _ {1}\right) ^ {2} \end{array}\tag{4}
$$

For prior parameters we are using $a _ { 1 } { = } 2 . 1$ and $b _ { 1 } { = } 2 0 . 0$ . These values give a prior mean of 18.18 and a prior variance of 3333.33 which we characterize as being vague and close enough to non-informative to have very little influence on the resulting posterior distribution. Non-informative priors, as the name implies, have been used so that the data and not the prior distribution determines the final results.

##

The terms from the joint distribution of all quantities which will be used in finding the full conditional distribution on $\sigma _ { \phi } ^ { ~ 2 }$ are:

$$
\prod_ {j = 1} ^ {J} N [ \phi_ {j} - \beta Z _ {j} | 0, \sigma_ {\phi} ^ {2} ] \times I G [ \sigma_ {\phi} ^ {2} | a _ {2}, b _ {2} ]\tag{5}
$$

Using the technique described above we see that the resulting full conditional distribution is:

jA<sup>2</sup> | Rest\~Inverse Gamma

$$
\begin{array}{l} a _ {2} ^ {\prime} = a _ {2} + \frac {J}{2} \\ b _ {2} ^ {\prime} = b _ {2} + \frac {1}{2} \sum_ {j = 1} ^ {J} (\phi_ {j} - \beta Z _ {j}) ^ {2} \end{array}\tag{6}
$$

For prior parameters we use the same setting $( a _ { 2 } { = } 2 . 1$ 1 and $b _ { 2 } { = } 2 0 . 0 )$ as we did for $\sigma ^ { 2 }$ with the same rational.

## 2.3. List price discount factor—b

The terms from the joint distribution of all quantities which will be used in finding the full conditional distribution on $\beta$ are:

$$
\prod_ {j = 1} ^ {J} N [ \phi_ {j} - \beta Z _ {j} | 0, \sigma_ {\phi} ^ {2} ] \times \prod_ {j = 1} ^ {J} N [ \beta | \tau , \gamma^ {2} ].\tag{7}
$$

The resulting full conditional distribution is:

b| Rest\~Normal

$$
\text { Mean } = \frac {\frac {\tau}{\gamma^ {2}} + \frac {\sum_ {j = 1} ^ {J} \phi_ {j} Z _ {j}}{\sigma_ {\phi} ^ {2}}}{\frac {1}{\gamma^ {2}} + \frac {\sum_ {j = 1} ^ {J} Z _ {j} ^ {2}}{\sigma_ {\phi} ^ {2}}}\tag{8}
$$

$$
\text { Variance } = \frac {1}{\frac {1}{\gamma^ {2}} + \frac {\sum_ {j = 1} ^ {J} z _ {j} ^ {2}}{\sigma_ {\phi} ^ {2}}}\tag{9}
$$

Throughout this analysis we set $\gamma ^ { 2 }$ to infinity which is equivalent to using a non-informative prior on beta and therefore the value of s is irrelevant.

## 2.4. Profit for bidder $i { \ - - } p _ { i }$

The terms from the joint distribution of all quantities which will be used in finding the full conditional distribution on $p _ { i }$ are:

$$
\prod_ {i = 1} ^ {I} N \left[ Y _ {i} - \sum_ {j = 1} ^ {J} K _ {i, j} \phi_ {j} - p _ {i} | 0, \sigma^ {2} \right] \times \prod_ {i = 1} ^ {I} N \left[ p _ {i} | \delta , \theta^ {2} \right]\tag{10}
$$

The resulting full conditional is:

$p _ { i } |$ Rest\~Normal

$$
\text { Mean } = \frac {\frac {\delta}{\theta^ {2}} + \frac {\left(Y _ {i} - \sum_ {j = 1} ^ {J} K _ {i , j} \phi_ {j}\right)}{\sigma^ {2}}}{\frac {1}{\theta^ {2}} + \frac {1}{\sigma^ {2}}}\tag{11}
$$

$$
\text { Variance } = \frac {1}{\frac {1}{\theta^ {2}} + \frac {1}{\sigma^ {2}}}\tag{12}
$$

The same as in the last subsection we set $\theta ^ { 2 }$ to infinity which implies a non-informative prior on the $\boldsymbol { p } _ { i } { } ^ { \prime } { \mathbf { s } }$ and the irrelevance of the value of $\delta .$ .

## 2.5. Unit price of product $j { \mathrm { - } } \phi _ { j _ { o } }$

The terms from the joint distribution of all quantities which will be used in finding the full conditional distribution on $\phi _ { j _ { 0 } }$ are:

$$
\begin{array}{l} \prod_ {i = 1} ^ {I} N \left[ Y _ {i} - \sum_ {j \neq j _ {o}} ^ {J} K _ {i, j} \phi_ {j} - p _ {i} | 0, \sigma^ {2} \right] \\ \times N \left[ \phi_ {j _ {0}} - \beta Z _ {j} | 0, \sigma_ {\phi} ^ {2} \right], \end{array}\tag{13}
$$

where $j _ { 0 }$ indicates the price of a particular product. The resulting full conditional is:

$\theta _ { j 0 } |$ Rest\~Normal

$$
\text { Mean } = \frac {\frac {\beta Z _ {j _ {0}}}{\sigma_ {\phi} ^ {2}} + \sum_ {i = 1} ^ {I} \frac {K _ {i , j _ {0}} (Y _ {i} - (p _ {i} + \sum_ {j \neq j _ {0}} K _ {i , j} \phi_ {j}))}{\sigma^ {2}}}{\frac {1}{\sigma_ {\phi} ^ {2}} + \frac {1}{\sum_ {i = 1} ^ {I} \frac {\sigma^ {2}}{K _ {i , j 0} ^ {2}}}}
$$

$$
\text { Variance } = \frac {1}{\frac {1}{\sigma_ {\phi} ^ {2}} + \frac {1}{\sum_ {i = 1} ^ {I} \frac {\sigma^ {2}}{K _ {i , j 0} ^ {2}}}}\tag{14}
$$

ð15Þ

There is no required prior parameter settings needed for this step of the Gibbs Sampler.

## 2.6. Simulation

The data we investigate in this study originates from a rule-based combinatorial auction described in Ref. [13]. The auction requires the bidder to establish a set of rules and a bid amount that represents the value of an allocation that satisfies all the imposed requirements. This mechanism relieves the buyer of burden of enumerating all the possible combinations of goods that would be required to place the exclusive-or (XOR) bids common in many combinatorial auctions.

The auction assumes the common value model where the value of each item (or bundle of items) to be sold has two components, the pure common value and a private value. All bidders have the same prior information regarding the pure common value such as a suggested list price. The private value is what influences the choice of bundle (or rules imposed on bundle creation) and their final bid amount. This amount could be above or below the common value. Bidders are myopic, trying to maximize their profit at each stage.

The domain in which the auction is employed is that of Television Advertising Sales where the buyers are attempting to buy a collection of 15-s commercial slots (units) in a number of primetime television shows (products) to satisfy their campaign requirements. A combinatorial auction is appropriate as synergies exist in this environment due to the need to combine the appropriate number of 15-s units to generate the correct commercial length and gather together enough of these combinations to satisfy the needed gross impressions (number of people expected to see the commercial) within a particular demographic category. The seller imposes a minimum reservation price on the aggregate collection of goods. This means that the sum of the bids received from winning bidders must exceed the seller’s value for all the units allocated. Because the reservation price constraint looks only at the aggregate level and not the individual bid, freeloaders are allowed as surplus from high paying bidders subsidize others who are allocated goods worth more than they bid. This characteristic is reflected in our data.

The bidding process as described above yields accepted bids for bundles of commercial slots on television shows. The heuristic winner determination procedure documented in [13] provides near optimal winner determinations. The allocation assigns the available commercial slots to the winning bidders taking into account various constraints that are imposed by the bidders and domain environment. In addition, the seller has requested that the collection of slots be sold at or above an aggregate reservation price that is set such that it is a percentage of the suggested list price published on the rate cards. Rate cards, specifying the amount that each show is expected to sell for are common in this industry. However, it is also common knowledge that the cost to the buyer for any show is generally discounted from the published rate.

The inputs to the Gibbs Sampling simulation were the known bundles allocated to the winning bidders in the final round of a combinatorial auction $( K _ { i , j } )$ along with the associated bids $( Y _ { i } )$ for each bidder i and the suggested list prices $( Z _ { j } )$ . As seen from Table 1 of Appendix A the matrix of $K _ { i , j } ^ { \phantom { } } \mathrm { { s } }$ is sparse in that there are many zeros because an individual bidder receives units in only one, two or a few shows.

Although we chose to use data from the final allocation, we could have chosen any intermediate round in the iterative auction. The simulation allows us to determine the posterior distributions of all the unknown quantities. One replication of the simulation explored each of the parameters to be estimated. These parameters included the market influenced unit value for each of the 24 shows $( \phi _ { j } )$ , the profit/loss for each bidder $( \boldsymbol { p } _ { i } )$ and the variance of the bids and unit prices $( \sigma ^ { 2 }$ and $\sigma _ { \phi } ^ { ~ 2 } )$ . For the data presented in the paper we have 130 accepted bids so I=130. We ran 6000 replications and discarded the first 2000 as transient.

<table><tr><td colspan="2">PHI10</td></tr><tr><td>Mean</td><td>35.75355</td></tr><tr><td>Standard Error</td><td>0.051181</td></tr><tr><td>Median</td><td>35.61399</td></tr><tr><td>Mode</td><td>31.952</td></tr><tr><td>Standard Deviation</td><td>3.236995</td></tr><tr><td>Sample Variance</td><td>10.47813</td></tr><tr><td>Kurtosis</td><td>0.099836</td></tr><tr><td>Skewness</td><td>0.38593</td></tr><tr><td>Range</td><td>19.29997</td></tr><tr><td>Minimum</td><td>27.4763</td></tr><tr><td>Maximum</td><td>46.77627</td></tr><tr><td>Sum</td><td>143014.2</td></tr><tr><td>Count</td><td>4000</td></tr></table>

The resulting empirical distribution represents the joint posterior distribution on all unknowns from which we extracted the marginal distributions for the estimated parameters. Detailed results are presented in the next section.

## 3. Results

An analysis of Gibbs Sampler results gives rich information that can be used to discover the market influenced price distribution at the unit level. From the marginal posterior distribution we are able extract summary statistics and generate easy to interpret histograms for each of the unknown parameters. In addition we are able to find from the joint posterior distribution patterns, such as correlations, that depict complementarities between products (in our case television shows).

## 3.1. Price distribution

Price discovery at the unit level is accomplished by looking at the posterior marginal distribution for each $\phi _ { j }$ . As indicated earlier, there may not be one single equilibrium price of an individual product sold in a bundle and the posterior marginal distribution for $\phi _ { j }$ indicates that allocation. A bidder can then use this posterior distribution represented by the summary statistics and/or histogram as shown in Fig. 1 to assist in determining her bid in an iterative auction. This distribution represents the common value component of the bid and closely mirrors the seller’s posted list price.

![](/api/attachments/X5RSQ8PG/fulltext/images/aea136495890e5b3cdcc7c4808593c3dab14c6aa5d0ce26a12b7c9007ee876c6.jpg)  
Fig. 1. Example of summary statistics and histogram representing the price distribution for show 10.

Reservation VS Gibbs  
![](/api/attachments/X5RSQ8PG/fulltext/images/ef7bb44181f1787c3a0fb09667b4120503485b6582c067e962b19f367ead74aa.jpg)  
Fig. 2. Comparison of Gibbs Show Prices and the Seller’s Reservation Price.

The seller can also use the unit price information to confirm or modify his published list prices. For example, the seller may compare the average unit price that is generated from the simulation to the existing list price to see if they are over or underestimating the buyer’s value of a good, see Fig. 2. The ability to obtain unit prices from the bundled allocations provides insight to the marginal contribution of each product that is vital to product lifecycle decision making.

![](/api/attachments/X5RSQ8PG/fulltext/images/2cd1b21ea2e25cd593169712ed99ec5f205612b828714eb25d8c868ce89e9972.jpg)  
Fig. 3. Histogram showing the distribution of the list price adjustment factor.

## 3.2. List price adjustment factor

The simulation also provides insight into the discount to the posted list price that the market will bear. This parameter, $\beta ,$ can be used by the seller to establish his reservation prices. The discount, known to the seller, for the auction from which we acquired our data was 45%. As you can tell by Fig. 3, the seller could conceivably reduce the discount to the mean of 43%.

## 3.3. Profit analysis

The distribution of the profit/loss attributed to each winning bidder was also estimated. The reservation requirement for the auction we studied was at the aggregate level requiring the sum of the winning bid amounts to exceed the reservation value of the total units allocated. Therefore freeloading was allowed, as bidders who paid more than the reservation requirement subsidized unprofitable allocations. The simulation results for the distribution of profit, $p _ { i } ,$ gives the seller insight into the contributions of the individual winning bidders. Summary statistics are shown in Fig. 4 for two of the winning bidders. Not only can the profit and loss from each bidder be determined but also a bidder’s price flexibility can be assessed by looking at the corresponding standard deviation. This flexibility can be identified as the private value component of the bid. For example, if the standard deviation is large on a specific $p _ { i }$ it would indicate that bidder has a wider range of bids to offer.

<table><tr><td colspan="2">PROFIT(1)</td><td colspan="2">PROFIT(130)</td></tr><tr><td>Mean</td><td>68.41768</td><td>Mean</td><td>-45.5081</td></tr><tr><td>Standard Error</td><td>0.112097</td><td>Standard Error</td><td>0.119025</td></tr><tr><td>Median</td><td>68.53649</td><td>Median</td><td>-45.3781</td></tr><tr><td>Standard Deviation</td><td>7.089627</td><td>Standard Deviation</td><td>7.527797</td></tr><tr><td>Sample Variance</td><td>50.26281</td><td>Sample Variance</td><td>56.66773</td></tr><tr><td>Kurtosis</td><td>-0.25559</td><td>Kurtosis</td><td>0.2911</td></tr><tr><td>Skewness</td><td>-0.11093</td><td>Skewness</td><td>0.059642</td></tr><tr><td>Range</td><td>49.31458</td><td>Range</td><td>61.12447</td></tr><tr><td>Minimum</td><td>46.76643</td><td>Minimum</td><td>-76.0945</td></tr><tr><td>Maximum</td><td>96.08101</td><td>Maximum</td><td>-14.9701</td></tr><tr><td>Sum</td><td>273670.7</td><td>Sum</td><td>-182033</td></tr><tr><td>Count</td><td>4000</td><td>Count</td><td>4000</td></tr></table>

Fig. 4. Examples of the profit (loss) statistics for the winning bidders.

## 3.4. Correlations

The correlation matrix of the prices shown in Fig. 5 gives the auctioneer information regarding the relationship between the products being sold in bundles. The ability to identify complements and substitutes could be used by the seller when deciding how to bundle items should he want to sell the products in other markets where the products are not bundled dynamically. In Fig. 5 we have identified a few shows with large and small correlations. We can interpret that those with correlation coefficients greater than 0.5 as complementary goods while correlation coefficients less than -0.5 may be thought of as substitutes.

![](/api/attachments/X5RSQ8PG/fulltext/images/0cf48788ca1284023febbd494df47df22c28fdcb0ede26940ef1d4bcf3a050cd.jpg)  
Fig. 5. Correlation matrix of the prices of shows describing the relationships between shows.

## 3.5. Computation time required

To be applicable to a real time auction environment the solution methodology must be able to produce results in real time. The problem we investigated consisted of 3282 known quantities and 157 unknown parameters. Simulating the 6000 replications over these parameters took less than a minute on a moderate to slow computer making this technique applicable to real time mechanisms for realistically large problems like the one investigated in this study.

## 4. Individual bidder strategy

The purpose of this section is to describe in greater detail how the complete information from the Gibbs Sampler can be used by bidders to develop their next bid value for a specific bundle of goods. If no information is available regarding the value of a desired bundle (i.e. no winning bundle of the exact composition from a previous round) this process can be used. Obviously, bid information from previous rounds would be used if available. However, this method would still provide helpful information to assess the amount to increment the previous known bid. From the output of the Gibbs Sampler we have the distribution of the $\phi ^ { \ast } \mathrm { . }$ . Also we have the posterior distributions of every profit, $p _ { i } ,$ associated with each bid. However, we do not have the profit associated with the individual unit prices.

Using some simplifying assumptions we allocate the distribution of bid profits to the unit prices and thereby are able to report a distribution for the bid on a new bundle. An example of this procedure is included in Appendix B.

The situation is that a bidder wishes to use the existing Gibbs output to submit a new bundled bid for the next round. The new bundled bid is designated $B ^ { * }$

$$
B ^ {*} = \sum_ {j = 1} ^ {J} K _ {j} ^ {*} S _ {j}\tag{16}
$$

where $K _ { j } ^ { * }$ =number of units of product j in the bid, $S _ { j } { = }$ =the bid amount associated with a single unit of product j.

The value, $S _ { j } ,$ includes the unit price, $\phi _ { j }$ , plus an allocated profit which we designate as ${ p } _ { j } ^ { * }$ , so

$$
S _ {j} = \phi_ {j} + p _ {j} ^ {*},\tag{17}
$$

We already have the posterior distribution of $\phi _ { j }$ . The following development will provide the distribution of $\dot { p } _ { j } ^ { * }$ .

Define

$$
J ^ {*} = \left\{j: K _ {j} ^ {*} 0 \right\}\tag{18}
$$

Thus $J ^ { * }$ is the set of all $j ^ { \circ } \mathbf { s }$ representing the products that are included in the new bundle.

For every $j { \in } J ^ { * }$ let,

$$
\begin{array}{r l} I _ {j} ^ {*} & = \left\{i: \text { The   } I \text { th   bid   that   contains   product   } j \text {   from   the   last   round. } \right\} \end{array}
$$

For every $i { \in } I _ { j } ^ { * }$ we have a profit, $p _ { i } ,$ , and we know the distribution of these profits from the output of the Gibbs Sampler. We assume that profit, can be divided, according to the bid bundle, between the products that comprised the bid. That is,

$$
p _ {i} = \sum_ {j = 1} ^ {J} K _ {i j} p _ {i j} ^ {\prime},\tag{19}
$$

where the $K _ { i j } { } ^ { \circ } \mathrm { s }$ are the number of units bidder i was allocated of product j from the last round and the $p _ { i j } ^ { \prime }$ is the profit from bidder i allocated to a single unit of product j.

Note that both $p _ { i }$ and the $p _ { i j } ^ { \prime \prime } \mathbf { s }$ are random variables. For a given i we assume that the $p _ { i j } ^ { \prime } \mathbf { \hat { s } }$ are identically distributed and independent for those j’s included in the ith bid.

This structure with the independent and identically distributed assumption will be used to determine the mean and variance of the individual $p _ { i j } ^ { \prime \prime } \mathrm { s }$ enroute to the construction of $S _ { j }$ in Eq. (17). However, there are usually multiple values of $\dot { p } _ { i j } ^ { \prime }$ that must be considered, one for every $i \in I _ { j } ^ { * }$

Define $N _ { j }$ to be the cardinality of $\Gamma _ { j } ^ { * } ;$ that is $N _ { j }$ is the number of bids in the last round that included product j. We want to construct $p j ^ { * }$ from its $N _ { j }$ components, designated $p _ { i j } ^ { \prime } .$ . At first thought one might want to take the average of these quantities but that would result in the variance of the $p _ { j } ^ { * } \mathrm { { s } }$ being smaller than the average variance of its components by a factor of $1 / N _ { j }$ We want the variance of $p _ { j } ^ { * }$ to be the average variance of its components.

Let $\mu _ { i j }$ and $\sigma _ { i j } ^ { 2 }$ be the mean and variance of $\dot { p } _ { i j }$ and let

$$
\sigma_ {\bullet j} ^ {2} = \sum_ {i \in I _ {j} ^ {*}} \sigma_ {i j} ^ {2}\tag{20}
$$

then we define $p _ { j } ^ { * }$ as follows:

$$
p _ {j} ^ {*} = \sum_ {i \in I _ {j} ^ {*}} \frac {\sigma_ {\bullet j}}{N _ {j} \sigma_ {i j}} p _ {i j} ^ {\prime}.\tag{21}
$$

Therefore, the mean and variance of ${ p } _ { j } ^ { * }$ will be

Mean of $p _ { j } ^ { * } = \sum _ { i \varepsilon I _ { j } ^ { * } } \frac { \sigma _ { j } } { N _ { j } \sigma _ { i j } } \mu _ { i j } ,$

$$
\text { Variance   of } p _ {j} ^ {*} = \frac {\sum_ {i \in I _ {j} ^ {*}} \sigma_ {i j} ^ {2}}{N _ {j}}\tag{22}
$$

ð ÞThe average of the component variances :

ð23Þ

The variance of $\dot { p } _ { j } ^ { * }$ is as prescribed, the average of the variances of the components. The mean of $p _ { j } ^ { * }$ is not the average of the means of the components but rather it is a weighted mean in which the weights are inversely proportional to the corresponding standard deviations. This is a good property in that those means with a large standard deviation will be weighted less.

The procedure of finding the distribution of $p _ { j } ^ { * }$ requires that first we find the component distributions of $\dot { p } _ { i j } ^ { \prime }$ from Eq. (19) and substitute them into Eq. (21). In order to do this we will make the simplifying assumption that all quantities have a normal distribution and therefore we only have to work with the means and variances.

We know the mean and variance of $p _ { i }$ from the output of the Gibbs Sampler. And since we have assumed that the $p _ { i j } ^ { \prime } \mathbf { \bar { s } }$ are identically distributed and independent we have

$$
\mu_ {i j} = \frac {\text { Mean   of   profit   (i) }}{\sum_ {j = 1} ^ {J} K _ {i j}},\tag{24}
$$

$$
\sigma_ {i j} ^ {2} = \frac {\text { Variance   of   profit(i) }}{\sum_ {j = 1} ^ {J} K _ {i j} ^ {2}}.\tag{25}
$$

These values for $\mu _ { i j }$ and $\mathrm { \sigma } _ { i j } ^ { 2 }$ can be substituted into Eqs. (22) and (23) to find the mean and variance of $p _ { j } ^ { * }$

We can determine our bidding strategy using this distribution on the bid amount which includes both unit price and allocated profit. For example, one could assume the strategy of biding the 75th percentile that is generated from the price distribution for the desired bundle. As this demonstrates, the complete information provided by the Gibbs Sampler can be very useful in building a bidding strategy for the next round of bids. The Gibbs Sampler data provided gives the market influenced unit price at the end of each round providing the bidder with signal information regarding her opponent’s value of the individual unit. She can use this information coupled with the profit on the units to adjust her subsequent bids. The above procedure can be provided as a service to the bidder or used internally to generate a recommended bid to returning bidders.

## 5. Summary and managerial implications

This paper presents a technique to facilitate a form of price discovery in combinatorial auctions where, until now, individual item values were concealed in the formation of bundles. Applying Gibbs Sampling within the context of Bayesian estimation, to a bundled allocation from a combinatorial auction we were able to extract not only market influenced individual item price distributions but other interesting characteristics. From the distributions we are able to provide signal information to bidders in iterative auctions in the form of unit level price recommendations and we presented a formulation to develop recommendations for reentering bids on bundles that reflect market conditions. In addition to providing bidder information the results of the Gibbs Sampler provide information for managerial decision making regarding individual items. The seller can also discover the profit and loss attributable to any particular bidder that can be used for bidder profiling and the identification of freeloaders. An analysis of the correlations between units identifies complements and substitute goods. The auctioneer can also assess the data provided from the Gibbs sampler to make adjustments to the auction on the fly. Although the possibilities are limitless, one way for the auctioneer to exploit this information would be to evaluate the factor $\beta$ of suggested list prices $Z _ { j }$ to determine if more or less products should be offered for sale. Since $\beta$ indicates the general deviation from the posted prices, a large positive number would indicate a higher than expected return suggesting that demand may be greater than anticipated. We have described some, but not all, of the insights that can be discovered when applying Gibbs Sampling to a combinatorial auction allocation.

<table><tr><td colspan="27">Allocation</td></tr><tr><td>Bid ID</td><td>BID $</td><td>K1</td><td>K2</td><td>K3</td><td>K4</td><td>K5</td><td>K6</td><td>K7</td><td>K8</td><td>K9</td><td>K10</td><td>K11</td><td>K12</td><td>K13</td><td>K14</td><td>K15</td><td>K16</td><td>K17</td><td>K18</td><td>K19</td><td>K20</td><td>K21</td><td>K22</td><td>K23</td><td>K24</td><td></td></tr><tr><td>1</td><td>134.528</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>2</td><td>0</td><td></td></tr><tr><td>2</td><td>92.8369</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td></td></tr><tr><td>3</td><td>92.1914</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td></td></tr><tr><td>4</td><td>114.834</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td></td></tr><tr><td>5</td><td>174.576</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>0</td><td></td></tr><tr><td>6</td><td>161.751</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>2</td><td>0</td><td></td></tr><tr><td>7</td><td>269.866</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>2</td><td>2</td><td></td></tr><tr><td>8</td><td>158.265</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>2</td><td>0</td><td></td></tr><tr><td>9</td><td>84.6014</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td></td></tr><tr><td>10</td><td>190.384</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>2</td><td></td></tr><tr><td>11</td><td>243.943</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>12</td><td>115.752</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>13</td><td>101.134</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td></td></tr><tr><td>14</td><td>181.008</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>2</td><td></td></tr><tr><td>15</td><td>165.927</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>2</td><td></td></tr><tr><td>16</td><td>242.309</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>2</td><td>2</td><td></td></tr><tr><td>17</td><td>136.616</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>2</td><td></td></tr><tr><td>18</td><td>197.008</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td></td></tr><tr><td>19</td><td>155.149</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>20</td><td>84.8318</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td></td></tr><tr><td>21</td><td>236.754</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td></td></tr><tr><td>22</td><td>151.03</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td></td></tr><tr><td>23</td><td>192.704</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td></td></tr><tr><td>24</td><td>64.5929</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>25</td><td>47.0918</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>26</td><td>36.6372</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td></td></tr><tr><td>27</td><td>197.092</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>2</td><td></td></tr><tr><td>28</td><td>398.253</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>29</td><td>205.14</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>30</td><td>273.423</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>2</td><td>1</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>31</td><td>143.413</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>32</td><td>356.081</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>0</td><td>0</td><td>0</td><td>3</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>33</td><td>155.99</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>34</td><td>208.606</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>35</td><td>298.821</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td></td></tr><tr><td>36</td><td>191.128</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>2</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>37</td><td>108.035</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td></td></tr><tr><td>38</td><td>89.523</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr></table>

J.L. Jones, R.W. Andrews / Decision Support Systems 42 (2006) 958–974 968

$$
\begin{array} { r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r l r } & 3 9 & 1 3 2 . 8 8 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ & 4 0 & 1 3 0 . 7 6 7 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ & 4 1 & 8 8 . 5 2 6 9 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ & 4 2 & 2 1 8 . 7 6 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 2 & 1 & 0 & 0 & 2 & 2 & 2 \\ & 4 3 & \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf{ ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \textbf { ~ } \end{array}
$$

Appendix A (continued)

<table><tr><td colspan="27">Allocation</td></tr><tr><td>Bid ID</td><td>BID $</td><td>K1</td><td>K2</td><td>K3</td><td>K4</td><td>K5</td><td>K6</td><td>K7</td><td>K8</td><td>K9</td><td>K10</td><td>K11</td><td>K12</td><td>K13</td><td>K14</td><td>K15</td><td>K16</td><td>K17</td><td>K18</td><td>K19</td><td>K20</td><td>K21</td><td>K22</td><td>K23</td><td>K24</td><td></td></tr><tr><td>84</td><td>222.172</td><td>0</td><td>0</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>85</td><td>284.736</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>86</td><td>220.189</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>87</td><td>58.7856</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>88</td><td>159.393</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>89</td><td>441.69</td><td>0</td><td>4</td><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>90</td><td>176.283</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>91</td><td>416.005</td><td>2</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>92</td><td>380.659</td><td>0</td><td>0</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>93</td><td>292.872</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>94</td><td>288.575</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>95</td><td>137.642</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>96</td><td>53.3021</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>97</td><td>312.139</td><td>0</td><td>0</td><td>2</td><td>0</td><td>2</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>98</td><td>93.0517</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>99</td><td>174.395</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>100</td><td>257.231</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>101</td><td>319.363</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>102</td><td>52.7159</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>103</td><td>655.336</td><td>0</td><td>2</td><td>0</td><td>0</td><td>2</td><td>0</td><td>2</td><td>4</td><td>0</td><td>0</td><td>0</td><td>4</td><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>104</td><td>109.78</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>105</td><td>193.364</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>106</td><td>193.031</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>107</td><td>103.774</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>108</td><td>254.01</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>109</td><td>85.7014</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>110</td><td>54.2599</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>111</td><td>174.554</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>112</td><td>280.035</td><td>0</td><td>0</td><td>0</td><td>2</td><td>2</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>113</td><td>51.6286</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>114</td><td>183.003</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>115</td><td>399.842</td><td>0</td><td>2</td><td>0</td><td>4</td><td>2</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr></table>

J.L. Jones, R.W. Andrews / Decision Support Systems 42 (2006) 958–974 970  
(continued on next page)

Table A1: Allocation from combinatorial auction

Appendix A
(continued)

<table><tr><td>Bid ID</td><td>BID $</td><td>K1</td><td>K2</td><td>K3</td><td>K4</td><td>K5</td><td>K6</td><td>K7</td><td>K8</td><td>K9</td><td>K10</td><td>K11</td><td>K12</td><td>K13</td><td>K14</td><td>K15</td><td>K16</td><td>K17</td><td>K18</td><td>K19</td><td>K20</td><td>K21</td><td>K22</td><td>K23</td><td>K24</td></tr><tr><td>116</td><td>96.2415</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>117</td><td>322.421</td><td>0</td><td>2</td><td>0</td><td>0</td><td>1</td><td>0</td><td>2</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>118</td><td>74.0892</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>119</td><td>182.745</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>120</td><td>111.009</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>121</td><td>101.086</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>122</td><td>52.0892</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>123</td><td>99.1852</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>124</td><td>274.891</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>125</td><td>242.012</td><td>0</td><td>3</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>126</td><td>103.804</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>127</td><td>103.429</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>128</td><td>317.871</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>129</td><td>92.5249</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>130</td><td>138.749</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

## Appendix B. Bundle price formulation example

To clarify the procedure used to reveal the price distribution for a desired bundle of goods we present the following example. We show the steps to determine.

The value of $B ^ { * } ,$ a bundled bid that includes 3 units of Show 7, a single unit of Show 12 and 2 units in show 14. The formulation for the bundle we will price is:

$$
B ^ {*} = 3 S _ {7} + S _ {1 2} + 2 S _ {1 4}.
$$

Therefore the set of all shows included in the example bundle is:

$$
J ^ {*} = \{7, 1 2, 1 4 \}.
$$

We must first determine which winning bidders were allocated these shows in the last round. Referring to Table 1 of Appendix A we see that the $I _ { j } { } ^ { * } { } ^ { * } { } _ { \mathrm { : } }$ the sets of all bids containing show j are:

I<sup>4</sup> ¼ f g103; 111; 112; 117; 119; 125; 127; 128; 130 ; indicating that bidders 103; 111; 112 . . . have been allocated at least one unit in Show 7 in the previous round: We generate the set of bidderswith Show 12 and 14 in a similar fashion::

$$
I _ {1 2} ^ {*} = \{8 6, 9 1, 9 3, 9 8, 1 0 0, 1 0 2, 1 0 3, 1 0 7, 1 0 8 \}
$$

$$
I _ {1 4} ^ {*} = \left\{ \begin{array}{l} 1 1, 1 8, 1 9, 2 3, 2 8, 3 0, 3 5, 3 6, 3 7, 3 9, 4 1, 4 4, 4 5, 5 1, \\ 5 4, 5 8, 5 9, 6 1, 6 3, 6 6, 6 7, 6 9, 7 0, 7 1, 7 3, 7 6, 8 0 \end{array} \right\}
$$

For each of the bids containing the shows of interest we have a profit, $p _ { i } .$ For example, consider $i { = } 1 0 3 { \in } I _ { 7 } ^ { * }$ . Then by inspecting the 103rd bid from the last round Eq. (19) becomes

$$
\begin{array}{r l} p _ {1 0 3} & = 2 \dot {p} _ {1 0 3, 2} + 2 \dot {p} _ {1 0 3, 5} + 2 \dot {p} _ {1 0 3, 7} + 4 \dot {p} _ {1 0 3, 8} \\ & + 4 \dot {p} _ {1 0 3, 1 2} + 4 \dot {p} _ {1 0 3, 1 3} \end{array}
$$

In our example for $j { = } 7$ we have $p _ { 1 0 3 , 7 } ^ { \prime } , p _ { 1 1 1 , 7 } ^ { \prime } , p _ { 1 1 2 , 7 } ^ { \prime } ,$ $p _ { 1 0 7 , 7 } ^ { \prime }$ , p<sub>119,7</sub>V , p<sub>125,7</sub>V , p<sub>127,7</sub>V , p<sub>128,7</sub>V , and $p _ { 1 3 0 , 7 } ^ { \prime }$ making $N _ { 7 } { = } 9 .$

We will now continue our example to find the recommended bid distribution of $B ^ { * }$ . From the output of the Gibbs Sampler it is easy to find the means and variances for all bid profits from the last bid that are associated with the new bid $B ^ { * }$ . There are 44 bids that included either Show (7), Show (12) or Show (14). Table B1 gives these values and the relationship to the associated Show ( j).

The values of $\textstyle \sum _ { j = 1 } ^ { J } K _ { i j }$ and $\textstyle \sum _ { j = 1 } ^ { J } K _ { i j } ^ { 2 }$ are also given in Table B1. Using these values in Eqs.

Table B1  
Mean and variance of bid profits

<table><tr><td>Bid number (i)</td><td>Associated show (j)</td><td>Mean: profit (i)</td><td>Var: profit (i)</td><td>Sum [K(ij)]</td><td>Sum [K(ij) $^2$ ]</td></tr><tr><td>11</td><td>14</td><td>106.79</td><td>211.60</td><td>6</td><td>18</td></tr><tr><td>18</td><td>14</td><td>74.10</td><td>120.78</td><td>4</td><td>8</td></tr><tr><td>19</td><td>14</td><td>59.17</td><td>50.46</td><td>4</td><td>4</td></tr><tr><td>23</td><td>14</td><td>69.87</td><td>121.39</td><td>4</td><td>8</td></tr><tr><td>28</td><td>14</td><td>127.26</td><td>357.56</td><td>11</td><td>41</td></tr><tr><td>30</td><td>14</td><td>72.15</td><td>185.05</td><td>7</td><td>11</td></tr><tr><td>35</td><td>14</td><td>90.17</td><td>168.25</td><td>6</td><td>10</td></tr><tr><td>36</td><td>14</td><td>64.46</td><td>60.96</td><td>5</td><td>7</td></tr><tr><td>37</td><td>14</td><td>21.81</td><td>73.82</td><td>3</td><td>3</td></tr><tr><td>39</td><td>14</td><td>39.51</td><td>51.32</td><td>3</td><td>5</td></tr><tr><td>41</td><td>14</td><td>10.24</td><td>27.32</td><td>2</td><td>2</td></tr><tr><td>44</td><td>14</td><td>59.61</td><td>350.49</td><td>8</td><td>16</td></tr><tr><td>45</td><td>14</td><td>37.89</td><td>49.61</td><td>3</td><td>5</td></tr><tr><td>51</td><td>14</td><td>17.00</td><td>52.34</td><td>3</td><td>3</td></tr><tr><td>54</td><td>14</td><td>21.43</td><td>52.65</td><td>3</td><td>3</td></tr><tr><td>58</td><td>14</td><td>27.26</td><td>74.26</td><td>5</td><td>5</td></tr><tr><td>59</td><td>14</td><td>112.22</td><td>189.19</td><td>9</td><td>29</td></tr><tr><td>61</td><td>14</td><td>72.04</td><td>256.72</td><td>8</td><td>16</td></tr><tr><td>63</td><td>14</td><td>52.48</td><td>88.72</td><td>7</td><td>7</td></tr><tr><td>66</td><td>14</td><td>33.51</td><td>91.31</td><td>6</td><td>12</td></tr><tr><td>67</td><td>14</td><td>51.35</td><td>84.71</td><td>5</td><td>9</td></tr><tr><td>69</td><td>14</td><td>27.38</td><td>100.05</td><td>5</td><td>5</td></tr><tr><td>70</td><td>14</td><td>17.29</td><td>23.75</td><td>2</td><td>2</td></tr><tr><td>71</td><td>14</td><td>17.23</td><td>23.01</td><td>2</td><td>2</td></tr><tr><td>73</td><td>14</td><td>18.68</td><td>115.27</td><td>5</td><td>9</td></tr><tr><td>76</td><td>14</td><td>30.33</td><td>225.78</td><td>8</td><td>14</td></tr><tr><td>80</td><td>14</td><td>95.46</td><td>445.01</td><td>10</td><td>36</td></tr><tr><td>86</td><td>12</td><td>4.20</td><td>121.05</td><td>6</td><td>6</td></tr><tr><td>91</td><td>12</td><td>15.37</td><td>515.57</td><td>10</td><td>20</td></tr><tr><td>93</td><td>12</td><td>-29.02</td><td>216.69</td><td>8</td><td>12</td></tr><tr><td>98</td><td>12</td><td>-17.93</td><td>53.49</td><td>3</td><td>3</td></tr><tr><td>100</td><td>12</td><td>5.13</td><td>201.16</td><td>6</td><td>12</td></tr><tr><td>102</td><td>12</td><td>-9.19</td><td>126.06</td><td>2</td><td>4</td></tr><tr><td>103</td><td>7,12</td><td>-127.03</td><td>1029.87</td><td>18</td><td>60</td></tr><tr><td>107</td><td>12,12</td><td>-8.26</td><td>66.63</td><td>3</td><td>3</td></tr><tr><td>108</td><td>7</td><td>-26.34</td><td>103.98</td><td>6</td><td>6</td></tr><tr><td>111</td><td>7</td><td>-49.39</td><td>101.32</td><td>4</td><td>4</td></tr><tr><td>112</td><td>7</td><td>-113.17</td><td>166.32</td><td>8</td><td>16</td></tr><tr><td>117</td><td>7</td><td>-49.24</td><td>245.92</td><td>7</td><td>11</td></tr><tr><td>119</td><td>7</td><td>-52.60</td><td>119.74</td><td>4</td><td>8</td></tr><tr><td>125</td><td>7</td><td>-70.90</td><td>178.888</td><td>5</td><td>11</td></tr><tr><td>127</td><td>7</td><td>-11.13</td><td>69.10</td><td>2</td><td>4</td></tr><tr><td>128</td><td>7</td><td>-50.78</td><td>197.62</td><td>6</td><td>12</td></tr><tr><td>130</td><td>7</td><td>-45.51</td><td>56.67</td><td>3</td><td>3</td></tr></table>

Table B2  
Mean and variance of profit components

<table><tr><td>Bid number (i)</td><td>Associated show (j)</td><td> $\mu$  (ij)</td><td> $\sigma^{2}$  (ij)</td></tr><tr><td>11</td><td>14</td><td>17.80</td><td>11.76</td></tr><tr><td>18</td><td>14</td><td>18.52</td><td>15.10</td></tr><tr><td>19</td><td>14</td><td>14.79</td><td>12.61</td></tr><tr><td>23</td><td>14</td><td>17.47</td><td>15.17</td></tr><tr><td>28</td><td>14</td><td>11.57</td><td>8.72</td></tr><tr><td>30</td><td>14</td><td>10.31</td><td>16.82</td></tr><tr><td>35</td><td>14</td><td>15.03</td><td>16.82</td></tr><tr><td>36</td><td>14</td><td>12.89</td><td>8.71</td></tr><tr><td>37</td><td>14</td><td>7.27</td><td>24.61</td></tr><tr><td>39</td><td>14</td><td>13.17</td><td>10.26</td></tr><tr><td>41</td><td>14</td><td>5.12</td><td>13.66</td></tr><tr><td>44</td><td>14</td><td>7.45</td><td>21.91</td></tr><tr><td>45</td><td>14</td><td>12.63</td><td>9.92</td></tr><tr><td>51</td><td>14</td><td>5.67</td><td>17.45</td></tr><tr><td>54</td><td>14</td><td>7.14</td><td>17.55</td></tr><tr><td>58</td><td>14</td><td>5.45</td><td>14.85</td></tr><tr><td>59</td><td>14</td><td>12.47</td><td>6.52</td></tr><tr><td>61</td><td>14</td><td>9.01</td><td>16.05</td></tr><tr><td>63</td><td>14</td><td>7.50</td><td>12.67</td></tr><tr><td>66</td><td>14</td><td>5.58</td><td>7.61</td></tr><tr><td>67</td><td>14</td><td>10.27</td><td>9.41</td></tr><tr><td>69</td><td>14</td><td>5.48</td><td>20.01</td></tr><tr><td>70</td><td>14</td><td>8.65</td><td>11.87</td></tr><tr><td>71</td><td>14</td><td>8.61</td><td>11.51</td></tr><tr><td>73</td><td>14</td><td>3.74</td><td>12.81</td></tr><tr><td>76</td><td>14</td><td>3.79</td><td>16.13</td></tr><tr><td>80</td><td>14</td><td>9.55</td><td>12.36</td></tr><tr><td>86</td><td>12</td><td>0.70</td><td>20.18</td></tr><tr><td>91</td><td>12</td><td>1.54</td><td>25.78</td></tr><tr><td>93</td><td>12</td><td>-3.63</td><td>18.06</td></tr><tr><td>98</td><td>12</td><td>-5.98</td><td>17.83</td></tr><tr><td>100</td><td>12</td><td>0.86</td><td>16.76</td></tr><tr><td>102</td><td>12</td><td>-4.60</td><td>31.52</td></tr><tr><td>103</td><td>7,12</td><td>-7.06</td><td>17.16</td></tr><tr><td>107</td><td>12</td><td>-2.75</td><td>22.21</td></tr><tr><td>108</td><td>12</td><td>-4.39</td><td>17.33</td></tr><tr><td>111</td><td>7</td><td>-12.35</td><td>25.33</td></tr><tr><td>112</td><td>7</td><td>-14.15</td><td>10.39</td></tr><tr><td>117</td><td>7</td><td>-7.03</td><td>22.36</td></tr><tr><td>119</td><td>7</td><td>-13.15</td><td>14.97</td></tr><tr><td>125</td><td>7</td><td>-14.18</td><td>16.26</td></tr><tr><td>127</td><td>7</td><td>-5.57</td><td>17.27</td></tr><tr><td>128</td><td>7</td><td>-8.46</td><td>16.47</td></tr><tr><td>130</td><td>7</td><td>-15.17</td><td>18.89</td></tr></table>

(24) and (25) we obtain the mean and variance of the $p _ { i j } ^ { \prime } \mathbf { \bar { s } } .$

These values are presented in Table B2. For j=7, 12, and 14 we use Table B2 to calculate

$$
\sigma_ {\bullet 7} ^ {2} = \sum_ {i \in I _ {7} ^ {*}} \sigma_ {i 7} ^ {2} = 1 5 9. 1 1,
$$

$$
\sigma_ {\bullet 1 2} ^ {2} = \sum_ {i \in I _ {1 2} ^ {*}} \sigma_ {i 1 2} ^ {2} = 1 8 6. 8 2,
$$

$$
\sigma_ {\bullet 1 4} ^ {2} = \sum_ {i \in I _ {1 4} ^ {*}} \sigma_ {i 1 4} ^ {2} = 3 7 2. 8 8.
$$

Using these values and the means and variances given in Table B2 we calculate the means and variances of the distribution of $p _ { j } ^ { * } \mathrm { ^ { * } s } .$ . They are

<table><tr><td></td><td> $p_{7}^{*}$ </td><td> $p_{12}^{*}$ </td><td> $p_{14}^{*}$ </td></tr><tr><td>Mean</td><td>-33.44</td><td>-8.75</td><td>54.14</td></tr><tr><td>Variance</td><td>17.68</td><td>20.76</td><td>13.81</td></tr></table>

From the output of the Gibbs Sampler we can find the means and variances of the distribution of $\phi _ { j } \mathbf { \bar { s } }$ They are:

<table><tr><td></td><td> $\phi_{7}$ </td><td> $\phi_{12}$ </td><td> $\phi_{14}$ </td></tr><tr><td>Mean</td><td>57.27</td><td>30.98</td><td>32.15</td></tr><tr><td>Variance</td><td>15.28</td><td>29.25</td><td>10.99</td></tr></table>

We can now find the mean and variance of $B ^ { * }$ the proposed bid.

$$
\begin{array}{r l} \text { Mean   of } B ^ {*} & = 3 (\text { Mean   of } (\phi_ {7} + p _ {7} ^ {*})) \\ & \quad + 1 (\text { Mean   of } (\phi_ {1 2} + p _ {1 2} ^ {*})) \\ & \quad + 3 (\text { Mean   of } (\phi_ {1 4} + p _ {1 4} ^ {*})) \\ & = 2 6 6. 2 5 5 \end{array}
$$

$$
\begin{array}{r l} \text { Var   of } B ^ {*} & = 9 (\text { Var   of } (\phi_ {7} + p _ {7} ^ {*})) \\ & + 1 (\text { Var   of } (\phi_ {1 2} + p _ {1 2} ^ {*})) \\ & + 9 (\text { Var   of } (\phi_ {1 4} + p _ {1 4} ^ {*})) \\ & = 4 4 5. 8 0 \text { so,   S.D.   of } B ^ {*} = 2 1. 1 1 \end{array}
$$

Although the mean and variance could represent any distribution it is common practice to approximate the posterior distribution with the normal distribution based on the central limit theorem of probability. Put in a Bayesian context shows: $\begin{array} { r } { ( \frac { \theta - E ( \theta | y ) } { \sqrt { \nu a r ( \theta | y ) } } | y ) {  } N ( 0 , 1 ) } \end{array}$ [2].

From this construction we know a lot about the possible bids we might submit for this bundle. We now have all the information to generate a distribution of prices for our desired bundle. The bidder can use this distribution information to help generate a new bid dependent on her bidding strategy, the expected strategies of her opponents, and the condition of the auction.

## References

[1] G.M. Allenby, P. Lenk, Reassessing brand loyalty, price sensitivity, and merchandising effects on consumer brand choice, Journal of Business and Economic Statistics 13 (3) (1995) 281–290.

[2] R.W. Andrews, O. Berger, M.H. Smith, Bayesian estimation of manufacturing effects in a fuel economy model, Journal of Applied Econometrics 8 (S) (1993) S5– S18.

[3] R.W. Andrews, M. Rosenberg, P.J. Lenk, A hierarchical Bayesian model for predicting the rate of non-acceptable inpatient hospital utilization, Journal of Business Economics and Statistics 17 (1999) 1 – 8.

[4] C. Beam, A. Segev, Auctions on the Internet: A Field Study; CMIT Working Paper 98-WP-1032, (May, 1998).

[5] S. Bikhchandani, J. Ostroy, The package assignment model, Journal of Economic Theory 107 (2) (2002) 377–406.

[6] G. Casella, E.I. George, Explaining the Gibbs Sampler, The American Statistician 46 (3) (1992) 167 – 174.

[7] C. DeMartini, A. Kwasnica, J. Ledyard, D. Porter, A New and Improved Design for Multi-object Iterative Auctions, Working paper, ICES, George Mason University (2002).

[8] R. Engelbrecht-Wiggins, Auctions and bidding models: a survey, Management Science 26 (2) (1980) 119–142.

[9] B. Eraker, MCMC analysis of diffusion models with application to finance, American Statistical Association Journal of Business and Economic Statistics 19 (2) (2001) 177– 191.

[10] A.E. Gelfand, A.F.M. Smith, Sampling-based approaches to calculating marginal densities, Journal of the American Statistical Association 85 (1990) 398 – 409.

[11] A.E. Gelfand, S.E. Hils, A. Racine-Poon, A.F.M. Smith, Illustration of Bayesian inference in normal data models using Gibbs Sampling, Journal of the American Statistical Association 85 (1990) 972– 985.

[12] W.R. Gilks, S. Richardson, D.J. Spiegelhalter, Markov Chain Monte Carlo in Practice, Chapman and Hall, London UK, 1996.

[13] J.L. Jones, G.J. Koehler, Combinatorial auctions with rulebased bids, Decision Support Systems 34 (1) (2002) 59– 74.

[14] P. Milgrom, Auctions and bidding: a primer, Journal of Economic Perspectives 3 (3) (1989) 3 – 22.

[15] R. O’Neill, P. Sotkiewicz, B. Hobbs, M. Rothkopf, W. Steward Jr., Efficient market-clearing prices in markets with non-

convexities, European Journal of Operational Research (2004) (in press).

[16] D.C. Parks, Iterative Combinatorial Auctions: Achieving Economic and Computational Efficiency, Dissertation in Computer and Information Science, University of Pennsylvania, (2001).

[17] S.J. Rassenti, V.L. Smith, R.L. Bulfin, A combinatorial mechanism for airport time slot allocation, Management Science 44 (8) (1982) 1131 – 1147.

[18] P.R. Wurman, M.P. Wellman, Efficiency and equilibrium in task allocation economies with hierarchical dependencies, Proceeding of the Sixteenth International Joint Conference on Artificial Intelligence (IJCAI 99), Stockholm, Sweden, July 31–August 6 1999.

[19] M. Xia, G.J. Koehler, A.B. Whinston, Pricing combinatorial auctions, European Journal of Operational Research 154 (1) (2004) 251– 270.

Dr. Jones holds a B.S. in Business Administration from the University of Illinois, Chicago (1992) where she majored in Marketing. She received her Ph.D. from the University of Florida<sup>T</sup>s Warrington College of Business in 2000. Dr Jones is currently an Assistant Professor of Information Systems and Decision Sciences at the University of South Florida. Her research interests include electronic commerce, pricing models for information goods and the analysis and design of business systems. She concentrates specifically on electronically mediated auction mechanisms.

Dr. Andrews was an Associate Professor of Statistics and Management Science at the University of Michigan Business School. His academic work focused on statistical quality control, applications of Bayesian statistical analysis, and vehicle fuel economy and emissions. Dr. Andrews passed away while teaching in the Brazil Global MBA program shortly after this paper was finished. He was a great teacher, scholar, and friend. He will be missed.
