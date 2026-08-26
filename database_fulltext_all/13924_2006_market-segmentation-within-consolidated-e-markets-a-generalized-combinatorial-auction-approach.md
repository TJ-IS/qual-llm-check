---
otero_id: 13924
otero_key: "P3C9ZWHJ"
title: "Market Segmentation Within Consolidated E-Markets: A Generalized Combinatorial Auction Approach"
authors: "Joni L. Jones; Robert F. Easley; Gary J. Koehler"
year: "2006"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222230105"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Market Segmentation Within Consolidated E-Markets: A Generalized Combinatorial Auction Approach

Joni L. Jones , Robert F. Easley & Gary J. Koehler

To cite this article: Joni L. Jones , Robert F. Easley & Gary J. Koehler (2006) Market Segmentation Within Consolidated E-Markets: A Generalized Combinatorial Auction Approach, Journal of Management Information Systems, 23:1, 161-182

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222230105

![](/api/attachments/P3C9ZWHJ/fulltext/images/8aede2d571817823fee9d665cefc3b6ea7ffd1ca54dbd54cb29a11f6dfb51757.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/P3C9ZWHJ/fulltext/images/8eb2dc8c1b18d4097eab151a24e0619c2000c2dd0e7efaa6e7f3a9b0636d7915.jpg)

Submit your article to this journal

![](/api/attachments/P3C9ZWHJ/fulltext/images/0dd9339787ed5f8e3324235ecf236680fd7c72ef70e65b04bfd952858786f9fc.jpg)

Article views: 8

![](/api/attachments/P3C9ZWHJ/fulltext/images/4b664ff8e6be38bfa74ae3510817899a8a54883c0194ce384bb3bc15db533bf6.jpg)

View related articles

![](/api/attachments/P3C9ZWHJ/fulltext/images/751e42d507b9cafee0818357e29595dac80a0f0fac7c289eeaa2a19b97dc0a80.jpg)

Citing articles: 1 View citing articles

# Market Segmentation Within Consolidated E-Markets: A Generalized Combinatorial Auction Approach

JONI L. JONES, ROBERT F. EASLEY, AND GARY J. KOEHLER

JONI L. JONES is an Assistant Professor of Information Systems and Decision Sciences at the University of South Florida. Her research interests include electronic commerce, pricing models for information goods, and the analysis and design of business systems. She concentrates specifically on electronically mediated auction and market mechanisms.

ROBERT F. EASLEY is an Associate Professor of Management Information Systems at the Mendoza College of Business of the University of Notre Dame. His research interests include e-commerce with a focus on Internet auctions, recommendation systems, personalization, collaborative technologies, and technology acceptance.

GARY J. KOEHLER is the John B. Higdon Eminent Scholar and Professor of Decision and Information Sciences in the Warrington School of Business at the University of Florida. His research interests include electronic commerce, machine learning, genetic algorithm theory, and topics at the interface of information systems and management science.

ABSTRACT: We analyze an e-market design that allows multiple market segments to be served simultaneously with a single generalized combinatorial auction. The mechanism uses rule-based bids designed to accommodate various kinds of bidders, such as those more sensitive to price or those more restricted in their requirements. We demonstrate experimentally—using agent-based simulation of the actual market for television advertising slots—that the rule-based approach effectively handles the wide range of market segments, while maintaining buyer and seller surplus and efficiently allocating goods.

KEY WORDS AND PHRASES: combinatorial auction, electronic markets, market segmentation.

FOR A NUMBER OF INDUSTRIES, THE ADVANTAGE of e-markets lies not only in the ability to serve a market electronically (often over the Internet) but also in leveraging the accompanying flow of information to enable gains in efficiency or productivity. This potential payoff is especially important in industries with a product that is highly timedependent, such as airlines or television broadcasting. In such industries—where an empty seat or unsold ad slot represents unrecoverable lost opportunity—complex pricing, allocation, and scheduling problems are also rendered more difficult by the number of factors that may enter into a prospective customer’s decision. For example, air travelers vary considerably in the flexibility of their schedule requirements, as do advertisers’ preferences for TV shows and time slots. The pricing aspect of this problem is often addressed by providing a variety of purchase channels, as exemplified by the existence of aftermarkets for unsold advertising slots and airline seats, yet this division of the marketplace impedes the timely flow of information and thus may degrade allocation and scheduling decisions. When an industry’s customer base is diverse, the ability to harness information systems to provide flexible pricing strategies and accurately segment the market is essential to firm profitability and survival [6].

Market segmentation is appealing, as it can increase economic efficiency. Recently, Clemons et al. examined the continued existence of significant price dispersion across online travel agents, and suggest that their “findings of price dispersion are robust to a substantial amount of innovation in price search capability” [7, p. 548]. They further argue that

service differentiation is a key strategic component of online sellers that offer access to heterogeneous goods. While this may appear unusual for markets that should theoretically have greater information transparency, it mirrors behavior in non-electronic markets: By exploiting consumers’ heterogeneity in tastes and uncertainty of vendor quality, vendors can base price competition by segmenting the market. [7, p. 548]

This is especially striking, given that these authors are not even examining the full online market for airline tickets. There is a well-established aftermarket for “lastminute” bookings (e.g., priceline.com) that further differentiates the market on the basis of the willingness of travelers to purchase tickets without knowledge of airline, aircraft, number of connections, exact times, or duration of travel.

Clearly, this desire to continue the nonelectronic tradition of market segmentation in the online world works against the increased transparency many expected in online transactions [4]. It may also, in part, explain the relative paucity of seller-owned e-markets designed to handle transactions centrally. With a simple price-based auction mechanism, a seller that consolidates its buyers in one location clearly cannot differentiate, because these mechanisms do not permit market segmentation in a single auction. What is lacking is a mechanism that serves multiple market segments with different purchaser requirements through a single consolidated e-market.

The strategic value of segmenting the market may appear to work against the consolidation of the market in one auction mechanism. However, when the gains from efficiently segmenting the market in a single auction are sufficient, there can be incentive for all parties to participate in the auction. Achieving such gains is possible with a mechanism that allows both bidders and sellers to specify and alter their requirements, expressed as rules, throughout the auction. These rules dictate constraints on trade-offs, firm requirements, and other considerations. A major difficulty with this approach, as shown in prior literature, is in the winner determination problem [17, 20].

We study a rule-based auction mechanism for which the winner determination problem has been satisfactorily solved [9, 10] for realistically sized problems (our study uses 325 bidders and 527 items). Using an agent-based simulation and an empirical example based on actual television ad slot sales, we establish that the rule-based combinatorial auction mechanism proposed by Jones and Koehler [9] can simultaneously serve all segments of the market—as defined by varying constraints, budgets, and bidding strategies—in a single auction. The auction mechanism is not the focus of this paper—it is described in detail in Jones and Koehler [9, 10]. Nor is the focus on the design of the agent-based simulation—it is a means to an end, permitting us to explore the premise that a single rule-based combinatorial auction can successfully sell to clients with very different demand types, budgets, and bidding strategies while simultaneously solving a difficult capacity allocation problem. Toward this end, we focus on the problem of allocating prime-time television advertising slots among a set of potential customers because of its richness in bidding options and strategies and in the diversity of customer types.

