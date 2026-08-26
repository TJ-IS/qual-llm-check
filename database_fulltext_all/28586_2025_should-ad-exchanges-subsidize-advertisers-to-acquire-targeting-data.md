---
otero_id: 28586
otero_key: "2R8G9AJN"
title: "Should Ad Exchanges Subsidize Advertisers to Acquire Targeting Data?"
authors: "Wangsheng Zhu; Shaojie Tang; Vijay Mookerjee"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.0126"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Should Ad Exchanges Subsidize Advertisers to Acquire Targeting Data?

Wangsheng Zhu,<sup>a</sup> Shaojie Tang,<sup>b</sup> Vijay Mookerjee<sup>c,</sup>\*

<sup>a</sup> Department of Information Systems, Business Statistics, and Operations Management, School of Business and Management, Hong Kong University of Science and Technology, Hong Kong; <sup>b</sup> Center for AI Business Innovation, Department of Management Science and Systems, University at Buffalo, Buffalo, New York 14260; <sup>c</sup> Naveen Jindal School of Management, The University of Texas at Dallas, Richardson, Texas 75080

\*Corresponding author

Contact: wangshengzhu@ust.hk, https://orcid.org/0000-0002-4478-659X (WZ); shaojiet@buffalo.edu (ST); vijaym@utdallas.edu https://orcid.org/0000-0001-5583-3585 (VM)

Received: March 2, 2023 Revised: September 18, 2023; May 23, 2024; September 18, 2024 Accepted: October 14, 2024 Published Online in Articles in Advance: November 26, 2024

https://doi.org/10.1287/isre.2023.0126

Copyright: © 2024 INFORMS

Abstract. Large volumes of online impressions are sold daily via real-time auctions to deliver targeted advertisements to consumers. Advertisers use data to learn about user preferences and select the most appropriate ad for each user, which also helps them optimize their bids in an ad auction. Although ad exchanges may provide some user data to advertisers, they are usually limited, and advertisers often acquire data from various sources to improve targeting performance. The acquisition of such data can significantly influence the revenue of the ad exchange, which motivates ad exchanges to take actions that reduce advertisers’ data acquisition costs and encourage them to buy data. Previous studies have examined the impact of ad exchanges revealing their data to advertisers, but little attention has been paid to the impact of ad exchanges subsidizing advertisers to acquire data from third parties. To address this gap, we propose three subsidy frameworks to increase ad exchange revenue by inducing more advertisers to acquire data: all subsidized (AS), winner subsidized (WS), and loser subsidized. Using a stylized model, we analyze the impact of subsidy provisions on the platform’s net revenue. Our results show that WS can be better or worse than AS depending on the cost of data acquisition, its beneficial impact on ad selection, and the distribution of impression values.

History: Martin Bichler, Senior Editor; Khim Yong Goh, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2023.0126.

Keywords: targeted advertising • ad auctions • targeting data acquisition • subsidy frameworks

## 1. Introduction

The digital advertising market experienced a surge of 35% in 2021, reaching \$189 billion, which marked the highest increase since 2006 (IAB 2022). As the digital advertising market grows, real-time bidding (RTB) is becoming increasingly popular for selling advertising impressions (Tunuguntla and Hoban 2021, Christopher et al. 2022). In RTB, an impression is generated when a user visits a website or app, triggering a real-time auction on a platform known as an ad exchange. Advertisers on the ad exchange observe user attributes, predict the potential value of displaying their ads for this user, and customize their bids accordingly. This allows advertisers to bid higher on more valuable impressions and deliver relevant ads for users (Taparia 2020, IAB 2021, Tunuguntla and Hoban 2021). Because of its advantage in advertisement targeting, the RTB market has been growing rapidly in the past years (eMarketer 2019).

Targeted advertising relies on the availability of user data, which allows advertisers to tailor their ads to users (Walter 2021). However, user data provided by ad exchanges may be limited to basic information, such as device type. To supplement this basic information, advertisers may query other third-party databases in real time. In this study, the data collected by the platform are termed “basic data,” whereas the data acquired from third parties are “additional data.” Additional data are acquired from various databases and are often more informative than what is provided by the ad exchange (Sayedi 2018). However, acquiring additional data can be costly, which may limit its use in RTB (Zawadzin´ski and Sweeney 2022).

Several studies (e.g., Golrezaei and Nazerzadeh 2016, Sayedi 2018) have explored the challenges and opportunities of targeted advertising. They suggest that targeting benefits not only advertisers but also, the ad exchange. With better targeting, advertisers have a higher willingness to pay for impressions, which can, in turn, boost the ad exchange’s net revenue in RTB (Sayedi 2018). Hence, ad exchanges may have the incentive to encourage advertisers’ data acquisition. Considering that data costs are a major consideration for advertisers, we explore the potential of ad exchanges to increase net revenue by subsidizing advertisers’ data acquisition. Our study aims to answer the following questions. When is it profitable for an ad exchange to subsidize the data acquisition cost for advertisers? What is the optimal subsidy, if any?

## 1.1. RTB Ecosystem

Table 1 displays the key participants in a typical RTB advertising ecosystem. Data providers play an important role in the ecosystem because basic data are restricted to the information that the focal publisher can gather. In contrast, additional data have cross-site information that captures more behavioral features. Oracle states that a cross-site data management platform “is the backbone of digital marketing, allowing companies to understand their customers better.”<sup>1</sup> Starita (2019) identifies data management platforms as “a key tool to enable more targeted and personalized ad campaigns.” IAB and Ipsos (2022) report that marketers spent \$22.0 billion in 2021 acquiring user data for marketing, which is an increase of 8.37% compared with 2020.

Traditionally, platforms do not participate in the transactions between advertisers and data providers. Nowadays, many platforms have begun to collaborate with data providers to help advertisers acquire additional data more easily. For example, platforms, like Pubmatic, Xandr, and OpenX, have formed partnerships with data providers, like Lotame.<sup>2</sup>

Take Pubmatic as a concrete example. Pubmatic has partnered with various data providers (e.g., Epsilon and Lotame) to offer data packages. One instance is the backto-school package that enables advertisers to target users interested in educational products.<sup>3</sup> If an advertiser purchases the package, then when an ad auction starts, Pubmatic queries its data partners to check if a particular user belongs to the advertiser’s targeting segment. After the ad auction, the advertiser makes payments to Pubmatic, which later transfers a data fee to data providers 4 With these data packages, advertisers can acquire additional data at a reduced cost compared with acquiring it directly from data providers (Pubmatic, Inc. 2021).

In practice, platforms typically form partnerships with data providers rather than buying and reselling data to advertisers. Several factors drive this approach.

Data providers are cautious about selling original data to platforms because of privacy concerns because they need to control its usage and ensure legitimacy (Sluis 2020). Moreover, the data market is technology intensive, with vast amounts of new targeting data generated daily (Zawadzin´ ski and Sweeney 2022). To succeed, data providers must effectively integrate diverse data sources, consistently update data sets, and combine proprietary advertiser data with cross-site data. They must also leverage data analytics to create reliable impression segments. Given the complexity and diversity of technology solutions—often involving advanced optimization and machine learning techniques—simply purchasing external data would not enable a platform to replicate the capabilities of a dedicated data provider.

Figure 1 depicts the operational process of an RTB ecosystem, where the ad exchange partners with data providers. Section EC.1 in the Online Appendix introduces technological details on advertisement targeting. In Figure 1, advertiser 1 purchases targeting data. This creates a data package deal involving the advertiser, the platform, and a data provider. Advertiser 1 creates a set of user segments of interest. For example, a seller of dog-related products may create a segment “dog owners.” The targeting process is as follows. When a user visits a publisher’s website, it generates an impression. The publisher collects the basic data and sends it to the ad exchange. Based on the data package deal, the ad exchange sends the basic data to the relevant data provider, which determines, based on the additional data, whether the user has a high likelihood of owning a dog. The data provider returns this result, and the ad exchange sends the result with basic data to advertiser 1. The advertiser uses this information to select the ad to display and the bid.

It is noteworthy that data providers do not need to share the raw user data with advertisers; they only need to tell advertisers whether the raw data suggest that the user belongs to the advertiser’s target segment. This restricts the use of user data for targeted advertising and protects the privacy of users. Data providers have also developed other privacy-preserving targeting technologies, which are discussed in Section EC.1 in the Online Appendix.

Table 1. Participants in an RTB Ecosystem

<table><tr><td>Participants</td><td>Description</td></tr><tr><td>Users</td><td>Individuals who browse websites where ads are displayed</td></tr><tr><td>Publishers</td><td>Website owners that supply advertising impressions. The publisher whose website is currently being visited is the focal publisher (e.g., publisher 1 in Figure 1).</td></tr><tr><td>Ad exchanges (platforms)</td><td>Marketplaces where ad auctions take place</td></tr><tr><td>Advertisers</td><td>Organizations that bid for impressions</td></tr><tr><td>Data providers</td><td>Firms that integrate additional data from different firms, websites, apps, and social media platforms and offer them for targeting (e.g., Adobe Audience Manager, Oracle BlueKai, Salesforce Audience Studio, Lotame, and Nielsen Marketing Cloud)</td></tr></table>

Figure 1. The RTB Ecosystem Under the Partnership Between the Ad Exchange and Data Providers  
![](/api/attachments/2R8G9AJN/fulltext/images/6e149891556617e23150fb463895aac374ba2d1df9ecadc4da046d5079e79065.jpg)

Unlike advertiser 1, advertiser 2 does not obtain additional data. Instead, the advertiser relies solely on the basic data to discern the user’s interests and determine the bid for this impression. In this study, we call the advertiser that acquires additional data an “informed” advertiser, whereas the advertiser that does not acquire data is referred to as an “uninformed” advertiser. After collecting bids from advertisers, the ad exchange chooses the auction winner and sends the winner’s ad to the publisher. Our focus in this study is the revenue earned by the ad exchange by selling impressions to advertisers. The specifics of how this revenue is shared between the ad exchange and the publisher do not affect our analysis.

## 1.2. Motivation and Research Agenda

Facilitating the acquisition of data by advertisers at a lower cost has gained much popularity among platforms, mainly because of the belief that better targeting increases the impression price. As the literature indicates, without targeting, the advertiser with the highest average impression value wins all impressions, even if this advertiser may not be well suited to some users. Targeting enables platforms to allocate each impression to the advertiser that best aligns with it, improving the fit between the displayed ad and the user. Targeting has a downside as well; it reduces the pool of advertisers interested in each impression and attenuates the competition among advertisers (Chen and Stallaert 2014). When the ad-fit improvement dominates the reduction in the competition, the impression price increases with targeting, which benefits the platform. This is why platforms are willing to help advertisers acquire data for targeting.

Despite the increasing popularity, there is a lack of a good understanding of the key issues related to platforms subsidizing advertisers’ data acquisition costs, including the following. How much subsidy is required to induce advertisers to acquire data? Can the increase in the impression price justify the subsidy? How does the subsidy provision affect the payoff of advertisers? Besides, platforms currently subsidize all data buyers. For example, advertisers that purchase the same data package pay the same data package price to Pubmatic. Thus, they receive the same subsidy from Pubmatic, which equals the extra data cost that they need to incur when they acquire data directly from the data provider. Because data acquisition primarily affects the platform’s revenue through its impact on the auction outcomes, we also ask the following question. Could a platform’s revenue be better off by selectively subsidizing advertisers based on the auction outcome?

To begin with, we analyze the case where a platform subsidizes all data buyers. This subsidy strategy is called an all-subsidized (AS) framework. Such a framework captures the current practice in that whether an advertiser receives a subsidy from the platform only depends on whether it has purchased data and has no relation to the auction outcome. We first model how data acquisition affects each advertiser’s behaviors (i.e., individual-level impact of data acquisition) and then use this model to analyze how the change in the advertiser’s behaviors affects the final auction outcome (i.e., auction-level impact of data acquisition). Table 2 summarizes the effects at these two levels. Our findings suggest that for the decision on subsidy provision, the key trade-offs faced by the platform are the net ad-fit effect and competitive effect.

After gaining insights into the optimal subsidy under AS, we consider the frameworks where the platform offers subsidies depending on the auction outcomes. Two new frameworks are proposed: loser subsidized (LS), where a data buyer receives a subsidy only when it loses in the auction, and winner subsidized (WS), where a data buyer receives a subsidy only when it wins in the auction. We evaluate the platform’s net revenue under these frameworks and compare it with the AS framework.

Table 2. Impact of Data Acquisition

<table><tr><td>Impact</td><td>Explanation</td></tr><tr><td>Individual-level impact</td><td></td></tr><tr><td>Ad selection effect</td><td>Advertisers select different ads for different users instead of choosing the ad with the highest expected value for all users. Advertising returns from all possible users weakly increase with better ad selection, so the average advertising return rises.</td></tr><tr><td>Bid selection effect</td><td>Advertisers bid based on the accurate return for advertising to each user instead of bidding the average return across all users. Bid selection allows advertisers to bid high (low) on more (less) valuable users. The average advertising return does not change with accurate bid selection.</td></tr><tr><td>Auction-level impact</td><td></td></tr><tr><td>Net ad-fit effect</td><td>The improvement in the fit between the displayed ad and the user net of the data acquisition cost incurred by advertisers and platforms.</td></tr><tr><td>Competitive effect</td><td>Change in the competition intensity for the impression. After targeting, some advertisers become more interested in the impression, whereas others become less interested; thus, the competition can be either attenuated or intensified.</td></tr></table>

