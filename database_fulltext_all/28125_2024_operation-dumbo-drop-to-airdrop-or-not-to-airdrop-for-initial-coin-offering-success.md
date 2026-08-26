---
otero_id: 28125
otero_key: "WM86ZCSF"
title: "Operation Dumbo Drop: To Airdrop or Not to Airdrop for Initial Coin Offering Success?"
authors: "Jian Li; Xiang (Shawn) Wan; Hsing Kenneth Cheng; Xi Zhao"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.0450"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Operation Dumbo Drop: To Airdrop or Not to Airdrop for Initial Coin Offering Success?

Jian Li,<sup>a</sup> Xiang (Shawn) Wan,<sup>b</sup> Hsing Kenneth Cheng,<sup>c</sup> Xi Zhao<sup>a,</sup>\*

<sup>a</sup> School of Management, Xi’an Jiaotong University, Xi’an 710049, China; <sup>b</sup> Leavey School of Business, Santa Clara University, Santa Clara, California 95053; <sup>c</sup> Warrington College of Business, University of Florida, Gainesville, Florida 32611

Contact: lijian\_som\_phd@stu.xjtu.edu.cn, https://orcid.org/0009-0006-1077-6373 (JL); xwan@scu.edu, https://orcid.org/0000-0003-1076-7945 (X(S)W); hkcheng@ufl.edu, https://orcid.org/0000-0001-5787-0777 (HKC); zhaoxi1@mail.xjtu.edu.cn, https://orcid.org/0000-0001-9983-6366 (XZ)

Received: September 3, 2021 Revised: June 25, 2022; July 10, 2023; November 12, 2023 Accepted: January 1, 2024 Published Online in Articles in Advance: February 8, 2024

https://doi.org/10.1287/isre.2021.0450

Copyright: © 2024 INFORMS

Abstract. The rapid advancement and adoption of blockchain technology have heralded an explosive growth of Initial Coin Offerings (ICOs) as a new and popular fundraising approach for blockchain start-ups. To motivate blockchain individuals to invest in the subsequent ICO, a growing number of blockchain-based project founders employ the airdrop campaign, through which they distribute a specific amount of free official tokens or promotional tokens to potential investors on the blockchain with or without their permission. Of paramount concern to the founders contemplating whether to launch an airdrop campaign are whether the airdrop campaign has a positive effect on the potential investors’ invest ment behaviors in their ICOs and how the efficacy of the airdrop may vary with investors. To address these critical questions, we implement a regression discontinuity design by leveraging the quasi-randomization of a blockchain project’s promotional airdrop campaign on the Ethereum platform. We find that the promotional airdrop leads to a 2.3 times increase in the potential investors’ ICO investment probability, as well as a significant and positive effect on their investment amount. We further find that the airdrop is more effective in increasing the investment for individuals with transacted projects dissimilar to the focal project than those with similar ones, which supports the diversification perspective in investment. We also find that the airdrop can motivate token receivers to stick with the focal project for a longer period. We show the generalizability of our findings by leveraging the randomized token airdrop strategies of multiple ICO projects. Our study contributes to the literature on ICOs and marketing strategy for financial instruments and provides important implications to blockchain start-ups on whether and how to launch an airdrop campaign.

History: Xiaoquan (Michael) Zhang, Senior Editor; Huaxia Rui, Associate Editor.

Funding: Financial support from the National Natural Science Foundation of China [Grant 72231007] and the Leavey School of Business of Santa Clara University [Grant GR103420] is gratefully acknowledged. X. Zhao is a Tang Scholar.

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.0450.

Keywords: initial coin offering (ICO) • airdrop • token drop • project similarity • natural language processing • diversification

## 1. Introduction

The advancement of blockchain technology in recent years has created an entirely novel economic layer to the internet protocols, allowing for digital currency transactions and various decentralized financial activities (Swan 2015). Along with the many blockchain-based financial services, Initial Coin Offerings (ICOs) have emerged as a new and popular fundraising approach for blockchain start-ups without involving third-party intermediaries (Howell et al. 2020, Chod and Lyandres 2021). In a typical ICO process, entrepreneurs would accept a wide variety of prevalent cryptocurrencies and fiat currencies and offer newly issued digital assets called “tokens” to investors, which, to some extent, represent the shares of the early stage enterprise they founded and payments for the enterprise’s future products/services (Howell et al. 2020, Gan et al. 2021). The ICO market has witnessed explosive growth recently. By the end of 2020, nearly 6,000 start-ups had attempted to raise capital through ICOs and acquired nearly 28 billion, significantly surpassing the 5.5 billion raised through the wellknown crowdfunding platform Kickstarter.<sup>1</sup> Ethereum is the most popular public blockchain, and more than 85% of blockchain ICO projects release their tokens on Ethereum.<sup>2</sup>

As numerous advertisements for ICOs and token sales are associated with deception and fraud, many national governments and social media platforms, including Facebook, Google, and Twitter, have banned advertisements of ICOs.<sup>3</sup> Consequently, a growing number of blockchain-based project founders start to launch an airdrop campaign before the ICO to advertise their project and motivate potential investors to invest in the subsequent ICO. Airdrop, also known as Coin Drop, is one of the unique phenomena of ICOs compared with other early stage fundraising channels, such as crowdfunding and initial public offerings (IPOs). The airdrop is to distribute a specific amount of free official tokens or promotional tokens to potential investors on the blockchain with or without their permission (Swan 2015, Howell et al. 2020, Harvey et al. 2021). A blockchain project adopting the promotional airdrop campaign distributes promotional tokens to blockchain individuals directly and rewards an additional amount of official tokens to the token receivers if they participate in the ICOs.<sup>4</sup> A critical question facing blockchain-based project founders is whether the promotional airdrop campaign has the desired effect on the individuals’ investment behaviors in the ICO period. Moreover, how would this effect vary with individuals? This research aims to address these crucial questions by empirically examining the blockchain projects’ promotional airdrop campaigns on the Ethereum platform.

Although prior studies have generally demonstrated the positive effects of marketing campaigns for traditional financial instruments like crowdfunding and IPOs (Cook et al. 2006, Hong et al. 2018, Yang et al. 2020, Wei et al. 2021), these findings may not apply directly to token airdrop campaigns in the blockchain context. Factors such as the unregulated ICO market, the transparency of blockchain, and the immutability of blockchain can potentially undermine the effectiveness of traditional marketing strategies. First, in the unregulated ICO market, the lack of standardized information disclosure and certification mechanisms (Bourveau et al. 2022) leads to limited critical information available to potential investors, making it challenging to make sound investment decisions and, thus, diminishing the impact of token airdrops. Second, the transparency of blockchain exposes individuals’ addresses, and the token airdrop without their permission can trigger negative psychological reactance, as individuals feel that their freedom and privacy are compromised, owing to the lack of control over receiving the airdropped token, which can hinder the success of airdrop campaigns. Third, the immutability of blockchain complicates the management of unwanted promotional tokens, as all transactions are permanently recorded, and removing them can be costly.<sup>5</sup> Therefore, the overall efficacy of promotional airdrops in the blockchain context remains uncertain.

To address the aforementioned research questions, we implement a regression discontinuity design (RDD) by leveraging the quasi-randomization of a blockchain project’s promotional airdrop campaign on the Ethereum platform. The official token of this project has been listed on multiple cryptocurrency exchanges after a successful ICO, and its final application—a decentralized platform—was also released in early 2020. Before its ICO, this project launched a large-scale promotional airdrop to individuals on Ethereum in November 2017. Ethereum users were to receive a fixed number of promotional tokens if they had more than 0.1 Ether in their account balance on the snapshot day.<sup>6</sup> Promotional token receivers were able to obtain a 5% bonus for purchasing the official tokens issued by this project during the ICO period. This project provides an ideal RDD context to investigate the effect of promotional airdrops on the individual’s investment behavior for several reasons. First, the rule of distributing promotional tokens (i.e., assigning the treatment) is publicly known afterward and, hence, empirically verifiable. Second, the project can observe the Ethereum individual’s account balance and, thus, can precisely assign the treatment. Third, this project did not announce its airdrop campaign in ad vance, and, thus, all potential investors could not manipulate their account balance (i.e., the assignment variable) to affect whether they could receive the promotional token.

In addition to ascertaining whether the promotional airdrop campaign is effective on the ICO success, our study aims to gain a deeper understanding of how the effect of the airdrop may vary with individuals. Owing to the pseudo-anonymity nature of blockchain individuals (as they are only identifiable by their public key blockchain addresses), it is impossible to gather even traditional demographic characteristics of individuals (e.g., gender, age, education, and residence). Thus, we focus on the transaction history of individuals. Although extensive finance research suggests that diversification can reduce investment risks by investing across sectors, industries, and asset classes (Markowitz 1952, Boyle et al. 2012), literature also reveals that individuals prefer to invest in those familiar to them (Huberman 2001). Therefore, it is of great interest to investigate whether the effect of airdrop is more substantial when the focal project is dissimilar or similar to blockchain projects with which the individual has transacted. Because the white papers of blockchain projects contain the most comprehensive information about the project (Chod and Lyandres 2021, Gan et al. 2021, Bourveau et al. 2022), we leverage the natural language processing techniques to construct the project similarity between the focal project and blockchain projects with which the individual has transacted through the similarity in topics embedded in their white papers.<sup>7</sup>

We find that potential investors on the blockchain have a higher probability of investing in the ICO if they received the promotional token than those who did not. In particular, the airdrop campaign results in a 2.3 times increase in investment probability among those token receivers, as well as a significant and positive effect on the investment amount. We provide evidence about the underlying mechanisms of this finding by leveraging the data of the discussions on the blockchain-based forum and Google search trends. We further find that the airdrop is more effective in increasing the investment probability (and investment amount) for individuals with transacted projects dissimilar to the focal project than those with similar ones, supporting the diversification perspective in investment. We demonstrate the robustness of our findings by conducting a series of validation tests and checks. We also explore the long-term impact of token airdrop and find that those token airdrop receivers stick to the focal project for a longer period in the post-ICO period.

To show the generalizability of our main findings, we further identify multiple projects that implemented the promotional token airdrop strategy. Specifically, we constructed a project-user data set of 1,423,706 Ethereum users and 13 projects implementing the randomized promotional token airdrop strategy. We identify the desired effects by combining the randomized experiment and the fixed effects model. We find consistent results of the airdrop effectiveness, the moderating role of project similarity, and the long-term impact of the token airdrop, indicating the generalizability of our main findings.

Our findings have important and valuable managerial implications for blockchain-based start-ups. First, our study shows the positive effect of the promotional airdrop campaign by increasing the investment probabilities of potential investors. The promotional airdrop strategy can thus be employed to increase the likelihood of success of an ICO. The effectiveness of token airdrop can be attributed to the increased awareness of token receivers and the reward. Thus, to amplify the effect of the promotional token, the start-ups should design a token distribution strategy to draw the individual’s attention as much as possible. For example, blockchainbased start-ups can send promotional tokens to potential investors multiple times with fewer promotional tokens, rather than a one-time airdrop with all tokens. The repeated exposure of the promotional token will amplify the effectiveness of the airdrop because of the informational mechanism. Second, our finding indicates that the airdrop is more effective in increasing the investment probabilities and amount of investors who engage in projects dissimilar to the focal project. Thus, blockchainbased start-ups should target dissimilar investors when launching the airdrop campaign. To this end, blockchain companies can follow the easy-to-implement methods described in our study to construct the overall project similarity from the white papers of blockchain projects.

