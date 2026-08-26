---
otero_id: 26470
otero_key: "54NFXP7Y"
title: "Measuring Switching Costs and the Determinants of Customer Retention in Internet-Enabled Businesses: A Study of the Online Brokerage Industry"
authors: "Pei-Yu (Sharon) Chen; Lorin M. Hitt"
year: "2002"
journal: "Information Systems Research"
doi: "10.1287/isre.13.3.255.78"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Measuring Switching Costs and the Determinants of Customer Retention in Internet-Enabled Businesses: A Study of the Online Brokerage Industry

Pei-Yu (Sharon) Chen • Lorin M. Hitt

Graduate School of Industrial Administration, Carnegie Mellon University, 5000 Forbes Avenue, Pittsburgh, Pennsylvania 15213

The Wharton School, University of Pennsylvania, 1318 Steinberg Hall-Dietrich Hall, Philadelphia, Pennsylvania 19104 pychen@andrew.cmu.edu • lhitt@wharton.upenn.edu

online businesses, especially those that invest heavily in advertising and customer acquisition. In this paper, we develop and implement an approach for measuring the magnitudes of switching costs and brand loyalty for online service providers based on the random utility modeling framework. We then examine how systems usage, service design, and other firmand individual-level factors affect switching and retention. Using data on the online brokerage industry, we find significant variation (as much as a factor of two) in measured switching costs. We find that customer demographic characteristics have little effect on switching, but that systems usage measures and systems quality are associated with reduced switching. We also find that firm characteristics such as product line breadth and quality reduce switching and may also reduce customer attrition. Overall, we conclude that online brokerage firms appear to have different abilities in retaining customers and have considerable control over their switching costs.

(Switching Cost; Electronic Markets; Customer Retention)

## 1. Introduction

Many emerging e-commerce companies, especially those focused on business-to-consumer (B2C) e-commerce, are in an aggressive phase of recruiting new customers in what analysts have called a “land grab.” These firms devote a large amount of their resources to advertising and promotion, and increasingly to outright customer subsidies. For example, E\*trade was offering \$400 in free computer merchandise for new customers who signed up between January and March 2000. E\*trade also spent about \$400 million in 1999 on selling and marketing, representing over 60% of their noninterest expenses and over 45% of net revenue. Customer acquisition costs, which are estimated to range from about \$40 per customer for Amazon.com to over \$400 for some online brokers (McVey 2000), are probably the largest contributor of cost to new B2C start-ups and represent a substantial portion of the initial financial losses these firms typically incur. Clearly, the expectation is that these early investments in customer acquisition will result in a long-term stream of profits from loyal customers, which will offset these costs.

Essential to this strategy is that customers experience some form of “lock-in” or switching costs to prevent them from defecting to another provider; otherwise firms would be unable to recover their initial investments in acquisition. These switching costs arise from a variety of factors, including the general nature of the product, the characteristics of customers that firms attract, or deliberate strategies and investments by product and service providers. By creating or exploiting switching costs, firms can soften price competition, build a “first mover” advantage, and earn supranormal profits on advertising or other investments (see the survey in Klemperer 1995). The ability to create switching costs and build customer loyalty has also been argued to be a major driver of success in e-commerce businesses (Reinchheld and Schefter 2000). However, it has been observed that over 50% of customers stop visiting completely before their third anniversary (Reinchheld and Schefter 2000). If switching costs are inherently low and firms are unable to lock in customers, long-term profitability may be difficult to attain, especially in many B2C e-commerce environments with low entry barriers (other than customer acquisition costs) and limited differentiation. As a result, it becomes critical for a firm to manage its retention ability, which is determined by switching costs and attrition rates. The first step for managing retention is to be able to measure the magnitude of switching cost and identify what factors affect switching and attrition. As Shapiro and Varian (1998) argue,

## You just cannot compete effectively in the information economy unless you know how to identify, measure, and understand switching costs and map strategy accordingly (p. 133).

Despite the critical role of switching costs in ecommerce strategy, there is surprisingly little empirical evidence about the presence, magnitude, or impact of switching costs on customer behavior. This appears to be true more broadly: Despite a robust theoretical literature, there are only a limited number of empirical analyses on the measurement of switching costs (Elzinga and Mills 1998, Kim et al. 2001), and even fewer that consider how firms might influence their customers’ switching costs. A few studies in the information systems and e-commerce literature have looked at related questions, such as price premia for branded retailers (Brynjolfsson and Smith 2000), the relationship between visit frequency and website experience (Moe and Fader 2000), customers’ propensity to search (Johnson et al. 2000), and the relationship between customer satisfaction and loyalty in online and offline environments (Shankar et al. 2000). However, these studies only investigate some aspects of switching or brand loyalty, and do not consider the factors that influence switching cost. In particular, they do not explore how systems characteristics or systems usage affect retention (a key research question identified by Straub and Watson 2001).

In this paper, we make three specific contributions. First, we utilize Web site traffic data to measure switching costs for online service providers, basing this on the well-known random utility/discrete choice modeling framework (McFadden 1974a).<sup>1</sup> Second, we measure how systems design variables as well as other customer and firm-specific characteristics affect switching as well as adoption behavior and attrition. Finally, we apply this model to study the online brokerage industry—a large and important online industry where switching cost and customer acquisition are a critical part of firm strategy and performance.

Using “clickstream” data on over 2000 individuals that utilize the 11 largest online broker sites provided by Media Metrix, we find that there is substantial heterogeneity in switching costs across providers, and that this variation is robust over time and after correcting for measurement biases and heterogeneity in customer characteristics. Moreover, we show that systems characteristics and systems usage as well as other firm and customer characteristics are related to a firm’s rate of switching, customer acquisition and attrition.

Overall, our analysis contributes to the literature on electronic commerce measurement and IS research by contributing approaches and measures for the analysis of customer retention using data commonly available for online service providers, as well as demonstrating the relationship between traditional information systems characteristics (e.g., DeLone and McLean 1992) and online consumer behavior. Moreover, our approach can be used in practice to measure and compare switching costs and enable firms to understand their retention effectiveness and evaluating alternative methods for managing customer retention through systems design changes and improvements in other service characteristics.

## 2. Literature Review and Background

## 2.1. Brand Loyalty and Switching Costs

In many markets, consumers face nonnegligible costs of switching between different brands of products or services. As classified by Klemperer (1987), there are at least three types of switching costs: transaction costs, learning costs, and artificial or contractual costs. Transaction costs are costs that occur to start a new relationship with a provider and sometimes also include the costs necessary to terminate an existing relationship. Learning costs represent the effort required by the customer to reach the same level of comfort or facility with a new product as they had for an old product. Artificial switching costs are created by deliberate actions of firms: frequent flyer programs, repeat-purchase discounts, and “clickthrough” rewards are all examples. Besides these explicit costs, there are also implicit switching costs associated with decision biases (e.g., the “Status Quo Bias”) and risk aversion, especially when the customer is uncertain about the quality of other products or brands.

Economists have noted that switching costs can affect a variety of critical competitive phenomena. For instance, switching costs have been linked to prices, entry decisions, new product diffusion patterns, and price wars (Klemperer 1987, 1995, Beggs and Klemperer 1992, Farrell and Shapiro 1988). Much of the economics literature has focused on market-wide switching costs—those faced by all adopters of a product (Kim et al. 2001) or addressed some specific forms of switching costs. For example, switching costs due to product compatibility or network externalities (e.g., Katz and Shapiro 1985) has been extensively studied, both in general and more specifically in software markets (Bresnahan 2001). Although the economics literature has stressed the importance of switching costs, less emphasis has been placed on switching costs that can be deliberately varied by firms through retention investments or by customer heterogeneity in switching cost or brand loyalty, the emphasis of the parallel literature in marketing.

The marketing literature has not focused on switching costs directly but has extensively examined customer product choice behavior including the choice to change providers or products. The focus of this literature has been on the concept of “brand loyalty” which is the tendency of at least some consumers to engage in repeat purchases of the same brand over time. There are many explanations for brand loyalty, including customer inertia, decision biases, uncertainty in the quality of other brands, or other psychological issues. Much of this extensive literature emphasizes the identification of loyal customers (Jacoby and Chestnet 1978) by individual behaviors such as repeat purchases or expressed preferences in surveys or focus groups, or the study of how marketing variables affect customers’ repeat purchase behaviors or firms’ ability in attracting loyal customers or switchers. However, this research has not directly measured the magnitudes of switching costs faced by customers at different firms.

Typically, the information systems literature has adopted the economic approach, focusing on marketwide switching costs and tangible forms of switching costs, such as contractual commitments, relationshipspecific investments, compatibility, and network externalities. However, much of this work has centered around specific technology investments rather than IT enabled services. Moreover, while there has been extensive discussion of information systems characteristics that could influence customers’ initial choices or adoption (see the meta-analysis in DeLone and McLean 1992); to our knowledge, there is little literature on how system quality and usage variables influence switching and attrition.

## 2.2. Brand Loyalty and Switching Costs in Electronic Markets

