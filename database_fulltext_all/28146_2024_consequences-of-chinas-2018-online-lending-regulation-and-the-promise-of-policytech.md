---
otero_id: 28146
otero_key: "P3QWX4MZ"
title: "Consequences of China’s 2018 Online Lending Regulation and the Promise of PolicyTech"
authors: "Yidi Liu; Xin Li; Zhiqiang (Eric) Zheng"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.0580"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Consequences of China’s 2018 Online Lending Regulation and the Promise of PolicyTech

Yidi Liu,<sup>a,</sup>\* Xin Li,<sup>b,</sup>\* Zhiqiang (Eric) Zheng<sup>c,</sup>\*

<sup>a</sup> School of Management and Economics and Shenzhen Finance Institute, Chinese University of Hong Kong, Shenzhen, Shenzhen 518172, China; <sup>b</sup> Department of Information Systems, College of Business, City University of Hong Kong, Hong Kong, China; <sup>c</sup> Department of Information Systems and Operations Management, Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080 \*Corresponding authors

Contact: Yidi.Liu.PhD@gmail.com, https://orcid.org/0000-0002-7285-0405 (YL); Xin.Li.PhD@gmail.com,

Received: November 11, 202 Revised: July 17, 2022; December 12, 2022; July 25, 2023 Accepted: August 18, 2023 Published Online in Articles in Advance: September 29, 2023

https://doi.org/10.1287/isre.2021.0580

Copyright: © 2023 INFORMS

Abstract. Financial regulators often focus on containing risks in financial services; however, they may not simultaneously pay adequate attention to regulation’s adverse effects. This study examines how the economic development of borrowers was affected by China’s suppressive regulation of peer-to-peer (P2P) lending in 2018, which unexpectedly switched from an “all-in” policy to an “all-shutdown” policy, leading to a massive closure of P2P lending companies and the eventual shutdown of the entire industry by 2021. Leveraging data on individuals’ credit applications, we show that this one-size-fits-all regulation obstructed borrowers’ economic development potential, especially for underprivileged and underserved borrowers, as reflected by their credit scores and their selection of financial channels. To alleviate the unintended adverse effects, we advocate using artificial intelligence (AI) to stipulate personalized regulation as a PolicyTech solution. We demonstrate that by restricting some borrowers’ access to P2P lending according to their AI-predicted financial risk, it is possible to protect borrowers’ overall economic development opportunity, while containing credit risks. This work yields significant theoretical and societal implications.

History: Olivia Sheng, Senior Editor; Huaxia Rui, Associate Editor.

Funding: Financial support from the National Natural Science Foundation of China [Grant 71831006], the Research Grant Council Hong Kong [Grants GRF 11501722 and 11500519], the InnoHK initiative, the Government of the Hong Kong Special Administrative Region, and the Laboratory for AI-Powered Financial Technologies is gratefully acknowledged.

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.0580.

Keywords: individual economic development • P2P lending regulation • AI • fintech

## 1. Introduction

Access to credit is critical to the economic development of individuals. Although banks are a well-known source of credit, a large portion of financial needs are not served by banks. Collectively referred to as Alternative Financial Services (AFS), credit channels such as microloans, payday loans, and peer-to-peer (P2P) lending were invented to fill this gap (Smith et al. 2008). In recent years, the internet has significantly eased access to AFS, leading to its rapid development. For example, in China, internet channels at their peaks provided 1 trillion U.S. dollars’ worth of credit in early 2018,<sup>1</sup> expanding 400 times from 2014, partially due to the Chinese government’s open support for this industry during this period of time.

However, as a high-cost credit channel, the role of AFS in society has been constantly debated. On the one hand, AFS provide credit to those in need, thus helping alleviate poverty (Wahid 1994). On the other hand, AFS are criticized for their high costs and negative consequences. For example, payday loans have been blamed for exacerbating borrowers’ economic hardships (Melzer 2011) and causing personal bankruptcies (Skiba and Tobacman 2019, Wang and Overby 2021). Because AFS are a double-edged sword, they often come under suppressive government regulations. The rampant growth of online lending in China also cultivated a credit bubble full of default risks and illegal practices, prompting the regulatory authority to tighten regulations in May 2018, with P2P lending firms as the main target. This led to a massive shutdown of P2P lending platforms. By the end of 2020, the entire industry was closed (PBC 2021).

Although financial regulations are commonly employed to contain financial risks, their societal impact (as in the case of China’s online lending market) has not been fully understood. Regulating AFS reduces the supply of high cost credit (McKernan et al. 2013). Regulators may anticipate that borrowers will then turn to lower-cost credit sources, such as bank loans (Bhutta et al. 2016). However, in reality, borrowers may be left with no choice but to seek higher-cost alternatives. The abrupt P2P lending regulation in China provides a unique opportunity to isolate the effect of such a suppressive policy on borrowers.

We investigate the impact of China’s regulatory policy on the change of borrowers’ economic status using a loan-application data set from a leading credit-scoring company in China, containing 80,000 randomly selected loan applicants from 2017 to 2019. Our econometrics analysis exploits the variation between P2P borrowers and non-P2P borrowers (borrowers seeking and not seeking P2P lending), who benefited differently from the government’s support of online lending before 2018. We investigate the impact of the regulation on borrowers’ credit scores and credit-channel choices (e.g., banks versus nonbanks), which reflect borrowers’ economic stratification within a financial system (Fourcade and Healy 2013).

Our analyses reveal that P2P borrowers and non-P2P borrowers exhibited different momentum in economic development before regulation. However, the relative advantage of P2P borrowers decreased after the regulation took place. The difference in the trend of economic development across the two groups before regulation poses a challenge in identification because it violates the parallel-trend assumption needed for a conventional difference-in-differences (DID) setting. We address this issue by using DID with a linear group-specific trend (Jayachandran et al. 2010) in conjunction with coarsened exact matching (CEM). The finding is consistent across a series of robustness checks, including the Honest DID methods (Rambachan and Roth 2023), which are specifically designed to account for the non-parallel-trend issue, and a fixed-effects counterfactual (FECT) analysis with linear group-specific trend. We show that this effect is stronger in regions that are less developed, more rural, and have fewer financial facilities and for borrowers who are younger or have fewer bank experiences (who tend to be the “invisible primes,” according to Di Maggio et al. 2021).

Our findings reveal a dilemma faced by policymakers between maintaining economic development and preventing financial risks when designing regulations. In view of this, we explore the possibility of achieving both goals with PolicyTech, a technical solution that restricts a portion of borrowers’ access to P2P lending based on AI prediction of their financial risk. We show how this ambidextrous policy is able to achieve both goals of economic development and risk management through simulated counterfactual analyses.

The remainder of this paper is organized as follows. Section 2 introduces the background and our data. Section 3 reviews the existing studies and discusses the theoretical basis. Section 4 elaborates on our methodology. Section 5 presents the results and explores the heterogeneous effects. Section 6 discusses how PolicyTech works, and Section 7 concludes the paper.

## 2. Research Context

## 2.1. Credit Channels in China

In China, the credit market consists of several channels. On one end of the spectrum are banks, mainly serving the low-risk sector of credit demands. Besides mort gages and car loans, which require collateral, banks also offer short-term loans (through credit cards) and medium-term loans (one to three years), such as college loans. In China, bank loan borrowers typically have stable jobs, higher incomes, and better credit histories. Banks tend to have a low (less than 1%) nonperforming loan ratio (NPL ratio).<sup>2</sup>

Consumer finance (CF) fulfills the short-term credit demand for durable consumer goods (e.g., electronics, appliances, and cars) or services (e.g., education expenses and house rentals). In China, CF service can only be provided by licensed financial firms with adequate reserved capital. Often, the purchased goods or services are used as collateral. Owing to straightforward risk control using the collateral, the CF default rate is relatively low, with an average 2.6% NPL ratio.

Microloan (ML) services, which issue small loans with short-term maturity, existed well before the internet era. The internet has enabled microloan companies to reach a large market. Companies offering MLs are required to own sufficient capital in reserve and can only lend their own capital to borrowers. MLs often do not require collateral. Borrowers only need to present their ID and proof of occupation and income to borrow. This segment relies heavily on government and third-party credit-scoring services to assess the default risk. Even with such sup port, the default risk is high because there is no guarantee or insurance on payments. The leading internet-based ML firms, on average, have around a 5% NPL ratio.<sup>4</sup>

At the low end of the market is peer-to-peer lending, where firms do not provide funds directly to consumers. Rather, they operate as an information intermediary to match lenders with borrowers and facilitate money transfers between the two parties. Thus, they do not require a financial license in China. P2P lending tends to have a higher risk than other channels due to the lenders’ lack of control over loan collections. Thus, some P2P platforms introduce insurance on issued loans to attract lenders. A few of them partner with creditors to use autos, houses, or collectibles as collateral. But the majority of these firms operate without collateral. The NPL ratio was estimated to be over 10% in the P2P lending industry.<sup>5</sup>

In the credit market, there are some other firms (Other) providing credit that does not naturally fall into one of the above categories. These firms mostly offer high-cost credit with a risk level similar to microloan or P2P lending.

## 2.2. The 2018 P2P Lending Regulation: A Natural Experiment

Internet-based lending channels, mostly P2P lending, serve a large borrower population in China. Because of the lack of adequate regulation, some P2P lending companies not only matched lenders with borrowers, but also formed a pooled fund collected from lenders to loan money to borrowers through their own accounts. This made money transfers between lenders and borrowers untraceable, which left room for the lending companies to circumvent regulations and use the collected capita for other purposes. In addition, serving low-end borrowers means a higher default risk. Without proper risk management by P2P lending platforms, the market faced significant defaults of borrowers. Related to the high default rate, another often-criticized issue with P2P lending is the violent loan-collection practices of some P2P lending firms, generating a negative social image.

Given these issues, the Chinese government took measures to regulate the P2P lending market in 2018, with June 2018 as the targeted time for enforcement.<sup>6</sup> In May 2018, the government announced the decree to regulate P2P lending<sup>7</sup> by the joint efforts of the China Banking Regulatory Commission, the Ministry of Public Security, the State Administration for Market Regulation, and the People’s Bank of China (PBOC), targeting illegal fundraising and pooled funds, among other actions. The abrupt announcement and enforcement of these regulations caught the P2P lending industry off-guard and caused a massive wave of bankruptcies. As shown in Figure 1, the number of monthly bankruptcies of P2P lending platforms increased from an average of 20 to 70 in June 2018, skyrocketed to 200 in July, then hovered at around 50 afterward. After this regulation, no new platforms were launched, and by January 2021, the government announced that all P2P lending platforms had been closed (PBC 2021). Not only did the number of P2P platforms dwindle, but P2P lenders were shunned because of the regulation. Figure 1 shows that the number of lenders and transactions rapidly decreased within three to four months after regulation, then stabilized. As a result, the credit supply on the market significantly decreased. In

Figure 1. (Color online) China’s P2P Industry in 2018  
![](/api/attachments/P3QWX4MZ/fulltext/images/3957c7ab682d0fdce9915d236109331ef4f43b1bf9d67b57f553f2be0d7b1490.jpg)  
Bankrupted P2P PlatformsNumber ofLenders---Transaction Amount

July 2018, over 70 billion renminbi (RMB) flew out of the P2P lending market, compared with an inflow of 5.6 billion and 15 billion RMB in May and June 2018, respectively (Li 2018). Although the impact of the regulation on the supply side of the credit market is obvious, it is unclear how it impacts the demand side (borrowers). We explore this question in this study.

## 3. Theoretical Basis

## 3.1. Credit and High-Cost Credit

The importance of access to finance has been highlighted in the literature regarding helping individuals accumulate wealth (Ce´lerier and Matray 2019), improving credit scores (Brown et al. 2019), and boosting entrepre neurship (Bittencourt 2012). Chopra and Tantri (2017) showed that providing bank accounts to the unbanked leads to significant uptake, usage, usage growth, and balance accumulation in these accounts. In their study of the Freedman’s Savings Bank, Stein and Yannelis (2020) found that providing the unbanked population with access to banking services could facilitate their literacy rates, occupational income, business ownership, real estate wealth, and their children’s education. Previous studies also found that receiving need-based financial aid could improve the achievement of low-income students (London˜ o-Ve´lez et al. 2020) and alleviate personal bankruptcy (Danisewicz and Elard 2023).

