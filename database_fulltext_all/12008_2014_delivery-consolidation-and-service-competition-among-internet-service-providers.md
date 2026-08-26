---
otero_id: 12008
otero_key: "B4NSYJB2"
title: "Delivery Consolidation and Service Competition Among Internet Service Providers"
authors: "I. Robert Chiang; Jhih-Hua Jhang-Li"
year: "2014"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2014.995561"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/B4NSYJB2/fulltext/images/a50ad335e306d207adda28b03352710b9a343350636fcc604e4b58b6335ea10a.jpg)

# Journal of Management Information Systems

Publication details, including instructions for authors and subscription information: http://www.tandfonline.com/loi/mmis20

# Delivery Consolidation and Service Competition Among Internet Service Providers

I. Robert Chiang & Jhih-Hua Jhang-Li Published online: 09 Mar 2015.

![](/api/attachments/B4NSYJB2/fulltext/images/3b2826ea5c830d73a0ac5ea4c0e1839279d0485c92ebd0489615168cec2edba4.jpg)

Click for updates

To cite this article: I. Robert Chiang & Jhih-Hua Jhang-Li (2014) Delivery Consolidation and Service Competition Among Internet Service Providers, Journal of Management Information Systems, 31:3, 254-286, DOI: 10.1080/07421222.2014.995561

To link to this article: http://dx.doi.org/10.1080/07421222.2014.995561

## PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the “Content”) contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms &

Conditions of access and use can be found at http://www.tandfonline.com/page/termsand-conditions

# Delivery Consolidation and Service Competition Among Internet Service Providers

I. ROBERT CHIANG AND JHIH-HUA JHANG-LI

I. ROBERT CHIANG is an associate professor of information systems at the Gabelli School of Business, Fordham University. He holds a Ph.D. in information systems from the University of Washington. His research interests are in IT portfolio and project management, information systems economics, and e-business strategy and design. His prior work has appeared in Communications of the ACM, Decision Support Systems, IEEE Transactions on Software Engineering, Information Systems Research, Information Technology and Management, INFORMS Journal on Computing, and Operations Research, among others.

JHIH-HUA JHANG-LI is an assistant professor in the Department of Information Management at Hsing Wu University, Taiwan. He received his B.S. degree in computer science and information engineering from the National Chung Cheng University and M.S. and Ph.D. degrees in information management from the National Chiao Tung University, Taiwan. His research interests include information systems strategy, economics of information systems, and e-business. His work has appeared in Decision Sciences, European Journal of Operational Research, and Information Technology and Management, among others.

ABSTRACT: The infrastructure of the Internet, by and large, is maintained by Internet service providers (ISPs) that cater to regional customers and by Internet backbone providers (IBPs) that serve large organizations and ISPs. Some IBPs have recently branched into content delivery network (CDN) services; separately, other ISPs have started offering on-demand video streaming to compete with pure-play content providers. These developments have intensified the competition in both content delivery and media-streaming markets. For the content delivery market, we study the competition equilibriums by analyzing factors such as market share, cost structure, service pricing, and subscriber preference. Our approach helps identify conditions under which a content provider should choose an IBP over the incumbent CDN for content distribution. We also show how an IBP’s CDN venture affects its interconnection relationship with ISPs. For the streaming service market, we examine conditions under which a content provider would partner with an ISP to lower operating and marketing costs while providing a more streamlined subscriber experience. Analytically, our game-theoretical models can optimize key contracting and pricing strategies for multiple classes of service providers; empirically, insights derived from the proposed models have anticipated events that coincide with several recent developments in content delivery and streaming service markets.

KEY WORDS AND PHRASES: content delivery network, Internet service provider, media streaming, peering and transit, service pricing.

The infrastructure of the modern-day Internet is a complex coalition of IP-based networks managed by two classes of “delivery” providers: Internet service providers (ISPs) and Internet backbone providers (IBPs), as shown in Figure 1. Although there is not a strict delineation between the two classes, ISPs generally operate in regional markets for retail customers, whereas IBPs, including the wholesale side of major telephone companies (telcos), maintain long-haul routes serving institutional clients and ISPs. Given that the Internet’s promise of global reach can be fulfilled only if customers from different providers can properly interact, it is of significant importance to investigate the incentive and economic issues surrounding network interconnection.

An interconnection agreement generally falls into one of two types: transit or peering. In transit agreements, one party (likely a regional ISP) pays the other (likely an IBP) to gain access to the rest of the Internet. In contrast, peering agreements, de facto among IBPs, are now gaining popularity among ISPs to swap traffic with “equals.” Under settlement-free (or regular) peering, both parties reciprocally terminate traffic (i.e., packets not relayed further) [39] without monetary exchanges. Settlement-free peering is thus more likely when the traffic flows stay relatively symmetric [36]. As an example, one $\mathrm { I B P ^ { 1 } }$ states that “the ratio of aggregate amount of traffic exchanged shall be roughly balanced and shall not exceed 1.8:1.” A paid peering is similar to its settlement-free counterpart, except that one side incurs transport or facility costs, or both. Not surprisingly, sometimes a provider demands more favorable peering $\mathrm { t e r m s } ^ { 2 }$ or switches to paid interconnection. Two networks may also agree to treat part of the traffic exchanged as “transited” and the rest as “peered.”

![](/api/attachments/B4NSYJB2/fulltext/images/af0db3e7d301861b4d80791325b119ab0dcae39493960c3a100dea289ac61123.jpg)  
Figure 1. Internet Providers

During the nascent era of the commercial Internet, overhyped traffic projections fueled the frenzied build-out of national and intercontinental backbones. The ensued reality, however, was one of glutted debts, unlit fibers, and diminished IBP roles.<sup>3</sup> The situation has been exacerbated by “doughnut peering” among ISPs to bypass backbones whenever feasible. Even though the recent proliferation of bandwidthintensive services, such as cloud computing and media streaming, has significantly increased utilization of the Internet backbone, IBPs continue to face pricing pressure [6]. According to a leading survey,<sup>4</sup> the per-unit transit pricing has suffered an annualized decline averaging 61 percent between 1998 and 2010!

Seeking better returns from their network infrastructure and data centers, some IBPs have branched into the realm of content delivery. A content delivery network (CDN) provider caches and replicates web content on the edges of the Internet to enhance site responsiveness and to streamline customer experience on behalf of content providers (CPs), such as web portals, streaming media providers, and ecommerce operators. A traditional CDN leases (rather than owns) capacity from ISPs and IBPs; it in turn charges clients a premium over cost. IBPs, with extensive infrastructure capacity and reach already in place, are poised to make inroads as lower-cost CDNs.

Another emerging development has been the intensified competition in streaming media services, as brought forth by the cable TV-based ISPs.<sup>5</sup> From 2008 to 2013, an estimated 5.06 million (\~5 percent) U.S. TV subscribers stopped their cable service to rely instead solely on online and over-the-air programming.<sup>6</sup> In response, cable TV-based ISPs have added on-demand streaming to appease subscribers while also offering it as a free add-on for pricier program packages. Because few CPs have invested in original productions, content from different providers exhibits little differentiation, having been licensed from the same television networks and movie studios. In such a commoditized market, gainful collaborations among providers may help improve operational efficiency while reducing the customer acquisition cost.

## Problems and Motivation

We first investigate the recent trending of delivery consolidation in media streaming, a topic that has been motivated by the well-publicized dispute between an ISP and an IBP. <sup>7</sup> The involved ISP (namely, Comcast) is a cable video, high-speed Internet, and phone service provider for residential and business customers in the United States; the IBP (namely, Level 3), also U.S. based, offers a range of integrated communications services, including fiber optics backbone routes. The contention arose from the IBP’s new role as the primary CDN for a major streaming CP (i.e., Netflix) that in turn altered the IBP’s interconnection dynamics with other service providers.

CPs traditionally rely on the CDNs’ edge server nearest to the subscribers (as measured by the number of hops, roundtrip latencies, etc.) to deliver content; the ISP in turn charges the CDNs for the amount of data. However, when an IBP consolidates the delivery chain, not only does the ISP stand to lose the transit revenue from the CDN, but it also receives much higher traffic inflow from the IBP exchange points, which may necessitate infrastructure upgrades [1]. The IBP involved in the dispute initially offered facility and network upgrades, an offer that was promptly rejected; it eventually agreed to pay for traffic beyond the 2-to-1 ratios [2], and the two parties recently agreed to settle their FCC case. Details of the agreement were not disclosed, but the IBP appeared to agree to improve its routing efficiency and load balancing in exchange for a lower peering rate.<sup>8</sup>

We also examine the implications of an ISP’s decision to start offering its own video streaming services. ISPs with access to film libraries and broadcasting archives (e.g., from affiliated TV networks and movie studios) likely have advantages in programming costs and bargaining positions (when negotiating licensing with other content owners) over a pure-play streaming CP. It thus remains to be seen whether a pure-play CP can, in the long run, sustain an outsized growth without the benefit of the “captive” customer base that cable and phone operators enjoy. Reportedly, a major pure-play CP has reached out to ISPs to discuss possible partnerships, seeking to become either an on-demand premium channel or to share revenue through consolidated billing. Although none of the overtures has come to fruition,<sup>9</sup> it is nonetheless valuable to assess different forms of collaboration as the market continues to evolve.

On the matter of delivery consolidation, we develop propositions that help prescribe the equilibrium strategies for several interconnection decisions. For example, we derive a cost ratio that suggests whether a CP is better off staying with its incumbent CDN or replacing it with an IBP. We also suggest when an ISP should switch to paid peering once its upstream IBP starts carrying CDN traffic. Last, we compare the merits of getting a one-time network and facility upgrade versus receiving recurring transit payments following a significant change in traffic pattern.

As for the competition and consolidation of content streaming services, we show that direct competition in a crowded and commoditized market may not always be the best strategy. Facing rising licensing costs and windowing restrictions (i.e., long waits after the DVD release and titles blocked for streaming during higher-margin pay-per-view runs), streaming providers would potentially benefit from partnerships. One possible form of partnership, at the operational level, is for the CP to designate ISPs as CDNs in selected markets. Our results show that such “disintermediation” could benefit both parties if the CP is above a size threshold. Another potentially gainful partnership is to bundle content and split the revenue. We show that such collaboration will work well if the content is sufficiently differentiated and the equilibrium revenue split can be identified. We also show that success in service bundling becomes more elusive if there is little content differentiation or if providers have difficulties raising the service prices.

Disputes among ISPs that we study here are not sporadic events. Although many are settled behind closed doors and away from public scrutiny, there has been another legal case involving a different set of CP, CDN, and ISPs that surfaced recently in the eurozone.<sup>10</sup> Furthermore, with major telco-based ISPs expanding ondemand streaming offerings, cable TV-based ISPs unbundling premium channels,<sup>11</sup> and gaming console makers planning and developing Internet-based TV channels, we anticipate the competition against pure-play streaming CPs will continue to intensify. Analytical insights derived here would provide valuable decision supports when drawing interconnection contracts or when pricing service collaborations.

## Literature Review

Peering and transit contracting have received significant attention in prior research. For example, Tan et al. [38] used game-theoretical models to show how contract pricing between IBPs can be derived based on quantifiable attributes such as link capacity, network utilization, and quality of service thresholds. Analyzing one IBP and two ISPs, Weiss and Shin [39] showed how peering gives the two ISPs bargaining power to avoid high-price settlement with the IBP. Economides [14] analyzed the interconnection between ISPs and IBPs and showed that peering among ISPs would keep IBPs from raising the transit fee. Likewise, Shrimali and Kumar [36] showed that peering is a fair and efficient outcome between two ISPs if the peering costs are symmetric and the backbone provider charges both inbound and outbound traffic. The adoption of peering has been shown to improve social welfare and soften competition among providers [5, 7, 17]. There are also studies favoring one interconnection type over the other. For example, Kennet and Ralph [26] maintained that capacity-based interconnection is more efficient than peering. It has also been shown that ISPs with more symmetric traffic would prefer a peering arrangement, and others would pay a transit fee to exchange traffic through an intermediary network [25]. Although differentiated services may benefit both ISPs and consumers, Ma et al. [31] indicated that ISPs would need an appropriate revenue distribution mechanism to foster a collaborative provisioning of differentiated services.

CPs rely on the CDNs to reach subscribers of many ISPs and IBPs. CDNs then charge the CPs according to factors such as bandwidth cost, traffic pattern, content size, and the number of proxy servers [35]. Hau et al. [22] indicated that CPs should “multihome” (i.e., contract with more than one ISP) and use CDNs to improve the delivery quality of service and to prevent ISPs from imposing monopolistic pricing. By examining three different CDN redirection policies, Stamos et al. [37] found that a close-by proxy server with subscriber-participated cooperation can achieve the best performance. Likewise, Du et al. [13] proposed the concept of a capacity provision network, consisting of many service providers, for better cost efficiency and higher quality of service. Their results suggest that service providers have significant incentives to engage in cooperative resource allocation and surplus sharing. He and Walrand [23] proposed a fair revenue-sharing policy to encourage collaboration among providers for higher profits. Although many CDNs adopt traditional volumebased pricing, Hosanagar et al. [24] showed that such an approach cannot lead to optimal profit when there is heterogeneous burstiness across CDNs.

The need to meet end-to-end quality of service requirements, such as handling transmission delays and jitteriness, calls for a robust Internet infrastructure. Korilis and Orda [27] showed there exists incentive-compatible pricing that drives the performance of network to the socially optimal level. However, whether ISPs can impose differentiated charges on CPs for preferential access remains a topic of fierce debate. Guo et al. [20] examined the issue of net neutrality by considering both uniform and differential fees to find conditions under which the broadband service provider will deviate from the social optimal. Cheng et al. [8] created a model with one ISP and two CPs to show that social welfare increases only if one of the CPs pays a preferential fee; the ISP will invest in network infrastructure at the socially optimal level only if there is net neutrality. Economides and Tåg [16] argued for network neutrality to increase the total surplus for consumers and CPs from the network effect. Guo and Easley [18] showed the positive effect of network neutrality on content innovation in the short run due to the conflux of the free-rider effect and the cross-group congestion effect. Lahiri et al. [30] also noted the issue of neutrality spreading from fixed Internet to wireless platforms.

