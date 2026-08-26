---
otero_id: 16642
otero_key: "8VBX6J3R"
title: "How Lending Experience and Borrower Credit Influence Rational Herding Behavior in Peer-to-Peer Microloan Platform Markets"
authors: "Paul Benjamin Lowry; Junji Xiao; Jia Yuan"
year: "2023"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2023.2229128"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Copyright © 2017–2023. This material is presented to ensure timely dissemination of scholarly and technical work. Copyright and all rights therein are retained by authors or by other copyright holders. All persons copying this information are expected to adhere to the terms and constraints invoked by each author's copyright. In most cases, these works may not be reposted without the explicit permission of the copyright holder. The following article is the POST-PRINTS version. An updated version will be available when the article is fully published. If you do not have access, you may contact the authors directly for a copy. The current reference for this work is as follows:

Paul Benjamin Lowry, Junji Xiao, and \*Jia Yuan (2023). “How lending experience and borrower credit influence rational herding behavior in peer-to-peer microloan platform markets,” Journal of Management Information Systems (JMIS) (accepted 07-Mar-2023).

If you have any questions, would like a copy of the final version of the article, or would like copies of other articles we’ve published, please contact any of us directly, as follows:

• Prof. Paul Benjamin Lowry, Eminent Scholar and Suzanne Parker Thornhill Chair Professor

<sub>o</sub> Business Information Technology, Pamplin College of Business

<sub>o</sub> Virginia Tech

<sub>o</sub> Email: Paul.Lowry.PhD@gmail.com

<sub>o</sub> Website: https://sites.google.com/site/professorlowrypaulbenjamin/home

System to request Paul’s articles: https://seanacademic.qualtrics.com/SE/?SID=SV\_7WCaP0V7FA0GWWx

• Dr. Junji Xiao, Associate Professor

<sub>o</sub> Department of Economics, Faculty of Social Sciences

<sub>o</sub> Lingnan University

<sub>o</sub> Email: junjixiao@ln.edu.hk

<sub>o</sub> Website: https://www.ln.edu.hk/econ/en/article/Professor-XIAO-Junji/15/1095/

• Dr. Jia Yuan, Associate Professor

<sub>o</sub> Department of Finance and Business Economics, Faculty of Business Administration

<sub>o</sub> University of Macau

<sub>o</sub> Email: jiayuan@um.edu.mo

<sub>o</sub> Website: https://fba.um.edu.mo/faculty/jiayuan/

\*corresponding author

# How Lending Experience and Borrower Credit Influence Rational Herding Behavior in Peer-to-Peer Microloan Platform Markets

Paul Benjamin Lowry, Ph.D. Business Information Technology Pamplin College of Business Virginia Tech Pamplin Hall, Suite 1007 880 West Campus Drive Blacksburg, VA 24061 Paul.Lowry.PhD@gmail.com

Dr. Lowry is an Eminent Scholar and the Suzanne Parker Thornhill Chair Professor in Business Information Technology at the Pamplin College of Business at Virginia Tech where he serves as the BIT Ph.D. and Graduate Programs Director. He is a former tenured Full Professor at both City University of Hong Kong and The University of Hong Kong. He received his PhD in Management Information Systems from the University of Arizona and an MBA from the Marriott School of Business. He has published 270+ publications, including 150+ journal articles in the Journal of Management Information Systems Information Systems Research, MIS Quarterly, JAIS, ISJ, EJIS, JSIS, JIT, and others. He is on the senior board of editors at the JMIS. He also is an SE at JAIS and ISJ, and AE at ISR. His research interests include (1) organizational and behavioral security and privacy; (2) online deviance, online harassment, and computer ethics; (3) HCI, social media, and gamification; and (4) business analytics, decision sciences, innovation, and supply chains.

Junji Xiao, Ph.D. Department of Economics Faculty of Social Sciences Lingnan University 8 Castle Peak Rd. Tuen Mun, New Territory Hong Kong junjixiao@ln.edu.hk

Dr. Xiao is an Associate Professor in Economics at Lingnan University. He received his Ph.D. in Economics from the University of Toronto. He is an economist with research interest in the fields of empirical industrial organization, environmental economics and China economy. His recent 7work has explored such topics as the competition structure, the welfare effect of environmental policies and the vertical restraints. Before joining Lingnan University, he taught at UTS Business School, the Chinese University of Hong Kong, Fudan University and Shanghai University of Finance and Economics, respectively. He was awarded the German DFG Fellowship in 2001 and Hong Kong RGC grant in 2016. His research papers have been published in such journals as the Journal of Management Information Systems, International Economic Review, Review of Economics and Statistics, Journal of Industrial Economics, Journal of Economics & Management Strategy, Journal of Economic Behavior and Organization, Journal of Environmental Economics and Management, International Journal of Industrial Organization, and Journal of Comparative Economics. He has also worked on commissioned projects for the State Administration for Market Regulation, China.

\*Jia Yuan, Ph.D. Department of Finance and Business Economics Faculty of Business Administration University of Macau Macau jiayuan@um.edu.mo

Dr. Yuan is an Associate Professor of Business Economics at the Faculty of Business Administration, University of Macau. He received his Ph.D. in Economics from the University of Minnesota. His research interests include applied economics, empirical industrial organization, and behavioral economics. Dr. Yuan has publications in journals such as the Journal of Management Information Systems, Journal of Comparative Economics, Journal of Economics Behavior and Organization, Economics Inquiry, Review of Industrial Organization, and others.

\* corresponding author; authors are listed in alphabetical order and authorship was equally shared

How Lending Experience and Borrower Credit Influences Rational Herding Behavior in Peer-to-Peer Microloan Platform Markets

## Abstract

This paper analyzes the herding behavior that characterizes lenders’ lending decisions on a microloan platform and explains how rational herding behavior can resolve the information-asymmetry problem, which is a well-known reason for the failure of online microloan platforms. Using a set of panel data on individual lending decisions acquired from Paipaidai.com (PPDai), an online microloan platform, we examine the influence of the lending decisions of prominent, experienced lenders on novice lenders to identify rational herding behavior. Our empirical analysis demonstrates that rational herding behavior can in fact efficiently reduce lender loss from borrower defaults caused by limited information. Although it is typically assumed that herding behavior is irrational, we find that it can be rational in this context and can thus shed light on why PPDai has succeeded while most other microloan platforms have failed. Accordingly, we make three key contributions: (1) we use heterogeneous herding effects to empirically determine whether lenders’ herding behavior on PPDai is rational based on observational learning; (2) we investigate the moderating effect of borrower credit and novice-lender experience on herding, and we leverage this heterogeneity in lender experience to better explain loan results; and (3) because PPDai publicly provides potential lenders with a transparent credit score—in contrast to platforms like Prosper.com, which leverage hidden proprietary credit information from Experian—we further analyze the credit composition of prominent lenders to better understand the crucial determinants of rational herding. In fact, our follow-up survival simulations indicate that without rational herding, the total number of successful PPDai loans would have decreased by around 46% during the study period—a finding that further underlines the crucial influence of rational herding and the unique contextual factors of PPDai that have fostered it.

Keywords: Peer-to-peer transactions, microloans, herding behavior, information asymmetry, platforms

## Introduction

Peer-to-peer (P2P) lending is the practice of loaning money to people through online platforms that provide services for matching lenders and borrowers [32, 68, 109]. Usually, P2P lending involves small transaction amounts (also known as microloans), and the online platforms involved disintermediate traditional financial institutions and do not require the borrowers to provide collateral; thus, most P2P loans are unsecured microloans. Several researchers have maintained that P2P lending will be one of the coming decade’s most valuable innovations in financial services [32, 95]. Conversely, the anonymity of the borrowers and the unsecured nature of microloans increase the risk of default [88] and give rise to the problems of information asymmetry and moral hazard [27, 65, 81, 104].

Online platforms can lower the risk of default, mitigate the problem of information asymmetry— consequently alleviating adverse selection and moral hazard issues—and increase transaction volume by providing lenders with useful information about borrowers, such as their credit scores or records of their past transactions on the focal platform [46, 48]. For example, Prosper.com, the first US-based microloan platform, provides lenders with potential borrowers’ credit-grade categories [29], which the platform generates using credit scores provided by Experian, an American–Irish multinational consumer-credit reporting company. However, such a credit system works poorly for P2P lending when consumers’ credit information is unavailable or inaccessible [2, 46], which is common in many developing countries, including China, or when most of the borrowers of such unsecured microloans are first-time borrowers who have no transaction records. Thus, one of the reasons behind the rise of microloan platforms in developing countries could be the well-designed credit systems many of these platforms provide.

Arguably the strongest explanation for what lenders do in these situations was theorized by Bikhchandani et al. [10, 11] and Banerjee [6], who provided compelling evidence that in a sequential decision-making process—when decision-makers can combine their private information signals with those of prior decision-makers (i.e., lenders)—their decisions will follow those of the better-informed decisionmakers, thus creating herding behavior. Herding behavior is a natural phenomenon in which animals or humans act collectively but without formal or centralized coordination, and it is pervasive in market and economic contexts [e.g., 6] and even in software adoption [110]. Substantial empirical research has established that herding behavior plays an important role in online P2P lending transactions [e.g., 9, 41, 46, 61, 68, 89, 106, 109]. These studies have suggested that lenders acquire information by observing the actions of individuals who preceded them in the lending process. Lenders are inclined to follow the crowd when making decisions because they believe a large number of preceding decisions to fund a loan request may reflect the collective wisdom regarding the borrower’s trustworthiness.

Such herding behaviors have been empirically observed in P2P lending platforms (e.g., Prosper.com, Pop Funding) in US and other Western markets [e.g., 9, 41, 58, 61, 74, 89, 106, 109]. However, the extant research has not addressed three important research opportunities, on which we focus our research: First, as Kim and Viswanathan [56] suggested, these studies do not shed light on the heterogeneous herding effects of different types of lenders on crowds. These effects have crucial research and practice implications. In terms of research, heterogeneous herding effects can be leveraged to determine whether lenders’ herding behavior is rational: if a crowd herds on experienced lenders rather than inexperienced lenders, it is likely that the crowd has conducted observational learning before engaging in herding, which Zhang and Liu [109] defined as rational herding behavior. In practice, this heterogeneity can prompt microloan platform managers to design listing features that enable borrowers to provide information to the most influential lenders. Although recent studies have proposed theoretical frameworks with which to identify strategies or mechanism designs that would best promote the success of loan listings [7, 17, 28, 45], research has provided scant empirical evidence of the existence and strength of the effects of such platform-designed features on lenders’ contribution behavior [103].

Second, few studies have examined the influence of the platform-supplied information and heterogeneity of lender expertise on herding behavior, with a few recent exceptions [e.g., 102, 103]. Because most of the literature has used cross-sectional variations to investigate the effects of herding behavior or platform-designed features on the success of lending or investment [e.g., 80], it is difficult to identify the influence of platform-designed features and herding and the moderating effects of lender expertise on herding. Moreover, the literature has provided mixed empirical evidence concerning the effects of platform-designed attributes on herding. For example, Jiang et al. [48] found no discrepancies in herding effects between listings assigned high-risk credit grades and those assigned low-risk grades, whereas Xiao et al. [103] suggested that the information dynamically disclosed through communicative messages after fundraising starts has a moderating effect on backer herding. This conflicting evidence indicates that further research is needed to examine the moderating effects of platform-designed attributes on herding.

Third, even fewer studies have investigated specific drivers of herding in P2P platform markets—and most of this research has focused on US and other Western P2P lending markets, with a few notable exceptions [46, 68, 109]. Although the US leads in overall market size of P2P lending, with Europe as a close second, the Asia-Pacific region has the fastest-growing P2P lending market, and at one point China was expected to take a dominant position and to quickly rival the US in market size [13]. The mysteriously rapid growth of the microloan market in China presents a conundrum: how could the market take off so quickly when a centralized credit system was unavailable? Crucially, leveraging empirical observations of this market provides us with an opportunity to identify the drivers of herding and its success. Examining herding behaviors at the macro level across 127 P2P lending markets in China, Jiang et al. [46] provided evidence that rational herding plays an important role in this industry; however, they did not discuss the lack of a centralized credit system, an issue our study uniquely addresses.

To contribute to this research stream, we investigate the phenomenon of herding behavior on Paipaidai.com (PPDai), the largest and most successful P2P platform in China, by examining the practices of PPDai before the P2P loan market was dramatically re-regulated in response to the 2018 crisis (see §2.1 for details). This context is crucial not just because of the market size but because few P2P herding studies have examined herding in the context of emerging markets. We analyze herding from three perspectives. First, we distinguish prominent lenders from novice lenders and focus on the former’s role in determining a follower’s lending behavior. Prominent lenders have accumulated rich experience from their previous loans and thus may be better at judging the potential risks of proposed microloans. By contrast, novice lenders have yet to acquire substantial loan experience. These inexperienced lenders can observe and follow the loan decisions of the prominent lenders—if they believe the prominent lenders have better information about a loan than they do. Thus, novice lenders may herd on a loan listing when they observe prominent lenders entering the listing. This unique context and data allow us to address three research opportunities in the P2P herding literature, as follows.

First, following Zhang and Liu [109], we use heterogeneous herding effects to empirically determine whether lenders’ herding behavior on PPDai is rational based on observational learning. Simonsohn and Ariely [92] suggested that the basis of rational herding is observers’ ability to make unbiased inferences from the decisions they observe, whereas other studies have defined rational herding in terms of inputs from decision-makers without considering the effects of herding. We propose that such herding behaviors are rational in this setting because novice lenders must engage in active, observational learning to identify prominent lenders [109].

To test this proposition, we leverage the performance of loan listings to test the rationality of novice lenders’ herding on prominent lenders. A unique feature of our data is that the performance of the successful transactions is retrieved after the repayment is completed. Analyzing the performance of different kinds of loans enables us to compare the default rates and overall loan returns with different kinds of prominentlender participation. We use the summary statistics from the performance data to justify our claim that the herding behavior of these lenders was indeed rational and thus effective in decreasing information asymmetry and buoying PPDai’s microloan platform at a time when the market was fraught with information asymmetry.

Second, we empirically address the open question concerning the moderating effects of platformdesigned attributes on herding by investigating the moderating effect of borrower credit and novice-lender experience on herding, and we leverage the heterogeneity of novice-lender experience to further explain loan performance. Zhang and Liu [109] suggested that listing features will accentuate the herding effect if herding is rational. Similarly, borrowers’ borrowing credit (BBC) may indicate the riskiness of the listings (where a lower value indicates greater loan risk)—thus serving as an instrument for identifying rational herding behavior. By contrast, lending experience may moderate or reinforce herding, depending on the type of herding. The platform provides information of borrowers, who initiate the loan listings, and the lenders, who commit lending amount. The lenders’ dynamic lending commitments are observable for each loan listing over our sample period. This unique data set with lending information at the individual commitment level enables us to identify the heterogenous herding behavior, which is moderated by lenders’ and borrowers’ experience.

Third, we further analyze the credit composition of prominent lenders to better understand the crucial determinants of rational herding. Importantly, PPDai has always provided potential lenders with this detailed information rather than masking credit details into a proprietary, score-based system, as some leading microloan platforms did (e.g., Prosper.com). This gave us the opportunity to investigate the influence of various kinds of credit information on microloans. We surmise that prominent lenders can accumulate credit through more channels than can novice lenders, an advantage that would give prominent lenders a stronger ability to identify the degree of a loan listing’s risk. By decomposing prominent-lender credit into distinct categories and examining the contribution of each category to novice-lender loan decisions, we identify the theoretical drivers of rational herding in P2P microloan platform markets.

Our study contributes to the understanding of why and how the P2P lending market differs other financial markets and how borrower and lender characteristics affect the rational herding effect. In the PPDai context, the implications are potentially profound, because we conducted follow-up survival simulations that indicate that without rational herding, the total number of successful PPDai loans would have decreased by around 46% during the study period. This finding further underlines the crucial influence of rational herding and the unique contextual factors of PPDai that have fostered it.

## Background

## The P2P Industry in China