Although the benefits of low-cost credit and financial services are widely accepted, high-cost credit, such as microloans and P2P lending, can be a double-edged sword for consumers. On the one hand, providing credit to those in need alleviates poverty and improves equality (Beck et al. 2007). Previous research has shown that access to such credit is important for labor reproduction (Beck et al. 2010, Becchetti and Castriota 2011), the success of small businesses (Gatti and Love 2008), and entrepreneurship (Afrin et al. 2009). For example, the microloan pioneer Grameen Bank was credited with increasing its customers’ income and society’s productivity (Wahid 1994). P2P lending was also found to help meet the capital needs of start-up businesses (Kim and Hann 2019). On the other hand, many AFS have been criticized for their high costs and negative consequences. Payday loans, for example, have been shown to undesirably increase borrowers’ economic hardship (Melzer 2011) and personal bankruptcy rates (Skiba and Tobacman 2019). Furthermore, P2P lending was also blamed for bankruptcies due to its high interest rates and strict payment terms (Skiba and Tobacman 2019).

## 3.2. Effects of Regulating High-Cost Credit

In view of the negative effects of high-cost credit, gov ernments often enact suppressive regulatory policies. For example, in the United States, payday loans were restricted in nine states and declared illegal in 14 states and Washington, DC (Bhutta et al. 2016). In 2013, Chile reduced the maximum legal interest rate for consumer loans from 54% to 36% (Madeira 2019). China’s 2018 P2P regulation joined these efforts to reduce the risk and illegal practices in the financial system.

In the literature, there are abundant empirical studies on the effect of bank regulations (Thamae and Odhiambo 2022). Many of these studies have found that suppressive regulations caused the shrinkage of bank loans (Peek and Rosengren 1995), whereas loose regulations boosted small business lending (Srivastav and Vallascas 2022). In contrast, studies on high-cost credit regulations are scarce. Among the few, Ramirez (2020) studied paydayloan regulation and found that enforcing price ceilings and liquidity requirements decreased supply branches. Cozarenco and Szafarz (2020) reported that applying a microloan size ceiling reduced the number of applications. Regarding P2P lending, most of these studies mainly express viewpoints on what proper regulation would involve (Nemoto et al. 2019), without rigorously analyzing the societal impact of the regulations on the lives of different stakeholders. For example, Rogers and Clarke (2016) conducted interviews on the UK’s policy and concluded that the UK regulation intended to make P2P lending more socially useful. Other studies (Verstein 2011) suggested that the U.S. regulation was overly rigorous, whereas China’s was inadequate (You 2018). Within the extant literature, it is not clear how a sudden P2P lending regulation, such as China’s suppressive policy, may affect the economy, such as borrowers’ economic status. This is a gap we seek to fill in this study by investigating the consequence of the regulation on the low-end segment of borrowers, including the underprivileged and underserved customers.

3.2.1. Entrapment of Low-End Borrowers Within High-Cost Credit. As illustrated in Figure 2 and discussed in Section 2.1, P2P lending is located at the lower end of the credit market. Many borrowers choose P2P lending because they are excluded from formal financial credit such as bank loans (Allen et al. 2016) due to a lack of credit history (Bhutta et al. 2015), unhealthy economic status (Gross and Hogarth 2012), or lending biases due to gender (Funga´cˇova ´ and Weill 2015), education (Funga´cˇova ´ and Weill 2015), or ethnicity (Bayer et al. 2018).

Figure 2. (Color online) Regulation Shock and Segments of China's Credit Market  
![](/api/attachments/P3QWX4MZ/fulltext/images/6917c28c101a07eafb6cb3ff01daab548ca65b1a3533b92c917f591c79587ace.jpg)

A suppressive financial regulation would reduce the credit supply in the lending market. The credit-supply shortage in the P2P lending channel would be first felt by P2P lending borrowers (low-end borrowers). Because of transparency of the lending activities on P2P-lending platforms (Lu et al. 2022), a regulation’s impact would be quickly felt by other borrowers, triggering instant herding behavior, such as switching to other platforms (Jiang et al. 2018). When imposing a regulation, regulators may expect to drive some borrowers to high-end (low-cost) credit. However, compared with their highend counterparts, low-end borrowers tend to have fewer credit-channel choices, and it is often more difficult for them to access low-cost credit. The limited channels available further intensifies competition between borrowers, making it harder for low-end borrowers to compete for credit from the remaining accessible channels. As a result, some low-end borrowers may be left with no choice but to seek credit with even higher costs or, worse, go bankrupt due to credit rationing (Danisewicz and Elard 2023). For instance, after Chile regulated its interest rate, 9.7% of borrowers were excluded from bank loans and resorted to higher-cost credit (Madeira 2019).

Because low-end borrowers may end up seeking high cost credit, P2P lending regulation could limit their chances of improving their economic status. In their book Poor Economics (Banerjee and Duflo 2011), 2019 Nobel laureates Abhijit Banerjee and Esther Duflo described a similar “poverty trap” phenomenon, where external financial support fails to catapult the poor out of the trap because these investments cannot recover their costs. Similarly, once low-end borrowers fall into the high-cost segment of the credit market, it is difficult fo them to recover from the high interest on these loans.

The reduced credit supply under a P2P lending regulation thus intensifies borrower competition and may leave borrowers to the hands of high-cost channels. We refer to this phenomenon as the “entrapment effect.”

3.2.2. Exacerbation of the Underprivileged. Within the low-end market, access to credit is especially vital to allow the underprivileged (e.g., the poor) to improve their economic status by providing them a chance to engage in economic development activities (Banerjee et al. 2015). In the economics literature, it is well documented that the underprivileged are more susceptible to economic hardship in a market with a limited credit supply. This group tends to spend more on basic needs (Hallegatte et al. 2020) and less on discretionary expenditures such as luxury jewels (Karim and Noy 2016, Hallegatte et al. 2020). When they need funds to cope with health shocks (Islam and Maitra 2012), natural disasters (Morse 2011), or accidents (Langley et al. 2019), if the credit supply is tightened due to a suppressive financial regulation, the underprivileged may have little or no room to cut their indispensable necessity spending, but seek higher-cost credit, further deteriorating their economic status. In contrast, high-end borrowers tend to have more room to maneuver—for example, by cutting down on discretionary expenditures to cope with difficulties. Thus, a suppressive regulation is more likely to exacerbate the underprivileged than for highend borrowers.

Moreover, the underprivileged tend to have less access to formal credit services. There are generally fewer (physical) bank branches in regions with more underprivileged populations (Banerjee and Duflo 2011), partially because there are fewer business opportunities that would enable banks to cover their operation costs. To fight poverty, Banerjee and Duflo suggested that governments should regulate banks to open more branches in less developed regions to help the underprivileged access credit, which is critical for their economic development (Hasan et al. 2019). P2P lending and other internet-based channels significantly alleviate the hurdle of credit access for the underprivileged. A regulation on the P2P channel, which removes a significant portion of credit access, would hurt the underprivileged more because of the low availability of formal credit to them and their higher reliance on internet-based credit access.

Thus, a regulation restricting access to P2P lending would exert a more negative impact on the underprivileged segment of borrowers, which we term the “exacerbation effect.”

3.2.3. Exclusion of the Underserved. Another major segment of P2P lending borrowers is the underserved borrowers, such as those with a shorter credit history, who are more likely to be excluded from traditiona credit channels (e.g., banks). The suppressive regulation could cause further exclusion of these borrowers, which can be attributed to the extensive use of advanced riskassessment technologies in the P2P lending industry. P2P lending firms often actively embrace advanced information technologies (such as big data analytics) to assess borrower risks and aggressively target these borrowers with a limited credit history (Agarwal et al. 2020) to identify the invisible primes (Di Maggio et al. 2021). They often leverage rich alternative data, such as social media postings (Ge et al. 2017), social relations (Lin et al. 2013), digital footprints on e-commerce platforms (Berg et al. 2020), mobile traces (Lu et al. 2020), and the writing style of loan descriptions (Netzer et al. 2019), to help determine borrower risk. Such alternative data help identify creditworthy borrowers who lack the track records to prove their acceptability to traditional lenders (Jagtiani and Lemieux 2019). Jiang et al. (2021) and Bjo¨rkegren and Grissen (2018) both reported that advanced credit-scoring algorithms could improve risk prediction on borrowers with limited credit records. The closure of P2P lending channels may shut down the option for these tech-savvy lenders to provide invisible primes with credit (Berg et al. 2020), which clamps down the economic development opportunities for these otherwise high-potential borrowers.

In comparison, traditional financial firms are found to be slow in adopting new technologies. For example, a large portion of banks (42% as of 2019)<sup>8</sup> still rely on oldfashioned data-processing systems, such as COBOL based ones. Firms using less advanced technologies are often less capable of assessing borrower risk and so may allocate funds suboptimally.<sup>9</sup> Although some traditional financial firms may have the needed capability to implement similar technologies to cover borrowers with a thin credit history, they may not have incentives to do so because these borrowers may not fall into their targeted market segment (Di Maggio et al. 2021).

The younger generation represents a special group of underserved borrowers who tend to have a short credit history, but are more tech-savvy and, thus, more likely to embrace P2P financing channels (Ichwan and Kasri 2019).<sup>10</sup> Even though this group’s economic status might be temporarily low, they have a high potential to improve their economic position, given a financing chance (Seidman and Kramer 2005). Removing the P2P channel would particularly obstruct the economic development opportunities for this promising group of borrowers. Thus, the younger generation tends to suffer more from the regulation than older borrowers.

P2P lending has the advantage of reaching a larger population due to its use of advanced technology and the embracement of the younger population. Removing this channel may affect such borrowers’ economic development potential. We term this effect on the underserved population the “exclusion effect.”

Overall, because of the entrapment effect, the exacerbation effect, and the exclusion effect, our major working hypothesis postulates that borrowers’ economic development potential will be hurt under the regulation that shut down P2P lending businesses.

## 4. Empirical Analysis

To investigate the effect of the P2P regulation on borrowers, we contrast borrowers who applied for P2P lending loans before the regulation shock (P2P borrowers) against those who never applied for P2P loans during the before-regulation period (non-P2P borrowers).

## 4.1. Data

To study the impact of China’s regulation on borrowers in the credit market, we collaborated with one of the larg est third-party credit-scoring companies in China. The company serves over 3,000 lending firms, covering most leading P2P lending firms, consumer finance firms, microloan firms, and banks. These clients reach 60% of all the end-borrowers in China, with over 30 million creditrating requests per day. The company’s dominant market share makes it one of the best data sources of this kind.

We acquired credit-application records of a random sample of 80,000 applicants who applied for loans from 1,413 firms that requested credit-rating services from the company from 2017 to 2019. Given the leading role of the company in the Chinese market, the data make a good random sample representative of the entire Chinese credit market. The data set contains the timestamp, product type $( \mathrm { e . g . , }$ , credit cards, online cash installments, online consumer loans, offline consumer loans, or offline cash installments), and the financial service firm from which a borrower is applying for credit. We know each applicant’s age group, city, and credit score (as assessed by our partner company). However, we do not observe the loan amount, how the loan is fulfilled in each lending firm,<sup>11</sup> whether the loan is approved, or the interest rate of a specific loan.

Our main analysis focuses on the period from July 2017 to June 2019, which is roughly one year before and one year after the regulation. We leave the rest of the data for the purpose of sample matching, feature construction, and policy simulation in this study. To start, we remove borrowers with missing data on credit scores (our dependent variable) from our raw data, leaving a sample of 71,818 borrowers applying for loans from 1,321 firms. In our data, these firms receive applications at different periods, which may be affected by their business contracts (for credit-assessment businesses) with our partner company. In the second step of data cleaning, we only keep the firms that appear in both the beginning and the end of our data $\mathrm { s e t } ^ { 1 2 }$ (termed “consistent firms”)—that is, firms with a stable contractual relationship with our partner company. This process rules out small firms (mostly under 1,000 applications), leaving 87 relatively large lending firms and 66,776 borrowers in the sample, accounting for 47% of all the applications in our data set. Moreover, borrowers also appear in different periods of the data. In the third step of data cleaning, we focus on the borrowers who appear in both the before- and after-regulation period (called “consistent borrowers”) to conduct a panel data DID analysis. To reduce concerns regarding staggered adoption, we construct the treated group as P2P borrowers who adopted P2P lending before July 2017 and the control group as non-P2P borrowers who never accessed P2P lending before June 2019. This yields an unbalanced borrowermonth panel containing 27,563 borrowers (8,251 P2P borrowers and 19,312 non-P2P borrowers) with 661,512 total observations in our sample.

## 4.2. Measurements

We leverage the individual credit score provided by our partnering company as the primary measure of borrowers’ economic status. The credit score is a commonly used indicator reflecting the effect of economic stratification (Fourcade and Healy 2013) on borrowers ability to afford and repay credit. It largely determines the level of financial services one is eligible to receive (Boyd 2019), and it is highly correlated with one’s income, wealth, and social mobility (Brown and Mazewski 2015). A poor credit score may hinder someone from moving up in society due to a denial of credit, higher financing costs, and a loss of employment opportunities (Thorne 2007).