Whether net neutrality is beneficial to society depends on several factors. For example, Choi et al. [9] found that the merit of net neutrality regulation hinges on how surplus is divided among CPs and consumers. In considering ISPs’ investment decisions, Njoroge et al. [34] showed a higher investment level under nonneutral regimes because it is easier to extract surpluses through differentiated CP pricing; essentially, allowing for tiered service quality and pricing lead to higher ISP service quality, which subsequently increases the CP’s revenue, consumer surplus, and social welfare. Guo et al. [21] analyzed the issue of net neutrality when broadband service providers vertically integrate with CPs and concluded that vertically integrated firms may not always degrade the delivery of the competing content. Abandoning net neutrality may reduce competition in the market of digital content, even though doing so could raise consumer surplus and broadband market coverage [19]. From the perspective of policy makers, Clemons and Madhani [11] studied the antitrust issue by analyzing Google to show that current regulatory frameworks may be detrimental to innovative digital business models.

Our research approach is closely aligned with that of Jahn and Prüfer [25] and Economides and Tåg [16] and also incorporates recent shifts in the competition landscape among providers. Jahn and Prüfer modeled the competition between two ISPs by comparing paid peering with free peering. They showed that sufficiently symmetric ISPs would agree to peer or would otherwise turn to transit through an intermediary network—a discovery shared by Badasyan and Chakrabarti [4]. Economides and Tåg [16] discussed Internet neutrality regulation in the context of a two-sided market. In their model, CPs rely on exogenous advertising revenue per consumer, which is similar to the revenue-generating components in Guo et al. [21].

Our research uses a similar modeling approach to capture the competition between a pure-play CP and a streaming ISP. To the best of our knowledge, the current work is one of the earliest to consider the joint interactions across four classes of providers: ISPs, IBPs, CDNs, and CPs. We investigate game equilibriums for delivery consolidation and service competition in the next two sections.

## Modeling the Delivery Consolidation

We consider the market for streaming media services, which involves several classes of providers, including content providers, content delivery networks, Internet backbone providers, and Internet service providers. We augment Figure 1 with the following summary to show how these providers interact with one another and with consumers:

● Internet service providers (ISPs). The primary role of ISPs is to offer Internet access to retail users. ISPs are often legacy cable TV providers or phone companies operating in regional markets. An ISP signs “transit” contracts with IBPs (see below) to reach other ISPs. ISPs can also bypass IBPs to “peer” directly with one another. Besides offering Internet access, some broadband ISPs also offer video on-demand and media-streaming services. Notable U.S.-based ISPs include Comcast, AT&T, Time Warner Cable, and Verizon.

● Internet backbone providers (IBPs). The traditional roles of IBPs have been to deliver long-haul traffic for regional ISPs and to provide Internet access to corporate clients. The transit payments from ISPs help recoup the cost of infrastructure build-out, monitoring, and upgrades. Underutilized network bandwidth and the increasingly prevalent peering among ISPs have driven down the margin for such transit services, forcing IBPs to offer other services to better utilize their infrastructure. Notable IBPs include Level 3, Tata Communications, CenturyLink, and Vodafone. Some providers (e.g., AT&T and Verizon) are both ISPs and IBPs.

● Content delivery networks (CDNs). CDNs deploy web servers deep into the edges of the Internet so that requests for applications and contents can be fulfilled by a data center of close proximity. CPs rely on CDNs to establish relationships with ISPs to improve performance and availability. Major CDNs include Akamai, BitGravity, and Limelight Networks. Traditionally, CDNs leased server space from ISPs and IBPs and did not own extensive network infrastructure. However, Amazon’s CloudFront, Microsoft’s Azure, and Level 3’s forays into CDN have changed that.

● Streaming content providers (streaming CPs) and consumers. Simply put, streaming CPs offer on-demand media-streaming services over the Internet. Streaming CPs normally delegate the content delivery side of their business to CDNs. Major pure-play streaming CPs include Netflix and Hulu. Consumers of media-streaming services are likely broadband Internet users. Because an ISP can also offer add-on video on demand and streaming media services, the subscribers of its broadband Internet can choose between the in-house streaming service and that offered by a pure-play CP.

Our main focus is on the competition and collaboration dynamics among the different classes of service providers. In this section, we model the ramifications of delivery consolidation when a streaming CP (i.e., Netflix) shifts part of the content delivery business from incumbent CDNs (i.e., Akamai and Limelight) to a backbone provider (i.e., Level 3 after branching into CDN) that has infrastructure and routing characteristics distinct from pure-play CDNs. What appeared to be a simple act of cost cutting by the CP has stirred up heated exchanges between the IBP and its downstream ISPs (e.g., Comcast, the “ISP-1” in our models). When modeling streaming service competition and collaboration in the next section, we analyze conditions under which the pure-play CP and a streaming ISP can collaborate, either on content delivery or on content pooling.

To capture the competition dynamics between the CP and ISP-1, we use a twostage decision process and show its structure and decision scenarios in Figure 2. The first stage reflects the recent trend of delivery consolidation, with backbone providers offering content caching, duplication, and delivery. The decision to be made during this stage is whether the CP should retain the incumbent CDN or replace it with an IBP. The CP’s decision in Stage 1 determines whether the media streams will be originated within the ISP-1’s network via CDN’s edge servers or from IBP-1. The decision in Stage 2 involves ISP-1’s choosing between free peering (case B) or paid peering (case C) if IBP-1 assumes the CDN role for the CP. If the CP stays with the incumbent CDN, then ISP-1 can be assumed to have stayed with regular peering (case A), because there is no incentive to switch to paid peering (and incur the traffic monitoring/metering cost) when local servers handle the media streams.

![](/api/attachments/B4NSYJB2/fulltext/images/cc1ffa44c711cecb16a30e168f7a35dc52213eafb641b52c021e522349ef8a12.jpg)

<table><tr><td></td><td>Stage 1</td><td>Stage 2</td></tr><tr><td>Case A</td><td>CP stays with CDN</td><td>ISP-1 peers free with its IBP</td></tr><tr><td>Case B</td><td>CP switches to IBP</td><td>ISP-1 peers free with its IBP</td></tr><tr><td>Case C</td><td>CP switches to IBP</td><td>ISP-1 opts for paid peering with its IBP</td></tr></table>

Figure 2. Game Stages and Scenarios

We summarize the decision variables and model parameters needed to construct and analyze each subgame in the Appendix. Proofs for all propositions can also be found there.

We derive the demand for the two streaming services using the Hotelling model, which incorporates the effect of consumer preference. Suppose ISP-1 and the CP are located at each end (point 0 and point 1, respectively) of the Hotelling line. The utilities of service from ISP-1 and CP for a consumer at point $\theta \in [ 0 , 1 ]$ are

$$
U _ {I S P, 1} = V _ {I S P, 1} - \theta - t _ {I S P, 1}
$$

$$
U _ {C P} = V _ {C P} - (1 - \theta) - t _ {C P}.
$$

Assuming a pay-per-subscription revenue model, which is common in digital content distribution [10], a typical consumer derives the value of the media-streaming service from ISP-1 at $V _ { I S P , 1 }$ and pays $t _ { I S P , 1 }$ for subscription. Because the streaming service from ISP-1 may be less than ideal (e.g., due to the number and genres of titles available, ease of search, recommendation quality, and types of devices supported) to a consumer, there is a misfit cost, proportional to the degree of divergence from the ideal service, to be deducted from the utility function. Deriving the utility for $\mathrm { C P } ^ { \bullet } \mathbf { s }$ service is similar, except the misfit cost is $1 - \theta$ instead. To economize the model’s notation, we normalized the misfit cost rate to 1 for both θ and $1 - \theta .$

The values of the service from CP and ISP-1 are denoted as $V _ { C P }$ and $V _ { I S P , 1 }$ respectively. CPs have used several strategies to differentiate service values. For example, they may strike exclusive distribution deals with studios, produce original programs, or jockey for earlier “windows” to stream titles soon after theatrical runs, TV debuts, or DVD sales. They may also try to create additional value via delivery quality and formatting (e.g., HD, 3D, and closed captioning) or platform support (e.g. to gaming systems and mobile devices) [15].

Solving $U _ { I S P , 1 } \left( \hat { \boldsymbol { \Theta } } \right) = U _ { C P } ( \hat { \boldsymbol { \Theta } } )$ and $U _ { C P } ( \underline { { { \theta } } } ) = 0$ yields the indifferent misfit cost $\hat { \boldsymbol { \theta } }$ and the maximum level of misfit θ for CP’s service worth subscribing [33]. In this study, we consider interior solutions of $0 < \underline { { \theta } } < \hat { \theta } < 1$ . As a fundamental condition in the horizontal differentiation model, $0 < \widehat { \theta } < 1$ shows a sustained competition between ISP-1 and CP, as either one service or the other is favored by each consumer. The difference, ${ \hat { 0 } } - \underline { { \theta } } .$ , measures the level of demand from consumers who prefer ISP-1’s media-streaming service but cannot get it (being outside of the ISP-1’s broadband service area). The condition $\underline { { \theta } } < \hat { \boldsymbol { \theta } }$ ensures the pricing dynamic between the two providers; when ${ \hat { \boldsymbol { \theta } } } \leq \underline { { \boldsymbol { \theta } } }$ holds, there is no direct competition between ISP-1 and CP, because their subscribers derive no positive utilities from switching to the competing service, leading to an unrealistic scenario in which providers can ignore the competitor’s pricing strategy. Finally, $0 < \underline { { \theta } }$ warrants sufficient heterogeneity in consumer preference so that the market will not be wholly served by CP (following ISP-1’s withdrawal). Overall, imposing the constraint of $0 < \underline { { \theta } } < \hat { \theta } < 1$ allows our analysis to take place when there are active marketing and pricing trade-offs for both ISP-1 and CP.

The ISP-1’s streaming service is available only to its own subscribers, whereas $\mathrm { C P } ^ { \bullet } \mathbf { s }$ is available to the subscribers of all ISPs. By using ${ \mathfrak { a } } ,$ an exogenous variable that indicates the proportion of broadband users who have ISP-1 as their ISP, the service demands are shown as

$$
\begin{array}{c} D _ {I S P, 1} = \alpha \cdot \hat {\theta} \\ D _ {C P} = \alpha \cdot (1 - \hat {\theta}) + (1 - \alpha) (1 - \underline {{\theta}}). \end{array}
$$

A high value of $\hat { \boldsymbol { \theta } }$ implies that the misfit cost for ISP-1’s service has to be quite high before its broadband subscribers would consider alternative streaming services. Thus, $D _ { I S P , 1 }$ increases with ${ \widehat { \mathsf { \theta } } } .$ The demand for $\mathrm { C P } ^ { \bullet } \mathbf { s }$ service comes from two sources, the first being ISP-1’s network subscribers who prefer $\mathrm { C P ^ { \bullet } s }$ streaming media service, and the second being broadband subscribers from other ISPs who find $\mathrm { C P } { \mathrm { { s } } }$ service acceptable. The two demand functions, through misfit costs $\hat { \boldsymbol { \theta } }$ and $\underline { { \theta } } ,$ are endogenously determined by factors such as content quality, consumer preference, and subscription fee.

ISP-1 charges the CDN a fee $F$ for each unit of traffic transmitted. We view this fee from ISP-1 as a market price<sup>12</sup> and thus exogenous. Essentially, with each CDN contracting with multiple ISPs, if ISP-1 tries to charge a price beyond $F ,$ the CDN can divert the traffic to a nearby ISP, which in turn peers with ISP-1. The network traffic can be classified into three types: local traffic, outbound traffic, and inbound traffic [39]. Prior economic literature assumes that a network incurs a different marginal cost for local traffic $( c _ { o } )$ than for inbound and outbound traffic $\left( c _ { t } \right)$ [3, 17, 22, 28, 29]. With $F$ being the premium-over-cost of the end-to-end delivery, we have $F > c _ { o } + c _ { t }$

To identify the equilibriums, we derive profit functions for all three cases and identify conditions under which one set of decisions is preferred over the others. For case A, the decision sequence is as follows: First, the CDN charges CP a service fee ${ \bf q } _ { C D N }$ for the content delivery work, which must be higher than F for the CDN to stay profitable. Then, both ISP-1 and CP make their pricing decisions simultaneously, and the prices for the streaming media services are $t _ { I S P , 1 }$ and $t _ { C P }$ , respectively. The profit functions for the three providers are

$$
\underset {t _ {I S P, 1}} {\text { Max }} \pi_ {I S P, 1} = (t _ {I S P, 1} - c _ {t}) \alpha \cdot \hat {\theta} + (F - c _ {t}) \alpha \cdot (1 - \hat {\theta})\tag{1}
$$

$$
\underset {a _ {C D N}} {\text { Max }} \pi_ {C D N} = (a _ {C D N} - F) \alpha \cdot (1 - \hat {\theta}) + (a _ {C D N} - F) (1 - \alpha) \cdot (1 - \underline {{\theta}})\tag{2}
$$

$$
\underset {t _ {C P}} {\text {Max}} \pi_ {C P} = (t _ {C P} - a _ {C D N}) \cdot \alpha \cdot (1 - \hat {\theta}) + (t _ {C P} - a _ {C D N}) \cdot (1 - \alpha) (1 - \underline {{\theta}}).\tag{3}
$$

The result from this subgame is summarized in Lemma 1.

Lemma 1 (Case A Profits—ISP-1 Peers with Incumbent CDN for Media Streams) ISP-1’s and $\mathrm { C P } ^ { \bullet } \mathbf { s }$ profits are given by $\pi _ { I S P , 1 } ^ { ( A ) } ~ = ~ 2 { \bf a } ~ \cdot ~ \widehat { \sf \theta } ^ { 2 } ~ + ~ ( F ~ - ~ c _ { t } ) ~ \cdot ~ { \bf a }$ and $\pi _ { C P } ^ { ( A ) } = 2 D _ { C P } ^ { 2 } / ( 2 - \alpha )$ ; where

$$
\begin{array}{c} (3 2 - 5 0 \alpha + 1 9 \alpha^ {2}) V _ {I S P, 1} - (8 - 1 0 \alpha + 3 \alpha^ {2}) V _ {C P} \\ \hat {\theta} = \frac {- (2 4 - 4 0 \alpha + 1 6 \alpha^ {2}) F + (3 2 + 3 \alpha^ {2} - 2 6 \alpha)}{4 (4 - 3 \alpha) (8 - 5 \alpha)} \end{array}
$$

$$
\text { and } D _ {C P} = \frac {\left(\alpha^ {2} - 2 \alpha\right) V _ {I S P , 1} + \left(3 \alpha^ {2} - 1 0 \alpha + 8\right) V _ {C P} - \left(4 \alpha^ {2} - 1 2 \alpha + 8\right) F + \left(6 \alpha - 3 \alpha^ {2}\right)}{4 (8 - 5 \alpha)}.
$$