While electronic markets appear to have low switching costs since a competing firm is “just a click away” (Friedman 1999), recent research suggests that there is significant evidence of brand loyalty in electronic markets. For example, using data from a price comparison service (the DealTime “shopbot”), Brynjolfsson and Smith (2000) found that customers were willing to pay premium prices for books from the retailers they had dealt with previously. Johnson et al. (2000) showed that 70% of the CD and book shoppers are loyal to just one site and consumers tend to search fewer sites as they become more experienced with online shopping. One possible explanation for these findings is that firms have found ways to retain customers in the online channel that introduce new “frictions” where old ones, such as difficulty in searching and making comparisons, have been removed. Examples include frequent-purchaser programs, use of user profiles for personalization, “clickthrough” rewards, and affiliate programs (Varian 1999, Smith et al. 1999, Bakos 2001). Others have suggested that online retention is influenced indirectly through engaging website design (Novak et al. 2000). However, the drivers of retention have proven difficult to determine empirically because of a lack of suitable measurement methods and data.

## 2.3. Setting: The Online Brokerage Industry

Retail brokers provide individual investors with the ability to buy and sell bonds and other financial instruments. Online brokers differ from their traditional counterparts in the discount brokerage segment by conducting the vast majority of their transactional activity using the Internet.

This industry is an interesting candidate to study for a number of reasons. First, the market is large and significant and is considered to be one of the “killer applications” in B2C electronic commerce (Varian 1998, Bakos et al. 2000). There were over 140 online retail brokers by the end of 1999 and they managed just over \$1 trillion in customer assets in 2000. By year-end 1999, these accounts represented about 15% of all brokerage assets and 30% of all retail stock trades (Saloman Smith Barney 2000). Second, as noted in the Introduction, this industry has very aggressive customer acquisition tactics, partially because of the high lifetime value of an active account (\$1000). Third, the complexity and financial significance of a stock trade makes it likely that consumers generally face learning costs and other deterrents to switching, including a difficult process of either transferring assets or liquidating stock positions in order to switch brokers. Finally, the industry has a diversity of potential customer retention tactics, which enables the study of these factors and their influence on customer switching and retention.

## 3. Hypotheses and Methodology

## 3.1. Key Constructs and Hypotheses

For our purposes, we define switching as a change of the major brokerage firm by a customer and attrition as cessation of a customer’s brokerage activity entirely throughout a designated time period. Switching behavior is influenced by switching costs, which are defined as any perceived disutility a customer would experience from switching service providers. User behavior and system design characteristics also influence switching and attrition as do Web site quality, ease of use, and cost, all of which are well-established constructs in the IS literature. Web site personalization has been added as an e-commerce distinctive construct in this group. Moreover, customer behaviors (especially system usage variables) and characteristics may also be related to the switching or attrition decision. Table 1 summarizes these factors along with descriptions and variable names.

We begin with a simple (null) hypothesis:

Hypothesis 1. There are no significant differences in measured switching costs across firms.

To the extent that this hypothesis can be rejected and switching costs vary, our analysis will focus on distinguishing the role of firm and customer effects because they are associated with different observable variables and have different strategic implications. If switching behavior is driven solely by customer characteristics, then the challenge for firms is to target and prescreen customers who are more likely to be loyal either through observable attributes or past behaviors. If it is solely due to firm practices, then the challenge is to design their service offerings and products such that they either attract loyal customers or lock in customers once they are acquired. Our empirical analysis will attempt to distinguish these effects by statistically controlling for the influence of customer heterogeneity. Thus, we formulate our second hypothesis as:

Hypothesis 2. There are no significant differences in measured switching costs across firms after controlling for customer characteristics.

The most commonly studied customer characteristic in consumer behavior research is demographics.

Table 1 Constructs and Measures Used in this Study

<table><tr><td>Constructs/Subconstructs</td><td>Description or Definitions</td><td>Code or Measures</td></tr><tr><td colspan="3">IS constructs</td></tr><tr><td>Quality</td><td>Summary measurement of system and information quality regarding the Web site</td><td>Because customer confidence level is positively correlated with the level of system and information quality, we use the Gomez Index on Customer Confidence as a measure of system and information quality. Higher value is related to higher customer confidence.</td></tr><tr><td>Ease of use</td><td>Ease of use of the Web site</td><td>From Gomez Index: Ease of Use. Higher value stands for easier to use.</td></tr><tr><td>Personalization</td><td>The degree of Web site personalization</td><td>From Gomez Index: Relationship Services. Higher value means higher degree of personalization.</td></tr><tr><td>Web site usage</td><td>Web site usage by customers</td><td>We measure Web site usage by visiting frequency. Visiting frequency is measured by the number of days in a quarter a customer has visited the restricted pages (for account holders only) on the Web site.*</td></tr><tr><td>Change in usage</td><td>Changes in visiting frequencies by a customer</td><td>Change in usage pattern is measured by the differences in usage (visiting frequency) between two periods divided by the former period&#x27;s usage, i.e., |period 2 freq. - period 1 freq./period 1 freq.l.</td></tr><tr><td colspan="3">Customer characteristics</td></tr><tr><td>Age</td><td>Age of the customer</td><td>The age of the customer.</td></tr><tr><td>Female (dummy)</td><td>Gender</td><td>Female = 1 for Female; Female = 0 for Male.</td></tr><tr><td>Hhsize (dummy)</td><td>Number of people in the household</td><td>Number of people in the household.</td></tr><tr><td>Race1, Race3 (two dummies)</td><td>Race</td><td>1 = White, 3 = Oriental, 4 = Black and other.</td></tr><tr><td>Hhinc</td><td>Household income</td><td>Household income.</td></tr><tr><td>Education</td><td>Education</td><td>1 = Grade school, 2 = Some high school, 3 = Graduated high school, 4 = Some college, 5 = Graduated college, 6 = Post graduate school.</td></tr><tr><td>Mktsize (four dummies)</td><td>Market size—MSA</td><td>3 = 50,000–499,999; 4 = 500,000–999,999; 5 = 1,000,000–2,499,999; 6 = 2,500,000 and over; 9 = Non-MSA.</td></tr><tr><td>Marital status (two dummies)</td><td>Marital Status</td><td>1 = Married, 3 = Widowed or divorced or separate, 4 = Single.</td></tr><tr><td>Occupation (five dummies)</td><td>Occupation</td><td>1 = Professional; 2 = Proprietors, Managers, Officials; 4 = Sales; 5 = Craftsmen, Foremen or operative; = Retired, Unemployed; o = Others.</td></tr><tr><td>No. of brokers</td><td>Number of different brokers the user adopts</td><td>This variable is used to capture the degree of a customer&#x27;s loyalty level or propensity of switching. Presumably, the more brokers a customer adopts, the more likely she would switch since the level of switching cost is lower.</td></tr><tr><td colspan="3">Firm attributes</td></tr><tr><td>Resources</td><td>Breadth of offerings or product variety</td><td>From Gomez Index: Online Resources. Higher value represents more online resources.</td></tr><tr><td>Cost</td><td>Overall cost level of the broker</td><td>From Gomez Index: Overall Cost index. Higher value indicates lower cost.</td></tr><tr><td>Minimum deposit</td><td>Minimum deposit required to open an account</td><td>Measured in thousands.</td></tr><tr><td>Broker dummies (10 dummies)</td><td>Specific retention strategy controlled by firms</td><td>Broker dummies.</td></tr></table>

\*Our measure of access (number of days visited) differs from traditional Web site visit metrics such as visits or page views (see Alpar et al. 2001 for a discussion) because of the nature of online brokerage industry. Most importantly, this industry differs from most other Web sites in that revenue is earned principally through transaction fees rather than advertising.

However, since demographics and other intrinsic customer characteristics are unchanging over time, we do not expect that these factors directly affect switching as long as consumers are well enough informed to make good initial product choices. However, they may be indirectly correlated with other customer characteristics, which in turn affect retention. Thus, we expect demographics might have an effect, but cannot make a specific magnitude or sign prediction. On the other hand, various observed customer behaviors may be directly indicative of customer characteristics that affect switching. For instance, consumers who adopt multiple service providers may be inherently “disloyal” and more likely to switch. Customers who change their usage patterns might also be more inclined to switch to the extent this suggests a change in underlying preferences. However, Web site usage itself does not have a clear prediction—on the one hand, usage might suggest learning or other psychological lock in at a service provider, indicating lower switching propensity (as suggested by Johnson et al. 2000). One the other hand, high-usage customers might also have the greatest incentive for maximizing service provider “fit,” and could be more likely to switch. Based on the discussion above, we can directly examine the effects of customer characteristics on switching. Our hypotheses are:

Hypothesis 3a. Use of multiple brokers is positively correlated with switching.

Hypothesis 3b. Changes in usage patterns is positively correlated with switching.

Hypothesis 3c. High volume of Web site usage is negatively correlated with switching.

