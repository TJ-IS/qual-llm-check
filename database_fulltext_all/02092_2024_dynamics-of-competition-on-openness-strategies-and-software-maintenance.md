---
otero_id: 2092
otero_key: "XAVBM799"
title: "Dynamics of Competition on Openness Strategies and Software Maintenance"
authors: "Rakesh R. Mallipeddi; Emre M. Demirezen; Subodha Kumar; Ram D. Gopal"
year: "2024"
journal: "MIS Quarterly"
doi: "10.25300/misq/2023/17063"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DYNAMICS OF COMPETITION ON OPENNESS STRATEGIES AND SOFTWARE MAINTENANCE<sup>1</sup>

Rakesh R. Mallipeddi Fisher College of Business, The Ohio State University, Columbus, OH, U.S.A. {Mallipeddi.1@osu.edu}

Emre M. Demirezen Warrington College of Business, University of Florida, Gainesville, FL, U.S.A. {Emre.Demirezen@warrington.ufl.edu}

Subodha Kumar Fox School of Business, Temple University Philadelphia, PA, U.S.A. {Subodha@temple.edu}

Ram D. Gopal Warwick Business School, The University of Warwick Coventry, U.K. {Ram.Gopal@wbs.ac.uk}

Software firms are increasingly adopting an open source strategy, allowing them to leverage the effort exerted by the open source community toward improving software quality. In addition to embracing a proprietary or fully open source strategy, several firms choose a partial openness strategy wherein only certain parts of the code are open source while the rest is proprietary. Specifically, when adopting a partial openness strategy, a firm may choose to make the core software code open source while keeping the extension software code proprietary or keep the core proprietary and make the extension open source. When making decisions related to different openness strategies, firms need to take into account the level of effort they are exerting toward the improvement of the quality of software, the level of engagement of the open source community, and pricing. Hence, the decisions related to a firm’s openness strategy are not straightforward. While this is an important question for many firms, it has not been analyzed in the literature. In this research, we attempt to fill this important gap by analyzing different openness strategies in the context of resource allocation for fixing defects. Specifically, using a game-theoretic model, we explore when a firm should make its software fully open source or partially open source and when it should keep it proprietary. Our results show that when the baseline demand for the firm increases with the extent of openness, the firm should either make its software fully open or keep it proprietary and, importantly, should not rely on partial openness. Next, in scenarios where customers are highly sensitive to security risks, the demand loss to efficiency gain ratio has an important role in determining a firm’s optimal openness strategies. These findings provide important insights to firms on how to effectively plan their openness strategies and also establish a basis for future research on the topic of partial openness.

Keywords: Software openness, defects, software quality, pricing, game theory, analytical modeling

## Introduction

The open source software paradigm, which refers to the phenomenon of firms releasing their software code to the open source community (i.e., external stakeholders such as users or customers) or adopting an existing open source software code, has become a key part of software development strategies of several firms including Apple and Microsoft (Apple, 2019, Microsoft, 2020). More than 2.5 million users from 41 countries actively contribute to open source projects on GitHub, a platform that facilitates collaboration on open source projects (Octoverse, 2019).

Despite the gradual increase in the number of open source software projects, several software products, including Windows, SAS, and Adobe, still remain proprietary. Thus, an understanding of the rationale behind why firms employ different strategies related to opening up software is warranted. We attempt to shed light on this by analyzing how factors such as collaboration cost, the open source community’s effort, and competitors’ open source strategies influence a firm’s optimal openness strategies.

## Motivation

A firm’s decision to open source its software is associated with the following trade-offs. On the one hand, by opening the software, firms can leverage the skills of the open source community to achieve higher levels of efficiency in improving the quality of the software, thus reducing its costs toward quality improvement (Lerner & Tirole, 2002). The following statement ratifies this argument from the perspective of a software firm— “Apple believes that using open source methodology makes Mac OS X a more robust, secure operating system, as its core components have been subjected to the crucible of peer review for decades” (Bartlett, 2019). Subsequently, this will entice more quality-sensitive customers to join the focal firm’s software platform. On the other hand, opening the software may result in additional costs associated with collaboration between the firm’s internal resources and external resources (Lerner & Tirole, 2000; West, 2003). Furthermore, an open source strategy may lead to concerns about software reproducibility, i.e., competing firms may be able to replicate certain portions of the code (Kumar et al., 2011).

Anecdotal evidence from industry and prior literature suggest that the openness decision of a firm is not necessarily a binary decision, i.e., adopt a fully open source strategy or proprietary software strategy (Casadesus-Masanell & Llanes, 2011; Myles, 2017; Hanson, 2019). Rather, the firm may also adopt a partial openness strategy, wherein only certain parts of the software code are made open source while the rest of the code remains proprietary.<sup>2</sup> This allows the firm to exploit some of the benefits of both open and proprietary software development while limiting the detrimental effects of openness.

Within the realm of partial openness, the firm may choose to keep the “core” portion of its software code proprietary (or open source) while making the “extension” code open source. Alternatively, the firm might decide to make its core software code open source while keeping the extension code closed. With varying degrees of openness, the different levels of effectiveness of the open source community’s contributions in fixing defects need to be accounted for. In particular, when the open source community has access to more crucial portions of the code (e.g., core software code), it might be more effective than when it only has access to the periphery (or extension) code (Arora et al., 2010). However, making large portions of the code open source could lead to higher collaboration costs between the firm and the open source community. Furthermore, the baseline demand for the software is also dependent on the degree of the firm’s openness. Specifically, opening up more crucial parts of the code may attract a larger base of users to the software platform. Thus, fully open software may attract a larger user base compared to software with only the core code open, which could in turn attract a larger base than software with only the extension code open or fully closed software (Rudin, 2019). On the contrary, opening more components of the software may be perceived to have higher security or intellectual property risks, which may, in turn, have a negative effect on demand (Casadesus-Masanell & Llanes, 2011). Thus, software with relatively fewer portions of open code might attract more users who prefer to keep their trade secrets. As detailed below, our model captures all the trade-offs among the different openness strategies discussed above.

To summarize, the openness strategies that we consider are: (1) fully open, which we refer to as Strategy O, (2) only the core code open, referred to as Strategy C, (3) only the extension code open, referred to as Strategy E, and (4) fully closed or proprietary, referred to as Strategy P. A few examples of firms employing different openness strategies include Linux and Java (Strategy O), Mac OS X (Strategy C), Stata (Strategy E), and Microsoft Windows (Strategy P) (Casadesus-Masanell & Llanes, 2011).

## Research Question and Contributions

Given the above-discussed trade-offs associated with different open source strategies, it is important for firms to understand optimal openness strategies. Hence, we seek to provide an answer to the following question: What is the optimal level of openness for firms in different market conditions? In particular, the focus of this research is to identify the conditions when a firm should employ Strategy O, C, E, or P.

Our findings reveal that in scenarios where opening up the software attracts more users to its platform, partial openness (i.e., Strategy C or E) is not an optimal strategy. In particular, in this business scenario, it may be optimal for the firm to either keep its software proprietary or pursue a fully open source strategy. On the other hand, when customers have a greater preference for the intellectual value of the software code, it may be optimal for the firms to rely on partial openness strategies, i.e., Strategy C or Strategy E in certain scenarios. In particular, the extent of openness of the software code depends on the demand loss due to openness to efficiency gains from the openness ratio. These results provide important managerial implications to firms under different market conditions and also serve as a basis for future research on firms’ openness strategies, including partial openness, which is widely prevalent. Our study’s contribution to the existing literature, which we discuss in the next section, lies in the simultaneous modeling of dynamics between the efforts of the firms and the open source community, pricing, and competition in terms of the firms’ openness strategies.

## Related Literature

Prior literature in this stream has primarily focused on the following three research themes: (1) contributions and management of the open source community, (2) effort levels of original software developers and service providers, and (3) competition between open source software and proprietary software. Regarding the first research theme, in one of the earlier works, Bonaccorsi and Rossi (2003) studied the intrinsic motivations of the open source community to improve the quality of software. They identified intrinsic utility and project challenges as key factors that motivate developers to provide free service for open source software projects. Practitioners also subscribe to this finding and suggest that developers from the open source community will have additional motivation to contribute to projects that open more critical parts of the software code (Haddad & Yehuda, 2021) and thereby increase their efficiency. Regarding the management of open source projects, Ho and Rai (2017) studied the impact of project quality on the participation of the open source community and found that coordination with software owners can lead to better outcomes. Our study builds on the findings from this research theme and incorporates the differential impact of which aspects of code are open on the efficiency of the open source community and the cost of coordinating the efforts of the open source community.

Previous literature has studied the decisions related to the effort levels of software development firms. For example, August et al. (2013) took a game-theoretic approach to understanding the impact of opening (i.e., fully open or proprietary) on the pricing and effort decisions of service providers. August et al. (2018) built on this study to explore the impact of licensing (e.g., rules regarding how much the service providers can modify the code) on the decisions of service providers. In contrast to this research theme, our focus is not on understanding the interaction between the original software developer and the service provider and its impact on pricing and effort levels. Instead, we focus on analyzing the interaction between the pricing and the effort levels of two competing software firms with differentiated products. Furthermore, in our study, we also consider scenarios in which firms partially open their software (e.g., core open or extension open).

Prior literature on the competition between open source and proprietary software has examined some of the decisions related to openness and their impact on network effects and other market-related dynamics (e.g., Haruvy et al., 2008; Casadesus-Masanell & Llanes, 2011, Huang et al., 2020). More recent papers have also studied why firms choose to open source their software products. For example, Huang et al. (2020) studied the problem from the perspective of learning costs associated with open source software. Niculescu et al. (2018) examined the problem of openness from the perspective of network effects. Perhaps, closest to our work, Casadesus-Masanell and Llanes (2011), were among the first to consider different partial openness strategies. However, they did not consider the effort of the open source community and the firm’s efforts in their model. Building on these previous studies, our study examines the effects of competition in software and market requirements on a firm’s openness strategies, pricing, and resource allocation (or optimal effort levels) decisions simultaneously. More specifically, our study takes an operational perspective by analytically examining the effects of software openness on the firm’s maintenance strategies. Furthermore, to the best of our knowledge, our study is the first to model the dynamics between openness strategies, pricing, and firms’ effort levels, which enabled us to determine the conditions when it is optimal for the firms to make their software fully open and partially open. In the next section, we introduce and discuss various components of our model and present our analytical model to examine the effects of openness on resource allocation for software maintenance and development.

![](/api/attachments/XAVBM799/fulltext/images/bc4dca5241d7799abbafaa5c365e4477e404b4d8d71a28104f8f9f3d0a27fc8a.jpg)

## Analytical Model

We considered two competing firms that offer differentiated products. For example, RedHat Linux<sup>3</sup> and Microsoft Windows are operating system software that offer differentiated products in terms of both quality and price (Ionos, 2019). We identified similar examples for other types of software as well (e.g., Stata and R). To capture such a scenario, we considered a market with two software firms (denoted by 1 and 2) with complete information that compete in price (denoted by ??) and quality (denoted by ??). The timeline for the four-stage game is as follows:

Stage 1: In the first stage, the firms simultaneously choose their open source strategy, i.e., firms choose to either keep their software proprietary (Strategy P), make it fully open source (Strategy O), open the core portion only while keeping the extension closed (Strategy C), or open the extension code while keeping the core portion closed (Strategy E).

Stage 2: After making the decision related to openness, in the second stage, the firms determine how much effort to exert toward improving the quality of their software (August et al., 2013). The effort levels of Firms 1 and 2 are denoted by $e _ { 1 }$ and $\boldsymbol { e } _ { 2 } ,$ , respectively. Effort in our context refers to labor and other resources required to develop the software product.

Stage 3: Once the decisions related to effort levels are made, both firms simultaneously determine the price of their respective software products $( p _ { 1 }$ and $p _ { 2 } )$ in the third stage. While certain open source software may be free, firms often rely on paid services offered by firms that complement the free software (August et al., 2013).<sup>4</sup> Furthermore, firms that develop open source software might license their software to other firms that provide value-added services to customers. For example, RedHat provides open source software products for free to their customers but charges a service fee for providing support (Levine, 2014). We would like to emphasize that our focus is not on the revenue models, which have been previously studied (e.g., August et al., 2013). Instead, our focus is on understanding the dynamics between market characteristics, openness strategies of the firms, pricing, and firms’ resource allocation.

Stage 4: Consumer demand is realized in the last stage after the openness strategy, effort levels, and prices are determined.

The model timeline is summarized in Figure 1. The timing consideration of our model is based on practical concerns but not analytical tractability, as the pricing and effort decisions can be solved simultaneously without added complexity. In practice, the decisions regarding the quality of software products are made before the pricing decisions are made. This approach has also been utilized in the literature (e.g., Banker et al., 1998; August et al., 2018; Huang et al., 2020).

## Cost Function

Previous literature has observed diseconomies of scale for the costs associated with efforts during the support phases of a software’s life cycle (Banker & Slaughter, 1997). This phenomenon is due to the fact that adding more resources to the project increases the complexity and training required, along with coordination issues (Xue et al., 2018); thus, the cost increases nonlinearly. Therefore, following the previous literature in this stream (e.g., August et al., 2018), we assume that the firms incur nonlinear or quadratic costs for their efforts, $c _ { 1 } e _ { 1 } ^ { 2 }$ and $c _ { 2 } e _ { 2 } ^ { 2 }$ , where $c _ { 1 }$ and $c _ { 2 }$ denote the cost multiplier for the effort exerted by Firms 1 and 2, respectively.

