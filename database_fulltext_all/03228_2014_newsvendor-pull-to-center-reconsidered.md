---
otero_id: 3228
otero_key: "FXBGWGZA"
title: "Newsvendor pull-to-center reconsidered"
authors: "Nelson Lau; Sameer Hasija; J. Neil Bearden"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.041"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Nelson Lau ⁎, Sameer Hasija, J. Neil Bearden

INSEAD, 1 Ayer Rajah Ave, 136676, Singapore

a r t i c l e i n f o

Available online 16 January 2013

Keywords: Behavioral operations management Newsvendor problem Pull-to-center Measurement and methodology Experimental economics

## a b s t r a c t

In the newsvendor problem, a pull-to-center effect has been asserted, whereby subjects are said to order a quantity between the mean of the demand distribution and the expected pro<sup>fi</sup>t-maximizing quantity. These claims have only been examined using group-level aggregate statistics. Looking at individual-level data from a previously published study and a new experiment, the current paper shows that while pull-to-center is present in aggregate data, it does not adequately describe the population of individual decision makers, who are found to be highly heterogeneous. Methodological implications and future research directions are discussed.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Extant literature has asserted the existence of a pull-to-center effect in empirical newsvendor behavior (see [4,6,9,27,29,39], among others). This implies that instead of ordering the expected pro<sup>fi</sup>t maximizing quantity (q\*), actual subjects order a quantity between q\* and the mean of the demand distribution (d).<sup>1,2</sup>

Research to date has assumed that the pull-to-center effect is a characteristic property of individual behavior. For example, Schweitzer and Cachon [39] stated that “subjects consistently order amounts lower than the expected pro<sup>fi</sup>t-maximizing quantity for high-pro<sup>fi</sup>t products and higher than the expected pro<sup>fi</sup>t-maximizing quantity for low-pro<sup>fi</sup>t products” (p. 418).

Based on this assumption, attempts have been made to explain the pull-to-center phenomenon. Individual decision making rules such as the “mean anchor heuristic” [39] (p. 409) have been proposed. Design factors such as the uncensored presentation of demand information have been advanced as explanations [37]. Models of individual ordering behavior based on bounded rationality have been suggested, with some success at replicating a pull-to-center ordering pattern [41].

Attempting to explain a phenomenon presumes its existence. However, evidence for pull-to-center has been based on aggregate data. For instance, [39] reported that in Experiment 1, “the average order quantities across all inventory decisions… exhibited the too low/too high pattern”

(p. 411), while in Experiment 2, “the average order quantities under the low-pro<sup>fi</sup>t condition [were] signi<sup>fi</sup>cantly above the expected pro<sup>fi</sup>tmaximizing quantities” (p. 415).

Aggregate averages can be misleading. If a distributor has a customer pool that consists of 50% small retailers buying products in 100-unit orders and 50% large retailers buying products in 10,000-unit orders, the average order size is 5050. However, this average is not representative of the population, and describes a type of customer who does not exist (example derived from [38]).

The current paper demonstrates that the same is true of newsvendor behavior. When group data are averaged, pull-to-center is observed. However, inspecting individual data reveals that ordering behavior is heterogeneous. It is obvious and unsurprising that not all subjects adhere to pull-to-center. What is unobvious and surprising is that most subjects do not exhibit this behavior. This has important implications, as existing literature suggests the opposite.

In particular, the identi<sup>fi</sup>cation of behavioral and cognitive biases is extremely important in advancing the practice of information system design. If pull-to-center is a commonly observed phenomenon in individual behavior, it deserves consideration in supply chain information system design. However, the results of this study suggest otherwise. This informs current design discussions and urges a meaningful reconsideration of research practices in behavioral investigations.

## 2. Experimental evidence

Two sources of data are used in the current paper. The <sup>fi</sup>rst is Study 1 of Bolton and Katok [6]. These authors presented 20 subjects with a low margin newsvendor problem and 18 subjects with a high margin problem, both for 100 seasons of demand. The second is a new experiment conducted based on [39]. 94 participants were presented with a low margin set-up and 80 participants with a high margin set-up, both for

Implicit de<sup>fi</sup>nitions of pull-to-center in extant literature.