The remainder of this paper is structured as follows. The following section reviews three streams of literature most relevant to our study and highlights our unique contributions to the literature. Section 3 describes the empirical context, the natural language processing techniques employed in our study, and the model-free evidence. Section 4 presents econometric models, results, validation tests, and robustness checks. Section 5 shows the generalizability of our findings. We conclude this study and offer future research directions in Section 6.

## 2. Literature Review

Our study contributes to the literature on ICOs and marketing strategies for financial instruments. First, we contribute to the literature on ICOs by uncovering the effect of the token airdrop campaign on individuals’ investment behavior. After thorough analyses of massive amounts of data, we empirically confirm the effectiveness of the promotional token airdrop campaign and provide evidence of the underlying mechanisms. Second, we further reveal the heterogeneity in the effectiveness of the token airdrop campaign from the perspective of the similarity between the focal project and projects with which investors have interacted. We find that indi viduals are more likely to invest when the focal project is dissimilar to their historical projects, possibly to diversify their investment. Third, our study contributes to the marketing strategies for financial instruments literature by investigating a new form of direct marketing for the unregulated ICO market of the blockchain context.

## 2.1. ICOs

There are a limited number of studies on the nascent phenomenon of ICOs, and the majority of them focus on empirically investigating the determinants of ICO success (Howell et al. 2020, Momtaz 2021, Xu et al. 2021, Bour veau et al. 2022). For instance, Howell et al. (2020) investigate the role of the issuer and ICO features on fundraising success by analyzing more than 1,500 ICO projects. They find that disclosure, credible commitment, and high-quality signals will positively affect the success of ICOs in this unregulated market. Similarly, based on project-level data, Bourveau et al. (2022) find that a higher level of information disclosure (e.g., white paper, source code) can lead to larger funds raised for ventures during ICO periods, and the facilitation is stronger if such information disclosure is verified through intermediaries. Momtaz (2021) demonstrates that CEO affective traits (extracted from their photos by artificial emotional intelligence) can affect firm valuation in ICO, and the association is more pronounced when asymmetric information is more serious. In addition to determinants during ICO, Lyandres et al. (2022) further explore factors that influence ICO success in the long term and find that post-ICO performance is positively associated with token returns, but negatively associated with return volatility.

A few theoretical studies examine the economics of ICOs. For example, Chod and Lyandres (2021) develop a model of entrepreneurial ventures through ICO and specify when the ICO could dominate traditional venture capital financing models. Gan et al. (2021) propose a three-period ICO model (i.e., ICO period, production period, and market period) with demand uncertainty for a physical product and investigate the optimal design of ICOs in terms of sales cap, token pricing, and production quantity under the assumption of a market-clearing condition, where the total token value equals the total product value.

Although airdropping tokens has become increasingly popular in the blockchain ecology, there is a lack of research on understanding whether the airdrop campaign helps the success of the ICO. Our study contributes to the ICO literature by examining the efficacy of promotional airdrop on individuals’ ICO investment behaviors and how this impact varies with individuals.

## 2.2. Marketing Strategy for Financial Instruments

Prior studies generally show the positive effect of marketing campaigns for traditional financial instruments, such as crowdfunding and IPOs. For instance, Yang et al. (2020) find an overall positive effect of the scarcity-based marketing strategy of setting a limit on the quantity of a particular reward (such as limited edition, price discount, or early access) for crowdfunding campaigns. Wei et al. (2021) find that projects with the prefunding/presale features (typically investments at a discounted price) are more likely to succeed than nonprefunding projects in the context of reward-based crowdfunding, which can be explained by the fact that the volume, length, and sentiment of the prefunding discussions alleviate the information asymmetry between founders and potential backers. Hong et al. (2018) find that increasing social media activity (Twitter activity) around a crowdfunding campaign will positively affect fundraising. Cook et al. (2006) examine the role of promotion on IPO issuance and reveal that a high preoffer date publicity (the number of articles that mention the firm’s name in the headline and the text) enabled by the promotion effort from investment banks can attract more retail investors to an IPO via raising their awareness and interest in an issue.

Previous findings regarding the effectiveness of traditional marketing strategies on crowdfunding and IPOs cannot be directly applied to ascertain whether the airdrop campaign helps the success of ICOs because of three unique features of the blockchain context: the unregulated ICO market, the transparency of blockchain, and the immutability of the blockchain.

First, the unregulated ICO market (Gan et al. 2021, Bourveau et al. 2022) may hinder the effectiveness of the airdrop campaign because of the early stage nature of the ICO project and the lack of critical project information for sound investment decisions. The Organisation for Economic Co-operation and Development states: “From the investor perspective, the investment in IPOs is based on a track record of both operational and financial performance. In ICOs, the investment is made on the basis of a proposed technological concept for a blockchain-enabled solution to a need.”<sup>8</sup> As blockchainbased start-ups attempting to raise funds via an ICO are typically in the pre-research-and-development stage (Chod and Lyandres 2021, Gan et al. 2021), the primary information source for potential investors is the voluntarily disclosed white paper from the start-ups. However, because of the lack of regulation, the information in white papers varies greatly (Howell et al. 2020, p. 3940). Bourveau et al. (2022, p. 131) observe that “some disclosure patterns in white papers differ from IPO prospectuses with regard to risk, financial, and dividend disclosures. Only 4% of white papers mention venturespecific risk factors, and less than 2% provide any financial information or projections.” Therefore, the critical information available for investors in the context of ICO is much less than that in the traditional financial instrument. To complicate the matter, many ICOs and token sales advertisements are even associated with deception and fraud. Therefore, the effectiveness of a token airdrop campaign may suffer, resulting from the early stage nature of ICO projects and the dearth of vital project information for making informed investment decisions.<sup>9</sup>

Second, the transparency of blockchain (Cong and He 2019, Amiram et al. 2022) can adversely affect potential investors’ behavior by triggering their psychological reactance. In the non-blockchain context, investors’ ad dress information (e.g., email addresses) is not public and, thus, is unavailable to all merchants. Moreover, investors can easily block or filter out promotional emails through privacy settings. However, the Ethereum address is public, and any blockchain start-up can send tokens to Ethereum users without their permission. More importantly, there is no feasible way for individuals to block or filter out token distribution or hide their addresses to prevent themselves from receiving promotional tokens. Psychological reactance theory suggests that individuals will be motivated to react oppositely if they feel that their behavioral or attitudinal freedom (e.g., possessions, emotions, and views) is limited or threatened (Lee and Lee 2009, Brehm and Brehm 2013). Thus, blockchain users may have a stronger feeling of intrusiveness about the promotional airdrop than in the traditional non-blockchain context because of losing control over whether to receive the airdropped tokens and what to receive.<sup>10</sup> As a result, the airdrop campaign can negatively affect the token sale by triggering psychological reactance among investors.

Third, the immutability of blockchain will increase the cost of dealing with the airdrop token. In the nonblockchain context, investors can easily deal with the promotions (e.g., coupons or price discounts from the email) by simply blocking or filtering it out, and deleting the email or disposing of a free sample involves little to no cost. However, owing to the immutability of the blockchain, all transactions are permanently recorded on the blockchain users’ accounts, including the transaction of receiving annoying promotional tokens. The only way to remove these tokens from their account is by transferring them to others, while incurring transaction fees.<sup>11</sup>

In sum, the overall efficacy of promotional airdrop cannot be inferred from the extant literature on the marketing campaign for the financial instrument in the nonblockchain context. Our study is among the first to address the critical question facing blockchain-based project (i.e., ICO) founders: whether the promotional airdrop campaign has the desired effect on the individuals investment behaviors in the ICO period and how this effect would vary with individuals.

2.3. Diversification vs. Concentration in Investing Extensive finance literature suggests that diversification can reduce investment risks by investing across sectors, industries, asset classes, and other categories (Markowitz 1952, Boyle et al. 2012). However, finance literature also reveals that individual investors prefer to invest in those with which they are familiar, such as their company’s stock (Benartzi 2001, Cohen 2009), shares of firms they frequent as customers (Keloharju et al. 2012), stocks that are discussed favorably in the media (Huberman 2001), and geographically close stocks (Grinblatt and Keloharju 2001, Massa and Simonov 2006). One reason to invest in familiarity may be behavior bias (Barber and Odean 2005, Polkovnichenko 2005, Goetzmann and Kumar 2008). For example, through conducting a series of experiments, Heath and Tversky (1991, p. 7) find that “people prefer to bet in the context where they consider themselves knowledgeable or competent than in a context where they feel ignorant or uninformed,” and this may explain why some investors are prepared to overlook the benefits of diversification and concentrate on a select group of businesses with which they are likely already familiar. Another stream of literature aims to rationalize why investors tend to invest in familiarities, such as information advantage and awareness of only a subset of the available options. For instance, Ivkovic and Weisbenner (2005) find that investors tend to invest in local stocks, and such decisions are primarily driven by individual investors’ ability to exploit asymmetric information, but not their inclination simply to invest in the companies with which they are familiar. Merton (1987) argues that investors may be only aware of a subset of the available securities and develops a two-period model of capital market equilibrium by incorporating this assumption.

Because promotional token airdrop can raise token receivers’ awareness and provide extra bonuses, we should expect that token airdrop is more effective for the “right” token receivers, who would have a high investing probability once they become aware of the project and the reward. However, it’s unclear whether investors in the context of blockchain will diversify their investments or concentrate on a few familiar ICO projects. If investors tend to invest in diversity (familiarity), they should invest in ICO projects dissimilar (similar) to their historical ICO projects. Answering this question wil help the ICO project identify the right type of potential investors for the airdrop campaign to target. To this end, we focus on how the similarity between the historical projects with which an investor ever interacted and a focal ICO project (called “project similarity”) may affect the effect of the airdrop. Because the white paper of the blockchain project contains the most comprehensive information about a project (Bourveau et al. 2022, Florysiak and Schandlbauer 2022, Thewissen et al. 2022), we measure the project similarity via the similarity of the white papers of the focal and the historical projects, an operationalization of interentity similarity consistent with existing finance literature (Brown and Knechel 2016, Testoni 2022).

## 3. Data and Methodology

In this section, we first describe our empirical context, the data collection process, and the methodology of constructing the similarity between the focal ICO project and the user’s historical projects. Then, we describe the collected data, show the balance checks, and present the model-free evidence.

## 3.1. Empirical Context

Our research design leverages the quasi-randomization of a blockchain project’s promotional airdrop campaign on the Ethereum platform. Ethereum is a public blockchain platform that enables both the peer-to-peer trading network of cryptocurrencies and decentralized applica tions based on “smart contracts”—the trackable and irre versible self-executing contracts written in the computer code residing on the blockchain network. Individuals on Ethereum can utilize the Ethereum virtual machine to develop their smart contracts in decentralization under Ethereum consensus (Cong and He 2019). Because Ethereum is the most popular blockchain platform and has over 600 million transactions from more than 84 million distinct accounts by early 2020, most blockchain projects launch their ICOs and deploy their programmable smart contracts (including token contracts) after the ICOs on Ethereum than other public chains (Howell et al. 2020).