The Asia-Pacific region has the fastest-growing market for P2P loan platforms; China now has the dominant position and is expected to soon rival the US in market size [13]. The P2P loan platform market has grown steadily since it emerged in 2007, and its growth peaked at around 6,610 platforms in 2019. However, as noted above, this industry endured a massive shake-up that came at a great cost.<sup>1</sup>

Two of this industry’s key challenges have been the irrational behavior of financially unsavvy lenders and information asymmetry [40, 71]. Around 2013, China’s credit reporting system covered only 60% of its population, and the system’s information was highly limited; even major financial institutions had limited access to the system, and lenders had no access [16]. Moreover, few laws governed the creation, use, and management of credit information at the time [87]. This meant that compared to Western credit systems, China’s was extremely opaque and provided a weak defense against information asymmetry.

The Chinese market recently experienced a major setback in which many platforms failed and billions of RMB were lost by lenders [40]. In January 2016, there were 3,383 P2P platforms in China collectively facilitating approximately RMB 130 billion (USD 18.77 billion) in monthly transactions [70], and by the end of 2018, there were 6,621 platforms facilitating a total of RMB 8.03 trillion (USD 1.26 trillion) [40]. Unfortunately, in 2018 a large number of platforms began to default, peaking at 163 in July [70]. Between 2011 and 2018, over 84% of Chinese P2P lending platforms had failed [40], and approximately 700,000 small lenders lost a total of about RMB 120 billion (USD 18.77 billion) [71]. Although the recent turmoil could be attributed in part to the unsecured nature of P2P lending [47], information asymmetry is a crucial reason for the crisis. To address this crisis, the Chinese government imposed more regulations on the P2P lending market—causing the microloan platforms themselves to become small-loan providers—because the market had been undermined by scams, unscrupulous operators, the irrational behavior of financially unsavvy lenders, and information asymmetry [40, 71].

A few platforms survived this period of tremendous turmoil, and their survival underscores the more effective operations and practices they engaged in when this market was less regulated. In a study of P2Ploan-platform survival in China, He and Li [40] demonstrated that large platforms, those that were publicly listed, and those with better information disclosure, which mitigates information asymmetry, were much less likely to go bankrupt or to experience “run off,” that is, the absconding of platform owners with lender funds. Notably, PPDai, which is known for its good management, innovative information disclosure, and unique credit system, was excellent at reducing information asymmetry and thus was able to continue to operate, adapt successfully to the new regulatory environment, and grow its business.

## The Emergence of PPDai and How It Reduced Information Asymmetry

The PPDai platform, which launched in June 2007, was the first P2P platform in China to offer unsecured loans.<sup>2</sup> As of April 14, 2022, the platform had over 135 million cumulative registered users, had facilitated over 63 million loans, and had a total transaction volume of around RMB 191.8 billion.<sup>3</sup> PPDai is both large and publicly listed, and its innovative processes and credit- and borrower-evaluation schemes have allowed the firm to greatly reduce information asymmetry.

## The Process of and Rules for Lending on PPDai

On PPDai, borrowers initiate loan transactions and post offers; they specify the size, interest rate, and duration of the loans, which vary across loan listings. This information about loan characteristics enables us to investigate the influence of various kinds of credit information on microloans. Lenders are free to review the offers and the borrowers’ credit information (see the next section) and to indicate their loan amount subsequently. PPDai adopted a transaction model similar to that of Prosper.com, where lenders simply need to “lend” an amount before the funding-target amount is reached,<sup>4</sup> which guarantees that lenders will have the opportunity to provide loans to borrowers on a first-come, first-served basis. The minimum lending amount is RMB 50, and the maximum lending amount is the target amount. PPDai updates the lending process when new lenders enter, which makes the ongoing changes in lending information publicly available. If the total amount cannot be met by the due date, a borrower’s offer fails. If a deal is set but the borrower defaults at the due date, PPDai will send out its debt-collecting team to collect the overdue debt. Its rate of debt-collection success is around 85%.

PPDai sets limits on loan sizes, interest rates, and terms. According to its rules, the minimum and maximum loan sizes are RMB 3,000 (USD 470) and RMB 1,000,000 (USD 156,000), respectively; the interest rates must be in the range of 6%–24%; and the loan terms must be 3, 6, 9, 12, 18, or 24 months. A borrower who successfully obtains a loan must make monthly repayments to the lender before the loan’s due date. If a payment is overdue, the borrower will be charged a late fee and penalized with a credit reduction. Borrowers pay two types of fees to the platform, the administrative fee and service commission, whereas lenders are exempt from fees. The administrative fee is 0.3% of the loan size, and the amount of the service commission is based on a borrower’s credit grade.

## PPDai’s Unique Credit-Evaluation Scheme

Because it is difficult to obtain “hard” information about borrowers in this context, PPDai uses several sources of “soft” information about borrowers to help lenders make sound decisions [cf.. 104] and avoid making bad loans, thus reducing default risk. All potential borrowers must submit to PPDai’s unique creditapproval process, which requires a plethora of soft information, such as diplomas, images of borrowers’ ID cards, and cell phone numbers. Because borrowers have successful and unsuccessful loans on PPDai, this information is tracked and integrated as part of the credit assessment. Based on its credit-assessment scheme, PPDai calculates a credit rating for each borrower and shows each borrower’s PPDai loan history, which potential lenders can access.

Table 1 details PPDai’s credit-evaluation scheme, which uses an awards approach to provide clear incentives and disincentives for desired and undesired behaviors, respectively. Borrowers can earn credit points in three ways. First, they can earn them by providing credit information for verification. For example, borrowers who upload their scanned ID card to the platform earn 10 points once their ID is verified, and they earn another 3 points for linking their debit account to the platform and making a successful wire transfer. Second, they earn credit points by inviting friends to the platform; for every friend they invite, borrowers receive 5 points. Third, borrowers earn credit points by successfully paying back loans and are penalized with significant credit-point reductions for each overdue payment.

Table 1. Credit-Evaluation Scheme for Borrowers

<table><tr><td>Category</td><td>Items</td><td>Points</td></tr><tr><td rowspan="5">Verification awards</td><td>Verified ID card</td><td>10</td></tr><tr><td>Video verification: a video clip showing the borrower holding their ID card. Brief self-introduction is a bonus.</td><td>10</td></tr><tr><td>Verified college (same as “high school”) or university diploma</td><td>5</td></tr><tr><td>Verified cellphone number</td><td>10</td></tr><tr><td>Verified debit account number</td><td>3</td></tr><tr><td rowspan="3">Referral awards Transaction awards</td><td>Each invited friend who signs up with Ppdai.com</td><td>5</td></tr><tr><td>Each fully paid loan</td><td>1</td></tr><tr><td>Each overdue payment (over 15 days)</td><td>-2</td></tr></table>

## PPDai’s Unique Lender-Evaluation Scheme

To improve information transparency by leveraging soft information, PPDai has also developed a scheme for evaluating its lenders. Like the credit-evaluation scheme, it is an awards-based system designed to encourage desired and discourage undesired behaviors. Table 2 summarizes the lender-evaluation scheme. Lenders can earn points in two ways. First, like borrowers, lenders earn points by providing documents verifying their soft information. Second, lenders earn points for each of their successful lending transactions.

Table 2. Lender-Evaluation Scheme

<table><tr><td>Category</td><td>Items</td><td>Points</td></tr><tr><td rowspan="5">Verification awards</td><td>Verified ID card</td><td>10</td></tr><tr><td>Video verification: a video clip showing the borrower holding their ID card. Brief self-introduction is a bonus.</td><td>10</td></tr><tr><td>Verified college (same as “high school”) or university diploma</td><td>5</td></tr><tr><td>Verified cellphone number</td><td>10</td></tr><tr><td>Verified debit account number</td><td>3</td></tr><tr><td rowspan="4">Transaction awards</td><td>Each successful lending</td><td>2</td></tr><tr><td>Each completed loan with full repayment of both principal and interest</td><td>2</td></tr><tr><td>Each repayment of principal or interests.</td><td>2</td></tr><tr><td>Each overdue loan</td><td>-10</td></tr></table>

## Herding

Prior research has examined the influence of widely observed herding behaviors on P2P loan transactions. Zhang and Liu [109] suggested that herding is critical to P2P loans because each potential lender can observe the amount of funds provided to a borrower and therefore infer that borrower’s creditworthiness, which contributes to successful transactions. Herzenstein et al. [41] found that lenders engage in strategic herding behavior and that such behavior benefits the lenders. Appendix A Table A1 summarizes several other studies that have documented herding behaviors on P2P lending platforms.

To explain these herding behaviors, the naïve theory posits that consumers (in our context, lenders) make inferences to address their knowledge gaps when asymmetry of information prevails. In such scenarios, customers make decisions based on inferential information [24, 55]. This theory may shed light on herding behaviors on P2P platforms. According to the concept of procedural rationality, herding based on “appropriate deliberation” is a time-saving decision heuristic and a cognitive strategy for reducing transaction costs [5, 90].

## Rationality in Herding

Neoclassical economics theory was developed on the basic postulate of optimization [12, 15, 35, 93]. According to this theory, rational lenders with insufficient information will herd because they believe others have more information and that herding could maximize their utility. Simonsohn and Ariely [92] suggested that the basis of rational herding is the ability of observers to make unbiased inferences from the decisions they observe. However, people can be irrational [33, 44, 75]. Simonsohn and Ariely [92] suggested that irrational herding occurs when consumers (in our context, lenders) simply mimic others without rationally processing their observations of others’ decisions. Thus, such inferences may turn out to be unjustified, and the resulting herding behavior may be irrational.

However, rational herding can result from observational learning [6]. Extending these concepts to the P2P microloan market, Zhang and Liu [109] proposed that the foundation of rational herding is observational learning. Zhang and Liu [109] proposed and empirically supported that under the premise of observational learning, each lender may receive a private signal of a borrower’s creditworthiness by analyzing the listing information based on their personal experience and interaction with borrowers. Thus, lenders can maximize their utility through rational herding and observational learning. More recently, Jiang et al. [46] provided strong evidence that herding at the macro level—i.e., when lenders are choosing a P2P lending platform—is rational.

## Lending Experience and Lending Behavior

Lender experience also plays a critical role in loan decision-making. For example, prominent lenders can better leverage relevant information to avoid loan fraud [36]. Theoretically, the critical role of experience has both economic (i.e., rational) and psychological foundations. Psychology research [51, 54, 94] has shown that a decision-maker’s retrospective evaluations of past episodes affect their choices; however, systematic errors may occur in retrospective evaluations, thus leading the decision-maker to choose inferior options. Economic research has predicted that as an individual’s market experience increases, their behavior will converge to the prediction of neoclassical economics theory prediction [38, 66]. In the context of financial decision-making, novice lenders are more skeptical of financial information and more willing to adopt passive methods of selecting financial options [42]. Because prominent lenders have had more opportunities to learn from experience, they are less likely to respond to irrelevant information, thus enhancing their decision accuracy [30, 76].

Previous research has investigated the effects of experience on online lending. Ward and Clark [101] suggested that experience helps lenders recognize the true value of the target. Zeithammer and Adams [107] found that prominent traders are more likely to behave “rationally” in the sense that their lending behaviors approximate those predicted by theory. List and Shogren [67] showed that experience helps lenders comprehend the strategic implications of second-price auctions. Kagel and Richard [50] concluded that in a first-price common value auction, prominent lenders, in contrast to novice lenders, can on average gain positive profits at least as good as the Nash equilibrium level.<sup>5</sup> Kagel [49] suggested that subjects can improve their lending performance as they accrue experience through repeated participation in English auctions. Yen and Lu [105] found that prominent lenders’ memory recall gives them more product information and that they can make more rational decisions by reviewing relevant information about the product options. In summary, prominent and novice lenders apply different forms of judgment, and this difference results in varying loan decisions. Prominent lenders are more likely to make sound loan decisions.

## Theoretical Model

Our theoretical model highlights the roles of herding in lender decision-making and the moderating effects of borrower and lender heterogeneity on herding. Our operationalized context focuses on PPDai, which famously has strong business practices and unique credit- and user-evaluation schemes designed to reduce information asymmetry. Figure 1 illustrates the processes and mechanisms of the herding effect in the context of P2P loan decisions under the condition of information asymmetry. Following previous studies, we discuss the effects of these factors on loan transactions.

Figure 1. Theoretical Model of the Herding Effect in P2P Microloan Platform Markets  
![](/api/attachments/8VBX6J3R/fulltext/images/7654fe3e20d662f9d69bbff3a4f1b11eedce9979e35f7984539828c32bf1c368.jpg)  
Confirming the Herding Effect in P2P Microloan Platform Markets

When information asymmetry exists between lenders and borrowers, herding arises and affects subsequent lending decisions because lenders perceive predecessor participation as a signal of a borrower’s creditworthiness [61]. The theoretical framework presented in Figure 1 explains the factors that affect novice lenders’ microloan decisions, including the lending amount (LA), cumulative amount (CA), prominent-lender behaviors, and herding effects.<sup>6</sup> At each time point (e.g., time T), a novice lender decides to lend an amount $L A _ { T }$ under the condition of information asymmetry. Although novice lenders have little ability to judge the listing due to limited knowledge, they can refer to signals from predecessor lenders to make their lending decision [10]. The participation of such predecessors in a loan may signal the loan’s quality, thus leading to a follower’s herding behavior. Thus, the total of all predecessors’ lending amounts $L A _ { t }$ for t = 1, 2, …T-1, or the cumulative loans at time T, $\begin{array} { r } { C A _ { T } = \sum _ { t = 1 } ^ { T - 1 } L A _ { t } } \end{array}$ , will influence $L A _ { T }$ if a herding effect exists. Moreover, because such lenders simply mimic predecessor decisions without applying observational learning to the behavior of predecessors, this kind of herding behavior is irrational [109]. Figure 1 represents this type of herding effect with the symbol “(I).”

Crucially, the lending decisions of prominent lenders may generate a rational herding effect. Different lenders will receive different private information about a borrower’s quality and have different perceptions of that quality [109]. Because their experience is richer than that of novice lenders, prominent lenders are more likely to be able to make a better lending decision based on the information they have. Thus, the participation of such predecessors (i.e., prominent lenders) in a loan may signal the loan’s quality, thus leading to a follower’s herding behavior. This herding effect helps materialize the loan listing and allows borrowers to secure larger loans. Because novice lenders have to engage in observational learning to identify the prominent lenders before herding occurs, this type of herding is rational [109]. Using data obtained from Prosper.com, Zhang and Liu [109] found that loans with rational herding are less risky than those without it. Prominent lenders have a better perception of the riskiness of loan listings; thus, loans with prominent-lender participation should have lower risk, which suggests that following prominent lenders is rational. In Figure 1, the symbol “(R)” represents rational herding. In contrast to irrational herding behavior, however, rational herding caused by prominent lenders may generate a structural break in the lending process. Thus, loans involving prominent lenders may exhibit patterns different from those without prominent-lender participation. In turn, such information can thus facilitate the identification of rational herding. Thus, our first hypothesis is an attempt to replicate and confirm the rational herding effect theorized by Zhang and Liu [109], but in a new context and with a new dataset:

H1 (Replication). Rational herding: Loans with prominent-lender participation will have lower risk than those without such participation, generating the rational herding effect, in which the participation of prominent lenders in a loan increases the novice-lender lending amount and shortens the time of loan materialization.

## Heterogeneity in Borrowers’ Creditworthiness

Because borrowers provide the listings, their characteristics—and especially their credit rating—will ultimately determine lenders’ lending-amount decisions. Research has shown that the financial characteristics of a loan listing, including interest rate, loan amount, and loan period, are eventually determined by the borrower’s credit rating [4, 83, 106]; thus, borrowers’ creditworthiness influences the listing’s attractiveness.

Herding occurs due to information asymmetry and indicates lender intentions to use others’ decisions to infer borrower quality. Thus, when borrowers can signal higher quality, rational herding becomes less valuable since the lenders can get the quality information from the listing directly. Zhang and Liu [109] suggested that if lenders are merely imitating the lending decisions of others, they will be less observant regarding—or even oblivious to—how others have arrived at such decisions; however, if they use observational learning, their herding will be moderated by the listing or borrower characteristics. Such observational herding will occur when lenders believe that predecessor lenders who are willing to fund a high-risk listing or a borrower without a strong credit record must have a certain amount of positive private information about that listing or borrower. Thus, characteristics of loan listings will attenuate rational herding. That is, favorable features of the listing or borrower will moderate the herding effect.

