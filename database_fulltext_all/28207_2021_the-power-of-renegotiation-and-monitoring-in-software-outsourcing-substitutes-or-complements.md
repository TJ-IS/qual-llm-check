---
otero_id: 28207
otero_key: "72VN8DNB"
title: "The Power of Renegotiation and Monitoring in Software Outsourcing: Substitutes or Complements?"
authors: "He Huang; Minhui Hu; Robert J. Kauffman; Hongyan Xu"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1026"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Power of Renegotiation and Monitoring in Software Outsourcing: Substitutes or Complements?

He Huang,<sup>a</sup> Minhui Hu,<sup>a</sup> Robert J. Kauffman,<sup>b,c</sup> Hongyan Xu<sup>a,</sup>\*

<sup>a</sup> School of Economics and Business Administration, Chongqing University, Chongqing 400044, China; <sup>b</sup> Department of Digitalization, Copenhagen School of Business, Frederiksberg 2000, Denmark; <sup>c</sup> School of Computing and Information Systems, Singapore Management University, Singapore 188065, Singapore

\*Corresponding author

Contact: huanghe@cqu.edu.cn, https://orcid.org/0000-0002-5437-6703 (HH); hu\_minhui@cqu.edu.cn, https://orcid.org/0000-0002-5288-4376 (MH); rk.digi@cbs.dk (RJK); xuhongyan@cqu.edu.cn, https://orcid.org/0000-0001-6681-390X (HX)

Received:

Revised:

Accepted:

<sup>February 28, 2021</sup>Published Online in Articles in Advance: August 31, 2021

https://doi.org/10.1287/isre.2021.1026

Copyright:

Abstract. Monitoring and contract renegotiation are two common solutions for addressing information asymmetry and uncertainty between a client and a vendor of software outsourcing services. Monitoring is mostly applied in time-and-materials contracts, as a basis for inspecting and reimbursing the vendor’s efforts in system development. Renegotiation, by contrast, is deployed in <sup>fi</sup>xed-price and time-and-materials contracts to mitigate the loss of surplus from uncertainty after system development. We investigate the interaction between monitoring and renegotiation and examine the corresponding contract choice problem. We <sup>fi</sup>nd that the client bene<sup>fi</sup>ts from renegotiation based on two effects: an uncertainty-resolution effect and a post-development incentive effect, which incentivizes the vendor to exert additional ef fort in system development. Monitoring does not resolve uncertainty, although it does encourage the vendor to exert additional effort, a pre-development incentive effect. Our analysis shows that the choice of renegotiation or monitoring depends on the interactions of the above effects, which are moderated by the renegotiation cost, monitoring cost, and bargaining power in renegotiation. When renegotiation cost is low: if the client has high bargaining power and low monitoring cost, monitoring and renegotiation are complements and both are selected; otherwise, the two instruments are substitutes and contract renegotiation is preferred. When renegotiation cost is high: monitoring substitutes for renegotiation and the client only chooses monitoring if the cost to do it is low; or else neither is used. Overall, this research shows that four appropriate contract strategies should be used under somewhat different circumstances. We further analyze the impacts of some other key aspects of software outsourcing and extend the base model to address two alternative situations to show the robustness of our <sup>fi</sup>ndings. The results apply to a range of software reliability growth models, including when machine learning or cloud computing are used.

History: Yong Tan, Senior Editor; Marius Niculescu, Associate Editor.

Funding: H. Huang was supported by the National Natural Science Foundation of China (NSFC) [Grant 71871032]. M. Hu was supported by PhD program funding at Chongqing University. H. Xu was supported by the NSFC [Grant 71972019] and the fundamental research funds for the Central Universities [Grant 2018 CDJSK02XK16]. R. J. Kauffman received prior sabbatical research funding from Singapore Management University, the 2018-2019 Otto Mønsted Faculty fellowship from the Copenhagen Business School (CBS), and more recent funding from the Endowed Chair in Digitali zation at CBS.

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.1026.

Keywords: software outsourcing software reliability monitoring renegotiation incentives incomplete contrac

## 1. Introduction

Software outsourcing has grown tremendously over the last two decades (Liang et al. 2016b). The analysts at ReportLinker (2020) forecasted the global information technology (IT) outsourcing market to have a compound annual growth rate (CAGR) of 5% from 2020 to 2024. According to the report from KPMG (2018), in 2017, 727 IT outsourcing contracts worth US\$137.2 billion were signed worldwide, and <sup>fi</sup>xedprice and time-and-materials contracts contributed to more than 49% and 2% of total IT business process outsourcing (BPO) deal value, respectively.<sup>1</sup> With so much money at stake, software outsourcing needs to be cost-effective for an organization to compete well in its markets.

The software outsourcing process has various general activities, including contracting, development, renegotiation, testing, and maintenance. Practitioners recognize that outsourcing involves various information asymmetries and uncertainties that introduce challenges in its management. They include, for example, how to estimate a vendor’s effort in system development (Dey et al. 2010); the volatility of software code as business needs change (Krishnan et al. 2004); and the ongoing transformation of the IT landscape that affects systems (Moreno 2017). Monitoring and contract renegotiation are two common instruments that organizations use to address information asymmetry and uncertainty in software outsourcing. Monitoring is applied in time-and-materials contracts to inspect and reimburse a vendor for its efforts. Renegotiation occurs when two parties revise their initial contract, and it can be deployed in both <sup>fi</sup>xed-price and time-and-materials contracts to mitigate the loss of valuable surplus when uncertainty arises after development. See Appendix A for a glossary of terms in this article.

Given their prevalence in industry, we focus on these two types of contracts: <sup>fi</sup>xed-price and time-andmaterials contracts (Gopal and Sivaramakrishnan 2008, Dey et al. 2010, Korotia 2017).<sup>2</sup> A fixed-price contract consists of a predetermined payment for system development, testing, and maintenance services from the vendor. By contrast, a time-and-materials contract includes an extra fee or reimbursement beyond the payment for services obtained based on the vendor’s effort.<sup>3</sup> Considering the noncontractibility of effort in a time-and-materials contract, the client needs to monitor the vendor’s effort to determine the appropriate compensation for what it has done.<sup>4</sup>

After two parties engage in an outsourcing process with a <sup>fi</sup>xed-price or a time-and-materials contract, they often renegotiate the initial contract terms once the system has been developed because of the realization of uncertainties.<sup>5</sup> According to Gartner, approximately 75% of all existing outsourcing relationships are renegotiated during their lifetime (James 2017). For example, the Kansas Department of Health and Environment signed a <sup>fi</sup>xed-price contract with Accenture, and after the system was developed, they extended the contract for <sup>fi</sup>ve years to test and debug the system (Marso 2016). Also, the British Columbia, Canada Ministry of Health signed a time-and-materials contract with IBM and revised the contractual terms around time-to-completion and defect remediation. It required IBM to resolve system bugs during testing, resulting in cost overruns (Auditor General of British Columbia 2015). Renegotiation of testing time addresses the uncertain ties in system development and affects the vendor’s ef fort backwardly, because testing time is determined by the quality of the effort expected to be made. Furthermore, testing time is a decision in software outsourcing to balance the tradeoffs between testing and maintenance costs and between the value of the system and bug-led disutility. If testing time is short, critical bugs may remain undiscovered, resulting in high maintenance costs and high disutility from bugs during system use. However, prolonged testing typically leads to high testing costs and system release delays which reduce the value of the system.

Mathur (2016) suggests that a <sup>fi</sup>xed-price contract with renegotiation is appropriate, and the client will most often use renegotiation only. However, the Scottish Police Authority decided to terminate its <sup>fi</sup>xed-price contract with Accenture within a year after renegotiating testing time (Evenstad 2016). Therefore, renegotiation is not effective for all clients, and nobody likes to renegotiate with a vendor (Shared Services and Outsourcing Network 2012). Thus, time-and-materials contracts are popular: they reduce the likelihood of renegotiation (Knoll 2016), implying that monitoring substitutes for renegotiation. Yet, after signing a time-and-materials contract, the British Columbia, Canada Ministry of Health nevertheless renegotiated with IBM on its initiative and the cost overruns that developed. A summary of examples with different contract forms motivating is provided in Table 1.

Software outsourcing thus creates challenges for the client. Should it monitor the vendor’s effort in development, renegotiate testing time after that, or both? Which contract type should it sign when initiating the outsourcing process? To address these questions, we build a multistage model in which a client outsources a customized system from an IT services vendor. It enables us to investigate the interaction between the use of monitoring and renegotiation and to evaluate contract choice. Our analysis shows that renegotiation generates direct and indirect uncertainty-resolution effects, making testing time ef<sup>fi</sup>cient and increasing social welfare. The direct uncertainty-resolution effect comes from the same effort as the case without renegotiation, and the indirect uncertainty-resolution effect stems from the additional effort compared with the nonrenegotiation case. With the indirect uncertainty-resolution effect, when the client’s required system complexity for the customized system is moderate, renegotiation can incentivize the vendor to exert more effort in system development. This can be regarded as the post-development incentive of renegotiation, and it increases with the vendor’s bargaining power in renegotiation.<sup>6</sup> Monitoring stimulates the vendor’s effort, which can be regarded as a pre-development incentive because monitoring is determined when the parties sign a time-and-materials contract.

Table 1. Examples of Software Outsourcing Contracts

<table><tr><td>Client</td><td>Vendor</td><td>Contract form</td><td>Renegotiation</td><td>Citation</td></tr><tr><td>Kansas Department of Health and Environment</td><td>Accenture</td><td>Fixed-price contract</td><td>Testing time</td><td>Marso (2016)</td></tr><tr><td>Scottish Police Authority</td><td>Accenture</td><td>Fixed-price contract</td><td>Testing time</td><td>Evenstad (2016)</td></tr><tr><td>British Columbia, Canada Ministry of Health</td><td>IBM</td><td>Time-and-materials contract</td><td>Testing time</td><td>Auditor General of British Columbia (2015)</td></tr></table>

When the costs of monitoring and renegotiation are low, a vendor with low bargaining power is not affected by the post-development incentive because of the low revenue share generated by renegotiation. The client adopts monitoring at the same time for the predevelopment incentive to create the indirect uncertainty-resolution effect of renegotiation. Thus, monitoring and renegotiation are complements in this scenario, and the client selects a time-and-materials contract with renegotiation.<sup>7</sup> This is different from prior studies (Gopal and Koka 2010, Benaroch et al. 2016), which show that monitoring reduces the possibility of opportunistic renegotiation. If the vendor has high bargaining power, the post-development incentive is suf<sup>fi</sup>ciently strong to increase the vendor’s effort, and renegotiation substitutes for monitoring. Thus, the client selects a <sup>fi</sup>xed-price contract with renegotiation. In the earlier example, Accenture’s bargaining power was large because the Kansas Department of Health and Environment was locked into a partnership that promised Accenture US\$200 million in revenue. Therefore, the Kansas Department of Health and Environment chose to sign a <sup>fi</sup>xed-price contract with Accenture based on the breadth of the mutual commitments.

When monitoring has a high cost and renegotiation is inexpensive, even if the vendor has low bargaining power, renegotiation can substitute for monitoring. This is because the indirect uncertainty-resolution effect does not cause the pre-development incentive to cover the cost of monitoring, and the client adopts renegotiation only for the direct uncertainty-resolution effect. Another example is related to the bargaining power of Fujitsu, which was lower than that of Whitbread PLC because the latter had other potential vendors it could choose (Had<sup>fi</sup>eld 2005). Yet, Whitbread PLC chose Fujitsu to provide IT services and extended its contract duration because Fujitsu agreed to <sup>fi</sup>xed annual pricing, allowing Whitbread PLC to be sure that its outsourcing budget would be suf<sup>fi</sup>cient, with no need for extra monitoring cost (Fujitsu 2004, 2009).

When renegotiation is expensive, renegotiation is not adopted by the client. For example, if the State of Michigan and Hewlett-Packard (HP) extended their contract duration, then half of the State of Michigan’s IT projects more than US\$15 million would have run 45% over budget (Bort 2015). The State of Michigan refused to renegotiate with HP and instead reached a US\$13 million settlement (Gerstein 2017). Meanwhile, if the bene<sup>fi</sup>t from the pre-development incentive of monitoring dominates its cost, the client adopts monitoring as a substitute for renegotiation to incent vendor effort. If monitoring cost is higher than its bene<sup>fi</sup>t, the client uses neither monitoring nor renegotiation and instead selects a <sup>fi</sup>xed-price contract without renegotiation.

We further explore how the vendor’s development effort and the client’s pro<sup>fi</sup>t change with some key aspects of software outsourcing. For example, a vendor is more likely to exert lower effort when system complexi ty is greater or the bug rate is higher and more likely to exert higher effort when system lifetime is longer. The client’s pro<sup>fi</sup>t decreases in system complexity and bug rate but increases in system lifetime. We extend the base model so the discrete levels of development effort become continuous and examine how our results change when renegotiation cost endogenously depends on the renegotiation process. We also show that the base model’s <sup>fi</sup>ndings hold qualitatively.

The rest of the paper is organized as follows. We <sup>fi</sup>rst discuss relevant literature and then lay out the details of an optimization model to analyze the most often-used <sup>fi</sup>xed-price and time-and-materials contracts. Then, our analysis probes contract choices, based on the interaction between monitoring and renegotiation, which also discusses how we are able to arrive at theoretically meaningful and managerially valid contract strategies. We further analyze the impacts of some other aspects of software outsourcing and extend the base model to two other situations to show the robustness of our <sup>fi</sup>ndings. We conclude with theoretical and managerial contributions, strate gy conjectures built on our theory perspective, and limitations.

## 2. Literature and Theory 2.1. Software and IT Outsourcing Contracts

This research is mainly related to the literature stream on software and IT outsourcing contracts. A summary of our <sup>fi</sup>ndings related to the papers in this stream is provided in Table 2. A large body of research in this stream focuses on contract choice. Fixed-price and time-and-materials contracts are commonly used contract forms in practice (Gopal and Koka 2010, Mani et al. 2012), although the former is most common by a wide margin (KPMG 2018). Compared with a <sup>fi</sup>xedprice contract, a time-and-materials contract entails higher monitoring costs (Bajari and Tadelis 2001, Roels et al. 2010). As system complexity under development increases, however, the client prefers a timeand-materials contract (Gefen et al. 2008) because monitoring transforms private information about vendor effort into public information (Liang et al. 2016a).

Table 2. Relevant Literature on Software and IT Outsourcing Contracts

<table><tr><td>Research angles</td><td>Theme</td><td>Paper</td><td>Monitoring</td><td>Renegotiation</td><td>Major findings</td></tr><tr><td rowspan="6">Contract choice</td><td>Fixed-price (FP) vs. time-and-materials (TM)</td><td>Gopal and Sivaramakrishnan (2008)</td><td>√</td><td>×</td><td rowspan="2">Vendor prefers a fixed-price contract for larger, longer projects with larger teams, to secure larger information rent.Vendor prefers a time-and-materials contract when the risk of employee attrition from the project team is high.Fixed-price contract is suitable for simple projects.Time-and-materials contract is suitable for complex projects with low monitoring costs.</td></tr><tr><td>FP vs. TM vs. performance-based vs. profit-sharing</td><td>Dey et al. (2010)</td><td>√</td><td>×</td></tr><tr><td>FP vs. TM</td><td>Gopal and Koka (2010)</td><td>√</td><td>×</td><td>In time-and-materials contracts, clients increase monitoring because it results in improved services.Fixed-price contracts enable vendors to leverage their capability and derive higher returns from software quality.</td></tr><tr><td>FP vs. TM vs. performance-based</td><td>Roels et al. (2010)</td><td>√</td><td>×</td><td>Fixed-price contracts contingent on performance are preferred when service output is sensitive to vendor effort.Time-and-materials contracts are optimal when output is sensitive to client effort.</td></tr><tr><td>TM vs. profit-sharing</td><td>Bhattacharya et al. (2014)</td><td>√</td><td>√</td><td>Compared with time-and-materials contracts, profit-sharing contracts can induce optimal effort from clients / vendors when cost of monitoring the verifiable outcome is low.Option-based contracts are robust to renegotiation which leads to hold-up problems.</td></tr><tr><td>Single- vs. multi-sourcing</td><td>Bhattacharya et al. (2018)</td><td>×</td><td>×</td><td>When tasks are modular, multi- dominates single-sourcing.When tasks are integrated, sourcing choice depends on tradeoffs among alignment between performance / project revenue, verifiability of project revenue, and moral hazard.</td></tr><tr><td rowspan="6">Incomplete contract</td><td>Transaction cost</td><td>Richmond et al. (1992)</td><td>×</td><td>√</td><td>Outsourcing provides incentives for vendors to sustain specific investments and promote future cost reduction.</td></tr><tr><td>Low balling</td><td>Whang (1995)</td><td>×</td><td>×</td><td>Even if clients and vendors share renegotiation surplus, outsourcing can lead to a higher value for clients compared with a salaried internal development team.Vendors sell customized software below their marginal cost because of the learning effect and software code reusability.For clients, directly picking a vendor and signing a contract with property rights sharing can improve the alignment of vendor incentives, compared with bidding auction.</td></tr><tr><td>Renegotiation</td><td>Benaroch et al. (2010)</td><td>×</td><td>√</td><td>Increased demand uncertainty ups clients&#x27; will to backsource.Vendor can modulate client&#x27;s tendency to outsource and increase likelihood of greater profitability, by varying usage-based subscription fee per IT service unit outsourced.</td></tr><tr><td>Transaction cost</td><td>Benaroch et al. (2016)</td><td>√</td><td>√</td><td>Contract type/extensiveness are mechanisms for saving transaction costs arising under different circumstances.</td></tr><tr><td>Asset transfer</td><td>Chang et al. (2017)</td><td>√</td><td>√</td><td>Preference for time-and-materials contracts counteracts effect of certain transaction attributes on contract extensiveness and cancels it with transaction uncertainty.Asset transfers affect contract design, as with inclusion of clauses that protect clients and vendors.Outsourcing objectives are more likely to be met when contracts have compensation mechanisms to support asset transfer.</td></tr><tr><td>Ethics</td><td>Anand and Goyal (2019)</td><td>×</td><td>√</td><td>Renegotiation is a myopic strategy to nonethical clients.Ethical clients can use IP sharing to insulate against worst effect of incomplete contracts and incomplete information.</td></tr><tr><td>Contract choice and incomplete contract</td><td>Fixed-price vs. Time-and-materials and renegotiation</td><td>Our work</td><td>√</td><td>√</td><td>Monitoring and renegotiation are substitute or complement, with renegotiation / monitoring cost, and bargaining power.Four contract strategies are available for clients, determined by the interaction of monitoring and renegotiation.</td></tr></table>