<table><tr><td>Paper</td><td>Implicit definition</td></tr><tr><td>[6]</td><td>“Plots for both conditions show average orders falling between average demand and the optimal order” (p. 525)</td></tr><tr><td rowspan="2">[7]</td><td>“Orders tend to be biased away from the expected profit maximizing order and towards the average demand, an effect known as ‘anchoring bias.’” (p. 1)</td></tr><tr><td>“Managers largely exhibit the same qualitative pattern of ordering bias as do students: They anchor between the optimal order and average demand and they exhibit little longitudinal adjustment in this behavior.” (p. 13)</td></tr><tr><td>[12]</td><td>“The pull-to-center effect predicts that individuals are biased towards the center of the distribution, 10.5, causing actual orders to be somewhere between 13 and 10.5 for the high-profit condition, and somewhere between 8 and 10.5 for the low-profit condition.” (p. 19)</td></tr><tr><td rowspan="2">[21]</td><td>“When explaining the ‘pull-to-center’ effect in the newsvendor problem observed in experimental data from American subjects, Schweitzer and Cachon proposed the ‘anchoring and insufficient adjustment’ bias, i.e., decision makers tend to anchor on the mean demand and insufficiently adjust toward the optimal quantity.” (p. 42-3)</td></tr><tr><td>“We can see that the ‘pull-to-center’ effect also appeared for Chinese subjects, as repeatedly observed from American subjects in the previous literature. That is, under both conditions, Chinese subjects’ average order quantities fell between the optimal order quantity of 75 and the mean demand (centered at 50 or 100 in the two conditions)” (p. 43)</td></tr><tr><td>[25]</td><td>“So average orders are between the optimal level and the average demand. This pattern has been termed the ‘pull-to-center’ effect.” (p. 35)</td></tr><tr><td>[27]</td><td>“Define subject i’s choices as mean ordering if in both the LP and the HP conditions the average order quantity  $q_i^T$  is biased toward mean demand, but not beyond.” (p. 678)</td></tr><tr><td rowspan="3">[37]</td><td>“Subjects tend to order below the normative quantity when facing high margin and above the normative quantity when facing low margin, but in neither case beyond mean demand (a.k.a. the pull-to-center effect).” (Abstract)</td></tr><tr><td>“Schweitzer and Cachon (2000) find support for the pull-to-center effect, i.e., a tendency to order between the normative solution and expected demand, which is consistent with anchoring and insufficient adjustment as well as ex-post inventory error minimization.” (p. 11)</td></tr><tr><td>“Pull-to-center regions, which has bounds established by expected demand and the normative order quantity.” (p. 12)</td></tr></table>

20 seasons of demand. Subjects were from Amazon Mechanical Turk (AMT), and compensation was awarded in an incentive compatible fashion (see [23,26,31,36] on the reliability of AMT for experiments).<sup>3</sup>

## 2.1. Aggregate summary statistics

Table 2 displays the mean orders for all four experiments. In every case, the average subject's order lies in the open interval bounded by d and q\*.<sup>4</sup> The difference between the mean order and ${ \mathfrak { q } } ^ { * }$ is subjected to a Wilcoxon signed-rank test, and the p-value in every experiment indicates statistical signi<sup>fi</sup>cance. Pull-to-center is observed in aggregate data.

## 2.2. Individual histograms

If pull-to-center characterized individual behavior, and there was no variability in ordering, then the histograms of individual orders would all be mass points at a quantity in the PTC zone. Incorporating variability in orders, each histogram should be a distribution with a mean in the PTC zone, and some noise around this mean. If the ordering process is thought to follow a quantal choice model such as in [41], or if variance in orders is believed to simply be noise around a target order quantity, then each individual histogram of orders can be expected to follow a truncated normal distribution.

Fig. 1 shows the histograms of individual orders in BKL. There is signi<sup>fi</sup>cant heterogeneity in behavior. Subjects 6 and 15 order exclusively above the PTC zone; Subjects 13 and 14 order exclusively below the PTC zone; Subjects 1 and 2 order ${ \mathfrak { q } } ^ { * }$ in virtually all seasons. Although summary statistics (Table 2) show the pull-to-center on group-level data, examining individual data reveals it to be less common than previously thought. The individual histograms for BKH, MTL, and MTH are available on request. These <sup>fi</sup>gures again indicate the subject heterogeneity and substantial absence of pull-to-center in individual data.

## Table 2

Aggregate summary statistics.

<table><tr><td>Experiment</td><td> $\overline{d}$ </td><td> $q^*$ </td><td>Mean order</td><td>p-Value for difference from  $q^*$ </td></tr><tr><td>BKL</td><td>100</td><td>75</td><td>88</td><td>&lt;0.001</td></tr><tr><td>BKH</td><td>50</td><td>75</td><td>61</td><td>&lt;0.001</td></tr><tr><td>MTL</td><td>100</td><td>75</td><td>90</td><td>&lt;0.001</td></tr><tr><td>MTH</td><td>50</td><td>75</td><td>53</td><td>&lt;0.001</td></tr></table>

## 2.3. Percentage of orders in PTC zone

From a de<sup>fi</sup>nitional standpoint, if pull-to-center characterizes an individual's ordering behavior, then it is fair to expect the participant's order quantity distribution to be concentrated within the PTC zone.<sup>5</sup>

The mean anchor heuristic suggested by Schweitzer and Cachon [39] – “a decision maker anchors on mean demand and adjusts towards the optimal order quantity” (p. 409) – is both a proposed explanation for and de<sup>fi</sup>nition of pull-to-center. If this holds, individuals' orders should lie exclusively in the PTC zone. Allowing for random errors in ordering decisions, the majority of individuals' orders should still lie in the PTC zone.

Fig. 2 shows the histogram of subjects by their percentage of orders in the PTC zone. For example, in BKL, the leftmost bar with a height of 50% means that half of the subjects placed between 0% and 10% of their orders in the PTC zone, and thus 90% to 100% of their orders outside the PTC zone.

