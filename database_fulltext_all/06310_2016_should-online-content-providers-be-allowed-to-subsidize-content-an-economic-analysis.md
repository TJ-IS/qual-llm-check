---
otero_id: 6310
otero_key: "YM5VWP2D"
title: "Should Online Content Providers Be Allowed To Subsidize Content?—An Economic Analysis"
authors: "Soohyun Cho; Liangfei Qiu; Subhajyoti Bandyopadhyay"
year: "2016"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0641"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/YM5VWP2D/fulltext/images/cae46524610201c9913e02e55103d53ad731e3d2ef81c553c6b212e50fa2a63c.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Should Online Content Providers Be Allowed To Subsidize Content?—An Economic Analysis

Soohyun Cho, Liangfei Qiu, Subhajyoti Bandyopadhyay

To cite this article:

Soohyun Cho, Liangfei Qiu, Subhajyoti Bandyopadhyay (2016) Should Online Content Providers Be Allowed To Subsidize Content?—An Economic Analysis. Information Systems Research

Published online in Articles in Advance 18 Jul 2016

http://dx.doi.org/10.1287/isre.2016.0641

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/YM5VWP2D/fulltext/images/3c18c6825ee88d823e5e197c863ad6f6c47997c831108f87e1e79f88f186a61c.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Should Online Content Providers Be Allowed To Subsidize Content?—An Economic Analysis

Soohyun Cho

Rutgers, The State University of New Jersey, Newark, New Jersey 07102; and Department of Information Systems and Operations Management, Warrington College of Business Administration, University of Florida, Gainesville, Florida 32611, soohyun.cho@warrington.ufl.edu

Liangfei Qiu, Subhajyoti Bandyopadhyay

Department of Information Systems and Operations Management, Warrington College of Business Administration, University of Florida, Gainesville, Florida 32611 {liangfei.qiu@warrington.ufl.edu, shubho.bandyopadhyay@warrington.ufl.edu}

nternet service providers (ISPs) are experimenting with a business model that allows content providers (CPs) to Isubsidize Internet access for end consumers. In this study, we develop a game-theoretical model to analyze the effects of this sponsorship of consumer data usage. We find that the ISP’s optimal network management choice of data sponsorship crucially depends on market conditions, such as the revenue rates of CPs and the fit cost of consumers. If the fit cost is low, the ISP will either allow both CPs to subsidize consumers’ Internet access, or will allow only the more competitive CP to subsidize, depending on the per-consumer revenue generation rates of CPs. If the fit cost is high, it is in the ISPs interest not to allow any subsidization. We also identify conditions under which the ISP’s network management choices of data sponsorship deviate from social optimum. These results should be of interest to the telecom industry as it searches additional revenue models, and to online CPs competing for customer loyalty. It should also be of interest to policymakers investigating into this issue.

Keywords: Internet service provider; online content provider; usage subsidization; consumer surplus; social welfare

History: Vijay Mookerjee, Senior Editor; Subodha Kumar, Associate Editor. This paper was received on March 12, 2015, and was with the authors 2 months for 2 revisions. Published online in Articles in Advance July 18, 2016.

## 1. Introduction

Consumers are increasingly migrating online to procure different types of digitized content. According to Cisco’s visual networking index, mobile Internet traffic has increased from 820 petabytes to 1.5 exabytes per month from 2012 to 2013 as consumers gained access to faster networks and created or downloaded richer media such as high-definition videos and video conferencing (Cisco 2014). In response to this growing traffic, several Internet service providers (ISPs) have proposed a plan to charge content providers (CPs) for prioritizing the latter’s content to consumers. CPs who pay a fee would have their content prioritized over that of rival CPs, thus ensuring a smoother online experience for consumers of their content. Given the relative lack of competition among ISPs in local geographies, ISPs would have both the incentive and the ability to discriminate among online content from different CPs. This has become a highly controversial issue in the past decade, bringing to the fore the ongoing debate on net neutrality (Choi and Kim 2010).

Recently, ISPs have come up with a different payment scheme for online CPs and end users. Online consumers in the United States usually subscribe to data plans with a cap on the amount of data they can use during a payment plan period. This is encountered more often on mobile broadband networks, but increasingly, ISPs on fixed broadband networks are also instituting such caps. Sensing an opportunity, AT&T developed a plan (which was quickly imitated by its competitors) whereby a particular CP could effectively subsidize the consumption of their own content: when subscribers from the ISP consume content from that particular CP, the downloaded content (up to a certain amount negotiated between the ISP and the CP) would not count toward the consumer’s ISP subscription cap (Sharma et al. 2013). Under this arrangement, eligible data usage charges are billed directly to the sponsoring company. Data sessions are identified by a “sponsored data” icon on the end user’s device, and the usage is itemized separately on the end user’s monthly invoice.<sup>1</sup> This new scheme allows CPs to pay for the bandwidth that end users consume. For example, a Seattle-area startup, Syntonic Wireless, is a subsidizing CP. Under the data subsidization plan, any content from Syntonic

Wireless that a consumer watches on her smartphone through a cellular connection would not count toward her monthly data cap. Some other sponsored data CPs listed in AT&T’s program include Aquto, 5 Screen Media, DataMi, and others (Sharma et al. 2013). This arrangement is beneficial to the CP because a consumer who consumes its content precludes herself from consuming a rival provider’s content. CPs can generate revenue from such consumers both directly through subscription or on-demand fees, and indirectly through advertising. CPs that are effective in generating revenue are in a better financial position to subsidize consumption of their content than CPs who generate less revenue (e.g., startups without an established consumer base).

All major mobile carriers are involved in data subsidization plans (or zero rating plans). For example, AT&T first announced sponsored data plans in January 2014, and Verizon announced a similar “Free-Bee Data 360” in January 2016. These sponsorship programs allow CPs to pay for the bandwidth that consumers use while accessing their content (Brodkin 2016). In late 2015, T-Mobile’s Binge On program allows subscribers to stream all the Netflix or Amazon Video (or videos from 40 other sites) they want on their phones without worrying about using up their data plans. StreamTV from Comcast allows subscribers to watch online videos for free through its own new streaming service, but would count streaming on Netflix, for instance, toward monthly data limits (Hong 2016).

Supporters of net neutrality have argued that such arrangements contradict the spirit of net neutrality, which holds that all content that is transmitted over the Internet should be treated equally (i.e., the Internet should be neutral down to every data packet, regardless of its origin, destination, or content). They argue that subsidization plans treat the subsidized packets preferentially, since consumers have more incentive to consume “free” packets over unsubsidized ones (Knutason and Gryta 2014, Kravets 2014). The telecom companies, however, have argued that these plans do not violate the principle of net neutrality since the sponsored data will be delivered at the same speed and performance as nonsponsored data (Reardon 2014). They point out that the plan affects only the CP paying for the sponsored traffic; it does not prioritize that traffic, nor does it throttle usage of nonsponsored content (Knutason and Gryta 2014). However, some CPs are contesting that view. YouTube, which is not a member of T-Mobile’s Binge On program, recently complained that its videos were not being streamed at HD quality, which is a requirement of T-Mobile for its Binge On partners (Kastrenakes 2015).

Sponsorship of content is not only a U.S.-centric phenomenon. In Australia, when Netflix began its streaming services during March 2015, it came into an agreement with iiNet, Australia’s second largest ISP, that Netflix content will not count toward the data caps that the ISP enforces among its customers (Brodkin 2015a). This practice is actually common in Australia, so much so that Netflix defended its decision as being a result of what their competitors did. Facebook’s Internet.org platform provides free access to consumers to a limited number of websites in countries like India, Kenya, Colombia, and elsewhere: when consumers visit these sites through Internet.org, they will not be billed for their data usage (Nichols 2015).<sup>2</sup> To achieve this goal, Facebook has teamed up with local ISPs—for example, in India, it has teamed up with Reliance Communications in February 2015 (Facebook 2015). However, in 2016, India’s main telecommunications regulatory agency has banned Free Basics, the data sponsorship plan proposed by Facebook. The biggest objection to Facebook’s Free Basics is that it offers only a few CPs chosen and controlled by Facebook, which may have a negative impact on digital content innovation (Greenstein et al. 2016). Facebook’s CEO Mark Zuckerberg has publicly defended the program against critics, which makes the practice of data subsidization a frontline debate in Internet policy (Hong 2016).

U.S. regulators are exploring the welfare implications of the new data subsidization plans. In letters to AT&T and T-Mobile, the Federal Communications Commission (FCC) wrote, “We want to ensure that we have all the facts to understand how these services (data subsidization) relate to the commission’s goal of maintaining a free and open Internet while incentivizing innovation and investment from all sources” (Kang 2015, p. 84). While FCC Chairman Tom Wheeler has said the commission would be “keeping an eye on” the data subsidization programs, he has praised them as “highly innovative and highly competitive” (Melendez 2015). From a policy perspective, it is vitally important to provide a framework to analyze the impact of the new data subsidization plans on social welfare and understand its policy implications.

Without broaching the issue of whether such plans violate the principle of net neutrality, our research analyzes the subsidization plans within an economic framework. We identify the incentives of the different players (the ISP, CPs, and consumers) to analyze the dominating equilibrium outcomes. We compare the consumer surplus and social welfare under such equilibria with the baseline scenario in which the ISP does not implement a subsidization plan.

