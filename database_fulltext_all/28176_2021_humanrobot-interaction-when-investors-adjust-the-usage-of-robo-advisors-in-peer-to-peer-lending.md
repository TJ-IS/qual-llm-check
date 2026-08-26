---
otero_id: 28176
otero_key: "7BRM9CDK"
title: "Human–Robot Interaction: When Investors Adjust the Usage of Robo-Advisors in Peer-to-Peer Lending"
authors: "Ruyi Ge; Zhiqiang (Eric) Zheng; Xuan Tian; Li Liao"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Human–Robot Interaction: When Investors Adjust the Usage of Robo-Advisors in Peer-to-Peer Lending

Ruyi Ge,<sup>a</sup> Zhiqiang (Eric) Zheng,<sup>b</sup> Xuan Tian,<sup>c</sup> Li Liao<sup>c</sup>

<sup>a</sup> Department of Electronic Commerce, Shanghai Business School, Shanghai 200235, China; <sup>b</sup> Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080; <sup>c</sup> PBC School of Finance, Tsinghua University, Beijing 100083, China

Contact: gery@sbs.edu.cn (RG); ericz@utdallas.edu, https://orcid.org/0000-0001-8483-8713 (ZZ); tianx@pbcsf.tsinghua.edu.cn (XT); liaol@pbcsf.tsinghua.edu.cn (LL)

Received: January 15, 2019<sub>Revised:</sub> Decem Accepted: Published Online in Articles in Advance: July 20, 2021

https://doi.org/10.1287/isre.2021.1009

Copyright:

Abstract. We study the human–robot interaction of <sup>fi</sup>nancial-advising services in peer-topeer lending (P2P). Many crowdfunding platforms have started using robo-advisors to help lenders augment their intelligence in P2P loan investments. Collaborating with one of the leading P2P companies, we examine how investors use robo-advisors and how the human adjustment of robo-advisor usage affects investment performance. Our analyses show that, somewhat surprisingly, investors who need more help from robo-advisors— that is, those encountered more defaults in their manual investing—are less likely to adopt such services. Investors tend to adjust their usage of the service in reaction to recent robo-advisor performance. However, interestingly, these human-in-the-loop interferences often lead to inferior performance.

History: Hemant Jain, Balaji Padmanabhan, Paul Pavlou, and Raghu Santanam, Senior Editors; Gordan Burtch, Associate Editor. This paper has been accepted for the Information Systems Research Special Section on Humans, Algorithms, and Augmented Intelligence: The Future of Work, Organizations and Society.

Funding: R. Ge received <sup>fi</sup>nancial support from the Ministry of Education in China Research Program for Humanities and Social Sciences [Grant No. 19YJC630041]. E. Zheng received <sup>fi</sup>nancial support from the National Natural Science Foundation of China (NSFC) [Grants 71850013 and 71532004]. T. Xuan received <sup>fi</sup>nancial support from the NSFC [Grants 71825002 and 71790591].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.1009.

Keywords: robo-advisor human-in-the-loop peer-to-peer lending augmented intelligence

## 1. Introduction

Robo-advisor (hereafter RA) is a service that provides automated, algorithm-based wealth-management advice without the use of a human <sup>fi</sup>nancial planner.<sup>1</sup> Typically, these services use algorithms to help investors determine how to invest based on their risk preference, budget, and investment goals. In other words, RAs help augment investor intelligence in a personalized manner. Compared with human advisors, RAs are more accessible (being available 24/7), and they charge less (e.g., 0.25% compared with the 2–20 standard in the <sup>fi</sup>nancial advising industry).<sup>2</sup> RAs also require much smaller capital outlays for receiving personal <sup>fi</sup>nancial advice—for example, \$500 for Wealthfront compared with \$50,000 for Vanguard.<sup>3</sup> Since the <sup>fi</sup>rst RA launched in 2008, the industry has grown rapidly. As of 2019, the three largest stand-alone RAs, Betterment, Wealthfront, and Personal Capital, boast assets under management (AUM) of approximately \$16 billion, \$11 billion, and \$8.5 billion, respectively.<sup>4</sup> Recently, traditional wealth-management companies, such as Vanguard and Charles Schwab, have also started to incorporate RAs into their <sup>fi</sup>nancialadvising services. For example, Charles Schwab’s intelligent portfolio provides clients with robo-advising services for managing conventional accounts, such as 401(k), IRA, trust, and 529 plan accounts. The total AUM of the RA industry is expected to increase to \$2.2 trillion by 2020 (KPMG 2016).

Most RAs in wealth management are founded based on Markowitz’s portfolio-optimization theory (Friedberg 2019), creating a diversi<sup>fi</sup>ed investment portfolio with the greatest returns for each risk level (Markowitz 1952). As such, the basic inputs are typically the returns and variance–covariance matrix of asset returns. RAs then employ computer algorithms to optimize the risk–return tradeoff and recommend a diversi<sup>fi</sup>ed portfolio accordingly. Some RAs start by using sophisticated machine learning algorithms, such as random forest, neural network, and nonlinear shrinkage methods, in their optimization model (D’Acunto et al. 2019, D’Hondt et al. 2019).

Although most RAs operate in the conventional wealth-management domain and help their clients build a portfolio of traditional assets—for example, stocks, bonds, and commodities—others explore new territories such as peer-to-peer (P2P) loans. Until July 2018, more than \$23 billion in loans originated in the two largest

U.S. P2P lending platforms, Prosper and Lending Club, while more than \$1,080 billion in loans have been transacted on Chinese P2P lending platforms (Jiang et al. 2020). A lender (i.e., investor) on a typical P2P platform usually needs to choose among hundreds of available loans to invest in at any time. These loans have different interest rates and default probabilities, and every loan is unique with limited information (e.g., loan descriptions) for lenders to evaluate. It is, therefore, challenging for lenders to optimize their loan investment in such an environment. Given this, most mainstream P2P platforms (e.g., Lending Club, Prosper, and PPdai.com) have started providing RA services to help lenders choose loans worthy of funding. For example, a third-party company, Fastbacker, builds a robo-advising application that monitors Kickstarter projects and noti<sup>fi</sup>es investors when suitable projects become available. LendingRobot RAs help lenders automate the management of their accounts across multiple P2P platforms, such as Lending Club and Prosper. Some RAs even help lenders design investment strategies. For example, Lending Club collaborated with InterestRadar to offer a robo-advising service that helped lenders scan available P2P loans and assisted them in choosing appropriate investment strategies for loans that met their prespeci<sup>fi</sup>ed criteria. These RAs gained popularity among lenders quickly. For example, at PPdai, the <sup>fi</sup>rst P2P lending platform in China, automated investments through RAs have outnumbered manual investments since it launched the RA service in 2015.

As these intelligence-augmentation tools become increasingly popular in people’s daily lives, it is important to understand how humans and algorithms should col laborate. The nascent literature on human-in-the-loop (e.g., Dietvorst et al. 2016, Xu and Chau 2018, Fugener ¨ et al. 2019) highlights the importance of having humans engaged in designing, implementing, and re<sup>fi</sup>ning algorithms. We draw on this body of literature in the context of human–RA interactions. Speci<sup>fi</sup>cally, we are interested in how investors use RA services in their investments and whether having humans in the loop of RA deployment augments investment performance or not.

Researchers and practitioners, however, have little understanding on these issues. This study attempts to <sup>fi</sup>ll these gaps by examining the human–RA interaction through collaboration with a leading P2P lending company publicly traded on the NASDAQ.<sup>5</sup> Lenders there can easily access the RA service and activate it by simply clicking a speci<sup>fi</sup>c button on the company’s homepage (see Online Appendix 1 for a screenshot). Once a lender decides to use an RA, they con<sup>fi</sup>gure their risk preference and investment amount. Lenders can turn off the RA service at any time they deem necessary.

The company provided us with the data on the complete transaction history of a random sample of lenders, including all the loans each lender funded, detailed information on each loan transacted (e.g., investment amount, date, maturity, interest rate, and payment status), and, most distinctively, the information on whether the lenders invested in the loans manually or through an RA. We observed a mix of lender populations. Some relied totally on RAs for choosing loans, some used the service occasionally, and others never tried the service at all.

