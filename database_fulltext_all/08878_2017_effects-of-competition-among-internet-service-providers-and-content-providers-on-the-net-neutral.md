---
otero_id: 8878
otero_key: "95SY3K9J"
title: "Effects of Competition among Internet Service Providers and Content Providers on the Net Neutrality Debate1"
authors: "Hong Guo; Subhajyoti Bandyopadhyay; Arthur Lim; Yu-Chen Yang; Hsing Kenneth Cheng"
year: "2017"
journal: "MIS Quarterly"
doi: "10.25300/misq/2017/41.2.02"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# EFFECTS OF COMPETITION AMONG INTERNET SERVICE PROVIDERS AND CONTENT PROVIDERS ON THE NET NEUTRALITY DEBATE

Hong Guo<sup>\*</sup>, Subhajyoti Bandyopadhyay<sup>\*\*</sup>, Arthur Lim<sup>\*</sup>, Yu-Chen Yang<sup>\*\*\*</sup>, Kenny Cheng<sup>\*\*</sup>

\* University of Notre Dame, {hguo, arthurlim}@nd.edu

\*\* University of Florida, {shubho.bandyopadhyay, kenny.cheng}@warrington.ufl.edu

\*\*\* National Sun Yat-sen University, ycyang@mis.nsysu.edu.tw

## ABSTRACT

Supporters of net neutrality have often argued that more competition among Internet service providers (ISPs) is beneficial for an open Internet and that the market power of the ISPs lies at the heart of the net neutrality debate. However, the joint effects of the competition among ISPs and among content providers (CPs) have yet to be examined. We study the critical linkage between ISP competition and CP competition, as well as its policy implications. We find that even under competitive pressure from a rival ISP, an ISP still has the incentive and the ability to enforce charging CPs for priority delivery of content. Upending the commonly held belief that when facing direct competition CPs will always support the preservation of net neutrality, we find that under certain conditions, it is economically beneficial for the dominant CP to reverse its stance on net neutrality. Our paper also makes an important contribution in extending the traditional multi-dimensional spatial-competition literature.

Keywords: Net Neutrality, Internet Service Provider Competition, Content Provider Competition, Packet Discrimination, Social Welfare

# EFFECTS OF COMPETITION AMONG INTERNET SERVICE PROVIDERS AND CONTENT PROVIDERS ON THE NET NEUTRALITY DEBATE

## INTRODUCTION

The Federal Communications Commission (FCC)’s path to enforce net neutrality rules to preserve an open Internet has been complicated and controversial. In its 2010 Open Internet Order, the FCC proposed net neutrality rules consisting of four core principles: transparency, no blocking, no unreasonable discrimination, and reasonable network management (FCC 2010). These rules were later struck down by the U.S. Court of Appeals for the District of Columbia Circuit, which assessed that the FCC only has limited regulatory options for broadband as an information service (Nagesh and Sharma 2014). During a five-month period in 2014, the FCC solicited public comments on net neutrality issue and received nearly 4 million comments, which makes it the most commented-upon issue in the agency’s history. In February 2015, the FCC introduced its new open Internet rules (FCC 2015), but was soon challenged again in court (Risen 2015).

Proponents of net neutrality have long opined that a lack of effective competition in the local broadband market enables Internet service providers (ISPs) to act as gatekeepers of content, and thus to be in a position to charge content providers (CPs) for priority delivery of their data packets<sup>1</sup>. The appeals court made the same argument as part of its ruling: “...if end users could immediately respond to any given broadband provider’s attempt to impose restrictions on edge providers by switching broadband providers, this gatekeeper power might well disappear... For example, a broadband provider like Comcast would be unable to

threaten Netflix that it would slow Netflix traffic if all Comcast subscribers would then immediately switch to a competing broadband provider.” (U.S. Court of Appeals 2014)

Supporters of net neutrality have often argued that more competition among ISPs is beneficial for an open Internet (Glaser 2014; Dunbar 2014) and that the market power of the ISPs lies at the heart of the net neutrality debate (Mcmillan 2014; Winegarden 2014). They argue that competition among ISPs would prevent them from gaining the market power that currently allows them to charge consumers supra-competitive prices for Internet access and to potentially charge CPs for preferential delivery. In fact, there have been several calls to remove the barriers to a competitive broadband market (Szoka et al. 2013).

In this paper, we investigate whether the presence of competition in local broadband markets would indeed prevent ISPs from charging online CPs for preferential delivery. Our analysis builds upon the extant research of Choi and Kim (2010) and Cheng et al. (2011), who examined the net neutrality issue for a monopoly ISP. The contribution of our research is to show that, even under competitive pressure from a rival ISP, an ISP still has the incentive and the ability to enforce charging CPs for priority delivery of content.

The issue of competition among CPs has thus far taken a back seat in the net neutrality debate. CPs have been among the strongest proponents of net neutrality (The Internet Association 2014). Recent developments, however, show some deviations from this stance. Manjoo (2014) observed that in contrast to the recent grassroots movements over the ongoing discussions regarding net neutrality regulation, the large Internet companies “have not joined online protests, or otherwise moved to mobilize their users in favor of new rules.” Google has been questioned for its stance on net neutrality after its entry into the broadband market through Google Fiber (Singel 2013). Two important issues remain unaddressed: to wit, how competitive pressures drive CPs to pay for preferential delivery and how their choices affect the ISPs’ incentives to manage their traffic.

We investigate the impact of CP competition in the presence of ISP competition. One question that is of particular interest is whether sufficient market power of the CP encourages it to abandon its support for net neutrality. We find that a dominant CP may be better off without net neutrality given sufficient market power relative to that of the ISPs. We study the critical linkage between ISP competition and CP competition, as well as its policy implications. Our findings suggest that the impact of net neutrality regulation on the incentives of CPs depends critically on the market power of the competitors both within the local ISP market and within the content market.

Apart from these policy prescriptions, this paper makes an important contribution in extending the traditional multi-dimensional spatial-competition literature. The proposed model captures the relevant characteristics of data transmission in the net neutrality debate. More generally, the modeling framework can be used to analyze the competition between two sets of firms providing complementary products that are consumed together to constitute the total end-user experience (e.g. computer hardware platforms and the software on those platforms).

The paper is organized as follows: In the next section, we review the related literature and discuss the contributions of this paper. We then propose a game-theoretical model of Internet data transmission in the presence of both ISP competition and CP competition. Following that, we analyze the outcomes under both net neutrality and packet discrimination regimes with a focus on the impact of ISP competition and CP competition. We then discuss the implications of relaxing some of the model assumptions. The paper concludes with theoretical, managerial, and policy implications.

## LITERATURE REVIEW

In this section, we first review the fast-growing literature of economic analysis of net neutrality. For a broader review of the network neutrality literature see Krämer et al. (2013). Studies in network interconnection (Armstrong 1998; Laffont et al. 2003; Tan et al. 2006; Chiang and Jhang-Li 2014) focus on the issues of interconnection settlements among backbone network providers. The issue of net neutrality, however, focuses on “last-mile” ISPs that provide Internet access services to their local consumers. Existing models make different assumptions about the market structure of Internet data transmission within the last mile and find a variety of results on the key economic outcomes (such as content innovation, social welfare, etc.) in the net neutrality debate.

Hermalin and Katz (2007) find that net neutrality reduces the set of available content and thus leads to lower content innovation. Economides and Tåg (2012) conclude that there are more active CPs under net neutrality when the value of an additional consumer to the CPs exceeds the value of an additional CP to the consumers. Guo et al. (2012) find that packet discrimination can hinder the ability of startups to compete against established rivals and thus reduce content innovation at the edge. Krämer and Wiewiorra (2012) model congestion-sensitive CPs with differing congestion-sensitivity distributions and find that content innovation is lower under net neutrality for less congestion-sensitive CPs and higher for more congestion-sensitive CPs. Guo and Easley (2014) find that net neutrality results in higher content innovation because of the existence of a pro bono innovation zone.

The results are mixed when it comes to evaluating the impact of the potential net neutrality regulation on social welfare. Some papers (Cheng et al. 2011; Guo et al. 2012; Krämer and Wiewiorra 2012; Bourreau et al. 2014; Guo and Easley 2014) find that net neutrality results in lower social welfare compared to packet discrimination, while others (Hermalin and Katz 2007; Choi and Kim 2010; Economides and Hermalin 2012; Economides and Tåg 2012) obtain mixed welfare results. Most of the articles suggest, however, that if packet discrimination were permitted, the ISP would be better off while most CPs would be worse off<sup>2</sup>, due to the ISP's added flexibility in network management.

From the perspective of modeling ISP competition, most extant models consider a monopoly ISP, though Hermalin and Katz (2007) and Economides and Tåg (2012) extend their models to consider the effects of ISP competition and in either case find results similar to the monopoly case. Bourreau et al. (2014) extend the model proposed in Krämer and Wiewiorra (2012) to allow ISP competition. They find that the packet discrimination regime results in higher infrastructure investment, more content innovation, and higher overall social welfare. The ISPs, however, may be worse off under the packet discrimination regime, due to intensified competition in the consumer market. Bykowsky and Sharkey (2014) study the welfare effects of the zero-price rule under various conditions of the ISPs’ market power. They find that the zero-price rule is welfare enhancing if and only if the ISP’s ability to establish competitive prices for the CPs exceeds its ability to establish such prices for consumers. Broos and Gautier (2015) look at the issue of ISPs excluding certain apps on their network, and their research indicates that in the presence of duopoly ISPs, the app may be offered only by one firm. However, prohibiting the exclusion of the app does not improve social welfare.

From the perspective of modeling CP competition, most papers assume that CPs are the sole providers of their own content and do not compete for consumers. As a result, these models are unable to capture the competitive pressure on the CPs to pay for preferential delivery service under a packet discrimination regime. Other papers (Choi and Kim 2010;

Guo et al. 2010; Cheng et al. 2011; Guo et al. 2013) consider the competition for consumers between two CPs, but assume that the service of delivering the content is provided by a monopolist ISP. Choi and Kim (2010) and Cheng et al. (2011) find that the ISP’s incentive to expand infrastructure capacity is higher under net neutrality. Guo et al. (2010) find that without net neutrality, when the ISP integrates with a CP, social welfare may decrease in certain cases, or increase at the expense of the competing pure-play CP in other cases. Furthermore, the vertically integrated ISP does not always degrade, and sometimes even prioritizes, the competing content. Guo et al. (2013) find that given the freedom to engage in non-neutral traffic management at both the CP side and the consumer side of the market, the ISP does not always discriminate both sides.

This paper is among the first to examine the joint effects of the competition among CPs and among ISPs in the context of net neutrality. Brito et al. (2013) study the competition among CPs and ISPs and find that the ISPs prefer to sell the highest quality of service to CPs with the highest advertising revenue. In their paper, consumers’ choice of ISP and CP are modeled as independent decisions, and therefore, the interaction between the competition among CPs and ISPs cannot be examined. Kourandi et al. (2014) investigate the impact of the net neutrality regulation on Internet fragmentation through exclusivity contracts between ISPs and CPs. They find that the zero-price rule on traffic termination is neither sufficient nor necessary to prevent Internet fragmentation. They study the competition among CPs and ISPs in the context of Internet fragmentation, an extreme case of non-neutral Internet when some content is not delivered by all ISPs. For example, if Comcast and Netflix enter an exclusivity contract, then Netflix’s content will be available only to Comcast subscribers and nobody else. In contrast, our paper studies a less severe case of non-neutral Internet – that of paid fast lanes, which is what the net neutrality debate has mostly been concerned with. This paper fills the research gap by studying the linkage between the markets of Internet access services and digital content in the context of paid fast lanes. Given the different roles of CPs and ISPs, it is important to investigate the impact of the competition among both these types of players on the outcomes. If one of the two markets is modeled as a monopoly, then that monopolist has greater market power to influence the outcomes of the other market. This is different from what is observed in reality, where the effects of competition in one market mediate the effects of competition in the other market. We find that the impact of net neutrality on some key outcomes such as the CPs’ profit critically depends on the relative strength of the ISP competition and the CP competition.

This paper also makes a theoretical contribution to the literature of multi-dimensional spatial competition with horizontal differentiation in both dimensions. There has been various efforts to extend the analysis of product competition from single dimension to two- or multi-dimensional product competition (Caplin and Nalebuff 1986). Matutes and Regibeau (1988) model two firms each producing two complementary components that are horizontally differentiated. They find that the firms choose full compatibility for their systems, which lead to higher prices. Tabuchi (1994) considers a two-dimensional setting and finds that maximum differentiation arises along one dimension, while minimum differentiation arises along the other dimension. Irmen and Thisse (1998) and Ansari et al. (1998) extend Tabuchi’s model to multiple horizontal dimensions and find that firms maximize differentiation on one dimension while minimizing differentiation along all others. von Ehrlich and Greiner (2013) adapt two-dimensional spatial-competition models to the context of media markets and analyze two media outlets providing both online and offline platforms. They find that maximum differentiation may occur in both dimensions.

This paper contributes to the traditional multi-dimensional spatial-competition literature in three ways. First, we analyze two interrelated markets with complementary products (the markets of Internet access services and digital content) as opposed to multiple product attributes in the same market, which has been considered in prior studies. In the existing multi-dimensional spatial-competition models, consumers choose between two firms based on multiple product attributes, e.g. between two computer printer manufacturers based on their products’ speed, noise, and clarity of output (Caplin and Nalebuff 1986). However, the two dimensions in our model represent two different but complementary duopoly markets. Consequently, consumers have to choose between two ISPs as well as between two CPs, i.e., choose among four ISP-CP combinations. Second, since the ISPs and the CPs know the mechanism of the consumers’ decision-making process, the competition between the CPs moderates the competition between the ISPs (and vice versa). In addition, we allow for different unit fit costs for the two different markets of Internet access services and digital content. In other words, the two markets differ in terms of competition intensity. Third, in the existing multi-dimensional spatial-competition models, a consumer’s choice of firm does not affect other consumers’ choices. In our model, a consumer’s choice of a particular ISP-CP combination does affect the choices of other consumers. The market shares of the ISPs and the CPs are determined by the consumers’ choices among the four ISP-CP combinations. The ISP-CP combination that a consumer finally chooses depends on the waiting times, which in turn depend on the market shares and the CPs’ delivery service choices. The CPs’ delivery service choices in turn depend on the expected waiting times at the ISPs. These interconnected variables (the market shares of the ISP-CP combinations, the waiting times, and the CPs’ delivery service choices) are simultaneously determined in our model. The above three features are key characteristics of the Internet data-transmission process, which is crucial to modeling the net neutrality issue.

## MODEL

## Modeling Framework

We consider two competing ISPs, <sub>??</sub> and <sub>??</sub>, providing Internet access services to a unit mass of consumers and content delivery services to two competing CPs <sub>??</sub> and <sub>??</sub> (as shown in Figure 1).

![](/api/attachments/95SY3K9J/fulltext/images/c02da66c81924ffef575f22234ec1064bc27016180adee7a7a13d6ce8a6516bf.jpg)  
Figure 1: Market Structure

Figure 1 also demonstrates payments the ISPs receive from consumers and potentially from CPs. In the net neutrality regime, the ISPs charge consumers fixed fees $F _ { C }$ and $F _ { D }$ , respectively, for Internet access, which are their only revenue source. In the packet discrimination regime, in addition to fixed fees $( F _ { C }$ and $F _ { D } )$ from consumers, the ISPs may also charge the CPs usage-based fees $p _ { C }$ and $p _ { D }$ , respectively, for preferential delivery of their content. In other words, the ISPs have two revenue sources in the packet discrimination regime – Internet access fees from consumers and preferential delivery fees from CPs. Table 1 provides a list of all notations.

Table 1: List of Notations

<table><tr><td>Subscript a</td><td>ISP a = C or D</td></tr><tr><td>Subscript b</td><td>CP b = Y or G</td></tr><tr><td>Subscript i</td><td>Outcome i = 1 (Neither CP pays), 2 (Only Y pays), 3 (Only G pays), and 4 (Both CPs pay) representing CPs&#x27; content delivery choices on ISP C</td></tr><tr><td>Subscript j</td><td>Outcome j = 1 (Neither CP pays), 2 (Only Y pays), 3 (Only G pays), and 4 (Both CPs pay) representing CPs&#x27; content delivery choices on ISP D</td></tr><tr><td> $F_{aij}$ </td><td>Fixed fee ISP a = C or D charges consumers for Internet access service in outcome ij</td></tr><tr><td> $p_{aij}$ </td><td>Usage-based fee ISP a = C or D charges CPs for preferential delivery in outcome ij</td></tr><tr><td>V</td><td>Consumers&#x27; gross valuation for each ISP-CP combination</td></tr><tr><td> $I_{abij}$ </td><td>Indicator function to represent whether CP b pays ISP a for preferential delivery in outcome ij</td></tr><tr><td> $u_{abij}(x,z)$ </td><td>Utility of the ISP-CP combination ab for consumer (x,z) in outcome ij</td></tr><tr><td> $U_{ij}(x,z)$ </td><td>Utility of the preferred ISP-CP combination for consumer (x,z) in outcome ij</td></tr><tr><td> $N_{abij}$ </td><td>Market share of the ISP-CP combination ab in outcome ij</td></tr><tr><td> $N_{aij}$ </td><td>Market share of ISP a = C or D in outcome ij and  $N_{aij} = N_{ayij} + N_{agij}$ </td></tr><tr><td> $N_{bij}$ </td><td>Market share of CP b = Y or G in outcome ij and  $N_{bij} = N_{Cbij} + N_{Dbij}$ </td></tr><tr><td>t</td><td>Unit fit cost for content</td></tr><tr><td>k</td><td>Unit fit cost for Internet access service</td></tr><tr><td> $r_b$ </td><td>Revenue rate per packet of CP b = Y or G</td></tr><tr><td>d</td><td>Consumers&#x27; unit delay cost (unit congestion cost)</td></tr><tr><td> $w_{abij}$ </td><td>Expected waiting time (expected delay) for consumers who choose ISP a and CP b in outcome ij</td></tr><tr><td>λ</td><td>Poisson arrival rate of content requested by each consumer, expressed in packets per unit of time.</td></tr><tr><td>μ</td><td>Capacity that the ISPs provide to the consumers, expressed in packets per unit of time</td></tr><tr><td> $π_{aij}$ </td><td>Profit of ISP a = C or D</td></tr><tr><td> $π_{bij}$ </td><td>Profit of CP b = Y or G</td></tr><tr><td> $CS_{ij}$ </td><td>Consumer surplus in outcome ij</td></tr><tr><td> $SW_{ij}$ </td><td>Social welfare in outcome ij</td></tr></table>

We use a two-dimensional spatial-competition model to capture consumers heterogeneous preferences for both content and Internet access service, and firm competition in these two markets. Specifically, consumers, characterized by their preference for content (<sub>??</sub>) and preference for Internet access service (<sub>??</sub>), are uniformly distributed on a unit square. Without loss of generality, we assume that the horizontal axis represents consumers’ preference for content (CP <sub>??</sub> located at 0 and CP <sub>??</sub> located at 1); the vertical axis represents consumers’ preference for Internet access service (ISP <sub>??</sub> located at 0 and ISP <sub>??</sub> located at 1). Consumers have four choices (i.e., the four ISP-CP combinations <sub>??</sub> , <sub>??</sub> , <sub>??</sub> , and <sub>??</sub> ), represented by the four corners of the unit square.

Let <sub>??</sub> be consumers’ gross valuation for each ISP-CP combination. We denote the unit fit cost for content and Internet access service as <sub>??</sub> and <sub>??</sub>, respectively, and use the weighted box topology distance measure to calculate the fit cost in consumers’ utility functions. As shown in Figure 2, when choosing the ISP-CP combination of <sub>??</sub> , the consumer located at $( x , z )$ incurs a fit cost for content of <sub>??</sub> and a fit cost for Internet access service of <sub>??</sub> . Similarly, consumer $( x , z ) \ ' \mathrm { s }$ fit costs for the other three ISP-CP combinations can be calculated by multiplying the unit fit cost (<sub>??</sub> or <sub>??</sub>) by the corresponding (horizontal or vertical) distance between the consumer and the ISP-CP combination.

![](/api/attachments/95SY3K9J/fulltext/images/3949595f149679333a2e23926be0091c34797fa5bb6abf98b7f4ebef9e8c4fa9.jpg)  
Figure 2: Consumer Choice

For ISP $a = C$ <sub>or</sub> <sub>??</sub>, CPs may decide whether to pay for preferential delivery of their content. The content delivery service choice of CP $b = Y$ <sub>or</sub> <sub>??</sub> can be represented by an indicator function $I _ { a b }$ , where $I _ { a b } = 1$ , if CP <sub>??</sub> pays ISP <sub>??</sub> for preferential delivery; $I _ { a b } = 0$ , otherwise. In other words,

$I _ { C Y } = 1$ , if CP <sub>??</sub> pays ISP <sub>??</sub> for preferential delivery; $I _ { C Y } = 0$ , otherwise.

<sub>?? =</sub> <sub>1</sub>, if CP <sub>??</sub> pays ISP <sub>??</sub> for preferential delivery; $I _ { C G } = 0$ , otherwise.

<sub>?? = 1</sub>, if CP <sub>??</sub> pays ISP <sub>??</sub> for preferential delivery; $I _ { D Y } = 0$ , otherwise.

<sub>?? = 1</sub>, if CP <sub>??</sub> pays ISP <sub>??</sub> for preferential delivery; $I _ { D G } = 0$ , otherwise.

There are four outcomes for each ISP based on the two $\mathrm { C P s } ^ { \prime }$ delivery service choices: outcome 1 (neither CP pays for preferential delivery), outcome 2 (only <sub>??</sub> pays), outcome 3 (only <sub>??</sub> pays), and outcome 4 (both CPs pay). Thus, there are 16 outcomes in all, based on the $\mathrm { C P s } ^ { \prime }$ delivery service choices for the two ISPs, represented by outcome <sub>??</sub> , with $i , j =$ (outcomes 11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44).

These outcomes are summarized in Table 2. Any one of these outcomes <sub>??</sub> is dictated by the $\mathrm { C P s } ^ { \prime }$ delivery service choices for the two ISPs, i.e., the indicator functions $\left( I _ { C Y i j } , I _ { C G i j } , I _ { D Y i j } , I _ { D G i j } \right)$ represent the CPs <sub>??</sub> and $G '$ s delivery service choice for the ISPs <sub>??</sub> and <sub>??</sub>, respectively. Consider outcome 43 as an example, in our notation, the first number (4) refers to the fact that both CPs pay ISP <sub>??</sub> for preferential delivery, and the second number (3) refers to the fact that only <sub>??</sub> pays ISP <sub>??</sub> for preferential delivery. In other words, $I _ { C Y 4 3 } = 1$ $I _ { C G 4 3 } = 1$ $I _ { D Y 4 3 } = 0$ , and $I _ { D G 4 3 } = 1$

Table 2: The 16 Potential Outcomes

<table><tr><td></td><td>Neither CP pays D</td><td>Y pays D</td><td>G pays D</td><td>Both CPs pay D</td></tr><tr><td>Neither CP pays C</td><td>Outcome 11</td><td>Outcome 12</td><td>Outcome 13</td><td>Outcome 14</td></tr><tr><td>Y pays C</td><td>Outcome 21</td><td>Outcome 22</td><td>Outcome 23</td><td>Outcome 24</td></tr><tr><td>G pays C</td><td>Outcome 31</td><td>Outcome 32</td><td>Outcome 33</td><td>Outcome 34</td></tr><tr><td>Both CPs pay C</td><td>Outcome 41</td><td>Outcome 42</td><td>Outcome 43</td><td>Outcome 44</td></tr></table>

Following prior work (Choi and Kim 2010; Cheng et al. 2011; Krämer and Wiewiorra 2012), we model the content delivery systems offered by the two ISPs as two independent M/M/1 queuing systems under net neutrality, one for each ISP. Let <sub>??</sub> denote the capacity of the ISPs and <sub>??</sub> denote the consumers’ rate of requests for content. These two queuing systems are interrelated through the traffic that they receive from consumers. Since the total consumer base is normalized to 1, the total consumer traffic is <sub>??</sub>, which is divided between the two ISPs based on their market shares. Under packet discrimination, the content delivery systems offered by the two ISPs are modeled as two priority M/M/1 queuing systems with two priority classes. In the packet discrimination regime, if only one CP pays for preferential delivery, then its data packets will be transmitted with higher priority compared to data packets from the other CP. However, if both CPs pay for preferential delivery, then all data packets will receive equal priority.

We denote the expected waiting time (expected delay) for consumers who choose ISP <sub>??</sub> and CP <sub>??</sub> in outcome <sub>??</sub> as $w _ { a b i j }$ . Table 3 presents the delays of the 16 outcomes under packet discrimination. Note that outcome 11, where neither CP pays for preferential delivery even with the option to do so, is essentially equivalent to the net neutrality regime.

Table 3: Delays under Packet Discrimination

<table><tr><td>Delays</td><td>Neither pays D</td><td>Y pays D</td><td>G pays D</td><td>Both pay D</td></tr><tr><td>Neither pays C</td><td> $w_{CY11} = w_{CG11} = w_{DY11} = w_{DG11}$  $= \frac{1}{\mu - N_{C11}\lambda}$ </td><td> $w_{CY12} = w_{CG12} = \frac{1}{\mu - N_{C12}\lambda}$  $w_{DY12} = \frac{1}{\mu - N_{DY12}\lambda}$  $w_{DG12} = \frac{\mu}{(\mu - N_{DY12}\lambda)(\mu - N_{D12}\lambda)}$ </td><td> $w_{CY13} = w_{CG13} = \frac{1}{\mu - N_{C13}\lambda}$  $w_{DY13} = \frac{\mu}{(\mu - N_{DG13}\lambda)(\mu - N_{D13}\lambda)}$  $w_{DG13} = \frac{1}{\mu - N_{DG13}\lambda}$ </td><td> $w_{CY14} = w_{CG14} = w_{DY14} = w_{DG14}$  $= \frac{1}{\mu - N_{C14}\lambda}$ </td></tr><tr><td>Y pays C</td><td> $w_{CY21} = \frac{1}{\mu - N_{CY21}\lambda}$  $w_{CG21} = \frac{\mu}{(\mu - N_{CY21}\lambda)(\mu - N_{C21}\lambda)}$  $w_{DY21} = w_{DG21} = \frac{1}{\mu - N_{D21}\lambda}$ </td><td> $w_{CY22} = w_{DY22} = \frac{1}{\mu - N_{CY22}\lambda}$  $w_{CG22} = w_{DG22}$  $= \frac{\mu}{(\mu - N_{CY22}\lambda)(\mu - N_{C22}\lambda)}$ </td><td> $w_{CY23} = \frac{1}{\mu - N_{CY23}\lambda}$  $w_{CG23} = \frac{\mu}{(\mu - N_{CY23}\lambda)(\mu - N_{C23}\lambda)}$  $w_{DY23} = \frac{\mu}{(\mu - N_{DG23}\lambda)(\mu - N_{D23}\lambda)}$  $w_{DG23} = \frac{1}{\mu - N_{DG23}\lambda}$ </td><td> $w_{CY24} = \frac{1}{\mu - N_{CY24}\lambda}$  $w_{CG24} = \frac{\mu}{(\mu - N_{CY24}\lambda)(\mu - N_{C24}\lambda)}$  $w_{DY24} = w_{DG24} = \frac{1}{\mu - N_{D24}\lambda}$ </td></tr><tr><td>G pays C</td><td> $w_{CY31} = \frac{\mu}{(\mu - N_{CG31}\lambda)(\mu - N_{C31}\lambda)}$  $w_{CG31} = \frac{1}{\mu - N_{CG31}\lambda}$  $w_{DY31} = w_{DG31} = \frac{1}{\mu - N_{D31}\lambda}$ </td><td> $w_{CY32} = \frac{\mu}{(\mu - N_{CG32}\lambda)(\mu - N_{C32}\lambda)}$  $w_{CG32} = \frac{1}{\mu - N_{CG32}\lambda}$  $w_{DY32} = \frac{1}{\mu - N_{DY32}\lambda}$  $w_{DG32} = \frac{\mu}{(\mu - N_{DY32}\lambda)(\mu - N_{D32}\lambda)}$ </td><td> $w_{CY33} = w_{DY33}$  $= \frac{\mu}{(\mu - N_{CG33}\lambda)(\mu - N_{C33}\lambda)}$  $w_{CG33} = w_{DG33} = \frac{1}{\mu - N_{CG33}\lambda}$ </td><td> $w_{CY34} = \frac{\mu}{(\mu - N_{CG34}\lambda)(\mu - N_{C34}\lambda)}$  $w_{CG34} = \frac{1}{\mu - N_{CG34}\lambda}$  $w_{DY34} = w_{DG34} = \frac{1}{\mu - N_{D34}\lambda}$ </td></tr><tr><td>Both pay C</td><td> $w_{CY41} = w_{CG41} = w_{DY41} = w_{DG41}$  $= \frac{1}{\mu - N_{C41}\lambda}$ </td><td> $w_{CY42} = w_{CG42} = \frac{1}{\mu - N_{C42}\lambda}$  $w_{DY42} = \frac{1}{\mu - N_{DY42}\lambda}$  $w_{DG42} = \frac{\mu}{(\mu - N_{DY42}\lambda)(\mu - N_{D42}\lambda)}$ </td><td> $w_{CY43} = w_{CG43} = \frac{1}{\mu - N_{C43}\lambda}$  $w_{DY43} = \frac{\mu}{(\mu - N_{DG43}\lambda)(\mu - N_{D43}\lambda)}$  $w_{DG43} = \frac{1}{\mu - N_{DG43}\lambda}$ </td><td> $w_{CY44} = w_{CG44} = w_{DY44} = w_{DG44}$  $= \frac{1}{\mu - N_{C44}\lambda}$ </td></tr></table>

In summary, the consumers’ utility functions for the four ISP-CP combinations are:

$$
u _ {C Y i j} (x, z) = V - t x - k z - d \lambda w _ {C Y i j} - F _ {C i j}
$$

$$
u _ {C G i j} (x, z) = V - t (1 - x) - k z - d \lambda w _ {C G i j} - F _ {C i j}
$$

$$
u _ {D Y i j} (x, z) = V - t x - k (1 - z) - d \lambda w _ {D Y i j} - F _ {D i j}
$$

$$
u _ {D G i j} (x, z) = V - t (1 - x) - k (1 - z) - d \lambda w _ {C Y i j} - F _ {D i j}
$$

where <sub>??</sub> represents the consumers’ unit delay cost (unit congestion cost).

Each consumer compares the four ISP-CP combinations and chooses the option that yields the highest utility. We denote the market share of the ISP-CP combination <sub>??</sub> in outcome ?? as $N _ { a b i j }$ . For example, $N _ { D G 4 3 }$ represents the market share of <sub>??</sub> when both CPs pay ISP <sub>??</sub> but only <sub>??</sub> pays ISP <sub>??</sub>.

## Outline of the Analysis Process

In this subsection, we present an overall structure of the solution process that we employ for analyzing this game. Figure 3 presents a schematic of the flow of content from the CPs to the consumers through the ISPs. For the purposes of illustration, we show the priority of content from the CPs <sub>??</sub> and <sub>??</sub> that would flow through the ISPs <sub>??</sub> and <sub>??</sub> in outcome 43. Recall that in outcome 43, both <sub>??</sub> and <sub>??</sub> pay priority delivery fees to ISP <sub>??</sub>, and therefore neither CP is at an advantage with respect to the other. Thus, the waiting time of consumers for both <sub>??</sub> and <sub>??</sub> on ISP <sub>??</sub> is the same (i.e., $w _ { C Y 4 3 } = w _ { C G 4 3 } )$ . However, on ISP <sub>??</sub>, only <sub>??</sub> pays the priority delivery fee, and as a result, the waiting time of consumers of <sub>??</sub> on ISP <sub>??</sub> is lesser than the waiting time of consumers of <sub>??</sub> on ISP <sub>??</sub> (i.e., $w _ { D G 4 3 } < w _ { D Y 4 3 } )$

![](/api/attachments/95SY3K9J/fulltext/images/819c09a2c17c2ae4dbacba0bbed53de590a2278b90c36902802d22f59eeeaa2e.jpg)  
Figure 3: Schematic of the Flow of Content in Outcome 43