We next consider how various firm-specific practices affect switching beyond the effects of differences in customer characteristics. While partially constrained by data availability, we are able to capture many of the central factors that might affect switching. Cost and quality are probably the best studied factors in IS, marketing, or economic models affecting consumer demand. In general, higher quality may reduce switching because it may build greater affinity with customers and decrease the chance of a negative customer service interaction (Boulding et al. 1993, Gans 2000). We have no particular prediction of the effect of cost—while cost is often an important decision on which service to adopt, customers are generally fully informed about cost and thus it is doubtful that it has an effect on switching. A third factor which has been identified in previous IT value research is product variety (Brynjolfsson and Hitt 1995). While this clearly contributes to customer value, it may also deter switching since firms that offer a broader product line can satisfy a greater range of customer needs, especially if needs change over time.

We are also interested in two specific factors directly related to computer-mediated services: Web site personalization and ease of use. Internet firms are increasingly able to tailor their customer interface and services to specific needs through personalization technologies—it is hoped that these technologies will build greater customer lock in and retention (Crosby and Stephens 1987, Pearson 1998, Mobasher et al. 2000, Cingil et al. 2000). Ease of use has been a critical factor in many studies of IS adoption with the general perspective that ease of use promotes service adoption (DeLone and McLean 1992). However, in the context of switching there may be a negative effect: To the extent that easy to use sites do not force consumers to make sunk investments in learning, switching costs may indeed be lower for services that are easier to use (this is the converse of an argument made previously by Johnson et. al. 2000). Overall, we expect:

Hypothesis 4a. Switching is negatively correlated with Web site personalization.

Hypothesis 4b. Switching is positively correlated with Web site ease of use.

Hypothesis 4c. Switching is negatively correlated with Web site quality.

Hypothesis 4d. Switching is negatively correlated with breadth of offerings.

Hypothesis 4e. Switching is not related to cost.<sup>2</sup>

These predictions are summarized in Figure 1.

Figure 1 Graphical Research Model on Switching and Attrition (Variables Emphasized in Previous IS Research are Italicized)  
![](/api/attachments/54NFXP7Y/fulltext/images/6bbe60632de442f5d1841d61ead66af72a4b17b2048833a320232ca549597b91.jpg)

In addition to the focus on switching, it may also be useful to consider the closely related issue of customer attrition since it is the absence of both switching and attrition that determines a firm’s ability to retain customers. The predictions on attrition largely parallel that of switching. As before, we have no strong predictions for demographics, although we would expect higher volume users and those with multiple brokers to be less likely to disappear, suggesting that some behavioral characteristics will matter.

Hypothesis 5a. Use of multiple brokers is negatively correlated with attrition.

Hypothesis 5b. High volume of Web site usage is negatively correlated with attrition.

By the same arguments as for switching, we would generally expect that personalization, quality, and breadth of offerings reduce attrition, and cost should have little effect. However, we expect ease of use to play a different role here—customers may be more likely to depart because the interface is too difficult to use. Also, we consider an additional factor, minimum account sizes (the amount of money the customer must deposit upon initiating an account), that could act as a screen against customers who intend only to collect new user subsides but not to actually use the service. We therefore expect:

Hypothesis 6a. Customer attrition is negatively correlated with Web site personalization.

Hypothesis 6b. Customer attrition is negatively correlated with Web site quality.

Hypothesis 6c. Customer attrition is negatively correlated with breadth of offerings.

Hypothesis 6d. Customer attrition is negatively correlated with Web site ease of use.

Hypothesis 6e. Customer attrition is not related to cost.

Hypothesis 6f. Customer attrition is negatively correlated with account minimums.

Again, these predictions are graphically summarized in Figure 1.

3.2. Methodology: Measurement of Switching Cost To examine Hypotheses 1 and 2, we devised a technique for measuring switching costs based on the random utility framework (McFadden 1974a). Random utility models have been extensively applied in studying consumer choice behavior among multiple products (McFadden 1974b, Guadagni and Little 1983, Brynjolfsson and Smith 2000). Our analysis relies on comparing the choice behavior of new customers with those of existing customers. If there were no switching costs, new customers and existing customers would choose brokers in exactly the same proportion based on average quality levels. However, if existing customers stay with their previous service providers at a disproportionate rate (relative to new adopters), this suggests some barrier to switching. Thus, we can infer switching cost by examining choice probabilities of new versus existing customers.

In our setting, the choices are brokerage firms, and the systematic component of utility includes aspects specific to the brokerage firms chosen: a price index $( r _ { j } ) _ { \ l }$ , a vector of nonprice attributes $( x _ { j } ) _ { j }$ , and a unique dummy variable for each firm to capture unobservable firm-specific effects $( \gamma _ { j } )$ . Consumer choice is also affected by characteristics of individuals: A vector of customer characteristics $( z ^ { i } )$ and a set of dummy variables (W), capturing where the customer is from. The underlying model for our analysis:

$$
\begin{array}{r} u _ {j} ^ {i} = \gamma_ {j} + x _ {j} \beta - r _ {j} \alpha + z ^ {i} \lambda_ {j} - \sum_ {k = 1} ^ {M} s _ {k} W _ {k} ^ {i} + \varepsilon_ {j} ^ {i} \\ \forall i \in [ 1, 2, \ldots , N ], \forall j \in [ 1, 2, \ldots , M ]. \end{array}\tag{1}
$$

