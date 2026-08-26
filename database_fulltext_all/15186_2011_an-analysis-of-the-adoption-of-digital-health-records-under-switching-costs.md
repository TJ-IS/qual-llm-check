---
otero_id: 15186
otero_key: "MJBNBA4F"
title: "An Analysis of the Adoption of Digital Health Records Under Switching Costs"
authors: "Zafer Ozdemir; Jack Barron; Subhajyoti Bandyopadhyay"
year: "2011"
journal: "Information Systems Research"
doi: "10.1287/isre.1110.0349"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/MJBNBA4F/fulltext/images/3b7626ce0b8c1b3b22420b9126ade92f397f01223187583b4d313923f54977e0.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# An Analysis of the Adoption of Digital Health Records Under Switching Costs

Zafer Ozdemir, Jack Barron, Subhajyoti Bandyopadhyay,

To cite this article:

Zafer Ozdemir, Jack Barron, Subhajyoti Bandyopadhyay, (2011) An Analysis of the Adoption of Digital Health Records Under Switching Costs. Information Systems Research 22(3):491-503. http://dx.doi.org/10.1287/isre.1110.0349

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2011, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/MJBNBA4F/fulltext/images/9bee8800445439da7e245aaa0a4c58a62e5ab163db1e2a5ee5da0f2962bb7b84.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# An Analysis of the Adoption of Digital Health Records Under Switching Costs

Zafer Ozdemir

Decision Sciences/MIS, Miami University, Oxford, Ohio 45056, ozdemir@muohio.edu

Jack Barron

Purdue University, West Lafayette, Indiana 47907, barron@purdue.edu

Subhajyoti Bandyopadhyay

Information Systems and Operations Management, University of Florida, Gainesville, Florida 32611, shubho@ufl.edu

W<sup>e</sup> <sup>investigate</sup> <sup>the</sup> <sup>incentive</sup> <sup>issues</sup> <sup>that</sup> <sup>surround</sup> <sup>the</sup> <sup>adoption</sup> <sup>and</sup> <sup>sharing</sup> <sup>of</sup> <sup>electronic</sup> <sup>health</sup> <sup>records</sup> <sup>(EHR)</sup> and the potential role of a personal health record (PHR) platform in facilitating data sharing. Through our analysis, we find evidence that health-care providers may not have an incentive to share patients’ records electronically even though EHR systems will increase consumer surplus, especially in the presence of provider heterogeneity and myopic consumers. In this context, we find that an independent PHR platform can create incentives for the providers to share their patients’ records electronically with other providers by selectively subsidizing them. In a pluralistic health-care system like that in the United States, where health-care providers have varying incentives to implement electronic health records, an online PHR platform can provide a proxy for a “national health information network,”’ wherein consumers can freely exchange their health records among competing providers.

Key words: electronic health records; personal health records; switching costs; national health information network; technology adoption

History: Rob Fichman, Rajiv Kohli, and Ranjani Krishnan, Senior Editors. This paper was received on February 5, 2009, and was with the authors 11 months for 2 revisions. Published online in Articles in Advance April 8, 2011.

## 1. Introduction

The adoption and sharing of electronic health records (EHR) by health-care providers can greatly facilitate the availability of complete patient health information at the point of care delivery. Together with clinical decision support systems such as those for medication order entry, this can prevent many errors and adverse events (injuries caused by medical management rather than by the underlying disease or condition of the patient) (Bates et al. 1998, 1999). Despite the potential benefits of shared electronic health records, the United States has lagged several of its counterparts in OECD countries in the use of EHR (Harris Interactive 2001).

A 2001 Harris Interactive study contends that one of the main reasons for the low level of EHR adoption in the United States is the prevailing market structure and the misaligned incentives. In Europe’s singlepayer systems, the payer can (and often does) dictate what health providers must do. In contrast, each provider in the U.S. pluralistic system makes its own decision of whether to digitize and share its medical records. Such decisions take into account the return on such capital investments, including the effect of sharing records on a provider’s competitive position (Bender et al. 2006, Markle Foundation 2004).

Sensing an opportunity, technology giants Google and Microsoft have recently entered this domain with their personal health record (PHR) solutions (Knowledge@Wharton 2007, Lohr 2008, McBride 2008). PHR is an electronic health record on an individual that can be drawn from multiple sources while being managed, shared, and controlled by the individual. Google has partnered with the Cleveland Clinic to pilot its PHR dubbed Google Health, whereas Microsoft is piloting its own system, called Health Vault, with the Mayo Clinic. PHRs come with application interfaces that facilitate integration with providers’ clinical electronic records, so that patients can send personal information, at the individual’s discretion, into the EHR or pull information from the EHR into the PHR.

One of the main criticisms of the EHRs implemented to date is that these systems do not communicate with each other, and are therefore islands of information. Consequently, patients find it extremely difficult to share their data with other providers. Experts in the field have long noted that in the absence of a national health information exchange and a willingness by medical providers to share their closely guarded patient information, the true potential of EHR would never materialize. However, the recent introduction of PHR tools with standard interfaces and data structures stand to change the status quo as they empower the patients in building a digital history of their health and easily sharing those records with the related parties as they see fit.

These developments lead us to ask the following research questions. Can social surplus increase with shared EHR, yet providers not adopt it? Given heterogeneous providers that compete with each other, which type of provider (in terms of size or quality) would gain from joint electronic sharing of health records? What role can a Web-based PHR platform (such as those by Microsoft and Google) play in this environment, and what would be the incentive of the PHR platform in providing such a service? We develop and analyze a stylized model that provides answers to these questions.

In determining the optimal EHR/PHR adoption strategies, providers consider improvements in care and value provided to their patients, and subscription fees (if any) on the one hand and technology implementation costs and reduced switching costs for existing patients on the other. A key feature that can limit adoption of the PHR platforms by the providers is that adoption can lower the costs of patients switching to alternative providers. We characterize the online platform as an entity that can leverage, through appropriate pricing (which can sometimes take the form of a subsidy), either of their clientele (patients on one side and health-care providers on the other) to ensure the participation of the other in maximizing their profits. To the best of our knowledge, this is the first study that analytically investigates how the two most-cited barriers to the widespread adoption of EHR (i.e., sizable costs and misaligned incentives) can be overcome in a pluralistic health-care system such as the one in the United States.

There are several key findings of this research. We first show that competing (heterogeneous) providers in many cases will not have the incentive to implement EHR systems or share their data electronically due to competitive concerns. In such situations, an online personal health records platform like Microsoft HealthVault or Google Health can serve three purposes. First, given the side benefits from the traffic generated, such entities may be willing to absorb some of the costs to transform previously noninteroperable EHR systems into systems that “talk” to each other through the “middleware” of the PHR platform.<sup>1</sup> In addition, as the PHR platform derives rents from the consumers that participate, it can selectively compensate providers for the impact of the reduction in the switching cost for consumers who may now be more willing to switch health-care providers. In other words, the PHR platform can subsidize the health-care providers in order to induce them to join the platform. Third, and perhaps most importantly, the PHR platform can tacitly enforce a binding agreement among competing providers to electronically share their records with one another. Thus, by its very nature, a PHR platform is well positioned to solve the issue of misaligned incentives. It can act as the underlying interoperable framework that can lead to increased sharing of medical records among competing health-care providers and facilitate the adoption and use of electronic health records in a pluralistic health-care system.