Gopal and Sivaramakrishnan (2008) examined data on 93 offshore projects and analyzed the different preferences between <sup>fi</sup>xed-price and time-andmaterials contracts from the vendor’s perspective. Dey et al. (2010) presented a contract-theoretic model that incorporates the quality of a developed system, the timeliness of delivery and the postdelivery software to compare the client’s pro<sup>fi</sup>t for different contract forms. Gopal and Koka (2010) studied data collected from 100 software projects and investigated how different incentive structures inherent in <sup>fi</sup>xed-price and time-andmaterials contracts in<sup>fl</sup>uence the quality provided by the vendor in software development outsourcing. Roels et al. (2010) studied IT outsourcing services and analyzed how contract form choice is driven by veri<sup>fi</sup>ability of the client’s and the vender’s effort levels. Bhattacharya et al. (2018) considered collaborative services and veri<sup>fi</sup>ability of the parties’ effort but focused more on how task modularity in<sup>fl</sup>uences effectiveness of singleversus multi-sourcing.

Our research departs from the above literature about contract choice. We study incomplete software outsourcing contracts because they involve unforeseen contingencies (Che and Hausch 1999), noncontractible investments and behavior (Susarla 2012), and unmeasurable performance (Fitoussi and Gurbaxani 2012). Bhattacharya et al. (2014) studied contract incompleteness and compared client and vendor pro<sup>fi</sup>ts for time-and-materials and pro<sup>fi</sup>tsharing contracts. They focused on negative effects of renegotiation on outsourcing and proposed an option-based contract robust to renegotiation. We focus on the positive effects of renegotiation and show it may incentivize development effort.

Contract incompleteness and renegotiation are also investigated for software and IT outsourcing contracts. Contract renegotiation has been studied in economics, and the classical conclusion is that the hold-up problem occurs when the parties can take unilateral actions after signing a contract. The investing party fears expropriation of investment bene<sup>fi</sup>ts by its contract partner in renegotiation (Che and Hausch 1999), leading to underinvestment (Maskin and Moore 1999). In contrast, we show that testing time renegotiation may offer the vendor additional incentive to invest in making more service-related effort.

For software and IT outsourcing contracts, previous literature investigated incomplete contracts from different perspectives, such as transaction cost, lowballing, renegotiation, asset transfer, and ethics. Richmond et al. (1992) considered the contract incompleteness and examined the impact of outsourcing on the IT developer’s effort and the transaction cost of outsourcing by comparing it with using an internal development team. Whang (1995) studied whether the bene<sup>fi</sup>ts of declining development costs are passed on to the client in the form of lower prices when vendors bid strategically: called low-balling. He suggested that directly signing a property rights-sharing contract with a vendor may dominate bidding in an auction. Benaroch et al. (2010) modeled the implications of a backsourcing renegotiation contract option. They distilled cost and value effects for the client and the vendor and computed the fair compensation and value for them by pricing the option at contract initiation. Benaroch et al. (2016) later focused on the ex ante and ex post transaction costs balance for incomplete contracts and examined contract design choices in terms of transaction and relational attributes. Chang et al. (2017) studied how asset transfer, based on property rights theory, affects the client’s contract design and the vendor’s investment incentive, and provided a guide to clients on IT outsourcing. Finally, Anand and Goyal (2019) built a dynamic model that integrated incomplete contracts and analyzed how ethics, reputation effects, and intellectual property (IP) sharing drive IT outsourcing.

We investigate the interplay between monitoring and renegotiation rather than just incomplete contracts in general in the present research: a clear difference. Most studies related to transaction cost and agency theory have emphasized the effect of monitoring to prevent vendor opportunism (Gopal and Koka 2010, Benaroch et al. 2016). Instead, we show that monitoring and opportunistic renegotiation (Aron et al. 2005) can complement each other under certain conditions to incentivize vendor effort in different ways.

## 2.2. Software Reliability and Bug Identification

Another stream is software reliability: how a system will perform without bugs over a period. The most commonly used reliability prediction model is the Goel-Okumoto nonhomogeneous Poisson process model (G-O model) (Goel and Okumoto 1979).<sup>8</sup> Using this, Pham and Zhang (1999) analyzed reliability cost for optimal testing time. Jiang et al. (2012) separated testing stop time from system release time, and considered testing that continues during system operation, as with post-release testing. August and Niculescu (2013) examined the software demand impact on postrelease testing. Also, Jiang et al. (2017) considered reliability and market bene<sup>fi</sup>ts and derived the optimal testing time and number of testers.

An unstated assumption in these studies is that the sys tem will be developed completely. This is not always true, however, as the business press and some of our examples suggest (Mezak 2018). Others ignored that the vendor must exert essential effort for system development. For example, it must ensure due diligence for the technology choices to be made and avoid the usual pitfalls of coding errors. Thus, we consider the development and testing stages. After the vendor develops the system, the parties may wish to renegotiate how much testing time should be in the contract before committing to it.

## 3. Modeling Software Outsourcing Contract Decisions

We now construct a decision model with testing time renegotiation. We present two base cases with the sum of the expected payoffs of the parties maximized under renegotiation and nonrenegotiation: the firstbest solution.<sup>9</sup> Comparing the cases, we obtain the impact of testing time renegotiation on outsourcing.

## 3.1. Model Description

We consider a client (Client hereafter) contracts for IT services from a vendor (Vendor hereafter) for three stages: development, testing, and maintenance. Table 3 presents our modeling notation.

In the system development stage, the Vendor develops a customized system for the Client based on its system complexity needs. We use $r$ to denote system complexity, for example, the size of the system’s codebase or the number of modules and functions (August and Niculescu 2013). The Vendor makes development effort, including identi<sup>fi</sup>cation of the Client’s desired system complexity and planning, designing, and programming the code for the system, to improve system reliability. As in Yamada (2014), we use the expected number of software bugs to indicate the system reliability level. The more effort the Vendor makes, the fewer the number of bugs and the higher the system reliability becomes. We assume two levels of effort $e ,$ high $( e _ { H } )$ and low $( e _ { L } )$ , for the Vendor to choose from. The decision is the Vendor’s private information, and the cost of effort e is $e / c ,$ , where c represents the Vendor’s capability in the development stage.

Assumption 1 (Expected Number of Bugs). Given system complexity $\boldsymbol { { \cal Y } } ,$ the Vendor’s development capability $c ,$ and effort $e ,$ at the end of development, the expected bugs for the system are $N _ { C S } ( e )$ , where<sup>10</sup>:

$$
\underbrace{N_{CS}(e)}_{\substack{\text{expected number of bugs}\\ \text{for customized system}}} = \underbrace{\mathcal{Y}B(c)}_{\substack{\text{initial expected}\\ \text{number of bugs}}} - \underbrace{e^{\beta}}_{\substack{\text{effort}\\ \text{performance}}} + \underbrace{\varepsilon}_{\substack{\text{uncertainty}}}  .\tag{1}
$$

In Equation (1), $\boldsymbol { { \ r } } _ { B ( c ) }$ denotes the initial expected number of bugs, increasing in system complexity $\boldsymbol { r }$ and bug rate $B ( c )$ , where B c represents the average number of bugs per thousand lines of code (August and Niculescu 2013) and decreases in the Vendor’s de velopment capability $c ~ ( \partial B ( c ) / \partial c < 0 )$ . Here, $e ^ { \beta }$ re<sup>fl</sup>ects the performance of Vendor’s effort on the reliability of the system. Following the single-factor Cobb-Douglas function, $\beta$ is the effectiveness of Vendor effort for decreasing the expected number of bugs (Hu et al. 1998). We further assume that $\beta \in ( 0 , 1 )$ because it is increasingly dif<sup>fi</sup>cult to reduce the expected number of bugs (Dey et al. 2010, Parker and Van Alstyne 2018). The uncertainty ε of the outcome of the Vendor’s development effort is uniformly distributed in $[ - \sigma , \sigma ]$ , where σ and σ are minimum and maximum values of ε. The uncertainty is realized when the Vendor <sup>fi</sup>nishes develop ment, and the parties observe the updated expected number of bugs, $N _ { C S } ( e )$ , in the system.

Assumption 2 (Existence of Bugs). Given development effort e and the realization of uncertainty ε, there are still some bugs in the system: ${ \mathcal { T } } { \bar { B ( c ) } } - e _ { H } ^ { \beta } - \sigma > 0$

Assumption 2 implies that the minimum expected number of bugs for the system, based on the initial expectation ${ \mathit { r B } } ( c ) .$ , is positive for the Vendor at any capability, even with high effort $e _ { H }$ and the most favorable realization of uncertainty ε. Thus, bugs still can be detected in testing and maintenance stages. Also, given system complexity $\boldsymbol { \Upsilon } ,$ development time is constant and <sup>fi</sup>xed (Ghoshal et al. 2017, Li et al. 2017). To focus on testing time renegotiation impacts, we normalize development time to zero.

After the Vendor has <sup>fi</sup>nished development, uncertainty ε for expected bugs $N _ { C S } ( e )$ is realized, and the system testing stage begins. We denote the time from the beginning of testing to the end of maintenance as the lifetime of the system T (Ji et al. 2011, August and Niculescu 2013). The Vendor spends time $: ( t < T ) ^ { 1 1 }$ to detect bugs with a cost of $K ( c ) \bar { t } .$ , where K c is testing cost per unit time which decreases in the Vendor’s development capability $( \partial K ( c ) / \partial c < 0 )$ . Testing is a nonhomogeneous Poisson process (Roy et al. 2015), and we assume it has two properties (Jiang et al. 2012):

Assumption 3 (Memoryless Property of Bug Detection). The detection of each bug in a system is independent of the detection of others, and the total bug-detection rate at any time is proportional to the number of undetected bugs at that time.

Assumption 3 implies the probability a bug will be detected by time t is $F ( t ) \stackrel { - } { = } 1 - \exp ( - \lambda t )$ , where $\lambda$ is the bug failure rate. This memoryless property is common in software reliability growth models that use math to characterize software bugs. See Appen dix B for additional details on how software models handle bugs. We assume perfect debugging for this analysis.

Table 3. Modeling Notation and Technical De<sup>fi</sup>nitions

<table><tr><td>Notation</td><td>Definition</td><td>Comments</td></tr><tr><td>S</td><td>Social surplus</td><td>S represents the social surplus.</td></tr><tr><td>C</td><td>Client</td><td>C represents the Client as a subscript (but cost when it is not a subscript).</td></tr><tr><td>V</td><td>Vendor</td><td>V represents the Vendor.</td></tr><tr><td>CS</td><td>Customized system</td><td>CS is a customized system; the Client outsources it from a Vendor.</td></tr><tr><td> $N_{CS}(e)$ </td><td>Expected bugs in system</td><td>Reliability of system after development; common knowledge to the parties.</td></tr><tr><td> $e\in\{e_L,e_H\}$ </td><td>Vendor&#x27;s development effort (low = L, high = H), 0 &lt;  $e_L < e_H$ </td><td>Development effort tied to reliability of system&#x27;s expected number of bugs.</td></tr><tr><td> $\hat{e}\in\{e_L,e_H\}$ </td><td>Vendor&#x27;s reported effort (low=L, high=H), 0 &lt;  $e_L < e_H$ </td><td>Vendor&#x27;s reported effort determines the payment made by Client in a time-and-materials contract.</td></tr><tr><td> $\varepsilon\sim U[-\sigma,\sigma]$ </td><td>Uncertainty about outcome of Vendor&#x27;s development effort</td><td>Uniformly distributed on  $[- \sigma, \sigma]; - \sigma, \sigma$  are min, max  $\varepsilon$  values ( $\sigma >0$ ).</td></tr><tr><td>T</td><td>System&#x27;s lifetime</td><td>Time duration when system developed until withdrawal of maintenance, including testing and maintenance time.</td></tr><tr><td> $t\in[0,T)$ </td><td>Initial testing time</td><td>Before system developed, Vendor negotiates initial testing time with Client.</td></tr><tr><td> $\tilde{t}\in[0,T)$ </td><td>Renegotiated testing time</td><td>After system developed, uncertainty of Vendor&#x27;s development effort is resolved, so both can renegotiate initial testing time to a new testing time.</td></tr><tr><td> $\tau$ </td><td>Time during maintenance</td><td>It can be any time which satisfies  $\tau\in[t,T]$ .</td></tr><tr><td> $\lambda\in(0,1)$ </td><td>Bug failure rate during testing</td><td>Reflects the Vendor&#x27;s testing effectiveness.</td></tr><tr><td> $\tilde{N}_{CS}(e,t)$ </td><td>Expected number of bugs in system after testing time t</td><td>Bugs of customized system decrease when testing time is increased.</td></tr><tr><td> $\tilde{N}_{CS}(e,T)$ </td><td>Expected number of bugs in system after system lifetime T</td><td>Bugs of customized system decrease when system lifetime is increased.</td></tr><tr><td>c&gt;0</td><td>Vendor development capability</td><td>When exerting the same effort, a Vendor with higher capability consumes less cost in system development.</td></tr><tr><td>a&gt;0</td><td>Cost of fixing one bug in testing</td><td>Average cost of fixing one bug when bug fix costs are low.</td></tr><tr><td>b&gt;0</td><td>Added cost of fixing one bug in maintenance after testing</td><td>Average cost of fixing one bug in later stage, when bug fix costs are high, and financial impacts on Client&#x27;s business operations may occur.</td></tr><tr><td>K(c)&gt;0</td><td>Cost of testing per unit time</td><td>Decreases with Vendor&#x27;s development capability ( $\partial K(c)/\partial c<0$ ).</td></tr><tr><td>TC</td><td>Vendor&#x27;s total cost</td><td>Vendor&#x27;s total costs include development cost, testing cost, and bug-fix costs during testing and maintenance.</td></tr><tr><td> $C_R\geq 0$ </td><td>Client&#x27;s cost of renegotiation</td><td>Client and Vendor share the renegotiation cost, but this yields similar results as when Client bears whole renegotiation cost. (Here, C is not a subscript.)</td></tr><tr><td>RS</td><td>Renegotiation surplus</td><td>Without renegotiation cost, value from renegotiation after development.</td></tr><tr><td>RB</td><td>Renegotiation benefit</td><td>Without renegotiation cost, the expected difference of social surplus between the renegotiation and nonrenegotiation cases.</td></tr><tr><td>U</td><td>Client&#x27;s total utility</td><td>Increases with system complexity and system use and decreases with the expected number of software bugs during maintenance.</td></tr><tr><td> $\gamma>0$ </td><td>System complexity</td><td>Includes size of system&#x27;s codebase, number of modules and functions and so on. Max value of system per unit time when zero bugs are guaranteed.</td></tr><tr><td>B(c)&gt;0</td><td>Bug rate</td><td>Decreases with Vendor&#x27;s development capability ( $\partial B(c)/\partial c<0$ ).</td></tr><tr><td> $\delta>0$ </td><td>Client&#x27;s sensitivity to bugs in customized system</td><td>If Client is more sensitive to bugs, the same expected number of bugs in a customized system will lead to higher disutility in use.</td></tr><tr><td> $\alpha\in[0,1]$ </td><td>Vendor&#x27;s bargaining power in renegotiation</td><td>Portion of incremental surplus the Vendor attains in renegotiation.</td></tr><tr><td> $\beta\in(0,1)$ </td><td>Effectiveness of Vendor effort</td><td>Restriction 0 &lt;  $\beta$  &lt; 1 signifies a decreasing return of Vendor&#x27;s effort and it becomes increasingly difficult to reduce the expected number of bugs.</td></tr><tr><td>P≥0</td><td>Initial payment for Vendor&#x27;s services</td><td>Set at beginning of software outsourcing for Vendor&#x27;s development, testing and maintenance services.</td></tr><tr><td> $\tilde{P}\geq 0$ </td><td>Ex post payment for Vendor&#x27;s service</td><td>Generated after renegotiation, including initial payment P and Vendor&#x27;s profit from renegotiation.</td></tr><tr><td>r≥0</td><td>Reimbursement for unit effort in time-and-materials contract</td><td>Reimbursement for Vendor effort per unit in time-and-materials contract.</td></tr><tr><td> $\phi\in[0,1]$ </td><td>Monitoring policy of Client</td><td>Probability that Client finds if Vendor reports its true effort by monitoring documents and development activities.</td></tr><tr><td>w≥0</td><td>Cost of monitoring</td><td>Per unit cost of monitoring Vendor&#x27;s development documents and process.</td></tr><tr><td>s&gt;0</td><td>Penalty for misreported effort</td><td>Cost of reputation loss and subsequent future business loss of the Vendor.</td></tr></table>

Assumption 4 (Perfect Debugging). A detected bug can be fixed without causing more errors.

Debugging is imperfect in practice though, the cumulative number of bugs detected at any time is expected to be the same with models that have perfect or imperfect debugging (Ohba and Chou 1989). Assumptions 3 and 4 are from the G-O model, which is widely adopted in software engineering (Yamada 2014, Roy et al. 2015) and information systems (IS) (Jiang et al. 2012, August and Niculescu $2 0 1 3 ) . ^ { 1 2 } { \mathrm { ~ A c - } }$ cording to the G-O model, the expected number of bugs remaining, $\tilde { N } _ { C S } ( e , t )$ , after testing time t will be

