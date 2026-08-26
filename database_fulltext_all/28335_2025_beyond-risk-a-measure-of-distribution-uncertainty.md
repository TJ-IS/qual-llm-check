---
otero_id: 28335
otero_key: "4ANN96BW"
title: "Beyond Risk: A Measure of Distribution Uncertainty"
authors: "Tao Lu; Lihong Zhang; Xiaoquan (Michael) Zhang; Zhenling Zhao"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0089"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Beyond Risk: A Measure of Distribution Uncertainty

Tao Lu,<sup>a</sup> Lihong Zhang,<sup>b</sup> Xiaoquan (Michael) Zhang,<sup>c,</sup>\* Zhenling Zhao<sup>d,</sup>\*

<sup>a</sup> College of Business, Southern University of Science and Technology, Shenzhen 518055, China; <sup>b</sup> School of Economics and Management, Tsinghua University, Beijing 100084, China; <sup>c</sup> Department of Decisions, Operations and Technology, CUHK Business School, Chinese University of Hong Kong, Hong Kong; <sup>d</sup> Faculty of Business in Scitech, School of Management, University of Science and Technology of China, Hefei 230026, China

\*Corresponding authors

Contact: lut@sustech.edu.cn, https://orcid.org/0000-0001-7005-6366 (TL); zhanglh2@sem.tsinghua.edu.cn, https://orcid.org/0009-0003-0439-8124 (LZ); zhang@cuhk.edu.hk, https://orcid.org/0000-0003-0690-2331 (X(M)Z); zzl1212@ustc.edu.cn, https://orcid.org/0000-0002-6165-7407 (ZZ)

Received: February 10, 2022 Revised: May 6, 2023; May 9, 2024 Accepted: June 13, 2024 Published Online in Articles in Advance: August 21, 2024, and updated November 1, 2024, and April 3, 2025

https://doi.org/10.1287/isre.2022.0089

Copyright: © 2024 INFORMS

Abstract. Uncertainty, particularly distribution uncertainty (a.k.a. ambiguity), holds significant relevance in both academic research and practical applications. Much of the existing research, however, has concentrated primarily on addressing outcome uncertainty (or risk), frequently neglecting the aspect of distribution uncertainty. This research delves into distribution uncertainty, a critical yet often overlooked aspect of empirical research. We argue that there is a pressing need to integrate considerations of ambiguity directly into the development and implementation of data analytics models, calling for the promotion and wider use of a well defined measure of ambiguity. We introduce a quantitative measure of ambiguity that surpasses conventional approaches by precisely capturing distribution uncertainty. We illustrate the properties and advantages of this measure, highlighting its ability to enhance empirical models, yield more reliable parameter estimates, and contribute to the decision-making process. Using decision making in the financial market as an example, we demonstrate the value of this ambiguity measure. This paper promotes a more nuanced understanding of uncertainty and offers implications for both research methodologies and practical risk management.

History: Yong Tan, Senior Editor; Chad Ho, Associate Editor.

Funding: This work was supported by the University Grants Committee Research Grants Council [Grants GRF 14500521, 165052947, 14501320, 14503818, and TRS:T31-604/18-N], the National Natural Science Foundation of China [Grants 72121001, 72301125], the Tsinghua University Initiative Scientific Research Program [Grant 2021THZWJC28], and the Shenzhen Stable Support Plan Program for Higher Education Institutions [Grant 20220815111555004].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.0089.

Keywords: ambiguity • financial market • uncertainty • distribution uncertainty • statistical inference

As far as the laws of mathematics refer to reality, they are not certain; and as far as they are certain, they do not refer to reality. —Albert Einstein

## 1. Introduction

Information systems (IS) research is a multidisciplinary field that investigates the design, implementation, management, and usage of information technology (IT) to solve business problems and enhance organizational performance. A key focus of IS research is to ensure that information is processed correctly and effectively. This focus spans various aspects of information processing, including data collection, storage, and analytics, and the transformation of data into actionable insights.

Pervasive inherent uncertainty in the real world often forces business decisions to be made using uncertain data. IS plays an essential role in reducing uncertainty by effectively managing and utilizing data to produce clearer, more predictable outcomes from ambiguous situations (Brynjolfsson et al. 2021). Uncertainty is one of the most important research topics in the IS literature. Many IS research streams fundamentally aim to reduce uncertainty in decision making for various members of society: in e-commerce (Pavlou et al. 2007, Dimoka et al. 2012, Fang et al. 2021), pricing (Brynjolfsson and Smith 2000, Wang and Zhang 2009), word of mouth (Dellarocas et al. 2007, Zhu and Zhang 2010, Lu et al. 2022), keyword auctions (Zhang and Feng 2011, Du et al. 2017, Gong et al. 2018), crowdfunding (Jiang et al. 2022, Kim et al. 2022, Hu et al. 2023), social media (Zhang and Zhu 2011, Xu and Zhang 2013, Rishika and Ramaprasad 2019), e-health (Gao et al. 2015, Zhou et al. 2023), online dating (Bapna et al. 2016, Shen et al. 2024), and finance (Zhang and Zhang 2015, Hendershott et al. 2021, Zhang and Zhang 2024).

This research delves into distribution uncertainty, a critical yet often overlooked aspect in both academia and the industry. Uncertainty can be divided into two distinct constructs: outcome uncertainty (or risk, with unknown outcomes but known distributions) and distribution uncertainty (or ambiguity, with unknown outcomes and unknown distributions). Knight (1921) initially distinguished the difference between risk (or outcome uncertainty) and ambiguity (or distribution uncertainty). Subsequent researchers, including Ellsberg (1961) and others such as Camerer and Weber (1992), Epstein and Zhang (2001), Abdellaoui et al. (2005), Maafi (2011), Abdellaoui et al. (2011), and Li et al. (2018), have underscored decision making under ambiguity as an important domain of research.

Ellsberg urns provide a clear illustration of the distinction between risk and ambiguity within decision-making contexts. Consider two urns, each containing 100 balls that can be either red or blue. Players are tasked with placing bets on the color of the ball that will be drawn from these urns, earning \$1 if a red ball is drawn and nothing for a blue one. The key difference between the two urns lies in the distribution of colors: urn A has a known distribution, with 50% of the balls being red and 50% being blue, allowing players to make informed bets based on these probabilities. A risk-neutral player is expected to bet \$0.50 to play such a game.

Ambiguity enters the scenario with urn B, where the distribution of red and blue balls is unknown. Players know that the urn contains 100 balls in total, which are a mix of red and blue, but the exact number of each color is not disclosed. This uncertainty represents ambiguity. Unlike risks, which are measurable and quantifiable uncertainties (as seen with urn A), ambiguity involves unknown probabilities, making it impossible to calculate odds or expected outcomes precisely. When facing urn B, a risk-neutral player often demands a higher compensation, by betting less than \$0.50 to play such a game.

The difference between the bets on the two urns measures players’ ambiguity aversion. If they know that there is no ambiguity, then they can use traditional models to bet \$0.50, and if they know ambiguity exists, they adjust their decision and bet less. If decision makers are to optimize their actions, it becomes imperative to accurately ascertain the level of distribution uncertainty prevalent in their environment.

From this example, it is easy to see (1) the data generating process in the real world often suffers from the issue of distribution uncertainty, in addition to outcome uncertainty, and (2) decision makers need to know the level of distribution uncertainty before they can decide their course of action based on their model of outcome uncertainty.

Despite the clear influence of ambiguity on decision making, two significant research gaps remain notably underexplored. First, there is a pressing need to integrate considerations of ambiguity directly into the development and implementation. Current empirical research frameworks predominantly cater to environments where outcome uncertainties are quantifiable and well defined, often neglecting scenarios where the probabilities of outcomes are themselves uncertain. This oversight can lead to the development of models that are ill equipped to support decision making in real-world scenarios characterized by high levels of ambiguity. The development of systems that can adapt to and effectively operate under conditions of ambiguity would mark a significant advancement in the field, enhancing the robustness and applicability of these systems across a broader spectrum of uncertain environments.

Second, the absence of a robust measure of ambiguity constitutes a critical limitation in both research and practice. Current methodologies largely focus on quantifying uncertainty in scenarios where the risks are known and probabilities can be assigned. For example, Benaroch (2018) represented uncertainty in terms of probability distribution and studied mitigations to reduce uncertainty in IT investment. However, these methods fall short in situations where such probabilities are unclear or entirely unknown—conditions that frequently arise in business, economics, finance, and beyond. Developing a standardized and easy-to-obtain measure of ambiguity would not only facilitate further research on this important topic but also empower practitioners to better assess and manage the uncertainty associated with unknown distributions.

With the advancement of IT, it is anticipated that the era of big data will alleviate information asymmetry or uncertainty (Mishra et al. 1998). For example, Amzal et al. (2006) advocate for a close association between statistical analysis, inference, and the data collection process. However, data collected from various sources such as sensors, social media, and financial records inherently carry uncertainty due to noise, incompleteness, and inconsistency. When decision makers rely on statistical analysis or data analytic models to derive empirical insights from the data, they must account for potential uncertainty, both outcome and distributional. In cases where the issue of uncertainty in distribution (ambiguity) arises, commonly used models may yield unreliable results. Given the widespread adoption of data analytics in research and practice, it is crucial to identify situations when ambiguity arises, measure it, and then develop methods to improve reliability.

To demonstrate how a measure of ambiguity is useful, we next discuss its application in ordinary least squares (OLS) regressions. OLS is a widely employed method for conducting empirical research. Although the Gauss–Markov theorem does not need a normality assumption to obtain unbiased estimates of means, the normality assumption is needed to have unbiased estimates of standard errors, and therefore influence confidence intervals and p-values (Schmidt and Finan 2018). In Wooldridge (2010), this assumption is named MLR.6. It can be shown that, under the assumptions of the classical linear model, the OLS estimators have the smallest variance among all the unbiased estimators. A good ambiguity measure can estimate how much the real distribution deviates from the assumed distribution. If there is no deviation, then estimates of standard errors obtained from OLS are trustworthy. However, when the deviation is large because of ambiguity, confidence intervals and p-values can no longer be trusted. Wooldridge (2012, p. 120) states that

Because u (error term) is the sum of many different unobserved factors affecting y (dependent variable), we can invoke the central limit theorem (see Appendix C) to conclude that u has an approximate normal distribu tion. This argument has some merit, but it is not without weaknesses. First, the factors in u can have very different distributions in the population (for example, ability and quality of schooling in the error in a wage equation). Although the central limit theorem (CLT) can still hold in such cases, the normal approximation can be poor depending on how many factors appear in u and how different their distributions are.

Later, in his appendix C, Wooldridge (2012, p. 767) warns: “A more serious problem with the CLT argument is that it assumes that all unobserved factors affect y in a separate, additive fashion. Nothing guarantees that this is so. If u is a complicated function of the unobserved factors, then the CLT argument does not really apply.” In such situations, when the distribution of the error term is uncertain or when ambiguity arises, there is no guarantee that the normality assumption is met. This may lead to errors in derived confidence levels. Adjusting the confidence levels for ambiguity, based on a measure of ambiguity, can therefore enhance various prediction, classification, and causal inference models. For example, a doctor using an analytics model based only on outcome uncertainty may expect a 99% success rate for prescribing a medicine to a patient. But in cases of significant ambiguity, confidence in the 99% parameter estimate can drop to as low as 60%, depending on the distribution uncertainty in the patient population, and potentially lead to severe consequences for the patient’s health. In this context, a good ambiguity measure offers a “confidence of confidence” for the estimates: the first “confidence” pertains to the level of distribution uncertainty, and the second “confidence” is related to the level of outcome uncertainty.

