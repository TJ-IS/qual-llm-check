---
otero_id: 7946
otero_key: "T65NB578"
title: "Understanding the formation of reciprocal hyperlinks between e-marketplace sellers"
authors: "Zhaoran Xu; Youwei Wang; Yulin Fang; Bernard Tan; Hai Sun"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.05.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Understanding the formation of reciprocal hyperlinks between e-marketplace sellers

Zhaoran Xu <sup>a</sup>, Youwei Wang <sup>a,</sup>⁎, Yulin Fang <sup>b</sup>, Bernard Tan <sup>c</sup>, Hai Sun <sup>a</sup>

<sup>a</sup> Department of Information Management and Information Systems, School of Management, Fudan University, 670 Guoshun Road, Shanghai, China

<sup>b</sup> Department of Information Systems, City University of Hong Kong, 83 Tat Chee Avenue Road, Kowloon, Hong Kong Special Administrative Region

<sup>c</sup> Department of Information Systems, National University of Singapore, Computing 1, 13 Computing Drive, Singapore

## a r t i c l e i n f o

Article history: Received 11 May 2016 Received in revised form 1 May 2017 Accepted 2 May 2017 Available online 8 May 2017

Keywords: Online seller Hyperlink exchange Market commonality Geographical distance Seller reputation

## a b s t r a c t

Online sellers in the e-marketplace cooperate with each other to increase resources and reduce transaction costs, both of which are crucial to the success of small businesses. A commonly used IT-enabled strategy is to ally with other online sellers by exchanging hyperlinks. This paper provides theoretical guidance to sellers on how to choose partners to improve reciprocity rates in hyperlink formation. Using the resource-based view and transaction-cost rationale, we examine the effects of market conditions and seller reputation on reciprocity link formation, using real transaction data from the largest online marketplace in China. The findings indicate that partners are less likely to exchange hyperlinks if the two sellers sharing a link are in highly overlapping markets and are geographically distant from one another, but the two factors weaken each other's negative effects. The study also explores the moderating effect of seller reputation, and finds that the negative effect of market commonality is weakened by seller reputation. The results of this study can be extended to other types of small business cooperation and are also useful to platform operators for designing mechanisms to encourage cooperation among online sellers.

© 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

Over the past decade, more and more sellers have conducted their business on e-marketplace platforms, such as eBay, Amazon and Taobao (an e-marketplace owned by Chinese e-commerce giant Alibaba). The large number of sellers leads to intensified competition in the e-marketplace. For example, by the end of 2013, more than eight million active sellers were competing on Taobao. The majority of these are small business owners [1–3] with limited resources and market presence, and are vulnerable to environmental forces [4]. According to a recent study [5], in 2010, 38.4% of the sellers in apparel shut down their businesses within six months of establishing their stores on Taobao. To survive the competition, online sellers cooperate with each other and undertake the same alliance activities as traditional bricks-and-mortar firms, such as co-branding and co-marketing. In addition, they deploy distinct strategies which rely on Internet infrastructures in an e-marketplaces [6]. The strategies involve forming alliances with other online sellers by exchanging website hyperlinks.

Hyperlink is an important feature of World Wide Web (WWW) [7]. It enables visitors to jump from one webpage to another by clicking on links embedded in the hypertexts. Because there are numerous webpages with similar information contents or services, these webpages have to attract visitors' attention by unique service offerings and techniques. Exchanging hyperlinks is a technique commonly utilized by Internet web services (more broadly those techniques fall into the category of search engine optimization). It is well known that exchanging hyperlinks can lift the rankings of the website in major search engines such as Google [8,9]. This is because websites with large number of hyperlinks will be given higher priority in search engines' ranking algorithm. In e-marketplaces, each seller manages an online store and the key motivation of exchanging hyperlinks is simply to attract and exchange web browsing traffic because this can lead to more online purchases [10,11]. Taking Taobao as an example, a focal seller links to another seller (link seller) by putting a hyperlink on its store front (typically on the left sidebar). This is an outgoing link for the focal seller. When customers browse the focal seller's shop, they may visit the link seller by clicking on the hyperlink. The link seller can establish a hyperlink back to the focal seller, which would be an incoming link or reciprocal link for the focal seller. When this happens, the two sellers exchange hyperlinks successfully.

Prior studies have shown that exchanging hyperlinks can help online sellers to achieve success by growing the customer base [12], enhancing customer trust [13,14], and eventually improving sellers' competitive advantage [15]. Hyperlinks can improve the seller's revenue and profit but the effects only lies in the incoming links [16]. Incoming links make it easier for customers to discover the seller whereas outgoing links can reduce customer traffic and undermine the performance of the seller [17]. Thus, online sellers with more incoming hyperlinks and fewer outgoing links tend to perform better [10]. If hyperlink exchange fails and the target seller does not reciprocate by placing a hyperlink back to the focal seller on its online store, the focal seller may suffer the loss of customers from the outgoing links.

Although it is obvious that having more incoming links and less outgoing links are often good for focal sellers [10,17], it is not clear how such goals can be achieved. This is because each seller can only control its outgoing links but not the incoming links. What usually happens is that sellers initiate hyperlinks to other sellers in the hope that some of them will reciprocate by linking back. However, no prior study has examined how sellers may get more reciprocal links in e-marketplaces. To fill this important gap in knowledge, this paper investigates the following research question: What types of partner sellers are more likely to exchange hyperlinks in an online marketplace?

To address this question, we build on the literature of alliance formation in the field of strategy by conceptualizing hyperlink exchanges as exchanges of customer resources. In the strategy literature, there are two kinds of antecedents in alliance formation. One is the individual characteristics of the partner firm, such as status or age [18]; the other is the dyad characteristics between the alliance partners, such as market commonality [19]. These factors can be better understood using theoretical perspectives like resource-based view and transaction-cost rationale [20].

Utilizing a dataset collected from Taobao, this study proposes and empirically validates the main effects and the interaction of market commonality and geographical distance (two market conditions between the partner sellers), and the moderating effects of reputation (a key characteristic of online sellers). Market commonality is the extent of overlap in the market segments of alliance partners. Geographical distance is the physical distance between alliance partners. Specifically, this study finds that sellers are less likely to exchange hyperlinks if they operate in highly overlapping markets and are geographically distant from each other, but the two factors weaken each other's negative effects. In addition, the negative effects of market commonality are ameliorated by seller reputation. These findings have important theoretical and empirical implications. Theoretically, these findings extend the generalizability of related theories from traditional bricks-and-mortar industries to e-marketplaces. Practically, these findings help online sellers to make better decisions about how to cooperate with other sellers and help platform operators make better decisions about how to enhance collaborations in e-marketplaces.

## 2. Theoretical background

2.1. Resource-based view and transaction-cost rationale on alliances in emarketplaces

The strategy literature offers theoretical guidance as to why firms enter into alliances. The resource-based view argues that firms should possess resources that are rare, valuable, imperfectly mobile, and non-substitutable to achieve competitive advantage [21]. Thus, developing and leveraging resources is a key driver for alliance formation [22]. The transactioncost rationale recommends that firms form alliances to minimize their fixed and continual transaction costs [23]. The literature suggests that firms tend to put resource concerns ahead of cost concerns when deciding whether or not to engage in alliances [24] but considerations of economic costs can influence inter-firm relationships [25]. Therefore, this study supplements the resource-based view with the transaction-cost rationale in discussing alliance formation in e-marketplaces.