To illustrate the moderation effects of the characteristics of loan listings on rational herding, consider two loans that differ only in terms of borrower credit, similar to the example proposed by Xiao et al. [103]: the borrower credit of loan A is higher than that of loan B. In the absence of rational herding, loan A is expected to attract more lenders and higher lending amounts than loan B. However, we observe that after prominent lenders lend on both loans, the loan amounts of the loans align. This indicates that the crowd perceives the prominent lenders’ contributions to loan B as having more informational value and hence relies more heavily on those signals. Intuitively, the crowd perceives less informational value with prominent lenders’ lending on loan A, because their decisions could be explained largely by the borrower’s favorable credit. Regarding loan B, however, the crowd believes that because the borrower’s credit is unfavorable, the prominent lenders must have some positive private information about the listing or borrower. Therefore, we expect that the rational herding effects will be larger for loans with more unfavorable borrower credit, implying that borrower credit attenuates the rational herding effects.

However, it is unlikely that novice lenders will believe that their predecessors with similar lending experience (i.e., peer predecessors) have better private information than they do; thus, rational herding is more likely to be rooted in lenders’ belief that there are prominent lenders who have access to more private information than does the novice lender [56, 68]. Hence, we predict that when we disentangle the influence of such prominent lenders from that of peer novice lenders, the features of loan listings or borrowers will only accentuate the direct effect of prominent-lender participation; moreover such features will reinforce herding on the cumulative amount, because the decision-makers will believe others’ loans are reasonable only when the listings are less risky (unless a prominent lender is involved). However, both types of moderating effect indicate that lenders have engaged in observational learning; hence, an interaction between listing or borrower features and the herding variables (prominent-lender participation and the cumulative account) empirically indicates rational herding behavior. We thus summarize the expected moderating effect of borrower heterogeneity on herding as follows:

H2. Moderating effect of borrower heterogeneity: A borrower’s total credit will dampen rational herding.

## Heterogeneity in Lenders’ Lending Experience

The extant literature has offered conflicting claims about the effects of heterogeneity in lending experience on rational herding. On one hand, Avery and Chevalier [3] proposed that more experienced fund managers have less incentive to herd than inexperienced managers. This proposition is supported by empirical evidence from studies of fund managers [20, 77], security analysts [43], and macroeconomic forecasters [60]. By contrast, Prendergast and Stole [85] suggested that herding increases with experience. Our study supports the latter claim.

Following Zhang and Liu [109], we use heterogeneous herding effects to empirically determine whether lenders’ herding behavior on PPDai is rational based on observational learning. Simonsohn and Ariely [92] suggested that the basis of rational herding is observers’ ability to make unbiased inferences from the decisions they observe, whereas other studies have defined rational herding in terms of inputs from decision-makers without considering the effects of herding. We propose that lenders’ herding behaviors are rational in our setting because novice lenders must engage in active, observational learning to identify prominent lenders [109]. Moreover, part of what makes prominent lenders more successful is their ability to engage in more observational learning than novices. A decision-maker’s experience is a crucial factor of their engagement in rational decision-making [91] and significantly affects herding behavior, although there are still both theoretical debates and controversial empirical evidence regarding its effect. Klein and Militello [57] proposed that prominent individuals develop strong perceptual skills through their experience and that these skills and experiences allow such individuals to simulate mental models more effectively than their less experienced counterparts. They can recognize problems and situations based on the experiential patterns in their memory. They can also concentrate on analytical problem-solving approaches, engage in mistake monitoring, and identify effective solutions to a problem. Such skills allow prominent lenders to make better judgements about the performance of loans. Glaser and Weber [34] suggested that experienced lenders have a more accurate perception of the actual loan return than novice lenders. Thus, as they become experienced, lenders learn from their mistakes [85] and leverage more observational learning over time generates less-biased inferences from the decisions they make [92], thus increasing rational herding, not decreasing it.

We categorize lenders into two types and assume that novice lenders become prominent lenders after accumulating sufficient experience, which enables them to make independent decisions [18]. Before this qualitative change occurs, their lending naïveté causes them to follow their predecessors, including prominent lenders, in making decisions. As they gain experience, novice lenders gradually learn the signaling role of the predecessor lenders; as Prendergast and Stole [85] argued, the herding effect therefore increases with experience. Thus, we propose:

H3. Moderating effect of lender heterogeneity: A lender’s experience will positively influence the herding effect.

## Drivers of Rational Herding

We expect that when rational herding is a driver of lender decisions, prominent lenders with rich experience in P2P loans will play a vital role in materializing a loan listing, because prominent lenders can more accurately analyze the signals sent by borrowers and their participation is thus a useful signal of a borrower’s quality. But what are the drivers of rational herding? Prior research has not addressed this question fully [e.g., 109].

Lender credit is attributed to counts of lending on materialized listings (CML) and lending with successful repayment (CSR).<sup>8</sup> Formally, the CML is defined as the ratio of the counts of lenders’ lending on materialized listings to the counts of their total lending. Likewise, the CSR is defined as the ratio of the counts of lenders’ lending on successfully repaid listings to the counts of their total lending; thus, a high CSR indicates a successful investment. Intuitively, the CSR-based ratio should more accurately indicate that lender’s ability to participate in less risky loans. Consequently, lenders should herd on high-CSR lenders, implying a positive correlation between lending with successful repayment and lending amount. However, lending with successful repayment is conditional on the materialization of a loan listing; thus, the primary risk of a loan listing is its uncertainty of materialization rather than the uncertainty of repayment, which is the secondary risk.

To explain the equity premium puzzle, Benartzi and Thaler [8] proposed the theory of myopic loss aversion. The myopic loss aversion theory combines the theory of loss aversion [52] and the theory of mental accounting [53, 97], and it posits that people are myopic in evaluating outcomes over time and are more sensitive to losses than to gains, a phenomenon Haigh and List [38] confirmed from a neoclassical perspective. The myopic loss aversion theory implies that lenders will pay more attention to lending on materialized listings than to lending with successful repayment, because they will immediately incur a time cost if a listing fails to materialize, whereas the premium from a higher expected return due to a high ratio of lending with successful repayment will be discounted.

By contrast, empirical evidence suggests that lenders may pay more attention to prominent lenders’ record of lending with successful repayment [31, 47]. Galak et al. [31] documented the fact that lenders prefer loans with a shorter repayment period because such loans bear lower default risks. Jiang et al. [47] suggested that the recent turmoil in China’s microloan market is attributable to the unsecured nature of P2P lending, that is, its repayment risks. Namely, if a listing fails to materialize into a loan, the money invested early on will be fully refunded. However, in the event of borrower default, the loan repayment is lost because the loan is unsecured [47]. Consequently, it is reasonable to assume that a risk-averse lender would care more about a loan’s repayment outcome than about the likelihood that a listing will turn into a loan. It thus is crucial to empirically examine whether rational herding in this context is more likely to be driven by lending on materialized listings or by lending with successful repayment. Given the compelling evidence on both sides, we propose the following pair of competing hypotheses:

H4a. Drivers of rational herding: Rational herding is more likely to be driven by lending on materialized listings than by lending with successful repayment.

H4b. Drivers of rational herding: Rational herding is more likely to be driven by lending with successful repayment than by lending on materialized listings.

## Methodology

Using data collected from PPDai, we statistically analyzed the process of a typical PPDai microloan to explain the factors that affect the decision-making of microloan lenders and the microloan performance. We used the feasible generalized least squared (FGLS) estimation to examine the number of lender decisions. This clarified how novice lenders use signals from prominent lenders to make their decisions.

We now explain the background, collection, and analyses of our data. We obtained our data for the PPDai platform from FinVolution Group.<sup>9</sup>

## Data Collection

To obtain our data, we wrote a Python program to scrape and process the loan listings from PPDai for the period of October 2012 to December 2012. Namely, we downloaded all the loan listings that were posted publicly during this period. We obtained a dataset with 5,706 observations. Each observation included variables such as the time at which the loan listing was posted online, the loan size, the interest rate, the duration of the loan, and so on. Based on each of the loan listings, we downloaded the information about all the borrowers and lenders, including their gender, age, borrowing credit, and lending credit. We also downloaded the time at which each lender provided a loan for a listing and the lending amount. A total of 4,643 borrowers and 8,472 lenders took part in P2P loan activities on PPDai during our study period. PPDai published only the usernames of borrowers and lenders (rather than their personal names), so borrowers and lenders were mutually anonymous. The PPDai platform also supplied a public “blacklist” of all the borrowers who had defaulted. Merging this default data with the loan-listing data, we calculated a default rate of roughly 3%, which was much lower than Prosper.com’s 2012 default rate of over 6% [109].<sup>10</sup>

## Measures of Key Variables

## Lending Amount

We used the lending amount of individual lenders at each time point as the dependent variable in the loanamount analysis. We captured the lender characteristics corresponding to each lending and observed their interaction with herding. This protocol extended the extant literature and enabled us to make inferences about the moderating effect of lender characteristics on the herding effect.

## Lender Experience

In the context of online activities, a decision-maker’s experience is typically understood as the extent to which they have previously participated in the activity [84]. For online purchases, the number of previous purchases is an indicator of experience [79]. For online auctions, Easley et al. [26] adopted two measures for experience: the number of auctions in which the lender had participated and the lender’s reputation score. We used PPDai’s lender score as a measure of lender experience. Figure 2 shows how the platform calculates this score. PPDai determines the lender score not only by the number of successful transactions a lender has undertaken (i.e., lending on materialized listings) but also by the successful repayment of loans

![](/api/attachments/8VBX6J3R/fulltext/images/9603604070bbdf5ba194486a9032aa64c51d3418632d69d86091fa1e63207cc5.jpg)

Figure 2. The PPDai Credit Scheme

<table><tr><td colspan="3">Borrowing credits: (30) points [Non real-time updated]</td></tr><tr><td rowspan="4">Real name verification:</td><td>0 point</td><td>Identity verification (10 points)</td></tr><tr><td>0 point</td><td>Video verification (10 points)</td></tr><tr><td>0 point</td><td>Diploma verification (5 points)</td></tr><tr><td>0 point</td><td>Cellphone verification (10 points)</td></tr><tr><td>Other verifications:</td><td>3 points</td><td>Online banking transfer verification (3 points)</td></tr><tr><td>Invitation rewards:</td><td>0 point</td><td>Inviting friends for evaluation: (5 points)</td></tr><tr><td rowspan="2">Transaction records:</td><td>19 points</td><td>Full payment: 19 (1 point per loan)</td></tr><tr><td>0 point</td><td>Overdue repayment (&gt;15 days): 0 (-2 points per loan)</td></tr><tr><td colspan="3">Lending credits: (17528) points [Non real-time updated]</td></tr><tr><td rowspan="4">Real name verification:</td><td>0 point</td><td>Identity verification (10 points)</td></tr><tr><td>0 point</td><td>Video verification (10 points)</td></tr><tr><td>0 point</td><td>Diploma verification (5 points)</td></tr><tr><td>0 point</td><td>Cellphone verification (10 points)</td></tr><tr><td>Bidding rewards:</td><td>3056 points</td><td>Win the bidding (successful lending): 1528 (2 points per lending)</td></tr><tr><td rowspan="3">Return rewards:</td><td>2998 points</td><td>Full Principal and interest received: 1499 (2 points per lending)</td></tr><tr><td>11764 points</td><td>Principal and interest received: 5882 (2 points per lending)</td></tr><tr><td>-290 points</td><td>Overdue (90-unlimited duration): 29 (-10 points per lending)</td></tr></table>

(i.e., lending with successful repayment) in a lender’s history. Because the total credit score indicates a lender’s experience, this score’s composition can reveal the sources of their credit.

## Borrower Credit

PPDai also calculates and publishes the borrower credit measure. Figure 2 illustrates its calculation, which incorporates verified information provided by a lender, lender referral efforts, and both the quantity and quality of a borrower’s previous transactions. For example, borrowers receive 10 points if they have their cellphone numbers verified and another 2 points if they repay a loan. The total borrower credit is the sum of the points acquired from information verification and transaction experience.

## Prominent versus Novice Lenders

We categorized lenders into two types based on their experience. We used a lender credit score of 1,000, which is the 90th-percentile cutoff point in the lender-credit distribution, to distinguish between prominent and novice lenders.<sup>11</sup> That is, we categorized lenders with lender credit equal to or greater than 1,000 as prominent lenders and lenders with lender credit less than 1,000 as novice lenders. Of course, novice lenders could have evolved into prominent lenders as they accrued credit over time, but because our study period was brief, we did not take such developments into consideration. In our later robustness testing, we used a different cutoff value to define the prominent lenders, and the results remained robust.

## Herding

Prior research has measured herding by the lagged total amount of investment, lagged percentage of the loan listing that has been funded, lagged total lending, and lagged average amount [109]. Table A1 summarizes the other measurements of herding used in extant research. To measure irrational herding upon which each lending decision is made, we used (1) the lagged cumulative loan amount and (2) the number of lending proceeding each decision. Zhang and Liu [109] suggested that the correlation between the lagged cumulative amount and an individual’s investment (i.e., loan) amount is attributable to three mechanisms: herding, payoff externalities,<sup>12</sup> and unobserved heterogeneity across listings. Following Zhang and Liu [109], we used the percentage needed for a listing to materialize to control this externality effect. We expected lenders to invest more in listings with a lower risk of failing to materialize (lower percentage needed) and thus that the coefficient of the percentage needed would be negative. We used listing fixed effects to control listing heterogeneity.

To measure a prominent lender’s influence on novice-lender decisions, we used a binary variable that indicated whether a prominent lender (PL) had invested in the loan project (PL = 1) or not (PL = 0). On the assumption that rational herding is contingent on observational learning, the coefficient of this variable thus indicated the rational herding effect because it was necessary for lenders to study predecessor experience to determine which prominent lenders to follow.

The interaction terms between the rational herding of prominent lenders (i.e., the binary variable PL) and the listing features, including the percentage needed for a listing to materialize, can serve as further indications of the two types of herding behavior. Zhang and Liu [109] suggested that the rational herding effect is accentuated by a listing’s unfavorable features and dampened by its favorable features; thus, we expected the coefficient of interaction between rational herding (via a prominent lender) and borrowers’ borrowing credit to be negative. Percentage needed is a measure of the likelihood that a listing will never be funded and therefore an unfavorable feature of the listing; hence, we expected its interaction with prominent lender to have a positive coefficient, which would imply that percentage needed reinforces the rational herding effect.

Prior research has not examined the effect of listing features on irrational herding. Because the listings can be sorted by percentage funded, novice lenders may flood listings with a relatively low percentage left unfunded or with favorable features (such as high borrowers’ borrowing credit) and then engage in irrational herding if they do not know how to use observational learning to gain information about the other aspects of the listing or to assess the experience of prominent lenders. We thus expected the irrational herding effect to be higher for listings with a lower percentage needed for a listing to materialize or with higher borrowers’ borrowing credit.

## Analysis Approach

We examined the herding effect by analyzing the influence of several factors on lenders’ loan-amount decisions. The individual lending amount is a traditional measure of a lender’s preference for a loan listing and is an indicator of a lender’s confidence in a loan’s performance. Lenders will invest a larger amount in a loan with higher expected returns, which are determined by the interest, loan period, and perceived default risk. The first two elements were observable directly from the lists, but the last one was not. However, we were able to control such unobservable features using listing fixed effects.

The logarithmic lending amount of lender i on a loan listing j at time t is denoted by <sub>log</sub> $( L A _ { i j t } )$ Assuming that both herding behavior and listing characteristics (such as borrower credit) determine a lender’s loan-amount decision yields the following formula:

$$
\begin{array}{r l} & {\log (L A _ {i j t}) = \beta_ {0} + \beta_ {1} \log (C A _ {j t}) + \beta_ {2} P L _ {j t} + \beta_ {3} B B C _ {j} \times \log (C A _ {j t}) + \beta_ {4} B B C _ {j} \times P L _ {j t} +} \\ & {\beta_ {5} L L C _ {i} \times \log (C A _ {j t}) + \beta_ {6} L L C _ {i} \times P L _ {j t} + C o n V _ {j t} + \delta_ {j} + \varepsilon_ {i j t},} \end{array}\tag{1}
$$

