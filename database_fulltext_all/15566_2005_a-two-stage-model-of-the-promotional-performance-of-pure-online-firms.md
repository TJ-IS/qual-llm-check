---
otero_id: 15566
otero_key: "CAGP2MCF"
title: "A Two-Stage Model of the Promotional Performance of Pure Online Firms"
authors: "Jianan Wu; Victor J. Cook; Edward C. Strong"
year: "2005"
journal: "Information Systems Research"
doi: "10.1287/isre.1050.0071"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/CAGP2MCF/fulltext/images/43e173affeccab30dba3bd6dedc535fb90b7ac01212bc67bda1be786e7c253eb.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# A Two-Stage Model of the Promotional Performance of Pure Online Firms

Jianan Wu, Victor J. Cook, Jr., Edward C. Strong,

To cite this article:

Jianan Wu, Victor J. Cook, Jr., Edward C. Strong, (2005) A Two-Stage Model of the Promotional Performance of Pure Online Firms. Information Systems Research 16(4):334-351. http://dx.doi.org/10.1287/isre.1050.0071

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2005 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/CAGP2MCF/fulltext/images/36f4b02f0b4be2801a8718877a90ef18420f16d50bdc0f6dd4e6ee7b5889af7e.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Two-Stage Model of the Promotional Performance of Pure Online Firms

Jianan Wu, Victor J. Cook, Jr., Edward C. Strong A. B. Freeman School of Business, Tulane University, New Orleans, Louisiana 70118 { jianan.wu@tulane.edu, victor.cook@tulane.edu, bigfoot@tulane.edu}

nternet firms frequently employ a two-stage approach to promotional activities. In Stage 1, they attract cus-Itomers to their websites through advertising. In Stage 2, firms generate sales transactions or sales leads through their website.

Comprehensive assessment of the promotional performance of pure online firms requires the study of Stage 1 and of Stage 2 jointly. In this paper we develop a joint two-stage conceptual and econometric model for assessing website promotion on three important dimensions: (1) how advertising response can be measured by linking media schedules to website log files; (2) how advertising and website characteristics jointly affect the desired system outcome of the promotion; and (3) whether the joint investigation of advertising response and desired system outcomes is essential to assess the results of website promotion.

Three general findings follow from application of our model to a pure online firm’s campaign to generate sales leads through print advertising. First, advertising and website characteristics affect sales leads in different ways. A characteristic may influence sales leads directly, or indirectly, or both. Second, assessing advertising effectiveness in an online environment may not require costly survey research data. Instead, secondary data available from website log files may be used for such assessment. Third, the interaction between the first and second stages of our two-stage model can lead to misspecifications that produce misleading inferences. This occurs because the unobserved characteristics in generating website visits and sales leads may be correlated.

Key words: e-commerce; website traffic; sales leads; two-stage model; sample selection History: V. Sambamurthy, Senior Editor; Nirup Menon, Associate Editor. This paper was received on December 12, 2002, and was with the authors 23.75 months for 3 revisions.

## 1. Introduction

Firms may be motivated to establish an online presence to achieve many objectives, including image building, generating sales leads, and transactions. These ends cannot be fulfilled unless customers know of and visit the firm’s website. Pure online firms and lesser-known offline firms must promote their websites to their target audience in various advertising vehicles in online and/or offline media. For an “Internet company that does not have a ‘brick and mortar’ counterpart, the ability of the website to ‘promote’ the company is likely to be a crucial factor in the company’s success” (Agarwal and Venkatesh 2002, p. 182). According to Advertising Age (adage.com), dot-coms spent \$7.4 billion on advertising in 1999.

Online firms follow essentially the same two-stage model of advertising. In the first stage, firms attract customers to their websites through advertising either in traditional media such as print, radio, and television, or via online media such as banners, search engines, e-mails, and affiliate programs (Hoffman and Novak 2000). In the second stage, when potential customers visit their website, firms provide them with carefully selected content and friendly navigation to create an environment conducive to generating the desired information system outcomes such as further inquiry, purchase, Web satisfaction, information quality, and system quality (Straub et al. 2002, p. 230).

These pure online firms share the same goal at Stage 1, but expect different system outcomes at Stage 2. In general, for firms in B-2-C or C-2-C markets with low customer involvement, the desired system outcome is a sales transaction. For other firms, the desired system outcome may be sales leads or some general expression of interest (Halliday 2001). In either situation, desirable system outcomes go beyond merely inducing website traffic like the number of visits or number of hits.

Measuring and understanding the behavior of website visitors and its linkage to the desired system outcome has attracted the attention of many scholars (e.g., the Special Issue on Measuring e-Commerce in Net-Enabled Organizations of Information Systems Research). The importance of research on “effective information processing techniques for analyzing customers’ electronic behavior patterns such as clickstream patterns, system outcomes such as further inquiry, purchases” (Straub et al. 2002, p. 230) has also gained recognition from the IS researchers (e.g., Straub et al. 2002). Indeed, published studies have contributed significantly to understanding customer online behavior, both in generating traffic (e.g., Hoffman and Novak 2000) and transactions within electronic stores (Hoque and Lohse 1999, Kraut et al. 2000, Telang et al. 2001, Agarwal and Venkatesh 2002, Chen and Hitt 2002, Wu and Rangaswamy 2003, etc.). However, these studies are inadequate to assess the promotional effect in the two-stage business model in online markets because the effect generated before the customers’ arrival at a firm’s website (i.e., in Stage 1) may confound the effect generated at the website (i.e., in Stage 2). A critical research question is: How do we disentangle the effects of the two stages so that we can comprehensively assess website promotion?

In this paper, we seek to answer that research question for pure online firms<sup>1</sup> by studying the two stages jointly. We develop a joint two-stage conceptual and econometric model to address three important dimensions of promotional effectiveness: (1) how advertising characteristics (e.g., ad exposure frequency, ad placement, etc.) affect website visits; (2) how website characteristics (e.g., website stickiness, serial position, etc.) affect the desired system outcome of a promotional campaign; and (3) how advertising characteristics and website characteristics jointly affect desired system outcomes.

This paper contributes to the literature in three ways. First, we develop a conceptual framework for the two-stage promotion model at the micro level. Second, we develop a methodology to measure advertising response in an online environment that does not require costly survey research data. Instead, it utilizes available secondary data from website log files, ad characteristics, and website design. Third, a customized econometric model based on our conceptual framework is developed to jointly assess promotional performance. This solution extends current discrete bivariate models (Greene 1998, Boyes et al. 1989) in several important aspects. The empirical analysis shows that the correlation between advertising response and sales leads is explained not only by the observed characteristics, but also by unobserved advertising and website factors that often are ignored. This suggests that the misspecification of single-stage website promotion models and separate two-stage models is likely to yield misleading results.

The paper is organized as follows. In §2, we develop the conceptual framework, generate the related hypothesis, and discuss the issues in our study design for the two-stage promotional model. In §3, we develop an econometric model to test our hypothesis, based on our conceptual framework. The empirical analysis using data from one pure online firm (Thestyle.com) appears in §4. Finally, in §5 we discuss some managerial implications and directions for future research. The empirical analysis using the conceptual framework applied to a pure online firm’s campaign to generate sales leads through print advertising suggests important insights: Advertising and website characteristics affect sales leads in different ways. Some advertising characteristics, like single versus double issues of a magazine, influence sales leads indirectly via their effect on website visits. Some website characteristics, like average time per page, influence sales leads directly. However, other characteristics, like response latency, affect sales leads both indirectly and directly. These insights matter to management by showing where to put an ad on a magazine page in order to increase website traffic. For example, if at zero marginal cost website traffic can be increased just 2% as a result of placing the ad flush with the right-hand page of a magazine rather than on the left-hand page, the profit impact of this action is significant.

## 2. Conceptual Framework Development

## A. Conceptual Framework and Hypothesis Development

The conceptual framework for the two-stage promotional model based on the consumers’ multistage decision-making processes is presented in Figure 1. We discuss the details of the consumers’ decision process and develop the associated hypothesis along their decision processes.

Stage 1: Advertising Exposure to Website Visits. An individual decides to visit the website if her expected utility after seeing an ad is beyond a certain threshold. A widely adopted theory of advertising response stems from utility theory in economics (e.g., Wu and Rangaswamy 2003, Moe and Fader 2004, etc.). This theory suggests that advertising response is determined by both an individual’s expected utility derived from the ad and her threshold utility (or reservation utility). Utility above the threshold leads to a favorable response (e.g., website visit). Holbrook and Lehmann (1980) and Naccarato and Neuendorf (1998) show that advertising response is multidimensional. It may take the form of brand recall, a cognition dimension; or brand preference, an attitude dimension; or brand choice, a behavioral dimension. In our conceptual framework, we specify the advertising response as the action of website visits (e.g., whether a website visit is generated or how many website visits are generated, etc.)—a behavioral dimension.

The visitor’s expected utility is affected by ad/media characteristics and dynamics. Broussard (2000) suggests that higher frequency of ad exposure leads to stronger advertising responses. Consider the case of a double issue of a magazine. A double issue remains on sale twice as long as a single issue. Being seen on the newsstand twice as long provides an opportunity for readers to experience a memory trigger from first exposure that sends them to a website. A double issue also remains in the reader’s inventory twice as long. Remaining in the reader’s inventory for twice as long increases the chance a visitor will be sent back to the website for more information. The frequency of ads increases brand recall, and thus the expected number of website visits. Therefore, we have:

Hypothesis 1a (H1a). Frequency of ad exposure has a positive impact on website visits.

Figure 1 A Dynamic Two-Stage Promotion Model of Pure Online Firms  
![](/api/attachments/CAGP2MCF/fulltext/images/33455bf6b04664526854c8253d1af65c3295b2538a7e94ca9e3171d7bf9cf2e2.jpg)