For case B, the decision sequence is as follows: First, IBP-1 charges CP a CDN service fee $a _ { I B P , 1 }$ while incurring a margin cost of $c _ { o }$ to carry each unit of traffic. Then, both ISP-1 and CP make their pricing decisions simultaneously. The profit functions are

$$
\underset {t _ {I S P, 1}} {\text { Max }} \pi_ {I S P, 1} = (t _ {I S P, 1} - c _ {t}) \alpha \cdot \hat {\theta} - c _ {t} \cdot \alpha \cdot (1 - \hat {\theta})\tag{4}
$$

$$
\underset {a _ {I B P, 1}} {\text { Max }} \pi_ {I B P, 1} = (a _ {I B P, 1} - c _ {o}) \alpha (1 - \hat {\theta}) + (a _ {I B P, 1} - c _ {o}) (1 - \alpha) (1 - \underline {{\theta}})\tag{5}
$$

$$
\underset {t _ {C P}} {\text { Max }} \pi_ {C P} = (t _ {C P} - a _ {I B P, 1}) \alpha (1 - \hat {\theta}) + (t _ {C P} - a _ {I B P, 1}) (1 - \alpha) (1 - \underline {{\theta}}).\tag{6}
$$

We summarize the results from this subgame in Lemma 2.

Lemma $^ 2$ (Case B Profits—ISP-1 Peers with IBP-1 for CDN Streams Settlement-Free)

ISP-1’s and $\mathrm { C P } { \mathrm { { s } } }$ profits are given by $\pi _ { I S P , 1 } ^ { ( B ) } = 2 { \bf a } \cdot \hat { \boldsymbol { \Theta } } ^ { 2 } - c _ { t } \cdot { \bf a }$ and $\pi _ { C P } ^ { ( B ) } = 2 D _ { C P } ^ { 2 } / ( 2 - \mathfrak { a } )$ where

$$
(3 2 - 5 0 \alpha + 1 9 \alpha^ {2}) V _ {I S P, 1} - (8 - 1 0 \alpha + 3 \alpha^ {2}) V _ {C P}
$$

$$
\hat {\theta} = \frac {+ (8 - 1 0 \alpha + 3 \alpha^ {2}) c _ {o} + (3 2 + 3 \alpha^ {2} - 2 6 \alpha)}{4 (4 - 3 \alpha) (8 - 5 \alpha)} \text { and }
$$

$$
D _ {C P} = \frac {\left(\alpha^ {2} - 2 \alpha\right) V _ {I S P , 1} + \left(3 \alpha^ {2} - 1 0 \alpha + 8\right) V _ {C P} - \left(3 \alpha^ {2} - 1 0 \alpha + 8\right) c _ {o} + \left(6 \alpha - 3 \alpha^ {2}\right)}{4 (8 - 5 \alpha)}.
$$

For case C, the stages of the subgame are the same as those in case B. ISP-1 charges IBP-1 for streaming content with a peering fee $p ;$ monitoring traffic between ISP-1 and IBP-1 incurs a fixed cost M. The profit functions are

$$
\underset {t _ {I S P, 1}} {\text { Max }} \pi_ {I S P, 1} = (t _ {I S P, 1} - c _ {t}) \alpha \cdot \hat {\theta} + (p - c _ {t}) \cdot \alpha \cdot (1 - \hat {\theta}) - M\tag{7}
$$

$$
\underset {a _ {I B P, 1}} {\text { Max }} \pi_ {I B P, 1} = (a _ {I B P, 1} - c _ {o} - p) \alpha \cdot (1 - \hat {\theta}) + (a _ {I B P, 1} - c _ {o}) (1 - \alpha) \cdot (1 - \underline {{\theta}}) - M\tag{8}
$$

$$
\underset {t _ {C P}} {\text {Max}} \pi_ {C P} = (t _ {C P} - a _ {I B P, 1}) \cdot \alpha \cdot (1 - \hat {\theta}) + (t _ {C P} - a _ {I B P, 1}) \cdot (1 - \alpha) (1 - \underline {{\theta}}).\tag{9}
$$

We summarize the results from the subgame in Lemma 3.

Lemma 3 (Case C Profits—ISP-1 Uses Paid Peering with IBP-1 for CDN Streams) ISP-1’s and $\mathrm { C P ^ { \bullet } s }$ profits are given by $\pi _ { I S P , 1 } ^ { ( C ) } \ = \ 2 { \alpha \hat { \theta } } ^ { 2 } \ - \ ( p \ - \ c _ { t } ) \ \cdot \ \alpha \ - \ M$ and $\pi _ { C P } ^ { ( C ) } = 2 D _ { C P } ^ { 2 } / ( 2 - \alpha )$ ; where

$$
\begin{array}{l} (3 2 - 5 0 \alpha + 1 9 \alpha^ {2}) V _ {I S P, 1} - (8 - 1 0 \alpha + 3 \alpha^ {2}) V _ {C P} + (3 2 + 3 \alpha^ {2} - 2 6 \alpha) \\ \hat {\theta} = \frac {(8 - 1 0 \alpha + 3 \alpha^ {2}) c _ {o} - (3 2 + 2 0 \alpha^ {2} - 5 2 \alpha) p}{4 (4 - 3 \alpha) (8 - 5 \alpha)} \\ \text { and } D _ {C P} = \frac {(\alpha^ {2} - 2 \alpha) V _ {I S P , 1} + (3 \alpha^ {2} - 1 0 \alpha + 8) V _ {C P} - (3 \alpha^ {2} - 1 0 \alpha + 8) c _ {o} + (6 \alpha - 3 \alpha^ {2})}{4 (8 - 5 \alpha)}. \end{array}
$$

Using Lemma 2 and Lemma 3, we analyze ISP-1’s best action when CP decides to contract IBP-1 for content delivery. Under free peering, IBP-1 can operate at a lower cost than incumbent CDN and can afford to charge CP less. CP’s exploitation of this CDN cost advantage would affect the ISP-1’s profit from streaming media service. An opposite effect occurs when IBP-1 interconnects with ISP-1 using paid peering due to higher cost. By comparing $\pi _ { I S P , 1 } ^ { ( B ) }$ with $\pi _ { I S P , 1 } ^ { ( C ) }$ , we derive our first proposition.

Proposition 1 (ISP-1’s Choice of Peering Contract)

If CP contracts with IBP-1, ISP-1’s best response is to adopt paid peering when

$$
\begin{array}{l} \left\{(1 - \alpha) \left[ \frac {- \Delta + (1 6 + 1 0 \alpha^ {2} - 2 6 \alpha) p}{(4 - 3 \alpha) ^ {2} (8 - 5 \alpha)} \right] + 1 \right\} p \cdot \alpha > M, \text {   where } \\ \Delta \equiv (3 2 - 5 0 \alpha + 1 9 \alpha^ {2}) V _ {I S P, 1} - (8 - 1 0 \alpha + 3 \alpha^ {2}) V _ {C P} + (8 - 1 0 \alpha + 3 \alpha^ {2}) c _ {o} + (3 2 + 3 \alpha^ {2} - 2 6 \alpha). \end{array}
$$

Otherwise, the ISP-1 should peer with IBP-1 settlement-free.

Proposition 1 shows that ISP-1 prefers paid peering when its share of broadband users (α) is high. When a high number of ISP-1’s subscribers use CP’s service, the traffic from IBP-1 to ISP-1 also increases; ISP-1 thus benefits from paid peering, provided that the extra revenue is high enough to offset the overhead for network monitoring and accounting. We use Figure 3 to compare $\pi _ { I S P , 1 } ^ { ( B ) }$ with $\pi _ { I S P , 1 } ^ { ( C ) }$ . The paid peering contract leads to higher profit when the market share of ISP-1 is sufficiently high; otherwise, peering settlement-free yields higher profit for ISP-1. Although the profits in Figure 3 are calculated for a given set of parameter values, the result $\pi _ { I S P , 1 } ^ { ( C ) } > \pi _ { I S P , 1 } ^ { ( B ) }$ holds as long as the ISP-1’s market share is high enough and the fixed cost M is relatively low. The robustness check for this result can be found in the Appendix.

Using the results in Lemma 2 and Lemma 3 to compare $\pi _ { C P } ^ { ( B ) }$ with $\pi _ { C P } ^ { ( C ) }$ , we derive Lemma 4.

![](/api/attachments/B4NSYJB2/fulltext/images/0d996f4039b57fd49d5523cdab9f93b796f2fcc9f800c9e86cf528e3df0ffef9.jpg)  
Figure 3. $\pi _ { I S P , 1 } ^ { * }$ in Cases B and C

Lemma 4 (Impact of Contract Type Between ISP-1 and IBP-1 on CP’s Profit)

When CP contracts with IBP-1, CP’s profit stays the same regardless of ISP-1’s interconnection type with IBP-1. Formally, $\pi _ { C P } ^ { ( B ) } = \pi _ { C P } ^ { ( C ) }$

Lemma 4 shows that CP is not concerned if IBP-1 charges a higher fee for content delivery when under paid peering with ISP-1. If ISP-1 charges IBP-1 for streaming content with a peering fee $p ,$ from Lemma 3 we see that IBP-1 will charge CP a higher CDN fee due to the increased cost of delivery; CP in turn will raise the price for the streaming media service. From Lemmas 2 and 3, $\mathrm { C P } ^ { \bullet } \mathbf { s }$ revenue per demand doesn’t change with the peering fee. Thus, if CP’s demand stays the same between case B and case C, its profit will not decline if ISP-1 chooses paid peering.

From ISP-1’s point of view, its best strategy is to raise price, which in turn pushes CP’s subscription fee higher. Doing so makes the demand from those who prefer CP over ISP-1 increase under equilibrium; however, ISP-1’s transit revenue is positively associated with $\mathrm { C P } ^ { \bullet } \mathbf { s }$ demand. From CP’s point of view, a higher price for its streaming media service causes the number of its subscribers to decrease; however, the effect does not affect its equilibrium demand, because the demand from those who prefer CP over ISP-1 will also increase.

Building on Lemma 4, we can compare $\pi _ { C P } ^ { ( A ) }$ with $\pi _ { C P } ^ { ( B ) }$ to identify conditions under which the CP will choose IBP-1 over the incumbent CDN.

## Proposition 2 (CP’s Choice of CDN Provider)

CP will stay with the incumbent CDN when $F / c _ { o } \leq ( 3 \alpha ^ { 2 } - 1 0 \alpha + 8 ) / ( 4 \alpha ^ { 2 } - 1 2 \alpha + 8 )$ otherwise, it will switch to IBP-1.

Based on Proposition 1 and 2, given $\chi _ { 1 } \equiv ( 3 a ^ { 2 } - 1 0 a + 8 ) / ( 4 a ^ { 2 } - 1 2 a + 8 )$ and $\chi _ { 2 } \equiv \Bigr \{ ( 1 - \mathfrak { a } ) \bigl ( - \Delta + \bigl ( 1 6 + 1 0 \mathfrak { a } ^ { 2 } - 2 6 \mathfrak { a } \bigr ) p \bigr ) \bigg / \Bigl ( \bigl ( 4 - 3 \mathfrak { a } \bigr ) ^ { 2 } \bigl ( 8 - 5 \mathfrak { a } \bigr ) \Bigr ) + 1 \Bigr \} p \cdot \mathfrak { a } ,$ we can plot the equilibrium result in Figure 4.

Corollary 1

1. When $\alpha \approx 1$ , the equilibrium is that CP contracts/stays with the incumbent CDN.

2. When ${ \mathfrak { a } } \approx 0$ , the equilibrium is that ISP-1 enters regular peering with IBP-1.

From Figure 4, before the CP contracts with a cheaper CDN, it considers factors such as the cost of originating traffic from IBP-1 to ISP-1, the CDN’s operating overhead, and the market share of ISP-1. As ISP-1’s market share increases, CP has higher incentive to stay with the incumbent CDN (that is, $\hat { \sigma } \chi _ { 1 } / \hat { \sigma } \mathbf { a } > 0 )$ because the cost of originating traffic from IBP-1 to ISP-1 increases with ISP-1’s market share. Differences in perceived service quality (reflected in the value of $\Delta )$ could also influence interconnection decisions. For example, if CP is to contract with the IBP-1, ISP-1 has incentives to keep the free peering when its content value is high but will switch to paid peering when $\mathrm { C P } ^ { \bullet } \mathbf { s }$ content value is high.

We next show how ISP-1 should set the rate for paid peering.

Corollary 2 (The ISP’s Optimal Pricing for Paid Peering)

ISP-1 sets the peering rate as $\begin{array} { r } { p ^ { * } = V _ { I S P , 1 } - 3 / 2 + \sqrt { \frac { \left( 2 \left( 1 - \mathbf { u } \right) \left( 8 - 5 \mathbf { u } \right) \left( V _ { I S P , 1 } - 3 \right) ^ { 2 } + \Psi \right) } { 8 \left( 1 - \mathbf { u } \right) \left( 8 - 5 \mathbf { u } \right) } } } \end{array}$ ; where $\Psi \equiv ( F - c _ { o } ) \{ ( 6 - 2 V _ { I S P , 1 } ) ( 1 9 \mathrm { a } ^ { 2 }$ – 50α + 32) + (2V<sub>CP</sub>(4 – 3α) – (αF + 8c<sub>o</sub> – 7αc<sub>o</sub>))(2 – α)} and $a < 4 ( F - c _ { o } ) / ( 4 F - 3 c _ { o } )$ . Moreover, $\partial p ^ { * } / \partial { \bf a } > 0$ if $V _ { C P } > V _ { I S P , 1 }$ and cost parameters $( F$ and $c _ { o } )$ are sufficiently small.

Corollary 2 shows that the peering fee is positively associated with $\mathrm { C P ^ { \bullet } s }$ content value. ISP-1 will request from IBP-1 a higher fee if CP acquires high-value content from content owners. When α approaches one, $p ^ { * }$ is infinite; however, Corollary 1 has shown that CP would have stayed with the CDN when $a \geq 4 ( F - c _ { o } ) / ( 4 F - 3 c _ { o } )$ . That is, the optimal peering fee $p ^ { * }$ is relevant only when the ISP-1 does not command an oversized market share.

![](/api/attachments/B4NSYJB2/fulltext/images/f05fea016921a475ecf04f89e3702e893fd5f4f6ef0afaf03102bc04efddd87e.jpg)  
Figure 4. Equilibrium of the Game