From the standpoint of the relevant economics literature, we build on and contribute to the research stream on switching costs. In particular, because digital sharing of health records makes it easy for consumers to change providers, technology adoption decisions endogenously determine switching costs in our setting, whereas in the switching cost literature such costs are treated exogenously. This results in a much more nuanced and complex analysis than can be found in the extant literature. Our other contributions include allowing for (i) seller heterogeneity, (ii) a set of experienced consumers for each seller at the outset, and (iii) differences in switching costs depending on the direction of the switch. These features are needed to accurately model the adoption of EHR in the health-care industry, and each plays an important role in the analysis.

The rest of the paper is arranged as follows. In the next section, we set up an economic model that incorporates switching costs to explain the nature of the competition between health-care providers. We then expand this discussion to include the possibility of adopting EHR systems in §3, the electronic sharing of medical records in §4, and the potential impact of a PHR platform in §5. The final section concludes with a discussion of the results and their implications.

## 2. Provider Competition Under Switching Costs

In this section, we present a model of a market with heterogeneous health-care providers. Our setting involves a variant of a differentiated product framework that allows us to examine the optimal EHR and PHR adoption strategies in a competitive equilibrium. A key feature of the analysis is to characterize the adoption of EHR systems by providers, as well as the entry of a PHR platform, not only in terms of the changes such adoptions imply for health-care services and costs of delivery, but also in terms of the changes in the costs consumers face to switch providers.

Introducing switching costs requires a dynamic setting such as that suggested by Klemperer (1987). In such a dynamic setting, consumers take into account the reduction in value to patronizing a health-care provider if that provider has high switching costs, because high switching costs not only can limit the freedom to change providers if circumstances change and the patient has a higher value for a different provider in the future, but also can increase anticipated prices in future periods.

The basic framework of the model is as follows. There are two types of economic actors in the market: providers and consumers. To simplify the analysis to follow, we consider the case of only two providers, $A$ and B. The costs to provider $i ( i = A , B )$ producing output $q _ { i t }$ in period t with the amenity level $a _ { i t } ( a _ { i t } \ge 0 , )$ 5 include both a fixed-cost component $k _ { i } ( a _ { i t } )$ and a constant marginal cost component $c ( a _ { i t } )$ . Total costs are given by:

$$
C (q _ {i t}, a _ {i t}) = k _ {i} (a _ {i t}) + c (a _ {i t}) q _ {i t}.
$$

This representation allows for the possibility that fixed and/or variable costs depend on the level of amenities. A list of the notation used in the text is shown in Table A.1 in the appendix.

We assume that the two providers in the healthcare market compete in terms of both prices and amenities or services. To simplify the discussion, let a consumer’s utility function be linear in price and amenities (decreasing in price, increasing in amenities) and let a provider’s marginal costs be linear in amenities, such that $c ( a _ { i t } ) = \theta + a _ { i t }$ . Then, competition between the two providers can be expressed in terms of prices net of amenities, with the “net” price for provider k defined by $p _ { i t } = p _ { i t } ^ { g } - a _ { i t } ,$ where $\hat { p } _ { i t } ^ { g }$ is the gross price for provider i that does not account for the value to the consumer of the amenities offered. A lower price can be interpreted as a provider either lowering its gross price or increasing amenities to attract additional consumers, with either action costly to the provider because it reduces the provider’s net revenues per unit sold.

We assume that each consumer $j , \ j = 1 , \ldots L ,$ purchases one unit of health-care services each period and is in the market for at most two periods. Klemperer (1987, 1995) and Marinoso (2001), among others, have noted the potential importance of switching costs for consumers in characterizing market competition. Such switching costs are likely to play an important role in the health-care sector: patients often stick to a health-care provider simply because switching to another provider can be extremely difficult, even if the latter might be a better “fit.” With switching costs, consumers each period fall into two distinct categories: new consumers who are entering the health care market for the first time and experienced consumers who purchased health-care services from a particular provider in the prior period.

Define $\eta _ { t }$ as the proportion of consumers new to the market in period t. A new consumer $j ^ { \prime } s$ gain to purchasing from provider i at net price $p _ { i t }$ in period t is defined by the utility

$$
u _ {j i t} = r _ {i} - p _ {i t} - \varepsilon_ {j i t},
$$

where $\varepsilon _ { i i t } \geq 0$ is the match loss for consumer j purchasing from provider i in period $t ,$ and $r _ { i }$ is the timeinvariant gain to purchasing health-care services from provider i. The loss $\varepsilon _ { j i t } \geq 0$ can be viewed as indicative of the costs of visiting a particular provider, a loss that varies for a particular consumer across providers and over time. Such a loss could reflect transportation costs or losses associated with the extent of misalignment between the specific services sought and the expertise of each of the providers. In the subsequent discussion, we assume that consumers’ gains to purchasing from either provider $r _ { i }$ are sufficiently high that all consumers are active buyers.

The proportion $( 1 - \eta _ { t } )$ 5 of consumers in period t are experienced consumers. Following Klemperer (1987), experienced consumers can be divided into two distinct groups. The proportion $\mu _ { t }$ of consumers in period t are experienced consumers with new loss values who consider alternative providers in period t + 1. The proportion $( 1 - \eta _ { t } - \mu _ { t } )$ of consumers in period t are experienced consumers who are assumed to be “locked-in” to their prior provider and do not consider switching providers.

An experienced consumer not “locked-in” to her prior provider receives a new loss value and decides whether to remain at the prior provider or switch to the alternative provider. In the health-care provider market, such a consumer has established a providerpatient relationship that involves a complete medical history stored by that provider, and thus faces “switching costs” when changing providers. These costs can include reestablishing a medical history through requesting copies of records from the previous provider and delivering them to the new provider, filling out forms at the new provider’s office, and repeating certain tests in case previous test results are missing, incomplete, or simply deemed uninformative or unacceptable by the new provider.

Experienced consumers who consider receiving care from a new provider weigh the utility gain from switching to a preferred provider on the one hand and the associated cost of the process on the other. An experienced consumer j who previously purchased from provider i will reap a net utility from purchasing from the other provider k in period t equal to

$$
u _ {j k t} = r _ {i} - p _ {k t} - \varepsilon_ {j k t} - s _ {i k},
$$

where $i = A , B , \ : k = A , B ,$ and $i \neq k .$ . The term $s _ { i k } \geq 0$ denotes the cost to the consumer of switching from provider i to provider k.

To simplify the model’s solutions, we assume that each period the consumers who experience a new match loss value draw from the time-invariant uniform distribution $H ( \varepsilon )$ with lower and upper bounds of 0 and 1, respectively.<sup>2</sup> As is standard in the switching costs literature, we adopt the Hotelling-like assumption of negatively correlated match losses for each consumer across the two providers, such that $\varepsilon _ { j B } = 1 - \varepsilon _ { j A } .$

The probability that an experienced consumer who purchased from provider A in the prior period and draws a new match loss value, $\varepsilon _ { A } ,$ , remains with provider A in period $t , \ y _ { t } ,$ is the probability that $[ r _ { A } - p _ { A t } - \varepsilon _ { A } ]$ exceeds $[ r _ { B } - p _ { B t } - ( 1 - \varepsilon _ { A } ) - s _ { A B } ]$ or:

$$
y _ {t} = \rho_ {t} + \frac {s _ {A B}}{2},\tag{1}
$$

where $\rho _ { t } = [ 1 + r _ { A } - p _ { A t } - ( r _ { B } - p _ { B t } ) ] / 2$ . Similarly, the probability that an experienced consumer with a new match loss value, who previously purchased from provider $B ,$ switches to provider A in period $t , \ x _ { t } ,$ is the probability that $[ r _ { A } - p _ { A t } - \varepsilon _ { A } - s _ { A B } ]$ exceeds $[ r _ { B } - { p _ { B t } } ^ { - } - ( 1 - \varepsilon _ { A } ) ] ~ \mathrm { o r } ^ { 3 }$