$$
\begin{array}{c} \underbrace {\tilde {N} _ {C S} (e , t)} _ {\text { expected   number   of   bugs   remaining   in   customized   system   after   testing   time } t} = \underbrace {N _ {C S} (e)} _ {\text { total   expected   number   of   bugs   in   customized   system }} \\ \times \exp (- \underbrace {\lambda} _ {\text { failure   rate   of   each   bug }} \underbrace {t} _ {\text { testing   time }}). \end{array} \tag {2}\tag{2}
$$

In testing, the cost of <sup>fi</sup>xing bugs is approximated by $a \cdot ( N _ { c s } ( e ) \dot { - } \tilde { N } _ { C S } ( e , t ) )$ for the Vendor, where a is the cost of <sup>fi</sup>xing each bug and $( N _ { C S } ( e ) - \tilde { N } _ { C S } ( e , t ) )$ is the expected number of bugs detected. When the Vendor <sup>fi</sup>nishes testing, the system will be given to the Client and put into operation. The Vendor maintains it after for the time <sub>(</sub>T <sub>−</sub> t<sub>)</sub>. In the system maintenance stage, maintenance cost is incurred by the Vendor when failures occur during operation. They include the direct cost of identifying and <sup>fi</sup>xing bugs, the downtime loss of revenue, and other costs. The cost for a bug-<sup>fi</sup>x during maintenance is higher than during testing, if the bug was detected during testing.<sup>13</sup> Based on this, total maintenance cost is $( a + \breve { b } ) \cdot ( \tilde { N } _ { C S } ( e , t ) - \tilde { N } _ { C S } ( e , T ) )$ for the Vendor, where b is the incremental cost for each bug in the maintenance stage compared with the testing stage, and $( \tilde { N } _ { C S } ( e , t ) - \tilde { N } _ { C S } ( e , \bar { T } ) )$ is the expected number of bugs .

Based on these assumptions, the expected total cost TC e, t for the Vendor includes four parts:

$$
\begin{array}{l} \underbrace {T C (e , t)} _ {\text { total   cost   of   the   Vendor }} = \underbrace {e / c} _ {\text { development   cost }} + \underbrace {K (c) t} _ {\text { testing   cost }} + \underbrace {a \cdot \left(N _ {C S} (e) - \tilde {N} _ {C S} (e , t)\right)} _ {\text { bug   -   fix   cost   during   testing }} \\ + \underbrace {(a + b) \cdot (\tilde {N} _ {C S} (e , t) - \tilde {N} _ {C S} (e , T))} _ {\text { bug   -   fix   cost   during   maintenance }}. \end{array} \tag {3}\tag{3}
$$

They are added without discounting, although they are incurred at different times. The parameters $( a , b , c ,$ and K c ) are assumed to be accounted in the usual discounting. Rewriting Equation (3) via Equation (2), where $\tilde { N } _ { C S } ( e , t ) = N _ { C S } ( \Breve { e } ) \cdot \grave { \exp } ( - \lambda t )$ with λ indicating bug detection intensity per unit time, yields

$$
\begin{array}{c} T C (e, t) = e / c + K (c) t + a N _ {C S} (e) \cdot (1 - \exp (- \lambda t)) \\ + (a + b) N _ {C S} (e) \cdot (\exp (- \lambda t) - \exp (- \lambda T)). \end{array}\tag{4}
$$

Equation (4) can be rewritten as

$$
\begin{array}{c} \underbrace {T C (e , t)} _ {\text {total cost of the Vendor}} = \underbrace {e / c} _ {\text {development cost}} + \underbrace {K (c) t} _ {\text {testing cost}} \\ + \underbrace {a N _ {C S} (e) \cdot (1 - \exp (- \lambda T))} _ {\text {(I) bug -fix cost if all the bugs of system lifetime were detected during testing}} \\ + \underbrace {b N _ {C S} (e) \cdot (\exp (- \lambda t) - \exp (- \lambda T))} _ {\text {(II) additional bug -fix cost in maintenance if some bugs were not detected during testing}}. \end{array}\tag{5}
$$

In Term (I) of Equation (5), $N _ { C S } ( e ) \cdot ( 1 - \exp ( - \lambda T ) )$ represents the total expected number of bugs during system lifetime and thus Term (I) is the bug-<sup>fi</sup>x cost if all the likely bugs over a system’s lifetime were detected during testing. In Term (II), $\begin{array} { r } { N _ { C S } ( e ) \cdot ( { \exp ( - \lambda t ) } - } \end{array}$ exp<sub>(−</sub>λT<sub>))</sub> represents the expected number of bugs that were not detected during testing but occur during maintenance. Term (II) thus denotes the added cost for bug-<sup>fi</sup>x in maintenance compared with testing.

The Client uses the system during time period t, T , and at any time $\tau \in [ t , \ { \dot { T } } ]$ , the expected number of the remaining bugs is $\tilde { N } _ { C S } ( e , \tau ) = \tilde { N _ { C S } } ( e ) \cdot \exp ( - \lambda \tau )$ , which can cause problems for the Client (Jiang et al. 2012). We assume the bug disutility rate at time τ is $\delta \tilde { N } _ { C S } ( e , \tau )$ with δ the Client’s sensitivity to bugs. The Client’s disutility from the expected number of bugs during period t, T is

$$
\int_ {t} ^ {T} \delta \tilde {N} _ {C S} (e, \tau) \mathrm{d} \tau = \frac {\delta}{\lambda} N _ {C S} (e) \cdot (\exp (- \lambda t) - \exp (- \lambda T)).\tag{6}
$$

Assumption 5 (Client’s Utility). The Client’s utility from the customized system is

$$
\underbrace{U(e,t)}_{\substack{\text{utility of}\\ \text{the Client}}} = \underbrace{\mathcal{Y}\cdot(T - t)}_{\substack{\text{value of}\\ \text{the system}}} - \underbrace{\frac{\delta}{\lambda}N_{CS}(e)\cdot(\exp(-\lambda t) - \exp(-\lambda T))}_{\substack{\text{disutility to be incurred by the expected}\\ \text{number of bugs during maintenance}}}\tag{7}
$$

Assumption 5 shows that the Client’s utility $U ( e , t )$ increases with system complexity $\boldsymbol { r }$ and system use time T  t and decreases with the expected number of bugs during maintenance.

Assumption 6 (Positive Profit of Software Outsourcing). The outsourcing of customized system always generate positive profit for the Client: $\begin{array} { r } { \frac { \delta } { \lambda } < \frac { b \check { T } } { K ( c ) } , } \end{array}$

Assumption 6 ensures that the Client’s disutility incurred by each bug $\delta / \lambda$ is lower than the per use time system value $r$ multiplied by the Vendor’s testing bene<sup>fi</sup>t $b / K ( c )$ of each bug, which guarantees the existence of the outsourcing service.<sup>14</sup>

Assumption 7 (Marginal Benefit and Cost During Testing). For system testing, the marginal benefit is greater than the marginal cost: $( \delta + \lambda b ) N _ { C S } ( e ) > T + K ( c )$

Assumption 7 for software outsourcing implies that the marginal bene<sup>fi</sup>t of system testing $( \delta \bar { + } \lambda b \bar { ) } N _ { C S } ( e )$ is greater than its marginal cost $r + K ( { \stackrel { \sim } { c } } )$ 15

For outsourcing, our model permits a Client to use a <sup>fi</sup>xed-price or time-and-materials contract (Menon $2 0 1 8 ) . ^ { 1 6 }$ In the former, a predetermined price $P _ { F P }$ is paid to the Vendor for development, testing, and maintenance services, including contractible testing time. In the latter, beyond the predetermined price $P _ { T M }$ for services, the Client also pays for the Vendor’s development effort: $P _ { T M } + r \hat { e }$ . Here, $\hat { e } \in \{ e _ { L } , e _ { H } \}$ is the effort the Vendor reports to the Client, and r is the reimbursement for per effort. For any noncontractible effort the Vendor makes, the Client must monitor the Vendor to verify its reported effort $\hat { e } . ^ { 1 7 }$ The Client’s monitoring policy $\phi \in [ \bar { 0 } , 1 ]$ corresponds to the probability that the Client <sup>fi</sup>nds out if the Vendor reports its real effort. A higher value of $\phi$ indicates the Client monitors more development documents and processes. When $\phi = 1$ , the Client monitors the entire process and knows the Vendor’s true effort. When $\phi = 0 ,$ the Vendor is free to misreport. A Client incurs monitoring cost wφ with per unit cost w (Dey et al. 2010). If it <sup>fi</sup>nds the Vendor has in<sup>fl</sup>ated its effort, the latter will pay a penalty $( \hat { e } - e ) ^ { + } s ,$ where $( x ) ^ { + } = \operatorname* { m a x } \{ 0 , x \}$ . This is a reputation loss cost affecting future business.

At the beginning of an outsourcing relationship, the Vendor negotiates the project duration with the Client, including testing time. After development, the uncertainty ε of the outcome of the Vendor’s development effort is resolved, and the testing time determined by the Vendor before development may not be optimal. Thus, by updating the expected number of bugs for the system $\bar { N } _ { C S } ( e )$ after development, the Client and the Vendor are prompted to renegotiate initial testing time t to a more effective renegotiated testing time <sup>˜</sup>t to generate more value (social surplus). Regardless of renegotiation cost, we de<sup>fi</sup>ne the incremental surplus generated by renegotiation as renegotiation surplus RS<sub>(</sub><sup>˜</sup>t<sub>)</sub>. If renegotiation occurs, the Client and the Vendor split the renegotiation surplus with proportions $( 1 - \alpha )$ and $\alpha ,$ which represent their relative bargaining power (Che and Hausch 1999, Bolton and Dewatripont 2005, Guo and Iyer 2013), and the ex post prices for the Vendor’s services in the <sup>fi</sup>xed-price and time-and-materials contracts become $\tilde { P } _ { F P } = \bar { P } _ { F P } +$ $\alpha \cdot R S ( \tilde { t } )$ and $\tilde { P } _ { T M } = P _ { T M } + \alpha \cdot R S ( \tilde { t } )$ , respectively. Renegotiation incurs cost $C _ { R }$ that the Client bears.<sup>18</sup> Event timing for a fixed-price (FP) or time-and-materials (TM) contract is illustrated in Figure 1.

## 3.1.1. Vendor and Client Actions.

: Client selects contract type: if the FP contract is chosen, then Client determines $\{ \bar { P } _ { F P } \} ;$ and if the TM contract is chosen, then Client determines $\{ P _ { T M } , r , \phi \}$

: During system development, Vendor decides effort level e and initial testing time t in FP contract, or effort level e to develop system, reported effort level ${ \hat { e } } ,$ and initial testing time t in TM contract.

Development is <sup>fi</sup>nished and the expected number of bugs $N _ { C S } ( e )$ is updated because of the realization of the uncertainty of Vendor’s effort. Parties may renegotiate testing time t to a new one ${ \tilde { t } } ,$ and split the renegotiation surplus according to their bargaining power. If parties keep the initial testing time, then ${ \tilde { t } } = t .$ The prices for Vendor’s services in FP and TM contracts change correspondingly.

: Related to testing time t or <sup>˜</sup>t, Vendor detects <sup>Stage 3</sup>and <sup>fi</sup>xes system bugs. Then, the system is delivered to Client, and Vendor offers system maintenance service.

## 3.2. First-Best Solution Without Renegotiation Cost

We next solve for optimal development effort and testing time by distilling what is socially optimal for a Vendor to do. This involves summing the maximum expected payoffs of the two parties, the <sup>fi</sup>rst-best solution. To investigate the impact of testing time renegotiation, we ignore the renegotiation cost $( C _ { R } = 0 )$ and consider two cases. The <sup>fi</sup>rst is the <sup>fi</sup>rst-best solution with renegotiation (FBR), where the initial testing time is revised after development. The second is the <sup>fi</sup>rst-best solution without renegotiation (FBN), where the initial testing time remains unchanged.

Figure 1. Timing of Events  
![](/api/attachments/72VN8DNB/fulltext/images/2185398d837fb5d708fe522e3076a9e1428c5d3171e7c7683a58c47fd08e0b19.jpg)

In the FBR case, when there is no renegotiation cost, after system development the renegotiation surplus RS <sup>˜</sup>t is

$$
\underbrace{RS(\tilde{t})}_{\substack{\text{renegotiation}\\ \text{surplus}}} = \underbrace{(U(e,\tilde{t}) - TC(e,\tilde{t}))}_{\text{social surplus if testing time is}\tilde{t}} - \underbrace{(U(e,t) - TC(e,t))}_{\substack{\text{social surplus if testing time is} t}}.\tag{8}
$$

Based on Equations (5) and (7), Equation (8) can be rewritten as