If pull-to-center is present in individual ordering, then in Fig. 2, almost all the mass should be on the right in each graph. Using a generous de<sup>fi</sup>- nition – that pull-to-center applies to an individual when 50% or more of their orders are in the PTC zone – only 35% of subjects in BKL, 33% in BKH, 24% in MTL, and 15% in MTH can be said to exhibit pull-to-center.

## 2.4. Mean, median, and modal order quantities

A looser de<sup>fi</sup>nition of pull-to-center would be that an individual's average order quantity lies in the PTC zone. This would also follow as a consequence of the mean anchor heuristic.

Table 3 summarizes the proportion of subjects with average order quantities inside or outside the PTC zone. The average is calculated using the mean, median, and mode, as displayed in the top, middle, and

## Bolton & Katok 2008 - Study 1 (Low Margin Condition)

![](/api/attachments/FXBGWGZA/fulltext/images/0e39853ef31c1b57c6f12fff0fafb87372daaa8ac740412041c9dfbcd1cebadd.jpg)  
Fig. 1. Histograms of individual ordering distributions in BKL.

bottom panels respectively. Table 3 also provides information about the percentage of subjects whose average orders were below or above the PTC zone.

![](/api/attachments/FXBGWGZA/fulltext/images/5aa5aeb1822658c25be0ba9dc4cbc5a731735280894d055c37bf9b65ee97b41c.jpg)

Thus, across the four experiments, between 28% and 45% of subjects have mean orders outside the PTC zone. Between 39% and 61% of subjects have median orders outside the PTC zone. Finally, between 56% and 76% of subjects have modal orders outside the PTC zone. These percentages indicate subjects who do not exhibit pull-to-center.

![](/api/attachments/FXBGWGZA/fulltext/images/b54a69162fb3c8497a42b9e4e3919464b1bc52790e10b2ef5c17397bcfc909cd.jpg)

![](/api/attachments/FXBGWGZA/fulltext/images/b5bf6147ef8f1473864c5494a4ede0fe3776106eaa091362ec89570bd88564dc.jpg)

![](/api/attachments/FXBGWGZA/fulltext/images/d5f86beced83453cb3248de4ba1d6b293399ad2d5eef7fcb4943d26647a031f5.jpg)  
Fig. 2. Percentage of orders in PTC zone.

Table 3  
Mean, median, and modal orders.

<table><tr><td>Measure</td><td>Experiment</td><td>Inside PTC zone</td><td>Below PTC zone</td><td>Above PTC zone</td><td>Outside PTC zone</td></tr><tr><td rowspan="4">Mean</td><td>BKL</td><td>70%</td><td>15%</td><td>15%</td><td>30%</td></tr><tr><td>BKH</td><td>72%</td><td>17%</td><td>11%</td><td>28%</td></tr><tr><td>MTL</td><td>67%</td><td>11%</td><td>22%</td><td>33%</td></tr><tr><td>MTH</td><td>55%</td><td>40%</td><td>5%</td><td>45%</td></tr><tr><td rowspan="4">Median</td><td>BKL</td><td>45%</td><td>30%</td><td>25%</td><td>55%</td></tr><tr><td>BKH</td><td>61%</td><td>28%</td><td>11%</td><td>39%</td></tr><tr><td>MTL</td><td>52%</td><td>17%</td><td>31%</td><td>48%</td></tr><tr><td>MTH</td><td>39%</td><td>54%</td><td>8%</td><td>61%</td></tr><tr><td rowspan="4">Mode</td><td>BKL</td><td>35%</td><td>35%</td><td>30%</td><td>65%</td></tr><tr><td>BKH</td><td>44%</td><td>39%</td><td>17%</td><td>56%</td></tr><tr><td>MTL</td><td>34%</td><td>19%</td><td>47%</td><td>66%</td></tr><tr><td>MTH</td><td>24%</td><td>59%</td><td>18%</td><td>76%</td></tr></table>

## 2.5. Bostian α-coefficients

Bostian et al. [9] operationalize the mean anchor heuristic as:

$$
q _ {t} = \overline {{d}} + \alpha \left(\mathbf {q} ^ {*} - \overline {{d}}\right) + \varepsilon_ {t}\tag{1}
$$

where α re<sup>fl</sup>ects the “extent of rationality” i.e., how far subjects deviate from the mean of the demand distribution towards $\boldsymbol { \mathrm { q } } ^ { * }$ (p. 594). Regressing $\left( q _ { t } - \overline { { d } } \right)$ on $\left( q ^ { * } - { \overline { { d } } } \right)$ thus yields the “Bostian α-coef<sup>fi</sup>cient,” which must lie in $( \tilde { 0 } , 1 )$ to be consistent with mean anchoring and consequently pull-to-center.

Table 4 classi<sup>fi</sup>es the estimated α-coef<sup>fi</sup>cients obtained from individual regressions. Across the four studies, between 28% and 45% of individuals have α-coef<sup>fi</sup>cients outside (0, 1), which is not consistent with pull-to-center.<sup>6</sup> The table also shows that the proportion of subjects with α-coef<sup>fi</sup>cients inside (0, 1) that are signi<sup>fi</sup>cant at the 0.05 level ranges between just 32% and 60%.

