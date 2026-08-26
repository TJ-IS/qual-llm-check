---
otero_id: 2514
otero_key: "H7EMY5BU"
title: "The Debate on Net Neutrality: A Policy Perspective"
authors: "Hsing Kenneth Cheng; Subhajyoti Bandyopadhyay; Hong Guo"
year: "2011"
journal: "Information Systems Research"
doi: "10.1287/isre.1090.0257"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.122.253.212] On: 25 May 2015, At: 04:59 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## 6SR

![](/api/attachments/H7EMY5BU/fulltext/images/accbcc9db8d3bad4f535237f6e8001f3c2a8852ae46f3b3f80c7798e6ddd1159.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## The Debate on Net Neutrality: A Policy Perspective

Hsing Kenneth Cheng, Subhajyoti Bandyopadhyay, Hong Guo,

## To cite this article:

Hsing Kenneth Cheng, Subhajyoti Bandyopadhyay, Hong Guo, (2011) The Debate on Net Neutrality: A Policy Perspective. Information Systems Research 22(1):60-82. http://dx.doi.org/10.1287/isre.1090.0257

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2011, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/H7EMY5BU/fulltext/images/f009d0f86a14c3b0ded88302523354dd9f8b50f04ef981a312b81728046a8e48.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# The Debate on Net Neutrality: A Policy Perspective

Hsing Kenneth Cheng, Subhajyoti Bandyopadhyay

Department of Information Systems and Operations Management, Warrington College of Business Administration, University of Florida, Gainesville, Florida 32611 {hkcheng@ufl.edu, shubho@ufl.edu}

Hong Guo

Department of Management, Mendoza College of Business, University of Notre Dame, Notre Dame, Indiana 46556, hguo@nd.edu

he status quo of prohibiting broadband service providers from charging websites for preferential access Tto their customers—the bedrock principle of net neutrality (NN)—is under fierce debate. We develop a game-theoretic model to address two critical issues of NN: (1) Who are gainers and losers of abandoning NN? (2) Will broadband service providers have greater incentive to expand their capacity without NN? We find tha if the principle of NN is abolished, the broadband service provider stands to gain from the arrangement, as a result of extracting the preferential access fees from content providers. Content providers are thus left worse off, mirroring the stances of the two sides in the debate. Depending on parameter values in our framework, consumer surplus either does not change or is higher in the short run. When compared to the baseline case under NN, social welfare in the short run increases if one content provider pays for preferential treatment but remains unchanged if both content providers pay. Finally, we find that the incentive to expand infrastructure capacity for the broadband service provider and its optimal capacity choice under NN are higher than those under the no-net-neutrality (NNN) regime, except in some specific cases. Under NN, the broadband service provider always invests in broadband infrastructure at the socially optimal level but either under- or overinvests in infrastructure capacity in the absence of NN.

Key words: net neutrality; economics of net neutrality; broadband service providers; content providers; consumer surplus; social welfare

History: Vallabh Sambamurthy, Senior Editor; Srinivasan Raghunathan, Associate Editor. This paper was received on May 20, 2007, and was with the authors 10 months for 3 revisions. Published online in Articles in Advance March 1, 2010.

## Introduction

The “net neutrality” debate has reached a fever pitch as Congress mulls legislation that would allow Internet service providers to charge Web sites for preferred delivery of digital content.

—“Should the Net Be Neutral,” The Wall Street Journal Online, May 24, 2006 (WSJ 2006)

The recent proposal by broadband providers such as Verizon, Comcast, and AT&T to charge popular websites for preferential access to their residential and commercial customers has generated widespread attention in the media (Helm 2006, Waldmeir 2006). The proposal goes straight to the heart of the debate on the idea of “net neutrality (NN)”—the phrase that was first coined by Columbia Law School Professor Tim Wu—and is used to signify the concept that the Internet is merely a carrier of online content that does not distinguish one website from another. The central idea inherent in this concept is that a “maximally useful public information network aspires to treat all content, sites, and platforms equally” (Wu 2003, p. 142), and while a formal definition of the operationalization of the principle does not exist, Hahn and Wallsten (2006) point out that NN “usually means that broadband service providers charge consumers only once for Internet access, do not favor one content provider over another, and do not charge content providers for sending information over broadband lines to end users” (p. 1).

Popular online content providers such as Google, Yahoo!, and Microsoft would like to maintain the status quo, which they claim would preserve the egalitarian philosophy on which the Internet was founded. Other supporters of the concept include online startups, which claim that it would be almost impossible for them to pay these proposed fees when their revenue streams are almost nonexistent, because they have to give away most of their content to build a loyal customer base (Sydell 2006). Some venture capitalists have even argued that abandoning NN would result in would-be entrepreneurs becoming more hesitant to start a business, which might hurt the competitiveness of American online firms in the long run (Sydell 2006, Wu 2006a). Vint Cerf, the renowned computer scientist who is commonly referred to as one of the “founding fathers of the Internet,” contends that such a payment structure would result in the Internet increasingly resembling today’s mass media, where a few Internet service providers (ISPs) control what the customers effectively may access (Waldmeir 2006). Tim Berners-Lee, the founder of the World Wide Web, also favors keeping NN in place, because “[the Internet] is the basis of a fair competitive market economy” (Berners-Lee 2006, blog entry). Finally, some people have voiced their fears of the ISPs starting to offer such services as Internet telephony to their consumers at rates that undercut rival providers who would struggle to remain competitive if they have to pay these fees. This again might result in stagnation in what has so far remained one of the most open marketplaces.

The ISPs have argued that they have put their resources to maintain and upgrade the physical infrastructure to provide the services to consumers, while the popular websites have thus far gotten a “free ride” on their resources<sup>1</sup> (Waldmeir 2006) and that the “Internet service providers should be allowed to strike deals to give certain websites or services priority in reaching computer users” (Krim 2005, p. D05). With online content increasing exponentially over the years, and consumers increasingly becoming used to broadband access, it will be necessary to meet the rising costs of increasing capacity and serving an expanded consumer base. Not having these sources of revenue might act as a disincentive to upgrade the service providers’ infrastructure and affect their plans of increasing existing capacities. That, in turn, would affect many emerging online services, such as realtime broadband video, which by design, require preferential treatment of their packets. In some ways, the ISPs contend, the new payment mechanisms might herald the beginning of new business models that demand preferential treatment of their packets and that the “vertical integration of new features and services by broadband network operators is an essential part of the innovation strategy companies will need to use to compete and offer customers the services they demand” (Thierer 2004, p. 1).

The proper usage and context of the term “net neutrality” itself has been subject to confusion (Wu 2006b); an extensive discussion of the issues can be found in Economides and Tag (2007) and Wu (2003). In brief, network neutrality aims to address concerns raised by some specific behavior of the broadband service providers: (1) blocking of some content providers; (2) preferential treatment of one content provider over another; and (3) transparency failures, whereby a broadband provider fails to notify its customers and content providers what service they offer in terms of estimated bandwidth, latency, etc. (Wu 2006b). The current proposals by the broadband service providers (i.e., the ISPs) have raised concerns around the second issue—i.e., the possibility that one content or application provider pays the broadband service provider for preferential treatment of its packets, as the ISP acts effectively as a gatekeeper between the content providers and the customers it serves.<sup>2</sup>

The entire debate has raised a number of unanswered questions that are of interest to researchers and practitioners alike, not to mention the regulatory agencies. The intensity of the public debate, and the stakes involved in the issue, were brought into focus during a House Committee hearing in April 2006 (Wu 2006a), where it was pointed out that “[the Internet] has become part of America’s basic infrastructure. It has become as essential to people and to the economy as the roads, the electric grid, or the telephone. Given this infrastructure, Americans are accustomed to basic rights to use the network as they see fit” (p. 43). After a relatively quiet year in 2007, the NN debate is back on top of the technology agenda in Washington, with the lawmakers introducing a new bill, the “Internet Freedom Preservation Act of 2008” (H. R. 5353) (2008), on February 12, 2008.

From a policy perspective, two issues are of particular interest. First, the regulatory agencies would like to know who are the gainers and losers if the principle of NN is abolished. Specifically, if social welfare increases as a result of abandoning net neutrality— and more specifically, the end consumers are better off—the idea for the proposed payment mechanisms would gain traction among policy makers. Conversely, if abandoning the principle of NN results in helping a few private agencies to extract more rent, the idea would find a much less sympathetic audience. In the first part of our paper, we analyze this issue in the NN debate within a game-theoretic model, where we determine the equilibrium in the strategies employed by the content providers, which, in turn, prompts the appropriate profit-maximization strategy of the Internet service provider.

The second issue of interest to policy makers is to check the veracity of a key claim of the ISPs: notably, that under NN, the incentive to expand the capacity of the existing infrastructure for the next generation of broadband services is much less, as compared to when they are allowed to charge the online content providers for preferential treatment. For policy makers, this is indeed a key issue. Higher capacity broadband services will enable many services that are deemed important for the society as a whole. Some examples of such services include disaster recovery, remote medical supervision, and the like. For content providers, the next generation broadband services will enable instant delivery of high-definition movies, consumer interactivity, a richer online shopping experience, and so forth, and in the process, open many new channels of revenue generation. In fact, many consumers who currently do not feel the need for broadband services for their typical Internet activities of e-mail or online shopping might be ready to pay for such broadband services (Bandyopadhyay and Cheng 2006). In the second half of this paper, we treat infrastructure capacity as a strategic variable for the ISP in the long run (as opposed to it being a constant in the short-run problem) and explore two related issues: (1) Do ISPs have a greater incentive to expand their capacities if the principle of NN is abandoned? (2) How do the optimal capacity choices under NN differ from those when NN is not longer enforced?

From the analytical perspective, what drives the problem is the increased latency of the applications and content of those providers that are given less favorable treatment by the ISP. In other words, the packets from these providers face increased congestion, which translates into a delay disutility for the end users. Thus, while a consumer might have some intrinsic preferences of favoring one content provider over another, these preferences can be modified by one’s ISP by decreasing the delay disutility of one provider’s packets over another’s. A proper analysis of the problem therefore demands the modeling of the objectives of all three players involved—the content providers, the consumers, and the ISP (Hahn and Wallsten 2006). This exercise is distinct and different from the two-player models that analyze the broadband service provider that provides different classes of service to the consumers (Bandyopadhyay and Cheng 2006, Bhargava and Sun 2005). It is imperative that this distinction be highlighted, because the NN principle has sometimes been misinterpreted as a barrier to the ability of the broadband service provider to charge consumers different prices for different classes of service. As existing broadband service offerings indicate, ISPs today already charge different prices for different classes of broadband connection,<sup>3</sup> and such price discrimination strategies enhance social welfare (Bandyopadhyay and Cheng 2006, Edell and Varaiya 1999, Hermalin and Katz 2007). Finally, in analyzing the NN debate, we are not concerned about how hosting service providers charge content providers for hosting or transmitting their content over the World Wide Web (see Figure 1) or the various ways (like Web caching, for example) by which content providers have their content delivered faster. In the NN debate, the issue is whether the broadband service provider should be allowed to charge content providers for transmitting their content from its local switching office to the consumers.<sup>4</sup> In other words, the issue of interest is only at the local loop, the part encircled by the dashed line in Figure 1. Thus the debate is not about how Tier-1 or Tier-2 ISPs charge content providers, but about how local Tier-3 ISPs serving the end users propose to charge the content providers. For a very good discussion on the three tiers of ISPs, see Kurose and Ross (2003, §1.5). For a discussion on some of the early works on Internet pricing itself, one is referred to Gupta et al. (1996, 1997), two of the seminal papers in this area that rigorously analyzed the problem. In contrast to that literature, which looks at the problem of congestion at the Internet backbone, the NN issue looks at the issue of the congestion over the last mile.

Figure 1 Schematic of the Model  
![](/api/attachments/H7EMY5BU/fulltext/images/3d89d6aa50c589df99524857eaeeeb93f3a0ee71b8150590dd11a15b3963f878.jpg)

Thus the role of the broadband service provider that we need to model is not that of a producer of the service of providing hosting services to the content providers (and in most cases, the hosting service provider is different from the local broadband service provider at the consumers end) but as that of a gatekeeper who determines how the content from the content producers reaches the consumer, after it reaches the broadband provider’s local switching office.

As Economides and Tag (2007) point out, in sharp contrast to the large amount of literature that discusses the legal issues surrounding NN, there is a surprising lack of rigorous economic analysis of the NN debate. Economides and Tag (2007) identify six economic consequences of abolishing NN. First, twosided pricing will be introduced by the last mile ISP to charge end consumers on one side and content providers on the other side of the network. Second, the packets from the content providers paying the ISP will receive priority over those from nonpaying firms. Third, the ISP can engage in identity-based discrimination. For example, the search engine firm with the highest bid receives priority delivery of its search results to consumers, resulting in great distortion of the search engine market. A more detailed discussion of this issue is covered in Economides (2007). Fourth, new start-up firms will not likely win the prioritization auction, leading to less innovation. Fifth, ISPs can impose preferential treatment for their own content and applications over those of other providers. To consumers, online content and broadband service can be viewed as complementary products, where one market is competitive while the other is not (see, e.g., Economides and Salop 1992 for the implications on pricing of the joint product). Sixth, a significant reduction of trade on the Internet will occur, because multiple fees are likely to be charged for a single transmission over the interconnected networks that comprise the Internet.

Economides and Tag (2007) address the first issue in the above framework and find that NN regulation increases total industry surplus in the presence of a monopoly ISP. The same finding also applies to a duopoly setting. In relation to the Economides and Tag (2007) framework, we examine the second economic issue of NN. The most crucial aspect of the NN debate is that there is a constrained resource (the pipe between the ISP and the consumer) that is shared by packets of all of the content providers, and the very existence of this constrained resource has negative externalities associated with it. If this pipe were not a constrained resource, the ISPs would not have any credible mechanism to charge for preferential access. Analyzing this negative externality introduces a significant amount of challenge in the modeling but cannot be wished away if one has to do justice to the quality of the debate.

The rest of this paper is arranged as follows. The following section outlines our model. The next two sections analyze the model with NN and without NN, respectively. The section on the gainers and losers addresses our first research question: Who are the gainers and losers under NN versus those under a payment mechanism model without NN? The section on the capacity expansion decision considers the twin issues of the incentive to expand capacity for the ISP and that of the optimal capacity choice under NN and in the absence of net neutrality. The final section concludes by summarizing the policy implications of our analysis and providing some possible directions for future research. The objective of this paper, however, is not to make any policy prescriptions but rather to provide an objective economic analysis that clarifies some of the germane issues in this ongoing debate.

## The Model

To analyze the problem at hand, we consider a stylized model with three types of players: (1) a monopolist ISP that not only serves consumers in a specific geographic market by providing them with Internet access but also serves content providers by delivering their content to the consumers in this market; (2) two competing content providers that provide their service for free to the end users as they generate revenues from advertisers and associated click-throughs of the consumers; and (3) consumers who consume content from their preferred content provider through the Internet access provided by the local ISP. We develop the model both under NN and when NN is abolished in favor of the regime in which the ISP can charge the content providers (i.e., no net neutrality (NNN)).

In the concluding section, we discuss, in greater detail, how germane this particular revenue model is, but, in short, we believe that we faithfully capture the revenue model that is overwhelmingly prevalent among online content providers, which is very different from traditional online retailers like Amazon.com. The specifics of the revenue model change from one provider to another but, in general terms, it involves no upfront fees from the customer, but rather a customer’s value is encapsulated in the entire life cycle of one’s relationship with the firm. The idea was first proposed by the noted journalist and commentator on digital technologies, Esther Dyson (1994), and is now considered mainstream by industry observers like Chris Anderson (2008) and Nicholas Carr (2008), economics researchers like Paul Krugman (2008) and Hal Varian (McKinsey Quarterly 2009), and information systems researchers like Eric Clemons (Knowledge@Wharton 2008). In this framework, the firm gets its revenues not directly from a particular customer, but rather in a stochastic sense when these customers indirectly generate revenues through a variety of means such as banner advertisements, affiliate revenues, rental of subscription lists, and sale of aggregate information, to name a few.

Without loss of generality, we normalize the total number of end consumers (i.e., the total number of consumers served by the monopolist ISP) to 1. This unit mass of customers is uniformly distributed on line segment 0- 1 in terms of their ideal content. There are two competing online content providers,

Figure 2 The Content Providers and Their Share of Consumers

<table><tr><td>0 (Y)</td><td>x, marginal consumer</td><td>1 (G)</td></tr></table>

Y and $G ,$ where content provider Y is located at zero, while content provider G is located at the opposite end of the interval (see Figure 2). Let x be the marginal consumer that is indifferent to the content between Y and G. Then, the market shares for Y and G are x and $1 - x ,$ , respectively. This amounts to the market being fully covered, a standard assumption made in existing literature on two-sided markets to achieve analytical closure (Armstrong 2006).

Both content providers offer their basic services at no cost to the end users.<sup>5</sup> In our model, we consider the revenue generation of the content provider as the average revenue generated (from all sources) per-packet requested by the end consumer. Let $r _ { Y }$ and $r _ { G }$ denote the revenue rates of content provider Y and $G ,$ respectively, per packet for content. In other words, these two parameters denote the average rates at which the requests for content from the consumers provide revenues to the content providers from myriad types of advertisers that want to reach them. Without loss of generality, we assume that $r _ { G } > r _ { Y } ,$ , which means that one content provider 	G is better than the other (Y in getting the right consumers for its advertisers (and its other revenue sources), and therefore can charge higher advertising fees. This assumption does not affect our analysis results and is actually consistent with our empirical findings.<sup>6</sup> Without NN, the ISP provides preferential delivery service for content at a price $p ,$ which is the unit price for priority data packet transmission per packet. The technology to discriminate packets and streamline Internet traffic has been available at minimal fixed cost, and therefore the cost of implementing this mechanism of priority delivery of some content is assumed to be negligible. In response, the two content providers decide whether to pay for this preferential treatment. Then, the service decisions (whether to choose the preferential delivery service) for the two content providers can be represented by the indicator functions

$$
I _ {Y} = \left\{ \begin{array}{l l} 1, & \text {if Y pays} \\ 0, & \text {if Y does not pay}, \end{array} \right.
$$

$$
I _ {G} = \left\{ \begin{array}{l l} 1, & \text {if G pays} \\ 0, & \text {if G does not pay.} \end{array} \right.
$$

Let  be the Poisson arrival rate of content requested by each consumer, and it is expressed in packets per unit of time. Content provider $Y ^ { \prime } \mathrm { s }$ decision problem is m $1 \mathsf { a x } _ { I _ { Y } } \{ r _ { Y } \cdot \lambda \cdot x ( I _ { Y } , I _ { G } ) - I _ { Y } \cdot p \cdot \lambda \cdot x ( I _ { Y } , I _ { G } ) \}$ and content provider G’s decision problem is ma $\mathsf { x } _ { I _ { G } } \{ r _ { G } \cdot \lambda$ $[ 1 - \hat { x ( I _ { Y } , I _ { G } ) } ] - I _ { G } \cdot p \cdot \lambda \cdot [ 1 - \hat { x ( I _ { Y } , I _ { G } ) } ] \}$ . The demand for content providers $x ( I _ { Y } , I _ { G } )$ and $1 - x ( I _ { Y } , I _ { G } )$ depends on their service choices $I _ { Y }$ and $I _ { G } .$ . We provide further analyses of the demand realization later.

A consumer’s net utility from using the services of either $Y$ or G depends on one’s individual preferences, the distance of one’s preferred provider (i.e., either Y or G) from one's ideal, and the cost of delay that is a result of the general congestion in the access network between the ISP and the consumer. Parameter t measures the “fit cost” of the deviation from a consumer’s ideal content in the Hotelling framework (Hotelling 1929). Following Mendelson (1985), we denote $V ( \bar { \lambda } )$ to be the gross value function of this content for each consumer, assumed to be twice differentiable and strictly concave. Furthermore, consumers get a congestion disutility because of waiting for packets: the delay cost parameter d multiplied by the expected time in such a queuing system, w. The ISP charges a fixed Internet access fee F per unit time to the consumers for Internet access. Both the fixed fee F and the priority charge p are expressed in the same unit of time. Therefore the utility function for an arbitrary consumer $\tilde { x } \in [ 0 , 1 ]$ is $U _ { Y } ( \tilde { x } ) =$ $V ( \lambda ) - t \tilde { x } - F - d \lambda u$ if the content provider is Y and is $\dot { U } _ { G } ( \tilde { x } ) = V ( \lambda ) - t ( 1 - \tilde { x } ) - F - \dot { d \lambda w }$ if the content provider is G. To determine the delay $w ,$ we consider $\mu$ to be the capacity that the ISP provides to the consumers, expressed in packets per unit of time. This capacity constraint affects the service that the ISP renders to the consumers in a unique fashion. Specifically, we can think of the packets requested by the consumers as being serviced in an $\bar { M / M / 1 }$ queuing system. We assume that customers are homogeneous in terms of having the same rate of requests for content, valuation of content, and sensitivity to delay. Currently under NN, the congestion delay is the same $w _ { \mathrm { N N } } = 1 / ( \mu - \lambda )$ for all consumers and does not figure into the consumers’ decisions. However, under NNN, the congestion delay plays an important role.

To understand the impact of abolishing NN, consider a situation in which the ISP starts charging content providers Y and G for preferential treatment of their packets, and suppose without loss of generality, that only Y decides to pay for the service. As a result, any packet from Y that is received by the ISP as a request from one of its customers now gets preferred treatment to the top of the queue (these packets still face the congestion from other similarly preferred packets from Y ). We model the congestion in the network after Bandyopadhyay and Cheng (2006) and Mendelson (1985). Packets from G do not receive any preferential treatment and at any point in time are, in fact, queued after any packet from Y that might be requested at that point in time. Depending on the number of $Y ^ { \prime } \mathrm { s }$ packets in the channel, some consumers who previously preferred G might now find the congestion of G’s packets causing enough disutility that they might now prefer Y ’s service. The delays of the content providers’ packets are thus dependent on their service choices, denoted by $w ( I _ { Y } , I _ { G } )$ . Table 1 gives the delays of the four different outcomes under NNN for a two-class priority $M / M / 1$ queue with service preemption. The xs in the delay expressions are the corresponding marginal consumer who is indifferent between Y and G. Individual consumers then choose the content provider that yields the higher utility.

We assume that the consumer located at the two ends of the market is loyal to her corresponding content providers as the consumer at the end point receives content of perfect fit. That is,

$$
V (\lambda) - \frac {d \mu \lambda}{(\mu - \lambda) ^ {2}} - F > V (\lambda) - t - \frac {d \lambda}{\mu - \lambda} - F,
$$

an expression that can be simplified to

$$
d <   \frac {t (\mu - \lambda) ^ {2}}{\lambda^ {2}}.
$$

This assumption ensures the existence of a meaningful competition between the two content providers G and Y , one that is similar to a standard assumption in two-sided markets literature, e.g., Equation (8) of Armstrong (2006) and Assumption A3 of Armstrong and Wright (2007). Armstrong (2006) notes that this assumption is the “necessary and sufficient condition for a market-sharing equilibrium to exist” (p. 674). Because we are modeling only broadband consumers, we assume that the ISP captures all end consumers in 0- 1 under NN. Furthermore, the ISPs have stated that their intention is not to degrade the online experience for any current broadband subscriber even if NN is abolished, and therefore we assume that the ISP continues to serve all the current consumers when they start charging content providers for preferential delivery of their packets. In other words, we assume that the consumers’ value function $V ( \lambda )$ is sufficiently high that the utility for the indifferent consumer in any of the outcomes that follow is nonnegative.

Table 1 Delays Under NNN

<table><tr><td>Content provider decision</td><td>G pays</td><td>G does not pay</td></tr><tr><td rowspan="2">Y pays</td><td> $w_{Y1} = \frac{1}{\mu - \lambda},$ </td><td> $w_{Y3} = \frac{\mu}{[\mu - (1 - x_3)\lambda](\mu - \lambda)},$ </td></tr><tr><td> $w_{G1} = \frac{1}{\mu - \lambda}$ </td><td> $w_{G3} = \frac{1}{\mu - (1 - x_3)\lambda}$ </td></tr><tr><td rowspan="2">Y does not pay</td><td> $w_{Y2} = \frac{1}{\mu - x_2\lambda},$ </td><td> $w_{Y4} = \frac{1}{\mu - \lambda}, w_{G4} = \frac{1}{\mu - \lambda}$ </td></tr><tr><td> $w_{G2} = \frac{\mu}{(\mu - x_2\lambda)(\mu - \lambda)}$ </td><td></td></tr></table>

We consider a monopolist ISP that delivers digital content from its local switching office to the end users. While the monopoly assumption is a simplification in some locales, unlike many other countries, the extent of competition in the local broadband services market is very limited in the United States, so much so that in many places, a single broadband service provider is often a de facto monopolist (Economides 2008, Hausman et al. 2001). The situation is aggravated by the high switching cost of long-term service contracts and incompatible broadband technologies between cable and phone companies. Furthermore, many customers are not qualified for a DSL broadband service from phone companies, because they exceed the three miles distance limit from the phone company’s nearest switching office, making the cable operators the de facto monopolistic broadband service provider in several local markets (Turner 2007). Thus, in addition to providing the benefit of making the analysis tractable, the assumption closely reflects the reality of local broadband services in the United States. The ISP charges consumers a fixed Internet access fee F per unit time. If it is allowed to charge the online content providers, the ISP would charge the content provider a price p, a per-packet charge for the priority transmission of its packets. To keep the model tractable, we do not consider differential pricing that the ISP might use (Shapiro and Varian 1998). Then, the payoff function for the ISP is F under NN and $F + I _ { Y }$ $p \cdot \lambda \cdot x + I _ { G } \cdot p \cdot \lambda \cdot ( 1 - x )$ under NNN. A list of our notations is provided in Appendix A.

As shown in Figure 3, the timing of the game is as follows. The ISP announces the Internet access fee F to consumers and the preferential delivery charge p to content providers under NNN. Based on the announced fees, the two content providers decide simultaneously whether to pay the premium price for priority delivery of their content. After the ISP and the content providers make their respective decisions, consumers choose either content provider Y or content provider G. In the following sections, we use backward induction to deduce the subgame perfect Nash equilibria of the game with and without NN regulation.

Figure 3 The Sequence of Events in the Game

<table><tr><td>Stage 1</td><td>Stage 2</td><td>Stage 3</td></tr><tr><td>The broadband provider announces F and p</td><td>Content providers choose pay or not pay</td><td>Consumers choose content provider Y or content provider G</td></tr></table>

## NN

In this section, we analyze the model under NN where the ISP decides on the optimal Internet access fee F , and consumers choose between content providers Y and G. The content providers do not have any decision to make here.

## Content Decisions for Consumers

Although individual consumers choose contents between Y and G independently, the consumers’ decisions as a whole can be represented by the marginal consumer x with all the consumers located in 0- x choosing Y and all the consumers located in x- 1 choosing G. The subscript NN denotes the case of NN. Then, $x _ { \mathrm { N N } }$ denotes the marginal consumer who is indifferent between content provider Y and content provider G under NN and can be specified by

$$
\begin{array}{r l} & V (\lambda) - t x _ {\mathrm{NN}} - \frac {d \lambda}{\mu - \lambda} - F _ {\mathrm{NN}} \\ & \qquad = V (\lambda) - t (1 - x _ {\mathrm{NN}}) - \frac {d \lambda}{\mu - \lambda} - F _ {\mathrm{NN}}. \end{array}\tag{1}
$$

This leads to $\begin{array} { r } { x _ { \mathrm { N N } } = \frac { 1 } { 2 } . } \end{array}$ , implying equal market share for the two content providers. The payoff to content provider Y is $\Pi _ { \mathrm { N N \_ Y } } = x _ { \mathrm { N N } } \lambda r _ { Y } = \textstyle { \frac { 1 } { 7 } } \lambda r _ { Y }$ , and the payoff to content provider G is $\Pi _ { \mathrm { N N \mathrm { - } G } } = \mathsf { \bar { ( } 1 - } x _ { \mathrm { N N } } ) \lambda r _ { G } = \textstyle { \frac { 1 } { 2 } } \lambda r _ { G }$

## Pricing Decisions for the ISP

Under NN, Internet access fees collected from consumers are the only revenues for the ISP. Assume that the ISP has negligible running costs. Anticipating consumers’ choices, the ISP solves the profit maximization problem as follows:

$$
\begin{array}{r l} \max _ {F _ {\mathrm{NN}}} & \Pi_ {\mathrm{NN}} = F _ {\mathrm{NN}} \\ \text {s.t.} & U _ {\mathrm {NN\_Y}} (\tilde {x}) \geq 0, \quad 0 \leq \tilde {x} \leq x _ {\mathrm{NN}}, \\ & U _ {\mathrm {NN\_G}} (\tilde {x}) \geq 0, \quad x _ {\mathrm{NN}} \leq \tilde {x} \leq 1. \end{array}\tag{2}
$$

This leads to

$$
\Pi_ {\mathrm{NN}} = F _ {\mathrm{NN}} = V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda}.
$$

## NNN

Next, we analyze the situation when the ISP is allowed to charge the content providers for preferential treatment of the latter’s packets. Under NNN, the ISP charges the content provider $p$ per packet for priority over its competitor’s packets, should its competitor choose to not pay. When both content providers pay the price $p ,$ both their packets receive equal treatment.

## Content Decisions for Consumers

Given the ISP’s choices of $F , p ,$ and content providers choices $I _ { Y }$ and ${ \cal I } _ { G } ,$ consumers decide on their preferred content provider. Based on content providers’ choices, there are essentially four possible outcomes: neither content provider pays $( I _ { Y } = I _ { G } = 0 ) ;$ one content provider pays and the other does not (which results in two different outcomes, $I _ { Y } = 1 , I _ { G } = 0$ and $I _ { Y } = 0 ,$ $I _ { G } = 1 )$ ; and both content providers pay $( I _ { Y } = I _ { G } = 1 )$

Outcome 1. Both content providers opt for not paying the priority price $p _ { 1 } \ ( I _ { Y } = I _ { G } = 0 )$ . The indifferent consumer $x _ { 1 }$ is signaled by

$$
V (\lambda) - t x _ {1} - \frac {d \lambda}{\mu - \lambda} - F _ {1} = V (\lambda) - t (1 - x _ {1}) - \frac {d \lambda}{\mu - \lambda} - F _ {1},
$$

which leads to $\textstyle x _ { 1 } = { \frac { 1 } { 2 } } . ^ { 7 }$ Notice that this outcome amounts to the same result as in NN.

Outcome 2. Content provider Y pays $_ { p _ { 2 } , }$ , while content provider G chooses not to pay $( I _ { Y } = 1 , I _ { G } = 0 )$ . In Outcome 2, content provider $Y ^ { \prime } \mathrm { s }$ packets are prioritized and therefore face congestion only to the extent of the traffic from $\boldsymbol { Y } ,$ but content provider G’s packets are not, so that $G ^ { \prime } \mathrm { s }$ congestion is a function of the entire traffic. The marginal consumer $x _ { 2 }$ who is indifferent between content provider Y and content provider G under NNN in Outcome 2 is specified by

$$
\begin{array}{l} V (\lambda) - t x _ {2} - \frac {d \lambda}{\mu - x _ {2} \lambda} - F _ {2} \\ = V (\lambda) - t (1 - x _ {2}) - \frac {d \mu \lambda}{(\mu - x _ {2} \lambda) (\mu - \lambda)} - F _ {2}. \end{array}\tag{3}
$$

This leads to $\begin{array} { r } { x _ { 2 } > \frac { 1 } { 2 } } \end{array}$ (see Appendix B for the proof) meaning that content provider Y enjoys a larger market share $x _ { 2 }$ at the price of $p _ { 2 }$ . Notice that $\bar { G ^ { \prime } } s$ traffic faces delay costs of an $M / M / 1$ priority queue with preemption.

Outcome 3. This case is the opposite of Outcome 2. Content provider G decides to pay the preferential packet treatment price of $p _ { 3 }$ per packet, while content provider Y chooses not to pay $( I _ { Y } = 0 , ~ I _ { G } = 1 )$ . Carrying out a similar analysis, we denote the marginal consumer $x _ { 3 } ,$ who is indifferent between content provider Y and content provider G under NNN in Outcome 3 and is specified by

$$
\begin{array}{c} {V (\lambda) - t x _ {3} - \frac {d \mu \lambda}{[ \mu - (1 - x _ {3}) \lambda ] (\mu - \lambda)} - F _ {3}} \\ {= V (\lambda) - t (1 - x _ {3}) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} - F _ {3}.} \end{array}\tag{4}
$$

It follows that $x _ { 3 } ~ < ~ \frac { 1 } { 2 }$ - meaning that content provider G enjoys a larger market share $1 - x _ { 3 }$ at the price of $p _ { 3 }$ .

Outcome 4. Both content providers pay the priority price $p _ { 4 }$ to have their content delivered $( I _ { Y } = I _ { G } = 1 )$ Because both content providers’ packets are treated the same, this leads to $\begin{array} { r } { x _ { 4 } = x _ { 1 } = x _ { \mathrm { N N } } = \frac { 1 } { 2 } } \end{array}$

Delivery Service Decisions for Content Providers Given certain values of F and p, content providers Y and G decide whether to pay for the preferential delivery of data packets. Content provider $Y ^ { \prime } \mathrm { s }$ decision problem is represented by $\begin{array} { r l } { \operatorname* { m a x } _ { I _ { Y } } \{ r _ { Y } \cdot \lambda \cdot x ( I _ { Y } , I _ { G } ) - } & { { } } \end{array}$ $I _ { Y } \cdot p \cdot \lambda \cdot x ( I _ { Y } , I _ { G } ) \big \}$ , while content provider G’s decision problem is represented by max $\overset { \cdot } { \cdot } _ { I _ { G } } \bar { \{ }  r _ { G } \cdot \lambda \cdot [ 1 - x ( I _ { Y } , I _ { G } ) ] -$ $\hat { I } _ { G } \cdot p \cdot \lambda \cdot [ 1 \bar { - } x ( I _ { Y } , I _ { G } ) ] \}$ . Table 2 presents the payoff matrix for the content providers under the four outcomes.

Outcome 1. The revenues for content provider Y and G are $\Pi _ { \gamma 1 } = { \textstyle \frac { 1 } { 2 } } \lambda r _ { Y }$ and $\begin{array} { r } { \Pi _ { G 1 } = \frac { 1 } { 2 } \lambda r _ { G } , } \end{array}$ respectively. The incentive compatibility constraint for content provider Y is $\Pi _ { Y 1 } - \Pi _ { Y 2 } \geq 0 _ { \astrosun }$ , and the incentive compatibility constraint for content provider G is $\Pi _ { G 1 } { - } \bar { \Pi } _ { G 3 } \bar { \geq 0 }$

Outcome 2. The revenue for Y is $\Pi _ { Y 2 } = x _ { 2 } \lambda r _ { Y } -$ $x _ { 2 } \lambda p$ and the revenue for G is $\Pi _ { G 2 } = ( 1 - x _ { 2 } ) \lambda r _ { G }$ . The incentive compatibility constraint for content provider Y is $\Pi _ { Y 2 } - \bar { \Pi _ { Y 1 } } \geq 0$ , and the incentive compatibility constraint for content provider G is $\Pi _ { G 2 } - \mathbf { \hat { I } } \mathbf { I } _ { G 4 } \geq \dot { 0 } .$

Table 2 Content Providers’ Payoffs

<table><tr><td>Content provider decision</td><td>G does not pay</td><td>G pays</td></tr><tr><td rowspan="2">Y does not pay</td><td> $\Pi_{Y1} = \frac{1}{2}\lambda r_Y,$ </td><td> $\Pi_{Y3} = x_3\lambda r_Y,$ </td></tr><tr><td> $\Pi_{G1} = \frac{1}{2}\lambda r_G$ </td><td> $\Pi_{G3} = (1 - x_3)\lambda r_G - (1 - x_3)\lambda p$ </td></tr><tr><td rowspan="2">Y pays</td><td> $\Pi_{Y2} = x_2\lambda r_Y - x_2\lambda p,$ </td><td> $\Pi_{Y4} = \frac{1}{2}\lambda r_Y - \frac{1}{2}\lambda p,$ </td></tr><tr><td> $\Pi_{G2} = (1 - x_2)\lambda r_G$ </td><td> $\Pi_{G4} = \frac{1}{2}\lambda r_G - \frac{1}{2}\lambda p$ </td></tr></table>

These two incentive compatibility constraints can be reduced to

$$
p \leq \frac {x _ {2} - \frac {1}{2}}{x _ {2}} r _ {Y}\tag{5}
$$

and

$$
p \geq \frac {x _ {2} - \frac {1}{2}}{\frac {1}{2}} r _ {G}.\tag{6}
$$

Comparing the right-hand side (RHS) of constraints (5) and (6) leads to

$$
\frac {\mathrm{RHS} _ {(5)}}{\mathrm{RHS} _ {(6)}} = \frac {r _ {Y}}{2 x _ {2} r _ {G}} <   1
$$

since $\begin{array} { r } { x _ { 2 } > \frac { 1 } { 2 } } \end{array}$ and $r _ { G } > r _ { Y }$ . Thus, there is no feasible p such that content provider Y pays for the preferential delivery, while content provider G does not. Therefore Outcome 2 cannot be an equilibrium. Note that this result is driven by the fact (or more correctly, the assumption) that $r _ { G } > r _ { Y }$ . In other words, if $r _ { G } > r _ { Y } ,$ we can never have an outcome where content provider Y decides to pay and G does not. The assumption $r _ { G } > r _ { Y }$ does not affect the key results of our analyses. If, however, this assumption is reversed, then Outcome 3 instead of Outcome 2 cannot be an equilibrium.

Outcome 3. The revenues for Y and G are $\Pi _ { Y 3 } =$ $x _ { 3 } \lambda r _ { Y }$ and $\Pi _ { G 3 } = ( 1 - x _ { 3 } ) \lambda r _ { G } - ( 1 - x _ { 3 } ) \lambda p _ { . }$ , respectively. The incentive compatibility constraint for content provider Y is $\Pi _ { Y 3 } ^ { - } - \Pi _ { Y 4 } ^ { - } \geq 0$ and the incentive compatibility constraint for content provider G is $\Pi _ { G 3 } - \Pi _ { G 1 } \geq 0$ . These two incentive compatibility constraints can be reduced to

$$
p \geq \frac {1 / 2 - x _ {3}}{1 / 2} r _ {Y}\tag{7}
$$

and

$$
p \leq \frac {1 / 2 - x _ {3}}{1 - x _ {3}} r _ {G}.\tag{8}
$$

Comparing the RHS of (7) and (8) gives

$$
\frac {\mathrm{RHS} _ {(7)}}{\mathrm{RHS} _ {(8)}} = \frac {2 (1 - x _ {3}) r _ {Y}}{r _ {G}}.
$$

To analyze the magnitude of this ratio, we consider two possibilities in the relative values of $r _ { G }$ and $r _ { Y } :$ Case I: $r _ { G } < 2 ( 1 - x _ { 3 } ) r _ { Y }$ and Case II: $r _ { G } \ge 2 ( 1 - x _ { 3 } ) r _ { Y }$ . If Case I holds, there is no feasible p such that content provider G pays for the preferential delivery and content provider Y does not, and therefore Outcome 3 cannot be an equilibrium. If Case II holds, Outcome 3 may be an equilibrium. We will further analyze the equilibrium results in the next subsection (i.e., Stage 1 of the game).

Outcome 4. In this case, content providers Y and G get the same revenues (i.e., $\scriptstyle { \frac { 1 } { 2 } } \lambda r _ { Y }$ and $\scriptstyle { \frac { 1 } { 2 } } \lambda r _ { G }$ for Y and $G ,$ respectively) as those in Outcome 1. Both content providers, however, incur an extra expense of ${ \scriptstyle { \frac { 1 } { 2 } } } \lambda p ,$ , which was paid to the ISP. The incentive compatibility constraint for content provider Y is $\Pi _ { \gamma _ { 4 } } -$ $\Pi _ { Y 3 } \ge 0$ and the incentive compatibility constraint for content provider G is $\Pi _ { G 4 } \bar { - } \Pi _ { G 2 } \bar { \geq 0 }$ . We note that Outcome 4 is a classical prisoner’s dilemma that has been described in other contexts (Brander and Spencer 1983, Roller and Tombak 1990)—both content providers know that they would be better off by not paying, but given the relative proximity of their per consumer revenue streams, they end up paying the ISP.

## Pricing Decisions for the ISP

Expecting the best responses of both content providers and consumers, the ISP analyzes the maximum profit that he can make under the various permutations of the choices of the content providers to pay him (recall that the content providers can decide either to pay or not pay the priority delivery charges) and the corresponding consumers’ choices represented by the marginal consumer x.

Outcome 1. Both content providers opt to not pay the priority price $p _ { 1 } ( I _ { Y } = I _ { G } = 0 )$ . Similar to the NN case, the Internet access fees collected from consumers is the only revenue for the ISP. The broadband provider solves the following profit-maximization problem:

$$
\begin{array}{l l} \max _ {F _ {1}, p _ {1}} & \Pi_ {1} = F _ {1} \\ \text {s.t.} & U _ {\mathrm {NNN\_Y}} (\tilde {x}, I _ {Y}, I _ {G}) \geq 0, \quad 0 \leq \tilde {x} \leq x _ {1}, \\ & U _ {\mathrm {NNN\_G}} (\tilde {x}, I _ {Y}, I _ {G}) \geq 0, \quad x _ {1} \leq \tilde {x} \leq 1, \\ & \Pi_ {Y 1} - \Pi_ {Y 2} \geq 0, \\ & \Pi_ {G 1} - \Pi_ {G 3} \geq 0. \end{array}\tag{9}
$$

The first two constraints are participation constraints for consumers of content provider Y and $G ,$ respectively. The last two constraints are incentive compatibility constraints for the content providers. The consumers’ participation constraints can be reduced to

$$
p _ {1} \geq \left(\frac {x _ {2} - 1 / 2}{x _ {2}}\right) r _ {Y} \quad \text { and } \quad p _ {1} \geq \left(\frac {1 / 2 - x _ {3}}{1 - x _ {3}}\right) r _ {G}.
$$

Since $\begin{array} { r } { x _ { 2 } - \frac 1 2 = \frac 1 2 - x _ { 3 } } \end{array}$ (this is shown to be true in Outcome 3, which is discussed later) and $r _ { G } > r _ { Y }$

$$
\left(\frac {1 / 2 - x _ {3}}{1 - x _ {3}}\right) r _ {G} \geq \left(\frac {x _ {2} - 1 / 2}{x _ {2}}\right) r _ {Y},
$$

which implies that the ISP’s optimal preferential delivery charge can be specified as

$$
p _ {1} \geq \left(\frac {1 / 2 - x _ {3}}{1 - x _ {3}}\right) r _ {G}.
$$

Therefore the results of the profit-maximization problem of the ISP in Outcome 1 are the ISP makes a profit of

$$
\Pi_ {1} = F _ {1} = V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda}
$$

and charges the content providers a fee $p _ { 1 }$ such that

$$
p _ {1} \geq \left(\frac {1 / 2 - x _ {3}}{1 - x _ {3}}\right) r _ {G}.
$$

The best response for both content provider Y and content provider G is not to pay the fee.

Outcome 2. Content provider Y pays ${ \displaystyle p _ { 2 } , }$ while content provider G chooses not to pay $( \dot { I _ { Y } } = 1 , I _ { G } = 0 )$ . In addition to the revenue from end users, the ISP also gains revenue from content provider $Y$ for preferential delivery of $Y ^ { \prime } \mathrm { s }$ content. The broadband provider’s profit-maximization problem is thus

$$
\begin{array}{l l} \max _ {F _ {2}, p _ {2}} & \Pi_ {2} = F _ {2} + x _ {2} \lambda p _ {2} \\ \text {s.t.} & U _ {\mathrm {NNN\_Y}} (\tilde {x}, I _ {Y}, I _ {G}) \geq 0, \quad 0 \leq \tilde {x} \leq x _ {2}, \\ & U _ {\mathrm {NNN\_G}} (\tilde {x}, I _ {Y}, I _ {G}) \geq 0, \quad x _ {2} \leq \tilde {x} \leq 1, \\ & \Pi_ {Y 2} - \Pi_ {Y 1} \geq 0, \\ & \Pi_ {G 2} - \Pi_ {G 4} \geq 0. \end{array}\tag{10}
$$

The first two constraints are the participation constraints of the consumers who prefer G and the consumers who prefer $\boldsymbol { Y } ,$ respectively. The last two constraints ensure that while content provider Y will pay, content provider G will not. As discussed in the second stage of the game, there is no feasible $p _ { 2 }$ to induce Outcome 2.

Outcome 3. Content provider G pays $p _ { 3 } ,$ , while content provider Y chooses not to pay $( I _ { Y } = 0 , ~ I _ { G } = 1 )$ . The ISP’s profit-maximization problem is given by

$$
\begin{array}{r l} \underset {F _ {3}, p _ {3}} {\max} & \Pi_ {3} = F _ {3} + (1 - x _ {3}) \lambda p _ {3} \\ \mathrm{s.t.} & U _ {\mathrm {NNN\_Y}} (\tilde {x}, I _ {Y}, I _ {G}) \geq 0, \quad 0 \leq \tilde {x} \leq x _ {3}, \\ & U _ {\mathrm {NNN\_G}} (\tilde {x}, I _ {Y}, I _ {G}) \geq 0, \quad x _ {3} \leq \tilde {x} \leq 1, \\ & \Pi_ {Y 3} - \Pi_ {Y 4} \geq 0, \\ & \Pi_ {G 3} - \Pi_ {G 1} \geq 0. \end{array}\tag{11}
$$

The first two constraints are the consumers’ participation constraints, while the last two ensure that this outcome actually holds—i.e., Y does not pay, but G does. Recall the two cases discussed in content providers’ decisions. If Case I holds, i.e., $r _ { G } <$

$2 ( 1 - x _ { 3 } ) r _ { Y }$ there is no feasible $p _ { 3 }$ and Outcome 3 is not possible. If Case II holds, i.e., $r _ { G } \ge 2 ( 1 - x _ { 3 } ) r _ { Y }$ , the $\mathrm { I S P ^ { \prime } s }$ optimal choice of pricing strategy and its profits are given by the expressions

$$
\begin{array}{c} {F _ {3} = V (\lambda) - t (1 - x _ {3}) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda},} \\ {p _ {3} = \bigg (\frac {1 / 2 - x _ {3}}{1 - x _ {3}} \bigg) r _ {G}, \quad \mathrm{and}} \\ {\Pi_ {3} = F _ {3} + (1 - x _ {3}) \lambda p _ {3} = V (\lambda) - t (1 - x _ {3})} \\ {- \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} + \bigg (\frac {1}{2} - x _ {3} \bigg) \lambda r _ {G}.} \end{array}
$$