The blockchain ICO project in our study (hereafter referred to as “the focal project”) is an Ethereum-based project. This project initialized its airdrop in November 2017 and issued its official token in 2018 after a successful ICO. The official token of this focal project has been listed on multiple leading cryptocurrency exchanges. The token of the focal project belongs to the utility token (specifically, the platform token), which is used to power a global decentralized grocery marketplace platform connecting manufacturers and consumers. That is, this token is associated with a decentralized application (DApp). The focal project is also well-developed, and its final product was successfully released in early 2020. During the ICO period, interested investors in Ethereum could invest in the focal project’s tokens using virtual currencies (e.g., Bitcoin, Ether) and fiat currency (e.g., U.S. dollars).

The focal project launched a large-scale promotional airdrop to Ethereum users on November 27, 2017, before its ICO period from December 2017 to November 2018. Those individuals who had more than 0.1 Ether in their account balance on the snapshot day of November 17, 2017, received a fixed number of promotional tokens. A snapshot in the blockchain context refers to the recording of “the contents of the entire blockchain ledger, which includes all existing addresses and their associated data (e.g., transactions, fees, balance, metadata).”<sup>12</sup> Those who received promotional tokens obtained a 5% bonus for purchasing tokens during the ICO period. We illustrate the timeline of the focal project’s promotional airdrop campaign in Figure 1.

The focal project provides an ideal context to leverage RDD to investigate the effect of the promotional airdrop on individuals’ investment behavior. First, the rule of distributing a promotional airdrop (i.e., assigning the treatment) is publicly known and, hence, empirically verifiable. Second, the focal project manager can observe the individual’s account balance and, thus, can precisely assign the treatment. Third, this project manager did not announce their airdrop campaign in advance, and, thus, the individuals on Ethereum could not manipulate their account balance (i.e., the assignment variable) to affect whether they received the promotional token.

Our empirical context includes three fundamental components in RDD: (i) individuals’ Ethereum account balance as the assignment variable, (ii) the balance of 0.1 Ether as the cutoff, and (iii) equal amounts of the airdropped promotional token as the treatment. A sharp RDD, as opposed to a fuzzy RDD, is appropriate in our context because the assignment rule is deterministic, as all individuals above the cutoff are treated, and all individuals equal to or below the cutoff are untreated (Calvo et al. 2019). Thus, we adopt a sharp RDD with a single cutoff and continuous assignment variable in subsequent empirical analyses.

## 3.2. Data Collection

We are interested in whether those who received promotional airdrop have a higher probability of investing in the focal project’s ICO than those who did not and how the effect varies with the individuals. To answer these questions, we need to identify who receives the promotional token, who invests in the ICO, and the characteris tics of the focal project and those projects with which individuals have interacted before the ICO of the foca project.

We first collect the account balance information of all individuals on Ethereum on the snapshot day. All activities taking place on Ethereum, including transactions of cryptocurrencies and utilization of smart contracts, are recorded on the platform and are public. This allows us to obtain the desired information on the account balance. We show an example of the home page of an Ethereum account in Figure 2 and a few white papers of the blockchain projects in Online Appendix B. We exclude the addresses of smart contracts, exchanges, miners, and hackers because our interest is individual investors. We identify a total of 9,440,979 valid individual accounts on the snapshot day and then collect their balance information on that day. Among these valid accounts, 926,957 have a balance higher than 0.1 Ether and received the focal project’s promotional airdrop token.

Second, we collect all token-transferring transactions flowing from the focal project to the individual account. These transactions include both the promotional token distribution in the pre-ICO period and official token sales in the ICO period. Specifically, we obtain the following information for each transfer: the unique 42-character hexadecimal address of the airdrop receiver’s Ethereum account; the value of the promotional token or the official token; and the timestamp. The collected information enables us to identify who received the promotional token (and how many) in the pre-ICOs period and who invested in the ICOs period (and how much).

Because RDD only takes observations within a narrow window around the cutoff value for analyses, we choose the data-driven optimal bandwidth of 0.008 Ether around the cutoff value of 0.1 (see Section 5.2 for further details). Out of the 9,440,979 valid individuals, 117,630 are in this range. Finally, we collect the token transaction history of this subgroup of 117,630 individuals and identify the corresponding white papers of projects involved in their transaction history. The white paper, required in the ICO or any other token distribution process for a blockchain-based enterprise, is a document that contains project concepts, technology interpretation, token mechanism, team description, and future business plan to be disclosed to the public for trust and attention (Bourveau et al. 2022). Tokens developed by professional blockchain projects are normally attached to white papers, and individuals’ interactions with these tokens can thus be treated as using products or services of the projects or making an investment like stock trading that has been described in white papers. We collect all transactions for this subgroup of individuals that took place from the release of Ethereum to the day of the focal project’s airdrop campaign. We collect the sender address, the receiver address, the contract address of the token transferred in the transaction, the exact time of the transaction for each transaction, and the corresponding white paper of the transaction. We find a total of 442 valid white papers of blockchain projects from the main cryptocurrency information platforms, as well as their official websites and GitHub repositories.<sup>13</sup>

Figure 1. Timeline of the Focal Project’s Airdrop Campaign  
![](/api/attachments/WM86ZCSF/fulltext/images/520b413723ac917e6a72861f901e767cec001652ca09b29e267d3c1514430714.jpg)

Figure 2. (Color online) Example of an Ethereum Account’s Home Page  
![](/api/attachments/WM86ZCSF/fulltext/images/a0afbbf8b1630ea33bf2dd6eb9b1b9fabf923534892dfc0d91fbe7536c217b3d.jpg)

The next subsection describes how we employ natural language processing (NLP) techniques to construct the similarity between the historical projects with which the individual ever interacted and the focal project (called “project similarity”).

## 3.3. Natural Language Processing

We construct the similarity between projects through the similarity of their white papers. White papers are among the best sources for constructing project similarity because the white paper contains the most comprehensive information about the project, including project concepts, technology interpretation, token mechanism, team description, and future business plan (Bourveau et al. 2022). We present several examples of white papers in Online Appendix B.

The topic modeling method has been widely used in the information systems and finance field to construct interentity similarity in terms of topics embedded in the text. Typically, this method first leverages natural language processing techniques to acquire topics/themes from formulaic texts (Dotzel and Shankar 2019, Toubia et al. 2019, Choi et al. 2021). Then, based on the topics/themes generated from texts, this method can form the topic vector of each entity and further construct the interentity similarity (Adamopoulos et al. 2018, Lee et al. 2020). Accordingly, we use the topic modeling method to construct project similarity.

Following the work of Liu et al. (2020), we utilize the Word Embedding along with the K-means Clustering approach to extract topics from white papers in our data set. In our analyses, we first conduct the basic preprocessing steps (e.g., remove stop-words, stemming, tokenization, lemmatization) and then leverage the Skip-gram model to obtain each word’s word-embedding vector. After acquiring the word-to-vector model, we utilize the K-means clustering algorithm to divide these words into different topics based on their distances in vector space. We apply a data-driven approach, the Elbow method, to locate the optimal number of topics and identify three clusters of topics, including sector, technology, and others. We present the details of the topic construction process in Online Appendix C.

Then, based on the topics generated from the white papers, we construct the interproject similarity (Adamopoulos et al. 2018, Lee et al. 2020). Finally, we aggregate the similarity of the focal project and the projects with which an investor has interacted (called “project similarity”) through the formula: ProjectSim $_ i = \sum _ { j } \left( \frac { t _ { i j } } { \sum _ { j } t _ { i j } } \right.$ $\times P r o j e c t S i m _ { j } )$ , where i denotes investor; $j$ denotes the blockchain project with which an investor has interacted in the past; ProjectSim denotes the similarity of the focal project’s white paper and the project $j ;$ and $t _ { i j }$ denotes the number of times that the individual i has ever interacted with the project j. That is, the similarity between the focal project and an investor’s historical project is a weighted average of the similarity of all projects with which individual has interacted in the past.

Our topic modeling analysis reveals that sector-related topics and technical-related topics are two major clusters embedded in the white papers of the blockchain project. Similar to the construction of overall project similarity, we also construct the project similarity in terms of sector and technology separately by leveraging the topics we identified for these two clusters.

In addition, we construct the project similarity through the textual similarity of their white papers using the Term Frequency-Inverse Document Frequency (TF-IDF) model and Latent Semantic Analysis (LSA) model, which are widely used algorithms to generate textual similarity (Henry and Leone 2016, Larsen and Bong 2016, Guzman and Li 2023). We present the details in Section 4.4.9.

## 3.4. Data Description

We conduct our analysis at the individual level. Among the total of 9,440,979 potential investors counted on the snapshot day, 926,957 had a balance higher than 0.1 Ether<sup>14</sup> and received the promotional airdrop. We identify the causal effect of the promotional airdrop by comparing the difference in investment behaviors between those who received the airdrop and those who did not around the cutoff balance value of 0.1 Ether. We select a subsample of “comparable individuals” in the receiver and non-receiver groups with a balance of around 0.1 Ether based on the data-driven method in the RDD procedure (see Section 4.1 for details). The average investment probability for individuals in the subsample is 0.17%. Moreover, the average investment probability for airdrop receivers (0.0033) is significantly higher than that of non-receivers (0.0013) with a t-value of 6.33 for the difference in means. This provides preliminary evidence that airdrop can improve receivers’ investment probability.

For the subsample of individuals who have transaction history with other blockchain projects before the promotional airdrop, we first construct the overall project similarity in topics embedded in white papers using three different similarity measures, including Inverse of Euclidean Distance, Cosine Similarity, and Jaccard Similarity. Specific definitions and calculations of these three metrics are shown in Online Appendix D. Then, we construct the similarity in sector-related topics and technology-related topics embedded in white papers. We report the summary statistics of variables in Table 1.

3.4.1. Balance Checks. We employ the RDD to investigate the effect of the promotional airdrop campaign on individuals’ investment behaviors in the focal project’s ICO. RDD can be analyzed like randomized experiments around the cutoff balance of 0.1 Ether (Lee and Lemieux 2010). If the investors are truly “locally” randomized around the cutoff 0.1, we should expect that the observed characteristics of investors with the account balance just above the cutoff $( \mathrm { i . e . , }$ receiving the airdrop token) and those just below the cutoff 0.1 are balanced (i.e., not receiving the airdrop token).

We check the balance of the following observed characteristics: account age, the amount of total Ether flows, the amount of Ether outflows, the amount of Ether inflows, the maximum transaction value, average value per transaction, transaction fees spent, maximum historical balance, average daily historical balance, and the moderators including project similarity, sector similarity, and technology similarity. We use the standardized difference as the diagnostic statistic for sample balance and report it in Table 2. We find that all covariates’ standardized differences are less than 0.2 (Cohen 1988), which indicates that these characteristics are statistically indistinguishable between the two groups. This provides further evidence that the RDD in our study is valid.

3.4.2. Model-Free Evidence of Discontinuity. One advantage of the RDD is that it can be presented graphically. We plot how the individuals’ investment probability and log of investment amount vary with their account balances around the cutoff value of 0.1 in Figure $^ { 3 , }$ (a) and (b), respectively. Following the common practice in existing literature (Cattaneo et al. 2019), we fit the cubic polynomial trends to the data below and above the cutoff value in the balance interval of [0.08, 0.12]. We observe a positive jump in both the investment probability and log of investment amount around the cutoff value of 0.1. This jump provides preliminary evidence that the promotional airdrop has a positive effect on the individuals’ ICO participation behaviors. In the following section, we describe in detail how we apply the RDD to examine the effect of promotional airdrops.