Despite recognizing ambiguity as a crucial factor, there remains a lack of clarity regarding its measurement. Previous studies have primarily investigated ambiguity through theoretical modeling or questionnaires. Theoretical papers often employ subjective expected utility (SEU) theory to explore ambiguity aversion, as probabilities are not necessarily objectively known in SEU (Camerer and Weber 1992, Klibanoff et al. 2005, Van De Kuilen and Wakker 2011, Abdellaoui et al. 2021). Questionnaires are thoughtfully designed to investigate various uncertainty scenarios, such as environmental uncertainty (Karimi et al. 2004, Chung et al. 2019), role ambiguity (Rizzo et al. 1970, Ayyagari et al. 2011, Ply et al. 2012), product uncertainty (Dimoka et al. 2012, Hong and Pavlou 2014), evaluation uncertainty (Lu et al. 2022), and privacy uncertainty (Al Natour et al. 2020), among others.

Prior literature proposed some measures of ambiguity. Anderson et al. (2009) proposed an ambiguity measure based on the disagreement among professional financial analysts. Williams (2015) suggested using the Chicago Board Options Exchange (CBOE) Volatility Index (VIX) as a measure of ambiguity. Chen et al. (2021) modeled and measured product quality uncertainty using the ratio of variance to the mean of online product ratings. However, these measures do not effectively distinguish between risk and ambiguity. Gong et al. (2018) and Hansen and Sargent (2001) proposed employing entropy to measure ambiguity. As we will discuss in detail in Section 3.1, the application of entropy has severe limitations.

To offer a more robust measurement of ambiguity, this paper proposes the use of the Hellinger distance (HD) as a measure for quantifying ambiguity. Although this measure is not a new mathematical con struct, it is the first time for it to be used in this setting. We argue that integrating our ambiguity measure, alongside traditional outcome uncertainty measures such as volatility and entropy, can enhance the accuracy and effectiveness of data analytics models. In this context, this paper aims to (1) advocate for the consideration of ambiguity in decision making, warning that neglecting it may result in misinterpretation of empirical findings and failure of information systems, and (2) introduce a measure quantifying ambiguity, demonstrating its implications and applications in providing useful additional information about uncertainty.

To illustrate the value of measuring ambiguity, we take the financial market as an example. Financial participants often overlook ambiguity in underlying distributions when relying on idealized financial economics models to understand the market and make decisions. For example, it is commonly assumed that financial assets’ price movements can be described using a geometric Brownian motion with constant drift and volatility. This leads to the assumption that financial returns are normally distributed (e.g., Black and Scholes 1973). The common assumption of normality in the underlying distribution may underestimate the frequency of highrisk downward movements, such as black swan events. For example, on October 19, 1987, the Dow Jones Industrial Average experienced a 22.6% plunge in a single day, a return equivalent to 22 standard deviations below the mean. If the returns had been normally distributed, the probability of observing such a return on that day would have been 10<sup>�107</sup>.<sup>1</sup> The extreme events occur more frequently than their probabilities suggest, revealing fundamental flaws in naively using the normality assumption to describe returns. Moreover, the dynamic nature of the underlying distribution suggests that the current distribution of returns may fail to hold in the future, leading to challenges to models that rely on invariant distribution.

In this paper, we argue that ambiguity can be quantified by measuring the distance between the actual distribution and the distribution of outcomes predicted by a reference model. The HD proves effective in capturing the dynamic nature of distributions, making it an ideal metric for ambiguity evaluation. Compared with other existing measures, the HD stands out by aligning with the definition of ambiguity, being normalized, and being easy to calculate. We initially explore its statistical properties and then conduct a simulation study to illustrate the advantages of explicitly considering ambiguity when running regression models. To illustrate the application of ambiguity, we estimate the HD in the financial market and show that incorporating ambiguity into data analytics models can lead to important new insights.

Our contribution to the literature lies in (1) theoretically proposing the difference between subjective and objective ambiguity, (2) deepening the understanding of how ambiguity may change the results obtained in data analytics models, (3) characterizing the statistica properties of the measure, and (4) highlighting the effectiveness of using the HD as a measurement tool for ambiguity. In addition to the established theoretical models of ambiguity aversion and questionnaires, we present a robust measure for quantifying ambiguity. By offering a concrete measure for ambiguity, we enable practitioners to assess the confidence of existing empirical models. This is particularly valuable in situations where high ambiguity renders traditional models unreliable. Practitioners can leverage our research findings to complement their current uncertainty measures. Beyond the financial market, our approach holds relevance in IS, marketing, and operations management where data analytics are employed for business intelligence, shedding light on valuable and previously unexplored insights by considering ambiguity and utilizing our proposed measure.

The structure of this paper is organized as follows. The subsequent section provides an introduction to the research background. In Section 3, we conduct a review of existing ambiguity measures, introduce our proposed ambiguity measure, and scrutinize its statistical properties. Section 4 explores the application of our ambiguity measure in the financial market as an illustration. Finally, Section 5 presents the conclusion of our study.

## 2. Background

## 2.1. Uncertainty: Risk and Ambiguity

Traditional information theory characterizes uncertainty as a feature of situations where the set of possible future outcomes is identified, but the associated probability distributions are either unknown or, at best, known subjectively (Schrader et al. 1993). Knight (1921) initially defines risk as a special case of uncertainty with known probabilities, whereas ambiguity is characterized by uncertainty with unknown probabilities. It is crucial, both in literature and practice, to distinguish between risk and ambiguity.

However, ambiguity and uncertainty are often treated as synonymous in practice, lacking an explicit distinction between them. The literature has defined the concepts of uncertainty or ambiguity in various ways, contingent upon the nature of the addressed research question. For example, in the context of online markets, Dimoka et al. (2012) define uncertainty as the challenge faced by buyers in predicting the outcome of an online transaction due to information asymmetry related to sellers and products. Specifically, they distinguish seller uncertainty as the buyer’s challenge in assessing the true characteristics of the seller and predicting whether the seller will act opportunistically. Simultaneously, they characterize product uncertainty as the buyer’s difficulty in thoroughly evaluating the product and forecasting its future performance.

Numerous studies, such as those by Klibanoff et al. (2005), Van De Kuilen and Wakker (2011), and Abdellaoui et al. (2021), have introduced theoretical models to investigate risk attitudes and ambiguity attitudes. Ellsberg’s experiment (Ellsberg 1961) has inspired many studies on ambiguity aversion, resulting in the develop ment of several theoretical models, including the multiple-priors model (Gilboa and Schmeidler 1989), robust-control model (Hansen and Sargent 2001), and smooth-ambiguity model (Klibanoff et al. 2005). Although these studies have significantly advanced ou understanding of ambiguity aversion, our approach in this paper introduces a unique differentiation between subjective and objective ambiguity.

Previous works predominantly focus on subjective ambiguity, delving into insights about ambiguity aversion among decision makers. Epstein and Zhang (2001) provide a behavioral definition of subjective ambiguity in an abstract setting involving Savage-style (Savage 1954) acts, and Zhang (2002) derives subjective ambiguity from preferences, suggesting that decision makers use unambiguous acts to approximate ambig uous ones. In contrast, Olszewski (2007) defines objective ambiguity as the absence of a single (objective) probability distribution over outcomes, interpreting larger sets of possible probability distributions as more ambiguous information.

In our study, we define objective ambiguity as the degree or extent of discrepancy between the actual distribution and a reference distribution. This metric can be derived from historical data and remains unaffected by decision makers’ preferences or attitudes. Agents lacking sufficient knowledge of the true distribution are unable to construct a reliable probability model that accurately characterizes data relationships (Hansen and Sargent 2001, Uppal and Wang 2003). Consequently, in research and practice where ambiguity is significant, the outcomes cannot be treated the same as in the situation when ambiguity does not exist. Therefore, incorporating a measure of ambiguity is crucial for ensuring the validity of empirical models.

## 2.2. Literature on Ambiguity

Duncan (1972) argues that the nature of uncertainty or ambiguity can manifest in either environmental or behavioral dimensions. Environmental uncertainty typically pertains to the uncertainty faced by an organization, whereas behavioral uncertainty is commonly employed to characterize an individual’s decisionmaking processes. Investigating the impact of environmental uncertainty and task characteristics on user satisfaction with data, Karimi et al. (2004) utilize IS and organizational theories and found that environmental uncertainty has a positive impact on task characteristics. Chung et al. (2019) examine the impact of contextual factors related to the nature of innovation underlying firms’ patent portfolios and environmental uncertainty on the value of software patents.

In the absence of a proper measurement of ambiguity, these studies have primarily relied on thoughtfully designed questionnaires. Rizzo et al. (1970) define role ambiguity as individual’s confusion regarding the definition and expectations of the job, developing and testing questionnaire measures for role ambiguity. Similarly, Ayyagari et al. (2011) consider the item “I am unsure what to prioritize: dealing with information and communication technologies (ICT) problems or my work activities” in the questionnaire to measure role ambiguity, finding that work overload and role ambiguity are the two most dominant stressors in the technological antecedents.

In e-commerce online markets, buyers continue to suffer from information asymmetry when purchasing experience products (Nelson 1970), such as used cars, that cannot be easily evaluated before purchase. This information asymmetry, in turn, gives rise to uncertainty or ambiguity. For example, product uncertainty, initially proposed by Arrow (1963), has recently been recognized as a significant impediment to online markets (e.g., Ghose 2009, Dimoka et al. 2012, Kim and Krishnan 2015), although IT systems such as diagnostic websites (Jiang and Benbasat 2007), third-party certifications (Dimoka et al. 2012, Kim et al. 2022), and digital videos (Kim and Krishnan 2015) have proven helpful in reducing product uncertainty. Dimoka et al. (2012) speculate that product uncertainty negatively impacts price premiums in online markets beyond seller uncertainty. Hong and Pavlou (2014) introduce the construct of product fit uncertainty (PFU), defined as the degree to which a consumer cannot assess whether a product’s attributes match his or her preference. The PFU is measured by asking consumers to report their subjective assessment of whether they were certain that the product would match their preferences. Al-Natour et al. (2020) elucidate the role of privacy uncertainty in the context of purchasing and using mobile apps by examining four research questions, introducing privacy uncertainty as an additional construct in the nomologic network explaining the intentions to purchase as well as continued use.

Although questionnaires are a straightforward method for measuring “ambiguity,” they pose a risk of biased results if participants interpret and respond to items inappropriately, resulting in “subjective” ambiguity. To address this limitation, we emphasize the importance of objective ambiguity, measured as the distance between the actual distribution and a reference distribution. Given data availability, we explore the application of ambiguity in the financial market as an illustrative example.

