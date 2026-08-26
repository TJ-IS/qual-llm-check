---
otero_id: 28696
otero_key: "BHKM4ACE"
title: "Algorithms to the Rescue: Market Mechanisms for Consensual Trading of Unbiased Individual Data"
authors: "Brian Birkhead; Ashkan Eshghi; Ram D. Gopal; Hooman Hidaji; Raymond A. Patterson"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2024.1115"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Algorithms to the Rescue: Market Mechanisms for Consensual Trading of Unbiased Individual Data

Brian Birkhead,<sup>a</sup> Ashkan Eshghi,<sup>b</sup> Ram D. Gopal,<sup>b</sup> Hooman Hidaji,<sup>c,</sup>\* Raymond A. Patterson<sup>c</sup>

<sup>a</sup> Coniak Limited, Sunninghill SL5 0PP, United Kingdom; <sup>b</sup> Information Systems and Management, Warwick Business School, University of Warwick, Coventry CV4 7AL, United Kingdom; <sup>c</sup> Haskayne School of Business, University of Calgary, Calgary, Alberta T2N 1N4, Canada \*Corresponding author

Contact: brian.birkhead@coniak.co.uk (BB); ashkan.eshghi@wbs.ac.uk (AE); ram.gopal@wbs.ac.uk (RDG); hooman.hidaji@haskayne.ucalgary.ca, https://orcid.org/0000-0002-5443-7297 (HH); raymond.patterson@ucalgary.ca, https://orcid.org/0000-0001-5408-6485 (RAP)

Received: April 22, 2024 Revised: November 8, 2024; January 23, 2025 Accepted: February 3, 2025 Published Online in Articles in Advance: March 25, 2025

https://doi.org/10.1287/isre.2024.1115

Copyright: © 2025 INFORMS

Abstract. The online economy has relied on collecting and monetizing users’ individual data in exchange for tools and services. A lack of transparency and the absence of proper compensation mechanisms have gradually eroded data quality in this market, giving rise to a new generation of platform-mediated data markets that aim to explicitly reimburse data subjects in return for their individual data. Moreover, these platforms can create data markets for direct collection of data from users in contexts like surveys and healthcare research. Such platforms, however, use either centralized-optimization or fixed-compensation mecha nisms, which lead to expensive and/or biased samples for data buyers. In this paper, we present an algorithmic market mechanism approach that employs an incentive-compatible compensation mechanism in conjunction with a novel sampling method to enable such plat forms to provide data buyers with low-cost, unbiased samples while properly compensat ing data subjects for their loss of privacy. We illustrate the superior performance of our market mechanism against current approaches. We find that our approach outperforms the fixed-compensation approach, and even if the platform has access to partial information about data subjects’ privacy concern, in practice, they are better off foregoing this information and using our approach instead. Finally, we provide insights about the trade-off between bias and cost in data samples and about the implications of sample size and anonymity.

History: Martin Bichler, Senior Editor; Jianqing Chen, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2024.1115.

Keywords: individual data • data market • mechanism design • sampling algorithm • privacy • bias

## 1. Introduction

In targeted advertising and in other applications that involve data collection on individuals, such as in surveys and healthcare research, there is a need for consensual and transparent collection of representative data from users. We propose an algorithmic market mechanism approach to achieve this at low cost. We begin by describing the shortcomings of the current approaches for data collection.

The current online economy has been founded in large part on users being willing to share their data in exchange for the use of online services, such as search engines, social media, email platforms, and mobile apps. The widespread use of the internet over recent decades has created legion online opportunities for companies to collect data on users. In 2020, there were approximately 4.9 billion active internet users worldwide (Johnson 2021) who created approximately 64 zettabytes of data (Von See 2020). These data, which we refer to as individual data, include information such as demographics, preferences, online behavior, purchasing patterns, and location information of individual users, whom we refer to as data subjects. Such data represent enormous potential value for companies trying to target and reach prospects, acquire new customers, grow customer loyalty, predict consumer needs, and develop new and more personalized products and services. This has led to an explosion in demand for individual data, creating a market now valued at \$270 billion in 2024 (Maximize Market Research 2025).

The collection of individual data is done largely by third-party brokers that assiduously track user browsing behavior across different websites, apps, social media, and e-commerce platforms, collecting their data with neither their true and explicit knowledge nor consent of these extended activities. Prior research illustrates that the third-party data collection process is murky at best (Gopal et al. 2018, Eshghi et al. 2023). The data resulting from this underhand data collection process are then often fed to machine-learning algorithms to build a range of products and services, including consumer profiling, market segmentation, audience targeting models, and tailored market insights (Tucker and Neumann 2020). Data subjects whose data assets are collected and sold in this way are seldom compensated for the use of their data or for any consequential loss of their privacy (Choi et al. 2019, Ichihashi 2021a, Acemoglu et al. 2022).

Historically, data subjects have been willing to give up their private information for no direct compensation, but they are now rapidly waking up to the risks to their privacy that may ensue when it is shared. A lack of proper compensation induces privacy-sensitive data subjects to protect their data through the use of privacy tools. According to Cisco (2021), in 2021, 86% of online users cared about their data privacy, and 79% of those who cared were willing to act, with 47% of these users actually acting to preserve their data privacy. According to another source (Security.org 2025), 105 million adult U.S. internet users claim to use a virtual private network (VPN) service, and Forbes (2019) reports that nearly 47% of internet users employed ad blockers in 2019. Given that the use of privacy tools acts as a restrictive filter on the reach of data brokers, it introduces significant levels of bias in their data sets, with data subjects less sensitive to privacy issues being overrepresented. Because of the correlations between privacy sensitivity and individual data, the lack of participation from privacy-sensitive data subjects causes the data to lack representativeness (Ghosh and Roth 2015, Hwang 2020). Indeed, Neumann (2019) has shown that the return on investment of online advertising is often negative, largely as a consequence of its reliance on fundamentally poor and inaccurate data.

To add to these shortcomings, the current market structure struggles to accommodate the strict regimes currently being introduced around the globe to regulate the acquisition and use of individual data, such as the European Union General Data Protection Regulation (GDPR) and the California Consumer Privacy Act (CCPA). Such regulation requires direct consent from data subjects along with clear limits on use, storage, and sharing of data before their individual data can be collected, throwing the current paradigms further into disarray (Forbes 2018). Adding to this the imminent introduction of constraints on using third-party tracking cookies (Mudd 2021, Temkin 2021), it is clear that a radical change in how the individual data market operates is needed.

## 1.1. Data Markets

In response to the above issues, a new market has emerged that strives to collect individual data consensually and properly compensate data subjects for their loss of privacy. In this emerging market, platforms offer primary services, such as data portability, with paid compensation for the use of that data being a secondary activity (e.g., mydex, digi.me, meeco, and dataswift). Others, including Reklaim, citizenme, BIGtoken, and getmyslice, have created digital marketplaces where users are directly compensated whenever their individual data are sold to buyers. Buyers are usually advertisers and marketers who provide services, such as business to business data enrichment, compliance, crossdevice identity management, crossdevice match ing, identity-based targeting, identity verification and resolution, and marketing and advertising services (Datarade 2022). These platforms also have uses in influencer-led campaigns and coupon-targeting campaigns. The firms in this sector rely on either fixed-price compensation mechanisms or centralized optimization based on partial information about data subjects’ pri vacy concerns.

The challenge of collecting unbiased data at low cost extends beyond online advertising into direct data collection from users. For example, consider collection of data through surveys, where the respondents are paid for their data and responses. This is done in various ways across different use cases, fo example, by Google Opinion Rewards, Branded Surveys, Swagbucks, SurveyJunkie, American Consumer Opinion, Find Out Now, and Pineconce Research, where the data-collecting company collects data on the buyer’s behalf. Traditionally, these companies provide data and insight services to buyers and collect data from individual users by paying them in return for completing surveys and providing their data. Representativeness of the data and its cost are critical aspects. Current methods for acquiring individual data involve paying each user a fixed amount for their responses (Google 2024) (left panel of Figure 1). Further examples abound in healthcare, where emerg ing platforms, such as Hu-manity, Nebula Genomics, and DeHealth, allow for the sale of individual’s health records (right panel of Figure 1). These emerging platforms set the compensation to data subjects without considering user privacy concerns and simply use either fixed-compensation or centralized-optimization approaches for data acquisition.

The flaws in the current approaches of fixed compensation and centralized optimization based on partial information are directly addressed in this paper. Fixed compensation is where the data subjects are compensated at a fixed amount for their data. Fixed compensation mechanisms, although simple to operate, result in the data subjects with privacy cost or reservation price above the set fixed price not participating and not allowing their data to be included in the sample sold to data buyers. As discussed above, this selfselection toward the privacy-insensitive end of the population causes significant bias in the resulting data set if privacy concern and data subjects’ characteristics are correlated. The importance of such correlation has been established in the context of data markets (Fleischer and Lyu 2012, Roth and Schoenebeck 2012, Ghosh and Roth 2015, Hwang 2020). Creating a representative data set, therefore, becomes prohibitively expensive as a result of having to set the fixed price above the highest individual privacy cost. Next, the centralized-optimization approach for buying data from data subjects involves the use of optimization and partial information on data subjects to set reimbursement to them. Even though this approach may work for platforms that have access to information about data subjects’ activities (e.g., Facebook in social media and Ant Financial in fintech), it cannot be used where no information about data subjects is available to the platform: for example, in the context provided above for advertising, survey data collection, and healthcare research. More importantly, even with partial information, the centralized approach may not be the best solution for data acquisition.

Figure 1. (Color online) Examples of Data Intermediary Platforms: Google Opinion Rewards and DeHealth  
![](/api/attachments/BHKM4ACE/fulltext/images/11aa95e98b2951ed92eeb6771734410364ba76cfb6329f07b60cfb1d9161c640.jpg)

## 1.2. Our Proposed Compensation Mechanism

In this paper, we propose an alternative compensation mechanism for such data markets, one that both yields an unbiased data sample and comes at a low cost to buyers. In collaboration with a new start-up in this sector, Numerous Limited,<sup>1</sup> we have developed a compensation mechanism that encourages data subjects to participate and receive compensation for their data. That is to say, we have designed a market mechanism that overcomes the issues around transparency, consent, and data subjects’ privacy concern and desire for reasonable compensation. Our approach employs novel sampling algorithms in conjunction with an incentive-compatible auction mechanism as a compensation scheme. We show that our methodology allows a platform to simultaneously induce data subjects to truthfully report their privacy concern, compensate data subjects for their loss of privacy, and provide unbiased and low-cost data samples to buyers.

The current practices for buying data from data subjects mainly involve data subjects responding to particular queries that belong to a specific context or business. In our proposed approach, the data will be collected from data subjects ex ante, and then, the data subjects will be compensated when a buyer buys that data subject’s data in an automated manner. Moreover, each data subject will be compensated according to their privacy preferences such that the collected data are representative of the population of data subjects. The incentive-compatible mechanism that we utilize in our approach prevents users from misrepresenting their privacy preferences to increase their compensation. At a high level, this is because if a data subject misrepresents their privacy preferences, then their expected compensation decreases. In other words, it is in data subjects’ interest to truthfully report their privacy preferences.

Use of an intermediary platform to enable the collection and sale of data is critical when it comes to aggregated data that are representative of the population as it enables economies of scale. When using a platform, data subjects do not have to complete their online profiles or answer individual surveys for each buyer. Rather, they can only do this once with the platform. The platform then enables large-scale sale of the data to buyers through automated transactions based on data subject preferences and compensates data subjects for each transaction. Because of a current lack of a robust platform that performs this task, such collection of data is not common practice. Once such a platform exists, it can enable broad adoption by data subjects and buyers.

We provide theoretical comparisons between our proposed approach and the benchmarks of fixed compensation and centralized optimization as well as with the best-case benchmark. We demonstrate that our market mechanism results in a representative data sample at near-optimal cost. Finally, we confirm the robustness of our findings across a wide array of simulations.