## Demand Function

One of our goals is to investigate the impacts of both quality levels (which are affected by the firm’s effort and the open source community’s effort) and pricing on openness decisions, as anecdotal evidence reveals that both quality and price can impact the demand for software products (Ablon et al., 2016). Since it is shown that insights from the linear model for demand with multiple inputs (e.g., quality and price) often hold for more general settings (Milgrom, 1994; Gal-Or & Ghose, 2005), and since the linear demand model has been used extensively in information systems and management science research (Banker et al., 1998), we also consider the demand function to be linear.<sup>5</sup> Thus, the demand function for the product is modeled as:

$$
q _ {i} = d _ {k i} - \alpha p _ {i} + \beta p _ {j} + \gamma x _ {i} - \lambda x _ {j}; i, j = 1, 2; i \neq j
$$

Hereafter, we refer to Firm 1 as the focal firm and its competitor as Firm 2. The parameter $d _ { k i }$ denotes the intrinsic demand for firm ?? that chooses openness strategy ??. The parameters ?? and ?? denote the market or demand responsiveness to the firm’s own price $( p _ { i } )$ and the firm’s software quality $( x _ { i } )$ , respectively. The market or demand responsiveness to competitor’s price and quality are denoted by ?? and ??, respectively. Based on the literature (e.g., Banker et al., 1998), demand sensitivity parameters of interest depend more on the focal firm than on the competitor. Therefore, we assume that $\alpha > \beta \ge 0$ and $\gamma > \lambda \ge 0$

## Quality Function

The quality of the software depends primarily on two components: (1) effort exerted by the firm’s resources, and (2) the open source community. In particular, software openness will attract the open source community to initialize or undertake quality improvement activities. The effects of software openness on the improvement in the quality of the software are well documented. Previous studies have empirically shown that defects are fixed faster when firms employ open source methodology. For example, Arora et al. (2010) used a proportional hazard model to investigate if software openness impacts patch release time. They found that patches for the vulnerabilities in open source software are released faster compared to proprietary software. Paulson et al. (2004) also found that defects are found and fixed faster in open source projects.

In order to further validate the results of Arora et al. (2010) and Paulson et al. (2004), we conducted an extensive empirical study and confirmed that defects in open source software are resolved at a faster rate than those in proprietary environments. While the details of our empirical study are provided in Appendix C, we provide a brief summary here. We collected data on vulnerabilities of both proprietary and open source software from the National Vulnerabilities Database, Common Vulnerabilities and Exposures website, and the websites of firms. The firms used in the empirical study are SUN, Apache, Apple, Google, IBM, Microsoft, Mozilla, MySQL, Oracle, PHP, and Ruby-on-Rails. The empirical results consistently revealed that the software type (i.e., proprietary vs open source) impacts the time to resolve the vulnerability—or, more specifically, if the software type is proprietary, it takes longer to resolve the defect. We also conducted several robustness checks to substantiate the findings of our empirical study.<sup>6</sup> The empirical findings support the argument made by Lerner and Tirole (2002) and West (2003) suggesting that as the open source community gains access to the more critical parts of the source code, it becomes easier for them to fix defects and increase the inherent quality of the software.

Anecdotal evidence also support the argument that the open source community can improve quality—for example, Google asserts that “more perspectives make better software” (Google, 2021). Therefore, consistent with the observations from practice and empirical findings, we modeled the quality of the product as a function of its own efforts and the effort of the open source community.

Let ?? denote firm ??’s business strategy related to the openness of its software, where $k \in O , C , E , P .$ . The quality of software of firm ?? (?? ) is modeled as $x _ { i } = e _ { i } + h _ { k i } s _ { i }$ , where $e _ { i }$ denotes the effort level that the firm exerts to improve the quality of the software and $s _ { i }$ denotes the effort exerted by the open source community (i.e., the benefit that the firm attains by opening the software). Note that $s _ { i } = 0$ if the software is proprietary, as the open source community will not have access to the firm’s software code. Our model does not assume any ordering of $s _ { i }$ based on the extent of openness. The parameter $h _ { k i }$ , where $k \in O , C , E , P$ and ?? ∈ 1,2, denotes the relative impact of open source community on the quality of firm ??’s product. Note that when the software is closed, the effectiveness is set to zero, i.e., $h _ { P i } = 0$

The results from our empirical study and previous literature (e.g., Arora et al., 2010),that quality improves when open source methodology is embraced, can be attributed to the fact that as the open source community gains access to a higher portion of the source code, it becomes easier for them to fix defects and to increase the inherent quality of the software. Thus, opening larger and more sensitive portions of the software code can induce higher efficiency of the open source community’s effort toward software quality. Therefore, we assume that the open source community will be more effective when the software is fully open compared to partially open. Similarly, based on the above discussion, the open source community will be more effective when the firm opens up the core components of its software code compared to when the firm opens up the extensions. Hence, in our model, $h _ { O i } \geq$ $h _ { C i } \geq h _ { E i } > 0$

## Objective Function

There are several sources of costs related to making the code open source, such as the management of collaboration among members of the open source community and in-house developers. With users of the open source community scattered around the globe, coordination between the internal team of the firm and the open source community is important from the firm’s perspective (Koch, 2009). For instance, a firm needs to examine every change in the source code (or every modified function) in order to make sure that the changes are meaningful and do not introduce new defects or compatibility issues. We capture this cost of opening the software as $y _ { i } s _ { i } ,$ where $y _ { i }$ denotes the relative cost of collaboration between the open source community and the firm and $s _ { i }$ denotes the efforts of the open source community. To summarize, the cost of collaboration captures various costs associated with managing the relationship between the open source community and the firm. For example, firms use GitHub to manage their open source software, and the costs of these types of resources may not increase nonlinearly. Hence, we assume that this cost is linear.<sup>7</sup>

As discussed earlier, when a firm opens up its software, it allows the external users of the software (i.e., the open source community) to learn about the firm’s software code and enables them to copy the unique features of the software, develop new features, and/or improve the security of the software (Liu et al., 2011). In such a scenario, a competing firm may also indirectly benefit from the external users’ efforts when they share the code on social networking platforms such as GitHub. Prior literature has captured knowledge sharing between software users as a positive cost spillover effect for competitors (e.g., Liu et al., 2011). Thus, we model the positive cost spillover for the competitor as $n _ { l i } s _ { j }$ , where $n _ { l i }$ is the positive cost spillover parameter from firm ?? to firm ??, which depends on the firm ??’s openness strategy (i.e., strategy ??).

Taking into account the revenue from the demand for the software, the effort costs, positive spillover costs, and the cost of the collaboration with the open source community (discussed above), we can write the objective function of the firm as: ?????? $\begin{array} { r } { \pi _ { i } = p _ { i } q _ { i } - c _ { i } e _ { i } ^ { 2 } - y _ { i } s _ { i } + n _ { l i } s _ { j } } \end{array}$ . For convenience, all parameters and variables are summarized in Table 1.

<table><tr><td colspan="2">Table 1. List of Parameters and Variables</td></tr><tr><td>Symbol</td><td>Definition</td></tr><tr><td> $\alpha$ </td><td>Market or demand sensitivity to firm’s own price</td></tr><tr><td> $\beta$ </td><td>Market or demand sensitivity to competitor’s price</td></tr><tr><td> $\gamma$ </td><td>Market or demand sensitivity to firm’s software quality</td></tr><tr><td> $\lambda$ </td><td>Market or demand sensitivity to competitor’s software quality</td></tr><tr><td> $c_i$ </td><td>Cost multiplier of firm  $i$ &#x27;s effort</td></tr><tr><td> $d_{ki}$ </td><td>Intrinsic or baseline demand of firm  $i$  under business strategy  $k$ </td></tr><tr><td> $y_i$ </td><td>Relative cost of collaboration between the open source community and firm  $i$ </td></tr><tr><td> $h_{ki}$ </td><td>Relative impact of the open source community’s effort on firm  $i$ &#x27;s product quality</td></tr><tr><td> $n_{li}$ </td><td>Positive spillover of competitor’s openness strategy,  $l$ </td></tr><tr><td> $e_i$ </td><td>Effort exerted by firm  $i$ </td></tr><tr><td> $x_i$ </td><td>Quality of firm  $i$ &#x27;s software</td></tr><tr><td> $s_i$ </td><td>Effort exerted by open source community</td></tr><tr><td> $q_i$ </td><td>Total demand for firm  $i$ &#x27;s software product</td></tr></table>

## Results

We first derived the optimal pricing decisions in Stage 3 and then obtained the firms’ effort levels in Stage 2 using backward induction. The equilibrium prices and effort levels for the focal firm (i.e., Firm 1) and the competitor (i.e., Firm 2) are presented in Appendix A. After characterizing the equilibrium effort levels and prices (in the second and third stages), we next determined the best response of firms to their competitor’s openness strategy. The firms could choose any one of the four openness strategies, i.e., fully open (O), proprietary (P), core open (C), and extension open (E). Thus, there are 16 possible equilibria as shown in Figure A1 (in the Appendix).

The adverse effects of software defects, which include data breaches and other cyberattacks, are well documented (D’Arcy et al., 2020). According to IBM’s 2021 Cost of a Data Breach Report, the average cost of a data breach is \$4.2 million in 2021, an increase from \$3.86 million in the previous year (IBM Security Report, 2021). With significant costs associated with software defects, customers are often highly sensitive to quality (Ablon et al., 2016). Therefore, in the rest of this section, we focus on the scenario when the market demand sensitivity to the quality of the firm’s product is high $\begin{array} { r } { ( \mathrm { i . e . , } \gamma > \frac { \tilde { 2 } \alpha \lambda } { \beta } ) } \end{array}$

As discussed in the previous section, the effectiveness of the open source community is higher $( \mathrm { i } . \mathrm { e } . , \ h _ { k i } )$ when the software is fully open (i.e., Strategy O) than when the software is partially open (i.e., Strategies C and E). This is because the effectiveness of the open source community regarding the software quality may be higher when opening larger and more sensitive portions of the software code.

With respect to baseline demands for partially open and fully open software, anecdotal evidence and prior literature provide several alternative arguments. In particular, on the one hand, it is argued that the baseline demand for open source software may be higher compared to partially open software. Specifically, previous literature on open source software argues that software openness may increase the likelihood of attracting a wider audience (Lerner & Tirole, 2002; West, 2003). Open source software may also attract skilled users or software developers as it provides the opportunity to modify the code and work with other developers (Dahlander & Magnusson, 2005). Therefore, one can argue that as a firm opens a higher portion of its software code, more developers and users become interested in the software so the demand for the product may become higher compared to that for proprietary or partially open software.

The reason is that the users now believe that open source software will be easy to use; hence, more users are likely to join the software platform (Rudin, 2019). Therefore, it can be argued that, in certain instances, fully opening up the software may be associated with higher baseline demand for the software, i.e., $d _ { O i } > d _ { C i } > d _ { E i }$

On the other hand, it is also argued that opening up software does not necessarily attract more users to the software platform and that opening up the software may instead decrease the baseline demand for the software. The reasons behind this argument include loss of intellectual property and increased security risks. Osborne (2019) reported that more than 65% of respondents “worry about license risk and the loss of intellectual property through using open-source software.” Similarly, Rudin (2019) reported that open source software may be associated with higher risks. Based on these arguments, we anticipate that fully open software may not attract a certain group of customers. Therefore, in certain business scenarios, the baseline demand for fully open software may be lower than that for partially open software, i.e., $d _ { E i } > d _ { C i } > d _ { O i }$

The above conflicting arguments suggest that increasing levels of openness may be associated with higher baseline demand or lower baseline demand. Given these two plausible business scenarios in the software market, for completeness, we first examine the firm’s best responses with respect to openness strategies when $d _ { O i } > d _ { C i } >$ $d _ { E i }$ and then shift our focus to the scenario when $d _ { E i } >$ $d _ { C i } > d _ { O i }$

## Scenario I: Higher Baseline Demand with Increasing Software Openness

In the first scenario, it might seem more beneficial for the firm to fully open its software to take advantage of the higher efficiency of the open source community and increased baseline demand for the software. However, our analysis reveals that this is not always the case. We found that the firm may open its software only when the benefits of openness (i.e., increased baseline demand and quality) outweigh the cost of collaboration between the open source community and the focal firm. In particular, when the cost of collaboration is high, it may be beneficial for the firm to keep its software proprietary. On the other hand, when the cost of collaboration is low, we found that the firm would choose Strategy O over the other open strategies (i.e., C and E). These results are summarized in the following proposition.

<table><tr><td colspan="4">Table 2. Nash Equilibrium Solutions: Scenario when  $d_{Oi} > d_{Ci} > d_{Ei}$ </td></tr><tr><td rowspan="2" colspan="2"></td><td colspan="2">Firm 2</td></tr><tr><td>Open</td><td>Proprietary</td></tr><tr><td rowspan="2">Firm 1</td><td>Open</td><td> $(O,O)^{*}$ Conditions: $y_1 < \mathcal{Y}_{C4}; y_2 < \mathcal{Y}_{R4}$ </td><td> $(O,P)^{*}$ Conditions: $y_1 < \mathcal{Y}_{C1}; y_2 > \mathcal{Y}_{R4}$ </td></tr><tr><td>Proprietary</td><td> $(P,O)^{*}$ Conditions: $y_1 > \mathcal{Y}_{C4}; y_2 < \mathcal{Y}_{R1}$ </td><td> $(P,P)^{*}$ Conditions: $y_1 > \mathcal{Y}_{C1}; y_2 > \mathcal{Y}_{R1}$ </td></tr></table>

