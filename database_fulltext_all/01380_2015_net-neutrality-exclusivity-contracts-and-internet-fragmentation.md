---
otero_id: 1380
otero_key: "RF4BUG3T"
title: "Net Neutrality, Exclusivity Contracts, and Internet Fragmentation"
authors: "Frago Kourandi; Jan Krämer; Tommaso Valletti"
year: "2015"
journal: "Information Systems Research"
doi: "10.1287/isre.2015.0567"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [155.198.30.43] On: 09 August 2015, At: 22:51 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/RF4BUG3T/fulltext/images/5578974ca32cd58ad2f54f1781fbdbd0086c16d1192a6586f84e26c74ee6e520.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Net Neutrality, Exclusivity Contracts, and Internet Fragmentation

Frago Kourandi, Jan Krämer, Tommaso Valletti

## To cite this article:

Frago Kourandi, Jan Krämer, Tommaso Valletti (2015) Net Neutrality, Exclusivity Contracts, and Internet Fragmentation. Information Systems Research 26(2):320-338. http://dx.doi.org/10.1287/isre.2015.0567

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2015, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/RF4BUG3T/fulltext/images/4b2d63ff3e7f854cc0460cf45e554f717a4560f4f4d73704f1d95666f49b8702.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Net Neutrality, Exclusivity Contracts, and Internet Fragmentation

Frago Kourandi

Regulatory Authority for Energy, 11854 Athens, Greece; and Athens University of Economics and Business, 10434 Athens, Greece, kourandi@aueb.gr

Jan Krämer University of Passau, 94032 Passau, Germany, jan.kraemer@uni-passau.de

Tommaso Valletti

Business School, Imperial College London, London SW7 2AZ, United Kingdom, t.valletti@imperial.ac.uk

fragmentation. We examine the relationship between NN regulation and Internet fragmentation in a gametheoretic model that considers the interplay between termination fees, exclusivity, and competition between two Internet service providers (ISPs) and between two content providers (CPs). An exclusivity arrangement between an ISP and a CP reduces the CP’s exposure to some end users, but it also reduces competition over ads among the CPs. Fragmentation arises in equilibrium when competition over ads among the CPs is very strong, the CPs’ revenues from advertisements are very low, the content of the CPs is highly complementary, or the termination fees are high. We find that the absence of fragmentation is always beneficial for consumers, because they can enjoy all available content. Policy interventions that prevent fragmentation are thus good for consumers. However, results for total welfare are more mixed. A zero-price rule on traffic termination is neither a sufficient nor a necessary policy instrument to prevent fragmentation. In fact, regulatory interventions may be ineffective or even detrimental to welfare and are only warranted under special circumstances.

Keywords: net neutrality; Internet fragmentation; exclusivity

History: Rahul Telang, Senior Editor; Sabyasachi Mitra, Associate Editor. This paper was received February 4, 2013, and was with the authors 9 months for 2 revisions. Published online in Articles in Advance April 1, 2015.

## 1. Introduction

In the past few years, the debate over net neutrality (NN) has attracted much attention from academia and the public alike. The term NN encompasses several distinct policy issues that are all concerned with how data flows on the Internet should be handled and priced (Krämer et al. 2013). One of the most salient issues of NN regulation is that it seeks to maintain the status quo, whereby content and service providers (CPs) pay once only for access to the Internet (usually to some backbone provider), and not again for the delivery of their traffic to end users at each terminating Internet service provider (ISP). This custom of ISPs not charging termination fees has been coined the zero-price rule (Hemphill 2008, Lee and Wu 2009). However, although the zero-price rule is still the status quo today, several ISPs worldwide, among them AT&T (Bloomberg Business 2005), Telefonica, and Vodafone (Lambert 2010), as well as Deutsche Telekom (Deutsche Welle 2010), have publicly announced that they intend to depart from this custom. This has heated, if not started, the public debate on NN.

Following Lee and Wu (2009), proponents of NN justify the zero-price rule based on the arguments that it (i) is efficient with respect to the economics of two-sided markets, (ii) stimulates innovation and investment in broadband networks as well as content, and (iii) prevents a fragmentation of the Internet. The first two of these arguments have been analyzed extensively in recent academic literature, resulting in a more differentiated view in this regard (for surveys, see Schuett 2010, Faulhaber 2011, Krämer et al. 2013). The conclusion from this research is that the zeroprice rule is in fact only efficient under special circumstances (see, e.g., Economides and Tåg 2012, Guo et al. 2012) and that the effect of NN regulation on innovation and investment is at best ambiguous (see, e.g., van Schewick 2007, Jamison and Hauge 2008, Choi and Kim 2010, Cheng et al. 2011, Economides and Hermalin 2012, Krämer and Wiewiorra 2012, Reggiani and Valletti 2012, Bourreau et al. 2015, Guo and Easley 2014). Interestingly, the third argument, that the zeroprice rule prevents a fragmentation of the Internet, has thus far not been considered in detail. This aspect of the NN debate is important, however, as has recently been highlighted by Neelie Kroes, vice president of the European Commission, who emphasized that Internet fragmentation should be a concern to all Internet stakeholders: “I know there are pressures— regulatory, political and economic—to ‘fragment’ the Internet. 0 0 0 But the Internet’s most important characteristic is its universality: in principle, every node can communicate with every other. This has important implications for innovation, plurality, democratic values, cohesion and economic growth” (Kroes 2011). Moreover, a comprehensive analysis of the effect of a zero-price rule with respect to all three of the abovementioned arguments seems necessary in light of current regulatory developments: several governments throughout the world (e.g., Canada, Japan, France, Germany, the United Kingdom; Carter et al. 2010, Sluijs 2012) are considering whether to adopt a zeroprice rule. The United States, the Netherlands, Chile, and Slovenia have already enacted such NN regulation, which in the United States has been challenged in court.

The link between Internet fragmentation and NN regulation (i.e., a zero-price rule) may not be obvious immediately. It can be traced back to an influential article by Lee and Wu (2009, p. 67), who conjectured that the presence of termination fees “would almost certainly result in service providers ‘competing’ for content, as seen in other platform industries, by charging different fees and bargaining on exclusive arrangements with content providers. In turn, such bilateral agreements would inevitably lead to fragmentation—where certain content would only be available on certain service providers—and hence multiple ‘Internets.’ ” Certainly, this is a daunting hypothesis, which, if true, could be able to tilt the debate in favor of NN regulation. However, this conjecture was never investigated formally, and there are at least two reasons to scrutinize it. First, the authors build their argument on a comparison of the Internet to other platform industries, such as video consoles and credit cards. They thereby neglect that, although the Internet can be seen as a platform industry that connects end users with CPs, it is also very different from the aforementioned industries with respect to how content is financed. On the Internet, content is still predominantly financed through advertisements (Dou 2004, Evans 2009, Anderson 2012), and these advertisement revenues are collected directly by the CPs. This makes the Internet distinct from other platform industries in which content is either paid for directly by end users (as, e.g., in the context of video games and credit cards) and not by advertisements, or in which advertisement revenues are collected by the vertically integrated platform providers (e.g., by TV stations and newspapers) and not by independent CPs.

Second, the proposed link between the presence of termination fees and the existence of exclusive content does not seem to be inevitable. For example, in the mid-1990s, when the zero-price rule was still undisputed, many ISPs, including AOL, Prodigy, and Compuserve, each adopted a so-called walled garden strategy, which relied on exclusive content to attract customers. More recently, especially mobile ISPs seem to compete for customers through exclusive content that is delivered through carrier-specific apps. To be precise, in this context, “exclusive” usually refers only to exclusive mobile access (e.g., via a smartphone) to the content, but does not mean that the content is generally not available through other channels (e.g., fixed networks). Nevertheless, the exclusive content deals are clearly aimed to differentiate the (mobile) ISPs’ networks, and they occur in the absence of a termination fee for CPs. For example, Verizon and the National Football League recently struck an exclusive content deal where certain games can be streamed only on smartphones for Verizon subscribers (CNNMoney 2013). To attain this exclusive content, Verizon pays an exclusivity fee of \$1 billion over the course of four years. Similarly, in the past Verizon customers received exclusive mobile access to content of Microsoft (Los Angeles Times 2010) and ESPN (Verizon 2007). Other mobile ISPs have made similar exclusivity arrangements. These include AT&T with Electronic Arts (AT&T 2008) and Zynga (Bloomberg Business 2011), Vodafone with Eidos (PRNewswire 2003), and Deutsche Telekom with Bild, Germany’s largest tabloid newspaper (Nehl and Parplies 2002). Hence, although the extent of exclusive content on the Internet is still rather limited (which is in line with the intuition that the current status quo of zero termination fees inhibits Internet fragmentation), it is not obvious that a zeroprice rule can prevent Internet fragmentation.

Thus, it is interesting to study the precise interaction between the zero-price rule and Internet fragmentation. In this paper, we propose a game-theoretic model to formally address this issue. The model takes into account the specifics of the Internet industry and considers the interplay between termination fees (i.e., a departure of the zero-price rule where fees are paid by the CPs to the terminating ISPs), exclusivity arrangements, and competition between ISPs and CPs, respectively. In this context, we also consider various externalities (such as complementarity and substitutability of content) that were not previously considered in the literature on NN. In this vein, we can offer a more fine-grained view on whether and when termination fees in fact raise the danger of Internet fragmentation, and what their impacts are on the

ISPs’ and CPs’ profits as well as on welfare. Moreover, we consider the impact of a no-exclusivity rule, which forbids ISPs and CPs to strike a deal on the exclusivity of content, as an alternative to the zero-price rule. The no-exclusivity rule, which is easy to implement and enforce by policy makers, may address the problem of Internet fragmentation more directly. A similar rule has been proposed to the TV broadcasting market in the United Kingdom, for example. However, this was justified on the grounds of antitrust concerns, and not by fear of fragmentation (Weeds 2015).

In particular, we consider competition between two access ISPs, which connect Internet users to CPs. Internet users prefer the ISP that offers more (or more valuable) content. In reverse, CPs make money through online advertisements and therefore prefer to be seen by many users. Hence, there are cross-side network effects that characterize a two-sided market (Armstrong 2006, Rochet and Tirole 2006). If exclusivity arrangements are allowed, each ISP can bargain with a CP for the terms under which it is visible exclusively to the ISP’s customers. Generally, the CP must trade off two effects when considering whether to accept such an exclusivity arrangement. On one hand, exclusivity may result in a loss of exposure, thereby diminishing the CP’s ad revenues. On the other hand, CPs are in competition for Internet users’ “clicks,” and thus, by means of exclusivity agreements, CPs may benefit from reduced competition. In addition, the ISP may choose to compensate the CP for agreeing to be exclusive to the ISP. This is especially true for highly valued content, which will in turn raise the relative attractiveness of the ISP and induce customers to sign contracts with it.

Our results highlight that Internet fragmentation (i.e., exclusivity of content) can also occur in the presence of a zero-price rule. This holds true even if ISPs are not allowed to financially compensate the CP for a loss in exposure (i.e., when the exclusivity fees are also restricted to be zero). In a nutshell, a zero-price rule, as suggested by Lee and Wu (2009), is neither a necessary nor sufficient condition to prevent Internet fragmentation. Hence, our finding is in line with the empirical evidence described above. However, everything else equal, we also confirm that Internet fragmentation does become more likely with the introduction of termination fees. The reason is simply that termination fees accrue at each ISP where the CP is visible, and thus they affect the CP’s outside option in favor of accepting exclusivity. However, the conditions under which fragmentation occurs are more subtle and sometimes counterintuitive, and even in the presence of termination fees, fragmentation is not the inevitable outcome.

