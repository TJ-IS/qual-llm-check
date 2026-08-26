---
otero_id: 15564
otero_key: "6ENPYBRB"
title: "Network Neutrality and Congestion Sensitive Content Providers: Implications for Content Variety, Broadband Investment, and Regulation"
authors: "Jan Krämer; Lukas Wiewiorra"
year: "2012"
journal: "Information Systems Research"
doi: "10.1287/isre.1120.0420"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/6ENPYBRB/fulltext/images/8dc4136f645f92a427f7f6aade4b1685fe0dfed449f181f4567cd4e36bfaf57c.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Network Neutrality and Congestion Sensitive Content Providers: Implications for Content Variety, Broadband Investment, and Regulation

Jan Krämer, Lukas Wiewiorra,

## To cite this article:

Jan Krämer, Lukas Wiewiorra, (2012) Network Neutrality and Congestion Sensitive Content Providers: Implications for Content Variety, Broadband Investment, and Regulation. Information Systems Research 23(4):1303-1321. http://dx.doi.org/10.1287/ isre.1120.0420

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2012, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/6ENPYBRB/fulltext/images/7ead5ea679294bcc08e776ca4ade86fda63d69f570e264c2669dde170580f97e.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Network Neutrality and Congestion Sensitive Content Providers: Implications for Content Variety, Broadband Investment, and Regulation

Jan Krämer, Lukas Wiewiorra

Karlsruhe Institute of Technology, Institute of Information Systems and Management, Karlsruhe, Germany {kraemer@kit.edu, wiewiorra@kit.edu}

W<sup>e</sup> <sup>study</sup> <sup>departures</sup> <sup>from</sup> <sup>network</sup> <sup>neutrality</sup> <sup>through</sup> <sup>implementing</sup> <sup>a</sup> <sup>quality</sup> <sup>of</sup> <sup>service</sup> <sup>tiering</sup> <sup>regime</sup> <sup>in</sup> which an Internet service provider charges for prioritization on a nondiscriminatory basis. We find that quality of service tiering may be more efficient in the short run because it better allocates the existing network capacity and in the long run because it provides higher investment incentives due to the increased demand for priority services by the entry of new congestion sensitive content providers. Which network regime is the most efficient depends on the distribution of congestion sensitivity among content providers, but a guideline is that the regime that provides higher incentives for infrastructure investments is more efficient in the long run.

Key words: telecommunications; net neutrality; quality of service; content variety; investment; regulation History: Published online in Articles in Advance May 7, 2012.

## 1. Introduction

The most controversial part of the net neutrality debate is the question of the future relationship between Internet service providers (ISPs) and content providers (CPs). We seek to investigate in particular whether ISPs should be allowed to offer CPs differentiated service classes for the transmission of their data packets to end customers—known as quality of service (QoS) tiering (Lessig 2001, p. 46; Hahn and Wallsten 2006). Under a network neutrality regime the prioritization of paid-for traffic would be prohibited, even if QoS tiering was offered on a nondiscriminatory basis.<sup>1</sup>

Proponents of network neutrality argue that only this regime can ensure a level playing field for competition among CPs and will thus lead to more content variety (Lessig 2001, pp. 168–175; Wu 2003; Van Schewick 2006; Sydell 2006). At a given transmission capacity, the acceleration of priority traffic will lead unmistakably to a deceleration of the remaining best-effort traffic. Thus, those CPs who are not willing to pay for priority access are put at a disadvantage because other providers’ content is accelerated in lieu of their own content. This disadvantage lies at the heart of the concern of network neutrality proponents. Moreover, advocates claim that in the long run, broadband infrastructure investments are likely to be higher under network neutrality because ISPs are forced to provide sufficient bandwidth in order to bring new content types on line and keep consumers satisfied (Lessig 2001, p. 47). They even express the fear that QoS tiering may in fact hinder the roll-out of additional transmission capacity because ISPs seek to charge CPs for exactly this resource, which is only possible if it is scarce (Wu and Yoo 2007, Choi and Kim 2010).

Opponents of a network neutrality regime argue to the contrary that QoS tiering will stimulate more content variety and broadband investment. A CP that offers an Internet telephony service, for example, is certainly more sensitive to network congestion than a simple email service provider.<sup>2</sup> Consequently, opponents argue that the best-effort one-size-fits-all transmission regime of a neutral network is not appropriate anymore (Yoo 2005). If customers’ experience of use is unsatisfactory because a CP’s service cannot be reliably offered, this CP’s advertisement revenues will decline, possibly up to the point where it is forced out of business (Crowcroft 2007). Hence,

QoS tiering may in fact be welfare enhancing because it explicitly enables entry by those innovative CPs who crucially hinge on transmission quality requirements that the traditional neutral best-effort Internet may soon be unable to provide. By contrast, net neutrality could in fact hinder entry of innovative CPs because congestion sensitive services can only be offered if they are sustainable under the besteffort domain. Furthermore, supporters of QoS tiering argue that investments in broadband infrastructure would be higher under this regime because CPs can be billed for the transmission quality they are using (Van Schewick 2006, Yoo 2005). Even if transmission capacity is not extended,<sup>3</sup> QoS tiering would still handle the existing capacity more efficiently.

In light of the arguments for and against network neutrality regulation, some observers have noted that the debate seems stuck in the sense that “at this point, it is impossible to foresee which architecture will ultimately represent the best approach” (Wu and Yoo 2007).<sup>4</sup> Nevertheless, the Federal Communications Commission (FCC) has issued a regulatory framework that prohibits QoS tiering (FCC 2010) and is challenged in courts. In an effort to advance the debate, we provide a formal economic framework that incorporates the arguments of either side. This allows us to compare QoS tiering with network neutrality in terms of their impacts on content variety, broadband investment, and overall welfare. More specifically, we model the Internet as a two-sided market (Armstrong 2006, Rochet and Tirole 2006) that connects congestion sensitive CPs with consumers and that is controlled by a monopolistic ISP.<sup>5</sup> Under network neutrality regulation all CPs experience the same transmission quality, whereas under the QoS tiering regime, every CP can choose to buy priority access to consumers on the same nondiscriminatory conditions. That is, discrimination occurs only between the best-effort and the priority class, but not within each class. In addition to the network externalities that are generated by either side, we explicitly consider the adverse effect that traffic prioritization has on the transmission quality of the remaining besteffort class as well as the positive effect that congestion is allocated away from the most congestion sensitive CPs. In this framework, we investigate the effects of QoS tiering both in the short run, when network capacity is fixed, as well as in the long run, when the ISP can strategically invest in broadband infrastructure.

Our main results are that in the short run QoS tiering will lead to the same level of content variety as does network neutrality if CPs’ congestion sensitivity is uniformly distributed in the Internet economy. However, because QoS tiering allocates congestion better to the congestion insensitive CPs, overall short run welfare is generally higher under this regime. Nevertheless, it should also be clear that QoS tiering enables ISPs to expropriate some of the CPs’ revenues, and thus, in the short run, all CPs are worse off under QoS tiering than under network neutrality. Indeed, this fact has driven much of the emotionality in the debate.<sup>6</sup> Although the shift of revenues from CPs to the ISP is welfare neutral per se, it will generally still need to be scrutinized by policy makers in order to evaluate the consequences.

Furthermore, our analysis reveals that QoS tiering is likely to result in higher investments in network infrastructure in the long run. The reason is that higher network capacity encourages more entry by CPs, whose additional demand keeps the value of the priority service high. This result contrasts the findings of Cheng et al. (2011) and Choi and Kim (2010) who do not consider entry of new (congestion sensitive) CPs and therefore find that the ISP has an incentive to keep the value of the priority service high by making network capacity scarce.

Finally, we also investigate the threat of strategic quality degradation and the effectiveness of minimum quality standards (MQS) in this context. Proponents of net neutrality are concerned that the ISP may have an incentive to degrade the transmission quality of the best-effort class even below its technical ability in order to drag CPs into a pay for priority agreement. We find that strategic quality degradation is only a profitable strategy for the ISP if consumers’ marginal valuation for content variety is sufficiently small. In this case, an MQS policy can safeguard the positive welfare effects of QoS tiering. However, if strategic quality degradation is not an issue (e.g., in the presence of effective transparency obligations), we find that an MQS policy that requires the ISP to guarantee a congestion level in the best-effort class under QoS tiering that is at least as good as the best-effort congestion level under network neutrality is not sufficient to guarantee efficient infrastructure investments.

The remainder of this article is structured as follows. In §2 we discuss our framework in the context of related work before we formally introduce the model in §3. Next, we investigate the differences between the QoS tiering and network neutrality regimes in the short run with respect to content variety (§4) and in the long run with respect to broadband investments (§5). In §6 we consider the scope for regulatory intervention and particularly discuss whether an MQS is an appropriate policy instrument in this context. Finally, in $\ S \bar { 7 }$ we comment on the possibility of strategic quality degradation under QoS tiering before we conclude in §8 by summarizing our results.

## 2. Related Work

Compared to the total number of academic papers that have been published in the context of the net neutrality debate, the number of formal economic papers within this domain is rather small. Schuett (2010) provides a comprehensive overview of this literature. The first formal approach to investigating net neutrality regulations is Economides and Tåg (2008), who consider a simple two-sided market model. On one side of the market, there is a continuum of noncompeting CPs and on the other side of the market, there is a continuum of consumers. Each side experiences positive network externalities through the presence of the other side. This is similar to our set-up; however, the authors do not consider a QoS tiering regime and instead see a violation of network neutrality in the ISP’s practice of charging CPs a termination fee for access to its customers.

Cheng et al. (2011) and Choi and Kim (2010) investigate the head-to-head competition of CPs and the ISP’s incentive to invest in network infrastructure under QoS tiering. Like us, they employ standard results from queuing theory to formalize the relationship between priority and best-effort traffic. However, their model set-up differs substantially from ours. The authors investigate the effect of QoS tiering on the competition of CPs that offer similar services. In their models, exactly two competing CPs are located at the end of a standard Hotelling line and it is assumed that customers dislike congestion and visit one of the two CPs exclusively (e.g., consumers either use Google or Bing, but never both). In contrast, our model studies the impact of QoS tiering on the variety of the available content on the Internet. The CPs in our model are not in direct competition to each other but offer heterogeneous services that differ in their sensitivity toward congestion. In other words, whereas Cheng et al. (2011) and Choi and Kim (2010) intend to study the impact of QoS tiering on a particular content submarket, we seek to study the effect of QoS tiering on the content market as a whole.

One of the important features of our model is that content variety (i.e., how many CPs choose to join the network in equilibrium) is determined endogenously.

This allows us to study the effect of QoS tiering on content variety, which is not possible in Cheng et al. (2011) and Choi and Kim (2010). In this respect, our model is similar to that of Jamison and Hauge (2008) and Hermalin and Katz (2007). However, in contrast to our model, Jamison and Hauge (2008) focus on the question of whether transmission quality can substitute for content quality. Moreover, they assume that the current network capacity will inevitably increase with the introduction of QoS, such that the transmission quality of the best-effort class is not affected (nondegradation condition). We study the ISP incentives to invest absent this condition but also consider a similar case where a minimum quality standard is enforced. In the model of Hermalin and Katz (2007), CPs differ in their value to consumers but do not differ in their sensitivity towards congestion. Also, their model neither explicitly studies investment incentives nor considers the inter-class externality that the high priority class exerts on the remaining best-effort class under fixed network capacity. In the subsequent paper of Economides and Hermalin (2010), which rests on the same principal modeling assumptions as Hermalin and Katz (2007), inter-class externalities are explicitly considered; however, much of the analysis is now based on the implicit assumption that content variety is exogenous and the same under net neutrality and QoS tiering. The clear focus of Economides and Hermalin (2010) is to show the negative impact of the so-called re-congestion effect on overall congestion under QoS tiering. The re-congestion effect describes that those CPs that are prioritized under a QoS tiering regime will receive even more consumer requests and thus generate more traffic than under net neutrality, which in turn re-congests the network. Our paper instead focuses on the reallocation effect, by which QoS tiering enables to allocate congestion away from the congestion sensitive and to the congestion insensitive CPs.

