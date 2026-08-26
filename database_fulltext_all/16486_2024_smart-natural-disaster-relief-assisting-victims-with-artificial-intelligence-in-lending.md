---
otero_id: 16486
otero_key: "S2Z345RE"
title: "Smart Natural Disaster Relief: Assisting Victims with Artificial Intelligence in Lending"
authors: "Yidi Liu; Xin Li; Zhiqiang (Eric) Zheng"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.1230"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/S2Z345RE/fulltext/images/e904c4fa7f32754bd4309ec099eac148ce446e973c4a4df56ce6795a20614c43.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Smart Natural Disaster Relief: Assisting Victims with Artificial Intelligence in Lending

Yidi Liu, Xin Li, Zhiqiang (Eric) Zheng

To cite this article: lo cite this article:

Yidi Liu, Xin Li, Zhiqiang (Eric) Zheng (2023) Smart Natural Disaster Relief: Assisting Victims with Artificial Intelligence in Lending. Information Systems Research

Published online in Articles in Advance 31 May 2023

. https://doi.org/10.1287/isre.2023.1230

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2023, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

Research Note

# Smart Natural Disaster Relief: Assisting Victims with Artificial Intelligence in Lending

Yidi Liu,<sup>a</sup> Xin Li,<sup>b</sup> Zhiqiang (Eric) Zheng<sup>c</sup>

<sup>a</sup> School of Management and Economics and Shenzhen Finance Institute, Chinese University of Hong Kong, Shenzhen, Shenzhen 518172, China; <sup>b</sup> Department of Information Systems, College of Business, City University of Hong Kong, Hong Kong; <sup>c</sup> Department of Information Systems and Operations Management, Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080 Contact: Yidi.Liu.PhD@gmail.com, https://orcid.org/0000-0002-7285-0405 (YL); Xin.Li.PhD@Gmail.com, https://orcid.org/0000-0002-0041-3134 (XL); ericz@utdallas.edu, https://orcid.org/0000-0001-8483-8713 (Z(E)Z)

Received: February 14, 2022 Revised: December 6, 2022; February 10, 2023 Accepted: April 10, 2023 Published Online in Articles in Advance: May 31, 2023

https://doi.org/10.1287/isre.2023.1230

Copyright: © 2023 INFORMS

Abstract. Natural disasters wreak economic havoc and cause financial distress for victims. Commercial loans provided by lending firms play a key role in helping victims recover from disasters. This research note studies whether lenders’ use of artificial intelligence (AI) in the lending process can, through reducing delinquency, benefit borrowers who experience natural disasters. Collaborating with a leading credit-scoring company, we track borrowers’ loan applications and lenders’ use of customized AI solutions in assessing loan risks. We find that borrowers who apply to AI-empowered lenders fare better in reducing delinquency rates after experiencing natural disasters. Notably, such a disaster mitigation effect is more pronounced for borrowers with lower credit scores. We explore the possible mechanisms at play and discuss the implications of our findings.

History: Ahmed Abbasi, Robin Dillon-Merrill, H. Raghav Rao, Olivia Sheng, Senior Editors; Zhepeng (Lionel) Li, Associate Editor. This paper has been accepted for the Information Systems Research Specia Issue on Unleashing the Power of Information Technology for Strategic Management of Disasters. Funding: This work was partially supported by the Research Grants Council of the Hong Kong Special Administrative Region, University Grants Committee [General Research Fund Grants 11501722 and 11500519]; the City University of Hong Kong [Strategic Research Grants 7005474 and 7005767]; the InnoHK Initiative; the government of the Hong Kong Special Administrative Region; and the Laboratory for AI-Powered Financial Technologies.

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2023.1230.

Keywords: AI • natural disasters • lending • delinquency • credit scoring • fintech

## 1. Introduction

Natural disasters such as earthquakes, hurricanes, floods, fires, and pandemics cause severe damage, with estimates ranging between USD 100 billion and USD 500 billion each year from 2000 to 2020.<sup>1</sup> Natural disasters inflict financial distress on victims, often leading to a surge in credit needs (Gallagher and Hartley 2017). Providing financial support is vital to the reconstruction and recovery of damaged regions (Celil et al. 2022), and it requires a joint effort from government funds, charities, banks, and other credit services.

In combating natural disasters, government funds often rightfully focus on relieving damage by providing necessities (e.g., food, water, and healthcare) to those in need. Commercial credit providers, such as banks and other lenders, are important supplemental channels for disaster relief. However, loans are not free and are not available to everyone. When a natural disaster strikes, many borrowers’ repayment abilities are likely to be impaired (at least temporarily). Some lenders may thus shun away from lending them money, leaving the market vulnerable to predatory lenders. As a result, victims may face a “double punch”: a direct blow from the natural disaster itself and an indirect blow due to the unavailability or high cost of the loans that they need to cope with the disaster. Worse, the underprivileged, who tend to be more vulnerable to natural disasters, are usually hurt more (Hallegatte et al. 2020). This reality moti vates our broad research question: How can commercial lenders better assist natural disaster victims?

One technology that may have the potential to help address this problem is artificial intelligence (AI). More and more lenders are leveraging AI (e.g., advanced machine learning techniques) in credit-scoring and lend ing decisions, reportedly with improved decision efficiency (Kleinberg et al. 2018) and reduced financial risk (Fuster et al. 2021). Specifically, in the case of natural disasters, AI could help identify victims who would truly benefit from a commercial loan despite the temporary impairment caused by the disaster. These borrowers, referred to as “invisible primes” by Di Maggio et al. (2021), may be able to recover and repay the loan once they receive necessary financial help. AI-based creditscoring tools, with their superior capability to assess creditworthiness, may fare better than non-AI tools in helping lenders discern such prospective borrowers from risky ones who have lost their long-term payback ability.

However, it is important to note that natural disasters could also cause concept drift in credit-scoring models from a machine learning perspective. This includes changes in the borrower population (sampling shift) due to emergence of new borrowers with little credit history in the lending market, and changes in the distribution of feature values (covariate drift) between borrowers in the training data and out-of-sample data. These two types of concept drift mechanisms may complicate the ability of AI-based scoring models in identifying invisible primes and impact AI’s performance differently over differ types of borrowers. Therefore, although AI has the potential to assist lenders in addressing the credit needs of natura disaster victims, it is essential to consider potential concept drift mechanisms that may affect the performance of AI-based credit-scoring models.

This study is an empirical investigation of how lenders’ use of AI in credit scoring can, through reducing loan delinquencies and defaults, benefits borrowers suffering from natural disasters. Delinquency and default rates reflect a borrower’s underlying economic status, and a lower rate suggests an improved status. Thus, if AI-empowered lending helps borrowers economically, it should manifest in lowered delinquency and default rates. To this end, we compile a unique data set linking lenders, borrowers, and disasters. We obtain data on lenders’ AI use and borrowers’ behaviors from a leading credit-scoring firm in China.<sup>2</sup> We then link the data with the natural disaster data retrieved from the China Stock Market and Accounting Research (CSMAR) database through location and time.

Unsurprisingly, our empirical results confirm that natural disasters increase delinquency among affected borrowers. But, interestingly, this adverse effect is mitigated by the use of AI. Specifically, disaster-afflicted borrowers who apply for loans from AI-empowered lenders have 3.9% fewer delinquencies than their counterparts, demonstrating AI’s power of identifying invisible primes. Moreover, AI’s benefit is more pronounced for low-end borrowers with higher needs for credit support, such as those who have lower credit scores, who tend to live in underdeveloped regions, who lack access to government relief funds, and who are relatively young with higher credit needs. These findings are robust under a variety of model specifications and robustness checks. We explore the mechanisms behind and provide evidence for the existence of various types of concept drift that lead to these scenarios.

Overall, our study shows that AI, via its enhanced risk assessment capability, helps reduce delinquency among underprivileged disaster-afflicted borrowers. We thus contribute to the literature in several ways. First, this research responds to the call for new practices to address the threat that disasters pose to society (Park et al. 2015, Abbasi et al. 2021). For policy makers, this research reveals that the use of AI helps ameliorate lending services’ risk and benefits borrowers by reducing their delinquencies after experiencing disasters. Our study is among the first to unveil this little-known benefit of AI in facilitating disaster relief through commercial lending. Second, we provide a posi tive use case of AI fairness where the use of AI in lending can benefit the underprivileged more than the average borrower, complementing the common findings that AI exacerbates unfairness to the underprivileged (Abbasi et al. 2018). Third, the study enriches our understanding of AI’s role in disaster management in general. We show that in addition to AI’s known efficacy in facilitating disaster management through predicting the occurrence of disasters and improving task assignment efficiency, it can provide indirect benefits by facilitating disaster relief through financing.

## 2. Literature and Theoretical Background 2.1. Natural Disasters and Lending

Natural disasters’ impact on the lending market has been widely studied in the literature. Most studies have found that natural disasters cause financial distress, increase victims’ credit demands and personal bankruptcies (Gallagher and Hartley 2017), lead to the loss of education opportunities (Gitter and Barham 2007), and even precipitate starvation (Shoji 2010).

The literature also highlights the importance of financial access in relieving the damage caused by natural disasters. Victims need extra funds or loans to smooth consumption (Sawada and Shimizutani 2008). On a society-wide level, financial access could facilitate faster recovery of businesses and provide jobs for victims. Credit access provided by local banks plays an essential role in fulfilling the credit needs of small and mediumsized enterprises, a key sector of job recovery after natural disasters (Celil et al. 2022). In addition to banks, alternative financial services help mitigate the harm of disasters by providing funding and increasing labor participation (Becchetti and Castriota 2011).