Alliance formation may differ depending on industry structure and competitive situation [26]. Given that this study is about e-marketplaces, the characteristics of the online environment have to be considered when examining resource maximization and cost minimization in alliance formation. Online sellers in e-marketplaces are small businesses which lack resources [27]. The resource-based view suggests that, to survive, they need access to resources of alliance partners, especially customer resources [6]. Indeed, it is critical for these small business to expand their customer base [28]. But it is difficult for these small business to retain customers because online retailing allows customers to transact with many different sellers [29]. Thus, in e-marketplaces, customer resources are vital but easy to come and go. Sellers engage in alliances to cooperate and compete for customer resources at the same time. The cooperation level (or competition level) depends on market conditions, such as market commonality and geographical distance [30].

Another important resource for online sellers is their reputation. Customers attach considerable importance to seller reputation in emarketplaces [14] and seller reputation positively affects revenue and total sales [31,32]. Online sellers should consider the reputation of prospective partners when forming alliances [33]. A good reputation improves the benefits of forming alliances [34]. Thus, this study also examines the role of seller reputation in the exchange of hyperlinks.

Unlike production costs, transaction costs are incurred in organizing information, coordinating behaviour, monitoring transactions, and safeguarding interests [35]. Online sellers use e-marketplaces to select alliance partners and execute transactions, which lower search costs compared to traditional approaches [36]. However, coordination costs are higher in e-marketplaces for two reasons. First, the online environment is complex in the sense that partners can leverage on environmental uncertainty and information asymmetry to be more opportunistic [37]. Second, competition tends to be fiercer in e-marketplace and this creates conflicts in alliances, which increase coordination costs [38]. Thus, e-marketplace alliances incur lower search costs and higher coordination costs compared to alliances in bricks-and-mortar industries.

## 2.2. Market conditions and alliance formation in e-marketplaces

This study examines two market conditions: market commonality and geographical distance. Market commonality is commonly known as “the degree of presence that a competitor manifests in the markets it overlaps with the focal firm” [39]. When firms operate in overlapping markets, they have higher market commonality and more collective strength compared to partner firms operating in distinct industries [19].

Research has shown that firms with high market commonality are more likely to form alliances because they share similar resources. This makes it easier for them to achieve economy of scale by aggregating similar resources through alliances [19,40]. Although there may be higher search costs associated with screening prospective alliance partners [41], firms in the same markets are usually quite familiar with each other and share common market knowledge [42]. This familiarity decreases the costs of searching for prospective partners and makes the process less time-consuming [43]. Thus, firms with high market commonality are likely to form alliances.

But research has also suggested that firms with low market commonality tend to cooperate [18,22,43]. Firms that are in different markets can also form alliances to develop new and complementary resources [44]. In this situation, firms tend to cooperate when their partners have strengths that can make up for their weaknesses [18]. They also cooperate to exploit business opportunities from their partners in different markets [40]. Besides, firms with low market commonality are less likely to find themselves competing in the same market [45]. Overall, past studies have indicated that market commonality is important to alliance formation. However, given that the business environment in e-marketplaces is different, it is important to re-examine this issue of alliance formation in the context of e-marketplaces.

Geographical distance is commonly known as the spatial or physical distance between economic actors, such as alliance partners [42]. Geographical distance is well documented in the international business [46,47] and industry cluster literature [48,49]. In alliance formation, remote partners can help firms reach out to different, diverse, and non-redundant resources that co-located firms cannot [47]. Because it can be difficult for firms to reach customers in distant markets, remote partners can provide access to these new markets, thus making alliance formation more likely [6,12].

But having co-located partners can lowers cost associated with distance (such as communication costs [50]) and search costs for identifying useful competences [51]. In addition, geographically distant partners are more likely to behave opportunistically, which can undermine trust in the alliance [42]. Thus, geographically distant firms tend to prefer deeper inter-partner relationships (e.g., joint venture or merger and acquisition) over alliances [52].

Studies have also reported that geographic distance is not particularly relevant to alliances under heterogeneous industry characteristics [49]. Furthermore, advances in communications technologies may weaken the role of geographical distance [53]. Therefore, it is useful to re-examine the role of geographical location in an online environment. The effects of the two market conditions may be interdependent. For example, partners in different markets (i.e., low market commonality) can help each other access new markets [40] but geographical distance can make it more difficult and costly to form alliances with partners [52]. Therefore, this study explores the interaction effects of market commonality and geographical distance.

## 2.3. Firm reputation and alliance formation in e-marketplaces

Compared to bricks-and-mortar shops, customers tend to perceive more risks in transacting with sellers in e-marketplaces. Thus, the reputation of online sellers plays a significant role in attracting customers [54]. The concept of reputation is different from that of status but prior studies have often confused the two [55]. Status represents the order or rank of the firm in a market whereas reputation indicates the quality of the firm as determined by its previous actions and this is a market signal when information is asymmetric [56].

The resource-based view suggests that reputation is a valuable resource to the firm [18] and can affect the exchange of resources because high reputation enhances trust in inter-firm relationships [57]. The transaction-cost rationale suggests that opportunism is a major concern in alliances and so a good reputation helps to reduce cooperation costs by enhancing trust. For example, negotiation costs are reduced when reputation improves trust between partner firms [58]. Thus, reputation can enhance the competitive advantage of partners and has a positive effect on alliance formation [59]. This study focuses on the moderating role of reputation on the effects of market conditions. For example, the good reputation of the potential partner may reduce the opportunistic risk arising from geographical distance.

## 3. Hypotheses development

## 3.1. Main effects of market conditions

Market commonality is commonly measured by sellers' product categories [18,22,43]. A single online seller can have multiple product categories. Overlapping categories between two partner sellers increase market commonality.

Based on the resource-based view, a major benefit of forming alliance among online sellers is that this increases the customer base for all sellers in the alliance [12]. As discussed above, research has shown that both high and low market commonality between alliance partners can improve their access to customers [22,40,43]. Traditionally, firms in overlapping markets form alliances to share similar resources and compete with outsiders [19,60]. In e-marketplaces, there can be numerous sellers in each product category that alliances are often loose and informal [28]. Moreover, sellers with high market commonality are competitors [61] because it is easy for customers to switch from one seller to another. Thus, plenty of online traffic flows through hyperlinks connecting sellers. These links provide opportunities for customers to leave [10], undermining the long-term interests of sellers [29]. In this situation, partner sellers with many overlapping products (i.e., high market commonality) are at greater risk of losing customers to their partners. On the contrary, partner sellers with few overlapping products (i.e., low market commonality) can help each other by facilitating customer purchase from both sellers through their hyperlinks.

The transaction-cost rationale suggests that search costs associated with finding the right partner are lower when partners have high market commonality in bricks-and-mortar industries [40]. However, this cost advantage is not as salient in e-marketplaces because search costs are low, regardless of market commonality [37]. Thus, the lower search costs that come with high market commonality are not applicable in emarketplaces. On the contrary, competition arising from high market commonality brings more costs, such as the need for extra services to retain customers [4]. Therefore, market commonality has a negative effect on hyperlink exchange (i.e., alliance formation) in e-marketplaces:

H1. Partner sellers are more likely to exchange hyperlinks if market commonality among the two sellers (in terms of product categories) is lower.