Finally, we examine a set of extensions of our model. These extensions include the heterogeneity of advertisers’ abilities to do targeting, the shift from the secondprice auction (SPA) to the first-price auction (FPA), and the quality variation in additional data. These extensions allow us to verify the robustness of our findings under different realistic settings.

## 1.3. Main Findings and Contribution

First, we find that the platform may benefit from subsidy provisions under AS but only when the data cost is neither high nor low. If the data cost is high, such that no one acquires data without subsidies (no natural data buyer), subsidizing advertisers does not benefit the platform. The reason is as follows. Although targeting increases the fit between the displayed ad and the user, our analysis shows that such an increase is less than the data acquisition costs incurred by new data buyers after subsidy provision. This implies a negative net ad-fit effect. Therefore, a platform can benefit from subsidy provision only when it leads to a positive competitive effect. When no one acquires data without subsidies, advertisers are equally interested in all impressions, leading to extremely fierce competition. In this case, the provision of subsidies can only reduce competition. Therefore, the platform cannot benefit from it.

Because the net ad-fit effect is negative, whether a platform benefits from subsidy provision depends on how much the competition can be intensified. A further analysis shows that after subsidy provision, competition intensification mainly happens on natural data buyers. Advertisers that do not purchase data after subsidy provision may face reduced competition and be better off.

Second, our results indicate that the optimal subsidy does not monotonically change with the ad selection effect. As the ad selection effect increases, the optimal strategy repetitively changes between providing and not providing the subsidy. Better ad selection increases the fit between the winner’s ad and the user, diminish ing the net ad-fit effect. The impact of ad selection improvement on the competitive effect is twofold. On the one hand, it raises the expected bids from advertisers that lose the auction, making the winning advertiser pay more for the impression and indicating a larger positive competitive effect. On the other hand, a larger ad selection improvement makes more advertisers acquire data naturally, leading to higher competition intensity before subsidy provision. This diminishes the room to intensify competition after subsidy provision. Therefore, ad selection improvement can either amplify or alleviate the competitive effect. These effects jointly lead to the nonmonotonic relationship between the ad selection effect and the optimal subsidy.

Third, we find that the subsidy under LS leads to a decrease in informed advertisers’ bids, which reduces competition intensity. Thus, the LS framework may not be desirable for platforms. On the contrary, the subsidy in WS positively influences the bids of informed advertisers, resulting in an increase in the impression price. However, despite offering a larger subsidy, the platform may not be able to incentivize all advertisers to acquire data under WS, whereas the platform can ensure that all advertisers acquire data under AS. Considering the distinct advantages and disadvantages of WS and AS, we compare the performances of these two frameworks. We demonstrate that the relative performance of these two frameworks depends on factors, such as the distribution of impression values and the extent of ad selection improvements.

Another factor related to the performance of WS is the heterogeneity of advertisers’ targeting abilities. In practice, some advertisers lack the analytical tools required to analyze user data and optimize their marketing campaigns (Hendricks 2017, Schoen 2021), thus falling under the category of traditional advertisers. Those with targeting ability are referred to as sophisticated advertisers. We find that the presence of traditional advertisers mitigates the competition attenuation, allowing the platform to achieve intense competition under AS. This reduces the advantage of WS as there is little room for competition intensity to increase further. Consequently, AS emerges (weakly) superior to WS in this case.

Fourth, we analyze the impact of subsidy provisions under FPA. The revenue equivalence theorem suggests that SPA and FPA have the same performance in many cases. We find that after the provision of subsidies, the revenue equivalence theorem still holds in most cases. However, we also find cases wherein FPA with subsidies leads to a lower net revenue than SPA with subsidies. The difference in data acquisition decisions breaks the symmetry between advertisers, and the revenue equivalence theorem does not hold. This suggests a possible risk associated with the shift to FPA when advertisers can decide to acquire data on their own.

To the best of our knowledge, this study is among the first theoretical investigations into the impact of platforms subsidizing advertisers’ costs of acquiring data from third-party providers. Previous studies typically focus on scenarios where the platform owns the data, omitting data acquisition costs from their models. They analyze the question of whether a platform should release the basic data to advertisers. Thus, they use the scenario where the platform does not release the data (i.e., no advertiser obtains data) as the baseline case. Under such a context, prior studies highlighted the impact of targeting as a positive ad-fit effect and a negative competitive effect. In contrast, our model includes a data acquisition cost per data buyer. Besides, because there are natural data buyers before the platform participates in the data acquisition process, our baseline is the model with only natural data buyers. Because of these differences, we find a negative net ad-fit effect and a competitive effect that can be either positive or negative.

This study also makes a theoretical contribution to the online advertising literature by developing an economic model where targeting is captured as a combination of ad selection and bid selection, whereas prior studies primarily model targeting as a bid selection process. Our results suggest that a platform may make suboptimal decisions on subsidy provisions if it overlooks the ad selection effect when estimating the impact of data acquisition. Although we focus on subsidies, the implications of our findings can extend to other critical managerial issues in real-time bidding. For example, prior research suggests that data decrease impression prices when only two advertisers are present, leading to the recommendation that platforms should not release basic data to advertisers (Chen and

Stallaert 2014). However, we find that data can still increase impression prices in this scenario when ad selection is significant.

## 2. Related Literature

Our research contributes to the literature on the impact of targeting on the net revenue of advertising platforms. For instance, Levin and Milgrom (2010) suggest that internet advertising platforms must balance the benefits and drawbacks of targeting as it can enhance ad-impression matching but also result in thinner markets that harm the platform. Since then, several studies (Table 3) have explored the relationship between targeting and net revenue under various conditions. So far, researchers have analyzed (1) the impact of targeting on the auction’s clearing price (e.g., Ganuza and Penalva 2010), (2) which advertisers the platform should share data with (e.g., Golrezaei and Nazerzadeh 2016), and (3) what features a platform should release and at which accuracy level (e.g., Sun et al. 2016, Rafieian and Yoganarasimhan 2021).

Our study departs from prior work in three notable ways. First, prior studies mainly focus on optimal strategy regarding the disclosure of basic data and do not investigate the platform’s incentive to help advertisers acquire additional data from third parties. Our study fills this gap by exploring the platform’s incentive to subsidize advertisers for the acquisition of additional data and the most effective subsidy framework.

Second, previous studies have not analyzed the impact of ad selection under targeted advertising. Although Sun et al. (2016) developed a model of the ad selection process, they did not assess the economic consequences of fine-grained ad selection on the platform’s net revenue. By contrast, our study investigates how the platform’s net revenue is affected by improvements in ad selection. Third, prior studies have not examined the role of traditional advertisers in relation to the impact of targeting in RTB. Amaldoss et al. (2016) considered the cost of advertisers to customize bids for each keyword in sponsored search advertising but assumed that advertisers would not participate in keyword auctions if they could not afford the cost. In contrast, our work investigates a scenario in which sophisticated and traditional advertisers coexist in auctions.

Our study loosely relates to the mechanism design literature. Prior studies in this area propose new auction formats that maximize auctioneers’ profits when bidders can obtain data to update their valuations for the item (e.g., Ye 2007, Shi 2012, Golrezaei and Nazerzadeh 2016). In contrast, we focus on the economic impact of the subsidy provision on the platform’s net revenue and the intuition behind it. Additionally, prior studies typically assume either that data acquisition is required to participate in the auction or that data access is controlled by the auctioneer, which differs from our context.

Table 3. Related Literature on Targeting and Data Acquisition

<table><tr><td>Literature</td><td>Research problem</td><td>Decision variable</td><td>Key findings</td></tr><tr><td>Levin and Milgrom (2010)</td><td>How does targeting affect different stakeholders&#x27; payoffs?</td><td>Nondisclosure vs. disclosure of basic data</td><td>First, targeting leads to better matching of ads to users.Second, it results in a thinner market for each impression.</td></tr><tr><td>Ganuza and Penalva (2010)</td><td>How does the precision of basic data affect the auction outcomes?</td><td>Precision of basic data</td><td>Precision increases the allocation efficiency and the information rents (i.e., reduced competition). Improving the precision increases the clearing price when the number of bidders is large. With two bidders, the price is nonincreasing with the precision.</td></tr><tr><td>Yao and Mela (2011)</td><td>How does targeting affect the outcomes of sponsored search auctions?</td><td>Nondisclosure vs. disclosure of basic data</td><td>Data disclosure and targeting increase consumer downloads of the advertised product, but it attenuates the competition between advertisers.</td></tr><tr><td>Chen and Stallaert (2014)</td><td>How does targeting affect impression prices vs. traditional advertising?</td><td>Nondisclosure vs. disclosure of basic data</td><td>Targeting relaxes the competition between advertisers but leads to a higher click-through rate because of better ad matching. Targeting may benefit the platform only when there are more than two advertisers.</td></tr><tr><td>Amaldoss et al. (2016)</td><td>How does the broad match service offered by search engines affect advertisers&#x27; behaviors in keyword auctions?</td><td>(Search engine) Broad match accuracy; (advertiser) nonadoption vs. adoption of broad match</td><td>Advertisers use broad match when its accuracy is not low.This creates a prisoner&#x27;s dilemma at intermediate accuracy levels, which vanishes at high accuracy. Offering broad match at intermediate accuracy benefits the search engine, whereas high accuracy may reduce its revenue as some advertisers may submit low bids for less relevant user segments.</td></tr><tr><td>De Corniere and De Nijs (2016)</td><td>How does basic data disclosure affect the auction payment when advertisers price products based on the disclosure policy?</td><td>(Platform) Nondisclosure vs. disclosure of basic data;(advertiser) product price</td><td>Data disclosure increases product prices, ad-user matching levels, and the total profit of the industry. Advertisers get a higher share of the total profit under data disclosure relative to cases of no disclosure. The platform&#x27;s revenue is higher under disclosure when the number of advertisers is large.</td></tr><tr><td>Golrezaei and Nazerzadeh (2016)</td><td>To which bidders and at what price should the platform release basic data?</td><td>The subset of bidders that receive basic data and the prices of basic data</td><td>Efficient and optimal mechanisms are designed to improve the platform&#x27;s revenue by releasing basic data to a selected subset of bidders.</td></tr><tr><td>Hummel and McAfee (2016)</td><td>How does targeting affect the platform&#x27;s revenue in position auctions?</td><td>Nondisclosure vs. disclosure of basic data</td><td>Data disclosure reduces the revenue of the auctioneer when there are two bidders and increases its revenue if the number of bidders is at least four given that bidders are asymmetric and their values are drawn from a distribution with a monotone hazard rate.</td></tr><tr><td>Sun et al. (2016)</td><td>Which features in basic data should the platform release?</td><td>The subset of basic data that should be released and when to release it</td><td>New mechanisms are designed to improve the platform&#x27;s revenue by probabilistically releasing basic data or selectively releasing a fraction of basic data. The performance guarantees of these mechanisms are derived.</td></tr><tr><td>Rafieian and Yoganarasimhan (2021)This study</td><td>How do targeting regimes affect the platform&#x27;s revenue?Does a platform benefit from subsidizing advertisers to acquire additional data?</td><td>Contextual targeting vs. behavioral targeting(1) Subsidy for the acquisition of additional data vs. no subsidy;(2) AS vs. LS vs. WS</td><td>The platform&#x27;s revenues are maximized when advertisers are not allowed to engage in behavioral targeting.First, subsidy provisions increase the ad-user matching level but at a magnitude less than the data cost. Second, subsidy provisions may intensify or attenuate competition between advertisers.</td></tr></table>

## 3. Model

When a user visits a website, an impression is created to display an ad to her. This triggers a second-price auction on the platform where advertisers bid on impressions. Consider N advertisers (bidders) indexed by 1, 2, $\dots ,$ N. Each advertiser can incur a cost of t to acquire targeting data from data providers. There is a variety of targeting data that can be obtained on the market, such as demographic information (e.g., age, gender, and marriage status), behavior information (e.g., website browsing history), and contextual information (e.g., the sentiment of the web-page content). Different advertisers may use different features for targeting. For example, advertiser 1 may use gender for targeting, whereas advertiser 2 relies on the age data. An advertiser can rely on both basic and additional data for targeting. However, because the aim is to analyze the impact of additional data on the RTB ecosystem, the informativeness of basic data is normalized to zero.

Let $\psi _ { i } \in \{ 0 , 1 \}$ be the feature used by advertiser i for targeting. For example, advertiser i might be interested in a user’s gender. If the data suggest that the user is female, $\psi _ { i } = 1 ;$ ; otherwise, $\psi _ { i } = 0$ . The probability of $\psi _ { i } =$ 1 is $p .$ In practice, an advertiser may have multiple ads. For instance, an “advertiser” may be an ad network. Instead of advertising for itself, an ad network runs ads on behalf of other firms and gets paid when a firm’s ad is displayed or based on some other contract (Sun et al. 2016). Motivated by such examples, we assume that each advertiser has multiple ads targeted at different impressions. These ads might be collected from different firms and promote different products. Let X be the ad inventory of advertiser i. For $x \in X _ { i } , v _ { i } ( x | \psi _ { i } )$ is the return of displaying x to a user with the feature $\psi _ { i } .$