The financial market, recognized as a complex and dynamic system with independent and constantly changing participants, is considered efficiently inefficient because of the inherent difficulty in predicting future events (Pedersen 2019). It is viewed as more efficient, liquid, and with less information asymmetry because of the implementation of electronic securities trading systems (Clemons and Weber 1996, 1997) and the evolution of the internet (Barclay et al. 2003). According to the efficient market hypothesis, share prices reflect all available information. However, in cases where one party (informed traders) in the transaction possesses more information than the others (noisy traders), uncertainty arises because of asymmetric information (Mishra et al. 1998; Zhang and Zhang 2015, 2024).

Researchers and practitioners commonly rely on the volatility or standard deviation of stock returns as a measure of risk and uncertainty (Shiller 1987). Stock returns are typically modeled assuming a normal distribution (Black and Scholes 1973), which works well in normal market conditions but proves inadequate dur ing market turmoil (e.g., Gabaix et al. 2003; Barro 2006, 2009). During market crashes, prices experience signifi cant declines and turbulent periods characterized by high variability. A well-acknowledged fact is that stock return changes follow a distribution with fatter tails than the normal distribution predicts, meaning that outliers occur more frequently than expected. To address this issue, Mandelbrot (1963) proposed utilizing “fattailed” distributions from the Paretian family, accommodating infinite standard deviations to describe stock returns. This solution allows for outliers to have a reasonable probability of existence, albeit at the expense of penalizing observations in the head of the distribution. Despite researchers recognizing distribution uncertainty or ambiguity, they often prioritize risk considerations, such as tail risk or downside risk. Once again, our HD approach perfectly captures the variation in the distribution.

The inherent complexity, behavioral aspects, and dynamic nature of the financial market make it an ideal arena for studying ambiguity or uncertainty. Examining the intricacies of financial markets provides researchers and practitioners with valuable insights into decision-making processes and risk management strategies in the presence of ambiguity. In the following section, we review other measures of ambiguity applied in finance and then introduce our approach of HD as a new measure of ambiguity.

## 3. Measurements of Ambiguity

Prior literature mainly focuses on subjective ambiguity and relies on thoroughly designed questionnaires to measure various kinds of reactions to uncertainty or ambiguity. This section focuses on objective ambiguity and provides a review of proposed metrics that have been suggested as proxies for measuring ambiguity. Notably, four quantitative approaches have been proposed, including dispersion in analyst forecasts, the CBOE VIX, f (mho), and relative entropy. We then introduce the HD as a new ambiguity measure and discuss its statistical properties and application in regression models.

## 3.1. Alternatives of Ambiguity

Agents are presumed to have substantial information about return volatility but limited knowledge about mean returns. To measure the extent of agents’ uncertainty regarding mean returns, Anderson et al. (2009) propose an ambiguity measure based on the disagreement among professional financial analysts. This measure relies on the variance of forecasts extracted from the Survey of Professional Forecasters. When all forecasters are in agreement about expected returns, uncertainty is likely low. Conversely, if forecasters articulate significantly different forecasts, agents are likely unsure about mean returns, resulting in high uncertainty. However, discerning ambiguity from risk presents challenges with this measure, as the dispersion of forecasts correlates strongly with stock price volatility. Additionally, this measure accommodates both forecasters’ subjective opinions regarding ambiguity and the objective ambiguity emanating from the market.

The CBOE VIX is widely recognized as an indicator of market panic, and Williams (2015) advocates its use as a measure of ambiguity. Nonetheless, the VIX might not be an ideal representation of ambiguity, as it incorporates information related to both risk and ambiguity, as confirmed by Miao et al. (2019). Moreover, from a theoretical standpoint, the VIX lacks a direct connection to distribution uncertainty.

Brenner and Izhakian (2018) introduce an ambiguity measure denoted by f (mho), which quantifies the uncertainty associated with the distribution of a financial asset’s returns. The quantity f is defined as

$$
\mathcal {U} ^ {2} [ r ] = \int \operatorname{E} [ \phi (r) ] \mathrm{Var} [ \phi (r) ] d r,
$$

where $\phi ( r )$ represents the probability density function of return $r ,$ whereas $\mathrm { E } [ \phi ( \boldsymbol { r } ) ]$ and $\mathrm { V a r } [ \phi ( r ) ]$ denote the expected probability and variance of return r, respectively. The compound probability model underlying f offers a comprehensive framework for empirical analysis (Augustin and Izhakian 2020, Izhakian et al. 2022). However, its calculation demands the distribution of distributions of stock returns, which requires highfrequency transaction data and is not readily accessible. This constraint presents challenges to effective decision making under distribution uncertainty.

Relative entropy, also known as Kullback–Leibler (KL) divergence, provides an alternative method for quantifying the disparity between a reference model and alternative models, falling within the family of $f -$ divergence (Gibbs and Su 2002). The relative entropy is defined from probability function $p _ { 2 } ( x )$ to $p _ { 1 } ( x )$ and requires that $p _ { 1 } ( x )$ is absolutely continuous with respect to $p _ { 2 } ( x )$

$$
D _ {\mathrm{KL}} (p _ {1} | | p _ {2}) = \sum_ {x} p _ {1} (x) \ln \left(\frac {p _ {1} (x)}{p _ {2} (x)}\right).
$$

However, the incorporation of the Radon–Nikodym derivative in defining the relative entropy imposes a constraint on the zero probability set of $p _ { 1 }$ . This requirement dictates that the zero probability set of $p _ { 1 }$ must align with the set of $_ { p _ { 2 } , }$ limiting its applicability in addressing extreme events, such as black swan moments. Additionally, the nonmetric property of the KL divergence (Gibbs and Su 2002), demonstrated by its asymmetry and failure to adhere to the triangle inequality, complicates the derivation of a consistent measure of ambiguity.

In summary, despite various attempts to develop ambiguity measures, existing measures have shortcomings, as shown in Table 1. Therefore, this paper proposes using the Hellinger distance between the empirical distribution and a reference distribution to assess ambiguity. This approach has the advantage of avoiding the requirement for identical zero support sets between the two distributions being compared. Furthermore, we demonstrate that the proposed measure serves as a valid indicator of ambiguity and provides additional valuable information for estimating market and individual stock crash risks.

Table 1. Summary of Ambiguity Measures

<table><tr><td>Measure</td><td>Pros</td><td>Cons</td></tr><tr><td>Forecast disagreement</td><td>Based on professional financial analysts&#x27; variance of forecasts; reflects uncertainty about mean returns</td><td>Challenges in distinguishing ambiguity from risk because of correlation with stock price volatility; subjective opinions may influence the measure</td></tr><tr><td>CBOE Volatility Index (VIX)</td><td>Widely recognized as an indicator of market panic</td><td>Cannot tease out risk from ambiguity; lacks a direct connection to distribution uncertainty</td></tr><tr><td> $\mathcal{U}$  (Mho) measure</td><td>Quantifies uncertainty associated with a financial asset&#x27;s returns distribution</td><td>Requires high-frequency transaction data for calculation; not readily accessible</td></tr><tr><td>Relative entropy (KL divergence)</td><td>Alternative method for quantifying disparity between reference and alternative models</td><td>Constraint on zero probability set alignment; nonmetric property complicates derivation</td></tr><tr><td>Hellinger distance</td><td>Distance between empirical and reference models; normalized metric; no conditions on support sets of distributions; no infimum or supremum calculations required</td><td></td></tr></table>

## 3.2. Hellinger Distance

A suitable ambiguity measure should meet several criteria. First, it should be easy to compute, even in the absence of comprehensive information about the true model, such as the probability distributions of an observable quantity. Second, the measure should demonstrate metric properties, including symmetry and the triangle inequality, ensuring that the distance between two distributions remains consistent regardless of the chosen reference distribution. Third, the measure should be normalized, facilitating comparisons between different levels of ambiguity. Based on these requirements, we propose using the Hellinger distance as an ambiguity measure.

The Hellinger distance, first proposed by Hellinger (1909), is a distance function between two probability distributions. For two cumulative distribution functions $P _ { 1 }$ and $P _ { 2 } ,$ the HD between them is defined as

$$
H D ^ {2} (P _ {1}, P _ {2}) = \frac {1}{2} \int \left(\sqrt {\frac {d P _ {1}}{d \lambda}} - \sqrt {\frac {d P _ {2}}{d \lambda}}\right) ^ {2} d \lambda ,\tag{1}
$$

where λ is a third cumulative distribution function. The HD is independent of the choice of λ. If the two distributions have probability density functions $f _ { 1 } ( x )$ and $f _ { 2 } ( x )$ , the HD can be calculated as

$$
H D ^ {2} (P _ {1}, P _ {2}) = \frac {1}{2} \int_ {- \infty} ^ {\infty} \left(\sqrt {f _ {1} (x)} - \sqrt {f _ {2} (x)}\right) ^ {2} d x.\tag{2}
$$

We will now outline the advantages of using the HD as a measure of discrepancy between two probability distributions, comparing it with other measures. First, the HD does not impose specific criteria on the zero support sets of distributions, allowing for the inclusion of rare black swan events that may be deemed implausible by prevailing reference models or historical experiences.

Second, the HD is normalized, that is, $0 \leq H D ( P _ { 1 } , P _ { 2 } )$ $\leq 1$ , regardless of the distributions being compared. A value of zero indicates practically identical distributions, whereas a value of one signifies almost surely disjoint support sets. This normalization feature facilitates the comparison of various levels of ambiguity. We demonstrate how uniform HD thresholds can be determined for normal reference distributions in the subsequent section.

Third, the HD adheres to fundamental axiomatic properties of a metric, including the identity of indiscernibles, nonnegativity, symmetry, and triangle inequality. These properties provide a set of well-defined, mathematically rigorous distance measures for comparison. Although alternative measures like the Wasserstein metric and total variation distance could be employed, the HD is preferred because of its avoidance of infimum or supremum calculations. Additionally, the HD encompasses all distances within the family of f-divergences (Csisza´r 1967, Gibbs and Su 2002), including the Kullback–Leibler divergence, emphasizing its suitability for probabilistic analysis.

It is important to note that the HD’s symmetry implies its inability to address inquiries about the direction of deviation between empirical and reference distributions. Consequently, decision makers must rely on the empirical distribution as an estimator of the actual distribution. In contexts such as the stock market, identifying deviations may not necessarily pose a challenge, as various other economic and financial variables can be observed.

## 3.3. Statistical Properties of the Hellinger Distance

The normality assumption is widely applied in the literature, leveraging the CLT to assert that the average of a sample from a random variable is asymptotically normally distributed. In regression analysis, assumption MLR.6 from Wooldridge (2010) states that the unobserved error is assumed to be normally distributed in the population. This assumption, combined with the

Gauss–Markov assumptions, is essential for making the sampling distributions of the estimators tractable.

When the distribution of the error term is uncertain or when ambiguity arises, there is no guarantee that the normality assumption is met. This may lead to errors in the derived confidence levels. Adjusting the confidence levels for ambiguity, based on a measure of ambiguity, can therefore enhance various prediction, classification, and causal inference models.