The information processing of an ad updates the visitor’s expected utility (Edell and Staelin 1983). The most salient attributes in ad processing are content and frame characteristics. Frame characteristics pertain to the medium itself and attract the attention of consumers. Content characteristics relate to the subject matter and presentation. Although both frame and content characteristics have an impact on the effectiveness of advertising (Naccarato and Neuendorf 1998), it has been consistently demonstrated that frame characteristics explain greater variance in print advertising effectiveness. Advertising studies (Holbrook and Lehmann 1980, Naccarato and Neuendorf 1998) show that content variables do not perform nearly as well as frame variables in predicting the effectiveness of advertising.

Hypothesis 1b (H1b). Attractive placement of the ad has a positive impact on website visits.

In particular, the marketing literature suggests that ads with more attractive placement in a medium will be more effective. For example, in print advertising, ads placed on the right-hand page create greater brand recall than those placed on the left-hand page of a magazine (e.g., Diamond 1968, Naccarato and Neuendorf 1998). Keller (1991) also shows that competitive advertising produces interference effect and significantly reduces recall of brand claims.

Hypothesis 1c (H1c). Competitive advertising has a negative impact on website visits.

If a reader does not visit in the current period, the advertising effect may be carried over in the reformation of expected utilities in a way that triggers visits in the next period, even though the effect wears out over time. Advertising carryover effects have been extensively studied in marketing literature and are often captured in lagged effects (e.g., Clarke 1976, Blattberg and Jeuland 1981). As such, we have:

Hypothesis 1d (H1d). Advertising has a diminishing carryover effect on website visits.

An individual’s threshold is affected by information desirability and search cost. An individual’s threshold is her reservation utility for visiting a website and may be affected by multiple factors. Higher information desirability and/or lower search costs may imply a lower threshold for a website visit. For example, individuals with a low-speed Internet connection incur higher search costs and hence have a higher threshold for visiting a website.<sup>2</sup> This situation is similar to Palmer’s (2002) “download delay” for a Web server. Ad response latency (i.e., advertising response time), as a surrogate for the effects of both advertising characteristics and ad response threshold, has been studied in marketing literature (Tybjee 1979). Haaijer et al. (2000) found that incorporating response latency significantly improved the prediction of choice behavior in conjoint analysis. Response latency has also been widely studied in the psychology literature. Shorter response latency to a stimulus often suggests stronger association and higher accessibility to the stimulus (Fazio 1990). Attitudes with higher accessibility are more likely to guide behavior than attitudes with lower accessibility (Fazio 1986). Therefore, we have:

Hypothesis 1e (H1e). The visitor’s response latency has a negative impact on website visits.

Stage 2: Website Visits to Desired System Outcomes. A desired system outcome is obtained from the visitor if her modified utility is beyond a certain threshold. The Stage 2 model again follows utility theory, as described in the Stage 1 model. If the visitor is pleased with what she has experienced on a website, she may produce a desired system outcome such as adding the product in her consideration set by requesting more information or making a purchase (Straub 2002). The nature of a promotional campaign depends on the business model (B-2-B, B-2-C, and C-2-C) and the degree of customer purchase involvement (high versus low). Classic marketing theory (e.g., Kotler 1991) suggests that consumers in B-2-C markets with low customer purchase involvement often exhibit habitual buying behavior in purchase decisions. A promotional campaign in such markets often targets sales transactions. For example, online stock-trading firms like etrade.com, ameritrade.com, and datek.com advertise aggressively to attract visitors to their websites. The firms expect that customers will sign up for their services and pay a transaction fee for each trade the customers execute. On the contrary, the purchase decisions in B-2-B markets often involve multiple decision makers/stages and exhibit complex buying behavior. A promotional campaign in such high customer purchase involvement markets primarily aims to generate sales contacts/leads rather than sales transactions per se. For example, the jobfinding firm monster.com, which advertised during both the 2001 and 2004 NFL Super Bowls, expects that their information system generates matches, not the eventual transactions, made between job seekers and employers. Our application concerns various forms of informational inquiries generated by the website (see §4).

The visitor’s expected utility is modified by website characteristics and dynamics. The factors that influence the degree to which the visitor’s utility is modified include (1) the Stage 1 response and (2) website characteristics. The linkage between advertising response and sales or sales leads has been well established in the marketing literature. Little (1979) found that sales move dynamically upward when advertising increases and downward when advertising decreases. We have:

Hypothesis 2a (H2a). The Stage 1 advertising response has a positive impact on desired system outcomes.

In e-commerce literature, Moe and Fader (2004) found that cumulative websites visits are good predictors of purchases. In particular, Bucklin and Sismeiro (2003) found that website stickiness predicts purchase behavior well.

Hypothesis 2b (H2b). A visitor’s website stickiness has a positive impact on desired system outcomes.

The website characteristics include: brand names and images (Degeratu et al. 2000); website layout and design characteristics like size, display format, serial position, ease of use/navigation (Devaraj et al. 2002, Koufaris 2002); the availability of interactive tools such as sorting, searching, and personal lists (Wu and Rangaswamy 2003); and website security variables such as privacy, trust, and reputation (Urban et al. 2000). Hoque and Lohse (1999) found that the serial position of information at a webpage attracts more attention. As such, we have:

Hypothesis 2c (H2c). The serial position on a webpage has a positive impact on desired system outcomes.

The Joint of Stage 1 and Stage 2. Indirect and direct effects on desired system outcomes. As we discussed above, the impact of website characteristics on desired system outcomes is direct, while that of advertising characteristics is indirect (via correlations between two stages). However, response latency, as a proxy for the impact from both advertising characteristics and consumers’ threshold response in Stage 1, may have not only an indirect impact on desired system outcome as stated by H1e (because of its association to advertising characteristics), but also a direct impact parallel to that stated for advertising response strength by H2a (because of its association to Stage 2 threshold and the possible correlation between the thresholds of the two stages). As such, we have:

Hypothesis 3 (H3). Response latency has both direct and indirect negative impact on desired system outcomes.

It is worth pointing out that although some of the hypotheses regarding either website visits only (H1a–H1e) or desired system outcomes only (H2a– H2c) may have been examined separately before in the marketing and information systems literature via single-stage models, they have never been tested in a joint two-stage promotional model. We next discuss our research design to empirically test these hypotheses.

## B. Field Study Design

Thestyle.com is an online retailer providing an original collection of designs built on the core concepts of de Stijl (Friedman 1982). The products featured on the website during the ad campaign quite literately were “not for sale.” They are museum-quality works of art as well as functional furniture. The owner’s advertising objective was to generate sales leads on the website<sup>3</sup> that might yield negotiated contracts for made-to-measure products sold on special commission. The products were handmade from rare hardwoods, delivered with a portfolio of construction photos for each step in the process, and assembled on the collector’s site.<sup>4</sup> Contract negotiations typically took several months, and the lead time on delivery was about 16 months. The designer-collector relationship in this application is similar to B-2-B markets with a long buying cycle, where sales leads and conversion rates, rather than transactions, are the focus of marketing efforts (e.g., Seibel Systems and GE Medical Imaging).

Thestyle.com’s advertising campaign was designed by the authors and implemented as a field experiment. Two important decisions were involved. First, selecting the media vehicle for the campaign. The New Yorker magazine was chosen based on the consideration of the targeted segment of the market. Subscribers to The New Yorker magazine fit the customer profile better than any other print vehicle: They had high disposable incomes; a large percentage were empty-nest urban professionals who owned two or more residences, and had taken two or more trips to Europe in the past year. Importantly, they also owned one or more pieces of collector-quality modern art. This product involvement increased the likelihood that readers would recognize the important link between the designs featured in ads for Thestyle and the early 20th century Dutch design group known by the name of their magazine: de Stijl. More than any other magazine, readers of The New Yorker were predisposed to find the designs featured in the ads attractive. To identify sales leads for Thestyle.com from its upscale target segment, an advertising campaign was executed in The New Yorker magazine from March 13, 2000, to December 11, 2000, in five periods. The actual ads used in this campaign and the website referenced in the ads are provided in Figure 2. During the advertising campaign, Thestyle.com recorded its system log files and sales leads. The website was not advertised on any search engines in order to avoid confounding visitor response to the advertising campaign. We also made sure from the log files that none of the visits were directed from popular search engines.

Second, selecting an advertising schedule for the campaign. This decision involved four considerations:

(1) the use of level versus pulsed insertions, (2) the size of the individual print ads, (3) the interinsertion time, and (4) the control of content characteristics. The first of these issues is well researched. The general conclusion is that pulsing schedules are more effective than level schedules in situations where advertising budgets are constrained (Strong 1974). More recently, Bronnenberg (1998) also shows that pulsing policy is optimal if the demand follows a discrete and interpretable Markov process with concave transition probabilities in advertising, and the advertising budget is constrained. Given that the advertising budget would allow far less than one insertion in every issue of the magazine, a pulsing schedule was designed.<sup>5</sup> The second decision regarding the size of the ads was a bit more complex. Learning theory (Ebbinghaus 1913) suggests that the effectiveness of an exposure increases less than proportionately with the area of the stimulus. Specifically, Ebbinghaus proposed that the effectiveness of a stimulus increases as the cube root of its area. Given this notion, two exposures of an ad of a particular size are more effective than a single exposure of an advertisement twice that area. This logic does not support using an advertisement larger than the minimum size required by The New Yorker (approximately 2 <sup>1</sup> inches square), so it was decided to use 10 exposures of the minimum-size ad. The

