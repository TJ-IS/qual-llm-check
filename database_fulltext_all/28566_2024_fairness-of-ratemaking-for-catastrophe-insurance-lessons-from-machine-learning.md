---
otero_id: 28566
otero_key: "NYXDCMR7"
title: "Fairness of Ratemaking for Catastrophe Insurance: Lessons from Machine Learning"
authors: "Nan Zhang; Heng Xu"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.1195"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Fairness of Ratemaking for Catastrophe Insurance: Lessons from Machine Learning

Nan Zhang,<sup>a,</sup>\* Heng Xu<sup>b</sup>

<sup>a</sup> Warrington College of Business, University of Florida, Gainesville, Florida 32611; <sup>b</sup> Kogod School of Business, American University, Washington, District of Columbia 20016

\*Corresponding author

Contact: nan.zhang@warrington.ufl.edu, https://orcid.org/0000-0002-0454-7885 (NZ); xu@american.edu (HX)

Received: February 15, 2022 Revised: August 24, 2022 Accepted: December 6, 2022 Published Online in Articles in Advance: January 17, 2023

https://doi.org/10.1287/isre.2022.1195

Copyright: © 2023 INFORMS

Abstract. Catastrophe insurance is an important element of disaster management. Yet the historical presence of inequalities in insurance, from redlining to pricing disparity, has had a devastating impact on minority communities. Whereas the fairness of insurance ratemaking is studied in general, we identify a unique challenge for catastrophe insurance that sets it apart from other lines of insurance. Drawing upon the recent advances in machine learning for fair data valuation, we reveal striking connections between the two seemingly unrelated problems and lean on insights from machine learning to mathematically and empirically study the fairness of ratemaking methods for catastrophe insurance. Our results indicate the potential existence of disparate impact against minorities across existing methods and point to a unique mathematical solution that can satisfy a few commonly assumed properties of fair ratemaking for catastrophe insurance.

History: This paper has been accepted for the Information Systems Research Special Section on Unleashing the Power of Information Technology for Strategic Management of Disasters. Ahmed Abbasi, Robin Dillon-Merrill, H. Raghav Rao, and Olivia Sheng, Senior Editors; Guodong (Gordon) Gao, Associate Editor.

Funding: This work was supported in part by the National Science Foundation Division of Information and Intelligent Systems [Grant 2040807] and Amazon Science

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.1195.

Keywords: catastrophe insurance • machine learning • fairness

## 1. Introduction

A hallmark of information technology (IT) use in disaster management is the wide adoption of complex information systems for risk assessment, portfolio management, and ratemaking in catastrophe insurance (Grossi 2005). Whereas the importance of catastrophe insurance to disaster preparedness is beyond dispute, catastrophe insurers are increasingly reckoning with the potential impact of inequality in insurance practices (Plitt and Maldonado 2007). Historically, insurance redlining, the discriminatory practice of making homeowner’s insurance unavailable for minority neighborhoods, is a major cause of the disinvestment and decline of urban minority communities (Plitt and Maldonado 2007). Even recently, people living in predominantly African American communities could still be charged (on average) a 70% higher premium for the same insurance coverage than people living in communities with less than one quarter of the population being African Americans (Heller and Advocate 2015). Acknowledging the graveness of this issue, the National Association of Insurance Commissioners (2020) commissioned a specia committee to study whether industry ratemaking practices have an unfair impact on racial minorities.

Given the public discourse on inequality following almost every major disaster in the United States (Cahn 2008), it is important to examine the fairness of ratemaking methods in catastrophe insurance and to address any potential issues that arise.

The fairness of ratemaking has long been a subject of normative debates (Landes 2015) and was studied for various types of insurance, such as health (Baker 2011) and car insurance (Meyers and Van Hoyweghen 2018). Catastrophe insurance, however, poses a distinct challenge because of the unique loss patterns of catastrophes (e.g., hurricanes, floods, earthquakes, tornadoes, etc.; Jaffee and Russell 1997): (1) infrequent loss events, (2) catastrophic amounts of losses, and (3) strong spatial correlations between occurrences of losses. Given these unique patterns, compared with other lines of insurance, catastrophe insurers have to allocate a much larger portion of the premium to risk load (Grossi 2005), a charge on top of the expected loss to compensate for the extra capital required to handle the volatility of catastrophic risks. For catastrophes such as hurricanes, risk load frequently exceeds expected loss and accounts for a majority of the insurance premium (Meyers 1996). It is, thus, critical to examine the fairness of risk-load calculation in order to achieve fair ratemaking for catastrophe insurance. Unfortunately, fair risk-load calculation has, thus far, received little attention in the literature.

The goal of this paper is to explore the notion of fair risk-load calculation and to examine the fairness of existing ratemaking methods. That is, we study how a catastrophe insurer could fairly calculate the risk load (portion of the premium) when setting the premium of an insurance policy, which is a contract between the insurer and a policy holder to specify the claims (e.g., perils, limits) covered by the insurer in exchange of the premium paid by the policy holder. We start by identifying a surprising link between fair risk-load calculation and a problem known as fair data valuation<sup>1</sup> in machine learning (e.g., Jia et al. 2019b), which studies the fair assessment of how much each input data point contributes to the output of a complex machine learning algorithm. Striking connections emerge once when we consider a data point in the machine learning problem as an insurance policy, a machine learning algorithm as a catastrophe loss model, and the algorithmic output as the estimated loss distribution for an insurer. After offering a detailed mapping between the two problems, we lean on insights from machine learning, particularly the success of an axiomatic approach (Ghorbani and Zou 2019), to develop an analogous conceptual framework for assessing the fairness of risk-load calculation in catastrophe insurance.

Specifically, we first identify three axioms that represent the minimum requirements for a risk-load calculation method to be deemed “fair.” Then, we draw on the axiomatic approach to reach a remarkable finding that there is only one mechanism for risk-load calculation—based on the notion of Shapley value (Shapley 1951)—that can satisfy all three axioms at once. Whereas Shapley value is a classic notion in game theory that frequently appears in theoretical discourse for insurance ratemaking (Mango 1997), its practical application is limited by its high computational cost, which grows exponentially with the number of insurance policies. To overcome this obstacle, we again draw on machine learning (Jia et al. 2019b) to develop an efficient FAST-SV algorithm that reduces the computational cost from exponential to close to linear to the input size. Equipped with this algorithm, we then compare the existing riskload calculation methods for catastrophe insurance with Shapley value both mathematically and empirically and find evidence of disparate impact against racial minorities across the existing methods.

Our findings add to the existing literature on IT use in the insurance industry (Barrett and Walsham 1999, Bassellier et al. 2003) by demonstrating the need for studying not only how IT advances the internal processes of insurance companies, but also how it affects the welfare of individual policy holders. To this end, our work supplements recent studies in information systems (IS) on the fairness of IT system design for disaster responses (Bharosa et al. 2010, Nussbaumer et al. 2023) by highlighting the existence of fairness concerns not only in responding to and recovering from disasters, but also on disaster preparedness issues, such as ratemaking for catastrophe insurance. At the end of the paper, we further elaborate the practical implications of our work, the limitations of our findings, and the potential directions for future research.

## 2. Related Work

In this section, we start with an overview of the related work in IS before discussing the existing methods for ratemaking in catastrophe insurance. We conclude with a brief review of the ongoing normative debate on the notion of fairness in insurance ratemaking.

## 2.1. Linking Collective Risks with Individual Actions: Related IS Phenomena

The basic premise of this paper is to examine how collective risks (Houston 1960) can be fairly linked to individual responsibilities (Milinski et al. 2008). In the case of catastrophe insurance, the economic risk being hedged is not independent across insured properties, but strongly correlated, making it a form of collective risk and giving rise to the need of fairly linking this collective risk to the premiums charged at the individual level. It is important to note, however, that this need of linking collective-level risks to individual-level actions is not limited to catastrophe insurance, but widely prevalent in IS, from strategic IT management to behavioral research, as highlighted by the following examples.

A notable example on the strategy side is research on data breaches. There is clear consensus that data breaches are not independent, isolated events for each organization, but feature substantial regularities in terms of victims’ location, industry, etc. (Sen and Borle 2015), indicating the collective nature of data-breach risks. Although the extant IS literature mostly focuses on organization-level factors (e.g., Angst et al. 2017, Goode et al. 2017, Khan et al. 2021), there is also a growing understanding that doing so leaves a dearth of under standing on how the collective risk of data breaches can be linked to managerial actions at individual organizations (e.g., Sen and Borle 2015, Kashmiri et al. 2017). For example, when a firm suffers from more frequent attacks, how much of it may be attributed to firm-level decisions and how much to attackers targeting firms of a similar nature? If an industry collectively suffers from a reputation of being “easy to hack,” are firms paying their fair share of cybersecurity investments to overcome this reputation? Whereas answers are elusive in the literature, questions of this sort, that is, how macro (e.g., industry/societal level) phenomena connect with micro organization-level managerial actions, are examples of the classic structure–agency struggle in strategy research (Herepath 2014) and is closely related to the challenges addressed in the paper.

A similar situation arises in behavioral IS research on information privacy. One issue of considerable interest to privacy scholars is how to objectively measure the risk associated with an individual’s behavior of disclosing private information to data collectors, such as online platforms (Adjerid et al. 2018). This risk resides at the collective level as data collectors reap benefits by mining data collected from numerous customers. The challenge, therefore, lies in how this collective risk can be linked to each individual. Whereas the technical community has largely settled on measuring the marginal risk introduced by the use of each individual’s data (e.g., through differential privacy; Dwork 2008), a critical issue is that the sum of marginal risks may not equate the collective risk, meaning that a set of private data may incur considerable collective risk even when its marginal risk is extremely small for each individual (Kifer and Machanavajjhala 2011). Once again, this issue of fairly linking collective privacy risks to each individual is closely related to the challenges addressed in this paper.

Data breaches and privacy risk assessment are but two examples of a broad range of IS phenomena that are relevant to the notion of collective risk. Many issues in artificial intelligence (AI) governance, from the interpretability (Rai 2020) to the fairness (Abbasi et al. 2018) of AI models, call for linking the collective risks posed by AI models to the attitudes, beliefs, and actions of individuals whose data are essential for training the AI model. The link is even more explicated (and quantified) in problems such as data monetization (Mehta et al. 2021). Whereas the scope of our study is limited to fair ratemaking for catastrophe insurance, we further discuss the broader implications of our findings on the relevant IS research in the discussions section.

## 2.2. Ratemaking for Catastrophe Insurance

The cost of a catastrophe insurance policy is the sum of three main components summarized in Table 1 (Grossi 2005), that is, the average annual loss (AAL), the risk load, and the expense load. Note that the key terms used in the paper are also listed in alphabetical order in the online appendix. AAL is the total expected loss of all covered events in a year. For most lines o property/casualty insurance, for example, auto insurance, the total amount of loss (over a reasonably large insurance pool) varies little from year to year, and AAL constitutes the majority of the insurance premium (Venezian 1985). Yet, for catastrophe insurance, the volatility of risk means that an insurer has to com mit a level of capital far beyond the expected annua loss in order to cover the potential for a catastrophic loss. Risk load reflects the cost of this extra capita needed to insure the catastrophic risk. Whereas the exact amount of capital raised to bear the risk varies by insurers (Jaffee and Russell 1997) and regulations (Nicholson et al. 2018), a well-known principle is to limit the exceedance probability, that is, the probabil ity of insolvency as total loss exceeds total capital (Oli vieri and Pitacco 2015). For example, the Florida Office of Insurance Regulation assesses hurricane insurers with a stress test of whether the probability exceeds 1% (Nicholson et al. 2018). This insolvency-based principle implies that the total capital requirement (and, correspondingly, the sum of risk load for all policies) is pro portional to the standard deviation of the insurer’s total loss distribution (Kreps 1990, Copeland et al. 2005). For catastrophes such as hurricanes and earthquakes, the standard deviation of loss frequently exceeds its mean, making risk load a much larger portion of the insurance premium than other property/casualty insurance (Meyers 1996). Finally, expense load captures the administrative costs associated with insurance policies, such as profits, commissions, taxes, expenses for loss adjustments, etc., and is usually calculated as a fixed percentage (e.g., 30%) of the sum of AAL and risk load (Grossi 2005).

Because expense load takes a fixed percentage of AAL and risk load, the key to fair ratemaking is the fairness of calculating AAL and risk load for a policy. To this end, it is helpful to identify an important difference between AAL and risk load. AAL is linear over the insurance pool, meaning that the total AAL for a set of policies is always equal to the sum of AAL for each policy. In contrast, risk load is not linear because standard deviation is a nonlinear function. More specifically, risk load is subadditive, meaning that the total risk load for a set of policies is always less than or equal to the sum of risk load for each policy. This difference between AAL and risk load leads to a unique challenge for calculating the risk load of an insurance policy. Unlike in the case of AAL, in which the calculation for one policy can be done independently of the other policies in the pool, the risk load of one policy can depend heavily on the risk profile of the other policies. For this reason, even when given a loss model, which allows us to calculate the total risk load for an insurance pool, how to allocate this total risk load to each policy remains a subtle issue that has received a diverse set of treatments in the literature.

Table 1. Cost Components of Catastrophe Insurance