$$
x _ {t} = \rho_ {t} - \frac {s _ {B A}}{2}.\tag{2}
$$

For period $t ,$ let $\alpha _ { t - 1 }$ denote the inherited proportion of experienced consumers in period t who purchased from provider A in the prior period $t - 1$ Looking forward and assuming that experienced consumers in period t + 1 are randomly drawn from new consumers of health services in period t, the probability that an experienced consumer in period $t + 1$ purchased from provider A in period $t , \ \alpha _ { t } ,$ 1 equals the probability that $\left[ { r _ { A } } - { p _ { A t } } - { \varepsilon _ { A } } + { \beta _ { c } } V _ { A t } \right]$ exceeds $\left[ r _ { B } - p _ { B t } - ( 1 - \varepsilon _ { A } ) - \beta _ { c } V _ { B t } \right]$ , where $V _ { A t } ( V _ { B t } )$ denotes the expected value associated with period t + 1 purchases of medical services conditional on being a consumer of provider A4B5 in period t, and $\beta _ { c }$ is the consumers’ discount factor, with $0 < \beta _ { c } \leq 1 $ 0 Thus, the probability $\alpha _ { t }$ that a new consumer buys from provider A rather than provider B in period t is given by

$$
\alpha_ {t} = \rho_ {t} + \frac {\beta_ {c}}{2} (V _ {A t} - V _ {B t}).\tag{3}
$$

Introducing the superscript e to denote new consumers’ expectations regarding key variables in the next period, the term $( V _ { A t } \ - \ V _ { B t } )$ in (3) can be expressed $\mathsf { a s } ^ { 4 }$

$$
\begin{array}{l} V _ {A t} - V _ {B t} = \frac {2 (1 - \mu_ {t + 1} - \eta_ {t + 1})}{1 - \eta_ {t + 1}} [ \rho_ {t + 1} ^ {e} + \alpha_ {t} ^ {e} - 1 ] + \frac {\mu_ {t + 1}}{1 - \eta_ {t + 1}} \\ \cdot (s _ {A B} + s _ {B A}) \left[ \rho_ {t + 1} ^ {e} + \frac {(s _ {B A} - s _ {A B})}{4} - 1 \right]. \end{array} \tag {4}
$$

Rational expectations on the part of consumers means that new consumers accurately forecast future prices and market shares, such that $\rho _ { t + 1 } ^ { e } = \rho _ { t + 1 }$ and $\alpha _ { t } ^ { e } = \alpha _ { t }$ Assuming rational expectations, we can substitute (4) into (3) and solve for the proportion of new consumers who purchase from provider A in period $t , \alpha _ { t } .$

The likelihood that a consumer purchases from provider A in the current period t is given by

$$
q _ {A t} = \eta_ {t} \alpha_ {t} + \mu_ {t} [ \alpha_ {t - 1} y _ {t} + (1 - \alpha_ {t - 1}) x _ {t} ] + (1 - \eta_ {t} - \mu_ {t}) \alpha_ {t - 1}.
$$

Similarly, the likelihood a consumer purchases from provider A in the following period is given by

$$
\begin{array}{r} q _ {A t + 1} = \eta_ {t + 1} \alpha_ {t + 1} + \mu_ {t + 1} [ \alpha_ {t} y _ {t + 1} + (1 - \alpha_ {t}) x _ {t + 1} ] \\ + (1 - \eta_ {t + 1} - \mu_ {t + 1}) \alpha_ {t}, \end{array}
$$

where $\alpha _ { t + 1 }$ is the proportion of new consumers in the following period who choose to purchase from provider A. Similar expressions hold for provider $B ,$ with $q _ { B t } = ( 1 - q _ { A t } )$ and $q _ { B t + 1 } = ( 1 - q _ { A t + 1 } )$

To simplify the analysis, we consider a twoperiod time horizon. For consumers, this means that we do not consider forward-looking behavior by new consumers in the second period, such that $\stackrel {  } { \alpha } _ { t + 1 } = \rho _ { t + 1 } = [ 1 + r _ { A } - p _ { A t + 1 } - ( r _ { B } - \stackrel {  } { p _ { B t + 1 } } ) ] / 2 . ^ { 5 }$ For providers, this means considering profits only for the periods t and t + 1. Expected profits for Providers A and B are then given by

$$
\pi_ {A} = q _ {A t} L (p _ {A t} - \theta) + \beta q _ {A t + 1} L (p _ {A t + 1} - \theta) - k _ {A} - \beta k _ {A}\tag{5}
$$

<sup>4</sup> A formal derivation of Equation (4) is provided in the mathematical supplement to this paper as part of the online version that can be found at http//isr.journal.informs.org/.

<sup>5</sup> Klemperer (1987) makes a similar assumption in the characterization of new consumers in the second period. Note that in Klemperer’s two-period analysis, new consumers in the second period replace a fraction of experienced consumers who exit the market. In contrast, in our overlapping-generations framework, all new consumers in the first period remain in the market in the second period as experienced consumers. These experienced consumers are joined by a cohort of new consumers.

and

$$
\begin{array}{r l} & {\pi_ {B} = (1 - q _ {A t}) L (p _ {B t} - \theta)} \\ & {\qquad + \beta (1 - q _ {A t + 1}) L (p _ {B t + 1} - \theta) - k _ {B} - \beta k _ {B},} \end{array}\tag{6}
$$

where $\beta$ denotes providers’ common discount factor, with $0 < \beta \leq 1$

Benchmark Case: No EHR or PHR. The prices in a sequential Nash equilibrium are determined as follows. First, one obtains the first-order conditions characterizing the optimal price for each of the two providers in the second period, period $t + 1$ . These first-order conditions for prices in the second period are solved for the set of future (second-period) equilibrium prices. These equilibrium prices are substituted into the two-period profit expressions (5) and (6). Then, one obtains the first-order conditions for prices in the first period, and these first-order conditions are solved for the set of current (first-period) equilibrium prices.

Equilibrium prices depend on specific parameters, such as switching costs $( s _ { A B }$ and $s _ { B A } )$ , providers’ and consumers’ discount factors $( \beta$ and $\beta _ { c } ) _ { . }$ , the gross utilities obtained from the two providers $( r _ { A }$ and $r _ { B } ) _ { \scriptscriptstyle  { B } }$ the division of consumers across various categories, including in particular the proportion of experienced consumers who are locked in each period $( \mathrm { i . e . , }$ $( 1 - \eta _ { t } - \mu _ { t } )$ and $( 1 - \eta _ { t + 1 } - \mu _ { t + 1 } ) )$ , and the production costs $( \theta ) .$ . The prices in each period also depend on the inherited proportion of current consumers who previously purchased from provider $A \left( \alpha _ { t - 1 } \right)$ . Proposition 1 provides explicit solutions for prices and profits for the benchmark symmetric case.