where $C A _ { j t }$ is the cumulative amount of listing j at time t and $P L _ { j t }$ is a binary variable indicating whether the prominent lender has participated in listing j at time t. $B B C _ { j }$ and $L L C _ { i }$ are borrowers’ borrowing credit and lenders’ lending credit, respectively. $\delta _ { j }$ is the fixed effect for listing $j ;$ it measures unobservable listing features. $C o n V _ { j t }$ includes all the other control variables that contribute to novice-lender decisions, including the variables measuring the time-variant flow information of the loan-listing process (such as percentage needed for the loan to materialize). Herding is one of the components of flow information. Here, $\varepsilon _ { i j t }$ is an unobservable factor that affects lender decisions.

We applied FGLS estimation to the regression of logarithmic lending amount (Eq. [1]). We assigned each listing in our panel data an identity, which was used to control the fixed effect of a listing, including the interest, terms of duration, and all the other unobservable features of a listing. When a lender lent money to the borrower through “lending” (i.e., offered a certain amount to the borrower at a given interest rate and loan duration), the listing status was changed to reflect the cumulative amount and whether the status of prominent-lender involvement had changed. Moreover, the borrowers who initiated the loan listings and the lenders involved in various listings were different. We used such variations within and between the listings to identify the model parameters.

## Analysis Results

## Descriptive Statistics

Our data included the transaction information for 5,706 listings. During the sample period, PPDai was transparent about the loan-listing information, which enabled us to collect the data for our analysis. Of these listings, 3,517 were successfully funded, for a successful-funding rate of 61.40%. Table 3 provides summary statistics of the key variables. On average, the successfully funded loans had larger loan amounts than the unsuccessfully funded loans, although the proposed interest rates and terms were similar between these two types. Because small loans are often for one-time consumption spending, such as the purchase of an iPhone, this finding suggested that lenders cared about the purpose of the loan. They were more inclined to lend for loans with an investment purpose than for loans intended to support a consumer purchase.

PPDai’s lending rules stated that anyone who had a mainland-China ID card and was 22–65 years old was qualified to borrow; the same rules applied to lenders, with the exception that they could start at age 20. Table 4 summarizes the demographic data for the borrowers and lenders in our panel. A feature of the successful borrowers was that their age distribution lay to the right of the entire sample distribution, which suggested that senior borrowers accounted for a disproportionately larger share of all the borrowers who posted successful listings. Most of the lenders (about 70%) were male, and most were over 26 years old.

Table 3. Summary Statistics of All Loan Listings

<table><tr><td>Variable</td><td>Obs</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td colspan="6">All Loan Listings:</td></tr><tr><td>Loan size</td><td>5,706</td><td>6,671.34</td><td>17,629.74</td><td>3,000</td><td>300,000</td></tr><tr><td>Proposed interest rate (%)</td><td>5,671</td><td>20.67</td><td>2.46</td><td>9</td><td>25.24</td></tr><tr><td>Loan term (month)</td><td>5,671</td><td>6.23</td><td>3.01</td><td>1</td><td>12</td></tr><tr><td colspan="6">Successfully Funded Loan Listings:</td></tr><tr><td>Loan amount</td><td>3,517</td><td>8,968.80</td><td>22,193.24</td><td>3,000</td><td>300,000</td></tr><tr><td>Loan term (month)</td><td>3,517</td><td>6.37</td><td>3.02</td><td>1</td><td>12</td></tr><tr><td colspan="6">Unsuccessfully Funded Loan Listings:</td></tr><tr><td>Loan amount</td><td>2,189</td><td>3,016.8</td><td>246.8</td><td>3,000</td><td>10,000</td></tr><tr><td>Loan term (month)</td><td>2,189</td><td>6.00</td><td>2.98</td><td>3</td><td>12</td></tr></table>

Table 4. Information about Borrowers and Lenders

<table><tr><td></td><td></td><td>Frequency</td><td>Percent (%)</td><td>Frequency</td><td>Percent (%)</td></tr><tr><td></td><td>Variable</td><td colspan="2">All Borrowers</td><td colspan="2">Successful Borrowers</td></tr><tr><td>Gender:</td><td>Male</td><td>3,748</td><td>80.72</td><td>2,308</td><td>80.7</td></tr><tr><td></td><td>Female</td><td>589</td><td>12.69</td><td>379</td><td>13.25</td></tr><tr><td></td><td>Unknown</td><td>306</td><td>6.59</td><td>173</td><td>6.05</td></tr><tr><td>Age range:</td><td>20–25 (lender)22–25 (borrower)</td><td>1,625</td><td>35</td><td>693</td><td>24.23</td></tr><tr><td></td><td>26–31 (both)</td><td>1,811</td><td>39</td><td>1,259</td><td>44.02</td></tr><tr><td></td><td>32–38 (both)</td><td>873</td><td>18.80</td><td>672</td><td>23.5</td></tr><tr><td></td><td>more than 39 (both)</td><td>331</td><td>7.13</td><td>234</td><td>8.18</td></tr><tr><td></td><td>Unknown (both)</td><td>3</td><td>0.06</td><td>2</td><td>0.07</td></tr><tr><td></td><td></td><td colspan="2">All Lenders</td><td colspan="2">Successful Lenders</td></tr><tr><td>Gender:</td><td>Male</td><td>5,924</td><td>68.92</td><td>5,916</td><td>69.93</td></tr><tr><td></td><td>Female</td><td>1,565</td><td>18.47</td><td>1,563</td><td>18.48</td></tr><tr><td></td><td>Unknown</td><td>983</td><td>11.60</td><td>981</td><td>11.60</td></tr><tr><td>Age range:</td><td>20–25 (lender)22–25 (borrower)</td><td>1,354</td><td>15.98</td><td>1,350</td><td>15.96</td></tr><tr><td></td><td>26–31 (both)</td><td>3,210</td><td>37.86</td><td>3,210</td><td>37.94</td></tr><tr><td></td><td>32–38 (both)</td><td>2,436</td><td>28.75</td><td>2,421</td><td>28.62</td></tr><tr><td></td><td>more than 39 (both)</td><td>1,089</td><td>12.77</td><td>1,081</td><td>12.78</td></tr><tr><td></td><td>Unknown (both)</td><td>398</td><td>4.64</td><td>398</td><td>4.70</td></tr></table>

Table 5 shows the transaction records of both the lenders and borrowers, and it indicates that borrowers who posted successful listings had more successful transaction records than the average. Although these borrowers also had more unsuccessful transaction records, this did not negatively affect their credit scores. Figure 3 and Figure 4 depict the kernel density estimation of the lending amount and interval, respectively. We deduced that most lenders lent a small amount, that is, an amount less than RMB 500 (USD 78). The average lending amount in our sample was RMB 184 (or USD 29), much lower than Prosper.com’s average lending amount of USD 86, which was documented by Zhang and Liu [109]. Moreover, most lenders

Table 5. Records of Successful Borrowers and Lenders

<table><tr><td>Variable</td><td>Obs</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td><td>Obs</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td colspan="6">All Borrowers</td><td colspan="5">Successful Borrowers</td></tr><tr><td># Successful</td><td>4643</td><td>1.65</td><td>4.11</td><td>0</td><td>51</td><td>2860</td><td>2.68</td><td>4.96</td><td>0</td><td>51</td></tr><tr><td># Unsuccessful</td><td>4643</td><td>1.10</td><td>2.03</td><td>0</td><td>26</td><td>2860</td><td>1.65</td><td>2.37</td><td>0</td><td>26</td></tr><tr><td>Borrower CS</td><td>4643</td><td>38.49</td><td>19.71</td><td>0</td><td>141</td><td>2860</td><td>50.10</td><td>22.37</td><td>0</td><td>141</td></tr><tr><td></td><td colspan="5">All lenders</td><td colspan="5">Successful Lenders</td></tr><tr><td>Borrower CS</td><td>8472</td><td>27.33</td><td>17.88</td><td>0</td><td>140</td><td>8460</td><td>27.34</td><td>17.89</td><td>0</td><td>139</td></tr><tr><td>Lender CS</td><td>8472</td><td>682.5</td><td>2682.2</td><td>0</td><td>106185</td><td>8460</td><td>681.98</td><td>2658.59</td><td>0</td><td>101545</td></tr></table>

Figure 3. Kernel Distribution Estimation of Individual Loan Amount

![](/api/attachments/8VBX6J3R/fulltext/images/f4597f8aa61c247163463ba488171003e11b2b19a7dc4007669d9491edced2ca.jpg)

Figure 4. Kernel Distribution Estimation of the Loan Decision-Making Interval  
![](/api/attachments/8VBX6J3R/fulltext/images/514d410a2760953d6944005f49598effe4d4c4787da2557abbda9746b355996f.jpg)

followed proceeding lending closely, because the average lending interval was six minutes, which suggested the presence of a longitudinal correlation among lender decisions.

Results of Hypothesis Testing

## Herding and Lending Amount

Table 6 presents the estimation results of the FGLS regression of lending amount. Column (1) presents the basic model specification with the irrational herding effect only. The coefficient of log(cumulative amount) measured the irrational herding effect and was positive and significant (0.161), suggesting that irrational herding played a role in determining a lender’s lending amount. Because the cumulative amounts could be attributed to many small contributions, we also controlled the number of lending in the regression, and its coefficient (-0.732) was negative and significant, implying that when the same cumulative amount was contributed by many lenders, the average lending amount was low, and the followers would not only herd on the cumulative amount but also herd on the predecessors’ decisions on average amount, meaning that they would lend less. The coefficients of the other control variables were intuitive. The positive coefficient of BBC (0.00127) revealed that lenders placed their trust in the credit record provided by PPDai: lenders were more likely to invest more in the loan listings proposed by borrowers with a good credit history. The negative coefficient of PN (percent needed for materialization) (-.214) indicated that listings with a lower risk of materialization would also attract lending with higher amounts. The loan size (0.179) was also positively correlated with the lending amount, because larger loan listings could accommodate more individual lending on average.

Table 6. Results of OLS Estimation of Loan Lending Amount $( n = 1 3 , 4 8 7 1 )$

<table><tr><td></td><td>(1) lending_amount</td><td>(2) lending_amount</td><td>(3) lending_amount</td><td>(4) lending_amount</td></tr><tr><td>BBC</td><td>0.00127***(12.26)</td><td>0.00134***(12.99)</td><td></td><td></td></tr><tr><td>log(CA)</td><td>0.161***(33.98)</td><td>0.131***(27.42)</td><td>0.482***(58.43)</td><td>0.404***(45.23)</td></tr><tr><td>Loan size</td><td>0.179***(33.49)</td><td>0.132***(23.95)</td><td></td><td></td></tr><tr><td>PN</td><td>-0.214***(-12.60)</td><td>-0.211***(-12.44)</td><td>2.327***(35.23)</td><td>1.943***(28.98)</td></tr><tr><td>Loan (NO)</td><td>-0.732***(-71.95)</td><td>-0.682***(-66.46)</td><td>-1.003***(-69.13)</td><td>-0.909***(-60.26)</td></tr><tr><td>PL</td><td></td><td>0.256***(33.14)</td><td>0.105***(7.11)</td><td>-0.0332(-1.32)</td></tr><tr><td>CA X PN</td><td></td><td></td><td>-0.267***(-32.41)</td><td>-0.224***(-26.88)</td></tr><tr><td>PL X PN</td><td></td><td></td><td>0.230***(9.60)</td><td>0.0965***(4.02)</td></tr><tr><td>LLC X PL</td><td></td><td></td><td></td><td>0.0509***(20.25)</td></tr><tr><td>BBC X PL</td><td></td><td></td><td></td><td>-0.00267***(-0.94)</td></tr><tr><td>LLC X CA</td><td></td><td></td><td></td><td>0.00279***(13.79)</td></tr><tr><td>BBC X CA</td><td></td><td></td><td></td><td>0.000208***(10.61)</td></tr><tr><td>Constant</td><td>2.024***(55.47)</td><td>2.593***(64.52)</td><td>0.815***(11.21)</td><td>1.275***(17.11)</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.120</td><td>0.127</td><td>0.130</td><td>0.150</td></tr></table>

t-statistics are in parentheses; $^ { * } = p < 0 . 0 5 ;$ \*\* $p < 0 . 0 1$ \*\*\* $p < 0 . 0 0 1$ . BBC = borrower borrowing credits; CA = cumulative amount; Loan (NO) = loan number of offers; PN = percent needed for materialization; $\mathrm { P L } = \mathrm { p r o m i n e n t }$ lender; LLC = lender lending credits; prominent lenders are the lenders with lending credits over the 90th percentile cutoff value in the credit distribution.

Column (2) presents the results from a model specification with a binary variable indicating the participation of prominent lenders. The coefficient of prominent-lender participation (0.256) was positive and significant, which suggested that rational herding behavior existed. This supported the second part of H1 (the first part will be discussed in §5.2.2). Our results indicated that the lending amount would increase by around 25.6% on average once the prominent lenders signaled their trust in the borrower by offering their lending. The other results were similar to those in column (1).

Column (3) merges the two listing features, loan size and borrower credit, into the listing fixed effects to focus our analysis on the interaction between listing features and herding effects. We added the interactions <sub>??</sub> <sub>×</sub> <sub>????</sub> and <sub>??</sub> <sub>×</sub> <sub>????</sub> to the regression. Because higher CA (+) and lower PN (-) together indicated that the risk of materialization was lower, the negative coefficient of <sub>??</sub> <sub>×</sub> <sub>????</sub> (-0.267) suggested that lenders preferred to provide loans for listings with lower risk, ceteris paribus. However, when a PL provided a loan for a listing in its earlier, riskier stage—when PN was large (or higher to-be funded amount)—rational herding lenders saw this as a positive signal that the PL was confident and had better knowledge of the listing, and they thus provided loans for the listing (i.e., engaged in rational herding), explaining the positive coefficient of <sub>??</sub> <sub>×</sub> <sub>????</sub> (0.230), ceteris paribus. The coefficients of all the other variables except PN remained in the same direction. Without the loan size in the regression, PN may also have indicated the loan size, because the same cumulative amount may have accounted for the lower percentage obtained when the loan size was larger. This confounding effect changed the coefficient of the percentage needed for a listing to materialize.

Finally, column (4) incorporates the interactions between borrowers’ borrowing credit and herding effects and the interactions between lenders’ lending credit and herding effects into the regression. The coefficients of the interactions between borrowers’ borrowing credit and herding effects (BBC X PL) were negative and significant. This suggests that when a loan with lower borrower credits (i.e., riskier loan) receives lending from a prominent lender (i.e., positive signal), the rational herding effect will be greater, which supports our proposed hypothesis concerning the attenuation effect of listing features on rational herding (H2). Our findings echo those of Jiang et al. [48], who found that the risk-related attributes of a loan listing could moderate the herding effects, and contribute evidence of the moderation effects of platform-supplied listing attributes on rational herding to the literature.

The results also demonstrated the effect of lenders’ lending experience on herding. Specifically, the regression shows a significant and positive coefficient of LLC X PL. This suggests that as lenders gained experience through lender credit, herding played a more pivotal role in determining their lending amounts. These results supported our assumption that lenders would undertake more observational learning for herding when their experience increased. This supported H3.

## Drivers of Rational Herding

To analyze the behavioral mechanisms behind rational herding, we replaced lenders’ lending credit with its two components—lending with successful repayment and lending on materialized listings—which contributed the most to lenders’ lending credit, in the regression. Table 7 reports the estimation results. Because the estimation results for the variables presented in Table 6 maintained the same sign and a similar magnitude, we explain only the results for the new variables. The results shown in column 1 suggested that rational herding was rooted in lending on materialized listings rather than lending with successful repayment, supporting myopic loss aversion theory and H4a. The coefficients of all the variables with lending with successful repayment, presented in column 2, were nonsignificant, suggesting that lending with successful repayment had no significant effect on lending amount and was thus not a factor leading to rational herding; we therefore rejected H4b. The coefficients of the interactions between lending on materialized listings and listing features or lender experience were significant and had the same sign as the interaction terms with prominent lender reported in Table 7. The myopic loss aversion theory may explain the results, because if the listings failed to materialize, any lending costs, including the opportunity cost of time, would be lost. It appears lenders were more sensitive to this immediate loss than to the more distant loss caused by a bad loan. If true, CML (measuring lenders’ ability to achieve higher expected returns); would have been discounted because lenders myopically discounted future returns.