Outcome 4. Both content providers pay the priority price $p _ { 4 } \ ( I _ { Y } = I _ { G } = 1 )$ , so that neither content gets any relative advantage for delivery. The ISP now gains revenue from consumers, as well as both content providers, and therefore solves the following optimization problem:

$$
\begin{array}{r l} \max _ {F _ {4}, p _ {4}} & \Pi_ {4} = F _ {4} + \lambda p _ {4} \\ \text {s.t.} & U _ {\mathrm {NNN\_Y}} (\tilde {x}, I _ {Y}, I _ {G}) \geq 0, \quad 0 \leq \tilde {x} \leq x _ {4}, \\ & U _ {\mathrm {NNN\_G}} (\tilde {x}, I _ {Y}, I _ {G}) \geq 0, \quad x _ {4} \leq \tilde {x} \leq 1, \\ & \Pi_ {Y 4} - \Pi_ {Y 3} \geq 0, \\ & \Pi_ {G 4} - \Pi_ {G 2} \geq 0. \end{array}\tag{12}
$$

It follows that the ISP’s optimal pricing strategy is given by

$$
F _ {4} = V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} \quad \mathrm{and} \quad p _ {4} = (1 - 2 x _ {3}) r _ {\Upsilon},
$$

while his profit is

$$
\Pi_ {4} = F _ {4} + \lambda p _ {4} = V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} + (1 - 2 x _ {3}) \lambda r _ {\gamma}.
$$