## 2.6. Convergence

Benzion et al. [4] study learning and convergence, asserting that orders “converge to a value between the mean demand and the quantity for maximizing the expected pro<sup>fi</sup>t” (abstract). If this alternate de<sup>fi</sup>nition of pull-to-center holds in individual data, then in the <sup>fi</sup>nal seasons of the experiment, subjects should be observed ordering quantities in the PTC zone.

Table 5 shows the percentage of subjects whose mean orders over a speci<sup>fi</sup>ed number of <sup>fi</sup>nal seasons lie in the PTC zone. The three panels of the table analyze these means for the last season of ordering, the last 25% of seasons (i.e., 25 seasons in BKL and BKH and 5 seasons in MTL and MTH), and the last 50% of seasons (i.e., 50 seasons in BKL and BKH and 10 seasons in MTL and MTH).

In the terminal season, between 62% and 83% placed orders outside the PTC zone (not consistent with pull-to-center). Across all four experiments, varying the number of ending seasons examined, between 28% and 83% of subjects converged to mean orders outside the PTC zone.

## 2.7. Tests of the prevalence of pull-to-center

Sections 2.1 to 2.6 established that looking only at aggregate means is quite misleading; individual order distributions are markedly more diverse. Pull-to-center is not a useful summary of empirical behavior – by some de<sup>fi</sup>nitions, most subjects do not behave in a manner consistent with the proposed effect.

Table 4  
Bostian α-coef<sup>fi</sup>cient.

<table><tr><td>Experiment</td><td>Inside (0, 1)</td><td>Inside (0, 1) and p&lt;0.05</td><td>Below (0, 1)</td><td>Above (0, 1)</td><td>Outside (0, 1)</td></tr><tr><td>BKL</td><td>70%</td><td>60%</td><td>15%</td><td>15%</td><td>30%</td></tr><tr><td>BKH</td><td>72%</td><td>56%</td><td>17%</td><td>11%</td><td>28%</td></tr><tr><td>MTL</td><td>67%</td><td>46%</td><td>22%</td><td>11%</td><td>33%</td></tr><tr><td>MTH</td><td>55%</td><td>32%</td><td>40%</td><td>5%</td><td>45%</td></tr></table>

However, extant research often presumes pull-to-center to be a fundamental and universal characteristic of empirical behavior. A clear example is found in papers that attempt to explain pull-to-center or some aspect of it (e.g., [13,15,32,33], or the references in Section 1). Several papers also attempt to build models of individual behavior, and include pull-to-center as a key component [4,9,28].

Thus, as a further analysis, this section explores the extent to which pull-to-center can be formally rejected as a ubiquitous feature of individual behavior. For each of the measures in Sections 2.3 to 2.6, we statistically test the null hypothesis that pull-to-center applies to the majority of subjects. Speci<sup>fi</sup>cally, we test ${ } ^ { \mathfrak { w } } \mathrm { H } _ { 0 } \colon$ The proportion of individuals exhibiting pull-to-center $\geq x ^ { \prime \prime }$ against $\mathrm { \ddot { H } A \dot { : } }$ The proportion of individuals exhibiting pull-to-center $< x " ;$ one-tailed exact binomial tests were used. Three values of x were used – 50%, 75%, and 90% – representing different levels of prevalence of pull-to-center. To be clear: these tests asked whether the observed sample of individual responses were consistent with a population where a proportion x of individuals exhibited pull-to-center. Rejecting the null hypothesis implies that prevalence of pull-to-center in the population is lower than x.

Table 6 summarizes the binomial tests of prevalence based on the percentage of orders in the PTC zone (cf. Section 2.3). An individual was classi<sup>fi</sup>ed as exhibiting pull-to-center if at least 50% of his orders were in the PTC zone. In almost all experiments, the null hypotheses that the proportion of individuals exhibiting pull-to-center is at least 90%, 75%, or 50%, were rejected at a signi<sup>fi</sup>cance level of 0.05. The exceptions were x=50% in BKL and BKH, which had fewer subjects

A meta-analysis of the results from the four experiments was performed, using Fisher's combined probability test [8,17,22,24,34]. This test combines the p-values from the studies into a $\chi ^ { 2 }$ statistic with eight degrees-of-freedom. It is applicable in this context as each study used different subjects (no subject participated in more than one study), assuring that the test statistics being combined are independent. The meta-analyses test ${ } ^ { \mathrm { { * } } } \mathrm { { H } } _ { 0 } { \mathrm { { : } } }$ The proportion of individuals exhibiting pull-to-center ≥x in all studies” against “H : The proportion of individuals exhibiting pull-to-center bx in at least one study.” As shown in Table 6, the meta-analysis of BKL, BKH, MTL, and MTH rejects the null hypothesis that the proportion of individuals exhibiting pull-to-center is at least 90% in every study, at a signi<sup>fi</sup>cance level of 0.05. The meta-analyses similarly reject the null hypothesis that the proportion is at least 75% in all studies and the null hypothesis that it is at least 50% in all studies.