Table 1. Summary Statistics

<table><tr><td>Variable</td><td>Description</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td colspan="6">Individuals&#x27; investment behaviors</td></tr><tr><td>Investment probability</td><td>A dummy variable indicating whether an individual invested in official tokens of the ICO</td><td>0.0017</td><td>0.0407</td><td>0.0000</td><td>1.0000</td></tr><tr><td>Investment amount</td><td>Amount ($) of official tokens an individual invested during the ICO period</td><td>5.0337</td><td>310.23</td><td>0.0000</td><td>56,940</td></tr><tr><td colspan="6">Similarity measures</td></tr><tr><td>Project similarity</td><td>Level of overall project similarity in topics embedded in white papers</td><td>7.7081</td><td>2.1133</td><td>2.1835</td><td>14.100</td></tr><tr><td>Sector similarity</td><td>Level of overall project similarity in sector-related topics embedded in white papers</td><td>0.1477</td><td>0.0377</td><td>0.0070</td><td>0.3357</td></tr><tr><td>Technology similarity</td><td>Level of overall project similarity in technology-related topics embedded in white papers</td><td>0.1488</td><td>0.0406</td><td>0.0166</td><td>0.3655</td></tr><tr><td colspan="6">Individual characteristics</td></tr><tr><td>Account age (day)</td><td>Number of days since the emergence of an individual&#x27;s account on Ethereum</td><td>129.60</td><td>132.19</td><td>9.0000</td><td>850.00</td></tr><tr><td>Amount of total Ether flows (Ether)</td><td>The amount of Ether flow in and out through an individual&#x27;s account</td><td>7.3424</td><td>238.02</td><td>0.0000</td><td>51,717</td></tr><tr><td>Amount of Ether outflows (Ether)</td><td>The amount of Ether flow out through an individual&#x27;s account</td><td>3.7994</td><td>120.87</td><td>0.0000</td><td>25,930</td></tr><tr><td>Amount of Ether inflows (Ether)</td><td>The amount of Ether flow in through an individual&#x27;s account</td><td>3.5430</td><td>118.56</td><td>0.0000</td><td>25,786</td></tr><tr><td>Maximum transaction value (Ether)</td><td>The maximum value counted in Ether among an individual&#x27;s historical transactions</td><td>2.3935</td><td>78.616</td><td>0.0000</td><td>19,531</td></tr><tr><td>Average value per transaction (Ether)</td><td>The average value counted in Ether among an individual&#x27;s historical transactions</td><td>1.0583</td><td>21.890</td><td>0.0000</td><td>4,999</td></tr><tr><td>Transaction fees spent (Ether)</td><td>The transaction fees paid based on an individual&#x27;s historical transactions</td><td>0.0008</td><td>0.0107</td><td>0.0000</td><td>1.3616</td></tr><tr><td>Maximum historical balance (Ether)</td><td>The maximum balance of Ether through an individual&#x27;s account history</td><td>1.5208</td><td>35.596</td><td>0.0920</td><td>5,000</td></tr><tr><td>Average daily historical balance (Ether)</td><td>The average daily balance of Ether through an individual&#x27;s account history</td><td>0.3191</td><td>8.6682</td><td>0.0031</td><td>2,177</td></tr></table>

We show in the previous section the preliminary evidence that promotional airdrop receivers have a higher investment probability and investment amount than non-receivers around the cutoff balance value of 0.1. In

## 4. Econometric Specifications and Results

this section, we describe in detail the econometrics methodology and model specification that we employ to examine the effect of promotional airdrop on individuals’ ICO participation decisions and the moderating effect of the project similarity.

Table 2. Balance Checks

<table><tr><td rowspan="2">Variable</td><td colspan="2">Below cutoff</td><td colspan="2">Above cutoff</td><td rowspan="2">Std. diff.</td></tr><tr><td>Mean</td><td>Std. dev.</td><td>Mean</td><td>Std. dev.</td></tr><tr><td>Account age (day)</td><td>126.5000</td><td>127.8800</td><td>144.6000</td><td>150.7400</td><td>-0.1292</td></tr><tr><td>Amount of total Ether flows (Ether)</td><td>7.3170</td><td>249.2800</td><td>7.4690</td><td>172.2000</td><td>-0.0007</td></tr><tr><td>Amount of Ether outflows (Ether)</td><td>3.8190</td><td>126.9700</td><td>3.7020</td><td>84.6170</td><td>0.0011</td></tr><tr><td>Amount of Ether inflows (Ether)</td><td>3.4980</td><td>123.5200</td><td>3.7660</td><td>90.2740</td><td>-0.0025</td></tr><tr><td>Maximum transaction value (Ether)</td><td>2.5410</td><td>85.1630</td><td>1.6660</td><td>30.0620</td><td>0.0137</td></tr><tr><td>Average value per transaction (Ether)</td><td>1.1600</td><td>23.0330</td><td>0.5587</td><td>15.0390</td><td>0.0309</td></tr><tr><td>Transaction fees spent (Ether)</td><td>0.0006</td><td>0.0086</td><td>0.0018</td><td>0.0176</td><td>-0.0887</td></tr><tr><td>Maximum historical balance (Ether)</td><td>1.6110</td><td>36.3560</td><td>1.0760</td><td>31.5890</td><td>0.0157</td></tr><tr><td>Average daily historical balance (Ether)</td><td>0.3316</td><td>9.4283</td><td>0.2576</td><td>2.7290</td><td>0.0107</td></tr><tr><td>Project similarity</td><td>7.6360</td><td>2.2048</td><td>7.9230</td><td>1.7952</td><td>-0.1424</td></tr><tr><td>Sector similarity</td><td>0.1475</td><td>0.0397</td><td>0.1481</td><td>0.0310</td><td>-0.0176</td></tr><tr><td>Technology similarity</td><td>0.1471</td><td>0.0427</td><td>0.1539</td><td>0.0333</td><td>-0.1777</td></tr></table>

Note. Std. Dev., standard deviation; Std. Diff., standardized difference.

Figure 3. Account Balance and Investment Behavior with 95% Confidence Interval  
(a)  
![](/api/attachments/WM86ZCSF/fulltext/images/30fccad9383aa8e11f1858939f851e476ec04076d111fec7893451347ba1b0b2.jpg)  
Notes. (a) Investment probability. (b) Investment amount (\$).

## 4.1. The Effect of Airdrop on ICO Investment

We employ the regression discontinuity design to investigate the effect of the promotional airdrop on an individual’s ICO investment decision and the moderating effect of the similarity between their historical projects and the focal project. Our RDD exploits the quasirandomization of individuals with account balance just above the 0.1 Ether (i.e., airdrop receivers) and those just below the 0.1 Ether threshold (i.e., non-receivers) and conducts the causal inference by comparing the investment decisions between these two groups.

RDD has become “one of the most credible nonexperimental strategies for the analysis of causal effects” (Cattaneo et al. 2019, p. 1). The main idea behind the RDD is that individuals with the score $( \mathrm { i . e . , }$ assignment variable) just below the threshold (and, thus, who did not receive the treatment) are good comparisons to those just above the cutoff (and, thus, who received the treatment), and they can be the valid counterfactual groups (Lee and Lemieux 2010). However, RDD is valid only when individuals cannot precisely manipulate the assignment variable. When these conditions are met, RDD can be employed like randomized experiments, and the discontinuous jump of the outcome variable at the cutoff can be attributed to the treatment effect.

As described in Section 3.1, our experiment context fits a sharp RDD with a single cutoff and continuous assignment variable. Local linear RDD estimation is one of the most popular estimation techniques because it delivers satisfactory boundary properties (Imbens and Lemieux 2008, Fan and Gijbels 2018) and reaches a good trade-off of simplicity, accuracy, and stability in the RDD (Narayanan and Kalyanam 2015). Following existing studies (Li 2018, Cattaneo et al. 2019, Gelman and Imbens 2019), we adopt the standard local linear parametric estimation to estimate the effect of promotional airdrop on the individual’s ICO participation, as specified in Equation (1):

(b)  
![](/api/attachments/WM86ZCSF/fulltext/images/0c8781d0c116882f7e3ccf1831f8559a6ea59b15365cf1aaa893bf51cea39723.jpg)

$$
\begin{array}{c} Y _ {i} = \beta_ {0} + \beta_ {1} \times I (B a l a n c e _ {i} > 0. 1) + \beta_ {2} \times (B a l a n c e _ {i} - 0. 1) \\ + \beta_ {3} \times (B a l a n c e _ {i} - 0. 1) \times I (B a l a n c e _ {i} > 0. 1) + \varepsilon_ {i}; \end{array}\tag{1}
$$

where the dependent variables $Y _ { i } ^ { \prime } \mathrm { { s } }$ are ICO investment behaviors: $P r o b _ { i }$ and $l o g ( A m t _ { i } + 1 )$ , which denotes whether the individual i invested (� 1) in the focal pro ject’s ICO period and the logarithms of the investment amount, respectively. Balance is the account balance of any potential investor on the snapshot day (i.e., assign ment variable). $I ( B a l a n c e _ { i } > 0 . 1 )$ is a dummy variable indicating whether the account balance of individual i is greater than 0:1 Ether. If $B a l a n c e _ { i } > 0 . 1 _ { . }$ , then I(Balance > $0 . 1 ) = 1$ . That is, the individual i received promotional tokens. The interaction between the adjusted assign ment variable (Balance � 0:1) and treatment variable $I ( B a l a n c e _ { i } > 0 . 1 )$ allows different slopes of fitted lines on both sides of the cutoff. Our interest is the unbiased estimates of the coefficient $\beta _ { 1 } ,$ which identifies the causal effect of receiving the promotional airdrop.

We use the triangular kernel functions to choose the optimal bandwidth automatically when estimating the RDD estimator and obtain an optimum value of 0.008 Ether. Therefore, we have a total of 117,630 individuals with a balance lying in the bandwidth of 0.008 Ether around the cutoff value of 0.1 selected as effective observations for estimations. Individuals outside this bandwidth will not be used in the estimation. We report the estimation of Equation (1) in Table 3.

We find a positive and significant coefficient value of 0.0031\*\*\* for $I ( B a l a n c e _ { i } \geq 0 . 1 )$ in column (1) of Table 3 (where \*\*\* indicates $p { < } 0 . 0 0 1 )$ ). This result indicates that the promotional airdrop leads to 2.3 times increase in the investment probability compared with those without receiving the airdrop, who have an average investment probability of 0.0013. Similarly, we find a positive and significant coefficient of 0.0203\*\*\* for $I ( B a l a n c e _ { i } \ge 0 . 1 )$ in column (2) of Table 3. Overall, these findings indicate that the promotional airdrop campaign has a positive effect on potential investors’ ICO investment decisions.

Table 3. RDD Estimation of the Airdrop Effect