<sup>Proposition</sup> <sup>1.</sup> Assume that all consumers are new in period $t \ ( \eta _ { t } = 1 , \mu _ { t } = 0 )$ . In period $t + 1 ,$ , assume there are new consumers $( \eta _ { t + 1 } > 0 )$ , experienced consumers who consider switching $( \mu _ { t + 1 } > 0 )$ , and experienced consumers who are “locked-in” $( \eta _ { t + 1 } + \mu _ { t + 1 } < 1 )$ . Let consumers’ values $r _ { A }$ and $r _ { B }$ be sufficiently high and the proportion $( 1 - \eta _ { t + 1 } - \mu _ { t + 1 } )$ of consumers locked in for period $t + 1$ be sufficiently low such that consumers’ values exceed equilibrium prices in both periods. Let switching costs $s _ { A B }$ and $s _ { B A }$ be positive, but sufficiently low such that some consumers will switch from each provider in period $t + 1$ Finally, let there be symmetry in the sense that providers have identical switching costs $( s _ { A B } = s _ { B A } = s )$ , identical values to consumers $( r _ { A } = r _ { B } = r )$ , and common fixed costs $( k _ { A } = k _ { B } = k )$ . Then, assuming that consumers and providers have a common discount factor $( \beta = \beta _ { c } )$ , are $f o r -$ ward looking $( 0 < \beta \leq 1 )$ , and have rational expectations, equilibrium prices and two-period profit are the same across providers and given by

$$
\begin{array}{l} {p _ {t} = \theta + 1 + \frac {\beta}{3 (\eta_ {t + 1} + \mu_ {t + 1})}} \\ {\cdot \left[ 3 \eta_ {t + 1} + 2 s \mu_ {t + 1} - \frac {\mu_ {t + 1} [ (4 \eta_ {t + 1} - 1) + \mu_ {t + 1} (1 + 4 s - 2 s ^ {2}) ]}{(1 - \eta_ {t + 1})} \right]} \end{array}
$$

$$
\begin{array}{c} p _ {t + 1} = \theta + \frac {1}{\eta_ {t + 1} + \mu_ {t + 1}} \\ \pi = - k (1 + \beta) + \pi_ {o}, \end{array}
$$

where

$$
\begin{array}{r l} & {\pi_ {o} = \frac {1}{2} + \frac {\beta}{6 (\eta_ {t + 1} + \mu_ {t + 1})}} \\ & {\qquad \cdot \bigg [ 3 (\eta_ {t + 1} + 1) + 2 s \mu_ {t + 1}} \\ & {\qquad - \frac {\mu_ {t + 1} [ (4 \eta_ {t + 1} - 1) + \mu_ {t + 1} (1 + 4 s - 2 s ^ {2}) ]}{(1 - \eta_ {t + 1})} \bigg ]} \end{array}
$$

denotes the two-period operating income of a provider.

Details of the proof of Proposition 1 are available in the mathematical supplement in the online version. Note that if switching costs were zero $( s = 0 )$ and there were no locked-in consumers in the second period $( \eta _ { t + 1 } + \mu _ { t + 1 } = 1 )$ , then equilibrium prices simplify to $p _ { t } = p _ { t + 1 } = \theta + 1$ . However, introducing small positive switching costs given some experienced consumers that consider switching $( \mu _ { t + 1 } > 0 )$ results in lower prices in the first period as providers compete for new consumers who in the subsequent period will face costs to changing providers.

## 3. Adoption of EHR Systems Without Data Sharing

According to a 2007 Harris Interactive survey, 54% of the respondents said that if they were to choose between two doctors, of whom only one used electronic health records, their choices would be influenced by the availability of this technology, at least to some extent. In another phone survey of 2,000 adults in eastern Massachusetts, 19% said they would switch their medical affiliation if they found a provider that offered electronic health records (Goth 2008). In our model, such perceived benefits of EHR by consumers can be interpreted as an increase in consumers’ gain to purchasing health-care services from the provider. In particular, if provider $A$ adopts EHR, then this would be reflected by an increase in the parameter $r _ { A }$ by $\Delta v > 0 ,$ , and a resulting increase in equilibrium operating profits $\Delta \pi _ { o } > 0$ . Assuming that such an amenity affects a provider’s fixed costs alone, accompanying provider $A ^ { \prime } { \mathrm { s } }$ adoption of EHR would be an increase in its fixed-cost component $k _ { A }$ by $\Delta F > 0$

The model developed in §2 allows us to examine the implications of the adoption of EHR by each provider. We first present a lemma that will help us characterize the providers’ equilibrium EHR adoption strategies.

<sup>Lemma</sup> <sup>1.</sup> Starting from the benchmark symmetric case identified in Proposition 1, adoption of EHR by a single provider increases that provider’s prices in periods t and $t + 1$ by a fraction of the increase in the value of EHR to the consumers. The adopting provider’s two-period operating income increases as well $\left( i . e . , \ \Delta \pi _ { o } > 0 \right)$ . The prices and operating income of the provider not adopting EHR decrease by equal magnitudes.

Details of the proof of Lemma 1 are available in the mathematical supplement.

In other words, given symmetric providers, adoption of EHR by one provider translates into equal but opposite sign changes in prices and operating income for the two providers. The proof of the lemma is provided in the mathematical appendix, and it revolves around evaluating the comparative statics of the equilibrium expressions that were determined from Proposition 1.

Accordingly, the normal form of the game reduces to Figure 1 where the upper (lower) expression in the parentheses represents the profit of provider A4B5. The result is a prisoner’s dilemma for the providers with respect to the adoption of EHR. That is, although there are gains to each provider adopting EHR if the other provider does not, the equilibrium with both providers adopting generates a loss for both providers. We provide the equilibrium strategies and outcomes formally in Proposition 2, which follows directly from the analysis of the normal form presented in Figure 1.

Proposition 2. <sub>If</sub> $\Delta \pi _ { o } \geq \Delta F .$ , then either provider will perceive a net gain to the unilateral adoption of EHR. However, if one provider adopts EHR, the second provider also adopts EHR because her gain equals the first provider’s original gain to adopting EHR. If both providers adopt EHR, equilibrium prices and operating income are identical to the case when neither adopts EHR. The providers’ profits will thus be lower if both adopt EHR, given the fixed costs $\Delta F > 0$ in implementing the EHR. Thus, we have the potential for the classic prisoner’s dilemma in the context of EHR adoption.

The key driving force for the above prisoner’s dilemma characterization of EHR adoption is that consumers’ choices across competing providers depend on prices, switching costs, and the perceived difference in values $r _ { A } - r _ { B }$ . With initial symmetry across providers, adoption of EHR by one provider translates into equal but opposite sign changes in operating income for the two providers, and that provides a potential incentive to adopt if EHR implementation costs are not too high. It also provides an incentive for the second provider to adopt if one provider has already adopted EHR. When both providers adopt EHR, providers’ relative competitive position is unchanged, their price elasticity of demand is unchanged, and thus equilibrium prices are the same as before. However, given positive implementation costs to generate the benefits of EHR, it follows that profits for each provider are lower when both adopt EHR. Proposition 2 predictions are consistent with the literature (e.g., Bender et al. 2006 and the previously cited reports by Harris Interactive (2007) and Mango and Reifberg 2008), namely, that the main benefit of EHR adoption accrues to the patients of the adopting provider, and this is particularly true if EHR adoption is widespread.

Figure 1 The Normal Form of the EHR Adoption Game

<table><tr><td></td><td colspan="2">Provider B</td></tr><tr><td>Provider A</td><td>Do not adopt</td><td>Adopt</td></tr><tr><td>Do not adopt</td><td> $\begin{pmatrix} \pi_o \\ \pi_o \end{pmatrix}$ </td><td> $\begin{pmatrix} \pi_o - \Delta \pi_o \\ \pi_o + \Delta \pi_o - \Delta F \end{pmatrix}$ </td></tr><tr><td>Adopt</td><td> $\begin{pmatrix} \pi_o + \Delta \pi_o - \Delta F \\ \pi_o - \Delta \pi_o \end{pmatrix}$ </td><td> $\begin{pmatrix} \pi_o^- \Delta F \\ \pi_o^- \Delta F \end{pmatrix}$ </td></tr></table>

