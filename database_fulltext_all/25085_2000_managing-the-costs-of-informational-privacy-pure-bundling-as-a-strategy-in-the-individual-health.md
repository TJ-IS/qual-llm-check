---
otero_id: 25085
otero_key: "J4K84ERN"
title: "Managing the Costs of Informational Privacy: Pure Bundling as a Strategy in the Individual Health Insurance Market"
authors: "Matt E. Thatcher; Erik K. Clemons"
year: "2000"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2000.11045639"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Managing the Costs of Informational Privacy: Pure Bundling as a Strategy in the Individual Health Insurance Market

Matt E. Thatcher & Erik K. Clemons

To cite this article: Matt E. Thatcher & Erik K. Clemons (2000) Managing the Costs of Informational Privacy: Pure Bundling as a Strategy in the Individual Health Insurance Market, Journal of Management Information Systems, 17:2, 29-57

To link to this article: http://dx.doi.org/10.1080/07421222.2000.11045639

![](/api/attachments/J4K84ERN/fulltext/images/1b6f8dbeb62957a7c1294fc612d0a91924e4108c890f70cd15c7c9d927f91610.jpg)

Published online: 09 Jan 2015.

![](/api/attachments/J4K84ERN/fulltext/images/f2fdc64370e2d947de69b15bed6323507150fe7a29d2de0c5d99189401131eb5.jpg)

Submit your article to this journal

![](/api/attachments/J4K84ERN/fulltext/images/412cce4814c5dc5e5472116d75ab1c5bd2ed478360f03fe06866999c14080e7a.jpg)

Article views: 23

![](/api/attachments/J4K84ERN/fulltext/images/11090fa580b82a77d084aded0585b78c6255ae11cc22c6414c208a46ec3825c1.jpg)

View related articles

# Managing the Costs of Informational Privacy: Pure Bundling as a Strategy in the Individual Health Insurance Market

MATT E. THATCHER AND ERIC K. CLEMONS

MATT E. THATCHER is Assistant Professor of Management Information Systems at the Eller College of Business and Public Administration at University of Arizona, where he has been a member of the faculty since 1997. He holds a B.S. in economics and an M.A. and Ph.D. in information technology from the Wharton School of the University of Pennsylvania. His research examines the economic impacts of information technology (IT) on industry and firm performance, the economic impacts of informational privacy on consumer welfare, the strategic uses of information, and financial decision-making for IT investments. His current teaching includes courses on information systems design and implementation and user interface design and evaluation for undergraduate students, and a course on financial decision-making for IT investments for M.B.A. students.

For biographical information on ERIC K. CLEMONS see the Guest Editors’ Introduction

ABSTRACT: Advances in genetic testing and data mining technologies have increased the availability of genetic information to insurance companies and insureds (applicants and policy holders) in the individual health insurance market (IHIM). Regulators, concerned that insurance companies will use this information to discriminate against applicants who have a genetic risk factor but who are still healthy, have implemented genetic privacy legislation in at least 18 states. However, in previous work we have demonstrated that such legislation will have unintended consequences— it will reduce consumer participation in the market without making those remaining better off. This paper identifies a mechanism, a pure bundling strategy, that insurance companies may implement in this regulatory environment to restore (or maximize) consumer participation in the market and to discourage such discrimination among insureds. This problem is examined through System Dynamics, a simulation-based modeling technique. The results will have significant implications for policy designs implemented by insurance companies, and for legislation implemented by industry regulators, and therefore, for the insurability of the individuals that rely on this market for health insurance coverage.

KEY WORDS AND PHRASES: bundling, information privacy, insurance markets, insur ance policy, privacy, privacy cost

Genetic testing has tremendous potential in the world of medicine. As the science develops, so will the public’s concern over its impact on society. As the legislation develops, so will our industry’s interest in its effect on our business. Our challenge becomes learning how to manage the issue, helping people get the protection they need at a fair price, while ensuring the future viability of the insurance industry. [23, p. 63]

ADVANCES IN BIOLOGICAL RESEARCH AND GENETIC TESTING TECHNOLOGIES continue to provide applicants for individual health insurance and their doctors with more accurate assessments of their personal risk for a growing number of medical conditions. In addition, advances in data warehousing and data mining technologies allow insurance companies in the individual health insurance market (IHIM) to access inexpensively and to manage effectively the growing amounts of applicant information, including genetic information, made available to them. This, in turn, has enabled these insurance companies to develop more accurate assessments of applicant risk as well. However, industry regulators are concerned that health insurance companies will use applicants’ genetic information, acquired through genetic testing or data mining efforts, to discriminate against those who are at higher risk for developing specific medical conditions, but who are presently in good health.

In response to this concern, state and federal legislators have proposed and implemented genetic privacy legislation that prevents insurance companies from denying coverage to, or setting higher rates for, applicants who are genetically predisposed to certain medical conditions. This informational privacy legislation is intended to accomplish three goals:

 protect the consumers’ rights to privacy

 increase consumer participation in the IHIM (toward universal coverage)

 improve the equity of premiums paid by insureds (i.e., individuals participating in the market)

Indeed, politicians and legislators continue to espouse these three goals when ad dressing the health care issue. However, our previous research demonstrates that under certain conditions such privacy legislation, while well-intended, will actually reduce both consumer participation and product affordability in this market [8, 9, 36]. These results are counterintuitive, and therefore counter to social trends.

This paper will extend our previous findings by further examining the social costs imposed upon an IHIM when applicants for health insurance coverage possess pri vate information regarding their personal risk for a large number of medical conditions. In particular, this paper will examine how the product set (i.e., types of insurance policies) offered by insurance companies to individuals in a regulated IHIM wil affect three factors: (1) the extent to which the population is insured, (2) the equity of premiums paid by insureds, and (3) the viability of the IHIM. Consistent with our previous work in this area, we will use System Dynamics, a simulation-based modeling technique, to explore these complex and dynamic issues [8, 9, 35, 36].

Our findings will demonstrate that it may be possible to attain universal coverage and premium equity in the IHIM despite the presence of extreme information asym metries (i.e., genetic privacy legislation) by offering only one policy to consumers, a comprehensive insurance policy, at a fixed price. This strategy may be referred to as a pure bundling strategy. The laws of statistics ensure that, under certain assump tions, individuals’valuations for a large bundle of medical coverages (e.g., a compre hensive insurance policy) will converge to a single value. Therefore, as long as individuals in the market are risk-averse (and they have no other policy options available to them) they will rationally choose to purchase the comprehensive policy, resulting in universal coverage at equitable premiums. Assuming this result holds under baseline model assumptions, the sensitivity of this result to changes in model parameters will be explored.

The structure of this paper is as follows. The following section presents a more detailed overview of the problem. The next two sections review relevant literature in the areas of insurance economics and product bundling. We then introduce a measure, market participation, that will be used to evaluate the efficiency of market outcomes in our models. We next present the assumptions and structure of the baseline model used to examine the impact of policy design decisions on market efficiency. Then we explain the methodology, System Dynamics, used to examine these issues. The results are then presented. Finally, we conclude the paper and discuss areas of future research.

## Problem Overview

WHILE MOST AMERICANS OBTAIN THEIR HEALTH INSURANCE COVERAGE through employee-sponsored group plans or government-sponsored programs such as Medicare and Medicaid, a significant minority purchases their insurance individually for themselves and their family [19]. (See Appendix for a definition of insurability.)<sup>1</sup> These participants in the IHIM primarily rely upon their own resources to obtain information about insurance options available in the market and to finance their health coverage.<sup>2</sup> In addition, structural changes in the workforce and changes in demographics suggest that a growing proportion of the population will come to rely primarily on the IHIM for their health coverage in the future [14, 18].<sup>3</sup> Within this growing market, there are two costs that threaten the insurability of individuals and the viability of the industry: the public cost of private information and the distributional cost of public information. This paper examines the trade-offs between these two costs and identifies a strategy (i.e., a policy design) for eliminating both from the market.

The public cost of private information is the reduction in consumer participation from adverse selection in the presence of informational asymmetries between insurance providers and insurance applicants. When regulators prohibit insurance companies from engaging in precise differential pricing, the alternative is uniform pricing across nonidentical populations, called pools or communities. When individuals possess private information regarding their personal risk for incurring medical costs and insurance companies are forced to engage in community rating, individuals who are at lower risk will determine that they are being overcharged and will choose to remain uninsured.

The public cost of private information may be eliminated in this market by making applicants’private information publicly available and by allowing insurance compa nies to engage in differential pricing strategies (or risk classification). However, such risk classification introduces an adverse distributional cost into the market. That is, by making information public, premiums across applicants are no longer equitable since each applicant is now paying a premium based on his own risk status. This inequity may be considered unfair by regulators in the IHIM, especially if the inequity is based on factors over which individuals have no control—for example, their genetic predispositions. This inequity represents the distributional cost of public information.