Our results indicate that our proposed approach can achieve theoretical best-case bias of zero, implying that it produces representative samples for buyers. Further, the cost of the resulting sample is close to the best-case benchmark. Not only does our market mechanism dominate the fixed-compensation approach, but also, in most practical settings, it outperforms even centralized-optimization approaches with access to partial information about user privacy concerns. Interestingly, this implies that even where a platform can estimate data subjects’ privacy concern, perhaps through observing their behavior on the platform, it is still better off not utilizing this information. The platform can achieve better results utilizing our market mechanism approach to create a market between data subjects and buyers. Moreover, we show that our mechanism is similar to the best-case benchmark in terms of equality and inclusion measurements. In addition to these main findings, we provide insights on the impact of sample size and anonymity on the performance of different mechanisms.

Our study contributes to both theory and practice. Theoretically, we propose an algorithmic market mechanism that combines a sampling algorithm with an auction mechanism. This creates an individually rational and incentive-compatible mechanism that provides an unbiased sample of the actual data with nearoptimal cost. Moreover, whereas prior studies in data markets combine mechanism design with estimation methods to get to an unbiased estimation from a biased sample, our approach yields an unbiased sample—a drastic change in the underlying approach. In terms of contributions to practice, our market mechanism not only performs close to best-case benchmarks but also, outperforms both current approaches of fixed compensation and centralized optimization, and it is, therefore, a strong alternative to the current practice. Moreover, our approach has desirable properties for implementation, making it a viable alternative to current practice. This enables the creation of a data market that benefits both the data subjects as well as buyers while being compliant with regulation requiring transparency and consent.

## 2. Literature Review

Personal data transactions have been the subject of many prior studies, most of which focus on the buyers valuation and pricing of the personal data. For example, Li et al. (2014) present a theoretical framework for private data sales, Garfinkel et al. (2006) explore a market scenario where individuals’ personal information is exchanged in the form of numeric data, and Mehta et al. (2021) develop pricing policies for data monetization when buyers have private information about their ideal records. More recent examples are Zhang et al. (2023) and Xing and Wang (2024), which examine pricing and sample set strategies of data providers under quality information asymmetry and competition. We do not consider buyers’ valuation of individual data and focus instead on designing mechanisms to incentivize privacy-aware individuals to sell their data in a marketplace. Our analysis is on the compensation to users rather than the price charged to buyers.

Recently, there has been significant attention toward designing market mechanisms for the trading of data (Ho¨rner and Skrzypacz 2016, Agarwal et al. 2019, Ber gemann and Bonatti 2019, Ichihashi 2020, Cummings et al. 2023, Fallah et al. 2024). A significant portion of the literature centers around personal data markets aiming to acquire private data from a group of individuals who are conscious of their privacy. The primary goal of these studies is to develop centralizedoptimization mechanisms that minimize the combined value of the estimation inaccuracy and the overall payment made to users as compensation for using their data. Ghosh and Roth (2015) claim that in cases where there is a correlation between individual data and pri vacy, it is impossible to come up with an individually rational and dominant strategy truthful mechanism. Chen et al. (2018) and Fallah et al. (2024) address this issue by making assumptions about the distribution of users’ privacy costs and by using a Bayesian mechanism design approach to create an optimal mechanism for collecting data with privacy guarantees. We also consider the user data and privacy concern to be correlated as in Ghosh and Roth (2015). On the other hand, we design a market mechanism that is individually rational and truthful and that dominates other approaches in realistic settings. Moreover, contrary to Chen et al. (2018) and Fallah et al. (2024), we do not impose restrictive constraints on the distribution of privacy concern and individual data.

An inherent challenge in designing mechanisms for purchasing data from privacy-aware users is the trade-off between privacy costs and the quality of data. One commonly employed approach to address this conflict is to employ techniques, such as differential privacy (Dwork 2006), to restrict the amount of personal data that is exposed. Differential privacy achieves this by making arbitrarily small changes (adding noise) to individual data in a way that does not change the statistics of the data set. Several studies employ differential privacy to measure the costs that users bear when disclosing their data (Nissim et al. 2012, 2014; Cummings et al. 2015, 2022, 2023;

Ghosh and Roth 2015; Fallah et al. 2024). These studies inherently assume strategic users who are capable of discerning complex mathematical constructs. An additional drawback of employing differential privacy is its complexity, which hinders further analysis of the market, limiting the solutions to the level of mechanism design. Our approach, on the other hand, does not require such complexities and employs practical sampling algorithms along with widely used compensation mechanisms to create a market for data. A strength of our market mechanism is that it yields an unbiased data sample, irrespective of the data subject preferences, without the need for adding noise.

Within this literature, there are a few studies that do not employ differential privacy to quantify privacy cost, including Roth and Schoenebeck (2012), Chen et al. (2018), and Chen and Zheng (2019). Instead, these studies consider a set of probability-price pairs to manage the level of privacy loss and compensation for individual users. These studies propose joint compensationestimation mechanisms with the aim of minimizing the sum of the value of estimation error and total payment to users through randomized mechanisms, wherein a user’s data are selected based on the probability determined by the user’s reported privacy costs. Whereas the resulting sample from these approaches is biased, our market mechanism provides an unbiased sample with near-optimal compensation cost. The focus of getting an unbiased sample rather than an unbiased estimation is an important novelty of our approach.

Our paper is also related to the other settings and concerns related to data markets that have been examined in the existing body of research. Ichihashi (2020), Cummings et al. (2023), and Fallah et al. (2024) examine a scenario where individuals derive advantages from an improved estimation result. The correlation between users’ data, referred to as data externalities, and its influence on data prices has been examined in several studies, including Choi et al. (2019), Ichihash (2021b), Acemoglu et al. (2022), and Liao et al. (2022). The impact of competition between firms on data prices and user decisions has been studied in Bimpikis et al. (2019), Ichihashi (2021a), and Ali et al. (2023). There is also a substantial body of research on the issue of nonverifiable data points, where providers may intentionally provide false data to manipulate the model and achieve desired results (Dekel et al. 2010, Meir et al. 2012, Ghosh et al. 2014, Liu and Chen 2016).

Our work contributes to the existing literature in several ways. Considering our proposed mechanism, prior works study mechanism design problems with a centralized-optimization approach, where the objective of the platform is to minimize the sum of cost because of estimation error and total payment to the users. We, on the other hand, propose an algorithmic market mechanism with the goal of minimizing total data subject compensation while providing an unbiased sample of the actual (noise-free) data. This approach incorporates a novel sampling algorithm that allows for using an individually rational and incentive-compatible compensation mechanism. In other words, the problem that we study in this paper is a novel one that has not been addressed in the literature regarding the derivation of unbiased data samples at near-optimal compensation cost.

Our proposed approach provides several benefits. First, it does not rely on assumptions about user ability or heterogeneity as we do not make any assumptions on the ability of data subjects to discern complex mathematical constructs. Additionally, whereas studies in the literature assume either that there is no heterogeneity in user privacy concerns or that the distribution of user privacy concerns is known, our proposed mechanism is ambivalent about the distribution of user privacy concerns. Our market mechanism also performs well with respect to measures of inclusion and equality in data markets. Such aspects are critical in the long-term viability of individual data markets but have not been previously considered. Finally, our analysis demonstrates the superiority of our approach in a wide variety of conditions as compared with the current approaches.

## 3. Setting and Problem Description

We consider a platform that offers buyers anonymized samples of sensitive attribute data. For context, consider a buyer that aims to target data subjects with an advertising campaign, collect survey data from data subjects, or collect health data from data subjects. The platform’s database consists of a population of indi vidual records containing a unique identifier, a quasiidentifier, and the sensitive attribute of interest to potential buyers. Unique identifiers are attributes such as phone number, email address, Social Security num ber, or any other attribute that uniquely identifies a data subject. The quasi-identifiers may include a range of data subject attributes, such as their demography (e.g., age, gender, and zip code) or interests and preferences (e.g., travel, games, and music). Sensitive attributes are ones about which data subjects may have privacy concerns if disclosed to buyers, such as health status, salary, and political opinions. Potential buyers are interested in and may benefit from knowing these sensitive attributes: for example, to enhance the effectiveness of their marketing, product design, or planning processes. Table 1 summarizes our notation.

Consider a buyer—one that aims to target users for advertising or one that aims to gain insights from them—that is interested in buying sensitive attribute data for an unbiased sample of n data subjects within a population defined by a specific set of quasi-identifiers.

Table 1. Variables

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td>N</td><td>Number of data subjects with the quasi-identifiers that are dictated by the buyer</td></tr><tr><td>n</td><td>Sample size</td></tr><tr><td>ai</td><td>Data subject i&#x27;s sensitive attribute</td></tr><tr><td>vi</td><td>Data subject i&#x27;s privacy concern</td></tr><tr><td>vi&#x27;</td><td>Data subject i&#x27;s reported privacy concern</td></tr><tr><td> $\overline{v}$ </td><td>Maximum privacy concern among data subjects</td></tr><tr><td>ki</td><td>k-anonymity: Number of data subjects in the data sample with the same quasi-identifiers as data subject i</td></tr><tr><td>γ(.)</td><td>Privacy cost function</td></tr><tr><td>α</td><td>The elasticity of privacy cost with respect to k-anonymity; as α increases, privacy cost is more sensitive to changes in k-anonymity</td></tr><tr><td>ci</td><td>The amount of compensation that data subject i receives if she consents to share her information</td></tr><tr><td>c</td><td>The amount of fixed compensation that all data subjects receive if they consent to share their information</td></tr><tr><td>Ui(.)</td><td>Data subject i&#x27;s utility function</td></tr><tr><td>S</td><td>Sample data set, which consists of selected data subjects&#x27; sensitive attributes</td></tr><tr><td>A</td><td>Set of all data subjects&#x27; sensitive attribute</td></tr><tr><td>C</td><td>Set of the selected data subjects&#x27; compensation</td></tr><tr><td>B</td><td>Sample bias</td></tr><tr><td>TC</td><td>Total compensation paid to obtain consent from data subjects</td></tr><tr><td>Z</td><td>Ratio of data subjects with no chance of being selected in the sample</td></tr><tr><td>G</td><td>Gini index for data subjects&#x27; probability of being selected in the sample</td></tr><tr><td>Vp</td><td>Variance of data subjects&#x27; chances for being selected in the sample</td></tr><tr><td>Φ</td><td>Total cost includes total compensation and cost of bias</td></tr><tr><td>ω</td><td>Per unit cost of bias</td></tr><tr><td>d</td><td>Platform&#x27;s level of uncertainty about data subjects&#x27; privacy concerns</td></tr></table>

We assume that the platform’s database includes N data subjects with the requisite quasi-identifiers.<sup>2</sup> The platform is tasked with selecting n data subjects from this population and sharing their anonymized data with the buyer. The data are anonymized by redacting unique identifiers. We assume that data subjects have privacy concerns about sharing their sensitive attributes with buyers. This is because of the fact that sharing even anonymized samples of data with a buyer may harm data subjects given the possibility of reidentification when their quasi-identifier information is combined with data from other sources. We explicitly incorporate this reidentification risk and its associated concerns in our model using the concept of k-anonymity. For a given data subject i, the data sample is $k _ { i ^ { - } }$ anonymous if there exist $k _ { i } - 1$ other data subjects in the sample with the same quasi-identifiers (Samarati 2001). This expresses the probability of being reidentified as the reciprocal of the number of data subjects in the sample with the same quasi-identifiers. It follows that as $\bar { k } _ { i }$ increases, the probability of data subject i being reidentified decreases.

To obtain data subjects’ consent to share their sensitive attribute data with a buyer, the platform compensates them for their expected loss of privacy. Users who are targeted for advertising, respond to survey questions, or share their healthcare data are subject to this loss of privacy. We assume that data subject $\bar { i } \in \mathcal { N } ,$ where $\mathcal { N } = \left\{ { 1 , \dots \dag } , N \right\}$ , gives her consent to share her sensitive attribute, denoted as $a _ { i } ,$ with the buyer if her utility $U _ { i }$ from sharing it is higher than zero. The expected utility of data subject $i \in \bar { \mathcal { N } }$ is given as