Figure 2 The New Yorker Advertising Campaign (2000) and Thestyle.com Website  
![](/api/attachments/CAGP2MCF/fulltext/images/548494bb00ccff889d2f6dcef765655939b1dc4388e63cab1bed4b938bc5c6e2.jpg)

third consideration was selecting the interval between exposures in the pulsing schedule. In a proprietary application of the scheduling model developed in Strong (1974), the underlying principle that makes pulsing or ad flight more effective was applied to time intervals less than a week. In that application, scheduling of two ads with very little temporal space between them (minutes) appeared to be even more effective than scheduling them with a week between ads. Given that the cost of the ad campaign remains constant, this suggests it would be more effective to schedule two ads within the same issue of a vehicle than to schedule them in consecutive issues. This led to purchasing a schedule that called for the appearance of ads in precisely the same location on two consecutive right-hand or left-hand pages in each of five editions of The New Yorker. The two pages were held relatively constant in terms of position in all five editions of the magazine. The fourth consideration was to control the potential interaction between content and frame characteristics. To control for this interaction, our advertising campaign held constant content variables like layout, appeal, brand name, and copy blocks.

## 3. Econometric Model Development

## A. Model Specification

The joint nature of our proposed two-stage promotion framework for pure online firms makes the existing single-stage methodology inappropriate for testing our hypotheses simultaneously. Therefore, we develop a customized econometric model (ORD) to test our hypothesis based on our conceptual framework.

In Stage 1, let $N _ { i j } ^ { * }$ be visitor $i \prime \mathrm { s }$ expected utility. $N _ { i j } ^ { * }$ is unobservable. We only observe $N _ { i j } ,$ the number of website visits an ad generated for a visitor i in a given advertising period $j . ^ { 6 }$ We specify $N _ { i j }$ as the measure of the websites visits in our conceptual framework. This specification is similar to the approach used by Hanssens and Weitz (1980). They specified advertising response as the number of telephone inquiries generated. This specification also matches the conceptualization of continuous awareness proposed in the classic advertising model by Nerlove and Arrow (1962) and its extensions (Naik et al. 1998). Following Gupta (1988), we posit that $N _ { i j }$ (count data) is generated in the manner of an ordered probit model.<sup>7</sup> Therefore, $N _ { i j } = n$ if and only if $\theta _ { n - 1 } \leq N _ { i j } ^ { * } \leq \theta _ { n }$ for some thresholds $\theta _ { n } \left( n = 0 , 1 , 2 , . . . \right)$ with $\theta _ { - 1 } \stackrel { \cdot } { = } - \infty$ . We further posit that the latent utility $N _ { i j } ^ { * }$ is a linear function of some observed Stage 1 drivers $X _ { i j }$ in period j and some unobserved characteristics captured by a random error $\xi _ { i j } ,$ i.e.,

$$
N _ {i j} ^ {*} = X _ {i j} \alpha + \xi_ {i j}.\tag{1}
$$

We elected to use the additive linear specifications in (1) to model a visitor’s expected utility for two reasons. First, linear specifications provide a good approximation of the true formation of utilities in both stages. There is ample evidence in the econometrics and marketing literature to support the linear assumption. Second, linear specifications are widely used in the literature and are simple to deal with in model estimation. The choice modeling literature in econometrics and marketing in the past two decades followed the linear specification in consumers’ utility formation (e.g., Wu and Rangaswamy 2003).

Let $L _ { i j } ^ { * }$ be visitor $i \prime \mathrm { s }$ modified expected utility in Stage 2. Again, $L _ { i j } ^ { * }$ is unobservable. We only observe $L _ { i j } ,$ an index indicating whether visitor i submits an

RSVP form or sends e-mail $( L _ { i j } = 1 )$ or not $( L _ { i j } = 0 )$ We specify $L _ { i j }$ as the measure of the desired system outcomes in our framework. We formulate Stage 2 as a binary probit model in which a desired system outcome is generated if the modified expected utility $L _ { i j } ^ { * }$ is beyond a certain threshold (which is assumed to be 0 because it confounds the anchor point of $L _ { i j } ^ { * } )$ , i.e., $L _ { i j } = 1$ if and only if $L _ { i j } ^ { * } > 0$ . With the same consideration as in Stage 1, we posit that $L _ { i j } ^ { * }$ is a linear function of some observed Stage 2 drivers $Z _ { i j }$ in the period and some unobserved random errors as

$$
L _ {i j} ^ {*} = Z _ {i j} \gamma + \eta_ {i j}.\tag{2}
$$

The binary specification of Stage 2 response is appropriate because the online retailer in our application was concerned only with whether the offline advertising and online website design jointly generated sales leads. However, our model can be easily modified to apply to other Stage 2 responses. For example, the desired system outcome of the website promotion could be the number of orders from a visitor in a period. In this case, the Stage 2 equation (2) can be specified as an ordered probit similar to the specification of Stage 1 equation (1). Alternatively, if the desired system outcome of the website promotion is sales revenues per customer in a period, then the Stage 2 equation (2) can be specified as a truncated normal distribution. In either case, the estimation can be carried out in a similar way with little difficulty.

So far, the Stage 1 drivers and Stage 2 drivers are specified at the period level, which is silent on the possible carryover effects for advertising response and website response across periods. For example, at Stage 1, potential customer $i ,$ who visited the website several times in period $j - 1$ may visit fewer times in period $j . \mathrm { O r } ,$ in Stage 2, a visitor i who did not generate a desired system outcome in period $j - 1$ but visited the website more times in period $j ,$ may be more likely to generate a desired system outcome in period $j .$ To take these issues into consideration, we posit some general dynamic effects across periods. Specifically, we posit that (1) visitor $i ^ { \prime } \mathrm { s }$ advertising response in period $j - 1 ~ ( N _ { i j - 1 } )$ has an impact on his or her advertising response $( N _ { i j } )$ in period $j ,$ and (2) both visitor i’s advertising response in period j $( N _ { i j } )$ and the website response in period $j - 1 \ ( L _ { i j - 1 } )$

have an impact on website response in period $j ~ ( L _ { i j } )$ We use the conventional lagged-modeling approach (e.g., Clarke 1976) to formalize this idea:

$$
N _ {i j} ^ {*} = X _ {i j} \alpha + \nu_ {N} N _ {i j - 1} + \xi_ {i j},\tag{3}
$$

$$
L _ {i j} ^ {*} = Z _ {i j} \gamma + \kappa_ {N} N _ {i j} + \kappa_ {L} L _ {i j - 1} + \eta_ {i j}.\tag{4}
$$

Note that in Equations (3) and (4), the random errors $\xi _ { i j }$ and $\eta _ { i j }$ capture the unobserved components (e.g., missing explanatory variables) of the advertising response and desired system outcome for visitor i in period $j .$ If these unobserved components share some common attributes $( \mathrm { e . g . }$ , the psychographics of visitor i), then $\xi _ { i j }$ and $\eta _ { i j }$ may be correlated. For this consideration, we then assume that $\xi _ { i j }$ and $\eta _ { i j }$ follow an i.i.d. bivariate normal distribution as

$$
\binom{\xi_ {i j}}{\eta_ {i j}} \sim B I V (0, \Sigma), \quad \text {and} \quad \Sigma = \left( \begin{array}{c c} \sigma_ {N} ^ {2} & \rho \sigma_ {N} \sigma_ {L} \\ \rho \sigma_ {N} \sigma_ {L} & \sigma_ {L} ^ {2} \end{array} \right)\tag{5}
$$

is the variance-covariance matrix. Our model is completely specified by Equations (3)–(5).

## B. Estimation Specification

Note that Stage 1 equation (3) is an ordered probit model and the Stage 2 equation (4) is a probit model. We fix $\sigma _ { L } = 1$ and $\sigma _ { N } = 1$ for model parameter identification. Further, we must fix $\theta _ { 0 } = 0$ because $\theta _ { 0 }$ is confounding the constant term in Equation (3). Also note that our model is a recursive simultaneous equation system (Greene 1998). Using the reduced form of the simultaneous equation system, it is easy to see that the structural parameter $\kappa _ { N }$ is also identified if the sets of independent variables of Equations (3) and (4) are not identical. This condition is indeed satisfied because $N _ { i j - 1 } ,$ which shows up in Equation (3), does not appear in Equation (4).

Our model has a censoring issue as well. If visitor i does not visit the website in period $j ~ ( \mathrm { i . e . } , ~ N _ { i j } = 0 )$ then visitor i can never return a desired system outcome $( \mathrm { i . e . , ~ } L _ { i j } = 0 )$ . This censoring characteristic leads to sample selection bias in parameter estimation if it is not properly dealt with (Boyes et al. 1989). Therefore, we partition the sample log-likelihood into two parts:

$$
\begin{array}{c} L L = \sum_ {i} \sum_ {j} \ln f (N _ {i j} = n, L _ {i j} = l) \big | _ {n \geq 1} \\ + \sum_ {i} \sum_ {j} \ln f (N _ {i j} = n, L _ {i j} = l) \big | _ {n = 0}. \end{array}\tag{6}
$$

The first term of (6) is calculated as

$$
\ln f (N _ {i j} = n, L _ {i j} = l) \big | _ {n \geq 1}
$$

$$
= l \ln \operatorname * {P r} (N _ {i j} = n, L _ {i j} = 1) + (1 - l) \ln \operatorname * {P r} (N _ {i j} = n, L _ {i j} = 0)
$$

$$
= l \ln (\operatorname * {P r} (N _ {i j} \leq n, L _ {i j} ^ {*} \geq 0) - \operatorname * {P r} (N _ {i j} \leq n - 1, L _ {i j} ^ {*} \geq 0))
$$