This data set provides us with a unique venue to investigate the interwoven effects of investors’ use of RAs and the corresponding performance of investments. Speci<sup>fi</sup>cally, we study the following three research questions:

1. How does investors’ investment performance in the past in<sup>fl</sup>uence their RA adoption when the service becomes available?

2. How do investors adjust their usage of RAs according to the RA’s investment performance?

3. How does the adjustment affect investment performance?

Taken together, the answers to these questions will help us answer the overarching question pertaining to how investors interact with RAs and whether having humans in the loop of using RA helps improve P2P investment.

We <sup>fi</sup>nd that investors who encountered more defaults in the past are less likely to try RA when the service becomes available. RA usage is positively in<sup>fl</sup>uenced by recent RA performance: When recent RA performance is lower, investors decrease their usage of RA immediately, and vice versa. However, such swift adjustment in RA usage often leads to worse investment performance, especially when the adjustments are frequent and substantial.

Our research makes several contributions. It represents one of the <sup>fi</sup>rst attempts at investigating RAaugmented intelligence in P2P lending investments. It also provides the <sup>fi</sup>rst empirical evidence demonstrating how investors’ investment performance in<sup>fl</sup>uences RA adoption. This <sup>fi</sup>nding can help RA marketers target certain customer segments to improve adoption rates. Moreover, as the <sup>fi</sup>rst study on human–RA interaction, our results show that users are subject to the recency effect when evaluating RAs. They experience more losses due to being too reactive to recent RA performance. This presents a new, but negative, use case for human–- arti<sup>fi</sup>cial intelligence (AI) symbiosis, where leaving too much control to humans over when to use an RA may be counterproductive. This result re<sup>fl</sup>ects investors’ possible misunderstanding and misuse of RAs. They may not always have proper knowledge of RA systems and may intervene counterproductively. It suggests that such RA systems need to offer more transparency in their services (Friedberg 2018), for example, by communicating with investors on their RA’s objective and inner-working mechanisms. Conversely, it also suggests that a well-designed RA should anticipate the possible adjustments lenders may make and factor in such reactions in their algorithms' design.

## 2. Background and Research Context 2.1. Literature Review

We <sup>fi</sup>rst brie<sup>fl</sup>y review the nascent body of literature on robo-advising. The scant literature largely focuses on describing the features of RAs (e.g., Lopez et al. 2015, Park et al. 2016, and Jung et al. 2017) or the IT components inside RAs (e.g., Musto et al. 2015 and Jung et al. 2018). Recently, a few studies have assessed the bene<sup>fi</sup>ts of robo-advising in terms of reduced fees, easy onboarding processes, and investment performance (D’Acunto et al. 2019, D’Hondt et al. 2019). We extend the RA literature by examining how human beings and RAs interact and how such interactions help augment or hamper investment performance. Context-wise, we also extend the literature’s predominant focus on traditional assets to P2P loan investments.

Our paper extends the P2P lending literature. Prior P2P lending studies mainly focus on the borrower’s side, considering factors that in<sup>fl</sup>uence funding success and loan risk (e.g., default or delinquency), including borrowers’ credit ratings (e.g., Iyer et al. 2016), demographic characteristics (e.g., Duarte et al. 2012), friendship with others (e.g., Lin et al. 2013), and social media communications (e.g., Ge et al. 2017 and Xu and Chau 2018). Only a few studies investigate lenders’ behavior and performance (e.g., Paravisini et al. 2016 and Jiang et al. 2020). However, none of these studies have examined investors’ interactions with RAs, which have become a dominant investment channel (in addition to human investing) in many P2P lending platforms. Our work is the <sup>fi</sup>rst to shed light on lenders’ usage of RAs and the corresponding performance.

Our study is also relevant to the broad literature on <sup>fi</sup>nancial technology (<sup>fi</sup>ntech) adoption. Early studies have examined ATM adoption (Hitt and Frei 2002), online banking-service adoption (e.g., Campbell and Frei 2010), and mobile-payment adoption (e.g., Schierz et al. 2010, Srivastava et al. 2010, and Zhou 2013). We only <sup>fi</sup>nd one study, D’Acunto et al. (2019), that performs a simple cross-sectional comparison of RA adopters’ characteristics versus nonadopters’. They note that users and nonusers are indistinguishable based on demographic characteristics such as gender, age, and trading experience. We extend this literature by analyzing how users adopt and adjust the use of RAs and, consequently, how the adjustments augment or hinder investment performance.

Finally, our study is related to the human–AI collaboration literature. As AI becomes increasingly integrated into our lives, people begin to view AI systems not only as applications, but also as collaborators (Fugener et al.¨ 2019). The literature has investigated different scenarios of how humans and AI should be in each other’s loops to ful<sup>fi</sup>ll a task. For example, humans and AI can work together to effectively manage crowd-labeling quality (Wang et al. 2017, Yin et al. 2021) or improve the effectiveness of customer-service chatbots (Schanke et al. 2021). Humans can also help identify cases that may cause the predictive model to fail (Attenberg et al. 2015), and a human-in-the-loop system can be used to shorten the time to build deployable machine learning models (Xin et al. 2018). The experiments of Dietvorst et al. (2015, 2016) and Germann and Merkle (2019) further examine humans’ attitudes toward the performance of algorithms, while the experiments of Fugener et al. ( ¨ 2019) investigate human collaboration with deep-learning methods to produce the best imageclassi<sup>fi</sup>cation accuracy. Our research contributes to this literature stream by examining a new form of human-inthe-loop case—that is, the case of having humans adjust the usage of AI by enabling or disabling AI.

## 2.2. Research Context

We collaborate with one of the earliest and largest P2P lending companies in the world. As of 2019, the company has attracted more than 70 million borrowers and investors and has successfully facilitated more than \$110 billion in loans.

To seek funding on the platform, a borrower must <sup>fi</sup>rst go through a veri<sup>fi</sup>cation process, authenticating her demographics, <sup>fi</sup>nancial status, and credit history. Once veri<sup>fi</sup>ed, the borrower becomes eligible to post an online listing, specifying her desired loan amount, interest rate, and description of the loan purpose, etc. The platform assesses the loan’s credit quality and assigns the loan a credit grade from AAA (the highest quality) to F (the lowest). The loan is fully funded only when the total bid amount reaches the sought amount. Otherwise, the request fails, and no funds will be transferred.

To bid on loans, lenders <sup>fi</sup>rst need to transfer adequate money to their accounts. They then decide which loans to bid on and how much to invest. Borrowers are not allowed to reject lenders’ bids. After a loan is fully funded, funds are collected from the lender’s accounts and transferred to the borrower’s account after deducting a transaction fee. Loans are repaid in equal installments monthly, and the repayments are distributed to lenders’ accounts automatically. If a monthly payment is made on time, the loan status is shown as “normal,” and otherwise “delayed.” The platform does not guarantee loan repayment, and, therefore, lenders will bear the potential loss of loan defaults themselves.

The platform launched a free RA service in April 2015 to help lenders bid. The RA worked in two steps:

1. First, it employed an ensemble of various machine learning methods, including decision tree, support vector machine, and shrinkage estimation, to assess the risk (e.g., default probability) of each loan. The inputs to these machine learning methods consist of loan characteristics (term, amount, loan description, etc.) and borrower characteristics (education, employment status, <sup>fi</sup>nancial status, social network features, borrowing history, online behavior, mobile communication features, etc.). A sample screenshot detailing the main variables is presented in Online Appendix 2.

2. Next, building on Markowitz’s portfolio-optimization approach, the RA chooses and invests in the loans that meet the lender’s risk preference.

The RA service became very popular among lenders; more than half of the bids were conducted by RAs after one year of release.

## 3. Data Description

We obtained a random data sample of 4,374 lenders from the company with the complete history of their bids across 18 months, from January 2015 to June 2016.<sup>6</sup> The descriptions of the sample are presented in Table 1.