## Multi-Attribute Combinatorial Auction Mechanism

THE MULTI-ATTRIBUTE COMBINATORIAL AUCTION mechanism discussed in this paper allows both the buyers and the seller to impose rules that establish the framework of the auction. The rule-based combinatorial auction, first studied in Jones and Koehler [9], has two unique features: (1) it is not necessary for a bidder to enumerate all possible acceptable combinations of desired goods, as is required in most other auction forms, and (2) the rules are not limited simply to defining the types of acceptable combinations, such as contiguous geographic regions for Federal Communication Commission (FCC) spectrum auctions [8, 13, 14], but may also cover other attributes of the goods or market setting.

The problem of allocating network advertising slots among a set of potential customers is sufficiently complex to merit the use of this multiple-attribute combinatorial auction approach. The television networks have a selection of shows available with a limited set of commercial slots, each with an expected exposure to various demographic groups. This exposure is measured in gross rating points (GRP), where each GRP represents 1 percent of U.S. households. The seller has a set of side constraints, some based on industry norms, concerning the number of similar products that may be advertised in a show or the type of product preferences or prohibitions per show. The buyers want to purchase a certain range of exposure (measured in GRP) for targeted demographics at the best cost per million (CPM) exposures, and may have side constraints concerning lists of desirable shows or other timing or placement requirements.

The seller begins by announcing a structure under which bids are accepted. This could consist of the establishment of seller reservation prices and constraints that enforce industry practices. For example, in the network television scenario, seller rules ensure that all accepted bids meet minimum reservation and commercial length requirements while not exceeding supply on hand, as well as a number of other industry-specific constraints such as protection against adjacent ad placement by a competitor. Bidders submit a set of rules along with the price they would pay for any combination of items satisfying all their accompanying rules. Such rules may require that ads appear in a certain number of shows, that no ads appear in certain other shows, that target demographics are satisfied, and so on. The final allocation is the collection of bids that “maximizes” seller revenue subject to satisfying both the seller framework constraints and all rules associated with the accepted bids. (We note that the winner determination allocation problem is NP-hard but that the solution methodology of Jones and Koehler [10] produces very good allocations though not necessarily provably optimal.)

The introduction of rule-based bids is founded on the idea that the space of feasible bids is better explored by the winner determination process rather than by the bidders themselves. This is because the space of feasible bids is typically exponential in size and the task of both enumerating and physically submitting a set of all feasible (and desirable) bids is impractical for more than trivial problem sizes. By translating the buyers’ descriptions of their ultimate goals into high-level rules that can be submitted as bids to an auction mechanism, the buyers are relieved of the responsibility of analyzing all possible combinations. The complexity of the rules also need not grow as rapidly, in relation to the size of a buyer’s set of feasible bids, as would the set of all possible feasible combinations.

Rules can be easy to state but difficult to enumerate. For example, in the context of the well-known FCC spectrum auctions [8, 13, 14], consider a rule that indicates the buyer is willing to pay \$100,000 for three adjoining FCC spectrum licenses as long as one includes a major city. Suppose Figure 1 depicts the license areas for sale. To comply with the rule stated above, a bidder would need to enumerate all the permissible options such as (1,2,5), (2,3,5), (2,4,5), (2,6,5), (3,6,5), and so on. Performing such an enumeration simply may not be practical for many of the complexities of actual business situations. Instead, the rules can be directly incorporated as constraints on a bidder’s feasible bids in a mixed-integer program representing the winner determination problem. To make this more precise, let $x _ { i , j , k }$ be a zero-one variable, which, when equal to one, means that bidder i gets area $( j , k )$ where j is the row and k the column of the won area in Figure 1. So the constraint

$$
\sum_ {j, k} x _ {i, j, k} = 3 x _ {i, 2, 2}
$$

implements this rule in the winner determination problem. (Either $x _ { i , 2 , 2 }$ is one—meaning there is a major city in the won assignment—and then two other cities are also won or $x _ { i , 2 , 2 }$ is zero and the bidder does not win an assignment.)

A typical rule that TV advertisers might request on ad placement is, for example, any combination of 15- and 30-second commercials in news shows only that would reach 100,000 viewers in the demographic category of women age 25–54. To enumerate all the possible show and ad-length combinations that would satisfy this rule would be onerous for the typical bidder. The rule itself is readily incorporated into the winner determination problem as follows. Let $d _ { s , c } =$ demographic coverage of show s for category c (e.g., women age 25–54); $x _ { i } = \mathrm { a }$ zero-one variable for agent i. When one, agent i has won some time slots; and $x _ { i , t , s } = \mathrm { a }$ zero-one variable for agent i, time slot type t (e.g., 15, 30, etc., seconds), and show s. When equal to one, agent i wins the time slot of type t in show s.

<table><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>4</td><td>5MajorCity</td><td>6</td></tr><tr><td>7</td><td>8</td><td>9</td></tr></table>

Figure 1. Example of Spectrum License Space

Then, the constraints

$$
\sum_ {s \in N e w s S h o w s} \sum_ {t \in \{1 5, 3 0 \}} d _ {s, c = W o m e n 2 5 - 5 4} x _ {i, t, s} \geq 1 0 0, 0 0 0 x _ {i}
$$

and

$$
\sum_ {s} \sum_ {t} x _ {i, t, s} \leq M x _ {i}
$$

implement this rule (M is the total number of time slots across all shows).

Thus, in the rule-based auction found in Jones and Koehler [9, 10], bids are represented by a bid amount and collection of rules that are translated into a mixed-integer program (the winner determination problem) that is heuristically solved using a number of strategies (including a combination of constraint programming, branch and bound search, linear programming relaxation, and dynamic programming). More specifically, the winner determination method employed in the rule-based auction mechanism is able to construct the complex logic required to represent the rules in a mixed-integer program, and hence all the feasible solutions they allow. The details of mapping rules to constraints in an integer program that represents the winner determination problem can be found in Jones and Koehler [9, 10] and is beyond the scope of this paper. The constraints induced by such rules implicitly represent all the feasible bids of a bidder. This spares the bidder the onerous (usually impossible) task of enumerating feasible bids.

Moreover, the winner determination problem can use solution methods to prune bidder solution spaces in ways bidders could not. This is akin to branch-and-bound methods used to solve mixed-integer programs. For instance, as tentative allocations are made during the winner determination process (i.e., as feasible solutions are discovered), the space of all remaining feasible bidder bundles is reduced, because only ones having a better solution need to be considered by the seller. A buyer would not normally be able to anticipate this intermediate, reduced, solution state, and, in a normal multistage auction, would have to submit a complete set of possible, acceptable bids. Instead, the auction mechanism can aggregate the bids and determine which combination satisfies the stated high-level needs of the buyers while at the same time maximizing the overall seller revenue. This iterative auction approach continues in rounds until it satisfies a stopping criterion.