We also propose a new measure, Bank Ratio, by exploiting borrowers’ choices of credit channels (banks, consumer finance institutes, microloan lenders, P2P lending, etc.) in our data. Bank Ratio assesses the extent to which a borrower pursues bank credit, as compared with credit through other channels:

$$
B a n k R a t i o _ {i, t} = B a n k L o a n s _ {i, t} / N _ {i, t},\tag{1}
$$

where Bank $L o a n s _ { i , t }$ is the number of applications to banks by borrowers i in time $t ; N _ { i , t }$ is all applications made by borrower i in time t. We argue that the pro posed Bank Ratio is a valid measure of individuals’ economic status in our context for the following reasons.

1. Credit applications reflect one’s position in the credit market, which is often stratified based on the social-economic status of the borrower. Credit and debt shaped inequalities through inclusion and exclusion (Dwyer 2018). Being included in bank credit services reflects a borrower’s high social-economic status (Ce´lerier and Matray 2019). For instance, bank borrowers are more likely to be property owners (Dower and Potamites 2014, Field and Torero 2006), and, as a whole, they tend to be wealthier than P2P lending borrowers. In China, it is observed that the poor rely more heavily on informal financing channels, whereas wealthy households with better political connections and financial knowledge are served more by formal finance like bank loans (Cull et al. 2019).

2. Rational borrowers apply for loans that fit their social-economic status due to the costs involved in applications. Loan applications are not free. Applications for formal credit—for example, mortgage loans— often incur significant transaction costs, in addition to the time and effort one has to spend during the process. In China, a typical credit application undergoes rigorous processes such as KYC (know your customer) and AML (antimoney laundry), which involve tedious identity verification<sup>13</sup> (such as ID, facial images, and proof of address), cell phone certification, and providing supporting materials for credit rating (such as bank balance, income, proof of occupation, and credit reports<sup>14</sup> from PBOC). Rational borrowers assess their chance of obtaining a loan when deciding which loan to apply for, rather than randomly trying. Thus, we hold that Bank Ratio reflects rational borrowers’ self-assessment of thei social-economic status. Ceteris paribus, having a higher Bank Ratio would indicate that a borrower has a higher social-economic status.

3. Irrational applications that deviate from the borrower’s needs and economic status may also affect that borrower’s credit rating. Credit-rating companies punish a borrower (in terms of credit score) for making too many unjustified applications—for example, applying for loans that are out of reach (e.g., subprime borrowers applying for low-interest credit) or seeking loans that are way below one’s stratum (e.g., a prime borrower suspiciously seeking a subprime loan).<sup>15</sup> Further, a failed application (i.e., denied loan) will also result in lowered credit score.

For these reasons, we believe Bank Ratio credibly reflects one’s social-economic status. Compared with the Credit Score, which reflects the supply-side (lender) view of borrowers’ creditworthiness, Bank Ratio reflects more of a demand-side perspective with regard to how the borrowers evaluate their own creditworthiness. Consequentially, these two measures paint a complete picture of borrowers from both the supply- and demandside viewpoints.

## 4.3. Summary Statistics

Table 1 reports the descriptive statistics of the panel data by P2P and non-P2P borrowers.<sup>16</sup> The two groups share similarities among demographic covariates (age, gender, rural region ratio, and bank density of their living region). However, there exist some differences in their borrowing activities. P2P borrowers tend to have lower credit scores, borrow more frequently, have lower bank ratios, and access lower-quality credit. Specifically, P2P borrowers have an average Credit Score of 511.961 compared with 667.061 for non-P2P borrowers.<sup>17</sup> On average, each P2P (non-P2P) borrower makes 1.250 (0.516) applications each month, including 0.134 (0.110) applications to banks and 0.081 (0) to P2P loans. The average Bank Ratio is 12.7% for P2P and 23.9% for non-P2P borrowers. Generally, P2P borrowers have relatively lower financial status than non-P2P ones.

We then investigate the borrower distribution over the four channels (bank, microloan, consumer finance, and P2P). We observe that 29% of the 27,563 borrowers use all the channels, 31% use three channels, 21% use two channels, and 19% use one channel. Figure 3 plots the percentage of applications made to different channels by P2P and non-P2P borrowers. As the figure shows, whereas medium-level credit channels (micro loan and consumer finance) generally have more appli cations, bank applications account for about 10% of the applications for P2P borrowers and 20% for non-P2P borrowers. We observe significant trend changes in applications. Before the regulation, P2P borrowers gradually increase their applications to banks. After the regulation, P2P and non-P2P borrowers both experience a downward trend in applications made to banks (which roughly shows a parallel trend between the two groups). This change in the application trend indicates borrowers response to the regulation.

Figure 4 further illustrates the borrower distributions on Credit Score and Bank Ratio across the two groups of borrowers and the two time periods, where credit score distribution is normal, whereas bank ratio distribution is power-law-shaped. In both panels, more P2P borrowers are located on the low-value side, and fewer P2P bor rowers are located on the high-value side, as compared with non-P2P borrowers, showing that P2P borrowers have a relatively lower Credit Score and Bank Ratio. Regarding Credit Score, we notice that non-P2P borrowers tend to have a higher credit score (in the left panel of Figure 4), which witnessed a left shift after regulation. In contrast, P2P borrowers have a lower credit score and slightly shifted to the right after regulation. The Bank Ratio panel exhibits a similar change. After reg ulation, non-P2P borrowers decreased on the right side and increased on the left side, whereas P2P borrowers decreased on the left side and slightly increased on the middle-right side. After presenting this mode-free evidence, we next conduct econometrics analyses to understand how the regulation changed borrowers’ economic status.

Table 1. Descriptive Statistics

<table><tr><td rowspan="2">Variable</td><td colspan="3">P2P borrowers</td><td colspan="3">Non-P2P borrowers</td></tr><tr><td>Obs</td><td>Mean</td><td>Std. Dev.</td><td>Obs</td><td>Mean</td><td>Std. Dev.</td></tr><tr><td># All Applications</td><td>198,024</td><td>1.250</td><td>2.005</td><td>463,488</td><td>0.516</td><td>1.125</td></tr><tr><td># Bank Applications</td><td>198,024</td><td>0.134</td><td>0.467</td><td>463,488</td><td>0.110</td><td>0.426</td></tr><tr><td># Consumer Finance Applications</td><td>198,024</td><td>0.310</td><td>0.757</td><td>463,488</td><td>0.152</td><td>0.510</td></tr><tr><td># Microloan Applications</td><td>198,024</td><td>0.445</td><td>1.001</td><td>463,488</td><td>0.161</td><td>0.543</td></tr><tr><td># P2P Applications</td><td>198,024</td><td>0.081</td><td>0.333</td><td>463,488</td><td>0.000</td><td>0.000</td></tr><tr><td>Credit Score</td><td>198,024</td><td>511.961</td><td>104.435</td><td>459,272</td><td>667.061</td><td>117.997</td></tr><tr><td>Bank Ratio</td><td>95,383</td><td>0.127</td><td>0.287</td><td>130,032</td><td>0.239</td><td>0.397</td></tr><tr><td>Age</td><td>198,024</td><td>31.001</td><td>6.910</td><td>463,488</td><td>30.987</td><td>7.473</td></tr><tr><td>Gender = Male</td><td>198,024</td><td>0.783</td><td>0.412</td><td>463,488</td><td>0.747</td><td>0.435</td></tr><tr><td>Rural Region</td><td>197,904</td><td>0.823</td><td>0.382</td><td>463,224</td><td>0.837</td><td>0.369</td></tr><tr><td>Bank Density</td><td>193,176</td><td>13.576</td><td>11.747</td><td>452,976</td><td>13.878</td><td>11.993</td></tr></table>

Figure 3. (Color online) Applications to Different Credit Channels  
![](/api/attachments/P3QWX4MZ/fulltext/images/ba5b3d35e93da99caeb769f6af131cdbf0f3eea6c07044560dfdbb5edaf54da7.jpg)  
Bank ConsumerFinanceMicroloansP2P Other

(b) Applications to Each Channel by Non-P2P Borrowers  
![](/api/attachments/P3QWX4MZ/fulltext/images/81f4aa482d29cafd3251667208993403978548c5744c70e196ae69a144f9f8d3.jpg)  
BankConsumerFinanceMicroloansP2P Other

## 4.4. Econometric Model

4.4.1. DID with Linear Group-Specific Trend. We employ a DID model to identify how P2P and non-P2P borrowers’ economic statuses change in reaction to the P2P regulation. However, before the policy shock, P2P and non-P2P borrowers’ economic statuses had a different trajectory. The different pretreatment trends across the two groups pose a challenge to conventional DID, which relies on the parallel-trend assumption.

To address this issue, we follow prior literature and directly include a pretreatment trend to account for the potential existence of nonparallel trends across the two groups. Such an identification strategy is widely used in the economics literature when dealing with nonparallel trends in DID design (Wolfers 2006, Jayachandran et al. 2010, Redding et al. 2011, Dimick et al. 2013, Dobkin et al. 2018, Goodman-Bacon 2018). For example, Redding et al. (2011) investigated the change in airport traffic in response to Germany’s division and reunification, factoring in airport-specific linear pretreatment trends. In their DID design, the airports in Berlin are the treated group, and those in Frankfurt belong to the control group. The treatment effect is estimated as the trend differences before and after the shocks of division and reuni fication. Such a method is also commonly employed in medical studies. For example, Jayachandran et al. (2010) controlled a linear pretreatment trend in a DID model by comparing diseases that can and cannot be treated by sulfa drugs to study the effect of sulfa drugs on mortality rate. The treatment effect is estimated by comparing observations before and after 1937, when sulfa drugs became widely available. As another example, Goodman-Bacon (2018) controlled state-specific linear trends to study Medicaid’s impact on mortality trends. As states differ in their levels of cash welfare recipient coverage before the Medicaid program, which expanded after the program, cross-state variation was used as the treatment for identification. In another study examining the economic consequences of hospital admission on adults, Dobkin et al. (2018) allowed for a linear pretreatment trend. Individuals’ hospital admission was taken as the treatment, and those before hospitalization were taken as the control, forming a staggered DID model.

Figure 4. (Color online) Credit Score and Bank Ratio Distributions  
![](/api/attachments/P3QWX4MZ/fulltext/images/aaff80685c3d3888c895f7566363ab487bdd740ef9f5f5cb38e86178e8cd09b1.jpg)

![](/api/attachments/P3QWX4MZ/fulltext/images/80a45776051e0fd8398f8930f53231f23548fe9d98f122a89b7477e01cfb1dae.jpg)  
---. P2P User Before Regulation -----Non-P2P User Before Regulation —P2P User After Regulation Non-P2P User After Regulatior

There are also studies that employ nonlinear pretreatment trends. For example, when investigating the impact of unilateral divorce law on the divorce rate, Wolfers (2006) considered state-level quadratic pretreatment trends, leveraging the different adoption timings of the law across states to estimate the treatment effect. In another study identifying Medicare’s impact on bariatric surgery outcomes, Dimick et al. (2013) examined different linear and nonlinear pretreatment trends to study the impact of coverage change of “Centers of Excellence.” They found no significant difference in the rates of complications and reoperations between Medicare patients and non-Medicare patients before and after the policy.

In this study, we follow the method of Dobkin et al. (2018) to first conduct a nonparametric event study to assess the existence of the pretreatment trend. Then, following Dobkin et al. (2018), Wolfers (2006), and Meer and West (2016), we draw the fitted pretrend to visualize the shape of the pretreatment trend. As elaborated on in Section A of the online appendix, the analysis reveals the existence of a linear pretreatment trend in our sample. Then, we examine cross-group differences before treatment after controlling for this linear trend. As shown in Section A of the online appendix, the two groups do not show significant differences in the pretreatment period after controlling for the linear trend, lending support to the consideration of a linear pretreatment trend for our identification.

In our study, we are interested in the trend, rather than the absolute value of individual economic status. Thus, we follow Jayachandran et al. (2010) and Redding et al. (2011) and estimate a trend change around the regulation on P2P ×t×After , where P2P denotes whether a borrower i is a P2P borrower before the regulation, and $A f t e r _ { t }$ denotes whether the observation at time t is after the regulation shock. Under this framework, our model is:

$$
\begin{array}{r l} Y _ {i, t} = \alpha + \beta_ {0} \times Y _ {i, t - 1} + \beta_ {1} \times P 2 P _ {i} \times t + \beta_ {2} \times P 2 P _ {i} \\ & \times A f t e r _ {t} + \beta_ {3} \times P 2 P _ {i} \times t \times A f t e r _ {t} + \Gamma \times C t r l _ {i, t} + \mu_ {i} \\ & + \tau_ {t} + \varepsilon_ {i, t}, \end{array} \tag {2}
$$