Note. No data sharing.

Paradoxically, factors that increase the two-period operating income advantage to a single provider adopting EHR also make losses from EHR adoption more likely. The reason for this is that the greater the operating-income gain to unilateral adoption of EHR, the more likely this gain will exceed the fixed cost of implementing EHR for a single provider. However, as the prisoner’s dilemma result of Proposition 2 indicates, the result of such a positive net gain to unilateral adoption of EHR is that both providers adopt, and thus both incur losses. We thus have the following proposition.

<sup>Proposition</sup> <sup>3.</sup> The prisoner’s dilemma outcome identified in Proposition 2, one in which both providers adopt EHR and suffer losses, is more likely to occur if there are higher switching costs (s), a higher proportion of consumers locked in to a provider in period t + 1 (due to a reduction in either $\eta _ { t + 1 } ~ o r ~ \mu _ { t + 1 } )$ , or if consumers place a greater value on EHR. Such factors raise the operatingincome gain to a single provider adopting EHR, and thus make it more likely that such operating-income gains will exceed the fixed costs of implementing EHR.

Details of the proof of Proposition 3 are available in the mathematical supplement.

## 4. The Decision to Share Health Records Electronically

Another potential benefit of EHR for patients is that the cost to switch to a different provider can drop if the providers share patient records electronically. This can happen when providers adopt the same system or their systems are built according to established data standards. Several standards currently exist for the interoperability of EHR systems, although in reality their implementation remains extremely limited. These include standards like the ATSM Continuity of Care Record for transfer of patient health records summary (based on XML), the ANSI X12 standard for transmitting billing information (this has become popular in the United States because of the regulatory requirements under the Health Insurance Portability and Accountability Act (HIPAA) for transmitting billing data to Medicare), the DICOM standard for representing and transferring radiology images, and the HL7 set of standards for transmitting messages or documents like physician notes. An interoperable EHR system can integrate with the other provider’s system in order to seamlessly exchange patient records.

We henceforth assume that both providers have adopted interoperable EHR systems. However, each provider still requires an economic incentive to share health records electronically; otherwise, they will accept electronic records from incoming new patients, but limit outgoing established patients’ access to their records, for instance, by only providing their records on paper.<sup>6</sup> Such strategic behavior introduces direction-dependent switching costs into the analysis. Within the context of the model developed in the previous section, taking as given that the two providers have adopted EHR, we now consider the choice of the providers regarding the ability to share electronic records and its impact on patient mobility and provider profits.

In the case of symmetric firms with no experienced consumers in the first period, Klemperer (1987) has shown that firms may be better or worse off with lower switching costs. In particular, consider the set of consumers in the second period who are either new consumers or experienced consumers who have new preferences. If the second group is very small $( \mu _ { t + 1 } \to 0 )$ , then lower switching costs can reduce firms’ profits. On the other hand, if the second group is large, then lower switching costs can increase firms’ profits. The reason for this is that lower switching costs reduce the competition for such consumers in the first period, and thus can lead to higher prices.

We conduct our analysis of the sharing of electronic health records in our more general setting in which providers’ technology decisions can unilaterally impact the switching costs (e.g., by adopting different policies regarding the format of data to hand out to outgoing established patients) and providers can differ in size. Given the complexity of the analytical solutions, especially when there are heterogeneous providers, we carried out extensive simulations to gain several insights.<sup>7</sup>

As we indicated in the proof of Proposition 1, the existence of a Nash equilibrium set of prices in the second period requires certain assumptions regarding the key parameters to assure that all consumers in the market purchase from one of the two providers and that there is robust competition across providers for new and experienced consumers in period t + 1. For such a situation to occur, we assume that (a) the values of providers to consumers 4r 5 are sufficiently high; (b) these values are sufficiently similar across providers; (c) the proportion of customers $( \eta _ { t + 1 } + \mu _ { t + 1 } )$ who potentially consider a new provider in period t + 1 is less than 1 but sufficiently large; and (d) the switching costs $( s _ { A B } , s _ { B A } )$ are sufficiently small. In particular, we consider the following “benchmark” set of parameter values: $r _ { A } = r _ { B } = 4 , \ s _ { A B } = s _ { B A } = 0 . 1 ,$ $\mu _ { t + 1 } = 0 . 4 , \ \eta _ { t + 1 } = 0 . 5$ . Normalizing fixed costs to 0 $( k _ { A } = k _ { B } = 0 )$ and setting discount factors equal to 1, we establish the following.

<sup>Result</sup> <sup>1.</sup> There exist cases where a provider may choose to retain a data-sharing arrangement even though this reduces the switching costs of its patients.

This result arises even though we can show that a provider who unilaterally reneges on the data-sharing arrangement would have higher prices and profits in the second period. This second-period profit increase, however, is more than offset by the fall in profits in the first period, because new consumers anticipate the negative impact of such higher switching costs on the value to patronizing that provider, and this leads to a significant drop in the perceived value of the provider in the first period. The negative impact on the first-period profit dominates the positive impact on the second-period profit because the proportion of the market affected by the provider’s decision in the second period is smaller than that in the first period.

However, such an outcome is less likely given our modifications to the benchmark analysis. In particular, other things being equal, when we simulate unilateral increases in switching costs (something that can be achieved in real life by giving outgoing patients their records in paper, for example), we find that this result is reversed if we allow for a sufficient proportion of inherited experienced consumers in the first period. The addition of experienced consumers in the first period reduces the relative importance of new consumers for which the providers compete. This allows

Figure 2 The Incentives of the Providers to Share Records Electronically  
![](/api/attachments/MJBNBA4F/fulltext/images/e815d5f4e5ca481fc8fede89943dec26bdc3bf1f5c1ff41681e658ba67001037.jpg)  
them to charge higher prices in the first period and thereby improve profits. Furthermore, the reduced importance of new consumers in the first period increases the potential gain from unilaterally reneging on the data-sharing arrangement (even though such an action makes the provider less attractive to the new consumers). We state this observation as our second simulation result.

<sup>Result</sup> <sup>2.</sup> Even if both providers may profit from an electronic data-sharing arrangement compared to the benchmark case of no electronic data sharing, each may have the incentive to deviate and give outgoing established patients their records on paper. The incentive to deviate, if any, is more pronounced for the better/larger provider.

The effects of Results 1 and 2 are illustrated in Figure 2, which shows the results of the numerical analyses as we move away from the benchmark case. The horizontal axis represents provider heterogeneity in terms of value as perceived by the consumers $\left( r _ { A } - r _ { B } \right)$ , and the vertical axis represents the degree of consumers’ forward-looking behavior $( \beta _ { C } )$ . The tan area of the graph represents combinations of parameter values where both providers have the incentive to share their health records electronically, thereby showing the possibilities for Result 1 to occur.

We observe that heterogeneity between the providers introduces the incentive to renege on a data-sharing arrangement, because given a sufficient size difference, the more attractive, and thus larger provider, will not find electronic sharing of patient records profitable (see the purple area in Figure 2). This is because high switching costs make the larger provider relatively more attractive to consumers in the current period, because the larger provider is more likely to be their preferred provider in the next period (and thereby have a smaller probability of a costly switch) if they experience new preferences. The reduced mobility of patients benefits the larger provider relatively more in the second period too. In other words, the larger/better provider will have the incentive to unilaterally increase the switching costs for patients who want to defect from it, even if the smaller provider continues to cooperate with it by lowering its own switching costs. In practice, this can be realized with the larger/better provider supplying the health records of a defecting patient on paper, even though the smaller provider continues to supply the health records of its own defecting patients electronically.