<table><tr><td>Component</td><td>Definition</td><td>Calculation</td><td>Linearity</td><td> $w_{\text{Cat}}$ </td><td> $w_{\text{NonCat}}$ </td></tr><tr><td>AAL</td><td>Annualized expected cost of all stochastic losses</td><td> $AAL = \sum_{i} p_{i} L_{i}$ </td><td>Yes</td><td>Low</td><td>High</td></tr><tr><td>Risk load</td><td>Annualized cost of capital requirement beyond AAL</td><td>Various ways, for example, $RL = c_{1} \cdot \sqrt{\sum_{i} (p_{i} L_{i}^{2}) - AAL^{2}}$ </td><td>No</td><td>High</td><td>Low</td></tr><tr><td>Expense load</td><td>Annualized cost of expenses incurred by the insurer</td><td> $EL = c_{2} \cdot (AAL + EL)$ </td><td>No</td><td>Low</td><td>Low</td></tr></table>

Notes. Under column “calculation,” $p _ { i } \ ( 0 < p _ { i } \ll 1 )$ is the annual probability of an adverse event occurring, $L _ { i }$ is the expected loss of such an event, and $\textstyle \sum _ { i }$ is the sum taken over all such events. Both $c _ { 1 }$ and $c _ { 2 }$ are constants. $w _ { \mathrm { C a t } }$ and $w _ { \mathrm { N o n C a t } }$ is the weight of a component for a typical catastrophe and noncatastrophe insurance, respectively

Table 2 lists the risk-load allocation methods that have been studied in theory or practice. The (theoretical) concept of solidarity (S) calls for flat allocations by equally dividing the total risk load across all policies (Lehtonen and Liukko 2011). The methods of variance (V) and standard deviation (SD) originate from the general principles for insurance premium calculation (Bu¨ hlmann 1970) and allocate the risk load as proportional to the variance and standard deviation of a property’s loss distribution, respectively. Recognizing that neither V nor SD takes into account how a policy diversifies the insurance pool (e.g., geographically to spread the risk), Kreps (1990) proposes marginal variance (MV) and marginal surplus (MS) methods to allocate the total risk load proportional to how much the inclusion of a policy increases the variance and standard deviation of the insurance pool, respectively.

Whereas the five methods listed in Table 2 are the ones most widely used in practice, the literature also notes numerous variations of these methods. For example, instead of calculating variance (in V and MV), Fu and Khury (2010) calculate semivariance, which (as with variance) measures the expected squared deviation of the random loss from its mean but only over conditions for which the random loss exceeds the mean. Similarly, in place of standard deviation (in SD and MS), various tail statistics, including the $p { \mathrm { - } } \mathrm { q u a n t i l e } ^ { 2 }$ of the loss distribution (also known as value at risk; Artzner et al. 1999) and its variations, such as tail value at risk (Rockafella and Uryasev 2002), the Choquet integral of a distorted loss distribution (Wang et al. 1997), etc., have been proposed as potential statistics for quantifying financial risks. Whereas the suitability of different statistics as risk measures is the subject of intense debate in the literature (e.g., Acerbi and Tasche 2002), the distinction between them is not as important for the purpose of this paper as we aim to study the fairness of allocating the quantified risk to individual policies, not how to quantify the risk. Thus, we focus on the five most representative methods in this paper.

## 2.3. Normative Notion of Fairness in Insurance Ratemaking

There is no secret that the meaning of fairness is not a settled matter in insurance ratemaking. Instead, two competing notions summarized in Table 3, solidarity and actuarial fairness, have both long held theoretical appeal and practical pertinence. Solidarity emphasizes cooperation between members of an insurance pool and allows subsidies across members of different risk levels (Lehtonen and Liukko 2011). The U.S. federal deposit insurance corporation, for example, charges a fixed insurance premium to banks regardless of the riskiness of their portfolios (Short 1985). Similarly, state-owned catastrophe insurers, such as the Spanish Consorcio de Compensacio´n de Seguros (Charpentier et al. 2022), are often required to follow the social insurance paradigm (Baker 2002) that prioritizes solidarity in setting premium for insurance policies.

In contrast, actuarial fairness underscores the responsibility of each member to pay for the risk it presents to the pool (Arrow 1978). Rather than insisting on the equality of premiums, actuarial fairness emphasizes the actuarial logic of adjusting a premium according to the risk level of each member insured. A key argument for actuarial fairness is its necessity for the business profitability of private insurers as a departure from actuarial fairness is known to lead to moral hazard and adverse selection in a competitive market (Landes 2015). For this reason, actuarial fairness is often argued as the only viable definition of fairness for private insurers (Thomas 2007) and is a principle widely respected by regulators in the United States (Frezal and Barry 2020).

Table 2. Methods for Allocating Catastrophe Risk Load

<table><tr><td>Method</td><td>Abbreviation</td><td>Definition</td><td>Calculation</td><td>Reference</td></tr><tr><td>Solidarity</td><td>S</td><td>Evenly distributed</td><td> $\propto 1/|\Omega|$ </td><td>Lehtonen and Liukko (2011)</td></tr><tr><td>Variance</td><td>V</td><td>Proportional to variance of loss</td><td> $\propto \sigma^{2}(s_{j})$ </td><td>Lange (1969)</td></tr><tr><td>Standard deviation</td><td>SD</td><td>Proportional to standard deviation of loss</td><td> $\propto \sigma(s_{j})$ </td><td>American Academy of Actuaries (2018)</td></tr><tr><td>Marginal variance</td><td>MV</td><td>Proportional to marginal increase of variance</td><td> $\propto \sigma^{2}(S_{j} \cup \{s_{j}\}) - \sigma^{2}(S_{j})$ </td><td>Kreps (1990), Meyers (1996)</td></tr><tr><td>Marginal surplus</td><td>MS</td><td>Proportional to marginal increase of standard deviation</td><td> $\propto \sigma(S_{j} \cup \{s_{j}\}) - \sigma(S_{j})$ </td><td>Kreps (1990), Dietz and Niehörster (2021)</td></tr></table>

Notes. ∝ � proportional relationship. | Ω | � number of policies in the pool. σ(·) � standard deviation. s � policy under consideration. S � the set of policies in the pool before adding s .

Table 3. Conceptions of Fairness in Insurance

<table><tr><td>Fairness</td><td>Idealized principle</td><td>Conception of insurance</td><td>Rate independent of</td><td>Examples</td></tr><tr><td>Actuarial fairness (or chance solidarity)</td><td>Each insured pays for the risk it introduces to the pool</td><td>A contract between an insured and the insurer underwriting a portfolio of policies</td><td>Who receives future indemnities</td><td>Most private insurances</td></tr><tr><td>Solidarity (or subsidizing solidarity)</td><td>Every insured pays the same premium (or commensurate with income)</td><td>A cooperative arrangement to redistribute risk and responsibility among members of an insurance pool</td><td>The risk profile of the insured</td><td>Most social insurances (e.g., social security)</td></tr></table>

Ethicists spend considerable efforts analyzing the epistemological differences underpinning the two fairness definitions, positing that they stem from differences in cultural backgrounds (Baker 2002), the availability of knowledge on individual risks (Frezal and Barry 2020), the attribution of moral responsibility for insured incidents (Ewald 2014), etc. Particularly relevant to our work is Lehtonen and Liukko’s (2011) argument that the definition of fairness in ratemaking is closely linked to how insurance is conceptualized; that is, whether as a social contract for people to share and redistribute collective risks (i.e., solidarity) or as a commercial contract between the insurer and the insured so as to transfer an individual’s risk to an insurer through the premium paid by the individual (i.e., actuarial fairness). Our conceptualization obviously belongs to the latter category as we strive to examine whether the ratemaking practice of private catastrophe insurers could have a disparate impact against minorities. Thus, we focus on the notion of actuarial fairness in this paper.

## 3. Fair Ratemaking for

## Catastrophe Insurance

In this section, we develop the conceptual foundation for fair ratemaking in catastrophe insurance. We first illustrate a unique challenge posed by the distinct loss patterns of catastrophes before drawing on a recent advance in machine learning to explicate the mechanism through which ratemaking for catastrophe insurance can satisfy a few commonly assumed properties of fairness. At the end of this section, we build on the conceptual foundation to mathematically analyze the fairness (or the lack thereof) of existing ratemaking methods for catastrophe insurance.

## 3.1. Unique Challenges

As discussed earlier, the infrequent yet severe nature of catastrophic losses results in volatile risks that place a specific emphasis on risk-load calculation in ratemaking for catastrophe insurance. Whereas the calculation of total risk load for an insurance pool is extensively studied (as reviewed in Section 2.2), what receives far less attention is the fairness of allocating this risk load to each individual policy in the pool. In the passages that follow, we use an idealized example to illustrate a challenge facing the fair allocation of risk load, which makes the problem nontrivial.

Consider Figure 1, which shows the risk load of insuring three properties (a, b, and c) in the state of Florida against hurricane damages. Properties a and b are on the Gulf coast, and c is on the Atlantic coast. For the purpose of illustration, we assume that geographic dispersion alone determines the loss correlation between properties. In other words, when a hurricane hits property a, it also hits b. Yet the probability for a hurricane to hit c is independent of that fo a and/or b. Following this assumption, Figure 1(b) depicts the exceedance probability curves (Olivieri and Pitacco 2015) for insuring every possible subset of the three properties. Each curve shows the amount of capital, as captured by the x-axis, required to reduce the exceedance probability (i.e., the aforementioned probability of insolvency) below a threshold captured by the y-axis. Because the risk load reflects the cost of (and is, thus, proportional to) the required capital, when the desired exceedance probability (p in the fig ure) is given, we can simply consider the correspond ing x as the total risk load for ensuring each subset of policies. Recall from Section 2.2 that the risk load is subadditive. For example, as can be seen from Figure 1(b), {a, b, c} is clearly smaller than three times the risk load for each individual policy.

The problem facing the fair allocation of total risk load is readily observable from Figure 1. Consider the risk load allocated to c when we follow the MS method, sequentially adding each policy into the pool. Recall that MS assigns the corresponding increase on the total risk load to the newly added policy. The allocation to c is $\epsilon _ { 1 }$ if we add c first, $\epsilon _ { 2 }$ if second, and $\epsilon _ { 3 }$ if last. Besides this order dependency being an operational challenge (Mango 1997), none of these allocations seems fair: if c is added first, it is “penalized” with the largest risk load, contradicting a commonsense intuition that c should be rewarded rather than penalized because, without it diversifying the risk, the entire insurance pool would be concentrated on the Gulf coast. If c is added second, a and b receive different risk loads (with the first added one shouldering a larger portion), contradicting a simple notion that the risks introduced by a and b are completely identical and, thus, should result in the same risk load. Finally, if c is added last, then it reaps all the benefits from the dispersion of risk, leaving a and b with the exact same risk load as if c were not in the pool. This is, once again, contradictory to the common sense that, because properties on both coasts contribute to the dispersion of risk, the resulting benefit should lower the risk load for all three properties rather than c alone.

Figure 1. (Color online) Illustration of Insuring Three Properties in Florida  
![](/api/attachments/NYXDCMR7/fulltext/images/7d187853e7712a263866a14b375bb106b8da4dd58458c8cde92e5cca73324e34.jpg)  
Notes. The y-axis of an exceedance probability curve represents the probability for total loss to exceed the amount specified by the x-axis. Panel (b) depicts the exceedance probability curves for insuring all possible subsets of properties a, b, and c. All curves are simulated using exponentia distribution (rate λ � 1) as the loss distribution for each property and the pairwise correlation coefficient being one for {a,b} and zero otherwise. (a) Map. (b) Exceedance probability curves.

The problem in this example highlights a key challenge facing fair ratemaking in catastrophe insurance. The subadditive nature of risk load requires a fair ratemaking method to account for the dependencies among policies in allocating the total risk load. For example, given that the total risk load of the three properties in Figure 1 would be higher were the three properties on the same coast, a ratemaking method has to fairly distribute this reduction of risk load among the three policies. As discussed earlier, a fair distribution depends on the geographic densities of policies in the pool as it stands to reason that property c should enjoy a larger share of the reduction because it is the only property on the Atlantic coast. Note that analyzing such dependencies among policies may require the risk load to be calculated numerous times over different subsets of policies, such as the curves depicted in Figure 1(b). When the calculation involves a computationally expensive catastrophe model (Grossi 2005), the computational cost of risk-load allocation becomes a critical challenge for fair ratemaking in catastrophe insurance. We draw on recent advances in machine learning to address these challenges in the rest of this section.

## 3.2. Connection with Fair Data Valuation in Machine Learning

In the passages that follow, we draw a somewhat surprising analogy between fair risk-load allocation and the problem of fair data valuation in machine learning (Ghorbani and Zou 2019) and demonstrate how the analogy allows us to leverage two recent advances in machine learning to address fair ratemaking in catastrophe insurance.

The problem of fair data valuation answers a key question in explainable machine learning: how valuable is each data point in a training data set to the predictive accuracy of a machine learning model trained from the data set? This question is directly tied to the pricing of data points in a data market (Jia et al. 2019b). Further, data valuation is used to identify outliers in training data (Tang et al. 2021), identify the types of data to acquire for improving a machine learning model (Ghorbani and Zou 2019), etc.