Our proposed measure reflects the degree to which actual data deviates from the normality assumption. A larger discrepancy signifies a greater distance and a diminished applicability of the normality assumption. To assess the confidence level at which two distributions differ from each other, we need to estimate the critical value of HD corresponding to the confidence level. We examine the HD between two normal distributions with distinct mean and standard deviation parameters to determine the critical values.

The choice of the normal distribution as the reference distribution reflects our objective to measure how the real world deviates from the perceived “ideal” world. It also makes the measure very useful in practice: if severe differences exist between the two distributions, then it suggests that the traditional model (which relies on the “ideal” assumption) may not be that useful anymore. It is important to note that a normal reference distribution is not mandatory. In some settings, commonly assumed distributions may take other functional forms $( \mathrm { e . g . }$ , exponential distribution), and then these alternative distributions can serve as the reference distributions.

The HD between two normal distributions is given by

$$
H D ^ {2} (P _ {1}, P _ {2}) = 1 - \sqrt {\frac {2 \sigma_ {1} \sigma_ {2}}{\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2}}} \exp \left[ - \frac {1}{4} \frac {(\mu_ {1} - \mu_ {2}) ^ {2}}{\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2}} \right],\tag{3}
$$

where $\mu _ { 1 }$ and $\mu _ { 2 }$ are the means and $\sigma _ { 1 }$ and $\sigma _ { 2 }$ are the standard deviations of the two normal distributions, respectively.

Determining critical values for the HD concerning a normal reference distribution can be accomplished with relative simplicity. The null hypothesis stating that the empirical and reference distributions are identical can be rejected through a meticulous appraisal of critical values. To obtain this outcome, we can conveniently employ Equation (3) to represent statistical measures of traditional statistical tests explicitly devised for normal distributions, such as the F-test and Welch’s t-test. The HD between two normal distributions can be written as

$$
H D = \sqrt {1 - a \exp (b)},\tag{4}
$$

where $\begin{array} { r } { a = \sqrt { \frac { 2 \sigma _ { 1 } \sigma _ { 2 } } { \sigma _ { 1 } ^ { 2 } + \sigma _ { 2 } ^ { 2 } } } } \end{array}$ and $\begin{array} { r } { b = - \frac { 1 } { 4 } \frac { ( \mu _ { 1 } - \mu _ { 2 } ) ^ { 2 } } { \sigma _ { 1 } ^ { 2 } + \sigma _ { 2 } ^ { 2 } } . } \end{array}$ . Considering the

F-test of equality of variances, the test statistic $\begin{array} { r } { F = \frac { \sigma _ { 1 } ^ { 2 } } { \sigma _ { 2 } ^ { 2 } } } \end{array}$ has an F-distribution with parameters $d _ { 1 } = d _ { 2 } = N - 1 .$ Here, we impose the assumption that the sizes of the two samples are the same. The cumulative distribution function of this F-distribution is then

$$
P _ {F} (x) = I _ {\frac {x}{x + 1}} \left(\frac {N - 1}{2}, \frac {N - 1}{2}\right), \text {   for   } x > 0,\tag{5}
$$

where I is the regularized incomplete beta function. The part of this function for $x \le 0$ is not needed fo evaluating critical values of the HD. For any given $p \mathrm { - }$ value, the corresponding minimum and maximum values of the test statistic are $F _ { \mathrm { m i n } } = P _ { F } ^ { - 1 } ( p )$ and $F _ { \mathrm { m a x } } =$ $P _ { F } ^ { - 1 } ( 1 - p )$ . Noticing that the quantity a in Equation (4) can be written as $\begin{array} { r } { a = \sqrt { \frac { 2 \sqrt { F } } { F + 1 } } , } \end{array}$ , for any given p-value, the corresponding minimum value of a is

$$
a _ {\min} = \min \left[ \sqrt {\frac {2 \sqrt {P _ {F} ^ {- 1} (p)}}{P _ {F} ^ {- 1} (p) + 1}}, \sqrt {\frac {2 \sqrt {P _ {F} ^ {- 1} (1 - p)}}{P _ {F} ^ {- 1} (1 - p) + 1}} \right].
$$

For the Welch’s t-test, the test statistic $\begin{array} { r } { t = \sqrt { N } \frac { \mu _ { 1 } - \mu _ { 2 } } { \sqrt { \sigma _ { 1 } ^ { 2 } + \sigma _ { 2 } ^ { 2 } } } } \end{array}$ has a Student’s t-distribution with the parameter approximately equal to $\nu = 2 ( N - 1 )$ . Here, the sizes of the two samples should be the same, and the variances of the two samples are approximately the same.<sup>2</sup> The cumulative distribution function of this Student’s t-distribution is

$$
P _ {t} (x) = \frac {1}{2} I _ {\frac {2 (N - 1)}{x ^ {2} + 2 (N - 1)}} \left(N - 1, \frac {1}{2}\right), \text {   for   } x \leq 0,\tag{6}
$$

where I is the regularized incomplete beta function. For any given p-value, the corresponding minimum and maximum values of the test statistic are $t _ { \mathrm { m i n } } = P _ { t } ^ { - 1 } ( p )$ and $t _ { \mathrm { m a x } } = - P _ { t } ^ { - 1 } ( p )$ . Noticing that the quantity b in Equation (4) can be written as $\begin{array} { r } { { \bf \dot { \boldsymbol { b } } } = - \frac { 1 } { 4 } \frac { t ^ { 2 } } { N } , } \end{array}$ , for any given pvalue, the corresponding minimum value of b is

$$
b _ {\mathrm{min}} = - \frac {1}{4} \frac {[ P _ {t} ^ {- 1} (p) ] ^ {2}}{N}.
$$

After calculating $a _ { \mathrm { m i n } }$ and $b _ { \mathrm { m i n } } ,$ the critical value of the HD is given by

$$
H D _ {\text { critical }} = \sqrt {1 - a _ {\min} \exp (b _ {\min})}.\tag{7}
$$

The set of critical values depends solely on the sample size, without being constrained by any specific attribute of the sample. Our identified set of critical values is not limited to particular instances and has universal applicability. Table 2 presents the numerically calculated values of $H D _ { \mathrm { c r i t i c a l } }$ for various p-values using a sample size of n $= 2 5 0 .$ . Our estimation of rejectability is conservative, as we have chosen the minimum possible values for both a and $b ,$ derived from the given p-value to evaluate the critical HD. It is noteworthy that our criteria ensure a minimal probability of committing a type I error (rejecting a true null hypothesis) while also reducing the likelihood of committing a type II error (accepting a false null hypothesis).

Table 2. Critical Values of the Hellinger Distance

<table><tr><td>p-value</td><td>0.05</td><td>0.01</td><td>0.005</td><td>0.001</td><td>0.0005</td><td>0.0001</td></tr><tr><td> $HD_{critical}$ </td><td>0.0736</td><td>0.1041</td><td>0.1152</td><td>0.1381</td><td>0.1470</td><td>0.1660</td></tr></table>

## 3.4. Value of Considering Ambiguity

Regression analysis is a fundamental and indispensable tool in the realm of empirical research, requiring careful consideration of its key assumptions. Primary assumptions related to explanatory variables include linearity, population orthogonality, and the absence of multicollinearity. Additionally, assumptions regarding error terms encompass homoskedasticity, zero conditional mean, and normal distribution. The normality assumption is needed to have unbiased estimate of standard errors, and therefore influence confidence intervals and p-values. In this paper, we argue that, in order to conduct valid empirical analysis, we must take into consideration ambiguity and measure it properly.

Consider the following regression model:

$$
\boldsymbol {Y} = \boldsymbol {X} \boldsymbol {\beta} + \epsilon .
$$

We are interested in the vector of least squares coefficients, ${ \hat { \pmb { \beta } } } ,$ which can be estimated as

$$
\hat {\pmb {\beta}} = (X ^ {\prime} X) ^ {- 1} X ^ {\prime} Y.\tag{8}
$$

In order to obtain the confidence levels of these estimators, we are also interested in the conditional variancecovariance matrix:

$$
V a r [ \hat {\pmb {\beta}} | \pmb {X} ] = \sigma^ {2} (\pmb {X ^ {\prime}} \pmb {X}) ^ {- 1},\tag{9}
$$

which can be estimated by calculating the standard errors of the regression

$$
\hat {V a r} [ \hat {\pmb {\beta}} | \pmb {X} ] = \frac {\epsilon^ {\prime} (\pmb {I} - \pmb {X} (\pmb {X} ^ {\prime} \pmb {X}) ^ {- 1} \pmb {X} ^ {\prime}) \epsilon}{n - K} (\pmb {X} ^ {\prime} \pmb {X}) ^ {- 1},
$$

where n is the number of observations, K is the number of variables, and I is an n-dimensional identity matrix.

Equation (9) relies on the existence of a static and normal variance $\sigma ^ { 2 }$ of the error term or the MLR.6 in Wooldridge (2010). That ${ \mathrm { i } } { \mathrm { s } } ,$ one implicit assumption is $E [ \epsilon \epsilon ^ { \prime } | X ] = \sigma ^ { 2 } I$ or, equivalently, $\epsilon | X \sim N [ 0 , \sigma ^ { 2 } I ]$

However, in practice, information about the distribution of observations is often limited. The CLT cannot guarantee the normality assumption if the error term is a complex function of unobserved factors or if the distribution of the error term is uncertain. Breaches of this assumption compromise the confidence in the estimators. To determine the validity of this supposition, a measure of ambiguity becomes necessary. Minimal ambiguity upholds the reliability of the conventional model, preserving confidence in our estimates. Excessive ambiguity, however, undermines the model’s trustworthiness, rendering the results unreliable, regardless of its goodness of fit.

Next, we demonstrate, through a simulation study, that when ambiguity exists but is not considered in empirical models, the results can be severely distorted.

We aim to examine the relationship between a dependent variable Y and an independent variable X over 30 years, with 250 days in each year. For each year $t ,$ we generate a random vector $X _ { t }$ of size 250, following a normal distribution $X \sim N ( 1 7 0 , 1 0 )$ , and add noise to it with a noise term vector: $\epsilon _ { t } \sim N ( 0 , 5 )$ . The dependent variable is then calculated as $Y _ { t } = 2 \times X _ { t } + \epsilon _ { t }$ . This process yields a $2 5 0 \times 3 0$ matrix, totaling $7 { , } 5 0 0$ observations over 30 years, with two columns representing the dependent and independent variables.

To introduce abnormal years with higher ambiguity, we randomly select 6 out of the 30 years and assign the noise term to follow a bimodal distribution: half of $\epsilon _ { y t } \sim$ $N ( 5 0 , 1 0 )$ ) and the other half $\epsilon _ { y t } \sim N ( - 5 0 , 1 0 )$ . This introduces ambiguity for some years without altering the mean of the observations.

Next, we assess the regression model $Y _ { t } = \boldsymbol { \beta } _ { t } \times X _ { t } + \boldsymbol { \epsilon } _ { t }$ for each year t and utilize $\epsilon _ { t }$ to calculate $H D _ { t }$ to evaluate the level of ambiguity in each year.<sup>3</sup> We designate a year as an ambiguous year if $H D _ { t }$ exceeds the critical value (0.1041 for $p { = } 0 . 0 1 )$ ).