where $Y _ { i , t }$ denotes the dependent variable indicating the economic status of borrower i in month t. $Y _ { i , t - 1 }$ controls for the serial correlation. $P 2 P _ { i } \times t$ captures the different trends of P2P and non-P2P borrowers’ economic status during the pretreatment period. $P 2 P _ { i } { \times } A f t e r _ { t }$ captures the intercept change after the regulation. In the model, our main interest is in the term $P 2 P _ { i } { \times } t { \times } A f t e r _ { t } ,$ which captures the trend change after regulation for P2P versus non-P2P borrowers. For clearer identification, we drop May 2018, the month during which the regulation gradually took effect. $C t r l _ { i , t }$ represents the time-variant control variables, and $\mu _ { i }$ and $\tau _ { t }$ denote the borrowerand time-fixed effects. Note that the main effect of $P 2 { P _ { i } }$ is absorbed by the individual-fixed effect, and the main effect of $A f t e r _ { t }$ is absorbed by time-fixed effects. $\varepsilon _ { i , t }$ denotes the random noise.

We employ multiple time-varying variables as control variables. We control for monthly Consumer Price Index (CPI) (Province\_ $C P I _ { i , t } ) .$ , quarterly GDP (Province ${ _ { G D P } } _ { i , t } ) ,$ 18 and quarterly total retail sales of consumer goods (Province\_ $T R S C G _ { i , t } ) ,$ , all at the province level. These regional-level macroeconomic indicators are direct measures of the economic status aggregated over the region where a borrower resides. We log-transform the count variables and cluster the standard errors at the borrower level.

In this model, one potential source of endogeneity is self-selection of P2P and non-P2P borrowers. We employ the CEM method (Blackwell et al. 2009, Iacus et al. 2012) to mitigate this problem. CEM is a matching method that reduces monotonic imbalance between control and treatment groups. It divides continuous variables into bins and matches treated and control samples to ensure that the distribution of matching covariates is balanced between the matched treated and the matched control groups. Even though the matching method can only address the imbalance in observable variables and cannot account for unobservable variables, it still helps strengthen identification by mitigating self-selection (Kim and King 2014, Greenwood and Wattal 2017).

In our context, we specify P2P and non-P2P borrowers based on P2P channel adoption before the pretreatment period (June 2017). We follow Stuart (2010) and use all available exogenous variables that could potentially affect the treatment assignments before June 2017 to conduct matching. Meanwhile, we avoid using variables having trivial correlations with the dependent variables (DVs). Specifically, we use borrowers’ gender, age, the provincial CPI, GDP per capital, and total retail sales of consumer goods (TRSCG) as matching covariates. For time-varying covariates, we take their values in June 2017 for matching.

The effectiveness of CEM is commonly examined using L1 distance. As exhibited in Table 2, before apply ing CEM, the treatment group and control group were significantly different, with a multivariate L1 distance of 0.148. After matching, we have a sample of 8,233 P2P and 19,117 non-P2P borrowers with L1 distance reduced to 0.048, indicating the effectiveness of matching. In

Table 2. CEM Effectiveness

<table><tr><td>Univariate L1 distance</td><td>Before matching</td><td>After matching</td></tr><tr><td>Gender</td><td>0.037</td><td>0.000</td></tr><tr><td>Age</td><td>0.055</td><td>0.025</td></tr><tr><td>Province CPI</td><td>0.057</td><td>0.000</td></tr><tr><td>Province GDP per capita</td><td>0.053</td><td>0.000</td></tr><tr><td>Province TRSCG</td><td>0.060</td><td>0.000</td></tr><tr><td>Multivariate L1 distance</td><td>0.148</td><td>0.048</td></tr></table>

Table A2 in the online appendix, we also compare the standard differences of the covariates before and after matching. As observed, the covariates of the treatment and control groups are not significantly different after matching. The DID estimation with CEM captures the average treatment effect on the matched treated borrowers conditional on the matching variables.

4.4.2. Honest DID. Another approach we employ to account for the existence of the pretreatment trend is Honest DID, developed by Rambachan and Roth (2023). The Honest DID method is specifically designed to identify the treatment effect when there exists a nonparallel pretreatment trend between the treated and control groups, where the posttreatment trend is assumed to be not too different from the pretreatment trend (Manski and Pepper 2018, Rambachan and Roth 2023). Suppose that our interest is to identify the actual treatment effect $\rho ,$ but this treatment effect is convoluted by the trend difference $\delta$ in outcome between the treated and control groups, and the estimated treatment effect by DID $\beta$ equals $\delta + \rho .$ . Before treatment, $\rho _ { p r e }$ equals zero, as no treatment has occurred; thus, $\delta _ { p r e }$ can be identified as $\beta _ { p r e } .$ Honest DID assumes that $\delta _ { p o s t }$ does not change much from $\delta _ { p r e }$ after the treatment, and it provides an estimation method to identify $\rho _ { p o s t } .$ . To apply this method, the difference between $\delta _ { p o s t }$ and $\delta _ { p r e }$ needs to be specified by the researcher. In our setting, we consider a linear groupspecific time trend to account for confounding trends that may evolve linearly over time. Honest DID provides a relaxed “smoothness restriction” setup to control for smooth differential trend. Specifically, the condition can be formalized below for time t:

$$
\Delta^ {\mathrm{SD}} (\mathbf {M}) = \{\delta : | (\delta_ {t + 1} - \delta_ {t}) - (\delta_ {t} - \delta_ {t - 1}) \leq \mathbf {M} \},
$$

where M bounds the slope of the differential trend and $\mathrm { M } = 0$ equals setting a linear pretreatment trend.

Rambachan and Roth (2023) prove that Honest DID can identify smoothness restriction models using fixedlength confidence intervals (FLCIs) based on affine estimators. The method has been shown to be effective in identifying the true treatment effect when the paralleltrend assumption is violated.

4.4.3. Fixed-Effects Counterfactual Analysis. The applicability of DID relies on several assumptions: the paralleltrend assumption, no anticipatory effect, and no carryover effect. An encompassing model that provides diagnostic tests for these assumptions is the FECT method (Liu et al. 2022). FECT is built upon the synthetic control method (Abadie et al. 2010), which constructs a synthetic counterfactual unit for a treated unit by weighting the untreated units that resemble the treated units. FECT generates latent time-varying factors from the control group in constructing synthetic counterfactuals. In this study, we follow the model-selection procedure recommended by Liu et al.

(2022) and Xu (2017) and specify a model as:

$$
\begin{array}{l} Y _ {i, t} = \alpha + \beta_ {0} \times Y _ {i, t - 1} + \beta_ {1} \times P 2 P _ {i} \times t + \delta_ {i, t} D _ {i, t} + \gamma X _ {i, t} \\ \quad + \mu_ {i} + \tau_ {t} + \lambda_ {i} f _ {t} + \varepsilon_ {i, t}, \end{array} \tag {3}
$$

where time t is time relative to the regulation date. $D _ { i , t } =$ $P 2 P _ { i } { \times } A f t e r _ { t }$ captures the treatment effect, which equals one for a $\mathrm { P 2 P }$ borrower after regulation, and zero otherwise. $X _ { i , t }$ denotes the covariates and control variables that influence the outcome variable. $\mu _ { i }$ and $\tau _ { t }$ are individual and time-fixed effects. $\varepsilon _ { i , t }$ is the random noise. Specifically, $f _ { t }$ captures the vector of latent time-variant unobservable confounders. When the number of latent factors of $f _ { t }$ is given, the model can be estimated with the expectationmaximization algorithm. Similar to our main model, we allow a pretreatment linear trend $P 2 P _ { i } \times t$ in FECT.

The model is first estimated on observations with $D _ { i , t }$ $= ~ 0$ to get the coefficients of $f _ { t }$ and $X _ { i , t } ,$ which then form the predicted counterfactuals $I _ { i , \mathrm { t } } .$ . The choice of the number of latent factors can be made through crossvalidation to reduce prediction errors on a holdout sample. For borrower i at time $t ,$ the differences between the treated observations and the predicted counterfactuals capture the estimated treatment effect $\delta _ { i , t } .$ FECT identifies the average treatment effect on the treated $( A T T )$ where $A T T = \mathsf { \bar { E } } [ \delta _ { i , t } | D _ { i , t } = 1 ]$ . The estimated ATT after s periods of the treatment change is: $A T T _ { s } = E [ \delta _ { i , t } | D _ { i , t - s } =$ $\stackrel { \cdot } { 0 } , D _ { i , t - s + 1 } = D _ { i , t - s + 2 } = \ldots = D _ { i , t } = 1 ] ,$

## 5. Results

## 5.1. Main Results

We report the results in Table 3. First, the model shows a positive coefficient of $P 2 P _ { i } { \times } t ,$ indicating that before regulation, P2P borrowers experienced a faster increase in economic status than non-P2P borrowers. Our main focus is on the interaction of $P 2 P _ { i } { \times } t { \times } A f t e r _ { t , }$ which captures the change of the trend difference across the two groups due to the regulation. Observe that in column (1), this coefficient on Credit Score is $- 2 . 5 3 4 \ ( p < 0 . 0 1 )$ Comparing this coefficient (coef.) with the coefficient of $P \bar { 2 P } _ { i } { \times } t \ \bar { ( } \mathrm { c o e f . } = 3 . 1 7 3 , p < 0 . 0 1 )$ , we conclude that the trend difference between the two groups decreased, if not fully disappeared, after regulation. In other words, the regulation hurt P2P borrowers, who had previously enjoyed relatively faster economic development, more than non-P2P borrowers. A similar finding is observed in Bank Ratio $( - 0 . 0 0 7 , p < 0 . 0 1 )$

Table 3. Economic Status Change in Response to P2P Regulation

<table><tr><td>Variable</td><td>(1) Credit score</td><td>(2) Bank ratio</td></tr><tr><td> $Y_{i,t-1}$ </td><td>0.810***(0.001)</td><td>0.032***(0.005)</td></tr><tr><td> $P2P_i \times t$ </td><td>3.173***(0.06831)</td><td>0.008***(0.002)</td></tr><tr><td> $P2P_i \times t \times After_t$ </td><td>-2.534***(0.07934)</td><td>-0.007***(0.002)</td></tr><tr><td> $P2P_i \times After_t$ </td><td>-6.038***(0.487)</td><td>0.003(0.010)</td></tr><tr><td>Province CPI</td><td>-0.251(0.191)</td><td>-0.003(0.003)</td></tr><tr><td>Province GDP</td><td>0.058(0.195)</td><td>0.004(0.003)</td></tr><tr><td>Province TRSCG</td><td>0.319(0.229)</td><td>-0.006(0.004)</td></tr><tr><td>Constant</td><td>141.375***(19.571)</td><td>0.492(0.328)</td></tr><tr><td>Observations</td><td>623,775</td><td>115,657</td></tr><tr><td> $R^2$ </td><td>0.920</td><td>0.406</td></tr><tr><td>Borrowers</td><td>27,350</td><td>16,787</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.  
Note. Time- and individual-fixed effects are controlled.

The average values of Credit Score (512 and 667) and Bank Ratio (0.127 and 0.239) for P2P and non-P2P borrowers are reported in Table 1. Normalizing the coefficients shown in Table 3 with these average values, we observe a monthly changes of about 0.5% for Credit Score and about 6% for Bank Ratio. In contrast to non-P2P borrowers, P2P lending borrowers exhibited a substantial increase in economic status before the regulation took effect. That is to say, P2P lending helped its borrowers improve their credit scores and credit-channel choices in a way that pointed borrowers to a better social-economic stratum. However, after the regulation, P2P borrowers no longer had any advantage over their non-P2P counterparts.

## 5.2. Robustness Checks

We conduct several analyses to bolster the robustness of our findings. First, one alternative explanation of our results is that the banking system might have simultaneously changed its credit supply in reaction to the P2P regulation. To address this concern, as reported in columns (1) and (2) in Table B1 of the online appendix, we control for the quarterly domestic RMB loan amount issued in each province (Province\_RMB\_loans<sub>i,t</sub>).<sup>19</sup> This measure is commonly used to capture the total credit supply to the real economy in a province. Our results remain consistent after controlling for this variable. In addition, the availability of credit supply may be reflected in the number of applications. We therefore include the number of applications as an additional control variable. As shown in columns (3) and (4) in Table B1 of the online appendix, the results remain consistent with our main model.

Second, when preprocessing our data, we focused on the set of consistent firms and excluded firms that might have stopped their business contracts with our datasource company for reasons unknown to us. As a robustness check, we now include all the firms in our analysis. As detailed in columns (5) and (6) in Table B1 of the online appendix, our main findings remain consistent. Similarly, our main model focuses on the set of consistent borrowers, who are present at least once in the preregulation period and at least once in the postregulation period. We conduct two robustness checks on this.