We note that $r _ { G } \ge 2 ( 1 - x _ { 3 } ) r _ { Y }$ (i.e., Case II) is a necessary condition for Outcome 3 to be an equilibrium. When this condition is not satisfied, i.e., $r _ { G } < 2 ( 1 - x _ { 3 } ) r _ { Y }$ (Case I), we have only two potential equilibria (Outcomes 1 and 4). Recall further that Outcome 2 is never an equilibrium as long as $r _ { G } > r _ { Y }$

To determine his optimal pricing strategy $( F ^ { * } , p ^ { * } )$ the ISP compares the profits under the various outcomes and for a given set of parameter values, chooses its pricing strategy (which drives the equilibrium to one of the above-mentioned outcomes) to arrive at the highest profit. As the monopolist gatekeeper between the content providers and the customers, the ISP can essentially drive the direction of the equilibrium in such a way that it ensures the highest possible profits.

We can readily observe that $\Pi _ { 4 } > \Pi _ { 1 }$ in both Cases I and II. As a result, in Case I, the broadband provider will set the final $( F ^ { * } , p ^ { * } )$ to

$$
F ^ {*} = F _ {4} = V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda}, p ^ {*} = p _ {4} = (1 - 2 x _ {3}) r _ {\gamma},
$$

and realize the profit

$$
\Pi^ {*} = \Pi_ {4} = V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} + (1 - 2 x _ {3}) \lambda r _ {Y}
$$

because Outcomes 1 and 4 are the only two potential equilibria.

In Case II, the ISP needs to compare $\Pi _ { 3 }$ with $\Pi _ { 4 }$ to determine the outcome that gives the maximum profit, which leads to the following comparison:

$$
\begin{array}{l} \Pi_ {3} - \Pi_ {4} \\ = \left[ V (\lambda) - t (1 - x _ {3}) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} + \left(\frac {1}{2} - x _ {3}\right) \lambda r _ {G} \right] \\ - \left[ V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} + (1 - 2 x _ {3}) \lambda r _ {Y} \right] \\ = \left(\frac {1}{2} - x _ {3}\right) [ \lambda r _ {G} - 2 \lambda r _ {Y} - t (1 - 2 x _ {3}) ] \end{array}
$$

after applying Equation (4) and some algebra.

We observe that if $\begin{array} { r } { r _ { G } \geq 2 r _ { Y } + \frac { t } { \lambda } ( 1 - 2 x _ { 3 } ) . } \end{array}$ , then $\Pi _ { 3 } \geq \Pi _ { 4 }$ . The broadband provider will then set the menu of prices $( F ^ { * } , p ^ { * } )$ to

$$
\begin{array}{c} F ^ {*} = F _ {3} = V (\lambda) - t (1 - x _ {3}) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda}, \\ p ^ {*} = p _ {3} = \bigg (\frac {1 / 2 - x _ {3}}{1 - x _ {3}} \bigg) r _ {G}, \end{array}
$$

and will realize the profit

$$
\Pi^ {*} = \Pi_ {3} = V (\lambda) - t (1 - x _ {3}) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} + \left(\frac {1}{2} - x _ {3}\right) \lambda r _ {G}.
$$

Conversely, if $\begin{array} { r } { r _ { G } < 2 r _ { Y } + \frac { t } { \lambda } ( 1 - 2 x _ { 3 } ) } \end{array}$ , then $\Pi _ { 3 } < \Pi _ { 4 } .$ The broadband provider will then set the menu of prices $( F ^ { * } , p ^ { * } )$ to

$$
F ^ {*} = F _ {4} = V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda}
$$

and $p ^ { * } = p _ { 4 } = ( 1 - 2 x _ { 3 } ) r _ { Y }$ to attain a profit of

$$
\Pi^ {*} = \Pi_ {4} = V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} + (1 - 2 x _ {3}) \lambda r _ {\gamma}.
$$

Note that the condition that ensures the ISP to realize more profit in Outcome 3 than Outcome 4 also satisfies the condition for Outcome 3 to be feasible since

$$
2 r _ {Y} + \frac {t}{\lambda} (1 - 2 x _ {3}) > 2 (1 - x _ {3}) r _ {Y}.
$$

We thus simplify the combination of the profit comparison condition (between Outcomes 3 and 4) and the feasibility condition of Outcome 3 into the following two cases (see Table 3).

Case A: $r _ { G } \ge 2 r _ { \gamma }$

$$
F ^ {*} = F _ {3} ^ {*} = V (\lambda) - t (1 - x _ {3}) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda}
$$

$$
+ \frac {t}{\lambda} (1 - 2 x _ {3})
$$

$$
p ^ {*} = p _ {3} ^ {*} = \left(\frac {1 / 2 - x _ {3}}{1 - x _ {3}}\right) r _ {G}
$$

$$
\begin{array}{r l} & {\Pi^ {*} = \Pi_ {3} ^ {*} = V (\lambda) - t (1 - x _ {3})} \\ & {- \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} + \bigg (\frac {1}{2} - x _ {3} \bigg) \lambda r _ {G}} \end{array}
$$

Case B: $r _ { G } < 2 r _ { Y }$