We then examine two scenarios: (1) a naïve one without considering ambiguity, including all data up to year t in the regression for each year, and (2) a sophisticated one in which we consider ambiguity and exclude the ambigu ous years from the regressions up to year t for each year. The simulation results are shown in Figure 1.

In the upper panel of Figure 1, the lines with circles indicate naïve estimations with ambiguity, whereas the lines with squares indicate the case when ambiguous years are excluded from the estimation. The lower panel displays the estimated HD measure for each year. Years $^ { 6 , }$ 16, 18, 21, 24, and 28 exhibit significantly larger ambiguity.

From the results, we have several observations:

• Initially, when there is no ambiguity, the line with circles and the line with squares overlap, demonstrating that the calculation of ambiguity does not impact years without ambiguity.

• From year 1 to year $^ { 7 , }$ the variance decreases for both scenarios, suggesting that more data (because of cumulative regressions up to year t) can effectively reduce variance.

• The line with squares gradually converge to the true value with ${ \hat { \beta } } = \beta { \bar { = } } 2$

• The line with circles are significantly affected by ambiguity. The mean does not converge to two, and the variance remains high under the influence of ambiguity.

Figure 1. (Color online) OLS Estimation with and Without Considering Ambiguity  
![](/api/attachments/4ANN96BW/fulltext/images/d210338ffb3c04553b1b910bfce4e641de8a0a1529ea4abfe581b58c7411054f.jpg)

![](/api/attachments/4ANN96BW/fulltext/images/b9dbe84bd60f1a175bc2806f4dd67846f4a02dac993c9013207b068a9acbffd4.jpg)

Table 3 compares regression results when ambiguity is ignored versus when it is considered, using the entire 30-year sample. When ambiguity is present but overlooked, the standard error (0.027) is significantly larger than when ambiguity is explicitly considered and removed (0.006). Notably, the coefficient of 2.019 for the naïve case falls outside the 95% confidence level of the estimate derived from the ambiguity-adjusted model. Simultaneously, the $R ^ { 2 }$ value (0.941) is much higher when ambiguity is accounted for (compared with 0.428 in the other case).

The simulation results suggest that when ambiguity arises, the coefficients and confidence levels of the estimators in the regression are unreliable, regardless of the goodness of fit. In the following section, we explore ambiguity in the financial market as an illustration of the implications of ambiguity in the real world.

Table 3. Regression Results with and Without Ambiguity

<table><tr><td></td><td>Ambiguity ignored</td><td>Ambiguity considered</td></tr><tr><td> $\beta$ </td><td>2.019(0.027)[1.966, 2.072]</td><td>1.996(0.006)[1.984, 2.009]</td></tr><tr><td>Intercept</td><td>-3.337(4.586)[-12.327, 5.652]</td><td>0.683(1.096)[-1.466, 2.832]</td></tr><tr><td>Observations</td><td>7,500</td><td>6,000</td></tr><tr><td> $R^{2}$ </td><td>0.428</td><td>0.941</td></tr></table>

## 4. Application of Ambiguity

In the preceding sections, we provide definitions for uncertainty, risk, and ambiguity; introduce a quantitative measure for ambiguity; and discuss the implications of this measure. Our proposed Hellinger distance metric, distinct from traditional approaches, effectively captures distribution uncertainty, offering a more nuanced and objective evaluation. Compared with existing IS literature, our work goes beyond theoretical discussions and questionnaire-based assessments by providing a quantitative tool for measuring ambiguity. Given the constraints posed by data availability in the field of IS, we conduct an in-depth investigation into the financial market to illustrate the practical applications of our ambiguity measure in this section.

## 4.1. Market Ambiguity Trend

We apply an Autoregressive Moving Average, i.e., ARMA(1, 1) model to the daily S&P 500 return in excess of the one-month Treasury rate for HD calculation based on the residuals. On the firm level, we compute HD using the residuals from the regression of individual stock returns on the Fama and French (1992) market factor (MKT).

The computation of the ambiguity index involves historical daily returns up to time t. With 250 days representing the total number of trading days in a year, we use a normal distribution with the same mean and variance as the residuals based on 250 days of return data as the reference distribution. Because the empirical distribution is discrete and the reference distribution is continuous, we first employ kernel density estimation to smooth the empirical distribution and then use Equation (2) to calculate the HD.

Figure 2 displays a time-series plot of stock market ambiguity, quantified by the HD. The plot incorporates relevant variables, including SPRET, representing the mean of daily returns of the S&P 500 in month t; SPVOL, representing the standard deviation of daily returns of the S&P 500 in month t; and VXO, denoting the implied volatility of an option contract on the S&P 100 index.<sup>4</sup>

The top panel of Figure 2 features a horizontal dashed line indicating the critical value (corresponding to $p = 0 . 0 1 )$ of the HD. Vertical dashed lines, from left to right, mark market crashes on Black Monday in October 1987, during the Russian crisis in August 1998, the subprime crisis in October 2007, Lehman Brothers’ collapse in September 2008, the U.S. sovereign credit degradation in August 2011, the Russian financial crisis in December 2014, the market crisis in February 2018, and the COVID-19 pandemic in February 2020.

Figure 2 reveals that the null hypothesis cannot be rejected at the 1% level for more than half of the time, as HD values consistently remain below the critical value. This implies that the empirical distribution of return residuals closely aligns with a normal distribution. However, it is crucial to note periods where the null hypothesis can be rejected, indicating a deviation from normality.

The analysis underscores the relationship between the HD, VIX, SPVOL, and SPRET with market crashes. The HD experiences a noticeable decline, crossing the p � 0.01 line preceding each market crash. This decline is coupled with an upswing in VIX and SPVOL, alongside a sharp ascent in HD during the crash. This pattern suggests an opportunity to leverage two HD peaks, accompanied by a VIX surge, as leading indicators of market crashes. The findings propose that the HD might possess stronger forward-looking properties compared with the widely accepted VIX.

It is crucial to emphasize that a decline in HD after the initial peak does not necessarily signify a return of the distribution to fundamental levels. Instead, it serves as a critical warning sign of an impending financial crisis. In the Online Appendix, Section A, we present model-free evidence illustrating how the trend of HD can provide signals of market crashes.

## 4.2. Ambiguity and Crash Risk

So far, our findings suggest that employing the ambiguity measure can provide insightful warning signals for market crashes. Nonetheless, because of the infrequency of market crash events, relying solely on regression models to analyze the correlation between market crashes and the ambiguity measure may not be entirely reliable. To further demonstrate the ambiguity measure’s potential, we use regression models to examine its value in indicating individual stock crash risks.

Figure 2. (Color online) Time-Series Plot of Stock Market Ambiguity and Crash Events  
![](/api/attachments/4ANN96BW/fulltext/images/0878a36314d4e9e16f892b0cc17cea921d692fe24386981593840a9518530eac.jpg)

4.2.1. Variable Definition. We first calculate the HD for each firm in each year. Similar to the market HD, we use returns from the 250 days leading up to the end of year t for each individual firm. To ensure an appropriate reference distribution, we compute the HD based on the residual of a regression model:

$$
R _ {i, d} - R _ {f, d} = \alpha_ {i} + \beta_ {i} M K T _ {d} + \varepsilon_ {i, d}.
$$

The dependent variable is the daily return in excess of the one-month Treasury rate for firm i in day $d ,$ and MKT is the Fama and French (1992) market factor. We then use the Equation (2) to calculate $H D _ { i , t }$ based on the daily $\varepsilon _ { i , d } .$

As discussed by Chen et al. (2001), the negative coefficient of skewness (NCSKEW) serves as a proxy for measuring the occurrence of financial crashes. Additionally, the concept of conditional skewness has been used in prior literature to both represent the likelihood of a financial crash occurring via crash expectation measurements (Bates 1991) and to assess the possibility of stock price crashes as a measure of crash risk (Kim et al. 2011). For stocks, the calculation of conditional skewness (NCSKEW) is conducted on a yearly basis using daily returns data:

$$
N C S K E W _ {i, t} = - \frac {n (n - 1) ^ {3 / 2} \sum R _ {i , t , d} ^ {3}}{(n - 1) (n - 2) \left(\sum R _ {i , t , d} ^ {2}\right) ^ {3 / 2}},
$$

where $R _ { i , t , d }$ is demeaned daily returns for firm i during year $t ,$ and n is the number of observations on daily returns during the period. The minus sign implies that an increase in NCSKEW corresponds to a firm being more “crash prone” or having a more left-skewed distribution.

We also employ the “down-to-up volatility” (DUVOL) measure, originally introduced by Chen et al. (2001). This metric enables the analysis of a specific firm’s behavior by distinguishing days with returns below the period mean $\mathrm { ( i . e . , ~ \mathrm { ^ { \prime \prime } D O W N ^ { \prime \prime } ~ d a y s ) } }$ from those with returns above the period mean $( \mathrm { i . e . , \Omega ^ { \prime \prime } U P ^ { \prime \prime } }$ days). We compute the standard deviation separately for both subsamples of data and obtain the logarithmic ratio of the sample analog for the standard deviation of the down days to the sample analog for the standard deviation of the up days. This measure captures the behavior of the financial asset concerning its volatility and the directional trend of the returns observed during the specified time period. Thus,

the DUVOL is calculated as

$$
D U V O L _ {i, t} = \log \left(\frac {(n _ {u} - 1) \sum_ {D O W N} R _ {i , t , d} ^ {2}}{(n _ {d} - 1) \sum_ {U P} R _ {i , t , d} ^ {2}}\right),
$$

where $n _ { u }$ and $n _ { d }$ are the numbers of UP and DOWN days, respectively.

Next, we use the HD to investigate the crashes through the regression model

$$
\begin{array}{r} C R A S H _ {i, t + 1} = \alpha + \beta_ {1} H D _ {i, t} + \beta_ {2} C R A S H _ {i, t} + \beta C o n t r o l _ {i, t} \\ + Y e a r _ {t} + F i r m _ {i} + \varepsilon_ {i, t}. \end{array}\tag{10}
$$

The dependent variable $C R A S H _ { i , t }$ represents $N C S K E W _ { i , t }$ or $D U \bar { V } O L _ { i , t }$ for firm i during year t. The independent variable of interest is the ambiguity measure (HD). In accordance with Chen et al. (2001), we also incorporate several control variables: VOL, the standard deviation of the excess daily returns during the period; RET, the yearly return; SIZE, the logarithm of the firm’s market value; BM, the book-to-market ratio; LEV, the leverage; ROA, the return on assets; COVER, the logarithm of one plus the number of analysts (Institutional Brokers’ Estimate System); and VOLEPS, the standard deviation of the forecast EPS by the analysts. Terms Year and Firm indicate the year and firm fixed effects, respectively.

4.2.2. Empirical Results. The daily stock files were obtained from the Center for Research in Security Prices, whereas the annual accounting data are from Compustat. The sample encompasses all NYSE, AMEX, and NASDAQ firms with common shares. We exclude firms with insufficient or missing data and require each firm to have a minimum of 100 daily transactions per year. Furthermore, we exclude companies with less than 10 years of available data, resulting in a final sample of 74,294 firm-year observations for 4,064 entities spanning from 1983 to 2020.