<table><tr><td>Variable</td><td>Prob. (1)</td><td>Log(Amt. + 1) (2)</td></tr><tr><td rowspan="2">I(Balance &gt; 0.1)</td><td>0.0031***</td><td>0.0203***</td></tr><tr><td>(0.0005)</td><td>(0.0032)</td></tr><tr><td rowspan="2">Balance - 0.1</td><td>-0.6129***</td><td>-4.1994***</td></tr><tr><td>(0.1020)</td><td>(0.7145)</td></tr><tr><td rowspan="2">I(Balance &gt; 0.1) × (Balance - 0.1)</td><td>0.4460*</td><td>3.1497*</td></tr><tr><td>(0.1945)</td><td>(1.3631)</td></tr><tr><td>Bandwidth</td><td>0.008</td><td>0.008</td></tr><tr><td>Kernel function</td><td>Triangular</td><td>Triangular</td></tr><tr><td>Eff. observations</td><td>117,630</td><td>117,630</td></tr><tr><td>Adj. R2</td><td>0.0007</td><td>0.0006</td></tr></table>

Notes. Standard errors are in parentheses. Adj., adjusted; amt., amount; eff., effective.  
\*p < 0.05; \*\*\*p < 0.001.

After being exposed to the promotional token, the unaware token receivers become aware of the focal project (informational effect), and the aware token receivers subsequently may invest in the focal project, owing to the reward (reward effect). Although the effectiveness of token airdrop can be hampered by the unregulated ICO market, the transparency of blockchain, and the immutability of blockchain, the benefits associated with the informational and reward effects outweigh those negative effects, leading to an overall positive effect of the token airdrop.

## 4.2. Evidence of Underlying Mechanism

If the airdrop campaign can motivate token receivers via informational effect and reward effect, we should expect token receivers to exert more online activities related to focal project after the token airdrop than before. Accordingly, we collect the following two sets of variables related to the focal project: (i) the number of discussions related to the focal project on one of the largest blockchain-related forums, bitcointalk.org; and (ii) normalized Google search trends related to the focal project, the search volume normalized to a scale from 0 to 100 based on the highest search volume on Google. We plot the number of discussions on the forum and normalized Google Trends before and after the airdrop campaign in Figure 4.

Figure 4. Investor Activities Before and After the Token Airdrop  
![](/api/attachments/WM86ZCSF/fulltext/images/3c8790164a41f3f7da6d6238467909e870b78f1e18e4fb171e357701fcb5061d.jpg)  
Notes. (a) Number of discussions on forum. (b) Normalized Google trends.

We observe that the number of discussions and Google search interest increased significantly after the airdrop for the focal project, compared with the pre-airdrop period. These results provide anecdotal evidence that token airdrop can promote token receivers’ investment via the informational and reward effects.<sup>15</sup>

## 4.3. The Moderating Effect of Project Similarity

The previous subsection establishes the positive effect of the promotional airdrop campaign. This subsection provides a deeper understanding of how the effect of promotional airdrop on individuals’ ICO investment behaviors may vary with the similarity between the focal project and the blockchain projects with which an investor has interacted. Accordingly, we run the following Specification (2):

$$
\begin{array}{r l} Y _ {i} & = \beta_ {0} + \beta_ {1} \times I (B a l a n c e _ {i} > 0. 1) + \beta_ {2} \times P r o j e c t S i m _ {i} \\ & + \beta_ {3} \times P r o j e c t S i m _ {i} \times I (B a l a n c e _ {i} > 0. 1) \\ & + \beta_ {4} \times (B a l a n c e _ {i} - 0. 1) + \beta_ {5} \times (B a l a n c e _ {i} - 0. 1) \\ & \times I (B a l a n c e _ {i} > 0. 1) + \varepsilon_ {i}, \end{array}\tag{2}
$$

where the variable ProjecSim in Equation (2) denotes the similarity between the focal ICO project and the projects with which investor i has interacted, which is the similar ity between white papers of the ICO projects (see Section

(b)  
![](/api/attachments/WM86ZCSF/fulltext/images/0a7625b2d89d898a38d4582c4684c6300a5f5da6f16a31ef330b7ab69fbaf294.jpg)

3.3). We also employ alternative methods of computing the project similarity and report the qualitatively same results in Section 4.4 of the robustness checks. All other variables have the same meanings as those in Equation (1). We are interested in estimating the unbiased coefficients of the interaction term between the treatment variable and project similarity $( \mathrm { e . g . } , \beta _ { 3 } ) .$ , which identifies the moderating role of the project similarity.

We note that the variables I(Balance > 0:1) in Equation (2) is exogenous at the investor level (around the cutoff balance of 0.1 Ether) because RDD can be analyzed like randomized experiments (Lee and Lemieux 2010). If the investors are true “locally” randomized around the cutoff 0.1, we should expect that the observed characteristics of investors with an account balance just above the cutoff (i.e., receiving the airdrop token) and those just below the cutoff 0.1 (i.e., not receiving the airdrop token) are balanced. Balance check results reported in Table 2 confirm that these two groups are statistically indistinguishable. This provides further evidence that the RDD in our study is valid.<sup>16</sup> Although the project similarity variable (i.e., ProjectSim ) is endogenous, we can still obtain the unbiased estimation of the coefficient of the interaction term of the project similarity and the treatment variable I(Balance<sub>i</sub> ≥ 0:1) after including the endogenous project similarity variables as the covariates (Kumar and Tan 2015, Wan et al. 2023). The intuition is that the remainder of Equation (2) is uncorrelated with the interaction term after excluding the correlation with endogenous covariates.

We report the estimation of Equation (2) in Table 4.<sup>17</sup> We find a negative and significant coefficient of the interaction item I(Balance<sub>i</sub> > 0:1) × ProjectSim . These findings indicate that the positive effect of promotional airdrop on individuals’ investment in the ICO will decrease with the increase of similarity between the focal project and the projects with which an investor has interacted. One plausible explanation is that investors are looking for diversification while investing in ICO projects and, thus, are more likely to invest in projects dissimilar to projects which with they have interacted. Therefore, the effectiveness of token airdrop is stronger in this subgroup of investors.

Table 4. The Moderating Effect of Project Similarity

<table><tr><td>Variable</td><td>Prob.(1)</td><td>Log(Amt. + 1)(2)</td></tr><tr><td> $I(Balance > 0.1)$ </td><td>0.0055***(0.0007)</td><td>0.0357***(0.0051)</td></tr><tr><td>Balance - 0.1</td><td>-0.5772**(0.1787)</td><td>-3.8304**(1.2699)</td></tr><tr><td> $I(Balance > 0.1) \times (Balance - 0.1)$ </td><td>-0.0096(0.3023)</td><td>0.0585(2.1483)</td></tr><tr><td colspan="3">The moderating role of project similarity</td></tr><tr><td> $I(Balance > 0.1) \times Project Similarity$ </td><td>-0.0054***(0.0006)</td><td>-0.0356***(0.0041)</td></tr><tr><td>Project Similarity</td><td>-0.0020***(0.0002)</td><td>-0.0138***(0.0016)</td></tr><tr><td>Bandwidth</td><td>0.008</td><td>0.008</td></tr><tr><td>Kernel function</td><td>Triangular</td><td>Triangular</td></tr><tr><td>Eff. observations</td><td>58,837</td><td>58,837</td></tr><tr><td>Adj.  $R^{2}$ </td><td>0.0056</td><td>0.0050</td></tr></table>

Notes. Standard errors are in parentheses. Adj., adjusted; amt., amount; eff., effective; prob., probability. \*\*p < 0.01; \*\*\*p < 0.001.

Prior finance literature suggests that individuals should diversify their investments across sectors, industries, asset classes, and other categories (Markowitz 1952, Boyle et al. 2012). Thus, if the diversification in investment drives our above findings, we should expect investors to diversify their investment in sectors in our context. That is, individuals should be more likely to invest in ICO projects with dissimilar sectors. Accordingly, we estimate the specification in Equation (2) to explore the moderating effect of project similarity in terms of the sector (called “sector similarity”). We report the estimation of Equation (2) in Table 5.

We find a negative and significant coefficient of the interaction item I(Balance > 0:1) × Sector Similarity in columns (1) and (2), indicating that the positive effect of the promotional airdrop will decrease with the increase of sector similarity. This finding is consistent with the diversification theory in the finance literature and provides support for the diversification perspective in investment.

Our topic modeling analysis identified two clusters of topics embedded in the white papers of blockchain projects: sector and technology. Thus, it is of great interest to explore whether individuals will diversify their investment in terms of technology. Accordingly, we estimate the specification in Equation (2) to explore the moderat ing effect of project similarity in terms of the technology (called “technology similarity”). We report the estima tion of Equation (2) in Table 5. We find a negative and significant coefficient of the interaction item I(Balance > 0:1) × Tech Similarity in columns (3) and (4), indicating that the positive effect of the promotional airdrop will decrease with the increase of technology similarity. This finding indicates that the high technology uncertainty of our context naturally drives individuals to diversify their investment in the technology aspect. Overall, individuals tend to diversify their investment in ICO projects in both sector and technology.

## 4.4. Validation Tests and Robustness Checks

We employ the local linear regression discontinuity (RDD) estimator with the triangular kernel function in our main analysis. In this section, we conduct additiona analyses to check the robustness of our results.

4.4.1. Density Checks for the Running Variable. We plot the density graph of the running variable (i.e., account balance) in Figure 5. We find a smooth line

Table 5. Underlying Mechanisms of the Moderating Effect of Project Similarity

<table><tr><td>Variable</td><td>Prob.(1)</td><td>Log(Amt. + 1)(2)</td><td>Prob.(3)</td><td>Log(Amt. + 1)(4)</td></tr><tr><td> $I(Balance > 0.1)$ </td><td>0.0040***(0.0007)</td><td>0.0262***(0.0050)</td><td>0.0048***(0.0007)</td><td>0.0315***(0.0051)</td></tr><tr><td>Balance – 0.1</td><td>-0.8300***(0.1766)</td><td>-5.6613***(1.2547)</td><td>-0.8149***(0.1755)</td><td>-5.5039***(1.2470)</td></tr><tr><td> $I(Balance > 0.1) \times (Balance - 0.1)$ </td><td>0.5063(0.3007)</td><td>3.6782(2.1368)</td><td>0.4064(0.3004)</td><td>2.9147(2.1345)</td></tr><tr><td> $I(Balance > 0.1) \times Sector Similarity$ </td><td>-0.0021***(0.0006)</td><td>-0.0126**(0.0042)</td><td></td><td></td></tr><tr><td>Sector Similarity</td><td>-0.0010***(0.0002)</td><td>-0.0065***(0.0016)</td><td></td><td></td></tr><tr><td> $I(Balance > 0.1) \times Tech Similarity$ </td><td></td><td></td><td>-0.0031***(0.0006)</td><td>-0.0203***(0.0043)</td></tr><tr><td>Tech Similarity</td><td></td><td></td><td>-0.0013***(0.0002)</td><td>-0.0092***(0.0016)</td></tr><tr><td>Bandwidth</td><td>0.008</td><td>0.008</td><td>0.008</td><td>0.008</td></tr><tr><td>Kernel function</td><td>Triangular</td><td>Triangular</td><td>Triangular</td><td>Triangular</td></tr><tr><td>Eff. observations</td><td>58,837</td><td>58,837</td><td>58,837</td><td>58,837</td></tr><tr><td>Adj. $R^2$ </td><td>0.0018</td><td>0.0015</td><td>0.0025</td><td>0.0023</td></tr></table>

Notes. Standard errors are in parentheses. Adj., adjusted; amt., amount; eff., effective; prob., probability

$$
^ {* *} p <   0. 0 1; ^ {* * *} p <   0. 0 0 1.
$$