$$
+ \frac {t}{\lambda} (1 - 2 x _ {3})
$$

$$
F ^ {*} = F _ {4} ^ {*} = V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda}
$$

$$
\Pi^ {*} = \Pi_ {4} ^ {*} = V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} + (1 - 2 x _ {3}) \lambda r _ {\gamma}
$$

Case A. Outcome 3 is not only feasible but also more profitable to the ISP than Outcome 4. Therefore, Outcome 3 is the equilibrium. The required condition for Case A is

$$
r _ {G} \geq 2 r _ {Y} + \frac {t}{\lambda} (1 - 2 x _ {3}).\tag{13}
$$

Case B. Either Outcome $^ 3$ is not feasible, or when Outcome 3 is feasible, Outcome 4 is more profitable. Therefore, Outcome 4 is the equilibrium. The required condition for Case B is

$$
r _ {G} <   2 r _ {Y} + \frac {t}{\lambda} (1 - 2 x _ {3}).\tag{14}
$$

Figure 4 summarizes these results graphically by plotting $r _ { G }$ against $r _ { Y }$ (see also Table 3). The $\mathrm { \bar { \mathrm { I S P ^ { \prime } s } } }$ choice of the equilibrium in the game between the two content providers is dictated by the relative magnitudes of their revenue-generation capabilities. In Region A (corresponding to Case $\mathrm { A } ) ,$ , where $r _ { G }$ is $s i g \mathbf { \varepsilon } -$ nificantly greater than $r _ { Y } ,$ , the ISP chooses its pricing strategy in such a way as to drive the game to Outcome 3, where the content provider with higher profitability has the incentive to pay for priority delivery, while the content provider with lower profitability does not have the incentive to pay that fee. Conversely, in Region B (corresponding to Case B) where the content providers have more comparable revenue rates, the game will end up with Outcome 4, when both content providers pay the ISP the priority delivery fee.

Figure 4 Graphical Representation of the Regions for Arriving at Different Equilibria of the Game When $r _ { G } > r _ { Y }$  
![](/api/attachments/H7EMY5BU/fulltext/images/d1aefbc8a60a3cef11032215720df682753b7a48ba762b6c2539dd1d645b9730.jpg)

Table 3 ISP’s Optimal Pricing Decisions and Profits in Regions A and B  
Figure 5 Generalized Representation of the Regions for Arriving at Different Equilibria of the Game  
![](/api/attachments/H7EMY5BU/fulltext/images/81a8b597f47c1d219e5d14956d37fe9370d48e531083d951dbe7ec33d7dde67d.jpg)

The choice of making $r _ { G } > r _ { Y }$ is simply a matter of convenience of exposition, that the generalized results are symmetric on either side of the line $r _ { G } = r _ { Y } ,$ , as indicated in Figure 5. We can interpret Regions C and D analogously, as we did with Regions A and B.

## Gainers and Losers—Comparison Between NN and NNN

In this section, we consider the resulting surpluses for the various players. These results can then be used by the policy maker who has to decide whether to allow the ISP to charge for preferential service (i.e., opt for NNN), or continue to maintain the NN status quo. The policy maker can proceed to compare the equilibrium under NN and NNN, by evaluating the payoff for the ISP and content providers, consumer surplus, and social welfare under each regime.

From the $\mathrm { I S P } ^ { \prime } \mathrm { s }$ point of view, NNN is preferred to NN because the profits in either Case A or Case $\scriptstyle \mathrm { \mathrm { B } , }$ $\Pi _ { 3 } ^ { * }$ or $\Pi _ { 4 } ^ { * } ,$ are higher than $\Pi _ { \mathrm { N N } } ^ { * }$ . What is of interest to the policy maker is whether the other participants gain from this arrangement too and whether social welfare as a whole increases. The results of this analysis are summarized in the following proposition.

Proposition 1 (Gainers and Losers in the Short Run). The economic outcomes in the short run under NN and NNN vary. Specifically, using NN as the benchmark,

Table 4 Comparison of Various Economic Outcomes of Interest Under NN and NNN

<table><tr><td>Variable</td><td>NN (benchmark)</td><td>NNN (Case A: Only G pays)</td><td>NNN (Case B: Both Y and G pay)</td></tr><tr><td>F</td><td> $F_{NN} = V(\lambda) - \frac{t}{2} - \frac{d\lambda}{\mu - \lambda}$ </td><td> $F_{NNN\_A} = F_3 = V(\lambda) - t(1 - x_3) - \frac{d\lambda}{\mu - (1 - x_3)\lambda} < F_{NN}$ Lower</td><td> $F_{NNN\_B} = F_4 = V(\lambda) - \frac{t}{2} - \frac{d\lambda}{\mu - \lambda} = F_{NN}$ Unchanged</td></tr><tr><td>p</td><td>N/A</td><td> $p_{NNN\_A} = p_3 = \left( \frac{1/2 - x_3}{1 - x_3} \right)r_G$ </td><td> $p_{NNN\_B} = p_4 = (1 - 2x_3)r_Y$ </td></tr><tr><td>ISP&#x27;s revenue</td><td> $\Pi_{NN\_ISP} = F_{NN} = V(\lambda) - \frac{t}{2} - \frac{d\lambda}{\mu - \lambda}$ </td><td> $\Pi_{NNN\_A\_ISP} = \Pi_3$  $= V(\lambda) - t(1 - x_3) - \frac{d\lambda}{\mu - (1 - x_3)\lambda}$  $+ \left( \frac{1}{2} - x_3 \right) \lambda r_G > \Pi_{NN}$ Better off</td><td> $\Pi_{NNN\_B\_ISP} = \Pi_4$  $= V(\lambda) - \frac{t}{2} - \frac{d\lambda}{\mu - \lambda}$  $+ (1 - 2x_3) \lambda r_Y > \Pi_{NN}$ Better off</td></tr><tr><td>Content providerY&#x27;s profit</td><td> $\Pi_{NN\_Y} = \frac{1}{2}\lambda r_Y$ </td><td> $\Pi_{NNN\_A\_Y} = x_3 \lambda r_Y < \Pi_{NN\_Y}$ Worse off</td><td> $\Pi_{NNN\_B\_Y} = x_3 \lambda r_Y < \Pi_{NN\_Y}$ Worse off</td></tr><tr><td>Content providerG&#x27;s profit</td><td> $\Pi_{NN\_G} = \frac{1}{2}\lambda r_G$ </td><td> $\Pi_{NNN\_A\_G} = \frac{1}{2}\lambda r_G = \Pi_{NN\_G}$ Unchanged</td><td> $\Pi_{NNN\_B\_G} = \frac{1}{2}\lambda [r_G - (1 - 2x_3)r_Y] < \Pi_{NN\_G}$ Worse off</td></tr><tr><td>Consumer surplus</td><td> $CS_{NN} = \frac{t}{4}$ </td><td> $CS_{NNN\_A} = t(x_3^2 - x_3 + \frac{1}{2}) > CS_{NN}$ Better off</td><td> $CS_{NNN\_B} = \frac{t}{4} = CS_{NN}$ Unchanged</td></tr><tr><td>Social welfare</td><td> $SW_{NN} = V(\lambda) - \frac{t}{4} - \frac{d\lambda}{\mu - \lambda}$  $+ \frac{1}{2}\lambda r_Y + \frac{1}{2}\lambda r_G$ </td><td> $SW_{NNN\_A}$  $= V(\lambda) - t\left( \frac{1}{2} - x_3^2 \right) - \frac{d\lambda}{\mu - (1 - x_3)\lambda}$  $+ x_3 \lambda r_Y + (1 - x_3) \lambda r_G > SW_{NN}$ Increased</td><td> $SW_{NNN\_B} = V(\lambda) - \frac{t}{4} - \frac{d\lambda}{\mu - \lambda}$  $+ \frac{1}{2}\lambda r_Y + \frac{1}{2}\lambda r_G = SW_{NN}$ Unchanged</td></tr></table>

Note. The bold and italicized text shows how those economic outcomes change when moving from NN to NNN.

(1) Social welfare would either increase or remain unchanged, depending on parameter values as stated in conditions (13) and (14). Likewise, consumer surplus would increase or remain unchanged.

(2) Content providers are usually worse off under NNN except under condition (13) when the content provider paying the priority delivery fee has the same surplus as under NN.

(3) The ISP is unambiguously better off.

## <sup>Proof.</sup> See Appendix C.

These results are organized in Table 4. Appendix C contains the details of their derivation.

Clearly, the gains of abolishing NN are not experienced equally. While the monopolist ISP gains if NNN were in place (in both Cases A and B of Table 4), the content providers are definitely worse off under this arrangement. Only content provider $G ^ { \prime } \mathrm { s }$ surplus is unchanged under Case A. Note that G does not get to enjoy the increase in the number of consumers, because the extra rent is fully extracted by the ISP. It is therefore no wonder why the content providers and the ISPs have been on the opposite sides of the NN debate.

The fate of the end consumers is more nuanced. If the two content providers do not differ significantly (Regions B or D in Figure 5) in terms of their revenue generation rates, the consumer surplus is unchanged. Consumers as a whole do stand to gain if one content provider is significantly better than the other in revenue generation (Regions A and C in Figure 5). This increase in overall consumer surplus, however, is derived at the expense of the group of consumers whose content provider does not pay the priority charge, a result contrary to the assertion of the ISPs that no consumer would be left worse off under the new arrangement (WSJ 2006).

Social welfare as a whole, in contrast, is at least as high under NNN as it is under NN, and is sometimes higher. Under NNN Case B, social welfare (like consumer surplus) does not change, but there is a transfer of wealth from the content providers to the ISP. This transfer is made possible by the priority delivery charge that the ISP extracts from both content providers, because the subscription fee to end users does not change $( F _ { 4 } ^ { * } = F _ { 1 } ^ { * } )$ . Under NNN Case A, the consumer surplus increases because of the most part of the lower subscription fees for all consumers $\bar { ( } F _ { 3 } ^ { * } < F _ { 1 } ^ { * } )$ . The winners under this arrangement are the consumers of content provider G (who are a majority) and the ISP, while the losers are the consumers of content provider $Y$ and content provider Y itself. Content provider $G ^ { \prime } \mathrm { s }$ surplus from the additional consumers that have migrated from Y is fully siphoned away by the ISP.

## Capacity Expansion Decision—Does NN Hinder the Broadband Service Provider’s Incentive to Expand Infrastructure Capacity?

The other key question for the policy maker is the ISP’s motivation to expand capacity under NN. To discuss this question, we consider the long-run problem, where the ISP can choose its capacity $\mu .$

Let C	 be the cost associated with capacity $\mu .$ The long-run problem can be modeled as a threestage game, where the ISP chooses capacity $\mu$ and announces the Internet access fee F to consumers and preferential delivery fee p to content providers under NNN in the first stage. Based on the announced fees, in the second stage, content providers choose whether to pay or not pay for preferential delivery, and in the third stage, consumers choose between content provider Y and content provider G. In the long-run problem, we also need to consider the cost of capacity expansion (this was not an issue in the preceding analysis, because in the short run, the existing network capacity is fixed).

Our objective is to determine the ISP’s incentive to expand capacity and its optimal capacity decision under NN and NNN, and compare the two meaningfully to find the regime under which the incentive for the ISP to expand capacity is higher. Finally, the choice of regime (NN or NNN) is not under the control of the ISP, and is a choice that lies with the policy makers (who can calculate the aforementioned incentives).

We observe that evaluating the incentive to expand for the ISP is different from calculating just the magnitude of its profit.<sup>8</sup> Furthermore, there is a crucial distinction between whether the ISP has incentive to expand the capacity and whether the ISP should expand the capacity as suggested in Jamison and Hauge (2007).<sup>9</sup>

We go through a process similar to that employed in analyzing the short-run problem to investigate the ISP’s incentive to expand capacity and his optimal capacity choice.

## Decisions for Both Content Providers and

## Consumers in the Capacity Expansion Problem Consumers in the Capacity Expansion Problem

Given certain $F , \ p ,$ and $\mu ,$ the analysis of the best responses for content providers and consumers do not differ from those in the short-term problem, and is therefore not repeated here. The content providers’ profits and consumers’ utilities in the longrun problem will be multiplied by ${ \frac { 1 } { 1 - \delta } } ,$ , where  is the discount factor. In other words, the content providers long-run profits are $\begin{array} { r } { \pi _ { Y i } = \frac { 1 } { 1 - \delta } \Pi _ { Y i } } \end{array}$ for Y and $\pi _ { G i } =$ $\textstyle { \frac { 1 } { 1 - \delta } } { \bar { \Pi } } _ { G i }$ for $G ,$ where $i ( = 1 , 2 , \bar { 3 } , 4 )$ represents the four different outcomes. The long-run utility of an arbitrary consumer $\tilde { x } \in [ 0 , 1 ]$ is $\begin{array} { r } { u _ { Y } ( \tilde { x } ) = \frac { 1 } { 1 - \delta } U _ { Y } ( \tilde { x } ) } \end{array}$ if content provider Y is chosen and is $\begin{array} { r } { u _ { G } ( \tilde { x } ) = \frac { \tilde { 1 } } { 1 - \delta } U _ { G } ( \tilde { x } ) } \end{array}$ if content provider G is chosen.

## Pricing and Capacity Expansion Decisions for the ISP in the Capacity Expansion Problem

Expecting the best responses of content providers and consumers, we evaluate the optimal decision $( F ^ { * } , p ^ { * } , \mu ^ { * } )$ for the ISP.

Under NN or Outcome 1. $\begin{array} { r } { x _ { 1 } = \frac { 1 } { 2 } . } \end{array}$ The ISP solves the following problem:

$$
\begin{array}{r l} \max _ {F _ {1}, p _ {1}, \mu_ {1}} & \pi_ {1} = \frac {1}{1 - \delta} F _ {1} - C (\mu_ {1}) \\ \text {s.t.} & u _ {\mathrm {NNN\_Y}} (\tilde {x}, I _ {Y}, I _ {G}) \geq 0, \quad 0 \leq \tilde {x} \leq x _ {1}, \\ & u _ {\mathrm {NNN\_G}} (\tilde {x}, I _ {Y}, I _ {G}) \geq 0, \quad x _ {1} \leq \tilde {x} \leq 1, \\ & \pi_ {Y 1} - \pi_ {Y 2} \geq 0, \\ & \pi_ {G 1} - \pi_ {G 3} \geq 0, \end{array}
$$

where $x _ { 2 }$ and $x _ { 3 }$ are as defined in Outcomes 2 and 3.

The long-run objective function represents the net cash flow for the ISP. We know that the first constraint is binding: i.e.,

$$
F _ {1} ^ {*} = V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu_ {1} ^ {*} - \lambda}.
$$

The optimal capacity $\mu _ { 1 } ^ { * }$ can be derived by maximizing the long-term net cash flow

$$
\pi_ {1} ^ {*} = \frac {1}{1 - \delta} \bigg [ V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu_ {1} ^ {*} - \lambda} \bigg ] - C (\mu_ {1} ^ {*}).
$$

Equation (15) gives the first-order condition of this optimization problem.

$$
\frac {\partial \pi_ {1}}{\partial \mu} = \frac {1}{1 - \delta} \cdot \frac {d \lambda}{(\mu - \lambda) ^ {2}} - \frac {\partial C (\mu)}{\partial \mu} = 0.\tag{15}
$$

The term $\displaystyle \frac { \partial \pi _ { 1 } } { \partial \mu }$ is the marginal increase in profit of the ISP with respect to $\mu ,$ and as such, we can interpret this term as the $\mathrm { I S P } ^ { \prime } \mathrm { s }$ incentive to expand capacity.

Outcome 2. It can be proved analogously as discussed earlier in the short-run problem that given the nature of the parameter values, this outcome is not possible.

Outcome 3. $\begin{array} { r } { x _ { 3 } < \frac { 1 } { 2 } } \end{array}$ - determined by

$$
\begin{array}{c} t x _ {3} + \frac {d \mu_ {3} \lambda}{[ \mu_ {3} - (1 - x _ {3}) \lambda ] (\mu_ {3} - \lambda)} \\ = t (1 - x _ {3}) + \frac {d \lambda}{\mu_ {3} - (1 - x _ {3}) \lambda}. \end{array}
$$

As before,

$$
\begin{array}{c} F _ {3} ^ {*} = V (\lambda) - t (1 - x _ {3}) - \frac {d \lambda}{\mu_ {3} ^ {*} - (1 - x _ {3}) \lambda}, \quad \text { and } \\ p _ {3} ^ {*} = \bigg (\frac {1 / 2 - x _ {3}}{1 - x _ {3}} \bigg) r _ {G}. \end{array}
$$

The ISP will choose the optimal capacity $\mu _ { 3 } ^ { * }$ to maximize the long-term net cash flows once again:

$$
\begin{array}{c} \pi_ {3} ^ {*} = \frac {1}{1 - \delta} \bigg [ V (\lambda) - t (1 - x _ {3}) - \frac {d \lambda}{\mu_ {3} ^ {*} - (1 - x _ {3}) \lambda} \\ \qquad \qquad + \left(\frac {1}{2} - x _ {3}\right) \lambda r _ {G} \bigg ] - C (\mu_ {3} ^ {*}) \\ = \frac {1}{1 - \delta} \bigg [ V (\lambda) - \frac {1}{2} t + \left(\frac {1}{2} - x _ {3}\right) \\ \qquad \cdot \left(\lambda r _ {G} - 2 t \frac {\mu}{\lambda} + t\right) \bigg ] - C (\mu_ {3} ^ {*}). \end{array}
$$

Then, $\mu _ { 3 } ^ { * }$ can be characterized by the first-order condition in Equation (16):

$$
\begin{array}{c} \frac {\partial \pi_ {3}}{\partial \mu} = \frac {1}{1 - \delta} \bigg [ t \bigg (\frac {2 \mu}{\lambda} - 1 \bigg) - \lambda r _ {G} \bigg ] \frac {\partial x _ {3}}{\partial \mu} - \frac {1}{1 - \delta} \\ \cdot \frac {2 t}{\lambda} \bigg (\frac {1}{2} - x _ {3} \bigg) - \frac {\partial C (\mu)}{\partial \mu} = 0. \end{array}\tag{16}
$$