Information technology (IT) is rapidly increasing the amount and accuracy of genetic information available to individuals and insurance companies in the IHIM. Advances in biological and genetic research have helped to identify genetic components of various diseases such as Alzheimer’s, breast cancer, cystic fibrosis, Huntington’s, and Tay Sachs, as well as those associated with nontraditional diseases such as mental illness, obesity, and alcoholism [21, 25, 26, 28]. For example, studies now show that mutations of the P53 gene are closely associated with the development of the many types of cancer, including ovarian, colonic, pulmonary, and testicular cancers [3]. Other studies show that women who inherit mutations of the BRCA–1 or BRCA–2 genes are more likely to develop breast cancer than those who do not [4, 8, 21].<sup>4</sup> In addition, researchers have recently discovered two hereditary genetic mutations that appear to help provide resistance to the AIDS virus [31, 33].<sup>5</sup> Researchers have even discovered genetic mutations that result in the inability to put suffixes (-s, -ed, -er) onto words [3].

This growing knowledge of human genetics, combined with rapid advances in technology, has enabled researchers to develop tests, based on DNA and chromosome analysis, that can determine if individuals possess genetic mutations that may in crease their chances of developing certain medical conditions [3, 9]. For example, Affymetrix has developed a technology called GeneChip that, through DNA analysis, identifies whether or not an individual is genetically predisposed to certain types of cancer and other medical conditions [3].<sup>6</sup> Genetic tests such as GeneChip may help individuals more accurately assess their propensity for acquiring certain medical conditions and therefore of incurring the associated treatment costs.

In the absence of state or federal regulation, insurance companies will attempt to price insurance policies based on available genetic information. In fact, advances in data warehousing technologies have enabled insurance companies to more easily and cheaply collect and store growing amounts of applicant information, including genetic test results, family history, medical history, and consumption behaviors that may be correlated with applicant risk.<sup>7</sup> Through data mining efforts insurance companies may be able to infer individuals’risk based on this information [7, 37].<sup>8</sup> However, using these inferences to engage in differential pricing introduces a distributional cost into the market, since individuals may be charged different premiums (or offered different amounts of coverage) based solely on their genetic dispositions, over which they have no control.

Regulators in the IHIM are concerned with promoting fairness by eliminating the distributional costs associated with insurance discrimination based on genetic infor mation. Their intuition is to accomplish this goal by denying insurance companies access to individuals’genetic information. In fact, regulators in at least 18 states (including New Jersey, New York, Vermont, Arizona, and Georgia) have passed genetic privacy legislation that prevents health insurance companies from denying coverage to, or setting higher rates for, applicants who are genetically predisposed to certain medical conditions, but who are presently in good health [19, 21, 22, 26]. Similar legislation is still pending in at least 14 other states.

Unfortunately, this genetic privacy legislation substitutes one form of unfairness for another. That is, this legislation eliminates the distributional cost of public infor mation, but it simultaneously introduces a public cost of private information. It wil encourage individuals at lower risk, who are now unable to signal their risk status to insurance companies, to opt out of the market, without providing any incremental benefit to those remaining in the market. This phenomenon is explored more fully in our previous work [8, 9, 36]. The problem addressed in the remainder of this paper is to identify a strategy (or a policy design) that insurance companies may implement to manage effectively the trade-offs between these two costs, or eliminate both costs altogether.

## Insurance Economics Literature

PREVIOUS LITERATURE IN THE AREA OF INSURANCE ECONOMICS has attempted to address different aspects of this problem. Work in the area of insurance economics has acknowledged that the presence of private information (or asymmetric information) in a market may lead to an adverse selection problem and, in the worst case, complete market collapse. Much of this literature has focused on the development of pricing strategies and policy designs to mitigate the costs of adverse selection (or the public cost of private information) in insurance markets where applicants possess private information about their propensity to incur a single specified loss. One stream of literature suggests that insurance companies may use price-quantity contracts (i.e., contracts that specify both the premium rate for the policy and the amount of coverage provided by the policy) as a screening mechanism to reduce the public cost of private information [15, 19, 20, 26].<sup>9</sup> Another stream of literature suggests that insurance companies may reduce the public cost of private information by offering tailored products to individuals based on individual characteristics (e.g., demographics such as age, or consumption patterns such as smoking) that are correlated with individuals risk [6, 11, 24, 32]. Unfortunately, both policy designs examined in these literatures reduce (but do not eliminate) the public cost of private information. In addition, they do so by introducing a distributional cost into the market; that is, in these models, individuals pay different premiums or receive different amounts of coverage based on their risk status. Therefore, their implementation in the IHIM will not lead to universal coverage; furthermore, their use may violate commonly held norms about fairness, especially if this discrimination is based on genetic information.

A third stream of literature is concerned with designing mechanisms that balance economic efficiency and equity within an insurance market. Tabarrok [34] examines genetic testing in the context of health insurance markets. He identifies a mechanism, genetic insurance, which he claims may eliminate both the public cost of private information and the distributional cost of public information.<sup>10</sup> However, his concept of genetic insurance would only work if participation in the market could be made mandatory and universal; otherwise it is prone to the same adverse selection effects of the IHIM that it is intended to correct.<sup>11</sup> Thus, it is infeasible in today’s IHIM.

In the following sections, we will develop a model that more accurately portrays the characteristics of the IHIM and examine an alternative, feasible strategy that will balance economic efficiency and equity (i.e., eliminate both the public cost of private information and the distributional cost of public information) in the IHIM.

## Bundling Literature

THE MECHANISM PROPOSED TO ELIMINATE BOTH COSTS IMPOSED UPON the IHIM (and generate universal coverage at equitable premiums) is termed a pure bundling strategy. Under a pure bundling strategy, a seller of a set of products would offer to sell buyers the entire set of products at a fixed price. Pure bundling essentially repre sents a “take it or leave it” offer in which buyers either decide to purchase the complete bundle of products at that fixed price or decide to purchase no products at all. The idea behind pure bundling is that it may be possible, under certain conditions, to make individuals who are heterogeneous in their valuations for a single product ho mogeneous in their valuations for a large bundle of products.<sup>12</sup>

Recent literature in information technology has focused on the use of pure bundling strategies to maximize profits of a monopoly seller of multiple goods with zero marginal costs. Bakos and Brynjolfsson find that when marginal costs are very low, consumer valuations for the goods are of comparable value, and the correlation in demand for different goods is low, a multiproduct monopolist may use a pure bundling strategy to increase profits, reduce consumer surplus, and reduce dead weight losses [2].<sup>13</sup> However, these authors acknowledge that regulators in the digital goods industry may be opposed to the implementation of any bundling strategy that is de signed to maximize profits by minimizing consumer surplus.

The problem addressed in this paper is complementary to, but critically different from, that addressed by Bakos and Brynjolfsson. We demonstrate that it may be possible to use a pure bundling strategy to attain universal coverage (or maximize consumer participation/consumer surplus) in a regulated IHIM (where marginal profits to sellers is zero) in which insurance companies offer coverage for a large number of medical conditions. Unlike previous models in the IT literature, in our model the marginal cost to insurance companies of providing coverage to consumers is high compared to consumers’ valuations for coverage.<sup>14</sup>

IN THE FOLLOWING SECTIONS, we attempt to solve the problem of maximizing market participation in a regulated IHIM with high marginal costs by having applicants valuations for a large number of goods (i.e., coverages for medical conditions) converge to a single value. As we will see, the findings will provide valuable insights into legislative policy and firm strategy.

The parameters to be explored in the model include:

 The number of diseases to be included in the bundle, to make individuals who are heterogeneous in their valuations for specific medical conditions sufficiently homogeneous in their valuations for a large bundle of medical conditions, to entice all individuals to purchase the bundled insurance policy.

 The impact of varying the distribution of risk types for each medical condition on the sustainability of the bundling solution.

 The impact of the presence of coverage for catastrophic medical conditions on the sustainability of the bundling solution.<sup>15</sup>

In order to evaluate the likelihood that a pure bundling strategy will meet the stated objectives, we first must identify an appropriate construct to measure the economic efficiency of alternative market outcomes. Consumers purchase products because they perceive that the purchase makes them better off. In our context, consumers purchase individual health insurance policies to off-load their financial risk (i.e., the potential treatment costs associated with acquiring poor health) to a neutral third party—the insurance company. In the traditional economics literature, the measure used to assess the aggregate benefit (net of costs) that consumers obtain from the purchasing of products in a market is consumer surplus.<sup>16</sup>

However, the purchase of insurance coverage generates a positive externality within the IHIM, which is not captured by modeling consumer surplus. That is, individuals who choose to remain uninsured may be less able, or less willing, to receive appropriate treatment for medical conditions in the future. This would be of particular concern for regulators if these medical conditions were contagious and could be spread throughout the population if not treated. This could have a very adverse effect on overall health care costs. However, universal coverage reduces the threat of epidemic by allowing all individuals to have access to necessary medical treatment.<sup>17</sup>