around the cutoff of 0.1 Ether. The McCrary test yields a t-statistic of 0.4541, indicating no manipulation of the running variable (McCrary 2008). Such results are expected because the focal project in our context did not announce its airdrop campaign in advance, and, thus, the individuals on Ethereum cannot manipulate their account balance to affect whether they receive the promotional token.

4.4.2. Falsification Tests on Placebo Cutoffs. Our focal project sets the cutoff at 0.1 Ether and assigns treatments (i.e., sending tokens) to all individuals with an Ether balance above 0.1 Ether. To check the robustness of our findings, we select several placebo cutoffs around 0.1 Ether. Because treatment assignment status around the placebo cutoffs does not really change, we should expect an insignificant effect of the token airdrop at these placebo cutoffs. We run the standard local linear parametric RDD estimation with a triangular kernel function and a bandwidth of 0.008 Ether. Online Appendix E presents the results based on the placebo cutoffs of 0.05, 0.2, and 0.5. We find an insignificant effect of token airdrop around these placebo cutoffs. These results strengthen the causal claim around the cutoff of 0.1 Ether.

4.4.3. Estimations with Different Bandwidths and Kernel Functions. We use the triangular kernel function to automatically generate the optimal bandwidth of 0.008 when estimating the RDD estimator. Following the common robustness checks in the literature, we first shrink the bandwidth to half of the optimal one (i.e., 0.008 × 1/ 2 � 0.004) and then double it $( \mathrm { i . e . , ~ } 0 . 0 0 8 \times 2 = 0 . 0 1 6 )$ to estimate Equations (1) and (2). We report these results based on different bandwidths in Online Appendix F. Our findings are robust with the selection of different bandwidths.

Figure 5. Density Checks around the Cutoff of 0.1 Ether  
![](/api/attachments/WM86ZCSF/fulltext/images/71e94ec2d15a0373574781e1370614d3c0e4b625c655ae98712f62a897078952.jpg)

We also use a uniform kernel to estimate the RDD estimator to check the robustness of our results. The triangular kernel function assigns a weight of zero to all observations with balance outside the optimal bandwidth around the cutoff and assigns positive weights to observations inside the bandwidth, but with a linearly decaying trend from the cutoff. Differently, the uniform kernel assigns all observations inside the optimal bandwidth around the cutoff with equal weight. We report the results based on the uniform kernel in Online Appendix F. Our findings are robust with different kernel functions.

4.4.4. Estimations with High-Order Polynomials. Following existing studies (Li 2018, Cattaneo et al. 2019, Gelman and Imbens 2019), we adopt the standard local linear parametric estimation to estimate the effect of promotional airdrop on the individual’s ICO participation. To address the possibility of pseudo-discontinuity arising from overfitting, we estimate the data with alternative specifications by varying the highest polynomial order of the term (Balance-0.1) from one (i.e., linear) to two and three. We find qualitatively similar results across different specifications. We report the results based on different polynomials in Online Appendix G.

4.4.5. Estimations Controlling for Investor Characteristics. We conduct additional analysis by controlling for investor characteristics, including account age, amount of total Ether flows, total outflow volume, total inflow volume, the maximum transaction amount, amount of total Ether flows, average value per transaction, transaction fees spent, maximum historical balance, and average daily historical balance. We report the estimations in Online Appendix H. We find qualitatively similar results, indicating the robustness of our findings.

4.4.6. Mapping Multiple Addresses to the Same Investor. We construct the project similarity of the focal project and investor’s historical projects based on their transaction history in Ethereum, the most prominent programmable blockchain for launching new crypto tokens. Within the Ethereum network, multiple addresses may belong to the same user. Thus, to measure the project similarity more precisely, we leverage the newly developed method (Victor 2020) to map multiple addresses, all likely belonging to the same user. Then, we conduct analyses based on two newly constructed samples: (i) merging multiple addresses into a single one; and (ii) dropping addresses with multiple address concerns. We find consistent results, indicating the robustness of our findings. We report the details of the mapping methods and estimations in Online Appendix I.

4.4.7. Alternative Weighting Methods for Project Simi larity. We construct project similarity based on investors’ transactions with blockchain projects and weight these blockchain projects’ similarity with the focal project by the number of transactions. We alternatively construct each investor’s project similarity by weighing the projects with the amount (\$) involved in the past related to a project. We find qualitatively similar results, indicating the robustness of our findings. We report the estimations in Online Appendix J.

4.4.8. Alternative Similarity Metrics for Project Similarity. We measure the project similarity by using the inverse of Euclidean distance over topics between them. To check the robustness of our findings regarding the moderating role of project similarity, we use two alternative measurements of project similarity, including Cosine similarity and Jaccard similarity. We report the estimations in Online Appendix K and find qualitatively similar findings.

4.4.9. Alternative Methodologies of Constructing Project Similarity. We construct the project similarity through the topics embedded in the white papers using the topic modeling techniques in our main analysis. We additionally construct the project similarity through the textual similarity of their white papers using the Term Frequency-Inverse Document Frequency model and the Latent Semantic Analysis model, which are widely used algorithms to generate textual similarity (Henry and Leone 2016, Larsen and Bong 2016, Guzman and Li 2023). The TF-IDF model reflects how important a word is to a document in a collection or corpus by weighting a word based on its frequency in a text, but compensated by its frequency in the corpus. The LSA model further transforms the TF-IDF vector space into a semantic space with lower dimensionality to overcome the data sparsity issue and identify word patterns and relationships. We report the estimations in Online Appendix L and find qualitatively similar findings.

## 4.5. Long-term Impact of Token Airdrop

As investors can trade the tokens after the ICO period in the secondary market, it would be of great interest to examine whether investors hold the token of the focal project. Accordingly, we construct three measures related to the investor’s post-ICO behaviors to capture the long-term impact of the promotional airdrop.

The first measure is the size of token holdings (\$) in the post-ICO period. Prior studies in finance show that the size of the number of stock holders is positively related to stock price performance (Amihud et al. 1999). Similarly, the size of token holding in post-ICO periods may affect the token returns in the long term (Lyandres et al. 2022). We thus construct “the size of token holdings in the post-ICO period” as a post-ICO performance outcome variable, which measures the amount (\$) of focal project tokens that each investor holds one year after the ICO.

The second measure is the size of investment (\$) in the secondary market in the post-ICO periods. Prior related studies show that if the majority of people want to buy a stock (i.e., demand side) rather than sell it (i.e., supply side) in the secondary market, the stock price will move up (Lakonishok et al. 1992). A similar phenomenon takes place in the secondary cryptocurrency market (Gan et al. 2021). Hence, we construct a post-ICO performance outcome variable, “the size of investment (\$) in the secondary market in post-ICO periods,” which measures the amount (\$) of focal project tokens that each investor purchases in the secondary market (i.e., crypto exchanges and decentralized exchanges) in one year after ICO.

The third measure is the product trial after its release. The focal project in our context released its product (i.e., platform) in 2020. Thus, investors’ participation is of great importance for the success of the launched platform. Consequently, we construct a post-ICO performance outcome variable, “product trial after its release,” a dummy variable indicating whether the investor participates in the product trial after the focal project’s platform was released in 2020. We estimate the specification in Equation (1) to explore the long-term effect of promotional airdrop with the above three newly constructed outcome variables. We report the estimation results in Table 6.

We consistently find a positive and significant coefficient for the term I(Balance ≥ 0:1) in these three outcome variables. These results indicate that the promotional airdrop motivates token receivers to stick with the focal project for longer. Reciprocal action theory suggests that customers are inclined to “return good for good” (Godfrey et al. 2011). Giving benefits to customers can generate psychological bonding, improve relationship quality, and induce a feeling of gratitude, which can further trigger customers’ reciprocity to repurchase or other feedback (De Wulf et al. 2001). Thus, investors’ reciprocal action of continued interactions with the focal project most likely contributes to the promotional airdrop’s three positive post-ICO results in the long term.

## 5. Generalizability: Multiple Projects with Token Airdrop Campaign

We additionally construct a sample involving multiple projects with the random token airdrop campaign to show the generalizability of our findings. In this section, we present the sample construction process and the analysis and results.

## 5.1. Sample Construction

To validate the generalizability of our main findings, we screened a large number of blockchain projects that launched the promotional token airdrop campaign in our research period. However, only a limited number of projects have the required information (such as the airdrop rule, sale information, and addresses for distributing tokens) for clean causal identification. Among them, 13 projects implemented the randomized promotional token airdrop strategy: sending promotional tokens to a number of randomly selected Ethereum users.

Online Appendix M presents the key characteristics of these 13 projects and our focal project. All of these 13 projects distribute their promotional tokens randomly to Ethereum users. These projects vary in their number of token receivers, rewarding for token receivers, industry, token type, whether connected with DApp, targeted funding size, raised capital, and whether listed successfully.

Then, we construct a project-user data set with the following steps: First, we randomly select an equal number of airdrop non-receivers as that of the airdrop receivers from the Ethereum platform during the airdrop period for each of these 13 projects. We identify 1,423,706 unique individual Ethereum users in this process. Second, we construct a project-user data set involving these 13 projects and 1,423,706 unique Ethereum users. We conduct balance checks and find qualitatively similar characteristics between the token receivers (treated) and non-receivers (control) for each project.

Table 6. Estimations for the Long-term Effect of Token Airdrop

<table><tr><td>Variable</td><td>Token holdings post-ICO ($) (1)</td><td>Investment in the secondary market ($) (2)</td><td>Product trial (1/0) (3)</td></tr><tr><td rowspan="2">I(Balance &gt; 0.1)</td><td>0.0036**</td><td>0.0046*</td><td>0.0003**</td></tr><tr><td>(0.0014)</td><td>(0.0023)</td><td>(0.0001)</td></tr><tr><td rowspan="2">Balance - 0.1</td><td>-0.6931*</td><td>-0.1611</td><td>-0.0253</td></tr><tr><td>(0.2996)</td><td>(0.4995)</td><td>(0.0225)</td></tr><tr><td rowspan="2">I(Balance &gt; 0.1) × (Balance - 0.1)</td><td>0.5361</td><td>-0.4147</td><td>-0.0317</td></tr><tr><td>(0.5716)</td><td>(0.9530)</td><td>(0.0428)</td></tr><tr><td>Bandwidth</td><td>0.008</td><td>0.008</td><td>0.008</td></tr><tr><td>Kernel function</td><td>Triangular</td><td>Triangular</td><td>Triangular</td></tr><tr><td>Eff. observations</td><td>117,630</td><td>117,630</td><td>117,630</td></tr><tr><td>Adj.  $R^2$ </td><td>0.00009</td><td>0.00002</td><td>0.00005</td></tr></table>

Notes. Standard errors are in parentheses. Adj., adjusted; eff., effective. \*p < 0.05; \*\*p < 0.01.

## 5.2. Analysis and Results

We run the following specification in Equation (3) to identify the treatment effect of token airdrop:

$$
Y _ {i j} = \gamma_ {i} + \delta_ {j} + \beta_ {1} \times T r e a t _ {i j} + \varepsilon_ {i j},\tag{3}
$$

where the dependent variable $Y _ { i j }$ includes two investment behaviors for user i to project j: (i) whether the individual i invested (� 1) in the project $j ^ { \prime } \mathrm { s }$ ICO period (Prob ) and (ii) the logarithms of the investment amount $( \log ( A m t _ { i j } + 1 ) )$ . Treat<sub>ij</sub> is a dummy variable indicating whether the individual i receives the promotional airdrop from project j. Coefficient $\beta _ { 1 }$ identifies the effect of the token airdrop, and $\gamma _ { i }$ and $\delta _ { j }$ denote the fixed effect for investor i and project j, respectively.