Proposition 1: When the baseline demand for fully open software is higher than the demand for partially open software (i.e., $d _ { O i } > d _ { C i } > d _ { E i } ) ,$ , partial openness is not observed at equilibrium. In particular, there exist thresholds ${ \mathcal { Y } } _ { \mathcal { C } 1 } , \ { \mathcal { Y } } _ { \mathcal { C } 4 } ,$ $\mathcal { Y } _ { \mathcal { R } 1 }$ and $\mathcal { Y } _ { \mathcal { R } 4 }$ that characterize the Nash equilibrium outcomes for Firm 1 and Firm 2:

I. Symmetric equilibria

(a) (??, ??) when $y _ { 1 } > y _ { \mathcal { C } 1 }$ and $y _ { 2 } > \mathcal { Y } _ { \mathcal { R } 1 } ,$

(b) (??, ??) when $y _ { 1 } < { \mathcal { Y } } _ { { \mathcal { C } } 4 }$ and $y _ { 2 } < \mathcal { Y } _ { \mathcal { R } 4 } ;$

II. Asymmetric equilibria

(a) (??, ??) when $y _ { 1 } < \mathcal { Y } _ { \mathcal { C } 1 }$ and $y _ { 2 } > \mathcal { Y } _ { \mathcal { R } 4 }$

(b) (??, ??) when $y _ { 1 } > y _ { \mathcal { C } 4 }$ and $y _ { 2 } < \mathcal { Y } _ { \mathcal { R } 1 }$

The equilibrium solutions and their conditions are summarized in Table 2.

One might anticipate that firms might switch from fully open to partial openness strategies as the cost of collaboration (i.e., ??) increases. However, Proposition 1 reveals that firms should not consider partial openness regardless of the cost of collaboration. Interestingly, we only observed fully open or fully closed strategies for firms when the baseline demand for fully open software was significantly high. More specifically, when the cost of collaboration is beyond the thresholds $\mathcal { Y } _ { \mathrm { { C l } } }$ for Firm 1 and $\mathcal { Y } _ { \mathrm { { R 1 } } }$ for Firm 2, (P, P) is an equilibrium, i.e., both firms are better off keeping their software proprietary in such a case. However, as the cost of collaboration goes below the thresholds $\mathcal { Y } _ { \mathrm { C 4 } }$ for Firm 1 and $\mathcal { Y } _ { \mathrm { { R 4 } } }$ for Firm 2, the equilibrium outcomes for both firms are open source, i.e., (O, O) is the Nash equilibrium. Asymmetric equilibria ((O, P) or (P, O)) arise when the cost of collaboration is low for one firm and high for a competing firm.

The intuition for the result in Proposition 1 that partial openness is not optimal for firms is as follows. When the demand’s sensitivity to quality is high $\begin{array} { r } { ( \mathrm { i . e . , } \gamma > \frac { 2 \alpha \lambda } { \beta } ) } \end{array}$ , it is beneficial for firms to increase the quality of the software when there is an opportunity. To benefit from the faster rate of improvement in quality due to the higher effectiveness of the open source community (as $h _ { O i } > h _ { C i } > h _ { E i } )$ , increasing the extent of openness is a plausible option. Furthermore, the firm can reduce its effort costs by relying more on the open source community. Therefore, when the cost of collaboration is low, a firm can increase its quality levels and reduce its effort costs by fully opening the software. Since the baseline demand for fully open software is higher than that for partially open software (i.e., $d _ { O i } > d _ { C i } > d _ { E i } )$ and the effectiveness of the open source community is also higher for fully open source software $( \mathrm { i . e . , } h _ { O i } > h _ { C i } > h _ { E i } )$ in this scenario, the full openness strategy dominates partial openness strategies. However, if the cost of collaboration is higher than the provided thresholds in Proposition 1, the additional benefit from any form of openness is less than the cost of collaboration. Therefore, the firm will choose to keep its software proprietary.

Given that the software market is highly sensitive to quality, the result in Proposition 1 provides a key business insight. Specifically, in this case, it might be beneficial for the firm to fully open its software rather than partially opening it. This conclusion is consistent with the strategy of Sun Microsystems and its decision to open source its programming software Java. We note that the marketplace for general-purpose programming software, which Java belonged to, was highly sensitive to quality, i.e., ?? was high (Martens, 2006). Sun Microsystem’s existing ties with the open source community ensured that the cost of collaboration (i.e., ??) was low. Furthermore, the firm believed that “open sourcing Java will help stop fragmentation in the market and instead drive convergence around Java” (Martens, 2006). In such a scenario, an optimal strategy for the firm to operate in a highly quality-sensitive market would be to make the software fully open when the cost of collaboration is relatively low or keep the software proprietary when the cost of collaboration is relatively high, which explains one plausible reason behind Sun Microsystem’s decision to fully open source its software.

![](/api/attachments/XAVBM799/fulltext/images/6a42d0c2215d6954073d4dbd4a222b3a1abcc12b6616e18541e80d73c522562f.jpg)  
Figure 2. Nash Equilibrium Solutions when ??<sub>??</sub> > ??<sub>??</sub> > ??<sub>??</sub> and ??<sub>??</sub> > ??<sub>??</sub> > ??<sub>??</sub>

## Scenario II: Lower Baseline Demand with Increasing Software Openness

We shift our focus to the second business scenario, where higher levels of openness could negatively impact baseline demands, i.e., $d _ { E i } > d _ { C i } > d _ { O i }$ . This business scenario is more appropriate when software customers prefer to keep their software codes proprietary (Rudin, 2019). Furthermore, when customers are highly sensitive to security risks, they will have a higher preference for software that does not reveal critical core components to customers. In the following proposition, we characterize the firm’s best response when the market is sensitive to security risks or when customers prefer to closely guard their intellectual property (i.e., software code).

Similar to Proposition 1, we found that when the cost of collaboration (i.e., ??) is high, it is optimal for the firm to keep its software proprietary. As discussed earlier, this result hinges on the fact that the benefit the firm gets from opening the software (either partially or fully) does not outweigh the cost of collaboration. However, when firms’ collaboration costs go below the thresholds (??<sub>C1</sub> for Firm 1 and $\mathcal { Y } _ { \mathrm { { R l } } }$ for Firm 2), the benefits of opening the software (either partially or fully) exceed the additional costs associated with software opening. We establish the existence of a Nash equilibrium in the proposition below.

Proposition 2: When the cost of collaboration is low $( y _ { 1 } <$ ??<sub>C1</sub> and $y _ { 2 } < \mathcal { Y } _ { \mathrm { R 1 } } )$ and the baseline demand for partially open software is higher than that for fully open software (i.e., $d _ { E 2 } > d _ { C 2 } > d _ { O 2 } )$ , there exist six thresholds for the firms’ open source community effort (i.e., s<sub>1</sub> and s<sub>2</sub>): $X _ { 1 } , ~ X _ { 2 } ,$

$X _ { 3 } , \ Z _ { 1 } , \ Z _ { 2 } ,$ , and $\Sigma _ { 3 } ,$ which characterize the Nash equilibrium outcomes for Firm 1 and Firm 2:

(a) There exists a Nash equilibrium when $X _ { 2 } > X _ { 3 } >$ $X _ { 1 }$ and $Z _ { 2 } > Z _ { 3 } > Z _ { 1 }$ . The equilibria solution sets are presented in Figure 2.

(b) There exists a Nash equilibrium when $X _ { 1 } > X _ { 3 } >$ $X _ { 2 }$ and $Z _ { 1 } > Z _ { 3 } > Z _ { 2 }$ . The equilibria solution sets are presented in Figure 3.

The thresholds are defined as follows: $\begin{array} { r } { X _ { 1 } \equiv \frac { X ( d _ { C 2 } - d _ { O 2 } ) } { h _ { O 2 } - h _ { C 2 } } , } \end{array}$ $\begin{array} { r } { X _ { 2 } \equiv \frac { X ( d _ { E 2 } - d _ { C 2 } ) } { h _ { C 2 } - h _ { E 2 } } , \quad X _ { 3 } \equiv \frac { X ( d _ { E 2 } - d _ { O 2 } ) } { h _ { O 2 } - h _ { E 2 } } , \quad Z _ { 1 } \equiv \frac { Z ( \stackrel { \smile } { d _ { C 1 } } - \stackrel { \smile } { d _ { O 1 } } ) } { h _ { O 1 } - h _ { C 1 } } , } \end{array}$ $\begin{array} { r } { Z _ { 2 } \equiv \frac { Z ( d _ { E 1 } - d _ { C 1 } ) } { h _ { C 1 } - h _ { E 1 } } , } \end{array}$ and $\begin{array} { r } { Z _ { 3 } \equiv \frac { Z ( d _ { E 1 } - d _ { O 1 } ) } { h _ { O 1 } - h _ { E 1 } } } \end{array}$ (Detailed expressions of ?? and ?? are presented in the proof.)

Proposition 2 reveals that in Scenario II (where the baseline demand decreases with the level of openness) adopting a partially open software approach can be an optimal strategy for firms. This stands in contrast to Scenario I (see Proposition 1), where a partial openness strategy is not optimal for firms. In Proposition 2, the thresholds $Z _ { 1 }$ and $X _ { 1 }$ represent the loss-to-gain ratio for Firms 1 and 2, respectively. These ratios quantify the reduction in demand relative to the gain in efficiency resulting from the collaborative efforts of the open source community when switching from Strategy C to Strategy O. Similarly, the thresholds $Z _ { 2 }$ and $X _ { 2 }$ denote the loss-to-gain ratio for Firms 1 and 2 respectively when switching from Strategy E to Strategy C. Finally, $Z _ { 3 }$ and?? <sub>3</sub> represent the loss-to-gain ratio when switching from Strategy E to Strategy O for Firms 1 and 2 respectively.

<table><tr><td>S2</td><td>(E,O)*</td><td>(C,O)*</td><td>(O,O)*</td></tr><tr><td>X1</td><td>(E,C)*</td><td>(C,C)*</td><td>(O,C)*</td></tr><tr><td>X2</td><td>(E,E)*</td><td>(C,E)*</td><td>(O,E)*</td></tr></table>

Figure 3. Nash Equilibrium Solutions when $\therefore \angle B = \angle A = \angle C$ and ??<sub>??</sub> > ??<sub>??</sub> > ??<sub>??</sub>

Part (a) of Proposition 2 summarizes the equilibrium strategy when the following inequalities for the thresholds of the efforts of the open source community hold: $X _ { 2 } > X _ { 3 } > X _ { 1 }$ and $Z _ { 2 } >$ $Z _ { 3 } > Z _ { 1 }$ . These thresholds reflect a scenario where the loss-togain ratio of switching from Strategy E to Strategy C exceeds that of switching from Strategy C to Strategy O for both firms. In practice, this scenario arises when the core components of the code are perceived to be highly sensitive. As a result, opening up these core components would significantly increase the lossto-gain ratio experienced by the firms. In this scenario, when the thresholds $Z _ { 3 }$ and $X _ { 3 }$ are surpassed by the open source community’s efforts on Firm 1’s (i.e., $s _ { 1 } > Z _ { 3 } )$ and Firm $2 \mathrm { { \dot { s } } }$ (i.e., $s _ { 2 } > X _ { 3 } )$ software efforts, respectively, both firms can reap benefits by fully opening the software, resulting in $( 0 , 0 )$ being the equilibrium. By fully opening up the software, the firms can effectively leverage the open source community’s effort with greater efficiency (as $h _ { O i } > h _ { C i } > h _ { E i } )$ This enhanced efficiency, combined with higher efforts by the open source community, helps firms increase the quality of the software. As a result, in a quality-dependent market, the firm’s benefit from the open source community can outweigh the negative impacts of opening. On the other hand, i.e., when the effort exerted by the open source community is low $( \mathrm { i } . \mathrm { e } . , s _ { 1 } <$ $Z _ { 3 }$ and $s _ { 2 } < X _ { 3 } )$ , our findings demonstrate that equilibrium is achieved through (E, E) firm strategies. Additionally, asymmetric equilibrium solutions, such as (O, E) or (E, O), can be achieved depending on the effort levels of the open communities on the respective firm’s software.

Notably, in the scenario presented in Part (a) of the proposition, Strategy C is never an optimal strategy for a firm. The reasoning behind this interesting result lies in the relatively high loss-togain ratio associated with transitioning from Strategy E to Strategy C. This insight has important implications for managers—the perceived sensitivity of core code components plays a crucial role in firms’ decision-making processes regarding openness. Specifically, when the core code is deemed sensitive, firms should consider adopting either a fully open source approach or selectively opening the extension code, depending on the level of engagement from the open source community.

Part (b) of Proposition 2 further provides insights when the lossto-gain ratios when switching from Strategy C to O is higher compared to switching from Strategy E to C (i.e., $Z _ { 1 } > Z _ { 3 } >$ $Z _ { 2 }$ and $X _ { 1 } > X _ { 3 } > X _ { 2 } )$ . When the effort of the open source community is high (i.e. $, s _ { 1 } > Z _ { 1 }$ and $s _ { 2 } > X _ { 1 } )$ , equilibrium is achieved through $( 0 , 0 )$ . The fully open strategies of the firms enable them to leverage the open source community’s higher effort levels and enhanced efficiency (as indicated by $h _ { O i } >$ $h _ { C i } > h _ { E i } )$ . In contrast, when the efforts of the open source community are at a medium level (i.e., $Z _ { 2 } < s _ { 1 } < Z _ { 1 }$ and $X _ { 2 } <$ $s _ { 2 } < X _ { 1 } )$ , the equilibrium strategy is $( \mathrm { C } , \mathrm { C } ) .$ Finally, when the effort levels are low $( \mathrm { i } . \mathrm { e } . , s _ { 1 } < Z _ { 2 }$ and $s _ { 2 } < X _ { 2 } )$ , the firm opens up its extension or the peripheral software code, resulting in (E, E) as the equilibrium. Furthermore, as illustrated in Figure 3, asymmetric equilibrium emerges depending on the effort levels of the open source community on the firm’s software.