$$
E (U _ {i}) = \left\{ \begin{array}{l l} p _ {i} [ c _ {i} - \gamma (v _ {i}, n) ], & \text { if   data   subject   } i \text {   consents } \\ & \text { to   share   her   information } \\ 0, & \text { otherwise }, \end{array} \right.\tag{1}
$$

where $p _ { i }$ is the probability of being selected in the sample data for data subject $i , v _ { i }$ is the privacy concern of data subject $i ,$ and $c _ { i }$ is the amount of compensation that data subject i receives if she consents to sharing her information. Data subjects’ privacy cost (γ) depends on privacy concern and the probability of being identified, which is captured by k-anonymity. In our setting, $k = k _ { i }$ is equal to the sample size (n) for all data subjects given that all data subjects in the sample have the same quasiidentifier specified by the buyer. If the sample includes only one data subject, then privacy cost is equal to privacy concern. Privacy cost function is increasing in pri vacy concern and decreasing in sample size. Properties of the privacy cost function are represented as follows:<sup>3</sup>

$$
\frac {\partial \gamma}{\partial v} > 0, \quad \frac {\partial \gamma}{\partial n} \leq 0, \quad \gamma (0, n) = 0, \quad \gamma (v, 1) = v.\tag{2}
$$

The platform selects a sample from the population that includes information on n data subjects who consent to sell their information to the buyer.<sup>4</sup> To obtain consent from each selected data subject, the platform needs to set the level of compensation higher than the privacy cost of that data subject: that is, $c _ { i } \geq \gamma ( v _ { i } , n )$ Data subjects’ sensitive attributes and privacy concerns may be either positively or negatively correlated, and we assume that the magnitude of this correlation is unknown to the platform. If the sensitive attributes and privacy concerns are uncorrelated, then even though our approach still results in an unbiased sample, its use is not necessary because the problem becomes trivial as the data subjects can be randomly sampled. The evidence from data markets, however, corroborates the importance of considering such a correlation, and this consideration is commonplace in the literature (Fleischer and Lyu 2012, Roth and Schoenebeck 2012, Ghosh and Roth 2015, Hwang 2020).

A simple but naive way for the platform to obtain data subject consent and one that is currently employed in data markets is to offer all data subjects a fixed, equal compensation. To ensure that the sample is unbiased, however, the fixed compensation needs to exceed every data subject’s privacy cost. The problem with this approach is that such a sample is prohibitively expensive to acquire. If the platform reduces the level of compensation below the maximum privacy cost, then it introduces bias into the sample by excluding subjects with high privacy concerns. To overcome the inefficiencies associated with this trade-off between cost and bias, the platform should adjust compensation in line with each individual data subject’s privacy concern, which requires the platform to know this for every individual. This trade-off between bias and sample cost is at the heart of the problem that we study. We introduce a marketplace approach, combining a compensation mechanism and a sampling algorithm that allow the platform to reliably elicit these privacy concerns and use them to provide unbiased and low-cost samples to buyers. We provide our model timeline in Figure 2.

## 4. Mechanism Design

To design a mechanism that generates an unbiased sample of size n from the platform’s qualifying population, we take the following approach. First, to ensure that the platform elicits reliable data on subjects’ privacy concerns, we adopt a compensation mechanism for selecting a single record from the data set that induces truth telling. In order to produce a sample of size n, this truth-telling mechanism should be repeated within n separate subpopulations. We show that the optimal subpopulation size is two; that is, each subpopulation should comprise just two data subjects. Then, using this mechanism, we propose a simple yet robust sampling algorithm for selecting the subpopulation pairs. Finally, we form our market mechanism by incorporating the compensation mechanism into our sampling algorithm.

## 4.1. Compensation Mechanism

We focus first on a basic mechanism for selecting one data subject from a set of potential data subjects. An effective compensation mechanism must satisfy two constraints: individual rationality to ensure that all data subjects participate and incentive compatibility to ensure that data subjects truthfully report their privacy concern. A compensation mechanism is individually rational if it results in nonnegative expected utility for all data subjects: that is, $\begin{array} { r } { E ( U _ { i } ) \geq 0 , } \end{array}$ , ∀i. This ensures that all data subjects participate, and the data set is representative of the population.<sup>5</sup> A compensation mechanism is incentive compatible if it is in the data subject’s best interest to truthfully report their privacy concern: that is, $E ( U _ { i } | v _ { i } ^ { \prime } = v _ { i } ) \geq \dot { E } ( U _ { i } \vert \mathbf { \hat { v } } _ { i } ^ { \prime } \neq v _ { i } )$ ), ∀i, where $v _ { i } ^ { \prime }$ is data subject $i ^ { \prime } \mathrm { s }$ reported privacy concern. This results in a mechanisms where data subjects do not have the incentive to misrepresent their privacy concern.

Figure 2. Model Timeline  
![](/api/attachments/BHKM4ACE/fulltext/images/ae78b88c43daa065b942a88ffaf9f7e1ee0069da5ea175a38455d63f4e1631d0.jpg)  
\*Data subjects can change their privacy preferences at any point in time.  
<sup>†</sup>This is equivalent to asking data subjects to report their privacy concern.

Proposition 1 (Second Compensation Auction). Let $v _ { i } ^ { \prime }$ be the reported privacy concern, $v _ { i }$ be the actual privacy concern, and $\gamma ( v _ { i } )$ be the privacy cost of data subject $i ,$ where $i \in \mathcal { T }$ and $| { \mathcal { T } } | \geq 2$ . Then, the following compensation mechanism is both incentive compatible $( v _ { i } ^ { \prime } = v _ { i } , \ \forall i \in \mathcal { T } )$ and individually rational $( U _ { i } \ge 0 , \ \forall i \in \mathcal { T } )$

$$
c _ {i} = \left\{ \begin{array}{l l} \gamma \bigg (\min _ {j \neq i} (v _ {j} ^ {\prime}), n \bigg), & \text { if } \quad v _ {i} ^ {\prime} <   \min _ {j \neq i} (v _ {j} ^ {\prime}), \forall j \in \mathcal {I} \\ 0, & \text { otherwise. } \end{array} \right.\tag{3}
$$

In this mechanism, the platform chooses the data subject with the lowest reported privacy concern (cheapest record $i , v _ { i } ^ { \prime } < \operatorname* { m i n } _ { j \neq i } ( v _ { i } ^ { \prime } ) )$ and compensates the data subject at the reservation price (privacy cost) of the data subject with the second-lowest reported privacy concern $( \mathrm { m i n } _ { j \neq i } ( v _ { j } ^ { \prime } ) )$ , which is $\gamma ( \mathrm { { m i n } } _ { j \neq i } \bar { ( } v _ { j } ^ { \prime } ) )$ . We refer to this procurement mechanism as second compensation auction, which is a variation of the Vickrey–Clarke–Grove (VCG) mechanism (Vickrey 1961, Clarke 1971, Groves 1973), where data subject i’s compensation is calculated as the difference between the surplus of other data subjects when data subject i is present and the surplus of other data subjects when data subject i is absent. Using modified versions of the VCG mechanism is a common approach in the literature of procurement auctions (Chen et al. 2005, Bichler et al. 2006, Chu and Shen 2008, Baranov et al. 2017). In our context where the data sample constitutes many data points (sellers), the data sample is created using a sampling algorithm that incorporates multiple second compensation auction mechanisms as we describe below.

## 4.2. Sampling Algorithm

To deliver a sample of size n, the platform requires us to create n subpopulations from the population of N qualifying data subjects and then, apply the second compensation auction mechanism in Proposition 1 to each subpopulation. Bias is defined as the difference between the expected sensitive attribute of the selected data subject and the average sensitive attribute of population. If the platform selects a random data subject from each subpopulation, then the final sample is unbiased with respect to the sensitive attribute; however, this results in a sample with high cost as discussed in Section 3. Instead, our proposed mechanism selects the data subject with the lowest reported privacy concern from each subpopulation in order to minimize the sample cost. Therefore, the larger the subpopulation, the higher the variation in data sub-$\mathrm { j e c t s } ^ { \prime }$ privacy concern, which results in higher variation in sensitive attribute when there is correlation between sensitive attribute and privacy concern. As subpopulation size increases, where the data subject with the lowest reported privacy cost is chosen from each subpopulation, the expected difference between the average sensitive attribute and the sensitive attribute of the data subject with lowest privacy concern increases, meaning that the expected bias increases. We incorporate this insight in our proposed sampling algorithm.

The goal of any sampling algorithm employed by the platform is to minimize the expected cost and bias of the sample. As explained above, to minimize bias, our approach uses the smallest possible subpopulation, representing a single pair of data subjects. To further decrease the bias, we propose that the platform sort data subjects by their sensitive attributes and select the adjacent pairs of ordered data subjects. Where the sensitive attributes and privacy concerns are correlated, this approach also decreases the expected difference between the privacy concerns of the selected pairs of data subjects and thus, decreases the expected cost.

Even though in our sampling method, the platform is able to sort the data set based on the data subjects sensitive attribute, which is shared with the platform as they subscribe to its service, we do not consider this to pose a privacy cost to the data subjects. In other words, we do not consider data subjects’ privacy concern when setting their profile with the platform. Rather, privacy concerns are realized only if the platform sells data subjects’ data to the buyers. This is without a loss in generality for three reasons. First, in cases where data subjects trust the platform, the platform is endowed with access to the sensitive attribute, thus enabling the sorting of D. Second, even if data subjects do not trust the platform, tools exist for the ordering of a data set according to a vector without gaining knowledge of the vector’s constituent values (Emmadi et al. 2015, Cheng et al. 2019, Chatterjee and Sengupta 2020, Hong et al. 2021). One such technique is homomorphic encryption, a cryptographic paradigm that facilitates the execution of computations on encrypted data while it remains in its encrypted form (Gentry 2010). In the context of sorting, homomorphic encryption allows for comparisons and rearrangements of encrypted records based on their inherent mathematical relationships (Van Dijk et al. 2010). Consequently, sorting can be accomplished on encrypted data, thus preserving the confidentiality and privacy of sensitive information throughout the process. In other words, in this approach, the platform does not have access to data subjects’ sensitive attributes and thereby, does not pose a privacy cost to them.

Third, even where data subjects have concerns about joining the platform, perhaps because they can not trust the platform’s use of homomorphic encryption or may be concerned about loss of data through a security breach, this will not impact our findings. This is because additional privacy concerns due to the platform will be imposed on all data subjects, and our constraint on individual rationality ensures that data subjects have the incentive to join the platform. Thereby, our results do not change with a diminished user base because of possible privacy or security concerns about the platform itself. With elevated privacy concerns across the board, the total compensation in our approach as well as all other benchmark approaches increases, and buyers need to pay more for data samples. However, this does not have a material impact on the comparison between approaches.

## 4.3. Market Mechanism

We now combine the compensation mechanism with the sampling algorithm to design our market mechanism, which we denote as random sampling of rolling pairs (RSP). In this approach, the platform first announces the mechanism and sample size (n) to all qualifying data subjects and asks the qualifying data subjects to report their privacy concern and sensitive attribute.<sup>6</sup> Then, the platform forms the data $\mathcal { D } =$ $\{ ( a _ { i } , v _ { i } ) | i \in \mathcal { N } \}$ and sorts D by the sensitive attribute in ascending (descending) order if the correlation between the privacy concerns and sensitive attribute is positive (negative); that is, if $c o r r ( a , v ) > 0 \ ( c o r r ( a , v ) < 0 )$ , then $a _ { i } > \breve { a } _ { j } ( a _ { i } < a _ { j } ) , \forall i > j , ( i , j ) \in \mathcal N ^ { 2 }$ . The inputs to this algorithm are, therefore, the sample size n and a set of data subjects’ sensitive attributes $\bar { \mathcal { A } } = \{ a _ { i } | i \in \mathcal { N } \}$ . The outputs are an anonymized sample $s \subset A$ of n data subjects sensitive attributes and a set of compensations for the selected data subjects denoted by C.

After sorting D, the platform randomly selects a data subject and compares her reported privacy concern with the next data subject in the sorted data D. Next, the platform selects the data subject of the pair with lower reported privacy concern, adds her sensitive attribute to the sample ${ \mathcal { S } } ,$ compensates her at the reservation price of the other data subject, and removes her from the data. The platform repeats this process n times to select n data subjects.<sup>7</sup> The logic of this method is set out in Algorithm 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 (RSP)
Input: A, n
Output: S, C
 $N \leftarrow |A|$ 
for i = 1 to N do
    $v_i \leftarrow i$ 's reported privacy concern
    $d_i \leftarrow (a_i, v_i)$ 
end for
 $D \leftarrow \{d_i | i \in \{1,..,N\}\}$ 
Sort D by A
 $S \leftarrow \varnothing$ $C \leftarrow \varnothing$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
for m=1 to n do
    for i=1 to  $|D|$  do
    $d_{i} \leftarrow$ ith element of D
    end for
    $k \leftarrow$ Random element of  $\{1,\ldots,|D|\}$ 
    if  $k \neq |D|$  then
    if  $v_{k} \leq v_{k+1}$  then
    $S \leftarrow S \cup \{a_{k}\}$ $C \leftarrow C \cup \{\gamma(v_{k+1},n)\}$ $D \leftarrow D \setminus \{d_{k}\}$ 
    else
    $S \leftarrow S \cup \{a_{k+1}\}$ $C \leftarrow C \cup \{\gamma(v_{k},n)\}$ $D \leftarrow D \setminus \{d_{k+1}\}$ 
    end if
    else
    $S \leftarrow S \cup \{a_{k}\}$ $C \leftarrow C \cup \{\gamma(\overline{v},n)\}$ $D \leftarrow D \setminus \{d_{k}\}$ 
    end if
end for
</div>

It is useful to discuss the practical viability of our approach at this point. In our approach, a set of n auctions is run for each transaction: that is, each query o request from a buyer. Considering that buyers may be looking for data from thousands of data subjects, this implies running thousands of auctions for each transaction. Even though this may on the surface seem burdensome both computationally and in terms of data subjects’ involvement, it does not pose a practical challenge, even if the number of transactions is considerably large. Computationally, our approach and its use of the procurement auction mechanism are similar to real-time bidding, which is common in online ad-exchange markets (also known as behavioral advertising). In that context, every time a user conducts an online search, visits a website, or interacts with an app, such auctions are used to place ads where many advertisers bid for the ad placement. Generally, the computational requirements of such auctions are considered to be insignificant, and they are run repeatedly in frac tions of a second (Chen et al. 2011). Further, considering the involvement of data subjects, even though they bid for each transaction, they do not set their prefer ences and privacy concerns every time there is a transaction. Rather, data subjects set these preferences and their profile once in the settings of the platform, possi bly in an app. The auctions can then be conducted automatically without the presence of the data subjects considering their set preferences and privacy concerns. This too is similar to real-time bidding in ad-exchange markets, where the bids are automated based on the preferences of advertisers, which are set on the platform. Additional details about our approach are pro vided in the model timeline in Figure 2.

## 5. Analysis and Results

In this section, we measure the performance of the proposed mechanisms under the worst-case scenario, where data subjects’ privacy concerns and sensitive attributes are perfectly correlated. We assume that the data subjects’ privacy concern and sensitive attributes both follow continuous distributions with finite supports:<sup>8</sup> $v \in [ 0 , 1 ] , a \in [ 0 , 1 ]$ , and $c o r r ( v , a ) \in \{ - 1 , 1 \}$ Perfect correlation constitutes the worst-case scenario because the higher the correlation, the higher the sample bias if a proper mechanism is not used. We investigate the performance of the above mechanisms under imperfect correlation in Section 6.

As explained above, the privacy cost of data subjects depends on their privacy concern and their probability of being identified in the data sample captured by k-anonymity. The sample size determines k-anonymity for a given data subject, and we capture the intensity of the k-anonymity effect on privacy cost through the elasticity of privacy cost with respect to k-anonymity, which we refer to as $\alpha \in [ 0 , 1 ]$ . Thus, the total privacy cost is defined as $\gamma ( v , n ) = v n ^ { - \alpha }$ . The term $n ^ { - \alpha }$ captures the effect of k-anonymity on data subjects’ privacy cost, which makes our cost function quite flexible and captures a wide variety of situations. If $\alpha = 0$ , then the sample size has no effect on the privacy cost, and as α increases, a larger sample size results in increasingly lower privacy cost. In other words, as α increases, privacy cost is more sensitive to changes in sample size. Our results are robust to different values of $\alpha ,$ and we use this parameter to provide additional insights on our results.

## 5.1. Measurements

To analyze the performance of benchmark methods and our proposed mechanism, we compare them in terms of bias and cost. Sample bias (B) is calculated as the difference between the sample mean, $\mu _ { S } = 1 / n \sum _ { a \in S } a ,$ , and the population mean, $\textstyle \mu = 1 / N \sum _ { a \in { \mathcal { A } } } a \colon$ that is, $B =$ $| \mu _ { S } - \mu |$ . A sampling method is unbiased if its expected bias is zero, where expected bias is given as follows:

$$
E (B) = | E (\mu_ {S}) - \mu |.
$$

Total compensation (TC) for a sample is the cost of obtaining the data subjects’ consent (that is, the summation of all data subjects’ compensation):

$$
T C = \sum_ {i = 1} ^ {N} c _ {i}.
$$

In the above equation, because the compensation to data subjects who are not chosen in the sample is zero per (3) in Proposition 1, the summation over the whole population (N) yields the compensation paid to only data subjects who are included in the sample (n).

Additionally, we consider two other aspects of a sampling method. First, a lack of inclusiveness is measured by exclusion $( Z ) .$ , which is defined as the proportion of all data subjects with a zero chance of being selected in the sample. A mechanism with high $Z$ is unattractive to a platform in the long run as it always excludes many data subjects for a given type of query. Exclusion is derived as

$$
Z = \frac {| \{i : p _ {i} = 0 \} |}{N}.
$$

The second aspect that we consider is the variability of data subjects’ chances of being selected or inequality. We investigate two measures of inequality: the variance of chances for being selected $( \hat V _ { p } )$ and the Gini index of chances for being selected (G). Given that the average probability of a data subject being selected is $n / N , \bar { V } _ { p }$ and G are derived as

$$
V _ {p} = \frac {1}{N - 1} \sum_ {i = 1} ^ {N} \left[ p _ {i} - \frac {n}{N} \right] ^ {2}, \qquad G = \frac {\sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} | p _ {i} - p _ {j} |}{2 \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} p _ {j}}.
$$