$$
+ (1 - l) \ln (\operatorname * {P r} (N _ {i j} \leq n, L _ {i j} ^ {*} <   0) - \operatorname * {P r} (N _ {i j} \leq n - 1, L _ {i j} ^ {*} <   0))
$$

$$
\begin{array}{r l} & {= l \ln [ (\Phi (\tau_ {i j n}) - \Phi_ {2} (\tau_ {i j n}, v _ {i j}; \rho))} \\ & {\qquad - (\Phi (\tau_ {i j n - 1}) - \Phi_ {2} (\tau_ {i j n - 1}, v _ {i j}; \rho)) ]} \\ & {\qquad + (1 - l) \ln [ \Phi_ {2} (\tau_ {i j n}, v _ {i j}; \rho) - \Phi_ {2} (\tau_ {i j n - 1}, v _ {i j}; \rho) ],} \end{array}\tag{7}
$$

where $\tau _ { i j n } = \theta _ { n } - ( X _ { i j } \alpha + \nu _ { N } N _ { i j - 1 } )$ and $v _ { i j } = - ( Z _ { i j } \gamma +$ $\kappa _ { N } N _ { i j } + \kappa _ { L } L _ { i j - 1 } )$ , and $\Phi _ { 2 }$ is the CDF for the standard bivariate normal distribution. The second term of (6) is calculated as

$$
\begin{array}{r l} & {\ln f (N _ {i j} = n, L _ {i j} = l) \big | _ {n = 0} = \ln (\Phi (\tau_ {i j 0}))} \\ & {\qquad = \ln (1 - \Phi (X _ {i j} \alpha + \nu_ {N} N _ {i j - 1})).} \end{array}\tag{8}
$$

Plug (7) and (8) into (6), and we obtain the sample log-likelihood. We use the maximum likelihood estimate (MLE) to estimate our model, i.e., for given data $( N _ { i j } , L _ { i j } , X _ { i j } , Z _ { i j } )$ , we estimate parameters $( \alpha , \gamma , \theta , \nu , \kappa , \Sigma )$ by maximizing sample log-likelihood (6). This joint MLE is consistent and efficient. The covariance matrix of the estimator is obtained using the Hessian of Newton-Raphson type of gradient methods in nonlinear optimization procedures. The estimates when two stages were separately estimated using random starting values were used as the starting values for our model.

Bivariate probit models have been studied before in the literature. For instance, Greene (1998) studied a cross-sectional simultaneous bivariate probit model without censoring, and Boyes et al. (1989) studied a cross-sectional censored bivariate probit model without simultaneity. It is important to recognize that our proposed model extends these bivariate probit models in several aspects. Our model (1) is both a censored and simultaneous equation model; (2) has an ordered probit model (rather than a binary probit) in Stage 1; and (3) is both cross-sectional and longitudinal.

## C. Alternative Model Specifications

While it might be standard to model a dichotomous variable $L _ { i j }$ (Stage 2 response) as a probit model, there are other alternatives for modeling the count variable $N _ { i j }$ (Stage 1 response). We considered three Poisson distribution-based alternatives in which each has a different rationale. The first alternative (POS) models $N _ { i j }$ as a Poisson process because it has been extensively used to model random count variables (e.g., Greene 2000). The second alternative, negative binomial distribution (NBD), is an extension of POS by taking into consideration that potential customers may be heterogeneous in their visit rates. This model, commonly referred to as the negative binomial, has also been extensively adopted in marketing and economics literature to study consumer heterogeneity. The third alternative (HUR) considers that the zero count in $N _ { i j }$ is qualitatively different from the nonzero count. For example, a visitor may have failed to visit the website because they did not see the ad and not because they saw the ad but chose not to visit. As such, the zero count reflects the no-exposure effect, while the nonzero count reflects the exposure effect of the ad. These two effects are qualitatively different.<sup>8</sup>

## 4. Empirical Analysis

## A. Measurements

To test the hypotheses, we specified the measurements for the constructs developed in our conceptual framework. The Stage 1 specifications include: SHEL $F _ { j } ,$ $R I G H T _ { j } , \ O T H C L _ { j } , \ N _ { - } L A G _ { i j } , \ F S T A V _ { i j } , \ P T I M E _ { j } . ^ { 9 }$ The Stage 2 specifications include: $N C \bar { U } R R _ { i j } , \ S T \bar { I } M E _ { i j } , ^ { 1 0 }$

$N P A G E _ { i j } , P R S V P _ { j } , L \_ L A G _ { i j } ,$ FSTAV<sub>ij</sub>. Their definitions and corresponding constructs are given in Table 1.

We plotted advertising pulses, website visits, and sales leads against time in Figure 3. Two stylized facts can be observed from this distribution. First, immediately after each ad exposure there is an increase in website visits and an increase in sales leads, suggesting face validity for our two-stage model. Second, the advertising effects for all five ads follow a similar pattern—rapid attainment of a peak, followed by a period where visits gradually fade away. $N _ { i j }$ has 79.06% of the total observations at 0, 18.90% at 1, 1.47% at 2, 0.39% at 3, 0.12% at 4, 0.04% at 5, and 0.02% at 6. Theory on search behavior for durable products (e.g., Punj and Staelin 1983) suggests that external search increases if search cost is low or prior knowledge is general and class specific (not product specific). Given the reduced search cost of Internet access and the unlikely prior knowledge from de Stijl’s early 20th century Dutch origin, multiple website visits from the same visitor for a durable product like our collector’s furniture are expected. The descriptive statistics of the independent variables in both stages are reported in Table 2. The correlations of the independent variables at both stages exist (three correlations at Stage 1 and one correlation at Stage 2 are around 0.5), but are not problematic in estimation convergence.

## B. Model Selection

To select the right model to test our hypothesis, we empirically benchmark the performance of the four specified models on calibration and validation. Sixty percent of our sample (2,069 visitors over the five periods, with 10,345 observations) was randomly selected as a calibration sample and the remaining 40% (1,379 visitors over the five periods, with 6,895 observations) was retained as a cross-validation sample. The observed highest $N _ { i j }$ in our data set is 6. Therefore, we estimated five thresholds in our model (ORD).

Table 1 Constructs and Their Measurements

<table><tr><td>Stage</td><td>Construct</td><td>Measures</td><td>Data extraction</td><td>Name</td></tr><tr><td rowspan="6">1</td><td>H1a: Frequency of ad exposure (e.g., Broussard 2000)</td><td>Shelf life of a magazine in ad period j. It is 1 if it is a double issue spanning a two-week period, 0 if it is a single issue on sale for one week.</td><td>Advertising schedule</td><td> $SHELF_j$ </td></tr><tr><td>H1b: Ad placement attractiveness (e.g., Holbrook and Lehmann 1980)</td><td>Ad placement position. It is 1 if the ad is in the right-most column of the right-hand page, 0 otherwise.</td><td>Advertising schedule</td><td> $RIGHT_j$ </td></tr><tr><td>H1c: Competitive advertising (e.g., Keller 1991)</td><td>Whether other color ads show up on the same page in ad period j. It is 1 if other color ads show up in the same page, 0 otherwise.</td><td>Advertising schedule</td><td> $OTHCL_j$ </td></tr><tr><td>H1d: Advertising carryover (e.g., Clarke 1976)</td><td>The number of times visitor i visited the website in period j - 1.</td><td>Web log file</td><td> $N\_LAG_{ij}$ </td></tr><tr><td>H1e and H3: Response latency (e.g., Fazio 1990)</td><td>A continuous variable which is taken as the time elapsed (scaled with a log transformation) between the start of the ad period and the time of visitor i&#x27;s first visit.</td><td>Advertising schedule and Web log file</td><td> $FSTAV_{ij}$ </td></tr><tr><td>Control variable</td><td>The period length of time (with a log transformation) is included as a control variables.</td><td>Advertising schedule</td><td> $PTIME_j$ </td></tr><tr><td rowspan="4">2</td><td>H2a: Stage 1 ad response (e.g., Little 1979)</td><td>The total number of visits visitor i made to the website in period j before i became a sales lead in period j.</td><td>Web log file</td><td> $NCURR_{ij}$ </td></tr><tr><td rowspan="2">H2b: Website stickiness (e.g., Bucklin and Sismeiro 2003)</td><td>The average time visitor i spent per page before he or she became a sales lead in period j.</td><td>Web log file</td><td> $STIME_{ij}$ </td></tr><tr><td>The average number of pages downloaded per visit by visitor i before i became a sales lead in period j.</td><td>Web log file</td><td> $NPAGE_{ij}$ </td></tr><tr><td>H2c: Serial position (e.g., Hoque and Lohse 1999)</td><td>The location of the “RSVP” form link on the home page of the website in period j, with 1 representing top position, 0 representing bottom position in the navigation frame.</td><td>Website file</td><td> $PRSVP_j$ </td></tr></table>

Notes.  
1. The decomposition of the total time visitor i spent on the website in period j into three components $( N C U R R _ { i j } , S T I M E _ { i j } , N P A G E _ { i j } )$ reduces the correlation among these variables to less than 0.2.  
2. In our application, the observation of the sales leads was a rare event (less than 1%). This fact leads to the serious lack of variation of the variable, which further leads to very unstable parameter estimation. Taking these facts into consideration, we dropped $L _ { - } L A G _ { i j }$ in our empirical analysis.

The goodness-of-fit for the calibration results for all four models are given in Table 3. Among these models, POS is the most parsimonious with 14 free parameters, while the ORD model is the least parsimonious one with 19 parameters. The NBD and HUR are in-between with 15 free parameters. We benchmark these models using various criteria: loglikelihood, AIC, and BIC. All the indices unanimously show that HUR is the worst, NBD and POS are better, but ORD is by far the best among the four.