Even though we show analytically in Corollary 2 that the optimal peering fee increases with ISP-1’s market share only under restricted conditions, numerically (see Figures A1 and A2 in the Appendix) we find the result holds in broader settings (for example, even when $V _ { C P } < V _ { I S P , 1 } )$ . In reality, since ISP-1 also transits with IBP-1 to gain access to the global Internet, deriving the optimal paid peering pricing could be a complicated matter. For example, after the recent settlement, there appears to be a peering rate change between ISP-1 and IBP-1 once the latter agreed to improve its routing policies for CDN and transit traffics.

One final aspect we analyze in this section is how IBP can best compensate the ISP after taking over as the CP’s CDN. In the following proposition, we show when ISP-1 would accept facility and network upgrades offers from IBP-1, or would instead demand paid peering. For simplicity, we assume the upgrades offered will help reduce ISP-1’s cost of terminating traffic to zero.

## Proposition 3 (ISP-1’s Condition for Accepting Infrastructure Upgrade)

There exists a certain threshold of ISP-1’s market share below which ISP-1 is willing to accept IBP-1’s offer of facility and network upgrades. If ISP-1’s market share is above the threshold value, it will instead demand paid peering when the peering fee is sufficiently high (namely, $p > c _ { t } )$ and the metering cost is not too high.

Essentially, ISP-1’s preference of adopting paid peering increases with its market share, provided that the peering fee more than covers the cost of metering the traffic exchange. With a combination of analytical and numerical (Figure A3 in the Appendix) analyses, we observe that the optimal peering fee $p ^ { * }$ increases with ISP-1’s market share. Pragmatically, an ISP with a large market share (thus bargaining power) is unlikely to lower the peering fee. Overall, as long as the optimal peering fee is sufficiently high, we anticipate ISPs to prefer paid peering over infrastructure and equipment upgrades as their market share grows.

## Modeling the Service Competition

Even though some streaming CPs have made strides in producing exclusive content and reducing the time lags between streaming and DVD releases, they are nevertheless competing in a market in which the content is widely distributed. As the market for media-streaming matures, the costs of acquiring customers and negotiating streaming licenses also increase. Instead of direct competition, which was assumed in the preceding section, forming partnerships to combine service offerings (e.g., making CP’s content accessible from ISP-1’s set-top box) and split the revenue potentially achieves cost savings, provides a more streamlined customer experience, and increases network value between operators [32].

To compare the benefits from different forms of partnerships, we set a baseline case (case D1) similar to case A (discussed in the earlier section), with the difference being that the CDN service fee is now treated as exogenous. One form of partnership (case D2) is to further “disintermediate” the CDN by designating ISP-1 as the local CDN using ISP-1’s existing streaming infrastructure. If distributing $\mathrm { C P } ^ { \bullet } \mathbf { s }$ media streams incurs a server cost of S, then the service fee Φ that ISP-1 collects from CP needs to more than cover the cost. Negotiating the value of $\Phi$ can be a contentious issue, as the outcome directly affects the revenue split between ISP-1 and CP. For simplicity, we consider the case that CP pays ISP-1 $a _ { C D N } ,$ the amount originally set aside for the CDN. For this special case, the profit functions are

$$
\underset {t _ {I S P, 1}} {\text { Max }} \pi_ {I S P, 1} = (t _ {I S P, 1} - c _ {t}) \alpha \cdot \hat {\theta} + (a _ {C D N} - c _ {t}) \cdot \alpha \cdot (1 - \hat {\theta}) - S\tag{10}
$$

$$
\underset {t _ {C P}} {\text { Max }} \pi_ {C P} = (t _ {C P} - a _ {C D N}) \cdot \alpha \cdot (1 - \hat {\theta}) + (t _ {C P} - a _ {C D N}) \cdot (1 - \alpha) (1 - \underline {{\theta}})\tag{11}
$$

## Lemma 5 (Case D2 Profits—ISP Serving as Local CDN)

ISP-1’s and CP’s profits are given by $\pi _ { I S P , 1 } ^ { ( D 2 ) } = 2 { \alpha } \hat { \theta } ^ { 2 } + ( a _ { C D N } - c _ { t } ) { \alpha } - S$ and $\pi _ { C P } ^ { ( D 2 ) } = $ $( t _ { C P } ^ { * } - a _ { C D N } ) \cdot ( \mathbf { a } \cdot ( 1 - \widehat { \mathbf { \theta } } ) + ( 1 - \mathbf { a } ) ( 1 - \mathbf { \theta } ) )$ where $t _ { C P } ^ { \ast } \ = \ \underline { { { \theta } } } - 1 + V _ { C P } , \hat { \theta } = ( ( 4 - 3 \alpha ) V _ { I S P , 1 } - ( 2 - \alpha ) V _ { C P } - ( 2 - 2 \alpha ) a _ { C D N } +$ $( 4 - \mathbf { a } ) ) / ( 2 ( 8 - 5 \mathbf { a } ) )$ and $\underline { { \theta } } = ( - \alpha V _ { I S P , 1 } - ( 4 - 2 \alpha ) V _ { C P } + ( 4 - \alpha ) a _ { C D N } + ( 8 -$ $2 \alpha ) ) / ( 8 - 5 \alpha )$

Proposition 4 (ISP-1 Serving as CP’s CDN)

1. Compared to the baseline case, CP’s profit increases if ISP-1 takes over as $\mathrm { C P } ^ { \bullet } \mathbf { s }$ local CDN.

2. There exists a market share threshold $\alpha ^ { * }$ for ISP-1, above which ISP-1 should be considered as $\mathrm { C P } ^ { \bullet } \mathbf { s }$ local CDN.

Our result indicates that CP could benefit from bypassing third-party CDNs. We also show ISPs with sufficient market share will be open to assuming the CDN role, as doing so benefits both parties by taking advantage of higher demand $( D _ { C P } )$ and higher service fee $( a _ { C D N } ,$ rather than the original F). Even though one major reason for $\mathrm { C P s } ^ { \mathrm { \bullet } }$ reliance on CDNs is to shield themselves from having to negotiate separate interconnection contracts with ISPs, it appears to be worthwhile to pursue direct CDN contracting with larger ISPs.

We now examine the second form of partnership—content bundling (case D3)— and compare ISP-1’s profit with that of case D2. Unlike the behind-the-scenes CDN partnership, content bundling creates marketing exposure and grants easier access to $\mathrm { C P } ^ { \bullet } \mathbf { s }$ content. Because content bundling may reduce consumer heterogeneity [12], we use $\lambda \cdot { \theta }$ to denote the reduced misfit cost from the original θ and use $\hat { V } _ { I S P , 1 }$ to express the value of the bundled content, where $\lambda < 1$ . The value of $\lambda$ reflects how well the customers perceive the blended content from ISP-1 and CP.

The utility of a consumer subscribing to the bundled service is now $U _ { I S P , 1 } = \hat { V } _ { I S P , 1 }$ $\lambda \cdot \theta - t _ { I S P , 1 }$ . If ISP-1 pays CP a royalty fee $\gamma ,$ their profits can be expressed as follows:

$$
\underset {t _ {I S P, 1}} {\text { Max }} \pi_ {I S P, 1} = (t _ {I S P, 1} - \gamma - c _ {t}) \alpha \cdot \hat {\theta} + (a _ {C D N} - c _ {t}) \cdot \alpha \cdot (1 - \hat {\theta}) - S\tag{12}
$$

$$
\begin{array}{c} M a x _ {t _ {C P}} \pi_ {C P} = (t _ {C P} - a _ {C D N}) \cdot \alpha \cdot (1 - \hat {\theta}) + (t _ {C P} - a _ {C D N}) \cdot (1 - \alpha) (1 - \underline {{\theta}}) \\ + \gamma \cdot \alpha \cdot \hat {\theta}. \end{array}\tag{13}
$$

Lemma 6 (Case D3 Profits—Bundled Streaming Contents)

The profit functions for ISP and CP are given by $\pi _ { I S P , 1 } ^ { ( D 3 ) } = \mathfrak { a } ( 1 + \lambda ) \widehat { \Theta } ^ { 2 } + \mathfrak { a } ( a _ { C D N } - c _ { t } ) - S$ and $\pi _ { C P } ^ { ( D 3 ) } = ( V _ { C P } - ( 1 - \underline { { { \Theta } } } ) - a _ { C D N } ) \cdot ( \boldsymbol { \mathrm { a } } \cdot ( \boldsymbol { 1 } - \hat { \boldsymbol { \Theta } } ) + ( 1 - \boldsymbol { \mathrm { a } } ) ( 1 - \underline { { { \Theta } } } ) ) + \gamma \cdot \boldsymbol { \mathrm { a } } \cdot \hat { \boldsymbol { \Theta } } ,$ , where θ = 2 $( 1 + \lambda ) \hat { \Theta } - \hat { V } _ { I S P , 1 } + \gamma + a _ { C D N } ,$ and

$$
\begin{array}{c} (2 - \alpha + 2 \lambda (1 - \alpha)) \hat {V} _ {I S P, 1} - (1 + \lambda (1 - \alpha)) V _ {C P} - (1 - \alpha) (1 + \lambda) a _ {C D N} \\ \hat {\theta} = \frac {+ (2 - \alpha) \lambda - 2 \gamma (1 - \alpha) (1 + \lambda) + 2}{(4 - \alpha + 4 \lambda (1 - \alpha)) (1 + \lambda)}. \end{array}
$$

## Proposition 5 (The Impact of ISP-1 Market Share on Subscription Fees)

With bundling, when the royalty payment $\gamma$ is higher (lower) than $\widetilde { \boldsymbol { \gamma } } ,$ , the optimal subscription fees, $t _ { I S P , 1 } ^ { * } = ( 1 + \lambda ) \hat { \Theta } + \gamma + a _ { C D N }$ and $t _ { C P } ^ { * } = V _ { C P } - ( 1 - \underline { { \theta } } )$ , increase (decrease) with the ISP-1’s market share. Formally, $\tilde { \gamma } = ( 2 \hat { V } _ { I S P , 1 } + V _ { C P }$ – 3a<sub>CDN</sub> – 4λ $- 2 ) / 6$

ISP-1 can reject the bundling proposal if accepting it would not bring in higher profit. Likewise, CP would not agree to bundle if the royalty payment is too low. As indicated by the double-arrow line in Figure 5, a region exists within which both ISP-1 and CP can gain higher profits than in case D1.

ISP-1’s profit increases with its market share $( \hat { \sigma } { \pi } _ { I S P , 1 } ^ { ( D 3 ) } / \hat { \sigma } { \bf a } = ( a _ { C D N } - c _ { t } ) + ( 1 + \lambda ) \hat { \Theta } ( \hat { \Theta }$ $+ 2 { \bf a } \cdot \widehat { \cal O } \widehat { \bf \theta } / \widehat { \cal O } { \bf a } ) > 0$ when $\hat { \cal O } \hat { \boldsymbol { \theta } } / \hat { \cal O } \mathbf { q } > 0 )$ . On the other hand, as shown in Figure 6, CP’s profit may increase or decrease with ISP-1’s market share; the profit increases with the market share only if the royalty payment is sufficiently high.

Proposition 5 further explains the driving force of CP’s profit. CP’s revenue comes both from its own video streaming service and from the royalty payments. A high royalty payment leads ISP-1 to charge a higher subscription fee; consequently, it raises both prices and profits. On the other hand, if the royalty payment is low, then CP relies on its own streaming service for most of its revenue. As ISP-1 increases its market share, CP may be forced to lower its price to slow down a decline in its profit.

![](/api/attachments/B4NSYJB2/fulltext/images/5594d1b9246d1d532ea615502e2f659e96c436bac2b41c211f0ec1872ae676f3.jpg)  
Figure 5. Comparison of Profits in Cases D1 and D3 with Respect to Royalty Payment

![](/api/attachments/B4NSYJB2/fulltext/images/036fc4ab92c5b2ba99bfd133fffa64015393baab7689864e2929a9780b376fc5.jpg)  
Figure 6. CP’s Profit in Case D3 with Respect to ISP-1’s Market Share

## Proposition 6 (ISP-1’s Choice of Service Collaboration Type)

For ISP-1, a combination of high-value content bundle and low royalty payment would generate higher profits than serving as CP’s local CDN. Formally, between case D2 and case D3, ISP-1 prefers service bundling over being the local CDN when $\hat { \boldsymbol { \Theta } } ^ { ( D 3 ) } \ge \hat { \boldsymbol { \Theta } } ^ { ( D 2 ) } \cdot \sqrt { 2 / ( 1 + \lambda ) }$

Our result indicates that ISP-1 should accept CP’s bundling proposal if the content is not highly overlapped and if the royalty payment paid to CP is not too high. Figure 7 shows that a bundled service benefits CP and could benefit ISP-1 (compared to the baseline case D1) if the ISP-1’s market share is higher than a specific threshold and if the bundle value and the royalty payment to CP are reasonably high. However, successful bundling hinges on one side’s ability to raise its price if the other side does. Given a major CP’s recent difficulty in raising service fees when separating its media-streaming operations from DVD rentals,<sup>13</sup> the streaming CP may have been too optimistic about forming partnerships with ISPs.

![](/api/attachments/B4NSYJB2/fulltext/images/2c3a80d99270a9783bee45f879dbdeb8561a2cf3d6118b453491f0ac7a38047d.jpg)  
Figure 7. Comparison of Profits in Cases D1 and D3 Given ISP-1’s Market Share

CP cannot determine the royalty payment unilaterally because ISP-1 does not depend on CP’s content to operate. Therefore, we consider a scenario in which ISP-1 and CP jointly decide the royalty payment, then price their services independently. We only focus on the level of royalty payment that maximizes the total profit; how the additional revenue is negotiated between the two providers is assumed to be done separately.

## Proposition 7 (Analysis of Optimal Royalty Fee)

If there exists a level of royalty payment that maximizes the combined profits for ISP-1 and CP, the payment increases with the content value and ISP-1’s market share but decreases as misfit cost increases. Formally, $\partial \gamma ^ { * } / \partial V _ { I S P , 1 } > 0 , \hat { \sigma } \gamma ^ { * } / \hat { \sigma } V _ { C P } > 0$ , and $\partial \gamma ^ { * } / \partial \mathbf { a } > 0 ; \partial \gamma ^ { * } / \partial \lambda < 0$ , where

$$
\gamma * = \frac {(1 - \alpha) ((4 + \alpha + 4 \lambda (1 - \alpha)) (V _ {C P} - a _ {C D N}) + 4 \alpha (\hat {V} _ {I S P , 1} + \lambda)) + \alpha ((8 + \alpha) - 4 (1 - \alpha) a _ {C D N})}{2 (1 - \alpha) (4 + 5 \alpha + 4 \lambda (1 - \alpha))}.
$$