In order to solve for the equilibrium, we start with deriving the market shares, i.e., $N _ { C Y }$ $N _ { C G }$ $N _ { D Y }$ , and $N _ { D G }$ . To derive these market shares, we need to determine the consumers who are indifferent between choosing a particular ISP-CP combination and another ISP-CP combination (the indifferent consumers between <sub>??</sub> and <sub>??</sub> , between <sub>??</sub> and <sub>??</sub> , between <sub>??</sub> and <sub>??</sub> , between <sub>??</sub> and <sub>??</sub> , between <sub>??</sub> and <sub>??</sub> , and between <sub>??</sub> and <sub>??</sub> ). As a result, we have six curves of indifferent consumers, which partition the market into four segments. We can then determine the market shares by calculating the sizes of these segments.

The indifferent consumers, say between the ISP-CP combinations of <sub>??</sub> and <sub>??</sub> , is derived by equating the utilities of the consumers when they access their content from <sub>??</sub> and from <sub>??</sub> . These utilities in turn are dependent on the waiting times of these consumers on <sub>??</sub> and <sub>??</sub> respectively (a higher waiting time leads to a lower utility).

We model that the content is delivered through a queueing mechanism (one queue for each ISP). The number of consumers in a particular “queue” (e.g., $N _ { C Y }$ and $N _ { C G }$ for the queuing system of ISP <sub>??</sub>) affects the waiting time for the consumers within that queue (an increased market share leads to a higher waiting time). However, if a CP pays an ISP for priority delivery while its rival does not (for example, in outcome 43, <sub>??</sub> pays ISP <sub>??</sub> while <sub>??</sub> does not) consumers of that CP will enjoy decreased waiting times and therefore more consumers will move over to that CP on that particular ISP. In outcome 43, where only <sub>??</sub> pays ISP <sub>??</sub>, the extra consumers of <sub>??</sub> on ISP <sub>??</sub> will come from three sources: (i) some consumers of <sub>??</sub> on ISP <sub>??</sub> who now prefer <sub>??</sub> (CP switching); (ii) the consumers of <sub>??</sub> on ISP <sub>??</sub> who would now rather access <sub>??</sub> on ISP <sub>??</sub> (ISP switching); and (iii) consumers of <sub>??</sub> on ISP <sub>??</sub> who would now access <sub>??</sub> on ISP <sub>??</sub> (simultaneous ISP and CP switching).

However, this increased market share of <sub>??</sub> on ISP <sub>??</sub> degrades the experience of these consumers (by increasing their waiting times). These two opposing effects (increasing waiting time from larger market shares and decreasing waiting times by paying the priority delivery fee) finally balance out in equilibrium. Note that this “balancing” needs to be done across all the four ISP-CP combinations simultaneously in order to determine the equilibrium market shares in an outcome. Thus, the waiting times (and therefore the market shares) for consumers within a particular ISP-CP combination is affected by the waiting times (and therefore market shares) of every ISP-CP combination, as well as the CPs’ payment choices on each ISP, and in equilibrium all these effects need to be simultaneously balanced. The surfeit of variables and parameters makes this process extremely complicated. The equilibrium market shares cannot be obtained using ordinary algebra, and hence we resort to group theory. These consumer demand patterns are summarized in Lemma 1.

The solution process is further complicated by the fact that in the ISPs’ profit maximization problem for each of the 16 outcomes, there are six incentive compatibility constraints for the two CPs. These incentive compatibility constraints make the different outcomes intertwined with each other. For example, in order for outcome 43 to be an equilibrium, both CPs <sub>??</sub> and <sub>??</sub> have to calculate their profits from three other possible outcomes each and then find that the delivery service choices in outcome 43 are their preferred choices. These different incentive compatibility constraints are summarized in Table 4.

We then eliminate all the dominated outcomes to derive the possible equilibrium outcomes, which are summarized in Lemma 2. Finally, within the universe of possible parameter values, we find out the market conditions under which each of remaining outcomes is the equilibrium. This enables us to characterize the different equilibria for changing parameter values. The equilibrium results are summarized in Lemma 3 (and graphically in Figure 6). Based on these equilibrium results, we present our main findings in Propositions 1, 2 3 and 4. In the next subsection, we formally describe the decision problems for the CPs and the ISPs. Following that, in the next section, we solve for the equilibrium under both the net neutrality and packet discrimination regimes.

## Formulation of the Decision Problems of the CPs and the ISPs

CPs decide whether to pay ISP <sub>??</sub>, ISP <sub>??</sub>, or both. The profit of CP <sub>?? = ?? or</sub> <sub>??</sub> is:

$$
\pi_ {b i j} = \left(N _ {C b i j} + N _ {D b i j}\right) \lambda r _ {b} - I _ {C b i j} N _ {C b i j} \lambda p _ {C i j} - I _ {D b i j} N _ {D b i j} \lambda p _ {D i j}
$$

where $r _ { b }$ is the revenue rate per packet of CP <sub>??</sub>. The CPs’ profit is their revenue generated from consumers served by both ISPs, net of their payments to the ISPs for preferential content delivery. Without loss of generality, we assume that $r _ { G } \geq r _ { Y }$ , or, CP <sub>??</sub> is more effective in generating revenue from its customer base than is CP <sub>??</sub>.

For any outcome <sub>??</sub> , ISPs make their pricing decisions as follows. ISP $a = C \mathrm { o r } D$ selects its prices $F _ { a i j }$ and $p _ { a i j }$ to maximize its profit $\pi _ { a i j }$ . To ensure that all consumers adopt the Internet access service, we need to consider the consumers’ participation constraint. In other words, consumers choose the ISP-CP combination that yields the highest net utility and we assume that all consumers have nonnegative net utility. This full-market-coverage assumption is commonly made not only in the literature of economics of net neutrality that considers competition among CPs (Choi and Kim 2010; Guo et al. 2010; Cheng et al. 2011; Guo et al. 2013), but also generally in the literature of economics of telecommunications (Armstrong 2002) to achieve analytical closure. To ensure that neither CP has any incentive to deviate from outcome $i j .$ , we need to consider the $\mathrm { C P s } ^ { \prime }$ incentive compatibility constraints. In other words, given the other $\mathrm { C P ^ { \bullet } s }$ delivery service choice, the profit for a CP in outcome <sub>??</sub> needs to be higher than that with its alternative choices. For any outcome, given <sub>??</sub>’s delivery service choice, <sub>??</sub> has three options to deviate from his current choice: change his delivery service choice on <sub>??</sub> only; change his delivery service choice on <sub>??</sub> only; or change his delivery service choice on both ISPs. <sub>??</sub>’s profit under these three options are denoted by $\pi _ { Y i _ { 1 } j _ { 1 } } , \ \pi _ { Y i _ { 2 } j _ { 2 } }$ , and $\pi _ { Y i _ { 3 } j _ { 3 } }$ respectively, and the incentive compatibility constraints ensure that <sub>??</sub>’s profit by employing its strategy in outcome <sub>????</sub> is at least equal to what it would be if he had decided to deviate from his strategy (which he could have done in the three aforementioned ways). Similarly, given $Y _ { \textrm { S } }$ delivery service choice, <sub>??</sub> also has three options to deviate from his current choice: change his delivery service choice on <sub>??</sub> only; change his delivery service choice on <sub>??</sub> only; or change his delivery service choice on both ISPs. <sub>??</sub>’s profit under these three options are denoted by $\pi _ { G i _ { 4 } j _ { 4 } }$ $\pi _ { G i _ { 5 } j _ { 5 } }$ , and $\pi _ { G i _ { 6 } j _ { 6 } }$ respectively, and the incentive compatibility constraints ensure that $G \ ' _ { \mathrm { s } }$ profit by employing his strategy in outcome <sub>??</sub> is at least equal to what it would be if he had

decided to deviate from its strategy (which he could have done in the three aforementioned ways). Formally, the decision problem of ISP <sub>??</sub> can be formulated as:

$$
\max _ {F _ {a i j}, p _ {a i j}} \pi_ {a i j} = (N _ {a Y i j} + N _ {a G i j}) F _ {a i j} + (I _ {a Y i j} N _ {a Y i j} + I _ {a G i j} N _ {a G i j}) \lambda p _ {a i j}
$$

subject to

$$
U _ {i j} (x, z) = \max \bigl \{u _ {C Y i j} (x, z), u _ {C G i j} (x, z), u _ {D Y i j} (x, z), u _ {D G i j} (x, z) \bigr \} \geq 0
$$

$$
\pi_ {Y i j} \geq \pi_ {Y i _ {1} j _ {1}}, \pi_ {Y i _ {2} j _ {2}}, \pi_ {Y i _ {3} j _ {3}}
$$

$$
\pi_ {G i j} \geq \pi_ {G i _ {4} j _ {4}}, \pi_ {G i _ {5} j _ {5}}, \pi_ {G i _ {6} j _ {6}}
$$

The ISPs’ profit consists of two components: payment from consumers for Internet access service and payment from CPs for preferential content delivery. The first set of constraints are the consumers’ participation constraints. A consumer $( x , z )$ compares the net utility of four ISP-CP combinations, i.e., $u _ { C Y i j } ( x , z )$ , $u _ { C G i j } ( x , z )$ $u _ { D Y i j } ( x , z )$ , and $u _ { D G i j } ( x , z )$ and selects the ISP-CP combination that yields the highest net utility, i.e., $U _ { i j } ( x , z )$ . As a result, the consumer market gets divided into four segments (corresponding to the four ISP-CP combinations) and we end up with four consumer participation constraints, one for each segment The full-market-coverage assumption ensures that this utility $U _ { i j } ( x , z )$ is nonnegative for all consumers. The last two sets of constraints are the $\mathrm { C P s ^ { \prime } }$ incentive compatibility constraints. In response to the prices $( F _ { a i j }$ and $p _ { a i j } )$ set by the ISPs, the CPs choose whether to pay for preferential delivery and their choices of content delivery services determine the outcomes <sub>??</sub> , where <sub>??</sub> and <sub>??</sub> take the values 1 (Neither CP pays), 2 (Only <sub>??</sub> pays), 3 (Only <sub>??</sub> pays), and 4 (Both CPs pay), and represent the CPs’ content delivery choices on ISP <sub>??</sub> and <sub>??</sub> respectively.

Let us illustrate this formulation with an example, by considering outcome 43, where both CPs pay ISP <sub>??</sub> and only <sub>??</sub> pays ISP <sub>??</sub>. For outcome 43 to be an equilibrium, there are three incentive compatibility constraints for each CP. Given that <sub>??</sub> pays both ISPs in outcome

43, <sub>??</sub> has three options to deviate from his current choice (of paying <sub>??</sub> but not <sub>??</sub>): (1) not pay either ISP (i.e., change his delivery service choice on <sub>??</sub> only, and since <sub>??</sub> would continue to pay both ISPs, this would correspond to outcome 33); (2) pay both ISPs (i.e., change his delivery service choice on <sub>??</sub> only, which would correspond to outcome 44); or (3) not pay ISP <sub>??</sub> but pay ISP <sub>??</sub> (i.e., change his delivery service choice on both ISPs, which would correspond to outcome 34). Similarly, given <sub>??</sub>’s delivery service choice in outcome 43 (he pays <sub>??</sub> but not <sub>??</sub>), <sub>??</sub> also has three options to deviate from his current choice (of paying both ISPs): (1) not pay <sub>??</sub> but pay <sub>??</sub> (i.e., change his delivery service choice on <sub>??</sub> only, which would correspond to outcome 23); (2) pay <sub>??</sub> but not pay <sub>??</sub> (i.e., change his delivery service choice on <sub>??</sub> only, which would correspond to outcome 41); or (3) not pay either ISP (i.e., change his delivery service choice on both ISPs, which would correspond to outcome 21). Formally, $\pi _ { Y 4 3 } \geq$ $\pi _ { Y 3 3 } , \pi _ { Y 4 4 } , \pi _ { Y 3 4 }$ and $\pi _ { G 4 3 } \geq \pi _ { G 2 3 } , \pi _ { G 4 1 } , \pi _ { G 2 1 }$ . Similarly, we arrive at the $\mathrm { C P s } ^ { \prime }$ incentive compatibility constraints for all the other outcomes, the details of which are presented in Table 4.

Table 4: CPs’ Incentive Compatibility Constraints

<table><tr><td>ICconstraints</td><td>Neither pays D</td><td>Y pays D</td><td>G pays D</td><td>Both pay D</td></tr><tr><td>Neitherpays C</td><td> $\pi_{Y11} \geq \pi_{Y21}, \pi_{Y12}, \pi_{Y22}$  $\pi_{G11} \geq \pi_{G31}, \pi_{G13}, \pi_{G33}$ </td><td> $\pi_{Y12} \geq \pi_{Y22}, \pi_{Y11}, \pi_{Y21}$  $\pi_{G12} \geq \pi_{G32}, \pi_{G14}, \pi_{G34}$ </td><td> $\pi_{Y13} \geq \pi_{Y23}, \pi_{Y14}, \pi_{Y24}$  $\pi_{G13} \geq \pi_{G33}, \pi_{G11}, \pi_{G31}$ </td><td> $\pi_{Y14} \geq \pi_{Y24}, \pi_{Y13}, \pi_{Y23}$  $\pi_{G14} \geq \pi_{G34}, \pi_{G12}, \pi_{G32}$ </td></tr><tr><td>Y pays C</td><td> $\pi_{Y21} \geq \pi_{Y11}, \pi_{Y22}, \pi_{Y12}$  $\pi_{G21} \geq \pi_{G41}, \pi_{G23}, \pi_{G43}$ </td><td> $\pi_{Y22} \geq \pi_{Y12}, \pi_{Y21}, \pi_{Y11}$  $\pi_{G22} \geq \pi_{G42}, \pi_{G24}, \pi_{G44}$ </td><td> $\pi_{Y23} \geq \pi_{Y13}, \pi_{Y24}, \pi_{Y14}$  $\pi_{G23} \geq \pi_{G43}, \pi_{G21}, \pi_{G41}$ </td><td> $\pi_{Y24} \geq \pi_{Y14}, \pi_{Y23}, \pi_{Y13}$  $\pi_{G24} \geq \pi_{G44}, \pi_{G22}, \pi_{G42}$ </td></tr><tr><td>G pays C</td><td> $\pi_{Y31} \geq \pi_{Y41}, \pi_{Y32}, \pi_{Y42}$  $\pi_{G31} \geq \pi_{G11}, \pi_{G33}, \pi_{G13}$ </td><td> $\pi_{Y32} \geq \pi_{Y42}, \pi_{Y31}, \pi_{Y41}$  $\pi_{G32} \geq \pi_{G12}, \pi_{G34}, \pi_{G14}$ </td><td> $\pi_{Y33} \geq \pi_{Y43}, \pi_{Y34}, \pi_{Y44}$  $\pi_{G33} \geq \pi_{G13}, \pi_{G31}, \pi_{G11}$ </td><td> $\pi_{Y34} \geq \pi_{Y44}, \pi_{Y33}, \pi_{Y43}$  $\pi_{G34} \geq \pi_{G14}, \pi_{G32}, \pi_{G12}$ </td></tr><tr><td>Both payC</td><td> $\pi_{Y41} \geq \pi_{Y31}, \pi_{Y42}, \pi_{Y32}$  $\pi_{G41} \geq \pi_{G21}, \pi_{G43}, \pi_{G23}$ </td><td> $\pi_{Y42} \geq \pi_{Y32}, \pi_{Y41}, \pi_{Y31}$  $\pi_{G42} \geq \pi_{G22}, \pi_{G44}, \pi_{G24}$ </td><td> $\pi_{Y43} \geq \pi_{Y33}, \pi_{Y44}, \pi_{Y34}$  $\pi_{G43} \geq \pi_{G23}, \pi_{G41}, \pi_{G21}$ </td><td> $\pi_{Y44} \geq \pi_{Y34}, \pi_{Y43}, \pi_{Y33}$  $\pi_{G44} \geq \pi_{G24}, \pi_{G42}, \pi_{G22}$ </td></tr></table>

Figure 4 shows the timing of the game. In stage 1, ISP $a = C$ <sub>or</sub> <sub>??</sub> sets the fixed fee $F _ { a }$ for end consumers and potentially set a priority price of $p _ { a }$ per packet for the CPs. In stage 2, CP <sub>??</sub> <sub>=</sub> <sub>??</sub> <sub>or</sub> <sub>??</sub> decides to pay or not to pay the ISPs <sub>??</sub> and <sub>??</sub> for preferential delivery of his content. In stage 3, consumers choose their preferred CP and ISP.

<table><tr><td>Stage 1</td><td>Stage 2</td><td>Stage 3</td></tr><tr><td>ISPs set  $F_C$  and  $F_D$  for end consumers and potentially set priority prices of  $p_C$  and  $p_D$  per packet for the CPs</td><td>CPs decide to pay or not to pay the ISPs for preferential delivery of their content.</td><td>Consumers choose their preferred CP and ISP.</td></tr></table>

Figure 4: Timing of the Game

## ANALYSIS OF NET NEUTRALITY AND PACKET DISCRIMINATION REGIMES

Consumers compare the four ISP-CP options and choose the option which yields the highest utility. In order to derive the market shares for each option, we need to calculate the six curves of indifferent consumers based on the pairwise comparisons among them. Figure 5 demonstrates the various possibilities of how consumers are distributed among the four options. Solving for the exact market shares under each ISP-CP combination is difficult and the market shares under each ISP-CP option could look very different (demonstrated by the dotted lines in Figure 5).

![](/api/attachments/95SY3K9J/fulltext/images/f64982b4d9e60713ab85c9fe14468765b51e0825fa07554c8e5a550832f77774.jpg)  
Figure 5: General Demand Distribution

In order to solve this problem, we utilize the symmetry of the corresponding market shares when the CPs interchange their decisions on paying for preferential delivery of their content. Interchanging the CPs’ delivery service choices induces what is called a $\mathbb { Z } _ { 2 } \times \mathbb { Z } _ { 2 }$ (or the Klein 4-group) action in group theory. We use the symmetry associated with this group action to solve for the demand distributions. The details of this symmetry analysis can be found in the appendix. The results of the consumer demand patterns (market shares) are summarized in Lemma 1. All proofs are relegated to the appendix.

Lemma 1 (Consumer Demand Patterns): Depending on the ISPs’ pricing decisions and the CPs’ delivery service choices, there are 16 possible outcomes. These outcomes can be grouped into four classes with similar consumer demand patterns under both symmetric and asymmetric equilibria.

The details of the consumer demand patterns can be found in Appendix A for the symmetric equilibrium case and Appendix C for the asymmetric equilibrium case.

Lemma 2 (Possible Equilibrium Outcomes): There are four possible (symmetric or asymmetric) equilibrium outcomes – only <sub>??</sub> pays on both ISPs (outcome 33); both CPs pay on ISP <sub>??</sub> and only <sub>??</sub> pays on ISP <sub>??</sub> (outcome 43); only <sub>??</sub> pays on ISP <sub>??</sub> and both CPs pay on ISP <sub>??</sub> (outcome 34); both CPs pay on both ISPs (outcome 44).

Lemma 2 shows that under both symmetric and asymmetric equilibria, the ISPs would have the incentive to deviate from the net neutrality outcome (which corresponds to the outcom 11), leading to four possible equilibrium outcomes, all of which involve packet discrimination. Due to the technical complexity of asymmetric equilibrium analysis, there is no closed-form expression for the separating market conditions for these four possible asymmetric equilibria. We henceforth focus on the symmetric equilibrium results in the rest of the analysis.

Lemma 3 (ISPs’ Strategy): Depending on market conditions, there are four possible symmetric equilibrium pricing strategies (i.e., the <sub>??</sub> and <sub>??</sub> choices) for the ISPs: (a) when $r _ { G } \ge$ ?? $\left\{ \alpha _ { 1 } , \beta _ { 1 } r _ { Y } , \alpha _ { 2 } + \beta _ { 2 } r _ { Y } \right\}$ , the equilibrium is outcome 33, where only <sub>??</sub> pays for priority delivery on both ISPs; (b) when $\beta _ { 3 } r _ { Y } \le r _ { G } < \alpha _ { 1 }$ and $r _ { Y } \leq \alpha _ { 3 }$ , the equilibrium is outcome 43 (and equivalently, equilibrium 34), where <sub>??</sub> pays for priority delivery on both ISPs, while <sub>??</sub> pays for priority delivery on only one ISP; and (c) otherwise, the equilibrium is outcome 44, where both CPs pay for priority delivery on both ISPs.

We diagrammatically show the results of Lemma 3 in Figure 6. The results of Lemma 3 is under the assumption of $r _ { G } \geq r _ { Y }$ , which correspond to the upper half above the $r _ { G } = r _ { Y }$ line in Figure 6. The equilibrium results assuming $r _ { G } \geq r _ { Y }$ can be easily generalized to the case when $r _ { G } < r _ { Y }$ (the lower half below the $r _ { G } = r _ { Y }$ line in Figure 6).

![](/api/attachments/95SY3K9J/fulltext/images/d76f01aa62cb3c98dbde66e1f64ce9e3fc43bd7f8b873007ece0f89abaf4c55a.jpg)  
Figure 6: Equilibrium Outcomes

In general, ISPs will charge higher prices to CPs when only one pays for priority delivery than when both CPs pay for priority delivery. Consumers, however, are charged less, indicating that as the revenue generation rate $r _ { G }$ increases, the relative contribution to ISPs’ profit gradually switches from the consumers to the CPs. This leads to our first proposition.

Proposition 1 (Competing ISPs still have an incentive to deviate from net neutrality): The competing ISPs’ profit is weakly higher under packet discrimination than under net neutrality, $i . e . , \ \pi _ { C } ^ { P D } = \pi _ { D } ^ { P D } \geq \pi _ { C } ^ { N N } = \pi _ { D } ^ { N N }$

Proposition 1 shows that the competing ISPs are always better off under packet discrimination even in the presence of ISP competition and thus have the incentive to deviate from net neutrality. In other words, when it comes to the net neutrality debate, ISPs will prefer abolishing net neutrality, even in the presence of ISP competition. This is a result that has been shown to be true when the ISP is a monopoly and it continues to hold with ISP competition. This finding is different from that of Bourreau et al. (2014), where the authors do not model the competition between CPs, and as a result, the effect of competition faced by the ISPs is exaggerated. Our analysis provides an explanation for the public stance of the ISPs in the ongoing net neutrality debate, as they continue to lobby for abolishing net neutrality. This result mirrors the results of Gans (2015), even though he does not explicitly model the effects of ISP competition.

Content providers, however, have supported the preservation of net neutrality. Would they continue to support net neutrality when there is competition between ISPs? Our next result (Proposition 2) shows that under certain conditions, it is economically beneficial for the dominant CP to reverse its stance on net neutrality. In other words, some CPs might be better off when net neutrality is abolished in the presence of competition between ISPs. This is a crucial and, in some ways, a surprising result. Ever since the issue of net neutrality has been publicly debated, prominent CPs like Google, Yahoo!, Microsoft, Netflix and others have publicly supported net neutrality, and so far, the economic analyses have mirrored the public stances of the various parties in the debate: when facing direct competition CPs are worse off when net neutrality is abolished, while the ISPs are better off. Proposition 2 shows that under ISP competition, the support for net neutrality from CPs – and more specifically, from the dominant CPs – might not be so forthcoming.

Proposition 2 (CP G may be better off under packet discrimination): When CP <sub>??</sub> is sufficiently dominant, its profit is higher under packet discrimination (corresponds to equilibrium 33) than that under net neutrality if the intensity of competition in the ISP market relative to that in the CP market is greater than a threshold. Formally, $\pi _ { G } ^ { P D } = \pi _ { G 3 3 } ^ { * } > \pi _ { G } ^ { N N }$ if the ratio of $t / k$ is higher than a threshold and the ratio of $r _ { G } / r _ { Y }$ is higher than a threshold.

Proposition 2 shows that under certain conditions, CP <sub>??</sub> might in fact do better than it could under net neutrality. When $r _ { G }$ and $r _ { Y }$ are similar and the corresponding equilibrium outcome is 44 (both CPs decide to pay the two ISPs), CP <sub>??</sub> is definitely worse off under packet discrimination than under net neutrality. As $r _ { G }$ becomes larger relative to $r _ { Y }$ <sub>,</sub> however, and the equilibrium shifts to outcome 33 (where only <sub>??</sub> prefers to pay the two ISPs), $G \ ' _ { \mathrm { s } }$ profit is at least as great as that under net neutrality. Specifically, the comparison result of $G \ ' _ { \mathrm { s } }$ profit depends on the relative magnitude of the intensity of competition in the ISP and CP markets. We can think of the unit fit costs <sub>??</sub> and <sub>??</sub> as the strengths of the consumer loyalties within the CP market and within the ISP market, respectively. A more differentiated market corresponds to a higher level of consumer loyalty. Thus, <sub>??</sub> and <sub>??</sub> can be interpreted as the reverse measures of the intensity of competition in the two markets, and the ratio of $t / k$ measures the relative magnitude of the intensity of competition in the ISP market to that in the CP market. When the intensity of competition between the CPs is relatively low compared to that between the ISPs, such that $t / k$ is greater than a threshold, the more efficient CP is actually better off under packet discrimination. In practice, it can be argued that the consumer loyalty in the CP market is relatively high compared to that in the ISP market, because digital content is more differentiated than Internet access service, which raises the possibility that this condition is likely to hold within markets for certain types of digital content.

To explain the intuition behind this result, it is instructive to first consider the effects of the CP competition between <sub>??</sub> and <sub>??</sub>: when $r _ { G }$ and $r _ { Y }$ are comparable, both CPs <sub>??</sub> and <sub>??</sub> may end up in a Prisoner’s Dilemma – both CPs are forced to pay for priority delivery due to competitive pressure. Neither CP would like to pay, but is forced $\mathbf { t o } ,$ since otherwise they would be much worse off due to competition. But when $r _ { G }$ is much higher than $r _ { Y }$ , both ISPs find it preferable to charge a high <sub>??</sub> that only <sub>??</sub> can afford to pay. There are also indirect effects – because of the higher delays associated with the consumers of <sub>??</sub>, the marginal consumer has lesser net utility, which leads to a lower fixed fee <sub>??</sub>. Due to ISP competition, the ISPs face some kind of a Prisoners’ Dilemma of their own: they would like to extract the surplus from the CPs as much as possible, but are limited by competition, i.e., ISP <sub>??</sub>’s ability to charge a high <sub>??</sub> is moderated by its competition with ISP <sub>??</sub>, and vice versa. Therefore, while they do stand to gain by extracting a part of $G '$ s additional surplus, they cannot extract it fully. As a result, <sub>??</sub> ends up with a higher surplus than what it would have had under net neutrality even after paying for priority delivery. In other words, <sub>??</sub> would want to pay for priority delivery to marginalize its competitor (<sub>??</sub>) in both the ISP markets. Consequently, the competition between the ISPs and the competition between the CPs will have moderating effects on each other. Which party has the upper hand in this scenario will depend on the relative magnitude of the intensity of competition in the two markets, in other words, the ratio of $t / k$

This result is extremely significant. In the presence of ISP competition, a dominant CP (in our case, <sub>??</sub>, with $r _ { G }$ being relatively large compared to $r _ { Y } )$ might no longer be concerned with preserving net neutrality. In fact, <sub>??</sub> might actually eke out a higher profit under packet discrimination, since its payments to the ISP for priority delivery might pay off in terms of the additional revenue garnered from consumers that have switched from a rival CP.

In the net neutrality debate thus far, CPs have generally been supportive of net neutrality. This stance has been vindicated in the literature (Choi and Kim 2010; Guo et al. 2010; Cheng et al. 2011; Guo et al. 2013), where it has been shown that when facing direct competition CPs are never better off under packet discrimination. Those results, however, have been derived under the assumption that there is no competition among ISPs. Indeed, a monopoly ISP can extract all the rent (and often more) from a CP that gains market share by paying for priority delivery. But when there is competition among ISPs, while they do increase their profits by deviating from net neutrality, they cannot extract the entire surplus from the CP that decides to pay for priority delivery of its content. The effect of competition moderates an ISP’s ability to extract the surplus from the CPs, and in such situations, a dominant CP can indeed be better off when ISPs deviate from net neutrality. In such cases (for example, in the mobile broadband market where there is effective ISP competition), we can expect the dominant CPs to be less supportive of the need for net neutrality.

In fact, such a shift in stance might already be underway (Manjoo 2014). He observed that “Large Internet businesses have written a few letters to regulators in support of the issue and have participated in the back-channel lobbying effort, but they have not joined online protests, or otherwise moved to mobilize their users in favor of new rules.” He further goes on to speculate on the reason why the large Internet businesses have taken such a stance: “They may be too big to bother with an issue that primarily affects the smallest Internet companies” and that they “would escape relatively unscathed” by the paid prioritization. Our research shows that not only would some of these large Internet companies escape “relatively unscathed” from paid prioritization, they might actually prosper from such an arrangement.

Proposition 3 (CP Y is always worse off under packet discrimination): CP Y’s profit is lower under packet discrimination than under net neutrality, i.e., $\pi _ { Y } ^ { N N } \geq \pi _ { Y } ^ { P D }$

Proposition 3 reminds us that although the dominant CP may be better off under the packet discrimination regime, the economically less successful CP, e.g., a startup in a market with an established market player, is always worse off. In such situations, packet discrimination, e.g., the option of a paid fast lane, can act as a disincentive to entry for newer entrants in a marketplace with well-established incumbents. From a policymaker’s perspective, in the long term, this can have a debilitating effect on content innovation. The impact of net neutrality and packet discrimination on content innovation has been studied from different perspectives, such as the entry of CPs (Krämer and Wiewiorra 2012; Guo and Easley 2014), the investment of CPs (Choi and Kim 2010), and the profitability of CPs (Guo et al. 2012). Our analysis contributes to this discussion. It shows that even in the presence of ISP competition, we do not have a ‘level playing field’ since the dominant CP can still marginalize a less efficient or newer rival, to the extent that it (the dominant CP) might be better off without net neutrality. So, in a way, the dominant CP can leverage the competition among ISPs to become even more dominant by taking advantage of the flexible traffic management options under the packet discrimination regime.

As Manjoo (2014) observed, recently it is the smaller Internet firms that have been most vocal in the net neutrality debate. Companies like Etsy, where consumers can shop directly from people around the world, “would not have been able to pay for priority access if broadband companies ever created a fast lane online.” Etsy’s public policy director went on to comment that “Delays of even fractions of a second result in dropped revenue for our users.” Our result in Proposition 3 shows that this concern is justified because the smaller firms will certainly be negatively affected by paid prioritization.

Prior studies with a monopolist ISP and competing CPs (Choi and Kim 2010; Cheng et al. 2011) show that all CPs will be united in their stance in preserving net neutrality. With both ISP competition and CP competition, however, our findings suggest that under certain market conditions, it will be just the smaller CPs who will support net neutrality.

Next, we study the welfare effect under net neutrality and packet discrimination regimes. Consumer surplus is defined as $\begin{array} { r } { C S _ { i j } = \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } U _ { i j } ( x , z ) } \end{array}$ and social welfare is defined as $S W _ { i j } = \pi _ { C i j } + \pi _ { D i j } + \pi _ { Y i j } + \pi _ { G i j } + C S _ { i j }$

Proposition 4 (Comparison of Social Welfare under Net Neutrality and Packet Discrimination): Social welfare is weakly higher under packet discrimination than under net neutrality, i.e., $S W ^ { P D } \ge S W ^ { N N }$

Proposition 4 indicates that packet discrimination with flexible network management options is welfare enhancing compared to the net neutrality regime. This result supports findings in prior studies (Cheng et al. 2011; Guo et al. 2012; Krämer and Wiewiorra 2012; Bourreau et al. 2014; Guo and Easley 2014).

# CONCLUDING REMARKS

## Discussions