First, we note that there are various degrees of fragmentation that must be differentiated. Fragmentation, if it occurs, can either be partial, i.e., only a subset of the CPs is available exclusively at some ISP, or full, i.e., each CP is available at exactly one ISP only. Full fragmentation is the likely outcome when (i) competition over ads among the CPs is very strong or (ii) the CPs’ revenues from advertisements are very low (i.e., there are only weak network effects for consumers on the CP side), (iii) the online content of the CPs is highly complementary, or (iv) the termination fees are high. When CPs compete fiercely for customers’ clicks (case i), full fragmentation becomes more likely, because it offers the CP a means to collectively evade this competitive pressure, although, unilaterally, exclusivity can harm a CP. Likewise, if the CPs’ ability to make money through advertisements is limited (case ii), they prefer to strike an exclusivity deal. If, however, Internet users consider the CPs’ content as highly complementary on the consumer side, then it is more likely that there is a Nash equilibrium wherein each ISP seeks to have an exclusive deal with a CP: if a rival ISP has agreed exclusivity with a CP, then the other ISP will want to do the same with the remaining CP, because otherwise the complementarity would benefit only the rival (case iii). Finally, when the termination fees paid to each ISP are high enough, it becomes more expensive for the CPs to deliver their content to both ISPs (case iv). On the contrary, if some of the above conditions are not met, either partial or no fragmentation is the likely outcome. In particular, fragmentation does not occur if competition over ads among the CPs is weak and CPs’ revenues from ads are high.

Concerning welfare, we find that consumer surplus is always highest under no fragmentation. Since the joint value of both contents is at least as high as the value of each content solely, this result arises because competition between ISPs does not allow them to raise the subscription fees too much to reflect the increase in content. However, with respect to total welfare, which also incorporates the ISPs’ and CPs’ revenues, no fragmentation is the efficient outcome only when ad competition among CPs is rather weak. If ad competition between CPs is strong, then exclusivity provides a means to avoid this competitive pressure and to increase CPs’ profits, which can render full fragmentation the efficient outcome with respect to total welfare. Thus, if policy makers want to ensure no fragmentation (e.g., because they value consumer surplus more, or because they believe that competition over ads among the CPs is rather weak), then a simple no-exclusivity rule is a wellsuited instrument. By contrast, as noted above, a zeroprice rule cannot prevent Internet fragmentation. In all other cases, NN or any other regulation is at best superfluous, because it cannot improve on the equilibrium outcome without NN regulation. In fact, such regulation can be harmful, in the sense that the equilibrium is shifted away from the first best. Thus, after all, NN regulation in the form of a zero-price rule does not seem to be the appropriate policy instrument to prevent Internet fragmentation.

The remainder of this article is organized as follows. In §2, we relate our framework and findings to the extant literature. Section 3 sets up the model. Section 4 derives the equilibrium with termination and exclusivity fees and discusses the properties of the equilibrium outcome. Section 5 examines different approaches with respect to NN regulation, and policy implications are discussed in §6. Finally, in §7 we present and discuss extensions and limitations of our base model before we conclude in §8.

## 2. Related Literature

The present paper relates both to the literature on NN and the literature on exclusive dealing. The economic research on NN is reviewed by Schuett (2010), Faulhaber (2011), and Krämer et al. (2013). These reviews highlight that deviations from NN can occur either with respect to the zero-price rule (e.g., demanding a termination fee from each CP that is accessible through the ISP’s network) or with respect to the socalled no-discrimination rule (e.g., blocking of content or degrading traffic flows by nonintegrated CPs), or both (e.g., pay-for-priority arrangements between ISP and CP). In this paper, we only consider NN as a zero-price rule for two reasons: First, the aim of this paper is to analyze the relationship between termination fees (i.e., the zero-price rule) and Internet fragmentation. To focus on this issue, we deliberately abstract from additional issues that may arise due to network congestion management (e.g., Guo et al. 2013) or due to competition of vertically integrated ISPs with independent CPs (e.g., Guo et al. 2010). In this context, also note that exclusive content, that we consider here, is not comparable to network management practices such as blocking content, because blocking is the result of a unilateral action by the ISP and not, as here, the outcome of a bilateral, voluntary agreement between the ISP and CP. Second, our focus on the zero-price rule is in line with the majority of economic papers on NN (e.g., Jamison and Hauge 2008, Choi and Kim 2010, Cheng et al. 2011, Economides and Hermalin 2012, Economides and Tåg 2012, Guo et al. 2012, Krämer and Wiewiorra 2012, Reggiani and Valletti 2012, Bourreau et al. 2015, Choi et al. 2015, Guo and Easley 2014). These papers have addressed important policy questions, ranging from the effect of a zero-price rule on CPs’ surplus (e.g., Jamison and Hauge 2008, Economides and Tåg 2012), on broadband investment (e.g., Choi and Kim 2010, Cheng et al. 2011, Krämer and Wiewiorra

2012), on content innovation (e.g., Hermalin and Katz 2007, Guo et al. 2012), on end user surplus, and on coverage of the consumer market (e.g., Krämer and Wiewiorra 2012, Guo and Easley 2014) to that on competition between ISPs (e.g., Economides and Tåg 2012, Reggiani and Valletti 2012, Njoroge et al. 2013, Bourreau et al. 2015, Choi et al. 2015). In summary, the previous economic literature suggests that a deviation from the zero-price rule may generally benefit welfare (i.e., consumer surplus or total surplus), although most papers also identify particular scenarios under which NN is welfare superior (for a review, see Krämer et al. 2013). In particular, by the logic of a two-sided market, consumer surplus has a tendency to be higher when deviating from NN because the ISP is likely to lower end users’ subscription fees when charging termination fees from CPs. Also, total surplus tends to be higher without NN, because the ISP can use its increased pricing flexibility to incentivize more efficient utilization of the network. However, none of these papers considers the effect of the zeroprice rule on Internet fragmentation, and, as we will show, the zero-price rule has a different effect on welfare here. On one hand, because consumers prefer a nonfragmented Internet and the zero-price rule hinders Internet fragmentation, it generally benefits consumer surplus. On the other hand, the zero-price rule restricts the contractual flexibility of ISPs and CPs, which can negatively affect total surplus, especially in the presence of strong competition among CPs. Overall, we thus find mixed evidence on the effect of the zero-price rule on welfare. At the same time, we can show that NN regulation is neither a necessary nor a sufficient policy instrument to improve welfare in the context of Internet fragmentation.

Our paper also relates to the literature on exclusive dealing, which, however, is primarily concerned with the conditions under which exclusive content emerges in the broadcasting and media industry (e.g., Armstrong 1999, Dukes and Gal-Or 2003, Peitz and Valletti 2008, D’Annunzio and Russo 2013, Weeds 2015). The paper from this stream of literature that is most similar to ours is Hagiu and Lee (2011). The authors also consider competition between platforms that can beforehand offer exclusivity contracts to CPs. However, their model setup differs in some key aspects to ours, as the authors clearly have other platform industries in mind (such as the video games industry), where consumers pay for content directly. The main differences are thus that Hagiu and Lee (2011): (1) do not consider ad-financed CPs, who cannot control the pricing of their content directly; (2) do not consider termination fees; and (3) do not consider that CPs are in competition with each other (for ads, in our model). These differences in assumptions also drive important differences in the results. For example, Hagiu and Lee (2011) find that either no or full fragmentation occurs in equilibrium. In their setting, unlike ours, partial fragmentation is not an equilibrium outcome. Moreover, because the focus of their paper is different, Hagiu and Lee (2011) study the conditions under which fragmentation occurs and do not address the policy questions that we are concerned with here. Thus, to the best of our knowledge, our paper is the first that formally considers the relationship between termination fees and exclusive contracting in the context of the NN debate.

## 3. A Model of Competing ISPs and CPs

We consider a scenario in which end users have the choice between two ISPs through which they can access content and services on the Internet. For expositional clarity, we assume that there exist exactly two CPs on the Internet to which all end users wish to have access. Of course, although the Internet is made up of a magnitude of CPs in reality, a subset of which creates some positive utility, this simplified structure of two CPs allows us to best study the role of NN regulation on the competition between CPs and ISPs. To obtain more general results, we make no particular assumption on the nature of the content and allow for every feasible economic relationship between the two contents, i.e., they may be perceived as complementary, substitutable, or independent by the end users. We assume that CPs provide content free of charge to the end users via the broadband networks of the ISPs and derive revenues from advertising on their websites. This is the prevalent business model on the Internet (Dou 2004, Evans 2009, Anderson 2012) and has therefore also been the dominant modeling assumption in previous literature (e.g., Choi and Kim 2010, Cheng et al. 2011, Guo et al. 2012, Krämer and Wiewiorra 2012, Reggiani and Valletti 2012, Bourreau et al. 2015).

Absent NN regulation, i.e., when no zero-price rule is in effect, an ISP may charge a positive termination fee for sending the CPs’ content to its customers. Moreover, each CP and ISP may strike an exclusivity deal under which the CP’s content is available exclusively at the ISP. Internet fragmentation is said to occur whenever some content is not delivered by all ISPs and, consequently, not to all end users. Partial fragmentation occurs if only one of the two CPs strikes an exclusivity deal, whereas full fragmentation is said to occur when each CP is mutually exclusive at one ISP. The details of the model follow.

## 3.1. End Users

There is a unit mass of heterogeneous end users that have a natural preference for one of the two ISPs.

Users’ preference for the ISPs is denoted by $z$ and assumed to be uniformly distributed between zero and one (Hotelling 1929). The two ISPs (denoted by $i \in \{ A , B \} )$ are horizontally differentiated and located at either end of the users’ preference spectrum, i.e., ISP A at $z = 0$ and ISP B at $z = 1$ (for a similar setup, see, e.g., Economides and Tåg 2012, Bourreau et al. 2015, Choi et al. 2015). Thus, a type z consumer derives utility $U _ { z } = b + u _ { A } - p _ { A } - t z .$ 1 when he subscribes to ISP $A ,$ whereas he obtains utility of $U _ { z } = b +$ $u _ { B } - p _ { B } - t ( 1 - z )$ when he subscribes to ISP B. Therefore, b denotes the base utility from being connected to the Internet, $u _ { i }$ denotes the utility of the content that is available at ISP $i ,$ and $p _ { i }$ is the subscription fee. Moreover, t measures the degree of competition between the two ISPs. When t is large, the users’ preferences for the ISPs becomes more important, such that competition on the basis of $u _ { i }$ and $p _ { i }$ becomes weaker. End users will choose the ISP that gives them the highest utility. We denote the end user demand for ISP i by $D _ { i } . ^ { 1 }$ Furthermore, we assume that b is large enough, such that the market is fully covered, i.e., $D _ { A } + D _ { B } = 1$

## 3.2. Content Providers

There are two competing and differentiated CPs (denoted by $j \in \{ 1 , 2 \} )$ that derive revenues from advertising and may have to pay fixed termination fees to the ISPs via which they deliver their content to the end users. Without loss of generality, let CP 1 offer content that is valued weakly more by the end users $( u _ { 1 } \geq u _ { 2 } )$ when consumed on its own. Although the content of CP 1 is weakly more valuable to consumers, this does not imply that CP 1 faces higher marginal costs than CP 2. CPs provide information goods, which are characterized by large fixed costs and zero marginal costs. When both contents are available to the end user, the utility of the joint consumption of both CPs’ content is denoted as $u _ { 1 2 } .$ . It is reasonable to assume that there exists no disutility from the availability of more content, i.e., $u _ { 1 2 } \geq u _ { 1 }$ . Therefore, both contents jointly do not reduce the value of any one content alone. Notice that $u _ { 1 2 }$ denotes the level of complementarity/substitutability of the CPs content. As $u _ { 1 2 }$ increases, everything else being equal, the contents of CP 1 and CP 2 become more complementary. Also note that $u _ { A } , u _ { B } \in \left\{ u _ { 1 2 } , u _ { 1 } , u _ { 2 } \right\}$ depending on the content that each ISP offers.