Since the consumer surplus measure does not account for the positive externalities associated with universal health insurance coverage, we introduce an alternative measure, market participation, which does. Market participation is defined as the per centage of outcome risk present in the population (or potential market) that is actually covered by health insurance. The market participation measure provides ordina rankings of alternatives consistent with those implied by the consumer surplus measure (as we will see later). However, it also accounts for the positive externalities discussed above and gives a clear and unambiguous metric for determining how closely we approach the goal of universal coverage (or full market participation). Therefore, this measure provides insurance companies and regulators with a more meaningful interpretation on which to base their decisions.

## Model

## Baseline Model Assumptions

## Assumptions About the Medical Conditions:

 There are N types of medical conditions in this world, the risks of which are independently and identically distributed (i.i.d.).<sup>18</sup>

 Each of the N conditions has a genetic component.

 The treatment cost, C, for each condition is known and fixed.

## Assumptions About the Individuals:

 Individuals are potential consumers of health-care products and services.

 Individuals are endowed with a genetic endowment; that is, individuals are endowed with either a high-risk status (H) or a low-risk status (L) for each of the N conditions through a set of N independent and identical Bernoulli trials.<sup>19</sup>

 The probability that a low-risk individual will develop condition j (where $j \in N )$ is represented by $p _ { { } _ { L } } ,$ the probability that a high-risk individual will develop con dition j is represented by $p _ { H } ,$ where $0 < { p } _ { L } < { p } _ { H } < 1$ . These probabilities are fixed and are not altered by individuals’ behaviors, eliminating the need to address moral hazard in this model.

 Individuals are perfectly informed, through a set of free and perfectly accurate genetic tests, about their risk status for each condition.

 Individuals are identical in every aspect except in their probability of developing each condition (and of therefore incurring the treatment costs associated with each).

 Individuals each possess the same underlying von Neumann–Morgenstern utility function for wealth, specified as $U ( W ) = - e ^ { - r W }$ , where r is the risk aversion parameter and W represents the individual’s wealth. The exponential utility function exhibits constant absolute risk aversion (CARA) as defined by Arrow [1].

 Individuals make insurance purchasing decisions that maximize their own expected utility.

## Assumptions About the Insurance Company:

 The model considers a single, risk-neutral insurance company participating in a regulated insurance market in which genetic privacy legislation has been passed and implemented. That is, in this model the insurance company cannot observe the individuals’ risk types. Therefore, individuals have an information advantage over the insurance company.

 However, population statistics are common knowledge. That is, the insurance company can observe:

— the population distribution of risk types, where the proportion of individuals at high risk for each condition is represented by $\lambda _ { _ H }$ and the proportion at low risk is represented by $( 1 - \lambda _ { _ { H } } )$

— the probabilities that each risk type will acquire a medical condition, $p _ { { _ H } }$ and $p _ { { _ L } } .$

 The insurance company engages in a pure bundling strategy; that is, the company offers to the market only one insurance policy, a bundled policy providing coverage for all N medical conditions at a single premium.

 The insurance company engages in actuarially fair pricing based on the claims experience for the policy; that is, the insurance company sets the premium for the policy in each period to the level that would have enabled the company to break even in the previous period had that premium been charged.

## Model Structure

Individuals:

 Enter the IHIM.

 Observe a free and perfectly accurate genetic test for each of the N conditions, which identifies the individual as either high-risk or low-risk for each condition.

 Observe the premium of the bundled insurance policy offered by the insurance company that period.

 Based on all available information (the realization of their risk status and the policy premium prevailing in the market), decide whether to purchase the policy offered in the market or remain uninsured, based on maximizing their own expected utility.

 Remain healthy or experience occurrences of illness during the period, after which, those with both illness and insurance coverage file claims.

## The Insurance Company:

 Observes the insurable population (i.e., $\lambda _ { { } _ { H } } , p _ { { } _ { H } }$ , and $p _ { { _ L } } )$ .

 Offers a bundled insurance policy to the market (where the initial premium of fered to the market is based on population statistics).

 Collects revenues from premiums.

 Pays claims and adjusts premiums as claims are filed.

In the model we track four outcome measures for each period: (1) percentage of individuals that purchase insurance, (2) market participation, (3) consumer surplus, and (4) premium rate.

## Methodology

PREVIOUS WORK IN THE AREA OF INSURANCE ECONOMICS typically uses closed-form analytics to examine methods to manage the cost of private information in an insur ance market in which individuals face a single risk. However, closed-form analytic solutions, when considering a more realistic insurance market in which individuals face a large number of risks for which they seek coverage, cannot capture the dy namic behaviors of the market. Due to the complexity and dynamic characteristics of the problem, we use simulation techniques to examine the issues presented in the model.

More specifically, as we saw in the previous section, the IHIM belongs to a class of social systems that Jay Forrester calls multiloop nonlinear feedback loops.<sup>20</sup> He introduces an approach, termed System Dynamics, that can lead to better understanding of these dynamic social systems and to more effective development of corporate and governmental policies for the future [15, 16, 17].<sup>21</sup> System Dynamics is essentially a simulation-based modeling technique that begins with populations or pools (e.g., communities or pools of individuals with similar personal risk), transitions among pools (e.g., purchasing decisions, realizations of illness), and determinants of rates of flow of populations among pools (e.g., levels of risk aversion, population statistics, and repricing decisions). Rates of flow can be based upon any information in the model, including previous rates of flow or size of pools and perceived differences among them. It is this ability to have flows influence pools, which in turn influence flows, that allows System Dynamics to capture complex and nonlinear behavior of systems over time.<sup>22</sup> We use this simulation technique to examine the model of the IHIM presented under the heading “Model.” The appendix presents the details of the implementation of the simulation.

## Results

TABLE 1 PRESENTS THE INITIAL PARAMETERS used to explore the model discussed under the heading “Model” and used to generate the findings presented in this section. Based on these initial parameters:

1. The actuarially fair premium to insure an individual at high risk for a medical condition against losses associated with that medical condition is:

$$
P _ {\text { ActuariallyFair,HR }} = p _ {H} * C = 0. 2 0 * 1 0 0 = 2 0
$$

2. The actuarially fair premium to insure an individual at low risk for a medical condition against losses associated with that medical condition is:

$$
P _ {\text { ActuariallyFair,LR }} = p _ {L} * C = 0. 0 5 * 1 0 0 = 5
$$

3. The actuarially fair premium for the population of an insurance policy that covers N medical conditions is:

$$
\begin{array}{r l} P _ {\text {ActuariallyFair}} & = \left[ \lambda_ {H} * p _ {H} + (1 - \lambda_ {H}) * p _ {L} \right] * C * N \\ & = [ 0. 1 0 (0. 2 0) + 0. 9 0 (0. 0 5) ] * 1 0 0 * N = 6. 5 N \end{array}
$$

In the following section, we examine the effect of varying N, the number of medi cal conditions covered in the bundled insurance policy, on four measures: (1) the percentage of individuals that choose to purchase the insurance policy, (2) market participation, or percentage of outcome risk covered in the market, (3) consumer surplus, and (4) premium rate (per condition covered by the policy) paid by insureds. Then we examine the sensitivity of the results to changes in $\lambda _ { H } ,$ or the distribution of risk types in the population. Then we examine the sensitivity of the results to the inclusion of coverage for a single, catastrophic medical condition in the bundled insurance policy.

Table 1. Initial Model Parameters

<table><tr><td> $\lambda_H$ </td><td>0.10</td></tr><tr><td> $p_H$ </td><td>0.20</td></tr><tr><td> $p_L$ </td><td>0.05</td></tr><tr><td>C</td><td>100</td></tr></table>

Note: For each medical condition: $\lambda _ { \scriptscriptstyle H } = \mathrm { p r o p o r t i o n }$ of individuals at high risk for that condition, $p _ { H } = { \mathrm { p r o b a b i l i t y } }$ a high-risk individual will incur the medical condition, $p _ { L } = \mathrm { p r o b a b i l i t y }$ a lowrisk individual will incur the medical condition, and C = the cost to treat each medical condition. Individuals’ risk status for each condition is determined through a set of N independent and identical Bernoulli trials where the probability of being endowed as high risk for a condition is $\lambda _ { \scriptscriptstyle H }$ and the probability of being endowed as low risk for a condition is $( 1 - \lambda _ { \scriptscriptstyle H } )$ . Once an individual’s risk status is determined, he is endowed with the appropriate probability of acquiring the medical condition, either ${ \underline { { p _ { H } \ { \mathrm { ~ O r ~ } } p _ { L } } } } .$

## Varying the Number of Medical Conditions Covered in the Bundled Insurance Policy (N)