## The Rationality of Rational Herding

We used loan performance data to replicate the rationality of rational herding (H1) shown by Zhang and Liu [109] using Prosper.com data. We first summarized the performance of the loan listings and tested the difference in default rates and final returns between prominent- and novice-lender loans. Figure 5 depicts the default rate of the loans by lender type, which is the ratio of the defaulted loan amount to the total loan amount. Figure 5 shows that the total loans made by prominent lenders had a lower default rate than those made by novice lenders. Figure 6 illustrates the return rates of the loans by lender type. These graphs summarize the returns from all the loans, including loan defaults.

Table 7. Results for Regression with Decomposed Lenders’ Lending Credit $( n = 1 3 , 4 8 7 0 )$

<table><tr><td></td><td>(1) lending_amount</td><td>(2) lending_amount</td></tr><tr><td>BBC</td><td>0.00132***(12.78)</td><td></td></tr><tr><td>log(CA)</td><td>0.133***(27.77)</td><td>0.406***(45.78)</td></tr><tr><td>Loan size</td><td>0.134***(24.31)</td><td></td></tr><tr><td>PN</td><td>-0.210***(-12.39)</td><td>1.956***(29.31)</td></tr><tr><td>Loan (NO)</td><td>-0.684***(-66.77)</td><td>-0.912***(-60.77)</td></tr><tr><td>CSR</td><td>-0.0175(-0.72)</td><td>0.0475(0.55)</td></tr><tr><td>CML</td><td>0.0310***(17.04)</td><td>-0.00541(-0.82)</td></tr><tr><td>CA X PN</td><td></td><td>-0.225***(-27.17)</td></tr><tr><td>CML X PN</td><td></td><td>0.0209**(3.18)</td></tr><tr><td>CSR X PN</td><td></td><td>-0.133(-1.53)</td></tr><tr><td>LLC X CSR</td><td></td><td>0.00124(0.12)</td></tr><tr><td>LLC X CML</td><td></td><td>0.00572***(7.30)</td></tr><tr><td>BBC X CSR</td><td></td><td>-0.00109(-1.17)</td></tr><tr><td>BBC X CML</td><td></td><td>-0.000258***(-3.51)</td></tr><tr><td>LLC X CA</td><td></td><td>0.00299***(14.88)</td></tr><tr><td>BBC X CA</td><td></td><td>0.000212***(10.91)</td></tr><tr><td>Constant</td><td>2.574***(64.07)</td><td>1.256***(16.94)</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.127</td><td>0.152</td></tr></table>

Notes: BBC = borrower borrowing credits; CA = cumulative amount; PN = percent needed for materialization; Loan (NO) = loan number of offers; PL = prominent lender; LLC = lender lending credits; CML = count materialized listings lending; $\mathrm { C S R } = \mathrm { c o u n t }$ successful repayment leading; t-statistics are in parentheses; $^ { * } = p < 0 . 0 5 ; ^ { * * } p < 0 . 0 1$ \*\*\* $p < 0 . 0 0 1$ . Prominent lender is defined as the lenders with lending credits over the 90th percentile cutoff value in the credit distribution.

Figure 5. Default Rate of Total Loans by Lender Type  
![](/api/attachments/8VBX6J3R/fulltext/images/56fe85e0218562dcfbffd1c79a3cf75b2dedf4570b239b2bb7124d3f43a91666.jpg)

Figure 6. Return Rates of Loans by Lender Type  
![](/api/attachments/8VBX6J3R/fulltext/images/69f9a4178286d02d975dba9b517ddc2ec06317c9553069d1cfb5009552d6bb12.jpg)

In contrast to our expectation, the return rates of prominent-lender loans were lower than those of novice-lender loans. Because the return rates were observable when lenders made their decisions, these summary statistics suggested that prominent lenders usually made more prudent decisions and invested in loans with reasonable returns, whereas novice lenders chased high-return loans without considering the potential risks. Considering the potential default risks, we calculated the expected return rates, which were defined as the ratio of actual returns to the total loans, including the defaulted loans. Figure 7 presents the actual return rates by lender type; this graph shows the error bars of actual returns with a 90% confidence interval by lender type, and it indicates that the eventual returns of the microloan projects in which prominent lenders invested were higher than those in which novice lenders invested. Therefore, the expertise of prominent lenders was characterized by their discretion regarding potential risks and their ability to maximize the expected returns while considering such risks, supporting the first part of H1. We thus refined our definition of rational herding as follows: herding on lenders who exercised discretion regarding potential risks and had the ability to acquire higher expected returns while considering such risks.

Figure 7. Actual Return Rates on Loans by Risk-neutral Lender Type  
![](/api/attachments/8VBX6J3R/fulltext/images/1c73b4117b7ab69a61eec44bcedb4bdae97f5ab4ed80934be66a61cb2454a89c.jpg)

Considering the possibility that confounding factors (e.g., a loan’s term) could moderate the difference in both default rates and expected returns between prominent- and novice-lender loans, we ran a logit model on default rates and a linear regression on effective interest rates, controlling the potential confounding factors. The effective interest rates were defined as the actual return rates on a loan. For fully paid loans, it was the interest rate offered by the borrower; however, for defaulted loans, it was -100%, because the lenders could not recover their principal. Both regressions accounted for lender loan amounts and used them as weights. Table 8 presents the results of this analysis.

Table 8. Results for the Analysis of the Rationality of Herding on Prominent Lenders $( n = 3 1 , 0 2 1 , 7 1 4 )$

<table><tr><td></td><td>(1) default</td><td>(2) effective interest</td></tr><tr><td>herding_sig</td><td>-0.295***(-81.76)</td><td>0.0934***(7.92)</td></tr><tr><td>period</td><td>0.190***(616.10)</td><td>-0.856***(-651.28)</td></tr><tr><td>interest</td><td>0.118***(232.25)</td><td></td></tr><tr><td>log(BBC)</td><td>-0.134***(-89.02)</td><td></td></tr><tr><td>Constant</td><td>-6.525***(-509.08)</td><td>20.45***(2059.84)</td></tr><tr><td>AIC</td><td>8766592.6</td><td></td></tr><tr><td>Adjusted  $R^2$ </td><td></td><td>0.013</td></tr></table>

Note: BBC = borrower borrowing credits; t statistics in parentheses; $^ { \ast } p < 0 . 0 5 , ^ { \ast \ast } p < 0 . 0 1 , ^ { \ast \ast \ast } p < 0 . 0 0 1$

Our results showed that the rates of loan defaults were lower for prominent lenders than for novice lenders. Because our analysis used lenders’ lending amounts as weights, these results demonstrated that prominent lenders were more likely to avoid defaulted loans or to invest small amounts in them. The results of the interest rate analysis also suggested that prominent lenders could usually achieve higher returns than novice lenders, although the difference in return rates was marginal. The results for the other covariates in both regressions were also intuitive: loans with higher offered interest and longer terms were more likely to be defaulted on, because it was more difficult for borrowers to fully repay such loans. Borrowers with more credit were less likely to default. The only counterintuitive result involved the coefficient of loan term in the regression of effective interest rates. The negative coefficients implied that loans with longer terms had lower effective returns—seemingly contradicting a normal interest rate scheme. This was the case because this regression was for an analysis of effective interest rates considering defaults. Because the default rate was higher for long-term loans, we had reason to conclude that the effective return was lower for long-term loans. The regression results echoed the results depicted in Figure 5, Figure 6, and Figure 7, providing evidence of herding that was rational and thus reflected observational learning.

## Robustness Checks

The key variable in our analysis was PL, and its measurement depended on the cutoff point used to distinguish prominent from novice lenders; this choice had the potential to change our empirical results. To test the robustness of our analysis, we chose different cutoffs of percentiles in the distribution of lender credits and checked whether our results were sensitive to different definitions of PL. Table 9 and Table 10 in Appendix B detail the results based on 95% and 75% cutoff points, respectively. These checks indicated that the major results remained the same and thus that our findings and conclusions were robust.

It may be possible to measure the influence of prominent lenders by incorporating the information on the number of prominent lenders, because the ratio of prominent lenders to total lenders may also play a key role in determining the materialization of a loan list. Thus, we explored a new variable to capture the possible influence of the number of prominent lenders: We used the number of PL/number of cumulative lenders up to the focal lender as the measure of the fraction of PL among all lenders prior to the focal lender, which we termed, FPL. We ran a regression of both lending amounts, and the results are reported in Table 11. The results remained virtually the same, providing further evidence of the robustness of our conclusions.

## Simulation to Demonstrate the Influence of Rational Herding

Next, we conducted a large simulation to demonstrate the influence of rational herding based on the score system set up by PPDai. To determine the magnitude of the influence of rational herding, we examined what would happen if all the lenders could observe the behavior of the prominent lenders and compared the quantified gain/loss of this simulated result with the actual results. To do $\mathbf { s o } ,$ we adopted the proportional hazard model proposed by Cox [21] to examine the effect of observed covariates on lenders’ decisionmaking duration. The conditional hazard is given by

$$
\lambda (t; x) = \lim _ {h \rightarrow 0} \frac {P (t \leq T <   t + h \mid T \geq t , x)}{h}
$$

where <sub>??</sub> is a vector of explanatory variables. Intuitively, this hazard rate is the probability that some lenders will invest in a loan project after duration <sub>??</sub>, given that they wait at least until <sub>??</sub>. Assuming that individual hazard functions are proportional to some common baseline hazard $\lambda _ { 0 } ( t )$ , the proportional hazard model is as follows:

$$
\lambda (t; x) = \kappa (x) \lambda_ {0} (t),
$$

where $\kappa ( x )$ is a nonnegative function of <sub>??</sub>. Typically, this function is parameterized as $\kappa ( x ) = e x p ( x \beta )$ , where $\beta$ is a vector of parameters that measures the semielasticity of hazard with respect to <sub>??</sub>. Cox [21] suggested a partial likelihood method for estimating the parameters in the proportional hazard model without specifying the baseline hazard. Specifically, the probability that an individual <sub>??</sub>, out of a set of lenders $S _ { k }$ who will exit at time $T _ { k }$ (or who have survived the first $T _ { k }$ periods) is

$$
P r o b [ t _ {i} = T _ {k} | i \in S _ {k} ] = \frac {\exp (\beta x _ {i})}{\sum_ {j \in S _ {k}} \exp (\beta x _ {j})}.\tag{2}
$$

Equation (1) shows that the baseline hazard rate does not affect the probability of defection. Thus, the partial likelihood of observing the existence of $M _ { k }$ lenders over <sub>??</sub> periods is as follows:

$$
l n L = \sum_ {k = 1} ^ {K} \sum_ {i = 1} ^ {M _ {k}} [ \beta x _ {k} - l n \sum_ {j \in S _ {k}} e x p (\beta x _ {j}) ].\tag{3}
$$

Cox’s partial likelihood maximization estimator should maximize the equation [21].

Figure 8 shows the Kaplan–Meier survival estimates for all loan listings with a prominent lender and all listings with no prominent lender (i.e., only novice lenders). The variable project\_sig was set to “1” if there is prominent lender in the loan listing and set to “0” otherwise. Figure 8 shows that the loan listings with prominent lenders were more likely to “exit” due to rational herding. The results of the Cox hazard estimation results were consistent with the previous findings. Using the Cox hazard estimation, we conducted simulations to quantify the possible loss or gain in the presence of rational herding based on PPDai’s score system, following the literature [22, 62]. In the simulations, we assumed lenders could not distinguish the prominent lenders and follow their loans (i.e., no rational herding). To do so, we substituted all the estimated baseline hazards and all the estimated parameters in Equation (3) and assigned zeros to the variable project\_sig (even if there were prominent lenders), and we computed the new survival function from the following standard Cox hazard model expression:

$$
\hat {S} (t; X) = \prod_ {i | t _ {i} <   t} \widehat {\alpha} _ {i} ^ {\exp (\widehat {\beta} X)}
$$

where $\widehat { \alpha _ { \iota } }$ is one minus the estimated baseline hazard for exit time i, and $\hat { \beta }$ is the vector of coefficients estimated with the Cox hazard model in Equation (3).<sup>13</sup> After we obtained the new survival functions, we computed the new total amount of successful loans. We conducted simulations one million times and obtained a distribution of the simulated total amount of loans. Figure 9 shows the distribution of the total successful loan amount for one million simulations. In our sample, the total amount of successful loans was RMB 8,904,556 (about USD 1.3 million). The median value of the simulated successful loan value decreased to RMB 4,728,524 (about USD 0.7 million). The simulation results suggests that without rational herding, many successful loans might have been unsuccessful and the total amount of successful loans would have decreased by around 46%. Rational herding thus had a highly consequential effect on the results.

Figure 8. Comparison of the Loan Listing Survival Probability between Prominent and Novice Lenders  
![](/api/attachments/8VBX6J3R/fulltext/images/69648a274a82c470c8926c86827d1f41f4469af144ea22e35c671490cfbdeb2a.jpg)

Figure 9. Distribution of the Values of Total Successful Loan Listings over One Million Simulations  
![](/api/attachments/8VBX6J3R/fulltext/images/10d0d26f74d40905ce77624519d6a2fecfc4f0011b657f6ba96f5e9ee183ec13.jpg)

## Discussion

The P2P loan platform market has continued to grow and thrive globally, especially in the US, Europe, and Asia. This market is a compelling area of research, particularly because P2P microlending is both increasingly popular and fraught with economic challenges. In fact, although the largest market is in China, this market endured a substantial period of turmoil brought about by scams, unscrupulous operators, and irrational behavior among financially unsavvy lenders as well as information asymmetry, adverse selection, moral hazard, and irrational herding behaviors [40, 71]. As a result, between 2011 and 2018, over 84% of the Chinese P2P platforms failed [40], and approximately 700,000 small lenders lost a total of approximately RMB 120 billion (USD 18.77 billion) [71]. At the end of 2019, the Chinese government imposed much tighter regulations on this market—and although only a few of the original platforms survived this regulatory regime, the market has transformed and continued to grow. As He and Li [40] showed, the platforms that survived this period were large, were publicly listed, and implemented information-disclosure practices that reduced information asymmetry.

Our study examines the P2P loan platform PPDai, which thrived during this period of turmoil because it was known for its innovative processes and information-disclosure systems (e.g., unique credit- and vendor-rating systems). These innovations reduced information asymmetry, adverse selection, and moral hazard. To illuminate what PPDai was doing right in terms of providing signals that led to rational herding, we focus on the period directly before the platforms were forced to change their lending practices.

We analyze the factors that determined the successful funding of P2P loan listings on PPDai during this period, with a focus on the effects of herding behavior. A key factor is that borrowers often lacked established credit histories, which gives rise to questions about whether lenders can make rational decisions in such risky scenarios and how these rational decisions are affected by lenders’ lending experience and borrowers’ creditworthiness. PPDai addressed this asymmetry issue in several innovative ways, including establishing its own transparent credit- and lender-evaluation system. We develop hypotheses to investigate whether rational herding, both alone and in the context of borrower and lender characteristics, contributed to PPDai’s success.

Our analyses of microloans on PPDai confirm that when making lending decisions, novice lenders mimicked predecessor decisions. In particular, the results associated with H1 confirm the existence of rational herding behaviors and replicate the relationship Zhang and Liu [109] demonstrated using Prosper.com data: First, prominent lenders’ loans resulted in lower default rates and higher expected return rates. Second, prominent-lender participation in loans had a positive effect on novice-lender lending amount. The results related to H2 showed that a borrower’s credit can dampen rational herding, and those related to H3 verify that lenders’ lending experience had a positive moderating effect on rational herding on loan amount. The results associated with H4 enable us to attribute rational herding to lending on materialized listings instead of to lending with successful repayment, thus supporting myopic loss aversion theory.