Every online seller has a physical location (their inventory site). In this study, geographical distance is measured by absolute distance between a pair of partner sellers based on their respective physical locations [62]. Taking the resource-based view, prior research suggests that long-distance alliances can provide access to new customers in remote markets and such access would be difficult without the alliances [47,48]. However, in e-marketplaces, market access is not restricted by location because sellers can easily overcome barriers of geographical distance to reach far-flung customers. Prior research also suggests that having nearby partners can help sellers increase their customer base because customers prefer the convenience of visiting retail clusters [63]. Having nearby partners bring in other resources, such as access to common specialised suppliers and skilled labour pools [48]. In e-marketplaces, closely-located partnerships can still increase customer base because customers may prefer to make multiple purchases from nearby sellers for reasons such as lower shipping costs and shorter delivery schedule for these purchases collectively [63,64]. Thus, lower geographical distance can still contribute to alliance formation.

Past research suggests that it can be more costly to monitor and coordinate geographically distant partnerships because partners are more likely to behave opportunistically [42,46]. This opportunism associated with environmental uncertainty [65] tends to be more pronounced in e-marketplaces due to the volatility [37]. For example, a seller may pursue an unfair competitive strategy (e.g., offering deep customer discounts) that undercuts its partner seller. Geographical distance can also undermine trust between partner sellers. This is because sellers tend to be less familiar with the service and product quality of distant partners and risks associating with disreputable distant partners [41]. Therefore, geographical distance has a negative effect on hyperlink exchange (i.e., alliance formation) in e-marketplaces:

H2. Partner sellers are more likely to exchange hyperlinks if geographical distance between the two sellers is shorter.

## 3.2. Interaction effects of market conditions

The negative effects of market commonality on alliance formation lie in the loss of customer resources when partner sellers' markets overlap [40,61]. However, geographical distance can reduce this loss of customer resources because, if the partner sellers are far apart, there is a lower chance that customers will switch from one seller to its partner seller through hyperlinks, given that customers still prefer nearby sellers for reasons such as lower shipping costs and shorter delivery schedule [64]. In this way, geographic distance between partner sellers can lessen their competition in overlapping markets and mitigate the associated costs. Therefore, geographical distance can weaken the negative effects of market commonality and sellers far away from each other are more likely to form alliances even if they are in highly overlapping markets.

Based on the transaction-cost rationale, sellers tend to avoid longdistance partnerships because these partnerships can incur higher monitoring and coordination costs as well as increase the risk of associating with low-quality partners [46]. To avoid engaging with an opportunistic partner, sellers need more market information to assess a prospective partner's future behaviour [66], and sellers with high market commonality tend to be more familiar with each other. This can reduce the coordination costs of alliances that arises from geographical distance [42]. Thus, market commonality can weaken the negative effects of geographical distance and sellers in highly overlapping markets are more likely to form alliances even if they are further away from each other.

H3. Market commonality and geographical distance have interaction effects such that they weaken each others negative effects on the likelihood of exchanging hyperlinks.

## 3.3. Moderating effects of reputation

Reputation plays a very important role in e-marketplaces because of the uncertainty of the online environment [54]. Sellers can improve their reputation and thereby attract more customers by forming alliances with partners with good reputation [34]. The benefits of seller reputation in e-marketplaces are well-known [59]. Going beyond past studies, this study examines the moderating effects of seller reputation on market conditions (market commonality and geographical distance).

Partners with high market commonality tend to have intensive competition that causes the loss of customers [40,61] so high market commonality has negative effects on alliance formation. This situation is aggravated when a partner seller has a better reputation that enables it to attract more customers [18,22]. Seller reputation is easily accessible in e-marketplaces due to wide availability of customer feedbacks. Therefore, high reputation of a partner seller strengthens the negative effects of market commonality on alliance formation.

H4. Higher reputation of a partner seller strengthens the negative effects of market commonality on the likelihood of exchanging hyperlinks.

Geographical distance increases the monitoring and coordination costs as well as the risk of associating with opportunistic partners [46]. To avoid engaging in less productive alliances, sellers can assess a prospective partner's likely future behaviour using its track record of past behaviours [66]. This practice may be particularly important for partners that are far away from each other given that they tend to have less information about each other [41]. However, such costs and risk arising from geographical distance is alleviated when a partner seller has a better reputation because such partner sellers tend to collaborate with other sellers so as to improve the overall customer purchase experience [59]. Therefore, high reputation of a partner seller weakens the negative effects of geographical distance on alliance formation.

H5. Higher reputation of a partner seller weakens the negative effects of geographical distance on the likelihood of exchanging hyperlinks.

## 4. Methodology

## 4.1. Dataset

Our dataset was obtained from Taobao, the largest e-marketplace in China. Taobao labels hyperlink exchanges as “friendship links”. Apparel sellers were examined in this study because apparel has been the bestselling product on Taobao. In 2011, there were 68 product categories on

Taobao. The 375,000 apparel sellers account for about 20% of the seller population. Competition was very intense in such a crowded market and sellers are motivated to collaborate in various ways, including exchanging friendship links.

Our data was collected in January 2011. The data was analysed at the dyad level, with the link itself as the unit of analysis. Each link involved two sellers: a focal seller and a link seller. There were two scenarios: (1) a focal seller sent an outgoing link to a link seller and the link seller decided whether to send a reciprocal link back to the focal seller; and (2) a focal seller received an incoming link from a link seller and the focal seller decided whether to send a reciprocal link back to the link seller. Information on both scenarios was included in our dataset.

A total of 1000 apparel sellers were randomly chosen as our focal sellers. Results of t-tests revealed that the difference between stock levels of sellers in our dataset and sellers in the population was not significant. Information was collected for friendship links of focal sellers (including outgoing hyperlinks and incoming hyperlinks) conditional on the following requirements: (1) the hyperlinks should be voluntary; (2) the hyperlinks should connect sellers with different identities (seller IDs); (3) two sellers connected by the hyperlinks should not share the same mailing address; and (4) the reciprocal hyperlinks were created within 20 days of the original hyperlinks (because the reciprocal hyperlinks might not be triggered by the original hyperlinks if the time interval was too long). Our dataset comprised 924 outgoing hyperlinks and 701 incoming hyperlinks for 323 focal sellers in the apparel industry.

## 4.2. Measurement

## 4.2.1. Dependent variable

When sellers received incoming hyperlinks as a consequence of sending outgoing hyperlinks to other sellers, these would be deemed reciprocal hyperlinks. Our analyses examined whether each hyperlinks was reciprocated and measured this as a binary variable, consistent with other studies on alliance partner selection [6,22,67]. Each outgoing hyperlink sent by a focal seller would be coded “1” if the focal seller received a reciprocal hyperlink later on and “0” otherwise. Each incoming hyperlink received by a focal seller would be coded “1” if the focal seller sent a reciprocal link later on and “0” otherwise.

## 4.2.2. Independent variables

4.2.2.1. Market commonality. Product category was used to measure the market commonality of sellers [18,22,43]. Taobao classifies the products on its platform into 68 categories and codes sellers into these categories based on major products they sell (using an algorithm that considers recently sold products). Each seller would have one or two major product categories. Market commonality was computed as follows:

Market commonality

∣Focal seller0s categories∩Link seller0s categories 二 ∣Focal seller0s categories∪Link seller0s categories

For example, if a focal seller traded apparel and bags and a link seller traded apparel and cosmetics, then they would have one common category (apparel) out of three categories (apparel, bags, and cosmetics) and their market commonality would be 0.33. The lowest possible market commonality of two sellers would be 0 (if they had no common categories) and the highest possible market commonality of two sellers would be 1 (if all their categories were identical).

