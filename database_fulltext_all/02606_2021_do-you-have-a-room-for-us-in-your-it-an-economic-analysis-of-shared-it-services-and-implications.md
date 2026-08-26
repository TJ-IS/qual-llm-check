---
otero_id: 2606
otero_key: "FEDT35PV"
title: "Do You Have a Room for Us in Your IT? An Economic Analysis of Shared IT Services and Implications for IT Industries"
authors: "Min Chen; Min-Seok Pang; Subodha Kumar"
year: "2021"
journal: "MIS Quarterly"
doi: "10.25300/misq/2021/15573"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DO YOU HAVE A ROOM FOR US IN YOUR IT? AN ECONOMIC ANALYSIS OF SHARED IT SERVICES AND IMPLICATIONS FOR IT INDUSTRIES<sup>1</sup>

Min Chen School of Business, George Mason University, 4400 University Drive, Fairfax, VA 22030 U.S.A. {mchen15@gmu.edu}

Min-Seok Pang and Subodha Kumar

Fox School of Business, Temple University, 1801 Liacouras Walk, Philadelphia, PA 19122 U.S.A. {minspang@temple.edu} {subodha@temple.edu}

We are witnessing an interesting and unique phenomenon in enterprise information technology (IT) adoption and management in public-sector organizations: shared IT services. Instead of implementing separate IT services, governments come together to pool their IT resources into one single IT service. In this study, we develop a game-theoretic model to analyze the governments’ decision to share IT services and understand how the introduction of shared services transforms the strategic interactions between the governments and the vendor. We study three common regimes used in the adoption of shared IT services: (1) a cost-sharing regime where costs are split proportionally, (2) a profit-center regime where one government charges a surplusmaximization price to the other, and (3) a coordination regime where governments coordinate their decisions to maximize aggregate surplus. Our analyses generate several intriguing findings. First, although charging a surplus-maximizing price seems to be a lucrative option, we find that a government does not always benefi by acting as a profit center. Second, the cost-sharing regime does not always incentivize the shared service adoption despite being often viewed as a fairer and more convenient arrangement. Third, we find that there can be significant under-utilization of shared services in the absence of proper coordination, in a sense that the governments may choose not to share their IT services even if doing so would increase their aggregate surplus. Finally, even though coordination promotes the adoption of shared IT services, it can sometimes be inefficient from the social welfare’s perspective because the increase in governments’ surplus can be outweighed by the decrease in the vendor’s profit. We also present a range of extensions to our model to show that our main takeaways carry over when some model assumptions are relaxed.

Keywords: Shared IT service, outsourcing, governments, economies of scale, social welfare, game theory

Tom Bossert, Assistant to the President for Homeland Security and Counterterrorism (J. Miller 2017)

## Introduction

The past few years have witnessed an interesting and unique phenomenon in enterprise information technology (IT) adoption and management in the public-sector organizations: shared IT services. Instead of implementing separate IT services, governments come together to pool their IT resources into one single IT service. The adoption of shared IT services is widespread among state and local governments in the United States, as evidenced by a recent survey reporting that 79% of the states surveyed plan to either introduce or expand their use of shared IT services (NASCIO 2017). For example, ReEmployUSA, a four-state unemployment insurance (UI) consortium led by Mississippi, was created to implement and launch a multi-tenant UI system for its member states including Rhode Island, Maine, and Connecticut (Pincus 2018). Similar efforts are underway elsewhere, including Idaho’s Internet Unemployment System (iUS), which is to be shared with Vermont (Douglas 2017a), and G2G Cloud Solutions developed by Oakland County, Michigan, which provides IT services to 82 agencies in the state (Knell 2017). The importance of shared IT services is also echoed by U.S. state chief information officers (CIOs), who ranked shared services as one of their top 10 policy and technology priorities (MeriTalk 2018).

Shared IT services are also a key strategy for IT modernization among agencies at the federal level. In 2015, the U.S. Office of Management and Budget (OMB) and the General Services Administration (GSA) announced the establishment of a government-wide operating model for shared services, as part of its plan to modernize the federal IT infrastructure (Mader and Roth 2015). Recently, the federal government has identified shared IT services as a key pillar of its IT strategy and has continued the push for wider adoption of shared services (Erlanger 2018; Goldstein 2018). In this direction, the White House has recently created the Office of Shared Solutions and Performance Improvement to centralize its plan for shared services (Cordell 2018). The fast-increasing adoption of shared IT services poses interesting questions: What are the key drivers for sharing IT services among governments? How does this affect governments’ surplus and social welfare?

## Background and Motivation

Shared IT services are gaining traction in the public sector for several reasons. First, by sharing the costs for development and maintenance of IT systems, participating governments can save a substantial amount of investments that would otherwise have been spent in separate systems (Heaton 2013; Mew

2018). According to a survey by Government Technology and Oracle, the biggest consideration for shared services is cost savings (Government Technology 2017). Since 2012, the federal government has saved nearly \$4 billion as a result of its IT reform efforts such as data center consolidation and migration to shared services (Goldstein 2016). Thus, a shared service has become an attractive option for governments that are suffering from mounting budget deficits and declining tax revenues. Second, the governments can save excess capacities that would exist in disparate systems. For example, the State of Ohio shares its unused server capacities with local governments within the state and is expected to save \$1 million annually in IT costs (Newcombe 2016a). Third, by pooling their scales (e.g., population, users, or capacity), the governments can increase their collective bargaining power vis-à-vis private-sector IT vendors, which has the potential to lower the prices (Morgan 2017).

Motivated by these benefits, the adoption of shared IT services has increased significantly in recent years. A recent survey reports that 83% of the cities and 78% of the counties surveyed are using shared IT services (Newcombe 2016a). For example, four U.S. states (Tennessee, North Carolina, South Carolina, and Georgia) formed the Southeast Consortium Unemployment Insurance Benefits Initiative (SCUBI) and agreed to build a single, shared unemployment insurance system because these states operate similar unemployment benefits and healthcare programs (Douglas 2017a). Likewise, Michigan agreed with Illinois that instead of developing a separate system, Illinois would piggyback on Michigan’s information system for Medicaid, a healthcare program for lower-income citizens (Heaton 2013). Recently, as a member of the National Consortium for Offender Management System (NCOMS), the Missouri Department of Corrections has committed to implementing a multi-state shared service for offender management systems (Wood et al. 2016).

What is unique in this setting is that these governments do not directly compete with each other, because their respective “markets” or jurisdictions are separate, whereas in the private sector, it is common that competition leads to a divided market and it is rare that a single firm can cover the entire market. As such, the markets in the public sector are fully “covered” (as there is typically one service provider/ government in each jurisdiction), and thus governments are not interested in outperforming others to increase market shares. This absence of direct competition makes it possible for the governments to adopt shared IT services. It would be difficult to find a similar case in the private sector; a business firm is unlikely to share its core IT system, which contains a range of confidential information for competitiveness, with its competitors in the same industry (e.g., between General Motors and Ford or between McDonald’s and Burger King).

## Research Questions and Contributions

Although shared IT services are an intriguing practice in the public sector, its impacts on IT industries and its welfare implications are not well understood in the Information Systems (IS) literature. In this paper, we attempt to fill this gap by building an economic model to analyze the decisions for shared service adoption and outsourcing. Our model considers the decision problems for two governments with different user populations and one external IT vendor. A larger government has an in-house IT function, whereas a smaller one does not have its own and must resort to either the larger government or the vendor.<sup>2</sup> The governments first decide whether to adopt a shared IT service, or have separate IT services. Following the IS literature and anecdotal evidence, we focus on two key factors affecting this decision: cost savings from economies of scales, and heterogeneity in the two governments’ requirements and IT profiles. Afterward, they choose whether to keep the IT services in-house or outsource to the external vendor, a decision that is greatly influenced by the vendor’s technological advantage.

In practice, there are three common arrangements used in the adoption of shared IT services. For example, the governments can split the development costs proportionally to their sizes (a cost-sharing regime); one government can charge the other a price for piggybacking on its IT system (a profit-center regime); or the two governments can coordinate their decision for shared services, in which case a transfer price can be made if necessary (a coordination regime). Correspondingly, we analyze the three regimes and compare the equilibrium results across them. In doing so, we examine how the choices of regimes can shape the decision to adopt and outsource a shared service and derive strategic implications on the vendor’s pricing and profits, the governments’ surplus, and social welfare. As such, our paper highlights and captures four major differences between shared and non-shared (separate) IT services: (1) cost savings from economies of scale; (2) compatibility costs due to heterogeneous requirements of the two governments; (3) three contractual regimes (cost-sharing, profit-center, and coordination), and (4) one contracting party instead of two.

One may wonder if the profit-center regime is always remunerative to the larger government as it can charge a surplus-maximizing price rather than splitting the costs. To understand it, we first ask the following question: Does the larger government always benefit from the setup of the profitcenter regime? We show that this is not always the case in our setting. In fact, the larger government may be better off with a simple cost-sharing setup when the vendor’s technological advantage is not too small. This explains why both the profit-center and the cost-sharing regimes are commonly adopted in practice (Eidam et al. 2017; Wood et al. 2016).

Another important question we analyze is: How is the decision to share IT services shaped by different regimes? One may expect that a shared service is more likely to be adopted in the cost-sharing regime as it is often viewed as a fairer and more convenient arrangement. We show that this is not always the case. In fact, the profit-center regime may better induce the governments to share IT services when the vendor’s technological advantage is small. Nevertheless, both the cost-sharing and profit-center regimes can lead to signifi cant under-utilization of shared services, in the sense that the governments may choose not to share their IT services even if doing so would increase their aggregate surplus, a classic prisoner’s dilemma result. This result provides insights into why shared services are more prevalent among federal agencies (where coordination exists) than at municipal levels (where coordination is absent or weak) (Newcombe 2016b; Rich 2013). As such, we propose several coordinating mechanisms to achieve such an alignment and a broader adoption of shared IT services, including financial incentives (e.g., transfer payments or matched funds). This is echoed by recent initiatives from major states such as Connecticut and New York that provide a large amount of financial incentives for shared IT services to local governments (Moody 2018; Towns and Knell 2014).

While coordination helps promote the adoption of shared IT services, an interesting question to ask is: Is promoting shared IT services always beneficial to social welfare? Surprisingly, we find that this is not always the case and the governments’ decision to adopt shared IT services may not be socially optimal. This occurs when an increase in the governments’ surplus is outweighed by a decrease in the vendor’s profit. This finding is of particular importance, because the governments are expected to act as a social planner to maximize social welfare. Given the increasing interest in government-provided incentives and subsidies for shared services (Moody 2018), this calls for more attention to conduct a thorough assessment of the impact on society.

In addition to the regimes, the decision to share IT services can be affected by other factors such as the size of participating governments. Therefore, another related question is: Are the governments more likely to form shared services with peers of similar sizes or different sizes? Intuitively, a government should be more likely to share its IT service with large governments for potentially greater benefits from economies of scale. Interestingly, we find this is not always true. Specifically, we find that a large government is more likely to form shared IT services with peers of smaller sizes under the cost-sharing and the coordination regimes. This helps explain why we see numerous examples of large municipalities sharing their IT services with smaller ones (Knell 2017; Newcombe 2016b).

Our finding echoes the idea that cost savings are a primary driver for shared IT services but highlights another interesting reason. In the absence of shared services, the vendor can set “personalized” prices for each government; alternatively, for a shared service, it can set only one price for a “bundle” (the shared service). Thus, the vendor’s inability to pricediscriminate in the shared service prevents it from extracting more surplus from the governments, resonating the findings from the literature of information goods bundling (Cao et al. 2015; Geng et al. 2005).

We extend the main model in several different ways to demonstrate that our core insights continue to hold when some assumptions are relaxed and obtain more intriguing results. For example, instead of an exogenous setup for the regime selection, we consider a “super game” (see “Endogenizing the Choice of Regime”) where a social planner is to choose a regime that maximizes social welfare (sum of the governments’ aggregated surplus and the vendor’s profit). Our analysis shows that the cost-sharing regime does not always yield the most social welfare. Given that the federal government mandates the cost-sharing regime for shared IT services for federally supported government programs (Newcombe 2016c), we find that such a requirement can undermine social welfare. An important takeaway is that the federal government should allow more flexibility for state and local governments with respect to arrangements for shared IT services.

This paper contributes to the IS literature by investigating an intriguing practice in enterprise IT adoption and management that little prior work has examined. While several theoretical studies examine management of internal IS functions with analytical modeling (e.g., Li and Chen 2012; Vithayathil and Choudhary 2014), ours is the first economic analysis of shared IT services in the public sector. We offer a new theoretical perspective to the IS outsourcing literature by analyzing different regimes commonly used in practice and how they shape the decisions for shared service adoption. We expect that our research will offer new insights for IS researchers and important implications for both IT managers in the public sector and practitioners in IT industries, of which governments are one of the largest customers.

## Related Work

Our study is mainly related to three streams of literature: (1) IS outsourcing, (2) organization of internal IT function, and (3) on-demand technologies. In each subsection below, we briefly discuss the related work and compare it with our work to highlight the contribution of this study.

## IS Outsourcing

Similar to prior studies in IS outsourcing, we study a decision of whether an enterprise IT system is developed internally or outsourced to an external vendor. The IS outsourcing literature shows that an outsourcing decision is driven by factors such as a vendor’s technical and business expertise, a client’s core competency, specificity of IT assets, transaction costs, service level agreements, and the degree of information asymmetry and conflicts of interests between the two parties (Goo et al. 2009; Goo et al. 2007; Lacity and Willcocks 1998; Levina and Ross 2003; Loh and Venkatraman 1992; Rao et al. 1996; Richmond et al. 1992; Smith et al. 1998; Susarla 2012; Susarla et al. 2010; Teng et al. 1995; Wang et al. 1997).

While many of these factors are also considered in this study, there is one important difference: In the IS literature, there is a clear distinction between a client and a vendor, and it does not consider a case in which a client can offer an IT service to another client. In our model, however, one of the clients (a government) may become a service provider to another client, blurring the boundary between the client and the vendor. In essence, we model the competition between a vendor and a client, a unique aspect that a few IS studies have acknowledged. In addition, the prior literature does not investigate a case in which two clients come together to share their IT services, a phenomenon that is increasingly prevalent in the public sector.

## Organization of Internal IT Functions

There is abundant literature on organization of IT functions with a firm (Choudhary and Vithayathil 2013; Clemons and Gu 2003; Dewan 1996; Dewan and Mendelson 1990; Mendelson 1985; Pick and Whinston 1989; Ross et al. 1999; Vithayathil and Choudhary 2014; Wang and Barron 1995; Whang 1990). For instance, Vithayathil and Choudhary (2014) compare two setups: a cost center in which top management decides the price and quality of IT services, and a profit center in which an internal IT group decides the price and quality. They find that under the profit center setting, business functions consume a greater amount of IT services than under the cost center setting when the marginal cost of IT services is high enough.

There are notable differences in our research. First, we consider a setting wherein governments execute strategic actions (i.e., share versus non-share and outsource versus in-house), a feature that the related prior studies do not consider. Second, we examine a case in which an IT function in one organization provides services to another organization that has heterogeneous requirements and IT profiles. Third, besides the profit-center regime that is similar to the setup considered in the previous studies, we also consider two other regimes (the cost-sharing and the coordination regimes), which are unique in the government IT sector.

## On-Demand Technologies

Our setting of shared IT services seems to resemble ondemand technologies such as cloud computing and softwareas-a-service (SaaS) (August et al. 2014; Susarla et al. 2003). Several studies analyze the pricing and competitive implications of such technologies (e.g., Cheng and Koehler 2003; Singh et al. 2004). For example, Chen and Wu (2013) investigate how the introduction of on-demand technologies with variable costs affects a market structure. However, shared IT services are different, conceptually and technically, from cloud computing in a number of ways.

First, with a shared service, participating entities share one single IT system, while cloud computing hosts several different IT systems. Second, from a vendor’s point of view, the cloud service provider has separate contracts with different clients, while a vendor for a shared service has one contract with an entity that represents participating organizations. For instance, in the case of the shared unemployment insurance system introduced earlier, the states have formed one contracting party named SCUBI (GCN 2014).

The remainder of this paper is organized as follows. First, we introduce the model setup. We then analyze the equilibriums under three regimes in the shared service context, followed by an examination of the strategic implications of shared IT services including the impacts on the vendor, governments, and overall social welfare. We then consider several extensions of the main model. Finally, we conclude the paper and provide directions for future research.

## The Model

We consider two governments (Gov-A and Gov-B) that seek to develop new IT services of similar functionalities for their users (residents or employees). Denote the size of their respective user bases by $N _ { i } , i \in \{ A , B \}$ , and without loss of generality, we let $N _ { A } \geq N _ { B } .$ There is one private-sector IT vendor<sup>3</sup> with expertise and capabilities in developing enterprise IT services for both Gov-A and Gov-B. We assume that Gov-A has an internal IT function with the capability to develop IT services for both governments in-house, whereas Gov-B has a small in-house IT group which either lacks sufficient technological capability to develop a separate IT service or is economically infeasible to do so.<sup>4</sup> As such, Gov-B needs to resort to an external party (either Gov-A or the vendor) for system development. Next, we discuss the important elements of our model.

## The Cost for IT Services

As in the prior literature (Jones and Mendelson 2011; Wei and Nault 2013), we consider the cost for developing and operating an IT service to be increasing and convex in the quality of the service q<sup>j</sup>, where j 0 {I, O} indicates the quality level of an IT system provided by Gov-A (j = I, insourcing) or the vendor (j = O, outsourcing). The vendor’s technological advantage is often cited as one primary motive for IT outsourcing in the literature (e.g., Ang and Straub 1998; Levina and Ross 2003). Capturing this and the heterogeneity in technological capabilities, the quality cost per user<sup>5</sup> in our model is $\alpha ^ { j } ( q ^ { j } ) ^ { 2 } ;$ , where á<sup>j</sup> is a measure of technological capabilities of Gov-A or the vendor. We let $0 < \alpha ^ { o } \ < \alpha ^ { I }$ reflect the notion that the vendor’s superior capability renders a cost advantage over Gov-A (Levina and Ross 2003; Ross 2011).

Prior studies (e.g., Janssen and Joha 2006; Schulz and Brenner 2010; Xue et al. 2011) widely recognize economies of scale as an important factor to share IT services. Thus, we consider the costs to be increasing and concave in the user population to capture the cost advantages accrued to the governments due to their scale of operation. Specifically, we consider a setting similar to prior studies on vertical differentiation and economies of scale (e.g., Banker et al. 1998; Cachon and Harker 2002; Moorthy 1988).<sup>6</sup> The cost function for developing and operating an IT service of quality $q ^ { j }$ for a government of size $N _ { i }$ by either Gov-A or the vendor is given by

$$
C _ {i} ^ {N j} = \alpha^ {j} \left(q ^ {N j}\right) ^ {2} N _ {i} + \phi N _ {i} ^ {\beta}
$$

where $i \in \{ A , B \} , j \in \{ I , O \} . ^ { 7 }$

We let $0 < \beta < 1$ capture the economies of scale: the marginal cost per user is decreasing in user population $N _ { i \cdot } ^ { \mathrm { ~ 8 ~ } }$ Here, $\phi$ is the coefficient for the economies of scale.

## Misfit Costs

Despite its cost advantage, outsourcing can sometimes entail additional costs that are not insubstantial. One such cost that has been widely documented in the literature is a “misfit” cost between an IT service by a vendor and the ideal system for a client (Cheng et al. 2011; Flinders 2014; Guo et al. 2012). This is because a service may not completely meet the unique requirements of the client when developed by another party (Marquis 2018; Meeken 2013). Another source of misfit cost arises from a need to change or migrate existing legacy systems in order to function with the outsourced IT service (Goodrich 2017; Hurt 2011). This is particularly true for government agencies, many of which still rely on decades-old legacy systems (Douglas 2017b; B. Miller 2017). If not implemented properly, the outsourced IT system may not work seamlessly with the existing IT systems, causing system failures or disruptions of services to users (e.g., Ellis 2018; O’Brien 2018). On the other hand, an in-house IT function can develop a system that better meets the requirements and specifications and fits with the existing IT infrastructures, because the in-house team has a better understanding of the needs and domain knowledge of the client (Clydebuilt Business Solutions 2012; Halstead 2017).

The misfit cost is modeled over a Hotelling line (d’Aspremont et al. 1979). In particular, the specifications of the vendor’s product and the requirements of the two governments are located along a unit Hotelling line, with the vendor located at 0 and Gov-A and Gov-B located at a and b $( 0 < a , b \leq 1 )$ respectively (Figure $1 ) . ^ { 9 }$ If Gov-A develops an IT service internally, the misfit cost for Gov-A is assumed to be $0 . { } ^ { 1 0 }$ However, if it is outsourced to the vendor, then Gov-A incurs a disutility of ak $N _ { A } ,$ where k is the unit misfit cost. Similarly, Gov-B’s disutility is $b k N _ { B }$ if its service is outsourced to the vendor and $d k N _ { B }$ if it is offered by Gov-A, where $d = | a - b | .$ The value of d would be smaller, for instance, for two governments with similar IT infrastructures or for two municipalities in the same state (e.g., Minneapolis and St. Paul) than ones in two different states (e.g., Philadelphia and New York City). We consider $b > a / 2$ (i.e., Gov-B is closer to Gov-A than the vendor) so that insourcing to Gov-A can be a feasible option for Gov-B. Otherwise, Gov-B would always prefer outsourcing, leading to trivial results.

## User Utility

The utility derived by a user from using an IT service of quality q<sup>j</sup> is denoted by $\theta q ^ { j } ,$ , where è is her marginal valuation for quality. We consider that all users will use the adopted IT service, i.e., the market is covered. This is quite reasonable in our setting because for public services (e.g., welfare programs, license and inspections), there is typically only one service provider (a government) in each jurisdiction, and the only way to access the services is through a dedicated system.<sup>11</sup> Without loss of generality, we normalize è to 1 (Cavusoglu et al. 2009). Thus, the total gross benefit of users from an IT service of quality $q ^ { j }$ is Nq<sup>j</sup> . Table 1 lists the key notations used in our model.

<table><tr><td>Vendor&#x27;s Profile</td><td>Gov-A&#x27;s Profile &amp; Requirement</td><td>Gov-B&#x27;s Profile &amp; Requirement</td></tr><tr><td>0</td><td>a</td><td>b</td></tr><tr><td colspan="3">(a) when a &lt; b</td></tr></table>

Figure 1. Location of the Governments and the Vendor in a Hotelling Line

<table><tr><td colspan="2">Table 1. List of Notations</td></tr><tr><td> $N_i$ </td><td>i ∈ {A, B}, user population of Gov-A and Gov-B</td></tr><tr><td> $q_i^{lj}$ </td><td>The IT service quality for Government i ∈ {A, B}, given its decision on shared service adoption l ∈ {N, S} and choice of insourcing/outsourcing j ∈ {O, I}</td></tr><tr><td> $C_i^{lj}$ </td><td>IT service development costs incurred for i ∈ {A, B}, j ∈ {I, O}, l ∈ {N, S}</td></tr><tr><td> $\alpha^j$ </td><td>Technological capability of Gov-A&#x27;s in-house team (j = I) and the outsourcing vendor (j = O)</td></tr><tr><td>β</td><td>Degree of economies of scale with respect to capacity (0 &lt; β &lt; 1)</td></tr><tr><td>φ</td><td>Coefficient for the economies of scale</td></tr><tr><td>a, b</td><td>Locations of Gov-A&#x27;s and Gov-B&#x27;s requirements in a Hotelling line, respectively (Figure 1)</td></tr><tr><td>d</td><td>= |a - b|, heterogeneity between Gov-A and Gov-B</td></tr><tr><td>k</td><td>Disutility cost per distance (Figure 1)</td></tr><tr><td>ψ</td><td>Unit compatibility cost to in the shared service</td></tr><tr><td> $\Delta_a$ </td><td>=  $\frac{(\alpha^l - \alpha^O)}{4\alpha^O\alpha^l}$ , the relative technological advantage of the vendor vis-à-vis Gov-A</td></tr><tr><td> $\pi^{lm}$ </td><td>The vendor&#x27;s profit given the choices of shared service adoption (l ∈ {N, S}) and outsourcing, with m ∈ {O, I, D} indicating outsource, insource, or different strategies, respectively</td></tr><tr><td> $W_i^{lm}$ </td><td>Surplus of Government i ∈ {A, B}, where m ∈ {O, I, D} indicates outsource, insource, or different strategies, respectively, and l ∈ {N, S} indicates the non-shared or the shared service case</td></tr></table>

## Sequence of the Game

As mentioned earlier, we consider three common contractual arrangements used in the adoption of shared IT services: (1) a cost-sharing regime where the governments can split the development costs proportionally to their sizes; (2) a profitcenter regime where one government can charge the other a price for piggybacking on its IT system; and (3) a coordination regime where the two governments can coordinate their decision for shared services. It is worth noting that the procurement of IT services and contractual arrangements in the public sector are bounded and governed by various laws and regulations that ex ante limit how governments can contract with each other, not the will of participating agencies. For example, when state or local governments use federal aid to develop public services (e.g., Medicaid or unemployment insurance), they are mandated to follow a cost-sharing regime (Newcombe 2016c). As such, it is reasonable to assume an exogenous setup regarding the three contractual arrangements (the cost-sharing, the profit-center, and the coordination regimes) in the shared service case.<sup>12</sup>

The sequence of the game is as follows (see Figure 2). First, given a regime, the two governments decide whether to share IT services and then solicit an offer from the vendor. They are fully aware of the applicable rules and policies of the regime (e.g., how to share the costs, etc.), should they agree to share IT services, and make their decisions based on rational expectation to predict the outcomes and maximize their self-interests. Second, contingent upon the first-stage outcome, both the vendor and Gov-A simultaneously choose the quality of their IT services and the prices for the shared service (if applicable) or for the non-shared services. Third, the governments decide whether to outsource IT services or keep in-house. If the IT services are not shared, both governments make an independent decision. If a shared service is adopted, they make a decision based on the prearranged contractual agreement given in the first stage.

![](/api/attachments/FEDT35PV/fulltext/images/cd618655e99e1437010a687f7029bc5d1dbc1b08adc11a0106b6a3bd566ee28d.jpg)