The royalty fee is determined based on how much value ISP-1 and CP can collectively extract from the service bundle. The profit of ISP-1 with a high number of subscribers is less affected by the increased royalty fee. Thus, if ISP-1 has a higher market share, the royalty fee could be set higher. Likewise, high content values benefit both ISP-1 and CP by extracting more consumer surplus with higher service prices and a suitable royalty fee. The bundled service reduces ISP-1’s misfit cost, but if the benefit from the combined content is not high, then the optimal royalty fee will also be lower. When ISP-1 has a very high market share, service pricing for ISP-1 and CP could turn from a single competitive equilibrium to multiple “kinked demand” equilibriums before reaching monopoly equilibrium. Mérel and Sexton [33] have studied in great detail the asymmetric price equilibrium for the Hotelling model.

## Managerial Implications and Limitations

One important edge of pure-play CPs over video-on-demand outlets or premium cable TV channels is the low subscription fee, hence the importance of keeping the cost of content delivery in check. One plausible approach is to delegate the content delivery chain to a provider operating at a lower marginal cost (likely by owning extensive network and data center infrastructures). Such a seemly simple approach, however, has caused a broad-based ripple effect in how the media streams travel through the Internet, which in turn has profoundly impacted the interconnection relationships among IBPs, ISPs, and CDNs.

The economic models developed here help identify threshold conditions and suggest equilibrium strategies for different classes of providers (including CPs) to adjust to new realities. Specifically, we are able to prescribe which CDN provider to choose for the CP (Proposition 2) and suggest the peering contract type between ISP and IBP for a given market share (Proposition 1). We are also able to show the impact of peering contracting between ISP and IBP on the CP’s profit (Lemma 4), identify the optimal peering price (Corollary 2), and compare the merits of a onetime facility/network upgrade and incremental raises in peering fees (Proposition 3). Furthermore, due to the static nature (i.e., predominantly nontransactional and readaccess) of media streams, it is possible for CPs to achieve further savings by leveraging the ISP’s existing infrastructure instead of using a third-party CDN. However, our analysis (Proposition 4) indicates that only a select group of ISPs will find such arrangement financially attractive. Empirically, the effects of provider size on interconnection relationship and contract pricing that we report here are validated by the proposed merger between two major ISPs<sup>14</sup> and a major CP’s further consolidation of its content delivery chains with a major ISP.<sup>15</sup>

Another area we investigate is whether streaming providers can reap benefits such as lower marketing and programming costs and higher content values by forming alliances. We show that, unlike the case of delivery consolidation where the streaming CP almost always benefits, collaborating with an ISP using content bundling is an equilibrium strategy under much more stringent conditions. A partner (such as a streaming ISP) likely owns extensive network and facility infrastructure, has access to a stable subscriber base, and holds bargaining advantage during media-licensing negotiations. The CP thus is not in a strong position to demand favorable profitsharing terms. A partnership exists only when the streaming ISP’s market share is low and the CP’s content value is high enough for the CP to receive a sufficiently high royalty payment to increase profit (Proposition 5). This finding mirrors the empirical evidence that one major CP has tried and failed twice to form an alliance (once with a premium cable TV network and another with a streaming ISP) partly due to the reality that CP has neither demonstrated the ability to raise its subscription fee nor made its content sufficiently unique to command a high royalty fee.<sup>16</sup> If the market conditions do support a strategic alliance, we find the optimal royalty fee (Proposition 7) and show that the payoff from content bundling will indeed be better than from the operational-level delivery consolidation (Proposition 6).

The current work, although also concerned with the dynamics between CPs and network operators, differs from treatments on net neutrality. For example, studies on net neutrality investigate retail ISPs’ general pricing, traffic shaping, and (denial of) access policies toward CPs to ensure a fair and open access to the Internet. In contrast, the analyses here concentrate on how such relations would impact the success of media-streaming services. Also, net neutrality studies focus on fair and open Internet access at the retail level (mainly ISPs), whereas much of the interconnection we study here takes place deep inside the Internet backbone. Finally, network interconnection predates net neutrality debates and will remain a source of contention as the Internet continues to evolve.

There are several limitations in the current study. First, because we use the Hotelling model to capture service competition, the assumption is that consumers will base their decisions on their valuations to choose the best service. However, it is possible that a consumer could subscribe to both streaming services. Second, we did not consider the issues of quality of service, such as congestion delay, in our model. Many prior studies have investigated the influence of quality of service on pricing strategies; instead, we focus more on the choice of service contracts and the different roles that each provider plays. Third, it is possible that the CDN may counter or match the IBP-1’s offering, so that CP may extract further gain from the competition. However, such an offer is often a short-term tactic and thus considered out of scope.

## Conclusions and Extensions

We study the latest shifts in the competition landscape for media-streaming services involving four classes of providers: Internet service provider, Internet backbone provider, content provider, and content delivery network. We first focus on the issue of content delivery, which has drawn growing press coverage for driving the prime-time Internet traffic in North America. With streaming CPs seeking lower delivery costs and IBPs entering the CDN business, the interconnection dynamics among providers is expected to undergo significant changes. In this study, we use economic modeling to derive equilibrium strategies for several pricing and interconnection decisions that affect different classes of service providers.

We show how decisions made by one provider could ripple through the Internet’s delivery chain. For example, a CP’s choice of content delivery could affect the relationship between two classes of service providers. Our models also demonstrate how provider collaboration can come in different forms. On a more technical level, the CP could further improve operational efficiency by engaging ISPs to handle onnet media streams. By showing more-exacting conditions, we also suggest when revenue sharing through content bundling would be mutually beneficial.

By not incurring the overhead of monitoring traffic, free peering used to be a reasonable approach to settling the finances of data exchange among most providers. However, a reevaluation of the practice appears to be inevitable as the industry goes through both consolidations (among CDN providers) and expansions (e.g., ISPs adding streaming services). With the streaming media market maturing, we posit that optimizing delivery efficiency and provider relationships will not be sufficient to drive success. Rather, managing content innovation and navigating media licensing will play an increasing role. One potentially fruitful extension of the current work thus will be to factor in the effect of content synergy and the bargaining power of content owners when forming partnerships among providers.

On the retail side, we are seeing ISPs steering away from data capping and instead easing into tiered pricing for data overage. A possible extension thus is to examine how the peering fees can be negotiated in conjunction with network topology, traffic patterns, and routing policies to maximize two-sided benefits. Nash’s cooperative bargaining solution is a promising approach when analyzing such situations. From the perspective of network neutrality, the issue of whether differential traffic pricing is beneficial to society should also be investigated. Yet another possible extension would be to consider the issues of quality of service, such as congestion delay, in a new model. Even though prior studies have investigated the role of quality of service when developing pricing strategies, a novel approach would move from a providercentric streaming to a more collaborative (P2P) CDN mechanism.

The explosive growth of online streaming services has created growth opportunities for both content owners and content producers upstream. For example, in an effort to spruce up demands, a streaming CP might be willing to offer an outsized license fee in exchange for exclusive distribution. On the other hand, content producers might be able to pool upfront investments from both streaming CPs and cable channels for content syndication. Work is under way to investigate the effects of both exclusive content distribution and pooling of production costs.

Beyond the various technical and economic factors analyzed in this study, the FCC’s ruling on net neutrality will continue to have far-reaching implications for the future of the streaming media market. For example, are innovations such as data plans with dynamic and tiered quality of service considered a permissible practice (with regard to net neutrality) for mobile streaming? Are data capping and bandwidth throttling necessary to rein in runaway infrastructure cost, or are they are mere signs of abuse from service providers? We expect the competition landscape will continue to evolve deep inside the core of the Internet, given the intertwined regulatory, technological, and economic forces.

Acknowledgments: Jhih-Hua Jhang-Li gratefully acknowledges support from the National Science Council of Taiwan (Republic of China) under grant NSC 102-2410-H-266-007.

## NOTES

1. Verizon (n.d.), Verizon business interconnection policy for Internet networks, www. verizonbusiness.com/terms/peering/ (accessed July 15, 2014).

2. C. Wilson, Peers or not? Cogent, Level 3 disagree, October 5, 2005, http://business. highbeam.com/437286/article-1G1-138013016/peers-not-cogent-level-3-disagree (accessed January 20, 2015).

3. The Economist, Beyond the bubble, October 9, 2003, www.economist.com/node/ 2098913 (accessed July 15, 2014).

4. Drpeering.net, Internet transit prices—Historical and projected, August 2010, http:// drpeering.net/white-papers/Internet-Transit-Pricing-Historical-And-Projected.php (accessed July 15, 2014).

5. S. Schechner, Comcast takes Aim at Netflix, February 22, 2012, http://online.wsj.com/ article/SB10001424052970204909104577237321153043092.html (accessed July 15, 2014).

6. Convergence Consulting Group Limited, The battle for the North American (US/ Canada) couch potato: Online & traditional TV and movie distribution, April 2014, www. convergenceonline.com/downloads/NAMNewContent2014.pdf (accessed July 15, 2014).

7. Associated Press, Comcast vs. Level 3: Online Netflix traffic causes fee fight, November 30, 2010, http://usatoday30.usatoday.com/tech/news/2010-12-01-comcast01\_ST\_N.htm (accessed January 20, 2015).

8. J. Engebretson, Behind the Level 3–Comcast peering settlement, July 17, 2013, www. telecompetitor.com/behind-the-level-3-comcast-peering-settlement/ (accessed July 15, 2014).

9. A. Chozic, Comcast declines to offer Netflix to its customers, March 8, 2012, http:// mediadecoder.blogs.nytimes.com/2012/03/08/comcast-rejects-idea-of-partnering-with-netflix/ (accessed July 15, 2014).

10. Autorité de la concurrence, press release, September 20, 2012, Internet traffic – Peering agreements. www.autoritedelaconcurrence.fr/user/standard.php?id\_rub=418&id\_article=1971\_ (accessed July 15, 2014).

11. J. Roettgers, Did Comcast just take a first step towards unbundling HBO?, October 24, 2013, http://gigaom.com/2013/10/24/did-comcast-just-take-a-first-step-towards-unbundlinghbo/ (accessed July 15, 2014).

12. D. Rayburn, CDN pricing stable: Survey data shows pricing down 15% this year, September 5, 2012, http://blog.streamingmedia.com/2012/09/cdn-pricing-stable-survey-datashows-pricing-down-15-this-year.html (accessed July 15, 2014).

13. S. Woo, Under fire, Netflix rewinds DVD plan: Company backs off plan to split mailed-DVD, streaming service, October 11, 2011, http://online.wsj.com/news/articles/ SB10001424052970203499704576622674082410578 (accessed July 15, 2014).

14. L. B. Baker, Comcast takeover of Time Warner Cable to reshape U.S. pay TV, February 13, 2014, www.reuters.com/article/2014/02/13/us-comcast-timewarnercable-idUSBREA 1C05A20140213 (accessed July 15, 2014).

15. R. Yu, Netflix cuts deal with Comcast to speed service, February 26, 2014, www. usatoday.com/story/money/business/2014/02/23/netflix-comcast-deal-streaming/5757631/ (accessed July 15, 2014)

16. D. Lieberman, Netflix negotiating to become a cable service: Report, March 7, 2012, www.deadline.com/2012/03/netflix-negotiating-to-become-a-cable-service-report/ (accessed July 15, 2014)

17. J. E. Solsman, Netflix, YouTube gobble up half of Internet traffic, November 11, 2013), http://www.cnet.com/news/netflix-youtube-gobble-up-half-of-internet-traffic (accessed January 20, 2015).

## REFERENCES

1. Anderson, N. Peering problems: Digging into the Comcast/Level 3 grudgematch. Ars Technica. December 10, 2010. http://arstechnica.com/tech-policy/2010/12/comcastlevel3/

2. Ante, S.E., and Schatz, A. 2010. Web-traffic spat over Netflix highlights new tensions. Wall Street Journal, November 30.

3. Armstrong, M. Network interconnection in telecommunications. Economic Journal, 108, 448 (1998), 545–564

4. Badasyan, N., and Chakrabarti, S. A simple game-theoretic analysis of peering and transit contracting among Internet service providers. Telecommunications Policy, 32, 1 (2008), 4–18.

5. Berger, U. Bill-and-keep vs. cost-based access pricing revisited. Economics Letters, 86, 1 (2005), 107–112.

6. Besen, S.; Milgrom, P.; Mitchell, B.; and Srinagesh, P. Advances in routing technologies and Internet peering agreements. American Economic Review, 91, 2 (2001), 292–296.

7. Cambini, C., and Valletti, T.M. Network competition with price discrimination: “Billand-keep” is not so bad after all. Economics Letters, 81, 2 (2003), 205–213.

8. Cheng, H.K.; Bandyopadhyay, S.; and Guo, H. The debate on Net neutrality: A policy perspective. Information Systems Research, 22, 1 (2011), 60–82.

9. Choi, J.P.; Jeon, D.-S.; and Kim, B.-C. Internet interconnection and network neutrality. (No. 753). Institute of Industrial Economics, Toulouse, France, 2012.

10. Clemons, E. Business models for monetizing Internet applications and Web sites: Experience, theory, and predictions. Journal of Management Information Systems, 26, 2 (2009), 15–41.

11. Clemons, E., and Madhani, N. Regulation of digital businesses with natural monopolies or third-party payment business models: Antitrust lessons from the analysis of Google. Journal of Management Information Systems, 27, 3 (2011), 43–80.

12. Crawford, G. The discriminatory incentives to bundle in the cable television industry. Quantitative Marketing and Economics, 6, 1 (2008), 41–78.

13. Du, A.Y.; Geng, X.; Gopal, R.D.; Ramesh, R.; and Whinston, A.B. Capacity provision networks: Foundations of markets for sharable resources in distributed computational economies. Information Systems Research, 19, 2 (2007), 126–144.

14. Economides, N. The economics of the Internet backbone. In S. Majumdar et al. (eds.), Handbook of Telecommunications Economics, vol. 2. Amsterdam: Elsevier, 2005.

15. Economides, N., and Katsamakas, E. Two-sided competition of proprietary vs. open source technology platforms and the implications for the software industry. Management Science, 52, 7 (2006), 1057–1071.

16. Economides, N., and Tåg, J. Network neutrality on the Internet: A two-sided market analysis. Information Economics and Policy, 24, 2 (2012), 91–104.

17. Gans, J.S., and King, S.P. Using ‘bill and keep’ interconnect arrangements to soften network competition. Economics Letters, 71, 3 (2001), 413–420.