Before deciding on her bid, advertiser i needs to decide which ad to display if she wins the impression. Suppose the advertiser does not acquire targeting data. In this case, she selects the best average ad (denoted by $\overline { { x } } _ { i } ^ { * } )$ ; that is, she selects the ad with the highest expected return across all possible users:

$$
\overline {{x}} _ {i} ^ {*} := \underset {x \in X _ {i}} {\arg \max} \mathrm{E} _ {\psi_ {i}} [ v _ {i} (x | \psi_ {i}) ].\tag{1}
$$

Without loss of generality, we assume that the maximizer to $\mathrm { E } _ { \psi _ { i } } [ v _ { i } ( { x } | \psi _ { i } ) ]$ is unique. Depending on the impression type, the return of displaying $\overline { { \boldsymbol { x } } } _ { i } ^ { * }$ might be h or $\bar { l } ,$ where $h > l ;$

$$
l := v _ {i} (\overline {{x}} _ {i} ^ {*} | \psi_ {i} = 0),\tag{2}
$$

$$
h := v _ {i} (\overline {{x}} _ {i} ^ {*} | \psi_ {i} = 1).\tag{3}
$$

Because advertiser i does not acquire data, she is unaware of $\psi _ { i }$ and only knows that the expected return of $\overline { { \boldsymbol { x } } } _ { i } ^ { * }$ is $p h + { \overline { { p } } } l$ , where ${ \dot { \overline { { p } } } } = 1 - p$

If advertiser i acquires data, she selects the ad that best fits the impression given by $x _ { i , \psi } ^ { * }$

$$
x _ {i, \psi_ {i}} ^ {*} := \underset {x \in X _ {i}} {\arg \max} v _ {i} (x | \psi_ {i}).\tag{4}
$$

Without loss of generality, we assume that the maximizer to $v _ { i } ( x | \psi _ { i } )$ is unique for $\psi _ { i } \in \{ 0 , 1 \}$ }. By definition, $x _ { i , \psi _ { i } } ^ { * }$ is the ad that best matches the user $\psi _ { i } ,$ whereas $\overline { { \boldsymbol { x } } } _ { i } ^ { * }$ is the best average ad across all possible users. Thus, the return of $x _ { i , \psi _ { i } } ^ { * }$ is equal to or higher than $\overline { { x } } _ { i } ^ { * } .$ . We assume that if $v _ { i } ( \overline { { x } } _ { i } ^ { * } | \psi _ { i } ) = h , v _ { i } ( x _ { i , \psi _ { i } } ^ { * } | \psi _ { i } ) = h + \delta _ { h }$ . Here, $\delta _ { h } \geq 0$ reflects the increase in impression value owing to a better match between the selected ad and the impression. If $v _ { i } ( \overline { { x } } _ { i } ^ { * } | \psi _ { i } ) = l , v _ { i } ( x _ { i , \psi _ { i } } ^ { * } | \psi _ { i } ) = l + \delta _ { l } .$ , where $\delta _ { l } \geq 0$ is the improved ad fit in this case.

To illustrate the ad selection process, consider advertiser i with three ads as shown in Table 4. These ads have different content and target different types of users. Ad 1 targets male users, whereas ad 2 targets female users. Different from ads 1 and $^ { 2 , }$ which only generate considerable returns for one type of user, ad 3 is a generic ad, and it generates considerable returns for both users.

Suppose the probability of a user being male or female is equal $( \mathrm { i . e . , } p = 0 . 5 )$ ). If the advertiser does not acquire gender information, she selects ad 3 for all users because the average return of ad 3 is $2 \times 0 . 5 + 4 \times$ $0 . 5 = 3 ,$ , the largest among the three ads. Thus, the best average ad $\overline { { \boldsymbol { x } } } _ { i } ^ { * }$ is ad 3. By definition, we have $h = 4$ and l � 2. Besides, $\boldsymbol { \psi } _ { i } = 1$ stands for female users, and $\psi _ { i } = 0$ stands for male users. If the advertiser acquires data, she displays ad 1 to male users and ad 2 to females. For a female user, the return changes from 4 to 4.8, implying $\delta _ { h } = 0 . 8$ . Similarly, we have $\delta _ { l } = 1$ for male users.

This example shows how $\overline { { \boldsymbol { x } } } _ { i } ^ { * }$ or $x _ { i , \psi _ { i } } ^ { * }$ is determined from the value matrix. Section EC.2 in the Online Appendix shows how our model can be mapped to advertisers with less than three or more than three advertisements. This study does not model the details of each advertiser’s value matrix. Instead, we directly model the returns of $\overline { { \boldsymbol { x } } } _ { i } ^ { * }$ and $x _ { i , \psi _ { i } } ^ { * }$ as described above. Qualitatively, this does not affect our findings.

We assume that advertisers are symmetric ex ante; that is, the distributions of $v _ { i } ( x _ { i , \psi _ { i } } ^ { * } | \psi _ { i } )$ and $v _ { i } ( \overline { { x } } _ { i } ^ { * } | \psi _ { i } )$ are identical for all advertisers. This assumption is motivated by the observation that if advertisers have very different impression values, platforms may separate them in the competition for impressions (e.g., by different levels of invitation-required auctions). Thus, advertisers in one auction tend to be approximately identical ex ante. We assume that the distribution of impression values is public knowledge. However, whether an impression is high value or low value to advertiser i is private information.

Table 4. An Illustrative Value Matrix (Three Ads)

<table><tr><td></td><td>Male user</td><td>Female user</td></tr><tr><td>Ad 1</td><td>3</td><td>0.5</td></tr><tr><td>Ad 2</td><td>0.2</td><td>4.8</td></tr><tr><td>Ad 3</td><td>2</td><td>4</td></tr></table>

We also assume the impression values of different advertisers are independent. Formally, for any i and $j ,$ ψ<sub>i</sub> is independent of $\psi _ { j } .$ This assumption implies that observing $\psi _ { i }$ does not provide advertiser i with any additional knowledge about other advertisers’ impression values. This is because advertisers use different targeting data in practice. For example, observing that a user is interested in music does not provide information on the user’s gender.

It is worth noting that additional data may contain noise arising from errors in the collection and integration of data. For instance, when merging data from various firms, the algorithm might incorrectly identify different users as the same person. Data providers might also intentionally introduce noise to protect user privacy. Data quality can impact the performance of ad selection.

For example, assume that Table 4 represents a value matrix with accurate gender data. If additional data are not precise—say, it has a 0.5 probability of incorrectly identifying a male user as female and a 0.1 probability of misidentifying a female user as male—with some algebra, we know that when the data indicate that a user’s gender is female (male), there is a probability of 0.35 (0.17) that it is wrong. In this case, the value of displaying ad 1 to a user indicated to be male by the data is $\bar { 3 } \times \mathsf { \Breve { 0 } { . } 8 3 } + 0 . 5 \times 0 . 1 7 = 2 . 5 8$ . Calculating other cells similarly leads to the value matrix as in Table 5.

In Table 5, the best average ad is still ad $3 ;$ hence, $h =$ 3.28, and $l = 2 . 3 3$ . If the advertiser acquires data, she selects ad 1 for users indicated to be male by additional data and ad 3 for users indicated to be female. The advertiser does not select the truly best ad for female users because the data carry a high likelihood of mistakenly identifying a male user as female. Consequently, when the data suggest that the user is female, the advertiser selects a generic ad to mitigate the risk of the user actually being male. The ad selection effects are $\delta _ { h } = 3 . 2 8 - 3 . 2 \dot { 8 } = 0$ and $\delta _ { l } = 2 . 5 8 - 2 . 3 3 = 0 . 2 5$ . Compared with Table 4, the noise in data decreases ad selection improvements. In our main model, $\delta _ { h }$ and $\delta _ { l }$ are assumed to be the same across advertisers. Section 7.3 analyzes an extension with variations in data qualities.

Table 5. An Illustrative Value Matrix (Noisy Data)

<table><tr><td rowspan="2"></td><td colspan="2">User gender suggested by data</td></tr><tr><td>Male user</td><td>Female user</td></tr><tr><td>Ad 1</td><td>2.58</td><td>1.39</td></tr><tr><td>Ad 2</td><td>0.97</td><td>3.16</td></tr><tr><td>Ad 3</td><td>2.33</td><td>3.28</td></tr></table>

In this study, our objective is to analyze whether a platform can increase its revenue by subsidizing advertisers to acquire data. We consider three frameworks: (1) all subsidized: all informed advertisers get a subsidy; (2) loser subsidized: an informed advertiser gets a subsidy only if she loses the auction; and (3) winner subsidized: an informed advertiser gets a subsidy only if she wins the auction. In the remainder of this paper, we analyze the optimal subsidy and the platform’s revenue under these frameworks (Table 6).

Given any subsidy framework, the timing of the game is as follows.

Stage 1. The platform announces the subsidy amount. The objective functions of the platform and advertisers depend on the subsidy framework, which is described later.

Stage 2. Advertisers decide on whether to acquire data.

Stage 3. A user arrives and generates an impression. The platform sends bid requests to advertisers. If advertiser i decides to acquire data in stage 2, she incurs a cost t to obtain and analyze the data. Based on the available data, each advertiser selects her ad and her bid for this impression.

Stage 4. Based on the bids received from advertisers, the platform selects the auction winner and displays her ad to the user. The winner pays the second-highest bid amount to the platform, and the platform subsidizes advertisers based on the picked subsidy framework.

In the above timeline, advertisers make data acquisition decisions before any impressions are generated. This is because an ad auction has to be finished in rea time, and advertisers cannot decide whether to acquire data on an impression-by-impression basis.

Table 6. Key Notations

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $\psi_{i}$ </td><td>Feature used by advertiser  $i$  for targeting</td></tr><tr><td> $\overline{x}_{i}^{*}$ </td><td>The best average ad of advertiser  $i$ </td></tr><tr><td> $x_{i,\psi_{i}}^{*}$ </td><td>The best ad of advertiser  $i$  given the feature  $\psi_{i}$ </td></tr><tr><td> $h$ </td><td>The value of the best average ad when  $\psi_{i} = 1$ </td></tr><tr><td> $l$ </td><td>The value of the best average ad when  $\psi_{i} = 0$ </td></tr><tr><td> $\delta_{h}$ </td><td>The difference between the values of  $\overline{x}_{i}^{*}$  and  $x_{i,\psi_{i}}^{*}$  when  $\psi_{i} = 1$ </td></tr><tr><td> $\delta_{l}$ </td><td>The difference between the values of  $\overline{x}_{i}^{*}$  and  $x_{i,\psi_{i}}^{*}$  when  $\psi_{i} = 0$ </td></tr><tr><td> $p$ </td><td>Probability of  $\psi_{i} = 1$ </td></tr><tr><td> $t$ </td><td>Cost of data acquisition</td></tr><tr><td> $v_{i}$ </td><td>Impression value to advertiser  $i$ </td></tr><tr><td> $w_{i}$ </td><td>Whether advertiser  $i$  wins the impression</td></tr><tr><td colspan="2">Decision variables</td></tr><tr><td> $b_{i}$ </td><td>Bid of advertiser  $i$ </td></tr><tr><td> $d_{i}$ </td><td>Advertiser  $i$ &#x27;s decision to acquire data;  $d_{i} = 1$  for acquiring data and  $d_{i} = 0$  for not acquiring it</td></tr><tr><td> $s$ </td><td>Subsidy for data acquisition;  $s \geq 0$ </td></tr></table>

## 4. All-Subsidized Framework

In this section, we analyze the AS framework, wherein the platform provides a subsidy to each advertiser that incurs a cost to acquire data. In the game, the platform selects the optimal subsidy amount that maximizes the revenue net of the subsidy. The platform’s net revenue is given by

$$
\operatorname{E} \left[ \operatorname{SH} (b _ {1}, \dots , b _ {N}) - s \sum_ {i = 1} ^ {N} d _ {i} | d _ {1}, \dots , d _ {N} \right],\tag{5}
$$

where $\mathrm { S H } ( b _ { 1 } , \dots , b _ { N } )$ denotes the second-highest bid among $b _ { 1 } , \dots , b _ { N }$

An advertiser decides on whether to acquire data and how much to bid in the auction so that her payoff net of the data cost can be maximized. Let $w _ { i } = 1$ denote that advertiser i wins the impression, and $w _ { i } = 0$ otherwise. The payoff of each advertiser i is as follows:

$$
\operatorname{E} [ w _ {i} (v _ {i} - b _ {- i}) - d _ {i} (t - s) | d _ {1}, \ldots , d _ {N} ],\tag{6}
$$

where $b _ { - i }$ is the largest bid among advertisers except advertiser i. The advertiser’s payoff has two components. The first component is $w _ { i } ( v _ { i } - b _ { - i } )$ , standing for the auction gain. If advertiser i loses the auction $( w _ { i } = 0 )$ her auction gain is zero. If she wins the impression (w $= 1 )$ , she pays $b _ { - i }$ and has an auction gain equal to $v _ { i } - b _ { - i } .$ . The second component, $d _ { i } ( t - s )$ , is the net data cost.

## 4.1. Equilibrium Under AS

Lemma 1 characterizes the equilibrium bidding strategies in stage 3. Compared with classical SPAs, advertisers in our model need to make a data acquisition decision before bidding. Data acquisition affects advertisers’ impression values. However, given the impression value, an advertiser’s bidding strategy is the same as that in classical SPAs; that is, they bid their true values.