The incentive to renege on a data-sharing arrangement increases further as consumers become less forward looking (low $\beta _ { C } )$ . This is because when consumers do not look ahead, each provider benefits (in the next period) from unilaterally raising its own switching costs because it limits the mobility of established patients. Consumers can often be myopic or discount the future impact of their current decisions regarding health care because they are less likely to think of future periods at a time when their immediate thoughts are centered around their current illness. This is especially true if the type of illness is not chronic in nature and the consumers do not expect to be back with the provider at regular intervals.

Thus, the presence of provider heterogeneity and myopic consumers are two reasons that may prevent providers from sharing their records electronically. This observation is consistent with the findings of Hillestad et al. (2005), who conclude that even though interoperable EHR systems could result in a large social surplus (estimated to be in the range of \$142– \$371 billion), they are unlikely to be realized in the current pluralistic health-care system.

So far, we have assumed that the two providers are identical in terms of the likelihood of acquiring new consumers in each period, as well as the likelihood that the new consumers will be locked in during the second period. However, this may not be the case. For example, there may be some specialized national providers $( \mathrm { e . g . }$ , the Mayo Clinic) who serve patients that are predominantly new each period, because prior patients typically switch to their local hospital for long-term care. In the context of our generalized model, this could be interpreted as asymmetry in both $\eta _ { t } s$ and $\mu _ { t + 1 } s$ across the providers. For instance, if provider A had a higher $\eta _ { A t }$ and a higher $\mu _ { A t + 1 } ,$ then this could induce provider A to seek a data-sharing arrangement (and correspondingly lower switching costs), because the gain this provides to prospective new consumers is more widespread and can be extracted by the provider in terms of higher prices.

Our discussion on data sharing up to this point has been independent of changes in either direct costs to the provider or direct benefits to consumers in terms of improved health care from adopting EHR. However, such factors may also play an important role in limiting the adoption of EHR systems. For example, smaller providers may find the fixed (per patient) cost of EHR implementation too high and, hence, may not digitize their records. This may explain why small providers would not seek to share data electronically even though, on the basis of reducing switching costs alone, a small provider might gain from doing so.

In addition, the improvement in the quality of health-care service due to the adoption of EHR could differ depending on the size of the providers. Specifically, the benefits of EHR may be greater at large providers, because a larger provider might realize a greater gain from the sharing of electronic records internally across a more diverse set of “departments.” Note that this would suggest that large providers would be more likely to adopt EHR systems, but does not directly address the question of their likelihood of making such a system interoperable with competitors for the purpose of data sharing. In fact, it could be the case that in offering more varied services, their patients would be less likely to seek to switch to a different provider, and thus large providers’ gain from electronic data sharing through interoperable EHR systems could be less than what is modeled here.

These findings are important in the context of the significant outlays allocated towards adoption of electronic health records in the American Recovery and Reinvestment Act of 2009 (House of Representatives 2009), popularly known as the stimulus bill. Although a great deal of emphasis was laid on having interoperable records, the results of our analysis indicate that having interoperable records might still not be sufficient to incentivize the providers to share the records electronically with competing providers. This can be achieved through new regulation or via an intervention of a private entity who can create the necessary incentives for data sharing. The entry of independent PHR platforms is, therefore, important in this context. We discuss the implications in the following section.

## 5. The PHR Platform

In this section, we consider a platform that offers an online PHR service to patients and providers, similar to the services of Google Health and Microsoft’s HealthVault. The PHR platform takes on the responsibility of developing the middleware and routines that will enable the automatic transfer of patients health records from providers’ EHR systems to its servers. A PHR platform typically seeks participation from both providers and consumers. A provider participates by uploading its patients’ records to the platform’s servers. Once records are on the platform, the consumer can establish an account with the platform and gain electronic access to her records. Assuming the providers have not already committed to electronic sharing of records directly thorough their EHRs, having a PHR account reduces the cost a patient incurs when transferring health records to a new provider. All the patient needs to do is to either grant appropriate access rights to the new provider (if that provider is on the platform) or download the records and submit them either electronically or physically (if that provider is not on the platform). Although the latter process would require the consumer to incur a nonnegligible cost, the actual amount is likely to be considerably lower than what would be the case without the platform. By strategically positioning itself between patients and providers, the PHR platform can charge appropriate prices to facilitate participation of either side of the two-sided market in a way that maximizes its total profit.

Taking as given the adoption of EHR, our analysis suggests that one advantage of the platform is the requirement that each participating provider makes electronic records available to a third party. This limits a provider’s ability to unilaterally raise switching costs for consumers through its policy on the format in which the patient data is shared (e.g., giving hard-copy, rather than electronic, records to prior established patients who wish to switch to a new provider, an outcome that was shown to be possible in Result 2). We find that this feature can play an important role in supporting an equilibrium with electronic data sharing.

In the previous section, we have discussed a scenario in which both providers would benefit from mutual data sharing through interoperable EHR, but that such an outcome may not be attained due to the providers’ strategic behavior, because each has the incentive to unilaterally renege on the data-sharing arrangement. We find that the emergence of the platform can help resolve such incentive issues. Specifically, we carried out simulations to investigate the different possibilities in this scenario. Although such simulations cannot be exhaustive due to the surfeit of parameters, exploring across a range of parameter values gives us the following result.

<sup>Result</sup> <sup>3.</sup> The PHR platform can facilitate participation by selectively subsidizing providers. Across a range of parameter values, the likelihood that a subsidy is required for at least one provider increases as the two providers become more heterogeneous in terms of the value they provide to consumers and decreases as the proportion of new consumers in the first period goes up.

Figure 3 illustrates these possibilities. The figure identifies three distinct outcomes in terms of the adoption of interoperable EHR and data sharing and links these outcomes to two key parameters: provider heterogeneity and the extent of inherited consumers in the first period. We have previously established the importance of these two parameters in the discussion of Result 2. On the graph, a higher value on the horizontal axis reflects an increase in the perceived value of provider A relative to provider $B \ ( r _ { A } - r _ { B } )$ and thus an increase in A’s market share. A higher value on the vertical axis reflects an increase in the proportion of new consumers in the first period, <sub>t</sub>. The remaining inherited consumers are assumed to obtain new preference values, such that $\eta _ { t } + \mu _ { t } = 1$ A provider that lowers her switching costs reduces the likelihood an inherited consumer will stay, other things equal. On the other hand, a provider that lowers her switching costs increases the likelihood a new consumer will choose that provider, because the new consumer values lower future switching costs, other things equal. As the proportion of new consumers in the first period increases, new consumers’ (rational) expectations of future switching costs play a greater role in the providers’ choices of electronic data sharing.

Assuming that both providers have adopted EHR, the topmost area in the graph indicates the parameter values such that both providers would benefit from electronic data sharing and hence would be interested in joining the platform if their systems are not interoperable. To understand this outcome, consider the limiting case of the benchmark model, with symmetric sellers and no inherited consumers in the first period $( r _ { A } = r _ { B }$ and $\eta _ { t } = 1 )$ ). In this case, a unilateral reduction in switching costs improves the competitive position of a provider in the first period, because forwardlooking new consumers in the first period place a higher value on a provider with a lower switching cost given the chance in the second period that the consumer will desire to switch. The resulting increase in profits from new consumers in the first period to a provider who reduces switching costs more than outweighs the potential loss in profits from lower switching costs in the second period regardless of what the other provider has done. Thus, this represents the parametric region associated with voluntary electronic data sharing across the providers.