However, because of the increased lending risk within a disaster-afflicted population (Gallagher and Hartley 2017), lenders may intentionally exclude victims from obtaining credit. For example, it is documented that banks have excluded natural disaster victims or raised their standards for lending, especially for new clients (Koetter et al. 2020). Garmaise and Moskowitz (2009) provided evidence that banks restrained their mortgage loans to customers suffering from natural disasters, especially African Americans. Residents in lower-income areas have had more difficulty obtaining financial aid and consequently have had higher bankruptcy rates (Hallegatte et al. 2020). In other words, lenders often serve disasterafflicted borrowers in a way that leaves the worst off even worse off at a time when they need the money most. As a result, the underprivileged are less likely to withstand natural disasters (Sawada and Shimizutani 2008).

## 2.2. Theoretical Background

Financial institutions’ underservice of natural disaster victims largely stems from their limited capability to handle the uncertainty caused by natural disasters. Assessing the credit risk of victims is challenging, and this is where AI can contribute. In Online Appendix A, we review the literature on the widespread use of AI in the financial industry and in the risk-scoring business in particular. In recent years, lenders have been leveraging big data on borrowers, such as data on their online purchases, daily consumption, payment histories, and social relationships, along with third-party financial data,<sup>3</sup> to assess creditworthiness. Although AI has empowered lenders to improve operational efficiency, there are debates about its impact on borrowers, especially those who are underprivileged. Some argue that AI techniques may perpetuate existing discriminative practices recorded in the training data, thereby harming vulnerable customers (Fuster et al. 2021). Others find that, because of its superior performance in predicting defaults and frauds for different types of borrowers, AI can actually enhance financial inclusiveness and expand financial services for minorities (Bartlett et al. 2022) or borrowers with short credit histories (Berg et al. 2020).

We therefore aim to answer the following question: Although AI can be a potent credit-scoring tool for discovering patterns hidden in the data, how effectively does it perform when borrowers face unexpected risks due to the shock of natural disasters?

Generally speaking, natural disasters cause unexpected financial distress to the victims. Before a natural disaster strikes, victims can hardly anticipate whether and to what extent they will suffer. Moreover, individuals’ endurance for disasters vary significantly depending on their job, financial status, personality, etc. Such unexpected uncertainties pose challenges for creditscoring models, and their performance hinges on their robustness to these changes. To an extent, natural disasters are black swan events that happen with a very small probability but with high consequences. The historical data are often dominated by nondisaster periods, so disaster-afflicted borrowers are often considered outliers, making it challenging to assess them accurately using a risk-scoring model (Kaur et al. 2019).

The scenario discussed above poses the challenge of concept drift for machine learning algorithms. A machine learning model’s predictive performance critically depends on how the training data (prior distribution) resembles the out-of-sample prediction environment (posterior distribution). A model’s performance deteriorates when there is a large divergence between the two, that is, when there is a concept drift (Widmer and Kubat 1996). Concept drift is also sometimes referred to as the “training-serving skew” (Polyzotis et al. 2017, p. 1724). There are multiple types of concept drift described in the computer science literature, including class drift (the change of class definition) and covariate drift (Webb et al. 2016).

Our study focuses on the two types of concept drift relevant to our context: (1) sampling shift driven by the change of sample (borrowers) between the training and out-of sample data (Salganicoff 1997) and (2) covariate drift, in which the feature values of users (borrowers) change across training and testing data (Webb et al. 2016). We describe below how, because of these two types of concept drift, the use of AI would benefit the underprivileged more by lowering their delinquency after a natural disaster.

2.2.1. Sampling Shift (Emergence of New Borrowers). Natural disasters could drive “new” borrowers to the lending market. The appearance of such disaster-induced borrowers would cause the sampling shift problem (Sal ganicoff 1997) in which borrowers in the testing data may be systematically different than those regular borrowers in the training data. In particular, such disaster-induced new customers may not have adequate credit history, which makes it challenging for lenders to assess their risk accurately. Simple credit-rating algorithms have been found to be inadequate when assessing the risk of such borrowers (Brevoort et al. 2016). Lenders often under serve these borrowers as a result, considering them to be of high default risk and charging them high interest or constraining their financial access (Di Maggio et al. 2021).

The use of AI may overcome this challenge by leveraging advanced algorithms and rich alternative data (Pliakos et al. 2019). For instance, when dealing with these incidental candidates with limited financial history, AI can use social media posts (Ge et al. 2017), borrowers social relationships (Lin et al. 2013), digital footprints on e-commerce platforms (Berg et al. 2020), and mobile traces (Lu et al. 2019) in their models. Such alternative data may help identify creditworthy borrowers who lack the track record to prove their acceptability to traditional lenders (Di Maggio et al. 2021). In a study of this question, Jiang et al. (2021) reported that AI-based credit scoring not only improved risk prediction on borrowers with ample credit history but also on those with limited credit records.

Because of AI’s advanced ability to leverage alternative data, it can better assess disaster-induced borrowers, who tend to be labeled as high risk by traditional algorithms. In other words, borrowers who are underserved by traditional non-AI models tend to benefit more from the use of AI credit-rating tools.

2.2.2. Covariate Drift (Change of Feature Values). Mean-Mean-while, natural disasters may cause covariate drift (Webb et al. 2016), in which the (same) borrowers change their behavioral patterns across training and prediction stages in the course of a natural disaster. When a disaster strikes and people get hurt financially, they tend to first guarantee they can meet their basic needs and reduce discretionary expenditures on luxury items such as jewels (Hallegatte et al. 2020). This observation is best summarized in the bestseller Poor Economics by Banerjee and Duflo (2011, p. 138), in which the authors provide extensive examples showing that adverse shocks hurt the poor and the rich differently: “[A] not-so-poor household … may sacrifice some cell phone minutes … . But for the poor, a large cut in income might mean [they] … cut the size of their meals at some point.” Thus, on normal days, the underprivileged spend more on basic needs (Hallegatte et al. 2020), whereas high-end borrowers are more likely to pursue discretionary loans for purposes including luxury expenditures, business expansions, or future income-generating activities (Imai and Azam 2012). During disasters, the priority of expenditures and loans shifts: both high-end and low-end borrowers still need to cover their basic necessities, although the priority level of discretionary expenditure goes down. In other words, the behaviors of low-end borrowers will remain relatively stable when affected by disasters, but the high-end borrowers’ behaviors will undergo a bigger change.

Natural disasters could potentially change borrowers behaviors, which would affect the alternative data that feed into AI credit-rating models. In particular, compared with a low-end borrower, the underlying variable distribution of a high-end borrower would likely drift more due to a disaster (e.g., change of consumption patterns). This would form a larger covariate drift within the alternative data between the training period (which often does not cover disasters) and the prediction period (when disaster happens) for the high-end borrowers. Thus, when an AI model is used, it is more likely to suffer from covariate drift (caused by disasters) and misclassify high-end borrowers. As a result, in the presence of disasters, we expect AI credit-scoring models to perform relatively better on low-end borrowers.

## 3. Research Context

Our data come mainly from a leading credit-scoring company in China (which we call Company X for anonymity purposes). The company serves over 3,000 lenders in China, covering most leading peer-to-peer (P2P) lending firms, consumer finance firms, microloan firms, and banks. It provides credit scores for over 60% of end borrowers in China through these lending firms. Its data are representative of the borrower population for the purpose of this study. Company X offers multiple tools when serving lenders, and its credit-scoring algorithm operates in two ways. First, it provides a basic credit-scoring application programming interface (API) through which lenders can query a borrower’s standard credit score upon receiving a loan application. This service is similar to the credit-reporting services provided by credit bureaus in the United States (e.g., Experian and Equifax): a borrower’s standard credit score (at a point in time) remains the same irrespective of which lender is querying. Such a standard credit score is assessed by Company X using basic features on borrowers (such as demographics and credit history) that are of general relevance to all types of lenders. The score also factors in the People’s Bank of China (PBC) credit report, which is a comprehensive report on individuals credit-related information, including their education level, address, occupation/industry, current debt level, delinquency records (for the past five years), credit/debit card ownership, and debt repayment records.

In addition, Company X provides a premier creditrating service that lets clients customize credit scores using a customized AI model jointly developed by Company X and the client. The model uses both Company X’s data and the client’s proprietary data. The service is typically carried out as a consulting project conducted by both Company X’s AI developers and the client’s data specialists. Company X has rich experience in deploying state-of-the-art AI algorithms, such as XGboost, LightGBM, and Deep Learning, in credit rating. The personalized AI model has the reputation of being superior to the standard scoring model, and it has become a main revenue source for Company X. With the model deployed, the client can then use the personalized AI credit score when processing loan applications.<sup>4</sup>

In this research, we consider the provision of the customized AI credit-rating model as an advanced AI ser vice, in contrast to the use of the standard credit-scoring API. From the top 235 clients of Company X, we identified 47 clients that eventually adopted the customized AI scoring service. We collected each lender’s implementation history of customized AI, which includes the date stamps showing when its AI model went live and every time it was upgraded. We also know the algorithms and the data sources used for feature generation for a small portion of lenders.<sup>5</sup> The features are generated from multiple data sources, including individuals’ demographics, loan application records, default records, and consumption history. Each data source may yield hundreds of features.