To assess the improvement of model fit due to model structure, we compared each of the four models with the equal probability model, in which each possible event $( N , L )$ happens with equal probability. The value of $\rho _ { 0 } ^ { 2 }$ indicates that each model structure significantly improves the goodness-of-fit compared to the equal probability model. To assess the improvement of model fit due to the specification of the independent variables, we also compared each of the four models with its restricted submodel, in which all the independent variables except the constants are dropped. The value of $\rho _ { C } ^ { 2 }$ indicates that the independent-variable specifications in both stages significantly improve the model fit as well $( \chi ^ { 2 }$ statistics are significant at 0.01 level). Again, both $\rho _ { 0 } ^ { 2 }$ and $\rho _ { C } ^ { 2 }$ indicate that the ORD model is superior to the other three alternatives.

Four criteria were used to make our judgment on validation: (1) predicted log-likelihood, (2) $\rho _ { 0 } ^ { 2 }$ and $\rho _ { C } ^ { 2 }$ (3) root mean square error (RMSE), (4) U statistics. For the managerial consideration, we employed two additional criteria for the prediction of Stage 2 outcomes: (5) average predicted probability and (6) adjusted hit ratio. In most of the literature, the hit ratio is determined using a naïve cut-off probability of 0.5 for a binary variable. Because the data structure of L is highly unbalanced in our data set (i.e., the proportion of nonleads (99.12%) is much bigger than the proportion of leads (0.88%)), the conventional hit ratio based on the naïve cut-off probability does not represent the true validity of the models and gives little predictive

<table><tr><td>Stage 1 correlation</td><td>SHELF</td><td>RIGHT</td><td>OTHCL</td><td>N_LAG</td><td>FSTAV</td><td>PTIME</td></tr><tr><td>SHELF</td><td>1.000</td><td>-0.166</td><td>-0.166</td><td>-0.003</td><td>0.187</td><td>0.166</td></tr><tr><td>RIGHT</td><td></td><td>1.000</td><td>0.166</td><td>0.161</td><td>0.536</td><td>0.566</td></tr><tr><td>OTHCL</td><td></td><td></td><td>1.000</td><td>-0.047</td><td>-0.182</td><td>-0.166</td></tr><tr><td>N_LAG</td><td></td><td></td><td></td><td>1.000</td><td>-0.328</td><td>0.170</td></tr><tr><td>FSTAV</td><td></td><td></td><td></td><td></td><td>1.000</td><td>0.546</td></tr><tr><td>PTIME</td><td></td><td></td><td></td><td></td><td></td><td>1.000</td></tr><tr><td>Mean</td><td>0.400</td><td>0.600</td><td>0.600</td><td>0.238</td><td>1.537</td><td>3.400</td></tr><tr><td>Stage 2 correlation</td><td>NCURR</td><td>STIME</td><td>NPAGE</td><td>PRSVP</td><td>FSTAV</td><td></td></tr><tr><td>NCURR</td><td>1.000</td><td>0.379</td><td>0.504</td><td>0.072</td><td>-0.328</td><td></td></tr><tr><td>STIME</td><td></td><td>1.000</td><td>0.364</td><td>-0.006</td><td>-0.148</td><td></td></tr><tr><td>NPAGE</td><td></td><td></td><td>1.000</td><td>0.035</td><td>-0.359</td><td></td></tr><tr><td>PRSVP</td><td></td><td></td><td></td><td>1.000</td><td>0.397</td><td></td></tr><tr><td>FSTAV</td><td></td><td></td><td></td><td></td><td>1.000</td><td></td></tr><tr><td>Mean</td><td>0.238</td><td>0.030</td><td>0.319</td><td>0.600</td><td>1.537</td><td></td></tr></table>

Figure 3 The Number of Visits, Number of Leads, and Advertising Against Time  
![](/api/attachments/CAGP2MCF/fulltext/images/c649deee2ae8c2a645ffc281cd1cb79b71571a31b30963f2c43a243f0c835b9e.jpg)

Table 2 Descriptive Statistics of Independent Variables power. To account for this characteristic of the data, we developed a new validity measure, the adjusted hit ratio. In this measure, the cut-off probability is calculated as the average predicted probability of the calibration sample, i.e.,

$$
\text { Cut - off   probability } = \frac {1}{N} \sum_ {i, j} \hat {L} _ {i j},\tag{9}
$$

$$
N = \text { calibration   sample   size }.
$$

The adjusted hit ratio not only exhibits greater validity, but also gives much higher predictive power. This cut-off probability is managerially useful for online firms to select the right customers to target, especially when the targeting costs are substantially greater than the expected benefits, as was true in our application. However, in other situations, one may just rank each visitor using the predicted lead generation probability $\hat { L } _ { i j }$ and pick up the top “n” prospects.<sup>11</sup>

Cross-sample validation results of the four competing models also are reported in Table 3. When the two stages of the models are examined jointly, we find that (1) the log-likelihood, $\rho _ { 0 } ^ { 2 } ,$ and $\rho _ { C } ^ { 2 }$ are consistent with

Table 3 Model Goodness-of-Fit and Cross-Sample Validation

<table><tr><td rowspan="3"></td><td colspan="8">Goodness-of-fit</td></tr><tr><td colspan="4">Model calibration</td><td colspan="4">Model validation</td></tr><tr><td>POS</td><td>NBD</td><td>HUR</td><td>ORD</td><td>POS</td><td>NBD</td><td>HUR</td><td>ORD</td></tr><tr><td>No. of customers</td><td>2,069</td><td>2,069</td><td>2,069</td><td>2,069</td><td>1,379</td><td>1,379</td><td>1,379</td><td>1,379</td></tr><tr><td>No. of observations</td><td>10,345</td><td>10,345</td><td>10,345</td><td>10,345</td><td>6,895</td><td>6,895</td><td>6,895</td><td>6,895</td></tr><tr><td>No. of free parameters</td><td>14</td><td>15</td><td>15</td><td>19</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>LL</td><td>-4,878.343</td><td>-4,885.832</td><td>-6,592.322</td><td>-3,780.42</td><td>-3,209.281</td><td>-3,220.641</td><td>-4,369.365</td><td>-2,517.90</td></tr><tr><td>AIC</td><td>0.946</td><td>0.947</td><td>1.277</td><td>0.735</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>BIC</td><td>0.956</td><td>0.958</td><td>1.288</td><td>0.748</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td> $\rho_0^2$ </td><td>0.810</td><td>0.810</td><td>0.744</td><td>0.853</td><td>0.813</td><td>0.812</td><td>0.745</td><td>0.853</td></tr><tr><td> $\rho_C^2$ </td><td>0.251</td><td>0.249</td><td>0.011</td><td>0.424</td><td>0.254</td><td>0.250</td><td>0.010</td><td>0.424</td></tr><tr><td rowspan="3"></td><td colspan="8">Cross-sample validation</td></tr><tr><td colspan="4">Advertising response</td><td colspan="4">Desired system outcome</td></tr><tr><td>POS</td><td>NBD</td><td>HUR</td><td>ORD</td><td>POS</td><td>NBD</td><td>HUR</td><td>ORD</td></tr><tr><td>RMSE</td><td>0.957</td><td>1.864</td><td>0.918</td><td>0.411</td><td>0.401</td><td>0.424</td><td>0.407</td><td>0.397</td></tr><tr><td>Total RMSE</td><td>—</td><td>—</td><td>—</td><td>—</td><td>0.734</td><td>1.351</td><td>0.710</td><td>0.404</td></tr><tr><td>U statistics</td><td>0.571</td><td>0.690</td><td>0.587</td><td>0.389</td><td>0.796</td><td>0.805</td><td>0.799</td><td>0.794</td></tr><tr><td>Total U statistics</td><td>—</td><td>—</td><td>—</td><td>—</td><td>0.590</td><td>0.694</td><td>0.607</td><td>0.472</td></tr><tr><td>Cut-off probability</td><td>—</td><td>—</td><td>—</td><td>—</td><td>0.010</td><td>0.012</td><td>0.011</td><td>0.010</td></tr><tr><td>APP for leads</td><td>—</td><td>—</td><td>—</td><td>—</td><td>0.084</td><td>0.078</td><td>0.084</td><td>0.086</td></tr><tr><td>APP for nonleads</td><td>—</td><td>—</td><td>—</td><td>—</td><td>0.010</td><td>0.011</td><td>0.010</td><td>0.010</td></tr><tr><td>AHR for leads</td><td>—</td><td>—</td><td>—</td><td>—</td><td>0.983</td><td>1.000</td><td>0.983</td><td>0.983</td></tr><tr><td>AHR for nonleads</td><td>—</td><td>—</td><td>—</td><td>—</td><td>0.838</td><td>0.818</td><td>0.833</td><td>0.840</td></tr></table>

Notes. $A | \mathsf { C } = [ - 2 * L L + 2 * K ] / N$ and ${ \mathsf { B I C } } = [ - 2 * L L + \mathsf { I n } ( N ) * k ] / N ,$ where K number of free parameters and N number of observations. LL is the log-likelihood value $\rho _ { 0 } ^ { 2 } = 1 - L L / L L ( 0 )$ and $\rho _ { C } ^ { 2 } = 1 - L L / L L ( C ) .$ , where LL 0 is the log-likelihood of the equal probability model and LL C is the log-likelihood value for the model in which all the covariates except the constant terms are dropped. RMSE is the square root of the average of the squared difference between the actual values and the predicted values. U statistics is a modified Theil’s U (e.g., Gupta 1988). APP for nonleads and leads are the average predicted probabilities for $L = 0$ and $L = 1 .$ . AHR for nonleads and leads are the adjusted hit ratio for L 0 and L 1. Total RMSE and total U statistics are the RMSE and U statistics with the two equations calculated together.