Although all of the models discussed here consider important facets of the net neutrality debate, none has addressed the issues of congestion sensitivity, inter-class externality, endogenous entry by CPs (content variety), and investment incentives by the ISP together. Accordingly, previous results with respect to content variety, network investment, and welfare are mixed: Hermalin and Katz (2007), who neglect interclass externality, find that network neutrality leads to less content variety in the short run and has a tendency to be welfare reducing. Jamison and Hauge (2008), who assume that the ISP invests more under QoS tiering, find that QoS tiering increases content variety. Cheng et al. (2011) and Choi and Kim (2010), who neglect endogenous entry and exit of ${ \mathrm { C P s } } ,$ show for a large range of parameters that the $\mathrm { I S P ^ { \prime } s }$ incentive to invest in infrastructure is higher under network neutrality, whereas QoS tiering is generally welfareenhancing in the short run.

Our paper complements these previous approaches and finds that because of inter-class externalities and better allocation of congestion, QoS tiering may be the more efficient regime in the short run. Also in the long run, it provides higher incentives for broadband investments because the entry by new, congestion sensitive CPs creates additional demand for the priority service that is absent under network neutrality. However, if the mass of congestion sensitive CPs is very large, then the priority service might get so overcrowded that the overall situation under QoS tiering is worse than under net neutrality. In effect this is similar to a re-congestion of the priority lane and thus the welfare conclusions of Economides and Hermalin (2010) are similar to ours: If the re-congestion effect is not too strong, QoS tiering provides higher investment incentives, leads to more content variety, and is thus likely to be the more efficient regime in the long run.

## 3. The Model

We model the Internet as a two-sided market, with CPs and Internet customers on either side, each of which value an increasing presence of the other side and dislike network congestion. We assume that the ISP has a terminating monopoly over its customers (e.g., because of the customers’ lack of alternative ISPs or high switching costs), which is reasonable for many regions in the United States and Europe. Therefore, the only way for the CPs to reach these customers is through the ISP’s network. Although the CPs’ customer base is probably composed of customers of many different ISPs, each of which might have a terminating monopoly, it is still insightful to investigate the relationship between CPs and a single ISP, particularly if that ISP is thought to be large. For example, it would certainly have a substantial impact on CPs’ business model if they would not have access to customers on AT&T’s network. Note that we only consider charges to the CPs that are above and beyond those for access to the Internet. Thus, we consider net neutrality as a zero price rule, which implies that the ISP cannot charge CPs additionally for terminating traffic in its network. Furthermore, we consider the politically relevant case where the best-effort lane under QoS tiering remains to be offered for zero additional cost.

Content Providers. We consider a continuum of CPs. Whatever service the CPs offer, they provide it for free and receive revenues only indirectly through online advertisements.<sup>7</sup> In the model, a CP’s advertisement revenue will depend on the average received traffic; the per-click advertisement revenue; and its individual click-through-rate, which is determined by the CP’s innate sensitivity towards network congestion. Before these measures are formally introduced below, we make one fundamental assumption:

<sup>Assumption</sup> <sup>1.</sup> Each CP receives the same average traffic from each customer, denoted by . This is independent of a content provider’s business model and consequently its innate sensitivity to network congestion.

For the remainder of this article, it will often be convenient to think of  as the number of “clicks” that a customer generates on each CP’s website. This assumption provides a neutral reference case with respect to the traffic that is generated by the specific CPs and with respect to the value of the individual content of the CPs. The relationship between congestion sensitivity of a CP and the amount of traffic that this CP generates is far from obvious. For example, VoIP services are highly congestion sensitive (in terms of jitter, delay, packet loss) but generate comparably very little traffic. Likewise, file hosting services are highly traffic intensive but not congestion sensitive. On the one hand, Assumption 1 avoids establishing such a relationship between the traffic that a CP generates and its congestion sensitivity, which would otherwise inevitably bias the analysis. This allows us to assess QoS tiering based on its core ability, i.e., increasing transmission quality (not bandwidth). On the other hand, Assumption 1 also avoids making any judgment about the value of specific content or services to consumers. In our model, CPs offer heterogeneous services that are all equally cherished by customers. Therefore it is reasonable to assume that customers distribute their clicks evenly among the available CPs.

In this context, it is important to highlight that we do not intend to study the effect of QoS tiering on the direct competition between otherwise similar CPs. This is done by Cheng et al. (2011) and Choi and Kim (2010). Instead, we seek to complement their analysis and study the effect of QoS tiering on content variety. Therefore, Assumption 1 implies that we abstract from any business stealing effects. More specifically, in what follows, we assume that  is constant, and thus as the number of active CPs increases, consumers also increase their total number of clicks accordingly. Alternatively, we could have assumed that the consumers’ total number of clicks is fixed and thus  diminishes as the variety of content increases. This would introduce a general notion of competitive pressure among the CPs; i.e., as more CPs enter the market, the revenue of each CP is reduced, everything else being constant. However, we believe that a constant  is more intuitive in the context of our analysis and note that the results of either assumption are qualitatively the same.<sup>8</sup> Instead, we have modeled such competitive pressure through diminishing ad revenues as described below.

Eventually, on the CP’s end, only a fraction of these clicks can be turned into advertisement revenue. This measure is known as the click-through rate. We assume that each CP’s click-through rate diminishes as network congestion increases. Moreover, each CP’s business model has an innate sensitivity as to what extent network congestion affects the click-through rate. For example, a Web-based email provider is likely to be relatively insensitive to network congestion. Consumers that arrive on the website are satisfied with the service even under high network congestion and more likely to click on advertisements. In contrast, consumers of a highly congestion sensitive Web service (e.g., TV streaming) may still arrive at the $\mathrm { C P ^ { \prime } s }$ website but are in the presence of network congestion less satisfied with the service and therefore less likely to view advertisements. This individual congestion sensitivity is denoted by  and the corresponding click-through rate of a CP is assumed to be 41 − w5, where w denotes the CP’s perceived average level of network congestion.<sup>9</sup> There exists a continuum of CPs with unit mass and distribution function $F ( \theta ) \colon [ 0 , 1 ] \to [ 0 , 1 ]$ . Let r be the average revenue-per-click on advertisements depending on the mass of active CPs in the market; then each CP’s profit under net neutrality is<sup>10</sup>