$$
\begin{array}{l} \underbrace {R S (\tilde {t})} _ {\text { renegotiation   surplus }} = \left[ \underbrace {\mathcal {Y} t + \frac {\delta}{\lambda} \cdot (\mathcal {Y} B (c) - e ^ {\beta} + \varepsilon) \cdot \exp (- \lambda t)} _ {\text { Client   disutility   if   testing   time   is } t} \right. \\ \quad + \underbrace {K (c) t + b \cdot (\mathcal {Y} B (c) - e ^ {\beta} + \varepsilon) \cdot \exp (- \lambda t)} _ {\text { Vendor   testing   and   added   bug - fix   costs   if   testing   time   is } t} \\ \quad - \left[ \underbrace {\mathcal {Y} \tilde {t} + \frac {\delta}{\lambda} \cdot (\mathcal {Y} B (c) - e ^ {\beta} + \varepsilon) \cdot \exp (- \lambda \tilde {t})} _ {\text { Client   disutility   if   testing   time   is } \tilde {t}} \right. \\ \quad + \underbrace {K (c) \tilde {t} + b \cdot (\mathcal {Y} B (c) - e ^ {\beta} + \varepsilon) \cdot \exp (- \lambda \tilde {t})} _ {\text { Vendor   testing   and   added   bug - fix   costs   if   testing   time   is } \tilde {t}}. \end{array} \tag {(1)}\tag{9}
$$

Maximizing renegotiation surplus RS <sup>˜</sup>t in Equation (9) over <sup>˜</sup>t, we obtain the optimal renegotiated testing time:

$$
\underbrace{\tilde{t}^{*}}_{\substack{\text{optimal renegotiated}\\ \text{testing time}}} = \frac{1}{\lambda}\ln \frac{(\delta + \lambda b)\cdot(\mathcal{Y}B(c) - e^{\beta} + \varepsilon)}{\mathcal{Y} + K(c)}.\tag{10}
$$

Equation (10) suggests that optimal renegotiated testing time decreases with Vendor effort, $\partial \tilde { t } ^ { * } ( e ) / \partial e < 0$ The reason is that lower effort in the development stage is likely to generate a higher expected number of bugs $N _ { C S } ( \dot { e } )$ ex post, so more testing time is needed. By determining the optimal renegotiated testing time after system development, renegotiation resolves the uncertain outcome of the expected number of bugs. We refer to it as the uncertainty-resolution effect of renegotiation, UR e . It can be measured at stage 0 as

$$
\underbrace {U R (e)} _ {\text { uncertainty - resolution   effect }} = \underbrace {E _ {\varepsilon} \big [ R S (\tilde {t} ^ {*}) \big ]} _ {\text { expected   renegotiation   surplus }},\tag{11}
$$

where $E _ { \varepsilon } [ \cdot ]$ represents the expectation over random variable ε.

Lemma 1 (Positive Uncertainty-Resolution Effect). The uncertainty-resolution effect of renegotiation is positive, $U R ( e ) > 0 .$

Lemma 1 suggests that the uncertainty-resolution effect contributes to the increase of social surplus. Further, with the optimal renegotiated testing time $\tilde { t } ^ { * }$ , we can obtain social surplus in the initial contracting stage under each case, where superscripts FBR and FBN are <sup>fi</sup>rst-best solutions with and without renegotiation, respectively, and subscript S is social surplus:

$$
\pi_ {S} ^ {F B R} (e, t) = E _ {\varepsilon} \Bigg [ \underbrace {U (e , t)} _ {\text {utility of Client}} - \underbrace {T C (e , t)} _ {\text {total cost of Vendor}} + \underbrace {R S (\tilde {t} ^ {*})} _ {\text {renegotiation surplus}} \Bigg ];\tag{12}
$$

$$
\pi_ {S} ^ {F B N} (e, t) = E _ {\varepsilon} \Bigg [ \underbrace {U (e , t)} _ {\text { utility   of   Client }} - \underbrace {T C (e , t)} _ {\text { total   cost   of   Vendor }} \Bigg ].\tag{13}
$$

By solving the problems $\operatorname* { m a x } _ { e , t } \pi _ { S } ^ { F B R }$ and max $e , t  \pi _ { S } ^ { F B N }$ , we have the <sup>fi</sup>rst-best solution on effort and testing time with and without renegotiation. Table C.1 in Appendix C provides the details on the regions, optimal testing times and development effort levels, and the regions are de<sup>fi</sup>ned by two thresholds of system complexity. With the optimal decisions, there is an expected difference between the renegotiation and the nonrenegotiation social surplus levels, and the renegotiation benefit is given by

$$
\underbrace{RB^{FB}}_{\substack{\text{renegotiation benefit}\\ \text{in first - best solution}}} = \underbrace{\pi_{S}^{FBR}(e_{FBR}^{*},t_{FBR}^{*})}_{\substack{\text{expected social surplus}\\ \text{under FBR case}}} - \underbrace{\pi_{S}^{FBN}(e_{FBN}^{*},t_{FBN}^{*})}_{\substack{\text{expected social surplus}\\ \text{under FBN case}}},\tag{14}
$$

where $e _ { F B R } ^ { * } \ ( e _ { F B N } ^ { * } )$ and $t _ { F B R } ^ { * } ~ ( t _ { F B N } ^ { * } )$ are the optimal effort level and optimal initial testing time, respectively, under the FBR (FBN) case. Renegotiation bene<sup>fi</sup>t in Equation (14) can be rewritten in two parts:

$$
\begin{array}{l} \underbrace {R B ^ {F B}} _ {\text { renegotiation   benefit }} = \underbrace {\pi_ {S} ^ {F B R} (e _ {F B N} ^ {*} , t _ {F B N} ^ {*}) - \pi_ {S} ^ {F B N} (e _ {F B N} ^ {*} , t _ {F B N} ^ {*})} _ {\text {(I) direct uncertainty - resolution effect}} \\ + \underbrace {\pi_ {S} ^ {F B R} (e _ {F B R} ^ {*} , t _ {F B R} ^ {*}) - \pi_ {S} ^ {F B R} (e _ {F B N} ^ {*} , t _ {F B N} ^ {*})} _ {\text {(II) indirect uncertainty - resolution effect}}. \end{array} \tag {15}
$$

Term (I) of Equation (15) is positive, because $\pi _ { S } ^ { F B R } ( e _ { F B N } ^ { * } , ~ t _ { F B N } ^ { * } ) - \hat { \pi } _ { S } ^ { F B N } ( e _ { F B N } ^ { * } , t _ { F B N } ^ { * } ) = \hat { U } R ( e _ { F B N } ^ { * } )$ .We refer to Term (I) as the direct uncertainty-resolution effect of renegotiation under the FBR case, since the Vendor exerts the same effort as under the FBN case, $e _ { F B N } ^ { * } .$ Furthermore, it can be shown that the uncertainty resolution effect increases with the Vendor’s effort. This is because the Client shares the incremental surplus generated by the uncertainty-resolution effect with the Vendor, and renegotiation may incentivize the Vendor to put more effort in development to enhance the uncertainty-resolution effect. We <sup>fi</sup>nd that when the Client’s system complexity is moderate, the Vendor exerts high effort in the FBR case, $e _ { F B R } ^ { * } = e _ { H } ,$ but low effort in the FBN case, $e _ { F B N } ^ { * } = e _ { L }$ . This is the post-development incentive of renegotiation, because the Vendor decides the effort by anticipating that renegotiation will occur after development. Compared with the FBN case the extra effort in the FBR case incurs an additional cost, $\pi _ { S } ^ { F B N } ( e _ { L } ) - \pi _ { S } ^ { F B N } ( e _ { H } )$ , but also leads to an additional positive uncertainty-resolution effect, $U R ( e _ { H } ) - U R ( e _ { L } )$ . It can be veri<sup>fi</sup>ed that the positive effect is larger than the cost, that is, ${ U R ( e _ { H } ) } ^ { - } - { U R ( e _ { L } ) } -$ $( \pi _ { S } ^ { F B N } ( e _ { L } ) - \pi _ { S } ^ { F B N } ( e _ { H } ) ) > 0$ . As such, Term (II) of Equation (15) is positive, where $\pi _ { S } ^ { F B R } ( e _ { H } ) \dot { - } \pi _ { S } ^ { F B R } ( e _ { L } ^ { \bf \Phi } ) =$ $U R ( e _ { H } ) - \ U R ( e _ { L } ) - ( \pi _ { S } ^ { F B N } ( e _ { L } ) - \pi _ { S } ^ { F B N } \bar { ( e _ { H } ) ) }$ . We refer to this as the indirect uncertainty-resolution effect.

Lemma 2 (Positive Renegotiation Benefit). Without renegotiation cost, in the first-best solution, the Client always benefits from renegotiation, $R B ^ { F B } > 0$

Lemma 2 suggests that the direct uncertaintyresolution effect from effort $e _ { F B N } ^ { * }$ and the indirect uncertainty-resolution effect from extra effort $( e _ { F B R } ^ { * } -$ $e _ { F B N } ^ { * } )$ (if any) together comprise the positive renegotiation bene<sup>fi</sup>t, $R B ^ { \ l \ l \ l \mathrm { F } B }$ . This result is consistent with Susarla (2012), who empirically showed that renegotiation enables surplus enhancement.

## 4. Analysis of Contracts

We next examine Client–Vendor decisions under <sup>fi</sup>xed-price and time-and-materials contracts with or without renegotiation and obtain the impacts of renegotiation on their attractiveness for use and also on the contract terms.

## 4.1. Fixed-Price Contract

Under a <sup>fi</sup>xed-price contract, the Client <sup>fi</sup>rst determines the initial payment $P _ { F P }$ for software services at the contracting stage. Observing the payment, the Vendor decides the initial testing time t and exerts effort e to build the system during the development stage. In the case of a <sup>fi</sup>xed-price contract with renegotiation (FPR), after system development the renegotiation stage occurs. The two parties revise initial testing time t to renegotiated testing time ${ \tilde { t } } ,$ and share the renegotiation surplus RS <sup>˜</sup>t via their bargaining power. The Client incurs renegotiation cost $C _ { R }$ . Then the Vendor offers system testing and maintenance services to the Client. Thus, in the FPR case, given the initial <sup>fi</sup>xed payment $P _ { F P . }$ , the expected pro<sup>fi</sup>t for the Vendor in the development stage is as follows, where subscript V represents the Vendor,

$$
\begin{array}{c} \pi_ {V} ^ {F P R} (e, t) = E _ {\varepsilon} \Big [ \underbrace {P _ {F P}} _ {\text {initial payment}} - \underbrace {T C (e , t)} _ {\text {total cost of Vendor}} \\ + \underbrace {\alpha \cdot R S (\tilde {t} ^ {*})} _ {\text {profit from renegotiation}} \Big ]. \end{array}\tag{16}
$$

In the case of a <sup>fi</sup>xed-price contract without renegotiation (FPN), after system development, the Vendor tests the system for the initial amount of testing time t. Thus, Vendor pro<sup>fi</sup>t in the development stage is

$$
\pi_ {V} ^ {F P N} (e, t) = E _ {\varepsilon} \bigg [ \underbrace {P _ {F P}} _ {\text { payment }} - \underbrace {T C (e , t)} _ {\text { total   cost   of   Vendor }} \bigg ].\tag{17}
$$

In the contracting stage, anticipating the Vendor’s best response, $e ^ { * }$ and $t ^ { * } ,$ the Client determines the initial payment, $P _ { F P _ { 4 } }$ , to maximize its own pro<sup>fi</sup>t in the FPR and FPN cases, where subscript C represents the Client:

$$
\begin{array}{r} \pi_ {C} ^ {F P R} (P _ {F P}) = E _ {\varepsilon} \Bigg [ \underbrace {U (e ^ {*} , t ^ {*})} _ {\text {utility of Client}} - \underbrace {P _ {F P}} _ {\text {initial payment}} \\ + \underbrace {(1 - \alpha) \cdot R S (\tilde {t} ^ {*}) - C _ {R}} _ {\text {profit from renegotiation}} \Bigg ]; \end{array}\tag{18}
$$

$$
\pi_ {C} ^ {F P N} (P _ {F P}) = E _ {\varepsilon} \Bigg [ \underbrace {U (e ^ {*} , t ^ {*})} _ {\text { utility   of   Client }} - \underbrace {P _ {F P}} _ {\text { payment }} \Bigg ].\tag{19}
$$

Assuming the reservation pro<sup>fi</sup>t of the Vendor is $0 ,$ the individual rationality (IR) constraints for the Vendor are $\pi _ { V } ^ { F P R } ( e ^ { * } , t ^ { * } ) \geq 0$ and $\pi _ { V } ^ { F P N } ( e ^ { * } , t ^ { * } ) \ge 0$ in the two cases, respectively. They guarantee the Vendor a minimum expected pro<sup>fi</sup>t to accept the contract. According to Equations (16)–(19), the optimal development effort levels $e _ { F P R } ^ { * }$ and $e _ { F P N } ^ { * }$ , and optimal initial testing times $t _ { F P R } ^ { * }$ and $t _ { F P N } ^ { * }$ under the FPR and FPN cases in the <sup>fi</sup>xed-price contract can be obtained. Table C.2 in Appendix C provides the optimal initial testing times and development effort levels, where the regions are de<sup>fi</sup>ned by the thresholds of the Vendor’s bargaining power and system complexity.

Higher system complexity leads to a greater expected number of bugs $N _ { C S } ( e ) ;$ ; thus, we observe the optimal initial testing times in both the FPN and FPR cases increase with $\boldsymbol { \Upsilon } ,$ , as Appendix C, Table C.2, shows. In the FPN case, from $\frac { \partial ^ { 2 } \pi _ { V } ^ { F P N } ( e , \ t ) } { \partial t \partial e } < 0 ,$ , initial testing time is inversely related to the Vendor’s effort; thus, lower (higher) system complexity leads the Vendor to exert high (low) effort. In the FPR case, according to Equation (10), optimal renegotiated testing time $\tilde { t } ^ { * }$ is inversely related to the opti mal Vendor’s effort $e _ { F P R } ^ { * }$ as well. When the Vendor has low bargaining power, low (high) initial and renegotiated testing times stemming from low (high) system complexity lead the Vendor to exert high (low) effort; and when the Vendor has high bargaining power, low (high) renegotiated testing time causes it to exert high (low) effort.

Like the <sup>fi</sup>rst-best solution, when system complexity is moderate $( Y _ { 3 } \leq Y < \operatorname* { m i n } \{ \varUpsilon _ { 4 } , \dot { \varUpsilon _ { 5 } } \}$ in Table C.2, where $\boldsymbol { Y } _ { 3 } , ~ \boldsymbol { Y } _ { 4 }$ , and ${ { T } _ { 5 } }$ are the thresholds), the Vendor’s optimal effort for the FPR case is higher than that for the FPN case by the post-development incentive of renegotiation, leading to a positive indirect uncertainty-resolution effect. The thresholds $\boldsymbol { { \cal Y } } _ { 4 }$ and ${ { T } _ { 5 } }$ both increase with Vendor bargaining power $\alpha ,$ implying that the post-development incentive increases with the Vendor’s bargaining power. The intuition is that when the Vendor has higher bargaining power, it attains a larger share of renegotiation surplus and is incentivized to exert more effort to improve the total renegotiation surplus, if system complexity is moderate.

## 4.2. Time-and-Materials Contract

In a time-and-materials contract, the Client <sup>fi</sup>rst determines the initial <sup>fi</sup>xed payment $P _ { T M } ,$ per unit effort reimbursement r (for Vendor reported effort), and monitoring policy $\phi .$ . Then, the Vendor decides its input effort $e ,$ reported effort $\hat { e } ,$ and initial testing time t. After development, an updated expected number of system bugs $N _ { C S } ( e )$ is recognized. The parties renegotiate testing time t to <sup>˜</sup>t when renegotiation happens (TMR). Thus, given contract terms $\{ P _ { T M } , r , \phi \}$ in the TMR case, the expected Vendor pro<sup>fi</sup>t in the development stage is

$$
\begin{array}{l} \pi_ {V} ^ {T M R} (e, \hat {e}, t) = E _ {\varepsilon} \left[ \underbrace {(P _ {T M} + r \hat {e})} _ {\text { initial   payment }} - \underbrace {T C (e , t)} _ {\text { total   cost   of   Vendor }} - \underbrace {\phi s \cdot (\hat {e} - e) ^ {+}} _ {\text { penalty   for   misreporting }} \right. \\ \left. + \underbrace {\alpha \cdot R S (\tilde {t} ^ {*})} _ {\text { profit   from   renegotiation }} \right]. \end{array} \tag {2}\tag{20}
$$

In the time-and-materials contract without renegotiation (TMN), the parties commit to testing time $t ,$ and the Vendor’s pro<sup>fi</sup>t is

$$
\pi_ {V} ^ {T M N} (e, \hat {e}, t) = E _ {\varepsilon} \Biggl [ \underbrace {(P _ {T M} + r \hat {e})} _ {\text {payment}} - \underbrace {T C (e , t)} _ {\text {total cost of Vendor}} - \underbrace {\phi s \cdot (\hat {e} - e) ^ {+}} _ {\text {penalty for misreporting}} \Biggr ].\tag{21}
$$

With the Vendor’s best response $( e ^ { * } , \hat { e } ^ { * } , t ^ { * } )$ , the Client determines $\{ P _ { T M } , ~ r , ~ \phi \}$ to maximize pro<sup>fi</sup>t in the TMR and TMN cases<sup>19</sup>:

$$
\begin{array}{c} \pi_ {C} ^ {T M R} (P _ {T M}, r, \phi) = E _ {\varepsilon} \Bigg [ \underbrace {U (e ^ {*} , t ^ {*})} _ {\text {utility of Client}} - \underbrace {(P _ {T M} + r \hat {e} ^ {*})} _ {\text {initial payment}} \\ - \underbrace {w \phi} _ {\text {monitoring cost}} + \underbrace {(1 - \alpha) \cdot R S (\tilde {t} ^ {*}) - C _ {R}} _ {\text {profit from renegotiation}} \Bigg ]; \end{array}\tag{22}
$$

$$
\begin{array}{c} \pi_ {C} ^ {T M N} (P _ {T M}, r, \phi) = E _ {\varepsilon} \Bigg [ \underbrace {U (e ^ {*} , t ^ {*})} _ {\text {utility of Client}} - \underbrace {(P _ {T M} + r \hat {e} ^ {*})} _ {\text {payment}} \\ - \underbrace {w \phi} _ {\text {monitoring cost}} \Bigg ]. \end{array}\tag{23}
$$

Beyond the individuality rationality (IR) constraints for the Vendor, $\pi _ { V } ^ { T M R } ( e ^ { * } , \hat { e } ^ { * } , t ^ { * } ) \geq 0$ and $\pi _ { V } ^ { T M N } ( e ^ { * } ,$ $\hat { e } ^ { * } , t ^ { * } ) \geq 0 .$ , in the TMR and TMN cases, the Client faces incentive compatibility (IC) constraints: they are $\pi _ { V } ^ { T M R } ( e ^ { * } , \hat { e } ^ { * } = e ^ { * } , t ^ { * } ) \stackrel { } { \geq } \pi _ { V } ^ { T M R } ( e ^ { * } , \hat { e } ^ { * } \neq e ^ { * } , t ^ { * } )$ and $\pi _ { V } ^ { T M N }$ $( e ^ { \dot { \ast } } , \hat { e } ^ { \ast } = e ^ { \ast } , t ^ { \ast } ) \geq \pi _ { V } ^ { T M N } ( e ^ { \ast } , \hat { e } ^ { \ast } \neq e ^ { \ast } , t ^ { \ast } ) .$ , and ensure that the Vendor reveals its true effort. With Equations (20)–(23), optimal Client monitoring policies, Vendor efforts, and initial testing time under the TMR and TMN cases can be obtained, as shown in Table C.3 of Appendix $C ,$ where the regions are de<sup>fi</sup>ned by the thresholds of the Vendor’s bargaining power and system complexity.

In Table $C . 3 ,$ we also observe that, when system complexity is too low or too high, the Client’s monitoring policies under the TMR and TMN cases become $0 ~ \left( \phi _ { T M R } ^ { * } = 0 \right.$ and $\phi _ { T M N } ^ { * } = 0 )$ . This implies the time-and-materials contract degenerates into the <sup>fi</sup>xed-price contract. The intuition is that when system complexity $\boldsymbol { r }$ is too low, under either contract (TM or FP) the Vendor exerts the effort of the <sup>fi</sup>rst-best solu tion. When system complexity $\boldsymbol { r }$ is too high, the Vendor does not exert high development effort under either contract. While, because the time-and-materials contract includes an effort reimbursement, the Vendor intends to misreport its effort. To deter this, the Client should adopt a high-cost monitoring policy. Thus, it will no longer use effort reimbursement and monitoring.

Furthermore, compared with the <sup>fi</sup>xed-price contract, when system complexity satis<sup>fi</sup>es the condition $\boldsymbol { { \cal T } } _ { 3 } \le$ $\mathcal { T } < \mathcal { r } _ { 6 } ~ ( \mathcal { T } _ { 3 }$ and $\boldsymbol { { \cal Y } } _ { 6 }$ are the thresholds in Table $C . 3 )$ the Vendor exerts high development effort in the timeand-materials contract without renegotiation (TMN) but low effort in the <sup>fi</sup>xed-price contract without renegotiation (FPN), as shown in the details of Appendix $C ,$ Table C.3. This implies that the Client can incentivize the Vendor’s effort in the time-and-materials contract via the pre-development incentive of monitoring. Simi lar to the <sup>fi</sup>rst-best solution, as earlier, when system complexity is moderate, $( T _ { 6 } \leq T <$ min $\{ \boldsymbol { { \ Y } } _ { 7 } , \boldsymbol { { \dot { Y } } } _ { 8 } \}$ in Table C.3), the Vendor exerts high effort in the TMR case but low effort in the TMN case because of the post-development incentive of renegotiation. In the TMR case, the positive direct uncertainty-resolution effect and positive indirect uncertainty-resolution effect (if any) constitute the positive aggregate renegotiation bene<sup>fi</sup>t.

## 4.3. Comparison Between Initial and Renegotiated Testing Time

In this section, we consider the possible renegotiation in the FPR and TMR cases and analyze the impacts of renegotiation on testing time and the payments.

For the testing time, it can be veri<sup>fi</sup>ed that the expected renegotiated testing time $E _ { \varepsilon } [ \tilde { t } ^ { * } ]$ is shorter (longer) than the optimal initial testing times in both the FPR and TMR cases if the Vendor has low (high) bargaining power. The intuition is that when deciding the initial testing time, the Vendor aims to maximize its own pro<sup>fi</sup>t in Equations (16) and (20). However, when deciding the renegotiated testing time, the Vendor and the Client maximize the total returns (social surplus). Shorter testing time implies a higher-value customized system for the Client, $\boldsymbol { \gamma } \cdot ( \boldsymbol { T } - \boldsymbol { t } )$ , but it leaves a greater expected number of bugs in the system after testing, $\bar { N _ { C S } } ( e ) \cdot \exp ( - \lambda t )$ , and higher maintenance cost for the Vendor. Thus, if the Vendor has low bargaining power, the renegotiated testing time is expected to be shorter than the optimal initial one. Meanwhile, if the Vendor has high bargaining power, with the high revenue share of the renegotiation surplus, it sets the initial testing time at 0 and then renegotiates a higher testing time with the Client, which reduces the Vendor’s initial payoff but substantially increases the renegotiation surplus. On the other hand, the realized renegotiated testing time $\tilde { t } ^ { * }$ in the renegotiation stage also depends on the outcome of Vendor’s effort in system development. It may be longer (shorter) than the optimal initial testing time when the outcome is unfavorable (favorable) after system development.

For the payment, it can be veri<sup>fi</sup>ed that the ex post prices $\tilde { P } _ { F P }$ and $\tilde { P } _ { T M }$ in both the FPR and TMR cases increase after renegotiation compared with initial prices $P _ { F P }$ and $P _ { T M } .$ . This is because, if there is no renegotiation, the Client reimburses the Vendor for the cost $T C ( e , t )$ based on the initial testing time. However, the ex post prices $\tilde { P } _ { F P }$ and $\tilde { P } _ { T M }$ are comprised of the initial prices $P _ { F P }$ and $P _ { T M }$ and the share of renegotiation surplus $\alpha \cdot R S ( \widetilde { t } ^ { * } )$ stemming from the renegotiated testing time. According to Lemma 1, renegotiation surplus is always positive; thus, the Vendor obtains higher payments after renegotiation.

## 5. Interaction Between Monitoring and Renegotiation

Because some Clients choose to renegotiate with their Vendor, whereas others do not, renegotiation is a realistic choice. We found earlier that monitoring and renegotiation can incentivize a Vendor’s effort. The difference between a <sup>fi</sup>xed-price and a time-andmaterials contract is whether to monitor Vendor effort. Thus, monitoring is a realistic choice too. This leads us to investigate the interaction between monitoring and renegotiation and the appropriate contract for the Client.<sup>20</sup> We analyze contract choice when: monitoring and renegotiation are costless: one incurs cost but not the other (and vice versa); and both incur costs.

5.1. Costless Monitoring and Costless Renegotiation We <sup>fi</sup>rst consider negligible monitoring and renegotiation costs, $w = 0$ and $C _ { R } = 0 .$ . By comparing the Client’s pro<sup>fi</sup>ts in the FPR, FPN, TMR, and TMN cases, we can derive the Client’s choice for monitoring and renegotiation. For this, we de<sup>fi</sup>ne two thresholds for the Vendor’s bargaining power, $\alpha _ { 1 }$ and $\alpha _ { 2 }$ , with $\alpha _ { 1 } < \alpha _ { 2 }$ . The online appendix provides additional details. Client choice is given by the following.

Proposition 1 (Client Contract Choice for Costless Monitoring and Costless Renegotiation). When monitoring and renegotiation are costless, $w = 0$ and $C _ { R } = 0 !$

i. $H \alpha _ { 1 } < \alpha < \alpha _ { 2 } ,$ , the Client chooses both monitoring and renegotiation (TMR), which complement each other.

ii. Otherwise, the Client chooses renegotiation only (FPR) and it substitutes for monitoring.

We use complements and substitutes for the relationship between monitoring and renegotiation. When they are complements, their simultaneous use increases the bene<sup>fi</sup>ts of the other; in contrast, when they are substitutes, their simultaneous use decreases the bene<sup>fi</sup>ts from the other (Tiwana 2010). Recall that renegotiation bene<sup>fi</sup>ts exist in both <sup>fi</sup>xed-price and time-and-materi als contracts. When renegotiation is costless, the Client always chooses renegotiation to increase its pro<sup>fi</sup>t. If the Vendor’s bargaining power becomes low in Proposition 1(i), $( \alpha _ { 1 } < \alpha < \alpha _ { 2 } )$ , the post-development incentive is limited in the <sup>fi</sup>xed-price contract. The positive indirect uncertainty-resolution effect stems from the additional effort compared with the nonrenegotiation case. Thus, the Client adopts monitoring as a complement to incentivize Vendor effort, and a timeand-materials contract with renegotiation (TMR) is preferred.

If the Vendor has high bargaining power, $\alpha _ { 2 } \leq \alpha \leq 1$ , the post-development incentive is strong, so the Vendor exerts high effort, and the Client does not use monitoring. Thus, renegotiation substitutes for monitoring, and the Client prefers a <sup>fi</sup>xed-price contract with renegotiation (FPR). For example, the National Aeronautics and Space Administration and Google partnered to sign a <sup>fi</sup>xed-price contract worth US\$10 million with D-Wave for quantum computing systems (Knapp 2013) and extended it two years later (Harris 2015). D-Wave had higher bargaining power in contracting because it was the only commercial supplier of quantum computers (Alto 2017).

The threshold $\alpha _ { 1 } \geq 0$ weakly increases with system complexity and when the complexity is high, $\alpha _ { 1 } > 0$ . In this case, for the region $0 \leq \alpha \leq \alpha _ { 1 } .$ , the Vendor exerts low effort, and the pre- and postdevelopment incentives do not work. Furthermore, the time-and-materials contract degenerates into a <sup>fi</sup>xed-price contract, and the Client uses renegotiation to bene<sup>fi</sup>t from the direct uncertainty-resolution effect only.

## 5.2. Costly Monitoring and Costless Renegotiation

What about when monitoring policy φ incurs cost wφ with no renegotiation costs, so $C _ { R } = 0 ?$ We de<sup>fi</sup>ne a threshold for per unit cost of monitoring wˆ . (Detailed expositions in the online appendix.)

Proposition 2 (Client Contract Choice for Costly Monitoring and Costless Renegotiation). When monitoring policy φ incurs cost wφ $( w > 0 )$ and renegotiation is costless $( C _ { R } = 0 )$ , the Client’s choice is determined in one of two ways:

i. $H f \alpha _ { 1 } < \alpha < \alpha _ { 2 }$ and $0 < w < \hat { w }$ , the Client selects monitoring and renegotiation (TMR) (complementary elements).

ii. Otherwise, the Client chooses renegotiation only (FPR), and it substitutes for monitoring.

We illustrate the results of Proposition 2 when $\alpha _ { 1 } = 0$ in Figure 2. In Region II, for Proposition 2(i), where per unit cost of monitoring is low and the Vendor has low bargaining power, the post-development incentive is limited by the low renegotiation surplus share of the Vendor in the <sup>fi</sup>xed-price contract. Recall that the indirect uncertainty-resolution effect of renegotiation stems from added Vendor effort compared with the nonrenegotiation case. Thus, the Client chooses to adopt monitoring for the pre-development incentive to create the indirect uncertainty-resolution effect of renegotiation. A time-and-materials contract with

Figure 2. Client Contract Choice Under Costly Monitoring and Costless Renegotiation  
![](/api/attachments/72VN8DNB/fulltext/images/d7acc44b1499ab7ba31e25549c2ca9b82e4e2928b88e6527ccaa2a06b1d08982.jpg)

$$
a _ {1} = 0.
$$

renegotiation (TMR) is preferred, and the two contract elements are complementary.

Regions I and III depict the results of Proposition 2(ii). In Region I, the post-development incentive from renegotiation is suf<sup>fi</sup>cient because of the Vendor’s high bargaining power, and it applies high effort to develop the system. Thus, the Client adopts renegotiation only (FPR) and that substitutes for monitoring. When per unit cost of monitoring is high and the Vendor has low bargaining power in Region III, the indirect uncertaintyresolution effect of renegotiation is not strong enough to enhance the bene<sup>fi</sup>t from the pre-development incentive of monitoring, which is dominated by monitoring cost. Therefore, the Client chooses renegotiation only (FPR) consistent with Benaroch et al. (2016). This shows that renegotiation substitutes for monitoring when it is costly. To illustrate, General Motors (GM) has other Vendors and an IT services subsidiary, EDS (Barkholz 2010), im plying $\mathrm { H P } ^ { \prime } \mathbf { s }$ bargaining power is lower than GM’s. Because of the high monitoring cost (Savitz 2013), GM and HP inked a <sup>fi</sup>xed-price contract and renewed it four years later (Barkholz 2010).

Similar to costless monitoring and renegotiation, with costly monitoring, when $\alpha _ { 1 } > 0 ,$ , in the region $0 \leq \alpha \leq \alpha _ { 1 }$ , the Vendor never exerts high effort because of high system complexity, making the pre- and postdevelopment incentives invalid. Thus, the Client adopts a <sup>fi</sup>xed-price contract with renegotiation (FPR) and reaps the bene<sup>fi</sup>t from the direct uncertaintyresolution effect of renegotiation only.

## 5.3. Costless Monitoring and Costly Renegotiation

What about when monitoring cost is negligible, $w = 0 ,$ and renegotiation incurs a cost, $C _ { R } > 0 \bar { ? }$ For this, we de<sup>fi</sup>ne another threshold for system complexity $\boldsymbol { { \cal Y } } _ { 9 } ,$ discussed in the online appendix.

Proposition 3 (Client Contract Choice for Costly Monitoring and Costless Renegotiation). When monitoring is costless $( w = 0 )$ and renegotiation has cost $C _ { R } > 0 _ { , }$ , the Client’s choice is

i. For $C _ { R } < \mathrm { m i n } \big \{ R B ^ { F P } , R B ^ { T M } \big \}$ , (a) $i f \alpha _ { 1 } < \alpha < \alpha _ { 2 } ,$ , it chooses both monitoring and renegotiation (TMR), which complement each other; and (b) otherwise, renegotiation substitutes for monitoring and it chooses renegotiation only (FPR). C

ii. For $C _ { R } \geq \operatorname* { m i n } \{ R B ^ { F P } , R B ^ { T M } \}$ , (a) if $\begin{array} { r } { \hat { Y } _ { 3 } \le \hat { Y } < \hat { Y } _ { 9 } , } \end{array}$ it uses monitoring only (TMN), which substitutes for renegotiation; and (b) otherwise, it uses neither (FPN).

The results of Proposition 3 are shown in Figure 3.

When renegotiation cost is low, in Proposition 3(i), the Client always chooses renegotiation for development uncertainties. However, whether the Client uses monitoring depends on the Vendor’s bargaining power in renegotiation. If it has low power, $\alpha _ { 1 } < \alpha < \alpha _ { 2 } ,$ , in Proposition 3(i.a) (moderate system complexity in Region V), the post-development incentive is limited. The Client chooses monitoring for the pre-development incentive to obtain the indirect uncertainty-resolution effect of renegotiation. Thus, monitoring and renegotiation are complements, and the Client selects a time-and-materials contract with renegotiation (TMR).

Figure 3. Client Contract Choice Under Costless Monitoring and Costly Renegotiation  
![](/api/attachments/72VN8DNB/fulltext/images/3408e416512c1642b1b28620cefb2b12bb7624fcc40c10dbe1ba43b111e4908e.jpg)

If the Vendor has high bargaining power, $\alpha _ { 2 } \leq \alpha \leq 1 ,$ in Proposition 3(i.b), the post-development incentive is strong enough to incentivize it to exert high effort. Thus, in Region IV, renegotiation substitutes for monitoring, and the Client selects a <sup>fi</sup>xed-price contract with renegotiation (FPR). Similar to Propositions 1 and 2, when α<sub>1</sub> > 0 (with high system complexity in Region VI), in the region $0 \leq \alpha \leq \alpha _ { 1 } .$ , the pre- and post-development incentives do not work. Therefore, the Client selects a <sup>fi</sup>xedprice contract with renegotiation (FPR) for the bene<sup>fi</sup>t from the direct uncertainty-resolution effect only.

When renegotiation cost is high, as in Proposition 3(ii), the renegotiation bene<sup>fi</sup>t is dominated by its cost, and the Client does not select renegotiation. Thus, the Client decides whether to adopt monitoring. If it has moderate system complexity as in Proposition 3(ii.a), monitoring substitutes for renegotiation to incentivize more Vendor effort, and the Client adopts a time-andmaterials contract without renegotiation (TMN; Region II). If system complexity is low (Region I), the Vendor exerts high effort. Thus, the Client does not need to incentivize the Vendor, and a <sup>fi</sup>xed-price contract only (FPN) works. If system complexity is high (Region III), the Vendor exerts low effort, and the predevelopment incentive does not work. Thus, the Client uses neither monitoring nor renegotiation (FPN).

## 5.4. Costly Monitoring and Costly Renegotiation

We now examine the scenario where both monitoring and renegotiation are costly. The Client’s choice for using monitoring and renegotiation is summarized by the following.

Proposition 4 (Client Contract Choice Under Costly Monitor ing and Costly Renegotiation). When monitoring and renegotiation are costly $( w > 0 , C _ { R } > 0 )$ , the Client’s choice is:

i. For $C _ { R } < \operatorname* { m a x } \{ R B ^ { F P } , ~ R B ^ { T M } \} ,$ , (a) if $\alpha _ { 1 } < \alpha < \alpha _ { 2 }$ and $0 < w < \hat { w }$ , then it chooses both monitoring and renegotiation (TMR), which complement each other; and (b) otherwise, renegotiation substitutes for monitoring and it uses renegotia tion only (FPR).

ii. For $C _ { R } \geq \operatorname* { m i n } \{ R B ^ { F P } , R B ^ { T M } \}$ , (a) if $\begin{array} { r } { \begin{array} { r } { \mathcal { r } _ { 3 } \leq \mathcal { r } < \mathcal { r } _ { 6 } , } \end{array} } \end{array}$ , it uses monitoring only (TMN), which substitutes for renegotiation; and (b) otherwise, it uses neither one (FPN).

Figure 4 shows results for Proposition 4 when system complexity is moderate. Naturally, when renegotiation cost is low, the Client always prefers it in Proposition 4(i), and when the cost is high, renegotiation is not used in Proposition 4(ii). With low renegotiation cost, similar to Proposition 2, Proposition 4(i.a) shows that if the Vendor has low bargaining power and per unit cost of monitoring is low, monitoring and renegotiation are complements, and the Client selects a time-and-materials contract with renegotiation (TMR) (Region IV; Figure 4). Otherwise, in Proposition 4(i.b) (Regions III and V), renegotiation substitutes for monitoring, and the Client selects a <sup>fi</sup>xed-price contract with renegotiation (FPR). In Region III of Figure 4, the postdevelopment incentive from renegotiation is suf<sup>fi</sup>cient because of the Vendor’s high bargaining power (like Region I; Figure 2). Thus, the Client adopts renegotiation only (FPR). In Region V of Figure 4, the bene<sup>fi</sup>t from the pre-development incentive of monitoring is dominated by its cost (similar to Region III; Figure 2). Therefore, the Client adopts renegotiation only (FPR).

With high renegotiation cost, similar to Proposition 3(ii), renegotiation is not used, and the Client’s decision is whether to adopt monitoring. If the bene<sup>fi</sup>t from the pre-development incentive of monitoring dominates its cost, in Proposition 4(ii.a) (Region I, Figure 4), the Client adopts monitoring to incent Vendor effort and selects a time-and-materials contract without renegotiation (TMN). Yet, if monitoring cost is higher than its bene<sup>fi</sup>t, Proposition 4(ii.b), the Client uses neither monitoring nor renegotiation and selects a <sup>fi</sup>xed-price contract without renegotiation (FPN) (Region II; Figure 4).

Figure 4. Client Contract Choice Under Costly Monitoring and Costly Renegotiation  
![](/api/attachments/72VN8DNB/fulltext/images/5a69a64add2223754ec87f5d647924e38c6c9d863b9374eae8881f141da7b0e6.jpg)  
Note. $\begin{array} { r } { \textstyle \mathcal { Y } _ { 3 } \leq \textstyle { \mathcal { Y } } < \operatorname* { m i n } \{ \mathcal { Y } _ { 7 } , \mathcal { Y } _ { 8 } \} . } \end{array}$

Furthermore, when per unit cost of monitoring becomes lower, the Client prefers to adopt both monitoring and renegotiation with larger renegotiation costs. The reason for such adoption is that when the Client uses monitoring to stimulate high Vendor effort with lower cost, the indirect uncertainty-resolution effect of renegotiation will be created. The Client bene<sup>fi</sup>ts more from renegotiation, generating a higher threshold for the renegotiation cost that determines whether renegotiation is chosen. For example, the U.S. Department of Defense (DoD) built a partnership with SAP, resulting in low monitoring cost. This further led DoD to sign a time-and-materials contract with SAP for enterprise resource planning and <sup>fi</sup>nancial programs (Hoover 2016), and the contract was renewed within the budget (Culclasure and Neff 2016).

## 6. Vendor Effort and Client Profit

## Changes: Sensitivity Analysis Results

We now analyze how Vendor effort and Client pro<sup>fi</sup>t change with the model parameters. However, we assess only some elements: system complexity , bug rate B c , and system lifetime T.

## 6.1. System Complexity and Bug Rate

Clients have various system complexity needs , and Vendors differ in development capability leading to diverse bug rates B c . We assess how system complexity and the bug rate affect Client and Vendor.

Corollary 1 (Impacts of System Complexity and Bug Rate on Vendor Effort and Client Profit). The Vendor is more likely to exert low effort when system complexity  is greater or the bug rate B c is higher, and Client profit decreases in $\boldsymbol { r }$ and B c .

It can be veri<sup>fi</sup>ed that greater system complexity or a higher bug rate leads to a greater expected number of bugs in the system, resulting in longer initial testing time in both the <sup>fi</sup>xed-price and time-and-materials contracts. Because the optimal initial testing time is inversely related to the Vendor’s effort, it is more likely to exert low effort with increasing system complexity and bug rate. Furthermore, the marginal bene<sup>fi</sup>t of the Vendor’s effort from the renegotiation surplus decreases in both system complexity and bug rate. Thus, the increased system complexity or bug rate also weakens the post-development incentive of renegotiation and further reduces the Vendor’s desire to exert high effort in system development.

According to Proposition 4, the Client’s pro<sup>fi</sup>t decreases in the expected number of bugs. Thus, the Client obtains lower pro<sup>fi</sup>t when system complexity or the bug rate increases. Furthermore, with Corollary 1, we observe that when system complexity is moderate, the region where the Client selects a <sup>fi</sup>xed-price contract without renegotiation (FPN) is enlarged by the increased system complexity or bug rate, as shown in Figure 5. The reason is that the direct and indirect uncertainty-resolution effects decrease with the expected number of bugs, which increases, in turn, with system complexity and bug rate. Recall that the indirect uncertainty-resolution effect generates postdevelopment incentive of renegotiation and strengthens the pre-development incentive of monitoring. Thus, the increased system complexity or bug rate reduces the effort incentives of renegotiation and monitoring, yielding a low likelihood of selecting monitoring and renegotiation.

Figure 5. Impacts of System Complexity and Bug Rate on Client Contract Choice  
![](/api/attachments/72VN8DNB/fulltext/images/17df0c62ebca5e09df76e0f7bb3e7ef4738cf89303b8bb730999f04ef01d84db.jpg)  
Note. $\ : T _ { 3 } \leq T < \ :$ < min $\boldsymbol { { \cal T } } _ { 7 } ,$ $ { \boldsymbol { { Y } } } _ { 8 }   \boldsymbol { \} }$ and “ ” implies the direction that increasing or B(c) pushes the region line to move into.

## 6.2. System Lifetime

A customized system’s lifetime T plays an important role in outsourcing (Ji et al. 2011, August and Niculescu 2013), and it includes the testing and maintenance times in our model. The following corollary shows how system lifetime affects the Client’s and Vendor’s decisions.

Corollary 2 (Impacts of System Lifetime on Vendor Effort and Client Profit). The Vendor is more likely to exert high effort when system lifetime T is longer, and Client profit increases in T.

Corollary 2 <sup>fi</sup>rst suggests that increased system lifetime incentivizes the Vendor to exert high effort in development. The intuition is that, with a longer system lifetime, more bugs may occur in both the <sup>fi</sup>xed-price and time-and-materials contracts, generating higher bug-<sup>fi</sup>x costs for the Vendor. To reduce them, the Vendor makes high effort in development to decrease their expected number. Meanwhile, the Client bene<sup>fi</sup>ts from the decreased bugs resulting from Vendor’s high effort after it has <sup>fi</sup>nished development. In addition, longer system lifetime increases the value of the system, which bene<sup>fi</sup>ts the Client as well.

Based on Corollary 2, we further observe that when system complexity is moderate, the regions in which the Client selects renegotiation are enlarged by the increased system lifetime, as illustrated in Figure 6. The reason is that, according to Lemma 2, the increased Vendor effort caused by the longer system lifetime creates the indirect uncertainty-resolution effect and increases the renegotiation bene<sup>fi</sup>t in the <sup>fi</sup>xed-price and time-and-materials contracts. Thus, the Client is more likely to select renegotiation when system lifetime increases.

## 7. Extensions

Our base model considers two effort levels, $e _ { H }$ and $e _ { L } ,$ that the Vendor chooses to make in system development. We now extend discrete effort to continuous effort, and <sup>fi</sup>rst check how the Client’s and the Vendor’s decisions change. Then, we examine how our main results are affected when renegotiation cost is endogenous and depends on the renegotiation process.

Figure 6. Impacts of System Lifetime on Client Contract Choice  
![](/api/attachments/72VN8DNB/fulltext/images/ecb8c0b09bdf371812ff62eba3269d42fb45abb5ea721c40e2292215adfdf967.jpg)  
Note. $\ : T _ { 3 } \leq T < \ :$ min $ { \boldsymbol { Y } } _ { 7 } ,  { \boldsymbol { Y } } _ { 8 }  { \boldsymbol { \jmath } }$ and $^ { \prime \prime } \longrightarrow ^ { \prime \prime }$ implies the direction that increasing T pushes the region line to move into.

## 7.1. Continuous Development Effort

Compared with the base model, we allow that the Vendor exerts effort $e ( e \geq 0 )$ to decrease the expected number of bugs in system development. By solving the Vendor’s and the Client’s problems with continu ous development effort, we prove that, similar to the base model, renegotiation generates direct and indirect uncertainty-resolution effects (both are positive) and a post-development incentive, and monitoring generates a pre-development incentive. We next summarize the Client’s contract choice when both moni toring and renegotiation are costly. For this, we de<sup>fi</sup>ne a function for per unit cost of monitoring Ω w , two thresholds for per unit cost of monitoring $w _ { E 1 }$ and w<sub>E2</sub>, and two thresholds for renegotiation cost $C _ { R } ^ { E 1 }$ and $C _ { R } ^ { E 2 }$ . The online appendix offers additional details of the modeling derivation for this.

Proposition 5 (Client Contract Choice Under Continuous Development Effort). When monitoring and renegotiation are costly $( w > 0 , C _ { R } > 0 )$ , the Client’s choice is:

i. For $\Omega ( w ) \leq 0 , ( { \mathsf { a } } ) i f C _ { R } < C _ { R } ^ { E 1 } ,$ , the Client chooses both monitoring and renegotiation (TMR); (b) $i f C _ { R } \geq C _ { R } ^ { E 1 }$ and $0 < w \leq w _ { E 1 }$ , it chooses monitoring only (TMN); and (c) otherwise, it uses neither one (FPN).

ii. For $\Omega ( w ) > 0 ,$ , (a) if $C _ { R } < \operatorname* { m a x } \{ C _ { R } ^ { E 1 } , C _ { R } ^ { E 2 } \}$ and $0 < w \le w _ { E 2 }$ , the Client chooses both monitoring and renegotiation (TMR); (b) $i f C _ { R } < \operatorname* { m a x } \{ C _ { R } ^ { E 1 } , C _ { R } ^ { E 2 } \}$ and $w > w _ { E 2 }$ , it chooses renegotiation only (FPR); and (c) otherwise, it uses neither (FPN).

Figure 7. Client Contract Choice Under Continuous Development Effort  
![](/api/attachments/72VN8DNB/fulltext/images/6b9cbfc76c3937993daffb174e0fbb8c639a11c4eedd8334b91fbce01e4f0d08.jpg)  
Notes. (a) Ω  w <sub>≤</sub> 0. (b) Ω  w > 0.

Figure 7 illustrates Proposition 5 when $\Omega ( w ) \leq 0$ and Ω w > 0. When $\Omega ( w ) \leq 0 ,$ , with low renegotiation cost (Region III; Figure 7(a)), Proposition 5(i.a) shows that the Client chooses both monitoring and renegotiation (TMR), and the two are complements. With high renegotiation cost, renegotiation becomes inef<sup>fi</sup>cient, and the Client decides whether to adopt monitoring. If per unit cost of monitoring is low (Region I; Figure 7(a)), Proposition 5(i.b) indicates the Client chooses time-and-materials contract without renegotiation (TMN). If per unit cost of monitoring is high (Region II; Figure 7(a)), the pre-development incentive of monitoring is dominated by its cost. Thus, the Client selects the <sup>fi</sup>xed-price contract without renegotiation (FPN) in Proposition 5(i.c).

When Ω w > 0 (implying $w > w _ { E 1 } )$ , the bene<sup>fi</sup>t from the pre-development incentive of monitoring is dominated by its cost if only monitoring is adopted. With high renegotiation cost (Region I; Figure 7(b)), Proposition 5(ii.c) states the Client selects neither monitoring nor renegotiation (FPN). With low renegotiation cost, the Client always chooses renegotiation for its postdevelopment incentive and direct and indirect uncertainty-resolution effects. At the same time, if per unit cost of monitoring, w is less than $w _ { E 2 }$ (Region II; Figure 7(b)), the indirect uncertainty-resolution effect of renegotiation enhances the pre-development incentive of monitoring, and they dominate the monitoring cost. Thus, the Client chooses the time-and-materials contract with renegotiation (TMR), as in Proposition 5(ii.a). If per unit cost of monitoring is high (Region III; Figure 7(b)), Proposition 5(ii.b) shows that the Client chooses <sup>fi</sup>xed-price contract with renegotiation (FPR) because the bene<sup>fi</sup>t of monitoring is less than its cost.

![](/api/attachments/72VN8DNB/fulltext/images/49efc0934fd2b2b47b60bed031feab29ed9e36aaa103e9f0629fda8a9e70fe8a.jpg)

## 7.2. Endogenous Renegotiation Cost

In the base model, we assume the cost of renegotiation is independent of its outcome. Previous literature also has treated renegotiation cost as an endogenous variable linked to renegotiation surplus (Guasch et al. 2006). We now examine when renegotiation cost is proportional to renegotiation surplus and how our results are affected. In contrast to the base model, we assume that the renegotiation cost becomes ζ RS <sup>˜</sup>t , where $\zeta \geq 0 .$ . Then, when the renegotiation process begins, the Vendor and the Client split the renegotiation pro<sup>fi</sup>t 1 ζ RS <sup>˜</sup>t according to their bargaining power α and 1 α. Solving the Vendor’s and the Client’s problems with endogenous renegotiation cost, we can derive the Client’s optimal contract. We <sup>fi</sup>nd that the base model’s results keep qualitatively. For this, we de<sup>fi</sup>ne a threshold for the Vendor’s bargaining power $\alpha _ { E 1 }$ , two thresholds for per unit cost of monitoring w<sub>E3</sub> and $w _ { E 4 }$ . See the online appendix for details.

Proposition 6 (Client Contract Choice Under Endogenous Renegotiation Cost). When renegotiation cost is proportional to renegotiation surplus $( \bar { C _ { R } } = \zeta \cdot R S ( \tilde { t } ) )$ , the Client’s choice is:

i. For $0 < \zeta < 1 , i f ( \mathrm { a } ) 0 < w \le w _ { E 3 } , o r ( \mathsf { b } ) w _ { E 3 } < w < w _ { E 4 }$ and $\alpha _ { E 1 } < \alpha \leq 1$ , it selects both monitoring and renegotiation (TMR); and $i f \left( \mathrm { c } \right) w _ { E 3 } < w < w _ { E 4 }$ and $0 < \alpha \leq \alpha _ { E 1 }$ , or $\mathrm { ( d ) } w \geq w _ { E 4 } ,$ , it chooses renegotiation only (FPR).

ii. $F o r \ \zeta \geq 1 , \ i f \ ( \mathsf { a } ) \ 0 < w < w _ { E 1 }$ , it chooses monitoring only (TMN); and (b) i $\dot { \boldsymbol { w } } \geq \boldsymbol { w } _ { E 1 }$ , it uses neither (FPN).

According to Proposition 6(i), when $0 < \zeta < 1$ , implying the renegotiation cost is lower than the renegotiation surplus (similar to when renegotiation cost $C _ { R }$ is low in our base model), the Client always chooses renegotiation. Proposition 6(i.a) (Proposition $6 ( \mathrm { i . d } ) )$ shows that, if per unit cost of monitoring is low (high), the Client selects (does not select) monitoring, and adopts a time-and-materials (<sup>fi</sup>xed-price) contract with renegotiation. If per unit cost of monitoring is moderate and the Vendor has high bargaining power, in Proposition 6(i.b), the increased post-development incentive of renegotiation enhances the indirect uncertainty-resolution effect and further increases the bene<sup>fi</sup>t from the pre-development incentive. Thus, the Client chooses both monitoring and renegotiation (TMR). If per unit cost of monitoring is moderate and the Vendor has low bargaining power, Proposition 6(i.c) shows that the Client chooses renegotiation (FPR) only because the indirect uncertainty-resolution effect is not strong enough to allow the pre-development incentive to cover the cost of monitoring.

When $\zeta \geq 1 .$ , the renegotiation cost is higher than the renegotiation surplus (similar again to when renegotiation cost $C _ { R }$ is high in our base model), renegotiation is not chosen, and the Client decides to select monitoring instead. Proposition 6(ii.a) shows that the Client chooses the time-and-materials contract without renegotiation (TMN) with low monitoring cost, and Proposition 6(ii.b) suggests that it selects the <sup>fi</sup>xed-price contract without renegotiation (FPN) with high monitoring cost.

## 8. Discussion

We conclude with contributions and insights obtained for a client’s software outsourcing contract strategy. We also share our thoughts on related applications of the modeling ideas.

## 8.1. Contributions

Our primary contribution is to provide novel insights about the way monitoring and opportunistic renegotiation may be complements, counter to the prevailing wisdom that monitoring prevents the vendor’s ex post opportunism. An important reason for this is that we identify the positive direct and indirect uncertaintyresolution effects generated by renegotiation to resolve uncertainty about system development and make testing time ef<sup>fi</sup>cient ex post. The indirect uncertainty resolution effect stems from the added effort compared with the nonrenegotiation case. Because monitoring generates a pre-development incentive to stimulate vendor effort, the client may adopt monitoring as a comple ment to incentivize vendor effort, resulting in the indirect uncertainty-resolution effect. This occurs only when the vendor has low bargaining power, and monitoring and renegotiation costs are low though.

A related insight is that monitoring and renegotiation are substitutes: they both stimulate the vendor’s effort. Counter to the conclusion that contract theory research has drawn, renegotiation results in underinvestment by the investing party that fears expropriation of its bene-<sup>fi</sup>ts by its contracting partner in the process (Maskin and Moore 1999). This again is the familiar hold-up problem. We demonstrate that testing time renegotiation incentivizes a vendor to invest in more development effort because the positive indirect uncertaintyresolution effect results from extra effort compared with the nonrenegotiation case, and the vendor attains renegotiation surplus according to its bargaining power. To stimulate the indirect uncertainty-resolution effect and obtain more bene<sup>fi</sup>ts from renegotiation, the vendor has an incentive to exert more effort in develop ment. This is a post-development incentive that increases in the vendor’s bargaining power.

Another contribution of our work is that, as the client contemplates which contract form works better—a <sup>fi</sup>xed-price or time-and-materials contract—and whether to renegotiate with the vendor after system development, the optimal contract strategy is determined by the interaction between monitoring and renegotiation. They are further moderated by the renegotiation cost, monitoring cost, and the two parties’ bargaining power in renegotiation. These insights are far-reaching for practice.

With low renegotiation cost, the client always adopts renegotiation. If the Vendor has low bargaining power and per unit cost of monitoring is low, monitoring and renegotiation are complements, and the client selects a time-and-materials contract with renegotiation. Otherwise, renegotiation substitutes for monitoring, and the client chooses a <sup>fi</sup>xed-price contract with renegotiation. With high renegotiation cost, renegotiation should not be chosen, and the client decides whether to adopt monitoring. If the per unit cost of monitoring is low, monitoring substitutes for renegotiation to incentivize the vendor’s effort, and the client adopts a time-and-materials contract without renegotiation. Otherwise, the client does not use monitoring or renegotiation and instead goes with a <sup>fi</sup>xed-price contract without renegotiation. A decision tree summarizes our results for the client’s contract choice, as Figure 8 shows.

Figure 8. Decision Tree for Client Contract Choice  
![](/api/attachments/72VN8DNB/fulltext/images/fe387c10e47451f771c30e1c8c2313bdbdb88d84fa3ee9e8d6d4836dbfa5e799.jpg)

We further <sup>fi</sup>nd that the vendor is more likely to exert low effort when system complexity is greater or the bug rate gets higher and to exert high effort when system lifetime lengthens. Moreover, the client’s pro<sup>fi</sup>t decreases in system complexity and bug rate and increases in system lifetime. The main <sup>fi</sup>ndings in the base model hold qualitatively in two situations where we consider continuous effort, and the renegotiation cost endogenously depends on the renegotiation process.

Our analysis related to bug detection is founded on the G-O model, which is valid and offers an appropriate way to handle bug detection in the presence of new technologies, including automated bug detection with machine learning and cloud computing. The online appendix offers further discussion of the G-O model assumptions related to this. Thus, our results can be applied in large-scale system implementation projects and software-as-a-service settings with cloudbased con<sup>fi</sup>gurations.

## 8.2. Limitations

In closing, we share some thoughts about the limitations of this research. First, investigating the effect of testing time renegotiation on the value of the vendor’s private information about testing ef<sup>fi</sup>ciency is valuable in management science terms. We assume the client knows the vendor’s testing ef<sup>fi</sup>ciency and the software failure rate for each bug in our model. Testing ef<sup>fi</sup>ciency may be the vendor’s private information, yet it affects the parties’ renegotiation of testing time. Because the client can observe the performance of effort and renegotiate the initial contract ex post, the value of information for the vendor’s testing ef<sup>fi</sup>ciency may decrease. In contrast, renegotiation may amplify the effect of the vendor’s private information on reducing the client’s pro<sup>fi</sup>t, although it increases the social surplus. Thus, the value of the vendor’s private information on testing ef<sup>fi</sup>ciency may increase when the client chooses renegotiation.

The client and the vendor may engage in renegotiation for other reasons. For example, if the client has new requirements for the complexity of a customized system, or if the client knows that the vendor’s cost has changed, they may wish to renegotiate with each other. Thus, investigating the extent to which the use of renegotiation results from different types of uncertainty is worthwhile. Finally, in practice, the client can outsource a system involving more than one vendor. The effect of vendor competition on the client’s use of monitoring and renegotiation is a worthwhile direction for additional research as a result.

## Acknowledgments

The authors thank Thomas Weber, Atanu Lahiri, Deb Dey, Rajiv Dewan, Eric Clemons, and the anonymous reviewers of the Strategy, Information, Technology, Economics and Society Minitrack at the Hawaii International Conference on System Sciences (HICSS) in January 2019 for helpful comments on an earlier version of this research. The authors also thank Tong Tan, senior editor, Marius Niculescu, associate editor, and three anonymous reviewers for constructive suggestions. All errors and omissions are the sole responsibility of the authors.

## Appendix A. Glossary of Managerial Terms for the Customized Software Outsourcing Context

<table><tr><td>Term</td><td>Definition</td></tr><tr><td>Backsourcing renegotiation</td><td>The conditions of client business warrant redress from the vendor, so the former can expend less cost and bring development effort in-house (backsourcing), by adjusting the contract to allow this.</td></tr><tr><td>Client bargaining power</td><td>Bargaining power client can exert on vendor so it offers higher-quality products, better services at lower prices.</td></tr><tr><td>Development stage</td><td>Stage of the software development life cycle in which design and coding occur.</td></tr><tr><td>First-best solution</td><td>Contract solution that can be achieved if details of the client&#x27;s required system complexity and vendor&#x27;s capabilities are known to both sides.</td></tr><tr><td>Fixed-price contract</td><td>Software development contracts that consist of a predetermined payment for development, testing and maintenance services from the vendor.</td></tr><tr><td>Hold-up problem</td><td>Vendor perceives the risk of expropriation of its investment benefits from its software by the client when contract renegotiation occurs, and vice versa.</td></tr><tr><td>Incentive compatibility</td><td>Client and the vendor are both able to obtain the best outcomes when they act according to their preferences.</td></tr><tr><td>Maintenance</td><td>The purpose of the last stage is to modify the software product after delivery to correct bugs, and to improve performance or other attributes.</td></tr><tr><td>Monitoring</td><td>Used to gauge how well the cost involved in software development is in step with the budgetary constraints of the client under different types of contracts. It also is the process of inspecting and reimbursing the service vendor&#x27;s noncontractible effort in system development.</td></tr><tr><td>Opportunistic renegotiation</td><td>Renegotiation between a client and a vendor when one is weakened by some events in its business, making it susceptible to negotiation pressure and more adverse contract terms.</td></tr><tr><td>Pre-development incentive</td><td>An incentive for the vendor when the client decides on the monitoring policy prior to when the vendor begins making development effort.</td></tr><tr><td>Post-development incentive</td><td>An incentive for the vendor, created when the client and vendor engage in post-development renegotiation, affecting the value exchange they settled on when the initial contract was signed.</td></tr><tr><td>Renegotiation</td><td>Bilateral interaction between the client and the vendor, in which the client attempts to mitigate the loss of surplus from uncertainty about system completion and performance after development occurs.</td></tr><tr><td>Renegotiation-proof</td><td>Describes a software contract is not subject to renegotiation after it is agreed upon by the client and the vendor because the costs for changing terms will be too high for either party to bear.</td></tr><tr><td>Renegotiation surplus</td><td>Value that can be split between a client and its vendor, when the two parties renegotiate a contract.</td></tr><tr><td>Software bugs</td><td>An error, flaw, failure, or fault in a computer program or system that causes it to violate at least one of its functional or nonfunctional requirements.</td></tr><tr><td>System complexity</td><td>What the client requires from a system&#x27;s complexity to address its managerial and operational uses, including the size of codebase, the number of modules and interfaces, and the extent of functionality.</td></tr><tr><td>Testing</td><td>First part of the testing and maintenance stage, whose purpose is to detect software failures that arise due to coding bugs. Because testing never reveals all the problems that are present, it is typically undertaken based on hypotheses about why failures may occur, against a testing mechanism, to detect the bug.</td></tr><tr><td>Time-and materials contract</td><td>Software development contracts that consist of an extra fee beyond the payment for services obtained, based on the vendor&#x27;s effort.</td></tr><tr><td>Uncertainty-resolution</td><td>An effect that arises from having the client and the vendor renegotiate their contract terms, such that the client will resolve some uncertainties it faces about the vendor&#x27;s development effort that is observed.</td></tr><tr><td>Vendor bargaining power</td><td>Pressure the vendor can bring to bear on a client by upping prices, adjusting software quality, and controlling availability and delivery times, by leveraging its competitive position.</td></tr></table>

## Appendix B. How Software Reliability Growth Models Represent Bugs at Time t via N t

The G-O model (Goel and Okumoto 1979) is the most commonly used model among the software reliability growth mod els (SRGMs). Two types use stochastic SRGMs and deterministic

SRGMs, as shown in Table B.1. The difference between them is the assumption about N t , the cumulative number of software bugs detected in time interval 0, t . In stochastic SRGMs, N t is a random variable, while in deterministic SRGMs, N t is based on curves with speci<sup>fi</sup>c functional forms.

Table B.1. Deterministic and Stochastic Software Growth and Reliability Models

<table><tr><td>Type</td><td colspan="2">SGRM Name</td><td>N(t)</td><td>Comments</td></tr><tr><td rowspan="8">Stochastic SRGMs</td><td rowspan="7">Nonhomogeneous Poisson process (NHPP)</td><td>Exponential (G-O model)</td><td> $N(t) = a(1 - e^{-bt})$ </td><td>Software failure occurs with a constant bug-detection rate at an arbitrary time</td></tr><tr><td>Modified exponential</td><td> $N(t) = a\sum_{i=1}^{2}p_i(1 - e^{-b_i t})$ </td><td>Bug-detection difficulty during testing is considered</td></tr><tr><td>Delayed S-shaped</td><td> $N(t) = a[1 - (1 + bt)e^{-bt}]$ </td><td>Bug-detection: failure-detection, bug-isolation process</td></tr><tr><td>Inflection S-shaped</td><td> $N(t) = \frac{a(1 - e^{-bt})}{(1 + ce^{-bt})}$ </td><td>Failure occurs with mutually dependent detected bugs</td></tr><tr><td>Testing effort dependent</td><td> $N(T) = a[1 - e^{-rW(t)}]$  $(W(t) = \alpha(1 - e^{-\beta t^n}))$ </td><td>Time-dependent behavior of testing effort and cumulative detected bugs both considered</td></tr><tr><td>Testing domain dependent</td><td> $N(t) = a\left[1 - \frac{1}{v - b}(ve^{-bt} - be^{-vt})\right]$ </td><td>Focus: software functions are influenced by past test cases</td></tr><tr><td>Log Poisson execution time</td><td> $N(t) = \frac{1}{\theta}\ln(\lambda_0\theta t + 1)$ </td><td>Exponentially decreasing failure model with cumulative bugs</td></tr><tr><td>Markovian software reliability model (MSRM)</td><td></td><td>Uses a counting process,  $N(t) \geq 0$ , with a random variable for time-interval,  $S_{i,n}(i \leq n)$ , distributed as  $G_{i,n}(t)$  for  $S_{i,n}$ .</td><td>Failure time interval between events is exponentially distributed</td></tr><tr><td rowspan="2">Deterministic SRGMs</td><td>Logistic curve model</td><td></td><td> $N(t) = \frac{a}{1 + me^{-\alpha t}}$ </td><td>Regression models</td></tr><tr><td>Gompertz curve model</td><td></td><td> $N(t) = a\beta^{(\alpha^t)}$ </td><td></td></tr></table>

## Appendix C. Optimal Decisions in the FBN, FBR, FPN, FPR, TMN, and TMR Cases

Table C.1. Optimal Decisions for First-Best Solution

<table><tr><td>Case</td><td>Region</td><td>Initial testing time</td><td>Effort level</td></tr><tr><td rowspan="2">FBN</td><td> $0 < \Upsilon < \Upsilon_{1}$ </td><td> $\frac{1}{\lambda} \ln \frac{(\delta + \lambda b) \cdot (\Upsilon B(c) - e_{H}^{\beta})}{\Upsilon + K(c)}$ </td><td> $e_{H}$ </td></tr><tr><td> $\Upsilon \geq \Upsilon_{1}$ </td><td> $\frac{1}{\lambda} \ln \frac{(\delta + \lambda b) \cdot (\Upsilon B(c) - e_{L}^{\beta})}{\Upsilon + K(c)}$ </td><td> $e_{L}$ </td></tr><tr><td rowspan="2">FBR</td><td> $0 < \Upsilon < \Upsilon_{2}$ </td><td> $[0,T)$ </td><td> $e_{H}$ </td></tr><tr><td> $\Upsilon \geq \Upsilon_{2}$ </td><td> $[0,T)$ </td><td> $e_{L}$ </td></tr></table>

Note. Detailed expositions of $\boldsymbol { { \cal Y } } _ { 1 }$ and $\boldsymbol { \mathcal { Y } } _ { 2 } \left( \boldsymbol { \mathcal { Y } } _ { 1 } < \boldsymbol { \mathcal { Y } } _ { 2 } \right)$ are available (see online appendix).

Table C.2. Optimal Decisions for Fixed-Price Contract

<table><tr><td>Case</td><td></td><td>Region</td><td>Initial testing time</td><td>Effort level</td></tr><tr><td rowspan="2">FPN</td><td></td><td> $0 < \Upsilon < \Upsilon_3$ </td><td> $\frac{1}{\lambda} \ln \frac{\lambda b \cdot (\Upsilon B(c) - e_H^\beta)}{K(c)}$ </td><td> $e_H$ </td></tr><tr><td></td><td> $\Upsilon \geq \Upsilon_3$ </td><td> $\frac{1}{\lambda} \ln \frac{\lambda b \cdot (\Upsilon B(c) - e_L^\beta)}{K(c)}$ </td><td> $e_L$ </td></tr><tr><td rowspan="4">FPR</td><td> $0 < \alpha < \hat{\alpha}$ </td><td> $0 < \Upsilon < \Upsilon_4$ </td><td> $\frac{1}{\lambda} \ln \frac{[(1-\alpha) \cdot \lambda b - \alpha \delta] \cdot (\Upsilon B(c) - e_H^\beta)}{(1-\alpha) \cdot K(c) - \alpha \Upsilon}$ </td><td> $e_H$ </td></tr><tr><td></td><td> $\Upsilon \geq \Upsilon_4$ </td><td> $\frac{1}{\lambda} \ln \frac{[(1-\alpha) \cdot \lambda b - \alpha \delta] \cdot (\Upsilon B(c) - e_L^\beta)}{(1-\alpha) \cdot K(c) - \alpha \Upsilon}$ </td><td> $e_L$ </td></tr><tr><td> $\hat{\alpha} \leq \alpha < 1$ </td><td> $0 < \Upsilon < \Upsilon_5$ </td><td>0</td><td> $e_H$ </td></tr><tr><td></td><td> $\Upsilon \geq \Upsilon_5$ </td><td>0</td><td> $e_L$ </td></tr></table>

Note. Detailed expositions of αˆ , $\mathcal { r } _ { 3 } , \mathcal { r } _ { 4 } ,$ and ${ { T } _ { 5 } }$ for $\mathcal { T } _ { 3 } < \operatorname* { m i n } \{ \mathcal { T } _ { 4 } , \mathcal { T } _ { 5 } \}$ are available (see online appendix).

Table C.3. Optimal Decisions for Time-and-Materials Contract

<table><tr><td>Case</td><td colspan="2">Region</td><td>Initial testing time</td><td>Effort level</td><td>Monitoring policy</td></tr><tr><td rowspan="3">TMN</td><td colspan="2"> $0 < \Upsilon < \Upsilon_{3}$ </td><td> $\frac{1}{\lambda} \ln \frac{\lambda b \cdot (\Upsilon B(c) - e_{H}^{\beta})}{K(c)}$ </td><td> $e_{H}$ </td><td>0</td></tr><tr><td colspan="2"> $\Upsilon_{3} \leq \Upsilon < \Upsilon_{6}$ </td><td> $\frac{1}{\lambda} \ln \frac{\lambda b \cdot (\Upsilon B(c) - e_{H}^{\beta})}{K(c)}$ </td><td> $e_{H}$ </td><td> $\min\left\{\frac{r_{1}}{s}, 1\right\}$ </td></tr><tr><td colspan="2"> $\Upsilon \geq \Upsilon_{6}$ </td><td> $\frac{1}{\lambda} \ln \frac{\lambda b \cdot (\Upsilon B(c) - e_{L}^{\beta})}{K(c)}$ </td><td> $e_{L}$ </td><td>0</td></tr><tr><td rowspan="6">TMR</td><td rowspan="3"> $0 < \alpha < \hat{\alpha}$ </td><td> $0 < \Upsilon < \Upsilon_{4}$ </td><td> $\frac{1}{\lambda} \ln \frac{[(1-\alpha) \cdot \lambda b - \alpha \delta] \cdot (\Upsilon B(c) - e_{H}^{\beta})}{(1-\alpha) \cdot K(c) - \alpha \Upsilon}$ </td><td> $e_{H}$ </td><td>0</td></tr><tr><td> $\Upsilon_{4} \leq \Upsilon < \Upsilon_{7}$ </td><td> $\frac{1}{\lambda} \ln \frac{[(1-\alpha) \cdot \lambda b - \alpha \delta] \cdot (\Upsilon B(c) - e_{H}^{\beta})}{(1-\alpha) \cdot K(c) - \alpha \Upsilon}$ </td><td> $e_{H}$ </td><td> $\min\left\{\frac{r_{2}}{s}, 1\right\}$ </td></tr><tr><td> $\Upsilon \geq \Upsilon_{7}$ </td><td> $\frac{1}{\lambda} \ln \frac{[(1-\alpha) \cdot \lambda b - \alpha \delta] \cdot (\Upsilon B(c) - e_{L}^{\beta})}{(1-\alpha) \cdot K(c) - \alpha \Upsilon}$ </td><td> $e_{L}$ </td><td>0</td></tr><tr><td rowspan="3"> $\hat{\alpha} \leq \alpha < 1$ </td><td> $0 < \Upsilon < \Upsilon_{5}$ </td><td>0</td><td> $e_{H}$ </td><td>0</td></tr><tr><td> $\Upsilon_{5} \leq \Upsilon < \Upsilon_{8}$ </td><td>0</td><td> $e_{H}$ </td><td> $\min\left\{\frac{r_{3}}{s}, 1\right\}$ </td></tr><tr><td> $\Upsilon \geq \Upsilon_{8}$ </td><td>0</td><td> $e_{L}$ </td><td>0</td></tr></table>

Note. Detailed expositions of $\Gamma _ { 6 } ,$ $\boldsymbol { { \cal Y } } _ { 7 } ,$ $\boldsymbol { \mathcal { T } } _ { 8 } , \boldsymbol { r } _ { 1 } , \boldsymbol { r } _ { 2 } ,$ and r<sub>3</sub> are available (see online appendix).

## Endnotes

<sup>1</sup> The analysis and findings presented in KPMG’s report are based on data from IDC’s contract database (www.idc.com).

2 The business press discusses other contract types in addition to the two main contracts. One is a target-cost contract, which is reimbursable when the scope of the project is relatively uncertain, and the exact costs are not easily estimated when the contract is signed (Grela and Jaworski 2020). The client must be willing to bear the risk associ ated with the cost uncertainty and any changes in project scope. An other is a capped-budget accelerated-bonus contract (Baird 2016). This is a fixed-price contract with an embedded bonus for the vendor to achieve additional payback that is beneficial for both sides, although completion may be ahead of schedule or somewhat below the targeted cost. Finally, a dedicated-team contract calls for staff members of the outsourcing vendor to join and collaborate with a client’s staff, which manages the overall process. This is seen in complex projects, and when new software methods are being brought into a firm.

3 The essential difference between a fixed-price contract and a timeand-materials contract is whether to monitor the vendor’s effort. In other words, a time-and-materials contract is a more general contract because the client needs to decide on the monitoring level. If it is zero, then a time-and-material contract will degenerate into a fixed-price contract, which is a corner-point solution of the more general time-and-materials contract.

We acknowledge Thomas Weber, who encouraged us to think of contract types as corner-points across a spectrum of possible solutions in view of information asymmetry and uncertainty. The suggestion was to derive the types of contracts that either do or could exist under different market circumstances. This idea is interesting, but we determined it would be more practical, in light of industry practices, to understand what we observe in industry in greater depth. Thus, we identified industries, settings, and firms to motivate our choices through examples. The wider-spectrum approach is left for future research.

<sup>5</sup> In general, the client initiates renegotiation by sharing the renegotiation surplus with the vendor (Flinders 2012, de Novoa 2015, Saad 2017). For example, in the software outsourcing contract between the British Columbia, Canada Ministry of Health and IBM, the Ministry expected to pay US\$16.2 million for IBM’s implementation services at the beginning, but after renegotiation, the payment rose to US\$73.5 million for a much greater amount of work (Auditor General of British Columbia 2015).

<sup>6</sup> The definition of client bargaining power (Porter 1979) is the power a client can exert on a vendor so the latter will offer higher quality products and better services at lower prices. Similarly, vendor bargain ing power is the pressure a vendor can create on a client by upping prices, and adjusting quality, availability, and delivery times. Bargaining power arises in outsourcing and other contracting when an established vendor’s risk for earning revenue is less than the risk a client would face if it were to lose the vendor as a partner (de Fontenay and Gans 2008). When the vendor offers access to essential assets for the client to create value in its business (Han et al. 2008): a classic example in the economics of property rights (Hart and Moore 1990). When the client’s contract is small, the vendor has many clients to spread risk. When the client is large relative to the vendor, it may have a natural advantage in bargaining power. So, the vendor must rely on a contract to drive revenue, especially new vendors with fewer clients.

<sup>7</sup> Complementarity means the simultaneous use of the solutions strengthens the benefits of one; substitution, in contrast, is the simultaneous use of the solutions weakens their joint benefits (Tiwana 2010).

<sup>8</sup> It is based on standard assumptions. All bugs in a piece of software are typically independent for any failure detection procedure. The likelihood of the count of future bugs detected is a function of the number of current and past bugs. Those that get detected are assumed to be fixed before the next testing event. When a software error occurs, an effort is made to fix the bug, so no new errors like it will occur.

<sup>9</sup> First-best refers to the best the principal can do to achieve both optimal allocative and distributive efficiency, if she knows the agents preferences over labor and income and the incentive compatibility is not imposed (Bolton and Dewatripont 2005).

<sup>10</sup> The expected number of bugs, $N _ { C S } ( e ) ,$ , of the system, and the remainder after testing $\tilde { N } _ { C S } ( e , t )$ and maintenance $\tilde { N } _ { C S } ( e , t )$ are assumed to be common knowledge. The IS literature has widely adopted this reliability modeling (Yamada 2014). In practice, experienced developers can estimate the bugs via source lines of code (SLOC) (Mayer 2012), and repository objects used.

<sup>11</sup> We assume that system lifetime $\begin{array} { c } { { T > { \frac { 1 } { \lambda } } l n \Big ( { \frac { \lambda b N _ { C S } ( e ) } { K ( c ) } } } \Big ) } \end{array}$ to ensure the optimal testing time has interior solutions.

<sup>12</sup> The online appendix assesses the assumptions for fixed-price and time-and-materials contracts with machine learning bug detection.

<sup>13</sup> IBM estimates a bug costs US\$1,500 to fix when testing but US\$10,000 in maintenance (McPeak 2017).

<sup>14</sup> The term is the Vendor’s cost saving for each bug detection, and represents testing cost per unit time.

<sup>15</sup> According to Equations (5) and (7), we have $\begin{array} { r } { \bigg ( \frac { \partial ( U ( e , t ) - T C ( e , t ) ) } { \partial t } \bigg ) = } \end{array}$ $- ( K ( c ) + \mathcal { T } ) + ( \delta + \lambda b ) N _ { C S } ( e ) \cdot \exp ( - \lambda t )$ . On the cost side, $( K ( c ) + { \mathit { \Sigma } } ^ { \prime } )$ represents the marginal cost of testing. On the benefit side, δ $\lambda \bar { b } ) N _ { C S } ( e )$ represents the marginal benefit of testing because $\lambda N _ { C S } ( e )$ is the expected bug detection rate at time 0, and $\begin{array} { r } { \left( \frac { \delta } { \lambda } + b \right) } \end{array}$ is each bug detection-driven cost saving (Jiang et al. 2012).