those reported in the model calibration; and (2) the total RMSE and total U statistics strongly suggest that ORD has the best predictive performance among the four models. When the two stages are examined separately, we further find that the superior performance of ORD is largely due to its performance at Stage 1. This is not a surprise because all of the four models have an identical specification at Stage 2. A further look at the predictive power at Stage 2 outcome revealed two interesting observations. First, the average predicted probability for leads from the calibration sample is between 0.078 and 0.086 for the four models. This fact indicates that a conventional cut-off probability at 0.5 would indeed predict each observation as a nonlead with certainty (100%), and hence would give no predictive power regardless of which model was used. On the other hand, using the cutoff probability suggested by Equation (9), each of the four models can discriminate the leads and nonleads satisfactorily with an adjusted hit ratio above 98% for leads and 81% for nonleads. Second, the ORD model seems to have the better discriminating power than the other three competing models. The ORD model produces the largest gap between the average predicted probabilities for leads and nonleads. In terms of adjusted hit ratio, the same conclusion holds. Based on these results, we selected the ORD model for the rest of our empirical analysis.

## C. Hypothesis Testing and Managerial Implications

Parameter estimates of the ORD model are reported in Table 4. Stage 1 hypotheses are supported. First, a double issue generates more website traffic than a single issue (the coefficient of SHELF is significantly positive in Stage 1), which supports Hypothesis H1a. This seemingly simple result has significant economic implications because ads placed in a double issue cost the same as those placed in a single issue. Second, placing ads in the right-most column of the right page produces higher traffic than placement in the lefthand column of the left page (the coefficient of RIGHT is significant and positive), which supports Hypothesis H1b. Third, the coefficient of OTHCL is significant and negative, suggesting it also would pay to have the vehicle sales representative place ads so as to avoid other color ads in the column. This finding supports Hypothesis H1c. Fourth, advertising indeed has carryover effect on website visits (the coefficient of N\_LAG is significant), but the effect wears out (the absolute value of the coefficient is smaller than 1), providing support for Hypothesis H1d. Finally, visitors who have visited the website immediately after the exposure to an ad are more likely to return to the website again in the same period (the coefficient of FSTAV is significant and negative). This finding supports Hypothesis H1e.

Table 4 Parameter Estimates and Marginal Effects on Sales Leads Generation of Model ORD and Hypothesis Testing

<table><tr><td>Variable</td><td>Estimate</td><td>Std. error</td><td>Indirect marginal effect</td><td>Direct marginal effect</td><td>Total marginal effect</td><td>Hypothesis</td><td>Support</td></tr><tr><td colspan="8">Stage 1</td></tr><tr><td>CONST</td><td>-2.131***</td><td>(0.050)</td><td>—</td><td>—</td><td>—</td><td></td><td></td></tr><tr><td>SHELF</td><td>0.196***</td><td>(0.024)</td><td>0.002</td><td>—</td><td>0.002</td><td>H1a</td><td>Yes</td></tr><tr><td>RIGHT</td><td>0.930***</td><td>(0.062)</td><td>0.010</td><td>—</td><td>0.010</td><td>H1b</td><td>Yes</td></tr><tr><td>OTHCL</td><td>-0.547***</td><td>(0.042)</td><td>-0.006</td><td>—</td><td>-0.006</td><td>H1c</td><td>Yes</td></tr><tr><td>N_LAG</td><td>-0.311***</td><td>(0.052)</td><td>-0.075</td><td>—</td><td>-0.075</td><td>H1d</td><td>Yes</td></tr><tr><td>FSTAV</td><td>-1.689***</td><td>(0.043)</td><td>-0.406</td><td>—</td><td>—</td><td>H1e</td><td>Yes</td></tr><tr><td>PTIME</td><td>2.257***</td><td>(0.075)</td><td>—</td><td>—</td><td>—</td><td></td><td></td></tr><tr><td>THETA_1</td><td>2.934***</td><td>(0.094)</td><td>—</td><td>—</td><td>—</td><td></td><td></td></tr><tr><td>THETA_2</td><td>3.486***</td><td>(0.107)</td><td>—</td><td>—</td><td>—</td><td></td><td></td></tr><tr><td>THETA_3</td><td>3.862***</td><td>(0.130)</td><td>—</td><td>—</td><td>—</td><td></td><td></td></tr><tr><td>THETA_4</td><td>4.180***</td><td>(0.179)</td><td>—</td><td>—</td><td>—</td><td></td><td></td></tr><tr><td>THETA_5</td><td>4.441***</td><td>(0.253)</td><td>—</td><td>—</td><td>—</td><td></td><td></td></tr><tr><td colspan="8">Stage 2</td></tr><tr><td>CONST</td><td>-3.390***</td><td>(0.418)</td><td>—</td><td>—</td><td>—</td><td></td><td></td></tr><tr><td>NCURR</td><td>0.222**</td><td>(0.082)</td><td>—</td><td>0.038</td><td>0.038</td><td>H2a</td><td>Yes</td></tr><tr><td>STIME</td><td>0.358**</td><td>(0.152)</td><td>—</td><td>0.062</td><td>0.062</td><td>H2b</td><td>Yes</td></tr><tr><td>NPAGE</td><td>0.418***</td><td>(0.094)</td><td>—</td><td>0.072</td><td>0.072</td><td>H2b</td><td>Yes</td></tr><tr><td>PRSVP</td><td>0.689***</td><td>(0.135)</td><td>—</td><td>0.033</td><td>0.033</td><td>H2c</td><td>Yes</td></tr><tr><td>FSTAV</td><td>-0.196***</td><td>(0.078)</td><td>-0.406</td><td>-0.034</td><td>-0.440</td><td>H3</td><td>Yes</td></tr><tr><td colspan="8">Error correlations</td></tr><tr><td>RHO (ρ)</td><td>0.108**</td><td>(0.058)</td><td>—</td><td>—</td><td>—</td><td></td><td></td></tr><tr><td>Log-likelihood</td><td colspan="7">-3,780.42</td></tr></table>

∗∗Significant at 0.05. ∗∗∗Significant at 0.01.

Stage 2 hypotheses are also supported. First, those visitors who are most likely to become sales leads have the following characteristics: (1) they made more visits to the website (the coefficient of NCURR is significant and positive), providing support for Hypothesis H2a; and (2) they spent more time on each page (the coefficient of STIME is significant and positive) and they downloaded more pages each time they made a visit (the coefficient of NPAGE is significant and positive), providing support for Hypothesis H2b. Second, the serial positioning of the link to the response form within the homepage navigation menu is important in generating sales leads. A visitor is more likely to submit an RSVP form if the link is placed at the top of the page than at the bottom of the page (the coefficient of PRSVP is significant and positive). This finding provides support for Hypothesis H2c. The decomposition of the stickiness into knowledge of viewing time and number of pages downloaded made it possible for the owner of Thestyle.com to sort leads into high-yield visitors and low-yield visitors. In this way, he tailored personal e-mail responses to fit the high-yield versus low-yield sales leads.

Table 4 indicates that the Stage 1 advertising response N 	 and the Stage 2 sales leads L	 are positively correlated in two different ways: (1) a positive correlation via the observed structural parameter $\kappa _ { N }$ (the coefficient of NCURR is significant and positive), and (2) a positive correlation via the unobserved errors (the correlation parameter RHO of the error terms is significant and positive). These two findings suggest that although observable consumer-specific advertising and website characteristics (e.g., response latency, session time, etc.) can partially characterize the correlation between Stage 1 and Stage 2 expected utilities, the often unobserved characteristics of visitors in our two-stage promotional model (e.g., threshold effects, consumer demographics and psychographics) contribute to such correlation. This attribution may bias the assessment of the drivers of desired system outcomes when the correlation between the unobserved errors is not introduced.

We further find that the quicker visits have both a positive direct effect (the coefficient of FSTAV in Stage 2 is significant and negative) and a positive indirect effect (the coefficient of FSTAV in Stage 1 is significant and negative), providing empirical support to Hypothesis H3. The hypothesis testing results are summarized in Table 4.

To further compare the relative impact of different independent variables on sales leads, we calculated the marginal effects (Greene 1998). In our model, the conditional mean of sales leads L is

$$
\begin{array}{r l} & E (L _ {i j} \mid X _ {i j}, Z _ {i j}) \\ & \quad = \sum_ {n > 0} \operatorname * {P r} (L _ {i j} = 1, N _ {i j} = n \mid X _ {i j}, Z _ {i j}) \\ & \quad = \sum_ {n > 0} \bigl \{(\Phi (\tau_ {i j n}) - \Phi_ {2} (\tau_ {i j n}, v _ {i j}; \rho)) \\ & \qquad - (\Phi (\tau_ {i j n - 1}) - \Phi_ {2} (\tau_ {i j n - 1}, v _ {i j}; \rho)) \bigr \}, \end{array}\tag{10}
$$

where $\tau _ { i j n } = \theta _ { n } - ( X _ { i j } \alpha + \nu _ { N } N _ { i j - 1 } )$ and $v _ { i j } = - ( Z _ { i j } \gamma +$ $\kappa _ { N } N _ { i j } + \kappa _ { L } L _ { i j - 1 } )$ , and $\Phi _ { 2 }$ is the CDF for the standard bivariate normal distribution. The marginal effects of independent variable X or Z on the sales leads L can be obtained in either of two ways, depending on the scale properties. If the independent variable is continuous, marginal effects can be calculated by evaluating the partial derivative of the conditional mean of L in (10) at the sample mean. If the independent variable is dichotomous, marginal effects may be calculated by evaluating the difference between the two conditional means and the sample means of other independent variables with the estimated model parameters. Those independent variables specified in Stage 1 will have an indirect marginal effect on sales leads, while those independent variables specified at Stage 2 will have a direct marginal effect. For those independent variables that enter both Stage 1 and Stage 2 (i.e., FSTAV), their total marginal effects on sales leads L will be the sum of the direct marginal effect from Stage 2 and an indirect effect from Stage 1, which is carried through the endogenous variable N and the random error correlation $\rho .$ The marginal effects are reported in Table 4. First, FSTAV has much higher marginal effect  0440	 on sales leads, which suggests that advertising characteristics surrogated by response latency have a stronger impact on sales leads than website characteristics. Second, these variables can affect sales leads in different ways. For instance, while the magazine’s shelf life SHELF has a significant indirect impact (0.002) only, response latency FSTAV has significant impact both indirectly and directly. Surprisingly, FSTAV’s indirect impact  0406	 is much greater than its direct impact <sub>−</sub>0034	 on generating desired system outcomes.