This setup is consistent with the well-established theories in the public economics and political sciences literatures that a government is an entity with self-interests and aims to maximize its own utility, as in tax revenues, local wealth, or reelection of officials (e.g., Baicker 2005; Besley and Case 1995; Breton and Wintrobe 1975; McCubbins et al. 1987; Nechyba 1997; Niskanen 1968). For example, in his theoretical model, Nechyba (1997, p. 364) puts forth that a government has one of the six objective functions:

(1) to maximize community income, (2) to maximize community property values, (3) to maximize local wealth, (4) to maximize local utility levels, (5) to maximize the size of the local public sector, and (6) to satisfy the current median voter.

It is also consistent with real-life examples where an outsourcing decision and a vendor selection were made after the agreement for shared services (MDHHS 2013; Raths 2015).

## Model Analysis

In this section, we first examine the governments’ decision to outsource IT services and solve the subgame equilibrium for the shared and the non-shared service cases. We then compare the results between the two cases and derive the conditions under which they choose to share IT services. Finally, we provide insights on the vendor’s pricing and profits as well as social welfare.

## The Non-Shared Service Case

The non-shared case is a benchmark case that essentially resembles a typical setting in the private sector where competing firms do not share IT services. The governments maximize their respective objective function, which is the total surplus subtracting the misfit disutility and the IT service cost/price. Specifically, when the Gov-A outsources the IT service to the vendor, its surplus $\mathrm { i s } ^ { 1 3 }$

$$
W _ {A} ^ {N O} = \left(q _ {A} ^ {N O} - k a\right) N _ {A} - p _ {A} ^ {N O} + I _ {B} ^ {N} \left(p _ {B} ^ {N I} - C _ {B} ^ {N I}\right)
$$

and when Gov-A insources, its surplus is

$$
W _ {A} ^ {N I} = q _ {A} ^ {N I} N _ {A} - C _ {A} ^ {N I} + I _ {B} ^ {N} \left(p _ {B} ^ {N I} - C _ {B} ^ {N I}\right)
$$

Here, $p _ { \mathcal { A } } ^ { N O }$ is the vendor’s outsourcing price for Gov-A. $I _ { B } ^ { N }$ is an indicator variable, with $I _ { B } ^ { N } = 1$ indicating Gov-B’s insourcing decision in which case Gov-B chooses Gov-A’s inhouse team and is charged a price $p _ { B } ^ { N I }$ . The development costs by Gov-A’s in-house team for separate services to Gov-A and Gov-B are $C _ { B } ^ { M }$ and $C _ { A } ^ { N I }$ . Similarly, Gov-B’s surplus under outsourcing to the vendor is

$$
W _ {B} ^ {N O} = \left(q _ {B} ^ {N O} - k b\right) N _ {B} - p _ {B} ^ {N O}
$$

and Gov-B’s surplus when its IT system is offered by Gov-A is

$$
W _ {B} ^ {N I} = \left(q _ {B} ^ {N I} - k d\right) N _ {B} - p _ {B} ^ {N I}
$$

$p _ { B } ^ { N I }$ and $p _ { B } ^ { N O }$ are the prices charged by Gov-A and the vendor, respectively. Note that our setting is similar to Li and Chen (2012), where firms represent their respective employees to purchase IT services as a group. Here, each government decides independently whether to outsource its respective IT service. For brevity, the equilibrium and the associated results are characterized in Lemma A1 and Table A1 in Appendix A. All proofs are provided in Appendix B.

Lemma A1 shows that the extent to which the vendor can compete is determined by its relative technological advantage over Gov-A, denoted by $\begin{array} { r } { \Delta _ { \alpha } = \frac { \left( \alpha ^ { I } - \alpha ^ { O } \right) } { 4 \alpha ^ { O } \alpha ^ { I } } } \end{array}$ . When $\Delta _ { a }$ is sufficiently high, the vendor can leverage this advantage to undercut Gov-A just enough to capture the demand from both Gov-A and Gov-B (Case NO) despite the misfit cost. In addition, it shows that the vendor’s equilibrium quality is higher than Gov-A’s but neither is dependent of the quality chosen by the other.

We would like to point out that a primary reason for the constant optimal service quality is the difference between the private and the public sectors. In the private sector, it is common that competition leads to a divided market because of heterogeneous users, and rarely a single firm can cover the entire market. Notable examples are the market of PC operating systems, which is shared by major competitors such as Microsoft and Apple, and the market of desktop browsers, which are dominated by Firefox, Chrome, and Safari. In contrast, when a government provides public services such as unemployment insurance systems or Medicaid systems, the entire population in the respective jurisdiction would have to use the same service, as there is no alternative service provider. See Douglas (2017a), Heaton (2013), Pincus (2018), and Wood et al. (2016) for examples. In this regard, the markets are fully “covered” in the public sector. Consequently, increasing or decreasing the quality level of IT services does not change the size of user population. As a result, both the vendor and Gov-A choose the cost-minimizing quality level and increasing or decreasing it does not help improve their payoffs. On the contrary, in the private sector, a firm can expand the market and improve profits by increasing the service quality. Therefore, the optimal quality in that context is often not a constant.

## The Shared Service Case

In this section, we extend our analysis to the shared service setting where the governments decide whether to share their IT services before making the outsourcing/insourcing decision. We use backward induction to solve the game. Specifically, we first examine whether to outsource IT services given the respective prices and qualities. Then, we compare the result of the shared case with that of the non-shared case to determine their optimal decisions.

Governments often have idiosyncratic requirements for IT services, due to their respective laws, political environments, existing IT infrastructures, and technological requirements (Goodrich 2017). This leads to additional costs needed to ensure that a shared service is properly developed and configured to accommodate the varying requirements of both governments. For instance, in the ReEmployUSA example discussed earlier, besides the common functions, the shared unemployment insurance (UI) system must accommodate UI policies unique to one or more states such as allowances for dependents in Rhode Island and Maine and temporary disability insurances in Rhode Island (Douglas 2017a). Portland, Oregon, led a project to create a shared regional police record management system with Clark County, Washington. But because of their respective laws and policies in the two states (e.g., public information requests in the two states are handled differently), the shared system for the two municipalities entailed substantial additional complexity and costs (Raths 2015). Similarly, in the example of Illinois–Michigan shared system for Medicaid (discussed earlier), since the benefit coverages and the eligibility requirements differ in two states to some extent, the shared system must be designed to accommodate different specifications.

Intuitively, the larger the differences between the governments, the higher costs are incurred to ensure a proper and compatible shared service. Since the governments’ requirements are represented in a Hotelling line (Figure 1), we capture this difference with the distance between their locations on the line $( d = | a - b | )$ . Specifically, we model this additional compatibility cost for the shared IT system as $\psi d N _ { T } ,$ where $N _ { T } { = } N _ { A } { + } N _ { B }$ and ø is the unit compatibility cost. Therefore, the cost function incurred by Gov-A (insourcing, $j = I )$ or the vendor (outsourcing, j = O) for a shared service is

$$
C ^ {S j} = \alpha^ {j} \left(q ^ {S j}\right) ^ {2} N _ {T} + \phi N _ {T} ^ {\beta} + \psi d N _ {T}
$$

When a shared IT service is outsourced, the vendor has only one contract with a delegation party that represents the participating organizations (Wood et al. 2016; Yasin 2014). On the other hand, when a shared IT service is insourced, Gov-A becomes a provider to Gov-B (Eidam 2017; Heaton 2013). As discussed earlier, we examine three common regimes for shared IT services. We first proceed to analyze the costsharing regime.

## The Cost-Sharing Regime

In this regime, the governments share the development costs or the prices proportionally to their user populations. Procurement and contractual arrangements in the public sector are bounded by various laws and regulations. For example, when U.S. state or local governments use funds or grants from the federal government, they are required to abide by “Uniform Administrative Requirements, Cost Principles, and Audit Requirements for Federal Awards” outlined by the U.S. Office of Management and Budget (OMB).<sup>14</sup> This regulation stipulates that cost accounting of federal funds be “reasonable and allocable” and “can readily be expressed in terms of dollars or other quantitative measures (total direct costs, … hours of usage, … population served, and the like).” This indicates that when state and local governments develop shared IT services for such federally-supported services as Medicaid or unemployment insurance, they are governed by a cost-sharing regime (Newcombe 2016c).

In addition to federal regulations, the cost-sharing regime is widely adopted because it is not only straightforward and convenient to implement (calculating the amount of shared costs), but also considered a fair arrangement by officials and constituents, making a shared service more politically achievable (Province of Nova Scotia 2014). As such, a number of shared service initiatives adopted this regime. For instance, Michigan and Illinois, which have similar population size, each agreed to bear half of the development costs for the shared Medicaid system (Johnson 2013). Missouri’s Corrections Department has organized a consortium of states to share the cost of replacing legacy offender management systems (Wood et al. 2016). In this regime, if the shared IT service is insourced to Gov-A’s IT function, Gov-A’s surplus $\mathrm { i s } ^ { 1 5 }$

$$
W _ {A} ^ {S I} = \left[ q ^ {S I} - \frac {C ^ {S I}}{\left(N _ {A} + N _ {B}\right)} \right] N _ {A}
$$

Similarly, Gov-B’s surplus is

$$
W _ {B} ^ {S I} = \left[ q ^ {S I} - \frac {C ^ {S I}}{\left(N _ {A} + N _ {B}\right)} - k d \right] N _ {B}
$$

where kd is Gov-B’s unit misfit cost. If the shared service is outsourced, Gov-A and Gov-B are charged a price $p ^ { s o }$ by the vendor that is paid in proportion to their sizes. Gov-A and Gov-B’s surplus are

$$
W _ {A} ^ {S O} = \left[ q ^ {S O} - \frac {p ^ {S O}}{\left(N _ {A} + N _ {B}\right)} - k a \right] N _ {A}
$$

and

$$
W _ {B} ^ {S O} = \left[ q ^ {S O} - \frac {p ^ {S O}}{\left(N _ {A} + N _ {B}\right)} - k _ {B} \right] N _ {B}
$$

The vendor’s profit is $\pi ^ { S O } = p ^ { S O } - C ^ { S O }$ if the shared IT service is outsourced, and 0 otherwise.

We first analyze the governments’ decision on outsourcing of shared IT services in the cost-sharing regime, in which case a shared IT service is outsourced to the vendor when doing so benefits both governments; otherwise, it is developed by Gov-A’s in-house team. The result is summarized in Table A2 in Appendix A. The governments then compare their surplus with that in the non-shared case to determine whether to share IT services. The equilibrium is reported in Lemma A2 in Appendix A and depicted in Figure 3.<sup>16</sup> The following parameter values are used in Figure 3 and subsequent figures unless otherwise noted: $N _ { A } = 1 0 0 , N _ { B } = 7 0 , k = 1 , a = 0 . 7 5$ b = 0.5, = 2, and â = 0.6 Here, the benefits from economies of scales are captured by $\hat { \Delta } _ { 1 } = \phi \Big [ N _ { _ { A } } ^ { ( \beta - 1 ) } - \big ( N _ { _ { A } } + N _ { _ { B } } \big ) ^ { ( \beta - 1 ) } \Big ]$ 2 1 which measures the unit cost savings in the shared case over the non-shared case.<sup>17</sup>

Intuitively, sharing IT services decreases the per unit cost for both governments by pooling their demands (captured in $\hat { \Delta } _ { 1 } ) ;$ on the other hand, doing so incurs additional compatibility costs (ød). Lemma A2 highlights this tradeoff and shows that in equilibrium, they share IT services only when the compatibility cost is not predominantly high (as illustrated in Figure 3). Next, we proceed to examine the profit-center regime.

## The Profit-Center Regime

The profit-center regime is another popular arrangement in the adoption of shared IT services (Morgan 2017). It differs from the cost-sharing regime in that Gov-A charges Gov-B a price $p ^ { S I }$ instead of sharing the development costs proportionally. Many governments favor this regime as it provides a source of additional revenue streams (McCandless 2016; Newcombe

![](/api/attachments/FEDT35PV/fulltext/images/efe6cb2f57487922ccac43cbf2f4f03e531212959440afe69af2ca694e060183.jpg)  
Figure 3. Equilibrium in the Cost-Sharing Regime When a \$ b (Illustrating Lemma A2)<sup>18</sup>

2016a). For instance, Oakland County, Michigan, charges between \$2.5 and 2.75% of the transaction payments to the participating peer governments in its shared system, generating \$17 million in revenues for the county in 2011 (Hanson 2012). Montana and Oregon agreed to allow them “to purchase IT services from the other state’s catalog of IT services” (The State of Montana 2015, p. 16).

When a shared IT service is insourced in the profit-center regime (Case SI), the surplus of Gov-A and Gov-B are

$$
W _ {A} ^ {S I} = q ^ {S I} N _ {A} - C ^ {S I} + p ^ {S I}
$$

and

$$
W _ {B} ^ {S I} = \left(q ^ {S I} - k d\right) N _ {B} - p ^ {S I}
$$

respectively. When the governments outsource the shared service (Case SO), they are charged $p ^ { S O }$ , which is shared in proportion to their respective populations. Hence, in Case SO, the surplus for Gov-A and Gov-B are the same as those in the cost-sharing regime.

Note that acting as a profit center, Gov-A could potentially set a price to capture Gov-B’s entire surplus in the profit-center regime if permitted. Knowing this, Gov-B would be unwilling to share service in the first place unless it is guaranteed the same or more surplus from the non-shared case. This could possibly result in trivial cases where not sharing is always the equilibrium. Thus, to prevent this, we consider that a shared IT service is insourced only if doing so benefits both Gov-A and Gov-B. That is, it is necessary for Gov-A to charge a reasonable and fair price to Gov-B so that the latter voluntarily chooses insourcing.

We summarize the result of the profit-center regime in Table A3 in Appendix A. The equilibrium is characterized in Lemma A3 in Appendix A and illustrated in Figure 4.<sup>19</sup> As in the cost-sharing regime, Lemma A3 shows that the choice to share IT services in the profit-center regime is also determined by the trade-off between the benefits from economies of scale and the compatibility costs.

![](/api/attachments/FEDT35PV/fulltext/images/90a0c31ae46f629fd0ecf019afe28bef423ce87f82d429dc4bdb6f622c57b536.jpg)  
Figure 4. Equilibrium in the Profit-Center Regime when a \$ b (Illustrating Lemma A3)<sup>20</sup>

## Managerial Implications

While Lemma A3 may appear similar to Lemma A2 on the surface, a closer examination of the two regimes reveals several nuanced differences. We here examine (1) how outsourcing decisions are affected by the different regimes, and (2) the strategic implications for the governments and the vendor. The result is summarized in Proposition 1.

## Proposition 1. Given the adoption of shared IT services,

1. Gov-A is better off with the cost-sharing regime than with the profit-center regime when the vendor’s technological advantage is large, that is, $\Delta _ { a } \geq k ( b - d )$

2. The vendor’s outsourcing price and profits in the profitcenter regime are higher than or equal to those in the cost-sharing regime.

3. The shared IT service is more likely to be outsourced under the profit-center regime than under the costsharing regime.

One may expect that the profit-center regime would always benefit Gov-A and encourage insourcing because of its ability to command a price (rather than sharing the costs). However, Proposition 1.1 shows that it is not always the case; the profitcenter regime could instead hurt Gov-A and benefit the vendor when its technological advantage is not small. This is partly due to Gov-A’s dual identity: It can act as either a client or a competitor to the vendor. Specifically, such an ability improves Gov-A’s surplus only when the vendor’s technological advantage (Ä ) is low. In this case, Gov-A can undercut the vendor with a lower price, acting as a competitor. The profit-center regime allows Gov-A to set a surplusmaximizing price to induce Gov-B to insource, to an extent that it is higher than the development costs that would be shared under the cost-sharing regime. As such, this price helps Gov-A extract a greater portion of Gov-B’s surplus.

Interestingly, acting as a profit-center may not benefit Gov-A when the vendor’s advantage is large; in this case, Gov-A becomes a client because it can no longer compete with the vendor. Instead, the vendor is better off in the profit-center regime because it can charge a higher price for the outsourced IT service (see Proposition 1.2). Loosely speaking, this is because the profit-center regime enables Gov-A to compete more aggressively to entice Gov-B to insource (as compared to simply sharing cost). Sometimes, Gov-A is even willing to give up part of its surplus to “subsidize” Gov-B in order to incentivize its choice of insourcing, as doing so can lead to a substantial saving in Gov-A’s misfit cost from using the vendor’s IT service. This intensified competition lowers Gov-A’s “reservation surplus” from the in-house IT service than that under the cost-sharing regime where no such flexibility is available. In simple terms, Gov-A’s in-house option becomes less attractive in the profit-center regime, so the vendor’s price needed to induce outsourcing can be higher than that in the cost-sharing regime. For this reason, it can be easier and more likely to induce outsourcing of a shared IT service in the profit-center regime than in the cost-sharing regime.

Next, we proceed to examine the question: How is the decision to share IT services shaped by different regimes? And which regime provides more incentives for the governments to adopt shared IT services? The result is summarized in Proposition 2.

Proposition 2. When the vendor’s technological advantage is large (small), technically, $\Delta _ { \alpha } \geq k ( b - d ) \left( \Delta _ { \alpha } < k ( b - d ) \right)$ , the adoption of a shared IT service is more (less) likely in the cost-sharing regime than in the profit-center regime.

One might think that the governments are more likely to adopt shared services in the cost-sharing regime, which is often viewed as a fairer arrangement. We show that this is not always true; the profit-center regime can better induce the governments to share IT services when the vendor’s technological advantage (Ä ) is small. In this case, the shared IT service would be insourced to Gov-A in both regimes if adopted, but the profit-center regime allows Gov-A to charge Gov-B a price that increases its own surplus, instead of simply sharing the development costs, making sharing IT service a more attractive option.

On the other hand, such a flexibility may hurt Gov-A when the vendor’s advantage $( \Delta _ { a } )$ is so high that the shared IT service, if adopted, would be outsourced to the vendor. The intuition follows from Proposition 1. Loosely speaking, Gov-A’s inhouse option is less attractive in the profit-center regime because its ability to compete fiercely lowers the reservation surplus it would receive from the in-house IT service. Knowing this, the vendor can compete less aggressively by raising the outsourcing price in this case. This higher outsourcing price reduces the governments’ surplus, making a shared IT service a less attractive option in the profit-center regime than keeping the services separated. As such, the adoption of shared IT service becomes less likely to happen under the profit-center regime than that under the cost-sharing regime.

## The Coordination Regime

Both the cost-sharing and the profit-center regimes assume that the governments are interested in maximizing the surplus of each own. Nevertheless, in contrast to the private sector, cooperation is not uncommon in the public sector. In the example above where the four states decided to build a shared unemployment insurance system, a delegating party was formed to coordinate their decisions (Raths 2012). A similar arrangement was adopted in the case of ReEmployUSA Consortium, which was spearheaded by Mississippi (Douglas 2017b). Furthermore, in many cases, the adoption of shared services explicitly aims to be “mutually beneficial” to participating governments (MFOA 2014; New York State Comptroller 2009). As such, it is important to examine how the governments’ decisions are affected when coordination between them is possible (Cavusoglu et al. 2008).

In this coordination regime, the governments choose to share their IT services when doing so maximizes the total surplus of the two. In effect, this can be viewed analogously to a case in which a central government “bundles” the lower-level governments and makes decisions on behalf of them to maximize the collective surplus of the bundle. On the other hand, under both the cost-sharing and the profit-center regimes, the two governments agree to share IT services only if the surplus of each government increases.

Specifically, when committing to share IT services, if the shared IT service is insourced, the two governments derive a total surplus of

$$
W _ {T} ^ {S I} = q ^ {S I} \left(N _ {A} + N _ {B}\right) - C ^ {S I} - k d N _ {B}
$$

and if the shared IT service is outsourced, the two governments derive a total surplus of

$$
W _ {T} ^ {S O} = q ^ {S O} \left(N _ {A} + N _ {B}\right) - p ^ {S O} - k \left(a N _ {A} + b N _ {B}\right)
$$

The outsourcing decision of the shared IT service in this regime is the same as that in the profit-center regime, which is characterized in Lemma A3. This is because the governments can transfer part of the surplus from one to the other if doing so increases their aggregated surplus. Such a mechanism is essentially similar to the price charged by Gov-A under the profit-center regime. Table A4 in Appendix A summarizes the results.

There is, however, a fundamental difference between the two regimes. In the profit-center regime, Gov-A charges Gov-B a price for the insourced service to maximize its own surplus. In the coordination regime, on the other hand, a transfer can occur in both the insourcing and outsourcing cases but does not need to occur if the two governments’ incentives are congruent. Thus, we can characterize only the total surplus (instead of each individual government’s surplus) in the coordination regime. For this reason, when the governments compare their surplus between the shared and the non-shared service cases, they compare the total surplus, instead of the individual government’s surplus. This leads to Lemma A4 (given in Appendix A), which is depicted in Figure 5. Note that the benefits from economies of scale in the coordination regime is captured by $\begin{array} { r } { \hat { \Delta } _ { 2 } = \frac { \hat { \phi } \left[ N _ { A } ^ { B } + N _ { B } ^ { B } - \left( N _ { A } + N _ { B } \right) ^ { \beta } \right] } { \left( N _ { A } + N _ { B } \right) } } \end{array}$ , instead of $\hat { \Delta } _ { 1 }$ (in the other two regimes), and we can show that $\hat { \Delta } _ { 2 } > \hat { \Delta } _ { 1 }$ for $N _ { A }$ $\geq N _ { B }$ and $0 < \beta < 1$

![](/api/attachments/FEDT35PV/fulltext/images/13770ec8a16151d52a7c9473cadfad6d21ef402885f1319ee4db70b7e4239b89.jpg)  
Figure 5. Equilibrium in the Coordination Regime When a \$ b (Illustrating Lemma A4)

As in the other two regimes, the governments adopt a shared IT service in the coordination regime if the benefits from economies of scale (captured in $\hat { \Delta } _ { 2 } )$ outweigh the compatibility costs. Note that there is an important difference in the coordination regime. Gov-A and Gov-B can coordinate their decisions in such a way that a surplus transfer between the two occurs when sharing IT services results in a loss to one of the two. On the contrary, in the profit-center regime, Gov-A unilaterally decides a price for Gov-B. This difference leads us to examine the next question: Are the two governments’ interests to share the IT services always aligned? We summarize the result in Proposition 3.

Proposition 3. In the absence of coordination, the governments may lack an incentive to voluntarily commit to sharing IT services even if doing so would increase their total surplus when the compatibility cost (ød) is moderate. In particular, this happens

1. In the cost-sharing regime, if (a) $\Delta _ { \alpha } \geq k \left( b - d \right)$ and $\hat { \Delta } _ { 1 } < \psi d \leq \hat { \Delta } _ { 2 } , o r ( b ) 0 < \Delta _ { \alpha } < k \left( b - d \right)$ and $\begin{array} { r } { \hat { \Delta } _ { 1 } - \frac { \left[ k \left( b - d \right) - \Delta _ { \alpha } \right] N _ { B } } { N _ { A } } < \psi d \leq \hat { \Delta } _ { 2 } } \end{array}$

$$
\begin{array}{l} 2. \quad \text { In   the   profit - center   regime,   if } (a) \Delta_ {\alpha} \geq \frac {k [ a N _ {A} + (b - d) N _ {B} ]}{(N _ {A} + N _ {B})} \text { and } \\ \hat {\Delta} _ {1} - \frac {k (a - b + d) N _ {B}}{(N _ {A} + N _ {B})} <   \psi d <   \hat {\Delta} _ {2}, \quad o r \quad (b) \\ k (b - d) \leq \Delta_ {\alpha} <   \frac {k [ a N _ {A} + (b - d) N _ {B} ]}{(N _ {A} + N _ {B})} \quad a n d \\ \hat {\Delta} _ {1} - \frac {[ \Delta_ {\alpha} - k (b - d) ] N _ {B}}{N _ {A}} <   \psi d <   \hat {\Delta} _ {2}, o r (c) 0 <   \Delta_ {\alpha} <   k (b - d) \\ a n d \hat {\Delta} _ {1} <   \psi d <   \hat {\Delta} _ {2}. \end{array}
$$

An important takeaway from Proposition 3 is that the two governments’ interests are not always congruent with respect to sharing their IT services. This is because the benefits from economies of scale are not identical to the governments: The per-unit cost savings from sharing IT services are lower for the government with a larger user base $( \mathrm { i . e . , G o v  – A ) }$ . However, the compatibility costs incurred from sharing are equally borne on a per-user basis between the two governments. When the compatibility cost (ød) is moderately high, the benefits from economies of scale outweigh the compatibility costs for Gov-B but not for Gov-A despite the higher collective surplus. Such a misalignment of interests can result in under-utilization of the shared IT service, in a sense that it inhibits the governments from voluntarily sharing their IT services even if doing so would increase their aggregate surplus. Figure 6 illustrates the regions of under-utilization of shared IT services. From a collective perspective, the two governments should adopt a shared service that would produce a higher aggregated surplus. However, they would not do so because the increase in surplus would not be shared in a way that appropriately incentivizes both governments to choose the shared service.

![](/api/attachments/FEDT35PV/fulltext/images/5341e839e1f5d4bd90092ea144cf038c65b5c6db4c47b0b42678e77947a83ea7.jpg)  
(a) Cost-Sharing Regime

![](/api/attachments/FEDT35PV/fulltext/images/702b6ce6f22d065b793029c892863e57bbd2baa7cb29e8bb6abdd52a34abbae6.jpg)  
(b) Profit-Center Regime  
Figure 6. Under-Utilization of the Shared IT Service When a \$ b (Illustrating Proposition 3)

a way that appropriately incentivizes both governments to choose the shared service.

There are several approaches to mitigate this misalignment and promote the governments to share their IT services. First, to induce Gov-A to share IT services, Gov-B may offer to transfer a part of its surplus to Gov-A, in a similar mechanism as in the profit-center regime. This type of transfer payment is often implemented to facilitate the distribution of surplus and to improve efficiency (SCPRC 2017; Wu et al. 2017). Second, a higher-level of government (e.g., the federal government or a state government over municipalities) may be involved in coordinating the decisions of the two subordinate governments. For example, the higher government may provide monetary grants to compensate for the loss of surplus from coordination. Indeed, the adoption of shared services in Michigan–Illinois and the four southern U.S. states (SCUBI) was facilitated by subsidies from the U.S. federal government (Heaton 2013; Raths 2012). As another example, the ReEmployUSA Consortium received a \$90 million development grant from the U.S. Department of Labor (Douglas 2017a). Similar efforts are also underway among state governments in the U.S. For example, both Connecticut and New York created large matching funds to incentivize the local governments to implement shared IT services (Moody 2018; Towns and Knell 2014).