## Hypotheses

THE RESEARCH QUESTIONS WE INVESTIGATE are (1) whether the auction mechanism described above can, in a single auction, successfully sell to clients with very different demand types, budgets, and bidding strategies while simultaneously solving a difficult capacity allocation problem, and (2) whether the resulting allocations will provide sufficient buyer and seller surplus to maintain incentives for participating in this competitive auction. As discussed above, we follow Jones and Koehler [9] by focusing our experiments on an auction mechanism for selling prime-time television advertising slots. This market consists of a set of buyers that is naturally segmented along two dimensions. First, they differ in the degree to which they insist on specific shows, ranging from buyers who are very flexible and will accept any shows that meet their demographic exposure requirements to those who insist on specific shows for their entire allocation. We represent this segmentation with five levels of rules specified by buyers on the desired shows, from rules imposing no constraint on show selections (very flexible) to rules imposing tight constraint (all shows specified) with three intermediate levels. Second, they differ in the degree to which they are willing to trade off price against their specific constraint on the shows they want. We represent this segmentation with three distinct bidding strategies: those only willing to modify their price; those who first modify price, then loosen constraint; and those who alternate between the two.

To study the effectiveness of this auction method in addressing market segmentation, we examine three sets of markets that vary in the overall composition of buyers such that they have significantly different levels of constraint, with a higher level of constraint meaning there is a higher percentage of bids that are bound to specific shows. The composition of these markets is shown in Table 1. A number of our hypotheses concern pricing effects, and it is important to measure the price paid for advertising slots in both absolute and relative terms. The absolute measure is straightforward—it is CPM, a standard measure of price paid per exposure. The relative measure is more complex and involves the estimation of expected value for sellers and buyers. The relative measures express gains relative to these expected values, which are described in greater detail in the Experimental Design section.

Table 1. Initial Desired Show Bounds Varied by Market Condition

<table><tr><td rowspan="2">Bounds</td><td colspan="3">Percent of bidders</td></tr><tr><td>Low</td><td>Medium</td><td>High</td></tr><tr><td>No bounds</td><td>40</td><td>20</td><td>0</td></tr><tr><td>2–3 percent of number selected</td><td>40</td><td>30</td><td>30</td></tr><tr><td>4–6 percent of number selected</td><td>10</td><td>30</td><td>40</td></tr><tr><td>6–8 percent of number selected</td><td>6</td><td>10</td><td>20</td></tr><tr><td>Tight</td><td>4</td><td>10</td><td>10</td></tr></table>

Our first hypothesis concerns the effect of the overall level of market constraint on the outcome of the auction. As noted above, a highly constrained market is modeled here as one with proportionally fewer buyers that are more flexible in their time slot allocations, whereas a lower market constraint level has proportionally more buyers with few or no constraints on the specific shows in which they want their advertising slots. This effectively captures the fact that in prime-time television advertising sales, it is simply more difficult to solve the problem of allocating all capacity when the number of constraints (the number of specific shows required) is greater, resulting in a higher level of unsold inventory at the end of the auction. Stated in general terms:

H1a (Higher levels of market constraint lead to higher levels of unsold inventory): As the proportion of bidders with greater numbers of specific show requirements increases, there will be higher levels of unsold inventory.

A closely related point concerns the importance of buyers who are flexible in their show selections, either initially or in the course of bidding, and, in particular, emphasizes how this importance changes with market conditions. In general, as the number of constraints increases and the allocation problem becomes more difficult to solve, those buyers who are willing to loosen their particular constraints are more likely to become part of the solution to the allocation problem. In the prime-time advertising market modeled in our auctions, when demand is highly constrained, it is more difficult to determine an allocation of capacity, thus buyers willing to loosen constraints should win a greater proportion of the advertising slots. In general terms, we state this as:

H1b (The relation of willingness to loosen constraints to winning proportion increases in market constraint levels): As the proportion of constrained bidders in the market increases, increasing the overall level of market constraint, those willing to loosen their specific show constraints will win a greater portion of advertising slots.

On one hand, one of the advantages of the rule-based method mentioned above is that the complexity inherent in calculating feasible solutions need not be explicitly addressed by the bidder, because the rules can allow many feasible solutions. A practical result of this is that the larger the buyer’s budget, all else being equal, the larger the set of shows that would satisfy the buyer’s rules—allowing the solution space to grow with buyer budget without increasing rule complexity. In general, this should lead to more efficient solutions due to the optimization built into the solution algorithm. Given the iterative nature of the auction implementation, this increase in efficiency should benefit both the buyer and the seller.

As a buyer’s budget increases, the seller will have a greater variety of shows that could be combined to satisfy the rules imposed by the bid. This, in turn, leads to more opportunities to improve the seller’s allocations to buyers, thus benefiting the seller. Seller surplus is measured with respect to the seller’s reservation price for each item. Hence, we hypothesize that:

H2a (Seller surplus increases with buyer budget): Seller surplus will increase in the number of units allocated per bidder.

Because the underlying auction mechanism is an ascending price auction (or nondescending price when new bids involve loosening contraints), the seller is not in a position to extract all the incremental savings that may ensue from the buyer’s increased budget. In other words, buyers with relatively low initial bids but a larger potential solution space will have a greater chance of arriving at an acceptable solution to the seller at a lower overall price. Thus,

H2b (Buyer surplus increases with buyer budget): Buyer surplus will increase in the number of units allocated per bidder.

The buyer surplus is measured with respect to buyer budget or reservation price, but the same result should hold for prices in general, again because of the efficiencies derived from optimization over a larger set of feasible solutions with a proportionately lower number of constraints. In this case, the CPM exposures should decrease. Thus,

## H2c (Average price decreases with buyer budget): CPM will decrease in the number of units allocated per bidder.

Moving on to the effect of specific bidder strategies, or types, we look first at the bidder who is not willing to adjust constraints at all. In the television advertising case, this could represent an advertiser who is only interested in placing ads in a specific show or type of show, such as the Super Bowl. In this case, we presume that this buyer is likely to be willing to pay more. Conversely, as long as capacity expires, as it does for advertising (an unsold advertising slot loses all value after that time period has passed), sellers are willing to sell at lower prices than expected, under certain conditions, in order to induce other buyers to loosen their constraints. As stated in H1b, we expect more loosely constrained buyers to win greater proportions of advertising slots in more constrained markets. Thus,

H3a (Seller surplus decreases with buyer willingness to loosen constraints in a tightly constrained market): The seller surplus for winning buyers unwilling to loosen constraints will exceed seller surplus for winning buyers who are willing to loosen constraints.