Our findings presented in Proposition 2 shed light on the dynamics of equilibrium strategies resulting from varying effort levels of the open source community. By carefully assessing effort levels and evaluating the potential impacts on loss-to-gain ratios, software firms can make informed decisions on whether to adopt a full openness or partial openness strategy. Notably, when the open source community exhibits higher levels of engagement, firms can adopt a fully open strategy. In so doing, firms can tap into the increased effort and effectiveness of the open source community, which will outweigh the potential negative consequences of openness, such as a lower baseline demand. However, when the effort of the open source community is low, it will be optimal for the firm to choose a partial openness strategy. Thus, when making decisions related to openness strategies, firms need to evaluate the engagement they expect to receive from the open source community. These findings yield compelling and valuable insights for firms in the business landscape. In particular, these insights hold significance when customers demonstrate sensitivity to both quality and privacy concerns.

## Discussion

Firms are increasingly switching to open source environments to leverage the benefits of open source communities. In addition to fully opening software, firms also have an option to partially open software. Partial opening may imply that a firm only opens its core software code or only opens software extensions to the open source community. We model the effects of openness decisions (i.e., what aspects of the code to open) on optimal pricing decisions and the effort exerted by firms. In order to determine the best course of action in open source environments with competition, software firms need to make several decisions, including what aspects to open (i.e., core, extension, or both), the effort required to improve the quality of the software, and the price of the product.

We built a game-theoretical model to understand the equilibrium outcome for competing firms. We considered a single-period setting using two software vendors with differentiated products competing on quality and price. We captured both the main effects (focal firm’s) and the crosseffects (competing firm’s) of prices and quality on the demand for the products. Our model also captured both the positive and negative effects of openness. Specifically, opening up the software enables the open source community to improve the quality of the software and may also have a positive effect on the baseline demand for the product.

However, software openness could also have a negative effect on the baseline demand for the product, especially when the customer is sensitive to intellectual property concerns. We also incorporated the cost of collaboration associated with opening the software in our model. Our work extends the prior literature by incorporating the notion of partial open sourcing when modeling the optimal price and effort required to maintain software.

## Managerial Implications

From a managerial perspective, our study aims to help managers in their decision-making process and highlight the importance of various factors that affect the optimal course of action, characteristics of the market (e.g., demand sensitivity to quality and competition), characteristics of the firm (e.g., the cost of fixing software defects), and characteristics of the open source community (e.g., effort exerted by the community).

Our analysis reveals that in a scenario where the fully open strategy attracts a wider audience than a partially open strategy, partially opening the software is not an optimal choice at any level of effort exerted by the open source community (see Proposition 1). Therefore, in this business scenario, the managers of software firms making decisions on the level of openness should carefully evaluate the marketing implications of openness strategies.

On the other hand, if the fully open strategy does not attract a wide audience because of potential increases in security risks and intellectual property losses, firms might consider partial openness strategies (see Proposition 2). Specifically, we found that the demand loss to efficiency gain ratio has a vital role in deciding on the extent of openness.

In addition to the effects of price and quality on demand for the software, demand may be affected by network externalities. In the presence of network externalities, if the positive network externality for a focal firm is significantly stronger for a fully open strategy than for a partially open strategy, the baseline demand parameter would be higher than what is derived from the current demand function. Subsequently, this may lead to the scenario discussed in Proposition 1 rather than the scenario presented in Proposition 2 (i.e., the baseline demand for fully open software is higher than that for partially open software). This further implies that rather than seeing partial openness as an equilibrium outcome, we would expect to observe either fully open or proprietary software strategies when positive network externalities are high.

## Future Research Directions Implications

In this research note, we take a stylized approach to determining strategic decisions related to openness, price, and effort level. Following prior literature, we consider a linear demand model that is a function of both quality and price. Future work can empirically examine the functional form of the demand model and incorporate network externalities into the model, which will allow researchers to examine the impacts of network externalities on the openness decisions of firms. In addition, while our current model setup provides insights related to openness strategies when firms make decisions simultaneously, future research could study firms decisions when they enter the market sequentially. Future studies could also consider estimating the key parameters that we use in the model (e.g., cost multiplier for effort, the relative impact of the open source community’s effort, and the relative cost of collaboration). Estimation of these parameters would make the results more generalizable and could provide prescriptive insights for firms.

## Acknowledgments

The authors thank the senior editor, the associate editor, and the three anonymous reviewers for their helpful feedback throughout the review process.

## References

Ablon, L., Heaton, P., Lavery, D. C., & Romanosky, S. (2016). Consumer attitudes toward data breach notifications and loss of personal information. RAND Corporation.

Apple (2019). Open at the source. https://www.apple.com/opensource/

Arora, A., Krishnan, R., Telang, R., & Yang, Y. (2010). An empirical analysis of software vendors’ patch release behavior: Impact of vulnerability disclosure. Information Systems Research, 21(1) 115-132. https://doi.org/10.1287/isre.1080.0226

August, T., Shin, H., & Tunca, T. I. (2013). Licensing and competition for services in open source software. Information Systems Research, 24(4), 1068-1086. https://doi.org/10.1287/ isre.2013.0486

August, T., Shin, H., & Tunca, T. I. (2018). Generating value through open source: Software service market regulation and licensing policy. Information Systems Research, 29(1), 186-205. https://doi.org/10.1287/isre.2017.0726

Banker, R. D., Khosla, I., & Sinha, K. K. (1998). Quality and competition. Management Science, 44(9), 1179-1192. https://doi.org/10.1287/mnsc.44.9.1179

Banker, R. D., & Slaughter, S. A. (1997). A field study of scale economies in software maintenance. Management Science, 43(12), 1709-1725. https://doi.org/10.1287/mnsc.43.12.1709

Bartlett, D (2019). How to make apps with Swift 5 on Mac. https://www.macworld.co.uk/how-to/mac-software/make-appsswift-5-mac-3523633/

Bonaccorsi, A., & Rossi, C. (2003). Why open source software can succeed. Research Policy, 32(7), 1243-1258. https://doi.org/ 10.1016/S0048-7333(03)00051-9

Casadesus-Masanell, R., & Llanes, G. (2011). Mixed source. Management Science, 57(7), 1212-1230. https://doi.org/10.1287/ mnsc.1110.1353

Dahlander, L., & Magnusson, M. G. (2005). Relationships between open source software companies and communities: Observations from Nordic firms. Research Policy, 34(4), 481-493. https://doi.org/10.1016/j.respol.2005.02.003

D’Arcy, J., Adjerid, I., Angst, C. M., & Glavas, A. (2020). Too good to be true: firm social performance and the risk of data breach. Information Systems Research, 31(4), 1200-1223. https://doi.org/10.1287/isre.2020.0939

Gal-Or, E., & Ghose, A. (2005). The economic incentives for sharing security information. Information Systems Research, 16(2), 186- 208. https://doi.org/10.1287/isre.1050.0053

Google. (2021). Why open source. https://opensource.google/docs/why/

Haddad, I., & Yehuda, G. (2021). Improving your open source development impact. Linux Foundation. https://linuxfoundation. org/tools/improving-your-open-source-development-impact/

Hanson, M. (2019). Windows core OS could be partially open source. https://www.techradar.com/news/windows-core-os-could-bepartially-open-source

Haruvy, E., Sethi, S. P., & Zhou, J. (2008). Open source development with a commercial complementary product or service. Production and Operations Management, 17(1), 29-43. https://doi.org/10.3401/poms.1070.0004

Ho, S. Y., & Rai, A. (2017). Continued voluntary participation intention in firm-participating open source software projects. Information Systems Research, 28(3), 603-625. https://doi.org/10.1287/isre.2016.0687

Huang, H., Parker, G., Tan, Y., & Xu, H. (2020). Altruism or shrewd business? Implications of technology openness on innovations and competition. MIS Quarterly, 44(3), 1049-1072. https://doi.org/10.25300/MISQ/2020/14589

IBM Security Report. (2021). How much does a data breach cost. https://www.ibm.com/security/data-breach

Ionos. (2019). Windows vs. Linux: A comparison. IONOS. https://www.ionos.com/digitalguide/server/know-how/linux-vswindows/

Koch, S. (2009). Exploring the effects of sourceforge.net coordination and communication tools on the efficiency of open source projects using data envelopment analysis. Empirical Software Engineering, 14(4), 397-417. https://doi.org/10.1007/ s10664-008-9086-4

Kumar, V., Gordon, B. R., & Srinivasan, K. (2011). Competitive strategy for open source software. Marketing Science, 30(6), 1066-1078. https://doi.org/10.1287/mksc.1110.0669

Lerner, J., & Tirole, J. (2000). The simple economics of open source. SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=214311

Lerner, J., & Tirole, J. (2002). Some simple economics of open source. The Journal of Industrial Economics, 50(2), 197-234. https://doi.org/10.1111/1467-6451.00174

Levine, P. (2014). Why there will never be another RedHat: The economics of open source. Techcrunch. https://techcrunch.com/ 2014/02/13/please-dont-tell-me-you-want-to-be-the-next-redhat/

Liu, D., Ji, Y., & Mookerjee, V. (2011). Knowledge sharing and investment decisions in information security. Decision Support Systems, 52(1), 95-107. https://doi.org/10.1016/j.dss.2011.05.007

Martens, C. (2006). It’s official: Sun open sources Java. https://www.javaworld.com/article/2077658/core-java/it-sofficial--sun-open-sources-java.html

Microsoft. (2020). Open source: Featured Projects. https://opensource.microsoft.com/projects/

Milgrom, P. (1994). Comparing optima: Do simplifying assumptions affect conclusions? Journal of Political Economy, 102(3), 607- 615. https://doi.org/10.1086/261948

Myles, G. (2017, December 13). Balancing open source and proprietary IP—They can co-exist. Dropbox.Tech https://blogs. dropbox.com/tech/2017/12/balancing-open-source-andproprietary-ip-they-can-co-exist/

Niculescu, M. F., Wu, D. J., & Xu, L. (2018). Strategic intellectual property sharing: Competition on an open technology platform under network effects. Information Systems Research, 29(2), 498-519. https://doi.org/10.1287/isre.2017.0756

Octoverse. (2019). The world of open source. https://octoverse. github.com/#the-world-of-open-source

Osborne, C. (2019). Open-source software management fails to meet security concerns. https://www.zdnet.com/article/open-sourcesoftware-management-falls-behind-security- concerns/

Paulson, J. W., Succi, G., & Eberlein, A. (2004). An empirical study of open-source and closed-source software products. IEEE Transactions on Software Engineering, 30(4), 246-256. https://doi.org/10.1109/TSE.2004.1274044

Rudin, D. (2019, December 12). Microsoft announces OpenChain 2.0 conformance for open source. Microsoft Open Source Blog. https://cloudblogs.microsoft.com/opensource/2019/12/12/annou ncing-microsoft-openchain-conformance/

West, J. (2003). How open is open enough? Melding proprietary and open source platform strategies. Research Policy, 32(7), 1259- 1285. https://doi.org/10.1016/S0048-7333(03)00052-0

Xue, L., Yang, K., & Yao, Y. (2018). Examining the effects of interfirm managerial social ties on IT components diversity: An agency perspective. MIS Quarterly 42(2), 679-694. https://doi.org/10.25300/MISQ/2018/13952

## About the Authors

Rakesh R. Mallipeddi is an assistant professor of operations and business analytics at the Fisher College of Business, The Ohio State University. His research interests include technology management, social networks and social responsibility. He received his Ph.D. in Business Administration from Mays Business School, Texas A&M University. He currently serves as an elected vice president of communications at the Production and Operations Management Society.

Emre M. Demirezen is an assistant professor of information and operations management at the Warrington College of Business, University of Florida. His research interests include platform participation and dynamics, the economics of health information technology, health information exchanges, physiological modeling, value co-creation, open source software, digital supply chains, and recommender systems. He received his Ph.D. in business administration from Mays Business School, Texas A&M University. He currently serves as an elected regional vice president-Africa and Middle East at the Production and Operations Management Society.

Subodha Kumar is the Paul Anderson Distinguished Chair Professor of Marketing and Supply Chain Management (with joint appointments in information systems and statistical science) at the Fox School of Business, Temple University. He is the founding director of the Center for Data Analytics and the Ph.D. concentration advisor of Operations and Supply Chain Management. He is the deputy editor and a department editor of Production and Operations Management and the founding executive editor of Management and Business Review. He has held several other editorial positions at leading journals and has published many papers in prestigious journals.

Ram D. Gopal is a Distinguished Fellow of the Information Systems Society and a Turing Fellow of the Alan Turing Institute, a professor of information systems and management, and the prodean for research, engagement, and impact at Warwick Business School. He also serves as the academic director of the Gillmore Centre for Financial Technology. His research spans big data analytics, health informatics, financial technologies, information security, privacy and valuation, intellectual property rights, online market design, and the business impacts of technology.