## Strategic Implications

In this section, we examine the impact of shared service adoption on (1) the vendor’s pricing and profits, and (2) social welfare. This analysis provides insights into how the introduction of a shared service transforms strategic interactions between the governments and the vendor.

## The Vendor’s Pricing and Profit

We start with an analysis of how the decision to share IT services affects the vendor’s price and profit across the different regimes, as summarized in Proposition 4.

Proposition 4. Under the cost-sharing and profit-center regimes, the vendor’s price and profit in the shared service case are not greater than those in the non-shared service case.

We find that sharing IT services may command the vendor to lower its price and profit. This is partly attributed to cost savings from pooling the IT demands of both governments together. Even though sharing IT services incurs additional compatibility costs, it is adopted only when this cost is not predominantly high (Lemmas A2-A4). This forces the vendor to compete more aggressively in the shared service case.

In addition, a more important reason is the vendor’s inability to price-discriminate in the shared case. In the non-shared case, the vendor can set two different prices to induce Gov-A and Gov-B to outsource, in a way that maximizes the surplus extracted from both governments. But in the shared case, the vendor can set only one price for a “bundle,” the shared IT service, in which case the price must be low enough to benefit both governments. Intuitively, this inflexibility inhibits the vendor from charging “personalized” prices to the governments to extract more surplus from them. As such, the vendor’s inability to price-discriminate the shared service decreases its price and profit.

![](/api/attachments/FEDT35PV/fulltext/images/b603d5457d5e66e05a3ce3d40d22814fc7d8de27a156f66cf1c9e4becd735e46.jpg)

![](/api/attachments/FEDT35PV/fulltext/images/13bf96b84de92fc6826dc32f3c938b7af8cba9014f29d33f19a5625631092e5f.jpg)  
Figure 7. Social Welfare (SW) Loss Due to Shared IT Service (Illustrating Proposition 5)

## Social Welfare: Does Sharing IT Services Increase Social Welfare?

Next, we examine the adoption of shared services from a social planner’s perspective. This is important in our setting as governments are expected to play the social planner’s role as well. As we have shown that proper coordination promotes the adoption of shared IT service, the next immediate questions to ask are: What are the implications of such coordination on social welfare? Does it also help achieve a socially optimal outcome? We summarize the results below.

## Proposition 5.

1. Under the cost-sharing and coordination regimes:

a. When $a < b ,$ the governments’ decision to share IT service is also socially optimal.

b. When $a \geq b ,$ the governments’ decision to share IT services may not be socially optimal when $\Delta _ { \alpha }$ and ød are moderate.

## 2. Under the profit-center regime, the governments’ decision to share IT services is always socially optimal.

Proposition 5 shows that the governments’ decision to adopt shared services does not always lead to socially optimal outcomes. In fact, it may hurt social welfare even in the presence of coordination between the governments. Specifically, under both the cost-sharing and the coordination regimes, when the compatibility costs (ød) and the vendor’s advantage (Ä ) are moderate, the governments choose to share IT services. Nevertheless, this leads to lower social welfare than in the non-shared case (in which the vendor serves Gov-B only). This is because even though the governments enjoy a higher surplus from the shared service, the vendor’s profit is significantly lower. In this case, the increase in the governments’ surplus is dominated by the reduction in the vendor’s profit, leading to an overall decrease in social welfare. We illustrate this result in Figure 7.

Interestingly, Proposition 5.2 shows that the decision to share IT services in the profit-center regime is always socially optimal. This is because when $\Delta _ { \alpha }$ is not small, inducing the governments to share IT services under the profit-center regime is more difficult and “selective” (see Proposition 2), in the sense that doing so requires substantial benefits from scale economies to outweigh the compatibility costs. Though this could lead to under-utilization of shared services as compared to the coordination regime (Proposition 3), it ensures that a decision to share IT service not only benefits the governments but also boosts the social welfare.

An important takeaway from Proposition 5 is that though coordination helps promote the adoption of shared services, it may have a detrimental effect on social welfare. Given the increasing interests in government-provided incentives and subsidies for shared services (Moody 2018; Towns and Knell

![](/api/attachments/FEDT35PV/fulltext/images/a182688a168ce5baa2e88b3ce87d052d8c627281731fa71c62fcd2e01288f2dc.jpg)

![](/api/attachments/FEDT35PV/fulltext/images/6673b33d40d4c1759c6060d1de83b6350f142ccc36b53d8b799403f023aa4c30.jpg)  
Figure 8. Upper Bound (UB) of Compatibility Cost (ød) for Shared Service Adoption (Illustrating Proposition 6)<sup>21</sup>

2014), this result calls for more attention to conduct a thorough assessment of the impact on the society and the IT industry as a whole. In the “Endogenizing the Choice of Regime” section, we will present a new setting in which the social planner can choose a regime to maximize social welfare.

## Partnership Strategy

We have shown that the adoption of a shared IT service can boost surplus for the governments and sometimes social welfare too. So, besides the effect of the different regimes, what would also affect the governments’ decision on shared service adoption? The literature identifies economies of scale as a key motive for sharing IT services, which is also explicitly considered in our model. As such, it would be interesting to examine a scale implication on the governments’ decision for shared IT services. Since economies of scale are directly related to user populations in our model, we focus on how the governments’ size influences their incentives and decisions. Specifically, we examine from Gov-A’s perspective on how the likelihood of shared IT service adoption is affected by the size of the peer government (Gov-B). The likelihood is measured by the upper bound of the compatibility cost (ød) for shared service adoption. Intuitively, a higher upper bound implies that the two governments may still find it beneficial to share their IT services despite a higher compatibility cost, thereby entailing a higher likelihood for shared service adoption. We report the result below and illustrate it in Figure 8.

Proposition 6. As the size of Gov-B increases, the likelihood of shared IT service adoption first increases and then decreases (a) in the cost-sharing regime if the vendor’s ad vantage is small, or (b) in the coordination regime. Otherwise, the likelihood of shared IT service adoption monotonically increases as the size of Gov-B increases.

One may expect that a government is more likely to share its IT service with large governments for potentially greater benefits from economies of scale, but interestingly, we find that this is not always the case. First, consider the costsharing regime. On the one hand, as Gov-B’s size increases, the unit cost of the shared IT service decreases, leading to an increase in Gov-A’s benefits from the economies of scale. On the other hand, by committing to share the IT services, Gov-A forgoes the possibility of extracting Gov-B’s surplus from accommodating its IT service in the non-shared case (Case NI), which would happen when the vendor’s advantage is small (see Figure 8(a)). Intuitively, this loss increases as Gov-B’s size increases and eventually dominates the benefits from economies of scale. Thus, the likelihood of shared service adoption does not monotonically increase when the vendor’s advantage is small.

The same result holds for the coordination regime case. Note that the decision to share IT services under the coordination regime is determined by the aggregated surplus rather than that of each individual government. The shared service im proves total surplus if the aggregated benefits from economies of scale outweigh the compatibility costs (see Lemma A4). Here, an increase in Gov-B’s size has two effects. First, as discussed earlier, it benefits Gov-A thanks to a reduction in the unit cost. Second, it decreases Gov-B’s marginal benefits from the economies of scale. When Gov-B is small, the first effect dominates the second; when it becomes larger, the second effect eventually outweighs the first. Thus, the likelihood of shared IT service adoption first increases and then decreases in Gov-B’s size, as depicted in Figure 8(b). These results help explain why we often see real-world examples of large municipalities sharing their IT services with smaller ones (Newcombe 2016b).

Interestingly, the result in the profit-center regime is somewhat different; the likelihood in the adoption of shared IT services monotonically increases in Gov-B’s size. This is because Gov-A can charge a price higher than the development costs to extract part of Gov-B’s surplus when the vendor’s advantage is small. This always leads to a positive net benefit to Gov-A from sharing IT services as the size of Gov-B increases.

## Endogenizing the Choice of Regime

Our model considers an exogenous setting for the contractual arrangements used for shared IT services because, as discussed earlier, the procurement of IT services in the public sector is bounded and governed by a range of legal and regulatory constraints that limit how governments can contract with each other. Next, we consider a change to this setup by modeling the selection of regime as an endogenous decision. Specifically, we examine a super game where an overarching agency (e.g., a central government) acts as a social planner and adopts a regime that maximizes social welfare. Gov-A and Gov-B make their subsequent decisions following the social planner’s choice. We summarize the results of this game below.

Proposition 7. Denote

$$
\begin{array}{l} A _ {1} = \max \left\{\hat {\Delta} _ {1} - \frac {k (a - b + d) N _ {B}}{(N _ {A} + N _ {B})}, \hat {\Delta} _ {1} - \frac {[ \Delta_ {\alpha} - k (b - d) ] N _ {B}}{N _ {A}} \right\}, \\ A _ {2} = \max \left\{\hat {\Delta} _ {2} - \frac {[ \Delta_ {\alpha} - k (b - d) ] N _ {B}}{(N _ {A} + N _ {B})}, \hat {\Delta} _ {2} - \frac {(k a - \Delta_ {\alpha}) N _ {A}}{(N _ {A} + N _ {B})} \right\} \end{array}
$$

1. When the compatibility cost is large, that is, $\psi d > \hat { \Delta } _ { 2 }$ , all regimes yield the same social welfare.

2. When the compatibility cost is small, that $i s ,$ ψd ≤ min $\left\{ \hat { \Delta } _ { 1 } , A _ { 1 } \right\}$

a. All regimes yield the same social welfare when (1) $\Delta _ { a } >$ ka or (2) $\begin{array} { r } { \Delta _ { \alpha } \leq \frac { k \left[ a N _ { A } + \left( b - d \right) N _ { B } \right] } { \left( N _ { A } + N _ { B } \right) } } \end{array}$ and $\begin{array} { r } { \psi d \leq \operatorname* { m i n } \left\{ \operatorname* { m i n } \left\{ \hat { \Delta } _ { 1 } , A _ { 1 } \right\} , \hat { \Delta } _ { 1 } - \frac { \left[ k \left( b - d \right) - \Delta _ { \alpha } \right] N _ { B } } { N _ { A } } \right\} } \end{array}$

b. Otherwise, the social planner prefers the profitcenter and coordination regimes.

3. When the compatibility cost is moderately large, that is, min $\left\{ \hat { \Delta } _ { 2 } , A _ { 2 } \right\} < \psi d \leq \hat { \Delta } _ { 2 }$ , the social planner prefers both the profit-center and the cost-sharing regimes only when max $\left\{ \hat { \Delta } _ { 1 } , A _ { 2 } \right\} < \psi d \leq \hat { \Delta } _ { 2 }$ ; otherwise it chooses only the profit-center regime.

4. When the compatibility cost is moderately small, that is, min $\left\{ \hat { \Delta } _ { 1 } , A _ { 1 } \right\} < \psi d \leq \mathrm { m i n } \left\{ \hat { \Delta } _ { 2 } , A _ { 2 } \right\}$ , the social planner prefers both the coordination and the cost-sharing regimes only when $\left\{ \hat { \Delta } _ { 1 } , A _ { 1 } \right\} < \psi d \leq \mathrm { m i n } \left\{ \hat { \Delta } _ { 1 } , A _ { 2 } \right\}$ otherwise, it chooses only the coordination regime.

Proposition 7 highlights several important findings from the new setting. First, we show that all three regimes generate the same social welfare when the compatibility cost is sufficiently high (see Proposition 7.1); in this case, the non-shared case prevails no matter which regime is adopted. Second, it shows that the profit-center and the coordination regimes can yield higher social welfare than the cost-sharing regime in several cases (see Proposition 7.2). This suggests that the costsharing regime, despite being often viewed as a fair and convenient arrangement by officials and constituents and widely used in practice, can instead likely decrease the social welfare. Third, one might wonder whether coordination would serve as an appropriate mechanism to align the governments’ surplus with the social welfare. We find that it is not always the case (see Proposition 7.3). This is because though coordination helps effectively overcome under-utilization of shared services, it can cause another problem: over-utilization of the shared service. It happens when the governments adopt a shared IT service in a situation where doing so incurs large compatibility costs and demands the vendor to compete fiercely at a very low price, leading to lower social welfare than under the other regimes. Fourth, we also identify situations where higher social welfare is attained when the governments act as a profit center, suggesting that the profitcenter regime can sometimes provide better alignment with social welfare (Proposition 7.3).

Proposition 7 provides an important insight for shared IT service arrangements. As stated above, the regime for shared IT services is often dictated by a higher authority. For example, state and local governments are sometimes mandated to follow the cost-sharing regime for government services under certain federal regulations. Our result shows that such restrictions could undermine the overall social welfare. Therefore, the federal government is advised to revise its cost-accounting regulation for federal grants and offer more flexibility in shared IT service regimes for state and local governments.

## Extensions of the Model

In this section, we consider several variations to the main model to demonstrate that the major insights are robust when some of our assumptions are relaxed or changed.

## Endogenizing the Vendor’s Location

In the current model setup, the fit of the IT service provided by the vendor is exogenous in the sense that its location on the Hotelling line is fixed (Figure 1). Here, we extend the model to a setting where the vendor can strategically position its IT services over the line. Specifically, we consider that the vendor, after observing the locations of Gov-A and Gov-B, can reposition itself to a different location c with a cost of ãc, where ã is the unit cost. After this, the governments make their subsequent decisions as described in the main model. We first analyze governments’ decisions given the vendor’s location c and provide detailed results in Lemma A5.1-A5.4 of Appendix A.

Comparing the new result with that of the main model reveals that the governments’ decisions remain qualitatively the same in this new setting, and only the boundaries conditions are shifted. Next, we proceed to examine the vendor’s optimal strategy when it is allowed to reposition itself on the Hotelling line.

Proposition 8. When the vendor can reposition on the Hotelling line, its strategy is as follows.

1. When ã is not very large, the vendor chooses to reposition at a new location $c ^ { * } = a ~ o r ~ c ^ { * } = b ,$ in which case outsourcing is more likely to be chosen by the governments.

2. When ã is sufficiently large, the vendor chooses to stay at its current location $c ^ { * } = 0$

The vendor can increase the competitiveness of its IT service by either improving the fit (i.e., moving closer to a client) or lowering the price. When the cost of the former is high, that is, it is very costly for the vendor to reposition (i.e., ã is large), then the vendor would simply stay at the original location, that ${ \mathrm { i s } } , c ^ { * } = 0$ , and the result remains identical to that of the main model.

On the other hand, when it is cost-effective to reposition (i.e., ã is not very large), the vendor offers better-fitted IT services to the governments by relocating itself on the Hotelling line, improving its competitiveness. Specifically, when the vendor chooses to relocate to $c ^ { * } = a$ , this is mathematically equivalent to a special case of the main model where $a = 0 .$ . In this case, by repositioning itself to Gov-A’s location, the vendor renders its IT service indifferent from Gov-A’s in-house service in the fit (horizontal) dimension, that is, both are equally fitted (unfitted) to Gov-A and Gov-B. Since the misfit costs are now identical for insourced and outsourced IT services, the vendor can leverage its technological advantage to undercut Gov-A to capture the entire demand, leading to outsourcing being the only strategy in equilibrium (both in the shared and the non-shared service cases).

Similarly, the vendor may relocate to $c ^ { * } = b ,$ thus offering an IT service that perfectly fits Gov-B. In this case, the distance between Gov-B and the vendor is 0, violating one of the assumptions in the main model: $b > a / 2$ Note that this assumption is to ensure that insourcing to Gov-A is a feasible option for Gov-B. Therefore, when $c ^ { * } = b .$ , Gov-B would always prefer outsourcing. In other words, Case (N,I) is no longer a possible equilibrium, but this does not change our key results qualitatively. In both of the above cases, the vendor’s repositioning expands the parameter regions for outsourcing.

## Economies of Scale in the Non-Shared Case

Our main model posits that the vendor gains economies of scale from developing and hosting the IT systems of both governments only for the shared service case. It could be possible, however, that this also occurs from hosting both of the separate IT services in the non-shared case, though perhaps at a different magnitude. As such, we extend our model to consider a case where the vendor and Gov-A can also gain economies of scale when hosting separate IT services from both governments in the non-shared case, with the following cost function:

$$
C _ {T} ^ {N j} = \alpha^ {j} \left(q ^ {N j}\right) ^ {2} \left(N _ {A} + N _ {B}\right) + \phi \left(N _ {A} + N _ {B}\right) ^ {\delta \beta}
$$

where $j ~ \in ~ \{ I , ~ O \}$ and $1 ~ \leq ~ \delta < ~ \overline { { \delta } } ,$ and ¯ä is such that $\left( N _ { _ A } + N _ { _ B } \right) ^ { \delta \beta } = N _ { _ A } ^ { \beta } + N _ { _ B } ^ { \beta }$ This captures the notion that economies of scale are also gained in the non-shared case, but to a lesser extent than in the shared case. The governments decisions in the non-shared case are characterized in Lemma A6 and Table A5 in Appendix A. We further examine the equilibria under the three regimes. For ease of exposition, we summarize the analysis result below, while the details are provided in Lemma A7.1-A7.3 in Appendix A. We also illustrate the result of the cost-sharing regime in Figure 9.<sup>22</sup>

![](/api/attachments/FEDT35PV/fulltext/images/5d2e42471f0d4a258c64632803006cccf16f2be14d20c70a06fba63220c6e09d.jpg)  
Figure 9. Equilibrium in the Cost-Sharing Regime When a \$ b (Illustrating Proposition 9)

Proposition 9. If economies of scale are also obtained in the non-shared case, in equilibrium,

1. The regions for the cases NI and NO either stay the same or expand in the non-shared case.

2. Inducing the adoption of shared IT services becomes more difficult in all three regimes.

Intuitively, the fact that the vendor and Gov-A can gain economies of scale from hosting separate IT services reduces the costs when either one serves both governments (i.e., Cases NI and NO). As a result, the regions for these two cases expand. Since the non-shared case becomes more cost-effective, the relative cost advantage in the shared service case is now smaller. As such, the equilibrium region for shared services shrinks, as shown in Figure 9. However, this change only shifts some of the boundary conditions as compared to the main model, and the core insights are not affected qualitatively.

## IT Capability for Gov-B

Our model assumes that Gov-B lacks an adequate IT capability to develop its own IT service (or it is economically infeasible to do so). As such, Gov-B would have to resort to either Gov-A and the vendor for its IT needs. While this assumption appropriately reflects many cases where some participating agencies do not have a sizable in-house IT group (e.g., many small municipal governments), there are also situations wherein all participating agencies are equipped with adequate IT capabilities. We here relax this assumption by endowing Gov-B with IT development capability such that it is capable of developing its own IT services just as Gov-A is.

For this purpose, we denote $\alpha ^ { A }$ and $\boldsymbol { \alpha } ^ { B }$ as the measures of technological capabilities of Gov-A and Gov-B, respectively.<sup>23</sup> Based on the common notion that larger organizations tend to have higher IT capabilities than small ones, we let $0 < \alpha ^ { o } < \alpha ^ { 4 } < \alpha ^ { B } , ^ { 2 4 }$ indicating that Gov-A’s superior capability renders a cost advantage over Gov-B. The governments’ decisions are characterized in Lemma A8 and Table A6 in Appendix ${ \mathrm { A . } } ^ { 2 5 }$ For brevity, we summarize the result in Proposition 10 and also illustrate the case of profit-center regime in Figure 10. Note that $\Delta _ { \alpha }$ captures the vendor’s relative technological advantage over Gov-A (as in Lemma A1), and $\Delta _ { \alpha } ^ { A B }$ captures Gov-A’s advantage over Gov-B.

![](/api/attachments/FEDT35PV/fulltext/images/9b8c8dfa522bf84e780899c5b2051b14d87c3334cd14949d1d9b99cad96fcd89.jpg)  
Figure 10. Equilibrium in the Profit-Center Regime When a \$ b (Illustrating Proposition10)

Proposition 10. Denote $\begin{array} { r } { \Delta _ { \alpha } = \frac { \left( \alpha ^ { A } - \alpha ^ { O } \right) } { 4 \alpha ^ { O } \alpha ^ { A } } } \end{array}$ and $\begin{array} { r } { \Delta _ { \alpha } ^ { \mathcal { A } B } = \frac { \left( \alpha ^ { B } - \alpha ^ { A } \right) } { 4 \alpha ^ { A } \alpha ^ { B } } } \end{array}$ When Gov-B also has an IT capability,

1. If Gov-A’s technological advantage over $G o \nu \ – B$ is sufficiently high, that is, $\Delta _ { \alpha } ^ { A B } > k d$ , the result reduces to the same as the main model.

2. If Gov-A’s technological advantage over Gov-B is not sufficiently high, that is, $\Delta _ { \alpha } ^ { A B } \leq k d$

a. Gov-B will insource to its own in-house unit when $\Delta _ { \alpha } \leq k b - \Delta _ { \alpha } ^ { \ A B }$

b. The regions for shared IT service either remain the same or expand (i.e., the upper bound of the compatibility cost, ød, becomes larger)

Proposition 10 highlights three important results. First, the new game is essentially identical to the main model when Gov-A’s technological advantage over Gov-B is sufficiently high, or technically, $\Delta _ { \alpha } ^ { A B } > k d$ . Second, since Gov-B now has a more active role, when $\Delta _ { \alpha } ^ { A B }$ is not very large, Gov-B may choose its own in-house team instead of resorting to the vendor or Gov-A, resulting in two new non-shared cases in equilibrium: (1) Case OB, where Gov-A outsources and Gov-B develops in-house; and (2) Case AB, where both Gov-A and Gov-B develop individually with their respective in-house teams. Third, the region for shared service cases expands, as shown in Figure 10. This is because empowering Gov-B with IT capability intensifies the competition in the non-shared case and decreases Gov-A’s surplus in certain non-shared cases. This makes it more likely for the governments to share the IT services. As shown in Lemma A8 and illustrated in Figure 10, these changes simply affect the boundaries of the equilibrium rather than our core insights.

## Extension to the Coordination Regime with Tax Revenues

The three regimes examined in the “Model Analysis” section only consider the governments’ surplus in decision makings. Since a government has a power to collect tax, it might aim to maximize the sum of its surplus and tax revenues from the vendor’s profit. Here, we extend the coordination regime by accounting for tax revenues from the vendor. Formally, we consider that the governments can impose a tax rate of on the vendor’s profit, where $\rho \in [ 0 , 1 )$ , and their total surplus is

$$
\begin{array}{c} W _ {T} ^ {S O} = q ^ {S O} \left(N _ {A} + N _ {B}\right) - p ^ {S O} \\ - k \left(a N _ {A} + b N _ {B}\right) + \rho \left(p ^ {S O} - C ^ {S O}\right) \end{array}
$$

The vendor’s profit becomes $\pi ^ { S O } = ( 1 - \rho ) ( p ^ { S O } - C ^ { S O } )$ and the social welfare is $S W ^ { S O } = W _ { T } ^ { S O } + \pi ^ { S O }$ . Intuitively, this setting is the same as the coordination regime at $\rho = 0 ;$ , and when $\rho$ approaches 1, $W _ { T } ^ { S O }$ increases asymptotically to the overall social welfare $S W ^ { S O }$ (and $\pi ^ { S O }$ diminishes asymptotically to zero).<sup>26</sup> The objective is to maximize $W _ { T } ^ { S O }$ , which includes both the governments’ surplus and the tax from the vendor’s profit.

Our analysis finds that the inclusion of the tax revenues in the governments’ optimization problem does not change the result. Under this regime, the vendor raises its price accordingly in response to the tax imposed, effectively canceling out the effect from taxation. We summarize the result in Proposition 11.

Proposition 11. Even with the tax revenues from the vendor, the equilibrium strategies of Gov-A and Gov-B remain the same as those in the coordination regime.

## Additional Benefits from Shared IT Services

The main model regards cost savings from economies of scale as a major benefit from a shared service. Besides this, sharing the IT services may bring additional benefits to governments, such as improved services to citizens and enhanced crossagency collaboration that can improve operational efficiency. In a survey by Government Technology and Oracle, “improved services” and “desire to collaboration” are listed as the second and the third biggest consideration for shared services, respectively (Government Technology 2017). Such benefits could be accrued to all agencies participating in a shared IT service arrangement.

We capture this extra benefit from the shared IT service by multiplying ë, where ë > 1, to the governments’ marginal valuation for quality when they choose to share. For brevity, we illustrate the impact of this additional benefit in our analysis under the cost-sharing regime below. The results for the other regimes are qualitatively the same. Specifically, if the shared IT service is insourced, Gov-A’s surplus is

$$
W _ {A} ^ {S I} = \left[ \lambda q ^ {S I} - \frac {C ^ {S I}}{\left(N _ {A} + N _ {B}\right)} \right] N _ {A}
$$

and Gov-B’s surplus is

$$
W _ {B} ^ {S I} = \left[ \lambda q ^ {S I} - \frac {C ^ {S I}}{\left(N _ {A} + N _ {B}\right)} \right] N _ {B}
$$

If the shared service is outsourced, Gov-A and Gov-B’s surplus are

$$
W _ {A} ^ {S O} = \left[ \lambda q ^ {S O} - \frac {p ^ {S O}}{\left(N _ {A} + N _ {B}\right)} - k a \right] N _ {A}
$$

and

$$
W _ {B} ^ {S O} = \left[ \lambda q ^ {S O} - \frac {p ^ {S O}}{\left(N _ {A} + N _ {B}\right)} - k a \right] N _ {B}
$$

respectively. We analyze the governments’ decision on outsourcing in the cost-sharing regime under the new setting. For simplicity, we report the details in Lemma A9 (in Appendix A) and summarize the result below.

Proposition 12. With additional benefits from shared IT service, the regions for shared IT services expand, and so does the region for outsourcing of shared IT services.