First, we repeat our analysis on all borrowers. Columns (7) and (8) in Table B1 of the online appendix yield consistent results. Then, we restrict consistent borrowers to be those who appear in at least three months of data before and after regulation. The results, detailed in columns (9) and (10) in Table B1 of the online appendix, are consistent with our main model. Because some of these tests involve changing the number of observations, we carry out CEM as detailed in Table B2 of the online appendix to ensure that the samples are matched.

Third, we consider an additional dependent variable, Credit Quality, by inspecting the specific type of credit products a firm offers, including online cash loans, online/offline consumption installment loans, online/offline installment loans, credit cards, and auto finance. Auto finance, credit cards, and offline install ment loans are considered low-cost credit with lower interest rates and longer maturity, whereas the other products are high-cost, according to the credit-product classification in China. Credit Quality assesses the average level of the high- or low-cost loans a borrower has applied for during a time period:

$$
C r e d i t Q u a l i t y _ {i, t} = \Sigma_ {j} C r e d i t C o s t _ {i, j, t} / N _ {i, t},\tag{4}
$$

where $N _ { i , t }$ is the number of applications of borrower i in time $t ,$ and $C r e d i t C o s t _ { i , j , t }$ is the cost level (one for lowcost, zero for high-cost) of each loan j applied for by i during time t. To address the concern that the result may be driven by our method of weighing high-/low-cost credit, we also experiment with a different weighting scheme by assigning �1 to high-cost and 1 to low-cost (and also assigning one to low-cost and zero to high cost). Table B3 of the online appendix reports the results, which are consistent with the main model.

Fourth, in our main model, we include a lagged dependent variable to control for serial correlation. We present the results of an analysis without this control variable in Online Appendix Table B4, and this approach yields results that are qualitatively consistent with our main model, though the magnitude of the coefficients differs slightly. This analysis further confirms the robustness of our findings.

## 5.3. Additional Models: Honest DID and FECT

When implementing Honest DID, we adopt the smoothness-restrictions approach to account for the linear pretreatment trend of borrowers’ economic development. The results from this analysis are reported in Figure 5, and they are consistent with our main model.

In Figure 5, the dark line represents the monthly difference of the two groups without considering the treatment effect, which is estimated from a two-way FE model. The gray line is the partially estimated treatment effect identified by Rambachan and Roth’s (2023) Honest DID method. The dotted lines indicate the 95% confidence intervals. The gray lines are located lower than the x-axis, meaning that the regulation significantly reduced the economic status (i.e., Credit Score, Bank Ratio) of the P2P borrowers. The average ATT bounds estimated over all the periods after regulation are also significantly below zero (upper bound of ATT on Credit Score � �18.260, upper bound of ATT on Bank Ratio � �0.009). Overall, the Honest DID results reconfirm our main model results.

Figure 5. (Color online) Honest DID Results  
![](/api/attachments/P3QWX4MZ/fulltext/images/5684e24942e600b0acd200972cd90ebb077987a93bcff0abc292a928af038221.jpg)

We then implement the FECT model with the same control variables and borrower- and time-fixed effects as used in the main model, and this model is elaborated on in Section C of the Online Appendix. Table 4 reports the estimated average ATT of the regulation over the afterregulation periods, which are all significant and negative. After regulation, the P2P borrowers experienced a reduction in economic development of 23.716 for Credit Score and 0.037 for Bank Ratio. Figure 6 depicts the monthly treatment effects. As shown in the figure, the Credit Score of P2P borrowers went down after the regulation. Similarly, Bank Ratio went down for about seven months after regulation. It should be noted that the ATT in Table 4 is the overall effect aggregated over 13 months during the after-treatment period (Jun 2018 through Jun 2019). For example, in Figure 6(a), the decreasing trend goes to about �40, leading to a mean of about �20 as the ATT in Table 4. Correspondingly, the main model results in Table 3 are estimates of a monthly trend change, which implies a 13-month change of �2.534 × 13 � �32.942 on Credit Score, which is aligned with the values in Figure 6. The results further validate the findings of our main model that P2P borrowers’ economic development was slowed down after regulation, as compared with non-P2P borrowers.

![](/api/attachments/P3QWX4MZ/fulltext/images/319942b138a1068d93d785231a2206c3afd5a7ca32c4f5169a210c65a62595b1.jpg)

The validity of the FECT estimation relies on several assumptions (Liu et al. 2022): a correctly specified functional form; a strict exogeneity; and a feasibility assumption that the impact of hidden or unobserved confounders can be decomposed at a low dimension specified as $\lambda _ { i } f _ { t }$ in Equation (2). In our study, the government regulation is exogenous from the borrower and lending firms choices. Following Liu et al. (2022), we conduct the placebo test to examine whether the treatment-effect estimation changes when we assume earlier treatments (a violation of the placebo test implies a violation of any of the three assumptions). We also conduct the equivalence test on the differential pretrend. Online Appendix C reports all the FECT test results. Note that in our setting, we code treatment as one on all periods after regulation. This setup does not require the carryover test, as pointed out by Liu et al. (2022). For both Credit Score and Bank Ratio, the placebo test and the equivalence test pass and support the identification assumptions.

## 5.4. Heterogeneous Effects

The above analyses show that the upward trend in P2P borrowers’ economic status as compared with non-P2P borrowers slowed down after the regulation. To further uncover the mechanisms at play, we examine how and why the regulation impacts different types of borrowers differently.

Table 4. Economic Status Change Estimated by FECT

<table><tr><td>DV</td><td>ATT</td><td>Std. Dev.</td><td>p-value</td><td># Obs.</td><td>95% lower bound</td><td>95% upper bound</td></tr><tr><td>Credit Score</td><td>-23.716</td><td>1.070</td><td>0.000</td><td>628,609</td><td>-25.378</td><td>-21.332</td></tr><tr><td>Bank Ratio</td><td>-0.037</td><td>0.018</td><td>0.041</td><td>117,347</td><td>-0.073</td><td>-0.002</td></tr></table>

Figure 6. (Color online) Monthly ATT Estimated by FECT  
![](/api/attachments/P3QWX4MZ/fulltext/images/a2abb79c4cf592fae1b85312971b7e7955baab0fa1a615f8b4ee6346c8a15923.jpg)

5.4.1. Entrapment of Low-End Borrowers Within High-Cost Credit. Our discussions in Section 3.2.1 posit that borrowers in the P2P channel could be trapped in highcost credit and unable to escape. To verify this conjecture, we conduct a panel vector autoregression (PVAR) analysis to estimate the channel-transition heterogeneity of borrower i at time t:

$$
\mathbf {Y} _ {i, t} = \alpha + \Lambda \times \mathbf {Y} _ {i, t - 1} + \Gamma \times C t r l _ {i, t} + \mu_ {i} + \tau_ {t} + \sigma_ {i, t},\tag{5}
$$

where $Y _ { i , t } = [ B a n k ~ A p p l i c a t i o n s _ { i , t }$ CF Applications ML Applications P2P Applications ]<sup>T</sup> denotes the vector of the number of applications made to each channel at time t. In the model, we consider the same control variables specified in the main model. The model essentially estimates the serial path dependence of borrowers’ choices of credit channels, as reflected in their loan applications.

The results of the model are summarized in Table 5 (the full table is reported in the online appendix as Table D1), where we report the before- and after-regulation transition coefficients across four main channels (Bank, CF, ML, and P2P). Following Clogg et al. (1995) and Paternoster et al. (1998), we employ a z-test on the differences between the coefficients of the two periods and highlight the channel transitions that significantly increased after regulation. The results show that the market becomes more bipolarized after regulation: The high-end borrowers tend to stay within low-cost credit channels, whereas, alarmingly, the low-end borrowers tend to get stuck in high-cost credit channels.

![](/api/attachments/P3QWX4MZ/fulltext/images/1459c999c61f9e3a19526782738faeab9ee13271cae50a796b1027837caba3b3.jpg)

We further illustrate these effects in Figure 7. We observe significant negative changes for cross-channel transitions between low-cost credit and high-cost credit. Transitions from bank borrowers and consumer finance borrowers to microloan borrowers also decrease. Transitions between consumer finance borrowers and P2P borrowers decrease. Overall, regulation increased the barrier for low-end customers to access low-cost credit. Moreover, we observe that the path dependency related to the P2P channel increases from 0.174 to 0.248 (p < 0.01), suggesting that P2P borrowers are more inclined to stay within P2P lending after regulation. This finding corroborates our argument that low-end borrowers tend to be trapped within high-cost credit.

5.4.2. Exacerbation of the Underprivileged. We argue that the regulation’s negative impact could exacerbate the underprivileged people with regard to credit access and social mobility. For many of these individuals, P2P lending may be the only viable financing source (Funga´cˇova ´ and Weill 2015, Zins and Weill 2016), so removing this channel puts them in a disadvantaged position. In this study, we proxy underprivileged borrowers by using the social-economic characteristics of their living regions.

Table 5. Channel Transition Heterogeneity in PVAR

<table><tr><td rowspan="3">Variable</td><td colspan="4">Before regulation</td><td colspan="4">After regulation</td></tr><tr><td colspan="4">Low-cost → High-cost</td><td colspan="4">Low-cost → High-cost</td></tr><tr><td> $Bank_t$ </td><td> $CF_t$ </td><td> $ML_t$ </td><td> $P2P_t$ </td><td> $Bank_t$ </td><td> $CF_t$ </td><td> $ML_t$ </td><td> $P2P_t$ </td></tr><tr><td> $Bank_{t-1}$ </td><td>0.097</td><td>0.024</td><td>0.021</td><td>0.004</td><td>0.108</td><td>0.021</td><td>-0.054***</td><td>0.000</td></tr><tr><td> $CF_{t-1}$ </td><td>0.023</td><td>0.119</td><td>0.056</td><td>0.014</td><td>0.030</td><td>0.093</td><td>0.018*</td><td>-0.002***</td></tr><tr><td> $ML_{t-1}$ </td><td>0.027</td><td>0.082</td><td>0.237</td><td>0.026</td><td>0.036</td><td>0.062</td><td>0.209</td><td>0.015</td></tr><tr><td> $P2P_{t-1}$ </td><td>0.035</td><td>0.131</td><td>0.143</td><td>0.174</td><td>0.020</td><td>0.027***</td><td>0.164</td><td>0.248***</td></tr></table>

$^ { * } p < 0 . 1 ; ^ { * * } p < 0 . 0 5 ; ^ { * * * } p < 0 . 0 1$ (indicating whether the coefficients of the two periods are different).

Figure 7. (Color online) Channel Transition Heterogeneity Change After Regulation  
![](/api/attachments/P3QWX4MZ/fulltext/images/649235ef38b3655bdbd9d7794cff869806c60e0c34238648bf2a49bd947110b9.jpg)

First, we use the GDP per capita of a city as a proxy because a higher GDP per capita indicates better infrastructure, more job openings, better access to big markets, etc., which would alleviate individuals’ chances of losing their economic status. The left panel of Figure 8 illustrates the coefficients of $P 2 P _ { i } \times t \times A f t e r _ { t }$ across regions with different GDP per capita. We split the cities into five categories with a 5K U.S. dollar (USD) bin size, according to their GDP per capita. As expected, we see that borrowers in cities with a lower GDP per capita (less than 10,000 USD, the average in China in 2018) had a larger trend reduction in Credit Score compared with highly developed regions. This shows that the P2P channel is more important for borrowers in regions with a low GDP per capita. The results on Bank Ratio are largely consistent, as detailed in Online Appendix Table D2.

Second, we examine whether living in rural or urban areas makes a difference. Rural and urban areas often differ in terms of economic development opportunities and financial support available to citizens (World Bank 2018). For rural residents, the expected income is lower, and the support from formal financial systems is weaker than in urban areas. Therefore, these people are more likely to rely on P2P lending to improve their financial status and will subsequently experience a larger trend reduction. The differential results on urban versus rural residents are depicted in the middle panel of Figure 8 and detailed in Online Appendix Table D3. After P2P regulation, rural borrowers experienced more losses than urban ones.

Third, we use the number of bank branches per square kilometer to proxy the development status of the borrower’s region: Regions with more business activity tend to have more bank facilities.<sup>20</sup> This measure has also been used as a proxy of the search cost to access credit (Argyle et al. 2020), which would moderate a borrower’s ability to look for alternative low-cost credit (Herkenhoff 2019). Even though banks can provide their own online channels, in regions with few local branches, there are still hurdles for borrowers to access formal credit (Argyle et al. 2020). In our study, we split the bank density into five percentiles. As illustrated in the right panel of Figure 8 and detailed in Online Appendix Table D4, P2P borrowers’ credit scores experienced a bigger change if they live in areas with a lower bank density. In other words, this implies that for borrowers residing in regions with more bank branches, the removal of the P2P channel upon regulation was less impactful.