18. Guo, H., and Easley, R. Broadband coverage, content innovation, and the network neutrality debate. Working paper, 2013. http://ssrn.com/abstract=2134085.

19. Guo, H.; Cheng, H.K.; and Bandyopadhyay, S. Net neutrality, broadband market coverage, and innovation at the edge. Decision Sciences, 43, 1 (2012), 141–172.

20. Guo, H.; Cheng, H.K.; and Bandyopadhyay, S. Broadband network management and the Net neutrality debate. Production and Operations Management, 22, 5 (2013), 1287–1298.

21. Guo, H.; Bandyopadhyay, S.; Cheng, H.; and Yang, Y.-C. Net neutrality and vertical integration of content and broadband services. Journal of Management Information Systems, 27, 2 (2010), 243–276.

22. Hau, T.; Burghardt, D.; and Brenner, W. Multihoming, content delivery networks, and the market for Internet connectivity. Telecommunications Policy, 35, 6 (2011), 532–542.

23. He, L., and Walrand, J. Pricing and revenue sharing strategies for Internet service providers. IEEE Journal on Selected Areas in Communications, 24, 5 (2006), 942–951.

24. Hosanagar, K.; Chuang, J.; Krishnan, R.; and Smith, M.D. Service adoption and pricing of content delivery network (CDN) services. Management Science, 54, 9 (2008), 1579–1593.

25. Jahn, E., and Prüfer, J. Interconnection and competition among asymmetric networks in the Internet backbone market. Information Economics and Policy, 20, 3 (2008), 243–256.

26. Kennet, D.M., and Ralph, E.K. Efficient interconnection charges and capacity-based pricing. International Economics and Economic Policy, 4, 2 (2007), 135–158.

27. Korilis, Y.A., and Orda, A. Incentive compatible pricing strategies for QoS routing. Networks and Spatial Economics, 4, 1 (March 2004), 39–53.

28. Laffont, J.-J.; Rey, P.; and Tirole, J. Network competition: I. Overview and nondiscriminatory pricing. RAND Journal of Economics, 29, 1 (1998), 1–37.

29. Laffont, J.-J.; Marcus, S.; Rey, P.; and Tirole, J. Internet Peering. American Economic Review, 91, 2 (2001), 287–291.

30. Lahiri, A.; Dewan, R.; and Freimer, M. The disruptive effect of open platforms on markets for wireless services. Journal of Management Information Systems, 27, 3 (2011), 81– 110.

31. Ma, R.T.B.; Chiu, D. M.; Lui, J.C.S.; Misra, V.; and Rubenstein, D. On cooperative settlement between content, transit and eyeball Internet service providers. IEEE/ACM Transactions on Networking (TON) 19, 3, 802–815.

32. Mantena, R., and Saha, R. Co-opetition between differentiated platforms in two-sided markets. Journal of Management Information Systems, 29, 2 (2012), 109–140.

33. Mérel, P.R., and Sexton, R.J. Kinked-demand equilibria and weak duopoly in the Hotelling model of horizontal differentiation. The B.E. Journal of Theoretical Economics, 10, 1 (April 2010), DOI:10.2202/1935-1704.1619.

34. Njoroge, P.; Ozdaglar, A.; Stier-Moses, N.; and Weintraub, G. Investment in two sided markets and the net neutrality debate. Columbia Business School DRO (Decision, Risk and Operations) Working Paper No. 2010-05, October 2012. http://ssrn.com/abstract=1641359.

35. Pallis, G., and Vakali, A. Insight and perspectives for content delivery networks. Communications of the ACM, 49, 1 (2006), 101–106.

36. Shrimali, G., and Kumar, S. Bill-and-keep peering. Telecommunications Policy, 32, 1 (2008), 19–32.

37. Stamos, K.; Pallis, G.; Vakali, A.; and Dikaiakos, M.D. Evaluating the utility of content delivery networks. Proceedings of the 4th edition of the UPGRADE-CN workshop on Use of P2P, GRID and agents for the development of content networks. New York: ACM Press, 2009.

38. Tan, Y.; Chiang, I.R.; and Mookerjee, V.S. An economic analysis of interconnection arrangements between Internet backbone providers. Operations Research, 54, 1, (2006), 776–788.

39. Weiss, M.B., and Shin, S.J. Internet interconnection economic model and its analysis: Peering and settlement. Netnomics, 6, 1 (2004), 43–57.

Table A1. Decision Variables

<table><tr><td> $t_{ISP,1}$ </td><td>Subscription fee to ISP-1’s media service</td></tr><tr><td> $t_{CP}$ </td><td>Subscription fee to CP’s media service</td></tr><tr><td> $a_{CDN}$ </td><td>Fee charged by incumbent CDN for content delivery</td></tr><tr><td> $a_{IBP,1}$ </td><td>Fee charged by IBP-1 for content delivery</td></tr></table>

Table A2. Model Parameters

<table><tr><td> $F$ </td><td>Infrastructure surcharged by each ISP to support content delivery service</td></tr><tr><td> $p$ </td><td>Peering fee charged by ISP-1, which depends on ISP-1’s bargaining power</td></tr><tr><td> $c_{o}$ </td><td>Marginal cost of transmitting off-net traffic end-to-end</td></tr><tr><td> $c_{t}$ </td><td>Marginal cost of processing local traffic</td></tr><tr><td> $\alpha$ </td><td>Market share of ISP-1</td></tr><tr><td> $V_{ISP,1} (V_{CP})$ </td><td>Perceived value of the media service from ISP-1 (CP)</td></tr><tr><td> $U_{ISP,1} (U_{CP})$ </td><td>Consumer’s utility for subscribing media service provided by ISP-1 (CP)</td></tr><tr><td> $\theta$ </td><td>Consumer’s preference for media service</td></tr><tr><td> $\hat{\theta}$ </td><td>An indifference point at which the utility derived from ISP-1’s service is the same as that of CP.</td></tr><tr><td> $\underline{\theta}$ </td><td>A specific point at which the utility derived from CP is zero.</td></tr><tr><td> $\pi_{ISP,1} (\pi_{IBP,1}, \pi_{CP}, \pi_{CDN})$ </td><td>Profit of ISP-1 (IBP-1, CP, CDN)</td></tr><tr><td> $D_{ISP,1}$ </td><td>Demand of ISP-1’s media service</td></tr><tr><td> $D_{CP}$ </td><td>Demand of CP’s media service</td></tr><tr><td> $M$ </td><td>Monitoring cost for traffic volumes</td></tr><tr><td> $\gamma$ </td><td>Royalty payment paid to CP</td></tr><tr><td> $S$ </td><td>Server cost for storing video content and processing consumer requests</td></tr><tr><td> $\lambda$ </td><td>Amount of reduction in misfit cost due to bundling</td></tr></table>

## Appendix

## Proof of Lemma 1

Solving $\partial \pi _ { C D N } ^ { ( A ) } / \partial a _ { C D N } ~ = ~ 0$ yields $a _ { C D N } ^ { * } = ( - \alpha V _ { I S P , 1 } + ( 4 - 3 \alpha ) V _ { C P } + ( 4 - 2 \alpha )$ $F + 3 { \bf a } ) / ( 2 ( 4 - 3 { \bf a } ) )$ . Then, by incorporating $a _ { C D N } ^ { * }$ into (1) and (3), solving $\hat { \sigma } \pi _ { I S P , 1 } ^ { ( A ) } / \hat { \sigma } t _ { I S P , 1 } ~ = ~ 0$ and $\partial \pi _ { C P } ^ { ( A ) } / \partial t _ { C P } = 0$ simultaneously yields $t _ { I S P , 1 } ^ { * } = F + 2 6$ and $t _ { C P } ^ { * } = a _ { C D N } ^ { * } + 2 D _ { C P } / ( 2 - \alpha )$

Ensuring $0 < \underline { { \theta } } < \hat { \theta } < 1$ entails the following three conditions:

1. $0 < \underline { { { \sf { d } } } } \Leftrightarrow 0 < - ( 6 { \bf { a } } - 4 { \bf { a } } ^ { 2 } ) V _ { I S P , 1 } - ( 8 - 1 0 { \bf { a } } + 3 { \bf { a } } ^ { 2 } ) V _ { C P } - ( { \bf { a } } ^ { 2 } + 4 { \bf { a } } - 8 ) F + ( 3 { \bf { a } } ^ { 2 } + 3 { \bf { a } } ^ { 2 } ) V _ { I P } ,$ $- 2 6 \mathbf { a } + 3 2 )$

2. $\begin{array} { r } { \underline { { \theta } } < \hat { \theta } \Leftrightarrow 0 < ( 3 2 - 2 6 \mathrm { a } + 3 \mathrm { a } ^ { 2 } ) V _ { I S P , 1 } + 3 ( 8 - 1 0 \mathrm { a } + 3 \mathrm { a } ^ { 2 } ) V _ { C P } + ( - 1 2 \mathrm { a } ^ { 2 } + 5 6 \mathrm { a } - 3 \mathrm { a } ^ { 2 } ) V _ { I P } . } \end{array}$ $5 6 ) F - 3 ( 3 2 + 3 a ^ { 2 } - 2 6 a )$

3. $\hat { \Theta } < 1 \Leftrightarrow 0 < - ( 3 2 - 5 0 \mathbf { a } + 1 9 \mathbf { a } ^ { 2 } ) V _ { I S P , 1 } + ( 8 - 1 0 \mathbf { a } + 3 \mathbf { a } ^ { 2 } ) V _ { C P } + ( 2 4 - 4 0 \mathbf { a } + 6 5 0 \mathbf { a } ^ { 2 } ) V _ { I S P , 0 } .$ $1 6 \mathrm { { a } } ^ { 2 } ) F + ( 9 6 - 1 5 0 \mathrm { { a } } + 5 7 \mathrm { { a } } )$

Thus, $0 < \underline { { \theta } } < \hat { \theta } < 1$ holds if and only if $M a x \{ L _ { 1 } , L _ { 3 } \} < V _ { C P } < L _ { 2 }$ , where

$$
L _ {1} \equiv \frac {(3 2 - 5 0 \alpha + 1 9 \alpha^ {2}) V _ {I S P , 1} - (2 4 - 4 0 \alpha + 1 6 \alpha^ {2}) F - (9 6 - 1 5 0 \alpha + 5 7 \alpha^ {2})}{(8 - 1 0 \alpha + 3 \alpha^ {2})},
$$

$$
L _ {2} \equiv \frac {- (6 \alpha - 4 \alpha^ {2}) V _ {I S P , 1} - (\alpha^ {2} + 4 \alpha - 8) F + (3 \alpha^ {2} - 2 6 \alpha + 3 2)}{(8 - 1 0 \alpha + 3 \alpha^ {2})},
$$

and

$$
L _ {3} \equiv \frac {- (3 2 - 2 6 \alpha + 3 \alpha^ {2}) V _ {I S P , 1} + (1 2 \alpha^ {2} - 5 6 \alpha + 5 6) F + 3 (3 2 + 3 \alpha^ {2} - 2 6 \alpha)}{3 (8 - 1 0 \alpha + 3 \alpha^ {2})}.
$$

The same procedure can be applied to other cases when a validity check for $\hat { \boldsymbol { \theta } }$ is needed.

## Proof of Lemma 2

Solving $\begin{array} { r l r } { \partial \pi _ { I P B , 1 } ^ { ( B ) } / \partial a _ { I B P , 1 } } & { { } = } & { 0 } \end{array}$ yields $a _ { I B P , 1 } ^ { \ast } = ( - \alpha V _ { I S P , 1 } + ( 4 - 3 \alpha ) V _ { C P } +$ $( 4 - 3 \alpha ) c _ { o } + 3 \alpha ) \big / ( 2 ( 4 - 3 \alpha ) )$ . Then, by incorporating $a _ { I B P , 1 } ^ { * }$ into (4) and (6), solving $\partial \pi _ { I P B , 1 } ^ { ( B ) } / \partial t _ { I S P , 1 } ~ = ~ 0$ and $\partial \pi _ { C P } ^ { ( B ) } / \partial t _ { C P } ~ = ~ 0$ simultaneously yields $t _ { I S P , 1 } ^ { * } ~ = ~ 2 \hat { 6 }$ and $t _ { C P } ^ { * } = a _ { I B P , 1 } ^ { * } + 2 D _ { C P } / ( 2 - a )$

## Proof of Lemma 3

Following the process described in Lemma 2, we have $t _ { I S P , 1 } ^ { * } ~ = ~ F ~ + ~ 2 \hat { \Theta } ,$ $t _ { C P } ^ { * } = a _ { I B P , 1 } ^ { * } + 2 D _ { C P } / ( 2 - \mathfrak { a } )$ and $a _ { I B P , 1 } ^ { * } = ( - \mathsf { a } V _ { I S P , 1 } + ( 4 - 3 \mathsf { a } ) V _ { C P } + 3 \mathsf { a }$ $+ ( 4 - 3 \alpha ) c _ { o } + 2 \alpha p ) \big / ( 2 ( 4 - 3 \alpha ) )$

## Proof of Proposition 1

ISP-1’s profit in scenario (B) is given by $\pi _ { I S P , 1 } ^ { ( B ) } ~ = ~ 2 { \bf a } \cdot \hat { \mathrm {  ~ \theta ~ } } \hat { \mathsf { \boldsymbol { \theta } } } ^ { 2 } ~ - ~ c _ { t } ~ \cdot ~ \mathrm {  ~ a ~ } _ { \cdot }$ , where $\hat { \theta } = \Delta / ( 4 ( 4 - 3 \mathbf { a } ) ( 8 - 5 \mathbf { a } ) )$ . Moreover, ISP-1’s profit in scenario (C) is given by $\pi _ { I S P , 1 } ^ { ( C ) } = 2 { \bf a } \cdot \hat { \bf \theta } ^ { 2 } + ( p - c _ { t } ) \cdot { \bf a } - M ,$ where $\hat { \theta } = ( \Delta - ( 3 2 + 2 0 \alpha ^ { 2 } - 5 2 \alpha ) p ) / ( 4 ( 4 - 3 \alpha )$ $\left( 8 - 5 \alpha \right) )$ . We complete the proof by examining $\pi _ { I S P , 1 } ^ { ( C ) } - \pi _ { I S P , 1 } ^ { ( B ) }$

## Proof of Proposition 2