To understand AI’s impact on borrowers, we collected the data of 80,000 randomly sampled borrowers from Company X, including their complete credit applications and delinquency records from 2017 to 2019. The application data contain the date stamp, the type of loan (credit card, small cash loan, online/offline installment loan, auto finance, etc.), and the type of lender (bank, P2P lending, microloan, consumer finance, etc.). Additionally, we know each borrower’s age, city, and standard credit score (assessed by Company X) at the time of application, and the date of a borrower’s delinquency occurrence (reported by lenders to the PBC and aggregated by Company X). Because of confidentiality and related financial regulations, our data provider does not disclose to us the specific loan terms such as loan amount, interest rate, and maturity date. We do not know whether the lender approved a specific loan application or not, nor can we connect a delinquency record with a specific loan application.

We obtained natural disaster information from the CSMAR database, which tracks major natural disasters in China. The disaster data were extracted from the China Earthquake Administration, the China Meteorological Administration, and the Ministry of Civil Affairs of the People’s Republic of China. All natural disasters were certified by the Chinese central government. From 2017 to 2019, 672 major natural disasters occurred, grouped into 11 categories with different levels of economic damage, as shown in Figure 1. By matching the disaster region with the borrower region, we are able to identify whether an individual borrower was a victim of a disaster during a certain time period.

## 4. Modeling Borrower Delinquency: Impact of AI and Natural Disasters

Our main interest is in examining whether the use of AI in lending truly helps victims. We choose to use borrower delinquency as the main outcome measure. Delinquency reflects borrowers’ economic status: not being able to pay back a loan on time typically means that the borrower is experiencing financial difficulty at that time.<sup>6</sup> The lending literature has documented the high correlation between delinquency and an individual’s temporal change of economic status, often as a direct result of negative income shocks (Campbell and Dietrich 1983) and unemployment (Oksanen et al. 2016) or as an indirect result of illness (Lyons and Yilmazer 2005) and impaired cognitive ability (Marshall et al. 2022).

Figure 1. (Color online) Natural Disasters in China from 2017 to 2019  
![](/api/attachments/S2Z345RE/fulltext/images/bbf1ae02cc5ecb4a7cdce312b42a15e4faaca4afc476391015031551aeee2c42.jpg)

China maintains a centralized social credit system through the PBC. Delinquency and default (three consecutive delinquencies are considered a default) are reported to the PBC and remain on record for five years.<sup>7</sup> In China, a delinquency and default record can lead to severe penalties: lowered credit score, restricted access to future credit, or a ban from taking high-speed trains or flights if a person is labeled by the PBC as having “lost credibility.” Hence, rational borrowers would not want to default unless there is no choice. It is prudent to assume that an individual’s delinquency status is indicative of her economic status, and reducing delinquency is beneficial to a borrower. For these reasons, we hold that only the loans that borrowers are able to pay back are the ones that truly help victims,<sup>8</sup> representing a win–win scenario for both the borrowers and the lenders.

## 4.1. Econometrics Estimation

We employ a difference-in-differences (DID) model as the main model to identify how disaster and AI jointly affect borrowers’ delinquency. Borrowers’ applications to AI versus non-AI lenders form the basis for identify ing treated and control groups. We then examine how the differences between the two groups change following the exogenous shock of a natural disaster. Our analysis is at the individual borrower level rather than the loan level. We begin by building a two-way fixed effect model for borrower i in month t to estimate the DID effect as

$$
\begin{array}{r} Y _ {i, t + 1 \sim t + T} = \alpha + \beta_ {1} \times A I _ {i, t} + \beta_ {2} \times D i s a s t e r _ {i, t} \\ + \beta_ {3} \times A I _ {i, t} \times D i s a s t e r _ {i, t} + C t r l _ {i, t} \\ + \mu_ {i} + \theta_ {t} + \varepsilon_ {i, k}, \end{array}\tag{1}
$$

where $Y _ { i , t + 1 \sim t + T }$ denotes the dependent variable of delinquency during a T-month period after t; $A I _ { i , t }$ denotes that a borrower i is an AI borrower at time t;

Total direct economic loss (in USD Billion)  
![](/api/attachments/S2Z345RE/fulltext/images/6b328ebf995cb2a62bcbdc5de8052cc7cfadfcb3d2655cb24523384641e49b1e.jpg)

$D i s a s t e r _ { i , t }$ is a dummy indicating whether borrower i is under the shock of a natural disaster at time $t \colon C t r l _ { i , t }$ represents the control variables that are time variant, including the individual’s current delinquency status in month t and the number of applications made in month t; $\mu _ { i } ,$ and $\theta _ { t }$ denote the borrower- and time-specific fixed effects; and $\varepsilon _ { i , t }$ denotes the random noise. We take the log transformation for the count variables and cluster the standard errors at the borrower level.

Because delinquency is a delayed outcome that only occurs after loan applications, we measure $Y _ { i , t + 1 \sim t + T }$ as the number of months a borrower is in delinquent status during $[ t + 1 , t + T ]$ , as shown in Figure 2 (e.g., if a borrower is delinquent within two out of T months, the measure is two). For a clearer identification that precludes double counting in the case of one individual experiencing multiple disasters, we focus on the borrowers who endured only one disaster within a 2T period around t. We construct $A I _ { i , t }$ to denote whether user i applied for a loan from an AI lender among the multiple applications made at time t. If the user’s applications are all to lenders not adopting the AI creditrating tool, the measure is zero, and otherwise it is one. Under this definition, only AI borrowers can receive loans from AI lenders (and possibly from non-AI lenders as well), whereas non-AI borrowers cannot get a loan from AI lenders. By contrasting AI borrowers’ with non-AI borrowers’ outcomes, we are able to tease out the impact of AI on borrower delinquency under the impact of disasters.

Furthermore, we differentiate high-end and low-end borrowers based on their credit scores provided by Company X and examine the moderation effect as follows:<sup>9</sup>

$$
\begin{array}{l} Y _ {i, t + 1 \sim t + T} = \alpha + \beta_ {1} \times A I _ {i, t} + \beta_ {2} \times D i s a s t e r _ {i, t} \\ \quad + \beta_ {3} \times A I _ {i, t} \times D i s a s t e r _ {i, t} + \beta_ {4} \times H i g h - S c o r e _ {i, t} \\ \quad \times A I _ {i, t} + \beta_ {5} \times H i g h - S c o r e _ {i, t} \times D i s a s t e r _ {i, t} \\ \quad + \beta_ {6} \times H i g h - S c o r e _ {i, t} \times A I _ {i, t} \times D i s a s t e r _ {i, t} \\ \quad + C t r l _ {i, t} + \mu_ {i} + \theta_ {t} + \varepsilon_ {i, k}, \end{array} \tag {2}
$$

where $H i g h – S c o r e _ { i , t }$ denotes whether the standard credit score of customer i is above 600 in month $t . ^ { 1 0 }$ Generally speaking, credit score is correlated with one’s socioeconomic status, such as income, employment, and education (Israel et al. 2014). According to a study by the Federal Reserve, household income is significantly correlated with consumers’ credit scores (Beer et al. 2018).

Figure 2. (Color online) Model Setup  
![](/api/attachments/S2Z345RE/fulltext/images/e636431bba93d63fa7d3670571e078780bc27326f1f3d2421f4de531f56de253.jpg)

Thus, this analysis can tell us the effect of AI on customers with different socioeconomic statuses.

## 4.2. Addressing Endogeneity

In our study, disaster is undoubtedly exogenous. However, endogeneity may stem from the AI variable. One may argue that firms adopt AI tools because of unobserved characteristics that are correlated with the erro term; for example, a higher default rate prompts a firm to adopt AI. However, because our analysis is on borrowers, a firm’s AI choice should not directly affect our identification of borrower behavior because firms do not disclose whether they adopt AI. However, selfselection at the borrower level is plausible. For example, AI lenders may process loans faster, and some borrowers may prefer applying for loans from such lenders, giving rise to endogeneity.

We first employ the coarsened exact matching (CEM) method (Iacus et al. 2012) to mitigate these endogeneity concerns. CEM is widely adopted to reduce the imbalance between control and treatment groups and thus mitigate self-selection. We follow Stuart (2010) and use a borrower’s number of applications in the last month, age, and gender as matching variables. The multivariate L1 distance is significantly reduced (from 0.129 down to 0.029, as reported in Table A2 in Online Appendix C), indicating the effectiveness of matching.

Furthermore, we employ an instrumental variable (IV) approach to address other sources of endogeneity. For example, there might exist unobservable factors, such as promotions by a low-interest AI lender or borrower preference for tech-savvy lenders, that may affect both a borrower’s decision to apply for a loan from an AI lender and their delinquency likelihood. We specifically construct two IVs:

1. the ratio of borrowers to AI firms among all other users in the same city as the focal user i, that is, $A I \_ R a t i o _ { i , t }$ $= \mid O A ( i , t ) \mid / \mid O B ( i , \dot { t } ) \mid$ , where OA(i, t) represents the set of borrowers from AI firms in the same city excluding i in $t ,$ and $O B ( i , t )$ represents all borrowers in the city of i in t;