A close examination of the challenge for fair data valuation reveals striking similarities to fair risk-load allocation in catastrophe insurance: as in the latter case, it is straightforward to compute the total value for any given set of data points as we can simply train a machine learning model using the set and then measure its predictive accuracy as the total value. Yet, as with risk load, the predictive accuracy of a machine learning model is nonlinear (and generally subadditive) to its training data points, making the division of a data set’s value to its individual members a nontrivial task. Table 4 summarizes the analogies between the two problems.

The analogies between the two problems inspire us to draw from two recent advances in data valuation for machine learning. One is the success of an axiomatic approach in developing the valuation design. To this end, researchers find that, once we specify a few axioms that, if violated, obviously disqualify a design from being deemed fair, the number of potential designs that can satisfy all axioms becomes surprisingly small. Specifically, Ghorbani and Zou (2019) prove that there is only one design based on the idea of Shapley (1951) value, which satisfies three widely accepted axioms. Drawing from this success in machine learning, in the next section, we follow the axiomatic approach to develop three axioms governing fair riskload allocation for catastrophe insurance before mathematically proving the existence of a unique solution that satisfies these axioms.

The second relevant advance in machine learning is a drastic reduction of the computational cost for fair data valuation. To appreciate its importance, recall that the total value of a training data set is calculated by measuring the predictive accuracy of a machine learning model trained from the set. Whereas this calculation is straightforward to implement, the actual training process is often computationally intensive and may have to be repeated numerous times in the data-valuation process (Ghorbani and Zou 2019). This exact issue arises in risk-load calculation for catastrophe insurance. As discussed earlier, with risk load being nonlinear, a fair allocation may require the computation of risk load over many subsets of insurance policies. Just as how the training of a machine learning model is computationally expensive, calculating the risk load for a set of policies is also costly as doing so may involve large-scale simulations of wind, meteorology, structural engineering, etc. (Grossi 2005). To address this computational challenge, we draw from the recent results in machine learning on the efficient approximation of Shapley values (Fatima et al. 2008,

Bachrach et al. 2010, Michalak et al. 2013, Jia et al. 2019b) to enable an efficient computational process for fair risk-load allocation in catastrophe insurance with the detailed algorithm discussed in the next section.

## 3.3. An Axiomatic Approach to Fair Ratemaking for Catastrophe Insurance

In this section, we follow the axiomatic approach in machine learning (Ghorbani and Zou 2019) to identify three axioms for the design of fair risk-load allocation in catastrophe insurance: (1) no risk, no pay; (2) higher risk, higher pay; and (3) separate risk, separate pay. To discuss these axioms with precision, we introduce a few mathematical notations first before defining the axioms in order. For each axiom, we also discuss which of the existing risk-load allocation methods satisfy or violate the axiom. Somewhat surprisingly, even though each axiom is satisfied by some of the existing methods and violated by others, no existing method satisfies all three axioms at once. Figure 2 visualizes all theoretical find ings from the axiomatic approach.

3.3.1. Mathematical Notations. We denote the insurance pool, that is, the set of policies under consideration, by $\Omega = \{ s _ { 1 } , \ldots , s _ { n } \}$ , where n is the number of policies in the pool. We use lowercase letters $( \mathrm { e . g . } , s )$ to denote individual policies and capital letters (e.g., S) to denote a set of policies $( \mathrm { i . e . , } S \bar { \subseteq } \Omega )$ . Let ${ \mathcal { L } } ( S )$ be the total risk load when the insurance pool consists of (only) the policies in S. Because a policy’s share of the risk load is determined by not only ${ \mathcal { L } } ,$ but also the other policies in the pool, we denote the share for policy sasr(s | Ω, L) to highlight such dependencies. It is important to note that $r ( \bar { \alpha } | \bar { \Omega } , \mathcal { L } ) \neq \mathcal { L } ( \{ \bar { s } \} )$ . Instead, as L is subadditive, the pooling of policies in Ω reduces the risk load allocated to a single policy. Thus, there is r(s | $\Omega , { \mathcal { L } } ) \leq { \mathcal { L } } ( \{ s \} )$ for all $s \in \Omega .$ . On the other hand, because $r ( s \mid \Omega , { \mathcal { L } } )$ is designed to allocate the total risk load for the entire insurance pool (i.e., L(Ω)) to all policies in the pool, by definition, there must be $\begin{array} { r l } {  { \sum _ { i = 1 } ^ { n ^ { \star } } r ( s _ { i } | \Omega , \mathcal { L } ) = } } \end{array}$ L(Ω). In the passages that follow, we use these mathematical notations to formally define the three axioms, which are also summarized in Table 5.

3.3.2. No Risk, No Pay. The first axiom stipulates that, if a (hypothetical) policy never increases the total risk load when being added to an insurance pool, no matter what policies are in the pool, then we should not charge any risk load to the policy. This axiom directly follows from the basic principle of actuarial fairness, that is, each insured pays for the risk it introduces to the pool because the principle implies that a policy incurring zero additional risk should not be charged a risk load. Mathematically, this axiom states that, if a policy ssatisfies ${ \mathcal { L } } ( S ) = { \mathcal { L } } ( \{ s \} \cup S )$ for all $S \subseteq \Omega ,$ then there must be $r ( s \mid \Omega , { \mathcal { L } } ) = 0$

Table 4. Connection with Fair Data Valuation in Machine Learning

<table><tr><td>Problem</td><td>Element</td><td>Input function</td><td>Desired output</td><td>Requirement</td></tr><tr><td>Fair risk-load allocation for catastrophe insurance</td><td>Individual insurance policy</td><td>Maps any set of policies to its (overall) risk load</td><td>Risk load for each individual policy</td><td>Sum of individual risk loads equals the overall risk load</td></tr><tr><td>Fair data valuation for machine learning</td><td>Individual data record</td><td>Maps any set of data records to its (overall) value</td><td>Value for each individual data record</td><td>Sum of individual values equals the overall value</td></tr></table>

Figure 2. Summary of Theoretical Results  
![](/api/attachments/NYXDCMR7/fulltext/images/93589f118e193022045eba18a5ff0e852101bbf8325b56463003de21b5bce57e.jpg)  
Notes. S, V, SD, MV, MS are the existing ratemaking methods in Table 2, and SV is our method. Panel (a), reflecting Theorem 1, shows that only SV satisfies all three axioms. Panel (b), reflecting Theorem $^ { . 2 , }$ shows that all existing methods overcharge policies with two known characteristic of minority-owned properties: (1) high risk and (2) low insurance uptake rate. (a) Fairness axioms. (b) Mathematical analysis

Consider the risk-load allocation methods discussed in Section 2.2. The only method that violates this first axiom is the solidarity method, which assigns a zerorisk policy the same risk load as any other policy. For all other methods, a policy that never introduces any additional risk receives a zero allocation for the risk load. For example, such a policy s always has a zero variance of modeled loss—that is, a zero allocation according to the variance or standard deviation method— as otherwise there is ${ \mathcal { L } } ( S ) < { \mathcal { L } } ( \{ s \} \cup S )$ when S is the empty set.

3.3.3. Higher Risk, Higher Pay. The second axiom stipulates that, if a policy $s _ { 1 }$ always introduces more risk than another policy $s _ { 2 }$ when being added to an insurance pool (without either $s _ { 1 } \mathrm { o r } s _ { 2 } )$ , no matter what policies are already in the pool, then we should charge a higher risk load to $s _ { 1 }$ than $s _ { 2 }$ . As with the first axiom, this second one also stems from the basic principle of actuarial fairness. Whereas the first axiom mandates a distinction between policies that do and do not introduce risks, this second axiom further distinguishes between two policies when there is a clear order between the risks they introduce. Mathematically, the axiom states that, if two policies $s _ { 1 }$ and $s _ { 2 }$ satisfy ${ \dot { \mathcal { L } } } ( S \cup$ $\{ s _ { 1 } \} ) \geq \mathcal { L } ( S \cup \{ s _ { 2 } \} )$ ) for all $S \subseteq \Omega \backslash \{ s _ { 1 } , s _ { 2 } \}$ , then there must be $r ( s _ { 1 } \mid \Omega , \mathcal { L } ) \geq r ( s _ { 2 } \mid \Omega , \mathcal { L } )$ . Note that the exclusion of $\{ s _ { 1 } , s _ { 2 } \}$ from S is necessary for the axiom to be nontrivial as otherwise there is always $\mathcal { L } ( S \cup \{ s _ { 1 } \} ) \cup \mathcal { L } ( S \cup$ $\left\{ s _ { 2 } \right\}$ ) when $s _ { 1 } \in S$ but $s _ { 2 } \notin S .$

Among the risk-load allocation methods discussed in Section 2.2, solidarity obviously satisfies this second axiom because $r ( s _ { 1 } | \bar { \Omega } , \mathcal { L } ) = r ( s _ { 2 } | \bar { \Omega } , \mathcal { L } )$ for all $s _ { 1 } , \ s _ { 2 } .$ Similarly, the variance and standard deviation methods also satisfy the axiom because the sign of comparison between $\dot { \boldsymbol { r } } ( s _ { 1 } | \Omega , \mathcal { L } )$ and $r ( s _ { 2 } \mid \Omega , \mathcal { L } )$ is, by definition, consistent with that between ${ \mathcal { L } } ( S \cup \{ s _ { 1 } \} )$ )and L(S ∪ {s<sub>2</sub>}) when S is the empty set, preventing any contradiction to the axiom. In contrast, neither marginal surplus nor marginal variance follows the axiom. This can be seen from the risk loads allocated to the two identical FL policies in the example in Section 3.1. The axiom clearly stipulates that the two policies should be allocated equal risk load. Yet, as illustrated in Section 3.1, with the marginal surplus/variance methods, the risk loads assigned to the two policies could vary depend ing upon the timing of their addition to the pool, obviously violating the axiom.

3.3.4. Separate Risk, Separate Pay. The third and final axiom concerns how the risk load allocated to a policy $( \mathrm { i . e . , \ } r ( s \mid \Omega , \mathcal { L } ) )$ should react to a change of the tota risk load $\mathcal { L } .$ . For example, if an increase of the reinsurance rate raises the total risk load L by a multiplica tive factor, then it is only fair to raise the allocation for each policy by the same factor. In other words, r(s | $\Omega , { \mathcal { L } } )$ should be linear to ${ \mathcal { L } } .$ Mathematically, the linearity of this mapping from (the domain of) L to (that of) r can be defined through the notion of module homo morphism (Bourbaki 2008). That is, if three risk load functions ${ \mathcal { L } } , { \mathcal { L } } _ { 1 }$ , and $\mathcal { L } _ { 2 }$ satisfy $\mathcal { L } ( S ) = \mathcal { L } _ { 1 } ( S ) + \mathcal { L } _ { 2 } ( S )$ for all $S \subseteq \Omega ,$ , then there must be $r ( s \mid \Omega , \mathcal { L } ) = r ( s \mid \Omega , \mathcal { L } _ { 1 } ) +$ $r ( s \mid \Omega , \mathcal { L } _ { 2 } )$ for all $s \in \Omega$ . This mathematical formalism offers another way to understand the axiom: if the total risk $\mathcal { L }$ can be decomposed into two components $\mathcal { L } _ { 1 }$ and $\mathcal { L } _ { 2 }$ (i.e., separate risk), such as the dwelling and personal property coverage parts of a hurricane insurance policy, then the rate allocated to a policy should be similarly decomposable into the sum of two corresponding components $r ( s \mid \Omega , \mathcal { L } _ { 1 } )$ and $r ( s \mid \Omega , \mathcal { L } _ { 2 } )$ $( \mathrm { i . e . , }$ separate pay). This is why we call this axiom “separate risk, separate pay.”

Table 5. Three Axioms of Fair Ratemaking for Catastrophe Insurance

<table><tr><td>Axiom</td><td>Conceptual and mathematical definitions</td><td>Violated by</td></tr><tr><td>No risk, no pay</td><td>A policy s should have zero risk load if adding it to any subset of policies S⊆Ω never changes the overall loss function; that is, r(s | Ω,L) = 0 if L(S) = L(S ∪ {s}) for all S⊆Ω</td><td>Solidarity</td></tr><tr><td>Higher risk, higher pay</td><td>A policy s1 should be allocated a higher (or equal) risk load than s2 if adding s1 to a pool of policies always introduces more (or equal) risk than adding s2; that is, r(s1 | Ω,L) ≥ r(s2 | Ω,L) if L(S ∪ {s1}) ≥ L(S ∪ {s2}) for all S⊆Ω\{s1,s2}</td><td>Marginal surplus, marginal variance</td></tr><tr><td>Separate risk, separate pay</td><td>The risk load allocated to a policy s should be linear to the risk load function L; that is, r(s | Ω,L) = r(s | Ω,L1) + r(s | Ω,L2) if L(S) = L1(S) + L2(S) for all S⊆Ω</td><td>Variance, standard deviation, marginal variance</td></tr></table>

Among the risk-load allocation methods discussed in Section 2.2, solidarity satisfies this axiom because an even division of the total risk load is always linear, that is,

$$
\begin{array}{r} r (s \mid \Omega , \mathcal {L}) = \frac {\mathcal {L} (\Omega)}{n} = \frac {\mathcal {L} _ {1} (\Omega)}{n} + \frac {\mathcal {L} _ {2} (\Omega)}{n} \\ = r (s \mid \Omega , \mathcal {L} _ {1}) + r (s \mid \Omega , \mathcal {L} _ {2}). \end{array}\tag{1}
$$