Figures 1 through 3 show how increasing N, the number of medical conditions covered in the bundled insurance policy, affects the efficiency of the IHIM and the pre mium rate paid by insureds when the insurance company engages in a pure bundling strategy:

 Figure 1 shows how the percentage of individuals covered in the market and market participation change as N varies.<sup>23</sup> In particular, it shows that as N increases, the proportion of applicants choosing to purchase the bundled policy and the proportion of outcome risk covered in the market both increase. That is, assuming the insurance company engages in a pure bundling strategy, market efficiency (normalized to account for the bundle size) increases monotonically with $N . ^ { 2 4 }$

 Figure 2 shows that consumer surplus, the third measure of market efficiency, also increases monotonically with $N . ^ { 2 5 }$

 Figure 3 shows that the premium rate (i.e., the premium per condition included in the bundle) paid by insureds decreases as N increases.<sup>26</sup>

Figures 1 through 3 also show that as the number of conditions covered in the bundle, N, becomes “sufficiently large,” the market approaches full market efficiency (i.e., universal coverage and full market participation) and the premium rate for the bundled policy approaches the actuarially fair rate for the population. The result is a full market participation pooling equilibrium. These results hold even if insureds possess perfect, private information regarding their risk for each of the N conditions.<sup>27</sup> A pure bundling strategy such as this—which encourages market participation at lower premiums, allows individuals to maintain their privacy, and does not threaten the viability of the insurance industry—would likely receive regulatory and public encouragement in today’s IHIM.

![](/api/attachments/J4K84ERN/fulltext/images/ba26990689301c728bea4c1fcab118b98cfb46e280e4ff013c9d9d37cfde82d5.jpg)  
Number of conditions included in the bundle

Figure 1. As N increases, market efficiency, as measured by the percent of individuals covered by the bundled insurance policy and by market participation, increases. As N becomes sufficiently large (i.e., N = 80 in this case), the market approaches universal coverage (i.e., ful market participation).  
![](/api/attachments/J4K84ERN/fulltext/images/02ff169da7e50ada7d0c26b6f39b03d5618ae3454a939e039cd1f49b2d5b433f.jpg)  
Number of conditions included in the bundle  
Figure 2. As N increases, market efficiency, as measured by consumer surplus (per medical condition per individual), increases.

The intuition behind these results is that as the number of conditions covered in the bundle increases, individuals, who are heterogeneous in their risk exposure to each condition, become homogenous in their risk exposure to the entire bundle of conditions. Figure 4 demonstrates that as N increases, individuals’ expected treatment costs associated with acquiring the N conditions converge to a single value, the average expected treatment costs for the population (i.e., 6.5 per condition). This suggests that for large N individuals’ expected treatment costs, and therefore their valuations for a bundled insurance policy, converge: That is, the variance of these expectations across the population decreases as N increases, making individuals more homogeneous in their valuations for large bundles of insurance coverage (e.g., comprehensive coverage). This phenomenon, which makes individuals homogeneous and which generates pooled universal coverage (and full market participation) as N becomes sufficiently large, simultaneously eliminates the adverse selection problem and the distributional costs from the market.

![](/api/attachments/J4K84ERN/fulltext/images/6a537e172ba9453db76fdb6a025ce4656fd0c2fb90fadaaa5f238e1821e0df38.jpg)  
Number of conditions included in the bundle  
Figure 3. As N increases, the premium rate charged per medical condition for the bundled insurance policy decreases. As N becomes sufficiently large (i.e., N = 80 in this case), the premium rate approaches the actuarially fair rate for the population (i.e., 6.5).

These results suggest that under a wide range of conditions an insurance company engaging in a pure bundling strategy may maximize market efficiency and lower premiums in the presence of extreme informational asymmetries by offering a single comprehensive health insurance policy to the market. If the insurance company instead decides to offer many policies in the market, each covering a small number of conditions, it will likely lead to a reduction in market efficiency and an increase in the premium rate paid by insureds, without making the insurance company any better off.

## Proportion of Risk Types in the Population $( \lambda _ { _ { H } } )$

Market efficiency under a pure bundling strategy will depend somewhat on the proportion of high-risk individuals present in the population for each of the medical conditions. Figure 5 shows the percentage of applicants participating in the market when varying the size of the bundled policy and the proportion of applicants at high risk for acquiring each condition covered in the policy. This figure shows that if the proportion of high-risk applicants present in the market is sufficiently small then all applicants will purchase the bundled policy regardless of the size of the bundle. The intuition behind this result is that the presence of a very small number of high-risk individuals in the population will adversely affect the average loss and thus the policy premium charged by the insurance company, but it will do so only slightly. Assuming sufficient (and reasonable) levels of risk aversion, those individuals who are at lower risk will be willing to accept the initial rate offered by the insurance company per coverage rather than remain uninsured, even though this rate is slightly higher than their own actuarially fair rate.<sup>28</sup>

![](/api/attachments/J4K84ERN/fulltext/images/c0882cd42a999bc7031251bfd37fcc1292911155350a0894708bd0fcf548070d.jpg)

2 N<sup>=</sup>  
![](/api/attachments/J4K84ERN/fulltext/images/b6510772f480af709c527482651c3ed0ed890e400d6fcb0382f4e5741fdc44b7.jpg)

![](/api/attachments/J4K84ERN/fulltext/images/02019d7200c024f72d1f0383127951ee2be2ed6163ca9a1e5fee3b638641e3c2.jpg)  
=<sup>1</sup>

![](/api/attachments/J4K84ERN/fulltext/images/927d15e4acc901034ce02bcba12fb22d3b7c2044e93ee09089e93c909a2e0ed5.jpg)  
<sub>iguresho</sub>w<sup>sthatindivid</sup>

![](/api/attachments/J4K84ERN/fulltext/images/ab95518b9ed73648468f50f11b5d2ce1a81232d9f24bee2394560bb1821a361d.jpg)  
Proportion of In dividuals at High Risk for Each Medical Condition  
Figure 5. This figure shows, consistent with the previous analysis, that for a given $\lambda _ { \scriptscriptstyle H }$ (the proportion of high-risk individuals), market efficiency increases as N increases. However, it also shows that for extreme values of $\lambda _ { { \scriptscriptstyle H } }$ the bundle size required to generate full market participation is relatively small. For example, when $\lambda _ { \scriptscriptstyle H } < . 1 0$ all individuals in the market will decide to purchase an insurance policy covering N medical conditions even when N is small $( \mathbf { e } . \mathbf { g } . , N = 5 )$ ). Similarly, when $\lambda _ { { \scriptscriptstyle H } }$ approaches 1, the percent of individuals deciding to purchase the bundled policy approaches 100% even for small bundle sizes. However, for intermediate values of $\lambda _ { { \scriptscriptstyle H } }$ the number of medical conditions covered by the insurance policy will have a significant impact on market efficiency (or the percent of individuals that purchase the policy).

Similarly, if the proportion of high-risk individuals is sufficiently high, a full market participation pooling solution can again be attained with a relatively small bundle size because in this case individuals are already initially very homogeneous in their valuation for insurance coverage. In the extreme case, in which everyone in the population is high-risk with certainty, individuals’valuations will be identical. Therefore, if the proportion of high-risk individuals is sufficiently high, full market participation may be generated and sustained even when N (the bundle size) is small.

However, if the proportion of high-risk individuals lies in between these “suffi cient” values, then the market participation and the resulting premium will depend heavily on the number of conditions covered in the bundle, as shown in the preceding section. That is, when the proportion of high-risk individuals does lie within this region and N is relatively small, the presence of high-risk applicants adversely affects the premium to such an extent that lower-risk applicants decide to opt out of the market and remain uninsured rather than pay the premium offered in the market. This leads to a reduction in market efficiency. Should those individuals at lower risk opt out, the premium of the bundled policy prevailing in the market is higher than the actuarially fair rate for the entire population, reflecting the risk (and thus the resulting claims loss experience) of those higher-risk individuals that purchase the policy.

Therefore, as the proportion of high-risk individuals present in the IHIM tends toward the extreme values (i.e., either 0% high-risk or 100% high-risk), individuals in the population have a more homogeneous risk profile. Their valuations for a bundle of insurance coverages will converge faster, requiring a smaller bundle size to encourage a high level of market participation, and therefore a lower premium rate. However, if the proportion of high-risk individuals is moderate, meaning individuals are more heterogeneous in their risk for each medical condition, the level of market participation and the level of insurance premiums prevailing in the market will depend heavily on N, the number of conditions covered in the bundle. As shown in the preceding section, a larger N will be required to make individuals that are heterogeneous in their valuation for single coverage more homogeneous in their valuation for comprehensive coverage.

## Presence of a Catastrophic Medical Condition

Up to this point, we have considered a bundled insurance policy that provides coverage for a large number of i.i.d. medical conditions. However, insurance companies have recently become very concerned about providing insurance coverage for catastrophic medical conditions—that is, conditions that occur with low probability but that have very high associated treatment costs. AIDS and many types of cancer may be considered catastrophic conditions when compared to other health care conditions, such as broken arms and common viral infections. The concerns of insurance companies about providing coverage for catastrophic conditions has been heightened by advances in genetic testing that enable individuals to acquire private information regarding their risk for many such diseases [31, 33]. One concern is that individuals who know themselves to be at low risk for certain low-probability, highconsequence conditions may opt out of the insurance market altogether to avoid paying what may be considered unfair premiums when compared to their overall level of risk.