The rest of this paper is arranged as follows. In Section 2, we review the literature that motivated our research. We then explain our model, analyze it under four subsidization scenarios, and discuss our results. Finally, in the conclusion section, we analyze the results, share their policy implications, and provide some possible directions for future research.

## 2. Literature Review

Our research draws on the general analysis framework for network management with three types of players. There are two streams of existing literature on network management. The first focuses on the economic analysis of net neutrality within a two-sided market framework and discusses the impact of access fees from CPs for the preferential delivery of digital content to consumers (Choi and Kim 2010, Cheng et al. 2011).

The second stream looks at subsidization plans in communication technology, which includes both hardware and software products. One of the reasons subsidization plans have drawn recent research and media attention is that the household budget for cell phone service has been growing over the past decade. Specifically, after the introduction of Apple’s iPhone, from 2007 to 2011, the average annual household expenditure on cell phone service has jumped by 10%, and this trend is predicted to continue for a few years (Troianovski 2012). According to Chaudhury and Rooke (2014), mobile carriers are aware of this trend, and are subsidizing their consumers’ smartphone purchase as a trade-off for long-term service contracts, with the goal of increasing their revenue from customers. However, as handset prices increase, this model becomes less attractive to mobile carriers, since they are forced to subsidize a larger fraction of the cost of the device.

In addition, Inoue et al. (2011) found that when deciding between mobile carriers, customers care more about the monthly cost of their service contract than they do about the discount price offered on the phone itself. In other words, consumers focus most on the subsidization of content when choosing their cell phone service provider. Marcus (2011) analyzed whether the increasing cost of online traffic would be borne by ISPs or CPs. His research suggested that ISPs can improve earnings without sacrificing revenue by proposing strategies in which CPs subsidize a portion of the monthly online traffic cost for their consumers. Economides and Hermalin (2015) used online traffic congestion to examine the effect of CPs’ subsidies on their users. Ma (2014) examined competition among CPs to subsidize data usage costs. The analysis assumed that an ISP does not charge CPs, and that any CPs voluntarily subsidize their users’ cost for Internet connectivity, which in turn affected the users’ choice of data plan. To our knowledge, none of the existing literature addresses the issues raised by the recently announced ISP plans to deliver sponsored (subsidized) data at the same speed as nonsponsored data, thereby allowing CPs to subsidize their users’ monthly costs through payments to ISPs without affecting the speed of delivery of their content. In this research, we consider this phenomenon: a contract between ISPs and CPs that does not discriminate in terms of online traffic speed but nonetheless affects consumers’ choice of CPs.

Hande et al. (2009) investigated a similar pricing structure with a price per unit data rate. In addition, they presented a price allocation subsidization plan in which CPs share the cost of connectivity with end users; in this model, the price charged by the ISP for connectivity is split between CPs and end users. The ISP chooses the delivery speed based on the usage of end users. In the competitive ISP market, CPs will set price q, which is paid to an ISP for sponsoring their consumers and maximizing their profits. In a monopoly ISP market, the ISP controls all three variables to maximize its profits (i.e., the price p it charges to the consumers, the price q it charges the CPs, and the delivery speed between CPs and end users). However, even though the monopoly ISP controls the price to deliver online traffic in the monopoly market, a controlled delivery speed based on price would violate the net neutrality principles and contradict the current sponsored data offerings of ISPs. Therefore, unlike Hande et al. (2009), we examine a subsidization plan that complies with the principle of delivering both sponsored and nonsponsored content at the same speed. In addition, we model the CPs to participate in sponsored-data allocation by deciding on the amount of sponsored data, which also mirrors reality.

In Section 3, we present our model. We investigate various ways for an ISP to allow CPs to sponsor consumer data usage for the end users. We then analyze how these proposals affect ISP and CP profits, consumer surplus, and social welfare.

## 3. A Model of Data Sponsorship

Our model to analyze the subsidization plan assumes three types of players engaged with the delivery of digital content: a monopolist ISP, two competing CPs, and a unit mass of consumers. We assume the monopolist ISP has complete market coverage, and delivers content from the CPs by providing Internet access and charging a usage-based per-packet price p to end consumers. In reality, we see some ISPs offer data plans with caps: subscribers pay a monthly fee, which provides them a monthly data allowance. If they exceed the allowance (cap) they pay a price per Gigabyte (GB). For analytical tractability, a pricing structure without data usage caps has been a dominant modeling assumption in prior studies on the economics of net neutrality (Choi and Kim 2010,

Cheng et al. 2011, Krämer and Wiewiorra 2012, Economides and Tåg 2012, Economides and Hermalin 2012, Choi et al. 2015, Bourreau et al. 2015, Kourandi et al. 2016). More specifically, Economides and Hermalin (2012) compared the fixed fee case (end users pay a flat fee without data caps) with the linear per-packet fee case (linear usage pricing without data caps) and showed that the results are robust no matter which assumption is adopted: the analysis carries through with one parameter replacing another in the relevant expressions. In our main model, we adopt the assumption of a linear per-packet fee like Hande et al. (2009),<sup>3</sup> but we also present the results under a fixed subscription fee in Online Appendix C. The analytical insights remain the same. Recently, linear per-packet pricing is becoming more widely adopted in reality as the data traffic has grown explosively. Per-packet pricing allows consumers who use less data to pay accordingly and helps manage congested networks. For instance, Google’s Project Fi plan does not have an annual contract: The \$20 fixed fee of Project Fi is for voice calls and messages (not related to data consumption), “then it’s \$10 per GB for data. \$10 for 1 GB, \$20 for 2 GB, \$30 for 3 GB and so on. That’s it. With no annual contract required.”<sup>4</sup> Therefore, there are no data caps in Google’s Project Fi plan at all, and linear per-packet pricing of data is used.

In our model, the two CPs, L and H, compete to reach the end consumers. The end consumers pay the ISP for Internet access to consume digital content from CPs, and we also assume that these consumers are heterogeneous in their CP preference. For a uniform distribution of consumer preference on a line segment 601 17, we set the preference for L at 0 and the preference for H at 1.

## 3.1. Internet Service Provider