In this paper, we assume that the entire consumer market is covered. If we relax this assumption, we postulate that under net neutrality the ISPs will choose to cover the whole market if consumers’ valuation of the Internet access service is higher than a threshold, and only part of the market if consumers’ valuation is low. In the packet discrimination regime, the ISPs’ decision whether to serve the whole consumer market should be similar. Intuitively, the threshold value under packet discrimination should be lower than that under net neutrality, since the ISPs have the option to subsidize end consumers from the payments collected from CPs and therefore have a higher incentive to serve more consumers. That is, the ISPs could cover more market without net neutrality. As a result, it is possible that social welfare is higher under packet discrimination than under net neutrality. In other words, we expect our social welfare result to continue to hold when the full-market-coverage assumption is relaxed. Another possible result of not enforcing the full-market-coverage constraint is that under certain conditions, in the absence of net neutrality, the disadvantaged CP <sub>??</sub> might be completely marginalized, especially when both the ISPs find it profitable to prioritize only $G \ ' \mathbf s$ content. This is more likely to occur when $r _ { G }$ is substantially greater than $r _ { Y }$ . In such a scenario, consumers of <sub>??</sub> that are being served by either ISP will find it advantageous to switch to $G$ or stay out of the market, so much so that <sub>??</sub> is completely driven out of the market.

We study a short-run problem where the $\mathrm { I S P s } '$ capacity is fixed, and focuses on the interaction between ISP competition and CP competition. In a long-run problem with competing ISPs having the option to expand their capacity, we envisage that the ISPs will face some kind of a Prisoners’ Dilemma of their own: individually, they would not like to invest in capacity expansion, but they would stand to lose a lot of customers (on both sides of the platform) if their competitor expands capacity. Consequently, the competition between the ISPs and the competition between the CPs will have moderating effects on each other. In other words, both CPs might be forced to pay for priority delivery and end up with the same congestion as they would have had when neither pays, thanks to the competition between CPs in the short run. This result will be alleviated by a higher bandwidth in the long run because the ISPs might be forced to expand capacity due to the competition between the ISPs.

We assume that the CPs generate their revenue based on an advertisement-supported model. In real life, some CPs (e.g., Netflix) charge consumers a subscription fee for accessing their content. If the consumers pay the CPs for content, the equilibrium results will be slightly different: for example, the Internet access fee <sub>??</sub> charged by the ISP will presumably be lower, because consumers now have to pay the additional subscription fee for content. But the dynamics of the competition between CPs will still remain the same. Under the subscription-fee-based revenue model for CPs, we expect that with this additional pricing instrument, i.e., the subscription fee from consumers, the dominant CP<sup>3</sup> would be even more dominant in competing with the other CP in the absence of net neutrality. In other words, our main result regarding the dominant CP being better off in the absence of net neutrality would be further amplified.

Another assumption in our model is that consumers only visit one of the two available CPs. It is possible that a consumer might split her attention between different competing contents of the same type, e.g., she might allocate some of her time from watching videos on YouTube to watching videos on Vimeo (with no change in her overall consumption). The content consumption of these “split” consumers is still captured by the market shares of the competing CPs in our model. A variant of this situation is where the consumer watches more videos on Vimeo on top of what she was already watching on YouTube (with an increase in her overall consumption). This type of consumption could be an extension of our model. It reduces the intensity of competition between the two CPs somewhat, but does not qualitatively change the insights of the paper.

## Theoretical Implications

We have proposed a modeling framework that captures the dynamics of two interrelated markets – that of Internet access service and that of digital content – providing complementary products. Duopolists compete for consumers in each market (ISPs <sub>??</sub> and <sub>??</sub> in the Internet access service market and CPs <sub>??</sub> and <sub>??</sub> in the digital content market). Therefore consumers choose their preferred option among four product combinations (<sub>??</sub> , <sub>??</sub> , <sub>??</sub> , and <sub>??</sub> ). Furthermore, user experiences are jointly determined by the ISPs’ pricing decisions and the CPs’ delivery service choices. We show that the interactions between the two markets and the relative market power of the agents in the two markets play a critical role in determining the equilibrium outcomes.

This modeling framework is not restricted to the Internet data transmission process and can be applied to a wide range of other contexts, where consumers derive their utility from a pair of complementary products. For example, in the ongoing hardware battle between competing hardware platforms (e.g. the Apple Macintosh versus the PC), a critical factor is software compatibility and functionality. While computer makers do not compete directly with software manufacturers, the competition between the computer hardware platforms nevertheless attenuates the competition between the software manufacturers, since consumers need to “consume” both the hardware and the software for their computing needs. When making their purchase decisions, users simultaneously consider the specifications of the device and the compatibility and ease-of-use of the corresponding software. The competitions between firms in both the computer hardware and software markets interact with each other and jointly determine the experiences of the end-users.

## Managerial and Policy Implications

Our findings have important managerial implications. We find that net neutrality regulation (or conversely, the potential packet discrimination mechanisms) affects CPs differently. Moreover, this impact on the CPs’ incentives and consequently content innovation critically depends on the market power of the CP and the relative magnitude of the intensity of competition between the markets of Internet access service and digital content. In practice, CPs strive to improve their profit margin through lowering the cost of generating new content or licensing existing content. For example, instead of spending money indiscriminately on licensing content from other producers, CPs like Netflix are instead sifting through consumer viewing patterns to license (or greenlight for internal production) only those kinds of content that will probably be viewed extensively by their consumers. This trove of consumer information will become even more important over time, as it can be used to make increasingly accurate predictions, which in turn will help lower the cost of licensing content even further. In such scenarios, it is likely that the more efficient CP would become increasingly dominant over time, which makes it more difficult for the less efficient CP to compete. This is especially true in many online markets, where there is often a large gulf between the market leader and the next leading competitor. Our findings suggest that packet discrimination in the presence of ISP competition amplifies the competitive advantage of the more efficient CP, even to the extent that the more efficient CP is better off with paid prioritization compared to the outcome under the net neutrality regime.

Our findings also have important policy implications for net neutrality. Our results show that ISP competition may not substitute for net neutrality regulation, especially in the presence of CP competition. Without net neutrality regulation, the competing ISPs still have the incentive to charge CPs for preferential delivery, and in the presence of CP competition, they have the ability to induce CPs to pay for packet prioritization. Contrary to popular belief, we find that some advantaged CPs may benefit from paid prioritization because such arrangements further enforce their dominance in the content market. Paid prioritization, however, always hurts the disadvantaged CPs. In order to protect and encourage content innovation, the policy makers are advised to evaluate the specific market conditions (such as revenue generation ability of CPs and competition intensity) of individual markets of ISPs and CPs.

Ansari, A., Economides, N., and Steckel, J. 1998. "The Max-Min-Min Principle of Product Differentiation," Journal of Regional Science (38:2), pp. 207-230.

Armstrong, M. 1998. "Network Interconnection in Telecommunications," Economic Journal (108:448), pp. 545-564.

. 2002. "The Theory of Access Pricing and Interconnection," in Handbook of Telecommunications Economics, M. Cave, S. Majumdar, and I. Vogelsang (eds.), Amsterdam, Netherlands: North-Holland.

Bourreau, M., Kourandi, F., and Valletti, T. 2014. "Net Neutrality with Competing Internet Platforms," Journal of Industrial Economics, Forthcoming.

Brito, D., Pereira, P., and Vareda, J. 2013. "Network Neutrality Under ISP Duopoly: On the Ability to Assign Capacity," CEFAGE-UE Working Paper.

Broos, S., and Gautier, A. 2015. "Competing One-Way Essential Complements: The Forgotten Side of Net Neutrality," Working Paper.

Bykowsky, M., and Sharkey, W. W. 2014. "Net Neutrality and Market Power: Economic Welfare with Uniform Quality of Service," Working Paper.

Caplin, A. S., and Nalebuff, B. J. 1986. "Multi-Dimensional Product Differentiation and Price Competition," Oxford Economic Papers (38), pp. 129-145, Supplement: Strategic Behaviour and Industrial Competition.

Cheng, H. K., Bandyopadhyay, S., and Guo, H. 2011. "The Debate on Net Neutrality: A Policy Perspective," Information Systems Research (22:1), pp. 60-82.

Chiang, I. R., and Jhang-Li, J. 2014. "Delivery Consolidation and Service Competition among Internet Service Providers," Journal of Management Information Systems (31:3), pp. 254-286.

Choi, J. P., and Kim, B. 2010. "Net Neutrality and Investment Incentives," RAND Journal of Economics (41:3), pp. 446-471.

Dunbar, F. 2014. "Net Neutrality: Competition is the Best Way to Keep an Open Playing Field on the Internet," SitNews, September 3.

Economides, N., and Hermalin, B. 2012. "The Economics of Network Neutrality," RAND Journal of Economics (43:4), pp. 602-629.

Economides, N., and Tåg, J. 2012. "Net Neutrality on the Internet: A Two-Sided Market Analysis," Information Economics and Policy (24:2), pp. 91-104.

FCC. 2010. "Report and Order: Preserving the Free and Open Internet," Federal Communications Commission, December 23, Available at: http://www.fcc.gov/document/preserving-open-internet-broadband-industry-practices-1.

Gans, J. S. 2015. "Weak Versus Strong Net Neutrality," Journal of Regulatory Economics (47:2), pp. 183-200.

Glaser, A. 2014. "Why the FCC Can't Actually Save Net Neutrality," Electronic Frontier Foundation, January 27.

Guo, H., Cheng, H. K., and Bandyopadhyay, S. 2013. "Broadband Network Management and the Net Neutrality Debate," Production and Operations Management (22:5), pp. 1287-1298.

Guo, H., and Easley, R. 2014. "Network Neutrality Versus Paid Fast Lanes: Analyzing the Impact on Content Innovation," Working Paper.

Guo, H., Bandyopadhyay, S., Cheng, H. K., and Yang, Y. 2010. "Net Neutrality and Vertical Integration of Content and Broadband Services," Journal of Management Information Systems (27:2), pp. 243-275.

Guo, H., Cheng, H. K., and Bandyopadhyay, S. 2012. "Net Neutrality, Broadband Market Coverage and Innovations at the Edge," Decision Sciences (43:1), pp. 141–172.

Hermalin, B. E., and Katz, M. L. 2007. "The Economics of Product-Line Restrictions with an Application to the Network Neutrality Debate," Information Economics and Policy (19), pp. 215-248.

Irmen, A., and Thisse, J. 1998. "Competition in Multi-Characteristics Spaces: Hotelling was almost Right," Journal of Economic Theory (78:1), pp. 76-102.

Kourandi, F., Krämer, J., and Valletti, T. 2014. "Net Neutrality, Exclusivity Contracts and Internet Fragmentation," Information Systems Research, Forthcoming.

Krämer, J., and Wiewiorra, L. 2012. "Network Neutrality and Congestion Sensitive Content Providers: Implications for Content Variety, Broadband Investment and Regulation," Information Systems Research (23:4), pp. 1303-1321.

Krämer, J., Wiewiorra, L., and Weinhardt, C. 2013. "Net Neutrality: A Progress Report," Telecommunications Policy (37:9), pp. 794-813, October.

Laffont, J., Marcus, S., Rey, P., and Tirole, J. 2003. "Internet Interconnection and the Off-Net-Cost Pricing Principle," RAND Journal of Economics (34:2), pp. 370-390.

Manjoo, F. 2014. "In Net Neutrality Push, Internet Giants on the Sidelines," The New York Times, November 11.

Matutes, C., and Regibeau, P. 1988. "'Mix and Match': Product Compatibility without Network Externalities," RAND Journal of Economics (19:2), pp. 221-234.

McMillan, R. 2014. "What Everyone Gets Wrong in the Debate Over Net Neutrality," Wired, June 23.

Nagesh, G., and Sharma, A. 2014. "Court Tosses Rules of Road for Internet," Wall Street Journal, January 14.

Risen, T. 2015. "Telecom Lawsuits Aim to Kill FCC Net Neutrality," U.S. News, March 24.

Singel, R. 2013. "Now that It’s in the Broadband Game, Google Flip-Flops on Network Neutrality," Wired, July 30.

Szoka, B., Starr, M., and Henke, J. 2013. "Don't Blame Big Cable. It’s Local Governments that Choke Broadband Competition," Wired, July 16.

Tabuchi, T. 1994. "Two-Stage Two-Dimensional Spatial Competition between Two Firms," Regional Science and Urban Economics (24:2), pp. 207-227.

Tan, Y., Chiang, I. R., and Mookerjee, V. S. 2006. "An Economic Analysis of Interconnection Arrangements between Internet Backbone Providers," Operations Research (54:4), pp. 776-788.

The Internet Association. 2014. "Statement on President Obama’s Net Neutrality and Patent Reform Remarks," The Internet Association, October 10.

U.S. Court of Appeals. 2014. "Verizon V. FCC," United States Court of Appeals, January 14, Available at: http://www.cadc.uscourts.gov/internet/opinions.nsf/3AF8B4D938CDEEA685257C6000 532062/\$file/11-1355-1474943.pdf.

von Ehrlich, M., and Greiner, T. 2013. "The Role of Online Platforms for Media Markets - Two-Dimensional Spatial Competition in a Two-Sided Market," International Journal of Industrial Organization (31:6), pp. 723-737.

Winegarden, W. 2014. "You Don't Promote a Competitive Broadband Market by Prohibiting Competition," Forbes, July 15.

## ONLINE APPENDIX

## A. Proof of Lemma 1 – The Symmetric Equilibrium Case

Consumers have four choices of ISP-CP combinations: <sub>????</sub>, <sub>????</sub>, <sub>??</sub> , and <sub>??</sub> . Consumer demands for these four ISP-CP combinations can be derived by analyzing the curves of indifferent consumers. There are six curves of indifferent consumers based on the pairwise comparisons among the four ISP-CP combinations. For a given outcome <sub>????</sub>, where $i , j = 1$ (Neither CP pays), <sub>2</sub> (Only pays), <sub>3</sub> (Only pays), and <sub>4</sub> (Both CPs pay), these six curves of indifferent consumers can be characterized by four points $x _ { C i j } , x _ { D i j } , z _ { Y i j }$ , and $z _ { G i j }$ : consumers located on $x = x _ { C i j }$ are indifferent between <sub>????</sub> and <sub>????</sub>; consumers located on $x = x _ { D i j }$ are indifferent between <sub>??</sub> and $D G ;$ consumers located on $z = z _ { Y i j }$ are indifferent between <sub>????</sub> and $D Y ;$ ; consumers located on $z = z _ { G i j }$ are indifferent between <sub>????</sub> and $_ { D G }$ ; consumers located on the line that goes through points $\left( { x _ { C i j } , z _ { Y i j } } \right)$ and $\left( { x _ { D i j } , z _ { G i j } } \right)$ are indifferent between <sub>????</sub> and <sub>??</sub> ; and consumers located on the line that goes through points $\left( { { x } _ { C i j } } , { { z } _ { G i j } } \right)$ and $\left( { x _ { D i j } , z _ { Y i j } } \right)$ are indifferent between <sub>????</sub> and <sub>??</sub> .

Comparing consumers’ utility functions for the corresponding pairs of ISP-CP combinations yields $\begin{array} { l } { { x _ { C i j } } = \frac { 1 } { 2 } + \frac { { d \lambda \left( { { \bf { w } } _ { C G i j } } - { { \bf { w } } _ { C Y i j } } \right) } } { 2 t } , { x _ { D i j } } = \frac { 1 } { 2 } + \frac { { d \lambda \left( { { \bf { w } } _ { D G i j } } - { { \bf { w } } _ { D Y i j } } \right) } } { 2 t } , { z _ { Y i j } } = \frac { 1 } { 2 } + \frac { { F _ { D } } - F _ { C } } { 2 k } + \frac { { d \lambda \left( { { \bf { w } } _ { C G i j } } - { { \bf { w } } _ { D Y i j } } \right) } } { 2 t } . } \end{array}$ $\begin{array} { r } { \frac { d \lambda \left( \mathbf { w } _ { D Y i j } - \mathbf { w } _ { C Y i j } \right) } { 2 k } } \end{array}$ , and $\begin{array} { r } { z _ { G i j } = \frac { 1 } { 2 } + \frac { F _ { D } - F _ { C } } { 2 k } + \frac { d \lambda \left( \mathbf { w } _ { D G i j } - \mathbf { w } _ { C G i j } \right) } { 2 k } } \end{array}$ . Considering symmetric equilibrium with $F _ { C } = F _ { D }$ , we have $\begin{array} { r } { z _ { Y i j } = \frac { 1 } { 2 } + \frac { d \lambda \left( \mathbf { w } _ { D Y i j } - \mathbf { w } _ { C Y i j } \right) } { 2 k } } \end{array}$ and $\begin{array} { r } { z _ { G i j } = \frac { 1 } { 2 } + \frac { d \lambda \left( \mathbf { w } _ { D G i j } - \mathbf { w } _ { C G i j } \right) } { 2 k } } \end{array}$ . We observe that the sign of $x _ { C i j } - x _ { D i j }$ is the same as the sign of $z _ { Y i j } - z _ { G i j }$ . In particular, $x _ { C i j } = x _ { D i j }$ if and only if $z _ { Y i j } = z _ { G i j }$

Each outcome <sub>????</sub> is determined by the ISPs’ pricing decisions and the corresponding content providers’ delivery service choices. We use indicator functions $I _ { C Y i j } , I _ { C G i j } , I _ { D Y i j }$ and $I _ { D G i j }$ , which take values of 0 or 1, to represent whether content providers and would pay for preferential delivery on ISPs <sub>??</sub> and <sub>??</sub>. To be consistent with the four ISP-CP combinations on the unit square, we denote outcome <sub>????</sub> by the matrix $\left[ \begin{array} { l l } { I _ { D Y i j } } & { I _ { D G i j } } \\ { I _ { C Y i j } } & { I _ { C G i j } } \end{array} \right]$ . We introduce two types of actions (horizontal and vertical flips) to explore the connections among the 16 outcomes:

Horizontal Flip: Decisions of and are simultaneously interchanged on ISPs <sub>??</sub> and <sub>??</sub>. Specifically, horizontal flip changes outcome <sub>????</sub> dictated by $\begin{array} { r l } { \left[ { \begin{array} { l l } { I _ { D Y i j } } & { I _ { D G i j } } \\ { I _ { C Y i j } } & { I _ { C G i j } } \end{array} } \right] } \end{array}$ to outcome <sub>??’ ’</sub> dictated by $\begin{array} { r l } { \left[ { \begin{array} { l l } { I _ { D G i j } } & { I _ { D Y i j } } \\ { I _ { C G i j } } & { I _ { C Y i j } } \end{array} } \right] } \end{array}$ , where $i ^ { \prime } = { \left\{ \begin{array} { l l } { 1 , } & { { \mathrm { i f ~ } } i = 1 } \\ { 3 , } & { { \mathrm { i f ~ } } i = 2 } \\ { 2 , } & { { \mathrm { i f ~ } } i = 3 } \\ { 4 , } & { { \mathrm { i f ~ } } i = 4 } \end{array} \right. }$ and $j ^ { \prime } = { \left\{ \begin{array} { l l } { 1 , } & { { \mathrm { i f } } j = 1 } \\ { 3 , } & { { \mathrm { i f } } j = 2 } \\ { 2 , } & { { \mathrm { i f } } j = 3 } \\ { 4 , } & { { \mathrm { i f } } j = 4 } \end{array} \right. }$

Vertical Flip: Decisions of and are simultaneously interchanged across ISPs <sub>??</sub> and <sub>??</sub>. Specifically, vertical flip changes outcome <sub>????</sub> dictated by $\begin{array} { r l } { \left[ { \begin{array} { l l } { I _ { D Y i j } } & { I _ { D G i j } } \\ { I _ { C Y i j } } & { I _ { C G i j } } \end{array} } \right] } \end{array}$ to outcome dictated by $\begin{array} { r l } { \left[ { \begin{array} { l l } { I _ { C Y i j } } & { I _ { C G i j } } \\ { I _ { D Y i j } } & { I _ { D G i j } } \end{array} } \right] } \end{array}$

Among the 16 outcomes, some outcomes permute amongst themselves when horizontal flip or vertical flip is applied and therefore can be grouped together into four invariant classes: (a) outcomes 11, 14, 41, and 44; (b) outcomes 22 and 33; (c) outcomes 23 and 32; (d) outcomes 12, 13, 21, 31, 42, 43, 24, and 34. In the following discussion, we give precise description of the changes to the indifferent customers when horizontal flip or vertical flip is applied to an outcome.

Applying Horizontal Flip: The decisions of on the two ISPs are interchanged with the decisions of in a given outcome. Horizontal flip changes outcome <sub>????</sub> dictated by $\left[ \begin{array} { l l } { I _ { D Y i j } } & { I _ { D G i j } } \\ { I _ { C Y i j } } & { I _ { C G i j } } \end{array} \right]$ to outcome $i ^ { \prime } j ^ { \prime }$ dictated by $\begin{array} { r l } { \lceil { I _ { D G i j } } } & { { } { I _ { D Y i j } } } \\ { { I _ { C G i j } } } & { { } { I _ { C Y i j } } } \end{array}$ . That is we have $I _ { C Y i ^ { \prime } j ^ { \prime } } = I _ { C G i j } , I _ { C G i ^ { \prime } j ^ { \prime } } = I _ { C Y i j }$ $I _ { D Y i ^ { \prime } j ^ { \prime } } = I _ { D G i j }$ , and $I _ { D G i ^ { \prime } j ^ { \prime } } = I _ { D Y i j }$ . When the decisions in outcome <sub>????</sub> are changed to $i ^ { \prime } j ^ { \prime }$ , the decisions of on <sub>??</sub> and <sub>??</sub> and the decisions of on <sub>??</sub> and <sub>??</sub> are interchanged. The queuing priorities are interchanged on ISPs <sub>??</sub> and <sub>??</sub>. This simultaneously interchanges the waiting times and market demand on <sub>??</sub> and <sub>??</sub> according to the new queuing priorities. We note that fees for all customers are equal so the redistribution is dependent solely on waiting times. Interchanging waiting times on ISPs and yields $w _ { C Y i ^ { \prime } j ^ { \prime } } = w _ { C G i j } , w _ { C G i ^ { \prime } j ^ { \prime } } = w _ { C Y i j } , w _ { D Y i ^ { \prime } j ^ { \prime } } = w _ { D G i j }$ , and $w _ { D G i ^ { \prime } j ^ { \prime } } = w _ { D Y i j }$ . This gives $\begin{array} { r } { x _ { C i j } + x _ { C i ^ { \prime } j ^ { \prime } } = \frac { 1 } { 2 } + \frac { d \lambda \left( \mathbf { w } _ { C G i j } - \mathbf { w } _ { C Y i j } \right) } { 2 t } + \frac { 1 } { 2 } + \frac { d \lambda \left( \mathbf { w } _ { C G i ^ { \prime } j ^ { \prime } } - \mathbf { w } _ { C Y i ^ { \prime } j ^ { \prime } } \right) } { 2 t } = \frac { 1 } { 2 } + } \end{array}$ $\begin{array} { r } { \frac { d \lambda \left( \mathbf { w } _ { C G i j } - \mathbf { w } _ { C Y i j } \right) } { 2 t } + \frac { 1 } { 2 } - \frac { d \lambda \left( \mathbf { w } _ { C G i j } - \mathbf { w } _ { C Y i j } \right) } { 2 t } = 1 } \end{array}$ , which implies $x _ { C i ^ { \prime } j ^ { \prime } } = 1 - x _ { C i j }$ . Similarly, we have $x _ { D i ^ { \prime } j ^ { \prime } } = 1 - x _ { D i j } , z _ { Y i j } = z _ { G i ^ { \prime } j ^ { \prime } }$ , and $z _ { G i j } = z _ { Y i ^ { \prime } j ^ { \prime } }$ . We note that the positions of these curves of indifferent consumers relative to the line of $\begin{array} { r } { x = \frac { 1 } { 2 } \ \mathrm { o r } \ z = \frac { 1 } { 2 } } \end{array}$ remain the same according to the decisions of and .

Applying Vertical Flip: The decisions of and on <sub>??</sub> are interchanged with their decisions on <sub>??</sub> in a given outcome. Vertical flip changes outcome <sub>????</sub> dictated by $\begin{array} { r l } { \left[ { \begin{array} { l l } { I _ { D Y i j } } & { I _ { D G i j } } \\ { I _ { C Y i j } } & { I _ { C G i j } } \end{array} } \right] } \end{array}$ to outcome dictated by $\begin{array} { r l } { \left[ { \begin{array} { l l } { I _ { C Y i j } } & { I _ { C G i j } } \\ { I _ { D Y i j } } & { I _ { D G i j } } \end{array} } \right] } \end{array}$ . That is we have $I _ { C Y j i } = I _ { D Y i j } , I _ { C G j i } = I _ { D G i j } , I _ { D Y j i } = I _ { C Y i j }$ 2 and $I _ { D G j i } = I _ { C G i j }$ . When the decisions in outcome <sub>????</sub> are changed to $j i ,$ , the decisions of and on <sub>??</sub> are swapped with the decisions of and on <sub>??</sub>. The queuing priorities are interchanged on ISPs <sub>??</sub> and <sub>??</sub>. This simultaneously interchanges the waiting times and market demand on ISPs <sub>??</sub> and <sub>??</sub> according to the new queuing priorities. We note that fees for all customers are equal so the redistribution is dependent solely on waiting times. Interchanging waiting times on ISPs <sub>??</sub>

and <sub>??</sub> yields $w _ { C Y j i } = w _ { D Y i j } , w _ { C G j i } = w _ { D G i j } , w _ { D Y j i } = w _ { C Y i j }$ , and $w _ { D G j i } = w _ { C G i j }$ . This gives $\begin{array} { r } { x _ { C i j } = \frac { 1 } { 2 } + \frac { d \lambda \left( \mathbf { w } _ { C G i j } - \mathbf { w } _ { C Y i j } \right) } { 2 k } = \frac { 1 } { 2 } + \frac { d \lambda \left( \mathbf { w } _ { D G j i } - \mathbf { w } _ { D Y j i } \right) } { 2 k } = x _ { D j i } } \end{array}$ . Similarly, $x _ { D i j } = x _ { C j i }$ . We also have $\begin{array} { r } { z _ { Y i j } + z _ { Y j i } = \frac { 1 } { 2 } + \frac { d \lambda \left( \mathbf { w } _ { D Y i j } - \mathbf { w } _ { C Y i j } \right) } { 2 t } + \frac { 1 } { 2 } + \frac { d \lambda \left( \mathbf { w } _ { D Y j i } - \mathbf { w } _ { C Y j i } \right) } { 2 t } = \frac { 1 } { 2 } - \frac { d \lambda \left( \mathbf { w } _ { D Y j i } - \mathbf { w } _ { C Y j i } \right) } { 2 t } + \frac { 1 } { 2 } + \frac { d \lambda \left( \mathbf { w } _ { D Y j i } - \mathbf { w } _ { C Y j i } \right) } { 2 t } . } \end{array}$ $\begin{array} { r } { \frac { d \lambda \left( \mathbf { w } _ { D Y j i } - \mathbf { w } _ { C Y j i } \right) } { 2 t } = 1 } \end{array}$ , which implies $z _ { Y j i } = 1 - z _ { Y i j }$ . Similarly, $z _ { G j i } = 1 - z _ { G i j }$

Next we apply the above results of horizontal and vertical flips to each of the classes (a) through (d) to characterize the demand distribution under each outcome.

## (Class a) Outcomes 11, 14, 41, and 44

Under outcomes 11, 14, 41, and 44, all customers have equal queuing priorities. Therefore applying horizontal flip or vertical flip to these outcomes will not change the queuing priorities. Hence the indifferent consumers remain unchanged when horizontal flip or vertical flip is applied.

From horizontal flip relations, we have $x _ { C 1 1 } = 1 - x _ { C 1 1 } , x _ { D 1 1 } = 1 - x _ { D 1 1 } , x _ { C 1 4 } = 1 -$ $x _ { C 1 4 } , x _ { D 1 4 } = 1 - x _ { D 1 4 } , x _ { C 4 1 } = 1 - x _ { C 4 1 } , x _ { D 4 1 } = 1 - x _ { D 4 1 } , x _ { C 4 4 } = 1 - x _ { C 4 4 } , \mathrm { a n d } x _ { D 4 4 } = 1 - x _ { D 2 2 } , \mathrm { a n d } , x _ { C 3 3 } = 1$ $x _ { D 4 4 }$ . That is $\begin{array} { r } { x _ { C 1 1 } = x _ { C 1 4 } = x _ { C 4 1 } = x _ { C 4 4 } = \frac { 1 } { 2 } \mathrm { { a n d } } \ x _ { D 1 1 } = x _ { D 1 4 } = x _ { D 4 1 } = x _ { D 4 4 } = \frac { 1 } { 2 } . \mathrm { { F r o m } } } \end{array}$ vertical flip relations, we have $z _ { G 1 1 } = 1 - z _ { G 1 1 } , z _ { Y 1 1 } = 1 - z _ { Y 1 1 } , z _ { G 1 4 } = 1 - z _ { G 1 4 } , z _ { Y 1 4 } = 1 -$ $z _ { Y 1 4 } , z _ { G 4 1 } = 1 - z _ { G 4 1 } , z _ { Y 4 1 } = 1 - z _ { Y 4 1 } , z _ { G 4 4 } = 1 - z _ { G 4 4 } , z _ { Y 4 4 } = 1 - z _ { Y 4 4 } .$ That is $z _ { G 1 1 } =$ ??<sub>??14</sub> = ??<sub>??41</sub> = ??<sub>??44</sub> = <sup>1 and</sup> ??<sub>??11</sub> = ??<sub>??14</sub> = ??<sub>??41</sub> = ??<sub>??44</sub> = <sup>1.</sup>

Therefore, as shown in Figure A-a, the market demand for <sub>????</sub>, <sub>??</sub> , <sub>????</sub>, and <sub>??</sub> are equal under outcomes 11, 14, 41, and 44. That is $\begin{array} { r } { N _ { C Y 1 1 } = N _ { D Y 1 1 } = N _ { C G 1 1 } = N _ { D G 1 1 } = \frac { 1 } { 4 } , N _ { C Y 1 4 } = } \end{array}$

$$
N _ {D Y 1 4} = N _ {C G 1 4} = N _ {D G 1 4} = \frac {1}{4}, N _ {C Y 4 1} = N _ {D Y 4 1} = N _ {C G 4 1} = N _ {D G 4 1} = \frac {1}{4}, \text {and} N _ {C Y 4 4} = N _ {D Y 4 4} =
$$

$$
N _ {C G 4 4} = N _ {D G 4 4} = \frac {1}{4}.
$$

![](/api/attachments/95SY3K9J/fulltext/images/e65103f0062037640fb688da5c096881df0c4dd1af21c0cddc941cef37a0a0cc.jpg)  
Figure A-a: Demand Distribution of Class a (outcomes 11, 14, 41, and 44)

## (Class b) Outcomes 22 and 33

Under outcome 22, only pays for preferential delivery on both ISPs. Under outcome 33, only pays for preferential delivery on both ISPs. Thus, $w _ { C G 2 2 } - w _ { C Y 2 2 } > 0 , w _ { D G 2 2 } - w _ { D Y 2 2 } > 0 ,$ ?? − ?? < 0<sup>,</sup> <sup>and</sup> ?? − ?? < 0<sup>.</sup>

Vertical flip does not change the decisions of and on <sub>??</sub> and <sub>??</sub> in outcomes 22 and 33.

Therefore we have $x _ { C 2 2 } = x _ { D 2 2 } > { \frac { 1 } { 2 } } , z _ { Y 2 2 } = 1 - z _ { Y 2 2 } \implies z _ { Y 2 2 } = { \frac { 1 } { 2 } } , z _ { G 2 2 } = 1 - z _ { G 2 2 } \implies$

$$
z _ {G 2 2} = \frac {1}{2}, x _ {C 3 3} = x _ {D 3 3} <   \frac {1}{2}, z _ {Y 3 3} = 1 - z _ {Y 3 3} \implies z _ {Y 3 3} = \frac {1}{2}, \text { and } z _ {G 3 3} = 1 - z _ {G 3 3} \implies z _ {G 3 3} = \frac {1}{2}.
$$

Moreover, horizontal flip applied to outcome 22 gives outcome 33 and vice versa. This gives

$x _ { C 2 2 } = 1 - x _ { C 3 3 } = x _ { D 2 2 } = 1 - x _ { D 3 3 }$ . Thus, we simplify the notations to $x _ { C 2 2 } = x _ { D 2 2 } = x _ { 2 2 } > \frac { 1 } { 2 }$ and $\begin{array} { r } { x _ { C 3 3 } = x _ { D 3 3 } = x _ { 3 3 } < \frac { 1 } { 2 } . } \end{array}$ Therefore, as shown in Figure A-b, the demands for <sub>????</sub>, <sub>??</sub> , <sub>????</sub>,

Outcome 33

and in outcome 22 and 33 are related such that $\begin{array} { r } { N _ { C Y 2 2 } = N _ { D Y 2 2 } = N _ { C G 3 3 } = N _ { D G 3 3 } = \frac { 1 - x _ { 3 3 } } { 2 } } \end{array}$ and $\begin{array} { r } { N _ { C Y 3 3 } = N _ { D Y 3 3 } = N _ { C G 2 2 } = N _ { D G 2 2 } = \frac { x _ { 3 3 } } { 2 } } \end{array}$ . In other words, ISPs <sub>??</sub> and <sub>??</sub> have the same market share, i.e., $N _ { C 2 2 } = N _ { D 2 2 } = N _ { C 3 3 } = N _ { D 3 3 } = { \frac { 1 } { 2 } } .$ Within each ISP, the paying CP gets more customers than the non-paying CP, i.e., $\begin{array} { r } { N _ { C Y 2 2 } = N _ { D Y 2 2 } = N _ { C G 3 3 } = N _ { D G 3 3 } > \frac { 1 } { 4 } > N _ { C Y 3 3 } = } \end{array}$ $N _ { D Y 3 3 } = N _ { C G 2 2 } = N _ { D G 2 2 } .$

![](/api/attachments/95SY3K9J/fulltext/images/6fdbaa90b7216f56082b243ee8cd4ec6f498e4de8cf2c0121b4dc3dd32583583.jpg)

![](/api/attachments/95SY3K9J/fulltext/images/f993dbe2abeb7faa52f475c585bc8e6a951eb12038a92c5cdc266b3a148a4bf3.jpg)  
Figure A-b: Demand Distribution of Class b (outcomes 22 and 33)

## (Class c) Outcomes 23 and 32

Under outcome 23, only pays for preferential delivery on <sub>??</sub> and only pays for preferential delivery on <sub>??</sub>. Under outcome 32, only pays for preferential delivery on <sub>??</sub> and only pays for preferential delivery on <sub>??</sub>. Thus $w _ { C G 2 3 } - w _ { C Y 2 3 } > 0 , w _ { D G 2 3 } - w _ { D Y 2 3 } < 0 , w _ { C G 3 2 } - w _ { C Y 3 2 } < 0$ and $w _ { D G 3 2 } - w _ { D Y 3 2 } > 0$ . Therefore we have $ { x _ { C 2 3 } } > \frac { 1 } { 2 } >  { x _ { D 2 3 } }$ and $\begin{array} { r } { x _ { C 3 2 } < \frac { 1 } { 2 } < x _ { D 3 2 } } \end{array}$ . Since the sign $x _ { C i j } - x _ { D i j }$ is the same as the sign of $z _ { Y i j } - z _ { G i j }$ for any outcome <sub>????</sub>, we have $z _ { Y 2 3 } > z _ { G 2 3 }$ and $z _ { Y 3 2 } < z _ { G 3 2 }$

Observe that both horizontal flip and vertical flip applied to outcome 23 gives outcome 32 and vice versa. Through the connection of horizontal flip, we have $x _ { C 2 3 } = 1 - x _ { C 3 2 } , x _ { D 2 3 } =$ $1 - x _ { D 3 2 } , z _ { Y 2 3 } = z _ { G 3 2 }$ , and $z _ { G 2 3 } = z _ { Y 3 2 }$ . Through the connection of Vertical flip, we have $x _ { C 2 3 } = x _ { D 3 2 } , x _ { D 2 3 } = x _ { C 3 2 } , z _ { Y 2 3 } = 1 - z _ { Y 3 2 }$ , and $z _ { G 2 3 } = 1 - z _ { G 3 2 }$ . Combining the two set of equalities gives $x _ { D 2 3 } = 1 - x _ { C 2 3 } , x _ { D 3 2 } = 1 - x _ { C 3 2 } , z _ { G 2 3 } = 1 - z _ { Y 2 3 }$ , and $z _ { G 3 2 } = 1 - z _ { Y 3 2 }$ Since $z _ { Y 2 3 } > z _ { G 2 3 }$ and $z _ { Y 3 2 } < z _ { G 3 2 }$ , the last set of equalities says that $z _ { Y 2 3 } > { \frac { 1 } { 2 } } > z _ { G 2 3 }$ and $z _ { Y 3 2 } < \frac { 1 } { 2 } < z _ { G 3 2 }$ . This says that the indifferent consumers $x _ { C 2 3 }$ and $x _ { D 2 3 }$ (as well as $x _ { C 3 2 }$ and $x _ { D 3 2 } )$ are symmetrically positioned on either side of $\begin{array} { r } { x = \frac { 1 } { 2 } . } \end{array}$ Likewise, $z _ { Y 2 3 }$ and $z _ { G 2 3 }$ (as well as $z _ { Y 3 2 }$ and $z _ { G 3 2 } )$ are symmetrically positioned on either side of $\begin{array} { r } { z = \frac { 1 } { 2 } . } \end{array}$ . Therefore the demands for , , , and in outcomes 23 and 32 are related such that $N _ { C Y 2 3 } = N _ { D G 2 3 } = N _ { C G 3 2 } =$ $N _ { D Y 3 2 }$ and $N _ { C G 2 3 } = N _ { D Y 2 3 } = N _ { C Y 3 2 } = N _ { D G 3 2 }$

As shown in Figure A-c, ISPs <sub>??</sub> and <sub>??</sub> have the same market share, i.e., $N _ { C 2 3 } = N _ { D 2 3 } =$ $\begin{array} { r } { N _ { C 3 2 } = N _ { D 3 2 } = \frac { 1 } { 2 } . } \end{array}$ . Within each ISP, the paying CP gets more customers than the non-paying CP, i.e., $\begin{array} { r } { N _ { C Y 2 3 } = N _ { D G 2 3 } = N _ { C G 3 2 } = N _ { D Y 3 2 } > \frac { 1 } { \lambda } > N _ { C Y 3 2 } = N _ { D G 3 2 } = N _ { C G 2 3 } = N _ { D Y 2 3 } } \end{array}$ 4

![](/api/attachments/95SY3K9J/fulltext/images/980de522e0e2a96e8868b9d7d48e8ca791cd462c1ba6ad4f3d35825e1ec06930.jpg)

![](/api/attachments/95SY3K9J/fulltext/images/9648ca1433931ee789d56739f5981edec51f168a28937eff86c874b821bb7082.jpg)

![](/api/attachments/95SY3K9J/fulltext/images/d1b30caa841ebd84870660ede48076b90d4b06fec10f90368e328bcbd253cc4c.jpg)  
Figure A-c: Demand Distribution of Class c (outcomes 23 and 32)

## (Class d) Outcomes 12, 13, 21, 31, 42, 43, 24, and 34

Based on CPs’ delivery service choices in outcomes 12, 13, 21, 31, 42, 43, 24, and 34, we know that $w _ { C G 1 2 } - w _ { C Y 1 2 } = w _ { C G 1 3 } - w _ { C Y 1 3 } = 0 , w _ { D G 2 1 } - w _ { D Y 2 1 } = w _ { D G 3 1 } - w _ { D Y 3 1 } = 0 , w _ { D G 1 2 } - w _ { D Y 1 2 } = 0 . 0 3 5$ $w _ { D Y 1 2 } > 0 , w _ { D G 1 3 } - w _ { D Y 1 3 } < 0 , w _ { C G 2 1 } - w _ { C Y 2 1 } > 0$ , and $w _ { C G 3 1 } - w _ { C Y 3 1 } < 0$ . Therefore we have $\begin{array} { r } { x _ { C 1 2 } = x _ { C 1 3 } = \frac { 1 } { 2 } , x _ { D 2 1 } = x _ { D 3 1 } = \frac { 1 } { 2 } , x _ { D 1 2 } > \frac { 1 } { 2 } > x _ { D 1 3 } } \end{array}$ , and $\begin{array} { r } { x _ { C 2 1 } > \frac { 1 } { 2 } > x _ { C 3 1 } } \end{array}$ . Since the sign $x _ { C i j } - x _ { D i j }$ is the same as the sign of $z _ { Y i j } - z _ { G i j }$ for any outcome <sub>????</sub>, we have $z _ { Y 1 2 } < z _ { G 1 2 }$ and $z _ { Y 2 1 } > z _ { G 2 1 }$ . Likewise, we have $z _ { Y 1 3 } > z _ { G 1 3 }$ and $z _ { Y 3 1 } < z _ { G 3 1 }$

Successive application of horizontal flip and vertical flip connect outcomes 12, 13, 21, and 31 as follows:

Through horizontal flip, we have $\begin{array} { r } { x _ { C 1 3 } = 1 - x _ { C 1 2 } = \frac { 1 } { 2 } , x _ { D 1 3 } = 1 - x _ { D 1 2 } < \frac { 1 } { 2 } , z _ { Y 1 3 } = z _ { G 1 2 } , } \end{array}$

$$
z _ {G 1 3} = z _ {Y 1 2}, x _ {C 3 1} = 1 - x _ {C 2 1} <   \frac {1}{2}, x _ {D 3 1} = 1 - x _ {D 2 1} = \frac {1}{2}, z _ {Y 3 1} = z _ {G 2 1}, \mathrm{and} z _ {G 3 1} = z _ {Y 2 1}.
$$

Through vertical flip, we have $\begin{array} { r } { x _ { C 2 1 } = x _ { D 1 2 } > \frac { 1 } { 2 } , x _ { D 2 1 } = x _ { C 1 2 } = \frac { 1 } { 2 } , z _ { Y 2 1 } = 1 - z _ { Y 1 2 } , z _ { G 2 1 } = 1 - } \end{array}$ $z _ { G 1 2 } , x _ { C 3 1 } = x _ { D 1 3 } < \frac { 1 } { 2 } , x _ { D 3 1 } = x _ { C 1 3 } = \frac { 1 } { 2 } , z _ { Y 3 1 } = 1 - z _ { Y 1 3 } .$ , and $z _ { G 3 1 } = 1 - z _ { G 1 3 }$ . Therefore the demand for , , , and in outcomes 12, 13, 21, and 31 are related such that $N _ { D Y 1 2 } =$ $N _ { D G 1 3 } = N _ { C G 3 1 } = N _ { C Y 2 1 } , N _ { D G 1 2 } = N _ { D Y 1 3 } = N _ { C Y 3 1 } = N _ { C G 2 1 } , N _ { C G 1 2 } = N _ { C Y 1 3 } = N _ { D Y 3 1 } = N _ { D G 2 1 } .$ and $N _ { C Y 1 2 } = N _ { C G 1 3 } = N _ { D G 3 1 } = N _ { D Y 2 1 }$

The demand analysis for outcomes 42, 43, 24, and 34 is the same as that in outcomes 12, 13, 21, and 31 since both CPs receive the same queuing priority when they both pay for preferential delivery. Therefore, the demand for <sub>????</sub>, <sub>??</sub> , <sub>????</sub>, and <sub>??</sub> in outcomes 42, 43, 24, and 34 are related such tha $N _ { D Y 4 2 } = N _ { D G 4 3 } = N _ { C G 3 4 } = N _ { C Y 2 4 } , N _ { D G 4 2 } = N _ { D Y 4 3 } = N _ { C Y 3 4 } = N _ { C G 2 4 } .$ $N _ { C G 4 2 } = N _ { C Y 4 3 } = N _ { D Y 3 4 } = N _ { D G 2 4 } , \mathrm { a n d } N _ { C Y 4 2 } = N _ { C G 4 3 } = N _ { D G 3 4 } = N _ { D Y 2 4 } .$

If and make identical decisions (1 or 4) on any ISP (<sub>??</sub> or <sub>??</sub>), consumers on that ISP will receive the same queuing priority. For example, under outcomes 13 and 43, indifferent consumers of all four ISP-CP combinations are the same, which leads to identical demand distribution for <sub>????</sub>, <sub>??</sub> , <sub>????</sub>, and <sub>??</sub> . That is $N _ { C Y 1 3 } = N _ { C Y 4 3 } , N _ { D Y 1 3 } = N _ { D Y 4 3 } , N _ { C G 1 3 } = N _ { C G 4 3 } ,$ and $N _ { D G 1 3 } = N _ { D G 4 3 }$ . By the same arguments above, we obtain the pairings with identical deman distribution for <sub>????</sub>, <sub>??</sub> , <sub>????</sub>, and <sub>??</sub> : outcomes 12 and 42, outcomes 21 and 24, and outcomes 31 and 34.

As shown in Figure A-d, outcomes in class d reveal particularly interesting demand patterns. For example, in outcome 43, although both CPs pay for preferential delivery on ISP <sub>??</sub>, gets fewer consumers than from ISP <sub>??</sub>, i.e., $N _ { C Y 4 3 } > N _ { C G 4 3 }$

![](/api/attachments/95SY3K9J/fulltext/images/1482fe359fe091c516c773d6346bffd12e7d3b9cb52f4c4b232d8e011b4aefea.jpg)

![](/api/attachments/95SY3K9J/fulltext/images/c741bc6bdd5674e75afed1ed9ed55e64affdf26b6d25ac2d6af7135036a5435c.jpg)

![](/api/attachments/95SY3K9J/fulltext/images/004590ab117606a13e5f922c4b8c032545af9ba533b19537fa11514bcbc80167.jpg)

![](/api/attachments/95SY3K9J/fulltext/images/ddf574f66557590e50e8c07c42c7c9b8ddb31b971d359f9be88aa4931cb15c7c.jpg)  
Figure A-d: Demand Distribution of Class d (outcomes 12, 13, 21, 31, 42, 43, 24, and 34)

Summarizing the above analysis for the symmetric equilibrium case, we conclude that the 16 outcomes can be grouped into four classes, within which all outcomes are invariant under horizontal and vertical flips with similar consumer demand patterns.

## B. Proof of Lemma 2 – The Symmetric Equilibrium Case

We derive the possible symmetric equilibria in the packet discrimination regime by the following steps: step 1, prove that all outcomes involving only <sub>??</sub> pays for priority delivery are infeasible; step 2, derive properties of the equilibrium fixed fee <sub>??</sub>; step 3, eliminate dominated outcomes.

Step 1: Prove that all outcomes involving only <sub>??</sub> pays for priority delivery are infeasible In step 1, we show that there is no feasible <sub>??</sub> for any outcome involving only <sub>??</sub> pays. Therefore such outcomes (12, 21, 42, 24, 23, 32, and 22) cannot be an equilibrium. Since some outcomes are infeasible for similar reasons, we group them together.

## Outcomes 12 and 21

Here we focus on showing that there is no feasible <sub>??</sub> for outcome 12, as the analysis for outcom 21 is similar. For outcomes 12 to be feasible, all the $\mathrm { C P s ^ { \prime } }$ incentive compatibility constraints need to be satisfied: <sub>(1)</sub> $\pi _ { Y 1 2 } - \pi _ { Y 2 2 } \geq 0 ; \left( 2 \right) \pi _ { Y 1 2 } - \pi _ { Y 1 1 } \geq 0 ; \left( 3 \right) \pi _ { Y 1 2 } - \pi _ { Y 2 1 } \geq 0 ;$

(4) $\pi _ { G 1 2 } - \pi _ { G 3 2 } \geq 0 ; \left( 5 \right) \pi _ { G 1 2 } - \pi _ { G 1 4 } \geq 0$ ; and <sub>(6)</sub> $\pi _ { G 1 2 } - \pi _ { G 3 4 } \geq 0$

Inequality (2) is $- N _ { D Y 1 2 } p \ + \ ( N _ { C Y 1 2 } - N _ { C Y 1 1 } - N _ { D Y 1 1 } + \ N _ { D Y 1 2 } ) r _ { Y } \ge 0$ . Since $N _ { C Y 1 2 } +$ $\begin{array} { r } { N _ { D Y 1 2 } > \frac { 1 } { 2 } \mathrm { a n d } N _ { C Y 1 1 } + N _ { D Y 1 1 } = \frac { 1 } { 2 } , } \end{array}$ inequality (2) can be reduced to $\begin{array} { r } { p \le \frac { ( N _ { C Y 1 2 } + N _ { D Y 1 2 } - 1 / 2 ) r _ { Y } } { N _ { D Y 1 2 } } } \end{array}$

Inequality (5) is $N _ { D G 1 4 } p + ( N _ { C G 1 2 } - N _ { C G 1 4 } + N _ { D G 1 2 } - N _ { D G 1 4 } ) r _ { G } \geq 0$ . Since $\begin{array} { r } { N _ { D G 1 4 } = \frac { 1 } { 4 } , } \end{array}$ $\begin{array} { r } { N _ { C G 1 4 } + N _ { D G 1 4 } = \frac { 1 } { 2 } , } \end{array}$ and $\begin{array} { r } { N _ { C G 1 2 } + N _ { D G 1 2 } < \frac { 1 } { 2 } , } \end{array}$ inequality (5) can be reduced to $p \geq$ $\frac { ( 1 / 2 - N _ { C G 1 2 } - N _ { D G 1 2 } ) r _ { G } } { 1 / 4 } .$

We know that $\begin{array} { r } { \frac { 1 } { 2 } - N _ { C G 1 2 } - N _ { D G 1 2 } = N _ { C Y 1 2 } + N _ { D Y 1 2 } - \frac { 1 } { 2 } , N _ { D Y 1 2 } > \frac { 1 } { 4 } . } \end{array}$ , and $r _ { G } \geq r _ { Y }$ . Thus we have $\begin{array} { r } { \frac { ( N _ { C Y 1 2 } + N _ { D Y 1 2 } - 1 / 2 ) r _ { Y } } { N _ { D Y 1 2 } } < \frac { ( 1 / 2 - N _ { C G 1 2 } - N _ { D G 1 2 } ) r _ { G } } { 1 / 4 } } \end{array}$ . Therefore (2) and (5) are inconsistent. Hence there is no solution for p that satisfies all incentive compatibility constraints for outcome 12.

## Outcomes 42 and 24

Outcomes 24 and 42 are infeasible for similar reasons. Outcome 24 is not feasible since the following incentive compatibility constraints are inconsistent: <sub>(1)</sub> $\pi _ { Y 2 4 } - \pi _ { Y 1 3 } \geq 0$ and (2) $\pi _ { G 2 4 } - \pi _ { G 4 4 } \geq 0$

Inequality (1) can be reduced to $\begin{array} { r } { p \leq \frac { ( N _ { C Y 2 4 } + N _ { D Y 2 4 } - N _ { C Y 1 3 } - N _ { D Y 1 3 } ) r _ { Y } } { ( N _ { C Y 2 4 } + N _ { D Y 2 4 } ) } } \end{array}$ . Note that we have $\begin{array} { r } { N _ { C Y 2 4 } + N _ { D Y 2 4 } - N _ { C Y 1 3 } - N _ { D Y 1 3 } = N _ { C Y 2 4 } + N _ { D Y 2 4 } - \frac { 1 } { 2 } + \frac { 1 } { 2 } - N _ { C Y 1 3 } - N _ { D Y 1 3 } } \end{array}$ . Since $N _ { C Y 2 4 } +$ $N _ { D Y 2 4 } - { \textstyle { \frac { 1 } { 2 } } } = { \textstyle { \frac { 1 } { 2 } } } - N _ { C Y 1 3 } - N _ { D Y 1 3 }$ , we have $N _ { C Y 2 4 } + N _ { D Y 2 4 } - N _ { C Y 1 3 } - N _ { D Y 1 3 } = 2 \left( N _ { C Y 2 4 } + \right.$ $\begin{array} { r } { N _ { D Y 2 4 } - \frac { 1 } { 2 } \bigg ) = 2 \left( \frac { 1 } { 2 } - N _ { C G 2 4 } - N _ { D G 2 4 } \right) } \end{array}$ . Thus inequality (1) can be simplified to $p \leq$ $\frac { ( 1 / 2 - N _ { C G 2 4 } - N _ { D G 2 4 } ) r _ { Y } } { ( N _ { C Y 2 4 } + N _ { D Y 2 4 } ) / 2 } .$

Inequality (2) can be reduced to $\begin{array} { r } { p \ge \frac { ( 1 / 2 - N _ { C G 2 4 } - N _ { D G 2 4 } ) r _ { G } } { ( 1 / 2 - N _ { D G 2 4 } ) } } \end{array}$ . Note that we have $N _ { C Y 2 4 } +$ $N _ { D Y 2 4 } + N _ { C G 2 4 } + N _ { D G 2 4 } = 1$ . But $N _ { C G 2 4 } < N _ { D G 2 4 }$ . Thus we have $\begin{array} { r } { \frac { N _ { C Y 2 4 } + N _ { D Y 2 4 } } { 2 } > \frac { 1 } { 2 } - N _ { D G 2 4 } } \end{array}$ Therefore $\begin{array} { r } { p \ge \frac { ( 1 / 2 - N _ { C G 2 4 } - N _ { D G 2 4 } ) r _ { G } } { ( 1 / 2 - N _ { D G 2 4 } ) } > \frac { ( 1 / 2 - N _ { C G 2 4 } - N _ { D G 2 4 } ) r _ { G } } { ( N _ { C Y 2 4 } + N _ { D Y 2 4 } ) / 2 } . } \end{array}$

In addition, we know $r _ { G } \geq r _ { Y }$ . Thus we have $\begin{array} { r } { \frac { \left( 1 / 2 - N _ { C G 2 4 } - N _ { D G 2 4 } \right) r _ { G } } { \left( 1 / 2 - N _ { D G 2 4 } \right) } > \frac { \left( 1 / 2 - N _ { C G 2 4 } - N _ { D G 2 4 } \right) r _ { G } } { \left( N _ { C Y 2 4 } + N _ { D Y 2 4 } \right) / 2 } \ge } \end{array}$ $\frac { ( 1 / 2 - N _ { C G 2 4 } - N _ { D G 2 4 } ) r _ { Y } } { ( N _ { C Y 2 4 } + N _ { D Y 2 4 } ) / 2 }$ . Therefore inequalities (1) and (2) are inconsistent. Hence outcome 24 is infeasible.

## Outcomes 23 and 32

Outcomes 23 and 32 are infeasible for similar reasons. Outcome 23 is feasible provided $\pi _ { Y 2 3 } -$ $\begin{array} { r } { \pi _ { Y 1 4 } \geq 0 , \mathrm { i . e . , } \left( \frac { 1 } { 4 } - N _ { C Y 2 3 } \right) p + \left( N _ { C Y 2 3 } + N _ { D Y 2 3 } - \frac { 1 } { 2 } \right) r _ { Y } \geq 0 } \end{array}$ . Note that $\begin{array} { r } { N _ { C Y 2 3 } + N _ { D Y 2 3 } = \frac { 1 } { 2 } . } \end{array}$ . This gives $\left( \frac { 1 } { 4 } - N _ { C Y 2 3 } \right) p \ge 0$ . Since $\begin{array} { r } { N _ { C Y 2 3 } > \frac { 1 } { 4 } , } \end{array}$ , we have $p \leq 0$ . Hence there is no positive solution for <sub>??</sub> and therefore outcome 23 is not feasible.

## Outcome 22

Outcome 22 is not feasible since the following incentive compatibility constraints are

inconsistent: <sub>(1)</sub> $\pi _ { Y 2 2 } - \pi _ { Y 1 1 } \geq 0$ and (2) $\pi _ { G 2 2 } - \pi _ { G 4 4 } \geq 0$

Inequality (1) is $\begin{array} { r } { \left( N _ { C G 2 2 } - N _ { C G 3 3 } - \frac { 1 } { 2 } \right) p + \left( N _ { C G 3 3 } - N _ { C G 2 2 } \right) r _ { Y } \geq 0 } \end{array}$ . Note that $N _ { C G 2 2 } +$ $\begin{array} { r } { N _ { C Y 2 2 } = \frac { 1 } { 2 } . } \end{array}$ Thus we have $\begin{array} { r } { \left( N _ { C G 2 2 } - N _ { C G 3 3 } - \frac { 1 } { 2 } \right) = - N _ { C G 3 3 } - N _ { C Y 2 2 } = - 2 N _ { C G 3 3 } < 0 } \end{array}$ . Therefore inequality (1) can be reduced to $\begin{array} { r } { p \le \left( \frac { 1 } { 2 } - \frac { N _ { C G 2 2 } } { 2 N _ { C G 3 3 } } \right) r _ { Y } } \end{array}$ . Inequality (2) can be reduced to $p \geq$ $( 1 - 4 N _ { C G 2 2 } ) r _ { G }$

Recall that $N _ { C G 2 2 } = N _ { C Y 3 3 } , N _ { C Y 2 2 } = N _ { C G 3 3 }$ , and $\begin{array} { r } { N _ { C Y 3 3 } + N _ { C G 3 3 } = \frac { 1 } { 2 } . } \end{array}$ Thus inequality (1) may be re-written as $\begin{array} { r } { p \le \left( 1 - \frac { 1 } { 4 N _ { C G 3 3 } } \right) r _ { Y } } \end{array}$ and inequality (2) may be re-written as $p \geq$ $\begin{array} { r } { 4 N _ { C G 3 3 } \left( 1 - \frac { 1 } { 4 N _ { C G 3 3 } } \right) r _ { G } } \end{array}$ . Since $r _ { Y } \leq r _ { G }$ and $4 N _ { C G 3 3 } > 1$ , inequality (1) implies that $p \leq$ $\begin{array} { r } { \left( 1 - \frac { 1 } { 4 N _ { C G 3 3 } } \right) r _ { Y } < r _ { G } } \end{array}$ but inequality (2) implies that $\begin{array} { r } { p \ge 4 N _ { C G 3 3 } \left( 1 - \frac { 1 } { 4 N _ { C G 3 3 } } \right) r _ { G } > r _ { G } } \end{array}$ . Therefore inequalities (1) and (2) are inconsistent and there is no feasible <sub>??</sub> for outcome 22.

In summary, outcomes 12, 21, 42, 24, 23, 32, and 22 cannot be an equilibrium.

## Step 2: Derive properties of the equilibrium fixed fee <sub>??</sub>

In step 2, we derive properties of the equilibrium fixed fee <sub>??</sub>. Here we first discuss some properties for all 16 outcomes and thus the subscript <sub>????</sub> is omitted in this discussion. Under the assumption of full market coverage, the profit maximizing fixed fee <sub>??</sub> is such that the consumers of all four ISP-CP combinations (<sub>??</sub> , <sub>??</sub> , <sub>????</sub>, and <sub>??</sub> ) with the lowest net utility will get zero net utility.

We now define the global utility function $U ( x , z )$ for the entire market $[ 0 , 1 ] \times [ 0 , 1 ]$ . First recall the definition of the demand distribution of each ISP-CP combinations characterized by the utility functions.

$$
R _ {C Y} = \{(x, z) \in [ 0, 1 ] \times [ 0, 1 ]; u _ {C Y} (x, z) \geq \max \{u _ {C G} (x, z), u _ {D Y} (x, z), u _ {D G} (x, z) \} \}
$$

$$
R _ {D Y} = \{(x, z) \in [ 0, 1 ] \times [ 0, 1 ]; u _ {D Y} (x, z) \geq \max \{u _ {D G} (x, z), u _ {C Y} (x, z), u _ {C G} (x, z) \} \}
$$

$$
R _ {C G} = \{(x, z) \in [ 0, 1 ] \times [ 0, 1 ]; u _ {C G} (x, z) \geq \max \{u _ {C Y} (x, z), u _ {D G} (x, z), u _ {D Y} (x, z) \} \}
$$

$$
R _ {D G} = \{(x, z) \in [ 0, 1 ] \times [ 0, 1 ]; u _ {D G} (x, z) \geq \max \{u _ {D Y} (x, z), u _ {C G} (x, z), u _ {C Y} (x, z) \} \}
$$

Note that each of the following inequalities reduces to regions on $[ 0 , 1 ] \times [ 0 , 1 ]$ dictated by the indifference customers between mutual pairs of $\mathrm { I S P - C P }$ combinations:

$$
u _ {C G} (x, z) - u _ {C Y} (x, z) \geq 0 \Longleftrightarrow x \geq x _ {C}
$$

$$
u _ {D G} (x, z) - u _ {D Y} (x, z) \geq 0 \Longleftrightarrow x \geq x _ {D}
$$

$$
u _ {D Y} (x, z) - u _ {C Y} (x, z) \geq 0 \Leftrightarrow z \geq z _ {Y}
$$

$$
u _ {D G} (x, z) - u _ {C G} (x, z) \geq 0 \Longleftrightarrow z \geq z _ {G}
$$

$$
u _ {D G} (x, z) - u _ {C Y} (x, z) \geq 0 \Leftrightarrow z \geq L _ {-} (x)
$$

$$
u _ {D Y} (x, z) - u _ {C G} (x, z) \geq 0 \Longleftrightarrow z \geq L _ {+} (x)
$$

Then the demand distributions can be written in terms of the indifference customers as follows:

$$
R _ {C Y} = \{(x, z) \in [ 0, 1 ] \times [ 0, 1 ]; x \leq x _ {C}, z \leq z _ {Y}, z \leq L _ {-} (x) \}
$$

$$
R _ {D Y} = \{(x, z) \in [ 0, 1 ] \times [ 0, 1 ]; x \leq x _ {D}, z \geq z _ {Y}, z \geq L _ {+} (x) \}
$$

$$
R _ {C G} = \{(x, z) \in [ 0, 1 ] \times [ 0, 1 ]; x \geq x _ {C}, z \leq z _ {G}, z \leq L _ {+} (x) \}
$$

$$
R _ {D G} = \{(x, z) \in [ 0, 1 ] \times [ 0, 1 ]; x \geq x _ {D}, z \geq z _ {G}, z \geq L _ {-} (x) \}
$$

Define the global utility function $U ( x , z )$ over the entire market $[ 0 , 1 ] \times [ 0 , 1 ]$ :

$$
U (x, z) = \left\{ \begin{array}{l l} u _ {C Y} (x, z), & \mathrm{if} (x, z) \in R _ {C Y} \\ u _ {D Y} (x, z), & \mathrm{if} (x, z) \in R _ {D Y} \\ u _ {C G} (x, z), & \mathrm{if} (x, z) \in R _ {C G} \\ u _ {D G} (x, z), & \mathrm{if} (x, z) \in R _ {D G} \end{array} \right.
$$

By definition of the demand regions $R _ { C Y } , R _ { D Y } , R _ { C G }$ , and $R _ { D G }$ , the global utility function gives the maximal utility value for the consumer $( x , z )$ according to its choice of ISP-CP combination. We also note that $U ( x , z )$ is a continuous function over the set $[ 0 , 1 ] \times [ 0 , 1 ]$ . Indeed, first note that the functions $u _ { C Y } ( x , z ) , u _ { D Y } ( x , z ) , u _ { C G } ( x , z )$ , and $u _ { D G } ( x , z )$ are linear functions in $( x , z )$ and thus are all continuous. Since $U ( x , z )$ is piecewise defined over demand regions $R _ { C Y } , R _ { D Y } , R _ { C G }$ and $R _ { D G }$ , we only need to check that $U ( x , z )$ is continuous at each point on the boundaries between mutual pairs of the demand regions $R _ { C Y } , R _ { D Y } , R _ { C G }$ , and $R _ { D G }$ . We check each boundary:

• Between $R _ { C Y }$ and $R _ { D Y }$ , the boundary is along the line $z = z _ { Y }$ on which $u _ { C Y } = u _ { D Y }$

Between $R _ { C Y }$ and $R _ { C G }$ , the boundary is along the line ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { C }$ on which $u _ { C Y } = u _ { C G }$

• Between $R _ { C Y }$ and $R _ { D G }$ , the boundary is along the line $z = L _ { - } ( x )$ on which $u _ { C Y } = u _ { D G }$

• Between $R _ { D G }$ and $R _ { C G }$ , the boundary is along the line $z = z _ { G }$ on which $u _ { D G } = u _ { C G }$

• Between $R _ { D G }$ and $R _ { D Y }$ , the boundary is along the line $\boldsymbol { x } = \boldsymbol { x } _ { D }$ on which $u _ { D G } = u _ { D Y }$

• Between $R _ { D Y }$ and $R _ { C G }$ , the boundary is along the line $z = L _ { + } ( x )$ on which $u _ { D Y } = u _ { C G }$

Since corresponding utility functions all matches along the boundaries between mutual pairs of the demand regions $R _ { C Y } , R _ { D Y } , R _ { C G }$ , and $R _ { D G }$ , the global utility function $U ( x , z )$ is continuous over the entire set $[ 0 , 1 ] \times [ 0 , 1 ]$

The global utility function $U ( x , z )$ is a continuous function over the closed and bounded set $[ 0 , 1 ] \times [ 0 , 1 ]$ . Therefore $U ( x , z )$ attains its maximum and minimum at some points in the set $[ 0 , 1 ] \times [ 0 , 1 ]$ . Under the assumption of full market coverage, the optimal fixed fees the ISPs charge consumers are such that the minimum of $U ( x , z )$ equal to zero. In other words, the optimal fixed fee is the maximum fee such that all consumers get nonnegative utility.

Since $U ( x , z )$ is piecewise defined by linear functions, it has no critical points in the interior of each demand regions $R _ { C Y } , R _ { D Y } , R _ { C G }$ , and $R _ { D G }$ . Therefore we only need to analyze the value of $U ( x , z )$ along each mutual boundaries to capture the minimum of $U ( x , z )$ . Before we analyze the boundaries between $R _ { C Y } , R _ { D Y } , R _ { C G }$ , and $R _ { D G }$ , we recall that the demand distributions split into the three geometric types (i) $x _ { C } = x _ { D }$ and $z _ { Y } = z _ { G } ; ( \mathrm { i i } ) x _ { C } < x _ { D }$ and $z _ { Y } < z _ { G }$ ; and (iii) $x _ { C } > x _ { D }$ and $z _ { Y } > z _ { G }$

The feasible outcomes 11, 14, 41, 44, and 33 are of type (i), where the demand regions are all rectangular in shape. The feasible outcomes 31 and 34 are of type (ii), which have exactly two rectangles, and two pentagonal regions sharing a boundary along $z = L _ { + } ( x )$ . And finally, the feasible outcomes 13 and 43 are of type (iii), which have exactly two rectangles, and two pentagonal regions sharing a boundary along $z = L _ { - } ( x )$

We organize the analysis into two cases $( \mathbf { A } ) \colon x _ { C } \leq x _ { D }$ and $z _ { Y } \leq z _ { G }$ and (B): $x _ { C } \geq x _ { D }$ and $z _ { Y } \ge z _ { G }$ . Obviously, Cases (A) and (B) overlaps in those of type (i) here the diagonal boundary on $z = L _ { + } ( x ) \mathrm { o r } z = L _ { - } ( x )$ collapses to the point of intersection of these lines.

Case $( A ) \colon x _ { C } \leq x _ { D }$ and $\underline { { Z _ { Y } } } \leq \underline { { Z _ { G } } }$

There are five boundaries including a segment on $z = L _ { + } ( x )$

(A1) Boundary between $R _ { C Y }$ and $R _ { D Y }$ . This boundary is along the horizontal line $z = z _ { Y }$ and is the line segment joining $( 0 , z _ { Y } )$ and the point $( x _ { C } , z _ { Y } )$ . Since $u _ { C Y } = u _ { D Y }$ on this boundary, along the boundary we may write for $0 \le x \le x _ { C } , U ( x , z _ { Y } ) = u _ { C Y } ( x , z _ { Y } ) = V - t x - k z _ { Y } -$ $d \lambda w _ { C Y } - F _ { C } , \mathrm { o r } U ( x , z _ { Y } ) = u _ { D Y } ( x , z _ { Y } ) = V - t x - k ( 1 - z _ { Y } ) - d \lambda w _ { D Y } - F _ { D }$ . In either formula, we see that on this boundary $U ( x , z )$ is a decreasing function of <sub>??</sub>. Therefore $U ( x , z )$ minimizes at $( x _ { C } , z _ { Y } )$ on the boundary between $R _ { C Y }$ and $R _ { D Y }$

(A2) Boundary between $R _ { D G }$ and $R _ { C G }$ . This boundary is along the horizontal line $z = z _ { G }$ and is the line segment joining $( x _ { D } , z _ { G } )$ and the point $( 1 , z _ { G } )$ . Since ${ \mathfrak { u } } _ { D G } = { \mathfrak { u } } _ { C G }$ on this boundary along the boundary we may write for $x _ { D } \leq x \leq 1 , U ( x , z _ { G } ) = u _ { C G } ( x , z _ { G } ) = V - t ( 1 - x ) -$ $k z _ { G } - d \lambda w _ { C G } - F _ { C } , \mathrm { o r } U ( x , z _ { G } ) = u _ { D G } ( x , z _ { G } ) = V - t ( 1 - x ) - k ( 1 - z _ { G } ) - d \lambda w _ { D G } - F _ { D }$ . In either formula, we see that on this boundary $U ( x , z )$ is a increasing function of . Therefore $U ( x , z )$ minimizes at $( x _ { D } , z _ { G } )$ on the boundary between $R _ { D G }$ and $R _ { C G }$

(A3) Boundary between $R _ { C Y }$ and $R _ { C G }$ . This boundary is along the vertical line $x = x _ { C }$ and is the line segment joining $( x _ { C } , 0 )$ and the point $( x _ { C } , z _ { Y } )$ . Since $u _ { C Y } = u _ { C G }$ on this boundary, along the boundary we may write for $0 \leq z \leq z _ { Y } , U ( x _ { C } , z ) = u _ { C Y } ( x _ { C } , z ) = V - t x _ { C } - k z -$ $d \lambda w _ { C Y } - F _ { C } , \mathrm { o r } U ( x _ { C } , z ) = u _ { C G } ( x _ { C } , z ) = V - t ( 1 - x _ { C } ) - k z - d \lambda w _ { C G } - F _ { C }$ . In either formula, we see that on this boundary $U ( x , z )$ is a decreasing function of . Therefore $U ( x , z )$ minimizes at $( x _ { C } , z _ { Y } )$ on the boundary between $R _ { C Y }$ and $R _ { C G }$

(A4) Boundary between $R _ { D G }$ and $R _ { D Y }$ . This boundary is along the vertical line $\boldsymbol { x } = \boldsymbol { x } _ { D }$ and is the line segment joining $( x _ { D } , z _ { G } )$ and the point $( x _ { D } , 1 )$ . Since $u _ { C Y } = u _ { C G }$ on this boundary, along the boundary we may write for $z _ { G } \leq z \leq 1 , U ( x _ { D } , z ) = u _ { D Y } ( x _ { D } , z ) = V - t x _ { D } - k ( 1 -$

$z ) - d \lambda w _ { D Y } - F _ { D } , \mathrm { o r } \ U ( x _ { D } , z ) = u _ { D G } ( x _ { D } , z ) = V - t ( 1 - x _ { D } ) - k ( 1 - z ) - d \lambda w _ { D G } - F _ { D } | | \lambda w _ { D } - z | | ^ { 2 } ,$ . In either formula, we see that on this boundary $U ( x , z )$ is a increasing function of . Therefore $U ( x , z )$ minimizes at $( x _ { D } , z _ { G } )$ on the boundary between $R _ { D G }$ and $R _ { D Y }$ (A5) Boundary between $R _ { C G }$ and $R _ { D Y }$ . This boundary is along the line $z = L _ { + } ( x )$ and is the line segment joining $( x _ { C } , z _ { Y } )$ and the point $( x _ { D } , z _ { G } )$ . We parameterize the directed line segment as follows: For $0 \leq s \leq 1 , x = ( 1 - s ) x _ { C } + s x _ { D }$ and $z = ( 1 - s ) z _ { Y } + s z _ { G }$ . On this boundary the utility function <sub>??</sub> is a function of the parameter <sub>??</sub>. Since $u _ { C G } = u _ { D Y }$ on this boundary, along the boundary we may write for $0 \leq s \leq 1 , U ( s ) = u _ { D Y } ( ( 1 - s ) x _ { C } + s x _ { D } , ( 1 -$ ??)?? + ???? ) = ?? − ??[(1 − ??)?? + ???? ] − ??[1 − (1 − ??)?? − ???? ] − ?????? − ?? = ?? + ?? (?? − ?? ) − ???? − ??(1 − ?? ) + ?? (?? − ?? ) − ?????? − ?? <sup>,</sup> <sup>or</sup> ??(??) = ?? ((1 − ??)?? + ???? , (1 − ??)?? + ???? ) = ??( ) − ??[1 − (1 − ??)?? − ???? ] − ??[(1 − ??)?? + ???? ] − ?????? − $F _ { C } = V ( \lambda ) - t ( 1 - x _ { C } ) + s t ( x _ { D } - x _ { C } ) - k z _ { Y } + s k ( z _ { Y } - z _ { G } ) - d \lambda w _ { C G } - F _ { C } . \mathrm { I f } \ x _ { D } = x _ { C }$ and $z _ { Y } = z _ { G }$ then <sub>??(??)</sub> is a constant not dependent on <sub>??</sub>. However, in general we note that the slope of $z = L _ { + } ( x )$ is given by $\begin{array} { r } { \frac { t } { k } = \frac { z _ { G } - z _ { Y } } { x _ { D } - x _ { C } } , } \end{array}$ i.e., $k ( z _ { G } - z _ { Y } ) = t ( x _ { D } - x _ { C } )$ . Thus the values of $U ( s )$ reduces to the constant: $U ( s ) = V - t x _ { C } - k ( 1 - z _ { Y } ) - d \lambda w _ { D Y } - F _ { D } \mathrm { o r } U ( s ) = V - t ( 1 -$ $x _ { C } ) - k z _ { Y } - d \lambda w _ { C G } - F _ { C }$ . From the analysis above, we could see that $U ( x , z )$ minimizes on the points along the boundary on the line $z = L _ { + } ( x )$ . In particular, $U ( x , z )$ minimizes at $( x _ { C } , z _ { Y } )$ or $( x _ { D } , z _ { G } )$ with the same value.

Case (B): <sub>?? ≥</sub> <sub>??</sub> and <sub>?? ≥</sub> <sub>??</sub>

There are five boundaries including a segment on $z = L _ { - } ( x )$

(B1) Boundary between $R _ { C Y }$ and $R _ { D Y }$ . This boundary is along the horizontal line $z = z _ { Y }$ and is the line segment joining $( 0 , z _ { Y } )$ and the point $( x _ { D } , z _ { Y } )$ . Since $u _ { C Y } = u _ { D Y }$ on this boundary, along the boundary we may write for $0 \le x \le x _ { D } , U ( x , z _ { Y } ) = u _ { C Y } ( x , z _ { Y } ) = V - t x - k z _ { Y } -$ $d \lambda w _ { C Y } - F _ { C } , \mathrm { o r } U ( x , z _ { Y } ) = u _ { D Y } ( x , z _ { Y } ) = V - t x - k ( 1 - z _ { Y } ) - d \lambda w _ { D Y } - F _ { D }$ . In either formula, we see that on this boundary $U ( x , z )$ is a decreasing function of <sub>??</sub>. Therefore $U ( x , z )$ minimizes at $( x _ { D } , z _ { Y } )$ on the boundary between $R _ { C Y }$ and $R _ { D Y }$

(B2) Boundary between $R _ { D G }$ and $R _ { C G }$ . This boundary is along the horizontal line $z = z _ { G }$ and is the line segment joining $( x _ { C } , z _ { G } )$ and the point $( 1 , z _ { G } )$ . Since $u _ { D G } = u _ { C G }$ on this boundary, along the boundary we may write for $x _ { C } \leq x \leq 1 , U ( x , z _ { G } ) = u _ { C G } ( x , z _ { G } ) = V - t ( 1 - x ) -$ $k z _ { G } - d \lambda w _ { C G } - F _ { C } , \mathrm { o r } U ( x , z _ { G } ) = u _ { D G } ( x , z _ { G } ) = V - t ( 1 - x ) - k ( 1 - z _ { G } ) - d \lambda w _ { D G } - F _ { D }$ . In either formula, we see that on this boundary $U ( x , z )$ is a increasing function of . Therefore $U ( x , z )$ minimizes at $( x _ { C } , z _ { G } )$ on the boundary between $R _ { D G }$ and $R _ { C G }$

(B3) Boundary between $R _ { C Y }$ and $R _ { C G }$ . This boundary is along the vertical line ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { C }$ and is the line segment joining $( x _ { C } , 0 )$ and the point $( x _ { C } , z _ { G } )$ . Since $u _ { C Y } = u _ { C G }$ on this boundary, along the boundary we may write for $0 \leq z \leq z _ { G } , U ( x _ { C } , z ) = u _ { C Y } ( x _ { C } , z ) = V - t x _ { C } - k z -$ $d \lambda w _ { C Y } - F _ { C } , \mathrm { o r } U ( x _ { C } , z ) = u _ { C G } ( x _ { C } , z ) = V - t ( 1 - x _ { C } ) - k z - d \lambda w _ { C G } - F _ { C }$ . In either formula, we see that on this boundary $U ( x , z )$ is a decreasing function of <sub>??</sub>. Therefore $U ( x , z )$ minimizes at $( x _ { C } , z _ { G } )$ on the boundary between $R _ { C Y }$ and $R _ { C G }$

(B4) Boundary between $R _ { D G }$ and $R _ { D Y }$ . This boundary is along the vertical line $\boldsymbol { x } = \boldsymbol { x } _ { D }$ and is the line segment joining $( x _ { D } , z _ { Y } )$ and the point $( x _ { D } , 1 )$ . Since $u _ { C Y } = u _ { C G }$ on this boundary along the boundary we may write for $z _ { Y } \le z \le 1 , U ( x _ { D } , z ) = u _ { D Y } ( x _ { D } , z ) = V - t x _ { D } - k ( 1 -$ $z ) - d \lambda w _ { D Y } - F _ { D } , \mathrm { o r } U ( x _ { D } , z ) = u _ { D G } ( x _ { D } , z ) = V - t ( 1 - x _ { D } ) - k ( 1 - z ) - d \lambda w _ { D G } - F _ { D } $ . In either formula, we see that on this boundary $U ( x , z )$ is a increasing function of . Therefore $U ( x , z )$ minimizes at $( x _ { D } , z _ { Y } )$ on the boundary between $R _ { D G }$ and $R _ { D Y }$

(B5) Boundary between $R _ { C Y }$ and $R _ { D G }$ . This boundary is along the line $z = L _ { - } ( x )$ and is the line segment joining $( x _ { D } , z _ { Y } )$ and the point $( x _ { C } , z _ { G } )$ . We parameterize the directed line segment as follows: For $0 \leq s \leq 1 , x = ( 1 - s ) x _ { D } + s x _ { C }$ and $z = ( 1 - s ) z _ { Y } + s z _ { G }$ . On this boundary the utility function <sub>??</sub> is a function of the parameter <sub>??</sub>. Since $u _ { C Y } = u _ { D G }$ on this boundary, along the boundary we may write for $0 \leq s \leq 1 , U ( s ) = u _ { D G } ( ( 1 - s ) x _ { D } + s x _ { C } , ( 1 -$ $s ) z _ { Y } + s z _ { G } ) = V - t [ 1 - ( 1 - s ) x _ { D } - s x _ { c } ] - k [ 1 - ( 1 - s ) z _ { Y } - s z _ { G } ] - d \lambda w _ { D G } - F _ { D } = V + s z _ { G } .$ $s t ( x _ { c } - x _ { D } ) - t ( 1 - x _ { D } ) - k ( 1 - z _ { Y } ) + s k ( z _ { G } - z _ { Y } ) - d \lambda w _ { D G } - F _ { D } , \mathrm { o r } U ( s ) =$ $u _ { c Y } ( ( 1 - s ) x _ { D } + s x _ { C } , ( 1 - s ) z _ { Y } + s z _ { G } ) = V - t [ ( 1 - s ) x _ { D } + s x _ { C } ] - k [ ( 1 - s ) z _ { Y } + s z _ { G } ] - u _ { c Y } ( ( 1 - s ) \mathbf { k } + s \mathbf { r } _ { D } )$ $d \lambda w _ { C Y } - F _ { C } = V - t x _ { D } + s t ( x _ { D } - x _ { C } ) - k z _ { Y } + s k ( z _ { Y } - z _ { G } ) - d \lambda w _ { C Y } - F _ { C } . \mathrm { I f } \ x _ { D } = x _ { C }$ and $z _ { Y } = z _ { G }$ then $U ( s )$ is a constant not dependent on <sub>??</sub>. However, in general we note that the slope of $z = L _ { - } ( x )$ is given by: $\begin{array} { r } { - \frac { t } { k } = \frac { z _ { G } - z _ { Y } } { x _ { C } - x _ { D } } , } \end{array}$ i.e., $k ( z _ { G } - z _ { Y } ) = t ( x _ { D } - x _ { C } )$ . Thus the values of $U ( s )$ reduces to the constant: $U ( s ) = V - t ( 1 - x _ { D } ) - k ( 1 - z _ { Y } ) - d \lambda w _ { D G } - F _ { D } \mathrm { o r } U ( s ) = V - t ( 1 - x _ { D } ) ,$ $t x _ { D } - k z _ { Y } - d \lambda w _ { C Y } - F _ { C }$ . From the analysis above, we could see that $U ( x , z )$ minimizes on the points along the boundary on the line $z = L _ { - } ( x )$ . In particular, $U ( x , z )$ minimizes at $( x _ { D } , z _ { Y } )$ or $( x _ { C } , z _ { G } )$ with the same value.

Maximum Fees for Case A: The maximum fees occur when the minimum of the global utility function is zero. Therefore from the formulas in (A5), the maximum fees are given by: $V - t x _ { C } - k ( 1 - z _ { Y } ) - d \lambda w _ { D Y } - F _ { D } = 0 \mathrm { a n d } V - t ( 1 - x _ { C } ) - k z _ { Y } - d \lambda w _ { C G } - F _ { C } = 0$ . This gives the maximum fees: $\begin{array} { r } { F _ { C } = V - t \left( 1 - \frac { x _ { C } + x _ { D } } { 2 } \right) - k \left( \frac { z _ { Y } + z _ { G } } { 2 } \right) - d \lambda w _ { C G } } \end{array}$ and $F _ { D } = V -$ $\begin{array} { r } { t \left( \frac { x _ { C } + x _ { D } } { 2 } \right) - k \left( 1 - \frac { z _ { Y } + z _ { G } } { 2 } \right) - d \lambda w _ { D Y } } \end{array}$

Maximum Fees for Case B: The maximum fees occur when the minimum of the global utility function is zero. Therefore from the formulas in (B5), the maximum fees are given by: $V - t ( 1 - x _ { D } ) - k ( 1 - z _ { Y } ) - d \lambda w _ { D G } - F _ { D } = 0 \mathrm { a n d } V - t x _ { D } - k z _ { Y } - d \lambda w _ { C Y } - F _ { C } = 0$ . This gives the maximum fees: $\begin{array} { r } { F _ { C } = V - t \left( \frac { x _ { C } + x _ { D } } { 2 } \right) - k \left( \frac { z _ { Y } + z _ { G } } { 2 } \right) - d \lambda w _ { C Y } } \end{array}$ and $F _ { D } = V -$ $\begin{array} { r } { t \left( 1 - \frac { x _ { C } + x _ { D } } { 2 } \right) - k \left( 1 - \frac { z _ { Y } + z _ { G } } { 2 } \right) - d \lambda w _ { D G } . } \end{array}$

We next solve for the optimal fixed fee for feasible outcomes in symmetric equilibrium when $F _ { C } = F _ { D } = F$

Optimal <sub>??</sub> for outcomes 11, 14, 41, and 44: All waiting times are the same and $x _ { C } =$ $\begin{array} { r } { x _ { D } = z _ { Y } = z _ { G } = \frac { 1 } { 2 } . } \end{array}$ Using the formulas for maximum fees above, we get $F _ { 1 1 } = F _ { 1 4 } = F _ { 4 1 } =$ $\begin{array} { r } { F _ { 4 4 } = V - \frac { t } { 2 } - \frac { k } { 2 } - \frac { d \lambda } { \mu - \lambda / 2 } . } \end{array}$

Optimal <sub>??</sub> for outcome 33: In this outcome, $z _ { Y 3 3 } = z _ { G 3 3 } = { \textstyle { \frac { 1 } { 2 } } } \operatorname { a n d } x _ { D 3 3 } = x _ { C 3 3 } < { \textstyle { \frac { 1 } { 2 } } } .$ We have four formulas for F which must be consistent. We verify that those in Case A and Case B both reduces to the following formula for $\begin{array} { r } { F \colon F _ { 3 3 } = V - t ( 1 - x _ { D 3 3 } ) - \frac { k } { 2 } - \frac { 2 d \lambda } { 2 \mu - ( 1 - x _ { D 3 3 } ) \lambda } . } \end{array}$

Optimal <sub>??</sub> for outcomes 13 and 43: These outcomes have the same demand distributions and so the same indifferent customers and waiting times. We use the formulas for Case B for these outcomes: $\begin{array} { r } { F _ { 4 3 } = F _ { 1 3 } = V - t ( 1 - x _ { D 4 3 } ) - k ( 1 - z _ { Y 4 3 } ) - \frac { d \lambda } { \mu - N _ { D G 4 3 } \lambda } . } \end{array}$

Optimal <sub>??</sub> for outcomes 31 and 34: These outcomes have the same demand distributions and so the same indifferent customers and waiting times. We use the formulas for Case A for these outcomes: $\begin{array} { r } { F _ { 3 4 } = F _ { 3 1 } = V - t ( 1 - x _ { C 3 4 } ) - k z _ { Y 3 4 } - \frac { d \lambda } { \mu - N _ { C G 3 4 } \lambda } . } \end{array}$

## Step 3: Eliminate dominated outcomes

From step 1, we know that any outcome involving only <sub>??</sub> pays on an ISP cannot be an equilibrium. Therefore, outcomes 12, 21, 22, 23, 24, 32, and 42 can be eliminated from the equilibrium analysis as shown in the following table.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="4">Decisions of Y and G on ISP D</td></tr><tr><td>1: Neither pays D</td><td>2: Y pays D</td><td>3: G pays D</td><td>4: both pay D</td></tr><tr><td rowspan="4">Decisions of Y and G on ISP C</td><td>1: Neither pays C</td><td> $(\pi_{C11}, \pi_{D11})$ </td><td> $(\pi_{C12}, \pi_{D12})$ </td><td> $(\pi_{C13}, \pi_{D13})$ </td><td> $(\pi_{C14}, \pi_{D14})$ </td></tr><tr><td>2: Y pays C</td><td> $(\pi_{C21}, \pi_{D21})$ </td><td> $(\pi_{C22}, \pi_{D22})$ </td><td> $(\pi_{C23}, \pi_{D23})$ </td><td> $(\pi_{C24}, \pi_{D24})$ </td></tr><tr><td>3: G pays C</td><td> $(\pi_{C31}, \pi_{D11})$ </td><td> $(\pi_{C32}, \pi_{D32})$ </td><td> $(\pi_{C33}, \pi_{D33})$ </td><td> $(\pi_{C34}, \pi_{D34})$ </td></tr><tr><td>4: both pay C</td><td> $(\pi_{C41}, \pi_{D41})$ </td><td> $(\pi_{C42}, \pi_{42})$ </td><td> $(\pi_{C43}, \pi_{D43})$ </td><td> $(\pi_{C44}, \pi_{D44})$ </td></tr></table>

Next, we further eliminate other dominated outcomes by comparing CPs’ profits. Recall that: $\begin{array} { r } { \pi _ { C 1 1 } = \pi _ { D 1 1 } = \frac { F _ { 1 1 } } { 2 } ; \pi _ { C 1 4 } = \frac { F _ { 1 4 } } { 2 } \operatorname { a n d } \pi _ { D 1 4 } = \frac { F _ { 1 4 } } { 2 } + \frac { \lambda p _ { 1 4 } } { 2 } ; \pi _ { C 4 1 } = \frac { F _ { 4 1 } } { 2 } + \frac { \lambda p _ { 4 1 } } { 2 } \operatorname { a n d } \pi _ { D 4 1 } = \frac { F _ { 4 1 } } { 2 } ; } \end{array}$ and $\begin{array} { r } { \pi _ { C 4 4 } = \pi _ { D 4 4 } = \frac { F _ { 4 4 } } { 2 } + \frac { \lambda p _ { 4 4 } } { 2 } } \end{array}$ . For outcomes 11, 14, 41, and 44, we have $F _ { 1 1 } = F _ { 1 4 } = F _ { 4 1 } = F _ { 4 4 }$ and equal demand distributions amongst all ISP-CP combinations. Comparing pairs of these outcomes yields $\pi _ { D 1 1 } < \pi _ { D 1 4 } , \pi _ { D 4 1 } < \pi _ { D 4 4 }$ , and $\pi _ { C 1 4 } < \pi _ { C 4 4 }$ . Therefore, outcomes 11, 41, and 14 are dominated and can be eliminated as shown in the following table.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="4">Decisions of Y and G on ISP D</td></tr><tr><td>1: Neither pays D</td><td>2: Y pays D</td><td>3: G pays D</td><td>4: both pay D</td></tr><tr><td rowspan="4">Decisions of Y and G on ISP C</td><td>1: Neither pays C</td><td> $(\pi_{C11}, \pi_{D11})$ </td><td> $(\pi_{C12}, \pi_{D12})$ </td><td> $(\pi_{C13}, \pi_{D13})$ </td><td> $(\pi_{C14}, \pi_{D14})$ </td></tr><tr><td>2: Y pays C</td><td> $(\pi_{C21}, \pi_{D21})$ </td><td> $(\pi_{C22}, \pi_{D22})$ </td><td> $(\pi_{C23}, \pi_{D23})$ </td><td> $(\pi_{C24}, \pi_{D24})$ </td></tr><tr><td>3: G pays C</td><td> $(\pi_{C31}, \pi_{D11})$ </td><td> $(\pi_{C32}, \pi_{D32})$ </td><td> $(\pi_{C33}, \pi_{D33})$ </td><td> $(\pi_{C34}, \pi_{D34})$ </td></tr><tr><td>4: both pay C</td><td> $(\pi_{C41}, \pi_{D41})$ </td><td> $(\pi_{C42}, \pi_{42})$ </td><td> $(\pi_{C43}, \pi_{D43})$ </td><td> $(\pi_{C44}, \pi_{D44})$ </td></tr></table>

Next, we compare outcomes 13, 31, 43, and 34. We know $F _ { 1 3 } = F _ { 3 1 } = F _ { 4 3 } = F _ { 3 4 }$ , and the following demand distributions amongst all ISP-CP combinations: $N _ { C Y 1 3 } = N _ { D Y 3 1 } =$

$N _ { C Y 4 3 } = N _ { D Y 3 4 } , N _ { D Y 1 3 } = N _ { C Y 3 1 } = N _ { D Y 4 3 } = N _ { C Y 3 4 } , N _ { C G 1 3 } = N _ { D G 3 1 } = N _ { C G 4 3 } = N _ { D G 3 4 } .$ and $N _ { D G 1 3 } = N _ { C G 3 1 } = N _ { D G 4 3 } = N _ { C G 3 4 }$ . Recall that $\pi _ { C 1 3 } = ( N _ { C Y 1 3 } + N _ { C G 1 3 } ) F _ { 1 3 } , \pi _ { D 1 3 } =$ $( N _ { D Y 1 3 } + N _ { D G 1 3 } ) F _ { 1 3 } + \lambda p _ { 1 3 } N _ { D G 1 3 } , \pi _ { C 3 1 } = ( N _ { C Y 3 1 } + N _ { C G 3 1 } ) F _ { 3 1 } + \lambda p _ { 3 1 } N _ { C G 3 1 } , \pi _ { D 3 1 } = ( N _ { C Y 3 1 } + N _ { D G 1 3 } ) F _ { 3 1 }$ $( N _ { D Y 3 1 } + N _ { D G 3 1 } ) F _ { 3 1 } , \pi _ { C 4 3 } = ( N _ { C Y 4 3 } + N _ { C G 4 3 } ) ( F _ { 4 3 } + \lambda p _ { 4 3 } ) , \pi _ { D 4 3 } = ( N _ { D Y 4 3 } + N _ { D G 4 3 } ) F _ { 4 3 } + ( N _ { D Y 3 1 } + N _ { D Y 2 2 } )$ $\lambda p _ { 4 3 } N _ { D G 4 3 } , \pi _ { C 3 4 } = ( N _ { C Y 3 4 } + N _ { C G 3 4 } ) F _ { 3 4 } + \lambda p _ { 3 4 } N _ { C G 3 4 }$ , and $\pi _ { D 3 4 } = ( N _ { D Y 3 4 } + N _ { D G 3 4 } ) ( F _ { 3 4 } +$ $\lambda p _ { 3 4 } )$ . Comparing pairs of these outcomes yields $\pi _ { C 1 3 } < \pi _ { C 4 3 }$ and $\pi _ { D 3 1 } < \pi _ { D 3 4 }$ . Therefore, outcomes 13 and 31 are dominated and can be eliminated from the equilibrium analysis as shown in the following table.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="4">Decisions of Y and G on ISP D</td></tr><tr><td>1: Neither pays D</td><td>2: Y pays D</td><td>3: G pays D</td><td>4: both pay D</td></tr><tr><td rowspan="4">Decisions of Y and G on ISP C</td><td>1: Neither pays C</td><td> $(\pi_{C11}, \pi_{D11})$ </td><td> $(\pi_{C12}, \pi_{D12})$ </td><td> $(\pi_{C13}, \pi_{D13})$ </td><td> $(\pi_{C14}, \pi_{D14})$ </td></tr><tr><td>2: Y pays C</td><td> $(\pi_{C21}, \pi_{D21})$ </td><td> $(\pi_{C22}, \pi_{D22})$ </td><td> $(\pi_{C23}, \pi_{D23})$ </td><td> $(\pi_{C24}, \pi_{D24})$ </td></tr><tr><td>3: G pays C</td><td> $(\pi_{C31}, \pi_{D31})$ </td><td> $(\pi_{C32}, \pi_{D32})$ </td><td> $(\pi_{C33}, \pi_{D33})$ </td><td> $(\pi_{C34}, \pi_{D34})$ </td></tr><tr><td>4: both pay C</td><td> $(\pi_{C41}, \pi_{D41})$ </td><td> $(\pi_{C42}, \pi_{42})$ </td><td> $(\pi_{C43}, \pi_{D43})$ </td><td> $(\pi_{C44}, \pi_{D44})$ </td></tr></table>

Therefore, after eliminating all the dominated outcomes, we conclude that outcomes 33, 34, 43, and 44 as the only four possible symmetric equilibria.

C. Proofs of Lemma 1 and Lemma 2 – The Asymmetric Equilibrium Case We derive the possible asymmetric equilibria in the packet discrimination regime by the following steps: in step 1, we characterize consumers demand patterns; in step 2, we derive properties of the equilibrium fixed fees $F _ { C }$ and $F _ { D } ;$ in step 3, we eliminate dominated outcomes and derive the only possible asymmetric equilibria. Without loss of generality, we assume $F _ { C } =$ $F _ { D } + \Delta F$ , where $\Delta F \ge 0$

Step 1: Characterize consumer demand patterns in asymmetric equilibrium Similar to the analysis of symmetric equilibrium, we compare consumers’ utility functions for the corresponding pairs of ISP-CP combinations and derive $\begin{array} { r } { x _ { C i j } = \frac { 1 } { 2 } + \frac { d \lambda \left( \mathbf { w } _ { C G i j } - \mathbf { w } _ { C Y i j } \right) } { 2 t } , x _ { D i j } = } \end{array}$ $\begin{array} { r } { \frac { 1 } { 2 } + \frac { d \lambda \left( \mathbf { w } _ { D G i j } - \mathbf { w } _ { D Y i j } \right) } { 2 t } , z _ { Y i j } = \frac { 1 } { 2 } - \frac { F _ { C } - F _ { D } } { 2 k } + \frac { d \lambda \left( \mathbf { w } _ { D Y i j } - \mathbf { w } _ { C Y i j } \right) } { 2 k } } \end{array}$ , and $\begin{array} { r } { z _ { G i j } = \frac { 1 } { 2 } - \frac { F _ { C } - F _ { D } } { 2 k } + \frac { d \lambda \left( \mathbf { w } _ { D G i j } - \mathbf { w } _ { C G i j } \right) } { 2 k } , } \end{array}$ Note that the sign of $x _ { C i j } - x _ { D i j }$ is the same as the sign of $z _ { Y i j } - z _ { G i j }$

Each outcome <sub>????</sub> is determined by the ISPs’ pricing decisions and the corresponding content providers’ delivery service choices. As in the symmetric case, we denote outcome <sub>????</sub> by the matrix $\left[ \begin{array} { l l } { I _ { D Y i j } } & { I _ { D G i j } } \\ { I _ { C Y i j } } & { I _ { C G i j } } \end{array} \right]$ . When considering asymmetric equilibrium, horizontal flip still applies to permuting the outcomes while vertical flip no longer applies since $F _ { C } \ge F _ { D }$

Among the 16 outcomes, we still have four invariant classes under horizontal flip: (a) outcomes 11, 14, 41, and 44; (b) outcomes 22 and 33; (c) outcomes 23 and 32; (d) outcomes 12, 13, 21, 31, 42, 43, 24, and 34. Next we apply the horizontal flip to each of the classes (a) through (d) to characterize the demand distribution under each outcome.

Under outcomes 11, 14, 41, and 44, all customers have equal queuing priorities. Therefore applying horizontal flip to these outcomes will not change the queuing priorities. Hence the indifferent customers remain unchanged when horizontal flip is applied.

From horizontal flip relations, we have $x _ { C 1 1 } = 1 - x _ { C 1 1 } , x _ { D 1 1 } = 1 - x _ { D 1 1 } , x _ { C 1 4 } = 1 -$ $x _ { C 1 4 } , x _ { D 1 4 } = 1 - x _ { D 1 4 } , x _ { C 4 1 } = 1 - x _ { C 4 1 } , x _ { D 4 1 } = 1 - x _ { D 4 1 } , x _ { C 4 4 } = 1 - x _ { C 4 4 } .$ , and $x _ { D 4 4 } = 1 -$ $x _ { D 4 4 }$ . That is $\begin{array} { r } { x _ { C 1 1 } = x _ { C 1 4 } = x _ { C 4 1 } = x _ { C 4 4 } = \frac { 1 } { 2 } \mathrm { a n d } x _ { D 1 1 } = x _ { D 1 4 } = x _ { D 4 1 } = x _ { D 4 4 } = \frac { 1 } { 2 } . } \end{array}$ . In other words, we know that in these outcomes $\begin{array} { r } { x _ { C } = \frac { 1 } { 2 } = x _ { D } } \end{array}$

Since the sign $x _ { C i j } - x _ { D i j }$ is the same as the sign of $z _ { Y i j } - z _ { G i j }$ for any outcome <sub>????</sub> and $x _ { C } = x _ { D }$ under outcomes 11, 14, 41, and 44, we have $z _ { Y } = z _ { G }$ . Next we prove that $\begin{array} { r } { z _ { Y } = z _ { G } \le \frac { 1 } { 2 } } \end{array}$ by contradiction. First, suppose $\begin{array} { r } { z _ { Y } < \frac { 1 } { 2 } - \frac { F _ { C } - F _ { D } } { 2 k } } \end{array}$ . Then $\begin{array} { r } { z _ { Y } < \frac { 1 } { 2 } } \end{array}$ since $F _ { C } \ge F _ { D }$ . This implies $N _ { D Y } >$ $N _ { C Y }$ which gives $w _ { D Y } > w _ { C Y }$ . But we also have $\begin{array} { r } { z _ { Y } = \frac { 1 } { 2 } - \frac { F _ { C } - F _ { D } } { 2 k } + \frac { d \lambda ( W _ { D Y } - W _ { C Y } ) } { 2 k } } \end{array}$ . Therefore $\scriptstyle { { \frac { 1 } { 2 } } - }$ $\begin{array} { r } { \frac { F _ { C } - F _ { D } } { 2 k } + \frac { d \lambda ( W _ { D Y } - W _ { C Y } ) } { 2 k } < \frac { 1 } { 2 } - \frac { F _ { C } - F _ { D } } { 2 k } } \end{array}$ which gives $w _ { D Y } - w _ { C Y } < 0$ . A contradiction arises. Therefore, we must have $z _ { Y } \ge \frac { 1 } { 2 } - \frac { F c ^ { - } F _ { D } } { 2 k }$ . Second, suppose $\begin{array} { r } { z _ { Y } > \frac { 1 } { 2 } . } \end{array}$ Then $N _ { D Y } < N _ { C Y }$ which gives $w _ { D Y } < w _ { C Y }$ . But we have $F _ { C } \ge F _ { D }$ . Therefore $\begin{array} { r } { z _ { Y } = \frac { 1 } { 2 } + \frac { F _ { D } - F _ { C } } { 2 k } + \frac { d \lambda ( W _ { D Y } - W _ { C Y } ) } { 2 k } < \frac { 1 } { 2 } . ~ \mathrm { A } } \end{array}$ contradiction arises. Therefore we must have $\begin{array} { r } { z _ { Y } \leq \frac { 1 } { 2 } . } \end{array}$

Therefore, as shown in Figure C-a, the market demands for <sub>????</sub> and <sub>????</sub> are equal, and the market demands of <sub>??</sub> and <sub>??</sub> are equal under outcomes 11, 14, 41, and 44. That is $N _ { C Y 1 1 } =$

$$
N _ {C G 1 1} = N _ {C Y 1 4} = N _ {C G 1 4} = N _ {C Y 4 1} = N _ {C G 4 1} = N _ {C Y 4 4} = N _ {C G 4 4} <   \frac {1}{4} \text {and} N _ {D Y 1 1} = N _ {D G 1 1} =
$$

$$
N _ {D Y 1 4} = N _ {D G 1 4} = N _ {D Y 4 1} = N _ {D G 4 1} = N _ {D Y 4 4} = N _ {D G 4 4} > \frac {1}{4}.
$$

![](/api/attachments/95SY3K9J/fulltext/images/197ea17c9abe8a67716a51ba34b114d13b1a68c72c4d3fc060e6237afa25b93d.jpg)  
Figure C-a: Demand Distribution of Class a (outcomes 11, 14, 41, and 44)

## (Class b) Outcomes 22 and 33

Based on symmetry under horizontal flip, we can obtain the demand distribution of 22 by reflecting the demand distribution of outcome 33 through the line $\begin{array} { r } { x = \frac { 1 } { 2 } . } \end{array}$ . Thus we may focus on deriving the demand distribution of outcome 33.

We know from the analysis of symmetric equilibrium that when $F _ { C } = F _ { D } , x _ { D 3 3 } = x _ { C 3 3 } <$ $\frac { 1 } { 2 }$ and $\begin{array} { r } { z _ { G 3 3 } = z _ { Y 3 3 } = \frac { 1 } { 2 } . } \end{array}$ . When $F _ { C } > F _ { D }$ , we know that $\begin{array} { r } { x _ { C 3 3 } = \frac { 1 } { 2 } + \frac { d \lambda ( w _ { C G 3 3 } - w _ { C Y 3 3 } ) } { 2 t } , x _ { D 3 3 } = \frac { 1 } { 2 } + } \end{array}$ $\begin{array} { r } { \frac { d \lambda ( w _ { D G 3 3 } - w _ { D Y 3 3 } ) } { 2 t } , z _ { Y 3 3 } = \frac { 1 } { 2 } - \frac { F _ { C } - F _ { D } } { 2 k } + \frac { d \lambda ( w _ { D Y 3 3 } - w _ { C Y 3 3 } ) } { 2 k } , } \end{array}$ and $\begin{array} { r } { z _ { G 3 3 } = \frac { 1 } { 2 } - \frac { F _ { C } - F _ { D } } { 2 k } + \frac { d \lambda ( w _ { D G 3 3 } - w _ { C G 3 3 } ) } { 2 k } } \end{array}$ Since only pays for preferential delivery on both ISPs, $w _ { C G 3 3 } - w _ { C Y 3 3 } < 0$ , and $w _ { D G 3 3 } -$ $w _ { D Y 3 3 } < 0$ . Thus, $\begin{array} { r } { x _ { C 3 3 } < \frac { 1 } { 2 } \mathrm { a n d } x _ { D 3 3 } < \frac { 1 } { 2 } . } \end{array}$

Furthermore, $\begin{array} { r } { x _ { C 3 3 } - x _ { D 3 3 } = \frac { d \lambda [ ( w _ { D Y 3 3 } - w _ { D G 3 3 } ) - ( w _ { C Y 3 3 } - w _ { C G 3 3 } ) ] } { 2 t } = } \end{array}$

$\begin{array} { r } { \frac { d \lambda } { 2 t } \left[ \frac { N _ { D G 3 3 } \lambda + N _ { D Y 3 3 } \lambda } { ( \mu - N _ { D G 3 3 } \lambda ) ( \mu - N _ { D G 3 3 } \lambda - N _ { D Y 3 3 } \lambda ) } - \frac { N _ { C G 3 3 } \lambda + N _ { C Y 3 3 } \lambda } { ( \mu - N _ { C G 3 3 } \lambda ) ( \mu - N _ { C G 3 3 } \lambda - N _ { C Y 3 3 } \lambda ) } \right] > 0 } \end{array}$ since $N _ { D G 3 3 } > N _ { C G 3 3 }$ and $N _ { D G 3 3 } + N _ { D Y 3 3 } > N _ { C G 3 3 } + N _ { C Y 3 3 }$ . Therefore, we have $\begin{array} { r } { x _ { D 3 3 } < x _ { C 3 3 } < \frac { 1 } { 2 } . } \end{array}$ . Since the sign $x _ { C i j } -$ $x _ { D i j }$ is the same as the sign of $z _ { Y i j } - z _ { G i j }$ for any outcome <sub>????</sub>, we have $z _ { G 3 3 } < z _ { Y 3 3 }$ . Furthermore, we know that $z _ { G 3 3 } < \frac { 1 } { 2 } \mathrm { s i n c e } N _ { D G 3 3 } + N _ { D Y 3 3 } > N _ { C G 3 3 } + N _ { C Y 3 3 }$

Therefore, as shown in Figure C-b, $x _ { D 3 3 } < x _ { C 3 3 } < \frac { 1 } { 2 } , z _ { G 3 3 } < z _ { Y 3 3 }$ , and $\begin{array} { r } { z _ { G 3 3 } < \frac { 1 } { 2 } . } \end{array}$ Based on horizontal flip, we know that $x _ { D 2 2 } = 1 - x _ { D 3 3 } , x _ { C 2 2 } = 1 - x _ { C 3 3 } , z _ { G 2 2 } = z _ { Y 3 3 }$ , and $z _ { Y 2 2 } =$ $z _ { G 3 3 }$ . Therefore, $x _ { D 2 2 } > x _ { C 2 2 } > \frac { 1 } { 2 } , z _ { Y 2 2 } < z _ { G 2 2 }$ , and $\begin{array} { r } { z _ { Y 2 2 } < \frac { 1 } { 2 } . } \end{array}$

![](/api/attachments/95SY3K9J/fulltext/images/0aa46f0fcc49631c285bc6a1f09f7104b94d34f6c91724bf924286b87d1740fe.jpg)

![](/api/attachments/95SY3K9J/fulltext/images/165336641c27a8bd2478fd0c29629c4273d559857736e9610eb1f403acd8368c.jpg)  
Figure C-b: Demand Distribution of Class b (outcomes 22 and 33)

## (Class c) Outcomes 23 and 32

Based on symmetry under horizontal flip, we can obtain the demand distribution of 32 by reflecting the demand distribution of outcome 23 through the line $\begin{array} { r } { x = \frac { 1 } { 2 } . } \end{array}$ . Thus we may focus on deriving the demand distribution of outcome 23.

Under outcome 23, only pays for preferential delivery on <sub>??</sub> and only pays for preferential delivery on <sub>??</sub>. Thus, $w _ { C G 2 3 } - w _ { C Y 2 3 } > 0$ and $w _ { D G 2 3 } - w _ { D Y 2 3 } < 0$ . Therefore we have $\begin{array} { r } { x _ { C 2 3 } > \frac { 1 } { 2 } > x _ { D 2 3 } } \end{array}$ . Since the sign $x _ { C i j } - x _ { D i j }$ is the same as the sign of $z _ { Y i j } - z _ { G i j }$ for any outcome $i j$ , we have $z _ { Y 2 3 } > z _ { G 2 3 }$ . When $F _ { C } > F _ { D }$ , we know that $N _ { D G 2 3 } + N _ { D Y 2 3 } > N _ { C G 2 3 } +$ $N _ { C Y 2 3 }$ . Therefore, we have $\begin{array} { r } { z _ { G 2 3 } < \frac { 1 } { 2 } . } \end{array}$

Therefore, as shown in Figure C-c, $x _ { D 2 3 } < \frac { 1 } { 2 } < x _ { C 2 3 } , z _ { G 2 3 } < z _ { Y 2 3 }$ , and $\begin{array} { r } { z _ { G 2 3 } < \frac { 1 } { 2 } . } \end{array}$ . Based on horizontal flip, we know that $x _ { D 3 2 } = 1 - x _ { D 2 3 } , x _ { C 3 2 } = 1 - x _ { C 2 3 } , z _ { G 3 2 } = z _ { Y 2 3 }$ , and $z _ { Y 3 2 } =$ $z _ { G 2 3 }$ . Therefore, $\begin{array} { r } { x _ { C 3 2 } < \frac { 1 } { 2 } < x _ { D 3 2 } , z _ { Y 3 2 } < z _ { G 3 2 } } \end{array}$ , and $\begin{array} { r } { z _ { Y 3 2 } < \frac { 1 } { 2 } . } \end{array}$

![](/api/attachments/95SY3K9J/fulltext/images/cf162a1020bc4b6a8b4bd5c9b1bf3aa7c1f0f51bc026337aa743c9d5f14b789b.jpg)

![](/api/attachments/95SY3K9J/fulltext/images/cf52ac58f7195563a4aa07babe64d3ef3e79eaa6c6507bc412fbe4cc2a703da3.jpg)  
Figure C-c: Demand Distribution of Class c (outcomes 23 and 32)

## (Class d) Outcomes 12, 13, 21, 31, 42, 43, 24, and 34

The demand analysis for outcomes 42, 43, 24, and 34 is the same as that in outcomes 12, 13, 21, and 31 since both CPs receive the same queuing priority when they both pay for preferential delivery. Based on symmetry under horizontal flip, we can obtain the demand distribution of 12 by reflecting the demand distribution of outcome 13 through the line $\begin{array} { r } { x = \frac { 1 } { 2 } . } \end{array}$ Similarly, we can obtain the demand distribution of 21 by reflecting the demand distribution of outcome 31

through the line $\begin{array} { r } { x = \frac { 1 } { 2 } . } \end{array}$ Thus, we may focus on deriving the demand distribution of outcomes 13 and 31.

In outcome 13, neither CP pays on <sub>??</sub> and only pays on <sub>??</sub>. Thus, $w _ { C G 1 3 } - w _ { C Y 1 3 } = 0$ and $w _ { D G 1 3 } - w _ { D Y 1 3 } < 0$ . Therefore, we have $\begin{array} { r } { x _ { D 1 3 } < x _ { C 1 3 } = \frac { 1 } { 2 } . } \end{array}$ Since the sign $x _ { C i j } - x _ { D i j }$ is the same as the sign of $z _ { Y i j } - z _ { G i j }$ for any outcome $i j ,$ , we have $z _ { G 1 3 } < z _ { Y 1 3 }$ . When $F _ { C } > F _ { D }$ , we know that $N _ { D G 1 3 } + N _ { D Y 1 3 } > N _ { C G 1 3 } + N _ { C Y 1 3 }$ . Therefore, we have $\begin{array} { r } { z _ { G 1 3 } < \frac { 1 } { 2 } . } \end{array}$

Therefore, as shown in Figure $\mathrm { C - d } , x _ { D 1 3 } < x _ { C 1 3 } = { \textstyle { \frac { 1 } { 2 } } } , z _ { G 1 3 } < z _ { Y 1 3 }$ , and $\begin{array} { r } { z _ { G 1 3 } < \frac { 1 } { 2 } . } \end{array}$ Based on horizontal flip, we know that $x _ { D 1 2 } = 1 - x _ { D 1 3 } , x _ { C 1 2 } = 1 - x _ { C 1 3 } , z _ { G 1 2 } = z _ { Y 1 3 }$ , and $z _ { Y 1 2 } =$ $z _ { G 1 3 }$ . Therefore, $x _ { C 1 2 } < x _ { D 1 2 } = \frac { 1 } { 2 } , z _ { Y 1 2 } < z _ { G 1 2 }$ , and $\begin{array} { r } { z _ { Y 1 2 } < \frac { 1 } { 2 } . } \end{array}$

Similarly, in outcome 31, only pays on <sub>??</sub> and neither CP pays on <sub>??</sub>. Thus, $w _ { C G 3 1 } -$ $w _ { C Y 3 1 } < 0$ and $w _ { D G 3 1 } - w _ { D Y 3 1 } = 0$ . Therefore, we have $\begin{array} { r } { x _ { C 3 1 } < x _ { D 3 1 } = \frac { 1 } { 2 } . } \end{array}$ Since the sign $x _ { C i j } -$ $x _ { D i j }$ is the same as the sign of $z _ { Y i j } - z _ { G i j }$ for any outcome $i j ,$ , we have $z _ { Y 3 1 } < z _ { G 3 1 }$ . From the analysis of symmetric equilibria, we know that when $\begin{array} { r } { F _ { C } = F _ { D } , z _ { Y 3 1 } < \frac { 1 } { 2 } . } \end{array}$ Thus, when $F _ { C } > F _ { D }$ have $\begin{array} { r } { z _ { Y 3 1 } < \frac { 1 } { 2 } . } \end{array}$

Therefore, as shown in Figure C-d, $x _ { C 3 1 } < x _ { D 3 1 } = \textstyle { \frac { 1 } { 2 } } , z _ { Y 3 1 } < z _ { G 3 1 }$ , and $\begin{array} { r } { z _ { Y 3 1 } < \frac { 1 } { 2 } . } \end{array}$ Based on horizontal flip, we know that $x _ { D 2 1 } = 1 - x _ { D 3 1 } , x _ { C 2 1 } = 1 - x _ { C 3 1 } , z _ { G 2 1 } = z _ { Y 3 1 }$ , and $z _ { Y 2 1 } =$ $z _ { G 3 1 }$ . Therefore, $\begin{array} { r } { x _ { D 2 1 } = \frac { 1 } { 2 } < x _ { C 2 1 } , z _ { G 2 1 } < z _ { Y 2 1 } } \end{array}$ , and $\begin{array} { r } { z _ { G 2 1 } < \frac { 1 } { 2 } . } \end{array}$

The demand patterns for outcomes 42, 43, 24, and 34 are identical to that for outcomes 12, 13, 21, and 31 respectively.

![](/api/attachments/95SY3K9J/fulltext/images/84d4d22bee4f6577c50398ecc8ba9ea27072fb4946cc1a191b8a0255095ec2f2.jpg)

![](/api/attachments/95SY3K9J/fulltext/images/27796dfed04046c68f749fe6d354f341b0e017185d0b2314331d1bf0eb9fe5be.jpg)

![](/api/attachments/95SY3K9J/fulltext/images/2ba678e3869ca9a3f5337d53868575f7751014b96c1889a51753c06584a756d1.jpg)

![](/api/attachments/95SY3K9J/fulltext/images/d9a9a675db977c5a469ba2674b3923acab40bf153a432ff4bcb85a95a59f4955.jpg)  
Figure C-d: Demand Distribution of Class d (outcomes 12, 13, 21, 31, 42, 43, 24, and 34)

## Step 2: Derive properties of the equilibrium fixed fees $\pmb { F } _ { C }$ and ${ \pmb F } _ { \pmb D }$ in asymmetric equilibrium

As shown in Step 2 in Appendix B, the equilibrium fixed fees $F _ { C }$ and $F _ { D }$ take two different forms: in Case (A) when $x _ { C } \le x _ { D }$ and $z _ { Y } \leq z _ { G }$ , we have $\begin{array} { r } { F _ { C } = V - t \left( 1 - \frac { x _ { C } + x _ { D } } { 2 } \right) - k \left( \frac { z _ { Y } + z _ { G } } { 2 } \right) - } \end{array}$ $d \lambda w _ { C G }$ and $\begin{array} { r } { F _ { D } = V - t { \left( \frac { x _ { C } + x _ { D } } { 2 } \right) } - k \left( 1 - \frac { z _ { Y } + z _ { G } } { 2 } \right) - d \lambda w _ { D Y } } \end{array}$ ; in Case (B) when $x _ { C } \geq x _ { D }$ and $z _ { Y } \ge$ $z _ { G }$ , we have $\begin{array} { r } { F _ { C } = V - t \left( \frac { x _ { C } + x _ { D } } { 2 } \right) - k \left( \frac { z _ { Y } + z _ { G } } { 2 } \right) - d \lambda w _ { C Y } \mathrm { a n d } F _ { D } = V - t \left( 1 - \frac { x _ { C } + x _ { D } } { 2 } \right) - } \end{array}$ $\begin{array} { r } { k \left( 1 - \frac { z _ { Y } + z _ { G } } { 2 } \right) - d \lambda w _ { D G } } \end{array}$ . Among the 16 outcomes, outcomes 11, 14, 41, and 44 are contained in both Case (A) and Case (B); outcomes 12, 42, 31, 34, 22, and 32 are contained in Case (A); outcomes 13, 43, 21, 24, 33, and 23 are contained in Case (B).

Based on the results in step 1, we know the demand patterns and waiting times are related across different outcomes by horizontal flip. Therefore, we can compare the equilibrium fixed fees $F _ { C }$ and $F _ { D }$ for the following groups of outcomes.

## Outcomes 11, 14, 41, and 44

For outcomes 11, 14, 41, and 44, we have $x _ { C 1 1 } = x _ { D 1 1 } = x _ { C 1 4 } = x _ { D 1 4 } = x _ { C 4 1 } = x _ { D 4 1 } = x _ { C 4 4 } =$ $\begin{array} { r } { x _ { D 4 4 } = \frac { 1 } { 2 } \mathrm { { a n d } } z _ { Y 1 1 } = z _ { G 1 1 } = z _ { Y 1 4 } = z _ { G 1 4 } = z _ { Y 4 1 } = z _ { G 4 1 } = z _ { Y 4 4 } = z _ { C 4 4 } < z _ { G 4 4 } < \frac { 1 } { 2 } . } \end{array}$ In addition, we know that $w _ { C G 1 1 } = w _ { C Y 1 1 } = w _ { C G 1 4 } = w _ { C Y 1 4 } = w _ { C G 4 1 } = w _ { C Y 4 1 } = w _ { C G 4 4 } = w _ { C G 4 4 } = w _ { C Y 4 4 } \mathrm { ~ a n d ~ } w _ { D Y 1 1 } = w _ { D Y 1 2 } = w _ { C G 4 4 }$ $w _ { D G 1 1 } = w _ { D Y 1 4 } = w _ { D G 1 4 } = w _ { D Y 4 1 } = w _ { D G 4 1 } = w _ { D Y 4 4 } = w _ { D G 4 4 }$ . Therefore, we know that $F _ { C 1 1 } =$ $F _ { C 1 4 } = F _ { C 4 1 } = F _ { C 4 4 } { \mathrm { ~ a n d ~ } } F _ { D 1 1 } = F _ { D 1 4 } = F _ { D 4 1 } = F _ { D 4 4 }$

## Outcomes 12, 13, 42, and 43

For outcomes 12, 13, 42, and 43, we have $x _ { C 1 2 } = x _ { C 1 3 } = x _ { C 4 2 } = x _ { C 4 3 } = \textstyle { \frac { 1 } { 2 } } , x _ { D 1 2 } = 1 - x _ { D 1 3 } =$ $1 - x _ { D 4 3 } = x _ { D 4 2 } , z _ { Y 1 2 } = z _ { G 1 3 } = z _ { Y 4 2 } = z _ { G 4 3 } ,$ , and $z _ { G 1 2 } = z _ { Y 1 3 } = z _ { G 4 2 } = z _ { Y 4 3 }$ . In addition, we know that $w _ { C G 1 2 } = w _ { C Y 1 3 } = w _ { C G 4 2 } = w _ { C Y 4 3 }$ and $w _ { D Y 1 2 } = w _ { D G 1 3 } = w _ { D Y 4 2 } = w _ { D G 4 3 }$ . Therefore, we know that $F _ { C 1 2 } = F _ { C 1 3 } = F _ { C 4 2 } = F _ { C 4 3 }$ and $F _ { D 1 2 } = F _ { D 1 3 } = F _ { D 4 2 } = F _ { D 4 3 }$

For outcomes 31, 21, 34, and 24, we have $x _ { D 3 1 } = x _ { D 2 1 } = x _ { D 3 4 } = x _ { D 2 4 } = { \textstyle { \frac { 1 } { 2 } } } , x _ { C 3 1 } = 1 - x _ { C 2 1 } =$ $1 - x _ { C 2 4 } = x _ { C 3 4 } , z _ { Y 3 1 } = z _ { G 2 1 } = z _ { Y 3 4 } = z _ { G 2 4 }$ , and $z _ { G 3 1 } = z _ { Y 2 1 } = z _ { G 3 4 } = z _ { Y 2 4 }$ . In addition, we know that $w _ { C G 3 1 } = w _ { C Y 2 1 } = w _ { C G 3 4 } = w _ { C Y 2 4 }$ and $w _ { D Y 3 1 } = w _ { D G 2 1 } = w _ { D Y 3 4 } = w _ { D G 2 4 }$ . Therefore, we know that $F _ { C 3 1 } = F _ { C 2 1 } = F _ { C 3 4 } = F _ { C 2 4 }$ and $F _ { D 3 1 } = F _ { D 2 1 } = F _ { D 3 4 } = F _ { D 2 4 }$

## Outcomes 32 and 23

For outcomes 32 and 23, we have $x _ { C 3 2 } = 1 - x _ { C 2 3 } , x _ { D 3 2 } = 1 - x _ { D 2 3 } , z _ { Y 3 2 } = z _ { G 2 3 }$ , and $z _ { G 3 2 } =$ $z _ { Y 2 3 }$ . In addition, we know that $w _ { C G 3 2 } = w _ { C Y 2 3 }$ and $w _ { D Y 3 2 } = w _ { D G 2 3 }$ . Therefore, we know that $F _ { C 3 2 } = F _ { C 2 3 }$ and $F _ { D 3 2 } = F _ { D 2 3 }$

Step 3: Eliminate dominated and infeasible outcomes in asymmetric equilibrium Next we compare groups of outcomes and eliminate the dominated outcomes from further analysis of asymmetric equilibrium.

## Outcomes 11, 14, and 41 are dominated

In outcome 11, the ISPs’ profit functions are $\pi _ { C 1 1 } = ( N _ { C Y 1 1 } + \ N _ { C G 1 1 } ) F _ { C 1 1 }$ and $\pi _ { D 1 1 } =$ $( N _ { D Y 1 1 } + \ N _ { D G 1 1 } ) F _ { D 1 1 }$ . In outcome 14, the ISPs’ profit functions are $\pi _ { C 1 4 } = ( N _ { C Y 1 4 } +$ $N _ { C G 1 4 } ) F _ { C 1 4 }$ and $\pi _ { D 1 4 } = ( N _ { D Y 1 4 } + \ N _ { D G 1 4 } ) ( F _ { D 1 4 } + \lambda p _ { D 1 4 } )$ . In outcome 41, the ISPs’ profit functions are $\pi _ { C 4 1 } = ( N _ { C Y 4 1 } + \ N _ { C G 4 1 } ) ( F _ { C 4 1 } + \lambda p _ { C 4 1 } )$ and $\pi _ { D 4 1 } = ( N _ { D Y 4 1 } + \ N _ { D G 4 1 } ) F _ { D 4 1 }$ . In outcome 44, the ISPs’ profit functions are $\pi _ { C 4 4 } = ( N _ { C Y 4 4 } + \ N _ { C G 4 4 } ) ( F _ { C 4 4 } + \lambda p _ { C 4 4 } )$ and $\pi _ { D 4 4 } =$ $( N _ { D Y 4 4 } + N _ { D G 4 4 } ) ( F _ { D 4 4 } + \lambda p _ { D 4 4 } )$ . Based on the results in step 1, we know that $N _ { C Y 1 1 } = N _ { C G 1 1 } =$ ?? = ?? = ?? = ?? = ?? = ?? <sup>and</sup> ?? = ?? = ?? = ?? = $N _ { D Y 4 1 } = N _ { D G 4 1 } = N _ { D Y 4 4 } = N _ { D G 4 4 }$ . Based on the results in step 2, we know that $F _ { C 1 1 } = F _ { C 1 4 } =$ $F _ { C 4 1 } = F _ { C 4 4 } { \mathrm { ~ a n d ~ } } F _ { D 1 1 } = F _ { D 1 4 } = F _ { D 4 1 } = F _ { D 4 4 } .$

Comparing pairs of these outcomes yields $\pi _ { D 1 1 } < \pi _ { D 1 4 } , \pi _ { D 4 1 } < \pi _ { D 4 4 }$ , and $\pi _ { C 1 4 } < \pi _ { C 4 4 }$ Therefore, outcomes 11, 41, and 14 are dominated and can be eliminated from further analysis of asymmetric equilibrium.

## Outcome 12 is dominated by outcome 13

The feasible region of $p _ { C 1 2 }$ and $p _ { D 1 2 }$ is determined by the six incentive compatibility constraints: $\pi _ { \gamma _ { 1 2 } } - \pi _ { \gamma _ { 2 2 } } \geq 0 , \pi _ { \gamma _ { 1 2 } } - \pi _ { \gamma _ { 1 1 } } \geq 0 , \pi _ { \gamma _ { 1 2 } } - \pi _ { \gamma _ { 2 1 } } \geq 0 , \pi _ { G 1 2 } - \pi _ { G 3 2 } \geq 0 , \pi _ { G 1 2 } - \pi _ { G 1 4 } \geq 0$ , and $\pi _ { G 1 2 } - \pi _ { G 3 4 } \geq 0$ . These constraints respectively imply $( N _ { C Y 1 2 } + \ N _ { D Y 1 2 } - N _ { C Y 2 2 } - \ N _ { D Y 2 2 } ) r _ { Y } +$ ??<sub>?? 22</sub>??<sub>??12</sub> + (??<sub>?? 22</sub> − ??<sub>?? 12</sub>)??<sub>??12</sub> ≥ 0 <sup>,</sup> �??<sub>?? 12</sub> + ??<sub>?? 12</sub> − <sup>1</sup>� ??<sub>??</sub> − ??<sub>?? 12</sub>??<sub>??12</sub> ≥ 0 <sup>,</sup> (??<sub>?? 12</sub> + ??<sub>??</sub> <sub>12</sub> − ??<sub>??</sub> <sub>21</sub> + ??<sub>??</sub> <sub>21</sub>)??<sub>??</sub> + ??<sub>??</sub> <sub>21</sub>??<sub>??12</sub> − ??<sub>??</sub> <sub>12</sub>??<sub>??12</sub> ≥ 0 <sup>,</sup> �??<sub>??</sub> <sub>12</sub> + ??<sub>??</sub> <sub>12</sub> − <sup>1</sup>� ??<sub>??</sub> + $\begin{array} { r } { N _ { C G 3 2 } p _ { C 1 2 } \ge 0 \ , \ \left( N _ { C G 1 2 } + \ N _ { D G 1 2 } - \frac { 1 } { 2 } \right) r _ { G } + N _ { D G 1 4 } p _ { D 1 2 } \ge 0 } \end{array}$ , and $( N _ { C G 1 2 } + \ N _ { D G 1 2 } - N _ { C Y 3 4 } -$ ?? )?? + ?? ?? + ?? ?? ≥ 0<sup>.</sup>

The feasible region of $p _ { C 1 3 }$ and $p _ { D 1 3 }$ is determined by the six incentive compatibility constraints: $\begin{array} { r } { \pi _ { Y 1 3 } - \pi _ { Y 2 3 } \geq 0 , \pi _ { Y 1 3 } - \pi _ { Y 1 4 } \geq 0 , \pi _ { Y 1 3 } - \pi _ { Y 2 4 } \geq 0 , \pi _ { G 1 3 } - \pi _ { G 3 3 } \geq 0 , \pi _ { G 1 3 } - \pi _ { X 1 3 } - \pi _ { Y 1 3 } . } \end{array}$ $\pi _ { G 1 1 } \geq 0$ , and $\pi _ { G 1 3 } - \pi _ { G 3 1 } \geq 0$ . These constraints respectively imply $\left( N _ { C Y 1 3 } + \ N _ { D Y 1 3 } - { \textstyle \frac { 1 } { 2 } } \right) r _ { Y } +$ $\begin{array} { r } { N _ { C Y 2 3 } p _ { C 1 3 } \ge 0 \quad , \quad \left( N _ { C Y 1 3 } + \ N _ { D Y 1 3 } - \frac { 1 } { 2 } \right) \tau _ { Y } + N _ { D Y 1 4 } p _ { D 1 3 } \ge 0 \quad , \quad ( N _ { C Y 1 3 } + \ N _ { D Y 1 3 } - N _ { C Y 2 4 } - \frac { 1 } { N _ { C Y } } ) \tau _ { Y } . } \end{array}$ ?? )?? + ?? ?? + ?? ?? ≥ 0 (?? + ?? − ?? − ?? )?? +

$$
N _ {C G 3 3} p _ {C 1 3} + (N _ {D G 3 3} - N _ {D G 1 3}) p _ {D 1 3} \geq 0, \left(N _ {C G 1 3} + N _ {D G 1 3} - \frac {1}{2}\right) r _ {G} - N _ {D G 1 3} p _ {D 1 3} \geq 0
$$

$$
(N _ {C G 1 3} + N _ {D G 1 3} - N _ {C G 3 1} - N _ {D G 3 1}) r _ {G} + N _ {C G 3 1} p _ {C 1 3} - N _ {D G 1 3} p _ {D 1 3} \geq 0.
$$

The feasible region of $p _ { C 1 3 }$ and $p _ { D 1 3 }$ contains the feasible region of $p _ { C 1 2 }$ and $p _ { D 1 2 }$ since $r _ { G } \geq r _ { Y }$ and the demand patterns across outcomes are related by horizontal flip. Based on the results in step 2, we know that $F _ { C 1 2 } = F _ { C 1 3 }$ and $F _ { D 1 2 } = F _ { D 1 3 }$ . In outcome 12, the ISPs’ profit functions are $\pi _ { C 1 2 } = ( N _ { C Y 1 2 } + ~ N _ { C G 1 2 } ) F _ { C 1 2 } \mathrm { ~ a n d ~ } \pi _ { D 1 2 } = ( N _ { D Y 1 2 } + ~ N _ { D G 1 2 } ) F _ { D 1 2 } + \lambda N _ { D Y 1 2 } p _ { D 1 2 } .$ In outcome 13, the ISPs’ profit functions are $\pi _ { C 1 3 } = ( N _ { C Y 1 3 } + ~ N _ { C G 1 3 } ) F _ { C 1 3 } \mathrm { ~ a n d ~ } \pi _ { D 1 3 } =$ $( N _ { D Y 1 3 } + N _ { D G 1 3 } ) F _ { D 1 3 } + \lambda N _ { D G 1 3 } p _ { D 1 3 }$ . Therefore, outcome 12 is dominated by outcome 13 since $\pi _ { D 1 2 } \leq \pi _ { D 1 3 }$

## Outcomes 42 is dominated by outcome 43

The feasible region of $p _ { C 4 2 }$ and $p _ { D 4 2 }$ is determined by the six incentive compatibility constraints:

$$
\pi_ {Y 4 2} - \pi_ {Y 3 2} \geq 0, \pi_ {Y 4 2} - \pi_ {Y 4 1} \geq 0, \pi_ {Y 4 2} - \pi_ {Y 3 1} \geq 0, \pi_ {G 4 2} - \pi_ {G 2 2} \geq 0, \pi_ {G 4 2} - \pi_ {G 4 4} \geq 0,
$$

$$
\pi_ {G 4 2} - \pi_ {G 2 4} \geq 0
$$

$$
\left(N _ {C Y 4 2} + N _ {D Y 4 2} - \frac {1}{2}\right) r _ {Y} - N _ {C Y 4 2} p _ {C 4 2} +
$$

$$
(N _ {D Y 3 2} - N _ {D Y 4 2}) p _ {D 4 2} \geq 0, \left(N _ {C Y 4 2} + N _ {D Y 4 2} - \frac {1}{2}\right) r _ {Y} + (N _ {C Y 4 1} - N _ {C Y 4 2}) p _ {C 4 2} - N _ {D Y 4 2} p _ {D 4 2} \geq 0,
$$

$$
(N _ {C Y 4 2} + N _ {D Y 4 2} - N _ {C Y 3 1} - N _ {D Y 3 1}) r _ {Y} - N _ {C Y 4 2} p _ {C 4 2} - N _ {D Y 4 2} p _ {D 4 2} \geq 0, (N _ {C G 4 2} + N _ {D G 4 2} - N _ {D G 4 2})
$$

$$
N _ {C G 2 2} - N _ {D G 2 2}) r _ {G} - N _ {C G 2 4} p _ {C 4 2} \geq 0, \left(N _ {C G 4 2} + N _ {D G 4 2} - \frac {1}{2}\right) r _ {G} + (N _ {C G 4 4} - N _ {C G 4 2}) p _ {C 4 2} +
$$

$$
N _ {D G 4 4} p _ {D 4 2} \geq 0, \mathrm{and} (N _ {C G 4 2} + N _ {D G 4 2} - N _ {C G 2 4} - N _ {D G 2 4}) r _ {G} - N _ {C G 4 2} p _ {C 4 2} + N _ {D G 2 4} p _ {D 4 2} \geq 0.
$$

The feasible region of $p _ { C 4 3 }$ and $p _ { D 4 3 }$ is determined by the six incentive compatibility constraints: $\pi _ { Y 4 3 } - \pi _ { Y 3 3 } \geq 0 , \pi _ { Y 4 3 } - \pi _ { Y 4 4 } \geq 0 , \pi _ { Y 4 3 } - \pi _ { Y 3 4 } \geq 0 , \pi _ { G 4 3 } - \pi _ { G 2 3 } \geq 0 , \pi _ { G 4 3 } - \pi _ { X 3 3 } = 0 . 0 7 .$ $\pi _ { G 4 1 } \geq 0$ , and $\pi _ { G 4 3 } - \pi _ { G 2 1 } \geq 0$ . These constraints respectively imply $( N _ { C Y 4 3 } + \ N _ { D Y 4 3 } -$

$$
N _ {C Y 3 3} - \left. N _ {D Y 3 3}\right) r _ {Y} - N _ {C Y 4 3} p _ {C 4 3} \geq 0, \left(N _ {C Y 4 3} + \left. N _ {D Y 4 3} - \frac {1}{2}\right) r _ {Y} + (N _ {C Y 4 4} - N _ {C Y 4 3}) p _ {C 4 3} + \right.
$$

$$
N _ {D Y 4 4} p _ {D 4 3} \geq 0, (N _ {C Y 4 3} + N _ {D Y 4 3} - N _ {C Y 3 4} - N _ {D Y 3 4}) r _ {Y} - N _ {C Y 4 3} p _ {C 4 3} + N _ {D Y 3 4} p _ {D 4 3} \geq 0,
$$

$$
(N _ {C G 4 3} + N _ {D G 4 3} - N _ {C G 2 3} - N _ {D G 2 3}) r _ {G} - N _ {C G 4 3} p _ {C 4 3} + (N _ {D G 2 3} - N _ {D G 4 3}) p _ {D 4 3} \geq 0,
$$

$$
\left(N _ {C G 4 3} + N _ {D G 4 3} - \frac {1}{2}\right) r _ {G} + (N _ {C G 4 1} - N _ {C G 4 3}) p _ {C 4 3} - N _ {D G 4 3} p _ {D 4 3} \geq 0, \mathrm{and} (N _ {C G 4 3} + N _ {D G 4 3} - N _ {D G 4 3}) p _ {D 4 3}.
$$

$$
N _ {C G 2 1} - \left. N _ {D G 2 1}\right) r _ {G} - N _ {C G 4 3} p _ {C 4 3} - N _ {D G 4 3} p _ {D 4 3} \geq 0.
$$