Therefore, in this section we consider a population of applicants that are at risk for acquiring a set of (N – 1) i.i.d. medical conditions about which they are perfectly informed as described in Table 1. However, in this section we also assume that each applicant has some risk of acquiring a single, catastrophic condition. The parameters characterizing this catastrophic disease are presented in Table 2.

Under these assumptions, we observe that the high cost associated with treating the single catastrophic condition does have a significant impact on the results found two sections earlier; that is, we find that including coverage for a catastrophic condition in the bundled policy will actually encourage applicants to purchase the policy and in duce a full market participation pooling equilibrium in which all applicants purchase the policy at a premium that is actuarially fair for the entire population. This result may appear counterintuitive to many insurance providers, who fear private informa tion related to catastrophic conditions will lead to an adverse selection problem. However, to the contrary, this model demonstrates that including such catastrophic conditions in the bundled policy will actually encourage, not deter, universal cover age at actuarially fair rates for the population.

Table 2. Parameters for the Catastrophic Medical Condition

<table><tr><td> $\lambda_{H,Cat}$ </td><td>0.10</td></tr><tr><td> $p_{H,Cat}$ </td><td>0.05</td></tr><tr><td> $p_{L,Cat}$ </td><td>0.001</td></tr><tr><td> $C_{Cat}$ </td><td>1000</td></tr></table>

The intuition behind this result is that the risk premium that individuals are willing to pay in order to obtain health coverage depends heavily on the size of the potential treatment cost (as well as the probability of incurring this cost). Individuals are typically more willing to pay a higher risk premium to avoid an uncertain catastrophic loss than to avoid an uncertain noncatastrophic loss (even if the expected costs of both losses are the same). A higher willingness to pay for catastrophic coverage will lead to a higher willingness to pay for a bundled insurance policy that includes coverage for that catastrophic condition than for a policy that does not. As a result, under a pure bundling strategy, including catastrophic conditions in the bundled policy will increase market participation and encourage the attainment of universal coverage. This result appears to be robust under a pure bundling strategy under a wide range of parameter assumptions.

However, we should discuss two caveats. The first caveat is that an adverse selection problem may exist in this environment if the difference in risk between those applicants at high risk for acquiring the catastrophic condition and those at low risk is extremely large. This adverse selection problem exists in our model when high-risk individuals are 750 times more likely to acquire the catastrophic condition than those at low risk. In that case, those individuals at low risk will determine that they are being overcharged so much for the bundled insurance policy that they will choose to opt out of the market and remain uninsured, while those at high risk for the catastrophic condition will continue to purchase coverage.

The second caveat is that an adverse selection problem may exist if insurance companies are able to offer an exclusion policy—a policy that covers individuals for all medical conditions except for a specified condition or set of conditions—along with the bundled policy in this environment. Assume that the regulated insurance company offers two policies in this market: a comprehensive policy and an exclusion policy that covers all medical conditions except for the catastrophic condition. In our model, if those individuals at high risk for the catastrophic condition are less than 450 times at risk than those at low risk (given parameter values), then the solution found in the case of pure bundling still holds. However, if those individuals at high risk for the catastrophic condition are more than 450 times at risk than those at low risk, then the pooling solution will be broken. That is, under these conditions low-risk individuals will purchase the exclusion policy, while high-risk individuals will continue to purchase the comprehensive policy.

These findings suggest that for some intermediate values (e.g., when high risks are 450 to 750 times more likely to acquire the catastrophic condition), a policy that provides comprehensive coverage will have universal appeal to applicants, as long as the exclusion policy is not offered. Therefore, legislation such as the Kennedy– Kassebaum health care reform bill, which prevents insurance companies from offering such exclusion policies, should be encouraged in this environment. That is, allowing individuals to pick and choose which conditions to insure will actually lead to a reduction in coverage and market participation.

## Conclusions

IN THIS PAPER WE ADDRESSED THE PROBLEM of attaining universal coverage in a regulated IHIM in which applicants for health coverage possess private information about their propensity to acquire a large number of medical conditions. In particular, we examined the conditions under which it may be possible to attain universal coverage at equitable premiums (i.e., a full market participation pooling equilibrium) in the IHIM by having insurance companies engage in a pure bundling strategy. Furthermore, we examined the robustness of this result to key parameter assumptions and to the case where insurance companies may offer an exclusionary insurance policy along with the comprehensive coverage policy. More specifically, we found that it may be possible to attain universal coverage at equitable premiums in the IHIM if insurance companies engage in a pure bundling strategy. This result is strengthened:

 as N, the number of conditions covered by the bundled insurance policy, in creases.

 if the proportion of individuals at high risk for acquiring each condition tends toward extreme values (i.e., 0% or 100%).<sup>29</sup>

 by including coverage for catastrophic (i.e., low-probability, high-consequence) conditions in the bundled insurance policy.

Addressing this problem of maximizing market participation is becoming increasingly important due to recent advances in technology and changes in regulatory policies in the IHIM because the presence of private information destroys risk pooling. This work provides significant contributions to existing research in the areas of insurance economics and information technology and has significant implications for firm strategy and regulatory policy in the IHIM.

## Directions for Future Research

THIS PAPER MAKES SUBSTANTIAL CONTRIBUTIONS to our understanding of the behavior of insurance applicants in insurance markets where decision-makers face both the presence of a large number of diseases and extreme differences in information endowment. Thus, the model studied corresponds quite closely to the situation actually faced by decision-makers in these markets, whether applicants, insurance company executives, or industry regulators. However, the following extensions would make the model even more robust, and we plan to explore their implications in subsequent work:

 Heterogeneity in risk aversion: As the model is currently constructed, all consumers have the same risk aversion: That is, all consumers are assumed to have the same exponential form of risk aversion, and to have the same parameters. This may lead to artificially coordinated lock-step behavior, much as the use of the same computer programs among portfolio traders has on occasion led to rapid and coupled behavior in financial markets. We believe that allowing consumers to employ different risk aversion parameters would actually make our solutions more stable and thus more robust, while making our models more realistic.

Heterogeneity in probability distributions for underlying diseases: As the model is currently constructed, all medical conditions are assumed to be independent, and all distributions for medical conditions are assumed to be i.i.d. However, in practice many diseases are strongly correlated, and thus an individual who is at high risk for adult onset diabetes would also be at risk for kidney failure, cardiovascular and circulatory problems, vision problems, and other medical conditions. Relaxing the i.i.d assumptions would increase the differences among consumers and would make the solutions we derive less stable than the ones presented here, while once again making our models more realistic.

 Heterogeneity in wealth: As the model is currently constructed, all consumers have the same wealth, and thus there are no “clipping effects” caused by insuf ficient wealth to purchase insurance.

 Empirical support: As the model is currently constructed, we have no formal empirical support, either for our assumed probability distributions, or for our assumptions concerning actual consumer behavior.

## NOTES

1. In a survey performed by the United States General Accounting Office (GAO) in 1996, it was estimated that 10.4 million individuals under 65 years of age (about 4.5 percent of the nonelderly population) relied on the IHIM as their only source of health coverage during 1994. Another 8.6 million nonelderly Americans either: (1) supplemented their employer-sponsored or government sponsored health coverage with individual coverage plans, or (2) purchased coverage in the individual market for part of the year and purchased coverage through their employer or the government during another part of the year (but did not hold the plans simultaneously). This paper will focus on those individuals who rely solely on the IHIM for their health coverage.

2. Participants in the IHIM not only identify and evaluate the multiple health insurance products offered by multiple insurance providers in this market, but also must obtain and finance the coverage on their own. This differs significantly from employment-based group plans in which employers generally evaluate options for their employees and obtain, administer, and largely finance the employer-sponsored coverage. In employer-sponsored health coverage plans, individuals and employers share the premium costs of the coverage; employers typically pay for 80% of an employee’s premium rate (70% for family coverage), leaving the remainder to be covered out-of-pocket by the employee [19]. Alternatively, participants in the

IHIM must pay the entire premium for coverage out-of-pocket. Therefore, the issue of affordability has been of paramount importance in the IHIM.