Outcome 4.

$$
x _ {4} = \frac {1}{2}, F _ {4} ^ {*} = V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu_ {4} ^ {*} - \lambda} \quad \text { and } \quad p _ {4} ^ {*} = (1 - 2 x _ {3}) r _ {\gamma}.
$$

Similarly, the corresponding net cash flows are given by

$$
\pi_ {4} ^ {*} = \frac {1}{1 - \delta} \left[ V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu_ {4} ^ {*} - \lambda} + (1 - 2 x _ {3}) \lambda r _ {Y} \right] - C (\mu_ {4} ^ {*})
$$

Figure 6 ISP’s Incentive to Expand Capacity

![](/api/attachments/H7EMY5BU/fulltext/images/2081887fa6e1f99ece03196b855e6bd763c3c97e14f338792474cce308fb7a12.jpg)

and $\mu _ { 4 } ^ { * }$ is the solution of Equation (17):

$$
\frac {\partial \pi_ {4}}{\partial \mu} = \frac {1}{1 - \delta} \cdot \frac {d \lambda}{(\mu - \lambda) ^ {2}} - \frac {2}{1 - \delta} \cdot \frac {\partial x _ {3}}{\partial \mu} \lambda r _ {\gamma} - \frac {\partial C (\mu)}{\partial \mu} = 0.\tag{17}
$$

Comparing the ISP’s incentive to expand capacity under NNN (either $\displaystyle \frac { \partial \pi _ { 3 } } { \partial \mu }$ or $\textstyle { \frac { \partial \pi _ { 4 } } { \partial \mu } } \Biggr )$ to that under NN, the ISP has more incentive to expand capacity under NN when

$$
r _ {G} <   2 r _ {Y} + \frac {t}{\lambda} (1 - 2 x _ {3}) \quad \text { or } \quad r _ {G} \geq \frac {2 t}{\lambda} (1 - 2 x _ {3}),\tag{18}
$$

and the ISP has more incentive to expand capacity under NNN when

$$
2 r _ {Y} + \frac {t}{\lambda} (1 - 2 x _ {3}) \leq r _ {G} <   \frac {2 t}{\lambda} (1 - 2 x _ {3}).\tag{19}
$$

These conditions are graphed in Figure 7 with condition (18) corresponding to the shaded area and condition (19) corresponding to the unshaded area.

Figure 7 Graphical Representation of the Region for Arriving at a Different Equilibrium of the Long-Run When Capacity Is Expanded from $\mu _ { 1 }$ to $\mu _ { 2 }$

![](/api/attachments/H7EMY5BU/fulltext/images/28f573c0fe5d197a8d1fbc1e4349d2eaaba49ce916e479b41b14673c3fa0a061.jpg)  
Notes. In the shaded region, the ISP has higher incentive to expand capacity, and the optimal capacity level is higher under NN. In the white region, the ISP has lower incentive to expand capacity, and the optimal capacity level is lower under NN.

The following proposition summarizes the result concerning ISP’s incentive to expand infrastructure capacity.

Proposition 2 (ISP’s Incentive to Expand Infrastructure Capacity). Except for the region defined in condition (19), the ISP has more incentive to expand capacity under NN.

## <sup>Proof.</sup> See Appendix F.

To understand the nature of the result in Figure $^ { 7 , }$ note that the capacity costs under NN and NNN are identical given any same capacity level. Hence we only need to focus on the revenue of the ISP. Furthermore, under NN, the ISP’s revenue

$$
\frac {1}{1 - \delta} \bigg [ V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} \bigg ]
$$

is derived solely from the consumers, while the ISP’s revenue under NNN has two components: (1) the contribution from the consumers and (2) the contribution from the content providers. The revenue contribution from consumers increases in $\mu$ (as consumers enjoy reduced congestion), while the revenue contribution from the content providers decrease in $\mu$ (as the content providers have a reduced willingness to pay for priority delivery when congestion is reduced). Specifically, when both content providers pay (Regions B and D in Figure 7), the ISP’s long-run revenue from consumers is

$$
\frac {1}{1 - \delta} \bigg [ V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} \bigg ],
$$

which increases in $\mu .$ The ISP’s long-run revenue from the content providers is $\begin{array} { r } { \frac { 1 } { 1 - \delta } ( 1 - \breve { 2 } x _ { 3 } ) \lambda r _ { Y } , } \end{array}$ , which decreases in $\mu .$ Thus, by increasing the capacity $\mu ,$ the ISP platform gains from the consumers’ side and loses from the content providers’ side. Because the gains under NN and NNN (Case B) are the same and the ISP incurs a loss from the content providers’ side under NNN from expanding the infrastructure capacity, the ISP will almost always have a higher incentive to increase capacity under NN.

When only one content provider pays (Region A or C in Figure 7), and the contribution from the consumers is

$$
\frac {1}{1 - \delta} \bigg [ V (\lambda) - t (1 - x _ {3}) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} \bigg ],
$$

which increases in $\mu$ and the contribution from the content providers is

$$
\frac {1}{1 - \delta} \left(\frac {1}{2} - x _ {3}\right) \lambda r _ {G},
$$

which decreases in $\mu .$ The ISP gains from the consumers’ side and loses from the content providers’ side when increasing capacity $\mu ,$ a result similar to that in the case where both content providers pay. It is only in the small unshaded area in Figure 7 that under condition (19), the gain outweighs the loss to give the ISP more incentive to expand the capacity under NNN.

From the policy maker’s perspective, the questions of utmost interest concern the ISP’s optimal capacity choices under NN and NNN, and whether the ISP’s optimal capacity choices under NN and NNN are socially optimal. The following two propositions provide useful guidance to the policy maker in addressing these questions.

Proposition 3 (ISP’s Optimal Capacity Choice). Except for the region defined in condition (19), the optima capacity choice under NN is higher than that under NNN.

<sup>Proof:</sup> See Appendix G.

Proposition 4 (Whether ISP’s Optimal Capacity Choice Is Socially Optimal?). The ISP always invests at the socially optimal level under NN. Abolishing NN results in underinvestment in infrastructure capacity by the ISP when both content providers pay the priority delivery charge, and either underinvestment or overinvestment when only one content provider pays the priority charge.

<sup>Proof:</sup> See Appendix H.

A corollary of Propositions 3 and 4 is that while the ISP’s optimal capacity choice might be higher under NNN than NN in some specific instances, this higher capacity choice reduces social welfare. As an aside, as the ISP’s capacity increases, the parameter space for Outcome 3 becomes bigger in the expense of Outcome 4 (i.e., the line separating the two outcomes squeezes out Region B as shown in Figure 6). The intuition is straightforward: notably, as capacity increases, congestion goes down and some customers of G prefer Y , which therefore has a lesser incentive to pay, thus making Outcome 3 more probable and therefore making it possible for a switch in equilibrium from Outcome 4 to Outcome 3).

The comparative statics for the various pricing variables and the surpluses of the various parties involved with respect to the capacity $\mu$ are summarized in Table 5.

## Conclusion—Policy Implications and Directions for Further Research

The absence of meaningful competition in providing broadband access to consumers in many areas of the United States makes the broadband service provider a de facto monopolist, and therefore the sole gatekeeper in determining (1) the content that gets across to the end users and (2) in what fashion. Therefore the debate about NN assumes tremendous importance to

ISP’s revenue

Table 5 Comparative Statics with Respect to Capacity 

Variable

Content provider

Y ’s profit

Content provider

G’s profit

![](/api/attachments/H7EMY5BU/fulltext/images/83af8f77f69e0b59f2f81d67731f935734db5fe615573e72684e17a68746129b.jpg)

Consumer surplus

Social welfare

Note. <sub>+</sub> : increasing in $\mu ; \boxed { - }$ : decreasing in $\mu ; \boxed { 0 }$ : independent of $\mu ; \boxed { ? }$ : depends on parameter values.

a policy maker. This research aims to answer two issues therein in a stylized framework. We find that if the principle of NN is abolished, the ISP definitely stands to gain from the arrangement, as a result of extracting the preferential delivery charge from the content providers. The content providers are thus left worse off, mirroring the stances of the two sides in the debate. Depending on the parameter values in our framework, consumer surplus either does not change or is higher in the short run, and in the latter case, while a majority of consumers are better off, a minority is left worse off with larger wait times to access their preferred content. Social welfare in the short run increases when compared to the baseline NN case when one content provider pays for preferential treatment, but remains unchanged when both content providers pay. The crucial parameter that determines the nature of the equilibrium is the relative magnitude of the revenue generation capabilities of the two content providers: if they differ significantly, the consumers of the less effective (i.e., in terms of revenue generation) content provider, who are a minority, are left worse off.

The incentive for the broadband service provider to expand under NN is mostly higher than the incentive to expand when the principle of NN is abolished. The exception to this outcome occurs when the ISP’s profit accrues mostly from the consumers and only one content provider has the incentive to pay the priority delivery fees. Similarly, for most of the parameter space, the ISP’s optimal capacity choice under NN is higher than that under the NNN regime. In fact, the experience in broadband markets around the world indicates that there might be some other forces in play that account for the infrastructure capacity expansions in other countries. In Japan, for example, fierce competition among broadband service providers has led to the introduction of download bandwidth speeds in excess of 100 Mbps as far back as in 2004 (Yang et al. 2004), with prices for the consumers significantly lower than that in the United States (Turner 2005).

A final finding that should be of interest to policy makers is that under NN, the ISP invests in broadband infrastructure to reach the socially optimal level, but when there is NNN, the ISP either under- or overinvests in infrastructure.

Some immediate areas of future research include relaxing the assumption that the market is covered under both NN and NNN, an assumption made, in part, to capture the broadband service provider’s claim to not abandon its customers to win support for NNN. The broadband provider might decide to not pursue all the current subscribers after all, if that scenario can ensure higher profits. When the full market coverage assumption is relaxed, we postulate that under NN, the broadband service provider will choose to cover the market if customers’ valuation of the broadband service is higher than a threshold value, and only part of the market will be served by the broadband provider if customers’ valuation is low. This threshold value is likely to depend on both the fit cost t and the delay cost parameter d. With NNN, the broadband provider’s decision as to whether to serve the whole consumer market should be similar. Intuitively, the threshold value under NNN should be lower than that of NN, because the broadband provider has the option to subsidize the end users from the payments collected from content providers. That is, the broadband provider could cover more of the market under NNN.

Note that to make a meaningful comparison between the two regimes, the content providers must follow the same revenue model under both NN and NNN, and the issue therefore is to choose a revenue model that accurately captures the incentives of the content providers. Thanks to content providers like Google or Yahoo!, the overwhelmingly popular revenue model for content providers in the online world is the advertisement-assisted model. In this framework, consumers get full access to all the content from the online providers. The reason for the popularity of this model is that free content brings about a large number of visitors who, in turn, generate revenue by clicking on the advertisements. For several years, many content providers aimed for a hybrid model, a prominent example of which being the online edition of the New York Times, whereby some content, which was advertisement assisted, was available for free, but other, ostensibly higher-quality content, was made available only to paying subscribers. The New York Times abandoned this revenue model in late 2007, after discovering that the free, advertisementsupported content that was viewed by a large number of users was more profitable than a limited audience of paying subscribers. In fact, Sydell (2007, audio broadcast) reports that “this might be the way that everything is going on the Web,” and that the lone example of a mainstream content provider that relies on a subscription model, the online version of the Wall Street Journal, is also expected to make most of its content available for free before the end of 2008 (Anderson 2008).

While it has been argued that in the future, a significant amount of content would have to be paid for, that right now that remains a conjecture, with a growing body of evidence that the advertisement-generated model is becoming more popular with time (Sydell 2007), even with many content providers that would have been expected to follow a subscriber revenue model. A new online music company, SpiralFrog, for example, is based on the advertisement-supported model, whereby users get to download legal copies of music for free, and part of the advertisementgenerated revenue goes toward paying the royalty to the music publishers and labels that provide the music. Another example is Qtrax, a new business offering free and legal music downloads with 25 million songs in its inventory. Thus, under the current state of affairs, where the hybrid quality-differentiated model has been all but abandoned in favor of the purely advertisement-assisted model, advertisementsupported free content from the content providers seems to mirror the ground realities.

In fact, the prominent technology journalist and author Chris Anderson has argued that this new revenue model based around “free” is here to stay (Anderson 2008), pointing out that today online content generates revenue from banner advertisements, affiliate revenues, rental of subscription lists, sale of aggregate information, licensing, live events, listing, paid inclusion, cost per install, getting users to create content for free, streaming audio and video advertising, and API fees, to name a few (Wilson 2008). Anderson (2008) argues that this is possible today, as the Web has made it possible to monetize two scarcities that are valuable—reputation and attention—and coupled with the fact that the marginal cost of the content is almost negligible, it has been possible for an increasing number of companies to generate more revenue from the free content (e.g., a free album by Radiohead) than they could have by charging for that content on traditional media (charging for that album on a compact disc).

In this paper, we do not consider the capacity allocation issue. One interesting extension would be to study whether the ISP will find it optimal to partition the capacity and whether such capacity partitioning will change the ISP’s incentive to invest in expanding the infrastructure capacity. A major reason for the ISP to invest less under NNN than under NN is that capacity expansion reduces the attractiveness of priority delivery of packets for content providers. A partitioned capacity may enhance the content providers willingness to pay for the priority charge under NNN, which, in turn, may make ISP’s capacity expansion more desirable under NNN.<sup>10</sup> Similarly, it is of interest to examine the implication of NN on the ability of a content provider to provide premium services (e.g., real-time video or remote medical supervision) that require dedicated bandwidth.

Another direction of research would be to consider the effect of the broadband service provider as a potential competitor to the content (or other service) providers. Such a situation already exists today (albeit with limited success so far) with broadband service providers like Comcast building their own modest Internet portals, or with providers like AT&T or Comcast offering VoIP digital phone services (Krim 2005). Policy makers would then like to assure that the monopolist broadband service provider does not enjoy unfair competitive advantage, and look for guiding principles for ensuring fair competition under NN and NNN. The issue gets more complicated and interesting when a service provider like AT&T might end up cannibalizing its own traditional phone service by offering the new VoIP product.

## Acknowledgments

The authors gratefully acknowledge the very useful comments from the associate editor and three anonymous reviewers, and seminar participants of Arizona State University, Bocconi University (Milan, Italy), National Tsing Hua University (Taiwan), Purdue University, University of Arizona, University of British Columbia (Canada), University of Florida, University of Illinois at Urbana Champaign, University of Notre Dame, University of Utah, University of Texas at Austin, and University of Washington (Seattle). Any remaining error belongs to the authors.

## Appendix A. List of Notations

x: the marginal consumer indifferent between content providers Y and G

x˜: an arbitrary consumer on 0- 1

$r _ { Y } :$ content provider Y ’s revenue rate per-packet request for content

$r _ { G } \colon$ content provider G’s revenue rate per-packet request for content

p: the per-packet price for priority data packet transmission

$I _ { Y } , I _ { G } \colon$ the content providers’ service choices

: Poisson arrival rate of content requested from each consumer in packets per unit of time

t: fit cost for an end consumer away from the ideal content

V 	 : the gross value function of retrieving content for each consumer; concave and twice differentiable

d: customers’ delay cost $( \mathrm { i . e . , }$ congestion cost) per unit of time

$w _ { \mathrm { N N } } \colon$ the expected time in the queuing system under NN

$w _ { Y i } , \ w _ { G i } .$ the expected time in the queuing system for Outcome $i = { 1 , 2 , 3 } ,$ , 4 under NNN

$U _ { \mathrm { N N _ { - } Y } } , \quad U _ { \mathrm { N N _ { - } G } } , \quad U _ { \mathrm { N N N _ { - } Y } } , \quad U _ { \mathrm { N N N _ { - } G } } \mathrm { i }$ consumers’ utility function

F : the fixed fee per unit of time charged by the broadband provider to the end consumers

: capacity of the broadband provider in packets per unit of time

: discount rate used in the long-run problem

$x _ { \mathrm { N N } } \mathrm { : }$ the marginal consumer indifferent between content providers $Y$ and G under NN

$x _ { i } { : }$ the marginal consumer indifferent between content providers Y and G in outcome $i = 1 , 2 , 3 , 4$ under NNN

$\Pi _ { i } \colon \mathrm { I S P ^ { \prime } s }$ revenue in outcome i 1- 2- 3- 4 of the short-run problem

$\pi _ { i } { : }$ ISP’s profit in outcome $i = 1 , 2 , 3 ,$ 4 of the long-run problem

$\Pi _ { \gamma { i } } , \ \Pi _ { G i } \colon$ Content providers’ profit in outcome $i =$ $1 , 2 , 3 , 4$ of the short-run problem

$\pi _ { Y i } , \pi _ { G i } \mathrm { : }$ Content providers’ profit in outcome $i = 1 , 2 , 3 ,$ 4 of the long-run problem

$\Pi _ { \mathrm { N N \mathrm { \_ I S P } } } , \Pi _ { \mathrm { N N N \mathrm { \_ A } } }$ ,  : ISP’s revenue in the equilibrium of the short-run problem

,  ,  : ISP’s profit in the equilibrium of the long-run problem

$\Pi _ { \mathrm { N N \_ Y } } , \Pi _ { \mathrm { N N N \_ A \_ Y } } , \Pi _ { \mathrm { N N N \_ B \_ Y } } , \Pi _ { \mathrm { N N \_ S } } , \Pi _ { \mathrm { N N \_ G } } , \Pi _ { \mathrm { N N N \_ A \_ G } } , \Pi _ { \mathrm { N N N \_ B \_ G } } .$ Content providers’ profit in the equilibrium of the short-run problem

,  ,  ,  ,  ,  : Content providers’ profit in the equilibrium of the long-run problem