4.2.2.2. Geographical distance. Geographical distance was computed based on absolute distance between the registered cities of the focal seller and the link seller [62]. This was measured in units of 1000 km to enlarge the coef cient estimates.

Table 1 Variable measurements.

<table><tr><td>Variables</td><td>Measurements</td></tr><tr><td>Reciprocal link</td><td>1 if focal seller or link seller received a reciprocal link, 0 otherwise</td></tr><tr><td>Market commonality</td><td>|Focal seller&#x27;s categories∩Link seller&#x27;s categories| |Focal seller&#x27;s categories∪Link seller&#x27;s categories|</td></tr><tr><td>Geographical distance</td><td>Absolute distance between the registered cities of the focal seller and the link seller (in 1000 km)</td></tr><tr><td>Seller reputation</td><td>Online seller&#x27;s ratio of positive ratings</td></tr><tr><td>Seller tenure</td><td>Online seller&#x27;s store age (in months)</td></tr><tr><td>Friendship links</td><td>Online seller&#x27;s number of existing friendship links</td></tr><tr><td>Assurance mechanism</td><td>1 if online seller participated in CRSP, 0 otherwise</td></tr></table>

Descriptive statistics and Pearson correlation matrix for apparel industry (focal seller → link seller).

<table><tr><td>Variable</td><td>Mean</td><td>S.D.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>1 Reciprocal link</td><td>0.26</td><td>0.44</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2 Market commonality</td><td>0.17</td><td>0.27</td><td>-0.12***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3 Geographical distance</td><td>1.26</td><td>1.31</td><td>-0.09***</td><td>0.03</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>4 Focal seller reputation</td><td>0.99</td><td>0.01</td><td>0.10***</td><td>0.08**</td><td>0.07**</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>5 Focal seller tenure</td><td>13.54</td><td>15.68</td><td>0.04</td><td>-0.06*</td><td>-0.09***</td><td>0.09***</td><td>1.00</td><td></td><td></td></tr><tr><td>6 Focal seller friendship links</td><td>13.08</td><td>14.00</td><td>0.29***</td><td>-0.09***</td><td>-0.01</td><td>0.04</td><td>0.03</td><td>1.00</td><td></td></tr><tr><td>7 Focal seller assurance mechanism</td><td>0.71</td><td>0.45</td><td>0.09***</td><td>-0.14***</td><td>0.02</td><td>-0.10***</td><td>0.21***</td><td>0.02</td><td>1.00</td></tr></table>

N = 924.

$$
^ {*} p <   0. 1.
$$

\*\* p b 0.05.

\*\*\* $\begin{array} { r } { p < 0 . 0 1 . } \end{array}$

4.2.2.3. Reputation. After completing a purchase, customers in Taobao would rate the product quality of the online seller. Seller reputation was measured by the ratio of positive ratings.

## 4.2.3. Control variables

Factors that might influence the likelihood of obtaining reciprocity hyperlinks were included as control variables. One control variable was the seller's business tenure (measured by number of months since the seller's online store was established). Established sellers might have more legitimacy in the e-marketplace [68–70]. Thus, it might be beneficial for a new seller to collaborate with an established seller but not the other way round. Another control variable was the numbers of existing friendship links. This reflected the inclination of sellers to exchange hyperlinks and might affect their decisions. Another control variable was whether sellers participated in the consumer rights safeguarding plan (CRSP) that was designed to enhance online trust.<sup>1</sup> Sellers might prefer to exchange hyperlinks with partners that participated in CRSP. Table 1 shows the measurements of all the variables.

## 4.3. Estimation method

The dependent variable was binary in nature. Correspondingly, a logit regression was used for estimation. The outcome variable p was the probability of receiving reciprocal hyperlinks.