The feasible region of $p _ { C 4 3 }$ and $p _ { D 4 3 }$ contains the feasible region of $p _ { C 4 2 }$ and $p _ { D 4 2 }$ since $r _ { G } \geq r _ { Y }$ and the demand patterns across outcomes are related by horizontal flip. Based on the results in step 2, we know that $F _ { C 4 2 } = F _ { C 4 3 }$ and $F _ { D 4 2 } = F _ { D 4 3 }$ . In outcome 42, the ISPs’ profit functions are $\pi _ { C 4 2 } = ( N _ { C Y 4 2 } + \ N _ { C G 4 2 } ) ( F _ { C 4 2 } + \lambda p _ { C 4 2 } )$ and $\pi _ { D 4 2 } = ( N _ { D Y 4 2 } + \ N _ { D G 4 2 } ) F _ { D 4 2 } +$ $\lambda N _ { D Y 4 2 } p _ { D 4 2 }$ . In outcome 43, the ISPs’ profit functions are $\pi _ { C 4 3 } = ( N _ { C Y 4 3 } + \ N _ { C G 4 3 } ) ( F _ { C 4 3 } +$ $\lambda p _ { C 4 3 } )$ and $\pi _ { D 4 3 } = ( N _ { D Y 4 3 } + N _ { D G 4 3 } ) F _ { D 4 3 } + \lambda N _ { D G 4 3 } p _ { D 4 3 }$ . Therefore, outcome 42 is dominated by outcome 43 since $\pi _ { D 4 2 } \leq \pi _ { D 4 3 }$