Figure 3 The Incentives of the Providers to Join the PHR Platform  
![](/api/attachments/MJBNBA4F/fulltext/images/b5b2addb4d41eddff3f618d517dc588584c4917d2476ad3cf4a2d29c6328a13e.jpg)

In contrast, the bottom area in the graph indicates the parameter values for which neither provider would find it advantageous to share the records electronically. Note that if providers are sufficiently similar and/or the inherited base of patients is sufficiently high (or, equivalently, the number of new consumers sufficiently low), then neither provider has an incentive to ease the switching process for consumers. For instance, for symmetric providers, as the proportion of inherited consumers in the first period increases, at some point the loss in profits from data sharing exceeds the associated gain due to being more attractive to new consumers who anticipate the potential desire to switch in the second period. Under these conditions, the PHR platform would need to subsidize both providers to secure their participation.

The middle area indicates the parameter values for which the smaller provider (B) is interested in data sharing, but the larger provider is not. The reason is that as provider A’s expected value advantage to consumers increases, and thus its market share, provider B appeals less to the new consumers in the first period. Accordingly, the smaller provider benefits relatively more from increased patient mobility, which enhances its perceived value by the new consumers who anticipate the other provider as being the more preferred provider in the second period. In contrast, as the market share of provider A increases due to its inherent higher valuation by consumers, electronically sharing patient records with the competing provider becomes less advantageous given the larger number of consumers who would leave with relative ease. Thus, in this parametric region, the PHR platform would need to subsidize provider A to ensure its participation. Note that this is precisely what Google Health and Microsoft HealthVault have embarked on doing with their (subsidized) partnerships with large, well-known providers.

We have indicated that by signing on the providers, possibly with a subsidy to induce participation or by providing costly software services, a PHR platform can offer a service that reduces switching costs across providers and provide patients with up-to-date online access to their medical history. What is the gain to the platform? While the PHR platform could charge a fee to patients, we expect the gains to be less direct due to the sensitivity of the information. Google, for example, expects that consumers who come to trust it for unbiased health information will subsequently use its other services exclusively in the long run. Thus, Google will benefit from its PHR service in a stochastic sense—the consumers of Google Health will indirectly provide revenues from the various other services that they use, when they, for example, click on advertiser links within other Google products (Healthcare Informatics 2008). Other sources of revenue can emanate from other entities, such as medical researchers who wish to gain access to the voluminous health data (with explicit permission from the patients) or companies who might wish to market medical devices (a strategy pursued aggressively by Microsoft HealthVault) or personalized advice to the patients (e.g., the online medical advice site Keas.com uses imported data from PHR services to come up with personalized recommendations for patients who grant access to their records).

## 6. Discussion and Conclusion

Studies have consistently pointed out the little progress that has been made in the United States toward a national health network, despite its distinct potential benefits. The core of the problem is that the adoption of interoperable systems and electronic sharing of data among competing providers requires that all key decision makers in a pluralistic system be better off by doing so. Online service providers such as Google and Microsoft have sensed the profit potential in this status quo, and have therefore decided to develop online PHR services that can extract some of the available surplus as rent. So, rather than an integrated, globally distributed health network, we may well be moving towards a system where health records are transported to and aggregated in “the cloud” provided by the private, independent PHR platforms. Our analysis shows that such platforms will have the incentive to not only provide the “middleware” for an interoperable system, but also in some cases subsidize the health-care providers in building their own EHR systems (or, equivalently, provide it as a cloud computing service).

Our results are important from a policy standpoint, because a significant amount of the public debate on health care revolves around the digitization and sharing of patients’ records among providers. Because many health-care providers do not have the incentive to adopt electronic health records, the subsidies provided to doctors in the recent stimulus bill to digitize patient records is indeed a laudable step. However, the results of our analysis indicate that this might not be enough, because even when competing providers (as well as their patients) stand to gain by sharing records electronically, an individual provider may have the perverse incentive to renege from such an arrangement. Data sharing may thus have to be enforced by diktat in the form of additional regulation, which may be met with resistance.

The cost of digitizing health-care records in the hospitals within the United States have been estimated at \$75 to \$100 billion dollars (Goldman 2009), and this represents a considerable risk for the stakeholders. As the ongoing experience of the United Kingdom government’s program to create an integrated national EHR shows (Charette 2008), such initiatives can go significantly over budget and behind schedule even in a single-provider system where providers do not have independent incentives. The challenges are only magnified in a pluralistic system. In this setting, the relatively low-key entry of a PHR platform such as Google Health can be a potentially important alternative to regulation. By enabling a proxy national exchange for health-care records, the presence of the online PHR platform can provide the impetus toward extracting the gains to shared EHRs.

The aggregation of health records in the cloud in a standard format has the potential to benefit medical research immensely. We believe that there will be significant opportunities for providers such as Microsoft and Google to tweak their revenue models in order to build a large base of users, as some industry observers have suggested (Roberts 2008). For example, Google can give consumers incentives for anonymous use of their health data: there can potentially be two types of subscriptions for consumers—a free subscription where consumers allow their data to be used anonymously, and a paid model where consumers strictly debar any use of their medical records whatsoever. Finally, PHR platforms can spawn increased loyalty of consumers for platform providers’ other online services such as search.

The main aim of this paper is to analytically investigate the adoption of EHR and the effect of electronic data sharing on consumer and provider surplus. As is customary in such a modeling exercise, we have abstracted away the many details of the health-care industry that do not directly affect the objectives of our study. One such modeling abstraction is the consideration of a single PHR platform. So far, the two major platforms from Google and Microsoft have tended to work with disjoint sets of providers in different localities that do not directly compete with each other. Although these two platforms (and perhaps some others) may engage in a fierce competition at some point in the future, it is important to keep in mind that the market for health care is for the most part local in nature—in rare cases do patients venture away from their local providers. We therefore believe that at this point it is justified to concentrate on the effect of an independent PHR platform on EHR adoption and data sharing, rather than the secondary effects of competition among platforms.

The model characterizes EHR as a technology that improves the quality of care. Due to our objective of focusing on how a widespread adoption of EHR can be achieved despite the misaligned incentives, we have not explicitly modeled some of the more subtle aspects that differentiate EHR systems, such as functionality and interoperability. We also have not explicitly incorporated the possibility of a patient working with multiple providers in the model, and furthermore, the benefit of EHR in allowing collaboration among such providers is only indirectly represented by an increase in the gross utilities of the consumers. Finally, in real life there are many variants of EHR with different types and levels of functionalities that may affect the quality of care consumers receive.

It is important to note that for a phenomenon as complicated as the health-care system in the United States, no single model can do justice to the entire environment. In this paper, the focus is on competing providers because they are the least likely to want to share records electronically among themselves. Therefore, their voluntary participation is essential for the widespread adoption, as well as sharing, of EHRs to materialize in the United States. Our model applies best to situations where consumers have access to a number of providers to choose from based on their preferences $( \mathrm { i . e . , }$ they are not simply referred to a specific specialist by the primary care physician). An example of such a specialty is obstetrics and gynecology. Our analysis also works better for patients with chronic medical conditions such as diabetes, rheumatoid arthritis, or chronic hepatitis that require chronic care management for effective long-term treatment. These types of diseases benefit greatly from patients’ ability to manage and keep track of their health-care records, and also generate substantial switching costs should the patients wish to change providers.