Following the current concerns of the policy debate outlined in §1, we introduce two types of lump-sum fees that might be exchanged between the ISPs and CPs. The first is the termination fee $f ,$ paid by a CP to the ISP for delivering its content to the end users. This fee $f$ is constant, the same across the ISPs and the CPs, and is exogenously set, for example, by a regulator. Consequently, $f = 0$ corresponds to the zeroprice rule. Second, we also study an exclusivity fee $e _ { i j } , \quad$ which is paid by CP j when it delivers its content exclusively to ISP i. As will be described later, $e _ { i j }$ is endogenously determined via a negotiation between the ISPs and the CPs. It may thus be positive or negative. This means that the ISP may either pay the CP to be exclusive to its network or be paid to grant the CP exclusivity. Each CP may choose to be available at a single ISP (and pay the termination fee plus the exclusivity fee) or at both ISPs (and pay only the termination fee, but at each ISP); that is, we allow the CPs to single home or to multihome. In particular, this means that when CPs do not have to pay termination fees $( f = 0 )$ , which is the current status quo, then the content of both CPs will generally be available at both ISPs, unless a CP deliberately chooses to make its content available exclusively. If a CP agrees to be exclusive with ISP i, then it can only be accessed by the end users connected to that ISP.<sup>2</sup>

CPs receive advertising revenues depending on the exposure to end users and depending on the level of competition over ads among the two $\mathsf { \check { C } P s } . ^ { 3 }$ Thus, a CP that is available at both ISPs receives an exposure of $D _ { A } + D _ { B } = 1$ . Similarly, a CP that is available only at one ISP, say i, will inevitably have a reduced exposure of $D _ { i } < 1$

When the CP competes for customers’ clicks with the other CP, the CPs receive a “standard” advertisement rate of r. However, if a CP is the only CP available to the end users at some ISP, it is assumed that this CP can demand a higher advertising rate (ar, with $a > 1 )$ . In other words, we are particularly interested in how the level of ad competition between CPs affects Internet fragmentation: when only one CP is available at an ISP, it is natural to assume that the CP will be able to command higher revenues from advertising compared to the situation where the CP has to share the end users’ attention with another

CP at the same ISP. There are several ways to motivate this assumption. For example, think of end users that consume Internet services for a limited period of time: when there are multiple contents offered by the platform they connect to, they may not visit all available content. This implies that, in the presence of more CPs at any given ISP i, each CP effectively receives less than D visits, whereas it would have received $D _ { i }$ visits if it were the only CP at ISP i. Consequently, the advertisement rate it can demand from advertisers is lower. Similarly, CPs may be literally substitutable, meaning that end users visit one specific content (e.g., one search engine) and not all available content, something that affects the effectiveness of advertising and the revenues associated with it (see Athey et al. 2013). But also if CPs are complementary and users are not time constrained, such that all end users connected to a given ISP will visit all available $\mathrm { C P s , }$ there is likely a differentiation in advertisement rates. For example, assume that the advertisers’ marginal valuation for an ad impression decreases with the number of impressions as in D’Annunzio and Russo (2013). Say the first impression is worth $r _ { 1 } ,$ whereas subsequent impressions of the same ad are worth only r, with $r _ { 1 } = a r > r$ . Consequently, if a CP is the only outlet for ads at a given ISP, it can demand an advertisement rate of $r _ { 1 } .$ . By contrast, if there are two CPs associated with an ISP, then advertisers have the choice to buy ad space from both CPs or from only one of the CPs. Because each CP will be visited equally often by the same end users, the advertiser will buy ad space from only one CP (say randomly) if CPs ask for more than r. This will drive the advertisement rate down to $r ,$ as any higher advertisement rate could be profitably undercut by the rival CP.

Although we fall short of providing a fully specified game of competition between CPs, our reducedform approach is an advancement with respect to the extant literature and allows us to study various types of competition scenarios, as exemplified above. A CP can be sure that end users on a platform will watch only its own content when this content is the only content delivered in that platform, and thus the advertising rate will be $r _ { 1 } = a r$ . If instead a CP has to share the end users’ attention with another CP on the same platform, the advertising rate will be reduced. The parameter a reflects this type of competitive pressure: the higher a is, the stronger the competition for clicks.<sup>4</sup> Moreover, notice that a can possibly take on any value between one and infinity. To see this, notice that $a = r _ { 1 } / r$ goes to infinity when the value of the second impression of an ad goes to zero in the example above.

In summary, depending on the exclusivity of content, the profit of ${ \dot { \mathrm { C P } } } ~ j$ is given by