Similarly, the marginal surplus method satisfies the axiom because of the proportional (therefore, linear) relationship between ${ \mathcal { L } } ( S )$ and the standard deviation $\sigma ( S )$ used for calculating the marginal surplus. In contrast, the other three methods (i.e., variance, standard deviation, and marginal variance) violate this axiom because they all include in $r ( s \mid \Omega , { \mathcal { L } } )$ a normalization factor that varies with L. Consider the standard deviation method as an example. Let $\sigma _ { 1 } ( \cdot )$ and $\sigma _ { 2 } ( \cdot )$ be the standard deviation associated with $\mathcal { L } _ { 1 }$ and $\mathcal { L } _ { 2 }$ , respectively. Because $\mathcal { L } ( S ) = \mathcal { L } _ { 1 } ( S ) + \mathcal { L } _ { 2 } ( S )$ for all $S \subseteq \Omega$ , there is $\sigma ( s ) = \sigma _ { 1 } ( s ) + \sigma _ { 2 } ( s )$ for all $s \in \Omega$ . Thus,

$$
\begin{array}{r} r (s _ {1} \mid \Omega , \mathcal {L}) = \frac {\sigma (s _ {1}) \mathcal {L} (\Omega)}{\sum_ {i = 1} ^ {n} \sigma (s _ {i})} \\ = \frac {(\sigma_ {1} (s _ {1}) + \sigma_ {2} (s _ {1})) (\mathcal {L} _ {1} (\Omega) + \mathcal {L} _ {2} (\Omega))}{\sum_ {i = 1} ^ {n} (\sigma_ {1} (s _ {i}) + \sigma_ {2} (s _ {i}))} \end{array}\tag{2}
$$

$$
\begin{array}{l} \neq \frac {\sigma_ {1} (s _ {1}) \mathcal {L} _ {1} (\Omega)}{\sum_ {i = 1} ^ {n} \sigma_ {1} (s _ {i})} + \frac {\sigma_ {2} (s _ {1}) \mathcal {L} _ {2} (\Omega)}{\sum_ {i = 1} ^ {n} \sigma_ {2} (s _ {i})} \\ = r (s _ {1} | \Omega , \mathcal {L} _ {1}) + r (s _ {1} | \Omega , \mathcal {L} _ {2}). \end{array}\tag{3}
$$

In other words, the axiom does not generally hold unless $\sigma _ { 2 } ( s ) / \sigma _ { 1 } ( s )$ is constant for all $s \in \Omega$ . Similar violations occur for both variance and marginal variance methods.

3.3.5. Summary. It is important to note that we make no claim of comprehensiveness when specifying the three axioms. In other words, we acknowledge that there may be many other essential or desirable properties for fair ratemaking in catastrophe insurance that could be specified as additional axioms. For example, in game theory, Myerson (1980) defines a property of balanced contributions, which requires there to be no excess claim from any player against any other, meaning that “any two players should enjoy the same gains from their cooperation together, relative to what they would get without cooperation” (p. 172). Translating to our context, it suggests that, if adding a new policy $s _ { 2 }$ reduces the risk load allocated to $s _ { 1 }$ by a certain amount, then adding $s _ { 1 }$ to the insurance pool should reduce the risk load allocated to $s _ { 2 }$ by the exact same amount. Similarly, Kamijo and Kongo (2010) define the property of balanced cycle contributions. Instead of precluding excess claim from any player to any other, it simply requires “balancedness of excess claims in a society as a whole” (Kamijo and Kongo 2010, p. 566), meaning that, for a given order of all players, the sum of excess claims from each player against its predecessor is equal to the sum of excess claims from each player against its successor. Even though the pertinence of these properties in the context of insurance ratemaking still requires future research, what is clear from these examples is that it is impossible for us to enumerate all possible axioms when exploring notion of fair risk-load calculation.

As such, we stop at the three axioms in Table 5 for two reasons. First, as summarized in the table, each of the five existing methods for risk-load allocation already violates at least one of the three basic axioms. Second, as we demonstrate in the next section, the three axioms alone narrow the number of feasible designs for fair risk-load allocation to one, meaning that any additional axioms are either satisfied by the unique design (and, therefore, implied by the three axioms) or inherently conflictive with the three axioms. In the discussions sec tion, we elaborate on how future research can further explore the existence of additional axioms for fair riskload allocation.

## 3.4. Shapley Value–Based Ratemaking for Catastrophe Insurance

Drawing from the close analogy with fair data valuation in machine learning, which, in turn, leverages the classic result by Shapley (1951) in game theory, we have the following theorem indicating the existence of one unique solution that can satisfy all three axioms. Because of space limits, we defer to the online appendix for all mathematical proofs in the paper.

Theorem 1. For given Ω and ${ \mathcal { L } } ,$ the only $r ( s \mid \Omega , { \mathcal { L } } )$ that satisfies all three axioms is Shapley value

$$
r _ {\mathrm{SV}} (s \mid \Omega , \mathcal {L}) = \sum_ {S \subseteq \Omega \setminus \{s \}} \frac {(n - 1) ! \mid S \mid !}{n !} (\mathcal {L} (S \cup \{s \}) - \mathcal {L} (S)),\tag{4}
$$

where |S| is the number of policies in S and (·)! represents the factorial.

The Shapley value–based allocation can be intuitively understood as follows. Note from the theorem that $r _ { \mathrm { S V } }$ for a policy $s \in \Omega$ is the mean of ${ \mathcal { L } } ( S \cup \{ s \} ) -$ ${ \mathcal { L } } ( S )$ if we enumerate all possible permutations of Ω and let S be the set of policies that appear before s. In other words, the Shapley value–based allocation for a policy can be simply understood as the expected value of the marginal surplus–based allocation to the policy if we add all policies into the pool in a random order. This observation readily explains why $r _ { \mathrm { S V } }$ overcomes the problems of the existing methods to satisfy all three axioms at once. Consider its comparison with the marginal surplus method as an example. Recall that marginal surplus satisfies the first and third axioms but violates the second one $( { \mathrm { i . e . } }$ , higher risk, higher pay) because two policies with identical risk profiles can be assigned different allocations depending on the timing of their addition to the pool. By taking an average over all possible timing, $r _ { \mathrm { S V } }$ eliminates this dependency and resumes compliance with the second axiom. Further, because $r _ { \mathrm { S V } }$ is simply a linear combination of all possible marginal surpluses, its compliance with the first and third axioms follows directly from that of marginal surplus. The uniqueness of $r _ { \mathrm { S V } }$ is subtler to explain, for which we refer to the mathematical proof for the theorem in the appendix.

## 3.5. Comparison Between Shapley Value and Existing Methods

In order to understand how Shapley value compares against the existing methods for risk-load allocation in terms of their impacts on minorities, it is important to situate the comparison in the historical and social context of catastrophe insurance, specifically in terms of the how the majority and minority groups differ in the characteristics of the properties they own and insure. As is well-recognized in the literature (Squires 2003), the historical practices of discriminatory actions by the U.S. property insurance industry had a profound impact on the uneven development of metropolitan areas, resulting in two notable characteristics of minority-owned properties.

1. In terms of individual properties, minority-owned ones are more likely to be older, inadequately maintained, and located in areas with low-quality infrastructure (e.g., inadequate wastewater systems; Smiley 2020), making them more susceptible to damages (Squires 2003). For example, Akter and Mallick (2013) find that poorly constructed properties are not only more likely to be damaged in a storm, but also require higher repair/replacement costs. In other words, insuring these properties introduces a higher risk (i.e., a larger σ(s)).

2. In terms of correlation among different properties, the insurance uptake rate is known to be considerably lower in minority-dominated geographic areas (Plitt and Maldonado 2007). A lower uptake rate, which reduces the geographic density of insured properties, also lowers the correlation among the losses of different insured properties. In other words, the correlation between the loss of a minority-owned property and the total loss of the pool tends to be weaker than that of a majority-owned property.

Whereas we defer to Section 5 for an empirical study of the allocation methods, we launch a mathematical analysis here to investigate how the two characteristics of minority-owned properties affect the risk load allocated to them by the various methods.

To make the analysis possible, it is necessary to consider an idealized case with some simplifying assumptions. Specifically, we assume that every policy $s _ { i } ( i \in [ 1 ,$ $n ] )$ follows the same loss distribution scaled by a differ ent multiplicative factor $\lambda _ { i } > 0$ . As such, we denote the standard deviation of the loss distribution for $s _ { i }$ by $\sigma \cdot \lambda _ { i } ,$ and the covariance between a pair of policies $\{ s _ { i } , s _ { j } \}$ by $c \cdot \lambda _ { i } \cdot \lambda _ { j } ,$ , where $\sigma > 0$ and $c \in [ 0 , \bar { \sigma ^ { 2 } } ]$ are constants. Specifically, $\mathbf { \Phi } _ { c } = 0$ represents the case in which all policies have independent loss distributions, and $c = \hat { \sigma } ^ { 2 }$ represents the case in which the loss distributions are perfectly correlated (i.e., with the Pearson correlation coefficient equal to one).

With this setting, the following theorem compares the risk-load allocated by the existing methods with the Shapley value method on two policies with distinct characteristics: $s ,$ which is riskier $( \mathrm { i . e . , } \sigma ( s ) > \sigma ( s ^ { \prime } ) )$ and located in a geographic area with low insurance uptake (idealized as independence from other policies), and $s ^ { \prime } ,$ , which has a lower risk and stronger correlation with other policies in the pool. As s matches the two characteristics of minority-owned properties discussed before, the theorem compares $r ( s ) / r ( s ^ { \prime } )$ ) across different methods with a larger ratio indicating a higher rate charged to minority-owned properties. Note that the theorem assumes positive covariance between losses for two reasons. First, it is a prevailing assumption in insurance ratemaking (e.g., Dong et al. 1996). Second, a negative covariance could potentially lead to a negative risk load being assigned to a policy by methods such as MV and MS.

Theorem 2. Consider two policies s and $s ^ { \prime }$ such that the loss distribution of s is independent of all other policies in $\Omega ,$ whereas the covariance between $s ^ { \prime }$ and any other policy $s _ { j }$ is positive and proportional $t o \ c .$ When n is sufficiently large, we have

$$
\frac {r _ {\mathrm{S}} (s)}{r _ {\mathrm{S}} (s ^ {\prime})} <   \frac {r _ {\mathrm{SV}} (s)}{r _ {\mathrm{SV}} (s ^ {\prime})} \sim \frac {r _ {\mathrm{SD}} (s)}{r _ {\mathrm{SD}} (s ^ {\prime})} <   \frac {r _ {\mathrm{V}} (s)}{r _ {\mathrm{V}} (s ^ {\prime})} \sim \frac {r _ {\mathrm{MV}} (s)}{r _ {\mathrm{MV}} (s ^ {\prime})} \sim \frac {r _ {\mathrm{MS}} (s)}{r _ {\mathrm{MS}} (s ^ {\prime})}\tag{5}
$$

when $c = 0$ and $\sigma ( s ) > \sigma ( s ^ { \prime } ) .$ , and

$$
\frac {r _ {\mathrm{SV}} (s)}{r _ {\mathrm{SV}} \left(s ^ {\prime}\right)} \sim \frac {r _ {\mathrm{MV}} (s)}{r _ {\mathrm{MV}} \left(s ^ {\prime}\right)} \sim \frac {r _ {\mathrm{MS}} (s)}{r _ {\mathrm{MS}} \left(s ^ {\prime}\right)} <   \frac {r _ {\mathrm{SD}} (s)}{r _ {\mathrm{SD}} \left(s ^ {\prime}\right)} <   \frac {r _ {\mathrm{V}} (s)}{r _ {\mathrm{V}} \left(s ^ {\prime}\right)} <   \frac {r _ {\mathrm{S}} (s)}{r _ {\mathrm{S}} \left(s ^ {\prime}\right)}\tag{6}
$$

when $c = \sigma ^ { 2 }$ and $\sigma ( s ) = \sigma ( s ^ { \prime } )$ , where \~ represents asymptotic equality, and $r _ { \mathrm { S } } , r _ { \mathrm { V } } ,$ r<sub>SD</sub>, r<sub>MV</sub>, r<sub>MS</sub>, and r<sub>SV</sub> represent the risk-load allocation by the solidarity, variance, standard deviation, marginal variance, marginal surplus, and Shapley value–based methods, respectively.

The theorem yields two important observations. In the first case, with correlation between policies held constant, a riskier policy $( \mathrm { i } . \mathrm { e } . , s )$ is assigned an unfairly high rate by the variance (r ), marginal variance (r ), and marginal surplus (r ) methods. In the second case, which allows varying correlation, a policy in a geographic area with a lower uptake rate (i.e., s, which has a weaker correlation with the other policies) is assigned an unfairly high rate by the standard deviation $( r _ { \mathrm { S D } } )$ , variance (r ), and solidarity (r ) methods. Taking into account both observations, all five existing allocation methods tend to assign a higher rate than the Shapley value–based method (r ) for minority-owned properties in at least one of the two categories (i.e., riskier and/or in a low-uptake geographic area). Whereas this theorem only reflects an idealized example, our empirical analysis in Section 5 corroborates its findings with real-world data of catastrophe losses.