Descriptive statistics for the variables are displayed in panel A of Table 4. Specifically, the mean (median) values for NCSKEW and DUVOL are �0.33 (�0.29) and �0.28 (�0.28), respectively. On average, the HD has a value of 0.11 with a standard deviation of 0.06. The median value of the HD (0.10) reveals that the nul hypothesis, asserting that the empirical distribution is identical to the normal distribution, cannot be rejected at the 1% level for at least half of the firm-year observations. This supports the notion that the empirical distribution of return residuals closely aligns with a normal distribution, as assumed by MLR.6 in Wooldridge (2010). The estimations for other variables align with the existing literature, indicating the dependability of our sample.

Panel B of Table 4 reveals that NCSKEW and DUVOL exhibit a high correlation of 92%, as both function as proxies for firm-level crashes. The crash measures display a negative correlation with the HD, at �0.09 and �0.11 for NCSKEW and DUVOL, respectively. During a given year, firms with a higher HD tend to be less likely to experience crashes or possess a distribution that is less skewed to the left. The correlation between the HD and other control variables remains moderate. Notably, the correlation between the HD and VIX is 0.27, which is reasonable, considering that the VIX contains information about both risk and ambiguity, whereas the HD specifically represents ambiguity. The negative relationship between the HD and SIZE implies that smaller firms are more likely to be ambiguous to investors. Additionally, in line with Anderson et al. (2009), who propose using professional forecaster disagreement levels as a proxy for uncertainty, we investigate analyst disagreement levels represented by VOLEPS as an alternative proxy for ambiguity. Our findings indicate that the HD is positively associated with VOLEPS, exhibiting a correlation of merely 4%.

<table><tr><td colspan="11">Panel A. Summary statistics</td></tr><tr><td colspan="2">Variable</td><td>Mean</td><td colspan="2">Median</td><td colspan="2">Minimum</td><td colspan="2">Maximum</td><td colspan="2">Std. dev.</td></tr><tr><td colspan="2">NCSKEW</td><td>-0.33</td><td colspan="2">-0.29</td><td colspan="2">-15.42</td><td colspan="2">12.18</td><td colspan="2">1.41</td></tr><tr><td colspan="2">DUVOL</td><td>-0.28</td><td colspan="2">-0.28</td><td colspan="2">-6.18</td><td colspan="2">3.45</td><td colspan="2">0.61</td></tr><tr><td colspan="2">HD</td><td>0.11</td><td colspan="2">0.10</td><td colspan="2">0.03</td><td colspan="2">0.66</td><td colspan="2">0.06</td></tr><tr><td colspan="2">VOL</td><td>2.79</td><td colspan="2">2.40</td><td colspan="2">0.33</td><td colspan="2">40.55</td><td colspan="2">1.59</td></tr><tr><td colspan="2">RET</td><td>0.14</td><td colspan="2">0.07</td><td colspan="2">-1.00</td><td colspan="2">24.99</td><td colspan="2">0.64</td></tr><tr><td colspan="2">SIZE</td><td>6.55</td><td colspan="2">6.45</td><td colspan="2">-0.69</td><td colspan="2">14.49</td><td colspan="2">1.88</td></tr><tr><td colspan="2">BM</td><td>0.66</td><td colspan="2">0.54</td><td colspan="2">0.00</td><td colspan="2">39.78</td><td colspan="2">0.59</td></tr><tr><td colspan="2">LEV</td><td>6.07</td><td colspan="2">6.06</td><td colspan="2">-3.04</td><td colspan="2">14.70</td><td colspan="2">2.36</td></tr><tr><td colspan="2">ROA</td><td>0.11</td><td colspan="2">0.12</td><td colspan="2">-2.35</td><td colspan="2">1.37</td><td colspan="2">0.15</td></tr><tr><td colspan="2">COVER</td><td>3.16</td><td colspan="2">3.22</td><td colspan="2">0.69</td><td colspan="2">6.08</td><td colspan="2">1.08</td></tr><tr><td colspan="2">VOLEPS</td><td>0.58</td><td colspan="2">0.10</td><td colspan="2">0.00</td><td colspan="2">107.53</td><td colspan="2">3.88</td></tr><tr><td colspan="11">Panel B. Correlations</td></tr><tr><td></td><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td></tr><tr><td>(1)</td><td>NCSKEW</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(2)</td><td>DUVOL</td><td>0.92</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(3)</td><td>HD</td><td>-0.09</td><td>-0.11</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(4)</td><td>VOL</td><td>-0.11</td><td>-0.17</td><td>0.27</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(5)</td><td>RET</td><td>0.05</td><td>0.05</td><td>-0.02</td><td>0.03</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>(6)</td><td>SIZE</td><td>0.10</td><td>0.16</td><td>-0.18</td><td>-0.39</td><td>-0.08</td><td>1</td><td></td><td></td><td></td></tr><tr><td>(7)</td><td>BM</td><td>-0.05</td><td>-0.06</td><td>0.06</td><td>0.13</td><td>0.12</td><td>-0.27</td><td>1</td><td></td><td></td></tr><tr><td>(8)</td><td>LEV</td><td>0.07</td><td>0.12</td><td>-0.15</td><td>-0.40</td><td>-0.05</td><td>0.77</td><td>0.10</td><td>1</td><td></td></tr><tr><td>(9)</td><td>ROA</td><td>0.10</td><td>0.13</td><td>-0.09</td><td>-0.29</td><td>-0.01</td><td>0.23</td><td>-0.14</td><td>0.07</td><td>1</td></tr><tr><td>(10)</td><td>COVER</td><td>0.07</td><td>0.11</td><td>-0.15</td><td>-0.22</td><td>-0.06</td><td>0.74</td><td>-0.15</td><td>0.57</td><td>0.19</td></tr><tr><td>(11)</td><td>VOLEPS</td><td>-0.03</td><td>-0.04</td><td>0.04</td><td>0.15</td><td>-0.05</td><td>-0.04</td><td>0.05</td><td>-0.03</td><td>-0.18</td></tr></table>

Table 4. Summary Statistics and Correlations Among the Firm-Level Variables  
Note. Std. dev., standard deviation.

As argued by Chen et al. (2001), corporate managers have discretion over information disclosure and are incentivized to strategically withhold negative information while hastening the release of positive information. This asymmetric disclosure behavior results in a degree of positive skewness in returns. If a firm exhibits greater ambiguity or opaqueness, managers are more inclined to adopt this disclosure strategy, leading to a more pronounced positive-skewness effect and a smaller NCSKEW. Consequently, we anticipate the ambiguity measure to exhibit a negative association with stock crashes (NCSKEW), and the regression coefficients of the HD should be negative.

Table 5 presents the regression results for firm-level crash risk considering HD and control variables. In Model (1), which solely incorporates HD, the coefficient is �2.49 with a statistically significant t-statistic of �25.83 (p < 0.01). The negative coefficient on HD persists in Model (2) with the inclusion of control variables, and the effects of these control variables align with Chen et al. (2001). Another ambiguity measure, VOLEPS, also shows a negative impact on crashes, albeit with a comparatively weak significance level. Model (3) includes fixed effects and adjusts the t-statistics using robust standard errors clustered at the firm level; how ever, the negative coefficient of HD remains signifi cant at the 1% level. The regression results for Models (4) through (6), utilizing DUVOL as a proxy for firm-

To address concerns about the time horizon of crash risk measures, we calculate NCSKEW using monthly, quarterly, and semiannual data. Additionally, we investigate whether the ambiguity measure can serve as an early warning indicator for predicted crash risks across various time frames. Unreported results from our analysis indicate that, even after adjusting for control variables, fixed effects, and t-statistics, the coefficients of HD consistently exhibit a negative and statistically significant relationship at the 1% level for all crashes estimated within distinct time periods. These findings suggest that ambiguity exerts a pervasive and stable influence on firm-level crashes.

Table 5. Ambiguity and Firm-Level Crash Risks

<table><tr><td rowspan="2"></td><td colspan="3"> $NCSKEW_{t+1}$ </td><td colspan="3"> $DUVOL_{t+1}$ </td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td> $HD_t$ </td><td>-2.49***(-25.83)</td><td>-1.33***(-12.77)</td><td>-1.35***(-9.57)</td><td>-1.33***(-32.05)</td><td>-0.58***(-13.11)</td><td>-0.64***(-9.50)</td></tr><tr><td>Constant</td><td>-0.12***(-9.34)</td><td>-0.39***(-11.53)</td><td>-0.39***(-6.28)</td><td>-0.15***(-28.69)</td><td>-0.32***(-22.15)</td><td>-0.51***(-17.72)</td></tr><tr><td>Controls</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>FEs (year and firm)</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Cluster (firm)</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Observations</td><td>74,294</td><td>74,294</td><td>74,294</td><td>74,294</td><td>74,294</td><td>74,294</td></tr><tr><td> $R^2$ </td><td>0.009</td><td>0.031</td><td>0.017</td><td>0.013</td><td>0.057</td><td>0.032</td></tr></table>

Note. FEs, fixed effects.  
\*\*\*p < 0.01.

To further explore the impact of the HD on firm-level crash risks, we examine the effect of the HD on firms with varying degrees of information asymmetry. Typically, firms are considered opaque when characterized by small market sizes, low liquidity, or low institutional ownership (IO). These opaque firms are expected to be more uncertain to investors, displaying a higher level of ambiguity. However, the sensitivity of crash risk to ambiguity for opaque firms remains unexplored.

Table 6 presents regression results for firms’ crashes (NCSKEW) on HD and its interaction with a dummy variable. This dummy variable takes a value of one if the firm exhibits small size, low liquidity, or low IO based on median values for each month. Our findings reveal that the coefficients of HD are significant and negative, consistent with previous results. Conversely, the interaction term is significantly positive, indicating that HD exhibits a weaker effect on crash risks for opaque firms (i.e., small size, low liquidity, or low IO). Specifically, in Model (1), the coefficients of HD are �2.62 and �1.51 (� �2:62 + 1:11) for large and small firms, respectively. This suggests that crash risk sensitivity to ambiguity is heightened for larger firms compared with smaller ones. Moreover, analogous results are observed for firms with high liquidity or IO.

Our results indicate that opaque firms have lower NCSKEW, consistent with Chen et al. (2001), where managers from opaque firms may face less scrutiny from security analysts, leading to a more pronounced positive-skewness effect. In contrast, managers who face greater scrutiny are less likely to adopt information disclosure strategies until the firms become more ambiguous. An increase in the degree of ambiguity leads to a larger positive-skewness effect in transparent firms compared with opaque firms. The coefficients of the interaction items are significantly positive, suggesting that the NCSKEW of transparent firms is more sensitive to HD than that of opaque firms.

Table 6. Ambiguity and Information Asymmetry