Altogether, our findings indicate that underprivileged borrowers in less developed regions, in rural areas, and in regions with fewer financial facilities tend to experience stronger negative impacts from P2P regulation.

5.4.3. Exclusion of the Underserved. Another reason we posit that the P2P regulation is impactful is because P2P lending firms are able to leverage IT (such as big data analytics) to identify invisible primes. Note that borrowers with more bank applications tend to provide more complete data in their application files for the lender to assess risk. Conversely, people with fewer bank applications are more likely to have incomplete data, and this is when technologies like big data analytics can help identify these invisible primes (Di Maggio et al. 2021). Many P2P lending firms were early adopters of such technologies to assess the risk of borrowers (Ge et al. 2021). P2P regulation inadvertently crowded out such tech-savvy lenders, so it may have a stronger impact on those borrowers who have high potential but less complete data.

Figure 8. (Color online) Region Heterogeneity: Change in Credit Score Trend upon Regulation  
![](/api/attachments/P3QWX4MZ/fulltext/images/4bebad312bbd709d7412b2d11251beb3c9526b52d9c1d87e0f60a72a3df2e4f3.jpg)

Figure 9. (Color online) Heterogeneity in Bank Experience  
![](/api/attachments/P3QWX4MZ/fulltext/images/b5a890d03ca9d6dd3d172c84f539384e9567b4865934cc0db10d74b1face6604.jpg)

To test this mechanism, we use bank experience (Bank Exp)—that is, the number of bank applications before the preregulation period (up to July 2017)—as a proxy for the bank data richness of borrowers. Figure 9 illustrates the effects on borrowers with different Bank Exp (detailed in Online Appendix Table D5). It shows that when bank experience increases, the regulation effect tends to decrease. Less experienced borrowers who have limited records with banks, who used to benefit more from P2P lending, tend to suffer more from the regulation.

Lastly, we conjecture that borrowers’ age also affects their reliance on the P2P channel. We examine age by grouping it into five-year bins starting from 18 (the minimum age required to access credit in China). As delineated in Figure 10 (details reported in Appendix Table D6), the effect of regulation on Credit Score is most salient among young borrowers between 18 and 22. Even though the young generation’s economic status is relatively lower, making them more reliant on the P2P lending channel, they would have high potential to improve their economic status when given a chance to receive credit (Seidman and Kramer 2005). As we would expect, the negative impact of regulation is stronger for the younger generation.

## 6. The Promise of PolicyTech

China’s P2P regulation had several intended goals, including controlling financial risk (e.g., loan defaults) and curbing P2P lending platforms’ illegal activities (e.g., forming pooled funds). From these perspectives, the onesize-fits-all policy of clamping down on P2P lending busi nesses is a straightforward decision, if not an optimal one. However, our analysis reveals that borrowers can be on the receiving end of collateral damage as their economic status deteriorates. So, is it possible to achieve both objectives—improving borrowers’ economic status and controlling financial risk—simultaneously by implementing a more personalized regulation?

We explore this possibility through a borrower-level regulation based on AI predictions, which we call Policy-Tech. A common practice in the lending market is to profile borrowers based on their risk levels and provide differentiated credit services (interest rate, loan amount, etc.). With the ubiquitous use of AI in the lending industry, this process can be automated, which makes it possible to evaluate an individual’s financial risk and accordingly determine their eligibility for a particular financing channel. That is, it is possible to stipulate and enforce different regulatory policies for different types of individuals, as opposed to a one-size-fits-all policy that affects all individuals indiscriminately.

Figure 10. (Color online) Heterogeneity Across Age Groups  
![](/api/attachments/P3QWX4MZ/fulltext/images/8ba2ccccdab9cacc843c20a64d0e92750cc5f8ec2b1b15aed443120590e95774.jpg)

![](/api/attachments/P3QWX4MZ/fulltext/images/cefac06847edf689488aea3ddd4c50fa08310587ba5008926aca0d0b29e9c3a8.jpg)

Figure 11 illustrates the process behind our PolicyTech. First, we build a classifier to predict the financial risk (i.e., loan default) of a borrower. Then, we separate the borrowers into two groups based on the classifier’s prediction as to whether the borrower should be “regulated” or “not regulated,” where regulated means the borrower should be prohibited from accessing P2P lending. In this approach, the economic status of regulated borrowers would change across the two time periods, just like what has happened in reality. For the not-regulated borrowers who continue to have access to P2P lending, we assume their economic status in the after-regulation period remains the same as in the before-regulation period. As we simulate regulating different portions of borrowers, we can observe the economic status changes in the population, which reflects what may have happened in a real-world counterfactual scenario.

## 6.1. Borrower Risk Prediction

In this study, we predict the financial risk at the borrower level. We select this unit of analysis because PolicyTech’s goal is to provide personalized regulation. In fact, the borrower default information—that is, whether and when a borrower had a default—is available to us only at the borrower level. Because of data privacy constraints, we unfortunately do not know on which individual loans the borrowers defaulted. Nevertheless, the borrower-level analysis is adequate for our setting because our interest is in the impact of the policy on borrowers. Moreover, borrower-level default better captures the economic status of a borrower than loan-level default because a borrower may partially repay some loans, while discretionarily defaulting on others. Further, a borrower-level intervention is more feasible than a loan-level intervention. Thus, we investigate the risk at the borrower level.

The prediction task is carried out in the beforeregulation period, aligning with our empirical analyses. Specifically, we calibrate the training model on the features constructed using the data between January 2017 and November 2017, and we predict borrowers’ default on the six-month period from November 2017 to April 2018 (i.e., the six months right before the regulation). This design mimics the real setting, where we make a regulation design before April 2018, impose the regulation in May 2018, and observe borrowers’ behaviors afterward. We are thus able to conduct counterfactual analysis and answer what-if questions, such as: How would the economic statuses of borrowers have changed if certain interventions had been taken based on Policy-Tech’s suggestions?

As an instantiation of risk-prediction models, we build a classifier using the XGBoost algorithm (eXtreme Gradient Boosting) to identify “bad borrowers”—that is, those who have been marked as “rejected,” “fraud,” “delinquent,” or “lost contact (after delinquency)” or were listed as “dishonest persons” by courts before the regulation. XGBoost is an improved GBDT (gradient boosting decision tree) algorithm that aggregates many weak classifiers in order to create a stronger classifier (Chen and Guestrin 2016). It is widely used by data scientists, and, unlike black-box methods such as deep learning, its high interpretability makes it one of the most popular methods for risk assessment in the lending industry.<sup>21</sup> As shown in Online Appendix Table E1, our features fall into four categories: Demographics, Financial Status, Applications, and Default & Lawsuit. We generate 2,303 features based on these variables by (1) converting all categorical variables (e.g., city) to dummy variables; (2) calculating log-transformed, squared variables as additional features for all numerical variables (e.g., city population, all variables concerning Applications); and (3) calculating minimum, maximum, standard deviation, and sum as additional features for all variables that recur monthly (e.g., variables concerning Applications). After the feature selection, we have 2,291 features to feed into the algorithm.

Figure 11. (Color online) Illustration of the Experiment Process  
![](/api/attachments/P3QWX4MZ/fulltext/images/4923dbb1680d273b8de8a8bd77fc25f9b1d395dd0a45ff19e9cd7ae2c489a9a7.jpg)

Our testbed contains 4,124 (6.2%) bad borrowers and 62,453 “good borrowers.” As illustrated in Figure 11, we randomly split our data into 80% for building prediction models and 20% for simulation (53,261 versus 13,316 borrowers, 3,316 versus 808 tagged as bad borrower in each set, respectively). We conduct a fivefold crossvalidation on the 80% model-building data for parameter tuning and algorithm assessment.

Table 6 reports the classification performance and receiver operating characteristic (ROC) curve of different algorithms. The XGBoost algorithm predicts the bad borrowers with high accuracy, achieving an F1 score of 0.863 and an AUC (area under the curve) of 0.942, which is the best among all the models. The AUC is statistically better than all the other algorithms at a 95% confidence interval. In fact, XGBoost generally outperforms the other models in comprehensive metrics (F1, accuracy, and AUC). Its excellent performance is another reason we adopt XGBoost as the prediction algorithm in the policy simulation.

## 6.2. Regulation Effect Simulation

Next, we use all the model-building data to build a classifier and predict the financial risk of the 13,316 borrowers in the simulation data set. To simulate “personalized” regulation, we sort all the borrowers according to the algorithm’s predictions and hypothetically prevent a certain number of high-risk borrowers from accessing the P2P channel (to mimic the P2P regulation). We gauge the effect of the regulation by examining the change in borrowers’ economic status during the six months right after the regulation. For brevity, in Figure 12, we only visualize the performance of PolicyTech with respect to Credit Score. The results pertaining to Bank Ratio are qualitatively similar and are delegated to Online Appendix Figure E1.

In Figure 12, the x-axis represents a certain number of borrowers being removed from accessing the P2P channel under PolicyTech (the dashed line indicates the percent of bad borrowers removed). The solid line visualizes the corresponding change in borrowers’ Credit Scores. As the figure reveals, PolicyTech’s effectiveness can be broken into three regions, as depicted by the solid line. When restricting fewer than 2,700 borrowers, the line generally exhibits an increasing trend, indicating an improvement in the population’s economic status. In this region, Policy-Tech is able to achieve both of its goals, economic development and risk control, at the same time. After that, restricting more borrowers would entail a reduction in borrowers’ economic status, as the line starts decreasing. This is where a policymaker would need to decide how to best trade off risk against economic status. Nevertheless, the line is still higher than the starting point (i.e., not regulating any people) before restricting about 7,500 borrowers. In this middle region, the market is still better off, achieving better risk control and economic status than an unregulated market. From this point on, as more borrowers are restricted from accessing P2P lending, the policy will benefit risk control, but lead to worse economic status for borrowers.

As a comparison, the P2P regulation was applied to the entire lending market and was able to crowd out some bad borrowers from the market by limiting the P2P credit supply. In Figure 12, the x-axis also shows the number of borrowers crowded out by the actual regulation. For our analysis, we regard a borrower as being crowded out of the P2P channel if there was no P2P application (by the same borrower) observed within the last six months of our sample. The double line indicates the crowding out of bad borrowers under the current P2P regulation. The dotted line indicates the borrowers average credit score under the P2P regulation. As shown in Figure 12, it took the extant regulation a year to crowd out 2,329 borrowers, which is about 20% of the entire market. By restricting 20% of borrowers, the P2P regulation only removed 21% of bad borrowers, which is not much better than a random removal and much worse than the 84% rate achieved by our algorithm. However, in this manner of crowding out of bad borrowers, the P2P regulation inadvertently caused a sharp reversal of social-economic upward momentum. Specifically, the Credit Score drops from 648 to less than 600.

The above analysis demonstrates that PolicyTech for personalized regulation is a promising tool to help policymakers maintain people’s economic status, while reducing the lending market’s financial risk. In comparison, the extant regulation unnecessarily crowds out too many promising borrowers and turns their upward trajectory into a downward trend. We argue that from the perspective of improving individuals’ economic status, PolicyTech holds an advantage over a one-size-fits-all policy.

Table 6. (Color online) Performance Comparison of Algorithms

<table><tr><td colspan="6">Receiver Operating Characteristic</td><td></td></tr><tr><td rowspan="7"></td><td>Model</td><td>Precision</td><td>Recall</td><td>F1</td><td>Accuracy</td><td>AUC</td></tr><tr><td>XGBoost</td><td>0.979</td><td>0.796</td><td>0.863</td><td>0.974</td><td>0.942</td></tr><tr><td>Random Forest</td><td>0.986</td><td>0.784</td><td>0.855</td><td>0.973</td><td>0.925</td></tr><tr><td>Decision Tree</td><td>0.985</td><td>0.791</td><td>0.861</td><td>0.974</td><td>0.890</td></tr><tr><td>Linear Discriminant Analysis</td><td>0.878</td><td>0.718</td><td>0.696</td><td>0.799</td><td>0.887</td></tr><tr><td>MLP</td><td>0.858</td><td>0.808</td><td>0.831</td><td>0.963</td><td>0.842</td></tr><tr><td>GaussianNB</td><td>0.903</td><td>0.802</td><td>0.844</td><td>0.968</td><td>0.802</td></tr></table>

Note. Bold cells are not significantly different from the highest value at a 95% confidence interval.

Figure 12. (Color online) PolicyTech vs. the Current P2P Regulation Policy in Removing Bad Borrowers  
![](/api/attachments/P3QWX4MZ/fulltext/images/4c473e954a17fa3defc7705ad7a97b688519c5aa17d82d70b86c9aaf73b5fb6e.jpg)