3. Although a wide range of individuals participate in the IHIM, a study by the GAO deter mined that the primary participants in the market include:

 Part-time, temporary, or contract workers who are not eligible for health insurance coverage through their employers. According to studies performed by the Employee Benefit Research Institute (EBRI), use of these types of workers—who are typically not offered employment-based health benefits—in the labor force is increasing, while the degree of unionization in the labor force is decreasing [18]. These structural changes in the workforce imply that a growing number of individuals will likely rely on the IHIM for their health coverage in the future.

 Early retirees who no longer have employment-based coverage and are not yet eligible for Medicare. In 1994, nearly 10 percent of retirees aged 64 or younger had individual insurance as the sole source of health coverage [12, 19]. This number is expected to increase in the future for three primary reasons. First, the individual market is becoming increasingly important for early retirees because fewer employers are providing health coverage for these individuals as they make the transition toward Medicare coverage [20]. Recent trends for insurance companies have been to provide less financing for retiree benefits, to increase the level of copayments and deductibles for which retirees are responsible, or to faze out retiree benefits altogether. Second, there have recently been proposals to increase the Medicare eligibility age from 64 to 67 [12]. These changes would significantly affect individuals’retirement decisions and would likely increase the number of individuals that rely on the IHIM for coverage. Third, according to EBRI President Dallas Salisbury, “the near elderly are projected to grow from 8.0 percent of the total population in 1995 to 12.9 percent in 2020” [14]. With baby boomers nearing retirement age, with employers reducing retiree benefits (e.g., health coverage benefits), and with legislators attempting to increase the age for Medicare eligibility, more and more near elderly individuals will come to rely on the IHIM for coverage.

 Self-employed people, people whose employers do not offer health insurance coverage, people not in the labor force, and people who lose their jobs and have exhausted, or are ineligible for continuation of, their employer-sponsored coverage.

4. Testing for a cancer gene is different than for other disease-causing genes. With a condition like Huntington’s disease, detection of a single gene for the illness means that the disease will strike. With cancer, on the other hand, finding an abnormal gene means you are one hit closer than a person without the gene to contracting the cancer in question—not that you will automatically develop a malignant tumor [39].

5. The AIDS virus enters human cells with the help of proteins called receptors. Researchers have noted that some individuals with unusual resistance to AIDS have two copies of a gene mutation—called Delta 32—in the two copies of the gene that makes the protein receptors called CCR5. The latest discovery found that people may also be resistant if they have another mutation, named m303, in one CCR5 gene copy and Delta 32 in the second CCR5 gene copy.

6. Affymetrix works as follows. DNA is extracted from a person’s blood and placed on the GeneChip, which is then inserted into an analyzer. A laser then scans the GeneChip and if the sample DNA matches the string of a known gene mutation that is built into the chip (i.e., stored in the database), it could mean that the patient is at greater risk for cancer.

7. A data warehouse is essentially a very large repository of historical data pertaining to a company and its customers. The promise of data warehousing is that data from disparate databases can be consolidated into a consistent and accurate form and managed from a single database. The notion of OLAP refers to the technique of performing complex analysis of the information stored in the data warehouse. OLAP technologies allow complex analytical queries on a database. These queries frequently aggregate and consolidate data. Such analysis facilitates decision-making for a company in many areas, including product choice and pricing.

8. Data mining technologies are statistical and logic tools that search through large databases (e.g., data warehouses) for hidden patterns, finding predictive information that experts may miss because it lies outside of their expertise or because it was previously too time-consuming to detect. Data mining tools help companies get more value out of their data warehouses by discovering patters, trends, and relationships among the data. Some tools used in data mining technologies include neural networks, decision trees, rule induction, and data visualization. A company called Trajecta sells data mining tools that help insurance companies more accurately predict which transactions are fraudulent, which policy holders are likely to leave for another insurer, and which marketing campaigns and products are appropriate for specific customer segments. Tools such as this are becoming more available to companies because high-speed systems have the power to perform data mining and other complex processes at speeds never before possible.

9. In these models, insurance companies typically induce individuals to sort themselves in risk classes by their choice of contracts. High risks select full insurance coverage at actuarially fair rates (calculated for the pool of high-risk individuals) while low risks select partial insurance coverage but at a lower average premium than that of high risks. The lower premium for low-risk individuals reflects both the lower degree of coverage and the lower average risk of applicants.

10. In his model, all individuals purchase genetic insurance at a single premium and then undergo genetic screening. Their genetic insurance policies will pay them the expected increase in health insurance premiums that would result from the conditions detected during their genetic screening. The fully public results of their testing would then determine the actual cost of their health insurance in an efficient market.

11. For example, individuals who do not observe a signal from their family or medical his tory regarding the presence of a genetic predisposition to certain medical conditions may find the genetic insurance overpriced and opt out of the market for genetic insurance.

12. This results by applying the law of large numbers and the Central Limit Theorem [2].

13. These authors suggest that this setting is consistent with the selling of digital information goods, which are essentially costless to reproduce and distribute and can be sold easily in large bundles.

14. In the IHIM the marginal cost for health coverage is the consumer’s expected medical costs. Consumers’ willingness to pay (or valuation) for this coverage will be only slightly higher due to the presence of risk aversion. Therefore, marginal costs are high relative to consumers’ valuations in this market.

15. Catastrophic conditions, defined as those conditions that have a low prior probability of occurrence but very high consequences (i.e., treatment costs) when acquired, presently pose a difficult problem for insurance companies. Companies are attempting to identify strategies that will allow them to provide health coverage to individuals for these catastrophic conditions in the presence of adverse selection. This analysis will provide some guidance.

16. Consumer surplus measures market efficiency in a competitive market where firms earn zero profits (i.e., producer surplus is zero).

17. In fact, a New York Times article discussed the public value, and social desirability, of universal inoculations [38]. The article claimed that:

Mass vaccination is without a doubt the greatest public-health triumph of the century. It has saved millions of lives, and prevented the crippling of countless others. . . . [The fact that] mass vaccination is among the cheapest and most effective ways to improve public health suggests that there are positive externalities associated with universal inoculations.

18. N is the key variable that varies in these models. Our goals is to examine the impact of the changes in N on economic efficiency and equity (and premium affordability) in the IHIM.

19. The binomial distribution better characterizes consumer valuations in the IHIM than those distributions investigated in previous literature (e.g., normal, uniform, etc.). That is, in the IHIM individuals are generally either high-risk or low-risk for acquiring certain medical conditions. For example, an individual either has the HIV virus or not; he either has a mutation of the P53 gene or not.

20. That is, in our model the insurance company adjusts premiums each period based on the claims history from the previous period. Individuals then make purchase decisions this in pe riod based on these adjusted premiums. These decisions then affect this period’s claims history which will affect the premiums charged by the insurance company next period, and so on. This represents a nonlinear interaction and a multiple-feedback loop. That is, the premium each period depends on the claims history from the previous period, which depends on individuals’purchasing decisions in the previous period, which depends on the premiums the previous period, etc. It is these dynamics that often lead to unexpected and unintended consequences.

21. In our previous work [8, 9, 36] System Dynamics typically demonstrate that laws, regulations, and programs designed by legislators, while well-intended, typically fail in their objectives and often create greater difficulties than those they tried to relieve. Such unintended consequences commonly occur because humans are unable to intuitively comprehend and to accurately predict the complex behavior of systems with nonlinear interactions and multiple-feedback loops.

22. Forrester used this technique to examine the dynamics of urban systems. In particular, he demonstrated how industry, housing, and people interact with each other as a city grows and decays, and the implications of this for governmental policies.

23. In Figure 1 N varies from 1 to 80.

24. When N = 1 (which is often referred to as pure unbundling in the literature) only 10% of the population (i.e., those individuals at high risk for the covered medical condition) purchases the insurance policy. This equilibrium results as follows:

1. The insurance company offers a policy at the actuarially fair rate for the population (i.e., 6.5) in period 0.

2. The high-risk individuals, valuing the policy at 20, will decide to purchase the policy.

3. The low-risk individuals, valuing the policy at 5, will find this policy too expensive given their low-risk status and will opt out of the market, assuming reasonable levels of risk aversion.

4. The insurance company will be forced to raise the premium to 20 in the next period based on realized claims in period 0.

5. The high-risk individuals continue to purchase the policy in period 1 while the low-risk individuals continue to opt out, resulting in a stable equilibrium.

Since the insureds are all high-risk for the condition, this 10% of the population accounts for 31% outcome risk in the market. As N increases, individuals’valuation for the bundled insurance policy begins to converge and more individuals begin to opt back into the market and purchase coverage for the N conditions. This leads to increases both in the percentage of individuals covered and in market participation. A more extensive discussion of the intuition for this result is presented in this section.

25. While our findings demonstrate that all three measures of market efficiency provide consistent ordinal rankings of the alternatives, we noted in the section on “Market Efficiency Measure” that these measures do not provide the same cardinal interpretation. That is, legislators would be more interested in the market participation measure when evaluating alternative regulatory o legislative policies because it more accurately describes how close the market is to attaining universal coverage, which is important considering the network externalities associated with universal coverage. The other two measures do not provide such an unambiguous interpretation.