$$
\begin{array}{l} \mathrm{p} = \operatorname * {P r} \left(y _ {i j} = 1\right) \\ \mathrm{y} _ {i j} = \left\{ \begin{array}{c c} & 1, \text { if   reciprocal   hyperlink   is   received } \\ & 0, \text { otherwise } \end{array} \right. \end{array}
$$

Because each seller could create multiple friendship links, the dataset was an unbalanced panel data (with the seller as the panel variable and the hyperlink as the time variable). Random effects (RE) model was used because RE parameter estimates could be applied to a random sample of the entire population. Fixed effects (FE) model could not be used because FE parameter estimation required variances in the dependent variable for the same seller. Therefore, if FE model was used, 225 sellers out of the 327 sellers would have to be dropped and the sample size would be too small. Thus, we used RE model with a logit model specification as follows:

$$
\operatorname{logit} (p) = \ln \left(\frac {p}{1 - p}\right) = \alpha_ {i} + x _ {i j} \beta + \varepsilon_ {i j}, \alpha_ {i} \sim I I D (\alpha , \sigma^ {2}),
$$

where $x _ { i j }$ was the vector of independent variables and $\alpha _ { \mathrm { i } }$ was a random variable distributed independently of the regressors. The model was estimated through a maximum likelihood procedure [71].

## 5. Data analyses

We analysed two situations in this study. In the first situation, focal sellers initiated hyperlinks to link sellers (focal seller → link seller) and it would be up to link sellers to decide whether to follow up with reciprocal hyperlinks. In the second situation, focal sellers received hyperlink invitations from link sellers (link seller → focal seller) and it would be up to focal sellers to decide whether to follow up with reciprocal hyperlinks. Tables 2 and 3 summarize the descriptive statistics for the two situations and show the Pearson correlation coefficients between the variables. Market commonality, geographical distance, and seller reputation were significantly correlated to the dependent variable. Multicollinearity was not an issue because the maximum variance inflation factor was 1.06 and 1.02 for apparel sellers initiating and receiving hyperlinks respectively, far below the threshold of 10 [72].

A hierarchical regression procedure was used to test the hypotheses. The variables were mean-centered [73]. Models 1 to 5 in Table 4 present the regression results for the situation where focal sellers first sent hyperlink invitations to link sellers. Market commonality and geographical distance had negative main effects on the likelihood of obtaining reciprocal hyperlinks (see Model 1), thus supporting H1 and H2. Market commonality and geographical distance had a positive interaction on the likelihood of obtaining reciprocal hyperlinks (Model 2). The results suggested that market commonality and geographical distance weakened the negative effects of each other, thus supporting H3. Market commonality and seller reputation had a negative interaction on the likelihood of obtaining reciprocal hyperlinks (Model 3). The results suggested that seller reputation strengthened the negative effects of market commonality, thus supporting H4. Geographical distance and seller reputation had no interaction on the likelihood of obtaining reciprocal hyperlinks (Model 4). The results suggested that seller reputation did not change the negative effects of geographical distance, thus rejecting H5. These results remained robust when all the interaction terms were examined together (Model 5). Models 6 to 10 in Table 4 present the regression results for the situation where focal sellers first received hyperlink invitations from link sellers. The results were consistent with those in Models 1 to 5, thereby providing further evidence of robustness of these results.

Table 3  
Descriptive statistics and Pearson correlation matrix for apparel industry (link seller → focal seller).

<table><tr><td>Variable</td><td>Mean</td><td>S.D.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>1 Reciprocal link</td><td>0.31</td><td>0.46</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2 Market commonality</td><td>0.13</td><td>0.25</td><td>-0.08**</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3 Geographical distance</td><td>1.07</td><td>1.09</td><td>-0.12***</td><td>-0.04</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>4 Link seller reputation</td><td>0.99</td><td>0.01</td><td>0.07**</td><td>-0.03</td><td>-0.03</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>5 Link seller tenure</td><td>14.36</td><td>15.45</td><td>0.02</td><td>-0.07*</td><td>-0.01</td><td>-0.01</td><td>1.00</td><td></td><td></td></tr><tr><td>6 Link seller friendship links</td><td>19.27</td><td>23.38</td><td>-0.11***</td><td>-0.02</td><td>-0.11***</td><td>0.03</td><td>-0.11***</td><td>1.00</td><td></td></tr><tr><td>7 Link seller assurance mechanism</td><td>0.62</td><td>0.49</td><td>0.08*</td><td>-0.10**</td><td>-0.02</td><td>-0.01</td><td>0.07**</td><td>0.01</td><td>1.00</td></tr></table>

N = 701.  
⁎ p b 0.1.  
\*\* p b 0.05.  
⁎⁎⁎ p b 0.01.

## 6. Discussion and implications

## 6.1. Discussion of results

This study examines the effects of two market conditions (market commonality and geographic distance) as well as the moderating effects of seller reputation on hyperlink exchange between sellers in an e-marketplace. The results that support H1 suggest that two sellers are more likely to exchange hyperlinks if they have low market overlaps. In emarketplaces, customers can shop from sellers with low switching costs [29]. Thus, market commonality creates substantial competitive tension for alliance partners and online sellers who rely on the same customer resources are likely to become direct competitors. However, the results that support H3 and H4 delineate the theoretical boundaries of the effects of market commonality. In particular, the results that support H3 show that market commonality has a positive effect on two sellers exchanging hyperlinks if they are located far away from each other (see Fig. 1), and the results that support H4 show that market commonality has a positive effect on two sellers exchanging hyperlinks if the seller initiating the hyperlink has poor reputation (see Fig. 2). Consistent with past findings on firm alliances [19,40], these results demonstrate that long distance between partners or poor partner reputation can reduce competition in high commonality situations because sellers have a better chance of attracting the customers of their partners.

The results that support H2 suggest that two sellers are more likely to exchange hyperlinks if they are geographically close to each other. In e-marketplaces, collaborating with nearby partners allow sellers to offer customers lower shipping costs and shorter delivery schedule for their purchases from partner sellers collectively [63,64]. However, the results that support H3 show the theoretical boundaries of the effects of geographic distance. Specifically, geographic distance has a positive effect on two sellers exchanging hyperlinks if they have high market overlap (see Fig. 3). The results that reject H5 show that the effects of geographic distance are not moderated by seller reputation. Even though high reputation of prospective partners can reduce the costs and risk of sellers collaborating with these prospective partners, such reputation information may have a weak influence [74] considering that the e-marketplace allows sellers to gather reasonably accurate information about prospective partners located anywhere (nearby or far away).

Table 4 Regression results.

<table><tr><td rowspan="2"></td><td colspan="4">Focal seller → Link seller</td><td colspan="6">Link seller → Focal seller</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td></tr><tr><td>Market commonality</td><td>-0.966**(-2.31)</td><td>-0.890**(-2.10)</td><td>-0.844**(-2.00)</td><td>-0.965**(-2.30)</td><td>-0.767*(-1.79)</td><td>-1.210**(-2.39)</td><td>-0.990*(-1.94)</td><td>-1.290**(-2.49)</td><td>-1.206**(-2.38)</td><td>-1.116**(-2.15)</td></tr><tr><td>Geographical distance</td><td>-0.183**(-2.11)</td><td>-0.183**(-2.11)</td><td>-0.183**(-2.13)</td><td>-0.203**(-2.18)</td><td>-0.201**(-2.17)</td><td>-0.457***(-4.02)</td><td>-0.428***(-3.71)</td><td>-0.455***(-4.02)</td><td>-0.453***(-3.94)</td><td>-0.428***(-3.71)</td></tr><tr><td>Seller reputation</td><td>28.37**(2.22)</td><td>28.66**(2.22)</td><td>26.38**(2.09)</td><td>31.29**(2.26)</td><td>28.92**(2.09)</td><td>36.79*(1.72)</td><td>36.32*(1.69)</td><td>35.07(1.61)</td><td>37.13*(1.74)</td><td>36.38*(1.66)</td></tr><tr><td>Market commonality*</td><td></td><td>0.684**(2.17)</td><td></td><td></td><td>0.666**(2.12)</td><td></td><td>0.912*(1.81)</td><td></td><td></td><td>0.888*(1.76)</td></tr><tr><td>Geographical distance</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Market commonality*</td><td></td><td></td><td>-77.83*(-1.87)</td><td></td><td>-76.50*(-1.79)</td><td></td><td></td><td>-174.3**(-2.08)</td><td></td><td>-165.0**(-2.03)</td></tr><tr><td>Seller reputation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Geographical distance*</td><td></td><td></td><td></td><td>6.716(0.60)</td><td>5.843(0.52)</td><td></td><td></td><td></td><td>5.135(-0.24)</td><td>0.0752(0.00)</td></tr><tr><td>Seller reputation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Seller tenure</td><td>-0.0104(-1.28)</td><td>-0.0112(-1.37)</td><td>-0.0105(-1.31)</td><td>-0.0104(-1.28)</td><td>-0.0113(-1.40)</td><td>-0.0020(-0.28)</td><td>-0.0021(-0.29)</td><td>-0.0018(-0.25)</td><td>-0.00200(-0.28)</td><td>-0.00192(-0.27)</td></tr><tr><td>Seller friendship links</td><td>0.0500***(7.13)</td><td>0.0503***(7.14)</td><td>0.0498***(7.14)</td><td>0.0501***(7.14)</td><td>0.0502***(7.15)</td><td>-0.0028(-0.28)</td><td>-0.0021(-0.21)</td><td>-0.0031(-0.31)</td><td>-0.00274(-0.27)</td><td>-0.00255(-0.25)</td></tr><tr><td>Seller assurance mechanism</td><td>0.699**(2.32)</td><td>0.704**(2.32)</td><td>0.720**(2.42)</td><td>0.704**(2.34)</td><td>0.726**(2.43)</td><td>0.288(1.24)</td><td>0.304(1.30)</td><td>0.296(1.28)</td><td>0.287(1.23)</td><td>0.309(1.32)</td></tr><tr><td>Intercept</td><td>-2.265***(-7.63)</td><td>-2.274***(-7.62)</td><td>-2.267***(-7.73)</td><td>-2.283***(-7.64)</td><td>-2.287***(-7.70)</td><td>-0.720***(-2.63)</td><td>-0.721***(-2.62)</td><td>-0.740***(-2.71)</td><td>-0.720**(-2.63)</td><td>-0.738**(-2.68)</td></tr><tr><td>N</td><td>924</td><td>924</td><td>924</td><td>924</td><td>924</td><td>701</td><td>701</td><td>701</td><td>701</td><td>701</td></tr><tr><td>Log likelihood</td><td>-454.84</td><td>-452.56</td><td>-453.16</td><td>-454.65</td><td>-450.86</td><td>-381.12</td><td>-379.57</td><td>-379.11</td><td>-381.09</td><td>-377.60</td></tr></table>

t statistics in parentheses.  
⁎ p b 0.1.  
⁎⁎⁎ p b 0.01.  
\*\* p b 0.05.

![](/api/attachments/T65NB578/fulltext/images/4bb687b0524cff50c040d77c8cc54702922f5986675261dbd23a21ece2c860c3.jpg)  
Fig. 1. Geographic distance moderating the effects of market commonality

## 6.2. Theoretical implications

Prior studies have explained the outcomes of hyperlink exchanges among sellers [10,14,17] but these studies have not provided theoretically-grounded explanations for the factors (or combination of factors) that lead to hyperlink exchanges. Because hyperlink exchanges are critical for the sustainability of the community of sellers in e-marketplaces [10], it is important to understand the factors that promote or hinder such alliances among sellers. In this regard, this study goes beyond past studies by examining the antecedents of hyperlink exchanges among sellers in e-marketplaces.

This study investigates alliance formation outside the traditional bricks-and-mortar context. The results re-assess the generalizability of theories (such as resource-based view and transaction-cost rationale) in the e-marketplace context. Extending past findings about the effects of market commonality on alliance formation in the traditional brickand-mortar context [22,40,43], this study re-examines these effects of market commonality in the e-marketplace context and show that the effects arising from market commonality can be moderated by geographic distance and seller reputation. While past studies have discussed the paradox due to geographic distance [46–49] and suggest that geographic distance may be less important in e-marketplaces [53], this study shows that geographic distance still affects the decision of sellers in e-marketplaces in terms of whether they should exchange hyperlinks with prospective partners. Past studies on strategy argue that geographic distance undermines collaboration [40,43]; our study demonstrates that geographic distance can facilitate collaboration in the context of e-marketplaces.

The moderating effects uncovered in this study enrich our theoretical understanding about how sellers make decisions on the exchange of hyperlinks in the e-marketplace context. The negative effects of market commonality can become positive effects when partners are located far away from each other or when the seller initiating the hyperlink has poor reputation. In these conditions, the drawbacks of collaboration (i.e., direct competition) are lessened while the benefits of collaboration (i.e., enlarged customer base) are heightened. Similarly, the negative effects of geographical distance can become positive effects when partners have high market overlaps. In this situation, collaboration barriers arising from coordination and monitoring costs are reduced.

![](/api/attachments/T65NB578/fulltext/images/3050ed5dc654c3b4cb9b478c973cb603c4f9997fc640b1443b3e05760aa508fb.jpg)  
..... low reputation - - - medium reputation  high reputation  
Fig. 2. Seller reputation moderating the effects of market commonality.

![](/api/attachments/T65NB578/fulltext/images/de5447275ccfeb04ccf24e792e0801a9d913a4ceab5ac0ba13ff136054c8f902.jpg)  
Fig. 3. Market commonality moderating the effects of geographic distance.

## 6.3. Managerial implications

The results of this study have managerial implications for sellers and platform operators in e-marketplaces. In spite of the ubiquity of hyperlinks in e-marketplaces, sellers have little guidance as to how they may benefit from hyperlink exchanges. This study guides sellers in their decisions about when to exchange hyperlinks. Specifically, when sellers are considering prospective partners with high market overlap, they are likely to be better off exchanging hyperlinks with those that are located far away or those with poor reputation. But when sellers are considering prospective partners located far away, they are likely to be better off exchanging hyperlinks with those that they have high market overlap. For sellers with weak reputation (e.g., new sellers) that have a greater need for customer resources [18], they are more likely to succeed in exchanging hyperlinks with partners with high market overlap.

Sellers in e-marketplaces often have difficulty in differentiating their products [75] but they have more opportunities to cooperate in the dynamic environment [45]. Because online sellers must collaborate for survival, this study offers guidance to sellers for their decisions on when to collaborate. Specifically, market conditions (e.g., market commonality and geographical distance) as well as partner characteristics (e.g., reputation) should factor into such decisions. The results of this study offer insights into the trade-off that occurs when different combinations of market conditions and partner characteristics come into the decision process. The payoff in making the right trade-off can be significant for the numerous sellers in e-marketplaces.

Platform operators can also leverage on the results of this study to improve collaboration among numerous sellers. For example, there are many seller associations on Taobao and some are organized by geography (e.g., Association of Shanghai Sellers). At present, the key activities of such seller associations are limited to sharing experience among members. Given that it can be beneficial for sellers located near each other to collaborate under some conditions, the platform operator can encourage collaboration among relevant members of such seller associations based on the results of this study. Other seller associations on Taobao are organized by industry (e.g., Association of Apparel Sellers). Again, the key activities of such seller associations are limited to sharing experience among members. Given that it can be beneficial for sellers with high market overlap to collaborate under some conditions, the platform operator can also encourage collaboration among relevant members of such seller associations based on the results of this study. Eventually, mutually productive collaboration is instrumental for the survival of seller population as a whole in e-marketplaces.

## 6.4. Limitations and future research

This study has several limitations. First, the measurement of market commonality is limited in accuracy. Market commonality is based on product type as classified by Taobao. The dataset only has the first two major product categories of each seller. In practice, sellers may be involved in more than two major product categories. Also, information on the percentage of sales for each seller in each product category is not available. Future research leveraging on a dataset with more detailed information on product categories can test the robustness of the findings in this study.

Second, future studies can investigate other forms of alliance which incur higher switching costs than exchanging hyperlinks. Such forms of alliance include sellers involved in jointly sourcing and inventory sharing. Also, sellers in e-marketplaces can customize and personalize their products and service offerings, thereby increasing switching costs for customers [6]. Higher switching costs may then affect the decisions of sellers on hyperlink exchange and alliance formation [76]. More research is needed on these topics.

Third, e-marketplace alliances are loose and easy to break if all partners do not benefit equally [28]. This study is confined to alliances that offer positive reciprocity (i.e., how sellers enter into collaboration). Future research can examine when and how sellers may end their collaboration (e.g., removing existing hyperlinks with partners).

## 7. Conclusion

Many sellers in e-marketplaces are small businesses [1–3]. The selection of alliance partners is a strategic decision for these sellers because they often lack resources and struggle to survive in a competitive environment [4]. Hyperlink exchange is an IT-enabled means of alliance formation. Although hyperlinks are ubiquitous on emarketplaces, past studies have rarely offered guidance to sellers about when they should exchange hyperlinks so as to raise their performance in e-marketplaces [10,14,17]. Going beyond past studies, this study extends our theoretical understanding in this area and offers guidance to sellers in terms of when they should or should not exchange hyperlinks in different situations. As e-marketplaces continue to offer more and better IT capabilities, sellers would need guidance about how to leverage these IT capabilities to improve their performance. Research in the direction of this study can help to address such issues and benefit the numerous sellers in e-marketplaces.

## Acknowledgement

This study was partially supported by the National Natural Science Foundation of China (71371056, 71490721, and 71571155) and China Scholarship Council (Youwei Wang). The work was also supported by grants from City University of Hong Kong (CityU 7004564) (Yulin Fang).

## References

[1] S. Bandyopadhyay, S. Bandyopadhyay, Estimating time required to reach bid levels in online auctions, J. Manag. Inf. Syst. 26 (3) (2010) 275–301.

[2] Z. Qu, Y. Wang, S. Wang, Y. Zhang, Implications of online social activities for e-tailers' business performance, Eur. J. Mark. 47 (8) (2013) 1190–1212

[3] X. Wu, R. Ma, Y. Shi, How do latecomer firms capture value from disruptive technologies? A secondary business-model innovation perspective, IEEE Trans. Eng. Manag. 57 (1) (2010) 51–62.

[4] M.H. Morris, A. Ko ak, A. Zer, Coopetition as a small business strategy: Implications for performance, J. Small Bus. Strateg. 18 (1) (2007) 35–55.

[5] Y. Wang, S. Wang, Y. Fang, P.Y.K. Chau, Store survival in online marketplace: an empirical investigation, Decis. Support. Syst. 56 (1) (2013) 482–493.

[6] N.K. Park, J.M. Mezias, J. Song, A resource-based view of strategic alliances and firm value in the electronic marketplace, J. Manag. 30 (1) (2004) 7–27.

[7] Z. Katona, M. Sarvary, Network formation and the structure of the commercial world wide web. Mark, Sci. 27 (5) (2008) 764–778.

[8] C. Dellarocas, Z. Katona, W.M. Rand, Media, aggregators and the link economy: strategic hyperlink formation in content networks, Manag. Sci. 59 (10) (2010) 2360–2379.

[9] H.W. Park, M. Thelwall, Hyperlink analyses of the world wide web: a review, J. Comput.-Mediat. Commun. 8 (4) (2003) 0.

[10] A.T. Stephen, O. Toubia, Deriving value from social commerce networks, J. Mark. Res. 47 (2) (2010) 215–228.

[11] L. Vaughan, Web hyperlinks reflect business performance: a study of US and Chinese IT companies, Can. J. Inf. Libr. Sci. 28 (1) (2004) 17 31.

[12] P. Evans, T.S. Wurster, Getting real about virtual commerce, Harv. Bus. Rev. 77 (1999) 84–98.

[13] P.B. Lowry, A. Vance, G. Moody, B. Beckman, A. Read, Explaining and predicting the impact of branding alliances and web site quality on initial consumer trust of e-commerce web sites, J. Manag. Inf. Syst. 24 (4) (2008) 199–224.

[14] K.J. Stewart, How hypertext links influence consumer perceptions to build and degrade trust online, J. Manag. Inf. Syst. 23 (1) (2006) 183–210.

[15] R.K. Srivastava, L. Fahey, H.K. Christensen, The resource-based view and marketing: the role of market-based assets in gaining competitive advantage, J. Manag. 27 (6) (2001) 777–802.

[16] M. Thelwall, T.A. Sheldon, Exploring the link structure of the web with network diagrams, J. Inf. Sci. 27 (6) (2001) 393–401.

[17] D. Mayzlin, H. Yoganarasimhan, Link to success: how blogs build an audience by promoting rivals, Manag. Sci. 58 (9) (2012) 1651–1668.

[18] Z.J. Lin, H. Yang, B. Arya, Alliance partners and firm performance: resource complementarity and status association, Strateg. Manag. J. 30 (9) (2009) 921–940.

[19] T. Das, B.S. Teng, Partner analysis and alliance performance, Scand. J. Manag. 19 (3) (2003) 279-308

[20] T.K. Das, B.S. Teng, A resource-based theory of strategic alliances, J. Manag. 26 (1) (2000) 31–61.

[21] J. Barney, Firm resources and sustained competitive advantage, J. Manag. 17 (1) (1991) 99–120.

[22] F.T. Rothaermel, W. Boeker, Old technology meets new technology: complementarities, similarities, and alliance formation, Strateg. Manag. J. 29 (2008) 47–77.

[23] O.E. Williamson, Comparative economic organization: the analysis of discrete structural alternatives Adm, Sci, O. (1991) 269–296

[24] J.G. Combs, David J. Ketchen, Explaining interfirm cooperation and performance: toward a reconciliation of predictions from the resource-based view and organization. al economics Strateg, Manag. L. 20 (9) (1999) 867–888

[25] K.M. Eisenhardt, C.B. Schoonhoven, Resource-based view of strategic alliance formation: strategic and social effects in entrepreneurial firms, Organ. Sci. 7 (2) (1996) 136 150.

[26] H. Yasuda, Formation of strategic alliances in high-technology industries: comparative study of the resource-based theory and the transaction-cost theory, Technovation 25 (7) (2005) 763–770.

[27] T. Boyles, Small business and Web 2.0: hope or hype? Entrep. Exec. 16 (2011).

[28] P. Chatterjee, Interfirm alliances in online retailing, J. Bus. Res. 57 (7) (2004) 714–723.

[29] S. Burt, L. Sparks, E-commerce and the retail process: a review, J. Retail. Consum. Serv. 10 (5) (2003) 275–286.

[30] Y. Luo, Coopetition in International Business, Copenhagen Business School Press, Copenhagen, 2004.

[31] D. Houser, J. Wooders, Reputation in auctions: theory, and evidence from eBay, J. Econ. Manag. Strateg. 15 (2) (2006) 353–369.

[32] M.I. Melnik, J. Alm, Does a seller's ecommerce reputation matter? Evidence from ebay auctions, J. Ind. Econ. 50 (3) (2002) 337–349.

[33] A.V. Shipilov, S.X. Li, H.R. Greve, The prince and the pauper: search and brokerage in the initiation of status-heterophilous ties, Organ. Sci. 22 (6) (2011) 1418–1434.

[34] G.U. Qian, L.U. Xiaohui, Unraveling the mechanisms of reputation and alliance formation: a study of venture capital syndication in China, Strateg. Manag. J. 35 (5) (2014) 739-750.

[35] B.A. Aubert, S. Rivard, M. Patry, A transaction cost approach to outsourcing behavior: some empirical evidence, Inf. Manag. 30 (2) (1996) 51–64.

[36] Y. Benslimane, M. Plaisent, P. Bernard, Investigating search costs and coordination costs in electronic markets: a transaction costs economics perspective, Electron. Mark. 15 (3) (2005) 213–224.

[37] S. Standing, C. Standing, P.E.D. Love, A review of research on e-marketplaces 1997– 2008, Decis. Support. Syst. 49 (1) (2010) 41–51.

[38] E.W. Tsang, Motives for strategic alliance: a resource-based perspective, Scand. J. Manag. 14 (3) (1998) 207–221.

[39] M.-J. Chen, Competitor analysis and interfirm rivalry: toward a theoretical integration, Acad. Manag. Rev. 21 (1) (1996) 100–134.

[40] H. Mitsuhashi, H.R. Greve, A matching theory of alliance formation and organizational success: complementarity and compatibility, Acad. Manag. J. 52 (5) (2009) 975–995.

[41] T.E. Stuart, Interorganizational alliances and the performance of firms: a study of growth and innovation rates in a high-technology industry, Strateg. Manag. J. 21 (8) (2000) 791–811.

[42] A. Capaldo, A.M. Petruzzelli, Partner geographic and organizational proximity and the innovative performance of knowledge-creating alliances, Eur. Manag. Rev. 11 (1) (2014) 63–84.

[43] S.A. Chung, H. Singh, K. Lee, Complementarity, status similarity and social capital as drivers of alliance formation, Strateg. Manag. J. 21 (1) (2000) 1–22.

[44] R.D. Ireland, M.A. Hitt, D. Vaidyanath, Alliance management as a source of competitive advantage, J. Manag. 28 (3) (2002) 413–446.

[45] L. Wang, E.J. Zajac, Alliance or acquisition? A dyadic perspective on interfirm resource combinations, Strateg. Manag. J. 28 (13) (2007) 1291–1317.

[46] A.P.R. Ragozzino, The effects of geographic distance on the foreign acquisition activity of US firms, Manag. Int. Rev. 49 (4) (2009) 509–535.

[47] A. Zaheer, E. Hernandez, The geographic scope of the MNC and its alliance portfolio: resolving the paradox of distance, Glob. Strateg. J. 1 (1–2) (2011) 109–126.

[48] C. Felzensztein, L. Huemer, E. Gimmon, The effects of co-location on marketing externalities in the salmon-farming industry, J. Bus. Ind. Mark. 25 (1) (2009) 73–82.

[49] C. Geldes, C. Felzensztein, E. Turkina, A. Durand, How does proximity affect interfirm marketing cooperation? A study of an agribusiness cluster, J. Bus. Res. 68 (2) (2015) 263-272.

[50] P.M. Rosenzweig, I.V. Singh, Organizational environments and the multinational enterprise, Acad. Manag. Rev. 16 (2) (1991) 340–361.

[51] O. Sorenson, T.E. Stuart, Syndication networks and the spatial distribution of venture capital investments, Am. J. Sociol. 106 (6) (2001) 1546–1588.

[52] H. Kranenburg, J. Hagedoorn, S. Lorenz-Orlean, Distance costs and the degree of inter-partner involvement in international relational-based technology alliances, Glob, Strateg, I. 4 (4)(2014) 280–291.

[53] F. Cairncross, The Death of Distance: How the Communications Revolution is Changing Our Lives, Harvard Business Press, 2001.

[54] S.S. Standifird, Reputation and e-commerce: eBay auctions and the asymmetrical impact of positive and negative ratings, J. Manag. 27 (3) (2001) 279–295.

[55] M. Washington, E.J. Zajac, Status evolution and competition: theory and evidence, Acad Manag L 48 (2) (2005) 282-296

[56] I. Stern, J.M. Dukerich, E. Zajac, Unmixed signals: how reputation and status affect alliance formation, Strateg. Manag. J. 35 (4) (2014) 512–531.

[57] S.M. Wagner, L.S. Coley, E. Lindemann, Effects of suppliers' reputation on the future of buyer - supplier relationships: the mediating roles of outcome fairness and trust, J. Supply Chain Manag. 47 (2) (2011) 29–48.

[58] A. Zaheer, B. Mcevily, V. Perrone, Does trust matter? Exploring the effects of interorganizational and interpersonal trust on performance, Organ. Sci. 9 (2) (1998) 141–159.

[59] Y. Bakos, C. Dellarocas, Cooperation Without Enforcement? A Comparative Analysis of Litigation and Online Reputation as Ouality Assurance Mechanisms, 57, Social Science Electronic Publishing, 2002 127–142 (11)

[60] P. Ingram, L.Q. Yue, Structure, affect and identity as bases of organizational competition and cooperation, Acad, Manag, Ann, 2 (1) (2008) 275–303.

[61] T.K. Das, B.S. Teng, The dynamics of alliance conditions in the alliance development process, J. Manag. Stud. 39 (5) (2002) 725–746.

[62] J. Knoben, L.A. Oerlemans, Proximity and inter-organizational collaboration: a literature review, Int. J. Manag. Rev. 8 (2) (2006) 71–89.

[63] M.J. Eppli, J.D. Benjamin, The evolution of shopping center research: a review and analysis, J. Real Estate Res. 9 (1) (1994) 5–32.

[64] A. Hortacsu, F.A. Martinez-Jerez, J. Douglas, The Geography of Trade on eBay and MercadoLibre, NET Institute Working Paper No. 06–09Available at SSRN http:// ssrn.com/abstract=939327 2006.

[65] D. Mukherjee, A.S. Gaur, S.S. Gaur, F. Schmid, External and internal influences on R&D alliance formation: evidence from German SMEs, J. Bus. Res. 66 (11) (2013) 2178–2185.

[66] A. Parkhe, Strategic alliance structuring: a game theoretic and transaction cost examination of interfirm cooperation, Acad. Manag. J. 36 (4) (1993) 794–829.

[67] G. Ahuja, The duality of collaboration: inducements and opportunities in the formation of interfirm linkages, Strateg. Manag. J. 21 (3) (2000) 317–343.

[68] C.E. Eesley, E.B. Roberts, Are you experienced or are you talented?: when does innate talent versus experience explain entrepreneurial performance? Strateg. Entrep. J. 6 (3) (2012) 207–219

[69] J.W. Lu, D. Xu, Growth and survival of international joint ventures: an external-internal legitimacy perspective L. Manag, 32 (3) (2006) 426–448

[70] S. Shane, M.-D. Foo, New firm survival: institutional explanations for new franchisor mortality, Manag. Sci. 45 (2) (1999) 142–159.

[71] A.C. Cameron, P.K. Trivedi, Microeconometrics: Methods and Applications, Cambridge Cambridge University Press, 2005.

[72] D.A. Belsley, E. Kuh, R.E. Welsch, Regression diagnostics, Wiley-Interscience, New York, 1980.

[73] L.S. Aiken, S.G. West, R.R. Reno, Multiple Regression: Testing and Interpreting Interactions, Sage Publications Inc, 1991.

[74] M.A. Fuller, M.A. Serva, J.S. Benamati, Seeing is believing: the transitory in uence of reputation information on e-commerce trust and decision making, Decis. Sci. 38 (4) (2007) 675–699.

[75] K. Uhlenbruck, M.A. Hitt, M. Semadeni, Market value effects of acquisitions involving internet firms: a resource-based analysis, Strateg. Manag. J. 27 (10) (2006) 899–913.

[76] J. Christoffersen, A review of antecedents of international strategic alliance performance: synthesized evidence and new directions for core constructs, Int. J. Manag. Rev. 15 (1) (2013) 66–85.

Zhaoran Xu is a PhD student in Department of Information Management and Information Systems at Fudan University. Her research interests include e-commerce, internet-based service for the elderly and smart city.

Youwei Wang is an Associate Professor in Department of Information Management and Information Systems at Fudan University. His current research interests include e-commerce, mobile business, online social networks, virtual community and business intelli gence. He is serving as senior editor of Electronic Commerce Research and Applications. His research has been published in Decision Support Systems, International Journal of Elec tronic Commerce, European Journal of Marketing, and others.

Yulin Fang is an Associate Professor in Department of Information Systems at the City Uni versity of Hong Kong. He earned his PhD at Richard Ivey School of Business, The University of Western Ontario in Canada. His current research interests include knowledge and innovation management, globally distributed work arrangements, and social media and commerce. He is serving as senior editor of Information Systems Research and Information Systems Journal. His work has appeared in Strategic Management Journal, Journal of Management Studies, Organizational Research Methods, MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Journal of the Association for Information Systems, among others.

Bernard Tan is a Professor in the Department of Information Systems at the National Uni versity of Singapore. He received his Ph.D. degree in information systems from NUS. His current research interests are knowledge management, virtual communities, and information privacy. He has served or is serving on the editorial boards of MIS Quarterly, Management Science, Journal of AIS, Journal of Management Information Systems, IEEE Transactions on Engineering Management, Information and Management, and others.

Hai Sun is an Assistant Professor in Department of Information Management and Information Systems at Fudan University. His current research interests are e-government and mobile business. His research has been published in Computational Intelligence and Neuro science, Journal of Computers, Journal of Software, and others.