## Appendix A

## Equilibrium Prices and Efforts

Firms determine their optimal prices in Stage 3, after they determine their openness strategy (in Stage 1) and their effort levels (in Stage 2). The equilibrium prices are in the lemma below.

LEMMA A.1 For a given effort and quality levels, the equilibrium prices are as follows:

$$
p _ {i} ^ {*} = \frac {2 \alpha d _ {k i} + \beta d _ {l j} + 2 \alpha \gamma x _ {i} ^ {*} - \beta \lambda x _ {i} ^ {*} - 2 \alpha \lambda x _ {j} ^ {*} + \beta \gamma x _ {j} ^ {*}}{4 \alpha^ {2} - \beta^ {2}}, i, j = 1, 2; i \neq j; k, l \in \{O, C, E, P \}.
$$

After deriving the price equilibrium, in the second stage, we characterized the optimal effort levels of the focal firm and its competitor given their openness strategy. We summarize the optimal effort levels in the following lemma.

LEMMA A.2 For a given strategy ?? for openness and price level $( { p } _ { i } ) ,$ , the optimal effort levels are as follows:

$$
e _ {i} = \frac {\alpha R (c _ {j} T (2 \alpha d _ {k i} + \beta d _ {l j} + 2 h _ {k i} R s _ {i} + h _ {l j} M s _ {j}) - \alpha R (\gamma d _ {k i} + d _ {l j} \lambda + h _ {k i} s _ {i} Z))}{c _ {i} T (c _ {j} T ^ {2} - \alpha R ^ {2}) - \alpha R ^ {2} (c _ {j} T - \alpha Z)}, i, j = 1, 2; i \neq j; k, l \in \{O, C, E, P \},
$$

where $R = 2 \alpha \gamma - \beta \lambda , T = 4 \alpha ^ { 2 } - \beta ^ { 2 } , Z = \gamma ^ { 2 } - \lambda ^ { 2 } , a n d M = \beta \gamma - 2 \alpha \lambda$

To ensure the concavity of the firm’s maximization problem, we require $\begin{array} { r } { \frac { \partial ^ { 2 } \Pi _ { i } } { \partial e _ { i } ^ { 2 } } < 0 \mathrm { ~ a n d } \frac { \partial ^ { 2 } \Pi _ { j } } { \partial e _ { j } ^ { 2 } } < 0 , } \end{array}$ , which implies: $\begin{array} { r } { c _ { i } > \frac { \alpha ( \beta \lambda - 2 \alpha \gamma ) ^ { 2 } } { ( \beta ^ { 2 } - 4 \alpha ^ { 2 } ) ^ { 2 } } ; i = 1 , 2 } \end{array}$ This condition provides a lower bound for the relative effort costs and ensures that the profit function is concave, which allowed us to derive comparative statics and managerial insights by focusing on the interior solutions. All proofs are provided in the following section.

## Proofs

## Proof of Lemma A1

The demand equation for firm ?? is given by: $q _ { i } = d _ { k i } - \alpha p _ { i } + \beta p _ { j } + \gamma x _ { i } - \lambda x _ { j }$

(A1)

The profit function for firm ?? is:

$$
\Pi_ {i} = p _ {i} q _ {i} - c _ {i} e _ {i} ^ {2} - y _ {i} s _ {i} + n _ {l i} s _ {j}.\tag{A2}
$$

Substituting the demand function $q _ { i }$ in the profit function (i.e., Equation A2), we get:

$$
\Pi_ {i} = p _ {i} \big (d _ {k i} - \alpha p _ {i} + \beta p _ {j} + \gamma x _ {i} - \lambda x _ {j} \big) - c _ {i} e _ {i} ^ {2} - y _ {i} s _ {i} + n _ {l i} s _ {j}.\tag{A3}
$$

We now solve for $p _ { i }$ following the firm’s profit maximization problem stated in Equation (A3) Specifically, from the first order condition $\begin{array} { r } { ( \mathrm { i . e . , ~ } \frac { d \Pi _ { i } } { d p _ { i } } = 0 ) } \end{array}$ , we get:

$$
p _ {i} = \frac {2 \alpha d _ {k i} + \beta d _ {l j} + 2 \alpha \gamma x _ {i} - \beta \lambda x _ {i} - 2 \alpha \lambda x _ {j} + \beta \gamma x _ {j}}{4 \alpha^ {2} - \beta^ {2}},
$$

where $i , j = 1 , 2 ; i \neq j ; k , l \in \{ O , C , E , P \}$ . For $\Pi _ { i }$ to be concave in $p _ { i } ,$ , we require, $\begin{array} { r } { \frac { d ^ { 2 } \Pi _ { i } } { d p _ { i } ^ { 2 } } < 0 \mathrm { o r } - 2 \alpha < \mathrm { ~ 0 ~ } } \end{array}$ and, thus, this condition is satisfied when $\alpha > 0$

## Proof of Lemma A.2

The quality of firm $i \ ' _ { \mathrm { { s } } }$ software is given by: $x _ { i } = e _ { i } + h _ { k i } s _ { i }$ . Substituting $x _ { i }$ and equilibrium price $( \mathrm { i } . \mathrm { e } . , p _ { i } )$ obtained in Lemma A1 and solving for effort $e _ { i } ,$ we get:

$$
\begin{array}{l}e _ {i}\\= \frac {\alpha (2 \alpha \gamma - \beta \lambda) \left(c _ {j} (4 \alpha^ {2} - \beta^ {2}) \big (\beta d _ {l j} + 2 \alpha d _ {k i} - 2 \alpha h _ {l j} \lambda s _ {j} + \beta \gamma h _ {l j} s _ {j} + 2 \alpha \gamma h _ {k i} s _ {i} - \beta h _ {k i} \lambda s _ {i}\right) - \alpha (2 \alpha \gamma - \beta \lambda) \left(d _ {l j} \lambda + \gamma d _ {k i} + h _ {k i} s _ {i} (\gamma^ {2} - \lambda^ {2})\right)\left. \right)}{c _ {i} (4 \alpha^ {2} - \beta^ {2}) \big (c _ {j} (\beta^ {2} - 4 \alpha^ {2}) ^ {2} - \alpha (\beta \lambda - 2 \alpha \gamma) ^ {2} \big) - \alpha (\beta \lambda - 2 \alpha \gamma) ^ {2} \big (- \alpha \gamma^ {2} + \alpha \lambda^ {2} + 4 \alpha^ {2} c _ {j} - \beta^ {2} c _ {j} \big)},\end{array}
$$

where $i , j = 1 , 2 ; i \neq j ; k , l \in \{ O , C , E , P \}$

Furthermore, in order to have the second-order condition satisfied $\begin{array} { r } { ( \mathrm { i } . \mathrm { e } . , \frac { d ^ { 2 } \Pi _ { i } } { d e _ { i } ^ { 2 } } < 0 ) , \mathrm { w e ~ r e q u i r e } \frac { 2 \alpha ( \beta \lambda - 2 \alpha \gamma ) ^ { 2 } } { ( \beta ^ { 2 } - 4 \alpha ^ { 2 } ) ^ { 2 } } - 2 c _ { i } < 0 \mathrm { ~ o r ~ } c _ { i } > \frac { \alpha ( \beta \lambda - 2 \alpha \gamma ) ^ { 2 } } { ( \beta ^ { 2 } - 4 \alpha ^ { 2 } ) ^ { 2 } } ; i = 1 , } \end{array}$ $^ { 1 , 2 . }$

Substituting $e _ { i }$ in $p _ { i }$ and $\Pi _ { i } ,$ we get:

$$
\begin{array}{l} p _ {i} = \\ \frac {c _ {i} (4 \alpha^ {2} - \beta^ {2}) \left(c _ {j} (4 \alpha^ {2} - \beta^ {2}) (\beta d _ {l j} + 2 \alpha d _ {k i} - 2 \alpha h _ {l j} \lambda s _ {j} + \beta \gamma h _ {l j} s _ {j} + 2 \alpha \gamma h _ {k i} s _ {i} - \beta h _ {k i} \lambda s _ {i}) - \alpha (2 \alpha \gamma - \beta \lambda) (d _ {l j} \lambda + \gamma d _ {k i} + h _ {k i} s _ {i} (\gamma - \lambda) (\gamma + \lambda))\right)}{c _ {i} (4 \alpha^ {2} - \beta^ {2}) (c _ {j} (\beta^ {2} - 4 \alpha^ {2}) ^ {2} - \alpha (\beta \lambda - 2 \alpha \gamma) ^ {2}) - \alpha (\beta \lambda - 2 \alpha \gamma) ^ {2} (- \alpha \gamma^ {2} + \alpha \lambda^ {2} + 4 \alpha^ {2} c _ {j} - \beta^ {2} c _ {j})} \end{array}
$$

$$
\Pi_ {i} =
$$

$$
\begin{array}{l} n _ {l i} s _ {j} - s _ {i} y _ {k i} \\ + \frac {\alpha c _ {i} ^ {2} (\beta^ {2} - 4 \alpha^ {2}) ^ {2} \Big (c _ {j} (4 \alpha^ {2} - \beta^ {2}) \big (\beta d _ {l j} + 2 \alpha d _ {k i} - 2 \alpha h _ {l j} \lambda s _ {j} + \beta \gamma h _ {l j} s _ {j} + 2 \alpha \gamma h _ {k i} s _ {i} - \beta h _ {k i} \lambda s _ {i} \big) - \alpha (2 \alpha \gamma - \beta \lambda) \left(d _ {l j} \lambda + \gamma d _ {k i} + h _ {k i} s _ {i} (\gamma^ {2} - \lambda^ {2})\right) \Big) ^ {2}}{\Big (\alpha (\beta \lambda - 2 \alpha \gamma) ^ {2} \big (- \alpha \gamma^ {2} + \alpha \lambda^ {2} + 4 \alpha^ {2} c _ {j} - \beta^ {2} c _ {j} \big) - c _ {i} (4 \alpha^ {2} - \beta^ {2}) \big (c _ {j} (\beta^ {2} - 4 \alpha^ {2}) ^ {2} - \alpha (\beta \lambda - 2 \alpha \gamma) ^ {2} \big) \Big) ^ {2}} \\ - \frac {\alpha^ {2} c _ {i} (\beta \lambda - 2 \alpha \gamma) ^ {2} \Big (c _ {j} (4 \alpha^ {2} - \beta^ {2}) \big (\beta d _ {l j} + 2 \alpha d _ {k i} - 2 \alpha h _ {l j} \lambda s _ {j} + \beta \gamma h _ {l j} s _ {j} + 2 \alpha \gamma h _ {k i} s _ {i l} - \beta h _ {k i} \lambda s _ {i l}) - \alpha (2 \alpha \gamma - \beta \lambda) \left(d _ {l j} \lambda + \gamma d _ {k i} + h _ {k i} s _ {i l} (\gamma^ {2} - \lambda^ {2})\right) \Big) ^ {2}}{\Big (\alpha (\beta \lambda - 2 \alpha \gamma) ^ {2} \big (- \alpha \gamma^ {2} + \alpha \lambda^ {2} + 4 \alpha^ {2} c _ {j} - \beta^ {2} c _ {j}) - c _ {i} (4 \alpha^ {2} - \beta^ {2}) \big (c _ {j} (\beta^ {2} - 4 \alpha^ {2}) ^ {2} - \alpha (\beta \lambda - 2 \alpha \gamma) ^ {2}) \Big) ^ {2}}. \end{array}
$$

We note that the solution is feasible when $\begin{array} { r } { \Pi _ { i } > 0 , p _ { i } > 0 , e _ { i } > 0 , \ : \alpha > \beta , \ : \gamma > \lambda , c _ { i } > \frac { \alpha ( \beta \lambda - 2 \alpha \gamma ) ^ { 2 } } { ( \beta ^ { 2 } - 4 \alpha ^ { 2 } ) ^ { 2 } } , } \end{array}$ and non-negativity constraints hold.

## Outline of Proof of Proposition 1

Below we provide an outline of the steps to derive the best response strategies and Nash equilibria for Proposition 1. Formal proofs are provided in Appendix B. We use the following nomenclature for the objective function for Firm $1 \colon \Pi _ { k l 1 } , \forall k \in \{ O , C , E , P \} , \forall l \in \{ \hat { O } , C , E , P \}$ where ?? denotes the open source strategy of Firm 1 and ?? denotes the open source strategy of its competitor (i.e., Firm 2).

1. The set of possible equilibrium solutions is presented in Figure A1. There are 16 possibilities of equilibria. In this proposition, we consider the scenario when $d _ { O i } > d _ { C i } > d _ { E i } , i = 1 , 2$ , and when the demand sensitivity to quality is high $\begin{array} { r } { ( \mathrm { i . e . , } \gamma > ^ { \overset { \cdot } { 2 } \alpha \overset { - } { \lambda } } ) } \end{array}$

2. We derived the best response of Firm 2 to Firm 1’s openness strategies. Specifically, we first compared the profit (or objective function) for each of the strategies of Firm 2 when the competitor’s strategy is proprietary (see Row 1 in Figure A1). In particular, we compared $\Pi _ { P O 2 } , \Pi _ { P C 2 } , \Pi _ { P E 2 }$ , and $\Pi _ { P P 2 }$ to find conditions when each of the strategies might be the best response of Firm 2 to Firm 1’s proprietary strategy.