$\mathrm { C S } _ { \mathrm { N N } } , \mathrm { C S } _ { \mathrm { N N N } _ { \mathrm { - } } \mathrm { A } } , \mathrm { C S } _ { \mathrm { N N N } _ { \mathrm { - } } \mathrm { B } } .$ Consumer surplus

$$
S W _ {\mathrm{NN}}, S W _ {\mathrm {NNN\_A}}, S W _ {\mathrm {NNN\_B}}: \mathrm{Socialwelfare}
$$

## Appendix B. Proof of $\begin{array} { r } { x _ { 2 } > \frac { 1 } { \mathit { \varepsilon } _ { \mathit { \varepsilon } } } } \end{array}$

Since $x _ { 2 }$ is between 0 and 1 and $\mu - \lambda > 0$ , Equation (3) can be rearranged as

$$
2 t \lambda (\mu - \lambda) x _ {2} ^ {2} - t (2 \mu + \lambda) (\mu - \lambda) x _ {2} + t \mu (\mu - \lambda) + d \lambda = 0.\tag{B1}
$$

Define $f ( x _ { 2 } ) = 2 t \lambda ( \mu - \lambda ) x _ { 2 } ^ { 2 } - t ( 2 \mu + \lambda ) ( \mu - \lambda ) x _ { 2 } +$ $t \mu ( \mu \textrm { -- } \lambda ) \ + \ d \lambda ^ { 2 }$ . Then $x _ { 2 }$ solves $f ( x _ { 2 } ) ~ = ~ 0 .$ . Since $2 t \lambda ( \mu - \lambda ) > 0 , f ( x _ { 2 } )$ is a convex quadratic function. We also know that $f ( \scriptstyle { \frac { 1 } { 2 } } ) = d \lambda > 0$ and

$$
\begin{array}{c} \frac {\partial f}{\partial x _ {2}} \bigg | _ {x _ {2} = 1 / 2} = t (\mu - \lambda) \bigg [ 4 \lambda \bigg (\frac {1}{2} \bigg) - 2 \mu - \lambda \bigg ] \\ = - t (\mu - \lambda) (2 \mu - \lambda) <   0. \end{array}
$$

Therefore $\begin{array} { r } { x _ { 2 } > \frac { 1 } { 2 } } \end{array}$

## Appendix C. Proof of Proposition 1

## (the Results of the Short-Run Problem)

Before we proceed to prove the results for the short-run problem, we prove the following important intermediate results, which will be repeatedly used in later proofs.

It follows from Equation (4) that

$$
t x _ {3} + \frac {d \mu \lambda}{[ \mu - (1 - x _ {3}) \lambda ] (\mu - \lambda)} = t (1 - x _ {3}) + \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda},
$$

which can be rewritten as

$$
\frac {d \mu \lambda}{[ \mu - (1 - x _ {3}) \lambda ] (\mu - \lambda)} - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} = t (1 - x _ {3}) - t x _ {3}.\tag{C1}
$$

It can be further simplified to

$$
\left[ \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} \right] \left(\frac {\lambda}{\mu - \lambda}\right) = 2 t \left(\frac {1}{2} - x _ {3}\right).
$$

This leads to

$$
\frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} = 2 t \left(\frac {1}{2} - x _ {3}\right) \left(\frac {\mu}{\lambda} - 1\right).\tag{C2}
$$

Substituting (C2) into (C1), we get

$$
\frac {d \mu \lambda}{[ \mu - (1 - x _ {3}) \lambda ] (\mu - \lambda)} - 2 t \left(\frac {1}{2} - x _ {3}\right) \left(\frac {\mu}{\lambda} - 1\right) = t (1 - x _ {3}) - t x _ {3},
$$

which can be simplified to

$$
\left(\frac {d \lambda}{\mu - \lambda} \left[ \frac {\mu}{\mu - (1 - x _ {3}) \lambda} \right] = 2 t \left(\frac {1}{2} - x _ {3}\right) \left(\frac {\mu}{\lambda}\right). \right.
$$

This leads to

$$
\frac {d \lambda}{\mu - \lambda} = 2 t \left(\frac {1}{2} - x _ {3}\right) \left[ \frac {\mu}{\lambda} - (1 - x _ {3}) \right].\tag{C3}
$$

From formulas (C2) and (C3), we get

$$
\begin{array}{r l} \frac {d \lambda}{\mu - \lambda} - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} & = 2 t \left(\frac {1}{2} - x _ {3}\right) \left[ \frac {\mu}{\lambda} - (1 - x _ {3}) \right] \\ & - 2 t \left(\frac {1}{2} - x _ {3}\right) \left(\frac {\mu}{\lambda} - 1\right) \\ & = 2 t \left(\frac {1}{2} - x _ {3}\right) \left[ \frac {\mu}{\lambda} - (1 - x _ {3}) - \frac {\mu}{\lambda} + 1 \right] \\ & = 2 t x _ {3} \left(\frac {1}{2} - x _ {3}\right). \end{array} \tag {C4}
$$

Consumer Surplus Under NN

$$
\begin{array}{l} \mathrm{CS} _ {\mathrm{NN}} = \int_ {0} ^ {1 / 2} \left(V (\lambda) - t x - \frac {d \lambda}{\mu - \lambda} - F _ {N N}\right) d x \\ \qquad + \int_ {1 / 2} ^ {1} \left(V (\lambda) - t (1 - x) - \frac {d \lambda}{\mu - \lambda} - F _ {N N}\right) d x \\ \qquad = \int_ {0} ^ {1 / 2} \left(V (\lambda) - t x - \frac {d \lambda}{\mu - \lambda} - \left(V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda}\right)\right) d x \\ \qquad + \int_ {1 / 2} ^ {1} \left(V (\lambda) - t (1 - x) - \frac {d \lambda}{\mu - \lambda} \right. \\ \qquad \qquad \qquad \qquad \qquad \left. - \left(V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda}\right)\right) d x \\ \qquad = \int_ {0} ^ {1 / 2} \left(\frac {t}{2} - t x\right) d x + \int_ {1 / 2} ^ {1} \left(t x - \frac {t}{2}\right) d x \\ \qquad = \left(\frac {t}{2} x - \frac {t}{2} x ^ {2}\right) \bigg | _ {0} ^ {\frac {1}{2}} + \left(\frac {t}{2} x ^ {2} - \frac {t}{2} x\right) \bigg | _ {1 / 2} ^ {1} = \frac {t}{4}. \end{array}
$$

Consumer surplus consists of two parts:

$$
\begin{array}{l} \mathrm{CS} _ {\mathrm {NN\_Y}} = \int_ {0} ^ {1 / 2} \bigg (V (\lambda) - t x - \frac {d \lambda}{\mu - \lambda} - F _ {N N} \bigg) d x \\ \qquad = \bigg (\frac {t}{2} x - \frac {t}{2} x ^ {2} \bigg) \bigg | _ {0} ^ {\frac {1}{2}} = \frac {t}{8}. \\ \mathrm{CS} _ {\mathrm {NN\_G}} = \int_ {1 / 2} ^ {1} \bigg (V (\lambda) - t (1 - x) - \frac {d \lambda}{\mu - \lambda} - F _ {N N} \bigg) d x \\ \qquad = \bigg (\frac {t}{2} x ^ {2} - \frac {t}{2} x \bigg) \bigg | _ {1 / 2} ^ {1} = \frac {t}{8}. \end{array}
$$

Social Welfare Under NN

$$
\begin{array}{l} \mathrm {SW_ {NN}} = \Pi_ {\mathrm {NN\_ISP}} + \Pi_ {\mathrm {NN\_Y}} + \Pi_ {\mathrm {NN\_G}} + \mathrm {CS_ {NN}} \\ \qquad = \left[ V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} \right] + \left(\frac {1}{2} \lambda r _ {_ Y}\right) + \left(\frac {1}{2} \lambda r _ {_ G}\right) + \left(\frac {t}{4}\right) \\ \qquad = V (\lambda) - \frac {t}{4} - \frac {d \lambda}{\mu - \lambda} + \frac {1}{2} \lambda r _ {_ Y} + \frac {1}{2} \lambda r _ {_ G}. \end{array}
$$

Internet Access Fee Under NNN Case A

$$
\begin{array}{c} F _ {\text {NNN\_A}} - F _ {\text {NN}} = \left[ V (\lambda) - t (1 - x _ {3}) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} \right] \\ - \left[ V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} \right] \\ = \frac {d \lambda}{\mu - \lambda} - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} - t \bigg (\frac {1}{2} - x _ {3} \bigg). \end{array}
$$

Substituting (C4) into the above, we get

$$
= 2 t x _ {3} \left(\frac {1}{2} - x _ {3}\right) - t \left(\frac {1}{2} - x _ {3}\right) = - 2 t \left(\frac {1}{2} - x _ {3}\right) ^ {2} <   0.
$$

Therefore $F _ { \mathrm { N N N \_ A } } < F _ { \mathrm { N N } }$

ISP’s Revenue Under NNN Case A

$$
\begin{array}{l} \Pi_ {\text {NNN\_A\_ISP}} - \Pi_ {\text {NN\_ISP}} \\ = \left[ V (\lambda) - t (1 - x _ {3}) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} + \left(\frac {1}{2} - x _ {3}\right) \lambda r _ {G} \right] \\ - \left[ V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} \right] \\ = \frac {d \lambda}{\mu - \lambda} - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} - t \left(\frac {1}{2} - x _ {3}\right) + \left(\frac {1}{2} - x _ {3}\right) \lambda r _ {G}. \end{array}
$$

$$
\begin{array}{l} \text { Substituting   (C4)   into   the   above, we   get } \\ \qquad = 2 t x _ {3} \big (\frac {1}{2} - x _ {3} \big) - t \big (\frac {1}{2} - x _ {3} \big) + \big (\frac {1}{2} - x _ {3} \big) \lambda r _ {G} \\ \qquad = \big (\frac {1}{2} - x _ {3} \big) [ \lambda r _ {G} - t (1 - 2 x _ {3}) ]. \end{array}
$$

Since we know under NNN Case A

$$
r _ {G} \geq 2 r _ {Y} + \frac {t}{\lambda} (1 - 2 x _ {3}), \quad \lambda r _ {G} - t (1 - 2 x _ {3}) > 0.
$$

Therefore $\Pi _ { \mathrm { N N N \_ A \_ I S P } } > \Pi _ { \mathrm { N N \_ I S P } }$

Content Providers’ Profit Under NNN Case A

$$
\begin{array}{r} \Pi_ {\mathrm {NNN\_A\_Y}} = x _ {3} \lambda r _ {Y} <   \frac {1}{2} \lambda r _ {Y} = \Pi_ {\mathrm {NN\_Y}}, \\ \Pi_ {\mathrm {NNN\_A\_G}} = \frac {1}{2} \lambda r _ {G} = \Pi_ {\mathrm {NN\_G}}. \end{array}
$$

Consumer Surplus Under NNN Case A

$$
\begin{array}{l} \text {CS} _ {\text {NNN\_A}} = \int_ {0} ^ {x _ {3}} \bigg (V (\lambda) - t x - \frac {d \mu \lambda}{[ \mu - (1 - x _ {3}) ] (\mu - \lambda)} - F _ {3} \bigg) d x \\ \qquad + \int_ {x _ {3}} ^ {1} \bigg (V (\lambda) - t (1 - x) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} - F _ {3} \bigg) d x. \end{array}
$$

Since

$$
\begin{array}{l} F _ {3} = V (\lambda) - t x _ {3} - \frac {d \mu \lambda}{[ \mu - (1 - x _ {3}) \lambda ] (\mu - \lambda)} \\ = V (\lambda) - t (1 - x _ {3}) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} \\ = \int_ {0} ^ {x _ {3}} \left(V (\lambda) - t x - \frac {d \mu \lambda}{[ \mu - (1 - x _ {3}) \lambda ] (\mu - \lambda)} \right. \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad + \int_ {x _ {3}} ^ {1} \left(V (\lambda) - t (1 - x) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} \right. \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad + \int_ {x _ {3}} ^ {1} (V (\lambda) - t (1 - x) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} \\ = \int_ {0} ^ {x _ {3}} (t x _ {3} - t x) d x + \int_ {x _ {3}} ^ {1} (t x - t x _ {3}) d x \\ = t \left(x _ {3} x - \frac {1}{2} x ^ {2}\right) \bigg | _ {0} ^ {x _ {3}} + t \left(\frac {1}{2} x ^ {2} - x _ {3} x\right) \bigg | _ {x _ {3}} ^ {1} \\ = t x _ {3} ^ {2} - \frac {t}{2} x _ {3} ^ {2} + \frac {t}{2} - t x _ {3} - \frac {t}{2} x _ {3} ^ {2} + t x _ {3} ^ {2} = t \left(x _ {3} ^ {2} - x _ {3} + \frac {1}{2}\right) \\ = t \left[ \left(x _ {3} - \frac {1}{2}\right) ^ {2} + \frac {1}{4} \right] > \frac {t}{4} = C S _ {\mathrm{NN}}. \end{array}
$$

Therefore $\mathrm { C S } _ { \mathrm { N N N \mathrm { ~ \tiny ~ A ~ } } } > \mathrm { C S } _ { \mathrm { N N } } ,$ i.e., the consumer surplus is increased in NNN Case A, compared to NN.

Consumer surplus consists of two parts:

$$
\begin{array}{l} \mathrm{CS} _ {\mathrm {NNN\_A\_Y}} = \int_ {0} ^ {x _ {3}} \left(V (\lambda) - t x - \frac {d \mu \lambda}{[ \mu - (1 - x _ {3}) \lambda ] (\mu - \lambda)} - F _ {3}\right) d x \\ = t \left(x _ {3} x - \frac {1}{2} x ^ {2}\right) \Big | _ {0} ^ {x _ {3}} = \frac {t}{2} x _ {3} ^ {2} <   \frac {t}{8} = \mathrm{CS} _ {\mathrm {NN\_Y}} \end{array}
$$

since $0 < x _ { 3 } < 1 / 2$

$$
\begin{array}{l} \mathrm{CS} _ {\text {NNN\_A\_G}} = \int_ {x _ {3}} ^ {1} \left(V (\lambda) - t (1 - x) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} - F _ {3}\right) d x \\ = t \left(\frac {1}{2} x ^ {2} - x _ {3} x\right) \Bigg | _ {x _ {3}} ^ {1} \\ = t \left(\frac {1}{2} x _ {3} ^ {2} - x _ {3} + \frac {1}{2}\right) > \frac {t}{8} = \mathrm{CS} _ {\text {NN\_G}} \end{array}
$$

since $0 < x _ { 3 } < 1 / 2$

Social Welfare Under NNN Case A

$$
\begin{array}{r l} \mathrm {SW_ {NNN\_A}} & = \Pi_ {\mathrm {NNN\_A\_ISP}} + \Pi_ {\mathrm {NNN\_A\_Y}} + \Pi_ {\mathrm {NNN\_A\_G}} + \mathrm {CS_ {NNN\_A}} \\ & = \left[ V (\lambda) - t (1 - x _ {3}) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} + \left(\frac {1}{2} - x _ {3}\right) \lambda r _ {G} \right] \\ & \quad + (x _ {3} \lambda r _ {Y}) + \left(\frac {1}{2} \lambda r _ {G}\right) + \left[ t \left(x _ {3} ^ {2} - x _ {3} + \frac {1}{2}\right) \right] \\ & = V (\lambda) - t \left(\frac {1}{2} - x _ {3} ^ {2}\right) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} \\ & \quad + x _ {3} \lambda r _ {Y} + (1 - x _ {3}) \lambda r _ {G} \end{array}
$$

$$
\begin{array}{l} \mathrm {SW_ {NNN\_A}} - \mathrm {SW_ {NN}} \\ = \left(V (\lambda) - t \left(\frac {1}{2} - x _ {3} ^ {2}\right) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} + x _ {3} \lambda r _ {Y} + (1 - x _ {3}) \lambda r _ {G}\right) \\ \quad - \left(V (\lambda) - \frac {t}{4} - \frac {d \lambda}{\mu - \lambda} + \frac {1}{2} \lambda r _ {Y} + \frac {1}{2} \lambda r _ {G}\right) \\ = - t \left(\frac {1}{4} - x _ {3} ^ {2}\right) + \frac {d \lambda}{\mu - \lambda} - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} \\ \quad - \left(\frac {1}{2} - x _ {3}\right) \lambda r _ {Y} + \left(\frac {1}{2} - x _ {3}\right) \lambda r _ {G} \\ = - t \left(\frac {1}{2} - x _ {3}\right) \left(\frac {1}{2} + x _ {3}\right) + 2 t x _ {3} \left(\frac {1}{2} - x _ {3}\right) + \left(\frac {1}{2} - x _ {3}\right) \lambda (r _ {G} - r _ {Y}) \end{array}
$$

because of Equation (C4)

$$
\begin{array}{l} = \left(\frac {1}{2} - x _ {3}\right) \left[ - t \left(\frac {1}{2} + x _ {3}\right) + 2 t x _ {3} + \lambda (r _ {G} - r _ {Y}) \right] \\ = \left(\frac {1}{2} - x _ {3}\right) \left[ \lambda (r _ {G} - r _ {Y}) - t \left(\frac {1}{2} - x _ {3}\right) \right] \\ > \left(\frac {1}{2} - x _ {3}\right) \left[ \lambda \left(2 r _ {Y} + \frac {t}{\lambda} (1 - 2 x _ {3}) - r _ {Y}\right) - t \left(\frac {1}{2} - x _ {3}\right) \right] \\ = \left(\frac {1}{2} - x _ {3}\right) \left[ \lambda r _ {Y} + t \left(\frac {1}{2} - x _ {3}\right) \right] > 0. \end{array}
$$

Therefore $\mathrm { S W _ { N N N \_ A } } > \mathrm { S W _ { N N } , i . e . } ,$ social welfare is increased in NNN Case A, compared to NN.