As a side note, we are aware that there may be concern over whether personalized regulation is fair. Although it is debatable, we find ample support for it in the law literature (Misostishkhov 2020). For example, Verstein (2019) reviewed the related literature, concluding that personalized law should be embraced when feasible. Busch (2019) discussed the positive implications and operations of personalized law in the context of digital markets. In this study, we focus on the technical aspect of PolicyTech and demonstrate the feasibility and potential benefit of having a personalized regulation, leaving the debate over fairness to law researchers.

The algorithm used in this study is a state-of-the-art algorithm and follows the regulation of model transparency in the finance industry. Although some of the features (such as the number of applications to different companies) we leverage are unique to our partner company, most features are available to all financial firms. The way we generate features is also generic to different business tasks, such as credit rating and targeted marketing. Thus, the proposed machine-learning approach has high generalizability to different countries or different firms. With that being said, we do not claim the specific model and features to be one of this study’s major innovations. The novelty of this study mainly stems from the proposed

PolicyTech framework that connects machine learning with personalized regulation and the extensive empiri cal demonstration of how it outperforms the extant one-size-fits-all policy in our context.

## 7. Conclusions and Implications

Maintaining and fostering the economic status of individuals is crucial for a society. We show how P2P borrowers’ economic development was slowed down by China’s 2018 regulatory policy that tightened up credit supply in the P2P lending market. Alarmingly, we find that the policy’s negative impact is severer among underprivileged borrowers (e.g., those living in less developed regions) and underserved borrowers (e.g., those who are younger or have less bank experience). In response to the challenge of tackling financial risk and maintaining borrowers’ economic status, we propose a solution called PolicyTech that uses AI to personalize the regulation. We show that personalized regulation could achieve both goals by eliminating a portion of risky borrowers from the lending market.

Our results have several interesting policy implications. First, they suggest that a simple suppressive policy that indiscriminately shuts down financial opportunities may create a dilemma. Although controlling financial risks (such as the risks of the P2P lending market) is important, it may come at the expense of the economic development potential of individual borrowers. Borrowers who lose the chance to improve their economic status may resort to crime, as revealed in our separate empirical investigation.<sup>22</sup> Such societal cost needs to be taken into account when policymakers develop financial regulations.

Second, we find that there is a heterogeneous effect of the regulation on borrowers. The regulation exacerbates underprivileged borrowers and excludes underserved borrowers. Borrowers in less developed regions, in rural areas, and in regions with fewer financial facilities (e.g., bank branches) suffered more damage in terms of losing their economic development potential after the regulation. The young generation, who tend to embrace P2P lending, and the invisible primes, who have less experience with traditional financial channels, are also hurt by the regulation. It would be necessary to factor in such heterogeneities when stipulating regulatory policies.

Third, we observe that low-end borrowers have limited choices and are not able to ascend to low-cost credit channels after regulation. In other words, they are more likely to be trapped within high-cost credit channels. To protect the underprivileged, alternative financial instruments (such as government-backed low-cost credit) should be provided when removing a credit channel.

Fourth, we show that it is possible to develop AI-based solutions—that is, PolicyTech—to personalize a policy. Such ambidextrous policies help protect borrowers’ economic development status, while regulating risk within the lending market. With the rapid deployment of AI across industries and countries in recent years, we believe the PolicyTech approach would be increasingly amenable and applicable to different contexts.

The finding regarding P2P regulation’s impact on low-end borrowers’ economic development is critical for policymakers and society because it affects social mobility. Social mobility<sup>23</sup> refers to the movement of individuals, families, households, or other categories of people within or between social strata in a society. Providing adequate social mobility, which enables individuals to move from a lower class to an upper class with better income, living standard, social status, etc., is critical to the health of a society. Without ample channels for improving social mobility, a social system may experience significant sociological and political instability (Bai and Jia 2016). In a context of good social mobility, the economic status of borrowers increases over time, which helps improve their position within their country’s social strata. Government funds, such as those from the U.S. Small Business Development Centers, and private funds, such as the Bill & Melinda Gates Foundation’s Economic Mobility and Opportunity program, serve this purpose. Studies have found that bank access improves people’s economic status (Chopra and Tantri 2017, Ce´lerier and Matray 2019). In addition, low-cost credit, such as credit cards, improves people’s living standards (Azevedo et al. 2021). Our findings indicate that highcost credit may help boost social mobility by improving borrowers’ economic status.

Our study is not without limitations. First, it focuses on short-term economic status, as reflected in individuals’ credit scores and loan applications. In future research, it would be interesting to investigate the effect of the regulation on intergenerational social-economic changes. Second, this study only considers the tradeoff between financial risk and borrowers’ economic status, whereas economic policies may need to weigh tradeoffs among many factors. In their examination of policies, future studies can factor in other effects such as economic crime rate. Third, our research context is China’s, where an abrupt policy change on P2P lending occurred as a shock to all. It remains to be seen how lending policies in other countries impact borrowers’ economic sta tus and how to best design such policies.

## Acknowledgments

The authors thank the senior editor, associate editor, and reviewers for their invaluable comments and suggestions. The authors also thank the anonymized company that allowed us to access the data for this study.

## Endnotes