<table><tr><td>Number of Terminal Seasons</td><td>Experiment</td><td>Inside PTC zone</td><td>Below PTC zone</td><td>Above PTC zone</td><td>Outside PTC zone</td></tr><tr><td rowspan="4">1</td><td>BKL</td><td>30%</td><td>35%</td><td>35%</td><td>70%</td></tr><tr><td>BKH</td><td>33%</td><td>28%</td><td>39%</td><td>67%</td></tr><tr><td>MTL</td><td>38%</td><td>24%</td><td>37%</td><td>62%</td></tr><tr><td>MTH</td><td>18%</td><td>58%</td><td>25%</td><td>83%</td></tr><tr><td rowspan="4">BKL/BKH: 25 MTL/MTH: 5</td><td>BKL</td><td>55%</td><td>25%</td><td>20%</td><td>45%</td></tr><tr><td>BKH</td><td>67%</td><td>11%</td><td>22%</td><td>33%</td></tr><tr><td>MTL</td><td>62%</td><td>10%</td><td>29%</td><td>38%</td></tr><tr><td>MTH</td><td>49%</td><td>40%</td><td>11%</td><td>51%</td></tr><tr><td rowspan="4">BKL/BKH: 50 MTL/MTH: 10</td><td>BKL</td><td>60%</td><td>20%</td><td>20%</td><td>40%</td></tr><tr><td>BKH</td><td>72%</td><td>11%</td><td>17%</td><td>28%</td></tr><tr><td>MTL</td><td>64%</td><td>11%</td><td>26%</td><td>36%</td></tr><tr><td>MTH</td><td>49%</td><td>39%</td><td>13%</td><td>51%</td></tr></table>

Table 6  
Binomial tests of prevalence: Percentage of orders in PTC zone.

<table><tr><td>Experiment</td><td>x=90% p-value</td><td>x=75% p-value</td><td>x=50% p-value</td></tr><tr><td>BKL</td><td>&lt;0.001</td><td>&lt;0.001</td><td>0.132</td></tr><tr><td>BKH</td><td>&lt;0.001</td><td>&lt;0.001</td><td>0.119</td></tr><tr><td>MTL</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td></tr><tr><td>MTH</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td></tr><tr><td>Meta-analysis:  $\chi^2$ </td><td>559.49</td><td>275.77</td><td>85.04</td></tr><tr><td>Meta-analysis: p-value</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td></tr></table>

Table 7 shows the prevalence test results based on the mean, median, and modal orders (cf. Section 2.4). An individual was considered as exhibiting pull-to-center if his average order (based on the mean, median, or mode) was in the PTC zone. Using a signi<sup>fi</sup>cance level of 0.05, the null hypothesis of 90% prevalence was rejected for all three measures in all studies. The null hypothesis of 75% prevalence was rejected in almost all studies. The null hypothesis of 50% prevalence for the median order in MTH, and for the modal order in MTL and MTH was rejected. The meta-analyses reveal that the null hypothesis for 90% and 75% prevalence in every study can be rejected for all measures. The null hypothesis for 50% prevalence in all studies can be rejected when looking at modal orders.

The results for the Bostian α-coef<sup>fi</sup>cient of Section 2.5 are shown in Table 8. An individual was considered as exhibiting pull-to-center if his estimated α was in (0, 1). Note that this is equivalent to requiring an individual's mean order to be in the PTC zone — and thus the results are identical to the top panel of Table 7.

Finally, the prevalence test results for convergence (cf. Section 2.6) are displayed in Table 9. Here, only the last season of ordering was taken into account, and an individual was considered to exhibit pull-to-center if his terminal order falls in the PTC zone. At a signi<sup>fi</sup>cance level of 0.05, the null hypotheses of prevalence at 90%, 75%, and 50% can be rejected in virtually all studies. This is reinforced by the meta-analyses, which reject all the prevalence null hypotheses – 90%, 75%, and 50% in all studies – at a significance level of 0.05.

Overall, there is evidence against pull-to-center being a prevalent characteristic of individual behavior. Note that the results in this section constitute a modus tollens rejection: asserting that pull-to-center is prevalent implies as a consequence the null hypotheses for each study, as explored in Tables 6–9; evidence against any one of these hypotheses falsi<sup>fi</sup>es the assertion. However, it is worth reiterating the central message — pull-to-center is repeatedly observed when looking at aggregate statistics; individual behavior is heterogeneous, and is not well described by the pull-to-center effect.

Binomial tests of prevalence: Mean, median, and modal orders.