Intuitively, when sharing IT services brings more benefits by $\lambda ,$ the governments are more incentivized to share their IT services, as shown in Lemma A9. Technically, the upper bound of ød $( \mathrm { i } . \mathrm { e } . , A _ { 3 }$ in Lemma A9) is higher in the new setting than in Lemma A2. Interestingly, we find that the outsourcing of shared IT services is also more likely to occur in this new setting, or technically, $\begin{array} { r } { \frac { k a } { \lambda ^ { 2 } } < k a \mathrm { \ f o r } \lambda > 1 } \end{array}$ . This is because the difference in quality between the outsourced and insourced services $( \mathrm { i . e . , } \lambda ( q ^ { S O } - q ^ { S I } ) )$ increases, owing to ë > 1. As such, the outsourcing becomes more attractive and likely to occur in equilibrium.

## Discussion and Conclusion

In this paper, we study a unique practice for enterprise IT systems in the public sector: shared IT services. Multiple governments, which provide similar services to their residents yet do not compete with each other, collectively share IT services for internal operations or delivery of public services. By pooling separate IT resources, they aim to save costs in developing and operating IT services and to augment their bargaining power vis-à-vis private-sector IT vendors. This new phenomenon poses challenges to IT industries, to which governments are one of the largest customers.

Our study produces several intriguing findings that would enrich IS theories and provide ample managerial implications for IT professionals and policy-makers. First, while charging a surplus-maximizing price seems to be a lucrative option compared to a simple cost-sharing structure, we find that a government does not always benefit by acting as a profit center. This is because doing so intensifies the competition and lowers the government’s “reservation surplus” from the in-house IT service, leading the vendor to command more surplus by charging a higher outsourcing price. As such, we offer an interesting insight that the vendor may prefer the profit-center regime because it could charge a higher price and obtain higher profits. Second, in order to incentivize the governments to share IT services, officials sometimes need to devise an effective mechanism to make sure that the interests of participating governments are congruent. We find that if each government pursues its own self-interest, a shared IT service may not be adopted even if doing so would boost their collective surplus. This provides insights into why shared services are more prevalent among state and federal agencies (where coordination exists) than at city and county levels (where coordination is absent or weak) (Newcombe 2016b). Hence, we propose that, in order to incentivize the adoption of a shared service, higher-level governments should consider providing financial incentives such as setting up a matching fund to sub-level governments for shared IT systems. This suggestion is echoed by several recent initiatives established by the federal government (Douglas 2017a) and major states such as New York and Connecticut (Moody 2018; Towns and Knell 2014).

Third, although coordination promotes the adoption of shared IT services, the governments are advised to assess this method with caution as it could be done at the cost of significantly lower profits to the vendor, leading to an overall lower social welfare. Importantly, we find that from the policy-makers perspective, they may want to choose the profit-center regime because the adoption of shared services in this regime always leads to socially optimal outcomes. Finally, we find that the likelihood of shared service adoption also depends on sizes of participating governments, whose effects can differ across the regimes. An intuition suggests that a government is more likely to seek a partnership with large ones for potentially greater economies of scale, we find that this is not always true. Specifically, we show that that a large government is more likely to form shared IT services with peers of smaller sizes under the cost-sharing and the coordination regimes. The result highlights the delicate differences between the regimes and provides managerial insights into the identification of partners under different arrangements.

There are multiple venues for IS researchers to extend this model and to further examine the practices of shared IT services in the public sector. One of the limitations of this study is that our model primarily considers a non-cooperative game setting among the two governments and the vendor; however, we acknowledge that cooperative behaviors among them are possible in practice. Future research may extend our study by considering issues such as coalition, bargaining, or communications between governments, all of which are crucial components in cooperative games. Based on our model, future researchers can empirically examine what factors facilitate or inhibit the formation of shared IT services. Researchers can also consider a case in which users experience positive network effects from shared government services. An example is a shared payment system for public transportation services (bus, train, or subway) in which transit providers in different jurisdictions (e.g., Washington D.C., Virginia, and Maryland) share a single payment system for transit riders. Additionally, the adoption of shared IT services could be impacted by other factors such as governments budgets, security risk, etc. These interesting perspectives certainly warrant further studies. Last, our model considers a single period, and like private-sector firms, governments may also face the choice of switching vendors in the long term, so future study may extend it to a multi-period setting and examine the role of switching cost in the game.

## Acknowledgments

The authors would like to thank the senior editor, H. R. Rao, the associate editor, and the anonymous reviewers for their constructive comments and suggestions. The authors also thank Jianqing Chen and participants at the 2014 INFORMS Conference on Information Systems and Technology, the 2014 INFORMS Annual Meeting, the 2014 Workshop on Information Technologies and Systems, and the 2019 China Workshop on Economics of Information Systems Theory for their helpful feedback.

## References

Ang, S., and Straub, D. W. 1998. “Production and Transaction Economies and IS Outsourcing: A Study of the U. S. Banking Industry,” MIS Quarterly (22:4), pp. 535-552.

August, T., Niculescu, M. F., and Shin, H. 2014. “Cloud Impli cations on Software Network Structure and Security Risks,” Information Systems Research (25:3), pp. 489-510.

Baicker, K. 2005. “The Spillover Effects of State Spending,” Journal of Public Economics (89:2-3), pp. 529-544.

Banker, R. D., Khosla, I., and Sinha, K. K. 1998. “Quality and Competition,” Management Science (44:9), pp. 1179-1192.

Besley, T. and Case, A. 1995. “Incumbent Behavior: Vote-Seeking, Tax-Setting, and Yardstick Competition,” American Economic Review (85:1), pp. 25-45.

Breton, A., and Wintrobe, R. 1975. “The Equilibrium Size of a Budget-Maximizing Bureau: A Note on Niskanen’s Theory of Bureaucracy,” Journal of Political Economy (83:1), pp. 195-207.

Cachon, G., and Harker, P. T. 2002. “Competition and Outsourcing with Scale Economies,” Management Science (48:10), pp. 1314-1333.

Cao, Q., Geng, X., and Zhang, J. 2015. “Strategic Role of Retailer Bundling in a Distribution Channel,” Journal of Retailing (99:1), pp. 50-67.

Cavusoglu, H., Cavusoglu, H., and Zhang, J. 2008. “Security Patch Management: Share the Burden or Share the Damage?,” Management Science (54:4), pp. 657-670.

Cavusoglu, H., Raghunathan, R., and Cavusoglu, H. 2009. “Configuration of and Interaction Between Information Security Technologies: The Case of Firewalls and Intrusion Detection Systems,” Information Systems Research (20:2), pp. 198-217.

Chambers, C., Kouvlis, P., and Semple, J. 2006. “Quality-Based Competition, Profitability, and Variable Costs,” Management Science (52:12), pp. 1884-1895

Chen, P.-Y., and Wu, S.-Y. 2013. “The Impact and Implications of On-Demand Services on Market Structure,” Information Systems Research (24:3), pp. 750-767.

Cheng, H. K., Bandyopadhyay, S., and Guo, H. 2011. “The Debate on Net Neutrality: A Policy Perspective,” Information Systems Research (22:1), pp. 60-82.

Cheng, H. K., and Koehler, G. J. 2003. “Optimal Pricing Policies of Web-Enabled Application Services,” Decision Support Systems (35:3), pp. 259-272.

Choudhary, V., and Vithayathil, J. 2013. “The Impact of Cloud Computing: Should the IT Department Be Organized as a Cost Center or a Profit Center?,” Journal of Management Information Systems (30:2), pp. 67-100.

Clemons, E., and Gu, B. 2003. “Justifying Contingent Information Technology Investments: Balancing the Need for Speed of Action with Certainty Before Action,” Journal of Management Information Systems (22:2), pp. 11-48.