In this model, $\gamma$ (an unobserved firm-specific effect), b (a vector of utility weights reflecting the importance of nonprice attributes $x _ { j } ) _ { \ l }$ ,  (the utility weight reflecting the importance of price index $r _ { j } ) , \lambda _ { j }$ (the customer preference parameters for firm $j ) ,$ , and $s _ { j }$ (switching cost of firm $j )$ are to be estimated. The estimation of the switching cost parameters $( s _ { j } )$ is our primary concern. Utility $( u _ { j } ^ { i } )$ is an unobserved latent variable that is revealed through a customer’s choice of service provider (that is, we know that when customer i chooses firm j, this choice maximizes her utility). Several additiona notes about this formulation are in order. First, this model is typically implemented by simultaneously estimating individual logistic (binary) choice equations for each firm for each customer—this yields a total of M firms $\times N$ individuals or $M \times N$ data points. In the discussion that follows, we will sometimes refer to one of the individual firms’ equations. Second, our only deviation from the standard model is the inclusion of a vector of dummy variables, one element per firm, $\boldsymbol { W } _ { k } ^ { i } ,$ which takes on the value of one if customer i is a potential switcher from firm k and zero otherwise. In other words, the dummy variable is one whenever a customer of a particular firm would face a switching cost if they chose to switch to another. The estimated values of the parameters on this set of dummy variables $( W _ { k } )$ are the mean level of switching costs $( s _ { k } )$ for each firm—the cost (disutility) a consumer must overcome when switching from firm k $( k \in [ 1 , 2 , . . . , M )$ to another firm. Note that we have implicitly assumed that the switching cost does not depend on the firm the customer switches $^ { \mathrm { t o , } }$ but only on the firm she switches from (a testable assumption and one satisfied by our data).<sup>3</sup> Third, the use of the conditional logit estimation method embeds an assumption about consumer choice known as “independence of irrelevant alternatives” (IIA). This is the assumption that the relative utility of any two products is independent of the characteristics of products other than the ones compared (this is also testable and satisfied by our data). Finally, we note that this is a choice equation over firms where the switching cost parameters are estimated—the firm and price effects do not represent the effects on switching cost but the effect on overall choice. We will assess drivers of customer retention in a separate analysis.

## 3.3. Methodology: Drivers of Switching and Attrition

To estimate the effects of firm attributes and customer characteristics on switching (for Hypotheses 3 and 4), we can proceed in two ways. First, we can compute switching cost estimates for each firm and regress these on firm and customer characteristics. However, this strategy is limited in this context by the small number of firms and time periods (a total of 33 estimates across three quarters), and thus, may have low statistical power. It also does not enable direct comparisons with adoption or attrition predictors, nor can it easily examine customer-specific effects. Alternatively, rather than testing the direct effect of firm attributes on switching costs, we can test how firm attributes and customer characteristics influence customers’ switching behaviors. That is, we predict switching as a function of customer characteristics and firm attributes using logistic regression. Formally, we estimate the model:

$$
\begin{array}{r l} & {\log \frac {\operatorname * {P r} (S w i t c h)}{1 - \operatorname * {P r} (S w i t c h)}} \\ & {\quad = \gamma_ {j} ^ {s} + \beta^ {s} x _ {j} - \alpha^ {s} r _ {j} + \lambda^ {s} z ^ {i} + \varepsilon_ {j} ^ {i}.} \end{array}\tag{2}
$$

Switch is a variable that is one if the customer switches, and zero otherwise. The parameters $( \gamma ^ { s } , \beta ^ { s } , \alpha ^ { s } , \lambda ^ { s } )$ are analogous to (but not the same as) the parameters included in the switching cost estimation model (1)—we use the superscript s to distinguish these coefficients from those in the earlier analysis. These parameters represent the influence of time-invariant, firm-specific switching effects, the effects of firm practices, the effects of price, and the effects of customer characteristics on switching rates, respectively.

Similarly, we can study the effects of firm attributes and customer characteristics on attrition (for Hypotheses 5 and 6) by the following model:

$$
\begin{array}{l} \log \frac {\operatorname * {P r} (A t t r i t)}{1 - \operatorname * {P r} (A t t r i t)} \\ = \gamma_ {j} ^ {a} + \beta^ {a} x _ {j} - \alpha^ {a} r _ {j} + \lambda^ {a} z ^ {i} + \varepsilon_ {j} ^ {i}. \end{array}\tag{3}
$$

Attrit is a variable that is 1 if the customer ceases all brokerage activities through the end of our data period, and zero otherwise. The parameters $( \gamma ^ { a } , \beta ^ { a } , \alpha ^ { a } , \lambda ^ { a } )$ parallel those included in the estimation model (2) with superscript a to distinguish these coefficients.

## 3.4. Data: Site Usage

Our primary data for this study is drawn from a panel of “clickstream” data provided by Media Metrix. Media Metrix has a panel of more than 25,000 households that have an applet installed in their computers that tracks the user, time, and URL of every page request they make on the World Wide Web. They also collect demographic information from the users (gender, household income, age, education level, occupation, race, etc.). This enables us to use the data for individual-level control variables, and also enables Media Metrix to ensure that their panel is demographically consistent over time and representative of the U.S. Internet-using population. Our analysis is focused on four consecutive quarters of data from July 1999 to June 2000 which we label Q399, Q499, Q100, and Q200. We restrict our analysis to customers who are tracked by Media Metrix in all four quarters so that we can get proper estimates of the number of first period nonadopters and track customer flow during this time frame.

Using analyst reports (Salomon Smith Barney and Morgan Stanley Dean Witter), we identified the 11 largest retail brokers,<sup>4</sup> which account for over 95% of all online brokerage accounts, and extracted all page references to these sites. We use the number of days that a broker is accessed and total time spent in a quarter as a proxy for activity at the broker. We restrict our analysis to individuals who are registered account holders at these brokers—individuals who browse broker sites that do not have an account are excluded. To determine whether a customer is an account-holder, we examine the individual URLs that each customer visited—If they accessed any pages that are restricted to account-holders for at least five active seconds<sup>5</sup> during the period, we define the customer as an account holder. We corroborated our estimates of overall market share with other sources (Salomon Smith Barney and Morgan Stanley Dean Witter) and found them to be consistent with a Pearson correlation over 90% and 98% rank order correlation.

There are two key limitations of these data. First, while we can tell whether the customer is an account holder, we cannot determine their trading volume, since in general, we cannot identify whether a page view corresponds to a trade. However, previous studies have suggested a positive relationship between visiting frequency and purchase propensity (Roy 1994, Moe and Fader 2000). This suggests that people who visit a broker more frequently will be more likely to trade.

A second issue is that our data covers home usage but not work usage. Given that significant trading activity in many accounts occurs during the daytime when the financial markets are open, our visit frequencies may not be indicative of trading activity. However, as long as there is positive connection between visiting frequency and trading propensity, which is very likely to be true, then visiting frequency still contains valuable information. More importantly, to the extent that most users utilize these sites for both trading (during market hours) and research and financial management in the off hours, we are not likely to be missing the overall adoption decision. There are also possible errors introduced by the presence of financial services aggregators (e.g., Yodlee.com) that enable customers to manage their accounts without visiting their brokers’ site but these services are used by less than 1% of the customers in our analysis. We address the general problem of missing some customer usage of these sites by aggregating our data to calendar quarters—this way, if a customer makes any access to these sites during the quarter, we will properly capture their broker choices.

In our sample, 80% (2,321) of the customers have only one broker at any one point in time. For the remaining 20%, we define a “major broker” for each customer to be the broker whose account holders’ pages the customer visits most often. Our switching analysis therefore focuses on customers who change their major broker. We chose this strategy for several reasons. First, and most importantly, it allows us to accommodate users with multiple brokers. Second, it enables us to compare the switching behavior of multiple broker users to other customers, since we would generally believe that these customers face lower switching costs. Finally, our results do not appear to be sensitive to this assumption, as similar switching cost estimates were found in earlier work that tracks all accounts (Chen and Hitt 2000).

## 3.5. Data: Broker Characteristics

We also utilize additional data from Gomez Advisors, an online market research firm, to determine the attributes of the sites we study. Gomez tracks firm-level characteristics in five dimensions: cost, consumer confidence (related to an abstract notion of “quality” and our construct Web site quality), online resources (breadth of offerings), relationship services (equivalent to a degree of personalization), and ease of use. These factors are broadly representative of the factors used by other consumer rating services, but have the advantage that they are defined by analysts rather than consumers (thus removing possible biases of customer heterogeneity), measured consistently over time, and are measured by an extensive measurement process at a finer level of granularity than other rating services that principally provide an “overall satisfaction” score.<sup>6</sup> The definitions and measurements of these factors are also listed in the Appendix as publicly described by Gomez (no data was available on the subcomponents of these scores that they use internally).

We also include a measure of the required initial investment to establish an account for use in the attrition analysis gathered directly from the brokers’ Web sites.

## 4. Data Analysis

4.1. Summary Statistics and Preliminary Analysis Among our four datasets from Media Metrix, we have a total of 28,807 households, of which 11,397 households are tracked throughout the period of interest (this includes both Web users who use online brokers and Web users who do not). Restricting our sample to only individuals that appear in all datasets, we have 1,249 broker users in Q399, 1,393 in Q499, 1,780 in Q100, and 1,586 in Q200. Overall, we have 2,902 unique broker users, including 1,653 new adopters during the year of interest. Figure 2 shows the movement of customers among different categories between two consecutive quarters.

Among the 2,902 unique users (from 2,257 households) we examine, 303 of them changed their major broker during the time period tracked. Figure 3 shows user flow by broker. For example, among all E\*Trade users, 55.7% of them remain active and stay with

Figure 2 Customer Flow Diagram (Sample Period: Q3–99 to Q4–99)  
![](/api/attachments/54NFXP7Y/fulltext/images/0697649155569cab370fe150602810a425a44649db95a2f6b1593890495693e2.jpg)

E\*Trade, 10.6% of them switch out, while 33.7% of them become inactive. Note that we define inactive as not returning to a broker at any time in the future through the end of our data period (as opposed to simply having no access during an intermediate period and then returning in a later period). As evident from Figure 3, there is considerable variation on switching and attrition rates. Schwab and Datek have a higher retention rate than DLJDirect, E\*Trade, MSDW, and Vanguard. For the top three brokers, E\*Trade has the most serious problem of customer departure. Their switching rate is more than 1.5 times that of Fidelity and Schwab, and attrition rate is the highest across all brokers we examine. These differences in flow rates are both economically and statistically significant $( \chi ^ { 2 } ( 2 0 )$ $= 6 9 . 3 2 , p < 0 . 0 0 1 $ ). Moreover, retention rates, switching rates, and attrition rates across brokers are all economically and statistically different $( p < 0 . 0 0 1 )$

## 4.2. Variation in Switching Costs

We can calculate switching costs for each broker based on the estimation model (1). Because the units of the switching cost measure are ambiguous (because of the scaling of variables used in the analysis<sup>7</sup>), we treat these estimates as relative values.

We begin by estimating a simple conditional logit model that computes switching cost using Estimation Model (1), including controls for firm attributes, firmspecific dummy variables, and time dummy variables. This analysis yields switching cost estimates (Table 2, Column 1). To examine Hypothesis 1 (equivalence of switching costs), we test whether all firms have the same switching cost—this is clearly rejected $( \chi ^ { 2 } ( 1 0 ) =$ 189, p  0.0001). The estimated switching costs, with 95% confidence intervals, are shown in Figure 4a.

More interestingly, the switching cost estimates are not substantially changed if we include a full set of demographic controls<sup>8</sup> in the analysis (Table 2, Column 2). The estimated switching costs after controls for customer heterogeneity, with 95% confidence intervals, are shown in Figure 4b. Based on the regression results, we are again able to easily reject the hypothesis that switching costs are identical across

Figure 3 Customer Flow Rates  
![](/api/attachments/54NFXP7Y/fulltext/images/5afbcd9f90bb8ea4ba57b6dd8f025f3a2221624703441823f1c0858da73b75b2.jpg)

Table 2 Estimated Switching Costs

<table><tr><td></td><td>Regression 1</td><td>Regression 2</td></tr><tr><td>AMERITRADE</td><td>4.07 (0.20)</td><td>3.97 (0.22)</td></tr><tr><td>DATEK</td><td>5.30 (0.34)</td><td>5.18 (0.37)</td></tr><tr><td>DLJDIRECT</td><td>4.70 (0.27)</td><td>4.79 (0.29)</td></tr><tr><td>ETRADE</td><td>2.77 (0.12)</td><td>2.72 (0.13)</td></tr><tr><td>FIDELITY</td><td>3.53 (0.13)</td><td>3.60 (0.15)</td></tr><tr><td>FLEET</td><td>5.29 (0.33)</td><td>5.49 (0.41)</td></tr><tr><td>MSDW</td><td>5.22 (0.39)</td><td>5.26 (0.47)</td></tr><tr><td>NDB</td><td>7.36 (0.75)</td><td>8.80 (1.23)</td></tr><tr><td>SCHWAB</td><td>4.05 (0.16)</td><td>4.02 (0.18)</td></tr><tr><td>TDWATERHOUSE</td><td>4.87 (0.23)</td><td>5.09 (0.27)</td></tr><tr><td>VANGUARD</td><td>4.34 (0.23)</td><td>4.38 (0.25)</td></tr></table>

Note.

Regression 1: switching cost measures without controls for customer heterogeneity. Standard error in parenthesis.

Regression 2: switching cost measures after controls for customer heterogeneity. Standard error in parenthesis.

brokers even controlling for demographics and individual customer characteristics $( \chi ^ { 2 } ( 1 0 ) ~ = ~ 1 6 2 , ~ p ~ <$ 0.0001). For example, we find that E\*Trade has significantly lower switching cost than all the other brokers we track (Figure 4b). It is also notable that Figures 4a and b are quite similar, suggesting that the overall effect of customer characteristics on switching is small. We therefore can also reject Hypothesis 2 (equivalence of switching cost, controlling for customer characteristics). Overall, this suggests that there is a significant firm-specific component of switching cost. We will explore this variation in the next section.

Now we examine the robustness of our model. As stated earlier, we made two assumptions in formulating the model: The IIA assumption and the assumption that switching costs depend only on the firm a customer switches from, and not on the destination firm. Since all brokers we examined are available to all users throughout the study period, we expect the independence assumption to hold, making the conditional (multinomial) logit the appropriate formulation. As expected, we find that the assumption of IIA cannot be rejected for our data based on the “mother logit model” (McFadden $^ { 1 9 7 4 } \mathrm { a } ,$ Kuhfeld 1996), including all cross effects $( p > 0 . 0 5 )$ . We also examined the later assumption by including all possible combinations of previous and new brokers in the model. Our analysis suggests that the hypothesis that the adoption distribution for switching customers is the same for all brokers cannot be rejected $( \chi ^ { 2 } ( 1 1 0 ) ~ = ~ 5 9 . 2 4 , ~ p ~ = ~ 1 . 0 0 ) _ { \it B }$ validating this assumption. These two tests are actually closely linked, since both are implied by IIA, but differ in implementation.

## 4.3. Predictors of Switching Behavior

We have defined switching to be the change of customers’ major brokerage firm. In Table 3, we estimate three variants of Estimation Model (2) on switching. First, we examine a regression with only customer characteristics (Column 1). We find that demographics have little effect on overall switching behavior as expected. However, more specific indicators of individual differences are much better predictors of switching. Customers who have adopted fewer brokers are less likely to switch: This is consistent if we interpret this measure as capturing unobserved propensity to be loyal. In terms of systems usage variables, changes in usage affect switching, and interestingly, we find that level of Web site activity is associated with reduced switching, which is consistent with a story that greater experience with a service provider creates implicit lock in through learning (as suggested by Johnson et al. 2000). These results lend support to our arguments summarized in the discussion in Hypothesis 3.

In Table 3, Column 2, we also add characteristics of the brokers to the analysis (the measures are the characteristics of the broker a customer used in that period). Overall, we find that higher Web site quality (measuring system and information quality of the site) reduces switching, while Web site ease of use has a negative effect on customer retention. Surprisingly, the availability of Web site personalization is not shown to have significant effect on reducing switching, inconsistent with the idea that personalization leads to greater customer lock in.

In Table 3, Column 3, dummy variables for each broker dummies are added to the regression to capture any firm level effects on switching. This eliminates the influence of time-invariant broker attributes and thus changes the coefficient interpretation of the broker characteristics variables to the influence of changes in these factors. The coefficients on Web site quality and Web site ease of use are no longer significant in the firm-effects regression, suggesting that these characteristics do not vary highly over time. We do find a strong beneficial effect of increasing resources (breadth of product line) and also that Web site personalization now is marginally significant with the “wrong” sign. Thus, we find support for the assertions in Hypotheses 4b–e (firm-level determinants of switching), except for the result on personalization (Hypothesis 4a), in both levels and fixed effects regressions.

Figure 4a Switching Cost Measures With 95% Confidence Interva Without Controlling for Demographics  
![](/api/attachments/54NFXP7Y/fulltext/images/041ab43692af3536b3185dc535bd204fee071269f5362247bad6431f23d769ed.jpg)

Figure 4b Switching Cost Measures with 95% Confidence Interval After Control for Customer Heterogeneity  
![](/api/attachments/54NFXP7Y/fulltext/images/3c3925170b16380970c2fef39755b1bae1c16734bfa2ccd719b7976a372be3a6.jpg)

This analysis indicates that higher Web site quality and increasing product line breadth are helpful in reducing switching, but that most other factors have little influence on switching. However, we still find large firm-level variation in switching as evidenced by our earlier results and the strong significance levels of the broker dummies (Table 3, Column 3) even when control variables for specific practices are included. This suggests that, while we have identified some of the mechanisms by which firms might be able to influence customer retention, they still have significant control over their switching costs in ways other than the practices we have identified and measured.

Table 3 Predictors of Switching Behavior (Negative Is Less Switching)

<table><tr><td></td><td>REGRESSION 1</td><td>REGRESSION 2</td><td>REGRESSION 3</td></tr><tr><td>Intercept</td><td>-2.2375*** (0.550)</td><td>-0.6148 (1.180)</td><td>-0.7803 (1.572)</td></tr><tr><td>Age</td><td>-0.0091 (0.005)</td><td>-0.0080 (0.005)</td><td>-0.0070 (0.005)</td></tr><tr><td>Female</td><td>0.0859 (0.140)</td><td>0.1142 (0.142)</td><td>0.1009 (0.144)</td></tr><tr><td>Hhsize</td><td>0.0282 (0.056)</td><td>0.0351 (0.056)</td><td>0.0282 (0.057)</td></tr><tr><td>Race1 (White)</td><td>-0.1965 (0.251)</td><td>-0.2095 (0.254)</td><td>-0.1990 (0.257)</td></tr><tr><td>Race3 (Oriental)</td><td>0.3913 (0.325)</td><td>0.3159 (0.329)</td><td>0.4517 (0.336)</td></tr><tr><td>Hhinc</td><td>-0.0015 (0.002)</td><td>0.0015 (0.002)</td><td>0.0017 (0.002)</td></tr><tr><td>Education</td><td>-0.0813 (0.065)</td><td>-0.0823 (0.065)</td><td>-0.0859 (0.066)</td></tr><tr><td>Mktsize</td><td> $\chi^2(4) = 4.86; p = 0.30$ </td><td> $\chi^2(4) = 4.58; p = 0.33$ </td><td> $\chi^2(4) = 5.03; p = 0.28$ </td></tr><tr><td>Marital status</td><td> $\chi^2(2) = 0.02; p = 0.99$ </td><td> $\chi^2(2) = 0.17; p = 0.92$ </td><td> $\chi^2(2) = 0.17; p = 0.92$ </td></tr><tr><td>Occupation</td><td> $\chi^2(5) = 3.88; p = 0.57$ </td><td> $\chi^2(5) = 3.80; p = 0.58$ </td><td> $\chi^2(5) = 3.66 p = 0.60$ </td></tr><tr><td>Web site usage</td><td>-0.0783*** (0.010)</td><td>-0.0779*** (0.011)</td><td>-0.0748*** (0.010)</td></tr><tr><td>Change in usage</td><td>0.0562*** (0.015)</td><td>0.0563*** (0.016)</td><td>0.0579*** (0.016)</td></tr><tr><td>No. of brokers</td><td>1.0766*** (0.096)</td><td>1.0742*** (0.097)</td><td>1.0473*** (0.098)</td></tr><tr><td>Q100</td><td>-0.3845** (0.147)</td><td>-0.407** (0.150)</td><td>-0.3563* (0.155)</td></tr><tr><td>Q200</td><td>-0.4777** (0.151)</td><td>-0.2611 (0.191)</td><td>-0.3066 (0.194)</td></tr><tr><td>Ease of use</td><td></td><td>0.0989* (0.050)</td><td>0.0231 (0.072)</td></tr><tr><td>Quality</td><td></td><td>-0.1959* (0.096)</td><td>-0.1658 (0.100)</td></tr><tr><td>Resources</td><td></td><td>-0.0495 (0.116)</td><td>-0.4879*** (0.137)</td></tr><tr><td>Personalization</td><td></td><td>-0.1096 (0.146)</td><td>0.3227* (0.160)</td></tr><tr><td>Cost</td><td></td><td>0.00737 (0.064)</td><td>0.1559 (0.095)</td></tr><tr><td>Minimum deposit</td><td></td><td>0.0568 (0.071)</td><td></td></tr><tr><td>Broker dummies</td><td></td><td></td><td>(10)=35.8; p&lt;0.0001***</td></tr><tr><td>N</td><td>2824</td><td>2824</td><td>2824</td></tr><tr><td> $\chi^2$ </td><td>264.06***</td><td>278.09***</td><td>316.73***</td></tr></table>

Note. Standard errors in parenthesis; \*: p  0.05; \*\*: p  0.01; \*\*\*: $p < 0 . 0 0 1$

## 4.4. Drivers of Customer Attrition

In our earlier analysis, we found that attrition (customers who have a brokerage account at some time but do not return to any broker in the future) is a significant problem. Figure 3 shows that attrition rates range from 33.7% for E\*trade to 25% for Schwab. There are a variety of reasons for attrition, most notably customer experimentation, especially experimentation encouraged by subsidies. We conduct the same analysis for attrition that we performed for switching using Estimating Model (3).

In Table 4, we present four variations of the base model (the three considered previously for switching, and an additional model that includes only firmspecific dummy variables and demographics).

Behavioral variables tend to be good predictors of attrition: Frequent visitors and people with more accounts are less likely to become inactive, lending support to Hypotheses 5a and b. From Table 4, we find that there are strong seasonal effects in attrition—attrition rates rose dramatically in Q2 2000. In addition, our data shows that the average visit frequency in Q200 is only 85% of that in Q100. Besides these observed variables, we find that E\*Trade and Ameritrade have significantly greater attrition rates than Schwab (Table 4, Columns 2 and 4). Greater minimum deposits are effective in reducing attrition rate (Column 3) and, as before, cost has no effect and ease of use has a negative effect on attrition. These results are consistent with our prior arguments in Hypotheses 6e and 6f, with the exception that Web site personalization, quality, breadth of offerings, and ease of use are not found to have positive effects on attrition (Hypotheses 6a–d). The test results for all hypotheses are summarized in Table 5.

Table 4 Attrition Analysis (Negative Is Less Attrition; Baseline: Schwab)

<table><tr><td></td><td>Regression 1</td><td>Regression 2</td><td>Regression 3</td><td>Regression 4</td></tr><tr><td>Intercept</td><td>1.4291*** (0.372)</td><td>1.0916** (0.401)</td><td>1.2518 (0.939)</td><td>1.1759 (2.940)</td></tr><tr><td>Age</td><td>-0.0106*** (0.003)</td><td>-0.0093** (0.003)</td><td>-0.0091** (0.003)</td><td>-0.00947** (0.003)</td></tr><tr><td>Female</td><td>0.2415** (0.089)</td><td>0.2615** (0.090)</td><td>0.2698** (0.090)</td><td>0.2506** (0.090)</td></tr><tr><td>Education</td><td>-0.0901* (0.046)</td><td>-0.0935* (0.046)</td><td>-0.0910* (0.046)</td><td>-0.0952* (0.046)</td></tr><tr><td>Occupation</td><td> $\chi^2(5)=10.75; p=0.06$ </td><td> $\chi^2(5)=10.45; p=0.06$ </td><td> $\chi^2(5)=11.55; p=0.04^*$ </td><td> $\chi^2(2)=11.14; p=0.05^*$ </td></tr><tr><td>Web site usage</td><td>-0.2549*** (0.016)</td><td>-0.2536*** (0.016)</td><td>-0.2543*** (0.016)</td><td>-0.2548*** (0.016)</td></tr><tr><td>No. of brokers</td><td>-0.2161 (0.118)</td><td>-0.2512* (0.121)</td><td>-0.2361* (0.120)</td><td>-0.2402* (0.121)</td></tr><tr><td>Q100</td><td>0.2110 (0.110)</td><td>0.2089 (0.110)</td><td>0.1451 (0.112)</td><td>0.1017 (0.120)</td></tr><tr><td>Q200</td><td>1.1391*** (0.103)</td><td>1.1355*** (0.103)</td><td>1.0697*** (0.134)</td><td>1.187*** (0.164)</td></tr><tr><td>Ease of use</td><td></td><td></td><td>0.1359*** (0.040)</td><td>0.3462*** (0.080)</td></tr><tr><td>Quality</td><td></td><td></td><td>0.0525 (0.066)</td><td>-0.0396 (0.104)</td></tr><tr><td>Resources</td><td></td><td></td><td>0.1126 (0.083)</td><td>-0.1391 (0.186)</td></tr><tr><td>Personalization</td><td></td><td></td><td>0.0073 (0.101)</td><td>-0.00711 (0.165)</td></tr><tr><td>Cost</td><td></td><td></td><td>-0.004 (0.045)</td><td>-0.2397 (0.167)</td></tr><tr><td>Minimum deposit</td><td></td><td></td><td>-0.101* (0.047)</td><td></td></tr><tr><td>Ameritrade</td><td></td><td>0.4934** (0.188)</td><td></td><td>2.3448* (0.938)</td></tr><tr><td>Datek</td><td></td><td>0.0824 (0.260)</td><td></td><td>1.4091 (1.041)</td></tr><tr><td>DLJDirect</td><td></td><td>0.2554 (0.231)</td><td></td><td>0.877 (0.535)</td></tr><tr><td>E*Trade</td><td></td><td>0.5008*** (0.147)</td><td></td><td>1.0587* (0.461)</td></tr><tr><td>Fidelity</td><td></td><td>0.1303 (0.140)</td><td></td><td>0.6848** (0.217)</td></tr><tr><td>Fleet</td><td></td><td>0.3517 (0.268)</td><td></td><td>1.8843* (0.860)</td></tr><tr><td>MSDW</td><td></td><td>0.2669 (0.381)</td><td></td><td>0.1476 (0.803)</td></tr><tr><td>NDB</td><td></td><td>0.1965 (0.351)</td><td></td><td>1.0515 (0.633)</td></tr><tr><td>TDWaterhouse</td><td></td><td>0.099 (0.204)</td><td></td><td>2.1112** (0.810)</td></tr><tr><td>Vanguard</td><td></td><td>0.3981* (0.18)</td><td></td><td>1.675 (0.922)</td></tr><tr><td>N</td><td>3634</td><td>3634</td><td>3634</td><td>3634</td></tr><tr><td> $\chi^2$ </td><td>1009.24***</td><td>1029.83***</td><td>1037.28***</td><td>1052.14***</td></tr></table>

Note. Standard errors in parenthesis; \*-p  0.05; \*\*-p  0.01; \*\*\*-p  0.001; Some insignificant demographic variables omitted from table due to space considerations but included in the analysis (hhsize, race, hhinc, mktsize and marital status).

## 5. Discussion

Overall, our analysis suggests that, using a variety of techniques, there are substantial differences in switching costs across brokers and that this variation is not solely due to variations in customer characteristics, at least along the dimensions we can measure. We find usage and changes in usage to be good predictors of switching and attrition, suggesting the importance of systems usage variables on studying firms’ switching costs. We also find that firm characteristics such as minimum balance requirements, “site quality,” and cost, also influences customers’ behaviors.

Ideally, a firm would like a high acquisition rate and low switching and attrition rates. Our analysis enables us to make comparisons on the types of factors that might be generally more desirable in building a large and loyal customer base, while identifying others that involve tradeoffs among practices or may be unexpectedly undesirable. For example, high levels of customer service may increase acquisition and reduce switching and attrition, while low minimum account requirements may improve acquisition at the expense of increasing switching or attrition. Using analyses we discussed earlier, we can summarize these effects in a single table (Table 6), using a consistent set of control variables. Note that we have altered the signs of the coefficients such that “” is good, and “-” is bad; a factor is coded as “NS” if it is not statistically significant (p  0.05).

Table 5 Summary of Hypothesis Tests

<table><tr><td>Hypothesis</td><td>Test Result</td></tr><tr><td>1. There are no significant differences in measured switching costs across firms.</td><td>Not supported ( $p < 0.0001$ )</td></tr><tr><td>2. There are no significant differences in measured switching costs across firms after controlling for customer characteristics.</td><td>Not supported ( $p < 0.0001$ )</td></tr><tr><td>3a. Use of multiple brokers is positively correlated with switching.</td><td>Supported</td></tr><tr><td>3b. Changes in usage patterns are positively correlated with switching.</td><td>Supported</td></tr><tr><td>3c. High volume of Web site usage is negatively correlated with switching.</td><td>Supported</td></tr><tr><td>4a. Switching is negatively correlated with personalization.</td><td>Not supported</td></tr><tr><td>4b. Switching is positively correlated with ease of use.</td><td>Supported</td></tr><tr><td>4c. Switching is negatively correlated with quality.</td><td>Supported</td></tr><tr><td>4d. Switching is negatively correlated with breadth of offerings.</td><td>Supported</td></tr><tr><td>4e. Switching is not related to cost.</td><td>Supported</td></tr><tr><td>5a. Use of multiple brokers is negatively correlated with attrition.</td><td>Supported</td></tr><tr><td>5b. High volume of Web site usage is negatively correlated with attrition.</td><td>Supported</td></tr><tr><td>6a. Customer attrition is negatively correlated with personalization.</td><td>Not supported</td></tr><tr><td>6b. Customer attrition is negatively correlated with quality.</td><td>Not supported</td></tr><tr><td>6c. Customer attrition is negatively correlated with breadth of offerings.</td><td>Not supported</td></tr><tr><td>6d. Customer attrition is negatively correlated with ease of use.</td><td>Not supported</td></tr><tr><td>6e. Customer attrition is not related to cost.</td><td>Supported</td></tr><tr><td>6f. Customer attrition is negatively correlated with account minimums.</td><td>Supported</td></tr></table>

The results in Table 6 suggest that breadth of product offering on Web sites is universally beneficial (as long as the costs of breadth are reasonable). Others have tradeoffs—low minimum balances increase acquisition at the expense of attrition. Interestingly, our analysis does not show that potentially promising technology strategies have their desired effects: Ease of use appears either ineffective or negative, and investments in personalization (“relationship services”) appear to have no effect, at best. For ease of use, it may suggest that improvements in ease of use reduce functionality, or it could be possible that a complex interface design creates lock in because of the time (cost) of learning the interface. For Web site personalization, it may simply reflect that the personalization technology used by firms is still primitive or that firms do not invest enough in these services to be effective—a situation that may change as personalization technology diffuses and matures. Alternatively, it could be that customers have different preferences in the degree of personalization and these are already reflected in their initial choices, and as a result, personalization does not influence customers switching decisions. It could also be that firms’ investments in personalization technology do not address customers’ needs, that customers do not actually use it, or that the dimensions captured by Gomez Advisors may not capture all dimensions of personalization that consumers actually value. This suggests that future work should be undertaken to evaluate the impact of personalization to distinguish between measurement problems and a true absence of an effect.

It is also important to note that demographics typically are not good predictors of behavior except for a few isolated results on attrition. One notable result is that women are found to be more likely to become

Table 6 Summary of Factors that Affect Acquisition, Switching and Attrition (Model Includes Broker Characteristics, Customer Characteristics and Time Controls)

<table><tr><td></td><td>Acquisition</td><td>Switching</td><td>Attrition</td></tr><tr><td>Cost</td><td>NS</td><td>NS</td><td>NS</td></tr><tr><td>Ease of use</td><td>NS</td><td>-*</td><td>-***</td></tr><tr><td>Quality</td><td>NS</td><td>+*</td><td>NS</td></tr><tr><td>Resources</td><td>+***</td><td>+***</td><td>NS</td></tr><tr><td>Personalization</td><td>NS</td><td>NS</td><td>NS</td></tr><tr><td>Minimum deposit</td><td>-**</td><td>NS</td><td>+*</td></tr><tr><td>Web Site usage</td><td>varied</td><td>+***</td><td>+***</td></tr><tr><td>Change in usage</td><td>na</td><td>-***</td><td>n/a</td></tr><tr><td>Multiple brokers</td><td>varied</td><td>-***</td><td>+*</td></tr><tr><td>Demographics</td><td>varied</td><td>minimal</td><td>Age (+**)</td></tr><tr><td></td><td></td><td></td><td>Women (-**)</td></tr><tr><td></td><td></td><td></td><td>Education (+*)</td></tr><tr><td>Overall Fit</td><td> $\chi^2(186) = 1430$ </td><td> $\chi^2(29) = 278$ </td><td> $\chi^2(28) = 1031$ </td></tr><tr><td>Model</td><td>Conditional logit</td><td>Logistic</td><td>Logistic</td></tr></table>

Note. \*: p  0.05; \*\*: p  0.01; \*\*\*: p  0.001.  
We have altered the signs of the coefficients such that “” is good, and “-” is bad; a factor is coded “NS” if it is not statistically significant.  
Many factors in the acquisition model are insignificant due to the large number of demographic control variables interacted with firm dummy variables (this an inherent problem with using conditional logit analysis to investigate individual-level effects). When individual effects are not included, the remaining firm factors (cost, ease of use, quality, personalization) are al positive and significant, as would be expected.

inactive. This gender effect appears consistent with a recent study by Barber and Odeon (1999) which found that men trade online significantly more frequently than women, so it is not surprising that women are more likely to become inactive. Interestingly, our visit frequency data is fairly consistent with Barber and Odeon’s study: Our data shows that single men visit their brokers 58% more than single women do, while their corresponding number for trading volume is 67%. This suggests that our visit frequency information may not be a bad proxy for trading behavior, at least when making comparisons in aggregate. Moreover, the seasonal effect found in the attrition analysis that attrition rates rose dramatically in Q2 2000 appears to be consistent with that which has been reported in Business Week (Gogoi 2000): “Overall, online trading volume fell more than 20% in the second quarter . . .” (pp. 98–102). This seasonal effect is likely driven by market conditions since the Nasdaq and Internet stocks in particular experienced declines over this period.

Overall, we conclude that systems usage variables, Web site usage, and changes in usage patterns are good predictors of switching and attrition. Thus, for targeting consumers it is important to focus on systems usage variables (particularly volume of usage and changes in usage patterns) to identify good customers. Because the price of trading services substantially exceeds marginal cost and there is very little unpriced customer service activity, higher volume customers are typically more profitable.<sup>9</sup> Therefore, for example, it may be worthwhile to subsidize customers who show a high level of use at a competitor (since they face higher switching costs) rather than new adopters. Moreover, firms should pay extra attention to customers who show changes in usage patterns since it can predict a tendency to switch. Moreover, to the extent that systems usage encourages retention through system-specific learning, it would imply that firms could improve retention by encouraging consumers to frequently visit and use their sites. Our analysis also suggests that systems design characteristics such as personalization and ease of use should be reconsidered both in terms of their measurement and in further evaluation to determine whether they have the intended effects on long-term customer behavior.

Finally, the consistency of our results with theoretical relationships proposed in prior literature suggests that the archival measures of IS variables, customer characteristics, and switching costs may have validity. Our results in this vein are in accord with the findings of Palmer (2002), who validated his use of archival data (Bagozzi 1980, Campbell 1960, Boudreau et al. 2001).

## 6. Conclusion

Previous theoretical work has shown that the presence of switching costs, either generally or in specific firms, can have a substantial effect on profitability. However, the creation of switching costs requires substantial and deliberate investments by the firm in customer retention. In order to effectively manage customer retention, it is important to have methods of measuring switching costs and understand the factors that influence them. Only by understanding the magnitude of these switching costs could firms measure trade-offs between investments in loyalty and retention programs and other types of investments such as advertising (for building new customer acquisition rates), technologies, and service level improvements or price reductions, which raise both the acquisition and retention rates simultaneously. This paper offers such a model for measuring switching costs and identifying the drivers of customer retention (as determined by customer switching and attrition). The study of the drivers of customer retention is important for product and service design and technology adoption. The exploration of how systems design and systems usage variables affect retention gives us feedback on how to utilize these variables in shaping a firm’s strategy and how to adjust these investments in the future. Our results also complement and extend previous work on IT adoption that has considered similar constructs.

Applying our measurement model to the online brokerage industry, we found that implied switching costs vary substantially across brokers, and that systems usage variables, such as usage and change in usage, are useful in predicting customers’ switching behaviors. Our result also suggests that factors under the firm’s control may influence these switching costs. Our initial analysis using firm attributes identifies some of these factors, but there is still substantial heterogeneity, suggesting that firms have significant control over their switching costs through various kinds of retention strategies. Although we do not find that systems design variables like ease of use and personalization are associated with beneficial customer behavior in our data, this may simply reflect that these technologies have not yet matured, a question that can be explored in future research.

The method and approach used by this paper is applicable to the analysis of other Internet-enabled markets or industries. The method proposed here is especially suitable for the analysis of Internet businesses because we are able to observe all the products a customer considered and know, with certainty, which options were available at the time the customer made an adoption choice. Using these approaches, firms can measure their switching costs—the first step to effectively managing them. In addition, by linking the switching costs due to firm-specific retention strategies to the implementation costs, managers can better gauge the effectiveness of their retention investments.

## Acknowledgments

The authors thank Eric Bradlow, Eric Clemons, David Croson, Rachel Croson, Marshall Fisher, Paul Kleindorfer, Robert Josefek, Eli Snir, Detmar Straub, Arun Sundararajan, Hal Varian, Dennis Yao, and seminar participants at Carnegie Mellon University, Georgia Tech, MIT, New York University, the University of British Columbia, the University of California at Berkeley, the University of California at Irvine, the University of Maryland, the University of Rochester, the University of Texas at Austin, The Wharton School, the Workshop on Information Systems and Economics, the International Conference on Information Systems (ICIS), three anonymous reviewers from ICIS, and three anonymous reviewers from Information Systems Research for comments on earlier drafts of this paper. The authors also thank Media Metrix and Gomez Advisors for providing essential data. This research was funded by the Wharton eBusiness Initiative (WeBI).

## Appendix. Definitions of Gomez Indices (Quote from Gomez Advisors Web Site)

1. Ease of Use. The Web site of a top firm in this category boasts a consistent and intuitive layout with tightly integrated content and functionality, useful demos, and extensive online help. Roughly 30 to 50 criteria points are assessed, including:

• Demonstrations of functionality.

• Simplicity of account opening and transaction process.

• Consistency of design and navigation.

• Adherence to proper user interaction principles.

• Integration of data providing efficient access to information commonly accessed by consumers.

2. Customer Confidence. The leaders in this category operate highly reliable Web sites, maintain knowledgeable and accessible customer service organizations, and provide quality and security guarantees. Roughly 30 to 50 criteria points are assessed, including:

• Availability, depth, and breadth of customer service options, including phone, e-mail, and branch locations.

• Ability to accurately and readily resolve a battery of telephone calls and e-mails sent to customer service, covering simple technical and industry-specific questions.

• Privacy policies, service guarantees, fees, and explanations of fees.

• Each ranked Web site is monitored every five minutes, seven days a week, 24 hours a day for speed and reliability of both public and secure (if available) areas.

• Financial strength, technological capabilities and independence, years in business, years online, and membership organizations.

3. On-Site Resources. The top firms in this category not only bring a wide range of products, services and information onto the Web, but also provide depth to these products and services through a full range of electronic account forms, transactions, tools and information look up. Roughly 30 to 50 criteria points are assessed, including:

• Availability of specific products.

• Ability to transact in each product online.

• Ability to seek service requests online.

4. Relationship Services. Firms build electronic relationships through personalization, by enabling customers to make service requests and inquiries online and through programs and perks that build customer loyalty and a sense of community. Roughly 30 to 50 criteria points are assessed, including:

• Online help, tutorials, glossary and FAQs.

• Advice.

• Personalization of data.

• Ability to customize a site.

• Reuse of customer data to facilitate future transactions.

• Support of business and personal needs such as tax reporting or repeated buying.

• Frequent buyer incentives.

5. Overall Cost. Go´mez looks at the total cost of ownership for a typical basket of services customized for each customer profile. Costs include:

1. A basket of typical services and purchases.

2. Added fees due to shipping and handling

3. Minimum balances.

4. Interest rates.

## References

Alpar, Paul, Marcus Porembski, Sebastian Pickerodt. 2001. Measuring the efficiency of Web site traffic generation. Internat. J. Electronic Commerce 6(1) 53–73.

Bagozzi, R. P., 1980. Causal Methods in Marketing. John Wiley and Sons, New York, NY.

Bakos, Y. 2001. The emerging landscape for retail e-commerce. J. Econom. Perspectives 15(1) 69–80.

——, H. C. Lucas, Jr., W. Oh, G. Simon, S. Viswanathan, B. Weber. 2000. The impact of electronic commerce on the retail brokerage industry. Working paper, Stern School of Business, New York University.

Barber, B., T. Odean. 1999. Boys will be boys: Gender, overconfidence, and common stock investment. Working paper, University of California-Davis, Davis, CA.

Beggs, A., P. Klemperer. 1992. Multi-period competition with switching costs. Econometrica 60(3) 651–666.

Boudreau, Marie, David Gefen, Detmar Straub. 2001. Validation in IS research: A state-of-the-art assessment. MIS Quart. 25(1) 1– 24.

Boulding, W., A. Kalra, R. Staelin, V. A. Zeithaml. 1993. A dynamic

process model of service quality: From expectations to behavioral intentions. J. Marketing Res. 30 7–27.

Bresnahan, T. 2001. The economics of the Microsoft case. Presented at the MIT Industrial Organization Workshop. -www .stanford.edu/tbres/.

Brynjolfsson, E., L. M. Hitt. 1995. Computers as a factor of production: The role of differences among firms. Econom. Innovation New Tech. 3 183–199.

——, M. Smith. 2000. The great equalizer? Consumer choice behavior at internet shopbots. Working paper, Sloan School of Management, MIT.

Campbell, Donald T. 1960. Recommendations for APA test standards regarding construct, trait, discriminant validity. Amer. Psychologist 15 (August) 546–553.

Chen, P-Y., L. M. Hitt. 2000. Switching cost and brand loyalty in electronic markets: Evidence from online retail brokers. S. Ang, H. Kremar, W. Orlikowski, P. Weill, and J. I. DeGross, eds. Proc. 21st Internat. Conf. Inform. Systems.

Cingil, I., A. Dogac, A. Azgin. 2000. A broader approach to personalization. Comm. ACM 43(8) 136–141.

Crosby, L. A., N. Stephens. 1987. Effects of relationship marketing on satisfaction, retention, and prices in the life insurance industry. J. Marketing Res. 24 404–411.

Delone, William H., Ephraim R. McLean. 1992. Information systems success: The quest for the dependent variable. Inform. Systems Res. 3(1) 60–95

Elzinga, K. G., D. E. Mills. 1998. Switching costs in the wholesale distribution of cigarettes. Southern Econom. J. 65(2) 282–293.

Farrell, J., C. Shapiro. 1988. Dynamic competition with switching costs. Rand J. Econom. 19(1) 123–137.

Friedman, T. L. 1999. Amazon.you. New York Times, February 26, A21.

Gans, N., Y. Zhou. 2000. Customer loyalty and supplier strategies for quality competition: I and II. Working paper, The Wharton School, University of Pennsylvania, Philadelphia, PA.

Gogoi, Pallavi. 2000. Rage against online brokers. Bus. Week, November 20, 98–102.

Guadagni, P. M., J. Little. 1983. A logit model of brand choice calibrated on scanner data. Marketing Sci. 2 203–238.

Jacoby, J., R. W. Chestnut. 1978. Brand Loyalty Measurement and Management. John Wiley and Sons, New York.

Johnson, E. J., Wendy Moe, Peter S. Fader, Steven Bellman, Jerry Lohse. 2000. On the depth and dynamics of online search behavior. Working paper, The Wharton School, University of Pennsylvania, Philadelphia, PA.

Katz, M. L., C. Shapiro. 1985. Network externalities, competition, and compatibility. Amer. Econom. Rev. 75(3) 424–440.

Kim, M., D. Kliger, B. Vale. 2001. Estimating switching costs and oligopolistic behavior. Working paper, The University of Haifa and The Wharton School, University of Pennsylvania, Philadelphia, PA, -http://hevra.haifa.ac.il/econ/workingpaper/ doc\_02/2.pdf.

Klemperer, P. 1987. Markets with consumer switching costs. Quart. J. Econom. 102(2) 375–394.

——. 1995. Competition when consumers have switching costs: An overview with applications to industrial organization, macroeconomics, and international trade. Rev. Econom. Stud. 62 515– 539.

Kuhfeld, W. F. 1996. Multinomial logit, discrete choice modeling. Technical report, SAS Institute Inc.

McFadden, D. 1974. Conditional logit analysis of qualitative choice behavior. P. Zarembka, ed. Frontiers in Econometrics. Academic Press, New York.

——. 1974b. The measurement of urban travel demand. J. Public Econom. 3 303–328.

McVey, Henry. 2000. Online Financial Services. Presentation by Morgan Stanley/Dean Witter. Available at: -www.msdw.com/.

Mobasher, B., R. Cooley, J. Srivastava. 2000. Automatic personalization based on Web usage mining. Comm. ACM 43(8) 142–151.

Moe, W., P. S. Fader. 2000. Capturing evolving visit behavior in clickstream data. Working paper, The Wharton School, University of Pennsylvania, Philadelphia, PA, -www.marketing.wharton .upenn.edu/ideas/pdf/00-003.pdf

Morgan Stanley/Dean Witter. 1999. The Internet and Financial Service Report.

Novak, T. P, D. L. Hoffman, Y-F. Yung. 2000. Measuring the customer experience in online environments: A structural modeling approach. Marketing Sci. 19(1) 22–44.

Palmer, Jonathan. 2002. Web site usability, design and performance metrics. Inform. Systems Res. 13(2).

Pearson, M. 1998. Attractors: Building mountains in the flat landscape of the World Wide Web. Director 51(12) 81.

Reichheld, F. F., P. Schefter. 2000. E-loyalty: Your secret weapon on the Web. Harvard Bus. Rev. 78(4) 105–113.

Roy, A. 1994. Correlates of mall visit frequency. J. Retailing 70(2) 139– 161.

Saloman Smith Barney. 2000. Research reports on online brokers.

Shankar, V., A. K. Smith, A. Rangaswamy. 2000. Customer satisfaction and loyalty in online and offline environments. Working paper, Penn State University, -www.ebrc.psu.edu/publications/ papers/pdf/2000\_02/pdf.

Shapiro, C., H. R. Varian. 1998. Information Rules. Harvard Business School Press, Boston, MA.

Smith, M. D., J. Bailey, E. Brynjolfsson. 1999. Understanding digital markets: Review and assessment. E. Brynjolfsson and B. Kahin, eds. Understanding the Digital Economy, MIT Press, Cambridge, MA.

Straub, D. W., R. T. Watson. 2001. Transformational issues in researching IS and Net-enabled organizations. Inform. Systems Res. 12(4) 337–345.

Varian, H. 1998. Effect of the internet on financial markets. Working paper, University of California-Berkeley, Berkeley, CA.

——. 1999. Market structure in the network age. Working paper, University of California, Berkeley, Berkeley, CA.

Detmar W. Straub, Senior Editor. This paper was received on January 16, 2001, and was with the authors 3 months for 2 revisions