Internet Access Fee Under NNN Case B

$$
F _ {\mathrm {NNN\_B}} = V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} = F _ {\mathrm{NN}}.
$$

ISP’s Revenue Under NNN Case B

$$
\begin{array}{c} \Pi_ {\text {NNN\_B\_ISP}} = V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} + (1 - 2 x _ {3}) \lambda r _ {Y} \\ > V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} = \Pi_ {\text {NN\_ISP}}. \end{array}
$$

Content Providers’ Profit Under NNN Case B

$$
\begin{array}{c} \Pi_ {\mathrm {NNN\_B\_Y}} = x _ {3} \lambda r _ {Y} <   \frac {1}{2} \lambda r _ {Y} = \Pi_ {\mathrm {NN\_Y}}, \\ \Pi_ {\mathrm {NNN\_B\_G}} = \frac {1}{2} \lambda [ r _ {G} - (1 - 2 x _ {3}) r _ {Y} ] <   \frac {1}{2} \lambda r _ {G} = \Pi_ {\mathrm {NN\_G}}. \end{array}
$$

Consumer Surplus Under NNN Case B

$$
\begin{array}{r l} & {\mathrm{CS} _ {\mathrm {NNN\_B}} = \int_ {0} ^ {\frac {1}{2}} \bigg (V (\lambda) - t x - \frac {d \lambda}{\mu - \lambda} - F _ {4} \bigg) d x} \\ & {\qquad + \int_ {\frac {1}{2}} ^ {1} \bigg (V (\lambda) - t (1 - x) - \frac {d \lambda}{\mu - \lambda} - F _ {4} \bigg) d x} \\ & {\qquad = \int_ {0} ^ {\frac {1}{2}} \bigg (V (\lambda) - t x - \frac {d \lambda}{\mu - \lambda} - \bigg (V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} \bigg) \bigg) d x} \\ & {\qquad + \int_ {\frac {1}{2}} ^ {1} \bigg (V (\lambda) - t (1 - x) - \frac {d \lambda}{\mu - \lambda}} \\ & {\qquad \qquad - \left(V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda}\right) \bigg) d x} \end{array}
$$

$$
\begin{array}{l} = \int_ {0} ^ {\frac {1}{2}} \left(\frac {t}{2} - t x\right) d x + \int_ {\frac {1}{2}} ^ {1} \left(t x - \frac {t}{2}\right) d x \\ = t \left(\frac {1}{2} x - \frac {1}{2} x ^ {2}\right) \bigg | _ {0} ^ {\frac {1}{2}} + t \left(\frac {1}{2} x ^ {2} - \frac {1}{2} x\right) \bigg | _ {\frac {1}{2}} ^ {1} = \frac {t}{4} = C S _ {\mathrm{NN}}. \end{array}
$$

Consumer surplus consists of two parts:

$$
\begin{array}{r l} & {\mathrm{CS} _ {\mathrm {NNN\_B\_Y}}} = \int_ {0} ^ {\frac {1}{2}} \bigg (V (\lambda) - t x - \frac {d \lambda}{\mu - \lambda} - F _ {4} \bigg) d x \\ & {\qquad = t \bigg (\frac {1}{2} x - \frac {1}{2} x ^ {2} \bigg) \bigg | _ {0} ^ {\frac {1}{2}} = \frac {t}{8} = \mathrm{CS} _ {\mathrm {NN\_Y}},} \\ & {\mathrm{CS} _ {\mathrm {NNN\_B\_G}}} = \int_ {\frac {1}{2}} ^ {1} \bigg (V (\lambda) - t (1 - x) - \frac {d \lambda}{\mu - \lambda} - F _ {4} \bigg) d x \\ & {\qquad = t \bigg (\frac {1}{2} x ^ {2} - \frac {1}{2} x \bigg) \bigg | _ {\frac {1}{2}} ^ {1} = \frac {t}{8} = \mathrm{CS} _ {\mathrm {NN\_G}}.} \end{array}
$$

Therefore, the consumer surplus remains unchanged.

Social Welfare Under NNN Case B

$$
\begin{array}{r l} & S W _ {\text {NNN\_B}} = \Pi_ {\text {NNN\_B\_ISP}} + \Pi_ {\text {NNN\_B\_Y}} + \Pi_ {\text {NNN\_B\_G}} + C S _ {\text {NNN\_B}} \\ & \qquad = \left[ V (\lambda) - \frac {t}{2} - \frac {d \lambda}{\mu - \lambda} + (1 - 2 x _ {3}) \lambda r _ {Y} \right] \\ & \qquad \qquad + (x _ {3} \lambda r _ {Y}) + \left\{\frac {1}{2} \lambda [ r _ {G} - (1 - 2 x _ {3}) r _ {Y} ] \right\} + \left(\frac {t}{4}\right) \\ & \qquad = V (\lambda) - \frac {t}{4} - \frac {d \lambda}{\mu - \lambda} + \frac {1}{2} \lambda r _ {Y} + \frac {1}{2} \lambda r _ {G} = S W _ {\text {NN}}. \end{array}
$$

Therefore, social welfare remains unchanged.

Appendix D. A Necessary and Sufficient Condition for the Existence of a

Unique $x _ { 3 } \in ( 0 , 1 )$

It follows from Equation (11) that

$$
t x _ {3} + \frac {d \mu \lambda}{[ \mu - (1 - x _ {3}) \lambda ] (\mu - \lambda)} = t (1 - x _ {3}) + \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda},
$$

which can be simplified to

$$
2 t \lambda (\mu - \lambda) x _ {3} ^ {2} + t (\mu - \lambda) (2 \mu - 3 \lambda) x _ {3} + d \lambda^ {2} - t (\mu - \lambda) ^ {2} = 0.\tag{D1}
$$

We consider the function $f ( x _ { 3 } ) \ = \ 2 t \lambda ( \mu \ - \ \lambda ) x _ { 3 } ^ { 2 } \ +$ $t ( \mu - \lambda ) ( 2 \mu - 3 \lambda ) x _ { 3 } + d \lambda ^ { 2 } - t ( \mu - \lambda ) ^ { 2 }$ . We know $f ( 0 ) = d \bar { \lambda } ^ { 2 } -$ $t ( \mu - \lambda ) ^ { 2 } , ~ f ( 1 ) = d \lambda ^ { 2 } + t \mu ( \mu - \lambda ) > 0 , ~ f ( \textstyle { \frac { 1 } { 7 } } ) = \dot { d } \lambda ^ { 2 } > 0 ,$ , and $f ( x _ { 3 } )$ achieves the minimum at $\begin{array} { r } { x _ { 3 } = \frac { 3 } { 4 } - \frac { \mu ^ { - } } { 2 \lambda } } \end{array}$ with

$$
f \left(\frac {3}{4} - \frac {\mu}{2 \lambda}\right) = \frac {8 d \lambda^ {3} - t (\mu - \lambda) (2 \mu - \lambda) ^ {2}}{8 \lambda}.
$$

There is a unique solution on 	0- 1 iff $f ( 0 ) = d \lambda ^ { 2 } \ : - \ :$ $t ( \mu - \lambda ) ^ { 2 } < 0$ . That is,

$$
d <   \frac {t (\mu - \lambda) ^ {2}}{\lambda^ {2}}.\tag{D2}
$$

Condition (D2) is necessary and sufficient for the existence of a unique $x _ { 3 } \in ( 0 , 1 )$ . This condition is equivalent to

$$
V (\lambda) - \frac {d \mu \lambda}{(\mu - \lambda) ^ {2}} - F _ {3} > V (\lambda) - t - \frac {d \lambda}{\mu - \lambda} - F _ {3},
$$

meaning that the consumers located at the two ends of the market are loyal to their corresponding content providers.

Under condition (D2), we know $\begin{array} { r } { \frac { 3 } { 4 } - \overline { { \mu } } / ( 2 \lambda ) < \overline { { x } } _ { 3 } < \frac { 1 } { 2 } } \end{array}$

Appendix E. The Location of Marginal Consumer in Outcome 3 Moves to the Right When ISP Capacity Increases, $\begin{array} { r } { \frac { \partial x _ { 3 } } { \partial \mu } > 0 } \end{array}$

Using implicit differentiation, $\frac { \partial x _ { 3 } } { \partial \mu }$ can be derived from Equation (D1) by solving

$$
\begin{array}{r l} & 2 t \lambda \bigg [ x _ {3} ^ {2} + 2 (\mu - \lambda) x _ {3} \frac {\partial x _ {3}}{\partial \mu} \bigg ] \\ & \qquad + t \bigg [ (4 \mu - 5 \lambda) x _ {3} + (\mu - \lambda) (2 \mu - 3 \lambda) \frac {\partial x _ {3}}{\partial \mu} \bigg ] - 2 t (\mu - \lambda) = 0 \\ & \qquad [ 4 \lambda (\mu - \lambda) x _ {3} + (\mu - \lambda) (2 \mu - 3 \lambda) ] \frac {\partial x _ {3}}{\partial \mu} \\ & \qquad = 2 (\mu - \lambda) - 2 \lambda x _ {3} ^ {2} - (4 \mu - 5 \lambda) x _ {3} \\ & (\mu - \lambda) (2 \mu - 3 \lambda + 4 \lambda x _ {3}) \frac {\partial x _ {3}}{\partial \mu} = (1 - 2 x _ {3}) (2 \mu - 2 \lambda + \lambda x _ {3}). \end{array}
$$

Since we know $1 - 2 x _ { 3 } > 0 , \ 2 \mu - 2 \lambda + \lambda x _ { 3 } > 0 , \ \mu - \lambda > 0 ,$ the sign of $\textstyle { \frac { \partial x _ { 3 } } { \partial \mu } }$ depends on $2 \mu - 3 \lambda + 4 \lambda x _ { 3 } .$ . From condition $( \mathsf { D } 2 ) .$ , it can be shown that $\begin{array} { r } { \frac { 3 } { 4 } - \frac { \mu } { 2 \lambda } < x _ { 3 } < \frac { 1 } { 2 } } \end{array}$ . Therefore from Appendix D,

$$
\frac {\partial x _ {3}}{\partial \mu} = \frac {(1 - 2 x _ {3}) (2 \mu - 2 \lambda + \lambda x _ {3})}{(\mu - \lambda) (2 \mu - 3 \lambda + 4 \lambda x _ {3})} > 0.
$$

Appendix F. Proof of Proposition 2 $\mathbf { ( \bar { I } \bar { S } \bar { P } ^ { \prime } s }$ Incentive to Expand Capacity)

To compare the ISP’s incentive to expand capacity, we need to compare

$$
\begin{array}{c} \frac {\partial \pi_ {\mathrm{NN}}}{\partial \mu} = \frac {1}{1 - \delta} \cdot \frac {d \lambda}{(\mu - \lambda) ^ {2}} - \frac {\partial C (\mu)}{\partial \mu} \\ \frac {\partial \pi_ {\mathrm {NNN\_A}}}{\partial \mu} = \frac {1}{1 - \delta} \cdot \left[ t \left(\frac {2 \mu}{\lambda} - 1\right) - \lambda r _ {G} \right] \frac {\partial x _ {3}}{\partial \mu} - \frac {1}{1 - \delta} \\ \cdot \frac {2 t}{\lambda} \left(\frac {1}{2} - x _ {3}\right) - \frac {\partial C (\mu)}{\partial \mu}, \quad \text { and } \\ \frac {\partial \pi_ {\mathrm {NNN\_B}}}{\partial \mu} = \frac {1}{1 - \delta} \cdot \frac {d \lambda}{(\mu - \lambda) ^ {2}} - \frac {2}{1 - \delta} \cdot \frac {\partial x _ {3}}{\partial \mu} \lambda r _ {Y} - \frac {\partial C (\mu)}{\partial \mu} \end{array}
$$

$$
\begin{array}{r l} & {\frac {\partial \pi_ {\mathrm{NN}}}{\partial \mu} - \frac {\partial \pi_ {\mathrm {NNN\_B}}}{\partial \mu}} \\ & {\quad = \left[ \frac {1}{1 - \delta} \cdot \frac {d \lambda}{(\mu - \lambda) ^ {2}} - \frac {\partial C (\mu)}{\partial \mu} \right]} \\ & {\quad \quad - \left[ \frac {1}{1 - \delta} \cdot \frac {d \lambda}{(\mu - \lambda) ^ {2}} - \frac {2}{1 - \delta} \cdot \frac {\partial x _ {3}}{\partial \mu} \lambda r _ {Y} - \frac {\partial C (\mu)}{\partial \mu} \right]} \\ & {\quad = \frac {2}{1 - \delta} \cdot \frac {\partial x _ {3}}{\partial \mu} \lambda r _ {Y} > 0} \end{array}
$$

$$
\begin{array}{r} \frac {\partial \pi_ {\mathrm{NN}}}{\partial \mu} - \frac {\partial \pi_ {\mathrm {NNN\_A}}}{\partial \mu} = \left[ \frac {1}{1 - \delta} \cdot \frac {d \lambda}{(\mu - \lambda) ^ {2}} - \frac {\partial C (\mu)}{\partial \mu} \right] \\ - \left\{\frac {1}{1 - \delta} \cdot \left[ t \left(\frac {2 \mu}{\lambda} - 1\right) - \lambda r _ {G} \right] \frac {\partial x _ {3}}{\partial \mu} - \frac {1}{1 - \delta} \right. \\ \left. \cdot \frac {2 t}{\lambda} \left(\frac {1}{2} - x _ {3}\right) - \frac {\partial C (\mu)}{\partial \mu} \right\} \end{array}
$$

$$
\begin{array}{c} = \frac {1}{1 - \delta} \bigg \{\frac {d \lambda}{(\mu - \lambda) ^ {2}} - \bigg [ t \bigg (\frac {2 \mu}{\lambda} - 1 \bigg) - \lambda r _ {G} \bigg ] \frac {\partial x _ {3}}{\partial \mu} \\ + \frac {2 t}{\lambda} \bigg (\frac {1}{2} - x _ {3} \bigg) \bigg \}. \end{array}
$$

Substituting

$$
\frac {\partial x _ {3}}{\partial \mu} = \frac {(1 - 2 x _ {3}) (2 \mu - 2 \lambda + \lambda x _ {3})}{(\mu - \lambda) (2 \mu - 3 \lambda + 4 \lambda x _ {3})}
$$

and

$$
{\frac {d \lambda}{\mu - \lambda}} = 2 t \left({\frac {1}{2}} - x _ {3}\right) \left[ {\frac {\mu}{\lambda}} - (1 - x _ {3}) \right]
$$

into the above, gives

$$
\begin{array}{l} \frac {\partial \pi_ {\mathrm{NN}}}{\partial \mu} - \frac {\partial \pi_ {\mathrm {NNN\_A}}}{\partial \mu} \\ = \frac {1}{1 - \delta} \left\{\frac {1}{\mu - \lambda} 2 t \left(\frac {1}{2} - x _ {3}\right) \left[ \frac {\mu}{\lambda} - (1 - x _ {3}) \right] \right. \\ \qquad \qquad \qquad - \left[ t \left(\frac {2 \mu}{\lambda} - 1\right) - \lambda r _ {G} \right] \frac {(1 - 2 x _ {3}) (2 \mu - 2 \lambda + \lambda x _ {3})}{(\mu - \lambda) (2 \mu - 3 \lambda + 4 \lambda x _ {3})} \\ \qquad \qquad \qquad + \frac {2 t}{\lambda} \left(\frac {1}{2} - x _ {3}\right) \Bigg \} \end{array}
$$

$$
\begin{array}{r} = \frac {2}{1 - \delta} \left(\frac {1}{2} - x _ {3}\right) \Bigg \{\frac {1}{\mu - \lambda} t \bigg [ \frac {\mu}{\lambda} - (1 - x _ {3}) \bigg ] - \bigg [ t \bigg (\frac {2 \mu}{\lambda} - 1 \bigg) - \lambda r _ {G} \bigg ] \\ \cdot \frac {(2 \mu - 2 \lambda + \lambda x _ {3})}{(\mu - \lambda) (2 \mu - 3 \lambda + 4 \lambda x _ {3})} + \frac {t}{\lambda} \Bigg \} \end{array}
$$

$$
\begin{array}{r l} & {= \frac {2}{1 - \delta} \bigg (\frac {1}{2} - x _ {3} \bigg) \bigg \{\lambda r _ {G} \frac {(2 \mu - 2 \lambda + \lambda x _ {3})}{(\mu - \lambda) (2 \mu - 3 \lambda + 4 \lambda x _ {3})}} \\ & {\qquad + \frac {t}{\lambda} \bigg [ \frac {\mu - \lambda + \lambda x _ {3}}{\mu - \lambda} - \frac {(2 \mu - \lambda) (2 \mu - 2 \lambda + \lambda x _ {3})}{(\mu - \lambda) (2 \mu - 3 \lambda + 4 \lambda x _ {3})} + 1 \bigg ] \bigg \}} \\ & {\qquad = \frac {2}{1 - \delta} \bigg (\frac {1}{2} - x _ {3} \bigg) \frac {(2 \mu - 2 \lambda + \lambda x _ {3})}{(\mu - \lambda) (2 \mu - 3 \lambda + 4 \lambda x _ {3})} [ \lambda r _ {G} - 2 t (1 - 2 x _ {3}) ].} \end{array}
$$

Therefore