<sup>16</sup> The prevalence of standardized tools, platforms, and metrics has made the development process quite mature (Synodinos 2012, Vollmer 2020, Wohlmuth 2020), which has reduced the barriers to market entry (Chang 2012). As a result, in the software outsourcing market, a large number of global vendors have been competing fiercely with many established firms for software outsourcing contracts (McFarlan and Delacey 2004) and power related to service pricing usually rests with the Clients (Dey et al. 2010, Roels et al. 2010, Bhattacharya et al. 2014, Cezar et al. 2014).

<sup>17</sup> Software development is complex and estimating the Vendor’s effort based on bugs after development is hard. For example, the Vendor’s development ideas may come from iterative refinement, but the Client only observes the final outcome (Dermdaly 2009).

<sup>18</sup> We also investigate the case in which the Client and the Vendor split the renegotiation cost based on their respective bargaining power, 1 α and α, and our main results still hold. Our analysis is included in the online appendix.

<sup>19</sup> The penalty for Vendor misreporting, $\phi s \cdot ( \hat { e } - e ) ^ { + }$ , is its reputation loss and future business loss costs, but this does not affect Client profit because the latter will not obtain this result in practice.

<sup>20</sup> Following the earlier example, the Kansas Department of Health and Environment renegotiated with Accenture, whereas the State of Michigan declined to do so with HP.