In our sample, 73% of the lenders were male, and the average lender was 37.6 years old, with 1.25 years of investment experience on the platform.<sup>7</sup> On average, a lender invested 251.2 renmibi (RMB) per bid and 138,555 RMB in total. The means of lenders’ annualized interest rates and terms were 15.96% and 8.94 months, respectively. During the 18 months, 63% of lenders used the RA service to invest in at least one loan, and the lenders’ average monthly return rate was 1%.<sup>8</sup>

It is noteworthy that the means of BidAmount and TotalAmount are much larger than their medians, which implies positive skewness. Therefore, we use the natural logarithm of these variables in the following analyses.

## 4. RA Adoption

Our <sup>fi</sup>rst research question (RQ1) asks how investment performance in the past affects investors’ RA adoption. RQ1 investigates the human–RA interaction from the adoption (i.e., <sup>fi</sup>rst interaction) perspective as a function of investors’ past performance. Past performance may affect RA adoption through two possible underlying mechanisms. First, investors’ previous investment performance will affect the perceived usefulness of RAs. An investor whose past performance was inferior is more likely to count on RAs to improve their performance; that is, RAs’ perceived usefulness turns higher. There has been abundant information systems literature documenting that users’ perceived usefulness or performance expectancy concerning a technology increases the likelihood of technology adoption (e.g., Venkatesh et al. 2003). This suggests that investors experiencing inferior performance should be more likely to adopt RAs when the service becomes available.

Table 1. Sample Description

<table><tr><td>Variable</td><td>Mean</td><td>S.D.</td><td>Min</td><td>Median</td><td>Max</td><td>N</td></tr><tr><td>Gender</td><td>0.73</td><td>0.45</td><td>0</td><td>1</td><td>1</td><td>4,370</td></tr><tr><td>Age</td><td>37.62</td><td>9.68</td><td>20</td><td>35</td><td>75</td><td>4,340</td></tr><tr><td>Experience</td><td>1.25</td><td>1.19</td><td>0</td><td>1</td><td>9</td><td>4,374</td></tr><tr><td>BidAmount</td><td>251.2</td><td>608.9</td><td>10</td><td>111.4</td><td>13698</td><td>4,374</td></tr><tr><td>TotalAmount</td><td>138,555</td><td>477,683</td><td>50</td><td>32,916</td><td>1.2e+07</td><td>4,374</td></tr><tr><td>InterestRate</td><td>15.96</td><td>3.75</td><td>7</td><td>16.35</td><td>23.64</td><td>4,374</td></tr><tr><td>Term</td><td>8.94</td><td>2.54</td><td>1</td><td>9.41</td><td>19.45</td><td>4,374</td></tr><tr><td>RAAdopted</td><td>0.63</td><td>0.48</td><td>0</td><td>1</td><td>1</td><td>4,374</td></tr><tr><td>ReturnRate</td><td>0.01</td><td>0.003</td><td>-0.03</td><td>0.01</td><td>0.02</td><td>4,374</td></tr></table>

Note. The units of BidAmount and TotalAmount are Chinese RMB.

On the other hand, ceteris paribus, underperforming means that the investor has encountered more defaults than others. The investor would then have a stronger perceived risk regarding P2P loans on the platform and would thus be less certain about RA performance in such cases. Prior studies have shown that investors are less likely to adopt a new technology when the perceived risk of using it is high (Featherman and Pavlou 2003). When performance risk is high—for example, the possibility of technology malfunctioning or technology not performing as designed or advertised—the technology will fail to deliver the desired bene<sup>fi</sup>ts (Featherman and Pavlou 2003). This suggests that investors with inferior past performances would be less likely to adopt RAs because of their higher level of perceived RA performance risk.

Because these two potential effects may counteract each other, our research question sets out to answer which one dominates in our study context.

## 4.1. Empirical Specifications

Our data sample began in January 2015, and the RA service launched in April 2015. In our sample, approximately 1,000 lenders had investment transactions both before and after April 2015, which provides a good setting for examining how lenders reacted to the service's launch. We <sup>fi</sup>nd that more than 50% of the <sup>fi</sup>rst tryouts occurred in the <sup>fi</sup>rst month, and nearly 75% of tryouts occurred within the <sup>fi</sup>rst three months. We examine the effect of lenders’ previous investment performance on their RA adoption behavior using the following two cross-sectional models:<sup>9</sup>

$$
\begin{array}{r l} & {P r o b (R A A d o p t e d _ {i, T} = 1 \mid X)} \\ & {\qquad = L o g i t (\alpha_ {0}} \\ & {\qquad + \alpha_ {1} P r e v i o u s \_ I n v e s t m e n t \_ P e r f o r m a n c e _ {i}} \\ & {\qquad + \alpha_ {2} P r e v i o u s \_ I n v e s t m e n t \_ C h a r a c t e r i s t i c s _ {i}} \\ & {\qquad + \alpha_ {3} C o n t r o l s _ {i}),} \end{array}\tag{1}
$$

$$
\begin{array}{c} R A S h a r e _ {i, T} = \beta_ {0} + \beta_ {1} P r e v i o u s \_ I n v e s t m e n t \_ P e r f o r m a n c e _ {i} \\ + \beta_ {2} P r e v i o u s \_ I n v e s t m e n t \_ C h a r a c t e r i s t i c s _ {i} + \beta_ {3} C o n t r o l s _ {i} + \varepsilon_ {i}. \end{array}\tag{2}
$$

We consider two alternative dependent variables, $R A A d o p t e d _ { i , T }$ and $R A S h a r e _ { i , T } ,$ to measure lenders’ adoption behavior. $R A A d o p t e d _ { i , T }$ denotes whether a lender has ever used the RA service during a period of T months after the service becomes available; it equals one if the lender has used the service to invest in at

Table 2. The Effect of Previous Investment Performance on RA Adoption