Lemma 1. Under the AS framework, advertiser i bids $v _ { i } ( x _ { i , \psi _ { i } } ^ { * } | \psi _ { i } )$ if she acquires data; otherwise, she bids $E _ { \psi _ { i } } [ v _ { i }$ $( \overline { { x } } _ { i } ^ { * } | \psi _ { i } ) ] = p h + \overline { { p } } l .$

The logic behind the truth-telling bidding strategy is as follows. Suppose advertiser i acquires data. She selects $x _ { i , \psi _ { i } } ^ { * }$ with a return $v _ { i } ( x _ { i , \psi _ { i } } ^ { * } | \psi _ { i } ) . \hat { \mathrm { I f } } b _ { i } < v _ { i } ( x _ { i , \psi _ { i } } ^ { * } | \psi _ { i } ) ,$ advertiser i may lose the auction when she could have won the impression with a price less than its worth. If $b _ { i } > v _ { i } ( x _ { i , \psi _ { i } } ^ { * } | \psi _ { i } )$ , she may win the impression at a price greater than its worth. Thus, bidding truthfully is the dominant strategy. The equilibrium bidding strategy when advertiser i does not acquire data can be derived using a similar argument.

We then determine how many advertisers acquire data in stage 2. Generally speaking, there are multiple equilibria such that m advertisers acquire data. Without loss of generality, we assume that advertisers 1 to m acquire data in the equilibrium. For an arbitrary $n \in$ $\{ m ^  \stackrel { - } { + } 1 , \ldots , N \}$ , the value of data acquisition to advertiser n equals the increase in her expected auction gain if she acquires data. Let $D V _ { m }$ denote the data value in this case; it does not depend on n because advertisers are symmetrical. Mathematically,

$$
D V _ {m} = \operatorname{E} [ w _ {n} (v _ {n} - b _ {- n}) | d _ {\{1, \dots , m \}} = 1, d _ {\{m + 1, \dots , N \} \setminus \{n \}} = 0,
$$

$$
\left. d _ {n} = 1 \right] - \mathrm{E} \left[ w _ {n} \left(v _ {n} - b _ {- n}\right) \mid d _ {\{1, \dots , m \}} = 1, \right.
$$

$$
d _ {\{m + 1, \ldots , N \} \setminus \{n \}} = 0, d _ {n} = 0 ].\tag{7}
$$

Section EC.3.1 in the Online Appendix explains the derivation of $D V _ { m }$ . When $\delta _ { l } \ge p ( h - l ) , D V _ { m }$ is given by