## Outcomes 13 is dominated by outcome 43

In outcome 13, the ISPs’ profit functions are $\pi _ { C 1 3 } = ( N _ { C Y 1 3 } + \ N _ { C G 1 3 } ) F _ { C 1 3 }$ and $\pi _ { D 1 3 } =$ $( N _ { D Y 1 3 } + N _ { D G 1 3 } ) F _ { D 1 3 } + \lambda N _ { D G 1 3 } p _ { D 1 3 }$ . In outcome 43, the ISPs’ profit functions are $\pi _ { C 4 3 } =$ $( N _ { C Y 4 3 } + \ N _ { C G 4 3 } ) ( F _ { C 4 3 } + \lambda p _ { C 4 3 } )$ and $\pi _ { D 4 3 } = ( N _ { D Y 4 3 } + N _ { D G 4 3 } ) F _ { D 4 3 } + \lambda N _ { D G 4 3 } p _ { D 4 3 }$ . Based on the results in step 1, we know that $N _ { C Y 1 3 } = N _ { C Y 4 3 }$ and $N _ { C G 1 3 } = N _ { C G 4 3 }$ . Based on the results in step 2, we know that $F _ { C 1 3 } = F _ { C 4 3 }$ . Therefore, outcome 13 is dominated by outcome 43 since $\pi _ { C 1 3 } \leq \pi _ { C 4 3 }$