3. We find that when $y _ { 2 } > \mathcal { Y } _ { \mathcal { R } 1 }$ (this expression is relegated to Appendix B) and the feasibility conditions for Proposition 1 to hold $\begin{array} { r } { ( \mathrm { i } . \mathrm { e } . , \gamma > \frac { 2 \alpha \lambda } { \beta } } \end{array}$ , and $d _ { O i } > d _ { C i } > d _ { E i } )$ , we have $\Pi _ { P P 2 } > M a x \{ \Pi _ { P C 2 } , \Pi _ { P E 2 } , \Pi _ { P O 2 } \}$

<table><tr><td></td><td>OPEN(Column 4)</td><td>CORE OPEN(Column 3)</td><td>EXTENSIONOPEN(Column 2)</td><td>PROPRIETARY(Column 1)</td></tr><tr><td rowspan="4">FIRM 1</td><td> $\text{OPEN}$ (Row 4)</td><td> $(\boldsymbol {O},\boldsymbol {O})$ </td><td> $(\boldsymbol {O},\boldsymbol {C})$ </td><td> $(\boldsymbol {O},\boldsymbol {E})$ </td></tr><tr><td> $\text{CORE OPEN}$ (Row 3)</td><td> $(\boldsymbol {C},\boldsymbol {O})$ </td><td> $(\boldsymbol {C},\boldsymbol {C})$ </td><td> $(\boldsymbol {C},\boldsymbol {E})$ </td></tr><tr><td>EXTENSION OPEN(Row 2)</td><td> $(\boldsymbol {E},\boldsymbol {O})$ </td><td> $(\boldsymbol {E},\boldsymbol {C})$ </td><td> $(\boldsymbol {E},\boldsymbol {E})$ </td></tr><tr><td>PROPRIETARY(Row 1)</td><td> $(\boldsymbol {P},\boldsymbol {O})$ </td><td> $(\boldsymbol {P},\boldsymbol {C})$ </td><td> $(\boldsymbol {P},\boldsymbol {E})$ </td></tr></table>

FIRM 2

## Figure A1. Possible Set of Equilibrium Solutions in Proposition 1

4. Similarly, comparing the profit of Firm 2 in Rows 2, 3, and 4 (in Figure A1) and ensuring that all the conditions presented in Proposition 1 hold, we find:

a. when $y _ { 2 } > y _ { \mathcal { R } 2 } , \Pi _ { E P 2 } > M a x \{ \Pi _ { E C 2 } , \Pi _ { E E 2 } , \Pi _ { E O 2 } \} ,$

b. when $y _ { 2 } > y _ { \mathcal { R } 3 } , \Pi _ { C P 2 } > M a x \{ \Pi _ { C C 2 } , \Pi _ { C E 2 } , \Pi _ { C O 2 } \} ,$ and

c. when $y _ { 2 } > y _ { \mathcal { R } 4 } , \Pi _ { O P 2 } > M a x \{ \Pi _ { O C 2 } , \Pi _ { O E 2 } , \Pi _ { O O 2 } \} .$

5. Furthermore, if:

$$
\mathrm{a.} y _ {2} <   \mathcal {Y} _ {\mathcal {R} 1}, \Pi_ {P O 2} > M a x \{\Pi_ {P C 2}, \Pi_ {P E 2}, \Pi_ {P P 2} \},
$$

$$
\mathsf {b}. y _ {2} <   \mathcal {Y} _ {\mathcal {R 2}}, \Pi_ {E O 2} > M a x \{\Pi_ {E C 2}, \Pi_ {E E 2}, \Pi_ {E P 2} \},
$$

$$
\mathrm{c.} \quad y _ {2} <   \mathcal {Y} _ {\mathcal {R} 3}, \Pi_ {C O 2} > M a x \{\Pi_ {C C 2}, \Pi_ {C E 2}, \Pi_ {C P 2} \}, \text { and }
$$

$$
\mathrm{d}. y _ {2} <   \mathcal {Y} _ {\mathcal {R 4}}, \Pi_ {O O 2} > M a x \{\Pi_ {O C 2}, \Pi_ {O E 2}, \Pi_ {O P 2} \},
$$

then this implies that partial openness is never the best response of Firm 2 to any of the strategies employed by Firm 1.

6. Similarly, we follow the above steps to find the best responses of Firm 1 to Firm $2 \mathit { \ ' } _ { \mathbf { S } }$ strategies (i.e., we analyze the profit functions in Columns 1-4) to derive thresholds ${ \mathcal { Y } } _ { C 1 }$ and ${ \mathcal { Y } } _ { C 4 }$

7. Following these steps corresponds to identifying the strategies that are underlined in Figure A2 as the best responses. In Figure A2, we see that the Nash Equilibrium emerges when the strategies of both firms are the best responses to each other within each cell (under certain thresholds for y). For instance, when ${ \bf y } _ { 2 } > \mathcal { Y } _ { \mathcal { R } 1 }$ and $y _ { 1 2 } > y _ { \mathsf { C 1 } }$ , we underline Strategy P for both firms. The interpretation of Figure A2 leads to the conditions presented in Proposition 1.

![](/api/attachments/XAVBM799/fulltext/images/0df25bf4eb8728b30dbaa351fb5c75b2988ba1c6bea49aac9a77ae107c5fd627.jpg)  
Figure A2. Nash Equilibrium Solutions in Proposition 1

## Outline of Proof of Proposition 2

We follow a similar approach as in Proposition 1, to first derive the best responses for each firm. In this proposition, we consider the scenario when $d _ { O i } < d _ { C i } < d _ { E i } , i = 1 , 2$ , and when the demand sensitivity to the quality is high $( { \mathrm { i . e . , } } \gamma > \frac { 2 { \mathrm { { o } } } { \bar { \lambda } } } { \beta } )$ . As it is the case in Proposition 1, when $y _ { 2 } < \mathcal { Y } _ { \mathcal { R } 1 }$ , we have $\Pi _ { k P 2 } < \Pi _ { k l 2 } , \forall k \in \{ O , C , E , P \} , \forall l \in \{ O , C , E \}$ . Hence, in the rest of this proof, we focus on deriving the best response (i.e., either O, C, or E) when $y _ { 2 } < \mathcal { Y } _ { \mathcal { R } 1 }$

We define the following thresholds:

$$
\begin{array}{r} X \equiv \frac {\alpha (\beta \gamma \lambda + 8 \alpha^ {2} c _ {1} - 2 \beta^ {2} c _ {1} - 2 \alpha \gamma^ {2})}{(2 \alpha \gamma - \beta \lambda) (- \alpha \gamma^ {2} + \alpha \lambda^ {2} + 4 \alpha^ {2} c _ {1} - \beta^ {2} c _ {1})}, X _ {1} \equiv \frac {X (d _ {C 2} - d _ {O 2})}{h _ {O 2} - h _ {C 2}}, X _ {2} \equiv \frac {X (d _ {E 2} - d _ {C 2})}{h _ {C 2} - h _ {E 2}}, \\ X _ {3} \equiv \frac {X (d _ {E 2} - d _ {O 2})}{h _ {O 2} - h _ {E 2}}. \end{array}
$$

We derive the best responses for Firm 2, given Firm 1’s openness levels when $X _ { 2 } > X _ { 3 } > X _ { 1 }$ . In order for O to be a dominant strategy for Firm 2, we need $\Pi _ { P O 2 } > \operatorname* { m a x } ( \Pi _ { P C 2 } , \Pi _ { P E 2 } ) , \Pi _ { E O 2 } > \operatorname* { m a x } ( \Pi _ { E C 2 } , \Pi _ { E E 2 } )$ , Π > max(Π , Π ), and $\Pi _ { O O 2 } > \operatorname* { m a x } ( \Pi _ { O C 2 } , \Pi _ { O E 2 } )$ . We find that these inequalities of Firm 2 objective functions hold when the following conditions (along with second-order conditions and nonnegativity conditions) are satisfied, $\begin{array} { r } { \gamma > \frac { 2 { \ 0 } \lambda } { 8 } , ~ d _ { O 2 } < d _ { C 2 } < d _ { E 2 } , ~ h _ { O 2 } > h _ { C 2 } > h _ { E 2 } , X _ { 2 } > X _ { 3 } > X _ { 1 } } \end{array}$ and $s _ { 2 } > X _ { 3 }$ . Similarly, we find that $\Pi _ { P E 2 } > \operatorname* { m a x } ( \Pi _ { P C 2 } , \Pi _ { P O 2 } ) , \Pi _ { E E 2 } > \operatorname* { m a x } ( \Pi _ { E C 2 } , \Pi _ { E O 2 } ) , \Pi _ { C E 2 } > \operatorname* { m a x } ( \Pi _ { C C 2 } , \Pi _ { C O 2 } ) , \mathrm { a n d } \Pi _ { O E 2 } > \operatorname* { m a x } ( \Pi _ { O C 2 } , \Pi _ { O O 2 } )$ holds when $X _ { 2 } > X _ { 3 } >$ $X _ { 1 }$ and $s _ { 2 } < X _ { 3 }$ along with the other conditions presented above.

Next, we analyze the objective functions of Firm 2 to derive dominant strategies when $X _ { 1 } > X _ { 3 } > X _ { 2 }$ . Using simple algebra, we can show that when $s _ { 2 } > X _ { 1 } , 0$ is the dominant strategy for Firm 2, when $X _ { 2 } > s _ { 2 } > X _ { 2 }$ , C is the dominant strategy for Firm 2, and when $s _ { 2 } < X _ { 2 } ,$ E is the dominant strategy for Firm 2.

Note that apart from $X _ { 2 } > X _ { 3 } > X _ { 1 }$ and $X _ { 1 } > X _ { 3 } > X _ { 2 }$ other orderings of $X _ { 1 } , X _ { 2 } ,$ , and $X _ { 3 }$ are not feasible. Similarly, we follow the above steps to derive the dominant strategies of Firm 1. Following the steps mentioned in the outline of the proof of Proposition 1, we find Nash Equilibrium based on the best responses of Firms 1 and 2.

## Appendix B

## Detailed Proofs

In this section, we provide detailed proofs of Proposition 1 and Proposition 2.

## Proof of Proposition 1

In the following subsections, we derive the best response strategies for a firm given its competing firm’s open source strategy.

We make the following definitions: $\pmb { { \cal D } } \equiv \left( - \alpha R ^ { 2 } T \big ( c _ { i } + c _ { j } \big ) + c _ { i } c _ { j } T ^ { 3 } + \alpha ^ { 2 } R ^ { 2 } Z \right) ^ { 2 }$ , where

$$
R \equiv 2 \alpha \gamma - \beta \lambda , T \equiv 4 \alpha^ {2} - \beta^ {2}, Z \equiv \gamma^ {2} - \lambda^ {2}, \mathrm{and} M \equiv \beta \gamma - 2 \alpha \lambda .
$$

Below, we first derive Firm 2’s best response to Firm 1’s proprietary strategy.

Best Response of Firm 2 to Firm 1’s Proprietary Strategy: We first define threshold $\mathcal { Y } _ { \mathcal { R } 1 }$ below.

$$
\mathcal {Y} _ {\mathcal {R 1}} = \frac {\alpha c _ {2} (c _ {2} T ^ {2} - \alpha R ^ {2}) \big (c _ {1} T (2 \alpha (d _ {O 2} - d _ {P 2}) + h _ {O 2} R s _ {2}) - \alpha R (\gamma (d _ {O 2} - d _ {P 2}) + h _ {O 2} s _ {2} Z) \big)}{s _ {2} D} \times \frac {c _ {1} T (2 \alpha (d _ {O 2} + d _ {P 2}) + 2 \beta d _ {P 1} + h _ {O 2} R s _ {2}) - \alpha R (\gamma (d _ {O 2} + d _ {P 2}) + 2 d _ {P 1} \lambda + h _ {O 2} s _ {2} Z)}{s _ {2} D}.
$$

When the following conditions (along with second-order conditions and non-negativity conditions) are satisfied, $\begin{array} { r } { y _ { 2 } > y _ { \mathcal { R } 1 } , \gamma > \frac { 2 \alpha \lambda } { \beta } , d _ { O 2 } > } \end{array}$ $d _ { C 2 } > d _ { E 2 } ,$ , and $h _ { O 2 } > h _ { C 2 } > h _ { E 2 } ,$ , we find that $\Pi _ { P P 2 } > \Pi _ { P k 2 } , \forall k \in \{ O , C , E \}$ . In other words, when Firm 1 keeps its software proprietary, the Firm 2’s profits from Strategy P are greater than the profits from Strategy O, E, or C when $y _ { 2 } > \mathcal { Y } _ { \mathcal { R } 1 }$ . Next, when $y _ { 2 } < \mathcal { Y } _ { \mathcal { R } 1 }$ , it is easy to show that $\Pi _ { P P 2 } < \Pi _ { P k 2 }$ $\forall k \in \{ O , C , E \}$ . Further examining the relationship between $\Pi _ { P O 2 } , \Pi _ { P C 2 } ,$ , and $\Pi _ { P E 2 }$ , we find that $\Pi _ { P O 2 } > \Pi _ { P C 2 }$ and $\Pi _ { P O 2 } > \Pi _ { P E 2 }$ hold when $y _ { 2 } < \mathcal { Y } _ { \mathcal { R } 1 }$

In the next subsection, we derive Firm 2’s best response to Firm 1’s open strategy.

Best Response for Firm 2 to Firm 1’s Open Strategy: We define threshold $\mathcal { Y } _ { \mathcal { R } 4 }$ below.

$$
\mathcal {Y} _ {\mathcal {R 4}} = \frac {\alpha c _ {2} (c _ {2} T ^ {2} - \alpha R ^ {2}) \big (c _ {1} T (2 \alpha (d _ {O 2} - d _ {P 2}) + h _ {O 2} R s _ {2}) - \alpha R (\gamma (d _ {O 2} - d _ {P 2}) + h _ {O 2} s _ {2} Z) \big)}{s _ {2} D} \times \frac {c _ {1} T (2 \alpha (d _ {O 2} + d _ {P 2}) + 2 \beta d _ {O 1} + h _ {O 2} R s _ {2} + 2 h _ {O 1} M s _ {1}) - \alpha R (\gamma (d _ {O 2} + d _ {P 2}) + 2 d _ {O 1} \lambda + h _ {O 2} s _ {2} Z)}{s _ {2} D}.
$$

When the following conditions (along with second-order conditions and non-negativity conditions) are satisfied $\begin{array} { r } { y _ { 2 } > y _ { \mathcal { R } ^ { 4 } } , \gamma > \frac { 2 \alpha \lambda } { \beta } , d _ { O 2 } > } \end{array}$ $d _ { C 2 } > d _ { E 2 }$ , and $h _ { O 2 } > h _ { C 2 } > h _ { E 2 }$ , we find that $\Pi _ { O P 2 } > \Pi _ { O k 2 } , \forall k \in \{ O , C , E \}$ . In other words, when Firm 1’s makes its software fully open source, the profits from Strategy P are greater than the profits from Strategy O, E, or C for Firm 2 when $y _ { 2 } > \mathcal { Y } _ { \mathcal { R } 4 }$

Next, when $y _ { 2 } < \mathcal { Y } _ { \mathcal { R } 4 }$ , it is easy to show that $\Pi _ { O P 2 } < \Pi _ { O k 2 } , \forall k \in \{ O , C , E \}$ . Examining the relationship between $\Pi _ { O O 2 } , \Pi _ { O C 2 }$ , and $\Pi _ { O E 2 } ;$ we find that $\Pi _ { O O 2 } > \Pi _ { O C 2 }$ ?????? $\Pi _ { O O 2 } > \Pi _ { O E 2 }$ hold when $y _ { 2 } < \mathcal { Y } _ { \mathcal { R } 4 }$

In the next subsection, we derive Firm 1’s best response to Firm 2’s proprietary strategy.

Best Response for Firm 1 to Firm 2’s Proprietary Strategy: We define threshold $\mathcal { Y } _ { \mathcal { C } 1 }$ below:

$$
\mathcal {Y} _ {\mathcal {C} 1} = \frac {\alpha c _ {1} (c _ {1} T ^ {2} - \alpha R ^ {2}) \big (c _ {2} T (2 \alpha (d _ {O 1} - d _ {P 1}) + h _ {O 1} R s _ {1}) - \alpha R (\gamma (d _ {O 1} - d _ {P 1}) + h _ {O 1} s _ {1} Z) \big)}{s _ {1} D} \times \frac {c _ {2} T (2 \alpha (d _ {O 1} + d _ {P 1}) + 2 \beta d _ {P 2} + h _ {O 1} R s _ {1}) - \alpha R (\gamma (d _ {O 1} + d _ {P 1}) + 2 d _ {P 2} \lambda + h _ {O 1} s _ {1} Z)}{s _ {1} D}.
$$

When the following conditions (along with second-order conditions and non-negativity conditions) are satisfied $\begin{array} { r } { , y _ { 1 } > y _ { \mathcal { C } 1 } , \gamma > \frac { 2 \alpha \lambda } { \beta } , d _ { O 1 } > } \end{array}$ $d _ { C 1 } > d _ { E 1 }$ , and $h _ { O 1 } > h _ { C 1 } > h _ { E 1 }$ , we find that $\Pi _ { P P 1 } > \Pi _ { k P 1 } , \forall k \in \{ O , C , E \}$ . That is, when Firm 2 keeps its software proprietary, the profits from Strategy P are greater than the profits from Strategy O, E, or C for Firm 1 when $y _ { 1 } > y _ { \mathcal { C } 1 }$ . Next, when $y _ { 1 } < \mathcal { Y } _ { \mathcal { C } 1 }$ , we find $\Pi _ { P P 1 } <$ $\Pi _ { k P 1 } , \forall k \in \{ O , C , E \}$ }. Further examining the relationship between $\Pi _ { O P 1 } , \Pi _ { C P 1 }$ , and $\Pi _ { E P 1 } ,$ , we find that $\Pi _ { O P 1 } > \Pi _ { C P 1 }$ and $\Pi _ { O P 1 } > \Pi _ { E P 1 }$ hold when $y _ { 1 } < \mathcal { Y } _ { \mathcal { C } 1 }$