## Contributions to Research and Theory

Our empirical analysis suggests that lender experience, borrower credit information provided by the platform, and the rational herding effect exerted by prominent lenders are key moderating factors that facilitate a lender’s decision and increase the lending amount. In particular, the herding effect plays a significant role in lender decision-making. Moreover, we further examine the influence of prominent lenders on a loan listing. This extends Simonsohn and Ariely’s [92] and Zhang and Liu’s [109] proposition that behavioral rationality interacts with lenders’ lending experience. We also test the premise that following prominent lenders is a rational herding behavior, and our findings demonstrate that prominent lenders usually invest in loans with lower default rates; thus, although the return rates of these loans are not higher than those of others, the expected return from such loans is generally higher, which suggests that lender herding behavior is rational, that is, based on observational learning. Our empirical findings confirm that rational herding plays an essential role in lender decision-making in microloan transactions.

Many studies have investigated the factors that facilitate transactions on P2P platforms in the presence of information asymmetry. The most vital of these factors is the platform’s supplying of the borrower’s credit information. However, these studies could not explain how this credit information affects herding behaviors for initial lending decisions when borrowers lack traditional credit histories, as is the case with Prosper.com’s use of Experian. This is especially problematic in China, which lacked a transparent and universal credit systems on which platforms or lenders could rely. PPDai’s unique and transparent credit system is a compelling research topic because the absence of such a system puts microloan platforms at high risk for failure caused by asymmetric information and irrational herding [65, 106].

Zhang and Liu [109] provided the first empirical analysis of the effects of herding behavior on microloan transactions. Their study used moderation effects to establish that rational herding can play a vital role in determining successful transactions on microloan platforms. Our study provides further empirical evidence concerning the rational herding effect in microloan transactions. Our study examines the interaction effects of borrower credits and lender experience on herding. Moreover, our study investigates two dimensions of listing materialization: lending on materialized listings and lending with successful repayment. Lending on materialized listings was supported, supporting myopic loss aversion theory. Although previous studies have overlooked these two dimensions, our study confirms that they can be used to reveal lender confidence in the listings and that they are drivers of rational herding.

Our study contributes to the understanding of why and how the P2P lending market differs other financial markets and how borrower and lender characteristics affect the rational herding effect. These insights can help researchers further explore the evaluation procedures and decision-making processes of lenders confronted with information asymmetry. In the PPDai context, the implications are potentially profound, because our follow-up survival simulations indicate that without rational herding, the total number of successful PPDai loans would have decreased by around 46% during the study period. This finding further underlines the crucial influence of rational herding and the unique contextual factors of PPDai that have fostered it.

## Contributions to Practice

The results of this study have key managerial implications. P2P platforms are not only changing retailing patterns but also altering loan patterns. Internet commerce is a disruptive force that will forever change retail, lending, and investing. Even though economists and finance experts did not expect P2P microloan platforms to succeed, the global P2P microloan market has become robust enough to disrupt traditional loan and investment markets.

The largest obstacle to the development of this online market is lender risk rooted in information asymmetry, adverse selection, moral hazard, and herding behaviors. The key difference between P2P microlending and bank investments for savers is that microlenders have no guarantee that their money will be repaid. Any funds they lend through a P2P website are not covered by government-backed insurance, which usually applies to savings. Thus, to support the success of this market, P2P platform managers must develop mechanisms for resolving such problems. Our empirical findings suggest that prominent lenders play significant roles in materializing loan listings. Thus, beneficial policies, such as favorable interest rates based on loan credits, may be an effective way for platform managers to promote transactions and increase profits.

Our study of P2P lending validates the critical importance of creditworthiness as a moderator of herding behavior. Unfortunately, the absence of financial institutions as intermediaries can cause a borrower’s creditworthiness to remain in doubt. Such ambiguity (i.e., increased information asymmetry) regarding creditworthiness can dampen rational herding, but it offers opportunities for lenders to seek better returns, depending on their ability to absorb the risk associated with different credit uncertainties. However, from the perspective of business operations, the uncertainty regarding borrowers’ creditworthiness should be monitored. Hence, P2P lending platforms should alleviate lenders’ loan risks by offering them more soft information on borrowers. For example, PPDai’s platform has rich qualitative information about its members, including their photos, social capital, and external online links, and PPDai is affiliated with a group of financial institutions and e-commerce platforms. PPDai could use its information architecture to disclose certain elements of this information to its members. In this scenario, lenders could use the information to improve their lending decisions.

Understanding the influence of lender experience on herding is essential to managing and designing P2P lending platforms. Herding allows lenders to draw inferences from the lending decisions they have observed. However, for novice lenders to lend effectively, there must be prominent lenders to follow. That is, early prominent lenders facilitate the fulfillment of loan listings. If early prominent lenders are nonexistent or insufficient in number, the probability of loan fulfillment deteriorates. Because distinct groups of customers have heterogeneous rational herding behaviors, a given platform can customize its information disclosure accordingly. Hence, P2P platform managers and designers should develop strategies for building up early lending by prominent lenders as a precondition of herding. For example, P2P operators could consider launching promotional strategies that encourage prominent lenders to lend in the initial stages of loan listings. Such strategies could include incentives like points, lower service costs, or even official titles for specific services offered. This strategy is analogous to that of organizing members into groups to inspire social networking. Another potentially useful strategy could be for platforms to highlight listings on which some prominent lenders have decided to invest as an aid to novice investors, while directing the listings proposed by borrowers with sound credit history to prominent lenders.

## Limitations and Future Research

In line with prior research, we examine the influence of herding behavior without fully identifying the reasons for herding. One such reason is that herding serves as the signal effect of prominent-lender choices. Although our study has a strong theoretical and empirical foundation, further research needs to be conducted to better distinguish rational from irrational herding. This will require a stronger experimental

examination of underlying causal mechanisms.

Additional analytical methodologies could be used to extend our study. For instance, researchers could examine survey data on consumer beliefs regarding borrower credit and novice-lender beliefs regarding prominent-lender choices. Such data could serve as the basis for psychological explanations of herding behavior that are grounded in psychometric measures. This area is ripe for consumer behavior research conducted from diverse perspectives, such as information systems, economics, marketing, and human– computer interaction.

Our study is limited to the investigation of one highly successful P2P microloan platform in China. Thus, our results may not generalize to different kinds of P2P microloan platforms or to different legal or consumer cultures. Cross-cultural research on systems use—for example, research that compares the systems use of Chinese and US participants—has shown that nation- and individual-level cultural factors can affect trust perceptions and decision-making [72, 73, 108]. Trust perceptions are important in P2P platform use and can vary greatly depending on cultural factors, legal protections, and the degree of trust in institutions and even the platform technology itself.

We believe it is important to further examine the possibility of rational herding and observational learning in other online-commerce contexts and platforms. This is especially promising in e-commerce settings that involve large social networks with key information cues, such as the effects of online reviews and recommendations on platforms [59, 96], and with general recommender systems [e.g., 64]. Moreover, rational herding and observational learning could be investigated in many other types of online crowdfunding markets [19, 23, 69]. It would also be useful to examine how rational herding and observational learning influence backers’ behaviors in the related but distinct online-platform markets of crowdfunding and crowdsourcing, which do not require loan repayment but use various schemes to provide rewards for backers [cf. 14, 63, 98]. Herding behaviors have been observed in other technology contexts, including software adoption, where it has been linked to information cascades [25, 110], an informationbased concept that explains “herd behavior that occurs when individuals who face a certain decision choose to follow the actions of others instead of making a decision based on their own private information” [98, p.

844], which can also be understood as a popularity effect [99] (see also [10, 11]). It would be particularly

intriguing to consider software adoption in terms of whether such behavior is rational and based on

observational learning, helping vendors understand how to best meet market needs and increase adoption.

Moreover, we assume that the P2P signals in question arise primarily from lending activity (and thus

involve observational learning), not from electronic word-of-mouth [cf. 1]. However, the latter is a

compelling source of direct learning that should be further considered in a P2P context. Electronic word-

of-mouth is “communication in an online context and can be described as a statement by potential, actual,

or former customers about a product or company” [98, p. 844]. Such information could also help lenders

decide whether to provide loans for a potential borrower, because in a crowdsourcing context, electronic

word-of-mouth has been shown to be linked to information cascades, another form of herding behavior [98].

Of course, the broader issue of lack of information disclosure between parties (and how to resolve it)

continues to vex most online markets [39] and fosters information asymmetry.

Finally, in contrast to the loans facilitated by the many P2P loan platforms that went bankrupt in China,

PPDai loans have had a low default rate. This is notable because although China’s legal system is

undergoing dramatic reforms, its rule of law remains less formalized than that of Western countries. Legal

experts believe this lack of legal formality contributes to moral hazard because it is more difficult to sue in

court to collect on a loan [78, 82, 100]. Yet, PPDai has an astounding collection rate of 85%, providing a

more cost-effective means of collection than going through any court in any country. PPDai (and other

successful Chinese platforms) skips the courts and successfully pursues its own “micro rule of law”; as a

result, it can operate without an unusually high burden of moral hazard. This is a promising phenomenon

for future study and policy development, because the dramatic potential of microloans rests largely in the

developing world, where the rule of law is fraught with challenges. Thus, a pressing need exists for research

on how PPDai has been able to create such effective mechanisms of trust and of the micro rule of law.

## Conclusion

In this paper, we make three key contributions to the literature: (1) we use heterogeneous herding effects to

empirically determine whether lenders’ herding behavior on PPDai is rational based on observational learning; (2) we investigate the moderating effect of borrower credit and novice-lender experience on herding, and we leverage this heterogeneity in lender experience to better explain loan results; and (3) because PPDai publicly provides potential lenders with a transparent credit score—in contrast to platforms like Prosper.com, which leverage hidden proprietary credit information from Experian—we further analyze the credit composition of prominent lenders to better understand the crucial determinants of rational herding. Crucially, our follow-up survival simulations indicate that without rational herding, the total number of successful PPDai loans would have decreased by around 46% during the study period—a finding that further underlines the crucial influence of rational herding and the unique contextual factors of PPDai that have fostered it. These important findings has the potential to generate several streams of research noted in our paper.

## References

1. Aggarwal, R; Gopal, R; Gupta, A; and Singh, H. Putting money where the mouths are: The relation between venture financing and electronic word-of-mouth. Information Systems Research, 23, 3-part-2 (2012), 976-992.

2. Agrawal, A; Catalini, C; and Goldfarb, A. Some simple economics of crowdfunding. Innovation Policy and the Economy, 14, (2014), 63-97.

3. Avery, CN and Chevalier, JA. Herding over the career. Economics Letters, 63, 3 (1999), 327-333.

4. Bachmann, A; Becker, A; Buerckner, D; Hilker, M; Kock, F; Lehmann, M; Tiburtius, P; and Funk, B. Online peer-to-peer lending -- A literature review. Journal of Internet Banking and Commerce, 16, 2 (2011), 1-18.

5. Baddeley, MC. Behind the black box: A survey of real-world investment appraisal approaches. Empirica, 33, 5 (2006), 329-350.

6. Banerjee, AV. A simple model of herd behavior. Quarterly Journal of Economics, 107, 3 (1992), 797-817.

7. Belavina, E; Marinesi, S; and Tsoukalas, G. Rethinking crowdfunding platform design: Mechanisms to deter misconduct and improve efficiency. Management Science, 66, 11 (2020), 4980-4997.

8. Benartzi, S and Thaler, RH. Myopic loss aversion and the equity premium puzzle. Quarterly Journal of Economics, 110, 1 (1995), 73–92.

9. Berkovich, E. Search and herding effects in peer-to-peer lending: Evidence from Prosper. com. Annals of Finance, 7, 3 (2011), 389-405.

10. Bikhchandani, S; Hirshleifer, D; and Welch, I. A theory of fads, fashion, custom, and cultural change as informational cascades. Journal of Political Economy, 100, 5 (1992), 992-1026.

11. Bikhchandani, S; Hirshleifer, D; and Welch, I. Learning from the behavior of others: Conformity, fads, and informational cascades. Journal of Economic Perspectives, 12, 3 (1998), 151-170.

12. Boss, D. On supporting the maximization postulate. Journal of Behavioral Economics, 15, 4 (1986), 35-39.

13. Brand Essence. Peer To Peer (P2P) lending market size, share, and trends analysis report by business model (alternate marketplace lending, traditional lending), by application (individuals, businesses), by end-users (consumer credit loans, small business loans, student loans, real estate loans), based on region, and segment forecasts, 2022-2028. Report ID: BMRC 545, (2022), Date last

accessed: April 15, 2022,

14. Burtch, G; Hong, Y; and Liu, D. The role of provision points in online crowdfunding. Journal of Management Information Systems, 35, 1 (2018), 117-144.

15. Caldwell, BJ. The neoclassical maximization hypothesis: Comment. American Economic Review, 73, 4 (1983), 824-827.

16. CCRC. Credit reference center: The People's Bank of China. (2017), Date last accessed: December 20, 2017, http://www.pbccrc.org.cn/crc/zxgk/index\_list\_list.shtml

17. Chakraborty, S and Swinney, R. Signaling to the crowd: Private quality information and rewardsbased crowdfunding. Manufacturing & Service Operations Management, 23, 1 (2021), 155-169.

18. Chen, G; Kim, KA; Nofsinger, JR; and Rui, OM. Trading performance, disposition effect, overconfidence, representativeness bias, and experience of emerging market investors. Journal of Behavioral Decision Making, 20, 4 (2007), 425-451.

19. Chen, J; Feng, J; and Whinston, AB. Keyword auctions, unit-price contracts, and the role of commitment. Production and Operations Management, 19, 3 (2010), 305-321.

20. Chevalier, J and Ellison, G. Career concerns of mutual fund managers. Quarterly Journal of Economics, 114, 2 (1999), 389-432.

21. Cox, DR. Regression models and life tables (with discussion). Journal of the Royal Statistical Society, 34, 1972 (1972), 187-220.

22. Cox, DR and Oates, D. Analysis of Survival Data. New York: Chapman and Hall, 1984.

23. Cui, X; Zhang, N; and Lowry, PB. The agent bidding habit and use model (ABHUM) and its validation in the Taobao online auction context. Information & Management, 54, 3 (2017), 281-289.

24. Deval, H; Mantel, SP; Kardes, FR; and Posavac, SS. How naïve theories drive opposing inferences from the same information. Journal of Consumer Research, 39, 6 (2012), 1185-1201.

25. Duan, W; Gu, B; and Whinston, AB. Informational cascades and software Adoption on the internet: An empirical investigation. MIS Quarterly, 33, 1 (2009), 23-48.

26. Easley, RF; Wood, CA; and Barkataki, S. Bidding patterns, experience, and avoiding the winner’s curse in online auctions. Journal of Management Information Systems, 27, 3 (2010), 241-268.

27. Emekter, R; Tu, Y; Jirasakuldech, B; and Lu, M. Evaluating credit risk and loan performance in online Peer-to-Peer (P2P) lending. Applied Economics, 47, 1 (2015), 54-70.

28. Fatehi, S and Wagner, MR. Crowdfunding via revenue-sharing contracts. Manufacturing & Service Operations Management, 21, 4 (2019), 875-893.

29. Freedman, S and Jin, GZ. The information value of online social networks: Lessons from peer-topeer lending. International Journal of Industrial Organization, 51, March (2017), 185-222.

30. Gaeth, GJ and Shanteau, J. Reducing the influence of irrelevant information on experienced decision makers. Organizational Behavior and Human Performance, 33, 2 (1984), 263-282.

31. Galak, J; Small, D; and Stephen, AT. Microfinance decision making: A field study of prosocial lending. Journal of Marketing Research, 48, SPL (2011), S130-S137.

32. Ge, R; Feng, J; Gu, B; and Zhang, P. Predicting and deterring default with social media information in peer-to-peer lending. Journal of Management Information Systems, 34, 2 (2017), 401-424.

33. Gelatt, H. Positive uncertainty: A new decision-making framework for counseling. Journal of Counseling Psychology, 36, 2 (1989), 252-256.

34. Glaser, M and Weber, M. Why inexperienced investors do not learn: They do not know their past portfolio performance. Finance Research Letters, 4, 4 (2007), 203-216.