## References

Alto P (2017) D-Wave 2000Q system to be installed at quantum arti <sup>fi</sup>cial intelligence laboratory run by Google, NASA, and Universi ties Space Research Association. Accessed March 12, 2021, https:// www.dwavesys.com/press-releases/d-wave-2000q-systembe-installed-quantum-arti<sup>fi</sup>cial-intelligence-lab-run-google-nasa.

Anand KS, Goyal M (2019) Ethics, bounded rationality, and IP sharing in IT outsourcing. Management Sci. 65(11):5252–5267.

Aron R, Clemons EK, Reddi S (2005) Just right outsourcing: Under standing and managing risk. J. Management Inform. Systems 22 (2):37–55.

Auditor General of British Columbia (2015) An audit of the Panorama public health system. Accessed March 12, 2021, https:// www.bcauditor.com/sites/default/<sup>fi</sup>les/publications/reports/ OAGBC PanoramaReport FINALpdf

August T, Niculescu MF (2013) The in<sup>fl</sup>uence of software process maturity and customer error reporting on software release and pricing. Management Sci. 59(12):2702–2726.

Baird B (2016) Four types of custom software development contracts. Accessed March 12, 2021, https://www.linkedin.com pulse/4-types-custom-software-development-contracts-bob-baird.

Bajari P, Tadelis S (2001) Incentives vs. transaction costs: A theory of procurement contracts. RAND J. Econom. 32(3):387–407.