FIRM 2

In the next subsection, we derive Firm 1’s best response to Firm 2’s open strategy.

Best Response for Firm 1 to Firm 2’s Open Strategy: We define threshold ${ \mathcal { Y } } _ { { \mathcal { C } } _ { 4 } }$ below.

$$
\mathcal {Y} _ {\mathcal {C 4}} \equiv \frac {\alpha c _ {1} (c _ {1} T ^ {2} - \alpha R ^ {2}) (c _ {2} T (2 \alpha (d _ {O 1} - d _ {P 1}) + h _ {O 1} R s _ {1}) - \alpha R (\gamma (d _ {O 1} - d _ {P 1}) + h _ {O 1} s _ {1} Z))}{s _ {1} D} \times \frac {c _ {2} T (2 \alpha (d _ {O 1} + d _ {P 1}) + 2 \beta d _ {P 2} + h _ {O 1} R s _ {1} + 2 h _ {O 2} M s _ {2}) - \alpha R (\gamma (d _ {O 1} + d _ {P 1}) + 2 d _ {P 2} \lambda + h _ {O 1} s _ {1} Z)}{s _ {1} D}.
$$

When the following conditions (along with second-order conditions and non-negativity conditions) are satisfied, $\begin{array} { r } { y _ { 1 } > y _ { \mathcal { C } 4 } , \gamma > \frac { 2 \alpha \lambda } { \beta } , d _ { O 1 } > } \end{array}$ $d _ { C 1 } > d _ { E 1 }$ , and $h _ { O 1 } > h _ { C 1 } > h _ { E 1 }$ , we find that $\Pi _ { P O 1 } > \Pi _ { k O 1 } , \forall k \in \{ O , C , E \}$ . In other words, when Firm 2 keeps its software proprietary, the profits from Strategy P are greater than the profits from Strategy O, E, or C for Firm 1. Next, when $y _ { 1 } < \mathcal { Y } _ { \mathcal { C } 4 } ,$ it is easy to show that $\Pi _ { P O 1 } < \Pi _ { k O 1 } , \forall k \in \{ O , C , E \}$ . Further examining the relationship between $\Pi _ { O O 1 } , \Pi _ { C O 1 }$ , and $\Pi _ { E O 1 }$ , we find that $\Pi _ { O O 1 } > \Pi _ { C O 1 }$ and $\Pi _ { O O 1 } >$ $\Pi _ { E O 1 }$ hold when $y _ { 1 } < \mathcal { Y } _ { \mathcal { C } 4 }$

In a similar way, we can derive the best response for Firm 1 (2) to Firm $2 \mathrm { { \dot { s } } } \left( 1 \mathrm { { \dot { s } } } \right)$ partial openness strategies (E and C). We find that the best response strategy for Firm 1 (Firm 2) to Firm 2’s (Firm 1’s) Strategy C or E is either P or O. Hence, partial openness cannot be an equilibrium solution for the case considered in this proposition.

Deriving the best response functions of firms corresponds to underlining the following strategies in the normal form of the game. In Figure B1, we see the Nash Equilibrium emerges when the strategies of both firms are underlined within each cell. The interpretation of the below graph leads to the conditions presented in Proposition 1.

We summarize the results thus far below.

1. Symmetric Equilibria

a. (??, ??) when $y _ { 1 } > y _ { \mathcal { C } 1 }$ and $y _ { 2 } > \mathcal { Y } _ { \mathcal { R } 1 } ;$

b. (??, ??) when $y _ { 1 } < \mathcal { Y } _ { \mathcal { C } 4 }$ and $y _ { 2 } < \mathcal { Y } _ { \mathcal { R } 4 } ;$

2. Asymmetric Equilibria

a. (??, ??) when $y _ { 1 } < \mathcal { Y } _ { \mathcal { C } 1 }$ and $y _ { 2 } > \mathcal { Y } _ { \mathcal { R } 4 } ;$

b. (??, ??) when $y _ { 1 } > y _ { \mathcal { C } 4 }$ and $y _ { 2 } < \mathcal { Y } _ { \mathcal { R } 1 }$

<table><tr><td></td><td>OPEN(Column 4)</td><td>CORE OPEN(Column 3)</td><td>EXTENSIONOPEN(Column 2)</td><td>PROPRIETARY(Column 1)</td></tr><tr><td rowspan="4">FIRM 1</td><td> $\underline{\text{(O,O)}}$ </td><td> $\underline{\text{(O,C)}}$ </td><td> $\underline{\text{(O,E)}}$ </td><td> $\underline{\text{(O,P)}}$ </td></tr><tr><td>CORE OPEN(Row 3)</td><td> $\underline{\text{(C,O)}}$ </td><td> $\underline{\text{(C,C)}}$ </td><td> $\underline{\text{(C,E)}}$ </td></tr><tr><td>EXTENSION OPEN(Row 2)</td><td> $\underline{\text{(E,O)}}$ </td><td> $\underline{\text{(E,C)}}$ </td><td> $\underline{\text{(E,E)}}$ </td></tr><tr><td>PROPRIETARY(Row 1)</td><td> $\underline{\text{(P,O)}}$ </td><td> $\underline{\text{(P,C)}}$ </td><td> $\underline{\text{(P,E)}}$ </td></tr></table>

Figure B1. Nash Equilibrium Solutions

## Proof of Proposition 2

Previously in Appendix A, we showed the dominant strategies of Firm 2. Before deriving the Nash equilibrium (i.e., the pair of best responses for Firm 1 and Firm 2), we obtain the dominant strategies of Firm 1. Following the steps explained in Proposition 1, we get the following results.

When ${ Z _ { 2 } } > { Z _ { 3 } } > { Z _ { 1 } }$ and

$\mathbf { } s _ { 1 } > Z _ { 3 } , \mathbf { } O$ is the dominant strategy for Firm 1,

$\pmb { s _ { 1 } } < \pmb { Z _ { 3 } }$ , ?? is the dominant strategy for Firm 1,

where thresholds $\mathbf { Z _ { 1 } } , \mathbf { Z _ { 2 } }$ , and $\mathbf { Z } _ { 3 }$ are given below:

$$
Z \equiv \frac {\alpha (\beta \gamma \lambda + 8 \alpha^ {2} c _ {2} - 2 \beta^ {2} c _ {2} - 2 \alpha \gamma^ {2})}{(2 \alpha \gamma - \beta \lambda) (- \alpha \gamma^ {2} + \alpha \lambda^ {2} + 4 \alpha^ {2} c _ {2} - \beta^ {2} c _ {2})}, Z _ {1} \equiv \frac {X (d _ {C 1} - d _ {O 1})}{h _ {O 1} - h _ {C 1}}, Z _ {2} \equiv \frac {X (d _ {E 1} - d _ {C 1})}{h _ {C 1} - h _ {E 1}}, Z _ {3} \equiv \frac {X (d _ {E 1} - d _ {O 1})}{h _ {O 1} - h _ {E 1}}.
$$

Similarly, when $Z _ { 1 } > Z _ { 3 } > Z _ { 2 }$ and

$s _ { 1 } > Z _ { 1 } , O$ is the dominant strategy for Firm 1;

$Z _ { 1 } > s _ { 1 } > Z _ { 2 } ,$ , ?? is the dominant strategy for Firm 1; and

$s _ { 1 } < Z _ { 2 } ,$ ?? is the dominant strategy for Firm 1.

The equilibrium solutions presented in the proposition are the pairs of best responses for Firms 1 and 2.

## Utility Function-Based Demand Model

We assume that the consumer’s preferences are uniformly distributed on an interval [0,1], with $0 < \Theta < 1$ representing consumers’ perceptional distance from Product 1 of Firm 1 and (1 − θ) denoting the perceptional distance from Product 2 of Firm 2. Considering a normalized market (and denoting customer mass with D), the utility of customer of type θ is represented as $U _ { 1 } = u _ { 1 } - \Theta - a _ { 1 } p _ { 1 } + g _ { 1 } x _ { 1 }$ and $U _ { 2 } = u _ { 2 } - ( 1 - \Theta ) - a _ { 2 } p _ { 2 } + g _ { 2 } x _ { 2 }$ for products of Firms 1 and 2, respectively. In the above utility functions, $u _ { i }$ denotes a customer’s baseline utility for firm $i \forall i \in \{ 1 , 2 \}$ (we assume it is large enough that the market is covered), $p _ { i }$ denotes the price of firm ??’s software, $a _ { i }$ denotes the price sensitivity for firm $i , x _ { i }$ denotes the quality of the software of firm ??, and $g _ { i }$ captures customer’s sensitivity to the quality of firm ??’s product. Based on the above setup, we derive the location of the indifferent consumer as $\theta ^ { * } = 1 / 2 ( 1 + u _ { 1 } - u _ { 2 } - a _ { 1 } p _ { 1 } + a _ { 2 } p _ { 2 } + g _ { 1 } x _ { 1 } -$ $g _ { 2 } x _ { 2 } )$ . Thus, consumers located between 0 and $\boldsymbol { \theta } ^ { \ast }$ on the Hotelling line purchase Product 1, and the remaining consumers purchase Product 2.