Although our model is specifically geared toward health care, with some modifications it can be applied to other environments that involve an online twosided market that reduces the switching costs for consumers. One example is that of the fast-growing financial aggregator site Mint.com, which can aggregate and analyze a consumer’s financial transactions across providers (banks, credit cards, loans, etc.) and come up with recommendations for competing financial products that can better serve the consumer. Other examples of this nature would include the popular bookmark aggregator delicious.com, which makes it easy for consumers to switch between browsers, and online “office suites” like Zoho.com and Google Docs that help consumers switch between different operating systems. In all such examples, the presence of the infomediary leads to lower switching costs and higher consumer surplus.

An extension of this research would be to consider vertical integration by the PHR platform. Once the PHR platforms are firmly established, they can take advantage of the cloud computing environment to provide EHR services to health-care providers as part of a software-as-a-service (SaaS) business model. In such a scenario, the cloud computing environment would provide advantages of scale that can be utilized by the online platforms to offer healthcare providers an EHR system at a much lower cost than an in-house system. Whereas the providers would obviously benefit from the cost savings, this arrangement might also benefit the consumers due to the higher rates of adoption of EHR systems.

## 7. Electronic Companion

An electronic companion to this paper is available as part of the online version that can be found at http:// isr.journal.informs.org/.

## Appendix

List of Notations Used in the Text

$a _ { i t }$ Level of amenities offered by provider i in period t $k _ { i } ( a _ { i t } )$ Fixed cost for provider i to offer amenities at level $a _ { i t }$ $c ( a _ { i t } )$ Marginal cost for provider i to offer amenities at level $a _ { i t }$ $q _ { i t }$ Output of provider i in period t $C ( q _ { i t } , a _ { i t } )$ Total cost for provider i to offer amenities at level $a _ { i t }$ $\theta$ Fixed component of marginal cost $c ( a _ { i t } )$ $p _ { i t } ^ { g }$ Gross price for provider i without accounting for amenities offered $p _ { i t }$ Price for provider i net of amenities offered $r _ { i }$ Gross utility of purchasing health-care services from provider i $\rho _ { t }$ $= ( 1 + r _ { A } - p _ { A t } - ( r _ { B } - p _ { B t } ) ) / 2$ 1 inserted for ease of exposition $j , j = 1 , \dots , L$ Consumers 1 through L $\eta _ { t }$ Proportion of consumers new to the market in period t $\varepsilon _ { j i t }$ Match loss for consumer j purchasing from provider i in period t $H ( \varepsilon )$ Uniform distribution of match loss values, with lower and upper bounds of 0 and 1, respectively $s _ { i k }$ Cost for consumer switching from provider i to k $( i \neq k )$ $\mu _ { t }$ Proportion of all consumers in period t who are experienced with new loss values $\alpha _ { t }$ Probability that a new consumer buys from provider A over provider B in time t

y<sub>t</sub> Probability an experienced consumer who purchased from provider A in period t − 1 and draws a new match loss value $x _ { t }$ Probability an experienced consumer who purchased from provider B in period t − 1 and draws a new match loss value $V _ { i t }$ Expected value associated with period t + 1 purchases of medical services conditional o being a patient of Provider i in period t $\beta$ Provider’s discount factor $\beta _ { c }$ Consumer’s discount factor $q _ { i t }$ The likelihood a consumer purchases from provider i in the current period t $\pi _ { i }$ Expected profit of provider i

## References

Bates, D. W., L. L. Leape, D. J. Cullen, N. Laird, L. A. Petersen, J. M. Teich, E. Burdick, M. Hickey, S. Kleefield, B. Shea. 1998. Effect of computerized physician order entry and a team intervention on prevention of serious medication errors. J. Amer. Medical Assoc. 28(15) 1311–1316.

Bates, D. W., J. M. Teich, J. Lee, D. Seger, G. J. Kuperman, N. Ma’Luf, D. Boyle, L. Leape. 1999. The impact of computerized physician order entry on medication error prevention. J. Amer. Medical Informatics Assoc. 6(4) 313–321.

Bender, M. W., A. H. Mitwalli, S. J. Van Kuiken. 2006. What’s holding back online medical data. McKinsey Quart. Issue 6(Winter 2005) 16–22.

Carr, N. 2009. The great library of Googleplex. http://www .roughtype.com/archives/2009/01/the\_great\_libra.php.

Charette, R. N. 2008. Electronic medical records: Dying for data. Accessed on February 15, 2009, http://www.spectrum.ieee .org/feb08/4589.

Gehrig, T., R. Stenbacka. 2004. Differentiation-induced switching costs and poaching. J. Econom. Management Strategy 13(4) 635–655.

Goldman, D. 2009. Obama’s big idea: Digital health records. Accessed on December 6, 2009, http://money.cnn.com/2009/01/12/ technology/stimulus\_health\_care/?postversion=2009011204.

Goth, G. 2008. Power to the patients. IEEE Distributed Systems Online 9(5) 1.

Harris Interactive. 2001. U.S. trails other English speaking countries in use of electronic medical records and electronic prescribing.

Health Care News 1(28). http://www.harrisinteractive.com/news/ newsletters/healthnews/hi\_healthcarenews2001vol1\_iss28.pdf.

Harris Interactive. 2001. The benefits of electronic medical records sound good, but privacy could become a difficult issue. Health Care News 1(28). http://www.harrisinteractive.com/news/ newsletters/healthnews/hi\_healthcarenews2001vol1\_iss28.pdf.

Healthcare Informatics. 2008. Google initiatives for Healthcare. Webinar, December 10. http://googleenterprise.blogspot.com/ 2008/12/helping-healthcare-providers-become\_04.html.

Hillestad, R., J. Bigelow, A. Bower, F. Girosi, R. Meili, R. Scoville, R. Taylor. 2005. Can electronic medical record systems transform health care? Potential health benefits, savings, and costs. Health Affairs 24(5) 1103–1117.

House of Representatives. 111th Congress, American Recovery and Reinvestment Act of 2009. H.R.1, January 6, http://www .gpo.gov/fdsys/pkg/PLAW-111publ5/content-detail.html.

Klemperer, P. 1995. Competition when consumers have switching costs: An overview with applications to industrial organization, macroeconomics, and international trade. Rev. Econom. Stud. 62(4) 515–539.

Knowledge@Wharton. 2007. The benefits, and potential side effects, of sharing medical records online. The Wharton Business School, University of Pennsylvania, Philadelphia, November 28. http://knowledge.wharton.upenn.edu/article .cfm?articleid=1846.

Klemperer, P. 1987. The competitveness of markets with wsitching costs. Rand J. Econom. 18(1) 138–150.

Lohr, S. 2008. Google becomes the latest entrant to offer personal health records on the web. New York Times (May 20) C3.

Mango, P. D., V. E. Reifberg. 2008. Three imperatives for improving U.S. health care. (December). McKinsey&Company, http:// www.mckinseyquarterly.com/Health\_Care/Hospitals/Three \_imperatives\_for\_improving\_US\_health\_care\_2274.

Marinoso, B. G. 2001. Technological incompatibility, endogenous switching costs and lock-in. J. Indust. Econom. 49(3) 281–298.

Markle Foundation. 2004. Financial, legal and organizational approaches to achieving electronic connectivity in healthcare. Markle Foundation, New York. http://www.markle.org/sites/ default/files/flo\_sustain\_healthcare\_rpt.pdf.

McBride, M. 2008. Google health: Birth of a giant. Newsweek 29 8–9.

Roberts, R. 2008. Cerner isn’t agog about google talks. Kansas City Bus. J. (June 2) B2.

von Weizsacker, C. 1984. The costs of substitution. Econometrica 52(5) 1085–1116.