<sup>1</sup> Source: 2019 China Consumer Finance Development Report (https://www.199it.com/archives/942415.html, p. 5; accessed Novem ber 19, 2020).

<sup>2</sup> According to the five-tier loan classification of People’s Bank of China (https://ccb.com/cn/ccbtoday/news/536114976100.html; accessed November 19, 2020), loans overdue for more than 90 days are nonperforming loans. The NPL ratio of commercial banks in China is typically less than 1% (https://www.ceicdata.com/zh-hans/china/non-performingloan-npl/cn-npl-ratio-com-bank-consumer-loan; accessed November 19, 2020).

<sup>3</sup> The average NPL rates of consumer finance firms were 2.74% and 2.63% in 2018 and 2019 (https://www.sohu.com/a/414731034\_ 118392; accessed November 19, 2020).

<sup>4</sup> The leading online microloan lending firms maintain an NPL ratio of about 5% (https://www.jinronghu.com/news/21282.html; accessed November 19, 2020).

<sup>5</sup> See https://www.rf.hk/news/jinrong/40018.html; accessed November 19, 2020.

<sup>6</sup> For example, the China Banking Regulatory Commission required P2P lending companies to be registered with regulatory authorities by June 2018, which was later documented in the operations standard of the National Internet Finance Association of China.

<sup>7</sup> Policy announcement (https://www.scio.gov.cn/xwfbh/xwbfbh/ wqfbh/39595/39902/xgzc39908/Document/1647673/1647673.htm; accessed November 19, 2020).

<sup>8</sup> Amazingly, 43% of U.S. banks are still using COBOL as of 2019 (https://www.ey.com/en\_us/banking-capital-markets/why-bankscan-t-delay-upgrading-core-legacy-banking-platforms) accessed December 19, 2020).

<sup>9</sup> See https://globalnews.ca/news/5664335/big-banks-big-tech-internetgiants-fiancial-system/ (accessed 19/12/2020)

<sup>10</sup> See https://www.bondora.com/blog/5-reasons-why-young-peopleare-investing-in-peer-to-peer-lending/ (accessed October 21, 2022).

<sup>11</sup> For example, if the lending firm is a P2P platform, we do not know how it matches lenders with borrowers to enable transactions or whether the loan is from a pooled fund.

<sup>12</sup> Focusing on the population of consistent firms helps alleviate the firm-level selection due to their contracts with our partner company (unobservable to us). In the robustness check, we examine the sensitivity of our analyses to this step of data processing using the entire sample with all the lending firms. The results are consistent.

<sup>13</sup> Materials required to apply for bank credit in China are specified in https://zhuanlan.zhihu.com/p/44920851; http://www.360doc. com/content/19/0504/17/62154959\_833315118.shtml; and https:// www.boc.cn/bcservice/bc3/bc31/201106/t20110607\_1414165.html (accessed August 2, 2021).

<sup>14</sup> Regulatory authorities require P2P platforms to ask for individuals’ PBOC credit reports in loan applications (https://baijiahao. baidu.com/s?id=1581835332780921746&wfr=spider&for=pc; accessed 02/08/2021).

<sup>15</sup> In a credit bureau’s risk-assessment models, seeking high-cost credit is typically considered to be a negative signal (e.g., https:// zhuanlan.zhihu.com/p/109649516; accessed August 2, 2021).

<sup>16</sup> Note that Bank Ratio (and Credit Quality used in the online appendix) can only be calculated with at least one application in that month. Thus, the number of observations in Table 1 for Bank Ratio becomes smaller. In addition, in our data, a small number of appli cations’ loan types are unspecified, leading to a small difference in the number of observations for the measure.

<sup>17</sup> A score of 650–750 is typically required for bank loan borrowers.

<sup>18</sup> The quarterly measures are converted to monthly by being divided by three when being applied in regressions.

<sup>19</sup> Domestic RMB loans constitute the largest portion of aggregate financing to the real economy in China. The other portions come from foreign loans, corporate bonds, entrusted loans, trust loans, and equity financing on the domestic stock market by nonfinancial enterprises. See https://www.pbc.gov.cn/eportal/fileDir/diaochatongjisi/resource/ cms/2018/04/2018041118111916933.htm (accessed July 16, 2022).

<sup>20</sup> The exact relationship may change as a result of e-banking developments, but it still largely remains true in China in the 2010s.

<sup>21</sup> See https://machinelearningmastery.com/gentle-introduction-xgboostapplied-machine-learning (accessed August 8, 2020).

<sup>22</sup> Results on this finding are available upon request.

<sup>23</sup> See https://en.wikipedia.org/wiki/Social\_mobility (accessed August 8, 2020).

## References

Abadie A, Diamond A, Hainmueller AJ (2010) Synthetic control methods for comparative case studies: Estimating the effect of California’s tobacco control program. J. Amer. Statist. Assoc. 105(490):493–505.

Afrin S, Islam N, Ahmed SU (2009) A multivariate model of micro credit and rural women entrepreneurship development in Ban gladesh. Internat. J. Bus. Management 3(8):169–185.

Agarwal S, Alok S, Ghosh P, Gupta S (2020) Fintech and credit scor ing for the millennials: Evidence using mobile and social footprints. Preprint, submitted January 14, https://dx.doi.org/10. 2139/ssrn.3507827.

Allen F, Demirguc-Kunt A, Klapper L, Martinez Peria MS (2016) The foundations of financial inclusion: Understanding ownership and use of formal accounts. J. Financial Intermediation 27:1–30.

Argyle B, Nadauld T, Palmer C (2020) Real effects of search frictions in consumer credit markets. NBER Working Paper 26645, National Bureau of Economic Research, Cambridge, MA.

Azevedo V, Figal Garone L, Maffioli A, Olarte Rodriguez L (2021) Credit cards issued by non-financial companies: An alternative tool for financial inclusion and economic development. J. Development Effectiveness 13(1):47–83.

Bai Y, Jia R (2016) Elite recruitment and political stability: The impact of the abolition of China’s civil service exam. Econometrica 84(2):677–733.

Banerjee AV, Duflo E (2011) Poor Economics: A Radical Rethinking of the Way to Fight Global Poverty (PublicAffairs, New York).

Banerjee A, Duflo E, Glennerster R, Kinnan C (2015) The miracle of microfinance? Evidence from a randomized evaluation. Amer. Econom. J. Appl. Econom. 7(1):22–53.

Bayer P, Ferreira F, Ross SL (2018) What drives racial and ethnic differences in high-cost mortgages? The role of high-Risk lenders. Rev. Financial Stud. 31(1):175–205

Becchetti L, Castriota S (2011) Does microfinance work as a recovery tool after disasters? Evidence from the 2004 tsunami. World Development 39(6):898–912.

Beck T, Demirguc¨ ¸-Kunt A, Levine R (2007) Finance, inequality and the poor. J. Econom. Growth 12(1):27–49.

Beck T, Levine R, Levkov A (2010) Big bad banks? The winners and losers from bank deregulation in the United States. J. Finance 65(5):1637-1667.

Berg T, Burg V, Gombovic ´ A, Puri M (2020) On the rise of FinTechs: Credit scoring using digital footprints. Rev. Financial Stud. 33(7):2845–2897.

Bhutta N, Goldin J, Homonoff T (2016) Consumer borrowing after payday loan bans. J. Law Econom. 59(1):225–259.

Bhutta N, Skiba PM, Tobacman J (2015) Payday loan choices and consequences. J. Money Credit Banking 47(2–3):223–260

Bittencourt M (2012) Financial development and economic growth in Latin America: Is Schumpeter right? J. Policy Model. 34(3):341–355.

Bjo¨ rkegren D, Grissen D (2018) The potential of digital credit to bank the poor. AEA Papers Proc. 108:68–71.

Blackwell M, Iacus S, King G, Porro G (2009) CEM: Coarsened exact matching in Stata. Stata J. 9(4):524–546.

Boyd B (2019) Promoting economic mobility and racial equity through credit building. Report, United Way of Massachusetts Bay and Merrimack Valley. Accessed March 18, 2021, https:// unitedwaymassbay.org/blog/economic-mobility-through-credit building/.

Brown JR, Cookson JA, Heimer RZ (2019) Growing up without finance. J. Financial Econom. 134(3):591–616.

Brown M, Mazewski M (2015) Stepping stone or quicksand? The role of consumer debt in the U.S. geography of economic mobility. Federal Reserve Bank of St. Louis, Board of Governors of the Federal Reserve System, eds. Economic Mobility: Research & Ideas on Strengthening Families, Communities, & the Economy (Federal Reserve Bank of St. Louis, St. Louis), 205–234.

Busch C (2019) Implementing personalized law. Univ. Chicago Law Rev. 86(2):309–332.

Ce´lerier C, Matray A (2019) Bank-branch supply, financial inclusion, and wealth accumulation. Rev. Financial Stud. 32(12):4767–4809.

Chen T, Guestrin C (2016) XGBoost: A scalable tree boosting system. KDD’16 Proc. ACM SIGKDD Internat. Conf. Knowledge Discov. Data Mining (Association for Computing Machinery, New York), 785–794.

Chopra Y, Tantri PL (2017) Bank accounts for the unbanked: Evi dence from a big bang experiment. Preprint, submitted Febru ary 21, https://dx.doi.org/10.2139/ssrn.2919091.

Clogg CC, Petkova E, Haritou A (1995) Statistical methods for comparing regression coefficients between models. Amer. J. Sociol. 100(5):1261–1293

Cozarenco A, Szafarz A (2020) The regulation of prosocial lending: Are loan ceilings effective? J. Banking Finance 121:105979.

Cull R, Gan L, Gao N, Xu LC (2019) Dual credit markets and household usage to finance: Evidence from a representative Chinese household survey. Oxford Bull. Econom. Statist. 81(6):1280–1317.

Danisewicz P, Elard I (2023) The real effects of financial technology: Marketplace lending and personal bankruptcy. J. Banking Finance 155:106986.

Di Maggio M, Ratnadiwakara D, Carmichael D (2021) Invisible primes: Fintech lending with alternative data. Preprint, submitted October 11, https://dx.doi.org/10.2139/ssrn.3937438.

Dimick JB, Nicholas LH, Ryan AM, Thumma JR, Birkmeyer JD (2013) Bariatric surgery complications before vs. after imple mentation of a national policy restricting coverage to centers of excellence. JAMA 309(8):792–799.

Dobkin C, Finkelstein A, Kluender R, Notowidigdo MJ (2018) The economic consequences of hospital admissions. Amer. Econom. Rev. 108(2):308–352.

Dower PC, Potamites E (2014) Signalling creditworthiness: Land titles, banking practices, and formal credit in Indonesia. Bull. Indonesian Econom. Stud. 50(3):435–459.

Dwyer RE (2018) Credit, debt, and inequality. Annu. Rev. Sociol. 44(1):237–261.

Field E, Torero M (2006) Do property titles increase credit access among the urban poor? Evidence from a nationwide titling pro gram. Working paper, Harvard University, Cambridge, MA.

Fourcade M, Healy K (2013) Classification situations: Life-chances in the neoliberal era. Accounting Organ. Soc. 38(8):559–572.

Funga´cˇova ´ Z, Weill L (2015) Understanding financial inclusion in China. China Econom. Rev. 34:196–206.

Gatti R, Love I (2008) Does access to credit improve productivity? Evidence from Bulgaria. Econ. Transition 16(3):445–465.

Ge R, Feng J, Gu B, Zhang P (2017) Predicting and deterring default with social media information in peer-to-peer lending. J. Man agement Inform. Systems 34(2):401–424.

Ge R, Zheng Z, Tian X, Liao L (2021) Human-robot interaction: When investors adjust the usage of robo-advisors in peer-topeer lending. Inform. Systems Res. 32(3):774–785.

Goodman-Bacon A (2018) Public insurance and mortality: Evidence from Medicaid implementation. J. Polit. Econom. 126(1):216–262.

Greenwood BN, Wattal S (2017) Show me the way to go home: An empirical investigation of ride-sharing and alcohol related motor vehicle fatalities. MIS Quart. 41(1):163–187.

Gross MB, Hogarth JM (2012) Who uses alternative financial services, and why? Consumer Interests Annu. 58:2012–2057.

Hallegatte S, Vogt-Schilb A, Rozenberg J, Bangalore M, Beaudet C (2020) From poverty to disaster and back: A review of the literature. Econom. Disaster. Climate Change 4(1):223–247.

Hasan I, Jackowicz K, Kowalewski O, Kozłowski Ł (2019) The economic impact of changes in local bank presence. Regional Stud. 53(5):644–656.

Herkenhoff KF (2019) The impact of consumer credit access on unemployment. Rev. Econom. Stud. 86(6):2605–2642.

Iacus SM, King G, Porro G (2012) Causal inference without balance checking: Coarsened exact matching. Polit. Anal. 20(1):1–24.

Ichwan I, Kasri RA (2019) Why are youth intent on investing through peer to peer lending? Evidence from Indonesia. J. Islamic Monetary Econom. Finance 5(4):741–762.

Islam A, Maitra P (2012) Health shocks and consumption smoothing in rural households: Does microcredit have a role to play? J. Development Econom. 97(2):232–243.

Jagtiani J, Lemieux C (2019) The roles of alternative data and machine learning in fintech lending: Evidence from the LendingClub con sumer platform. Financial Management 48(4): 1009–1029.

Jayachandran S, Lleras-Muney A, Smith KV (2010) Modern medicine and the twentieth century decline in mortality: Evidence on the impact of sulfa drugs. Amer. Econom. J. Appl. Econom. 2(2):118–146.

Jiang J, Liao L, Lu X, Wang Z, Xiang H (2021) Deciphering big data in consumer credit evaluation. J. Empirical Finance 62:28–45.

Jiang Y, Ho YCC, Yan X, Tan Y (2018) Investor platform choice: Herding, platform attributes, and regulations. J. Management Inform. Systems 35(1):86–116.

Karim A, Noy I (2016) Poverty and natural disasters: A regression meta-analysis. Rev. Econom. Inst. 7(2):2.

Kim JW, King BG (2014) Seeing stars: Matthew effects and status bias in major league baseball umpiring. Management Sci. 60(11):2619–2644.

Kim K, Hann IH (2019) Crowdfunding and the democratization of access to capital-an illusion? Evidence from housing prices. Inform. Systems Res. 30(1):276–290.

Langley P, Anderson B, Ash J, Gordon R (2019) Indebted life and money culture: Payday lending in the United Kingdom. Econom. Soc. 48(1):30–51.

Li H (2018) P2P bankruptcy: Reason, impact and suggestions. BOC Res. 230:1–8.

Lin M, Prabhala NR, Viswanathan S (2013) Judging borrowers by the company they keep: Friendship networks and information asymmetry in online peer-to-peer lending. Management Sci 59(1):17–35.

Liu L, Wang Y, Xu Y (2022) A practical guide to counterfactual estimators for causal inference with time-series cross-sectional data. Amer. J. Polit. Sci., ePub ahead of print August 2, https:// doi.org/10.1111/ajps.12723.

London˜ o-Ve´lez J, Rodr´ıguez C, Sa´nchez F (2020) Upstream and downstream impacts of college merit-based financial aid for low-income students: Ser Pilo Peaga in Colombia. Amer. Econom. J. Econom. Policy 12(2):193–227.

Lu K, Wei Z, Chan TY (2022) Information asymmetry among investors and strategic bidding in peer-to-peer lending. Inform. Systems Res. 33(3):824–845.

Lu T, Zhang Y, Li B (2020) The value of alternative data in credit risk prediction: Evidence from a large field experiment. 40th Internat. Conf. Inform. Systems ICIS 2019 (Association for Information Systems, Atlanta), 1–16.

Madeira C (2019) The impact of interest rate ceilings on households credit access: Evidence from a 2013 Chilean legislation. J. Bank ing Finance 106:166–179

Manski CF, Pepper JV (2018) How do right-to-carry laws affect crime rates? Coping with ambiguity using bounded-variation assumptions. Rev. Econom. Statist. 100(2):232–244.

McKernan SM, Ratcliffe C, Kuehn D (2013) Prohibitions, price caps, and disclosures: A look at state policies and alternative finan cial product use. J. Econom. Behav. Organ. 95:207–223.

Meer J, West J (2016) Effects of the minimum wage on employment dynamics. J. Human Resources 51(2):500–522.

Melzer BT (2011) The real costs of credit access: Evidence from the payday lending market. Quart. J. Econom. 126(1):517–555.

Misostishkhov TZ (2020) Personalized law and fundamental rights Digital Law J. 1(4):56–73.

Morse A (2011) Payday lenders: Heroes or villains? J. Financial Econom. 102(1):28–44

Nemoto N, Huang B, Storey DJ (2019) Optimal regulation of P2P lending for small and medium-sized enterprises. Preprint, sub mitted January 11, https://dx.doi.org/10.2139/ssrn.3313999.

Netzer O, Lemaire A, Herzenstein M (2019) When words sweat: Identifying signals for loan default in the text of loan applica tions. J. Markeint Res. 56(6):960–980.

Paternoster R, Brame R, Mazerolle P, Piquero A (1998) Using the correct statistical test for the equality of regression coefficients Criminology 36(4):859–866.

Peek J, Rosengren E (1995) Bank regulation and the credit crunch. J. Banking Finance 19(3–4):679–692.

People’s Bank of China (2021) All P2P companies in China are closed. Accessed March 3, 2021, https://www.yicai.com/news 100915680.btml

Rambachan A, Roth J (2023) A more credible approach to parallel trends. Rev. Econom. Stud. 90(5):2555–2591.

Ramirez SR (2020) Regulation and the payday lending industry. Contemp. Econom. Policy 38(4):675–693.

Redding SJ, Sturm DM, Wolf N (2011) History and industry location: Evidence from German airports. Rev. Econom. Statist. 93(3):814–831.

Rogers C, Clarke C (2016) Mainstreaming social finance: The regulation of the peer-to-peer lending marketplace in the United Kingdom. British J. Polit. Internat. Relations 18(4):930–945.

Seidman E, Kramer J (2005) Getting to know underbanked consumers: A financial services analysis. Report, Center for Financial Services Innovation, Chicago.

Skiba PM, Tobacman J (2019) Do payday loans cause bankruptcy? J. Law Econo. 62(3):485–519.

Smith TE, Smith MM, Wackes J (2008) Alternative financial service providers and the spatial void hypothesis. Regional Sci. Urban Econom. 38(3):205–227.

Srivastav A, Vallascas F (2022) Small business lending and regula tion for small banks. Management Sci. 68(10):7742–7760.

Stein LCD, Yannelis C (2020) Financial inclusion, human capital, and wealth accumulation: Evidence from the Freedman’s Savings Bank. Rev. Financial Stud. 33(11):5333–5377.

Stuart EA (2010) Matching methods for causal inference: A review and a look forward. Statist. Sci. 25(1):1–21.

Thamae RI, Odhiambo NM (2022) The impact of bank regulation on bank lending: A review of international literature. J. Banking Regulations 23(4):405–418.

Thorne D (2007) Personal bankruptcy and the credit report: Conflict ing mechanisms of social mobility. J. Poverty 11(4):23–43.

Verstein A (2011) The misregulation of person-to-person lending UC Davis Law Rev. 45(2):445–530.

Verstein A (2019) Privatizing personalized law. Univ. Chicago Law Rev. 86(2):551–580

Wahid ANM (1994) The Grameen Bank and poverty alleviation in Bangladesh: Theory, evidence and limitations. Amer. J. Econom. Sociol. 53(1):1–15

Wang H, Overby EM (2021) How does online lending influence bankruptcy filings? Management Sci. 68(5):3309–3329.

Wolfers J (2006) Did unilateral divorce laws raise divorce rates? A reconciliation and new results. Amer. Econom. Rev. 96(5): 1802–1820.

World Bank (2018) Toward universal financial inclusion in China models: Challenges, and global lessons. Report 123323, World Bank, Washington, DC.

Xu Y (2017) Generalized synthetic control method: Causal inference with interactive fixed effects models. Polit. Anal. 25(1):57–76.

You C (2018) Recent development of FinTech regulation in China: A focus on the new regulatory regime for the P2P lending (loanbased crowdfunding) market. Capital Markets Law J. 13(1): 85–115.

Zins A, Weill L (2016) The determinants of financial inclusion in Africa. Rev. Development Financ. 6(1):46–57.

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