$$
D V _ {m} = \left\{ \begin{array}{l l} p \delta_ {h} + \overline {{p}} \delta_ {l}, & \text { if } m = 0, \\ p (\overline {{p}}) ^ {m} (h - l + \delta_ {h} - \delta_ {l}), & \text { if } m \geq 1. \end{array} \right.\tag{8}
$$

When $\delta _ { l } < p ( h - l ) , D V _ { m }$ is given by

$$
D V _ {m} = \left\{ \begin{array}{l l} p (\overline {{p}}) ^ {m} (\overline {{p}} (h - l) + \delta_ {h}), & \text {if m <   N - 1}, \\ (\overline {{p}}) ^ {N - 1} (p \delta_ {h} + \overline {{p}} \delta_ {l}), & \text {if m = N - 1}. \end{array} \right.\tag{9}
$$

We can observe that $D V _ { m }$ decreases in m, implying that advertiser n benefits less from additional data as more competitors acquire it. As long as one of the advertisers 1 to m (data buyers) bids $h + \delta _ { h } ,$ , we have $b _ { - n } = h + \delta _ { h }$ No matter whether advertiser n acquires data or not, her expected auction gain is ma $\mathsf { \Omega } _ { : } ( 0 , v _ { n } - b _ { - n } ) = 0$ because $v _ { n } \leq h + \delta _ { h }$ . Thus, data benefit advertiser n only when advertisers 1 to m all have low impression values. This explains why data become less valuable to advertiser n as m increases.

Besides, $D V _ { m }$ increases with the difference between h and $\mathbf { \xi } ( \mathbf { i . e . , } h - l )$ . To see the reason, we first look at a scenario wherein each advertiser has only one ad $( \mathrm { i . e . , }$ $\delta _ { h } = \delta _ { l } = 0 )$ . Without data, an advertiser bids $p h + { \overline { { p } } } l .$ For $\boldsymbol { \psi } _ { n } = 0 ,$ , the advertising return is l. Hence, bidding $p h + { \overline { { p } } } l$ is too high. The advertiser may win the impression with a price $p h + { \overline { { p } } } l ,$ , ending up with a loss $p ( h - l )$ In contrast, for $\boldsymbol { \psi } _ { n } = 1$ , the advertising return is $h ,$ and bidding $p h + { \overline { { p l } } }$ is too low. If $b _ { - n } = p h + \overline { { p } } l$ , the advertiser can win the impression by increasing the bid to h and obtain a payoff $\overline { { p } } ( h - l ) ,$ , which would not be obtained under the bid $p h + { \overline { { p l } } }$ . By acquiring data, advertisers can bid accurately and avoid these overbidding and underbidding losses. As $h - l$ increases, user types have a greater impact on advertising returns. This increases the overbidding and underbidding losses and adds to the importance of bidding selection.

We now look at how $\delta _ { l }$ and $\delta _ { h }$ affect $D V _ { m } .$ . As Corollary 1 shows, the impact of $\delta _ { l }$ is twofold. On the one hand, a larger δ implies that advertisers select better ads for $\psi _ { i } = 0$ and get more returns from advertising. On the other hand, with $\delta _ { h } > 0$ and $\delta _ { l } > 0$ , the gap between two user types’ advertising returns changes from $h - l$ to $h + \delta _ { h } - l - \delta _ { l }$ . An increase in $\delta _ { l }$ reduces the gap and the bid selection benefit. Because of these two opposite impacts, $D V _ { m }$ may increase or decrease with $\delta _ { l } .$ Unlike $\delta _ { l } ,$ a larger $\delta _ { h }$ leads to a bigger gap between the advertising returns, adding to the bid selection benefit. Thus, $D V _ { m }$ always increases with $\delta _ { h } .$

Figure 2. (Color online) Ranges of t and $\delta _ { h } ,$ Where $s ^ { \mathrm { A S } } > 0 ( h = 8 , l = 4 , p = 1 / 2 , \delta _ { l } = 0 )$  
![](/api/attachments/2R8G9AJN/fulltext/images/2bf853c3a8a01622b390357308f715fd2da4c41d08afc3f4397a7ae4fc646dfd.jpg)

![](/api/attachments/2R8G9AJN/fulltext/images/a3ceba4b38576b30bee818a875f38067dfe52a5090ca946dc1611be0a5810450.jpg)  
Notes. (a) N � 2. (b) N � 4.

Corollary 1. (1) When $\delta _ { l } < p ( h - l ) , D V _ { m }$ weakly increases with $\delta _ { l } .$ When $\delta _ { l } \ge p ( h - l ) , D V _ { m }$ increases with $\delta _ { l } f o r m = 0$ and decreases with $\delta _ { l } f o r m \geq 1 . \left( 2 \right) D V _ { m }$ increases with $\delta _ { h } .$

Under AS, all advertisers that acquire data can obtain the subsidy. Thus, the data cost becomes t � s. If $D V _ { m }$ $< t - s < \bar { D } V _ { m - 1 } ,$ there are m advertisers acquiring data in the equilibrium. After deriving the number of informed advertisers in stage 2, we calculate the optimal subsidy in stage 1. There may exist multiple subsidy values that maximize the platform’s net revenue. If so, zero must be one of them. For ease of discussion, we simply say that the optimal subsidy is zero in this case. Let $\mathbf { \chi } _ { S } ^ { \star }$ be the optimal subsidy under AS. Theorem 1 characterizes the optimal subsidy amount that the platform should provide.

Theorem 1. Let $\Psi _ { m } = p ( \overline { { p } } ) ^ { m } ( \delta _ { h } + \overline { { p } } h - \overline { { p } } l ) , \Phi _ { m } = p ( \overline { { p } } ) ^ { m }$ $( h - l + \delta _ { h } - \delta _ { l } ) , \Theta _ { m } = ( \overline { { p } } ) ^ { m } ( p \delta _ { h } + \overline { { p } } \delta _ { l } )$ , and $\Delta _ { 1 } = \left( N - 2 \right)$ $p ^ { 2 } \delta _ { h } + ( \overline { { p } } ) ^ { 2 } \delta _ { l } - p \overline { { p } } ( h - l ) ( 1 + p - N p ) .$

1. When $\delta _ { l } < p ( h - l ) , s ^ { A S } > 0$ in the following cases: a. $s ^ { A S } = \dot { t } - \Psi _ { m } ~ i f \Psi _ { m - 1 } ( m + \overline { { p } } ) / ( m + 1 \bar { ) } > t > \Psi _ { m } ,$ where m is an integer between 1 and $N - 3 ;$ $\mathrm { b . } s ^ { A S } = t - \Psi _ { N - 2 } ^ { \sim } i f ( \Psi _ { N - 3 } ( N - 2 ) + \Theta _ { N - 2 } ) / ( N - 1 )$ $> t > \Psi _ { N - 2 } \ a n d \ \Delta _ { 1 } > 0 ;$ and $\mathsf { c . } \mathsf { \ s } ^ { A S } = t - \Theta _ { N - 1 } \mathsf { \ i f } ( 1 - p / N ) \Theta _ { N - 2 } > t > \Theta _ { N - 1 } .$

2. When $\delta _ { l } \geq p ( h - l ) , s ^ { A S } > 0$ in the following cases: a $\begin{array} { r } { \cdot \ s ^ { A S } = t - \Phi _ { 1 } \ i f _ { 2 } ^ { 1 } ( \Phi _ { 1 } + \Theta _ { 0 } ) > t > \Phi _ { 1 } \ a n d } \end{array}$ b. $s ^ { A S } = t - \Phi _ { m } \ i f \Phi _ { m - 1 } ( m + \overline { { p } } ) / ( m + 1 ) > t > \Phi _ { m } ,$ where m is an integer between 2 and $N - 1$

Figures 2 and 3 depict the ranges of $t , \delta _ { h } ,$ and $\delta _ { l } ,$ wherein $s ^ { \mathrm { A S } } > 0 .$ . We can see that the range of t where the platform should provide subsidies may be a set of disconnected intervals. As t increases from zero, the platform repeatedly changes from not providing the subsidy to providing it.

Figure 3. (Color online) Ranges of t and $\delta _ { l } ,$ Where $s ^ { \mathrm { A S } } > 0 ( h = 8 , l = 4 , p = 1 / 2 , \delta _ { h } = 0 )$  
(a)  
![](/api/attachments/2R8G9AJN/fulltext/images/cb9ef14268498584425eeb09a8388ec41e832d12ad42b990344aa9cc0bbbfd83.jpg)  
Notes. (a) N � 2. (b) N � 4.

(b)  
![](/api/attachments/2R8G9AJN/fulltext/images/8dd6d66b16b3f200eff3f1eda60ef26d3a14b0ef4e4446ac34ebc546435828b4.jpg)

## 4.2. Data Cost and Optimal Subsidy

From Figures 2 and 3, we observe that $s ^ { \mathrm { A S } } = 0$ when $t \le D V _ { N - 1 }$ . In this case, the cost of data is so low that all advertisers acquire data without subsidies. Thus, there is no need to provide subsidies. If t increases above $D V _ { N - 1 }$ , the platform starts to provide subsidies. However, as t further increases and becomes closer to $D V _ { N - 2 } ,$ the optimal strategy again becomes one of not providing subsidies.

When $D V _ { N - 1 } < t \le D V _ { N - 2 } , N - 1$ advertisers acquire data without subsidies. Suppose the platform uses subsidies to induce advertiser n (the last uninformed advertiser) to acquire data. We call advertisers that acquire data without subsidies naturally informed advertisers and advertiser n that acquires data after the subsidy provision an induced informed advertiser. If naturally informed advertisers all have a low valuation, the impression price is $l + \delta _ { l . }$ , no matter whether advertiser n acquires data or not. If more than two naturally informed advertisers have a high valuation, the impression price is always $h + \delta _ { h }$ . In these two cases, inducing advertiser n to acquire data does not increase the impression price.

In the third case, only one naturally informed advertiser (say, advertiser 1) has a high valuation. For ease of discussion, assume $\delta _ { l } \leq p ( h - \bar { l } )$ . If advertiser n does not acquire data, advertiser 1 wins the impression and pays $\bar { p h } + \overline { { p l } }$ . If advertiser n acquires data and bids $l + \delta _ { l } ,$ advertiser 1 still wins the auction and pays $l + \delta _ { l }$ If advertiser n bids $h + \delta _ { h } ,$ , advertiser 1 pays $h + \delta _ { h }$ (assume that advertiser 1 is selected as the winner). In summary, after advertiser n acquires data, the average payment of advertiser 1 increases to $p ( h + \delta _ { h } ) + \overline { { p } } ( l + \delta _ { l } )$ This is because advertiser n selects better ads and submits higher bids on average, intensifying the competition faced by advertiser 1.

Inducing advertiser n to acquire data may intensify the competition, allowing the platform to extract more surplus from advertisers. If the extracted surplus is more than the subsidy, the platform’s net revenue increases. As t increases from $D V _ { N - 1 }$ to $D V _ { N - 2 }$ , naturally informed advertisers incur higher costs to acquire data, and their payoffs decrease. Because less surplus can be extracted from advertisers, the optimal strategy changes to not providing subsidies when t approaches $D V _ { N - 2 }$ . When t increases above $D V _ { N - 2 }$ , the number of naturally informed advertisers reduces from $N - 1$ to $N - 2$ . This attenuates the competition and increases advertisers’ payoffs. Therefore, the platform can, again, extract more surplus from them.

When $t \geq D V _ { 0 } ,$ , the optimal subsidy is always zero. Because of the large data cost, no one acquires data without subsidies, and all advertisers bid $p h + { \overline { { p } } } l .$ . In this case, the competition among advertisers is extremely fierce, and no advertiser has a positive payoff. There is no surplus left to exploit. Thus, the platform should not provide any subsidy when the data cost is greater than $D V _ { 0 } .$

The impression price is determined by two factors: the fit between delivered ads and users and the competition among advertisers. The former determines the total value created through advertising, and the latter reflects how much of the value is shared by the platform. Prior work suggests that data acquisition attenuates competition while improving the fit of delivered ads (e.g., Ganuza 2004, Chen and Stallaert 2014). Our findings are different from those of previous studies in two aspects.

First, prior work identifies competition attenuation after data acquisition because some informed advertisers find low impression values and become less interested in that impression. In contrast, we identify intensified competition. Prior studies consider situations where the data acquisition decision is exogenous to advertisers: the data owner releases data to none or all advertisers. In our study, the equilibrium number of informed advertisers is calculated endogenously. It is possible that some advertisers decide to acquire data, whereas others do not. In this case, uninformed advertisers outbid informed advertisers that are not interested in the impression. Thus, their reduced interests do not attenuate the competition.

Second, because prior work finds competition attenuated after data acquisition, they identify improved ad fitting as the critical factor that increases the impression price. For example, Chen and Stallaert (2014) indicate that the platform has the incentive to release basic data to advertisers for free only when the ad-fit improvement dominates the competition attenuation. Different from prior work, we find that in the absence of subsidies, advertisers balance the data acquisition cost and the fit between delivered ads and users. If the platform uses subsidies to induce more informed advertisers, the improvements in ad fit are less than the extra data acquisition cost. Thus, the net ad-fit effect (i.e., improved ad fits minus the data cost) is negative.

Proposition 1. Without subsidies, advertisers’ data acqui sition decisions maximize the expected advertising return after the auction minus the data acquisition cost incurred by all advertisers.

Because of the negative net ad-fit effect, whether subsidies benefit the platform depends on the ability to intensify competition. This explains why the platform does not provide subsidies when $t \geq D V _ { 0 } ,$ . This is even true when data acquisition increases the impression price. In this case, if the platform has the data, it would be willing to release the data. However, if the platform does not own data and subsidies are needed to induce data acquisition, the platform is unwilling to do it because the competition is extremely fierce when $t \geq D V _ { 0 } ,$ , and data acquisition can only attenuate the competition.

To summarize, there is a fundamental difference between the platform’s incentive to release the basic data owned by the platform and that of subsidizing advertisers to acquire data on their own. In the former case, the platform maximizes the impression price determined by the ad-matching improvement and competition attenuation. In the latter case, the platform maximizes the net revenue that is determined by the net ad-fit effect and the competition effect, which may be competition intensification or attenuation.

## 4.3. Ad Selection and Optimal Subsidy

This section discusses the relationship between ad selection and the optimal subsidy. First, given any $t ,$ the ranges of $\delta _ { h }$ and $\delta _ { l } ,$ wherein $s ^ { \check { \mathrm { A S } } } > 0 ,$ , may be a set of disjointed intervals. Similar to the impact of $t ,$ competition intensity changes nonmonotonically with $\delta _ { h }$ and $\delta _ { l } .$ . On the one hand, an increase in $\delta _ { h }$ and $\delta _ { l }$ means that informed advertisers select better ads and get more advertising returns. On the other hand, as $\delta _ { h }$ and $\delta _ { l }$ increase, naturally informed advertisers increase, intensifying the competition and reducing advertisers’ surplus. Subsidy provisions are beneficial only when they can extract enough surplus for the platform.

Second, as $\delta _ { h }$ and $\delta _ { l }$ increase, the range of $t ,$ wherein $s ^ { \mathrm { A S } } > 0 .$ , increases; that is, subsidy provisions are more likely to increase the platform’s net revenue. The reasons are as follows. Larger $\delta _ { h }$ and $\delta _ { l }$ imply a higher value of data acquisition. As a result, the platform can use a smaller subsidy to induce advertisers to acquire data. Besides, as $\delta _ { h }$ increases, informed advertisers get more returns from advertising and bid higher. Thus, inducing more informed advertisers intensifies the competition more significantly.

Ignoring ad selection may lead to suboptimal decisions on whether the platform should subsidize advertisers. For example, Chen and Stallaert (2014) find that when there are only two advertisers, data acquisition decreases the impression price because the competition attenuation dominates the ad-fit improvements. Based on their results, the platform should not provide the subsidy. However, Figures 2 and 3 show that the platform may still provide the subsidy when $N = 2$ . The key difference is that Chen and Stallaert (2014) do not consider the impact of data on ad selection. For instance, Theorem 1 shows that given two advertisers, the platform provides subsidies only when $( 1 -$ $p / 2 ) ( p \delta _ { h } + \overline { { p } } \delta _ { l } ) > t > \overline { { p } } ( p \delta _ { h } + \overline { { p } } \delta _ { l } )$ ). When $\dot { \delta } _ { h } = \delta _ { l } = 0 .$ , this interval disappears, and the platform should never provide subsidies, which is the same as that implied by Chen and Stallaert (2014).

## 4.4. Advertisers’ Payoffs

Because we assume that the platform is a profit maximizer, it only provides subsidies when this can increase its net revenue. A related question is how the subsidy provision affects advertisers in the RTB ecosystem. Theorem 2 presents the analysis of advertisers’ payoffs after the subsidy provision.

Theorem 2. After providing $s ^ { A S } > 0 ,$ , we have that

• the naturally informed advertiser’s payoff decreases,

• the induced informed advertiser’s payoff does not change, and

• the remaining uninformed advertiser’s payoff (weakly) increases.

We divide advertisers into three groups—(i) naturally informed advertisers, (ii) induced informed advertisers, and (iii) advertisers that remain uninformed after the subsidy provision. First, naturally informed advertisers are worse off. This is because more advertisers acquire data and increase bids because of better ad selection. Thus, naturally informed advertisers face more intense competition. Second, induced informed advertisers have the same payoff as before. This is because the platform, as a profit maximizer, provides a subsidy that induces informed advertisers to be indif ferent between acquiring and not acquiring data.

Third, advertisers that remain uninformed after the subsidy provision may be better off. Suppose advertisers $n - 1$ and n are the only two uninformed advertisers without subsidies. They bid $p h + { \overline { { p } } } l$ and have zero payoffs. The platform now provides subsidies to make advertiser $n - 1$ acquire data. Advertiser n remains unin formed. Advertiser n has a positive payoff if all of $N - 1$ informed advertisers bid $l + \delta _ { l } ,$ , assuming $\delta _ { l } < p ( h - l )$ Because data acquisition makes the impression value more dispersed, having more advertisers acquire data relaxes the competition faced by the remaining uninformed advertisers. That is why they may be better off when they neither acquire data nor get subsidies.

The impact of subsidy provision on a platform’s benefits depends on how effectively it intensifies competition. According to Theorem $^ { 2 , }$ subsidies increase the competition intensity faced by naturally informed advertisers that typically purchase data without them. However, they weakly attenuate the competition faced by advertisers that do not purchase data, often smaller businesses with limited budgets. As a result, subsidies can end up being a tax on the wealthy. Moreover, subsidies not only increase a platform’s revenue but also, can encourage weaker firms to participate, thereby promoting market growth.

## 5. Loser-Subsidized Framework

In this section, we analyze the LS framework, wherein the platform only subsidizes an informed advertiser when she loses the auction. The LS framework is motivated by the usual practice in most auctions; if you do not win, you pay nothing. When acquiring data, advertisers face the risk of losing the auction. If an informed advertiser loses the auction, she spends money on data acquisition without any returns. By subsidizing informed advertisers that lose the auction, the platform can reduce the risk associated with data acquisition and induce more advertisers to acquire data.

Because of the change in the subsidy mechanism, the payoff of advertiser i becomes

$$
\operatorname{E} [ w _ {i} (v _ {i} - b _ {- i}) - d _ {i} (t - (1 - w _ {i}) s) | d _ {1}, \ldots , d _ {N} ].\tag{10}
$$

The platform’s objective function is

$$
\mathrm{E} \left[ \mathrm{SH} (b _ {1}, \dots , b _ {N}) - s \sum_ {i = 1} ^ {N} (d _ {i} (1 - w _ {i})) \Big | d _ {1}, \dots , d _ {N} \right].\tag{11}
$$

We start with advertisers’ bidding strategies under LS. Proposition 2 indicates that informed advertisers’ bids are affected by the subsidy amount. Under LS, informed advertisers receive a subsidy from the platform if they lose the auction, but they cannot get it if they win. Thus, the net gain from winning the auction is the impression value minus the subsidy. Therefore, under LS, informed advertisers bid $v _ { i } ( x _ { i , \psi _ { i } } ^ { * } | \psi _ { i } ) - s$

Proposition 2. Under LS, advertiser i bids $\operatorname* { m a x } ( v _ { i } ( x _ { i , \psi } ^ { * }$ φi $| \psi _ { i } ) - s , 0 )$ if she acquires data, and she bids $p h + { \overline { { p l } } }$ otherwise.

When $s = \overline { { p } } ( h - l ) + \delta _ { h } ,$ , an informed advertiser with a high impression valuation bids the same value as uninformed advertisers. In this case, whether the impression is allocated to this informed advertiser or an uninformed advertiser does not affect any advertiser’s payoff. However, the platform’s net revenue is higher when the informed advertiser is chosen to be the winner because there is no need for a subsidy payout. Besides, although the informed advertiser bids the same as uninformed advertisers, she has a higher impression valuation than uninformed advertisers. This implies that the informed advertiser’s ads fit the user better than those of uninformed advertisers. In a nutshell, all stakeholders (weakly) prefer to allocate the impression to the informed advertiser. Thus, we assume that the platform selects the informed advertiser as the winner in this case.

After clarifying the allocation rule and advertisers bidding strategies, we then analyze the platform’s net revenue under LS. Because informed advertisers under LS decrease their bids by the amount of subsidy, the competition among advertisers is attenuated. Thus, we have Theorem 3.

Theorem 3. The platform’s net revenue under AS is at least the same as that under LS.

The intuition is as follows; the platform’s net revenue depends on the level of ad fit and competition intensity. For any subsidy under LS, we can always set an appropriate subsidy under AS that leads to the same number of informed advertisers. Thus, AS and LS lead to the same level of ad fit. However, the competition is less intense under LS; hence, the platform’s net revenue is lower under LS.

## 6. Winner-Subsidized Framework

So far, we have analyzed AS and LS. The last framework is WS, wherein the platform only subsidizes an informed advertiser when she wins the auction. The objective of advertiser i is given by

$$
\operatorname{E} [ w _ {i} (v _ {i} - b _ {- i}) - d _ {i} (t - w _ {i} s) | d _ {1}, \dots , d _ {N} ].\tag{12}
$$

The platform’s objective function is

$$
\operatorname{E} \left[ \mathrm{SH} (b _ {1}, \dots , b _ {N}) - s \sum_ {i = 1} ^ {N} (d _ {i} w _ {i}) \Big | d _ {1}, \dots , d _ {N} \right].\tag{13}
$$

## 6.1. Equilibrium Under WS

In stage 4, the platform sends the subsidy to the auction winner if she has acquired data. Under WS, winning an auction brings two benefits to the informed advertiser. First, she can display her ad to the user. Second, she can get a subsidy from the platform. Thus, the value of winning is the sum of the advertising return and the subsidy. Using a similar argument for AS, we have that the dominant strategy of informed advertisers is bidding the sum of these two benefits under WS.

Proposition 3. Under the WS framework, advertiser i bid $v _ { i } ( x _ { i , \psi _ { i } } ^ { * } | \psi _ { i } ) + s$ if she acquires data, and she bids $p h + { \overline { { p l } } }$ otherwise.

With advertisers’ bidding strategies, we next derive the equilibrium in stage 2. The equilibrium number of informed advertisers under WS (denoted by $N ^ { W S } )$ is given by Lemma 2.

## Lemma 2.

a. Case $\delta _ { l } < p ( h - l ) . \quad I f \quad Y _ { 1 , m } < t \leq Y _ { 2 , m } , N ^ { W S }$ given by

is

$$
N ^ {W S} = \left\{ \begin{array}{l l} m + 1, & i f s \geq Y _ {3, m}, \\ m, & i f s <   Y _ {3, m}. \end{array} \right.\tag{14}
$$

b. Case $\delta _ { l } \ge p ( h - l ) . I f t > \Theta _ { 0 } , N ^ { W S }$ is given by

$$
N ^ {W S} = \left\{ \begin{array}{l} 1, i f s \geq t - \Theta_ {0}, \\ 0, i f s <   t - \Theta_ {0}. \end{array} \right.\tag{15}
$$

Otherwise, $N ^ { W S }$ only depends on t and is not affected by s.

Under ${ \mathrm { A S } } ,$ as long as the subsidy is large enough, the platform can induce all advertisers to acquire data. By contrast, Lemma 2 shows that the platform may not be able to make all advertisers acquire data under WS. To explain the reason, suppose $\bar { \delta _ { l } } < p ( h - l )$ . Consider a scenario wherein the platform provides $s = p ( h - l ) - \delta _ { l } ,$ and only advertiser 1 acquires data. Let advertiser n be an arbitrary, uninformed advertiser. Notice that the minimum bid of advertiser 1 is $l + \delta _ { l } + s = p h + \overline { { p } } l ,$ the same as the bid of advertiser n. Thus, the payoff of advertiser n is zero. If the platform increases the subsidy, advertiser 1 bids higher, and the payoff of advertiser n remains zero.

We next check the payoff of advertiser n if she acquires data given $s = p ( h - l ) - \delta _ { l }$ . After advertiser n acquires data, there are two possible outcomes. If she loses the auction, her payoff is –t. If advertiser n wins, she gains $v _ { n } ( x _ { n , \psi _ { n } } ^ { * } | \psi _ { n } ) + s$ . Notice that the competitors of advertiser n include advertiser 1 and $N - 2$ uninformed advertisers. Because advertiser 1 bids at least the same as uninformed advertisers, the payment of advertiser n is equal to advertiser 1’s bid (i.e., $v _ { 1 } ( x _ { 1 , \psi _ { 1 } } ^ { * } | \psi _ { 1 } ) + s )$ . Her net payoff is $v _ { n } ( x _ { n , \psi _ { n } } ^ { * } | \psi _ { n } ) - v _ { 1 } ( x _ { 1 , \psi _ { 1 } } ^ { * } | \psi _ { 1 } ^ { , } ) - t$ . We observe that advertiser n gets a subsidy but pays it back to the platform. As a result, her payoff does not depend on s. If the platform increases $s ,$ the payoff of advertiser n remains the same.

To summarize, no matter whether advertiser n acquires data or not, her payoff does not change for $s \geq p ( h - l ) - \delta _ { l }$ . Thus, the data value remains the same for $s \geq p ( h - l ) - \delta _ { l }$ . If advertiser n does not acquire data given $s = p ( h - l ) - \delta _ { l } ,$ , she does not acquire it no matter how much the subsidy is increased. We call $p ( h - l ) -$ $\delta _ { l }$ the effective subsidy upbound (denoted by s˜). Formally, s ˜ is the subsidy such that informed advertisers bid at least the same as uninformed advertisers.

If no one acquires data for $s = \tilde { s } _ { \scriptscriptstyle \perp }$ , the platform can induce one informed advertiser by increasing s. This occurs because if there is only a single informed advertiser, upon winning the impression, she pays the bid from an uninformed advertiser rather than that from another informed advertiser. Thus, she does not pay the subsidy back to the platform. If there are informed advertisers under $s = \tilde { s } ,$ increasing s does not affect any advertiser’s payoff because the winner receiving the subsidy pays it back to the platform. As a result, increasing s does not attract any new informed advertisers. When $\delta _ { l } \geq p ( h - l )$ , informed advertisers outbid uninformed advertisers even if $s = 0 ,$ , implying $\tilde { s } = 0$ Therefore, as case (b) of Lemma 2 shows, subsidies can only induce new informed advertisers when t is so large that no advertisers acquire data naturally.

We then derive the optimal subsidy under WS. When $s = \tilde { s } ,$ an informed advertiser with a low valuation bids the same as uninformed advertisers. Unlike LS, all stakeholders (weakly) prefer to allocate the impression to an uninformed advertiser in this case. When deriving the optimal subsidy, we assume that an uninformed advertiser is selected as the winner. Theo rem 4 shows the optimal subsidy under WS, denoted by $s ^ { W S }$ . From Theorem $^ { 4 , }$ we can see that similar to $s ^ { \mathrm { A S } }$ the ranges of $t , \delta _ { h } ,$ and $\delta _ { l } ,$ wherein $s ^ { W S } > 0 ,$ , are disconnected intervals because of the nonlinear changes in the competition intensity as $t , \delta _ { h } ,$ and $\delta _ { l }$ increase.

Theorem 4. When $\delta _ { l } \geq p ( h - l ) , s ^ { W S } = 0$ . When $\delta _ { l } < p ( h$ $- l ) , s ^ { W S }$ is summarized as follows: $\begin{array} { r } { \mathtt { a . } \ s ^ { W S } = ( t - \Psi _ { m } ) / ( p ( \overline { { p } } ) ^ { m } ) \ i f \operatorname* { m i n } ( \Psi _ { m - 1 } ( m + \overline { { p } } ) / ( m + 1 ) , } \end{array}$ $\Phi _ { m } ) > t > \Psi _ { m } f o r 1 \leq m \leq N - 3 ;$ $\mathrm { ~ b . ~ } s ^ { W S } = ( t - \Psi _ { N - 2 } ) / ( p ( \overline { { p } } ) ^ { N - 2 } )$ if min $( \Omega _ { 2 } , \Phi _ { N - 2 } ) > t >$ $\Psi _ { N - 2 } \mathrm { ~ } a n d \mathrm { ~ } p > 1 / N ;$ $\mathrm { ~ c ~ . ~ } s ^ { W S } = p ( h - l ) - \delta _ { l } i f \Phi _ { N - 2 } > t > \Psi _ { N - 2 } , \Delta _ { 2 } > 0 ,$ , and $0 < p \leq 1 / N ;$ $\begin{array} { r } { \dot { \mathrm { d } . ~ s } ^ { W S } = p ( h - l ) - \delta _ { l } ~ i f \Psi _ { N - 2 } > t > \Phi _ { N - 1 } } \end{array}$ and $0 < p \leq$ $1 / N ;$ $\mathrm { ~ e . ~ } s ^ { W S } = ( t - \Theta _ { N - 1 } ) / ( \overline { { p } } ) ^ { N - 1 } i f \Phi _ { N - 1 } > t > \Theta _ { N - 1 } ; a$ and f. otherwise, $s ^ { W S } = 0$

## 6.2. Comparison Between AS and WS

Compared with AS, the advantage of WS is that the platform can intensify the competition to a greater degree. However, the effective subsidy upper bound limits the platform’s ability to induce more informed advertisers. Because WS and AS have distinct advantages, it is interesting and meaningful to compare the platform’s net revenues under AS and WS.

Theorem 5. When $\delta _ { l } \geq p ( h - l )$ , AS can achieve at least the same net revenue as WS.

When $\delta _ { l } \geq p ( h - l ) .$ , because of the effective subsidy upbound, the platform does not provide any subsidies under WS. However, under ${ \mathrm { A S } } ,$ the platform may be able to increase its net revenue through the provision of subsidies. Thus, AS is always (weakly) better than WS. On the contrary, when $\delta _ { l } < p ( h - l )$ , either WS or AS can be the better framework. Proposition 4 summarizes the comparison results between AS and WS. The detailed results are provided in the proof of Proposition 4 in the Online Appendix. When t is large, AS dominates WS because more than one advertiser remains uninformed after the subsidy provision. Thus, the competition under AS is fierce, diminishing the advantage of WS.

Proposition 4. Suppose $\delta _ { l } < p ( h - l )$ . When $t \geq \Psi _ { N - 3 } ,$ AS (weakly) dominates WS. Otherwise, which mechanism is better depends on the distributions of impression values and the number of advertisers.

We next analyze how the number of advertisers affects the selection between AS and WS. Proposition 4 implies that as N increases, the data cost range such that WS may be better than AS $( { \mathrm { i . e . , ~ } } \Theta _ { N - 1 } < t < \Psi _ { N - 3 } )$ decreases. Generally speaking, as the number of advertisers increases, the intensity of competition also increases.

Because there is less room to intensify the competition further, the advantage of WS decreases. Thus, AS is more likely to be better than WS as the number of advertisers increases.

To illustrate the comparison between AS and WS when $t < \Psi _ { N - 3 . }$ , we look at Figure 4, which visualizes the comparison results between ${ \mathrm { A S } }$ and WS when $N =$ 2 and $\delta _ { h } = \delta _ { l } = \delta$ . Notice that when $N = 2 ,$ , whenever the platform provides subsidies, it falls in the case $t < \Psi _ { N - 3 }$ . In Figure $^ { 4 , }$ the high-cost region refers to the data cost such that no one acquires data without subsidies. The low-cost region refers to the data cost at which both advertisers acquire data without subsidies. We have shown that the platform should not provide subsidies in these regions. Thus, we focus on the intermediate-cost region.

First, WS tends to be better than AS when δ is not very large. Recall that the shortcoming of WS is the upbound on the effective subsidy amount $( \mathrm { i . e . , }$ $\displaystyle p ( h - l ) - \delta )$ . When δ is large, this upbound is small. The intuition is as follows. When the ad selection effect is larger, informed advertisers bid higher values; hence, even with a low subsidy, informed advertisers always outbid uninformed advertisers. Thus, the disadvantage of WS becomes more significant, and it is more likely for AS to be better than WS.

Besides, WS tends to be better than AS when the data cost is close to the lower bound of the intermediate-cost region. In this case, no matter whether under AS or WS, the platform uses subsidies to induce two advertisers to acquire data. Because the number of informed advertisers is the same, the levels of ad fit are the same under the two frameworks. However, informed advertisers bid higher under WS, leading to more intense competition and a higher impression price.

When the data cost is close to the upper bound of the intermediate-cost region, WS is also more likely to be better than AS. However, this only happens when the probability of $\boldsymbol { \psi } _ { i } = 1 \ ( \mathrm { i . e . , } p )$ is small. When t is large, a large subsidy is required to induce additional informed advertisers. In this case, the platform does not provide subsidies under AS because the subsidy amount is larger than the extracted surplus. However, the platform may provide a subsidy under WS. Because the competition is more intense under WS, the platform may extract more surplus under WS, and such a surplus may be larger than the subsidy.

WS can increase the competition intensity more than AS because it increases the bids of informed advertisers. This is more likely to happen when p is small. For instance, suppose advertiser 1 acquires data, whereas advertiser 2 does not acquire it. If advertiser 1 has a valuation $h + \delta _ { h } ,$ , she bids $h + \delta _ { h } + s$ and wins the impression. Regardless of the value of $s ,$ her payment for the impression is always ph + pl. If advertiser 1 has a valuation $l + \delta _ { l } ,$ advertiser 2 wins the auction and pays $l + \delta _ { l } + s$ . The payment increases with the subsidy. In a nutshell, the increase in the bids of informed advertisers is more likely to increase the impression price when their bids are low. That is why WS has a more significant advantage when p is small.

## 7. Extensions

This section analyzes three extensions: (1) advertisers have heterogeneous targeting abilities, (2) impressions are sold through first-price auctions, and (3) there are variations in the quality of data. In this section, we restrict our analysis to the case of $\delta _ { l } \leq p ( h - l )$

## 7.1. Advertisers with Heterogeneous Targeting Abilities

Although the benefit of targeting has been widely acknowledged, some advertisers cannot do it because they lack the expertise to turn data into actionable targeting strategies (Milenkovic 2019). Traditional and sophisticated advertisers may compete for the same impression, especially in open auctions where many advertisers participate. In this section, we assume that in addition to the N advertisers, there is another group (more than two) of traditional advertisers in the auction.

Figure 4. (Color online) Comparison Between AS and WS $( h = 8 , l = 4 , N = 2 , \delta < p ( h - l ) )$  
![](/api/attachments/2R8G9AJN/fulltext/images/412ae248bd134ee1ccfc8a004a84e561986725eec6cc2ef13ec3795e2fa6688c.jpg)  
(a)  
Notes. (a) $p = 1 / 4 . \left( \mathrm { b } \right) p = 3 / 4 .$

(b)  
![](/api/attachments/2R8G9AJN/fulltext/images/7cae153be12e26c670e40c08da24392b40fe650c8b6400a7da44c9bcab13b2b5.jpg)

In this section, we analyze how the heterogeneity in advertisers’ targeting abilities affects the optimal subsidy under AS and WS. We use the superscript $^ { \prime \prime } \mathrm { H } ^ { \prime \prime }$ to denote the model with both advertisers. To begin, we assume that $\delta _ { h } = \delta _ { l } = 0$ . The optimal subsidy under AS is given by

$$
s ^ {\text { H,AS }} = \left\{ \begin{array}{l l} t - \Psi_ {m}, & \text { if } \frac {\Psi_ {m - 1} (m + \overline {{p}})}{m + 1} > t > \Psi_ {m}, \\ 0, & \text { otherwise }, \end{array} \right.\tag{16}
$$

where $m \in \{ 1 , 2 , \ldots , N - 1 \}$ . The literature (Table 3) finds that if only two advertisers acquire data, the impression price decreases because competition attenuates. Thus, the subsidy provision cannot increase the platform’s net revenue. Our previous analysis has shown that the ad selection effect can reverse this result, making subsidy provisions profitable for the platform in this case. Equation (16) now suggests that with only two sophisticated advertisers and no ad selection effects, the platform should provide a subsidy when $p \overline { { { p } } } ( 1 - \textstyle \frac { p } { 2 } ) ( h - l ) > t >$ $p ( \overline { { p } } ) ^ { 2 } ( h - l )$ . Therefore, the presence of traditional advertisers is another factor that may reverse previous findings in the literature and make subsidy provisions beneficial for platforms.

Bid selection attenuates advertisers’ competition because some informed advertisers may find that the impression value is low and decrease their bids. However, in the presence of traditional advertisers, low bids from these informed advertisers are outbid and no longer affect the impression price. Therefore, bid selection does not attenuate the competition. As a result, the impression increases with data acquisition, even in the absence of ad selection.

We next analyze the WS framework. The optimal subsidy under WS $( s ^ { \mathrm { H } , \mathrm { \Delta W S } } )$ is given by

$$
s ^ {\text { H,WS }} = \left\{ \begin{array}{l l} \frac {t - \Psi_ {m}}{p (\overline {{p}}) ^ {m}}, & \text { if } \frac {\Psi_ {m - 1} (m + \overline {{p}})}{m + 1} > t > \Psi_ {m}, \\ 0, & \text { otherwise }. \end{array} \right.\tag{17}
$$

By comparing $s ^ { \mathrm { H } , \mathrm { A } S }$ and $s ^ { \mathrm { H } , \ W S }$ , we observe that the platform provides a subsidy under WS whenever it does that under AS. We can further derive that the platform’s net revenue is $( \overline { { { p } } } ) ^ { m + 1 } ( p h + \overline { { { p } } } l ) + ( 1 - ( \overline { { { p } } } ) ^ { m + 1 } ) h -$ (m + 1)t under $s ^ { \mathrm { H } , \mathrm { A S } }$ and $s ^ { \mathrm { H } , \mathrm { W S } }$ . Thus, AS and WS are equivalent in terms of the platform’s net revenue.

Because of traditional advertisers, any uninformed advertiser gets a zero payoff. If the platform wants to induce advertisers to acquire data, it provides a subsidy that makes them indifferent between acquiring and not acquiring data. Thus, the payoff of an induced informed advertiser remains zero. By symmetry of all informed advertisers, we have that under the optimal subsidy $s ^ { \mathrm { H } , \mathrm { A } S }$ , all informed advertisers have zero payoffs. This implies that the intensity of competition under AS is extremely fierce. The platform cannot further intensify competition by using WS over AS. Thus, the advantage of WS diminishes. Besides, when $\delta _ { h } =$ $\delta _ { l } = 0 ,$ , s ˜ is relatively large and does not put a constraint on the optimal subsidy under WS. The disadvantage of WS diminishes. Hence, WS and AS become equivalent.

We next assume that $\delta _ { h } > 0$ and $\delta _ { l } > 0$ . The optimal subsidy under AS is not changed, and the optimal subsidy under WS is given by Equation (18):

$$
s ^ {\text { H,WS }} = \left\{ \begin{array}{l l} \frac {t - \Psi_ {m}}{p (\overline {{p}}) ^ {m}}, & \text { if   } \min \left(\frac {\Psi_ {m - 1} (m + \overline {{p}})}{m + 1}, \Phi_ {m}\right) > t > \Psi_ {m}, \\ 0, & \text { otherwise }. \end{array} \right.\tag{18}
$$

We can observe that the range of $t ,$ wherein the platform is willing to offer subsidies, is narrower under WS than AS. Further analysis of the platform’s net revenue shows that in the presence of traditional advertisers, the net revenue under WS is always (weakly) less than that under AS.

Proposition 5. If $\because \Psi _ { m - 1 } ( m + \overline { { p } } ) / ( m + 1 ) > t > \Phi _ { m } ,$ AS is better than WS. Otherwise, AS achieves the same net revenue as WS.

Similar to the previous case, advertisers’ competition under AS is extremely fierce, and the advantage of WS diminishes. Besides, $\delta _ { h }$ and $\delta _ { l }$ are greater than zero in this case, and s ˜ becomes smaller. Because of the constraint of the effective subsidy upbound, WS cannot consistently achieve a net revenue as good as AS.

## 7.2. First-Price Auction

Platforms may use first-price auctions to sell impressions. In this section, we revisit the previous findings when the impression is sold through first-price auctions. To start with, we investigate the optimal subsidy under the FPA with an all-subsidized mechanism. We first derive the equilibrium bidding strategy in stage 3. Because we consider a first-price auction with discrete valuation distributions, there may not exist a purestrategy equilibrium in bidding. Following the literature $( \mathrm { e . g . }$ , Maskin and Riley 2003), we consider mixed bidding strategies for advertisers. Because of the page limitation, the equilibrium bidding strategy is given in Lemma EC.4 in the Online Appendix. The main difference between the bidding strategies under FPA and SPA is that an advertiser’s bid under FPA is (weakly) lower than SPA on average.

We next turn to the value of data acquisition to advertisers, which is defined as the increase in the payoff after an advertiser acquires data. Lemma 3 compares the value of data acquisition to advertisers under two auction formats and the impact of auction formats on the impression price.

Lemma 3. Given that advertisers 1 to m have acquired data, we have the following.

1. $D V _ { m }$ under FPA is (weakly) larger than $D V _ { m }$ under SPA.

2. The expected impression price under FPA is (weakly) lower than that under SPA.

Compared with SPA, the data value is higher under FPA, implying that advertisers have stronger incentives to acquire data under FPA. This is because bids are lower on average under FPA, leading to attenuated competitions. Thus, data acquisition brings larger benefits to advertisers. Lower bids also lead to a (weakly) lower impression price under FPA. The well-known revenue equivalence theorem states that SPA and FPA result in the same revenue for the auctioneer when all bidders are ex ante symmetric (Krishna 2010).<sup>5</sup> This suggests the platforms are unlikely to experience a significant profit loss when they switch from SPA to FPA. However, because of advertisers’ different decisions on data acquisition, advertisers are not symmetrical in the auction period. Therefore, the revenue equivalence theorem may not hold in our context, although advertisers are ex ante at the beginning of the game. Our results suggest that FPA may lead to a lower impression price when advertisers can acquire data for targeting.

Theorem 6. The optimal subsidy under FPA-AS is summarized as follows:

a. $s ^ { F P A , A S } = t - \Psi _ { m } i f \Psi _ { m - 1 } ( m + \overline { { p } } ) / ( m + 1 ) > t > \Psi _ { m } ,$ where m is an integer between 1 and $N - 3 ;$

b. $s ^ { F P A , A S } = t - \Omega _ { 4 } i f \Omega _ { 3 } > t > \Omega _ { 4 }$ and $\Delta _ { 3 } > 0 ;$

c. $s ^ { F P A , A S } = t - \Theta _ { N - 1 } \mathrm { ~ } i f \Omega _ { 5 } + ( 1 - p / N ) \Theta _ { N - 2 } > t > \Theta _ { N - 1 } ;$ and

d. otherwise, $s ^ { F P A , A S } = 0 .$

Besides, the platform’s revenue under FPA-AS is (weakly) lower than that under $S P A { - } A S .$

By comparing the subsidies under FPA-AS and SPA-AS, we can see that the optimal subsidies are the same under the two auction formats in most cases except for an intermediate data cost. When the cost is low, al advertisers acquire data naturally, or the optimal subsidy makes all advertisers acquire data under both auction formats. Thus, all advertisers are symmetrical, and two auction formats are equivalent. When the data cost is high, many advertisers do not acquire data, leading to fierce competition among advertisers. When the competition intensity is high, FPA and SPA do not make a big difference to the auction outcome.

When the data cost is intermediate, the optimal subsidy under FPA may be larger than SPA because the impression price without subsidies is lower under FPA, and the platform has more incentives to subsidize advertisers. However, higher data values on FPA may decrease the required subsidy to induce data acquisition relative to SPA. Thus, we have mixed results on the relationship between the optimal subsidies under the two auction formats. As for the net revenues, it is similar to the comparison of impression prices in Lemma 3. SPA-AS leads to a net revenue that is not less than that under FPA-AS because the intensity of competition and the allocation efficiency under FPA are lower.

Next, we look at the LS and AS mechanisms under FPA. As for LS, Theorem 3 still holds. We can always find a subsidy under AS that leads to the same number of informed advertisers under the optimal subsidy of LS. However, advertisers bid lower under LS, leading to a lower impression price. As for FPA-WS, the optimal subsidy is summarized as follows:

$s ^ { \mathrm { F P A , W S } } = ( t - \Psi _ { m } ) / ( p ( \overline { { p } } ) ^ { m } )$ if min $( \Psi _ { m - 1 } ( m + \overline { { p } } ) / ( m$ $+ 1 ) , \Phi _ { m } ) > t > \Psi _ { m } ,$ , where $1 \leq m \leq N - 3 ;$ $\bullet s ^ { \mathrm { F P A , W S } } = ( t - \Omega _ { 4 } ) / ( d \Omega _ { 4 } ^ { \mathrm { F P A } } / d s )$ if min $\left( \Omega _ { 6 } , \Phi _ { N - 2 } \right) >$ $t > \Omega _ { 4 } \mathrm { a n d } \Delta _ { 4 } < 0 ;$

$$
s ^ {\text { FPA,WS }} = p (h - l) - \delta_ {l} \text {   if   } \Phi_ {N - 2} > t > \Omega_ {4}, \Delta_ {2} > 0,
$$

$$
\Delta_ {4} > 0;
$$

$$
s ^ {\text { FPA,WS }} = p (h - l) - \delta_ {l} \text {   if   } \Omega_ {4} > t > \Phi_ {N - 1}
$$

$$
\Delta_ {4} > 0;
$$

$$
s ^ {\mathrm{FPA,WS}} = (t - \Theta_ {N - 1}) / (\overline {{p}}) ^ {N - 1} \mathrm{if} \Phi_ {N - 1} > t > \Theta_ {N - 1};
$$

$$
s ^ {\mathrm{FPA,WS}} = 0
$$

Here, $\Omega _ { 6 }$ is the value that makes the platform’s net revenue when the subsidy is $( \Omega _ { 6 } - \dot { \Omega _ { 4 } } ) / ( d \Omega _ { 4 } ^ { \mathrm { F P A } } / d s )$ the same as that before the subsidy provision. Besides, $\Delta _ { 4 } = d S ^ { \mathrm { F P A } } / d s + ( 1 - p ) ^ { N - 1 } + ( d \Omega _ { 4 } ^ { \mathrm { F P A } } / \acute { d } s ) .$ , where $S ^ { \mathrm { F P A } }$ is given by Equation (EC.41) in the Online Appendix.

Comparing this result with that under SPA-WS, we can see that the optimal subsidy under FPA-WS is the same as that under WS-SPA in most cases. Besides, similar to AS, the platform’s net revenue is weakly smaller under FPA-WS than under SPA-WS. To sum marize, in most cases, the choice between FPA and SPA does not make a big difference in the performance of the three subsidy mechanisms. However, under a certain range of t, FPA can be inferior to SPA, no matter whether AS or WS is used.

## 7.3. Variation in Data Quality

So far, we assume the quality of targeting data is the same across different advertisers. In practice, there may be variations in data quality. Such variations can result in the heterogeneity of advertisers in terms of $\delta _ { h }$ and $\delta _ { l } .$ . This section investigates how this heterogeneity affects the subsidy mechanisms. Suppose the data quality may be accurate or inaccurate. If the data acquired by an advertiser is accurate, the ad selection improvements are $\delta _ { h } ^ { \mathrm { A } }$ and $\delta _ { l } ^ { \mathrm { A } }$ . If the data are inaccurate, the ad selection improvements are $\delta _ { h } ^ { I }$ and $\delta _ { l } ^ { I } ,$ where $\delta _ { h } ^ { \mathrm { A } } > \delta _ { h } ^ { I }$ and $\delta _ { l } ^ { \mathrm { A } } > \delta _ { l } ^ { I }$ . Data quality is private information. Each advertiser knows the quality of her data but does not know the quality of other advertisers’ data. Suppose a fraction q of advertisers can acquire accurate data; q is public knowledge. Besides, we assume ph + $( 1 - p ) \dot { l } > \hat { l } + \delta _ { l } ^ { \mathrm { A } }$ (i.e., the low value is less than the dataabsent average, regardless of the data quality).

The variation in data qualities leads to a game with incomplete information. The action space of each advertiser includes three possible strategies: (a) do not acquire data regardless of the data quality, (b) acquire data only when it is accurate, and (c) acquire data regardless of the quality. Depending on the parameters, the equilibria can change dramatically, and it is very hard to find the general expression of the optimal subsidy. Section EC.7.3 in the Online Appendix discusses a general process to solve this optimization problem. Because we are interested in whether the previous findings are robust to the heterogeneity in data quality, we focus on a case wherein the heterogeneity is sufficiently significant (i.e., when $\delta _ { h } ^ { \mathrm { A } } - \delta _ { h } ^ { I } > \chi .$ , where $\chi$ is defined in Section EC.7.3 in the Online Appendix).

Because of the page limitation, the optimal subsidy is given in Table EC.9 in the Online Appendix. By comparing the optimal subsidy in Table EC.9 in the Online Appendix with Theorem 1, we can see that the heterogeneity in data qualities and ad selection improvements does not affect the qualitative relationship between the optimal subsidy and the parameters. The range of t wherein the optimal subsidy is positive is still a set of disconnected intervals. Similar to the main model, as t decreases, advertisers pay less for the data acquisition and have higher payoffs. However, a lower data cost also increases the number of informed advertisers, intensifying the competition. Thus, the provision of subsidies can increase the net revenue only when the first impact plays a dominant role.

Next, we turn to the other two mechanisms. The LS mechanism is still inferior to the AS mechanism because of the decrease in the bids and the resulting competition attenuation. As for the WS mechanism, Proposition 6 compares its performance with the AS mechanism.

Proposition 6. When $t \geq p ( 1 - p q ) ^ { N - 2 } ( \delta _ { h } ^ { A } - \delta _ { l } ^ { A } + h - l ) ,$ AS (weakly) dominates WS. Otherwise, which mechanism is better depends on the distributions of impression values, the number of advertisers, and the fraction of advertisers with accurate data.

The properties of the results in this case are similar to Proposition 4 in the main model. For example, AS tends to be better than WS when the data cost is relatively high, and most advertisers do not acquire data. Besides, the range where WS may be better than AS diminishes as N increases. Further, $p ( 1 - p q ) ^ { N - 2 } ( \delta _ { h } ^ { A } -$ $\delta _ { l } ^ { A } + h - l )$ decreases with $\delta _ { l } ^ { \mathrm { A } }$ , implying an increasing advantage of AS similar to Figure 4. This is because a larger $\delta _ { l } ^ { \mathrm { K } }$ reduces the effective subsidy upbound under WS. To summarize, the heterogeneity in data qualities can lead to more complications in advertisers’ decisions. However, this does not qualitatively affect the optimal subsidy amount and the comparison between mechanisms.

## 8. Discussion and Conclusion

Online advertising relies on targeted ads customized to user preferences. Advertisers often need to acquire additional data from data providers for better targeting. Although previous research has investigated the impact of platform-released data on net revenue, little is known about the platform’s active role when advertisers acquire data by themselves. Our study aims to address this gap. We explore how platforms can benefit by subsidizing advertisers to acquire additional data.

We examine the AS framework and find that platforms benefit from subsidizing advertisers, especially when it boosts competition. Next, we analyze the LS framework and demonstrate that it cannot generate a net revenue larger than that of AS. This is because sophisticated advertisers lower their bids under LS, resulting in weakened competition. In our study, we propose the WS framework as a third option. Our results indicate that WS leads to higher advertiser bids and intensifies competition more than AS. However, the platform’s ability to attract more informed advertisers is relatively limited under WS compared with AS. Our analysis shows that the choice between WS and AS depends on factors, such as the number of advertisers, the magnitude of ad selection improvements, and the targeting ability of advertisers.

## 8.1. Managerial Implications

Our analysis has several implications. First, platforms are increasingly collaborating with data providers to facilitate advertisers’ data acquisition. In this process, platforms absorb some expenses associated with data integration, which were previously borne by advertisers. Thus, advertisers could acquire additional data at lower costs. This rising trend stems from various factors, including the belief that improved targeting leads to higher impression prices and the imperative of addressing privacy concerns. Using a stylized model, we gain insight into when it is profitable for platforms to subsidize advertisers’ data acquisition. The platform benefits from the subsidy provision only when the competition intensity is significantly increased after more advertisers are induced to acquire data.

Second, our findings draw attention to the importance of the ad selection effect in its role in increasing competition intensity. Although it is common for advertisers to have multiple ads, the influence of ad selection remains relatively unexplored. Our results imply that enhanced ad selection not only improves the alignment between ads and users but also, intensifies the competition among advertisers. This finding underscores the potential pitfalls of disregarding ad selection in the subsidy provision decision. A platform that fails to consider ad selection may provide the subsidy when it hurts the profit or withhold it when it could increase the profit.

Because of the significant role of the ad selection effect, it is crucial for platforms to estimate the potential improvement in their advertisers’ ad selections with additional data. Platforms could enhance the quality of this estimation by acquiring information regarding the number of ads that each advertiser possesses and the diversity of these ads concerning targeting segments and advertising returns. This implication can also extend to other contexts related to targeted advertising, such as the precision of basic data that a platform should release. Overall, platforms could benefit from integrating additional information to estimate the ad selection effect and enhance decision making.

Third, past years have witnessed a shift from second-price auctions to first-price auctions in RTB. The benefits of the first-price auction include falsename proofness, transparency, easy implementation with header bidding, and others (Despotakis et al. 2021, Conitzer et al. 2022). Given that, in most scenarios, the first-price auction generates the same revenue for the auctioneer as the second-price auction, concerns regarding revenue loss for platforms are alleviated (Krishna 2010, Despotakis et al. 2021). However, we show that because of the asymmetry that advertisers make different data acquisition decisions, the firstprice auction could result in a lower impression price compared with the second-price auction. The possibility of this profit loss could provide another rationale for the continued prevalence of second-price auctions in the industry (Despotakis et al. 2021, Tunuguntla and Hoban 2021). When a platform is estimating whether it is worth shifting to the first-price auction, such a loss in profit should be considered carefully. From a broader perspective, given the substantial influence of the data market on RTB outcomes, it is imperative for platforms to consider the impact of the data market when making any changes to platform design.

Finally, our study also has implications for social planners. Our analysis of advertisers’ payoffs reveals that subsidies lead to intensified competition primarily among naturally informed advertisers that acquire data without subsidies. After subsidies are provided, advertisers that remain uninformed may face less intense competition and have higher payoffs. This suggests that subsidies can end up being a tax on the wealthy as naturally informed advertisers tend to be big firms, and social planners should encourage the involvement of platforms in advertisers’ data acquisition.

In the past years, various regulations have been rolled out to set the legal requirements on the market for additional data. On the user side, these regulations protect their privacy. However, when looking at the impact of these regulations on the advertiser side, they add to the difficulty of acquiring high-quality addi tional data. Wernerfelt et al. (2023) suggests that these regulations make it harder “for smaller advertisers to acquire new customers and compete with incumbent firms. That could have implications for entry into the market, and it could ultimately have downstream negative consequences for consumers if that leads to less variety and higher prices.” As a tax on the wealthy, subsidy provision can help with the development of small advertisers, preventing them from being squeezed out because of the disadvantages caused by data regulations. This fosters a healthy market environment that could ultimately enhance user payoffs. Besides, as the platforms get involved in the acquisition and activation of additional data, more privacy-safe targeting technol ogies could be developed (Wu 2023).

## 8.2. Limitations and Future Research

Although our study contributes to understanding the subsidy problem in the context of data acquisition for targeted advertising, it is important to acknowledge its limitations. First, we focus on the role of additional targeting data to improve ad selection and bid selection. However, additional data rely on the basic data to improve targeting. Future research could explore the platform’s decision of how basic data must be configured to leverage the targeting benefit of additional data.

Second, we assume that advertisers make data acquisition decisions before observing user data from the platform. However, advertisers may make these decisions in real time after seeing the basic data. Examining the subsidy problem in this context is another meaningful direction for future research. Overall, although our study sheds light on the subsidy problem in the context of data acquisition for targeted advertising, there are several avenues for further exploration that can enhance our understanding of this complex issue.

## Endnotes

<sup>1</sup> See https://www.oracle.com/cx/marketing/data-managementplatform/what-is-dmp.

<sup>2</sup> See https://www.lotame.com/partner-connections.

<sup>3</sup> See https://pubmatic.com/auction-packages/us.

<sup>4</sup> See https://pubmatic.com/legal/demand-service-agreement.

## References

Amaldoss W, Jerath K, Sayedi A (2016) Keyword management costs and “broad match” in sponsored search advertising. Marketing Sci. 35(2):259–274.

Chen J, Stallaert J (2014) An economic analysis of online advertising using behavioral targeting. MIS Quart. 38(2):429–450.

Christopher RM, Park S, Han SP, Kim MK (2022) Bypassing performance optimizers of real time bidding systems in display ad valuation. Inform. Systems Res. 33(2):399–412.

Conitzer V, Kroer C, Panigrahi D, Schrijvers O, Stier-Moses NE, Sodomka E, Wilkens CA (2022) Pacing equilibrium in first price auction markets. Management Sci. 68(12):8515–8535.

De Corniere A, De Nijs R (2016) Online advertising and privacy. RAND J. Econom. 47(1):48–72.

Despotakis S, Ravi R, Sayedi A (2021) First-price auctions in online display advertising. J. Marketing Res. 58(5):888–907.

eMarketer (2019) US real-time bidding (RTB) digital display ad spending, by segment, 2015–2021 (billions). Accessed June 20, 2022, https://www.emarketer.com/chart/228035/us-real-timebidding-rtb-digital-display-ad-spending-by-segment-2015-2021- billions.

Ganuza JJ (2004) Ignorance promotes competition: An auction model with endogenous private valuations. RAND J. Econom. 35(3):583–598.

Ganuza J, Penalva JS (2010) Signal orderings based on dispersion and the supply of private information in auctions. Econometrica 78(3):1007–1030.

Golrezaei N, Nazerzadeh H (2016) Auctions with dynamic costly information acquisition. Oper. Res. 65(1):130–144.

Hendricks D (2017) Why behavioral analytics is your company’s secret weapon. Accessed June 20, 2022, https://www.inc.com/ drew-hendricks/why-behavioral-analytics-is-your-companyssecret-weapon.html.

Hummel P, McAfee RP (2016) When does improved targeting increase revenue? ACM Trans. Econom. Comput. 5(1):1–29.

IAB (2021) Video ad spend 2020 & outlook for 2021. Accessed June 20, 2022, https://www.iab.com/insights/2020-digital-video-adspend-report.

IAB (2022) Digital advertising soared 35% to \$189 billion in 2021 according to the IAB internet advertising revenue report. Accessed June 20, 2022, https://www.iab.com/news/digital advertising-soared-35-to-189-billion-in-2021-according-to-the-iabinternet-advertising-revenue-report.

IAB, Ipsos (2022) State of data 2022: The measurement dilemma. Accessed April 15, 2024, https://www.iab.com/wp-content uploads/2022/02/IAB\_State\_of\_Data\_2022\_Master.pdf.

Krishna V (2010) Auction Theory, 2nd ed. (Elsevier, Amsterdam).

Levin J, Milgrom P (2010) Online advertising: Heterogeneity and conflation in market design. Amer. Econom. Rev. 100(2): 603–607.

Maskin E, Riley J (2003) Uniqueness of equilibrium in sealed highbid auctions. Games Econom. Behav. 45(2):395–409.

Milenkovic M (2019) The 45 most important advertising statistics of 2020. Accessed June 20, 2022, https://www.smallbizgenius.net/ by-the-numbers/advertising-statistics

Pubmatic, Inc. (2021) The media buyer’s guide to impactful auction packages. Accessed March 15, 2024, https://pubmatic.com/wpcontent/uploads/2021/12/The-Media-Buyers-Guide-to-Impact ful-Auction-Packages-12162021.pdf.

Rafieian O, Yoganarasimhan H (2021) Targeting and privacy in mobile advertising. Marketing Sci. 40(2):193–218

Sayedi A (2018) Real-time bidding in online display advertising. Marketing Sci. 37(4):553–568.

Schoen M (2021) Three strategies for improving your marketing analytics. Forbes (November 15), https://www.forbes.com/sites/ forbescommunicationscouncil/2021/11/09/three-strategies-for improving-your-marketing-analytics.

Shi X (2012) Optimal auctions with information acquisition. Games Econom. Behav. 74(2):666–686.

Sluis S (2020) Pubmatic’s audience encore makes it easier to use publisher first-party data. Accessed February 15, 2024, https:// www.adexchanger.com/platforms/pubmatics-audience-encore makes-it-easier-to-use-publisher-first-party-data.

Starita L (2019) How does a data management platform work? Gartner (November 20), https://www.gartner.com/en/marketing insights/articles/how-does-a-data-management-platform-work.

Sun Z, Dawande M, Janakiraman G, Mookerjee VS (2016) The mak ing of a good impression: Information hiding in ad exchanges. MIS Quart. 40(3):717–739.

Taparia N (2020) 3 ways small business retail can survive and thrive with technology. Forbes (December 9), https://www.forbes.com sites/nealtaparia/2020/12/09/3-ways-small-business-retail-cansurvive-and-thrive-with-technology.

Tunuguntla S, Hoban PR (2021) A near-optimal bidding strategy for real-time display advertising auctions. J. Marketing Res. 58(1):1–21.

Walter G (2021) First-party data will reign supreme for marketers in 2021. Forbes (January 13), https://www.forbes.com/sites/forbes techcouncil/2021/01/13/first-party-data-will-reign-supreme-formarketers-in-2021.

Wernerfelt N, Tuchman A, Shapiro B, Moakler R (2023) As data privacy improves, small advertisers could get squeezed. Accessed April 15, 2024, https://insight.kellogg.northwestern.edu/article as-data-privacy-improves-small-advertisers-could-get-squeezed.

Wu S (2023) Why sell-side targeting solutions matters now more than ever. Accessed April 15, 2024, https://pubmatic.com/ blog/why-sell-side-targeting-matters-now-more-than-ever.

Yao S, Mela CF (2011) A dynamic model of sponsored search adver tising. Marketing Sci. 30(3):447–468

Ye L (2007) Indicative bidding and a theory of two-stage auctions. Games Econom. Behav. 58(1):181–207.

Zawadzin´ski M, Sweeney M (2022) The AdTech book: The platforms, processes, and players that make up the digital advertising industry. Accessed February 10, 2023, https://adtechbook. clearcode.cc.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.