26. Figure 3 shows that when N = 1 insureds (those purchasing the policy) pay a premium of 20, which is not surprising since that is the actuarially fair rate for an individual at high risk for the medical condition (and we saw before that only individuals at high risk for the covered medical condition end up purchasing this policy when N = 1). However, the figure also shows that as N increases and as more individuals opt back into the market, the premium rate decreases. However, it decreases at a slower rate as N increases since the last individuals that choose to opt back into the market are those at least risk in the population (for the N conditions).

27. In addition, the results do not rely on the assumption that the risk statuses across diseases are i.i.d. The general result that the market will converge to a full market participation pooling equilibrium as the number of medical conditions covered in the bundled policy increases still holds even if the risks are correlated. However, this convergence occurs at a slower rate than under the i.i.d. assumption (i.e., a larger bundle is required to attain the universal coverage solution). In addition, the results do not rely on the assumption that risk status for each medical condition is distributed according to a binomial. The Central Limit Theorem and law of large numbers ensure that when considering a sufficiently large applicant base the results will hold under a wide range of assumptions about the underlying distribution of risk.

28. In this section, the risk aversion parameter for the exponential utility function, r, is equal to 0.005. For this model, this risk aversion parameter implies that applicants are willing to pay between 13 percent and 18 percent above actuarially fair rates to avoid uncertain losses. Risk premiums of this magnitude seem reasonable in most insurance markets [27].

29. Conversely, intermediate values for the proportion of high risks will weaken pooling.

## REFERENCES

1. Arrow, K. The value of and demand for information. In S. Begley (ed.), Essays in the Theory of Risk Bearing. Chicago: Markham, 1971, pp. 268–278.

2. Bakos, Y., and Brynjolfsson, E. Bundling information goods: pricing, profits and effi ciency. Working paper (1999), Forthcoming in Management Science.

3. Begley, S. Uncovering secrets, big and small. Newsweek, January 27, 1997.

4. Begley, S. The mammogram war. Newsweek, February 24, 1997, pp. 55–58.

5. Begley, S. Cancer killer. Newsweek, December 23, 1996, p. 42.

6. Bond, E., and Crocker, K. Smoking, skydiving, and knitting: the endogenous categorization of risks in insurance markets with asymmetric information. Journal of Political Economy, 99, 1 (February 1991), 177–200.

7. Cavoukian, A. Data mining: staking a claim on your privacy. http://www.ipc.on.ca web\_site.eng/MATTERS/SUM\_PAP/PAPERS/datamine.htm, January 1998.

8. Clemons, E., and Thatcher, M. Evaluating alternative information regimes in the private health insurance industry: managing the social cost of private information. Journal of Management Information Systems, 14, 2 (Fall 1997), 9–31.

9. Clemons, E.K.; Thatcher, M.; Blecherman, B.; and Croson, D. Information technology and information asymmetry: the future of private individual health insurance. The Proceedings of the Thirtieth Annual Hawaii International Conference on System Sciences, January 1997.

10. Cowley, G. Beyond the mammogram. Newsweek, February 24, 1997, p. 59.

11. Crocker, K., and Snow, A. The efficiency effects of categorical discrimination in the insurance industry. Journal of Political Economy, 94, 21 (1986), 321–343.

12. EBRI Issue Brief. Retiree health benefits, no. 175, July 1996. http://ebri.org/ibex/ ib175.htm.

13. EBRI Issue Brief. Sources of health insurance and characteristics of the uninsured: analysis of the March 1997 current population survey, no. 192, December 1997. http://ebri.org/ibex/ ib192.htm.

14. EBRI Notes.Access to and sources of health insurance coverage of the near elderly. May 1997. http://www.ebri.org/prrel/pr378.htm.

15. Forrester, J. Counterintuitive behavior of social systems. Technology Review (January 1971), 53–68.

16. Forrester, J. Urban Dynamics. Cambridge, MA: The MIT Press, 1969.

17. Forrester, J. Industrial Dynamics. Cambridge, MA: The MIT Press, 1961.

18. Fronstin, P. Employment-based health insurance and the changing work force. EBRI Notes, June 1997.

19. GAO/HEHS-97-8. Private health insurance: millions relying on individual market face cost and coverage trade-offs. November 25, 1996, pp. 1–76.

20. GAO/HRD-93-125. Retiree health plans: health benefits not secure under employerbased system. July 9, 1993.

21. Johnson, C. Introduction to symposium on genetic testing and insurance: report of the NAIC genetic testing workshop group. Journal of Insurance Regulation, 15, 1 (Fall 1996), 3–6.

22. Just you and your DNA: how the system worked to insure genetic privacy. New York Times, June 30, 1996, 9, 13NJ.

23. Linde, G. Getting frenetic about genetics (effect of legislation on insurance industry). Best’s Review—Life Insurance Edition, 98, 4 (August 1997), 63.

24. Marquis, M. Adverse selection with a multiple choice among health insurance plans: a simulation analysis. Journal of Health Economics, 11, 2 (1992), 129–151.

25. Miyasaki, H. The rat race and internal labor markets. Bell Journal of Economics, 8 (1977), 394–418.

26. Preston, J. Trenton votes to put strict limits on the use of gene tests by insurers. The New York Times, June 18, 1996, 1, B6.

27. Puelz, R., and Snow, A. Evidence of adverse selection: equilibrium signaling and crosssubsidization in the insurance market. Journal of Political Economy, 102, 2 (April 1994), 236– 257.

28. Report of the NAIC genetic testing workshop group. Journal of Insurance Regulation, 15, 1 (Fall 1996), 7–65.

29. Riley, J. Informational equilibrium. Econometrica, 47 (1979), 331–359.

30. Rothschild, M., and Stiglitz, J. Equilibrium in competitive insurance markets: an essay on the economics of imperfect information. Quarterly Journal of Economics (November 1976), 629–649.

31. Seward, D. Genetic finding boosts AIDS hope. The Honolulu Advertiser, Saturday, January 3, 1998, A3.

32. Shoeborn, C., and Benson, V. Relationships between smoking and other unhealthy hab its: United States, 1985. Advanced Data (1988).

33. Sternberg, S. The plague, AIDS and human evolution. USA Today, Tuesday, June 2, 1998, 7D.

34. Tabarrok, A. Genetic testing: an economic and contractarian analysis. Journal of Health Economics (March 1994), 75–91.

35. Thatcher, M., and Clemons, E. Managing the costs of informational privacy in the individual health insurance market. The Proceedings of the Thirty-Third Annual Hawaii International Conference on System Sciences, January 4–7, 2000.

36. Thatcher, M. Information asymmetries, adverse selection, and the individual health insurance market: alternative mechanisms for managing the cost of private information. Doctoral dissertation—OPIM Department, The Wharton School, University of Pennsylvania; Decem ber 1998.

37. Thearling, K. From data mining to database marketing. The Data Intelligence, 1997. Group at http://www.santafe.edu/\~kurt/wp9502.shtml.

38. Vaccination and public health: going with the herd. Economist.April 11–17, 1998, p. 13.

39. When genetic testing might be appropriate: the role of the genetic counselor. Tufts Univer sity Health & Nutrition Letter, March 1998, 16, 1, p. 8.

40. Wilson, C. A model of insurance markets with complete information. Journal of Eco nomic Theory, 16 (1977), 167–207.

## Appendix 1: Definition of Insurability

A definition of insurability generally includes the following characteristics:

Risk Pooling: There must be a suitable level of information and a suitable level of ambiguity or uncertainty about certain events for insurance markets to exist. For example, both insurers and policyholders can determine rough estimates of risk, based on construction and location of a house. This enables insurance companies to estimate their expected losses from a large pool of similar houses over a long enough period of time, and enables consumers to estimate the expected value of the policy, but neither party can determine exactly the risk to any individual home or any individual homeowner.

 Indemnification: There must be credible off-loading of risk, through an enforceable contract, from the insured to a financially secure insurer, such that the insur ing firm and not the insured individual is at risk once the contract is written.

 Rating: Using information on similar policyholders, and recent historical data, it must be possible to assess expected losses with sufficient accuracy to support a profitable (or at least break-even) insurance market and to price policies appropriately.

## Appendix 2: Simulation Specifications

Below is a table of parameters and variables used in the simulation:

$N$ number of i.i.d. medical conditions covered by the bundled insurance policy offered in the market

$\lambda _ { { \scriptscriptstyle H } }$ percentage of the population at high risk for medical condition j, $\forall j \in N$ $P _ { H }$ probability that an individual at high risk for medical condition j will acquire j (and incur the associated treatment cost), $\forall j \in N$

$P _ { L }$ probability that an individual at low risk for medical condition j will acquire j (and incur the associated treatment cost), $\forall j \in N$

$$
C
$$

$$
j, \forall j \in \mathbf {N}
$$

$P _ { B , t }$ premium the insurance company charges for the bundled insurance policy in time period t

$$
M
$$

$$
W
$$

$g _ { i , j }$ = 1 if individual i is endowed as high risk for medical condition j

$$
= 0
$$

$$
G _ {i}
$$