Barkholz D (2010) HP contract opens new round of IT outsourcing at GM. Auto. News (July 26), https://www.autonews.com/ article/20100726/OEM01/307269953/hp-contract-opens-newround-of-it-outsourcing-at-gm.

Benaroch M, Dai Q, Kauffman RJ (2010) Should we go our own way? Analyzing backsourcing <sup>fl</sup>exibility in IT service outsourcing contracts. J. Management Inform. Systems 26(4):317–358.

Benaroch M, Lichtenstein Y, Fink L (2016) Contract design choices and the balance of ex-ante and ex-post transaction costs in soft ware development outsourcing. MIS Quart. 40(1):57–82.

Bhattacharya S, Gupta A, Hasija S (2014) Joint product improvement by client and customer support center: The role of gain-share contracts in coordination. Inform. Systems Res. 25(1):137–151.

Bhattacharya S, Gupta A, Hasija S (2018) Single-sourcing vs. multi sourcing: The roles of output veri<sup>fi</sup>ability of task modularity MIS Quart. 42(4):1171–1186

Bolton P, Dewatripont M (2005) Contract Theory (MIT Press, Cam bridge, MA)

Bort J (2015) Michigan is suing HP because it says the company hasn’t <sup>fi</sup>nished a project after 10 years of work. Business Insider (September 21). Accessed March 12, 2021, https://www. businessinsider.com.au/michigan-sues-hp-for-decade-longproject-2015-9.