<table><tr><td rowspan="2"></td><td colspan="2">Small size</td><td colspan="2">Low liquidity</td><td colspan="2">Low IO</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>HD</td><td>-2.62***(-9.98)</td><td>-2.05***(-7.91)</td><td>-2.54***(-10.02)</td><td>-1.88***(-7.52)</td><td>-3.10***(-9.00)</td><td>-2.70***(-7.85)</td></tr><tr><td>HD × Dummy</td><td>1.11***(3.60)</td><td>1.16***(3.73)</td><td>0.95***(3.16)</td><td>0.89***(2.92)</td><td>1.16***(2.65)</td><td>1.08**(2.42)</td></tr><tr><td>Dummy</td><td>-0.33***(-8.79)</td><td>-0.22***(-5.58)</td><td>-0.32***(-8.82)</td><td>-0.24***(-6.47)</td><td>-0.19***(-3.87)</td><td>-0.15***(-3.02)</td></tr><tr><td>Constant</td><td>-0.00(-0.14)</td><td>-0.20***(-2.73)</td><td>-0.01(-0.37)</td><td>-0.13*(-1.82)</td><td>-0.03(-0.88)</td><td>-0.50***(-5.04)</td></tr><tr><td>Controls</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>FEs (year and firm)</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Cluster (firm)</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>74,213</td><td>74,213</td><td>74,213</td><td>74,213</td><td>52,034</td><td>50,940</td></tr><tr><td> $R^2$ </td><td>0.007</td><td>0.017</td><td>0.007</td><td>0.018</td><td>0.006</td><td>0.017</td></tr></table>

Note. FEs, fixed effects.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

Table 7. Comparison Between HD and Other Ambiguity Measures

<table><tr><td rowspan="2"></td><td colspan="5"> $NCSKEW_{t+1}$ </td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td> $HD_t$ </td><td>-2.07***(-9.65)</td><td></td><td></td><td></td><td>-1.67***(-7.77)</td></tr><tr><td> $HDSP_t$ </td><td></td><td>-2.67***(-10.74)</td><td></td><td></td><td>-1.70***(-6.29)</td></tr><tr><td> $VIX_t$ </td><td></td><td></td><td>1.24***(8.34)</td><td></td><td>0.20(1.17)</td></tr><tr><td> $\mathcal{U}_t$  (mho)</td><td></td><td></td><td></td><td>-4.23***(-12.48)</td><td>-2.78***(-6.46)</td></tr><tr><td>Constant</td><td>-0.77***(-9.15)</td><td>-0.89***(-10.75)</td><td>-0.97***(-11.69)</td><td>-1.10***(-12.75)</td><td>-1.02***(-11.62)</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>FEs (year and firm)</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Cluster (firm)</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>54,257</td><td>54,257</td><td>54,257</td><td>54,257</td><td>54,257</td></tr><tr><td> $R^2$ </td><td>0.019</td><td>0.018</td><td>0.017</td><td>0.018</td><td>0.022</td></tr></table>

Note. FEs, fixed effects.  
\*\*\*p < 0.01.

Next, we compare various measures of firm-level and market-level HD in predicting the risks of market crashes. Specifically, we compare the firm-level HD with the market-level HD (HDSP), VIX, and Brenner and Izhakian (2018) f (mho).<sup>6</sup> Measure HDSP is computed based on the S&P 500 index, as illustrated in Figure 2. To match firm-year observations, we derive the yearly average of the remaining ambiguity measures.

Table 7 show that all ambiguity measures are significant at the 1% level when included alone, with negative coefficients, except for the VIX. The R<sup>2</sup> values reveal that the HD has a slightly higher value than the other measures in capturing crash risks, indicating that the HD contains more explanatory power than other measures. Interestingly, all ambiguity measures, except for the VIX, remain significant when incorporated into a unified regression analysis in column (5). Compared with the other measures, the HD exhibits a comparatively lower percentage drop of 19% from 2.07 to 1.67 in coefficient estimates, whereas other measures drop more than 34%, implying that the HD is more informative in predicting crash risks. As such, our results suggest that the HD has greater power in predicting market crashes than other ambiguity measures.

In summary, we investigate the implications and applications of ambiguity in the financial market as an illustration. The aforementioned findings underscore the significance of the ambiguity measure in providing insights into crash risks at the firm level. Firms demonstrating higher ambiguity measures typically exhibit less negative skewness, implying a decreased probability of encountering a crash. Managers of high-ambiguity companies tend to adopt an asymmetric disclosure strategy, characterized by withholding negative news while disseminating positive news. This approach results in a more pronounced positive-skewness effect (smaller NCSKEW) or diminished crash-proneness. In the Online Appendix, Section B, we further investigate the effect of ambiguity on country-level crash risk and find conclusions similar to those from the firm-level tests.

## 5. Conclusion

The measure presented in this paper makes contributions to the understanding and measurement of distribution uncertainty. First, we emphasize the importance of considering distribution uncertainty, in addition to outcome uncertainty, highlighting the negative consequences of not doing so. Second, prior works on ambiguity mostly examine subjective ambiguity aversion, but we distinguish objective ambiguity and focus on the examination of measuring it. Third, we propose a measure of distribution uncertainty that can be used in empirical research. This measure specifically targets the limitations of existing measures, such as volatility or entropy, by emphasizing incremental information derived from distribution uncertainty.

One key contribution of this study is the demonstration of the properties and advantages of the HD measure. It enhances the accuracy and utility of existing data analytics models by providing a more comprehen sive assessment of uncertainty. By incorporating the HD measure into data analysis frameworks, researchers and practitioners can obtain more reliable parameter estimates, leading to improved predictive models and more informed decision-making processes. This is particularly valuable in domains where uncertainty plays a crucial role, such as finance, where the ability to accurately assess and manage distribution uncertainty can significantly impact risk management strategies and investment decisions. Furthermore, the study goes beyond theoretical implications by providing practical applications of the HD measure. Through an extensive empirical analysis, this paper showcases the HD measure’s ability to offer new information and serve as a valuable predictor of market crashes. This empirical evidence demonstrates the real-world implications and predictive power of the HD measure, highlighting its potential as a practical tool for risk management and decision support.

Overall, this research contributes to a deeper understanding of ambiguity in empirical research and offers valuable insights for both research methodologies and practical risk management. By introducing the HD measure, the study addresses the need for reliable and robust measures to effectively capture and quantify distribution uncertainty. The implications of this work likely extend to various other domains and disciplines, providing researchers and practitioners with a powerful tool to enhance their data analysis models, improve decision-making processes, and mitigate the impact of uncertainty in their respective fields.

One limitation of this work is that this paper focuses on a specific reference distribution of the measure. Future work could examine other types of reference distributions in other contexts. Incorporating a comparative analysis of multiple reference distributions would provide a more comprehensive understanding of their strengths and weaknesses. Additionally, this paper primarily focuses on quantitative measures of ambiguity and does not extensively address qualitative aspects or subjective perceptions of ambiguity. Incorporating qualitative research methods, especially those already extensively used in the literature, could provide valuable insights into individuals’ subjective perception of ambiguity and its impact on decision making.

Furthermore, although this paper highlights the practical applications of the HD measure in enhancing data analysis models and decision-making processes, it does not address potential challenges or limitations in implementing these applications. Future research could explore the practical feasibility and scalability of incorporating ambiguity measures in real-world scenarios, considering factors such as data availability, computational complexity, and interpretability of results. Additionally, this paper primarily emphasizes the role of ambiguity in the financial market, leaving room for investigation in other domains, such as supply chain management, marketing, or social sciences. Exploring the applicability and effectiveness of ambiguity measures in these different contexts would broaden the scope and relevance of the research.

In terms of future directions, it would be valuable to investigate the dynamic nature of ambiguity and its implications over time. Understanding how ambiguity evolves, how it interacts with other factors such as market conditions or external events, and how it influences decision-making dynamics would provide deeper insights into its multifaceted nature. Additionally, fur ther exploring the potential synergies between ambiguity measures and other uncertainty-related concepts, such as risk measures or information entropy, could lead to a more comprehensive framework for capturing and managing uncertainty. Moreover, considering the rapid advancements in technology and data analytics, future research could explore the integration of machine learning and artificial intelligence techniques in ambiguity measurement and analysis, enabling more sophisticated and accurate assessments of distribution uncertainty. Overall, these future directions would contribute to a more nuanced understanding of ambiguity and its implications across various domains and facilitate the development of practical tools and frameworks for decision makers to navigate uncertainty effectively.

## Acknowledgments

This work was supported by the Research Grants Council, University Grants Committee [GRF 14504524, 14500521, 14501320]. The authors thank James Zhan of Super Quantum Fund and Yuriy Nevmyvaka of Morgan Stanley for stimulating discussions.

## Endnotes

<sup>1</sup> To put this into perspective, the estimated number of atoms in the observable universe is about 10<sup>80</sup> (Barrow 2002).

<sup>2</sup> Both conditions are automatically satisfied by construction of the HD measure.

<sup>3</sup> Because of the simplicity of the simulation assumptions, we can also calculate the ambiguity measure across years to obtain the same result.

<sup>4</sup> Note that CBOE constructs the VIX index based on the S&P 500 for a broader range of strike prices, whereas we use VXO because of real-time availability since 1986. Additionally, VXO and VIX are highly correlated, and we treat them interchangeably hereafter.

<sup>5</sup> Because of the high correlation between NCSKEW and DUVOL, our results remain consistent for both crash measures. In subsequent analyses, we omit the results of DUVOL for brevity.

<sup>6</sup> We are grateful to Yehuda (Yud) Izhakian for sharing the data.

## References

Abdellaoui M, Vossmann F, Weber M (2005) Choice-based elicitation and decomposition of decision weights for gains and losse under uncertainty. Management Sci. 51(9):1384–1399.

Abdellaoui M, Baillon A, Placido L, Wakker PP (2011) The rich domain of uncertainty: Source functions and their experimental implementation. Amer. Econom. Rev. 101(2):695–723.

Abdellaoui M, Bleichrodt H, Kemel E, l’Haridon O (2021) Measur ing beliefs under ambiguity. Oper. Res. 69(2):599–612.

Al-Natour S, Cavusoglu H, Benbasat I, Aleem U (2020) An empirical investigation of the antecedents and consequences of privacy

uncertainty in the context of mobile apps. Inform. Systems Res. 31(4):1037–1063.

Amzal B, Bois FY, Parent E, Robert CP (2006) Bayesian-optimal design via interacting particle systems. J. Amer. Statist. Assoc. 101(474):773–785.

Anderson EW, Ghysels E, Juergens JL (2009) The impact of risk and uncertainty on expected returns. J. Financial Econom. 94(2): 233–263.

Arrow KJ (1963) Uncertainty and the welfare economics of medical care. Amer. Econom. Rev. 53(5):941–973.

Augustin P, Izhakian Y (2020) Ambiguity, volatility, and credit risk. Rev. Financial Stud. 33(4):1618–1672.

Ayyagari R, Grover V, Purvis R (2011) Technostress: Technological antecedents and implications. MIS Quart. 35(4):831–858.

Bapna R, Ramaprasad J, Shmueli G, Umyarov A (2016) One-way mirrors in online dating: A randomized field experiment. Man agement Sci. 62(11):3100–3122.

Barclay MJ, Hendershott T, McCormick DT (2003) Competition among trading venues: Information and trading on electronic communications networks. J. Finance 18(6):2637–2665.