The feasible region of $p _ { C 2 1 }$ and $p _ { D 2 1 }$ is determined by the six incentive compatibility constraints:

$$
\pi_ {Y 2 1} - \pi_ {Y 1 1} \geq 0, \pi_ {Y 2 1} - \pi_ {Y 2 2} \geq 0, \pi_ {Y 2 1} - \pi_ {Y 1 2} \geq 0, \pi_ {G 2 1} - \pi_ {G 4 1} \geq 0, \pi_ {G 2 1} - \pi_ {G 2 3} \geq 0, \mathrm{and}
$$

$\pi _ { G 2 1 } - \pi _ { G 4 3 } \geq 0$ . These constraints respectively imply $\left( N _ { C Y 2 1 } + \ N _ { D Y 2 1 } - { \textstyle { \frac { 1 } { 2 } } } \right) r _ { Y } - N _ { C Y 2 1 } p _ { C 2 1 } \ge$

$$
0, (N _ {C Y 2 1} + N _ {D Y 2 1} - N _ {C Y 2 2} - N _ {D Y 2 2}) r _ {Y} + (N _ {C Y 2 2} - N _ {C Y 2 1}) p _ {C 2 1} + N _ {D Y 2 2} p _ {D 2 1} \geq 0,
$$

$$
(N _ {C Y 2 1} + N _ {D Y 2 1} - N _ {C Y 1 2} - N _ {D Y 1 2}) r _ {Y} - N _ {C Y 2 1} p _ {C 2 1} + N _ {D Y 1 2} p _ {D 2 1} \geq 0, (N _ {C G 2 1} + N _ {D G 2 1} - N _ {D G 1 2}) r _ {Y},
$$

$$
\left. \frac {1}{2}\right) r _ {G} + N _ {C G 4 1} p _ {C 2 1} \geq 0, (N _ {C G 2 1} + N _ {D G 2 1} - N _ {C G 2 3} - N _ {D G 2 3}) r _ {G} + N _ {D G 2 3} p _ {D 2 1} \geq 0, \mathrm{and}
$$

$$
(N _ {C G 2 1} + N _ {D G 2 1} - N _ {C G 4 3} - N _ {D G 4 3}) r _ {G} + N _ {C G 4 3} p _ {C 2 1} + N _ {D G 4 3} p _ {D 2 1} \geq 0.
$$

The feasible region of $p _ { C 3 1 }$ and $p _ { D 3 1 }$ is determined by the six incentive compatibility

$$
\text { constraints: } \pi_ {Y 3 1} - \pi_ {Y 4 1} \geq 0, \pi_ {Y 3 1} - \pi_ {Y 3 2} \geq 0, \pi_ {Y 3 1} - \pi_ {Y 4 2} \geq 0, \pi_ {G 3 1} - \pi_ {G 1 1} \geq 0, \pi_ {G 3 1} -
$$

$\pi _ { G 3 3 } \geq 0$ , and $\pi _ { G 3 1 } - \pi _ { G 1 3 } \geq 0$ . These constraints respectively imply $\left( N _ { C Y 3 1 } + \ N _ { D Y 3 1 } - \right.$

$$
\frac {1}{2} \Big) r _ {Y} + N _ {C Y 4 1} p _ {C 3 1} \geq 0, (N _ {C Y 3 1} + N _ {D Y 3 1} - N _ {C Y 3 2} - N _ {D Y 3 2}) r _ {Y} + N _ {D Y 3 2} p _ {D 3 1} \geq 0,
$$

$$
(N _ {C Y 3 1} + N _ {D Y 3 1} - N _ {C Y 4 2} - N _ {D Y 4 2}) r _ {Y} + N _ {C Y 4 2} p _ {C 3 1} + N _ {D Y 4 2} p _ {D 3 1} \geq 0, (N _ {C G 3 1} + N _ {D G 3 1} - N _ {D G 3 1}) r _ {Y},
$$

$$
\left. \frac {1}{2}\right) r _ {G} - N _ {C G 3 1} p _ {C 3 1} \geq 0, (N _ {C G 3 1} + N _ {D G 3 1} - N _ {C G 3 3} - N _ {D G 3 3}) r _ {G} + (N _ {C G 3 3} - N _ {C G 3 1}) p _ {C 3 1} +
$$

$$
N _ {D G 3 3} p _ {D 3 1} \geq 0, \mathrm{and} (N _ {C G 3 1} + N _ {D G 3 1} - N _ {C G 1 3} - N _ {D G 1 3}) r _ {G} - N _ {C G 3 1} p _ {C 3 1} + N _ {D G 1 3} p _ {D 3 1} \geq 0.
$$

The feasible region of $p _ { C 3 1 }$ and $p _ { D 3 1 }$ contains the feasible region of $p _ { C 2 1 }$ and $p _ { D 2 1 }$ since $r _ { G } \ge r _ { Y }$ and the demand patterns across outcomes are related by horizontal flip. Based on the results in step 2, we know that $F _ { C 3 1 } = F _ { C 2 1 }$ and $F _ { D 3 1 } = F _ { D 2 1 }$ . In outcome 31, the ISPs’ profit functions are $\pi _ { C 3 1 } = ( N _ { C Y 3 1 } + ~ N _ { C G 3 1 } ) F _ { C 3 1 } + \lambda N _ { C G 3 1 } p _ { C 3 1 }$ and $\pi _ { D 3 1 } = ( N _ { D Y 3 1 } + \ N _ { D G 3 1 } ) F _ { D 3 1 }$ . In outcome 21, the ISPs’ profit functions are $\pi _ { C 2 1 } = ( N _ { C Y 2 1 } + \ N _ { C G 2 1 } ) F _ { C 2 1 } + \lambda N _ { C Y 2 1 } p _ { C 2 1 }$ and

$\pi _ { D 2 1 } = ( N _ { D Y 2 1 } + \ N _ { D G 2 1 } ) F _ { D 2 1 }$ . Therefore, outcome 21 is dominated by outcome 31 since $\pi _ { C 2 1 } \leq$ ??<sub>??31</sub><sup>.</sup>

Outcomes 24 is dominated by outcome 34

The feasible region of $p _ { C 2 4 }$ and $p _ { D 2 4 }$ is determined by the six incentive compatibility constraints:

$$
\pi_ {Y 2 4} - \pi_ {Y 1 4} \geq 0, \pi_ {Y 2 4} - \pi_ {Y 2 3} \geq 0, \pi_ {Y 2 4} - \pi_ {Y 1 3} \geq 0, \pi_ {G 2 4} - \pi_ {G 4 4} \geq 0, \pi_ {G 2 4} - \pi_ {G 2 2} \geq 0,
$$

$\pi _ { G 2 4 } - \pi _ { G 4 2 } \geq 0$ . These constraints respectively imply $\left( N _ { C Y 2 4 } + \ N _ { D Y 2 4 } - { \textstyle { \frac { 1 } { 2 } } } \right) r _ { Y } - N _ { C Y 2 4 } p _ { C 2 4 } +$

$$
(N _ {D Y 1 4} - N _ {D Y 2 4}) p _ {D 2 4} \geq 0, \left(N _ {C Y 2 4} + N _ {D Y 2 4} - \frac {1}{2}\right) r _ {Y} + (N _ {C Y 2 3} - N _ {C Y 2 4}) p _ {C 2 4} - N _ {D Y 2 4} p _ {D 2 4} \geq 0,
$$

$$
(N _ {C Y 2 4} + N _ {D Y 2 4} - N _ {C Y 1 3} - N _ {D Y 1 3}) r _ {Y} - N _ {C Y 2 4} p _ {C 2 4} - N _ {D Y 2 4} p _ {D 2 4} \geq 0, (N _ {C G 2 4} + N _ {D G 2 4} - N _ {D G 2 4}) r _ {Y},
$$

$$
\left. \frac {1}{2}\right) r _ {G} + N _ {C G 4 4} p _ {C 2 4} + (N _ {D G 4 4} - N _ {D G 2 4}) p _ {D 2 4} \geq 0, (N _ {C G 2 4} + N _ {D G 2 4} - N _ {C G 2 2} - N _ {D G 2 2}) r _ {G} -
$$

$$
N _ {D G 2 4} p _ {D 2 4} \geq 0, \mathrm{and} (N _ {C G 2 4} + N _ {D G 2 4} - N _ {C G 4 2} - N _ {D G 4 2}) r _ {G} + N _ {C G 4 2} p _ {C 2 4} - N _ {D G 2 4} p _ {D 2 4} \geq 0.
$$

The feasible region of $p _ { C 3 4 }$ and $p _ { D 3 4 }$ is determined by the six incentive compatibility

constraints: $\pi _ { Y 3 4 } - \pi _ { Y 4 4 } \geq 0 , \pi _ { Y 3 4 } - \pi _ { Y 3 3 } \geq 0 , \pi _ { Y 3 4 } - \pi _ { Y 4 3 } \geq 0 , \pi _ { G 3 4 } - \pi _ { G 1 4 } \geq 0 , \pi _ { G 3 4 } - \pi _ { X 3 3 } > 0 .$

$\pi _ { G 3 2 } \geq 0$ , and $\pi _ { G 3 4 } - \pi _ { G 1 2 } \geq 0$ . These constraints respectively imply $\left( N _ { C Y 3 4 } + \ N _ { D Y 3 4 } - \right.$

$$
\left. \frac {1}{2}\right) r _ {Y} + N _ {C Y 4 4} p _ {C 3 4} + (N _ {D Y 4 4} - N _ {D Y 3 4}) p _ {D 3 4} \geq 0, (N _ {C Y 3 4} + N _ {D Y 3 4} - N _ {C Y 3 3} - N _ {D Y 3 3}) r _ {Y} -
$$

$$
N _ {D Y 3 4} p _ {D 3 4} \geq 0, (N _ {C Y 3 4} + N _ {D Y 3 4} - N _ {C Y 4 3} - N _ {D Y 4 3}) r _ {Y} + N _ {C Y 4 3} p _ {C 3 4} - N _ {D Y 3 4} p _ {D 3 4} \geq 0,
$$

$$
\left(N _ {C G 3 4} + N _ {D G 3 4} - \frac {1}{2}\right) r _ {G} - N _ {C G 3 4} p _ {C 3 4} + (N _ {D G 1 4} - N _ {D G 3 4}) p _ {D 3 4} \geq 0, \left(N _ {C G 3 4} + N _ {D G 3 4} - \frac {1}{2}\right) r _ {G} +
$$

$$
(N _ {C G 3 2} - N _ {C G 3 4}) p _ {C 3 4} - N _ {D G 3 4} p _ {D 3 4} \geq 0, \mathrm{and} (N _ {C G 3 4} + N _ {D G 3 4} - N _ {C G 1 2} - N _ {D G 1 2}) r _ {G} -
$$

$$
N _ {C G 3 4} p _ {C 3 4} - N _ {D G 3 4} p _ {D 3 4} \geq 0.
$$

The feasible region of $p _ { C 3 4 }$ and $p _ { D 3 4 }$ contains the feasible region of $p _ { C 2 4 }$ and $p _ { D 2 4 }$ since $r _ { G } \ge r _ { Y }$ and the demand patterns across outcomes are related by horizontal flip. Based on the

results in step 2, we know that $F _ { C 3 4 } = F _ { C 2 4 }$ and $F _ { D 3 4 } = F _ { D 2 4 }$ . In outcome 24, the ISPs’ profit functions are $\pi _ { C 2 4 } = ( N _ { C Y 2 4 } + \ N _ { C G 2 4 } ) F _ { C 2 4 } + \lambda N _ { C Y 2 4 } p _ { C 2 4 } \mathrm { a n d } \ \pi _ { D 2 4 } = ( N _ { D Y 2 4 } +$ $N _ { D G 2 4 } ) ( F _ { D 2 4 } + \lambda p _ { C 2 4 } )$ . In outcome 34, the ISPs’ profit functions are $\pi _ { C 3 4 } = ( N _ { C Y 3 4 } +$ $N _ { C G 3 4 } ) F _ { C 3 4 } + \lambda N _ { C G 3 4 } p _ { C 3 4 }$ and $\pi _ { D 3 4 } = ( N _ { D Y 3 4 } + \ N _ { D G 3 4 } ) ( F _ { D 3 4 } + \lambda p _ { C 3 4 } )$ . Therefore, outcome 24 is dominated by outcome 34 since $\pi _ { C 2 4 } \leq \pi _ { C 3 4 }$

## Outcomes 31 is dominated by outcome 34

In outcome 31, the ISPs’ profit functions are $\pi _ { C 3 1 } = ( N _ { C Y 3 1 } + ~ N _ { C G 3 1 } ) F _ { C 3 1 } + \lambda N _ { C G 3 1 } p _ { C 3 1 }$ and $\pi _ { D 3 1 } = ( N _ { D Y 3 1 } + \ N _ { D G 3 1 } ) F _ { D 3 1 }$ . In outcome 34, the ISPs’ profit functions are $\pi _ { C 3 4 } =$ $( N _ { C Y 3 4 } + N _ { C G 3 4 } ) F _ { C 3 4 } + \lambda N _ { C G 3 4 } p _ { C 3 4 }$ and $\pi _ { D 3 4 } = ( N _ { D Y 3 4 } + \ N _ { D G 3 4 } ) ( F _ { D 3 4 } + \lambda p _ { C 3 4 } )$ . Based on the results in step 1, we know that $N _ { D Y 3 1 } = N _ { D Y 3 4 }$ and $N _ { D G 3 1 } = N _ { D G 3 4 }$ . Based on the results in step 2, we know that $F _ { D 3 1 } = F _ { D 3 4 }$ . Therefore, outcome 31 is dominated by outcome 34 since $\pi _ { D 3 1 } \leq \pi _ { D 3 4 }$

## Outcomes 32 and 23 are infeasible

Here we focus on showing that there is no feasible <sub>??</sub> for outcome 23, as the analysis for outcome 32 is similar. For outcomes 23 to be feasible, all the CPs’ incentive compatibility constraints need to be satisfied: <sub>(1)</sub> $\pi _ { Y 2 3 } - \pi _ { Y 1 3 } \geq 0 ; ( 2 ) \pi _ { Y 2 3 } - \pi _ { Y 2 4 } \geq 0 ; ( 3 ) \pi _ { Y 2 3 } - \pi _ { Y 1 4 } \geq 0 ; ( 4 ) \pi _ { G 2 3 } -$ $\pi _ { G 4 3 } \geq 0 ; \left( 5 \right) \pi _ { G 2 3 } - \pi _ { G 2 1 } \geq 0 ; \left( 6 \right) \pi _ { G 2 3 } - \pi _ { G 4 1 } \geq 0 .$

Inequality (3) is $( N _ { C Y 2 3 } + N _ { D Y 2 3 } - N _ { C Y 1 4 } - N _ { D Y 1 4 } ) r _ { Y } + N _ { D Y 1 4 } p _ { D } - N _ { C Y 2 3 } p _ { C } \ge 0 .$ Since $\begin{array} { r } { N _ { C Y 1 4 } + \ N _ { D Y 1 4 } = \frac { 1 } { 2 } ; } \end{array}$ , inequality (3) can be reduced to $\begin{array} { r } { p _ { D } \ge \left( \frac { N _ { C Y 2 3 } } { N _ { D Y 1 4 } } \right) p _ { C } + } \end{array}$ $\left( \frac { \frac { 1 } { 2 } - N _ { C Y 2 3 } - N _ { D Y 2 3 } } { N _ { D Y 1 4 } } \right) r _ { Y } .$

Inequality (6) is $( N _ { C G 2 3 } + \ N _ { D G 2 3 } - N _ { C G 4 1 } - N _ { D G 4 1 } ) r _ { G } + N _ { C G 4 1 } p _ { C } - N _ { D G 2 3 } p _ { D } \ \geq \ 0 .$ Since $\begin{array} { r } { N _ { C G 4 1 } + N _ { D G 4 1 } = \frac { 1 } { 2 } ; } \end{array}$ inequality (6) can be reduced to $\begin{array} { r } { p _ { D } \leq \left( \frac { N _ { C G 4 1 } } { N _ { D G 2 3 } } \right) p _ { C } + } \end{array}$

$$
\left(\frac {\frac {1}{2} - N _ {C G 2 3} - N _ {D G 2 3}}{N _ {D G 2 3}}\right) r _ {G}.
$$

Based on the result in step 1, we have ${ \textstyle \frac { 1 } { 2 } } - N _ { C Y 2 3 } - N _ { D Y 2 3 } = N _ { C G 2 3 } + N _ { D G 2 3 } - { \textstyle \frac { 1 } { 2 } } > 0$ This $\begin{array} { r } { \mathrm { g i v e s } \left( \frac { \frac { 1 } { 2 } - N _ { C Y 2 3 } - N _ { D Y 2 3 } } { N _ { D Y 1 4 } } \right) r _ { Y } > 0 } \end{array}$ and $\left( \frac { \frac { 1 } { 2 } - N _ { C G 2 3 } - N _ { D G 2 3 } } { N _ { D G 2 3 } } \right) r _ { G } < 0$ . Next we show that $\begin{array} { r } { \frac { N _ { C Y 2 3 } } { N _ { D Y 1 4 } } > } \end{array}$ $\frac { N _ { C G 4 1 } } { N _ { D G 2 3 } }$ . We first note that $N _ { D Y 1 4 } = N _ { D G 1 1 }$ and $N _ { C G 4 1 } = N _ { C Y 1 1 }$ . Thus, $\begin{array} { r } { \frac { N _ { C Y 2 3 } } { N _ { D Y 1 4 } } > \frac { N _ { C G 4 1 } } { N _ { D G 2 3 } } \Longleftrightarrow \frac { N _ { C Y 2 3 } } { N _ { D G 1 1 } } > } \end{array}$ $\begin{array} { r } { \frac { N _ { C Y 1 1 } } { N _ { D G 2 3 } } \iff \frac { N _ { C Y 2 3 } } { N _ { C Y 1 1 } } > \frac { N _ { D G 1 1 } } { N _ { D G 2 3 } } . } \end{array}$

Since $N _ { C Y 2 3 } > N _ { C Y 1 1 }$ and $N _ { D G 2 3 } > N _ { D G 1 1 }$ , we have $\begin{array} { r } { \frac { N _ { C Y 2 3 } } { N _ { C Y 1 1 } } > 1 > \frac { N _ { D G 1 1 } } { N _ { D G 2 3 } } } \end{array}$ . Thus, we also have $\begin{array} { r } { \frac { N _ { C Y 2 3 } } { N _ { D Y 1 4 } } > \frac { N _ { C G 4 1 } } { N _ { D G 2 3 } } } \end{array}$ . Then (3) and (6) implies that $p _ { C }$ and $p _ { D }$ are both negative. Therefore, outcome 23 is infeasible.

Similarly, we can show that there is no feasible for outcome 32. Therefore, both outcomes 23 and 32 are infeasible.

For outcomes 22 to be feasible, all the $\mathrm { C P s ^ { \prime } }$ incentive compatibility constraints need to be satisfied:

$$
) \pi_ {Y 2 2} - \pi_ {Y 1 3} \geq 0; (2) \pi_ {Y 2 2} - \pi_ {Y 3 1} \geq 0; (3) \pi_ {Y 2 2} - \pi_ {Y 1 1} \geq 0; (4) \pi_ {G 2 2} - \pi_ {G 4 2} \geq 0;
$$

$$
(5) \pi_ {G 2 2} - \pi_ {G 2 4} \geq 0; (6) \pi_ {G 2 2} - \pi_ {G 4 4} \geq 0.
$$

Inequality (3) is $( N _ { C Y 2 2 } + N _ { D Y 2 2 } - N _ { C Y 1 1 } - N _ { D Y 1 1 } ) r _ { Y } - N _ { C Y 2 2 } p _ { C } - N _ { D Y 2 2 } p _ { D } \ge 0$ . Since $\begin{array} { r } { N _ { C Y 1 1 } + \ N _ { D Y 1 1 } = \frac { 1 } { 2 } } \end{array}$ , inequality (3) can be reduced to $\begin{array} { r } { \left( N _ { C Y 2 2 } + N _ { D Y 2 2 } - \frac { 1 } { 2 } \right) r _ { Y } \ge N _ { C Y 2 2 } p _ { C } + } \end{array}$ $N _ { D Y 2 2 } p _ { D }$

Inequality (6) is $( N _ { C G 2 2 } + N _ { D G 2 2 } - N _ { C G 4 4 } - N _ { D G 4 4 } ) r _ { G } + N _ { C G 4 4 } p _ { C } + N _ { D G 4 4 } p _ { D } \ge 0$ Since $\begin{array} { r } { N _ { C G 4 4 } + \ N _ { D G 4 4 } = \frac { 1 } { 2 } ; } \end{array}$ , inequality (6) can be reduced to $\begin{array} { r } { N _ { C G 4 4 } p _ { C } + N _ { D G 4 4 } p _ { D } \ \geq \left( \frac { 1 } { 2 } - N _ { C G 2 2 } - \right. } \end{array}$ $N _ { D G 2 2 } ) r _ { G }$