As mentioned above, the monopolist ISP charges usage-based price p per packet to consumers who want to have Internet connectivity. For ease of exposition, we assume that if CPs wish to subsidize their users’ data usage, they are also charged the same usage-based price p. We will relax this assumption in Online Appendix D, where ISPs can charge the CPs a different price for subsidization, and we find that the basic contours of our findings still hold true. Consumption is measured in packets of content (5 and the ISP is assumed to have zero marginal cost. Accordingly, the ISP’s profit is written as $\pi _ { \mathrm { I S P } } = p \cdot \lambda$ and the ISP’s profit is directly related to the amount of content consumed. Table 1 provides a list of the notations used in our model.

Table 1 List of Notations

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $p$ </td><td>Usage-based price charged to consumers and CPs  $L$  and  $H$ </td></tr><tr><td> $t$ </td><td>Fit cost parameter for an end consumer away from the content that is perfectly fitted with her preference</td></tr><tr><td> $\lambda$ </td><td>Poisson arrival rate of content requested from each consumer in packets per unit of time</td></tr><tr><td> $\lambda_{s,L}, \lambda_{s,H}$ </td><td>Poisson arrival rate of content from CPs  $L$  and  $H$ , respectively, subsidized for each consumer in packets per unit of time</td></tr><tr><td> $r_{L}, r_{H}$ </td><td>CP  $L$  and CP  $H$ &#x27;s revenue rate per packet request, respectively, for content</td></tr><tr><td> $x$ </td><td>An arbitrary consumer on [0, 1]</td></tr><tr><td> $x^{*}$ </td><td>Marginal consumer who is indifferent between CP  $L$  and  $H$  in equilibrium</td></tr><tr><td> $V(\lambda)$ </td><td>Gross value function of retrieving content for each consumer</td></tr><tr><td> $I_{L}, I_{H}$ </td><td>Functions to indicate whether ISP allows CP  $L$  or  $H$ , respectively, to subsidize the usage of their consumers</td></tr><tr><td> $U_{L}, U_{H}$ </td><td>Consumers&#x27; utility function of subscribing to  $L$  and  $H$ , respectively</td></tr><tr><td> $\pi_{\text{ISP}}$ </td><td>ISP profit</td></tr><tr><td> $\pi_{L}, \pi_{H}$ </td><td>CP  $L$  and  $H$ &#x27;s profit, respectively, with a certain subsidy plan  $i$ </td></tr><tr><td> $CS$ </td><td>Consumer surplus</td></tr><tr><td> $SW$ </td><td>Social welfare</td></tr></table>

## 3.2. Content Provider

We use an indicator function to track whether the ISP allows CPs to subsidize consumers’ usage. The indicator function is set to 1 if the ISP allows subsidization, and 0 otherwise. The indicators, $I _ { L }$ and ${ \cal I } _ { H } ,$ are endogenous variables decided by the ISP according to its profit maximization process. We assume that the CPs provide consumers with content for free, and that they earn revenue through advertising (Choi and Kim 2010, Cheng et al. 2011). The amount of revenue that a CP earns from a consumer through advertising is directly related to the amount of data the latter consumes. Without loss of generality, we assume that CP H has a better ability to attract the right consumers for its advertisers, and consequently it can charge higher fees to advertisers and has a greater revenuegeneration rate than $L , r _ { H } \ge r _ { L }$ . If CPs are allowed to subsidize consumers’ usage, the ISP charges usagebased price p per packet per consumer to CPs, and the profit equations are as follows:

$$
\pi_ {L} = r _ {L} \lambda D _ {L} - I _ {L} \cdot p \lambda_ {s, L} D _ {L},\tag{1}
$$

$$
\pi_ {H} = r _ {H} \lambda D _ {H} - I _ {H} \cdot p \lambda_ {s, H} D _ {H},\tag{2}
$$

where $D _ { L }$ and $D _ { H }$ are the demand for CP H and $L ,$ respectively, measured by their market shares, and $\lambda _ { s , L }$ and $\lambda _ { s , H }$ are the amount of data the CPs want to subsidize. The CPs in our paper are modeled as being horizontally differentiated. They produce their content on their own but have exclusive rights to their content.<sup>5</sup>

Figure 1 Timeline of the Game  
![](/api/attachments/YM5VWP2D/fulltext/images/85289da6d7eddf656f7b39b7f420a2a197f47f87b3ec0fe770f25a26fd5b1017.jpg)

## 3.3. Consumers

In this model, we consider a unit mass of consumers who access broadband content. The consumers have a gross valuation for the content, V 45, and they decide whether to purchase content based on their net utility. The net utility consists of three parts— the aforementioned gross value function, the disutility cost incurred from the difference between the consumer’s preferred and consumed content (i.e., the fit cost), and the cost of broadband access. To illustrate the deviation from the consumer’s ideal content, we introduce a fit cost t from the Hotelling framework (Hotelling 1929). When a consumer accesses the Internet to acquire content, they pay usage-based price $p$ per packet to the ISP. If L or H subsidize $\lambda _ { s , L }$ or $\lambda _ { s , H }$ packets (respectively) for their consumers, a consumer’s cost decreases by $p \lambda _ { s , L } \operatorname { o r } p \lambda _ { s , H }$ . Therefore the utility function for an arbitrary consumer x ∈ 601 17 is $U _ { L } ( { \boldsymbol { x } } ) = V ( \lambda ) - t x - p \lambda + I _ { L } \cdot p \lambda _ { s , L }$ if the consumer consumes the content from L, or $U _ { H } ( x ) = V ( \lambda ) - ( 1 - x ) t -$ $p \lambda + I _ { H } \cdot p \lambda _ { s , H }$ if the consumer consumes the content from H.

## 3.4. The Sequence of Events in the Game

In this model, the three types of players—the ISP, CPs (CP L and CP H), and consumers—make decisions to maximize their utility or profits though the sequence of events. The sequence of decisions is illustrated in Figure 1.

In stage 1, the ISP decides whether or not to allow CPs to subsidize data (deciding the value of $I _ { L }$ and $I _ { H } )$ and announces the per-packet price p to end users. To analyze all of the potential network management options of the ISP, we consider the four possible outcomes: the ISP does not allow either CP to subsidize packets (Case 1); the ISP allows only L to subsidize packets (Case 2); the ISP allows only H to subsidize packets (Case 3); and the ISP allows both L and H to subsidize packets (Case 4). Table 2 presents these four network management options.

In stage 2, CPs L and H, which have contract(s) with the ISP, decide how much content they will subsidize for their users. In stage $^ { 3 , }$ consumers choose a CP. We use backward induction to deduce the subgame perfect Nash equilibrium (SPNE) of the players’ actions in each stage. In stage 3, consumers choose their preferred CP, after factoring in the $\mathrm { I S P } ^ { \prime } \mathrm { s }$ usage-based price p per packet, the CPs’ plan to subsidize their users with the amount of packets and  , and <sub>S1</sub> <sub>L</sub> S1 H their intrinsic preference for L and H. The consumers’ decisions can be demonstrated by the marginal consumer x<sup>∗</sup> who is indifferent between L and H. That is, x\* the consumers located in 601 x<sup>∗</sup>7 choose L and the consumers located in choose H. In an equilibrium, 6x<sup>∗</sup>1 17 the demand for each CP is and D<sub>L</sub> = x<sup>∗</sup>, D<sub>H</sub> = 1 − x<sup>∗</sup>.

Table 2 ISP’s Network Management Options

<table><tr><td>Case 1ISP does not allow either CP to subsidize.</td><td>Case 2ISP allows only L to subsidize packets.</td></tr><tr><td>Case 3ISP allows only H to subsidize packets.</td><td>Case 4ISP allows both L and H to subsidize packets.</td></tr></table>

Moving back to stage 2, let us examine the CPs’ decisions. Given the consumer information from stage 3, the CPs will decide on the number of packets to subsidize for their users to maximize their profits. We use the first-order condition to solve the profit maximization problem for the CPs.

Finally, we analyze the ISP’s decision in stage 1. The ISP decides whether to contract with L or H to maximize its profit and sets a usage-based price $p .$ Because of the full market coverage assumption and the participation constraints, the ISP will set its prices so that both the consumers’ utility and the CPs’ profit are nonnegative. Taking these constraints into consideration, the ISP’s profit maximization problem is as follows:

$$
\max _ {p} \pi_ {\mathrm{ISP}}
$$

$$
\mathrm{s.t.} U _ {H} (x ^ {*}) \geq 0, U _ {L} (x ^ {*}) \geq 0,
$$

$$
\pi_ {L} (\lambda_ {s, L} ^ {*}) \geq 0, \quad \pi_ {H} (\lambda_ {s, H} ^ {*}) \geq 0,\tag{3}
$$

(4)

$$
0 \leq x ^ {*} \leq 1,\tag{5}
$$

$$
0 \leq \lambda_ {s, L} ^ {*} \leq \lambda , 0 \leq \lambda_ {s, H} ^ {*} \leq \lambda .\tag{6}
$$

Constraints (3) and (4) specify the participation constraints of the marginal consumer and the two CPs. Constraint (5) is self-explanatory, while (6) specifies the fact that the CPs will at most subsidize the entire content consumed by a consumer.

## 4. Results

In Lemma 2, we characterize the benchmark equilibrium (no data subsidization), in which the ISP does not have an option to allow data sponsorship. In this equilibrium, the CPs have no decision variables: the ISP sets the price, and the end consumers choose one CP according to their preferences. All proofs are relegated to Online Appendix A.

Lemma 1 (Equilibrium Without Data Subsidiza-<sup>tion).</sup> In the equilibrium without data subsidization, the equilibrium marginal consumer is $\begin{array} { r } { x ^ { * } = \frac { 1 } { 2 } , } \end{array}$ and the optimal price set by the ISP is $p = ( 2 V ( \lambda ) - t ) / \bar { ( 2 \lambda ) }$

In this study, we mainly focus on the horizontal product differentiation of CPs instead of the vertical product differentiation, so we assume consumers have the same gross valuation, $V ( \lambda )$ , for the content from different CPs. That is why the equilibrium marginal consumer is $\begin{array} { r } { x ^ { * } = \frac { 1 } { 2 } , } \end{array}$ which implies equal market share for the two CPs. The model can be extended to the vertical differentiation case with $V _ { L } ( \lambda )$ and $V _ { H } ( \lambda )$ for each CP, but the analytical insights remain the same. We discuss this more in Online Appendix B. From Lemma 2, the optimal per-packet price set by the ISP increases with consumers’ gross valuation $V ( \lambda )$ and decreases with the fit cost t. Because of the full market coverage assumption, the ISP’s ability to extract consumer surplus is constrained by the marginal consumer. Among all consumers, the marginal consumer is the one who has the lowest level of utility because of the fit cost t. Therefore, the optimal price set by the ISP should let the marginal consumer’s utility be zero.

Next, we describe the results when the ISP can maximize its profits by choosing one of the network management options described in Table 2. As outlined in the previous section, we use backward induction to find the equilibrium amount of subsidized data, $\lambda _ { s , L } ^ { * }$ and $\lambda _ { s , H } ^ { * } ,$ and the usage-based price $p ^ { * }$ in each case, and the results are summarized in Tables 3–5. Given the values of the exogenous parameters  and $V ( \lambda ) .$ Tables 3–5 show that the equilibrium values of $\lambda _ { s , L } ^ { * } ,$ $\lambda _ { s , H } ^ { * } ,$ and $p ^ { * }$ are dependent on the revenue-generation rates of the $\mathrm { C P s } , r _ { L }$ and $r _ { H } ,$ and consumers’ fit cost, t. In Case 1, the ISP does allow either CP to subsidize traffic, so it is equivalent to the benchmark case in the absence of data subsidization.

Lemma 2 (Data Subsidization). <sub>Depending</sub> <sub>on</sub> <sub>the</sub> values of the different parameters, there are several possible cases. When data subsidization is not allowed by the

Table 3 Equilibrium in Case 2

<table><tr><td>Conditions</td><td> $\lambda^{*}_{s,L}$ </td><td> $p^{*}$ </td></tr><tr><td> $r_{L}<\frac{t}{\lambda}$ </td><td>0</td><td> $\frac{2V(\lambda)-t}{2\lambda}$ </td></tr><tr><td> $\frac{t}{\lambda}\leq r_{L}<\frac{4\lambda V(\lambda)+(2\lambda-3)t}{\lambda(-1+2\lambda)}$ </td><td> $\frac{2\lambda(r_{L}\lambda-t)}{4V(\lambda)-3t+r_{L}\lambda}$ </td><td> $\frac{V(\lambda)}{\lambda}+\frac{r_{L}\lambda-3t}{4\lambda}$ </td></tr><tr><td> $r_{L}\geq\frac{4V(\lambda)+t(\lambda-2)}{\lambda^{2}}$ </td><td> $\lambda$ </td><td> $\frac{2V(\lambda)-t}{\lambda}$ </td></tr></table>

Table 4 Equilibrium in Case 3

<table><tr><td>Conditions</td><td> $\lambda^{*}_{s,H}$ </td><td> $p^{*}$ </td></tr><tr><td> $r_{H}<\frac{t}{\lambda}$ </td><td>0</td><td> $\frac{2V(\lambda)-t}{2\lambda}$ </td></tr><tr><td> $\frac{t}{\lambda}\leq r_{H}<\frac{4\lambda V(\lambda)+(2\lambda-3)t}{\lambda(-1+2\lambda)}$ </td><td> $\frac{2\lambda(r_{H}\lambda-t)}{4V(\lambda)-3t+r_{H}\lambda}$ </td><td> $\frac{V(\lambda)}{\lambda}+\frac{r_{H}\lambda-3t}{4\lambda}$ </td></tr><tr><td> $r_{H}\geq\frac{4V(\lambda)+t(\lambda-2)}{\lambda^{2}}$ </td><td> $\lambda$ </td><td> $\frac{2V(\lambda)-t}{\lambda}$ </td></tr></table>

Table 5 Equilibrium in Case 4

<table><tr><td>Conditions</td><td></td><td> $\lambda_{s,L}^{*}$ </td><td> $\lambda_{s,H}^{*}$ </td><td> $p^{*}$ </td></tr><tr><td> $r_{L} \leq \frac{t}{\lambda}$ </td><td> $r_{H} \leq \frac{t}{\lambda}$ </td><td>0</td><td>0</td><td> $\frac{2V(\lambda) - t}{2\lambda}$ </td></tr><tr><td> $r_{H} + 2r_{L} \leq \frac{3t}{\lambda}$ </td><td> $\frac{t}{\lambda} < r_{H} \leq \frac{4V(\lambda) - t}{\lambda}$ </td><td>0</td><td> $\frac{2(-t\lambda + r_{H}\lambda^{2})}{4V(\lambda) - 3t + r_{H}\lambda}$ </td><td> $\frac{4V(\lambda) - 3t + r_{H}\lambda}{4\lambda}$ </td></tr><tr><td> $\frac{-2V(\lambda) + 2t}{\lambda} \geq r_{L}$ </td><td> $\frac{4V(\lambda) - t}{\lambda} < r_{H}$ </td><td>0</td><td> $\lambda$ </td><td> $\frac{2V(\lambda) - t}{\lambda}$ </td></tr><tr><td> $\frac{3t}{\lambda} < 2r_{L} + r_{H}$ </td><td> $r_{H} - r_{L} \leq \frac{6V(\lambda) - 3t}{\lambda}$ </td><td> $\frac{2\lambda(-3t + (r_{H} + 2r_{L})\lambda)}{3(2V(\lambda) - 3t + (r_{H} + r_{L})\lambda)}$ </td><td> $\frac{2\lambda(-3t + (2r_{H} + r_{L})\lambda)}{3(2V(\lambda) - 3t + (r_{H} + r_{L})\lambda)}$ </td><td> $\frac{2V(\lambda) - 3t + (r_{H} + r_{L})\lambda}{2\lambda}$ </td></tr><tr><td> $\frac{-2V(\lambda) + 2t}{\lambda} < r_{L}$ </td><td> $r_{H} - r_{L} > \frac{6V(\lambda) - 3t}{\lambda}$ </td><td> $\frac{\lambda(2V(\lambda) - 2t + r_{L}\lambda)}{-3t + 4V(\lambda) + r_{L}\lambda}$ </td><td> $\lambda$ </td><td> $\frac{4V(\lambda) - 3t + r_{L}\lambda}{\lambda}$ </td></tr></table>

ISP (Case 1), the price is given by $p ^ { * } = ( 2 V ( \lambda ) - t ) / ( 2 \lambda )$ There are three possible subcases under Case 2, depending on the value of $r _ { L }$ . These are summarized in Table 3. Under Case 3, there are three possible subcases, depending on the value of $r _ { H } .$ . The results are shown in Table 4. Finally, under Case 4, there are five possible subcases, depending on the values of both $r _ { L }$ and $r _ { H } .$ . These are summarized in Table 5.

As can be observed from these results, whether the CPs sponsor (subsidize) the consumption of content by their consumers depends crucially on the amount of revenue they generate from their consumers. When the revenue generation rate is below a threshold, CPs do not have an incentive to sponsor any traffic. However, when the revenue-generation rate is higher than that threshold, the CPs begin sponsoring the connectivity to content. Finally, when the revenue-generation rate reaches a second threshold, the CPs have the incentive to fully sponsor their consumers’ traffic. We further explain the intuitions of the subsidized amount in the following propositions. A descriptive summary of all equilibrium cases of subsidization can be found in Table 6.

In the current practice of data subsidization, some CPs choose to fully subsidize their consumers, i.e., the subsidized amount is . For instance, by cooperating with music steaming services, T-Mobile waived data fees for Spotify, Pandora, iTunes radio, etc. (Kumparak 2014). Some other CPs subsidize their consumers partially, $\mathrm { i . e . , }$ the subsidized amount is less than . For instance, in its sponsored data service, AT&T enables CPs to sponsor the data usage for specific content, and CPs are able to put a limit on the amount of sponsored data content they are responsible for (partial subsidization): A CP may choose to subsidize some specific videos within its application, and a consumer will see the sponsored data icon, identifying that the videos are sponsored. When the customer clicks the icon to play the video, the data usage incurred while watching the video does not count toward her cap. In the next proposition, we examine the conditions under which partial or full subsidization occurs.

Table 6 A Descriptive Summary of All Equilibrium Cases

<table><tr><td></td><td>Conditions</td><td> $\lambda^{*}_{s,L}$ </td><td> $\lambda^{*}_{s,H}$ </td></tr><tr><td rowspan="3">Case 2</td><td>Low  $r_{L}$ </td><td>No data subsidization</td><td>N.A.</td></tr><tr><td>Moderate  $r_{L}$ </td><td>Partial data subsidization</td><td>N.A.</td></tr><tr><td>High  $r_{L}$ </td><td>Full data subsidization</td><td>N.A.</td></tr><tr><td rowspan="3">Case 3</td><td>Low  $r_{H}$ </td><td>N.A.</td><td>No data subsidization</td></tr><tr><td>Moderate  $r_{H}$ </td><td>N.A.</td><td>Partial data subsidization</td></tr><tr><td>High  $r_{H}$ </td><td>N.A.</td><td>Full data subsidization</td></tr><tr><td rowspan="5">Case 4</td><td>Low  $r_{L}$  and  $r_{H}$ </td><td>No data subsidization</td><td>No data subsidization</td></tr><tr><td>Low  $r_{L}$ , moderate  $r_{H}$ </td><td>No data subsidization</td><td>Partial data subsidization</td></tr><tr><td>Low  $r_{L}$ , high  $r_{H}$ </td><td>No data subsidization</td><td>Full data subsidization</td></tr><tr><td>Moderate  $r_{L}$  and  $r_{H}$ </td><td>Partial data subsidization</td><td>Partial data subsidization</td></tr><tr><td>High  $r_{L}$  and  $r_{H}$ </td><td>Partial data subsidization</td><td>Full data subsidization</td></tr></table>

Proposition 1 (Full Subsidization versus Par-<sup>tial</sup> <sup>Subsidization).</sup> The CPs are more likely to fully subsidize their consumers when their revenue-generation rates $r _ { L }$ and $r _ { H }$ are higher.

The underlying intuition of this proposition is that the CPs’ incentives to subsidize data depends on the impact of its market share on its profits. When its revenue-generation rate is higher, an increase in its market share can bring more profits to a CP. Therefore, a CP is more likely to fully subsidize its consumers when its revenue-generation rate is higher.

<sup>Proposition</sup> <sup>2.</sup> If both content providers are allowed to subsidize consumer data consumption, CP H has a higher incentive to subsidize data than $C P ~ L , \ i . e . , \lambda _ { s , H } ^ { * } \geq \lambda _ { s , L } ^ { * } .$

As stated previously, the CPs’ incentives to subsidize data depends on the impact of its market share on its profits. CP H’s revenue-generation rate is higher than CP L’s, so an increase in the market share will bring more profits to CP H. Therefore, CP H has a greater incentive to subsidize data than CP L.

In the next proposition, we compare the benchmark equilibrium (no data subsidization) when the option of allowing data subsidization is not available to the ISP with the results when the ISP can choose one of the network management options described in Table 2 to maximize its profits, and thereby examine the impact of data subsidization.

<sup>Proposition</sup> <sup>3.</sup> Compared with the benchmark equilibrium, when the ISP can choose one of the network management options to maximize its profits, (1) the perpacket price p weakly increases, (2) the ISP’s profit weakly increases, and (3) the change of the market share of $C P \overset { \cdot } { L }$ or H depends on the cases described in Table 2: (i) in Case 1 (no CPs are allowed to subsidize), the market share of CP L or H remains the same, (ii) in Case 2 (only CP L is allowed to subsidize), the market share of CP L weakly increases, and that of H weakly decreases, (iii) in Case 3 (only CP H is allowed to subsidize), the market share of CP L weakly decreases, and that of H weakly increases, and (iv) in Case 4 (both CPs are allowed to subsidize), the market share of CP L weakly decreases, and that of H weakly increases.

The intuition behind these results is as follows. When the ISP can choose one of the network management options according to its profit, Case 1 in Table 2 is always available: the ISP does not allow either CP to subsidize the data. In other words, the ISP’s profit in Case 1 is equal to the profit when the option of allowing data subsidization is not available. Therefore, the $\mathrm { I S P } ^ { \prime } \mathrm { s }$ profit should be at least equal to its profit in the benchmark equilibrium when it can choose one of the network management options. Under some market conditions, the ISP’s profits should be strictly greater when the network managing options are available because it can extract the CPs’ profits as well as consumer surplus in the presence of data subsidization. The same logic applies to the per-packet price $p .$ The change of CPs’ market shares depends on which CP is allowed to subsidize data. When data subsidization is not allowed, $\begin{array} { r } { x ^ { * } = \frac { 1 } { 2 } } \end{array}$ . If only CP H or L is allowed to subsidize data, the market share of CP H or L will weakly increase because data subsidization allows the CP to attract more consumers from its competitor. If both CPs are allowed to subsidize data, the market share of CP H will weakly increase and the market share of CP L will weakly decrease because, as compared with CP L, CP H has a greater incentive to subsidize data.

For a given set of parameter values, the ISP determines (a) whether to enter into a contract with one of the CPs, both CPs, or neither CP (in other words, Case 1, 2, 3, or 4); and (b) the equilibrium price that maximizes its profits in each scenario. Unfortunately, the surfeit of parameters makes it impossible to analytically derive the dominating equilibrium in many cases, which is why we employ numerical analyses. We present analytical results as formal propositions, while all of the conclusions we draw from the numerical analyses are stated as results. Based on the equilibrium results, we present the preferred cases in terms of ISP’s profits, consumer surplus, and social welfare with different parameter values.

Consumer choice depends on the fit cost t, which is used to model horizontal product/service differentiation between CPs (Choi and Kim 2010). If the fit cost t is high, it means that the horizontal product differentiation is high, and it is more difficult to transfer service from one CP to another in our context. If the fit cost is low, then the horizontal product differentiation is low. In an extreme case, $t = 0$ It implies no horizontal product differentiation, and two CPs provide homogenous products/services (the degree of competition is the highest). Therefore, the fit cost t measures the degree of competition between the two CPs caused by product differentiation (Kourandi et al. 2016). Another important parameter is the ratio of the revenue-generation rate of the two CPs $( r _ { L } / r _ { H } )$ When the revenue-generation rates are comparable, the ISP will find it preferable to have similar policies with regards to both CPs (since either one of them will react similarly to any proposed contract of subsidizing content for their consumers). However, if the revenue-generation rates are considerably different, the two CPs might find it advantageous to react differently to a contract proposed by the ISP. In our numerical analyses, the second factor that we examine is therefore the effect of changing the ratio of the revenue generation rates of the two CPs, i.e., $r _ { L } / r _ { H } .$

To conduct the numerical analysis, we need to choose the values of three exogenous parameters , $V ( \lambda )$ , and $r _ { H }$ . To satisfy all of the necessary conditions that are required for the existence of the equilibrium in Cases 2–4 (these are detailed within the proofs in the online appendix), we choose $\lambda = 1 , ~ V ( \bar { \lambda ) } = 1 0 ,$ and $r _ { H } = 2$ . Our results below are derived using these parameter values. To test the validity of our numerical analyses, we tried other combinations of $\lambda , ~ V ( \lambda )$ and $r _ { H }$ under the feasible regions of equilibrium results in all of the cases, and the results and propositions that follow hold for all those other values of the parameters.

Result 1 shows the interplay between the two main factors that drive the equilibrium results, the fit cost t and ratio of the revenue-generation rates of the two CPs, $r _ { L } / r _ { H }$

Result 1 (ISP’s Network Management Choices). If the fit cost is low, the ISP will choose one of the equilibria under Case 3 (only H is allowed to subsidize its packets) or one of those under Case 4 (H and L are allowed to subsidize their packets) depending on the ratio of the revenue-generation rate of the two CPs. However, if the fit cost is high, the ISP will not enter into any contract that allows subsidization of content by the CPs.

Figure 2 illustrates the ISP’s network management choices under various parameter values. The ISP’s profit is always maximized under either Case 3 or Case 4 if the fit cost is low. However, if the fit cost is high, the ISP allows no subsidization (Case 1). The following observations offer some intuitions for Result 1. First, we observe that for small values of $r _ { L } ,$ CP L will not participate in any subsidization plan because it cannot afford to pay the connectivity cost for its users. Second, if the fit cost is low, consumers may switch from one CP to another to take advantage of the subsidization. As $r _ { L }$ increases and subsidization becomes more affordable, CP L will also begin to subsidize its content to attract more consumers, but it can never happen that CP L prefers to subsidize while H does not, which is why the possible equilibria under Case 2 is always dominated (in other words, if the ISP allows data subsidization, either only H will subsidize its content or both CPs will subsidize their content). If the ISP allows both L and H to subsidize the consumers’ usage, both CPs would rather pay the ISP than lose their consumers to their rivals, allowing the ISP to charge a higher $p .$ In effect, the CPs are in a classic “prisoner’s dilemma,” which the monopolist ISP can exploit to its advantage. Accordingly, the ISP has the largest profit under Case 4 when $r _ { L }$ is not too low as compared to $r _ { H }$

Figure 2 Internet Service Provider’s Network Management Choices, V 45 = 10,  = 1, r<sub>H</sub> = 2  
![](/api/attachments/YM5VWP2D/fulltext/images/cd4ef2e7732e34c504fc0786f5b59754316defe74f074dfb19fa3832b79a5fc1.jpg)

In practical terms, a low fit cost t can be interpreted as a market condition in which the horizontal product differentiation is not too high. Therefore, the implication of our result is that the ISP will enter into a subsidization contract only if the horizontal product differentiation is not too high. In our context, the revenue of each CP comes from the advertising income based on its market share. To gain a larger market share, both CPs have incentives to subsidize data traffic. When horizontal product differentiation is low, the CPs will conduct a fiercer “price $\mathbf { W } \mathbf { a r } ^ { \prime \prime }$ by subsidizing consumers with a larger amount of data. The reason is that a CP is able to obtain a large increase in its market share by increasing its subsidization amount when the fit cost t is small. Therefore, the CPs might be trapped in a prisoner’s dilemma with regards to their decision to subsidize consumers when the fit cost t is low. The ISP will benefit from the CPs’ fierce competition and more effectively extract the $\mathrm { C P ^ { \prime } s }$ profits by allowing the data sponsorship. To highlight the importance of the fit cost t, we complement Result 1 with the following analytical proposition.

Proposition 4. <sub>If</sub> <sub>the</sub> <sub>fit</sub> <sub>cost</sub> $t \geq \lambda r _ { H } ,$ the ISP will choose not to allow either CP to subsidize data.

The intuition of this proposition is that when the fit cost is high, the competition between the CPs is less fierce, and the ISP cannot benefit from data subsidization.

It is important to note that the ISP may allow only CP H to subsidize data (Case 3) under some market conditions shown in Figure 2. An interesting observation is that before the introduction of data sponsorship, CP L earns a positive market share, $\begin{array} { r } { x ^ { * } = \frac { 1 } { 2 } } \end{array}$ However, under some market conditions, data subsidization may let CP H become the monopoly in the market and drive CP L out of the market, i.e., $x ^ { * } = 0 ,$ in Case 3. It raises an important anticompetitive concern: In the presence of data subsidization, a big CP may leverage its advantage in revenuegeneration capability to expand its market share and gain market power in digital content markets. For startups and entrepreneurs hoping to have their content spread naturally or virally, they are suddenly at a disadvantage after the introduction of data sponsorship. The following proposition characterizes the market conditions under which CP L is driven out of the market in Case 3.

<sup>Proposition</sup> <sup>5.</sup> When only CP H is allowed to subsidize data, the market share of CP $L , x ^ { * } = 0 , i f r _ { H } \geq 3 t / \lambda$ and $V ( \lambda ) \geq t$

Figure 3 Network Management Options That Maximize Consumer Surplus, $V ( \lambda ) { \stackrel { - } { = } } 1 0 , \lambda { \stackrel { - } { = } } 1 , r _ { \scriptscriptstyle H } = 2$  
![](/api/attachments/YM5VWP2D/fulltext/images/787bf262d643309097a9caa1f972fd35dd93104bf489ac7869c1c7e2c5654bcd.jpg)

This proposition tells policymakers when they should pay special attention to the $\mathrm { I S P ^ { \prime } s }$ network management decisions with regard to data subsidization. If the product differentiation is low (the fit cost t is low) and the revenue-generation rate of CP H is high, allowing only CP H to subsidize data may drive CP L out of the market. The intuition behind this proposition is that when the product differentiation is low, the data subsidization of CP H will cause a larger increase in its market share. When $r _ { H }$ is high, an increase in CP H’s market share will yield a relatively larger increase in its revenue. Therefore, if the fit cost t is low and the revenue-generation rate $r _ { H }$ is high, CP H will provide a high level of data subsidization, and hence CP L will be more likely to be driven out of the market. This analytical result helps policymakers understand the impact of data subsidization on the CPs’ competition and sheds some light on when the introduction of sponsored data is more likely to be anticompetitive. Van Schewick (2016, $\mathsf { p } . 5 )$ argued that data subsidization will end the era of “innovation without permission”—an important principle that has allowed innovation to flourish on the Internet. The reason is that in the presence of data subsidization/zero rating, more and more ISPs will tend to become gatekeepers that pick winners and losers, and CPs will need to work with ISPs to join their data subsidization programs. In particular, small CPs and start-ups without the resources to engage ISPs will be left behind.

Figure 4 (Color online) Usage-Based Price p in Terms of $r _ { L } / r _ { H } ~ { \sf a n d } ~ t , V ( \lambda ) = 1 0 , \lambda = 1 , r _ { H } = 2$  
![](/api/attachments/YM5VWP2D/fulltext/images/555f451abcd613709b1d2522886fc77419daaf83011abbcb93d6e26567536c06.jpg)

Next, we consider the conditions under which consumer surplus and social welfare are maximized. Result 1 establishes the fact that, depending on parameter values, the ISP might prefer outcomes under cases 1, 3, or 4. From a policymaker’s perspective, however, it is not only the ISP’s profit that matters. For example, policymakers might want to take into consideration other factors like consumer surplus and social welfare. Results 2 and 3 consider those factors.

Consumer surplus is the sum of consumers’ utility and is calculated as follows:

$$
\text {   Consumer   Surplus   } = \int_ {0} ^ {x ^ {*}} U _ {L} (x) d x + \int_ {x ^ {*}} ^ {1} U _ {H} (x) d x.\tag{7}
$$

Result 2 (Consumer Surplus). <sub>Consumer</sub> <sub>surplus</sub> is maximized under Case 2 or Case 4 when the fit cost is low. However, if the fit cost is high, the case without subsidization (Case 1) yields the highest consumer surplus.

Figure 3 illustrates the result graphically. It is instructive to analyze why such a result holds. As Figure 4 illustrates, the ISP charges the lowest usage-based price p under Case 1 (i.e., no subsidization). One might therefore expect that Case 1 would maximize consumer utility. However consider Case $^ { 2 , }$ in which the ISP charges the second lowest price to consumers and CPs. In this case, if consumers choose their content from CP L, they will enjoy the lowest net cost to get online (thanks to CP L’s subsidization).

(b) Cases 3 and 4  
![](/api/attachments/YM5VWP2D/fulltext/images/16ea2bfbc40042b37d6c8691b9ea383b684e71b994a70d63b8852f8256f551b6.jpg)

Next, consider the fit cost. A small fit cost implies that consumers will easily switch from their preferred CP to the rival CP. In the process, they incur a low disutility cost but they can lower their connectivity costs (from CPs’ subsidization), which increases their overall utility. Yet if consumers have a strong preference for their CP (high fit cost), they will not switch providers; they would rather pay a little more to continue using their preferred CP. Under such a scenario, they would prefer Case 4, which results in both a lower cost of connectivity (due to CP subsidization) and the opportunity to continue enjoying content from their preferred CP. However, when fit cost is really very high, the CPs balk at paying the high price required to switch the marginal consumers from their rival. Thus, for really high fit costs, consumer surplus is maximized under Case 1.

Along with the ISP profit maximization and consumer satisfaction, we examine which subsidization plan options are socially optimal. We define social welfare to be the sum of the ISP’s profit, the CPs’ profits, and the consumer surplus.

Result 3 (Social Welfare). <sub>Social</sub> <sub>welfare</sub> <sub>is</sub> <sub>max-</sub> imized under Case 1 or Case 4.

Figure 5 illustrates the proposition graphically. When the fit cost is high, the profits of the ISP and the CPs, as well as consumer surplus are maximized under Case 1, and so it is clear that social welfare under high fit cost is maximized under Case 1. Cumulatively, the overall welfare is highest under Case 4 when the fit cost is low. We will discuss the components of social welfare further in Section 5. Result 3 may guide policymakers who are interested in maximizing social welfare. The ISP should treat CPs equally according to the criterion of social welfare: When horizontal product differentiation is high (the fit cost t is high), neither CPs should be allowed to sponsor data (Case 1); when horizontal product differentiation is low (the fit cost t is low), both CPs should be allowed to subsidize data (Case 4). However, the choice of the policymakers with regards to network management options might be at odds with that of the ISP, since social welfare comprises not only the ISP’s profit but also the profits of the CPs’ profits as well as the consumers’ surplus. According to Result 1, we know that when t is low, the ISP may have an incentive to deviate from the social optimum and allow only the more efficient CP H to sponsor data.

Figure 5 Social Welfare Maximizing Network Management Options, V 45 = 10,  = 1, r = 2  
![](/api/attachments/YM5VWP2D/fulltext/images/37e00e2100eb7ae082173909c934efd6fb2e18c6430c1fe5d5242b77db235336.jpg)

Why is no subsidization or allowing both CPs to subsidize preferred from a social planner’s perspective? From a social planner’s perspective, the ISP’s pricing policy p is purely “wealth transfer” rather than “wealth creation.” In other words, end consumers’ payments to the ISP for the Internet service and CPs’ payments to the ISP for data subsidization are essentially internal transfers within the system. As far as the calculation of the social welfare is concerned, the social planner cares only about the factors that can affect net “wealth creation” (more precisely, the social planner is concerned about the net increase in social welfare). There are two factors that can impact social welfare creation in our model. The first is the total fit cost of all end consumers along 601 17, which is given by the following equation:

$$
\int_ {0} ^ {x ^ {*}} (t x) d x + \int_ {x ^ {*}} ^ {1} t (1 - x) d x = t \left(x ^ {*} - \frac {1}{2}\right) ^ {2} + \frac {t}{4}.
$$

The total fit cost is minimized when the marginal consumer is located at 1/2. The other factor that impacts the social welfare is the CPs’ revenue generation capability. Without considering the fit cost, the social planner would like to see the market share of CP H to be high because the advertising revenue rate of $\mathrm { C P } \ H , \ r _ { H } ,$ is greater than that of $\mathrm { C } \breve { \mathrm { P } } \ L , \ r _ { L }$ . These two factors together make no subsidization or allowing both CPs to subsidize the preferred outcomes from a social planner’s perspective. More specifically, there is a trade-off between these two factors. If the social planner considers only the first factor, the marginal consumer should be located as close to $\frac { 1 } { 2 }$ as possible (equal market shares). However, if only the second factor is considered, the social planner wants the marginal consumer to be as close to 0 as possible (the market share of CP H is high). Recall that in the no subsidization case (Case 1), the marginal consumer is located at ${ \frac { 1 } { 2 } } ,$ so Case 1 minimizes the total fit cost of all end consumers. On the other hand, the market share of CP H is high under Case 4. Therefore, Case 1 or

Figure 6 The Impact of the Fit Cost and the CPs’ Revenue-Generation Rates on the ${ \mathsf { I } } { \mathsf { S } } { \mathsf { P } } ^ { \prime } { \mathsf { S } }$ Equilibrium Profit, $V ( \lambda ) = 1 0 , \lambda = 1 , r _ { { \scriptscriptstyle H } } = 2$  
![](/api/attachments/YM5VWP2D/fulltext/images/5565357b5c5367a96139f1e6cbf92b14b86d589dd4c963511dd3d48b903aa79f.jpg)

Case 4 is preferred by the social planner, depending on t.

If we compare Figures 3 and 5, the network management options to maximize consumer surplus are different from the options to maximize social welfare. According to Figure 3, we know that when the revenue-generation rates of two CPs are close, Case 2 (only $\mathrm { C P } \ \bar { L }$ is allowed to subsidize) can generate a higher level of consumer surplus. However, when we consider the choice that can maximize social welfare, Case 2 is never optimal. Once again, the $\mathrm { C P s ^ { \prime } }$ revenuegeneration capability is a “wealth creation” factor, and the choice that can maximize social welfare will never allow CP L to subsidize the data because the revenue-generation rate of CP L is lower than that of CP H. Policymakers need to think about their objectives (maximizing social welfare versus maximizing consumer surplus) when they regulate the ISP’s network management choices. Under some market conditions, the choice of network management that can maximize social welfare might be at odds with the choice that maximizes consumer surplus.

We also perform some sensitivity analyses to illustrate the effect of the key model parameters on the $\mathrm { I S P } ^ { \prime } \mathrm { s }$ profit, consumer surplus, and social welfare. Figure 6 shows how the fit cost and the ratio of the CPs’ revenue-generation rate affect the $\mathrm { I S P } ^ { \prime } \mathrm { s }$ equilibrium profit. Figure 6(a) displays the $\mathrm { I S P ^ { \prime } s }$ equilibrium profit under different market conditions. Figure 6(b) depicts the contour lines of the $\mathrm { I S P } ^ { \prime } \mathrm { s }$ profit. In general, if the fit cost is high $( t > 2 )$ , the $\hat { \mathrm { C P s ^ { \prime } } }$ revenue-generation rates will have no impact on the $\mathrm { I S P ^ { \prime } s }$ profit because

![](/api/attachments/YM5VWP2D/fulltext/images/5a8f5f198d157ce2e101cdc470300152223f433d0a8832619d0dc514096065ff.jpg)  
the ISP will prefer no data subsidization when t is high (recall our Result 1). Similarly, Figures $7$ and 8 demonstrate the impact of the fit cost and the ratio of the $\mathrm { C P s ^ { \prime } }$ revenue-generation rate on the equilibrium consumer surplus and social welfare, respectively. It is worth noting that the equilibrium consumer surplus increases with the fit cost. At first glance, it seems counterintuitive because a higher t tends to reduce consumers’ utility directly. However, the $\mathrm { I S P ^ { \prime } s }$ ability to extract consumer surplus depends on t endogenously. When t is high, the ISP will charge a low price otherwise the marginal consumer’s utility becomes negative and the full market coverage is violated (in Figure $6 ,$ the $\mathrm { I S P ^ { \prime } s }$ equilibrium profit decreases with the fit cost). Therefore, in general, the equilibrium consumer surplus increases with the fit cost.

## 5. Discussion

The results in the previous section are useful in determining the equilibrium scenarios, but a policymaker would presumably want to get a sense of the distribution of the social surplus—for example, a scenario where social surplus is not maximized (but nonetheless is close to the maximum) but the surplus is more equitably distributed among the various actors would perhaps be considered better than a welfare-maximizing option where the surplus is mostly directed toward just one actor (or an option where, say, the consumer surplus is minimal). We consider such scenarios in this section. We choose four potential scenarios to discuss how the $\mathrm { I S P ^ { \prime } s }$ decisions social welfare as the sum of the profit of CP H, the profit of CP L, the consumer surplus, and the ISP’s profit.

Figure 7 The Impact of the Fit Cost and the CPs’ Revenue-Generation Rates on Equilibrium Consumer Surplus, $V ( \lambda ) = 1 0 , \lambda = 1 , r _ { H } = 2$  
![](/api/attachments/YM5VWP2D/fulltext/images/871c67117f91061196ac7f5f236713b84538e828679913c12419b122f2b41c22.jpg)

![](/api/attachments/YM5VWP2D/fulltext/images/babc0e23dfe2f47809d716abe53163dee25efd9807e69caf161214fe0cd6e8a2.jpg)

Figure 8 The Impact of the Fit Cost and the CPs’ Revenue-Generation Rates on Equilibrium Social Welfare, V 45 = 10,  = 1, $r _ { H } = 2$  
![](/api/attachments/YM5VWP2D/fulltext/images/a45eaad6a52a89a911f688ce8cc492a0e33fe1376fd7804e6da256b5c454726b.jpg)  
influence its profit, the consumer surplus, social welfare, and the CPs’ profits. In this analysis, we exclude the case with very high fit cost because then, as we mentioned earlier, Case 1 (no subsidization) is the most preferred scenario for all three types of players. The four scenarios are as follows: (1) t is small and $r _ { L } / r _ { H }$ is small (Figure 9); (2) t is small and $r _ { L } / r _ { H }$ is large (Figure 10); (3) t is large and $r _ { L } / r _ { H }$ is small (Figure 11); and (4) t is large and $r _ { L } / r _ { H }$ is large (Figure 12). The stacked bars in Figures 9 through 12 represent the

![](/api/attachments/YM5VWP2D/fulltext/images/954f0db931f92e5520d9e228fe85dccd441d0d78f87352447e2979bb197cd065.jpg)

Expectedly, if CP H is much more efficient than CP L in generating revenue $( \mathrm { i . e . , ~ } r _ { L } / r _ { H }$ is small, Figures 9 and 11), the two large components of the social welfare are the profits of H and the ISP. However, when the CPs are relatively comparable with each other (in terms of their revenue-generation rates), we see that the ISP profit makes the biggest contribution

to social welfare (Figures 10 and 12): that is, if the CPs are more or less equally competitive, their profits are mostly extracted by the ISP. At the same time, consumer surplus also suffers, as compared to that under scenarios 1 and 3. In addition, in most conditions (except when the fit cost is very high), social welfare is maximized under Case 4, which is consistent with the results discussed in Section 4. As a general rule, consumer surplus is greater when the fit cost is higher. We show this statement is true in Case 1, and the same logic follows in other cases. In Case 1, consumer surplus is given by the following equation:

Scenario 2: The components of social welfare  
Figure 9 Scenario 1 (t Is Small and $r _ { L } / r _ { H }$ Is Small)  
Scenario 1: The components of social welfare  
![](/api/attachments/YM5VWP2D/fulltext/images/a9711fd7429f88f2e7950c640912e90a2a63ff577bc1c898090e8a158b77c3e1.jpg)  
Figure 10 Scenario 2 (t Is Small and $r _ { L } / r _ { H }$ Is Large)

![](/api/attachments/YM5VWP2D/fulltext/images/fbe3ef8aa52e0ea9c82bb2ebba7f4f59bfab2516c31f11697545817e390525cb.jpg)  
Figure 11 Scenario 3 (t Is Large and $r _ { L } / r _ { H }$ Is Small)

Scenario 3: The components of social welfare  
![](/api/attachments/YM5VWP2D/fulltext/images/ded4b96e772df82df112dac8cc5fe9fc1b034abc0909c8d0fb174d11d8737da9.jpg)  
Figure 12 Scenario 4 (t Is Large and $r _ { L } / r _ { H }$ Is Large)

Scenario 4: The components of social welfare  
![](/api/attachments/YM5VWP2D/fulltext/images/04d0b9c2022fb137a80da39c31ef27369cd8a0f7f0a0da065c26c1dab397dbee.jpg)

$$
\text {   Consumer   Surplus   } = \int_ {0} ^ {1 / 2} U _ {L} (x) d x + \int_ {1 / 2} ^ {1} U _ {H} (x) d x = \frac {1}{4} t.
$$

Therefore, consumer surplus is an increasing function of fit cost t. The intuition is that the $\mathrm { I S P ^ { \prime } s }$ ability to extract consumer surplus is constrained by the marginal consumer because of the full market coverage assumption. In Case 1, the ISP can set a price such that the marginal consumer’s net utility is 0 while other consumers have positive net utility. That is the highest price that the ISP can charge, because otherwise the full market coverage assumption will be violated. Therefore, when the fit cost is low (the horizontal product differentiation is low), the ISP can more effectively extract the consumer surplus. An extreme example is when t = 0. When $t = 0 ,$ , there is no product differentiation. In Case 1, every consumer has exactly the same utility function $V ( \lambda ) - p \lambda$ , and the ISP can charge the price $p = V ( \lambda ) / \lambda$ such that every consumer’s net utility is 0. It implies that when $t = 0 ,$ , the consumer surplus is 0. By contrast, when the fit cost is high, it is more difficult for the ISP to fully extract consumer surplus. That is why consumer surplus increases with the fit cost t. If the equitable distribution of the cumulative surplus is a concern, these guidelines should provide a basis for deciding whether there is a need for intervention in the market if the ISP decides to propose a data subsidization plan to the CPs.

So far, we have assumed that the ISP charges the CPs the same per-packet price when the CPs are allowed to sponsor data traffic. However, to maximize its profit, the ISP can implement price discrimination by charging consumers p per packet and CPs c per packet. We discuss the ISP’s possibility of adopting price discrimination and present the results in Online Appendix D.

## 6. Conclusion

Subsidizing consumers for broadband usage is quickly becoming a way for CPs to get a leg up on competition. In this paper, we examine the strategy that a monopolist ISP chooses to maximize its profit if it considers allowing CPs to subsidize consumers’ data usage. As smartphones become bigger and more powerful, consumers are increasingly using them to watch videos, listen to streaming music, and for other bandwidth-hungry applications. ISPs therefore have to rapidly upgrade their broadband infrastructures to meet this exploding demand for bandwidth (Fung 2014). For many households, the cost of Internet access is already a significant portion of their budget (Troianovski 2012). ISPs are therefore trying to solve the challenge of effectively monetizing broadband traffic while increasing infrastructure capital expenditures and without passing that cost onto their consumers (Cisco 2014). Getting the CPs to subsidize bandwidth access seems to be one part of solving the challenge without running afoul of the principles of net neutrality (which, as we point out below, has been contested by some proponents of the law). It is this phenomenon that motivated our research, and we examine which method of subsidization will maximize an ISP’s profit when there are two competing CPs. Our analysis should serve as a guide for policymakers as they analyze this phenomenon.

Our research has several managerial implications. For an ISP, the best subsidization plan will involve inducing the dominant CP to pay for subsidizing its content, if the revenue-generation rate of the latter is much higher compared to its competition and the consumers are easily persuaded to switch their loyalties for content. However, in a content market dominated by two relatively comparable competitors (in terms of their per-consumer revenue-generation capability), the ISP would prefer a subsidization plan that induces both CPs to retain their customers, and subsidize them for the consumption of their content. The current practice of data subsidization is also related to the policy debate on net neutrality. Van Schewick (2016) argued that data subsidization violates key net neutrality principles and harms user choice, innovation, and competition. Critics have argued that data subsidization may undermine the core vision of net neutrality: ISPs should not act as gatekeepers that pick winners and losers online by favoring some CPs over others. Our analysis provides the analytical backbone in this debate.

There are several possible extensions to our research. In our study, the monopoly assumption for the ISP makes our model analytically tractable. As a future research direction, it would be interesting to examine the competition between multiple ISPs. When only one ISP exists in the market, it can effectively extract CPs’ profits by the introduction of data subsidization. The existence of multiple competing ISPs should make CPs better off. However, the impact of data subsidization on consumer surplus and social welfare is unclear and needs to be further examined.

Second, Guo et al. (2013) considered heavy consumers and light consumers to capture heterogeneous data usage of consumers. In the future, we intend to extend our research to explore consumers who have different data usage patterns. Curien and Moreau (2007) researched the complementary strategies between ISPs and CPs, in which access providers participate in the production and distribution of digital content. They found that these strategies benefit both access providers and CPs. Access providers acquire additional profits from coproducing content and thus generate more data consumption, and CPs take advantage of the relatively larger market size of the access providers and reduce the illegal consumption of their digital content. Our model could be extended to incorporate this setting in which the ISP is merged with a CP and thus provides both the Internet connectivity as well as the digital content. Prominent examples of such mergers can be found in the United States: Comcast, for example, has a majority stake in NBC Universal, while Google is slowly getting into the ISP market with Google Fiber (Brodkin 2015b, Nicolas and François 2007, Snider et al. 2015). The implications of subsidization in such contexts should provide additional insights, and give us a better understanding of the issues surrounding production and delivery of digital content.

Additionally, our model assumes that the ISP charges both CPs the same price for data subsidization when both of them are allowed to subsidize. In the future, it would be interesting to examine the impact of differential pricing of the CPs based on the competition intensity of CPs.

Our paper models the content subsidization issue as a short-term problem, and therefore the capacity of the ISP is assumed to be fixed. However, in a longer time horizon, as the consumption levels of the consumers increase, the ISP’s capacity, and the investment in its broadband infrastructure, will become a decision variable. The unlimited capacity in the current model setup is a limitation of our study, and capacity constraints could be another potential avenue for further research.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2016.0641.

## Acknowledgments

The authors thank the senior editor, the associate editor, and three anonymous reviewers for their detailed and constructive comments. The authors also thank Barrie Nault, Haldun Aytug, Hong Guo, Arunava Banerjee, and seminar participants at the University of Calgary for their helpful feedback.

## References

Bourreau M, Kourandi F, Valletti T (2015) Net neutrality with competing Internet platforms. J. Indust. Econom. 63(1):30–73.

Brodkin J (2015a) Google Fiber confirmed for four new metro areas, 18 cities. arstechnica (January 27), http://arstechnica .com/business/2015/01/google-fiber-confirmed-for-four-new -metro-areas-18-cities/.

Brodkin J (2015b) Netflix opposes data cap exemptions, except when it benefits from them. arstechnica (March 4), http:// arstechnica.com/business/2015/03/netflix-opposes-data-cap -exemptions-except-when-it-benefits-from-them/.

Brodkin J (2016) Verizon Wireless selling data cap exemptions to content providers. arstechnica (January 19), http://arstechnica .com/business/2016/01/verizon-wireless-selling-data-cap -exemptions-to-content-providers/.

Chaudhury R, Rooke J (2014) Wrestling the subsidy challenge in telecom. AT Kearney, http://www.atkearney.com/en/paper/-/ asset\_publisher/dVxv4Hz2h8bS/content/wrestling-the-subsidy -challenge/10192.

Cheng HK, Bandyopadhyay S, Guo H (2011) The debate on net neutrality: A policy perspective. Inform. Systems Res. 22(1):60–82.

Choi JP, Kim B (2010) Net neutrality and investment incentives. RAND J. Econom. 41(3):446–471.

Choi JP, Jeon DS, Kim BC (2015) Net neutrality, business models, and Internet interconnection. Amer. Econom. J.: Microeconomics 7(3):104–141.

Cisco (2014) Cisco visual networking index: Global mobile data traffic forecast update, 2014–2019. White paper, http://www .cisco.com/c/en/us/solutions/collateral/service-provider/ visual-networking-index-vni/white\_paper\_c11-520862.pdf.

Curien N, Moreau F (2007) The convergence between contents and access: Internalizing the market complementarity. Rev. Network Econom. 6(2):161–174.

Economides N, Hermalin BE (2012) The economics of network neutrality. RAND J. Econom. 43(4):602–629.

Economides N, Hermalin BE (2015) The strategic user of download limits by a monopoly platform. RAND J. Econom. 46(2):297–327.

Economides N, Tåg J (2012) Network neutrality on the Internet: A two-sided market analysis. Inform. Econom. Policy 24(2):91–104.

Facebook (2015) Internet.org app now available in India. (February 10), http://newsroom.fb.com/news/2015/02/internet-org -app-now-available-in-india/.

Fung B (2014) AT&T complains it needs more money for infrastructure upgrade. No, it doesn’t. Washington Post (March 25), http://www.washingtonpost.com/blogs/the-switch/wp/2014/ 03/25/att-complains-it-needs-more-money-for-infrastructure -upgrades-no-it-doesnt/.

Goel V (2015) Indian regulators suspend Facebook’s free basic services. New York Times (December 23), http://bits.blogs.nytimes .com/2015/12/23/indian-regulators-suspend-facebooks-free -basic-services/?\_r=0.

Greenstein S, Peitz M, Valletti T (2016) Net neutrality: A fast lane to understanding the trade-offs. J. Econom. Perspectives 30(2): 127–150.

Guo H, Cheng HK, Bandyopadhyay S (2013) Broadband network management and the net neutrality debate. Production Oper. Management 22(3):1287–1298.

Hande P, Chiang M, Calderbank AR, Rangan S (2009) Network pricing and rate allocation with content provider participation. Proc. IEEE Infocom, 990–998.

Hong E (2016) Zero-rating, explained. New York Times (February 8), http://www.slate.com/articles/technology/future\_tense/2016/ 02/why\_activists\_are\_fighting\_facebook\_t\_mobile\_over\_zero \_rating.html.

Hotelling H (1929) Stability in competition. Econom. J. 39(153): 41–57.

Inoue A, Kurosawa T, Takano Y, Iwashita M, Nishimatsu K (2011) Mobile-carrier choice modeling under competitive conditions. 1st ACIS/JNU Internat. Conf. Comput., Networks, Systems, Indust. Engrg. 4CNSI 20115, Jeju Island, South Korea, 164–169.

Kang C (2015) F.C.C. asks Comcast, AT&T and T-Mobile about “zero-rating” services. New York Times (December 17), http:// bits.blogs.nytimes.com/2015/12/17/f-c-c-asks-comcast-att -and-t-mobile-about-zero-rating-services/?\_r=0.

Kastrenakes J (2015) YouTube doesn’t like T-Mobile’s lowquality video scheme. The Verge (December 22), http://www .theverge.com/2015/12/22/10654730youtube-criticizes-tmobile -binge-on-video-quality-throttling.

Knutason R, Gryta T (2014) AT&T to let content companies subsidize users’ data costs. Wall Street Journal (January 6), http:// online.wsj.com/news/articles/SB1000142405270230488710457 9304451794540152.

Kourandi F, Krämer J, Valletti T (2016) Net neutrality, exclusivity contracts, and Internet fragmentation. Inform. Systems Res. Forthcoming.

Krämer J, Wiewiorra L (2012) Network neutrality and congestion sensitive content providers: Implications for content variety, broadband investment, and regulation. Inform. Systems Res. 23(4):1303–1321.

Kravets D (2014) AT&T thumbs nose at net neutrality with “sponsored” bandwidth scheme. Wired (January 6), http://www .wired.com/2014/01/att-sponsored-data/.

Kumparak G (2014) T-Mobile stops counting data used with Spotify, Pandora, and certain other music services. TechCrunch (June 18), http://techcrunch.com/2014/06/18/t-mobile-stops -counting-data-used-with-spotify-pandora-itunes-radio-and -certain-other-music-services/.

Ma RTB (2014) Subsidization competition: Vitalizing the neutral Internet. Proc. 10th ACM Internat. Conf. Emerging Networking Experiments Tech. (ACM, New York), 283–294.

Marcus JS (2011) Network operators and content providers: Who bears the cost? Wissenschaftliches Institut für Infrastruktur und Kommunikationsdienste, Bad Honnef, Germany, http://ssrn.com/abstract=1926768.

Melendez S (2015) T-Mobile “binge on” video streaming program accused of throttling traffic to YouTube. FastCompany (December 23), http://www.fastcompany.com/3054977/fast-feed/t -mobile-binge-on-video-streaming-program-accused-of-throttling -traffic-to-youtube?partner=rss.

Nichols S (2015) Zuck’ed up: Facebook opens up free Internet in India—But bans HTTPS. The Register (May 4), http://www .theregister.co.uk/2015/05/04/internet\_org\_facebook/.

Nicolas C, François M (2007) The convergence between content and access: Internalizing the market complementarity. Rev. Network Econom. 6(2):161–173.

Reardon M (2014) AT&T says “sponsored data” does not violate net neutrality. cnet (January 9), http://www.cnet.com/news/ at-t-says-sponsored-data-does-not-violate-net-neutrality/.

Sharma A, Ante SE, Troianovski A (2013) ESPN eyes subsidizing wireless-data plans. Wall Street Journal (May 9), http://online .wsj.com/news/articles/SB1000142412788732405970457847340 0083982568.

Snider M, Yu R, Brown E (2015) What is net neutrality and what does it mean for me? USA Today (February 27), http://www .usatoday.com/story/tech/2015/02/24/net-neutrality-what-is -it-guide/23237737/.

Troianovski A (2012) Cellphones are eating the family budget. Wall Street Journal (September 28), http://www.wsj.com/articles/ SB10000872396390444083304578018731890309450.

Van Schewick B (2016) T-mobile’s binge on violates key net neutrality principles. Working paper, Stanford University, Stanford, CA. https://cyberlaw.stanford.edu/downloads/van Schewick-2016-Binge-On-Report.pdf.