Barro RJ (2006) Rare disasters and asset markets in the twentieth century. Quart. J. Econom. 121(3):823–866.

Barro RJ (2009) Rare disasters, asset prices, and welfare costs. Amer. Econom. Rev. 99(1):243–264.

Barrow J (2002) The Constants of Nature from Alpha to Omega: The Numbers That Encode the Deepest Secrets of the Universe (Pantheon Books, New York).

Bates DS (1991) The crash of ‘87: Was it expected? The evidence from options markets. J. Finance 46(3):1009–1044.

Benaroch M (2018) Real options models for proactive uncertainty reducing mitigations and applications in cybersecurity investment decision making. Inform. Systems Res. 29(2):315–340.

Black F, Scholes M (1973) The pricing of options and corporate liabilities. J. Political Econom. 81(3):637–654.

Brenner M, Izhakian Y (2018) Asset pricing and ambiguity: Empiri cal evidence. J. Financial Econom. 130(3):503–531.

Brynjolfsson E, Smith MD (2000) Frictionless commerce? A comparison of internet and conventional retailers. Management Sci. 46(4):563–585.

Brynjolfsson E, Wang A, Zhang XM (2021) The economics of IT and digitization: Eight questions for research. MIS Quart. 45(1): 473–477.

Camerer C, Weber M (1992) Recent developments in modeling preferences: Uncertainty and ambiguity. J. Risk Uncertainty 5(4): 325–370.

Chen J, Hong H, Stein JC (2001) Forecasting crashes: Trading volume, past returns, and conditional skewness in stock prices. J. Financial Econom. 61(3):345–381.

Chen P, Hitt LM, Hong Y, Wu S (2021) Measuring product type and purchase uncertainty with online product ratings: A theoretical model and empirical application. Inform. Systems Res. 32(4):1470–1489.

Chung S, Animesh A, Han K, Pinsonneault A (2019) Software patents and firm value: A real options perspective on the role of innovation orientation and environmental uncertainty. Inform. Systems Res. 30(3):1073–1097.

Clemons EK, Weber BW (1996) Alternative securities trading systems: Tests and regulatory implications of the adoption of tech nology. Inform. Systems Res. 7(2):163–188.

Clemons EK, Weber BW (1997) Information technology and screenbased securities trading: Pricing the stock and pricing the trade. Management Sci. 43(12):1693–1708.

Csisza´r I (1967) Information-type measures of difference of probability distributions and indirect observation. Studia Scientiarum Mathematicarum Hungarica 2:299–318.

Dellarocas C, Zhang XM, Awad NF (2007) Exploring the value of online product reviews in forecasting sales: The case of motion pictures. J. Interactive Marketing 21(4):2–20.

Dimoka A, Hong Y, Pavlou PA (2012) On product uncertainty in online markets: Theory and evidence. MIS Quart. 36(2):395–426.

Du X, Su M, Zhang XM, Zheng X (2017) Bidding for multiple keywords in sponsored search advertising: Keyword categorie and match types. Inform. Systems Res. 28(4):711–722.

Duncan RB (1972) Characteristics of organizational environments and perceived environmental uncertainty. Admin. Sci. Quart. 17(3):313–327.

Ellsberg D (1961) Risk, ambiguity, and the savage axioms. Quart. J. Econom. 75(4):643–669.

Epstein LG, Zhang J (2001) Subjective probabilities on subjectively unambiguous events. Econometrica 69(2):265–306.

Fama E, French KR (1992) The cross-section of expected stock returns. J. Finance 47(2):427–465.

Fang Z, Ho YC, Tan JX, Tan Y (2021) Show me the money: The economic impact of membership free shipping programs on online retailers. Inform. Systems Res. 32(4):1115–1127.

Gabaix X, Gopikrishnan P, Plerou V, Stanley HE (2003) A theory of power-law distributions in financial market fluctuations. Nature 423(6937):267–270.

Gao G, Greenwood BN, McCullough JS, Agarwal R (2015) Vocal minority and silent majority: How do online ratings reflect pop ulation perceptions of quality? MIS Quart. 39(3):565–589.

Ghose A (2009) Internet exchanges for used goods: An empirical analysis of trade patterns and adverse selection. MIS Quart. 33(2):263–291.

Gibbs AL, Su FE (2002) On choosing and bounding probability metrics. Internat. Statist. Rev. 70(3):419–435.

Gilboa I, Schmeidler D (1989) Maxmin expected utility with non unique prior. J. Math. Econom. 18(2):141–153.

Gong J, Abhishek V, Li B (2018) Examining the impact of keyword ambiguity on search advertising performance: A topic model approach. MIS Quart. 42(3):805–829.

Hansen LP, Sargent TJ (2001) Robust control and model uncertainty. Amer. Econom. Rev. 91(2):60–66.

Hellinger E (1909) Neue Begru¨ ndung der Theorie quadratischer Formen von unendlichvielen Vera¨nderlichen. J. Reine Angewandte Mathematik 136:210–271.

Hendershott T, Zhang XM, Zhao JL, Zheng ZE (2021) Fintech as a game changer: Overview of research frontiers. Inform. Systems Res. 32(1):1–17.

Hong Y, Pavlou PA (2014) Product fit uncertainty in online markets: Nature, effects, and antecedents. Inform. Systems Res. 25(2): 328–344.

Hu M, Li X, Shi Y, Zhang XM (2023) Numerological heuristics and credit risk in peer-to-peer lending. Inform. Systems Res. 34(4): 1744-1760

Izhakian Y, Yermack D, Zender JF (2022) Ambiguity and the tradeoff theory of capital structure. Management Sci. 68(6):4090–4111.

Jiang ZJ, Benbasat I (2007) The effects of presentation formats and task complexity on online consumers’ product understanding MIS Quart. 31(3):475–500.

Jiang Y, Ho YC, Yan X, Tan Y (2022) What’s in a “username”? Examining the effect of perceived anonymity on herding in online crowdfunding. Inform. Systems Res. 33(1):1–17.

Karimi J, Somers TM, Gupta YP (2004) Impact of environmental uncertainty and task characteristics on user satisfaction with data. Inform. Systems Res. 15(2):175–193.

Kim Y, Krishnan R (2015) On product-level uncertainty and online purchase behavior: An empirical analysis. Management Sci. 61(10):2449–2467.

Kim JB, Li Y, Zhang L (2011) Corporate tax avoidance and stock price crash risk: Firm-level analysis. J. Financial Econom. 100(3): 639–662.

Kim K, Park J, Pan Y, Zhang K, Zhang X (2022) Risk disclosure in crowdfunding. Inform. Systems Res. 33(3):1023–1041.

Klibanoff P, Marinacci M, Mukerji S (2005) A smooth model of deci sion making under ambiguity. Econometrica 73(6):1849–1892.

Knight FH (1921) Risk, Uncertainty and Profit (Houghton Mifflin, Boston).

Li Z, Mu¨ ller J, Wakker PP, Wang TV (2018) The rich domain of ambiguity explored. Management Sci. 64(7):3227–3240.

Lu T, Yuan M, Wang CA, Zhang XM (2022) Histogram distortion bias in consumer choices. Management Sci. 68(12):8963–8978.

Maafi H (2011) Preference reversals under ambiguity. Management Sci. 57(11):2054–2066.

Mandelbrot B (1963) The variation of certain speculative prices. J. Bus. 36(4):394–419.

Miao J, Wei B, Zhou H (2019) Ambiguity aversion and the variance premium. Quart. J. Finance 9(02):1950003.

Mishra DP, Heide JB, Cort SG (1998) Information asymmetry and levels of agency relationships. J. Marketing Res. 35(3): 277–295.

Nelson P (1970) Information and consumer behavior. J. Political Econom. 78(2):311–329.

Olszewski W (2007) Preferences over sets of lotteries. Rev. Econom. Stud. 74(2):567–595.

Pavlou PA, Liang H, Xue Y (2007) Understanding and mitigating uncertainty in online exchange relationships: A principal-agent perspective. MIS Quart. 31(1):105–136.

Pedersen LH (2019) Efficiently Inefficient: How Smart Money Invests and Market Prices are Determined (Princeton University Press, Princeton, NJ).

Ply JK, Moore JE, Williams CK, Thatcher JB (2012) IS employee atti tudes and perceptions at varying levels of software process maturity. MIS Quart. 36(2):601–624.

Rishika R, Ramaprasad J (2019) The effects of asymmetric social ties, structural embeddedness, and tie strength on online content contribution behavior. Management Sci. 65(7):3398–3422.

Rizzo JR, House RJ, Lirtzman SI (1970) Role conflict and ambiguity in complex organizations. Admin. Sci. Quart. 15(2):150–163.

Savage LJ (1954) The Foundations of Statistics (Wiley, New York).

Schmidt AF, Finan C (2018) Linear regression and the normality assumption. J. Clinical Epidemiology 98:146–151.

Schrader S, Riggs WM, Smith RP (1993) Choice over uncertainty and ambiguity in technical problem solving. J. Engrg. Tech. Management 10(1–2):73–99.

Shen H, Dang I, Zhang XM (2024) Mr. Right or Mr. Best: The role of information under preference mismatch in online dating Inform. Systems Res., ePub ahead of print March 13, https://doi org/10.1287/isre.2022.0233.

Shiller RJ (1987) The volatility of stock market prices. Science 235(4784):33–37.

Uppal R, Wang T (2003) Model misspecification and underdiversification. J. Finance 58(6):2465–2486.

Van De Kuilen G, Wakker PP (2011) The midweight method to measure attitudes toward risk and ambiguity. Management Sci. 57(3):582–598

Wang A, Zhang XM (2009) Sampling of information goods. Decision Support Systems 48(1):14–22.

Williams CD (2015) Asymmetric responses to earnings news: A case for ambiguity. Accounting Rev. 90(2):785–817.

Wooldridge JM (2010) Econometric Analysis of Cross Section and Panel Data (MIT Press, Cambridge, MA)

Wooldridge JM (2012) Introductory Econometrics: A Modern Approach, 5th ed. (Cengage Learning, Boston).

Xu SX, Zhang XM (2013) Impact of Wikipedia on market information environment: Evidence on management disclosure and investor reaction. MIS Quart. 37(4):1043–1068.

Zhang J (2002) Subjective ambiguity, expected utility and Choquet expected utility. Econom. Theory 20(1):159–181.

Zhang XM, Feng J (2011) Cyclical bid adjustments in search-engine advertising. Management Sci. 57(9):1703–1719.

Zhang XM, Zhang L (2015) How does the internet affect the financial market? An equilibrium model of internet facilitated feed back trading. MIS Quart. 39(1):17–38.

Zhang L, Zhang X (2024) Mispricing and algorithm trading. Inform. Systems Res., ePub ahead of print February 19, https://doi.org 10.1287 /isre 2021.0570

Zhang XM, Zhu F (2011) Group size and incentives to contribute: A natural experiment at Chinese Wikipedia. Amer. Econom. Rev. 101(4):1601–1615.

Zhou J, Zhang Q, Zhou S, Li X, Zhang X (2023) Unintended emotional effects of online health communities: A text mining supported empirical study. MIS Quart. 47(1):195–266.

Zhu F, Zhang XM (2010) Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.