35. Gordon, DF. A neo‐classical theory of Keynesian unemployment. Economic Inquiry, 12, 4 (1974), 431-459.

36. Gregg, DG and Scott, JE. The role of reputation systems in reducing on-line auction fraud. International Journal of Electronic Commerce, 10, 3 (2006), 95-120.

37. Guo, Y; Zhou, W; Luo, C; Liu, C; and Xiong, H. Instance-based credit risk assessment for investment decisions in P2P lending. European Journal of Operational Research, 249, 2 (2016), 417-426.

38. Haigh, MS and List, JA. Do professional traders exhibit myopic loss aversion? An experimental

analysis. Journal of Finance, 60, 1 (2005), 523-534.

39. Hao, L and Tan, Y. Who wants consumers to be informed? Facilitating information disclosure in a distribution channel. Information Systems Research, 30, 1 (2019), 34-49.

40. He, Q and Li, X. The failure of Chinese peer-to-peer lending platforms: Finance and politics. Journal of Corporate Finance, 66, February (2021), Article: 101852.

41. Herzenstein, M; Dholakia, UM; and Andrews, RL. Strategic herding behavior in peer-to-peer loan auctions. Journal of Interactive Marketing, 25, 1 (2011), 27-36.

42. Holm, C and Rikhardsson, P. Experienced and novice investors: does environmental information influence investment allocation decisions? European Accounting Review, 17, 3 (2008), 537-557.

43. Hong, H; Kubik, JD; and Solomon, A. Security analysts' career concerns and herding of earnings forecasts. Rand Journal of Economics, 31, 1 (2000), 121-144.

44. Hsini, M. Noise, uncertainty and investor psychology: A behavioral analysis. International Business Research, 8, 7 (2015), 1-15.

45. Hu, M; Li, X; and Shi, M. Product and pricing decisions in crowdfunding. Marketing Science, 34, 3 (2015), 331-345.

46. Jiang, Y; Ho, Y-C; Yan, X; and Tan, Y. Investor platform choice: Herding, platform attributes, and regulations. Journal of Management Information Systems, 35, 1 (2018), 86-116.

47. Jiang, Y; Ho, Y-C; Yan, X; and Tan, Y. When online lending meets real estate: Examining investment decisions in lending-based real estate crowdfunding. Information Systems Research, 31, 3 (2020), 715-730.

48. Jiang, Y; Ho, Y-C; Yan, X; and Tan, Y. What’s in a 'username'? The effect of perceived anonymity on herding in crowdfunding. Information Systems Research, 33, 1 (2022), 1-17.

49. Kagel, J. Cross-game learning: Experimental evidence from first-price and English common value auctions. Economics Letters, 49, 2 (1995), 163-170.

50. Kagel, JH and Richard, J-F. Super-experienced bidders in first-price common-value auctions: Rules of thumb, Nash equilibrium bidding, and the winner’s curse. Review of Economics and Statistics, 83, 3 (2001), 408-419.

51. Kahneman, D and Thaler, RH. Anomalies: Utility maximization and experienced utility. Journal of Economic Perspectives, 20, 1 (2006), 221-234.

52. Kahneman, D and Tversky, A. Prospect theory: An analysis of decision under risk. Econometrica, 47, 2 (1979), 263-291.

53. Kahneman, D and Tversky, A. Choices, values and frames. American Psychologist, 39, 4 (1984), 341-350.

54. Kahneman, D; Wakker, PP; and Sarin, R. Back to Bentham? Explorations of experienced utility. Quarterly Journal of Economics, 112, 2 (1997), 375-405.

55. Kardes, FR; Posavac, SS; and Cronley, ML. Consumer inference: A review of processes, bases, and judgment contexts. Journal of Consumer Psychology, 14, 3 (2004), 230-256.

56. Kim, K and Viswanathan, S. The experts in the crowd: the role of experienced investors in a crowdfunding market. MIS Quarterly, 43, 2 (2019), 347–372.

57. Klein, G and Militello, L. The knowledge audit as a method for cognitive task analysis. In H.E. Montgomery, R.E. Lipshitz, and B.E. Brehmer (eds.), How Professionals Make Decisions. Mahway, NJ: Lawrence Erlbaum Associates, 2004, pp. 335-342.

58. Krumme, KA and Herrero, S. Lending behavior and community structure in an online peer-to-peer economic network. Presented at CSE'09. International Conference on Computational Science and Engineering, 2009, Vancouver, 2009, pp. 613-618.

59. Kwark, Y; Chen, J; and Raghunathan, S. Online product reviews: Implications for retailers and competing manufacturers. Information Systems Research, 25, 1 (2014), 93-110.

60. Lamont, OA. Macroeconomic forecasts and microeconomic forecasters. Journal of Economic Behavior & Organization, 48, 3 (2002), 265-280.

61. Lee, E and Lee, B. Herding behavior in online P2P lending: An empirical investigation. Electronic Commerce Research and Applications, 11, 5 (2012), 495-503.

62. Lefebvre, P and Merrigan, P. The impact of welfare benefits on the conjugal status of single mothers in Canada: Estimates from a hazard hodel. J. of Human Resources, 33, 3 (1998), 742-757.

63. Li, G and Wang, J. Threshold effects on backer motivations in reward-based crowdfunding. Journal of Management Information Systems, 36, 2 (2019), 546-573.

64. Li, L; Chen, J; and Raghunathan, S. Recommender systems rethink: Implications for an electronic marketplace with competing manufacturers. Information Systems Research, 29, 4 (2018), 1003- 1023.

65. Lin, M; Prabhala, NR; and Viswanathan, S. Judging borrowers by the company they keep: Friendship networks and information asymmetry in online peer-to-peer lending. Management Science, 59, 1 (2013), 17-35.

66. List, JA. Does market experience eliminate market anomalies? Quarterly Journal of Economics, 118, 1 (2003), 41-71.

67. List, JA and Shogren, JF. Price information and bidding behavior in repeated second-price auctions. American Journal of Agricultural Economics, 81, 4 (1999), 942-949.

68. Liu, D; Brass, D; Lu, Y; and Chen, D. Friendships in online peer-to-peer lending: Pipes, prisms, and relational herding. MIS Quarterly, 39, 3 (2015), 729-742.

69. Liu, D; Chen, J; and Whinston, AB. Ex ante information and the design of keyword auctions. Information Systems Research, 21, 1 (2010), 133-153.

70. Liu, J. The dramatic rise and fall of online P2P lending in China. TechCrunch, (2018), Date last accessed: April 19, 2022,

71. Liu, X; Ni, X; Qiu, Z; and Zhang, K. Like a moth to a flame: Does the stock market exacerbate credit risks of peer-to-peer (P2P) lending? Available at SSRN 3905453, (2021), Date last accessed: April 19, 2022, https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=3905453

72. Lowry, PB; Cao, J; and Everard, A. Privacy concerns versus desire for interpersonal awareness in driving the use of self-disclosure technologies: The case of instant messaging in two cultures. Journal of Management Information Systems, 27, 4 (2011), 163-200.

73. Lowry, PB; Zhang, D; Zhou, L; and Fu, X. Effects of culture, social presence, and group composition on trust in technology-supported decision-making groups. Information Systems Journal, 20, 3 (2010), 297-315.

74. Luo, B and Lin, Z. A decision tree model for herd behavior and empirical evidence from the online P2P lending market. Information Systems and e-Business Management, 11, 1 (2013), 141-160.

75. Marglin, SA. The social rate of discount and the optimal rate of investment. Quarterly Journal of Economics, 77, 1 (1963), 95-111.

76. Means, B; Crandall, B; Salas, E; and Jacobs, T. Training decision makers for the real wold. In G.A. Klein, J. Orasanu, R. Calderwood, and C.E. Zsambok (eds.), Decision Making in Action: Models and Methods. Norwood, NJ: Ablex Pyblishing Corporation, 1993, pp. 306-326.

77. Menkhoff, L; Schmidt, U; and Brozynski, T. The impact of experience on risk taking, overconfidence, and herding of fund managers: Complementary survey evidence. European Economic Review, 50, 7 (2006), 1753-1766.

78. Pan, W. Toward a consultative rule of law regime in China. Journal of Contemporary China, 12, 34 (2003), 3-43.

79. Pappas, IO; Pateli, AG; Giannakos, MN; and Chrissikopoulos, V. Moderating effects of online shopping experience on customer satisfaction and repurchase intentions. International Journal of Retail & Distribution Management, 42, 3 (2014), 187-204.

80. Parhankangas, A and Renko, M. Linguistic style and crowdfunding success among social and commercial entrepreneurs. Journal of Business Venturing, 32, 2 (2017), 215-236.

81. Pavlou, PA; Liang, H; and Xue, Y. Understanding and mitigating uncertainty in online exchange relationships: A principal-agent perspective. MIS Quarterly, 31, 1 (2007), 105-136.

82. Peerenboom, R. Globalization, path dependency and the limits of law: Administrative law reform and rule of law in the People's Republic of China. Berkeley Journal of International Law, 19, (2001), 161.

83. Pope, DG and Sydnor, JR. What’s in a picture? Evidence of discrimination from Prosper. com. Journal of Human Resources, 46, 1 (2011), 53-92.

84. Pownall, RA and Wolk, L. Bidding behavior and experience in Internet auctions. European Economic Review, 61, July (2013), 14-27.

85. Prendergast, C and Stole, L. Impetuous youngsters and jaded old-timers: Acquiring a reputation for learning. Journal of Political Economy, 104, 6 (1996), 1105-1134.

86. Reuters. China gives P2P lenders two years to exit industry: document. (2019), Date last accessed: April 19, 2022

87. SC. Regulation on credit reporting industry. (2013), Date last accessed: December 20, 2017

88. Serrano-Cinca, C and Gutiérrez-Nieto, B. The use of profit scoring as an alternative to credit scoring systems in peer-to-peer (P2P) lending. Decision Support Systems, 89, (2016), 113-122.

89. Shen, D; Krumme, C; and Lippman, A. Follow the profit or the herd? Exploring social effects in peer-to-peer lending. Presented at 2010 IEEE Second International Conference on Social Computing (SocialCom), Minneapolis, MN, 2010, pp. 137-144.

90. Simon, HA. From substantive to procedural rationality. In T.J. Kastelein, S.K. Kuipers, W.A. Nijenhuis, and G.R. Wagenaar (eds.), 25 Years of Economic Theory: Retrospect and Prospect. Boston, MA: Springer, 1976, pp. 65-86.

91. Simon, HA. Rational decision making in business organizations. American Economic Review, 69, 4 (1979), 493-513.

92. Simonsohn, U and Ariely, D. When rational sellers face nonrational buyers: Evidence from herding on eBay. Management Science, 54, 9 (2008), 1624-1637.

93. Singh, H and Frantz, R. Maximization postulate: Type I and Type II errors. Journal of Post Keynesian Economics, 11, 1 (1988), 100-107.

94. Stone, AA; Broderick, JE; Porter, LS; and Kaell, AT. The experience of rheumatoid arthritis pain and fatigue: Examining momentary reports and correlates over one week. Arthritis & Rheumatism, 10, 3 (1997), 185-193.

95. Sviokla, J. Forget Citibank, borrow from Bob. Harvard Business Review, 87, 2 (2009), 19-40.

96. Tan, X; Wang, Y; and Tan, Y. Impact of live chat on purchase in electronic markets: The moderating role of information cues. Information Systems Research, 30, 4 (2019), 1248-1271.

97. Thaler, RH. Mental accounting and consumer choice. Marketing Science, 4, 3 (1985), 199-214.

98. Thies, F; Wessel, M; and Benlian, A. Effects of social interaction dynamics on platforms. Journal of Management Information Systems, 33, 3 (2016), 843-873.

99. Tucker, C and Zhang, J. How does popularity information affect choices? A field experiment. Management Science, 57, 5 (2011), 828-842.

100. Turner, KG; Feinerman, JV; and Guy, RK. The Limits of the Rule of Law in China. Seattle, WA: University of Washington Press, 2015.

101. Ward, SG and Clark, JM. Bidding behavior in on-line auctions: An examination of the eBay Pokemon card market. International Journal of Electronic Commerce, 6, 4 (2002), 139-155.

102. Wei, X; Fan, M; You, W; and Tan, Y. An empirical study of the dynamic and differential effects of prefunding. Production and Operations Management, 30, 5 (2021), 1331-1349.

103. Xiao, S; Ho, Y-C; and Che, H. Building the momentum: Information disclosure and herding in online crowdfunding. Production and Operations Management, 30, 9 (2021), 3213-3230.

104. Xu, JJ and Chau, M. Cheap talk? The impact of lender-borrower communication on peer-to-peer lending outcomes. Journal of Management Information Systems, 35, 1 (2018), 53-85.

105. Yen, C-H and Lu, H-P. Factors influencing online auction repurchase intention. Internet Research, 18, 1 (2008), 7-25.

106. Yum, H; Lee, B; and Chae, M. From the wisdom of crowds to my own judgment in microfinance through online peer-to-peer lending platforms. Electronic Commerce Research and Applications, 11, 5 (2012), 469-483.

107. Zeithammer, R and Adams, C. The sealed-bid abstraction in online auctions. Marketing Science, 29, 6 (2010), 964-987.

108. Zhang, D; Lowry, PB; Zhou, L; and Fu, X. The impact of individualism-collectivism, social presence, and group diversity on group decision making under majority influence. Journal of Management Information Systems, 23, 4 (2007), 53-80.

109. Zhang, J and Liu, P. Rational herding in microloan markets. Management Science, 58, 5 (2012), 892-912.

110. Zhao, X; Tian, J; and Xue, L. Herding and software adoption: A re-examination based on postadoption software discontinuance. Journal of Management Information Systems, 37, 2 (2020), 484- 509.

Appendix A. Literature Review Support  
Table A1. Prominent Research on Herding Behavior in the P2P Online Lending (Microloan) Market