## 4. Algorithmic Design for Fair Ratemaking

The computational cost of Shapley value has long been known as a challenge, blunting its practical use. Theoretically, the computation of Shapley value is proven to be #P-complete (Deng and Papadimitriou 1994), implying that no efficient solution exists unless a fundamental conjecture in computer science, $\mathsf { P } \neq \mathsf { N P } ,$ is wrong (Cormen et al. 2009). Practically, a straightfor ward implementation of the Shapley value incurs a computational cost exponential to the input size $n ,$ which, in our case, is the number of policies in the pool. This makes the implementation prohibitively expensive when n is large.

As discussed earlier, the recent discovery of the importance of Shapley value to machine learning led to renewed interest in seeking an efficient algorithm for computing Shapley values. Two different approaches are explored. One is to leverage certain special properties of the input function ${ \mathcal { L } } ,$ , which, in our case, is the risk load for a given set of policies. For example, the literature notes solutions when $\mathcal { L }$ is binary (Bachrach et al. 2010), a Heaviside step function (Fatima et al. 2008), or (the accuracy of) a k-nearest neighbor classification model (Jia et al. 2019a). Whereas this stream of research demonstrates the feasibility of reducing the computational complexity from being exponential to n to sublinear to n (Jia et al. 2019a), its ability in doing so obviously depends on the specific design of L. As the literature focuses on $\mathcal { L }$ being the accuracy of a machine learning model, we cannot directly apply these results because the definition of $\mathcal { L }$ is different in our design (i.e., representing the standard deviation of catastrophe losses).

The second approach explored in the literature is more general and designed to work for any L as it uses statistical sampling to approximate the Shapley value rather than precisely computing it (Castro et al. 2009). The key idea here is fairly simple: as discussed earlier, the Shapley value for a policy $s , r _ { \mathrm { S V } } ( s \mid \Omega , { \mathcal { L } } )$ , is the expected value of $\mathcal { L } ( S \cup \{ s \} ) ^ { - } \mathcal { L } ( S )$ when S is taken over all subset permutations of Ω. Thus, if we pick random samples of S from Ω, we can form an unbiased estimate of $r _ { \mathrm { S V } } ( s \mid \Omega , { \mathcal { L } } )$ by computing a weighted average of ${ \mathcal { L } } ( S \cup \{ s \} ) - { \mathcal { L } } ( S )$ over all samples. Following this idea, the state-of-the-art algorithm in machine learning requires $\mathcal { L }$ to be evaluated over $n ( \log n ) ^ { 2 }$ sample subsets of Ω (Jia et al. 2019b). Whereas this algorithm is a signifi cant improvement over previous solutions that require n<sup>2</sup>log n samples (Maleki et al. 2013), its efficiency is still inadequate for our purpose because, in order to compute the Shapley value for a policy s, this algorithm requires a postsampling step of solving a linear programming feasibility problem with $n ^ { \widetilde { 2 } } - n + 1$ input constraints. Even with the latest advances in linear programming, solving such a feasibility problem requires a computational cost of the polylogarithm of $n ^ { 5 }$ (Lee and Sidford 2015), which is prohibitively expensive for a large insurance pool.

To enable the efficient computation of Shapley values for fair ratemaking in catastrophe insurance, we develop a novel algorithm that combines the two approaches. Specifically, it further reduces the computational cost of the sampling approach by leveraging a cluster assumption (Verma et al. 2022) on the risk correlation between policies, meaning that the insured properties can be roughly partitioned into homogeneous clusters, and the loss correlation between two properties is largely determined by the clusters to which they belong. Consider hurricane windstorm insurance for example. As illustrated in Figure 1, whether two properties are hit by the same hurricane is mostly determined by their geographic locations. If we partition all properties into clusters according to their counties or $\mathrm { Z I P }$ codes, then the loss correlation between two properties can be estimated based on the clusters to which they belong (Grossi 2005). Specifically, their losses can be highly correlated if the two ZIP codes are spatially close to each other but close to zero when they are far apart. Whereas clusters are defined according to location alone in this example, the general definition of a cluster can depend on multiple factors, such as location, construction quality, neighborhood infrastructure, etc.

Regardless of how the clusters are defined, let $\{ v _ { 1 } , \ldots , v _ { c } \}$ be the set of all possible cluster IDs and $g ( s )$ be the cluster ID associated with a policy s. Note that $c ,$ the number of clusters, is a constant $\left( \mathrm { e . g . } \right)$ number of ZIP codes) that does not grow with n, the number of policies. To understand how this cluster assumption reduces the computational cost for Shapley values, note that, for any policy s and any set of policies $S \subseteq \Omega \backslash \{ s \}$ , there is

$$
\begin{array}{c} (\mathcal {L} (S \cup \{s \})) ^ {2} - (\mathcal {L} (S)) ^ {2} = (\mathcal {L} (\{s \})) ^ {2} + 2 \sum_ {i = 1} ^ {c} \sum_ {s ^ {\prime} \in S, g (s ^ {\prime}) = i} \rho_ {i} \\ \cdot \mathcal {L} (\{s \}) \cdot \mathcal {L} (\{s ^ {\prime} \}), \end{array} \tag {7}\tag{7}
$$

where $\rho _ { i }$ is the Pearson correlation coefficient between (the losses incurred by) s and another policy with cluster ID $v _ { i } . \mathrm { A }$ key observation from Equation (7) is that we can manually compute ${ \mathcal { L } } ( S \cup \{ s \} )$ based on nothing but access to $\mathcal { L } ( S ) , \bar { \mathcal { L } } ( \{ s \} ) , \mathcal { L } ( \{ s ^ { \prime } \} )$ for all $s ^ { \prime } \in S$ and $\rho _ { 1 } , \ldots , \rho _ { c } .$ . Consider the scenario in which we incrementally add s to Ω and maintain a sample of subsets of Ω, that is, a collection of S denoted by $S _ { 1 } , \ldots , S _ { m } ,$ where m is a predetermined sample size. When adding s to Ω, we only need to compute $\rho _ { 1 } , \ldots , \rho _ { c }$ and $\mathcal { L } ( \{ s \} )$ , meaning that the number of calls we need to make to $\begin{array} { r } { \mathcal { L } ( \cdot ) i s c + 1 } \end{array}$ , a constant number that does not grow with the size of Ω. Then, we can compute $\mathcal { L } ( S _ { i } \cup \{ s \} ) - \mathcal { L } ( S _ { i } )$ for all $i \in [ 1 , m ]$ no matter how large m is.

## Algorithm 1 (FAST-SV)

Calculate Shapley value $r _ { \mathrm { S V } } ( s \mid \Omega , { \mathcal { L } } )$ after adding s to Ω.

Input: $\mathbf { s } ; \Omega \ ( s \notin \Omega )$ ; m sample subsets of $\Omega ,$ that is, $\bar { S _ { 1 } , \ldots , S _ { m } } ; \bar { \mathcal { L } } ( S _ { 1 } ) , \ldots , \mathcal { L } ( S _ { m } ) ; \bar { \mathcal { L } } ( s ^ { \prime } )$ for all $s ^ { \prime } \in \Omega$

Output: $r _ { \mathrm { S V } } ( s \mid \Omega , { \mathcal { L } } )$

1: Call $\mathcal { L } ( \cdot )$ to calculate $\mathcal { L } ( \{ s \} )$

2: for each location identifier $v _ { i } \left( i \in \left[ 1 , c \right] \right)$ do

3: Call $\mathcal { L } ( \cdot )$ to calculate $\rho _ { i } ,$ the correlation coefficient between s and any policy with $v _ { i }$

4: end for

5: for each sample subset $S _ { i } \left( i \in \left[ 1 , m \right] \right)$ do

6: Use Equation (7) to calculate $( { \mathcal { L } } ( S _ { i } \cup \{ s \} ) ) ^ { 2 } - ( { \mathcal { L } } ( S _ { i } ) ) ^ { 2 }$ 7: end for

8: return $r _ { \mathrm { S V } } ( s \mid \Omega , { \mathcal { L } } )$ approximated using the m samples according to Equation (4).

Following this idea, Algorithm FAST-SV depicts the pseudocode for our algorithm to incrementally calculate the Shapley value for a new policy $s \not \in \Omega$ . Note that the algorithm can be easily adapted for batch processing $( \mathrm { i . e . , }$ to compute the Shapley value for every policy $s \in \Omega )$ by running FAST-SV for each $s \in \Omega$ after a preprocessing step of making $m + n$ calls to $\mathcal { L } ( \cdot )$ (the cost of which can be amortized over all n policies) in order to compute $\mathcal { L } ( S _ { 1 } ) , \ldots , \mathcal { L } ( S _ { m } )$ and $\mathcal { L } ( s _ { 1 } ) , \ldots , \mathcal { L } ( s _ { n } )$ which are taken as input in FAST-SV. Note that, with batch processing, in line 6 of the algorithm, we calculate either $( \tilde { \mathcal { L } } ( S _ { i } \cup \{ s \} ) ) ^ { 2 } - ( \tilde { \mathcal { L } } ( S _ { i } ) ) ^ { 2 } \mathrm { o r } ( \tilde { \mathcal { L } } ( S _ { i } ) ) ^ { 2 } - ( \tilde { \mathcal { L } } ( S _ { i } \backslash \{ s \} ) ) ^ { 2 } .$ depending on whether s already belongs to $S _ { i } .$ . All other steps remain the same as in the incremental version.

Building on the computational complexity analysis for sampling-based Shapley value approximation in machine learning (Jia et al. 2019b), the following theorem shows that, with Algorithm FAST-SV, the Shapley value $r _ { \mathrm { S V } } ( s \mid \Omega , { \mathcal { L } } )$ for a policy s can be estimated to any arbitrary precision with a constant number of calls to the risk-load function $\mathcal { L } ( \cdot )$ and an additional computational cost of O(nlog n), where n is the number of insurance policies in the pool.

Theorem 3. Algorithm FAST-SV returns an (ɛ, δ)-approximation of $r _ { \mathrm { S V } } ( s \mid \Omega , \mathcal { L } )$ , that is, with an estimation error ω satisfyingPr $\left\{ \mid \omega \mid < \epsilon \right\} > 1 - \delta$ , after making O(1) calls to L and incurring a computational cost of ${ \mathcal { O } } ( ( n / \epsilon ^ { 2 } ) \mathrm { l o g }$ $\left( n / \delta \right) )$

## 5. Empirical Examination

Earlier discussions establish the axiomatic properties of our Shapley value–based method with regard to fairness and demonstrate how the existing risk-load allocation methods deviate from these fairness principles. To gauge the implications of this deviation on the rate charged to individual policy holders, we launched an empirical study based on real-world data of catastrophe losses. Specifically, we examined the disparate impact of existing methods against racial minorities and lower income policy holders by comparing them with the risk load allocated by our Shapley value– based method, which is proven to satisfy the fairness principles.

## 5.1. Data Sets

We used two data sets provided by the U.S. Federal Emergency Management Agency, containing all historic claims (1973–2021) and policies in effect during the past 12 years (2009–2020) in the National Flood Insurance Program (NFIP), respectively. It is important to note that, whereas flood insurance is a typical example of catastrophe insurance (e.g., most losses to the NFIP were caused by hurricanes; Michel-Kerjan 2010), the NFIP is not a private insurer, but a public–private partnership designed to charge actuarial premiums to only a subset of policies and subsidize the others (Grossi 2005). Thus, our purpose of using the NFIP data sets was not to assess the actuarial fairness of NFIP’s ratemaking practices (as they were not designed to be actuarially fair). Rather, we leveraged data about historic losses and policies in NFIP as the basis for comparing all ratemaking methods reviewed earlier in the paper (also summarized in the next section).

The NFIP claim data set contains all 2,547,311 claims filed with the NFIP from 1973 to the present (as of September 8, 2021). The variables included for each claim cover information about the property (e.g., ZIP code), the time of loss, and the payout. Given the long time span of the claim data, we adjusted all payout amounts to constant 2020 dollars (according to the year of loss) using the gross domestic product deflator published by the World Bank (Ha et al. 2021). To assess the distribution of yearly losses for each ZIP code, we extracted from the data set all 1,914,809 claims for which the total payout is larger than zero and the ZIP code field is nonempty. These claims feature 24,002 unique ZIP codes and 159,798 unique combinations of ZIP code and year (of loss). The summary statistics for the claim data set is available in the online appendix.

The policy data set contains all 6,908,556 (yearly) policies with effective date ranging from 2009 to 2020. We used this data set in two ways. First, we used it to count the number of policies in effect for each ZIP code in each year. For any given year, this then allows us to divide the total claim payout (from the claim data set) for a ZIP code in that year by the policy count so as to calculate the average loss per policy in the ZIP code—an important measure for capturing the spatial and temporal variation of the loss function as elaborated later in the empirical design.

Second, we also used the policy data set to generate the insurance pool for our empirical study. For this purpose, it is important to note that, for privacy reasons, all unique identifiers (e.g., address) for the insured properties were redacted from the policy data set. Given the redaction, to ensure that the insurance pool we analyzed includes each property only once, we followed NFIP’s recommendation to focus on 500,842 policies with an effective date in 2020 (and, correspondingly, an expiration date in 2021). We further removed 382 policies with invalid ZIP codes and 35,880 policies from ZIP codes with no record in the claim data set (hence, zero historic loss). The resulting data set contains 464,580 policies, which became the insurance pool in our study.