$$
1 = \left[ g _ {i, l}, \dots , g _ {i, j}, \dots , g _ {i, N} \right].
$$

$$
\forall i \in M
$$

$$
H _ {i}
$$

$$
N - h _ {i}
$$

$U ( x )$ utility function for individuals in the IHIM; $U ( x ) = - e ^ { - r x } ,$ , where r = risk aversion parameter

$$
E U _ {i, U N, t}
$$

$E U _ { i , B , t }$ expected utility for individual i of purchasing the bundled insurance policy in period t

$b _ { i , t }$ = 1 if individual i purchases the bundled insurance policy in period t

= 0 if individual i remains uninsured in period t

$r _ { i , j , t }$ = 1 if individual i acquires medical condition j in period t

$T C _ { t }$ Total amount of claims paid out by the insurance company in period t to cover those treatment costs incurred by insureds and covered by the insur ance policy in that period

$Z _ { t }$ Percent of individuals that purchase the bundled policy in period t

$M P _ { t }$ Market participation, or the percent of outcome risk covered by insurance, in period t

$C S _ { t }$ Consumer surplus in period t (divided by $( \mathbf { M } ^ { * } \mathbf { N } )$ to allow comparisons of the outcome variable as N varies)

## Assigning a Genetic Endowment, $G _ { _ i } ,$ , to Each Individual

As individuals enter the IHIM, each is assigned a genetic endowment, $G _ { i } = [ g _ { i , I } , \ldots , g _ { i , j } ,$ $\dots , g _ { i , N } ]$ , through random number generation:

$$
\begin{array}{r l} & g _ {i j} = 1 \text {if} 0 \leq r a n d _ {i j} \leq \lambda_ {H} \\ & \qquad = 0 \text {if} \lambda_ {H} <   r a n d _ {i j} \leq 1, \end{array}
$$

where $r a n d _ { i , j }$ is a random variable, between 0 and 1, generated for each $( i , j )$ combination.

That is, individuals are endowed with either a high-risk status (H) or a low-risk status (L) for each of the N medical conditions through a set of N independent and identical Bernoulli trials. For each Bernoulli trial, the probability that individual i will be endowed as high risk for medical condition $j \ ( \mathrm { i . e . , } \ g _ { i , j } = 1 )$ $\lambda _ { \scriptscriptstyle H }$ and the probability that individual i will be endowed as low risk for medical condition j (i.e., $g _ { i , j } = 0 ) \operatorname { i s } { ( 1 { - } \lambda _ { \scriptscriptstyle H } ) }$ . If an individual is endowed as high risk for a medical condition, the probability that he will acquire the medical condition is $p _ { H } \mathrm { , }$ otherwise, it is $p _ { L } .$

In addition, the number of medical conditions for which individual i is at high risk can be represented as follows:

$$
h _ {i} = \sum_ {j = 1} ^ {N} g _ {i, j}.
$$

Setting the Premium for the Bundled Insurance Policy for Each Time Period

Initially, in period $t = 0$ , the insurance company observes the insurable population $( \mathrm { i . e . , } \lambda _ { { \scriptscriptstyle H } } , p _ { { \scriptscriptstyle H } } ,$ , and $p _ { L } )$ . Based on this observation, the insurance company offers a bundled insurance policy to the market with a premium based on these initial population statistics:

$$
P _ {B, 0} = N * C * \Big [ \lambda_ {H} * p _ {H} + (1 - \lambda_ {H}) * p _ {L} \Big ].
$$

For $t > 0$ the insurance company adjusts the premium charged for the bundled policy based on claims experience from the previous period (i.e., experience rating):

$$
P _ {B, t} = \frac {\sum_ {i = 1} ^ {M} \left[ b _ {i , t - 1} * \sum_ {j = 1} ^ {N} C * r _ {i , j , t - 1} \right]}{\sum_ {i = 1} ^ {M} b _ {i , t - 1}}, \forall t \neq 0,
$$

where the numerator is the total claims the insurance company paid out to insureds (i.e., individuals that purchased the bundled coverage) in period (t – 1) and the denominator is the total number of insureds in period (t – 1). The premium, $P _ { B , t } ,$ offered by the insurance company in period t is the premium that would have allowed the insurance company to break even in period (t – 1).

## Consumer Choice Under Pure Bundling

Each period individuals (or potential consumers) in the IHIM observe the premium of the bundled insurance policy offered by the insurance company. Based on all available information (the realization of their risk status and the policy premium prevailing in the market), they decide whether to purchase the bundled insurance policy offered in the market or remain uninsured, based on maximizing their own expected utility:

$$
\begin{array}{c} b _ {i, t} = 1 \text {if} E U _ {i, B, t} \geq E U _ {i, U N, t} \\ = 0 \text {if} E U _ {i, B, t} <   E U _ {i, U N, t} \end{array}
$$

where

$$
E U _ {i, U N, t} = \sum_ {x = 0} ^ {h i} \left[ \frac {N !}{(N - x) !} * p _ {H} ^ {x} * (1 - p _ {H}) ^ {N - x} * \sum_ {y = 0} ^ {N - h _ {i}} \frac {(N - h _ {i}) !}{(N - h _ {i} - y) !} \right.
$$

$$
\left. \ast p _ {L} ^ {y} \ast (1 - p _ {L}) ^ {N - h _ {i} - y} \ast U (W - (x + y) \ast C) \right]
$$

and

$$
E U _ {i, B, t} = U \Big (W - P _ {B, t} \Big).
$$

Claims Paid Out to Insureds

Each period each individual either remains healthy or experiences occurrences of illness. Realization of sickness for each individual is modeled through two sets of Bernoulli trials. An individual is at high risk for $h _ { i }$ medical conditions and at low risk for the remaining $( N - h _ { i } )$ medical conditions.

We first determine which of the $h _ { i }$ high-risk conditions each individual acquires. We do this by performing, for each individual, $h _ { i }$ Bernoulli trials where the probabil ity that individual i will acquire medical condition j $( \forall j \ : \varepsilon \ : h _ { i } )$ is $p _ { H }$

$$
\begin{array}{r l} & r _ {i, j, t} = 1 \text {if} 0 \leq r a n d _ {i, j, t} \leq p _ {H} \\ & \qquad = 0 \text {if} p _ {H} <   r a n d _ {i, j, t} \leq 1, \forall j \in h _ {i} \end{array}
$$

We then determine which of the $( N - h _ { i } )$ low-risk conditions each individual acquires. We do this by performing, for each individual, $( N - h _ { i } )$ Bernoulli trials where the probability that individual i will acquire medical condition $[ \forall j \ : \mathfrak { E } \ : ( N - h _ { i } ) ]$ is $p _ { L }$

$$
\begin{array}{l} r _ {i, j, t} = 1 \text {if} 0 \leq r a n d _ {i, j, t} \leq p _ {L} \\ \qquad = 0 \text {if} p _ {L} <   r a n d _ {i, j, t} \leq 1, \forall j \in (N - h _ {i}). \end{array}
$$

Insureds (i.e., individuals that purchase the bundled insurance policy) in period t file insurance claims for treatment costs that are incurred in that period (and that are covered by the policy). The claims paid out by the insurance company in period t to all insureds are:

$$
T C _ {t} = \sum_ {i = 1} ^ {M} \left[ b _ {i, t} * \sum_ {j = 1} ^ {N} C * r _ {i, j, t} \right]
$$

## Measures of Market Efficiency

In this model we track three measures of market efficiency during each period to evaluate market outcomes:

 Percentage of Individuals Purchasing the Bundled Policy

$$
Z _ {t} = \frac {\sum_ {i = 1} ^ {M} b _ {i , t}}{M}
$$

 Market Participation

$$
M P _ {t} = \frac {\sum_ {i = 1} ^ {M} \left[ b _ {i , t} * (h _ {i} * p _ {H} + (N - h _ {i}) * p _ {L}) \right]}{\sum_ {i = 1} ^ {M} \left[ h _ {i} * p _ {H} + (N - h _ {i}) * p _ {L} \right]},
$$

where the numerator is the outcome risk covered by insurance and the denomi nator is the total outcome risk exposure in the market.

 Consumer Surplus per Condition per Individual

$$
C S _ {t} = \frac {\sum_ {i = 1} ^ {M} \left[ b _ {i , t} * \left(W T P _ {i , t} - P _ {B , t}\right) \right]}{M * N}
$$

$$
C S _ {t} = \frac {\sum_ {i = 1} ^ {M} \left[ b _ {i , t} * \left(C E _ {i , B , t} - C E _ {i , U N , t} - P _ {B , t}\right) \right]}{M * N},
$$

where $W T P _ { i , t } ~ =$ Consumer i’s willingness to pay for the bundled insurance policy in period t.

$C E _ { i , B , t }$ = Certainty equivalent for individual i for purchasing bundled policy in period t.

$C E _ { i , U N , t }$ = Certainty equivalent for individual i for remaining uninsured in period t.