Cezar A, Cavusoglu H, Raghunathan S (2014) Outsourcing information security: Contracting issues and security implication. Man agement Sci. 60(3):638–657.

Chang A (2012) Microsoft lowers barriers to entry, waits for developers to arrive. Wired.com (November 15). Accessed March 12, 2021, https://www.wired.com/2012/11/microsoft-lowers-barriersto-entry-waits-for-developers-to-arrive/.

Chang YB, Gurbaxani V, Ravindran K (2017) Information technology outsourcing: Asset transfer and the role of contract. MIS Quart. 41(3):959–973.

Che YK, Hausch DB (1999) Cooperative investments and the value of contracting. Amer. Econom. Rev. 89(1):125–147.

Culclasure D, Neff T (2016) Better to best. AL&T Mag. (June 27). Accessed March 12, 2021, https://api.army.mil/e2/c/downloads/ 430914.pdf.

de Fontenay CC, Gans J (2008) A bargaining perspective on strategic outsourcing and supply competition. Strategic Management J. 29(8):819–839.

de Novoa CD (2015) Renegotiation outsourcing contracts: What works and why. Accessed March 12, 2021, https://nearshore americas.com/successfully-renegotiate-outsourcing-contracts/.

Dermdaly (2009) The problem with "revenue share." Accessed March 12, 2021, https://tapadoo.com/the-problem-with-revenue -share/.

Dey D, Fan M, Zhang CL (2010) Design and analysis of contracts for software outsourcing. Inform. Systems Res. 21(1):93–114.

Evenstad L (2016) Scottish police and Accenture terminate IT systems contract. Comp. Weekly (July 4). Accessed March 12, 2021, https://www.computerweekly.com/news/450299611/Scottishpolice-terminates-IT-systems-contract-with-Accenture.

Fitoussi D, Gurbaxani V (2012) IT outsourcing contracts and perfor mance measurement. Inform. Systems Res. 23(1):129–143

Flinders K (2012) Renegotiation outsourcing contracts to <sup>fi</sup>t new reality. Comp. Weekly (October 22). Accessed March 12, 2021, https:/ www.computerweekly.com/news/2240168932/Renegotiatingoutsourcing-contracts-to-<sup>fi</sup>t-new-reality.

Fujitsu (2004) Whitbread sign <sup>fi</sup>ve-year network contract with Fujit su. Accessed March 12, 2021, https://www.fujitsu.com/ie/ news/pr/2004/fs-20040608-01.btml

Fujitsu (2009) Whitbread PLC renews network contract with Fujitsu Accessed March 12, 2021, https://www.fujitsu.com/uk/news/ pr/fs-20090303-review.html.

Gefen D, Wyss S, Lichtenstein Y (2008) Business familiarity as risk mitigation in software development outsourcing contracts. MIS Quart. 32(3):531–542.

Gerstein M (2017) State, HP settle on failed \$49m computer contract. Detroit News (April 25). Accessed March 12, 2021, https://www.

detroitnews.com/story/news/local/michigan/2017/04/25/ state-hp-settle-failed-computer-contract/100909770/.

Ghoshal A, Lahiri A, Dey D (2017) Drawing a line in the sand: Commitment problem in ending software support. MIS Quart. 41(4):1227–1247.

Goel A, Okumoto K (1979) Time-dependent error-detection rate model for software reliability and other performance measures. IEEE Trans. Reliability 28(3):206–211.

Gopal A, Koka BR (2010) The role of contracts on quality and returns to quality in offshore software development outsourcing. Decision Sci. 41(3):491–516.

Gopal A, Sivaramakrishnan K (2008) On vendor preferences for contract types in offshore software projects: The case of <sup>fi</sup>xed price vs. time and materials contracts. Inform. Systems Res. 19(2): 202–220.

Grela M, Jaworski B (2020) The four most popular types of outsourcing contracts. Accessed March 12, 2021, https://www. future-processing.com/blog/the-3-most-popular-typesof-outsourcing-contracts/.

Guasch JL, Laffont JJ, Straub S (2006) Renegotiation of concession contracts: A theoretical approach. Rev. Industry Organ. 29(1-2): 55–73.

Guo L, Iyer G (2013) Multilateral bargaining and downstream com petition. Marketing Sci. 32(3):411–430.

Had<sup>fi</sup>eld W (2005) Whitbread integrates hotel systems for £2.25m. Comp. Weekly (November 15). Accessed March 12, 2021, https:// www.computerweekly.com/news/2240075811/Whitbreadintegrates-hotel-systems-for-225m.

Han K, Kauffman RJ, Nault B (2008) Relative importance, speci<sup>fi</sup>c investment and ownership in interorganizational systems. In form. Tech. Management 9(3):181–200.

Harris D (2015) Quantum computing research carries on at Google and NASA. Fortune (September 28), https://fortune.com/2015/ 09/28/google-nasa-quantum-computer/.

Hart OD, Moore J (1990) Property rights and the nature of the <sup>fi</sup>rm. J. Political Econom. 98(6):1119–1158.

Hoover M (2016) SAP wins \$17.5 million Army contract to support ERP, <sup>fi</sup>nancial programs. Accessed March 12, 2021, https:// washingtontechnology.com/articles/2016/03/22/sap-armycontract.aspx.

Hu Q, Plant RT, Hertz DB (1998) Software cost estimation using economic production models. J. Management Inform. Systems 15 1):143–163.

James S (2017) Seven reasons why you should renegotiation your outsourcing relationships. Accessed March 12, 2021, https:// www.bestpracticegroup.com/renegotiate-outsourcing-relationship/.

Ji Y, Kumar S, Mookerjee VS, Sethi SP, Yeh D (2011) Optimal enhancement and lifetime of software systems: A control theoretic analysis. Production Oper. Management 20(6):889–904.

Jiang Z, Sarkar S, Jacob VS (2012) Post-release testing and software release policy for enterprise-level systems. Inform. Systems Res. 23(3-part-1):635–657.

Jiang Z, Scheibe KP, Nilakanta S, Qu X (2017) Economics of public beta testing. Decision Sci. 48(1):150–175.

Knapp A (2013) NASA and Google partner to work with a D-Wave quantum computer. Forbes (May 16), https://www.forbes.com/ sites/alexknapp/2013/05/16/nasa-and-google-partner-to-purchasea-d-wave-quantum-computer/?sh=3d0cc8de67da

Knoll L (2016) Five reasons to love time & material and avoid the <sup>fi</sup>xed-price model. Accessed March 12, 2021, https://brainhub. eu/blog/5-reasons-to-love-time-materials-avoid-<sup>fi</sup>xed-costmodel/.

Korotia Y (2017) Time-and-materials s fixed price: Which to choose for your project? Accessed March 12, 2021, https://medium. com/@Eugeniya/time-and-materials-vs-<sup>fi</sup>xed-price-which-tochoose-for-your-project-11dc6adc758b.

KPMG (2018) Global IT-BPO outsourcing deals analysis: Annual analysis for 2017. Accessed March 12, 2021, https://assets. kpmg/content/dam/kpmg/in/pdf/2018/05/KPMG-Deal Tracker-2017.pdf.

Krishnan MS, Mukhopadhyay T, Kriebel CH (2004) A decision mode for software maintenance. Inform. Systems Res. 15(4):396–412.

Li S, Cheng HK, Duan Y, Yang YC (2017) A study of enterprise software licensing models. J. Management Inform. Systems 34(1): 177–205.

Liang C, Hong Y, Gu B (2016a) Effects of IT-enabled monitoring systems in online labor markets. Proc. 37th Internat. Conf. Inform. Systems (Association for Information Systems, Atlanta), https:// aisel.aisnet.org/icis2016/Economics/Presentations/18/.

Liang HG, Wang JJ, Xue YJ, Cui XC (2016b) IT outsourcing research from 1992 to 2013: A literature review based on main path analysis. Inform. Management 53(2):227–251.

Mani D, Barua A, Whinston AB (2012) An empirical analysis of the contractual and information structures of business process outsourcing relationships. Inform. Systems Res. 23(3-part-1):618–634.

Marso A (2016) Behind the backlog: The problem-plagued rollout of KEES. Accessed March 12, 2021, https://www.khi.org/news/ article/behind-the-backlog-of-kees-applications.

Maskin E, Moore J (1999) Implementation and renegotiation. Rev. Econom. Stud. 66(1):39–56.

Mathur N (2016) Vodafone India renews IT deal with IBM for <sup>fi</sup>ve years. Accessed March 12, 2021, https://www.livemint.com/ Industry/uxvj1Tn5sK5zT9kG7QggdO/Vodafone-India-signs-IT-deal-with-IBM-for-<sup>fi</sup>ve-years.html.

Mayer D (2012) Ratio of bugs per line of code. Accessed March 12, 2021, https://www.mayerdan.com/ruby/2012/11/11/bugs-per -line-of-code-ratio.

McFarlan FW, Delacey BJ (2004) Outsourcing IT: The Global Landscape in 2004. Case Study 9-304-104 (Harvard Business School, Boston, MA).

McPeak A (2017) What’s the true cost of a software bug? Accessed March 12, 2021, https://crossbrowsertesting.com/blog/develop ment/software-bug-cost/.

Menon NG (2018) What are the different types of software development contracts? Accessed March 12, 2021, https://www. cognitiveclouds.com/insights/what-are-the-different-types of-software-development-contracts/.

Mezak S (2018) What technology risks can cause software outsourcing to fail? CIO (Framingham MA). Accessed March 12, 2021, https://www.cio.com/article/3269259/what-technology-riskscan-cause-software-outsourcing-to-fail.html

Moreno H (2017) How IT service management delivers value to the digital enterprise. Forbes (March 16), https://www.forbes.com/ sites/forbesinsights/2017/03/16/how-it-service-managementdelivers-value-to-the-digital-enterprise/?sh=53b76f34732e.

Ohba M, Chou XM (1989) Does imperfect debugging affect software reliability growth? Proc. 11th Internat. Conf. Software Engrg. (ACM Press, New York), 237–244.

Parker G, Van Alstyne M (2018) Innovation, openness, and platform control. Management Sci. 64(7):3015–3032.

Pham H, Zhang X (1999) Software release policies with gain in reli ability justifying the costs. Ann. Software Engrg. 8(1):147–166

Porter ME (1979) How competitive forces shape strategy. Harvard Bus. Rev. 57(2):137–145.

ReportLinker (2020) Global outsourcing market, 2020-2024 (In<sup>fi</sup>niti Res. Ltd). Accessed March 12, 2021, https://www.reportlinker. com/p02673147/Global-IT-Outsourcing-Market-in-Capital-Markets.html.

Richmond WB, Seidmann A, Whinston AB (1992) Incomplete contracting issues in information systems development outsourc ing. Decision Support Systems 8:459–477.

Roels G, Karmarkar U, Carr S (2010) Contracting for collaborative services. Management Sci. 56(5):849–863.

Roy P, Mahapatra GS, Dey KN (2015) Neuro-genetic approach on logistic model-based software reliability prediction. Expert Systems Appl. 42(10):4709–4718.

Saad A (2017) IT outsourcing contracts renegotiation: When? Why? How? Accessed March 12, 2021, https://www.tiespecialistas. com.br/it-outsourcing-contracts-renegotiation-when-why-how/.

Savitz E (2013) Why some U.S. companies are giving up on outsourcing. Forbes (January 16), https://www.forbes.com/sites/ ciocentral/2013/01/16/why-some-u-s-companies-aregiving-up-on-outsourcing/?sh=1af9592065af.

Shared Services and Outsourcing Network (2012) Top ten tips for a smooth contract renegotiation. Accessed March 12, 2021, https://www.ssonetwork.com/business-process-outsourcing/ articles/top-ten-tips-for-a-smooth-contract-renegotiation.

Susarla A (2012) Contractual <sup>fl</sup>exibility, rent seeking, and renegotiation design: An empirical analysis of information technology outsourcing contracts. Management Sci. 58(7):1388–1407.

Synodinos D (2012) What are the most important and mature cross platform mobile tools? Accessed March 12, 2021, https://www. infoq.com/research/cross-platform-mobile-tools/

Tiwana A (2010) Systems development ambidexterity: Explaining the complementary and substitutive roles of formal and infor mal controls. J. Management Inform. Systems 27(2):87–126.

Vollmer P (2020) Shift your DevOps into high gear: Key models to consider. Accessed March 12, 2021, https://techbeacon.com/ devops/shift-your-devops-high-gear-key-models-consider.

Whang S (1995) Market provision of custom software: Learning ef fects and low balling. Management Sci. 41(8):1343–1352.

Wohlmuth M (2020) State of software development in 2020. Accessed March 12, 2021, https://codingsans.com/state-of -software-development-2020.

Yamada S (2014) Software Reliability Modeling Fundamentals and Appli cations (Springer, Cham, Switzerland).

C<sub>opy</sub>ri<sub>g</sub>ht 202 1 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>express wr</sub>itt<sub>en perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