## 5. Conclusion

We proposed a two-stage conceptual and econometric model to jointly assess website promotion performance for pure online firms. To the best of the authors’ knowledge, this is the first study on website promotion assessment that investigates the effects of traditional media advertising and website presence in an integrated framework. As such, our research has several limitations. The testing of our hypothesis is based on a single study. More empirical research is needed to establish the generalization of the empirical findings. Second, we remained silent on impact of advertising content characteristics on generating website visits because of the research design and ad budget constraints. Third, the measurements we use in this study were limited by the technology available in 2000 as well as by the owner’s resistance to the use of cookies. We anticipate that better measurements will emerge as information technology continues to advance.

Our research also contributes to the e-commerce literature in important aspects. Two important managerial findings emerge from this empirical study of a pure online firm’s campaign to generate sales leads through print advertising. First, advertising and website characteristics affect sales leads in different ways. Some advertising characteristics, like single versus double issues of a magazine, influence sales leads indirectly via their effect on website visits and two-stage correlations. Some website characteristics, like average time per page, influence sales leads directly. Still other characteristics, like advertising response latency, affect sales leads both indirectly and directly. These findings generate insights for positioning ads in print vehicles as well as for website design for online firms. Second, some of the measurements we developed are directly actionable. For example, consumers spending more time per page should be treated differently from the rest of the visitors because they are more likely to generate desired system outcomes. Also, putting an RSVP at the top of a Web page generates more sales leads directly, while putting an ad on the right page of a magazine generates more website traffic, which consequently generates more sales leads.

Our joint two-stage econometric model offers several innovations that are important in the analysis of online data. First, the model is designed to deal with the simultaneity and censoring issues. These issues are intrinsic in the data structure of all pure online firms’ promotional campaigns. Our model demonstrates several ways to extend current discrete bivariate models (Greene 1998, Boyes et al. 1989): (1) it is a simultaneous bivariate model with censoring; (2) it is an ordered probit model in Stage 1 and a binary probit model Stage 2; (3) it is longitudinal. Second, our model specification is flexible. It allows the impact of advertising on desired system outcomes to be assessed separately as an indirect effect in Stage 1 via the website traffic and as a direct effect in Stage 2. This feature of our model provides better and more complete assessment of the promotional performance for online firms. Third, our approach permits the modeling of the relationships between website traffic and desired system outcomes in two different ways: as a coefficient of the observed website traffic and as a correlation of the unobserved errors. Fourth, our model can be used in situations in which survey research is not possible or is too costly. These conditions often hold in the case of new products with limited marketing budgets. The data required in our study illustrates this point. The advertising schedule and customer online shopping data are readily available at virtually no additional cost for online firms. In our application, we rely on customers’ IP addresses to identify unique visitors. This approach is appropriate for our particular application because products are high-priced collectors’ items and repeated visits are infrequent.<sup>12</sup> In our data set, repeated visits are between 1% and 4% within a given period and only 2% for the five periods aggregated together. In theory, IP addresses alone are not enough to guarantee the uniqueness. The impact of this imperfect identification on the estimate in our application can be an issue for websites that carry frequently purchased products. In such cases, cookie technology should be implemented to help identify unique visitors.

There are several promising ways to extend the current research. First, our model can be extended to encompass those net-enabled organizations that employ websites in their business strategies (Straub et al. 2002). For instance, Zufryden (2000) observes that a new film’s promotion strategy often consists of two components: (1) producers broadcast a trailer on television (or in newspapers) for an upcoming film and invite moviegoers to visit the film’s website, and (2) when moviegoers visit the film’s website they obtain detailed information about it (e.g., plot, stars, and trailers). Using aggregate data, Zufryden (2000) found that website visits have a significant positive influence on box-office performance. Second, information technology has made tracking of advertising effectiveness an important service for many organizations (e.g., www.hitslink.com). Our model can be extended to those firms with an online presence that employ multiple advertising vehicles to drive website traffic by simultaneously combining online with offline media. The opportunities to extend the research in this direction increase significantly with the rapid growth of consumer access to broadband and the shift of mass TV advertising to targeted streaming-video ads.

## Acknowledgments

The authors thank the 2001 ICIS Conference reviewers and audience and the 2002 Marketing Science Conference audience for providing valuable comments for an earlier version of this paper.

## Appendix

## A. The POS Model

In the model POS, we posit that a potential customer i arrives at the website following a Poisson distribution with rate $\lambda _ { i j }$ (per unit of time). Let the period length be $t _ { j }$ (number of days), then $N _ { i j }$ follows a Poisson distribution with rate $\lambda _ { i j } t _ { j }$ . Because $\lambda _ { i j } > 0 ,$ , we further posit that ln $\lambda _ { i j }$ is a linear function of some observable Stage 1 drivers $\dot { X } _ { i j }$ in the period (the conventional log-linear specification). Therefore, Equation (3) in the ORD model is replaced by

$$
\operatorname * {P r} (N _ {i j} = n) = \frac {(\lambda_ {i j} t _ {j}) ^ {n} e ^ {- \lambda_ {i j} t _ {j}}}{n !} \quad \mathrm{and}\tag{A1}
$$

$$
\ln \lambda_ {i j} = X _ {i j} \alpha + \nu_ {N} N _ {i j - 1}.
$$

Notice that $N _ { i j }$ is a count variable; it will be hard to directly specify the correlation of $N _ { i j }$ and $L _ { i j } ^ { * }$ Therefore, we first transfer the count variable $N _ { i j }$ into a continuous standard normal variable $\xi _ { i j }$ (e.g., van Ophem 2000). Let

$$
\tau_ {i j n} = \Phi^ {- 1} \left(\sum_ {k = 0} ^ {n} \operatorname * {P r} (N _ {i j} = k)\right) = \Phi^ {- 1} (\operatorname * {P r} (N _ {i j} \leq n)) \quad \text { and }\tag{A2}
$$

$$
\operatorname * {P r} (N _ {i j} = n) = \int_ {\tau_ {i j n - 1}} ^ {\tau_ {i j n}} \phi (\xi_ {i j}) d \xi_ {i j},
$$

where $\phi$ and  are the PDF and CDF of the standard normal distribution. In this way, the correlations of $\xi _ { i j }$ and $\eta _ { i j }$ will be specified just as in Equation (5) of the ORD model.

The likelihood function is formed similar to Equation (8) of the ORD model as

$$
\begin{array}{c} L L = \sum_ {i} \sum_ {j} \ln f (N _ {i j} = n, L _ {i j} = l) \big | _ {n \geq 1} \\ + \sum_ {i} \sum_ {j} \ln f (N _ {i j} = n, L _ {i j} = l) \big | _ {n = 0}, \end{array}\tag{A3}
$$

in which the first term is

$$
\begin{array}{l} \ln f (N _ {i j} = n, L _ {i j} = l) \big | _ {n \geq 1} \\ \quad = l \ln \operatorname * {P r} (N _ {i j} = n, L _ {i j} = 1) + (1 - l) \ln \operatorname * {P r} (N _ {i j} = n, L _ {i j} = 0) \\ \quad = l \ln [ (\Phi (\tau_ {i j n}) - \Phi_ {2} (\tau_ {i j n}, v _ {i j}; \rho_ {1})) \\ \quad \quad - (\Phi (u _ {i j n - 1}) - \Phi_ {2} (\tau_ {i j n - 1}, v _ {i j}; \rho_ {1})) ] \\ \quad + (1 - l) \ln [ \Phi_ {2} (\tau_ {i j n}, v _ {i j}; \rho_ {0}) - \Phi_ {2} (\tau_ {i j n - 1}, v _ {i j}; \rho_ {0}) ] \end{array} \tag {A4}
$$

where $\tau _ { i j n } = \theta _ { n } - ( X _ { i j } \alpha + \nu _ { N } N _ { i j - 1 } )$ and $v _ { i j } = - ( Z _ { i j } \gamma + \kappa _ { N } N _ { i j } +$ $\kappa _ { L } L _ { i j - 1 } )$ and $\Phi _ { 2 }$ is the CDF for standard bivariate normal distribution. The second term is

$$
\begin{array}{c} \ln f (N _ {i j} = n, L _ {i j} = l) \big | _ {n = 0} = \ln (\Phi (\tau_ {i j 0})) = \ln \Phi (\Phi^ {- 1} (e ^ {- \lambda_ {i j} t _ {j}})) \\ = \ln (e ^ {- \lambda_ {i j} t _ {j}}) = - \lambda_ {i j} t _ {j}. \end{array} \tag {A}\tag{A5}
$$

## B. The NBD Model

In this model, we generalize the POS model by introducing an unobserved heterogeneity effect $w _ { i j }$ (following a Gamma distribution) into the Poisson rate $\lambda _ { i j } \ ( \mathrm { e . g } { } ,$ ., Greene 2000),