<table><tr><td>Citation</td><td>Platform</td><td>Definition of herding</td><td>Measures of herding</td><td>Implications</td></tr><tr><td>Berkovich [2]</td><td>Prosper</td><td>Buyers infer the purchase decisions of previous buyers as a public signal of asset quality. Thus, a higher number of buyers corresponds to higher quality.</td><td>Examining whether the estimated loan return correlates with the number of bids.</td><td>Loans with more bids are more valuable.</td></tr><tr><td>Herzenstein et al. [6]</td><td>Prosper</td><td>The greater likelihood of bidding in auctions with more existing bids.</td><td>Determining whether as the bid number on a listing increases, its likelihood of receiving an additional bid also increases.</td><td>Bidders in Prosper auctions have a greater likelihood of bidding on a listing with more bids, but only to the point at which the listing has received full funding</td></tr><tr><td>Jiang et al. [8]</td><td>127 different Chinese P2P lending platforms</td><td>A well-documented social dynamic in which individuals follow the actions of their peers</td><td>Because they focus on the platform-level, their herding measure is based on the cumulative number of investors of a platform during a given week.</td><td>This is the first and only study to examine and establish that herding behavior also occurs on the macro level, in that investors also herd in choosing which platform to use on which to offer loans. By examining platform characteristics and government regulations, and ruling out confounds, the authors provide evidence that such macro-level herding is rational.</td></tr><tr><td>Jiang et al. [9]</td><td>Anonymous leading debt-based crowdfunding platform</td><td>The tendency for an individual to follow the actions of preceding peers</td><td>The impact of cumulative lending amount a listing has received give a time on current lending amount.</td><td>Herding momentum is moderated by the predecessors' anonymity level associated with their usernames.</td></tr><tr><td>Kim and Viswanathan [10]</td><td>Appbackr</td><td>Individuals with less-accurate information tend to follow the lead of individuals with more-accurate information</td><td>The impact of cumulative amount of funding at time t-1 on current amount of funding. Or the cumulative number of investment at time t-1 as another measure.</td><td>The crowd, rather than following the herd, has the ability to infer the informative signals conveyed by the actions of the distinct types of early investors and are selective in who they follow for the distinct types of investments on this platform</td></tr><tr><td>Krumme and Herrero [11]</td><td>Prosper</td><td>The bid decision depends on the number of previous lenders.</td><td>Comparing the number of bids in each round.</td><td>The percentage funding asymptotically approaches the maximum, but initial funding occurs slowly and then accelerates once a few “pioneer” bids are placed.</td></tr><tr><td>Lee and Lee [12]</td><td>Pop Funding</td><td>An individual will follow others' decisions, regardless of source or certainty of the information.</td><td>Examining whether the increase of participation rate of a listing positively affects the probability of full findings.</td><td>An auction with a higher participation rate attracts more bids.</td></tr><tr><td>Liu et al. [13]</td><td>PPDai</td><td>When individuals face uncertainties in making economic decisions, they follow the actions of others.</td><td>Using the probability of lender bidding on a listing conditional on the total number of bids the listing gets.</td><td>The lending probability increased with the number of prior bids.</td></tr><tr><td>Luo and Lin [14]</td><td>Prosper</td><td>People use public information to infer the beliefs of others while ignoring private information.</td><td>Determining whether the average time interval between two consecutive bids is smaller for listings that contain a “friend bid” or more bid counts.</td><td>“Friend bids” and bid counts impose significant effects on the decision-making time of investors, which is evidence of herding. The availability of perfect information of the listing history would reduce the probability of herding.</td></tr><tr><td>Wei et al. [16]</td><td>JD Crowdfunding</td><td>An individual will demand more (less) of a commodity at a given price because some or all other individuals in the market also demand more (less) of the commodity</td><td>The positive regression coefficient of number of lottery backers (less informative ones) on the number of regular backers (more informative ones)</td><td>Prefunding affects regular backers directly, who in turn influence lottery backers, demonstrating the mediation effect of regular backers on lottery backers. As a result, the prefunding effect on lottery backers is indirect and second-order; herding occurs where lottery backers are attracted primarily due to the activity of regular backers, rather than prefunding.</td></tr><tr><td>Xiao et al. [17]</td><td>A leading reward-based crowdfunding platform in China</td><td>By observing and taking predecessors' funding decisions as quality signals, successors can learn about a campaign's quality from the collective wisdom of the crowd</td><td>The impact of the number of cumulative investors on the number of new investors at certain time or the funding amount as an alternative measure.</td><td>The frequency of communicative messages attenuates successors' herding momentum towards predecessors</td></tr><tr><td>Yum et al. [18]</td><td>Pop Funding</td><td>Lenders interpret information provided by borrowers and infer the creditworthiness of borrowers from observing peer voting decisions under imperfect information.</td><td>Calculating whether the portion of voting “yes” positively affects the loan funding success probability.</td><td>Collective intelligence, represented by the aggregated voting results, positively influences the funding success of borrowers who have never received funding.</td></tr><tr><td>Zhang and Liu [19]</td><td>Prosper</td><td>Rational herding is the result of observational learning among lenders.Irrational herding refers to others'decisions as a descriptive social norm or follows well-funded and thus salient listings.</td><td>Assessing the sequential influence of the lagged cumulative funding amount on the current funding.</td><td>Considerable evidence is found of rational herding on Prosper.</td></tr></table>

Table A2. Prominent Crowdfunding Research that Does not Address Herding Behavior

<table><tr><td>Citation</td><td>Platform</td><td>Purpose of paper</td><td>Non-herding claims by the paper</td></tr><tr><td>Belavina et al. [1]</td><td>General crowdfunding platforms</td><td>This paper proposes two mechanisms based on deferred payment to mitigate the risks in crowdfunding platforms.</td><td>Certain redesigned crowdfunding platform mechanism can help curb the issues of fund misappropriation and performance opacity.</td></tr><tr><td>Chakraborty and Swinney [3]</td><td>General crowdfunding platforms</td><td>This paper studies how entrepreneurs signal the quality of their product to the investors. It assumes that herding is not possible.</td><td>Assumes that herding is not possible and claims the entrepreneur should signal high quality by setting a high target that is distorted above the full information optimal level.</td></tr><tr><td>Fatehi and Wagner [4]</td><td>Bolstr, Localstake, Startwise</td><td>This paper studies how the new model of crowdfunding with revenue-sharing contracts affects investors&#x27; net present value.</td><td>Revenue-sharing contracts are a novel approach to crowdfunding and are superior to other financing models.</td></tr><tr><td>Galak et al. [5]</td><td>Kiva</td><td>This paper studies how two psychological mechanisms help investors determine to whom they should lend: the borrower group size and the investor-borrower social distance.</td><td>Investors prefer a lower number of borrowers (the size of borrower group matters). Investors favor socially similar borrowers in terms of gender, occupation, and even first name initials.</td></tr><tr><td>Hu et al. [7]</td><td>Kickstarter</td><td>This paper studies the optimal marketing product line strategy and the pricing strategy on the Kickstarter crowdfunding platform. It isolates the effects of asymmetric information and primarily addresses the marketing strategy at the platform.</td><td>When buyers are heterogeneous in their product evaluations, creators should offer a line of products with distinct levels of production quality.</td></tr><tr><td>Parhankangas and Renko [15]</td><td>Kickstart</td><td>This paper studies how the style of verbal communication factors into crowdfunding success.</td><td>Whereas improving the linguistic style in crowdfunding campaigns can improve perceptions of founding and their social campaigns, such communication factors have little influence financially.</td></tr></table>

Appendix B. Support for Robustness Checks (Tables 9–11)  
Table 9. Robustness Check (Cutoff = 95%)

<table><tr><td></td><td>(1) ln_lending_amt</td><td>(2) ln_lending_amt</td><td>(3) ln_lending_amt</td><td>(4) ln_lending_amt</td></tr><tr><td>BBC</td><td>0.00127***(12.28)</td><td>0.00148***(14.33)</td><td></td><td></td></tr><tr><td>CA</td><td>0.161***(34.06)</td><td>0.136***(28.27)</td><td>0.497***(61.28)</td><td>0.410***(46.77)</td></tr><tr><td>Loan size</td><td>0.179***(33.37)</td><td>0.141***(25.62)</td><td></td><td></td></tr><tr><td>PN</td><td>-0.213***(-12.50)</td><td>-0.228***(-13.46)</td><td>2.366***(35.71)</td><td>1.978***(29.38)</td></tr><tr><td>Loan lending</td><td>-0.732***</td><td>-0.715***(-70.40)</td><td>-1.044***(-73.57)</td><td>-0.949***(-64.31)</td></tr><tr><td>PL</td><td></td><td>0.242***(30.35)</td><td>0.113***(7.31)</td><td>0.0809**(3.16)</td></tr><tr><td>CA X PN</td><td></td><td></td><td>-0.267***(-32.53)</td><td>-0.225***(-27.05)</td></tr><tr><td>PL X PN</td><td></td><td></td><td>0.178***(7.22)</td><td>0.0678**(2.74)</td></tr><tr><td>LLC X PL</td><td></td><td></td><td></td><td>0.0283***(11.38)</td></tr><tr><td>BBC X PL</td><td></td><td></td><td></td><td>-0.00240***(-10.05)</td></tr><tr><td>LLC X CA</td><td></td><td></td><td></td><td>0.00450***(23.56)</td></tr><tr><td>BBC X CA</td><td></td><td></td><td></td><td>0.000175***(9.68)</td></tr><tr><td>Constant</td><td>2.025***(55.48)</td><td>2.502***(63.15)</td><td>0.694***(9.67)</td><td>1.165***(15.83)</td></tr><tr><td>Observations</td><td>134,870</td><td>134,870</td><td>134,870</td><td>134,870</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.120</td><td>0.126</td><td>0.129</td><td>0.148</td></tr></table>

BBC = borrower borrowing credit; CA = log(cumulative amount; PL = prominent lender; PN = percent needed for materialization; LLC = lender lending credits; CML = count materialized listings lending; CSR = count successful repayment leading

Table 10. Robustness Check (Cutoff = 75%)

<table><tr><td></td><td>(1)In_lending_amt</td><td>(2)In_lending_amt</td><td>(3)In_lending_amt</td><td>(4)In_lending_amt</td></tr><tr><td>BBC</td><td>0.00127***(12.28)</td><td>0.00105***(10.12)</td><td></td><td></td></tr><tr><td>CA</td><td>0.161***(34.06)</td><td>0.137***(28.43)</td><td>0.498***(62.26)</td><td>0.426***(49.95)</td></tr><tr><td>Loan size</td><td>0.179***(33.37)</td><td>0.139***(25.08)</td><td></td><td></td></tr><tr><td>PN</td><td>-0.213***(-12.50)</td><td>-0.185***(-10.88)</td><td>2.450***(38.96)</td><td>2.073***(32.86)</td></tr><tr><td>Loan lending</td><td>-0.732***(-71.96)</td><td>-0.667***(-64.02)</td><td>-0.995***(-67.67)</td><td>-0.901***(-59.51)</td></tr><tr><td>PL</td><td></td><td>0.203***(27.81)</td><td>0.0497***(3.65)</td><td>-0.153***(-6.45)</td></tr><tr><td>CA X PN</td><td></td><td></td><td>-0.283***(-35.51)</td><td>-0.240***(-30.29)</td></tr><tr><td>PL X PN</td><td></td><td></td><td>0.271***(11.77)</td><td>0.142***(6.16)</td></tr><tr><td>LLC X PL</td><td></td><td></td><td></td><td>0.0701***(27.03)</td></tr><tr><td>BBC X PL</td><td></td><td></td><td></td><td>-0.00344***(-13.51)</td></tr><tr><td>LLC X CA</td><td></td><td></td><td></td><td>0.00104***(4.66)</td></tr><tr><td>BBC X CA</td><td></td><td></td><td></td><td>0.000277***(12.46)</td></tr><tr><td>Constant</td><td>2.025***(55.48)</td><td>2.498***(62.18)</td><td>0.683***(9.70)</td><td>1.151***(16.14)</td></tr><tr><td>Observations</td><td>134,870</td><td>134,870</td><td>134,870</td><td>134,870</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.120</td><td>0.125</td><td>0.129</td><td>0.152</td></tr></table>

BBC = borrower borrowing credit; CA = log(cumulative amount; PL = prominent lender; PN = percent needed for materialization; LLC = lender lending credits; CML = count materialized listings lending; CSR = count successful repayment leading

Table 11. Robustness Check (fraction of PL among all lenders)

<table><tr><td></td><td>(1) ln_lending_amt</td><td>(2) ln_lending_amt</td><td>(3) ln_lending_amt</td><td>(4) ln_lending_amt</td></tr><tr><td>BBC</td><td>0.00127*** (12.28)</td><td>0.00163*** (15.19)</td><td></td><td></td></tr><tr><td>CA</td><td>0.161*** (34.06)</td><td>0.148*** (31.39)</td><td>0.456*** (64.58)</td><td>0.399*** (52.73)</td></tr><tr><td>Loan size</td><td>0.179*** (33.37)</td><td>0.123*** (22.59)</td><td></td><td></td></tr><tr><td>FPN</td><td>-0.213*** (-12.50)</td><td>-0.198*** (-11.74)</td><td>2.004*** (35.73)</td><td>1.829*** (32.17)</td></tr><tr><td>Loan lending</td><td>-0.732*** (-71.96)</td><td>-0.588*** (-55.81)</td><td>-0.916*** (-63.37)</td><td>-0.863*** (-57.08)</td></tr><tr><td>PL</td><td></td><td>2.746*** (47.60)</td><td>3.394*** (25.03)</td><td>1.687*** (6.23)</td></tr><tr><td>CA X PN</td><td></td><td></td><td>-0.218*** (-33.29)</td><td>-0.240*** (-30.29)</td></tr><tr><td>PL X PN</td><td></td><td></td><td>-1.090*** (-6.04)</td><td>-1.008*** (-5.24)</td></tr><tr><td>LLC X PL</td><td></td><td></td><td></td><td>0.177*** (7.38)</td></tr><tr><td>BBC X PL</td><td></td><td></td><td></td><td>-0.0061* (-2.47)</td></tr><tr><td>LLC X CA</td><td></td><td></td><td></td><td>0.00513*** (37.14)</td></tr><tr><td>BBC X CA</td><td></td><td></td><td></td><td>0.000677*** (4.92)</td></tr><tr><td>Constant</td><td>2.025*** (55.48)</td><td>2.605*** (68.23)</td><td>1.064*** (16.23)</td><td>1.289*** (19.20)</td></tr><tr><td>Observations</td><td>134,870</td><td>134,870</td><td>134,870</td><td>134,870</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.120</td><td>0.125</td><td>0.129</td><td>0.152</td></tr></table>

BBC = borrower borrowing credit; CA = log(cumulative amount; FPL = number of prominent lenders/number of cumulative lenders; PN = percent needed for materialization; LLC = lender lending credits; CML = count materialized listings lending; CSR = count successful repayment leading

## Appendix References

1. Belavina, E; Marinesi, S; and Tsoukalas, G. Rethinking crowdfunding platform design: Mechanisms to deter misconduct and improve efficiency. Management Science, 66, 11 (2020), 4980-4997.

2. Berkovich, E. Search and herding effects in peer-to-peer lending: Evidence from Prosper. com. Annals of Finance, 7, 3 (2011), 389-405.

3. Chakraborty, S and Swinney, R. Signaling to the crowd: Private quality information and rewards-based crowdfunding. Manufacturing & Service Operations Management, 23, 1 (2021), 155-169.

4. Fatehi, S and Wagner, MR. Crowdfunding via revenue-sharing contracts. Manufacturing & Service Operations Management, 21, 4 (2019), 875-893.

5. Galak, J; Small, D; and Stephen, AT. Microfinance decision making: A field study of prosocial lending. Journal of Marketing Research, 48, SPL (2011), S130-S137.

6. Herzenstein, M; Dholakia, UM; and Andrews, RL. Strategic herding behavior in peer-to-peer loan auctions. Journal of Interactive Marketing, 25, 1 (2011), 27-36.

7. Hu, M; Li, X; and Shi, M. Product and pricing decisions in crowdfunding. Marketing Science, 34, 3 (2015), 331-345.

8. Jiang, Y; Ho, Y-C; Yan, X; and Tan, Y. Investor platform choice: Herding, platform attributes, and regulations. Journal of Management Information Systems, 35, 1 (2018), 86- 116.

9. Jiang, Y; Ho, Y-C; Yan, X; and Tan, Y. What’s in a 'username'? The effect of perceived anonymity on herding in crowdfunding. Information Systems Research, 33, 1 (2022), 1-17.

10. Kim, K and Viswanathan, S. The experts in the crowd: the role of experienced investors in a crowdfunding market. MIS Quarterly, 43, 2 (2019), 347–372.

11. Krumme, KA and Herrero, S. Lending behavior and community structure in an online peerto-peer economic network. Presented at CSE'09. International Conference on Computational Science and Engineering, 2009, Vancouver, 2009, pp. 613-618.

12. Lee, E and Lee, B. Herding behavior in online P2P lending: An empirical investigation. Electronic Commerce Research and Applications, 11, 5 (2012), 495-503.

13. Liu, D; Brass, D; Lu, Y; and Chen, D. Friendships in online peer-to-peer lending: Pipes, prisms, and relational herding. MIS Quarterly, 39, 3 (2015), 729-742.

14. Luo, B and Lin, Z. A decision tree model for herd behavior and empirical evidence from the online P2P lending market. Information Systems and e-Business Management, 11, 1 (2013), 141-160.

15. Parhankangas, A and Renko, M. Linguistic style and crowdfunding success among social and commercial entrepreneurs. Journal of Business Venturing, 32, 2 (2017), 215-236.

16. Wei, X; Fan, M; You, W; and Tan, Y. An empirical study of the dynamic and differential effects of prefunding. Production and Operations Management, 30, 5 (2021), 1331-1349.

17. Xiao, S; Ho, Y-C; and Che, H. Building the momentum: Information disclosure and herding in online crowdfunding. Production and Operations Management, 30, 9 (2021), 3213-3230.

18. Yum, H; Lee, B; and Chae, M. From the wisdom of crowds to my own judgment in microfinance through online peer-to-peer lending platforms. Electronic Commerce Research and Applications, 11, 5 (2012), 469-483.

19. Zhang, J and Liu, P. Rational herding in microloan markets. Management Science, 58, 5 (2012), 892-912.