$$
\Gamma_ {N} (\theta) = \left\{ \begin{array}{l l} (1 - \theta w _ {N}) \lambda \bar {\eta} r & \text { if   active } \\ 0 & \text { otherwise }, \end{array} \right.\tag{1}
$$

where $\bar { \eta }$ denotes the share of Internet customers in equilibrium. Under network neutrality all CPs perceive the same level of congestion, $w _ { N }$ . In the QoS tiering regime, however, CPs can opt for the priority transmission class with $w _ { Q 1 } < w _ { N }$ at a price of p per click. The CPs that remain in the best-effort class, on the other hand, experience a higher congestion level $w _ { Q 2 } > w _ { N }$

$$
\Gamma_ {Q} (\theta) = \left\{ \begin{array}{l l} (1 - \theta w _ {Q 2}) \lambda \bar {\eta} r & \\ \quad \text { if   active   in   best - effort   class } & \\ (1 - \theta w _ {Q 1}) \lambda \bar {\eta} r - \lambda \bar {\eta} p & \\ \quad \text { if   active   in   priority   class } & \\ 0 & \text { otherwise. } \end{array} \right.\tag{2}
$$

The CP that is indifferent between choosing the priority and the best-effort transmission class under a QoS tiering regime is denoted by <sup>˜</sup>. Furthermore, in both regimes, the CP that is indifferent between becoming active and staying out of the market is characterized by a congestion sensitivity of <sup>¯</sup>. Thus F 45<sup>¯</sup> reflects the mass of all active CPs (content variety) and the share of CPs choosing the priority class under a QoS tiering regime is given by $\bar { \beta } \equiv 1 - \mathrm { \tilde { \cal F } } ( \tilde { \theta } ) / F ( \bar { \theta } )$

We assume a competitive advertisement market, which introduces an indirect element of competition between the CPs. More specifically, it is assumed that the level of CPs’ gross advertisement revenues depends on the mass of active CPs, i.e., $r ( F ( { \bar { \theta } } ) )$ and that $\partial r ( \cdot ) / \partial F ( \bar { \theta } ) \leq 0$

Customers. Internet customers value basic connectedness to the Internet as well as the presence of many CPs. In particular, we assume that connectedness adds a base utility of $b > 0$ , whereas each additional CP adds a marginal utility of $v > 0$ to a customer’s utility. In reverse, congestion diminishes a customer’s utility of using the ${ \check { \mathrm { C P s ^ { \prime } } } }$ services. To keep the analysis as clear as possible, we assume that consumers’ utility is determined only by the average congestion level $w _ { Q } = \beta w _ { Q 1 } + ( 1 - \beta ) w _ { Q 2 }$ or $w _ { N } ,$ respectively. This implies that $w _ { Q } = w _ { N }$ in the short run (when $\mu _ { Q } =$ $\mu _ { N } )$ whenever $\bar { \theta } _ { N } = \bar { \theta } _ { Q }$ . Alternatively, we could have assumed that customers are congestion sensitive as well and instead evaluated the level of congestion as $\begin{array} { r } { \hat { w } _ { N } = \int _ { \theta = 0 } ^ { \theta } w _ { N } \theta f ( \theta ) } \end{array}$ d and $\begin{array} { r } { \hat { w } _ { Q } = \int _ { \theta = 0 } ^ { \theta } w _ { Q 2 } \theta f ( \theta ) d \theta + } \end{array}$ $\begin{array} { r } { \int _ { \theta = \tilde { \theta } } ^ { \tilde { \theta } } w _ { Q 1 } \theta f ( \theta ) d \theta , } \end{array}$ , respectively. Although reasonable, this assumption would qualitatively not change our analysis but merely emphasize the advantageousness of the QoS tiering regime whenever this is the case.<sup>11</sup> The reason is, as will be seen later, that the QoS tiering regime allocates congestion more efficiently such that $\hat { w } _ { Q } \le \hat { w } _ { N }$ . Our assumption is therefore more conservative and tipped in favor of the network neutrality regime. Formally,

$$
U = \left\{ \begin{array}{l l} b + v \bar {\theta} - \iota w - a & \text { if   connected } \\ 0 & \text { otherwise }, \end{array} \right.\tag{3}
$$

where $\iota > 0$ denotes a consumer’s marginal disutility because of congestion and a the Internet access fee charged by the ISP.

As outlined before, in our analysis we intend to focus on the effect of QoS tiering on the relationship between CPs and the ISP. Thus, for expositional clarity we assume that customers are homogeneous and therefore the ISP is able to set an access fee such that all consumers connect to the ISP in equilibrium. This does not violate the two-sided market property (compare Rochet and Tirole 2006) and is not a crucial limitation of the model per se. First, departing from this assumption would foremost allow for a more fine grained analysis of the rent distribution between customers and the ISP. With homogeneous customers, the ISP is able to fully extract the consumer surplus and thus no dead weight loss occurs.<sup>12</sup> By contrast, with heterogeneous customers, consumer rent will be positive but also possibly generate a dead weight loss. Recall that the consumers’ access fee is the only source of revenue for the ISP under net neutrality. Thus, this fee is likely to be higher under net neutrality than under QoS tiering where the ISP can collect additional rents from CPs through the priority fee. In fact, under QoS tiering the ISP may find it profitable to subsidize the consumer side by lowering the access fee, possibly down to zero, in order to stimulate customer subscriptions that in turn allow the ISP to make higher profits on the CPs’ side. Consequently, the customer access fee and associated dead weight loss is lower under QoS tiering. Indeed, the dead weight loss may even be zero if the access fee is zero. Under net neutrality, the consumers’ access fee (and thus the dead weight loss) can never be zero because otherwise the ISP would not make any profit. Consequently, it is likely that more consumers will subscribe under QoS tiering and that consumers’ welfare is higher than under net neutrality.<sup>13</sup>

Second, despite customers’ homogeneity, demandside effects can be modeled through further assumptions on the distribution function F . For example, if it is assumed that priority providers will receive relatively more demand (clicks) by consumers than will nonprioritized CPs, which in turn leads to a recongestion of the priority lane, then this effect is for the purpose of our analysis qualitatively similar to a situation where a decrease in congestion to the priority class evokes such re-congestion by the overproportional entry of new, congestion sensitive CPs. The latter can be achieved by assuming that $F ^ { \prime }$ is sufficiently increasing in .<sup>14</sup>

Network Congestion. Network congestion is measured through Internet consumers’ average waiting time following a content request. We employ the wellknown $M / M / 1$ queuing model (Kleinrock 1976) to fix ideas on the relationship between average waiting time, network traffic, and capacity.<sup>15</sup> Under a network neutral regime, the M/M/1 model predicts that each consumer has an expected average waiting time of

$$
w _ {N} = \frac {1}{\mu - \Lambda}.\tag{4}
$$

Here  represents the average rate at which service requests are handled, which is interpreted as the overall transmission capacity, whereas $\bar { \Lambda ( \mathbf { \bar { \Lambda } } ) } \overset { - } { = } \lambda \bar { \eta } F ( \bar { \theta } )$ denotes the average rate at which customers’ aggregate content requests arrive at the ISP’s network, which is interpreted as network traffic. For the queuing system to be stable, we must assume that $\mu > \Lambda$

Under a QoS regime, CPs are offered the choice between a priority and a best-effort transmission class. In the $M / M / 1$ model this translates to introducing an additional queue that handles the request of the CPs in the priority class and that is processed ahead of the queue for the best-effort class. However, in each class the queue is cleared on a first-come firstserved basis. In this vein, the classical results of the $M / M / 1$ queuing model represent the average waiting time in the priority class, $w _ { Q 1 } ,$ and the best-effort class, $w _ { Q 2 } \mathrm { : }$

$$
w _ {Q 1} = \frac {1}{\mu - \beta \Lambda}, w _ {Q 2} = \frac {\mu}{\mu - \Lambda} w _ {Q 1}\tag{5}
$$

It is easy to see that relation $w _ { Q 1 } < w _ { N } < w _ { Q 2 }$ is always fulfilled, assuming a fixed transmission capacity $\mu = \mu _ { Q } = \mu _ { N }$ and $\beta < 1 . ^ { 1 6 }$ This is an important feature of our model because it shows formally that serving some CPs with priority will (in the short run) unambiguously lead to a degradation of service quality for the remaining CPs in the best-effort class.<sup>17</sup>

Internet Service Provider. The ISP controls the (twosided) Internet market, over which it has a terminating monopoly, through a number of strategic variables. First, it charges an access fee, $a ,$ from connected consumers. Under a network neutral regime, the consumer access fee is the only source of revenue for the ISP. Second, in the long run the ISP also sets the level of network capacity, $\mu .$ As outlined before, customers and $\mathrm { C P s }$ dislike network congestion. The level of network congestion is captured by customers’ average waiting time for content, w, which is again controlled by the ISP through its choice of network capacity.

Hence, under a network neutrality regime, the ISP’s profit is

$$
\Pi_ {N} = \bar {\eta} a - c (\mu),\tag{6}
$$

where $c ( \mu )$ denotes the costs of capacity expansion.<sup>18</sup> Under a QoS tiering regime, the ISP has an additional strategic variable, $p ,$ the price it charges CPs to transmit data packets with priority. The ISP will choose p in order to maximize its additional revenues from selling priority access. More precisely, under QoS tiering the $\bar { \mathrm { I S P ^ { \prime } s } }$ profit function is

$$
\Pi_ {Q} = \bar {\eta} a + \beta \Lambda p - c (\mu).\tag{7}
$$

We consider the $\mathrm { I S P } ^ { \prime } \mathrm { s }$ previous investment decisions in transmission capacity as sunk in all regimes. Therefore, in the short run $\mu$ can be considered an exogenous variable that is irrelevant for profit maximization.

## 4. Short Run Effects on Content Variety and Welfare

First, we compare the two network regimes in the short run, i.e., when network capacity, , is exogenous and equal in both regimes.

## 4.1. Short Run Equilibrium and Content Variety

Network Neutrality Regime. First, it is obvious that the ISP will set an optimal customer access charge of $a = b + v \bar { \theta } - \iota w _ { N } ,$ , such that all customers will connect to the network $( \bar { \eta } = 1 )$ and total consumer surplus is appropriated by the ISP. Under network neutrality all CPs expect the same congestion level of $w _ { N }$ and enter the network only if they have nonnegative utility at this level. Consequently, the last CP to enter the network is located $\mathsf { a t } ^ { \mathsf { i } \mathsf { s } }$

$$
\bar {\theta} _ {N} = \frac {1}{w _ {N}} = \mu - \lambda F (\bar {\theta}).\tag{8}
$$

Hence, an increase in network traffic per CP, , has an adverse effect on network congestion $( \partial w _ { N } / \partial \lambda > 0 )$ and content variety $( \partial \bar { \theta } _ { N } / \partial \lambda < 0 )$ . This is central to the debate on network neutrality because it exemplifies the network operators’ concerns with respect to the expected increase in traffic.

Quality of Service Tiering Regime. In the QoS tiering regime, the ISP can alleviate congestion for the most congestion sensitive CPs through the provision of differentiated transmission classes. We may now distinguish three types of CPs: (1) CPs whose business model is relatively insensitive to network congestion. They will remain in the free-of-charge best-effort class. (2) CPs whose business model is sufficiently sensitive to network congestion. They will opt for priority access at a price of p. (3) CPs whose business model is extremely sensitive to network congestion. They will remain inactive because entry is not profitable. Remember that the CP indifferent between the first two cases is denoted by ${ \tilde { \theta } } ,$ whereas the CP indifferent between the last two cases is denoted by ${ \bar { \theta } } _ { Q }$ . Obviously, it must hold that $0 \leq \tilde { \theta } \leq \bar { \theta } _ { O } . ^ { 2 0 }$ In a fulfilled expectations equilibrium, the last CP to enter is located at

$$
\bar {\theta} _ {Q} = \frac {1 - p / r}{w _ {Q 1}} = \frac {r - p}{r} (\mu - \lambda (F (\bar {\theta} _ {Q}) - F (\tilde {\theta}))).\tag{9}
$$

From

$$
\begin{array}{l} \frac {\partial \bar {\theta} _ {Q}}{\partial p} = \underbrace {- \frac {1}{r} (\mu - \lambda (F (\bar {\theta} _ {Q}) - F (\tilde {\theta})))} _ {\text { First   Order   Effect }} \\ + \underbrace {\lambda \frac {r - p}{r} \left(\frac {\partial F (\tilde {\theta})}{\partial p} \frac {\partial \tilde {\theta}}{\partial p} - \frac {\partial F (\bar {\theta} _ {Q})}{\partial p} \frac {\partial \bar {\theta}}{\partial p}\right)} _ {\text { Second   Order   Effect }} \end{array}\tag{10}
$$

it is easy to see that an increase in the price for priority transmission, $p ,$ has an unambiguously negative first order effect on content variety. This is the central concern of net neutrality proponents, who argue that starting from a zero price under net neutrality, the introduction of a positive price under QoS tiering has negative first order effects on content variety. However, this argument neglects that there is a second order effect as well: An increase in p will induce more CPs to choose the free best-effort class and therefore alleviate congestion in the priority class. This in turn may encourage new, congestion sensitive CPs to enter, which drives congestion in the priority class up again. The size and direction of the second order effect hinges on the mass of CPs that is located locally at <sup>˜</sup> and <sup>¯</sup> (i.e., $( \partial F ( \tilde { \theta } ) / \partial p ) ( \partial \tilde { \theta } / \partial p ) \ -$ $( \partial F ( \bar { \theta } _ { Q } ) / \partial p ) ( \partial \bar { \theta } / \partial p ) )$ and cannot be determined more specifically for a general distribution function. For the purpose of our analysis, let us therefore assume a particular density function of  that exemplifies the effect of having a nonuniform distribution of . To this end, we consider the density function $f \colon [ 0 , 1 ]  [ 0 , 1 ] .$ $f ( \theta ) : = \alpha + 2 \theta ( 1 - \alpha )$ , with $\alpha \in [ 0 , 2 ] .$ . Let F be the distribution function to f and notice that for $\alpha = 1$ we obtain a uniform distribution with $F ( \theta ) = \theta .$ Otherwise, if $\alpha > 1$ , there exists a relatively larger mass of congestion insensitive CPs $\left( F ( \theta ) > \theta \right)$ and if $\alpha < 1$ there is a relatively larger mass of congestion sensitive CPs $\left( F ( \theta ) < \theta \right)$ . A variation of  is therefore equivalent to a gradual shift of mass from the congestion sensitive portion $( \theta > 0 . 5 )$ to the congestion insensitive portion $( \theta < 0 . 5 )$ of the CPs and vice versa.

In the appendix we show that under a uniform distribution $( \alpha = 1 )$ the first order and second order effect are exactly offset, at any price level, such that the price for priority transmission has no effect on content variety under QoS tiering. Thus, under a uniform distribution, net neutrality and QoS tiering will exactly yield the same level of content variety, i.e., $\bar { \theta } _ { Q } = \bar { \theta } _ { N } \dot { = }$ $\mu / ( \lambda + 1 ) = 1 / w _ { N }$ . However, if the mass of congestion sensitive CPs is relatively large $( \alpha < 1 )$ , an increase in price for priority will not lead to an equally large congestion alleviation for the priority class such that the first order effect prevails. Consequently, under QoS tiering fewer CPs will enter in equilibrium than under net neutrality. Conversely, if the mass of congestion sensitive CPs is comparably small $( \alpha > 1 )$ , then the second order effect dominates and QoS tiering leads to more content variety than net neutrality. The following proposition, whose proof can be found in the appendix, summarizes these results.

Proposition 1 (Content Variety). <sub>If</sub> <sub>content</sub> providers’ congestion sensitivity is uniformly distributed, QoS tiering has no effect on content variety in the short run: The number of active content providers is the same as under network neutrality. In both regimes the number of active content providers is inversely proportional to the average level of congestion in the network. However, if the mass of congestion sensitive content providers is comparably small (large), then QoS tiering is likely to lead to more (less) content variety.

Therefore, it is useful to assume a uniform distribution of  as the reference case for the subsequent analysis, from which it is then easy to draw more general conclusions.

<sup>Assumption</sup> <sup>2.</sup> Content providers’ congestion sensitivity, , is uniformly distributed such that $F ( \theta ) = \theta .$

Under the present assumptions QoS tiering will lead to neither more nor less content variety. However, under a QoS tiering regime the ISP can additionally extract rents from CPs through sales of priority access. In the short run, it will do so by maximizing revenues from priority sales $( \Lambda \beta p )$ , which is achieved by

$$
p = \left(1 - \sqrt {\frac {\bar {\theta} _ {Q}}{\mu}}\right) r = \left(1 - \frac {w _ {Q 1}}{w _ {Q}}\right) r.\tag{11}
$$

Intuitively, this shows that the ISP can extract a fraction of the $\mathrm { C P s ^ { \prime } }$ gross advertisement revenue $r ,$ depending on the congestion alleviation to the priority class compared to the average congestion level in the network.

Proposition 2 (ISP Preferred Regime). <sub>The</sub> <sub>ISP</sub> always prefers the QoS tiering regime because it can make extra profits by selling a priority transmission service to content providers.

The proof is in the appendix.

## 4.2. Short Run Welfare Implications

Now we investigate the short run effect of QoS tiering on welfare. Total welfare, W , is the sum of consumers surplus, CPs’ surplus, and the ISP’s profit. Thus, the difference in social surplus between QoS tiering and network neutrality is given by

$$
\Delta W = (U _ {Q} - U _ {N}) + (\Gamma_ {Q} - \Gamma_ {N}) + (\Pi_ {Q} - \Pi_ {N}).\tag{12}
$$

Recall that $U _ { Q } = U _ { N } = 0$ because consumers’ surplus is always fully appropriated by the ISP. However, notice that changes in consumers’ gross surplus are reflected in changes of the $\mathrm { I S P } ^ { \prime } \mathrm { s }$ profit. Furthermore, $\Pi _ { Q } - \Pi _ { N } > 0$ according to Proposition 2. What remains to be examined is the short run effect of QoS tiering on CPs’ surplus.

To this extent, consider Figure 1 and notice that those CPs located at $\theta \in [ 0 , \tilde { \theta } )$ are evidently worse off under a QoS tiering regime because for them network congestion has increased from $w _ { N }$ to $w _ { Q 2 } .$ . Second, the CPs’ welfare loss increases with congestion sensitivity on the interval $\theta \in [ 0 , \tilde { \theta } )$ . The business model of the provider located at $\theta = 0$ is not affected at all through congestion, whereas the provider at $\theta = \widetilde { \theta }$ is already suffering so much that it is indifferent between staying in the best-effort class and buying priority access.

Figure 1 The Short Run Effect of QoS Tiering on CPs’ Surplus  
![](/api/attachments/6ENPYBRB/fulltext/images/80d47708576473aad9e461346681b57fb3d5625e1e9dd72eb63640500605624c.jpg)

Third, by the converse argument, notice that the welfare loss decreases for the CPs in the priority class as $\theta \in [ \tilde { \theta } , \bar { \theta } )$ increases. To see this, recall from Proposition 1 that the last CP to enter the market, ${ \bar { \theta } } ,$ is identical under both regimes and receives a surplus of zero. For this CP, the benefit through reduced congestion (compared to the network neutrality regime) is just offset by the price that it pays for priority access. Consequently, for all CPs with less congestion sensitivity $( \theta \in [ \tilde { \theta } , \bar { \theta } ) )$ , the price that is paid for priority is higher than the benefit of being in the priority class. Nevertheless, by definition of ${ \tilde { \theta } } ,$ for these providers the welfare loss is still less severe in the first priority class than in the best-effort class. In this line of argumentation, it is also obvious that CP $\tilde { \theta }$ incurs the greatest welfare loss. In summary, we can conclude that in the short run all active CPs are (weakly) worse off under a QoS tiering regime.

However, the price that CPs pay for priority access is merely a welfare shift to the ISP (hatched area in Figure 1). The sign of the overall welfare effect will therefore only depend on the difference between the gross surplus gain through less congestion of those CPs in the priority class and the gross surplus loss through increased congestion of those providers remaining in the best-effort class. In the appendix we show that this difference is always positive.

Proposition 3 (Short Run Welfare). <sub>If</sub> <sub>content</sub> providers’ congestion sensitivity is uniformly distributed, QoS tiering unambiguously increases welfare with respect to the network neutrality regime in the short run because congestion is alleviated for the most congestion sensitive content providers in lieu of the less congestion sensitive content providers. However, all content providers are worse off under a QoS tiering regime because the increased surplus is expropriated by the ISP.

Furthermore, it is easy to see that this welfare conclusion is not as clear-cut under a nonuniform distribution. If QoS tiering leads to more content variety, then those CPs who are newly active in the market will enjoy a higher surplus than under network neutrality and Proposition 3 is even strengthened. However, if there is a relatively large mass of congestion sensitive CPs in the economy such that QoS tiering leads to less content variety, the associated welfare loss must be counterweighted with the welfare gain from better congestion allocation. In this case it is likely that Proposition 3 does not hold anymore.

## 5. Long Run Effects on Broadband Investments, Innovation, and Welfare

Much of the neutrality debate is rooted in the ISPs’ concerns about infrastructure investments. On the one hand, ISPs would like to accommodate new (congestion sensitive) content because this is valued by customers. However, on the other hand ISPs disapprove of CPs who free-ride on their infrastructure investments. QoS tiering seems to be a plausible way out of this dilemma, but it is unclear whether in the long run this regime will lead to greater or fewer incentives for infrastructure investments than will network neutrality regulation. Thus, in this section we extend our analysis to long run investments in network transmission capacity. In our model, transmission capacity is represented by the average service rate, $\mu ,$ at which customer requests can be handled. An increase of $\mu$ allows the ISP to handle more service requests to CPs at a time.

## 5.1. Investment Incentives

Formally, the ISP’s investment decision is a discrete decision stage that precedes the previous analysis. The ISP chooses the network capacity level, $\mu ,$ first, and subsequently sets the customer access charge, $a ,$ and the priority price, $p ,$ if applicable. In the subgame perfect equilibrium, the ISP will set the optimal capacity level at the point where the marginal revenues of capacity expansion, $M R \equiv \partial \Pi / \partial \mu$ , equal marginal costs, $M \bar { C } \equiv \bar { \partial c } ( \mu ) / \partial \mu$ . Consequently, the $\mathrm { I S P } ^ { \prime } \mathrm { s }$ optimal capacity level will be higher if marginal revenues from capacity expansion are higher.<sup>21</sup> In both network regimes the following two marginal effects of capacity expansion on ISP revenue can be distinguished:

• The variety incentive $( v \cdot \partial F ( \bar { \theta } ) / \partial \mu )$ denotes the ISP’s marginal revenue effect on the customer access fee that comes from the entry of new, congestion sensitive CPs.

• The congestion incentive $\left( - \pmb { \iota } \cdot \partial \boldsymbol { w } / \partial \mu \right)$ denotes the $\mathrm { I S P } ^ { \prime } \mathrm { s }$ marginal revenue effect on the customer access fee that comes from a change of the overall congestion level.

Furthermore, notice that under the assumption of a uniform distribution of $\mathrm { C P s ^ { \prime } }$ congestion sensitivity, these investment incentives are always positive and identical under both network regimes. Hence, potential differences in investments between the two regimes may only be a result of an additional investment incentive that an ISP has only under QoS tiering:

• The priority revenue incentive $\left( \partial ( \beta \Lambda p ) / \partial \mu \right)$ denotes the ISP’s marginal revenue effect from selling priority access.

Consequently, the sign of the priority revenue incentive is definitive for the comparison between investment incentives under QoS tiering and network neutrality. The result is summarized by the following proposition, whose proof can be found in the appendix.

Proposition 4 (Investment Incentives). <sub>If</sub> <sub>the</sub> <sub>con-</sub> gestion sensitivity of content providers is uniformly distributed, the $I S P ^ { \prime } s$ optimal capacity level is higher under QoS tiering.

This finding contradicts the results of Cheng et al. (2011) and Choi and Kim (2010). The reason is that we explicitly account for more network capacity encouraging, the entry of new CPs, whose additional demand keeps the value of the priority service high. By contrast, in Cheng et al. (2011) and Choi and Kim (2010), entry of new CPs is not possible and therefore it is more profitable to exploit the current CP base and to keep network capacity scarce.

Note that for nonuniform distribution functions, the mass of active CPs may differ between the two network regimes and thus the variety and congestion incentive will generally not coincide. In particular, if the mass of congestion sensitive CPs is very small, then the priority incentive can even be negative. This is because the ISP has only few congestion sensitive CPs to which it can sell priority and hence it seeks to make the priority class attractive to less congestion sensitive CPs by keeping network capacity scarce and the congestion level high. To see this, consider Figure 2, which presents a numerical example of the marginal investment incentives for varying distributions of CPs’ congestion sensitivity. In line with Proposition 4, the variety and congestion incentive under either regime coincide under the uniform distribution of CPs’ congestion sensitivity $( \alpha = 1 )$ such that the positive priority revenue incentive is decisive for the higher investment incentives under QoS tiering. However, the more congestion sensitive CPs are in the Internet economy $( \alpha < 1 , \alpha \to 0 )$ , the stronger is the variety incentive under net neutrality compared to QoS tiering. Notwithstanding, the priority revenue incentive, which is only present under QoS tiering, also increases. As the variety incentive grows linearly in v and the priority revenue incentive grows linearly in $r ,$ net neutrality may only lead to more infrastructure investments for $\alpha < 1$ if v is sufficiently larger than $r .$ On the other hand, when there are relatively fewer congestion sensitive CPs in the economy $( \alpha > 1 )$ , the variety and congestion incentive are slightly larger under QoS tiering while the priority incentive remains positive. In this case, QoS tiering provides unambiguously higher incentives for infrastructure investments. However, when the mass of congestion sensitive CPs becomes very small $( \alpha \gg 1 )$ the priority revenue incentive can indeed become negative, and eventually also the variety incentive under QoS tiering drops below the level under net neutrality. In this case, it is likely that net neutrality promotes investments in network infrastructure more. In summary, we can conjecture that Proposition 4 holds locally around $\alpha = 1$ (Assumption $^ { 2 ) , }$ $\mathrm { i . e . , }$ if the proportion of congestion sensitive CPs to congestion insensitive CPs is balanced.

Figure 2 ISP’s Marginal Investment Incentives Under QoS Tiering (Gray) and Net Neutrality (Black) for Different Distributions of CPs’ Congestion Sensitivity 4Á5  
![](/api/attachments/6ENPYBRB/fulltext/images/46f267f38c1f51da66a5b57a4b9556bc51a331df520bc5e72ec71d48abdd8912.jpg)  
Note. The figure is derived for $\mu = 7 / 4 , \lambda = 1 , r = 1 , v = 1$ , but qualitatively identical results are obtained for other parameter values.

5.2. Innovation at the Edge and Long Run Welfare The $\mathrm { I S P ^ { \prime } s }$ investments in network infrastructure have direct ramifications for welfare. At higher capacity levels customers enjoy lower network congestion (congestion incentive) and higher network benefits (variety incentive). Figure 3 illustrates the effect of capacity expansion for CPs under QoS tiering. The reduction of network congestion increases CPs’ click-through rate and thus the slope of their surplus curve in both transmission classes. The CPs in the best-effort class and also some CPs in the first priority class may still be worse off than under network neutrality. However, as a consequence of the overall decreased congestion level, both marginal CPs, <sup>˜</sup> and ${ \bar { \theta } } ,$ are shifted to the right. This means that new, highly congestion sensitive CPs are able to enter the network. This has been referred to as “innovation at the edge” in the present context (Jamison and Hauge 2008). Obviously the surplus of the new CPs (crosswise hatched area) and also the surplus of some of the previously most congestion sensitive CPs (vertically hatched area) are thus increased compared to a network neutrality regime.

Figure 3 The Long Run Effect of QoS Tiering on Innovation and Welfare  
![](/api/attachments/6ENPYBRB/fulltext/images/8c5c45f2cd5675361cf4b5f89e3885292f7c8052bd995e01b449d25fd8ae8298.jpg)

Accordingly, higher capacity levels will ceteris paribus lead to higher gross utility for consumers and CPs and are thus beneficial for welfare. This is also shown formally in the appendix.

Proposition 5 (Long Run Welfare). <sub>The</sub> <sub>regime</sub> that provides more incentives for infrastructure investments is more efficient in the long run. If the congestion sensitivity of content providers is uniformly distributed, QoS tiering is more efficient and provides more content variety than net neutrality.

QoS tiering is consequently the more efficient regime in the long run and, by Proposition 3, also in the short run if CPs’ congestion sensitivity is uniformly distributed. However, the fact remains that a nonnegligible share of this surplus is immediately expropriated by the ISP.

## 6. Minimum Quality Standards

Price controls are not a suitable policy instrument in this context because in the short run social and private incentives are in line: To see this, note that the social planner seeks to set the regulated priority price such that the socially optimal share of CPs selects the priority transmission class. In this vein CPs’ gross surplus is maximized. The ISP, however, pursues the same goal, because it can subsequently extract a fraction of the CPs’ surplus.

With regard to the $\mathrm { I S P } ^ { \prime } \mathrm { s }$ investments in infrastructure, there generally is reason for regulation, however: Opponents of net neutrality regulation have often objected that net neutrality forces ISPs to invest above the efficient level, which is known as overprovisioning. On the contrary, opponents of QoS tiering argue that QoS tiering induces ISPs to keep transmission capacity scarce, and thus broadband investments are likely to be below the efficient level (underprovisioning). In the appendix we show that the difference between the efficient and private level of infrastructure investments is in fact independent of the network regime.

Proposition 6 (Efficient Investments). <sub>The</sub> <sub>social</sub> planner has a higher incentive to invest in network capacity than does the ISP. This result holds for both network regimes, QoS tiering and network neutrality.

Minimum Quality Standards. It has therefore been argued that a minimum quality standard (MQS) could be an appropriate policy instrument in this context (Brennan 2010); an MQS policy is also already feasible under the new European legislative framework. After all, MQSs have found to be generally welfareenhancing in competitive settings (Ronnen 1991). For example, it has been argued that the MQS could be set such that the ISP is required to offer CPs under QoS tiering a congestion level in the best-effort class that is as least as low as the equilibrium best-effort congestion level under network neutrality. Consequently, under the QoS tiering regime no CP would be set at a disadvantage anymore. Moreover, in order to meet this MQS, the ISP is required to increase the network’s capacity, potentially to the extent that the gap between the level of private and efficient investments is closed. More precisely, by requiring the MQS $w _ { N } ( \mu _ { N } ^ { * } ) \equiv w _ { Q 2 } ( \mu _ { \mathrm { M Q S } } )$ the regulator implicitly defines the new capacity level $\mu _ { \mathrm { M Q S } } > \mu _ { N } ^ { * } . ^ { 2 }$ 2

By Propositions 4 and 6 the order of relevant capacity levels is $\mu _ { Q } ^ { * * } > \mu _ { Q } ^ { * } > \mu _ { N } ^ { * }$ . Remember that $\mu _ { \mathrm { M Q S } } > \mu _ { N } ^ { * } ,$ and thus we can differentiate between three different cases. First, if $\mu _ { Q } ^ { * } \geq \mu _ { \mathrm { M Q S } }$ the MQS is not a binding condition for the $\mathrm { I S P ^ { \prime } s }$ capacity choice and hence is simply ineffective. Second, if $\mu _ { Q } ^ { * * } \geq \mu _ { \mathrm { M Q S } } > \mu _ { Q } ^ { * }$ the MQS is effective in raising the ISP’s network capacity level, potentially up to the efficient level. Third, if $\mu _ { \mathrm { M Q S } } > \mu _ { Q } ^ { * * }$ the MQS policy may lead to an excessive investment in network infrastructure. In summary,

MQSs are only effective in one out of three cases, and thus for now their use is questionable.<sup>23</sup>

Proposition 7 (Minimum Quality Standard Reg-<sup>ulation).</sup> An MQS policy, which requires the ISP to guarantee a best-effort congestion level under QoS tiering that is equal to the equilibrium congestion level under network neutrality, may increase welfare but may also lead to excessive investments or be ineffective.

## 7. Strategic Quality Degradation

In the preceding analysis we have neglected the possibility that the monopolistic ISP may also engage in non-price discrimination, for example by degrading the quality of the best-effort class under QoS tiering. The concern for strategic quality degradation under a QoS tiering regime has been expressed by network neutrality proponents, but also previous empirical and theoretical research has identified several circumstances under which such practice is indeed profitable (Economides 1998, Foros et al. 2002, Crawford and Shum 2007). Absent the possibility to degrade the quality of the best-effort class, the ISP’s only control over the share of CPs that buys priority transmission in equilibrium () is through the price p. Quality degradation, however, provides the ISP with an additional means through which it can manipulate the relative attractiveness of the priority class over the best-effort class and thus the mass of CPs that buy priority transmission in equilibrium. It is inevitable that such practice will destroy some CPs’ surplus and therefore questions the previously positive welfare results of QoS tiering. However, ex ante it is not clear whether there exist scenarios under which quality degradation may actually be profitable to the ISP in the first place.

To this end, consider the extreme scenario where the ISP degrades the best-effort class under a QoS tiering regime maximally $( w _ { Q 2 } \to \infty )$ such that in equilibrium no CP wants to remain in the best-effort class $( \tilde { \theta }  0 , \beta  1 )$ . Furthermore, let $r ( { \bar { \theta } } ) = r$ be constant in this example.<sup>24</sup> We will show that there exist circumstances under which even this extreme form of quality degradation is profitable. More precisely, by rendering the best-effort class useless, the ISP effectively forces all CPs into the priority transmission class. It is easy to see that this is equivalent to a scenario in which the ISP demands a termination fee from each CP for transmitting content to its connected consumers.<sup>25</sup> At a fixed transmission capacity, this has detrimental effects on content variety and welfare.

To see this, recall that without quality degradation, the last CP to enter the network was located at $\bar { \theta } _ { N , Q } =$ 1/w, independent of the network regime and independent of the price for priority transmission. In contrast, the last CP to enter under quality degradation is located at $\bar { \theta } _ { D } = ( 1 - p _ { D } / r ) w . ^ { 2 6 }$ Because all CPs are forced into the priority transmission class, congestion is the same for all CPs and at a similar level under network neutrality. Thus, maximum quality degradation not only destroys the source of the positive welfare effects of the QoS tiering regime but also forces the most congestion sensitive CPs out of the network: CPs experience a similar congestion level as under network neutrality but have to pay a price $p > 0$ as if they were under QoS tiering. To be precise, it must be mentioned that the smaller mass of active CPs will also slightly reduce the average congestion level compared to network neutrality or QoS tiering. However, this type of congestion alleviation cannot outweigh the detrimental effect to content variety and welfare. Proofs are relegated to the appendix.

Proposition 8 (Content Variety and Welfare Under Quality Degradation). <sub>When</sub> <sub>the</sub> <sub>ISP</sub> <sub>degrades</sub> the quality of the best-effort class under QoS tiering such that all CPs choose to buy priority transmission, then compared to network neutrality, fewer content providers enter the network in equilibrium and overall welfare is lower.

Consequently, quality degradation is undesirable from a policy perspective and tarnishes the short run welfare results of QoS tiering. The question remains, however, whether quality degradation is in fact a profitable option to the ISP under QoS tiering and thus constitutes an actual source of concern to policy makers. The effect of quality degradation on the ISP’s revenue depends on the trade-off of two opposing effects. By Proposition 8 quality degradation results in less content variety and consequently the ISP can charge consumers less for access. On the other hand, quality degradation forces all CPs to pay for their traffic and thus revenues from priority sales are potentially larger than before. Obviously, this trade-off is driven by the relative size of the marginal valuations of consumers and $\mathrm { C P s , }$ respectively. This can be exemplified by the equilibrium price formula:

$$
p _ {D} = \frac {r (1 + \lambda) - \sqrt {r (v + r (1 + \lambda))}}{\lambda}.\tag{13}
$$

Prices are positive as long as $v < r \lambda ( 1 + \lambda )$ , i.e., as long as the consumers’ marginal utility for variety is not too large with respect to the CPs’ marginal valuation for gross traffic (generated by consumers). On the contrary, if $v > r \lambda ( 1 + \lambda )$ , the ISP would theoretically like to subsidize the CPs and thus promote their entry in order to extract consumers’ high utility from variety.

Proposition 9 (Profitability of Quality Degradation). <sub>For</sub> <sub>all</sub> $v < \underline { { v } } ,$ , where $\underline { { v } } < r \lambda ( 1 + \lambda ) , \forall \lambda > 0 ,$ , the ISP makes larger profits under a QoS tiering regime in which the transmission quality of the best-effort class is degraded, such that all content providers choose to buy priority transmission in comparison to a QoS tiering regime without quality degradation.

Proposition 9 establishes first that the ISP never subsidizes CPs by imposing negative prices under maximum quality degradation but rather prefers to refrain from quality degradation and revert to the unhampered QoS tiering regime instead. This also implies that the ISP will not privately establish a network neutrality regime, which could be the result of QoS tiering with maximum quality degradation and a price of zero. Secondly, and more importantly, the proposition highlights that strategic quality degradation is in fact a profitable strategy for the ISP as long as consumers’ marginal valuation for variety is sufficiently small.<sup>27</sup>

Given the detrimental welfare consequences of quality degradation under a QoS tiering regime, policy makers should be aware of this strategic option. In particular, if policy makers suspect the ISP engages in quality degradation, some of the previously reviewed policy instruments may now regain attention. Price regulation (i.e., $p _ { D } = 0 )$ can at least ensure the current status quo of the network neutrality regime. However, such regulation also excludes the potentially positive welfare effects of an unhampered QoS tiering regime. In this context, minimum quality standards and transparency obligations seem to provide a more appropriate policy tool. If applied effectively, such obligations can preclude the ISP’s negative strategic incentives under QoS tiering while maintaining the generally positive welfare effects of this regime; after all, the ISP is still left better off than under network neutrality.

## 8. Conclusions and Policy Implications

Network neutrality has become a prime topic for many regulatory authorities, but the effect of such regulation is still unclear. Scholarly papers often find contradictory results with respect to the consequences of network neutrality on content variety, broadband investments, and welfare. We contribute to the debate on network neutrality by providing a formal framework that incorporates the relevant arguments of net neutrality proponents and opponents in a twosided market framework with Internet customers, CPs, and an ISP. Our analysis focuses on the relationship between CPs and a monopolistic ISP and compares network neutrality to a QoS tiering regime in which CPs may pay for the prioritized transmission of their data packets on a nondiscriminatory basis. We explicitly consider the negative externality that prioritization has on the remaining best-effort class but acknowledge that CPs’ services differ in their sensitivity toward network congestion, and CPs may offer their services only if they are sustainable under the given congestion level.

We find that the comparison between the two network regimes depends on the distribution of CPs’ congestion sensitivity in the Internet economy. In particular, we have thoroughly investigated the neutral reference case where CPs’ congestion sensitivity is uniformly distributed and find that QoS tiering increases welfare in the short run because the installed level of network capacity is used more efficiently: Network congestion is reallocated, such that it is alleviated for the most congestion sensitive CPs. This offsets the congestion aggravation for the CPs in the remaining best-effort class. However, QoS tiering does not immediately promote the entry of new content provides with innovative services that are even more congestion sensitive. In fact, in the short run, all CPs likely to be worse off under a QoS tiering regime because the ISP is able to expropriate some of the CPs’ surplus through priority pricing. Consequently, the ISP always prefers the QoS tiering regime. It is subject to the authority of policy makers to evaluate the shift of surplus from CPs to ISPs, which is welfare neutral per se but lies at the heart of the net neutrality debate. On the other hand, ISPs argue that they will use the additional revenues to invest more in broadband infrastructure. We show that this is true for the reference case of uniformly distributed congestion sensitivities but may not hold for more skewed distribution functions. In sum, QoS tiering is likely to be the more efficient regime if the proportion of congestion sensitive to congestion insensitive CPs is balanced. In this case, the ISP invests more in broadband infrastructure and thereby allows for entry of new, congestion sensitive CPs in the short run. Therefore, particularly the very congestion sensitive CPs will be better off under QoS tiering, and hence it is not surprising that Google and Verizon have privately agreed on a tiered system (Wyatt 2010).<sup>28</sup>

Furthermore, our analysis reveals that the level of private investments is generally not efficient. We show that an MQS policy requiring the ISP to guarantee a congestion level in the best-effort class under QoS tiering that is at least as good as the besteffort congestion level under network neutrality is not sufficient to guarantee efficient infrastructure investments. However, if the ISP has an incentive to strategically degrade the quality of the best-effort class, an MQS may be an appropriate policy instrument to mitigate the detrimental effects that this practice can have on content variety and welfare. Strategic quality degradation can also possibly be counteracted by Internet transparency obligations. Such obligations are already explicitly incorporated in the new U.S. and European regulatory framework (FCC 2010; European Commission 2009, art. 21).

In conclusion, although our results show that some of the objections to QoS tiering are justified, we also find a strong case for a tiered network. The potential dangers of a QoS tiering regime, such as strategic quality degradation, can be overcome by transparency obligations or minimum quality standards. Furthermore, because strategic quality degradation reduces content variety, it is even less profitable when ISPs are in competition for customers. To the contrary, under competition ISPs will try to attract customers by offering them more content variety and a lower average congestion level than does their competitor. This will boost their investment incentives. Likewise, the ISPs will also lower the customers’ access charge and therefore some of the ISPs’ rent is shifted toward the consumers. However, competition between ISPs does not change the main insights of our analysis under monopoly if we make the reasonable assumption that CPs multihome (i.e., are connected with besteffort to every ISP) whereas consumers singlehome (i.e., are connected to one ISP exclusively). In this case, every CP would again face a terminating monopoly over the connected consumers at each ISP, leaving the previously described relationship between the ISP and the CPs intact. Consequently, our result that QoS tiering is the ISPs’ preferred regime and that it will lead to more investment and content variety because of the additional priority revenue incentive remains unchanged. Hence, there is no reason to believe that competition between ISPs will warrant network neutrality. In reverse, the prohibition of QoS tiering (pay for priority), which has been proposed by the FCC for fixed line networks, can eventually be harmful to content variety, broadband investment, and welfare.

## Acknowledgments

The authors would like to thank Ingo Vogelsang, Michal Grajek, Marc Bourreau and two anonymous referees as well as the editors for helpful comments. Financial aid by the German Research Foundation (DFG) and the NET Institute is gratefully acknowledged.

## Appendix A. Alternative Model Variants

## A.1. Model with Heterogeneous Internet Customers

Internet customers are now considered to be heterogeneous with respect to their willingness to pay for Internet connectivity. To this end, customers’ utility (3) is modified as follows

$$
U = \left\{ \begin{array}{l l} b - t \eta + v \bar {\theta} - \iota w - a & \text { if   connected } \\ 0 & \text { otherwise }, \end{array} \right.\tag{A1}
$$

where t is the degree of heterogeneity and  is assumed to be uniformly distributed on the unit interval. The results for this model cannot be presented in closed form solutions. Therefore we provide numerical results in Figure A.1. Therein the outcomes under net neutrality (black) and QoS tiering (gray) are compared for a range of values of r (the CP’s marginal valuation for customers) and v (the customers marginal valuation for CPs), the parameters that are relevant for the cross-side network effects in our two-sided market model. Compared to net neutrality, we find that QoS tiering indeed results in lower access fees to consumers, and thus more consumer subscriptions, as well as higher consumer welfare. At the same time, under QoS tiering less CPs are active in the network, and CPs’ surplus is likely to be lower. Interestingly, if r is much larger than v, CPs’ surplus may even be higher under QoS tiering. This is because CPs are charged relatively less for priority and customers relatively more for access in this case. Finally, it is evident that the ISP still prefers QoS tiering over net neutrality and that total short run welfare remains higher under QoS tiering.

## A.2. Model with Re-Congestion Effect

The re-congestion effect describes that CPs in the priority class receive more traffic (clicks) than CPs in the best-effort class. We model this through the following modification of (2).

$$
\Gamma_ {Q} (\theta) = \left\{ \begin{array}{l l} (1 - \theta w _ {Q 2}) \lambda_ {B E} \bar {\eta} r \\ \qquad \text { if   active   in   best - effort   class } \\ (1 - \theta w _ {Q 1}) \lambda_ {\mathrm{QOS}} \bar {\eta} r - \lambda_ {\mathrm{QOS}} \bar {\eta} p \\ \qquad \text { if   active   in   priority   class } \\ 0 \quad \text { otherwise }, \end{array} \right.\tag{A2}
$$

where $\lambda _ { B E }$ and $\lambda _ { \mathrm { Q O S } }$ denote the clicks received by each CP in the best-effort and priority class, respectively. By definition of the re-congestion effect $\lambda _ { B E } < \lambda _ { \mathrm { Q O S } }$ . The ISP’s profit

## Figure A.1 Comparison Between QoS Tiering (Gray) and Net Neutrality (Black) with Heterogeneous Customers

(a) Customer access fee  
![](/api/attachments/6ENPYBRB/fulltext/images/54b9250a2ceaa39f4bfb45d2c70c8e3d760308af107df147ea8451b7b0054a9f.jpg)  
(d) Active CPs

(b) Customer subscriptions  
![](/api/attachments/6ENPYBRB/fulltext/images/b9c441846906b05034e2fbe00ccebd2dc96797204ba064d50dfb88677e1fbd0b.jpg)

![](/api/attachments/6ENPYBRB/fulltext/images/d19efe910dbf2f9961254c43ee0daee44399022895ec86c3556f76d1f9112e12.jpg)

(e) CPs’ surplus  
(c) Customers’ surplus  
![](/api/attachments/6ENPYBRB/fulltext/images/3e3f609911681eb8e300647c1c586241e74698ae37a19b2822f65d6efddd76a3.jpg)

![](/api/attachments/6ENPYBRB/fulltext/images/373c01a6a78375cf7db0440f99b66413082ada9a75de12833c648eb51ad74585.jpg)

(f) Priority price  
![](/api/attachments/6ENPYBRB/fulltext/images/2ded49e833005df39b54646edde631c9d85130825d04c8a65951a2a0af1ce556.jpg)  
(h) Short run welfare

(g) ISP’s surplus  
![](/api/attachments/6ENPYBRB/fulltext/images/fd87422900a6c7ca959f71b1397d9a56b4bada75bd24def8e1f5f4b1f5f188b1.jpg)

![](/api/attachments/6ENPYBRB/fulltext/images/c01227efe9c44d09103894e0542296bd2b62d7bd0cd3a6e65b76d36dd2f325b0.jpg)  
Note. The figures are derived for $\mu = 1 , \lambda = 1 , t = 1 0 , b = 1$ , but qualitatively identical results are obtained for other parameter values.

under QoS tiering is adapted accordingly. In the following we intend to show that this model yields qualitatively the same results as the standard model with a relatively large mass of congestion sensitive CPs $( \alpha < 1 )$ . To this end, we conduct a numerical analysis in which we compare the results of both models side by side (Figure A.2). The figure shows that the two models yield qualitatively the same results with respect to the comparison of QoS tiering and net neutrality. Thus, it can be concluded that an increase in the re-congestion effect (i.e., an increase of $\lambda _ { \mathrm { Q O S } } )$ acts very similarly to an increase in the mass of congestion sensitive CPs (i.e., a decrease of ) within the scope of our analysis.

## A.3. Model with Competitive Clicks

We now assume each customer spends an exogenous amount of clicks on the Internet, say å, that he evenly distributes among the available CPs. That is, $\lambda = \Lambda / F ( \bar { \theta } )$ and consequently,  decreases as the number of active CPs increases. Notice that this model is in line with Assumption 1 because each active CP receives the same number of clicks from each customer. In conjunction with Assumption 2 this model variant yields the following results:

$$
F (\bar {\theta} _ {N}) = \bar {\theta} _ {N} = \mu - \Lambda\tag{A3}
$$

$$
F (\bar {\theta} _ {Q}) = \bar {\theta} _ {Q} = \mu - \Lambda\tag{A4}
$$

$$
F (\tilde {\theta}) = \tilde {\theta} = \frac {p}{r - p} \frac {\mu - \Lambda}{\Lambda} \bar {\theta} _ {Q},\tag{A5}
$$

Obviously, it holds that $\bar { \theta } _ { N } = \bar { \theta } _ { Q } = 1 / w _ { N } ,$ , which is exactly the result that is denoted by Proposition 1. Furthermore, the optimal priority price, which maximizes $\Lambda \beta p ,$ , is given by

$$
p = \frac {\mu - \sqrt {\mu (\mu - 1)}}{\mu} r = \left(1 - \sqrt {\frac {\bar {\theta} _ {Q}}{\mu}}\right) r = \left(1 - \frac {w _ {Q 1}}{\hat {w} _ {Q}}\right) r,\tag{A6}
$$

which is exactly the price structure that is described by (11). Consequently this model variant must yield the same qualitative results.

## A.4. Model with Congestion Sensitive Consumers

Consider the Internet customers’ utility function from (3), but now assume that consumers are congestion sensitive and, instead of the average congestion level, evaluate congestion by $\begin{array} { r } { \hat { w } _ { N } = \int _ { \theta = 0 } ^ { \theta } w _ { N } \theta f ( \theta ) d \theta } \end{array}$ and $\hat { w } _ { Q } =$ $\begin{array} { r } { \int _ { \theta = 0 } ^ { \tilde { \theta } } w _ { Q 2 } \theta f ( \theta ) d \theta + \int _ { \theta = \tilde { \theta } } ^ { \tilde { \theta } } w _ { Q 1 } \theta f ( \theta ) d \theta , } \end{array}$ , respectively. It follows that $\hat { w } _ { N } \ge \hat { w _ { Q } }$ for $\bar { \theta } _ { Q } = \bar { \theta } _ { N } = \bar { \theta }$ and $\mu _ { N } = \mu _ { Q } = \mu \colon$

$$
\hat {w} _ {N} \geq \hat {w} _ {Q} \Leftrightarrow \frac {w _ {N} - w _ {Q 1}}{w _ {Q 2} - w _ {N}} \geq \frac {\int_ {\theta = 0} ^ {\tilde {\theta}} \theta f (\theta) d \theta}{\int_ {\theta = \tilde {\theta}} ^ {\bar {\theta}} \theta f (\theta) d \theta}
$$

Figure A.2 Comparison of the Re-Congestion Effect and the Effect of a Skewed Distribution of CPs’ Congestion Sensitivity 4 < 15 with Respect to the Outcome of the Comparison Between QoS Tiering (Gray) and Net Neutrality (Black)  
(a) Active CPs (re-congestion)  
![](/api/attachments/6ENPYBRB/fulltext/images/4d409b157eadaaeb0c74b3920d51ccfb4a51246b698d0ac65e52a38fd4299da4.jpg)  
(d) ISP’s surplus (re-congestion)

(b) Priority price (re-congestion)  
![](/api/attachments/6ENPYBRB/fulltext/images/8d9d3980de9fe9f26a003eddc1d551d858744762e22ffc5957832fa307c08df3.jpg)  
(e) Short run welfare (re-congestion)

(c) CPs’ surplus (re-congestion)  
![](/api/attachments/6ENPYBRB/fulltext/images/ddd84a744c529516e366f511310b621c9153021624d730e2e54f187340279ca3.jpg)

![](/api/attachments/6ENPYBRB/fulltext/images/dd082fba06623b0a0c6a211bc90d9ffd2401c11cac2924b3a4b15232d074326e.jpg)

(f) Active CPs (skewed dist.)  
![](/api/attachments/6ENPYBRB/fulltext/images/e9c478ef074f447dcd94e9f61011e38ef960378d3e308965c5b16ccc16f4c723.jpg)

![](/api/attachments/6ENPYBRB/fulltext/images/ea1fc609b48ece15d0deaee0c1c707949bbd62290a5739e9e80cc9e273bf83b4.jpg)

(g) Priority price (skewed dist.)  
![](/api/attachments/6ENPYBRB/fulltext/images/65c50d37b11c6f2aec00cc9c22403d48e02ae80dcbe07cf2851814f642e41260.jpg)

(h) CPs’ surplus (skewed dist.)  
![](/api/attachments/6ENPYBRB/fulltext/images/360ef4859dd9d03eed529f0fa0a7a0b50e35a1c9c36da33fdb1bffb9620cb6d1.jpg)

(i) ISP’s surplus (skewed dist.)  
![](/api/attachments/6ENPYBRB/fulltext/images/0bdb2fe6133d3ca7b00ce5aa6f399c38b22216bc7b0969c0947f9cc74dde1b30.jpg)

(j) Short run welfare (skewed dist.)  
![](/api/attachments/6ENPYBRB/fulltext/images/a4a4fb0ec0b0b7e1b73069cadcbb7d96b6c6b6cf939ac7739c592bcedab1b439.jpg)  
Note. The figures are derived for $\mu = 7 / 4 , \lambda = 1 , b = 1 0 , r = 1 0 ,$ but qualitatively identical results are obtained for other parameter values.

Substituting $w _ { N } = \beta w _ { Q 1 } + ( 1 - \beta ) w _ { Q 2 }$ and $\beta = 1 - F ( \tilde { \theta } ) / F ( \bar { \theta } )$ and integrating the right-hand side yields:

$$
\begin{array}{c} \frac {F (\tilde {\theta})}{F (\bar {\theta}) - F (\tilde {\theta})} \geq \frac {\tilde {\theta} F (\tilde {\theta}) - \int_ {\theta = 0} ^ {\bar {\theta}} F (\theta)   d \theta}{\bar {\theta} F (\bar {\theta}) - \tilde {\theta} F (\tilde {\theta}) - \int_ {\theta = \bar {\theta}} ^ {\bar {\theta}} F (\theta)   d \theta} \\ \Leftrightarrow F (\bar {\theta}) (\bar {\theta} - \tilde {\theta}) + \frac {F (\bar {\theta}) - F (\tilde {\theta})}{F (\tilde {\theta})} \int_ {\theta = 0} ^ {\bar {\theta}} F (\theta)   d \theta \geq \int_ {\theta = \tilde {\theta}} ^ {\bar {\theta}} F (\theta)   d \theta \end{array}
$$

From $\begin{array} { r } { F ( \bar { \theta } ) ( \bar { \theta } - \tilde { \theta } ) \geq \int _ { \theta = \tilde { \theta } } ^ { \bar { \theta } } F ( \theta ) d \theta } \end{array}$ and from $\bar { \theta } \geq \tilde { \theta }$ as well as the monotonicity of the distribution function $F ,$ it follows that the inequality is always satisfied.

Consequently, if consumers are congestion sensitive, QoS tiering will warrant consumers a higher gross utility than net neutrality. Therefore, the specification with congestion sensitive consumers introduces an additional short run welfare gain in favor of the QoS tiering regime that is not present in the base model.

## Appendix B: Proofs

B.1. Relation Between Indifferent Content Providers Recall ${ \bar { \theta } } _ { Q }$ from (9) and notice that

$$
\tilde {\theta} = \frac {p (\mu - \lambda (F (\bar {\theta} _ {Q}))}{r \lambda F (\bar {\theta} _ {Q})} (\mu - \lambda (F (\bar {\theta} _ {Q}) - F (\tilde {\theta}))).\tag{B1}
$$

It follows that

$$
\tilde {\theta} \leq \bar {\theta} _ {Q} \Leftrightarrow p \leq r \frac {\lambda F (\bar {\theta} _ {Q})}{\mu}.\tag{B2}
$$

Under Assumption $^ { 2 , }$ where p is determined by (B6) and $F ( { \bar { \theta } } _ { Q } )$ by (B4), this condition becomes $\sqrt { \lambda + 1 } \leq \dot { \lambda } + \dot { 1 }$ , which is always true.

## B.2. Proposition 1

It is easy to verify that for $\alpha = 1$

$$
F (\bar {\theta} _ {N}) = \bar {\theta} _ {N} = \frac {\mu}{\lambda + 1}\tag{B3}
$$

$$
F (\bar {\theta} _ {Q}) = \bar {\theta} _ {Q} = \frac {\mu}{\lambda + 1}\tag{B4}
$$

$$
F (\tilde {\theta}) = \tilde {\theta} = \frac {p}{\lambda (r - p)} \bar {\theta} _ {Q},\tag{B5}
$$

which proves the first part of the proposition. Furthermore, from (11) it follows that

$$
p = \left(1 - \sqrt {\frac {1}{\lambda + 1}}\right) r = \left(1 - \sqrt {\frac {\bar {\theta} _ {Q}}{\mu}}\right) r.\tag{B6}
$$

For $\alpha \neq 1 , \bar { \theta } _ { Q }$ will generally depend on p. First see that p cannot exceed $p _ { \mathrm { m a x } } ,$ , which solves $\Gamma _ { Q } ( \bar { \theta } _ { Q } ) = \Gamma _ { Q } ( \tilde { \theta } )$ . This price is

$$
p _ {\max} = r \left(1 + \frac {\lambda \alpha + 1 - \sqrt {(\lambda \alpha + 1) ^ {2} + 4 \mu \lambda (1 - \alpha)}}{2 \mu \lambda (1 - \alpha)}\right).
$$

The feasible values of $F ( { \bar { \theta } } _ { Q } )$ and $F ( { \bar { \theta } } _ { N } )$ in the interval $p \in$ $[ 0 , { p _ { \mathrm { m a x } } } ]$ are plotted in Figure B.1. It can be readily seen that $F ( { \bar { \theta } } _ { N } ) = F ( { \bar { \theta } } _ { Q } )$ for $\alpha = 1$ , irrespective of the value of $p ,$ and for $\alpha \neq 1$ whenever $p = 0 \mathrm { ~ o r ~ } p = p _ { \mathrm { m a x } }$ . In all other cases $F ( { \bar { \theta } } _ { N } ) \neq F ( { \bar { \theta } } _ { Q } )$ according to the proposition.

## B.3. Proposition 2

Given that $F ( { \bar { \theta } } _ { N } ) = F ( { \bar { \theta } } _ { Q } )$ under our assumptions, it follows that

$$
\Pi_ {Q} - \Pi_ {N} = \Lambda \beta p = \mu r \left(1 + \frac {1}{1 + \lambda} - \frac {2}{\sqrt {1 + \lambda}}\right),
$$

which is always greater than zero for $\mu , r , \lambda > 0$

Figure B.1 Active CPs Under QoS Tiering (Gray) and Net Neutrality (Black) for Different Distributions of CPs Congestion Sensitivity 4Á5  
![](/api/attachments/6ENPYBRB/fulltext/images/754942bfaf9ad8353c9871c4ccc97235f23b4d6413a8b1082c1df604945878fd.jpg)  
Note. The figure is derived fo $\mu = 7 / 4 , \lambda = 1 , r = 1 0 $ , but qualitatively identical results are obtained for other parameter values.

## B.4. Proposition 3

$$
\begin{array}{l} \text {B.4. Proposition 3} \\ \Delta W = (\Pi_ {Q} - \Pi_ {N}) + (\Gamma_ {Q} - \Gamma_ {N}) \\ = \lambda r \left(\underbrace {(w _ {N} - w _ {Q 1}) \int_ {\tilde {\theta}} ^ {\tilde {\theta}} \theta d \theta} _ {\text {congestion alleviation to priority class}} - \underbrace {(w _ {Q 2} - w _ {N}) \int_ {0} ^ {\tilde {\theta}} \theta d \theta} _ {\text {congestion aggravation to best - effort class}}\right) \\ = \frac {\lambda r}{2} ((\bar {\theta} ^ {2} - \tilde {\theta} ^ {2}) (w _ {N} - w _ {Q 1}) - \tilde {\theta} ^ {2} (w _ {Q 2} - w _ {N})). \end{array}\tag{B7}
$$

Thus,

$$
\begin{array}{r c l} \Delta W > 0 & \Leftrightarrow & \frac {w _ {N} - w _ {Q 1}}{w _ {Q 2} - w _ {N}} > \frac {\tilde {\theta} ^ {2}}{\bar {\theta} ^ {2} - \tilde {\theta} ^ {2}} \\ & \Leftrightarrow & \frac {1 - \beta}{\beta} > \frac {(1 - \beta) ^ {2}}{1 - (1 - \beta) ^ {2}} \\ & \Leftrightarrow & 0 <   \beta <   1 \end{array}
$$

Equation (B7) reveals that the overall effect of QoS tiering on welfare depends on the relative size of the congestion alleviation effect to providers in the priority class (vertically hatched area in Figure B.2) versus the congestion aggravation effect to providers in the best-effort class (horizontally hatched area in Figure B.2). These effects relate directly to the main argument of proponents and opponents of net neutrality, respectively.

## B.5. Proposition 4

Incentives to invest in network capacity are higher under QoS tiering iff marginal revenues from priority sales are greater than zero, provided that the ISP revenues are concave, and the costs of capacity expansion convex in $\mu .$ . The latter is warranted by assumption. To ensure that the ISP’s revenues are concave, the property $\partial ^ { 2 } \Pi _ { O } / \partial \mu ^ { 2 } \le 0$ has to be fulfilled. The second order condition is thus given by

$$
\begin{array}{c} \frac {\partial^ {2} \Pi_ {Q}}{\partial \mu^ {2}} = - \frac {\iota (1 + \lambda)}{\mu^ {3}} + \underbrace {\left[ \frac {\partial^ {2} r (\bar {\theta})}{\partial \bar {\theta} ^ {2}} \frac {\bar {\theta}}{2} + \frac {\partial r (\bar {\theta})}{\partial \bar {\theta}} \right]} _ {A} \\ \cdot \frac {\partial \bar {\theta}}{\partial \mu} \underbrace {\left(1 + \frac {1}{(1 + \lambda)} - \frac {2}{\sqrt {1 + \lambda}}\right)} _ {B} <   0. \end{array}
$$

Figure B.2 Congestion Alleviation vs. Congestion Aggravation Effect of QoS Tiering  
![](/api/attachments/6ENPYBRB/fulltext/images/d0445e519a881d12a2f26e6012133e6839c74f00a9c8888f048c3604a289e78f.jpg)

Because $B \geq 0$ always holds, the $\mathrm { I S P ^ { \prime } s }$ revenues are concave if

$$
\frac {\partial^ {2} \Pi_ {Q}}{\partial \mu^ {2}} \leq 0 \left\{ \begin{array}{l l} A \leq 0 & \text {   always   } \\ A > 0 & \text {   if   } \frac {\iota (1 + \lambda) ^ {2}}{\mu^ {3} B} \geq A. \end{array} \right.
$$

It is easy to see that $A \le 0$ is warranted if ad revenues are decreasing (which is given by assumption) and concave (or not too convex). Otherwise we must assume that the condition in the second case holds. However, alternatively it can also be assumed that the second order condition holds locally around $\mu ^ { * }$ . Now consider $\Pi _ { Q } - \Pi _ { N } = \Lambda \beta p$ . Differentiating with respect to $\mu$ yields

$$
\frac {\partial (\Pi_ {Q} - \Pi_ {N})}{\partial \mu} = \frac {\sqrt {\lambda + 1} ((\lambda + 1) - \sqrt {\lambda + 1})}{(\lambda + 1) \sqrt {\lambda + 1}} \left[ \frac {\partial r (\bar {\theta})}{\partial \bar {\theta}} \frac {\partial \bar {\theta}}{\partial \mu} \mu + r (\bar {\theta}) \right]
$$

The sign of the derivative is determined by the part in square brackets. Notice from (B3) and (B4) that ${ \partial } { \bar { \theta } } / { \partial } \mu =$ $1 / ( \lambda + 1 )$ and $\mu = \bar { \theta } ( \lambda + 1 )$ . Consequently,

$$
\frac {\partial (\Pi_ {Q} - \Pi_ {N})}{\partial \mu} > 0 \Leftrightarrow \varepsilon^ {r} = \frac {\partial r (\bar {\theta})}{\partial \bar {\theta}} \frac {\bar {\theta}}{r (\bar {\theta})} > - 1
$$

Note that the gross industry advertisement revenue under net neutrality is given by $R ( \bar { \theta } ) = \lambda r ( F ( \bar { \theta } ) ) F ( \bar { \theta } )$ . It is sensible to assume that $R ( \cdot )$ does not decrease as more content becomes available. Thus, under the uniform distribution,

$$
\frac {\partial R (\cdot)}{\partial \bar {\theta}} = \lambda \frac {\partial r (\cdot)}{\partial \bar {\theta}} \bar {\theta} + \lambda r (\cdot) > 0,
$$

which holds iff $\varepsilon ^ { r } > - 1$ , in which case QoS tiering leads to more investments.

## B.6. Proposition 5

To see that the overall congestion level, w, decreases with capacity expansion, we show that $\partial w / \partial \mu = \partial ( 1 / ( \mu - \Lambda ) ) /$ $\partial \mu < 0 .$ . Notice that $\Lambda = \bar { \theta } \lambda = \lambda \mu / \lambda + 1 _ { \mathit { \Omega } }$ , so that $\partial \Lambda / \partial \mu =$ $\lambda / \lambda + 1 < 1$ . Therefore, it holds that $\partial ( \mu - \Lambda ) / \partial \mu > 0$ and consequently, $\partial ( 1 / ( \mu - \Lambda ) ) / \partial \mu < 0$ 0 By Equations (2) and (3) it is immediately obvious that the gross utility of customers and CPs increases as the congestion level decreases. The homogeneity of customers allows the ISP to fully expropriate the additional customer utility. Capacity expansion also increases the amount of active CPs because ${ \partial \bar { \theta } } / { \partial \mu } > 0$ by Equation (B4). Before the capacity expansion occurred, these CPs had a surplus of zero and are therefore unambiguously better off.

If QoS tiering provides a higher capacity level $( \mu _ { Q } ^ { * } >$ $\mu _ { N } ^ { * } ) _ { \scriptscriptstyle { \cdot } }$ , the critical CP that is just as equally well off as under network neutrality is determined by the equation $( 1 \textrm { -- }$ $\breve { \theta } w _ { N } ) \lambda r _ { N } = ( 1 - \breve { \theta } w _ { Q 1 } ) \lambda r _ { Q } - \lambda p$ . Inserting (11) and reformulating yields

$$
\breve {\theta} = \frac {(r _ {N} - r _ {Q}) w _ {Q} + (w _ {Q} - w _ {Q 1})}{w _ {Q} (w _ {N} r _ {N} - w _ {Q} r _ {Q})}.\tag{B8}
$$

Because $\mu _ { Q } ^ { * } > \mu _ { N } ^ { * }$ , it immediately follows that that $w _ { N } > w _ { Q } ,$ ${ \bar { \theta } } _ { N } < { \bar { \theta } } _ { Q }$ and thus $r _ { N } \ge r _ { Q }$ . It is easy to see that $0 < \breve { \theta } < \bar { \theta } _ { Q } =$ $1 / w _ { Q } .$ Therefore, all CPs in the interval $( { \breve { \theta } } , { \bar { \theta } } _ { Q } ]$ are better off than under network neutrality.

## B.7. Proposition 6

We consider each regime separately and show that the conditions with respect to efficient investments coincide. First, we derive the conditions for which $\partial ( W _ { N } - \Pi _ { N } ) / \partial \mu$ is larger than zero:

$$
\begin{array}{c} W _ {N} - \Pi_ {N} = \frac {\lambda}{2 (\lambda + 1)} \mu r (\bar {\theta}) \\ \frac {\partial (W _ {N} - \Pi_ {N})}{\partial \mu} > 0 \Leftrightarrow \frac {\partial r (\bar {\theta})}{\partial \bar {\theta}} \frac {\bar {\theta}}{r (\bar {\theta})} > - 1 \Leftrightarrow \varepsilon^ {r} > - 1 \end{array}
$$

The difference of private and efficient investment incentives under the QoS tiering regime is

$$
\begin{array}{c} W _ {Q} - \Pi_ {Q} = \frac {\sqrt {\lambda + 1} - 1}{\lambda + 1} \mu r (\bar {\theta}) \\ \frac {\partial (W _ {Q} - \Pi_ {Q})}{\partial \mu} = \frac {\sqrt {\lambda + 1} - 1}{\lambda + 1} \bigg (\frac {\partial r (\bar {\theta})}{\partial \bar {\theta}} \mu + r (\bar {\theta}) \bigg) > 0 \\ \Leftrightarrow \frac {\partial r (\bar {\theta})}{\partial \bar {\theta}} \frac {\bar {\theta}}{r (\bar {\theta})} > - 1 \Leftrightarrow \varepsilon^ {r} > - 1 \end{array}
$$

By the same argument as in the proof of Proposition 4, only $\varepsilon ^ { r } > - 1$ is feasible, and thus the proposition obtains.

## B.8. Proposition 7

To show that the ISP under a minimum quality standard enforcement of $w _ { Q 2 } = w _ { N }$ has a higher incentive to invest in capacity than under network neutrality, we have to show that $\mu _ { \mathrm { M Q S } } > \mu _ { N } ^ { * }$

$$
\begin{array}{r c l} w _ {Q 2} = w _ {N} & \Leftrightarrow & \frac {\mu_ {\mathrm{MQS}}}{\mu_ {\mathrm{MQS}} - \lambda \bar {\theta}} \frac {1}{\mu_ {\mathrm{MQS}} - \lambda \beta \bar {\theta}} = \frac {1}{\mu_ {N} ^ {*} - \lambda \bar {\theta} _ {N}} \\ & \Leftrightarrow & \mu_ {\mathrm{MQS}} = \frac {1 + \lambda}{1 + \lambda (1 - \beta)} \mu_ {N} ^ {*} \end{array}
$$

Because $\beta < 1 .$ , it is easy to see that $\mu _ { \mathrm { M Q S } } > \mu _ { N } ^ { * }$ always holds true.

## B.9. Proposition 8

In the QoS tiering regime with maximum quality degradation, the last CP to enter the market is located at $\bar { \theta } _ { D } = ( \mu ( 1 -$ $p _ { D } / r ) ) / ( 1 + \lambda ( 1 - p _ { D } / r ) )$ . In contrast, the last CP to enter under network neutrality, or equivalently under the unhampered QoS tiering regime, is located at $\bar { \theta } _ { N , Q } = \mu / ( 1 + \lambda )$ Obviously, for $p _ { D } = 0 ,$ which corresponds to a network neutrality regime, the indifferent CPs coincide. However, $\forall p _ { D } >$ 0 it easy to see that ${ \bar { \theta } } _ { D } < { \bar { \theta } } _ { N , Q }$ for $\lambda > 0 > r / ( p _ { D } - r )$ 5. This proves the first part of the proposition.

The ISP’s profit under maximum quality degradation is $\Pi _ { { D } } = a ( p _ { D } ) + \lambda \bar { \theta } _ { { D } } ( p _ { D } ) p _ { D } ,$ , which is maximized by a price of $p _ { D } = [ r ( 1 + \lambda ) - \sqrt { r ( v + r ( 1 + \lambda ) ) } ] / \lambda$ . At this price level, $W _ { D } <$ $W _ { N }$ iff $v < r \lambda ( 1 + \lambda )$ , which is the same condition as for a positive equilibrium price. Thus, as long as $p _ { D } > 0$ (which is shown in Proposition 9), welfare is lower under QoS tiering with maximum quality differentiation compared to network neutrality (which again has lower welfare than the unhampered QoS tiering regime in the short run).

## B.10. Proposition 9

Inserting optimal prices and solving $\Pi _ { D } > \Pi _ { Q }$ for v yields

$$
\begin{array}{c} v <   r \Big (\lambda (3 + 2 \lambda - 2 \sqrt {\lambda + 1}) \\ - 2 \sqrt {\lambda (\lambda + 1) ^ {2} (\lambda + 2 - 2 \sqrt {\lambda + 1})} \Big) \equiv \underline {{v}}. \end{array}\tag{B9}
$$

Furthermore, $\forall \lambda > 0$ it holds that $\underline { { v } } < r \lambda ( 1 + \lambda )$ at which $p = 0 .$ . Thus, the ISP never engages in maximum quality degradation at $p _ { D } \leq 0$ but prefers the unhampered QoS tiering regime instead.

## References

Armstrong M (2006) Competition in two-sided markets. RAND J. Econom. 37(3):668–691.

Brennan T (2010) Net neutrality and minimum quality standards: Network effects vs. market power justifications. Spiecker gen. Göhmann I and Krämer J eds. Network Meutrality and Open Access. (Nomos Publishing, Baden Baden), 61–80.

Cheng HK, Bandyopadhyay S, Guo H (2011) The debate on net neutrality: A policy perspective. Inform. Systems Res. 22(1): 60–82.

Choi JP, Kim B-C (2010) Net neutrality and investment incentives. RAND J. Econom. 41(3):446–471.

Crawford GS, Shum M (2007) Monopoly quality degradation and regulation in cable television. J. Law Econom. 50:181–219.

Crowcroft J (2007) Net neutrality: The technical side of the debate— A white paper. Internat. J. Comm. 1(1):567–579.

Dou W (2004) Will internet users pay for online content? J. Advertising Res. 44(4):349–359.

Economides N (1998) The incentive for non-price discrimination by an input monopolist. Internat. J. Indust. Organ. 16(3): 271–284.

Economides N, Hermalin B (2012) The economics of network neutrality. RAND J. of Econom. Forthcoming.

Economides N, Tåg J (2008) Net neutrality on the internet: A twosided market analysis. Inform. Econom. & Policy. Forthcoming.

European Commission (2009) Directive 2009/136/ec of the European parliament and of the council of 25 November 2009. Official J. Eur. Union L337:11–36. http://eur-lex.europa.eu/ LexUriServ/LexUriServ.do?uri=OJ:L:2009:337:0011:0036:En:PDF.

FCC (2010) Report and order: In the matter of preserving the open internet broadband industry practices. FCC 10-201, Washington, DC.

Fehrenbacher K (2010) Caught on video: Google CEO dishes on Google Wave, Verizon and social strategy. Accessed March 29, 2011, http://gigaom.com/mobile/google-ceo-dishes-on-google -wave-verizon-social-strategy/.

Foros Ø, Kind HJ, Sørgard L (2002) Access pricing, quality degradation, and foreclosure in the Internet. J. Regulatory Econom. 22(1):59–83.

Hahn R, Wallsten S (2006) The economics of net neutrality. Berkeley Econom. Press—Economists’ Voice 3(6):1–7.

Hahn R, Litan R, Singer H (2007) The economics of wireless net neutrality. J. Competition Law Econom. 3(3):399–451.

Hermalin BE, Katz ML (2007) The economics of product-line restrictions with an application to the network neutrality debate. Inform. Econom. Policy 19(2):215–248.

Jamison M, Hauge J (2008) Getting what you pay for: Analyzing the net neutrality debate. Mimeo, Social Science Research Network. Accessed March 29, 2011, http://ssrn.com/ abstract=1081690.

Kleinrock L (1976) Queuing Systems, Vol. 1 (John Wiley & Sons, New York).

Lambert P (2010) Vodafone and Telefonica are overplaying their hand with Google. Accessed December 12, 2010, http://www .telecoms.com/18389/vodafone-and-telefonica-are-overplaying -their-hand-with-google/.

Lessig L (2001) The Future of Ideas (Random House, New York).

McDysan D (1999) QoS and Traffic Management in IP and ATM Networks (McGraw-Hill, New York).

O’Connell P (2005) At SBC, it’s all about “scale and scope.” Bus. week (November 7, 2005) http://www.businessweek.com/ magazine/content/05\_45/b3958092.htm.

Owen B, Rosston G (2006) Local broadband access: Primum non nocere or primum processi? A property rights approach. Lenard T, May R, eds. Net Neutrality or Net Neutering: Should Broadband Internet Services Be Regulated? (Springer, New York), 163–194.

Rochet JC, Tirole J (2006) Two-sided markets: A progress report. RAND J. Econom. 37(3):645–667.

Ronnen U (1991) Minimum quality standards, fixed costs, and competition. RAND J. Econom. 22(4):490–504.

Schneibel G, Farivar C (2010) Deutsche telekom moves against Apple, Google and net neutrality. Deutsche Welle. (July 4). Accessed March 29, 2012, http://www.dw-world.de/dw/ article/0,,5439525,00.html.

Schuett F (2010) Network neutrality: A survey of the economic literature. Rev. Network Econom. 9(2):1–13.

Sidak JG (2006a) A consumer-welfare approach to network neutrality regulation of the Internet. J. Competition Law Econom. 2(3):349.

Sidak JG (2006b) Hearing on network neutrality. Testimony before the United States Senate, Committee on Commerce, Science and Transportation, Washington, DC.

Sydell L (2006) Internet debate—Preserving user parity. All Things Considered, National Public Radio. (April 25). Accessed March 29, 2012, http://www.npr.org/templates/story/story .php?storyId=5362403.

Sydell L (2007) Firms abandon online subscription plans. All Things Considered, National Public Radio. (September 19). Accessed March 29, 2012, http://www.npr.org/template/ story/story.php?storyId=14537587.

Van Schewick B (2006) Towards an economic framework for network neutrality regulation. J. Telecomm. High Tech. Law 5(2):329–391.

Wu T (2003) Network neutrality, broadband discrimination. J. Telecomm. High Tech. Law 2(1):141–176.

Wu T, Yoo CS (2007) Keeping the Internet neutral?: Tim Wu and Christopher Yoo debate. Federal Comm. Law J. 59(3):575–592.

Wyatt E (2010) Google and Verizon near deal on web pay tiers. New York Times. (August 4). Assessed March 29, 2012, http:// www.nytimes.com/2010/08/05/technology/05secret.html.

Yoo C (2005) Beyond network neutrality. Harvard J. Law Tech. 19:1–77.