The demand for Product 1 can be easily derived as follows: $\begin{array} { r } { q _ { 1 } = \frac { D ( 1 + u _ { 1 } - u _ { 2 } - a _ { 1 } p _ { 1 } + a _ { 2 } p _ { 2 } + g _ { 1 } x _ { 1 } - g _ { 2 } x _ { 2 } ) } { 2 } { } _ { l } } \end{array}$ , and the demand for Product 2 is $q _ { 2 } =$ $\frac { D ( 1 - u _ { 1 } + u _ { 2 } + a _ { 1 } p _ { 1 } - a _ { 2 } p _ { 2 } - g _ { 1 } x _ { 1 } + g _ { 2 } x _ { 2 } ) } { 2 }$ . The demand functions that we derived using the Hotelling model approach correspond to the aggregate demand function presented in the manuscrip $( \mathrm { e . g . } , q _ { 1 } = ( d _ { k 1 } - \alpha p _ { 1 } + \beta p _ { 2 } + \gamma x _ { 1 } - \lambda x _ { 2 } )$ , where $\begin{array} { r } { \alpha = \frac { D a _ { 1 } } { 2 } , \beta = \frac { D a _ { 2 } } { 2 } , \ \gamma = \frac { D g _ { 1 } } { 2 } , \lambda = \frac { D g _ { 2 } } { 2 } } \end{array}$ , and the baseline demand, $\begin{array} { r } { d _ { k 1 } = \frac { D \left( 1 + u _ { 1 } - u _ { 2 } \right) } { 2 } } \end{array}$ for Product 1).

## Appendix C

## Empirical Study Description

In this section, we investigate whether vulnerabilities in open source software environments are fixed faster than their proprietary counterparts. We collected data on 605 vulnerabilities of both closed source (i.e., proprietary) and open source software. The vendors used for this study are SUN, Apache, Apple, Google, IBM, Microsoft, Mozilla, MySQL, Oracle, PHP, and Ruby-on-Rails (ROR). The information about vulnerabilities is collected from the National Vulnerabilities Database (https://nvd.nist.gov/), Common Vulnerabilities and Exposures Website (https://cve.mitre.org/), and the websites of vendors. The variables used in this analysis are summarized in Table C1.

<table><tr><td colspan="4">Table C1. Data Summary</td></tr><tr><td>Variable name</td><td>Type</td><td>Values</td><td>Statistics</td></tr><tr><td>Resolving days</td><td>Numeric</td><td>17-1198 days</td><td>Mean = 128.97, SD = 113.92</td></tr><tr><td>Software type</td><td>Classified</td><td>Open source (0), Closed source (1)</td><td>% open: 85.62 % closed source: 14.38</td></tr><tr><td>Severity level</td><td>Numeric</td><td>1 to 10</td><td>Mean = 7.12, SD = 1.96</td></tr><tr><td>Access complexity</td><td>Classified</td><td>Low, medium, high</td><td>% low: 40, % medium: 56 % high: 4%</td></tr><tr><td>Vendor</td><td>Classified</td><td>SUN, Apache, Apple, Google, IBM, Microsoft, Mozilla, MySQL, Oracle, PHP, Ruby-on-Rails (ROR)</td><td></td></tr></table>

The dependent variable resolving days indicates the number of days taken by a vendor to resolve a particular vulnerability. It is calculated by subtracting the reported vulnerability date in the National Vulnerabilities Database (NVD) from the date the vulnerability patch is availabl on the vendor’s website. The variable software type defines the type of software associated with the vulnerability (open source or closed source). The software type is the main independent variable in our model, which is converted into a dummy variable for the analysis. The variable severity level measures the severity level of vulnerability (denoted by NVD as CVSS scores). This is defined by a numeric number between 1 and 10. In addition to CVSS scores, the NVD also provides severity rankings of low, medium, and high. However, these qualitative ratings are simply mapped from the numeric CVSS scores. Specifically, the severity level for a vulnerability is labeled as follows: (1) low if it has a CVSS score of 0.0-3.9, (2) medium if it has a CVSS score of 4.0-6.9, and (3) high if it has a CVSS score of 7.0-10.0. Since these two measures are equivalent, we consider only numeric values in our analysis

The variable access complexity measures the complexity of the attack required to exploit the vulnerability once an attacker gains access to the target system. For example, consider a buffer overflow in an internet service: Once the target system is located, the attacker can launch an exploit at will. Other vulnerabilities, however, may require additional steps in order to be exploited. For example, a vulnerability in an email client is only exploited after the user downloads and opens a tainted attachment. The possible values for this metric are: high, medium, and low. A high value indicates that the specialized access conditions exist. For example, the attacking party must already have elevated privileges or spoof additional systems in addition to the attacking system (e.g., DNS hijacking). A medium value indicates that the access conditions are somewhat specialized. For example, the attacking party is limited to a group of systems or users at some level of authorization, possibly untrusted. Finally, a low value indicates that the specialized access conditions or extenuating circumstances do not exist. In this case, the affected product typically requires access to a wide range of systems and users, possibly anonymous and untrusted (e.g., internet-facing web or mail server). The attack can be performed manually and requires little skill or additional information gathering.

The variable vendor indicates the name of the vendor associated with the software for which the vulnerability is reported. For a given software vendor, there may be different software in our dataset. Further, a given vendor may have both closed source and open source software. Table C2 summarizes the number of observations and types of software for each vendor in our dataset. As can be seen, for most of the software vendors in our dataset, the software type is either open source or closed source. However, two vendors (Apple and Oracle) have both open source and closed source software in our dataset. The variables severity level, access complexity, and vendor serve as control variables in our regression model.

<table><tr><td colspan="3">Table C2. Types of Software for Different Vendors</td></tr><tr><td>Name of the vendor</td><td>Number of observations</td><td>Types of software</td></tr><tr><td>Apple</td><td>240</td><td>Open source and closed source</td></tr><tr><td>Google</td><td>138</td><td>Open source</td></tr><tr><td>PHP</td><td>48</td><td>Open source</td></tr><tr><td>SUN</td><td>45</td><td>Open source</td></tr><tr><td>Microsoft</td><td>45</td><td>Closed source</td></tr><tr><td>Apache</td><td>34</td><td>Open source</td></tr><tr><td>Mozilla</td><td>20</td><td>Open source</td></tr><tr><td>Oracle</td><td>17</td><td>Open source and closed source</td></tr><tr><td>Ruby-on-Rails (ROR)</td><td>9</td><td>Open source</td></tr><tr><td>MySQL</td><td>8</td><td>Open source</td></tr><tr><td>IBM</td><td>1</td><td>Closed source</td></tr><tr><td>Total</td><td>605</td><td></td></tr></table>

## Model and Results

The dependent variable in our model is resolving days and the key independent variable is the software type (open source or closed source). We operationalize software type as a dummy variable: 0 for open source and 1 for closed source. We also employ several control variables: severity, access complexity, and vendor. The basic empirical model we test is:

$$
R e s o l v i n g D a y s = \psi_ {0} + \psi_ {1} S o f t w a r e T y p e + \psi_ {2} S e v e r i t y + \psi_ {3} A c c e s s C o m p l e x i t y + \gamma V e n d o r d u m m y + \epsilon .
$$

The variable access complexity with three categories, low, medium, and high, is operationalized with two dummy variables: ACH and ACM. When the access complexity is high (resp., medium), ACH (resp., ACM) is equal to 1. In order to overcome potential vendor-specific effects on the relationship between software type and resolving days, we consider several operationalizations of vendor as follows:

(a) To evaluate whether vendors who report vulnerabilities more frequently exhibit a distinct and different relationship, we categorize frequent vendors as ones with more than 30 observations in our dataset. As can be seen in Table C2, the following six vendors are in this category: Apache, Apple, Microsoft, Google, PHP, and SUN. Table C3 presents the regression results for all vendors and for frequent vendors.

(b) We introduce vendor-specific dummy variables to capture vendor effects through the intercept term. Table C4 presents the regression results for all vendors and for frequent vendors.

(c) While the above specification does capture vendor-specific effects, it does so only through the intercept term. In such a specification all other variables are assumed to exhibit similar relationships with the dependent variable. This assumption is evaluated through an analysis of one vendor, Apple, which reported 240 vulnerabilities with both open source and closed source software. The regression results are presented in Table C5.

<table><tr><td colspan="3">Table C3. Regression Results for All Vendors and Frequent Vendors</td></tr><tr><td></td><td>All vendors</td><td>Only frequent vendors</td></tr><tr><td colspan="3">Main variable</td></tr><tr><td>Closed dummy</td><td>30.50(13.63)**</td><td>41.53(14.57)***</td></tr><tr><td colspan="3">Control variables</td></tr><tr><td>Severity</td><td>-14.41(2.49)***</td><td>-16.64(2.79)***</td></tr><tr><td>ACH dummy</td><td>-5.58(24.99)</td><td>-17.15(26.60)</td></tr><tr><td>ACM dummy</td><td>-7.95(9.54)</td><td>-18.61(10.33)*</td></tr><tr><td>Intercept</td><td>231.83(18.95)***</td><td>254.61(21.23)***</td></tr><tr><td>Model fit:  $R^2(F-value)$ </td><td>0.060(9.48)</td><td>0.072(10.60)</td></tr></table>

Note: Standard errors are in brackets. \*\*\*: significant at p = 0.01, \*\*: significant at p = 0.05, \*: significant at p = 0.10

<table><tr><td colspan="3">Table C4. Regression Results with Vendor-Specific Dummy Variables</td></tr><tr><td></td><td>All vendors</td><td>Only frequent vendors</td></tr><tr><td colspan="3">Main variable</td></tr><tr><td>Closed dummy</td><td>48.65(17.21)***</td><td>53.49(18.65)***</td></tr><tr><td colspan="3">Control variables</td></tr><tr><td>Severity</td><td>-7.12(2.52)***</td><td>-7.53(2.78)***</td></tr><tr><td>ACH dummy</td><td>32.05(23.48)</td><td>32.36(25.21)</td></tr><tr><td>ACM dummy</td><td>0.98(11.06)</td><td>1.58(11.84)</td></tr><tr><td>VendorApple dummy</td><td>2.12(34.40)</td><td>-149.17(20.78)***</td></tr><tr><td>VendorGoogle dummy</td><td>73.09(34.41)**</td><td>-77.14(21.41)***</td></tr><tr><td>VendorIBM dummy</td><td>-61.12(106.39)</td><td>-</td></tr><tr><td>VendorMicrosoft dummy</td><td>4.63(40.37)</td><td>-150.27(30.60)***</td></tr><tr><td>VendorMozilla dummy</td><td>70.93(41.00)*</td><td>-</td></tr><tr><td>VendorMySQL dummy</td><td>45.08(48.91)</td><td>-</td></tr><tr><td>VendorPHP dummy</td><td>63.96(36.18)*</td><td>-86.88(23.78)***</td></tr><tr><td>VendorOracle dummy</td><td>-77.31(41.44)*</td><td>-</td></tr><tr><td>VendorSun dummy</td><td>-71.31(36.83)*</td><td>-221.41(25.29)***</td></tr><tr><td>VendorApache dummy</td><td>151.56(37.60)***</td><td>-</td></tr><tr><td>Intercept</td><td>144.04(37.10)***</td><td>297.09(24.03)***</td></tr><tr><td>Model Fit: R2(F-value)</td><td>0.256(14.48)</td><td>0.237(18.60)</td></tr></table>

Note: Standard errors are in parentheses. \*\*\*: significant at $p { = } 0 . 0 1 , ^ { \star \star }$ : significant at $p { = } 0 . 0 5 , \cdots$ significant at $p { = } 0 . 1 0$

The results consistently reveal that the software type impacts the time to resolve the vulnerability. Hence, when the software type is closed source, it takes longer to resolve the vulnerability (compared to open source software). A robust low-end estimate of 30 additional days fo resolution for the closed source (i.e., proprietary) software is an important insight from the analysis. The results also show that the coefficient for severity is negative and significant across the different model specifications. Thus, more severe vulnerabilities appear to be resolved faster. This result can be explained by the fact that software vendors usually exert extra effort to resolve more severe vulnerabilities. Finally, we found that the dummy variables for access complexity are mostly insignificant (except in two scenarios where it registers significance at p = 0.10). This result implies that the complexity of the attack required to exploit the vulnerability has little bearing on the time to resolve the vulnerability.

<table><tr><td colspan="2">Table C5. Regression Results for Apple</td></tr><tr><td></td><td>Coefficients</td></tr><tr><td colspan="2">Main variable</td></tr><tr><td>Closed dummy</td><td>62.28(18.58)***</td></tr><tr><td colspan="2">Control variables</td></tr><tr><td>Severity</td><td>-12.38(4.12)***</td></tr><tr><td>ACH dummy</td><td>74.75(50.22)</td></tr><tr><td>ACM dummy</td><td>-38.36(23.05)*</td></tr><tr><td>Intercept</td><td>216.68(31.58)***</td></tr><tr><td>Model fit:  $R^{2}$ (F-value)</td><td>0.12(8.04)</td></tr></table>

Note: Standard errors are in parentheses. \*\*\*: significant at p = 0.01, \*\*: significant at p = 0.05, \*: significant at $p { = } 0 . 1 0$