<table><tr><td>Measure</td><td>Experiment</td><td>x=90%p-value</td><td>x=75%p-value</td><td>x=50%p-value</td></tr><tr><td rowspan="6">Mean</td><td>BKL</td><td>0.011</td><td>0.383</td><td>0.979</td></tr><tr><td>BKH</td><td>0.028</td><td>0.481</td><td>0.985</td></tr><tr><td>MTL</td><td>&lt;0.001</td><td>0.051</td><td>1.000</td></tr><tr><td>MTH</td><td>&lt;0.001</td><td>&lt;0.001</td><td>0.843</td></tr><tr><td>Meta-analysis:  $\chi^2$ </td><td>126.85</td><td>28.23</td><td>0.42</td></tr><tr><td>Meta-analysis: p-value</td><td>&lt;0.001</td><td>0.004</td><td>1.000</td></tr><tr><td rowspan="6">Median</td><td>BKL</td><td>&lt;0.001</td><td>0.004</td><td>0.412</td></tr><tr><td>BKH</td><td>0.001</td><td>0.139</td><td>0.881</td></tr><tr><td>MTL</td><td>&lt;0.001</td><td>&lt;0.001</td><td>0.697</td></tr><tr><td>MTH</td><td>&lt;0.001</td><td>&lt;0.001</td><td>0.028</td></tr><tr><td>Meta-analysis:  $\chi^2$ </td><td>264.00</td><td>93.19</td><td>9.88</td></tr><tr><td>Meta-analysis: p-value</td><td>&lt;0.001</td><td>&lt;0.001</td><td>0.27</td></tr><tr><td rowspan="6">Mode</td><td>BKL</td><td>&lt;0.001</td><td>&lt;0.001</td><td>0.132</td></tr><tr><td>BKH</td><td>&lt;0.001</td><td>0.005</td><td>0.407</td></tr><tr><td>MTL</td><td>&lt;0.001</td><td>&lt;0.001</td><td>0.001</td></tr><tr><td>MTH</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td></tr><tr><td>Meta-analysis:  $\chi^2$ </td><td>443.05</td><td>198.56</td><td>46.16</td></tr><tr><td>Meta-analysis: p-value</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td></tr></table>

Table 8  
Binomial tests of prevalence: Bostian α-coef<sup>fi</sup>cient.

<table><tr><td>Experiment</td><td>x=90% p-value</td><td>x=75% p-value</td><td>x=50% p-value</td></tr><tr><td>BKL</td><td>0.011</td><td>0.383</td><td>0.979</td></tr><tr><td>BKH</td><td>0.028</td><td>0.481</td><td>0.985</td></tr><tr><td>MTL</td><td>&lt;0.001</td><td>0.051</td><td>1.000</td></tr><tr><td>MTH</td><td>&lt;0.001</td><td>&lt;0.001</td><td>0.843</td></tr><tr><td>Meta-analysis:  $\chi^2$ </td><td>126.85</td><td>28.23</td><td>0.42</td></tr><tr><td>Meta-analysis: p-value</td><td>&lt;0.001</td><td>&lt;0.001</td><td>1.000</td></tr></table>

## 3. Conclusion

The following statement summarizes the current paper<sup>7</sup>:

What was thought to be a single phenomenon is in reality composed of assorted heterogeneous elements.

Drawing conclusions about individual behavior from aggregate data invokes an implicit representativeness assumption. In some instances, this can be misleading (see the discussions in the Mathematical Psychology and Psychonomics Literature — [2,18–20,40], among others). However, there exist situations in which it is appropriate to make inferences from group data (a recent example is [35]). To differentiate between the two cases, it is important to assess the heterogeneity in individual responses, and the extent to which aggregate summary statistics are representative of the variety of agents' behaviors. In short, the representativeness assumption must be veri<sup>fi</sup>ed.

To be clear, simpli<sup>fi</sup>cation need not be avoided. It is important in advancing theory and knowledge, especially as part of model building. The concern is whether the suggested simpli<sup>fi</sup>cation is appropriate (see [1] for a valuable discussion).

Pull-to-center may be an inappropriate simpli<sup>fi</sup>cation.

Imagine a model of behavior based on pull-to-center was adopted. A distributor of goods faces a retailer population similar to Fig. 1, and makes decisions based on this model. The distributor would end up acting sub-optimally when facing retailers like Subjects 1, 2, 6, 13, 14, or 15, among others. More broadly, based on the analyses in Sections 2.3 to 2.6, a pull-to-center model would be inaccurate when dealing with a very signi<sup>fi</sup>cant proportion of actual agents.

Similarly, consider a <sup>fi</sup>rm with many retail outlets, each having a manager who makes decisions at the local level. It looks at summary statistics of its managers' aggregated ordering behavior, and observes a pull-to-center effect. The <sup>fi</sup>rm then implements changes to its information system in an attempt to correct for this presumed bias. Despite observing pull-to-center in the group summary statistics, the majority of managers might not be helped by the change in the information system. These managers may even veer further away from optimality, and the result of the change – which may surprise the <sup>fi</sup>rm – is lower overall performance.

This point is well recognized by Becker-Peth et al. [3], (among other <sup>fi</sup>ndings) contrast the outcome of using the optimal contract based on an aggregate behavioral model against the outcome of using individually optimal contracts. In general, it should be noted that research in behavioral operations has not been blind to heterogeneity in individual responses. Wu and Chen [42] parameterize newsvendor types and analyze the optimal contract type based on the value of the type parameter. De Véricourt et al. [16] explore individual differences explaining variations in newsvendor ordering tendencies. Unfortunately, these best practices are far from universal, and the current paper seeks merely to encourage improvement on this front.