A limitation of the NFIP data is their lack of individual-level sociodemographic variables, such as race, household income, etc. This is not surprising because insurers such as NFIP are, in general, prohib ited by law from collecting these variables in insurance applications (Squires 2003). Yet the absence of sociodemographic variables presents a challenge to our analysis of the disparate impact of insurance ratemaking. To address this challenge, a common method used across disciplines (including IS, Xu et al. 2021; economics, Nevo 2001; and public health, Krieger 1992) is to adopt the census-based aggregates of such variables at a certain geographic level (e.g., ZIP code) as proxies for individual-level data. We followed this approach in our empirical study and joined the NFIP data with census sociodemographic data at the ZIP-code level.

Specifically, we used the 2016 American Community Survey (ACS) data set from the U.S. Census Bureau and extracted three sociodemographic variables<sup>3</sup> from the data set at the ZIP code level: average age (hereafter denoted as age), percentage of the population who are African Americans (race), and median family income in the past 12 months (income). There are two main reasons why we operationalized race as the percentage of African Americans. First, a key fairness concern on insurance ratemaking is its disparate impact against African Americans, in large part a result of the historic practice of discriminatory redlining against African American neighborhoods (Plitt and Maldonado 2007). Second, in the specific context of flood damage, African American communities are known to shoulder disproportionate burdens, especially in the aftermath of major hurricanes such as Katrina (Colten 2006, Fothergill 2006). The summary statistics for the joined data set is available in the online appendix.

## 5.2. Design of Empirical Study

In the passages that follow, we first introduce our implementations of the ratemaking methods for allocating a catastrophe risk load to insurance policies before discussing the disparity detection method used to identify the potential disparate impact of these ratemaking methods.

5.2.1. Ratemaking Methods. We implemented all six ratemaking methods discussed earlier for allocating the risk load of an insurance pool: solidarity, variance, standard deviation, marginal surplus, marginal varianc, and our Shapley value–based method (SV). Recall that Table 2 summarizes the design of all methods except ours, which is described in Section 3.4. With the only exception of the solidarity method (S, which evenly divides the total risk load), all other methods require access to the loss distribution, specifically the standard deviation of loss σ(·) for a policy. Further, recall from Section 4 that MS, MV, and SV can be efficiently computed using the correlation matrix containing the Pearson correlation coefficients of annual per-property losses between each pair of ZIP codes. Thus, in what follows, we first describe our method of computing the loss distribution for a policy from the NFIP data before discussing our calculation of the correlation matrix. Note that, to ensure a fair comparison, for each ratemaking method, we normalize its final outputs so the average charge per policy is always one.

As discussed earlier, a limitation of the NFIP data are the redaction of individual-level identifiers for privacy reasons. Following the aforementioned approach of using ZIP code–level aggregates as proxies (Nevo 2001), for each policy in the pool, we derived its loss distribution from the historic claim data for properties in the same ZIP code. Specifically, for each of the 3,165 unique ZIP codes present in the insurance pool, we first calculated its average loss per in-effect policy—in constant 2020 dollars as mentioned earlier—for each of the 12 years between 2009 and 2020 (i.e., the time span of the policy data set) before using the standard deviation of such losses as the standard deviation of modeled loss for policies in the ZIP code. Similarly, we also used the yearly per-policy losses to calculate the correlation coefficients between pairs of ZIP codes. In other words, we considered ZIP codes as cluster IDs in the cluster assumption discussed earlier. To ensure that the correlation matrix reflects risk correlations stemming from the cluster assumption (instead of spurious ones occurring by chance), we performed a one-sided ttest for each correlation coefficient (with significance level $\alpha = 0 . 0 5 )$ and set the correlation matrix to be its Hadamard product with the test results (i.e., by setting all coefficients not passing the significance test to zero). The resulting matrix is then used in implementing MS, MV, and SV. It is important to note that, although we introduce the correlation matrix–based calculation in Section 4 as an approximation method to speed up the computation of Shapley values, in the specific case of NFIP data, this calculation is indeed precise because policies are already grouped at the ZIP code level. In other words, there was no accuracy loss from the use of correlation matrix in implementing MS, MV, and SV.

5.2.2. Disparity Detection. To assess the disparity impact of ratemaking methods, we examine the aforementioned race, age, and income as the focal social determinant, respectively, following the common practice in disparity studies (Zhang et al. 2017). Further, as our mathematical analysis in Section 3.5 indicates the importance of two factors—that is, high annual loss and low uptake rate—in determining whether minorities tend to be overcharged, we include in our analysis two variables capturing the two factors, respectively, (1) aal is the average annual loss calculated from the claim data (as per-policy average at the ZIP code level, like the social determinants); (2) uptake is the ratio between the number of active policies in the ZIP code and the population of the ZIP code (according to the census ACS data discussed before).

In terms of the dependent variable, we examine five variables corresponding to the difference-in-rate between each existing ratemaking method (i.e., S, V, SD, MS, MV) and our Shapley value–based method SV, respectively. The key rationale for this approach is Theorem 1, which proves that SV is the only possible ratemaking method that satisfies the three fairness axioms defined earlier in the paper. Whereas we do not claim SV to be the only fair method in practice, it is at least a reasonable attempt at making catastrophe insurance ratemaking fairness-aware. Thus, if the difference-in-rate between an existing method, say MS, and SV (denoted as MS–SV) is significantly higher for African Americans, then it stands to reason that, compared with a fairness-aware ratemaking method such as SV, MS could exhibit a disparate impact against African Americans by overcharging them in allocating the risk load. This is why we calculate rate differences such as MS–SV as a dependent variable in disparity detection.

We stress at the outset that, as in most existing disparity studies (National Research Council 2004), we did not attempt to establish any causal relationships between a social determinant and a dependent vari able in this paper. In other words, we strove to detect the statistical disparate impact but not the causal notion of discrimination (National Research Council 2004). As elaborated in the discussions, establishing causal relationships in the context of disparity detection not only calls for theoretical development beyond the scope of this paper, but also requires a subtle and theory-driven scrutiny of control variables—an issue that is still undergoing intense debates in the literature of disparity detection (Pager and Shepherd 2008).

In terms of the method for disparity detection, because our dependent variable is numerical, we followed the disparity-through-separation method (Xu and Zhang 2022). Specifically, the disparity in a dependent variable (e.g., MS–SV) over a focal social determinant (e.g., race) was estimated using regression analysis with the outcome being MS–SV and the independent variables consisting of the focal social determinant race, the other two social determinants age and income, and (optionally) the two control variables aal and uptake.

Following the common practice in disparity detection (Everett and Wojtkiewicz 2002, Xu and Zhang 2022), we did not include interaction items in the model. Whereas we estimate the model using the ordinary least squares (OLS) method, we recognize two potential concerns on using OLS when the dependent variable in our analysis (i.e., distributed risk load) is known to follow a heavy-tailed distribution (Embrechts et al. 2013). One is the possible presence of heteroskedasticity, which could prevent OLS from consistently estimating the variance of regression coefficients (White 1980). To address this concern, we replace the covariance-matrix computation in OLS with the heteroscedasticity-consistent White’s (1980) estimator and find no qualitative difference in the results. The other concern is that the possible presence of a long-tailed error distribution could affect the robustness of the OLS estimates (Zhou et al. 2018). To this end, we fit the model using the robust Huber’s (1973) M-estimator with iterated reweighted least squares, and again find no qualitative difference in the results of disparity detection.

## 5.3. Empirical Results

To provide an intuitive illustration of the differences between ratemaking methods, we depict in Figure 3 the cumulative distribution function (CDF) for the rates produced by the methods tested. As can be seen from the figure, our SV method distributes the total risk load more evenly across policies than the existing methods (except S, which assigns equal rate to every policy). This is consistent with our earlier discussions; that is, the existing methods tend to over-penalize policies with a higher risk or in an area with lower uptake, leading to an overly rapid increase of CDF as shown in the figure.

To quantitatively assess the differences of ratemaking methods, Table 6 reports the results of disparity detection for the existing ratemaking methods S, V, SD, MS, and MV. As can be seen from the table, when we regress the rate difference (e.g., MS–SV) over the social determinants, all five existing methods exhibit disparate impact against African Americans by overcharging them at a significance level of 0.01. Similarly, all five exhibit disparate impact against lower income policy holders at a significance level of 0.001.

When we regress the rate difference over both social determinants and the two variables involved in mathematical analysis, that is, uptake and aal, the empirical results confirm and expand our mathematical finding on the presence of disparate impact. For example, consistent with Theorem 2, Table 6 shows that V, MS, MV overcharge policies with higher aal, whereas V, S, and SD overcharge policies with lower uptake. Further, Table 6 shows that MS and MV overcharge policies with lower uptake too, whereas SD overcharges policies with higher aal even though these findings are inconclusive from the mathematical analysis. Also note from the last two columns of Table 6 that, consistent with earlier discussions and findings in the literature (Squires 2003, Plitt and Maldonado 2007), African American communities tend to be associated with a lower uptake and a higher aal.

Figure 3. (Color online) Cumulative Distribution Functions for Ratemaking Methods  
![](/api/attachments/NYXDCMR7/fulltext/images/b4fd37a32307d14f365ceb7badbf6729da99e2c136b9ec9713aac5c91f3cdc79.jpg)  
Notes. S was not included because it assigns an equal rate to all policies, leading to a step CDF. For each method, the rates are normalized into [0, 1] using min-max feature scaling. The lines for MS and MV completely overlap.

Finally, note from Table 6 that, even after controlling for uptake and aal, the disparate impact against African Americans remains for four out of five existing methods with V being the only exception for which the coefficient estimate for race is no longer sig nificantly different from zero. Further, the disparate impact against lower income policy holders remains for all five existing methods. These results suggest that, even though uptake and aal do account for a substantial part of the differences between ratemaking methods (as evidenced by the sharp increase in R<sup>2</sup> after including uptake and aal), there are likely other factors that also contribute to the differences in output rates and manifest as disparate impact against African Americans and lower income policy holders. The identification of these factors could be a promising direction for future research.

## 6. Discussions

In this section, we elaborate the policy, managerial, and research implications of our findings before concluding with the limitations of our work and potential directions for future research.

Table 6. Disparate Impact of Ratemaking Methods

<table><tr><td>Dependent variable</td><td>S-SV</td><td>S-SV</td><td>V-SV</td><td>V-SV</td><td>SD-SV</td><td>SD-SV</td><td>MS-SV</td><td>MS-SV</td><td>MV-SV</td><td>MV-SV</td><td>uptake</td><td>aal</td></tr><tr><td>(Intercept)</td><td>1.14***(0.02)</td><td>2.30***(0.04)</td><td>0.94***(0.09)</td><td>-5.72***(0.82)</td><td>1.37***(0.02)</td><td>1.04***(0.05)</td><td>0.68***(0.02)</td><td>0.00(0.06)</td><td>0.68***(0.02)</td><td>0.00(0.06)</td><td>-0.05***(0.00)</td><td>1.23***(0.01)</td></tr><tr><td>race</td><td>0.04**(0.01)</td><td>0.08***(0.01)</td><td>0.49***(0.06)</td><td>-0.14(0.08)</td><td>0.14***(0.02)</td><td>0.07***(0.01)</td><td>0.33***(0.02)</td><td>0.20***(0.01)</td><td>0.33***(0.02)</td><td>0.20***(0.01)</td><td>-0.11***(0.00)</td><td>0.08***(0.02)</td></tr><tr><td>age</td><td>0.03***(0.00)</td><td>0.00***(0.00)</td><td>-0.00(0.00)</td><td>0.18***(0.02)</td><td>-0.00*(0.00)</td><td>0.01***(0.00)</td><td>-0.00***(0.00)</td><td>0.02***(0.00)</td><td>-0.00***(0.00)</td><td>0.02***(0.00)</td><td>0.01***(0.00)</td><td>-0.03***(0.00)</td></tr><tr><td>income</td><td>-0.33***(0.00)</td><td>-0.21***(0.01)</td><td>-0.13***(0.01)</td><td>-0.84***(0.09)</td><td>-0.18***(0.00)</td><td>-0.22***(0.01)</td><td>-0.08***(0.00)</td><td>-0.16***(0.01)</td><td>-0.08***(0.00)</td><td>-0.16***(0.01)</td><td>-0.01***(0.00)</td><td>0.13***(0.00)</td></tr><tr><td>uptake</td><td></td><td>-0.31***(0.01)</td><td></td><td>-1.84***(0.15)</td><td></td><td>-0.46***(0.01)</td><td></td><td>-0.80***(0.01)</td><td></td><td>-0.80***(0.01)</td><td></td><td></td></tr><tr><td>aal</td><td></td><td>-0.95***(0.04)</td><td></td><td>5.33***(0.71)</td><td></td><td>0.25***(0.04)</td><td></td><td>0.51***(0.05)</td><td></td><td>0.51***(0.05)</td><td></td><td></td></tr><tr><td> $R^2$ </td><td>0.06</td><td>0.36</td><td>0.00</td><td>0.25</td><td>0.03</td><td>0.06</td><td>0.01</td><td>0.14</td><td>0.01</td><td>0.14</td><td>0.05</td><td>0.04</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.06</td><td>0.36</td><td>0.00</td><td>0.25</td><td>0.03</td><td>0.06</td><td>0.01</td><td>0.14</td><td>0.01</td><td>0.14</td><td>0.05</td><td>0.04</td></tr></table>