In general terms, bidders understand that their flexibility should allow them to achieve better value. This is captured in their private valuations of suitable solutions to the rule sets and thus in the bids they submit. We measure buyer’s surplus relative to reservation value, and assume that as buyers adjust their constraints, they also adjust their reservation values. Buyers with higher constraints are willing to pay more; those loosening constraints are paying less but they also have lower reservation values. Thus,

H3b (Buyer surplus is invariant over bidder types): Buyer surplus—measured against buyer’s reservation value—will not vary across bidder types.

Seller and buyer surplus are defined relative to their respective expectations concerning prices obtained in the market. However, if we look at CPM (an objective measure of buyer cost), the results should parallel those for the seller, whose reservation price is invariant in the buyer constraint level (while the buyer’s is not). Thus,

H3c (Realized price decreases with willingness to loosen constraints in a tightly constrained market): The CPM for winning buyers unwilling to loosen constraints will exceed the CPM for winning buyers who are willing to loosen constraints.

A final test for the proposed auction mechanism is that it must efficiently allocate the units such that those with the highest value for an item(s) are among the winning allocations. The ability of the proposed method to do this is not affected by market conditions; thus we expect that it will prove to be an efficient allocation method regardless of market conditions.

H4 (Auction efficiency is invariant over market demand conditions): Allocation efficiency will not vary when the concentration of constrained bidders varies.

## Experimental Design

TO EFFECTIVELY ANALYZE THE ABILITY of the proposed auction mechanism to serve diverse market segments, we ran auctions that simulate the actual sale of a week of prime-time TV advertising slots, using bidding agents programmed to present differing demand and budget characteristics as well as differing bidding strategies. Simulation is appropriate in “cases in which mathematical models are either apparently intractable or provably insoluble” [1, p. 18]. The combinatorial auction allocation problem is a variant of the multiple knapsack problem, which is NP-complete. Therefore, to gain insight into the efficacy of our auction mechanism, we developed agents based as closely as possible on characteristics of a known negotiated market and allowed them to compete in the auction that we investigate in this research. We replicate the simulations to gather sufficient data for analysis, using differing random number of seeds across replications to assure differing sets of bidder types.

Because the critical differences between bidders involve both their bidding strategy and the degree to which they are willing to trade off constraints for price, we impose three different overall levels of market constraint, manifest in the severity of the initial constraints associated with the different bidding agents. We use the same random number of seeds across market conditions to assure identical initial bidder type distributions and facilitate comparisons across conditions. As the overall level of constraint rises, it becomes more difficult to find solutions to the underlying allocation problem, making the willingness to trade off constraints less common and thus more valuable. This allows us to test the sensitivity of the auction outcomes to this market factor.

## Agent Generation

The bidding agents we generate are patterned on the observed characteristics of the actual results of standard negotiations (not using an auction mechanism) for a major television network. We use these characteristics to craft agents (discussed below) that bid in the multi-attribute combinatorial electronic auction described in this paper. Each bidding agent represents an individual bidder with defined parameters that reflect media buying practices within the industry, including bidder product requirements and bidder strategy. Product requirements comprise the desired demographic category and GRP required as well as bidder reservation prices. A list of desired shows, an upper and lower bound on the number required, the number of commercials allowed in each show, and the type of product being sold were also specified.

The data underlying the modeling of the bidders and the establishment of market parameters are derived from a review of two representative weeks of actual airtime allocations from negotiations. The data consists of 150 unique buyers representing 209 purchases to acquire 1,290 units of airtime across 48 shows. In the two weeks of data, we observed roughly 90 to 120 buyers who negotiated allocations in each week. Our industry source indicated that 300 to 350 buyers typically enter into negotiations, with those successfully reaching agreement receiving allocations distributed across the weeks of the year—we generate 325 bidding agents.

## Parameter Estimation