## 5.2. Best-Case Benchmark: Simple Random Sampling

For the best-case benchmark approach, we consider the platform to have complete information about the privacy concern of all qualifying data subjects in its database. Even though this method is not feasible in practice because of the platform not having access to data subjects’ privacy cost, it represents a theoretical best-case benchmark. In this approach, the platform randomly selects a sample of size n and offers each data subject compensation equal to her reservation price. This randomly selected sample is unbiased, $E ( B ^ { \hat { \mathrm { S R S } } } ) = 0 .$ , and the probability of being selected $p _ { i } ^ { \mathrm { S R S } } = n / N$ is equal for all data subjects, which means that $Z ^ { \mathrm { S R S } ^ { ' } } = G ^ { \mathrm { S R S } } = V _ { v } ^ { \mathrm { S R S } } = 0$ (simple random sampling (SRS)). Data subject i’s reservation price is $\gamma ( v _ { i } , n )$ , and the expected privacy concern is $E ( v _ { i } ) = 1 / 2$ . Thus, the expected total compensation of this method is $E ( T C ^ { \mathrm { S R S } } ) = \dot { n } ^ { 1 - \alpha } / 2$

## 5.3. Fixed Compensation

In this approach, the platform offers a fixed compensation to all data subjects $( c _ { i } = c , \forall i \in \{ 1 , \dots , N \} )$ ) and randomly selects a sample from those data subjects who provide consent. When privacy concerns and sensitive attributes are correlated, if c is lower than the maximum reservation price, $\gamma ( \overline { { v } } , n )$ , then the sample is biased as it only includes data subjects with reservation prices lower than $c .$ To ensure that at least n data subjects provide consent, the fixed compensation should be greater than the nth-lowest reservation price: that ${ \mathrm { i } } \mathbf { s } ,$ $c \in [ c _ { L } , c _ { H } ] .$ , where $c _ { L } = \gamma ( v _ { ( n ) } , n ) , c _ { H } = \gamma ( \overline { { v } } , n )$ , and $v _ { ( n ) }$ is the nth-lowest privacy concern.

For any given $c ,$ there are m data subjects with positive expected utility, which means that $\gamma ( v _ { ( m ) } , n ) \leq c .$ . In other words, there are exactly m data subjects with $v _ { ( m ) } \leq c n ^ { \alpha }$ and $N - m$ data subjects with $v _ { ( m ) } > c n ^ { \alpha }$ Thus, m follows a binomial distribution, $m \sim \dot { B } ( N , c n ^ { \alpha } ) .$ and $E ( a _ { ( m ) } ) = E ( v _ { ( m ) } ) = c n ^ { \alpha }$ . Therefore, the expected mean of the sample is $E ( \mu _ { \scriptscriptstyle S } ^ { F C } ) = c n ^ { \alpha } / 2 ,$ , and the expected bias is $E ( B ^ { \hat { F } C } ) = ( c n ^ { \alpha } - 1 ) / 2$

There is a trade-off between the bias and total compensation of the sample. As c increases, expected total compensation increases, and bias decreases. Assuming a linear cost of bias,<sup>9</sup> where the platform incurs a cost equal to ω for each unit of bias, the platform’s objective would be minimizing the total cost of $\Phi = T C + { \ ' { \omega } } | B |$ | . In the fixed-compensation scenario $\Phi ^ { F C } = ( c [ 2 n - \omega n ^ { \alpha } ] + \omega ) / 2 ,$ the platform’s problem is

$$
\begin{array}{l l} \underset {c} {\min} & \Phi^ {F C} \\ \text {s.t.} & c \geq \gamma (v _ {(n)}, n). \end{array}
$$

From above, $\partial ^ { 2 } \Phi ^ { F C } / \partial c ^ { 2 } = 0 ;$ that is, the objective function is linear, and therefore, there is no interior solution to the above optimization problem. The corner solution depends on the sign of $\hat { \partial } \Phi / \partial c = ( 2 n - \omega n ^ { \alpha } ) / 2 .$ If $\partial \Phi ^ { F C } / \partial c \hat { < } 0$ , which implies $\omega > \hat { \omega } \equiv 2 n ^ { 1 - \alpha }$ , then the optimal compensation would be equal to the highest reservation price: that is, $c ^ { * } = c _ { H } = \gamma ( \overline { { v } } , n )$ . We refer to this variation of fixed compensation as FCH. On the other hand, if ${ \partial \Phi } / { \partial c } > 0 .$ , which implies $\omega < { \hat { \omega } } .$ , then the optimal compensation would be equal to the nthlowest reservation price: that is, $c ^ { * } = c _ { L } = \gamma ( v _ { ( n ) } , n )$ . We refer to this variation of fixed compensation as FCL:

$$
c ^ {* F C} = \left\{ \begin{array}{l l} c ^ {F C H} = c _ {H}, & \text { if } \quad \omega > \hat {\omega} \equiv 2 n ^ {1 - \alpha} \\ c ^ {F C L} = c _ {L}, & \text { if } \quad \omega \leq \hat {\omega}. \end{array} \right.
$$

In FCH, the probability of being selected is equal for all data subjects; therefore, $Z ^ { F C H } = G ^ { F C H } = V _ { n } ^ { F C H } = 0 \ :$ . In the FCL method, data subject i’s probability of being selected is

$$
p _ {i} ^ {F C L} = \left\{ \begin{array}{l l} 1, & \text { if } v _ {i} \leq v _ {(n)} \\ 0, & \text { otherwise. } \end{array} \right.
$$

Therefore, $Z ^ { F C L } = G ^ { F C L } = ( N - n ) / N ,$ , and $V _ { p } ^ { F C L } = ( n [ N$ $- n ] ) / ( N [ N - 1 ] )$

## 5.4. Random Sampling of Rolling Pairs

In this approach, which we described in Section 4.3, the platform randomly samples n data subjects without replacement, and it compares the privacy concern of each chosen data subject with that of the data subject with the next highest sensitive attribute and chooses the one with the lower privacy concern. This method clearly provides an unbiased sample: that is, $E ( B ^ { R S P } ) = 0 \dot { }$ . Moreover, the probability of being selected is equal for all data subjects, which means that $Z ^ { R S P } = G ^ { R S P } = V _ { v } ^ { R S P } = 0$ . Arnold et al. (2008) show that for a sample of size n from any continuous distribution with finite supports l and $u ,$ the expected distance between the ith-order and (i + 1)th-order statistics is $( u - l ) / ( n + 1 )$ . Therefore, the expected compensation for data subject i is derived as

$$
\begin{array}{l} E (c _ {i} ^ {R S P}) \\ = \left\{ \begin{array}{l l} \frac {n ^ {1 - \alpha} [ i + 1 ]}{N [ N + 1 ]} + \sum_ {j = 1} ^ {n - 1} \frac {n ! [ N - j - 1 ] !}{n ^ {\alpha} [ j + 1 ] [ n - j - 1 ] ! [ N - 1 ] !}, & \forall i \leq N - n \\ \frac {n ^ {1 - \alpha} [ i + 1 ]}{N [ N + 1 ]} + \sum_ {j = 1} ^ {N - i} \frac {n ! [ N - j - 1 ] !}{n ^ {\alpha} [ j + 1 ] [ n - j - 1 ] ! [ N - 1 ] !}, & \forall i > N - n. \end{array} \right. \end{array}
$$

Employing this mechanism, the expected total compensation of obtaining data subjects’ consent is

$$
\begin{array}{l} E (T C ^ {R S P}) = \sum_ {i = 1} ^ {N} \frac {n ^ {1 - \alpha} [ i + 1 ]}{N [ N + 1 ]} \\ \qquad + \sum_ {j = 1} ^ {n - 1} \frac {n ! [ N - j ] !}{n ^ {\alpha} [ j + 1 ] [ n - j - 1 ] ! [ N + 1 ] !}. \end{array}\tag{4}
$$

The expected total compensation in (4) can be rewritten as $n ^ { 1 - \hat { \alpha } } / 2 + ( { \bf H } _ { N + 2 } - { \bf H } _ { N + 2 - n } ^ { \hat { \alpha } } ) / n ^ { \alpha } .$ , where $\textstyle \mathbf { H } _ { x } = \sum _ { r = 1 } ^ { x } 1 / r$ is the xth harmonic number and $\mathbf { H } _ { x } - \mathbf { H } _ { y } \approx \ln ( x ) - \ln ( y ) -$ $[ [ x - y ] / 2 x y ]$

## 5.5. Comparison of Method Performance

The theoretical bias, total compensation, exclusion, and inequality for each of the benchmarks and the proposed mechanism are summarized in Table 2.

To evaluate the performance of our proposed mechanism, we compare it with the fixed-compensation methods with equivalent bias and total compensation in our next proposition.

Proposition 2. In the worst-case scenario, for an equivalent total compensation (bias), RSP performs better than fixed compensation in terms of bias (total compensation). In other words, $\forall N > 1 , \ i f \ B ^ { F C } \leq B ^ { R S P }$ , then $\dot { T } C ^ { F C } > T C ^ { R S P }$ and if $T C ^ { F C } \le T C ^ { R S P }$ , then $B ^ { F C } > B ^ { R S P }$

Proposition 2 indicates that our proposed mechanism performs better than the corresponding fixedcompensation method in terms of both bias and total compensation. This implies that our mechanism dominates fixed-compensation approach.

We next compare the total costs of the two approaches: that is, where the cost of bias is considered along with compensation cost.

Proposition 3. Total cost of RSP is less than that of the best fixed-compensation method unless the per unit cost of bias is small; that is, $\omega < \hat { \omega } _ { L }$ , where $\hat { \omega } _ { L } = ( [ N - 2 n$ $+ 1 ] n + 2 [ N + 1 ] [ \mathbf { H } _ { N + 2 } - \mathbf { H } _ { N + 2 - n } ] ) / ( n ^ { \alpha } [ N - n + 1 ] ) < \hat { \omega }$

Proposition 3 specifies the condition on per unit cost of bias for which best fixed compensation has lower cost than RSP. This proposition indicates that if best fixed compensation occurs with FCH (rather than with

Table 2. Theoretical Results

<table><tr><td rowspan="2">Method</td><td rowspan="2">Bias E(B)</td><td rowspan="2">Total compensation E(TC)</td><td rowspan="2">Exclusion Z</td><td colspan="2">Inequality</td></tr><tr><td>G</td><td> $V_p$ </td></tr><tr><td>SRS (best-case benchmark)</td><td>0</td><td> $\frac{n^{1-\alpha}}{2}$ </td><td>0</td><td>0</td><td>0</td></tr><tr><td>FCH</td><td>0</td><td> $n^{1-\alpha}$ </td><td>0</td><td>0</td><td>0</td></tr><tr><td>FCL</td><td> $\frac{n-N}{2[N+1]}$ </td><td> $\frac{n^{2-\alpha}}{N+1}$ </td><td> $\frac{N-n}{N}$ </td><td> $\frac{N-n}{N}$ </td><td> $\frac{n[N-n]}{N[N-1]}$ </td></tr><tr><td>RSP</td><td>0</td><td> $\frac{n^{1-\alpha}}{2}+\frac{\mathbf{H}_{N+2}-\mathbf{H}_{N+2-n}}{n^\alpha}$ </td><td>0</td><td>0</td><td>0</td></tr></table>

FCL), then RSP performs better than the best fixedcompensation method. This emphasizes that if the goal is to achieve an unbiased sample, then the best fixedcompensation method is inferior to RSP. On the other hand, if some bias in the sample is acceptable, then best fixed compensation may yield lower cost than RSP (although with higher bias) only where the cost of bias is low. That is, only where $\omega < \hat { \omega } _ { L }$ does $\mathrm { R S P ^ { \prime } s }$ linear total cost become larger than that of the best fixedcompensation method, which is FCL for these regions of ω. Small values of ω represent the cases where the buyer does not benefit from high-quality data samples with low bias. In other words, intuitively, the best fixed-compensation method is only useful where bias is not important to the buyer. Figure 3 illustrates the comparison between our proposed mechanism and the best fixed compensation in terms of total cost.

## 5.6. Impact of Sample Size

The FCH and RSP approaches generate samples that are unbiased, irrespective of sample size. FCL is the only approach that does not randomly select data subjects and is, therefore, highly affected by sample size. As sample size increases, the magnitude of the bias for this method decreases. The measures of exclusion and Gini index both decrease with sample size, whereas variance of chances first increases and then, decreases with it. These conclusions about the impact of sample size on bias follow directly from our theoretical results summarized in Table 2. Moreover, the total compensation of our proposed mechanism is close to the bestcase benchmark, irrespective of sample size. FCH has the highest total compensation of all methods. FCL has the lowest total compensation for small sample size, but as sample size increases, its total compensation increases faster than other methods; as expected, when $n = N ,$ its total compensation is equal to the total compensation of FCH.

Considering the above results, it is clear that our proposed mechanism (RSP) weakly dominates all of the benchmarks with respect to all measurements of performance, with the exception of total compensation, where the sample size is small. RSP is unbiased irrespective of sample size. However, where the sampling fraction is small $( n < N / 2 )$ , it is more costly than FCL. This shortcoming disappears for large sample sizes $( n > N / 2 )$ as FCL becomes more costly.

In our next proposition, we discuss the impact of sample size on average cost (per data subject) of each approach.

## Proposition 4.

a. As sample size increases, the average cost of FCH decreases, but the average cost of FCL increases.

Figure 3. (Color online) Total Cost of RSP vs. Best Fixed-Compensation Method  
![](/api/attachments/BHKM4ACE/fulltext/images/50bd4e3c7d138869f169465abb0af4942395e375dbc40136522673a85cf40d47.jpg)

b. As sample size increases, the average cost of RSP increases if the elasticity of privacy cost is small $( \alpha < \check { \alpha } )$ and decreases if the elasticity of privacy cost is large $( \alpha > { \hat { \alpha } } )$ where $\check { \alpha } \approx 1 / ( N [ N - 1 ] )$ and $\begin{array} { r } { \hat { \alpha } \approx \frac { 3 } { 4 } . } \end{array}$ On the other hand, if the elasticity of privacy cost is moderate $( \check { \alpha } < \alpha < \hat { \alpha } )$ , then as sample size increases, the average cost of RSP decreases when sample size is small $( n < \tilde { n } )$ and increases when sample size is large (n > n˜ ), where $\widetilde { n } \approx N - 1 / \alpha N$

Proposition 4 explores the economies of scale of the approaches in choosing a sample size. If privacy cost is elastic with respect to k-anonymity (α > 0), then the average and marginal costs of FCH decrease with sample size, implying that these methods create data samples that benefit from economies of scale in transacting individual data. At the extreme, where α � 1, the marginal costs of these two methods are zero, and their total compensation is independent of sample size. By way of contrast, the average and marginal costs associated with the FCL increase with sample size, thereby creating data samples with diseconomies of scale.

For RSP, marginal cost initially decreases but then, increases at higher levels of sample size. This is because as sampling is done without replacement, the gap between the privacy cost of adjacent data subjects increases as sample size increases, resulting in an exponential increase in compensation. The combination of this effect and the impact from k-anonymity produces a U-shaped marginal cost with respect to sample size, suggesting the existence of both economies of scale and diseconomies of scale at different sample sizes for this mechanism.

## 6. Simulation Analysis

To further analyze the performance of the mechanisms, we generate simulated population data and then, use the benchmark and our proposed mechanisms to produce samples. Once again, we use bias, total compensation, exclusion, and inequality to compare the methods. We generate the sensitive attribute and privacy concern for the population according to standard uniform distributions.<sup>10</sup> To check the robustness of our results, we also rerun the simulation analysis considering both privacy concern and sensitive attribute to follow a beta distribution. To extend our theoretical results above, in addition to the perfect correlation scenario, we further generate population data sets with different levels of correlation between the sensitive attribute and privacy concern by randomly reordering the privacy concerns to achieve the different levels of correlation. Finally, we have added to our simulated results an analysis of the mechanisms on a real-world data set provided by our industry partner, Numerous Limited.

## 6.1. Perfect Correlation

First, we consider the case of perfect correlation between the sensitive attribute and privacy concern, which as we have already noted, is a worst-case scenario because high correlation causes significant bias if an appropriate approach is not used. In this section, we aim to confirm through simulation our theoretical results presented in Section 5. The simulated data set is composed of N � 200 data subjects, and a number of samples of size n � 50 were drawn from it using different sampling methods, assuming α � 1. The sampling process was repeated 500,000 times for each method. The results of these simulations are summarized in Table 3, where these are also compared with our theoretical results (see Table 2) for N � 200, n � 50, and α � 1.

It can be seen that, as expected, the simulation results confirm our findings about the performance of the mechanisms where there is perfect correlation between the sensitive attribute and privacy concern.

To evaluate the magnitude of bias associated with each method, we use the two one-sided t-test (TOST) approach of Schuirmann (1987). In this approach, two one-sided t tests are used to find if the difference between a method’s bias and zero is greater than a so-called “margin of equivalence,” denoted as δ. The statistical test hypotheses are given as

$$
\begin{array}{l l} H _ {0}: & \mu_ {S} - \mu <   - \delta \quad \text {or} \quad \mu_ {S} - \mu > \delta \\ H _ {1}: & - \delta \leq \mu_ {S} - \mu \leq \delta . \end{array}\tag{5}
$$

In $( 5 ) , H _ { 0 }$ can be converted into two null hypotheses— $H _ { 0 } ^ { 1 } : \mu _ { S } - \mu < - \delta$ and $H _ { 0 } ^ { 2 } : \mu _ { S } - \mu > \delta$ If both null hypotheses are rejected using one-sided t tests and the larger p-value, then it can be concluded that bias is in the range $[ - \delta , \delta ]$ . In this case, we calculated δ as a percentage of the population mean of $\mu = 0 . 5$ using three different equivalence margins, $\delta = 0 . 0 1 \times 0 . 5 , \delta = 0 . 0 0 5$ $\times 0 . 5 ,$ , and $\mathbf { \bar { \delta } } ( \delta = 0 . 0 0 1 \times 0 . 5 .$ . The resulting p-values are presented in Table 4. This implies that, as expected, SRS, FCH, and RSP are unbiased, whereas FCL is biased.

Table 3. Comparison of Theoretical and Simulation Results Under Perfect Correlation

<table><tr><td rowspan="2">Method</td><td colspan="5">Theoretical values</td><td colspan="5">Simulation results</td></tr><tr><td> $E(B)$ </td><td> $E(TC)$ </td><td>Z</td><td>G</td><td> $V_p$ </td><td> $E(B)$ </td><td> $E(TC)$ </td><td>Z</td><td>G</td><td> $V_p$ </td></tr><tr><td>SRS</td><td>0</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td> $7.53 \times 10^{-6}$ </td><td>0.5</td><td>0</td><td>0.0013</td><td> $3.43 \times 10^{-7}$ </td></tr><tr><td>FCH</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td> $6.97 \times 10^{-5}$ </td><td>0.9932</td><td>0</td><td>0.0013</td><td> $3.35 \times 10^{-7}$ </td></tr><tr><td>FCL</td><td>-0.3731</td><td>0.2487</td><td>0.75</td><td>0.75</td><td>0.1884</td><td>-0.3899</td><td>0.2581</td><td>0.75</td><td>0.75</td><td>0.1884</td></tr><tr><td>RSP</td><td>0</td><td>0.5056</td><td>0</td><td>0</td><td>0</td><td> $5.46 \times 10^{-5}$ </td><td>0.5057</td><td>0</td><td>0.0013</td><td> $3.48 \times 10^{-7}$ </td></tr></table>

Table 4. Two One-Sided t-Test p-Values—Simulated Data Set $( \mu = 0 . 5 )$

<table><tr><td>Method</td><td> $\delta = \mu \times 0.01$ </td><td> $\delta = \mu \times 0.005$ </td><td> $\delta = \mu \times 0.001$ </td></tr><tr><td>SRS</td><td>0</td><td>0</td><td> $2.7 \times 10^{-22}$ </td></tr><tr><td>FCH</td><td>0</td><td>0</td><td> $1.34 \times 10^{-27}$ </td></tr><tr><td>FCL</td><td>1</td><td>1</td><td>1</td></tr><tr><td>RSP</td><td>0</td><td>0</td><td> $2.41 \times 10^{-26}$ </td></tr></table>

## 6.2. Imperfect Correlation

We extend our simulation analysis beyond the confirmatory exercise in Section 6.1 to cover situations where there is imperfect correlation between privacy concern and the sensitive attribute. Figure 4 shows the impact of varying levels of correlation on bias. For all levels of correlation between the sensitive attribute and privacy concern, our proposed method provides samples with insignificant bias. As correlation increases, bias for RSP decreases and tends toward zero.

The impact of correlation on total compensation is shown in Figure 5. It can be seen that total compensation of RSP is significantly lower than that of FCH, and as correlation increases, total compensation decreases and nears the best-case benchmark.

Figure 6 summarizes our results for the impact of correlation on exclusion and inequality. Correlation does not impact exclusion and inequality except in the case of RSP, for which exclusion and inequality increase with correlation.

In summary, our simulation results confirm that our proposed mechanisms continue to perform well in the presence of imperfect correlation.

To rule out any impact on results that may be because of the choice of distributions, we also consider both privacy concern and sensitive attribute to follow a beta distribution with random parameters $\alpha$ and $\beta$ between 1 and 100. Because of the flexibility of the beta distribution, this choice of distribution captures a wide variety of conditions of symmetry, skewness, and variation. For example, this captures where the distributions follow a normal distribution or where they are heavily skewed. We randomize the two distributions 1,000,000 times with randomized parameters, and we calculate the correlation between them. These results are consistent with those drawn from the uniform distribution and are omitted for brevity.

## 6.3. Random Sampling of Rolling Pairs vs. Fixed Compensation

In this section, we compare our proposed method with that of fixed compensation with equivalent total compensation or bias with imperfect correlation between privacy concern and sensitive attribute as was done in the worst-case scenario in Proposition 2. These results are summarized in Figure 7 using the beta distribution for privacy concern and sensitive attribute.

The left panel of Figure 7 shows the bias of RSP along with the corresponding fixed-compensation method, which has the same total compensation as the RSP. The right panel of Figure 7 shows the total compensation of RSP along with the corresponding fixed-compensation method, which has the same bias as RSP. As can be seen in Figure 7, as long as correlation is higher than a threshold, RSP dominates the fixed-compensation method with the corresponding bias or total compensation. This shows the superiority of our proposed method in the majority of the scenarios that are the focus of our study.

Figure 4. (Color online) Comparison of Bias—Simulated Data  
![](/api/attachments/BHKM4ACE/fulltext/images/0704e8bbf607479fd69cdf7b5567a38b724cb62a3dcb70a7cf4b20e7f2ada249.jpg)

Figure 5. (Color online) Comparison of Total Compensation—Simulated Data  
![](/api/attachments/BHKM4ACE/fulltext/images/e04e246f1e823d502586d4771d720b4e8485126e3c7eb765e0e518d56fb85de6.jpg)

## 6.4. Real-World Data Set

We test our mechanisms using a real-world data set from our industry partner, Numerous Limited. This data set was collected through a survey with 444 data subjects. The survey details and summary statistics are provided in Table 5. Three questions from the survey are used to generate a measure of privacy concern: “1. How would you describe yourself when it comes to data sharing and privacy? 2. I dislike the fact that third parties make money from my personal data while I don’t receive anything (scale of 1—strongly disagree to 5—strongly agree). 3. Which of the following techniques have you employed to improve your data privacy (I use incognito mode when I’m browsing; I say no to cookies online; I use a privacy-focused search engine, like Duck Duck Go; I use a VPN).” The measure of privacy concern is formed by extracting the first principal component of these three responses to capture the variation among data subjects’ privacy concern. The response to the survey question “What is your household income?” is used to measure the sensitive attribute. The average the sensitive attribute is $\mu = 2 9 , 6 8 7 ,$ and its correlation with the measure of privacy concern is low at $c o r r ( v , a ) = 0 . 0 1 8 6$

The same simulation setup described in Section 6.1 above produced the results shown in Table $^ { 6 , }$ and the TOST p-values are reported in Table 7. These results demonstrate that even in the case where the correlation between the sensitive attribute and privacy concern is low, RSP provides an unbiased sample. Additionally, the cost of our proposed method is close to the bestcase benchmark. These results are all consistent with our previous findings.

To further analyze the impact of sample size on the performance of the methods, we repeated the above simulation process 88 times for different sample sizes $n \in \{ 5 , 1 0 , 1 5 , \dots , 4 4 0 \}$ using the real-world data set. The results from these analyses are in line with the theoretical findings, and they demonstrate that our proposed mechanism continues to perform well in the real-world setting.

## 7. Partial Information Scenario

We extend our analysis to consider a scenario where the platform has partial information about data subjects’ privacy concern. We model the partial information scenario as follows. For each data subject $i ,$ the platform knows that the privacy concern $v _ { i }$ falls within a range $[ l _ { i } , u _ { i } ] .$ , where $u _ { i } ^ { \phantom { } - } - l _ { i } ^ { \phantom { } } = \dot { d }$ for all i. Thereby, the parameter d represents the extent of the platform’s uncertainty about privacy concerns and captures a wide array of conditions. As d approaches zero, the problem converges to the complete information scenario, and as d increases, the problem approaches the no information scenario.

Under partial information, the platform can attempt to solve the centralized-optimization problem to match data supply and demand. If the platform’s objective is to provide an unbiased sample, it can randomly select a sample S of n data subjects and offer compensation $c _ { i } \geq v _ { i }$ to each $i \in S$ to ensure that all selected data subjects give consent to share their data. If the platform knows the exact privacy concern of all data subjects $( d = 0 )$ , then $c _ { i } = \gamma ( v _ { i } , n )$ , and the expected total compensation of acquiring an unbiased sample would be $\begin{array} { r } { E ( \sum _ { i \in \mathcal { S } } \gamma ( v _ { i } , n ) \hat { ) } = n ^ { 1 - \alpha } E ( v ) = n ^ { 1 - \alpha } / 2 . } \end{array}$ , which is equal to the expected total compensation of the best-case benchmark, $\mathsf { T C } ^ { S R S }$ . Where $\bar { d } \neq 0 ,$ , to ensure that all selected data subjects give consent to share their data, the platform needs to offer $c _ { i } = \gamma ( u _ { i } , n )$ to data subject I, and the expected total compensation of acquiring an unbiased sample would be $\begin{array} { r } { E ( \sum _ { i \in \cal S } \gamma ( u _ { i } , n ) ) = n ^ { 1 - \alpha } [ ( 1 + d ) / 2 ] } \end{array}$

Figure 6. (Color online) Comparison of Exclusion and Inequality—Simulated Data  
![](/api/attachments/BHKM4ACE/fulltext/images/3188a04d9b930f9bfd35a2f0a310804684b63b9937896025b34113265f5c6040.jpg)

![](/api/attachments/BHKM4ACE/fulltext/images/32e867824e9d96d7ae50d7b314196f4b1891cd6c26289cc921bc45d9feefceef.jpg)

![](/api/attachments/BHKM4ACE/fulltext/images/8ebf00c820442ae5f9068a2d53f2936cdeae6c1a8ad698e2d35d0b046176ebba.jpg)

Figure 7. (Color online) Bias and Total Cost Comparison Between Random Sampling of Rolling Pairs and Fixed Compensation (FC)  
![](/api/attachments/BHKM4ACE/fulltext/images/a2b0318bca4aa6f3affbff120086343c71c3302ac548a5dad19acc0804a2fdfb.jpg)  
Correlation between sensitive attribute and privacy concern

![](/api/attachments/BHKM4ACE/fulltext/images/7a85efaa30a965e0aaef727eda9264736d1f9296eb01c6e11b28869682299e8f.jpg)  
Correlation between sensitive attribute and privacy concern

Under the worst-case scenario, where data subjects’ privacy concerns and sensitive attributes are perfectly correlated, the total compensation of the centralized-optimization (denoted as CO) approach can be formulated as $\begin{array} { r } { \dot { T } C ^ { C O } = n ^ { 1 - \alpha } [ ( 1 + d ) / 2 ^ { \cdot } - | B | ] } \end{array}$ Considering that the platform incurs a cost equal to ω for each unit of bias, the platform’s objective is to find a sample with a bias that minimizes $\Phi ^ { C O } =$ $T C ^ { C O } + \ \omega | \hat { B | } = n ^ { 1 - \alpha } [ ( 1 + d ) / 2 - | B | ] + \omega | B |$ . If there is more than one sample with the optimal bias, then the platform is indifferent between them and can randomly choose between them. Given that the objective function is linear, there is no interior solution to this optimization problem. The corner solution depends on the sign of $\overset { \cdot } { \partial } \Phi / \partial B = \omega - n ^ { 1 - \alpha } . \mathrm { I f } \ \omega < n ^ { 1 - \alpha } ,$ , then the optimal sample is the one with the lowest expected total compensation that we refer to as COL, $\begin{array} { r } { E ( \dot { T } \dot { C } ^ { C O L } ) = \sum _ { i \in 1 , \dots , n } \dot { \gamma } ( u _ { ( i ) } , n ) ) } \end{array}$ $= ( n ^ { 1 - \alpha } [ n + 1 ] + n d [ N + 1 ] ) / ( 2 [ N + 1 ] )$ ), and the expected bias is $E ( B ^ { C O L } ) = ( n - N ) / ( 2 [ N + 1 ] )$ . On the other hand, if $\omega > n ^ { 1 - \alpha } ,$ then the optimal bias is zero, which means that the optimal sample is any random sample (referred to as COH), and the expected total compensation is $E ( T C ^ { C O H } ) = n ^ { 1 - \alpha } \left\lceil \frac { 1 + d } { 2 } \right\rceil$ . Our next proposition formalizes our findings in comparing RSP with centralized optimization.

Table 5. Survey Details and Summary Statistics

<table><tr><td>Question</td><td>Item (score)</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td rowspan="3">“How would you describe yourself when it comes to data sharing and privacy?”</td><td>I have no concerns about sharing my data (0)</td><td>0.87</td><td>0.64</td><td>0</td><td>2</td></tr><tr><td>I have some concerns about sharing my data (1)</td><td></td><td></td><td></td><td></td></tr><tr><td>I have significant concerns about sharing my data (2)</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="5">“I dislike the fact that third parties make money from my personal data while I don’t receive anything.”</td><td>Strongly disagree (0)</td><td>3.34</td><td>0.85</td><td>0</td><td>4</td></tr><tr><td>Disagree (1)</td><td></td><td></td><td></td><td></td></tr><tr><td>Neither agree nor disagree (2)</td><td></td><td></td><td></td><td></td></tr><tr><td>Agree (3)</td><td></td><td></td><td></td><td></td></tr><tr><td>Strongly agree (4)</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="6">“Which of the following techniques have you employed to improve your data privacy?”</td><td>None (0)</td><td>2.55</td><td>2.65</td><td>0</td><td>10</td></tr><tr><td>I say no to cookies online (1)</td><td></td><td></td><td></td><td></td></tr><tr><td>I use incognito mode when I am browsing (2)</td><td></td><td></td><td></td><td></td></tr><tr><td>I use a privacy-focused search engine, like Duck Duck Go (3)</td><td></td><td></td><td></td><td></td></tr><tr><td>I use a VPN (4)</td><td></td><td></td><td></td><td></td></tr><tr><td>Note. If use multiple techniques, add up the scores</td><td></td><td></td><td></td><td></td></tr><tr><td>“What’s your household income?” ($)</td><td></td><td>29,684</td><td>20,128</td><td>5,000</td><td>100,000</td></tr></table>

Table 6. Simulation Results Using the Real-World Data Set

<table><tr><td>Method</td><td> $E(B)$ </td><td> $E(TC)$ </td><td>Z</td><td>G</td><td> $V_p$ </td></tr><tr><td>SRS</td><td>5.78</td><td>2.6211</td><td>0</td><td>0.0023</td><td> $2.11 \times 10^{-7}$ </td></tr><tr><td>FCH</td><td>3.58</td><td>10.1173</td><td>0</td><td>0.0023</td><td> $2.07 \times 10^{-7}$ </td></tr><tr><td>FCL</td><td>-1,584.68</td><td>0.0732</td><td>0.8873</td><td>0.8873</td><td>0.1001</td></tr><tr><td>RSP</td><td>1.02</td><td>3.0129</td><td>0.0563</td><td>0.2891</td><td> $4.9 \times 10^{-3}$ </td></tr></table>

Proposition 5. Total compensation (total cost) of RSP is less than that of COH unless the level of uncertainty in $p r i -$ vacy concerns is small $( d < \hat { d } \equiv ( 2 [ \mathbf { H } _ { N + 2 } - \mathbf { H } _ { N + 2 - n } ] ) / n )$

Proposition 5 provides a clear criterion for choosing between centralized optimization and our proposed mechanism when the platform’s objective is to provide an unbiased sample. As the level of uncertainty in privacy concerns $( d )$ increases, the centralized-optimization approach must compensate for this increased uncertainty by offering higher payments to ensure individual rationality for all selected data subjects. In contrast, our mechanism does not rely on prior knowledge of privacy concerns. Proposition $\dot { 5 }$ establishes a threshold $\hat { d }$ for the uncertainty in privacy concerns, above which our proposed mechanism outperforms the centralizedoptimization approach. Interestingly, this implies that under the partial information scenario with $\dot { d } > \hat { d } ,$ the platform is better off by not using the information that it has about the privacy concerns. As we discuss below, the condition $\hat { d } > \hat { d }$ is almost always the case in practice.

The threshold $\hat { d }$ on the level of uncertainty in privacy concerns in Proposition 5 is a function of the sample size and increases with it. Therefore, substituting n with $N ,$ the upper bound of $\hat { d }$ can be derived as $( 2 { \bf H } _ { N + 2 } - 3 ) / N .$ . As the population size increases, the upper bound of $\hat { d }$ decreases. It can be shown that for any realistic population size, $\hat { d }$ is close to zero. For example, if there are merely 1,000 users in the population, then $\hat { d } < 0 . 0 1 2$ , and if there are 100,000 users in the population, then $\hat { d } < 0 . 0 0 0 2 2$ . Therefore, in most practical settings, our proposed approach dominates the centralized-optimization approach, implying that the use of partial information about data subjects privacy concern is not useful to the platform when it can utilize our proposed mechanism.

Table 7. Two One-Sided t-Test p-Values—Real-World Data Set $( \mu = 2 9 , 6 8 4 . 6 8 )$

<table><tr><td>Method</td><td> $\delta = \mu \times 0.01$ </td><td> $\delta = \mu \times 0.005$ </td><td> $\delta = \mu \times 0.001$ </td></tr><tr><td>SRS</td><td>0</td><td>0</td><td> $1.4 \times 10^{-10}$ </td></tr><tr><td>FCH</td><td>0</td><td>0</td><td> $1.34 \times 10^{-27}$ </td></tr><tr><td>FCL</td><td>1</td><td>1</td><td>1</td></tr><tr><td>RSP</td><td>0</td><td>0</td><td> $2 \times 10^{-14}$ </td></tr></table>

## 8. Concluding Remarks

Individual-level data hold enormous potential fo businesses, and the growing usage of the internet over the last few decades has created legion opportunities for companies to collect data on users online. However, the process of collecting individual data is currently opaque to data subjects and to potential buyers, and this has created a problematic data market characterized by several major issues. As data subjects have become increasingly aware of how their data may be used, they have become concerned about their online privacy. These concerns combined with the lack of compensation for sharing their data have prompted data subjects to employ privacy tools, thereby degrading the quality and representativeness of the data being collected. The use of privacy tools effectively filters data brokers’ reach, introducing substantial bias in their data sets. Privacy-insensitive data subjects become overrep resented, whereas privacy-sensitive subjects opt out, leading to nonrepresentative samples because of the correlation between privacy concerns and individual data. On top of this, policymakers have legislated regulations that prevent the collection of individual data without proper consent. To help eliminate this issue, new mechanisms are required that provide highquality data at a reasonable price to buyers and that appropriately obtain data subjects’ consent for selling their data and directly compensate them for any loss of privacy when their data are sold.

In this study, we propose a novel algorithmic market mechanism for creating a viable market for individual data. Our approach considers an intermediary platform that employs a combination of an auction mechanism and a sampling algorithm and provides unbiased and low-cost individual-level data samples to buyers. The proposed mechanism uniquely enables the platform to induce data subjects to truthfully report their privacy concerns and to compensate them according to their privacy preferences. Whereas there are several methods in the literature for producing unbiased aggregated attribute statistics or noisy data, to the best of our knowledge, ours is the first mechanism that creates unbiased samples of individual data. Moreover, our approach works irrespective of the distribution of user privacy concerns and does not suffer from issues that arise from inaccurate reporting of user privacy concerns.

To analyze the performance of our proposed approach, we have compared the measures of sample bias, total compensation, total cost, exclusion, and inequality against benchmark methods. Our theoretical results show that our proposed mechanism provides unbiased data and that the total cost of our approach is close to the best-case benchmark. Furthermore, as long as data buyers are concerned about data quality, our proposed mechanism dominates the fixed-compensation approach. Our proposed mechanism also demonstrates superior performance compared with centralized-optimization approaches with access to partial information about data subjects’ privacy concerns. Surprisingly, this suggests that platforms are better off disregarding any imperfect estimates of user privacy preferences that they have gathered through monitoring their behavior. Instead, platforms can achieve better outcomes by employing our proposed approach. This suggests that our approach’s ability to elicit truthful information directly from data subjects outweighs the potential benefits of utilizing estimated privacy concerns in centralized optimization.

This study makes important contributions to the emerging literature on data markets. Prior studies have focused on situations in which there is a direct transaction between data subjects and a data analyst, and they propose joint compensation-estimation mechanisms to acquire biased data samples, with the goal of minimizing the summation of estimation error cost and compensation to data subjects. We, in contrast, propose an individually rational and incentive-compatible market mechanism, where an intermediary platform provides unbiased individual-level data samples to buyers at near-optimal cost. We also provide insights regarding the impact of the size and anonymity of the requested sample on the performance of different mechanisms.

Our study has important implications for the individual data industry. Unlike prior work that relies on complex techniques, such as differential privacy, our approach offers a more pragmatic solution. We employ straightforward sampling algorithms and conventional compensation mechanisms that can be readily implemented in real-world data markets. Our proposed market mechanism also exhibits practical advantages that make it a viable alternative to current data market practices. Through theoretical analysis and simulations, we demonstrate that our proposed market mechanism consistently performs close to the best-case benchmark. Moreover, in realistic scenarios, the proposed mechanism outperforms both fixed-compensation and centralized-optimization approaches across all performance measures. This enables the creation of an effective data market that benefits both data subjects and buyers while ensuring compliance with regulations that require transparency and consent mechanisms.

Several avenues for future research can be envisioned. Even though we provide insights on the size of the sample that is chosen, we do not directly model the buyer’s choice of sample size, and this would be an interesting subject for future research. In addition, the issues around operationalizing the elicitation of privacy cost from a platform’s data subjects merit future work. In our setting with an intermediary platform, there are approaches that might help anchor the privacy cost of data subjects. For example, the platform can present data subjects with a range of plausible compensations for them to choose from. This is similar to the procedures currently used for measuring attitudes to risk, where a list or table of binary choices (Holt and Laury 2002) or a set of options (Binswanger 1981) is designed so that an individual’s choice or ranking of the options conveys information about their level of risk aversion. Similarly, it is interesting to empirically study the data subjects’ attitude toward valuation of their own data. It is equally interesting to empirically estimate other model parameters, such as elasticity of privacy cost with respect to anonymity or the platform’s level of uncertainty about data subjects privacy concerns. Moreover, we do not consider the platform’s and buyers’ choices in our paper. Future research can focus on the practical implications of our proposed algorithmic mechanism for platforms’ and buyers’ profitability, platforms’ pricing of data, and buyers’ decision making in buying a data sample.

## Endnotes

<sup>1</sup> Numerous is a transactional digital platform in development that facilitates data subjects securely and consensually submitting their individual data in return for “fair” financial compensation when ever it is later shared with brands (buyers).

<sup>2</sup> Note that the platform may have a much larger user base; however, for the purpose of a single transaction with a buyer, the popu lation is defined as the data subjects who fit the buyer’s descriptions in terms of the quasi-identifiers.

Our main findings do not depend on the characterization of reidentification risk and continue to hold where users’ privacy cost does not depend on sample size: for example, where privacy cost and privacy concern are equivalent. Our purpose in considering reidentification risk is to provide additional insights on the impact of sample size and anonymity on the performance of mechanisms.

<sup>4</sup> Note that selling of data in this context does not imply that the buyer becomes the owner of the data and can use them for any purpose and in perpetuity. The selling of data can include terms on how and for how long it can be used. This is consistent with data regulation such as GDPR and CCPA, both of which include terms on the purpose for which the data will be used and the limits around their use and on data storage over long periods. Deviation from the stated purpose and timeline for which data will be used is illegal. We do not consider such nuances of consent and the purpose for which the data are sold as they have no bearing on our proposed methodology and results, and we use the terms “buy” and “sell” for brevity

<sup>5</sup> Note that this study is ambivalent about the value of data to buyers but considers that the buyer is willing to pay the compensation cost of the data sample as dictated by the individual rationality constraint. In other words, we focus on the compensation to data subjects rather than the price charged to buyers. Therefore, the valuation of data to the buyer does not impact our analysis and results as they pertain to the mechanisms and the comparison among them.

<sup>6</sup> Note that this can be done in real time as data subjects set their preferences in the settings of the platform, similar to real-time bidding in ad-exchange markets. Moreover, as discussed above, the sensitive attribute can be encrypted so that the platform cannot access the actual records.

<sup>7</sup> A similar algorithm can be designed where the data subjects are paired sequentially. Such an algorithm demonstrates comparable performance with the RSP algorithm. For brevity, we focus on the RSP method in this paper.

<sup>8</sup> We limit the range of these attributes to be in [0, 1] for brevity, noting that our results do not change with a parameterized range.

<sup>9</sup> For brevity, we only present results for a linear cost function with respect to bias, noting that our approach remains superior where cost is assumed to be quadratic.

<sup>10</sup> We tested different combinations of uniform and normal distributions for the sensitive attribute and privacy concern. These distribution manipulations yield similar results to the uniform distribution and thus, are omitted for brevity.

## References

Acemoglu D, Makhdoumi A, Malekian A, Ozdaglar A (2022) Too much data: Prices and inefficiencies in data markets. Amer. Econom. J. Microeconomics 14(4):218–256.

Agarwal A, Dahleh M, Sarkar T (2019) A marketplace for data: An algo rithmic solution. Proc. 2019 ACM Conf. Econom. Comput. (Associa tion for Computing Machinery, New York), 701–726.

Ali SN, Lewis G, Vasserman S (2023) Voluntary disclosure and per sonalized pricing. Rev. Econom. Stud. 90(2):538–571.

Arnold BC, Balakrishnan N, Nagaraja HN (2008) A First Course in Order Statistics (SIAM, Philadelphia).

Baranov O, Aperjis C, Ausubel LM, Morrill T (2017) Efficient pro curement auctions with increasing returns. Amer. Econom. J. Microeconomics 9(3):1–27.

Bergemann D, Bonatti A (2019) Markets for information: An intro duction. Annual Rev. Econom. 11(1):85–107.

Bichler M, Davenport A, Hohner G, Kalagnanam J (2006) Industrial procurement auctions. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 593–612.

Bimpikis K, Crapis D, Tahbaz-Salehi A (2019) Information sale and competition. Management Sci. 65(6):2646–2664.

Binswanger HP (1981) Attitudes toward risk: Theoretical implications of an experiment in rural India. Econom. J. 91(364):867–890.

Chatterjee A, Sengupta I (2020) Sorting of fully homomorphic encrypted cloud data: Can partitioning be effective? IEEE Trans. Services Com put. 13(3):545–558.

Chen Y, Zheng S (2019) Prior-free data acquisition for accurate statis tical estimation. Proc. 2019 ACM Conf. Econom. Comput. (Associa tion for Computing Machinery, New York), 659–677.

Chen Y, Berkhin P, Anderson B, Devanur NR (2011) Real-time bid ding algorithms for performance-based display ad allocation. Proc. 17th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (Association for Computing Machinery, New York), 1307–1315.

Chen RR, Roundy RO, Zhang RQ, Janakiraman G (2005) Efficient auction mechanisms for supply chain procurement. Management Sci. 51(3):467–482.

Chen Y, Immorlica N, Lucier B, Syrgkanis V, Ziani J (2018) Optimal data acquisition for statistical estimation. Proc. 2018 ACM Conf. Econom. Comput. (Association for Computing Machinery, New York), 27–44.

Cheng K, Shen Y, Zhang Y, Zhu X, Wang L, Zhong H (2019) Towards efficient privacy-preserving auction mechanism for two-sided cloud markets. ICC 2019 2019 IEEE Internat. Conf. Comm. (ICC) (IEEE, Piscataway, NJ), 1–6.

Choi JP, Jeon DS, Kim BC (2019) Privacy and personal data collection with information externalities. J. Public Econom. 173(C): 113–124.

Chu LY, Shen ZJM (2008) Truthful double auction mechanisms. Oper. Res. 56(1):102–120.

Cisco (2021) Building consumer confidence through transparency and control. Accessed November 20, 2021, https://www.cisco com/c/dam/en\_us/about/doing\_business/trust-center/docs cisco-cybersecurity-series-2021-cps.pdf.

Clarke EH (1971) Multipart pricing of public goods. Public Choice 11(1):17–33.

Cummings R, Feldman V, McMillan A, Talwar K (2022) Mean estimation with user-level privacy under data heterogeneity. Koyejo S, Mohamed S, Agarwal A, Belgrave D, Cho K, Oh A eds. Advances in Neural Information Processing Systems, vol. 35 (Curran Associates, Inc., New York), 29139–29151.

Cummings R, Elzayn H, Pountourakis E, Gkatzelis V, Ziani J (2023) Optimal data acquisition with privacy-aware agents. 2023 IEEE Conf. Secure Trustworthy Machine Learn. (SaTML) (IEEE, Piscataway, NJ), 210–224.

Cummings R, Ligett K, Roth A, Wu ZS, Ziani J (2015) Accuracy fo sale: Aggregating data with a variance constraint. Proc. 2015 Conf. Innovations Theoret. Comput. Sci. (Association for Comput ing Machinery, New York), 317–324.

Datarade (2022) Reklaim—Instantly purchasable datasets. Accessed January 20, 2023, https://www.reklaimyours.com/partners.

Dekel O, Fischer F, Procaccia AD (2010) Incentive compatible regression learning. J. Comput. System Sci. 76(8):759–777.

Dwork C (2006) Differential privacy. Internat. Colloquium Automata Languages Programming (Springer, Berlin, Heidelberg), 1–12.

Emmadi N, Gauravaram P, Narumanchi H, Syed H (2015) Updates on sorting of fully homomorphic encrypted data. 2015 Internat. Conf. Cloud Comput. Res. Innovation (ICCCRI) (IEEE, Piscataway, NJ), 19–24.

Eshghi A, Gopal RD, Hidaji H, Patterson RA (2023) Now you see it, now you don’t: Obfuscation of online third-party information sharing. INFORMS J. Comput. 35(2):286–303.

Fallah A, Makhdoumi A, Malekian A, Ozdaglar A (2024) Optima and differentially private data acquisition: Central and local mechanisms. Oper. Res. 72(3):1105–1123.

Fleischer LK, Lyu YH (2012) Approximately optimal auctions fo selling privacy when costs are correlated with data. Proc. 13th ACM Conf. Electronic Commerce (Association for Computing Machinery, New York), 568–585.

Forbes (2018) How does GDPR impact advertising and e-commerce? Accessed January 28, 2023, https://www.forbes.com/sites/for besagencycouncil/2018/05/08/how-does-gdpr-impact-advertising and-e-commerce/?sh=19c7ccaf3277.

Forbes (2019) 47 percent of consumers are blocking ads. Accessed August 4, 2021, https://www.forbes.com/sites/tjmccue/2019/03 19/47-percent-of-consumers-are-blocking-ads/?sh=f1939252037e.

Garfinkel R, Gopal RD, Nunez M, Rice DO (2006) Secure electronic markets for private information. IEEE Trans. Systems Man Cybernetics Part A Systems Humans 36(3):461–471.

Gentry C (2010) Computing arbitrary functions of encrypted data. Comm. ACM 53(3):97–105.

Ghosh A, Roth A (2015) Selling privacy at auction. Games Econom. Behav. 91(C):334–346.

Ghosh A, Ligett K, Roth A, Schoenebeck G (2014) Buying private data without verification. Proc. Fifteenth ACM Conf. Econom. Comput. (Association for Computing Machinery, New York), 931–948.

Google (2024) Google opinion rewards help. Accessed October 10, 2024, https://play.google.com/store/apps/details?id=com.google.android. apps.paidtasks.

Gopal RD, Hidaji H, Patterson RA, Rolland E, Zhdanov D (2018) How much to share with third parties? User privacy concerns and website dilemmas. MIS Quart. 42(1):143–164.

Groves T (1973) Incentives in teams. Econometrica 41(4):617–631.

Holt CA, Laury SK (2002) Risk aversion and incentive effects. Amer. Econom. Rev. 92(5):1644–1655.

Hong S, Kim S, Choi J, Lee Y, Cheon JH (2021) Efficient sorting of homomorphic encrypted data with k-way sorting network. IEEE Trans. Inform. Forensics Security 16:4389–4404.

Ho¨ rner J, Skrzypacz A (2016) Selling information. J. Political Econom. 124(6):1515–1562.

Hwang T (2020) Subprime Attention Crisis: Advertising and the Time Bomb at the Heart of the Internet (Farrar, Straus and Giroux, New York).

Ichihashi S (2020) Online privacy and information disclosure by consumers. Amer. Econom. Rev. 110(2):569–595.

Ichihashi S (2021a) Competing data intermediaries. RAND J. Econom. 52(3):515–537.

Ichihashi S (2021b) The economics of data externalities. J. Econom. Theory 196:105316.

Johnson J (2021) Number of internet users worldwide from 2005 to 2021. Accessed March 6, 2022, https://www.statista.com/statistics/ 273018/number-of-internet-users-worldwide/.

Li C, Li DY, Miklau G, Suciu D (2014) A theory of pricing private data. ACM Trans. Database Systems 39(4):34.

Liao G, Su Y, Ziani J, Wierman A, Huang J (2022) The privacy paradox and optimal bias-variance trade-offs in data acquisition. ACM Sigmetrics Performance Evaluation Rev. 49(2):6–8.

Liu Y, Chen Y (2016) Learning to incentivize: Eliciting effort via output agreement. Proc. Twenty-Fifth Internat. Joint Conf. Artificial Intelligence (AAAI Press, Palo Alto, CA), 3782–3788.

Maximize Market Research (2025) Data broker market: Global industry analysis and forecast (2025–2032). Accessed March 12, 2025, https://www.maximizemarketresearch.com/market-report global-data-broker-market/55670.

Mehta S, Dawande M, Janakiraman G, Mookerjee V (2021) How to sell a data set? Pricing policies for data monetization. Inform. Systems Res. 32(4):1281–1297.

Meir R, Procaccia AD, Rosenschein JS (2012) Algorithms for strategyproof classification. Artificial Intelligence 186(C):123–156.

Mudd G (2021) Privacy-enhancing technologies and building for the future. Accessed March 20, 2022, https://www.facebook.com business/news/building-for-the-future.

Neumann N (2019) How audience targeting and AI campaigns undermine brand growth. Presentation, Melbourne Business School, Melbourne, Australia.

Nissim K, Orlandi C, Smorodinsky R (2012) Privacy-aware mechanism design. Proc. 13th ACM Conf. Electronic Commerce (Association for Computing Machinery, New York), 774–789.

Nissim K, Vadhan S, Xiao D (2014) Redrawing the boundaries on purchasing data from privacy-sensitive individuals. Proc. 5th Conf. Innovations Theoret. Comput. Sci. (Association for Comput ing Machinery, New York), 411–422.

Roth A, Schoenebeck G (2012) Conducting truthful surveys, cheaply. Proc. 13th ACM Conf. Electronic Commerce (Association for Com puting Machinery, New York), 826–843.

Samarati P (2001) Protecting respondents identities in microdata release. IEEE Trans. Knowledge Data Engrg. 13(6): 1010–1027.

Schuirmann DJ (1987) A comparison of the two one-sided tests procedure and the power approach for assessing the equivalence of average bioavailability. J. Pharmacokinetics Biopharmaceutics 15(6):657–680.

Security.org (2025) VPN consumer usage, adoption & shopping study: 2020. Accessed March 12, 2025, https://www.security org/resources/vpn-consumer-report-annual/.

Temkin D (2021) Charting a course towards a more privacy-first web. Accessed March 20, 2022, https://blog.google/products/ ads-commerce/a-more-privacy-first-web.

Tucker C, Neumann N (2020) Buying consumer data? Tread carefully. Harvard Bus. Rev. (May 1), https://hbr.org/2020/05/buyingconsumer-data-tread-carefully.

Van Dijk M, Gentry C, Halevi S, Vaikuntanathan V (2010) Fully homomorphic encryption over the integers. Adv. Cryptology EURO-CRYPT 2010 29th Annual Internat. Conf. Theory Appl. Cryptographic Techniques (Springer Berlin Heidelberg, Berlin, Heidelberg), 24–43.

Vickrey W (1961) Counterspeculation, auctions, and competitive sealed tenders. J. Finance 16(1):8–37.

Von See A (2020) Volume of data/information created, captured, copied, and consumed worldwide from 2010 to 2023, with forecasts from 2024 to 2028. Accessed March 6, 2022, https://www. statista.com/statistics/871513/worldwide-data-created/.

Xing A, Wang H (2024) Pricing and sample set strategies of data providers under quality information asymmetry. J. Oper. Res. Soc. 75(2):278–296.

Zhang X, Yue WT, Yu Y, Zhang X (2023) How to monetize data: An economic analysis of data monetization strategies under com petition. Decision Support Systems 173:114012.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