We report estimations in Table 7. We find a positive and significant coefficient for the term Treat in columns (1) and (2), indicating the positive effect of promotional airdrop on individuals’ investment in the ICO period.

We further leverage the specification in Equation (4) to examine the moderating effect of project similarity and the mechanisms driving the results of the moderating analysis.

$$
\begin{array}{c} Y _ {i j} = \gamma_ {i} + \delta_ {j} + \beta_ {1} \times T r e a t _ {i j} + \beta_ {2} \times P r o j e c t S i m _ {i j} \\ + \beta_ {3} \times P r o j e c t S i m _ {i j} \times T r e a t _ {i j} + \varepsilon_ {i j}. \end{array}\tag{4}
$$

We report the estimation results in Table 8. We find negative and significant coefficients for the interaction term Treat × Project Similarity in columns (1) and (2). These results indicate that the positive effect of promotional airdrop on individuals’ investment in the ICO will decrease with project similarity between the focal project and the projects with which an investor has interacted. We find negative and significant coefficients for the interaction terms Treat × Sector Similarity and Treat × Tech Similarity in columns (3)–(6). These results provide evidence of the diversification perspective in investment.

In addition, we estimate the specification in Equation (3) to explore the long-term effect of promotional airdrop in terms of the number of token holdings in the post-ICO period, the size of investment (\$) in the secondary market in post-ICO periods, and the product trial after its release.<sup>18</sup> We report the estimation results in Table 9. We consistently find a positive and significant coefficient for the coefficient of Treat in these outcome variables. The positive and significant results in columns (1)–(3) indicate that token receivers are more likely to hold the token in the long term and invest in the token in the secondary market.

Table 7. Estimations for the Main Effect of Token Airdrop

<table><tr><td>Variable</td><td>Prob. (1)</td><td>Log(Amt. + 1) (2)</td></tr><tr><td rowspan="2">Treat</td><td>0.0008***</td><td>0.0025***</td></tr><tr><td>(0.0000)</td><td>(0.0002)</td></tr><tr><td>Investor fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Project fixed effect</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>16,210,834</td><td>16,210,834</td></tr><tr><td>Adj.  $R^{2}$ </td><td>0.0221</td><td>0.0249</td></tr></table>

Notes. Standard errors in parentheses are clustered at the investor level. Adj., adjusted; amt., amount; prob., probability. \*\*\*p < 0.001.

Overall, we find consistent results of the main effect of the token airdrop, the moderating effect of project similarity, and the long-term impact. The above results indicate the generalizability of our main findings.

## 6. Discussions and Conclusions

Our study investigates the impact of the promotional airdrop campaign on potential investors’ investment behaviors in the subsequent ICO of the project and how this effect varies with the similarity between the focal block chain project and projects with which investors have interacted. We implement a regression discontinuity design by leveraging the quasi-randomization of a blockchain project’s promotional airdrop campaign on the Ethereum platform. We employ natural language processing techniques to construct the project similarity measure. We find that the promotional airdrop can increase the potential investors’ probability of investing in the focal project’s ICO by 2.3 times, as well as the investment amount. We further provide anecdotal evidence of the underlying mechanisms. We find that the airdrop effect will decrease with the increase in project similarity, a result that supports the diversification perspective in investment. We also find that the token airdrop can motivate token receivers to stick with the focal project for a longer period. We further show the generalizability of our findings based on multiple blockchain projects with airdrop campaigns.

## 6.1. Theoretical Contributions

Our study contributes to the literature on ICOs and marketing strategies for financial instruments. First, compared with extant empirical ICO literature that mainly focuses on project-level data to explore factors influencing ICO success, we are among the first to uncover the effect of the airdrop campaign on the success of ICOs, by examining large-scale individual-level blockchain data. We also provide anecdotal evidence about the underlying mechanisms for the positive effect of the airdrop campaign. Second, we uncover additional insights into the effectiveness of the token airdrop campaign by examining its heterogeneity based on the similarity between the focal project and the projects in which investors have previously engaged. Our findings indicate that individuals are more inclined to invest when their past projects differ from the focal project. This behavior can be attributed to investors’ inclination to diversify their investments. Third, by examining a novel direct-to-investor marketing technique for financial instruments in the unregulated ICO market of the blockchain setting, our research adds to the literature on marketing strategies for financial instruments.

Table 8. Estimations for the Moderating Effect of Project Similarity

<table><tr><td>Variable</td><td>Prob.(1)</td><td>Log(Amt. + 1)(2)</td><td>Prob.(3)</td><td>Log(Amt. + 1)(4)</td><td>Prob.(5)</td><td>Log(Amt. + 1)(6)</td></tr><tr><td>Treat</td><td>0.0023***(0.0001)</td><td>0.0073***(0.0005)</td><td>0.0013***(0.0001)</td><td>0.0039***(0.0003)</td><td>0.0015***(0.0001)</td><td>0.0047***(0.0004)</td></tr><tr><td>Treat × Project Similarity</td><td>-0.0015***(0.0001)</td><td>-0.0050***(0.0004)</td><td></td><td></td><td></td><td></td></tr><tr><td>Project Similarity</td><td>-0.0003***(0.0000)</td><td>-0.0016***(0.0001)</td><td></td><td></td><td></td><td></td></tr><tr><td>Treat × Sector Similarity</td><td></td><td></td><td>-0.0006***(0.0001)</td><td>-0.0022**(0.0002)</td><td></td><td></td></tr><tr><td>Sector Similarity</td><td></td><td></td><td>-0.0001***(0.0000)</td><td>-0.0005***(0.0001)</td><td></td><td></td></tr><tr><td>Treat × Tech Similarity</td><td></td><td></td><td></td><td></td><td>-0.0006***(0.0001)</td><td>-0.0020***(0.0003)</td></tr><tr><td>Tech Similarity</td><td></td><td></td><td></td><td></td><td>-0.0000(0.0000)</td><td>-0.0007***(0.0001)</td></tr><tr><td>Investor fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Project fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>7,078,280</td><td>7,078,280</td><td>7,078,280</td><td>7,078,280</td><td>7,078,280</td><td>7,078,280</td></tr><tr><td>Adj.  $R^2$ </td><td>0.0232</td><td>0.0264</td><td>0.0231</td><td>0.0263</td><td>0.0230</td><td>0.0263</td></tr></table>

Notes. Standard errors are in parentheses. Adj., adjusted; amt., amount; prob., probability. \*\*p < 0.01; \*\*\*p < 0.001.

## 6.2. Managerial Implications

Our findings have important managerial implications for blockchain-based start-ups. First, our study shows the positive impact of such campaigns on the success of ICOs. The promotional airdrop strategy can be effectively utilized to increase the likelihood of a successful ICO. The effectiveness of token airdrops can be attributed to the increased awareness and the rewards provided to token receivers. To maximize the impact of promotional tokens, start-ups can design token distribution strategies that attract receivers’ attention. For instance, instead of a one-time airdrop with all tokens, blockchain-based start-ups can consider multiple distributions of promotional tokens in smaller quantities. Repeated exposure to promotional tokens enhances the effectiveness of the airdrop by leveraging the informational mechanism. Second, our findings indicate that airdrops are particularly effective in increasing the probability and amount of investment from investors engaged in projects dissimilar to the focal project. Therefore, when launching an airdrop campaign, blockchain-based startups should specifically target dissimilar investors. Blockchain start-ups can adopt the method described in our study to assess overall project similarity by analyzing the white papers of blockchain projects. By incorporating the insights from our study into their airdrop campaign strategy, blockchain start-ups can make informed decisions regarding promotional airdrops and effectively target the right potential investors to enhance the success of their ICOs.

Table 9. Estimations for the Long-Term Effect of Token Airdrop

<table><tr><td>Variable</td><td>Token holdings post-ICO(1)</td><td>Investment in the secondary market ($) (2)</td><td>Product trial (1/0)(3)</td></tr><tr><td>Treat</td><td>0.0022***(0.0003)</td><td>0.0003*(0.0001)</td><td>0.0009***(0.0002)</td></tr><tr><td>Investor fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Project fixed effect</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>No. of observations</td><td>16,210,834</td><td>5,172,276</td><td>2,795,725</td></tr><tr><td>Adj.  $R^i$ </td><td>0.0256</td><td>0.0682</td><td>0.0198</td></tr></table>

\*p < 0.05; \*\*\*p < 0.001.  
Notes. Standard errors are in parentheses. Adj., adjusted.

## 6.3. Limitations and Future Directions

Our research has several limitations that provide opportunities for future research. First, our estimates of the promotional airdrop effect may be conservative. The airdrop may affect not only those receivers, but also their social network friends. It is worthwhile for future research to consider the investing behaviors of both the airdrop receivers and their social network friends to estimate the externality effect of airdrop on the friends of receivers. We would expect a larger impact of airdrops considering the social network effect. However, it would be very challenging, if not impossible, to identify the social network friends of individuals who receive the airdrop because each of the receivers’ accounts is only identified by an anonymous, unique, 42-character hexadecimal address. Second, owing to the data limitation, we are unable to identify the online discussion and search behaviors for each blockchain address and, thus, only provide anecdotal evidence of the underlying mechanism through which the airdrop exerts an effect. Third, we leverage the existing method proposed by Victor (2020) to address the multiple addresses issue and show the robustness of our findings. Future studies can further leverage newly developed techniques for identifying multiple blockchain addresses to validate our findings. Fourth, our analysis is conducted at the individual level to reveal how airdrop will affect individual investment decisions and how this effect may vary with investors. Future studies can conduct project-level analysis to demonstrate the overall airdrop effect at the project level by including ICO projects with and without token airdrop and further explore how the airdrop effect varies with project-level characteristics. Last, our study focuses on the major Ethereum platform for ICO projects to release their tokens. Future studies can further improve the generalizability of our findings by including ICO projects launched on smaller platforms, such as Waves and EOS.

## Acknowledgments