Media buyers must achieve a certain amount of demographic exposure, or GRP, within a specific demographic group to satisfy their campaign needs. The ACNeilsen Ratings for network television is the measure used to determine the number of people exposed to a particular program and, hence, to the commercials appearing in that show. The ratings are broken down in various categories representing the gender and age of the viewing audience. Six of these categories are typically associated with prime-time advertising sales: women, men, and adults within age groups 18–49 and 25–54. Category assignments for each agent were randomly chosen from a uniform distribution over the values 1 to 6. An analysis of the data revealed that the amount of demographic GRP required by each buyer followed a gamma distribution. Appropriate maximum likelihood estimates of gamma distribution parameters α[ and $\hat { \beta }$ were generated for each category. The Kolmogorov-Smirnov one-sample test was used to determine the goodness of fit between the estimated gamma distribution and the sample values. The cumulative distribution for the theoretical gamma distribution is compared to the cumulative distribution of the actual data. The maximum deviation from the theoretical distribution must be less than or equal to a critical value defined for the test. Results of the test are presented in Table 2 and validate at a 0.05 significance level that the sample came from a population having a gamma distribution [18]. Using Phillips gamma variate generator [15] and the estimated $\hat { \alpha }$ and $\hat { \beta }$ for the appropriate category, we are able to generate a representative random demographic value to assign an agent.

Table 2. Goodness-of-Fit Test

<table><tr><td colspan="3">Kolmogorov-Smirnov one-sample testSignificance level = 0.05 (two-tailed)Critical value = 0.09407</td></tr><tr><td colspan="2">Maximum difference</td><td>≤ critical value?</td></tr><tr><td>Demo 1</td><td>0.0675</td><td>Yes</td></tr><tr><td>Demo 2</td><td>0.0657</td><td>Yes</td></tr><tr><td>Demo 3</td><td>0.0777</td><td>Yes</td></tr><tr><td>Demo 4</td><td>0.0721</td><td>Yes</td></tr><tr><td>Demo 5</td><td>0.0696</td><td>Yes</td></tr><tr><td>Demo 6</td><td>0.0751</td><td>Yes</td></tr></table>

The data analyzed for this study include the amount that each successful buyer paid for each of their allocated commercials with the associated placement information. We can safely assume that the buyer’s reservation price over all their units is at least the sum of the individual unit values. We also know the network’s estimated GRP for the shows within the sampled weeks. The seller’s rating estimates are not common knowledge among the buyers; instead, buyers base their demographic requirement calculations on approximations discovered from historical ratings of prior seasons and market research on new programming. These approximations are fairly accurate in reflecting the seller’s figures; therefore, we apply the known seller rating estimates to determine roughly how many demographic GRP the buyers desired by summing the demographics over the shows they were allocated. We then standardize the demographics to reflect the length of commercials. For example, a 30-second commercial would receive twice the demographic exposure of a 15-second spot. A strong linear relationship was found to exist between the price paid for the units and the equivilized demographic GRP for the associated shows but showed signs of heteroskedasticity. A natural logarithm transformation of both variables remedied the increasing variance. See Table 3 for a summary of the fit.

By regressing logarithmic price against the logarithmic standardized total demographic GRP (converted to account for heteroskedasticity in the data) within each demographic category, we were able to establish equations for determining a representative reservation price. Each category’s regression equation was determined for the base case from the 209 observations. Based on the demographic category and the total demographic GRP formulated in the previous steps, we can calculate, from the appropriate regression equation, individual reservation prices to assign the agents that reflect the amount and type of product desired. This reserve price also constitutes the buyer’s budget.

Table 3. Regression Fitness Statistics

<table><tr><td colspan="5">LNPrice = Constant + (Coefficient * LNDemo)</td></tr><tr><td>Demo</td><td>R-square</td><td>F</td><td>t</td><td>Significance</td></tr><tr><td>1</td><td>0.836</td><td>1056.437</td><td>32.503</td><td>0.000</td></tr><tr><td>2</td><td>0.837</td><td>1065.432</td><td>32.641</td><td>0.000</td></tr><tr><td>3</td><td>0.835</td><td>1047.752</td><td>32.369</td><td>0.000</td></tr><tr><td>4</td><td>0.834</td><td>1038.267</td><td>32.222</td><td>0.000</td></tr><tr><td>5</td><td>0.844</td><td>1118.842</td><td>33.449</td><td>0.000</td></tr><tr><td>6</td><td>0.846</td><td>1135.407</td><td>33.696</td><td>0.000</td></tr></table>

The regression gives us the reservation prices representing the budget for those buyers who were successful in achieving an allocation. We recognize that there may have been participating buyers that were not successful in securing an allocation and others that were not forced to pay their true valuation; therefore, we increase the variance of the actual reservation price assigned by a random amount uniformly distributed between 20 percent above or below the calculated figure.

We assume that an allocation has no value to the buyer unless all constraints have been met, while any allocation that satisfies the constraints is valued at his or her reservation price. Buyers are trying to satisfy explicit campaign goals at a minimal cost; thus, adding additional units to the minimal constraint satisfying allocation is assumed not to add value. To account for the buyers’ willingness to pay more for a more demanding allocation, we increase the original budget calculated above by 2 percent for each show that a buyer demands. For example, if a buyer indicates that he or she requires at least three of the shows targeted, the buyer’s budget will be increased by 6 percent. This reflects a higher willingness to pay for more control of the final allocation.

An analysis of the historical data indicates that approximately 76 percent of bidders aired multiple commercials within the campaign week, while 24 percent placed only one spot. Our agent demands reflect these statistics. Within the two groups, multiple or single placement, we were also able to determine a frequency of the lengths of commercials aired. Dispersing commercials across various shows ensures that as many different viewers as possible are exposed to an advertiser’s message. Generally, advertisers limit to one the number of commercials in each show. The data confirmed that 70 percent of advertisers with multiple commercials in the campaign week allowed only one spot per show, while 28 percent accepted up to two and 2 percent permitted as many as three. We capture these same frequencies within our agents.

The type of product advertised by our participants affects the allowable placement of the commercials. The industry practice of “pod protection” involves not allowing two commercials promoting the same type of product to appear in the same commercial break if one is at least 30 seconds long. It makes distribution of product types across buyers an important consideration in our agent development. We were able to ascertain from the data provided the frequency of the various product types and use those frequencies to establish a representative mixture in our agents.

## Market Constraint Levels

We designed our experiments to determine the effect of the overall market level of constraint imposed by our bidders. The three market conditions—referred to as high, medium, and low constraint levels—are determined by establishing an initial lower bound on the number of selected shows required by each bidder. At the bidder level, there are five levels of constraints that determine the number of shows that each bidder requires. These are varied to create the three market conditions, as shown in Table 1. Notice that the percentage of bidders with a larger percentage of selected shows requested increases with the constraint level. In the case of high constraints, all bidders initially demand at least one specific show.

Upper bounds were set at the number of shows selected. The frequencies were chosen at random but reflect anecdotal evidence. Buyers are described as routinely indicating that they would prefer as many shows of a particular type of programming as possible, but generally do not specify the exact number required. For example, buyers may want their commercials to appear mostly in situation comedy shows, or possibly only in news programming. Rarely, an advertiser may demand to appear in a specific show or group of shows and if the network is unable to grant the request, will not accept alternative placement. This last level represents a bidder with tight bounds.

## Bidder Strategies and Types

Classical auction theory often assumes homogeneity among auction participants, and frequently assumes, or attempts to derive, optimal bidding behavior. Recent electronic auction research reveals the existence of a multitude of bidder types, such as the evaluators, participators, and opportunists described by Bapna et al. [2, 3]. Given that our television network resources describe bidder behaviors that align well with these types, we also model three distinct bidding strategies, looking at the relative advantages and disadvantages as an outcome of the auction, but not as one that would necessarily affect bidders’ choice of strategy. This is consistent with the argument in Rothkopf that in some cases, “it may make sense to assume a restriction typically utilized by bidders, even if it is theoretically suboptimal” [16, p. 73].

A buyer’s type is associated with specific bidding strategies used during the execution of the auction. We developed three distinct bidder types, of which one modifies the bid amount only and two modify both the bid amount and the constraints imposed on commercial placement. We define BidAdjustors (Bid) as those bidders who only modify the price they are willing to pay for an allocation. AllAdjustors (All) and Modifiers (Mod) combine the techniques of bid and constraint modification, but differ in the manner in which they make their bid modifications. AllAdjustors first attempt to modify the amount they bid, and when they have reached a point where they can no longer increase the dollars bid by the minimum increment, they resort to modifying their constraints. Modifiers alternate between adjusting their bid amount and loosening constraints.

Constraint adjustments involve relaxing the restrictions imposed on the shows required or allowed to be allocated to the bidder. These restrictions include the bounds on the number of shows included in the desired show list. As a minimum, the bidder must loosen a restriction by at least one unit. Bidders are advised of the constraint(s) that cannot be met. For example, the shows available to allocate to a bidder may not satisfy the minimum number of shows desired by the bidder; in this case, the bidder is notified that his or her lower bound of desired shows is too high. Bidders use this information to direct the choice of constraint modification strategy.

For each of the three bidder types, the modification of bid amounts is done by one of two increments. The bidder may reenter the auction with an offer incremented by a percentage of his or her rejected bid; the rules of the auction establish this minimum increase. Alternatively, our auction mechanism provides the bidder with a recommended bid increment to assist in the formation of subsequent bids, and agents may increase their prior bid by this recommended amount. The recommended increment is calculated as the difference between the amount the individual bid previously and the seller’s discounted list price for what was determined to be the best allocation for that bidder’s demographic requirement in that round. Following the rules imposed by our auction, any recommended bid is at least the minimum percentage increase above the previous bid, but may be greater. The option to choose between these two increments dictates the bid adjustment strategies, either maximum or minimum. In either case, prior to posting, a check is made to see if the interval between the prospective bid and the bidder’s reservation price is less than the minimum bid amount required in the next round. If the gap is smaller than an allowable bid, the bidder will submit a bid equal to his or her reservation price to avoid a situation where the current bid is less than the reservation price, but the bidder cannot reenter the bid because his or her next bid will not meet the minimum increment requirement. The approach is similar to the strategic at margin strategy suggested by Bapna et al. [3].

Bidders choosing the maximum of the percentage or recommended increase are acting on the assumption that they will have a greater chance of achieving an allocation if they choose the largest increment. This approach could be viewed as representative of risk-averse bidders with the difference between the minimum percentage and the recommended increase being the risk premium [19]. If the buyer believes that there is a chance that a lower bid will be successful in the subsequent round, the minimum increment strategy would be a better choice. Regardless of the strategy chosen, the buyer cannot bid an amount greater than his or her budget.

The three bidder types and the choice between minimum and maximum increments in the bid amount result in six distinct bid strategies, which are randomly assigned to the bid agents, with an equal probability for each strategy, at the inception of a simulation run. When designated as inactive, all bidder types will attempt to reenter the auction following their adjustment strategy until they can no longer meet the minimum increment guidelines. We assume that bidders will accept an allocation as long as it meets the criteria and restrictions specified by the agent in the associated bid. Therefore, we do not include logic permitting bidder rejection of an allocation or early withdrawal from the game.

## The Simulation

Using automated agents—generated using the specifics identified above—we tested the efficacy of the various agents on a total of 24 different auctions. The agents were exposed to three different treatments, which varied on the level of constraints imposed (low, medium, high). Each treatment was generated with the same set of eight different random number seeds used in the randomization of agent parameters.

The experiments were conducted using the activity-based stopping rule, which ends the auction when no new bids are received. A new bid could consist of a bidder either increasing the bid amount or decreasing a constraint. To determine the impact of the treatments on the auction outcome, we tracked the number of winning bidders of each type, buyer surplus, seller surplus, and the CPM demographic exposures for the agents in each auction. Buyer surplus is the difference between the amount of an individual bidder’s reservation price and the amount of his or her final winning bid. Seller surplus is defined as the difference between the sum of the seller’s reservation price for the bundle of goods sold and the final winning bid for each bidder. We also tracked the amount of unsold inventory remaining at the end of each auction.

## Results

IN THIS SECTION, WE PRESENT THE RESULTS associated with each of our stated hypotheses. Nonparametric tests were used in our analysis because our data was shown not to be normally distributed, and, in some cases, the number of observations was small enough that we could not apply the central limit theorem (i.e., when the number of surviving bidders of a particular type was small). We used the Kolmogorov-Smirnov test to determine if the data sets differ significantly. This test makes no assumptions about the distribution of the data and should be used when the treatment groups may differ in mean or in some other way such as range or variance. Given that we are looking at the characteristics of a group of buyers, these other differences may be an important consideration in analyzing our results. We also applied the Kruskal-Wallis test, which is the nonparametric analog of the one-way analysis of variance (ANOVA) [18].

As a preliminary matter, we examine whether there is any advantage or disadvantage associated with following the minimum (or maximum) version of any given strategy, wherein the seller’s recommended bid increment is ignored (or used) if the bid amount is, in fact, being modified, and provided it does not exceed the buyer’s reservation value. We find that seller surplus is greater for those bidding only the minimum increment, while buyer surplus is less (Table 4). This seems counterintuitive, but hinges on a consequence of the winner determination process: the bidders taking smaller steps (minimum bidders) are less likely to be tentatively assigned winning allocations during the auction, and are therefore more likely to have to enter new bids to remain in the auction. For the simulated bidding agents 67 percent of surviving minimum bidders had bid up to their reservation values (leaving them a buyer surplus of 0), whereas only 53 percent of surviving maximum bidders had bid up to their reservation values. The auction mechanism appears then to offer a slight advantage to the more aggressive bid strategy of following the maximum bid recommendation. This same phenomenon also underlies the positive seller surplus associated with bidders using the minimum strategy. There is not a significant difference in the CPM the bidders in these categories are able to achieve.

Table 4. Comparison of Maximum Versus Minimum Bid Increment Strategies

<table><tr><td rowspan="2"></td><td>Kwallis</td><td>Ksmirnov</td></tr><tr><td>Chi-square</td><td>Minimum versus maximum</td></tr><tr><td>Seller surplus</td><td>14.946***</td><td>&gt;***</td></tr><tr><td>Buyer surplus</td><td>37.609***</td><td>&lt;***</td></tr><tr><td>CPM</td><td>0.057</td><td>ns</td></tr></table>

\* significant at 0.05; \*\* significant at 0.01; \*\*\* significant at 0.001.

H1a and H1b are both concerned with demonstrating the impact of serving different market segments, modeled here by buyers with differing levels of constraint. First, it is important to note that the seller is assumed not to adjust reservation prices in the face of higher overall constraint levels. Therefore, it is to be expected that the overall level of unsold inventory would increase as the market constraint level increased, as suggested by H1a. In Table 5, we see that the average amount of unsold inventory does not significantly decrease between medium to high and between medium to low constrained cases (paired t-test proved insignificant) as overall market constraint level decreases. However, there is a significant difference between high to low (at the 0.05 level). The consistency in the amount of unsold inventory across constraint levels may be due to the high percentage of winning bidders that are willing to adjust their constraints, and an excess of demand over supply even in the highly constrained market, allowing for an efficient allocation regardless of the constraints initially imposed.

Furthermore, we expect that as the market becomes more constrained, those who are willing to loosen constraints (All, Mod) will fare better than buyers with less flexible constraints (Bid). Table 6 shows the survival rate of each type of bidder over the various treatments. Overall, the number of winning bidders that were willing to modify their constraints (All or Mod) far exceeds those that were not (Bid). The survival rate is defined as the percent of the original bidders generated of that agent type (All, Mod, or Bid) that are among the winning bidders. All and Mod agents preformed similarly; however, Mod agents survived to a greater degree with the difference most pronounced in the low and moderately constrained conditions. The decline in the percent of BidAdjustor (Bid) winners is significant as market constraint levels increase, as tested using pairwise one-tailed t-tests (at the 0.01 level).

Table 5. Unsold Inventory Levels (H1a)

<table><tr><td rowspan="2">Replication</td><td colspan="3">Market constraint level</td></tr><tr><td>High</td><td>Medium</td><td>Low</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>2</td><td>5</td><td>5</td><td>3</td></tr><tr><td>3</td><td>6</td><td>8</td><td>2</td></tr><tr><td>4</td><td>1</td><td>4</td><td>2</td></tr><tr><td>5</td><td>6</td><td>5</td><td>2</td></tr><tr><td>6</td><td>2</td><td>5</td><td>0</td></tr><tr><td>7</td><td>5</td><td>1</td><td>5</td></tr><tr><td>8</td><td>5</td><td>3</td><td>4</td></tr><tr><td>Average</td><td>3.88</td><td>4</td><td>2.25</td></tr></table>

Table 6. Survival Rate of Buyers by Type and Market Constraint Level (H1b) (in percent)

<table><tr><td rowspan="2">Bidder type</td><td colspan="3">Market constraint level</td></tr><tr><td>High</td><td>Medium</td><td>Low</td></tr><tr><td>AllMax</td><td>49.6</td><td>38.5</td><td>37.7</td></tr><tr><td>AllMin</td><td>52.6</td><td>46.8</td><td>44.1</td></tr><tr><td>BidMax</td><td>2.9</td><td>10.3</td><td>11.0</td></tr><tr><td>BidMin</td><td>4.2</td><td>10.9</td><td>14.6</td></tr><tr><td>ModMax</td><td>47.6</td><td>41.8</td><td>33.9</td></tr><tr><td>ModMin</td><td>51.0</td><td>42.1</td><td>47.7</td></tr></table>

The choice of acting on a recommendation (maximum) or increasing bid amounts by the minimum requirement does not significantly affect the number of surviving bidders within each agent type, except in the case of BidAdjustors. This implies that the choice of bid modification amount is more important to the agents that only modify their prices and not their constraints. Although this was not hypothesized, it is a reasonable result—the BidAdjustors have only the bid value to work with, so it makes sense that they are the most sensitive to any additional information that may help in setting that value.

The second set of hypotheses, H2a, H2b, and H2c, concerns whether financial incentives for making large-volume purchases (defined as an allocation of five or more advertising units), which are associated with higher buyer budget levels, will continue to operate under this auction design when measured with respect to seller surplus, buyer surplus, and CPM, respectively. In Table 7, we show the results of nonparametric tests. Seller surplus is not significantly different for small versus large purchases, so H2a is not supported. As pointed out in the formulation of the hypotheses, the auction mechanism provides a means for the buyer to extract some of the expected gain due to the larger solution space associated with higher budgets—it appears that the buyers are able to extract essentially all of that gain. Because the buyer’s budget is determined by the buyer, the necessary incentives are maintained. Although the seller is not able to extract any of the gain, it is important to note that the seller is no worse off with larger buyer budgets; they are simply indifferent. Buyer surplus and CPM are distributed in the directions predicted in H2b and H2c: buyer surplus is greater for larger purchases than smaller purchases, and CPM is smaller, indicating that the larger buyer can command better trades.

Table 7. Comparison of Large Versus Small Purchase Size

<table><tr><td rowspan="2"></td><td>Kwallis</td><td>Ksmirnov</td></tr><tr><td>Chi-square</td><td>Large versus small</td></tr><tr><td>Seller surplus (H2a)</td><td>1.930</td><td>ns</td></tr><tr><td>Buyer surplus (H2b)</td><td>5.744*</td><td>&gt;***</td></tr><tr><td>CPM (H2c)</td><td>8.894**</td><td>&lt;**</td></tr></table>

\* significant at 0.05; \*\* significant at 0.01; \*\*\* significant at 0.001.

Next, we assess how bidding strategies affect seller surplus (H3a), buyer surplus (H3b), and CPM (H3c). AllAdjustor agents (All) and Modifier agents (Mod) will loosen the constraints, as the auction progresses, on the shows they initially indicated were required. As indicated in Table 8, H3a is only partially supported. Seller surplus was less for BidAdjustor agents when compared to AllAdjustor agents, as expected, but there was no significant difference between BidAdjustor and Modifier types. A possible explanation is that only those BidAdjustors that contributed significantly to seller surplus were able to survive, whereas the other agents had greater flexibility to remain in the auction while providing less benefit to the seller. However, Table 8 shows support for H3b, that buyer surplus will not vary across bidder types, and highly significant support for H3c, that the CPM for winning buyers unwilling to loosen constraints will exceed CPM for winning buyers who are willing to loosen constraints.

We formulate an efficiency measure similar to those used in prior combinatorial auctions studies [5, 11, 12]. As in Jones and Koehler [9], we define the final allocation of the auction mechanism as

$$
y _ {b} (A) = \arg \max \sum_ {b = 1} ^ {B} a _ {b} y _ {b},
$$

Table 8. Comparison of Bidding Strategies All and Mod Versus Bid

<table><tr><td rowspan="2"></td><td>Kwallis</td><td colspan="2">Ksmirnov</td></tr><tr><td>Chi-square</td><td>All versus Bid</td><td>Mod versus Bid</td></tr><tr><td>Seller surplus (H3a)</td><td>18.410***</td><td>&gt;∗</td><td>ns</td></tr><tr><td>Buyer surplus (H3b)</td><td>5.656</td><td>ns</td><td>ns</td></tr><tr><td>CPM (H3c)</td><td>13.677**</td><td>&lt;***</td><td>&lt;***</td></tr></table>

\* significant at 0.05; \*\* significant at 0.01; \*\*\* significant at 0.001.

where $a _ { b }$ is bidder b’s bid amount and $y _ { b }$ is an indicator variable set to 1 if bidder b is a winner in the auction. Further, we determine an upper bound on the value attainable in the auction as

$$
V ^ {*} = \max \sum_ {b = 1} ^ {B} v _ {b} y _ {b}.
$$

From these two equations, we obtain

$$
E = \frac {\sum_ {b = 1} ^ {B} v _ {b} y _ {b} (A)}{V ^ {*}}.
$$

We estimate E by replacing the “max’s” with results from our heuristic. Although this measure does not use optimal solutions, the gaps we found between upper bounds and solution values are tight enough to provide reasonable estimates of efficiency. Table 9 shows that the efficiency of the auction is high, with results ranging from 97– 100 percent. Paired t-tests provide only partial support for H4, that constraint level of the market has no effect on the efficiency of the auction. When comparing high to medium and medium to low, there is no significant difference (at the 0.05 level); however, we cannot claim there is no difference in efficiency between high and low levels of market constraint. Surprisingly, it appears that the markets that have lessconstrained buyers are less efficient. This could be due to a higher level of less-flexible buyers surviving in the less-constrained market.

## Discussion

WITH A SINGLE RULE-BASED AUCTION MECHANISM, we are able to efficiently and simultaneously address internal seller constraints (e.g., meeting industry constraints such as not placing competitive ads together), buyer constraints (e.g., show restrictions), and pricing for the multiple market segments, captured in our simulation by bidding agents that mimic different observed bidder types. As the overall market level of constraint increases, we have demonstrated in our simulations an increase in unsold inventory only when comparing the extreme cases (i.e., low versus high constrained cases). Since the model parameters, especially reservation prices, were based on an actual market that did not include the aftermarket for unsold inventory, the fact that there remains inventory at the end of the auction is indicative of a good fit between the simulation and the actual market. The results of this study are based solely on the results of simulations. Although we made every effort to model our agents on real data, the results may not be robust to environments that do not reflect the agent behavior generated for this simulation.

Table 9. Efficiency

<table><tr><td rowspan="2">Replication</td><td colspan="3">Market constraint level</td></tr><tr><td>High</td><td>Medium</td><td>Low</td></tr><tr><td>1</td><td>99.3528</td><td>98.5887</td><td>99.2994</td></tr><tr><td>2</td><td>97.7185</td><td>98.8043</td><td>97.1791</td></tr><tr><td>3</td><td>97.7766</td><td>97.7835</td><td>97.1535</td></tr><tr><td>4</td><td>99.7493</td><td>98.6232</td><td>97.0843</td></tr><tr><td>5</td><td>100.0000</td><td>98.0938</td><td>97.2955</td></tr><tr><td>6</td><td>98.7346</td><td>99.6278</td><td>97.7400</td></tr><tr><td>7</td><td>99.4174</td><td>98.6243</td><td>98.8374</td></tr><tr><td>8</td><td>98.3785</td><td>100.0000</td><td>98.6853</td></tr></table>

The fact that the auction mechanism we implement here is able to preserve the advantages of volume purchase is significant, given that this is a combinatorial auction approach. It is intuitively appealing that volume purchases should lead to greater efficiencies and thus to improved profitability and pricing, but this has been problematic in combinatorial auctions, where the complexity of bid construction can grow so quickly in purchase volume as to swamp any benefits. With the rule-based mechanism that averts the explosion in complexity as purchase volume increases, we are able to preserve the expected efficiency gains.

We are also able to examine an interesting question that arises with respect to the sharing of information obtained from the allocation process with bidders to help them improve their chances of winning in the next round. It is clear analytically that it may not be advantageous for the seller to provide such information. But we have discussed cases where the provision and use of the information did appear to make a difference for the buyer.

We have shown that those bidders willing to loosen constraints on their original demands were able to perform better in the auction. Not only did they have a greater chance of being among the winners but their allocation was generally less costly, leaving them with a reduced CPM demographic exposure. At the same time, due to the increased flexibility in allocating units across the various winners, the seller was able to increase surplus. The AllAdjustor and Modifier agents in our simulation were programmed to be able to completely eliminate all specific show demands that may be somewhat unrealistic. Of those with specific shows desired at the beginning of the auction, 87.7 percent of All agents and 97 percent of the Mod agents reduced their requests to zero by the auction’s end. Should the bidders become more demanding overall, we would expect that survival rates of the nonconstraint-adjusting bidders to increase and the associated benefits to decrease for the constraint adjustors.

The ability to serve most or all market segments with a single mechanism is important not just to simplify e-markets, but it can also have a significant effect on productive and efficient handling of capacity by the supplier by providing information on demand and pricing from all market segments in a timely manner. Such a mechanism may help facilitate seller ownership of e-markets. One factor currently favoring buyerowned e-markets may be the relative complexity of specifications and constraints on the buyer side (e.g., in many manufacturing settings), including quality, delivery, and other attributes of the transaction. It is also possible that sufficient power may reside on the buyer side (e.g., General Electric, Wal-Mart) to preempt a supplier e-market. Nonetheless, a single auction mechanism that is capable of addressing multiple market segments and obtaining differing prices from those segments may help overcome barriers to the implementation of seller-owned e-markets.

## REFERENCES

1. Axtell, R. Why agents? On the varied motivations for agent computing in the social sciences. Working Paper No. 17, Center on Social and Economic Dynamics, Brookings Institution, November 2000.

2. Bapna, R.; Goes, P.; and Gupta, A. Insights and analyses of online auctions. Communications of the ACM, 44, 11 (2001), 42–50.

3. Bapna, R.; Goes, P.; and Gupta, A. Analysis and design of business-to-consumer online auctions. Management Science, 49, 1 (2003), 85–101.

4. Brynjolfsson, E., and Smith, M.D. Frictionless commerce? A comparison of Internet and conventional retailers. Management Science, 46, 4 (2000), 563–585.

5. Bykowsky, M.M.; Cull, R.J.; and Ledyard, J.O. Mutually destructive bidding: The FCC auction design problem. Journal of Regulatory Economics, 17, 3 (2000), 205–228.

6. Clemons, E.K., and Weber, B.W. Segmentation, differentiation, and flexible pricing: Experiences with information technology and segment-tailored strategies. Journal of Management Information Systems, 11, 2 (Fall 1994), 9–28.

7. Clemons, E.K.; Hann, I.-H.; and Hitt, L.M. Price dispersion and differentiation in online travel: An empirical investigation. Management Science, 48, 4 (2002), 534–549.

8. Crampton, P. The FCC spectrum auctions: An early assessment. Journal of Economics and Management Strategy, 6, 3 (1997), 431–495.

9. Jones, J., and Koehler, G.J. Combinatorial auctions using rule-based bids. Decision Support Systems and Electronic Commerce, 34, 1 (2002), 59–74.

10. Jones, J., and Koehler, G.J. A heuristic for winner determination in rule-based combinatorial auctions. INFORMS Journal on Computing, 17, 4 (Fall 2005), 475–489.

11. Kwasnica, A.M.; Ledyard, J.O.; Porter, D.; and DeMartini, C. A new and improved design for multiobject iterative auctions. Management Science, 51, 3 (2005), 419–435.

12. Ledyard, J.O.; Porter, D.; and Rangel, A. Experiments testing multiobject allocation mechanisms. Journal of Economics and Management Strategy, 6, 3 (1997), 639–675.

13. McAfee, R.P., and McMillan, J. Analyzing the airwaves auction. Journal of Economic Perspectives, 10, 1 (1996), 159–175.

14. McMillan, J. Selling spectrum rights. Journal of Economic Perspectives, 8, 3 (1994), 145–162.

15. Phillips, D.T. Generation of random gamma variates from the two-parameter gamma. AIIE Transactions, 3 (September 1971), 191–198.

16. Rothkopf, M.H.; Harstad, R.M.; and Fu, Y. Is subsidizing inefficient bidders actually costly? Management Science, 49, 1 (2003), 71–84.

17. Rothkopf, M.H.; Pekec, A.; and Harstad, R.M. Computationally manageable combinational auctions. Management Science, 44, 8 (1998), 1131–1147.

18. Siegel, S. Nonparametric Statistics for the Behavioral Sciences. New York: McGraw-Hill, 1956.

19. Varian, H.R. Microeconomic Analysis, 3d ed. New York: W.W. Norton, 1992.

20. Xia, M.; Koehler, G.J.; and Whinston, A.B. Pricing combinatorial auctions. European Journal of Operational Research, 154, 1 (April 2004), 251–270.
