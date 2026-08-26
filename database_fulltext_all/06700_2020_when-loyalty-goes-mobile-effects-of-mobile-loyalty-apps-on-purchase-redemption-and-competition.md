---
otero_id: 6700
otero_key: "7UQ23PV2"
title: "When Loyalty Goes Mobile: Effects of Mobile Loyalty Apps on Purchase, Redemption, and Competition"
authors: "Yoonseock Son; Wonseok Oh; Sang Pil Han; Sungho Park"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0918"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [132.174.252.179] On: 26 August 2020, At: 17:23 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## Information Systems Research

![](/api/attachments/7UQ23PV2/fulltext/images/7e2f272737627247cf57a262c5879a8a914fa54ef2587541cfccc43a556fdcad.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## When Loyalty Goes Mobile: Effects of Mobile Loyalty Apps on Purchase, Redemption, and Competition

Yoonseock Son, Wonseok Oh, Sang Pil Han, Sungho Park

To cite this article:

Yoonseock Son, Wonseok Oh, Sang Pil Han, Sungho Park (2020) When Loyalty Goes Mobile: Effects of Mobile Loyalty Apps on Purchase, Redemption, and Competition. Information Systems Research

Published online in Articles in Advance 26 Aug 2020

https://doi.org/10.1287/isre.2019.0918

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individua professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# When Loyalty Goes Mobile: Effects of Mobile Loyalty Apps on Purchase, Redemption, and Competition

Yoonseock Son,<sup>a</sup> Wonseok Oh,<sup>b,</sup>\* Sang Pil Han,<sup>c</sup> Sungho Park<sup>d</sup>

<sup>a</sup> Mendoza College of Business, University of Notre Dame, Indiana 46556; <sup>b</sup> College of Business, Korea Advanced Institute of Science and Technology, Seoul 02455, South Korea; <sup>c</sup> W.P. Carey School of Business, Arizona State University, Tempe, Arizona 85281; <sup>d</sup> SNU Business School, Seoul National University, Seoul 08825, South Korea

\*Corresponding author

Contact: yson@nd.edu, https://orcid.org/0000-0002-4758-5611 (YS); wonseok.oh@kaist.ac.kr,

https://orcid.org/0000-0002-8123-1382 (WO); shan73@asu.edu, https://orcid.org/0000-0001-5125-9846 (SPH); spark104@snu.ac.kr (SP)

Received: Revised: July 27, 2018; April 2, 2019; August 5 July 27, 2018; Accepted: Published Online in Articles in Advance: August 26, 2020

https://doi.org/10.1287/isre.2019.0918

Copyright:

Abstract. Avenues for the delivery of loyalty programs have rapidly shifted from plastic card schemes to mobile app–based initiatives, yet our understanding of the economic value presented by the latter (i.e., loyalty apps) has not kept pace with this development. We examine the effects of loyalty app adoption on customers’ offline purchase patterns, reward redemption, and deal-prone behaviors as well as store-level competition in a multivendor loyalty program (MVLP) context, where multiple offline brands collaborate in the operation of point-sharing initiatives. Mobile-driven loyalty apps substantially lower consumer search costs, thereby enhancing on-demand information accessibility and facilitating the monitoring of reward points. Based on a unique data set that comprises information on customers’ loyalty app adoption status, loyalty point redemption patterns, and purchase behaviors in MVLP environments, we investigate how the transition from plastic-based programs to loyalty apps influences the out-of-pocket spending and point redemption patterns of consumers. Our findings reveal that the adoption of loyalty apps is associated with an increase in purchases and the predilection for point redemption. Despite these positive outcomes, however, potential adverse consequences may arise in the form of deal-susceptible behaviors and reduced store-specific loyalty. Loyalty app adopters tend to be more vulnerable to deals, with these customers selectively buying highly discounted products of low margin. Additionally, loyalty app consumers visit more stores but spend less in a focal store, thereby diminishing loyalty to this specific store. These results have managerial implications on optimal mobile-based loyalty program designs and implementation, reward-driven platform strategies, and risk management initiatives in an MVLP setting.

History: Saby Mitra, Senior Editor; Sam Ransbotham, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0918.

Keywords: mobile apps • mobile customer relationship management (mCRM) • loyalty programs • mobile channel • deal-susceptible behaviors difference-in-differences • econometrics • spillover effects • propensity score matching • mere exposure • technology adoption

## 1. Introduction

Customer loyalty programs (LPs)—marketing schemes that enable repeat consumers to earn reward points for use in future purchases and service upgrades—have facilitated customer relationship management (CRM) across a wide range of retail sectors from airlines and supermarkets to coffee shops. These “purchase-andreward” programs are intended to foster increased trust from patrons, create switching barriers, and immerse consumers in brand experience, all of which translate into increased revenue in the short or long term (Dorotic et al. 2012).

Plastic cards have long been the medium through which loyalty is cultivated. Many vendors continue to rely on these marketing avenues because card-based

LPs are easier to implement and require fewer economic resources to operate compared with their digital counterparts.<sup>1</sup> However, because these physical schemes place greater weight on transactions than information accessibility, they are limited in terms of promoting and preserving consumer engagement (Viswanathan et al. 2017). Moreover, carrying a collection of plastic cards in overflowing wallets is regarded by consumers as in convenient and makes them feel forced to remember redeeming their rewards. This deficiency in consumer experience may explain why LPs accessed through plastic card membership cannot completely capture customer loyalty (Shugan 2005).

As such, businesses are rapidly replacing plastic cards with mobile-based loyalty apps, hoping that digitalizing “fidelity” can reduce consumer friction. Mobile devices as channels for program delivery and in-app functions that are available through loyalty apps enhance the portability, interactivity, and accessibility of loyalty points. Furthermore, digitalized LPs offer consumers personalized promotions and instant access to their accounts for an improved service experience (Ransbotham 2015).

However, in spite of these merits, whether converting loyalty measures into mobile-oriented endeavors can live up to firms’ expectations, boost sales, and expand customer engagement remain unproven. Moreover, the low search costs associated with mobiledriven LPs can motivate consumers to exhibit deal-prone behaviors, thereby creating an environment that encourages membership from customers who are unprofitable for the respective firms.

Another important transformation witnessed in the race to secure loyalty is the emergence of partnerships and platform developments by way of reward schemes (Breugelmans et al. 2015). The rapid evolution of the loyalty landscape has recently encouraged retailers to join multivendor loyalty programs (MVLPs) through which customers can earn reward points from an affiliated retailer that they can use as cash at another vendor participating in the point-sharing venture (Berman 2006). However, notwithstanding the synergistic benefits accrued from collaboration, this shift may also reshape the competitive dynamics among participating retailers, with the phenomenon exerting spillover effects across brands and stores that compete for devoted customers.

Despite the rapid penetration of mobile-based LPs and the shared loyalty initiatives (i.e., MVLP), a significant gap remains in our understanding of how digitalized and coalition-oriented loyalty alters the purchase behaviors of customers, their relationship and engagement with a firm, and the competition across participating stores. Numerous scholarly works focus on traditional CRM (Reinartz and Kumar 2003, Rust and Huang 2014) while largely neglecting mobile CRM (mCRM) and the associated app-based LPs in the MVLP environment. This lack of attention stems mostly from the novelty of and minimal participation to date in mobile and shared LPs.

To fill this gap, we first explain how turning loyalty schemes into mobile measures reduces consumer search costs and increases the accessibility of rewardrelated information. We then develop relevant hypotheses regarding how the transition from card-based loyalty initiatives to mobile-driven LPs affects customer behaviors when multiple brands form a cross-brand LP. To empirically disentangle these issues, we analyze a large-scale individual-level panel data set containing information on 7,712 randomly selected customers and their loyalty app adoption, transactions, and reward point redemption behaviors. This unique data set comes from a large multinational retailer that offers an MVLP.

For econometric validation, we carry out propensity score matching (PSM) with difference-in-differences (DID) analysis to compare the changes in purchase and reward redemption among loyalty app adopters and nonadopters before and after the use of mobiledriven LPs. Consumers’ purchase frequencies and spending levels often serve as key measures for estimating customer value, and reward redemption is regarded as a critical aspect of a loyalty reward program (Dorotic et al. 2012). Correspondingly, we examine how the transition from card-based scheme to mobile LPs affects four dimensions of consumer behaviors, namely (1) out-of-pocket (i.e., cash and credit card) expenditure, (2) frequency of out-ofpocket purchase, (3) amount of points redeemed, and (4) frequency of point redemption.

Our results indicate that the adoption of mobile loyalty apps positively influences purchase and point redemption. Loyalty app adoption also encourages consumers to visit stores that they would otherwise ignore but spend less in focal stores where they expend the most resources. This finding suggests that competition among retailers can further intensify in a mobile-based MVLP environment and that storespecific loyalty can diminish when MVLP initiatives are in place. Furthermore, loyalty app adoption is also associated with deal susceptibility among consumers. These empirical patterns highlight the potential risk presented by loyalty apps, accentuating the vulnerability of customers to deals with which they are encouraged to selectively purchase highly discounted products of low margins. Finally, the effects of both mobile channels and in-app functions are related to spending behaviors, but in-app features are associated with the spillover effect of stores visited under an MVLP scheme.

This study offers several important contributions to the growing body of literature that revolves around the effects of LP digitalization on the dynamics of customer behaviors and the performance of businesses as follows. First, we scrutinize how the adoption of mobile-driven loyalty initiatives affects a customer’s interaction with brands and consequently leads to purchase. Although studies on mobile targeting (Andrews et al. 2016) have adequately demonstrated the advantages of mobile platforms, they focus exclusively on particular spontaneous purchase events (e.g., coupon redemption) rather than on sustained efforts to foster customer–firm relationships. Second, our research broadens the current understanding of loyalty points through the integrated lens of search costs and mere exposure effects (Zajonc 1968, Rishika et al. 2013) with an explanation of consumers’ point spending and management behaviors after loyalty app adoption. This study articulates how the reduced search costs and enhanced accessibility driven by mobile channel and in-app function effects influence consumers’ spending behaviors and point redemption patterns. Third, this study delves into the MVLP environment, wherein multiple brands collaborate in point-sharing programs. This orientation broadens extant literature because it introduces the dynamics unique to the MVLP setting and uncovers how the transferability of reward points causes potential spillover effects and influences competition among brands and stores. Fourth, although the benefits of mobile technologies are well established in the literature (Fong et al. 2015), the knowledge concerning potential business-related hazards posed by such innovations is scarce. Our study demonstrates that although the digitalization of loyalty may yield many tangible benefits, retailers should nevertheless be alerted to potential threats that can adversely affect their performance.

## 2. Related Literature

The first stream of literature relevant to our study concerns LPs. This stream of literature investigates the relationship between reward point redemption and cash expenditure behaviors (Kivetz et al. 2006, Dorotic et al. 2014). These authors show that customers exhibit a forward-looking behavior and hasten their purchase as they become closer to redeeming a reward (Kivetz et al. 2006) and that redemption itself can be a by-product of positive learning (Taylor and Neslin 2005). Furthermore, such effects are maintained regardless of the amount and timing of redemption (Dorotic et al. 2014). Previous studies draw on the mental accounting framework (Thaler 1985) to highlight how customers perceive cash and reward points differently when they purchase products from the store where they earned points (Dreze and Nunes\` 2004, Stourm et al. 2015), despite their equal economic value.

A recent stream of the literature focuses on MVLPs because they have become increasingly prominent (Breugelmans et al. 2015). To date, studies have presented mixed evidence of the effects of MVLPs using only limited data (Lemon and Wangenheim 2009, Dorotic et al. 2012, Schumann et al. 2014). On the one hand, MVLPs can create positive synergy among participating partners as a result of consumers’ crossbuying behaviors (Lemon and Wangenheim 2009). On the other hand, they can also generate negative spillover effects when service failure by one partner within the MVLP negatively affects not only company loyalty but also program loyalty (Schumann et al. 2014).

Our research also draws on the growing literature related to the effect of commercial apps. The advancement of information technology (IT) innovations (i.e., mobile technologies) has led the customer–firm relationship to become one in which consumers take charge of business dealings. Among the analytical efforts concerned with commercial app adoption and customer behaviors, Bellman et al. (2011) use a laboratory experiment designed to examine the effects of a branded mobile app on customers’ brand attitude and purchase intention. The results indicate that app usage increases customers’ interest in a brand and its product category while also promoting their purchase intention. Similarly, Kim et al. (2015) show that app adoption and the continued use of a branded app raise adopters’ spending levels, whereas the abandonment of the apps decreases their spending levels. The authors also inquire into the manner by which information lookups and check-ins influence adopters’ spending. Lastly, Viswanathan et al. (2017) use data from an LP and examine how customer engagement and purchase behaviors influence each other over time. They find that customers’ disengagement with mobile apps can negatively affect the long-term success of vendors. To the best of our knowledge, little research has been devoted to mobile innovations for LPs, and only limited studies have analyzed the competitive nature of brands and stores (Fong et al. 2015) as well as the role of IT within an MVLP setting. In contrast to previous research, we further examine the spillover effects associated with loyalty app adoption from the viewpoints of firms. We also provide an understanding of the underlying mechanism that may have driven the results in the empirical analyses by disentangling the estimated business impact (i.e., mobile channel and in-app function effects) engendered by the loyalty app adoption.

## 3. Theoretical Background and Hypothesis Development

## 3.1. Effects of Loyalty App Adoption on Point Redemption and Out-of-Pocket Spending

Information search (one of the key tasks in consumers purchase decision processes) profoundly affects customer behavior and preferences (Punj and Staelin 1983). However, the search for and gathering of information involve both tangible and intangible monetary costs (i.e., time and effort) that often exceed expected benefits. High search costs can prevent consumers from actively engaging in information search, affecting their inclination to purchase products (Bakos 1997, Huang et al. 2009). However, such an impediment may be less problematic with the advent of mobile technologies that allow customers ubiquitous access to desired information and, accordingly, reduce the costs incurred from searching for products and services (Ghose et al. 2013).

In this light, two major features of interest arise. First, the high intrinsic portability and communicative utility of mobile channels offer the advantage of convenience, that is, the value of achieving a task effectively. Loyalty app users spend less time and effort viewing and managing current loyalty points because this information is instantly accessible through a single touch on a loyalty app. Hence, loyalty apps repeatedly expose users to loyalty points via the familiarity that develops through mere exposure (Sun et al. 2017). The low search costs incurred over mobile apps can encourage consumers to repeatedly monitor their resources (i.e., reward points) through their devices—a behavior that produces and reinforces the positive effects of loyalty apps. Moreover, mobile-based reminders, which can further strengthen the need for point maintenance, exert an immediate effect on how an individual conducts himself or herself (Calzolari and Nardotto 2016). The same positive influence of exposure on the behaviors of loyalty app users can thus originate from a prompt regarding loyalty points.

These convenient features strikingly contrast with the extra effort required to view and manage loyalty point balances in plastic card–based LPs—an inconvenience that drives consumers to perceive loyalty points as a secondary source of funds (Dreze and\` Nunes 2004). Plastic card users are therefore relatively less likely to be exposed to loyalty points than are loyalty app users. This lack of mere exposure effects (Zajonc 1968) translates to a mutually reinforcing cycle of unfavorable outcomes, where the increased time and procedure required to access information reduce convenience and accessibility, which, in turn, discourage endeavors to keep track of loyalty points.

The effects of adopting a loyalty app do not result solely from the intrinsic advantages of mobile channels (e.g., portability, accessibility, and convenience) but also result from additional features embedded in loyalty apps (e.g., in-app functions). With in-app functions, concern revolves around the supplementary functions that are offered exclusively by loyalty apps and mostly unavailable on web browsers. Hence, unlike the plastic card users who can access only core information and functions (i.e., checking loyalty points), loyalty app consumers can activate auxiliary in-app functions that are unique to mobile innovations. Such empowerment is also engendered through mobiledriven functions, such as the increasingly personalized communication enabled by location flexibility and high accessibility (Ghose et al. 2013, Ransbotham et al. 2019).

Because mobile-based artifacts (e.g., loyalty apps) augment convenience and accessibility as well as reduce search costs associated with shopping and managing the time and effort devoted to resources, customers who transact through such technologies are likely to actively purchase products and services (Gupta and Kim 2010). Thus the intrinsic features of mobile channels and the supplementary functional elements provided by loyalty apps may favorably affect behaviors, such as point redemption and outof-pocket spending. In this respect, we hypothesize the following.

Hypothesis 1. Loyalty app adoption is positively associated with point redemption and out-of-pocket purchase behaviors.

## 3.2. Effects of Loyalty App Adoption on Cross-Store Sales

In contrast to a single-vendor LP, an MVLP allows customers to purchase products as well as accumulate and redeem loyalty points from multiple stores that are affiliated with the LP. This single membership but multioption character of MVLPs affords customers increased convenience and redemption options (Bijmolt and Verhoef 2017) and generates a network effect.

We posit that before loyalty app adoption, customers’ consideration of a set of stores is restricted and static because of limited touchpoints between vendors and consumers under a plastic card–based scheme. Specifically, the time and effort expended in searching for information on multiple stores that are banded together through MVLP arrangements would be high for plastic card users relative to those required from loyalty app users. However, after loyalty app adoption, customers freely access information on different stores that participate in the respective MVLP without temporal and geographic restrictions because loyalty app usage reduces search costs while enhancing information accessibility. Customers can also take advantage of in-app functions such as locationbased technology (i.e., Global Positioning System) to search for nearby stores. Consequently, they become aware of stores they have previously overlooked.

Additionally, customers more actively establish meaningful contact over loyalty apps than over plastic card–based initiatives given that the interactivity, engagement, and control advanced by mobile technology bring forth a positive persuasive effect, correspondingly increasing interest in not only a store but also its product categories (Bellman et al. 2011). Before loyalty app adoption, the search for suitable alternatives (i.e., other stores offering similar product categories) may be relatively complicated given the dispersion of limited information and the high costs associated with searches and evaluations (Ray et al. 2012). However, the increased information availability allowed by loyalty apps enhances consumers’ awareness of alternative stores. When an alternative is viewed as complementary to an existing option, customers may easily track expenses for related selections within the same category and easily transfer allocated budgets from existing to alternative choices (Netemeyer et al. 2012).

These effects, in turn, facilitate purchases from a nonfocal store (James 2005) and decrease store-specific loyalty. Correspondingly, we put forward the following hypothesis.

Hypothesis 2. In MVLP environments, loyalty app adoption is positively related to the number of stores from which customers purchase but negatively associated with storespecific loyalty.

## 3.3. Effects of Loyalty App Adoption on Customers Susceptibility to Deals

The innate characteristics of mobile channels broaden LP engagement from a transaction-based occupation to an engagement-based activity. Consumers can proactively acquire information on promotions and redeemable points via loyalty apps with increased accessibility—a convenience that facilitates enriched interactions between customers and firms. We believe that the convenience and information accessibility made possible by loyalty apps promote customers efficient spending behaviors and preference for deals. Loyalty apps may motivate consumers to become increasingly price conscious and responsive to promotional deals and campaigns because of the ease and enhanced in-app functions offered by these programs. The control placed in the hands of consumers may alter how they search for products and make purchase decisions (Rishika et al. 2013). For instance, low search cost can facilitate the active use of loyalty apps instead of passive involvement in promotions (Hui et al. 2013). It also increases price sensitivity and changes consumer’s willingness to pay (Clemons 2008) and the price elasticity of demand (Granados et al. 2012).

This loyalty app–enabled opportunity for vigorous participation translates into an effortless search for price promotions, which prompts customers to satisfy their desire to increase the transaction utility of each purchase. However, this situation does not necessarily imply that a customer reduces the expenditure allocated to a firm following loyalty app adoption because not all products are offered under a promotion. Rather, customers exhibit efficient purchase behaviors when alternative price options exist and technological intervention expedites search and purchase processes. Following this line of reasoning, we formulate the next hypothesis.

Hypothesis 3. Loyalty app adoption is positively associated with susceptibility to promoted deals.

## 4. Empirical Setting

The data set for this study comes from a large multinational offline firm that provides an extensive MVLP, encompassing 15 brands (i.e., Baskin Robbins, Jamba Juice, and others) of baked goods and other food categories. We focus on the brands and stores that the retailer operates in Korea. The firm has more than 18,000 offline stores nationwide, serves millions of customers, and offers one of the most widely known customer loyalty reward programs in the country. Enrolled customers can earn 5% of their expenditure as reward points, which are redeemable as cash.<sup>2</sup> A noteworthy attribute is that the MVLP permits customers to earn points at a store of an affiliated brand and use them as cash at another store, even for a different brand within the same MVLP This transferability engenders potential spillover effects among brands and stores.

In addition to the plastic cards through which customers can accumulate points, a loyalty app was launched to enhance customer engagement with the brands. When customers first enroll, they can either receive a plastic card or directly register on the firm’s loyalty app after download. A customer who initially opted for the plastic card can still register on the loyalty app. A notable feature of the loyalty app is that its users can instantly check their point status and ongoing promotions in real time (e.g., accumulated loyalty points and redeemable coupons), whereas the plastic card users have to search the web or log in to the firm’s website to access the same functions. We define loyalty app adopters as those who first registered for the plastic card LP, later enrolled in the loyalty app scheme, and accumulated records of loyalty app usage to earn and redeem loyalty points. Our empirical data set contains individual consumer-level panel data (7,712 consumers) on cash (“out-of-pocket”)<sup>3</sup> and point transactions as well as demographic profiles from January 2015 to July 2015 (seven months) on a monthly basis. Table 1 lists the variable definitions and summary statistics for our data set.

## 5. Methodology and Main Results 5.1. Identi<sup>fi</sup>cation Strategies

Given that our data are not obtained from a controlled field experiment, the estimate of loyalty app adoption can be biased because of potential self-selection. We address this problem by using a PSM method in constructing a matched control group for each customer in the treatment group. After constructing a matched customer data set, we carried out DID estimations to probe into the effects of loyalty app adoption on purchase and point redemption behaviors. We also perform store-level analysis and explain the mechanism under which loyalty app adoption may pose risks to certain stores.

## 5.2. Propensity Score Matching

PSM is used to find a matched pair of control and treatment groups in accordance with the proximity of their propensity scores (Rosenbaum and Rubin 1983). In this study, the major difference between the two groups is that although they both initially enrolled in the company’s plastic card scheme, the customers constituting the treatment group subsequently adopted the loyalty app. Moreover, we focus on the sample of customers who registered in the LP before the initiation of our data-collection period and made at least three purchases during the preadoption period of our analysis. Through PSM, we use three months of data before adoption to identify a control group that is similar to the treatment group in the preadoption period to mirror a randomized experimental setup (Rubin 2006). Because of this, loyalty app adoptions occur in month 4 of our data or after. This procedure leaves us with 3,856 pairs of customers. The validation results of the PSM procedure are presented in Online Appendix A.

Table 1. Variable Definition and Summary Statistics (Monthly Average)

<table><tr><td>Category and variable</td><td>Definition</td><td>Mean</td><td>Standard deviation</td><td>Minimum</td><td>Maximum</td><td>Median</td></tr><tr><td colspan="7">Time variant(53,984 observations)</td></tr><tr><td>Monetary value</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $Spending\_level_{it}$ </td><td>Amount transacted by the customer (in U.S. dollars)</td><td>24.65</td><td>22.31</td><td>0.00</td><td>418.50</td><td>19.54</td></tr><tr><td>Frequency</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $Purchase\_freq_{it}$ </td><td>Number of transactions made</td><td>2.74</td><td>2.69</td><td>0.00</td><td>45</td><td>2.00</td></tr><tr><td> $Mean\_IPT_{it}$ </td><td>Average interpurchase time (IPT; in days)</td><td>11.90</td><td>6.48</td><td>0.00</td><td>185.00</td><td>9.75</td></tr><tr><td>Recency</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $SD\_Day_{it}$ </td><td>Standard deviation of purchase time (in days)</td><td>12.35</td><td>7.85</td><td>0.00</td><td>129.40</td><td>8.71</td></tr><tr><td> $SD\_Hour_{it}$ </td><td>Standard deviation of purchase time (in hours)</td><td>3.65</td><td>1.00</td><td>0.00</td><td>16.26</td><td>3.05</td></tr><tr><td>Reward points</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $Usage\_level_{it}$ </td><td>Average reward point redemption amount</td><td>1.20</td><td>4.10</td><td>0.00</td><td>40.45</td><td>1.24</td></tr><tr><td> $Usage\_freq_{it}$ </td><td>Number of point redemptions</td><td>0.20</td><td>0.52</td><td>0.00</td><td>11.00</td><td>0.00</td></tr><tr><td>Promotion</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $Prom\_spending_{it}$ </td><td>Amount transacted by the customer on promoted products (in U.S. dollars)</td><td>0.33</td><td>2.95</td><td>0.00</td><td>42.27</td><td>0.45</td></tr><tr><td> $Prom\_freq_{it}$ </td><td>Number of transactions made on promoted products</td><td>1.07</td><td>0.36</td><td>0.00</td><td>7.00</td><td>0.00</td></tr><tr><td>Multivendor</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $Brand_{it}$ </td><td>Number of brands visited</td><td>1.50</td><td>0.40</td><td>0.00</td><td>6.00</td><td>1.00</td></tr><tr><td> $Store_{it}$ </td><td>Number of stores visited</td><td>2.03</td><td>0.76</td><td>0.00</td><td>13.00</td><td>2.00</td></tr><tr><td colspan="7">Time invariant(7,712 observations)</td></tr><tr><td>Direct marketing</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $SMS_{i}$ </td><td>1 if customer opted for SMS marketing, 0 otherwise</td><td>0.83</td><td>0.38</td><td>0.00</td><td>1.00</td><td>1.00</td></tr><tr><td> $Email_{i}$ </td><td>1 if customer opted for email marketing, 0 otherwise</td><td>0.64</td><td>0.48</td><td>0.00</td><td>1.00</td><td>1.00</td></tr><tr><td>Demographics</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $Age_{i}$ </td><td>Age of customer</td><td>37.06</td><td>10.19</td><td>10.00</td><td>67.00</td><td>38.00</td></tr><tr><td> $Gender_{i}$ </td><td>1 if customer is male, 0 otherwise</td><td>0.17</td><td>0.37</td><td>0.00</td><td>1.00</td><td>0.00</td></tr><tr><td> $City_{i}$ </td><td>1 if customer resides in the urban areas, 0 otherwise</td><td>0.56</td><td>0.50</td><td>0.00</td><td>1.00</td><td>1.00</td></tr></table>

Notes. The units of time-variant variables are individual (i) and month (t). The units of time-invariant variables are individual (i). The time-variant variables are measured by calculating the monthly average of each customer, and observations of time-variant variables totaling 53,984 are obtained by multiplying the number of consumers by the number of months $( 7 , 7 1 2 \times 7 )$ . Months with no purchase records are excluded for the recency variables. SMS, short message service.

## 5.3. Effects of Loyalty App Adoption on Point Redemption and Purchase Behaviors

In our DID estimation, we compare the relative change in the purchase and reward redemption behaviors of adopters and nonadopters before and after loyalty app adoption using the following model:

$$
\begin{array}{r l} \ln (O _ {i j t}) = & \beta_ {1} A d o p t i o n _ {i j t} + \beta_ {2} A d o p t i o n _ {i j t} \times T r e a t m e n t _ {i} \\ & + \alpha_ {t} + \tau_ {i} + \varepsilon_ {i t}, \end{array}\tag{1}
$$

where i denotes customer $i , j$ denotes a matched pair of customers, and t represents month t. $O _ { i j t }$ is the dependent variable (i.e., expenditure and purchase frequency of cash and point redemption transactions), and Treatment is a treatment dummy variable that equals one if the customer belongs to the treatment group and zero otherwise. Adoption denotes an adoption dummy variable that equals one in periods on and after the month of loyalty app adoption and zero prior to the adoption month for each treated user and the matched untreated user. Hence, if a treated user in a pair adopts a loyalty app in the first month of our adoption period, the pair’s indicator of the adoption dummy variable will be one for that month and the following months and zero for months before the adoption month. Such operationalization of the variables accounts for temporal factors that may simultaneously affect loyalty app adoption in between users (Xu et al. 2016). Individual (τ<sub>i</sub>) and monthly (α<sub>t</sub>) dummy variables are included to control for customerspecific heterogeneity and longitudinal systematic changes common across all customers. The coefficient of interest, $\cdot \beta _ { 2 } ,$ captures the effects of loyalty app adoption on the four key dependent variables for adopters after adoption in comparison with nonadopters.

Table 2 reports the estimation results of model (1) using a sample based on our baseline matching technique (i.e., one-to-one matching without replacement). The estimates of $\beta _ { 2 }$ indicate that point redemption expenditure and purchase frequency increase by 21.05% and 23.49%, respectively. Furthermore, the outof-pocket expenditure and purchase frequency also increase by 37.58% and 40.49%, respectively, thus supporting Hypothesis 1 (p < 0.01).

These results indicate that consumers spend more money and purchase more often on pure cash transactions and pure point redemption transactions after loyalty app adoption. To validate our findings, we perform two sensitivity analyses—Rosenbaum bounds analysis (Rosenbaum 2002) to account for the magnitude of hidden bias and the relative correlation restriction analysis (Krauth 2016) to account for the presence of unobserved selection with regard to the treatment effect (see Online Appendix B). Nonetheless, the causal relationship between loyalty app adoption and behavior change should be interpreted with caution because the selection biases related to unobservable attributes cannot be completely ruled out in our setting in which the adoption of loyalty apps was not exogenously assigned to each customer.<sup>4</sup>

## 5.4. Spillover Effects Across Stores

Despite the merits of loyalty apps, there are risks associated with the integration of mobile technology with the card-based LP. For instance, the ease of location-based search via loyalty apps may create a store-level spillover effect, wherein loyalty app adopters visit more stores that they would otherwise disregard. From a firm’s perspective, such spillover effects may not necessarily be constantly advantageous and may not be equally applicable to all stores within an MVLP.

To ascertain the existence of cross-store spillover effects, we calculate individual customer’s expenditure in every store during the pretreatment period and identify in which store the customer spent the most (we refer to the store as a focal store). Given that loyalty app adopters increase their spending and store visits (compared with plastic card users) after adoption, we assess whether customers change their spending share and amount from the focal store after adopting the loyalty app. To this end, we first calculate the number of stores visited and use this as a dependent variable. Second, we divide each customer’s expenditure at the focal store by the total expenditure during the pre- and posttreatment periods to obtain the variable focal store purchase percentage. Hence, a negative coefficient would imply that despite an increase in total expenditure, customers spend disproportionately less in their focal store after adoption of the loyalty app. We also calculate purchase frequency ( focal store purchase frequency) and expenditure level ( focal store expenditure level) from a focal store in the absolute values because the absolute amount of expenditure could increase despite a decrease in the percentage spent.

Results in panel A of Table 3 indicate that customers visit more stores after adoption of the loyalty app. However, despite the increase in an individual’s total expenditure after adoption, customers spend less in their focal store in terms of both percentage and absolute amount.

These findings suggest that the use of loyalty apps is associated with an increase in store-level competition, providing support for Hypothesis 2 (p < 0.01).

Table 2. Effects of Loyalty App Adoption on Point Redemption and Purchase Behaviors

<table><tr><td rowspan="2">Hypothesis 1</td><td colspan="2">Point redemption</td><td colspan="2">Out of pocket</td></tr><tr><td>Expenditure</td><td>Frequency</td><td>Expenditure</td><td>Frequency</td></tr><tr><td>Adoption ( $\beta_1$ )</td><td>0.136***(0.0140)</td><td>0.193***(0.0180)</td><td>-0.0173(0.0302)</td><td>-0.0315(0.0300)</td></tr><tr><td>Adoption × Treatment ( $\beta_2$ )</td><td>0.191***(0.0090)</td><td>0.211***(0.0118)</td><td>0.319***(0.0233)</td><td>0.340***(0.0236)</td></tr><tr><td> $R^2$ </td><td>0.342</td><td>0.355</td><td>0.182</td><td>0.201</td></tr><tr><td>No. of observations</td><td>53,984</td><td>53,984</td><td>53,984</td><td>53,984</td></tr><tr><td>No. of users</td><td>7,712</td><td>7,712</td><td>7,712</td><td>7,712</td></tr></table>

Notes. The robust standard errors are enclosed in parentheses (clustered on individuals). We used oneto-one matching with common support and a caliper size of 0.2× standard deviation. The unit of analysis is at the user-month level. After the inclusion of individual time-invariant variables without individual fixed effects, the results remained robust for all of the variables  
\*\*\*p < 0.01.

This result is contrary to the motivation behind the implementation of MVLPs: firms expect a greater share of profit as customers visit more stores on a regular basis. Thus, despite an increase in the number of stores from which customers purchase products after the adoption of the loyalty app, such spillover may not always be rewarding for all parties.

## 5.5. Deal-Susceptible Behaviors of Customers

Previous literature asserts that because not all customers enrolled in an LP are profitable for a firm, a more beneficial strategy is to exclude unprofitable customers and concentrate on serving high-profit consumers (Shin et al. 2012). Likewise, although previous analyses highlight the positive aspects of a mobile medium, low search costs for promotions and discounts may lead to deal-susceptible behaviors among customers, thereby fostering an environment that encourages membership from unprofitable customers.

The high information accessibility provided by mobile devices may expose consumers to promotional information anywhere and anytime, and it may also strengthen the bond between a firm and its customers. At the same time, the low search cost enabled by mobile technology may engender a dealsusceptible behavior that involves hunting for discounts, generating negative profits for retailers (Talukdar et al. 2010). We operationalize the deal susceptibility as discount percentage from purchases. Panel B of Table 3 illustrates that, on average, customers tend to reserve a high proportion of their spending for promoted products after loyalty app adoption, lending support for Hypothesis $\bar { 3 ( p < 0 . 0 1 ) }$

To delve into the economic impact of the deal proneness evoked by loyalty apps, we first create indicators for the number of purchases by individuals during the pretreatment period. We then interact the interaction dummy of the treatment and adoption variables with the dummies for each subgroup. Hence, the interaction is incorporated into the analysis on the basis of the number of purchases during the pretreatment period, allowing an estimation of the following specification (Blake et al. 2015):

$$
\begin{array}{l} \text {Discount percentage} _ {i g t} \\ = \beta_ {1} \big (\text {Treatment} _ {i} \times \text {Adoption} _ {i t} \times \text {Indicator} _ {i g} \big) \\ + \beta_ {g} + \varepsilon_ {i t}. \end{array}\tag{2}
$$

In Equation (2), $g \ ( = 4 , \ldots , 1 6 )$ indicates the user segment based on purchase frequency. For example, customers who purchased seven times in the pretreatment period would belong to the g = 7 segment. Figure 1 plots the DID interaction estimates $( { \bar { \beta } } _ { 1 } )$ for each segment and shows that less active users engage in deal-susceptible behaviors more frequently. We can therefore infer that loyalty app adoption is related to the susceptibility of consumers to deals and may thereby undermine the profitability of loyalty programs.

## 6. Disentangling the Mobile Channel Effect and In-app Function Effect of Loyalty App Adoption

In this section, we focus on the two underlying factors that markedly differentiate loyalty apps from plastic cards: mobile channel and in-app function effects. The mobile channel effect refers to the intrinsic characteristic of mobile channels (i.e., portability and always-on connectivity), which reflects the lower time and effort required to initiate a search process for acquiring information.<sup>5</sup> Meanwhile, the in-app function effect mainly concerns the additional in-app functions provided exclusively by loyalty apps and that are unavailable on web browsers. To the best of our knowledge, the opportunities offered by mobile technologies have not motivated active inquiries into the differential effects of loyalty app adoption in relation to MVLPs.

Table 3. Increased Store-Level Competition and Customer-Level Deal-Susceptible Behavior

<table><tr><td></td><td>Dependent variable</td><td>Interaction term</td><td> $R^2$ </td><td>No. of observations</td><td>No. of users</td></tr><tr><td colspan="6">Panel A: Store-level competition (Hypothesis 2)</td></tr><tr><td>(1)</td><td>Number of stores visited</td><td>0.077*** (0.0098)</td><td>0.404</td><td>53,984</td><td>7,712</td></tr><tr><td>(2)</td><td>Focal store purchase percentage</td><td>-0.0354*** (0.00733)</td><td>0.437</td><td>45,244</td><td>7,712</td></tr><tr><td>(3)</td><td>Focal store purchase frequency</td><td>-0.0292*** (0.00714)</td><td>0.218</td><td>53,984</td><td>7,712</td></tr><tr><td>(4)</td><td>Focal store expenditure level</td><td>-0.0738** (0.0324)</td><td>0.341</td><td>53,984</td><td>7,712</td></tr></table>

Panel B: Deal-susceptible behavior (Hypothesis 3)

<table><tr><td>Discount percentage</td><td>0.0038*** (0.0016)</td><td>0.794</td><td>45,244</td><td>7,712</td></tr></table>

Notes. Robust standard errors are in parentheses (clustered on individual). Equation (1) is used while using different dependent variables, and the number of brands visited is included as a covariate to control for customers’ brand usage intensity. Results remain consistent after including discount percentage, focal store purchase percentage, and focal store purchase frequency in the matching variables of PSM (results are available on request). The number of observations for focal store purchase percentage and discount percentage falls short of the total observations given that the months in which customers did not make a purchase were excluded from the analysis  
\*\*\*p < 0.01; \*\*p < 0.05.

Figure 1. Deal-Susceptible Behavior and Purchase Frequency with 95% Confidence Intervals  
![](/api/attachments/7UQ23PV2/fulltext/images/80983b43cbdfef6b02bea81255b660b079b3d3a13f4efc754325a02b2e7d96ce.jpg)  
Notes. Dotted line represents the trend line. Error bars are at 95% confidence intervals.

Because the loyalty app in our study encompasses both effects, we disentangle them by collecting additional data on adopters of the so-called basic app. Plastic card users of our focal loyalty program can enroll via two types of apps: a branded app (focal app) and a basic app. The branded app is an innovation launched exclusively by the brand or loyalty program of interest (e.g., Starbucks LP) and offers various inapp functions (i.e., sending gifts to friends or connecting to affiliated online shopping malls) provided by most other loyalty apps. When customers activate the branded app, they are directed to a landing page that displays a range of functions and information related specifically to the focal LP. Thus, a branded app encompasses both the mobile channel and in-app function effects. Unlike the branded app, the basic app (i.e., Loyalty Card Keychain, Loyalty Card Wallet)<sup>6</sup> refers to a mobile app that is akin to an all-inclusive repository of customers’ memberships; that is, customers can register several loyalty reward programs to which they subscribe in a single basic app. For instance, if a customer is enrolled in three LPs, he or she can put all of these on record in the basic app, similar to how a mobile wallet for LPs is used. A key difference between the branded and basic apps is that additional functions and features are unavailable via basic apps, with which users can only register loyalty programs and then, earn and redeem loyalty points. Hence, basic apps include the mobile channel effect but without the in-app function effect.<sup>7</sup>

Given the structural difference between branded and basic apps, we explore mobile channel and in-app function effects by comparing the treatment effects of these two loyalty apps. We replicate our main identification strategies to control for selection bias by conducting PSM between 21,583 basic app adopters and 3,856 branded app adopters, resulting in a sample of 3,856 pairs of matched basic app and branded app adopters. Next, to acquire matched pairs for basic app adopters and nonadopters, we additionally conduct PSM between the matched 3,856 basic app adopters and nonadopters who were not originally included in our sample. Hence, our final sample consists of 7,712 nonadopters (3,856 users matched with basic app adopters and 3,856 users matched with branded app adopters) and 7,712 app adopters (3,856 basic app adopters and 3,856 branded app adopters). We then interact the indicator variable (BrandedApp) that takes the value of one for branded app adopters and zero otherwise with the interaction effect to create a three-way interaction term and fulfill the following specification:

$$
\begin{array}{l} \ln (O _ {i j t}) = \beta_ {1} A d o p t i o n _ {i j t} + \beta_ {2} A d o p t i o n _ {i j t} \times T r e a t m e n t _ {i} \\ \quad + \beta_ {3} A d o p t i o n _ {i j t} \times T r e a t m e n t _ {i} \times B r a n d e d A p p _ {i} \\ \quad + \varphi \mathbf {X} _ {i} + \alpha_ {t} + \varepsilon_ {i t}. \end{array} \tag {3}
$$

The variables Adoption and Treatment are defined the same way as in Equation (1), and we include indi vidual time-invariant customer information and BrandedApp as controls (X ). The key coefficients of interest are $\beta _ { 2 }$ and $\beta _ { 3 } ,$ , denoting the mobile channe and in-app function effects, respectively. The threeway interaction term estimates the extent to which the moderator (whether the adopters adopted branded app or basic app) affects the app adoption effect. To reiterate, basic apps enable users to leverage mobile channels by allowing them to check available redemption points at any time with higher convenience and accessibility (i.e., mobile channel effect), but such apps do not generate functional effects because they do not offer additional functions or features that are available via branded apps. Before presenting our results, we direct attention to the fact that our in tention is to disentangle channel and in-app function effects and not the effect of each app function. As shown in Table 4, both have a significantly positive impact on all four dependent variables. Interestingly, we observe a differential effect of each element on outof-pocket and point expenditure behaviors. For instance, the channel element exhibits a strong impact when it comes to activating out-of-pocket spending, whereas no significant difference in magnitudes exists between the mobile channel and in-app function effects with respect to point redemption behaviors. Specifically, the higher information accessibility and lower search cost (i.e., mobile channel effect) granted by loyalty apps are effective in activating both customer purchase and point redemption behaviors. In addition, the availability of in-app functions also contributes to more active purchase and point redemption behaviors. We also examine whether the channel and function usage factors have differential effects on the store-level purchases and find that in-app function effects contribute to an increase in dealseeking behavior; both effects contribute to an increase in the number of stores visited, whereas only the in-app function effect is associated with the spillover effect of store-level purchases (details of these results are available in Online Appendix C).

## 7. Robustness Checks

Because we used observational data in our empirical analyses wherein customers were not randomly assigned to either the control or treatment group, there may be both observable and unobservable differences between the two groups affecting the decision to adopt the loyalty app. Hence, to validate the consistency of our main results, we conduct a series of robustness checks and falsification tests in multiple dimensions. First, we account for additional observable differences that may affect the result of loyalty app adoption. Specifically, we use alternative PSM specifications, include additional sets of variables in the matching procedure, and use an alternative matching procedure (i.e., coarsened exact matching). Second, because the matching procedures do not capture the differences related to unobservable factors, we carry out several analyses to examine the robustness of our results to the unobservable differences. Specifically, we account for customers’ planned behaviors by using alternative matching methods and analysis periods,<sup>8</sup> conducting forward-looking matching (Xu et al. 2016) procedures, and using Heckman’s two-step correction approach (Heckman 1979) and a treatment effects model (Maddala 1983). Third, by using the relative time model (Greenwood and Agarwal 2016), we assess whether our results are biased by the heterogeneous trend in the preadoption period between the two groups. Fourth, to eliminate the possibility that our treatment effect has occurred spuriously, we conduct a set of falsification tests. In doing so, we randomly assign adoption period and treatment groups to assess whether our results are not a mere consequence of spurious correlation that occurred by a random chance. Fifth, we assess the robustness of our results by using alternative model estimators and model setup, such as using equivalent gender distribution because the majority of the customers in our sample are female, considering serial correlation in standard errors, and using count models for count-dependent variables. Sixth, we carry out additional analyses to rule out alternative explanations to our findings, such as outliers driving the treatment effects. The results remain consistent throughout the series of robustness checks, and the details are provided in Online Appendix D.

## 8. Implications and Conclusion

Using large-scale transaction data obtained from a multinational retailer, we assessed how a shift from traditional loyalty cards to mobile-driven loyalty apps affects consumers’ reward redemption patterns, purchase behaviors, and store-level competition. The findings indicate that loyalty app adoption is associated with increased expenditure and purchase frequency as well as more active point redemption. In an MVLP context, the use of loyalty apps is associated with spillover effects in which case customers visit more stores that they had not previously considered and exhibit diminished allegiance to their focal shop after they adopt a loyalty app. Finally, the adoption of loyalty apps is related to deal-prone behaviors because informed consumers tend to selectively purchase highly discounted products.

Our findings provide several valuable implications for managers and platform owners who are considering launching mobile LPs and participating in an MVLP market. Although the merits of loyalty app adoption are apparent, we caution against potential downsides at individual store levels. Many customers are likely to succumb to deals, selectively purchasing highly discounted products with low margins through loyalty apps. Because consumers are typically in constant engagement with their mobile devices, they can easily access information and strategically forage for inexpensive goods or products on promotion. The thrust of LPs should be directed toward fostering a strong connection with a brand, going beyond the promise of deals and promotions. Yet, loyalty apps can mold consumers into increasingly price-responsive individuals because these apps function as channels for promotions and deals. Managers should therefore endeavor to reinforce loyalty among customers who may display a predilection for deals and discretely establish a point redemption system with consideration that the benefits derived from MVLPs tend to steer customers away from their focal stores. Notwithstanding the general increase in consumers’ total expenditure and the number of stores they visit, the frequency with which they purchase in focal stores can decrease. These findings suggest that mobile-driven LPs place many individual stores at risk and further intensify “local” competition among participating offline stores. Store managers should correspondingly be mindful that their consumers can always be “mobile” as their choice sets expand and that such mobility can further increase after loyalty app adoption, particularly in an MVLP environment. Focal stores may therefore face intensified local rivalry and suffer from declining loyalty from their regular patrons. This implies that collaboration is the principal driver of MVLP establishment but that competition can also be pivotal in determining the outcome of such an arrangement. That is, both collaboration and competition among member retailers would increase after the adoption of loyalty apps.

Table 4. Main DID Estimation Results with Mobile Channel Effect and In-app Function Effect

<table><tr><td rowspan="2"></td><td colspan="2">Out of pocket</td><td colspan="2">Point redemption</td></tr><tr><td>Expenditure</td><td>Purchase frequency</td><td>Expenditure</td><td>Purchase frequency</td></tr><tr><td>Adoption × Treatment ( $\beta_2$ )</td><td>0.216***(0.0247)</td><td>0.238***(0.0249)</td><td>0.110***(0.00976)</td><td>0.168***(0.0153)</td></tr><tr><td>Adoption × Treatment × BrandedApp ( $\beta_3$ )</td><td>0.107***(0.0210)</td><td>0.108***(0.0206)</td><td>0.114***(0.0117)</td><td>0.169***(0.0130)</td></tr><tr><td> $R^2$ </td><td>0.031</td><td>0.027</td><td>0.026</td><td>0.026</td></tr><tr><td>No. of observations</td><td>107,968</td><td>107,968</td><td>107,968</td><td>107,968</td></tr><tr><td>No. of users</td><td>15,424</td><td>15,424</td><td>15,424</td><td>15,424</td></tr></table>

Notes. Robust standard errors are in parentheses (clustered by individual). We confirm that the difference in matched variables for two groups was statistically insignificant and that the matched sample represents the entire sample used for matching  
\*\*\*p < 0.01.

Similar to other research, our study is encumbered by certain limitations. First, panel data that cover seven months were used in our analysis. Although this duration should be sufficient to observe consumers’ repeat purchases and degrees of loyalty to a firm, we acknowledge that longer time horizons may provide more comprehensive insights. Future studies should use varying time windows to verify the consistency of our results. Moreover, with longer sample periods, future research can be grounded in a system panel approach that casts light on dynamic structural relationships among key dependent variables. Second, our research did not involve a randomized field experiment through which endogeneity issues can be more adequately addressed. Because the customers were not randomly assigned to treatment and control groups and they adopted the loyalty apps of their own volition, we cannot rule out selection biases related to unobservable attributes. We can only present arguments on treatment effects after accounting for such bias on the observable factors. Accordingly, our results must be interpreted with caution in terms of the causal relationship. For instance, we cannot concretely identify whether and to what extent loyalty app adoption drives behavior changes, and the availability of loyalty apps determines the separation of customers into different behavior groups. Furthermore, the customers could plan ahead for the purchase of food and beverages in many ways that we could not control on the basis of the available data set. Several robustness procedures have confirmed that biases arising from unobservable factors do not significantly influence findings. Nevertheless, future studies could conduct randomized field experiments to eliminate the possibility of influence from unobservable factors. Third, our investigation did not identify how consumers use each in-app function despite the fact that such innovations may be used in multiple ways to engage with an LP (e.g., checking points, obtaining localized push messages, or responding to promotions). Future studies can capitalize on more detailed app usage data to demonstrate how customer behaviors in each platform (e.g., mobile app or mobile web) change following mobileapp adoption and to determine how MVLP mobile apps work and how each function stimulates change in consumer behaviors.

Despite the noted shortcomings, this study broadens our understanding of the effects that mobile-based LPs exert on the dynamics of customer behaviors and the performance of companies. Vendors should take heed of potential hazards that may emerge from the mobiledriven digitalization of loyalty. Such threats may eventually diminish profitability and sustainability in the long run. An issue that warrants equally serious consideration is the possibility that consumer loyalty and dedication will decline in a digital environment where customers are afforded increased access to information and by extension, increased choice of brands or companies.

## Endnotes

<sup>1</sup> See https://loyaltyplant.com/blog/article-04-10-2018-why-mobile -loyalty-apps-are-rapidly-replacing-plastic-loyalty-cards.

<sup>2</sup> Plastic card and loyalty app users equally earn 5% of their expenditure as reward points.

<sup>3</sup> Note that cash (or out of pocket) includes all monetary transactions (e.g., cash, debit card, credit cards, electronic payments, and others) excluding loyalty point redemptions. The terms cash and out of pocke are used interchangeably throughout this paper.

<sup>5</sup> Although plastic card users can also access loyalty points through a mobile browser, they are less likely to be repeatedly exposed to the LP than loyalty app users are. We focus on the relative convenience of accessing the core functions between plastic card and mobile app LPs.

<sup>6</sup> See https://play.google.com/store/apps/details?id=protect.card\_locker or https://play.google.com/store/apps/details?id=com.panaustik .cardwallet (accessed on October 26, 2019).

<sup>7</sup> More details on the difference between the two types of apps are provided in Online Appendix C.1.

<sup>8</sup> We thank the senior editor for this suggestion.

## References

Andrews M, Luo X, Fang Z, Ghose A (2016) Mobile ad effectiveness: Hyper-contextual targeting with crowdedness. Marketing Sci. 35(2):218–233.

Bakos JY (1997) Reducing buyer search costs: Implications for elec tronic marketplaces. Management Sci. 43(12):1676–1692.

Bellman S, Potter RF, Treleaven-Hassard S, Robinson JA, Varan D (2011) The effectiveness of branded mobile phone apps. J. Interactive Marketing 25(4):191–200.

Berman B (2006) Developing an effective customer loyalty program. Calif. Management Rev. 49(1):123–148.

Bijmolt TH, Verhoef PC (2017) Loyalty programs: Current insights, research challenges, and emerging trends. Wierenga B, van der Lans R, eds. Handbook of Marketing Decision Models (Springer, Cham, Switzerland), 143–165.

Blake T, Nosko C, Tadelis S (2015) Consumer heterogeneity and paid search effectiveness: A large-scale field experiment. Econometrica 83(1):155–174.

Breugelmans E, Bijmolt THA, Zhang J, Basso LJ, Dorotic M, Kopalle P, Minnema A, Mijnlieff WJ, Wunderlich NV (2015) Advancing research on loyalty programs: A future research agenda. Marketing Lett. 26(2):127–139.

Calzolari G, Nardotto M (2016) Effective reminders. Management Sci. 63(9):2915–2932.

Clemons EK (2008) How information changes consumer behavior and how consumer behavior determines corporate strategy. J. Management Inform. Systems 25(2):13–40.

Dorotic M, Bijmolt TH, Verhoef PC (2012) Loyalty programmes: Current knowledge and research directions. Internat. J. Management Rev. 14(3):217–237.

Dorotic M, Verhoef PC, Fok D, Bijmolt TH (2014) Reward redemption effects in a loyalty program when customers choose how much and when to redeem. Internat. J. Res. Marketing 31(4):339–355.

Dreze X, Nunes JC (2004) Using combined-currency prices to lower \` consumers’ perceived cost. J. Marketing Res. 41(1):59–72.

Fong Z, Gu B, Luo X, Xu Y (2015) Contemporaneous and delayed sales impact of location-based mobile promotions. Inform. Systems Res. 26(3):552–564.

Ghose A, Goldfarb A, Han SP (2013) How is the mobile internet different? Search costs and local activities. Inform. Systems Res. 24(3):613–631.

Granados N, Gupta A, Kauffman RJ (2012) Online and offline demand and price elasticities: Evidence from the air travel industry. Inform. Systems Res. 23(1):164–181.

Greenwood BN, Agarwal R (2016) Matching platforms and HIV incidence: An empirical investigation of race, gender, and so cioeconomic status. Management Sci. 62(8):2281–2303.

Gupta S, Kim HW (2010) Value-driven internet shopping: The mental accounting theory perspective. Psych. Marketing 27(1):13–35.

Heckman JJ (1979) Sample selection bias as a specification error. Econometrica 47(1):153–161.

Huang P, Lurie NH, Mitra S (2009) Searching for experience on the web: An empirical examination of consumer behavior for search and experience goods. J. Marketing 73(2):55–69.

Hui SK, Inman JJ, Huang Y, Suher J (2013) The effect of in-store travel distance on unplanned spending: Applications to mobile promotion strategies. J. Marketing 77(2):1–16.

James D (2005) Guilty through association: Brand association transfe to brand alliances. J. Consumer Marketing 22(1):14–24.

Kim SJ, Wang RJ-H, Malthouse EC (2015) The effects of adopting and using a brand’s mobile application on customers’ subsequent purchase behavior. J. Interactive Marketing 31:28–41.

Kivetz R, Urminsky O, Zheng Y (2006) The goal-gradient hypothesis resurrected: Purchase acceleration, illusionary goal progress, and customer retention. J. Marketing Res. 43(1):39–58.

Krauth B (2016) Bounding a linear causal effect using relative correlation restrictions. J. Econom. Methods 5(1):117–141.

Lemon KN, Wangenheim FV (2009) The reinforcing effects of loyalty program partnerships and core service usage: A longitudina analysis. J. Service Res. 11(4):357–370.

Maddala GS (1983) Limited-dependent and Qualitative Variables in Econometrics (Cambridge University Press, Cambridge, UK).

Netemeyer RG, Heilman CM, Maxham JG III (2012) The impact of a new retail brand in-store boutique and its perceived fit with the parent retail brand on store performance and customer spending. J. Retailing 88(4):462–475.

Punj GN, Staelin R (1983) A model of consumer information search behavior for new automobiles. J. Consumer Res. 9(4):366–380

Ransbotham S (2015) Marketing in five dimensions. MIT Sloan Man agement Rev. 57(1):5.

Ransbotham S, Lurie NH, Liu H (2019) Creation and consumption of mobile word of mouth: How are mobile reviews different? Marketing Sci. 38(5):773–792.

Ray S, Kim SS, Morris JG (2012) Research note—Online users switching costs: Their nature and formation. Inform. Systems Res. 23(1):197–213.

Reinartz WJ, Kumar V (2003) The impact of customer relationship characteristics on profitable lifetime duration. J. Marketing 67(1): 77–99.

Rishika R, Kumar A, Janakiraman R, Bezawada R (2013) The effect of customers’ social media participation on customer visit frequency and profitability: An empirical investigation. Inform. Systems Res. 24(1):108–127

Rosenbaum PR (2002) Observational Studies (Springer, New York), 1–17.

Rosenbaum PR, Rubin DB (1983) The central role of the propensity score in observational studies for causal effects. Biometrika 70(1): 41–55.

Rubin DB (2006) Matched Sampling for Causal Effects (Cambridge University Press, Cambridge, UK).

Rust RT, Huang M-H (2014) The service revolution and the transformation of marketing science. Marketing Sci. 33(2):206–221.

Schumann JH, Wünderlich NV, Evanschitzky H (2014) Spillover effects of service failures in coalition loyalty programs: The buffering effect of special treatment benefits. J. Retailing 90(1): 111-118

Shin J, Sudhir K, Yoon D-H (2012) When to “fire” customers: Cus tomer cost-based pricing. Management Sci. 58(5):932–947.

Shugan SM (2005) Brand loyalty programs: Are they sham? Marketing Sci. 24(2):185–193.

Stourm V, Bradlow ET, Fader PS (2015) Stockpiling points in linear loyalty programs. J. Marketing Res. 52(2):253–267

Sun Z, Dawande M, Janakiraman G, Mookerjee V (2017) Not just a fad: Optimal sequencing in mobile in-app advertising. Inform. Systems Res. 28(3):511–528

Talukdar D, Gauri DK, Grewal D (2010) An empirical analysis of the extreme cherry picking behavior of consumers in the frequently purchased goods Marketing J. Retailing 86(4):336–354.

Taylor GA, Neslin SA (2005) The current and future sales impact of a retail frequency reward program. J. Retailing 81(4):293–305.

Thaler R (1985) Mental accounting and consumer choice. Marketing Sci. 4(3):199–214.

Viswanathan V, Hollebeek LD, Malthouse EC, Maslowska E, Jung Kim S, Xie W (2017) The dynamics of consumer engagement with mobile technologies. Service Sci. 9(1):36–49.

Xu K, Chan J, Ghose A, Han S (2016) Battle of the channels: The impact of tablets on digital commerce. Management Sci. 63(5):1469–1492.

Zajonc RB (1968) Attitudinal effects of mere exposure. J. Personality Soc. Psych. 9(2):1–27.