<table><tr><td rowspan="3">Variable</td><td colspan="2">Panel A: Logit specification</td><td colspan="2">Panel B: Tobit specification</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $RAAdopted_{i,T=1}$ </td><td> $RAAdopted_{i,T=3}$ </td><td> $RAShare_{i,T=1}$ </td><td> $RAShare_{i,T=3}$ </td></tr><tr><td> $ReturnRate_i$ </td><td>-52.979(76.178)</td><td>-119.361(79.433)</td><td>-15.934(20.159)</td><td>-27.746(21.655)</td></tr><tr><td> $\ln(\#Default)_i$ </td><td>-0.499**(0.210)</td><td>-0.487**(0.208)</td><td>-0.106**(0.049)</td><td>-0.180***(0.060)</td></tr><tr><td> $InterestRate_i$ </td><td>-0.080(0.062)</td><td>-0.042(0.066)</td><td>-0.025(0.017)</td><td>-0.016(0.018)</td></tr><tr><td> $Term_i$ </td><td>0.306***(0.041)</td><td>0.265***(0.039)</td><td>0.087***(0.010)</td><td>0.088***(0.010)</td></tr><tr><td> $\ln(BidAmount)_i$ </td><td>-0.078(0.127)</td><td>-0.057(0.126)</td><td>0.029(0.032)</td><td>0.011(0.036)</td></tr><tr><td> $\ln(TotalAmount)_i$ </td><td>0.195***(0.059)</td><td>0.136**(0.058)</td><td>0.005(0.016)</td><td>0.012(0.017)</td></tr><tr><td>Lender characteristics</td><td>Controlled</td><td>Controlled</td><td>Controlled</td><td>Controlled</td></tr><tr><td>Observations</td><td>924</td><td>984</td><td>924</td><td>984</td></tr><tr><td> $R^2$ </td><td>0.077</td><td>0.066</td><td>0.083</td><td>0.057</td></tr></table>

$$
^ {* *} p <   0. 0 5; ^ {* * *} p <   0. 0 1.
$$

least one loan during the period, and zero otherwise. $R A S h a r e _ { i , T }$ is the proportion of RA bids among all the bids a lender invested during the period, capturing the intensity of a lender’s RA usage. In both models, i indexes lender; T equals one or three, standing for one month or three months after the RA launch (i.e., April 2015). In other words, if T 1, we calculate RAAdopted<sub>i</sub> and RAShare based on the data from May 2015; if T 3, we calculate RAAdopted and RAShare using the three-month data from May to July 2015.<sup>10</sup>

Previous\_Investment\_Performance takes two measures:<sup>11</sup> ReturnRate and ln(#Default ), representing lenders average monthly return rate and (the natural logarithm of) the number of defaulted loans that lenders encountered before the launch of RA, respectively. The vector Previous\_Investment\_Characteristics includes the average interest rate, the average terms of a lender’s investment (i.e., InterestRate and Term ), and the natural logarithm of the lender’s bid amount and the total amount (i.e., ln(BidAmount ) and ln(TotalAmount )) before the RA launch. Because our data sample began in January 2015, Previous\_Investment\_Performance and Previous\_ Investment\_Characteristics are calculated based on January, February, and March 2015 data. The vector Controls contains lender characteristic variables, including gender, age, and experience.

## 4.2. Results

In Table 2, panel A reports the results from the above logit speci<sup>fi</sup>cation. The coef<sup>fi</sup>cients for ReturnRate are insigni<sup>fi</sup>cant, whereas those for ln(#Default ) are signi<sup>fi</sup>- cant. Speci<sup>fi</sup>cally, columns (1) and (2) suggest that when $\# D e f a u l t _ { i }$ increases by 1%, the odds of $R A A d o p t e d _ { i } , _ { T = 1 }$ decreases by 39.3% (odds ratio 0.607), and the odds of $R A A d o p t e d _ { i , T = 3 }$ decreases by 38.5% (odds ratio 0.615).

These results indicate that a lender experiencing a higher level of loan defaults is less likely to try the RA service. Columns (3) and (4) in panel B report the Tobit regression results with the dependent variable $R A S h a r e _ { i , T } .$ The results show that ln(#Default<sub>i</sub>) exhibits a signi<sup>fi</sup>cant and negative effect on $R A S h a r e _ { i , T } ,$ which is consistent with the results of panel A.

Taken together, the results in Table 2 suggest that investors’ past investment performance affects their adoption of RAs. In other words, a human’s own past performance may well be in the loop regarding the <sup>fi</sup>rst interaction (adoption) decision with RA services. Interestingly, it is the number of defaulted bids, rather than bid return rates, that in<sup>fl</sup>uence lender adoption behavior signi<sup>fi</sup>cantly, possibly because #Default conveys a clearer and more straightforward risk message, as opposed to ReturnRate. Loan defaults are painful, salient events for investors. According to prospect theory (Tversky and Kahneman 1974), salient instances affect people’s assessments of the probability of an event occurring the most. Lenders experiencing more defaulted loans are more likely to perceive the P2P market to be risky and, thus, tend to rely more on their own judgment rather than an RA’s, echoing the <sup>fi</sup>ndings of Featherman and Pavlou (2003), who show that risk perceptions exert a negative impact on the use of e-services.

## 4.3. Robustness Checks

4.3.1. Alternative Explanation. One potential alternative explanation is that investors’ capability, rather than investment performance, drives investors’ RA adoption. However, we do not directly observe investors’ hidden abilities. To alleviate this concern, we replace ln(#Default) with ln(#Default\_Ultimate). The former records whether a loan was defaulted before the RA launch, while the latter is a forward-looking metric capturing whether a loan ultimately defaults. Obviously, the latter is a more accurate proxy for investors’ capabilities. This renders a different result: The coef<sup>fi</sup>cients for ln(#Default\_Ultimate) are not statistically signi<sup>fi</sup>cant (see Table 3), whereas those of ln(#Default) remain signi<sup>fi</sup>cant. This test alleviates the concern that the capability of investors is the more likely driver behind RA adoption.

Table 3. The Effect of Investors’ Capability on RA Adoption

<table><tr><td rowspan="2">Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td> $RAAdopted_{T=1}$ </td><td> $RAAdopted_{T=3}$ </td><td> $RAShare_{T=1}$ </td><td> $RAShare_{T=3}$ </td></tr><tr><td>ReturnRate</td><td>-52.634(76.233)</td><td>-118.154(79.469)</td><td>-15.678(20.257)</td><td>-27.049(21.756)</td></tr><tr><td>ln(#Default_Ultimate)</td><td>0.018(0.138)</td><td>0.064(0.140)</td><td>0.015(0.031)</td><td>0.033(0.037)</td></tr><tr><td>ln(#Default)</td><td>-0.514**(0.241)</td><td>-0.540**(0.243)</td><td>-0.118**(0.053)</td><td>-0.207***(0.066)</td></tr><tr><td>InterestRate</td><td>-0.082(0.064)</td><td>-0.050(0.067)</td><td>-0.027(0.018)</td><td>-0.021(0.019)</td></tr><tr><td>Term</td><td>0.305***(0.041)</td><td>0.263***(0.039)</td><td>0.086***(0.010)</td><td>0.087***(0.011)</td></tr><tr><td>ln(BidAmount)</td><td>-0.073(0.136)</td><td>-0.039(0.135)</td><td>0.034(0.034)</td><td>0.021(0.039)</td></tr><tr><td>ln(TotalAmount)</td><td>0.190***(0.070)</td><td>0.119*(0.070)</td><td>0.001(0.018)</td><td>0.003(0.020)</td></tr><tr><td>Lender characteristics</td><td>Controlled</td><td>Controlled</td><td>Controlled</td><td>Controlled</td></tr><tr><td>Observations</td><td>924</td><td>984</td><td>924</td><td>984</td></tr><tr><td> $R^2$ </td><td>0.078</td><td>0.066</td><td>0.083</td><td>0.058</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

4.3.2. Coarsened Exact Matching. We then use the coarsened exact matching (CEM) approach to alleviate the above endogeneity concern further. CEM coarsens each covariate into meaningful bins, matches observations based on these bins, and then retains the covariates’ original values for analysis (Blackwell et al. 2009). Compared with some other matching methods, such as propensity score matching, CEM can generate matched data sets with lower imbalance (Iacus et al. 2012). To make full use of the data, we use the T 3 data set, which has more observations than T 1 for the matching procedure. We divide lenders into two groups: One group of lenders encountered no defaults (i.e., control group) before the RA launch. The other group of lenders encountered at least one default (i.e., treatment group) before the RA launch. We match these two groups with two sets of covariates, previous investment characteristics and lender characteristics, with a CEM procedure. In total, 126 lenders are matched. The logit regression results of the covariates before and after matching are shown in Table 4.

Then, we use the matched samples to regress lenders’ adoption outcome on the treatment. Table 5 shows that the treatment exerts signi<sup>fi</sup>cant and negative effects on RAAdopted and RAShare, consistent with the main model’s results.

## 5. Adjustment of RA Usage

Our second research question (RQ2) studies how investors adjust their RA usage based on recent RA performance. RQ2 looks at investor interaction with RAs during the phase of using RA services in investments as a function of past RA performance. The investor is allowed to enable or disable RA services at any point in time.

We explain how RA usage is adjusted from the lens of the recency effect, which is the tendency of an individual to recall or emphasize the most recent events. This effect was <sup>fi</sup>rst discovered in cognitive science (Deese and Kaufman 1957, Murdock 1962) and then applied in <sup>fi</sup>nance (e.g., Cushing and Ahlawat 1996, Arnold et al. 2000, and Pompian 2011). Pompian (2011) points out that a manifestation of the recency effect among investors explains their misuse of investment-performance records for mutual funds. Investors tend to analyze a small data sample, such as the fund performance of recent periods, and then make investment decisions based on such recent experiences without paying attention to the cyclical nature of asset class returns. RA services in P2P lending are designed to select suitable loans from all the listed loans on the platform, so as to build a portfolio that meets an investor’s long-term risk and return objectives. However, P2P lending platforms typically release the performance of RA investments to investors monthly. Thus, it is interesting to investigate whether RA users are subject to the recency effect, adjusting their RA usage mainly based on RAs’ recent and short-term performance.

## 5.1. Empirical Specification

In order to examine how recent RA investment performance in<sup>fl</sup>uences investors’ usage of the RA service, we construct a one-year panel starting from May 2015 (immediately after RA became available), with which we estimate the following model:

Table 4. The Logit Speci<sup>fi</sup>cations Before and After Matching

<table><tr><td>Treatment</td><td>(1) Unmatched</td><td>(2) Matched</td></tr><tr><td>InterestRate</td><td>0.751***(0.079)</td><td>0.020(0.153)</td></tr><tr><td>Term</td><td>-0.177(0.109)</td><td>-0.172(0.166)</td></tr><tr><td>ln(BidAmount)</td><td>-1.583***(0.226)</td><td>-0.917(0.652)</td></tr><tr><td>ln(TotalAmount)</td><td>1.574***(0.159)</td><td>0.362(0.288)</td></tr><tr><td>Age</td><td>-0.031*(0.016)</td><td>0.025(0.056)</td></tr><tr><td>Gender</td><td>0.187(0.369)</td><td>0.341(0.549)</td></tr><tr><td>Experience</td><td>-0.212(0.161)</td><td>-0.455(0.327)</td></tr><tr><td>Observations</td><td>984</td><td>126</td></tr><tr><td> $R^2$ </td><td>0.527</td><td>0.046</td></tr></table>

\*p < 0.1; \*\*\*p < 0.01.

$$
\begin{array}{r l} R A S h a r e _ {i, t} = & \beta_ {0} + \beta_ {1} R A \_ P e r f o r m a n c e _ {i, t - 1} \\ & + \beta_ {2} M a n u a l \_ P e r f o r m a n c e _ {i, t - 1} \\ & + \beta_ {3} C o n t r o l s _ {i, t} + L e n d e r _ {i} + M o n t h _ {t} + \varepsilon_ {i, t}. \end{array}\tag{3}
$$

The dependent variable $R A S h a r e _ { i , t }$ is the proportion of RA bids among all the loans in which a lender invested in month $t . R A \_ P e r f o r m a n c e _ { i , t - 1 }$ represents the RA investment performance of month $t \ - \ 1 .$ , measured by $R A \_ R e t u r n R a t e _ { i , t - 1 }$ and ln(RA $\# D e f a u t _ { i , t - 1 } )$ . Manual\_ $P e r f o r m a n c e _ { i , t - 1 }$ is used to control for manual-bidding performance that may also affect a lender’s RA usage. $C o n t r o l s _ { i , t }$ contains the investment characteristics of a lender in month t. Both lender and month <sup>fi</sup>xed effects are included.

## 5.2. Results

Table 6 reports the results under the above speci<sup>fi</sup>cations with two alternative RA\_Performance measures as independent variables. Column (1) measures the performance with ReturnRate, while column (2) uses ln(#Default) as the measurement; column (3) uses the combination of both variables. Similar to the results in Section 4, investors tend to react to ln(#Default) instead of ReturnRate. The results show that the number of defaulted loans invested through RAs that occurred in month t 1 exhibits a signi<sup>fi</sup>cantly negative effect on RA usage in month t.

Table 5. The Effect of Treatment on RA Adoption

<table><tr><td rowspan="2">Variable</td><td>(1)</td><td>(2)</td></tr><tr><td> $RAAdopted_{T=3}$ </td><td> $RAShare_{T=3}$ </td></tr><tr><td>Treatment</td><td>-0.929**(0.454)</td><td>-0.352***(0.108)</td></tr><tr><td>Observations</td><td>126</td><td>126</td></tr><tr><td> $R^2$ </td><td>0.032</td><td>0.060</td></tr></table>

\*\*p < 0.05; \*\*\*p < 0.01.

The results in Table 6 demonstrate that lenders do intervene in RAs’ usage: They tend to adjust their RA usage based on RAs’ latest performance. Furthermore, it is not the return rate of bids, but the number of defaulted bids that affects RA usage. This suggests that when lenders encounter more defaults in a recent RA investment (in the previous month), they tend to reduce RA service usage; conversely, fewer defaults increase RA usage. Speci<sup>fi</sup>cally, column (3) indicates that when $R \bar { A } \_ \# D \bar { e } f a u l t _ { t - 1 }$ increases by 1%, RAShare decreases by 1.4%. Moreover, from the coef<sup>fi</sup>cients of Manual\_Performance variables, we <sup>fi</sup>nd that lenders’ usage of RAs is also affected by the number of defaults of manually bid loans. When lenders experience more defaults in their latest manual investments, they go for RA.

## 5.3. Robustness Checks

5.3.1. Alternative Explanation. An alternative explanation for lenders’ adjustment of RA usage is that lenders adjust their RA usage as a function of their recent overall investment performance, including both RA and manual bidding. The above results may be confounded with the possibility that lenders’ RA performance is commensurate with overall performance. To rule out this alternative explanation, we replace the latest RA performance with the latest overall performance for the previous month in Equation (3). The results in Table 7 show that neither of the overall performance measures $( \mathrm { i . e . , } R e t u r n R a t e _ { t - 1 }$ and $\# D e f a u l t _ { t - 1 } )$ exhibit any signi<sup>fi</sup>cant effect on RA usage. Lenders are more likely to adjust their RA usage based on RA performance rather than overall investment performance.

5.3.2. A Longer Time Window. Moreover, we re-estimate Equation (3) with a longer time window, including both t 1 and t 2. Table 8 shows that only the ln(RA\_#Default) of the most recent month has a negative effect on RA usage, which is consistent with the former result.

## 6. Performance of RA Adjustment

Our third research question (RQ3) aims to answer the following question: Does adjusting RA usage pay off? In other words, can human intervention help augment the intelligence of RAs conversely? If yes, RA service providers should learn from human interventions and incorporate such human intelligence into their RA design loop accordingly.

Investors make an active adjustment of RA usage based on recent RA performance with an intention to

Table 6. The Effect of Recent RA Performance on RA Usage

<table><tr><td rowspan="2">Variable</td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td> $RAShare_t$ </td><td> $RAShare_t$ </td><td> $RAShare_t$ </td></tr><tr><td> $RA\_ReturnRate_{t-1}$ </td><td>1.494 (1.378)</td><td></td><td>1.078 (1.342)</td></tr><tr><td> $Manual\_ReturnRate_{t-1}$ </td><td>-0.136 (0.243)</td><td></td><td>0.082 (0.270)</td></tr><tr><td> $ln(RA_\#Default_{t-1})$ </td><td></td><td>-0.015** (0.006)</td><td>-0.014** (0.006)</td></tr><tr><td> $ln(Manual_\#Default_{t-1})$ </td><td></td><td>0.026*** (0.008)</td><td>0.026*** (0.008)</td></tr><tr><td>Investment characteristics</td><td>Controlled</td><td>Controlled</td><td>Controlled</td></tr><tr><td>Lender &amp; month fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>12,895</td><td>12,895</td><td>12,895</td></tr><tr><td>Lenders</td><td>2,101</td><td>2,101</td><td>2,101</td></tr><tr><td> $R^2$ </td><td>0.170</td><td>0.172</td><td>0.172</td></tr></table>

$$
^ {* *} p <   0. 0 5; ^ {* * *} p <   0. 0 1.
$$

improve their investment performance. However, it is not clear whether such interference pays off. As pointed out by Pompian (2011), the recency effect can cause investors to make suboptimal decisions as a result of relying on historical data samples that are too small to ensure accuracy, which may inadvertently end up in losses. Our investigation of RQ2 reveals that investors make adjustments based on RAs’ monthly performance. RA services in P2P lending typically focus on relatively long-term returns (Ludwig 2020), such as annual returns. Evaluating RA performance and adjusting RA usage based on monthly data may thus be suboptimal. We set out to answer RQ3 by examining the impact of RA usage adjustment on the return rate of loans.

## 6.1. Empirical Specifications

The econometrics model we estimate is:

$$
\begin{array}{c} R e t u r n R a t e _ {i} = \beta_ {0} + \beta_ {1} R A S h a r e \_ A d j u s t m e n t _ {i} \\ + \beta_ {2} R A S h a r e _ {i} + \beta_ {3} C o n t r o l s _ {i} + \varepsilon_ {i}. \end{array}\tag{4}
$$

We estimate the model using two samples built on the one-year panel data starting from May 2015. The <sup>fi</sup>rst sample only includes the completed loans (those either paid off or defaulted) invested during the period. ReturnRate is the average return rate of a lender’s completed loans. RAShare is the RA share among all the completed loans. RAShare\_Adjustment<sub>i</sub> is the coef-<sup>fi</sup>cient of variation of a lender’s monthly RA share (i.e., RAShare\_CoV ), and Controls includes the average investment characteristics of all the completed loans and lender characteristics.

Table 7. The Effect of Recent Overall Performance on RA Usage

<table><tr><td>Variable</td><td> $RAShare_t$ </td></tr><tr><td> $ReturnRate_{t-1}$ </td><td>-0.139 (1.595)</td></tr><tr><td> $\ln(\#Default_{t-1})$ </td><td>-0.001 (0.007)</td></tr><tr><td>Investment characteristics</td><td>Controlled</td></tr><tr><td>Lender &amp; month fixed effects</td><td>Yes</td></tr><tr><td>Observations</td><td>12,895</td></tr><tr><td>Lenders</td><td>2,101</td></tr><tr><td> $R^2$ </td><td>0.169</td></tr></table>

The second sample uses the aggregated data of lenders’ monthly investment performance and characteristics, including both completed and ongoing loans. ReturnRate here is the average of a lender’s monthly return rate. RAShare is the mean of the monthly RA share. Because there exists high multicollinearity between RAShare and RAShare\_CoV in this sample, we reconstruct RAShare\_Adjustment<sub>i</sub> as the standard deviation of a lender’s monthly RA share—that is, RAShare\_ Std . Controls includes the average of monthly investment characteristics and lender characteristics.

## 6.2. Results

Columns (1) and (2) in Table 9 present the estimates of the above speci<sup>fi</sup>cation based on the two data samples, respectively. Both coef<sup>fi</sup>cients of RAShare\_Adjustment in Table 9 are signi<sup>fi</sup>cant and negative, demonstrating that larger adjustments of RA usage result in a worse return rate. In other words, human intervention here leads to worse investment outcomes. Speci<sup>fi</sup>cally, for the <sup>fi</sup>rst sample, a one-unit increase in RAShare\_CoV decreases the average loan return rate by 0.2%. The average total loan investment amount of the investors in the <sup>fi</sup>rst sample is more than 350,000 RMB, and the average term of their investments is nine months. This

Table 8. The Effect of RA Performance in Recent Two Months on RA Usage

<table><tr><td>Variable</td><td> $RAShare_t$ </td></tr><tr><td> $RA\_ReturnRate_{t-1}$ </td><td>1.695 (1.904)</td></tr><tr><td> $RA\_ReturnRate_{t-2}$ </td><td>-0.057 (2.055)</td></tr><tr><td> $\ln(RA\_#Default_{t-1})$ </td><td>-0.017* (0.009)</td></tr><tr><td> $\ln(RA\_#Default_{t-2})$ </td><td>-0.003 (0.010)</td></tr><tr><td> $Manual\_Performance_{t-n}$ </td><td>Controlled</td></tr><tr><td>Investment characteristics</td><td>Controlled</td></tr><tr><td>Lender &amp; month fixed effects</td><td>Yes</td></tr><tr><td>Observations</td><td>10,909</td></tr><tr><td>Lenders</td><td>18,18</td></tr><tr><td> $R^2$ </td><td>0.174</td></tr></table>

$$
^ {*} p <   0. 1.
$$

Table 9. The Effect of RA Usage Adjustment on Investment Performance

<table><tr><td>Variable</td><td>(1) ReturnRate</td><td>(2) ReturnRate</td></tr><tr><td> $RAShare\_Adjustment$ </td><td>-0.001**(0.000)</td><td>-0.002**(0.001)</td></tr><tr><td> $RAShare$ </td><td>-0.000***(0.000)</td><td>-0.013***(0.002)</td></tr><tr><td>Investment characteristics</td><td>Controlled</td><td>Controlled</td></tr><tr><td>Lender characteristics</td><td>Controlled</td><td>Controlled</td></tr><tr><td>Lenders</td><td>1751</td><td>1205</td></tr><tr><td> $R^2$ </td><td>0.372</td><td>0.354</td></tr></table>

\*\*p < 0.05; \*\*\*p < 0.01.

translates into a decrease of nearly 235 RMB in annual return for an average investor, when she increases RA usage by 10% in its coef<sup>fi</sup>cient of variation, holding her mean and standard deviation of RAShare constant at 42% and 43%, respectively. For the second sample, a one-unit increase in RAShare\_Std decreases the average monthly return rate by 0.1%—that is, a 1.2% decrease in the average annual return rate. Hence, it seems better to let the algorithms do the work; having humans (lenders) in the decision loop in terms of enabling or disabling RA services can be counterproductive. RAs aim to achieve long-term portfolio optimization concerning risk and return, which means there is a longterm mean that the RA targets. A bad loan is just a small deviation from the long-term mean. Manually adjusting the usage of RAs too frequently and substantially may inadvertently disrupt the stochastic process of RA performance, leading to inferior performance.

## 6.3. Robustness Checks

6.3.1. Coarsened Exact Matching. Here, we apply a CEM approach to strengthen identi<sup>fi</sup>cation. We <sup>fi</sup>rst divide lenders into two groups based on RAShare\_ CoV. Lenders in the top 20% of RAShare\_CoV form the treatment group (n 241), and lenders in the bottom 20% of RAShare\_CoV form the control group (n 238). We utilize the CEM method to eliminate the difference caused by the covariates between the two groups and then regress the outcome variable on the treatment. We match the two groups with the two sets of covariates, investment characteristics and lender characteristics, with two CEM procedures. In the <sup>fi</sup>rst procedure, 134 lenders are matched. The matched samples are mostly balanced, except for experience. In the second procedure, 59 lenders are matched. The matched samples are completely balanced. Table 10 tabulates the logit regression results of covariates before and after matching. We then use the matched samples to regress lenders’ ReturnRate on the treatment. Table 11 shows that the treatment has signi<sup>fi</sup>cant and negative effects on ReturnRate, consistent with the main models’ results.

Table 10. The Logit Speci<sup>fi</sup>cations Before and After Matching

<table><tr><td>Treatment</td><td>(1)Unmatched</td><td>(2)CEM_1</td><td>(3)CEM_2</td></tr><tr><td>RAShare</td><td>-11.455***(1.927)</td><td>-0.894(1.263)</td><td>-0.554(1.701)</td></tr><tr><td>InterestRate</td><td>0.063(0.077)</td><td>-0.133(0.151)</td><td>-0.086(0.199)</td></tr><tr><td>Term</td><td>-0.405***(0.118)</td><td>0.026(0.251)</td><td>0.082(0.256)</td></tr><tr><td>ln(BidAmount)</td><td>0.454(0.280)</td><td>0.257(0.564)</td><td>0.227(0.702)</td></tr><tr><td>ln(TotalAmount)</td><td>-0.218(0.214)</td><td>0.028(0.252)</td><td>0.127(0.289)</td></tr><tr><td>Age</td><td>-0.024(0.023)</td><td>0.031(0.039)</td><td>0.010(0.042)</td></tr><tr><td>Gender</td><td>-0.280(0.569)</td><td>1.207(0.891)</td><td>1.252(1.124)</td></tr><tr><td>Experience</td><td>0.469**(0.205)</td><td>1.505***(0.523)</td><td>-0.411(1.048)</td></tr><tr><td>Observations</td><td>479</td><td>134</td><td>59</td></tr><tr><td> $R^2$ </td><td>0.836</td><td>0.240</td><td>0.044</td></tr></table>

\*\*p < 0.05; \*\*\*p < 0.01.

6.3.2. Causal Forest. As a sensitivity analysis to further solidify identi<sup>fi</sup>cation, we applied a causal forest approach to estimate the treatment effect (Wager and Athey 2018). Causal forest has been widely used to estimate and infer heterogeneous treatment effects (e.g., Davis and Heller 2017 and Luo et al. 2019). In our case, however, we are not attempting to estimate heterogeneous treatment effects. Instead, we use this approach as an alternative matching method to CEM, where the samples falling into each leaf are considered homogeneous. We treat RAShare\_CoV as a treatment variable and use regression trees to build a causal forest. The results show that the average treatment effect of RAShare\_ CoV is 0.0024, and its 95% con<sup>fi</sup>dence interval is [ 0.0045, 0.0003]. This analysis further corroborates that the adjustment exerts a signi<sup>fi</sup>cant and negative effect on ReturnRate, consistent with our main results.

6.3.3. Adjustment Direction. In the above analysis, RAShare\_Adjustment only measures the intensity of adjustments, without considering the direction of adjustments. Potentially, investors may decrease RA shares when RAs did not do well in the previous period or, conversely, increase RA shares when RAs performed well. To determine which type of adjustment leads to worse return rates, we examine the moderating effect of the adjustment direction.

Table 11. The Effect of Treatment on ReturnRate

<table><tr><td></td><td>(1)</td><td>(2)</td></tr><tr><td>ReturnRate</td><td>CEM_1</td><td>CEM_2</td></tr><tr><td>Treat</td><td>-0.007**(0.003)</td><td>-0.012*(0.006)</td></tr><tr><td>Constant</td><td>0.049***(0.002)</td><td>0.052***(0.003)</td></tr><tr><td>Observations</td><td>134</td><td>59</td></tr><tr><td> $R^2$ </td><td>0.024</td><td>0.048</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Table 12. The Moderating Effect of RA Adjustment Direction

<table><tr><td>Variable</td><td>ReturnRate</td></tr><tr><td> $RAShare\_CoV$ </td><td>-0.002**(0.001)</td></tr><tr><td> $Direction \times RAShare\_CoV$ </td><td>-0.001(0.001)</td></tr><tr><td> $RAShare$ </td><td>-0.011***(0.002)</td></tr><tr><td>Investment characteristics</td><td>Controlled</td></tr><tr><td>Lender characteristics</td><td>Controlled</td></tr><tr><td>Lenders</td><td>664</td></tr><tr><td> $R^{2}$ </td><td>0.461</td></tr></table>

\*\*p < 0.05; \*\*\*p < 0.01.

We calculate Direction for lenders who made more than two adjustments by summing up their adjustment directions. For example, if a lender made 10 adjustments in total (e.g., three for increasing RAShare and seven for decreasing RAShare), then their Direction value is 4. We add the interaction of Direction and RAShare\_CoV into Equation (4) and present the results in Table 12. Direction has no signi<sup>fi</sup>cant moderating effect on the relationship between RAShare\_CoV and ReturnRate, which means that when the mean RA share is the same, regardless of whether a lender increases or decreases the RA share, more adjustments always mean worse investment performance.

## 7. Conclusion

Robo-advising has proliferated, becoming a central topic in <sup>fi</sup>ntech. RA services are designed to provide crowds affordable wealth-management services without human intervention. It is important to understand how investors interact with RAs and how RAs augment investment performance in order to improve their design. However, there are a lack of studies on investor adoption, usage, and interaction with RAs. We <sup>fi</sup>ll in these gaps by conducting empirical studies in a setting of P2P lending with RA services.

We <sup>fi</sup>nd that investors who have encountered more defaults are less likely to adopt the RA service, suggesting that investors’ adoption of RA is affected by their past investment performance. For investors who have adopted RA services, we <sup>fi</sup>nd that they swiftly adjust their RA usage based on recent RA performance, but such interventions undermine their own investment performance. Our study’s <sup>fi</sup>ndings help RA marketers and designers understand and predict user behavior regarding RA adoption and usage and help them better design the RAs thereof.

More broadly speaking, due to the complexity of algorithms, most intelligent systems are designed as black boxes, at least as far as users are concerned. However, to ensure that the system works orderly and ef<sup>fi</sup>- ciently, the providers of intelligent systems need to offer more transparency of their services, for example, by communicating with users on system objectives, offering adequate explanations of the inner-working mechanisms, and providing proper evaluation schemes. Furthermore, a well-designed intelligent system should anticipate possible user behaviors and account for such human factors in its system design. It is especially important to know when it is bene<sup>fi</sup>cial to include humans in the loop of a system’s deployment. All of these implications require a clear understanding of how users might adopt and react to the systems.

There are a few caveats one needs to bear in mind when interpreting or generalizing our results. First, we do not observe what loans are available to lenders or what loans an RA recommends at a particular point in time. It is possible that RAs may recommend the same loans to different lenders, leading to a correlated and crowded bidding environment. Consequently, this may lead to correlated performance among certain lenders. We believe this should not be a serious problem in our analysis because the platform we collaborated with has a large volume of active borrower requests. However, this is an interesting future research topic when data on loan availability and RA recommendations become available. Moreover, we do not observe these lenders’ <sup>fi</sup>nancial literacy, which may affect their reliance on RAs. Finally, our study only focuses on the effect of investors’ enabling and disabling RA services. It would warrant an interesting future study to examine the impact of humans in the loop of the RA design phase, where lenders can recon<sup>fi</sup>gure and tune the investing parameters directly.

## Acknowledgments

The authors gratefully acknowledge the guidance received from the special section coeditors, associate editor, and the reviewer team. They are also grateful to Kartik Hosanagar, Jason Chan, and the participants at the Special Section Workshop at Chattanooga and the seminar at Temple University for their insightful comments on an early version of the paper.

## Endnotes

<sup>1</sup> See https://www.investopedia.com/terms/r/roboadvisor-roboad viser.asp (last accessed June 5, 2020).

<sup>2</sup> For example, Betterment charges 0.25% for management fee, and Wealthfront requires a minimum of \$500 for each investment; see https://www.betterment.com/pricing/ (accessed April 1, 2021).

<sup>3</sup> See www.financialsamurai.com/personal-capital-investment, last accessed.12/02/2019.

<sup>4</sup> See https://www.roboadvisorpros.com/robo-advisors-with-most -aum-assets-under-management (accessed December 2, 2019).

<sup>5</sup> The nondisclosure agreement we signed with the company requires us to ensure anonymity of the name of the company.

<sup>6</sup> The company randomly selected these samples according to the last two digits of lenders’ user IDs. Each user ID is generated based on lenders’ registration sequences. The random sample accounts for 0.3% of the entire lender population in 2015.

<sup>7</sup> The distributions of gender and age in our sample are similar to the population statistics released by the platform in 2016. A few lenders did not report their genders or ages, making the number of records (N in Table 1) of the two variables slightly smaller than that of others.

<sup>8</sup> The monthly return rate is calculated based on the equation specified by the platform—that is, ReturnRate (Rinterests obtained in the focal month Rprincipal losses in the focal month)/Rprincipals that were lent out in the focal month.

<sup>9</sup> We also model the hazard of adoption as a function of previous performance. The results, presented in the online appendix, are consistent with the main models.

<sup>10</sup> We also estimate Equations (1) and (2) with a larger adoption window, T 6, which covers nearly 90% tryouts after the launch of the RA service. The results are consistent with the results of T 1 and T 3. The details are presented in the online appendix.

<sup>11</sup> We use these two performance measures because ReturnRate<sub>i</sub> and #Default<sub>i</sub> are directly displayed on the monthly report provided by the platform to lenders. However, %Default is not provided by the platform. Because the loans defaulted in a month may originate from loans invested at different months, there is no uniform way to determine the value of %Default accurately.

## References

Arnold V, Collier P, Leech S, Sutton S (2000) The effect of experience and complexity on order and recency bias in decision making by professional accountants. Accounting Finance 40(2): 109–134.

Attenberg J, Ipeirotis P, Provost F (2015) Beat the machine: Challenging humans to <sup>fi</sup>nd a predictive model’s “unknown unknowns.” J. Data Inform. Quality 6(1):1–17.

Blackwell M, Iacus S, King G, Porro G (2009) CEM: Coarsened exact matching in Stata. Stata J. 9(4):524–546.

Campbell D, Frei F (2010) Cost structure, customer pro<sup>fi</sup>tability, and retention implications of self-service distribution channels: Evidence from customer behavior in an online banking channel. Management Sci. 56(1):4–24.

Cushing B, Ahlawat S (1996) Mitigation of recency bias in audit judgment: The effect of documentation. Auditing 15(2):110–122.

D’Acunto F, Prabhala N, Rossi AG (2019) The promises and pitfalls of robo-advising. Rev. Financial Stud. 32(5):1983–2020.

Davis J, Heller SB (2017) Using causal forests to predict treatment heterogeneity: An application to summer jobs. Amer. Econom. Rev. 107(5):546–550.

Deese J, Kaufman R (1957) Serial effects in recall of unorganized and sequentially organized verbal material. J. Experiment. Psych. 54(3):180–187.

D’Hondt C, De Winne R, Ghysels E, Raymond S (2019) Arti<sup>fi</sup>cial intelligence alter egos: Who bene<sup>fi</sup>ts from robo-investing? Preprint, submitted November 6, https://dx.doi.org/10.2139/ssrn .3415981.

Dietvorst BJ, Simmons JP, Massey C (2015) Algorithm aversion: People erroneously avoid algorithms after seeing them err. J. Experiment. Psych. Gen. 144(1):114–126.

Dietvorst BJ, Simmons JP, Massey C (2016) Overcoming algorithm aversion: People will use imperfect algorithms if they can (even slightly) modify them. Management Sci. 64(3):1155–1170.

Duarte J, Siegel S, Young L (2012) Trust and credit: The role of appearance in peer-to-peer lending. Rev. Financial Stud. 25(8): 2455–2483.

Featherman M, Pavlou P (2003) Predicting e-services adoption: A perceived risk facets perspective. Internat. J. Human Comput. Stud. 59(4):451–474.

Friedberg B (2018) Six of the newest trends in robo advisors. USNews (June 27), https://money.usnews.com/investing/investing-101/ articles/2018-06-27/6-of-the-newest-trends-in-robo-advisors.

Friedberg BA (2019) How do robo-advisors work? Roboadvisorpros (January 27), https://www.roboadvisorpros.com/how-do-robo -advisors-work.

Fugener A, Grahl J, Gupta A, Ketter W (2019) Collaboration and¨ delegation between humans and AI: An experimental investigation of the future of work. ERIM Report Series Research in Management, Erasmus Research Institute of Management, Erasmus University Rotterdam, Rotterdam, Netherlands.

Ge R, Feng J, Gu B (2017) Predicting and deterring default with social media information in peer-to-peer lending. J. Management Inform. Systems 34(2):401–424.

Germann M, Merkle C (2019) Algorithm aversion in <sup>fi</sup>nancial investing. Preprint, submitted November 6, https://dx.doi.org/10 .2139/ssrn.3364850.

Hitt LM, Frei FX (2002) Do better customers utilize electronic distribution channels? The case of PC banking. Management Sci. 48(6):732–748.

Iacus SM, King G, Porro G (2012) Causal inference without balance checking: Coarsened exact matching. Politcal Anal. 20(1):1–24.

Iyer R, Khwaja I, Luttmer P (2016) Screening peers softly: Inferring the quality of small borrowers. Management Sci. 62(2):1554–1577.

Jiang Y, Ho Y, Yan X, Tan Y (2020) When online lending meets real estate: An empirical investigation of lender behavior in realestate crowdfunding. Inform. Res. Systems 31(3):715–730.

Jung D, Dorner V, Glaser F (2017) Robo-advisory. Bus. Inform. Systems. Engrg. 60(1):81–86.

Jung D, Dorner V, Weinhardt C, Pusmaz H (2018) Designing a robo-advisor for risk-averse, low-budget consumers. Electronic Marketing 28(3):367–380.

KPMG (2016) Robo advising: Catching up and getting ahead. https://home.kpmg/content/dam/kpmg/pdf/2016/07/Robo -Advising-Catching-Up-And-Getting-Ahead.pdf.

Lin M, Prabhala R, Viswanathan S (2013) Judging borrowers by the company they keep: Friendship networks and information asymmetry in online peer-to-peer lending. Management Sci. 59(1): 17–35.

Lopez C, Babcis S, De-laOssa A (2015) Advice goes virtual: How new digital investment services are changing the wealth management landscape. J. Financial Perspect. 3(2):156–164.

Ludwig L (2020) Best robo advisors for 2020. InvestorJunkie (February 1), https://investorjunkie.com/best-robo-advisors/.

Luo X, Lu X, Li J (2019) When and how to leverage e-commerce cart targeting: The relative and moderated effects of scarcity and price incentives with a two-stage <sup>fi</sup>eld experiment and causal forest optimization. Inform. Systems Res. 30(4):1203–1227.

Markowitz H (1952) Portfolio selection. J. Finance 7(1):77–91.

Murdock B (1962) The serial position effect of free recall. J. Exp. Psychol. 64(5):482–488.

Musto C. Semeraro G. Lops P. De Gemmis M. Lekkas G (2015) Personalized <sup>fi</sup>nance advisory through case-based recommender systems and diversi<sup>fi</sup>cation strategies. Decision Support Systems 77(9):100–111.

Paravisini D, Rappoport V, Ravina E (2016) Risk aversion and wealth: Evidence from person-to-person lending portfolios. Management Sci. 63(2):279–297.

Park J, Ryu J, Shin H (2016) Robo-advisors for portfolio management. Adv. Sci. Tech. Lett. 141(1):104–108.

Pompian M (2011) Behavioral Finance and Wealth Management: How to Build Investment Strategies that Account for Investor Biases (John Wiley & Sons, Hoboken, NJ).

Schanke S, Burtch G, Ray G (2021) Estimating the impact of ‘humanizing’ customer service chatbots. Inform. Systems Res., ePub ahead of print May 24, https://doi.org/10.1287/isre.2021.1015.

Schierz PG, Schilke O, Wirtz BW (2010) Understanding consumer acceptance of mobile payment services: An empirical analysis. Electronic Commerce Res. Appl. 9(3):209–216.

Srivastava SC, Chandra S, Theng YL (2010) Evaluating the role of trust in consumer adoption of mobile payment systems: An empirical analysis. Commun. Assoc. Inform. Systems 27:561–588.

Tversky A, Kahneman D (1974) Judgment under uncertainty: Heuristics and biases. Science 185(4157):1124–1131.

Venkatesh V, Morris M, Davis G, Davis F (2003) User acceptance of information technology: Toward a uni<sup>fi</sup>ed view. MIS Quart. 27(53):425–478.

Wager S, Athey S (2018) Estimation and inference of heterogeneous treatment effects using random forests. J. Amer. Statist. Assoc. 113(523):1228–1242.

Wang J, Ipeirotis PG, Provost F (2017) Cost-effective quality assurance in crowd labeling. Inform. Systems Res. 28(1):137–158.

Xin D, Ma L, Liu J, Macke S, Song S, Parameswaran A (2018) Accelerating human-in-the-loop machine learning: Challenges and opportunities. DEEM’18 Proc. Second Workshop Data Management End-to-End Machine Learn. (Association for Computing Machinery, New York), 1-4.

Xu J, Chau M (2018) Cheap talk? The impact of lender-borrower communication on peer-to-peer lending outcomes. J. Management Inform. Systems 35(1):53–85.

Yin J, Luo J, Brown SA (2021) Learning from crowdsourced multilabeling: A variational Bayesian approach. Inform. Systems Res. Forthcoming.

Zhou T (2013) An empirical examination of continuance intention of mobile payment services. Decision Support Systems 54(2):1085–1091.

C<sub>opy</sub>ri<sub>g</sub>ht 202 1 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>express wr</sub>itt<sub>en perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