$$
\Pi_ {\mathrm{CP} _ {j}} = \left\{ \begin{array}{l l} r - 2 f & \text { if   both   CPs   nonexclusive, } \\ a r D _ {i} + r D _ {- i} & \text { if   CP   j   nonexclusive   and } \\ - 2 f & \text { CP   -j   exclusive   at   ISP   -i, } \\ r D _ {i} - f - e _ {i j} & \text { if   CP   j   exclusive   at   ISP   i   and } \\ & \text { CP   -j   nonexclusive, } \\ a r D _ {i} - f - e _ {i j} & \text { if   CP   j   exclusive   at   ISP   i   and } \\ & \text { CP   -j   exclusive   at   ISP   -i; } \end{array} \right.
$$

−i and $- j$ denote the index of the other ISP and CP, respectively. Moreover, note that the exposure $D _ { i }$ differs among the four cases.

## 3.3. Internet Service Providers The profit function of ISP i is

$$
\Pi_ {\mathrm{ISP} _ {i}} = \left\{ \begin{array}{l l} p _ {i} D _ {i} + 2 f, & \text { if   both   CPs   nonexclusive }, \\ p _ {i} D _ {i} + f, & \text { if   CP   } j \text {   nonexclusive   and   CP   } - j \text {   exclusive   at   ISP   } - i, \\ p _ {i} D _ {i} + 2 f + e _ {i j}, & \text { if   CP   } j \text {   exclusive   at   ISP   } i \text {   and   CP   } - j \text {   nonexclusive }, \\ p _ {i} D _ {i} + f + e _ {i j}, & \text { if   CP   } j \text {   exclusive   at   ISP   } i \text {   and   CP   } - j \text {   exclusive   at   ISP   } - i. \end{array} \right.\tag{1}
$$

Notice that the cases correspond to no, partial, and full Internet fragmentation, respectively.

## 3.4. Structure and Timing

We consider the following three-stage game:

1. The ISPs simultaneously make take-it-or-leave-it exclusivity offers to $\mathrm { C P } 1 , e _ { i 1 } . \mathrm { C P } \overset { \cdot } { _ { \cdot } }$ 1 accepts one of the two offers or rejects both, in which case it delivers its content to both ISPs.<sup>5</sup>

2. (a) If there was no exclusivity reached in the first stage, the ISPs simultaneously make take-it-or-leave-it exclusivity offers to CP $2 , e _ { i 2 } ,$ and CP 2 either accepts one of the two offers or rejects both and delivers its content to both ISPs.

(b) Otherwise, if ISP −i has agreed with CP 1 on an exclusivity contract, it cannot offer an exclusivity contract to $\dot { \mathrm { C P } } 2$ as well. Thus, only ISP i can make an exclusivity offer to CP 2. CP 2 either accepts this offer or rejects it and delivers its content to both ISPs.<sup>6</sup>

3. The ISPs simultaneously announce the subscription fees $p _ { A } , \ p _ { B } ,$ and the end users, who are aware about which CP is available at each ISP, choose which ISP to subscribe to.

Under NN regulation, the game is modified in one of the following three ways. First, NN regulation can impose a zero-price rule, which restricts the termination fee to zero. This is the standard notion of NN regulation that is currently discussed in the policy debate. Second, regulators may also wish to adopt a stricter form of the zero-price rule that restricts all fees that might be exchanged between ISPs and CPs to zero (i.e., the termination fees and the exclusivity fees). Third, and alternatively, NN regulation could impose a straightforward no-exclusivity rule that forbids any exclusivity arrangements between ISPs and CPs. These cases are presented in §5.

The base model outlined above establishes the minimal set of interactions necessary to drive our results. Evidently, the actual interaction between ISPs and CPs may be more complex. In the online appendix (available as supplemental material at http://dx.doi .org/10.1287/isre.2015.0567) we therefore study several variants and extensions of the above three-stage game, which show that our main insights derived from this game are robust. In Online Appendix D we allow ISPs to make exclusivity offers to both CPs simultaneously. In Online Appendix F we study an extended game where CPs determine the quality of their content endogenously at an initial stage. Similarly, in Online Appendix G we consider a game where ISPs determine the termination fee endogenously. Finally, in Online Appendix H we modify the last stage of the game in that we allow consumers to subscribe to both ISPs (multihoming). We discuss these extensions in more detail in §7.

## 4. Without NN Regulation

Without NN regulation, exclusivity contracts and positive termination fees are both feasible. Recall that the ISPs make exclusivity offers first to the more efficient CP, i.e., CP 1, which generates more value in the network, and then to the less efficient CP 2. The two ISPs, however, are symmetric such that it is in most cases not necessary to distinguish between them. Thus, there are four potential subgames that should be considered (see Figure 1). These can be denoted by a tuple 4x1 y5, where $x , y \in \{ E , N E \}$ means that CP 1 (x) and CP 2 (y) are exclusive (E) or not exclusive (NE) with any of the two ISPs, respectively. When both CPs sign an exclusivity contract, full fragmentation emerges, $( E , E ) , ^ { 7 }$ whereas when a single

Figure 1 Potential Subgames  
![](/api/attachments/RF4BUG3T/fulltext/images/e1119340659d3032347234ce8693d050d5011afc8972eb027e0bb00fa25e557c.jpg)

CP signs an exclusivity contract, partial fragmentation emerges, either 4E1 NE5 or $( N E , E ) . ^ { 8 }$ Finally, when both CPs deliver their content to both ISPs, there is no fragmentation, i.e., 4NE1 NE5.

We proceed backward to solve for the subgame perfect equilibrium.

## 4.1. Stage 3: Subscription Fees and End Users’ Decisions

At the third stage, each consumer chooses whether to subscribe to ISP A or ISP B. The consumer that is indifferent between the two ISPs, denoted by z˜, is derived by equating $b + u _ { A } - p _ { A } - t \tilde { z } = b + u _ { B } - p _ { B } -$ t41 − z5˜ , which yields

$$
\tilde {z} (u _ {A}, u _ {B}, p _ {A}, p _ {B}) = \frac {1}{2} + \frac {u _ {A} - u _ {B}}{2 t} + \frac {p _ {B} - p _ {A}}{2 t}.\tag{2}
$$

The end users’ demands for ISP A and ISP B are thus $D _ { A } = \tilde { z }$ and $D _ { B } = 1 - \tilde { z } ,$ respectively. The two ISPs compete by setting a subscription fee to the end users. ISP i maximizes (1) with respect to $p _ { i }$ . Because f and $e _ { i j }$ are fixed fees, the first-order conditions give the equilibrium subscription fees

$$
p _ {A} = t + \frac {u _ {A} - u _ {B}}{3}, \qquad p _ {B} = t + \frac {u _ {B} - u _ {A}}{3}.\tag{3}
$$

Replacing for $p _ { A }$ and $p _ { B }$ into (2), we obtain for the equilibrium demand of the ISPs

$$
D _ {A} = 1 - D _ {B} = \frac {1}{2} + \frac {u _ {A} - u _ {B}}{6 t},\tag{4}
$$

which is exactly $\frac { 1 } { 2 }$ in case the same content is available at both ISPs. Otherwise, the ISP with the more valuable content receives a higher market share than the rival.

To focus on the interesting case where each ISP receives positive demand, we need that $- 3 t < u _ { i } -$ u $_ - i < 3 t .$ . A sufficient condition that satisfies this, and that we assume throughout the paper, is

$$
t > \frac {u _ {1 2} - u _ {2}}{3}.\tag{5}
$$

## 4.2. Stage 2: Exclusivity Offered to CP 2

In this stage, there are two different types of subgames, depending on whether CP 1 has accepted exclusivity (cases 4E1 · 5) or not (cases 4NE1 · 5).

Although we relegate all of the details to Online Appendix A, we now sketch how the game develops. Consider first the case where, in Stage 1, CP 1 has agreed on exclusivity with ISP −i. In this case, at Stage 2, it is the ISP i that can respond by offering exclusivity to CP 2 (this corresponds to the left branch of Figure 1). Since exclusivity fees are lump sums, exclusivity will arise if and only if the joint profits of CP 2 and ISP i are higher under exclusivity than without it. There are two conflicting effects at play here. On one hand, when exclusivity is chosen, ISP i gets a larger market share and can compensate CP 2 for agreeing to exclusivity. On the other hand, the CP that delivers its content to a single ISP exclusively inevitably loses some exposure. The value to CP 2 from exposure, however, depends on the intensity of competition over ads between the CPs. We find that when ad competition is high $( \mathrm { i } . \mathrm { e } . , a > \hat { a } )$ , the first effect dominates the second effect, and, thus, full fragmentation arises in equilibrium. Exclusivity prevails as CPs’ competition is intense, and thus the benefit from exposure is low, which also means that CP 2 may end up paying a rather substantial exclusivity fee.

Fragmentation can also arise for weak competition over ads among the CPs $( a \leq \hat { a } )$ , as long as the advertisement rate is generally low $( r < \hat { r } )$ . The reason for exclusivity is now different, however. Take, for example, the extreme case where r approaches zero. It is then cheap for ISP i to attract exclusively CP 2, because the latter has not much advertising revenues to lose anyway, although the ISP can increase its own market share. Instead, when competition over ads among the CPs is weak $( a \leq \hat { a } )$ and the advertisement rate is high $( r \geq { \hat { r } } )$ , it would be very costly to convince CP 2 to agree on exclusivity. Therefore, in this parameter range, ISP i does not offer exclusivity to CP 2.

The remaining cases are those in which no exclusivity has been reached at Stage 1 between CP 1 and any ISP (right branch of Figure 1). Now, there is competition between the two ISPs for CP 2; either one ISP achieves an exclusive arrangement with CP 2 or the content of CP 2 is delivered to both platforms. This bidding game obviously goes to the advantage of CP 2 and stops when each ISP is just indifferent between winning and losing to the rival the content delivered by CP 2. In particular, exclusivity arises as long as $r < { \bar { r } } .$ Again, in the presence of a high advertisement rate $( r \geq { \bar { r } } ) .$ , exclusivity is not offered to CP 2 by any of the two ISPs, because it would be too costly to compensate $\mathrm { C P } \ 2$ for its loss in exposure.

## 4.3. Stage 1: Exclusivity Offered to CP 1

At the first stage of the game, the reasoning is similar, with the additional feature that CP 1 and the ISPs anticipate the decisions in the second stage. Exclusivity with CP 1 will arise if and only if the joint profits of CP 1 and ISP i are higher under exclusivity than without it. CP 1 will be offered an exclusivity contract, which it accepts either when the ad competition between CPs is very strong $( a \geq \hat { a } )$ or when ad competition between CPs is weak $( a < \hat { a } )$ and the advertisement rate is rather low. Whereas for $a \geq { \hat { a } } ,$ full fragmentation is the inevitable equilibrium outcome $( \mathrm { i . e . , } ( E , E ) )$ , for $a < { \hat { a } } ,$ either full $\bar { ( } ( E , E ) )$ , partial (4E1 NE5, or 4NE1 E5) or no fragmentation (4NE1 NE5) may arise in equilibrium, depending on the level of r. The equilibrium outcome is summarized by the following proposition. The details of the proof are in Online Appendix A.

<sup>Proposition</sup> <sup>1.</sup> Full Internet fragmentation emerges in equilibrium either when ad competition between CPs is relatively high $( a \geq \hat { a } ) .$ , or when ad competition between CPs is relatively low $( a < \hat { a } )$ and the advertisement rate on the Internet is low $\left( r < { \hat { r } } ( a ) \right)$ . When ad competition between CPs is relatively low $( a < \hat { a } )$ and the advertisement rate takes intermediate values $( { \hat { r } } ( a ) < r < { \tilde { r } } ) .$ , partial Internet fragmentation occurs. On the contrary, no Internet fragmentation occurs when ad competition between CPs is relatively low $( a < \hat { a } )$ and the advertisement rate is high $( r \geq \operatorname* { m a x } \{ \tilde { r } , \hat { r } ( a ) \} )$

The relevant thresholds are as follows:

$$
\hat {a} = (u _ {1 2} - u _ {2} + 3 t) / (u _ {1 2} - u _ {1});\tag{6}
$$

$$
\hat {r} (a) = \left(f + \frac {u _ {1 2} - u _ {1}}{3} + \frac {(u _ {1} - u _ {2}) ^ {2}}{1 8 t} - \frac {(u _ {1 2} - u _ {2}) ^ {2}}{1 8 t}\right) /
$$

$$
\left(\frac {3 t + u _ {1 2} - u _ {2} - a (u _ {1 2} - u _ {1})}{6 t}\right);\tag{7}
$$

$$
\tilde {r} = \left(\frac {(3 t + u _ {1 2} - u _ {2}) ^ {2}}{1 8 t} - \frac {t}{2} + f\right) / \left(\frac {3 t - (u _ {1 2} - u _ {2})}{6 t}\right).\tag{8}
$$

Before providing the intuition for this result, we first present a numerical example to illustrate the equilibrium outcome. Figure 2 shows the thresholds for the various fragmentation cases and the resulting equilibrium regions in the 4a1 r 5 space.<sup>9</sup> When a is high enough, full fragmentation always occurs. Full fragmentation also emerges for low values of a and r: in the area to the left of the dashed vertical line, both exclusivity fees become negative; i.e., ISPs pay the CPs to obtain exclusivity. The exclusivity fee paid by the less efficient CP becomes positive faster with the increase in a than the exclusivity fee paid by the more efficient CP.

Figure 2 Equilibrium Outcome for t = 1, u = 3, u = 2, u = 1, f = 0  
![](/api/attachments/RF4BUG3T/fulltext/images/a752813a1c406db12fada3dbd74baf3c8fd9309e2277cfb704c50b1e30661cda.jpg)

For relatively low values of a and intermediate values of $r ,$ partial fragmentation is the equilibrium outcome. Finally, when r is high enough but a is not too high, CPs deliver their content to both ISPs and serve all end users.

We now provide further intuition for the three types of equilibria that emerge from Proposition 1.

4.3.1. Full Fragmentation. In our three-stage game, full Internet fragmentation emerges in equilibrium either when a is relatively high or when both a and r are relatively low. For relatively high $a ,$ competition for ads between the CPs is strong enough; thus, a way to relax this competition is to collectively opt for exclusivity at each platform. Note, however, that a CP cannot unilaterally evade competition by choosing exclusivity: say CP 1 and ISP A strike an exclusive deal, but CP 2 multihomes. Then CP 2 (and not CP 1) is going to benefit from reduced competition, because it is the only CP available at ISP $B ,$ whereas CP 1 continues to face competition by CP 2 at ISP A. Hence, the CPs can only evade competition if they both strike an exclusive deal with a different ISP, i.e., under full fragmentation. Also note that competition between CPs can be so intense, and thus the CPs’ benefits under full fragmentation so large, that for relatively high values of a and $r ,$ both exclusivity fees are positive (i.e., CPs should pay these fees to the ISPs). But as a and r become smaller, competition between ISPs becomes the driver for full Internet fragmentation. Advertising revenues are not too important, and each ISP is fighting with its rival for an exclusivity contract, to boost the demand they obtain and, therefore, their revenues via the subscription fees. The exclusivity fee paid by the more efficient CP 1 is lower than the exclusivity fee paid by $\mathrm { C P } 2 ( e _ { i 1 } < e _ { i 2 } ) .$ , because CP 1 can leverage its content, which is more valuable to the end users. In this context, it is important to mention that the absolute size of the exclusivity fee generally depends on the relative bargaining power between ISPs and CPs, which we do not study in detail. However, also note that whether exclusivity emerges in equilibrium depends only on the comparison of the joint profits of the ISP and CP in each scenario. Hence, the fragmentation equilibrium is independent of the relative bargaining power, i.e., how the additional surplus from exclusivity is divided among the ISP and CP.

4.3.2. Partial Fragmentation. For intermediate values of the advertising rate r and $a < { \hat { a } } ,$ partial fragmentation is obtained in equilibrium. Depending on the parameter values, both types of partial fragmentation may emerge in equilibrium, i.e., with exclusivity obtained by the more efficient CP 1, 4E1 NE5, or with the less efficient CP 2, 4NE1 E5. In both cases the CP that delivers its content exclusively to a single ISP obtains a slotting fee, whereas the rival CP delivers its content to both ISPs. The reason for this richness of partial fragmentation equilibria stems from the possible different best replies by CP 2 in the continuation game. When r is high enough,<sup>10</sup> it is a dominant strategy for CP 2 always not to be exclusive in the continuation game. Hence, in the first stage, CP 1 goes for exclusivity with ISP i only when it can be compensated enough for the loss of exposure at the other ISP −i. This indeed happens as long as $r < { \tilde { r } } ,$ yielding 4E1 NE5. When instead r is low, in the ensuing game there is no dominant strategy for CP 2: if CP 1 achieves exclusivity, then CP 2 will not, whereas if CP 1 does not, then CP 2 will. In this region, therefore, CP 1 has to take into account also the additional possibility that by not accepting exclusivity, it will induce CP 2 to achieve exclusivity at some ISP $i ,$ which actually can benefit CP 1 because it will achieve higher revenues at ISP −i: this opens the room for a 4NE1 E5 equilibrium when a is sufficiently high.

4.3.3. No Fragmentation. For relatively high values of the advertising rate r and $a < { \hat { a } } ,$ no fragmentation occurs. All content is available to both platforms and, thus, to all end users. In this area, it is a dominant strategy for $\mathrm { C P } \ 2$ to never accept exclusivity at the second stage. Anticipating this, CP 1 also has no incentive to get exclusivity in the first stage since the advertising rate r is high enough. CPs prefer to obtain revenues via advertising at both platforms than via exclusivity fees.

From (4), we also obtain that the number of the end users subscribed to the ISP with more content $( \mathrm { i . e . , }$ with $u _ { 1 2 } )$ or with the more valuable content $\left( u _ { 1 } \right)$ is higher than the number of end users subscribed to the ISP with less content (either $u _ { 1 }$ or u ) or the less valuable content $\left( u _ { 2 } \right)$ . In addition, from (3), we obtain that the ISP with more content or the more valuable content can extract higher subscription fees by the end users. Nevertheless, in all cases, the profits of ISP A are equal to the profits of ISP B. Although this is trivial without fragmentation, because both ISPs carry the same content, identical profits arise also with full or partial fragmentation due to the bargaining power that CPs have to pay low exclusivity fees or even extract a part of the ISPs’ profits. The bidding war among the ISPs for an exclusive CP makes them— finally—indifferent between winning and losing.

## 4.4. Comparative Statics

We now discuss how Internet fragmentation is affected through changes in the exogenous parameters of our setting. In particular, we study $u _ { 1 2 } ,$ which is a measure of content substitutability, and t, which is a measure of ISPs’ intensity of competition.

Complementarity of content. First, we examine how the level of complementarity (or substitutability) of the two contents affects the equilibrium outcome. We obtain these results by directly differentiating expressions (7) and (8) with respect to $u _ { 1 2 } .$ As the level of complementarity between the two contents $u _ { 1 2 }$ increases, the two thresholds ${ \hat { r } } ( a )$ and $\tilde { r }$ increase as well $( d \hat { r } / d u _ { 1 2 } > 0 , d \tilde { r } / d u _ { 1 2 } > 0 )$ . This means that the threshold ${ \hat { r } } ( a )$ that characterizes the full fragmentation area increases with $u _ { 1 2 } ,$ leading to more full fragmentation, and that the threshold $\breve { \tilde { r } }$ that characterizes the no fragmentation area increases with $u _ { 1 2 }$ as well, rendering the no fragmentation outcome less likely in the market.

<sup>Proposition</sup> <sup>2.</sup> As the two contents become more complementary, that is, as $u _ { 1 2 }$ increases, full fragmentation is more likely to arise in equilibrium, whereas no fragmentation is less likely to arise in equilibrium.

The intuition behind this result is as follows: full fragmentation is more likely when the content becomes more complementary because it is then particularly valuable for an ISP to try to break an equilibrium without full fragmentation. To see this, imagine that ISP i has an exclusive deal with CP 1 at Stage 1. At Stage 2, ISP −i can either offer an exclusivity deal to CP 2 or let this content be available on both platforms: since $u _ { 1 2 }$ is large, the latter scenario is what ISP −i wants to avoid, because it would be only the rival that benefits from the complementarity. This shifts to the left the threshold ${ \hat { r } } ( a )$ that we identified at Stage $^ { 2 , }$ making full fragmentation more likely to arise. As an outcome, no consumer enjoys any complementarity, precisely when this could be valuable to them. This apparent paradox arises because, taking as given the exclusivity reached by the rival ISP, the remaining ISP does not want to confer a positive externality to its rival.

Figure 3 Effect of Complementarity of Content  
![](/api/attachments/RF4BUG3T/fulltext/images/96e445a0bdb87d4212ee53b34f792fa3e4020f7a08a3660b580a7d34124df028.jpg)  
Note. $t = 1 ; u _ { 1 } = 2 ; u _ { 2 } = 1 ; t = 0 .$ For the dashed line, $u _ { 1 2 } = 3 . 5 ;$ for the thin line, $u _ { 1 2 } = 3 ;$ and for the thick line, $u _ { 1 2 } = 2 . 5$

As CPs are instead more substitutable for the end users, it becomes less and less likely that a full fragmentation scenario could emerge in equilibrium. In the limiting case, if the content of CP 2 does not add any more value when consumed jointly $( u _ { 1 2 } = u _ { 1 } )$ and the termination fee f is zero, there is no possibility of full fragmentation.<sup>11</sup>

Moreover, an increase in $u _ { 1 2 }$ shifts $\widetilde { r } \ \mathrm { u p } ,$ which means that the no fragmentation area reduces as content becomes more complementary. To see this, imagine CP 2 delivers its content to both ISPs. As $u _ { 1 2 }$ goes up, it becomes more likely that CP 1 prefers to be available exclusively at one ISP, which will be willing to pay a slotting allowance to CP 1, so as to take advantage solely of the content complementarity. This leads to a decrease in the area of no fragmentation.

The above result is presented in a numerical example in Figure 3. Three alternative cases are plotted. First, the CPs offer complementary contents $( u _ { 1 2 } >$ $u _ { 1 } + u _ { 2 } ) ;$ ; second, the CPs offer purely additive content $( u _ { 1 2 } = u _ { 1 } + u _ { 2 } ) _ { \it }$ and third, they offer substitutable contents $\left( { { u _ { 1 2 } } < { u _ { 1 } } + { u _ { 2 } } } \right)$

Competition between ISPs. As t increases, the ISPs become more differentiated such that competition between them is reduced. By directly differentiating expressions (8) and (7) with respect to $t ,$ we obtain that the threshold r˜ always decreases with t $( d \tilde { r } / d t < 0 )$ , whereas the threshold r 4a5 ˆ increases for low a $( d \hat { r } / d t \geq 0$ for $a \leq ( 6 f ( u _ { 1 2 } - u _ { 2 } ) + ( u _ { 1 2 } - u _ { 1 } ) ( u _ { 1 } -$ $u _ { 2 } + 3 ( u _ { 1 2 } - u _ { 2 } ) ) ) / ( 2 ( u _ { 1 2 } - u _ { 1 } ) ( 3 f + u _ { 1 2 } - u _ { 1 } ) ) )$ and decreases with high a.

<sup>11</sup> From (6), we have $\hat { a } \to \infty$ when $u _ { 1 2 } \to u _ { 1 } ,$ , and from (7), we have $\hat { r } \to 0$ when $u _ { 1 2 } \to u _ { 1 }$ and $f  0 .$

Figure 4 Effect of Competition Between ISPs  
![](/api/attachments/RF4BUG3T/fulltext/images/51612a570a7a8b722fc2693a0b9c8b2f780e4489b4446c2c86e5dd275ea48cea.jpg)  
Note. $u _ { 1 2 } = 3 ; u _ { 1 } = 2 ; u _ { 2 } = 1 ; t = 0 .$ . For the dashed line, t = 1; for the thin line, $t = 2 ;$ ; and for the thick line, $t = 3 .$

<sup>Proposition</sup> <sup>3.</sup> As competition between ISPs increases, Internet fragmentation is more likely to arise in equilibrium. Full fragmentation may be either more or less likely to arise, depending on the level of ad competition between $C P s .$

The threshold r˜ shifts down with t, which means that no fragmentation is more likely to arise in equilibrium. Competition among the ISPs is relaxed, and thus they are less keen on obtaining exclusivity of content to boost their own demand, since the end users are less willing to switch to the rival ISP. Concerning the threshold $\hat { r } ( a )$ that defines the full fragmentation area, we find that ${ \hat { r } } ( a )$ shifts to the right with t when a is relatively high, leading to less full fragmentation, but ${ \hat { r } } ( a )$ shifts up for relatively low values of a. In Figure 4, we present a numerical example.

## 5. NN Regulation: Zero-Price Rule, Strict Zero-Price Rule, and No-Exclusivity Rule

We now discuss the impact of the different approaches to NN regulation on Internet fragmentation. First, NN regulation can impose a zero-price rule, which sets the termination fee to zero. Second, a stricter form of the zero-price rule restricts all fees that might be exchanged between ISPs and CPs to zero (i.e., the termination and the exclusivity fees). Third, and alternatively, NN regulation could impose a straightforward no-exclusivity rule that forbids any exclusivity arrangements between ISPs and CPs, but does not impose restrictions on the termination fees (this would preclude the first two stages of the basic game described in the previous section). We now analyze each case in turn.

## 5.1. Zero-Price Rule

The effect of a zero-price rule can be readily addressed by studying how a change in f affects the equilibrium

## Figure 5 Effect of Termination Fee

![](/api/attachments/RF4BUG3T/fulltext/images/8b0fca8b480073a260e14018ffec7b66ae5102eb6ad5429f0301b2dd41a33965.jpg)  
Note. $t = 1 ; u _ { 1 2 } = 3 ; u _ { 1 } = 2 ; u _ { 2 } = 1$ . For the dashed line, $f = 0 . 4 ;$ for the thin line, $t = 0 . 2 ;$ for the thick line, $\boldsymbol { f } = 0$

outcome of the (otherwise) unregulated scenario. In particular, differentiating the relevant thresholds (7) and (8) with respect to f yields $\partial { \hat { r } } / \partial f > 0$ and $\partial \tilde { r } / \partial f > 0$ . Consequently, as the termination fee f increases, full fragmentation is more likely to arise in equilibrium, whereas no fragmentation is less likely to arise in equilibrium. However, it is important to note that (full and partial) Internet fragmentation may still occur under a zero-price rule where f is restricted to zero. The equilibrium properties described by Proposition 1 remain valid.

<sup>Proposition</sup> <sup>4.</sup> A zero-price rule cannot prevent full or partial Internet fragmentation. However, Internet fragmentation is less likely to occur under a zero-price rule.

In Figure 5, we change the values of the termination fee f and find that, as f increases, the area of full fragmentation increases, and the area of no fragmentation decreases, since it becomes more expensive for the CPs to deliver their contents to both ISPs.<sup>12</sup>

## 5.2. Strict Zero-Price Rule

Under the strict notion of the zero-price rule, both termination fees and exclusivity fees are restricted to zero; i.e., $f = e _ { i j } = 0 , i = A , B , \dot { j } = 1 , 2$ . Otherwise, the structure and timing of the game remains the same as before. In particular, a CP can still choose to offer its content (without any direct financial compensation) exclusively at one of the two ISPs.

Again, we provide some intuition for the derivation of the equilibrium, although we relegate all of the technical details to Online Appendix B. The lumpsum fees have no impact on the optimal subscription price of the ISPs in the third stage of the game. In the second stage, CP 2 decides whether to accept exclusivity or not, provided CP 1’s decision. If CP 1 has an exclusivity contract with an ISP, then CP 2 wishes to be exclusive with the other ISP if and only if ad competition between the two CPs is strong $( a > \hat { a } )$ Otherwise, if CP 1 does not have an exclusivity contract with any ISP, then CP 2 always prefers not to be exclusive to any ISP. Anticipating this, CP 1 decides whether to be exclusive to any ISP in the first stage. In the absence of exclusivity fees, the ISPs cannot engage in a bidding war for CP 1. Nevertheless, we find that if ad competition between the CPs is strong $( a > { \hat { a } } )$ , CP 1 opts for exclusivity exactly to mitigate this effect, anticipating that CP 2 will also opt for exclusivity. Otherwise, if competition is weak, CP 1 decides to deliver its content to all ISPs, and thus CP 2 also refrains from exclusivity, which yields no fragmentation in equilibrium. Thus, partial fragmentation cannot occur in equilibrium under the strict zero-price rule.

<sup>Proposition</sup> <sup>5.</sup> Full Internet fragmentation may arise in equilibrium even under the strict zero-price rule, where all termination and exclusivity fees are zero. In particular, full Internet fragmentation emerges in equilibrium when competition between CPs is intense $( a > { \hat { a } } )$ . Otherwise, the Internet remains unfragmented. Partial fragmentation does not emerge in equilibrium.

In addition, by comparing the two full fragmentation cases (one arising when ISP A delivers exclusively the content of CP 1 and ISP B delivers exclusively the content of CP 2, and the other when ISP A delivers exclusively the content of CP 2 and ISP B delivers exclusively the content of CP 1), we observe that ISP i obtains higher profits than its rival ISP when ISP i carries the content of the more efficient CP. In contrast, without NN regulation or under the standard zero-price rule, the two ISPs always obtained the same profits for the same parameter values due to the power of CPs to extract a part of the ISPs’ profits. In the absence of exclusivity fees, the bidding war between the ISPs cannot be triggered, which preserves the ISPs’ profits.

## 5.3. No-Exclusivity Rule

The regulator could also enact a blunt no-exclusivity rule; that is, all content must be delivered to all ISPs. This rule is similar to a mandated interconnection of networks, which is well known to the telecommunications industry. Obviously, under the no-exclusivity rule, Internet fragmentation cannot occur, by definition. This means that the profits of the two ISPs are the same, since they split the market equally. Likewise, the advertisement revenues of the two CPs are the same, although CP 1 is more efficient, because they reach an identical exposure.

## 6. Welfare Analysis and Policy Implications

## 6.1. Welfare Analysis

To discuss the policy implications for the case without NN regulation and the various NN cases, we make reference to the concepts of consumer surplus and total welfare. These are natural choices, given the attention put by regulators on users and efficiency, respectively, though of course one could also conduct an additional analysis based on the profits of the remaining stakeholders.

We start with consumer surplus. By summing up the net surplus of all end users, we obtain the consumers’ surplus for all potential values of $u _ { A }$ and $u _ { B } ,$

$$
\mathrm{CS} = \int_ {0} ^ {D _ {A}} (u _ {A} - p _ {A} - t z) d z + \int_ {D _ {A}} ^ {1} (u _ {B} - p _ {B} - t (1 - z)) d z.
$$

By substituting the demand and subscription fees (from expressions (4) and (3)), we have

$$
C S = \frac {u _ {A} + u _ {B}}{2} + \frac {(u _ {A} - u _ {B}) ^ {2}}{3 6 t} - \frac {5}{4} t.\tag{9}
$$

The analysis of CS is immediate. Note that $\partial { \mathrm { C S } } / \partial u _ { i } =$ $\textstyle \frac { 1 } { 2 } + ( u _ { i } - u _ { - i } ) / 1 8 t > 0 ,$ , where the positive sign is always ensured by (5). Hence, it is always better for consumers at ISP i to obtain more content, whatever the content offered at ISP −i. Intuitively, higher content will be reflected in a higher price, as described by (3), but competition ensures that the direct increase in utility always more than compensates for the higher subscription fee. Hence, the ranking of possible equilibria, from the consumers’ perspective, is unambiguous: no fragmentation is strictly better than any partial fragmentation equilibria, which, in turn, do strictly better than full fragmentation.

In particular, by substituting the relevant expressions from the equilibrium outcome presented in Online Appendix A into expression (9), we find that, in the unregulated case, it is

$$
\mathrm{CS} ^ {*} = \left\{ \begin{array}{l l} \frac {u _ {1} + u _ {2}}{2} + \frac {(u _ {1} - u _ {2}) ^ {2}}{3 6 t} - \frac {5}{4} t, & \\ & \text { if   full   fragmentation }, \\ \frac {u _ {1 2} + u _ {2}}{2} + \frac {(u _ {1 2} - u _ {2}) ^ {2}}{3 6 t} - \frac {5}{4} t, & \\ & \text { if   partial   fragmentation } (E, N E), \\ \frac {u _ {1 2} + u _ {1}}{2} + \frac {(u _ {1 2} - u _ {1}) ^ {2}}{3 6 t} - \frac {5}{4} t, & \\ & \text { if   partial   fragmentation } (N E, E), \\ u _ {1 2} - \frac {5}{4} t, & \text { if   no   fragmentation }. \end{array} \right.
$$

By direct comparison of consumer surplus in the case without NN regulation among the different fragmentation scenarios, we confirm the CS ranking described above. Also, CS under the partial fragmentation 4NE1 E5 scenario is higher compared to the partial fragmentation 4E1 NE5 scenario, which is expected since under 4NE1 E5 the more valuable content is delivered to both ISPs and hence enjoyed by all end users.

We now turn to the analysis of total welfare. Total welfare W is defined as the sum of ISPs’ profits, CPs’ profits, and consumers’ surplus,

$$
W = \Pi_ {\mathrm{ISP} _ {A}} + \Pi_ {\mathrm{ISP} _ {B}} + \Pi_ {\mathrm{CP} _ {1}} + \Pi_ {\mathrm{CP} _ {2}} + \mathrm{CS}.\tag{10}
$$

The analysis is more involved, because there are now several trade-offs. On one hand, symmetric distribution of content between both ISPs is more efficient than asymmetric distributions, since the resulting symmetric ISPs’ market shares at equilibrium minimize transportation costs. In addition, it is more efficient that users see both types of content, instead of excluding any possible viewer. Hence, from this perspective, one would expect no fragmentation to dominate both partial and full fragmentation. On the other hand, however, fragmented equilibria always increase the advertising revenues that directly enter the profits of the CP that faces no competition, and may increase the total ad revenues available at a given ISP. Hence, this effect can potentially go in the opposite direction.

To resolve this possible tension, we substitute the relevant expressions from the equilibrium outcome presented in Online Appendix A into (10). Total welfare in the unregulated case is then

$$
W ^ {*} = \left\{ \begin{array}{l} \frac {u _ {1} + u _ {2}}{2} + \frac {5 (u _ {1} - u _ {2}) ^ {2}}{3 6 t} - \frac {1}{4} t + a r, \\ \qquad \text {if full fragmentation}, \\ \frac {u _ {1 2} + u _ {2}}{2} + \frac {5 (u _ {1 2} - u _ {2}) ^ {2}}{3 6 t} - \frac {1}{4} t \\ \qquad + r \bigg (\frac {3 t + u _ {1 2} - u _ {2}}{3 t} + \frac {a (3 t - (u _ {1 2} - u _ {2}))}{6 t} \bigg), \\ \qquad \text {if partial fragmentation (E, NE)}, \\ \frac {u _ {1 2} + u _ {1}}{2} + \frac {5 (u _ {1 2} - u _ {1}) ^ {2}}{3 6 t} - \frac {1}{4} t \\ \qquad + r \bigg (\frac {3 t + u _ {1 2} - u _ {1}}{3 t} + \frac {a (3 t - (u _ {1 2} - u _ {1}))}{6 t} \bigg), \\ \qquad \text {if partial fragmentation (NE,E)}, \\ u _ {1 2} - \frac {1}{4} t + 2 r, \text {if no fragmentation.} \end{array} \right.\tag{11}
$$

We find that, whenever a is relatively low (i.e., competition for ad revenues among the CPs is relatively

Figure 6 Equilibrium Outcome Without NN Regulation and Socially Optimal Areas for $\scriptstyle t = 1 , u _ { 1 2 } = 3 , u _ { 1 } = 2 , u _ { 2 } = 1 , t = 0$  
![](/api/attachments/RF4BUG3T/fulltext/images/53ac4f3dc72abf9657eb49763b9b011a8459a40a79a8af064df1b6e44eb180a9.jpg)  
low, and thus the advertising profits obtained via exclusivity are not too high), total welfare under no fragmentation exceeds the total welfare under partial fragmentation, and the latter exceeds, in turn, the total welfare under full fragmentation.<sup>13</sup> In particular, when $a \leq 2$ this result always holds. Hence, in this case, all of the welfare effects described above go in the same direction and there is no trade-off. Therefore, for weak ad competition among the CPs (low a), it would be socially more desirable to obtain no fragmentation, since advertising revenues are not important, although content variety is. Nevertheless, this may not be an equilibrium outcome without any policy intervention.

In addition, when we compare the relative welfare between the two types of partial fragmentation, we observe a further trade-off. When exclusivity is achieved by the more valuable CP, $( E , N E )$ , on one hand, CS is lower compared with the 4NE1 E5 scenario since fewer end users enjoy the more valuable content, but, on the other hand, the more valuable CP obtains a higher market share and higher profits.

<sup>Proposition</sup> <sup>6.</sup> No fragmentation is always the $e f f i -$ cient outcome with respect to consumer surplus. With respect to total welfare, no fragmentation is efficient when ad competition between content providers is rather low $( a \leq 2 )$ . When ad competition between content providers is rather high $( a > 2 )$ , any one of the feasible fragmentation outcomes 44NE1 NE51 4E1 NE51 4NE1 E51 4E1 E55 may be efficient with respect to total welfare, depending crucially on the interplay of the parameter values.

Using the same numerical example as before, the total welfare ranking is illustrated in Figure 6, which shows the region of validity of each equilibrium outcome (focus on the solid lines) and the corresponding welfare ranking (focus on the downward sloping dashed and dotted lines). Below the downward sloping dashed line, the efficient outcome is no fragmentation 4NE1 NE5. Above the downward sloping dotted line, the efficient outcome is full fragmentation $( E , E )$ whereas in between the dashed and dotted line, the efficient outcome is partial fragmentation 4NE1 E5.<sup>14</sup> It is clear that, for the same set of parameters, the corresponding equilibrium outcome does not always coincide with the efficient outcome. In fact, only in the shaded areas are the privately chosen equilibrium regimes also socially optimal. In all other areas, a welfare-maximizing regulator would want to achieve a different regime. Note the richness of possibilities that arise: there may be both excessive content $( \mathrm { e . g . , }$ point A) and excessive exclusivity (e.g., point B). At point A, the equilibrium outcome is no fragmentation 4NE1 NE5, whereas the social optimum regime is full fragmentation 4E1 E5. But at point B, firms choose full fragmentation 4E1 E5, whereas the social optimum regime is no fragmentation 4NE1 NE5. Note that for $a < 2 ,$ , only excessive exclusivity may arise.

## 6.2. Policy Implications

Having shown that there is potentially room for intervention, the next step is to ask whether the specific policy tools at the regulator’s disposal are apt to improve welfare.<sup>15</sup> We first discuss the role played by termination fees in an otherwise unregulated scenario (zero-price rule). Note that the presence of the termination fees does not affect the level of total welfare since these fees are pure transfers from the CPs to the ISPs. Nevertheless, the termination fees affect the critical thresholds of $r ,$ which define the type of Internet fragmentation. When the termination fee f increases, both critical thresholds r 4a5ˆ and r˜ increase; thus, full fragmentation becomes more likely, whereas no fragmentation becomes less likely (Proposition 4). Through exclusivity, the CPs avoid paying the termination fees twice. Therefore, the zero-price rule where the termination fee is restricted to zero ensures that no fragmentation emerges more often in equilibrium. However, as pointed out by Proposition 4 and Figure 5, partial and full fragmentation remain to emerge in equilibrium. In addition, a strict zeroprice rule, where both termination and exclusivity fees are restricted to zero, ensures that no fragmentation emerges more often in equilibrium, compared to the unregulated case, but it does not always ensure no fragmentation. Consequently, a (strict) zero-price rule is not a perfect policy instrument to fully prevent Internet fragmentation. Clearly, when consumer surplus is the ultimate policy goal, then no fragmentation is always the preferred outcome, and a no-exclusivity rule is consequently a perfect policy instrument.

<sup>Proposition</sup> <sup>7.</sup> With respect to consumer surplus, the no-exclusivity rule is a perfect policy instrument.

With regard to total welfare, the analysis is more involved. According to Proposition $^ { 6 , }$ no Internet fragmentation is the unique efficient outcome when the intensity of competition over ads among the CPs is rather low $( \mathrm { i } . \mathrm { e } . , \bar { a } \leq 2 )$ . Thus, for the subsequent discussion, it is useful to consider this case first, and then the case where $a > 2$

6.2.1. When no Internet Fragmentation is the Unique Efficient Outcome $( a < 2 )$ . As mentioned above, the zero-price rule can help to achieve the efficient outcome in equilibrium more often (see Figure 7). However, even when $a \leq 2 ,$ , partial and full fragmentation continue to arise in equilibrium for low values of r.

By contrast, recall that the strict zero-price rule prevents partial fragmentation in equilibrium and achieves no fragmentation whenever $a \leq \hat { a }$ (see Proposition 5). Because ${ \hat { a } } > 2 ,$ , the strict zero-price rule effectively prevents Internet fragmentation for $a \leq 2$ (see Figure 8). However, the strict zero-price rule is a heavy-handed regulation that is hard to administer, because the regulator would have to monitor the possible side payments $( e _ { i j } )$ between CPs and ISPs. Evidently, for $a \leq 2 ,$ , the same outcome of no fragmentation could also be achieved by the simple noexclusivity rule, which is much easier to administer and should therefore be the preferred regulatory instrument in this parameter range.

Figure 7 Performance of the Zero-Price Rule Compared to No NN Regulation  
![](/api/attachments/RF4BUG3T/fulltext/images/6cabb97081465e4a118c71160d75ef785cff78be0f9881daf097070d1eddb5c6.jpg)  
Note. Black shaded areas indicate welfare improvements toward the first best, whereas gray shaded areas indicate welfare deteriorations away from the first best $( t = 1 , u _ { 1 2 } = 3 , u _ { 1 } = 2 , u _ { 2 } = 1 )$

Figure 8 Performance of the Strict Zero-Price Rule Compared to No NN Regulation  
![](/api/attachments/RF4BUG3T/fulltext/images/c7f2813effdd93a019f58830fcd22fd1308d3dc3df93ae16420ebb92fa1b8dd4.jpg)  
Note. Black shaded areas indicate welfare improvements toward the first best, whereas gray shaded areas indicate welfare deteriorations away from the first best $( t = 1 , u _ { 1 2 } = 3 , u _ { 1 } = 2 , u _ { 2 } = 1 , t = 0 . 4 )$

<sup>Proposition</sup> <sup>8.</sup> When no Internet fragmentation is the unique efficient outcome (i.e., when $a \leq 2 )$ , all policy interventions (zero-price rule, strict zero-price rule, and noexclusivity rule) will improve total welfare. In particular, the strict zero-price rule and the no-exclusivity rule are perfect policy instruments in this case.

6.2.2. When Internet Fragmentation may be the Efficient Outcome $( a > 2 )$ . When the regulator deems that $a > 2 ,$ or if it is unsure about the level of $^ { a , }$ and it puts considerable weight on total welfare (as opposed to consumer surplus alone), then the choice of the appropriate policy instruments is much more complicated. In fact, none of the policy instruments surveyed here will be able to perfectly align private and social incentives for all parameter ranges.

Consider the case when ad competition between CPs is intense $( a > { \hat { a } } )$ , such that full fragmentation is most likely the efficient outcome, unless r is close to zero. In this parameter range, full fragmentation is already achieved in equilibrium without any policy intervention. Thus, the use of additional policy instruments cannot do better than if the market were left without NN regulation. At least the zero-price rule and the strict-zero-price rule will not affect this privately efficient equilibrium outcome, and they are thus not harmful here (see also Figures 7 and 8). On the contrary, the application of the no-exclusivity rule could yield to excessive content in this parameter range and is thus potentially harmful to total welfare.

For the case where ad competition between CPs is at an intermediate level $( a \in ( 2 , { \hat { a } } ) )$ , a meaningful application of any one of the available policy instruments seems almost impossible. Depending on the parameter range and on the policy instrument, welfare can be improved or deteriorated (see Figures 7 and 8) compared to the case without NN regulation. Consider point D in Figures 7 and $^ { 8 , }$ for example. Here the efficient outcome is full fragmentation, which is achieved in the private equilibrium for $f = 0 . 4$ . Any type of intervention ((strict) zeroprice rule or no-exclusivity rule) would be counterproductive there, because this would alter the full fragmentation result and would in turn decrease welfare. (The strict zero-price rule and the no-exclusivity rule would lead to no fragmentation, whereas the zero-price rule would lead to partial fragmentation.) In other cases instead, when r is low, the strict zeroprice rule and also the no-exclusivity rule are able to do much better than the private equilibrium, because they can achieve the first-best regime (e.g., point B in Figure 6).

<sup>Proposition</sup> <sup>9.</sup> When ad competition between content providers is intense $( a > { \hat { a } } ) .$ , policy interventions are at best superfluous with respect to total welfare, but can also be harmful as in the case of the no-exclusivity rule. For intermediate levels of content providers’ ad competition $( 2 <$ $a < { \hat { a } } )$ , any one of the available policy instruments can be harmful to total welfare.

In conclusion, it seems that, for $a > 2 ,$ any policy intervention is either unnecessary or risks being harmful to total welfare. Thus, in the absence of a clear benefit from regulation, it seems safe to say that policy intervention should be avoided.

## 7. Model Extensions and Limitations

The base model presented above already provides a rich set of equilibria and nuanced policy advice. In an effort to demonstrate the robustness as well as the potential limitations of the base model and its implications, we will now scrutinize some of the assumptions made.

First, the base model assumes that ISPs negotiate initially with the more valuable CP and then subsequently with the less valuable CP. In Online Appendix D, we explore an alternative timing of the game, where both ISPs offer exclusivity contracts simultaneously to the CPs. The analysis shows that our results are very robust in this regard. More precisely, the only difference to the results of the base model is this, that for large r and large $a ,$ no fragmentation and full fragmentation are equilibria. However, this does not affect our policy conclusions since full fragmentation remains an equilibrium for large a and is the unique equilibrium for small r and large a.

Second, we posited that the measure of complementarity of the two contents $( u _ { 1 2 } )$ and the measure of ad competition among the CPs (a) are independent. However, it could reasonably be argued that strong CP competition over ads is likely to be driven by high substitutability of content. Thus, $u _ { 1 2 }$ and a might be negatively correlated. In Online Appendix $\mathrm { E } ,$ we analyze the fragmentation equilibria under such correlation and show that our results are robust to this modification.

Third, in the base model we assume that the CPs’ investment in quality is sunk already at the time when CPs decide about accepting exclusivity contracts. We then characterize the equilibrium for every feasible constellation of CPs’ content qualities. In Online Appendix F, we instead allow the CPs to strategically invest in quality prior to negotiating exclusivity. We then determine for zero and nonzero termination fees which quality levels will be chosen by the CPs and which fragmentation outcome will prevail in equilibrium. We can show that termination fees do not just affect the fragmentation regime, but also the CPs’ incentives to invest in content quality. As in the base model, fragmentation becomes more likely when termination fees increase. However, under fragmentation, CPs’ incentives to invest into quality also increase. Thus, over and beyond the welfare effects discussed previously, a departure from the zero-price rule has an additional positive welfare effect due to the fact that CPs’ content quality is likely to increase.

Fourth, the base model assumes that termination fees are exogenous and the same for both ISPs. We then characterize the equilibrium for every value of such a termination fee. Although this assumption is certainly a simplification, which keeps the analysis tractable, it is worth mentioning that it is not an insensible assumption. First, as termination fees are currently set at zero, it is unlikely that a regulator would allow for large variations compared to the status quo, because changes might be disruptive. Second, if changes were allowed, they would be implemented either by the regulator itself, who would treat ISPs identically, or by industry-wide agreements that, again, are very likely to be nondiscriminatory. In either case, both ISPs would charge the same level of $f .$ . Yet, it is of interest to analyze the case where, alternatively, each ISP could set unilaterally its own termination fee; that is, ISP A could set a termination fee $f _ { A }$ unilaterally and independently from $f _ { B } ,$ the fee set by ISP B. We study this extension in Online Appendix G. We find that each ISP would have unilateral incentives to set high termination fees, as is typical of competitive bottlenecks. We can show that the result of Proposition 4 is extended to its natural consequence: with endogenous termination fees, the only equilibria that can arise are those that involve full fragmentation. Moreover, as termination fees, in our model, do not affect the amount of content delivered, they are simply an additional rent extraction device that ISPs use to appropriate CPs’ profits, but they do not directly affect total surplus.

Fifth, in the base model, we assume that end users subscribe to exactly one of the two ISPs, i.e., they single home. This is sensible when end users have a limited budget or when they incur significant transaction costs for establishing and maintaining a second network subscription. However, it can also be reasonable to assume that end users are indeed able to subscribe to both ISPs, i.e., they multihome. This can be desirable when users are confronted with a full fragmentation scenario. By multihoming users can then “undo” fragmentation. We study multihoming in Online Appendix H. We derive that multihoming can possibly occur, and thus affect our results, only in a fairly limited parameter region. This is the case when $t \in ( ( u _ { 1 2 } - u _ { 2 } ) / 2 , ( 2 u _ { 1 2 } - ( u _ { 1 } + u _ { 2 } ) ) / 2 ) .$ , i.e., when the degree of content complementarity $\left( u _ { 1 2 } \right)$ is neither too large nor too small compared to the degree of differentiation between ISPs (t). Even in this parameter region, we can show that the different fragmentation scenarios that we characterize under single homing (full/partial/no fragmentation) still arise. In this sense, our main results are robust. However, in line with the intuition, if we allow for multihoming, fragmentation becomes less likely as users themselves can undo full fragmentation by subscribing to both ISPs. Moreover, multihoming yields new trade-offs with respect to welfare. On one hand, with multihoming, some (but generally not all) end users see all content under full fragmentation. This tends to increase consumer surplus compared to single homing. On the other hand, prices are monopoly-like under multihoming, and those end users that multihome also bear additional transportation costs. This tends to lower consumer surplus compared to single homing. Likewise, there also exists an additional welfare trade-off from the perspective of the CPs. On one hand, CPs earn less exclusivity ad revenues under multihoming. On the other hand, there is also additional demand (viewers) due to multihoming. In other words, we cannot expect that multihoming generally delivers better welfare results compared to single homing, and the assessment depends crucially on the specific parameter setting.

Sixth, in the base model we assume that CPs receive revenues predominantly from advertising. In fact, this was highlighted as one of the distinct features that differentiates Internet CPs from other, traditional CPs. Notice that even though a CP’s revenue model may not be entirely financed through advertisement, it may still heavily rely on advertisement. This includes the so-called “freemium” model, where a basic version of the content is offered for free (and financed through advertisements), whereas consumers have to pay extra to access the premium version. Popular services that use the freemium model are, for example, Skype, LinkedIn, Spotify, and Flickr. However, even for the most successful services, the freemium model still relies on advertising. Usually users that are willing to pay for the service are greatly outnumbered and comprise only around 5% of all users (see, e.g., Doerr et al. 2010, Wagner et al. 2013). Accordingly, advertisement expenditures on the Internet continue to grow (Nielsen 2013). Nevertheless, we acknowledge as a limitation of our model that we do not consider direct payments between end users and CPs. This would fundamentally change our model and parallel more closely the model analyzed in Hagiu and Lee (2011).

Seventh, in the base model we assume that ISPs make take-it-or-leave-it offers to the CPs. This does not necessarily mean that all of the surplus of CPs is extracted. The ISPs’ bargaining power is in fact limited as they compete to attain exclusivity with CPs. In any case, it is important to highlight that the relative bargaining power of ISPs and CPs in each stage will only affect the size and sign of the exclusivity fee, but not the fragmentation equilibrium outcome or corresponding welfare result. This is because the fragmentation equilibrium depends on the joint profits of the ISP and CP, and is independent of how the joint profits are divided between the two.

Finally, our welfare analysis rests on the assumption that advertising is informative. If it were purely persuasive, we should have instead given zero weight to advertising since “it has no ‘real’ value to consumers” (Bagwell 2007, p. 1705), in which case we currently overestimate the benefits from advertising for welfare. Moreover, a fuller model of informative advertising would need to also take into account the profits of the producers who advertise and of the consumers/subscribers who also consume the advertised products. We have basically given a zero weight to these additional aspects, so we may be either underor overestimating the role of advertising rates in our social welfare function.

## 8. Summary and Conclusion

The potential fragmentation of the Internet due to exclusivity agreements between CPs and ISPs is currently of concern to policy makers, such as the European Commission. This is because Internet fragmentation counters the idea of a global Internet, in which content is ubiquitously available and benefits everybody. In this context, it has been argued that the principle of NN would preserve an unfragmented Internet (Lee and Wu 2009). More specifically, it is argued that absent NN regulation, which imposes a zeroprice rule on the termination fees that CPs must pay to ISPs, the emergence of Internet fragmentation is enkindled by the ISPs’ desire to compete on exclusive content.

In this article, we formally investigate this argument under some general assumptions. In particular, we study how termination fees (i.e., a zero-price rule), competition between ISPs, and ad competition between CPs affect the emergence of exclusive contracts and thus Internet fragmentation. We find that the zero-price rule of NN is neither a sufficient nor a necessary policy instrument to prevent Internet fragmentation. More precisely, we can show that Internet fragmentation (partial or full) emerges in equilibrium, both without NN regulation as well as under a zeroprice rule. Full Internet fragmentation even continues to emerge in equilibrium under a strict notion of the zero-price rule where not only the termination fees but all side payments (exclusivity fees) between CPs and ISPs are restricted to zero. Thus, if the ultimate regulatory goal is to prevent Internet fragmentation, then it seems more appropriate to directly target the emergence of exclusive content by means of a noexclusivity rule. In contrast to a zero-price rule, for which the regulator would need to monitor the payments between CPs and ISPs, a no-exclusivity rule is relatively easy to administer and control. However, we can also confirm that the zero-price rule indeed increases the likelihood that the Internet remains unfragmented in equilibrium, whereas at the same time full fragmentation becomes less likely. Hence, all of the considered policy interventions (zero-price rule, strict zero-price rule, and no-exclusivity rule) will push the market toward less or even no Internet fragmentation compared to a market without NN regulation.

Nevertheless, it is questionable whether any policy intervention is justified in the present context. We proved that no fragmentation is in fact always the efficient outcome with respect to consumer surplus. Consequently, if the policy maker considers consumer surplus as its welfare standard, then the use of a noexclusivity rule is advisable. However, with respect to total welfare, no fragmentation is the efficient outcome only when the competition over ads among the CPs is not too strong. If, on the contrary, ad competition between CPs is intense (which implies that the advertisement revenues that CPs can earn under full exclusivity are much higher than under competition), then full fragmentation becomes the efficient outcome with respect to total surplus, provided that advertising is informative. In the latter case, none of the above policy tools is able to improve on the equilibrium outcome absent regulation. Evidently, here intervention by means of a no-exclusivity rule entails a significant type I error, as it may even be detrimental to total welfare in this case. Also, for intermediate levels of ad competition between CPs, all of the surveyed policy instruments are subject to significant type I (i.e., regulating away from the first best) or type II (i.e., not regulating toward the first best) errors. Although welfare improvements may be achieved under some circumstances, it may also occur that welfare is deteriorated. Thus, any policy intervention is very risky and should be avoided.

In conclusion, we do not find a strong case for the use of NN regulation to prevent Internet fragmentation. Although NN regulation may lessen the extent of Internet fragmentation, it cannot prevent it. If such prevention is desired, a simple no-exclusivity rule seems to be more suitable to achieve it. Moreover, with respect to total welfare, Internet fragmentation is not necessarily an inefficient outcome, and any policy intervention involves significant errors and may thus be harmful. To avoid ill-guided regulation, especially in such a dynamic industry, where not only consumer surplus but also innovations (for which total welfare is a sensible measure) are important, it is therefore reasonable not to impose NN regulation ex ante. Of course, this does not limit the applicability of ex post regulation in the form of competition policy, which may still scrutinize termination fees and exclusivity contracts, but on a case-by-case basis.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2015.0567.

## Acknowledgments

The authors thank the senior editor, associate editors, three anonymous referees, and Marc Bourreau, Anna D’Annunzio, Bruno Jullien, Tobias Klein, and Thibaud Vergé for very constructive and helpful discussions and comments.

## References

Anderson SP (2012) Advertising on the Internet. Peitz M, Waldfogel J, eds. The Oxford Handbook of the Digital Economy (Oxford University Press, New York), 355–398.

Armstrong M (1999) Competition in the pay-TV market. J. Japanese Internat. Econom. 13(4):257–280.

Armstrong M (2006) Competition in two-sided markets. RAND J. Econom. 37(3):668–691.

Athey S, Calvano E, Gans JS (2013) The impact of the Internet on advertising markets for news media. NBER Working paper 19419, Cambridge, MA. http://www.nber.org/papers/w19419.

AT&T (2008) AT&T and EA bring spore to a new universe of gamers. Accessed September 12, 2013, http://www.att .com/gen/press-room?pid=4800&cdvn=news&newsarticleid =25976.

Bagwell K (2007) The economic analysis of advertising. Armstrong M, Porter R, eds. Handbook of Industrial Organization, Vol. 3 (North Holland, Amsterdam), 1701–1844.

Bloomberg Business (2005) At SBC, it’s all about “scale and scope.” Accessed September 12, 2013, http://www.bloomberg.com/ bw/stories/2005-11-06/online-extra-at-sbc-its-all-about-scale -and-scope.

Bloomberg Business (2011) AT&T to offer exclusive Zynga content, sell HTC Facebook phone. Accessed September 12, 2013, http://www.bloomberg.com/news/articles/2011-06-29/ at-t-reports-download-agreement-with-zynga.

Bourreau M, Kourandi F, Valletti T (2015) Net neutrality with competing Internet platforms. J. Indust. Econom. 63(1):30–73.

Carter KR, Watanabe T, Peake A, Marcus JS (2010) A comparison of network neutrality approaches in: the U.S., Japan, and the European Union. Working paper, WIK-Consult, Bad Honnef, Germany. http://ssrn.com/abstract=1658093.

Cheng HK, Bandyopadhyay S, Guo H (2011) The debate on net neutrality: A policy perspective. Inform. Systems Res. 22(1):60–82.

Choi JP, Kim BC (2010) Net neutrality and investment incentives. RAND J. Econom. 41(3):446–471.

Choi JP, Jeon DS, Kim BC (2015) Network neutrality, business models, and Internet interconnection. Amer. Econom. J.: Microeconomics Forthcoming.

CNNMoney (2013) Verizon inks deal to live-stream Sunday afternoon NFL games. Accessed September 12, 2013, http:// money.cnn.com/2013/06/05/technology/mobile/verizon-nfl/

D’Annunzio A, Russo A (2013) Network neutrality, access to content and online advertising. KOF Working paper 344, KOF Swiss Economic Institute, ETH Zurich, Zurich. http://www.kof .ethz.ch/de/publikationen/p/kof-working-papers/344/.

Deutsche Welle (2010) Deutsche Telekom moves against Apple, Google and net neutrality. Accessed September 12, 2013, http:// www.dw.de/deutsche-telekom-moves-against-apple-google-and -net-neutrality/a-5439525.

Doerr J, Benlian A, Vetter J, Hess T (2010) Pricing of content services—An empirical investigation of music as a service. Nelson ML, Shaw MJ, Strader TJ, eds. Sustainable e-Business Management, Lecture Notes Bus. Inform. Processing, Vol. 58 (Springer, Berlin Heidelberg), 13–24.

Dou W (2004) Will Internet users pay for online content? J. Advertising Res. 44(4):349–359.

Dukes A, Gal-Or E (2003) Negotiations and exclusivity contracts for advertising. Marketing Sci. 22(2):222–245.

Economides N, Hermalin B (2012) The economics of network neutrality. RAND J. Econom. 43(4):602–629.

Economides N, Tåg J (2012) Net neutrality on the Internet: A twosided market analysis. Inform. Econom. Policy 24(2):91–104.

Evans D (2009) The online advertising industry: Economics, evolution, and privacy. J. Econom. Perspect. 23(3):37–60.

Faulhaber GR (2011) Economics of net neutrality: A review. Comm. Convergence Rev. 3(1):53–64.

Guo H, Easley RF (2014) Network neutrality versus paid fast lanes: Analyzing the impact on content innovation. Working paper, Department of Management, Mendoza College of Business, University of Notre Dame, South Bend, IN. http://ssrn.com/ abstract=2134085.

Guo H, Cheng HK, Bandyopadhyay S (2012) Net neutrality, broadband market coverage and innovations at the edge. Decision Sci. 43(1):141–172.

Guo H, Cheng HK, Bandyopadhyay S (2013) Broadband network management and the net neutrality debate. Production Oper. Management 22(5):1287–1298.

Guo H, Bandyopadhyay S, Cheng HK, Yang YC (2010) Net neutrality and vertical integration of content and broadband services. J. Management Inform. Systems 27(2):243–275.

Hagiu A, Lee R (2011) Exclusivity and control. J. Econom. Management Strategy 20(3):679–708.

Hemphill CS (2008) Network neutrality and the false promise of zero-price regulation. Yale J. Regulation 25(212):135–179.

Hermalin B, Katz M (2007) The economics of product-line restrictions with an application to the network neutrality debate. Inform. Econom. Policy 19(2):215–248.

Hotelling H (1929) Stability in competition. Econom. J. 39(153): 41–57.

Jamison M, Hauge JA (2008) Getting what you pay for: Analyzing the net neutrality debate. Working paper, Public Utility Research Center Department of Economics, University of Florida, Gainesville, FL. http://ssrn.com/abstract=1081690.

Krämer J, Wiewiorra L (2012) Network neutrality and congestion sensitive content providers: Implications for content variety, broadband investment and regulation. Inform. Systems Res. 23(4):1303–1321.

Krämer J, Wiewiorra L, Weinhardt C (2013) Net neutrality: A progress report. Telecomm. Policy 37(9):794–813.

Kroes N (2011) Speech at the OECD High Level Meeting on the Internet Economy, Paris. European Commission SPEECH/11/ 479. http://europa.eu/rapid/press-release\_SPEECH-11-47.

Lambert (2010) Vodafone and Telefonica are overplaying their hand with Google. Accessed September 12, 2013, http:// telecoms.com/opinion/vodafone-and-telefonica-are-overplaying -their-hand-with-google/.

Lee R, Wu T (2009) Subsidizing creativity through network design: Zero pricing and net neutrality. J. Econom. Perspect. 23(3):61–76.

Los Angeles Times (2010) Verizon-only Bing app shows proprietary side of Android (August 30). Accessed March 19, 2015, http:// latimesblogs.latimes.com/technology/2010/08/bing-verizon -android.html.

Nehl HP, Parplies K (2002) Internet joint ventures and the quest for exclusive content: The T -online cases. EC Competition Policy Newsletter 2002(2):57–60.

Nielsen (2013) Global ad spend: Display ads see double-digit growth in Q1. Accessed September 12, 2013, http://www .nielsen.com/content/corporate/us/en/newswire/2013/global -ad-spend–display-ads-see-double-digit-growth-in-q1.html.

Njoroge P, Ozdaglar AE, Stier-Moses NE, Weintraub GY (2013) Investment in two-sided markets and the net neutrality debate. Rev. Network Econom. 12(4):355–402.

Peitz M, Valletti T (2008) Content and advertising in the media: Pay TV versus free-to-air. Internat. J. Indust. Organ. 26(4):949–965.

PRNewswire (2003) Vodafone and Eidos sign Lara Croft Tomb Raider mobile deal. Accessed September 12, 2013, http://www .vodafone.com/content/index/media/vodafone-group-releases/ 2003/press\_release24\_09.html.

Reggiani C, Valletti T (2012) Net neutrality and innovation at the core and at the edge. Discussion Paper 1202, School of Economics, University of Manchester, Manchester, UK.

Rochet J, Tirole J (2006) Two-sided markets: A progress report. RAND J. Econom. 37(3):645–667.

Schuett F (2010) Network neutrality: A survey of the economic literature. Rev. Network Econom. 9(2):1–13.

Sluijs JP (2012) Network neutrality and Internet market fragmentation. Common Market Law Rev. 49(5):1647–1673.

van Schewick B (2007) Towards an economic framework for network neutrality regulation. J. Telecomm. High Tech. Law 5(2): 329–392.

Verizon (2007) ESPN and Verizon Wireless announce exclusive multi-year licensing agreement for award-winning ESPN sports content. Accessed September 12, 2013, http://www .verizonwireless.com/news/article/2007/02/pr2007-02-08.html.

Wagner TM, Benlian A, Hess T (2013) The advertising effect of free– Do free basic versions promote premium versions within the freemium business model of music services? Proc. 46th Hawaii Internat. Conf. System Sci. (IEEE, Washington, DC), 2928–2937.

Weeds H (2015) TV wars: Exclusive content and platform competition in pay TV. Econom. J., ePub ahead of print April 4, http://dx.doi.org/10.1111/ecoj.12195.