Similar to the proof of Proposition 1, we examine $\pi _ { C P } ^ { ( A ) } - \pi _ { C P } ^ { ( B ) }$ because $\pi _ { C P } ^ { ( B ) } = \pi _ { C P } ^ { ( C ) }$ We have $\pi _ { C P } ^ { ( B ) } = 2 D _ { C P } ^ { 2 } / ( 2 - \alpha )$ , where

$$
D _ {C P} = \frac {\left(\alpha^ {2} - 2 \alpha\right) V _ {I S P , 1} + (3 \alpha^ {2} - 1 0 \alpha + 8) V _ {C P} - (3 \alpha^ {2} - 1 0 \alpha + 8) c _ {o} + (6 \alpha - 3 \alpha^ {2})}{4 (8 - 5 \alpha)},
$$

and $\pi _ { C P } ^ { ( A ) } = 2 D _ { C P } ^ { 2 } / ( 2 - \mathfrak { a } )$ , where

$$
D _ {C P} = \frac {\left(\alpha^ {2} - 2 \alpha\right) V _ {I S P , 1} + \left(3 \alpha^ {2} - 1 0 \alpha + 8\right) V _ {C P} - \left(4 \alpha^ {2} - 1 2 \alpha + 8\right) F + \left(6 \alpha - 3 \alpha^ {2}\right)}{4 (8 - 5 \alpha)}.
$$

When $\pi _ { C P } ^ { ( A ) } \geq \pi _ { C P } ^ { ( B ) } \Rightarrow F / c _ { o } \leq ( 3 { \mathfrak a } ^ { 2 } - 1 0 { \mathfrak a } + 8 ) / ( 4 { \mathfrak a } ^ { 2 } - 1 2 { \mathfrak a } + 8 )$

## Proof of Corollary 2

With IBP-1 taking the role of a CDN, it can be assumed that IBP-1 can pay a nearby ISP to deliver video streaming to ISP-1. Given the market price $F ,$ the profit for IBP-1 in this “detoured” case can be specified by

$$
\begin{array}{c} \pi_ {I B P, 1} = (a _ {I B P, 1} - F) \alpha \Big (1 - \hat {\theta} \Big) + (a _ {I B P, 1} - c _ {o}) (1 - \alpha) (1 - \underline {{\theta}}) - M \\ = (a _ {I B P, 1} - F) D _ {C P} + (F - c _ {o}) (1 - \alpha) (1 - \underline {{\theta}}) - M. \end{array}
$$

The expression above is the same as in Case B, except that the cost of delivering traffic to ISP-1 is replaced with F. Our goal is to find the root $\operatorname { o f } p$ such that $\pi _ { I B P , 1 }$ in the “detoured” case is the same as that in Case C. Given $\pi _ { I S P , 1 } ^ { ( B ) } = \pi _ { I S P , . } ^ { ( C ) }$ holds when $p$ $= 0 .$ , it can be inferred that $\pi _ { I S P , 1 } ^ { ( C ) } > \pi _ { I B P , 1 } ^ { ( d e t o u r e d ) }$ when $p = 0$ because $F > c _ { o }$ . Thus, there exists a value of $\dot { p }$ such that $\pi _ { I S P , 1 } ^ { ( C ) } = \pi _ { I B P , 1 } ^ { ( d e t o u r e d ) }$ because $\partial ^ { 2 } \pi _ { I S P } ^ { ( C ) } / \partial p ^ { 2 } < 0$ . Solving $\pi _ { I S P , 1 } ^ { ( C ) }$ 1 $= \pi _ { I B P , 1 } ^ { ( d e t o u r e d ) }$ yields

$$
\pi_ {I B P} ^ {(C)} - \pi_ {I B P} ^ {(d e t o u r e d)} = \frac {\alpha}{8 (4 - 3 \alpha) (8 - 5 \alpha)} \cdot \left\{8 p \left(V _ {I S P, 1} - 3 - p\right) (1 - \alpha) (8 - 5 \alpha) + \psi \right\}, \text {   where   }
$$

$$
\begin{array}{l} \Psi \equiv (F - c _ {o}) \{(6 - 2 V _ {I S P, 1}) (1 9 \alpha^ {2} - 5 0 \alpha + 3 2) + (2 V _ {C P} (4 - 3 \alpha) - (\alpha F + 8 c _ {o} - 7 \alpha c _ {o})) (2 \\ - \alpha) \}. \end{array}
$$

Choose the highest root of $p$ because $\partial \pi _ { I S P , 1 } ^ { ( C ) } / \partial p > 0$ , and we have

$\begin{array} { r } { p ^ { * } \ = \ V _ { I S P , 1 } \ - \ 3 / 2 \ + \ \sqrt { \frac { \left( 2 \left( 1 - \alpha \right) \left( 8 - 5 \alpha \right) \left( V _ { I S P , 1 } - 3 \right) ^ { 2 } + \Psi \right) } { 8 \left( 1 - \mathbf { a } \right) \left( 8 - 5 \mathbf { a } \right) } } . } \end{array}$ . Note that CP will stay with the incumbent CDN when $F / c _ { o } \leq ( 3 \alpha ^ { 2 } - 1 0 \alpha + 8 ) / ( 4 \alpha ^ { 2 } - 1 2 \alpha + 8 )$ so that $p ^ { * }$ is valid only if $\alpha < 4 ( F - c _ { o } ) / ( 4 F - 3 c _ { o } )$ . From the expression for $p ^ { * }$ , analyzing the sign of ${ \partial p ^ { * } } / { \partial \alpha }$ is equivalent to analyzing that of ${ \partial / \partial \alpha ( \Psi / ( ( 1 - \alpha ) ( 8 - 5 \alpha ) ) } )$ Thus, we have ∂/∂α $( \Psi / ( 1 - \alpha ) ( 8 - 5 \alpha ) ) = ( F - c _ { o } ) \cdot \Gamma / ( ( 1 - \alpha ) ^ { 2 } ( 8 - 5 \alpha ) ^ { 2 } )$ , where $\Gamma \equiv 6 ( 4 - 3 \alpha ) ( 4 - \alpha ) + ( 4 8 - 6 4 \alpha + 2 2 \alpha ^ { 2 } ) V _ { C P } - ( 3 2 - 4 8 \alpha + 1 9 \alpha ^ { 2 } ) c _ { o } - ( 4 - 3 \alpha ) ( 4 - \alpha )$ $( 2 V _ { I S P , 1 } + F )$

Notice that $\partial p ^ { * } / \partial { \bf a } > 0 \mathrm { i f } \Gamma | _ { \alpha = 0 } > 0$ and $\partial \Gamma / \partial \mathbf { q } > 0$ for ${ \mathfrak { a } } \in ( 0 , 1 )$ . Accordingly, we verify the two conditions as follows:

$$
1. \Gamma | _ {\alpha = 0} = 9 6 + 4 8 V _ {C P} - 3 2 V _ {I S P, 1} - 3 2 c _ {o} - 1 6 F
$$

$$
1 - \hat {\theta} > 0 \Leftrightarrow (9 6 - 1 5 0 \alpha + 5 7 \alpha^ {2}) - (3 2 - 5 0 \alpha + 1 9 \alpha^ {2}) V _ {I S P, 1} + (8 - 1 0 \alpha + 3 \alpha^ {2})
$$

$$
(V _ {C P} - c _ {o}) + (F - c _ {o}) \left(\alpha^ {2} - 2 \alpha\right) > 0 \Rightarrow 9 6 - 3 2 V _ {I S P, 1} + 8 \left(V _ {C P} - c _ {o}\right) > 0
$$

$$
\alpha \approx 0 \Rightarrow \Gamma | _ {\alpha = 0} > 0;
$$

$$
\begin{array}{l} 2. \partial \Gamma / \partial \alpha = (6 4 - 4 4 \alpha) V _ {C P} - (3 2 - 1 2 \alpha) V _ {I S P, 1} + (9 6 - 3 6 \alpha - 4 8 c _ {o} - 1 6 F + 3 8 \alpha c _ {o} \\ + 6 \alpha F). \end{array}
$$

When $V _ { C P } > V _ { I S P , 1 }$ and the cost parameters (namely, $F$ and $c _ { o } )$ are sufficiently low, we have $\partial \Gamma / \partial { \bf a } > 0$ , or $\partial p ^ { * } / \partial { \bf a } > 0$

![](/api/attachments/B4NSYJB2/fulltext/images/f667e86bf85ca873e10f48c14b29375485ba57e5f9ce44b452cb178b18ec0790.jpg)  
Figure A1. p\*(F = 0.1, c<sub>o</sub> = 0.02, α = 0.2)

![](/api/attachments/B4NSYJB2/fulltext/images/ad715b6b66e557850ee73e3781396f0b6d4c374653c9302faa73aa4db42f761a.jpg)  
Figure A2. ∂ p\*/∂α (F = 0.1, c<sub>o</sub> = 0.02, α = 0.2)

![](/api/attachments/B4NSYJB2/fulltext/images/000bdb8280a85c9004646a99d2379935c62257be17b72bd31926edf44ad690d8.jpg)  
Figure A3. $p ^ { * } \left( F = 0 . 1 \right.$ $c _ { o } = 0 . 0 5$ 4 $V _ { I S P , 1 } = 2 . 5 ,$ and $V _ { C P } = 2 )$

We now examine ${ \partial p ^ { * } } / { \partial { \bf { q } } }$ numerically. In Figure A1 and Figure A2 we plot $p ^ { * }$ and ${ \partial p ^ { * } } / { \partial { \bf { q } } }$ and all values are positive. In Figure A3 we observe how $p ^ { * }$ changes with ${ \mathfrak { a } } ,$ which also shows that $p ^ { * }$ increases with α even if $V _ { C P } < V _ { I S P , 1 }$

Proof of Proposition 3 In paid peering, we have $\pi _ { I S P , 1 } ^ { ( C ) } = 2 \alpha \widehat { \boldsymbol { \theta } } _ { ( C ) } ^ { 2 } + ( \boldsymbol { p } - \boldsymbol { c } _ { t } ) \cdot \boldsymbol { \alpha } - M ,$ where

$$
\hat {\theta} ^ {(C)} = \frac {(3 2 - 2 6 \alpha + 3 \alpha^ {2}) + (3 2 - 5 0 \alpha + 1 9 \alpha^ {2}) V _ {I S P , 1} - (8 - 1 0 \alpha + 3 \alpha^ {2})}{(V _ {C P} - c _ {o}) - (3 2 - 5 2 \alpha + 2 0 \alpha^ {2}) p}   \frac {}{4 (4 - 3 \alpha) (8 - 5 \alpha)}.
$$

In free peering with infrastructure and hardware upgrades, denoted as case $B ^ { \prime }$ with ISP-1’s profit function in Case B being replaced with $\pi _ { I S P , 1 } = ( t _ { I S P , 1 } - c _ { t } ) \mathbf { a } \cdot \hat { \mathbf { \boldsymbol { \theta } } }$ , we have $\pi _ { I S P , 1 } ^ { ( B \prime ) } = 2 \alpha \hat { \boldsymbol { \theta } } ^ { 2 ^ { ( B \prime ) } }$ , where

$$
\hat {\theta} ^ {(B ^ {\prime})} = \frac {(3 2 - 2 6 \alpha + 3 \alpha^ {2}) + (3 2 - 5 0 \alpha + 1 9 \alpha^ {2}) V _ {I S P , 1} - (8 - 1 0 \alpha + 3 \alpha^ {2})}{(V _ {C P} - c _ {o}) - (3 2 - 5 0 \alpha + 1 9 \alpha^ {2}) c _ {t}}   \frac {(V _ {C P} - c _ {o}) - (3 2 - 5 0 \alpha + 1 9 \alpha^ {2}) c _ {t}}{4 (4 - 3 \alpha) (8 - 5 \alpha)}.
$$

When ${ \mathfrak { a } } \approx 0 .$ , we have $\pi _ { I S P , 1 } ^ { ( B \prime ) } > \pi _ { I S P , 1 } ^ { ( C ) }$ . On the other hand, we have

$$
\hat {\theta} ^ {(C)} - \hat {\theta} ^ {(B ^ {\prime})} = \frac {- (3 2 - 5 2 \alpha + 2 0 \alpha^ {2}) p}{4 (4 - 3 \alpha) (8 - 5 \alpha)} + \frac {(3 2 - 5 0 \alpha + 1 9 \alpha^ {2}) c _ {t}}{4 (4 - 3 \alpha) (8 - 5 \alpha)} > 0 \text {   if   } \alpha = 1.
$$

In addition, let $\mathbf { \boldsymbol { \mathbf { \varepsilon } } } _ { \mathbf { \boldsymbol { \mathbf { \varepsilon } } } } \equiv \boldsymbol { p } - \boldsymbol { c } _ { t } ,$ and we have

$$
\begin{array}{c} \frac {\partial \hat {\theta} ^ {(C)}}{\partial \alpha} - \frac {\partial \hat {\theta} ^ {(B ^ {\prime})}}{\partial \alpha} = \frac {\partial}{\partial \alpha} \frac {- (3 2 - 5 2 \alpha + 2 0 \alpha^ {2}) p}{4 (4 - 3 \alpha) (8 - 5 \alpha)} + \frac {\partial}{\partial \alpha} \frac {(3 2 - 5 0 \alpha + 1 9 \alpha^ {2}) c _ {t}}{4 (4 - 3 \alpha) (8 - 5 \alpha)} \\ = \frac {1}{2} \left\{\frac {3 2 - 3 2 \alpha + 7 \alpha^ {2}}{(4 - 3 \alpha) ^ {2} (8 - 5 \alpha) ^ {2}} \right\} c _ {t} + \frac {1 2 8 - 1 6 0 \alpha + 5 0 \alpha^ {2}}{2 (4 - 3 \alpha) ^ {2} (8 - 5 \alpha) ^ {2}} \cdot \varepsilon . \end{array}
$$

We can confirm that (1) $\hat { \sigma } \hat { \boldsymbol { \Theta } } ^ { ( C ) } / \hat { \sigma } \mathbf { a } > \hat { \sigma } \hat { \boldsymbol { \Theta } } ^ { ( B ^ { \prime } ) } / \hat { \sigma } \mathbf { a }$ when $p > c _ { t } ,$ and $( 2 ) \hat { \boldsymbol { \theta } } ^ { ( C ) } > \hat { \boldsymbol { \theta } } ^ { ( B ^ { \prime } ) }$ when ${ \mathfrak { a } } = 1 . { \mathrm { B y } } \left( 1 \right)$ and (2), we have $\partial \pi _ { I S P , 1 } ^ { ( C ) } / \partial \mathbf { a } > \partial \pi _ { I S P , 1 } ^ { ( B \prime ) } / \partial \mathbf { a }$ when $p > c _ { t } .$ . That is, if $p > c _ { t }$ and M is not too high, there exists an upper bound $\bar { \mathsf { a } } < 1$ such that $\pi _ { I S P , 1 } ^ { ( C ) } > \pi _ { I S P , 1 } ^ { ( B \prime ) }$ when ${ \mathfrak { a } } > { \bar { \mathfrak { a } } }$