Based on the result in step 1, we have $N _ { C Y 1 1 } = N _ { C G 4 4 } , N _ { D Y 1 1 } = N _ { D G 4 4 }$ and

$\left( { \textstyle { \frac { 1 } { 2 } } } - N _ { C G 2 2 } - N _ { D G 2 2 } \right) = \left( N _ { C Y 2 2 } + N _ { D Y 2 2 } - { \textstyle { \frac { 1 } { 2 } } } \right)$ . We also know that $r _ { G } \ge r _ { Y }$ . Thus, $N _ { C Y 1 1 } p _ { C } +$ $N _ { D Y 1 1 } p _ { D } = N _ { C G 4 4 } p _ { C } + N _ { D G 4 4 } p _ { D } \ge N _ { C Y 2 2 } p _ { C } + N _ { D Y 2 2 } p _ { D }$ , which implies $( N _ { C Y 2 2 } - N _ { C Y 1 1 } ) p _ { C } +$ $( N _ { D Y 2 2 } - N _ { D Y 1 1 } ) p _ { D } \leq 0 .$

Since <sub>??</sub> pays for priority delivery on both <sub>??</sub> and <sub>??</sub>, we know that $N _ { C Y 2 2 } > N _ { C Y 1 1 }$ and $N _ { D Y 2 2 } > N _ { D Y 1 1 } , \mathrm { i . e . , } \left( N _ { C Y 2 2 } - N _ { C Y 1 1 } \right) > 0$ and $( N _ { D Y 2 2 } - N _ { D Y 1 1 } ) > 0$ . Thus, (3) and (6) imply that either $p _ { C }$ or $p _ { D }$ is negative. Therefore, outcome 22 is infeasible.

Therefore, after eliminating all the dominated and infeasible outcomes, we conclude that outcomes 33, 34, 43, and 44 as the only four possible asymmetric equilibria.

## D. Proof of Lemma 3

From Lemma 2, we know that outcomes 33, 34, 43, and 44 as the only four possible equilibria. Here we conduct symmetric equilibrium analysis $( F _ { C } = F _ { D } = F$ and $p _ { C } = p _ { D } = p )$ and derive the ISPs’ equilibrium pricing strategies and the corresponding equilibrium outcomes in the packet discrimination regime in the following two steps.

## Step 1: Solve for the equilibrium fixed fee <sub>??</sub> and preferential delivery fee <sub>??</sub> for the candidate outcomes

In step 1, we solve for the equilibrium fixed fee <sub>??</sub> and preferential delivery fee <sub>??</sub> for the candidate outcomes one by one. Among the four candidate equilibria, outcome 43 and outcome 34 are symmetric. Thus, we focus on outcomes 44, 43, and 33 in this analysis.

## Outcome 44

The preferential delivery fee <sub>??</sub> for outcome 44 is determined by the following two CPs’ incentive compatibility constraints: $\pi _ { Y 4 4 } \geq \pi _ { Y 4 3 }$ yields $\begin{array} { r } { p _ { 4 4 } \le \frac { ( 1 / 2 - N _ { D Y 4 3 } - N _ { C Y 4 3 } ) r _ { Y } } { 1 / 2 - N _ { C Y 4 3 } } ; \pi _ { Y 4 4 } \ge \pi _ { Y 3 3 } } \end{array}$ yields $\begin{array} { r } { p _ { 4 4 } \le \frac { ( 1 / 2 - N _ { C Y 3 3 } - N _ { D Y 3 3 } ) r _ { Y } } { 1 / 2 } } \end{array}$ . Therefore, $p _ { 4 4 } ^ { * } = H _ { 4 4 } r _ { Y }$ , where $H _ { 4 4 } =$ min $\left\{ \frac { 1 / 2 - N _ { D Y 4 3 } - N _ { C Y 4 3 } } { 1 / 2 - N _ { C Y 4 3 } } , \frac { 1 / 2 - N _ { C Y 3 3 } - N _ { D Y 3 3 } } { 1 / 2 } \right\}$ . In addition, we know from the results in Lemma 2 that $\begin{array} { r } { F _ { 4 4 } ^ { * } = V - \frac { t } { 2 } - \frac { k } { 2 } - \frac { d \lambda } { \mu - \lambda / 2 } . } \end{array}$

## Outcome 43

The preferential delivery fee <sub>??</sub> for outcome 43 is determined by the following three CPs’ incentive compatibility constraints: $\pi _ { Y 4 3 } \geq \pi _ { Y 3 3 }$ yields $\begin{array} { r } { p _ { 4 3 } \leq \frac { ( N _ { C Y 4 3 } + N _ { D Y 4 3 } - N _ { C Y 3 3 } - N _ { D Y 3 3 } ) r _ { Y } } { N _ { C Y 4 3 } } ; \ \pi _ { Y 4 3 } \geq \pi _ { Y 4 4 } } \end{array}$ yields $\begin{array} { r } { p _ { 4 3 } \ge \frac { ( 1 / 2 - N _ { C Y 4 3 } - N _ { D Y 4 3 } ) r _ { Y } } { 1 / 2 - N _ { C Y 4 3 } } ; \pi _ { G 4 3 } \ge \pi _ { G 4 1 } \mathrm { ~ y i e l d s ~ } p _ { 4 3 } \le \frac { ( N _ { C G 4 3 } + N _ { D G 4 3 } - 1 / 2 ) r _ { G } } { N _ { C G 4 3 } + N _ { D G 4 3 } - 1 / 4 } } \end{array}$ . Thus, there exists a feasible <sub>??</sub> if and only if (1⁄2−?? −?? )?? 1⁄2− ?? min $\left\{ \frac { ( N _ { C Y 4 3 } + N _ { D Y 4 3 } - N _ { C Y 3 3 } - N _ { D Y 3 3 } ) r _ { Y } } { N _ { C Y 4 3 } } , \frac { ( N _ { C G 4 3 } + N _ { D G 4 3 } - 1 / 2 ) r _ { G } } { N _ { C G 4 3 } + N _ { D G 4 3 } - 1 / 4 } \right\}$ , which can be reduced to $r _ { G } \geq $ (??<sub>????43</sub>+??<sub>?? 43</sub>−1⁄4)?? and 1⁄2−??<sub>????43</sub>−??<sub>??</sub> <sub>43</sub> <sup>??????43+????</sup> <sup>43−??????33−????</sup> <sup>33</sup> When these feasible 1⁄2− ??<sub>????43</sub> 1⁄2− ??<sub>????43</sub> ??<sub>????43</sub> conditions hold, we obtain $p _ { 4 3 } ^ { * } = \operatorname* { m i n } \{ H _ { Y 4 3 } r _ { Y } , H _ { G 4 3 } r _ { G } \}$ , where $\begin{array} { r } { H _ { Y 4 3 } = \frac { N _ { C Y 4 3 } + N _ { D Y 4 3 } - N _ { C Y 3 3 } - N _ { D Y 3 3 } } { N _ { C Y 4 3 } } } \end{array}$ and $\begin{array} { r } { H _ { G 4 3 } = \frac { N _ { C G 4 3 } + N _ { D G 4 3 } - 1 / 2 } { N _ { C G 4 3 } + N _ { D G 4 3 } - 1 / 4 } . } \end{array}$

We know that in a symmetric equilibrium, $\pi _ { C 4 3 } = \pi _ { D 4 3 } , \ \mathrm { i . e . , } \ ( N _ { D Y 4 3 } + N _ { D G 4 3 } ) F _ { 4 3 } +$ $\lambda p _ { 4 3 } N _ { D G 4 3 } = ( N _ { C Y 4 3 } + N _ { C G 4 3 } ) ( F _ { 4 3 } + \lambda p _ { 4 3 } )$ . Thus, $\begin{array} { r } { F _ { 4 3 } ^ { * } = \frac { ( N _ { C Y 4 3 } + N _ { C G 4 3 } - N _ { D G 4 3 } ) \lambda p _ { 4 3 } ^ { * } } { N _ { D Y 4 3 } + N _ { D G 4 3 } - N _ { C Y 4 3 } - N _ { C G 4 3 } } } \end{array}$ . Note that since $N _ { C Y 4 3 } + N _ { C G 4 3 } > N _ { D G 4 3 }$ and $F _ { 4 3 } ^ { * } \geq 0$ , we have $N _ { D Y 4 3 } + N _ { D G 4 3 } > N _ { C Y 4 3 } + N _ { C G 4 3 } .$

## Outcome 33

The preferential delivery fee <sub>??</sub> for outcome 33 is determined by the following three CPs

incentive compatibility constraints: $\pi _ { Y 3 3 } \geq \pi _ { Y 4 3 }$ yields $\begin{array} { r } { p _ { 3 3 } \geq \frac { \left( N _ { C Y 4 3 } + N _ { D Y 4 3 } - N _ { C Y 3 3 } - N _ { D Y 3 3 } \right) r _ { Y } } { N _ { C Y 4 3 } } ; } \end{array}$

$$
\pi_ {Y 3 3} \geq \pi_ {Y 4 4} \mathrm{yields} p _ {3 3} \geq \frac {(1 / 2 - N _ {C Y 3 3} - N _ {D Y 3 3}) r _ {Y}}{1 / 2}; \pi_ {G 3 3} \geq \pi_ {G 1 1} \mathrm{yields} p _ {3 3} \leq \frac {(N _ {C G 3 3} + N _ {D G 3 3} - 1 / 2) r _ {G}}{N _ {C G 3 3} + N _ {D G 3 3}};
$$

$$
\pi_ {G 3 3} \geq \pi_ {G 1 3} \mathrm{yields} p _ {3 3} \leq \frac {(N _ {C G 3 3} + N _ {D G 3 3} - N _ {C G 4 3} - N _ {D G 4 3}) r _ {G}}{N _ {C G 3 3} + N _ {D G 3 3} - N _ {D G 4 3}}.
$$

$$
\text {Let} L _ {3 3} = \max \left\{\frac {N _ {C Y 4 3} + N _ {D Y 4 3} - N _ {C Y 3 3} - N _ {D Y 3 3}}{N _ {C Y 4 3}}, \frac {1 / 2 - N _ {C Y 3 3} - N _ {D Y 3 3}}{1 / 2} \right\} \text {and} H _ {3 3} =
$$

min $\left\{ \frac { N _ { C G 3 3 } + N _ { D G 3 3 } - 1 / 2 } { N _ { C G 3 3 } + N _ { D G 3 3 } } , \frac { N _ { C G 3 3 } + N _ { D G 3 3 } - N _ { C G 4 3 } - N _ { D G 4 3 } } { N _ { C G 3 3 } + N _ { D G 3 3 } - N _ { D G 4 3 } } \right\}$ . Thus, there exists a feasible $p _ { 3 3 }$ if and only if $L _ { 3 3 } r _ { Y } \le H _ { 3 3 } r _ { G }$ . Here we note that $\begin{array} { r } { L _ { 3 3 } \ge \frac { 1 / 2 - N _ { C Y 3 3 } - N _ { D Y 3 3 } } { 1 / 2 } } \end{array}$ and $\begin{array} { r } { H _ { 3 3 } \le \frac { N _ { C G 3 3 } + N _ { D G 3 3 } - 1 / 2 } { N _ { C G 3 3 } + N _ { D G 3 3 } } . } \end{array}$ . So we have $\begin{array} { r } { \frac { L _ { 3 3 } } { H _ { 3 3 } } \ge \frac { \frac { 1 / 2 - N _ { C Y 3 3 } - N _ { D Y 3 3 } } { 1 / 2 } } { \frac { N _ { C G 3 3 } + N _ { D G 3 3 } - 1 / 2 } { N _ { C G 3 3 } + N _ { D G 3 3 } } } = \frac { N _ { C G 3 3 } + N _ { D G 3 3 } } { 1 / 2 } > 1 } \end{array}$ . When these feasible conditions hold, we obtain $p _ { 3 3 } ^ { * } = H _ { 3 3 } r _ { G }$ . In addition, we know from the results in step 2 in the proof of Lemma 2 that $F _ { 3 3 } ^ { * } = $ $\begin{array} { r } { V - t ( 1 - x _ { 3 3 } ) - \frac { k } { 2 } - \frac { d \lambda } { \mu - ( 1 - x _ { D 3 3 } ) \lambda / 2 } . } \end{array}$

We note here that the solution of price <sub>??</sub> in outcomes 44, 43, and 33 form three nonoverlapping intervals. Specifically, we have $\begin{array} { r } { p _ { 4 4 } \leq H _ { 4 4 } r _ { Y } \leq \frac { ( 1 / 2 - N _ { C Y 4 3 } - N _ { D Y 4 3 } ) r _ { Y } } { 1 / 2 - N _ { C Y 4 3 } } \leq p _ { 4 3 } \leq } \end{array}$ min $\{ H _ { Y 4 3 } r _ { Y } , H _ { G 4 3 } r _ { G } \} \le L _ { 3 3 } r _ { Y } \le p _ { 3 3 } \le H _ { 3 3 } r _ { G }$ . The non-overlapping solution reflects the fact that incentive criteria for content providers in outcomes 44, 43, and 33 are mutually exclusive. Observe also that the endpoints of the non-overlapping intervals are given by constant multiples of the revenue rates $r _ { Y }$ and $r _ { G }$ .

## Step 2: Compare the candidate outcomes and derive equilibrium outcomes

In step 2, we compare the ISPs’ profits in outcomes 44, 43, and 33 to determine the equilibrium outcomes. Since ISPs <sub>??</sub> and <sub>??</sub> have the same profit level in a given outcome, we simplify the notations to $\pi _ { C 4 4 } = \pi _ { D 4 4 } = \pi _ { 4 4 } , \pi _ { C 4 3 } = \pi _ { D 4 3 } = \pi _ { 4 3 } , \mathrm { a n d } \pi _ { C 3 3 } = \pi _ { D 3 3 } = \pi _ { 3 3 }$

Outcome 33 is the equilibrium provided all the following inequalities are satisfied: $L _ { 3 3 } r _ { Y } \le$ $H _ { 3 3 } r _ { G } , \pi _ { 3 3 } \ge \pi _ { 4 3 }$ , and $\pi _ { 3 3 } \geq \pi _ { 4 4 }$ . These reduces to the following inequalities: $\begin{array} { r } { r _ { G } \ge \frac { L _ { 3 3 } r _ { Y } } { H _ { 3 3 } } \equiv \beta _ { 1 } r _ { Y } } \end{array}$ $\begin{array} { r } { r _ { G } \ge \frac { ( N _ { C Y 4 3 } + N _ { C G 4 3 } ) p _ { 4 3 } } { H _ { 3 3 } N _ { C G 3 3 } } + \frac { ( N _ { C Y 4 3 } + N _ { C G 4 3 } ) F _ { 4 3 } - F _ { 3 3 } / 2 } { \lambda H _ { 3 3 } N _ { C G 3 3 } } \equiv \alpha _ { 1 } } \end{array}$ , and $\begin{array} { r } { r _ { G } \geq \frac { H _ { 4 4 } r _ { Y } } { 2 H _ { 3 3 } N _ { C G 3 3 } } + \frac { F _ { 4 4 } - F _ { 3 3 } } { 2 \lambda H _ { 3 3 } N _ { C G 3 3 } } \equiv \beta _ { 2 } r _ { Y } + } \end{array}$ $\alpha _ { 2 }$ . Outcome 43 (or outcome 34) is the equilibrium provided all the following inequalities are satisfied: $\begin{array} { r } { r _ { G } \ge \frac { ( N _ { C G 4 3 } + N _ { D G 4 3 } - 1 / 4 ) r _ { Y } } { 1 / 2 - N _ { C Y 4 3 } } \equiv \beta _ { 3 } r _ { Y } , \pi _ { 4 3 } > \pi _ { 3 3 } } \end{array}$ , and $\pi _ { 4 3 } \geq \pi _ { 4 4 }$ . These reduces to the following inequalities: $r _ { G } \ge \beta _ { 3 } r _ { Y } , r _ { G } < \alpha _ { 1 }$ , and $\begin{array} { r } { r _ { Y } \leq \frac { 2 \left( N _ { C Y 4 3 } + N _ { C G 4 3 } \right) p _ { 4 3 } } { H _ { 4 4 } } - \frac { F _ { 4 4 } - 2 \left( N _ { C Y 4 3 } + N _ { C G 4 3 } \right) F _ { 4 3 } } { \lambda H _ { 4 4 } } \equiv } \end{array}$ $\alpha _ { 3 }$ . When the above market conditions are not satisfied, outcome 44 is the equilibrium. Summarizing the above analysis yields Lemma 3.

## E. Proof of Proposition 1

Since the net neutrality regime is essentially equivalent to outcome 11, where neither CP pays for preferential delivery even though they have the option to do so. Based on the results from Lemma 2, we know that in the net neutrality regime, $\begin{array} { r } { \pi _ { C } ^ { N N } = \pi _ { D } ^ { N N } = \pi _ { 1 1 } ^ { * } = \frac { F _ { 1 1 } ^ { * } } { 2 } } \end{array}$ . In addition, there are four possible equilibria in the packet discrimination regime, i.e., $\pi _ { C } ^ { P D } = \pi _ { D } ^ { P D } = \pi _ { 3 3 } ^ { * } =$ $\begin{array} { r } { \frac { F _ { 3 3 } ^ { * } + \lambda p _ { 3 3 } ^ { * } ( 1 - \chi _ { 3 3 } ) } { 2 } , \mathrm { o r } \pi _ { C } ^ { P D } = \pi _ { D } ^ { P D } = \pi _ { 4 3 } ^ { * } = N _ { C 4 3 } ( F _ { 4 3 } ^ { * } + \lambda p _ { 4 3 } ^ { * } ) = \pi _ { 3 4 } ^ { * } = N _ { D 3 4 } ( F _ { 3 4 } ^ { * } + \lambda p _ { 3 4 } ^ { * } ) , \mathrm { o r } \pi _ { C } ^ { P D } = } \end{array}$ $\begin{array} { r } { \pi _ { D } ^ { P D } = \pi _ { 4 4 } ^ { * } = \frac { F _ { 4 4 } ^ { * } + \lambda p _ { 4 4 } ^ { * } } { 2 } } \end{array}$ . From the results in step 3 in the proof of Lemma 2, we know $\pi _ { 4 4 } ^ { * } \geq \pi _ { 1 1 } ^ { * }$ Therefore, we get $\pi _ { C } ^ { P D } = \pi _ { D } ^ { P D } \ge \pi _ { 4 4 } ^ { * } \ge \pi _ { 1 1 } ^ { * } = \pi _ { C } ^ { N N } = \pi _ { D } ^ { N N }$

## F. Proof of Proposition 2

In the net neutrality regime, we know that $\begin{array} { r } { \pi _ { G } ^ { N N } = \pi _ { G 1 1 } ^ { * } = \frac { \lambda r _ { G } } { 2 } } \end{array}$ . In the packet discrimination regime, there are three possible equilibria – outcomes 33, 43, and 44. The corresponding profit for content provider is: $\pi _ { G 3 3 } ^ { * } = \lambda ( N _ { C G 3 3 } + N _ { D G 3 3 } ) ( r _ { G } - p _ { 3 3 } ^ { * } ) , \pi _ { G 4 3 } ^ { * } = \lambda ( N _ { C G 4 3 } + N _ { D G 4 3 } ) ( r _ { G } -$ $p _ { 4 3 } ^ { * } )$ , and $\begin{array} { r } { \pi _ { G 4 4 } ^ { * } = \frac { \lambda ( r _ { G } - p _ { 4 4 } ^ { * } ) } { 2 } } \end{array}$ . Next we focus on comparing $\pi _ { G 3 3 } ^ { * }$ and $\pi _ { G 1 1 } ^ { * }$

Recall that $p _ { 3 3 } ^ { * } = H _ { 3 3 } r _ { G }$ , where $\begin{array} { r } { H _ { 3 3 } = \operatorname* { m i n } \bigg \{ \frac { N _ { C G 3 3 } + N _ { D G 3 3 } - 1 / 2 } { N _ { C G 3 3 } + N _ { D G 3 3 } } , \frac { N _ { C G 3 3 } + N _ { D G 3 3 } - N _ { C G 4 3 } - N _ { D G 4 3 } } { N _ { C G 3 3 } + N _ { D G 3 3 } - N _ { D G 4 3 } } \bigg \} } \end{array}$ If $\begin{array} { r } { p _ { 3 3 } = \frac { \left( N _ { C G 3 3 } + N _ { D G 3 3 } - 1 / 2 \right) r _ { G } } { N _ { C G 3 3 } + N _ { D G 3 3 } } \mathrm { , } } \end{array}$ , then $\begin{array} { r } { \pi _ { G 3 3 } ^ { * } = \lambda ( N _ { C G 3 3 } + N _ { D G 3 3 } ) \left( r _ { G } - \frac { \left( N _ { C G 3 3 } + N _ { D G 3 3 } - 1 / 2 \right) r _ { G } } { N _ { C G 3 3 } + N _ { D G 3 3 } } \right) = } \end{array}$ $\begin{array} { r } { \frac { \lambda r _ { G } } { 2 } = \pi _ { G 1 1 } ^ { * } \cdot \mathrm { H } { \mathrm { p } _ { 3 3 } } = \frac { \left( N _ { C G 3 3 } + N _ { D G 3 3 } - N _ { C G 4 3 } - N _ { D G 4 3 } \right) r _ { G } } { N _ { C G 3 3 } + N _ { D G 3 3 } - N _ { D G 4 3 } } \mathrm { , t h e n } \pi _ { G 3 3 } ^ { * } = \lambda ( N _ { C G 3 3 } + N _ { D G 3 3 } ) \left( r _ { G } - \mathrm { G e } _ { G 1 1 } \right) \left( r _ { G 1 } ^ { * } \frac { { \mathrm { x } _ { 0 } } } { r _ { G 2 } ^ { 2 } } \right) , } \end{array}$ $\begin{array} { r } { \frac { ( N _ { C G 3 3 } + N _ { D G 3 3 } - N _ { C G 4 3 } - N _ { D G 4 3 } ) r _ { G } } { N _ { C G 3 3 } + N _ { D G 3 3 } - N _ { D G 4 3 } } ) = \frac { N _ { C G 4 3 } ( N _ { C G 3 3 } + N _ { D G 3 3 } ) \lambda r _ { G } } { N _ { C G 3 3 } + N _ { D G 3 3 } - N _ { D G 4 3 } } \ge \frac { \lambda r _ { G } } { 2 } = \pi _ { G 1 1 } ^ { * } } \end{array}$ . Thus, CP <sub>??</sub>’s profit in outcome 33 is higher than that in outcome 11 if and only if $\begin{array} { r } { \frac { N _ { C G 3 3 } + N _ { D G 3 3 } - N _ { C G 4 3 } - N _ { D G 4 3 } } { N _ { C G 3 3 } + N _ { D G 3 3 } - N _ { D G 4 3 } } < } \end{array}$ $\frac { N _ { C G 3 3 } + N _ { D G 3 3 } - 1 / 2 } { N _ { C G 3 3 } + N _ { D G 3 3 } } .$ , which can be simplified to $\begin{array} { r } { ( N _ { C G 3 3 } + N _ { D G 3 3 } ) N _ { C G 4 3 } > \frac { N _ { C G 3 3 } + N _ { D G 3 3 } - N _ { D G 4 3 } } { 2 } . } \end{array}$

From the proof of Lemma 1, we know $\begin{array} { r } { N _ { C G 3 3 } + N _ { D G 3 3 } = 1 - x _ { 3 3 } , N _ { C G 4 3 } = \frac { z _ { G 4 3 } } { 2 } } \end{array}$ , and $\scriptstyle { { \frac { 1 } { 2 } } - }$ $x _ { D 4 3 } = \frac { k } { t } \left( z _ { Y 4 3 } - z _ { G 4 3 } \right)$ . This gives: $N _ { D G 4 3 } = ( 1 - x _ { D 4 3 } ) ( 1 - z _ { G 4 3 } ) - { \textstyle { \frac { 1 } { 2 } } } ( z _ { Y 4 3 } - z _ { G 4 3 } ) ( { \textstyle { \frac { 1 } { 2 } } } -  \cal$ $x _ { D 4 3 } \big ) = ( 1 - x _ { D 4 3 } ) ( 1 - z _ { G 4 3 } ) - \textstyle \frac { k } { 2 t } ( z _ { Y 4 3 } - z _ { G 4 3 } ) ^ { 2 } .$

Substituting these equations into the $\begin{array} { r } { ( N _ { C G 3 3 } + N _ { D G 3 3 } ) N _ { C G 4 3 } > \frac { N _ { C G 3 3 } + N _ { D G 3 3 } - N _ { D G 4 3 } } { 2 } } \end{array}$ yields $\begin{array} { r } { ( 1 - x _ { 3 3 } ) \left( \frac { z _ { G 4 3 } } { 2 } \right) > \frac { 1 } { 2 } \bigg ( ( 1 - x _ { 3 3 } ) - ( 1 - x _ { D 4 3 } ) ( 1 - z _ { G 4 3 } ) + \frac { k } { 2 t } ( z _ { Y 4 3 } - z _ { G 4 3 } ) ^ { 2 } \bigg ) } \end{array}$ . Rearranging this inequality gives $\begin{array} { r } { \frac { t } { k } > \frac { ( z _ { Y 4 3 } - z _ { G 4 3 } ) ^ { 2 } } { 2 ( x _ { 3 3 } - x _ { D 4 3 } ) \left( 1 - z _ { G 4 3 } \right) } . } \end{array}$ . Therefore, if the ratio of $\frac { t } { k }$ is higher than a threshold, $\pi _ { G 3 3 } ^ { * } > \pi _ { G 1 1 } ^ { * }$

In general, comparisons of $\pi _ { G 3 3 } ^ { * } , \pi _ { G 4 4 } ^ { * }$ , and $\pi _ { G 1 1 } ^ { * }$ show that CP <sub>??</sub>’s profit may be lower, unchanged or higher in the packet discrimination regime than that in the net neutrality regime. Specifically, it is lower under equilibrium 44, but is unchanged or higher under equilibrium 33, i.e., $\pi _ { G 3 3 } ^ { * } \geq \pi _ { G 1 1 } ^ { * } \geq \pi _ { G 4 4 } ^ { * }$

## G. Proof of Proposition 3

In the net neutrality regime, we know that $\begin{array} { r } { \pi _ { Y } ^ { N N } = \pi _ { Y 1 1 } ^ { * } = \frac { \lambda r _ { Y } } { 2 } } \end{array}$ . In the packet discrimination regime, there are three possible equilibria – outcomes 33, 43, and 44. The corresponding profit for content provider <sub>??</sub> is: $\pi _ { Y 3 3 } ^ { * } = \lambda x _ { 3 3 } r _ { Y } , \pi _ { Y 4 3 } ^ { * } = \lambda ( N _ { Y 4 3 } r _ { Y } - N _ { C Y 4 3 } p _ { 4 3 } ^ { * } )$ , and $\begin{array} { r } { \pi _ { Y 4 4 } ^ { * } = \frac { \lambda ( r _ { Y } - p _ { 4 4 } ^ { * } ) } { 2 } . } \end{array}$ We compare <sub>??</sub>’s profit in the three possible equilibria in the packet discrimination regime to its profit in the net neutrality regime one by one. We first note that $\pi _ { Y 1 1 } ^ { * } \geq \pi _ { Y 4 4 } ^ { * }$ . Furthermore, since $\begin{array} { r } { x _ { 3 3 } \leq \frac { 1 } { 2 } , } \end{array}$ we get that $\pi _ { Y 1 1 } ^ { * } \geq \pi _ { Y 3 3 } ^ { * }$ . Lastly, since $p _ { 4 4 } ^ { * } \leq p _ { 4 3 } ^ { * } , \pi _ { Y 4 4 } ^ { * } \geq ( N _ { C Y 4 3 } + N _ { D Y 4 3 } ) \lambda r _ { Y } -$

$$
N _ {C Y 4 3} \lambda p _ {4 4} ^ {*} \geq (N _ {C Y 4 3} + N _ {D Y 4 3}) \lambda r _ {Y} - N _ {C Y 4 3} \lambda p _ {4 3} ^ {*} = \pi_ {Y 4 3} ^ {*}.
$$

Summarizing the above, we conclude that $Y _ { \textrm { S } }$ profit is higher in the net neutrality regime than that in all three possible equilibria in the packet discrimination regime. Therefore, $\pi _ { Y } ^ { N N } \geq$ $\pi _ { Y } ^ { P D }$

## H. Proof of Proposition 4

Substituting the equilibrium prices into the social welfare formula $S W _ { i j } = \pi _ { C i j } + \pi _ { D i j } + \pi _ { Y i j } +$ $\begin{array} { r } { \pi _ { G i j } + \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } U _ { i j } ( x , z ) d x d z } \end{array}$ , we get that, in the net neutrality regime, $S W ^ { N N } = S W _ { 1 1 } = V -$ $\begin{array} { r } { \frac { t + k } { 4 } - \frac { d \lambda } { \mu - \lambda / 2 } + \frac { \lambda ( r _ { Y } + r _ { G } ) } { 2 } } \end{array}$ . In the packet discrimination regime, there are three possible equilibria – outcomes 33, 43, and 44. The corresponding social welfare is: $S W _ { 3 3 } = V - t \left( { \textstyle { \frac { 1 } { 2 } } } - x _ { 3 3 } ^ { 2 } \right) - { \textstyle { \frac { k } { 4 } } } -$ $\begin{array} { r } { \frac { d \lambda } { \mu - ( 1 - x _ { 3 3 } ) \lambda / 2 } + \lambda x _ { 3 3 } r _ { Y } + \lambda ( 1 - x _ { 3 3 } ) r _ { G } , S W _ { 4 3 } = F _ { 4 3 } + \frac { \lambda ( r _ { Y } + r _ { G } ) } { 2 } + \frac { \lambda ( r _ { G } - r _ { Y } ) } { 2 } ( 2 - z _ { Y 4 3 } - z _ { G 4 3 } ) \left( \frac { 1 } { 2 } - \frac { 1 } { 3 } ( r _ { X } + r _ { G } ) ^ { 2 } \right) , } \end{array}$ ??<sub>??43</sub>� + ????<sub>??43</sub>??<sub>??</sub> + ????<sub>??43</sub>??<sub>??</sub> + ?? �??<sub>??43</sub> − <sup>1</sup> + ?? �??<sub>??43</sub> − <sup>1</sup>� + <sup>??</sup> �??<sub>??43</sub> + (??<sub>??43</sub> − ??<sub>??43</sub>) + <sup>??</sup> (??<sub>??43</sub> + ??<sub>??43</sub>) 1 − ??<sub>??43</sub> 2??<sup>2</sup> �<sup>1</sup> − ??<sub>??43</sub><sup>3</sup> � + <sup>2??2</sup> (??<sub>??43</sub><sup>3</sup> − ??<sub>??43</sub><sup>3</sup> ) t (?? + 2????<sub>??43</sub>) 1 一 2 � 3k (8 3?? 2?? � ??<sub>??43</sub><sup>2</sup> � ?? (?? + 2???? )(??<sup>2</sup> − ??<sup>2</sup> )<sup>,</sup> <sup>and</sup> ???? = ?? − <sup>??+??</sup> ???? (?? +?? ) 一 + 2t 4 ??− ⁄2 2

We first note that $S W _ { 4 4 } = S W _ { 1 1 }$ . Furthermore, since $\begin{array} { r } { x _ { 3 3 } \leq \frac { 1 } { 2 } , } \end{array}$ we get that $S W _ { 3 3 } \ge S W _ { 1 1 }$ Lastly, we compare $S W _ { 4 3 }$ and $S W _ { 1 1 }$ . Let $\Delta S W = S W _ { 4 3 } - S W _ { 1 1 }$ . We can show that $\frac { \partial \Delta S W } { \partial \mu } \geq 0$ and $\Delta S W = 0 \mathrm { a t } \mu = \lambda$ . Therefore, $S W _ { 4 3 } \geq S W _ { 1 1 }$

Summarizing the above, we conclude that social welfare is weakly higher in all three possible equilibria in the packet discrimination regime than that in the net neutrality regime. Therefore, $S W ^ { P D } \ge S W ^ { N N }$