2. the average ratio of applications to AI firms for all users in the same city as the focal user i, that ${ \mathrm { i } } s ,$ $\begin{array} { r } { A I \_ A v e r a g e _ { i , t } = \sum _ { k } ^ { O B ( i , t ) } ( \# A I \ A p p l i c a t i o n s _ { k , t } / \# A l l \ A p p l i c a t i o n s _ { k , t } ) / } \end{array}$ |OB(i, t)|:

As borrowers in the same city may have mutual influence on each other or may be influenced by the same marketing efforts and geographical or socioeconomic factors, the two IVs should be correlated with $A I _ { i , t } .$ . However, because of the financial independence of individuals, other borrowers’ delinquency will unlikely be directly correlated with the focal borrower’s delinquency. We test the statistical properties of these IVs. The results lend support to their validity: the Kleibergen–Paap rk Langrange-multiplier statistic is 214.014, passing the underidentification test; the Hansen J statistic is 3.335, passing the overidentification test; and the Wald F statistic is 27.626, passing the weak IV test.

We also consider the Heckit approach, kernel propensity score matching (PSM), and the doubly robust DID (DR-DID) estimator (Sant’Anna and Zhao 2020) to strengthen identification, and we elaborate on these results in the robustness check section.

## 5. Results

## 5.1. Summary Statistics and Model-Free Evidence

Among the clients of Company X, 47 lenders adopted the customized AI credit-rating service by the end of our data collection period. The left panel of Figure 3 displays the change in the number of AI lenders versus regular lenders: the AI adoption rate gradually increased and sped up after April 2019. The never-adopters may be systematically different from the AI adopters. To reduce such potential self-selection, we focus on the borrowers of these 47 firms that eventually adopted AI in our analysis, following the gist of look-ahead propensity score matching (Bapna et al. 2018). We also contrast the earlier-treated units with the later-treated units as recommended by Baker et al. (2022). The 47 lenders received 1,151,761 loan applications from a total of 59,919 borrowers.

We construct a borrower-month panel on these 59,919 borrowers and report the summary statistics in Table 1. The average credit score of these borrowers is 567 (ranging from 300 to 991), slightly tilted toward lowend borrowers. Also, 73.7% of the borrowers are male, with an average age of 31.8. On average, there is 1% chance that a borrower will encounter a natural disaster in a given month. Each borrower makes an average of 2.029 applications per month, where 65.6% of the applications are made to AI-empowered lenders.

The right panel of Figure 3 illustrates the change in the average of the AI variable (dotted line) and the average ratio of applications to AI firms (the solid line) over time. On average, each borrower has a 2% probability of being delinquent within a month, which increases over time to 2.7% three months after application. For our dependent variable that counts delinquency within three months of a focal observation, the value is about 0.07. In Table A1 in Online Appendix B, we further break down these descriptive statistics by contrasting AI versus non-AI and disaster versus nondisaster borrowers. We observe largely consistent demographic characteristics (similar gender, age, etc.) across subgroups.

Figure 3. (Color online) The Use of Customized AI Credit Rating Services  
![](/api/attachments/S2Z345RE/fulltext/images/ab524c50b69812f22bdeecfc45595d1f5a4ef9569e292775251b4d0da0ff358f.jpg)

Figure 4 visualizes the contrast between borrowers from disaster-affected regions and those from disasterfree regions (within the same province at around the same time) and with versus without applications to AI-empowered lenders in terms of delinquency. The xaxis of the graph indexes the relative time (between the time of an application and a disaster; e.g., t + 3 indicates that these applications arrived three months after the disaster). Figure 4 shows that the four curves exhibit a similar trend three months before and three months after a disaster (i.e., the period of [�3, 3]). However, they diverge three months after the disaster, showing a delayed effect on delinquency. Specifically, without AI, disaster-impacted borrowers would have more delinquencies than disaster-free borrowers (the two single lines). The fact that the two double lines are located below the two single lines in the long run (after six months following a disaster) presents model-free evidence that AI helps reduce delinquency, even more so for disaster-hit borrowers. Next, we examine these phenomena with rigorous econometrics analyses.

## 5.2. DID Results

Table 2 reports the DID estimation results, where columns (1) and (2) display the fixed effect models, columns (3) and (4) represent the IV estimation results, and columns (5) and (6) show the results using IVs and CEM. The CEM + IV model is our main model of interest.

To ensure the validity of the DID model, we test the parallel trend by contrasting borrower applications to AI versus non-AI lenders and contrast applications from disaster-afflicted versus disaster-free borrowers, as reported in Online Appendix D. The results confirm that the parallel trend assumption holds.

![](/api/attachments/S2Z345RE/fulltext/images/d485080b2f8a6db3272f5afd947a4bb4af815fa8723ef23114761e63e410cb0e.jpg)

Table 1. Descriptive Statistics

<table><tr><td>Variable</td><td>Obs.</td><td>Mean</td><td>Std. dev.</td><td>Min</td><td>Max</td></tr><tr><td>Credit  $Score_{i,t}$ </td><td>59,358</td><td>567.519</td><td>125.772</td><td>300</td><td>991</td></tr><tr><td> $Gender_{i,t}$ </td><td>59,547</td><td>0.737</td><td>0.440</td><td>0</td><td>1</td></tr><tr><td> $Age_{i,t}$ </td><td>59,547</td><td>31.803</td><td>7.363</td><td>20</td><td>69</td></tr><tr><td> $Disaster_{i,t}$ </td><td>59,547</td><td>0.010</td><td>0.053</td><td>0</td><td>1</td></tr><tr><td> $Applications_{i,t}$ </td><td>59,547</td><td>2.029</td><td>1.321</td><td>1</td><td>17.857</td></tr><tr><td> $AI_{i,t}$ </td><td>59,547</td><td>0.656</td><td>0.302</td><td>0</td><td>1</td></tr><tr><td> $Delinquency_{i,t}$ </td><td>59,547</td><td>0.020</td><td>0.093</td><td>0</td><td>1</td></tr><tr><td> $Delinquency_{i,t+1}$ </td><td>58,866</td><td>0.022</td><td>0.098</td><td>0</td><td>1</td></tr><tr><td> $Delinquency_{i,t+2}$ </td><td>58,167</td><td>0.024</td><td>0.105</td><td>0</td><td>1</td></tr><tr><td> $Delinquency_{i,t+3}$ </td><td>57,257</td><td>0.027</td><td>0.112</td><td>0</td><td>1</td></tr><tr><td> $Y_{i,t+1\sim t+3}$ </td><td>57,257</td><td>0.070</td><td>0.301</td><td>0</td><td>3</td></tr></table>

Note. Obs., Observations; Std. dev., standard deviation.

Overall, our regression results show that disasters increase delinquencies, which is aligned with our intuition. In addition, the main effect of AI is generally insignificant or negative, suggesting that the use of AI itself does not increase delinquency. Our main interests in Table 2 are the interaction terms between disaster and AI and the three-way interaction between disaster, $\operatorname { A I } ,$ and high score (indicating above or below 600). Interestingly, AI exhibits a significant impact on delinquency during disasters. For example, in column (5), the coefficient $- 0 . 0 2 7 \left( p < 0 . 0 5 \right)$ suggests that adopting AI would reduce delinquency by $2 . 7 \% ( = 1 - \mathrm { e } ^ { - 0 . 0 \dot { 2 } 7 } )$ under disasters, which fully offsets disasters’ adverse impact (coefficient � 0.021, p < 0.05). This finding that AI mitigates disaster’s unfavorable impact on delinquency is consistent across all the models.

The three-way interaction shows up as positive and marginally significant (e.g., coefficient $= - \bar { 0 } . 0 4 5 , p < 0 . 1$ in column (6)), showing that AI’s mitigating effect on disaster is stronger for low-score borrowers. To better interpret the three-way effects, we opt to visualize the joint effects in Figure 5. There, we compare the four scenarios by mixing the conditions of AI and disaster for high-score and low-score borrowers against the baseline case: no-AI, no-disaster low-score borrowers. The y-axis shows the percentage of change in delinquency, with a lower value preferred. We observe the following:

1. Natural disasters hit the underprivileged (lowscore) borrowers harder, regardless of AI. Low-end borrowers have a significant delinquency increase (about 2.8%).

2. After lenders implement AI, the two lines appear below the corresponding no-AI lines, implying that the use of AI helps reduce delinquency.

3. With the help of AI, low-end borrowers incur a higher gain relative to high-end customers. Their delinquencies decrease after disasters (by about 1%). The delinquencies among high-end customers applying to AI-empowered lenders increase by roughly 3.5% after the shocks of natural disasters. Compared with the no-AI disaster case, AI mitigates the potential delinquency of low-end (high-end) borrowers by 3.9% (2.9%). This implies that the mitigating role of AI is accentuated for underprivileged customers when it comes to disaster relief.

In addition to the three-way interaction, we also conduct subsample analysis on high-score and low-score borrowers separately under the joint impact of AI and disasters. Online Appendix E, Section E.9, shows that our findings still hold: low-score borrowers benefit more from AI. Moreover, we test for how long AI’s mitigation effect may last in Online Appendix E, Section E.10. Results show that the effect gradually increases until six months after a disaster and then stabilizes afterward.

## 5.3. Robustness Checks

We conduct a series of analyses to ensure the robustness of our findings. First, delinquency may exhibit path dependence, that is, serial correlation over time. DID estimates may be biased in the presence of serial correlation (Bertrand et al. 2004). We follow the methods proposed by Bertrand et al. (2004) to account for serial correlation, with the results in Online Appendix E, Section E.1. The adjustment of the standard error and the two-step estimation both yield consistent results.

Second, we replace CEM with a kernel PSM approach. PSM is widely used to account for self-selection bias.

Figure 4. (Color online) Delinquency Rates After Disasters  
![](/api/attachments/S2Z345RE/fulltext/images/142bc81228ef66b4737372ad8d26067db2712ed0153fb9cd5a6a7d2326c5a720.jpg)

Table 2. AI and Borrowers’ Delinquency in Disasters

<table><tr><td>T = 3</td><td>(1) FE</td><td>(2) FE</td><td>(3) IV</td><td>(4) IV</td><td>(5) CEM + IV</td><td>(6) CEM + IV</td></tr><tr><td> $Disaster_{i,t}$ </td><td>0.008**(0.004)</td><td>0.010**(0.004)</td><td>0.018**(0.009)</td><td>0.025**(0.01)</td><td>0.021**(0.009)</td><td>0.028**(0.011)</td></tr><tr><td> $AI_{i,t}$ </td><td>-0.002**(0.001)</td><td>0.000(0.001)</td><td>-0.010(0.034)</td><td>-0.033*(0.019)</td><td>-0.011(0.036)</td><td>-0.037(0.024)</td></tr><tr><td> $Disaster_{i,t} \times AI_{i,t}$ </td><td>-0.009**(0.004)</td><td>-0.012**(0.005)</td><td>-0.025**(0.012)</td><td>-0.035**(0.015)</td><td>-0.027**(0.013)</td><td>-0.038**(0.015)</td></tr><tr><td> $High-Score_{i,t} \times Disaster_{i,t} \times AI_{i,t}$ </td><td></td><td>0.017*(0.01)</td><td></td><td>0.042*(0.025)</td><td></td><td>0.045*(0.025)</td></tr><tr><td> $High-Score_{i,t} \times Disaster_{i,t}$ </td><td></td><td>-0.010(0.008)</td><td></td><td>-0.026(0.018)</td><td></td><td>-0.028(0.018)</td></tr><tr><td> $High-Score_{i,t} \times AI_{i,t}$ </td><td></td><td>-0.009***(0.001)</td><td></td><td>-0.029***(0.003)</td><td></td><td>-0.035***(0.005)</td></tr><tr><td> $High-Score_{i,t}$ </td><td></td><td>0.007***(0.001)</td><td></td><td>0.019***(0.002)</td><td></td><td>0.026***(0.003)</td></tr><tr><td> $Applications_{i,t}$ </td><td>-0.006***(0.001)</td><td>-0.006***(0.001)</td><td>-0.005(0.004)</td><td>-0.001(0.002)</td><td>-0.005(0.004)</td><td>-0.001(0.003)</td></tr><tr><td> $Delinquency_{i,t}$ </td><td>1.383***(0.008)</td><td>1.382***(0.008)</td><td>1.384***(0.009)</td><td>1.383***(0.009)</td><td>1.363***(0.009)</td><td>1.363***(0.009)</td></tr><tr><td>Constant</td><td>0.036***(0.001)</td><td>0.034***(0.001)</td><td></td><td></td><td></td><td></td></tr><tr><td>Borrower FEs</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time FEs</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>399,751</td><td>398,603</td><td>380,119</td><td>379,037</td><td>352,199</td><td>351,312</td></tr><tr><td> $R^2$ </td><td>0.682</td><td>0.682</td><td>0.448</td><td>0.442</td><td>0.443</td><td>0.435</td></tr><tr><td>Wald F statistic</td><td></td><td></td><td>26.926</td><td>42.682</td><td>22.342</td><td>27.626</td></tr><tr><td>Hansen J statistic</td><td></td><td></td><td>1.089</td><td>2.902</td><td>0.700</td><td>3.335</td></tr></table>

Note. FE, Fixed effect. Standard errors are in parentheses.  
\* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01.

Recently, it was suggested that PSM may prune out too many observations, and these dropped observations may be systematically different from the remaining matched observations (King and Nielsen 2019). Furthermore, PSM may not always reduce covariate imbalance, and therefore CEM or kernel PSM are recommended as alternative matching approaches (King and Nielsen 2019). Thus, we implement kernel PSM and report the results in column (1) of Table A7 in Online Appendix E, and these results are consistent with our main model.

Figure 5. (Color online) Joint Impact of Disaster, AI, and Credit Score on Borrowers’ Delinquency  
![](/api/attachments/S2Z345RE/fulltext/images/81acdd0ee72ac1bd4af88f3184b43a277f0be3ee3845a613708f9c2d956087e6.jpg)

Third, our main model defines AI as whether a borrower makes loan applications to AI lenders at month t. It would be interesting to investigate the effect when a borrower switches to AI lenders for the first time. Thus, we alter the AI measure to indicate whether the focal borrower has ever applied for a loan from any AI lenders until time t. As reported in column (2) of Table A7, the results are qualitatively consistent with our main model, yet with slightly larger coefficients. We also construct two new measures of AI: (1) AI Ratio, which is the ratio of applications made to AI-empowered lenders among all the applications of a borrower, and (2) AI Only, indicating whether the borrower applied for only AI-empowered loans. The results, reported in columns (3) and (4) of Table A7, are consistent.

Fourth, one may be concerned that delinquency can be caused by loans made before the borrower experienced a natural disaster. To address this, we conduct a subsample analysis on borrowers who only made applications within three months after a disaster. After CEM matching with borrowers uninfluenced by disasters as the control group, we arrive at a consistent conclusion on AI’s mitigation effect as shown in column (5) in Table A7.

Fifth, we adjust the threshold for labeling high-/lowend customers and the delinquency time window. We experiment with credit score cutoffs of 550 and 650 and report the results in columns (6) and (7) of Table A7. The results are consistent. Our model-free evidence suggests that delinquency outcomes may take longer than three months to manifest. Accordingly, we prolong the delinquency window (T) from three months to six months to capture the longer-term effect. Column (8) of Table A7 shows largely consistent results. In column (9) of Table A7, we further change the model to a quarterly level, which generates consistent results.

Sixth, to show that firms are unlikely to self-select AI as a function of the variables of our interest, we conduct a firm-level analysis by regressing a firm’s AI adoption on disaster, credit score, and several control variables as reported in Section E.8 of Online Appendix E. This is essentially the first stage of the Heckit model. The result shows that the coefficients of disaster and credit score are insignificant, suggesting firms do not choose AI based on disaster or credit score.

Seventh, we employ the Heckit approach to address possible borrower self-selection of AI lenders (Heckman 1979). We first model borrowers’ binary choices of applying to AI lenders, $A I _ { i , \mathrm { t } } ,$ with explanatory variable $\bar { Z _ { i , t } } ,$ from which we estimate the inverse Mills ratio (IMR) to be included in the second stage of the model. The Heckit model requires that variable $Z _ { i , t }$ affect the dependent variable only through $I M R _ { i , t }$ (i.e., the exclusion restriction). We use the two instrument variables $A I \_ R a t i o _ { i , t }$ and AI\_Average<sub>i,t</sub> as $Z _ { i , t } .$ . These variables may be correlated with $A I _ { i , t }$ but will not be directly correlated with the dependent variable because they do not reflect the individual’s financial status. Column (10) of Table A7 reports the estimation under this specification, which yields results consistent with our main model.

Last, we implement a DR-DID estimator as recommended by Baker et al. (2022, p. 394) for a staggered DID setting. This estimator requires only that either the propensity score matching model or the outcome regression model (but not both) is correctly specified, thus rendering a doubly robust estimation (Sant’Anna and Zhao 2020). For simplicity, we adopt the canonical two-by-two DID setting and reconfigure the model to be at the quarterly level on borrower–disaster pairs for each (independent)

disaster event, with borrowers uninfluenced by disasters as the control group.

Table 3 reports the average treatment effect on the treated (ATT) of DR-DID for the treatment of natural disasters. We conduct a subsample analysis to compare the effect on AI and non-AI borrowers. The first three columns together show that natural disasters would increase delinquency, and the effect is more pronounced on non-AI borrowers compared with AI borrowers. In other words, AI mitigates the unfavorable impact of disasters on borrowers. Furthermore, contrasting the results in columns (4) and (6) against those in columns (5) and (7) shows that AI’s mitigating effect is stronger on low-score borrowers: whereas column (6) (AI) shows a much smal ler treatment effect than column (4) (non-AI) on low-score borrowers, such a mitigating effect is not observed (col umn (5) versus (7)) for the high-score borrowers. In summary, the findings in Table 3 lend further support to the findings of our main model.

## 5.4. Evidence on Mechanisms

When theorizing our research questions, we anticipated that the differential impacts of AI on low-end and highend borrowers during natural disasters could be (partially) caused by sampling shift and covariate drift. Below we present empirical evidence on these phenomena.

5.4.1. Sampling Shift. To show the existence of sampling shift, we first examine whether disasters drive new customers into the lending market, and we do this using two measures: tenure and historical applications. The tenure of a borrower measures the number of days the borrower has been in the lending market, and the historical applications measure captures the number of applications the borrower has made in the past. Both measures approximate a customer’s credit history. If new customers are entering the lending market, we would expect the values of both measures to go down.

Table 4 reports the regression results with the two measures as the dependent variables. It shows that borrowers who have experienced natural disasters have significantly shorter customer tenure $( - 1 . 3 \% , p < 0 . 0 1 )$ and fewer applications in the past $( - 1 . 1 \% , p < 0 . 0 1 ) .$ lending support to the argument that disasters propel new and less experienced applicants to apply for loans.

Table 3. DR-DID Estimation of Disaster’s Impact on Borrowers’ Delinquency

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td rowspan="2">(4) Non-AI, low score</td><td rowspan="2">(5) Non-AI, high score</td><td rowspan="2">(6) AI, low score</td><td rowspan="2">(7) AI, high score</td></tr><tr><td>Treatment = Disaster</td><td>All</td><td>Non-AI</td><td>AI</td></tr><tr><td>ATT</td><td>0.0119***(0.003)</td><td>0.0183***(0.006)</td><td>0.0098***(0.003)</td><td>0.0232***(0.009)</td><td>0.0098*(0.006)</td><td>0.0086**(0.004)</td><td>0.0129***(0.005)</td></tr><tr><td>Observations</td><td>329,446</td><td>94,810</td><td>234,636</td><td>58,636</td><td>35,984</td><td>179,376</td><td>55,028</td></tr></table>

Note. Standard errors are in parentheses.  
\* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01.

Table 4. Disasters Bring in “Unprepared” Applicants

<table><tr><td></td><td>(1)Tenure</td><td>(2)Historical applications</td></tr><tr><td> $Disaster_{i,t}$ </td><td>-0.013***(0.004)</td><td>-0.011***(0.004)</td></tr><tr><td>Constant</td><td>0.995***(0.000)</td><td>1.31***(0.000)</td></tr><tr><td>Borrower FEs</td><td>Yes</td><td>Yes</td></tr><tr><td>Time FEs</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>2,492,084</td><td>2,492,084</td></tr><tr><td> $R^2$ </td><td>0.791</td><td>0.830</td></tr></table>

Note. Standard errors are in parentheses.  
\* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01.

Second, we investigate whether these borrowers motivated by disaster respond to AI lenders differently than the other borrowers (referred to as regular borrowers). Specifically, those who apply only after disasters are referred to as disaster-induced borrowers and form our treated group, whereas the regular borrowers constitute the control group. Because the two groups may systematically differ in demographics, we conduct CEM to ensure these covariates are as close as possible in order to isolate the effect we are interested in. Column (1) of Table 5 shows that the three-way interaction has a marginally significant and negative coefficient $( - 0 . 0 7 3 , p < 0 . 1 0 )$ , meaning that disaster-induced borrowers benefit more from AI: their delinquency increase is lower than that of regular borrowers. As discussed in Section 2.3.1, AI solutions tend to have a higher ability to tackle the sampling shift challenge. This finding lends support to our argument.

5.4.2. Covariate Drift. To demonstrate the existence of covariate drift, we directly compare the training data with the out-of-sample data constructed from the applications made within 30 days after a natural disaster. For simplicity, we assume that the lender constructs its training data using the most recent one-year customer data. The difference between the training and out-ofsample data is measured by the multivariate L1 distance. The variables we use to compute the distance include age, gender, the number of defaults in the past, and the number of applications in the past. As shown in Figure 6(a), the divergence goes up as credit scores increase. In other words, during disasters, the applications of high-end borrowers change more.

Figure 6. (Color online) Covariate Drift Caused by Disasters  
![](/api/attachments/S2Z345RE/fulltext/images/97a5ce8d6f46a9add56342e9508eaf6892021763b1df4ab60566edf780b7f23d.jpg)

Table 5. AI Impact on Different Types of Borrowers

<table><tr><td></td><td>(1) Disaster induced</td><td>(2) Extra funding</td></tr><tr><td> $Disaster_{i,t}$ </td><td>-0.027 (0.017)</td><td>0.032*** (0.011)</td></tr><tr><td> $AI_{i,t}$ </td><td>0.020 (0.112)</td><td>-0.022 (0.035)</td></tr><tr><td> $Disaster_{i,t} \times AI_{i,t}$ </td><td>0.037 (0.023)</td><td>-0.045*** (0.016)</td></tr><tr><td> $Borrower Type_{i,t} \times Disaster_{i,t} \times AI_{i,t}$ </td><td>-0.073** (0.032)</td><td>0.044* (0.025)</td></tr><tr><td> $Borrower Type_{i,t} \times Disaster_{i,t}$ </td><td>0.052** (0.025)</td><td>-0.025 (0.018)</td></tr><tr><td> $Borrower Type_{i,t} \times AI_{i,t}$ </td><td>0.006 (0.024)</td><td>0.005 (0.006)</td></tr><tr><td> $Borrower Type_{i,t}$ </td><td>-0.010 (0.018)</td><td>-0.001 (0.004)</td></tr><tr><td> $Applications_{i,t}$ </td><td>-0.008 (0.014)</td><td>-0.004 (0.004)</td></tr><tr><td> $Delinquency_{i,t}$ </td><td>1.490*** (0.041)</td><td>1.363*** (0.009)</td></tr><tr><td>Observations</td><td>36,177</td><td>352,199</td></tr><tr><td> $R^2$ </td><td>0.592</td><td>0.442</td></tr><tr><td>Wald F statistic</td><td>0.586</td><td>11.459</td></tr><tr><td>Hansen J statistic</td><td>6.27</td><td>5.496</td></tr></table>

Note. Standard errors are in parentheses  
\* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01.

Furthermore, we look into the change in loan types (auto finance, credit card, and small cash loans). Figure 6(b) reports the ratio of the three types of loans subject to a disaster’s influence (i.e., applications made within a month after a disaster) against those made during a disaster-free period. We observe that higher-score borrowers tend to apply for fewer cash loans but more credit card and auto finance loans. However, when natural disasters strike, the increase in cash loan applications, which are more likely to be used for necessities, is more substantial among higher-score borrowers, especially those with scores between 600 and 750. In other words, high-end borrowers tend to have a higher covariate drift than low-end borrowers.

![](/api/attachments/S2Z345RE/fulltext/images/a013f6fa3751ea6b6ac74b377efa156e91e21b73ba31b293b197b8c035b0fc07.jpg)

## 6. Discussion

The above analyses demonstrate the presence of a heterogeneous effect of AI’s mitigating role on different segments of borrowers. But might this heterogeneous effect be an artifact of the credit score measure? Might it be due to lenders’ manipulation of loan approvals, for example, achieving a lower default rate by deliberately rejecting low-score borrowers? And what characteristics of AI may lead to such heterogeneous effects? We discuss these issues in this section.

## 6.1. Borrower Heterogeneity

We first discuss different sources of borrower heterogeneity, examining three factors. First, borrowers’ reliance on commercial credit depends on their economic environment. Better developed regions tend to have more credit sources that can fulfill borrowers’ credit needs. When a natural disaster strikes such a region, there will be fewer disaster-induced borrowers, rendering the sampling shift smaller. By the same token, covariate drift would be expected to be smaller in such regions. Thus, we expect a smaller benefit of AI in neutralizing disasters in developed regions. In Figure A2 in Online Appendix F, we illustrate AI’s heterogeneous mitigating effect based on the economic status of the regions borrowers reside in. We split the sample into three strata based on a region’s gross domestic product (GDP) per capita. The figure shows that AI does have the highest impact in the least developed regions (with the lowest GDP). The complete discussion can be found in Online Appendix F, Section F.1.

Second, the accessibility of government disaster-relief funds may confound our findings. Such funds are critical to the employment and economic recovery of a region (Gallagher et al. 2022). Borrowers in regions with adequate government relief funds may not need to apply for commercial loans. Here, we leverage a special disaster-relief program in China to examine the effect of government funding on our findings. In 2007, the Chinese government launched a program called the National Disaster Resistant Demonstration Commu-$\mathrm { \ n i t y ^ { 1 1 } }$ to provide selected regions with extra funds for disaster relief (World Bank 2020). Thus, these regions would be more resilient to disaster shocks, and we expect a smaller mitigating effect of AI on these regions. We are able to identify the counties covered by the program using the data from the Ministry of Emergency Management. Column (2) of Table 5 shows that the coefficient of the three-way interaction is positive (coefficient $= 0 . 0 4 4 , p < 0 . 1 )$ , indicating that the mitigating effect of AI in regions with such government funding is less pronounced under the impact of disasters (likely because of borrowers’ reduced reliance on commercial loans). The complete discussion can be found in Online Appendix F, Section F.2. There we also present evidence that government funding is often insufficient for individuals to recover from the damage caused by disasters and that commercial loans play a significant role in providing the needed financial support (Celil et al. 2022), which forms the basis for this study.

Third, people of different ages may have different levels of credit needs, which would moderate the role of AI. We report AI’s mitigating effect across age groups in Figure A3 in Online Appendix F. Interestingly, AI’s impact exhibits a U shape, where the age groups between 26 and 45 years yield the largest gain (biggest reduction in terms of delinquency rate), and the indebtedness ratio peaks around age 35. This result indicates that age groups with more need for commercial credit would benefi more from AI during disasters. The complete discussion is available in Online Appendix F, Section F.3.

## 6.2. Loan Approval, Delinquency, and Invisible Primes

We then rule out the alternative explanation that the lowered delinquency rate might be a result of simply rejecting more loan applications from low-score borrowers. Because of the lack of loan approval information, we are unable to verify this directly. We therefore take two measures to examine this possibility. First, we use a heuristic that the number of loan applications in the near future should go down if a loan has been approved. The results, reported in Online Appendix G, Section G.1, show that the number of applications drops when AI is involved. Second, we manage to obtain a small sample that contains loan approval information. This sample provides some direct evidence that the use of AI does not lead to a reduction in loan approval rate (see Online Appendix G, Section G.2), falsifying this alternative explanation.

Then how does AI help reduce delinquency in our context? AI’s ability to identify the invisible primes among low-end borrowers has been documented as a major reason (Di Maggio et al. 2021). In a highly competitive lending market, being able to expand one’s business to a larger spectrum of customers is key to survival (Clemons and Thatcher 2008). AI’s superior risk-scoring ability enables lenders to identify the hidden gems in the uncertain area (e.g., customers with little history) and thus helps expand lenders’ business to lower-income and lesseducated populations (Lu et al. 2019). AI lenders are also able to provide more competitive interest rates than traditional lenders (Di Maggio et al. 2021).

The occurrence of natural disasters complicates the efficacy of credit-scoring models. High-end customers tend to have stable jobs, high incomes, and more savings. Even when they temporarily run late in repaying a loan because of a disaster, this segment of borrowers has a higher chance of recovering and being able to pay back in the long run. Statistically speaking, when a lender serves high-end borrowers, the cost of type I error (rejecting good borrowers) looms larger than that of type II error (accepting bad borrowers). Conversely, the cost of type II error would be higher than that of type I error for a lender serving low-end borrowers. Thus, lowering the delinquency and default rate of lowend borrowers is more critical for lenders. This incentivizes lenders to adopt AI to discern invisible primes.

## 6.3. AI’s Use of Alternative Data

We argue that the enhanced ability of AI is partially due to the high-dimensional features generated from using alternative data. We provide direct evidence of this. In column (11) of Table A7 in Online Appendix E, we first examine the impact of the number of feature categories (i.e., the different data sources used in feature generation) on borrower delinquencies. The results confirm that AI’s mitigating effect is stronger when more features are used, and the low-end borrowers benefit even more in such cases.

Next, we examine which types of features matter more in reducing delinquency. The four high-level feature categories (identity certification, loan applications, default history, and consumption behavior) yield a total of 15 potential combinations that can be used in a model. In Online Appendix H, we show that AI’s mitigating effect is consistently more pronounced whenever the consumption behavior data are used. The consumption data are considered to be a major type of alternative data (Hong Kong Applied Science and Technology Research Institute 2020) that provide a different lens on a borrower than data on their financial status. To examine the importance of the consumption data, we reconstruct the AI variable based on whether the consumption data were used in an AI lender’s credit-scoring model and then re-estimate our models. Without using the consumption data in the model, the low-end borrowers no longer benefit from AI (insignificant three-way interaction term in column (1) of Table 6), whereas this coefficient (coefficient � 0.149, p < 0.05) turns significant and positive when the consumption data are used (see column (2)). These results provide evidence that the use of alternative data are one potential reason for AI’s heterogeneous mitigating effects, as we discussed in Section 2.3.

## 7. Conclusion

This research note investigates whether lenders’ use of AI benefits borrowers by reducing their delinquency in the aftermath of a natural disaster. Intriguingly, we find that low-end borrowers with relatively lower credit scores benefit more. The same effect is found among borrowers who live in underdeveloped regions, lack access to government relief funds, or are in the 26–45 age group with a high credit need. We show that this effect is likely due to AI’s efficacy in credit scoring (e.g., by leveraging alternative data) and its ability to deal with sampling shift and covariate drift caused by natural disasters.

Our research provides immediate implications for policy makers and managers. First, our findings suggest that lending companies should consider deploying advanced AI models when handling loan applications from disaster-hit borrowers. AI’s ability to reduce delinquency and default can lead to a win–win outcome for both len ders and borrowers. Second, this study informs policy makers on how to better respond to disasters by providing differentiated disaster-relief services to different types of victims. Those with limited repayment ability should not be dependent on commercial loans, and, if possible, their credit needs should first be covered by government funds and charities. However, commercial loans can be a win–win choice for the segment of invisible primes (Di Maggio et al. 2021). Our study shows that AI can make such market segmentation possible, demonstrating the strategic value of AI in disaster management and echoing the theme of this special issue (Abbasi et al. 2021). Third, our findings highlight the importance of corporate social responsibility (Wikipedia 2022) in the disaster management context. Lenders should not simply turn away from borrowers driven by natural disasters,

Note. Standard errors are in parentheses.

\* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01.

Table 6. AI’s Mitigation Effect by AI Type

<table><tr><td></td><td>(1) AI = model without alternative data</td><td>(2) AI = model with alternative data</td></tr><tr><td> $Disaster_{i,t}$ </td><td>0.022 (0.018)</td><td>0.009** (0.004)</td></tr><tr><td> $AI_{i,t}$ </td><td>-0.009 (0.017)</td><td>0.274* (0.148)</td></tr><tr><td> $Disaster_{i,t} \times AI_{i,t}$ </td><td>-0.034 (0.034)</td><td>-0.037*** (0.013)</td></tr><tr><td> $High-Score_{i,t} \times Disaster_{i,t} \times AI_{i,t}$ </td><td>0.063 (0.045)</td><td>0.149** (0.068)</td></tr><tr><td> $High-Score_{i,t} \times Disaster_{i,t}$ </td><td>-0.034 (0.024)</td><td>-0.010 (0.007)</td></tr><tr><td> $High-Score_{i,t} \times AI_{i,t}$ </td><td>-0.021*** (0.004)</td><td>0.063 (0.079)</td></tr><tr><td> $High-Score_{i,t}$ </td><td>0.009*** (0.002)</td><td>-0.006 (0.008)</td></tr><tr><td> $Applications_{i,t}$ </td><td>-0.006*** (0.002)</td><td>-0.036** (0.017)</td></tr><tr><td> $Delinquency_{i,t}$ </td><td>1.307*** (0.011)</td><td>1.369*** (0.012)</td></tr><tr><td>Borrowers</td><td>42,283</td><td>46,140</td></tr><tr><td>Observations</td><td>285,969</td><td>379,037</td></tr><tr><td> $R^2$ </td><td>0.419</td><td>0.292</td></tr></table>

nor should they exploit these borrowers by providing loans borrowers cannot afford to repay. Rather, a socially responsible firm can leverage AI to decide who should be and can be helped. Lastly, at a broader level, this study informs the need to find the right technology for different decision environments, such as the one complicated by the shock of a disaster.

On a side note, our research enriches our understanding on the nuanced role of concept drift in AI performance, highlighting the importance of understanding the underlying data-generating process when applying AI tools. We show that sampling shift and covariate drift could exhibit different patterns for different segments of data (borrowers), which would in turn lead to differences in AI performance for these data segments. Furthermore, this study contributes to the emergent research area of AI bias. AI bias in lending against the underprivileged, such as minorities (Bayer et al. 2018), lower-income households (Begley and Purnanandam 2021), or the elderly and immigrants (Dobbie et al. 2021), has been commonly reported. In contrast, our study provides a positive use case of AI: it benefits the underprivileged when it comes to disaster relief.

Our study is not without limitations. First, we focus on investigating the outcome of delinquency due to data availability, although indicators such as loan amount, interest rate, and paid principal/interest can be key barometers of lending as well. When such data are available to researchers, there will be interesting work to be done in examining AI’s impact more comprehensively using these performance measures. Second, we examine delinquency at the individual borrower level. Future research can study the loan-level delinquency if such data are available. Third, we mainly study the impact of whether a lender deployed customized AI for credit scoring. It should be noted that AI has also been widely applied in other aspects of lending, such as customer service, fraud detection, and loan collection. One interesting future effort would examine how different types of AI applications can jointly help improve lending efficiency and efficacy. Fourth, we focus on the benefit AI has for borrowers. Yet by reducing delinquency, lenders have a better chance of sustaining their business after disasters. Future research could expand the scope of this study by more comprehensively examining AI’s benefit to lending firms. Last, our research context is the credit market and disaster management in China. The effect of AI depends on the specific culture, regulation, and technology development level in a region. Although we do not believe the China context is atypical, a study on how the impact of AI pans out in other territories is warranted.

## Acknowledgments

The authors thank the guest editors of the special issue, the associate editor, and the reviewers for their invaluable comments and suggestions. The authors also thank the anonymous company that allowed them to access the data for the study.

## Endnotes

<sup>1</sup> See https://www.statista.com/statistics/510894/natural-disastersglobally-and-economic-losses/ (accessed December 17, 2022).

<sup>2</sup> Our nondisclosure agreement with this firm requires us to keep the identity of the firm confidential.

<sup>3</sup> See https://www.pwc.com/id/en/fintech/fintech-lending-teaser-060519.pdf (accessed April 15, 2023).

<sup>4</sup> The client’s loan process may or may not involve machine learning, and we cannot observe this.

<sup>5</sup> We know only the actual algorithms used by a small portion of lenders and so we do not drill down on the specific algorithms in our empirical analysis. We also only observe the algorithm used in the final stage of the model. Various machine learning techniques (e.g., XGBoost) could be used during different steps of model building, including feature generation, feature engineering, and feature selection processes. For example, an autoencoder of deep learning was commonly used for feature engineering. Such models used during the intermediate steps are not observed in our data.

One may argue that approving more loans to victims is all that matters when it comes to disaster relief. However, commercial lenders charge interest. An approved loan also means an extra financial burden and may not always help a victim. A loan that leads to delinquency may exacerbate the economic hardship of borrowers (Melzer 2011).

<sup>7</sup> See Wikipedia (2022). Note that only delinquency of financial institutions’ loans is reported. Default on personal loans among friends is only recorded by the court if it goes to a lawsuit.

<sup>8</sup> Victims who cannot bear the burden of loan interest should not be supported by commercial loans. Rather, they should seek charity or government funds. Also, indicators such as approval speed, loan amount, loan period, and interest rate are viable alternative measures. However, such loan-level information is not available to us.

<sup>9</sup> The credit score used in our analysis is the standard credit score provided by Company X to all of its clients, analogous to the credit report provided by the U.S. credit bureaus such as Experian. The AI customized credit score (personalized for each subscribed client) is not observable to us and is not used in this paper.

<sup>10</sup> Aligning with the U.S. credit score system, the average credit score of Company X is around 600, which is a commonly accepted threshold in lending to separate good from bad borrowers (see White 2022).

<sup>11</sup> See http://www.ndrcc.org.cn/zcfg/5924.jhtml (accessed August 12, 2022).

## References

Abbasi A, Li J, Clifford G, Taylor H (2018) Make “fairness by design” part of machine learning. Harvard Bus. Rev. August 1, 2018, https://hbr.org/2018/08/make-fairness-by-design-part-ofmachine-learning.

Abbasi A, Dillon-Merrill R, Rao HR, Sheng O, Chen R (2021) Call for papers—Special issue of Information Systems Research— Unleashing the power of information technology for strategic management of disasters. Inform. Systems Res. 32(4):1490–1493.

Baker AC, Larcker DF, Wang CCY (2022) How much should we trust staggered difference-in-differences estimates? J. Financial Econom, 144(2):370–395

Banerjee AV, Duflo E (2011) Poor Economics: A Radical Rethinking of the Way to Fight Global Poverty (PublicAffairs, New York).

Bapna R, Ramaprasad J, Umyarov A (2018) Monetizing freemium communities: Does paying for premium increase social engage ment? MIS Quart. 42(3):719–735.

Bartlett R, Morse A, Stanton R, Wallace N (2022) Consumer-lending discrimination in the FinTech Era. J. Financial Econom. 143(1): 30–56.

Bayer P, Ferreira F, Ross SL (2018) What drives racial and ethnic differences in high-Cost mortgages? The role of high-Risk lenders. Rev. Financial Stud. 31(1):175–205.

Becchetti L, Castriota S (2011) Does microfinance work as a recovery tool after disasters? Evidence from the 2004 tsunami. World Development 39(6):898–912.

Beer R, Ionescu F, Li G (2018) Are income and credit scores highly correlated? FEDS Notes (August 13), https://www.federalreserve. gov/econres/notes/feds-notes/are-income-and-credit-scoreshighly-correlated-20180813.htm.

Begley TA, Purnanandam A (2021) Color and credit: Race, regulation, and the quality of financial services. J. Financial Econom. 141(1):48–65.

Berg T, Burg V, Gombovic ´ A, Puri M (2020) On the rise of FinTechs: Credit scoring using digital footprints. Rev. Financial Stud. 33(7):2845–2897.

Bertrand M, Duflo E, Mullainathan S (2004) How much should we trust differences-in-differences estimates? Quart. J. Econom. 119(1):249–275.

Brevoort KP, Grimm P, Kambara M (2016) Credit invisibles and the unscored. Cityscape 18(2):9–34.

Campbell TS, Dietrich JK (1983) The determinants of default on insured conventional residential mortgage loans. J. Finance 38(5):1569–1581.

Celil HS, Oh S, Selvam S (2022) Natural disasters and the role of regional lenders in economic recovery. J. Empirical Finance 68:116–132.

Clemons EK, Thatcher ME (2008) Capital One Financial and a decade of experience with newly vulnerable markets: Some propositions concerning the competitive advantage of new entrants. J. Strategic Inform. Systems 17(3):179–189.

Di Maggio M, Ratnadiwakara D, Carmichael D (2021) Invisible primes: Fintech lending with alternative data. Preprint, submitted October 11, http://dx.doi.org/10.2139/ssrn.3937438.

Dobbie W, Liberman A, Paravisini D, Pathania V (2021) Measuring bias in consumer lending. Rev. Econom. Stud. 88(6):2799–2832.

Fuster A, Goldsmith-Pinkham P, Ramadorai T, Walther A (2021) Predictably unequal? The effects of machine learning on credit markets. J. Finance 77(1):5–47.

Gallagher J, Hartley D (2017) Household finance after a natural disaster: The case of Hurricane Katrina. Amer. Econom. J. Econom. Policy 9(3):199–228.

Gallagher J, Hartley D, Shawn R (2022) Weathering an unexpected financial shock: The role of disaster assistance on household finance and business survival. J. Assoc. Environ. Resource Economists 10(2):525–567.

Garmaise MJ, Moskowitz TJ (2009) Catastrophic risk and credit mar kets. J. Finance 64(2):657–707.

Ge R, Feng J, Gu B, Zhang P (2017) Predicting and deterring default with social media information in peer-to-peer lending. J. Man agement Inform. Systems 34(2):401–424.

Gitter SR, Barham BL (2007) Credit, natural disasters, coffee, and educational attainment in rural Honduras. World Development 35(3):498–511.

Hallegatte S, Vogt-Schilb A, Rozenberg J, Bangalore M, Beaudet C (2020) From poverty to disaster and back: A review of the liter ature. Econom. Disaster Climate Change 4(1):223–247.

Heckman J (1979) Sample specification bias as a selection error. Econometrica

Hong Kong Applied Science and Technology Research Institute (2020) ASTRI publishes white paper on alternative credit scoring of MSMEs. Report, Hong Kong Applied Science and Technology Research Institute, Hong Kong.

Iacus SM, King G, Porro G (2012) Causal inference without balance checking: Coarsened exact matching. Political Anal. 20(1):1–24.

Imai KS, Azam MS (2012) Does microfinance reduce poverty in Bangladesh? New evidence from household panel data. J. Develop ment Stud. 48(5):633–653.

Israel S, Caspia A, Belskyd DW, Harrington HL, Hogan S, Houts R, Ramrakha S, Sersg S, Poulton R, Moffitt TE (2014) Credit scores, cardiovascular disease risk, and human capital. Proc. Natl. Acad. Sci. USA 111(48):17087–17092.

Jiang J, Liao L, Lu X, Wang Z, Xiang H (2021) Deciphering big data in consumer credit evaluation. J. Empirical Finance 62:28–45

Kaur H, Pannu HS, Malhi AK (2019) A systematic review on imbalanced data challenges in machine learning: Applications and solutions. ACM Comput. Surveys 52(4):79.

King G, Nielsen R (2019) Why propensity scores should not be used for matching. Political Anal. 27(4):435–454.

Kleinberg J, Lakkaraju H, Leskovec J, Ludwig J, Mullainathan S (2018) Human decisions and machine predictions. Quart. J. Econom. 133(1):237–293.

Koetter M, Noth F, Rehbein O (2020) Borrowers under water! Rare disasters, regional banks, and recovery lending. J. Financial Intermediation 43(C):100811.

Lin M, Prabhala NR, Viswanathan S (2013) Judging borrowers by the company they keep: Friendship networks and information asymmetry in online peer-to-peer lending. Management Sci 59(1):17–35.

Lu T, Zhang Y, Li B (2019) The value of alternative data in credit risk prediction: Evidence from a large field experiment. Proc. 40th Internat. Conf. Inform. Systems (Association for Information Systems, Atlanta), 10.

Lyons AC, Yilmazer T (2005) Health and financial strain: Evidence from the survey of consumer finances. Southern Econom. J. 71(4):873–890.

Marshall GL, Canham SL, Kahana E, Larson E (2022) Mortgage delinquency, foreclosure, and cognition in later life. Housing Soc. 49(2):113–127.

Melzer BT (2011) The real costs of credit access: Evidence from the payday lending market. Quart. J. Econom. 126(1):517–555.

Oksanen A, Aaltonen M, Rantala K (2016) Debt problems and life transitions: A register-based panel study of Finnish young people. J. Youth Stud. 19(9):1184–1203.

Park I, Sharman R, Rao HR (2015) Disaster experience and hospital information systems: An examination of perceived information assurance, risk, resilience, and his usefulness. MIS Quart. 39(2):317–344.

Pliakos K, Joo SH, Park JY, Cornillie F, Vens C, Van den Noortgate W (2019) Integrating machine learning into item response theory for addressing the cold start problem in adaptive learning systems. Comput. Ed. 137:91–103.

Polyzotis N, Roy S, Whang SE, Zinkevich M (2017) Data management challenges in production machine learning. Proc. ACM SIGMOD Internat. Conf. Management Data (Association for Computing Machinery, New York), 1723–1726

Salganicoff M (1997) Tolerating concept and sampling shift in lazy learning using prediction error context switching. Artificial Intelligence Rev. 11(1–5):133–155.

Sant’Anna PHC, Zhao J (2020) Doubly robust difference-in-differences estimators. J. Econometrics 219(1):101–122.

Sawada Y, Shimizutani S (2008) How do people cope with natural disasters? Evidence from the great Hanshin-Awaji (Kobe) earth quake in 1995. J. Money Credit Banking 40(2–3):463–488.

Shoji M (2010) Does contingent repayment in microfinance help the poor during natural disasters? J. Development Stud. 46(2):191–210.

Stuart EA (2010) Matching methods for causal inference: A review and a look forward. Statist. Sci. 25(1):1–21.

Webb GI, Hyde R, Cao H, Nguyen HL, Petitjean F (2016) Characteriz ing concept drift. Data Mining Knowledge Discovery 30(4):964–994

White A (2022) What is considered an average credit score and how to improve your credit. Accessed August 25, 2022, https://www. cnbc.com/select/what-is-an-average-credit-score/.

Widmer G, Kubat M (1996) Learning in the presence of concept drift and hidden contexts. Machine Learn. 23(1):69–101.

Wikipedia. Corporate social responsibility. Accessed Septem ber 3, 2022, https://en.wikipedia.org/wiki/Corporate\_social\_ responsibility.

Wikipedia. Social credit system. Accessed September 2, 2022, https://en.wikipedia.org/wiki/Social\_Credit\_System.

World Bank (2020) Learning from Experience (World Bank, Washing ton, DC).