$$
\frac {\partial \pi_ {\mathrm{NN}}}{\partial \mu} - \frac {\partial \pi_ {\mathrm {NNN\_A}}}{\partial \mu} \left\{ \begin{array}{l l} \geq 0, & \text { if } r _ {G} \geq \frac {2 t}{\lambda} (1 - 2 x _ {3}) \\ <   0, & \text { if } r _ {G} <   \frac {2 t}{\lambda} (1 - 2 x _ {3}) \end{array} \right..
$$

Recall that when $\begin{array} { r } { r _ { G } \geq 2 r _ { Y } + \frac { t } { \lambda } ( 1 - 2 x _ { 3 } ) , } \end{array}$ , Outcome 3 is the equilibrium and when $\begin{array} { r } { r _ { G } ^ { \because } < 2 r _ { Y } + \frac { t } { \lambda } ( 1 - 2 x _ { 3 } ) } \end{array}$ , Outcome 4 is the equilibrium. We conclude that when $\begin{array} { r } { r _ { G } < 2 r _ { Y } + \frac { t } { \lambda } ( 1 - 2 x _ { 3 } ) } \end{array}$ or $\begin{array} { r } { r _ { G } \geq \frac { 2 t } { \lambda } ( 1 - 2 x _ { 3 } ) } \end{array}$ , the ISP has more incentive to expand capacity under NN; when $2 r _ { Y } +$ $\begin{array} { r } { \frac { t } { \lambda } ( 1 - 2 x _ { 3 } ) \leq r _ { G } < \frac { 2 t } { \lambda } ( 1 - 2 x _ { 3 } ) } \end{array}$ , the ISP has more incentive to expand capacity under NNN.

## Appendix G. Proof of Proposition 3 (Optimal Capacity Choice)

Recall that the optimal capacity level for the ISP is determined by first-order conditions $\dot { \frac { \partial \pi _ { \mathrm { N N } } } { \partial \mu } } = 0$ for NN, $\frac { \partial \pi _ { \mathrm { N N N _ { - } A } } } { \partial \mu } = 0$ for NNN Case A, and $\frac { \partial \pi _ { \mathrm { N N N _ { - } B } } } { \partial \mu } = 0$ for NNN Case B described in Equations (15)–(17), respectively.

From the proof of Proposition 1, when $\begin{array} { r } { r _ { G } < 2 r _ { Y } + \frac { t } { \lambda } } \end{array}$ $( 1 - 2 x _ { 3 } )$ or $\begin{array} { r } { r _ { G } > \operatorname* { m a x } \{ 2 \bar { r _ { Y } } + \frac { t } { \lambda } ( 1 - 2 x _ { 3 } ) , \frac { 2 t } { \lambda } ( 1 - 2 x _ { 3 } ) \} . } \end{array}$ , the ISP has more incentive to expand capacity under NN, i.e., $\begin{array} { r } { \frac { \partial \pi _ { \mathrm { N N } } } { \partial u } > \frac { \partial \pi _ { \mathrm { N N N } } } { \partial u } } \end{array}$ . Let $\mu _ { \mathrm { N N } } ^ { * }$ and $\mu _ { \mathrm { N N N } } ^ { * }$ be the optimal capacity levels for NN and NNN, respectively. Then

$$
\left. \frac {\partial \pi_ {\mathrm{NN}}}{\partial \mu} \right| _ {\mu = \mu_ {\mathrm{NN}} ^ {*}} = 0 \quad \text {and} \quad \left. \frac {\partial \pi_ {\mathrm{NNN}}}{\partial \mu} \right| _ {\mu = \mu_ {\mathrm{NNN}} ^ {*}} = 0.
$$

Since

$$
\begin{array}{c} \frac {\partial \pi_ {\mathrm{NN}}}{\partial \mu} > \frac {\partial \pi_ {\mathrm{NNN}}}{\partial \mu}, \\ \frac {\partial \pi_ {\mathrm{NNN}}}{\partial \mu} \bigg | _ {\mu = \mu_ {\mathrm{NNN}} ^ {*}} = 0 = \frac {\partial \pi_ {\mathrm{NN}}}{\partial \mu} \bigg | _ {\mu = \mu_ {\mathrm{NN}} ^ {*}} > \frac {\partial \pi_ {\mathrm{NNN}}}{\partial \mu} \bigg | _ {\mu = \mu_ {\mathrm{NN}} ^ {*}}. \end{array}
$$

Second-order condition gives

$$
\frac {\partial^ {2} \pi_ {\mathrm{NN}}}{\partial \mu^ {2}} <   0 \quad \text { and } \quad \frac {\partial^ {2} \pi_ {\mathrm{NNN}}}{\partial \mu^ {2}} <   0.
$$

So $\frac { \partial \pi _ { \mathrm { N N } } } { \partial \mu }$ and $\frac { \partial \pi _ { \mathrm { N N N } } } { \partial \mu }$ decrease in $\mu .$ . Therefore $\mu _ { \mathrm { N N N } } ^ { * } < \mu _ { \mathrm { N N } } ^ { * }$

Similarly, when $\begin{array} { r } { 2 r _ { Y } + \frac { t } { \lambda } ( 1 - 2 x _ { 3 } ) \le r _ { G } \le \frac { 2 t } { \lambda } ( 1 - 2 x _ { 3 } ) , } \end{array}$ , the ISP has more incentive to expand capacity under NNN, i.e., $\begin{array} { r } { \frac { \partial \pi _ { \mathrm { N N } } } { \partial \omega } \leq \frac { \partial \pi _ { \mathrm { N N N } } } { \partial \omega } } \end{array}$ . Let $\mu _ { \mathrm { N N } } ^ { * }$ and $\mu _ { \mathrm { N N N } } ^ { * }$ be the optimal capacity levels for NN and NNN, respectively. Then

$$
\left. \frac {\partial \pi_ {\mathrm{NN}}}{\partial \mu} \right| _ {\mu = \mu_ {\mathrm{NN}} ^ {*}} = 0 \quad \text {and} \quad \left. \frac {\partial \pi_ {\mathrm{NNN}}}{\partial \mu} \right| _ {\mu = \mu_ {\mathrm{NNN}} ^ {*}} = 0.
$$

Since

$$
\begin{array}{c} \frac {\partial \pi_ {\mathrm{NN}}}{\partial \mu} \leq \frac {\partial \pi_ {\mathrm{NNN}}}{\partial \mu}, \\ \frac {\partial \pi_ {\mathrm{NNN}}}{\partial \mu} \bigg | _ {\mu = \mu_ {\mathrm{NNN}} ^ {*}} = 0 = \frac {\partial \pi_ {\mathrm{NN}}}{\partial \mu} \bigg | _ {\mu = \mu_ {\mathrm{NN}} ^ {*}} \leq \frac {\partial \pi_ {\mathrm{NNN}}}{\partial \mu} \bigg | _ {\mu = \mu_ {\mathrm{NN}} ^ {*}}. \end{array}
$$

Second-order condition gives $\begin{array} { r } { \frac { \partial ^ { 2 } \pi _ { \mathrm { N N } } } { \partial \mu ^ { 2 } } < 0 } \end{array}$ and $\frac { \partial ^ { 2 } \pi _ { \mathrm { N N N } } } { \partial \mu ^ { 2 } } \ < \ 0 .$ Hence $\frac { \partial \pi _ { \mathrm { N N } } } { \partial \mu }$ and $\frac { \partial \pi _ { \mathrm { N N N } } } { \partial \mu }$ decrease in $\mu .$ Therefore $\mu _ { \mathrm { N N N } } ^ { * } \geq \mu _ { \mathrm { N N } } ^ { * } .$

## Appendix H. Proof of Proposition 4 (Whether ISP’s Optimal Capacity Choice Is Socially Optimal)

The long-run social welfare under NN is

$$
\mathrm{SW} _ {\mathrm{NN}} = \frac {1}{1 - \delta} \left[ V (\lambda) - \frac {t}{4} - \frac {d \lambda}{\mu - \lambda} + \frac {1}{2} \lambda r _ {Y} + \frac {1}{2} \lambda r _ {G} \right] - C (\mu).
$$

The socially optimal capacity is derived by the first-order condition $\begin{array} { r } { \frac { \partial \mathsf { S } \mathsf { W } _ { \mathrm { N N } } } { \partial \mu } = 0 . } \end{array}$ . Since $\begin{array} { r } { \frac { \partial \overline { { \pi } } _ { \mathrm { N N } } } { \partial \mu } = \frac { \partial { S W _ { \mathrm { N N } } } } { \partial \mu } } \end{array}$ , the $\mathrm { I S P ^ { \prime } s }$ optimal capacity decision that maximizes his profit coincides with that of the long-run social welfare. Namely, ISP always invests at the socially optimal level under NN.

The long-run social welfare under Case A in the absence of net neutrality (NNN\_A) is

$$
\begin{array}{c} S W _ {\text {NNN\_A}} = \frac {1}{1 - \delta} \bigg [ V (\lambda) - t \bigg (\frac {1}{2} - x _ {3} ^ {2} \bigg) - \frac {d \lambda}{\mu - (1 - x _ {3}) \lambda} \\ + x _ {3} \lambda r _ {Y} + (1 - x _ {3}) \lambda r _ {G} \bigg ] - C (\mu), \end{array}
$$

which can be rewritten as

$$
\begin{array}{c} \mathrm{SW} _ {\mathrm {NNN\_A}} = \frac {1}{1 - \delta} \bigg [ V (\lambda) - t \bigg (\frac {1}{2} - x _ {3} ^ {2} \bigg) - 2 t \bigg (\frac {1}{2} - x _ {3} \bigg) \bigg (\frac {\mu}{\lambda} - 1 \bigg) \\ + x _ {3} \lambda r _ {Y} + (1 - x _ {3}) \lambda r _ {G} \bigg ] - C (\mu). \end{array}
$$

After some algebra, one has

$$
\frac {\partial \mathrm{SW} _ {\mathrm {NNN\_A}}}{\partial \mu} - \frac {\partial \pi_ {\mathrm {NNN\_A}}}{\partial \mu} = \frac {1}{1 - \delta} [ \lambda r _ {Y} - t (1 - 2 x _ {3}) ] \frac {\partial x _ {3}}{\partial \mu}.
$$

We find that $\begin{array} { r } { \frac { \partial S W _ { \mathrm { N N N } , \mathrm { A } } } { \partial \mu } > \frac { \partial \pi _ { \mathrm { N N N } , \mathrm { A } } } { \partial \mu } } \end{array}$ when $\begin{array} { r } { r _ { Y } \ge \frac { t } { \lambda } ( 1 - 2 x _ { 3 } ) } \end{array}$ . That is, the ISP underinvests in capacity.

If, however, $\begin{array} { r } { r _ { Y } < \frac { t } { \lambda } ( 1 - 2 x _ { 3 } ) } \end{array}$ , then $\begin{array} { r } { \frac { \partial S W _ { \mathrm { N N N \mathrm { \mathbf { N } } , A } } } { \partial \mu } \ < \ \frac { \partial \pi _ { \mathrm { N N N \mathbf { N } } , \mathrm { A } } } { \partial \mu } } \end{array}$ resulting in the ISP overinvesting in capacity.

For the Case B in the absence of net neutrality (NNN\_B), the long-run social welfare is

$$
\mathrm{SW} _ {\text { NNN\_B }} = \frac {1}{1 - \delta} \left[ V (\lambda) - \frac {t}{4} - \frac {d \lambda}{\mu - \lambda} + \frac {1}{2} \lambda r _ {Y} + \frac {1}{2} \lambda r _ {G} \right] - C (\mu).
$$

Since $\begin{array} { r } { \frac { \partial S W _ { \mathrm { N N N N \mathrm { ~ B ~ } } } } { \partial \mu } > \frac { \partial \pi _ { \mathrm { N N N \mathrm { ~ B ~ } } } } { \partial \mu } . } \\ { \mathbf { D } \mathbin { \sim } c \mathrm { ~ \Gamma ~ } \mathrm { ~ a ~ n ~ m ~ } \mathrm { ~ r ~ } } \end{array}$ , the ISP always underinvests under Case B of NNN.

## References

Anderson, C. 2008. Free! Why \$0.00 is the future of business. Wired 16(February 25) 140–194.

Armstrong, M. 2006. Competition in two-sided markets. RAND J. Econom. 37(3) 668–691.

Armstrong, M., J. Wright. 2007. Two-sided markets, competitive bottlenecks and exclusive contracts. Econom. Theory 32(2) 353–380.

Bandyopadhyay, S., H. K. Cheng. 2006. Liquid pricing for digital infrastructure services. Internat. J. Electronic Commerce 10(4) 47–72.

Berners-Lee, T. 2006. Neutrality on the net. Accessed February 13, 2009, http://dig.csail.mit.edu/breadcrumbs/node/132.

Bhargava, H. K., D. Sun. 2005. Quality-contingent pricing for broadband services. Proc. Hawaii Internat. Conf. Systems Sci., Big Island, HI, 211b–220b.

Brander, J. A., B. J. Spencer. 1983. Strategic commitment with R&D: The symmetric case. Bell J. Econom. 14(1) 225–235.

Carr, N. 2008. The Big Switch: Rewiring the World, from Edison to Google. W. W. Norton, New York.

Dyson, E. 1994. Intellectual Property on the Net. Edventure Holdings Inc., New York.

Economides, N. 2007. Nonbanks in the payments system: Vertical integration issues. NET Institute Working Paper 07-06, Stern School of Business, New York University, New York.

Economides, N. 2008. “Net neutrality,” non-discrimination and digital distribution of content through the Internet. I/S: A J. Law Policy Inform. Soc. 4(2) 209–233.

Economides, N., S. C. Salop. 1992. Competition and integration among complements and network market structure. J. Indust. Econom. 40(1) 105–123.

Economides, N., J. Tag. 2007. Net neutrality on the Internet: A two-sided market analysis. NET Institute Working Paper 07-14, Stern School of Business, New York University, New York.

Edell, R. J., P. P. Varaiya. 1999. Providing Internet access: What we learn from the INDEX trial. INDEX Project Report 99-010W, University of California at Berkeley, Berkeley.

Hahn, R., S. Wallsten. 2006. The economics of net neutrality. The Berkeley Econom. Press Economists’ Voice 3(6) 1–7.

Hausman, J. A., J. G. Sidak, H. J. Singer. 2001. Residential demand for broadband telecommunications and consumer access to Yale J. Regulation 18 129–173.

Hearing on “Network Neutrality: Competition, Innovation, and Nondiscriminatory Access.” 2006. House Committee on the Judiciary Telecom and Antitrust Task Force, Washington, DC, http://ssrn.com/abstract=903118.

Helm, B. 2006. Tech giants’ Internet battles. Accessed February 13, 2009, http://www.businessweek.com/technology/content/apr2006/

tc20060426\_553893.htm?chan=technology\_technology+index+ page\_more+of+today.

Hermalin, B. E., M. L. Katz. 2007. The economics of productline restrictions with an application to the network neutrality debate. Inform. Econom. Policy 19 215–248.

Hotelling, H. 1929. Stability in competition. Econom. J. 39(153) 41–57.

House of Representatives. 2008. Internet Freedom Preservation Act of 2008. http://thomas.loc.gov/cgi-bin/query/ z?c110:H.R.5353.

Jamison, M. A., J. A. Hauge. 2007. Getting what you pay for: Analyzing the net neutrality debate. Accessed August 16, 2008, http://ssrn.com/abstract=1081690.

Knowledge@Wharton. 2008. Betting on betas: How Internet entrepreneurs are creating new paths to online revenue. Accessed October 15, 2008, http://knowledge.wharton.upenn. edu/article.cfm?articleid=2015.

Krim, J. 2005. Executive wants to charge for Web speed. Washington Post (December 1) D05.

Krugman, P. 2008. Bits, bands and books. New York Times. Accessed February 13, 2009, http://www.nytimes.com/2008/06/ 06/opinion/06krugman.html.

Kurose, J. F., K. W. Ross. 2003. Computer Networking: A Top-Down Approach Featuring the Internet. Addison-Wesley, Reading, MA.

Mendelson, H. 1985. Pricing computer services: Queueing effects. Comm. ACM 28(3) 312–321.

McKinsey Quarterly. 2009. Hal Varian on how the Web challenges managers. Accessed February 9, 2009, http://www. mckinseyquarterly.com/Strategy/Innovation/Hal\_Varian\_ on\_how\_the\_Web\_challenges\_managers\_2286.

Roller, L.-H., M. M. Tombak. 1990. Strategic choice of flexible production technologies and welfare implications. J. Indust. Econom. 38(4) 417–431.

Shapiro, C., H. R. Varian. 1998. Versioning: The smart way to sell information. Harvard Bus. Rev. (November–December) 106–114.

Sydell, L. 2006. Internet debate—Preserving user parity. All Things Considered, NPR, April 25.

Sydell, L. 2007. Firms abandon online subscription plans. All Things Considered, NPR, September 19.

Thierer, A. D. 2004. “Net Neutrality” Digital Discrimination or Regulatory Gamesmanship in Cyberspace? Cato Institute, Washington, DC.

Turner, S. D. 2005. Broadband Reality Check: The FCC Ignores America’s Digital Divide. Consumers Union, Consumer Federation of America, Free Press.

Turner, S. D. 2007. Give net neutrality a chance. Accessed July 12, 2008, http://www.businessweek.com/technology/content/ jul2007/tc20070712\_243240.htm?campaign\_id=rss\_daily.

Waldmeir, P. 2006. The net neutrality dogfight that is shaking up cyberspace. Financial Times (March 23) B12.

Wilson, F. 2008. Make money around free content. Accessed February 13, 2009, http://howto.wired.com/wiki/Make\_ Money\_Around\_Free\_Content.

WSJ (Wall Street Journal). 2006. Should the net be neutral? Accessed February 13, 2009, http://online.wsj.com/article/ SB114839410026160648.html.

Wu, T. 2003. Network neutrality, broadband discrimination. J. Telecomm. High Tech. Law 2 141.

Wu, T. 2006a. Network neutrality: Competition, innovation, and nondiscriminatory access. Working paper, Columbia University Law School, New York. http://ssrn.com/abstract= 903118.

Wu, T. 2006b. Net neutrality FAQ. Accessed February 13, 2009. http://www.timwu.org/network\_neutrality.html.

Yang, C., M. Ihlwan, H. Tashiro. 2004. Commentary: Behind in broadband. Business Week. Accessed February 13, 2009, http://www.businessweek.com/magazine/content/04\_36/ b3898111\_mz063.htm.