Notes. Dependent variable is rate difference between an existing risk-load allocation method (e.g., MS) and our Shapley value–based method (i.e., SV). income and aal are in \$10,000s.

$$
^ {* * *} p <   0. 0 0 1; ^ {* *} p <   0. 0 1; ^ {*} p <   0. 0 5.
$$

## 6.1. Practical Implications

As recognized by the National Association of Insurance Commissioners (2020), fair ratemaking has emerged as an issue front and center for insurance companies and regulators. Meanwhile, the growing intensities of natural disasters, especially weather-related ones, afford catastrophe insurance an increasingly vital role in disaster preparedness and responses. The primacy of these two issues is only likely to be reinforced in the future, making it all the more important for academic researchers, industry practitioners, and policy makers to scrutinize the fairness of ratemaking in catastrophe insurance. With this backdrop, our results illuminate the intricacies of fair risk-load allocation in catastrophe insurance ratemaking, and identify the potential disparate impact of existing methods. In what follows, we lean on our findings to provide actionable suggestions for ensuring a fair and equitable future for ratemaking in catastrophe insurance.

First, to catastrophe insurers, the conceptual development and methodological innovation in our paper highlights the theoretical appeal and practical pertinence of Shapley value in ratemaking for catastrophe insurance. Drawing on advances in machine learning, our FAST-SV algorithm drastically reduces the computational cost for Shapley value in the context of ratemaking, breaking the barrier to its use in practice. To this end, our results provide catastrophe insurers with a practical computational tool for enhancing the fairness of ratemaking practices.

Second, to insurance regulators, our mathematical analysis and empirical results demonstrate the importance of foregrounding the allocation of total risk load when examining the fairness of ratemaking practices for catastrophe insurance. In terms of risk-load calculation, the current research and practice (e.g., the catastrophe stress tests in Florida; Nicholson et al. 2018) tend to emphasize the adequacy of total risk load in covering catastrophic losses. Whereas the calculation of total risk load is important for the business viability of insurance companies, our mathematical and empirical results demonstrate that the allocation of this total risk load is critical in setting a fair premium for individual policies and could manifest disparate impact if not carefully designed. Thus, to ensure fairness in ratemaking, future regulators should pay closer attention to the risk-load allocation methods adopted by catastrophe insurers.

## 6.2. Research Implications

For research on IT-enabled disaster management, our findings illustrate the importance and challenge of ensuring fairness in the design of complex IT solutions for societal imperatives, such as catastrophe insurance. By showing that no existing ratemaking method satisfies the three axioms at once, we demon strate that simple and ostensibly reasonable methods can violate taken-for-granted notions of fairness when used in practice. From this perspective, our work highlights the need for careful quantitative examinations of how an IT solution affects the welfare of individuals, especially those in historically disadvantaged groups, in disaster management.

More broadly, for IS research examining phenomena that involves collective risks, our findings illustrate the value of an axiomatic approach, especially Shapley value, in operationalizing the linkage between collective-level risks and individual-level responsibilities. We do so by demonstrating the feasibility of contextualizing the axiomatic properties of Shapley value in a specific application (i.e., catastrophe insurance ratemaking). More important, we show that, by leveraging context-specific features of the risk measurement, one can overcome the computational challenge traditionally associated with the Shapley value. From this perspective, our work highlights the value of a Shapley value–based framework to the broad set of cross-level studies discussed in the related work section for strategic IT management and behavioral IS research.

## 6.3. Limitations and Future Research

The conceptual development of our work is limited by its technical focus on the mathematical definable properties of fairness within the insurance mechanism (Landes 2015). As such, we do not consider a broader conceptualization of fair ratemaking that also takes into account the externalities produced by insurance (Daniels 1990), such as how insurance ratemaking may be designed to incentivize homeowners to voluntarily strengthen their properties against hurricanes or earthquakes. The latter, more demanding, notion of fairness requires the analysis of a broad set of social benefits connected with insurance (Landes 2015) and is not a technical issue that can be treated with mathematical axioms as in our work. Similarly, when analyzing the disparate impact of existing ratemaking methods, we focus on the presence of statistically detectable disparity but do not further analyze the potential existence of any causal discrimination. As is widely recognized in the literature (Pager and Shepherd 2008), even persistent and large disparities in an empirical data set do not prove discrimination as ascertaining the latter requires knowledge of the underlying data-generation mechanisms. Owing to these limitations, our work should be viewed as only the first step in understanding the fairness of risk-load allocation. Future studies can examine, for example, the underlying causes and the societal implications of disparate impact in ratemaking for catastrophe insurance.

Another limitation of our work relates to an assumption made in almost all premium principles for catastrophe insurance, that is, a unique, stable, and known loss distribution (Pichler 2014). In practice, however, there is often pronounced uncertainty associated with the probability of loss, requiring considerable subjective judgment in setting the loss distribution for insurance ratemaking. This reliance on subjective judgment can bring additional challenges to fair ratemaking that are not captured in our work. To address such challenges, future studies can explore the recently proposed notion of ambiguity load (Dietz and Walker 2019, Dietz and Nieho¨rster 2021), which is designed to capture the uncertainty of loss distribution in insurance ratemaking.

We also offer the caveat that, even though our use of Shapley value and the axiomatic approach was motivated by recent work in machine learning, this by no means suggests that axiomatization or Shapley value has not been studied in other fields. Indeed, axiomatization has a long tradition in game theory (Nash 1950, Shapley 1951), and both axiomatization and Shapley value are extensively studied in the economic literature (Roth 1977, Gul 1989, Moulin 1992, Krishna and Serrano 1996, McQuillin and Sugden 2016). With economics being a foundational discipline for business research, there should be no surprise that Shapley value is applied to many business fields, for example, in accounting to study cost assignment in organizations (Roth and Verrecchia 1979), in finance to assess the systemic importance of a bank (Tarashev et al. 2016), in IS to explain machine learning models (Zhang et al. 2022), in strategic management to disentangle the sources of heterogeneity in firm performance (Sharapov et al. 2021), in marketing for tracing profit increase to publishers of online advertisement (Berman 2018), and in operations research for a variety of purposes (Shubik 2002) from studying the mathematical properties of Shapley value (Alonso-Meijide et al. 2021, Leng et al. 2021) to applications such as the horizontal cooperation (e.g., resource sharing) between logistic service providers (Kimms and Kozeletskyi 2016) and the vertical coordination of supply chains (Zheng et al. 2019). Even though we drew our inspiration from the machine learning literature because of the importance of addressing the computational challenge and the close resemblance in problem formulation (as discussed earlier in the paper), we also acknowledge the relevance of our work to this broad literature in economic and business research.

Finally, recall from earlier discussions that the three axioms in our work are not the only possible ones fo fairness in risk-load allocation. A promising future research direction is to examine whether there are additional properties, such as those studied in the game theory literature (cf. Ko´czy 2018), which are potentially applicable to the notion of fairness in catastrophe insurance ratemaking. Interestingly, this is also an area in which the economic literature meets the recent work in machine learning, which suggest that many desirable properties of fairness may not be mathematically compatible with each other (Kleinberg et al. 2017). This (in)compatibility issue is evident in our context as the uniqueness result in Theorem 1 already indicates that, if the introduction of additional axioms shifts the allo cation mechanism away from Shapley value, then the new axioms must be mathematically incompatible with the current three (because no mechanism other than Shapley value can satisfy the current three axioms). Thus, future studies can explore the existence of other axioms for fair risk-load allocation and, if so, the trade offs a catastrophe insurer may have to make in determining which axioms to follow in allocating risk load to individual policies.

## Acknowledgments

The authors express their sincere gratitude to the editors and reviewers for their helpful comments. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not nec essarily reflect the views of the sponsors.

## Endnotes

<sup>1</sup> Whereas this problem is sometimes simply called data valuation in machine learning, we refer to it as “fair data valuation” to high light the importance of fairness as a design objective in data valuation (Jia et al. 2019b).

${ } ^ { 2 } p \in [ 0 , 1 ]$ is a predetermined parameter. Note that the p-quantile Q(p) is connected to the standard deviation σ through the inequality $Q ( p ) \leq \mu + \sigma { \sqrt { p / ( 1 - p ) } } ,$ , where µ is the mean loss.

<sup>3</sup> The specific names for these three variables are B01002\_001, B02001\_003, and B19119\_001, respectively.

## References

Abbasi A, Li J, Clifford G, Taylor H (2018) Make “fairness by design” part of machine learning. Harvard Bus. Rev. https://hbr. org/2018/08/make-fairness-by-design-part-of-machine-learning.

Acerbi C, Tasche D (2002) Expected shortfall: A natural coherent alternative to value at risk. Econom. Notes 31(2):379–388.

Adjerid I, Peer E, Acquisti A (2018) Beyond the privacy paradox: Objective vs. relative risk in privacy decision making. Manage ment Inform. Systems Quart. 42(2):465–488.

Akter S, Mallick B (2013) The poverty-vulnerability-resilience nexus: Evidence from Bangladesh. Ecological Econom. 96(1):114–124.

Alonso-Meijide JM, A<sup>´</sup> lvarez-Mozos M, Fiestras-Janeiro MG, Jime´nez-Losada A (2021) Marginality and convexity in partition function form games. Math. Methods Oper. Res. 94(1):99–121.

American Academy of Actuaries (2018) Uses of Catastrophe Model Output (American Academy of Actuaries, Washington, DC).

Angst CM, Block ES, D’arcy J, Kelley K (2017) When do it security investments matter? Accounting for the influence of institutional factors in the context of healthcare data breaches. Man agement Inform. Systems Quart. 41(3):893–916.

Arrow KJ (1978) Uncertainty and the welfare economics of medical care. Uncertainty in Economics (Academic Press, Cambridge, MA).

Artzner P, Delbaen F, Eber JM, Heath D (1999) Coherent measures of risk. Math. Finance 9(3):203–228.

Bachrach Y, Markakis E, Resnick E, Procaccia AD, Rosenschein JS, Saberi A (2010) Approximating power indices: Theoretical and empirical analysis. Autonomous Agents Multi-Agent Systems 20(2):105–122.

Baker T (2002) Risk, insurance, and the social construction of responsibility. Embracing Risk: The Changing Culture of Insurance and Responsibility, (University of Chicago Press, Chicago) 33–51.

Baker T (2011) Health insurance, risk, and responsibility after the Patient Protection and Affordable Care Act. Univ. Pennsylvania Law Rev. 159(6):1577–1622

Barrett M, Walsham G (1999) Electronic trading and work transfor mation in the London insurance market. Inform. Systems Res. 10(1):1–22.

Bassellier G, Benbasat I, Reich BH (2003) The influence of business managers’ IT competence on championing it. Inform. Systems Res. 14(4):317–336.

Berman R (2018) Beyond the last touch: Attribution in online adver tising. Marketing Sci. 37(5):771–792.

Bharosa N, Lee J, Janssen M (2010) Challenges and obstacles in sharing and coordinating information during multi-agency disaster

response: Propositions from field exercises. Inform. Systems Frontiers 12(1):49–65.

Bourbaki N (2008) Lie Groups and Lie Algebras (Springer Science & Business Media, New York).

Bu¨ hlmann H (1970) Mathematical Methods in Risk Theory (Springer Science & Business Media, New York).

Cahn AL (2008) Our rights are not cast in stone: Post-Katrina environmental red-lining and the need for a broad-based human right lawyering movement. Univ. Pennsylvania J. Law Soc. Change 12(1):37–71.

Castro J, Go´mez D, Tejada J (2009) Polynomial calculation of the Shap ley value based on sampling. Comput. Oper. Res. 36(5):1726–1730

Charpentier A, Barry L, James MR (2022) Insurance against natural catastrophes: Balancing actuarial fairness and social solidarity. Geneva Papers Risk Insurance-Issues Practice 47(1):50–78.

Colten CE (2006) Vulnerability and place: Flat land and uneven risk in New Orleans. Amer. Anthropologist 108(4):731–734.

Copeland TE, Weston JF, Shastri K (2005) Financial Theory and Corpo rate Policy, vol. 4 (Pearson, New York).

Cormen TH, Leiserson CE, Rivest RL, Stein C (2009) Introduction to Algorithms (MIT Press, Cambridge, MA).

Daniels N (1990) Insurability and the HIV epidemic: Ethical issues in underwriting. Milbank Quart. 68(4):497–525.

Deng X, Papadimitriou CH (1994) On the complexity of cooperative solution concepts. Math. Oper. Res. 19(2):257–266.

Dietz S, Nieho¨ rster F (2021) Pricing ambiguity in catastrophe risk insurance. Geneva Risk Insurance Rev. 46(2):112–132.

Dietz S, Walker O (2019) Ambiguity and insurance: Capital require ments and premiums. J. Risk Insurance 86(1):213–235.

Dong W, Shah H, Wong F (1996) A rational approach to pricing of catastrophe insurance. J. Risk Uncertainty 12(2):201–218.