Table 9  
Binomial tests of prevalence: Convergence.

<table><tr><td>Experiment</td><td>x=90% p-value</td><td>x=75% p-value</td><td>x=50% p-value</td></tr><tr><td>BKL</td><td>&lt;0.001</td><td>&lt;0.001</td><td>0.058</td></tr><tr><td>BKH</td><td>&lt;0.001</td><td>&lt;0.001</td><td>0.119</td></tr><tr><td>MTL</td><td>&lt;0.001</td><td>&lt;0.001</td><td>0.015</td></tr><tr><td>MTH</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td></tr><tr><td>Meta-analysis:  $\chi^2$ </td><td>472.61</td><td>219.51</td><td>58.93</td></tr><tr><td>Meta-analysis: p-value</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td></tr></table>

In closing, we note that the pull-to-center effect does not accurately describe individual behavior. Thus, models based on it cannot even function as “useful <sup>fi</sup>ctions” [30] or “as-if” models [5]. Predictions of subject behavior based on pull-to-center are inaccurate; it is not a useful starting point for investigating individual decision making in the newsvendor problem, and should be reconsidered.

## Acknowledgments

This research was funded by the INSEAD Alumni Fund.

## References

[1] M. Anderson, MIT scientists declare there is no science of brains! In after phrenology. Available online http://www.psychologytoday.com/blog/after phrenology/201109/mit-scientists-declare-there-is-no-science-brains.

[2] D. Bakan, A generalization of Sidman's results on group and individual functions, and a criterion, Psychological Bulletin 51 (1) (1954) 63–64.

[3] M. Becker-Peth, E. Katok, U.W. Thonemann, Designing contracts for irrational but predictable newsvendors, Working Paper, University of Cologne, 2011.

[4] U. Benzion, Y. Cohen, R. Peled, T. Shavit, Decision-making and the newsvendor problem: an experimental study, Journal of the Operations Research Society 59 (9) (2008) 1281–1287.

[5] N. Berg, G. Gigerenzer, As-if behavioral economics: neoclassical economics in disguise? History of Economic Ideas 18 (1) (2010) 133–165.

[6] G.E. Bolton, E. Katok, Learning by doing in the newsvendor problem: a laboratory investigation of the role of experience and feedback, Manufacturing & Service Operations Management 10 (3) (2008) 519–538.

[7] G.E. Bolton, A. Ockenfels, U. Thonemann, Managers and students as newsvendors: how out-of-task experience matters, Working Paper, University of Cologne, 2008.

[8] M. Borenstein, L.V. Hedges, J.P.T. Higgins, H.R. Rothstein, Meta-analysis Methods Based on Direction and p-Values, in Introduction to Meta-analysis, John Wiley & Sons, United Kingdom, 2009, pp. 325 –330.

[9] A.J.A. Bostian, C.A. Holt, A.M. Smith, Newsvendor “pull-to-center” effect: adaptive learning in a laboratory experiment, Manufacturing & Service Operations Management 10 (4) (2008) 590–608.

[10] G.P. Cachon, Interesting, really interesting, and maybe even fascinating research in O. M., M&SOM 2011 Fellow Presentation (2011). Available online http://prezi. com/z4hb9phbhsp8/gerard-cachon-msom-fellow-presentation.

[11] G.P. Cachon, C. Terwiesch, Betting on Uncertain Demand: The Newsvendor Model, Matching Supply with Demand, Intl. Ed. McGraw-Hill, Singapore, 2009, pp. 220–255.

[12] L. Chen, A.G. Kōk, J. Tong, The effect of payment timing on inventory decisions in a newsvendor experiment, Working Paper, Duke University, 2010.

[13] D.C. Croson, R. Croson, Y. Ren, How to manage an overcon<sup>fi</sup>dent newsvendor, Working Paper, University of Texas at Dallas, 2008.

[14] M.S. Davis, That's interesting! Towards a phenomenology of sociology and a sociology of phenomenology, Philosophy of Social Science 1 (1971) 309–344.

[15] T. Deng, Z. Shen, Asymmetries in the pull-to-center effect of the newsvendor experiment, Working Paper, University of California, Berkeley, 2012.

[16] F. de Véricourt, J.N. Bearden, A. Filipowicz, Sex, risk, and the newsvendor, Working Paper, INSEAD, 2011.

[17] N. Drinkwater, C. Denniston, Multiple samples and multiple experiments, in Statistical problems in genetics and molecular biology, CreateSpace, USA. Available online http:// www mcardle wisc edu/mstat/help/help/Notes-09 html#toc1642011

[18] W.K. Estes, The problem of inference from curves based on group data, Psychological Bulletin 53 (2) (1956) 134–140

[19] W.K. Estes, Traps in the route to models of memory and decision, Psychonomic Bulletin & Review 9 (1) (2002) 3–25.

[20] W.K. Estes, W.T. Maddox, Risks of drawing inferences about cognitive processes from model <sup>fi</sup>ts to individuals versus average performance, Psychonomic Bulletin & Review 12 (3) (2005) 403–408.