Proof of Lemma 5 Solving $\partial \pi _ { I S P , 1 } ^ { ( D 2 ) } / \partial t _ { I S P , 1 } = 0$ and $\partial \pi _ { C P } ^ { ( D 2 ) } / \partial t _ { C P } = 0$ simultaneously yields $t _ { I S P , 1 } ^ { * } = V _ { I S P , 1 } +$ $\underline { { \theta } } - 2 \hat { \Theta }$ and $t _ { C P } ^ { * } = V _ { C P } + \underline { { { \theta } } } - 1$

Proof of Proposition 4

To show $\pi _ { C P } ^ { ( D \bar { 2 } ) } \geq \pi _ { C P } ^ { ( D 1 ) }$ when $\Phi = a _ { C D N }$ is the same as showing $\partial \pi _ { C P } ^ { ( D 1 ) } / \partial F > 0$ , which is the case because $\pi _ { C P } ^ { ( D 1 ) } = 2 D _ { C P } ^ { 2 } / ( 2 - \mathfrak { a } )$ , where $D _ { C P } = ( 2 - \mathfrak { a } ) \big ( - \mathfrak { a } V _ { I S P , 1 } + ( 4 - 3 \mathfrak { a } )$ $V _ { C P } - ( 4 - 3 \alpha ) a _ { C D N } + ( 3 + F ) \alpha ) / ( 2 ( 8 - 5 \alpha ) )$

On the other hand, with $\pi _ { I S P , 1 } ^ { ( D 1 ) } = 2 \dot { \bf a } \hat { \theta } ^ { 2 } + ( F - c _ { t } ) \alpha$ and $\pi _ { I S P , 1 } ^ { ( D 2 ) } = 2 { \bf a } \hat { \Theta } ^ { 2 } + ( a _ { C D N } - c _ { t } ) { \bf a } -$ $S ,$ there exist $\alpha ^ { * }$ such that $\pi _ { I S P , 1 } ^ { ( D 2 ) } \ge \pi _ { I S P , 1 } ^ { ( D 1 ) }$ when ${ \mathrm { ~  ~ a ~ } } \geq { \mathrm { ~  ~ a ~ } } ^ { * }$ because ${ \partial \hat { \boldsymbol { \theta } } ^ { ( D 1 ) } } \mathord { \left/ { \vphantom { \partial \hat { \boldsymbol { \alpha } } \partial ^ { 1 } } \partial \alpha } \right. \kern - delimiterspace } \partial \alpha =$

$$
\left(6 - 2 V _ {I S P, 1} - V _ {C P} + 2 F + \alpha_ {C D N}\right) / (5 \alpha - 8) ^ {2} \leq \left(6 - 2 V _ {I S P, 1} - V _ {C P} + 3 \alpha_ {C D N}\right)
$$

$$
/ (5 \alpha - 8) ^ {2} = \partial \hat {\theta} ^ {D 2} / \partial \alpha .
$$

Proof of Lemma 6

Solving $\partial \pi _ { I S P , 1 } ^ { ( D 3 ) } / \partial t _ { I S P , 1 } = 0$ and $\partial \pi _ { C P } ^ { ( D 3 ) } / \partial t _ { C P } = 0$ simultaneously yields $t _ { I S P , 1 } ^ { * } = \hat { V } _ { I S P , 1 } +$ $\underline { { \theta } } - ( 1 + \lambda ) \hat { \Theta }$ and $t _ { C P } ^ { * } = V _ { C P } + \underline { { { \theta } } } - 1$

Proof of Proposition 5

$4 \lambda + 2 + 6 \gamma + 3 a _ { C D N } - 2 \hat { V } _ { I S P , 1 } - V _ { C P } > 0$ implies $\hat { \sigma } \hat { \boldsymbol { \Theta } } ^ { ( D 3 ) } / \hat { \sigma } \boldsymbol { \mathbf { a } } > 0$ because $\partial \hat { \boldsymbol { \theta } } ^ { ( D 3 ) } / \partial \mathbf { q } =$ $( 4 \lambda + 2 + 6 \gamma + 3 a _ { C D N } - 2 \hat { V } _ { I S P , 1 } - V _ { C P } ) / ( { \bf a } - 4 - 4 \lambda + 4 0 \lambda ) ^ { 2 }$ . Notice that Lemma 6 shows that $t _ { I S P , 1 } ^ { * } = ( 1 + \lambda ) \hat { \Theta } + \gamma + a _ { C D N }$ and $2 ( 1 + \lambda ) \hat { \Theta } = \hat { V } _ { I S P , 1 } - V _ { C P } - \gamma - a _ { C D N } + t _ { C P } ^ { * }$ $^ { + 1 }$ . Thus, the signs of $\partial t _ { I S P , 1 } ^ { * } / \partial \mathbf { a }$ and $\partial t _ { C P } ^ { * } / \partial \mathbf { a }$ are the same as that of $\partial { \hat { \boldsymbol { \theta } } } / \partial \mathbf { q }$

Proof of Proposition 6

Notice tha $\begin{array} { r } { \mathbf { \dot { \pi } } _ { I S P , 1 } ^ { ( D 2 ) } = 2 \mathbf { a } ( \hat { \boldsymbol { \Theta } } ^ { ( D 2 ) } ) ^ { 2 } + \mathbf { a } \cdot ( a _ { C D N } - c _ { t } ) - S , } \end{array}$ where

$$
\hat {\theta} ^ {(D 2)} = \frac {(4 - 3 \alpha) V _ {I S P , 1} - (2 - \alpha) V _ {C P} - (2 - 2 \alpha) a _ {C D N} + (4 - \alpha)}{2 (8 - 5 \alpha)}.
$$

In addition, $\pi _ { I S P , 1 } ^ { ( D 3 ) } = \mathfrak { a } ( 1 + \lambda ) ( \widehat { \Theta } ^ { ( D 3 ) } ) ^ { 2 } + \mathfrak { a } \cdot ( a _ { C D N } - c _ { t } ) - S ;$ , where

$$
\hat {\theta} ^ {(D 3)} = \frac {(2 - \alpha + 2 \lambda (1 - \alpha)) \hat {V} _ {I S P , 1} - (1 + \lambda (1 - \alpha)) V _ {C P} - (1 - \alpha) (1 + \lambda) a _ {C D N}}{+ (2 - \alpha) \lambda - 2 \gamma (1 - \alpha) (1 + \lambda) + 2} \\ \qquad \qquad \qquad \qquad \qquad \qquad (4 - \alpha + 4 \lambda (1 - \alpha)) (1 + \lambda).
$$

Thus, we can show the influences of bundled content and royalty payment by comparing the two equations.

Proof of Proposition 7 Notice that $\begin{array} { r } { \hat { \mathcal { O } } ^ { 2 } \ ( \pi _ { I S P , 1 } ^ { ( D 3 ) } + \pi _ { C P } ^ { ( D 3 ) } ) / \hat { \sigma } \gamma ^ { 2 } = - 2 ( 1 - \mathfrak { a } ) ( 5 \mathfrak { a } + 4 + 4 \lambda ( 1 - \mathfrak { a } ) ) \mathfrak { a } / ( 4 - \mathfrak { a } + 4 \lambda ( 1 - \mathfrak { a } ) ) , } \end{array}$ $\left( \mathsf { a } \right) ) ^ { 2 } < 0$ hints the maximal value of $\pi _ { I S P , 1 } ^ { ( D 3 ) } ~ + ~ \pi _ { C P } ^ { ( D 3 ) }$ can be found by solving $\partial \Big ( \pi _ { I S P , 1 } ^ { ( D 3 ) } + \pi _ { C P } ^ { ( D 3 ) } \Big ) \Big / \partial \gamma = 0$ , which yields

$$
\gamma^ {*} = \frac {(1 - \alpha) ((4 + \alpha + 4 \lambda (1 - \alpha)) (V _ {C P} - a _ {C D N}) + 4 \alpha (\hat {V} _ {I S P , 1} + \lambda)) + \alpha ((8 + \alpha) - 4 (1 - \alpha) a _ {C D N})}{2 (1 - \alpha) (4 + 5 \alpha + 4 \lambda (1 - \alpha))}.
$$

Therefore, we have $\partial \gamma ^ { * } \big / \partial \hat { V } _ { I S P , 1 } = 2 \mathbf { a } / ( 4 + 5 \mathbf { a } + 4 \lambda ( 1 - \mathbf { a } ) ) > 0 , \partial \gamma ^ { * } \big / \partial V _ { C P } =$ $( 4 + \mathfrak { a } + 4 \lambda ( 1 - \mathfrak { a } ) ) / ( 2 ( 4 + 5 \mathfrak { a } + 4 \lambda ( 1 - \mathfrak { a } ) ) ) > 0 , \ \hat { \sigma } \gamma ^ { * } / \hat { \sigma } \lambda = 8 \mathfrak { a } ( V _ { C P } - \hat { V } _ { I S P , 1 } - 1 )$ $( 1 - \mathsf { a } ) / ( 4 + 5 \mathsf { a } + 4 \lambda ( 1 - \mathsf { a } ) ) ^ { 2 } < 0$ , and

$$
\frac {\partial \gamma *}{\partial \alpha} = \frac {1 6 (\hat {V} _ {I S P , 1} - V _ {C P}) (1 - \alpha) ^ {2} (1 + \lambda) + 8 \lambda (1 - \alpha) (6 + 3 \alpha + 2 \lambda (1 - \alpha)) + 3 2 + 8 \alpha + 4 1 \alpha^ {2}}{2 (1 - \alpha) ^ {2} (4 + 5 \alpha + 4 \lambda (1 - \alpha)) ^ {2}} > 0.
$$

Although we treat $V _ { C P }$ and $\hat { V } _ { I S P , 1 }$ as independent variables in the static analysis, we can confirm $\partial \gamma ^ { * } / \partial V _ { I S P , 1 } > 0$ and $\partial \gamma ^ { * } / \partial V _ { C P } > 0$ because $\hat { V } _ { I S P , 1 }$ is positively associated with $V _ { C P }$ and $V _ { I S P , 1 }$

## Robustness Check for Figure 3

The purpose of the check is to show $\pi _ { I S P , 1 } ^ { ( C ) } > \pi _ { I S P , 1 } ^ { ( B ) }$ when α is sufficiently high and M is not too large. With $\pi _ { I S P , 1 } ^ { ( C ) } \approx \pi _ { I S P , 1 } ^ { ( B ) } - M < \pi _ { I S P , 1 } ^ { ( B ) }$ for small α $( \alpha \approx 0 )$ , the result shown in Figure 3 holds if we also show $\partial \pi _ { I S P , 1 } ^ { ( C ) } / \partial \alpha > \partial \pi _ { I S P , 1 } ^ { ( B ) } / \partial \alpha$ . With $\partial \pi _ { I S P , 1 } ^ { ( B ) } / \partial \alpha = - c _ { 1 } +$ $\partial ( 2 \alpha \hat { \boldsymbol { \theta } } ^ { 2 } ) / \partial \alpha$ and $\partial \pi _ { I S P , 1 } ^ { ( C ) } \Big / \partial \alpha = - p - c _ { t } + \partial \Big ( 2 \alpha \hat { \boldsymbol { \Theta } } ^ { 2 } \Big ) \Big / \partial \alpha ,$ , the inequality holds if $\partial / \partial \alpha ( ( 5 2 \alpha - 3 2 - 2 0 \alpha ^ { 2 } ) \cdot p / ( 4 ( 4 - 3 \alpha ) ( 8 - 5 \alpha ) ) ) > 0$ because $\hat { \theta } ^ { ( C ) } - \hat { \theta } ^ { ( B ) } =$ $( 5 2 \alpha - 3 2 - 2 0 \alpha ^ { 2 } ) \cdot p / ( 4 ( 4 - 3 \alpha ) ( 8 - 5 0 ) )$ . We complete the proof because $\partial / \partial \alpha \big ( ( 5 2 \alpha - 3 2 - 2 0 \alpha ^ { 2 } ) \cdot p / \big ( 4 ( 4 - 3 \alpha ) ( 8 - 5 \alpha ) \big ) \big ) = p \big / ( 4 - 3 \alpha ) ^ { 2 } > 0 .$

Incorporating the optimal peering fee $p ^ { * }$ from Corollary 2 into the robustness check, the result holds as long as $\partial p ^ { * } / \partial { \bf a } > 0 ,$ , which is the case under conditions outlined in Corollary 2. After also checking the sign of ${ \partial p ^ { * } } / { \partial { \bf { q } } }$ numerically, the result holds in much more general cases. To show $\pi _ { I S P , 1 } ^ { ( C ) ^ { - } } > \pi _ { I S P , } ^ { ( B ) }$ when α is sufficiently large, we use Figure A4 to demonstrate the robustness of the result by solving the indifferent value of α for $\pi _ { I S P , 1 } ^ { ( C ) } = \pi _ { I S P , 1 } ^ { ( B ) }$ . The parameters used in the graph are $F = 0 . 1 , M = 0 . 1 , V _ { I S P , 1 } =$ $2 . 5 , c _ { t } = c _ { o } = 0 . 0 5$ , and $2 \leq V _ { C P } \leq 3$

![](/api/attachments/B4NSYJB2/fulltext/images/1d8e8568a7f4775a3a1f4615aa26d547b3aac73d1a174b720c3d6cd29c8fa006.jpg)  
Figure A4. The Indifference Market Share Between Case B and Case C

In Figure $_ { \mathrm { A 4 , } }$ we first consider $p = 0 . 2$ and examine the indifferent market share under which $\pi _ { I S P , 1 } ^ { ( \bar { B } ) } = \pi _ { I S P , 1 } ^ { ( C ) }$ holds. ISP-1 adopts paid peering when its market share is higher than the threshold, and peers freely when the opposite holds. We also incorporate the optimal peering fee $p ^ { * }$ derived from Corollary 2. We have a similar result, but the indifferent market share is higher than when $p = 0 . 2$ . Because the value of $\dot { p } ^ { * }$ ranges between 0.168 and 0.184 (and lower than the original $p$ value of 0.2), ISP-1 will need a higher market share to offset the monitoring cost M.