The authors thank the senior editor, associate editor, and the three anonymous reviewers for their constructive and insightful suggestions. The authors extend their appreciation for the valuable comments provided by Professor Liangfe Qiu (University of Florida) and Professor Zhiqiang (Eric) Zheng (University of Texas at Dallas), along with the insightful feedback received during presentations of this research at various institutions and conferences. The authors also thank the Inddigo platform (http://inddigo.io) for providing blockchain data and computing capacity.

## Endnotes

<sup>1</sup> Source: https://icobench.com/stats; https://www.kickstarter.com/ help/stats (accessed July 6, 2021).

<sup>2</sup> ICO as a decentralized public fundraising approach does not need a third-party platform to aggregate projects and investors and

conduct investing process management. All investors could send cryptocurrency or fiat currency directly to the venture’s account. These ventures do need a blockchain platform to release their own tokens and distribute them to investors. These platforms include Ethereum, Stellar, Waves, and NEO. Source: https://icobench.com stats (accessed July 6, 2021).

<sup>3</sup> Source: https://www.bloomberg.com/news/articles/2018-03-26/ twitter-joins-facebook-google-in-banning-crypto-coin-sale-ads (accessed July 6, 2021).

The term project in the blockchain context and its corresponding ICO are oftentimes used interchangeably.

<sup>5</sup> We show a few complaints on the airdrop of our focal project on the blockchain-related forums in Online Appendix A.

<sup>6</sup> Ether is the transactional crypto currency on Ethereum for individuals to execute multiple operations.

<sup>7</sup> We show a few examples of the content outline of the white papers of blockchain projects in Online Appendix B.

<sup>8</sup> Source: www.oecd.org/finance/initial-coin-offerings-for-smefinancing.htm (p. 24).

<sup>9</sup> Differently, customers in the traditional free sample marketing campaign can make more informed decisions regarding their potential purchase because they have the opportunity to try out the product or service before committing to a purchase.

<sup>10</sup> We present evidence from blockchain-related forum (bitcointalk. org) postings that token receivers feel intrusiveness of the airdrop; see Online Appendix A.

<sup>11</sup> For example, Ethereum users can dispose of the unwanted tokens by transferring them to the address (0). However, such a transaction incurs a cost of \$8.5 to \$45 in our research period.

<sup>12</sup> Source: https://academy.binance.com/en/glossary/snapshot (accessed June 16, 2022).

<sup>13</sup> The main cryptocurrency information platforms and ICO information aggregators includes etherscan.io, coinmarketcap.com, coingecko. com, icorating.com, icobench.com, icomarks.com, and icoholder.com.

<sup>14</sup> Ether is divisible up to 18 decimal places, and one unit of Ether can exchange for around \$700 at the time of the ICO in December 2017.

<sup>15</sup> Token airdrop campaigns are always accompanied with rewards. Thus, it is nearly impossible to tease out the informational effect and reward effect separately.

<sup>16</sup> To check the robustness of our results, we additionally include a set of observed individual-related control variables. See Section 4.3.5 for details.

<sup>17</sup> Note that we have multiple methods to measure the project similarity. We report the estimation based on the measure of the inverse of Euclidean distance.

<sup>18</sup> We explore the long-term impact of token airdrop in terms of investment in the secondary market for only successfully listed ICOs and the product trial after its release for only ICO projects that launched a product or service.

## References

Adamopoulos P, Ghose A, Todri V (2018) The impact of user personality traits on word of mouth: Text-mining social media platforms. Inform. Systems Res. 29(3):612–640.

Amihud Y, Mendelson H, Uno J (1999) Number of shareholders and stock prices: Evidence from Japan. J. Finance 54(3):1169–1184.

Amiram D, Jørgensen BN, Rabetti D (2022) Coins for bombs: The predictive ability of on-chain transfers for terrorist attacks. J. Accounting Res. 60(2):427–466.

Barber BM, Odean T (2005) Trading is hazardous to your wealth: The common stock investment performance of individual in vestors. J. Finance 55(2):773–806.

Benartzi S (2001) Excessive extrapolation and the allocation of 401(k) accounts to company stock. J. Finance 56(5):1747–1764.

Bourveau T, De George ET, Ellahie A, Macciocchi D (2022) The role of disclosure and information intermediaries in an unregulated capital market: Evidence from initial coin offerings. J. Accounting Res. 60(1):129–167.

Boyle P, Garlappi L, Uppal R, Wang T (2012) Keynes meets Marko witz: The trade-off between familiarity and diversification. Management Sci. 58(2):253–272.

Brehm SS, Brehm JW (2013) Psychological Reactance: A Theory of Free dom and Control (Academic Press, New York).

Brown SV, Knechel WR (2016) Auditor-client compatibility and audit firm selection. J. Accounting Res. 54(3):725–775.

Calvo E, Cui R, Serpa JC (2019) Oversight and efficiency in public projects: A regression discontinuity analysis. Management Sci. 65(12):5651–5675.

Cattaneo MD, Idrobo N, Titiunik R (2019) A Practical Introduction to Regression Discontinuity Designs (Cambridge University Press, Cambridge, UK).

Chod J, Lyandres E (2021) A theory of ICOs: Diversification, agency, and information asymmetry. Management Sci. 67(10):5969–5989.

Choi J, Menon A, Tabakovic H (2021) Using machine learning to revisit the diversification–performance relationship. Strategic Management J. 42(9):1632–1661.

Cohen J (1988) Statistical Power Analysis for the Behavioral Sciences, 2nd ed. (Lawrence Erlbaum Associates Publishers, Mahwah, NJ).

Cohen L (2009) Loyalty-based portfolio choice. Rev. Financial Stud. 22(3):1213–1245.

Cong LW, He Z (2019) Blockchain disruption and smart contracts. Rev. Financial Stud. 32(5):1754–1797.

Cook DO, Kieschnick R, Van Ness RA (2006) On the marketing of IPOs. J. Financial Econom. 82(1):35–61.

De Wulf K, Odekerken-Schro¨der G, Iacobucci D (2001) Investments in consumer relationships: A cross-country and cross-industry exploration. J. Marketing. 65(4):33–50.

Dotzel T, Shankar V (2019) The relative effects of business-to-business (vs. business-to-consumer) service innovations on firm value and firm risk: An empirical analysis. J. Marketing 83(5):133–152.

Fan J, Gijbels I (2018) Local Polynomial Modelling and Its Applications (Routledge, Abingdon, UK).

Florysiak D, Schandlbauer A (2022) Experts or charlatans? ICO analysts and white paper informativeness. J. Banking Finance 139(1):106476.

Gan J, Tsoukalas G, Netessine S (2021) Initial coin offerings, speculation, and asset tokenization. Management Sci. 67(2):914–931.

Gelman A, Imbens G (2019) Why high-order polynomials should not be used in regression discontinuity designs. J. Bus. Econom. Statist. 37(3):447–456.

Godfrey A, Seiders K, Voss GB (2011) Enough is enough! The fine line in executing multichannel relational communication. J. Marketing 75(4):94–109.

Goetzmann WN, Kumar A (2008) Equity portfolio diversification. Rev. Finance 12(3):433–463.

Grinblatt M, Keloharju M (2001) How distance, language, and culture influence stockholdings and trades. J. Finance 56(3): 1053–1073.

Guzman J, Li A (2023) Measuring founding strategy. Management Sci. 69(1):101–118.

Harvey CR, Ramachandran A, Santoro J (2021) DeFi and the Future of Finance (John Wiley & Sons, Hoboken, NJ).

Heath C, Tversky A (1991) Preference and belief: Ambiguity and competence in choice under uncertainty. J. Risk Uncertainty 4(1): 5–28.

Henry E, Leone JA (2016) Measuring qualitative information in capital markets research: Comparison of alternative methodologie to measure disclosure tone. Accounting Rev. 91(1):153–178.

Hong Y, Hu Y, Burtch G (2018) Embeddedness, prosociality, and social influence: Evidence from online crowdfunding. MIS Quart. 42(4):1211–1224.

Howell ST, Niessner M, Yermack D (2020) Initial coin offerings: Financing growth with cryptocurrency token sales. Rev. Financial Stud. 33(9):3925–3974.

Huberman G (2001) Familiarity breeds investment. Rev. Financial Stud. 14(3):659–680.

Imbens GW, Lemieux T (2008) Regression discontinuity designs: A guide to practice. J. Econometrics 142(2):615–635.

Ivkovic Z, Weisbenner S (2005) Local does as local is: Information content of the geography of individual investors’ common stock investments. J. Finance 60(1):267–306.

Keloharju M, Knu¨ pfer S, Linnainmaa J (2012) Do investors buy what they know? Product market choices and investment deci sions. Rev. Financial Stud. 25(10):2921–2958.

Kumar A, Tan YR (2015) The demand effects of joint product adver tising in online videos. Management Sci. 61(8):1921–1937.

Lakonishok J, Shleifer A, Vishny RW (1992) The impact of institutional trading on stock prices. J. Financial Econom. 32(1):23–43.

Larsen KR, Bong CH (2016) A tool for addressing construct identity in literature reviews and meta-analyses. MIS Quart. 40(3):529–552.

Lee G, Lee WJ (2009) Psychological reactance to online recommendation services. Inform. Management 46(8):448–452.

Lee DS, Lemieux T (2010) Regression discontinuity designs in economics. J. Econom. Lit. 48(2):281–355.

Lee GM, He S, Lee J, Whinston AB (2020) Matching mobile applica tions for cross-promotion. Inform. Systems Res. 31(3):865–891.

Li X (2018) Impact of average rating on social media endorsement: The moderating role of rating dispersion and discount threshold. Inform. Systems Res. 29(3):739–754.

Liu Y, Sheng J, Wang W (2020) Technology and cryptocurrency valuation: Evidence from machine learning. Preprint, submitted May 11, https://dx.doi.org/10.2139/ssrn.3577208

Lyandres E, Palazzo B, Rabetti D, Lyandres E, Palazzo B (2022) Initial coin offering (ICO) success and post-ICO performance Management Sci. 68(12):8658–8679.

Markowitz HM (1952) Portfolio selection. J. Finance 7(1):77–91.

Massa M, Simonov A (2006) Hedging, familiarity and portfolio choice. Rev. Financial Stud. 19(2):633–685.

McCrary J (2008) Manipulation of the running variable in the regression discontinuity design: A density test. J. Econometrics 142(2):698–714.

Merton RC (1987) A simple model of capital market equilibrium with incomplete information. J. Finance 42(3):483–510.

Momtaz PP (2021) CEO emotions and firm valuation in initial coin offerings: An artificial emotional intelligence approach. Strategic Management J. 42(3):558–578.

Narayanan S, Kalyanam K (2015) Position effects in search advertising and their moderators: A regression discontinuity approach. Marketing Sci. 34(3):388–407.

Polkovnichenko V (2005) Household portfolio diversification: A case for rank-dependent preferences. Rev. Financial Stud. 18(4):1467–1502.

Swan M (2015) Blockchain: Blueprint for a New Economy (O’Reilly Media, Inc., Sebastopol, CA).

Testoni M (2022) The market value spillovers of technological acqui sitions: Evidence from patent-text analysis. Strategic Management J. 43(5):964–985.

Thewissen J, Shrestha P, Torsin W, Pastwa AM (2022) Unpacking the black box of ICO white papers: A topic modeling approach. J. Corporate Finance 75(6):102225.

Toubia O, Iyengar G, Bunnell R, Lemaire A (2019) Extracting features of entertainment products: A guided latent Dirichlet allocation

approach informed by the psychology of media consumption. J. Marketing Res. 56(1):18–36.

Victor F (2020) Address clustering heuristics for Ethereum. Bonneau J, Heninger N, eds. 24th Internat. Conf. Financial Cryptography Data Security (Springer, Cham), 617–633.

Wan X, Kumar A, Li X (2023) Retargeted vs. generic product recommendations: When is it valuable to give retargeted recommendations? Inform. System Res., ePub ahead of print October 16, https://doi.org/10.1287/isre.2020.0560.

Wei X, Fan M, You W, Tan Y (2021) An empirical study of the dynamic and differential effects of prefunding. Production Oper. Management 30(5):1331–1349.

Xu W, Wang T, Chen R, Zhao JL (2021) Prediction of initial coin offering success based on team knowledge and expert evaluation. Decision Support Systems 147:113574.

Yang L, Wang Z, Hahn J (2020) Scarcity strategy in crowdfunding: An empirical exploration of reward limits. Inform. Systems Res. 31(4):1107–1131.

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