$$
\begin{array}{c} \ln \mu_ {i j} = \ln \lambda_ {i j} + \ln w _ {i j} = X _ {i j} \alpha + \nu_ {N} N _ {i j - 1} + \ln w _ {i j} \quad \text { and } \\ g (w _ {i j}) = \frac {\theta^ {\theta}}{\Gamma (\theta)} e ^ {- \theta w _ {i j}} w _ {i j} ^ {\theta - 1}. \end{array}\tag{B1}
$$

This is the negative binomial distribution (NBD) for modeling the Stage 1 advertising response. Therefore, the NBD model is specified by replacing (A1) in the POS model by

$$
\begin{array}{c} \operatorname * {P r} (N _ {i j} = n) = \frac {\Gamma (\theta + n)}{\Gamma (n + 1) \Gamma (\theta)} r _ {i j} ^ {n} (1 - r _ {i j}) ^ {\theta} \quad \text { and } \\ r _ {i j} = \frac {\lambda_ {i j} t _ {j}}{\lambda_ {i j} t _ {j} + \theta}. \end{array}\tag{B2}
$$

The remaining specification of the model and the loglikelihood are similarly formed as in the POS model.

## C. The HUR Model

In this model, we assume that the zero outcome of the data generating process of visits for potential customer i in period $j , N _ { i j } ,$ , is qualitatively different from the positive ones (called hurdle Poisson model). A binary probability model determines whether a zero (with probability p) or a nonzero outcome (with probability 1 p) occurs. If the nonzero outcome occurs, it follows a truncated Poisson distribution with rate $\lambda _ { i j } .$ The HUR model is specified by replacing (A1) in the POS model by

$$
\begin{array}{c} \operatorname * {P r} (N _ {i j} = 0) = p, \quad 0 <   p <   1 \qquad \text { and } \\ \operatorname * {P r} (N _ {i j} = n) = \frac {(1 - p) (\lambda_ {i j} t _ {j}) ^ {n} e ^ {- \lambda_ {i j} t _ {j}}}{(1 - e ^ {- \lambda_ {i j} t _ {j}}) n !} \end{array}\tag{C1}
$$

where ln $\lambda _ { i j } = X _ { i j } \alpha + \nu _ { N } N _ { i j - 1 }$ if n > 0. The remaining specifications of the model and the log-likelihood are formed as in the POS model.

## References

Agarwal, Ritu, Viswanath Venkatesh. 2002. Assessing a firm’s Web presence: A heuristic evaluation procedure for the measurement of usability. Inform. Systems Res. 13(2) 168–186.

Blattberg, Robert C., Abel P. Jeuland. 1981. A micromodeling approach to investigate the advertising-sales relationship. Management Sci. 27(9) 988–1005.

Boyes, William, J. Dennis, L. Hoffman, Stuart A. Low. 1989. An econometric analysis of the bank credit scoring problem. J. Econometrics 40 1–14.

Bronnenberg, Bart. 1998. Advertising frequency decisions in a discrete Markov process under a budget constraint. J. Marketing Res. XXXV(August) 399–406.

Broussard, Gerard. 2000. How advertising frequency can work to build online advertising effectiveness. Internat. J. Market Res. 42(4) 439–457.

Bucklin, Randolph E., Catarina Sismeiro. 2003. A model of Web site browsing behavior estimated on clickstream data. J. Marketing Res. 40(3) 249–267.

Chen, Pei-Yu, Lorin M. Hitt. 2002. Measuring switching costs and their determinants in Internet enabled businesses: A study of the online brokerage industry. Inform. Systems Res. 13(3) 255–274.

Clarke, Darral G. 1976. Econometric measurement of the duration of advertising effect on sales. J. Marketing Res. XIII(November) 345–357.

Degeratu, Alexandru, Arvind Rangaswamy, Jianan Wu. 2000. Consumer choice behavior in online and traditional supermarkets: The effects of brand name, price, and other search attributes. Internat. J. Res. Marketing 17(1) 55–78.

Devaraj, Sarv, Ming Fan, Rajiv Kohli. 2002. Antecedents of B2C channel satisfaction and preference: Validating ecommerce metrics. Inform. Systems Res. 13(3) 316–333.

Diamond, Daniel S. 1968. A quantitative approach to magazine advertisement format selection. J. Marketing Res. V(November) 376–386.

Ebbinghaus, H. 1913. Memory. Columbia University Press, New York.

Edell, Julie A., Richard Staelin. 1983. The information processing of pictures in print advertisements. J. Consumer Res. 10(June) 45–61.

Fazio, Russell. 1986. How do attitudes guide behavior? Robert M. Sorrentino, E. Thomas Higgins, eds. The Handbook of Motivation and Cognition: Foundations of Social Behavior. Lawrence Erlbaum, Hillsdale, NJ, 204–243.

Fazio, Russell. 1990. A practical guide to the use of response latency in social psychological research. C. Hendrick, M. S. Clark, eds. Review of Personality and Social Psychology, Vol. 11. Sage Publications, Beverly Hills, CA, 74–97.

Friedman, Mildred. 1982. De Stijl: 1917–1931 Visions of Utopia. Abbeville Press, New York.

Greene, William H. 1998. Gender economics courses in liberal arts colleges: Further results. J. Econom. Ed. 29(4) 291–300.

Greene, William H. 2000. Econometric Analysis, 4th ed. Prentice Hall, Upper Saddle River, NJ.

Gupta, Sunil. 1988. Impact of sales promotions on when, what, and how much to buy. J. Marketing Res. XXV(Nov) 342–355.

Haaijer, Rinus, Wagner Kamakura, Michel Wedel. 2000. Response latency in the analysis of conjoint choice experiments. J. Marketing Res. XXXVII(August) 376–382.

Halliday, Jean. 2001. Ford finds sales leads productive. Advertising Age. http://www.adage.com/interactive/articles/20010122/ article1.html.

Hanssens, Dominique M., Barton A. Weitz. 1980. The effectiveness of industrial print advertisements across product categories. J. Marketing Res. XVII(August) 294–306.

Hoffman, Donna L., Thomas P. Novak. 2000. How to acquire customers on the Web. Harvard Bus. Rev. 78(3) 179–185.

Holbrook, M. B., D. R. Lehmann. 1980. Form versus content in predicting starch scores. J. Advertising Res. 20(4) 53–62.

Hoque, Abeery Y., Gerald L. Lohse. 1999. An information search cost perspective for designing interfaces for electronic commerce. J. Marketing Res. XXXVI(August) 387–394.

Keller, Kevin L. 1991. Memory and evaluation effects in competitive advertising environment. J. Consumer Res. 17(4) 463–476.

Kotler, Philip. 1991. Marketing Management: Analysis, Planning, Implementation, and Control, 7th ed. Prentice-Hall, Englewood Cliffs, NJ.

Koufaris, Marios. 2002. Applying the technology acceptance model and flow theory to online consumer behavior. Inform. Systems Res. 13(2) 205–223.

Kraut, R., T. Mukhopadhyay, J. Szczypula, S. Kiesler, B. Scherlis. 2000. Information and communication: Alternative uses of the Internet in households. Inform. Systems Res. 10 287–303.

Little, John. 1979. Aggregate advertising models: The state of the art. Oper. Res. 27(4) 629–667.

Mahajan, Vijay, Eitan Muller. 1986. Advertising pulsing policies for generating awareness for new products. Marketing Sci. 5 89–106.

Moe, Wendy W., Peter Fader. 2004. Dynamic conversion behavior at e-commerce sites. Management Sci. 50(3) 326–335.

Naccarato, John L., Kimberly A. Neuendorf. 1998. Content analysis as a predictive methodology: Recall, readership, and evaluations of business-to-business print advertising. J. Advertising Res. 38(3) 19–33.

Naik, Prasad A., Murali K. Mantrala, Alan G. Sawyer. 1998. Planning media schedules in the presence of dynamic advertising quality. Marketing Sci. 17(3) 214–235.

Nerlove, Marc, Kenneth Arrow. 1962. Optimal advertising policy under dynamic conditions. Economica 19(May) 129–142.

Palmer, Jonathan W. 2002. Web site usability, design, and performance metrics. Inform. Systems Res. 13(2) 151–167.

Punj, Girish N., Richard Staelin. 1983. A model of consumer information search behavior for new automobiles J. Consumer Res. 9(4) 366–381.

Sasieni, Maurice W. 1971. Optimal advertising expenditure. Man agament Sci. 18(4, Part 2) 64–72.

Straub, Detmar W., Donna L. Hoffman, Bruce W. Weber, Charles Steinfield. 2002. Toward new metrics for net-enhanced organizations. Inform. Systems Res. 13(3) 227–238.

Strong, E. C. 1974. The use of field experimental observations in estimating advertising recall. J. Marketing Res. 11(November) 369–378.

Telang, Rahul, Tridas Mukhopadhyay, Ronald T. Wilcox. 2001. An empirical analysis of the antecedents of Internet search engine choice. Working paper, Carnegie Mellon University, Pittsburgh, PA.

Tybjee, Tyzoon T. 1979. Response time, conflict, and involvement in brand choice. J. Consumer Res. 6(December) 295–304.

Urban, Glen L., Fareena Sultan, William J. Qualls. 2000. Placing trust at the center of your Internet strategy. MIT Sloan Management Rev. 42(1) 39–48.

Van Ophem, Hans. 2000. Modeling selectivity in count-data models. J. Bus. Econom. Statist. 18(4) 503–511.

Wu, Jianan, Arvind Rangaswamy. 2003. A fuzzy set model of search and consideration with an application to an online market. Marketing Sci. 22(3) 411–434.

Zufryden, Fred. 2000. New film website promotion and box-office performance. J. Advertising Res. 40(1) 55.