Dwork C (2008) Differential privacy: A survey of results. Proc. Internat. Conf. Theory Appl. Models Comput., 1–19.

Embrechts P, Klu¨ ppelberg C, Mikosch T (2013) Modelling Extremal Events (Springer, Berlin).

Everett RS, Wojtkiewicz RA (2002) Difference, disparity, and race/ethnic bias in federal sentencing. J. Quant. Criminology 18(2):189–211.

Ewald F (2014) L’Etat Providence (Grasset, Paris).

Fatima SS, Wooldridge M, Jennings NR (2008) A linear approximation method for the Shapley value. Artificial Intelligence 172(14): 1673–1699.

Fothergill A (2006) In the Wake of the Storm: Environment, Disaster, and Race After Katrina (SAGE, New York).

Frezal S, Barry L (2020) Fairness in uncertainty: Some limits and misinterpretations of actuarial fairness. J. Bus. Ethics 167(1): 127–136.

Fu L, Khury C (2010) Optimal layers for catastrophe reinsurance Variance 4(2):191–208.

Ghorbani A, Zou J (2019) Data Shapley: Equitable valuation of data for machine learning. Proc. Machine Learn. Res. 97(1):2242–2251.

Goode S, Hoehle H, Venkatesh V, Brown SA (2017) User compensation as a data breach recovery action: An investigation of the Sony Playstation network breach. Management Inform. Systems Quart. 41(3):703–727.

Grossi P (2005) Catastrophe Modeling: A New Approach to Managing Risk (Springer, New York).

Gul F (1989) Bargaining foundations of Shapley value. Econometrica 57(1):81–95.

Ha J, Kose MA, Ohnsorge F (2021) One-stop source: A global database of inflation. Policy Research Working Paper 9737, World Bank, Washington, DC.

Heller D, Advocate C (2015) High price of mandatory auto insurance in predominantly African American communities. Technical Report 2015-11-18, Consumer Federation of America, Washington, DC.

Herepath A (2014) In the loop: A realist approach to structure and agency in the practice of strategy. Organ. Stud. 35(6):857–879.

Houston DB (1960) Risk theory. J. Insurance 27(1):77–82.

Huber PJ (1973) Robust regression: Asymptotics, conjectures and Monte Carlo. Ann. Statist. 1(5):799–821.

Jaffee DM, Russell T (1997) Catastrophe insurance, capital markets, and uninsurable risks. J. Risk Insurance 64(2):205–230.

Jia R, Dao D, Wang B, Hubis FA, Gurel NM, Zhang BLC, Song CSD (2019a) Efficient task-specific data valuation for nearest neigh bor algorithms. Proc. VLDB Endowment. 12(11):1610–1623.

Jia R, Dao D, Wang B, Hubis FA, Hynes N, Gu¨ rel NM, Li B, Zhang C, Song D, Spanos CJ (2019b) Toward efficient data valuation based on the Shapley value. Proc. Machine Learn. Res. 89(1): 1167–1176.

Kamijo Y, Kongo T (2010) Axiomatization of the Shapley value using the balanced cycle contributions property. Internat. J. Game Theory 39(4):563–571.

Kashmiri S, Nicol CD, Hsu L (2017) Birds of a feather: Intraindustry spillover of the target customer data breach and the shielding role of it, marketing, and CSR. J. Acad. Marketing Sci. 45(2):208–228.

Khan F, Kim JH, Mathiassen L, Moore R (2021) Data breach management: An integrated risk model. Inform. Management 58(1): 103392.

Kifer D, Machanavajjhala A (2011) No free lunch in data privacy. Proc. 2011 ACM SIGMOD Internat. Conf. Management Data, 193–204.

Kimms A, Kozeletskyi I (2016) Core-based cost allocation in the cooperative traveling salesman problem. Eur. J. Oper. Res. 248(3):910–916.

Kleinberg J, Mullainathan S, Raghavan M (2017) Inherent trade-offs in the fair determination of risk scores. Proc. Eighth Conf. Innova tions Theoretical Comput. Sci., 1–23.

Ko´czy LA <sup>´</sup> (2018) Partition Function Form Games, Theory and Decision Library C, vol. 48 (Springer, New York).

Kreps R (1990) Reinsurer risk loads from marginal surplus require ments. Proc. Casualty Actuarial Soc. 77:196–203.

Krieger N (1992) Overcoming the absence of socioeconomic data in medical records: Validation and application of a census-based methodology. Amer. J. Public Health 82(5):703–710.

Krishna V, Serrano R (1996) Multilateral bargaining. Rev. Econom. Stud. 63(1):61–80.

Landes X (2015) How fair is actuarial fairness? J. Bus. Ethics 128(3):519–533.

Lange JT (1969) Application of a mathematical concept of risk to property-liability insurance ratemaking. J. Risk Insurance 36(4): 383–391.

Lee YT, Sidford A (2015) Efficient inverse maintenance and faster algorithms for linear programming. 2015 IEEE 56th Annual Sympos. Foundations Comput. Sci., 230–249.

Lehtonen TK, Liukko J (2011) The forms and limits of insurance soli darity. J. Bus. Ethics 103(1):33–44.

Leng M, Luo C, Liang L (2021) Multiplayer allocations in the presence of diminishing marginal contributions: Cooperative game analysis and applications in management science. Managemen Sci. 67(5):2891–2903.

Maleki S, Tran-Thanh L, Hines G, Rahwan T, Rogers A (2013) Bounding the estimation error of sampling-based Shapley value approximation. Preprint, submitted June 18, https://arxiv.org/ abs/1306.4265.

Mango DF (1997) An application of game theory: Property catastro phe risk load. Proc. Casualty Actuarial Soc. 84:33–49.

McQuillin B, Sugden R (2016) Backward induction foundations of the Shapley value. Econometrica 84(6):2265–2280.

Mehta S, Dawande M, Janakiraman G, Mookerjee V (2021) How to sell a data set? Pricing policies for data monetization. Inform. Systems Res. 32(4):1281–1297.

Meyers G (1996) The competitive market equilibrium risk load formula for catastrophe ratemaking. Proc. Casualty Actuarial Soc. 83:563–600.

Meyers G, Van Hoyweghen I (2018) Enacting actuarial fairness in insurance: From fair discrimination to behaviour-based fairness. Sci. Culture 27(4):413–438.

Michalak TP, Aadithya KV, Szczepanski PL, Ravindran B, Jenning NR (2013) Efficient computation of the Shapley value for gametheoretic network centrality. J. Artificial Intelligence Res. 46(1): 607–650.

Michel-Kerjan EO (2010) Catastrophe economics: The national flood insurance program. J. Econom. Perspect. 24(4):165–186.

Milinski M, Sommerfeld RD, Krambeck HJ, Reed FA, Marotzke J (2008) The collective-risk social dilemma and the prevention of simulated dangerous climate change. Proc. Natl. Acad. Sci. USA 105(7):2291–2294.

Moulin H (1992) An application of the Shapley value to fair division with money. Econometrica 60(6):1331–1349.

Myerson RB (1980) Conference structures and fair allocation rules. Internat. J. Game Theory 9(3):169–182.

Nash JF (1950) The bargaining problem. Econometrica 18(1):155–162.

National Association of Insurance Commissioners (2020) NAIC announces special committee on race and insurance. Accessed January 15, 2022, https://content.naic.org/article/news\_release\_ naic\_announces\_special\_committee\_race\_and\_insurance.htm.

National Research Council (2004) Measuring Racial Discrimination (National Academies Press).

Nevo A (2001) Measuring market power in the ready-to-eat cereal industry. Econometrica 69(2):307–342.

Nicholson JE, Clark K, Daraskevich G (2018) The Florida insurance market: An analysis of vulnerabilities to future hurricane losses. J. Insurance Regulation 37(3):57–89.

Nussbaumer A, Pope A, Neville K (2023) A framework for applying ethics-by-design to decision support systems for emergency management. Inform. Systems J. 33(1):34–55.

Olivieri A, Pitacco E (2015) Introduction to Insurance Mathematics: Tech nical and Financial Features of Risk Transfers (Springer, New York).

Pager D, Shepherd H (2008) The sociology of discrimination: Racial discrimination in employment, housing, credit, and consumer markets. Annual Rev. Sociol. 34:181–209.

Pichler A (2014) Insurance pricing under ambiguity. Eur. Actuarial J. 4(2):335–364.

Plitt S, Maldonado D (2007) Prohibiting de facto insurance redlining: Will Hurricane Katrina draw a discriminatory redline in the Gulf Coast sands prohibiting access to home ownership. Wash ington Lee J. Civil Rights Soc. Justice 14(2):199–254.

Rai A (2020) Explainable AI: From black box to glass box. J. Acad. Marketing Sci. 48(1):137–141.

Rockafellar RT, Uryasev S (2002) Conditional value-at-risk for general loss distributions. J. Banking Finance 26(7):1443–1471.

Roth AE (1977) The Shapley value as a Von Neumann-Morgenstern utility. Econometrica 45(3):657–664.

Roth AE, Verrecchia RE (1979) The Shapley value as applied to cost allocation: A reinterpretation. J. Accounting Res. 17(1):295–303.

Sen R, Borle S (2015) Estimating the contextual risk of data breach: An empirical approach. J. Management Inform. Systems 32(2):314–341.

Shapley L (1951) Notes on the n-person game-II: The value of an nperson game. The RAND Corporation Research Memorandum 670.

Sharapov D, Kattuman P, Rodriguez D, Velazquez FJ (2021) Using the Shapley value approach to variance decomposition in strategy research: Diversification, internationalization, and corporate group effects on affiliate profitability. Strategic Management J. 42(3):608–623.

Short ED (1985) FDIC settlement practices and the size of failed banks. Econom. Rev. Federal Reserve Bank of Dallas, March 1985, 12–20.

Shubik M (2002) Game theory and operations research: Some musings 50 years later. Oper. Res. 50(1):192–196.

Smiley KT (2020) Social inequalities in flooding inside and outside of floodplains during Hurricane Harvey. Environ. Res. Lett. 15(9):0940b3.

Squires GD (2003) Racial profiling, insurance style: Insurance redlin ing and the uneven development of metropolitan areas. J. Urban Affairs 25(4):391–410.

Tang S, Ghorbani A, Yamashita R, Rehman S, Dunnmon JA, Zou J, Rubin DL (2021) Data valuation for medical imaging using Shapley value and application to a large-scale chest X-ray data set. Sci. Rep. 11(1):1–9.

Tarashev N, Tsatsaronis K, Borio C (2016) Risk attribution using the Shapley value: Methodology and policy applications. Rev. Finance 20(3):1189–1213.

Thomas RG (2007) Some novel perspectives on risk classification. Geneva Papers Risk Insurance Issues Practice 32(1):105–132.

Venezian EC (1985) Ratemaking methods and profit cycles in property and liability insurance. J. Risk Insurance 52(1):477–500.

Verma V, Kawaguchi K, Lamb A, Kannala J, Solin A, Bengio Y, Lopez-Paz D (2022) Interpolation consistency training for semisupervised learning. Neural Networks 145(1):90–106.

Wang SS, Young VR, Panjer HH (1997) Axiomatic characterization of insurance prices. Insurance Math. Econom. 21(2):173–183.

White H (1980) A heteroskedasticity-consistent covariance matrix estimator and a direct test for heteroskedasticity. Econometrica 48(4):817–838.

Xu H, Zhang N (2022) Implications of data anonymization on the statistical evidence of disparity. Management Sci. 68(4):2600– 2618.

Xu Y, Armony M, Ghose A (2021) The interplay between online reviews and physician demand: An empirical investigation. Management Sci. 67(12):7344–7361.

Zhang X, Du Q, Zhang Z (2022) A theory-driven machine learning system for financial disinformation detection. Production Oper. Management 31(8):3160–3179.

Zhang X, Pe´rez-Stable EJ, Bourne PE, Peprah E, Duru OK, Breen N, Berrigan D, et al. (2017) Big data science: Opportunities and challenges to address minority health and health disparities in the 21st century. Ethnicity Disease 27(2):95–106.

Zheng XX, Li DF, Liu Z, Jia F, Sheu JB (2019) Coordinating a closed-loop supply chain with fairness concerns through variable-weighted Shapley values. Transportation Res. Part E Logist. Transportation Rev. 126:227–253.

Zhou WX, Bose K, Fan J, Liu H (2018) A new perspective on robust m-estimation: Finite sample theory and application to dependence-adjusted multiple testing. Ann. Statist. 46(5): 1904–1931.

C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pera</sub>ti<sub>ons</sub> R<sub>esearc</sub>h & th<sub>e</sub> M<sub>anagemen</sub>t S<sub>c</sub>i<sub>ences an</sub>d it<sub>s con</sub>t<sub>en</sub>t <sub>may no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or</sub> <sub>ema</sub>il<sub>e</sub>d t<sub>o</sub> <sub>mu</sub>lti<sub>p</sub>l<sub>e</sub> <sub>s</sub>it<sub>es</sub> <sub>or</sub> <sub>pos</sub>t<sub>e</sub>d t<sub>o</sub> <sub>a</sub> li<sub>s</sub>t<sub>serv</sub> <sub>w</sub>ith<sub>ou</sub>t th<sub>e</sub> <sub>copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup> <sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use.</sub>