Clydebuilt Business Solutions. 2012. Developing In-House vs. Off the Shelf (available at http://www.clydebuiltsolutions.com/wpcontent/uploads/2012/05/Inhouse-VS-Off-the-Shelf-May.pdf; accessed May 24, 2018).

Cordell, C. 2018. Beth Angerman on the New Shared Services Office and Tech Standards in Government (available at https://www.fedscoop.com/beth-angerman-shared-servicesfedscoop-qa/; accessed April 11, 2018).

d’Aspremont, C., Gabszewicz, J. J, and Thisse, J. F. 1979. “On Hotelling’s Stability in Competition,” Econometrica (47:5), pp. 1145-1150.

Dewan, S. 1996. “Pricing Computer Services under Alternative Control Structures: Tradeoffs and Trends,” Information Systems Research (7:3), pp. 301-307.

Dewan, S., and Mendelson, H. 1990. “User Delay Costs and Internal Pricing for a Service Facility,” Management Science (36:12), pp. 1502-1517.

Douglas, T. 2017a. Efficiency in Numbers as States Take Unemployment Insurance to the Cloud (available at http://www.govtech.com/computing/Efficiency-in-Numbers-as-States-Take-Unemployment-Insurance-to-the-Cloud.html; accessed May 25, 2018).

Douglas, T. 2017b. Maine Officially Becomes Next State to Join Unemployment Insurance Cloud Consortium (available at http://www.govtech.com/civic/Maine-Officially-Becomes-Next-State-To-Join-Unemployment-Insurance-Cloud-Consortium.html; accessed May 25, 2018).

Eidam, E., Knell, N., Harrison, L., Mulholland, J., Newcombe, T., Miller, B, McCauley, R., Douglas, T., and Quaintance, Z. 2017. Digital Counties Survey 2017: Winners Focus on Knowing When, How to Introduce New Tech (available at http://www.govtech.com/dc/articles/Digital-Counties-Survey-2017-Results.html; accessed April 12, 2018).

Ellis, C. 2018. State’s New Unemployment Claims System Cont i n u e s t o F r u s t r a t e M a i n e r s ( a v a i l a b l e a t https://www.pressherald.com/2018/01/28/state-unemploymentsystem-continues to-frustrate-mainers/; accessed May 25, 2018).

Erlanger, L. 2018. Shared Services Under Trump Could Lead to Fewer Systems, Greater Security (available at https://fedtechmagazine.com/article/2017/06/shared-servicesunder-trump-could-lead-fewer-systems-greater-security; accessed April 11, 2018).

Flinders, K. 2014. Why IT Outsourcing Is Increasingly Blamed for IT Failures at Banks (available at https://www. computerweekly.com/news/2240214081/Why-IT-outsourcing-isincreasingly-fingered-for-IT-failures-at-banks; accessed May24, 2018).

GCN. 2014. Southeast States Share Unemployment Benefits System (available at http://gcn.com/articles/2014/01/29/stateunemployment-systems.aspx; accessed May 24, 2018).

Geng, X., Stinchcombe, M. B, and Whinston, A. B. 2005. “Bundling Information Goods of Decreasing Value,” Management Science (51:4), pp. 662-667.

Goldstein, P. 2016. 2017 Budget Boosts IT Spending to \$89.9 Billion, Expands U.S. Digital Service (available at https://fedtechmagazine.com/article/2016/02/2017-budgetboosts-it-spending-899-billion-expands-us-digital-service; accessed April 11, 2018).

Goldstein, P. 2018. Trump Administration Highlights the Importance of Shared Services (available at https://fedtechmagazine. com/article/2017/09/trump-administration-highlights-importanceshared-services; accessed April 11, 2018).

Goo, J., Kishore, R., Nam, K., Rao, H. R., and Song, Y. 2007. “An Investigation of Factors that Influence the Duration of IT Outsourcing Relationships,” Decision Support Systems (42), pp. 2107-2125.

Goo, J., Kishore, R., Rao, H. R., and Nam, K. 2009. “The Role of Service Level Agreements in Relational Management of Information Technology Outsourcing: An Empirical Study,” MIS Quarterly (33:1), pp. 119-145.

Goodrich, S. 2017. 6 Challenges to Implementing Shared Services (available at https://www.federaltimes.com/opinions/2017/05/16 6-challenges-to-implementing-shared-services-commentary/; accessed April 11, 2018).

Government Technology. 2017. Survey on Shared Services in State and Local Government (available at http://www.oracle. com/us/industries/046114.pdf; accessed February 16, 2019).

Guo, H., Cheng, H. K., and Bandyopadhyay, S. 2012 “Net Neutrality, Broadband Market Coverage, and Innovation at the Edge,” Decision Sciences (43:1), pp. 141-172.

Halstead, S. 2017. The Pros and Cons of an In-House or Outsourced E-Commerce Solution (available at https://info. fastspring.com/blog/the-pros-and-cons-of-an-in-house-oroutsourced-e-commerce-solution; accessed May 24, 2018).

Hanson, W. 2012. Oakland County, Mich., Taking Shared Services National (available at http://www.govtech.com/e government/Oakland-County-Mich-Taking-Shared-Services-National.html; accessed May 24, 2018).

Heaton, B. 2013. Michigan and Illinois Get Two Medicaid Systems for the Price of One (available at http://www.governing.com/ blogs/view/gov-michigan-illinois-create-two-medicaidsystems.html; accessed May 24, 2018).

Hurt, K. 2011. RKV Successfully Implements NCOMS (available at http://rkvtechnologies.com/missouris-department-of-corrections/; accessed April 12, 2018).

Janssen, M., and Joha, A. 2006. “Motives for Establishing Shared Service Centers in Public Administrations,” International Journal of Information Management (26:1), pp. 102-115.

Johnson, S. R. 2013. Two for the Price of One: Michigan, Illinois Collaboration on Medicaid IT System Saves on Cost (available at http://www.modernhealthcare.com/article/20131019/ MAGAZINE/ 310199951; accessed May 24, 2018).

Jones, R., and Mendelson, H. 2011. “Information Goods vs. Industrial Goods: Cost Structure and Competition,” Management Science (57:1), pp. 164-176.

Knell, N. 2017. IT Spending in State and Local Government: What Does 2017 Hold? (available at http://www.govtech.com/ budget-finance/IT-Spending-in-State-and-Local-IT-What-Does-2017-Hold.html; accessed April 11, 2018).

Lacity, M. C., and Willcocks, L. P. 1998. “An Empirical Investigation of Information Technology Sourcing Practices: Lessons from Experience,” MIS Quarterly (22:3), pp. 363-408.

Levina, N., and Ross, J. W. 2003. “From the Vendor’s Perspective: Exploring the Value Proposition in Information Technology Outsourcing,” MIS Quarterly (27:3), pp. 331-364.

Li, X., and Chen, Y. 2012. “Corporate IT Standardization: Product Compatibility, Exclusive Purchase Commitment, and Competition Effects,” Information Systems Research (23:4), pp. 1158-1174.

Loh, L., and Venkatraman, N. 1992. “Diffusion of Information Technology Outsourcing: Influence Sources and the Kodak Effect,” Information Systems Research (3:4), pp. 334-358.

Mader, D., and Roth, T. 2015. Scaling Implementation of Shared Services (available at https://obamawhitehouse.archives.gov/ blog/2015/10/22/scaling-implementation-shared-services; accessed April 11, 2018).

Marquis, A. 2018. The Difference Between Outsourcing & Insourcing (available at http://smallbusiness.chron.com/differencebetween-outsourcing-insourcing-32400.html; accessed April 15, 2018).

Maryland State Rifle and Pistol Association. 2019. A Guide to Obtaining The Maryland Handgun Qualification License (available at https://www.msrpa.org/pdf/document11\_92.pdf; accessed March 20, 2019).

McCandless, J. 2016. Idaho Sells Home-Grown Unemployment System to Iowa and Vermont (available at http://www.govtech. com/health/Idaho-Sells-Home-Grown-Unemployment-System-to-Iowa-and-Vermont.html; accessed May 28, 2018).

McCubbins, M. D., Noll, R. G., and Weingast, B. R. 1987. “Administrative Procedures as Instruments of Political Control,” Journal of Law, Economics, and Organization (3:2), pp. 243-277.

MDHHS. 2013. Michigan and Illinois Announce Interstate Technology Modernization Partnership (available at http:// www.michigan.gov/mdhhs/0,5885,7-339--310082--,00.html; accessed April 16, 2018).

Meeken, Z. 2013. The Pros and Cons of Developing Your Own Software Versus Outsourcing (available at http://www.business. org/it/the-pros-and-cons-of-developing-your-own-softwareversus-outsourcing/; accessed May 24, 2018).

Mendelson, H. 1985. “Pricing Computer Services: Queueing Effects,” Communications of the ACM (28:3), pp. 312-321.

MeriTalk. 2018. NASCIO Top 10 Shows State CIOs Fall in Love All Over Again (available at https://meritalkslg.com/ articles/nascio-top-10-shows-state-cios-fall-in-love-all-overagain/; accessed May 23, 2018).

Mew, B. 2018. Learning To Share—Why with Collective Will, Direction and Agile Delivery, Shared Services Can Revolutionise Government (available at https://government.diginomica. com/2018/02/07/learning-share-collective-will-direction-agiledelivery-shared-services-can-revolutionise-government/; accessed April 11, 2018).

MFOA. 2014. Shared Services in Ontario’s Local Public Sector: L o c a l i z i n g A c c o u n t a b i l i t y ( a v a i l a b l e a t http://ryersontownship.ca/wp-content/uploads/2016/09/MFOA-Guide\_to\_shared\_services-Ontario.pdf; accessed May 24, 2018).

Miller, B. 2017. Oregon DMV Buys FAST Software to Replace Systems Older than Mark Zuckerberg (available at http://www. govtech.com/biz/Oregon-DMV-Buys-FAST-Software-to-Replace-Old-Systems.html; accessed May 25, 2018).

Miller, J. 2017. Trump Signs Cyber EO Promoting IT Modernization, Shared Services (available at https://federalnewsradio. com/cybersecurity/2017/05/trump-signs-cyber-eo-promoting-itmodernization-shared-services/; accessed June 1, 2018).

Moody, R. 2018. Cuomo to Expand Shared Services to Further Property Taxes in Wake of Tax Cuts & Jobs Act (available at https://www.hudsonvalley360.com/article/cuomo-expand-sharedservices-further-property-taxes-wake-tax-cuts-jobs-act-0; accessed April 12, 2018).

Moorthy, S. K. 1988. “Product and Price Competition in a Duopoly,” Marketing Science (7:2), pp. 141-168.

Morgan, J. 2017. Municipal Shared Services Agreements for Information Technology (available at https://www.cio.com/ article/3196248/leadership-management/municipal-sharedservices-agreements-for-information-technology.html#\_edn1; accessed April 2018).

NASCIO. 2017. A New Engine Driving Innovation in State Technology (available at https://www.nascio.org/Portals/0/ Publications/Documents/2017/NASCIO\_2017\_State\_CIO Survey.pdf?ver=2017-10-25-174540-510; accessed May 24, 2018).

Nechyba, T. J. 1997. “Local Property and State Income Taxes: The Role of Interjurisdictional Competition and Collusion,” Journal of Political Economy (105:2), pp. 351-384.

New York State Comptroller. 2009. Local Government Management Guide: Shared Services in Local Government (available at https://www.osc.state.ny.us/localgov/pubs/lgmg/ sharedservices.pdf; accessed May 24, 2018).

Newcombe, T. 2016a. Assessing Shared IT Services Today (available at http://www.govtech.com/dc/Assessing-Shared-IT-Services-Today.html; accessed April 11, 2018).

Newcombe, T. 2016b. Digital Communities Special Report: Time to Share (available at http://www.govtech.com/dc/articles/ Digital-Communities-Special-Report-Time-to-Share.html; accessed May 24, 2018).

Newcombe, T. 2016c. 3 Best Practices for Successful Shared IT Services Programs (available at http://www.govtech.com/dc/ articles/3-Best-Practices-for-Successful-Shared-IT-Services-Programs.html; accessed February 16, 2019).

Niskanen, W. A. 1968. “Nonmarket Decision Making: The Peculiar Economics of Bureaucracy,” American Economics Review (58:2), pp. 293-305.

O’Brien, A. 2018. New Unemployment System Still Frustrating Laid-Off Workers (available at https://freepressonline.com/

Content/Features/Andy-O-Brien-Archives/Article/New-Un e mp l o yme n t - S ys t em-Still-Fru stratin g-Laid -Off-Workers/52/777/56960; accessed May 25, 2018).

Pick, R. A., and Whinston, A. B. 1989. “A Computer Charging Mechanism for Revealing User Preferences Within a Large Organization,” Journal of Management Information Systems (6:1), pp. 87-100.

Pincus, E. 2018. Governments, Data Have Roles to Play in Citizen Employment (available at http://www.govtech.com/workforce/ Go vern men ts-Data-Have-Ro l e s -to -P lay-in -Citizen - Employment.html; accessed May 24, 20018).

Province of Nova Scotia. 2014. Regional Service Delivery Cost Sharing Guide (available at http://novascotia.ca/dma/pdf/mun-RSD-cost-sharing-guide.pdf; accessed May 24, 2018).

Rao, H. R., Nam, K., and Chaudhury, A. 1996. “Information Systems Outsourcing,” Communications of the ACM (39:7), pp. 27-29.

Raths, D. 2012. Shared and Regional Services Are on the Rise (available at http://www.govtech.com/policy-management/ Shared-and-Regional-Services-Are-on-the-Rise.html; accessed May 24, 2018).

Raths, D. 2015. The Promise and Pain of Building a Regional Justice Information Network (available at http://www.govtech. com/The-Promise-and-Pain-of-Building-a-Regional-Justice-Information-Network.html; accessed May 24, 2018).

Rich, S. 2013. Massachusetts Municipalities Share IT Infrastructure in the Cloud (available at http://www.govtech.com/ computing/Massachusetts-Municipalities-Share-IT-Infrastructurein-the-Cloud.html; accessed May 24, 2018).

Richmond, W. B., Seidmann, A., and Whinston, A. B. 1992. “Incomplete Contracting Issues in Information Systems Development Outsourcing,” Decision Support Systems (8:5), pp. 459-477.

Ross, J. W., Vitale, M. R., and Beath, C. M. 1999. “The Untapped Potential of IT Chargeback,” MIS Quarterly (23:2), pp. 215-237.

Ross, R. 2011. Two Different Worlds: The Public and Private Sectors (available at http://spectator.org/articles/37541/twodifferent-worlds-public-and-private-sectors; accessed May 24, 2018).

Schulz, V., and Brenner, W. 2010. “Characteristics of Shared Service Centers,” Transforming Government: People, Process, and Policy (4:3), pp. 210-219.

SCPRC. 2017. Transfer Payment Guideline to Promote Equal Development (available at http://english.gov.cn/policies/ latest\_releases/2015/02/02/content\_281475049185334.htm; accessed April 13, 2018).

Singh, C., Shelor, R., Jiang, J., and Klein, G. 2004. “Rental Software Valuation in IT Investment Decisions,” Decision Support Systems (38:1), pp. 115-130.

Smith, M. A., Mitra, S., and Narasimhan, S. 1998. “Information Systems Outsourcing: A Study of Pre-Event Firm Characteristics,” Journal of Management Information Systems (15:2), pp. 61-93.

Susarla, A. 2012. “Contractual Flexibility, Rent Seeking, and Renegotiation Design: An Empirical Analysis of Information Technology Outsourcing Contracts,” Management Science (58:7), pp. 1388-1407.

Susarla, A., Barua, A., and Whinston, A. B. 2003. “Understanding the Service Component of Application Service Provision: An Empirical Analysis of Satisfaction with ASP Services,” MIS Quarterly (27:1), pp. 91-123.

Susarla, A., Subramanyam, R., Karhade, P. 2010. “Contractual Provisions to Mitigate Holdup: Evidence from Information Technology Outsourcing,” Information Systems Research (21:1), pp. 37-55.

Teng, J. T. C., Cheon, M. J., and Grover, V. 1995. “Decisions to Outsource Information Systems Functions: Testing a Strategy-Theoretic Discrepancy Model,” Decision Sciences (26:1), pp. 75-103.

The State of Montana. 2015. 2015 Biennial Report on Information Technology (available at http://leg.mt.gov/content/ Publications/services/2014-agency-reports/SITSD-State-Biennial-Report-2015.pdf; accessed May 24, 2018).

Towns, S., and Knell, N. 2014. Digital States Survey: Which States Are the Best of the Best? (available at http://www.govtech. com/state/Digital-States-Survey-Which-States-Are-the-Best-ofthe-Best.html; accessed April 12, 2018).

Vithayathil, J., and Choudhary, V. 2014. “Organizational Structure for the IT Department: Profit Center or Cost Center?” (available at https://webfiles.uci.edu/jvithaya/www/pdfs/r1.pdf; accessed May 24, 2018).

Wang, E. T. G., and Barron, T. 1995. “Controlling Information Systems Department in the Presence of Cost Information Asymmetry,” Information Systems Research (6:1), pp. 24-50.

Wang, E. T. G., Barron, T., and Seidmann, A. 1997. “Contracting Structures for Custom Software Development: The Impacts of Informational Rent and Uncertainty on Internal Development and Outsourcing,” Management Science (43:12), pp. 1726-1744.

Wei, X., and Nault, B. R. 2013. “Experience Information Goods: ‘Version-to-Upgrade,’” Decision Support Systems (56), pp. 494-501.

Whang, S. 1990. “Alternative Mechanisms of Allocating Computer Resources Under Queueing Delays,” Information Systems Research (1:1), pp. 71-88.

Wood, C., Knell, N., Pittman, E., Mulholland, J., Newcombe, T., Eidam, E., Miller, B., McCaulley, R., and Shueh, J. 2016. How Digital Is Your State? (available at http://www.govtech.com/ computing/Digital-States-2016.html; accessed April 12, 2018).

Wu, Q., Huang, Y., Zhao, J., and Pu, Y. 2017. “Transfer Payment Structure and Local Government Fiscal Efficiency: Evidence from China,” China Finance and Economic Review (5:12), pp. 1-15.

Xue, L., Gautam, R., and Gu, B. 2011. “Environmental Uncertainty and IT Infrastructure Governance: A Curvilinear Relationship,” Information Systems Research (22:2), pp. 389-399.

Yasin, R. 2014. Southeast States Share Unemployment Benefits System (available at http://gcn.com/articles/2014/01/29/stateunemployment-systems.aspx; accessed May 24, 2018).

## About the Authors

Min Chen is an associate professor of Information Systems and Operations Management at the School of Business, George Mason University. He holds a Ph.D. in Management Science from the

Jindal School of Management, the University of Texas at Dallas. His research interests include economics of information systems, information security, optimization methods, and data mining. His research has appeared in journals including Decision Support Systems, IEEE Transactions on Knowledge and Data Engineering, and Information Systems Research, and premier conferences and workshops.

Min-Seok Pang is an associate professor of Management Information Systems and Milton F. Stauffer Research Fellow at the Fox School of Business, Temple University. He serves as an associate editor for MIS Quarterly and Journal of the Association for Information Systems. He received a B.S. in Industrial Engineering and an M.S. in Management from Korea Advanced Institute of Science and Technology (KAIST) and holds a Ph.D. in Business Administration from University of Michigan. His research interests include strategic management of information technology in the public sector and technology-enabled public policies. His research has published in Management Science, MIS Quarterly, and Information Systems Research. He received an AIS Best Information Systems Publication Award, a Best Published Paper Award from Information Systems Research, and an Outstanding Reviewer of the Year Award from MIS Quarterly.

Subodha Kumar is the Paul Anderson Distinguished Chair Professor of Marketing and Supply Chain Management (with joint appointments in Information Systems and Statistical Science) at the Fox School of Business, Temple University. He is the Founding Director of the Center for Data Analytics and the Ph.D. concentration advisor of Operations and Supply Chain Management. He is the Deputy Editor and a Department Editor of Production and OperationsManagement Journal and the Founding Executive Editor of Management and Business Review Journal. He has held several other editorial positions in leading journals. He has published many papers in prestigious journals.

## Appendix A

## Summary of Equilibrium Results

## Table A1. Results in the Non-Shared Service Case

<table><tr><td colspan="2">Case NI – Non-Shared Services, both choose Gov-A&#x27;s in-house team</td></tr><tr><td>Vendor Profit</td><td> $\pi^{NI} = 0$ </td></tr><tr><td>Gov-A&#x27;s Price</td><td> $p_{B}^{NI} = \left[ \frac{1}{4\alpha^{I}} - \Delta_{\alpha} + k(b - d) + \phi N_{B}^{(\beta - 1)} \right] N_{B}$ </td></tr><tr><td>Surplus of Gov-A</td><td> $W_{A}^{NI} = \left[ \frac{1}{4\alpha^{I}} - \phi N_{A}^{(\beta - 1)} \right] N_{A} + [k(b - d) - \Delta_{\alpha}] N_{B}$ </td></tr><tr><td>Surplus of Gov-B</td><td> $W_{B}^{NI} = \left[ \frac{1}{4\alpha^{O}} - \phi N_{B}^{(\beta - 1)} - kb \right] N_{B}$ </td></tr><tr><td>Total Surplus</td><td> $W_{T}^{NI} = W_{A}^{NI} + W_{B}^{NI} = \frac{1}{4\alpha^{I}} (N_{A} + N_{B}) - \phi (N_{A}^{\beta} + N_{B}^{\beta}) - kd N_{B}$ </td></tr><tr><td>Social Welfare</td><td> $SW^{NI} = \pi^{NI} + W_{T}^{NI} = \frac{1}{4\alpha^{I}} (N_{A} + N_{B}) - \phi (N_{A}^{\beta} + N_{B}^{\beta}) - kd N_{B}$ </td></tr><tr><td colspan="2">Case ND – Non-Shared Services, Gov-A chooses insourcing, Gov-B chooses outsourcing</td></tr><tr><td>Vendor Profit</td><td> $\pi^{ND} = [\Delta_{\alpha} - k(b - d)] N_{B}$ </td></tr><tr><td>Vendor Price for Gov-B</td><td> $p_{B}^{NO} = \left[ \frac{1}{4\alpha^{O}} + \Delta_{\alpha} - k(b - d) + \phi N_{B}^{(\beta - 1)} \right] N_{B}$ </td></tr><tr><td>Surplus of Gov-A</td><td> $W_{A}^{ND} = \left[ \frac{1}{4\alpha^{I}} - \phi N_{A}^{(\beta - 1)} \right] N_{A}$ </td></tr><tr><td>Surplus of Gov-B</td><td> $W_{B}^{ND} = \left[ \frac{1}{4\alpha^{I}} - \phi N_{B}^{(\beta - 1)} - kd \right] N_{B}$ </td></tr><tr><td>Total Surplus</td><td> $W_{T}^{ND} = W_{A}^{ND} + W_{B}^{ND} = \frac{1}{4\alpha^{I}} (N_{A} + N_{B}) - \phi (N_{A}^{\beta} + N_{B}^{\beta}) - kd N_{B}$ </td></tr><tr><td>Social Welfare</td><td> $SW^{ND} = \pi^{ND} + W_{T}^{ND} = \frac{1}{4\alpha^{I}} N_{A} + \frac{1}{4\alpha^{O}} N_{B} - \phi (N_{A}^{\beta} + N_{B}^{\beta}) - kb N_{B}$ </td></tr><tr><td colspan="2">Case NO – Non-Shared Services, both outsource to the vendor</td></tr><tr><td>Vendor Profit</td><td> $\pi^{NO} = (\Delta_{\alpha} - ka) N_{A} + [\Delta_{\alpha} - k(b - d)] N_{B}$ </td></tr><tr><td>Vendor Price for Gov-A</td><td> $p_{A}^{NO} = \left[ \frac{1}{4\alpha^{O}} + \Delta_{\alpha} - ka + \phi N_{A}^{(\beta - 1)} \right] N_{A}$ </td></tr><tr><td>Vendor Price for Gov-B</td><td> $p_{B}^{NO} = \left[ \frac{1}{4\alpha^{O}} + \Delta_{\alpha} - k(b - d) + \phi N_{B}^{(\beta - 1)} \right] N_{B}$ </td></tr><tr><td>Surplus of Gov-A</td><td> $W_{A}^{NO} = \left[ \frac{1}{4\alpha^{I}} - \phi N_{A}^{(\beta - 1)} \right] N_{A}$ </td></tr><tr><td>Surplus of Gov-B</td><td> $W_{B}^{NO} = \left[ \frac{1}{4\alpha^{I}} - \phi N_{B}^{(\beta - 1)} - kd \right] N_{B}$ </td></tr><tr><td>Total Surplus</td><td> $W_{T}^{NO} = W_{A}^{NO} + W_{B}^{NO} = \frac{1}{4\alpha^{I}} (N_{A} + N_{B}) - \phi (N_{A}^{\beta} + N_{B}^{\beta}) - kd N_{B}$ </td></tr><tr><td>Social Welfare</td><td> $SW^{NO} = \pi^{NO} + W_{T}^{NO} = \frac{1}{4\alpha^{O}} (N_{A} + N_{B}) - \phi (N_{A}^{\beta} + N_{B}^{\beta}) - k(a N_{A} + b N_{B})$ </td></tr></table>

## Lemma A1. (Equilibrium in the Non-Shared Case)

Denote $\begin{array} { r } { \Delta _ { \alpha } \mathrm { = } \frac { \left( \alpha ^ { I } - \alpha ^ { O } \right) } { 4 \alpha ^ { O } \alpha ^ { I } } . } \end{array}$ . If IT services are not shared, in equilibrium,

(1) (Case NI) When $\Delta _ { \alpha } \leq k ( b - d )$ , both governments choose Gov-A’s in-house team to develop IT services individually. The quality is $\begin{array} { r } { q _ { A } ^ { N I } = q _ { B } ^ { N I } = \frac { 1 } { 2 \alpha ^ { I } } . } \end{array}$

(2) (Case ND) When $k ( b - d ) < \Delta _ { \alpha } <$ <sub>????</sub>, Gov-A develops in-house and Gov-B outsources to the vendor. The quality of Gov-A and the vendor is $\begin{array} { r } { q _ { A } ^ { N O } = \frac { 1 } { 2 \alpha ^ { o } } } \end{array}$ and $\begin{array} { r } { q _ { B } ^ { N I } = \frac { 1 } { 2 \alpha ^ { I } } , } \end{array}$ respectively.

(3) $( \underline { { C a s e } } \underline { { N O } } )$ When $\Delta _ { \alpha } \geq k a ,$ , both governments outsource IT services to the vendor individually. The vendor’s quality is $q _ { A } ^ { N O } = q _ { B } ^ { N O } =$ ${ \frac { 1 } { 2 \alpha ^ { o } } } .$

Table A2. Results in the Shared Service Case under the Cost-Sharing Regime

<table><tr><td colspan="2">Case SI – Shared Service,insourced to Gov-A</td></tr><tr><td>Vendor’s Profit</td><td> $\pi^{SI^{CS}} = 0$ </td></tr><tr><td>Surplus of Gov-A</td><td> $W_{A}^{SI^{CS}} = \left[ \frac{1}{4\alpha^{I}} - \phi (N_{A} + N_{B})^{(\beta-1)} - \psi d \right] N_{A}$ </td></tr><tr><td>Surplus of Gov-B</td><td> $W_{B}^{SI^{CS}} = \left[ \frac{1}{4\alpha^{I}} - \phi (N_{A} + N_{B})^{(\beta-1)} - \psi d - kd \right] N_{B}$ </td></tr><tr><td>Total Surplus</td><td> $W_{T}^{SI^{CS}} = W_{A}^{SI^{CS}} + W_{B}^{SI^{CS}} = \left[ \frac{1}{4\alpha^{I}} - \phi (N_{A} + N_{B})^{(\beta-1)} - \psi d \right] (N_{A} + N_{B}) - kd N_{B}$ </td></tr><tr><td>Social Welfare</td><td> $SW^{SI^{CS}} = \pi^{SI^{CS}} + W_{T}^{SI^{CS}} = \left[ \frac{1}{4\alpha^{I}} - \phi (N_{A} + N_{B})^{(\beta-1)} - \psi d \right] (N_{A} + N_{B}) - kd N_{B}$ </td></tr><tr><td colspan="2">Case SO – Shared Service,outsourced to the vendor</td></tr><tr><td>Vendor’s Profit</td><td> $\pi^{SO^{CS}} = (\Delta_{\alpha} - ka)(N_{A} + N_{B})$ </td></tr><tr><td>Vendor’s Price</td><td> $p^{SO^{CS}} = \left[ \frac{1}{4\alpha^{O}} + \Delta_{\alpha} - ka + \psi d + \phi (N_{A} + N_{B})^{(\beta-1)} \right] (N_{A} + N_{B})$ </td></tr><tr><td>Surplus of Gov-A</td><td> $W_{A}^{SO^{CS}} = \left[ \frac{1}{4\alpha^{I}} - \phi (N_{A} + N_{B})^{(\beta-1)} - \psi d \right] N_{A}$ </td></tr><tr><td>Surplus of Gov-B</td><td> $W_{B}^{SO^{CS}} = \left[ \frac{1}{4\alpha^{I}} - \phi (N_{A} + N_{B})^{(\beta-1)} + k(a - b) - \psi d \right] N_{B}$ </td></tr><tr><td>Total Surplus</td><td> $W_{T}^{SO^{CS}} = W_{A}^{SO^{CS}} + W_{B}^{SO^{CS}} = \left[ \frac{1}{4\alpha^{I}} - \phi (N_{A} + N_{B})^{(\beta-1)} - \psi d \right] (N_{A} + N_{B}) + k(a - b) N_{B}$ </td></tr><tr><td>Social Welfare</td><td> $SW^{SO^{CS}} = \left[ \frac{1}{4\alpha^{O}} - \phi (N_{A} + N_{B})^{(\beta-1)} - \psi d \right] (N_{A} + N_{B}) - k(a N_{A} + b N_{B})$ </td></tr></table>

## Lemma A2. (Equilibrium in the Shared Service Case under the Cost-Sharing Regime)

Denote $\hat { \Delta } _ { 1 } { = } \phi \big [ { N _ { A } } ^ { ( \beta - 1 ) } - ( N _ { A } + N _ { B } ) ^ { ( \beta - 1 ) } \big ]$ . Under the cost-sharing regime, in equilibrium, Gov-A and B share their IT services under the following conditions:

1. $\Delta _ { \alpha } \geq k ( b - d )$ and $0 < \psi d \leq \widehat { \Delta } _ { 1 }$ , in which the shared IT service is outsourced $i f \Delta _ { \alpha } \geq$ <sub>????</sub> and insourced $i f k ( b - d ) \leq \Delta _ { \alpha } <$ ????<sup>.</sup>

2. $0 < \Delta _ { \alpha } < k ( b - d )$ and $\begin{array} { r } { 0 < \psi d \le \hat { \Delta } _ { 1 } - \frac { [ k ( b - d ) - \Delta _ { \alpha } ] N _ { B } } { N _ { A } } , } \end{array}$ in which the shared IT service is insourced.

Otherwise, they choose to not share IT services, and the outsourcing decision is characterized in Lemma A1.

<table><tr><td colspan="2">Table A3. Results in the Shared Service Case under the Profit-Center Regime</td></tr><tr><td colspan="2">Case SI – Shared Service, insourced to Gov-A</td></tr><tr><td>Vendor&#x27;s Profit</td><td> $\pi^{SI^{PC}} = 0$ </td></tr><tr><td>Gov-A&#x27;s Price</td><td> $p^{SI^{PC}} = \left[ \frac{1}{4\alpha^{I}} - \Delta_{\alpha} + k(b - d) + \phi(N_A + N_B)^{(\beta-1)} + \psi d \right] N_B$ </td></tr><tr><td>Surplus of Gov-A</td><td> $W_A^{SI^{PC}} = \left[ \frac{1}{4\alpha^{I}} - \phi(N_A + N_B)^{(\beta-1)} - \psi d \right] N_A - [\Delta_{\alpha} - k(b - d)]N_B$ </td></tr><tr><td>Surplus of Gov-B</td><td> $W_B^{SI^{PC}} = \left[ \frac{1}{4\alpha^{O}} - \phi(N_A + N_B)^{(\beta-1)} - kb - \psi d \right] N_B$ </td></tr><tr><td>Total Surplus</td><td> $W_T^{SI^{PC}} = W_A^{SI^{PC}} + W_B^{SI^{PC}} = \left[ \frac{1}{4\alpha^{I}} - \phi(N_A + N_B)^{(\beta-1)} - \psi d \right] (N_A + N_B) - kdN_B$ </td></tr><tr><td>Social Welfare</td><td> $SW^{SI^{PC}} = \left[ \frac{1}{4\alpha^{I}} - \phi(N_A + N_B)^{(\beta-1)} - \psi d \right] (N_A + N_B) - kdN_B$ </td></tr><tr><td colspan="2">Case SO – Shared Service, outsourced to the vendor</td></tr><tr><td>Vendor&#x27;s Profit</td><td> $\pi^{SO^{PC}} = \Delta_{\alpha}(N_A + N_B) - k[aN_A + (b - d)N_B]$ </td></tr><tr><td>Vendor&#x27;s Price</td><td> $p^{SO^{PC}} = \left[ \frac{1}{4\alpha^{O}} + \Delta_{\alpha} + \psi d + \phi(N_A + N_B)^{(\beta-1)} \right] (N_A + N_B) - k[aN_A + (b - d)N_B]$ </td></tr><tr><td>Surplus of Gov-A</td><td> $W_A^{SO^{PC}} = \left[ \frac{1}{4\alpha^{I}} - \phi(N_A + N_B)^{(\beta-1)} - \psi d - \frac{k(a-b+d)N_B}{(N_A+N_B)} \right] N_A$ </td></tr><tr><td>Surplus of Gov-B</td><td> $W_B^{SO^{PC}} = \left[ \frac{1}{4\alpha^{I}} - \phi(N_A + N_B)^{(\beta-1)} - \psi d + \frac{k[(a-b)N_A-dN_B]}{(N_A+N_B)} \right] N_B$ </td></tr><tr><td>Total Surplus</td><td> $W_T^{SO^{PC}} = W_A^{SO^{PC}} + W_B^{SO^{PC}} = \left[ \frac{1}{4\alpha^{I}} - \phi(N_A + N_B)^{(\beta-1)} - \psi d \right] (N_A + N_B) - kdN_B$ </td></tr><tr><td>Social Welfare</td><td> $SW^{SO^{PC}} = \left[ \frac{1}{4\alpha^{O}} - \phi(N_A + N_B)^{(\beta-1)} - \psi d \right] (N_A + N_B) - k(aN_A + bN_B)$ </td></tr></table>

## Lemma A3. (Equilibrium in the Shared Service Case under the Profit-Center Regime)

Under the profit-center regime, in equilibrium, Gov-A and B share their IT services if

$$
1. \Delta_ {\alpha} \geq \frac {k [ a N _ {A} + (b - d) N _ {B} ]}{(N _ {A} + N _ {B})} a n d 0 <   \psi d <   \hat {\Delta} _ {1} - \frac {k (a - b + d) N _ {B}}{(N _ {A} + N _ {B})}, o r
$$

$$
2. k (b - d) \leq \Delta_ {\alpha} <   \frac {k [ a N _ {A} + (b - d) N _ {B} ]}{(N _ {A} + N _ {B})} a n d 0 <   \psi d <   \hat {\Delta} _ {1} - \frac {[ \Delta_ {\alpha} - k (b - d) ] N _ {B}}{N _ {A}}, o r
$$

3. $0 < \Delta _ { \alpha } < k ( b - d )$ and $0 < \psi d < \widehat { \Delta } _ { 1 }$

Specifically, the shared service is outsourced to the vendor under Case 1 and insourced to Gov-A under Cases 2 and 3 above. Otherwise, they choose to not share IT services, and the outsourcing decision is characterized in Lemma A1.

<table><tr><td colspan="2">Table A4. Results in Shared Service Case under the Coordination Regime</td></tr><tr><td colspan="2">Case SI – Shared Service,insourced to Gov-A</td></tr><tr><td>Vendor’s Profit</td><td> $\pi^{SI^{CR}} = 0$ </td></tr><tr><td>Total Surplus</td><td> $W_{T}^{SI^{CR}} = \left[ \frac{1}{4\alpha^{I}} - \phi(N_{A} + N_{B})^{(\beta-1)} - \psi d \right] (N_{A} + N_{B}) - kdN_{B}$ </td></tr><tr><td>Social Welfare</td><td> $SW^{SI^{CR}} = \left[ \frac{1}{4\alpha^{I}} - \phi(N_{A} + N_{B})^{(\beta-1)} - \psi d \right] (N_{A} + N_{B}) - kdN_{B}$ </td></tr><tr><td colspan="2">Case SO – Shared Service,outsourced to the vendor</td></tr><tr><td>Vendor’s Profit</td><td> $\pi^{SO^{CR}} = \Delta_{\alpha}(N_{A} + N_{B}) - k[aN_{A} + (b-d)N_{B}]$ </td></tr><tr><td>Vendor’s Price</td><td> $p^{SO^{CR}} = \left[ \frac{1}{4\alpha^{O}} + \Delta_{\alpha} + \psi d + \phi(N_{A} + N_{B})^{(\beta-1)} \right] (N_{A} + N_{B}) - k[aN_{A} + (b-d)N_{B}]$ </td></tr><tr><td>Total Surplus</td><td> $W_{T}^{SO^{CR}} = \left[ \frac{1}{4\alpha^{I}} - \phi(N_{A} + N_{B})^{(\beta-1)} - \psi d \right] (N_{A} + N_{B}) - kdN_{B}$ </td></tr><tr><td>Social Welfare</td><td> $SW^{SO^{CR}} = \left[ \frac{1}{4\alpha^{O}} - \phi(N_{A} + N_{B})^{(\beta-1)} - \psi d \right] (N_{A} + N_{B}) - k(aN_{A} + bN_{B})$ </td></tr></table>

## Lemma A4. (Equilibrium in the Shared Service Case under the Coordination Regime)

Denote $\begin{array} { r } { \widehat { \Delta } _ { 2 } = \frac { \phi \left[ { N _ { A } } ^ { \beta } + { N _ { B } } ^ { \beta } - ( N _ { A } + N _ { B } ) ^ { \beta } \right] } { ( N _ { A } + N _ { B } ) } . } \end{array}$ When the governments can coordinate,

1. $I f \psi d \leq \hat { \Delta } _ { 2 } ,$ in equilibrium, Gov-A and B share their IT services, which are outsourced $\begin{array} { r } { i f \Delta _ { \alpha } \ge \frac { k \left[ a N _ { A } + ( b - d ) N _ { B } \right] } { ( N _ { A } + N _ { B } ) } } \end{array}$ and insourced

otherwise.

2. $I f \psi d > \hat { \Delta } _ { 2 }$ , in equilibrium, Gov-A and B do not share their IT services. The two governments’ decisions are characterized in Lemma

A1.

## Lemma A5.1 (Section 5.1: Endogenizing the Vendor’s Location – Non-Shared Service Case)

Denote $d _ { A } = | a - c |$ and $d _ { B } = | b - c |$ . If the IT services are not shared, in equilibrium,

(1) (Case NI) When $\Delta _ { \alpha } \leq k ( d _ { B } - d ) + \gamma c$ , both governments choose Gov-A’s in-house team to develop IT services individually.

(2) (Case ND) When $k ( d _ { B } - d ) + \gamma c < \Delta _ { \alpha } < k d _ { A } + \gamma c ,$ , Gov-A develops in-house and Gov-B outsources to the vendor.

(3) (Case NO) When $\Delta _ { \alpha } \geq k d _ { A } + \gamma c ,$ , both governments outsource IT services to the vendor individually.

## Lemma A5.2 (Section 5.1: Endogenizing the Vendor’s Location – Cost-Sharing Regime)

Under the cost-sharing regime, in equilibrium, Gov-A and B share their IT services under the following conditions:

1. $\Delta _ { \alpha } \geq k ( d _ { B } - d )$ + ?? and $0 < \psi d \leq \widehat { \Delta } _ { 1 }$ , in which the shared IT service is outsourced $i f \Delta _ { \alpha } \geq k d _ { A } .$ <sub>+</sub> <sub>??</sub> and insourced if

$$
k (d _ {B} - d) + \gamma c \leq \Delta_ {\alpha} <   k d _ {A} + \gamma c.
$$

2. $0 < \Delta _ { \alpha } < k ( d _ { B } - d ) + \gamma c$ and $\begin{array} { r } { 0 < \psi d \leq \widehat { \Delta } _ { 1 } - \frac { [ k ( d _ { B } - d ) - \Delta _ { \alpha } ] N _ { B } } { N _ { A } } ; } \end{array}$ in which the shared IT service is insourced.

3.

## Lemma A5.3 (Section 5.1: Endogenizing the Vendor’s Location – Profit-Center Regime)

Under the profit-center regime, in equilibrium, Gov-A and B share their IT services if

$$
1. \Delta_ {\alpha} \geq \frac {k [ d _ {A} N _ {A} + (d _ {B} - d) N _ {B} ]}{(N _ {A} + N _ {B})} + \gamma c a n d 0 <   \psi d <   \hat {\Delta} _ {1} - \frac {k (d _ {A} - d _ {B} + d) N _ {B}}{(N _ {A} + N _ {B})}, o r
$$

$$
2. k (d _ {B} - d) + \gamma c \leq \Delta_ {\alpha} <   \frac {k [ d _ {A} N _ {A} + (d _ {B} - d) N _ {B} ]}{(N _ {A} + N _ {B})} + \gamma c a n d 0 <   \psi d <   \widehat {\Delta} _ {1} - \frac {[ \Delta_ {\alpha} - k (d _ {B} - d) ] N _ {B}}{N _ {A}}, o r
$$

3. $0 < \Delta _ { \alpha } < k ( d _ { B } - d ) + \gamma c ~ a n d ~ 0 < \psi d < \hat { \Delta } _ { 1 }$

Specifically, the shared service is outsourced to the vendor under Case 1 and insourced to Gov-A under Cases 2 and 3 above. Otherwise, they choose to not share IT services, and the outsourcing decision is characterized in Lemma A5.1.

## Lemma A5.4 (Section 5.1: Endogenizing the Vendor’s Location – Coordination Regime)

When the governments can coordinate,

1. $I f \psi d \leq \hat { \Delta } _ { 2 } ,$ , in equilibrium, Gov-A and B share their IT services, which are outsourced $\begin{array} { r } { i f \Delta _ { \alpha } { \geq \frac { k [ d _ { A } N _ { A } + ( d _ { B } - d ) N _ { B } ] } { ( N _ { A } + N _ { B } ) } } + \gamma c \ a n d } \end{array}$

insourced otherwise.

2. $I f \psi d > \hat { \Delta } _ { 2 }$ , in equilibrium, Gov-A and B do not share their IT services. The two governments’ decisions are characterized in Lemma A5.1.

<table><tr><td colspan="2">Table A5. Results in the Non-Shared Service Case When Economies of Scale Is Present</td></tr><tr><td colspan="2">Case NI – Non-Shared Services, both choose Gov-A’s in-house team</td></tr><tr><td>Vendor Profit</td><td> $\pi^{NI} = 0$ </td></tr><tr><td>Gov-A’s Price</td><td> $p_{B}^{NI-T} = \left[ \frac{1}{4\alpha^{I}} - \Delta_{\alpha} + k(b-d) + \phi N_{B}^{(\beta-1)} \right] N_{B}$ </td></tr><tr><td>Surplus of Gov-A</td><td> $W_{A}^{NI} = \frac{1}{4\alpha^{I}} N_{A} + [k(b-d) - \Delta_{\alpha}] N_{B} - \phi [(N_{A} + N_{B})^{\delta\beta} - N_{B}^{\beta}]$ </td></tr><tr><td>Surplus of Gov-B</td><td> $W_{B}^{NI} = \left[ \frac{1}{4\alpha^{O}} - \phi N_{B}^{(\beta-1)} - kb \right] N_{B}$ </td></tr><tr><td>Total Surplus</td><td> $W_{T}^{NI} = W_{A}^{NI} + W_{B}^{NI} = \frac{1}{4\alpha^{I}} (N_{A} + N_{B}) - \phi (N_{A} + N_{B})^{\delta\beta} - kd N_{B}$ </td></tr><tr><td>Social Welfare</td><td> $SW^{NI} = \pi^{NI} + W_{T}^{NI} = \frac{1}{4\alpha^{I}} (N_{A} + N_{B}) - \phi (N_{A} + N_{B})^{\delta\beta} - kd N_{B}$ </td></tr><tr><td colspan="2">Case ND – Non-Shared Services, Gov-A chooses insourcing, Gov-B chooses outsourcing</td></tr><tr><td>Vendor Profit</td><td> $\pi^{ND} = [\Delta_{\alpha} - k(b-d)] N_{B} + \phi [(N_{A} + N_{B})^{\delta\beta} - (N_{A}^{\beta} + N_{A}^{\beta})]$ </td></tr><tr><td>Vendor Price for Gov-B</td><td> $p_{B}^{NO} = \frac{1}{4\alpha^{O}} N_{B} + [\Delta_{\alpha} - k(b-d)] N_{B} + \phi [(N_{A} + N_{B})^{\delta\beta} - N_{A}^{\beta}]$ </td></tr><tr><td>Surplus of Gov-A</td><td> $W_{A}^{ND} = \left[ \frac{1}{4\alpha^{I}} - \phi N_{A}^{(\beta-1)} \right] N_{A}$ </td></tr><tr><td>Surplus of Gov-B</td><td> $W_{B}^{ND} = \left( \frac{1}{4\alpha^{I}} - kd \right) N_{B} - \phi [(N_{A} + N_{B})^{\delta\beta} - N_{A}^{\beta}]$ </td></tr><tr><td>Total Surplus</td><td> $W_{T}^{ND} = W_{A}^{ND} + W_{B}^{ND} = \frac{1}{4\alpha^{I}} (N_{A} + N_{B}) - kd N_{B} - \phi (N_{A} + N_{B})^{\delta\beta}$ </td></tr><tr><td>Social Welfare</td><td> $SW^{ND} = \pi^{ND} + W_{T}^{ND} = \frac{1}{4\alpha^{I}} N_{A} + \frac{1}{4\alpha^{O}} N_{B} - kb N_{B} - \phi (N_{A}^{\beta} + N_{A}^{\beta})$ </td></tr><tr><td colspan="2">Case NO – Non-Shared Services, both outsource to the vendor</td></tr><tr><td>Vendor Profit</td><td> $\pi^{NO} = (\Delta_{\alpha} - ka) N_{A} + [\Delta_{\alpha} - k(b-d)] N_{B}$ </td></tr><tr><td>Vendor Price for Gov-A</td><td> $p_{A}^{NO-T} = \left[ \frac{1}{4\alpha^{O}} + \Delta_{\alpha} - ka + \phi N_{A}^{(\beta-1)} \right] N_{A}$ </td></tr><tr><td>Vendor Price for Gov-B</td><td> $p_{B}^{NO-T} = \left[ \frac{1}{4\alpha^{O}} + \Delta_{\alpha} - k(b-d) \right] N_{B} + \phi [(N_{A} + N_{B})^{\delta\beta} - N_{A}^{\beta}]$ </td></tr><tr><td>Surplus of Gov-A</td><td> $W_{A}^{NO} = \left[ \frac{1}{4\alpha^{I}} - \phi N_{A}^{(\beta-1)} \right] N_{A}$ </td></tr><tr><td>Surplus of Gov-B</td><td> $W_{B}^{NO} = \left( \frac{1}{4\alpha^{I}} - kd \right) N_{B} - \phi [(N_{A} + N_{B})^{\delta\beta} - N_{A}^{\beta}]$ </td></tr><tr><td>Total Surplus</td><td> $W_{T}^{NO} = W_{A}^{NO} + W_{B}^{NO} = \frac{1}{4\alpha^{I}} (N_{A} + N_{B}) - kd N_{B} - \phi (N_{A} + N_{B})^{\delta\beta}$ </td></tr><tr><td>Social Welfare</td><td> $SW^{NO} = \frac{1}{4\alpha^{O}} N_{A} + \frac{1}{4\alpha^{O}} N_{B} - k(a N_{A} + b N_{B}) - \phi (N_{A} + N_{B})^{\delta\beta}$ </td></tr></table>

## Lemma A6. (Section 5.2: Economies of Scale in the Non-Shared Case)

Denote $\begin{array} { r } { \widehat { \Delta } _ { 3 } = \frac { \phi \left[ \left( N _ { A } { } ^ { \beta } + N _ { B } { } ^ { \beta } \right) - \left( N _ { A } + N _ { B } \right) \delta \beta \right] } { N _ { A } } } \end{array}$ . If economies of scale are also obtained in the non-shared case, in equilibrium,

(1) (Case NI) When $\Delta _ { \alpha } \leq$ min $\begin{array} { r l } { \quad } & { { } \Big \{ \frac { k [ a N _ { A } + ( b - d ) N _ { B } ] } { ( N _ { A } + N _ { B } ) } , \Big [ k ( b - d ) + \hat { \Delta } _ { 3 } \left( \frac { N _ { A } } { N _ { B } } \right) \Big ] \Big \} } \end{array}$ , both governments choose Gov-A’s in-house team to develop IT services individually.

(2) (Case ND) When $\begin{array} { r } { \left[ k ( b - d ) + \hat { \Delta } _ { 3 } \left( \frac { N _ { A } } { N _ { R } } \right) \right] < \Delta _ { \alpha } < \left[ k a - \hat { \Delta } _ { 3 } \right] } \end{array}$ , Gov-A develops in-house and Gov-B outsources to the vendor.

(3) (Case NO) When $\begin{array} { r } { \Delta _ { \alpha } \geq \operatorname* { m a x } \Big \{ \frac { k [ a N _ { A } + ( b - d ) N _ { B } ] } { ( N _ { A } + N _ { B } ) } , \big [ k a - \widehat \Delta _ { 3 } \big ] \Big \} , } \end{array}$ , both governments outsource IT services to the vendor individually.

## Lemma A7.1 (Section 5.2: Equilibrium in the Cost-Sharing Regime)

Denote $\hat { \Delta } _ { 4 } { = } \phi \big [ { N _ { B } } ^ { ( \beta - 1 ) } - ( N _ { A } + N _ { B } ) ^ { ( \beta - 1 ) } \big ]$ . Under the cost-sharing regime, in equilibrium, Gov-A and B share their IT services under the following conditions:

$$
1. \quad \Delta_ {\alpha} > k a a n d 0 <   \psi d <   \min \left\{\hat {\Delta} _ {1}, \hat {\Delta} _ {4} - \hat {\Delta} _ {3} \left(\frac {N _ {A}}{N _ {B}}\right) + k (a - b + d) \right\} o r
$$

$$
2. \quad \min \left\{\frac {k [ a N _ {A} + (b - d) N _ {B} ]}{(N _ {A} + N _ {B})}, \left[ k (b - d) + \widehat {\Delta} _ {3} \left(\frac {N _ {A}}{N _ {B}}\right) \right] \right\} <   \Delta_ {\alpha} \leq k a a n d 0 <   \psi d \leq \min \left\{\widehat {\Delta} _ {1}, \widehat {\Delta} _ {4} - \widehat {\Delta} _ {3} \left(\frac {N _ {A}}{N _ {B}}\right) \right\} o r
$$

$$
3. 0 <   \Delta_ {\alpha} <   \min \left\{\frac {k [ a N _ {A} + (b - d) N _ {B} ]}{(N _ {A} + N _ {B})}, \left[ k (b - d) + \hat {\Delta} _ {3} \left(\frac {N _ {A}}{N _ {B}}\right) \right] \right\} a n d 0 <   \psi d \leq \left(\hat {\Delta} _ {1} - \hat {\Delta} _ {3}\right) - \frac {[ k (b - d) - \Delta_ {\alpha} ] N _ {B}}{N _ {A}}.
$$

Specifically, the shared service is outsourced to the vendor under Case 1 and insourced to Gov-A under Cases 2 and 3 above. Otherwise, they choose to not share IT services, and the outsourcing decision is characterized in Lemma A6.

## Lemma A7.2 (Section 5.2: Equilibrium in the Profit-Center Regime)

Under the profit-center regime, in equilibrium, Gov-A and B share their IT services if

$$
1. \Delta_ {\alpha} \geq \frac {k [ a N _ {A} + (b - d) N _ {B} ]}{(N _ {A} + N _ {B})} a n d 0 <   \psi d <   \hat {\Delta} _ {1} - \frac {k (a - b + d) N _ {B}}{(N _ {A} + N _ {B})}, o r
$$

$$
2. \quad \min \left\{\frac {k [ a N _ {A} + (b - d) N _ {B} ]}{(N _ {A} + N _ {B})}, \left[ k (b - d) + \widehat {\Delta} _ {3} \left(\frac {N _ {A}}{N _ {B}}\right) \right] \right\} \leq \Delta_ {\alpha} <   \frac {k [ a N _ {A} + (b - d) N _ {B} ]}{(N _ {A} + N _ {B})} a n d 0 <   \psi d <   \widehat {\Delta} _ {1} - \frac {[ \Delta_ {\alpha} - k (b - d) ] N _ {B}}{N _ {A}}, o r
$$

$$
3. 0 <   \Delta_ {\alpha} <   \min \left\{\frac {k [ a N _ {A} + (b - d) N _ {B} ]}{(N _ {A} + N _ {B})}, \left[ k (b - d) + \hat {\Delta} _ {3} \left(\frac {N _ {A}}{N _ {B}}\right) \right] \right\} a n d 0 <   \psi d <   \hat {\Delta} _ {1} - \hat {\Delta} _ {3}.
$$

Specifically, the shared service is outsourced to the vendor under Case 1 and insourced to Gov-A under Cases 2 and 3 above. Otherwise, they choose to not share IT services, and the outsourcing decision is characterized in Lemma A6.

## Lemma A7.3 (Section 5.2: Equilibrium in the Coordination Regime)

When the governments can coordinate,

1. $\begin{array} { r } { I f \psi d \leq \hat { \Delta } _ { 2 } - \hat { \Delta } _ { 3 } \left( { \frac { N _ { A } } { N _ { A } + N _ { B } } } \right) } \end{array}$ , in equilibrium, Gov-A and B share their IT services, which are outsourced $\begin{array} { r } { i f \Delta _ { \alpha } \ge \frac { k \left[ a N _ { A } + ( b - d ) N _ { B } \right] } { ( N _ { A } + N _ { B } ) } } \end{array}$ and

insourced otherwise.

2. If <sub>??</sub> $\begin{array} { r l r } { \mathrm { ~ } } & { { } } & { > \hat { \Delta } _ { 2 } - \hat { \Delta } _ { 3 } \left( \frac { N _ { A } } { N _ { A } + N _ { B } } \right) } \end{array}$ , in equilibrium, Gov-A and B do not share their IT services. The two governments’ decisions are

characterized in Lemma A6.

<table><tr><td colspan="2">Table A6. Results in the Non-Shared Service Case When Gov-B also has IT Capability</td></tr><tr><td colspan="2">Case AA – Both choose Gov-A’s in-house team</td></tr><tr><td>Vendor Profit</td><td> $\pi^{AA} = 0$ </td></tr><tr><td>Gov-A’s Price</td><td> $p_B^{AA} = \left[ \frac{1}{4\alpha^I} - \Delta_\alpha + k(b-d) + \phi N_B^{(\beta-1)} \right] N_B$ </td></tr><tr><td>Surplus of Gov-A</td><td> $W_A^{AA} = \left[ \frac{1}{4\alpha^A} - \phi N_A^{(\beta-1)} \right] N_A + [k(b-d) - \Delta_\alpha] N_B$ </td></tr><tr><td>Surplus of Gov-B</td><td> $W_B^{AA} = \left[ \frac{1}{4\alpha^O} - \phi N_B^{(\beta-1)} - kb \right] N_B$ </td></tr><tr><td>Total Surplus</td><td> $W_T^{AA} = \frac{1}{4\alpha^A}(N_A + N_B) - \phi(N_A^\beta + N_B^\beta) - kd N_B$ </td></tr><tr><td>Social Welfare</td><td> $SW^{AA} = \frac{1}{4\alpha^A}(N_A + N_B) - \phi(N_A^\beta + N_B^\beta) - kd N_B$ </td></tr><tr><td colspan="2">Case AB – Both choose respective in-house unit</td></tr><tr><td>Vendor Profit</td><td> $\pi^{AB} = 0$ </td></tr><tr><td>Surplus of Gov-A</td><td> $W_A^{AB} = \left[ \frac{1}{4\alpha^A} - \phi N_A^{(\beta-1)} \right] N_A$ </td></tr><tr><td>Surplus of Gov-B</td><td> $W_B^{AB} = \left[ \frac{1}{4\alpha^B} - \phi N_B^{(\beta-1)} \right] N_B$ </td></tr><tr><td>Total Surplus</td><td> $W_T^{AB} = \frac{1}{4\alpha^A} N_A + \frac{1}{4\alpha^B} N_B - \phi(N_A^\beta + N_B^\beta)$ </td></tr><tr><td>Social Welfare</td><td> $SW^{AB} = \frac{1}{4\alpha^A} N_A + \frac{1}{4\alpha^B} N_B - \phi(N_A^\beta + N_B^\beta)$ </td></tr><tr><td colspan="2">Case AO – Gov-A chooses insourcing, Gov-B chooses outsourcing</td></tr><tr><td>Vendor Profit</td><td> $\pi^{AO} = [\Delta_\alpha - kb + \min\{\Delta_A^{AB}, kd\}] N_B$ </td></tr><tr><td>Vendor Price for Gov-B</td><td> $p_B^{AO} = \left[ \frac{1}{4\alpha^O} + \Delta_\alpha - kb + \phi N_B^{(\beta-1)} + \min\{\Delta_A^{AB}, kd\} \right] N_B$ </td></tr><tr><td>Surplus of Gov-A</td><td> $W_A^{AO} = \left[ \frac{1}{4\alpha^A} - \phi N_A^{(\beta-1)} \right] N_A$ </td></tr><tr><td>Surplus of Gov-B</td><td> $W_B^{AO} = \left[ \frac{1}{4\alpha^A} - \phi N_B^{(\beta-1)} - \min\{\Delta_A^{AB}, kd\} \right] N_B$ </td></tr><tr><td>Total Surplus</td><td> $W_T^{AO} = \frac{1}{4\alpha^A}(N_A + N_B) - \phi(N_A^\beta + N_B^\beta) - N_B \times \min\{\Delta_A^{AB}, kd\}$ </td></tr><tr><td>Social Welfare</td><td> $SW^{AO} = \frac{1}{4\alpha^A} N_A + \frac{1}{4\alpha^O} N_B - kb N_B - \phi(N_A^\beta + N_B^\beta)$ </td></tr><tr><td colspan="2">Case OB – Gov-A outsources to the vendor and Gov-B develops in-house</td></tr><tr><td>Vendor Profit</td><td> $\pi^{OB} = (\Delta_\alpha - ka) N_A$ </td></tr><tr><td>Vendor Price for Gov-A</td><td> $p_A^{OB} = \left[ \frac{1}{4\alpha^O} + \Delta_\alpha - ka + \phi N_A^{(\beta-1)} \right] N_A$ </td></tr><tr><td>Surplus of Gov-A</td><td> $W_A^{OB} = \left[ \frac{1}{4\alpha^A} - \phi N_A^{(\beta-1)} \right] N_A$ </td></tr><tr><td>Surplus of Gov-B</td><td> $W_B^{OB} = \left[ \frac{1}{4\alpha^B} - \phi N_B^{(\beta-1)} \right] N_B$ </td></tr><tr><td>Total Surplus</td><td> $W_T^{OB} = \frac{1}{4\alpha^A} N_A + \frac{1}{4\alpha^B} N_B - \phi(N_A^\beta + N_B^\beta)$ </td></tr><tr><td>Social Welfare</td><td> $SW^{OB} = \frac{1}{4\alpha^O} N_A + \frac{1}{4\alpha^B} N_B - ka N_A - \phi(N_A^\beta + N_B^\beta)$ </td></tr><tr><td colspan="2">Case OO – Both outsource to the vendor</td></tr><tr><td>Vendor Profit</td><td> $\pi^{OO} = (\Delta_\alpha - ka) N_A + [\Delta_\alpha - kb + \min\{\Delta_A^{AB}, kd\}] N_B$ </td></tr><tr><td>Vendor Price for Gov-A</td><td> $p_A^{OO} = \left[ \frac{1}{4\alpha^O} + \Delta_\alpha - ka + \phi N_A^{(\beta-1)} \right] N_A$ </td></tr><tr><td>Vendor Price for Gov-B</td><td> $p_B^{OO} = \left[ \frac{1}{4\alpha^O} + \Delta_\alpha - kb + \phi N_B^{(\beta-1)} + \min\{\Delta_A^{AB}, kd\} \right] N_B$ </td></tr><tr><td>Surplus of Gov-A</td><td> $W_A^{OO} = \left[ \frac{1}{4\alpha^A} - \phi N_A^{(\beta-1)} \right] N_A$ </td></tr><tr><td>Surplus of Gov-B</td><td> $W_B^{OO} = \left[ \frac{1}{4\alpha^A} - \phi N_B^{(\beta-1)} - \min\{\Delta_A^{AB}, kd\} \right] N_B$ </td></tr><tr><td>Total Surplus</td><td> $W_T^{OO} = \frac{1}{4\alpha^A}(N_A + N_B) - \phi(N_A^\beta + N_B^\beta) - N_B \times \min\{\Delta_A^{AB}, kd\}$ </td></tr><tr><td>Social Welfare</td><td> $SW^{OO} = \frac{1}{4\alpha^O}(N_A + N_B) - k(a N_A + b N_B) - \phi(N_A^\beta + N_B^\beta)$ </td></tr></table>

## Lemma A8. (Section 5.3: IT Capability for Gov-B)

Denote $\begin{array} { r } { \Delta _ { \alpha } \mathrm { = } \frac { \left( \alpha ^ { A } - \alpha ^ { O } \right) } { 4 \alpha ^ { O } \alpha ^ { A } } a n d \Delta _ { \alpha } ^ { A B } \mathrm { = } \frac { \left( \alpha ^ { B } - \alpha ^ { A } \right) } { 4 \alpha ^ { A } \alpha ^ { B } } \mathrm { . } } \end{array}$ If the IT services are not shared, in equilibrium,

(1) (Case AA) When $\Delta _ { \alpha } \leq k ( b - d )$ and $\Delta _ { \alpha } ^ { A B } > k d$ , both governments choose Gov-A’s in-house team to develop IT services individually.

(2) (Case AB) When $\Delta _ { \alpha } \leq \operatorname* { m i n } \{ k a , k b - \Delta _ { \alpha } ^ { A B } \}$ and $\Delta _ { \alpha } ^ { A B } \leq k d ,$ , each government chooses its own in-house team to develop IT services (3) (Case AO) When <sub>ma</sub> $\{ k b - \Delta _ { \alpha } ^ { A B } , k ( b - d ) \} < \Delta _ { \alpha } <$ < ????<sup>,</sup> <sup>and</sup> $\Delta _ { \alpha } ^ { A B } > k ( b - a )$ , Gov-A develops in-house and Gov-B outsources to the vendor.

(4) (Case OB) When <sub>????</sub> $\leq \Delta _ { \alpha } < k b - \Delta _ { \alpha } ^ { A B }$ and $\Delta _ { \alpha } ^ { A B } \leq k ( b - a )$ , Gov-A outsources to the vendor and Gov-B develops in-house.

(5) (Case OO) When $\Delta _ { \alpha } \geq \operatorname* { m a x } \{ k a , k b - \Delta _ { \alpha } ^ { A B } \}$ , both governments outsource IT services to the vendor individually.

## Lemma A9 (Section 5.5: Additional Benefits from Shared IT Services)

Define $\begin{array} { r } { A _ { 3 } = \operatorname* { m i n } \left\{ \hat { \Delta } _ { 1 } , \hat { \Delta } _ { 1 } - \frac { [ k ( b - d ) - \Delta _ { \alpha } ] N _ { B } } { N _ { A } } \right\} + \frac { 1 } { 4 \alpha ^ { I } } \big ( \lambda ^ { 2 } - 1 \big ) } \end{array}$ . Under the cost-sharing regime, in equilibrium, Gov-A and B share their IT services under the following conditions:

1. $\begin{array} { r } { \Delta _ { \alpha } > \operatorname* { m i n } \left\{ \frac { k a } { \lambda ^ { 2 } } , k ( b - d ) \right\} } \end{array}$ and $0 < \psi d \leq A _ { 3 } ,$ in which the shared IT service is outsourced $\begin{array} { r } { i f \Delta _ { \alpha } { \geq } \frac { k a } { \lambda ^ { 2 } } } \end{array}$ and insourced otherwise.

2. $\begin{array} { r } { 0 < \Delta _ { \alpha } \leq \operatorname* { m i n } \left\{ \frac { k a } { \lambda ^ { 2 } } , k ( b - d ) \right\} a n d 0 < \psi d \leq A _ { 3 } , } \end{array}$ in which the shared IT service is insourced.

Otherwise, they choose to not share IT services, and the outsourcing decision is characterized in Lemma A1.

## Appendix B

## Proofs of Lemmas and Propositions in the Main Model

## Proof of Lemma A1

Gov-B’s surplus is $W _ { B } = \bigl ( q _ { B } ^ { N O } - k b \bigr ) N _ { B } - p _ { B } ^ { N O }$ if its IT service is developed by the vendor and $W _ { B } = ( q _ { B } ^ { N I } - k d ) N _ { B } - p _ { B } ^ { N I }$ if it is developed by Gov-A’s in-house team. As such, Gov-B will resort to Gov-A if

$$
p _ {B} ^ {N O} > \left[ \left(q _ {B} ^ {N O} - q _ {B} ^ {N I}\right) - k (b - d) \right] N _ {B} + p _ {B} ^ {N I} \geq \left[ \left(q _ {B} ^ {N O} - q _ {B} ^ {N I}\right) - k (b - d) \right] N _ {B} + C _ {B} ^ {N I} = p _ {2}.
$$

Gov-B will outsource to the vendor $\mathrm { i f } p _ { B } ^ { N O } \le p _ { 2 }$ . When Gov-B outsources, $\mathrm { i . e . , } p _ { B } ^ { N O } \le p _ { 2 }$ , Gov-A’s surplus is $W _ { A } = \bigl ( q _ { A } ^ { N O } - k a \bigr ) N _ { A } - p _ { A } ^ { N O }$ if its IT service is developed by the vendor and $W _ { A } = q _ { A } ^ { N I } N _ { A } - C _ { A } ^ { N I }$ if it is developed in-house. Gov-A will outsource if

$$
p _ {A} ^ {N O} \leq \left[ \left(q _ {A} ^ {N O} - q _ {A} ^ {N I}\right) - k a \right] N _ {A} + C _ {A} ^ {N I} = p _ {1}
$$

and develop in-house if $p _ { A } ^ { N O } > p _ { 1 }$ . When Gov-B resorts to $\mathrm { G o v { - } A , \ i . e . , } p _ { B } ^ { N O } > p _ { 2 } , \mathrm { G o v { - } A ^ { \prime } s }$ surplus is $W _ { A } = \bigl ( q _ { A } ^ { N O } - k a \bigr ) N _ { A } - p _ { A } ^ { N O } +$ $( p _ { B } ^ { N I } - C _ { B } ^ { N I } )$ if its IT service is developed by the vendor and $W _ { A } = q _ { A } ^ { N I } N _ { A } - C _ { A } ^ { N I } + ( p _ { B } ^ { N I } - C _ { B } ^ { N I } )$ if it is developed in-house. Gov-A will outsource if

$$
p _ {A} ^ {N O} \leq \big [ \big (q _ {A} ^ {N O} - q _ {A} ^ {N I} \big) - k a \big ] N _ {A} + C _ {A} ^ {N I} = p _ {1}
$$

and develop in-house if $p _ { A } ^ { N O } > p _ { 1 }$ . Thus, the vendor’s profit is:

$$
\pi = \left\{ \begin{array}{l l} \left(p _ {A} ^ {N O} - C _ {A} ^ {N O}\right) + \left(p _ {B} ^ {N O} - C _ {B} ^ {N O}\right) & \text {if p_{A} ^{NO} \leq p_{1} and p_{B} ^{NO} \leq p_{2}} \\ p _ {B} ^ {N O} - C _ {B} ^ {N O} & \text {if p_{A} ^{NO} >p_{1} and p_{B} ^{NO} \leq p_{2}} \\ p _ {A} ^ {N O} - C _ {A} ^ {N O} & \text {if p_{A} ^{NO} \leq p_{1} and p_{B} ^{NO} >p_{2}} \\ 0 & \text {if p_{A} ^{NO} >p_{1} and p_{B} ^{NO} >p_{2}} \end{array} \right.
$$

(1) $\mathrm { I f } p _ { A } ^ { N O } \leq p _ { 1 }$ and $p _ { B } ^ { N O } \leq p _ { 2 } , \pi = \left( p _ { A } ^ { N O } - C _ { A } ^ { N O } \right) + \left( p _ { B } ^ { N O } - C _ { B } ^ { N O } \right)$ . The vendor has an incentive to “undercut” Gov-A unless its price hits its marginal cost. If $C _ { A } ^ { N O } \le p _ { 1 }$ , the vendor can lower its price just enough to capture the demand of $\mathrm { { G o v - A : } } \ p _ { A } ^ { N O } = p _ { 1 }$ . Similarly, if $C _ { B } ^ { N O } \leq p _ { 2 } .$ , the vendor can undercut Gov-A just enough to capture the demand of Gov-B: $p _ { B } ^ { N O } = p _ { 2 }$ . The vendor’s profit function is concave in $q _ { A } ^ { N O }$ , and using FOC yields the optimal IT service quality for Gov-A and Gov-B under outsourcing as $\begin{array} { r } { q _ { A } ^ { N O } = q _ { B } ^ { N O } = \frac { 1 } { 2 \alpha ^ { O } } . } \end{array}$ Denote $\begin{array} { r } { \Delta _ { \alpha } \mathrm { = } \frac { \left( \alpha ^ { I } - \alpha ^ { O } \right) } { 4 \alpha ^ { O } \alpha ^ { I } } } \end{array}$ . To satisfy the boundary condition for $C _ { A } ^ { N O } \le p _ { 1 }$ and $C _ { B } ^ { N O } \le p _ { 2 }$ , we need $\Delta _ { \alpha } \geq$ ???? <sup>and</sup> $\Delta _ { \alpha } \geq k ( b - d )$ . It follows that $k a \geq k ( b - d )$ , where the inequality follows because $a \geq ( b - d ) \colon ( 1 ) { \mathrm { i f } } a < b .$ , then $a - ( b - d ) = a - { \big ( } b - ( b - a ) { \big ) } = 0$ , and (2) if <sub>≥</sub> <sub>??</sub> then $a - ( b - d ) = a - { \bigl ( } b - ( a - b ) { \bigr ) } = 2 ( a - b ) > 0 . \operatorname { S o } ,$ , the equilibrium exists if and only $\mathrm { i f } \Delta _ { \alpha } \ge k a .$

(2) ${ \mathrm { I f } } p _ { A } ^ { N O } > p _ { 1 } { \mathrm { ~ a n d } } p _ { B } ^ { N O } \leq p _ { 2 } , \pi = \left( p _ { B } ^ { N O } - C _ { B } ^ { N O } \right)$ . The vendor is able to lower its price just enough to capture the demand of Gov-B only, i.e. $. , p _ { B } ^ { N O } = p _ { 2 }$ . The vendor’s profit function is concave in $q _ { B } ^ { N O }$ and Gov-A’s surplus function is concave in $q _ { A } ^ { N I }$ , and using FOC yields the optimal IT service quality for Gov-A and Gov-B as $\begin{array} { r } { q _ { B } ^ { N O } = \frac { 1 } { 2 \alpha ^ { o } } } \end{array}$ and $q _ { A } ^ { N I } = \frac { \hat { 1 } } { 2 \alpha ^ { I } }$ . This occurs when $C _ { A } ^ { N O } > p _ { 1 }$ and $C _ { B } ^ { N O } \le p _ { 2 }$ Rearranging the two inequalities yields $\Delta _ { \alpha } <$ and $\Delta _ { \alpha } \geq k ( b - d )$ , respectively. To satisfy the boundary condition, we need $k ( b - d ) \leq \Delta _ { \alpha } <$ ???? <sup>and</sup> $a > b$ for this region to be non-empty.

(3) I $\mathrm { f } p _ { A } ^ { N O } \leq p _ { 1 }$ and $p _ { B } ^ { N O } > p _ { 2 } , \pi = p _ { A } ^ { N O } - C _ { A } ^ { \bar { N } O }$ . In this case, the vendor is able to lower the price enough to capture the demand of Gov-A only. This occurs when $C _ { A } ^ { N O } \le p _ { 1 }$ and $C _ { B } ^ { N O } > p _ { 2 } .$ , which implies $k a \le \Delta _ { \alpha } < k ( b - d )$ . This region is empty as $a \geq ( b - d )$ ; hence this equilibrium does not exist.

(4) $\mathrm { I f } p _ { A } ^ { N \bar { O } } > p _ { 1 }$ and $p _ { B } ^ { N O } > p _ { 2 } , \pi = 0$ . In this case, the vendor is unable to lower the price enough to capture the demand of either government. Gov-A’s surplus function is concave in $q _ { A } ^ { N I }$ and $q _ { B } ^ { N I }$ , and using FOC yields the optimal IT service quality for Gov-A and Gov-B under insourcing as $\begin{array} { r } { q _ { A } ^ { N I } = q _ { B } ^ { N I } = \frac { 1 } { 2 \alpha ^ { I } } } \end{array}$ . Gov-B chooses Gov-A’s in-house team and pays

$$
p _ {B} ^ {N I} = C _ {B} ^ {N O} - \left[\left(q _ {A} ^ {N O} - q _ {A} ^ {N I}\right) - k (b - d) \right] N _ {B} = \left\lceil \frac {1}{4 \alpha^ {I}} - \Delta_ {\alpha} + k (b - d) + \phi N _ {B} ^ {(\beta - 1)} \left. \right] N _ {B}.
$$

To satisfy the boundary condition, we need $0 < \Delta _ { \alpha } < k ( b - d )$ and $0 < \Delta _ { \alpha } < k a$ . For the first inequality, (1) if $\qquad \imath < b .$ , it becomes $0 <$ $\Delta _ { \alpha } < k a ; ( 2 ) { \mathrm { ~ i f ~ } } a \geq b$ , it becomes $0 < \Delta _ { \alpha } < k ( 2 b - a )$ , and for this region to be non-empty, we need $\begin{array} { r } { b > \frac { a } { 2 } , } \end{array}$ which is assumed in the paper. It is worth noting that without the assumption $b > { \frac { a } { \gamma } } ,$ this case would be infeasible, leading to a trivial case that Gov-B would always choose outsourcing. Therefore, the equilibrium exists if and only if $\cdot \Delta _ { \alpha } < k ( b - d )$

The others can be obtained by substituting back the optimal service quality to the respective functions. The results with respect to the governments’ decisions on outsourcing of separate IT services are summarized in Table A1. Note that in all equilibriums, neither the vendor nor the governments have an incentive to deviate from their equilibrium decisions, because doing so would lead to lower surplus when the boundary condition is not satisfied.

## Proof of Lemma A2

We first consider the subgame where a shared IT service is adopted and then use backward induction to solve the game. The shared service will be outsourced if $W _ { A } ^ { S O } \geq W _ { A } ^ { S I }$ , that is,

$$
p ^ {S O} \leq C ^ {S I} + [ (q ^ {S O} - q ^ {S I}) - k a ] (N _ {A} + N _ {B}) = p ^ {S O ^ {\#}}.
$$

and if $W _ { B } ^ { S O } \geq W _ { B } ^ { S I }$ , that is,

$$
p ^ {S O} \leq C ^ {S I} + [ (q ^ {S O} - q ^ {S I}) - k (b - d) ] (N _ {A} + N _ {B}) = p ^ {S O ^ {\# \#}}.
$$

Comparing $p ^ { S O ^ { \# } }$ with $p ^ { S O ^ { \# \# } }$ yields:

$$
p ^ {S O ^ {\#}} - p ^ {S O ^ {\# \#}} = k (b - a - d),
$$

which is $0 \mathrm { i f } b \geq a$ and less than $0 { \mathrm { ~ i f ~ } } b < a .$ As such, we have $p ^ { s o ^ { \# } } < p ^ { s o ^ { \# \# } }$ , and for the shared service to be outsourced, we need $p ^ { s o } \leq$ $p ^ { S O ^ { \# } }$ . There are two cases:

(1) I $\begin{array} { r } { \mathrm { f } p ^ { s o } \leq p ^ { s o ^ { \# } } } \end{array}$ , the shared service is outsourced, and the vendor’s profit function is concave in $q ^ { s o }$ . Using FOC yields the optimal IT service quality for outsourcing as $\begin{array} { r } { q ^ { S O } = \frac { 1 } { 2 \alpha ^ { o } } } \end{array}$ . The vendor faces a Bertrand competition with Gov-A and has an incentive to “undercut” Gov-A unless its price hits its marginal cost. In particular, the vendor can lower its price enough to incentivize outsourcing and makes non-negative profits if

$$
C ^ {S O} \leq C ^ {S I} + [ (q ^ {S O} - q ^ {S I}) - k a ] (N _ {A} + N _ {B}).
$$

To satisfy the boundary condition, we need $\Delta _ { \alpha } \geq$ . Therefore, the equilibrium exists if and only if $\Delta _ { \alpha } \geq k a$ . The others can be obtained by substituting back the optimal service quality to the respective functions. Note that neither the vendor nor Gov-A has an incentive to deviate from this equilibrium as doing so does not improve their profit or surplus.

(2) If $p ^ { s o } > p ^ { s o ^ { \# } }$ , the shared service is insourced, and Gov-A’s surplus is concave in Gov-A’s quality $q ^ { S I }$ . Using FOC yields the optima IT service quality for insourcing as $\begin{array} { r } { q ^ { S I } = \frac { 1 } { 2 \alpha ^ { I } } } \end{array}$ . This happens if the vendor is unable to undercut $\mathbf { G o v - A } , \mathrm { i . e . }$

$$
C ^ {S O} > C ^ {S I} + \left[ \left(q ^ {S O} - q ^ {S I}\right) - k a \right] \left(N _ {A} + N _ {B}\right).
$$

To satisfy the boundary condition, we need $\Delta _ { \alpha } <$ . The others can be obtained by substituting back the optimal service quality to the respective functions. Note that neither the vendor nor Gov-A has an incentive to deviate from this equilibrium as doing so does not improve their profit or surplus.

The results with respect to the governments’ decision on outsourcing of shared IT services in the cost-sharing regime are summarized in Table A2. Next, we proceed to examine the governments’ decision on whether to adopt a shared IT service. Depending on the location of the two governments, there are two cases: case (1) when $a < b$ and case (2) when $a \geq b$ . For brevity, we present here only the proof of case 1 because the proof of case 2 follows the same procedure. There are two subcases, as shown below.

a. If $\Delta _ { \alpha } \geq k a$ , in the non-shared service case, both outsource to the vendor individually, and in the shared service case, the shared service is outsourced to the vendor. Comparing Gov-A’s surplus between the two cases gives:

$$
W _ {A} ^ {S O ^ {C S}} - W _ {A} ^ {N O} = \big [ \phi \big [ N _ {A} ^ {(\beta - 1)} - (N _ {A} + N _ {B}) ^ {(\beta - 1)} \big ] - \psi d \big ] N _ {A}.
$$

So, $W _ { A } ^ { S O ^ { C S } } > W _ { A } ^ { N O }$ if

$$
\psi d <   \phi \big [ N _ {A} ^ {(\beta - 1)} - (N _ {A} + N _ {B}) ^ {(\beta - 1)} \big ].
$$

Comparing Gov-B’s surplus between the two cases gives:

$$
W _ {B} ^ {S O ^ {C S}} - W _ {B} ^ {N O} = \big [ \phi \big [ N _ {B} ^ {(\beta - 1)} - (N _ {A} + N _ {B}) ^ {(\beta - 1)} \big ] - \psi d \big ] N _ {B}.
$$

So, $W _ { B } ^ { S O ^ { C S } } > W _ { B } ^ { N O } \mathrm { ~ i f ~ }$

$$
\psi d <   \phi \big [ N _ {B} ^ {(\beta - 1)} - (N _ {A} + N _ {B}) ^ {(\beta - 1)} \big ].
$$

It can be verified that ${ N _ { A } } ^ { ( \beta - 1 ) } \le { N _ { B } } ^ { ( \beta - 1 ) }$ for $N _ { A } \geq N _ { B }$ and $0 < \beta < 1$ . Thus, for both to be satisfied, we need

$$
\psi d <   \phi \big [ N _ {A} ^ {(\beta - 1)} - (N _ {A} + N _ {B}) ^ {(\beta - 1)} \big ].
$$

b. If $\Delta _ { \alpha } < k a .$ , in the non-shared service case, both choose Gov-A individually, and in the shared service case, the shared service is insourced. Comparing Gov-A’s surplus between the two cases gives:

$$
W _ {A} ^ {S I ^ {C S}} - W _ {A} ^ {N I} = \big [ \phi \big [ N _ {A} ^ {(\beta - 1)} - (N _ {A} + N _ {B}) ^ {(\beta - 1)} \big ] - \psi d \big ] N _ {A} + (\Delta_ {\alpha} - k a) N _ {B}.
$$

So, $W _ { A } ^ { S I } { } ^ { C S } > W _ { A } ^ { N I }$ if

$$
\psi d <   \phi \big [ N _ {A} ^ {(\beta - 1)} - (N _ {A} + N _ {B}) ^ {(\beta - 1)} \big ] - \frac {(k a - \Delta_ {\alpha}) N _ {B}}{N _ {A}}.
$$

Comparing Gov-B’s surplus between the two cases yields:

$$
W _ {B} ^ {S I ^ {C S}} - W _ {B} ^ {N I} = \big [ \phi \big [ N _ {B} ^ {(\beta - 1)} - (N _ {A} + N _ {B}) ^ {(\beta - 1)} \big ] - \psi d \big ] N _ {B} + (k a - \Delta_ {\alpha}) N _ {B}.
$$

So, $W _ { B } ^ { S I } { } ^ { C S } > W _ { B } ^ { N I }$ if

$$
\psi d <   \phi \big [ N _ {B} ^ {(\beta - 1)} - (N _ {A} + N _ {B}) ^ {(\beta - 1)} \big ] + \frac {(k a - \Delta_ {\alpha}) N _ {B}}{N _ {A}}.
$$

Intuitively, for both to opt for the shared service, we need

$$
\psi d <   \phi \big [ N _ {A} ^ {(\beta - 1)} - (N _ {A} + N _ {B}) ^ {(\beta - 1)} \big ] - \frac {(k a - \Delta_ {\alpha}) N _ {B}}{N _ {A}}.
$$

for both to be satisfied.

## Proof of Lemma A3

Like Lemma A2, we first consider the subgame where a shared IT service is adopted and then use backward induction to solve the game. As discussed in the paper, a shared IT service is insourced only if it benefits both Gov-A and B; otherwise, acting as a profit center, Gov-A could set a price to capture Gov-B’s entire surplus. Therefore, the shared service will be insourced if $W _ { A } ^ { S O } \leq W _ { A } ^ { S I }$ , that is,

$$
p ^ {S I} \geq [ (q ^ {S O} - q ^ {S I}) - k a ] N _ {A} + C ^ {S I} - \frac {p ^ {S O} N _ {A}}{(N _ {A} + N _ {B})} = p ^ {S I ^ {*}},
$$

and $W _ { B } ^ { S O } \leq W _ { B } ^ { S I }$ , that is,

$$
p ^ {S I} \leq \frac {p ^ {S O} N _ {B}}{(N _ {A} + N _ {B})} - [ (q ^ {S O} - q ^ {S I}) - k (b - d) ] N _ {B} = p ^ {S I ^ {* *}}.
$$

Taking the difference between $p ^ { S I ^ { * * } }$ and $p ^ { S I ^ { * } }$ yields:

$$
p ^ {S I ^ {* *}} - p ^ {S I ^ {*}} = p ^ {S O} - C ^ {S I} - (q ^ {S O} - q ^ {S I}) (N _ {A} + N _ {B}) + k [ a N _ {A} + (b - d) N _ {B} ].
$$

The region for insourcing of the shared service is non-empty $\mathrm { i f } \ p ^ { S I ^ { * } } < p ^ { S I ^ { * * } }$ , which can be rearranged to:

$$
p ^ {S O} > C ^ {S I} + (q ^ {S O} - q ^ {S I}) (N _ {A} + N _ {B}) - k [ a N _ {A} + (b - d) N _ {B} ] = p ^ {S O ^ {*}}.
$$

Hence, there are two cases:

(1) If $p ^ { s o } \leq p ^ { s o ^ { * } }$ , the shared IT service is outsourced. The vendor faces a Bertrand competition with Gov-A and has an incentive to “undercut” Gov-A unless its price hits its marginal cost. In particularly, if $C ^ { s o } \leq p ^ { s o ^ { * } }$ , the vendor can lower its price enough to incentivize outsourcing and makes non-negative profits. To satisfy the boundary condition, we need $\begin{array} { r } { \Delta _ { \alpha } \ge \frac { k [ a N _ { A } + \hat { ( } b - d ) N _ { B } ] } { ( N _ { A } + N _ { B } ) } . } \end{array}$ . Therefore, the equilibrium exists if and only if $\begin{array} { r } { \mathbf { \dot { \Delta } } \Delta _ { \alpha } \ge \frac { k \left[ a N _ { A } + ( b - d ) N _ { B } \right] } { ( N _ { A } + N _ { B } ) } } \end{array}$ . To maximize the its profit, the vendor sets $p ^ { s o ^ { P C } } = p ^ { s o ^ { * } }$ . The vendor’s profit function is concave in $q ^ { s o }$ , and using FOC yields the optimal IT service quality for the shared service in outsourcing as $q ^ { s o } = $ ${ \frac { \mathbf { \bar { \rho } } _ { 1 } } { 2 \alpha ^ { o } } } .$ The others can be obtained by substituting back the optimal service quality to the respective functions.

(2) If $\cdot _ { p } s o  > p ^ { S O ^ { * } }$ , the shared service is insourced if the vendor is unable to undercut Gov-A, i.e., $C ^ { S O } > p ^ { S O ^ { * } }$ . To satisfy the boundary condition, we need $\begin{array} { r } { \Delta _ { \alpha } < \frac { k \left[ a N _ { A } + ( b - d ) N _ { B } \right] } { ( N _ { A } + N _ { B } ) } } \end{array}$ . In this case, Gov-A charges Gov-B a surplus-maximizing price of

$$
p ^ {S I ^ {P C}} = \frac {C ^ {S O} N _ {B}}{(N _ {A} + N _ {B})} - [ (q ^ {S O} - q ^ {S I}) - k (b - d) ] N _ {B}
$$

for providing the shared service. Gov-A’s surplus is concave in its quality $q ^ { S I }$ , and using FOC yields the optimal IT service quality for the shared IT service in insourcing as $\begin{array} { r } { q ^ { S I } = \frac { 1 } { 2 \alpha ^ { I } } . } \end{array}$ The others can be obtained by substituting back the optimal service quality to the respective functions.

Note that neither the vendor nor Gov-A has an incentive to deviate from this equilibrium as doing so does not improve their profit or surplus. The results with respect to the governments’ decision on outsourcing of shared IT services in the profit-center regime are summarized in Table A3. Following the same procedure as that in the proof of Lemma A2, we can derive governments’ decision on whether to adopt shared IT service in Lemma A3.

## Proof of Proposition 1

1. When the vendor’s technology advantage is low, i.e., $\begin{array} { r } { \Delta _ { \alpha } < \frac { k \left[ a N _ { A } + ( b - d ) N _ { B } \right] } { ( N _ { A } + N _ { B } ) } } \end{array}$ , the shared IT service is insourced in both regimes. Subtracting the per-unit insourcing price by the per-unit development cost gives:

$$
\frac {p ^ {S I ^ {P C}}}{N _ {B}} - \frac {C ^ {S I}}{N _ {A} + N _ {B}} = k (b - d) - \Delta_ {\alpha}.
$$

The difference is greater than 0 if $0 < \Delta _ { \alpha } < k ( b - d )$ and less than $\begin{array} { r } { 0 \mathrm { ~ i f ~ } k ( b - d ) < \Delta _ { \alpha } < \frac { k [ a N _ { A } + ( b - d ) N _ { B } ] } { ( N _ { A } + N _ { B } ) } } \end{array}$ It can be verified that the same result holds for Gov-A’s surplus.

When the vendor’s technology advantage is moderate, $\begin{array} { r } { \mathrm { i . e . , } \frac { k \left[ a N _ { A } + ( b - d ) N _ { B } \right] } { \left( N _ { A } + N _ { B } \right) } \le \Delta _ { \alpha } < } \end{array}$ <sub>????</sub>, the shared IT service is insourced in the cost-sharing regime and outsourced in the profit-center regime. Taking the difference between Gov-A’s surplus in the two cases yields:

$$
W _ {A} ^ {S I ^ {C S}} - W _ {A} ^ {S O ^ {P C}} = - \frac {k (a - b + d) N _ {A} N _ {B}}{(N _ {A} + N _ {B})} \leq 0.
$$

We can also verify that the same result hold for $\Delta _ { \alpha } \geq k a ,$ , where Gov-A outsources in both regimes.

2. When the shared IT service is outsourced in both regimes, i.e. $, \Delta _ { \alpha } > k a$ . Subtracting the outsourcing prices between the two regimes gives:

$$
p ^ {S O ^ {P C}} - p ^ {S O ^ {C S}} = k (a - b + d) N _ {B} \geq 0.
$$

It can be verified that the same result holds for the vendor’s profit.

3. The shared IT service is outsourced in the cost-sharing regime if $\Delta _ { \alpha } \geq k a$ , and in the profit-center regime if $\begin{array} { r } { \Delta _ { \alpha } \ge \frac { k \left[ a N _ { A } + ( b - d ) N _ { B } \right] } { ( N _ { A } + N _ { B } ) } . } \end{array}$ Comparing the two lower bounds, we have

$$
k a - \frac {k [ a N _ {A} + (b - d) N _ {B} ]}{(N _ {A} + N _ {B})} = \frac {k (a - b + d) N _ {B}}{(N _ {A} + N _ {B})} \geq 0.
$$

So, the lower bound for outsourcing is higher in the cost-sharing regime than in the profit-center regime.

## Proof of Proposition 2

It follows from Lemma A2 and Lemma A3 that the governments choose to adopt a shared IT service if <sub>??</sub> is not very large. Comparing the upper bounds of <sub>??</sub> between them yields the following results:

1. When $\Delta _ { \alpha } < k ( b - d )$ , taking the difference of the upper bound of <sub>??</sub> between the cost-sharing and profit-center regimes yields:

$$
\widehat {\Delta} _ {1} - \frac {[ k (b - d) - \Delta_ {\alpha} ] N _ {B}}{N _ {A}} - \widehat {\Delta} _ {1} = - \frac {[ k (b - d) - \Delta_ {\alpha} ] N _ {B}}{N _ {A}} <   0.
$$

Thus, the upper bound of  for sharing IT services is higher in the profit-center regime when $\Delta _ { \alpha } < k ( b - d )$ , and this implies that the governments that do not benefit from sharing IT services under the cost-sharing regime due to a large compatibility cost may instead find it beneficial to do so in the profit-center regime.

2. When $\Delta _ { \alpha } \geq k ( b - d )$ , taking the difference of the upper bound of <sub>??</sub> between the cost-sharing and profit-center regimes yields:

$$
\begin{array}{r l r} & & {\hat {\Delta} _ {1} - \left(\hat {\Delta} _ {1} - \frac {[ \Delta_ {\alpha} - k (b - d) ] N _ {B}}{N _ {A}}\right) = \frac {[ \Delta_ {\alpha} - k (b - d) ] N _ {B}}{N _ {A}} \geq 0} \\ & & {\mathrm{if} k (b - d) \leq \Delta_ {\alpha} <   \frac {k [ a N _ {A} + (b - d) N _ {B} ]}{(N _ {A} + N _ {B})}, \mathrm{or}} \\ & & {\hat {\Delta} _ {1} - \left(\hat {\Delta} _ {1} - \frac {k [ a N _ {A} + (b - d) N _ {B} ]}{(N _ {A} + N _ {B})}\right) = \frac {k [ a N _ {A} + (b - d) N _ {B} ]}{(N _ {A} + N _ {B})} \geq 0} \\ & & {\mathrm{if} \Delta_ {\alpha} \geq \frac {k [ a N _ {A} + (b - d) N _ {B} ]}{(N _ {A} + N _ {B})}.} \end{array}
$$

As such, the upper bound of for sharing IT services is lower in the profit-center regime when $\Delta _ { \alpha } \geq k ( b - d )$ , and this implies that the governments that do not benefit from sharing IT services under the profit-center regime due to a large compatibility cost may instead find it beneficial to do so in the cost-sharing regime.

## Proof of Lemma A4

We first consider the subgame where a shared IT service is adopted and then use backward induction to solve the game. As discussed in the paper, because Gov-A has the capability to develop in-house, it has the liberty not to implement a shared IT service if doing so does not benefit itself. Thus, for a shared IT service to be outsourced, it is necessary for the vendor to induce Gov-A to choose outsourcing. As such, the shared service will be outsourced if $W _ { A } ^ { S O } \geq W _ { A } ^ { S I }$ , that is,

$$
p ^ {S O} \leq C ^ {S I} + [ (q ^ {S O} - q ^ {S I}) ] (N _ {A} + N _ {B}) - k [ a N _ {A} + (b - d) N _ {B} ] = p ^ {S O ^ {\# \#}}.
$$

There are two cases:

(1) If $p ^ { s o } \leq p ^ { s o ^ { \# \# } }$ , the shared service is outsourced, and the vendor’s profit function is concave in $q ^ { s o }$ . Using FOC yields the optimal IT service quality for outsourcing as $\begin{array} { r } { q ^ { S O } = \frac { 1 } { 2 \alpha ^ { o } } . } \end{array}$ . The vendor faces a Bertrand competition with Gov-A and has an incentive to “undercut” Gov-A unless its price hits its marginal cost. In particular, the vendor can lower its price enough to incentivize outsourcing and makes non-negative profits if

$$
C ^ {S O} \leq p ^ {S O ^ {\# \#}}.
$$

To satisfy the boundary condition, we need $\Delta _ { \alpha } \geq$ <sub>????</sub>. Therefore, the equilibrium exists if and only if $\begin{array} { r } { \Delta _ { \alpha } \ge \frac { k \left[ a N _ { A } + ( b - d ) N _ { B } \right] } { ( N _ { A } + N _ { B } ) } } \end{array}$ . The others can be obtained by substituting back the optimal service quality to the respective functions. Note that neither the vendor nor Gov-A has an incentive to deviate from this equilibrium as doing so does not improve their profit or surplus.

(2) $\operatorname { I f } p ^ { s o } > p ^ { s o ^ { \# \# } }$ , the shared service is insourced, and Gov-A’s surplus is concave in Gov-A’s quality $q ^ { S I }$ . Using FOC yields the

optimal IT service quality for insourcing as $\begin{array} { r } { q ^ { S I } = \frac { 1 } { 2 \alpha ^ { I } } . } \end{array}$ This happens if the vendor is unable to undercut Gov-A, i.e.,

$$
C ^ {S O} > p ^ {S O ^ {\# \#}}.
$$

To satisfy the boundary condition, we need $\begin{array} { r } { \Delta _ { \alpha } < \frac { k \left[ a N _ { A } + ( b - d ) N _ { B } \right] } { ( N _ { A } + N _ { B } ) } } \end{array}$ . The others can be obtained by substituting back the optimal service quality to the respective functions. Note that neither the vendor nor Gov-A has an incentive to deviate from this equilibrium as doing so does not improve their profit or surplus.

The results with respect to the governments’ decision on outsourcing of shared IT services in the profit-center regime are summarized in Table A4. Following the same procedure as that in the proof of Lemma A2, we can derive governments’ decision on whether to adopt shared IT service in Lemma A4.

## Proof of Proposition 3

We present the proof for the cost-sharing regime here, the proof for the profit-center regime follows the same procedure. It follows from Lemma A2 that under the cost-sharing regime, the two governments adopt a shared service if (1). $\Delta _ { \alpha } \geq k ( b - d )$ and $0 < \psi d \leq \widehat { \Delta } _ { 1 }$ or (2). $0 < \Delta _ { \alpha } < k ( b - d )$ and $\begin{array} { r } { 0 < \psi d \le \hat { \Delta } _ { 1 } - \frac { \bar { [ k ( b - d ) - \Delta _ { \alpha } ] } N _ { B } } { N _ { A } } } \end{array}$ . On the other hand, we have shown in Lemma A4 that under the coordination regime, the two governments share IT services if $\psi d \leq \hat { \Delta } _ { 2 } .$ . Given these results and the fact that $\hat { \Delta } _ { 1 } < \hat { \Delta } _ { 2 }$ for $N _ { A } \geq N _ { B }$ and $0 < \beta < 1$ , it is intuitive that under the following conditions, the governments will not voluntarily the share IT services in the cost-sharing regime even though doing

so improves their collective surplus:

$$
(1). \Delta_ {\alpha} \geq k (b - d) \mathrm{and} \hat {\Delta} _ {1} <   \psi d \leq \hat {\Delta} _ {2}, (2). 0 <   \Delta_ {\alpha} <   k (b - d) \mathrm{and} \hat {\Delta} _ {1} - \frac {[ k (b - d) - \Delta_ {\alpha} ] N _ {B}}{N _ {A}} <   \psi d \leq \hat {\Delta} _ {2}.
$$

## Proof of Proposition 4

We analyze the vendor’s pricing and profit in the cost-sharing regime below. The analysis for the profit-center regime is similar and thus is omitted for brevity.

(i) When the shared service is outsourced, the proportion paid by Gov-B is $\frac { p ^ { S O ^ { C S } } N _ { B } } { ( N _ { A } + N _ { B } ) } .$ Taking the difference between $\frac { p ^ { S O ^ { C S } } N _ { B } } { ( N _ { A } + N _ { B } ) } \mathrm { a n d } p _ { B } ^ { N O }$ yields

$$
\frac {p ^ {S O ^ {C S}} N _ {B}}{(N _ {A} + N _ {B})} - p _ {B} ^ {N O} = \big [ \psi d - \phi \big [ N _ {B} ^ {(\beta - 1)} - (N _ {A} + N _ {B}) ^ {(\beta - 1)} \big ] - k (a - b + d) \big ] N _ {B}.
$$

So $\frac { p ^ { S O ^ { C S } } N _ { B } } { ( N _ { A } + N _ { B } ) } < p _ { B } ^ { N O }$ when <sub>??</sub> $< \phi \big [ { \cal N } _ { B } ^ { ~ ( \beta - 1 ) } - ( { \cal N } _ { A } + { \cal N } _ { B } ) ^ { ( \beta - 1 ) } \big ] + k ( a - b + d )$ , which can be shown to be always satisfied in this case.

(ii) When the shared service is outsourced, the proportion paid by $\begin{array} { r } { \mathrm { G o v - A i s } \frac { p ^ { S O ^ { C S } } N _ { A } } { ( N _ { A } + N _ { B } ) } . } \end{array}$ Taking the difference between $\frac { p ^ { S O ^ { C S } } N _ { A } } { ( N _ { A } + N _ { B } ) }$ and $p _ { A } ^ { N O }$ yields

$$
\frac {p ^ {S O ^ {C S}} N _ {A}}{(N _ {A} + N _ {B})} - p _ {A} ^ {N O} = \big (\psi d - \hat {\Delta} _ {1} \big) N _ {A}.
$$

Therefore, $\begin{array} { r } { \frac { p ^ { S O ^ { C S } } N _ { A } } { ( N _ { A } + N _ { B } ) } < p _ { A } ^ { N O } \mathrm { ~ i f ~ } \psi d < \hat { \Delta } _ { 1 } . } \end{array}$ , which can be shown to be always satisfied in this case.

(iii) When $\varDelta _ { \alpha } \geq k a$ , the IT services are outsourced in both the shared and the non-shared service cases. Comparing the vendor’s profit in these two cases yields:

$$
\pi^ {S O ^ {C S}} - \pi^ {N O} = - k (a - b + d) N _ {B} \leq 0,
$$

where the inequality follows as it can be shown that $a - b + d \geq 0 . { \mathrm { A s } }$ such, under the cost-sharing regime, the vendor receives no more profit from the shared service case than that in the non-shared service case.

## Proof of Proposition 5

We analyze the three regimes with respect to social welfare. For brevity, we show only the proof for the cost-sharing regime as follows. The derivations for the profit-center and coordination regimes follow the same procedure. Depending on the location of the two governments, there are two cases: case (1) when $a < b$ and case (2) when $a \geq b$ . For brevity, we present here only the proof of case 1 because the proof of case 2 follows the same procedure.

a. If $\Delta _ { \alpha } \geq k a$ , the IT services are outsourced in both the shared and non-shared service cases (from Lemma A2). Comparing the

social welfare in the two cases yields:

$$
S W ^ {S O ^ {C S}} - S W ^ {N O} = \left[ \phi \frac {\left(N _ {A} ^ {\beta} + N _ {B} ^ {\beta}\right) - (N _ {A} + N _ {B}) ^ {\beta}}{(N _ {A} + N _ {B})} - \psi d \right] (N _ {A} + N _ {B}).
$$

$\begin{array} { r } { \mathrm { S o } , S W ^ { s o ^ { C S } } > S W ^ { N o } \mathrm { ~ i f ~ } \psi d < \phi \frac { \left( N _ { A } { } ^ { \beta } + N _ { B } { } ^ { \beta } \right) - ( N _ { A } + N _ { B } ) ^ { \beta } } { ( N _ { A } + N _ { R } ) } = \widehat \Delta _ { 2 } } \end{array}$ Intuitively, the governments share the IT services if <sub>??</sub> $l < \hat { \Delta } _ { 1 } < \hat { \Delta } _ { 2 }$ , and thus this decision is also socially optimal in this case.

b. If $\Delta _ { \alpha } < k a$ , the governments choose insourcing in both cases (from Lemma A2). Comparing the social welfare in the two

cases yields:

$$
S W ^ {S I ^ {C S}} - S W ^ {N I} = \big (\hat {\Delta} _ {2} - \psi d \big) (N _ {A} + N _ {B}).
$$

$\mathrm { S o } , S W ^ { S I } { } ^ { C S } > S W ^ { N I } \mathrm { i f } \psi d < \hat { \Delta } _ { 2 }$ . Note that the governments choose to share the IT services only when $\begin{array} { r } { \psi d \leq \widehat { \Delta } _ { 1 } - \frac { [ k ( b - d ) - \Delta _ { \alpha } ] N _ { B } } { N _ { A } } < \widehat { \Delta } _ { 2 } , } \end{array}$ Hence the outsourcing/insourcing decision on the shared service will also result in higher social welfare.

## Proof of Proposition 6

We analyze the three regimes with respect to the effect of Gov-B’s size on the adoption of a shared IT service as follows.

## 1. Cost-sharing regime

The two governments will adopt a shared service if (a) $\Delta _ { \alpha } \geq k ( b - d )$ and $0 < \psi d \leq \hat { \Delta } _ { 1 } \mathrm { o r } \mathrm { ( b ) } 0 < \Delta _ { \alpha } < k ( b - d )$ and $0 < \psi d \leq \hat { \Delta } _ { 1 } -$ $[ k ( b - d ) - \Delta _ { \alpha } ] N _ { B }$ N

(a) When $\Delta _ { \alpha } \geq k ( b - d )$ , taking the derivative of the upper bound $\hat { \Delta } _ { 1 }$ with respect to $N _ { B }$ yields:

$$
\frac {d \hat {\Delta} _ {1}}{d N _ {B}} = \phi (1 - \beta) (N _ {A} + N _ {B}) ^ {(\beta - 2)} > 0,
$$

for $N _ { A } \geq N _ { B }$ and $0 < \beta < 1 . \mathrm { S o } .$ , the $\hat { \Delta } _ { 1 }$ is an increasing function of $N _ { B }$ and maximizes at $N _ { B } = N _ { A }$

(b) When $0 < \Delta _ { \alpha } < k ( b - d )$

Taking the second order derivative of the upper bound $\begin{array} { r } { \left[ \widehat { \Delta } _ { 1 } - \frac { \left[ k \left( b - d \right) - \Delta _ { \alpha } \right] N _ { B } } { N _ { A } } \right] } \end{array}$ with respect to $N _ { B }$ yields:

$$
\frac {d ^ {2} \left[ \hat {\Delta} _ {1} - \frac {[ k (b - d) - \Delta_ {\alpha} ] N _ {B}}{N _ {A}} \right]}{d N _ {B} ^ {2}} = - \phi (1 - \beta) (2 - \beta) (N _ {A} + N _ {B}) ^ {(\beta - 2)} <   0.
$$

$\mathrm { S o } ,$ it is a concave function of $N _ { B } . { \mathrm { U s i n g ~ F O C } } .$ , we have

$$
\frac {d \left[ \hat {\Delta} _ {1} - \frac {[ k (b - d) - \Delta_ {\alpha} ] N _ {B}}{N _ {A}} \right]}{d N _ {B}} = \phi (1 - \beta) (N _ {A} + N _ {B}) ^ {(\beta - 2)} - \frac {[ k (b - d) - \Delta_ {\alpha} ]}{N _ {A}} = 0,
$$

Solving it gives

$$
N _ {B} ^ {*} = \left[ \frac {\phi (1 - \beta) N _ {A}}{k (b - d) - \Delta_ {\alpha}} \right] ^ {\frac {1}{2 - \beta}} - N _ {A}.
$$

Next, we check if there are corner solutions. Reorganizing ${ N _ { B } } ^ { * }$ , we have:

$$
N _ {B} ^ {*} = \left[ \frac {\phi (1 - \beta) N _ {A}}{k (b - d) - \Delta_ {\alpha}} \right] ^ {\frac {1}{2 - \beta}} - N _ {A} = N _ {A} ^ {\frac {1}{2 - \beta}} \left[ \left[ \frac {\phi (1 - \beta)}{k (b - d) - \Delta_ {\alpha}} \right] ^ {\frac {1}{2 - \beta}} - N _ {A} ^ {\frac {1 - \beta}{2 - \beta}} \right]
$$

We first check if ${ N _ { B } } ^ { * } = 0$ can be a corner solution. In particular, this happens if ${ N _ { B } } ^ { * } \leq 0 ,$ that is

$$
\left[ \frac {\phi (1 - \beta)}{k (b - d) - \Delta_ {\alpha}} \right] ^ {\frac {1}{2 - \beta}} \leq N _ {A} ^ {\frac {1 - \beta}{2 - \beta}},
$$

which can be rewritten as

$$
\Delta_ {\alpha} \leq k (b - d) - \phi (1 - \beta) N _ {A} ^ {(\beta - 1)}.
$$

Using the assumption $\begin{array} { r } { k ( b - d ) \leq \frac { \phi [ N _ { A } { } ^ { ( \beta - 1 ) } - ( N _ { A } + N _ { B } ) ^ { ( \beta - 1 ) } ] N _ { A } } { N _ {  } } ; } \end{array}$ , we have

$$
\begin{array}{r l} & {\Delta_ {\alpha} \leq \frac {\phi N _ {A}}{N _ {B}} \big [ N _ {A} ^ {(\beta - 1)} - (N _ {A} + N _ {B}) ^ {(\beta - 1)} - N _ {A} ^ {(\beta - 2)} N _ {B} \big ]} \\ & {\quad <   \frac {\phi N _ {A}}{N _ {B}} \big [ N _ {A} ^ {(\beta - 1)} - (N _ {A} + 0) ^ {(\beta - 1)} - N _ {A} ^ {(\beta - 2)} 0 \big ] = 0.} \end{array}
$$

The second inequality follows from

$$
\frac {d \left[ N _ {A} ^ {(\beta - 1)} - (N _ {A} + N _ {B}) ^ {(\beta - 1)} - N _ {A} ^ {(\beta - 2)} N _ {B} \right]}{d N _ {A}} = (1 - \beta) (N _ {A} + N _ {B}) ^ {(\beta - 2)} - N _ {A} ^ {(\beta - 2)} <   0.
$$

Therefore, it implies $\Delta _ { \alpha } < 0 .$ , which contradicts with $0 < \Delta _ { \alpha } < k ( b - d )$ . As such, ${ { N } _ { B } } ^ { * }$ has to be positive, which rules out ${ N _ { B } } ^ { * } = 0$ as a corner solution.

Second, we check if ${ N _ { B } } ^ { * } = { N _ { A } }$ can be a corner solution. In particular, this happens if ${ N _ { B } } ^ { * } \geq N _ { A }$ , that is,

$$
\left[ \frac {\phi (1 - \beta) N _ {A}}{k (b - d) - \Delta_ {\alpha}} \right] ^ {\frac {1}{2 - \beta}} - N _ {A} \geq N _ {A},
$$

which can be rewritten as

$$
\Delta_ {\alpha} \geq k (b - d) - \phi (1 - \beta) 2 ^ {(\beta - 2)} N _ {A} ^ {(\beta - 1)}.
$$

It can be verified and as shown in our numerical example that $k ( b - d ) - \phi ( 1 - \beta ) 2 ^ { ( \beta - 2 ) } N _ { A } ^ { ( \beta - 1 ) } > 0$ does not always lead to an empty parameter region. Thus, when $k ( b - d ) - \phi ( 1 - \beta ) 2 ^ { ( \beta - 2 ) } { N _ { A } } ^ { ( \beta - 1 ) } \le \Delta _ { \alpha } < k ( b - d )$ , we have a corner solution ${ N _ { B } } ^ { * } = { N _ { A } }$ , and when $0 <$ $\Delta _ { \alpha } { < } k ( b - d ) - \phi ( 1 - \beta ) 2 ^ { ( \beta - 2 ) } { N _ { A } } ^ { ( \beta - 1 ) }$ , we have an interior solution:

$$
N _ {B} ^ {*} = \left[ \frac {\phi (1 - \beta) N _ {A}}{k (b - d) - \Delta_ {\alpha}} \right] ^ {\frac {1}{2 - \beta}} - N _ {A}.
$$

## 2. Profit-center regime

The two governments share IT services $\begin{array} { r } { \vert \mathrm { f \left( a \right) } \Delta _ { \alpha } \ge \frac { k \left[ a N _ { A } + \left( b - d \right) N _ { B } \right] } { \left( N _ { A } + N _ { B } \right) } \mathrm { a n d } 0 < \psi d < \hat { \Delta } _ { 1 } - \frac { k \left( a - b + d \right) N _ { B } } { \left( N _ { A } + N _ { B } \right) } \mathrm { , ~ o r ~ } ( b ) k \left( b - d \right) \le \Delta _ { \alpha } < \frac { k \left[ a N _ { A } + \left( b - d \right) N _ { B } \right] } { \left( N _ { A } + N _ { B } \right) } } \end{array}$ and $\begin{array} { r } { 0 < \psi d < \hat { \Delta } _ { 1 } - \frac { [ \Delta _ { \alpha } - k ( b - d ) ] N _ { B } } { N _ { A } } \mathrm { o r } , ( \mathrm { c } ) 0 < \Delta _ { \alpha } < k ( b - d ) \mathrm { a n d } 0 < \psi d < \hat { \Delta } _ { 1 } } \end{array}$

(a) When $\begin{array} { r } { \Delta _ { \alpha } \ge \frac { k [ a N _ { A } + ( b - \dot { d } ) ^ { } N _ { B } ] } { ( N _ { A } + N _ { B } ) } } \end{array}$ , taking the derivative of the upper bound of <sub>??</sub> with respect to $N _ { B }$ gives

$$
\frac {d \left[ \hat {\Delta} _ {1} - \frac {k (a - b + d) N _ {B}}{(N _ {A} + N _ {B})} \right]}{d N _ {B}} = \phi (1 - \beta) (N _ {A} + N _ {B}) ^ {(\beta - 2)} - \frac {k (a - b + d) N _ {A}}{(N _ {A} + N _ {B}) ^ {2}}.
$$

When $a < b ,$

$$
\frac {d \left[ \hat {\Delta} _ {1} - \frac {k (a - b + d) N _ {B}}{(N _ {A} + N _ {B})} \right]}{d N _ {B}} = \phi (1 - \beta) (N _ {A} + N _ {B}) ^ {(\beta - 2)} > 0.
$$

When $a \geq b ,$

$$
\begin{array}{l} \frac {d \left[ \hat {\Delta} _ {1} - \frac {k (a - b + d) N _ {B}}{(N _ {A} + N _ {B})} \right]}{d N _ {B}} = \phi (1 - \beta) (N _ {A} + N _ {B}) ^ {(\beta - 2)} - \frac {2 k (a - b) N _ {A}}{(N _ {A} + N _ {B}) ^ {2}} \\ > \frac {\phi \big [ (N _ {A} + N _ {B}) ^ {(\beta - 1)} [ (1 - \beta) N _ {B} + N _ {A} ] - N _ {A} ^ {\beta} \big ]}{(N _ {A} + N _ {B}) N _ {B}} > 0. \end{array}
$$

The first inequality holds as it is assumed tha $\begin{array} { r } { k \le \frac { \phi \left[ { \overset { . . . } N _ { A } } ^ { ( \beta - 1 ) ^ { - } } - ( { \overset { . . . } N _ { A } } + N _ { B } ) ^ { ( \beta - 1 ) } \right] ( N _ { A } + N _ { B } ) } { 2 ( a - b ) N _ { B } } } \end{array}$ when $a > b$ to ensure that the case of shared IT service outsourcing can appear in equilibrium. The second inequality holds as

$$
\frac {d \big [ (N _ {A} + N _ {B}) ^ {(\beta - 1)} [ (1 - \beta) N _ {B} + N _ {A} ] - N _ {A} ^ {\beta} \big ]}{d N _ {B}} = \beta (1 - \beta) (N _ {A} + N _ {B}) ^ {(\beta - 2)} N _ {B} > 0,
$$

so

$$
\left[ (N _ {A} + N _ {B}) ^ {(\beta - 1)} [ (1 - \beta) N _ {B} + N _ {A} ] - N _ {A} ^ {\beta} \right] > \left[ (N _ {A} + 0) ^ {(\beta - 1)} [ (1 - \beta) 0 + N _ {A} ] - N _ {A} ^ {\beta} \right] = 0
$$

when $N _ { B } > 0$

(b) When $\begin{array} { r } { k ( b - d ) \leq \Delta _ { \alpha } < \frac { k \left[ a N _ { A } + ( b - d ) N _ { B } \right] } { ( N _ { A } + N _ { B } ) } } \end{array}$ , taking derivative of the upper bound of <sub>??</sub> with respect to $N _ { B } \mathrm { : }$

$$
\begin{array}{l} \frac {d \left[ \hat {\Delta} _ {1} - \frac {[ \Delta_ {\alpha} - k (b - d) ] N _ {B}}{N _ {A}} \right]}{d N _ {B}} = \phi (1 - \beta) (N _ {A} + N _ {B}) ^ {(\beta - 2)} - \frac {[ \Delta_ {\alpha} - k (b - d) ]}{N _ {A}} \\ > \left[ \phi (1 - \beta) (N _ {A} + N _ {B}) ^ {(\beta - 2)} - \frac {k (a - b + d) N _ {B}}{(N _ {A} + N _ {B})} \right] \\ > \left[ \phi (1 - \beta) (N _ {A} + N _ {B}) ^ {(\beta - 2)} - \frac {k (a - b + d) N _ {A}}{(N _ {A} + N _ {B})} \right] > 0 \end{array}
$$

where the first inequality follows from $\begin{array} { r } { \Delta _ { \alpha } < \frac { k \left[ a N _ { A } + ( b - d ) N _ { B } \right] } { ( N _ { A } + N _ { B } ) } } \end{array}$ and the last follows the result from part (a).

(c) When $0 < \Delta _ { \alpha } < k ( b - d )$ , this is identical to part (a) in the cost-sharing regime.

## 3. Coordination regime

The two governments share the IT services in the coordination regime if $\begin{array} { r } { \psi d < \frac { \phi \left[ N _ { A } { } ^ { \beta } + N _ { B } { } ^ { \beta } - ( N _ { A } + N _ { B } ) ^ { \beta } \right] } { ( N _ { A } + N _ { B } ) } = \widehat \Delta _ { 2 } } \end{array}$ Taking the derivative of $\hat { \Delta } _ { 2 }$ with respect to $N _ { B }$ yields:

$$
\frac {d \widehat {\Delta} _ {2}}{d N _ {B}} = \frac {\phi}{(N _ {A} + N _ {B}) ^ {2}} \Big [ (1 - \beta) \big [ (N _ {A} + N _ {B}) ^ {\beta} - N _ {B} ^ {\beta} \big ] - N _ {A} \big [ N _ {A} ^ {(\beta - 1)} - \beta N _ {B} ^ {(\beta - 1)} \big ] \Big ]
$$

Intuitively, the first term is strictly positive given $0 < N _ { B } \le N _ { A }$ and $0 < \beta < 1$ . As such, a sufficient condition for $\begin{array} { r } { \frac { d \widehat { \Delta } _ { 2 } } { d N _ { B } } > 0 \mathrm { i s } { N _ { A } } ^ { ( \beta - 1 ) } - } \end{array}$ $\beta { N _ { B } } ^ { ( \beta - 1 ) } < 0$ , which can be rearranged as $N _ { B } < N _ { A } \beta ^ { \frac { 1 } { 1 - \beta } }$ . In addition, the first-order derivative evaluated at $N _ { B } = N _ { A }$ is

$$
\frac {d \hat {\Delta} _ {2}}{d N _ {B}} | _ {N _ {B} = N _ {A}} = \frac {\phi}{4 N _ {A} ^ {2}} \big [ (1 - \beta) N _ {A} ^ {\beta} (2 ^ {\beta} - 2) \big ] <   0,
$$

where the inequality follows from $0 < \beta < 1$ . So, $N _ { B } = N _ { A }$ cannot be a corner solution. Combined with the fact that $\begin{array} { r } { \frac { d \hat { \Delta } _ { 2 } } { d N _ { B } } > 0 \mathrm { i f } N _ { B } < N _ { A } \beta ^ { \frac { 1 } { 1 - \beta } } } \end{array}$ this suggests that there exists an interior solution to maximize $\hat { \Delta } _ { 2 }$ In addition, the second-order derivative of $\hat { \Delta } _ { 2 }$ with respect to $N _ { B }$ is

$$
\frac {d ^ {2} \hat {\Delta} _ {2}}{d N _ {B} ^ {2}} = \frac {\phi}{(N _ {A} + N _ {B}) ^ {3}} \Big [ 2 N _ {A} ^ {\beta} - 2 \beta (2 - \beta) N _ {A} N _ {B} ^ {(\beta - 1)} - \beta (1 - \beta) N _ {A} ^ {2} N _ {B} ^ {(\beta - 2)} - (1 - \beta) (2 - \beta) \big [ (N _ {A} + N _ {B}) ^ {\beta} - N _ {B} ^ {\beta} \big ] \Big ]
$$

Clearly, $\hat { \Delta } _ { 2 }$ is continuous and twice differentiable in $N _ { B }$ . Therefore, there exist one or more stationary points $N _ { B } \in \left( N _ { A } \beta ^ { \frac { 1 } { 1 - \beta } } , N _ { A } \right)$ that results $\begin{array} { r } { \mathrm { i n } \frac { d \hat { \Delta } _ { 2 } } { d N _ { B } } = 0 } \end{array}$ , and one of these points maximizes $\hat { \Delta } _ { 2 }$

## Proof of Proposition 7

First, note that when $> \hat { \Delta } _ { 2 } .$ ,Case NO is the equilibrium across all regimes and yields the same social welfare. Next, we examine the remaining regions, i.e., $\psi d \leq \hat { \Delta } _ { 2 }$ . There are four cases: case (1) when $\Delta _ { \alpha } > k a .$ , case (2) when $\begin{array} { r } { \frac { k \left[ a N _ { A } + ( b - d ) N _ { B } \right] } { \left( N _ { A } + N _ { B } \right) } < \Delta _ { \alpha } \leq } \end{array}$ <sub>????</sub>, and case (3) when $\begin{array} { r } { k ( b - d ) < \Delta _ { \alpha } \leq \frac { k \left[ a N _ { A } + ( b - d ) N _ { B } \right] } { ( N _ { A } + N _ { B } ) } } \end{array}$ , and case (4) when $0 < \Delta _ { \alpha } \leq k ( b - d )$ . We show the proof for case (1) below and we can follow the same procedure to derive the results in the other three cases. There are three subcases for case (1).

(a) $\begin{array} { r } { \psi d \leq \hat { \Delta } _ { 1 } - \frac { k \left( a - b + d \right) N _ { B } } { \left( N _ { A } + N _ { B } \right) } ; } \end{array}$ , Case SO is the equilibrium and yields the same social welfare across all regimes.

(b) $\begin{array} { r } { \widehat { \Delta } _ { 1 } - \frac { k ( a - b + d ) N _ { B } } { ( N _ { A } + N _ { B } ) } < \psi d \leq \widehat { \Delta } _ { 1 } } \end{array}$ , Case SO is the equilibrium in both the cost-sharing and coordination regimes whereas Case NO is the

equilibrium in the profit-center regime. Comparing these two yields:

$$
S W ^ {S O ^ {C S}} - S W ^ {N O} = \phi \big [ N _ {A} ^ {\beta} + N _ {B} ^ {\beta} - (N _ {A} + N _ {B}) ^ {\beta} \big ] - \psi d (N _ {A} + N _ {B}).
$$

$\begin{array} { r } { S W ^ { s o ^ { C S } } - S W ^ { N O } \geq 0 \mathrm { i f } \psi d \leq \hat { \Delta } _ { 2 } , } \end{array}$ , which is true in the parameter region examined. So, the social welfare is higher in cost-sharing and coordination regimes.

(c) $\widehat { \Delta } _ { 1 } < \psi d \leq \widehat { \Delta } _ { 2 }$ , Case SO is the equilibrium in the coordination regime whereas Case NO is the equilibrium in the other two. The

comparison result is identical to 1(b) above, so the coordination regime has the highest social welfare.

Putting together the results above with other cases yields Proposition 7.

## Proofs of Lemma A5-A9 and Proofs of Proposition 8-12

For brevity, we do not include the proofs of lemmas and propositions in the extensions in this document, as the primary purpose of these extensions was to show that our main findings remain qualitatively the same when several key assumptions are relaxed. The technical proofs of these lemmas and propositions are available upon request from the authors.