[21] T. Feng, R. Keller, X. Zheng, Decision making in the newsvendor problem: a cross-national laboratory study, Omega 39 (2011) 41–50.

[22] R.A. Fisher, Statistical Methods for Research Workers, 4th ed. Oliver and Boyd, London, 1932.

[23] J.J. Horton, D.G. Rand, R.J. Zeckhauser, The online laboratory: conducting experiments in a real labor market, NBER Working Paper 15961, National Bureau of Economic Research, Cambridge, MA, 2010.

[24] L. Jost, Combining signi<sup>fi</sup>cance levels from multiple experiments or analyses, n. d. Available online http://www.loujost.com/Statistics%20and%20Physics Signi<sup>fi</sup>cance%20Levels/CombiningPValues.htm.

[25] E. Katok, Using laboratory experiments to build better operations management models, Foundations and Trends® in Technology, Information and Operations Management 5 (1) (2011) 1–86.

[26] A. Kittur, E.H. Chi, B. Suh, Crowdsourcing user studies with Mechanical Turk, Proceedings of the Twenty-sixth Annual SIGCHI Conference on Human Factors in Computing Systems, 2008, pp. 453–456.

[27] M. Kremer, S. Minner, L.N.V. Wassenhove, Do random errors explain newsvendor behavior? Manufacturing & Service Operations Management 12 (4) (2010) 673–681.

[28] J.K. Kwak, Y. Xia, Y.H. Park, S. Gavirneni, Inventory control when selling to human newsvendors, Working Paper, Cornell University, 2012.

[29] N.H. Lurie, J.M. Swaminathan, Is timely information always better? The effect of feedback frequency on decision making, Organizational Behavior and Human Decision Processes 108 (2) (2009) 315–329.

[30] P.K. MacDonald, Useful <sup>fi</sup>ction or miracle maker: the competing epistemological foundations of rational choice theory, The American Political Science Review 97 (4) (2003) 551–565.

[31] W. Mason, D.J. Watts, Financial incentives and the “performance of crowds”, Proceedings of the ACM SIGKDD Workshop on Human Computation, 2009, pp. 77–85.

[32] B. Moritz, A.V. Hill, K. Donohue, Cognition and individual differences in the newsvendor problem: behavior under dual process theory, Working Paper, University of Minnesota, 2009.

[33] B. Moritz, A.V. Hill, K. Donohue, Asymmetric ordering behavior in newsvendor inventory decisions, Working Paper, Pennsylvania State University, 2012.

[34] F. Mosteller, R.A. Fisher, Questions and answers, The American Statistician 2 (5) (1948) 30–31.

[35] A. Ovchinnikov, B. Boulu-Reshef, P.E. Pfeifer, Revenue management with lifetime value considerations: balancing customer acquisition and retention spending for <sup>fi</sup>rms with limited capacity, Working Paper, University of Virginia, 2012.

[36] G. Paolacci, J. Chandler, P.G. Ipeirotis, Running experiments on Amazon Mechanical Turk, Judgment and Decision Making 5 (5) (2010) 411–419.

[37] N. Rudi, D. Drake, N. Rudi, D. Drake, Observation bias: the impact of demand censoring on newsvendor level and adjustment behavior, Working Paper, INSEAD, 2010.

[38] S. Savage, The Flaw of Averages: Why We Underestimate Risk in the Face of Uncertainty, John Wiley & Sons, Hoboken, NJ, 2009.

[39] M.E. Schweitzer, G.P. Cachon, Decision bias in the newsvendor problem with a known demand distribution: experimental evidence, Management Science 46 (3) (2000) 404–420.

[40] M. Sidman, A note on functional relations obtained from group data, Psychological Bulletin 49 (3)(1952) 263–269

[41] X. Su, Bounded rationality in newsvendor models, Manufacturing & Service Operations Management 10 (4) (2008) 566–589.

[42] D.Y. Wu, K.Y. Chen, Supply chain contract design: impact of bounded rationality and individual heterogeneity, Working Paper, University of Kansas, 2012.

Nelson Lau is a PhD Candidate in Decision Sciences at INSEAD. He has a B.A. (Summa Cum Laude) in Economics and Mathematics-Statistics from Columbia University, and is a CFA® charterholder. He was employed as a Trader/Researcher at a quantitative hedge fund prior to starting the PhD. Nelson's research to date has focused on decision making and behavioral operations management.

Sameer Hasija is a faculty member at INSEAD. He did his undergraduate studies at the Indian Institute of Technology at Chennai, and his graduate studies at the Simon School, University of Rochester, NY. Sameer's current research focuses on outsourcing of knowledge and/or information intensive service processes, impact of incentives on <sup>fi</sup>rm operations, and healthcare operations

Neil Bearden is an Associate Professor of Decision Sciences at INSEAD. He received his BA in Psychology from Southeastern Louisiana University and his PhD in Cognitive Psychology from The University of North Carolina at Chapel Hill. His research lies at the intersection of psychology and operations management.
